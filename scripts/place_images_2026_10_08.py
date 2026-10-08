#!/usr/bin/env python3
"""2026-10-08: all 20 frames (KIE -0.5 credits + Higgsfield 0.38 = no generation possible) sourced from
Pexels + Wikimedia Commons, hand-vetted from contact sheets. Crop to 9:16 around a
(cx, cy) centre fraction (default centre), resize 1536x2730, JPEG q92.
Writes my-video/public/images/news/2026-10-08-<slug>/ and scripts/_image_credits_2026_10_08.json.
Usage: place_images_2026_10_08.py [slug | slug/file]"""
import io, json, sys, urllib.parse, urllib.request
from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
IMG = ROOT / "my-video/public/images/news"
ONLY = sys.argv[1] if len(sys.argv) > 1 else None
UA = {"User-Agent": "PhotonectNewsBot/1.0 (https://photonect.net; ahmed@photonect.net)"}
D = "2026-10-08"
W, H = 1536, 2730

# (file, source, id, cx, cy)  source: "commons" -> File: title, "pexels" -> photo id
PLAN = {
 "a-food-eggs-93k": [
  ("hero.jpg",    "pexels", 4199400, 0.50, 0.5),
  ("broll_1.jpg", "pexels", 11750605, 0.50, 0.5),
  ("broll_2.jpg", "pexels", 29863325, 0.50, 0.5),
  ("broll_3.jpg", "pexels", 9629685, 0.50, 0.5),
 ],
 "b-dollar-166800-1900": [
  ("hero.jpg",    "pexels", 14820414, 0.50, 0.5),
  ("broll_1.jpg", "pexels", 6266270, 0.50, 0.5),
  ("broll_2.jpg", "pexels", 5942583, 0.50, 0.5),
  ("broll_3.jpg", "commons", "File:Central Bank of Iraq.png", 0.50, 0.5),
 ],
 "c-iraqi-airways-iran-daily": [
  ("hero.jpg",    "commons", "File:Iraqi Airways, Airbus A320-214, YI-ARD (13996366772).jpg", 0.42, 0.5),
  ("broll_1.jpg", "commons", "File:AL NAJAF AL ASHRAF INT.AIRPORT - panoramio.jpg", 0.50, 0.5),
  ("broll_2.jpg", "pexels", 32874765, 0.50, 0.5),
  ("broll_3.jpg", "commons", "File:Imam Reza shrine.jpg", 0.50, 0.5),
 ],
 "d-karbala-meter-bribe": [
  ("hero.jpg",    "pexels", 32549020, 0.50, 0.5),
  ("broll_1.jpg", "pexels", 27873246, 0.50, 0.5),
  ("broll_2.jpg", "pexels", 32894669, 0.50, 0.5),
  ("broll_3.jpg", "pexels", 4096038, 0.50, 0.5),
 ],
 "e-eu-asylum-66-percent": [
  ("hero.jpg",    "pexels", 15871440, 0.50, 0.5),
  ("broll_1.jpg", "pexels", 30782813, 0.50, 0.5),
  ("broll_2.jpg", "pexels", 7654118, 0.50, 0.5),
  ("broll_3.jpg", "pexels", 14232002, 0.50, 0.5),
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
