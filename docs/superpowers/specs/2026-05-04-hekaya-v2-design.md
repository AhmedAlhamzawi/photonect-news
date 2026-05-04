# HEKAYA v2 — Design Spec

**Status:** Approved (Ahmed, 2026-05-04) — build begins immediately.
**Author:** Claude (after 6-perspective committee research).
**v1 archive:** `my-video/src/compositions/Hekaya/Hekaya.tsx` — left untouched.

---

## 1. Purpose

HEKAYA is the slow-storytelling sister track to NEWS on @photonect.news. Each post is one true tale told slowly — a forgotten figure, a lost place, an origin story.

**v1 outcome:** Ahmed's verdict — "It's not live, it's a slideshow. I can't even stay 2 seconds watching it." Six committee members from independent angles converged on the same diagnosis: silent stills + ambient music = mood film, not story. Speech grabs the language network instantly; ambient music *relaxes* attention. v1 was sedative.

**v2 mission:** every reel is a 75-second narrated mini-documentary that holds a viewer at any second. The SAME stories (Fatima al-Fihri, Bayt al-Hikma, etc.), told as actual cinema.

---

## 2. Architecture — Six Pillars

### Pillar 1 — Voice-Over Spine

The spine of attention. Without it, on-screen Arabic text is asking the viewer's reading muscles to do the storytelling, with sound off by 60% of viewers and Arabic right-to-left text-tracking. A losing bet.

**Specs:**
- **Provider:** ElevenLabs Arabic (recommended — best Arabic prosody, voice-cloning option for Ahmed-as-narrator). Fallback: Kie AI (only if it ships an Arabic VO endpoint with comparable quality). Murf.ai's Arabic voices are weaker.
- **Voice register:** mid-chest, AJ Documentary mid-Arabic — NOT news-anchor MSA, NOT colloquial. Iraqi-Levantine flavored فصحى, ~30s old narrator energy.
- **Pacing:** 2-2.5 words/second sustained. 150-180 Arabic words across 75s.
- **Pause architecture:** sentence-end ~0.4s, paragraph-end ~1.2-1.8s, dramatic-pivot full silence 0.6-1.0s.
- **Mic feel:** close-mic, warm proximity, controlled breath audible.

**On-screen text:** punctuation only — hooks, dates, killer-fact quotes — never a transcript. Rendered as kinetic typography (Pillar 4).

**Pipeline:**
1. Script written by `hekaya-storyteller-v2.md` agent (Pillar 3 voice rules).
2. Script length-validated to 150-180 words.
3. POST to TTS provider with voice ID + script.
4. MP3 saved to `my-video/public/audio/hekaya-vo/<slug>.mp3`.
5. Composition reads `voiceOver` field from props for the path.

---

### Pillar 2 — Story-Craft Script

Three-act compressed to 75s. Every beat connected with **but / therefore**, never "and then" (the slideshow connective). Five archetypal structures available; each story picks one.

**Timeline (75s = 2250 frames @ 30fps):**

| Phase | Frames | Time | Function |
|---|---|---|---|
| Cold open | 0-60 | 0-2s | Hook in action — close-up detail, killer quote, no title yet |
| Inciting incident | 60-240 | 2-8s | The world breaks; lower-third title arrives at ~6s |
| Setup of want | 240-525 | 8-17.5s | Protagonist + felt want, by name |
| First obstacle | 525-750 | 17.5-25s | The first try fails |
| Escalation 1 | 750-1050 | 25-35s | Stakes raise — second try/fail |
| Escalation 2 | 1050-1350 | 35-45s | Third complication or dilemma |
| **Silence pivot** | 1350-1380 | 45-46s | 0.8s full silence — Murch's "white frame in audio" |
| Climax | 1380-1650 | 46-55s | Reveal / decision / turn |
| Resolution | 1650-1950 | 55-65s | Aftermath, what changed |
| Resonance | 1950-2160 | 65-72s | Final image + 6-word sentence |
| Loop | 2160-2250 | 72-75s | Cold-cut back to opener visually + musically |

**Archetypal structures (script picks one per story):**

- **A. The Impossible Task** — ordinary world → call to impossible task → three failed attempts → unexpected ally/insight → triumph + cost. *Use for:* Fatima al-Fihri, Ibn Battuta, builders.
- **B. The Secret Hidden in Plain Sight** — familiar object → "you've been wrong about it" → buried evidence → reveal → implication. *Use for:* Bayt al-Hikma, Andalusian engineering.
- **C. One Decision That Changed Everything** — world before → dilemma → decision in slow-motion → cascade → line we remember. *Use for:* a caliph's edict, a scholar's emigration.
- **D. The Map and the Territory** — what we think happened → what actually happened → the gap → why the gap matters now. *Use for:* coffee origin, Al-Khwarizmi.
- **E. The Quiet Victory** — small, deliberate act → ripples → unintended consequence → the long arc → resonance. *Use for:* Zubaidah's road.

---

### Pillar 3 — Native Arabic Voice Rules

New copywriter agent: `.claude/agents/hekaya-storyteller-v2.md`. Replaces v1's `hekaya-storyteller.md`.

**Five non-negotiables:**

1. **Open with sensory action — NEVER a date or year.**
   - ✗ "في عام 859 ميلادية، أسست فاطمة الفهري..."
   - ✓ "ورثَت ذهباً. كان يكفي لقصر. بَنَت به مدرسةً."

2. **Verbs : adjectives, 3:1.** Cut every abstract noun chain.

3. **Short main clauses (5-9 words).** Sentence fragments allowed and encouraged.

4. **No Quranic-register phrases** (ولقد، إنّ، تُعدّ، يُقال إنّ) unless directly quoting.

5. **End every story on a concrete noun the listener can picture, not a moral.**

**Anti-patterns banned:**
- Calendar-fact opens
- Passive constructions (تُعتبر، يُعدّ)
- Borrowed Quranic register without earning it
- Abstract noun chains ("رحلة من العزيمة والإصرار والتفاني")
- Explanatory clauses ("أنّها كانت امرأةً تونسية من القرن التاسع")

**Test:** read the script aloud. If it sounds like a Wikipedia summary, rewrite. If it sounds like a friend leaning into your ear at 11pm — ship it.

---

### Pillar 4 — Multi-Tier Visual Motion

Three motion tiers running simultaneously across every frame:

**Tier 1 — Atmospheric (continuous, slow):** subtle Ken Burns drift, embers floating up, slow gradient hue-shift, vignette pulse. No more than 1px/frame on KB. This is the "alive" baseline.

**Tier 2 — Structural (per-beat, choreographed):** B-roll cuts every 2.4-3.2s, layout transitions between scenes, calligraphic divider line draw-on at chapter changes, lower-third title slide-in.

**Tier 3 — Emphatic (sharp, attention-grabbing):** scale-pop on key word, color-flash to gold for 4f on the killer noun, mask-wipe reveal on punchline frames, hand-drawn underline (SVG strokeDashoffset) under the killer fact word, light-leak overlay sweep at chapter transitions.

**B-roll cycle (per chapter):** 5-7 stills with a varied shot ladder:
- (a) wide establishing
- (b) medium contextual
- (c) close-up detail
- (d) texture/material (paper, calligraphy, fabric, stone)
- (e) human face
- (f) environment without humans
- (g) object/artifact

Cuts every ~2.6s with each still getting its own subtle KB direction (one zooms in, next pans left, next holds with a graphic) so the cumulative motion is varied, not metronomic.

**Layout rotation across the 75s reel** (NOT the same layout every chapter):
1. Cold-open close-up + lower-third
2. Full-bleed quote on black
3. Image with caption corner
4. Split-screen — image left 50%, giant pull-quote right 50%
5. Single word on black (for the punchline beat — held 1.5s, silent)
6. Photo collage panning vertical
7. Animated map / archival treatment
8. Single image full-bleed with hand-drawn underline

Aim for 4-5 distinct layouts across the reel. Repetition kills motion.

**Arabic kinetic typography (works for RTL):**
- **Phrase-by-phrase masked reveal** (gold standard) — `clip-path: inset()` wiping right-to-left, 8-12f per phrase. Looks like ink flowing into the page.
- **Word-by-word with baseline shift** — each word enters from y:+8 and settles, 2-3f overlap.
- **Full-line scale-pop on emphasis** — killer-fact line arrives at scale 0.92 and springs to 1.0 with brief gold flash.
- ✗ **AVOID letter-by-letter** — breaks Arabic ligatures, reads as Roman cosplay.

**Image treatment beyond Ken Burns:**
- 2.5D parallax: foreground subject masked from background, divergent transforms (foreground 12px, background 4px, opposite direction)
- Masked window framing: photo revealed inside an animated rectangle
- Duotone (gold + deep blue) for archival, switching to full-color at the chapter "lands"
- Photo collage panning: 3 stills tiled vertically, reel pans down across them

**Palette stays:** dusk-blue ink (#0B1A2A), burnished gold (#D4A668), warm ivory (#F5EBD8), muted rose (#C4806B). Tajawal Arabic font (already shipped).

---

### Pillar 5 — Layered Audio

Four-layer audio stack. Suno track stays — but now does 30% of audio work, not 100%.

**Layers (with mix targets):**
1. **VO** — primary, -6 dB, sidechain trigger for music
2. **Foley/SFX** — punctuation, -20 to -22 dB
3. **Music** — Suno track, ducked to -18 dB under VO, swell to -10 dB between sentences, uncovered at -8 dB on climax
4. **Ambience bed** — room tone / environment, -28 dB

**Foley/SFX library (small, reusable across reels):**
- Reed pen on parchment
- Distant adhan (heavy reverb tail) — geographic anchor for North Africa / Levant
- Single oud pluck — sentence-end punctuation, replaces a comma
- Page turn — transitions between story beats
- Candle flicker / oil lamp hiss — intimate scene-setting
- Water drip on stone — for fountains, ablution, courtyard imagery
- Bazaar ambience bed — under wide context shots
- Paper rustle — under historical references

**Saved at:** `my-video/public/audio/hekaya-sfx/<name>.mp3` — committed to repo.

**Sidechain ducking:** music drops to -18 dB with a 200ms attack / 400ms release whenever VO is speaking. Implementation: in Remotion, duck via `interpolate()` on the music `volume` based on VO timing markers in props.

**Cold open — first 2 seconds:**
- 0:00 — Foley element only (reed pen, distant adhan, single sound)
- 0:00.5 — VO first syllable arrives
- 0:01.2 — Music enters underneath at -20 dB
- 0:02 — Lower-third title slides in

**Silence pivot at 0:45:** Murch's "white frame in audio." Drop everything — music, SFX, VO — for 0.6-1.0s. The viewer's brain, having adapted to the audio bed, snaps back to full alertness. This is the highest-retention move in 75-second storytelling.

---

### Pillar 6 — Loop Engineering

Final 2 seconds engineer the reel to feel like it could lead back into 0:00. Instagram's autoplay loop will then deliver continuity, not repetition. Dwell time doubles.

**Mechanics:**
- Closing line poses the question that the opening line answered
- End frame visually matches opener (same shot composition, different meaning after the story)
- Music resolves to opening key — Suno prompt explicitly asks for "ABA structure, ending note matches opening note"
- Final foley element echoes the opening foley (a reed pen at 0:01 returns at 1:14)
- **Cold-cut at 1:15** — NOT a fade. Fades signal "over"; cold cuts let the loop work.

---

## 3. Technical Architecture

### File layout (new vs reused)

```
my-video/src/compositions/
├── Hekaya/                          # v1 — ARCHIVED, untouched
│   ├── Hekaya.tsx
│   └── schema.ts
└── Hekaya2/                         # NEW
    ├── Hekaya2.tsx                  # composition root
    ├── schema.ts                    # new schema with VO + chapter B-roll arrays
    └── scenes/                      # broken-out scene components
        ├── ColdOpen.tsx
        ├── Chapter.tsx              # generic chapter scene with motion tiers
        ├── FullBleedQuote.tsx
        ├── SplitScreen.tsx
        ├── SingleWord.tsx           # for punchline beats
        ├── PhotoCollage.tsx
        └── Resonance.tsx

.claude/agents/
├── hekaya-storyteller.md            # v1 — left untouched (could be deleted later)
└── hekaya-storyteller-v2.md         # NEW

automation/scripts/
├── generate-suno-music.py           # reused (Suno tracks per story)
├── generate-hekaya-vo.py            # NEW — produces VO mp3 per story
├── upload-hekaya-to-drive.py        # reused
└── (new) build-hekaya-script.py     # optional — script-validation helper

data/hekaya/
└── <date>-<slug>/
    └── .meta/
        ├── props.json               # NEW schema
        └── script.txt               # NEW — the source script for the VO

my-video/public/audio/
├── hekaya/<slug>.mp3                # reused — Suno music tracks
├── hekaya-vo/<slug>.mp3             # NEW — VO tracks
└── hekaya-sfx/                      # NEW — foley library
    ├── reed-pen.mp3
    ├── distant-adhan.mp3
    ├── oud-pluck.mp3
    ├── page-turn.mp3
    ├── candle-flicker.mp3
    ├── water-drip.mp3
    ├── bazaar-bed.mp3
    └── paper-rustle.mp3

cloud-media/hekaya/<date>/
└── <date>-<slug>/
    ├── hero.jpg                     # opener
    ├── chapter1_*.jpg               # 5-7 photos for chapter 1 cycle
    ├── chapter2_*.jpg               # 5-7 photos for chapter 2 cycle
    ├── chapter3_*.jpg               # 5-7 photos for chapter 3 cycle
    └── closing.jpg                  # for resonance scene

.github/workflows/
└── render-hekaya.yml                # extend to point at Hekaya2 composition
```

### New props.json schema (sketch)

```typescript
const Hekaya2Schema = z.object({
  dateLabel: z.string(),
  arabicDateLabel: z.string(),
  handle: z.string(),
  
  // Audio
  voiceOver: z.string(),              // path to VO mp3
  music: z.string(),                  // path to Suno music mp3
  sfx: z.array(z.object({             // foley/SFX timing markers
    file: z.string(),
    startFrame: z.number(),
    volumeDb: z.number().default(-22),
  })),
  
  // Story
  title: z.object({
    arabic: z.string(),               // 5-8 word lyrical title
    englishSubtitle: z.string(),
    era: z.string(),
    place: z.string(),
  }),
  
  // The script — the spine of the reel
  scriptArabic: z.string(),           // full VO script, used for caption
  scriptKeyMoments: z.array(z.object({  // phrase-by-phrase reveal markers
    arabicText: z.string(),           // phrase shown on screen
    startFrame: z.number(),           // when VO says this
    durationFrames: z.number(),
    layoutType: z.enum([
      "lower-third",
      "full-bleed-quote", 
      "split-screen",
      "single-word",
      "photo-caption",
      "collage-pan",
    ]),
    keyWord: z.string().optional(),   // word that gets gold flash
  })),
  
  // Visuals — varied B-roll cycles
  heroMedia: z.string(),              // first image — cold open detail
  chapterCycles: z.array(z.object({
    chapterIndex: z.number(),
    photos: z.array(z.string()),      // 5-7 images for this chapter
    durationFrames: z.number(),
  })).length(3),
  closingMedia: z.string(),           // resonance image
  
  // Loop
  loopHook: z.object({
    openingPhrase: z.string(),        // the line that opens
    closingPhrase: z.string(),        // the line that loops back
  }),
  
  // Sources for caption
  sources: z.array(z.object({ name: z.string(), domain: z.string() })),
});
```

### Pipeline (per story)

```
research entry (existing)
    ↓
hekaya-storyteller-v2 agent → script.txt (150-180 words, voice rules)
    ↓
generate-hekaya-vo.py → voiceOver mp3
    ↓
script timing analysis → scriptKeyMoments[] (phrase markers + layout assignment)
    ↓
photo hunter (extended) → 24-30 photos per story (6 photos × 3 chapters + hero + closing)
    ↓
generate-suno-music.py → music mp3 (already exists, reuse)
    ↓
foley assignment → sfx[] markers
    ↓
props.json assembled → Hekaya2 composition renders
    ↓
upload-hekaya-to-drive.py → Drive HEKAYA folder
```

---

## 4. Build Plan (Phased)

### Phase 0 — Spec & Approval ✅
This document. Approved by Ahmed 2026-05-04.

### Phase 1 — Infrastructure
1. Build `Hekaya2/schema.ts` with new schema
2. Build `Hekaya2/Hekaya2.tsx` composition + scene components
3. Register in `Root.tsx`
4. Build `hekaya-storyteller-v2.md` agent
5. Build `generate-hekaya-vo.py` script (TTS pipeline)
6. Source initial foley/SFX library (Pixabay/Freesound CC0)

### Phase 2 — Proof Reel: Fatima al-Fihri
1. Run hekaya-storyteller-v2 on Fatima research → script.txt
2. Generate VO mp3 via TTS
3. Hunt 18-24 photos with shot-ladder discipline
4. Assemble props.json with phrase markers + layout assignments
5. Render via Hekaya2 composition locally
6. QA pass — does it hold for 75s?
7. If yes → push + cloud render → Drive upload to HEKAYA folder
8. **Ahmed reviews proof. SIGN-OFF GATE.**

### Phase 3 — Batch the other 5
Only after Ahmed signs off on the Fatima proof.

---

## 5. Open Questions (for Ahmed when he wakes)

1. **VO voice provider.** ElevenLabs (best Arabic, ~$0.30/reel), Kie AI Suno-voice (uneven), or one-time clone of Ahmed's own voice (cheapest premium). Recommendation: ElevenLabs preset for the first proof reel, voice-clone Ahmed for v3.
2. **Voice register confirmation.** Iraqi-Levantine male, mid-chest, ~30s-old narrator energy. OK to ship?

---

## 6. Out of Scope (v2)

- Video B-roll (only stills + motion graphics)
- AI-generated images (skip Kie image gen for now — Pexels stills + motion design carry the load)
- Animated maps as full-frame sequences (we can do simple animated route lines, not full geographic animations)
- A separate workflow file for Hekaya2 (we extend the existing `render-hekaya.yml`)

---

## 7. Success Criteria

The proof reel ships if:
1. **Ahmed watches it for the full 75 seconds without scrolling away.** This is the only metric that matters. v1 failed at 2 seconds.
2. The narrative holds — protagonist + want + obstacle + turn + resonance all land.
3. The audio is layered (VO + music + SFX + silence) — not single-track.
4. Visual cuts every 2.5s on average — no single image holds longer.
5. The Arabic voice rules are visibly enforced (no calendar opens, no Quranic register, fragments allowed).
6. The reel loops — final frame matches opener, music resolves to opening key, cold-cut at 1:15.

If 4/6 land on the proof, ship. Iterate the rest in v2.1.
