import React from "react";
import { useCurrentFrame, useVideoConfig, staticFile } from "remotion";
import { useWindowedAudioData, visualizeAudio } from "@remotion/media-utils";

const TONE_COLORS: Record<string, string> = {
  cyan: "#36E0FF",
  amber: "#FFC217",
  red: "#D72638",
};

/**
 * Persistent audio-reactive equalizer bars (the format's signature motif).
 * Rendered ONCE at the composition top level (not inside a Sequence) so the
 * frame is the global timeline frame — keeps the spectrum continuous and in
 * sync with the single audio track. Colour is driven by the active beat tone.
 */
export const EqBars: React.FC<{
  audioSrc: string;
  tone: "cyan" | "amber" | "red";
  bars?: number;
  height?: number;
}> = ({ audioSrc, tone, bars = 56, height = 110 }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const { audioData, dataOffsetInSeconds } = useWindowedAudioData({
    src: staticFile(audioSrc),
    frame,
    fps,
    windowInSeconds: 16,
  });

  if (!audioData) {
    return null;
  }

  const freqs = visualizeAudio({
    fps,
    frame,
    audioData,
    numberOfSamples: 128,
    optimizeFor: "speed",
    dataOffsetInSeconds,
  });

  // Use the lower-mid band (most musical energy), mirror it for a symmetric
  // centre-out spectrum like a broadcast EQ.
  const half = Math.floor(bars / 2);
  const band = freqs.slice(2, 2 + half);
  const mirrored = [...[...band].reverse(), ...band];
  const color = TONE_COLORS[tone] ?? TONE_COLORS.cyan;

  return (
    <div
      style={{
        display: "flex",
        alignItems: "flex-end",
        justifyContent: "center",
        gap: 4,
        height,
        width: "100%",
      }}
    >
      {mirrored.map((v, i) => {
        const norm = Math.min(1, Math.pow(v, 0.7) * 2.4);
        const h = Math.max(3, norm * height);
        return (
          <div
            key={i}
            style={{
              width: 6,
              height: h,
              background: `linear-gradient(to top, ${color}, ${color}cc)`,
              borderRadius: 3,
              opacity: 0.9,
              boxShadow: `0 0 10px ${color}aa`,
            }}
          />
        );
      })}
    </div>
  );
};
