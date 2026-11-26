#!/usr/bin/env python3
"""Snooze Button Roast — a one-line roast of an alarm clock that rings at
6 AM on a Saturday: the clock as a tiny landlord collecting rent for a day
you don't even live in.

Writes the entry to /output/entry.txt with no trailing newline.
"""

import os

ENTRY = (
    "My alarm clock rings at 6 AM on a Saturday like a tiny landlord "
    "collecting rent for a day I don't even live in."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
