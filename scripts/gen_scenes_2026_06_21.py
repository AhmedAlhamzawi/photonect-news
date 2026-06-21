#!/usr/bin/env python3
"""Generate the 22 non-face AI scenes for the 2026-06-21 slate via Nano Banana Pro 9:16 2K.
Golf faces (Wyndham Clark, Scottie Scheffler) are real Commons photos, fetched separately.
Reuses gen_2026_05_28 infrastructure. One still per beat — no cycling.
"""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

D = "2026-06-21"
# stronger anti-fake-UI / anti-text guard appended to every prompt
X = "absolutely no on-screen text, no Arabic or English writing, no captions, no Instagram or app UI, no fake screenshots, no watermark, no logos, no garbled characters"

JOBS = [
    # 1. IRAQ WATER CRISIS — dusty ochre, bright daylight
    (f"{D}-iraq-water-crisis", "hero.jpg", f"A cracked sun-baked Mesopotamian riverbed in southern Iraq, a stranded wooden fishing boat tilted on dried mud, only a thin trickle of water remaining, harsh midday desert sun, dusty ochre and amber palette, wide cinematic establishing shot, {NEG}, {X}"),
    (f"{D}-iraq-water-crisis", "broll_1.jpg", f"Aerial view of a shrunken reservoir behind a concrete dam in Iraq, a wide pale bathtub-ring of exposed rock around a low blue-green water body, arid hills, bright daylight, ultra-realistic, {NEG}, {X}"),
    (f"{D}-iraq-water-crisis", "broll_2.jpg", f"A southern Iraqi farmer in a traditional white dishdasha standing in a dead salt-crusted cracked field, withered brown crops, bright harsh sunlight, documentary photojournalism, {NEG}, {X}"),
    (f"{D}-iraq-water-crisis", "broll_3.jpg", f"A large concrete dam spillway releasing a strong jet of turquoise water into a river, arid mountains behind, bright daylight, wide aerial cinematic shot, {NEG}, {X}"),
    # 2. SYRIA SWEIDA — full-bleed, no UI
    (f"{D}-syria-sweida-autonomy", "hero.jpg", f"Armed Druze fighters standing on a rocky hilltop overlooking the city of Sweida in southern Syria at golden hour, a large multicolored Druze five-stripe star flag (green red yellow blue white) raised on a pole, wide cinematic landscape, {NEG}, {X}"),
    (f"{D}-syria-sweida-autonomy", "broll_1.jpg", f"A daytime protest in a dusty southern Syrian town square, a crowd of Druze men holding blank cloth banners and the multicolored Druze flag, low-rise Levantine buildings, documentary photojournalism, {NEG}, {X}"),
    (f"{D}-syria-sweida-autonomy", "broll_2.jpg", f"A damaged government ministry building facade in Damascus, broken windows and dark scorch marks, grey overcast daylight, somber documentary, {NEG}, {X}"),
    (f"{D}-syria-sweida-autonomy", "broll_3.jpg", f"A quiet ceasefire checkpoint on a southern Syria road at dusk, stacked sandbags and a concrete barrier, a single white SUV parked, empty and tense, documentary, {NEG}, {X}"),
    # 3. GULF WEALTH FUNDS — bright, kinetic data
    (f"{D}-gulf-wealth-funds", "hero.jpg", f"A gleaming Gulf financial skyline of modern glass skyscrapers at golden dusk, abstract glowing golden upward arrows and luminous light-streaks rising between the towers suggesting capital flow, ultra-modern, bright, cinematic, {NEG}, {X}"),
    (f"{D}-gulf-wealth-funds", "broll_1.jpg", f"An abstract deep-blue globe of the Earth with glowing bright golden arcs of light flowing from the Arabian Gulf toward North America and Europe, luminous data-visualization style, no labels, {NEG}, {X}"),
    (f"{D}-gulf-wealth-funds", "broll_2.jpg", f"A modern financial trading floor with large glowing screens showing rising green line charts, blurred professionals in suits in the foreground, bright cool blue lighting, ultra-realistic, {NEG}, {X}"),
    (f"{D}-gulf-wealth-funds", "broll_3.jpg", f"A split composition, on the left a lone oil pumpjack in the desert at dusk, on the right a cluster of gleaming modern glass tech and tourism towers in bright daylight, symbolizing a shift from oil to non-oil economy, cinematic, {NEG}, {X}"),
    # 4. US OPEN GOLF — hero + trophy only (faces fetched separately)
    (f"{D}-us-open-golf", "hero.jpg", f"A lone golfer silhouette mid-swing against windswept seaside links sand dunes at golden hour, dramatic cloudy sky, coastal championship golf course, no identifiable face, ultra-realistic sports photography, {NEG}, {X}"),
    (f"{D}-us-open-golf", "broll_3.jpg", f"A gleaming silver golf championship trophy on a pedestal on a manicured putting green at sunset, soft bokeh of a crowd behind, ultra-realistic, no logos, {NEG}, {X}"),
    # 5. TIANWEN-2 ASTEROID — well-lit against black space
    (f"{D}-tianwen2-asteroid", "hero.jpg", f"A sleek spacecraft probe with golden solar panels hovering beside a small dark-grey rocky asteroid in deep space, bright Sun rim-lighting the probe and asteroid edge, a small blue crescent of Earth far in the distance, stars, ultra-realistic NASA-style space photography, {NEG}, {X}"),
    (f"{D}-tianwen2-asteroid", "broll_1.jpg", f"Extreme close-up of a cratered dark-grey weathered asteroid surface, strong directional sunlight raking across creating sharp shadows, fine regolith dust, ultra-realistic space photography, {NEG}, {X}"),
    (f"{D}-tianwen2-asteroid", "broll_2.jpg", f"A spacecraft sampling arm with a collection horn touching the sunlit surface of a grey asteroid, a small plume of grey dust rising, black space behind, ultra-realistic, {NEG}, {X}"),
    (f"{D}-tianwen2-asteroid", "broll_3.jpg", f"A glowing re-entry capsule streaking across a dawn sky above the green grasslands of Inner Mongolia, bright fiery orange trail, ultra-realistic, {NEG}, {X}"),
    # 6. GLP-1 ORAL PILL — bright clinical
    (f"{D}-glp1-oral-pill", "hero.jpg", f"A single small white oval pill held between two fingers in clean bright clinical light, soft shallow focus, a faint downward weight-loss curve glowing softly in the blurred background, ultra-realistic, {NEG}, {X}"),
    (f"{D}-glp1-oral-pill", "broll_1.jpg", f"A medical injection pen lying crossed-out beside a white pill bottle on a clean white clinical surface, symbolizing a needle-free shift, bright even lighting, no readable labels, ultra-realistic, {NEG}, {X}"),
    (f"{D}-glp1-oral-pill", "broll_2.jpg", f"A clean minimalist medical line graph showing a single steep downward curve, soft blue and white, bright, abstract data-visualization, no numbers, no text, {NEG}, {X}"),
    (f"{D}-glp1-oral-pill", "broll_3.jpg", f"A modern pharmacy shelf in a Gulf clinic with neat rows of plain white medicine boxes, an Arab pharmacist in a white coat reaching for one, bright clean lighting, no readable text on packages, ultra-realistic, {NEG}, {X}"),
]


def main():
    jobs = []
    print(f"== Submitting {len(JOBS)} scene jobs ==", flush=True)
    for slug, fname, prompt in JOBS:
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
                    print(f"  ! dl {j['slug']}/{j['file']}: {e}", file=sys.stderr, flush=True)
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
            print(f"  MISSING: {j['slug']}/{j['file']}", flush=True)
    return 0 if ok == len(JOBS) else 1


if __name__ == "__main__":
    sys.exit(main())
