# Self-Prompt — Build the 2h Rotating Posting Routine + a Clear Manual-Posting Output File

> Written 2026-04-18. Meta-brief for executing the "rotate topics every 2 hours and give Ahmed a dead-simple file to post from" task. Self-contained: a fresh session plus this repo should be enough to carry it out.

---

## Who you are

You are the autonomous content operator for **@photonect.news**, an Arabic-first Instagram + TikTok news channel owned by Ahmed (ahmed@photonect.net). Ahmed posts every upload **manually** — he pulls the rendered video file and pastes the caption himself, on both platforms. You do **not** have IG or TikTok credentials and **must not** attempt to post on his behalf.

## Why this task exists

You already render great reels. What's broken is the **last mile**:
- `SHOWCASE.md` has a suggested 2h cadence table, but it's prose — Ahmed has to mentally map "slot 3" → "which folder" → "open props.json to get the Arabic hook" → "find caption.txt" → "copy paste into IG".
- The cadence isn't enforced against the **topic-diversity mandate** (no two consecutive posts from the same bucket — see [feedback_topic_diversity.md](~/.claude/projects/-Users-ahmed-Desktop-Photonect-NEWS-NEWS-CODE/memory/feedback_topic_diversity.md) in memory).
- There is no reusable *rotation logic* — the SHOWCASE table was hand-picked once and won't regenerate when tomorrow's reels land.

Ahmed's verbatim ask: *"where is the routine that will post a different topic every two hours? also the output file should be very clear to me so I don't get lost when I post on my pages manually."*

## Hard constraints (read before you type anything)

1. **No automated posting.** Producing a *plan*, not a *publisher*. Refuse if anything in scope drifts toward `curl`/`POST` against IG or TikTok endpoints.
2. **Architectural Fix Mandate** (memory: `feedback_architectural_mandate.md`). The rotation logic must live in one place and benefit *every future day* — do not hard-code `2026-04-17` into the routine.
3. **Topic-diversity mandate** (memory: `feedback_topic_diversity.md`). The rotation must enforce "no two consecutive posts from the same bucket." The 7 buckets: `mena_geopolitics`, `iraq_domestic`, `gulf_regional`, `europe`, `global_economy`, `tech_ai`, `wildcard`.
4. **No new .md files unless they serve the user-facing posting flow.** Ahmed should see the posting plan first; internal logs are secondary.
5. **Keep shell scripts in `data/_template/`** alongside the existing three helpers (`new-reel.sh`, `queue-status.sh`, `render-reel.sh`).
6. **Arabic-first output.** Any headline/hook shown to Ahmed in the plan is the Arabic one. English subhead is supplementary.

## Context you need from the repo

- `data/posts/<slug>/props.json` — single source of truth for headline, beats, big stats, sources. Each reel's **topic bucket is not stored explicitly today** — you'll need to add a `topicBucket` field to props.json (architectural change) and backfill the existing 6 reels. Every future `new-reel.sh` scaffold must include it.
- `data/posts/<slug>/caption.txt` — ready-to-paste IG/TikTok copy. Arabic hook + body + hashtags.
- `data/posts/<slug>/newsreel*.mp4` — video. Latest variant precedence: v3 > v2 > v1 (same logic as `queue-status.sh` line 20-22).
- [SHOWCASE.md](SHOWCASE.md) — currently holds the suggested cadence; after this task, it remains a human-readable overview but the *posting plan* lives elsewhere.
- [AUTONOMOUS_LOG_2026-04-17.md](AUTONOMOUS_LOG_2026-04-17.md) — context on what's in the queue right now.
- Memory files of interest: `project_photonect_news.md`, `feedback_topic_diversity.md`, `feedback_architectural_mandate.md`, `feedback_newsreel_approved.md`, `reference_captions_format.md`.

## The two deliverables

### Deliverable 1 — `data/_template/build-posting-plan.sh`

A shell script that:

1. Takes optional args: `--date YYYY-MM-DD` (default = today), `--start HH:MM` (default = 12:00 GMT+3), `--interval 2h`.
2. Walks `data/posts/<date>-*/` directories.
3. For each slug: reads `props.json` (via `jq`), picks the latest rendered video file, extracts:
   - Arabic headline (`breaking.arabicHeadline`)
   - English subhead (`breaking.englishSubhead`)
   - `topicBucket` (new field — if missing, print a clear error with the slug and exit non-zero so Ahmed knows what to fix)
   - First-beat big stat (`beats[0].bigStat.value` + `arabicLabel`) for the hook
4. **Orders the slots** so that no two consecutive posts share a `topicBucket`. If the mix makes this impossible, report the conflict instead of silently breaking the rule.
5. Writes the plan to `data/posts/POSTING_PLAN_<date>.md` (user-facing) — see Deliverable 2.
6. Also prints a one-line summary to stdout: `6 slots scheduled 12:00→22:00 GMT+3 — buckets: mena→iraq→mena→tech→mena→mena`.

**Why a shell script (not Python or a Node thing):** the rest of `data/_template/` is bash + jq, and Ahmed has approved that toolchain. Stay consistent.

### Deliverable 2 — `data/posts/POSTING_PLAN_<date>.md`

The file Ahmed actually opens at posting time. It must be copy-paste-friendly on a phone. Format for each slot:

```markdown
## Slot 3 — 16:00 GMT+3

**Bucket:** mena_geopolitics
**Arabic hook:** ١٠٠ ساعة تفصل واشنطن وطهران عن نقطة اللاعودة
**One-line angle (EN):** US–IRAN TALKS • 100h TO DEADLINE
**Big stat to tease in story:** APR 21 (deadline)

### 📹 Upload this video
`data/posts/2026-04-17-iran-talks/newsreel.mp4` (28 MB, 30s)

### 📋 Paste this caption
<details><summary>Tap to expand (copy everything between the lines)</summary>

```
<full caption.txt content inlined here>
```
</details>

### #️⃣ Hashtags (already included above — don't double-paste)
#إيران #أمريكا #هرمز #حرب_الخليج …

---
```

At the top of the file, put a masthead:

```markdown
# Posting Plan — 2026-04-17 (Fri)

**Channel:** @photonect.news · IG + TikTok · Arabic-first
**Total slots:** 6 · **Window:** 12:00 → 22:00 GMT+3 · **Interval:** 2h

| # | Time | Slug | Bucket | Video size |
|---|------|------|--------|------------|
| 1 | 12:00 | 2026-04-17-hormuz-week2 | mena_geopolitics | 38M |
| 2 | 14:00 | 2026-04-17-iraq-blackout | iraq_domestic | 25M |
| ... |
```

This top table is the glanceable index; the per-slot sections below are the copy-paste details.

### Backfill `topicBucket` in the 6 existing reels

Touch each `data/posts/2026-04-17-*/props.json` and add `"topicBucket": "<bucket>"` at the root. Use this mapping (derived from SHOWCASE.md and the conversation history):

- `2026-04-17-hormuz-week2` → `mena_geopolitics`
- `2026-04-17-iran-talks` → `mena_geopolitics`
- `2026-04-17-lebanon-ceasefire` → `mena_geopolitics`
- `2026-04-17-flight-aftermath` → `mena_geopolitics`
- `2026-04-17-ai-hundred-billion` → `tech_ai`
- `2026-04-17-iraq-blackout` → `iraq_domestic`

Also update `data/_template/props.template.json` to include `"topicBucket": "{{TOPIC_BUCKET}}"` and update `new-reel.sh` to accept/prompt for the bucket.

### Acceptance tests (run these, don't just assume)

1. `bash data/_template/build-posting-plan.sh --date 2026-04-17` produces `data/posts/POSTING_PLAN_2026-04-17.md` without errors.
2. `POSTING_PLAN_2026-04-17.md` has **exactly 6 slots**, starts at **12:00**, ends at **22:00**, interval 2h.
3. No two consecutive slots share a `topicBucket`.
4. Every slot references a file that actually exists (`ls` proves it).
5. Every caption block in the plan file matches its source `caption.txt` byte-for-byte (no truncation, no escaping errors — Arabic must round-trip cleanly).
6. Running the script on a day with no reels (`--date 2030-01-01`) exits non-zero with a clean "no reels found for date" message, not a cryptic jq error.

## Creative discretion you have

- The masthead emoji / icon choices.
- Whether to add a "Why this slot" reminder pulled from SHOWCASE.md per entry.
- Whether to add a "✅ Posted?" checkbox Ahmed can tick manually.
- Whether to also emit a `POSTING_PLAN_<date>.txt` (plain text) version for terminals without Markdown rendering.

Keep additions in service of the "don't get lost when posting" goal — cut anything that doesn't.

## What to return to Ahmed

After execution:
1. One sentence: "Built. Open `data/posts/POSTING_PLAN_2026-04-17.md`."
2. The rotated bucket sequence (e.g. `mena → iraq → mena → tech → mena → mena` — if the last-two-are-mena case is unavoidable, flag it).
3. The next-day invocation he'd use: `bash data/_template/build-posting-plan.sh --date 2026-04-18`.

No victory lap.

---

**End of self-prompt.** Execute now, don't ask for clarification — the brief is complete.
