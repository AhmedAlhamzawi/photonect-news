#!/usr/bin/env python3
"""Place the 9 reused/real frames for the 2026-10-14 slate (the other 11 are KIE, gen_scenes_2026_10_14.py).

The 2026-10-10 slate was never committed or posted, so its frames below have not aired.
a/broll_2: food-market eggs stall (2026-10-10-d, unaired).  a/broll_3: PM Ali al-Zaidi real portrait (Wikimedia Commons).
b/broll_1: gold-shop window (2026-10-10-b/broll_2, unaired).  b/broll_2: real CBI HQ tower (Wikimedia Commons CC0).
c/hero, c/broll_2, c/broll_3: oil-field flares, storage tanks, refinery at night (2026-10-10-c, unaired).
d/broll_1: card/POS payment at a shop counter (2026-10-10-d, unaired).  d/broll_3: older man counting cash with tea (2026-10-10-a/hero, unaired).
"""
import shutil
from pathlib import Path
N = Path(__file__).resolve().parents[1] / "my-video" / "public" / "images" / "news"
MAP = {
 "2026-10-14-a-customs-food-medicine/broll_2.jpg": "2026-10-10-d-cement-installments-2-years/broll_2.jpg",
 "2026-10-14-a-customs-food-medicine/broll_3.jpg": "2026-10-11-a-watan-95k-plots/broll_3.jpg",
 "2026-10-14-b-dollar-167000-rebound/broll_1.jpg": "2026-10-10-b-dollar-163600-gold/broll_2.jpg",
 "2026-10-14-b-dollar-167000-rebound/broll_2.jpg": "2026-10-11-b-dollar-163300-gap/broll_2.jpg",
 "2026-10-14-c-jordan-kirkuk-oil/hero.jpg": "2026-10-10-c-lukoil-west-qurna-sale/hero.jpg",
 "2026-10-14-c-jordan-kirkuk-oil/broll_2.jpg": "2026-10-10-c-lukoil-west-qurna-sale/broll_3.jpg",
 "2026-10-14-c-jordan-kirkuk-oil/broll_3.jpg": "2026-10-10-c-lukoil-west-qurna-sale/broll_2.jpg",
 "2026-10-14-d-retirees-loans-fraud/broll_1.jpg": "2026-10-10-d-cement-installments-2-years/broll_1.jpg",
 "2026-10-14-d-retirees-loans-fraud/broll_3.jpg": "2026-10-10-a-salaries-dollar-8-months/hero.jpg",
}
for dst, src in MAP.items():
    (N / dst).parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(N / src, N / dst)
    print("placed", dst, "<-", src)
