import React from "react";
import { AbsoluteFill, interpolate, useCurrentFrame, Easing, spring, useVideoConfig } from "remotion";
import { PHOTONECT } from "../../PhotonectBrandReel/brand";
import { FONT_ARABIC, FONT_LATIN } from "../../PhotonectBrandReel/fonts";
import { VideoBackdrop } from "../VideoBackdrop";
import { BREAKING_FRAMES } from "../schema";
import { CONTENT_PADDING, CONTENT_WIDTH } from "../safeArea";

type Props = {
  arabicKicker: string;
  arabicHeadline: string;
  englishSubhead: string;
  heroMedia: string;
  heroMediaType: "video" | "image";
};

export const Breaking: React.FC<Props> = ({
  arabicKicker,
  arabicHeadline,
  englishSubhead,
  heroMedia,
  heroMediaType,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const badgePulse = 0.6 + 0.4 * Math.sin(frame * 0.28);
  const badgeReveal = spring({ frame, fps, config: { damping: 14 } });

  const headlineReveal = spring({
    frame: frame - 12,
    fps,
    config: { damping: 18, stiffness: 120 },
  });

  const subheadReveal = interpolate(frame, [28, 50], [0, 1], {
    easing: Easing.bezier(0.16, 1, 0.3, 1),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const bgShift = interpolate(frame, [0, BREAKING_FRAMES], [0, 1], {
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill>
      <VideoBackdrop
        src={heroMedia}
        type={heroMediaType}
        accent={"#FF2D55"}
        intensity="hero"
        durationFrames={BREAKING_FRAMES}
      />

      {/* Red radial gloom that intensifies over the hook */}
      <AbsoluteFill
        style={{
          background: `radial-gradient(ellipse at 50% 80%, #FF2D5522 0%, transparent 60%)`,
          opacity: bgShift,
          mixBlendMode: "screen",
        }}
      />

      <AbsoluteFill
        style={{
          padding: CONTENT_PADDING,
          display: "flex",
          flexDirection: "column",
          justifyContent: "flex-end",
          alignItems: "flex-end",
          direction: "rtl",
        }}
      >
        {/* عاجل pulsing badge */}
        <div
          style={{
            display: "flex",
            alignItems: "center",
            gap: 16,
            padding: "14px 26px 14px 20px",
            background: "#FF2D55",
            borderRadius: 6,
            opacity: badgeReveal,
            transform: `translateY(${(1 - badgeReveal) * 20}px)`,
            boxShadow: `0 0 ${18 + badgePulse * 28}px #FF2D5588`,
            marginBottom: 36,
          }}
        >
          <div
            style={{
              width: 14,
              height: 14,
              borderRadius: 99,
              background: "#FFF",
              opacity: badgePulse,
              boxShadow: `0 0 ${8 + badgePulse * 12}px #FFF`,
            }}
          />
          <div
            style={{
              fontFamily: FONT_ARABIC,
              fontWeight: 700,
              fontSize: 36,
              color: "#FFF",
              letterSpacing: "0.08em",
            }}
          >
            {arabicKicker}
          </div>
        </div>

        {/* Giant Arabic headline */}
        <div
          style={{
            fontFamily: FONT_ARABIC,
            fontWeight: 700,
            fontSize: 82,
            color: PHOTONECT.paper,
            lineHeight: 1.18,
            textAlign: "right",
            direction: "rtl",
            maxWidth: CONTENT_WIDTH,
            letterSpacing: "-0.01em",
            opacity: headlineReveal,
            transform: `translateY(${(1 - headlineReveal) * 28}px)`,
            textShadow: `0 6px 28px ${PHOTONECT.ink}`,
          }}
        >
          {arabicHeadline}
        </div>

        {/* English subhead — smaller, lower-opacity */}
        <div
          style={{
            fontFamily: FONT_LATIN,
            fontWeight: 600,
            fontSize: 28,
            color: PHOTONECT.signal,
            marginTop: 28,
            letterSpacing: "0.12em",
            textTransform: "uppercase",
            opacity: subheadReveal * 0.9,
            textAlign: "right",
          }}
        >
          {englishSubhead}
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
