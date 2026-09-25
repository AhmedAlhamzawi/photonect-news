#!/usr/bin/env python3
"""2026-09-25: all 20 frames (KIE 11.5 credits + Higgsfield 0.38 = no generation possible) sourced from
Pexels + Wikimedia Commons, hand-vetted from contact sheets. Crop to 9:16 around a
(cx, cy) centre fraction (default centre), resize 1536x2730, JPEG q92.
Writes my-video/public/images/news/2026-09-25-<slug>/ and scripts/_image_credits_2026_09_25.json.
Usage: place_images_2026_09_25.py [slug | slug/file]"""
import io, json, sys, urllib.parse, urllib.request
from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
IMG = ROOT / "my-video/public/images/news"
ONLY = sys.argv[1] if len(sys.argv) > 1 else None
UA = {"User-Agent": "PhotonectNewsBot/1.0 (https://photonect.net; ahmed@photonect.net)"}
D = "2026-09-25"
W, H = 1536, 2730

# (file, source, id, cx, cy)  source: "commons" -> File: title, "pexels" -> photo id
PLAN = {
 "a-oil-theft-500-million": [
  ("hero.jpg",    "pexels", 10965266, 0.50, 0.5),
  ("broll_1.jpg", "pexels", 10965344, 0.50, 0.5),
  ("broll_2.jpg", "pexels", 20333182, 0.50, 0.5),
  ("broll_3.jpg", "pexels", 35827232, 0.50, 0.5),
 ],
 "b-dollar-friday-spread": [
  ("hero.jpg",    "pexels", 4968383, 0.50, 0.5),
  ("broll_1.jpg", "pexels", 1047305, 0.50, 0.5),
  ("broll_2.jpg", "pexels", 6266280, 0.50, 0.5),
  ("broll_3.jpg", "pexels", 35827231, 0.50, 0.5),
 ],
 "c-najaf-iran-flights": [
  ("hero.jpg",    "commons", "File:AL NAJAF AL ASHRAF INT.AIRPORT - panoramio.jpg", 0.40, 0.5),
  ("broll_1.jpg", "pexels", 16527397, 0.50, 0.5),
  ("broll_2.jpg", "commons", "File:2 10 2023 Iraq’s Deputy Prime Minister and Foreign Minister Fuad Hussein (52702799764).jpg", 0.40, 0.4),
  ("broll_3.jpg", "pexels", 10905771, 0.50, 0.5),
 ],
 "d-somo-oil-buyers": [
  ("hero.jpg",    "pexels", 12366464, 0.50, 0.5),
  ("broll_1.jpg", "pexels", 25685767, 0.50, 0.5),
  ("broll_2.jpg", "pexels", 10407692, 0.50, 0.5),
  ("broll_3.jpg", "pexels", 15475599, 0.50, 0.5),
 ],
 "e-syria-petrol-baniyas": [
  ("hero.jpg",    "pexels", 39114829, 0.50, 0.5),
  ("broll_1.jpg", "commons", "File:Baniyas sept 2009 3714.jpg", 0.55, 0.5),
  ("broll_2.jpg", "pexels", 36488828, 0.50, 0.5),
  ("broll_3.jpg", "pexels", 31161428, 0.50, 0.5),
 ],
}


def pexels_key():
    for fn in (".env.local", ".env"):
        p = ROOT / fn
        if p.exists():
            for l in p.read_text().splitlines():
                if l.startswith("PEXELS_API_KEY="):
                    return l.split("=", 1)[1].strip().strip('"').strip("'")


def get(url, headers=UA):
    return urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=120).read()


def resolve(src, ident):
    if src == "pexels":
        ph = json.loads(get(f"https://api.pexels.com/v1/photos/{ident}", {**UA, "Authorization": pexels_key()}))
        url = ph["src"]["original"]
        meta = {"src": "pexels", "title": ph.get("alt", ""), "page": ph["url"], "artist": ph["photographer"], "license": "Pexels License"}
    else:
        q = urllib.parse.urlencode({"action": "query", "format": "json", "titles": ident, "prop": "imageinfo", "iiprop": "url|size|extmetadata"})
        pg = next(iter(json.loads(get("https://commons.wikimedia.org/w/api.php?" + q))["query"]["pages"].values()))
        ii = pg["imageinfo"][0]; md = ii.get("extmetadata", {})
        url = ii["url"]
        meta = {"src": "commons", "title": ident, "page": ii["descriptionurl"],
                "artist": md.get("Artist", {}).get("value", "")[:200], "license": md.get("LicenseShortName", {}).get("value", "")}
    return url, meta


def crop(im, cx, cy):
    r = W / H
    if im.width / im.height > r:
        nw = int(im.height * r); x = int(min(max(cx * im.width - nw / 2, 0), im.width - nw))
        im = im.crop((x, 0, x + nw, im.height))
    else:
        nh = int(im.width / r); y = int(min(max(cy * im.height - nh / 2, 0), im.height - nh))
        im = im.crop((0, y, im.width, y + nh))
    return im.resize((W, H), Image.LANCZOS)


cp = ROOT / f"scripts/_image_credits_{D.replace('-', '_')}.json"
credits = json.load(open(cp)) if cp.exists() else {}
for slug, jobs in PLAN.items():
    out = IMG / f"{D}-{slug}"; out.mkdir(parents=True, exist_ok=True)
    for f, src, ident, cx, cy in jobs:
        key = f"{slug}/{f}"
        if ONLY and ONLY not in (key, slug):
            continue
        url, meta = resolve(src, ident)
        im = ImageOps.exif_transpose(Image.open(io.BytesIO(get(url)))).convert("RGB")
        crop(im, cx, cy).save(out / f, "JPEG", quality=92)
        credits[key] = meta
        print(f"{key} <- {src} {str(ident)[:70]} ({im.width}x{im.height})")
json.dump(credits, open(cp, "w"), ensure_ascii=False, indent=1)
