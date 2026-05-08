import React from "react";
import { useCurrentFrame, interpolate, Easing } from "remotion";

/**
 * SourceChip — V7 leap component.
 *
 * Lower-left attribution chip that shows the source of the current scene's
 * broll. Inspired by the Vox / C4 / Reuters pattern of keeping credibility
 * as a continuous design element rather than an end-card afterthought.
 *
 * Position: 32px from left, 28px from bottom of the beat content frame
 * (above any subtitle bar, in the safe zone). Style: 11pt mono-like sans,
 * 70% white, 0.4 letter-spacing, all caps, no background — just the chip.
 *
 * Reveals at the same moment the broll cuts in (frame 6 inside the beat),
 * holds for the rest of the beat, and fades out on the last 6 frames.
 */
export const SourceChip: React.FC<{
  /** e.g. "REUTERS · MAY 6", "WIKIMEDIA · CC-BY", "AP · BAGHDAD" */
  source?: string;
  /** total frames the chip's parent scene lasts; used for the closing fade */
  durationFrames: number;
}> = ({ source, durationFrames }) => {
  const frame = useCurrentFrame();
  if (!source) return null;

  // Reveal in 6-18, hold, fade out in last 6 frames
  const fadeIn = interpolate(frame, [6, 18], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.quad),
  });
  const fadeOut = interpolate(
    frame,
    [durationFrames - 6, durationFrames],
    [1, 0],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" },
  );
  const opacity = Math.min(fadeIn, fadeOut) * 0.7;

  // Slide in from x:-12 to 0
  const x = interpolate(frame, [6, 18], [-12, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.quad),
  });

  return (
    <div
      style={{
        position: "absolute",
        left: 36,
        bottom: 132, // sits above the SubtitleBar (~96px tall + 36 padding)
        opacity,
        transform: `translateX(${x}px)`,
        fontFamily: '"IBM Plex Mono", "SF Mono", monospace',
        fontSize: 16,
        fontWeight: 500,
        color: "#fff",
        letterSpacing: "0.18em",
        textTransform: "uppercase",
        // tiny gold accent dot in front for credibility-as-design feel
        display: "flex",
        alignItems: "center",
        gap: 10,
        pointerEvents: "none",
      }}
    >
      <span
        style={{
          width: 6,
          height: 6,
          borderRadius: 6,
          background: "#FFC217",
          boxShadow: "0 0 8px rgba(255,194,23,0.6)",
        }}
      />
      <span>{source}</span>
    </div>
  );
};
