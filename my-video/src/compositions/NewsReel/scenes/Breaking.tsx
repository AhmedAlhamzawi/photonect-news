import React from "react";
import { AbsoluteFill, interpolate, useCurrentFrame, Easing, spring, useVideoConfig } from "remotion";
import { PHOTONECT } from "../../PhotonectBrandReel/brand";
import { FONT_ARABIC, FONT_LATIN } from "../../PhotonectBrandReel/fonts";
import { VideoBackdrop } from "../VideoBackdrop";
import { BREAKING_FRAMES } from "../schema";
import { CONTENT_PADDING, CONTENT_WIDTH } from "../safeArea";

type Props = {
  arabicKicker: string;
  arabicHeadline: string;
  englishSubhead: string;
  heroMedia: string;
  heroMediaType: "video" | "image";
};

/**
 * Breaking — V7 leap (2026-05-08).
 *
 * Cold-open redesign after watching 100 best news videos. The pattern from
 * BBC, Vice, Vox, Bloomberg, Reuters/NowThis is unanimous: withhold the
 * title for the first 1-2 seconds. Open on footage + audio only. Only after
 * the viewer has committed do you start layering text.
 *
 * Timing (BREAKING_FRAMES = 150 = 5s):
 *   0-30    (0.0-1.0s)  — hero image alone, darkened 65%, no text. Just look.
 *   30-90   (1.0-3.0s)  — small kicker chip slides into lower-left (was a giant
 *                          centered red badge in V6). Hero lifts to 90% brightness.
 *   60-115  (2.0-3.83s) — Arabic headline reveals via spring-in from below right,
 *                          lower-right of frame.
 *   100-150 (3.33-5.0s) — English subhead fades in beneath headline.
 *
 * Net: the centered red 🔴 عاجل badge that used to blare at frame 0 is gone.
 * Replaced with a quiet attribution-style chip in the lower-left and a
 * delayed-reveal headline. Hero image carries the first beat alone — exactly
 * what Vox/BBC do.
 */
export const Breaking: React.FC<Props> = ({
  arabicKicker,
  arabicHeadline,
  englishSubhead,
  heroMedia,
  heroMediaType,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Hero image brightness: starts at 65%, lifts to 100% over frames 0-30.
  // Trial 2 fix (2026-05-08): the original V7 lift (35→95%) stacked with the
  // vignette pulse below to render the t=2s frame near-black. Loosening the
  // bottom of the brightness ramp from 0.35 → 0.65 keeps the "delayed reveal"
  // mood without burying the hero entirely.
  const heroLift = interpolate(frame, [0, 30], [0.65, 1.0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.bezier(0.16, 1, 0.3, 1),
  });

  // Subtle slow zoom on the hero image for the first 90 frames (3s)
  const heroZoom = interpolate(frame, [0, 90], [1.04, 1.0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.bezier(0.16, 1, 0.3, 1),
  });

  // Kicker chip — slides in lower-left, frames 30-60
  const kickerReveal = spring({
    frame: frame - 30,
    fps,
    config: { damping: 16, stiffness: 110 },
  });

  // Headline — spring in from below right, frames 60-95
  const headlineReveal = spring({
    frame: frame - 60,
    fps,
    config: { damping: 18, stiffness: 120 },
  });

  // Subhead — fade in frames 100-130
  const subheadReveal = interpolate(frame, [100, 130], [0, 1], {
    easing: Easing.bezier(0.16, 1, 0.3, 1),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Vignette pulse over runtime — pulls eye to center after image is up.
  // Trial 2 fix: the V7 amplitude (0.4-0.7 multiply) was too aggressive and
  // combined with the brightness mask above to bury the hero. Toning down to
  // 0.18-0.32 — still creates the centerward pull but lets the image breathe.
  const vignettePulse = 0.18 + 0.14 * Math.sin(frame * 0.06);

  return (
    <AbsoluteFill>
      {/* Hero image — slow zoom, brightness ramp */}
      <AbsoluteFill style={{ transform: `scale(${heroZoom})` }}>
        <VideoBackdrop
          src={heroMedia}
          type={heroMediaType}
          accent={"#FF2D55"}
          intensity="hero"
          durationFrames={BREAKING_FRAMES}
        />
      </AbsoluteFill>

      {/* Brightness mask — darker at start, lifts as we move into the reel */}
      <AbsoluteFill
        style={{
          background: "#000",
          opacity: 1 - heroLift,
          pointerEvents: "none",
        }}
      />

      {/* Vignette pulse — pulls eye centerward */}
      <AbsoluteFill
        style={{
          background: `radial-gradient(ellipse at 50% 55%, transparent 35%, rgba(0,0,0,${vignettePulse}) 100%)`,
          mixBlendMode: "multiply",
          pointerEvents: "none",
        }}
      />

      {/* Kicker chip — small, lower-left, attribution style (V7 leap) */}
      <div
        style={{
          position: "absolute",
          left: 56,
          top: 156,
          opacity: kickerReveal,
          transform: `translateX(${(1 - kickerReveal) * -16}px)`,
          display: "flex",
          alignItems: "center",
          gap: 12,
          padding: "10px 18px 10px 14px",
          background: "rgba(255,45,85,0.92)",
          borderRadius: 4,
          boxShadow: "0 4px 16px rgba(255,45,85,0.4)",
        }}
      >
        <div
          style={{
            width: 8,
            height: 8,
            borderRadius: 99,
            background: "#fff",
            boxShadow: `0 0 ${4 + 6 * (0.5 + 0.5 * Math.sin(frame * 0.3))}px #fff`,
          }}
        />
        <div
          style={{
            fontFamily: FONT_ARABIC,
            fontWeight: 700,
            fontSize: 22,
            color: "#fff",
            letterSpacing: "0.08em",
          }}
        >
          {arabicKicker}
        </div>
      </div>

      {/* Headline + subhead block — anchored bottom-right of safe zone */}
      <AbsoluteFill
        style={{
          padding: CONTENT_PADDING,
          display: "flex",
          flexDirection: "column",
          justifyContent: "flex-end",
          alignItems: "flex-end",
          direction: "rtl",
        }}
      >
        {/* Giant Arabic headline */}
        <div
          style={{
            fontFamily: FONT_ARABIC,
            fontWeight: 800,
            fontSize: 92,
            color: PHOTONECT.paper,
            lineHeight: 1.18,
            textAlign: "right",
            direction: "rtl",
            maxWidth: CONTENT_WIDTH,
            letterSpacing: "-0.01em",
            opacity: headlineReveal,
            transform: `translateY(${(1 - headlineReveal) * 28}px)`,
            textShadow: `0 6px 28px ${PHOTONECT.ink}`,
          }}
        >
          {arabicHeadline}
        </div>

        {/* English subhead */}
        <div
          style={{
            fontFamily: FONT_LATIN,
            fontWeight: 600,
            fontSize: 32,
            color: PHOTONECT.signal,
            marginTop: 28,
            letterSpacing: "0.12em",
            textTransform: "uppercase",
            opacity: subheadReveal * 0.9,
            textAlign: "right",
          }}
        >
          {englishSubhead}
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
