import React from "react";
import { interpolate, useCurrentFrame, useVideoConfig, Easing } from "remotion";

type Props = {
  size: number;
  primary: string;
  accent: string;
  draw: number; // 0 → 1 reveal
};

// Photonect "photon-connect" mark: a stylized P built from a circle (photon)
// and a connecting arc (connect). Programmatic SVG — no asset files needed.
export const LogoMark: React.FC<Props> = ({ size, primary, accent, draw }) => {
  const circleCircumference = 2 * Math.PI * 80;
  const circleDashOffset = interpolate(draw, [0, 0.55], [circleCircumference, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Vertical stem of the P
  const stemLength = 180;
  const stemOffset = interpolate(draw, [0.35, 0.85], [stemLength, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Accent dot (photon)
  const dotScale = interpolate(draw, [0.75, 1], [0, 1], {
    easing: Easing.bezier(0.34, 1.56, 0.64, 1),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <svg
      width={size}
      height={size}
      viewBox="0 0 240 240"
      fill="none"
      style={{ overflow: "visible" }}
    >
      {/* Photon ring (the bowl of the P) */}
      <circle
        cx="120"
        cy="90"
        r="80"
        stroke={primary}
        strokeWidth="14"
        strokeLinecap="round"
        strokeDasharray={circleCircumference}
        strokeDashoffset={circleDashOffset}
        transform="rotate(-90 120 90)"
      />
      {/* Stem */}
      <line
        x1="50"
        y1="50"
        x2="50"
        y2={50 + stemLength}
        stroke={primary}
        strokeWidth="14"
        strokeLinecap="round"
        strokeDasharray={stemLength}
        strokeDashoffset={stemOffset}
      />
      {/* Accent dot — photon */}
      <circle
        cx="170"
        cy="90"
        r="12"
        fill={accent}
        transform={`scale(${dotScale})`}
        style={{ transformOrigin: "170px 90px", transformBox: "fill-box" as const }}
      />
    </svg>
  );
};

// Wordmark uses Inter 900 with tight tracking
export const Wordmark: React.FC<{
  text: string;
  fontFamily: string;
  color: string;
  opacity: number;
  x: number;
  fontSize: number;
}> = ({ text, fontFamily, color, opacity, x, fontSize }) => {
  return (
    <div
      style={{
        fontFamily,
        fontWeight: 900,
        fontSize,
        color,
        letterSpacing: "-0.03em",
        opacity,
        transform: `translateX(${x}px)`,
        textTransform: "lowercase",
      }}
    >
      {text}
    </div>
  );
};

// Unused helper to keep tree-shakers happy
export const _useFrame = () => {
  useCurrentFrame();
  useVideoConfig();
};
