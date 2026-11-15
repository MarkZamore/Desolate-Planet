"""Publish only the reviewed controls layer over the current pack payload."""

from datetime import datetime, timezone
from hashlib import sha256
from io import BytesIO
import json
import os
from pathlib import Path
import subprocess
import time
from urllib.request import Request, urlopen
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

from build_preset import PRESET
from check_preset import check

REPO = "MarkZamore/Desolate-Planet"
TAG = "pack-latest"
PATH = "launcher/controls-preset.txt"
BASE = f"https://github.com/{REPO}/releases/download/{TAG}/"


def gh(*args):
    return subprocess.check_output(["gh", *args])


def read(name):
    request = Request(BASE + name + f"?revision_check={time.time_ns()}", headers={"Cache-Control": "no-cache"})
    with urlopen(request, timeout=70) as response:
        return response.read()


def pin(data):
    return {"sizeBytes": len(data), "sha256": sha256(data).hexdigest()}


def encode(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode()


def zip_bytes(members):
    target = BytesIO()
    with ZipFile(target, "w") as archive:
        for name, data in sorted(members.items()):
            archive.writestr(ZipInfo(name), data, compress_type=ZIP_DEFLATED)
    return target.getvalue()


def main():
    expected = check()
    preset = PRESET.read_bytes()
    revision = os.environ["GITHUB_SHA"]
    previous = read("pack-manifest.json")
    manifest = json.loads(previous)
    if manifest["packId"] != "minecraft-19" or manifest["loader"] != {"type": "forge", "version": "47.4.20"}:
        raise ValueError("Unexpected pack or platform")
    if manifest["revision"] == revision:
        row, = [row for row in manifest["files"] if row["path"] == PATH]
        if row["sha256"] != expected:
            raise ValueError("This revision is already published with a different preset")
        return

    allowed = {".github/workflows/publish.yml", ".gitattributes", PATH, "tools/qa/full-book-locales.json"}
    paths = subprocess.check_output(["git", "diff", "--name-only", manifest["revision"], revision], text=True)
    if any(not (name in allowed or name.startswith("tools/keybinds/")) for name in paths.splitlines()):
        raise ValueError("Source has game payload changes requiring normal pack preparation")
    old_tag = json.loads(gh("api", f"repos/{REPO}/git/ref/tags/{TAG}"))["object"]["sha"]
    if old_tag != manifest["revision"]:
        raise ValueError("The public tag and manifest revisions differ")

    library = manifest["library"]
    library_bytes = read(library["name"])
    if any(library[k] != v for k, v in pin(library_bytes).items()):
        raise ValueError("Public library differs from the manifest")
    with ZipFile(BytesIO(library_bytes)) as archive:
        if sorted(archive.namelist()) != ["library.json", "preview.jpg"]:
            raise ValueError("Unexpected library members")
        library_metadata = json.loads(archive.read("library.json"))
        if library_metadata["revision"] != old_tag:
            raise ValueError("Public library revision differs")
        library_metadata["revision"] = revision
        next_library = zip_bytes({"library.json": encode(library_metadata), "preview.jpg": archive.read("preview.jpg")})

    old_controls = [asset for asset in manifest["assets"] if PATH in asset["covers"]]
    if any(asset["covers"] != [PATH] for asset in old_controls):
        raise ValueError("Controls must be isolated in a single-file archive")
    controls = zip_bytes({PATH: preset})
    controls_pin = pin(controls)
    name = f"r-{controls_pin['sha256'][:12]}-launcher-controls.zip"
    manifest["assets"] = sorted(
        [a for a in manifest["assets"] if a not in old_controls] +
        [{"name": name, "kind": "zipRoot", "covers": [PATH], **controls_pin}], key=lambda a: a["name"])
    manifest["files"] = sorted([row for row in manifest["files"] if row["path"] != PATH] +
                               [{"path": PATH, **pin(preset)}], key=lambda row: row["path"])
    if sorted(p for a in manifest["assets"] for p in a["covers"]) != [r["path"] for r in manifest["files"]]:
        raise ValueError("Asset coverage differs from file inventory")
    library_pin = pin(next_library)
    library_name = f"library-{library_pin['sha256']}.zip"
    manifest["library"] = {"name": library_name, "revision": revision, **library_pin}
    manifest["revision"] = revision
    seconds = int(subprocess.check_output(["git", "show", "-s", "--format=%ct", revision]))
    manifest["generatedAtUtc"] = datetime.fromtimestamp(seconds, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    assets = json.loads(gh("release", "view", TAG, "--repo", REPO, "--json", "assets"))["assets"]
    published = {asset["name"]: asset for asset in assets}
    for asset in manifest["assets"]:
        if asset["name"] == name:
            continue
        remote = published[asset["name"]]
        if (remote["size"], remote["digest"]) != (asset["sizeBytes"], "sha256:" + asset["sha256"]):
            raise ValueError(f"Unverified inherited asset {asset['name']}")

    work = Path(os.environ["RUNNER_TEMP"]) / "desolate-controls"
    work.mkdir()
    for asset, data in [(name, controls), (library_name, next_library)]:
        file = work / asset
        file.write_bytes(data)
        remote = published.get(asset)
        if not remote:
            gh("release", "upload", TAG, str(file), "--repo", REPO)
        if read(asset) != data:
            raise ValueError(f"Downloaded bytes differ: {asset}")
    if read("pack-manifest.json") != previous:
        raise ValueError("Public manifest changed during publication")
    output = work / "pack-manifest.json"
    output.write_bytes(encode(manifest))
    gh("release", "upload", TAG, str(output), "--clobber", "--repo", REPO)
    gh("api", "--method", "PATCH", f"repos/{REPO}/git/refs/tags/{TAG}", "-f", f"sha={revision}", "-F", "force=false")
    gh("release", "edit", TAG, "--target", revision, "--repo", REPO)
    if read("pack-manifest.json") != output.read_bytes():
        raise ValueError("Fresh public manifest differs")
    with ZipFile(BytesIO(read(name))) as archive:
        if archive.namelist() != [PATH] or pin(archive.read(PATH))["sha256"] != expected:
            raise ValueError("Public preset hash or archive members differ")
    print(f"Published {revision} with {PATH} SHA-256 {expected}")


if __name__ == "__main__":
    main()
