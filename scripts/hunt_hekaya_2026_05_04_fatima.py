#!/usr/bin/env python3
"""Hunt 18 atmospheric photos for the Hekaya v2 Fatima al-Fihri reel (2026-05-04).

Slots: hero + c1_1..5 + c2_1..5 + c3_1..5 + pivot + closing = 18 images.
Visual direction: dusk, candlelit, weathered Moroccan/Andalusian, no modern people.
Pexels primary (api), Unsplash featured fallback.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time
import urllib.parse
from io import BytesIO
from pathlib import Path

from PIL import Image  # type: ignore

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE")
ENV_PATH = ROOT / ".env.local"
DATE = "2026-05-04"
SLUG = "2026-05-04-fatima-al-fihri-qarawiyyin"
OUT_DIR = ROOT / "cloud-media" / "hekaya" / DATE / SLUG
USED_PATH = ROOT / "cloud-media" / "hekaya" / DATE / "_used_ids.json"


def load_env() -> dict[str, str]:
    env: dict[str, str] = {}
    if ENV_PATH.exists():
        for line in ENV_PATH.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip().strip('"').strip("'")
    return env


ENV = load_env()
PEXELS_KEY = ENV.get("PEXELS_API_KEY", "")


# Slot -> (filename, ordered keyword tries)
PLAN: list[tuple[str, str, list[str]]] = [
    ("hero", "hero.jpg", [
        "moroccan brass key shadow",
        "antique brass key dark",
        "old brass key wood",
        "arabic parchment hand close-up",
        "old manuscript hand pen",
        "gold coins close up brass",
    ]),
    # Chapter 1 — the world before / her inheritance / Fez context
    ("c1_1", "c1_1.jpg", [
        "fez old city alley",
        "morocco medina alleyway",
        "moroccan old town narrow street",
    ]),
    ("c1_2", "c1_2.jpg", [
        "moroccan madrasa courtyard",
        "moroccan riad courtyard",
        "marrakech madrasa interior",
    ]),
    ("c1_3", "c1_3.jpg", [
        "arabesque tile geometric",
        "moroccan zellige tile",
        "islamic geometric tile mosaic",
    ]),
    ("c1_4", "c1_4.jpg", [
        "north african old door brass",
        "moroccan wooden door studded",
        "old wooden door morocco",
    ]),
    ("c1_5", "c1_5.jpg", [
        "weathered arabic manuscript",
        "old quran pages calligraphy",
        "ancient arabic book parchment",
    ]),
    # Chapter 2 — construction / decision / determination
    ("c2_1", "c2_1.jpg", [
        "stone wall morocco worn",
        "ancient stone wall texture morocco",
        "weathered desert stone wall",
    ]),
    ("c2_2", "c2_2.jpg", [
        "moroccan archway sandstone",
        "moorish arch sandstone sunset",
        "moroccan archway dusk",
    ]),
    ("c2_3", "c2_3.jpg", [
        "moroccan calligraphy ink",
        "arabic calligraphy ink pen",
        "ink calligraphy parchment close",
    ]),
    ("c2_4", "c2_4.jpg", [
        "brass lantern hanging morocco",
        "moroccan lantern light",
        "antique brass lantern dark",
    ]),
    ("c2_5", "c2_5.jpg", [
        "carved stucco arabesque",
        "moroccan carved plaster wall",
        "alhambra stucco detail",
    ]),
    # Chapter 3 — the school endures / scholars / legacy
    ("c3_1", "c3_1.jpg", [
        "qarawiyyin courtyard",
        "fez university courtyard",
        "moroccan mosque courtyard",
    ]),
    ("c3_2", "c3_2.jpg", [
        "moroccan prayer hall pillars",
        "mosque interior columns morocco",
        "andalusian columns prayer hall",
    ]),
    ("c3_3", "c3_3.jpg", [
        "fez old gate morocco",
        "moroccan city gate stone",
        "old north african fortress gate",
    ]),
    ("c3_4", "c3_4.jpg", [
        "moroccan tile mosaic blue gold",
        "moroccan zellige blue gold",
        "moorish tile mosaic close",
    ]),
    ("c3_5", "c3_5.jpg", [
        "arabic books stack candle",
        "old books stack library candle",
        "old library candle dark",
    ]),
    # Pivot
    ("pivot", "pivot.jpg", [
        "single candle darkness",
        "candle flame dark",
        "empty courtyard moonlight",
    ]),
    # Closing
    ("closing", "closing.jpg", [
        "moroccan archway sunset light",
        "open wooden door morocco light",
        "arabesque arch sunset golden",
    ]),
]


def http_get(url: str, headers: dict[str, str] | None = None, timeout: int = 30) -> bytes:
    cmd = ["curl", "-sSL", "--max-time", str(timeout), "--retry", "2", "--retry-delay", "1",
           "-A", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"]
    if headers:
        for k, v in headers.items():
            cmd += ["-H", f"{k}: {v}"]
    cmd.append(url)
    res = subprocess.run(cmd, capture_output=True, timeout=timeout + 10)
    if res.returncode != 0:
        raise RuntimeError(f"curl rc={res.returncode}: {res.stderr.decode('utf-8', 'ignore')[:200]}")
    return res.stdout


def pexels_search(query: str, per_page: int = 24) -> list[dict]:
    if not PEXELS_KEY:
        return []
    q = urllib.parse.quote(query)
    url = f"https://api.pexels.com/v1/search?query={q}&per_page={per_page}"
    try:
        data = http_get(url, headers={"Authorization": PEXELS_KEY})
        body = json.loads(data.decode("utf-8"))
        return body.get("photos", []) or []
    except Exception as e:
        print(f"    pexels error: {e}", file=sys.stderr)
        return []


def pexels_url(photo: dict) -> tuple[int, str]:
    pid = int(photo["id"])
    src = photo.get("src", {})
    return pid, src.get("large2x") or src.get("large") or src.get("original")


def unsplash_url(keywords: list[str]) -> str:
    kw = ",".join(urllib.parse.quote(k) for k in keywords[:3])
    return f"https://source.unsplash.com/featured/1200x900/?{kw}"


def pil_check(buf: bytes) -> tuple[bool, str]:
    try:
        if len(buf) < 80 * 1024:
            return False, f"too small {len(buf)}B"
        img = Image.open(BytesIO(buf))
        img.load()
        w, h = img.size
        if max(w, h) < 1200:
            return False, f"low-res {w}x{h}"
        gs = img.convert("L")
        h_data = gs.histogram()
        total = sum(h_data)
        if total == 0:
            return False, "empty"
        mean = sum(i * c for i, c in enumerate(h_data)) / total
        # Hekaya: 25-220 (slightly darker tolerance per spec)
        if mean < 25 or mean > 220:
            return False, f"luminance {mean:.1f}"
        return True, f"ok L={mean:.1f} {w}x{h} {len(buf)//1024}KB"
    except Exception as e:
        return False, f"pil err {e}"


def hunt_one(query_tries: list[str], used: set[int], log_prefix: str) -> tuple[bytes, dict] | None:
    # Pexels primary — try each keyword
    for q in query_tries:
        photos = pexels_search(q)
        time.sleep(0.35)
        for p in photos:
            pid, url = pexels_url(p)
            if not url or pid in used:
                continue
            try:
                buf = http_get(url, timeout=45)
            except Exception as e:
                print(f"    {log_prefix} dl fail {pid}: {e}", file=sys.stderr)
                continue
            ok, msg = pil_check(buf)
            if ok:
                print(f"    {log_prefix} pexels:{pid} q='{q}' {msg}")
                used.add(pid)
                return buf, {"src": "pexels", "id": str(pid), "query": q}
    # Broaden — drop last word of each query
    for q in query_tries:
        words = q.split()
        if len(words) < 2:
            continue
        broad = " ".join(words[:-1])
        photos = pexels_search(broad, per_page=30)
        time.sleep(0.35)
        for p in photos:
            pid, url = pexels_url(p)
            if not url or pid in used:
                continue
            try:
                buf = http_get(url, timeout=45)
            except Exception:
                continue
            ok, msg = pil_check(buf)
            if ok:
                print(f"    {log_prefix} pexels:{pid} (broad '{broad}') {msg}")
                used.add(pid)
                return buf, {"src": "pexels", "id": str(pid), "query": broad}
    # Unsplash fallback
    for q in query_tries:
        kw = q.split()
        url = unsplash_url(kw)
        try:
            buf = http_get(url, timeout=30)
        except Exception as e:
            print(f"    {log_prefix} unsplash fail '{q}': {e}", file=sys.stderr)
            continue
        ok, msg = pil_check(buf)
        if ok:
            print(f"    {log_prefix} unsplash q='{q}' {msg}")
            return buf, {"src": "unsplash", "id": q.replace(' ', '_'), "query": q}
    return None


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # Load used IDs (legacy format: list of ints from prior hekaya run)
    used: set[int] = set()
    if USED_PATH.exists():
        try:
            existing = json.loads(USED_PATH.read_text())
            if isinstance(existing, list):
                used = {int(x) for x in existing if isinstance(x, (int, str)) and str(x).isdigit()}
            elif isinstance(existing, dict) and "ids" in existing:
                used = {int(x) for x in existing["ids"]}
        except Exception:
            pass

    failures: list[str] = []
    saved = 0
    slot_meta: dict[str, dict] = {}

    for slot_key, filename, queries in PLAN:
        target = OUT_DIR / filename
        # Reuse if it already exists & passes QA
        if target.exists() and target.stat().st_size > 80 * 1024:
            ok, msg = pil_check(target.read_bytes())
            if ok:
                print(f"[{slot_key}] kept existing ({msg})")
                saved += 1
                continue

        print(f"[{slot_key}]")
        res = hunt_one(queries, used, f"  {slot_key}")
        if res is None:
            print(f"  {slot_key} FAILED — no candidate passed", file=sys.stderr)
            failures.append(slot_key)
            continue
        buf, meta = res
        target.write_bytes(buf)
        slot_meta[slot_key] = meta
        saved += 1

    # Persist used IDs (merge & sort)
    USED_PATH.write_text(json.dumps(sorted(used), ensure_ascii=False))
    print(f"\nDone. Saved this run: {saved}/18")
    if failures:
        print(f"Failures: {failures}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
