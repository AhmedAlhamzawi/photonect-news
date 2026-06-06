#!/usr/bin/env python3
"""Generate the 23 non-face AI scenes for 2026-06-06 via Nano Banana Pro (9:16, 2K).
Real face fetched separately: Muqtada al-Sadr -> iraq-new-government broll_3.
Every scene prompt MATCHES its target beat's text. Bright lighting to clear engine
luminance floors. Extra-strong no-text/no-UI negatives (KIE screenshot guard) —
critical on the OpenAI/ChatGPT story, which must NOT render a fake app screenshot."""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

D = "2026-06-06"
GUARD = "absolutely no text, no captions, no Instagram or app UI, no phone screen, no chat interface, no user interface, no watermark, no logos, no brand marks, photorealistic editorial photograph"

JOBS = [
    # 1. IRAQ NEW GOVERNMENT (hero/broll_1/broll_2 generated; broll_3 = real al-Sadr)
    (f"{D}-iraq-new-government", "hero.jpg", f"The grand interior of an Iraqi parliamentary assembly chamber in bright daylight, curved tiers of empty seats, the flag of Iraq (red white black horizontal bands with green Arabic script) on the front wall, formal Arab government hall, wide cinematic establishing shot, no people, {GUARD}, {NEG}"),
    (f"{D}-iraq-new-government", "broll_1.jpg", f"A stately Iraqi government ministry building with the national flag of Iraq flying on a tall pole out front under a bright clear sky, sandstone facade, formal seat of power, wide low heroic establishing shot, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-iraq-new-government", "broll_2.jpg", f"Iraqi army and security forces in desert camouflage standing at a checkpoint in Baghdad beside an armored vehicle, alert posture under bright daylight, symbolizing vacant defense and interior ministries, documentary photojournalism, distant figures with no recognizable faces, {GUARD}, {NEG}"),
    # 2. LEBANON CEASEFIRE STRAINS (all 3 generated, tasteful — no bodies)
    (f"{D}-lebanon-ceasefire-strains", "hero.jpg", f"A southern Lebanese hillside village at dusk with a damaged concrete building and a distant column of grey smoke rising on the horizon, somber tense aftermath atmosphere, no people, no bodies, wide cinematic establishing shot, {GUARD}, {NEG}"),
    (f"{D}-lebanon-ceasefire-strains", "broll_1.jpg", f"A quiet southern Lebanon rural town with stone houses and olive groves under a hazy sky, a faint plume of smoke far on the horizon, tense fragile-ceasefire mood, daylight wide shot, no people, no bodies, {GUARD}, {NEG}"),
    (f"{D}-lebanon-ceasefire-strains", "broll_2.jpg", f"A calm river winding through a green border valley in southern Lebanon at golden hour, the Litani river, reeds along the banks, strategic frontier landscape, wide cinematic aerial shot, no people, {GUARD}, {NEG}"),
    (f"{D}-lebanon-ceasefire-strains", "broll_3.jpg", f"A grey naval destroyer warship at sea in the Persian Gulf at dusk firing a defensive missile interceptor against a small drone, distant haze, tense military standoff near the Strait of Hormuz, wide cinematic shot, no recognizable faces, {GUARD}, {NEG}"),
    # 3. OIL WAR ECONOMY (all 4 generated)
    (f"{D}-oil-war-economy", "hero.jpg", f"A massive crude oil supertanker crossing the Strait of Hormuz at dusk, calm steel-blue Persian Gulf water, faint hazy coastline and distant tankers, strategic energy chokepoint, cinematic wide aerial establishing shot, no text, {GUARD}, {NEG}"),
    (f"{D}-oil-war-economy", "broll_1.jpg", f"Rows of large industrial crude oil storage tanks and pipelines at a refinery under bright daylight, gleaming steel infrastructure, sense of global oil supply, wide cinematic establishing shot, no people, no text, {GUARD}, {NEG}"),
    (f"{D}-oil-war-economy", "broll_2.jpg", f"A huge container and tanker port in China at dawn with rows of cranes and a docked oil tanker, vast harbour, cooling global energy demand, wide aerial establishing shot, no readable text, {GUARD}, {NEG}"),
    (f"{D}-oil-war-economy", "broll_3.jpg", f"An oil export terminal and refinery on the coast of Oman at dusk with a tall flaring stack and jetty reaching into the calm sea, fragile Gulf supply, wide cinematic shot, no people, no text, {GUARD}, {NEG}"),
    # 4. OPENAI MEMORY UPGRADE (all 4 generated — STRICT no-UI, no screenshot)
    (f"{D}-openai-memory-upgrade", "hero.jpg", f"A glowing abstract three-dimensional artificial-intelligence neural network shaped softly like a human brain, bright blue and teal nodes and flowing light connections on a dark background, concept of machine memory, clean futuristic 3D render, {GUARD}, {NEG}"),
    (f"{D}-openai-memory-upgrade", "broll_1.jpg", f"A person sitting at a bright modern desk using a laptop, soft warm window light, the laptop screen glowing blank and out of focus showing only abstract soft light, no readable content, shallow depth of field, candid lifestyle photograph, face not clearly recognizable, no screen text, no app interface, {GUARD}, {NEG}"),
    (f"{D}-openai-memory-upgrade", "broll_2.jpg", f"An abstract visualization of data being synthesized, many small streams of glowing blue particles converging into a single bright orb of light on a dark background, concept of background memory consolidation, clean 3D render, no text, {GUARD}, {NEG}"),
    (f"{D}-openai-memory-upgrade", "broll_3.jpg", f"A glowing blue digital globe of the Earth wrapped in a soft web of bright network connection lines and points of light, concept of a global software rollout, dark background, clean futuristic 3D render, no text, no labels, {GUARD}, {NEG}"),
    # 5. NBA FINALS KNICKS SPURS (all 4 generated, generic no-logo)
    (f"{D}-nba-finals-knicks-spurs", "hero.jpg", f"A vast packed indoor basketball arena at night under brilliant white lights, a glowing polished hardwood court below tiers of cheering crowds, electric championship-final atmosphere, wide cinematic establishing shot, no recognizable faces, no logos, no readable text, no jersey numbers, {GUARD}, {NEG}"),
    (f"{D}-nba-finals-knicks-spurs", "broll_1.jpg", f"A basketball dropping cleanly through the hoop and net in a brightly lit arena, motion frozen, blurred crowd in the background, dynamic sports moment, no recognizable faces, no logos, no text, {GUARD}, {NEG}"),
    (f"{D}-nba-finals-knicks-spurs", "broll_2.jpg", f"A roaring basketball arena crowd celebrating with raised arms under bright lights, sea of fans in silhouette and bokeh, jubilant playoff atmosphere, no recognizable faces, no readable text, no logos, {GUARD}, {NEG}"),
    (f"{D}-nba-finals-knicks-spurs", "broll_3.jpg", f"A gleaming generic golden basketball championship trophy standing on a dark plinth under a single dramatic spotlight, polished metal reflections, prestige and anticipation, plain dark background, no logos, no brand marks, no text, {GUARD}, {NEG}"),
    # 6. MAVEN MARS FINALE (all 4 generated)
    (f"{D}-maven-mars-finale", "hero.jpg", f"The planet Mars as a rusty red sphere filling the frame against the black of space, a small distant robotic orbiter spacecraft silhouette in the foreground, thin Martian atmosphere glowing at the limb, cinematic NASA-style space photograph, no text, {GUARD}, {NEG}"),
    (f"{D}-maven-mars-finale", "broll_1.jpg", f"A robotic Mars orbiter spacecraft with large solar panels gliding above the rusty cratered surface of Mars, stars in the black sky behind, detailed realistic space render, no text, {GUARD}, {NEG}"),
    (f"{D}-maven-mars-finale", "broll_2.jpg", f"An artistic visualization of the thin upper atmosphere of Mars being stripped away into space by a stream of golden solar wind particles, the red planet below, cool scientific space illustration, dark starry background, no text, {GUARD}, {NEG}"),
    (f"{D}-maven-mars-finale", "broll_3.jpg", f"A wide desolate rusty-red Martian surface landscape with rolling dunes and distant hills under a pale dusty pink sky, the thin atmosphere on the horizon, lonely cinematic planetary vista, no people, no text, {GUARD}, {NEG}"),
]


def main():
    only = set(sys.argv[1:])
    sel = [(s, f, p) for (s, f, p) in JOBS if not only or f"{s}/{f}" in only or s in only]
    print(f"== Submitting {len(sel)} scene jobs ==", flush=True)
    jobs = []
    for slug, fname, prompt in sel:
        out = IMG_ROOT / slug / fname
        try:
            tid = submit(prompt)
            jobs.append({"slug": slug, "file": fname, "out": out, "tid": tid, "ok": False})
            print(f"  + {slug}/{fname} tid={tid}", flush=True)
        except Exception as e:
            print(f"  ! submit {slug}/{fname}: {e}", file=sys.stderr, flush=True)
        time.sleep(0.5)
    pending = [j for j in jobs if j.get("tid")]
    print(f"\n== Polling {len(pending)} ==", flush=True)
    deadline = time.time() + 20 * 60
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
                    j["done"] = True; continue
                try:
                    info = download(url, j["out"]); j["ok"] = True
                    print(f"  ✓ {j['slug']}/{j['file']} {info}", flush=True)
                except Exception as e:
                    print(f"  ! dl {j['slug']}/{j['file']}: {e}", file=sys.stderr, flush=True)
            elif st == "fail":
                print(f"  ✗ {j['slug']}/{j['file']} FAIL {str(data)[:120]}", file=sys.stderr, flush=True)
            else:
                still.append(j)
        pending = still
        if pending:
            print(f"    ... {len(pending)} generating", flush=True)
    ok = sum(1 for j in jobs if j["ok"])
    print(f"\n== Done {ok}/{len(sel)} ==", flush=True)
    fails = [f"{j['slug']}/{j['file']}" for j in jobs if not j["ok"]]
    if fails:
        for f in fails:
            print(f"  FAIL: {f}", file=sys.stderr)
    return 0 if ok == len(sel) else 1


if __name__ == "__main__":
    sys.exit(main())
