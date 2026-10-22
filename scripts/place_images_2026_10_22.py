#!/usr/bin/env python3
"""Place the 20 frames for the 2026-10-22 slate. KIE 11.5 credits and Higgsfield 0.38: NO generation possible (6th day).
All frames reused from our own KIE archive, matched per beat and viewed on contact sheets. No named person needs a face
(the Dhi Qar suspects are unnamed; the oil undersecretary and the expert are quoted, not pictured)."""
import shutil
from pathlib import Path
R = Path(__file__).resolve().parents[1]
N = R / "my-video" / "public" / "images" / "news"
D = "2026-10-22"
MAP = {
 # A · Dhi Qar governorate accounts director caught taking a bribe
 f"{D}-a-dhiqar-accounts-bribe-caught/hero.jpg":    N / "2026-09-10-e-bribe-car-papers/hero.jpg",        # cash under a hand on stamped papers, Iraqi flag
 f"{D}-a-dhiqar-accounts-bribe-caught/broll_1.jpg": N / "2026-09-08-a-karbala-bribery-caught/hero.jpg",  # govt corridor with waiting chairs (contractor's repeated visits)
 f"{D}-a-dhiqar-accounts-bribe-caught/broll_2.jpg": N / "2026-09-08-a-karbala-bribery-caught/broll_1.jpg", # cash slid across a desk (caught red-handed)
 f"{D}-a-dhiqar-accounts-bribe-caught/broll_3.jpg": N / "2026-10-04-d-ishaqi-wheat-bribe/broll_3.jpg",   # scales + gavel (detention, art. 308)
 # B · dollar 170,000
 f"{D}-b-dollar-170000-shops/hero.jpg":    N / "2026-07-20-dinar-dollar-fall/broll_2.jpg",     # exchange-shop street at dusk
 f"{D}-b-dollar-170000-shops/broll_1.jpg": N / "2026-10-05-b-dollar-159050-160k/broll_1.jpg",   # stacks of $100s + calculator (bourse 169,500)
 f"{D}-b-dollar-170000-shops/broll_2.jpg": N / "2026-10-17-b-dollar-166850-gold-976/hero.jpg", # counter hand-over (shops 170,000)
 f"{D}-b-dollar-170000-shops/broll_3.jpg": N / "2026-07-20-dinar-dollar-fall/broll_3.jpg",     # scales: dinar vs dollar (Bloomberg -14.2%)
 # C · Iran toman 273,700
 f"{D}-c-toman-273700-iran/hero.jpg":    N / "2026-10-04-c-toman-270950-record/hero.jpg",     # Tehran skyline, Milad tower
 f"{D}-c-toman-273700-iran/broll_1.jpg": N / "2026-10-04-c-toman-270950-record/broll_1.jpg",  # Iranian banknote (free-market rate)
 f"{D}-c-toman-273700-iran/broll_2.jpg": N / "2026-10-04-c-toman-270950-record/broll_2.jpg",  # covered bazaar (inflation 73.6%)
 f"{D}-c-toman-273700-iran/broll_3.jpg": N / "2026-10-04-c-toman-270950-record/broll_3.jpg",  # dried-fruit stall, Iranian goods (trade dollar demand)
 # D · education: third round + no-fail year
 f"{D}-d-no-fail-year-third-round/hero.jpg":    N / "2026-07-16-school-bribe-50k/broll_2.jpg",         # pupils walking through a school gate
 f"{D}-d-no-fail-year-third-round/broll_1.jpg": N / "2026-07-16-school-bribe-50k/hero.jpg",            # classroom, chalkboard (third round)
 f"{D}-d-no-fail-year-third-round/broll_2.jpg": N / "2026-06-14-iraq-government-cabinet/broll_2.jpg",  # cabinet meeting table (needs cabinet approval)
 f"{D}-d-no-fail-year-third-round/broll_3.jpg": N / "2026-09-16-a-school-start-11-october/broll_1.jpg", # boy with backpack (no-fail year)
 # E · Artawi gas 96% (V10.1 control)
 f"{D}-e-artawi-gas-96-percent/hero.jpg":    N / "2026-08-05-current-khormor-gas/hero.jpg",      # gas plant with flare, aerial
 f"{D}-e-artawi-gas-96-percent/broll_1.jpg": N / "2026-09-16-c-danagas-1000-megawatts/broll_2.jpg", # yellow gas pipework (96% complete)
 f"{D}-e-artawi-gas-96-percent/broll_2.jpg": N / "2026-07-24-iran-gas-oil-barter/broll_1.jpg",    # gauges and valves (50m scf raw gas)
 f"{D}-e-artawi-gas-96-percent/broll_3.jpg": N / "2026-08-05-current-khormor-gas/broll_2.jpg",    # power-station turbine hall (GMP / fuel for plants)
}
for dst, src in MAP.items():
    (N / dst).parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, N / dst)
    print("placed", dst, "<-", Path(src).parent.name + "/" + Path(src).name)
