import { z } from "zod";

// Parametrized brand travel reel — one composition → N clients (Sindibad first).
// All copy is authored in props; nothing is AI-generated at render time.

export const Destination = z.object({
  image: z.string(), // staticFile path under public/
  index: z.string(), // "01"
  tag: z.string(), // crimson pill, e.g. "تراث UNESCO"
  name: z.string(), // big Arabic destination name
  descriptor: z.string(), // one-line Arabic descriptor
});
export type DestinationT = z.infer<typeof Destination>;

export const BrandTravelReelSchema = z.object({
  brand: z.object({
    name: z.string(),
    crimson: z.string(),
    cream: z.string(),
    sand: z.string(),
    ink: z.string(),
    logo: z.string(),
    handle: z.string(),
  }),
  audio: z.string(),
  intro: z.object({
    image: z.string(),
    kicker: z.string(),
    hook: z.string(),
    subhead: z.string(),
  }),
  destinations: z.array(Destination).min(1).max(6),
  outro: z.object({
    headline: z.string(),
    subline: z.string(),
  }),
});
export type BrandTravelReelProps = z.infer<typeof BrandTravelReelSchema>;

// ---- timing (seconds × fps, never hardcoded frame magic) ----
export const FPS = 30;
export const INTRO_F = 4.2 * FPS; // 126
export const DEST_F = 5.4 * FPS; // 162
export const OUTRO_F = 4.0 * FPS; // 120
export const TRANS_F = 0.5 * FPS; // 15

export const computeTravelDuration = (n: number): number =>
  Math.round(INTRO_F + n * DEST_F + OUTRO_F - TRANS_F * (n + 1));
