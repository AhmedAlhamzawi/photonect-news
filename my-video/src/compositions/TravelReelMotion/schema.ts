import { z } from "zod";

// Motion travel reel — real video b-roll (Veo clips), vibrant, fast cuts.
export const MScene = z.object({
  clip: z.string(), // staticFile path to mp4
  startFrom: z.number(), // frame offset into the clip to begin
  name: z.string(),
  tag: z.string(),
});
export type MSceneT = z.infer<typeof MScene>;

export const TravelReelMotionSchema = z.object({
  brand: z.object({
    name: z.string(),
    crimson: z.string(),
    cream: z.string(),
    ink: z.string(),
    logo: z.string(),
    handle: z.string(),
  }),
  audio: z.string(),
  audioStartFrom: z.number().default(0),
  hook: z.object({
    clip: z.string(),
    startFrom: z.number(),
    line1: z.string(),
    line2: z.string(),
    save: z.string(),
  }),
  scenes: z.array(MScene).min(1).max(6),
  outro: z.object({
    headline: z.string(),
    subline: z.string(),
  }),
});
export type TravelReelMotionProps = z.infer<typeof TravelReelMotionSchema>;

// ---- timing — fast travel cadence ----
export const FPS = 30;
export const HOOK_F = Math.round(4.0 * FPS); // 120
export const DEST_F = Math.round(3.9 * FPS); // 117
export const OUTRO_F = Math.round(3.6 * FPS); // 108

export const computeMotionDuration = (n: number): number =>
  HOOK_F + n * DEST_F + OUTRO_F;
