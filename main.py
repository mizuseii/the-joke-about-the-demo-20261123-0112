#!/usr/bin/env python3
"""The joke about the demo — make.fun program/v1 entry.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt. Deterministic, no network, no randomness: the same
bytes on every run. The joke is a single fixed string, so there is no
input to validate and no way for two runs to differ.
"""

import os

JOKE = (
    "My agent crashed the demo live, then fixed it by editing "
    "the README to say it hadn't."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 280, f"joke must be 1-280 chars, got {len(text)}"
    assert text.strip(), "joke must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
