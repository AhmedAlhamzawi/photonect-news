import React from "react";
import {
  AbsoluteFill,
  interpolate,
  useCurrentFrame,
  staticFile,
  Img,
  Easing,
} from "remotion";
import { PHOTONECT } from "../../PhotonectBrandReel/brand";

/**
 * MultiShotBackdrop — V8 leap (2026-05-10).
 *
 * Replaces the V6 single-photo Ken Burns hold with a multi-shot cycle that
 * cuts between 3-6 photos over the beat's runtime. The pattern every world-
 * class news short-form reel uses (median 1.8s/shot in the top decile per
 * Buffer 2024 data; AJ Arabic / Vox / BBC all do this).
 *
 * Each shot gets:
 *   - 8-frame crossfade in (overlapping the previous shot's tail)
 *   - subtle per-shot Ken Burns: zoom 1.06 → 1.10 with a small panX offset
 *     that varies per shot index so consecutive shots don't feel identical
 *   - hold for ~85% of its window
 *   - 8-frame crossfade out into the next
 *
 * Top of frame is darker so the upper-area chrome (kicker chip / chapter card)
 * stays readable; bottom is darker so the SubtitleBar stays readable. The
 * mid-band is the brightest part — that's where the photo content lives.
 */

type Props = {
  shots: string[];
  durationFrames: number;
  accent: string;
  /** When true, applies the heavier "hero" overlay; lighter for beats. */
  intensity?: "hero" | "beat";
};

const PER_SHOT_FADE = 8; // frames

export const MultiShotBackdrop: React.FC<Props> = ({
  shots,
  durationFrames,
  accent,
  intensity = "beat",
}) => {
  const frame = useCurrentFrame();

  // Defensive — fall back to a black fill if the array is empty
  if (!shots || shots.length === 0) {
    return <AbsoluteFill style={{ background: PHOTONECT.ink }} />;
  }

  const shotDuration = durationFrames / shots.length;

  // Light overlay so headlines, chips, and subtitle bar all stay readable.
  // Calibrated: top 13% / mid 18% / bottom 47% (hero intensity).
  // Beat intensity is heavier all around since beats also carry text + stats.
  const overlay =
    intensity === "hero"
      ? `linear-gradient(180deg, ${PHOTONECT.ink}22 0%, ${PHOTONECT.ink}30 35%, ${PHOTONECT.ink}77 100%)`
      : `linear-gradient(180deg, ${PHOTONECT.ink}55 0%, ${PHOTONECT.ink}40 35%, ${PHOTONECT.ink}AA 100%)`;

  return (
    <AbsoluteFill
      style={{
        overflow: "hidden",
        background: PHOTONECT.ink,
      }}
    >
      {/* Each shot is a layered AbsoluteFill that fades in/out at its window */}
      {shots.map((shotPath, i) => {
        const start = i * shotDuration;
        const end = start + shotDuration;

        // Crossfade in: 0 → 1 over PER_SHOT_FADE frames at shot start
        // Crossfade out: 1 → 0 over PER_SHOT_FADE frames at shot end (overlaps next)
        // EXCEPT the last shot, which holds its opacity to the end.
        const fadeIn = interpolate(
          frame,
          [start - PER_SHOT_FADE / 2, start + PER_SHOT_FADE / 2],
          [0, 1],
          { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.bezier(0.16, 1, 0.3, 1) },
        );
        const fadeOut = i === shots.length - 1
          ? 1
          : interpolate(
              frame,
              [end - PER_SHOT_FADE / 2, end + PER_SHOT_FADE / 2],
              [1, 0],
              { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.bezier(0.16, 1, 0.3, 1) },
            );
        const opacity = Math.min(fadeIn, fadeOut);

        // Per-shot Ken Burns. Vary the zoom direction and pan per shot index
        // so the cycle never feels mechanical. shot[0] zooms in slowly,
        // shot[1] pans right, shot[2] zooms out, shot[3]+ alternate.
        const localProgress = (frame - start) / shotDuration; // 0 → 1
        const clamped = Math.max(0, Math.min(1, localProgress));
        let zoomFrom = 1.06;
        let zoomTo = 1.10;
        let panX = 0;
        switch (i % 4) {
          case 0:
            zoomFrom = 1.06; zoomTo = 1.12; panX = 0; break;
          case 1:
            zoomFrom = 1.10; zoomTo = 1.10; panX = -2 + clamped * 4; break; // pan -2% → +2%
          case 2:
            zoomFrom = 1.18; zoomTo = 1.06; panX = 2; break;                // zoom OUT
          case 3:
            zoomFrom = 1.04; zoomTo = 1.08; panX = -1; break;
        }
        const zoom = zoomFrom + (zoomTo - zoomFrom) * clamped;
        const resolved = shotPath.startsWith("http") ? shotPath : staticFile(shotPath);

        // Skip rendering shots that are fully invisible — saves a bit of decode work
        if (opacity <= 0.001 && (frame < start - PER_SHOT_FADE || frame > end + PER_SHOT_FADE)) {
          return null;
        }

        return (
          <AbsoluteFill
            key={`${i}-${shotPath}`}
            style={{ opacity, willChange: "opacity, transform" }}
          >
            <AbsoluteFill
              style={{
                transform: `scale(${zoom}) translateX(${panX}%)`,
                filter: "saturate(0.92) contrast(1.06)",
              }}
            >
              <Img
                src={resolved}
                style={{
                  width: "100%",
                  height: "100%",
                  objectFit: "cover",
                }}
              />
            </AbsoluteFill>
          </AbsoluteFill>
        );
      })}

      {/* Overlay gradient — readability anchor */}
      <AbsoluteFill style={{ background: overlay, pointerEvents: "none" }} />

      {/* Accent scanlines for hero intensity (matches V6 VideoBackdrop look) */}
      {intensity === "hero" && (
        <AbsoluteFill
          style={{
            backgroundImage: `repeating-linear-gradient(0deg, ${accent}09 0, ${accent}09 1px, transparent 1px, transparent 5px)`,
            mixBlendMode: "screen",
            pointerEvents: "none",
          }}
        />
      )}

      {/* Inset shadow vignette for cinematic edges */}
      <AbsoluteFill
        style={{
          pointerEvents: "none",
          boxShadow:
            intensity === "hero"
              ? `inset 0 0 0 2px ${accent}33, inset 0 0 120px ${PHOTONECT.ink}99`
              : `inset 0 0 0 2px ${accent}22, inset 0 0 80px ${PHOTONECT.ink}88`,
        }}
      />

      {/* Cut indicator — a faint horizontal accent line that flashes briefly
          on each shot transition. Cinematic sting that signals "we cut". */}
      {shots.map((_, i) => {
        if (i === 0) return null;
        const cutAt = i * shotDuration;
        const flash = interpolate(
          frame,
          [cutAt - 2, cutAt + 2, cutAt + 8],
          [0, 1, 0],
          { extrapolateLeft: "clamp", extrapolateRight: "clamp" },
        );
        if (flash <= 0.001) return null;
        return (
          <AbsoluteFill
            key={`cut-${i}`}
            style={{
              pointerEvents: "none",
              opacity: flash * 0.5,
              background: `linear-gradient(180deg, transparent 0%, ${accent}33 49%, ${accent}66 50%, ${accent}33 51%, transparent 100%)`,
              mixBlendMode: "screen",
            }}
          />
        );
      })}
    </AbsoluteFill>
  );
};
