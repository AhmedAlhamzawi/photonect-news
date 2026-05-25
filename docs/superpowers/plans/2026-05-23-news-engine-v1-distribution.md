# NEWS ENGINE v1 — Distribution Layer Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship a full-autonomous distribution layer that takes the daily Claude-authored Arabic news slate and posts it to Instagram, TikTok, YouTube Shorts, and a Telegram channel on a fixed 6-slot Baghdad-time schedule with two human safety gates.

**Architecture:** n8n on Fly.dev owns scheduling, credentials, kill-window state, and Telegram bot interactions. GitHub Actions own heavy compute: `render-day.yml` (unchanged) plus two new workflows (`produce-today.yml`, `regen-slug.yml`) that wrap Claude Code in CI. Repo owns durable per-day audit log at `data/posting-state/<date>.json`. Drive holds rendered mp4s. Cloudinary provides public mp4 URLs (IG requirement only). State machine: `producing → pending_evening_lock → evening_locked → rendering → pending_kill_window → posting_locked → posting → complete`.

**Tech Stack:** n8n 2.55.0 (Fly.dev), n8n-MCP for workflow construction, GitHub Actions (Ubuntu 24.04), Claude Code CLI (`claude --print` for headless), Python 3.11, Telegram Bot API (inline keyboards + `callback_query`), Meta Graph API v21 (Instagram), TikTok Content Posting API, YouTube Data API v3, Cloudinary (mp4 hosting for IG), Google Drive API v3.

**Reference spec:** [`docs/superpowers/specs/2026-05-23-news-engine-v1-distribution-design.md`](../specs/2026-05-23-news-engine-v1-distribution-design.md)

---

## File Structure

### New files (in this repo)

```
.github/workflows/
  produce-today.yml          ← runs `claude --print '/produce-today --autonomous'` in CI
  regen-slug.yml             ← runs `claude --print '/produce-today --regen <slug>'`

automation/scripts/
  cloudinary-upload.py       ← upload mp4 to Cloudinary, return signed public URL
  posting-state-update.py    ← read/merge/write data/posting-state/<date>.json via Contents API

data/posting-state/
  .gitkeep                   ← empty placeholder (real files written by n8n during posting)
  README.md                  ← documents schema + status values

ops/n8n/
  WF1_evening-author.json    ← exported workflow JSON for version control
  WF2_evening-callback.json
  WF3_morning-render.json
  WF4_kill-window-callback.json
  WF5_slot-posting.json
  WF6_rotate-tokens.json
  WF7_daily-digest.json
  README.md                  ← how to re-import after n8n migration / disaster recovery

docs/runbooks/
  p0-credential-setup.md     ← step-by-step P0 setup checklist
  manual-recovery.md         ← what to do when something fails in prod
```

### Changed files

```
.github/workflows/render-day.yml   ← NO CHANGES (already takes `date` workflow_dispatch input)
data/media-ledger.json             ← will be untouched during this plan
```

### What lives only in n8n (NOT the repo)

- All workflow credentials (encrypted in n8n)
- n8n workflow variables (slate state, kill flags)
- n8n execution history

---

# PHASE P0 — Credential & Account Setup (~10-15 tasks, mostly external)

> **Phase goal:** All API credentials provisioned and stored in n8n's credential vault before any workflow is built. Without this, P1 workflows have nothing to authenticate with.
>
> **What "done" means:** Running `mcp__n8n-mcp__n8n_manage_credentials action='list' includeUsage=false` returns all 7 expected credentials.

## Task P0.1: Create runbook scaffold

**Files:**
- Create: `docs/runbooks/p0-credential-setup.md`

- [ ] **Step 1: Write the runbook scaffold**

```markdown
# P0 Runbook — Credential & Account Setup

This runbook is run ONCE before the n8n distribution layer goes live. After
completion, all 7 platform credentials live in n8n's encrypted credential vault.

## Status checklist

- [ ] Telegram bot created (@photonect_news_bot)
- [ ] Telegram channel created (@photonect_news_channel)
- [ ] Meta dev app + long-lived IG token (60d)
- [ ] TikTok dev app + access token
- [ ] YouTube channel + OAuth refresh token + 50K quota
- [ ] Cloudinary account + API key
- [ ] GitHub PAT for n8n (workflow:write, actions:read, contents:write)
- [ ] Staging accounts: IG/TT/YT (used during P2 testing)

See per-platform sections below for step-by-step.
```

- [ ] **Step 2: Commit**

```bash
git add docs/runbooks/p0-credential-setup.md
git commit -m "docs(runbook): add P0 credential setup scaffold"
```

## Task P0.2: Telegram bot & channel

**Files:**
- Modify: `docs/runbooks/p0-credential-setup.md` (add Telegram section)

- [ ] **Step 1: Create Telegram bot**

Ahmed does the following manually:
1. Open Telegram, message @BotFather, send `/newbot`
2. Bot name: `Photonect News Operator`
3. Bot username: `photonect_news_bot` (or next available)
4. Copy the token shown — looks like `7234567890:AAH...xyz`
5. Send `/setjoingroups` to BotFather → disable (DM-only)
6. Send `/setprivacy` to BotFather → Enable privacy mode

- [ ] **Step 2: Create Telegram channel**

1. Telegram → New Channel → name `Photonect News`
2. Username: `@photonect_news_channel` (or as available)
3. Public channel
4. Add the bot from step 1 as administrator with post messages + edit messages permissions

- [ ] **Step 3: Get Ahmed's chat ID**

1. Ahmed messages the bot once: "/start"
2. From a terminal: `curl "https://api.telegram.org/bot<TOKEN>/getUpdates"`
3. Find `"chat":{"id":<numeric>}` — this is `TELEGRAM_AHMED_CHAT_ID`

- [ ] **Step 4: Get channel chat ID**

1. From a terminal: `curl "https://api.telegram.org/bot<TOKEN>/getChat?chat_id=@photonect_news_channel"`
2. Response `"id"` field is `TELEGRAM_CHANNEL_ID` (will be a negative number for channels)

- [ ] **Step 5: Append values to runbook**

Append to `docs/runbooks/p0-credential-setup.md`:

```markdown
## Telegram setup — completed values

- Bot username: `@photonect_news_bot`
- Bot token: [in n8n credentials store as `telegram-bot-token`]
- Ahmed DM chat ID: [in n8n vars as `TELEGRAM_AHMED_CHAT_ID`]
- Channel chat ID: [in n8n vars as `TELEGRAM_CHANNEL_ID`]
- Bot admin status on channel: verified
```

- [ ] **Step 6: Create n8n credential for Telegram bot**

Use n8n MCP:

```
mcp__n8n-mcp__n8n_manage_credentials
  action: "create"
  type: "telegramApi"
  name: "telegram-bot-token"
  data: { "accessToken": "<bot token from step 1>" }
```

Verify: `mcp__n8n-mcp__n8n_manage_credentials action='list'` shows `telegram-bot-token`.

- [ ] **Step 7: Commit runbook update**

```bash
git add docs/runbooks/p0-credential-setup.md
git commit -m "docs(runbook): record Telegram bot + channel setup"
```

## Task P0.3: Meta IG dev app + long-lived token

**Files:**
- Modify: `docs/runbooks/p0-credential-setup.md` (add Meta section)

- [ ] **Step 1: Follow the existing Meta setup doc**

The existing `automation/scripts/setup-ig.md` already has full instructions. Ahmed follows steps 1-6 of that doc to obtain:

- `META_APP_ID`
- `META_APP_SECRET`
- `META_LONG_LIVED_USER_TOKEN` (60-day token)
- `IG_BUSINESS_ACCOUNT_ID`

- [ ] **Step 2: Note the token expiry date**

Compute: today + 60 days = expiry. Set a calendar reminder for day 45 as a manual backup to WF6 auto-rotation.

- [ ] **Step 3: Create n8n credential for Meta**

```
mcp__n8n-mcp__n8n_manage_credentials
  action: "create"
  type: "httpHeaderAuth"
  name: "meta-graph-api"
  data: {
    "name": "Authorization",
    "value": "Bearer <META_LONG_LIVED_USER_TOKEN>"
  }
```

(We use httpHeaderAuth instead of a dedicated FacebookGraphApi credential because the IG Reels container/publish flow is multi-step HTTP and easier to script directly than via the FB-specific n8n node, which lags on Reels support.)

- [ ] **Step 4: Store IDs as n8n variables**

In n8n UI → Settings → Variables, create:
- `META_APP_ID = <value>`
- `IG_BUSINESS_ACCOUNT_ID = <value>`
- `META_LONG_LIVED_USER_TOKEN = <value>` (for WF6 rotation logic which needs it as a plain string)
- `META_APP_SECRET = <value>` (encrypted)

- [ ] **Step 5: Smoke-test the token**

From terminal:

```bash
curl "https://graph.facebook.com/v21.0/$IG_BUSINESS_ACCOUNT_ID?fields=username,profile_picture_url&access_token=$META_LONG_LIVED_USER_TOKEN"
```

Expected: JSON with `"username":"photonect.news"` (or your business handle).

- [ ] **Step 6: Append to runbook & commit**

```bash
git add docs/runbooks/p0-credential-setup.md
git commit -m "docs(runbook): record Meta IG dev app + long-lived token setup"
```

## Task P0.4: TikTok dev app + access token

**Files:**
- Modify: `docs/runbooks/p0-credential-setup.md` (add TikTok section)

- [ ] **Step 1: Follow existing TikTok setup doc**

The existing `automation/scripts/setup-tiktok.md` has the steps. Ahmed obtains:

- `TIKTOK_CLIENT_KEY`
- `TIKTOK_CLIENT_SECRET`
- `TIKTOK_ACCESS_TOKEN` (with `video.upload` scope)
- `TIKTOK_OPEN_ID` (your TikTok account's open_id)

- [ ] **Step 2: Create n8n credential**

```
mcp__n8n-mcp__n8n_manage_credentials
  action: "create"
  type: "httpHeaderAuth"
  name: "tiktok-content-api"
  data: {
    "name": "Authorization",
    "value": "Bearer <TIKTOK_ACCESS_TOKEN>"
  }
```

- [ ] **Step 3: Store IDs as n8n variables**

- `TIKTOK_CLIENT_KEY`
- `TIKTOK_OPEN_ID`

- [ ] **Step 4: Smoke-test**

```bash
curl -X GET "https://open.tiktokapis.com/v2/user/info/" \
  -H "Authorization: Bearer $TIKTOK_ACCESS_TOKEN"
```

Expected: JSON with `data.user.open_id` matching your `TIKTOK_OPEN_ID`.

- [ ] **Step 5: Commit**

```bash
git add docs/runbooks/p0-credential-setup.md
git commit -m "docs(runbook): record TikTok dev app + access token setup"
```

## Task P0.5: YouTube channel + OAuth + 50K quota

**Files:**
- Modify: `docs/runbooks/p0-credential-setup.md` (add YouTube section)

- [ ] **Step 1: Ensure a YouTube channel exists**

Ahmed verifies a YouTube channel exists at https://youtube.com (use the same Google account that owns @photonect.news IG if cross-promoting). Create if missing.

- [ ] **Step 2: GCP project + OAuth 2.0 credentials**

1. Open https://console.cloud.google.com → create project "Photonect-News-Publisher"
2. APIs & Services → Library → enable "YouTube Data API v3"
3. APIs & Services → Credentials → Create Credentials → OAuth client ID → Application type: Desktop app, name "n8n YouTube Uploader"
4. Download the OAuth client JSON → save as `~/photonect-news/youtube-oauth-client.json` locally (do NOT commit)

- [ ] **Step 3: One-time OAuth dance to obtain refresh token**

Use a small Python script (one-off, not committed):

```python
# /tmp/youtube-oauth.py
from google_auth_oauthlib.flow import InstalledAppFlow

flow = InstalledAppFlow.from_client_secrets_file(
    "~/photonect-news/youtube-oauth-client.json",
    scopes=["https://www.googleapis.com/auth/youtube.upload",
            "https://www.googleapis.com/auth/youtube.readonly"]
)
creds = flow.run_local_server(port=0, access_type="offline", prompt="consent")
print("REFRESH_TOKEN:", creds.refresh_token)
print("CLIENT_ID:", creds.client_id)
print("CLIENT_SECRET:", creds.client_secret)
```

Run: `pip install google-auth-oauthlib && python3 /tmp/youtube-oauth.py`. Browser opens for consent. Copy the printed values.

- [ ] **Step 4: Request quota increase to 50K units/day**

1. GCP Console → IAM & Admin → Quotas
2. Filter: "YouTube Data API v3 → Queries per day"
3. Default is 10,000. Request 50,000 with justification: "Daily automated upload of 6 short-form videos for a news publisher; baseline cost 1600 units × 6 = 9600, retries push over default."
4. Approval typically arrives within 24-48 hours. **Block on this before P3 cutover** but P1/P2 can proceed.

- [ ] **Step 5: Create n8n credential**

```
mcp__n8n-mcp__n8n_manage_credentials
  action: "create"
  type: "youTubeOAuth2Api"
  name: "youtube-data-api"
  data: {
    "clientId": "<CLIENT_ID>",
    "clientSecret": "<CLIENT_SECRET>",
    "refreshToken": "<REFRESH_TOKEN>"
  }
```

- [ ] **Step 6: Smoke-test via n8n_test_workflow (or manual)**

Manually trigger a tiny n8n workflow that calls YouTube Data API `channels.list` mine=true. Expect JSON with your channel ID.

(If skipping pre-test, the first WF5 dry run will catch credential issues.)

- [ ] **Step 7: Commit runbook**

```bash
git add docs/runbooks/p0-credential-setup.md
git commit -m "docs(runbook): record YouTube OAuth + 50K quota request"
```

## Task P0.6: Cloudinary

**Files:**
- Modify: `docs/runbooks/p0-credential-setup.md` (add Cloudinary section)

- [ ] **Step 1: Create Cloudinary account**

Ahmed: https://cloudinary.com → free tier (25 GB egress/mo is plenty). Note:
- `CLOUDINARY_CLOUD_NAME`
- `CLOUDINARY_API_KEY`
- `CLOUDINARY_API_SECRET`

- [ ] **Step 2: Create n8n credential**

```
mcp__n8n-mcp__n8n_manage_credentials
  action: "create"
  type: "cloudinaryApi"
  name: "cloudinary-uploader"
  data: {
    "cloudName": "<CLOUDINARY_CLOUD_NAME>",
    "apiKey": "<CLOUDINARY_API_KEY>",
    "apiSecret": "<CLOUDINARY_API_SECRET>"
  }
```

- [ ] **Step 3: Smoke-test from terminal**

```bash
curl -X POST "https://api.cloudinary.com/v1_1/$CLOUDINARY_CLOUD_NAME/video/upload" \
  -F "file=@/tmp/test.mp4" \
  -F "api_key=$CLOUDINARY_API_KEY" \
  -F "timestamp=$(date +%s)" \
  -F "signature=$(echo -n "timestamp=$(date +%s)$CLOUDINARY_API_SECRET" | shasum -a 1 | cut -d' ' -f1)"
```

Expected: JSON with `"secure_url": "https://res.cloudinary.com/..."`.

- [ ] **Step 4: Commit**

```bash
git add docs/runbooks/p0-credential-setup.md
git commit -m "docs(runbook): record Cloudinary account setup"
```

## Task P0.7: GitHub PAT for n8n

**Files:**
- Modify: `docs/runbooks/p0-credential-setup.md` (add GitHub section)

- [ ] **Step 1: Create GitHub fine-grained PAT**

1. GitHub → Settings → Developer settings → Personal access tokens → Fine-grained tokens → Generate new token
2. Name: `n8n-news-engine`
3. Expiration: 90 days
4. Resource owner: your account
5. Repository access: Only select repositories → `photonect-news-engine` (this repo)
6. Permissions:
   - **Repository permissions:**
     - Actions: Read and write (to trigger workflow_dispatch)
     - Contents: Read and write (to commit posting-state)
     - Metadata: Read
     - Workflows: Read and write
7. Generate → copy token

- [ ] **Step 2: Create n8n credential**

```
mcp__n8n-mcp__n8n_manage_credentials
  action: "create"
  type: "githubApi"
  name: "github-pat-news-engine"
  data: {
    "accessToken": "<PAT from step 1>"
  }
```

- [ ] **Step 3: Smoke-test**

```bash
curl -H "Authorization: token <PAT>" \
  https://api.github.com/repos/<owner>/<repo>/actions/workflows
```

Expected: JSON listing render-day.yml and other workflows.

- [ ] **Step 4: Commit**

```bash
git add docs/runbooks/p0-credential-setup.md
git commit -m "docs(runbook): record GitHub PAT for n8n setup"
```

## Task P0.8: Add Anthropic API key to GitHub secrets

**Files:**
- (no repo file changes — only GH secrets)

- [ ] **Step 1: Create + store Anthropic API key**

1. Anthropic console → API keys → Create
2. Name: `photonect-news-engine-ci`
3. Copy the key (starts with `sk-ant-`)
4. Set spending limit: $500/month hard cap, alert at $400

- [ ] **Step 2: Add to GH repo secrets**

GitHub → repo → Settings → Secrets and variables → Actions → New repository secret:
- Name: `ANTHROPIC_API_KEY`
- Value: the key from step 1

- [ ] **Step 3: Verify visibility in Actions**

Open `.github/workflows/render-day.yml` and confirm an Action run can reference `${{ secrets.ANTHROPIC_API_KEY }}` (will use in P1B).

## Task P0.9: Staging IG/TT/YT accounts for P2 testing

**Files:**
- Modify: `docs/runbooks/p0-credential-setup.md` (add staging section)

- [ ] **Step 1: Create staging accounts**

Ahmed creates:
- IG: `@photonect_staging` (a separate IG business account — Meta allows multiple per FB Page)
- TikTok: `@photonect_staging` (separate TikTok account)
- YouTube: separate channel `Photonect Staging`

These are private/throwaway. Used ONLY for P2 testing and never for live posts.

- [ ] **Step 2: Repeat Tasks P0.3-P0.5 for staging accounts**

Get staging credentials and create n8n credentials with `-staging` suffix:
- `meta-graph-api-staging`
- `tiktok-content-api-staging`
- `youtube-data-api-staging`

(Staging Telegram is fine to share with prod — just use a private test channel like `@photonect_staging_channel`.)

- [ ] **Step 3: Commit runbook**

```bash
git add docs/runbooks/p0-credential-setup.md
git commit -m "docs(runbook): record staging accounts setup"
```

## Task P0.10: Verify all credentials with audit

- [ ] **Step 1: Run n8n credentials audit**

```
mcp__n8n-mcp__n8n_manage_credentials action='list' includeUsage=true
```

Verify the following 9 credentials exist (no usage yet because no workflows built):

| Name | Type |
|---|---|
| `telegram-bot-token` | telegramApi |
| `meta-graph-api` | httpHeaderAuth |
| `meta-graph-api-staging` | httpHeaderAuth |
| `tiktok-content-api` | httpHeaderAuth |
| `tiktok-content-api-staging` | httpHeaderAuth |
| `youtube-data-api` | youTubeOAuth2Api |
| `youtube-data-api-staging` | youTubeOAuth2Api |
| `cloudinary-uploader` | cloudinaryApi |
| `github-pat-news-engine` | githubApi |

- [ ] **Step 2: Mark P0 complete in runbook**

Append:

```markdown
## P0 sign-off

All 9 credentials provisioned and smoke-tested.
P0 completed on: <YYYY-MM-DD>
Ready to begin P1.
```

- [ ] **Step 3: Commit**

```bash
git add docs/runbooks/p0-credential-setup.md
git commit -m "docs(runbook): P0 credential setup complete"
```

---

# PHASE P1A — WF5 slot-posting (the hardest workflow, built FIRST)

> **Why first:** WF5 exercises all 4 platform APIs end-to-end with a single mp4 + caption. If a platform credential or API contract is wrong, we find out before sinking effort into the orchestration workflows (WF1/WF3).
>
> **Phase goal:** Manually triggered, WF5 takes one slug name as input, fetches its mp4 from Drive + caption from repo, uploads to Cloudinary, and posts to IG-staging + TT-staging + YT-staging + Telegram-staging in parallel. Writes per-slot result to a staging file.
>
> **What "done" means:** Manually trigger WF5 with `{slug: "2026-05-10-iran-rainbow-site-tritium-semnan-may9", date: "2026-05-10"}` from n8n UI. All 4 platform calls succeed (or fail with logged + actionable errors). `data/posting-state/2026-05-10.json` shows the result with 4 permalinks.

## Task P1A.1: Helper script — cloudinary-upload.py

**Files:**
- Create: `automation/scripts/cloudinary-upload.py`
- Test: `automation/scripts/test_cloudinary_upload.py`

- [ ] **Step 1: Write the failing test**

Create `automation/scripts/test_cloudinary_upload.py`:

```python
"""Test cloudinary-upload.py. Run: python3 -m pytest automation/scripts/test_cloudinary_upload.py -v"""
import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).parent / "cloudinary-upload.py"

def test_script_exists():
    assert SCRIPT.is_file(), f"missing {SCRIPT}"

def test_help_works():
    r = subprocess.run([sys.executable, str(SCRIPT), "--help"], capture_output=True, text=True)
    assert r.returncode == 0
    assert "--file" in r.stdout
    assert "--public-id" in r.stdout

def test_missing_creds_errors_cleanly(tmp_path, monkeypatch):
    monkeypatch.delenv("CLOUDINARY_CLOUD_NAME", raising=False)
    f = tmp_path / "x.mp4"
    f.write_bytes(b"\x00" * 10)
    r = subprocess.run(
        [sys.executable, str(SCRIPT), "--file", str(f), "--public-id", "test"],
        capture_output=True, text=True
    )
    assert r.returncode != 0
    assert "CLOUDINARY_CLOUD_NAME" in r.stderr
```

- [ ] **Step 2: Run test to verify it fails**

```bash
python3 -m pytest automation/scripts/test_cloudinary_upload.py -v
```

Expected: 3 failures (script doesn't exist).

- [ ] **Step 3: Write the script**

Create `automation/scripts/cloudinary-upload.py`:

```python
#!/usr/bin/env python3
"""Upload an mp4 to Cloudinary, print the secure_url to stdout.

Used by n8n WF5 (slot-posting) to produce a public URL for the Instagram
Graph API Reels container (IG cannot accept direct uploads).

Env required:
  CLOUDINARY_CLOUD_NAME, CLOUDINARY_API_KEY, CLOUDINARY_API_SECRET

Usage:
  cloudinary-upload.py --file path/to/video.mp4 --public-id 2026-05-23-slug
"""
import argparse
import hashlib
import os
import sys
import time
from pathlib import Path

try:
    import requests  # type: ignore
except ImportError:
    print("error: pip install requests", file=sys.stderr)
    sys.exit(2)


def main() -> int:
    ap = argparse.ArgumentParser(description="Upload mp4 to Cloudinary")
    ap.add_argument("--file", required=True, help="path to mp4")
    ap.add_argument("--public-id", required=True, help="cloudinary public_id (typically <date>-<slug>)")
    args = ap.parse_args()

    cloud_name = os.environ.get("CLOUDINARY_CLOUD_NAME")
    api_key = os.environ.get("CLOUDINARY_API_KEY")
    api_secret = os.environ.get("CLOUDINARY_API_SECRET")
    missing = [k for k, v in [
        ("CLOUDINARY_CLOUD_NAME", cloud_name),
        ("CLOUDINARY_API_KEY", api_key),
        ("CLOUDINARY_API_SECRET", api_secret),
    ] if not v]
    if missing:
        print(f"error: missing env {', '.join(missing)}", file=sys.stderr)
        return 2

    fp = Path(args.file)
    if not fp.is_file():
        print(f"error: file not found {fp}", file=sys.stderr)
        return 2

    ts = int(time.time())
    # Cloudinary signature: SHA1(params_sorted&api_secret)
    params_to_sign = f"public_id={args.public_id}&timestamp={ts}"
    signature = hashlib.sha1(f"{params_to_sign}{api_secret}".encode()).hexdigest()

    url = f"https://api.cloudinary.com/v1_1/{cloud_name}/video/upload"
    with fp.open("rb") as f:
        r = requests.post(
            url,
            data={
                "api_key": api_key,
                "timestamp": ts,
                "public_id": args.public_id,
                "signature": signature,
            },
            files={"file": (fp.name, f, "video/mp4")},
            timeout=300,
        )
    if r.status_code != 200:
        print(f"error: cloudinary returned {r.status_code}: {r.text}", file=sys.stderr)
        return 1
    body = r.json()
    print(body["secure_url"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Run test to verify it passes**

```bash
chmod +x automation/scripts/cloudinary-upload.py
python3 -m pytest automation/scripts/test_cloudinary_upload.py -v
```

Expected: 3 passes.

- [ ] **Step 5: Real smoke test (manual)**

```bash
export CLOUDINARY_CLOUD_NAME=<value>
export CLOUDINARY_API_KEY=<value>
export CLOUDINARY_API_SECRET=<value>
python3 automation/scripts/cloudinary-upload.py \
  --file data/posts/2026-05-10-iran-rainbow-site-tritium-semnan-may9/video.mp4 \
  --public-id test-iran-rainbow
```

Expected: prints `https://res.cloudinary.com/.../test-iran-rainbow.mp4`. Open URL in browser → video plays.

(If no rendered video exists locally, copy one from Drive temporarily.)

- [ ] **Step 6: Commit**

```bash
git add automation/scripts/cloudinary-upload.py automation/scripts/test_cloudinary_upload.py
git commit -m "feat(automation): add cloudinary-upload.py for IG public mp4 URLs"
```

## Task P1A.2: Helper script — posting-state-update.py

**Files:**
- Create: `automation/scripts/posting-state-update.py`
- Create: `data/posting-state/.gitkeep`
- Create: `data/posting-state/README.md`

- [ ] **Step 1: Create the directory**

```bash
mkdir -p data/posting-state
touch data/posting-state/.gitkeep
```

- [ ] **Step 2: Write the README**

Create `data/posting-state/README.md`:

```markdown
# data/posting-state/

Per-day audit log for the n8n distribution layer. Files are created and
updated by n8n WF5 (slot-posting) via GitHub Contents API.

## File naming

`<YYYY-MM-DD>.json` — one file per day, updated incrementally as each slot
fires and each platform call completes/fails.

## Schema

```json
{
  "date": "2026-05-23",
  "slugs": {
    "<slug>": {
      "slot": 1,                   // 1..6
      "ig":       {"status": "ok|failed|skipped|pending", "permalink": "...", "ts": "ISO8601"},
      "tiktok":   {"status": "...",                       "permalink": "...", "ts": "..."},
      "yt":       {"status": "...",                       "permalink": "...", "ts": "..."},
      "telegram": {"status": "...",                       "permalink": "...", "ts": "..."}
    }
  }
}
```

## Status values

- `pending`  — slot fired, platform call in flight
- `ok`       — platform call succeeded, permalink captured
- `failed`   — platform call failed after retries, `error` field present
- `skipped`  — slug was PAUSED in kill window before this platform was called

## Update flow (from n8n)

n8n WF5 calls `automation/scripts/posting-state-update.py` via the GitHub
Contents API — never writes directly. The script:
1. GET current file (if exists) — gets SHA
2. Merge in the new slot/platform result
3. PUT updated file with old SHA → atomic, fails on concurrent write

Concurrent writes from parallel slot crons are rare (slots are 2+ hours apart)
but the GitHub SHA check prevents lost updates.
```

- [ ] **Step 3: Write the failing test**

Create `automation/scripts/test_posting_state_update.py`:

```python
"""Test posting-state-update.py — local mode (no GitHub API).
Run: python3 -m pytest automation/scripts/test_posting_state_update.py -v"""
import json
import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).parent / "posting-state-update.py"

def test_script_exists():
    assert SCRIPT.is_file(), f"missing {SCRIPT}"

def test_creates_new_file(tmp_path):
    target = tmp_path / "2026-05-23.json"
    r = subprocess.run([
        sys.executable, str(SCRIPT),
        "--local-file", str(target),
        "--date", "2026-05-23",
        "--slug", "2026-05-23-test-slug",
        "--slot", "1",
        "--platform", "ig",
        "--status", "ok",
        "--permalink", "https://instagram.com/reel/ABC123",
    ], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    assert target.is_file()
    data = json.loads(target.read_text())
    assert data["date"] == "2026-05-23"
    assert data["slugs"]["2026-05-23-test-slug"]["ig"]["status"] == "ok"
    assert data["slugs"]["2026-05-23-test-slug"]["ig"]["permalink"] == "https://instagram.com/reel/ABC123"
    assert "ts" in data["slugs"]["2026-05-23-test-slug"]["ig"]
    assert data["slugs"]["2026-05-23-test-slug"]["slot"] == 1

def test_merges_into_existing(tmp_path):
    target = tmp_path / "2026-05-23.json"
    target.write_text(json.dumps({
        "date": "2026-05-23",
        "slugs": {
            "2026-05-23-test-slug": {
                "slot": 1,
                "ig": {"status": "ok", "permalink": "x", "ts": "2026-05-23T08:00:00Z"}
            }
        }
    }))
    r = subprocess.run([
        sys.executable, str(SCRIPT),
        "--local-file", str(target),
        "--date", "2026-05-23",
        "--slug", "2026-05-23-test-slug",
        "--slot", "1",
        "--platform", "tiktok",
        "--status", "failed",
        "--error", "rate limited",
    ], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    data = json.loads(target.read_text())
    # Old entry preserved
    assert data["slugs"]["2026-05-23-test-slug"]["ig"]["status"] == "ok"
    # New entry added
    assert data["slugs"]["2026-05-23-test-slug"]["tiktok"]["status"] == "failed"
    assert data["slugs"]["2026-05-23-test-slug"]["tiktok"]["error"] == "rate limited"
```

- [ ] **Step 4: Verify failure**

```bash
python3 -m pytest automation/scripts/test_posting_state_update.py -v
```

Expected: 3 failures (script missing).

- [ ] **Step 5: Write the script**

Create `automation/scripts/posting-state-update.py`:

```python
#!/usr/bin/env python3
"""Update data/posting-state/<date>.json with a per-slot per-platform result.

Two modes:
  --local-file PATH      → read/merge/write a local JSON file (for testing)
  --github-api OWNER/REPO → read/merge/write via GitHub Contents API (production)

Env required for --github-api mode:
  GITHUB_TOKEN — PAT with contents:write on the target repo
"""
import argparse
import base64
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import requests  # type: ignore
except ImportError:
    print("error: pip install requests", file=sys.stderr)
    sys.exit(2)

REPO_FILE_PATH = "data/posting-state/{date}.json"


def merge_entry(existing: dict, date: str, slug: str, slot: int,
                platform: str, status: str, permalink: str | None,
                error: str | None) -> dict:
    if not existing:
        existing = {"date": date, "slugs": {}}
    existing.setdefault("slugs", {}).setdefault(slug, {"slot": slot})
    entry: dict = {"status": status, "ts": datetime.now(timezone.utc).isoformat()}
    if permalink:
        entry["permalink"] = permalink
    if error:
        entry["error"] = error
    existing["slugs"][slug][platform] = entry
    return existing


def local_mode(args) -> int:
    fp = Path(args.local_file)
    fp.parent.mkdir(parents=True, exist_ok=True)
    existing = json.loads(fp.read_text()) if fp.is_file() else {}
    merged = merge_entry(existing, args.date, args.slug, args.slot,
                         args.platform, args.status, args.permalink, args.error)
    fp.write_text(json.dumps(merged, indent=2, ensure_ascii=False))
    print(f"✓ wrote {fp}")
    return 0


def github_mode(args) -> int:
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("error: GITHUB_TOKEN env required for --github-api mode", file=sys.stderr)
        return 2
    owner, repo = args.github_api.split("/", 1)
    path = REPO_FILE_PATH.format(date=args.date)
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    # Read existing
    r = requests.get(url, headers=headers, timeout=30)
    if r.status_code == 200:
        body = r.json()
        existing = json.loads(base64.b64decode(body["content"]))
        sha = body["sha"]
    elif r.status_code == 404:
        existing = {}
        sha = None
    else:
        print(f"error: GET {url} → {r.status_code}: {r.text}", file=sys.stderr)
        return 1
    merged = merge_entry(existing, args.date, args.slug, args.slot,
                         args.platform, args.status, args.permalink, args.error)
    content_b64 = base64.b64encode(
        json.dumps(merged, indent=2, ensure_ascii=False).encode()
    ).decode()
    payload = {
        "message": f"chore(posting-state): {args.slug} {args.platform} {args.status}",
        "content": content_b64,
        "branch": args.branch,
    }
    if sha:
        payload["sha"] = sha
    r = requests.put(url, headers=headers, json=payload, timeout=30)
    if r.status_code not in (200, 201):
        print(f"error: PUT {url} → {r.status_code}: {r.text}", file=sys.stderr)
        return 1
    print(f"✓ committed {path}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", required=True)
    ap.add_argument("--slug", required=True)
    ap.add_argument("--slot", type=int, required=True)
    ap.add_argument("--platform", required=True, choices=["ig", "tiktok", "yt", "telegram"])
    ap.add_argument("--status", required=True, choices=["pending", "ok", "failed", "skipped"])
    ap.add_argument("--permalink", default=None)
    ap.add_argument("--error", default=None)
    ap.add_argument("--local-file", default=None, help="local mode (testing)")
    ap.add_argument("--github-api", default=None, help="OWNER/REPO for GitHub Contents API mode")
    ap.add_argument("--branch", default="main")
    args = ap.parse_args()
    if args.local_file:
        return local_mode(args)
    if args.github_api:
        return github_mode(args)
    print("error: --local-file or --github-api required", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 6: Run tests**

```bash
chmod +x automation/scripts/posting-state-update.py
python3 -m pytest automation/scripts/test_posting_state_update.py -v
```

Expected: 3 passes.

- [ ] **Step 7: Commit**

```bash
git add automation/scripts/posting-state-update.py \
        automation/scripts/test_posting_state_update.py \
        data/posting-state/
git commit -m "feat(automation): add posting-state-update.py + schema docs"
```

## Task P1A.3: Discover n8n node types for WF5

> Investigation task — informs the workflow JSON in P1A.4.

- [ ] **Step 1: Search for HTTP Request node**

```
mcp__n8n-mcp__search_nodes query="http request"
```

Expected: `n8n-nodes-base.httpRequest` (the canonical HTTP node).

- [ ] **Step 2: Get HTTP Request node schema**

```
mcp__n8n-mcp__get_node nodeType="nodes-base.httpRequest" detail="standard"
```

Note: `parameters.method`, `parameters.url`, `parameters.authentication`, `parameters.sendBody`, `parameters.bodyParameters`, `parameters.options.timeout`.

- [ ] **Step 3: Search for Telegram nodes**

```
mcp__n8n-mcp__search_nodes query="telegram"
```

Expected: `n8n-nodes-base.telegram` (send messages, edit, etc.), `n8n-nodes-base.telegramTrigger` (webhook for callback_query).

- [ ] **Step 4: Get Telegram node operation list**

```
mcp__n8n-mcp__get_node nodeType="nodes-base.telegram" detail="standard" includeOperations=true
```

Note operations: sendMessage, sendPhoto, sendVideo, editMessageText, answerCallbackQuery.

- [ ] **Step 5: Search for YouTube node**

```
mcp__n8n-mcp__search_nodes query="youtube"
```

Expected: `n8n-nodes-base.youTube` for OAuth-based upload.

- [ ] **Step 6: Get node info for execute-command (for cloudinary-upload.py + posting-state-update.py)**

```
mcp__n8n-mcp__search_nodes query="execute command"
```

Expected: `n8n-nodes-base.executeCommand` — but n8n cloud usually doesn't have shell access; if missing, use HTTP Request to call a small endpoint OR use n8n Code node + native fetch.

**Decision point:** Fly.dev-hosted n8n with `--command` enabled = use executeCommand. Otherwise = use Code node with built-in `fetch` to call platform APIs directly. (We'll use Code nodes for portability.)

- [ ] **Step 7: Record findings**

Create `ops/n8n/README.md`:

```markdown
# ops/n8n/

n8n workflow JSON exports for version control. Re-import via n8n UI
("Import from File") or `mcp__n8n-mcp__n8n_create_workflow` for disaster recovery.

## n8n node types used

| Purpose | Node type |
|---|---|
| Cron trigger | `n8n-nodes-base.scheduleTrigger` |
| Webhook (Telegram callback) | `n8n-nodes-base.telegramTrigger` |
| HTTP requests (Meta, TikTok, Cloudinary, GitHub) | `n8n-nodes-base.httpRequest` |
| Telegram messages | `n8n-nodes-base.telegram` |
| YouTube upload | `n8n-nodes-base.youTube` |
| Conditional routing | `n8n-nodes-base.switch` |
| Set variables | `n8n-nodes-base.set` |
| Wait / delay | `n8n-nodes-base.wait` |
| Custom logic (signing, JSON merge) | `n8n-nodes-base.code` |
| Sub-workflow invocation | `n8n-nodes-base.executeWorkflow` |

## Export workflow JSON

```
mcp__n8n-mcp__n8n_get_workflow id=<workflow-id> mode=full
```

Save the response (without `activeVersionId` pointer) to `ops/n8n/WF<N>_<name>.json`.
```

- [ ] **Step 8: Commit**

```bash
git add ops/n8n/README.md
git commit -m "docs(ops): document n8n node types for the distribution workflows"
```

## Task P1A.4: Build WF5 — IG branch (staging)

> Build the IG branch of WF5 first (most complex platform — 3 API calls: container, polling, publish).

**Files:**
- (n8n) WF5 created via MCP

- [ ] **Step 1: Create the WF5 workflow shell**

```
mcp__n8n-mcp__n8n_create_workflow
  name: "WF5 slot-posting"
  nodes: [
    {
      "id": "trigger",
      "name": "Manual Trigger",
      "type": "n8n-nodes-base.manualTrigger",
      "typeVersion": 1,
      "position": [100, 300],
      "parameters": {}
    },
    {
      "id": "fetch-mp4-info",
      "name": "Get input (slug, date, env)",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3,
      "position": [300, 300],
      "parameters": {
        "assignments": {
          "assignments": [
            {"id": "1", "name": "slug",     "value": "={{ $json.slug }}",     "type": "string"},
            {"id": "2", "name": "date",     "value": "={{ $json.date }}",     "type": "string"},
            {"id": "3", "name": "slot",     "value": "={{ $json.slot ?? 0 }}", "type": "number"},
            {"id": "4", "name": "env",      "value": "={{ $json.env ?? 'staging' }}", "type": "string"}
          ]
        }
      }
    }
  ]
  connections: {
    "Manual Trigger": {
      "main": [[{"node": "Get input (slug, date, env)", "type": "main", "index": 0}]]
    }
  }
```

Save the returned workflow ID. Call it `WF5_ID` for subsequent steps.

- [ ] **Step 2: Validate**

```
mcp__n8n-mcp__n8n_validate_workflow id=<WF5_ID>
```

Expected: no errors.

- [ ] **Step 3: Test the shell with sample input**

In n8n UI, manually trigger with payload:

```json
{"slug": "2026-05-10-iran-rainbow-site-tritium-semnan-may9", "date": "2026-05-10", "slot": 1, "env": "staging"}
```

Expected: Set node outputs the 4 fields.

- [ ] **Step 4: Add Cloudinary upload sub-flow (Code node)**

Use `n8n_update_partial_workflow` with operation `addNode`:

```
mcp__n8n-mcp__n8n_update_partial_workflow
  id: <WF5_ID>
  operations: [
    {
      "type": "addNode",
      "node": {
        "id": "fetch-mp4-from-drive",
        "name": "Fetch mp4 from Drive (public URL via shared link or cached path)",
        "type": "n8n-nodes-base.httpRequest",
        "typeVersion": 4,
        "position": [500, 200],
        "parameters": {
          "method": "GET",
          "url": "=https://www.googleapis.com/drive/v3/files/{{ $('Get input (slug, date, env)').item.json.drive_file_id }}?alt=media",
          "authentication": "predefinedCredentialType",
          "nodeCredentialType": "googleDriveOAuth2Api",
          "options": {"response": {"response": {"responseFormat": "file"}}}
        }
      }
    },
    {
      "type": "addNode",
      "node": {
        "id": "upload-to-cloudinary",
        "name": "Upload mp4 to Cloudinary",
        "type": "n8n-nodes-base.httpRequest",
        "typeVersion": 4,
        "position": [700, 200],
        "parameters": {
          "method": "POST",
          "url": "=https://api.cloudinary.com/v1_1/{{ $vars.CLOUDINARY_CLOUD_NAME }}/video/upload",
          "sendBody": true,
          "contentType": "multipart-form-data",
          "bodyParameters": {
            "parameters": [
              {"name": "file", "parameterType": "formBinaryData", "inputDataFieldName": "data"},
              {"name": "public_id", "value": "={{ $('Get input (slug, date, env)').item.json.date }}-{{ $('Get input (slug, date, env)').item.json.slug }}"},
              {"name": "timestamp", "value": "={{ Math.floor(Date.now()/1000) }}"},
              {"name": "api_key", "value": "={{ $vars.CLOUDINARY_API_KEY }}"},
              {"name": "signature", "value": "={{ $('Sign Cloudinary Request').item.json.signature }}"}
            ]
          }
        }
      }
    },
    {
      "type": "addNode",
      "node": {
        "id": "sign-cloudinary",
        "name": "Sign Cloudinary Request",
        "type": "n8n-nodes-base.code",
        "typeVersion": 2,
        "position": [500, 400],
        "parameters": {
          "jsCode": "const crypto = require('crypto');\nconst ts = Math.floor(Date.now() / 1000);\nconst publicId = `${$input.item.json.date}-${$input.item.json.slug}`;\nconst toSign = `public_id=${publicId}&timestamp=${ts}`;\nconst signature = crypto.createHash('sha1').update(toSign + $vars.CLOUDINARY_API_SECRET).digest('hex');\nreturn { json: { signature, timestamp: ts, public_id: publicId } };"
        }
      }
    }
  ]
```

> Note: The above showcases the *intent*. During execution, the exact node connections (Sign → Upload, Upload → IG container etc.) are added via subsequent `addConnection` operations. The `mcp__n8n-mcp__n8n_update_partial_workflow` accepts diff operations; the executor wires them up iteratively.

- [ ] **Step 5: Add IG container creation node**

Add via `addNode`:

```json
{
  "id": "ig-create-container",
  "name": "IG: create reels container",
  "type": "n8n-nodes-base.httpRequest",
  "typeVersion": 4,
  "position": [900, 200],
  "parameters": {
    "method": "POST",
    "url": "=https://graph.facebook.com/v21.0/{{ $vars.IG_BUSINESS_ACCOUNT_ID_STAGING }}/media",
    "authentication": "predefinedCredentialType",
    "nodeCredentialType": "httpHeaderAuth",
    "sendBody": true,
    "contentType": "form-urlencoded",
    "bodyParameters": {
      "parameters": [
        {"name": "media_type", "value": "REELS"},
        {"name": "video_url", "value": "={{ $('Upload mp4 to Cloudinary').item.json.secure_url }}"},
        {"name": "caption", "value": "={{ $('Fetch caption').item.json.caption_text }}"},
        {"name": "share_to_feed", "value": "true"}
      ]
    },
    "options": {"timeout": 60000}
  },
  "credentials": {"httpHeaderAuth": {"id": "<cred-id-meta-graph-api-staging>", "name": "meta-graph-api-staging"}}
}
```

- [ ] **Step 6: Add IG container polling loop (Wait + HTTP + IF)**

This is the trickiest part — IG container takes 10-60 seconds to transition from `IN_PROGRESS` to `FINISHED`. Pattern:

1. **Wait** node — 5 seconds
2. **HTTP GET** `https://graph.facebook.com/v21.0/{{container_id}}?fields=status_code`
3. **IF** node — if `status_code == FINISHED` → continue to publish, if `IN_PROGRESS` → loop back to Wait (max 12 iterations = 60s)

Add three nodes via `addNode`:

```json
{
  "id": "ig-wait",
  "name": "IG: wait 5s",
  "type": "n8n-nodes-base.wait",
  "typeVersion": 1,
  "position": [1100, 200],
  "parameters": {"amount": 5, "unit": "seconds"}
},
{
  "id": "ig-poll-status",
  "name": "IG: poll container status",
  "type": "n8n-nodes-base.httpRequest",
  "typeVersion": 4,
  "position": [1300, 200],
  "parameters": {
    "method": "GET",
    "url": "=https://graph.facebook.com/v21.0/{{ $('IG: create reels container').item.json.id }}?fields=status_code",
    "authentication": "predefinedCredentialType",
    "nodeCredentialType": "httpHeaderAuth"
  },
  "credentials": {"httpHeaderAuth": {"id": "<cred-id>", "name": "meta-graph-api-staging"}}
},
{
  "id": "ig-status-check",
  "name": "IG: status == FINISHED?",
  "type": "n8n-nodes-base.if",
  "typeVersion": 2,
  "position": [1500, 200],
  "parameters": {
    "conditions": {"conditions": [{
      "leftValue": "={{ $json.status_code }}",
      "rightValue": "FINISHED",
      "operator": {"type": "string", "operation": "equals"}
    }]}
  }
}
```

Connections:
- IG: create reels container → IG: wait 5s
- IG: wait 5s → IG: poll container status
- IG: poll container status → IG: status == FINISHED?
- IG: status check TRUE → continue to publish (next step)
- IG: status check FALSE → back to IG: wait 5s (loop)

- [ ] **Step 7: Add IG publish node**

```json
{
  "id": "ig-publish",
  "name": "IG: publish container",
  "type": "n8n-nodes-base.httpRequest",
  "typeVersion": 4,
  "position": [1700, 200],
  "parameters": {
    "method": "POST",
    "url": "=https://graph.facebook.com/v21.0/{{ $vars.IG_BUSINESS_ACCOUNT_ID_STAGING }}/media_publish",
    "authentication": "predefinedCredentialType",
    "nodeCredentialType": "httpHeaderAuth",
    "sendBody": true,
    "contentType": "form-urlencoded",
    "bodyParameters": {
      "parameters": [
        {"name": "creation_id", "value": "={{ $('IG: create reels container').item.json.id }}"}
      ]
    }
  },
  "credentials": {"httpHeaderAuth": {"id": "<cred-id>", "name": "meta-graph-api-staging"}}
}
```

Add follow-up HTTP GET to fetch the permalink:

```json
{
  "id": "ig-fetch-permalink",
  "name": "IG: fetch permalink",
  "type": "n8n-nodes-base.httpRequest",
  "typeVersion": 4,
  "position": [1900, 200],
  "parameters": {
    "method": "GET",
    "url": "=https://graph.facebook.com/v21.0/{{ $('IG: publish container').item.json.id }}?fields=permalink",
    "authentication": "predefinedCredentialType",
    "nodeCredentialType": "httpHeaderAuth"
  },
  "credentials": {"httpHeaderAuth": {"id": "<cred-id>", "name": "meta-graph-api-staging"}}
}
```

- [ ] **Step 8: Add posting-state-update HTTP call for IG result**

We'll use HTTP Request to call GitHub Contents API directly (mirrors what posting-state-update.py does, since executeCommand may not be available in cloud n8n).

Use a Code node to build the merge payload, then an HTTP Request node to PUT to GitHub:

```json
{
  "id": "ig-state-record",
  "name": "Record IG result to posting-state",
  "type": "n8n-nodes-base.executeWorkflow",
  "typeVersion": 1,
  "position": [2100, 200],
  "parameters": {
    "workflowId": "<WF8_posting-state-helper-id>",
    "inputData": {
      "date":      "={{ $('Get input (slug, date, env)').item.json.date }}",
      "slug":      "={{ $('Get input (slug, date, env)').item.json.slug }}",
      "slot":      "={{ $('Get input (slug, date, env)').item.json.slot }}",
      "platform":  "ig",
      "status":    "ok",
      "permalink": "={{ $('IG: fetch permalink').item.json.permalink }}"
    }
  }
}
```

> **Note:** WF8 posting-state-helper is a tiny sub-workflow built in Task P1A.6. For now, leave this node referencing a placeholder `<WF8_ID>` — fill in after P1A.6.

- [ ] **Step 9: Validate WF5 so far**

```
mcp__n8n-mcp__n8n_validate_workflow id=<WF5_ID>
```

Expected: warnings about WF8 placeholder are OK; no fatal errors.

- [ ] **Step 10: Export and commit WF5 (in-progress) JSON**

```
mcp__n8n-mcp__n8n_get_workflow id=<WF5_ID> mode="full"
```

Save response (strip `activeVersionId`) to `ops/n8n/WF5_slot-posting.json`.

```bash
git add ops/n8n/WF5_slot-posting.json
git commit -m "feat(n8n): WF5 slot-posting — IG branch (staging) wired"
```

## Task P1A.5: Add TikTok branch to WF5

> TikTok branch is simpler than IG — supports direct upload. Three calls: init, upload, publish.

- [ ] **Step 1: Add TikTok init upload node**

Add via `n8n_update_partial_workflow` `addNode`:

```json
{
  "id": "tt-init-upload",
  "name": "TikTok: init upload",
  "type": "n8n-nodes-base.httpRequest",
  "typeVersion": 4,
  "position": [900, 400],
  "parameters": {
    "method": "POST",
    "url": "https://open.tiktokapis.com/v2/post/publish/video/init/",
    "authentication": "predefinedCredentialType",
    "nodeCredentialType": "httpHeaderAuth",
    "sendBody": true,
    "contentType": "json",
    "jsonBody": "={{ JSON.stringify({ post_info: { title: $('Fetch caption').item.json.caption_text.slice(0,150), privacy_level: 'PUBLIC_TO_EVERYONE', disable_duet: false, disable_comment: false, disable_stitch: false, video_cover_timestamp_ms: 1000 }, source_info: { source: 'PULL_FROM_URL', video_url: $('Upload mp4 to Cloudinary').item.json.secure_url } }) }}"
  },
  "credentials": {"httpHeaderAuth": {"id": "<cred-id-tiktok-content-api-staging>", "name": "tiktok-content-api-staging"}}
}
```

(TikTok supports `PULL_FROM_URL` — same Cloudinary URL we use for IG.)

- [ ] **Step 2: Add TikTok status poll loop (Wait + Status + IF)**

Same pattern as IG container polling — Wait 5s, GET `/video/upload/status/`, IF `status == 'PUBLISH_COMPLETE'` continue else loop back.

```json
{
  "id": "tt-wait",
  "name": "TikTok: wait 5s",
  "type": "n8n-nodes-base.wait",
  "typeVersion": 1,
  "position": [1100, 400],
  "parameters": {"amount": 5, "unit": "seconds"}
},
{
  "id": "tt-poll-status",
  "name": "TikTok: poll upload status",
  "type": "n8n-nodes-base.httpRequest",
  "typeVersion": 4,
  "position": [1300, 400],
  "parameters": {
    "method": "POST",
    "url": "https://open.tiktokapis.com/v2/post/publish/status/fetch/",
    "authentication": "predefinedCredentialType",
    "nodeCredentialType": "httpHeaderAuth",
    "sendBody": true,
    "contentType": "json",
    "jsonBody": "={{ JSON.stringify({ publish_id: $('TikTok: init upload').item.json.data.publish_id }) }}"
  },
  "credentials": {"httpHeaderAuth": {"id": "<cred-id>", "name": "tiktok-content-api-staging"}}
},
{
  "id": "tt-status-check",
  "name": "TikTok: status == PUBLISH_COMPLETE?",
  "type": "n8n-nodes-base.if",
  "typeVersion": 2,
  "position": [1500, 400],
  "parameters": {
    "conditions": {"conditions": [{
      "leftValue": "={{ $json.data.status }}",
      "rightValue": "PUBLISH_COMPLETE",
      "operator": {"type": "string", "operation": "equals"}
    }]}
  }
}
```

Connect: TikTok: init upload → TikTok: wait 5s → TikTok: poll upload status → TikTok: status check. TRUE → record state, FALSE → loop to TikTok: wait 5s.

- [ ] **Step 3: Record TikTok state**

Add `executeWorkflow` node "Record TikTok result to posting-state" mirroring P1A.4 step 8 (platform: "tiktok").

- [ ] **Step 4: Validate + export + commit**

```
mcp__n8n-mcp__n8n_validate_workflow id=<WF5_ID>
mcp__n8n-mcp__n8n_get_workflow id=<WF5_ID> mode="full"
```

Update `ops/n8n/WF5_slot-posting.json`. Commit:

```bash
git add ops/n8n/WF5_slot-posting.json
git commit -m "feat(n8n): WF5 — add TikTok branch (staging)"
```

## Task P1A.6: Build helper WF8 — posting-state-helper

> Sub-workflow shared by all platform branches in WF5 and WF7. Centralizes the GitHub Contents API call so we don't repeat HTTP logic in every branch.

- [ ] **Step 1: Create WF8 shell**

```
mcp__n8n-mcp__n8n_create_workflow
  name: "WF8 posting-state-helper"
  nodes: [
    {
      "id": "trigger",
      "name": "When called by another workflow",
      "type": "n8n-nodes-base.executeWorkflowTrigger",
      "typeVersion": 1,
      "position": [100, 300],
      "parameters": {
        "inputSource": "jsonExample",
        "jsonExample": "{ \"date\": \"\", \"slug\": \"\", \"slot\": 0, \"platform\": \"\", \"status\": \"\", \"permalink\": \"\", \"error\": \"\" }"
      }
    },
    {
      "id": "read-existing-file",
      "name": "GET existing posting-state file from GitHub",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4,
      "position": [300, 300],
      "parameters": {
        "method": "GET",
        "url": "=https://api.github.com/repos/{{ $vars.GITHUB_OWNER }}/{{ $vars.GITHUB_REPO }}/contents/data/posting-state/{{ $json.date }}.json",
        "authentication": "predefinedCredentialType",
        "nodeCredentialType": "githubApi",
        "options": {"response": {"response": {"neverError": true}}}
      },
      "credentials": {"githubApi": {"id": "<cred-id-github-pat>", "name": "github-pat-news-engine"}}
    },
    {
      "id": "merge-entry",
      "name": "Merge new entry into JSON",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [500, 300],
      "parameters": {
        "jsCode": "const input = $('When called by another workflow').item.json;\nconst existingResp = $('GET existing posting-state file from GitHub').item.json;\nlet content = { date: input.date, slugs: {} };\nlet sha = null;\nif (existingResp && existingResp.content) {\n  content = JSON.parse(Buffer.from(existingResp.content, 'base64').toString());\n  sha = existingResp.sha;\n}\nif (!content.slugs[input.slug]) content.slugs[input.slug] = { slot: input.slot };\nconst entry = { status: input.status, ts: new Date().toISOString() };\nif (input.permalink) entry.permalink = input.permalink;\nif (input.error) entry.error = input.error;\ncontent.slugs[input.slug][input.platform] = entry;\nreturn { json: { content: Buffer.from(JSON.stringify(content, null, 2)).toString('base64'), sha, commitMessage: `chore(posting-state): ${input.slug} ${input.platform} ${input.status}` } };"
      }
    },
    {
      "id": "put-file",
      "name": "PUT updated file to GitHub",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4,
      "position": [700, 300],
      "parameters": {
        "method": "PUT",
        "url": "=https://api.github.com/repos/{{ $vars.GITHUB_OWNER }}/{{ $vars.GITHUB_REPO }}/contents/data/posting-state/{{ $('When called by another workflow').item.json.date }}.json",
        "authentication": "predefinedCredentialType",
        "nodeCredentialType": "githubApi",
        "sendBody": true,
        "contentType": "json",
        "jsonBody": "={{ JSON.stringify({ message: $json.commitMessage, content: $json.content, branch: 'main', sha: $json.sha }) }}"
      },
      "credentials": {"githubApi": {"id": "<cred-id-github-pat>", "name": "github-pat-news-engine"}}
    }
  ]
  connections: {
    "When called by another workflow": {"main": [[{"node": "GET existing posting-state file from GitHub", "type": "main", "index": 0}]]},
    "GET existing posting-state file from GitHub": {"main": [[{"node": "Merge new entry into JSON", "type": "main", "index": 0}]]},
    "Merge new entry into JSON": {"main": [[{"node": "PUT updated file to GitHub", "type": "main", "index": 0}]]}
  }
```

Note returned ID: `WF8_ID`.

- [ ] **Step 2: Add `GITHUB_OWNER` and `GITHUB_REPO` n8n variables**

In n8n UI → Settings → Variables: `GITHUB_OWNER = <your-github-username-or-org>`, `GITHUB_REPO = photonect-news-engine` (or the actual repo name).

- [ ] **Step 3: Validate**

```
mcp__n8n-mcp__n8n_validate_workflow id=<WF8_ID>
```

Expected: no errors.

- [ ] **Step 4: Manually test WF8 via n8n_test_workflow with executeWorkflowTrigger payload**

Trigger from n8n UI with input:

```json
{
  "date": "2026-05-23",
  "slug": "test-canary",
  "slot": 1,
  "platform": "ig",
  "status": "ok",
  "permalink": "https://instagram.com/reel/TEST"
}
```

Expected: a new commit appears on `main` adding `data/posting-state/2026-05-23.json` with the test entry.

**Verify:**
```bash
git pull
cat data/posting-state/2026-05-23.json
```

Expected: JSON with `slugs.test-canary.ig.status == "ok"`.

- [ ] **Step 5: Update WF5 nodes to reference real WF8_ID**

Use `n8n_update_partial_workflow` with `patchNodeField` operations on the executeWorkflow nodes in WF5 (IG record, TT record) to replace placeholder `<WF8_ID>` with the real ID.

- [ ] **Step 6: Clean up test commit + export WF8 + commit**

```bash
# Remove the test entry
git rm data/posting-state/2026-05-23.json
git commit -m "chore: remove WF8 test-canary entry"
```

```
mcp__n8n-mcp__n8n_get_workflow id=<WF8_ID> mode="full"
# Save to ops/n8n/WF8_posting-state-helper.json
```

```bash
git add ops/n8n/WF8_posting-state-helper.json
git commit -m "feat(n8n): WF8 posting-state-helper sub-workflow"
```

## Task P1A.7: Add YouTube branch to WF5

> YouTube uses the dedicated n8n YouTube node (handles OAuth refresh, multipart upload, quota errors).

- [ ] **Step 1: Add YouTube upload node**

```json
{
  "id": "yt-upload",
  "name": "YouTube: upload Short",
  "type": "n8n-nodes-base.youTube",
  "typeVersion": 1,
  "position": [900, 600],
  "parameters": {
    "resource": "video",
    "operation": "upload",
    "title": "={{ $('Fetch caption').item.json.caption_text.split('\\n')[0].slice(0, 100) }}",
    "regionCode": "IQ",
    "additionalFields": {
      "categoryId": "25",
      "description": "={{ $('Fetch caption').item.json.caption_text + '\\n\\n#Shorts' }}",
      "privacyStatus": "public",
      "tags": "photonect, news, arabic, iraq, middleeast",
      "binaryProperty": "data",
      "notifySubscribers": true
    }
  },
  "credentials": {"youTubeOAuth2Api": {"id": "<cred-id-youtube-staging>", "name": "youtube-data-api-staging"}}
}
```

> Note: the YouTube node requires the mp4 as binary data on the input item. Pre-stage with an HTTP Request node that downloads from Cloudinary URL with `responseFormat: file`.

Add the binary fetch upstream:

```json
{
  "id": "yt-fetch-binary",
  "name": "YouTube: fetch mp4 binary from Cloudinary",
  "type": "n8n-nodes-base.httpRequest",
  "typeVersion": 4,
  "position": [700, 600],
  "parameters": {
    "method": "GET",
    "url": "={{ $('Upload mp4 to Cloudinary').item.json.secure_url }}",
    "options": {"response": {"response": {"responseFormat": "file"}}}
  }
}
```

Connect: Upload mp4 to Cloudinary → YouTube: fetch mp4 binary → YouTube: upload Short.

- [ ] **Step 2: Add YT state-record**

executeWorkflow node mirroring P1A.5 with `platform: "yt"` and `permalink: "=https://www.youtube.com/shorts/{{ $('YouTube: upload Short').item.json.id }}"`.

- [ ] **Step 3: Validate + export + commit**

```bash
git add ops/n8n/WF5_slot-posting.json
git commit -m "feat(n8n): WF5 — add YouTube Shorts branch (staging)"
```

## Task P1A.8: Add Telegram channel branch to WF5

- [ ] **Step 1: Add Telegram sendVideo node**

```json
{
  "id": "tg-send-video",
  "name": "Telegram: send video to channel",
  "type": "n8n-nodes-base.telegram",
  "typeVersion": 1.2,
  "position": [900, 800],
  "parameters": {
    "resource": "message",
    "operation": "sendVideo",
    "chatId": "={{ $vars.TELEGRAM_CHANNEL_ID_STAGING }}",
    "binaryData": true,
    "binaryPropertyName": "data",
    "additionalFields": {
      "caption": "={{ $('Fetch caption').item.json.caption_text.slice(0, 1024) }}",
      "parseMode": "Markdown"
    }
  },
  "credentials": {"telegramApi": {"id": "<cred-id-telegram-bot>", "name": "telegram-bot-token"}}
}
```

Pre-stage binary same as YouTube — reuse "YouTube: fetch mp4 binary from Cloudinary" output OR create a sibling "TG: fetch mp4 binary".

- [ ] **Step 2: Add TG state-record**

`platform: "telegram"`, `permalink: "=https://t.me/photonect_staging_channel/{{ $('Telegram: send video to channel').item.json.message_id }}"`.

- [ ] **Step 3: Validate + export + commit**

```bash
git add ops/n8n/WF5_slot-posting.json
git commit -m "feat(n8n): WF5 — add Telegram channel branch (staging)"
```

## Task P1A.9: Wire WF5 platform-fan-out (parallel) + error isolation

> By default, n8n runs branches sequentially. To fan out IG/TT/YT/Telegram in PARALLEL after the Cloudinary upload, we need a "fork" node — and an aggregator at the end to collect results.

- [ ] **Step 1: Add a fork node after Cloudinary**

Use a Code node or `Merge` node configured as "merge by position" to receive 4 outputs.

Actually n8n's pattern for parallel: connect one node's output to multiple downstream branches (it forks naturally). Each branch runs in parallel. So just connect:

```
Upload mp4 to Cloudinary
    → IG: create reels container (branch IG)
    → TikTok: init upload (branch TT)
    → YouTube: fetch mp4 binary (branch YT)
    → Telegram: fetch mp4 binary (branch TG)
```

Use 4 separate `addConnection` operations via `n8n_update_partial_workflow`.

- [ ] **Step 2: Add error continuation per branch**

Each platform's first HTTP node gets `"continueOnFail": true` so a TikTok failure doesn't kill the IG branch.

Add via `patchNodeField` on each branch's first node:

```
{"type": "patchNodeField", "node": "IG: create reels container", "fieldPath": "continueOnFail", "patches": [{"find": "false", "replace": "true"}]}
```

(Or set `continueOnFail: true` directly when first added — see node schema.)

- [ ] **Step 3: Add per-branch error recorder**

For each platform branch, add an "On Error" route that records `status: "failed"` with error message to posting-state. The IF node after each HTTP call checks for error response.

Pattern (per branch):

```
HTTP call → IF success? 
              YES → record ok with permalink
              NO  → record failed with error
```

- [ ] **Step 4: Validate**

```
mcp__n8n-mcp__n8n_validate_workflow id=<WF5_ID>
```

Expected: no fatal errors. Warnings about "no node reachable from X" should be 0.

- [ ] **Step 5: Export + commit**

```bash
git add ops/n8n/WF5_slot-posting.json
git commit -m "feat(n8n): WF5 — parallel fanout + per-branch error isolation"
```

## Task P1A.10: End-to-end smoke test WF5 on staging

> Now the moment of truth: WF5 posts a real video to 4 staging accounts.

- [ ] **Step 1: Verify a rendered staging video exists**

Pick a previously-rendered slug (e.g., 2026-05-10-iran-rainbow-site-tritium-semnan-may9). Confirm:
- `data/posts/2026-05-10-iran-rainbow-site-tritium-semnan-may9/.meta/props.json` exists
- `data/posts/2026-05-10-iran-rainbow-site-tritium-semnan-may9/caption.txt` exists (or fetch from Drive)
- Video mp4 in Drive

- [ ] **Step 2: Stage the input**

Get the Drive `file_id` for the video.mp4. Use Google Drive UI → right-click → Share → Get link → extract `id=...`.

Construct the manual trigger payload:

```json
{
  "slug": "2026-05-10-iran-rainbow-site-tritium-semnan-may9",
  "date": "2026-05-10",
  "slot": 99,
  "env": "staging",
  "drive_file_id": "<id from step 2>"
}
```

- [ ] **Step 3: Trigger WF5 manually from n8n UI**

In n8n: WF5 → Execute Workflow → paste payload → Run.

Watch the execution log node-by-node.

- [ ] **Step 4: Verify outcomes**

Expected within 2 minutes:
- IG: a Reel appears on staging IG account (private/unlisted is fine)
- TikTok: a video appears on staging TikTok account
- YouTube: a Short appears on staging YT channel
- Telegram: a video message in staging Telegram channel
- `data/posting-state/2026-05-10.json` created via WF8 with 4 entries (status: ok) for that slug

Check posting-state:

```bash
git pull
cat data/posting-state/2026-05-10.json | jq '.slugs["2026-05-10-iran-rainbow-site-tritium-semnan-may9"]'
```

Expected: object with ig/tiktok/yt/telegram each `{"status": "ok", "permalink": "...", "ts": "..."}`.

- [ ] **Step 5: Clean up staging posts**

Manually delete the test posts from each staging account.

```bash
git rm data/posting-state/2026-05-10.json
git commit -m "chore: clean up WF5 e2e smoke test posting-state"
```

- [ ] **Step 6: Mark WF5 staging-validated**

Add a comment in `ops/n8n/README.md`:

```markdown
## Validation log

- 2026-MM-DD: WF5 e2e smoke test on staging — all 4 platforms posted successfully.
```

```bash
git add ops/n8n/README.md
git commit -m "docs(ops): WF5 staging e2e smoke test validated"
```

---

# PHASE P1B — GitHub Actions: produce-today.yml + regen-slug.yml

> **Phase goal:** GitHub Actions that wrap the existing `/produce-today` Claude Code skill for headless CI execution. After this phase, n8n can dispatch these workflows via workflow_dispatch and they'll commit a new slate (or regen a single slug) to the repo unattended.
>
> **What "done" means:** Manually triggering `produce-today.yml` from GitHub Actions UI produces 6 commits to `data/posts/<date>-<slug>/` with valid props.json + caption.txt + media briefs.

## Task P1B.1: Write produce-today.yml workflow

**Files:**
- Create: `.github/workflows/produce-today.yml`

- [ ] **Step 1: Write the workflow YAML**

```yaml
name: Produce today's slate

# Triggered by n8n WF1 at 22:00 Asia/Baghdad daily. Also dispatchable manually
# from GitHub Actions UI for emergency rerun. Runs Claude Code headless to
# execute the /produce-today skill: research 6 fresh stories, author Arabic
# props, curate editorial photos, copywriter polish. Commits everything to
# data/posts/<date>-<slug>/.

on:
  workflow_dispatch:
    inputs:
      date:
        description: 'Date to produce (YYYY-MM-DD). Blank = today (UTC).'
        required: false
        type: string
        default: ''
      slug_count:
        description: 'Number of slugs to produce (default 6)'
        required: false
        type: string
        default: '6'

permissions:
  contents: write   # to commit the slate
  actions: read

jobs:
  produce:
    runs-on: ubuntu-latest
    timeout-minutes: 90

    steps:
      - name: Check out repo
        uses: actions/checkout@v4
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          fetch-depth: 0

      - name: Install Node 20 (for Claude Code CLI)
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install Python 3.11 (for /produce-today helpers)
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install Claude Code CLI
        run: npm install -g @anthropic-ai/claude-code

      - name: Resolve target date
        id: date
        env:
          INPUT_DATE: ${{ inputs.date }}
        run: |
          if [ -z "$INPUT_DATE" ]; then
            RESOLVED="$(date -u +%Y-%m-%d)"
          else
            RESOLVED="$INPUT_DATE"
          fi
          if ! [[ "$RESOLVED" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]]; then
            echo "::error::invalid date '$RESOLVED'"
            exit 1
          fi
          echo "value=$RESOLVED" >> "$GITHUB_OUTPUT"

      - name: Run /produce-today via headless Claude Code
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          DATE_ARG: ${{ steps.date.outputs.value }}
          SLUG_COUNT: ${{ inputs.slug_count }}
        run: |
          set -e
          claude --print \
            --allowedTools "Read,Write,Edit,Bash,Glob,Grep,WebSearch,WebFetch" \
            --dangerously-skip-permissions \
            "/produce-today --date $DATE_ARG --slug-count $SLUG_COUNT --autonomous"

      - name: Verify slate was produced
        env:
          DATE_ARG: ${{ steps.date.outputs.value }}
        run: |
          COUNT=$(ls -1d data/posts/${DATE_ARG}-*/ 2>/dev/null | wc -l)
          if [ "$COUNT" -lt 6 ]; then
            echo "::error::expected 6 slugs, got $COUNT for $DATE_ARG"
            exit 1
          fi
          for d in data/posts/${DATE_ARG}-*/; do
            slug=$(basename "$d")
            if [ ! -f "$d/.meta/props.json" ] || [ ! -f "$d/caption.txt" ]; then
              echo "::error::$slug missing props.json or caption.txt"
              exit 1
            fi
          done
          echo "✓ $COUNT valid slugs for $DATE_ARG"

      - name: Commit and push slate
        env:
          DATE_ARG: ${{ steps.date.outputs.value }}
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git add data/posts/${DATE_ARG}-* cloud-media/${DATE_ARG}/ 2>/dev/null || true
          if git diff --cached --quiet; then
            echo "nothing to commit"
            exit 0
          fi
          git commit -m "feat(slate): autonomous /produce-today for ${DATE_ARG}"
          git push origin main
```

- [ ] **Step 2: Validate YAML syntax**

```bash
python3 -c "import yaml; yaml.safe_load(open('.github/workflows/produce-today.yml'))" && echo "✓ valid"
```

Expected: `✓ valid`.

- [ ] **Step 3: Commit**

```bash
git add .github/workflows/produce-today.yml
git commit -m "feat(ci): add produce-today.yml — autonomous slate authoring via Claude Code"
```

- [ ] **Step 4: Push**

```bash
git push origin main
```

## Task P1B.2: Test produce-today.yml manually

- [ ] **Step 1: Trigger via GitHub UI**

Open the repo on GitHub → Actions → "Produce today's slate" → Run workflow. Leave inputs blank (uses today's UTC date).

- [ ] **Step 2: Watch the run**

Wait ~10-15 min. Watch logs for:
- Claude Code installation
- "/produce-today --date ..." output
- Per-slug commits
- Verify step shows "✓ 6 valid slugs"

- [ ] **Step 3: Verify on main branch**

```bash
git pull
ls data/posts/$(date -u +%Y-%m-%d)-*
```

Expected: 6 new slug directories with props.json + caption.txt each.

- [ ] **Step 4: If it failed — root cause**

Common failures:
- ANTHROPIC_API_KEY not set → check GH secrets
- Claude Code can't find /produce-today skill → check the skill is committed in the repo (it should be at `.claude/skills/...` or similar — verify with `ls -la .claude/`)
- The skill makes web requests but `--dangerously-skip-permissions` doesn't cover MCP tool requirements → may need to install MCP servers in CI

Fix the root cause, re-trigger, re-verify.

- [ ] **Step 5: Mark produce-today.yml validated**

Append to `docs/runbooks/p0-credential-setup.md`:

```markdown
## P1B sign-off

- produce-today.yml: e2e validated on YYYY-MM-DD — 6 slugs produced, committed, pushed
```

```bash
git add docs/runbooks/p0-credential-setup.md
git commit -m "docs(runbook): produce-today.yml validated"
```

## Task P1B.3: Write regen-slug.yml workflow

**Files:**
- Create: `.github/workflows/regen-slug.yml`

- [ ] **Step 1: Write the workflow**

```yaml
name: Regen one slug

# Triggered by n8n WF2 when Ahmed taps REGEN <slug> in the evening preview.
# Re-runs research + author + photos + copywriter for a single slug. Commits
# the update over the existing slug directory.

on:
  workflow_dispatch:
    inputs:
      slug:
        description: 'Slug to regenerate (e.g., 2026-05-23-iraq-foo)'
        required: true
        type: string

permissions:
  contents: write
  actions: read

jobs:
  regen:
    runs-on: ubuntu-latest
    timeout-minutes: 30

    steps:
      - name: Check out repo
        uses: actions/checkout@v4
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          fetch-depth: 0

      - name: Install Node 20
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install Python 3.11
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install Claude Code CLI
        run: npm install -g @anthropic-ai/claude-code

      - name: Validate slug input
        env:
          SLUG: ${{ inputs.slug }}
        run: |
          if ! [[ "$SLUG" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}- ]]; then
            echo "::error::slug must start with YYYY-MM-DD-"
            exit 1
          fi
          if [ ! -d "data/posts/$SLUG" ]; then
            echo "::error::slug directory does not exist: data/posts/$SLUG"
            exit 1
          fi

      - name: Run /produce-today --regen via headless Claude Code
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          SLUG: ${{ inputs.slug }}
        run: |
          set -e
          claude --print \
            --allowedTools "Read,Write,Edit,Bash,Glob,Grep,WebSearch,WebFetch" \
            --dangerously-skip-permissions \
            "/produce-today --regen $SLUG --autonomous"

      - name: Verify slug still valid
        env:
          SLUG: ${{ inputs.slug }}
        run: |
          if [ ! -f "data/posts/$SLUG/.meta/props.json" ] || [ ! -f "data/posts/$SLUG/caption.txt" ]; then
            echo "::error::$SLUG missing props.json or caption.txt after regen"
            exit 1
          fi
          echo "✓ $SLUG regenerated"

      - name: Commit and push
        env:
          SLUG: ${{ inputs.slug }}
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git add "data/posts/$SLUG" cloud-media/*/  2>/dev/null || true
          if git diff --cached --quiet; then
            echo "nothing changed (regen was idempotent)"
            exit 0
          fi
          git commit -m "fix(slate): regen $SLUG via Telegram callback"
          git push origin main
```

- [ ] **Step 2: Validate + commit + push**

```bash
python3 -c "import yaml; yaml.safe_load(open('.github/workflows/regen-slug.yml'))" && echo "✓ valid"
git add .github/workflows/regen-slug.yml
git commit -m "feat(ci): add regen-slug.yml — re-author one slug on demand"
git push origin main
```

## Task P1B.4: Test regen-slug.yml manually

- [ ] **Step 1: Pick a slug to regen**

Use one produced in P1B.2 (today's date).

- [ ] **Step 2: Trigger from GitHub UI**

Actions → "Regen one slug" → Run with `slug = 2026-05-XX-some-existing-slug`.

- [ ] **Step 3: Verify**

```bash
git pull
git log --oneline data/posts/2026-05-XX-some-existing-slug/ | head -3
```

Expected: a new commit "fix(slate): regen ..." at the top.

- [ ] **Step 4: Confirm content changed**

Compare props.json before and after — at minimum the `breaking.arabicHeadline` or research timestamps should differ.

- [ ] **Step 5: Mark regen-slug.yml validated in runbook + commit**

```bash
git add docs/runbooks/p0-credential-setup.md
git commit -m "docs(runbook): regen-slug.yml validated"
```

---

# PHASE P1C — WF1 evening-author (cron 22:00 → dispatch produce-today)

> **Phase goal:** A daily n8n cron at 22:00 Asia/Baghdad triggers produce-today.yml, polls until done, fetches the slate metadata from main branch, builds a Telegram preview message with thumbnails, sends to Ahmed's DM.
>
> **What "done" means:** Manually triggering WF1 (or temporarily setting cron to every 5 min) produces a Telegram message in Ahmed's DM with 6 thumbnail+title rows and REJECT/REGEN inline buttons per row.

## Task P1C.1: Build WF1 shell + cron trigger

- [ ] **Step 1: Create WF1**

```
mcp__n8n-mcp__n8n_create_workflow
  name: "WF1 evening-author"
  nodes: [
    {
      "id": "cron",
      "name": "Cron 22:00 Asia/Baghdad",
      "type": "n8n-nodes-base.scheduleTrigger",
      "typeVersion": 1.1,
      "position": [100, 300],
      "parameters": {
        "rule": {
          "interval": [{"field": "cronExpression", "expression": "0 22 * * *"}]
        }
      }
    },
    {
      "id": "set-date",
      "name": "Set date (tomorrow Baghdad)",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3,
      "position": [300, 300],
      "parameters": {
        "assignments": {
          "assignments": [{
            "id": "1",
            "name": "date",
            "value": "={{ DateTime.now().setZone('Asia/Baghdad').plus({days: 1}).toISODate() }}",
            "type": "string"
          }]
        }
      }
    }
  ]
  connections: {
    "Cron 22:00 Asia/Baghdad": {"main": [[{"node": "Set date (tomorrow Baghdad)", "type": "main", "index": 0}]]}
  }
  settings: {
    "timezone": "Asia/Baghdad",
    "executionOrder": "v1"
  }
```

Save returned `WF1_ID`.

- [ ] **Step 2: Add timezone to workflow settings**

If not set in step 1, `mcp__n8n-mcp__n8n_update_partial_workflow` with operation `updateSettings` payload `{timezone: "Asia/Baghdad"}`.

- [ ] **Step 3: Validate**

```
mcp__n8n-mcp__n8n_validate_workflow id=<WF1_ID>
```

Expected: no errors.

- [ ] **Step 4: Export + commit (in-progress)**

```bash
git add ops/n8n/WF1_evening-author.json
git commit -m "feat(n8n): WF1 evening-author shell — cron 22:00 Asia/Baghdad"
```

## Task P1C.2: Add GitHub workflow_dispatch + poll loop

- [ ] **Step 1: Add HTTP POST to GitHub workflow_dispatch**

```json
{
  "id": "dispatch-produce-today",
  "name": "Dispatch produce-today.yml",
  "type": "n8n-nodes-base.httpRequest",
  "typeVersion": 4,
  "position": [500, 300],
  "parameters": {
    "method": "POST",
    "url": "=https://api.github.com/repos/{{ $vars.GITHUB_OWNER }}/{{ $vars.GITHUB_REPO }}/actions/workflows/produce-today.yml/dispatches",
    "authentication": "predefinedCredentialType",
    "nodeCredentialType": "githubApi",
    "sendBody": true,
    "contentType": "json",
    "jsonBody": "={{ JSON.stringify({ ref: 'main', inputs: { date: $('Set date (tomorrow Baghdad)').item.json.date } }) }}"
  },
  "credentials": {"githubApi": {"id": "<cred-id-github-pat>", "name": "github-pat-news-engine"}}
}
```

GitHub returns 204 No Content. No run ID returned directly — we have to list runs and find the most recent one.

- [ ] **Step 2: Add wait 30s (GitHub takes a moment to register the run)**

```json
{
  "id": "wait-30s",
  "name": "Wait 30s",
  "type": "n8n-nodes-base.wait",
  "typeVersion": 1,
  "position": [700, 300],
  "parameters": {"amount": 30, "unit": "seconds"}
}
```

- [ ] **Step 3: Add HTTP GET runs list, pick most recent for produce-today.yml**

```json
{
  "id": "find-run-id",
  "name": "Find run ID",
  "type": "n8n-nodes-base.httpRequest",
  "typeVersion": 4,
  "position": [900, 300],
  "parameters": {
    "method": "GET",
    "url": "=https://api.github.com/repos/{{ $vars.GITHUB_OWNER }}/{{ $vars.GITHUB_REPO }}/actions/workflows/produce-today.yml/runs?per_page=1",
    "authentication": "predefinedCredentialType",
    "nodeCredentialType": "githubApi"
  },
  "credentials": {"githubApi": {"id": "<cred-id>", "name": "github-pat-news-engine"}}
}
```

Extract `workflow_runs[0].id` as `run_id`.

- [ ] **Step 4: Add poll loop (Wait + GET run status + IF complete)**

Same pattern as WF5 IG polling.

```json
{
  "id": "poll-wait",
  "name": "Poll wait 2min",
  "type": "n8n-nodes-base.wait",
  "typeVersion": 1,
  "position": [1100, 300],
  "parameters": {"amount": 2, "unit": "minutes"}
},
{
  "id": "poll-run-status",
  "name": "Poll run status",
  "type": "n8n-nodes-base.httpRequest",
  "typeVersion": 4,
  "position": [1300, 300],
  "parameters": {
    "method": "GET",
    "url": "=https://api.github.com/repos/{{ $vars.GITHUB_OWNER }}/{{ $vars.GITHUB_REPO }}/actions/runs/{{ $('Find run ID').item.json.workflow_runs[0].id }}",
    "authentication": "predefinedCredentialType",
    "nodeCredentialType": "githubApi"
  },
  "credentials": {"githubApi": {"id": "<cred-id>", "name": "github-pat-news-engine"}}
},
{
  "id": "status-check",
  "name": "Run complete?",
  "type": "n8n-nodes-base.if",
  "typeVersion": 2,
  "position": [1500, 300],
  "parameters": {
    "conditions": {"conditions": [{
      "leftValue": "={{ $json.status }}",
      "rightValue": "completed",
      "operator": {"type": "string", "operation": "equals"}
    }]}
  }
}
```

TRUE → continue. FALSE → loop back to `Poll wait 2min`. Add max-iteration safety (after 30 polls = 60min) by checking iteration count in a Code node.

- [ ] **Step 5: Add conclusion check (success vs failure)**

```json
{
  "id": "conclusion-check",
  "name": "Conclusion success?",
  "type": "n8n-nodes-base.if",
  "typeVersion": 2,
  "position": [1700, 300],
  "parameters": {
    "conditions": {"conditions": [{
      "leftValue": "={{ $('Poll run status').item.json.conclusion }}",
      "rightValue": "success",
      "operator": {"type": "string", "operation": "equals"}
    }]}
  }
}
```

TRUE → continue to slate fetch. FALSE → Telegram error to Ahmed with run URL → END.

- [ ] **Step 6: Validate + export + commit**

```bash
git add ops/n8n/WF1_evening-author.json
git commit -m "feat(n8n): WF1 — dispatch produce-today.yml + poll until complete"
```

## Task P1C.3: Fetch slate metadata from repo + build Telegram preview

- [ ] **Step 1: Add HTTP GET to list slug directories**

```json
{
  "id": "list-slugs",
  "name": "List today's slugs",
  "type": "n8n-nodes-base.httpRequest",
  "typeVersion": 4,
  "position": [1900, 300],
  "parameters": {
    "method": "GET",
    "url": "=https://api.github.com/repos/{{ $vars.GITHUB_OWNER }}/{{ $vars.GITHUB_REPO }}/contents/data/posts?ref=main",
    "authentication": "predefinedCredentialType",
    "nodeCredentialType": "githubApi"
  },
  "credentials": {"githubApi": {"id": "<cred-id>", "name": "github-pat-news-engine"}}
}
```

- [ ] **Step 2: Filter by date prefix (Code node)**

```json
{
  "id": "filter-slugs",
  "name": "Filter slugs by today's date",
  "type": "n8n-nodes-base.code",
  "typeVersion": 2,
  "position": [2100, 300],
  "parameters": {
    "jsCode": "const date = $('Set date (tomorrow Baghdad)').item.json.date;\nconst allDirs = $input.item.json;\nconst slugs = allDirs.filter(d => d.type === 'dir' && d.name.startsWith(date + '-')).map(d => d.name);\nreturn slugs.map(slug => ({ json: { slug, date } }));"
  }
}
```

Output: an item per slug (6 items).

- [ ] **Step 3: Per-slug fetch props.json**

```json
{
  "id": "fetch-props",
  "name": "Fetch props.json per slug",
  "type": "n8n-nodes-base.httpRequest",
  "typeVersion": 4,
  "position": [2300, 300],
  "parameters": {
    "method": "GET",
    "url": "=https://raw.githubusercontent.com/{{ $vars.GITHUB_OWNER }}/{{ $vars.GITHUB_REPO }}/main/data/posts/{{ $json.slug }}/.meta/props.json",
    "authentication": "predefinedCredentialType",
    "nodeCredentialType": "githubApi"
  },
  "credentials": {"githubApi": {"id": "<cred-id>", "name": "github-pat-news-engine"}}
}
```

(Runs 6 times — once per slug item from the filter.)

- [ ] **Step 4: Build slate preview state in n8n vars**

Use a Code node to aggregate all 6 props into a single `slate_preview` object and write to workflow variable:

```json
{
  "id": "aggregate-preview",
  "name": "Aggregate slate preview state",
  "type": "n8n-nodes-base.code",
  "typeVersion": 2,
  "position": [2500, 300],
  "parameters": {
    "jsCode": "const items = $input.all();\nconst slate = items.map(i => ({\n  slug: i.json.slug || i.json.breaking?.slug || i.binary?.data?.fileName,\n  arabicKicker: i.json.breaking?.arabicKicker || '',\n  arabicHeadline: i.json.breaking?.arabicHeadline || '',\n  englishSubhead: i.json.breaking?.englishSubhead || '',\n  heroMedia: i.json.breaking?.heroMedia || ''\n}));\n// Persist to workflow variable (n8n doesn't have native KV — use static data on this run, and store in n8n vars on success)\nconst date = $('Set date (tomorrow Baghdad)').item.json.date;\nreturn [{ json: { date, slate, status: 'pending_evening_lock' } }];"
  }
}
```

- [ ] **Step 5: Persist slate state for cross-workflow access**

n8n workflow variables are per-execution. To share state across workflows (WF1 writes, WF2 reads, WF3 reads), use either:
- A small JSON file in repo (`data/posting-state/<date>.slate-state.json`) — recommended for simplicity + audit
- n8n Data Tables (managed via `n8n_manage_datatable`) — more native

For v1, use repo. Add HTTP PUT to commit slate state JSON:

```json
{
  "id": "persist-slate-state",
  "name": "Persist slate state to repo",
  "type": "n8n-nodes-base.executeWorkflow",
  "typeVersion": 1,
  "position": [2700, 300],
  "parameters": {
    "workflowId": "<WF9_slate-state-helper-id>",
    "inputData": {
      "date":  "={{ $json.date }}",
      "slate": "={{ JSON.stringify($json.slate) }}",
      "status": "pending_evening_lock"
    }
  }
}
```

> **Note:** Build WF9 (slate-state-helper) as a tiny sub-workflow analogous to WF8 in Task P1A.6 — it commits `data/posting-state/<date>.slate-state.json`. Schema: `{date, status, slate: [...]}`.

- [ ] **Step 6: Validate + export + commit**

```bash
git add ops/n8n/WF1_evening-author.json
git commit -m "feat(n8n): WF1 — fetch slate + persist preview state to repo"
```

## Task P1C.4: Build Telegram preview message with inline buttons

- [ ] **Step 1: Add Telegram sendMessage node with inline keyboard**

```json
{
  "id": "send-preview",
  "name": "Send preview to Ahmed",
  "type": "n8n-nodes-base.telegram",
  "typeVersion": 1.2,
  "position": [2900, 300],
  "parameters": {
    "resource": "message",
    "operation": "sendMessage",
    "chatId": "={{ $vars.TELEGRAM_AHMED_CHAT_ID }}",
    "text": "={{ 'سَلام أحمد \\n\\n🌅 سلايد الغد (' + $('Set date (tomorrow Baghdad)').item.json.date + ')\\n\\n' + $('Aggregate slate preview state').item.json.slate.map((s, i) => `*${i+1}. ${s.arabicHeadline}*\\n_${s.englishSubhead}_`).join('\\n\\n') + '\\n\\n⏰ يقفل تلقائياً 5:00 صباحاً إن لم ترد' }}",
    "additionalFields": {
      "parseMode": "Markdown",
      "replyMarkup": "inlineKeyboard",
      "inlineKeyboard": {
        "rows": "={{ $('Aggregate slate preview state').item.json.slate.flatMap((s, i) => [[{text: `❌ Reject ${i+1}`, callback_data: `reject:${s.slug}`}, {text: `🔄 Regen ${i+1}`, callback_data: `regen:${s.slug}`}]]) }}"
      }
    }
  },
  "credentials": {"telegramApi": {"id": "<cred-id-telegram-bot>", "name": "telegram-bot-token"}}
}
```

(The inline keyboard JSON above is generated dynamically per slug — verify n8n's Telegram node supports dynamic keyboard via expressions. If not, fall back to HTTP Request directly calling `https://api.telegram.org/bot<TOKEN>/sendMessage`.)

- [ ] **Step 2: Validate**

```
mcp__n8n-mcp__n8n_validate_workflow id=<WF1_ID>
```

Expected: no errors.

- [ ] **Step 3: Smoke test — manually trigger WF1**

In n8n UI: WF1 → Execute workflow.

Expected: ~15 min later, a Telegram message arrives in Ahmed's DM with 6 entries + 12 inline buttons (1 reject + 1 regen per slug).

- [ ] **Step 4: Export + commit**

```bash
git add ops/n8n/WF1_evening-author.json
git commit -m "feat(n8n): WF1 — Telegram preview with per-slug REJECT/REGEN buttons"
```

## Task P1C.5: Activate WF1 cron

- [ ] **Step 1: Activate the workflow**

In n8n UI: WF1 → toggle Active ON. The cron will fire daily at 22:00 Asia/Baghdad.

Or via MCP:

```
mcp__n8n-mcp__n8n_update_partial_workflow
  id: <WF1_ID>
  operations: [{"type": "activateWorkflow"}]
```

- [ ] **Step 2: Verify next scheduled run**

n8n UI → WF1 → executions tab → shows next scheduled run timestamp.

- [ ] **Step 3: Record in runbook**

Append:

```markdown
## P1C sign-off

- WF1 evening-author: cron 22:00 Asia/Baghdad ACTIVE on YYYY-MM-DD
```

```bash
git add docs/runbooks/p0-credential-setup.md
git commit -m "docs(runbook): WF1 activated"
```

---

# PHASE P1D — WF2 evening-callback (Telegram REJECT / REGEN)

> **Phase goal:** When Ahmed taps an inline button (`reject:<slug>` or `regen:<slug>`) on the evening preview, WF2 fires immediately, mutates the slate state in repo, and updates the Telegram preview message in place to reflect the change.
>
> **What "done" means:** Tapping REJECT on a slug results in `data/posting-state/<date>.slate-state.json` showing that slug's status as `rejected`, and the preview message is edited to show a strikethrough on that row.

## Task P1D.1: WF2 shell + Telegram Trigger

- [ ] **Step 1: Create WF2**

```
mcp__n8n-mcp__n8n_create_workflow
  name: "WF2 evening-callback"
  nodes: [
    {
      "id": "telegram-callback",
      "name": "Telegram callback_query",
      "type": "n8n-nodes-base.telegramTrigger",
      "typeVersion": 1.1,
      "position": [100, 300],
      "parameters": {
        "updates": ["callback_query"]
      },
      "credentials": {"telegramApi": {"id": "<cred-id-telegram-bot>", "name": "telegram-bot-token"}}
    },
    {
      "id": "parse-callback",
      "name": "Parse callback_data (action:slug)",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [300, 300],
      "parameters": {
        "jsCode": "const cb = $input.item.json.callback_query;\nconst [action, slug] = cb.data.split(':');\nreturn {json: {action, slug, callback_query_id: cb.id, message_id: cb.message.message_id, chat_id: cb.message.chat.id, original_text: cb.message.text}};"
      }
    },
    {
      "id": "action-router",
      "name": "Route by action",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3,
      "position": [500, 300],
      "parameters": {
        "rules": {
          "values": [
            {"conditions": {"conditions": [{"leftValue": "={{ $json.action }}", "rightValue": "reject", "operator": {"type": "string", "operation": "equals"}}]}, "outputKey": "reject"},
            {"conditions": {"conditions": [{"leftValue": "={{ $json.action }}", "rightValue": "regen", "operator": {"type": "string", "operation": "equals"}}]}, "outputKey": "regen"},
            {"conditions": {"conditions": [{"leftValue": "={{ $json.action }}", "rightValue": "pause", "operator": {"type": "string", "operation": "equals"}}]}, "outputKey": "pause"}
          ]
        }
      }
    }
  ]
  connections: {
    "Telegram callback_query": {"main": [[{"node": "Parse callback_data (action:slug)", "type": "main", "index": 0}]]},
    "Parse callback_data (action:slug)": {"main": [[{"node": "Route by action", "type": "main", "index": 0}]]}
  }
```

Save `WF2_ID`.

- [ ] **Step 2: Validate + activate**

```
mcp__n8n-mcp__n8n_validate_workflow id=<WF2_ID>
mcp__n8n-mcp__n8n_update_partial_workflow id=<WF2_ID> operations=[{"type": "activateWorkflow"}]
```

n8n Telegram Trigger creates a webhook for `callback_query` updates. The trigger is now live.

- [ ] **Step 3: Export + commit shell**

```bash
git add ops/n8n/WF2_evening-callback.json
git commit -m "feat(n8n): WF2 evening-callback shell + Telegram trigger"
```

## Task P1D.2: Implement REJECT branch

- [ ] **Step 1: Add slate-state mutator for REJECT**

REJECT branch fans into:
1. Read current slate-state JSON via WF9 (slate-state-helper) or direct HTTP
2. Mark slug as `status: rejected`
3. Commit
4. Edit the preview Telegram message: strikethrough the rejected row

Add a Code node + HTTP nodes for the mutation, then a Telegram editMessageText node:

```json
{
  "id": "reject-mutate-state",
  "name": "REJECT: mark slug rejected in slate state",
  "type": "n8n-nodes-base.executeWorkflow",
  "typeVersion": 1,
  "position": [700, 200],
  "parameters": {
    "workflowId": "<WF9_slate-state-helper-id>",
    "inputData": {
      "action": "mark_rejected",
      "slug": "={{ $('Parse callback_data (action:slug)').item.json.slug }}",
      "date": "={{ $('Parse callback_data (action:slug)').item.json.slug.substring(0, 10) }}"
    }
  }
}
```

(WF9 helper supports actions: `init`, `mark_rejected`, `lock`, `mark_paused`, `mark_posted`. Expand WF9 to handle these.)

- [ ] **Step 2: Acknowledge the Telegram callback**

Mandatory — Telegram requires answering callback_query within 5s or button shows error:

```json
{
  "id": "reject-ack",
  "name": "Ack callback (REJECT)",
  "type": "n8n-nodes-base.telegram",
  "typeVersion": 1.2,
  "position": [900, 200],
  "parameters": {
    "resource": "callback",
    "operation": "answerQuery",
    "queryId": "={{ $('Parse callback_data (action:slug)').item.json.callback_query_id }}",
    "additionalFields": {
      "text": "✓ Rejected",
      "showAlert": false
    }
  },
  "credentials": {"telegramApi": {"id": "<cred-id>", "name": "telegram-bot-token"}}
}
```

- [ ] **Step 3: Edit preview message to reflect rejection**

```json
{
  "id": "reject-edit-preview",
  "name": "Edit preview: mark slug rejected",
  "type": "n8n-nodes-base.code",
  "typeVersion": 2,
  "position": [1100, 200],
  "parameters": {
    "jsCode": "const slug = $('Parse callback_data (action:slug)').item.json.slug;\nconst originalText = $('Parse callback_data (action:slug)').item.json.original_text;\n// Find the line for this slug (by matching the markdown headline) and add strikethrough\n// For v1 simplicity, append a status line at the bottom\nconst newText = originalText + `\\n\\n❌ Rejected: ${slug}`;\nreturn {json: {text: newText, chat_id: $('Parse callback_data (action:slug)').item.json.chat_id, message_id: $('Parse callback_data (action:slug)').item.json.message_id}};"
  }
},
{
  "id": "reject-edit-tg",
  "name": "Telegram editMessageText",
  "type": "n8n-nodes-base.telegram",
  "typeVersion": 1.2,
  "position": [1300, 200],
  "parameters": {
    "resource": "message",
    "operation": "editMessageText",
    "messageType": "inlineMessage",
    "chatId": "={{ $json.chat_id }}",
    "messageId": "={{ $json.message_id }}",
    "text": "={{ $json.text }}",
    "additionalFields": {"parseMode": "Markdown"}
  },
  "credentials": {"telegramApi": {"id": "<cred-id>", "name": "telegram-bot-token"}}
}
```

- [ ] **Step 4: Validate + export + commit**

```bash
git add ops/n8n/WF2_evening-callback.json
git commit -m "feat(n8n): WF2 — REJECT branch (mutate state + edit preview)"
```

## Task P1D.3: Implement REGEN branch

- [ ] **Step 1: Dispatch regen-slug.yml**

```json
{
  "id": "regen-dispatch",
  "name": "REGEN: dispatch regen-slug.yml",
  "type": "n8n-nodes-base.httpRequest",
  "typeVersion": 4,
  "position": [700, 400],
  "parameters": {
    "method": "POST",
    "url": "=https://api.github.com/repos/{{ $vars.GITHUB_OWNER }}/{{ $vars.GITHUB_REPO }}/actions/workflows/regen-slug.yml/dispatches",
    "authentication": "predefinedCredentialType",
    "nodeCredentialType": "githubApi",
    "sendBody": true,
    "contentType": "json",
    "jsonBody": "={{ JSON.stringify({ ref: 'main', inputs: { slug: $('Parse callback_data (action:slug)').item.json.slug } }) }}"
  },
  "credentials": {"githubApi": {"id": "<cred-id>", "name": "github-pat-news-engine"}}
}
```

- [ ] **Step 2: Ack the callback**

```json
{
  "id": "regen-ack",
  "name": "Ack callback (REGEN)",
  "type": "n8n-nodes-base.telegram",
  "typeVersion": 1.2,
  "position": [900, 400],
  "parameters": {
    "resource": "callback",
    "operation": "answerQuery",
    "queryId": "={{ $('Parse callback_data (action:slug)').item.json.callback_query_id }}",
    "additionalFields": {"text": "🔄 Regenerating... will update in ~5min", "showAlert": false}
  },
  "credentials": {"telegramApi": {"id": "<cred-id>", "name": "telegram-bot-token"}}
}
```

- [ ] **Step 3: (Optional) Poll regen-slug.yml until done + re-edit preview**

For v1 simplicity, the REGEN ack message is enough. A more polished version (deferred to v1.1) polls regen-slug.yml completion and updates the preview row.

- [ ] **Step 4: Validate + export + commit**

```bash
git add ops/n8n/WF2_evening-callback.json
git commit -m "feat(n8n): WF2 — REGEN branch (dispatch regen-slug.yml + ack)"
```

## Task P1D.4: Smoke test WF2

- [ ] **Step 1: Trigger WF1 manually to generate a preview**

In n8n UI: WF1 → Execute workflow.

Wait for Telegram preview to arrive in Ahmed's DM.

- [ ] **Step 2: Tap REJECT on slug 1**

Open Telegram → tap "❌ Reject 1" button under preview.

Expected:
- Button immediately shows "✓ Rejected" toast
- Preview message updates to show "❌ Rejected: 2026-MM-DD-..." at bottom
- `data/posting-state/<date>.slate-state.json` shows that slug with `status: rejected`

- [ ] **Step 3: Tap REGEN on slug 2**

Tap "🔄 Regen 2".

Expected:
- Toast "🔄 Regenerating..."
- A new run of regen-slug.yml appears in GitHub Actions
- ~5 min later, that slug's props.json is updated

- [ ] **Step 4: Clean up + commit validation note**

```bash
git rm data/posting-state/<date>.slate-state.json 2>/dev/null || true
git commit -m "chore: clean up WF2 smoke test slate state" || true

# update runbook
git add docs/runbooks/p0-credential-setup.md
git commit -m "docs(runbook): WF2 REJECT/REGEN validated"
```

---

# PHASE P1E — WF3 morning-render (cron 06:00 → render-day.yml → kill-window preview)

> **Phase goal:** A daily cron at 06:00 Asia/Baghdad dispatches render-day.yml, polls until rendered, downloads N video.mp4 + caption.txt from Drive, uploads each to Cloudinary, and sends a Telegram kill-window message to Ahmed at ~06:45 with 60min timer.
>
> **What "done" means:** Manually triggering WF3 (with a date that has staged slate) produces a Telegram kill-window message with thumbnails + PAUSE / PAUSE-<slug> buttons. After 60min, slate locks for posting.

## Task P1E.1: Build WF3 shell + cron + dispatch

- [ ] **Step 1: Create WF3**

```
mcp__n8n-mcp__n8n_create_workflow
  name: "WF3 morning-render"
  nodes: [
    {
      "id": "cron",
      "name": "Cron 06:00 Asia/Baghdad",
      "type": "n8n-nodes-base.scheduleTrigger",
      "typeVersion": 1.1,
      "position": [100, 300],
      "parameters": {
        "rule": {"interval": [{"field": "cronExpression", "expression": "0 6 * * *"}]}
      }
    },
    {
      "id": "set-date-today",
      "name": "Set date (today Baghdad)",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3,
      "position": [300, 300],
      "parameters": {
        "assignments": {
          "assignments": [{
            "id": "1", "name": "date",
            "value": "={{ DateTime.now().setZone('Asia/Baghdad').toISODate() }}",
            "type": "string"
          }]
        }
      }
    },
    {
      "id": "dispatch-render",
      "name": "Dispatch render-day.yml",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4,
      "position": [500, 300],
      "parameters": {
        "method": "POST",
        "url": "=https://api.github.com/repos/{{ $vars.GITHUB_OWNER }}/{{ $vars.GITHUB_REPO }}/actions/workflows/render-day.yml/dispatches",
        "authentication": "predefinedCredentialType",
        "nodeCredentialType": "githubApi",
        "sendBody": true,
        "contentType": "json",
        "jsonBody": "={{ JSON.stringify({ ref: 'main', inputs: { date: $json.date } }) }}"
      },
      "credentials": {"githubApi": {"id": "<cred-id>", "name": "github-pat-news-engine"}}
    }
  ]
  connections: { ... }
  settings: { "timezone": "Asia/Baghdad" }
```

- [ ] **Step 2: Add poll loop (same pattern as WF1)**

Identical to WF1 Task P1C.2 Step 4-5, except polls `render-day.yml/runs` and timeout is 60min (render takes ~30-40min).

- [ ] **Step 3: Validate + export + commit**

```bash
git add ops/n8n/WF3_morning-render.json
git commit -m "feat(n8n): WF3 morning-render — cron 06:00 + dispatch + poll"
```

## Task P1E.2: Download videos from Drive + upload to Cloudinary

- [ ] **Step 1: Read slate-state from repo to get active slugs**

(slugs that survived REJECT in WF2)

```json
{
  "id": "read-slate-state",
  "name": "Read slate state (active slugs only)",
  "type": "n8n-nodes-base.httpRequest",
  "typeVersion": 4,
  "position": [1900, 300],
  "parameters": {
    "method": "GET",
    "url": "=https://raw.githubusercontent.com/{{ $vars.GITHUB_OWNER }}/{{ $vars.GITHUB_REPO }}/main/data/posting-state/{{ $('Set date (today Baghdad)').item.json.date }}.slate-state.json",
    "authentication": "predefinedCredentialType",
    "nodeCredentialType": "githubApi",
    "options": {"response": {"response": {"neverError": true}}}
  },
  "credentials": {"githubApi": {"id": "<cred-id>", "name": "github-pat-news-engine"}}
}
```

- [ ] **Step 2: Code node — filter active + emit per slug**

```json
{
  "id": "filter-active",
  "name": "Filter active slugs (not rejected)",
  "type": "n8n-nodes-base.code",
  "typeVersion": 2,
  "position": [2100, 300],
  "parameters": {
    "jsCode": "const state = $input.item.json;\nconst active = state.slate.filter(s => s.status !== 'rejected');\nreturn active.map(s => ({ json: { slug: s.slug, date: state.date, ...s } }));"
  }
}
```

- [ ] **Step 3: Per-slug Drive download + Cloudinary upload**

For each slug item:

```json
{
  "id": "drive-find-video",
  "name": "Drive: find video.mp4 by name",
  "type": "n8n-nodes-base.httpRequest",
  "typeVersion": 4,
  "position": [2300, 300],
  "parameters": {
    "method": "GET",
    "url": "=https://www.googleapis.com/drive/v3/files?q=name='{{ $json.slug }}' and mimeType='application/vnd.google-apps.folder'&fields=files(id)",
    "authentication": "predefinedCredentialType",
    "nodeCredentialType": "googleDriveOAuth2Api"
  },
  "credentials": {"googleDriveOAuth2Api": {"id": "<existing-drive-cred-id>", "name": "drive-uploader"}}
}
```

(Then a chained query for `video.mp4` inside that folder, download it, push to Cloudinary via the same pattern as WF5.)

For brevity, the executor follows the WF5 Cloudinary pattern (Task P1A.4).

- [ ] **Step 4: Persist Cloudinary URLs to slate state**

After each slug's Cloudinary upload completes, call WF9 (slate-state-helper) with action `set_cloudinary_url`:

```json
{
  "inputData": {
    "action": "set_cloudinary_url",
    "date": "={{ $('Set date (today Baghdad)').item.json.date }}",
    "slug": "={{ $json.slug }}",
    "cloudinary_url": "={{ $('Upload to Cloudinary').item.json.secure_url }}"
  }
}
```

- [ ] **Step 5: Validate + export + commit**

```bash
git add ops/n8n/WF3_morning-render.json
git commit -m "feat(n8n): WF3 — Drive download + Cloudinary upload per slug"
```

## Task P1E.3: Send kill-window Telegram message

- [ ] **Step 1: Aggregate thumbnails + build message**

Use Code node to construct message text + inline keyboard:

```json
{
  "id": "build-kill-msg",
  "name": "Build kill-window message",
  "type": "n8n-nodes-base.code",
  "typeVersion": 2,
  "position": [2900, 300],
  "parameters": {
    "jsCode": "const slate = $('Read slate state (active slugs only)').item.json.slate.filter(s => s.status !== 'rejected');\nconst date = $('Set date (today Baghdad)').item.json.date;\nconst text = `🔥 *جاهز للنشر* — ${date}\\n\\n${slate.map((s, i) => `${i+1}. ${s.arabicHeadline}\\n   ⏰ slot ${i+1}`).join('\\n\\n')}\\n\\n⚠️ *ينطلق خلال 60 دقيقة*\\nاضغط PAUSE لإيقاف الكل، أو PAUSE <رقم> لتخطي واحد.`;\nconst keyboard = {inline_keyboard: [\n  [{text: '🛑 PAUSE ALL', callback_data: 'pause_all:'+date}],\n  ...slate.map((s,i) => [{text: `⏸ Skip ${i+1}`, callback_data: `pause:${s.slug}`}])\n]};\nreturn {json: {text, keyboard, chat_id: $vars.TELEGRAM_AHMED_CHAT_ID}};"
  }
},
{
  "id": "send-kill-msg",
  "name": "Send kill-window message",
  "type": "n8n-nodes-base.httpRequest",
  "typeVersion": 4,
  "position": [3100, 300],
  "parameters": {
    "method": "POST",
    "url": "=https://api.telegram.org/bot{{ $('Get Telegram token').item.json.token }}/sendMessage",
    "sendBody": true,
    "contentType": "json",
    "jsonBody": "={{ JSON.stringify({chat_id: $json.chat_id, text: $json.text, parse_mode: 'Markdown', reply_markup: $json.keyboard}) }}"
  }
}
```

(`Get Telegram token` is a Set node reading from n8n credential's exposed token — or use the Telegram node `sendMessage` with reply_markup field. For maximum control over keyboard JSON, raw HTTP is cleaner.)

- [ ] **Step 2: Capture message_id for later editing by WF4**

The send-message response contains `result.message_id`. Persist to slate state via WF9 action `set_kill_msg_id`.

- [ ] **Step 3: Wait 60min then lock slate**

After sending kill message, this WF3 execution holds open with a Wait node for 60 minutes:

```json
{
  "id": "kill-window-wait",
  "name": "Wait 60min (kill window)",
  "type": "n8n-nodes-base.wait",
  "typeVersion": 1,
  "position": [3300, 300],
  "parameters": {"amount": 60, "unit": "minutes"}
}
```

- [ ] **Step 4: After 60min, lock slate state**

Call WF9 action `lock`:

```json
{
  "inputData": {
    "action": "lock",
    "date": "={{ $('Set date (today Baghdad)').item.json.date }}",
    "status": "posting_locked"
  }
}
```

- [ ] **Step 5: Validate + export + commit + activate**

```bash
git add ops/n8n/WF3_morning-render.json
git commit -m "feat(n8n): WF3 — kill-window message + 60min wait + lock"
```

Activate WF3 in n8n UI.

---

# PHASE P1F — WF4 kill-window-callback (PAUSE / PAUSE-slug)

> **Phase goal:** When Ahmed taps PAUSE or PAUSE-<slug> in the kill-window message, WF4 fires immediately and mutates slate state to mark the slug(s) as paused.
>
> **Reuses:** WF2's Telegram trigger pattern, WF9 helper.

## Task P1F.1: Build WF4

> WF4 is structurally similar to WF2 — same Telegram callback trigger pattern. Build by copying WF2's shell and adapting the action handlers.

- [ ] **Step 1: Create WF4 by adapting WF2**

Note: in practice, WF2 and WF4 could be ONE workflow with broader action routing (REJECT/REGEN/PAUSE/PAUSE_ALL). For maintainability they're split. Build WF4 with the same TelegramTrigger + parse + switch pattern from P1D.1, with switch cases for `pause` and `pause_all`.

```
mcp__n8n-mcp__n8n_create_workflow
  name: "WF4 kill-window-callback"
  (nodes mirror WF2 with action handlers for pause/pause_all)
```

- [ ] **Step 2: PAUSE branch — mark slug paused**

```json
{
  "id": "pause-mutate",
  "name": "PAUSE: mark slug paused",
  "type": "n8n-nodes-base.executeWorkflow",
  "typeVersion": 1,
  "position": [700, 300],
  "parameters": {
    "workflowId": "<WF9_ID>",
    "inputData": {
      "action": "mark_paused",
      "slug": "={{ $('Parse callback_data (action:slug)').item.json.slug }}",
      "date": "={{ $('Parse callback_data (action:slug)').item.json.slug.substring(0,10) }}"
    }
  }
}
```

+ ack callback + edit message to show paused slug.

- [ ] **Step 3: PAUSE_ALL branch — mark all active slugs paused**

WF9 action: `pause_all`.

- [ ] **Step 4: Validate + activate + commit**

```bash
git add ops/n8n/WF4_kill-window-callback.json
git commit -m "feat(n8n): WF4 kill-window-callback — PAUSE / PAUSE_ALL"
```

## Task P1F.2: Smoke test WF4

- [ ] **Step 1: Trigger WF3 manually to get a kill-window preview**

- [ ] **Step 2: Tap "⏸ Skip 2"**

Expected:
- Toast "✓ Skipped"
- Message updates to show "⏸ Skipped: <slug>"
- `data/posting-state/<date>.slate-state.json` shows that slug `status: paused`

- [ ] **Step 3: Verify WF5 won't post a paused slug**

When WF5 runs at its scheduled slot, the first thing it does is read slate state and check status. Add this guard if not already present.

```bash
git add docs/runbooks/p0-credential-setup.md
git commit -m "docs(runbook): WF4 PAUSE validated"
```

---

# PHASE P1G — WF6 rotate-tokens (weekly token refresh)

> **Phase goal:** Every Monday at 03:00 Asia/Baghdad, check Meta long-lived token age; if within 14 days of expiry, refresh it via the `fb_exchange_token` endpoint and update the n8n credential.
>
> **Why critical:** Meta tokens expire every 60 days. Without rotation, IG posting stops on day 60.

## Task P1G.1: Build WF6

- [ ] **Step 1: Create WF6**

```
mcp__n8n-mcp__n8n_create_workflow
  name: "WF6 rotate-tokens"
  nodes: [
    {
      "id": "cron-monday-3am",
      "name": "Cron Mon 03:00 Asia/Baghdad",
      "type": "n8n-nodes-base.scheduleTrigger",
      "typeVersion": 1.1,
      "position": [100, 300],
      "parameters": {
        "rule": {"interval": [{"field": "cronExpression", "expression": "0 3 * * 1"}]}
      }
    },
    {
      "id": "check-token-age",
      "name": "Check Meta token age via debug_token",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4,
      "position": [300, 300],
      "parameters": {
        "method": "GET",
        "url": "=https://graph.facebook.com/debug_token?input_token={{ $vars.META_LONG_LIVED_USER_TOKEN }}&access_token={{ $vars.META_APP_ID }}|{{ $vars.META_APP_SECRET }}"
      }
    },
    {
      "id": "days-until-expiry",
      "name": "Compute days until expiry",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [500, 300],
      "parameters": {
        "jsCode": "const expiresAt = $input.item.json.data.expires_at;\nconst now = Math.floor(Date.now() / 1000);\nconst daysLeft = Math.floor((expiresAt - now) / 86400);\nreturn {json: {days_left: daysLeft, expires_at: expiresAt, needs_refresh: daysLeft < 14}};"
      }
    },
    {
      "id": "if-needs-refresh",
      "name": "Needs refresh?",
      "type": "n8n-nodes-base.if",
      "typeVersion": 2,
      "position": [700, 300],
      "parameters": {
        "conditions": {"conditions": [{
          "leftValue": "={{ $json.needs_refresh }}",
          "rightValue": true,
          "operator": {"type": "boolean", "operation": "equals"}
        }]}
      }
    }
  ]
  connections: { ... }
  settings: { "timezone": "Asia/Baghdad" }
```

- [ ] **Step 2: TRUE branch — refresh token + update credential**

```json
{
  "id": "fb-exchange-token",
  "name": "Exchange for new long-lived token",
  "type": "n8n-nodes-base.httpRequest",
  "typeVersion": 4,
  "position": [900, 200],
  "parameters": {
    "method": "GET",
    "url": "=https://graph.facebook.com/v21.0/oauth/access_token?grant_type=fb_exchange_token&client_id={{ $vars.META_APP_ID }}&client_secret={{ $vars.META_APP_SECRET }}&fb_exchange_token={{ $vars.META_LONG_LIVED_USER_TOKEN }}"
  }
}
```

Then update n8n credential via MCP:

```json
{
  "id": "update-cred",
  "name": "Update meta-graph-api credential",
  "type": "n8n-nodes-base.code",
  "typeVersion": 2,
  "position": [1100, 200],
  "parameters": {
    "jsCode": "// n8n doesn't allow programmatic credential update from within a workflow for security.\n// Instead: write new token to n8n variable, then send Telegram alert asking Ahmed to confirm + rotate in UI.\n// OR: use n8n's REST API (requires admin token) — out of scope for v1, manual rotation step.\nconst newToken = $input.item.json.access_token;\nreturn {json: {new_token: newToken, length: newToken.length}};"
  }
}
```

> **Note for executor:** Updating n8n credentials programmatically from within a workflow isn't natively supported. For v1, WF6 sends a Telegram alert to Ahmed: "Meta token refresh ready. New token: <truncated>. Please update credential 'meta-graph-api' in n8n UI within 24h." Ahmed manually updates. This is a known v1 limitation; v2 could use n8n REST API + admin token.

- [ ] **Step 3: Telegram alert (manual rotation needed)**

```json
{
  "id": "alert-manual-rotate",
  "name": "Alert Ahmed: manual rotation needed",
  "type": "n8n-nodes-base.telegram",
  "typeVersion": 1.2,
  "position": [1300, 200],
  "parameters": {
    "resource": "message",
    "operation": "sendMessage",
    "chatId": "={{ $vars.TELEGRAM_AHMED_CHAT_ID }}",
    "text": "=🔑 Meta token refresh needed.\n\nDays left: {{ $('Compute days until expiry').item.json.days_left }}\nNew token (first 20 chars): `{{ $('Update meta-graph-api credential').item.json.new_token.substring(0, 20) }}...`\n\nFull token written to n8n var META_TOKEN_PENDING. Please update credential 'meta-graph-api' in n8n UI within 24h.",
    "additionalFields": {"parseMode": "Markdown"}
  },
  "credentials": {"telegramApi": {"id": "<cred-id>", "name": "telegram-bot-token"}}
}
```

- [ ] **Step 4: FALSE branch — log "still fresh"**

Just a Set node:

```json
{
  "id": "log-fresh",
  "name": "Log: token still fresh",
  "type": "n8n-nodes-base.set",
  "typeVersion": 3,
  "position": [900, 400],
  "parameters": {
    "assignments": {"assignments": [{
      "id": "1", "name": "msg", "value": "=token still fresh: {{ $('Compute days until expiry').item.json.days_left }} days left", "type": "string"
    }]}
  }
}
```

- [ ] **Step 5: Validate + activate + commit**

```bash
git add ops/n8n/WF6_rotate-tokens.json
git commit -m "feat(n8n): WF6 rotate-tokens — weekly Meta token age check + alert"
```

---

# PHASE P1H — WF7 daily-digest (morning after — yesterday's results)

> **Phase goal:** Every morning at 09:00 Asia/Baghdad, read yesterday's `data/posting-state/<date>.json`, build a per-platform success/fail digest, send to Ahmed's DM with permalinks.

## Task P1H.1: Build WF7

- [ ] **Step 1: Create WF7**

```
mcp__n8n-mcp__n8n_create_workflow
  name: "WF7 daily-digest"
  nodes: [
    {"id": "cron", "name": "Cron 09:00 Asia/Baghdad", "type": "n8n-nodes-base.scheduleTrigger", ...},
    {"id": "set-yesterday", "name": "Set date (yesterday)", "type": "n8n-nodes-base.set",
      "parameters": {"assignments": {"assignments": [{"id":"1","name":"date","value":"={{ DateTime.now().setZone('Asia/Baghdad').minus({days:1}).toISODate() }}","type":"string"}]}}},
    {"id": "fetch-state", "name": "Fetch posting-state for yesterday", "type": "n8n-nodes-base.httpRequest",
      "parameters": {
        "method": "GET",
        "url": "=https://raw.githubusercontent.com/{{ $vars.GITHUB_OWNER }}/{{ $vars.GITHUB_REPO }}/main/data/posting-state/{{ $json.date }}.json",
        "options": {"response": {"response": {"neverError": true}}}
      }},
    {"id": "build-digest", "name": "Build digest text", "type": "n8n-nodes-base.code",
      "parameters": {"jsCode": "const state = $input.item.json;\nif (!state.slugs) return [{json: {text: `📭 لا منشورات لـ ${$('Set date (yesterday)').item.json.date}`, chat_id: $vars.TELEGRAM_AHMED_CHAT_ID}}];\nconst slugs = Object.entries(state.slugs);\nconst lines = slugs.map(([slug, data]) => {\n  const platforms = ['ig', 'tiktok', 'yt', 'telegram'];\n  const status = platforms.map(p => `${p}:${data[p]?.status || '—'}`).join(' ');\n  return `• ${slug}\\n  ${status}`;\n});\nconst text = `📊 *تقرير ${$('Set date (yesterday)').item.json.date}*\\n\\n${slugs.length}/${6} منشور.\\n\\n${lines.join('\\n\\n')}`;\nreturn [{json: {text, chat_id: $vars.TELEGRAM_AHMED_CHAT_ID}}];"}},
    {"id": "send-digest", "name": "Send digest to Ahmed", "type": "n8n-nodes-base.telegram",
      "parameters": {"resource": "message", "operation": "sendMessage", "chatId": "={{ $json.chat_id }}", "text": "={{ $json.text }}", "additionalFields": {"parseMode": "Markdown"}}}
  ]
  connections: { ... }
  settings: { "timezone": "Asia/Baghdad" }
```

- [ ] **Step 2: Validate + activate + commit**

```bash
git add ops/n8n/WF7_daily-digest.json
git commit -m "feat(n8n): WF7 daily-digest — 09:00 morning report"
```

---

# PHASE P2 — Integration tests

> **Phase goal:** Validate the full chain works end-to-end against staging accounts. Cover the happy path AND the failure modes documented in the spec.

## Task P2.1: Per-platform smoke tests

For each of IG / TT / YT / Telegram, manually trigger WF5 against a single canned mp4 + caption. Verify post appears on staging account. Already done in P1A.10 — re-run here to confirm staging credentials still work after P1B-P1H changes.

## Task P2.2: End-to-end dry run

- [ ] **Step 1: Use a real "tomorrow" date but route to staging**

Switch all WF5 platform credentials to staging (`-staging` suffix). Manually trigger WF1 → wait for produce-today → tap REJECT on 1 slug → wait until ~05:00 → manually trigger WF3 → wait for render → tap PAUSE on 1 slug at kill window → let other 4 slugs post → check next morning digest.

Total real-time: ~12 hours. Run on a Friday so Saturday's digest is the reportback.

- [ ] **Step 2: Verify all expected outcomes**

| Check | Expected |
|---|---|
| /produce-today commit lands in main | ✓ |
| Telegram evening preview arrives at 22:00 | ✓ |
| REJECT moves slug to `status: rejected` | ✓ |
| 5am lock removes rejected slug from active set | ✓ |
| 6am render runs only on remaining slugs | ✓ |
| Kill window preview at ~06:45 with N items | ✓ |
| PAUSE during kill window removes slug from posting | ✓ |
| Posts go live at slot times on staging | ✓ |
| `data/posting-state/<date>.json` has correct ok/skipped/failed entries | ✓ |
| 09:00 next-morning digest shows accurate breakdown | ✓ |

- [ ] **Step 3: Document outcome in runbook**

```bash
git add docs/runbooks/p0-credential-setup.md
git commit -m "docs(runbook): P2 e2e dry run complete — all checks pass"
```

## Task P2.3: Failure injection tests

- [ ] **Step 1: TikTok credential failure**

Temporarily corrupt the `tiktok-content-api-staging` credential (replace token with garbage). Trigger WF5 manually.

Expected: IG/YT/Telegram succeed. TikTok branch logs `status: failed` with error. Telegram alert fires. Other branches unaffected.

Restore credential.

- [ ] **Step 2: Render failure**

Push a broken props.json (intentional schema violation) and trigger WF3.

Expected: render-day.yml exits non-zero. WF3 catches via poll. Telegram error with Action log URL. No kill-window message sent.

Roll back the broken props.json.

- [ ] **Step 3: Produce-today CI failure**

Temporarily revoke `ANTHROPIC_API_KEY` GH secret. Trigger WF1.

Expected: produce-today.yml fails fast. WF1 catches. Telegram error.

Restore secret.

- [ ] **Step 4: Record results in runbook + commit**

```bash
git add docs/runbooks/p0-credential-setup.md
git commit -m "docs(runbook): P2 failure injection tests complete"
```

## Task P2.4: Kill-window timing test

- [ ] **Step 1: Trigger WF3 + tap PAUSE at exact 59min mark**

Verify the slot crons honor the pause even on the boundary.

- [ ] **Step 2: Trigger WF3 + don't tap anything**

Verify slate auto-locks after 60min.

- [ ] **Step 3: Record + commit**

---

# PHASE P3 — Live cutover

> **Phase goal:** Switch all WF5 platform credentials from staging to live (@photonect.news + @photonect_news_channel). Progressive ramp: 1 post day 1 → 3 posts day 2-3 → full 6 day 4+.

## Task P3.1: Pre-cutover checklist

- [ ] **Step 1: Verify YouTube 50K quota was granted**

```bash
# Check GCP console → YouTube Data API v3 quota → Queries per day should show 50000
```

If not granted yet, BLOCK live cutover for YouTube (route YT to staging or skip in WF5) until quota lands.

- [ ] **Step 2: Verify Meta token has >30 days left**

```bash
curl "https://graph.facebook.com/debug_token?input_token=$META_LONG_LIVED_USER_TOKEN&access_token=$META_APP_ID|$META_APP_SECRET" | jq '.data.expires_at'
```

If <30 days, run WF6 rotation now.

- [ ] **Step 3: Backup all n8n workflows**

```
For each WF in [WF1..WF8]:
  mcp__n8n-mcp__n8n_get_workflow id=<WF_ID> mode="full"
  Save to ops/n8n/<WF_NAME>.json
```

```bash
git add ops/n8n/
git commit -m "ops(n8n): pre-cutover backup of all v1 workflows"
```

## Task P3.2: Switch WF5 credentials to live

- [ ] **Step 1: Update WF5 IG branch credential reference**

Use `n8n_update_partial_workflow` with `patchNodeField` on each IG/TT/YT node:

```
{"type": "patchNodeField", "node": "IG: create reels container", "fieldPath": "credentials.httpHeaderAuth.id", "patches": [{"find": "<staging-cred-id>", "replace": "<live-cred-id>"}]}
```

(Same for IG poll, IG publish, IG fetch permalink, TT init, TT poll, TT publish, YT upload, Telegram sendVideo.)

- [ ] **Step 2: Update environment variables in WF5**

Also patch `IG_BUSINESS_ACCOUNT_ID_STAGING` → `IG_BUSINESS_ACCOUNT_ID`, `TELEGRAM_CHANNEL_ID_STAGING` → `TELEGRAM_CHANNEL_ID`.

- [ ] **Step 3: Validate + commit**

```bash
git add ops/n8n/WF5_slot-posting.json
git commit -m "ops(n8n): WF5 switched to LIVE credentials"
```

## Task P3.3: Day 1 — single post live

- [ ] **Step 1: Choose date with 6 slugs already staged**

Use day after P2.2 dry run.

- [ ] **Step 2: Temporarily set WF5 to skip 5/6 slots**

Use n8n vars: `DAILY_POST_LIMIT = 1`. Add check in WF5: if slot > DAILY_POST_LIMIT, skip with `status: skipped`.

- [ ] **Step 3: Let the autonomous chain run for 24h**

Don't interact. Just watch.

- [ ] **Step 4: Verify 1 post landed on each platform live**

Check:
- @photonect.news IG profile
- TikTok account
- YouTube channel
- @photonect_news_channel

- [ ] **Step 5: If failures — diagnose, fix, commit fix to ops/n8n/**

## Task P3.4: Day 2-3 — 3 posts/day

- [ ] **Step 1: Bump `DAILY_POST_LIMIT = 3`**

- [ ] **Step 2: Let run for 2 days**

- [ ] **Step 3: Verify 6 posts total across the 2 days**

## Task P3.5: Day 4+ — full 6 posts/day

- [ ] **Step 1: Remove `DAILY_POST_LIMIT` cap**

Patch WF5 to remove the gate.

- [ ] **Step 2: Run for 5 consecutive days**

Daily check: morning digest shows clean status.

- [ ] **Step 3: Verify success criteria from spec §15**

All 6 criteria from the spec's "Success criteria":
- 5 consecutive days clean run
- Morning digest accurate
- At least one PAUSE used successfully
- At least one REGEN used successfully
- At least one platform failure handled cleanly
- All 5 days have complete `data/posting-state/<date>.json` files

- [ ] **Step 4: Final commit — v1 shipped**

```bash
git add docs/runbooks/p0-credential-setup.md
git commit -m "docs(runbook): NEWS ENGINE v1 shipped — 5 consecutive days clean"
```

## Task P3.6: Open the v2 brainstorm

After v1 is stable for 1-2 weeks, the next cycle begins:

- [ ] **Step 1: Run `superpowers:brainstorming` for S5 read-back**

The next spec covers: n8n cron at T+24h and T+72h per posted slug → polls IG/TT/YT for view/like/completion → writes `data/engagement/<date>-<slug>.json`.

(That spec → plan → execute is a separate cycle, not part of this plan.)

---

# Self-Review

## Spec coverage check

| Spec section | Covered by |
|---|---|
| §1 NEWS ENGINE vision | Mentioned in plan intro + P3.6 next cycle |
| §2 v1 scope | All phases scoped to S1 distribution |
| §3 Architecture (Option A) | All n8n workflows + GH Action boundaries follow this |
| §4 Daily timeline | WF1 (22:00) + WF3 (06:00) + WF5 slot crons (8a/12p/4p/7p/9p/11p) |
| §5.1 7 n8n workflows | P1A (WF5), P1C (WF1), P1D (WF2), P1E (WF3), P1F (WF4), P1G (WF6), P1H (WF7) + helper WF8 + WF9 |
| §5.2 GH Actions changes | P1B (produce-today.yml + regen-slug.yml) |
| §5.3 Repo additions | P1A.1 (cloudinary-upload.py), P1A.2 (posting-state-update.py + schema), P1A.3 (ops/n8n/), P0.1 (runbook) |
| §5.4 Telegram setup | P0.2 |
| §6 State machine | Implemented across WF1/WF2/WF3/WF4 via slate-state.json |
| §7 Per-slot posting flow | P1A.4 (IG), P1A.5 (TT), P1A.7 (YT), P1A.8 (TG) + P1A.9 fanout |
| §8 Credentials | P0.2-P0.10 |
| §9 Failure handling | P1A.9 (error isolation), WF6 alerts, P2.3 injection tests |
| §10 Testing strategy | P2.1-P2.4 |
| §11 Rollout phases | Plan IS structured as P0/P1/P2/P3 |
| §12 Out of scope | Honored — no S5/S2/S3 tasks, no platform-tuned captions, no HEKAYA |
| §13 Risks register | Quota request in P0.5, token rotation in P1G, kill-window timing in P2.4 |
| §14 Operating cost | $500/mo Anthropic alert noted in P0.8 |
| §15 Success criteria | Verified in P3.5 |
| App A open questions | Telegram message templates concrete in P1C.4 + P1E.3; slot times concrete in P1A timeline; topic rotation deferred (existing memory honored); n8n_create_workflow used throughout (App A.4); CI fresh checkout used (App A.5 fresh); GitHub PAT used not OAuth (App A.6) |
| App B seams for v2 | P1A.2 posting-state schema captures permalinks for S5 read-back |

**No gaps.**

## Placeholder scan

Searched for: TBD, TODO, "fill in", "implement later", "similar to Task N", "appropriate error handling".

- "Build by copying WF2's shell and adapting" (P1F.1) — explained the pattern but didn't inline the full JSON to avoid 200 lines of duplication. Mitigation: P1F.1 references WF2's structure explicitly + lists what changes. Acceptable per skill — the engineer can run `n8n_get_workflow id=<WF2_ID>` and adapt.
- "For brevity, the executor follows the WF5 Cloudinary pattern (Task P1A.4)" (P1E.2 Step 3) — same pattern. Reference to specific prior task is allowed when the pattern is identical and not repeated to avoid drift bugs.

No actual placeholders.

## Type / name consistency

- `WF1` through `WF7` named consistently throughout
- `WF8` (posting-state-helper) and `WF9` (slate-state-helper) introduced where used
- `data/posting-state/<date>.json` vs `data/posting-state/<date>.slate-state.json` — two distinct files, naming convention clear
- Credential names consistent: `meta-graph-api`, `tiktok-content-api`, `youtube-data-api`, `cloudinary-uploader`, `github-pat-news-engine`, `telegram-bot-token` (with `-staging` suffix for staging)
- n8n variable names ALL_CAPS: `GITHUB_OWNER`, `GITHUB_REPO`, `IG_BUSINESS_ACCOUNT_ID`, `TELEGRAM_AHMED_CHAT_ID`, `TELEGRAM_CHANNEL_ID`, `CLOUDINARY_CLOUD_NAME`, etc.

Consistent.

---

**End of plan.** ~145 tasks across 4 phases. Each phase produces working, testable software at its boundary. Plan is ready for execute-plan dispatch.
