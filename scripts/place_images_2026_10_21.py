#!/usr/bin/env python3
"""Place the 20 frames for the 2026-10-21 slate. KIE 11.5 credits and Higgsfield 0.38: NO generation possible (5th day).
All frames reused from our own KIE archive, matched per beat and viewed on contact sheets. No named person needs a face
(the Anbar suspects are unnamed; the Iranian spokesman is quoted, not pictured)."""
import shutil
from pathlib import Path
R = Path(__file__).resolve().parents[1]
N = R / "my-video" / "public" / "images" / "news"
D = "2026-10-21"
MAP = {
 # A · Anbar Education: resigned employee's back pay
 f"{D}-a-anbar-resigned-salary-6-years/hero.jpg":    N / "2026-07-16-school-bribe-50k/hero.jpg",           # empty classroom (education directorate)
 f"{D}-a-anbar-resigned-salary-6-years/broll_1.jpg": N / "2026-09-06-c-ghost-employee-six-years/hero.jpg", # old office with files (4 arrest warrants)
 f"{D}-a-anbar-resigned-salary-6-years/broll_2.jpg": N / "2026-09-06-c-ghost-employee-six-years/broll_2.jpg", # ledger + stamp (forged return-to-work letter)
 f"{D}-a-anbar-resigned-salary-6-years/broll_3.jpg": N / "2026-07-16-school-bribe-50k/broll_3.jpg",        # gavel on a file (detention, arts 289/298)
 # B · dollar
 f"{D}-b-dollar-168900-near-170/hero.jpg":    N / "2026-10-11-b-dollar-163300-gap/hero.jpg",      # exchange street, queue at a counter
 f"{D}-b-dollar-168900-near-170/broll_1.jpg": N / "2026-10-14-b-dollar-167000-rebound/hero.jpg",  # counting $100s by a machine (bourse 168,900)
 f"{D}-b-dollar-168900-near-170/broll_2.jpg": N / "2026-10-19-b-dollar-168600-near-169/broll_2.jpg", # exchange window hand-over (shop 169,500)
 f"{D}-b-dollar-168900-near-170/broll_3.jpg": N / "2026-10-07-b-dollar-168500-bourse/broll_2.jpg",  # shuttered shop arcade (Ramadi: shops for rent)
 # C · Iran crossings
 f"{D}-c-shib-closed-iran-crossings/hero.jpg":    N / "2026-09-24-e-mehran-453-million/hero.jpg",     # trucks queued at a border customs yard
 f"{D}-c-shib-closed-iran-crossings/broll_1.jpg": N / "2026-08-15-security-border-committee/broll_2.jpg", # border gate, trucks on a desert road (Shib closed)
 f"{D}-c-shib-closed-iran-crossings/broll_2.jpg": N / "2026-08-15-security-border-committee/broll_1.jpg", # empty ministry meeting room (Iran: no prior notice)
 f"{D}-c-shib-closed-iran-crossings/broll_3.jpg": N / "2026-09-24-e-mehran-453-million/broll_1.jpg",  # tiles warehouse, imported goods ($10B trade)
 # D · solar customs + grid connection
 f"{D}-d-solar-zero-customs-bills/hero.jpg":    N / "2026-09-20-d-solar-loans-30-million/hero.jpg",   # rooftop solar panel over the city
 f"{D}-d-solar-zero-customs-bills/broll_1.jpg": N / "2026-09-20-d-solar-loans-30-million/broll_2.jpg", # man installing a panel on a roof (zero customs)
 f"{D}-d-solar-zero-customs-bills/broll_2.jpg": N / "2026-07-31-power-2tn-unused/hero.jpg",           # pylons to the horizon (national grid)
 f"{D}-d-solar-zero-customs-bills/broll_3.jpg": N / "2026-09-27-d-electricity-52-percent-lost/broll_2.jpg", # wall of electricity meters (smart meters / bills)
 # E · debt + reserves (V10.1 control)
 f"{D}-e-debt-113-trillion-reserves/hero.jpg":    N / "2026-09-20-e-public-debt-109-trillion/hero.jpg",    # central bank tower
 f"{D}-e-debt-113-trillion-reserves/broll_1.jpg": N / "2026-09-20-e-public-debt-109-trillion/broll_1.jpg", # open ledger under a lamp (113.485 tn)
 f"{D}-e-debt-113-trillion-reserves/broll_2.jpg": N / "2026-09-20-e-public-debt-109-trillion/broll_3.jpg", # cash drawer (CBI claims, +25.4%)
 f"{D}-e-debt-113-trillion-reserves/broll_3.jpg": N / "2026-10-17-a-imf-loan-request/broll_2.jpg",         # vault (foreign reserves)
}
for dst, src in MAP.items():
    (N / dst).parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, N / dst)
    print("placed", dst, "<-", Path(src).parent.name + "/" + Path(src).name)
