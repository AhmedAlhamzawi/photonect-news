import React from "react";
import { AbsoluteFill, interpolate, useCurrentFrame, Easing } from "remotion";
import { Hekaya2Props, HEKAYA_PALETTE } from "../schema";
import { ParallaxImage } from "../components/ParallaxImage";
import { Embers } from "../components/Embers";

interface Props {
  closingMedia: string;
  loopHook: Hekaya2Props["loopHook"];
  handle: string;
  sources: Hekaya2Props["sources"];
  durationFrames: number;
}

/**
 * Resonance — the final 65-75s window. Closing image + the loop hook
 * (a closing phrase that echoes the opening, so the loop feels causal,
 * not repetitive). Handle + sources strip slides in toward the end.
 *
 * NO fade-out at the end — the composition ends on a cold cut so the
 * Instagram loop snaps back to 0:00 cleanly. Fades signal "over"; cold
 * cuts let the loop work.
 */
export const Resonance: React.FC<Props> = ({
  closingMedia,
  loopHook,
  handle,
  sources,
  durationFrames,
}) => {
  const frame = useCurrentFrame();

  // Closing phrase fades in at frame 0-30, settles, holds
  const closingOpacity = interpolate(frame, [0, 30], [0, 1], {
    extrapolateRight: "clamp",
  });
  const closingY = interpolate(frame, [0, 40], [20, 0], {
    easing: Easing.bezier(0.16, 1, 0.3, 1),
    extrapolateRight: "clamp",
  });

  // Handle + sources fade in toward the end, sustain to the cold-cut
  const handleOpacity = interpolate(
    frame,
    [80, 120, durationFrames - 6, durationFrames],
    [0, 1, 1, 1],
    { extrapolateRight: "clamp" },
  );

  return (
    <AbsoluteFill style={{ backgroundColor: HEKAYA_PALETTE.ink }}>
      <ParallaxImage
        src={closingMedia}
        durationFrames={durationFrames}
        direction="out"
      />
      <Embers />

      {/* Closing phrase — the loop hook */}
      <div
        style={{
          position: "absolute",
          top: "32%",
          left: 80,
          right: 80,
          textAlign: "center",
          opacity: closingOpacity,
          transform: `translateY(${closingY}px)`,
        }}
      >
        <div
          dir="rtl"
          style={{
            color: HEKAYA_PALETTE.ivory,
            fontFamily: "Tajawal, system-ui, sans-serif",
            fontSize: 72,
            fontWeight: 800,
            lineHeight: 1.4,
            textShadow: `0 4px 20px ${HEKAYA_PALETTE.shadow}`,
          }}
        >
          {loopHook.closingPhrase}
        </div>
      </div>

      {/* Handle + sources strip */}
      <div
        style={{
          position: "absolute",
          bottom: 220,
          left: 0,
          right: 0,
          textAlign: "center",
          opacity: handleOpacity,
        }}
      >
        <div
          style={{
            color: HEKAYA_PALETTE.ivory,
            fontFamily: "system-ui, -apple-system, sans-serif",
            fontSize: 28,
            letterSpacing: 4,
            fontWeight: 500,
            opacity: 0.92,
          }}
        >
          {handle}
        </div>
        <div
          style={{
            color: HEKAYA_PALETTE.gold,
            fontFamily: "system-ui, -apple-system, sans-serif",
            fontSize: 13,
            letterSpacing: 3,
            marginTop: 14,
            opacity: 0.6,
            textTransform: "uppercase",
          }}
        >
          {sources
            .slice(0, 4)
            .map((s) => s.name)
            .join(" · ")}
        </div>
      </div>
    </AbsoluteFill>
  );
};
