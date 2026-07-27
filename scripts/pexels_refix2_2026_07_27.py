#!/usr/bin/env python3
"""Second re-source pass for the 2026-07-27 slate — 5 stills still failing
Read-verification after pexels_refix_2026_07_27.py:

  bank broll_2  — antique safe with readable "FICHET PARIS" embossing
  dollar broll_2 — legible English handwriting ("Taxes 60 / loan 800") + CASIO branding
  fuel broll_1  — black-and-white European industrial-heritage site with tourists
  fuel broll_3  — hourglass-and-coins stock cliché, soft pastel tone, off-register for news
  gulf broll_2  — candlelit portrait of an identifiable woman, reads romantic not blackout

Replacements stay brandless, textless, people-free and on-biome.
"""
from __future__ import annotations
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import pexels_fetch_2026_07_27 as base  # type: ignore

D = "2026-07-27"

REFIX = [
    (f"{D}-bank-forgery-network", "broll_2.jpg",
     ["safe deposit boxes wall", "safety deposit box rows", "metal deposit boxes bank"]),
    (f"{D}-dollar-official-gap", "broll_2.jpg",
     ["banknotes bundles stacked", "currency notes bundles cash", "money bundles stack table"]),
    (f"{D}-fuel-to-lebanon-debt", "broll_1.jpg",
     ["power plant cooling towers", "power station chimneys sunset", "electricity plant industrial"]),
    (f"{D}-fuel-to-lebanon-debt", "broll_3.jpg",
     ["oil barrels stacked", "fuel barrels row industrial", "oil drums storage"]),
    (f"{D}-gulf-power-link-delay", "broll_2.jpg",
     ["air conditioner units building wall", "air conditioners facade apartment", "ac units wall building"]),
]


def main() -> int:
    base.JOBS = REFIX
    for slug, fname, _ in REFIX:
        p = base.IMG_ROOT / slug / fname
        if p.exists():
            p.unlink()
    return base.main()


if __name__ == "__main__":
    raise SystemExit(main())
