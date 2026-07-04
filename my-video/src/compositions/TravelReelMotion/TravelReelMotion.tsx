import React from "react";
import {
  AbsoluteFill,
  Audio,
  OffthreadVideo,
  Img,
  Series,
  staticFile,
  interpolate,
  useCurrentFrame,
  Easing,
} from "remotion";
import {
  TravelReelMotionProps,
  MSceneT,
  HOOK_F,
  DEST_F,
  OUTRO_F,
  computeMotionDuration,
} from "./schema";
import { CAIRO } from "../BrandTravelReel/fonts";

const EASE_OUT = Easing.bezier(0.16, 1, 0.3, 1);
const EASE_POP = Easing.bezier(0.34, 1.56, 0.64, 1);
const SAFE = 90;

// punchy entrance: rise + slight scale, snappy
const pop = (f: number, delay: number, dist = 46) => {
  const o = interpolate(f, [delay, delay + 10], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const y = interpolate(f, [delay, delay + 16], [dist, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: EASE_POP,
  });
  return { opacity: o, transform: `translateY(${y}px)` };
};

// vibrant video layer + a tiny entry zoom-punch for energy; light bottom scrim only
const VividClip: React.FC<{ src: string; startFrom: number; dur: number }> = ({
  src,
  startFrom,
  dur,
}) => {
  const f = useCurrentFrame();
  const zoom = interpolate(f, [0, dur], [1.06, 1.0], {
    extrapolateRight: "clamp",
    easing: EASE_OUT,
  });
  return (
    <AbsoluteFill>
      <OffthreadVideo
        src={staticFile(src)}
        startFrom={startFrom}
        muted
        style={{
          width: "100%",
          height: "100%",
          objectFit: "cover",
          transform: `scale(${zoom})`,
          filter: "saturate(1.2) contrast(1.08) brightness(1.03)",
        }}
      />
      {/* light scrims for legibility ONLY — keep image vivid */}
      <AbsoluteFill
        style={{
          background:
            "linear-gradient(to top, rgba(15,4,9,0.78) 0%, rgba(15,4,9,0.30) 18%, rgba(15,4,9,0) 42%)",
        }}
      />
      <AbsoluteFill
        style={{
          background:
            "linear-gradient(to bottom, rgba(15,4,9,0.42) 0%, rgba(15,4,9,0) 16%)",
        }}
      />
    </AbsoluteFill>
  );
};

const BrandChip: React.FC<{ p: TravelReelMotionProps }> = ({ p }) => (
  <div
    style={{
      position: "absolute",
      top: 70,
      right: SAFE,
      background: p.brand.crimson,
      color: "#fff",
      fontFamily: CAIRO,
      fontWeight: 900,
      fontSize: 32,
      padding: "9px 26px 13px",
      borderRadius: 999,
      direction: "rtl",
      boxShadow: "0 6px 22px rgba(0,0,0,0.35)",
    }}
  >
    {p.brand.name}
  </div>
);

const HookScene: React.FC<{ p: TravelReelMotionProps }> = ({ p }) => {
  const f = useCurrentFrame();
  const { crimson, cream } = p.brand;
  const barW = interpolate(f, [8, 26], [0, 200], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: EASE_OUT,
  });
  // save-bait fades in late, gentle pulse
  const saveO = interpolate(f, [40, 56], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const pulse = 1 + 0.04 * Math.sin(f / 7);
  return (
    <AbsoluteFill>
      <VividClip src={p.hook.clip} startFrom={p.hook.startFrom} dur={HOOK_F} />
      <BrandChip p={p} />
      <div
        style={{
          position: "absolute",
          right: SAFE,
          left: SAFE,
          bottom: 300,
          direction: "rtl",
          textAlign: "right",
        }}
      >
        <div style={{ ...pop(f, 6) }}>
          <span
            style={{
              fontFamily: CAIRO,
              fontWeight: 900,
              fontSize: 120,
              color: cream,
              lineHeight: 1.0,
              textShadow: "0 6px 34px rgba(0,0,0,0.55)",
            }}
          >
            {p.hook.line1}
          </span>
        </div>
        <div
          style={{
            height: 9,
            width: barW,
            background: crimson,
            borderRadius: 5,
            marginRight: 6,
            marginTop: 10,
            marginBottom: 14,
          }}
        />
        <div style={{ ...pop(f, 16) }}>
          <span
            style={{
              fontFamily: CAIRO,
              fontWeight: 800,
              fontSize: 62,
              color: cream,
              textShadow: "0 4px 24px rgba(0,0,0,0.55)",
            }}
          >
            {p.hook.line2}
          </span>
        </div>
        <div
          style={{
            opacity: saveO,
            transform: `scale(${pulse})`,
            transformOrigin: "right center",
            marginTop: 34,
          }}
        >
          <span
            style={{
              display: "inline-block",
              background: "rgba(255,255,255,0.16)",
              backdropFilter: "blur(6px)",
              border: "2px solid rgba(255,255,255,0.5)",
              color: "#fff",
              fontFamily: CAIRO,
              fontWeight: 700,
              fontSize: 34,
              padding: "10px 26px 14px",
              borderRadius: 999,
            }}
          >
            {p.hook.save}
          </span>
        </div>
      </div>
    </AbsoluteFill>
  );
};

const DestScene: React.FC<{ p: TravelReelMotionProps; s: MSceneT }> = ({
  p,
  s,
}) => {
  const f = useCurrentFrame();
  const { crimson, cream } = p.brand;
  const barH = interpolate(f, [4, 22], [0, 132], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: EASE_OUT,
  });
  return (
    <AbsoluteFill>
      <VividClip src={s.clip} startFrom={s.startFrom} dur={DEST_F} />
      <BrandChip p={p} />
      <div
        style={{
          position: "absolute",
          right: SAFE,
          left: SAFE,
          bottom: 300,
          direction: "rtl",
          textAlign: "right",
          display: "flex",
          flexDirection: "row-reverse",
          alignItems: "flex-end",
          gap: 28,
        }}
      >
        <div
          style={{ width: 9, height: barH, background: crimson, borderRadius: 5, flex: "none" }}
        />
        <div style={{ flex: 1 }}>
          <div style={{ ...pop(f, 2, 28) }}>
            <span
              style={{
                display: "inline-block",
                background: crimson,
                color: "#fff",
                fontFamily: CAIRO,
                fontWeight: 800,
                fontSize: 34,
                padding: "8px 24px 12px",
                borderRadius: 999,
                marginBottom: 18,
              }}
            >
              {s.tag}
            </span>
          </div>
          <div style={{ ...pop(f, 8, 54) }}>
            <span
              style={{
                fontFamily: CAIRO,
                fontWeight: 900,
                fontSize: 104,
                color: cream,
                lineHeight: 1.02,
                textShadow: "0 6px 30px rgba(0,0,0,0.6)",
              }}
            >
              {s.name}
            </span>
          </div>
        </div>
      </div>
    </AbsoluteFill>
  );
};

const OutroScene: React.FC<{ p: TravelReelMotionProps }> = ({ p }) => {
  const f = useCurrentFrame();
  const { crimson, cream, ink } = p.brand;
  const logoScale = interpolate(f, [4, 26], [0.8, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: EASE_POP,
  });
  const logoO = interpolate(f, [4, 18], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  return (
    <AbsoluteFill style={{ background: cream }}>
      <AbsoluteFill
        style={{
          background:
            "radial-gradient(ellipse 80% 50% at 50% 26%, rgba(232,201,148,0.4) 0%, rgba(255,252,250,0) 60%)",
        }}
      />
      <AbsoluteFill
        style={{ background: `linear-gradient(to top, ${crimson} 0%, rgba(205,0,55,0) 24%)` }}
      />
      <AbsoluteFill
        style={{
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
          padding: SAFE,
        }}
      >
        <div style={{ opacity: logoO, transform: `scale(${logoScale})`, marginBottom: 64 }}>
          <Img src={staticFile(p.brand.logo)} style={{ width: 560 }} />
        </div>
        <div style={{ ...pop(f, 20), direction: "rtl", textAlign: "center" }}>
          <span style={{ fontFamily: CAIRO, fontWeight: 900, fontSize: 90, color: ink }}>
            {p.outro.headline}
          </span>
        </div>
        <div style={{ ...pop(f, 30), direction: "rtl", textAlign: "center" }}>
          <span
            style={{
              fontFamily: CAIRO,
              fontWeight: 600,
              fontSize: 42,
              color: "#5A3540",
              marginTop: 18,
              display: "inline-block",
            }}
          >
            {p.outro.subline}
          </span>
        </div>
        <div style={{ ...pop(f, 42), position: "absolute", bottom: 140 }}>
          <span
            style={{
              fontFamily: CAIRO,
              fontWeight: 700,
              fontSize: 40,
              color: "#fff",
              letterSpacing: 1.5,
            }}
          >
            {p.brand.handle}
          </span>
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

export const TravelReelMotion: React.FC<TravelReelMotionProps> = (p) => {
  const total = computeMotionDuration(p.scenes.length);
  const f = useCurrentFrame();
  const vol = interpolate(f, [0, 14, total - 32, total - 4], [0, 0.7, 0.7, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  return (
    <AbsoluteFill style={{ background: p.brand.ink }}>
      <Audio
        src={staticFile(p.audio)}
        startFrom={p.audioStartFrom}
        volume={vol}
        loop
      />
      <Series>
        <Series.Sequence durationInFrames={HOOK_F}>
          <HookScene p={p} />
        </Series.Sequence>
        {p.scenes.map((s, i) => (
          <Series.Sequence key={i} durationInFrames={DEST_F}>
            <DestScene p={p} s={s} />
          </Series.Sequence>
        ))}
        <Series.Sequence durationInFrames={OUTRO_F}>
          <OutroScene p={p} />
        </Series.Sequence>
      </Series>
    </AbsoluteFill>
  );
};
