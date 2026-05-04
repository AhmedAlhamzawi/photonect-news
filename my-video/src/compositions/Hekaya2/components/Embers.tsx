import React from "react";
import { AbsoluteFill, interpolate, useCurrentFrame } from "remotion";
import { HEKAYA_PALETTE } from "../schema";

/**
 * Atmospheric layer 1 — gold particles drifting upward.
 * Decoupled from v1 so v2 can evolve independently. 22 deterministic
 * dots at fixed seeds so the look is reproducible across renders.
 */
export const Embers: React.FC<{ count?: number }> = ({ count = 22 }) => {
  const frame = useCurrentFrame();
  const dots = Array.from({ length: count }, (_, i) => i);
  return (
    <AbsoluteFill style={{ pointerEvents: "none" }}>
      {dots.map((i) => {
        const seed = (i * 37) % 100;
        const x = (seed * 13) % 1080;
        const y = (seed * 47) % 1920;
        const driftY = interpolate(frame, [0, 600], [0, -120 - (seed % 40)]);
        const opacity = interpolate(
          frame,
          [0, 60, 540, 600],
          [
            0,
            0.45 + (seed % 30) / 200,
            0.45 + (seed % 30) / 200,
            0,
          ],
          { extrapolateRight: "extend" },
        );
        return (
          <div
            key={i}
            style={{
              position: "absolute",
              left: x,
              top: y + driftY,
              width: 3 + (seed % 3),
              height: 3 + (seed % 3),
              borderRadius: "50%",
              background: HEKAYA_PALETTE.gold,
              boxShadow: `0 0 8px ${HEKAYA_PALETTE.gold}`,
              opacity,
            }}
          />
        );
      })}
    </AbsoluteFill>
  );
};
