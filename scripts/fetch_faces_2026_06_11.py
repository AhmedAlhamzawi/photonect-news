#!/usr/bin/env python3
"""Fetch real Commons portrait of PM Ali al-Zaidi for 2026-06-11 (the named state actor
leading Iraq's disarmament initiative -> iraq-militia-disarmament beat-2). Tries several
title variants; if none resolve, the generated neutral meeting-room fallback stays."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from fetch_faces_2026_05_29 import IMG, get_image_url, download  # type: ignore

# (list of title variants, output_path_rel) — first variant that resolves wins
CANDIDATES = [
    (["Ali_al-Zaidi", "Ali_Faleh_al-Zaidi", "Ali_Falih_al-Zaidi", "Ali_al-Zaydi"],
     "2026-06-11-iraq-militia-disarmament/broll_2.jpg"),
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
    return 0 if ok == len(CANDIDATES) else 1


if __name__ == "__main__":
    sys.exit(main())
