#!/usr/bin/env python3
"""Auto-post a rendered day's reels to Instagram (Reels) + TikTok via upload-post.com.

Called by `.github/workflows/render-day.yml` after the Drive upload step. Posts the
LOCAL video.mp4 (+ caption.txt) for each slug of a given date via upload-post's
unified API, so we never touch Meta/TikTok app review ourselves.

Safety:
  - No-op (exit 0) when UPLOAD_POST_API_KEY is unset — safe to ship before keys exist.
  - Idempotent: writes .posted.json per slug; re-runs skip already-posted slugs.
  - Per-slug fail isolation: one bad slug/platform never aborts the rest.
  - Stdlib only (urllib) — no extra CI dependency.

Run locally:
    export UPLOAD_POST_API_KEY=...
    python3 automation/scripts/post-to-uploadpost.py --date 2026-06-28 --user photonect-news
    # add --dry-run to list what WOULD post without calling the API
"""
from __future__ import annotations

import argparse
import json
import mimetypes
import os
import sys
import time
import urllib.request
import urllib.error
import uuid
from pathlib import Path

UPLOAD_URL = "https://api.upload-post.com/api/upload"
STATUS_URL = "https://api.upload-post.com/api/uploadposts/status"
POLL_INTERVAL = 10          # seconds
MAX_POLL_MIN = 10           # per slug
SLEEP_BETWEEN_SLUGS = 4     # gentle gap to avoid per-minute bursts

ROOT = Path(__file__).resolve().parents[2]   # NEWS CODE/
POSTS = ROOT / "data" / "posts"


def api_key() -> str:
    return os.environ.get("UPLOAD_POST_API_KEY", "").strip()


def _encode_multipart(fields: list[tuple[str, str]], file_field: str, file_path: Path):
    """Build a multipart/form-data body from text fields + one file. Returns (body, content_type).

    `fields` is a list of (name, value) pairs; repeat a name (e.g. 'platform[]') for arrays.
    """
    boundary = f"----photonect{uuid.uuid4().hex}"
    crlf = b"\r\n"
    out = bytearray()
    for name, value in fields:
        out += b"--" + boundary.encode() + crlf
        out += f'Content-Disposition: form-data; name="{name}"'.encode() + crlf + crlf
        out += str(value).encode("utf-8") + crlf
    # file part
    mime = mimetypes.guess_type(file_path.name)[0] or "video/mp4"
    out += b"--" + boundary.encode() + crlf
    out += (f'Content-Disposition: form-data; name="{file_field}"; '
            f'filename="{file_path.name}"').encode() + crlf
    out += f"Content-Type: {mime}".encode() + crlf + crlf
    out += file_path.read_bytes() + crlf
    out += b"--" + boundary.encode() + b"--" + crlf
    return bytes(out), f"multipart/form-data; boundary={boundary}"


def submit(video: Path, caption: str, user: str, platforms: list[str]) -> str:
    fields = [("user", user), ("title", caption)]
    for p in platforms:
        fields.append(("platform[]", p))
    fields += [
        ("media_type", "REELS"),          # IG → Reel
        ("share_to_feed", "true"),        # also show in grid
        ("post_mode", "DIRECT_POST"),     # TikTok publishes live
        ("privacy_level", "PUBLIC_TO_EVERYONE"),
        ("is_aigc", "true"),              # AI-generated-content disclosure
        ("async_upload", "true"),         # background processing → request_id
    ]
    body, content_type = _encode_multipart(fields, "video", video)
    req = urllib.request.Request(
        UPLOAD_URL, data=body, method="POST",
        headers={"Authorization": f"Apikey {api_key()}", "Content-Type": content_type,
                 "Accept": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=180) as r:
        resp = json.loads(r.read().decode("utf-8"))
    rid = resp.get("request_id") or (resp.get("data") or {}).get("request_id")
    if not rid:
        raise RuntimeError(f"no request_id in response: {str(resp)[:300]}")
    return rid


def poll(request_id: str) -> dict:
    deadline = time.time() + MAX_POLL_MIN * 60
    url = f"{STATUS_URL}?request_id={request_id}"
    last = None
    while time.time() < deadline:
        try:
            req = urllib.request.Request(
                url, headers={"Authorization": f"Apikey {api_key()}", "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=30) as r:
                data = json.loads(r.read().decode("utf-8"))
        except Exception as e:
            print(f"    poll error: {e}", file=sys.stderr)
            time.sleep(POLL_INTERVAL); continue
        st = str(data.get("status") or (data.get("data") or {}).get("status") or "").lower()
        if st != last:
            print(f"    status: {st or '?'}", flush=True); last = st
        if st in ("completed", "success", "done", "failed", "error", "partial"):
            return data
        time.sleep(POLL_INTERVAL)
    raise RuntimeError("poll timeout")


def per_platform_results(status: dict) -> dict:
    """Best-effort extraction of {platform: success_bool} from the status payload."""
    out = {}
    def walk(o):
        if isinstance(o, dict):
            plat = o.get("platform")
            if plat and "success" in o:
                out[str(plat)] = bool(o.get("success"))
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for it in o:
                walk(it)
    walk(status)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", required=True, help="YYYY-MM-DD")
    ap.add_argument("--user", required=True, help="upload-post profile handle holding the connected accounts")
    ap.add_argument("--platforms", default="instagram,tiktok")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    platforms = [p.strip() for p in args.platforms.split(",") if p.strip()]

    if not args.dry_run and not api_key():
        print("UPLOAD_POST_API_KEY unset — skipping auto-post (no-op).")
        return 0

    slugs = sorted(d for d in POSTS.glob(f"{args.date}-*") if d.is_dir())
    if not slugs:
        print(f"no post folders under {POSTS}/{args.date}-*", file=sys.stderr)
        return 1

    posted = skipped = failed = 0
    for slug_dir in slugs:
        name = slug_dir.name
        video = slug_dir / "video.mp4"
        caption_file = slug_dir / "caption.txt"
        marker = slug_dir / ".posted.json"
        if not video.is_file():
            print(f"  skip {name}: no video.mp4"); skipped += 1; continue
        if marker.is_file():
            print(f"  skip {name}: already posted"); skipped += 1; continue
        caption = caption_file.read_text(encoding="utf-8").strip() if caption_file.is_file() else ""
        if args.dry_run:
            print(f"  [dry-run] would post {name} → {platforms}  (caption {len(caption)} chars)")
            posted += 1; continue
        try:
            rid = submit(video, caption, args.user, platforms)
            print(f"  → {name}: request_id={rid}", flush=True)
            status = poll(rid)
            results = per_platform_results(status)
            marker.write_text(json.dumps(
                {"request_id": rid, "results": results, "date": args.date}, ensure_ascii=False, indent=2))
            ok = [p for p, v in results.items() if v]
            bad = [p for p, v in results.items() if not v]
            print(f"  ✓ {name}: posted={ok or '?'}" + (f"  FAILED={bad}" if bad else ""), flush=True)
            posted += 1
            if bad:
                failed += 1
        except Exception as e:
            print(f"  ✗ {name}: {e}", file=sys.stderr); failed += 1
        time.sleep(SLEEP_BETWEEN_SLUGS)

    print(f"\nauto-post: posted {posted}/{len(slugs)}  (skipped {skipped}, with-failures {failed})")
    return 0 if posted > 0 else 1


if __name__ == "__main__":
    sys.exit(main())
