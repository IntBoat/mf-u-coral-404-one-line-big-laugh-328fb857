#!/usr/bin/env python3
"""One Line, Big Laugh (make.fun).

Writes the entry -- one original one-line joke, kept as a single line
with no trailing newline -- to /output/entry.txt, where the sealed
scorer reads it.
"""

import os

ENTRY = 'My code finally passed all the tests, so I celebrated by deleting the tests — turns out the bug was my confidence all along.'


def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


def main():
    write_entry()


if __name__ == "__main__":
    main()
