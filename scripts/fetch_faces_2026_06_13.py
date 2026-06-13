#!/usr/bin/env python3
"""Fetch real Commons portraits for the 2026-06-13 slate's named people:
  - PM Ali al-Zaidi  -> iraq-kurdistan-oil-restart broll_1 (he ordered the resumption)
  - Helen Blau       -> stanford-cartilage-regrow broll_3 (senior author)
  - Jalen Brunson    -> nba-finals-knicks broll_3 (Knicks lead scorer)
Tries several title variants per person; if none resolve, the generated neutral fallback stays."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from fetch_faces_2026_05_29 import IMG, get_image_url, download  # type: ignore

CANDIDATES = [
    (["Ali_al-Zaidi", "Ali_Faleh_al-Zaidi", "Ali_Falih_al-Zaidi", "Ali_al-Zaydi"],
     "2026-06-13-iraq-kurdistan-oil-restart/broll_1.jpg"),
    (["Helen_M._Blau", "Helen_Blau"],
     "2026-06-13-stanford-cartilage-regrow/broll_3.jpg"),
    (["Jalen_Brunson", "Jalen_Brunson_(basketball)"],
     "2026-06-13-nba-finals-knicks/broll_3.jpg"),
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
            print(f"  ✗ {rel}: no Commons portrait for any of {titles}", file=sys.stderr)
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
