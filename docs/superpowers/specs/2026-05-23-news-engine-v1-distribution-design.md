# Photonect NEWS ENGINE — v1 Distribution Layer (n8n Hybrid)

> **Status:** Design spec, approved 2026-05-23. Awaiting user file-level review before transition to implementation plan.
> **Author:** Brainstormed by Claude Opus 4.7 with Ahmed Alhamzawi via `superpowers:brainstorming`.
> **Next step:** `superpowers:writing-plans` to produce the executable plan; then `superpowers:execute-plan`.

---

## 1. NEWS ENGINE vision (frames what v1 must ENABLE, not what v1 SHIPS)

The long-term ambition is a self-evolving Photonect NEWS ENGINE. v1 is the first of four shipping cycles:

```
S4 News Intelligence   ──→   S1 Distribution   ──→   S5 Performance     ──→   S2 Auto-evolve
(research / author /         (THIS DOC — v1)         feedback                  config (music,
 photo / copywriter)         n8n cron, kill,         (read views, likes,       density, accent,
already exists at            4-platform fanout,      completion at             pacing) per signal
/produce-today               Telegram)               24h / 72h)                    ↓
                                                                              S3 Auto-development
                                                                              (Claude proposes
                                                                               components, opens
                                                                               PR, Ahmed approves)
```

**Each future subsystem will get its own brainstorm → spec → plan → execute cycle.** v1 must leave clean seams so S5 can plug in as a new n8n branch (24h/72h read-back per slug) without re-plumbing.

The historical "Photonect Engine Evolver" attempt (April 19, claude-mem 773-836) stalled because it tried to auto-evolve without a real audience signal. The lesson informing this sequencing: **auto-evolve is only valuable when closed with engagement data**, which requires distribution to exist first.

---

## 2. v1 scope (S1 only)

**Ships:** Full-autonomous distribution layer that takes a Claude-authored Arabic news slate and posts it to four platforms (Instagram, TikTok, YouTube Shorts, Telegram channel) on a fixed daily schedule, with two human safety gates and a Telegram operational dashboard.

**Does NOT ship:** Performance read-back (S5), auto-evolve (S2), auto-development (S3), platform-tuned captions, hashtag-per-platform optimization, multi-language, A/B testing, audience-time-zone slot optimization, HEKAYA integration, auto-recovery for bad live posts, an analytics dashboard.

**Daily volume:** 6 reels/day, fixed Baghdad slots, all 4 platforms per slot.

**Operator interactions per day:** maximum 2 (evening preview, morning kill window). Designed for zero-touch when the slate is good.

---

## 3. Architecture (Option A — n8n owns brain, GH Action renders)

n8n on Fly.dev (`photonect-n8n.fly.dev`) owns:
- All scheduling (cron triggers)
- All platform credentials (encrypted)
- All editorial-gate state (rejected slugs, paused slugs)
- All Telegram bot interactions
- All cross-posting fanout

GitHub Actions owns:
- Heavy ephemeral compute: `produce-today.yml` (Claude Code in CI) and `render-day.yml` (Remotion render, unchanged from current).

Repo owns:
- Authored slate (`data/posts/<date>-<slug>/`)
- Historical posting log (`data/posting-state/<date>.json`) — feeds S5 later
- Engine config (mood rotation, accent palette, density caps — unchanged)

Drive owns:
- Rendered `video.mp4` + `caption.txt` per slug (unchanged)

Cloudinary owns:
- Public mp4 URL per slug (only needed by Instagram Graph API, which cannot accept direct upload)

Platform APIs own:
- The actual posted permalinks (we read back via API and cache in `data/posting-state/<date>.json`)

**Rejected alternatives:**
- *Option B (GH Actions cron-driven, n8n cross-post only):* GitHub `workflow_schedule` is best-effort (5-30min late), kill-window needs a long-running waiting job (wasteful), Telegram integration is custom plumbing.
- *Option C (repo-as-source-of-truth):* Reinvents n8n's execution log. Concurrent-write messiness on `data/posting-state/<date>.json`. GitHub API rate limits hurt under retries.

---

## 4. Daily timeline (Baghdad time, no DST)

```
10:00 PM  ──┬── n8n cron fires WF1 evening-author
            │   POST GitHub Action: produce-today.yml dispatch
            │   Polls every 2min until Action completes (~10-15min)
            ↓
10:15 PM  ──┬── Slate committed to repo (6 slugs)
            │   Telegram preview message sent to Ahmed's DM:
            │     "Tomorrow's 6 stories — titles + hero thumbnails.
            │      Tap REJECT <slug> to drop · REGEN <slug> to re-research
            │      Locks at 5am if no reply."
            ↓
[overnight: Ahmed sleeps / interacts / ignores]
            │
05:00 AM  ──┬── Evening preview window CLOSES, slate locks (N ≤ 6 slugs)
            ↓
06:00 AM  ──┬── n8n cron fires WF3 morning-render
            │   POST render-day.yml dispatch with date param
            │   Polls every 2min until done (~30-40min)
            │   On success: downloads N video.mp4 + caption.txt from Drive
            │   Uploads each mp4 to Cloudinary (for IG public URL)
            ↓
06:45 AM  ──┬── Render done. Telegram kill-window message sent:
            │     "Posts going out in 60min. Thumbnails attached.
            │      Tap PAUSE to stop entire slate.
            │      Tap PAUSE <slug> to skip one."
            ↓
07:45 AM  ──┬── Kill window CLOSES, slate locks for the day (M ≤ N slugs)
            ↓
08:00 AM  ┐
12:00 PM  │ ── WF5 slot-posting fires for each slot. Parallel fanout per slot:
04:00 PM  │      → Instagram Graph API (container + publish, polls until FINISHED)
07:00 PM  │      → TikTok Content Posting API (direct upload)
09:00 PM  │      → YouTube Data API v3 (videos.insert with shorts metadata)
11:00 PM  ┘      → Telegram channel (sendVideo to @photonect_news_channel)
            │
[next morning 9:00 AM: WF7 daily-digest sends Telegram message:
   "Yesterday: 6/6 ran. IG 6 ok, TT 6 ok, YT 5 ok (1 quota fail), TG 6 ok.
    Permalinks attached. Failures: <slug X TT post failed at 4pm — manual recovery needed>."]
```

---

## 5. Components we build

### 5.1 n8n workflows (7)

| # | Workflow | Trigger | Notes |
|---|---|---|---|
| **WF1** | `evening-author` | Cron `0 22 * * * Asia/Baghdad` | Dispatches `produce-today.yml`, polls, sends Telegram preview |
| **WF2** | `evening-callback` | Telegram webhook | REJECT/REGEN handlers; REGEN dispatches `regen-slug.yml`, updates preview in place |
| **WF3** | `morning-render` | Cron `0 6 * * * Asia/Baghdad` | Dispatches `render-day.yml`, polls, downloads from Drive, uploads to Cloudinary, sends kill-window preview |
| **WF4** | `kill-window-callback` | Telegram webhook | PAUSE / PAUSE \<slug\> handlers, updates n8n vars |
| **WF5** | `slot-posting` | 6 cron triggers (8a/12p/4p/7p/9p/11p Baghdad) | Per fire: read slate from vars, skip paused, parallel fanout to 4 platforms, write per-slot result to `data/posting-state/<date>.json` via GitHub Contents API |
| **WF6** | `rotate-tokens` | Cron `0 3 * * 1 Asia/Baghdad` (weekly Monday 3am) | Refreshes Meta 60-day token if within 14d of expiry; Telegram-alerts on failure |
| **WF7** | `daily-digest` | Cron `0 9 * * * Asia/Baghdad` | Sends yesterday's per-platform success/fail Telegram message with permalinks |

### 5.2 GitHub Actions changes

| File | Status | Purpose |
|---|---|---|
| `.github/workflows/render-day.yml` | **unchanged** | Already takes `date` workflow_dispatch input |
| `.github/workflows/produce-today.yml` | **NEW** | Runs `claude --print '/produce-today --date <date> --autonomous'` in CI with `ANTHROPIC_API_KEY` secret. Commits slate to `data/posts/`. |
| `.github/workflows/regen-slug.yml` | **NEW** | Re-runs research+author+photos+copywriter for one slug only. Commits update. |

### 5.3 Repo additions

```
data/posting-state/
  2026-05-23.json    ← per-slug per-platform status + permalinks + timestamps
                       ONE file per day, updated incrementally after each slot
                       fires via GitHub Contents API (read SHA → merge → commit).
                       Status values: pending | ok | failed | skipped
                         pending  = slot fired, platform call in flight
                         ok       = platform call succeeded, permalink captured
                         failed   = platform call failed after retries, error logged
                         skipped  = slug was PAUSED in kill window before this platform
                       Schema:
                       {
                         "date": "2026-05-23",
                         "slugs": {
                           "<slug>": {
                             "slot": 1,
                             "ig":       {"status": "ok",     "permalink": "...",      "ts": "..."},
                             "tiktok":   {"status": "ok",     "permalink": "...",      "ts": "..."},
                             "yt":       {"status": "failed", "error": "quota exceeded","ts": "..."},
                             "telegram": {"status": "ok",     "permalink": "t.me/...", "ts": "..."}
                           }, ...
                         }
                       }

.github/workflows/
  produce-today.yml     ← new
  regen-slug.yml        ← new

(No new automation/scripts/ files — Claude Code wraps the existing skill in CI.)
```

### 5.4 Telegram setup

- **New bot via @BotFather:** `@photonect_news_bot`
- **Two destinations:**
  - Ahmed's personal DM — evening preview, kill-window, daily digest, error alerts
  - Public channel `@photonect_news_channel` — cross-post destination for actual reels
- **Required bot capabilities:** `sendPhoto`, `sendVideo`, `editMessageText` (for in-place preview updates), webhook for inline button callbacks
- **Inline buttons used (NOT slash commands or typed text):** REJECT/REGEN per slug on preview, PAUSE/PAUSE-this on kill window, RETRY/MANUAL_OVERRIDE on errors. n8n Telegram Trigger node listens on `callback_query` updates from the Bot API; each button carries `callback_data` like `reject:<slug>` or `pause:<slug>` that the workflow switch routes on.

---

## 6. State machine

```
empty
   ↓ [10pm cron]
producing  ──→ Telegram preview sent
   ↓
pending_evening_lock                    ┌── REJECT <slug> → drop slug
   ↓ [Ahmed interacts or doesn't] ─────┤
   ↓                                    └── REGEN <slug> → re-author, update preview
   ↓ [5am evening window closes]
evening_locked  (N ≤ 6 active slugs)
   ↓ [6am cron]
rendering
   ↓ [render-day.yml + Drive download + Cloudinary upload]
pending_kill_window  ──→ Telegram kill message sent
   ↓                                    ┌── PAUSE → kill ALL for day
   ↓ [Ahmed interacts or doesn't] ─────┤
   ↓                                    └── PAUSE <slug> → drop one
   ↓ [7:45am kill window closes]
posting_locked  (M ≤ N active slugs)
   ↓ [slot crons fire at 8a/12p/4p/7p/9p/11p]
posting  (per slot: parallel fanout to 4 platforms)
   ↓ [each slot writes data/posting-state/<date>.json]
complete
   ↓ [next morning 9am digest]
```

**State ownership:**
- n8n executions: ephemeral schedule/kill/reject flags (lives in workflow variables, retained 30 days)
- Repo: durable per-day audit log at `data/posting-state/<date>.json` (written after each slot completes)

---

## 7. Per-slot posting flow

```
slot fires (e.g., 8:00 AM)
   │
   ├──────────────────────────┐
   ↓                          ↓
[upload mp4 to            [fetch caption.txt
 Cloudinary, get           from Drive]
 public URL]                  │
   ↓                          ↓
   ├──── 4 parallel branches ──────────────────────────┐
   ↓                ↓               ↓                  ↓
[Instagram     [TikTok        [YouTube           [Telegram
 Graph API]    Content API]    Data API v3]      Bot API]
   ↓                ↓               ↓                  ↓
 container         direct          videos.insert      sendVideo
 → publish         upload          (shorts metadata)  to channel
   ↓                ↓               ↓                  ↓
   └────── all 4 results aggregated ───────────────────┘
   ↓
[commit per-slot result to data/posting-state/<date>.json via GitHub Contents API]
   ↓
[on any platform failure: Telegram alert + retry per failure policy below]
```

**Idempotency:** before each platform call, check `data/posting-state/<date>.json` — if `{slug, platform}` already has a permalink, skip that branch. Retries are safe.

---

## 8. Credentials & secrets

| Credential | Lives in | Rotation | Scope |
|---|---|---|---|
| `ANTHROPIC_API_KEY` | GH secrets | Anthropic console | `produce-today.yml` + `regen-slug.yml` only |
| `DRIVE_OAUTH_JSON` (exists) | GH secrets | gcloud CLI | `render-day.yml` only |
| `DRIVE_PARENT_FOLDER_ID` (exists) | GH secrets | static | `render-day.yml` only |
| `GITHUB_TOKEN_N8N` (PAT for n8n → repo) | n8n credentials | GitHub PAT settings | `workflow:write` + `actions:read` + `contents:write` (for posting-state commits) |
| `META_LONG_LIVED_USER_TOKEN` | n8n credentials | **WF6 auto-rotates weekly** (60-day token, refresh at 50d) | `instagram_basic` + `instagram_content_publish` |
| `IG_BUSINESS_ACCOUNT_ID` | n8n vars | static | — |
| `TIKTOK_ACCESS_TOKEN` | n8n credentials | TikTok dev console | content posting |
| `YOUTUBE_OAUTH_REFRESH_TOKEN` | n8n credentials | GCP console | `youtube.upload` + `youtube.readonly` |
| `TELEGRAM_BOT_TOKEN` | n8n credentials | @BotFather | per-bot |
| `TELEGRAM_AHMED_CHAT_ID`, `TELEGRAM_CHANNEL_ID` | n8n vars | static | — |
| `CLOUDINARY_API_KEY` + `CLOUDINARY_API_SECRET` + `CLOUDINARY_CLOUD_NAME` | n8n credentials | Cloudinary dashboard | upload + signed URL generation |

**Security principles:**
- Least-privilege scopes on every token
- n8n stores credentials encrypted at rest (Fly.dev secrets + n8n's own encryption)
- No secret appears in repo, in exported workflow JSON, or in any log line
- Token rotation cron (WF6) alerts on failure via Telegram

---

## 9. Failure handling

| Failure mode | Behavior |
|---|---|
| One platform fails for one slot | 3 retries with 60s backoff. Then skip + Telegram alert. Other 3 platforms in same slot proceed. Other slots unaffected. |
| All 4 platforms fail for one slot | Retry once after 5min. Then Telegram alert + skip slot. Other slots continue. |
| Render fails (`render-day.yml` non-zero exit) | n8n catches via poll. Telegram error with Action log URL. Slate is staged but won't post. Recovery: re-trigger from GH mobile, tap "RESUME POSTING" in Telegram. |
| `/produce-today` CI fails | Telegram error. Recovery: tap RETRY (n8n re-dispatches) or run /produce-today on laptop + tap MANUAL_OVERRIDE in Telegram (n8n reads slate from repo and skips authoring). |
| n8n Fly.dev outage | Nothing fires. v1 has no fallback (deferred to v2 GH cron). Recovery: bring n8n back, manually re-trigger pending workflows from n8n UI. |
| Already-posted retry (idempotency) | WF5 checks `data/posting-state/<date>.json` per-platform before each call — skips if permalink exists. |
| Bad post slips past both gates and goes live | Manual recovery — Ahmed deletes from each platform. v1 does not auto-recover. The 2-gate design (evening + morning) is the primary mitigation. |

**Explicit non-recovery:**
- v1 does NOT auto-retry the day's slate after midnight. If today mostly failed, slate is forfeit; tomorrow runs fresh.
- v1 does NOT auto-republish to a different account on quota exhaustion.

---

## 10. Testing strategy

**Pre-launch (staging accounts):**
1. **Per-platform smoke test** — each platform's posting node tested against a STAGING IG/TT/YT account + a private Telegram test channel with a single canned mp4. Manual approve per platform.
2. **End-to-end dry-run** — full daily cycle with all platforms targeting staging, captions `[TEST]` prefixed.
3. **Kill window test** — trigger morning render, tap PAUSE during kill window, confirm slate doesn't post. Repeat with PAUSE \<slug\> to confirm scoped suppression.
4. **Failure injection** — disable TikTok credential mid-slate, confirm IG/YT/Telegram proceed and TikTok logs Telegram alert.

**Live cutover (progressive):**
- Day 1: 1 post only (manually staged single-slug slate), all 4 platforms, observe.
- Days 2-3: 3 posts/day.
- Day 4+: Full 6.

---

## 11. Rollout phases

| Phase | Sessions | Ships |
|---|---|---|
| **P0** Account + credential setup | 1-2 | Telegram bot via @BotFather; Meta dev app + long-lived IG token; TikTok dev app + access token; YouTube channel + OAuth refresh token via GCP; Cloudinary account; staging IG/TT/YT accounts; n8n credential entries populated |
| **P1** Workflow construction | 2-3 | WF5 (slot-posting) built first targeting staging accounts; WF1/WF3 (cron triggers); WF2/WF4 (Telegram callbacks); WF6 (token rotation); WF7 (daily digest); new `.github/workflows/produce-today.yml` + `regen-slug.yml` |
| **P2** Integration test | 1 | Full dry-run on staging; failure injection per §10; kill-window tests per §10 |
| **P3** Live cutover | ~1 week | Switch n8n credentials from staging to live; 1-post day → 3-post days → 6-post days |
| **Total** | **~4-7 sessions to ship v1** | |

---

## 12. Out of scope for v1 (explicit — do not let these creep in)

- ❌ **S5 read-back** (view/like/completion metrics) — separate brainstorm cycle
- ❌ **S2 auto-evolve** (config deltas from signal) — separate cycle
- ❌ **S3 auto-development** (Claude proposes components) — separate cycle
- ❌ Platform-tuned captions — v1 uses single `caption.txt` everywhere
- ❌ Hashtag optimization per platform — embedded in caption only
- ❌ Multi-language posting — Arabic-only
- ❌ A/B variant testing
- ❌ Audience-time-zone-optimized slots — fixed Baghdad clock
- ❌ HEKAYA track integration — separate workflow, separate plan
- ❌ Auto-recovery for bad live posts — Ahmed deletes manually
- ❌ Analytics dashboard — Telegram digest only
- ❌ GH Actions cron as n8n fallback — deferred to v2
- ❌ Per-slot kill window (instead of single morning kill) — single kill is simpler

---

## 13. Risks register

| Risk | Likelihood | Mitigation |
|---|---|---|
| **YouTube quota** (1600 units × 6 uploads = 9,600 of 10K daily — retries push us over) | High | Request 50K quota increase from Google during P0. Cache permalinks (idempotent retries don't re-upload). |
| Meta 60-day token expiry | Certain | WF6 rotates weekly. Telegram alert on rotation failure. |
| TikTok rate limits (often surprising) | Medium | Per-platform backoff. Skip+alert pattern. |
| n8n Fly.dev outage | Low | v1 has no fallback. Documented manual recovery. v2 could add GH cron fallback. |
| Bad post slips past both gates and goes live | Low | 2-gate design (evening + morning) catches most. Manual delete recovery. |
| Claude API cost spike (>$500/mo) | Medium | Anthropic console hard alert at $500/mo. |
| `/produce-today` flaky in CI | Medium | Headless Claude Code validated in P0. Fallback: manual /produce-today on laptop + MANUAL_OVERRIDE button. |
| n8n workflow corrupts slate | Low | Repo is git-versioned. Recovery: revert + re-trigger. |
| Cloudinary bandwidth cost spike | Low-Medium | 6 reels × 30 days × 30MB = 5.4 GB/mo egress; well within free tier (25 GB/mo on Cloudinary free). Monitor. |

---

## 14. Operating cost (monthly)

| Item | Cost |
|---|---|
| n8n on Fly.dev (already paid) | $5-10/mo |
| Claude API for daily `/produce-today` + occasional regen | $150-450/mo |
| GitHub Actions render | Free if public repo, ~$50/mo if private (30min × 30 days × $0.008/min) |
| Drive, Telegram Bot API, IG/TT/YT APIs (within quotas) | Free |
| Cloudinary (within free 25 GB egress) | Free |
| **Total** | **~$200-500/mo for full autonomy** |

---

## 15. Success criteria (v1 is shipped when…)

- ✅ 5 consecutive days of full autonomous posting: evening preview at 22:00, slate authored unattended, kill window at 06:45, all 6 slots fire on schedule, all 4 platforms receive each post (modulo per-platform skips with logged alerts)
- ✅ Daily digest message at 09:00 shows clean status for previous day
- ✅ At least one PAUSE \<slug\> interaction has been used successfully (proves kill window works under load)
- ✅ At least one REGEN \<slug\> interaction has been used (proves evening preview re-authoring works)
- ✅ At least one platform failure has occurred and been alerted, with all other platforms posting cleanly (proves fail-isolation)
- ✅ `data/posting-state/<date>.json` files exist for all 5 days with complete per-platform per-slug permalinks

When all six are met, v1 is considered shipped and we open the brainstorm cycle for **S5 (performance read-back)**.

---

## Appendix A — open questions deferred to implementation plan

These will be answered concretely in the writing-plans phase:

1. Exact Telegram message templates (Arabic? English? bilingual? Markdown? plain?)
2. Exact slot times — 8a/12p/4p/7p/9p/11p is the proposal; can be tuned during P3
3. Concrete topic-bucket rotation algorithm (current is documented in [memory feedback_topic_diversity.md](/Users/ahmed/.claude/projects/-Users-ahmed-Desktop-Photonect-NEWS-NEWS-CODE/memory/feedback_topic_diversity.md))
4. Whether to use `n8n_create_workflow` MCP for initial workflow construction, or build by hand in n8n UI then export
5. Whether produce-today.yml runs on a fresh checkout or persistent cache (affects Claude Code first-run cost)
6. Specific GitHub PAT vs n8n's GitHub OAuth credential (PAT is simpler, OAuth has finer audit)

---

## Appendix B — seams for v2 (S5 — read-back)

When v2 is built, the seams already in place:

- `data/posting-state/<date>.json` has per-platform permalinks → S5 polls platform APIs with these
- n8n already has Instagram/TikTok/YouTube credentials → reuse for `_insights` endpoints
- A new n8n workflow `WF8 read-back` runs at T+24h and T+72h per slug, writes to `data/engagement/<date>-<slug>.json`
- No code change needed in v1 components

---

**End of spec.** Awaiting Ahmed's file-level review before transition to `superpowers:writing-plans`.
