import { z } from "zod";

// HEKAYA v2 schema — built per docs/superpowers/specs/2026-05-04-hekaya-v2-design.md.
// v1 schema lives at compositions/Hekaya/schema.ts and stays untouched.

const Source = z.object({
  name: z.string(),
  domain: z.string(),
});

// Phrase-by-phrase reveal marker. Drives kinetic typography timed to VO audio.
// Each marker = one Arabic phrase shown on screen.
const PhraseMarker = z.object({
  arabicText: z.string(),
  startFrame: z.number(),
  durationFrames: z.number(),
  layoutType: z.enum([
    "lower-third",
    "full-bleed-quote",
    "single-word",
    "photo-caption",
  ]),
  // Optional word inside arabicText that gets the gold flash for 4 frames.
  keyWord: z.string().optional(),
});

// Foley/SFX marker for the audio layer. The composition spawns one Audio
// element per marker, each gain-staged independently.
const SfxMarker = z.object({
  file: z.string(), // e.g. "audio/hekaya-sfx/reed-pen.mp3"
  startFrame: z.number(),
  // dB gain. -22 by default (committee 6 spec). Linear gain = 10^(db/20).
  volumeDb: z.number().default(-22),
});

// One chapter's photo cycle — 5-7 stills with shot-ladder variety.
// The Chapter scene cycles through these on a metronomic ~2.5s cadence.
const ChapterCycle = z.object({
  startFrame: z.number(),
  durationFrames: z.number(),
  photos: z.array(z.string()).min(4).max(8),
});

export const Hekaya2Schema = z.object({
  dateLabel: z.string(),
  arabicDateLabel: z.string(),
  handle: z.string().default("@photonect.news"),

  // ── AUDIO ────────────────────────────────────────────────────────
  voiceOver: z.string(), // VO mp3 path (the spine)
  music: z.string(),     // Suno music mp3 (ducked under VO)
  sfx: z.array(SfxMarker).default([]),

  // ── TITLE METADATA ───────────────────────────────────────────────
  title: z.object({
    arabic: z.string(),         // 5-8 word lyrical Arabic title
    englishSubtitle: z.string(), // ~6-12 word ALL-CAPS Latin subtitle
    era: z.string(),            // "859 AD" / "9th Century"
    place: z.string(),          // "Fez, Morocco"
  }),

  // ── SCRIPT ───────────────────────────────────────────────────────
  // The full VO script — used for caption.txt generation, NOT rendered.
  scriptArabic: z.string(),

  // Phrase markers drive on-screen kinetic typography. Time them so each
  // phrase appears as the narrator says it, with a 14-frame mask wipe
  // reveal. See PhraseReveal component for the visual treatment.
  phrases: z.array(PhraseMarker),

  // ── VISUAL CONTENT ───────────────────────────────────────────────
  heroMedia: z.string(),         // first image — cold-open detail
  // Three chapter scenes covering 8-65s. Each with its own photo cycle.
  chapters: z.array(ChapterCycle).length(3),
  closingMedia: z.string(),      // resonance scene image

  // ── LOOP ENGINEERING ─────────────────────────────────────────────
  loopHook: z.object({
    openingPhrase: z.string(),  // what the opening line is
    closingPhrase: z.string(),  // what the closing line says — must echo opening
  }),

  sources: z.array(Source).min(2).max(6),
});

export type Hekaya2Props = z.infer<typeof Hekaya2Schema>;
export type PhraseMarkerProps = z.infer<typeof PhraseMarker>;
export type SfxMarkerProps = z.infer<typeof SfxMarker>;
export type ChapterCycleProps = z.infer<typeof ChapterCycle>;

// 75s @ 30fps = 2250 frames. Mapped to story-craft phases.
export const HEKAYA2_TOTAL_FRAMES = 2250;
export const HEKAYA2_FPS = 30;

// Story-craft phase boundaries, in absolute frames from composition start.
// Used by the composition + props authors so timing stays consistent.
export const HEKAYA2_PHASES = {
  COLD_OPEN: { start: 0, end: 60 },             // 0-2s: hero detail, no title yet
  INCITING: { start: 60, end: 240 },            // 2-8s: world breaks; title slides in
  WANT: { start: 240, end: 525 },               // 8-17.5s: protagonist + felt want
  OBSTACLE_1: { start: 525, end: 750 },         // 17.5-25s: first try fails
  ESCALATION_1: { start: 750, end: 1050 },      // 25-35s: stakes raise
  ESCALATION_2: { start: 1050, end: 1350 },     // 35-45s: third complication
  SILENCE_PIVOT: { start: 1350, end: 1380 },    // 45-46s: full silence (1s)
  CLIMAX: { start: 1380, end: 1650 },           // 46-55s: reveal/turn
  RESOLUTION: { start: 1650, end: 1950 },       // 55-65s: aftermath
  RESONANCE: { start: 1950, end: 2160 },        // 65-72s: final image + 6-word line
  LOOP: { start: 2160, end: 2250 },             // 72-75s: cold-cut back to opener
} as const;

// Reused palette from v1.
export const HEKAYA_PALETTE = {
  ink: "#0B1A2A",
  gold: "#D4A668",
  ivory: "#F5EBD8",
  rose: "#C4806B",
  shadow: "#06101C",
  vellum: "#E8DCC4",
} as const;

// Convert -dB to linear gain. Used by the audio layer for SFX volumes.
export const dbToLinear = (db: number) => Math.pow(10, db / 20);
