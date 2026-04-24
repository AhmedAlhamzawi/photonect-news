---
name: produce-today
description: End-to-end daily Photonect NEWS production — research today's 12 stories, author Arabic props, hunt media, render reels with the current engine, run triple QA, output a ready-to-post DELIVERY_<date>.md. Run when Ahmed says "produce today" or presses the button.
allowed-tools: Bash, Read, Write, Edit, Glob, Grep, WebSearch, WebFetch, TodoWrite, Agent
---

# /produce-today — Unified daily production run

You are producing today's full Photonect NEWS slate in ONE manual run. No scheduled tasks. No partial output. When this command finishes, Ahmed must be able to post immediately.

## Invariants — non-negotiable

1. **Latest engine state only.** Use whatever the engine currently is in `my-video/src/compositions/NewsReel/` and `data/_template/`. Do NOT attempt engine fixes during production. Engine evolution happens in a separate session.
2. **Directional evolution gate.** Before generating the slate, diff today's plan against the most recent `DELIVERY_*.md` (yesterday or the last produced day). At least ONE of these must be visibly different: topic mix, variant distribution, bucket rotation pattern, beat pacing, supportingStat style, caption voice, visual treatment. If nothing meaningfully changes, stop and ask Ahmed what direction to push. Reference: `memory/feedback_engine_static.md`.
3. **12 slugs, 7 buckets, no two consecutive same bucket.** Buckets: mena_geopolitics, iraq_domestic, gulf_regional, europe, global_economy, tech_ai, wildcard. Slots: 08:00, 09:20, 10:40, 12:00, 13:20, 14:40, 16:00, 17:20, 18:40, 20:00, 21:20, 22:40 (GMT+3).
4. **Variant distribution.** Target ~4 A / ~4 B / ~4 C. Variant A = BAR money-shot, B = STRIKE kinetic-split, C = HAIRLINE cinema-reveal. Variant choice should match story type.
5. **Triple QA is a hard gate.** Every reel must pass luminance (per-variant floors), margin/safe-zone, and audio RMS > -50 dB. Any QA failure means that slug is NOT ready to post — flag it, do not hide it.
6. **Ahmed must never catch an error first.** Self-check the delivery doc before reporting done.

## Phases

### Phase 0 — Bootstrap (first tool calls)

Run in parallel:
- `date +%Y-%m-%d` to resolve today
- `ls data/posts/ | grep ^<date>` to see if slate already exists
- `ls -t DELIVERY_*.md | head -3` to find the last delivery for diffing
- `cat data/_template/ENGINE.md | head -50` to confirm current engine rev

Read the most recent DELIVERY to lock in what yesterday looked like — this is the baseline the new slate must visibly diverge from.

Write a TodoWrite plan with one todo per slug plus one for each phase gate.

### Phase 1 — Research + slate design

Skip this phase only if `data/posts/<date>-*` already has 12 complete props.json files.

1. Use WebSearch to pull today's real news across the 7 buckets. Query each bucket separately (one search per bucket minimum). Cross-reference dates — reject stories older than 24h.
2. Pick 12 stories. Enforce bucket rotation (no two consecutive same bucket). Enforce topic diversity across the day.
3. Pick the **directional shift** for today. Examples of valid shifts: new variant mix ratio, new beat-composition approach (e.g. data-led vs. scene-led), new caption format, a new typographic treatment rolled across all 12, a different pacing curve. Write the shift as one sentence at the top of the delivery doc.
4. For each slug, author Arabic content: `arabicDateLabel`, `breaking.arabicHeadline`, 3 beats each with `arabicHeading`, `arabicBody` (20-35 words), 3 `supportingStats` (value + label). Tech_ai posts MUST have numeric stats (phase-1 validator enforces this).
5. Write `data/posts/<date>-<slug>/props.json` matching `data/_template/props.template.json`. Set `variant`, `topicBucket`, `audioBed` per bucket map in `NewsReel.tsx`.
6. Parallelize slug generation: dispatch Agent calls per slug when the volume warrants it, but keep author voice consistent by reading the last 3 DELIVERY files first.

### Phase 2 — Media hunt

For each slug that lacks `broll/` assets:
```
bash data/_template/hunt-media.sh <slug>
```
Or manually populate `data/posts/<slug>/broll/{hero,beat1,beat2,beat3}.{jpg,mp4}` from the media-ledger or Wikipedia Commons.

Verify: every `beat.broll` path referenced in props.json exists on disk before rendering.

### Phase 3 — Render + triple QA (existing pipeline)

Delegate to the existing orchestrator:
```
bash generate-daily.sh <date>
```
This runs:
- Phase 1 validation (placeholders, required fields, tech_ai numeric stats)
- Phase 2 render (render-reel.sh v3 per slug)
- Phase 3 triple QA (ffmpeg frame extraction + PIL luminance + volumedetect RMS, variant-aware)
- Phase 4 writes DELIVERY_<date>.md

Stream the output. If any slug fails render or QA, do NOT abandon the slate — continue the rest, then surface failures in the final report.

### Phase 4 — Captions + posting plan

After render succeeds, generate IG captions per slug:
- Use the existing pattern in recent DELIVERY_*.md (hook + 3 pillars + 3 scenarios + sources + 15 hashtags + credit).
- Write captions into the DELIVERY markdown (append to each slug section).

Run `bash data/_template/build-posting-plan.sh <date>` if it exists and wire MD5 + file size references into the delivery.

### Phase 5 — Pre-flight self-check

Before telling Ahmed you are done, audit:
- [ ] 12/12 slugs have props.json, broll assets, rendered mp4
- [ ] 12/12 mp4 durations are 34.0s ± 0.5s
- [ ] 12/12 audio RMS in [-30, -15] dB (louder than silence, quieter than clipping)
- [ ] luminance report passes per-variant floors
- [ ] no two consecutive bucket repeats in posting order
- [ ] DELIVERY_<date>.md exists and has per-slug caption + MD5 + size
- [ ] one-sentence directional shift is stated at the top of DELIVERY

Any FAIL → fix before reporting done.

### Phase 6 — Report

Respond with:
1. `✅ 12/12 reels rendered, N/12 passed triple QA, ready to post.` (or the real numbers)
2. The directional shift summary (one sentence).
3. Link to `DELIVERY_<date>.md`.
4. Any QA warnings — which slugs, what failed, whether to post anyway or re-render.

Never report "done" if anything is incomplete. Say exactly what is missing.

## Notes for Claude

- If this is the first run where bootstrap is empty, follow the engine-evolver's run-1 bootstrap pattern: capture a fresh baseline for the canonical samples before rendering the slate.
- Prefer delegating heavy slug authoring to Agent subagents so the main context stays clean for coordination and QA judgment.
- Treat `memory/feedback_*.md` as binding guidance — especially `feedback_topic_diversity.md`, `feedback_video_pacing.md`, `feedback_card_opacity.md`, `feedback_engine_static.md`, `feedback_qa_checklist.md`.
- The Remotion project lives at `/Users/ahmed/Desktop/Claude <> Ahmed - 2nd Brain/Photonect/my-video/` — render-reel.sh handles paths; do not hardcode.
- Engine state is whatever `NewsReel.tsx` says. Do not fork or branch.
