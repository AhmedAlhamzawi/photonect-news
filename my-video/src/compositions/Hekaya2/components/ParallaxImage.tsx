import React from "react";
import {
  AbsoluteFill,
  Img,
  interpolate,
  useCurrentFrame,
  Easing,
  staticFile,
} from "remotion";
import { HEKAYA_PALETTE } from "../schema";

interface Props {
  src: string;
  durationFrames: number;
  /** Background drift direction. Default "in" (slow zoom in). */
  direction?: "in" | "out" | "left" | "right";
  /** Apply duotone treatment for archival feel. Default false. */
  duotone?: boolean;
  /** Apply warm vignette + top/bottom gradient. Default true. */
  vignette?: boolean;
}

/**
 * 2.5D parallax photo treatment — the visual workhorse for Hekaya2.
 *
 * Two layers of the same image translate / scale at different rates,
 * creating a felt depth that flat Ken-Burns can't deliver. The
 * background does the slow ambient drift; the foreground (lower
 * opacity, slightly tighter scale) moves opposite, giving the eye a
 * micro-cue that this is a *scene*, not a slide.
 *
 * Optional duotone treatment shifts colour toward gold-on-blue —
 * use on every third image in a chapter cycle for archival rhythm.
 */
export const ParallaxImage: React.FC<Props> = ({
  src,
  durationFrames,
  direction = "in",
  duotone = false,
  vignette = true,
}) => {
  const frame = useCurrentFrame();
  const progress = interpolate(frame, [0, durationFrames], [0, 1], {
    extrapolateRight: "clamp",
  });

  // Background drift parameters
  let bgScale = 1;
  let bgTx = 0;
  let bgTy = 0;

  if (direction === "in") {
    bgScale = interpolate(progress, [0, 1], [1.0, 1.1], {
      easing: Easing.bezier(0.25, 0, 0.25, 1),
    });
  } else if (direction === "out") {
    bgScale = interpolate(progress, [0, 1], [1.16, 1.04]);
  } else if (direction === "left") {
    bgScale = 1.12;
    bgTx = interpolate(progress, [0, 1], [-2.5, 2.5]);
  } else {
    bgScale = 1.12;
    bgTx = interpolate(progress, [0, 1], [2.5, -2.5]);
  }

  // Foreground moves opposite for the parallax illusion
  const fgScale = bgScale * 1.04;
  const fgTx = -bgTx * 0.4;
  const fgTy = -bgTy * 0.4;

  const resolvedSrc = src.startsWith("http") ? src : staticFile(src);

  // Duotone via CSS filter chain — cheap and effective for archival look
  const filter = duotone
    ? "grayscale(60%) sepia(25%) hue-rotate(-25deg) brightness(0.9) contrast(1.05)"
    : undefined;

  return (
    <AbsoluteFill
      style={{
        overflow: "hidden",
        backgroundColor: HEKAYA_PALETTE.shadow,
      }}
    >
      {/* Background plane — full image, slow drift */}
      <Img
        src={resolvedSrc}
        style={{
          width: "100%",
          height: "100%",
          objectFit: "cover",
          transform: `scale(${bgScale}) translate(${bgTx}%, ${bgTy}%)`,
          filter,
        }}
      />
      {/* Foreground plane — opposite drift, lower opacity */}
      <AbsoluteFill style={{ opacity: 0.45 }}>
        <Img
          src={resolvedSrc}
          style={{
            width: "100%",
            height: "100%",
            objectFit: "cover",
            transform: `scale(${fgScale}) translate(${fgTx}%, ${fgTy}%)`,
            filter,
          }}
        />
      </AbsoluteFill>

      {vignette ? (
        <>
          <AbsoluteFill
            style={{
              background: `radial-gradient(ellipse at center,
                transparent 35%,
                ${HEKAYA_PALETTE.ink}99 75%,
                ${HEKAYA_PALETTE.ink} 100%)`,
            }}
          />
          <AbsoluteFill
            style={{
              background: `linear-gradient(180deg,
                ${HEKAYA_PALETTE.ink}40 0%,
                transparent 38%,
                transparent 62%,
                ${HEKAYA_PALETTE.ink}cc 100%)`,
            }}
          />
        </>
      ) : null}
    </AbsoluteFill>
  );
};
