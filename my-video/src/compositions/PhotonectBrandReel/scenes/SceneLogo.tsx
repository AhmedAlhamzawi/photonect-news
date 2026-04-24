import React from "react";
import { AbsoluteFill, interpolate, useCurrentFrame, useVideoConfig, Easing } from "remotion";
import { LogoMark, Wordmark } from "../LogoMark";
import { useSceneProgress } from "../useSceneProgress";
import { FONT_LATIN } from "../fonts";

type Props = {
  brandName: string;
  primary: string;
  accent: string;
  paper: string;
};

export const SceneLogo: React.FC<Props> = ({ brandName, primary, accent, paper }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const { progress, exit } = useSceneProgress(0.8, 0.3);

  // Mark draws from frame 0 to ~1s
  const draw = interpolate(frame, [0, 1 * fps], [0, 1], {
    easing: Easing.bezier(0.16, 1, 0.3, 1),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Wordmark fades in after mark completes (~1s)
  const wordmarkProgress = interpolate(frame, [1 * fps, 1.8 * fps], [0, 1], {
    easing: Easing.bezier(0.16, 1, 0.3, 1),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const wordmarkOpacity = wordmarkProgress * (1 - exit);
  const wordmarkX = interpolate(wordmarkProgress, [0, 1], [-30, 0]);

  // Accent underline stroke
  const underline = interpolate(frame, [1.5 * fps, 2.2 * fps], [0, 1], {
    easing: Easing.bezier(0.65, 0, 0.35, 1),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const groupScale = interpolate(progress, [0, 1], [0.96, 1]);
  const groupY = interpolate(progress, [0, 1], [20, 0]);

  return (
    <AbsoluteFill
      style={{
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <div
        style={{
          transform: `translateY(${groupY}px) scale(${groupScale})`,
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          gap: 36,
        }}
      >
        <LogoMark size={280} primary={paper} accent={accent} draw={draw} />
        <Wordmark
          text={brandName}
          fontFamily={FONT_LATIN}
          color={paper}
          opacity={wordmarkOpacity}
          x={wordmarkX}
          fontSize={110}
        />
        {/* Accent underline */}
        <div
          style={{
            height: 4,
            width: 420,
            background: accent,
            transform: `scaleX(${underline})`,
            transformOrigin: "left center",
            borderRadius: 2,
            opacity: 1 - exit,
            marginTop: -12,
          }}
        />
      </div>
    </AbsoluteFill>
  );
};
