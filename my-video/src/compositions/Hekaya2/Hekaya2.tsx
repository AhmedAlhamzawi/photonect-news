import React from "react";
import {
  AbsoluteFill,
  Audio,
  Sequence,
  interpolate,
  useCurrentFrame,
  staticFile,
} from "remotion";
import {
  Hekaya2Props,
  HEKAYA2_TOTAL_FRAMES,
  HEKAYA2_PHASES,
  HEKAYA_PALETTE,
  dbToLinear,
} from "./schema";
import { ColdOpen } from "./scenes/ColdOpen";
import { Chapter } from "./scenes/Chapter";
import { SilencePivot } from "./scenes/SilencePivot";
import { Resonance } from "./scenes/Resonance";

/**
 * HEKAYA v2 — narrated mini-documentary, 75 seconds.
 *
 * Audio architecture (4 layers):
 *   - VO (the spine, -6 dB ≈ 0.5 linear)
 *   - Music (Suno track, ducked under VO at -18 dB, swells -10 dB at climax,
 *     full silence during the pivot phase)
 *   - SFX/foley markers (each at its own dB target, default -22 dB)
 *
 * Visual architecture (4 scenes):
 *   - ColdOpen (0-8s) — hero detail, lower-third title at 2s
 *   - Chapter ×3 (8-45s, 46-65s) — photo cycles + phrase reveals
 *   - SilencePivot (45-46s) — single image, full silence
 *   - Resonance (65-75s) — closing image + loop hook, cold-cut at 1:15
 */
export const Hekaya2: React.FC<Hekaya2Props> = ({
  dateLabel,
  arabicDateLabel,
  handle,
  voiceOver,
  music,
  sfx,
  title,
  phrases,
  heroMedia,
  chapters,
  closingMedia,
  loopHook,
  sources,
}) => {
  const frame = useCurrentFrame();

  // ── Music volume curve ──────────────────────────────────────────
  // Cold open: silent until 1.2s (frame 36), then ramp to ducked -18 dB.
  // Climax: swell from -18 dB to -10 dB over 60 frames.
  // Silence pivot: zero for the full 30 frames.
  // Loop ending: cold-cut to zero in the last 5 frames.
  const musicVol = (() => {
    if (
      frame >= HEKAYA2_PHASES.SILENCE_PIVOT.start &&
      frame < HEKAYA2_PHASES.SILENCE_PIVOT.end
    ) {
      return 0; // full silence pivot
    }
    if (frame < 36) return 0; // cold-open lead-in (foley + VO only)
    if (frame < 48) {
      return interpolate(frame, [36, 48], [0, dbToLinear(-18)], {
        extrapolateRight: "clamp",
      });
    }
    if (
      frame >= HEKAYA2_PHASES.CLIMAX.start &&
      frame < HEKAYA2_PHASES.CLIMAX.start + 60
    ) {
      return interpolate(
        frame,
        [HEKAYA2_PHASES.CLIMAX.start, HEKAYA2_PHASES.CLIMAX.start + 60],
        [dbToLinear(-18), dbToLinear(-10)],
        { extrapolateRight: "clamp" },
      );
    }
    if (
      frame >= HEKAYA2_PHASES.CLIMAX.start + 60 &&
      frame < HEKAYA2_PHASES.RESOLUTION.start
    ) {
      return dbToLinear(-10);
    }
    if (frame >= HEKAYA2_TOTAL_FRAMES - 5) return 0;
    return dbToLinear(-18);
  })();

  // ── VO volume curve ─────────────────────────────────────────────
  // Steady at -6 dB, silent during pivot, cold-cut at end.
  const voVol = (() => {
    if (
      frame >= HEKAYA2_PHASES.SILENCE_PIVOT.start &&
      frame < HEKAYA2_PHASES.SILENCE_PIVOT.end
    ) {
      return 0;
    }
    if (frame >= HEKAYA2_TOTAL_FRAMES - 5) return 0;
    return dbToLinear(-6);
  })();

  const voSrc = voiceOver.startsWith("http") ? voiceOver : staticFile(voiceOver);
  const musicSrc = music.startsWith("http") ? music : staticFile(music);

  return (
    <AbsoluteFill style={{ backgroundColor: HEKAYA_PALETTE.ink }}>
      {/* Audio layers — VO + music + each SFX marker */}
      <Audio src={voSrc} volume={voVol} />
      <Audio src={musicSrc} volume={musicVol} />
      {sfx.map((s, i) => (
        <Sequence key={i} from={s.startFrame}>
          <Audio src={staticFile(s.file)} volume={dbToLinear(s.volumeDb)} />
        </Sequence>
      ))}

      {/* Cold open + inciting (0-8s, frames 0-240) */}
      <Sequence from={0} durationInFrames={HEKAYA2_PHASES.INCITING.end}>
        <ColdOpen
          hero={heroMedia}
          title={title}
          durationFrames={HEKAYA2_PHASES.INCITING.end}
        />
      </Sequence>

      {/* Chapter 1 (covers WANT + OBSTACLE_1, frames 240-750) */}
      <Sequence
        from={chapters[0].startFrame}
        durationInFrames={chapters[0].durationFrames}
      >
        <Chapter
          cycle={chapters[0]}
          phrases={phrases}
          absoluteStart={chapters[0].startFrame}
        />
      </Sequence>

      {/* Chapter 2 (ESCALATION_1 + ESCALATION_2, frames 750-1350) */}
      <Sequence
        from={chapters[1].startFrame}
        durationInFrames={chapters[1].durationFrames}
      >
        <Chapter
          cycle={chapters[1]}
          phrases={phrases}
          absoluteStart={chapters[1].startFrame}
        />
      </Sequence>

      {/* Silence pivot (frames 1350-1380, 1s of full silence) */}
      <Sequence
        from={HEKAYA2_PHASES.SILENCE_PIVOT.start}
        durationInFrames={
          HEKAYA2_PHASES.SILENCE_PIVOT.end - HEKAYA2_PHASES.SILENCE_PIVOT.start
        }
      >
        <SilencePivot
          pivotImage={chapters[1].photos[chapters[1].photos.length - 1]}
        />
      </Sequence>

      {/* Chapter 3 (CLIMAX + RESOLUTION, frames 1380-1950) */}
      <Sequence
        from={chapters[2].startFrame}
        durationInFrames={chapters[2].durationFrames}
      >
        <Chapter
          cycle={chapters[2]}
          phrases={phrases}
          absoluteStart={chapters[2].startFrame}
        />
      </Sequence>

      {/* Resonance + loop (frames 1950-2250, 65-75s) */}
      <Sequence
        from={HEKAYA2_PHASES.RESONANCE.start}
        durationInFrames={
          HEKAYA2_TOTAL_FRAMES - HEKAYA2_PHASES.RESONANCE.start
        }
      >
        <Resonance
          closingMedia={closingMedia}
          loopHook={loopHook}
          handle={handle}
          sources={sources}
          durationFrames={
            HEKAYA2_TOTAL_FRAMES - HEKAYA2_PHASES.RESONANCE.start
          }
        />
      </Sequence>

      {/* Persistent date stamps — slim chrome, never animates */}
      <div
        style={{
          position: "absolute",
          bottom: 70,
          left: 50,
          color: HEKAYA_PALETTE.ivory,
          fontFamily: "system-ui, -apple-system, sans-serif",
          fontSize: 16,
          letterSpacing: 4,
          fontWeight: 500,
          opacity: 0.55,
          textTransform: "uppercase",
        }}
      >
        {dateLabel}
      </div>
      <div
        dir="rtl"
        style={{
          position: "absolute",
          bottom: 70,
          right: 50,
          color: HEKAYA_PALETTE.ivory,
          fontFamily: "Tajawal, system-ui, sans-serif",
          fontSize: 18,
          fontWeight: 500,
          opacity: 0.55,
        }}
      >
        {arabicDateLabel}
      </div>
    </AbsoluteFill>
  );
};
