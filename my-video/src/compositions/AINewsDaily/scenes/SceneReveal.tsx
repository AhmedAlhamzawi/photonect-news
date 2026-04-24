import React from "react";
import { AbsoluteFill, interpolate, Easing } from "remotion";
import { useSceneProgress } from "../../PhotonectBrandReel/useSceneProgress";
import { FONT_LATIN, FONT_ARABIC } from "../../PhotonectBrandReel/fonts";
import { PHOTONECT } from "../../PhotonectBrandReel/brand";
import { SupportingStats, ContextLine, PhotoBackdrop, ArabicKicker } from "../MotionLayers";

type Props = {
  kicker: string;
  arabicKicker: string;
  title: string;
  quote: string;
  context: string;
  arabicContext: string;
  supportingStats: { label: string; value: string }[];
  arabic: string;
  images: string[];
  storyIndex: number;
  total: number;
};

export const SceneReveal: React.FC<Props> = ({
  kicker,
  arabicKicker,
  title,
  quote,
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

  const atmoP = interpolate(frame, [0, 1.0 * fps], [0, 1], {
    easing: Easing.bezier(0.45, 0, 0.55, 1),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const words = title.split(" ");
  let letterCounter = 0;

  const quoteP = interpolate(frame, [2.4 * fps, 3.2 * fps], [0, 1], {
    easing: Easing.bezier(0.16, 1, 0.3, 1),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const arP = interpolate(frame, [2.8 * fps, 3.5 * fps], [0, 1], {
    easing: Easing.bezier(0.16, 1, 0.3, 1),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill>
      {images[0] && <PhotoBackdrop src={images[0]} accent={accent} mode="classified" />}
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
          opacity: atmoP * alive,
        }}
      >
        {String(storyIndex).padStart(2, "0")} / {String(total).padStart(2, "0")}
      </div>

      {/* Classified kicker */}
      <div
        style={{
          display: "flex",
          alignItems: "center",
          gap: 18,
          opacity: atmoP * alive,
        }}
      >
        <div
          style={{
            width: 16,
            height: 16,
            background: "#FF3B30",
            borderRadius: 2,
            boxShadow: "0 0 18px #FF3B30",
          }}
        />
        <div style={{ display: "flex", flexDirection: "column", gap: 4 }}>
          <ArabicKicker text={arabicKicker} color="#FF3B30" opacity={1} />
          <div
            style={{
              fontFamily: FONT_LATIN,
              fontWeight: 800,
              fontSize: 30,
              color: paper,
              letterSpacing: "0.28em",
            }}
          >
            {kicker}
          </div>
        </div>
      </div>

      {/* Huge title: word-safe letter animation */}
      <div
        style={{
          display: "flex",
          flexWrap: "wrap",
          gap: "0 34px",
          marginTop: 24,
          fontFamily: FONT_LATIN,
          fontWeight: 900,
          fontSize: 160,
          lineHeight: 0.94,
          color: paper,
          letterSpacing: "-0.04em",
          maxWidth: 960,
        }}
      >
        {words.map((word, wIdx) => (
          <div key={wIdx} style={{ display: "flex", whiteSpace: "nowrap" }}>
            {word.split("").map((l) => {
              const i = letterCounter++;
              const delay = 0.6 * fps + i * 3;
              const p = interpolate(frame, [delay, delay + 0.5 * fps], [0, 1], {
                easing: Easing.bezier(0.34, 1.56, 0.64, 1),
                extrapolateLeft: "clamp",
                extrapolateRight: "clamp",
              });
              return (
                <span
                  key={i}
                  style={{
                    display: "inline-block",
                    opacity: p * alive,
                    transform: `translateY(${(1 - p) * 30}px) scale(${0.9 + p * 0.1})`,
                    textShadow: p > 0.8 ? `0 0 70px ${accent}55` : "none",
                  }}
                >
                  {l}
                </span>
              );
            })}
          </div>
        ))}
      </div>

      {/* Accent line */}
      <div
        style={{
          height: 5,
          width: interpolate(quoteP, [0, 1], [0, 540]),
          background: accent,
          borderRadius: 2,
          marginTop: 22,
          opacity: alive,
          boxShadow: `0 0 18px ${accent}88`,
        }}
      />

      {/* Quote */}
      <div
        style={{
          fontFamily: FONT_LATIN,
          fontStyle: "italic",
          fontWeight: 500,
          fontSize: 44,
          color: paper,
          opacity: quoteP * 0.9 * alive,
          transform: `translateY(${(1 - quoteP) * 20}px)`,
          marginTop: 20,
          maxWidth: 900,
          lineHeight: 1.25,
        }}
      >
        “{quote}”
      </div>

      {/* Arabic */}
      <div
        style={{
          fontFamily: FONT_ARABIC,
          fontWeight: 500,
          fontSize: 38,
          color: accent,
          opacity: arP * alive,
          direction: "rtl",
          marginTop: 14,
        }}
      >
        {arabic}
      </div>

      {/* Supporting stats */}
      <div style={{ width: "100%", marginTop: 28 }}>
        <SupportingStats stats={supportingStats} startAtSeconds={4.2} color={accent} paper={paper} />
      </div>

      {/* Context */}
      <div style={{ marginTop: 14 }}>
        <ContextLine
          text={context}
          arabic={arabicContext}
          startAtSeconds={6.8}
          paper={paper}
          accent={accent}
        />
      </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
