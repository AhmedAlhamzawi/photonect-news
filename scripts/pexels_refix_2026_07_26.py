#!/usr/bin/env python3
"""QA RE-FIX pass for the 2026-07-26 slate.

Seven Pexels/KIE slots failed the hand Read-verify gate and are re-sourced here
with tighter queries. Rejected and why:
  dollar-under-150/broll_2   KIE gave the WORLD BANK HQ (globe+laurel emblem) —
                             a real, identifiable institution that is not an
                             Iraqi monetary authority. Reframed to an exchange
                             counter, which matches the beat (Erbil/Baghdad
                             exchange-shop rates) better than a bank facade.
  ampere-price-july/broll_2  Western candle-lit dinner party w/ pumpkins.
  ampere-price-july/broll_3  French "Garage Mongereau" ESSO forecourt — real
                             foreign brand, readable Latin signage.
  us-zero-crude/broll_1      Small fishing trawler, not an oil berth.
  us-zero-crude/broll_2      Tank farm behind a "SOYUZ(R)" branded fence.
  nonoil-revenue-16/hero     European RORO ferry deck w/ readable "Spedition
                             BODE / D-REINFELD FIN-LAHTI" livery.
  nonoil-revenue-16/broll_2  "Sovan" night kiosk, Eastern European, near-black.

Overwrites in place. Every replacement is Read-verified again after this run.
"""
from __future__ import annotations
import io, sys, time, urllib.parse, urllib.request
from pathlib import Path
from PIL import Image  # type: ignore

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE")
IMG_ROOT = ROOT / "my-video" / "public" / "images" / "news"
D = "2026-07-26"


def load_key() -> str:
    for fn in (".env.local", ".env"):
        p = ROOT / fn
        if not p.exists():
            continue
        for line in p.read_text().splitlines():
            if line.strip().startswith("PEXELS_API_KEY="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    return ""


KEY = load_key()
UA = "PhotonectNewsBot/1.0 (https://photonect.net)"

JOBS = [
    (f"{D}-dollar-under-150", "broll_2.jpg",
     ["money counting machine cash", "currency exchange counter money", "counting banknotes hands desk"]),
    (f"{D}-ampere-price-july", "broll_2.jpg",
     ["electric fan close up", "old ceiling fan room", "fan blowing summer heat"]),
    (f"{D}-ampere-price-july", "broll_3.jpg",
     ["diesel generator engine", "industrial generator machine", "power generator engine metal"]),
    (f"{D}-us-zero-crude", "broll_1.jpg",
     ["oil terminal pipeline port", "industrial pipes harbour", "refinery pipeline sea"]),
    (f"{D}-us-zero-crude", "broll_2.jpg",
     ["oil refinery industrial", "refinery towers night", "petrochemical plant industrial"]),
    (f"{D}-nonoil-revenue-16", "hero.jpg",
     ["trucks queue highway", "truck convoy road desert", "lorry driving highway line"]),
    (f"{D}-nonoil-revenue-16", "broll_2.jpg",
     ["small shop counter interior", "convenience store shelves", "market stall vendor day"]),
]


def search(query: str):
    url = "https://api.pexels.com/v1/search?" + urllib.parse.urlencode(
        {"query": query, "orientation": "portrait", "per_page": 6, "size": "large"})
    req = urllib.request.Request(url, headers={"Authorization": KEY, "User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        import json
        return json.loads(r.read().decode()).get("photos", [])


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
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
    for slug, fname, queries in JOBS:
        out = IMG_ROOT / slug / fname
        done = False
        for q in queries:
            try:
                photos = search(q)
            except Exception as e:
                print(f"  ! search '{q}': {e}", file=sys.stderr); time.sleep(1); continue
            for p in photos:
                src = p.get("src", {})
                url = src.get("large2x") or src.get("original") or src.get("large")
                if not url:
                    continue
                try:
                    size = save_916(fetch(url), out)
                    print(f"  OK {slug}/{fname}  q='{q}'  {size}  id={p.get('id')}  by={p.get('photographer')}")
                    ok += 1; done = True
                except Exception as e:
                    print(f"  ! dl: {e}", file=sys.stderr)
                break
            if done:
                break
            time.sleep(0.3)
        if not done:
            print(f"  MISSING {slug}/{fname}", file=sys.stderr)
        time.sleep(0.3)
    print(f"\n== {ok}/{len(JOBS)} re-fixed ==")
    return 0 if ok == len(JOBS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
