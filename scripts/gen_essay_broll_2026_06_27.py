#!/usr/bin/env python3
"""Generate 7 Veo b-roll clips (one per beat) for the Development Road essay.

Reads data/essay-faw-road/script.json, submits each segment's broll_prompt to
KIE Veo 3.1 fast (9:16, 8s), polls, and downloads via curl (robust on big files
— the smoke-test's urllib download truncated a 21MB clip). Verifies the moov
atom with ffprobe and retries the download if invalid.
"""
from __future__ import annotations
import json, os, re, subprocess, sys, time, urllib.request
from pathlib import Path

KIE = "https://api.kie.ai"
GEN = f"{KIE}/api/v1/veo/generate"
INFO = f"{KIE}/api/v1/veo/record-info"
CALLBACK = "https://webhook.site/00000000-0000-0000-0000-000000000000"
POLL, MAX_MIN = 15, 14
ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "data" / "essay-faw-road" / "script.json"
OUT = ROOT / "data" / "essay-faw-road" / "broll"


def load_key():
    for envf in (ROOT/".env", ROOT/".env.local"):
        if envf.is_file():
            for line in envf.read_text().splitlines():
                m = re.match(r"\s*(?:export\s+)?KIE_AI_API_KEY\s*=\s*(.+)\s*$", line)
                if m: return m.group(1).strip().strip('"').strip("'")
    return os.environ.get("KIE_AI_API_KEY")


def post(url, body, key):
    req = urllib.request.Request(url, data=json.dumps(body).encode(), method="POST",
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json", "Accept": "application/json"})
    return json.loads(urllib.request.urlopen(req, timeout=30).read().decode())


def get(url, key):
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {key}", "Accept": "application/json"})
    return json.loads(urllib.request.urlopen(req, timeout=30).read().decode())


def result_url(data):
    resp = data.get("response") or {}
    for k in ("resultUrls", "videoUrls"):
        v = resp.get(k) or data.get(k)
        if v: return (v if isinstance(v, list) else [v])[0]
    return None


def valid_mp4(p: Path) -> bool:
    if not p.is_file() or p.stat().st_size < 200_000:
        return False
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", str(p)], capture_output=True, text=True)
    return r.returncode == 0 and r.stdout.strip() not in ("", "N/A")


def curl_download(url: str, dest: Path, tries=4) -> bool:
    dest.parent.mkdir(parents=True, exist_ok=True)
    for t in range(1, tries + 1):
        subprocess.run(["curl", "-sL", "--retry", "3", "--max-time", "300",
                        "-A", "Mozilla/5.0", url, "-o", str(dest)], check=False)
        if valid_mp4(dest):
            return True
        print(f"      download attempt {t} invalid, retrying...", flush=True)
        time.sleep(3)
    return False


def submit(prompt, key) -> str:
    body = {"prompt": prompt, "model": "veo3_fast", "generationType": "TEXT_2_VIDEO",
            "aspect_ratio": "9:16", "resolution": "1080p", "duration": 8, "callBackUrl": CALLBACK}
    resp = post(GEN, body, key)
    if resp.get("code") != 200:
        raise RuntimeError(f"submit failed: {resp}")
    return (resp.get("data") or {}).get("taskId")


def main():
    key = load_key()
    if not key: sys.exit("no KIE key")
    segs = json.loads(SCRIPT.read_text())["segments"]
    OUT.mkdir(parents=True, exist_ok=True)
    print(f"━━━ Essay b-roll — {len(segs)} Veo clips ━━━")

    # Submit all first (they generate in parallel server-side)
    tasks = []
    for i, s in enumerate(segs, 1):
        dest = OUT / f"clip_{i}_{s['beat_role']}.mp4"
        if valid_mp4(dest):
            print(f"  [{i}] {s['beat_role']} — exists, skip"); tasks.append((i, s, None, dest)); continue
        try:
            tid = submit(s["broll_prompt"], key)
            print(f"  [{i}] {s['beat_role']} → {tid}")
            tasks.append((i, s, tid, dest))
        except Exception as e:
            print(f"  [{i}] SUBMIT FAIL: {e}"); tasks.append((i, s, None, dest))
        time.sleep(2)

    manifest = []
    for i, s, tid, dest in tasks:
        if tid is None:
            manifest.append({"beat": i, "role": s["beat_role"], "file": dest.name if valid_mp4(dest) else None})
            continue
        print(f"\n  polling [{i}] {s['beat_role']} ({tid[:8]})")
        deadline = time.time() + MAX_MIN * 60
        url = None
        while time.time() < deadline:
            try:
                d = (get(f"{INFO}?taskId={tid}", key).get("data") or {})
            except Exception as e:
                print(f"      poll err: {e}"); time.sleep(POLL); continue
            url = result_url(d)
            if url: break
            if str(d.get("errorCode") or "") not in ("", "None", "0") or d.get("errorMessage"):
                print(f"      FAILED: {d.get('errorMessage')}"); break
            time.sleep(POLL)
        if url and curl_download(url, dest, ):
            print(f"      ✓ saved {dest.name}")
            manifest.append({"beat": i, "role": s["beat_role"], "file": dest.name, "url": url})
        else:
            print(f"      ✗ no valid clip for beat {i}")
            manifest.append({"beat": i, "role": s["beat_role"], "file": None})

    (OUT / "_manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False))
    ok = len([m for m in manifest if m.get("file")])
    print(f"\n✅ b-roll: {ok}/{len(segs)} clips → {OUT}")


if __name__ == "__main__":
    sys.exit(main())
