#!/usr/bin/env python3
"""«الملف» series batch production — scenes → VO (Fatima) → props → briefs.

Reads data/posts/_almalaf_series.json (QA-final). For each of the 7 episodes:
  1. Generates its 4 Bible-grade scenes via KIE Nano Banana Pro (skip-if-exists)
  2. Ep5: fetches the real al-Zaidi Commons portrait into slot broll_2
  3. Generates Fatima VO + word timestamps
  4. Builds V11 props via scripts/build_v11_props.py
  5. Writes caption.txt
Idempotent — safe to re-run; only missing pieces are produced.
Render happens separately (render_almalaf.sh) so this script stays fast to retry.
"""
from __future__ import annotations
import json, subprocess, sys, time, urllib.parse, urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

ROOT = Path(__file__).resolve().parents[1]
SERIES = json.loads((ROOT / "data/posts/_almalaf_series.json").read_text())
DATE = "2026-07-04"  # series start; all slugs share it, episodes post on later days by schedule
SLOTS = ["hero.jpg", "broll_1.jpg", "broll_2.jpg", "broll_3.jpg"]
UA = "Mozilla/5.0 (PhotonectNews/1.0; ahmed@photonect.net)"


def slug_of(e): return f"{DATE}-{e['slug']}"


def gen_scenes():
    jobs = []
    for e in SERIES["episodes"]:
        slug = slug_of(e)
        for i, prompt in enumerate(e["scenePrompts"]):
            fname = SLOTS[i]
            if e["ep"] == 5 and fname == "broll_2.jpg":
                continue  # real al-Zaidi portrait slot
            out = IMG_ROOT / slug / fname
            if out.exists() and out.stat().st_size > 50_000:
                continue
            out.parent.mkdir(parents=True, exist_ok=True)
            for attempt in range(4):
                try:
                    tid = submit(prompt)
                    jobs.append({"slug": slug, "file": fname, "out": out, "tid": tid, "ok": False})
                    print(f"  + {slug}/{fname} {tid}", flush=True)
                    break
                except Exception as ex:
                    print(f"  ! submit retry {slug}/{fname}: {ex}", file=sys.stderr)
                    time.sleep(4 * (attempt + 1))
            time.sleep(0.7)
    pending = list(jobs)
    deadline = time.time() + 22 * 60
    while pending and time.time() < deadline:
        time.sleep(POLL_INTERVAL)
        nxt = []
        for j in pending:
            try:
                d = (http_get(f"{STATUS_URL}?taskId={j['tid']}").get("data") or {})
            except Exception:
                nxt.append(j); continue
            st = d.get("state")
            if st == "success":
                url = first_image_url(d)
                if url:
                    try:
                        download(url, j["out"]); j["ok"] = True
                        print(f"  ✓ {j['slug']}/{j['file']}", flush=True)
                    except Exception as ex:
                        print(f"  ! dl {j['slug']}/{j['file']}: {ex}", file=sys.stderr); nxt.append(j)
                else:
                    nxt.append(j)
            elif st == "fail":
                print(f"  ✗ FAIL {j['slug']}/{j['file']}", file=sys.stderr)
            else:
                nxt.append(j)
        pending = nxt
        print(f"  ... {len(pending)} pending", flush=True)
    ok = sum(1 for j in jobs if j["ok"])
    print(f"scenes: {ok}/{len(jobs)} generated this run")


def fetch_zaidi():
    e5 = next(e for e in SERIES["episodes"] if e["ep"] == 5)
    dest = IMG_ROOT / slug_of(e5) / "broll_2.jpg"
    if dest.exists() and dest.stat().st_size > 40_000:
        print("zaidi portrait: exists"); return
    dest.parent.mkdir(parents=True, exist_ok=True)
    q = urllib.parse.urlencode({"action": "query", "titles": "Ali Falih al-Zaidi", "prop": "pageimages",
                                "piprop": "thumbnail", "pithumbsize": "1400", "format": "json", "redirects": "1"})
    d = json.loads(urllib.request.urlopen(urllib.request.Request(
        f"https://en.wikipedia.org/w/api.php?{q}", headers={"User-Agent": UA}), timeout=30).read().decode())
    src = next((p.get("thumbnail", {}).get("source") for p in d.get("query", {}).get("pages", {}).values()
                if p.get("thumbnail")), None)
    if not src:
        raise SystemExit("no al-Zaidi Commons portrait found — HOLD ep5")
    subprocess.run(["curl", "-sL", "--retry", "3", "--max-time", "90", "-A", UA, src, "-o", str(dest)], check=True)
    print(f"zaidi portrait: {dest.stat().st_size//1024} KB")


def build_all():
    for e in SERIES["episodes"]:
        slug = slug_of(e)
        img_rel = [f"images/news/{slug}/{s}" for s in SLOTS]
        brief = {
            "slug": slug,
            "kicker": f"الملف {e['ep']}/7",
            "hookHeadline": e["hookHeadline"],
            "voText": e["voText"],
            "endQuestion": e["endQuestion"],
            "sourcesLine": e["sourcesLine"],
            "images": img_rel,
            "audioBed": "audio/mood_cinematic.mp3",
            "statPops": [{"value": p["value"], "label": p["label"], "matchWord": p["matchWord"]}
                         for p in e.get("statPops", [])],
        }
        bpath = ROOT / "data/posts" / slug / ".meta" / "brief.json"
        bpath.parent.mkdir(parents=True, exist_ok=True)
        bpath.write_text(json.dumps(brief, ensure_ascii=False, indent=1))
        r = subprocess.run([sys.executable, str(ROOT / "scripts/build_v11_props.py"), str(bpath)],
                           capture_output=True, text=True)
        print(r.stdout.strip())
        if r.returncode != 0:
            print(f"  ✗ props EP{e['ep']}: {r.stderr.strip()[:300]}", file=sys.stderr)
            continue
        (ROOT / "data/posts" / slug / "caption.txt").write_text(e["caption"] + "\n")
        print(f"  ✓ EP{e['ep']} {slug} ready")


if __name__ == "__main__":
    print("━━━ «الملف» batch production ━━━")
    gen_scenes()
    fetch_zaidi()
    build_all()
    print("✅ production pass complete (renders run separately)")
