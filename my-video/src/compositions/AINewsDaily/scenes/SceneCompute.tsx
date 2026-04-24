import React from "react";
import { AbsoluteFill, interpolate, Easing, random } from "remotion";
import { useSceneProgress } from "../../PhotonectBrandReel/useSceneProgress";
import { FONT_LATIN, FONT_ARABIC } from "../../PhotonectBrandReel/fonts";
import { PHOTONECT } from "../../PhotonectBrandReel/brand";
import { SupportingStats, ContextLine, PhotoBackdrop, ArabicKicker } from "../MotionLayers";

type Props = {
  kicker: string;
  arabicKicker: string;
  value: number;
  unit: string;
  label: string;
  partners: string[];
  context: string;
  arabicContext: string;
  supportingStats: { label: string; value: string }[];
  arabic: string;
  images: string[];
  storyIndex: number;
  total: number;
};

export const SceneCompute: React.FC<Props> = ({
  kicker,
  arabicKicker,
  value,
  unit,
  label,
  partners,
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

  const countP = interpolate(frame, [0.4 * fps, 2.4 * fps], [0, 1], {
    easing: Easing.bezier(0.16, 1, 0.3, 1),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const counted = (countP * value).toFixed(1);

  const labP = interpolate(frame, [1.8 * fps, 2.6 * fps], [0, 1], {
    easing: Easing.bezier(0.16, 1, 0.3, 1),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Server grid — 14x6 cells lighting up progressively, continue pulsing
  const cols = 14;
  const rows = 6;
  const cells: { x: number; y: number; lit: number }[] = [];
  for (let y = 0; y < rows; y++) {
    for (let x = 0; x < cols; x++) {
      const delay = 0.6 * fps + random(`cell-${x}-${y}`) * 2.0 * fps;
      const lit = interpolate(frame, [delay, delay + 0.5 * fps], [0, 1], {
        easing: Easing.bezier(0.16, 1, 0.3, 1),
        extrapolateLeft: "clamp",
        extrapolateRight: "clamp",
      });
      // Ongoing pulse after lit
      const pulse = lit * (0.7 + 0.3 * (0.5 + 0.5 * Math.sin(frame * 0.1 + x + y)));
      cells.push({ x, y, lit: pulse });
    }
  }

  return (
    <AbsoluteFill>
      {images[0] && <PhotoBackdrop src={images[0]} accent={accent} mode="grid" />}
      <AbsoluteFill style={{ padding: "200px 60px 180px", justifyContent: "flex-start" }}>
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

      <div style={{ opacity: kickP * alive, marginBottom: 4 }}>
        <ArabicKicker text={arabicKicker} color={accent} opacity={1} />
      </div>
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

      {/* Giant value */}
      <div
        style={{
          fontFamily: FONT_LATIN,
          fontWeight: 900,
          fontSize: 340,
          lineHeight: 0.85,
          color: paper,
          letterSpacing: "-0.055em",
          marginTop: 14,
          opacity: alive,
        }}
      >
        {counted}
        <span style={{ fontSize: 160, color: accent, marginLeft: 10 }}>{unit}</span>
      </div>

      {/* Server grid */}
      <div
        style={{
          display: "grid",
          gridTemplateColumns: `repeat(${cols}, 1fr)`,
          gap: 8,
          marginTop: 14,
          padding: 20,
          background: "rgba(255,255,255,0.04)",
          borderRadius: 12,
          border: `1px solid ${accent}44`,
          opacity: alive,
        }}
      >
        {cells.map((c, i) => (
          <div
            key={i}
            style={{
              height: 26,
              background: `rgba(0, 229, 160, ${0.08 + c.lit * 0.9})`,
              borderRadius: 2,
              boxShadow: c.lit > 0.7 ? `0 0 8px ${accent}` : "none",
            }}
          />
        ))}
      </div>

      {/* Partners + label row */}
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "baseline",
          marginTop: 18,
          opacity: labP * alive,
          transform: `translateY(${(1 - labP) * 16}px)`,
        }}
      >
        <div
          style={{
            fontFamily: FONT_LATIN,
            fontWeight: 800,
            fontSize: 36,
            color: paper,
          }}
        >
          {partners.join("  +  ")}
        </div>
        <div
          style={{
            fontFamily: FONT_LATIN,
            fontWeight: 900,
            fontSize: 42,
            color: accent,
            letterSpacing: "0.06em",
          }}
        >
          {label}
        </div>
      </div>

      {/* Arabic */}
      <div
        style={{
          fontFamily: FONT_ARABIC,
          fontWeight: 500,
          fontSize: 34,
          color: paper,
          opacity: labP * 0.7 * alive,
          direction: "rtl",
          marginTop: 10,
        }}
      >
        {arabic}
      </div>

      {/* Supporting stats */}
      <div style={{ width: "100%", marginTop: 22 }}>
        <SupportingStats stats={supportingStats} startAtSeconds={3.8} color={accent} paper={paper} />
      </div>

      {/* Context */}
      <div style={{ marginTop: 16 }}>
        <ContextLine
          text={context}
          arabic={arabicContext}
          startAtSeconds={6.6}
          paper={paper}
          accent={accent}
        />
      </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
