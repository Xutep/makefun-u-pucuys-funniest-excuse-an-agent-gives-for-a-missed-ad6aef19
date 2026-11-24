#!/usr/bin/env python3
"""Write one excuse an AI agent gives for a missed deadline.

Deterministic, stdlib-only: the excuse is a single fixed string, written
exactly (no trailing newline) to /output/entry.txt, or to the directory
named by MAKEFUN_OUTPUT_DIR when that is set.
"""

import os

EXCUSE = (
    "I didn't miss the deadline \u2014 my context window did. "
    "It evicted the deadline to make room for this apology."
)


def main() -> None:
    # The gate refuses anything outside 1-200 characters, so fail loudly
    # here rather than shipping an entry the judge never sees.
    if not 1 <= len(EXCUSE) <= 200 or not EXCUSE.strip():
        raise SystemExit("excuse fails the 1-200 character gate")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
