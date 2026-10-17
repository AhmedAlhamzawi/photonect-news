#!/usr/bin/env python3
"""Place the 20 frames for the 2026-10-17 slate. KIE 11.5 credits (<1 frame) and Higgsfield 0.38: NO generation possible.
Archive KIE scenes (matched per beat, re-viewed) + 5 Pexels frames (originals, Pexels licence) + 1 real Commons portrait
(Kristalina Georgieva, IMF official headshot via Wikipedia pageimages). New external sources live in scripts/_src_2026_10_17/."""
import shutil
from pathlib import Path
R = Path(__file__).resolve().parents[1]
N = R / "my-video" / "public" / "images" / "news"
X = R / "scripts" / "_src_2026_10_17"
D = "2026-10-17"
MAP = {
 # A · IMF loan request
 f"{D}-a-imf-loan-request/hero.jpg":    X / "fin_georgieva.jpg",                                   # Commons: Kristalina Georgieva headshot (real face)
 f"{D}-a-imf-loan-request/broll_1.jpg": N / "2026-06-06-iraq-new-government/broll_1.jpg",          # Iraqi govt building + flag (Iraq requested)
 f"{D}-a-imf-loan-request/broll_2.jpg": N / "2026-10-10-a-salaries-dollar-8-months/broll_2.jpg",   # vault, cash cages (reserves) — 10-10 unaired
 f"{D}-a-imf-loan-request/broll_3.jpg": X / "fin_gas_1.jpg",                                       # Pexels 28688185 fuel nozzle in a car (fuel subsidy)
 # B · dollar + gold
 f"{D}-b-dollar-166850-gold-976/hero.jpg":    N / "2026-07-14-dollar-three-tier/hero.jpg",          # calm counter: dollars fanned beside dinar bundles (gate 1: queue frame read as a run)
 f"{D}-b-dollar-166850-gold-976/broll_1.jpg": N / "2026-07-27-dollar-official-gap/broll_2.jpg",    # hands with dollars over dinar stack, counter
 f"{D}-b-dollar-166850-gold-976/broll_2.jpg": N / "2026-09-24-b-dollar-week-2000/hero.jpg",        # small Baghdad exchange shop
 f"{D}-b-dollar-166850-gold-976/broll_3.jpg": N / "2026-10-10-b-dollar-163600-gold/broll_2.jpg",   # Nahr St gold jeweller window — 10-10 unaired
 # C · oil output (V10.1 control)
 f"{D}-c-oil-4399-recovery/hero.jpg":    N / "2026-10-10-c-lukoil-west-qurna-sale/hero.jpg",       # southern oil field flares — 10-10 unaired
 f"{D}-c-oil-4399-recovery/broll_1.jpg": N / "2026-10-10-c-lukoil-west-qurna-sale/broll_3.jpg",    # crude tanks + workers from behind — 10-10 unaired
 f"{D}-c-oil-4399-recovery/broll_2.jpg": N / "2026-09-24-c-ebrd-minus-12/hero.jpg",                # idle tankers at anchor (the war low)
 f"{D}-c-oil-4399-recovery/broll_3.jpg": N / "2026-08-10-route-baniyas-oil/broll_3.jpg",           # laden tanker under way (exports / Brent)
 # D · Interior fees review
 f"{D}-d-interior-fees-review/hero.jpg":    N / "2026-07-21-graft-oil-undersecretary/broll_2.jpg", # ministry building at dusk + flag
 f"{D}-d-interior-fees-review/broll_1.jpg": N / "2026-09-09-d-baghdad-fees-41-thousand/broll_3.jpg",  # clerk hands, blank forms, stamp (fees)
 f"{D}-d-interior-fees-review/broll_2.jpg": N / "2026-10-11-d-salahaddin-7-properties/broll_1.jpg",  # tied government files + stamp (gate 1: legible CONTRACT frame removed)
 f"{D}-d-interior-fees-review/broll_3.jpg": N / "2026-09-27-a-pension-bribes-nazaha/broll_2.jpg",  # hand presenting a payment card (e-passport fee)
 # E · Iraqis buy Turkish homes
 f"{D}-e-iraqis-turkey-homes-166/hero.jpg":    X / "fin_isk_0.jpg",   # Pexels 39370154 Istanbul skyline, Turkish flag, residential hills
 f"{D}-e-iraqis-turkey-homes-166/broll_1.jpg": X / "fin_ist_2.jpg",   # Pexels 17082168 dense apartment blocks
 f"{D}-e-iraqis-turkey-homes-166/broll_2.jpg": X / "fin_bos_2.jpg",   # Pexels 10725136 Bosphorus waterfront houses
 f"{D}-e-iraqis-turkey-homes-166/broll_3.jpg": X / "fin_key_1.jpg",   # Pexels 7599735 keys + house model, faceless
}
for dst, src in MAP.items():
    (N / dst).parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, N / dst)
    print("placed", dst, "<-", Path(src).name)
