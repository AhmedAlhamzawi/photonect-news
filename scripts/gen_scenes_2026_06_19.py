#!/usr/bin/env python3
"""Generate the AI scenes for the 2026-06-19 slate via Nano Banana Pro (9:16, 2K).
One still per beat, each prompt MATCHED to its target beat's text. Strong
no-text/no-UI/no-screenshot/no-logo negatives. No real-face slot this slate —
no story is centrally about a single named individual, so all 24 are scenes."""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

D = "2026-06-19"
GUARD = ("absolutely no text, no captions, no Instagram or app UI, no phone screen interface, no watermark, "
         "no logos, no brand marks, no jersey numbers, no readable signage, no labels, no numbers, "
         "no recognizable real people or celebrities, one single uncropped photograph, single continuous wide shot, "
         "one frame only, not a collage, not a grid, not split panels, photorealistic editorial photograph")

JOBS = [
    # 1. IRAQ BUDGET BYPASS (iraq_domestic, A) — parliament stalemate, cash crisis, customs pivot
    (f"{D}-iraq-budget-bypass", "hero.jpg", f"Interior of a modern Iraqi parliamentary chamber with curved rows of empty seats and the flag of Iraq (red, white and black horizontal bands with green Arabic script) on the front wall, a tense empty assembly hall under dramatic overhead lighting, a sense of political stalemate, photorealistic editorial wide shot, no people, {GUARD}, {NEG}"),
    (f"{D}-iraq-budget-bypass", "broll_1.jpg", f"A formal empty Middle Eastern parliamentary committee room with a long polished table, closed leather folders and microphones, the flag of Iraq on a pole, soft window light, a solemn stalled-negotiation mood, photorealistic editorial shot, no people, no readable documents, {GUARD}, {NEG}"),
    (f"{D}-iraq-budget-bypass", "broll_2.jpg", f"Close-up of thick stacks of bundled Iraqi dinar banknotes on a dark surface under cool light, a sense of a cash-liquidity crunch and money printing, shallow depth of field, photorealistic editorial macro, no readable serial numbers, {GUARD}, {NEG}"),
    (f"{D}-iraq-budget-bypass", "broll_3.jpg", f"A busy modern customs border crossing with rows of cargo trucks and stacked shipping containers under bright daylight, a sense of trade and non-oil customs revenue, photorealistic editorial wide shot, no people, no readable signage, {GUARD}, {NEG}"),
    # 2. WORLD CUP GOAL DELUGE (wildcard/sport, B) — net bulging, packed stadium, celebration
    (f"{D}-worldcup-goal-deluge", "hero.jpg", f"A soccer ball resting in the back of a goal net with the white mesh gently rippling, inside a vast floodlit packed stadium at night, a sense of a goal just scored, photorealistic editorial sports wide shot, generic unmarked ball, no people, {GUARD}, {NEG}"),
    (f"{D}-worldcup-goal-deluge", "broll_1.jpg", f"Close-up of a plain soccer ball nestled in the white netting of a goal, the mesh softly stretched, bright stadium floodlights glowing behind, photorealistic editorial sports shot, generic unmarked ball, no people, {GUARD}, {NEG}"),
    (f"{D}-worldcup-goal-deluge", "broll_2.jpg", f"A vast packed football stadium at night filled with a roaring crowd and bright floodlights, a sea of fans, an electric record-breaking atmosphere, photorealistic editorial wide shot, no readable banners, no logos, {GUARD}, {NEG}"),
    (f"{D}-worldcup-goal-deluge", "broll_3.jpg", f"A packed football stadium at night erupting with golden confetti and bright floodlights, a jubilant celebratory atmosphere after a goal, empty green pitch in the foreground, photorealistic editorial wide shot, no people in foreground, no logos, no readable text, {GUARD}, {NEG}"),
    # 3. SAUDI TOURISM 2030 (gulf_regional, C) — AlUla heritage, Red Sea luxury, NEOM future
    (f"{D}-saudi-tourism-2030", "hero.jpg", f"The majestic ancient Nabataean rock-carved tombs of Hegra near AlUla in Saudi Arabia glowing warm gold at sunset amid dramatic desert sandstone formations, awe-inspiring heritage tourism, photorealistic editorial wide shot, no people, {GUARD}, {NEG}"),
    (f"{D}-saudi-tourism-2030", "broll_1.jpg", f"A sweeping desert landscape of AlUla Saudi Arabia with towering eroded sandstone cliffs and a winding oasis of green palms at golden hour, a sense of a thriving tourism destination, photorealistic editorial wide shot, no readable signage, {GUARD}, {NEG}"),
    (f"{D}-saudi-tourism-2030", "broll_2.jpg", f"A luxurious modern Red Sea resort in Saudi Arabia with sleek architecture, turquoise water and overwater villas at golden hour, palm trees, a premium-tourism atmosphere, photorealistic editorial wide shot, no people, no logos, {GUARD}, {NEG}"),
    (f"{D}-saudi-tourism-2030", "broll_3.jpg", f"A futuristic ultramodern desert megaproject in Saudi Arabia with vast sleek mirrored architecture rising from golden sand under a clear sky, a visionary giga-project atmosphere, photorealistic editorial wide shot, no readable signage, no logos, {GUARD}, {NEG}"),
    # 4. PRESERVATIVES & HEART (wildcard/health, B) — processed food, study, blood pressure
    (f"{D}-preservatives-heart", "hero.jpg", f"Long bright supermarket shelves densely packed with colorful canned and packaged processed foods, clean clinical editorial lighting, a sense of everyday packaged food and additives, photorealistic editorial wide shot, no readable text on packaging, no logos, {GUARD}, {NEG}"),
    (f"{D}-preservatives-heart", "broll_1.jpg", f"A clean modern nutrition research laboratory with gloved hands examining packaged food samples and a microscope, cool scientific lighting, an epidemiology-study mood, photorealistic editorial shot, no recognizable faces, no readable text, {GUARD}, {NEG}"),
    (f"{D}-preservatives-heart", "broll_2.jpg", f"A close-up of a blood-pressure monitor cuff wrapped on an arm with a softly glowing abstract heart-health visualization nearby, cool clinical tones, a cardiovascular-risk mood, photorealistic editorial shot, face not visible, no readable numbers, {GUARD}, {NEG}"),
    (f"{D}-preservatives-heart", "broll_3.jpg", f"An overhead close-up of assorted processed deli meats and canned preserved foods arranged on a dark surface, glossy and tightly packed, an editorial food-science mood, photorealistic editorial macro, no readable labels, no logos, {GUARD}, {NEG}"),
    # 5. STARGATE UAE AI (tech_ai, B) — desert hyperscale datacenter, GPU hardware, network
    (f"{D}-stargate-uae-ai", "hero.jpg", f"A vast hyperscale AI data center hall with endless symmetrical rows of tall black server racks glowing with cool blue and cyan indicator lights, polished reflective floor, dramatic vanishing-point perspective, immense scale in a Gulf desert facility, photorealistic editorial wide shot, {GUARD}, {NEG}"),
    (f"{D}-stargate-uae-ai", "broll_1.jpg", f"Extreme close-up of cutting-edge AI GPU server hardware, dense green circuit boards and gold connectors, thick bundles of orange and blue fiber-optic cables, rows of glowing status LEDs, shallow depth of field, photorealistic editorial macro, no readable text, {GUARD}, {NEG}"),
    (f"{D}-stargate-uae-ai", "broll_2.jpg", f"A sweeping aerial view of an enormous modern data-center campus of long white buildings in a flat desert near a distant Gulf city skyline at golden hour, immense scale, photorealistic editorial wide shot, no readable signage, no logos, {GUARD}, {NEG}"),
    (f"{D}-stargate-uae-ai", "broll_3.jpg", f"A glowing abstract digital globe with luminous data arcs over a softly lit modern Gulf city skyline at dusk, cool blue and teal tones, a sense of a global AI hub, photorealistic 3D render, no readable text, {GUARD}, {NEG}"),
    # 6. AMAZON FUNGUS SPIDER (wildcard/nature, C) — Cordyceps-mimic spider, rainforest macro
    (f"{D}-amazon-fungus-spider", "hero.jpg", f"A dramatic extreme macro of an exotic orb-weaver spider whose pale knobbly abdomen mimics the white fruiting body of a parasitic fungus, perched on a mossy twig in a dark rainforest, shallow depth of field, eerie natural camouflage, photorealistic wildlife macro photograph, {GUARD}, {NEG}"),
    (f"{D}-amazon-fungus-spider", "broll_1.jpg", f"A macro close-up of a small pale fungus-mimicking spider resting on a green rainforest leaf, its body resembling a whitish fungal growth, soft diffused daylight, lush Ecuadorian Amazon foliage behind, photorealistic wildlife macro, {GUARD}, {NEG}"),
    (f"{D}-amazon-fungus-spider", "broll_2.jpg", f"A night macro in a dense rainforest of a pale spider that looks exactly like a white fungal fruiting body on a wet branch, lit by a soft headlamp glow, dewy leaves, mysterious mood, photorealistic wildlife macro, {GUARD}, {NEG}"),
    (f"{D}-amazon-fungus-spider", "broll_3.jpg", f"A lush misty Ecuadorian Amazon cloud-forest landscape with dense green canopy, drifting fog and shafts of soft light, a pristine biodiversity hotspot, photorealistic editorial nature wide shot, no people, {GUARD}, {NEG}"),
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
        print(f"  .. {len(pending)} pending", flush=True)
    ok = sum(1 for j in jobs if j.get("ok"))
    print(f"\n== Done: {ok}/{len(jobs)} images ==", flush=True)
    return 0 if ok == len(jobs) else 1


if __name__ == "__main__":
    sys.exit(main())
