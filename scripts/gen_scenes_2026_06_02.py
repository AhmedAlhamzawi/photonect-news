#!/usr/bin/env python3
"""Generate the 21 non-face AI scenes for 2026-06-02 via Nano Banana Pro (9:16, 2K).
Faces (Hakimi->hakimi hero, Hadi->hadi broll_1, Sisi->egypt broll_1) are real photos
fetched separately. Every scene prompt MATCHES its target beat's text. Bright lighting
to clear engine luminance floors. Strong no-text/no-UI negatives (KIE screenshot guard)."""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

D = "2026-06-02"
GUARD = "absolutely no text, no captions, no Instagram or app UI, no phone screen, no watermark, no logos, photorealistic editorial photograph"

JOBS = [
    # 1. IRAQ CABINET DEADLOCK (all 4 generated)
    (f"{D}-iraq-cabinet-deadlock", "hero.jpg", f"Interior of a modern Iraqi parliamentary chamber, curved rows of wooden seats, the flag of Iraq (red white black horizontal bands with green Arabic script) on the front wall, bright daylight through tall windows, formal Arab government assembly hall, wide cinematic establishing shot, {GUARD}, {NEG}"),
    (f"{D}-iraq-cabinet-deadlock", "broll_1.jpg", f"Wide shot of an Iraqi parliament session with many members seated and several conspicuously empty seats in the front rows, formal assembly hall, bright overhead lighting, sense of an incomplete chamber, {GUARD}, {NEG}"),
    (f"{D}-iraq-cabinet-deadlock", "broll_2.jpg", f"Exterior of an official Iraqi government ministry building in Baghdad with the Iraqi flag on a tall pole and a guarded gate, bright clear daylight, sandstone official architecture, wide establishing shot, {GUARD}, {NEG}"),
    (f"{D}-iraq-cabinet-deadlock", "broll_3.jpg", f"An empty formal government press podium with the Iraqi flag beside it in a bright official hall, rows of empty chairs facing it, anticipation of an announcement, wide cinematic shot, {GUARD}, {NEG}"),
    # 2. HAKIMI (hero = real Hakimi face; broll_1/2/3 generated, no player likeness)
    (f"{D}-hakimi-ucl-record", "broll_1.jpg", f"A gleaming silver UEFA-style European club football trophy held aloft amid golden confetti and bright stadium floodlights at night, jubilant celebration atmosphere, no recognizable faces, low heroic angle, {GUARD}, {NEG}"),
    (f"{D}-hakimi-ucl-record", "broll_2.jpg", f"A glowing display cabinet filled with golden football trophies and winners medals under warm spotlights, sense of a decorated career, close cinematic shot, no people, {GUARD}, {NEG}"),
    (f"{D}-hakimi-ucl-record", "broll_3.jpg", f"A football stadium packed with fans waving the red and green flag of Morocco under bright daylight, festive World Cup atmosphere, wide aerial establishing shot, no recognizable faces, {GUARD}, {NEG}"),
    # 3. HADI (broll_1 = real Hadi face; hero/broll_2/broll_3 generated)
    (f"{D}-hadi-yemen-legacy", "hero.jpg", f"The old city of Sana'a Yemen at soft dawn, distinctive ancient tower houses with white gypsum tracery, a large Yemeni flag (red white black bands) on a pole, solemn quiet mood, wide cinematic establishing shot, {GUARD}, {NEG}"),
    (f"{D}-hadi-yemen-legacy", "broll_2.jpg", f"Riyadh Saudi Arabia skyline at golden dusk, the Kingdom Centre tower and modern capital, hazy desert light, wide aerial establishing shot, a place of long exile, {GUARD}, {NEG}"),
    (f"{D}-hadi-yemen-legacy", "broll_3.jpg", f"A single Yemeni national flag flying at half-mast against a muted grey overcast sky, solemn mourning atmosphere, low angle, sense of the end of an era, {GUARD}, {NEG}"),
    # 4. TIANWEN-2 ASTEROID (all 4 generated)
    (f"{D}-tianwen2-asteroid", "hero.jpg", f"A Chinese robotic space probe with large solar panels approaching a small irregular grey near-Earth asteroid in deep space, distant blue Earth and bright Sun in the background, cinematic photoreal space scene, {GUARD}, {NEG}"),
    (f"{D}-tianwen2-asteroid", "broll_1.jpg", f"A spacecraft probe orbiting close to a small rocky grey asteroid against the black starfield, gold foil and solar panels catching sunlight, sense of arrival after a long journey, photoreal, {GUARD}, {NEG}"),
    (f"{D}-tianwen2-asteroid", "broll_2.jpg", f"Extreme close-up of the dusty cratered grey surface of a small asteroid with a robotic sampling arm reaching down to collect material, sunlit, deep space, photoreal, {GUARD}, {NEG}"),
    (f"{D}-tianwen2-asteroid", "broll_3.jpg", f"A small space return capsule descending under a parachute toward the green grasslands of Inner Mongolia at dawn, recovery scene, wide cinematic daylight shot, {GUARD}, {NEG}"),
    # 5. EGYPT IMF + SAUDI (broll_1 = real Sisi face; hero/broll_2/broll_3 generated)
    (f"{D}-egypt-imf-saudi", "hero.jpg", f"Cairo Egypt skyline along the Nile river at bright midday, modern towers of the new financial district and the river with feluccas, wide aerial establishing shot, {GUARD}, {NEG}"),
    (f"{D}-egypt-imf-saudi", "broll_2.jpg", f"The national flag of Egypt and the national flag of Saudi Arabia flying side by side on two tall flagpoles against a bright clear blue sky, sense of partnership, low heroic angle, {GUARD}, {NEG}"),
    (f"{D}-egypt-imf-saudi", "broll_3.jpg", f"A bright modern financial trading floor in Cairo with large wall screens showing currency exchange rates and line charts, blurred staff in the foreground, daylight, {GUARD}, {NEG}"),
    # 6. LILLY OBESITY DRUG (all 4 generated)
    (f"{D}-lilly-obesity-drug", "hero.jpg", f"A bright clean modern pharmaceutical research laboratory, scientists in white coats working at benches with vials and instruments, crisp daylight, high-tech medical research facility, wide establishing shot, {GUARD}, {NEG}"),
    (f"{D}-lilly-obesity-drug", "broll_1.jpg", f"Extreme close-up of a sleek white medical injection pen and a small glass vial on a clean reflective surface, soft bright studio lighting, shallow depth of field, modern medicine, {GUARD}, {NEG}"),
    (f"{D}-lilly-obesity-drug", "broll_2.jpg", f"A bright modern doctor office where a physician in a white coat speaks with a patient beside a medical weighing scale, optimistic clean clinical setting, daylight, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-lilly-obesity-drug", "broll_3.jpg", f"An automated pharmaceutical production line with rows of small medicine vials moving along a bright stainless-steel conveyor, clean factory, crisp lighting, wide shot, {GUARD}, {NEG}"),
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
    deadline = time.time() + 18 * 60
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
