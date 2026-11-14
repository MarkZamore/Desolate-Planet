[CmdletBinding()]
param(
    [Parameter(Mandatory)][string] $LauncherRepo,
    [Parameter(Mandatory)][string] $RunDirectory,
    [Parameter(Mandatory)][string] $JdkDirectory,
    [ValidatePattern('^[a-z0-9-]{1,36}$')][string] $BuildLabel,
    [switch] $WithBookLocales
)

$ErrorActionPreference = 'Stop'
$workspace = (Resolve-Path -LiteralPath $LauncherRepo).Path
$runs = (Resolve-Path -LiteralPath (Join-Path $workspace 'artifacts/agent-runs')).Path
$run = (Resolve-Path -LiteralPath $RunDirectory).Path
if ([IO.Path]::GetDirectoryName($run) -ine $runs -or !(Test-Path -LiteralPath "$run/RUN.json" -PathType Leaf)) {
    throw 'Use a marked QA run within artifacts/agent-runs.'
}
$owner = Get-Content -LiteralPath "$run/RUN.json" -Raw | ConvertFrom-Json
if ($owner.owner -cne 'Codex') { throw 'The selected run is not owned by this QA task.' }
$work = Join-Path $run $(if ($WithBookLocales) { 'respawn-book-probe' } else { 'respawn-probe' })
if ($BuildLabel) { $work += "-$BuildLabel" }
if (Test-Path -LiteralPath $work) { throw 'The respawn probe output already exists.' }
$sourcePath = Join-Path $workspace 'tools/PackData/CurseForge/Forge118SteamQaAgent.java'
$source = [IO.File]::ReadAllText($sourcePath)
$runBody = $source.IndexOf('            checkWindowTitle("world_before_steam");')
if ($runBody -lt 0) { throw 'Review the QA harness against the current common agent.' }
$runFinish = $source.IndexOf('        } catch (Exception failure) {', $runBody)
if ($runBody -lt 0 -or $runFinish -lt 0 -or !$source.Contains('private void checkPermissions() throws Exception') -or
    !$source.Contains('waitUntil("Minecraft instance", 180') -or !$source.Contains('waitUntil("world join", 180')) {
    throw 'Review the QA harness against the current common agent.'
}
$source = $source.Substring(0, $runBody) + @'
            verifyRespawn();
            saveWorld();
            event("complete", Map.of("nativeRespawn", "PASS", "nativeSteam", "NOT RUN"));

'@ + $source.Substring($runFinish)
$source = $source.Replace('TimeUnit.MINUTES.toNanos(11)', 'TimeUnit.MINUTES.toNanos(29)')
$source = $source.Replace('waitUntil("Minecraft instance", 180', 'waitUntil("Minecraft instance", 1200')
$source = $source.Replace('waitUntil("world join", 180', 'waitUntil("world join", 700')
$source = $source.Replace('String suffix = System.getProperty(PREFIX + "worldSuffix", "");', @'
String suffix = System.getProperty(PREFIX + "worldSuffix", "");
        require("1.20.1".equals(minecraftVersion) && "Respawn".equals(suffix),
            "The respawn probe only operates on its reserved Forge 1.20.1 test world.");
'@)
$source = $source.Replace('    private void checkPermissions() throws Exception {',
    [IO.File]::ReadAllText((Join-Path $PSScriptRoot 'RespawnProbe.java.inc')) + [char]10 +
    '    private void checkPermissions() throws Exception {')
if ($WithBookLocales) {
    $source = $source.Replace('            verifyRespawn();', "            verifyBookLocales();`n            verifyRespawn();")
    $source = $source.Replace('    private void checkPermissions() throws Exception {',
        [IO.File]::ReadAllText((Join-Path $PSScriptRoot 'BookLocaleProbe.java.inc')) + [char]10 +
        '    private void checkPermissions() throws Exception {')
}

$javac = Join-Path $JdkDirectory 'bin/javac.exe'
$jar = Join-Path $JdkDirectory 'bin/jar.exe'
if (!(Test-Path -LiteralPath $javac) -or !(Test-Path -LiteralPath $jar)) { throw 'Use a full JDK.' }
$classes = New-Item -ItemType Directory -Path (Join-Path $work 'classes')
$javaFile = Join-Path $work 'Forge118SteamQaAgent.java'
$manifest = Join-Path $work 'MANIFEST.MF'
$output = Join-Path $work 'forge-respawn-qa.jar'
[IO.File]::WriteAllText($javaFile, $source)
@('Manifest-Version: 1.0','Premain-Class: lanminecraft.qa.Forge118SteamQaAgent','') | Set-Content -LiteralPath $manifest -Encoding ascii
& $javac --release 17 -encoding UTF-8 -d $classes.FullName $javaFile
if ($LASTEXITCODE -ne 0) { throw 'Respawn probe compilation failed.' }
& $jar --create --file $output --manifest $manifest --date 1980-01-01T00:00:02Z -C $classes.FullName lanminecraft
if ($LASTEXITCODE -ne 0) { throw 'Respawn probe packaging failed.' }
Write-Output $output
