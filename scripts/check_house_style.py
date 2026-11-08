#!/usr/bin/env python3
"""House-style and listing checks for the Career Helper repository.

Runs in CI and locally (Python 3.12 or later):

    python3 scripts/check_house_style.py

Checks:
1. No em dashes or en dashes in any text file.
2. No emoji or emoji-style markers (ticks, crosses, warning signs, checkboxes).
3. plugin.json and marketplace.json parse, and their versions match.
4. The plugin folder holds no binary files other than images, and no OS junk files.
5. Every SKILL.md, command, and agent starts with YAML front matter that has a description.

Exits non-zero and lists every problem found.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "career-helper"

TEXT_SUFFIXES = {".md", ".html", ".json", ".py", ".yml", ".yaml", ".txt"}
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}
JUNK_NAMES = {".DS_Store", "Thumbs.db", "desktop.ini"}
SKIP_DIRS = {".git", "node_modules", "__pycache__"}

DASHES = {chr(0x2014): "em dash", chr(0x2013): "en dash"}
EMOJI_RANGES = [(0x1F300, 0x1FAFF), (0x2600, 0x27BF), (0x2B50, 0x2B50), (0x2B55, 0x2B55), (0x23E9, 0x23FA), (0xFE0F, 0xFE0F)]
EMOJI = re.compile("[" + "".join(f"{chr(a)}-{chr(b)}" for a, b in EMOJI_RANGES) + "]")


def iter_files(base: Path):
    for path in sorted(base.rglob("*")):
        if path.is_file() and not any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts):
            yield path


def check_text(problems: list[str]) -> None:
    for path in iter_files(ROOT):
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        rel = path.relative_to(ROOT)
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            for char, name in DASHES.items():
                if char in line:
                    problems.append(f"{rel}:{number}: {name} found")
            if EMOJI.search(line):
                problems.append(f"{rel}:{number}: emoji or emoji-style marker found")


def check_manifests(problems: list[str]) -> None:
    try:
        plugin = json.loads((PLUGIN / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
        market = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        problems.append(f"manifest could not be read: {error}")
        return
    if plugin.get("version") != market.get("version"):
        problems.append(
            f"version mismatch: plugin.json {plugin.get('version')} vs marketplace.json {market.get('version')}"
        )
    for field in ("description", "author", "license", "homepage", "repository", "icon", "privacyPolicyUrl", "supportUrl"):
        if not plugin.get(field):
            problems.append(f"plugin.json: missing {field}")
    icon = plugin.get("icon")
    if icon and not (PLUGIN / icon).is_file():
        problems.append(f"plugin.json: icon {icon} does not exist")


def check_plugin_files(problems: list[str]) -> None:
    for path in iter_files(PLUGIN):
        rel = path.relative_to(ROOT)
        if path.name in JUNK_NAMES:
            problems.append(f"{rel}: OS junk file")
            continue
        suffix = path.suffix.lower()
        if suffix in TEXT_SUFFIXES or suffix in IMAGE_SUFFIXES:
            continue
        problems.append(f"{rel}: non-image binary or unexpected file type in the plugin folder")


FRONT_MATTER = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)


def check_front_matter(problems: list[str]) -> None:
    targets = list(PLUGIN.glob("skills/*/SKILL.md")) + list(PLUGIN.glob("commands/*.md")) + list(PLUGIN.glob("agents/*.md"))
    for path in sorted(targets):
        rel = path.relative_to(ROOT)
        match = FRONT_MATTER.match(path.read_text(encoding="utf-8"))
        if not match:
            problems.append(f"{rel}: missing YAML front matter")
            continue
        if not re.search(r"^description:[ \t]*\S", match.group(1), re.MULTILINE):
            problems.append(f"{rel}: front matter has no description")
        if path.name == "SKILL.md":
            for key in ("name", "tags"):
                if not re.search(rf"^{key}:[ \t]*\S", match.group(1), re.MULTILINE):
                    problems.append(f"{rel}: front matter has no {key}")


def main() -> int:
    problems: list[str] = []
    check_text(problems)
    check_manifests(problems)
    check_plugin_files(problems)
    check_front_matter(problems)
    if problems:
        print("FAIL: house-style and listing checks")
        for problem in problems:
            print(f"  {problem}")
        return 1
    print("PASS: house-style and listing checks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
