import React from "react";
import { AbsoluteFill, interpolate, Easing } from "remotion";
import { useSceneProgress } from "../../PhotonectBrandReel/useSceneProgress";
import { FONT_LATIN, FONT_ARABIC } from "../../PhotonectBrandReel/fonts";
import { PHOTONECT } from "../../PhotonectBrandReel/brand";
import { LogoPhotonect } from "../LogoPhotonect";

// Title scene runs 5s (150f). Plenty of time to read.
export const SceneTitle: React.FC = () => {
  const { frame, fps, exit } = useSceneProgress(1.0, 0.4);
  const accent = PHOTONECT.signal;
  const paper = PHOTONECT.paper;

  const headlineP = interpolate(frame, [0, 1.3 * fps], [0, 1], {
    easing: Easing.bezier(0.16, 1, 0.3, 1),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const numeralP = interpolate(frame, [0.4 * fps, 1.7 * fps], [0, 1], {
    easing: Easing.bezier(0.34, 1.56, 0.64, 1),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const subP = interpolate(frame, [1.2 * fps, 2.2 * fps], [0, 1], {
    easing: Easing.bezier(0.16, 1, 0.3, 1),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const arP = interpolate(frame, [1.8 * fps, 2.8 * fps], [0, 1], {
    easing: Easing.bezier(0.16, 1, 0.3, 1),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const briefP = interpolate(frame, [2.5 * fps, 3.3 * fps], [0, 1], {
    easing: Easing.bezier(0.16, 1, 0.3, 1),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const logoP = interpolate(frame, [0, 0.8 * fps], [0, 1], {
    easing: Easing.bezier(0.16, 1, 0.3, 1),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const alive = 1 - exit;

  return (
    <AbsoluteFill
      style={{
        justifyContent: "center",
        alignItems: "center",
        padding: "220px 80px 200px",
      }}
    >
      <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 14 }}>
        {/* Photonect brand lockup — pre-title */}
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            gap: 10,
            opacity: logoP * alive,
            transform: `translateY(${(1 - logoP) * -14}px)`,
            marginBottom: 6,
          }}
        >
          <LogoPhotonect size={88} variant="dark" orientation="stacked" />
          <div
            style={{
              fontFamily: FONT_LATIN,
              fontWeight: 700,
              fontSize: 20,
              color: accent,
              letterSpacing: "0.42em",
              marginTop: 4,
            }}
          >
            PRESENTS
          </div>
        </div>

        {/* Huge 24H numeral */}
        <div
          style={{
            fontFamily: FONT_LATIN,
            fontWeight: 900,
            fontSize: 520,
            lineHeight: 0.8,
            color: "transparent",
            WebkitTextStroke: `5px ${accent}`,
            letterSpacing: "-0.07em",
            opacity: numeralP * alive,
            transform: `scale(${0.85 + numeralP * 0.15})`,
          }}
        >
          24H
        </div>

        {/* AI NEWS wordmark with clip reveal */}
        <div
          style={{
            fontFamily: FONT_LATIN,
            fontWeight: 900,
            fontSize: 150,
            letterSpacing: "-0.035em",
            color: paper,
            clipPath: `inset(0 ${(1 - headlineP) * 100}% 0 0)`,
            lineHeight: 1,
            marginTop: 8,
          }}
        >
          AI NEWS
        </div>

        {/* Accent bar */}
        <div
          style={{
            height: 8,
            width: 460,
            background: accent,
            transform: `scaleX(${headlineP})`,
            transformOrigin: "left center",
            borderRadius: 4,
            marginTop: 2,
            boxShadow: `0 0 24px ${accent}88`,
          }}
        />

        {/* Subtitle */}
        <div
          style={{
            fontFamily: FONT_LATIN,
            fontWeight: 500,
            fontSize: 44,
            color: paper,
            opacity: subP * 0.92 * alive,
            letterSpacing: "0.28em",
            transform: `translateY(${(1 - subP) * 18}px)`,
            marginTop: 16,
          }}
        >
          THE LAST 24 HOURS
        </div>

        {/* Arabic */}
        <div
          style={{
            fontFamily: FONT_ARABIC,
            fontWeight: 500,
            fontSize: 48,
            color: accent,
            opacity: arP * alive,
            direction: "rtl",
            marginTop: 14,
            transform: `translateY(${(1 - arP) * 18}px)`,
          }}
        >
          أخبار الذكاء الاصطناعي — آخر ٢٤ ساعة
        </div>

        {/* Brief — explaining the format */}
        <div
          style={{
            marginTop: 38,
            padding: "14px 26px",
            border: `2px solid ${accent}`,
            borderRadius: 6,
            fontFamily: FONT_LATIN,
            fontWeight: 700,
            fontSize: 26,
            color: paper,
            letterSpacing: "0.16em",
            opacity: briefP * alive,
            transform: `translateY(${(1 - briefP) * 12}px)`,
          }}
        >
          05 STORIES  •  60 SECONDS  •  NO FLUFF
        </div>
      </div>
    </AbsoluteFill>
  );
};
