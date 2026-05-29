import { z } from "zod";

const Stat = z.object({
  label: z.string(),
  value: z.string(),
});

const BigStat = z.object({
  value: z.string(),
  label: z.string(),
  arabicLabel: z.string(),
});

// V6 (2026-04-22) — restore content density that V5 over-stripped.
// V7 (2026-05-08, Leap) — adds editorial-craft fields after watching ~100 best
// short-form news videos. Every existing prop keeps validating because all new
// fields are optional. New fields enable:
//   - brollSource:     persistent attribution chip in lower-left of every beat
//                      (Vox/C4/Sky/Reuters pattern — "credibility as design")
//   - subtitlePhrases: phrase-by-phrase caption bar in bottom 10% of frame
//                      (BBC/Vice pattern — sound-off design system)
const Beat = z.object({
  label: z.string(),
  arabicHeading: z.string(),
  arabicBody: z.string().optional(),
  bigStat: BigStat.optional(),
  // V6: 3 is the narrative sweet spot — one anchor stat + two supports.
  // Caps content generation to keep pill row inside 800px CONTENT_WIDTH.
  supportingStats: z.array(Stat).max(3).optional(),
  broll: z.string(),
  brollType: z.enum(["video", "image"]),
  // V8 leap (2026-05-10) — multi-shot photo cycle within the beat. When set,
  // the Beat scene cycles through these images at ~2.5s intervals with crop/
  // zoom variations (the "cuts every 2.5s" pattern that every world-class
  // short-form news reel uses). 3-6 entries; the first is treated as the
  // anchor/hero of the beat. Falls back to single `broll` when omitted, so
  // existing posts render unchanged.
  brolls: z.array(z.string()).min(3).max(6).optional(),
  // V7 leap — short attribution string for the persistent SourceChip in the
  // lower-left of the beat (e.g. "REUTERS · MAY 6", "WIKIMEDIA · CC-BY",
  // "AP · BAGHDAD"). When omitted, the chip falls back to the slug's first
  // top-level source (so existing posts still render meaningfully).
  brollSource: z.string().optional(),
  // V7 leap — 3-4 short Arabic phrases (5-9 words each) that reveal phrase-by-
  // phrase in a bottom subtitle bar across the beat's runtime. They are NOT a
  // duplicate of arabicBody — they're the screenshot-able punch lines a viewer
  // reads with sound off. When omitted, the bar stays empty and the beat falls
  // back to V6 behavior.
  subtitlePhrases: z.array(z.string()).max(4).optional(),
  accent: z.string().optional(),
  photoInsert: z.string().optional(),
  photoCaption: z.string().optional(),
  mapOverlay: z.enum(["hormuz", "lebanon", "flight_europe"]).optional(),
});

const Source = z.object({
  name: z.string(),
  domain: z.string(),
});

// Template + style variant knobs. All default to "A" so every existing
// props.json keeps rendering unchanged; adding `variant: "B"` or
// `topicBucket: "tech_ai"` is the opt-in path into the variant rotation.
export const VARIANT_VALUES = ["A", "B", "C"] as const;
export const TOPIC_BUCKETS = [
  "mena_geopolitics",
  "iraq_domestic",
  "gulf_regional",
  "europe",
  "global_economy",
  "tech_ai",
  "wildcard",
] as const;

export type VariantName = (typeof VARIANT_VALUES)[number];

// V4 mapping retained. Tonal register per topic class:
//  A MONEY-SHOT  → hot-breaking politics / conflict (punchy, tabloid)
//  B KINETIC     → data / tech / macro (uptempo, info-forward)
//  C CINEMA      → feature / wildcard / strategic stories (slow reveal)
export const BUCKET_VARIANT: Record<string, VariantName> = {
  mena_geopolitics: "A",
  iraq_domestic:    "A",
  tech_ai:          "B",
  global_economy:   "B",
  wildcard:         "C",
  europe:           "C",
  gulf_regional:    "C",
};

export const NewsReelSchema = z.object({
  dateLabel: z.string(),
  arabicDateLabel: z.string(),
  handle: z.string().default("@photonect.news"),
  audioBed: z.string().optional(),
  variant: z.enum(VARIANT_VALUES).optional(),
  topicBucket: z.enum(TOPIC_BUCKETS).optional(),
  breaking: z.object({
    arabicKicker: z.string().default("عاجل"),
    arabicHeadline: z.string(),
    englishSubhead: z.string(),
    heroMedia: z.string(),
    heroMediaType: z.enum(["video", "image"]).default("video"),
  }),
  beats: z.array(Beat).length(3),
  sources: z.array(Source).min(3).max(8),
  arabicTicker: z.array(z.string()).min(3).max(8),
});

export type NewsReelProps = z.infer<typeof NewsReelSchema>;
export type BeatProps = z.infer<typeof Beat>;
export type BigStatProps = z.infer<typeof BigStat>;
export type SourceProps = z.infer<typeof Source>;

// V10 (2026-05-29) — Ahmed feedback (again): "text is too much and the speed to
// show it is too fast, I can't read the facts." V9's 13s wasn't enough. Two
// levers pulled together: (1) beats extended 13s → 15s here, and (2) every
// variant's reveal schedule compressed so all text lands by ~frame 90 (3s) and
// then HOLDS for ~12s. Net readable-hold per beat jumps from ~7s to ~12s.
// Breaking 150f (5s) + Beat 450f ×3 + Sources 90f = 1590f @ 30fps = 53s.
// MultiShotBackdrop cycles 4 shots/beat at 112.5f each (3.75s/shot — calmer cuts).
export const BREAKING_FRAMES = 150;
export const BEAT_FRAMES = 450;
export const BEAT3_FRAMES = 450;
export const SOURCES_FRAMES = 90;

export const computeNewsReelDurationInFrames = () =>
  BREAKING_FRAMES + BEAT_FRAMES + BEAT_FRAMES + BEAT3_FRAMES + SOURCES_FRAMES;

// Resolve a reel's variant: explicit reel.variant wins, else bucket map, else "A".
export const resolveVariant = (
  explicit: VariantName | undefined,
  bucket: string | undefined,
): VariantName => {
  if (explicit) return explicit;
  if (bucket && BUCKET_VARIANT[bucket]) return BUCKET_VARIANT[bucket];
  return "A";
};
