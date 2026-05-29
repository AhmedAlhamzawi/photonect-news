#!/usr/bin/env python3
"""Generate 24 accurate, NON-generic editorial images for the 2026-05-28 slate
via KIE.ai Nano Banana Pro (Gemini 3 Pro Image), 9:16, 2K.

Submit-all-then-poll-all for speed. Saves directly into the engine's image dirs.
Reads KIE_AI_API_KEY from .env / .env.local.
"""
from __future__ import annotations

import io
import json
import os
import sys
import time
import urllib.request
from pathlib import Path

from PIL import Image  # type: ignore

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE")
IMG_ROOT = ROOT / "my-video" / "public" / "images" / "news"

KIE_BASE = "https://api.kie.ai"
CREATE_URL = f"{KIE_BASE}/api/v1/jobs/createTask"
STATUS_URL = f"{KIE_BASE}/api/v1/jobs/recordInfo"
MODEL = "nano-banana-pro"
CALLBACK = "https://webhook.site/00000000-0000-0000-0000-000000000000"
POLL_INTERVAL = 8
MAX_MIN = 14


def load_key() -> str:
    for fn in (".env.local", ".env"):
        p = ROOT / fn
        if not p.exists():
            continue
        for line in p.read_text().splitlines():
            line = line.strip()
            if line.startswith("KIE_AI_API_KEY=") and "=" in line:
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    return os.environ.get("KIE_AI_API_KEY", "").strip()


API_KEY = load_key()

NEG = "ultra-realistic editorial photojournalism, cinematic lighting, vertical 9:16 composition, no on-screen text, no captions, no watermark, no logos"

# slug -> [(slot_filename, prompt)]
PLAN: dict[str, list[tuple[str, str]]] = {
    "2026-05-28-humain-xai-fund": [
        ("hero.jpg", f"Establishing shot inside a vast hyperscale AI data center in Saudi Arabia, endless symmetrical rows of tall black server racks glowing with cool blue and cyan indicator lights, polished reflective floor, dramatic vanishing-point perspective, immense scale, {NEG}"),
        ("broll_1.jpg", f"Riyadh Saudi Arabia skyline at golden dusk, the distinctive Kingdom Centre tower with its inverted-arch opening and the pointed Al Faisaliah tower, dense modern capital, warm gold and deep blue sky, hazy desert light, aerial wide shot, {NEG}"),
        ("broll_2.jpg", f"Extreme close-up of cutting-edge AI GPU server hardware, dense green circuit boards and gold connectors, thick bundles of orange and blue fiber-optic cables, rows of green and amber status LEDs, shallow depth of field, {NEG}"),
        ("broll_3.jpg", f"The national flag of Saudi Arabia, a solid green field with white Arabic calligraphy above a white horizontal sword, flying on a tall pole in front of a sleek modern glass technology campus, clear blue sky, low heroic angle, {NEG}"),
    ],
    "2026-05-28-iran-us-ceasefire": [
        ("hero.jpg", f"Tehran Iran cityscape at dusk, the tall white needle-like Milad Tower rising above a sprawling dense capital city, distant snow-capped Alborz mountains, hazy golden-grey sky, aerial wide establishing shot, {NEG}"),
        ("broll_1.jpg", f"A young Iranian man on a Tehran street at night looking down at his glowing smartphone with a freshly restored signal, warm blurred city lights and neon shop signs in bokeh behind him, quiet hopeful mood, {NEG}"),
        ("broll_2.jpg", f"A formal diplomatic negotiation room, a long polished wooden table with the flag of the United States and the flag of Iran standing upright facing each other, empty leather chairs, neutral mediator setting, soft window light, no people, {NEG}"),
        ("broll_3.jpg", f"Aerial view of a massive crude oil supertanker crossing the Strait of Hormuz at dawn, calm steel-blue Persian Gulf water, faint hazy coastline, strategic tension, cinematic wide shot, {NEG}"),
    ],
    "2026-05-28-iraq-cabinet-crisis": [
        ("hero.jpg", f"Interior of a modern Iraqi parliamentary chamber, curved rows of seats with several conspicuously empty, the flag of Iraq (red, white and black horizontal bands with green Arabic script) on the front wall, formal Arab government assembly hall, dramatic overhead lighting, {NEG}"),
        ("broll_1.jpg", f"Baghdad Iraq at night, the iconic Victory Arch crossed-swords monument floodlit, city skyline along the Tigris river, warm lights reflecting on the water, deep blue night sky, wide establishing aerial shot, {NEG}"),
        ("broll_2.jpg", f"Iraqi army soldiers in desert camouflage at a security checkpoint in Baghdad, an armored Humvee behind them, alert tense posture, overcast daylight, documentary photojournalism, {NEG}"),
        ("broll_3.jpg", f"A large concrete dam and reservoir on the Tigris river in Iraq, vast turquoise water body behind the spillway, arid mountains, water-management infrastructure, daylight aerial wide shot, {NEG}"),
    ],
    "2026-05-28-saudi-uae-rivalry": [
        ("hero.jpg", f"The national flag of Saudi Arabia (green with white calligraphy and sword) and the national flag of the United Arab Emirates (a red vertical bar with green, white and black horizontal bands) flying side by side on two tall flagpoles against a dramatic cloudy dusk sky, low heroic angle, sense of contrast and rivalry, {NEG}"),
        ("broll_1.jpg", f"Riyadh Saudi Arabia, the King Abdullah Financial District cluster of distinctive modern skyscrapers at dusk, warm desert haze, wide aerial establishing shot, {NEG}"),
        ("broll_2.jpg", f"Abu Dhabi UAE skyline at dusk, the curved Etihad Towers and the corniche waterfront, calm Gulf water in front, glowing city lights, wide aerial establishing shot, {NEG}"),
        ("broll_3.jpg", f"An oil pumpjack and pipeline infrastructure in the Arabian desert at sunset, burnt-orange sky, long shadows, heat haze, sense of petro-power, cinematic wide shot, {NEG}"),
    ],
    "2026-05-28-uae-ai-government": [
        ("hero.jpg", f"The Museum of the Future in Dubai at dusk, the iconic silver torus-shaped building covered in flowing Arabic calligraphy window cut-outs, illuminated against the Dubai skyline, futuristic, wide cinematic establishing shot, {NEG}"),
        ("broll_1.jpg", f"A sleek modern UAE government smart-service center, a person using a glowing interactive touchscreen kiosk showing an abstract digital government dashboard, clean minimalist Emirati architecture, cool blue lighting, {NEG}"),
        ("broll_2.jpg", f"Interior of a sovereign AI data center in the United Arab Emirates, rows of advanced server racks with crisp blue and white lighting, an Emirati engineer in business attire walking the aisle, high-tech clean environment, cinematic depth, {NEG}"),
        ("broll_3.jpg", f"Abu Dhabi UAE at night, futuristic skyline with the leaning Capital Gate tower and the Etihad Towers, glowing lights, deep blue sky, wide aerial establishing shot, {NEG}"),
    ],
    "2026-05-28-uae-opec-exit": [
        ("hero.jpg", f"A formal OPEC oil ministers summit hall, a large circular conference table ringed with the national flags of oil-producing nations, empty leather chairs, modern wood-paneled international conference room, dramatic chandelier lighting, no identifiable people, {NEG}"),
        ("broll_1.jpg", f"Aerial wide shot of a giant crude oil supertanker riding low in the water crossing the calm Persian Gulf at dawn, golden light on a steel-blue sea, distant coastline, {NEG}"),
        ("broll_2.jpg", f"A massive oil refinery and petrochemical complex in the UAE at night, glowing gas flares, webs of illuminated pipes and distillation towers, rising steam, dramatic industrial nightscape, wide aerial shot, {NEG}"),
        ("broll_3.jpg", f"A financial trading floor with large screens showing rising oil-price line charts and candlestick graphs in red and green, blurred traders in the foreground, tense market mood, {NEG}"),
    ],
}


def http_post(url: str, body: dict) -> dict:
    req = urllib.request.Request(
        url, data=json.dumps(body).encode("utf-8"), method="POST",
        headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json", "Accept": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


def http_get(url: str) -> dict:
    req = urllib.request.Request(
        url, method="GET",
        headers={"Authorization": f"Bearer {API_KEY}", "Accept": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


def submit(prompt: str) -> str:
    body = {
        "model": MODEL,
        "callBackUrl": CALLBACK,
        "input": {
            "prompt": prompt,
            "image_input": [],
            "aspect_ratio": "9:16",
            "resolution": "2K",
            "output_format": "jpg",
        },
    }
    r = http_post(CREATE_URL, body)
    if r.get("code") != 200:
        raise RuntimeError(f"submit failed: {r!r}")
    tid = (r.get("data") or {}).get("taskId")
    if not tid:
        raise RuntimeError(f"no taskId: {r!r}")
    return tid


def first_image_url(data: dict) -> str | None:
    rj = data.get("resultJson")
    if isinstance(rj, str):
        try:
            urls = (json.loads(rj).get("resultUrls") or [])
            if urls:
                return urls[0]
        except Exception:
            pass

    def walk(o):
        if isinstance(o, dict):
            for v in o.values():
                if isinstance(v, str) and v.startswith("http") and any(s in v.lower() for s in (".png", ".jpg", ".jpeg", ".webp")):
                    return v
                got = walk(v)
                if got:
                    return got
        elif isinstance(o, list):
            for it in o:
                got = walk(it)
                if got:
                    return got
        return None
    return walk(data)


def download(url: str, out: Path) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=120) as r:
        data = r.read()
    im = Image.open(io.BytesIO(data))
    im.load()
    out.parent.mkdir(parents=True, exist_ok=True)
    im.convert("RGB").save(out, "JPEG", quality=92)
    return f"{len(data)//1024}KB {im.size[0]}x{im.size[1]}"


def main() -> int:
    if not API_KEY:
        print("ERROR: KIE_AI_API_KEY not found", file=sys.stderr)
        return 2

    # Optional slug filter via argv (regenerate a subset)
    only = set(sys.argv[1:])

    jobs: list[dict] = []  # {slug, file, prompt, out, tid, done}
    print("== Submitting jobs ==", flush=True)
    for slug, slots in PLAN.items():
        if only and slug not in only:
            continue
        for fname, prompt in slots:
            out = IMG_ROOT / slug / fname
            try:
                tid = submit(prompt)
                jobs.append({"slug": slug, "file": fname, "out": out, "tid": tid, "done": False, "ok": False})
                print(f"  + {slug}/{fname}  tid={tid}", flush=True)
            except Exception as e:
                print(f"  ! submit error {slug}/{fname}: {e}", file=sys.stderr, flush=True)
                jobs.append({"slug": slug, "file": fname, "out": out, "tid": None, "done": True, "ok": False})
            time.sleep(0.5)

    pending = [j for j in jobs if j["tid"]]
    print(f"\n== Polling {len(pending)} jobs ==", flush=True)
    deadline = time.time() + MAX_MIN * 60
    while pending and time.time() < deadline:
        time.sleep(POLL_INTERVAL)
        still: list[dict] = []
        for j in pending:
            try:
                r = http_get(f"{STATUS_URL}?taskId={j['tid']}")
            except Exception:
                still.append(j); continue
            data = r.get("data") or {}
            st = data.get("state")
            if st == "success":
                url = first_image_url(data)
                if not url:
                    print(f"  ? {j['slug']}/{j['file']}: success but no url", file=sys.stderr, flush=True)
                    j["done"] = True; continue
                try:
                    info = download(url, j["out"])
                    j["done"] = True; j["ok"] = True
                    print(f"  ✓ {j['slug']}/{j['file']}  {info}", flush=True)
                except Exception as e:
                    print(f"  ! download {j['slug']}/{j['file']}: {e}", file=sys.stderr, flush=True)
                    j["done"] = True
            elif st == "fail":
                print(f"  ✗ {j['slug']}/{j['file']}: FAIL {str(data)[:160]}", file=sys.stderr, flush=True)
                j["done"] = True
            else:
                still.append(j)
        pending = still
        if pending:
            print(f"    ... {len(pending)} still generating", flush=True)

    ok = sum(1 for j in jobs if j["ok"])
    print(f"\n== Done. {ok}/{len(jobs)} generated ==", flush=True)
    fails = [f"{j['slug']}/{j['file']}" for j in jobs if not j["ok"]]
    if fails:
        print("FAILURES:", file=sys.stderr)
        for f in fails:
            print(f"  - {f}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
