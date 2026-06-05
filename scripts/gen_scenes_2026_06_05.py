#!/usr/bin/env python3
"""Generate the 23 non-face AI scenes for 2026-06-05 via Nano Banana Pro (9:16, 2K).
Real face fetched separately: al-Burhan -> sudan broll_2.
Every scene prompt MATCHES its target beat's text. Bright lighting to clear engine
luminance floors. Strong no-text/no-UI negatives (KIE screenshot guard)."""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

D = "2026-06-05"
GUARD = "absolutely no text, no captions, no Instagram or app UI, no phone screen, no watermark, no logos, no brand marks, photorealistic editorial photograph"

JOBS = [
    # 1. IRAQ POWER REVENUE (all 4 generated)
    (f"{D}-iraq-power-revenue", "hero.jpg", f"A sprawling Iraqi city at dusk with a tangle of electrical transmission towers and power lines in the foreground, part of the skyline lit and part in darkness suggesting rolling blackouts, warm hazy sky over Baghdad, wide cinematic establishing shot, no people, {GUARD}, {NEG}"),
    (f"{D}-iraq-power-revenue", "broll_1.jpg", f"A dense Iraqi residential neighborhood in bright daylight with chaotic bundles of overhead electrical wires strung between poles and a cluster of old electricity meters on a wall, documentary realism, wide shot, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-iraq-power-revenue", "broll_2.jpg", f"A large high-voltage electrical substation and power plant in Iraq under bright clear daylight, rows of transformers and tall transmission pylons, vast energy infrastructure, wide cinematic establishing shot, no people, {GUARD}, {NEG}"),
    (f"{D}-iraq-power-revenue", "broll_3.jpg", f"A sweltering Middle Eastern city street at the height of summer under a fierce blazing sun, shimmering heat haze, rows of air-conditioning units on apartment facades, oppressive heat, wide cinematic shot, no recognizable faces, {GUARD}, {NEG}"),
    # 2. SUDAN KORDOFAN (hero/broll_1/broll_3 generated; broll_2 = real al-Burhan)
    (f"{D}-sudan-kordofan-offensive", "hero.jpg", f"A military reconnaissance drone silhouette flying over an arid Sahel landscape at dusk, distant columns of smoke on the horizon, tense conflict atmosphere over Sudan, wide cinematic establishing shot, no people, no faces, {GUARD}, {NEG}"),
    (f"{D}-sudan-kordofan-offensive", "broll_1.jpg", f"Soldiers of a national army in desert camouflage standing by an armored vehicle on a dusty arid frontline with the flag of Sudan (red white black horizontal bands with a green triangle at the hoist) on a pole, harsh daylight, documentary photojournalism, distant figures with no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-sudan-kordofan-offensive", "broll_3.jpg", f"A high aerial wide view of arid semi-desert terrain in the Kordofan region of Sudan, dusty supply roads cutting across scrubland toward the horizon, scattered acacia trees, strategic frontline geography, bright harsh daylight, no people, {GUARD}, {NEG}"),
    # 3. PANCREATIC CANCER DRUG (all 4 generated)
    (f"{D}-pancreatic-cancer-drug", "hero.jpg", f"A bright clean modern oncology research laboratory, a scientist in a white coat and gloves holding a small glass vial of medicine up to soft daylight, hopeful clinical breakthrough mood, shallow depth of field, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-pancreatic-cancer-drug", "broll_1.jpg", f"Extreme macro close-up of a single smooth pharmaceutical capsule pill resting on a clean reflective white surface, soft bright studio lighting, shallow depth of field, sense of a new targeted cancer therapy, no text, {GUARD}, {NEG}"),
    (f"{D}-pancreatic-cancer-drug", "broll_2.jpg", f"A glowing abstract three-dimensional visualization of human cells and a molecular signaling pathway in cool blue and teal tones, scientific medical illustration of a targeted drug blocking a mutated gene, dark background with bright highlights, no text, {GUARD}, {NEG}"),
    (f"{D}-pancreatic-cancer-drug", "broll_3.jpg", f"A large bright modern medical conference auditorium with a stage and a huge blank presentation screen glowing softly, rows of empty seats, prestigious oncology summit atmosphere, wide cinematic shot, blank screen with absolutely no text, {GUARD}, {NEG}"),
    # 4. AI UNIVERSAL VACCINE (all 4 generated)
    (f"{D}-ai-universal-vaccine", "hero.jpg", f"A bright modern biotech laboratory, a single vaccine vial and a syringe on a clean bench with a faint glowing abstract neural-network pattern of light in the background suggesting artificial intelligence, hopeful scientific breakthrough, shallow depth of field, no people, no text, {GUARD}, {NEG}"),
    (f"{D}-ai-universal-vaccine", "broll_1.jpg", f"Extreme macro close-up of a clear glass vaccine vial and a medical syringe on a clean reflective surface, soft bright clinical lighting, droplet of liquid, shallow depth of field, no text, {GUARD}, {NEG}"),
    (f"{D}-ai-universal-vaccine", "broll_2.jpg", f"A bright modern university research laboratory with scientists in white coats working at benches with pipettes and instruments, crisp daylight through large windows, Cambridge-style academic science setting, wide establishing shot, faces not clearly recognizable, {GUARD}, {NEG}"),
    (f"{D}-ai-universal-vaccine", "broll_3.jpg", f"A glowing scientific visualization of a single coronavirus particle with its spike proteins, surrounded by an abstract web of bright artificial-intelligence network lines and nodes, cool blue and white tones on a dark background, no text, {GUARD}, {NEG}"),
    # 5. WORLD CUP 2026 KICKOFF (all 4 generated, generic no-logo)
    (f"{D}-worldcup-2026-kickoff", "hero.jpg", f"A vast packed modern football stadium at night under brilliant white floodlights, a green pitch glowing below tiers of cheering crowds, festive international tournament atmosphere, wide cinematic establishing shot, no recognizable faces, no logos, no banners with text, {GUARD}, {NEG}"),
    (f"{D}-worldcup-2026-kickoff", "broll_1.jpg", f"The grand exterior of a huge iconic football stadium in Mexico City at golden hour, sweeping concrete architecture, crowds streaming toward the entrances, clear warm sky, wide cinematic establishing shot, no logos, no text, {GUARD}, {NEG}"),
    (f"{D}-worldcup-2026-kickoff", "broll_2.jpg", f"A high aerial view of a modern North American city skyline at bright midday with a large sports stadium visible among the towers, clear blue sky, host-city atmosphere, wide cinematic shot, no logos, no text, {GUARD}, {NEG}"),
    (f"{D}-worldcup-2026-kickoff", "broll_3.jpg", f"A gleaming generic golden football trophy cup standing on a dark plinth under a single dramatic spotlight, polished metal reflections, prestige and anticipation, plain dark background, no logos, no brand marks, no text, {GUARD}, {NEG}"),
    # 6. GULF NON-OIL ECONOMY (all 4 generated)
    (f"{D}-gulf-nonoil-economy", "hero.jpg", f"Dubai United Arab Emirates skyline at bright midday, the Burj Khalifa towering above a dense thriving modern financial district, clear blue sky, busy prosperous metropolis, wide aerial establishing shot, no text, {GUARD}, {NEG}"),
    (f"{D}-gulf-nonoil-economy", "broll_1.jpg", f"A bright modern Gulf business district with sleek glass office towers and active construction cranes under clear daylight, a busy diversified non-oil economy, wide cinematic establishing shot, no text, {GUARD}, {NEG}"),
    (f"{D}-gulf-nonoil-economy", "broll_2.jpg", f"Riyadh Saudi Arabia skyline at bright midday, the distinctive Kingdom Centre tower and modern capital skyscrapers, clear sky, growing diversified economy, wide aerial establishing shot, no text, {GUARD}, {NEG}"),
    (f"{D}-gulf-nonoil-economy", "broll_3.jpg", f"A bright airy modern Gulf shopping and tourism district with people walking among palm trees and contemporary architecture, sunlit, vibrant non-oil consumer economy, wide cinematic shot, faces not clearly recognizable, no text, {GUARD}, {NEG}"),
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
