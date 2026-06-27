#!/usr/bin/env python3
"""Generate AI scenes for the 2026-06-27 slate via Nano Banana Pro 9:16 2K.
One still per beat — no cycling. Real faces (Ahmed al-Sharaa, Serena Williams)
are fetched separately into their respective broll_1.jpg, so this script skips
those two slots."""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

D = "2026-06-27"
X = "absolutely no on-screen text, no Arabic or English writing, no captions, no Instagram or app UI, no fake screenshots, no scoreboard graphics, no watermark, no logos, no brand marks, no garbled characters"

JOBS = [
    # 1. IRAQ MOSUL REVIVAL — old city, restored landmarks, museum hall, excavation
    (f"{D}-iraq-mosul-revival", "hero.jpg", f"The restored old city of Mosul Iraq at golden hour along the Tigris river, a reconstructed historic stone mosque with a tall leaning brick minaret and nearby church bell-towers freshly rebuilt, sandy honey-colored stone, warm hopeful light, wide cinematic establishing shot, {NEG}, {X}"),
    (f"{D}-iraq-mosul-revival", "broll_1.jpg", f"A beautifully restored historic Middle Eastern stone courtyard with intricate arches and a rebuilt minaret, the last construction scaffolding being removed, masons finishing carved stonework, warm afternoon light, sense of renewal, documentary wide shot, {NEG}, {X}"),
    (f"{D}-iraq-mosul-revival", "broll_2.jpg", f"Interior of a restored Mesopotamian museum hall with a large ancient Assyrian winged-bull lamassu sculpture and stone relief carvings under soft warm gallery spotlights, polished floor, reverent atmosphere, wide cinematic shot, {NEG}, {X}"),
    (f"{D}-iraq-mosul-revival", "broll_3.jpg", f"An archaeological excavation site of ancient Mesopotamian mudbrick ruins in the Iraqi sun, a partially exposed ziggurat-like terrace, archaeologists with brushes and survey gear working among the trenches, golden dust haze, documentary wide shot, {NEG}, {X}"),
    # 2. WIMBLEDON SERENA — centre court grass, (broll_1 = real Serena, fetched), player, crowd/trophy
    (f"{D}-wimbledon-serena-return", "hero.jpg", f"An immaculate pristine grass tennis centre court in an English summer, freshly mowed striped lawn, deep green ivy on the surrounding stands, soft warm afternoon light, elegant and quiet before play, wide cinematic establishing shot, no logos or text, {NEG}, {X}"),
    (f"{D}-wimbledon-serena-return", "broll_2.jpg", f"A female tennis player in crisp all-white kit mid-serve on a green grass court, ball tossed high, dynamic powerful motion, shallow depth of field, classic grass-court tennis photography, no logos or text, {NEG}, {X}"),
    (f"{D}-wimbledon-serena-return", "broll_3.jpg", f"A packed tennis stadium crowd at dusk applauding around a green grass court under warm stadium light, festive English summer atmosphere, a gleaming silver trophy on a plinth in soft focus foreground, no logos or text, {NEG}, {X}"),
    # 3. SYRIA MINORITY CABINET — Damascus skyline, (broll_1 = real al-Sharaa, fetched), cabinet room, street
    (f"{D}-syria-minority-cabinet", "hero.jpg", f"Damascus Syria skyline at tense dusk, the minarets and great dome of the historic Umayyad Mosque rising above the old city rooftops, distant hills, moody amber and grey sky, wide cinematic establishing shot, {NEG}, {X}"),
    (f"{D}-syria-minority-cabinet", "broll_2.jpg", f"A formal government cabinet meeting room with a long polished table and many empty leather chairs, neutral unmarked flag stands, soft daylight through tall windows, an austere institutional transition mood, no people, no readable text, {NEG}, {X}"),
    (f"{D}-syria-minority-cabinet", "broll_3.jpg", f"A Syrian city street with a diverse mix of ordinary civilians walking past weathered stone buildings, a quiet military checkpoint with a soldier in the background, cautious everyday life in a country in transition, documentary wide shot, no readable text, {NEG}, {X}"),
    # 4. GSK HEPATITIS CURE — research lab, vial macro, liver/virus viz, hopeful patient
    (f"{D}-gsk-hepatitis-cure", "hero.jpg", f"A modern biomedical research laboratory, a scientist in a white coat and gloves holding a pipette over a rack of glass vials, cool clean blue clinical light, advanced lab equipment behind, focused precise mood, wide cinematic shot, no readable text on screens, {NEG}, {X}"),
    (f"{D}-gsk-hepatitis-cure", "broll_1.jpg", f"An extreme macro close-up of a single clear medicine vial and a syringe on a sterile reflective lab surface, a droplet at the needle tip, soft cool light, shallow depth of field, pharmaceutical breakthrough mood, no readable label text, {NEG}, {X}"),
    (f"{D}-gsk-hepatitis-cure", "broll_2.jpg", f"An abstract glowing medical visualization of a human liver and floating virus particles being neutralized, warm gold light overtaking cold blue infection, elegant scientific 3D concept art, no labels or text, {NEG}, {X}"),
    (f"{D}-gsk-hepatitis-cure", "broll_3.jpg", f"A hopeful middle-aged patient sitting in a bright airy modern clinic by a sunlit window, calm relieved expression, a doctor's hand gently reassuring in soft focus, warm optimistic healthcare mood, no readable text, {NEG}, {X}"),
    # 5. DUBAI EMAAR MEGACITY — masterplan skyline, scale model, construction, waterfront district
    (f"{D}-dubai-emaar-megacity", "hero.jpg", f"A futuristic Dubai megacity skyline at golden dusk, clusters of sleek new glass towers under a forest of construction cranes, a vast new master-planned district rising from the desert, sweeping aerial cinematic establishing shot, no logos or text, {NEG}, {X}"),
    (f"{D}-dubai-emaar-megacity", "broll_1.jpg", f"A detailed white architectural scale model of a vast new urban district with miniature towers, parks and waterways under bright studio light, designers' hands gesturing over it, master-planning concept, shallow depth of field, no readable text, {NEG}, {X}"),
    (f"{D}-dubai-emaar-megacity", "broll_2.jpg", f"A massive Dubai construction megasite at golden hour, towering cranes lifting steel, half-built skyscrapers wrapped in scaffolding, dramatic scale of development, wide documentary shot, no logos or text, {NEG}, {X}"),
    (f"{D}-dubai-emaar-megacity", "broll_3.jpg", f"A vibrant new waterfront residential district in a Gulf city at dusk, families strolling a palm-lined promenade beside calm water, modern apartment towers glowing with warm lights, lush green public spaces, lively livable urban mood, no logos or text, {NEG}, {X}"),
    # 6. RAD-BAARG GALAXY — bow-shock galaxy, telescope array, plasma arc, researcher
    (f"{D}-radbaarg-galaxy", "hero.jpg", f"A breathtaking deep-space scene of a bright galaxy plunging through a distant galaxy cluster, ploughing up an enormous glowing curved arc of magenta and teal radio plasma shaped like a bow, set against the black star-filled cosmos, dramatic astrophysical visualization, cinematic, no labels or text, {NEG}, {X}"),
    (f"{D}-radbaarg-galaxy", "broll_1.jpg", f"A giant radio telescope dish silhouetted against a brilliant star-filled Himalayan night sky with the glowing band of the Milky Way overhead, remote mountain observatory, awe and scale, wide cinematic shot, no text, {NEG}, {X}"),
    (f"{D}-radbaarg-galaxy", "broll_2.jpg", f"An abstract close visualization of a vast curved plasma shock-wave arc of glowing teal and magenta energy sweeping across deep space, cosmic bow shock concept, intricate filaments, dark starry background, no labels or text, {NEG}, {X}"),
    (f"{D}-radbaarg-galaxy", "broll_3.jpg", f"A young researcher silhouetted in a dark observatory control room, face lit by the glow of large monitors showing abstract astronomical data and a bright spot of interest, quiet eureka moment, cinematic, no readable text, {NEG}, {X}"),
]


def submit_retry(prompt, tries=5):
    last = None
    for i in range(tries):
        try:
            return submit(prompt)
        except Exception as e:
            last = e
            time.sleep(3 * (i + 1))
    raise last


def main():
    jobs = []
    print(f"== Submitting {len(JOBS)} scene jobs (skip existing) ==", flush=True)
    for slug, fname, prompt in JOBS:
        out = IMG_ROOT / slug / fname
        if out.exists() and out.stat().st_size > 50_000:
            print(f"  = skip {slug}/{fname} (already on disk)", flush=True)
            continue
        try:
            tid = submit_retry(prompt)
            jobs.append({"slug": slug, "file": fname, "out": out, "tid": tid, "ok": False})
            print(f"  + {slug}/{fname} tid={tid}", flush=True)
        except Exception as e:
            print(f"  ! submit {slug}/{fname}: {e}", file=sys.stderr, flush=True)
        time.sleep(0.8)
    if not jobs:
        print("== nothing to generate; all on disk ==", flush=True)
        return 0
    pending = [j for j in jobs if j.get("tid")]
    print(f"\n== Polling {len(pending)} ==", flush=True)
    deadline = time.time() + 16 * 60
    while pending and time.time() < deadline:
        time.sleep(POLL_INTERVAL)
        still = []
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
                    continue
                try:
                    info = download(url, j["out"]); j["ok"] = True
                    print(f"  ✓ {j['slug']}/{j['file']} {info}", flush=True)
                except Exception as e:
                    print(f"  ! dl retry {j['slug']}/{j['file']}: {e}", file=sys.stderr, flush=True)
                    still.append(j)
            elif st == "fail":
                print(f"  ✗ {j['slug']}/{j['file']} FAIL {str(data)[:160]}", file=sys.stderr, flush=True)
            else:
                still.append(j)
        pending = still
        print(f"  ... {len(pending)} pending", flush=True)
    ok = sum(1 for j in jobs if j["ok"])
    print(f"\n== DONE {ok}/{len(JOBS)} scenes ==", flush=True)
    for j in jobs:
        if not j["ok"]:
            print(f"  MISSING {j['slug']}/{j['file']}", flush=True)
    return 0 if ok == len(JOBS) else 1


if __name__ == "__main__":
    sys.exit(main())
