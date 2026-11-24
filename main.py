#!/usr/bin/env python3
"""The One-Line Cat Joke That Lands — make.fun entry (cat-joke-2248).

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt: exactly one line,
under 200 characters, no trailing newline.
"""

import os
import sys

LINE = "My cat reviewed my cooking on the kitchen floor: one sniff, one slow blink, then she buried it like something that died in the garden."

MAX_CHARS = 200


def main() -> int:
    line = LINE
    if line != line.strip():
        print("error: line has leading or trailing whitespace", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: line must be a single line", file=sys.stderr)
        return 1
    if len(line) >= MAX_CHARS:
        print(f"error: line is {len(line)} chars, must be under {MAX_CHARS}", file=sys.stderr)
        return 1
    if not line.endswith("."):
        print("error: line must end with a period", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print(line)
    print(f"chars: {len(line)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
