#!/usr/bin/env python3
"""KIE Veo 3.1 smoke test — does our existing KIE key generate usable cinematic
9:16 b-roll, and does it hallucinate on-screen text? One clip, ~$cheap.

Endpoint (docs.kie.ai/veo3-api): POST /api/v1/veo/generate
  body {prompt, model:veo3_fast, generationType:TEXT_2_VIDEO, aspect_ratio:9:16,
        resolution:1080p, duration:8, callBackUrl}
  → {code:200, data:{taskId}}
Poll: GET /api/v1/veo/record-info?taskId=  (result URL parsed defensively).
No negative-prompt field exists → anti-text instructions baked into the prompt.
No `watermark` field sent → clean, watermark-free (a key upgrade over the original).
"""
from __future__ import annotations
import json, os, re, sys, time, urllib.request, urllib.error
from pathlib import Path

KIE = "https://api.kie.ai"
GEN = f"{KIE}/api/v1/veo/generate"
INFO_CANDIDATES = [f"{KIE}/api/v1/veo/record-info", f"{KIE}/api/v1/veo/recordInfo"]
CALLBACK = "https://webhook.site/00000000-0000-0000-0000-000000000000"
POLL, MAX_MIN = 15, 12
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "essay-video-test"

PROMPT = (
    "Cinematic slow aerial push-in over a dense modern Middle Eastern financial "
    "district at dusk, glass skyscrapers with glowing windows, highways with car "
    "light trails, dramatic clouds, volumetric golden light, photorealistic, "
    "filmic color grade, subtle film grain, shallow depth of field. "
    "Absolutely no text, no signage, no billboards, no shop names, no logos, "
    "no captions, no subtitles, no watermark, no UI, no on-screen graphics. "
    "Clean cinematic frame, vertical 9:16."
)


def load_key() -> str:
    k = os.environ.get("KIE_AI_API_KEY")
    if k:
        return k.strip()
    for envf in (ROOT / ".env", ROOT / ".env.local"):
        if envf.is_file():
            for line in envf.read_text().splitlines():
                m = re.match(r"\s*(?:export\s+)?KIE_AI_API_KEY\s*=\s*(.+)\s*$", line)
                if m:
                    return m.group(1).strip().strip('"').strip("'")
    sys.exit("error: KIE_AI_API_KEY not found")


def post(url, body, key, timeout=30):
    req = urllib.request.Request(url, data=json.dumps(body).encode(), method="POST",
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json", "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode())


def get(url, key, timeout=30):
    req = urllib.request.Request(url, method="GET",
        headers={"Authorization": f"Bearer {key}", "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode())


def download(url, dest, timeout=180):
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept": "video/mp4,video/*,*/*"})
    with urllib.request.urlopen(req, timeout=timeout) as r, dest.open("wb") as f:
        n = 0
        while True:
            c = r.read(131072)
            if not c:
                break
            f.write(c); n += len(c)
    return n


def find_urls(data: dict):
    """Defensively pull video URL(s) from any of KIE's known result shapes."""
    paths = []
    resp = data.get("response") or {}
    info = data.get("info") or {}
    for src in (resp, info, data):
        if isinstance(src, dict):
            for k in ("resultUrls", "videoUrls", "videoUrl", "urls"):
                v = src.get(k)
                if v:
                    paths += v if isinstance(v, list) else [v]
    rj = data.get("resultJson") or resp.get("resultJson")
    if rj:
        try:
            paths += (json.loads(rj).get("resultUrls") or [])
        except Exception:
            pass
    # de-dupe preserve order
    seen, out = set(), []
    for u in paths:
        if u and u not in seen:
            seen.add(u); out.append(u)
    return out


def main():
    key = load_key()
    OUT.mkdir(parents=True, exist_ok=True)
    body = {"prompt": PROMPT, "model": "veo3_fast", "generationType": "TEXT_2_VIDEO",
            "aspect_ratio": "9:16", "resolution": "1080p", "duration": 8, "callBackUrl": CALLBACK}
    print("━━━ KIE Veo 3.1 fast smoke test ━━━")
    resp = post(GEN, body, key)
    if resp.get("code") != 200:
        sys.exit(f"submit failed: {resp}")
    tid = (resp.get("data") or {}).get("taskId")
    print(f"  taskId: {tid}")

    info_url = INFO_CANDIDATES[0]
    deadline = time.time() + MAX_MIN * 60
    last = None
    while time.time() < deadline:
        ok = False
        for cand in INFO_CANDIDATES:
            try:
                r = get(f"{cand}?taskId={tid}", key)
                info_url = cand; ok = True
                break
            except urllib.error.HTTPError as e:
                if e.code == 404:
                    continue
                raise
        if not ok:
            print("      no record-info endpoint responded; waiting..."); time.sleep(POLL); continue
        data = r.get("data") or {}
        st = data.get("status") or data.get("successFlag") or r.get("msg")
        if st != last:
            print(f"      status: {st}", flush=True); last = st
        urls = find_urls(data)
        if urls:
            print(f"      {len(urls)} result url(s)")
            for i, u in enumerate(urls, 1):
                dest = OUT / f"veo_smoketest_{i}.mp4"
                sz = download(u, dest)
                print(f"      saved {dest.name} ({sz/1e6:.1f} MB)")
            (OUT / "_result.json").write_text(json.dumps({"taskId": tid, "urls": urls, "info_url": info_url}, indent=2))
            print(f"\n✅ done → {OUT}")
            return 0
        if str(st).upper() in {"GENERATE_AUDIO_FAILED", "CREATE_TASK_FAILED", "FAILED", "FAIL", "ERROR"}:
            sys.exit(f"task failed: {st} | raw={json.dumps(data)[:400]}")
        time.sleep(POLL)
    sys.exit("poll timeout")


if __name__ == "__main__":
    sys.exit(main())
