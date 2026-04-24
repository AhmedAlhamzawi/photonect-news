import React from "react";
import { AbsoluteFill, interpolate, Easing } from "remotion";
import { LogoMark } from "../LogoMark";
import { useSceneProgress } from "../useSceneProgress";
import { FONT_LATIN } from "../fonts";

type Props = {
  brandName: string;
  ctaText: string;
  ctaUrl: string;
  paper: string;
  accent: string;
  primary: string;
};

export const SceneCTA: React.FC<Props> = ({
  brandName,
  ctaText,
  ctaUrl,
  paper,
  accent,
  primary,
}) => {
  const { frame, fps, progress, exit } = useSceneProgress(0.7, 0.4);

  // Logo mark already drawn (draw=1) — just fade + scale
  const logoP = interpolate(frame, [0, 0.6 * fps], [0, 1], {
    easing: Easing.bezier(0.16, 1, 0.3, 1),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // CTA text: the hero moment — one spring allowed
  const heroP = interpolate(frame, [0.6 * fps, 1.4 * fps], [0, 1], {
    easing: Easing.bezier(0.34, 1.56, 0.64, 1),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // URL fade-in after CTA
  const urlP = interpolate(frame, [1.2 * fps, 1.8 * fps], [0, 1], {
    easing: Easing.bezier(0.16, 1, 0.3, 1),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Accent ring pulse around logo
  const ringP = interpolate(frame, [0.8 * fps, 1.6 * fps], [0, 1], {
    easing: Easing.bezier(0.65, 0, 0.35, 1),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const ringScale = interpolate(ringP, [0, 1], [0.8, 1.6]);
  const ringOpacity = interpolate(ringP, [0, 1], [0.5, 0]);

  return (
    <AbsoluteFill
      style={{
        justifyContent: "center",
        alignItems: "center",
        padding: "0 80px",
      }}
    >
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          gap: 52,
          transform: `scale(${interpolate(progress, [0, 1], [0.96, 1])})`,
        }}
      >
        {/* Logo with pulse ring */}
        <div style={{ position: "relative", width: 240, height: 240 }}>
          <div
            style={{
              position: "absolute",
              inset: 0,
              border: `4px solid ${accent}`,
              borderRadius: "50%",
              transform: `scale(${ringScale})`,
              opacity: ringOpacity * (1 - exit),
            }}
          />
          <div
            style={{
              opacity: logoP * (1 - exit),
              transform: `scale(${interpolate(logoP, [0, 1], [0.85, 1])})`,
            }}
          >
            <LogoMark size={240} primary={paper} accent={accent} draw={1} />
          </div>
        </div>

        {/* Brand name small */}
        <div
          style={{
            fontFamily: FONT_LATIN,
            fontWeight: 900,
            fontSize: 72,
            color: paper,
            letterSpacing: "-0.03em",
            opacity: logoP * (1 - exit),
            textTransform: "lowercase",
          }}
        >
          {brandName}
        </div>

        {/* CTA — hero moment */}
        <div
          style={{
            fontFamily: FONT_LATIN,
            fontWeight: 700,
            fontSize: 64,
            color: accent,
            letterSpacing: "-0.02em",
            textAlign: "center",
            opacity: heroP * (1 - exit),
            transform: `scale(${interpolate(heroP, [0, 1], [0.85, 1])}) translateY(${(1 - heroP) * 20}px)`,
            maxWidth: 900,
          }}
        >
          {ctaText}
        </div>

        {/* URL */}
        <div
          style={{
            fontFamily: FONT_LATIN,
            fontWeight: 500,
            fontSize: 38,
            color: paper,
            letterSpacing: "0.02em",
            opacity: urlP * 0.8 * (1 - exit),
            padding: "14px 40px",
            border: `2px solid ${paper}`,
            borderRadius: 999,
          }}
        >
          {ctaUrl}
        </div>
      </div>
      {/* Keep unused vars tidy */}
      <div style={{ display: "none", color: primary }} />
    </AbsoluteFill>
  );
};
