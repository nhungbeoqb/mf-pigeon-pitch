#!/usr/bin/env python3
"""Pigeon Pitch, One Line — CrumbCoin.

Writes the one-line elevator pitch a city pigeon gives investors
for its startup to /output/entry.txt.

Chosen concept (from 8 generated, strangest that still answers the brief):
CrumbCoin — a pigeon corners the park's breadcrumb market. Beats:
(1) cornered the market, (2) the statue pays rent in seeds,
(3) invest before the squirrels IPO. Concrete startup, pigeon voice,
no LinkedIn/printer/meeting tropes.
"""

import os

ENTRY = (
    "CrumbCoin: I cornered the park's breadcrumb market \u2014 one bench, "
    "forty pigeons, zero overhead \u2014 and the statue pays rent in "
    "seeds. Invest before the squirrels IPO."
)


def main() -> None:
    text = ENTRY
    # Gate self-check, mirroring the sealed scorer:
    # /output/entry.txt must be UTF-8, 1-200 chars, not only whitespace.
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be only whitespace"
    text.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
