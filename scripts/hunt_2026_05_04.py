#!/usr/bin/env python3
"""Hunt 4 images per slug for 2026-05-04 (24 total). Pexels + Unsplash fallback."""
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
OUT_ROOT = ROOT / "cloud-media" / DATE
USED_PATH = OUT_ROOT / "_used_ids.json"


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


# slug -> { hero: [keywords...], broll1/2/3: [keywords...] }
PLAN: dict[str, dict[str, list]] = {
    "trump-project-freedom-hormuz-15000-troops": {
        "hero":   ["us navy destroyer warship", "guided missile destroyer ocean", "navy warship gulf"],
        "broll1": ["oil tanker queue port", "oil tankers row sea", "tanker fleet harbor"],
        "broll2": ["strait of hormuz aerial", "narrow strait ocean aerial", "persian gulf sea aerial"],
        "broll3": ["fighter jet f-35 silhouette", "military aircraft sky silhouette", "jet fighter takeoff"],
    },
    "iraq-zaidi-cabinet-vote-next-week": {
        "hero":   ["iraqi parliament chamber", "council of ministers baghdad", "iraq parliament building"],
        "broll1": ["iraq flag baghdad", "iraqi flag waving sky", "iraq government"],
        "broll2": ["oil pipeline desert middle east", "oil pipeline pumpjack", "iraq oil pipeline"],
        "broll3": ["baghdad city skyline night", "baghdad city night view", "iraq city night"],
    },
    "iran-fujairah-drone-uae-12-missiles": {
        "hero":   ["oil refinery flame at night", "refinery fire industrial night", "oil refinery night smoke"],
        "broll1": ["uae skyline dusk", "abu dhabi skyline night", "dubai skyline tower"],
        "broll2": ["oil tanker silhouette dawn", "oil tanker ocean sunrise", "supertanker dawn sea"],
        "broll3": ["military missile silhouette sky", "ballistic missile launch night", "military missile launch"],
    },
    "brent-114-fujairah-shock-2022-high": {
        "hero":   ["red trading screen stock", "stock market red chart screen", "trading floor red screens"],
        "broll1": ["oil pump jack pumpjack", "oil pump sunset", "oil drilling pumpjack"],
        "broll2": ["offshore oil rig persian gulf", "oil rig ocean platform", "drilling rig sea sunset"],
        "broll3": ["wall street trader screens", "trader stock exchange floor", "trading floor screens"],
    },
    "pentagon-anthropic-blacklist-classified-deals": {
        "hero":   ["pentagon building exterior", "pentagon dc aerial", "us military headquarters"],
        "broll1": ["data center server racks blue lights", "server room blue lights", "datacenter aisle"],
        "broll2": ["code on screen developer", "programming code monitor", "screen of code matrix"],
        "broll3": ["semiconductor chip macro", "computer chip macro silicon", "microchip processor closeup"],
    },
    "ukraine-mosfilm-tower-drone-moscow-victory-day": {
        "hero":   ["moscow skyline at dusk", "moscow city night kremlin", "moscow towers night"],
        "broll1": ["military drone close up sky", "uav drone military", "quadcopter military silhouette"],
        "broll2": ["smoke pillar industrial fire", "industrial fire smoke plume", "factory smoke disaster"],
        "broll3": ["fire skyscraper building night", "burning building night smoke", "fire highrise"],
    },
}


def http_get(url: str, headers: dict[str, str] | None = None, timeout: int = 30) -> bytes:
    """Use curl — Pexels' Cloudflare blocks Python urllib HTTP/1.1 fingerprint."""
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


def pexels_search(query: str, per_page: int = 18) -> list[dict]:
    if not PEXELS_KEY:
        return []
    q = urllib.parse.quote(query)
    url = f"https://api.pexels.com/v1/search?query={q}&per_page={per_page}&orientation=landscape"
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
        if mean < 25 or mean > 230:
            return False, f"luminance {mean:.1f}"
        return True, f"ok L={mean:.1f} {w}x{h} {len(buf)//1024}KB"
    except Exception as e:
        return False, f"pil err {e}"


def already_used(used: set[str], pid: int) -> bool:
    return f"pexels:{pid}" in used


def hunt_one(query_tries: list[str], used: set[str], log_prefix: str) -> tuple[bytes, dict] | None:
    # Pexels primary
    for q in query_tries:
        photos = pexels_search(q)
        time.sleep(0.4)
        for p in photos:
            pid, url = pexels_url(p)
            if not url or already_used(used, pid):
                continue
            try:
                buf = http_get(url, timeout=45)
            except Exception as e:
                print(f"    {log_prefix} dl fail {pid}: {e}", file=sys.stderr)
                continue
            ok, msg = pil_check(buf)
            if ok:
                print(f"    {log_prefix} pexels:{pid} q='{q}' {msg}")
                used.add(f"pexels:{pid}")
                return buf, {"src": "pexels", "id": str(pid), "query": q}
    # Broaden
    for q in query_tries:
        broad = q.split()[0] if q.split() else q
        if broad == q:
            continue
        photos = pexels_search(broad, per_page=24)
        time.sleep(0.4)
        for p in photos:
            pid, url = pexels_url(p)
            if not url or already_used(used, pid):
                continue
            try:
                buf = http_get(url, timeout=45)
            except Exception as e:
                print(f"    {log_prefix} dl fail {pid}: {e}", file=sys.stderr)
                continue
            ok, msg = pil_check(buf)
            if ok:
                print(f"    {log_prefix} pexels:{pid} (broad '{broad}') {msg}")
                used.add(f"pexels:{pid}")
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
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    if USED_PATH.exists():
        used_doc = json.loads(USED_PATH.read_text())
    else:
        used_doc = {"date": DATE, "source": "pexels+unsplash", "ids_by_slug": {}}

    used: set[str] = set()
    for slug_ids in used_doc.get("ids_by_slug", {}).values():
        for pid in slug_ids.values():
            if isinstance(pid, str):
                used.add(f"pexels:{pid}")

    failures: list[str] = []
    saved_count = 0

    for slug, slots in PLAN.items():
        slug_dir = OUT_ROOT / f"{DATE}-{slug}"
        slug_dir.mkdir(parents=True, exist_ok=True)
        slug_ids: dict[str, str] = used_doc.setdefault("ids_by_slug", {}).setdefault(slug, {})
        print(f"\n[{slug}]")
        slot_targets = [
            ("hero",    "hero.jpg",    slots["hero"]),
            ("broll_1", "broll_1.jpg", slots["broll1"]),
            ("broll_2", "broll_2.jpg", slots["broll2"]),
            ("broll_3", "broll_3.jpg", slots["broll3"]),
        ]
        for slot_key, filename, queries in slot_targets:
            target = slug_dir / filename
            if target.exists() and target.stat().st_size > 80 * 1024:
                ok, msg = pil_check(target.read_bytes())
                if ok:
                    print(f"  {slot_key} kept existing ({msg})")
                    saved_count += 1
                    continue
            res = hunt_one(queries, used, f"  {slot_key}")
            if res is None:
                print(f"  {slot_key} FAILED — no candidate passed", file=sys.stderr)
                failures.append(f"{slug}/{slot_key}")
                continue
            buf, meta = res
            target.write_bytes(buf)
            slug_ids[slot_key] = meta["id"]
            saved_count += 1

    USED_PATH.write_text(json.dumps(used_doc, ensure_ascii=False, indent=2))
    print(f"\nDone. Saved files this run: {saved_count}")
    if failures:
        print(f"Failures: {len(failures)}", file=sys.stderr)
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
