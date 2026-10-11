#!/usr/bin/env python3
"""Place the 6 reused/real frames for the 2026-10-11 slate (the other 14 are KIE, gen_scenes_2026_10_11.py).

The 2026-10-10 slate was never committed or posted, so its frames have not aired.
a/broll_3: PM Ali al-Zaidi portrait (Wikimedia Commons, via 2026-10-10-a).
b/hero, b/broll_1: KIE exchange-shop + counting-machine scenes (from 2026-10-10-b, unaired).
b/broll_3: KIE market-stall scene (from 2026-10-10-d/broll_3, unaired).
b/broll_2: real CBI HQ tower (Wikimedia Commons CC0, via 2026-10-10-b).
d/broll_2: the synthetic cash-seizure scene was rejected at QA; regenerated as a neutral housing-complex aerial (gen_scenes).
"""
import shutil
from pathlib import Path
N = Path(__file__).resolve().parents[1] / "my-video" / "public" / "images" / "news"
MAP = {
 "2026-10-11-a-watan-95k-plots/broll_3.jpg": "2026-10-10-a-salaries-dollar-8-months/broll_3.jpg",
 "2026-10-11-b-dollar-163300-gap/hero.jpg": "2026-10-10-b-dollar-163600-gold/hero.jpg",
 "2026-10-11-b-dollar-163300-gap/broll_1.jpg": "2026-10-10-b-dollar-163600-gold/broll_1.jpg",
 "2026-10-11-b-dollar-163300-gap/broll_2.jpg": "2026-10-10-b-dollar-163600-gold/broll_3.jpg",
 "2026-10-11-b-dollar-163300-gap/broll_3.jpg": "2026-10-10-d-cement-installments-2-years/broll_3.jpg",
}
for dst, src in MAP.items():
    (N / dst).parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(N / src, N / dst)
    print("placed", dst, "<-", src)
