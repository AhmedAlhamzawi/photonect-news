#!/usr/bin/env python3
"""Generate the 19 non-face AI scenes for 2026-05-29 via Nano Banana Pro.
Faces (Musk/Messi/Ronaldo/Hakimi/al-Sharaa) are real photos, fetched separately.
Reuses gen_2026_05_28 infrastructure.
"""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

D = "2026-05-29"
# (slug, filename, prompt)
JOBS = [
    # IRAQ ELECTRICITY
    (f"{D}-iraq-electricity-collapse", "hero.jpg", f"An Iraqi family sitting in a dim apartment during a summer power blackout, lit only by a battery lantern and phone screens, sweltering Baghdad night, intimate documentary, {NEG}"),
    (f"{D}-iraq-electricity-collapse", "broll_1.jpg", f"A high-voltage electrical substation and transmission towers at dusk in Iraq, dark and dormant, heat haze, ominous wide cinematic shot, {NEG}"),
    (f"{D}-iraq-electricity-collapse", "broll_2.jpg", f"Young men protesting at night on a Baghdad street, burning tires and black smoke blocking the road, silhouettes against fire, tense documentary, {NEG}"),
    (f"{D}-iraq-electricity-collapse", "broll_3.jpg", f"Baghdad city skyline at night mostly blacked out, only scattered lights, the Tigris river dark, summer heat haze, somber aerial wide shot, {NEG}"),
    # MUSK (hero is real Musk photo)
    (f"{D}-musk-spacex-ipo", "broll_1.jpg", f"A SpaceX Starship rocket launching at dawn, massive plume of fire and smoke, brilliant exhaust, dramatic low angle, ultra-realistic, {NEG}"),
    (f"{D}-musk-spacex-ipo", "broll_2.jpg", f"The Nasdaq stock exchange tower in Times Square glowing with green financial tickers at dusk, IPO energy, ultra-realistic editorial, {NEG}"),
    (f"{D}-musk-spacex-ipo", "broll_3.jpg", f"A sleek SpaceX Starship spacecraft in orbit above Earth heading toward Mars, stars, cinematic space photography, {NEG}"),
    # WORLD CUP (hero=Messi, broll_1=Ronaldo, broll_3=Hakimi are real)
    (f"{D}-worldcup-messi-ronaldo", "broll_2.jpg", f"The golden FIFA World Cup trophy on a pedestal in a packed floodlit stadium at night, confetti, electric crowd, ultra-realistic sports photography, {NEG}"),
    # LEBANON (broll_2=al-Sharaa is real)
    (f"{D}-lebanon-ceasefire-brink", "hero.jpg", f"Beirut Lebanon skyline at dusk along the Mediterranean, modern towers beside war-scarred buildings, tense calm, hazy golden light, wide aerial cinematic, {NEG}"),
    (f"{D}-lebanon-ceasefire-brink", "broll_1.jpg", f"Lebanese army soldiers in green camouflage at a checkpoint in southern Lebanon near the border, armored vehicle, alert posture, overcast, documentary, {NEG}"),
    (f"{D}-lebanon-ceasefire-brink", "broll_3.jpg", f"A partially collapsed residential building in southern Lebanon, rubble and twisted rebar, grey overcast sky, somber documentary, {NEG}"),
    # SPACE / FUSION
    (f"{D}-space-iss-fusion", "hero.jpg", f"The International Space Station orbiting above the bright blue curve of Earth, solar panels gleaming in sunlight, black space, ultra-realistic NASA-style photography, {NEG}"),
    (f"{D}-space-iss-fusion", "broll_1.jpg", f"A SpaceX Crew Dragon capsule descending under red-and-white parachutes toward a dawn ocean splashdown, ultra-realistic, {NEG}"),
    (f"{D}-space-iss-fusion", "broll_2.jpg", f"Glowing pink-orange fusion plasma inside a futuristic tokamak reactor core, intricate magnetic coils, intense energy, ultra-realistic science photography, {NEG}"),
    (f"{D}-space-iss-fusion", "broll_3.jpg", f"The planet Mars in deep space, rusty red surface detail, stars, a distant spacecraft silhouette approaching, cinematic, {NEG}"),
    # SUDAN — dignified humanitarian
    (f"{D}-sudan-famine-year4", "hero.jpg", f"A long line of Sudanese refugee families carrying belongings walking across an arid Darfur landscape at dusk toward a camp, dignified documentary, wide shot, {NEG}"),
    (f"{D}-sudan-famine-year4", "broll_1.jpg", f"Rows of white UN tents in a vast Sudanese displacement camp on cracked dry earth, harsh sunlight, aerial wide shot, ultra-realistic, {NEG}"),
    (f"{D}-sudan-famine-year4", "broll_2.jpg", f"Humanitarian aid workers distributing sacks of grain from a white truck to a crowd in Sudan, dust and heat, documentary photojournalism, {NEG}"),
    (f"{D}-sudan-famine-year4", "broll_3.jpg", f"A Sudanese mother holding her child at a clinic tent, worried but dignified, soft natural light, respectful documentary portrait, {NEG}"),
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
    print(f"\n== Done {ok}/{len(JOBS)} ==", flush=True)
    fails = [f"{j['slug']}/{j['file']}" for j in jobs if not j["ok"]]
    if fails:
        for f in fails:
            print(f"  FAIL: {f}", file=sys.stderr)
    return 0 if ok == len(JOBS) else 1


if __name__ == "__main__":
    sys.exit(main())
