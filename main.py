#!/usr/bin/env python3
"""Entry program for 'The One-Line Cat Joke That Lands' (make.fun).

Writes a single one-line cat joke to /output/entry.txt and to this
entry directory's entry.txt.
"""

import os

ENTRY = "My cat knocked my phone off the table, looked me in the eye, and somehow I apologized — I don't own a cat, I rent a house from one and pay in kibble."

ENTRY_DIR = os.path.dirname(os.path.abspath(__file__))


def main():
    line = ENTRY.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, f"entry length {len(line)} out of range"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    with open(os.path.join(ENTRY_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)
    print(f"wrote {len(line)} chars: {line}")


if __name__ == "__main__":
    main()
