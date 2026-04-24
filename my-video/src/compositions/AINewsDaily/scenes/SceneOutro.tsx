import React from "react";
import { AbsoluteFill, interpolate, Easing, useCurrentFrame } from "remotion";
import { useSceneProgress } from "../../PhotonectBrandReel/useSceneProgress";
import { FONT_LATIN, FONT_ARABIC } from "../../PhotonectBrandReel/fonts";
import { PHOTONECT } from "../../PhotonectBrandReel/brand";
import { LogoPhotonect } from "../LogoPhotonect";

type Props = {
  handle: string;
};

export const SceneOutro: React.FC<Props> = ({ handle }) => {
  const { frame, fps, exit } = useSceneProgress(0.7, 0.3);
  const accent = PHOTONECT.signal;
  const paper = PHOTONECT.paper;
  const alive = 1 - exit;
  const globalFrame = useCurrentFrame();

  const p1 = interpolate(frame, [0, 0.7 * fps], [0, 1], {
    easing: Easing.bezier(0.16, 1, 0.3, 1),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const p2 = interpolate(frame, [0.4 * fps, 1.2 * fps], [0, 1], {
    easing: Easing.bezier(0.16, 1, 0.3, 1),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const p3 = interpolate(frame, [0.9 * fps, 1.6 * fps], [0, 1], {
    easing: Easing.bezier(0.34, 1.56, 0.64, 1),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const p4 = interpolate(frame, [1.5 * fps, 2.2 * fps], [0, 1], {
    easing: Easing.bezier(0.16, 1, 0.3, 1),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const pulse = 0.6 + 0.4 * Math.sin(globalFrame * 0.2);

  return (
    <AbsoluteFill style={{ justifyContent: "center", alignItems: "center", padding: "200px 60px" }}>
      <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 20 }}>
        <div
          style={{
            fontFamily: FONT_LATIN,
            fontWeight: 800,
            fontSize: 36,
            color: accent,
            letterSpacing: "0.3em",
            opacity: p1 * alive,
          }}
        >
          TOMORROW. SAME TIME.
        </div>

        {/* BIG Photonect logo lockup — parent brand hero */}
        <div
          style={{
            opacity: p2 * alive,
            transform: `translateY(${(1 - p2) * 30}px) scale(${0.95 + p2 * 0.05})`,
            marginTop: 8,
          }}
        >
          <LogoPhotonect size={260} variant="dark" orientation="stacked" />
        </div>

        {/* AI NEWS show label under the logo */}
        <div
          style={{
            display: "flex",
            alignItems: "center",
            gap: 18,
            opacity: p2 * alive,
            marginTop: 4,
          }}
        >
          <div
            style={{
              height: 4,
              width: 80,
              background: accent,
              borderRadius: 2,
            }}
          />
          <div
            style={{
              fontFamily: FONT_LATIN,
              fontWeight: 800,
              fontSize: 44,
              color: accent,
              letterSpacing: "0.22em",
            }}
          >
            AI NEWS
          </div>
          <div
            style={{
              height: 4,
              width: 80,
              background: accent,
              borderRadius: 2,
            }}
          />
        </div>

        <div
          style={{
            fontFamily: FONT_LATIN,
            fontWeight: 800,
            fontSize: 52,
            color: paper,
            opacity: p3 * alive,
            transform: `scale(${0.9 + p3 * 0.1 + pulse * 0.02})`,
            marginTop: 16,
          }}
        >
          {handle}
        </div>

        <div
          style={{
            fontFamily: FONT_ARABIC,
            fontWeight: 500,
            fontSize: 44,
            color: accent,
            opacity: p4 * alive,
            direction: "rtl",
            marginTop: 6,
          }}
        >
          كل يوم. في نفس الوقت.
        </div>

        <div
          style={{
            marginTop: 22,
            padding: "14px 28px",
            border: `2px solid ${accent}`,
            borderRadius: 6,
            fontFamily: FONT_LATIN,
            fontWeight: 700,
            fontSize: 26,
            color: paper,
            letterSpacing: "0.18em",
            opacity: p4 * alive,
          }}
        >
          FOLLOW • SAVE • SHARE
        </div>
      </div>
    </AbsoluteFill>
  );
};
