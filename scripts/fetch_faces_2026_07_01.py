#!/usr/bin/env python3
"""Fetch real Commons/Wikipedia portraits for the named people in the 2026-07-01 slate.
→ my-video/public/images/news/<slug>/<slot>.jpg  (face slots only; scenes handled separately)."""
from __future__ import annotations
import json, sys, urllib.parse, urllib.request, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IMG = ROOT / "my-video" / "public" / "images" / "news"
UA = "Mozilla/5.0 (PhotonectNews/1.0; ahmed@photonect.net)"

# (wikipedia title, slug, slot)
FACES = [
    ("Ben Shelton",    "2026-07-01-wimbledon-shelton-upset", "hero.jpg"),
    ("Abbas Araghchi", "2026-07-01-lebanon-war-committee",   "broll_1.jpg"),
    ("Marco Rubio",    "2026-07-01-lebanon-war-committee",   "broll_3.jpg"),
]


def pageimage(title: str) -> str | None:
    q = urllib.parse.urlencode({
        "action": "query", "titles": title, "prop": "pageimages",
        "piprop": "thumbnail", "pithumbsize": "1200", "format": "json", "redirects": "1",
    })
    url = f"https://en.wikipedia.org/w/api.php?{q}"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    data = json.loads(urllib.request.urlopen(req, timeout=30).read().decode())
    pages = data.get("query", {}).get("pages", {})
    for _, p in pages.items():
        th = p.get("thumbnail", {}).get("source")
        if th:
            return th
    return None


def main():
    ok, miss = [], []
    for title, slug, slot in FACES:
        dest = IMG / slug / slot
        dest.parent.mkdir(parents=True, exist_ok=True)
        try:
            src = pageimage(title)
            if not src:
                print(f"  ✗ {title}: no Commons portrait"); miss.append((title, slug, slot)); continue
            subprocess.run(["curl", "-sL", "--retry", "3", "--max-time", "60", "-A", UA, src, "-o", str(dest)], check=False)
            sz = dest.stat().st_size if dest.is_file() else 0
            if sz > 25_000:
                print(f"  ✓ {title} → {slug}/{slot} ({sz//1024} KB)  [{src.split('/')[-1][:40]}]")
                ok.append((title, slug, slot))
            else:
                print(f"  ✗ {title}: download too small ({sz}b)"); miss.append((title, slug, slot))
        except Exception as e:
            print(f"  ✗ {title}: {e}"); miss.append((title, slug, slot))
    print(f"\nfaces: {len(ok)} ok, {len(miss)} missing")
    if miss:
        print("MISSING (fall back to scene):", [f"{s}/{sl}" for _, s, sl in miss])
    (IMG / "_faces_missing_0701.json").write_text(json.dumps([[s, sl] for _, s, sl in miss]))


if __name__ == "__main__":
    main()
