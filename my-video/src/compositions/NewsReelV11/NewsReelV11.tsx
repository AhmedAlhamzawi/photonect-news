import React from "react";
import {
  AbsoluteFill,
  Audio,
  Img,
  Sequence,
  staticFile,
  interpolate,
  useCurrentFrame,
  useVideoConfig,
  Easing,
} from "remotion";
import { FONT_ARABIC, FONT_LATIN } from "../PhotonectBrandReel/fonts";
import { GrainOverlay, Vignette } from "../PhotonectBrandReel/GrainOverlay";
import {
  NewsReelV11Props,
  V11_ENDCARD_FRAMES,
} from "./schema";

const C = {
  ink: "#08080C",
  yellow: "#FFC217",
  red: "#D72638",
  paper: "#F6F6F1",
};

// ── One kinetic shot: hard-cut Ken Burns crop of a still ─────────────────────
const Shot: React.FC<{
  img: string;
  durationF: number;
  fromScale: number;
  toScale: number;
  fromX: number;
  fromY: number;
  toX: number;
  toY: number;
}> = ({ img, durationF, fromScale, toScale, fromX, fromY, toX, toY }) => {
  const frame = useCurrentFrame();
  const t = interpolate(frame, [0, durationF], [0, 1], {
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.quad),
  });
  const scale = fromScale + (toScale - fromScale) * t;
  const x = (fromX + (toX - fromX) * t) * 60; // px pan range
  const y = (fromY + (toY - fromY) * t) * 60;
  // 4-frame punch-in at shot start = a visible "cut" energy even on the same image
  const punch = interpolate(frame, [0, 4], [1.035, 1], {
    extrapolateRight: "clamp",
  });
  return (
    <AbsoluteFill style={{ overflow: "hidden", backgroundColor: C.ink }}>
      <Img
        src={staticFile(img)}
        style={{
          width: "100%",
          height: "100%",
          objectFit: "cover",
          transform: `scale(${scale * punch}) translate(${x}px, ${y}px)`,
        }}
      />
    </AbsoluteFill>
  );
};

// ── Karaoke captions: active word glows yellow, synced to VO ─────────────────
const Karaoke: React.FC<{ props: NewsReelV11Props }> = ({ props }) => {
  const frame = useCurrentFrame();
  const line = props.lines.find((l) => frame >= l.startF && frame < l.endF + 6);
  if (!line) return null;
  const appear = interpolate(frame, [line.startF, line.startF + 5], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  return (
    <div
      style={{
        position: "absolute",
        bottom: 300,
        left: 40,
        right: 40,
        textAlign: "center",
        direction: "rtl",
        opacity: appear,
        transform: `translateY(${(1 - appear) * 14}px)`,
      }}
    >
      <div
        style={{
          display: "inline-block",
          background: "rgba(8,8,12,0.55)",
          borderRadius: 18,
          padding: "18px 26px",
          backdropFilter: "blur(4px)",
        }}
      >
        {line.words.map((w, i) => {
          const active = frame >= w.startF && frame < w.endF + 2;
          const past = frame >= w.endF + 2;
          return (
            <span
              key={i}
              style={{
                fontFamily: FONT_ARABIC,
                fontWeight: 800,
                fontSize: 58,
                lineHeight: 1.5,
                margin: "0 7px",
                color: active ? C.yellow : past ? C.paper : "rgba(246,246,241,0.55)",
                textShadow: active
                  ? `0 0 26px ${C.yellow}88, 0 3px 16px rgba(0,0,0,0.9)`
                  : "0 3px 16px rgba(0,0,0,0.9)",
                display: "inline-block",
                transform: active ? "scale(1.08)" : "scale(1)",
              }}
            >
              {w.word}
            </span>
          );
        })}
      </div>
    </div>
  );
};

// ── Hook headline: kinetic text that lands in the first half-second ──────────
const HookHeadline: React.FC<{ text: string }> = ({ text }) => {
  const frame = useCurrentFrame();
  const HOLD = 80; // ~2.7s then hand off to captions
  const inT = interpolate(frame, [3, 14], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.back(1.6)),
  });
  const outT = interpolate(frame, [HOLD, HOLD + 12], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  if (frame > HOLD + 14) return null;
  return (
    <div
      style={{
        position: "absolute",
        top: 210,
        left: 44,
        right: 44,
        textAlign: "center",
        direction: "rtl",
        opacity: inT * outT,
        transform: `scale(${0.86 + inT * 0.14})`,
      }}
    >
      <div
        style={{
          fontFamily: FONT_ARABIC,
          fontWeight: 900,
          fontSize: 78,
          lineHeight: 1.32,
          color: C.paper,
          textShadow: "0 4px 30px rgba(0,0,0,0.95)",
        }}
      >
        {text}
      </div>
      <div
        style={{
          width: 130 * inT,
          height: 8,
          background: C.yellow,
          borderRadius: 4,
          margin: "18px auto 0",
        }}
      />
    </div>
  );
};

// ── Stat pop: number card synced to the word being spoken ────────────────────
const StatPop: React.FC<{ value: string; labelArabic: string; holdFrames: number }> = ({
  value,
  labelArabic,
  holdFrames,
}) => {
  const frame = useCurrentFrame();
  const inT = interpolate(frame, [0, 8], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.back(2)),
  });
  const outT = interpolate(frame, [holdFrames - 10, holdFrames], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  return (
    <div
      style={{
        position: "absolute",
        top: 430,
        left: 0,
        right: 0,
        display: "flex",
        justifyContent: "center",
        opacity: inT * outT,
        transform: `scale(${0.8 + inT * 0.2})`,
      }}
    >
      <div
        style={{
          background: "rgba(8,8,12,0.78)",
          border: `2.5px solid ${C.yellow}`,
          borderRadius: 20,
          padding: "20px 40px",
          textAlign: "center",
          boxShadow: `0 0 44px ${C.yellow}44`,
        }}
      >
        <div
          style={{
            fontFamily: FONT_LATIN,
            fontWeight: 900,
            fontSize: 92,
            color: C.yellow,
            lineHeight: 1,
            direction: "ltr",
          }}
        >
          {value}
        </div>
        <div
          style={{
            fontFamily: FONT_ARABIC,
            fontWeight: 700,
            fontSize: 30,
            color: C.paper,
            marginTop: 8,
            direction: "rtl",
          }}
        >
          {labelArabic}
        </div>
      </div>
    </div>
  );
};

// ── End card: the open question + brand sting ────────────────────────────────
const EndCard: React.FC<{ props: NewsReelV11Props }> = ({ props }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const inT = interpolate(frame, [0, 12], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  });
  const pulse = 0.6 + 0.4 * Math.abs(Math.sin((frame / fps) * Math.PI * 1.6));
  return (
    <AbsoluteFill>
      <AbsoluteFill style={{ background: `rgba(8,8,12,${0.82 * inT})` }} />
      <div
        style={{
          position: "absolute",
          top: 0,
          bottom: 0,
          left: 60,
          right: 60,
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
          gap: 40,
          opacity: inT,
        }}
      >
        <div
          style={{
            fontFamily: FONT_ARABIC,
            fontWeight: 900,
            fontSize: 66,
            lineHeight: 1.45,
            color: C.paper,
            textAlign: "center",
            direction: "rtl",
          }}
        >
          {props.endQuestion}
        </div>
        <div
          style={{
            fontFamily: FONT_ARABIC,
            fontWeight: 700,
            fontSize: 32,
            color: C.yellow,
            direction: "rtl",
          }}
        >
          شاركنا رأيك بالتعليقات 👇
        </div>
        <div style={{ display: "flex", alignItems: "center", gap: 14, marginTop: 10 }}>
          <div
            style={{
              width: 15,
              height: 15,
              borderRadius: 8,
              background: C.red,
              boxShadow: `0 0 ${8 + pulse * 14}px ${C.red}`,
              opacity: pulse,
            }}
          />
          <div
            style={{
              fontFamily: FONT_LATIN,
              fontWeight: 900,
              fontSize: 34,
              letterSpacing: 3,
              color: C.paper,
            }}
          >
            PHOTONECT
          </div>
          <div
            style={{
              fontFamily: FONT_LATIN,
              fontWeight: 600,
              fontSize: 24,
              color: "rgba(246,246,241,0.65)",
            }}
          >
            {props.handle}
          </div>
        </div>
        {props.sourcesLine ? (
          <div
            style={{
              fontFamily: FONT_ARABIC,
              fontWeight: 500,
              fontSize: 22,
              color: "rgba(246,246,241,0.5)",
              direction: "rtl",
            }}
          >
            {props.sourcesLine}
          </div>
        ) : null}
      </div>
    </AbsoluteFill>
  );
};

// ── Main ─────────────────────────────────────────────────────────────────────
export const NewsReelV11: React.FC<NewsReelV11Props> = (props) => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  const endStart = props.totalFrames - V11_ENDCARD_FRAMES;
  const pulse = 0.55 + 0.45 * Math.abs(Math.sin(frame / 13));

  return (
    <AbsoluteFill style={{ backgroundColor: C.ink }}>
      {/* VO — the spine. Starts at frame 0, full volume. */}
      <Audio src={staticFile(props.vo)} />
      {props.audioBed ? (
        <Audio
          src={staticFile(props.audioBed)}
          loop
          volume={(f) =>
            interpolate(
              f,
              [0, 15, endStart, endStart + 12, durationInFrames - 10, durationInFrames],
              [0, props.bedVolume, props.bedVolume, Math.min(0.5, props.bedVolume * 2.4), Math.min(0.5, props.bedVolume * 2.4), 0],
              { extrapolateLeft: "clamp", extrapolateRight: "clamp" },
            )
          }
        />
      ) : null}

      {/* kinetic shots — hard cuts on word boundaries */}
      {props.shots.map((s, i) => (
        <Sequence key={i} from={s.startF} durationInFrames={s.durationF} name={`shot-${i}`}>
          <Shot
            img={s.img}
            durationF={s.durationF}
            fromScale={s.fromScale}
            toScale={s.toScale}
            fromX={s.fromX}
            fromY={s.fromY}
            toX={s.toX}
            toY={s.toY}
          />
        </Sequence>
      ))}

      {/* soft legibility scrim, bottom third */}
      <div
        style={{
          position: "absolute",
          bottom: 0,
          left: 0,
          right: 0,
          height: "42%",
          background:
            "linear-gradient(to top, rgba(8,8,12,0.75) 0%, rgba(8,8,12,0.35) 55%, rgba(8,8,12,0) 100%)",
        }}
      />

      {/* brand chip — small, persistent, top-right (RTL-natural) */}
      <div
        style={{
          position: "absolute",
          top: 40,
          right: 44,
          display: "flex",
          alignItems: "center",
          gap: 10,
          background: "rgba(8,8,12,0.6)",
          borderRadius: 12,
          padding: "8px 16px",
          zIndex: 40,
        }}
      >
        <div
          style={{
            width: 11,
            height: 11,
            borderRadius: 6,
            background: C.red,
            boxShadow: `0 0 ${6 + pulse * 9}px ${C.red}`,
            opacity: pulse,
          }}
        />
        <span style={{ fontFamily: FONT_LATIN, fontWeight: 900, fontSize: 21, letterSpacing: 2, color: C.paper }}>
          PHOTONECT
        </span>
        <span style={{ fontFamily: FONT_ARABIC, fontWeight: 800, fontSize: 22, color: C.yellow }}>
          {props.kicker}
        </span>
      </div>

      {/* hook headline (first ~3s) */}
      <HookHeadline text={props.hookHeadline} />

      {/* stat pops, word-synced */}
      {props.statPops.map((sp, i) => (
        <Sequence key={`sp-${i}`} from={sp.atFrame} durationInFrames={sp.holdFrames} name={`stat-${i}`}>
          <StatPop value={sp.value} labelArabic={sp.labelArabic} holdFrames={sp.holdFrames} />
        </Sequence>
      ))}

      {/* karaoke captions (hidden during end card) */}
      {frame < endStart ? <Karaoke props={props} /> : null}

      {/* end card */}
      <Sequence from={endStart} durationInFrames={V11_ENDCARD_FRAMES} name="end-card">
        <EndCard props={props} />
      </Sequence>

      <Vignette />
      <GrainOverlay />
    </AbsoluteFill>
  );
};
