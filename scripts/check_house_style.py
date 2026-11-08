#!/usr/bin/env python3
"""House-style and listing checks for the Career Helper repository.

Runs in CI and locally (Python 3.12 or later):

    python3 scripts/check_house_style.py

Checks:
1. No em dashes or en dashes in any text file.
2. No emoji or emoji-style markers (ticks, crosses, warning signs, checkboxes).
3. plugin.json and marketplace.json parse, and their versions match.
4. The plugin folder holds only the file types the plugin directory accepts from
   unverified organisations (Markdown, text, JSON, YAML, and PNG, JPEG, GIF, WebP, or
   ICO images), no file starting with #!, no package manager configuration, no OS junk
   files, and only UTF-8 text with no NUL bytes.
5. Every SKILL.md, command, and agent starts with YAML front matter that has a description
   and uses only the keys the plugin directory accepts.

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
PLUGIN_TEXT_SUFFIXES = {".md", ".txt", ".json", ".yml", ".yaml"}
PLUGIN_IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico"}
PACKAGE_CONFIG_NAMES = {
    "package.json", "package-lock.json", "npm-shrinkwrap.json", "pnpm-workspace.yaml", "pnpm-lock.yaml",
    "yarn.lock", ".yarnrc", ".yarnrc.yml", ".npmrc", "bunfig.toml", "bun.lock", "bun.lockb",
    "uv.toml", "pyproject.toml", "requirements.txt", "pip.conf", "Pipfile", "Pipfile.lock", "poetry.lock",
}
ALLOWED_KEYS = {
    "skill": {"name", "description"},
    "command": {"description", "argument-hint"},
    "agent": {"name", "description", "model"},
}
JUNK_NAMES = {".DS_Store", "Thumbs.db", "desktop.ini"}
SKIP_DIRS = {".git", "node_modules", "__pycache__"}

DASHES = {chr(0x2014): "em dash", chr(0x2013): "en dash"}
EMOJI_RANGES = [(0x1F300, 0x1FAFF), (0x2600, 0x27BF), (0x2B50, 0x2B50), (0x2B55, 0x2B55), (0x23E9, 0x23FA), (0xFE0F, 0xFE0F)]
EMOJI = re.compile("[" + "".join(f"{chr(a)}-{chr(b)}" for a, b in EMOJI_RANGES) + "]")


def iter_files(base: Path):
    """Yield every file under base, skipping .git, node_modules, and __pycache__."""
    for path in sorted(base.rglob("*")):
        if path.is_file() and not any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts):
            yield path


def check_text(problems: list[str]) -> None:
    """Record any em dash, en dash, or emoji in the repository's text files."""
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
    """Check both manifests parse, versions match, and listing fields are present."""
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
    """Flag any file in the plugin folder that the plugin directory would refuse."""
    for path in iter_files(PLUGIN):
        rel = path.relative_to(ROOT)
        if path.name in JUNK_NAMES:
            problems.append(f"{rel}: OS junk file")
            continue
        if path.name in PACKAGE_CONFIG_NAMES:
            problems.append(f"{rel}: package manager configuration file")
            continue
        suffix = path.suffix.lower()
        if suffix in PLUGIN_IMAGE_SUFFIXES:
            continue
        if suffix not in PLUGIN_TEXT_SUFFIXES:
            problems.append(f"{rel}: file type not accepted by the plugin directory (Markdown, text, JSON, YAML, or image only)")
            continue
        data = path.read_bytes()
        if data.startswith(b"#!"):
            problems.append(f"{rel}: starts with #!")
        if b"\x00" in data:
            problems.append(f"{rel}: contains NUL bytes")
        try:
            data.decode("utf-8")
        except UnicodeDecodeError:
            problems.append(f"{rel}: not valid UTF-8")


FRONT_MATTER = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)


def check_front_matter(problems: list[str]) -> None:
    """Check skills, commands, and agents start with front matter that has a description."""
    targets = (
        [(p, "skill") for p in PLUGIN.glob("skills/*/SKILL.md")]
        + [(p, "command") for p in PLUGIN.glob("commands/*.md")]
        + [(p, "agent") for p in PLUGIN.glob("agents/*.md")]
    )
    for path, kind in sorted(targets):
        rel = path.relative_to(ROOT)
        match = FRONT_MATTER.match(path.read_text(encoding="utf-8"))
        if not match:
            problems.append(f"{rel}: missing YAML front matter")
            continue
        if not re.search(r"^description:[ \t]*\S", match.group(1), re.MULTILINE):
            problems.append(f"{rel}: front matter has no description")
        if kind == "skill" and not re.search(r"^name:[ \t]*\S", match.group(1), re.MULTILINE):
            problems.append(f"{rel}: front matter has no name")
        for key in re.findall(r"^([A-Za-z0-9_-]+):", match.group(1), re.MULTILINE):
            if key not in ALLOWED_KEYS[kind]:
                problems.append(f"{rel}: front matter key '{key}' is not accepted by the plugin directory")


def main() -> int:
    """Run every check, print the result, and return the process exit code."""
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
