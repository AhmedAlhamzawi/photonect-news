#!/usr/bin/env python3
"""Place the 20 frames for the 2026-10-19 slate. KIE 11.5 credits (<1 frame) and Higgsfield 0.38: NO generation possible.
Archive KIE scenes (matched per beat, re-viewed) + 2 Pexels frames (originals, Pexels licence, centre-cropped to 1536x2730).
No free portrait exists for Najla Imad (no Commons file, no wiki image) — e uses faceless frames, no lookalike faces.
New external sources live in scripts/_src_2026_10_19/."""
import shutil
from pathlib import Path
R = Path(__file__).resolve().parents[1]
N = R / "my-video" / "public" / "images" / "news"
X = R / "scripts" / "_src_2026_10_19"
D = "2026-10-19"
MAP = {
 # A · Diwaniyah real-estate arrests
 f"{D}-a-diwaniyah-property-arrests/hero.jpg":    N / "2026-09-11-d-tikrit-land-arrest/broll_3.jpg",      # archive aisle of files, light shaft
 f"{D}-a-diwaniyah-property-arrests/broll_1.jpg": N / "2026-08-10-land-files-nasiriya/broll_1.jpg",       # tied property files + stamp (4 employees)
 f"{D}-a-diwaniyah-property-arrests/broll_2.jpg": N / "2026-09-07-d-nazaha-104-properties/broll_2.jpg",   # hand on a stamped document (seized papers)
 f"{D}-a-diwaniyah-property-arrests/broll_3.jpg": N / "2026-08-28-a-lands-muthanna-61/hero.jpg",          # registry office, open ledgers (30 more warrants) — gate 1: gavel removed
 # B · dollar
 f"{D}-b-dollar-168600-near-169/hero.jpg":    N / "2026-09-10-b-dollar-official-gap/broll_1.jpg",   # exchange counter, counting machine, dollars
 f"{D}-b-dollar-168600-near-169/broll_1.jpg": N / "2026-09-10-b-dollar-official-gap/broll_2.jpg",  # dinar + dollar stacks on a desk (bourse rate) — gate 1: kiosk crowd removed
 f"{D}-b-dollar-168600-near-169/broll_2.jpg": N / "2026-09-09-b-dollar-bourse-counter/broll_3.jpg", # notes passed through a shop window (shop sell/buy)
 f"{D}-b-dollar-168600-near-169/broll_3.jpg": N / "2026-10-14-b-dollar-167000-rebound/broll_2.jpg", # CBI tower (official rate / the gap)
 # C · US embassy travel alert
 f"{D}-c-us-alert-iraq-airports/hero.jpg":    N / "2026-10-11-c-riyadh-airport-flights/broll_1.jpg",   # airport apron at dusk, aerial
 f"{D}-c-us-alert-iraq-airports/broll_1.jpg": N / "2026-10-11-c-riyadh-airport-flights/broll_2.jpg",  # airliner climbing, contrails (flights) — gate 1: ominous suitcase removed
 f"{D}-c-us-alert-iraq-airports/broll_2.jpg": N / "2026-09-27-c-us-warning-iraq-airports/broll_2.jpg", # control tower in fog (threat / airspace)
 f"{D}-c-us-alert-iraq-airports/broll_3.jpg": N / "2026-09-27-c-us-warning-iraq-airports/broll_3.jpg", # lone traveller walking with suitcase, calm (check your flight) — gate 1: queue removed
 # D · damaged dinar replacement
 f"{D}-d-damaged-dinar-free-swap/hero.jpg":    N / "2026-08-16-silence-currency-dinar/broll_1.jpg",  # fanned dinar notes
 f"{D}-d-damaged-dinar-free-swap/broll_1.jpg": X / "px_phone.jpg",                                    # Pexels 7971696 hands booking on a phone (Ur platform)
 f"{D}-d-damaged-dinar-free-swap/broll_2.jpg": N / "2026-10-14-d-retirees-loans-fraud/hero.jpg",     # queue in an old office hall (banks / appointment)
 f"{D}-d-damaged-dinar-free-swap/broll_3.jpg": N / "2026-09-17-b-dollar-158850-159000/broll_1.jpg",  # worn, frayed dinar bundle (negligence vs not)
 # E · Iraq at the Asian Para Games (V10.1 control)
 f"{D}-e-para-games-japan-3-0/hero.jpg":    N / "2026-09-11-c-muaythai-13-medals/broll_3.jpg",       # Iraqi flag over a crowd
 f"{D}-e-para-games-japan-3-0/broll_1.jpg": N / "2026-07-29-female-volleyball-olympics/broll_2.jpg", # ball over the net (volleyball win)
 f"{D}-e-para-games-japan-3-0/broll_2.jpg": X / "px_paddle.jpg",                                    # Pexels 24196269 hands holding paddles, faceless (table tennis)
 f"{D}-e-para-games-japan-3-0/broll_3.jpg": N / "2026-10-02-e-wrestling-bronze-16-years/hero.jpg",  # Iraqi flag over water (semi-final, games to 24 Oct) — gate 2: medals frame removed (no medal won yet)
}
for dst, src in MAP.items():
    (N / dst).parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, N / dst)
    print("placed", dst, "<-", Path(src).name)
