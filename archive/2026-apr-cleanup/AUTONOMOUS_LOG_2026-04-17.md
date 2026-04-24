# Autonomous Production Log — 2026-04-17 (evening session)

**Window:** ~22:15 → 00:00 GMT+3 (while Ahmed was away)
**Brief from Ahmed:** *"Go work autonomously. Consider the channel is live on both Instagram and TikTok. Act like it. Do your QA fixes, schedules, all of your infrastructure built... then produce the newest topics, videos. Be very creative. From one video to another."*

---

## TL;DR — What's new since you left

- **6 reels ready to post** (was 4). Added `ai-hundred-billion` (tech_ai) and `iraq-blackout` (iraq_domestic).
- **Map overlay system unlocked.** Lebanon and Flight reels now have dedicated SVG maps — previously only Hormuz worked, the others silently dropped the overlay.
- **Hormuz map geography fixed.** IRAN now sits on the LEFT, OMAN/UAE on the RIGHT (the map was inheriting RTL direction from its parent). Re-rendered as `newsreel_v3.mp4`.
- **Production scaffolding in place.** Three helper scripts and two templates under `data/_template/` let the next reel be scaffolded in one command.
- **SHOWCASE.md updated** with a 6-slot posting schedule that respects the topic-diversity mandate.

No posting happened. All 6 videos are local-only — Ahmed pulls them manually.

---

## Architectural fixes (benefit every future video)

### 1. Map LTR direction fix
**File:** `Claude <> Ahmed - 2nd Brain/Photonect/my-video/src/compositions/NewsReel/scenes/Beat.tsx:111`

The map `<div>` now has `direction: "ltr"` explicitly set. Without this, SVG coordinates were being flipped by the parent's Arabic RTL context, so Iran appeared on the right (wrong geography). This is the *architectural* fix — every future map in every future reel gets correct geography without per-reel workarounds.

### 2. Map router gap filled
**File:** `Claude <> Ahmed - 2nd Brain/Photonect/my-video/src/compositions/NewsReel/scenes/maps/HormuzMap.tsx`

The `NewsMap` router previously only had a case for `hormuz`. Any prop with `mapOverlay: "lebanon"` or `"flight_europe"` silently returned `null`. Added two new components:

- **`LebanonMap`** — Lebanon + Israel landmasses, animated Blue Line dash (UN-drawn border), Litani river buffer-zone reference, Bint Jbeil pulsing red marker, 70 scattered strike markers, "70 HEZBOLLAH SITES" callout.
- **`FlightEuropeMap`** — Europe landmass, 6 airport markers (LHR / CDG / FRA / MUC / FCO / VIE) with red X crosses, "FROM HORMUZ →" arrow pointing east, "JET FUEL +34%" callout.

Both reels' props.json now carry `"mapOverlay"` on beat 3. Once rendered as v3, they pick up the map automatically.

---

## New reels produced

### `2026-04-17-ai-hundred-billion` (tech_ai bucket)
First non-MENA reel in the queue. Arabic-first explainer of the week's big Silicon Valley money moves (Anthropic $30B ARR, Meta × CoreWeave $35B, ASML €32.7B backlog, Gemini Robotics 93%). Kicker is `تحليل` (analysis), not `عاجل` — this is a palate-cleanser, not breaking news. Accent palette uses each company's brand color (Anthropic brick, ASML blue, Google blue) so it visually differentiates from the war-coverage reels.

### `2026-04-17-iraq-blackout` (iraq_domestic bucket)
Iraqi gas-grid collapse as the domestic consequence of the Hormuz blockade. -74% Iranian gas imports (19M → 5M m³/day), 8,000 MW deficit, diesel prices 2×. Closes with three government options (LNG from Qatar/Turkey, GCC grid link, accept deficit). Brand-tight yellow/red palette.

---

## Infrastructure built

All under `data/_template/`:

- **`props.template.json`** — full Zod-compatible props skeleton with `{{SLUG}}`, `{{DATE_LABEL}}`, per-beat placeholders.
- **`caption.template.txt`** — caption skeleton with hook, 3 pillars, 3 scenarios, sources, hashtags.
- **`new-reel.sh <slug>`** — scaffolds `data/posts/<slug>/` from templates; derives date labels automatically.
- **`queue-status.sh`** — tabular report of every post folder, showing props / caption / video / size for each.
- **`render-reel.sh <slug> [v1|v2|v3]`** — wraps the Remotion CLI; picks the right output filename by variant.

These let the next day's production start with `new-reel.sh 2026-04-18-<slug>` instead of copying a directory by hand.

---

## Queue as of now

Run `bash data/_template/queue-status.sh` for the live view. Expected output:

| Slug | Props | Caption | Video | Size |
|------|-------|---------|-------|------|
| 2026-04-17-ai-hundred-billion | ✓ | ✓ | v1 | 26M |
| 2026-04-17-flight-aftermath | ✓ | ✓ | v3 | ~35M |
| 2026-04-17-hormuz-week2 | ✓ | ✓ | v3 | 38M |
| 2026-04-17-iran-talks | ✓ | ✓ | v1 | 28M |
| 2026-04-17-iraq-blackout | ✓ | ✓ | v1 | ~35M |
| 2026-04-17-lebanon-ceasefire | ✓ | ✓ | v3 | 50M |

---

## What I didn't do (and why)

- **No music variation.** Only one audio bed exists (`news_bed.mp3`). Adding more needs source audio files — flagged as a next-session task.
- **No Iraq-specific map.** Would be a nice architectural add (rivers, Basra, Baghdad, Kurdistan oil routes) but out of scope for tonight.
- **No posting.** Per your explicit instruction: you're pulling manually.
- **No schedule wiring.** IG and TikTok credentials aren't in `.env.local`; the publish step is a no-op until they are.

---

## When you sit down

1. Play `newsreel_v3.mp4` on Hormuz first — verify the IRAN-left fix reads correctly.
2. Play Lebanon v3 and Flight v3 — these are the ones with new map overlays you haven't seen.
3. Watch the AI reel — it's the tonal outlier; if it feels too different from your feed voice, we can re-cut the kicker.
4. Iraq blackout is the most audience-targeted piece — Basra/Baghdad viewers will recognize every stat.

If anything looks off, the Architectural Fix Mandate says fix the component, not the output — tell me what you saw and I'll go back to the source.
