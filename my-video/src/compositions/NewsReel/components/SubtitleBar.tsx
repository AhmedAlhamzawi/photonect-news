import React from "react";
import { useCurrentFrame, interpolate, Easing } from "remotion";

/**
 * SubtitleBar — V7 leap component.
 *
 * Persistent translucent dark band at the bottom 96px of the beat frame
 * carrying 3-4 Arabic phrases that reveal one at a time across the beat's
 * runtime. Sound-off design (BBC/Vice pattern): the viewer can read the
 * gist of the beat from the subtitle bar alone.
 *
 * RTL Tajawal, single-line per phrase, white at 95%, 32px font with light
 * baseline shadow. Phrases reveal via masked clip-path wipe (RTL: from
 * right to left), 12 frames per reveal, hold remainder of phrase window.
 *
 * Layout: divides durationFrames evenly across phrases.length, reserves
 * 6f at start of each window for the wipe-in animation.
 */
export const SubtitleBar: React.FC<{
  phrases?: string[];
  durationFrames: number;
}> = ({ phrases, durationFrames }) => {
  const frame = useCurrentFrame();
  if (!phrases || phrases.length === 0) return null;

  // Divide the beat into N equal windows, one per phrase
  const window = Math.floor(durationFrames / phrases.length);
  const idx = Math.min(Math.floor(frame / window), phrases.length - 1);
  const localFrame = frame - idx * window;
  const current = phrases[idx];

  // Mask wipe in: right-to-left over first 14 frames of each window
  const wipe = interpolate(localFrame, [0, 14], [0, 100], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  });

  // Subtle vertical lift on entry
  const y = interpolate(localFrame, [0, 14], [4, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  });

  // Bar fades in only once on the very first frame of the scene, holds for the rest
  const barOpacity = interpolate(frame, [4, 14], [0, 0.78], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <div
      style={{
        position: "absolute",
        left: 0,
        right: 0,
        bottom: 32,
        height: 96,
        background: `linear-gradient(180deg, rgba(0,0,0,0.0) 0%, rgba(0,0,0,${barOpacity}) 35%, rgba(0,0,0,${barOpacity}) 100%)`,
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        padding: "0 64px",
        pointerEvents: "none",
      }}
    >
      <div
        style={{
          // RTL clip from the right. clip-path inset(top right bottom left)
          // wipe goes from inset(0 100% 0 0) → inset(0 0 0 0) RTL
          clipPath: `inset(0 ${100 - wipe}% 0 0)`,
          transform: `translateY(${y}px)`,
          fontFamily:
            '"Tajawal", "Noto Sans Arabic", "SF Pro Arabic", system-ui, -apple-system, sans-serif',
          fontWeight: 700,
          fontSize: 36,
          lineHeight: 1.18,
          color: "rgba(255,255,255,0.95)",
          textAlign: "center",
          direction: "rtl",
          textShadow: "0 2px 12px rgba(0,0,0,0.75)",
          letterSpacing: "-0.005em",
          maxWidth: 960,
        }}
      >
        {current}
      </div>
    </div>
  );
};
