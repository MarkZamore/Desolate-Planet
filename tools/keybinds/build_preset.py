from pathlib import Path
import json
import re

HERE = Path(__file__).resolve().parent
PRESET = HERE.parents[1] / "launcher/controls-preset.txt"
KEY = re.compile(r"key_[^:\s]+:key\.(?:keyboard|mouse)\.[a-z0-9.]+(?::(?:SHIFT|CONTROL|ALT))?")


def mappings(text):
    result = {}
    for raw in text.splitlines():
        if not KEY.fullmatch(raw):
            raise ValueError(f"Invalid controls row: {raw!r}")
        name, value = raw.split(":", 1)
        if name in result:
            raise ValueError(f"Duplicate mapping: {name}")
        result[name] = value
    return result


def build():
    stock = mappings((HERE / "native-options.txt").read_text(encoding="utf-8"))
    changes = json.loads((HERE / "overrides.json").read_bytes())
    if not changes.keys() <= stock.keys():
        raise ValueError(f"Unregistered mappings: {changes.keys() - stock.keys()}")
    for name, value in changes.items():
        stock[name] = "key.keyboard." + value
    return "".join(f"{name}:{value}\n" for name, value in stock.items())


if __name__ == "__main__":
    PRESET.write_bytes(build().encode("utf-8"))
