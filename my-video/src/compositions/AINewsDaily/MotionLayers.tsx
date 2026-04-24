import React, { useMemo } from "react";
import { AbsoluteFill, interpolate, useCurrentFrame, Easing, random, Img } from "remotion";
import { PHOTONECT } from "../PhotonectBrandReel/brand";
import { FONT_LATIN, FONT_ARABIC } from "../PhotonectBrandReel/fonts";
import { LogoPhotonectInline } from "./LogoPhotonect";

// Photo backdrop — image behind scene content with slow Ken Burns + dark gradient overlay + scanlines
type PhotoBackdropProps = {
  src: string;
  accent: string;
  mode?: "hero" | "classified" | "grid"; // style variant
  zoomFrom?: number;
  zoomTo?: number;
  panX?: [number, number];
};
export const PhotoBackdrop: React.FC<PhotoBackdropProps> = ({
  src,
  accent,
  mode = "hero",
  zoomFrom = 1.08,
  zoomTo = 1.18,
  panX = [0, -4],
}) => {
  const frame = useCurrentFrame();
  const zoom = interpolate(frame, [0, 300], [zoomFrom, zoomTo], {
    easing: Easing.linear,
    extrapolateRight: "clamp",
  });
  const px = interpolate(frame, [0, 300], panX, {
    easing: Easing.linear,
    extrapolateRight: "clamp",
  });
  const reveal = interpolate(frame, [0, 20], [0, 1], {
    easing: Easing.bezier(0.16, 1, 0.3, 1),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const overlay =
    mode === "classified"
      ? `linear-gradient(180deg, ${PHOTONECT.ink}99 0%, ${PHOTONECT.ink}70 40%, ${PHOTONECT.ink}BB 100%)`
      : mode === "grid"
      ? `linear-gradient(180deg, ${PHOTONECT.ink}88 0%, ${PHOTONECT.ink}55 50%, ${PHOTONECT.ink}AA 100%)`
      : `linear-gradient(180deg, ${PHOTONECT.ink}77 0%, ${PHOTONECT.ink}40 45%, ${PHOTONECT.ink}99 100%)`;

  return (
    <AbsoluteFill style={{ overflow: "hidden", opacity: reveal }}>
      <AbsoluteFill
        style={{
          transform: `scale(${zoom}) translateX(${px}%)`,
          filter: mode === "classified" ? "grayscale(1) contrast(1.15)" : "saturate(0.85) contrast(1.05)",
        }}
      >
        <Img
          src={src}
          style={{
            width: "100%",
            height: "100%",
            objectFit: "cover",
          }}
        />
      </AbsoluteFill>
      {/* Dark gradient overlay for text legibility */}
      <AbsoluteFill style={{ background: overlay }} />
      {/* Accent frame */}
      <AbsoluteFill
        style={{
          pointerEvents: "none",
          boxShadow: `inset 0 0 0 3px ${accent}33, inset 0 0 60px ${PHOTONECT.ink}`,
        }}
      />
      {/* Scanlines for classified mode */}
      {mode === "classified" && (
        <AbsoluteFill
          style={{
            backgroundImage: `repeating-linear-gradient(0deg, ${accent}08 0, ${accent}08 1px, transparent 1px, transparent 4px)`,
            mixBlendMode: "screen",
            pointerEvents: "none",
          }}
        />
      )}
    </AbsoluteFill>
  );
};

// BrandMark — typographic brand badge. Honest alternative to a portrait photo.
// Renders initials or short name in Inter 900 inside a brand-colored circle.
type BrandMarkProps = {
  name: string; // full name for label rendering
  initials?: string; // override (e.g. "A" for Anthropic, "OAI" for OpenAI)
  brandColor: string;
  size: number;
  textColor?: string;
};
export const BrandMark: React.FC<BrandMarkProps> = ({
  name,
  initials,
  brandColor,
  size,
  textColor = "#FFFFFF",
}) => {
  const initialText = initials ?? name.charAt(0);
  return (
    <div
      style={{
        width: size,
        height: size,
        borderRadius: size / 2,
        background: brandColor,
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        fontFamily: FONT_LATIN,
        fontWeight: 900,
        fontSize: size * (initialText.length > 2 ? 0.32 : 0.5),
        color: textColor,
        letterSpacing: "-0.02em",
        boxShadow: `0 0 ${size * 0.3}px ${brandColor}66, inset 0 -${size * 0.05}px ${size * 0.1}px rgba(0,0,0,0.25)`,
        border: `3px solid ${textColor}`,
        flexShrink: 0,
      }}
    >
      {initialText}
    </div>
  );
};

// Small framed image — for inline use (race bars, alliance nodes)
type PhotoChipProps = {
  src: string;
  size: number;
  accent: string;
  rounded?: boolean;
};
export const PhotoChip: React.FC<PhotoChipProps> = ({ src, size, accent, rounded = false }) => {
  return (
    <div
      style={{
        width: size,
        height: size,
        borderRadius: rounded ? size / 2 : 6,
        overflow: "hidden",
        border: `2px solid ${accent}`,
        boxShadow: `0 0 24px ${accent}44`,
        flexShrink: 0,
        background: PHOTONECT.ink,
      }}
    >
      <Img
        src={src}
        style={{ width: "100%", height: "100%", objectFit: "cover" }}
      />
    </div>
  );
};

// Animated dot grid — pulses softly and drifts. Runs for the whole composition.
export const DotGrid: React.FC = () => {
  const frame = useCurrentFrame();
  const cols = 18;
  const rows = 32;
  const dots = useMemo(() => {
    const arr: { x: number; y: number; phase: number }[] = [];
    for (let y = 0; y < rows; y++) {
      for (let x = 0; x < cols; x++) {
        arr.push({
          x: x / (cols - 1),
          y: y / (rows - 1),
          phase: random(`dot-${x}-${y}`) * 6.28,
        });
      }
    }
    return arr;
  }, []);

  return (
    <AbsoluteFill style={{ pointerEvents: "none" }}>
      {dots.map((d, i) => {
        const pulse = 0.15 + 0.35 * (0.5 + 0.5 * Math.sin(frame * 0.04 + d.phase));
        return (
          <div
            key={i}
            style={{
              position: "absolute",
              left: `${d.x * 100}%`,
              top: `${d.y * 100}%`,
              width: 4,
              height: 4,
              borderRadius: 99,
              background: PHOTONECT.signal,
              opacity: pulse * 0.35,
              transform: "translate(-50%, -50%)",
            }}
          />
        );
      })}
    </AbsoluteFill>
  );
};

// Diagonal scanning beam that sweeps across every ~6s
export const ScanBeam: React.FC = () => {
  const frame = useCurrentFrame();
  const period = 180; // 6s at 30fps
  const t = (frame % period) / period;
  const y = interpolate(t, [0, 1], [-30, 130]);
  return (
    <AbsoluteFill style={{ pointerEvents: "none" }}>
      <div
        style={{
          position: "absolute",
          left: -100,
          right: -100,
          top: `${y}%`,
          height: 120,
          background: `linear-gradient(to bottom, transparent, ${PHOTONECT.signal}11, transparent)`,
          transform: "rotate(-8deg)",
        }}
      />
    </AbsoluteFill>
  );
};

// Bottom scrolling headlines ticker — bilingual (interleaves EN and AR)
type TickerProps = { headlines: string[]; arabicHeadlines?: string[] };
export const BottomTicker: React.FC<TickerProps> = ({ headlines, arabicHeadlines }) => {
  const frame = useCurrentFrame();
  const accent = PHOTONECT.signal;
  const paper = PHOTONECT.paper;

  // Arabic-only ticker — cleaner, no language switching
  const parts: { text: string; lang: "en" | "ar" }[] = [];
  const source = arabicHeadlines && arabicHeadlines.length > 0 ? arabicHeadlines : headlines;
  const lang = arabicHeadlines && arabicHeadlines.length > 0 ? "ar" : "en";
  for (let i = 0; i < source.length; i++) {
    if (source[i]) parts.push({ text: source[i], lang: lang as "en" | "ar" });
  }

  // Estimate scroll width
  const approxW = parts.reduce((acc, p) => acc + p.text.length * 19 + 80, 0);
  const loop = (frame * 2.2) % approxW;

  return (
    <div
      style={{
        position: "absolute",
        bottom: 40,
        left: 0,
        right: 0,
        height: 70,
        display: "flex",
        alignItems: "center",
        background: `linear-gradient(90deg, ${PHOTONECT.ash} 0%, ${PHOTONECT.ash}EE 10%, ${PHOTONECT.ash}EE 90%, ${PHOTONECT.ash} 100%)`,
        borderTop: `2px solid ${accent}`,
        borderBottom: `2px solid ${accent}`,
        overflow: "hidden",
      }}
    >
      <div
        style={{
          position: "absolute",
          left: 20,
          top: 0,
          bottom: 0,
          width: 110,
          background: accent,
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          fontFamily: FONT_LATIN,
          fontWeight: 900,
          fontSize: 26,
          color: PHOTONECT.ink,
          letterSpacing: "0.1em",
          zIndex: 2,
          boxShadow: `0 0 20px ${accent}88`,
        }}
      >
        LIVE
      </div>
      <div
        style={{
          position: "absolute",
          left: 150,
          right: 0,
          top: 0,
          bottom: 0,
          overflow: "hidden",
        }}
      >
        <div
          style={{
            position: "absolute",
            left: -loop,
            top: 0,
            bottom: 0,
            display: "flex",
            alignItems: "center",
            whiteSpace: "nowrap",
            fontSize: 28,
            color: paper,
          }}
        >
          {[0, 1].map((loopIdx) => (
            <React.Fragment key={loopIdx}>
              {parts.map((p, i) => (
                <React.Fragment key={`${loopIdx}-${i}`}>
                  <span
                    style={{
                      fontFamily: p.lang === "ar" ? FONT_ARABIC : FONT_LATIN,
                      fontWeight: p.lang === "ar" ? 700 : 600,
                      letterSpacing: p.lang === "ar" ? 0 : "0.03em",
                      color: p.lang === "ar" ? accent : paper,
                      direction: p.lang === "ar" ? "rtl" : "ltr",
                    }}
                  >
                    {p.text}
                  </span>
                  <span style={{ color: accent, padding: "0 24px", fontSize: 22 }}>◆</span>
                </React.Fragment>
              ))}
            </React.Fragment>
          ))}
        </div>
      </div>
    </div>
  );
};

// Top strip: LIVE badge + PHOTONECT logo + date, persistent.
// Positioned inside the IG/TikTok platform-safe zone — anything above y=280 is
// occluded by the status bar / back button / search overlay on both platforms.
type TopStripProps = { dateLabel: string; arabicDateLabel: string; showName?: string; showColor?: string };
export const TopStrip: React.FC<TopStripProps> = ({ dateLabel, arabicDateLabel, showName = "AI NEWS", showColor }) => {
  const frame = useCurrentFrame();
  const pulse = 0.6 + 0.4 * Math.sin(frame * 0.2);
  return (
    <div
      style={{
        position: "absolute",
        top: 280,
        left: 120,
        right: 160,
        height: 64,
        display: "flex",
        alignItems: "center",
        justifyContent: "space-between",
        padding: "0 18px",
        background: `${PHOTONECT.ash}DD`,
        borderTop: `2px solid ${PHOTONECT.signal}`,
        borderBottom: `2px solid ${PHOTONECT.signal}`,
        backdropFilter: "blur(6px)",
        borderRadius: 6,
      }}
    >
      {/* Left: LIVE pill (moved from the deleted BottomTicker) */}
      <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
        <div
          style={{
            width: 12,
            height: 12,
            borderRadius: 99,
            background: "#FF3B30",
            opacity: pulse,
            boxShadow: `0 0 ${8 + pulse * 12}px #FF3B30`,
          }}
        />
        <div
          style={{
            fontFamily: FONT_LATIN,
            fontWeight: 900,
            fontSize: 20,
            color: "#FF3B30",
            letterSpacing: "0.18em",
          }}
        >
          LIVE
        </div>
      </div>
      {/* Center: PHOTONECT + show name */}
      <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
        <LogoPhotonectInline size={22} variant="dark" />
        <div
          style={{
            fontFamily: FONT_LATIN,
            fontWeight: 800,
            fontSize: 20,
            color: showColor ?? PHOTONECT.signal,
            letterSpacing: "0.2em",
          }}
        >
          {showName}
        </div>
      </div>
      {/* Right: date (stacked EN over AR) */}
      <div
        style={{
          fontFamily: FONT_LATIN,
          fontWeight: 700,
          fontSize: 18,
          color: PHOTONECT.signal,
          letterSpacing: "0.1em",
          textAlign: "right",
          lineHeight: 1,
        }}
      >
        {dateLabel}
        <div style={{ fontSize: 14, color: PHOTONECT.paper, opacity: 0.75, marginTop: 3 }}>
          {arabicDateLabel}
        </div>
      </div>
    </div>
  );
};

// Shared supporting-stats row: up to 4 stats as mini-cards that cascade in
type SupportingStatsProps = {
  stats: { label: string; value: string }[];
  startAtSeconds: number; // when to begin the cascade
  color: string;
  paper: string;
};
export const SupportingStats: React.FC<SupportingStatsProps> = ({
  stats,
  startAtSeconds,
  color,
  paper,
}) => {
  const frame = useCurrentFrame();
  const fps = 30;
  return (
    <div
      style={{
        display: "grid",
        gridTemplateColumns: stats.length >= 3 ? "1fr 1fr" : "1fr",
        gap: 18,
        width: "100%",
      }}
    >
      {stats.map((s, i) => {
        const start = (startAtSeconds + i * 0.15) * fps;
        const p = interpolate(frame, [start, start + 0.6 * fps], [0, 1], {
          easing: Easing.bezier(0.16, 1, 0.3, 1),
          extrapolateLeft: "clamp",
          extrapolateRight: "clamp",
        });
        return (
          <div
            key={i}
            style={{
              padding: "18px 22px",
              background: "rgba(255,255,255,0.04)",
              border: `1px solid ${color}44`,
              borderLeft: `4px solid ${color}`,
              borderRadius: 6,
              opacity: p,
              transform: `translateX(${(1 - p) * -24}px)`,
            }}
          >
            <div
              style={{
                fontFamily: FONT_LATIN,
                fontWeight: 700,
                fontSize: 22,
                color: paper,
                opacity: 0.65,
                letterSpacing: "0.1em",
                textTransform: "uppercase",
              }}
            >
              {s.label}
            </div>
            <div
              style={{
                fontFamily: FONT_LATIN,
                fontWeight: 900,
                fontSize: 42,
                color: color,
                lineHeight: 1.05,
                marginTop: 4,
                letterSpacing: "-0.02em",
              }}
            >
              {s.value}
            </div>
          </div>
        );
      })}
    </div>
  );
};

// Shared "context line" — italicized "why this matters" that appears later in a scene
type ContextLineProps = {
  text: string;
  arabic?: string;
  startAtSeconds: number;
  paper: string;
  accent: string;
};
export const ContextLine: React.FC<ContextLineProps> = ({
  text,
  arabic,
  startAtSeconds,
  paper,
  accent,
}) => {
  const frame = useCurrentFrame();
  const fps = 30;
  const p = interpolate(
    frame,
    [startAtSeconds * fps, (startAtSeconds + 0.7) * fps],
    [0, 1],
    {
      easing: Easing.bezier(0.16, 1, 0.3, 1),
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    },
  );
  return (
    <div style={{ opacity: p, transform: `translateY(${(1 - p) * 14}px)` }}>
      <div
        style={{
          display: "flex",
          alignItems: "center",
          gap: 14,
          marginBottom: 8,
          direction: "rtl",
        }}
      >
        <div style={{ width: 36, height: 3, background: accent, borderRadius: 2 }} />
        <div
          style={{
            fontFamily: FONT_ARABIC,
            fontWeight: 700,
            fontSize: 22,
            color: accent,
            letterSpacing: "0.02em",
          }}
        >
          لماذا يهم؟
        </div>
      </div>
      {arabic ? (
        <div
          style={{
            fontFamily: FONT_ARABIC,
            fontWeight: 500,
            fontSize: 36,
            color: paper,
            lineHeight: 1.5,
            maxWidth: 960,
            direction: "rtl",
            opacity: 0.95,
          }}
        >
          {arabic}
        </div>
      ) : (
        <div
          style={{
            fontFamily: FONT_LATIN,
            fontStyle: "italic",
            fontWeight: 500,
            fontSize: 34,
            color: paper,
            lineHeight: 1.3,
            maxWidth: 920,
            opacity: 0.9,
          }}
        >
          {text}
        </div>
      )}
    </div>
  );
};

// Arabic kicker — small RTL label paired with Latin kicker
type ArabicKickerProps = {
  text: string;
  color: string;
  opacity: number;
};
export const ArabicKicker: React.FC<ArabicKickerProps> = ({ text, color, opacity }) => {
  if (!text) return null;
  return (
    <div
      style={{
        fontFamily: FONT_ARABIC,
        fontWeight: 700,
        fontSize: 30,
        color,
        direction: "rtl",
        opacity: opacity * 0.88,
        letterSpacing: "0.02em",
        lineHeight: 1.25,
      }}
    >
      {text}
    </div>
  );
};
