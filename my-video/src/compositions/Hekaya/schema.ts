import { z } from "zod";

// Hekaya (حكاية) — Photonect's slow-storytelling track.
// Sister composition to NewsReel. Same channel, fundamentally different rhythm.
// Where NewsReel is hook-cliffhanger, Hekaya is breath-pause-reveal.
//
// Each reel = ONE true tale. A forgotten figure, a lost place, an origin story.
// Voice: lyrical Arabic, sensory prose, reflective close. NO cliffhangers.
//
// Music: ONE original Suno-generated track per reel. No rotation pool —
// each story has its own bespoke soundtrack.
//
// Visuals: real photos (Pexels/Wikimedia) + Kie-AI-generated dreamy frames +
// Remotion-native typography. Warm palette (gold / dusk-blue / ivory).

const Source = z.object({
  name: z.string(),
  domain: z.string(),
});

// A single chapter / scene of the story. Three of these carry the narrative.
const HekayaChapter = z.object({
  // Lyrical Arabic chapter heading. ~3-6 words. Not a headline — a verse.
  arabicTitle: z.string(),
  // 80-130 word Arabic prose. Sensory. Slow. Past-tense narrative voice.
  arabicNarration: z.string(),
  // Optional: a single anchored fact (date / number / place) shown as a
  // delicate overlay card. NOT a statistic dump like NewsReel — used sparingly.
  anchorFact: z
    .object({
      label: z.string(),
      value: z.string(),
    })
    .optional(),
  // Path to chapter image — real photo OR AI-generated frame.
  visual: z.string(),
  visualType: z.enum(["image", "video"]).default("image"),
  // Optional Latin caption sliding in from the side — translation or attribution.
  latinCaption: z.string().optional(),
  // Per-chapter accent color override; defaults to the global gold.
  accent: z.string().optional(),
});

export const HekayaSchema = z.object({
  dateLabel: z.string(),
  arabicDateLabel: z.string(),
  handle: z.string().default("@photonect.news"),
  // SINGLE Suno-generated track for THIS story. Required — never silent.
  audioBed: z.string(),

  // Opening title card. Establishes era + place + the lyrical title.
  prologue: z.object({
    // Lyrical Arabic title, ~5-8 words. Could be a verse or sensory image.
    arabicTitle: z.string(),
    // ALL-CAPS Latin subtitle, slim line. ~6-12 words.
    englishSubtitle: z.string(),
    // Era stamp. "859 AD" or "9th Century" or "Andalusia, 1010".
    era: z.string(),
    // Place stamp. "Fez, Morocco" or "Baghdad on the Tigris".
    place: z.string(),
    // The opening sensory line. 30-50 Arabic words. The first thing the
    // narrator would say if reading aloud. Vivid image, slow rhythm.
    arabicHook: z.string(),
    // The hero image — atmospheric, evocative, not literal.
    heroMedia: z.string(),
    heroMediaType: z.enum(["image", "video"]).default("image"),
  }),

  // The story — exactly THREE chapters: setting → heart → resolution.
  // Why three: matches the canonical short-story arc and keeps engineering
  // simple (parallel to NewsReel's 3-beat structure).
  chapters: z.array(HekayaChapter).length(3),

  // Closing reflection. The "what does this mean today" beat.
  // No question mark, no CTA — just resonance.
  epilogue: z.object({
    // 60-90 word Arabic reflection.
    arabicReflection: z.string(),
    // Optional poetic sign-off line, ~5-10 words.
    arabicSignature: z.string().optional(),
    // Optional closing image. If absent, falls back to a calligraphic motif.
    closingMedia: z.string().optional(),
  }),

  // 2-6 verifiable sources for credibility.
  sources: z.array(Source).min(2).max(6),
});

export type HekayaProps = z.infer<typeof HekayaSchema>;
export type HekayaChapterProps = z.infer<typeof HekayaChapter>;
export type HekayaSourceProps = z.infer<typeof Source>;

// Pacing — slower than news. Total 75 seconds @ 30 fps = 2250 frames.
//
// Prologue 360f (12s) — title card + era + place + hero
// Chapter 1 480f (16s) — the setting (mood, world, characters)
// Chapter 2 660f (22s) — the heart of the story
// Chapter 3 540f (18s) — the resolution
// Epilogue 210f  (7s) — reflection + handle
//
// Why these numbers: each chapter holds ~100 Arabic words at ~6 wpm reading
// speed. Slower than news (which sits at ~9 wpm) — Hekaya is meant to breathe.
export const HEKAYA_PROLOGUE_FRAMES = 360;
export const HEKAYA_CHAPTER1_FRAMES = 480;
export const HEKAYA_CHAPTER2_FRAMES = 660;
export const HEKAYA_CHAPTER3_FRAMES = 540;
export const HEKAYA_EPILOGUE_FRAMES = 210;

export const computeHekayaDurationInFrames = () =>
  HEKAYA_PROLOGUE_FRAMES +
  HEKAYA_CHAPTER1_FRAMES +
  HEKAYA_CHAPTER2_FRAMES +
  HEKAYA_CHAPTER3_FRAMES +
  HEKAYA_EPILOGUE_FRAMES;

// Hekaya's warm palette. Distinct from PHOTONECT brand red/yellow news colors.
// Goal: dusk light. Calm. Reading-by-candle vibe.
export const HEKAYA_PALETTE = {
  ink: "#0B1A2A",        // deep dusk blue — primary background
  gold: "#D4A668",       // burnished gold — accent / dividers
  ivory: "#F5EBD8",      // warm ivory — body text
  rose: "#C4806B",       // muted rose — secondary accent
  shadow: "#06101C",     // deeper blue for layering
  vellum: "#E8DCC4",     // parchment tint for cards
} as const;
