import React from "react";
import {
  AbsoluteFill,
  Audio,
  Img,
  staticFile,
  interpolate,
  useCurrentFrame,
  Easing,
} from "remotion";
import { TransitionSeries, linearTiming } from "@remotion/transitions";
import { fade } from "@remotion/transitions/fade";
import {
  BrandTravelReelProps,
  DestinationT,
  INTRO_F,
  DEST_F,
  OUTRO_F,
  TRANS_F,
  computeTravelDuration,
} from "./schema";
import { CAIRO } from "./fonts";

// ---------- shared motion helpers ----------
const EASE_IN = Easing.bezier(0.16, 1, 0.3, 1); // crisp UI entrance
const EASE_KB = Easing.bezier(0.45, 0, 0.55, 1); // editorial Ken Burns
const EASE_POP = Easing.bezier(0.34, 1.56, 0.64, 1); // sparing overshoot

const rise = (f: number, delay: number, dist = 36) => {
  const opacity = interpolate(f, [delay, delay + 16], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: EASE_IN,
  });
  const y = interpolate(f, [delay, delay + 24], [dist, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: EASE_IN,
  });
  return { opacity, transform: `translateY(${y}px)` };
};

// ---------- texture layers ----------
const KenBurns: React.FC<{ src: string; dur: number; dir: number }> = ({
  src,
  dur,
  dir,
}) => {
  const f = useCurrentFrame();
  const p = interpolate(f, [0, dur], [0, 1], {
    extrapolateRight: "clamp",
    easing: EASE_KB,
  });
  const scale = 1.12 + p * 0.13;
  const tx = (dir % 2 === 0 ? -1 : 1) * p * 30;
  const ty = (dir % 3 === 0 ? 1 : -1) * p * 22;
  return (
    <AbsoluteFill>
      <Img
        src={staticFile(src)}
        style={{
          width: "100%",
          height: "100%",
          objectFit: "cover",
          transform: `scale(${scale}) translate(${tx}px, ${ty}px)`,
        }}
      />
    </AbsoluteFill>
  );
};

const Scrim: React.FC = () => (
  <AbsoluteFill
    style={{
      background:
        "linear-gradient(to top, rgba(20,6,11,0.95) 0%, rgba(20,6,11,0.62) 26%, rgba(20,6,11,0.0) 52%, rgba(20,6,11,0.10) 78%, rgba(20,6,11,0.42) 100%)",
    }}
  />
);

const Vignette: React.FC = () => (
  <AbsoluteFill
    style={{
      background:
        "radial-gradient(ellipse 75% 60% at 50% 45%, rgba(0,0,0,0) 55%, rgba(0,0,0,0.5) 100%)",
    }}
  />
);

const Grain: React.FC<{ opacity?: number }> = ({ opacity = 0.07 }) => (
  <AbsoluteFill style={{ opacity, mixBlendMode: "overlay", pointerEvents: "none" }}>
    <svg width="100%" height="100%">
      <filter id="grainf">
        <feTurbulence
          type="fractalNoise"
          baseFrequency="0.9"
          numOctaves={2}
          stitchTiles="stitch"
        />
      </filter>
      <rect width="100%" height="100%" filter="url(#grainf)" />
    </svg>
  </AbsoluteFill>
);

// ---------- scenes ----------
const SAFE_X = 96; // platform-safe horizontal padding

const IntroScene: React.FC<{ p: BrandTravelReelProps }> = ({ p }) => {
  const f = useCurrentFrame();
  const { crimson, cream, sand } = p.brand;
  // crimson accent line draws in
  const lineW = interpolate(f, [10, 34], [0, 140], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: EASE_IN,
  });
  return (
    <AbsoluteFill>
      <KenBurns src={p.intro.image} dur={INTRO_F} dir={0} />
      <Scrim />
      <Vignette />
      {/* brand chip top-right (RTL) */}
      <div
        style={{
          position: "absolute",
          top: 86,
          right: SAFE_X,
          ...rise(f, 4, 24),
        }}
      >
        <div
          style={{
            background: crimson,
            color: "#fff",
            fontFamily: CAIRO,
            fontWeight: 900,
            fontSize: 34,
            padding: "12px 30px 16px",
            borderRadius: 999,
            letterSpacing: 1,
            direction: "rtl",
          }}
        >
          {p.brand.name}
        </div>
      </div>
      {/* bottom hook block */}
      <div
        style={{
          position: "absolute",
          right: SAFE_X,
          left: SAFE_X,
          bottom: 360,
          direction: "rtl",
          textAlign: "right",
        }}
      >
        <div style={{ ...rise(f, 8) }}>
          <div
            style={{
              fontFamily: CAIRO,
              fontWeight: 700,
              fontSize: 40,
              color: sand,
              marginBottom: 18,
            }}
          >
            {p.intro.kicker}
          </div>
        </div>
        <div
          style={{
            height: 7,
            width: lineW,
            background: crimson,
            borderRadius: 4,
            marginLeft: "auto",
            marginBottom: 26,
          }}
        />
        <div style={{ ...rise(f, 14) }}>
          <div
            style={{
              fontFamily: CAIRO,
              fontWeight: 900,
              fontSize: 96,
              lineHeight: 1.08,
              color: cream,
              whiteSpace: "pre-line",
              textShadow: "0 4px 30px rgba(0,0,0,0.5)",
            }}
          >
            {p.intro.hook}
          </div>
        </div>
        <div style={{ ...rise(f, 26) }}>
          <div
            style={{
              fontFamily: CAIRO,
              fontWeight: 600,
              fontSize: 44,
              color: cream,
              opacity: 0.92,
              marginTop: 24,
            }}
          >
            {p.intro.subhead}
          </div>
        </div>
      </div>
    </AbsoluteFill>
  );
};

const DestScene: React.FC<{
  p: BrandTravelReelProps;
  d: DestinationT;
  i: number;
}> = ({ p, d, i }) => {
  const f = useCurrentFrame();
  const { crimson, cream, sand } = p.brand;
  // crimson vertical bar grows
  const barH = interpolate(f, [6, 30], [0, 210], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: EASE_IN,
  });
  // faint giant index in corner
  const idxOpacity = interpolate(f, [4, 24], [0, 0.16], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  return (
    <AbsoluteFill>
      <KenBurns src={d.image} dur={DEST_F} dir={i + 1} />
      <Scrim />
      <Vignette />
      {/* faint giant index, top-left */}
      <div
        style={{
          position: "absolute",
          top: 70,
          left: SAFE_X - 8,
          fontFamily: CAIRO,
          fontWeight: 900,
          fontSize: 300,
          lineHeight: 0.8,
          color: cream,
          opacity: idxOpacity,
        }}
      >
        {d.index}
      </div>
      {/* bottom text block (RTL, right-aligned) with crimson bar on its right */}
      <div
        style={{
          position: "absolute",
          right: SAFE_X,
          left: SAFE_X,
          bottom: 360,
          direction: "rtl",
          textAlign: "right",
          display: "flex",
          flexDirection: "row-reverse",
          alignItems: "flex-end",
          gap: 34,
        }}
      >
        <div
          style={{
            width: 8,
            height: barH,
            background: crimson,
            borderRadius: 4,
            flex: "none",
          }}
        />
        <div style={{ flex: 1 }}>
          {/* crimson tag pill */}
          <div style={{ ...rise(f, 8, 24) }}>
            <div
              style={{
                display: "inline-block",
                background: crimson,
                color: "#fff",
                fontFamily: CAIRO,
                fontWeight: 700,
                fontSize: 32,
                padding: "8px 24px 12px",
                borderRadius: 999,
                marginBottom: 22,
              }}
            >
              {d.tag}
            </div>
          </div>
          <div style={{ ...rise(f, 14) }}>
            <div
              style={{
                fontFamily: CAIRO,
                fontWeight: 900,
                fontSize: 92,
                lineHeight: 1.05,
                color: cream,
                textShadow: "0 4px 28px rgba(0,0,0,0.55)",
              }}
            >
              {d.name}
            </div>
          </div>
          <div style={{ ...rise(f, 22) }}>
            <div
              style={{
                fontFamily: CAIRO,
                fontWeight: 600,
                fontSize: 42,
                color: cream,
                opacity: 0.9,
                marginTop: 16,
              }}
            >
              {d.descriptor}
            </div>
          </div>
        </div>
      </div>
    </AbsoluteFill>
  );
};

const OutroScene: React.FC<{ p: BrandTravelReelProps }> = ({ p }) => {
  const f = useCurrentFrame();
  const { crimson, cream, ink, sand } = p.brand;
  const logoScale = interpolate(f, [6, 34], [0.82, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: EASE_POP,
  });
  const logoOpacity = interpolate(f, [6, 24], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  return (
    <AbsoluteFill style={{ background: cream }}>
      {/* soft sand glow top, crimson band bottom */}
      <AbsoluteFill
        style={{
          background:
            "radial-gradient(ellipse 80% 50% at 50% 22%, rgba(232,201,148,0.35) 0%, rgba(255,252,250,0) 60%)",
        }}
      />
      <AbsoluteFill
        style={{
          background: `linear-gradient(to top, ${crimson} 0%, rgba(205,0,55,0) 26%)`,
        }}
      />
      <Grain opacity={0.04} />
      <AbsoluteFill
        style={{
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
          padding: SAFE_X,
        }}
      >
        <div
          style={{
            opacity: logoOpacity,
            transform: `scale(${logoScale})`,
            marginBottom: 70,
          }}
        >
          <Img src={staticFile(p.brand.logo)} style={{ width: 560 }} />
        </div>
        <div style={{ ...rise(f, 22), direction: "rtl", textAlign: "center" }}>
          <div
            style={{
              fontFamily: CAIRO,
              fontWeight: 900,
              fontSize: 86,
              color: ink,
              lineHeight: 1.1,
            }}
          >
            {p.outro.headline}
          </div>
        </div>
        <div style={{ ...rise(f, 32), direction: "rtl", textAlign: "center" }}>
          <div
            style={{
              fontFamily: CAIRO,
              fontWeight: 600,
              fontSize: 40,
              color: "#5A3540",
              marginTop: 22,
              maxWidth: 760,
            }}
          >
            {p.outro.subline}
          </div>
        </div>
        <div
          style={{
            ...rise(f, 44),
            position: "absolute",
            bottom: 150,
          }}
        >
          <div
            style={{
              fontFamily: CAIRO,
              fontWeight: 700,
              fontSize: 40,
              color: "#fff",
              letterSpacing: 1.5,
            }}
          >
            {p.brand.handle}
          </div>
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

// ---------- root composition ----------
export const BrandTravelReel: React.FC<BrandTravelReelProps> = (p) => {
  const total = computeTravelDuration(p.destinations.length);
  const f = useCurrentFrame();
  const audioVolume = interpolate(
    f,
    [0, 18, total - 40, total - 6],
    [0, 0.6, 0.6, 0],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" },
  );
  const trans = () => (
    <TransitionSeries.Transition
      presentation={fade()}
      timing={linearTiming({ durationInFrames: TRANS_F })}
    />
  );
  return (
    <AbsoluteFill style={{ background: p.brand.ink }}>
      <Audio src={staticFile(p.audio)} volume={audioVolume} loop />
      <TransitionSeries>
        <TransitionSeries.Sequence durationInFrames={INTRO_F}>
          <IntroScene p={p} />
        </TransitionSeries.Sequence>
        {trans()}
        {p.destinations.map((d, i) => (
          <React.Fragment key={i}>
            <TransitionSeries.Sequence durationInFrames={DEST_F}>
              <DestScene p={p} d={d} i={i} />
            </TransitionSeries.Sequence>
            {trans()}
          </React.Fragment>
        ))}
        <TransitionSeries.Sequence durationInFrames={OUTRO_F}>
          <OutroScene p={p} />
        </TransitionSeries.Sequence>
      </TransitionSeries>
      <Grain opacity={0.06} />
    </AbsoluteFill>
  );
};
