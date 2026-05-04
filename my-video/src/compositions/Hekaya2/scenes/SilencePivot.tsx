import React from "react";
import { AbsoluteFill, interpolate, useCurrentFrame } from "remotion";
import { HEKAYA_PALETTE } from "../schema";
import { ParallaxImage } from "../components/ParallaxImage";

interface Props {
  pivotImage: string;
}

/**
 * The 30-frame (1s) silence pivot at 45-46s — Walter Murch's "white frame
 * in audio." The composition zeroes the audio for this window; this scene
 * holds a single still with a subtle vignette pulse and nothing else.
 *
 * Intentionally minimal — no embers, no text, no kinetic typography.
 * The silence does the work; the image just breathes.
 */
export const SilencePivot: React.FC<Props> = ({ pivotImage }) => {
  const frame = useCurrentFrame();

  // Vignette pulse — subtle breath that signals the pause is intentional
  const pulseOpacity = interpolate(
    frame,
    [0, 15, 30],
    [0.6, 0.85, 0.6],
    { extrapolateRight: "clamp" },
  );

  return (
    <AbsoluteFill style={{ backgroundColor: HEKAYA_PALETTE.ink }}>
      <ParallaxImage src={pivotImage} durationFrames={30} direction="in" />
      <AbsoluteFill
        style={{
          background: `radial-gradient(ellipse at center,
            transparent 25%,
            ${HEKAYA_PALETTE.ink} 90%)`,
          opacity: pulseOpacity,
        }}
      />
    </AbsoluteFill>
  );
};
