import React from "react";
import { AbsoluteFill, interpolate, Easing } from "remotion";
import { useSceneProgress } from "../useSceneProgress";
import { FONT_LATIN, FONT_ARABIC } from "../fonts";

type Props = {
  latin: string;
  arabic?: string;
  paper: string;
  accent: string;
};

// Word-stagger helper
const WordStack: React.FC<{
  words: string[];
  fontFamily: string;
  fontSize: number;
  color: string;
  direction: "ltr" | "rtl";
  frame: number;
  fps: number;
  startDelayFrames: number;
  exit: number;
}> = ({ words, fontFamily, fontSize, color, direction, frame, fps, startDelayFrames, exit }) => {
  // CRITICAL: do NOT reverse the array for RTL. `dir="rtl"` on the container
  // handles visual word order automatically. Manual reversal = reversed reading order.
  return (
    <div
      style={{
        display: "flex",
        flexDirection: "row",
        gap: 16,
        direction,
        justifyContent: "center",
        flexWrap: "wrap",
      }}
    >
      {words.map((w, i) => {
        const delay = startDelayFrames + i * 4;
        const p = interpolate(frame, [delay, delay + 0.5 * fps], [0, 1], {
          easing: Easing.bezier(0.16, 1, 0.3, 1),
          extrapolateLeft: "clamp",
          extrapolateRight: "clamp",
        });
        return (
          <span
            key={i}
            style={{
              fontFamily,
              fontSize,
              fontWeight: 700,
              color,
              opacity: p * (1 - exit),
              transform: `translateY(${(1 - p) * 30}px)`,
              display: "inline-block",
              letterSpacing: "-0.02em",
            }}
          >
            {w}
          </span>
        );
      })}
    </div>
  );
};

export const SceneTagline: React.FC<Props> = ({ latin, arabic, paper, accent }) => {
  const { frame, fps, exit } = useSceneProgress(0.5, 0.3);
  const latinWords = latin.split(" ");
  const arabicWords = arabic ? arabic.split(" ") : [];

  // Accent divider fade
  const divider = interpolate(frame, [0.3 * fps, 1.0 * fps], [0, 1], {
    easing: Easing.bezier(0.16, 1, 0.3, 1),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

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
          gap: 42,
          width: "100%",
        }}
      >
        <WordStack
          words={latinWords}
          fontFamily={FONT_LATIN}
          fontSize={88}
          color={paper}
          direction="ltr"
          frame={frame}
          fps={fps}
          startDelayFrames={0}
          exit={exit}
        />
        {arabic ? (
          <>
            <div
              style={{
                height: 2,
                width: 200,
                background: accent,
                transform: `scaleX(${divider})`,
                transformOrigin: "center center",
                opacity: 1 - exit,
              }}
            />
            <WordStack
              words={arabicWords}
              fontFamily={FONT_ARABIC}
              fontSize={78}
              color={paper}
              direction="rtl"
              frame={frame}
              fps={fps}
              startDelayFrames={Math.round(0.4 * fps)}
              exit={exit}
            />
          </>
        ) : null}
      </div>
    </AbsoluteFill>
  );
};
