import { z } from "zod";

// ── NewsReel V11 — the VO-spine reel (2026-07-03 growth overhaul) ────────────
// Inversion of V10: the narrator drives the timeline. 28-34s single-story unit,
// cold open (no title card), kinetic multi-crop visuals cut on word boundaries,
// karaoke captions, one big stat pop, question end-card. All timing is baked by
// the props builder (scripts/build_v11_props.py) from words.json — the comp is
// deliberately dumb: it renders exactly what props say, so a malformed timestamp
// fails at BUILD time, never at render time.

export const v11WordSchema = z.object({
  word: z.string(),
  startF: z.number(), // frames @30fps, absolute
  endF: z.number(),
});

export const v11LineSchema = z.object({
  words: z.array(v11WordSchema).min(1),
  startF: z.number(),
  endF: z.number(),
});

export const v11ShotSchema = z.object({
  img: z.string(),          // staticFile-relative image path
  startF: z.number(),
  durationF: z.number(),
  // Ken-Burns move: crop rectangle animates from->to (unit = fraction of image)
  fromScale: z.number().default(1.08),
  toScale: z.number().default(1.22),
  fromX: z.number().default(0),   // -1..1 pan offsets
  fromY: z.number().default(0),
  toX: z.number().default(0),
  toY: z.number().default(0),
});

export const v11StatPopSchema = z.object({
  value: z.string(),        // "1470" or "11%"
  labelArabic: z.string(),
  atFrame: z.number(),      // when it pops (word-synced by the builder)
  holdFrames: z.number().default(75),
});

export const newsReelV11Schema = z.object({
  kicker: z.string().default("عاجل"),          // top chip label
  hookHeadline: z.string(),                     // kinetic text landing ~frame 12
  vo: z.string(),                               // staticFile-relative vo.mp3
  audioBed: z.string().default(""),             // music bed (ducked under VO)
  bedVolume: z.number().default(0.16),
  shots: z.array(v11ShotSchema).min(3),
  lines: z.array(v11LineSchema).min(1),         // karaoke caption lines
  statPops: z.array(v11StatPopSchema).default([]),
  endQuestion: z.string(),                      // the open question card
  handle: z.string().default("@photonect.news"),
  sourcesLine: z.string().default(""),          // tiny attribution strip, e.g. "المصادر: رويترز · AP"
  totalFrames: z.number(),                      // VO frames + end-card
});

export type NewsReelV11Props = z.infer<typeof newsReelV11Schema>;

export const V11_FPS = 30;
export const V11_ENDCARD_FRAMES = 75; // 2.5s question + brand sting

export const computeV11Duration = (props: { totalFrames: number }): number =>
  Math.max(90, props.totalFrames);
