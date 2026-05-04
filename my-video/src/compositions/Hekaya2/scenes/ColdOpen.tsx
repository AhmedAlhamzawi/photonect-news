import React from "react";
import { AbsoluteFill, interpolate, useCurrentFrame, Easing } from "remotion";
import { Hekaya2Props, HEKAYA_PALETTE } from "../schema";
import { ParallaxImage } from "../components/ParallaxImage";
import { Embers } from "../components/Embers";

interface Props {
  hero: string;
  title: Hekaya2Props["title"];
  durationFrames: number;
}

/**
 * 0-8s opener — the hook.
 *
 * For the first 2 seconds (frame 0-60), only the hero detail + atmospheric
 * embers are visible. The VO + foley do the work; no title yet. The title
 * lower-third slides in at frame 60-90 as the inciting incident lands.
 */
export const ColdOpen: React.FC<Props> = ({ hero, title, durationFrames }) => {
  const frame = useCurrentFrame();

  const titleOpacity = interpolate(frame, [60, 90], [0, 1], {
    extrapolateRight: "clamp",
  });
  const titleY = interpolate(frame, [60, 105], [30, 0], {
    easing: Easing.bezier(0.16, 1, 0.3, 1),
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill style={{ backgroundColor: HEKAYA_PALETTE.ink }}>
      <ParallaxImage
        src={hero}
        durationFrames={durationFrames}
        direction="in"
      />
      <Embers />

      {/* Lower-third title — appears at 2s, NOT at 0s. The reel earns the title. */}
      <div
        style={{
          position: "absolute",
          bottom: 280,
          left: 70,
          right: 70,
          opacity: titleOpacity,
          transform: `translateY(${titleY}px)`,
        }}
      >
        {/* Era + place stamp */}
        <div
          style={{
            color: HEKAYA_PALETTE.gold,
            fontFamily: "system-ui, -apple-system, sans-serif",
            fontSize: 22,
            letterSpacing: 6,
            fontWeight: 500,
            textTransform: "uppercase",
            marginBottom: 16,
          }}
        >
          {title.era}  ·  {title.place}
        </div>

        {/* Arabic title — restrained as lower-third, not full-bleed */}
        <div
          dir="rtl"
          style={{
            color: HEKAYA_PALETTE.ivory,
            fontFamily: "Tajawal, system-ui, sans-serif",
            fontSize: 64,
            fontWeight: 800,
            lineHeight: 1.2,
            textShadow: `0 4px 20px ${HEKAYA_PALETTE.shadow}`,
          }}
        >
          {title.arabic}
        </div>

        {/* English subtitle */}
        <div
          style={{
            color: HEKAYA_PALETTE.gold,
            fontFamily: "system-ui, -apple-system, sans-serif",
            fontSize: 20,
            letterSpacing: 4,
            fontStyle: "italic",
            fontWeight: 400,
            opacity: 0.85,
            marginTop: 18,
          }}
        >
          {title.englishSubtitle}
        </div>
      </div>
    </AbsoluteFill>
  );
};
