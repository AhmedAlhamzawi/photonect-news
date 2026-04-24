import React, { useMemo } from "react";
import { AbsoluteFill, random } from "remotion";

// Deterministic film grain — cheap CSS-based noise via many tiny divs.
// For heavy grain use a noise SVG filter; this is light + fast.
export const GrainOverlay: React.FC<{ opacity?: number; seed?: number }> = ({
  opacity = 0.06,
  seed = 1,
}) => {
  const dots = useMemo(() => {
    const arr: { x: number; y: number; s: number; o: number }[] = [];
    for (let i = 0; i < 220; i++) {
      arr.push({
        x: random(`grain-x-${seed}-${i}`) * 100,
        y: random(`grain-y-${seed}-${i}`) * 100,
        s: 1 + random(`grain-s-${seed}-${i}`) * 2,
        o: 0.4 + random(`grain-o-${seed}-${i}`) * 0.6,
      });
    }
    return arr;
  }, [seed]);

  return (
    <AbsoluteFill style={{ opacity, pointerEvents: "none" }}>
      {dots.map((d, i) => (
        <div
          key={i}
          style={{
            position: "absolute",
            left: `${d.x}%`,
            top: `${d.y}%`,
            width: d.s,
            height: d.s,
            background: "white",
            opacity: d.o,
            borderRadius: "50%",
          }}
        />
      ))}
    </AbsoluteFill>
  );
};

// Subtle vignette for focus
export const Vignette: React.FC<{ strength?: number }> = ({ strength = 0.35 }) => (
  <AbsoluteFill
    style={{
      pointerEvents: "none",
      background: `radial-gradient(ellipse at center, transparent 50%, rgba(0,0,0,${strength}) 100%)`,
    }}
  />
);
