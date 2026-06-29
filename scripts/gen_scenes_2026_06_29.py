#!/usr/bin/env python3
"""Generate AI scenes for the 2026-06-29 slate via Nano Banana Pro 9:16 2K.
One still per beat — no cycling. Two REAL faces are fetched separately into
their slots (Russell -> f1 broll_1, Davies -> worldcup broll_2), so this script
skips those two slots. The Aramco crash scenes are SOBER and respectful — no
wreckage, no victims, no gore; only calm establishing/industrial/official
imagery."""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

D = "2026-06-29"
X = "absolutely no on-screen text, no Arabic or English writing, no captions, no Instagram or app UI, no fake screenshots, no scoreboard graphics, no watermark, no logos, no brand marks, no garbled characters"

JOBS = [
    # 1. IRAQ DROUGHT + EXPOSED TOMBS — cracked riverbed, low reservoir, parched land, excavated tombs
    (f"{D}-iraq-drought-tombs", "hero.jpg", f"A vast cracked dried riverbed of the Tigris in Iraq under a harsh hazy sky, deep fissures in baked cracked earth stretching to the horizon, a thin trickle of water in the middle, distant date palms wilting, climate-crisis mood, wide cinematic establishing aerial shot, {NEG}, {X}"),
    (f"{D}-iraq-drought-tombs", "broll_1.jpg", f"A large reservoir behind a concrete dam in Iraq at a dramatically low water level, wide exposed pale shoreline and stranded cracked mud banks, the water shrunk far from its former line, arid mountains beyond, sober documentary wide shot, {NEG}, {X}"),
    (f"{D}-iraq-drought-tombs", "broll_2.jpg", f"Parched cracked Iraqi farmland with dead dry crops and an empty irrigation canal, a lone farmer figure in the distance looking over the barren field, dust haze and hard sunlight, water-scarcity documentary wide shot, {NEG}, {X}"),
    (f"{D}-iraq-drought-tombs", "broll_3.jpg", f"An archaeological excavation of ancient stone tombs revealed on a dry lakebed near a reservoir in Iraq, rectangular Hellenistic-era stone burial chambers exposed in the cracked earth, low warm light, quiet discovery mood, wide cinematic shot, {NEG}, {X}"),
    # 2. F1 AUSTRIA RUSSELL — (broll_1 = real Russell, fetched), hero car, podium, garage standings
    (f"{D}-f1-austria-russell", "hero.jpg", f"A sleek silver Formula 1 car powering through a sweeping green hillside racetrack corner at high speed, the Austrian Red Bull Ring alpine backdrop, motion blur and dynamic low angle, bright race-day light, no logos or text, wide cinematic sports photography, {NEG}, {X}"),
    (f"{D}-f1-austria-russell", "broll_2.jpg", f"A triumphant Formula 1 driver in a plain racing suit and helmet raising an arm on the top step of a podium, spraying champagne, blurred jubilant crowd and confetti, golden celebratory light, face not identifiable, no logos or text, dynamic cinematic shot, {NEG}, {X}"),
    (f"{D}-f1-austria-russell", "broll_3.jpg", f"A Formula 1 pit garage and grid scene with mechanics in plain overalls around a covered race car, telemetry and tyres, intense focused mood before a championship battle, cool industrial lighting, shallow depth of field, no logos or readable text, {NEG}, {X}"),
    # 3. HORMUZ RECORD FLOW — supertanker, tanker fleet, naval escort near Oman, shipping lane
    (f"{D}-hormuz-record-flow", "hero.jpg", f"A massive crude oil supertanker riding low and heavy crossing the narrow Strait of Hormuz at golden dawn, calm steel-blue Persian Gulf water, hazy rocky coastline of Oman in the distance, strategic and tense, wide cinematic aerial establishing shot, {NEG}, {X}"),
    (f"{D}-hormuz-record-flow", "broll_1.jpg", f"An aerial line of several large oil tankers queued across a calm sea waterway at dawn, immense scale and volume of crude shipping, glassy water reflecting orange sky, sense of record flow, wide cinematic drone shot, {NEG}, {X}"),
    (f"{D}-hormuz-record-flow", "broll_2.jpg", f"A grey naval warship escorting commercial shipping through a narrow strait near a rugged coastline at dusk, wake trailing behind, vigilant maritime-security atmosphere, distant tanker silhouettes, wide cinematic shot, no readable text or insignia, {NEG}, {X}"),
    (f"{D}-hormuz-record-flow", "broll_3.jpg", f"A wide calm aerial of a strategic sea shipping lane at twilight, a single distant tanker on glassy water between two hazy headlands, quiet but tense maritime-chokepoint mood, soft gradient sky, cinematic, {NEG}, {X}"),
    # 4. ASTEROID 1997 NC1 — passing Earth, asteroid in space, close detail, radar dish
    (f"{D}-asteroid-flyby-1997nc1", "hero.jpg", f"A large rocky grey asteroid drifting past planet Earth in deep space, the blue curve of Earth glowing softly in the lower frame against the black star-filled cosmos, awe and scale, no danger, cinematic astrophotography visualization, no labels or text, {NEG}, {X}"),
    (f"{D}-asteroid-flyby-1997nc1", "broll_1.jpg", f"A solitary cratered grey asteroid tumbling through the blackness of space, faint sunlight raking across its rugged pockmarked surface, distant stars, vast emptiness, cinematic space visualization, no labels or text, {NEG}, {X}"),
    (f"{D}-asteroid-flyby-1997nc1", "broll_2.jpg", f"An extreme detailed close visualization of a kilometre-wide rocky near-Earth asteroid surface, sharp craters and boulders, hard low sunlight and deep shadows, the curve of the asteroid against star-filled black space, no labels or text, {NEG}, {X}"),
    (f"{D}-asteroid-flyby-1997nc1", "broll_3.jpg", f"A giant white parabolic deep-space radar dish antenna tilted toward a starry night sky in a desert, the Goldstone-style 34-meter antenna under faint twilight, scientific and majestic, wide cinematic shot, no readable text or logos, {NEG}, {X}"),
    # 5. ARAMCO RAS TANURA — SOBER: oil terminal dawn, emergency response distant, terminal, official setting
    (f"{D}-aramco-rastanura-crash", "hero.jpg", f"A large oil export terminal and jetty on the Saudi east coast at a grey overcast dawn, pipelines storage tanks and loading arms over calm Gulf water, a subdued somber quiet atmosphere, no people, wide cinematic establishing aerial shot, {NEG}, {X}"),
    (f"{D}-aramco-rastanura-crash", "broll_1.jpg", f"Emergency response vehicles with quiet flashing lights gathered at a distance on an industrial coastal access road near oil infrastructure under a pale overcast sky, respectful sober mood, seen from far away, no wreckage, no people visible, wide documentary shot, {NEG}, {X}"),
    (f"{D}-aramco-rastanura-crash", "broll_2.jpg", f"A sprawling crude oil export terminal on the Arabian Gulf coast, rows of storage tanks and pipeline networks along the shoreline, a tanker berthed in the distance, grey calm sea, sober industrial documentary wide aerial shot, {NEG}, {X}"),
    (f"{D}-aramco-rastanura-crash", "broll_3.jpg", f"A quiet formal official setting with a Saudi national flag at half mast on a tall pole against a muted overcast sky, an austere government building facade behind, somber respectful mood of mourning, low angle wide shot, no readable text, {NEG}, {X}"),
    # 6. WORLD CUP CANADA — stadium, (broll_1 = goal celebration), (broll_2 = real Davies, fetched), broll_3 tunnel/next
    (f"{D}-worldcup-canada-r16", "hero.jpg", f"A packed modern World Cup football stadium at night in Los Angeles, brilliant floodlights, a sea of blurred fans with red and white colors, lush green pitch glowing, electric knockout-night atmosphere, wide cinematic establishing shot, no logos or readable text, {NEG}, {X}"),
    (f"{D}-worldcup-canada-r16", "broll_1.jpg", f"A male footballer in a plain red jersey wheeling away in ecstatic celebration after a dramatic last-minute goal, arms outstretched, jubilant blurred teammates rushing in behind under stadium floodlights, face not identifiable, dynamic cinematic sports photography, no logos or text, {NEG}, {X}"),
    (f"{D}-worldcup-canada-r16", "broll_3.jpg", f"A dim stadium players tunnel leading toward a brightly lit pitch, a lone football resting on the grass at the threshold, anticipation of the next knockout match, dramatic backlight, wide cinematic shot, no logos or readable text, {NEG}, {X}"),
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
