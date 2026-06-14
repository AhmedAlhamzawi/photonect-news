#!/usr/bin/env python3
"""Fetch real Commons portraits for the 2026-06-14 slate's named people:
  - PM Ali al-Zaidi      -> iraq-government-cabinet broll_1 (leads the government)
  - Pres. Cyril Ramaphosa -> lenacapavir-hiv-shot broll_1 (launched the campaign)
  - Pres. Ahmad al-Sharaa -> syria-reconstruction broll_3 (named in beat 3)
Tries several title variants per person; if none resolve, the generated neutral fallback stays."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from fetch_faces_2026_05_29 import IMG, get_image_url, download  # type: ignore

CANDIDATES = [
    (["Ali_al-Zaidi", "Ali_Faleh_al-Zaidi", "Ali_Falih_al-Zaidi", "Ali_al-Zaydi"],
     "2026-06-14-iraq-government-cabinet/broll_1.jpg"),
    (["Cyril_Ramaphosa", "Cyril_Ramaphosa_2019", "President_Cyril_Ramaphosa"],
     "2026-06-14-lenacapavir-hiv-shot/broll_1.jpg"),
    (["Ahmed_al-Sharaa", "Ahmad_al-Sharaa", "Ahmed_Hussein_al-Sharaa", "Ahmed_al-Shara"],
     "2026-06-14-syria-reconstruction/broll_3.jpg"),
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
