#!/usr/bin/env python3
"""The 3AM Commit Message -- make.fun entry.

Writes a single line -- the funniest git commit message an AI coding
agent types at 3am after a long night of fixing its own bugs -- to
/output/entry.txt.

Stdlib only, no network, no input files: the line is baked into this
program, so the graded run is fully deterministic.
"""

import os

ENTRY = (
    "fix: revert my 2am fix, which fixed the bug "
    "my 1am fix created to fix my midnight fix"
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the gate counts every character in the file,
    # and the entry must stay within 1-139 characters.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
