import React from "react";
import { AbsoluteFill, interpolate, Easing } from "remotion";
import { useSceneProgress } from "../../PhotonectBrandReel/useSceneProgress";
import { FONT_LATIN, FONT_ARABIC } from "../../PhotonectBrandReel/fonts";
import { PHOTONECT } from "../../PhotonectBrandReel/brand";
import { ContextLine, PhotoBackdrop, BrandMark, ArabicKicker } from "../MotionLayers";

type Item = { label: string; value: number; color: string; growth?: string; initials?: string };
type Props = {
  kicker: string;
  arabicKicker: string;
  context: string;
  arabicContext: string;
  arabic: string;
  unit: string;
  items: Item[];
  images: string[];
  storyIndex: number;
  total: number;
};

export const SceneRace: React.FC<Props> = ({
  kicker,
  arabicKicker,
  context,
  arabicContext,
  arabic,
  unit,
  items,
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
  const arP = interpolate(frame, [0.5 * fps, 1.3 * fps], [0, 1], {
    easing: Easing.bezier(0.16, 1, 0.3, 1),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const max = Math.max(...items.map((i) => i.value));

  return (
    <AbsoluteFill>
      {images[0] && <PhotoBackdrop src={images[0]} accent={accent} mode="hero" panX={[0, -2]} />}
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

      {/* Arabic kicker (RTL) — above headline */}
      <div
        style={{
          opacity: kickP * alive,
          transform: `translateY(${(1 - kickP) * 20}px)`,
          marginBottom: 8,
        }}
      >
        <ArabicKicker text={arabicKicker} color={accent} opacity={1} />
      </div>

      {/* Kicker headline */}
      <div
        style={{
          fontFamily: FONT_LATIN,
          fontWeight: 900,
          fontSize: 84,
          color: paper,
          letterSpacing: "-0.025em",
          lineHeight: 0.98,
          opacity: kickP * alive,
          transform: `translateY(${(1 - kickP) * 30}px)`,
          maxWidth: 960,
        }}
      >
        {kicker}
      </div>

      {/* Arabic */}
      <div
        style={{
          fontFamily: FONT_ARABIC,
          fontWeight: 500,
          fontSize: 42,
          color: accent,
          opacity: arP * alive,
          direction: "rtl",
          marginTop: 18,
        }}
      >
        {arabic}
      </div>

      {/* Bars */}
      <div style={{ display: "flex", flexDirection: "column", gap: 44, marginTop: 50 }}>
        {items.map((it, i) => {
          const start = 1.6 * fps + i * 0.6 * fps;
          const grow = interpolate(frame, [start, start + 1.8 * fps], [0, 1], {
            easing: Easing.bezier(0.16, 1, 0.3, 1),
            extrapolateLeft: "clamp",
            extrapolateRight: "clamp",
          });
          const textFade = interpolate(frame, [start, start + 0.6 * fps], [0, 1], {
            easing: Easing.bezier(0.16, 1, 0.3, 1),
            extrapolateLeft: "clamp",
            extrapolateRight: "clamp",
          });
          const widthPct = (it.value / max) * 100 * grow;
          const counted = (grow * it.value).toFixed(1);
          return (
            <div
              key={i}
              style={{ display: "flex", flexDirection: "column", gap: 10, opacity: alive }}
            >
              <div
                style={{
                  display: "flex",
                  justifyContent: "space-between",
                  alignItems: "center",
                  fontFamily: FONT_LATIN,
                  color: paper,
                  opacity: textFade,
                }}
              >
                <div style={{ display: "flex", alignItems: "center", gap: 18 }}>
                  <BrandMark
                    name={it.label}
                    initials={it.initials ?? it.label.charAt(0)}
                    brandColor={it.color}
                    size={80}
                  />
                  <span style={{ fontWeight: 800, fontSize: 54, letterSpacing: "0.02em" }}>
                    {it.label}
                  </span>
                </div>
                <span
                  style={{
                    fontWeight: 900,
                    fontSize: 84,
                    color: it.color,
                    letterSpacing: "-0.02em",
                  }}
                >
                  ${counted}
                  <span style={{ fontSize: 42, color: paper, opacity: 0.7, marginLeft: 8 }}>
                    {unit}
                  </span>
                </span>
              </div>
              <div
                style={{
                  height: 50,
                  background: "rgba(255,255,255,0.08)",
                  borderRadius: 8,
                  overflow: "hidden",
                  position: "relative",
                }}
              >
                <div
                  style={{
                    height: "100%",
                    width: `${widthPct}%`,
                    background: `linear-gradient(90deg, ${it.color} 0%, ${it.color}CC 100%)`,
                    boxShadow: `0 0 30px ${it.color}88`,
                  }}
                />
              </div>
              {it.growth ? (
                <div
                  style={{
                    fontFamily: FONT_LATIN,
                    fontWeight: 700,
                    fontSize: 28,
                    color: it.color,
                    opacity: textFade,
                    letterSpacing: "0.08em",
                  }}
                >
                  GROWTH: {it.growth}
                </div>
              ) : null}
            </div>
          );
        })}
      </div>

      {/* Why it matters */}
      <div style={{ marginTop: 40 }}>
        <ContextLine
          text={context}
          arabic={arabicContext}
          startAtSeconds={6.4}
          paper={paper}
          accent={accent}
        />
      </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
