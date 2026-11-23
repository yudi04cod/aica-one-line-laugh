#!/usr/bin/env python3
"""One-line laugh entry for make.fun.

Writes a single original funny sentence (at most 200 characters) to
/output/entry.txt. Pure standard library, deterministic: the same bytes
on every run.
"""

import os

LINE = "I replaced my dead plant with a fake one, and now even the fake one looks thirsty."

MAX_CHARS = 200


def main():
    text = LINE.strip()
    if not text:
        raise ValueError("entry line is empty")
    if len(text) > MAX_CHARS:
        raise ValueError("entry line is %d characters, over the 200 limit" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("entry line must be a single line")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry line must be exactly one sentence")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
