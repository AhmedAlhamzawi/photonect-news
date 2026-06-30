#!/usr/bin/env python3
"""Cinematic AI scenes for the 2026-06-30 slate via Nano Banana Pro 9:16 2K.
Skips the 3 real-face slots (Lewandowski hero, Witkoff broll_1, Mona Zaki broll_2)."""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

X = ("absolutely no on-screen text, no Arabic or English writing, no captions, no UI, no fake screenshots, "
     "no watermark, no logos, no brand marks, no garbled characters, no readable signage")

GRID = "2026-06-30-iraq-grid-summer-deficit"
DOHA = "2026-06-30-iran-doha-frozen-assets"
LEWA = "2026-06-30-lewandowski-mls-chicago"
LONG = "2026-06-30-china-longcat-no-nvidia"
SAUD = "2026-06-30-saudi-engineering-saudization"
UMMK = "2026-06-30-umm-kulthum-biopic-us"

JOBS = [
    # IRAQ GRID (all scenes)
    (GRID, "hero.jpg", f"Cinematic wide aerial of an Iraqi electrical grid at dusk in scorching summer, high-voltage transmission towers and power lines stretching across a hazy desert city, heat shimmer, scattered city lights flickering on, tense energy-crisis mood, {NEG}, {X}"),
    (GRID, "broll_1.jpg", f"Interior of a large thermal power station with massive turbines and generators, control gauges, warm industrial light, strained hardworking atmosphere, wide cinematic shot, {NEG}, {X}"),
    (GRID, "broll_2.jpg", f"A symbolic shot of an old electricity meter on a cracked concrete wall in a Middle Eastern neighborhood at dusk, tangled overhead power cables, a sense of unpaid bills and strain, moody light, {NEG}, {X}"),
    (GRID, "broll_3.jpg", f"A vast natural gas pipeline with a flickering gas flare stack against a dusk desert sky, industrial energy infrastructure, dramatic silhouette, wide cinematic shot, {NEG}, {X}"),
    # IRAN-DOHA (broll_1 = Witkoff face)
    (DOHA, "hero.jpg", f"Cinematic wide shot of a tense high-level diplomatic negotiation room in Doha Qatar, an empty long polished table with microphones and water glasses, blurred Gulf skyline through tall windows at dusk, plain flag stands, charged anticipatory mood, {NEG}, {X}"),
    (DOHA, "broll_2.jpg", f"A symbolic cinematic shot of neat stacks of banknotes locked behind a heavy steel bank-vault door, cold blue security light, themes of frozen assets, no readable text on the money, {NEG}, {X}"),
    (DOHA, "broll_3.jpg", f"A dramatic close shot of an old clock face beside a formal signed agreement document on a dark desk, soft directional light, a sense of a ticking deadline, no readable text, {NEG}, {X}"),
    # LEWANDOWSKI (hero = his face)
    (LEWA, "broll_1.jpg", f"A vibrant Major League Soccer stadium at night, packed crowd, bright floodlights on a green pitch, festive American soccer atmosphere, wide cinematic shot, {NEG}, {X}"),
    (LEWA, "broll_2.jpg", f"A lone soccer ball on a pristine floodlit pitch at dusk with a vast empty modern stadium behind, a sense of a big decision and a new chapter, cinematic, {NEG}, {X}"),
    (LEWA, "broll_3.jpg", f"Close cinematic shot of soccer boots and a ball on dewy green grass under bright stadium lights, dynamic sporting mood, shallow depth of field, {NEG}, {X}"),
    # CHINA LONGCAT (all scenes — NO fake UI/screens)
    (LONG, "hero.jpg", f"Cinematic wide shot of a vast modern AI data center, endless rows of glowing server racks receding into the distance, cool blue and teal light, cables and cooling systems, immense computational power, no screens, {NEG}, {X}"),
    (LONG, "broll_1.jpg", f"An extreme macro close-up of an advanced AI computer processor chip on a circuit board, glowing micro-circuitry, cool clinical light, cutting-edge semiconductor, no markings, {NEG}, {X}"),
    (LONG, "broll_2.jpg", f"A massive server cluster hall with thousands of accelerator cards in racks, blue indicator lights, cooling pipes, a colossal compute farm, wide cinematic shot, no screens, {NEG}, {X}"),
    (LONG, "broll_3.jpg", f"An abstract cinematic visualization of a glowing neural network of interconnected nodes and data streams in deep blue and gold, powerful AI concept, no labels, {NEG}, {X}"),
    # SAUDI SAUDIZATION (all scenes)
    (SAUD, "hero.jpg", f"Cinematic wide shot of a modern Saudi Arabian construction megasite at golden hour, engineers in hard hats and high-vis vests with blueprints, towering cranes and a gleaming Riyadh skyline behind, national workforce ambition, {NEG}, {X}"),
    (SAUD, "broll_1.jpg", f"A group of engineers in hard hats and high-vis vests reviewing plans on a tablet at a modern construction site, focused professional mood, warm light, no readable screen text, {NEG}, {X}"),
    (SAUD, "broll_2.jpg", f"A symbolic cinematic shot of an engineer's hands signing a formal employment contract on a desk beside a hard hat, soft office light, themes of labor policy, no readable text, {NEG}, {X}"),
    (SAUD, "broll_3.jpg", f"A quiet stalled construction site at dusk with idle cranes and an unfinished office tower under a moody sky, a sense of regulatory pressure, wide cinematic shot, {NEG}, {X}"),
    # UMM KULTHUM (hero = scene; broll_2 = Mona Zaki face)
    (UMMK, "hero.jpg", f"A cinematic evocative scene of a legendary mid-20th-century Arab diva performing on a grand ornate concert-hall stage, a lone elegant female singer in a flowing gown holding a handkerchief under a warm golden spotlight, a full orchestra in silhouette, opulent vintage 1960s Cairo theater, reverent nostalgic mood, {NEG}, {X}"),
    (UMMK, "broll_1.jpg", f"A grand vintage cinema auditorium with rich red velvet seats and a softly glowing screen, ornate golden details, warm nostalgic light, the magic of classic film, wide cinematic shot, {NEG}, {X}"),
    (UMMK, "broll_3.jpg", f"A cinematic shot of a classic movie-theater marquee and red carpet at night glowing with warm lights, an elegant film-premiere atmosphere, no readable letters on the marquee, {NEG}, {X}"),
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
