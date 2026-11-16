"""Publish the reviewed client files over the current pack payload."""

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
WARNING_SCRIPT = "kubejs/client_scripts/lanmc_multiplayer_warning.js"
OWNERSHIP = "launcher/pack-owned.txt"
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
    root = PRESET.parents[1]
    files = {path: (root / path).read_bytes() for path in (PATH, WARNING_SCRIPT, OWNERSHIP)}
    recipe = json.loads((root / "tools/overlay.json").read_bytes())
    locked_script, = recipe["clientScripts"]["files"]
    if locked_script != {"path": WARNING_SCRIPT, **pin(files[WARNING_SCRIPT])}:
        raise ValueError("Warning script differs from its pack policy pin")
    revision = os.environ["GITHUB_SHA"]
    previous = read("pack-manifest.json")
    manifest = json.loads(previous)
    if manifest["packId"] != "minecraft-19" or manifest["loader"] != {"type": "forge", "version": "47.4.20"}:
        raise ValueError("Unexpected pack or platform")
    current_files = {row["path"]: row for row in manifest["files"]}
    lock = json.loads((root / "tools/upstream-lock.json").read_bytes())
    dependencies = {(row["projectId"], row["fileId"]): row for row in lock["files"] if row["required"]}
    for dependency in recipe["clientScripts"]["dependencies"]:
        locked = dependencies[dependency["projectId"], dependency["fileId"]]
        public = current_files[locked["path"]]
        if any(public[key] != locked[key] for key in ("sizeBytes", "sha256")):
            raise ValueError(f"Public client script dependency differs: {locked['path']}")
    if manifest["revision"] == revision:
        if {row["path"]: row["sha256"] for row in manifest["files"] if row["path"] in files} != {
            path: pin(data)["sha256"] for path, data in files.items()
        }:
            raise ValueError("This revision is already published with different client files")
        return

    ownership_asset, = (asset for asset in manifest["assets"] if OWNERSHIP in asset["covers"])
    old_ownership = read(ownership_asset["name"])
    if any(ownership_asset[key] != value for key, value in pin(old_ownership).items()):
        raise ValueError("Public ownership archive differs from the manifest")
    with ZipFile(BytesIO(old_ownership)) as archive:
        previous_paths = archive.read(OWNERSHIP).decode().splitlines()
    current_paths = files[OWNERSHIP].decode().splitlines()
    if current_paths != sorted(set(previous_paths) | {WARNING_SCRIPT}):
        raise ValueError("The ownership update must only add the warning script")

    allowed = {".github/workflows/publish.yml", ".gitattributes", *files,
               "tools/qa/full-book-locales.json", "tools/overlay.json", "README.md"}
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

    changed = {path: data for path, data in files.items()
               if current_files.get(path) != {"path": path, **pin(data)}}
    old_assets = [asset for asset in manifest["assets"] if set(asset["covers"]) & changed.keys()]
    if any(len(asset["covers"]) != 1 for asset in old_assets):
        raise ValueError("Expected single-file archives for the reviewed client files")
    new_assets = []
    new_payloads = {}
    suffixes = {PATH: "launcher-controls", WARNING_SCRIPT: "multiplayer-warning", OWNERSHIP: "launcher-owned"}
    for path, contents in changed.items():
        data = zip_bytes({path: contents})
        archive_pin = pin(data)
        name = f"r-{archive_pin['sha256'][:12]}-{suffixes[path]}.zip"
        new_assets.append({"name": name, "kind": "zipRoot", "covers": [path], **archive_pin})
        new_payloads[name] = data
    manifest["assets"] = sorted(
        [a for a in manifest["assets"] if a not in old_assets] + new_assets, key=lambda a: a["name"])
    manifest["files"] = sorted([row for row in manifest["files"] if row["path"] not in files] +
                               [{"path": path, **pin(data)} for path, data in files.items()], key=lambda row: row["path"])
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
        if asset["name"] in new_payloads:
            continue
        remote = published[asset["name"]]
        if (remote["size"], remote["digest"]) != (asset["sizeBytes"], "sha256:" + asset["sha256"]):
            raise ValueError(f"Unverified inherited asset {asset['name']}")

    work = Path(os.environ["RUNNER_TEMP"]) / "desolate-controls"
    work.mkdir()
    for asset, data in {**new_payloads, library_name: next_library}.items():
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
    for asset in new_assets:
        path, = asset["covers"]
        with ZipFile(BytesIO(read(asset["name"]))) as archive:
            if archive.namelist() != [path] or archive.read(path) != files[path]:
                raise ValueError(f"Public file or archive members differ: {path}")
    print(f"Published {revision} with {PATH} SHA-256 {expected} and {WARNING_SCRIPT} SHA-256 {pin(files[WARNING_SCRIPT])['sha256']}")


if __name__ == "__main__":
    main()
