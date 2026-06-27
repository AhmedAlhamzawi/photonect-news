import { z } from "zod";

// ── Photonect ESSAY — a variable-length cinematic video-essay track ──────────
// Unlike NewsReel (frozen 3-beat / 1590f contract), an Essay flexes: N segments,
// each with its own durationFrames, mirroring the Hekaya2 variable-duration model.
// Spine = the 7-beat steelman→critique→reframe→resolve arc, narrated MSA rap over
// AI-video b-roll with audio-reactive EQ bars, sourced number counters, RTL captions.

export const essayCounterSchema = z.object({
  value: z.string(),
  label_ar: z.string(),
  source: z.string(),
  as_of: z.string().optional().default(""),
  unit: z.string().optional().default(""),
});

export const essaySegmentSchema = z.object({
  beat_role: z.string(), // hook | steelman | turn | critique | concession | reframe | resolve
  arabic_vo: z.string(), // the rapped MSA bars (lines separated by " / ")
  broll: z.string(), // staticFile-relative path to this beat's video clip
  brollSeconds: z.number().default(8), // source clip length (for fit playbackRate)
  eq_tone: z.enum(["cyan", "amber", "red"]).default("cyan"),
  durationFrames: z.number(),
  counters: z.array(essayCounterSchema).default([]),
});

export const essaySchema = z.object({
  titleArabic: z.string(),
  kicker: z.string().default("تحليل"), // top-strip label
  handle: z.string().default("@photonect.news"),
  dateLabel: z.string().default(""),
  audio: z.string(), // staticFile-relative MSA-rap track
  audioFadeOutFrames: z.number().default(45),
  segments: z.array(essaySegmentSchema).min(1),
});

export type EssayProps = z.infer<typeof essaySchema>;
export type EssaySegment = z.infer<typeof essaySegmentSchema>;
export type EssayCounter = z.infer<typeof essayCounterSchema>;

// Cross-dissolve length between segments (frames @ 30fps).
export const ESSAY_TRANSITION_FRAMES = 18;

// Total composition length: segments laid back-to-back, each pair overlapped by
// one cross-dissolve. total = Σ durations − (N−1)·transition.
export const computeEssayDuration = (
  segments: { durationFrames: number }[],
): number => {
  const sum = segments.reduce((a, s) => a + s.durationFrames, 0);
  return Math.max(1, sum - Math.max(0, segments.length - 1) * ESSAY_TRANSITION_FRAMES);
};
