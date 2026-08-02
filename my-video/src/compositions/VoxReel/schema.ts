import { z } from "zod";

// ── VOX REEL — editorial motion-graphics explainer ───────────────────────────
// A code-native reproduction of the Vox "mixed media collage" look: flat colour
// fields, archival cutouts with rough paper borders, halftone + paper grain,
// hand-drawn marker annotations that DRAW THEMSELVES, abstract charts that grow,
// snappy pop-in with overshoot, slow push-ins, whip transitions between blocks.
//
// Why Remotion instead of AI video: real Vox motion graphics ARE keyframed
// design, not filmed or generated footage. Animating in code gives us genuine
// snap, exact timing on the narration, and deterministic re-renders — an
// AI-video model can only approximate the look and cannot hit word-level beats.

export const voxAnnotationSchema = z.object({
  // marker circle / underline / arrow that draws itself on
  kind: z.enum(["circle", "underline", "arrow", "bracket"]).default("circle"),
  atFrame: z.number(),          // when the stroke starts drawing
  drawFrames: z.number().default(14),
  // normalised placement 0..1 of the canvas
  x: z.number(), y: z.number(), w: z.number().default(0.4), h: z.number().default(0.22),
  color: z.string().default("#0A0A10"),
});

export const voxBarsSchema = z.object({
  atFrame: z.number(),
  values: z.array(z.number()).min(2),   // 0..1 heights, grow in sequence
  x: z.number().default(0.58), y: z.number().default(0.62),
  w: z.number().default(0.34), h: z.number().default(0.26),
  color: z.string().default("#D72638"),
});

export const voxBlockSchema = z.object({
  arabicVo: z.string(),          // the narration line (also the caption source)
  collage: z.string(),           // staticFile path to the generated collage art
  bg: z.string().default("#F2E9D8"),   // flat colour field behind the collage
  accent: z.string().default("#FFC217"),
  startF: z.number(),
  durationF: z.number(),
  // motion
  pushIn: z.number().default(0.10),    // camera push over the block (fraction)
  driftX: z.number().default(0),       // lateral parallax drift
  annotations: z.array(voxAnnotationSchema).default([]),
  bars: voxBarsSchema.optional(),
  // the recurring through-line object, drawn as an escalating motif
  throughline: z.number().default(0),  // 0..1 escalation level for this block
});

export const voxCaptionWordSchema = z.object({
  word: z.string(), startF: z.number(), endF: z.number(),
});
export const voxCaptionLineSchema = z.object({
  words: z.array(voxCaptionWordSchema).min(1),
  startF: z.number(), endF: z.number(),
});

export const voxReelSchema = z.object({
  titleArabic: z.string(),
  vo: z.string(),                       // narration audio
  audioBed: z.string().default(""),
  bedVolume: z.number().default(0.14),
  blocks: z.array(voxBlockSchema).min(1),
  lines: z.array(voxCaptionLineSchema).default([]),
  handle: z.string().default("@photonect.news"),
  sourcesLine: z.string().default(""),
  endQuestion: z.string().default(""),
  totalFrames: z.number(),
});

export type VoxReelProps = z.infer<typeof voxReelSchema>;
export type VoxBlock = z.infer<typeof voxBlockSchema>;

export const VOX_FPS = 30;
export const VOX_ENDCARD_F = 72;
export const computeVoxDuration = (p: { totalFrames: number }) => Math.max(90, p.totalFrames);
