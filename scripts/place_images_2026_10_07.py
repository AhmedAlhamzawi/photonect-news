#!/usr/bin/env python3
"""2026-10-07: all 20 frames (KIE -0.5 credits + Higgsfield 0.38 = no generation possible) sourced from
Pexels + Wikimedia Commons, hand-vetted from contact sheets. Crop to 9:16 around a
(cx, cy) centre fraction (default centre), resize 1536x2730, JPEG q92.
Writes my-video/public/images/news/2026-10-07-<slug>/ and scripts/_image_credits_2026_10_07.json.
Usage: place_images_2026_10_07.py [slug | slug/file]"""
import io, json, sys, urllib.parse, urllib.request
from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
IMG = ROOT / "my-video/public/images/news"
ONLY = sys.argv[1] if len(sys.argv) > 1 else None
UA = {"User-Agent": "PhotonectNewsBot/1.0 (https://photonect.net; ahmed@photonect.net)"}
D = "2026-10-07"
W, H = 1536, 2730

# (file, source, id, cx, cy)  source: "commons" -> File: title, "pexels" -> photo id
PLAN = {
 "a-dinar-1520-official": [
  ("hero.jpg",    "commons", "File:Central Bank of Iraq.png", 0.50, 0.5),
  ("broll_1.jpg", "pexels", 4386439, 0.50, 0.5),
  ("broll_2.jpg", "pexels", 6801680, 0.50, 0.5),
  ("broll_3.jpg", "pexels", 14866072, 0.50, 0.5),
 ],
 "b-dollar-168500-bourse": [
  ("hero.jpg",    "pexels", 14820414, 0.50, 0.5),
  ("broll_1.jpg", "pexels", 6266282, 0.50, 0.5),
  ("broll_2.jpg", "pexels", 1047305, 0.50, 0.5),
  ("broll_3.jpg", "pexels", 26668817, 0.50, 0.5),
 ],
 "c-basra-crude-china": [
  ("hero.jpg",    "pexels", 12366464, 0.50, 0.5),
  ("broll_1.jpg", "pexels", 10407692, 0.50, 0.5),
  ("broll_2.jpg", "pexels", 25685767, 0.50, 0.5),
  ("broll_3.jpg", "pexels", 15970027, 0.50, 0.5),
 ],
 "d-salahaldin-56k-receipts": [
  ("hero.jpg",    "pexels", 30350318, 0.50, 0.5),
  ("broll_1.jpg", "pexels", 4959926, 0.50, 0.5),
  ("broll_2.jpg", "pexels", 13315189, 0.50, 0.5),
  ("broll_3.jpg", "pexels", 8872400, 0.50, 0.5),
 ],
 "e-dust-139-cases": [
  ("hero.jpg",    "pexels", 19477753, 0.50, 0.5),
  ("broll_1.jpg", "pexels", 5593681, 0.50, 0.5),
  ("broll_2.jpg", "commons", "File:Dust Storm over Iraq.jpg", 0.50, 0.5),
  ("broll_3.jpg", "pexels", 39446405, 0.50, 0.5),
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
