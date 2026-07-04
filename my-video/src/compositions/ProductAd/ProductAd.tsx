import React from "react";
import {
  AbsoluteFill,
  OffthreadVideo,
  Audio,
  Img,
  Sequence,
  staticFile,
  interpolate,
  useCurrentFrame,
  useVideoConfig,
  Easing,
} from "remotion";
import { loadFont } from "@remotion/google-fonts/Cairo";
import type { ProductAdProps } from "./schema";

const { fontFamily } = loadFont();
const EASE = Easing.bezier(0.16, 1, 0.3, 1); // crisp UI entrance

// A caption block, timed locally inside its own <Sequence>.
const Beat: React.FC<{ durF: number; children: React.ReactNode }> = ({ durF, children }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const enter = interpolate(frame, [0, 0.45 * fps], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: EASE });
  const exit = interpolate(frame, [durF - 0.35 * fps, durF], [1, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  const opacity = enter * exit;
  const y = interpolate(enter, [0, 1], [46, 0]);
  return (
    <div style={{ opacity, transform: `translateY(${y}px)`, width: "100%", textAlign: "center", direction: "rtl", fontFamily }}>
      {children}
    </div>
  );
};

export const ProductAd: React.FC<ProductAdProps> = (p) => {
  const { fps, durationInFrames } = useVideoConfig();
  const frame = useCurrentFrame();

  // gentle push-in on the footage for life
  const bgScale = interpolate(frame, [0, durationInFrames], [1.06, 1.16]);
  // logo bug fade-in
  const bugOpacity = interpolate(frame, [6, 24], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });

  const capWrap: React.CSSProperties = {
    position: "absolute", left: 0, right: 0, bottom: 210, padding: "0 70px",
  };
  const hookStyle: React.CSSProperties = { color: "#fff", fontWeight: 800, fontSize: 82, lineHeight: 1.15, textShadow: "0 6px 30px rgba(0,0,0,0.7)" };
  const benefitStyle: React.CSSProperties = { color: "#fff", fontWeight: 700, fontSize: 66, lineHeight: 1.2, textShadow: "0 6px 30px rgba(0,0,0,0.7)" };

  return (
    <AbsoluteFill style={{ backgroundColor: p.charcoal }}>
      {/* real product footage */}
      <AbsoluteFill style={{ transform: `scale(${bgScale})` }}>
        <OffthreadVideo
          src={staticFile(p.clip)}
          startFrom={Math.round(p.clipStartSec * fps)}
          muted
          style={{ width: "100%", height: "100%", objectFit: "cover" }}
        />
      </AbsoluteFill>

      {/* legibility gradients: top for bug, big bottom for captions */}
      <AbsoluteFill style={{ background: `linear-gradient(to bottom, ${p.charcoal}CC 0%, transparent 22%, transparent 55%, ${p.charcoal}F2 100%)` }} />

      {/* logo bug */}
      <div style={{ position: "absolute", top: 60, left: 56, opacity: bugOpacity, display: "flex", alignItems: "center", gap: 16 }}>
        <Img src={staticFile(p.brandIcon)} style={{ width: 96, height: 96, borderRadius: 22 }} />
      </div>

      {/* Beat 1 — hook */}
      <Sequence from={0} durationInFrames={Math.round(4.6 * fps)} premountFor={fps}>
        <div style={capWrap}><Beat durF={Math.round(4.6 * fps)}><div style={hookStyle}>{p.hook}</div></Beat></div>
      </Sequence>

      {/* Beat 2 — benefit */}
      <Sequence from={Math.round(4.6 * fps)} durationInFrames={Math.round(4.4 * fps)} premountFor={fps}>
        <div style={capWrap}><Beat durF={Math.round(4.4 * fps)}><div style={benefitStyle}>{p.benefit}</div></Beat></div>
      </Sequence>

      {/* Beat 3 — price pill */}
      <Sequence from={Math.round(9 * fps)} durationInFrames={Math.round(4.5 * fps)} premountFor={fps}>
        <div style={capWrap}>
          <Beat durF={Math.round(4.5 * fps)}>
            <div style={{ display: "inline-flex", flexDirection: "column", alignItems: "center", gap: 18 }}>
              <div style={{ background: p.teal, color: "#08120F", fontWeight: 900, fontSize: 96, padding: "14px 54px", borderRadius: 28, boxShadow: "0 12px 40px rgba(31,252,193,0.35)" }}>
                {p.price} <span style={{ fontSize: 46, fontWeight: 800 }}>{p.priceUnit}</span>
              </div>
              <div style={{ color: "#fff", fontWeight: 700, fontSize: 48 }}>{p.priceNote}</div>
            </div>
          </Beat>
        </div>
      </Sequence>

      {/* Beat 4 — CTA */}
      <Sequence from={Math.round(13.5 * fps)} durationInFrames={Math.round(4.5 * fps)} premountFor={fps}>
        <div style={capWrap}>
          <Beat durF={Math.round(4.5 * fps)}>
            <div style={{ display: "inline-flex", flexDirection: "column", alignItems: "center", gap: 16 }}>
              <div style={{ color: p.teal, fontWeight: 900, fontSize: 92, textShadow: "0 6px 30px rgba(0,0,0,0.7)" }}>{p.cta}</div>
              <div style={{ color: "#fff", fontWeight: 700, fontSize: 50 }}>{p.ctaNote}</div>
            </div>
          </Beat>
        </div>
      </Sequence>

      {p.audioBed ? <Audio src={staticFile(p.audioBed)} volume={p.bedVolume} /> : null}
    </AbsoluteFill>
  );
};
