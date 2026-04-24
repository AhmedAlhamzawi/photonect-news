import React from "react";
import { AbsoluteFill, interpolate, Easing } from "remotion";
import { useSceneProgress } from "../../PhotonectBrandReel/useSceneProgress";
import { FONT_LATIN, FONT_ARABIC } from "../../PhotonectBrandReel/fonts";
import { PHOTONECT } from "../../PhotonectBrandReel/brand";
import { SupportingStats, ContextLine, PhotoBackdrop, ArabicKicker } from "../MotionLayers";

type Props = {
  kicker: string;
  arabicKicker: string;
  prefix: string;
  value: number;
  suffix: string;
  decimals: number;
  label: string;
  context: string;
  arabicContext: string;
  supportingStats: { label: string; value: string }[];
  arabic: string;
  images: string[];
  storyIndex: number;
  total: number;
};

export const SceneBigNumber: React.FC<Props> = ({
  kicker,
  arabicKicker,
  prefix,
  value,
  suffix,
  decimals,
  label,
  context,
  arabicContext,
  supportingStats,
  arabic,
  images,
  storyIndex,
  total,
}) => {
  const { frame, fps, exit } = useSceneProgress(0.8, 0.4);
  const accent = PHOTONECT.signal;
  const paper = PHOTONECT.paper;
  const alive = 1 - exit;

  const kickP = interpolate(frame, [0, 0.8 * fps], [0, 1], {
    easing: Easing.bezier(0.16, 1, 0.3, 1),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Count up over 2s
  const countP = interpolate(frame, [0.4 * fps, 2.6 * fps], [0, 1], {
    easing: Easing.bezier(0.16, 1, 0.3, 1),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const counted = (countP * value).toFixed(decimals);

  const labP = interpolate(frame, [1.8 * fps, 2.8 * fps], [0, 1], {
    easing: Easing.bezier(0.16, 1, 0.3, 1),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const arP = interpolate(frame, [2.2 * fps, 3.2 * fps], [0, 1], {
    easing: Easing.bezier(0.16, 1, 0.3, 1),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const barP = interpolate(frame, [0.5 * fps, 1.4 * fps], [0, 1], {
    easing: Easing.bezier(0.65, 0, 0.35, 1),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill>
      {/* Photo backdrop */}
      {images[0] && <PhotoBackdrop src={images[0]} accent={accent} mode="hero" />}
      <AbsoluteFill style={{ padding: "200px 60px 180px", justifyContent: "flex-start" }}>
      {/* Story pill top-right */}
      <div
        style={{
          position: "absolute",
          top: 180,
          right: 60,
          fontFamily: FONT_LATIN,
          fontWeight: 900,
          fontSize: 32,
          color: accent,
          letterSpacing: "0.18em",
          opacity: kickP * alive,
        }}
      >
        {String(storyIndex).padStart(2, "0")} / {String(total).padStart(2, "0")}
      </div>

      <div style={{ display: "flex", flexDirection: "column", gap: 14, alignItems: "flex-start" }}>
        {/* Arabic kicker first (RTL) */}
        <div style={{ opacity: kickP * alive, transform: `translateX(${(1 - kickP) * -24}px)` }}>
          <ArabicKicker text={arabicKicker} color={accent} opacity={1} />
        </div>
        {/* Kicker */}
        <div
          style={{
            fontFamily: FONT_LATIN,
            fontWeight: 800,
            fontSize: 32,
            color: accent,
            letterSpacing: "0.22em",
            opacity: kickP * alive,
            transform: `translateX(${(1 - kickP) * -40}px)`,
          }}
        >
          {kicker}
        </div>

        {/* Accent bar */}
        <div
          style={{
            height: 6,
            width: 220,
            background: accent,
            transform: `scaleX(${barP})`,
            transformOrigin: "left center",
            borderRadius: 3,
          }}
        />

        {/* Huge number */}
        <div
          style={{
            fontFamily: FONT_LATIN,
            fontWeight: 900,
            fontSize: 380,
            lineHeight: 0.82,
            color: paper,
            letterSpacing: "-0.055em",
            opacity: alive,
            marginTop: 4,
          }}
        >
          <span style={{ fontSize: 220, verticalAlign: "top", color: accent }}>{prefix}</span>
          {counted}
          <span style={{ fontSize: 220, color: accent }}>{suffix}</span>
        </div>

        {/* Label */}
        <div
          style={{
            fontFamily: FONT_LATIN,
            fontWeight: 600,
            fontSize: 46,
            color: paper,
            opacity: labP * 0.92 * alive,
            transform: `translateY(${(1 - labP) * 20}px)`,
            maxWidth: 960,
            lineHeight: 1.2,
          }}
        >
          {label}
        </div>

        {/* Arabic */}
        <div
          style={{
            fontFamily: FONT_ARABIC,
            fontWeight: 500,
            fontSize: 38,
            color: paper,
            opacity: arP * 0.75 * alive,
            transform: `translateY(${(1 - arP) * 16}px)`,
            direction: "rtl",
            maxWidth: 960,
            lineHeight: 1.35,
          }}
        >
          {arabic}
        </div>

        {/* Supporting stats */}
        <div style={{ width: "100%", marginTop: 18 }}>
          <SupportingStats stats={supportingStats} startAtSeconds={3.6} color={accent} paper={paper} />
        </div>

        {/* Context / why it matters */}
        <div style={{ marginTop: 12, width: "100%" }}>
          <ContextLine
            text={context}
            arabic={arabicContext}
            startAtSeconds={6.4}
            paper={paper}
            accent={accent}
          />
        </div>
      </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
