#!/usr/bin/env python3
"""FALLBACK media for the 2026-06-28 slate — KIE Nano Banana Pro was out of
credits (HTTP 402), so we source real editorial stock from Pexels (the engine's
documented tier-2 fallback). One matched still per beat. Real faces (Fiziev,
Burhan) already fetched from Wikimedia Commons into their broll_1.jpg and are
SKIPPED here. Portrait orientation, center-cropped to 9:16, saved as JPEG into
the engine's image tree. Each slot has a list of candidate queries; first query
that returns a large-enough portrait wins."""
from __future__ import annotations
import io, sys, time, urllib.parse, urllib.request
from pathlib import Path
from PIL import Image  # type: ignore

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE")
IMG_ROOT = ROOT / "my-video" / "public" / "images" / "news"
D = "2026-06-28"


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

# slug/file -> ordered candidate queries (first good portrait wins)
JOBS = [
    # 1. IRAQ GREEN ZONE
    (f"{D}-iraq-greenzone-arrests", "hero.jpg", ["Baghdad city night", "middle east city night aerial", "city skyline night"]),
    (f"{D}-iraq-greenzone-arrests", "broll_1.jpg", ["soldiers night patrol", "military checkpoint", "armored vehicle soldiers"]),
    (f"{D}-iraq-greenzone-arrests", "broll_2.jpg", ["stacks of cash money", "pile of banknotes", "money bundles"]),
    (f"{D}-iraq-greenzone-arrests", "broll_3.jpg", ["government parliament building", "government building columns", "courthouse building"]),
    # 2. UFC BAKU (broll_1 = real Fiziev, skip)
    (f"{D}-ufc-baku-fiziev", "hero.jpg", ["boxing ring arena", "fighting cage arena", "boxing arena lights"]),
    (f"{D}-ufc-baku-fiziev", "broll_2.jpg", ["mma fighter kick", "martial arts fight", "kickboxing training"]),
    (f"{D}-ufc-baku-fiziev", "broll_3.jpg", ["stadium crowd cheering", "concert crowd lights", "arena crowd"]),
    # 3. SUDAN (broll_1 = real Burhan, skip)
    (f"{D}-sudan-burhan-deadlock", "hero.jpg", ["Nile river aerial", "Khartoum Sudan", "african river city dusk"]),
    (f"{D}-sudan-burhan-deadlock", "broll_2.jpg", ["empty conference room", "negotiation meeting room", "boardroom table chairs"]),
    (f"{D}-sudan-burhan-deadlock", "broll_3.jpg", ["refugee camp tents", "displaced people walking", "humanitarian aid camp"]),
    # 4. EXOPLANETS
    (f"{D}-exoplanets-superpuff", "hero.jpg", ["planet space cosmos", "exoplanet illustration", "planets galaxy"]),
    (f"{D}-exoplanets-superpuff", "broll_1.jpg", ["satellite space earth orbit", "space telescope stars", "satellite stars"]),
    (f"{D}-exoplanets-superpuff", "broll_2.jpg", ["jupiter gas giant planet", "planet clouds close", "gas planet space"]),
    (f"{D}-exoplanets-superpuff", "broll_3.jpg", ["scientist computer screens dark", "observatory control room", "data screens night"]),
    # 5. UAE RAIL
    (f"{D}-uae-etihad-rail", "hero.jpg", ["high speed train station", "modern train desert", "fast train dusk"]),
    (f"{D}-uae-etihad-rail", "broll_1.jpg", ["train platform passengers", "train station interior people", "modern railway platform"]),
    (f"{D}-uae-etihad-rail", "broll_2.jpg", ["railway tracks desert", "train tracks landscape", "railway aerial"]),
    (f"{D}-uae-etihad-rail", "broll_3.jpg", ["modern station architecture interior", "airport terminal interior", "futuristic transit hall"]),
    # 6. TOY STORY 5 (generic cinema only)
    (f"{D}-toystory5-record", "hero.jpg", ["cinema audience watching", "movie theater screen audience", "full cinema hall"]),
    (f"{D}-toystory5-record", "broll_1.jpg", ["cinema popcorn lobby", "popcorn movie tickets", "cinema lobby lights"]),
    (f"{D}-toystory5-record", "broll_2.jpg", ["animation studio desk", "creative studio computer color", "designer workstation colorful"]),
    (f"{D}-toystory5-record", "broll_3.jpg", ["family cinema children", "children movie theater", "family entering cinema"]),
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
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read()


def save_916(data: bytes, out: Path):
    im = Image.open(io.BytesIO(data)).convert("RGB")
    w, h = im.size
    target = 9 / 16
    # center-crop to 9:16
    if w / h > target:
        nw = int(h * target); x = (w - nw) // 2
        im = im.crop((x, 0, x + nw, h))
    else:
        nh = int(w / target); y = (h - nh) // 2
        im = im.crop((0, y, w, y + nh))
    # upscale to at least 1080x1920
    if im.width < 1080:
        im = im.resize((1080, 1920), Image.LANCZOS)
    out.parent.mkdir(parents=True, exist_ok=True)
    im.save(out, "JPEG", quality=90)
    return im.size


def main():
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
                    data = fetch(url)
                    size = save_916(data, out)
                    print(f"  ✓ {slug}/{fname}  q='{q}'  {size}  id={p.get('id')}  by={p.get('photographer')}")
                    ok += 1; done = True; break
                except Exception as e:
                    print(f"  ! dl {slug}/{fname}: {e}", file=sys.stderr)
            if done:
                break
            time.sleep(0.4)
        if not done:
            print(f"  MISSING {slug}/{fname}", file=sys.stderr)
        time.sleep(0.3)
    print(f"\n== {ok}/{len(JOBS)} fetched ==")
    return 0 if ok == len(JOBS) else 1


if __name__ == "__main__":
    sys.exit(main())
