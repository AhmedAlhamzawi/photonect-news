# Photonect News — Engine Architecture

**Purpose of this file.** Single source of truth for how the engine that produces
@photonect.news reels actually works, slot-by-slot, guard-by-guard. When something
changes (new filter, new atlas entry, new template variant, new music bed, new
failure mode observed in the wild), update this file in the same commit. If a
reel ships broken and this doc doesn't explain why it was allowed to ship, the
doc is out of date — fix it first, then fix the bug.

**Owning principles (from user's feedback mandate).**

1. **Every run must evolve.** Stagnation is failure.
2. **Fix the component, not the output.** Per-slug patches are a smell — architect
   the class of failure out of the pipeline.
3. **Images must be visible.** Overlays don't get to eat the image.
4. **The user must never catch the bug first.** Automated QA or explicit guard
   before publish.
5. **Free resources only.** Wikimedia Commons first, Pexels second,
   motion-graphic fallback — in that order. No paid APIs. No scraping
   rights-managed feeds.
6. **Topic diversity mandate.** At 2h cadence, no two consecutive posts share a
   `topicBucket`. Rotation is enforced by `build-posting-plan.sh`.

---

## 1. Pipeline (outer loop — one reel)

```
props.template.json
    │
    │  (daily fill-in, either by research agent or by hand)
    ▼
data/posts/<slug>/props.json   ← caption.txt sits alongside it
    │
    ▼
hunt-media.sh <slug>  →  media_hunter.py
    │   synth_queries()  — derives tight English queries from slug tokens
    │   hunt_wikimedia() — score-ranked, filter-gated
    │   hunt_pexels()    — fallback
    │   motion graphic   — last-resort fallback
    │
    │   writes hero.jpg, broll_1.jpg/mp4, broll_2.*, broll_3.*
    │   updates data/media-ledger.json (14-day dedup)
    │   updates props.json media paths
    │   writes data/posts/<slug>/media-stamp.json
    ▼
render-reel.sh <slug> [v1|v2|v3]
    │   pre-flight: refuse {{PLACEHOLDER}} in props.json            [GUARD 1]
    │   pre-flight: warn on bidi-dangerous englishSubhead           [GUARD 2]
    │   ensures media-stamp.json exists, else hunts                 [GUARD 3]
    │   strips iCloud "* 2.*" conflict duplicates                   [GUARD 4]
    │   exec: npx remotion render NewsReel …
    ▼
data/posts/<slug>/newsreel_v3.mp4
    │
    ▼
build-posting-plan.sh --date YYYY-MM-DD
    │   reads every props.json + caption.txt + newest mp4
    │   enforces no-two-consecutive-buckets rotation (awk)
    │   emits POSTING_PLAN_<date>.md
    ▼
Ahmed posts from phone, one row at a time
```

---

## 2. `media_hunter.py` guardrail stack

All filters are **subtractive** — start from a generous candidate pool, carve out
failure modes we've observed. Every new guardrail has a specific failure it was
installed to prevent. When adding a new guardrail, annotate it with the date and
the wire-level example that triggered it.

### 2a. Query synthesis (`synth_queries`)
- **Atlas lookup.** `ATLAS[token]` maps slug/topic tokens to `(hero, broll, data)`
  tight English queries. Atlas is the single lever for "make this topic produce
  good imagery"; extend it preemptively when you can see new topics coming
  (see 2f below).
- **Topic-bucket fallback.** `_<bucket>` entries (`_mena_geopolitics`,
  `_iraq_domestic`, `_gulf_regional`, `_europe`, `_global_economy`, `_tech_ai`,
  `_wildcard`) provide generic queries when the slug's tokens don't hit.

### 2b. Per-candidate title scoring (`score_title`)
Applied to Wikimedia search results. Candidate is rejected if score ≤ 0.
- `+3` per query-token that appears in the image title (core relevance).
- `+2` for archetype signals (portrait dim, orientation cues).
- `-50` if the title matches **CONFLICT_GEO** and the query includes a **MENA_ANCHOR**
  (prevents "Byblos Harbour, Millwall, London" winning an Iraq query).
- `-10` per **HISTORICAL_DENY** hit (parthian/sassanid/1800s/1970s etc — rejects
  the 1950s B&W Parthian map that beat "Hormuz" in week 1).
- `-10` per **CONTENT_DENY** hit (music/concert/food/wedding/painting/cartoon —
  rejects the Baghdad Hall recital that beat "Iraq blackout").
- `-10` per **MAP_DENY** hit when archetype is `hero` (map/atlas/chart/diagram
  — keeps the hero frame human-readable, saves maps for dedicated map slots).

### 2c. Post-download brightness gate (2026-04-19)
After the candidate passes title scoring and dedup, a PIL-based mean-luminance
check is applied:

| slot          | floor (mean L/255) | reason |
|---------------|--------------------|--------|
| hero          | **62**             | sits behind the largest Arabic headline; crushed blacks crush legibility |
| broll_1/2/3   | 45                 | covered by stat cards but still must read through the overlay |
| photo_insert  | 40                 | lives inside a framed card with its own bg, so mid-tones are fine |

Rejects print as `∅ hero too dark (L=37.3 < 62.0) ← wikimedia` and the hunter
continues to the next candidate. Pillow is soft-imported; if unavailable the
gate is a no-op (never crashes the pipeline).

**Why a floor, not an overlay-adjustment.** An overlay tweak would fix *one*
image but leak into composites where the source image is already balanced.
The floor rejects the unusable candidate upstream.

### 2d. Ledger dedup (`data/media-ledger.json`)
- 14-day TTL (`LEDGER_TTL_DAYS`).
- Two indices: by URL (prevents refetching a known bad fit) and by sha256
  (prevents the same image surfacing under a different URL).
- **Pruning for forced re-hunt:** see §7 "Re-hunt procedure."

### 2e. Pexels tier
- Applies CONTENT_DENY + MAP_DENY to alt-text.
- `time.sleep(0.15)` between requests — stay under their rate limit.
- Requires `PEXELS_API_KEY` env var; returns 403 → hunter silently falls through
  to motion-graphic fallback.

### 2f. Motion-graphic fallback (`ffmpeg`)
When no wire image survives filters + dedup, generate a 4s accent-colored
MP4 with the beat's `accent` color. Never blocks a render.

### 2g. Extending the atlas preemptively
If you know tomorrow's news cycle will include a topic not yet in `ATLAS`,
add it before the first slug lands. The atlas currently covers:

- **Conflict:** strike-military, drone, border, ceasefire, blockade, hormuz,
  lebanon, gaza, frontier, tanker, pipeline, blackout
- **Politics:** election, vote, protest, summit, sanctions, pm-race
- **Economy:** oil, brent, opec, deal, investment, billion, market
- **Tech/AI:** chip, model, frontier (servers, GPUs), ai-race
- **Disasters:** earthquake, flood, fire, evacuation

If a new slug contains a token not in ATLAS, the bucket fallback catches it
but the hero may be generic. Prefer one-line atlas additions over
post-hoc re-hunts.

---

## 3. Render guardrails (`render-reel.sh`)

Installed in order; each one refuses to call `npx remotion render` if it
trips.

| #       | Guard                                                              | Installed |
|---------|--------------------------------------------------------------------|-----------|
| GUARD 1 | `{{TEMPLATE_PLACEHOLDER}}` grep in props.json — hard fail (exit 3) | 2026-04-19 (gulf-pivot shipped with `{{ARABIC_HEADLINE}}` visible on screen) |
| GUARD 2 | englishSubhead ending in `?!.` — warn under RTL bidi flip risk     | 2026-04-19 (oil-shock shipped with `?OIL SHOCK • $95 → $150` — trailing `?` jumped to front) |
| GUARD 3 | Missing `media-stamp.json` auto-runs `hunt-media.sh`               | 2026-04-17 |
| GUARD 4 | iCloud `* 2.*` conflict duplicates deleted before bundle copy     | 2026-04-18 (Remotion ETIMEDOUT on `broll_1 2.jpg` copyfile) |

**Adding a new guard.** Append a block before `exec npx remotion render …` —
`exit` with a non-zero code so the outer batch script counts it as fail.

---

## 4. Composition (`src/compositions/NewsReel/`)

```
NewsReel.tsx          ← top-level composition, Audio + BackgroundPulse +
                        DotGrid + ScanBeam + TransitionSeries
schema.ts             ← Zod schema (NewsReelSchema) + frame constants
safeArea.ts           ← platform-safe zones (IG/TikTok crop boxes)
scenes/
  Breaking.tsx        ← 4s opening — hero image + Arabic kicker + headline
  Beat.tsx            ← 8s beat — broll + bigStat + supportingStats
  PhotoInsert.tsx     ← optional 2s inset portrait
  Sources.tsx         ← 3s closing credits
  maps/               ← hormuz, lebanon, flight_europe SVGs
VideoBackdrop.tsx     ← hero/broll image container + overlay gradient
```

**Frame budget (30s total @ 30fps).**
`BREAKING_FRAMES=120 · BEAT_FRAMES=240 · BEAT_FRAMES=240 · BEAT3_FRAMES=210 · SOURCES_FRAMES=90`.
Transitions: 12-frame fade between each sequence.

**Audio.** `audioBed` prop (default `audio/news_bed.mp3`); volume fades 0→0.35
over first 15 frames and 0.35→0 over final 45. The variant system (§6) rotates
between multiple beds.

---

## 5. Posting plan rotation (`build-posting-plan.sh`)

- Walks `data/posts/<date>-*/`, loads `props.json.topicBucket` + caption.
- Uses newest of (`newsreel_v3.mp4` > `newsreel_v2.mp4` > `newsreel.mp4`).
- awk-based rotation builds slot order under the constraint "no two adjacent
  slots share a bucket." If the bucket mix makes this mathematically
  impossible (one bucket exceeds ceil(N/2)), offending slots are flagged
  `⚠️ CONFLICT` and a warning is added to the plan header.
- Default window: 12:00 → N×2h GMT+3. Override with `--start` / `--interval`.

---

## 6. Template / style / music variant system (evolution mandate)

**Current state (2026-04-19):** Single template, single bed. All reels look
identical except for content.

**Target state:** Multi-variant rotation so the feed doesn't look like a loop
when all 6-8 daily reels play in sequence. Variants MUST stay inside the
existing brand guardrails (margins, text min-size, card opacity ≥.18,
border opacity ≥.40, overlay ≤.88).

### 6a. Template variants (layout)
Three layouts, rotated per-slot to avoid visual monotony:

| variant | hero layout          | beat layout                        | sources |
|---------|----------------------|------------------------------------|---------|
| **A** (current) | Full-bleed hero + lower-third | Broll + right-side bigStat card | centered list |
| **B**           | Half-screen split hero + Arabic caption card | Broll top, stats bottom strip | carousel tiles |
| **C**           | Hero with Arabic number-overlay | Broll + circular stat dial | sources over mini-map |

Implementation: `variant: "A" | "B" | "C"` added to `NewsReelSchema`. `NewsReel.tsx`
branches on variant at the scene-component level; scenes keep a shared safe-area
contract so margins never regress.

### 6b. Music beds
Source all beds from free/CC0 libraries only:

1. **Freesound.org** (CC0 / CC-BY only — check license per track).
2. **Free Music Archive** (cc_by_4 / cc_zero).
3. **Pixabay Music** (royalty-free for reels).

Current plan: download 4 beds into `public/audio/`:
- `news_bed.mp3` — existing (default / variant A).
- `news_bed_tense.mp3` — deeper sub, variant B, for conflict/geopolitics buckets.
- `news_bed_uplift.mp3` — brighter synth, variant C, for tech_ai + global_economy.
- `news_bed_somber.mp3` — minor-key, for casualty/disaster reels.

Selection is **bucket-aware**, not random. Tech/AI reel should never get a
minor-key somber bed; a wildfire reel should never get uplift synth.

### 6c. Style variants
- **Accent palette rotation** — current accents `#00E5A0 / #FFB020 / #D72638`
  rotated per beat. Variant C introduces `#5B8FF9 / #C084FC` for tech-forward
  stories.
- **Typography rotation** — default Tajawal; variant B swaps to Cairo for
  headline only (body stays Tajawal for consistency).
- **Motion-layer rotation** — DotGrid vs. ScanBeam vs. new GridPulse
  (todo). Only one persistent motion layer at a time; never two.

### 6d. Rotation rules
- Day-level: the 6-8 slots for a date draw from variants in sequence A → B → C → A…
  guaranteeing at least 2 variants across any day.
- Bucket-level: each bucket has a preferred variant (geopolitics = A, economy
  = B, tech = C) but the day-level rotation overrides when variants would
  repeat twice in a row.
- Music is chosen by bucket, then adjusted if two adjacent posts would draw
  the same bed.

---

## 7. Re-hunt procedure

When a slug's media is wrong and atlas/filter evolution doesn't retroactively
fix the downloaded files:

```bash
# 1. Delete the specific slot(s) you want to re-hunt
rm public/images/news/<slug>/hero.jpg          # or broll_N

# 2. Prune matching ledger entries so dedup doesn't block re-picks
python3 -c "
import json, pathlib
p = pathlib.Path('data/media-ledger.json')
led = json.loads(p.read_text())
led['entries'] = [e for e in led['entries']
                   if not (e['slug']=='<slug>' and e['slot']=='hero')]
p.write_text(json.dumps(led, indent=2, ensure_ascii=False))
"

# 3. Delete media-stamp.json so the hunter re-processes this slug
rm data/posts/<slug>/media-stamp.json

# 4. Hunt again
python3 data/_template/media_hunter.py <slug>

# 5. Re-render
bash data/_template/render-reel.sh <slug> v3
```

---

## 8. Side-agent: Photonect Engine Evolver (spec — 2026-04-19)

**Directive (user, 2026-04-19 ~1:20am GMT+3):**
> You should also have a side agent. That runs for the sole purpose of developing
> photonect. And the engine that runs it by researching then analyzing, then
> deciding, then planning, then executing, the development direct into the engine.
> It should be able to install plugins, skills, repos, and tools, and integrate
> things for the goal of constantly developing and evolving the engine that runs
> photonect news.

### 8a. Lifecycle (runs nightly, 03:00 GMT+3)

```
[RESEARCH]  scan yesterday's renders, ledger, user feedback signals,
            failure logs, competitor posts, Arabic news-Twitter trending
            topics that didn't make today's slate, MCP-registry new tools,
            wikimedia new categories, Remotion changelog.
     │
     ▼
[ANALYZE]   classify observations into:
            - bugs (something shipped wrong or almost did)
            - regressions (a previously-good pattern stopped working)
            - opportunities (new free asset source, new MCP, new template idea)
            - coverage-gaps (topic entered the news cycle but atlas lacks it)
     │
     ▼
[DECIDE]    for each observation, pick: fix / extend / prototype / defer / reject
            with a 1-line rationale. Surface a daily summary.
     │
     ▼
[PLAN]      translate decisions into a patch set. Each patch:
            - target file
            - diff (before/after)
            - rollback path
            - test ("how do I know this didn't regress")
     │
     ▼
[EXECUTE + MULTI-QA]
            Ahmed's directive (2026-04-19): "the agent should do multiple
            QA on its work before reporting." Every fix/extend patch must
            pass ALL FOUR QA passes or get downgraded to prototype:
              PASS 1 — Static (lint, tsc --noEmit, bash -n)
              PASS 2 — Sample renders (2 canonical slugs, size within ±25%)
              PASS 3 — Visual (4-frame brightness + placeholder-OCR + SSIM)
              PASS 4 — Regression sweep (build-posting-plan on last 3 dates
                       must be byte-identical to baseline)
            Missing QA tool counts as FAIL, not skip (anti-false-green).
     │
     ▼
[REPORT]    append daily entry to data/_template/EVOLUTION_LOG.md
            per-patch QA audit trail at proposals/<date>-qa.json
            summary: N patches applied, N deferred, N rejected, with rationale
```

### 8b. Capabilities (what the side-agent may install)

- `pip install <pkg>` — permitted for Pillow, requests, beautifulsoup4, etc.
  Never for paid-API clients.
- `npm install <pkg>` in `my-video/` — Remotion ecosystem only (`@remotion/*`
  + audited community packages).
- MCP registry discoveries: propose via `mcp-registry.search_mcp_registry`,
  only install after user approves (install step is a prohibited action
  without explicit consent per Claude safety rules).
- Git: commits go on a `side-agent/evolve-<date>` branch. Merges to main
  require user approval.

### 8c. Hard constraints
- **Never deletes user content.** Props.json, captions, posted mp4s are
  read-only to the side-agent.
- **Never pushes to remote without approval.**
- **Never commits secrets.** Scans every patch for `.env`, `API_KEY`,
  `PASSWORD`, `TOKEN` literals.
- **Never touches the brand file** (`src/compositions/PhotonectBrandReel/brand.ts`)
  without proposing it as a user-review item.

### 8d. Implementation layers
1. **Scheduled task** — `mcp__scheduled-tasks__create_scheduled_task` at 03:00
   GMT+3 daily, triggers the agent.
2. **Agent prompt** — loaded from `data/_template/side-agent.prompt.md`.
3. **State** — `data/_template/EVOLUTION_LOG.md` is the append-only decision log;
   `data/_template/proposals/` holds PR-style patches awaiting review.
4. **Guards** — the side-agent's shell runs with a reduced toolset: no
   `rm -rf`, no force-push, no `npm publish`.

### 8e. Current status
- **Spec written:** here (§8).
- **Scheduled task:** not yet created — deferred until Ahmed approves the spec.
- **Proposals directory:** will be created on first run.
- **First manual targets for the side-agent once live:**
  1. Add a 4th music bed (somber, for disaster reels).
  2. Prototype variant B (half-screen split hero).
  3. Add a "thumbnail composite" step that picks the brightest frame of the
     reel as the IG grid thumbnail.
  4. Scan the last 30 days' ledger for over-reused URLs (same source >2x) and
     suggest atlas extensions to diversify.

---

## 9. Change log

- **2026-04-23 15:14** — NewsReel.tsx: audioVolume peak raised 0.35→0.45 for stronger audio presence (all beds loudnorm-'d to −16 LUFS; +2 dB headroom confirmed safe). NewsReel.tsx: pickAudioBed fallback updated from stale `news_bed.mp3` to `bed_anchor.mp3` (anchor bed is in AVAILABLE_BEDS and loudnorm-normalised; old fallback bypassed the Set). generate-daily.sh Phase 1: added tech_ai numeric supportingStat lint — posts with `topicBucket: "tech_ai"` must have at least one beat supportingStat with a digit in its value. Both canonical sample baselines updated to V6 rev2 render characteristics (arabicBody restored; ai-frontier-race 15.8→14.4 MB, iran-day-50 82.8→66.9 MB; duration now 34.0 s both slugs). [side-agent run 7]
- **2026-04-23 00:03** — BeatA/B/C.tsx: restored `arabicBody` (adaptive 22–26 px) and 3-pill `supportingStats` row inside safe-zone containers (V5 had stripped them, causing ~30% information-density loss). BeatB.tsx restructured: bigStat moved to top-half broll chyron, freeing bottom half for full content stack. BeatC.tsx: bottom-anchored progressive reveal now emits label→heading→body→pills→inline stat within CONTENT_BOTTOM boundary. NewsReel.tsx comments rewritten. 12 new lavfi music beds synthesised (`make-v6-beds.py`): unique key/BPM/arrangement per bed, loudnorm-'d −16 LUFS, 12/12 distinct PCM fingerprints confirmed. Captions restored to full format: hook + 3 pillars + 3 scenarios + 15 hashtags. [manual V6 rev2]
- **2026-04-22 03:07** — VideoBackdrop.tsx: made `src`/`type` props optional; added `if (!src)` ink-fallback guard (BUG-V4-001: prevents render crash when beat.broll absent from props.json). generate-daily.sh: variant-aware luminance QA — reads `variant` from props.json, crops Variant B beat frames to top 50% before L_safe check to eliminate false positives from intentional dark lower half (BUG-V4-004). media_hunter.py synth_queries: added step 1b using `beat.bigStat.label` as per-beat broll seed query for non-hero slots (BUG-V4-002: topically specific broll instead of bucket-generic atlas fallback). iran-day-50 baseline updated post-V5 (BeatA translateY overhaul raised CRF bitrate). [side-agent run 6]
- **2026-04-21 19:30** — extract-thumbnail.sh: replaced broken signalstats lavfi
  method with ffmpeg -ss + Pillow mean-L (same as QA PASS 3 authoritative method).
  render-reel.sh: replaced `exec npx remotion render` with regular call + auto-runs
  extract-thumbnail.sh on success. ATLAS extended with `starlink` and `embargo`
  entries (§2a). render-reel.sh: added inline tech_ai supportingStat pre-flight
  warning (non-blocking). CC0 music bed candidate placed: `news_bed_tense.mp3`
  from OpenGameArt CC-BY 4.0 — awaiting Ahmed ear-verification before enabling.
- **2026-04-19 01:20** — Added brightness-floor gate (§2c). Added GUARD 1
  (placeholder scan) and GUARD 2 (bidi warning) to render-reel.sh (§3).
  Wrote this doc. Side-agent spec drafted (§8).
- **2026-04-19 01:13** — Atlas extended preemptively for election / protest /
  summit / sanctions / strike / border / drone / strike-military / earthquake
  / flood / chip / model / deal / investment / billion / ceasefire.
- **2026-04-18 ~20:00** — CONFLICT_GEO filter added (rejects London/Millwall/etc
  hits on MENA queries after Byblos-Harbour-Millwall disaster).
- **2026-04-18 ~19:30** — iCloud `* 2.*` cleanup added to render-reel.sh
  (GUARD 4) after Remotion ETIMEDOUT on copyfile.
- **2026-04-18 ~18:00** — HISTORICAL_DENY + MAP_DENY filters added (after
  Parthian-era B&W map beat a Hormuz hunt).
- **2026-04-18 ~17:00** — CONTENT_DENY filter added (after Baghdad music
  recital beat an Iraq-blackout hunt).
- **2026-04-17** — NewsReel composition approved; autonomous 2h cadence
  granted.

When you change the engine, add a line here. No change is "too small" for
the changelog — the point is traceability, not filtering.
