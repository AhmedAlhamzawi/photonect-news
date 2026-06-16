#!/usr/bin/env python3
"""Generate the AI scenes for the 2026-06-16 slate via Nano Banana Pro (9:16, 2K).
One still per beat, each prompt MATCHED to its target beat's text. Strong
no-text/no-UI/no-screenshot/no-logo negatives. NO real-face slots this slate
(none of the six stories is centrally about a single named individual:
Iraq=team, G7=multiple leaders, fungi/Stonehenge/GLP-1=science, Qatar=airline).
Bright/clean lighting to clear engine luminance floors; the underground/space-like
fungal scenes kept luminous, not pitch black."""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

D = "2026-06-16"
GUARD = ("absolutely no text, no captions, no Instagram or app UI, no phone screen interface, no watermark, "
         "no logos, no brand marks, no jersey numbers, no scoreboard numbers, no registration codes, "
         "one single uncropped photograph, single continuous wide shot, one frame only, not a collage, "
         "not a grid, not split panels, photorealistic editorial photograph")

JOBS = [
    # 1. IRAQ WORLD CUP RETURN (sport / national pride; fans, stadium, no logos/numbers/faces)
    (f"{D}-iraq-world-cup-return", "hero.jpg", f"A euphoric packed World Cup football stadium under bright floodlights, a vast sea of fans dressed in red, white and black waving plain unmarked flags, joyful national-pride atmosphere, photorealistic editorial wide shot, no readable text, no logos, no jersey numbers, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-iraq-world-cup-return", "broll_1.jpg", f"A lush green football pitch inside a huge modern World Cup stadium seen from a high wide angle, players in plain unmarked kits standing for kickoff, colorful packed stands, bright clear daylight, photorealistic sports establishing shot, no jersey numbers, no logos, no readable text, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-iraq-world-cup-return", "broll_2.jpg", f"A massive outdoor crowd of football fans celebrating in a Middle Eastern city square at night, waving plain red-white-black flags with fireworks bursting overhead, euphoric jubilant atmosphere, photorealistic editorial wide shot, no readable text, no logos, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-iraq-world-cup-return", "broll_3.jpg", f"A single football resting on the center spot of a floodlit green pitch at dusk inside a grand empty stadium, long dramatic shadows, an atmosphere of anticipation and destiny, photorealistic shot, no logos, no numbers, no readable text, {GUARD}, {NEG}"),
    # 2. FUNGI UNDERGROUND MAP (science / ecology; luminous mycelium, soil, roots)
    (f"{D}-fungi-underground-map", "hero.jpg", f"A breathtaking luminous underground macro view of a vast glowing network of fine white and gold fungal threads weaving through dark rich soil around pale tree roots, soft bioluminescent glow, awe-inspiring intricate scale, photorealistic macro render, vivid highlights, no readable text, no logos, {GUARD}, {NEG}"),
    (f"{D}-fungi-underground-map", "broll_1.jpg", f"An abstract luminous data visualization of a planetary web of golden filament networks spreading across a dark earthy globe, glowing threads connecting continents like underground highways, vivid and clean, photorealistic render, no readable text, no labels, no country borders, no logos, {GUARD}, {NEG}"),
    (f"{D}-fungi-underground-map", "broll_2.jpg", f"A bright clean cross-section of healthy soil beneath a small green plant, delicate glowing pale fungal threads intertwined with the roots exchanging nutrients, warm sunlight from above, vivid and detailed, photorealistic macro render, no readable text, no logos, {GUARD}, {NEG}"),
    (f"{D}-fungi-underground-map", "broll_3.jpg", f"A gloved hand gently cupping dark forest soil laced with fine pale fungal threads, dappled sunlight in a green woodland behind, shallow depth of field, a tender sense of discovery and protection, photorealistic editorial shot, no recognizable faces, no readable text, no logos, {GUARD}, {NEG}"),
    # 3. G7 EVIAN SUMMIT (diplomacy; alpine lake, flags, summit hall, neutral, no faces)
    (f"{D}-g7-evian-summit", "hero.jpg", f"A grand modern summit hall beside a serene alpine lake in France, a large round conference table with neat empty chairs and a row of plain unmarked flags, bright daylight pouring through tall windows, a sense of a major world-leaders gathering, photorealistic wide interior shot, no people, no readable text, no logos, no recognizable flag emblems, {GUARD}, {NEG}"),
    (f"{D}-g7-evian-summit", "broll_1.jpg", f"A row of plain unmarked national flags on tall poles fluttering in front of an elegant lakeside summit venue with alpine mountains behind under a bright clear sky, photorealistic editorial wide shot, no people, no readable text, no emblems, no logos, {GUARD}, {NEG}"),
    (f"{D}-g7-evian-summit", "broll_2.jpg", f"An empty formal diplomatic meeting room with two facing rows of chairs, water carafes and closed folders on a long polished table, soft daylight through large windows, an atmosphere of high-stakes negotiation, photorealistic wide interior shot, no people, no readable text, no logos, {GUARD}, {NEG}"),
    (f"{D}-g7-evian-summit", "broll_3.jpg", f"A wide serene view of an alpine lake and snow-touched mountains at golden dusk with a sleek modern conference building on the shore, a calm hopeful diplomatic atmosphere, photorealistic editorial landscape, no people, no readable text, no logos, {GUARD}, {NEG}"),
    # 4. GLP-1 DIABETES PILL (health; pills, blister pack, clinic, no faces)
    (f"{D}-glp1-diabetes-pill", "hero.jpg", f"A bright clean medical macro close-up of a single small white pill held between fingertips just above a blister pack on a soft-lit clinical surface, a hopeful breakthrough-medicine atmosphere, shallow depth of field, photorealistic shot, no readable text, no logos, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-glp1-diabetes-pill", "broll_1.jpg", f"A neat array of small white oral tablets in a blister pack on a bright clinical white surface beside a small clear medical vial, soft daylight, a clean modern pharmaceutical look, photorealistic macro shot, no readable text, no logos, no faces, {GUARD}, {NEG}"),
    (f"{D}-glp1-diabetes-pill", "broll_2.jpg", f"A bright symbolic health still life contrasting a single small daily pill beside a slim medical injection pen on a clean white surface, soft focus, a sense of an easier simpler treatment, photorealistic editorial shot, no readable text, no logos, no faces, {GUARD}, {NEG}"),
    (f"{D}-glp1-diabetes-pill", "broll_3.jpg", f"A bright modern pharmaceutical research laboratory with clean glassware and a tray of small white tablets under soft clinical light, a sense of active drug development, photorealistic editorial wide shot, no readable text, no logos, no recognizable faces, {GUARD}, {NEG}"),
    # 5. QATAR AIR GLOBAL HUB (aviation / business; planes, terminal, route map, no livery/logos)
    (f"{D}-qatar-air-global-hub", "hero.jpg", f"A sleek modern wide-body passenger jet with a plain unmarked livery climbing into a brilliant clear blue sky just after takeoff, dramatic low upward angle, a sense of global ambition, photorealistic editorial shot, no airline logos, no registration text, no readable text, {GUARD}, {NEG}"),
    (f"{D}-qatar-air-global-hub", "broll_1.jpg", f"A vast gleaming modern Gulf airport terminal interior with soaring glass-and-steel architecture, bright daylight flooding in, distant travelers as motion-blurred silhouettes, a global aviation hub atmosphere, photorealistic wide interior shot, no readable signage, no logos, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-qatar-air-global-hub", "broll_2.jpg", f"A clean bright abstract visualization of glowing flight-path arcs radiating from a single Gulf hub across a dark stylized world map to many continents, luminous and elegant, photorealistic render, no readable text, no country labels, no logos, {GUARD}, {NEG}"),
    (f"{D}-qatar-air-global-hub", "broll_3.jpg", f"A plain unmarked wide-body jet parked at a futuristic Gulf airport gate at golden dusk with a jet bridge connected, warm glowing light, a sense of expanding horizons, photorealistic editorial shot, no airline logos, no readable text, no faces, {GUARD}, {NEG}"),
    # 6. STONEHENGE ALTAR STONE (archaeology / heritage; ancient circle, Scotland, transport)
    (f"{D}-stonehenge-altar-stone", "hero.jpg", f"The ancient Stonehenge stone circle silhouetted against a dramatic golden sunrise on Salisbury Plain, long shadows stretching across dewy grass, a mysterious timeless atmosphere, photorealistic editorial wide shot, no people, no readable text, no logos, {GUARD}, {NEG}"),
    (f"{D}-stonehenge-altar-stone", "broll_1.jpg", f"A massive flat recumbent grey sandstone megalith lying at the heart of an ancient stone circle under soft daylight, weathered lichen-covered surface, a sense of deep prehistoric mystery, photorealistic editorial shot, no people, no readable text, no logos, {GUARD}, {NEG}"),
    (f"{D}-stonehenge-altar-stone", "broll_2.jpg", f"A sweeping dramatic landscape of rugged northeast Scottish highlands with a faint ancient track winding across moorland and distant hills under broody bright light, a sense of an epic prehistoric journey, photorealistic editorial wide shot, no people, no readable text, no logos, {GUARD}, {NEG}"),
    (f"{D}-stonehenge-altar-stone", "broll_3.jpg", f"A conceptual Neolithic scene of a huge sandstone slab on wooden log rollers being hauled by ropes across a green ancient landscape, only distant anonymous silhouetted figures, soft daylight, a sense of monumental human effort, photorealistic editorial shot, no recognizable faces, no readable text, no logos, {GUARD}, {NEG}"),
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
        print(f"  .. {len(pending)} pending", flush=True)
    ok = sum(1 for j in jobs if j.get("ok"))
    print(f"\n== Done: {ok}/{len(jobs)} images ==", flush=True)
    return 0 if ok == len(jobs) else 1


if __name__ == "__main__":
    sys.exit(main())
