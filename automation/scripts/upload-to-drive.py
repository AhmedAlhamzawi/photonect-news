#!/usr/bin/env python3
"""Upload a rendered day's video.mp4 + caption.txt pairs to Google Drive.

Called by `.github/workflows/render-day.yml` after `generate-daily.sh` finishes.
Target layout inside Drive:

    <PARENT_FOLDER>/
        2026-04-24/
            2026-04-24-slug-a/
                video.mp4
                caption.txt
            2026-04-24-slug-b/
                ...

Ahmed opens Drive on his phone, finds the dated folder, picks a slug, and
long-presses video + caption to post to IG/TikTok.

Run locally:
    export DRIVE_PARENT_FOLDER_ID=...
    python3 automation/scripts/upload-to-drive.py \\
        --date 2026-04-24 \\
        --parent-id "$DRIVE_PARENT_FOLDER_ID" \\
        --credentials ~/.config/gcloud/application_default_credentials.json
"""

from __future__ import annotations

import argparse
import mimetypes
import sys
from pathlib import Path

# These are only needed at runtime (CI installs them via pip)
try:
    from google.auth import load_credentials_from_file  # type: ignore
    from googleapiclient.discovery import build  # type: ignore
    from googleapiclient.http import MediaFileUpload  # type: ignore
except ImportError as e:
    print(f"error: {e}. Install with: pip install google-api-python-client google-auth",
          file=sys.stderr)
    sys.exit(2)

SCOPES = ["https://www.googleapis.com/auth/drive.file"]
# drive.file scope limits whoever authenticates to files they create themselves —
# it can never read or modify the user's other Drive content.

ROOT = Path(__file__).resolve().parents[2]       # NEWS CODE/
POSTS = ROOT / "data" / "posts"


def drive_client(credentials_path: Path):
    """Load credentials from a JSON file.

    Accepts either an 'authorized_user' (OAuth refresh token) or a
    'service_account' JSON. Ahmed's account uses personal Drive, which requires
    authorized_user — service accounts have no storage quota in personal Drives.
    """
    creds, _ = load_credentials_from_file(str(credentials_path), scopes=SCOPES)
    return build("drive", "v3", credentials=creds, cache_discovery=False)


def find_or_create_folder(service, name: str, parent_id: str) -> str:
    """Return folder ID, creating the folder under parent if needed."""
    # Quote name safely: escape single quotes by doubling them per Drive query rules
    safe_name = name.replace("'", "\\'")
    q = (
        f"name = '{safe_name}' "
        f"and mimeType = 'application/vnd.google-apps.folder' "
        f"and '{parent_id}' in parents "
        f"and trashed = false"
    )
    resp = service.files().list(
        q=q, fields="files(id, name)", pageSize=10,
        supportsAllDrives=True, includeItemsFromAllDrives=True,
    ).execute()
    files = resp.get("files", [])
    if files:
        return files[0]["id"]
    folder = service.files().create(
        body={
            "name": name,
            "mimeType": "application/vnd.google-apps.folder",
            "parents": [parent_id],
        },
        fields="id",
        supportsAllDrives=True,
    ).execute()
    return folder["id"]


def upload_file(service, local_path: Path, parent_id: str) -> str:
    mime, _ = mimetypes.guess_type(local_path.name)
    if mime is None:
        mime = "application/octet-stream"
    media = MediaFileUpload(str(local_path), mimetype=mime, resumable=True)
    resp = service.files().create(
        body={"name": local_path.name, "parents": [parent_id]},
        media_body=media,
        fields="id, name, size",
        supportsAllDrives=True,
    ).execute()
    return resp["id"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", required=True, help="YYYY-MM-DD")
    ap.add_argument("--parent-id", required=True,
                    help="Drive folder ID to upload into (the dated folder is created under this)")
    ap.add_argument("--credentials", required=True,
                    help="Path to Drive credentials JSON (OAuth 'authorized_user' or service account)")
    ap.add_argument("--trial-label", default=None,
                    help="Optional trial-comparison subfolder (e.g. 'Trial 2'). When set, uploads "
                         "land inside <date>/<trial-label>/<slug>/ instead of <date>/<slug>/. "
                         "Used by leap-mandate runs to surface Trial 1 vs Trial 2 side-by-side "
                         "in Drive without overwriting.")
    args = ap.parse_args()

    creds_path = Path(args.credentials)
    if not creds_path.is_file():
        print(f"error: credentials file missing: {creds_path}", file=sys.stderr)
        return 2

    slugs = sorted(d for d in POSTS.glob(f"{args.date}-*") if d.is_dir())
    if not slugs:
        print(f"error: no post folders under {POSTS}/{args.date}-*", file=sys.stderr)
        return 2

    service = drive_client(creds_path)
    date_folder_id = find_or_create_folder(service, args.date, args.parent_id)
    print(f"→ Drive folder for {args.date}: {date_folder_id}")

    # Trial-subfolder support (leap-mandate runs). If the workflow passes a
    # --trial-label like "Trial 2", we create that subfolder under the date
    # folder and upload there. Trial 1 is conventionally uploaded WITHOUT a
    # label (lands at the date folder root), so Ahmed sees Trial 1 files at
    # the top alongside a "Trial 2" subfolder.
    upload_root_id = date_folder_id
    if args.trial_label:
        upload_root_id = find_or_create_folder(service, args.trial_label, date_folder_id)
        print(f"→ Trial subfolder '{args.trial_label}': {upload_root_id}")

    uploaded, skipped = 0, 0
    for slug_dir in slugs:
        video = slug_dir / "video.mp4"
        caption = slug_dir / "caption.txt"
        if not video.is_file() or not caption.is_file():
            print(f"  skip {slug_dir.name} (missing video.mp4 or caption.txt)")
            skipped += 1
            continue

        slug_folder_id = find_or_create_folder(service, slug_dir.name, upload_root_id)
        upload_file(service, video, slug_folder_id)
        upload_file(service, caption, slug_folder_id)
        size_mb = video.stat().st_size // (1024 * 1024)
        print(f"  ✓ {slug_dir.name}  ({size_mb} MB)")
        uploaded += 1

    print(f"\n{uploaded} slug(s) uploaded, {skipped} skipped")
    return 0 if uploaded > 0 else 1


if __name__ == "__main__":
    sys.exit(main())
