import React from "react";
import { AbsoluteFill, interpolate, useCurrentFrame, spring, useVideoConfig } from "remotion";
import { PHOTONECT } from "../../PhotonectBrandReel/brand";
import { FONT_ARABIC, FONT_LATIN } from "../../PhotonectBrandReel/fonts";
import { VideoBackdrop } from "../VideoBackdrop";
import type { BeatProps } from "../schema";
import {
  CONTENT_WIDTH,
  SPLIT_TOP_HEIGHT,
  SPLIT_BOTTOM_HEIGHT,
  PLATFORM_SAFE,
  adaptiveFontSize,
} from "../safeArea";
import { parseStat, BeatStatPill } from "./BeatA";

type Props = BeatProps & {
  index: number;
  durationFrames: number;
};

// V6 — Variant B KINETIC SPLIT (2026-04-22)
// Restores V4 content density by splitting the data across both halves:
//   TOP half (broll 960px): bigStat floats in lower-right over dark gradient.
//   BOTTOM half (560px budget): strike label + kinetic heading + body + 3 pills.
// The V5 problem — cramming everything into 560px — is solved by moving the
// hero stat up into the broll region where it reads as a news chyron overlay.
export const BeatB: React.FC<Props> = ({
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
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const a = accent ?? PHOTONECT.signal;

  const labelReveal = spring({ frame, fps, config: { damping: 16 } });

  const words = arabicHeading.split(/\s+/).filter(Boolean);
  const WORD_STEP = 5;
  const wordStart = 12;
  const headingEndFrame = wordStart + words.length * WORD_STEP;

  const statRevealFrame = 20;
  const bodyRevealFrame = headingEndFrame + 10;
  const pillsRevealFrame = bodyRevealFrame + 24;

  // 2026-05-03: Ahmed feedback "make it bigger by ~15%". With heading caps
  // tightened to 1 short sentence and body caps cut to 55-90w, the shorter
  // tiers will be the typical case — bumped each tier ~15-18%.
  const headingLen = arabicHeading.length;
  const headingFontSize = headingLen > 70 ? 52 : headingLen > 50 ? 58 : 66;

  const bodyLen = (arabicBody ?? "").length;
  const bodyFontSize = bodyLen > 130 ? 24 : bodyLen > 95 ? 26 : 28;

  return (
    <AbsoluteFill>
      {/* TOP HALF — broll with stat overlay */}
      <div
        style={{
          position: "absolute",
          top: 0,
          left: 0,
          right: 0,
          height: SPLIT_TOP_HEIGHT,
          overflow: "hidden",
        }}
      >
        <VideoBackdrop
          src={broll}
          type={brollType}
          accent={a}
          intensity="hero"
          durationFrames={durationFrames}
        />

        {/* Lower-third scrim in top half (so stat reads over broll) */}
        <div
          style={{
            position: "absolute",
            left: 0,
            right: 0,
            bottom: 0,
            height: 220,
            background: `linear-gradient(180deg, transparent 0%, ${PHOTONECT.ink}CC 60%, ${PHOTONECT.ink}F0 100%)`,
          }}
        />

        {/* BIG STAT — overlaid as news chyron in lower-right of top half */}
        {bigStat && (
          <div
            style={{
              position: "absolute",
              right: PLATFORM_SAFE.right,
              bottom: 24,
              display: "flex",
              alignItems: "baseline",
              gap: 16,
              direction: "rtl",
              opacity: interpolate(frame, [statRevealFrame, statRevealFrame + 24], [0, 1], {
                extrapolateLeft: "clamp",
                extrapolateRight: "clamp",
              }),
              transform: `translateY(${(1 - Math.min(1, Math.max(0, (frame - statRevealFrame) / 24))) * 16}px)`,
              maxWidth: CONTENT_WIDTH,
            }}
          >
            <div
              style={{
                fontFamily: FONT_ARABIC,
                fontWeight: 500,
                fontSize: 22,
                color: PHOTONECT.paper,
                opacity: 0.88,
                maxWidth: 320,
                textAlign: "right",
                lineHeight: 1.35,
              }}
            >{bigStat.arabicLabel}</div>
            <div
              style={{
                fontFamily: FONT_LATIN,
                fontWeight: 900,
                fontSize: adaptiveFontSize(110, bigStat.value.length, 400),
                color: a,
                letterSpacing: "-0.04em",
                lineHeight: 1,
                whiteSpace: "nowrap",
                textShadow: `0 6px 30px ${a}88`,
              }}
            >{animatedStat(bigStat.value, frame, statRevealFrame)}</div>
          </div>
        )}

        {/* Accent seam between halves */}
        <div
          style={{
            position: "absolute",
            bottom: 0,
            left: 0,
            right: 0,
            height: 4,
            background: `linear-gradient(90deg, transparent, ${a} 50%, transparent)`,
            opacity: labelReveal,
          }}
        />
      </div>

      {/* BOTTOM HALF — studio dark, text stack */}
      <div
        style={{
          position: "absolute",
          top: SPLIT_TOP_HEIGHT,
          left: PLATFORM_SAFE.left,
          right: PLATFORM_SAFE.right,
          height: SPLIT_BOTTOM_HEIGHT,
          background: `linear-gradient(180deg, ${PHOTONECT.ink}FA 0%, ${PHOTONECT.ink} 100%)`,
          display: "flex",
          flexDirection: "column",
          justifyContent: "flex-start",
          alignItems: "flex-end",
          direction: "rtl",
          paddingTop: 28,
          paddingBottom: 16,
          overflow: "hidden",
          gap: 14,
        }}
      >
        {/* STRIKE LABEL */}
        <div
          style={{
            opacity: labelReveal,
            transform: `translateY(${(1 - labelReveal) * 16}px)`,
            position: "relative",
            display: "inline-flex",
            flexDirection: "column",
            alignItems: "flex-end",
          }}
        >
          <div
            style={{
              display: "flex",
              alignItems: "baseline",
              gap: 12,
              direction: "ltr",
            }}
          >
            <div
              style={{
                fontFamily: FONT_LATIN,
                fontWeight: 900,
                fontSize: 14,
                color: a,
                letterSpacing: "0.28em",
              }}
            >{`//${String(index).padStart(2, "0")}`}</div>
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
          <div
            style={{
              width: "100%",
              height: 3,
              background: a,
              marginTop: 5,
              opacity: 0.85,
            }}
          />
        </div>

        {/* KINETIC HEADING — word-by-word slam */}
        <div
          style={{
            fontFamily: FONT_ARABIC,
            fontWeight: 700,
            fontSize: headingFontSize,
            color: PHOTONECT.paper,
            lineHeight: 1.18,
            textAlign: "right",
            direction: "rtl",
            letterSpacing: "-0.005em",
            maxWidth: CONTENT_WIDTH,
          }}
        >
          {words.map((w, i) => {
            const p = spring({
              frame: frame - (wordStart + i * WORD_STEP),
              fps,
              config: { damping: 12, stiffness: 180, mass: 0.7 },
            });
            return (
              <span
                key={i}
                style={{
                  display: "inline-block",
                  opacity: p,
                  transform: `translateY(${(1 - p) * 14}px) scale(${0.92 + p * 0.08})`,
                  marginLeft: 12,
                  willChange: "transform, opacity",
                }}
              >{w}</span>
            );
          })}
        </div>

        {/* ARABIC BODY */}
        {arabicBody && (
          <div
            style={{
              fontFamily: FONT_ARABIC,
              fontWeight: 500,
              fontSize: bodyFontSize,
              color: PHOTONECT.paper,
              opacity: interpolate(frame, [bodyRevealFrame, bodyRevealFrame + 22], [0, 0.92], {
                extrapolateLeft: "clamp",
                extrapolateRight: "clamp",
              }),
              transform: `translateY(${(1 - Math.min(1, Math.max(0, (frame - bodyRevealFrame) / 22))) * 12}px)`,
              lineHeight: 1.45,
              textAlign: "right",
              direction: "rtl",
              maxWidth: CONTENT_WIDTH,
            }}
          >{arabicBody}</div>
        )}

        {/* 3 STAT PILLS */}
        {supportingStats && supportingStats.length > 0 && (
          <div
            style={{
              display: "flex",
              flexDirection: "row-reverse",
              gap: 10,
              width: "100%",
              maxWidth: CONTENT_WIDTH,
              marginTop: "auto",
              opacity: interpolate(frame, [pillsRevealFrame, pillsRevealFrame + 30], [0, 1], {
                extrapolateLeft: "clamp",
                extrapolateRight: "clamp",
              }),
              transform: `translateY(${(1 - Math.min(1, Math.max(0, (frame - pillsRevealFrame) / 30))) * 12}px)`,
            }}
          >
            {supportingStats.slice(0, 3).map((s, i) => (
              <BeatStatPill
                key={i}
                label={s.label}
                value={s.value}
                accent={a}
                startFrame={pillsRevealFrame + i * 3}
                frame={frame}
              />
            ))}
          </div>
        )}
      </div>
    </AbsoluteFill>
  );
};

function animatedStat(value: string, frame: number, startFrame: number) {
  const { numPart, prefix, suffix } = parseStat(value);
  if (numPart == null) return value;
  const prog = Math.max(0, Math.min(1, (frame - startFrame) / 36));
  const ease = 1 - Math.pow(1 - prog, 3);
  const n = Math.round(numPart * ease);
  const hasDecimal = !Number.isInteger(numPart);
  const formatted = hasDecimal && n < 100 ? n.toFixed(1) : n.toLocaleString("en-US");
  return `${prefix}${formatted}${suffix}`;
}
