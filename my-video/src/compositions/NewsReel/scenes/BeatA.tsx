import React from "react";
import { AbsoluteFill, interpolate, useCurrentFrame, Easing, spring, useVideoConfig } from "remotion";
import { PHOTONECT } from "../../PhotonectBrandReel/brand";
import { FONT_ARABIC, FONT_LATIN } from "../../PhotonectBrandReel/fonts";
import { VideoBackdrop } from "../VideoBackdrop";
import type { BeatProps } from "../schema";
import {
  CONTENT_TOP,
  CONTENT_HEIGHT,
  CONTENT_WIDTH,
  STAT_MAX_WIDTH,
  PLATFORM_SAFE,
  adaptiveFontSize,
} from "../safeArea";

type Props = BeatProps & {
  index: number;
  durationFrames: number;
  hideBackdrop?: boolean;
};

// V6 — Variant A MONEY-SHOT (2026-04-22)
// Restores V4 content density — arabicBody + 3 supportingStats — after V5
// over-stripped to fix margin cutoffs. Safe-zone discipline retained via
// overflow:hidden + adaptive font sizing. Distinct signature: vertical accent
// BAR label + GIANT stat slam + heading + body + 3-pill row.
//
// Content contract per beat:
//   label (Arabic) + arabicHeading (bold, 2-3 lines) + arabicBody (20-30 words)
//   + bigStat (hero number + Arabic gloss) + supportingStats (3 compact pills)
//
// Vertical budget (1156px between CONTENT_TOP=364 and CONTENT_BOTTOM=1520):
//   label 70 + stat 230 + heading 150 + body 110 + pills 80 = ~640px used,
//   leaves ~500px of slack absorbed by flex justifyContent:center.
export const BeatA: React.FC<Props> = ({
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

  // V10 reveal schedule — COMPRESSED so all text lands by ~frame 95 (3.2s) then
  // holds for the rest of the 15s beat. Ahmed: "the speed to show it is too fast,
  // I can't read the facts." Earlier reveal = longer readable hold.
  const labelReveal = spring({ frame, fps, config: { damping: 16 } });
  const slamIn = spring({
    frame: frame - 6,
    fps,
    config: { damping: 9, stiffness: 140, mass: 0.9 },
  });
  const slamTY = (1 - slamIn) * -36;

  // Count-up — preserves decimals (V10.1: was Math.round, which turned 1.75→2)
  const { numPart, suffix, prefix, decimals } = parseStat(bigStat?.value);
  const countProg = interpolate(frame, [10, 34], [0, 1], {
    easing: Easing.bezier(0.22, 1, 0.36, 1),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const countVal = numPart != null ? numPart * countProg : null;
  const displayedStat = bigStat
    ? countVal != null
      ? `${prefix}${formatStatNumber(countVal, decimals)}${suffix}`
      : bigStat.value
    : "";

  const headingReveal = spring({
    frame: frame - 28,
    fps,
    config: { damping: 18, stiffness: 110 },
  });

  const bodyReveal = interpolate(frame, [44, 70], [0, 1], {
    easing: Easing.bezier(0.22, 1, 0.36, 1),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const pillsReveal = interpolate(frame, [74, 98], [0, 1], {
    easing: Easing.bezier(0.22, 1, 0.36, 1),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const flashOpacity = interpolate(frame, [14, 20, 32], [0, 0.55, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const statFontSize = adaptiveFontSize(200, displayedStat.length, STAT_MAX_WIDTH);

  // 2026-05-03: Ahmed feedback "tune text down by 30% and make it bigger".
  // With body word caps cut from 80-130w to 55-90w, bodyLen now sits in
  // ~60-100 range — so the shortest tier is the typical case. Each tier
  // bumped ~12-15% so the shortest body breathes at 30px instead of 26.
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

      {/* Dark scrim below for body/pills legibility — bottom 42% of canvas */}
      <AbsoluteFill
        style={{
          background: `linear-gradient(180deg, transparent 0%, transparent 40%, ${PHOTONECT.ink}C8 75%, ${PHOTONECT.ink}E0 100%)`,
        }}
      />

      {/* Radial flash — pulses once during slam */}
      <AbsoluteFill
        style={{
          background: `radial-gradient(circle at 50% 45%, ${a}AA 0%, transparent 55%)`,
          opacity: flashOpacity,
          mixBlendMode: "screen",
        }}
      />

      {/* ABSOLUTE content container — explicit top/height + overflow:hidden */}
      <div
        style={{
          position: "absolute",
          top: CONTENT_TOP,
          left: PLATFORM_SAFE.left,
          right: PLATFORM_SAFE.right,
          height: CONTENT_HEIGHT,
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          alignItems: "flex-end",
          direction: "rtl",
          gap: 16,
          overflow: "hidden",
        }}
      >
        {/* BAR LABEL */}
        <div
          style={{
            display: "flex",
            alignItems: "stretch",
            gap: 0,
            opacity: labelReveal,
            transform: `translateY(${(1 - labelReveal) * 16}px)`,
            direction: "ltr",
          }}
        >
          <div style={{ width: 6, background: a }} />
          <div
            style={{
              padding: "6px 18px",
              display: "flex",
              flexDirection: "column",
              gap: 0,
              background: `${PHOTONECT.ink}CC`,
              borderTop: `1px solid ${a}44`,
              borderBottom: `1px solid ${a}44`,
              borderRight: `1px solid ${a}44`,
            }}
          >
            <div
              style={{
                fontFamily: FONT_LATIN,
                fontWeight: 900,
                fontSize: 14,
                color: a,
                letterSpacing: "0.24em",
                lineHeight: 1,
              }}
            >{`CH ${String(index).padStart(2, "0")}`}</div>
            <div
              style={{
                fontFamily: FONT_ARABIC,
                fontWeight: 700,
                fontSize: 26,
                color: PHOTONECT.paper,
                letterSpacing: "0.02em",
                lineHeight: 1.15,
                marginTop: 3,
              }}
            >{label}</div>
          </div>
        </div>

        {/* GIANT STAT */}
        {bigStat && (
          <div
            style={{
              textAlign: "right",
              opacity: slamIn,
              transform: `translateY(${slamTY}px)`,
              maxWidth: STAT_MAX_WIDTH,
              width: "100%",
            }}
          >
            <div
              style={{
                fontFamily: FONT_LATIN,
                fontWeight: 900,
                fontSize: statFontSize,
                color: a,
                lineHeight: 0.9,
                letterSpacing: "-0.05em",
                textShadow: `0 10px 60px ${a}66, 0 2px 0 ${PHOTONECT.ink}`,
                whiteSpace: "nowrap",
                overflow: "hidden",
              }}
            >{displayedStat}</div>
            <div
              style={{
                fontFamily: FONT_ARABIC,
                fontWeight: 700,
                fontSize: 26,
                color: PHOTONECT.paper,
                opacity: Math.max(0, interpolate(frame, [26, 44], [0, 0.92])),
                marginTop: 6,
                textAlign: "right",
                maxWidth: STAT_MAX_WIDTH,
                lineHeight: 1.2,
              }}
            >{bigStat.arabicLabel}</div>
          </div>
        )}

        {/* ARABIC HEADING */}
        <div
          style={{
            fontFamily: FONT_ARABIC,
            fontWeight: 700,
            fontSize: 48,
            color: PHOTONECT.paper,
            lineHeight: 1.22,
            textAlign: "right",
            direction: "rtl",
            opacity: headingReveal,
            transform: `translateY(${(1 - headingReveal) * 24}px)`,
            textShadow: `0 4px 24px ${PHOTONECT.ink}EE`,
            maxWidth: CONTENT_WIDTH,
            letterSpacing: "-0.005em",
          }}
        >{arabicHeading}</div>

        {/* ARABIC BODY — restored from V4, capped via adaptive font */}
        {arabicBody && (
          <div
            style={{
              fontFamily: FONT_ARABIC,
              fontWeight: 500,
              fontSize: bodyFontSize,
              color: PHOTONECT.paper,
              opacity: bodyReveal * 0.94,
              lineHeight: 1.5,
              textAlign: "right",
              direction: "rtl",
              maxWidth: CONTENT_WIDTH,
              textShadow: `0 2px 12px ${PHOTONECT.ink}`,
              transform: `translateY(${(1 - bodyReveal) * 14}px)`,
            }}
          >{arabicBody}</div>
        )}

        {/* SUPPORTING STATS — 3 compact pills, horizontal RTL row */}
        {supportingStats && supportingStats.length > 0 && (
          <div
            style={{
              display: "flex",
              flexDirection: "row-reverse",
              gap: 12,
              maxWidth: CONTENT_WIDTH,
              width: "100%",
              opacity: pillsReveal,
              transform: `translateY(${(1 - pillsReveal) * 14}px)`,
            }}
          >
            {supportingStats.slice(0, 3).map((s, i) => (
              <StatPill key={i} label={s.label} value={s.value} accent={a} startFrame={74 + i * 4} frame={frame} />
            ))}
          </div>
        )}
      </div>
    </AbsoluteFill>
  );
};

const StatPill: React.FC<{ label: string; value: string; accent: string; startFrame: number; frame: number }> = ({
  label,
  value,
  accent,
  startFrame,
  frame,
}) => {
  const r = interpolate(frame, [startFrame, startFrame + 30], [0, 1], {
    easing: Easing.bezier(0.22, 1, 0.36, 1),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  return (
    <div
      style={{
        flex: 1,
        minWidth: 0,
        padding: "10px 14px",
        background: `${PHOTONECT.ink}D0`,
        border: `1px solid ${accent}80`,
        borderRadius: 4,
        display: "flex",
        flexDirection: "column",
        alignItems: "flex-end",
        direction: "rtl",
        opacity: r,
        transform: `translateY(${(1 - r) * 10}px)`,
      }}
    >
      <div
        style={{
          fontFamily: FONT_LATIN,
          fontWeight: 900,
          fontSize: 26,
          color: accent,
          letterSpacing: "-0.02em",
          lineHeight: 1,
          whiteSpace: "nowrap",
          overflow: "hidden",
          textOverflow: "clip",
          maxWidth: "100%",
        }}
      >{value}</div>
      <div
        style={{
          fontFamily: FONT_ARABIC,
          fontWeight: 500,
          fontSize: 14,
          color: PHOTONECT.paper,
          opacity: 0.82,
          marginTop: 3,
          textAlign: "right",
          lineHeight: 1.25,
          letterSpacing: "0.01em",
          overflow: "hidden",
          display: "-webkit-box",
          WebkitLineClamp: 2,
          WebkitBoxOrient: "vertical",
        }}
      >{label}</div>
    </div>
  );
};

export function parseStat(value: string | undefined) {
  if (!value) return { numPart: null as number | null, prefix: "", suffix: "", decimals: 0 };
  const m = value.trim().match(/^([^\d\-]*)([\d,.]+)(.*)$/);
  if (!m) return { numPart: null, prefix: "", suffix: "", decimals: 0 };
  const raw = m[2].replace(/,/g, "");
  const num = parseFloat(raw);
  if (!isFinite(num)) return { numPart: null, prefix: "", suffix: "", decimals: 0 };
  const dot = raw.indexOf(".");
  const decimals = dot >= 0 ? raw.length - dot - 1 : 0;
  return { numPart: num, prefix: m[1] || "", suffix: m[3] || "", decimals };
}

// V10.1 — count-up formatter that PRESERVES the original's decimal places.
// Previously Math.round turned "$1.75T" -> "$2.0T" and "$1.25T" -> "$1.0T".
// Ints get thousands separators; decimals keep their exact precision.
export function formatStatNumber(n: number, decimals: number) {
  if (decimals > 0) return n.toFixed(decimals);
  return Math.round(n).toLocaleString("en-US");
}

// Re-export StatPill so BeatB and BeatC can share one visual vocabulary.
export { StatPill as BeatStatPill };
