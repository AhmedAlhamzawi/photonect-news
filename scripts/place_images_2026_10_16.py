#!/usr/bin/env python3
"""Place the 20 frames for the 2026-10-16 slate. KIE 15.5 credits (<1 frame at ~18/frame) and Higgsfield 0.38,
so NO generation was possible: every frame is reused from our own archive of KIE Nano Banana Pro scenes, matched per beat
and re-viewed. The e (weather) set is the 2026-10-10 Hit-lightning slate, which was never committed or posted (unaired).
No real named individual appears in any frame."""
import shutil
from pathlib import Path
N = Path(__file__).resolve().parents[1] / "my-video" / "public" / "images" / "news"
D = "2026-10-16"
MAP = {
 # A · passport fee
 f"{D}-a-passport-101k-reversed/hero.jpg":    "2026-10-11-c-riyadh-airport-flights/hero.jpg",   # travellers with luggage in a hall (gate 1: no USD cash)
 f"{D}-a-passport-101k-reversed/broll_1.jpg": "2026-09-27-a-pension-bribes-nazaha/broll_2.jpg",  # hand presenting a payment card (fee paid electronically)
 f"{D}-a-passport-101k-reversed/broll_2.jpg": "2026-09-08-a-karbala-bribery-caught/hero.jpg",    # govt office corridor, waiting chairs
 f"{D}-a-passport-101k-reversed/broll_3.jpg": "2026-09-09-d-baghdad-fees-41-thousand/broll_3.jpg",  # hands, blank forms, stamp (fees)
 # B · travel dollar
 f"{D}-b-travel-dollar-2-months/hero.jpg":    "2026-10-10-b-dollar-163600-gold/hero.jpg",       # crowd outside a Baghdad exchange shop (10-10, unaired)
 f"{D}-b-travel-dollar-2-months/broll_1.jpg": "2026-10-10-b-dollar-163600-gold/broll_1.jpg",    # cashier at a counting machine (10-10, unaired)
 f"{D}-b-travel-dollar-2-months/broll_2.jpg": "2026-10-11-c-riyadh-airport-flights/broll_2.jpg", # airliner climbing at dusk
 f"{D}-b-travel-dollar-2-months/broll_3.jpg": "2026-10-14-b-dollar-167000-rebound/hero.jpg",     # cashier fanning dollars (bourse)
 # C · US sanctions on an Iraqi bank
 f"{D}-c-us-sanctions-iraqi-bank/hero.jpg":    "2026-09-11-e-us-sanctions-iraqi-firms/hero.jpg",  # chained, padlocked dollar stack
 f"{D}-c-us-sanctions-iraqi-bank/broll_1.jpg": "2026-08-27-d-banks-six-trillion/broll_2.jpg",     # bank building, Baghdad street
 f"{D}-c-us-sanctions-iraqi-bank/broll_2.jpg": "2026-09-11-e-us-sanctions-iraqi-firms/broll_1.jpg",  # Baghdad skyline over the Tigris (gate 1: neutral)
 f"{D}-c-us-sanctions-iraqi-bank/broll_3.jpg": "2026-08-27-d-banks-six-trillion/hero.jpg",        # bank hall, counters
 # D · Rafidain cashier + Kirkuk bribe
 f"{D}-d-rafidain-cashier-6-years/hero.jpg":    "2026-09-28-a-state-banks-loans-probe/hero.jpg",   # ledger + calculator (account balances)
 f"{D}-d-rafidain-cashier-6-years/broll_1.jpg": "2026-10-04-d-ishaqi-wheat-bribe/broll_3.jpg",     # scales of justice + gavel
 f"{D}-d-rafidain-cashier-6-years/broll_2.jpg": "2026-09-19-c-aqari-platform-kirkuk/broll_3.jpg",  # stacked files on an office table (gate 2: no cash, no act)
 f"{D}-d-rafidain-cashier-6-years/broll_3.jpg": "2026-09-11-e-us-sanctions-iraqi-firms/broll_2.jpg", # commercial building under construction (gate 1: non-depictive)
 # E · weather (2026-10-10-e, unaired)
 f"{D}-e-rain-north-40-south/hero.jpg":    "2026-10-10-e-hit-lightning-rain/broll_3.jpg",  # rainy Iraqi street, umbrellas
 f"{D}-e-rain-north-40-south/broll_1.jpg": "2026-10-10-e-hit-lightning-rain/broll_2.jpg",  # towering storm cloud over a desert road
 f"{D}-e-rain-north-40-south/broll_2.jpg": "2026-10-10-e-hit-lightning-rain/hero.jpg",     # lightning over a town
 f"{D}-e-rain-north-40-south/broll_3.jpg": "2026-09-20-c-sandstorms-300-days/hero.jpg",    # hot dusty street (south heat + wind)
}
for dst, src in MAP.items():
    (N / dst).parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(N / src, N / dst)
    print("placed", dst, "<-", src)
