import React from "react";
import { AbsoluteFill, useCurrentFrame, interpolate, spring, useVideoConfig, Easing } from "remotion";
import type { BeatProps, VariantName } from "../schema";
import { BeatA } from "./BeatA";
import { BeatB } from "./BeatB";
import { BeatC } from "./BeatC";
import { SourceChip } from "../components/SourceChip";
import { SubtitleBar } from "../components/SubtitleBar";

type Props = BeatProps & {
  index: number;
  durationFrames: number;
  variant: VariantName;
};

// V7 leap dispatcher — wraps the variant-specific Beat scene with two new
// overlays applied to ALL beats:
//
//   1. SourceChip (lower-left) — persistent attribution chip showing the
//      broll's source. Pattern from Vox/C4/Reuters: credibility as design.
//
//   2. SubtitleBar (bottom 96px) — phrase-by-phrase Arabic caption bar.
//      Pattern from BBC/Vice: sound-off design system.
//
// AND: when index === 3 (the climax beat), an extra GiantStatStamp overlay
// kicks in around 60% through the beat. Pattern from Bloomberg/Vox: the
// killer number isn't a card, it's stamped 60-70% of frame width over the
// broll. The viewer can't miss the anchor.

const GiantStatStamp: React.FC<{
  value?: string;
  arabicLabel?: string;
  durationFrames: number;
}> = ({ value, arabicLabel, durationFrames }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  if (!value) return null;

  // The stat lands at 55% of the beat (BEAT3=240 → frame 132 of beat-local).
  const stampStart = Math.floor(durationFrames * 0.55);
  const stampHold = 60;       // 2s hold
  const stampOutFade = 18;    // 0.6s fade

  // Spring scale-in
  const scaleIn = spring({
    frame: frame - stampStart,
    fps,
    config: { damping: 14, mass: 0.6, stiffness: 120 },
  });

  // Fade out at the end of the hold window
  const fadeOut = interpolate(
    frame,
    [stampStart + stampHold, stampStart + stampHold + stampOutFade],
    [1, 0],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" },
  );

  if (frame < stampStart || frame > stampStart + stampHold + stampOutFade) {
    return null;
  }

  const scale = 0.6 + 0.4 * scaleIn;
  const opacity = scaleIn * fadeOut;

  return (
    <AbsoluteFill
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        pointerEvents: "none",
        opacity,
      }}
    >
      {/* Vignette pulse to pull the eye centerward */}
      <div
        style={{
          position: "absolute",
          inset: 0,
          background:
            "radial-gradient(ellipse at 50% 50%, rgba(0,0,0,0.0) 0%, rgba(0,0,0,0.55) 100%)",
          pointerEvents: "none",
        }}
      />
      {/* The giant number — 60% of frame width, ivory white, drop shadow */}
      <div
        style={{
          fontFamily:
            '"Tajawal", "Inter", "SF Pro Display", system-ui, sans-serif',
          fontWeight: 900,
          fontSize: 320,                                     // 30% of 1080 width visually
          lineHeight: 0.95,
          letterSpacing: "-0.04em",
          color: "rgba(255, 252, 242, 0.97)",
          textShadow:
            "0 12px 48px rgba(0,0,0,0.85), 0 4px 12px rgba(0,0,0,0.9)",
          transform: `scale(${scale})`,
          transformOrigin: "center",
        }}
      >
        {value}
      </div>
      {/* Small Arabic label sliding up under the number */}
      {arabicLabel ? (
        <div
          style={{
            marginTop: 24,
            fontFamily: '"Tajawal", "Noto Sans Arabic", sans-serif',
            fontWeight: 600,
            fontSize: 44,
            color: "rgba(255, 194, 23, 0.95)",                  // brand gold
            letterSpacing: "0.02em",
            direction: "rtl",
            opacity: scaleIn,
            transform: `translateY(${(1 - scaleIn) * 16}px)`,
            textShadow: "0 4px 16px rgba(0,0,0,0.7)",
          }}
        >
          {arabicLabel}
        </div>
      ) : null}
    </AbsoluteFill>
  );
};

export const Beat: React.FC<Props> = (props) => {
  let scene: React.ReactNode;
  switch (props.variant) {
    case "B":
      scene = <BeatB {...props} />;
      break;
    case "C":
      scene = <BeatC {...props} />;
      break;
    case "A":
    default:
      scene = <BeatA {...props} />;
      break;
  }

  return (
    <AbsoluteFill>
      {scene}
      <SubtitleBar
        phrases={props.subtitlePhrases}
        durationFrames={props.durationFrames}
      />
      <SourceChip
        source={props.brollSource}
        durationFrames={props.durationFrames}
      />
      {props.index === 3 ? (
        <GiantStatStamp
          value={props.bigStat?.value}
          arabicLabel={props.bigStat?.arabicLabel}
          durationFrames={props.durationFrames}
        />
      ) : null}
    </AbsoluteFill>
  );
};
