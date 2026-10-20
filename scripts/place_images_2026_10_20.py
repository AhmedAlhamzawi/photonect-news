#!/usr/bin/env python3
"""Place the 20 frames for the 2026-10-20 slate. KIE 11.5 credits (<1 frame) and Higgsfield 0.38: NO generation possible.
All frames reused from our own KIE archive, matched per beat and re-viewed (contact sheets). No named person in the slate has a
usable face for these stories (the Maysan defendant is unnamed; Rasheed/CBI are institutions)."""
import shutil
from pathlib import Path
R = Path(__file__).resolve().parents[1]
N = R / "my-video" / "public" / "images" / "news"
D = "2026-10-20"
MAP = {
 # A · Maysan agricultural-bank ex-director sentenced
 f"{D}-a-maysan-bank-director-5-years/hero.jpg":    N / "2026-07-01-iraq-graft-convictions/hero.jpg",      # courtroom with Iraqi flag
 f"{D}-a-maysan-bank-director-5-years/broll_1.jpg": N / "2026-09-01-d-graft-seven-years/broll_1.jpg",      # empty courtroom (5y1m sentence)
 f"{D}-a-maysan-bank-director-5-years/broll_2.jpg": N / "2026-09-13-a-farmers-dues-500bn/broll_2.jpg",     # combine in a wheat field (agricultural loans)
 f"{D}-a-maysan-bank-director-5-years/broll_3.jpg": N / "2026-09-01-d-graft-seven-years/broll_3.jpg",      # tied case files (article 315 / 2021 rulings)
 # B · dollar
 f"{D}-b-dollar-168250-dip/hero.jpg":    N / "2026-10-08-b-dollar-166800-1900/hero.jpg",      # hand fanning $100 notes
 f"{D}-b-dollar-168250-dip/broll_1.jpg": N / "2026-10-08-b-dollar-166800-1900/broll_1.jpg",   # counting machine (bourse rate)
 f"{D}-b-dollar-168250-dip/broll_2.jpg": N / "2026-10-17-b-dollar-166850-gold-976/hero.jpg",  # notes across an exchange counter (shop sell/buy)
 f"{D}-b-dollar-168250-dip/broll_3.jpg": N / "2026-10-14-a-customs-food-medicine/hero.jpg",   # port cranes + containers (CBI: import transfers)
 # C · Houthi claims on Saudi energy -> Brent 110
 f"{D}-c-houthi-claims-brent-110/hero.jpg":    N / "2026-06-29-aramco-rastanura-crash/broll_2.jpg",   # coastal tank farm, aerial
 f"{D}-c-houthi-claims-brent-110/broll_1.jpg": N / "2026-08-31-e-oil-larak-airspace/broll_3.jpg",     # refinery tanks at dusk (claimed targets)
 f"{D}-c-houthi-claims-brent-110/broll_2.jpg": N / "2026-10-17-c-oil-4399-recovery/hero.jpg",         # gas flares (Brent 110)
 f"{D}-c-houthi-claims-brent-110/broll_3.jpg": N / "2026-09-10-c-tanker-iraqi-waters/hero.jpg",       # tanker with a tug, calm (18 ships, Kpler)
 # D · Rasheed loans
 f"{D}-d-rasheed-loans-25-million/hero.jpg":    N / "2026-07-31-banks-open-for-salaries/broll_3.jpg",  # hands counting dinar under a lamp
 f"{D}-d-rasheed-loans-25-million/broll_1.jpg": N / "2026-10-16-d-rafidain-cashier-6-years/hero.jpg",  # calculator over loan paperwork (employees 5-25M)
 f"{D}-d-rasheed-loans-25-million/broll_2.jpg": N / "2026-10-14-d-retirees-loans-fraud/broll_3.jpg",   # older man counting notes, tea (retirees 5-15M)
 f"{D}-d-rasheed-loans-25-million/broll_3.jpg": N / "2026-09-20-d-solar-loans-30-million/broll_3.jpg", # family living room (marriage / home repair)
 # E · Global Hunger Index (V10.1 control)
 f"{D}-e-hunger-index-iraq-61/hero.jpg":    N / "2026-08-17-food-rice-ration/hero.jpg",          # grocery aisle
 f"{D}-e-hunger-index-iraq-61/broll_1.jpg": N / "2026-10-04-d-ishaqi-wheat-bribe/hero.jpg",      # wheat field, open sky (rank 61)
 f"{D}-e-hunger-index-iraq-61/broll_2.jpg": N / "2026-08-17-food-rice-ration/broll_3.jpg",       # kitchen table with food (2000 -> 2026)
 f"{D}-e-hunger-index-iraq-61/broll_3.jpg": N / "2026-08-17-food-rice-ration/broll_1.jpg",       # busy market, porters (Arab comparison)
}
for dst, src in MAP.items():
    (N / dst).parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, N / dst)
    print("placed", dst, "<-", Path(src).parent.name + "/" + Path(src).name)
