import React from "react";
import { AbsoluteFill, interpolate, Easing } from "remotion";
import { useSceneProgress } from "../useSceneProgress";
import { FONT_LATIN } from "../fonts";

type Props = {
  index: number; // 1, 2, 3
  headline: string;
  body?: string;
  paper: string;
  accent: string;
  ink: string;
};

export const SceneBenefit: React.FC<Props> = ({
  index,
  headline,
  body,
  paper,
  accent,
  ink,
}) => {
  const { frame, fps, progress, exit } = useSceneProgress(0.6, 0.3);

  // Big numeral enters from left
  const numeralP = interpolate(frame, [0, 0.5 * fps], [0, 1], {
    easing: Easing.bezier(0.16, 1, 0.3, 1),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const numeralX = interpolate(numeralP, [0, 1], [-120, 0]);
  const numeralOpacity = numeralP * (1 - exit);

  // Headline enters word by word
  const headlineWords = headline.split(" ");

  // Body slides up
  const bodyP = interpolate(frame, [0.6 * fps, 1.2 * fps], [0, 1], {
    easing: Easing.bezier(0.16, 1, 0.3, 1),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Accent bar
  const barP = interpolate(frame, [0.3 * fps, 0.9 * fps], [0, 1], {
    easing: Easing.bezier(0.65, 0, 0.35, 1),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill
      style={{
        padding: "160px 100px",
        justifyContent: "center",
      }}
    >
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          alignItems: "flex-start",
          gap: 32,
          transform: `scale(${interpolate(progress, [0, 1], [0.98, 1])})`,
          transformOrigin: "left center",
        }}
      >
        {/* Big numeral */}
        <div
          style={{
            fontFamily: FONT_LATIN,
            fontWeight: 900,
            fontSize: 320,
            lineHeight: 0.85,
            color: "transparent",
            WebkitTextStroke: `3px ${accent}`,
            opacity: numeralOpacity,
            transform: `translateX(${numeralX}px)`,
            letterSpacing: "-0.05em",
          }}
        >
          0{index}
        </div>

        {/* Accent bar */}
        <div
          style={{
            height: 6,
            width: 160,
            background: accent,
            transform: `scaleX(${barP})`,
            transformOrigin: "left center",
            borderRadius: 3,
            opacity: 1 - exit,
          }}
        />

        {/* Headline word-stagger */}
        <div
          style={{
            display: "flex",
            flexWrap: "wrap",
            gap: 18,
            fontFamily: FONT_LATIN,
            fontWeight: 700,
            fontSize: 92,
            color: paper,
            lineHeight: 1.05,
            letterSpacing: "-0.025em",
            maxWidth: 880,
          }}
        >
          {headlineWords.map((w, i) => {
            const delay = Math.round(0.4 * fps) + i * 3;
            const p = interpolate(frame, [delay, delay + 0.5 * fps], [0, 1], {
              easing: Easing.bezier(0.16, 1, 0.3, 1),
              extrapolateLeft: "clamp",
              extrapolateRight: "clamp",
            });
            return (
              <span
                key={i}
                style={{
                  display: "inline-block",
                  opacity: p * (1 - exit),
                  transform: `translateY(${(1 - p) * 40}px)`,
                }}
              >
                {w}
              </span>
            );
          })}
        </div>

        {body ? (
          <div
            style={{
              fontFamily: FONT_LATIN,
              fontWeight: 400,
              fontSize: 38,
              color: paper,
              opacity: bodyP * 0.7 * (1 - exit),
              transform: `translateY(${(1 - bodyP) * 20}px)`,
              maxWidth: 820,
              lineHeight: 1.35,
            }}
          >
            {body}
          </div>
        ) : null}
      </div>
    </AbsoluteFill>
  );
};
