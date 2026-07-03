#!/usr/bin/env python3
"""Fetch real Commons portraits of named newsmakers for the 2026-07-03 slate.
Reuses the Wikipedia REST/pageimages pattern from fetch_faces_2026_05_29.py.
"""
import io, json, sys, urllib.request
from pathlib import Path
from PIL import Image

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE")
IMG = ROOT / "my-video" / "public" / "images" / "news"

# (wikipedia_title, output_path_rel)
FACES = [
    ("LeBron_James", "2026-07-03-nba-free-agency-quake/broll_1.jpg"),
    ("Giannis_Antetokounmpo", "2026-07-03-nba-free-agency-quake/broll_3.jpg"),
    ("Mohammed_bin_Salman", "2026-07-03-saudi-led-axis/broll_1.jpg"),
]

UA = "PhotonectNewsBot/1.0 (https://photonect.net; ahmed@photonect.net)"


def get_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())


def get_image_url(title):
    try:
        d = get_json(f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}")
        for k in ("originalimage", "thumbnail"):
            if d.get(k, {}).get("source"):
                return d[k]["source"]
    except Exception as e:
        print(f"  summary err {title}: {e}", file=sys.stderr)
    try:
        d = get_json(f"https://en.wikipedia.org/w/api.php?action=query&titles={title}&prop=pageimages&piprop=original&format=json")
        pages = d.get("query", {}).get("pages", {})
        for p in pages.values():
            if p.get("original", {}).get("source"):
                return p["original"]["source"]
    except Exception as e:
        print(f"  pageimages err {title}: {e}", file=sys.stderr)
    return None


def download(url, out: Path):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=120) as r:
        data = r.read()
    im = Image.open(io.BytesIO(data)).convert("RGB")
    out.parent.mkdir(parents=True, exist_ok=True)
    im.save(out, "JPEG", quality=92)
    return im.size, len(data) // 1024


def main():
    ok = 0
    for title, rel in FACES:
        url = get_image_url(title)
        if not url:
            print(f"  x {title}: no image url", file=sys.stderr); continue
        try:
            size, kb = download(url, IMG / rel)
            print(f"  + {title} -> {rel}  {size} {kb}KB")
            ok += 1
        except Exception as e:
            print(f"  x {title}: {e}", file=sys.stderr)
    print(f"\n{ok}/{len(FACES)} faces fetched")
    return 0 if ok == len(FACES) else 1


if __name__ == "__main__":
    sys.exit(main())
