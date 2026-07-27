#!/usr/bin/env python3
"""Re-source the 12 rejected stills from the 2026-07-27 Pexels fallback pass.

Read-verification of the first pass rejected 12/20:
  bank hero (revolver in drawer), bank broll_1 (craft-stamp flatlay),
  bank broll_2 (cash pile, wanted a bank interior), dollar broll_1 (handcuffs),
  dollar broll_2 (readable "BANCO DE LA NACION ARGENTINA" signage),
  dollar broll_3 (Western supermarket checkout, winter coats),
  fuel hero (readable "ISLAND EXPRESS / HONG KONG" hull branding),
  fuel broll_1 (generic wooded smokestack), fuel broll_3 (readable "INVOICE" text),
  power broll_2 (Mexico/Colgate posters, Latin-American decor),
  power broll_3 (European coastal chimney), turkey broll_3 (tropical paddy canal).

Replacement queries deliberately avoid: identifiable people, any readable
signage or branding, and wrong-biome (tropical / temperate-European) scenery.
Abstract, industrial and arid-landscape framings are preferred.
"""
from __future__ import annotations
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import pexels_fetch_2026_07_27 as base  # type: ignore

D = "2026-07-27"

REFIX = [
    # 1. BANK FORGERY NETWORK
    (f"{D}-bank-forgery-network", "hero.jpg",
     ["archive shelves folders documents", "office archive boxes files", "document folders shelf storage"]),
    (f"{D}-bank-forgery-network", "broll_1.jpg",
     ["stack of paper documents", "pile of papers desk", "paper stack documents closeup"]),
    (f"{D}-bank-forgery-network", "broll_2.jpg",
     ["bank vault door steel", "safe deposit boxes vault", "steel vault door"]),
    # 2. DOLLAR vs OFFICIAL RATE GAP
    (f"{D}-dollar-official-gap", "broll_1.jpg",
     ["dollar banknotes macro closeup", "banknote texture closeup", "money bills stacked closeup"]),
    (f"{D}-dollar-official-gap", "broll_2.jpg",
     ["calculator banknotes desk", "calculator money finance", "coins calculator table"]),
    (f"{D}-dollar-official-gap", "broll_3.jpg",
     ["spice market bazaar stall", "vegetable market stall middle east", "bazaar market goods"]),
    # 3. IRAQI FUEL OIL TO LEBANON
    (f"{D}-fuel-to-lebanon-debt", "hero.jpg",
     ["oil tanker aerial sea", "tanker ship aerial ocean", "cargo ship aerial water"]),
    (f"{D}-fuel-to-lebanon-debt", "broll_1.jpg",
     ["refinery night lights industrial", "power plant night illuminated", "industrial plant night lights"]),
    (f"{D}-fuel-to-lebanon-debt", "broll_3.jpg",
     ["coins stack money", "stacked coins finance", "coins pile closeup"]),
    # 4. GULF POWER LINK DELAYED
    (f"{D}-gulf-power-link-delay", "broll_2.jpg",
     ["candle dark room night", "candlelight darkness home", "candle flame dark interior"]),
    (f"{D}-gulf-power-link-delay", "broll_3.jpg",
     ["industrial pipes plant aerial", "oil gas plant aerial night", "industrial facility pipes"]),
    # 5. PM ANKARA VISIT
    (f"{D}-turkey-water-road-visit", "broll_3.jpg",
     ["date palm trees farm", "palm grove desert farm", "palm trees plantation arid"]),
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
