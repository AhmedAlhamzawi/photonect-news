#!/usr/bin/env python3
"""FALLBACK media for the 2026-07-26 slate — KIE Nano Banana Pro ran out of
credits mid-run (HTTP 402) after 10/20 images, so the remaining 10 slots come
from Pexels (the engine's documented tier-2 fallback).

KIE covered (keep): audit-100tn-loans x4 (the LEAD), dollar-under-150 x4,
ampere-price-july hero + broll_1.
Pexels covers here: ampere broll_2/3, us-zero-crude x4, nonoil-revenue-16 x4.

One matched still per beat. Portrait orientation, center-cropped to 9:16, saved
as JPEG into the engine's image tree. Each slot has a list of candidate queries;
first query that returns a large-enough portrait wins. Every result is
Read-verified by hand before acceptance.
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
    # 3. AMPERE PRICE — remaining two beats
    (f"{D}-ampere-price-july", "broll_2.jpg",
     ["family home candle light", "dark room electric fan", "hot summer room fan", "power outage candle home"]),
    (f"{D}-ampere-price-july", "broll_3.jpg",
     ["diesel generator fuel", "pouring fuel jerrycan", "fuel tank refueling worker", "diesel engine generator"]),
    # 4. US ZERO CRUDE — all four
    (f"{D}-us-zero-crude", "hero.jpg",
     ["oil tanker ship sea", "crude oil tanker port", "cargo tanker ocean"]),
    (f"{D}-us-zero-crude", "broll_1.jpg",
     ["empty port dock dawn", "harbour pier empty water", "industrial port quiet morning"]),
    (f"{D}-us-zero-crude", "broll_2.jpg",
     ["oil storage tanks", "refinery tanks aerial", "petroleum tanks industry"]),
    (f"{D}-us-zero-crude", "broll_3.jpg",
     ["cargo ship open sea sunset", "tanker ship ocean dusk", "ship sailing horizon"]),
    # 5. NON-OIL REVENUE — all four
    (f"{D}-nonoil-revenue-16", "hero.jpg",
     ["trucks border crossing queue", "cargo trucks highway line", "truck convoy road"]),
    (f"{D}-nonoil-revenue-16", "broll_1.jpg",
     ["shipping containers port crane", "container terminal stacks", "port cranes containers"]),
    (f"{D}-nonoil-revenue-16", "broll_2.jpg",
     ["small shop kiosk street night", "corner store vendor", "street shop counter customer"]),
    (f"{D}-nonoil-revenue-16", "broll_3.jpg",
     ["parked cars lot aerial", "new cars parking rows", "car dealership lot"]),
]


def search(query: str):
    url = "https://api.pexels.com/v1/search?" + urllib.parse.urlencode(
        {"query": query, "orientation": "portrait", "per_page": 8, "size": "large"})
    req = urllib.request.Request(url, headers={"Authorization": KEY, "User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        import json
        return json.loads(r.read().decode()).get("photos", [])


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def save_916(data: bytes, out: Path) -> tuple:
    im = Image.open(io.BytesIO(data)).convert("RGB")
    w, h = im.size
    target = 9 / 16
    if w / h > target:
        nw = int(h * target); x = (w - nw) // 2
        im = im.crop((x, 0, x + nw, h))
    else:
        nh = int(w / target); y = (h - nh) // 2
        im = im.crop((0, y, w, y + nh))
    if im.width > 1080:
        im = im.resize((1080, 1920), Image.LANCZOS)
    out.parent.mkdir(parents=True, exist_ok=True)
    im.save(out, "JPEG", quality=92)
    return im.size


def main() -> int:
    ok = 0
    for slug, fname, queries in JOBS:
        out = IMG_ROOT / slug / fname
        if out.exists() and out.stat().st_size > 50_000:
            print(f"  = skip {slug}/{fname} (on disk)"); ok += 1; continue
        done = False
        for q in queries:
            try:
                photos = search(q)
            except Exception as e:
                print(f"  ! search '{q}' {slug}/{fname}: {e}", file=sys.stderr); time.sleep(1); continue
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
                    print(f"  ! dl {slug}/{fname}: {e}", file=sys.stderr)
                break
            if done:
                break
            time.sleep(0.3)
        if not done:
            print(f"  MISSING {slug}/{fname}", file=sys.stderr)
        time.sleep(0.3)
    print(f"\n== {ok}/{len(JOBS)} fetched ==")
    return 0 if ok == len(JOBS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
