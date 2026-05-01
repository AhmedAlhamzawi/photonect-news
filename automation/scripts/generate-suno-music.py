#!/usr/bin/env python3
"""Generate one Suno track per HEKAYA story via the Kie AI API.

For each story in `data/hekaya/_research/<date>-hekaya-research.json`, this
script:

  1. POSTs to Kie AI's Suno endpoint with the story's `music_prompt` to start
     a generation task.
  2. Polls the status endpoint until the track is `SUCCESS`.
  3. Downloads the MP3 to `my-video/public/audio/hekaya/<slug>.mp3`.
  4. Writes a manifest JSON describing what was generated.

Each story gets ONE bespoke ~80-120 second instrumental track. No rotation,
no shared tracks — the music is part of the story.

Usage:
    export KIE_AI_API_KEY=<key>
    python3 automation/scripts/generate-suno-music.py 2026-05-01

API reference (verified 2026-05-01):
    POST https://api.kie.ai/api/v1/generate
        Headers: Authorization: Bearer <key>
        Body: {prompt, model, customMode, instrumental, callBackUrl, style, title}
        → 200 {code:200, data:{taskId}}
    GET  https://api.kie.ai/api/v1/generate/record-info?taskId=<id>
        → 200 {code:200, data:{status, response:{sunoData:[{audioUrl,duration,title}]}}}
        Status values: PENDING, TEXT_SUCCESS, FIRST_SUCCESS, SUCCESS,
                       CREATE_TASK_FAILED, GENERATE_AUDIO_FAILED, ...
"""
from __future__ import annotations

import json
import os
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

# ── Config ─────────────────────────────────────────────────────────────────
KIE_BASE = "https://api.kie.ai"
GENERATE_URL = f"{KIE_BASE}/api/v1/generate"
STATUS_URL = f"{KIE_BASE}/api/v1/generate/record-info"

# A free public webhook sink. Kie *requires* a callBackUrl on the generate
# request even if we don't actually consume the callback (we poll instead).
# webhook.site swallows POSTs and returns 200; perfectly fine for our purposes.
DEFAULT_CALLBACK = "https://webhook.site/00000000-0000-0000-0000-000000000000"

# Suno model for HEKAYA. V5 gives best instrumental quality + longer takes.
# V4_5 / V5_5 are also valid; V5 is the documented sweet spot.
SUNO_MODEL = "V5"

# Polling cadence — Suno usually needs 90-180s for an 80-120s track.
POLL_INTERVAL_SECS = 12
MAX_POLL_MINUTES = 12  # safety cap per track

ROOT = Path(__file__).resolve().parents[2]
RESEARCH_DIR = ROOT / "data" / "hekaya" / "_research"
AUDIO_OUT_DIR = ROOT / "my-video" / "public" / "audio" / "hekaya"


# ── HTTP helpers (urllib only — keep this script dependency-free) ──────────
def _http_post(url: str, body: dict, api_key: str, timeout: int = 30) -> dict:
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


def _http_get(url: str, api_key: str, timeout: int = 30) -> dict:
    req = urllib.request.Request(
        url,
        method="GET",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _download(url: str, dest: Path, timeout: int = 90) -> int:
    """Download a URL to disk. Returns bytes written.

    Suno audio URLs land on Cloudflare-fronted tempfile.aiquickdraw.com which
    blocks the default Python-urllib UA with HTTP 403. We must send a browser
    User-Agent for the download to succeed.
    """
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36"
            ),
            "Accept": "audio/mpeg, audio/*, */*",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp, dest.open("wb") as f:
        size = 0
        while True:
            chunk = resp.read(64 * 1024)
            if not chunk:
                break
            f.write(chunk)
            size += len(chunk)
    return size


# ── Suno task lifecycle ────────────────────────────────────────────────────
def submit_generation(api_key: str, prompt: str, title: str, style: str | None = None) -> str:
    """Submit a Suno generation task. Returns taskId on success.

    We use customMode=False because the `prompt` field is the natural-language
    description and Kie's customMode toggle is for advanced multi-clip layouts
    — not what HEKAYA needs.
    """
    body = {
        "prompt": prompt,
        "model": SUNO_MODEL,
        "customMode": False,
        "instrumental": True,            # HEKAYA tracks are vocal-free
        "callBackUrl": os.environ.get("KIE_CALLBACK_URL", DEFAULT_CALLBACK),
        "title": title[:80],             # Suno API caps title at 80 chars
    }
    if style:
        body["style"] = style

    resp = _http_post(GENERATE_URL, body, api_key)
    if resp.get("code") != 200:
        raise RuntimeError(f"submit failed: code={resp.get('code')} msg={resp.get('msg')!r}")
    task_id = resp.get("data", {}).get("taskId")
    if not task_id:
        raise RuntimeError(f"submit returned no taskId: {resp!r}")
    return task_id


def poll_until_done(api_key: str, task_id: str) -> dict:
    """Poll the task until it finishes. Returns the `data` block on SUCCESS.

    Raises RuntimeError on failure status or timeout.
    """
    deadline = time.time() + MAX_POLL_MINUTES * 60
    last_status: str | None = None

    while time.time() < deadline:
        resp = _http_get(f"{STATUS_URL}?taskId={task_id}", api_key)
        if resp.get("code") != 200:
            # Transient HTTP errors — back off and retry once.
            time.sleep(POLL_INTERVAL_SECS)
            continue

        data = resp.get("data") or {}
        status = data.get("status")
        if status != last_status:
            print(f"      status: {status}", flush=True)
            last_status = status

        if status == "SUCCESS":
            return data
        if status in {"CREATE_TASK_FAILED", "GENERATE_AUDIO_FAILED",
                      "CALLBACK_EXCEPTION", "SENSITIVE_WORD_ERROR"}:
            raise RuntimeError(f"task {task_id} failed: status={status}")

        time.sleep(POLL_INTERVAL_SECS)

    raise RuntimeError(f"task {task_id} timed out after {MAX_POLL_MINUTES} min")


def first_audio_url(task_data: dict) -> str:
    suno = (task_data.get("response") or {}).get("sunoData") or []
    if not suno:
        raise RuntimeError(f"no sunoData in task: {task_data!r}")
    url = suno[0].get("audioUrl")
    if not url:
        raise RuntimeError(f"no audioUrl in first track: {suno[0]!r}")
    return url


# ── Orchestration ──────────────────────────────────────────────────────────
def style_for(story: dict) -> str:
    """Compose a short Suno style hint from the story's place + era.

    Keeps the regional sonic palette in the right neighbourhood (oud/ney for
    Andalus and Baghdad, qanun for Yemen, etc.) without overriding the music
    prompt the researcher gave us.
    """
    place = (story.get("place") or "").lower()
    if "andalus" in place or "córdoba" in place or "cordoba" in place or "spain" in place:
        return "Andalusian oud + warm strings, instrumental, slow"
    if "baghdad" in place or "iraq" in place:
        return "Mesopotamian oud + soft ney, instrumental, dusk"
    if "yemen" in place or "mocha" in place:
        return "Arabian Peninsula qanun + soft percussion, instrumental"
    if "fez" in place or "morocco" in place:
        return "Maghrebi oud + soft strings, instrumental, slow"
    if "khwarazm" in place or "uzbek" in place:
        return "Central-Asian dutar + ambient strings, instrumental"
    return "Middle-Eastern oud + ambient strings, instrumental, slow"


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: generate-suno-music.py <YYYY-MM-DD>", file=sys.stderr)
        return 2
    date = sys.argv[1]

    api_key = os.environ.get("KIE_AI_API_KEY")
    if not api_key:
        print("error: KIE_AI_API_KEY not set in environment", file=sys.stderr)
        return 2

    research_path = RESEARCH_DIR / f"{date}-hekaya-research.json"
    if not research_path.is_file():
        print(f"error: research file missing: {research_path}", file=sys.stderr)
        return 2

    stories = json.loads(research_path.read_text())
    if not stories:
        print(f"error: no stories in {research_path}", file=sys.stderr)
        return 2

    print(f"━━━ HEKAYA Suno generation — {date} ({len(stories)} tracks) ━━━")
    AUDIO_OUT_DIR.mkdir(parents=True, exist_ok=True)
    manifest: list[dict] = []

    for i, story in enumerate(stories, start=1):
        slug = story["slug"]
        prompt = story.get("music_prompt") or "Slow ambient oud + soft strings, instrumental, dusk"
        title = (story.get("title_en") or slug).replace("—", "-")

        dest_mp3 = AUDIO_OUT_DIR / f"{slug}.mp3"
        if dest_mp3.is_file() and dest_mp3.stat().st_size > 200_000:
            print(f"  [{i}/{len(stories)}] {slug} — already exists, skipping")
            manifest.append({"slug": slug, "audio": f"audio/hekaya/{slug}.mp3", "skipped": True})
            continue

        print(f"  [{i}/{len(stories)}] {slug}")
        print(f"      prompt: {prompt}")
        try:
            task_id = submit_generation(api_key, prompt=prompt, title=title, style=style_for(story))
            print(f"      taskId: {task_id}")
            data = poll_until_done(api_key, task_id)
            audio_url = first_audio_url(data)
            print(f"      audio:  {audio_url[:90]}...")
            size = _download(audio_url, dest_mp3)
            mb = size / (1024 * 1024)
            print(f"      saved:  {dest_mp3.name}  ({mb:.1f} MB)")
            manifest.append(
                {
                    "slug": slug,
                    "task_id": task_id,
                    "audio": f"audio/hekaya/{slug}.mp3",
                    "size_bytes": size,
                    "remote_url": audio_url,
                }
            )
        except (urllib.error.HTTPError, urllib.error.URLError, RuntimeError) as e:
            print(f"      FAIL:   {e}")
            manifest.append({"slug": slug, "error": str(e)})

    # Write a manifest so the workflow / future runs can see what happened.
    manifest_path = AUDIO_OUT_DIR / f"_manifest-{date}.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False))
    print(f"\nmanifest: {manifest_path}")

    failed = [m for m in manifest if "error" in m]
    if failed:
        print(f"⚠  {len(failed)} track(s) failed — see manifest")
        return 1
    print(f"✅  all {len(manifest)} tracks ready")
    return 0


if __name__ == "__main__":
    sys.exit(main())
