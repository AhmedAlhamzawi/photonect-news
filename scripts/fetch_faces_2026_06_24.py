#!/usr/bin/env python3
"""Fetch real Commons portraits for the 2026-06-24 slate's centrally-named people:
  - Marco Rubio          -> rubio-gulf-tour broll_1 (beat 1: he tours the Gulf)
  - Mohammed bin Salman  -> saudi-pif-sports-pivot broll_1 (beat 1: he chairs the PIF strategy)
Tries several title variants; if none resolve, the generated fallback stays."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from fetch_faces_2026_05_29 import IMG, get_image_url, download  # type: ignore

CANDIDATES = [
    (["Marco_Rubio", "Marco_Rubio_official_portrait", "Secretary_Marco_Rubio", "Marco_Rubio_secretary_of_state"],
     "2026-06-24-rubio-gulf-tour/broll_1.jpg"),
    (["Mohammed_bin_Salman", "Mohammed_bin_Salman_Al_Saud", "Mohammed_bin_Salman_2019", "Crown_Prince_Mohammed_bin_Salman"],
     "2026-06-24-saudi-pif-sports-pivot/broll_1.jpg"),
]


def main():
    ok = 0
    for titles, rel in CANDIDATES:
        url = None; used = None
        for t in titles:
            url = get_image_url(t)
            if url:
                used = t; break
        if not url:
            print(f"  ✗ {rel}: no Commons portrait for any of {titles} — keeping generated scene", file=sys.stderr)
            continue
        try:
            size, kb = download(url, IMG / rel)
            print(f"  ✓ {used} -> {rel}  {size} {kb}KB")
            ok += 1
        except Exception as e:
            print(f"  ✗ {used}: {e}", file=sys.stderr)
    print(f"\n{ok}/{len(CANDIDATES)} faces fetched")
    return 0


if __name__ == "__main__":
    sys.exit(main())
