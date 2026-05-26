---
name: produce-today
description: End-to-end daily Photonect NEWS production — research 6 signal-only stories, author Arabic props, hunt media, render reels with the current engine, run triple QA, output a ready-to-post DELIVERY_<date>.md. Run when Ahmed says "produce today" or presses the button.
allowed-tools: Bash, Read, Write, Edit, Glob, Grep, WebSearch, WebFetch, TodoWrite, Agent
---

# /produce-today — Unified daily production run

You are producing today's full Photonect NEWS slate in ONE manual run. No scheduled tasks. No partial output. When this command finishes, Ahmed must be able to post immediately.

## Invariants — non-negotiable

1. **Latest engine state only.** Use whatever the engine currently is in `my-video/src/compositions/NewsReel/` and `data/_template/`. Do NOT attempt engine fixes during production. Engine evolution happens in a separate session.
2. **Directional evolution gate.** Before generating the slate, diff today's plan against the most recent `DELIVERY_*.md`. At least ONE of these must be visibly different: topic mix, variant distribution, bucket rotation pattern, beat composition approach, supportingStat style, caption voice, visual treatment. If nothing meaningfully changes, stop and ask Ahmed what direction to push. Reference: `memory/feedback_engine_static.md`.
3. **6 slugs, ≥4 buckets, no two consecutive same bucket.** Buckets: mena_geopolitics, iraq_domestic, gulf_regional, europe, global_economy, tech_ai, wildcard. At least 1 slug MUST be iraq_domestic. Music mood cycles [cinematic → newsroom → orchestral → mideast → cinematic → newsroom] by slot order — run the rotation script after slugs are created.
4. **Signal only. Unbiased only.** Every story must pass the editorial mandate in `memory/feedback_editorial_mandate.md`. Signal = structural event with lasting consequences + ≥2 named sources + <24h. Noise = rumors, tweets, repackaged yesterday, unattributed "sources say". Reject noise at selection time, not after authoring.
5. **Variant distribution.** Target ~2 A / ~2 B / ~2 C across 6 slugs. Match variant to story type: A = political/conflict money-shot, B = data/tech kinetic, C = feature/wildcard cinema.
6. **Triple QA is a hard gate.** Every reel must pass luminance (per-variant floors), margin/safe-zone, and audio RMS > -50 dB. Any QA failure = that slug is NOT ready to post. Flag it. Do not hide it.
7. **Ahmed must never catch an error first.** Self-check the delivery doc before reporting done.

---

## Phases

### Phase 0 — Bootstrap (first tool calls, run in parallel)

- `date +%Y-%m-%d` to resolve today's date
- `ls data/posts/ | grep ^<date>` to see if any slugs already exist
- `ls -t DELIVERY_*.md 2>/dev/null | head -3` to find the last delivery for diffing
- `cat data/_template/ENGINE.md 2>/dev/null | head -30` to confirm engine rev

Read the most recent DELIVERY to lock in what yesterday looked like — today's slate must visibly diverge from it. Note the previous bucket sequence, variant distribution, and mood rotation.

Write a TodoWrite plan: one todo per slug + one per phase gate.

---

### Phase 1 — Story Research (signal-only)

Skip if `data/posts/<date>-*` already has 6 complete props.json.

**Step 1 — Query each bucket separately.** Run one WebSearch per bucket, limited to the last 24h:
- mena_geopolitics: regional conflict, diplomacy, sanctions, US/Iran/Israel/Lebanon/Syria/Yemen
- iraq_domestic: Baghdad politics, PMO, parliament, budget, oil, electricity, water, security
- gulf_regional: Saudi/UAE/Qatar/Kuwait domestic + trade, Vision 2030, OPEC+
- europe: EU policy, energy, migration, NATO — only if direct MENA impact exists
- global_economy: oil prices, Fed/ECB decisions, IMF/World Bank — only with explicit Iraq/Gulf angle
- tech_ai: AI regulation, deployment in Arab markets, GCC tech — only if regional relevance
- wildcard: infrastructure breakthroughs, water/climate/disaster, culture with news peg

**Step 2 — Score and filter.** For each candidate story:
- Has ≥2 independent named sources? If no → reject
- Is it <24h old with a new development? If no → reject
- Does it have structural, lasting consequences? If no → reject
- Does it pass the "signal not noise" test from `memory/feedback_editorial_mandate.md`? If no → reject

**Step 3 — Select 6 stories.** Enforce:
- No two consecutive same bucket
- ≥1 iraq_domestic
- Mix at least 4 different buckets
- Document WHY each story is signal (one sentence per slug in your working notes)

---

### Phase 2 — Slate Design + Props Authoring

For each slug, author props.json matching `data/_template/props.template.json`.

**Arabic copy rules (read `memory/feedback_editorial_mandate.md` §2 before writing):**
- `arabicHeadline`: ≤8 words, fact-first, no loaded adjectives, no verb "يشتعل/ينفجر" unless literal
- `arabicBody` per beat: 20–35 words. Every sentence has a source attribution embedded
- `supportingStats`: 3 stats with real numbers from named sources — values + Arabic labels
- `subtitlePhrases`: REMOVED (V9). Do not include in props.
- No `voScript`, `voicePath`, `voiceDurationSeconds` — VO is dead (V9)

**Field checklist per slug:**
```json
{
  "dateLabel": "MAY 26",
  "arabicDateLabel": "٢٦ مايو",
  "handle": "@photonect.news",
  "audioBed": "← set by rotation script, do not guess",
  "variant": "A|B|C",
  "topicBucket": "one of the 7 buckets",
  "breaking": { "arabicKicker": "عاجل", "arabicHeadline": "...", "englishSubhead": "...", "heroMedia": "...", "heroMediaType": "image" },
  "beats": [ 3 beats with arabicHeading + arabicBody + broll + brolls[] + brollSource + supportingStats ],
  "sources": [ 3–8 named sources with domain ],
  "arabicTicker": [ 3–8 short Arabic fact strings ]
}
```

**Music rotation — mandatory step after all props.json are written:**
```bash
python3 automation/scripts/assign-mood-rotation.py <date>
```
This overwrites `audioBed` in every slug deterministically (slot 0→cinematic, 1→newsroom, 2→orchestral, 3→mideast, 4→cinematic, 5→newsroom). Run it. Verify output shows 6 slugs updated. Do NOT manually set audioBed before running this.

**Iraqi-copywriter pass — mandatory for every slug:**
Invoke the `iraqi-copywriter` agent on each slug's props.json before proceeding. This ensures kicker/headline/subhead/beats hit Arabic broadcast standards. No slug goes to render without this pass.

---

### Phase 3 — Media Hunt

For each slug, ensure 4 images exist: `images/news/<slug>/hero.jpg`, `broll_1.jpg`, `broll_2.jpg`, `broll_3.jpg`

Set `brolls` in each beat to a 3-4 image array from that slug's folder. MultiShotBackdrop will cycle them at ~3.25s/shot.

Source priority:
1. Pexels / Unsplash (free, no attribution required)
2. Wikimedia Commons (CC license, attribute in brollSource)
3. AP / Reuters embed if available via news search

Verify: every `beat.broll` and `brolls[]` path exists on disk before moving to render. Missing asset = render will fail.

---

### Phase 4 — Render + Triple QA

```bash
bash generate-daily.sh <date>
```

This runs Phase 1 validation → render (Remotion, 1410 frames / 47s per slug) → triple QA → writes DELIVERY_<date>.md.

Stream output. If any slug fails, continue the rest, then surface failures in the final report. V9 engine — do NOT check for 34s duration. Correct duration is **47.0s ± 0.5s** (1410 frames at 30fps).

---

### Phase 5 — Captions + Posting Plan

After render succeeds, generate IG caption per slug:
- Hook (1 line, stops the scroll — a number or a question, in Arabic)
- 3 fact bullets (translated from the beats, cited)
- 3 "what this means for you" points
- 3 named sources
- 15 Arabic/bilingual hashtags
- Credit: @photonect.news

Append captions to DELIVERY_<date>.md, one section per slug.

---

### Phase 6 — Pre-flight Self-Check

Before telling Ahmed you are done:

- [ ] 6/6 slugs have props.json with correct fields (no voScript, no subtitlePhrases)
- [ ] 6/6 props.json have audioBed set by rotation script (not manually)
- [ ] 6/6 slugs passed iraqi-copywriter pass
- [ ] 6/6 slugs have 4 images on disk
- [ ] 6/6 mp4 durations are **47.0s ± 0.5s**
- [ ] 6/6 audio RMS in [-30, -15] dB
- [ ] Luminance passes per-variant floors
- [ ] No two consecutive bucket repeats in posting order
- [ ] ≥1 iraq_domestic slug in the slate
- [ ] Every story in the slate passes editorial mandate (signal, sourced, <24h)
- [ ] DELIVERY_<date>.md exists with per-slug caption + MD5 + size
- [ ] One-sentence directional shift stated at top of DELIVERY

Any FAIL → fix before reporting done.

---

### Phase 7 — Report

```
✅ 6/6 reels rendered, N/6 passed triple QA, ready to post.
Directional shift: <one sentence>.
Editorial note: <which buckets covered, any signal highlights>.
→ DELIVERY_<date>.md
Warnings (if any): <slug, issue, recommendation>.
```

Never report "done" if anything is incomplete. Say exactly what is missing.

---

## Engine State Reference (V9, 2026-05-26)

| Parameter | Value |
|-----------|-------|
| Total frames | 1410 (47s at 30fps) |
| Breaking | 150f (5s) |
| Beat 1 / 2 / 3 | 390f each (13s each) |
| Sources | 90f (3s) |
| VO | ❌ Removed |
| SubtitleBar | ❌ Removed |
| MultiShotBackdrop | ✅ 4 shots × 97.5f = 3.25s/shot |
| Music moods | cinematic / newsroom / orchestral / mideast |
| Rotation script | `automation/scripts/assign-mood-rotation.py <date>` |

## Key memory files (read before every run)

- `memory/feedback_editorial_mandate.md` — signal/unbiased rules ← NEW, binding
- `memory/feedback_evolution_mandate.md` — must improve every run
- `memory/feedback_engine_static.md` — no micro-tweaks
- `memory/feedback_music_rotation.md` — 4 moods, always music
- `memory/feedback_topic_diversity.md` — bucket rotation
- `memory/feedback_copywriter_mandate.md` — iraqi-copywriter on every post
- `memory/feedback_qa_checklist.md` — 7-point QA before showing Ahmed
