"""Check a localized AE2 GuideME book against the exact upstream Forge build."""

import argparse
from collections import Counter
from hashlib import file_digest
from pathlib import Path
import posixpath
import re
from urllib.parse import unquote, urlsplit
from zipfile import ZipFile

GUIDE_ROOT = "assets/ae2/ae2guide/"
JAR_SHA256 = "fbfee05c6674cb6b00fe425e945ca4818d41eb34069b60dcb4a36221a0390fcc"
TRANSLATED_ROOT = Path(__file__).resolve().parents[2] / "kubejs/assets/ae2/ae2guide/_ru_ru"
INLINE_CODE = re.compile(r"(?<![\x60])\x60([^\x60\n]+)\x60(?![\x60])")
LINK = re.compile(r"\]\(([^()\s]+)\)")
TAG = re.compile(r"<(/?[a-zA-Z][\w.-]*)(?=\s|/?>)([^<>]*?)>", re.S)
ATTRIBUTE = re.compile(r"""([\w:.-]+)=(?:"([^"]*)"|'([^']*)'|(\{[^{}]*\}))""", re.S)
HEADING = re.compile(r"^#{1,6}\s+(.+)$", re.M)
EXPLICIT_ANCHOR = re.compile(r"""<a\s+name=["']([^"']+)["']""")
INLINE_TAGS = {"a", "ItemLink", "ItemIcon"}


def front_matter(text):
    parts = text.split("---", 2)
    if len(parts) != 3 or parts[0]:
        raise ValueError("Guide page must begin with YAML front matter")
    return "\n".join(
        line.rstrip() for line in parts[1].splitlines()
        if not re.match(r"^\s*title:", line)
    ).strip()


def targets(text):
    return Counter([*LINK.findall(text), *re.findall(r'\bhref="([^"]+)"', text)])


def tags(text):
    without_code = INLINE_CODE.sub("", text)
    structure = []
    inline = Counter()
    for match in TAG.finditer(without_code):
        name, attributes = match.groups()
        if name in {"/a", "br"}:  # Anchor aliases and harmless line breaks are valid.
            continue
        pairs = tuple(sorted((key, double or single or expression or "")
                             for key, double, single, expression in ATTRIBUTE.findall(attributes)))
        if name == "a" and any(key == "name" for key, _ in pairs):
            continue
        style = "self-closing" if attributes.rstrip().endswith("/") else "normal"
        token = (name, style, pairs)
        if name in INLINE_TAGS:
            inline[token] += 1
        else:
            structure.append(token)
    return structure, inline


def anchors(text):
    # GuideME 20.1.15 AnchorIndexer normalizes visible headings this way.
    inferred = {re.sub(r"\s+", "-", heading.strip().lower()) for heading in HEADING.findall(text)}
    return inferred | set(EXPLICIT_ANCHOR.findall(text))


def broken_references(pages, resources):
    anchor_index = {name: anchors(text) for name, text in pages.items()}
    broken = []
    for name, text in pages.items():
        for raw in sorted(targets(text)):
            uri = urlsplit(raw)
            if uri.scheme or uri.netloc:
                continue
            path = unquote(uri.path)
            if path.startswith("/"):
                resolved = posixpath.normpath(path.lstrip("/"))
            else:
                resolved = posixpath.normpath(posixpath.join(posixpath.dirname(name), path)) if path else name
            if resolved not in pages and resolved not in resources:
                broken.append((name, raw, "missing path"))
            elif uri.fragment and resolved in pages and unquote(uri.fragment) not in anchor_index[resolved]:
                broken.append((name, raw, "missing anchor"))
    return set(broken)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("jar", type=Path, help="Original Applied Energistics 2 Forge 15.4.10 JAR")
    parser.add_argument("--translations", type=Path, default=TRANSLATED_ROOT)
    parser.add_argument("--partial", action="store_true", help="Use English for pages missing while translating")
    args = parser.parse_args()

    with args.jar.open("rb") as jar:
        if file_digest(jar, "sha256").hexdigest() != JAR_SHA256:
            parser.error(f"Expected exact upstream JAR SHA-256 {JAR_SHA256}")

    with ZipFile(args.jar) as bundle:
        resources = {
            entry.removeprefix(GUIDE_ROOT) for entry in bundle.namelist()
            if entry.startswith(GUIDE_ROOT) and not entry.endswith("/")
        }
        english = {
            name: bundle.read(GUIDE_ROOT + name).decode("utf-8")
            for name in sorted(resources) if name.endswith(".md") and not name.startswith("_")
        }

    russian = {
        file.relative_to(args.translations).as_posix(): file.read_text(encoding="utf-8")
        for file in args.translations.rglob("*.md")
    }
    failures = [
        *(f"{name}: no Russian page" for name in sorted(english.keys() - russian.keys()) if not args.partial),
        *(f"{name}: page is absent from the pinned JAR" for name in sorted(russian.keys() - english.keys())),
    ]
    for name in sorted(english.keys() & russian.keys()):
        original, translated = english[name], russian[name]
        if not re.search(r"[Ѐ-ӿ]", translated):
            failures.append(f"{name}: no Russian text")
        if front_matter(original) != front_matter(translated):
            failures.append(f"{name}: changed front matter other than the display title")
        if tags(original) != tags(translated):
            failures.append(f"{name}: changed MDX tags, bindings, or ordering")
        if targets(original) != targets(translated):
            failures.append(f"{name}: changed Markdown link or image targets")
        if not set(EXPLICIT_ANCHOR.findall(original)) <= anchors(translated):
            failures.append(f"{name}: lost an explicit source anchor")

    inherited = broken_references(english, resources)
    current = broken_references({**english, **russian}, resources)
    failures.extend(f"{file}: {reason}: {href}" for file, href, reason in sorted(current - inherited))
    for file, href, reason in sorted(inherited & current):
        print(f"Inherited from English: {file}: {reason}: {href}")
    if failures:
        parser.exit(1, "\n".join(failures) + "\n")
    print(f"Verified {len(russian)}/{len(english)} Russian pages with no new broken references.")


if __name__ == "__main__":
    main()
