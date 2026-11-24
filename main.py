#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line excuse a developer gives when code breaks
in production to /output/entry.txt. The line is a fixed, deterministic
string: no randomness, no network, no input files. It runs twice and
writes the same bytes both times.
"""

import os

EXCUSE = (
    "The outage wasn't my deploy. "
    "My deploy just happened to be standing next to the outage "
    "when it fell over."
)


def main() -> None:
    text = EXCUSE
    if not (1 <= len(text) <= 200):
        raise SystemExit("excuse must be 1 to 200 characters")
    if not text.strip():
        raise SystemExit("excuse must not be only white space")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
