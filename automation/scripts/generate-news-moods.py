#!/usr/bin/env python3
"""Regenerate the 4 NEWS rotation mood beds via Kie AI Suno.

The NEWS track has always rotated 4 mood beds — cinematic / newsroom /
orchestral / mideast — so that adjacent posts in a daily slate never share a
track. The previous beds were CC0 Pexels stock that Ahmed (2026-05-02) called
"boring" — humans need emotion, and stock music doesn't deliver it.

This script regenerates all four moods as Suno V5 originals:
  - Each track is unique, instrumental, broadcast-grade
  - Each has a deliberate emotional register (urgent / cinematic / orchestral /
    middle-eastern modern)
  - Total runtime per track ~3-5 min so the rotation script can crop or fade
    inside any 58-second reel

Output overwrites:
  my-video/public/audio/mood_cinematic.mp3
  my-video/public/audio/mood_newsroom.mp3
  my-video/public/audio/mood_orchestral.mp3
  my-video/public/audio/mood_mideast.mp3

These filenames are referenced from automation/scripts/assign-mood-rotation.py
and from the Remotion AVAILABLE_BEDS set, so the rotation continues to work
unchanged — only the audio behind the names becomes Suno-generated.

Usage:
    export KIE_AI_API_KEY=<key>
    python3 automation/scripts/generate-news-moods.py
"""
from __future__ import annotations

import json
import os
import sys
import time
import urllib.request
from pathlib import Path

KIE_BASE = "https://api.kie.ai"
GENERATE_URL = f"{KIE_BASE}/api/v1/generate"
STATUS_URL = f"{KIE_BASE}/api/v1/generate/record-info"
DEFAULT_CALLBACK = "https://webhook.site/00000000-0000-0000-0000-000000000000"
SUNO_MODEL = "V5"
POLL_INTERVAL_SECS = 12
MAX_POLL_MINUTES = 12

ROOT = Path(__file__).resolve().parents[2]
AUDIO_OUT_DIR = ROOT / "my-video" / "public" / "audio"

# 4 moods × emotional register. Each prompt is engineered to be:
#   - Distinctly different from the other three
#   - Broadcast-quality (Bloomberg / Aljazeera / Vice News territory)
#   - Emotional but not overwrought — news has gravity, not melodrama
#   - 100% instrumental
MOODS = [
    {
        "slug": "mood_cinematic",
        "title": "Photonect News — Cinematic",
        "style": "Cinematic Documentary, Instrumental",
        "prompt": (
            "Slow cinematic news-documentary score. Solo piano on a sustained low cello drone, "
            "soft strings entering at the second minute, distant filmic reverb, low sub-bass pulse "
            "every four bars. Mood: gravity, tension held under restraint, the weight of an "
            "unfolding story. 72 BPM, instrumental, no vocals, no drums."
        ),
    },
    {
        "slug": "mood_newsroom",
        "title": "Photonect News — Newsroom Pulse",
        "style": "Modern Broadcast, Electronic, Instrumental",
        "prompt": (
            "Modern broadcast newsroom score. Crisp synth arpeggios pulsing in 16ths, taut "
            "felt-piano staccato, a tight low kick on the downbeat, quiet hi-hat shuffle, "
            "occasional risers. Mood: alert, kinetic, professional, the rhythm of a desk on "
            "deadline. 110 BPM, instrumental, no vocals."
        ),
    },
    {
        "slug": "mood_orchestral",
        "title": "Photonect News — Orchestral Gravity",
        "style": "Orchestral Score, Instrumental",
        "prompt": (
            "Slow orchestral score with gravitas. Low strings sustaining a minor pedal, soft brass "
            "swelling under a single piano motif, distant timpani, no melodrama. Mood: a long-read "
            "headline at dusk — historic, sober, reflective. 68 BPM, instrumental, no vocals."
        ),
    },
    {
        "slug": "mood_mideast",
        "title": "Photonect News — Middle East Modern",
        "style": "Modern Middle-Eastern, Cinematic, Instrumental",
        "prompt": (
            "Modern Middle-Eastern broadcast score. Solo oud over a sub-bass drone, distant ney "
            "flute, qanun glissando filtering in and out, light electronic texture, no percussion. "
            "Mood: sand-light at golden hour over Baghdad/Beirut/Doha — regional, contemporary, "
            "emotional but composed. 80 BPM, instrumental, no vocals."
        ),
    },
]


def _http_post(url, body, api_key, timeout=30):
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode("utf-8"),
        method="POST",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _http_get(url, api_key, timeout=30):
    req = urllib.request.Request(
        url, method="GET",
        headers={"Authorization": f"Bearer {api_key}", "Accept": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _download(url, dest, timeout=120):
    """Download with browser User-Agent — Cloudflare 403s the urllib default."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={
        "User-Agent": ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                        "AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/124.0.0.0 Safari/537.36"),
        "Accept": "audio/mpeg, audio/*, */*",
    })
    with urllib.request.urlopen(req, timeout=timeout) as resp, dest.open("wb") as f:
        size = 0
        while True:
            chunk = resp.read(64 * 1024)
            if not chunk: break
            f.write(chunk); size += len(chunk)
    return size


def submit(api_key, mood):
    body = {
        "prompt": mood["prompt"],
        "model": SUNO_MODEL,
        "customMode": False,
        "instrumental": True,
        "callBackUrl": os.environ.get("KIE_CALLBACK_URL", DEFAULT_CALLBACK),
        "title": mood["title"][:80],
        "style": mood["style"],
    }
    r = _http_post(GENERATE_URL, body, api_key)
    if r.get("code") != 200:
        raise RuntimeError(f"submit failed for {mood['slug']}: {r!r}")
    task_id = r.get("data", {}).get("taskId")
    if not task_id:
        raise RuntimeError(f"no taskId in response: {r!r}")
    return task_id


def poll(api_key, task_id):
    deadline = time.time() + MAX_POLL_MINUTES * 60
    last_status = None
    while time.time() < deadline:
        r = _http_get(f"{STATUS_URL}?taskId={task_id}", api_key)
        if r.get("code") != 200:
            time.sleep(POLL_INTERVAL_SECS); continue
        data = r.get("data") or {}
        status = data.get("status")
        if status != last_status:
            print(f"      status: {status}", flush=True); last_status = status
        if status == "SUCCESS":
            return data
        if status in {"CREATE_TASK_FAILED", "GENERATE_AUDIO_FAILED",
                       "CALLBACK_EXCEPTION", "SENSITIVE_WORD_ERROR"}:
            raise RuntimeError(f"failed: status={status}")
        time.sleep(POLL_INTERVAL_SECS)
    raise RuntimeError(f"timed out after {MAX_POLL_MINUTES} min")


def first_audio_url(task_data):
    suno = (task_data.get("response") or {}).get("sunoData") or []
    if not suno: raise RuntimeError(f"no sunoData: {task_data!r}")
    url = suno[0].get("audioUrl")
    if not url: raise RuntimeError(f"no audioUrl: {suno[0]!r}")
    return url


def main():
    api_key = os.environ.get("KIE_AI_API_KEY")
    if not api_key:
        print("error: KIE_AI_API_KEY not set", file=sys.stderr); return 2

    print(f"━━━ NEWS mood-bed regeneration via Suno V5 ({len(MOODS)} tracks) ━━━")
    AUDIO_OUT_DIR.mkdir(parents=True, exist_ok=True)
    manifest = []

    for i, mood in enumerate(MOODS, start=1):
        slug = mood["slug"]
        dest = AUDIO_OUT_DIR / f"{slug}.mp3"
        print(f"  [{i}/{len(MOODS)}] {slug}")
        print(f"      style:  {mood['style']}")
        print(f"      prompt: {mood['prompt'][:90]}…")
        try:
            tid = submit(api_key, mood)
            print(f"      taskId: {tid}")
            data = poll(api_key, tid)
            url = first_audio_url(data)
            print(f"      audio:  {url[:90]}…")
            size = _download(url, dest)
            print(f"      saved:  {dest.name}  ({size/(1024*1024):.1f} MB)")
            manifest.append({"slug": slug, "task_id": tid, "size_bytes": size, "remote_url": url})
        except Exception as e:
            print(f"      FAIL:   {e}")
            manifest.append({"slug": slug, "error": str(e)})

    mp = AUDIO_OUT_DIR / "_manifest-news-moods.json"
    mp.write_text(json.dumps(manifest, indent=2, ensure_ascii=False))
    print(f"\nmanifest: {mp}")
    failed = [m for m in manifest if "error" in m]
    if failed:
        print(f"⚠  {len(failed)} mood(s) failed"); return 1
    print(f"✅  all {len(manifest)} NEWS moods regenerated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
