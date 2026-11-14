from __future__ import annotations

import argparse
import hashlib
import os
import shutil
import subprocess
import tempfile
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SHA256_HQM = "9b62b6dedfd51591b64ae3476c19b3f0fd9474f4cf030a5d875370d130c30865"
FORGE_INPUTS = {
    "net/minecraft/client/1.20.1-20230612.114412/client-1.20.1-20230612.114412-srg.jar":
        "e2e940fe7ca0a9fba5a5c11ad2cf3e2f7df91bbf51d12af22cdde7af18adc344",
    "net/minecraftforge/javafmllanguage/1.20.1-47.4.20/javafmllanguage-1.20.1-47.4.20.jar":
        "fb659dd963f14b2c34c2b935dcf1f7f40e8018c6900deaa9c673229893bb0218",
    "net/minecraftforge/mergetool/1.1.5/mergetool-1.1.5-api.jar":
        "39d9a3d9277c1402b8e7b97f917ce278241cf1796312aec85b87f19a376dd99a",
    "org/spongepowered/mixin/0.8.5/mixin-0.8.5.jar":
        "ca15a907e4d1f6b38cefed51d7df96a83347dcfb0bc8ced53111519e991d887d",
}
JAR_NAME = "desolate-hqm-localization-1.0.0.jar"
MANIFEST = b"Manifest-Version: 1.0\r\nMixinConfigs: desolate_hqm_localization.mixins.json\r\n\r\n"


def checked(path, pin):
    with path.open("rb") as file:
        if hashlib.file_digest(file, "sha256").hexdigest() != pin:
            raise ValueError(f"Unexpected Forge build input: {path}")
    return str(path)


def save(archive, name, data):
    member = zipfile.ZipInfo(name)
    member.create_system = 3
    member.external_attr = 0o100644 << 16
    archive.writestr(member, data)


def main():
    parser = argparse.ArgumentParser(description="Build the Desolate Planet client-side HQM localization mod.")
    parser.add_argument("--shared-libraries", required=True, type=Path)
    parser.add_argument("--hqm-jar", required=True, type=Path)
    parser.add_argument("--output-directory", required=True, type=Path)
    parser.add_argument("--javac", default=shutil.which("javac"))
    args = parser.parse_args()
    if not args.javac:
        parser.error("A full JDK is required.")
    output = args.output_directory.resolve()
    run = next((parent for parent in (output, *output.parents)
                if parent.parent.name == "agent-runs" and parent.parent.parent.name == "artifacts"), None)
    if run is None or not (run / "RUN.json").is_file():
        parser.error("Output must be within a marked artifacts/agent-runs directory.")
    classpath = [checked(args.hqm_jar.resolve(), SHA256_HQM)]
    classpath += [checked(args.shared_libraries.resolve() / relative, pin) for relative, pin in FORGE_INPUTS.items()]
    output.mkdir(parents=True, exist_ok=True)
    target = output / JAR_NAME
    if target.exists():
        parser.error(f"Use an empty output directory: {target}")
    sources = sorted((ROOT / "src/main/java").rglob("*.java"))
    resources = ROOT / "src/main/resources"
    with tempfile.TemporaryDirectory(prefix="compile-", dir=output) as temporary:
        classes = Path(temporary) / "classes"
        classes.mkdir()
        subprocess.run([
            args.javac, "--release", "17", "-encoding", "UTF-8", "-g:none", "-proc:none",
            "-classpath", os.pathsep.join(classpath), "-d", str(classes), *map(str, sources)
        ], check=True)
        built = Path(temporary) / JAR_NAME
        with zipfile.ZipFile(built, "x") as archive:
            save(archive, "META-INF/MANIFEST.MF", MANIFEST)
            for path in sorted(resources.rglob("*")):
                if path.is_file():
                    save(archive, path.relative_to(resources).as_posix(), path.read_bytes().replace(b"\r\n", b"\n"))
            for path in sorted(classes.rglob("*.class")):
                save(archive, path.relative_to(classes).as_posix(), path.read_bytes())
        built.replace(target)
    print(f"{target} ({target.stat().st_size} bytes, SHA-256 {hashlib.sha256(target.read_bytes()).hexdigest()})")


if __name__ == "__main__":
    main()
