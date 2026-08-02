import React from "react";
import { interpolate, useCurrentFrame, Easing } from "remotion";

// ── The Vox device kit ───────────────────────────────────────────────────────
// Each device below is one entry from the Vox visual vocabulary, implemented as
// a deterministic Remotion component so it animates on exact frames.

/** Snappy ease with slight overshoot — the signature Vox "pop into place". */
export const pop = (frame: number, at: number, dur = 10) =>
  interpolate(frame, [at, at + dur], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.back(2.2)),
  });

/** Paper grain + halftone dots — sells the "cut and pasted" print feel. */
export const PaperTexture: React.FC<{ opacity?: number }> = ({ opacity = 0.5 }) => (
  <div
    style={{
      position: "absolute",
      inset: 0,
      pointerEvents: "none",
      opacity,
      backgroundImage:
        // halftone dot grid
        "radial-gradient(circle at 1px 1px, rgba(0,0,0,0.16) 1px, transparent 1.6px)," +
        // coarse paper mottle
        "radial-gradient(circle at 7px 12px, rgba(0,0,0,0.05) 2px, transparent 3px)",
      backgroundSize: "6px 6px, 23px 23px",
      mixBlendMode: "multiply",
    }}
  />
);

/** Torn / rough white paper border around a photographic cutout. */
export const Cutout: React.FC<{
  src: string;
  x: number; y: number; w: number;      // normalised
  rotate?: number;
  atFrame: number;
  scaleTo?: number;
}> = ({ src, x, y, w, rotate = 0, atFrame, scaleTo = 1 }) => {
  const frame = useCurrentFrame();
  const p = pop(frame, atFrame, 12);
  return (
    <div
      style={{
        position: "absolute",
        left: `${x * 100}%`,
        top: `${y * 100}%`,
        width: `${w * 100}%`,
        transform: `translate(-50%,-50%) rotate(${rotate}deg) scale(${p * scaleTo})`,
        opacity: Math.min(1, p * 1.4),
        // the rough white paper edge + print drop shadow
        padding: "1.6%",
        background: "#FCFAF4",
        boxShadow: "0 18px 34px rgba(0,0,0,0.28)",
        filter: "drop-shadow(0 2px 0 rgba(0,0,0,0.06))",
      }}
    >
      <img src={src} style={{ width: "100%", display: "block" }} />
    </div>
  );
};

/** Hand-drawn marker annotation that draws itself in one confident stroke. */
export const Marker: React.FC<{
  kind: "circle" | "underline" | "arrow" | "bracket";
  x: number; y: number; w: number; h: number;
  atFrame: number; drawFrames?: number; color?: string;
}> = ({ kind, x, y, w, h, atFrame, drawFrames = 14, color = "#0A0A10" }) => {
  const frame = useCurrentFrame();
  const t = interpolate(frame, [atFrame, atFrame + drawFrames], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.inOut(Easing.quad),
  });
  if (t <= 0) return null;

  // slightly irregular geometry so it reads hand-drawn, never vector-perfect
  const path =
    kind === "circle"
      ? "M 96 50 C 96 74, 76 92, 50 92 C 24 92, 4 74, 4 50 C 4 26, 24 8, 50 8 C 74 8, 97 24, 96 49 C 95 60, 93 66, 90 72"
      : kind === "underline"
      ? "M 3 62 C 26 52, 55 50, 97 58"
      : kind === "arrow"
      ? "M 4 78 C 30 70, 58 48, 88 20 M 88 20 L 66 26 M 88 20 L 82 42"
      : "M 22 6 C 6 20, 6 78, 22 94 M 78 6 C 94 20, 94 78, 78 94";

  return (
    <svg
      viewBox="0 0 100 100"
      preserveAspectRatio="none"
      style={{
        position: "absolute",
        left: `${(x - w / 2) * 100}%`,
        top: `${(y - h / 2) * 100}%`,
        width: `${w * 100}%`,
        height: `${h * 100}%`,
        overflow: "visible",
      }}
    >
      <path
        d={path}
        fill="none"
        stroke={color}
        strokeWidth={3.4}
        strokeLinecap="round"
        strokeLinejoin="round"
        pathLength={1}
        strokeDasharray={1}
        strokeDashoffset={1 - t}
        style={{ filter: "drop-shadow(0 1px 0 rgba(0,0,0,0.12))" }}
      />
    </svg>
  );
};

/** Abstract bar chart that grows step by step — no numerals, pure shape. */
export const Bars: React.FC<{
  values: number[]; x: number; y: number; w: number; h: number;
  atFrame: number; color?: string;
}> = ({ values, x, y, w, h, atFrame, color = "#D72638" }) => {
  const frame = useCurrentFrame();
  return (
    <div
      style={{
        position: "absolute",
        left: `${(x - w / 2) * 100}%`,
        top: `${(y - h / 2) * 100}%`,
        width: `${w * 100}%`,
        height: `${h * 100}%`,
        display: "flex",
        alignItems: "flex-end",
        gap: "6%",
      }}
    >
      {values.map((v, i) => {
        const g = interpolate(frame, [atFrame + i * 5, atFrame + i * 5 + 11], [0, 1], {
          extrapolateLeft: "clamp",
          extrapolateRight: "clamp",
          easing: Easing.out(Easing.back(1.5)),
        });
        return (
          <div
            key={i}
            style={{
              flex: 1,
              height: `${v * g * 100}%`,
              background: color,
              boxShadow: "0 8px 18px rgba(0,0,0,0.22)",
            }}
          />
        );
      })}
    </div>
  );
};

/** Redaction / highlight bar sliding across — the Vox "censor" beat. */
export const Redaction: React.FC<{
  x: number; y: number; w: number; h: number; atFrame: number; color?: string;
}> = ({ x, y, w, h, atFrame, color = "#0A0A10" }) => {
  const frame = useCurrentFrame();
  const t = interpolate(frame, [atFrame, atFrame + 9], [0, 1], {
    extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.out(Easing.cubic),
  });
  return (
    <div style={{
      position: "absolute",
      left: `${(x - w / 2) * 100}%`, top: `${(y - h / 2) * 100}%`,
      width: `${w * t * 100}%`, height: `${h * 100}%`,
      background: color, transformOrigin: "left center",
    }} />
  );
};

/** The recurring through-line motif: a widening crack that escalates each block. */
export const ThroughLine: React.FC<{ level: number; color?: string }> = ({
  level, color = "#D72638",
}) => {
  const frame = useCurrentFrame();
  if (level <= 0) return null;
  const breathe = 1 + 0.02 * Math.sin(frame / 11);
  const spread = 0.4 + level * 3.4;      // the gap widens block by block
  return (
    <svg
      viewBox="0 0 100 220"
      preserveAspectRatio="none"
      style={{ position: "absolute", inset: 0, width: "100%", height: "100%", opacity: 0.9 }}
    >
      {/* two diverging strokes — the widening gap between the two rates */}
      <path
        d={`M 50 0 C ${50 - spread} 60, ${50 - spread * 1.6} 140, ${50 - spread * 2.4} 220`}
        fill="none" stroke={color} strokeWidth={1.1 * breathe} strokeLinecap="round" opacity={0.85}
      />
      <path
        d={`M 50 0 C ${50 + spread} 60, ${50 + spread * 1.6} 140, ${50 + spread * 2.4} 220`}
        fill="none" stroke="#0A0A10" strokeWidth={1.1 * breathe} strokeLinecap="round" opacity={0.5}
      />
    </svg>
  );
};
