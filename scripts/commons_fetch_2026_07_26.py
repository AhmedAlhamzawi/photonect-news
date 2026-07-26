#!/usr/bin/env python3
"""COMMONS re-source pass for the 2026-07-26 slate (round 3).

KIE is out of credits and Pexels' library keeps returning Western/European
everyday scenes with readable foreign branding for the Iraq-specific slots. For
the five slots still failing QA we go to Wikimedia Commons instead, where real
Iraq/region photography exists. Authenticity beats sharpness for a 3-second
b-roll sitting behind text overlays.

Slots and why the previous candidate was rejected:
  dollar-under-150/broll_2   Pexels money-counter read as a casino table
                             (green baize + crystal ashtray).
  ampere-price-july/broll_3  Pexels gave a motorsport pit crew hoisting a truck
                             racing engine ("Formula Truck" livery).
  us-zero-crude/broll_1      Pexels gave a snow-covered European rail tank farm
                             with "GATX" branding — wrong climate, wrong region.
  nonoil-revenue-16/hero     Dark rainy US highway w/ "HOME DEPOT" trailer.
  nonoil-revenue-16/broll_2  British cheese shop, English chalkboards, GBP.

Every download is Read-verified again after this run.
"""
from __future__ import annotations
import io, json, sys, time, urllib.parse, urllib.request
from pathlib import Path
from PIL import Image  # type: ignore

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE")
IMG_ROOT = ROOT / "my-video" / "public" / "images" / "news"
D = "2026-07-26"
UA = "PhotonectNewsBot/1.0 (https://photonect.net; ahmed@photonect.net)"

# slug/file -> ordered Commons search terms
JOBS = [
    (f"{D}-dollar-under-150", "broll_2.jpg",
     ["Central Bank of Iraq building", "Central Bank of Iraq", "Iraqi dinar banknotes"]),
    (f"{D}-ampere-price-july", "broll_3.jpg",
     ["diesel generator set", "standby diesel generator", "generator set engine"]),
    (f"{D}-us-zero-crude", "broll_1.jpg",
     ["Al Basrah Oil Terminal", "Basra oil terminal", "crude oil loading terminal offshore"]),
    (f"{D}-nonoil-revenue-16", "hero.jpg",
     ["Trebil border crossing", "Iraq border crossing trucks", "Iraqi customs checkpoint truck"]),
    (f"{D}-nonoil-revenue-16", "broll_2.jpg",
     ["Baghdad market street shop", "Iraqi market shop Baghdad", "Baghdad shop street vendor"]),
]

MIN_W = 900


def commons_search(term: str, limit: int = 14):
    q = urllib.parse.urlencode({
        "action": "query", "generator": "search", "gsrsearch": term,
        "gsrlimit": limit, "gsrnamespace": "6", "prop": "imageinfo",
        "iiprop": "url|size|extmetadata", "iiurlwidth": "1600", "format": "json",
    })
    req = urllib.request.Request("https://commons.wikimedia.org/w/api.php?" + q,
                                headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=40) as r:
        pages = json.loads(r.read().decode()).get("query", {}).get("pages", {})
    out = []
    for p in pages.values():
        ii = (p.get("imageinfo") or [{}])[0]
        title = p.get("title", "")
        if not any(title.lower().endswith(e) for e in (".jpg", ".jpeg", ".png")):
            continue
        w, h = ii.get("width") or 0, ii.get("height") or 0
        if w < MIN_W or h < 600:
            continue
        url = ii.get("thumburl") or ii.get("url")
        if url:
            out.append({"title": title, "url": url, "w": w, "h": h})
    return out


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=90) as r:
        return r.read()


def save_916(data: bytes, out: Path):
    im = Image.open(io.BytesIO(data)).convert("RGB")
    w, h = im.size
    target = 9 / 16
    if w / h > target:
        nw = int(h * target); x = (w - nw) // 2
        im = im.crop((x, 0, x + nw, h))
    else:
        nh = int(w / target); y = (h - nh) // 2
        im = im.crop((0, y, w, y + nh))
    im = im.resize((1080, 1920), Image.LANCZOS)
    out.parent.mkdir(parents=True, exist_ok=True)
    im.save(out, "JPEG", quality=92)
    return im.size


def main() -> int:
    ok = 0
    for slug, fname, terms in JOBS:
        out = IMG_ROOT / slug / fname
        done = False
        for t in terms:
            try:
                cands = commons_search(t)
            except Exception as e:
                print(f"  ! search '{t}': {e}", file=sys.stderr); time.sleep(1); continue
            if not cands:
                print(f"    (no candidates for '{t}')")
                continue
            c = cands[0]
            try:
                size = save_916(fetch(c["url"]), out)
                print(f"  OK {slug}/{fname}  term='{t}'  {size}  <- {c['title']} ({c['w']}x{c['h']})")
                ok += 1; done = True
            except Exception as e:
                print(f"  ! dl {c['title']}: {e}", file=sys.stderr)
            if done:
                break
            time.sleep(0.4)
        if not done:
            print(f"  MISSING {slug}/{fname}", file=sys.stderr)
        time.sleep(0.4)
    print(f"\n== {ok}/{len(JOBS)} sourced from Commons ==")
    return 0 if ok == len(JOBS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
