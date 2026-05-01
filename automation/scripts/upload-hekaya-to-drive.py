#!/usr/bin/env python3
"""Upload a rendered HEKAYA day's video.mp4 + caption.txt pairs to Drive.

Sister script to `upload-to-drive.py`. The two stay separate so HEKAYA reels
NEVER mix with NEWS reels in Drive.

Target layout inside the existing Photonect Drive parent:

    <PARENT_FOLDER>/
        Photonect HEKAYA/                      ← created if missing
            2026-05-01/
                2026-05-01-fatima-al-fihri-qarawiyyin/
                    video.mp4
                    caption.txt
                ...

The "Photonect HEKAYA" subfolder is created on first run and reused thereafter.
This keeps HEKAYA browsable as its own world inside the parent Photonect folder.

Run locally:
    python3 automation/scripts/upload-hekaya-to-drive.py \\
        --date 2026-05-01 \\
        --parent-id "$DRIVE_PARENT_FOLDER_ID" \\
        --credentials ~/.config/gcloud/application_default_credentials.json
"""
from __future__ import annotations

import argparse
import mimetypes
import sys
from pathlib import Path

try:
    from google.auth import load_credentials_from_file  # type: ignore
    from googleapiclient.discovery import build  # type: ignore
    from googleapiclient.http import MediaFileUpload  # type: ignore
except ImportError as e:
    print(f"error: {e}. Install with: pip install google-api-python-client google-auth",
          file=sys.stderr)
    sys.exit(2)

# Same OAuth scope as the news upload script — drive.file is intentionally
# narrow (we can only see / modify files we ourselves create).
SCOPES = ["https://www.googleapis.com/auth/drive.file"]

ROOT = Path(__file__).resolve().parents[2]              # NEWS CODE/
HEKAYA_DIR = ROOT / "data" / "hekaya"

# The name of the HEKAYA folder we create inside the existing Photonect parent.
# Keep this STABLE — renaming after first run will fork uploads.
HEKAYA_TRACK_FOLDER = "Photonect HEKAYA"


def drive_client(credentials_path: Path):
    creds, _ = load_credentials_from_file(str(credentials_path), scopes=SCOPES)
    return build("drive", "v3", credentials=creds, cache_discovery=False)


def find_or_create_folder(service, name: str, parent_id: str) -> str:
    """Return the folder id, creating the folder under parent if needed."""
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
                    help="Drive ID of the existing Photonect NEWS parent folder. "
                         "We create a 'Photonect HEKAYA' subfolder under this on first run.")
    ap.add_argument("--credentials", required=True,
                    help="Path to Drive credentials JSON")
    args = ap.parse_args()

    creds_path = Path(args.credentials)
    if not creds_path.is_file():
        print(f"error: credentials file missing: {creds_path}", file=sys.stderr)
        return 2

    slugs = sorted(d for d in HEKAYA_DIR.glob(f"{args.date}-*") if d.is_dir())
    if not slugs:
        print(f"error: no hekaya folders under {HEKAYA_DIR}/{args.date}-*", file=sys.stderr)
        return 2

    service = drive_client(creds_path)

    # 1) Find/create the persistent "Photonect HEKAYA" folder under the parent.
    track_folder_id = find_or_create_folder(service, HEKAYA_TRACK_FOLDER, args.parent_id)
    print(f"→ HEKAYA track folder: {track_folder_id}")

    # 2) Find/create today's date subfolder under the track folder.
    date_folder_id = find_or_create_folder(service, args.date, track_folder_id)
    print(f"→ Drive folder for HEKAYA {args.date}: {date_folder_id}")

    uploaded, skipped = 0, 0
    for slug_dir in slugs:
        video = slug_dir / "video.mp4"
        caption = slug_dir / "caption.txt"
        if not video.is_file() or not caption.is_file():
            print(f"  skip {slug_dir.name} (missing video.mp4 or caption.txt)")
            skipped += 1
            continue

        slug_folder_id = find_or_create_folder(service, slug_dir.name, date_folder_id)
        upload_file(service, video, slug_folder_id)
        upload_file(service, caption, slug_folder_id)
        size_mb = video.stat().st_size // (1024 * 1024)
        print(f"  ✓ {slug_dir.name}  ({size_mb} MB)")
        uploaded += 1

    print(f"\n{uploaded} hekaya slug(s) uploaded, {skipped} skipped")
    return 0 if uploaded > 0 else 1


if __name__ == "__main__":
    sys.exit(main())
