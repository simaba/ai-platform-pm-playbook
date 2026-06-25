#!/usr/bin/env python3
"""Fail CI when a relative Markdown link points to a missing tracked path."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
SKIPPED_PREFIXES = ("#", "http://", "https://", "mailto:", "tel:", "data:", "//")


def target_from_match(value: str) -> str:
    """Return the link destination without an optional Markdown title."""
    destination = value.strip()
    if destination.startswith("<") and ">" in destination:
        destination = destination[1 : destination.index(">")]
    else:
        destination = destination.split(maxsplit=1)[0]
    return unquote(destination.split("#", 1)[0])


def main() -> int:
    failures: list[str] = []

    for markdown_file in ROOT.rglob("*.md"):
        if ".git" in markdown_file.parts:
            continue
        text = markdown_file.read_text(encoding="utf-8")
        for match in LINK_PATTERN.finditer(text):
            destination = target_from_match(match.group(1))
            if not destination or destination.startswith(SKIPPED_PREFIXES):
                continue
            if not (markdown_file.parent / destination).resolve().exists():
                relative_file = markdown_file.relative_to(ROOT)
                failures.append(f"{relative_file}: missing local link target '{destination}'")

    if failures:
        print("Broken local Markdown links:", file=sys.stderr)
        print("\n".join(failures), file=sys.stderr)
        return 1

    print("Local Markdown links are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
