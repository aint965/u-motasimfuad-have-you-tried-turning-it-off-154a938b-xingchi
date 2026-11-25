#!/usr/bin/env python3
"""Have You Tried Turning It Off? — make.fun entry.

Writes one funny single line a hopeless tech support agent says to a
desperate customer, to /output/entry.txt. Deterministic: the same bytes
on every run.
"""

import os

LINE = "I've escalated your ticket to a specialist. It's me, in a different hat."


def main():
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
