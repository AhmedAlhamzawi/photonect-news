#!/usr/bin/env python3
"""Fetch real Commons portraits of named newsmakers for 2026-06-08.
Zverev -> French Open hero (the champion); Cobolli -> broll_2 (the runner-up);
al-Sharaa -> Syria hero (the president framing the transition);
El Mazned -> UNESCO Arab culture hero (the prize winner; may be absent on Commons → fallback handled by gen script)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from fetch_faces_2026_05_29 import IMG, get_image_url, download  # type: ignore

FACES = [
    ("Alexander_Zverev", "2026-06-08-zverev-french-open/hero.jpg"),
    ("Flavio_Cobolli", "2026-06-08-zverev-french-open/broll_2.jpg"),
    ("Ahmed_al-Sharaa", "2026-06-08-syria-transition-year/hero.jpg"),
    ("Brahim_El_Mazned", "2026-06-08-unesco-arab-culture/hero.jpg"),
]


def main():
    ok = 0
    for title, rel in FACES:
        url = get_image_url(title)
        if not url:
            print(f"  ✗ {title}: no image url", file=sys.stderr); continue
        try:
            size, kb = download(url, IMG / rel)
            print(f"  ✓ {title} -> {rel}  {size} {kb}KB")
            ok += 1
        except Exception as e:
            print(f"  ✗ {title}: {e}", file=sys.stderr)
    print(f"\n{ok}/{len(FACES)} faces fetched")
    return 0  # non-fatal: missing faces fall back to generated scenes


if __name__ == "__main__":
    sys.exit(main())
