import React from "react";
import { AbsoluteFill, interpolate, useCurrentFrame, Easing, spring, useVideoConfig } from "remotion";
import { PHOTONECT } from "../../PhotonectBrandReel/brand";
import { FONT_ARABIC, FONT_LATIN } from "../../PhotonectBrandReel/fonts";
import { VideoBackdrop } from "../VideoBackdrop";
import type { BeatProps } from "../schema";
import {
  CONTENT_TOP,
  CONTENT_BOTTOM,
  CONTENT_WIDTH,
  STAT_MAX_WIDTH,
  PLATFORM_SAFE,
  adaptiveFontSize,
} from "../safeArea";
import { parseStat, BeatStatPill, formatStatNumber } from "./BeatA";

type Props = BeatProps & {
  index: number;
  durationFrames: number;
  hideBackdrop?: boolean;
};

// V6 — Variant C CINEMA REVEAL (2026-04-22)
// Restores V4 content density — arabicBody + 3 supportingStats — with a
// bottom-anchored cinematic layout. Full-bleed broll + progressive reveal
// stack: hairline label → Arabic heading → body → inline stat → 3 pills.
// Content is flex-anchored from bottom via `bottom: PLATFORM_SAFE.bottom` so
// nothing ever enters the IG caption-drawer strip.
export const BeatC: React.FC<Props> = ({
  label,
  arabicHeading,
  arabicBody,
  bigStat,
  supportingStats,
  broll,
  brollType,
  accent,
  index,
  durationFrames,
  hideBackdrop,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const a = accent ?? PHOTONECT.signal;

  // V10 — compressed cinematic reveal so the whole stack lands by ~frame 95 (3s)
  // and holds. Ahmed: "too fast, I can't read the facts."
  const labelReveal = interpolate(frame, [6, 24], [0, 1], {
    easing: Easing.bezier(0.22, 1, 0.36, 1),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const headingReveal = interpolate(frame, [20, 50], [0, 1], {
    easing: Easing.bezier(0.16, 1, 0.3, 1),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const bodyReveal = interpolate(frame, [44, 72], [0, 1], {
    easing: Easing.bezier(0.16, 1, 0.3, 1),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const statReveal = spring({
    frame: frame - 74,
    fps,
    config: { damping: 22, stiffness: 70, mass: 1 },
  });

  const pillsStartFrame = 86;

  const bottomScrim = interpolate(frame, [0, 60], [0.4, 0.88], {
    extrapolateRight: "clamp",
  });
  const scrimHex = Math.round(bottomScrim * 255).toString(16).padStart(2, "0");

  // 2026-05-03: Ahmed feedback "make it bigger ~15%". Tightened text caps
  // mean the shorter tier is now the common case; bumped each tier ~15-18%.
  const headingLen = arabicHeading.length;
  const headingFontSize = headingLen > 70 ? 54 : headingLen > 50 ? 60 : 68;

  const bodyLen = (arabicBody ?? "").length;
  const bodyFontSize = bodyLen > 140 ? 26 : bodyLen > 100 ? 28 : 30;

  return (
    <AbsoluteFill>
      {!hideBackdrop && (
        <VideoBackdrop
          src={broll}
          type={brollType}
          accent={a}
          intensity="hero"
          durationFrames={durationFrames}
        />
      )}

      {/* Gradient scrim — dark bottom, transparent top */}
      <AbsoluteFill
        style={{
          background: `linear-gradient(180deg, transparent 0%, transparent 30%, ${PHOTONECT.ink}${scrimHex} 100%)`,
        }}
      />

      {/* ABSOLUTE content — anchored to bottom-safe line, stacks upward */}
      <div
        style={{
          position: "absolute",
          left: PLATFORM_SAFE.left,
          right: PLATFORM_SAFE.right,
          bottom: PLATFORM_SAFE.bottom,
          display: "flex",
          flexDirection: "column",
          alignItems: "flex-start",
          direction: "rtl",
          gap: 14,
          maxHeight: CONTENT_BOTTOM - CONTENT_TOP,
          overflow: "hidden",
        }}
      >
        {/* INLINE STAT — reveals after heading */}
        {bigStat && (
          <div
            style={{
              display: "flex",
              alignItems: "baseline",
              gap: 18,
              opacity: statReveal,
              transform: `translateY(${(1 - statReveal) * 14}px)`,
              direction: "rtl",
              maxWidth: STAT_MAX_WIDTH,
            }}
          >
            <div
              style={{
                fontFamily: FONT_LATIN,
                fontWeight: 900,
                fontSize: adaptiveFontSize(96, bigStat.value.length, 400),
                color: a,
                lineHeight: 0.95,
                letterSpacing: "-0.04em",
                textShadow: `0 4px 20px ${a}44`,
                whiteSpace: "nowrap",
              }}
            >{cinemaStat(bigStat.value, frame)}</div>
            <div
              style={{
                fontFamily: FONT_ARABIC,
                fontWeight: 500,
                fontSize: 22,
                color: PHOTONECT.paper,
                opacity: 0.82,
                maxWidth: 320,
                textAlign: "right",
                lineHeight: 1.35,
              }}
            >{bigStat.arabicLabel}</div>
          </div>
        )}

        {/* 3 STAT PILLS — placed between stat and body for visual rhythm */}
        {supportingStats && supportingStats.length > 0 && (
          <div
            style={{
              display: "flex",
              flexDirection: "row-reverse",
              gap: 10,
              width: "100%",
              maxWidth: CONTENT_WIDTH,
            }}
          >
            {supportingStats.slice(0, 3).map((s, i) => (
              <BeatStatPill
                key={i}
                label={s.label}
                value={s.value}
                accent={a}
                startFrame={pillsStartFrame + i * 4}
                frame={frame}
              />
            ))}
          </div>
        )}

        {/* ARABIC BODY */}
        {arabicBody && (
          <div
            style={{
              fontFamily: FONT_ARABIC,
              fontWeight: 500,
              fontSize: bodyFontSize,
              color: PHOTONECT.paper,
              opacity: bodyReveal * 0.92,
              transform: `translateY(${(1 - bodyReveal) * 14}px)`,
              lineHeight: 1.5,
              textAlign: "right",
              direction: "rtl",
              maxWidth: CONTENT_WIDTH,
              textShadow: `0 2px 12px ${PHOTONECT.ink}`,
            }}
          >{arabicBody}</div>
        )}

        {/* CINEMATIC HEADING */}
        <div
          style={{
            fontFamily: FONT_ARABIC,
            fontWeight: 700,
            fontSize: headingFontSize,
            color: PHOTONECT.paper,
            lineHeight: 1.22,
            textAlign: "right",
            direction: "rtl",
            opacity: headingReveal,
            transform: `translateY(${(1 - headingReveal) * 28}px)`,
            textShadow: `0 6px 28px ${PHOTONECT.ink}`,
            letterSpacing: "-0.005em",
            maxWidth: CONTENT_WIDTH,
          }}
        >{arabicHeading}</div>

        {/* HAIRLINE LABEL */}
        <div
          style={{
            display: "flex",
            alignItems: "center",
            gap: 14,
            opacity: labelReveal,
            transform: `translateY(${(1 - labelReveal) * 8}px)`,
            direction: "ltr",
          }}
        >
          <div
            style={{
              fontFamily: FONT_LATIN,
              fontWeight: 900,
              fontSize: 20,
              color: a,
              letterSpacing: "0.28em",
            }}
          >{`· ${String(index).padStart(2, "0")}`}</div>
          <div style={{ width: 42, height: 1, background: a, opacity: 0.85 }} />
          <div
            style={{
              fontFamily: FONT_ARABIC,
              fontWeight: 700,
              fontSize: 24,
              color: a,
              letterSpacing: "0.02em",
            }}
          >{label}</div>
        </div>
      </div>
    </AbsoluteFill>
  );
};

function cinemaStat(value: string, frame: number) {
  const { numPart, prefix, suffix, decimals } = parseStat(value);
  if (numPart == null) return value;
  const prog = Math.max(0, Math.min(1, (frame - 74) / 36));
  const ease = 1 - Math.pow(1 - prog, 2);
  return `${prefix}${formatStatNumber(numPart * ease, decimals)}${suffix}`;
}
