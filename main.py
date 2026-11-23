#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes one line, at most 160 characters: a software patch note for a
bug in real life / human biology, in the dry register of a release note.
Deterministic: the same line on every run.
"""

import os

ENTRY = (
    "v2.0.7: fixed a bug where the brain replayed an embarrassing "
    "moment from 2009 at 2 a.m. instead of sleeping."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
