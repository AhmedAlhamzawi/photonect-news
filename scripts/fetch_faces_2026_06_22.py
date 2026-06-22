#!/usr/bin/env python3
"""Fetch real Commons portraits for the 2026-06-22 slate's centrally-named people:
  - JD Vance        -> iran-us-switzerland-talks broll_1 (beat 1: he arrives in Switzerland)
  - Abbas Araghchi  -> iran-us-switzerland-talks broll_2 (beat 2: he announces progress)
  - Ali al-Zaidi    -> iraq-militia-disarmament broll_1 (beat 1/2: he meets the factions)
Tries several title variants; if none resolve, the generated fallback stays."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from fetch_faces_2026_05_29 import IMG, get_image_url, download  # type: ignore

CANDIDATES = [
    (["JD_Vance", "J._D._Vance", "JD_Vance_official_portrait", "Vice_President_JD_Vance"],
     "2026-06-22-iran-us-switzerland-talks/broll_1.jpg"),
    (["Abbas_Araghchi", "Seyed_Abbas_Araghchi", "Abbas_Aragchi"],
     "2026-06-22-iran-us-switzerland-talks/broll_2.jpg"),
    (["Ali_al-Zaidi", "Ali_Al-Zaidi", "Ali_Al_Zaidi_(politician)", "Ali_Zaidi"],
     "2026-06-22-iraq-militia-disarmament/broll_1.jpg"),
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
