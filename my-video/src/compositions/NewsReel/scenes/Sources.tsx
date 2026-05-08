import React from "react";
import { AbsoluteFill, interpolate, useCurrentFrame, Easing, spring, useVideoConfig } from "remotion";
import { PHOTONECT } from "../../PhotonectBrandReel/brand";
import { FONT_ARABIC, FONT_LATIN } from "../../PhotonectBrandReel/fonts";
import type { SourceProps } from "../schema";
import { LogoPhotonectInline } from "../../AINewsDaily/LogoPhotonect";
import { CONTENT_PADDING, CONTENT_WIDTH } from "../safeArea";
import { SOURCES_FRAMES } from "../schema";

type Props = {
  sources: SourceProps[];
  handle: string;
};

/**
 * Sources — V7 leap (2026-05-08).
 *
 * Adds a loop-hook outro to the last 24 frames (0.8s):
 *   - All Sources content fades out
 *   - Frame goes near-black with a single bottom-right kicker still visible
 *   - The very last 5 frames are pure 100% black (cold-cut to allow IG autoplay
 *     loop to land cleanly back at frame 0 of Breaking, which is also dark)
 *
 * Pattern from Bloomberg/Insider/BBC: closing rhymes with opening; cold-cut
 * never fade-out (a fade signals "this is over" — cold cut signals "play me again").
 */
export const Sources: React.FC<Props> = ({ sources, handle }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const titleReveal = spring({ frame, fps, config: { damping: 16 } });
  const handleReveal = spring({ frame: frame - 40, fps, config: { damping: 14 } });

  // Loop-hook outro: everything fades to black over the last 24 frames.
  // Sources duration is SOURCES_FRAMES (90); fade window is 66-90.
  const outroFade = interpolate(
    frame,
    [SOURCES_FRAMES - 24, SOURCES_FRAMES - 5],
    [1, 0],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" },
  );
  // Black overlay to enforce cold-cut darkness in the final 5 frames
  const blackOut = interpolate(
    frame,
    [SOURCES_FRAMES - 8, SOURCES_FRAMES - 5, SOURCES_FRAMES],
    [0, 1, 1],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" },
  );

  return (
    <AbsoluteFill
      style={{
        background: `radial-gradient(ellipse at 50% 45%, ${PHOTONECT.signal}16 0%, ${PHOTONECT.ink} 70%)`,
        opacity: outroFade,
      }}
    >
      <AbsoluteFill
        style={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
          gap: 36,
          padding: CONTENT_PADDING,
        }}
      >
        {/* Arabic label */}
        <div
          style={{
            display: "flex",
            alignItems: "center",
            gap: 18,
            opacity: titleReveal,
            transform: `translateY(${(1 - titleReveal) * 18}px)`,
          }}
        >
          <div style={{ width: 60, height: 2, background: PHOTONECT.signal }} />
          <div
            style={{
              fontFamily: FONT_ARABIC,
              fontWeight: 700,
              fontSize: 40,
              color: PHOTONECT.signal,
              letterSpacing: "0.02em",
            }}
          >
            المصادر
          </div>
          <div style={{ width: 60, height: 2, background: PHOTONECT.signal }} />
        </div>

        {/* Sources grid */}
        <div
          style={{
            display: "grid",
            gridTemplateColumns: "1fr 1fr",
            gap: 16,
            maxWidth: CONTENT_WIDTH,
            width: "100%",
          }}
        >
          {sources.map((s, i) => {
            const start = 8 + i * 4;
            const p = interpolate(frame, [start, start + 14], [0, 1], {
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
                  border: `1px solid ${PHOTONECT.signal}55`,
                  borderRadius: 6,
                  opacity: p,
                  transform: `translateY(${(1 - p) * 18}px)`,
                  display: "flex",
                  flexDirection: "column",
                  gap: 4,
                }}
              >
                <div
                  style={{
                    fontFamily: FONT_LATIN,
                    fontWeight: 800,
                    fontSize: 24,
                    color: PHOTONECT.paper,
                    letterSpacing: "0.01em",
                  }}
                >
                  {s.name}
                </div>
                <div
                  style={{
                    fontFamily: FONT_LATIN,
                    fontWeight: 500,
                    fontSize: 18,
                    color: PHOTONECT.signal,
                    opacity: 0.8,
                    letterSpacing: "0.05em",
                  }}
                >
                  {s.domain}
                </div>
              </div>
            );
          })}
        </div>

        {/* CTA block */}
        <div
          style={{
            marginTop: 28,
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            gap: 10,
            opacity: handleReveal,
            transform: `translateY(${(1 - handleReveal) * 14}px)`,
          }}
        >
          <LogoPhotonectInline size={54} variant="dark" />
          <div
            style={{
              fontFamily: FONT_LATIN,
              fontWeight: 900,
              fontSize: 34,
              color: PHOTONECT.paper,
              letterSpacing: "0.02em",
            }}
          >
            {handle}
          </div>
          <div
            style={{
              fontFamily: FONT_ARABIC,
              fontWeight: 500,
              fontSize: 22,
              color: PHOTONECT.signal,
              opacity: 0.9,
              marginTop: 2,
            }}
          >
            أخبار العالم يومياً — بالعربية
          </div>
        </div>
      </AbsoluteFill>

      {/* Loop-hook black-out overlay — outside the outro-fade wrapper so it
          can fully cover even when the wrapper has already started fading. */}
      <AbsoluteFill
        style={{
          background: "#000",
          opacity: blackOut,
          pointerEvents: "none",
        }}
      />
    </AbsoluteFill>
  );
};
