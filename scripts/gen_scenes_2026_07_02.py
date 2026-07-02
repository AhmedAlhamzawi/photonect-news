#!/usr/bin/env python3
"""Cinematic AI scenes for the 2026-07-02 slate via Nano Banana Pro 9:16 2K.
Face slots handled by fetch_faces_2026_07_02.py:
  iraq hero = al-Zaidi, centcom broll_1 = Brad Cooper, michael hero = Michael Jackson, skorea broll_1 = Lee Jae-myung."""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

X = ("absolutely no on-screen text, no Arabic or English writing, no captions, no UI, no fake screenshots, "
     "no watermark, no logos, no brand marks, no garbled characters, no readable signage, no digits")

IRAQ = "2026-07-02-iraq-us-chevron-pivot"
WC = "2026-07-02-worldcup-r32-drama"
CENT = "2026-07-02-centcom-bahrain-summit"
MJ = "2026-07-02-michael-biopic-record"
TW = "2026-07-02-tianwen2-quasimoon"
KOR = "2026-07-02-skorea-chip-megaplan"

JOBS = [
    # IRAQ — US energy pivot / Chevron West Qurna 2 (hero = al-Zaidi face)
    (IRAQ, "broll_1.jpg", f"A cinematic wide aerial of a vast southern Iraq oilfield in the desert at golden dusk, rows of pumpjacks and gas flares, sprawling pipelines and storage tanks, heat haze, immense scale of a supergiant oil field, {NEG}, {X}"),
    (IRAQ, "broll_2.jpg", f"A symbolic cinematic close shot of two formal business hands shaking over a polished dark conference table beside a plain Iraqi flag and a plain American flag on small stands, an oil-deal signing mood, warm directional light, {NEG}, {X}"),
    (IRAQ, "broll_3.jpg", f"A cinematic dusk exterior of a grand American government building with classical columns and a distant Iraqi flag flying, a sense of a high-stakes Washington energy summit and foreign investment, dramatic sky, {NEG}, {X}"),
    # WORLD CUP — Round of 32 knockout drama (all scenes; no single named person)
    (WC, "hero.jpg", f"A breathtaking cinematic wide shot of a colossal packed football stadium at night during a World Cup knockout match, blazing floodlights, a sea of colorful fans and flags in the stands, electric decisive-match atmosphere, {NEG}, {X}"),
    (WC, "broll_1.jpg", f"A dynamic cinematic action shot of two football players in unmarked kits battling for the ball mid-sprint on a pristine green pitch under bright stadium lights, motion blur, intense competitive energy, {NEG}, {X}"),
    (WC, "broll_2.jpg", f"A dramatic cinematic shot of exhausted football players during extra time, hands on knees on a floodlit pitch, sweat and tension, a blurred roaring crowd behind, a sense of a match decided in the final minutes, {NEG}, {X}"),
    (WC, "broll_3.jpg", f"A cinematic emotional shot of one football team celebrating a decisive knockout goal in a pile near the corner flag while opposing players sink dejected to the grass, split fortunes, floodlit night stadium, faces not clearly visible, {NEG}, {X}"),
    # CENTCOM — 12-nation Bahrain security summit (broll_1 = Brad Cooper face)
    (CENT, "hero.jpg", f"A cinematic wide shot of a grand multinational military security summit hall, a long polished conference table ringed with many plain unmarked national flag stands and rows of empty leather chairs, dignified high-level defense conference mood, dramatic overhead lighting, no identifiable people, {NEG}, {X}"),
    (CENT, "broll_2.jpg", f"A cinematic wide shot of naval warships and a distant crude oil supertanker escorting shipping through the narrow strategic Strait of Hormuz at dawn, calm steel-blue Gulf water, hazy coastline, a sense of maritime security, {NEG}, {X}"),
    (CENT, "broll_3.jpg", f"A symbolic cinematic close shot of many small unmarked national flags of Gulf and Middle Eastern states clustered together on a summit table, a sense of new regional unity and two newcomers joining, soft warm light, no readable text, {NEG}, {X}"),
    # MICHAEL biopic record (hero = Michael Jackson face)
    (MJ, "broll_1.jpg", f"A glamorous cinematic shot of a dazzling movie premiere red carpet at night outside a grand cinema, bright marquee lights, flashing camera bulbs, an excited crowd, Hollywood blockbuster event mood, no readable text on signage, {NEG}, {X}"),
    (MJ, "broll_2.jpg", f"A dramatic cinematic silhouette of a lone iconic pop dancer mid-pose in a fedora hat under a single blazing spotlight on a vast concert stage, swirling haze, a roaring stadium crowd in darkness, electric showmanship, {NEG}, {X}"),
    (MJ, "broll_3.jpg", f"A cinematic close shot of a packed dark movie theater auditorium seen from the front, rows of silhouetted spectators watching a huge glowing blank cinema screen, a record-breaking sold-out premiere mood, {NEG}, {X}"),
    # TIANWEN-2 quasi-moon asteroid sample mission (all scenes)
    (TW, "hero.jpg", f"A breathtaking cinematic view of a sleek golden robotic space probe with wide solar panels approaching a small dark rocky asteroid the size of a city block in the deep black of space, the tiny distant Earth and Sun behind, ultra detailed, {NEG}, {X}"),
    (TW, "broll_1.jpg", f"A cinematic close view of a small irregular grey rocky near-Earth asteroid tumbling slowly in space, its cratered surface catching harsh sunlight, the blue crescent of distant Earth faint in the black cosmos, {NEG}, {X}"),
    (TW, "broll_2.jpg", f"A dramatic cinematic scene of a spacecraft's articulated robotic sampling arm reaching down to touch and grab material from the rocky surface of an asteroid, a puff of dust rising in the vacuum, precise touch-and-go maneuver, {NEG}, {X}"),
    (TW, "broll_3.jpg", f"A cinematic shot of a glowing sample-return capsule streaking through Earth's night atmosphere with a fiery orange re-entry trail, heading toward a vast dark landing zone, mission-success mood, {NEG}, {X}"),
    # SOUTH KOREA $880B chip / AI megaplan (broll_1 = Lee Jae-myung face)
    (KOR, "hero.jpg", f"A stunning cinematic wide shot inside a vast ultramodern semiconductor fabrication cleanroom, endless rows of high-tech chip-making machines bathed in amber and blue light, a technician in a full white bunny suit, immense scale of advanced manufacturing, {NEG}, {X}"),
    (KOR, "broll_2.jpg", f"An extreme cinematic macro close-up of a gleaming circular silicon semiconductor wafer covered in intricate microchip circuitry, iridescent rainbow reflections, robotic arms handling it in a spotless fab, cutting-edge technology, {NEG}, {X}"),
    (KOR, "broll_3.jpg", f"A cinematic wide shot of a futuristic AI data center and humanoid robotics assembly hall, glowing server racks and sleek robot arms, cool blue high-tech light, a sense of a massive national technology investment, {NEG}, {X}"),
]


def submit_retry(p, tries=5):
    last = None
    for i in range(tries):
        try: return submit(p)
        except Exception as e: last = e; time.sleep(3*(i+1))
    raise last


def main():
    jobs = []
    print(f"== Submitting {len(JOBS)} scene jobs ==", flush=True)
    for slug, fname, prompt in JOBS:
        out = IMG_ROOT / slug / fname
        if out.exists() and out.stat().st_size > 50_000:
            print(f"  = skip {slug}/{fname}"); continue
        try:
            tid = submit_retry(prompt)
            jobs.append({"slug": slug, "file": fname, "out": out, "tid": tid, "ok": False})
            print(f"  + {slug}/{fname} {tid}", flush=True)
        except Exception as e:
            print(f"  ! submit {slug}/{fname}: {e}", file=sys.stderr, flush=True)
        time.sleep(0.8)
    pending = [j for j in jobs if j.get("tid")]
    print(f"\n== Polling {len(pending)} ==", flush=True)
    deadline = time.time() + 18*60
    while pending and time.time() < deadline:
        time.sleep(POLL_INTERVAL)
        still = []
        for j in pending:
            try: r = http_get(f"{STATUS_URL}?taskId={j['tid']}")
            except Exception: still.append(j); continue
            data = r.get("data") or {}
            st = data.get("state")
            if st == "success":
                url = first_image_url(data)
                if not url: still.append(j); continue
                try: download(url, j["out"]); j["ok"] = True; print(f"  ✓ {j['slug']}/{j['file']}", flush=True)
                except Exception as e: print(f"  ! dl {j['slug']}/{j['file']}: {e}", file=sys.stderr); still.append(j)
            elif st == "fail":
                print(f"  ✗ {j['slug']}/{j['file']} FAIL {str(data)[:120]}", file=sys.stderr)
            else: still.append(j)
        pending = still
        print(f"  ... {len(pending)} pending", flush=True)
    ok = sum(1 for j in jobs if j["ok"])
    print(f"\n== DONE {ok}/{len(JOBS)} ==", flush=True)
    for j in jobs:
        if not j["ok"]: print(f"  MISSING {j['slug']}/{j['file']}")
    return 0 if ok == len(jobs) else 1


if __name__ == "__main__":
    sys.exit(main())
