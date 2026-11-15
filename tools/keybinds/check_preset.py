from collections import defaultdict
from pathlib import Path
import argparse
import hashlib
import json
from build_preset import HERE, PRESET, build, mappings


def check(mods=None):
    raw = PRESET.read_bytes()
    if raw != build().encode("utf-8"):
        raise ValueError("Regenerate launcher/controls-preset.txt")
    rows = mappings(raw.decode("utf-8"))
    base = mappings((HERE / "native-options.txt").read_text(encoding="utf-8"))
    for name, value in base.items():
        if name == "key_key.tagtooltips.show_tag_tooltip":
            break
        if rows[name] != value:
            raise ValueError(f"Vanilla input changed: {name}")
    occupied = defaultdict(list)
    for name, value in rows.items():
        key = value.split(":", 1)[0]
        if key != "key.keyboard.unknown":
            occupied[key.removeprefix("key.keyboard.").removeprefix("key.")].append((name, value))
    review = json.loads((HERE / "shared-inputs.json").read_bytes())
    actual = {key: dict(values) for key, values in occupied.items() if len(values) > 1}
    if actual != review:
        changed = sorted(key for key in actual.keys() | review.keys() if actual.get(key) != review.get(key))
        raise ValueError(f"Unreviewed shared inputs: {', '.join(changed)}")
    pin = hashlib.sha256(raw).hexdigest()
    if mods:
        source = json.loads((HERE.parents[1] / "library/loaded-mods.json").read_bytes())
        for path, expected in source["sourceJars"].items():
            file = mods / Path(path).name
            with file.open("rb") as stream:
                if hashlib.file_digest(stream, "sha256").hexdigest() != expected:
                    raise ValueError(f"JAR differs from native inventory: {path}")
    print(f"{len(rows)} mappings, {sum(map(len, occupied.values()))} bound, {len(actual)} reviewed shared physical inputs, SHA-256 {pin}")
    return pin


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mods", type=Path)
    check(parser.parse_args().mods)
