import React from "react";
import { AbsoluteFill, interpolate, Easing } from "remotion";
import { useSceneProgress } from "../../PhotonectBrandReel/useSceneProgress";
import { FONT_LATIN, FONT_ARABIC } from "../../PhotonectBrandReel/fonts";
import { PHOTONECT } from "../../PhotonectBrandReel/brand";
import { ContextLine, PhotoBackdrop, ArabicKicker, BrandMark } from "../MotionLayers";

type Node = { label: string; initials?: string; brandColor?: string };
type Props = {
  kicker: string;
  arabicKicker: string;
  nodes: Node[];
  verdict: string;
  context: string;
  arabicContext: string;
  arabic: string;
  images: string[];
  storyIndex: number;
  total: number;
};

export const SceneAlliance: React.FC<Props> = ({
  kicker,
  arabicKicker,
  nodes,
  verdict,
  context,
  arabicContext,
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

  const verdictP = interpolate(frame, [3.0 * fps, 3.8 * fps], [0, 1], {
    easing: Easing.bezier(0.16, 1, 0.3, 1),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const arP = interpolate(frame, [3.4 * fps, 4.0 * fps], [0, 1], {
    easing: Easing.bezier(0.16, 1, 0.3, 1),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Triangle layout
  const cx = 540;
  const cy = 1140;
  const radius = 340;
  const nodePositions = nodes.map((_, i) => {
    const angle = -Math.PI / 2 + (i * (2 * Math.PI)) / nodes.length;
    return {
      x: cx + Math.cos(angle) * radius,
      y: cy + Math.sin(angle) * radius,
    };
  });

  return (
    <AbsoluteFill>
      {images[0] && <PhotoBackdrop src={images[0]} accent={accent} mode="hero" />}
      <AbsoluteFill style={{ padding: "200px 60px 180px" }}>
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

      <div
        style={{
          fontFamily: FONT_LATIN,
          fontWeight: 900,
          fontSize: 118,
          color: paper,
          letterSpacing: "-0.03em",
          lineHeight: 0.95,
          marginTop: 14,
          opacity: kickP * alive,
          maxWidth: 960,
        }}
      >
        UNITED
        <br />
        FRONT.
      </div>

      {/* SVG connections + nodes */}
      <svg
        width={1080}
        height={1920}
        viewBox="0 0 1080 1920"
        style={{
          position: "absolute",
          left: 0,
          top: 0,
          pointerEvents: "none",
          opacity: alive,
        }}
      >
        {nodePositions.map((a, i) =>
          nodePositions.slice(i + 1).map((b, j) => {
            const start = 0.8 * fps + (i + j) * 10;
            const p = interpolate(frame, [start, start + 1.0 * fps], [0, 1], {
              easing: Easing.bezier(0.16, 1, 0.3, 1),
              extrapolateLeft: "clamp",
              extrapolateRight: "clamp",
            });
            // Pulsing data dot traveling along the line
            const travelT = ((frame * 0.015) + i * 0.33) % 1;
            const dotX = a.x + (b.x - a.x) * travelT;
            const dotY = a.y + (b.y - a.y) * travelT;
            const x2 = a.x + (b.x - a.x) * p;
            const y2 = a.y + (b.y - a.y) * p;
            return (
              <g key={`${i}-${j}`}>
                <line
                  x1={a.x}
                  y1={a.y}
                  x2={x2}
                  y2={y2}
                  stroke={accent}
                  strokeWidth={3}
                  strokeLinecap="round"
                  opacity={0.75}
                />
                {p > 0.95 ? (
                  <circle
                    cx={dotX}
                    cy={dotY}
                    r={6}
                    fill={accent}
                    opacity={0.9}
                  />
                ) : null}
              </g>
            );
          }),
        )}
        {nodePositions.map((n, i) => {
          const start = 0.6 * fps + i * 10;
          const p = interpolate(frame, [start, start + 0.6 * fps], [0, 1], {
            easing: Easing.bezier(0.34, 1.56, 0.64, 1),
            extrapolateLeft: "clamp",
            extrapolateRight: "clamp",
          });
          const ringPulse = 0.5 + 0.5 * Math.sin(frame * 0.14 + i);
          return (
            <g key={i}>
              <circle
                cx={n.x}
                cy={n.y}
                r={100 + ringPulse * 20}
                fill="none"
                stroke={accent}
                strokeWidth={2}
                opacity={0.28 * p}
              />
              {/* Outer ring — brand mark sits on top via DOM layer below */}
              <circle
                cx={n.x}
                cy={n.y}
                r={96 * p}
                fill="none"
                stroke={accent}
                strokeWidth={4}
                opacity={0.4}
              />
            </g>
          );
        })}
      </svg>

      {/* Node brand marks + labels (DOM layer over SVG) */}
      {nodePositions.map((n, i) => {
        const start = 0.6 * fps + i * 10;
        const p = interpolate(frame, [start, start + 0.6 * fps], [0, 1], {
          easing: Easing.bezier(0.34, 1.56, 0.64, 1),
          extrapolateLeft: "clamp",
          extrapolateRight: "clamp",
        });
        const node = nodes[i];
        return (
          <React.Fragment key={`dom-${i}`}>
            <div
              style={{
                position: "absolute",
                left: n.x - 80,
                top: n.y - 80,
                opacity: p * alive,
                transform: `scale(${0.6 + p * 0.4})`,
              }}
            >
              <BrandMark
                name={node.label}
                initials={node.initials ?? node.label.charAt(0)}
                brandColor={node.brandColor ?? accent}
                size={160}
                textColor="#FFFFFF"
              />
            </div>
            <div
              style={{
                position: "absolute",
                left: n.x - 140,
                top: n.y + 96,
                width: 280,
                textAlign: "center",
                fontFamily: FONT_LATIN,
                fontWeight: 900,
                fontSize: 30,
                color: paper,
                letterSpacing: "0.08em",
                textShadow: `0 0 12px ${PHOTONECT.ink}`,
                opacity: p * alive,
              }}
            >
              {node.label}
            </div>
          </React.Fragment>
        );
      })}

      {/* Verdict */}
      <div
        style={{
          position: "absolute",
          bottom: 360,
          left: 60,
          right: 60,
          fontFamily: FONT_LATIN,
          fontWeight: 800,
          fontSize: 56,
          color: paper,
          opacity: verdictP * alive,
          transform: `translateY(${(1 - verdictP) * 22}px)`,
          lineHeight: 1.18,
        }}
      >
        {verdict}
      </div>

      <div
        style={{
          position: "absolute",
          bottom: 300,
          left: 60,
          right: 60,
          fontFamily: FONT_ARABIC,
          fontWeight: 500,
          fontSize: 38,
          color: accent,
          opacity: arP * alive,
          direction: "rtl",
        }}
      >
        {arabic}
      </div>

      {/* Context */}
      <div
        style={{
          position: "absolute",
          bottom: 180,
          left: 60,
          right: 60,
        }}
      >
        <ContextLine
          text={context}
          arabic={arabicContext}
          startAtSeconds={5.2}
          paper={paper}
          accent={accent}
        />
      </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
