import React from "react";
import { AbsoluteFill, interpolate, useCurrentFrame, Easing, Video, Img, staticFile } from "remotion";
import { PHOTONECT } from "../PhotonectBrandReel/brand";

type Props = {
  src?: string;
  type?: "video" | "image";
  accent: string;
  intensity?: "hero" | "beat";
  durationFrames: number;
  muted?: boolean;
};

export const VideoBackdrop: React.FC<Props> = ({
  src,
  type,
  accent,
  intensity = "beat",
  durationFrames,
  muted = true,
}) => {
  const frame = useCurrentFrame();

  const zoom = interpolate(frame, [0, durationFrames], [1.06, 1.16], {
    easing: Easing.linear,
    extrapolateRight: "clamp",
  });
  const panX = interpolate(frame, [0, durationFrames], [0, -3], {
    easing: Easing.linear,
    extrapolateRight: "clamp",
  });
  const reveal = interpolate(frame, [0, 14], [0, 1], {
    easing: Easing.bezier(0.16, 1, 0.3, 1),
    extrapolateRight: "clamp",
  });

  // Hero overlay (calibrated 2026-04-20): previous ED (93%) bottom stop crushed
  // the rendered hero below L=62 even for uniformly-bright source images
  // (empirically: L=106 raw → L=48 rendered under ED bottom). New gradient 22/33/77
  // (13/20/47% alpha) preserves dramatic bottom mood while keeping rendered mean
  // above the 62 floor for raw L≥90 inputs. Headline legibility preserved by the
  // headline's own textShadow + a dedicated narrow scrim in Breaking.tsx.
  //
  // Beat overlay calibrated so broll with L≥75 source luminance renders at L≥40
  // after compositing (avg overlay alpha ≈52% vs the prior 71% which crushed dark broll).
  // Stat cards retain legibility via their own rgba(10,10,15,0.55) card backgrounds.
  const overlay =
    intensity === "hero"
      ? `linear-gradient(180deg, ${PHOTONECT.ink}22 0%, ${PHOTONECT.ink}33 35%, ${PHOTONECT.ink}77 100%)`
      : `linear-gradient(180deg, ${PHOTONECT.ink}77 0%, ${PHOTONECT.ink}66 35%, ${PHOTONECT.ink}BB 100%)`;

  const mediaStyle: React.CSSProperties = {
    width: "100%",
    height: "100%",
    objectFit: "cover",
  };

  // Guard: if broll is missing from props.json, render solid ink fallback rather than crash.
  // Root cause of BUG-V4-001: Zod schema marks broll required but Remotion doesn't re-validate
  // at render time, so undefined propagates to src.startsWith() and throws.
  if (!src) {
    return (
      <AbsoluteFill
        style={{ overflow: "hidden", opacity: reveal, background: PHOTONECT.ink }}
      />
    );
  }

  const resolved = src.startsWith("http") ? src : staticFile(src);

  return (
    <AbsoluteFill style={{ overflow: "hidden", opacity: reveal, background: PHOTONECT.ink }}>
      <AbsoluteFill
        style={{
          transform: `scale(${zoom}) translateX(${panX}%)`,
          filter: "saturate(0.9) contrast(1.08)",
        }}
      >
        {type === "video" ? (
          <Video src={resolved} style={mediaStyle} muted={muted} />
        ) : (
          <Img src={resolved} style={mediaStyle} />
        )}
      </AbsoluteFill>

      <AbsoluteFill style={{ background: overlay }} />

      {intensity === "hero" && (
        <AbsoluteFill
          style={{
            backgroundImage: `repeating-linear-gradient(0deg, ${accent}09 0, ${accent}09 1px, transparent 1px, transparent 5px)`,
            mixBlendMode: "screen",
            pointerEvents: "none",
          }}
        />
      )}

      <AbsoluteFill
        style={{
          pointerEvents: "none",
          boxShadow:
            intensity === "hero"
              ? `inset 0 0 0 2px ${accent}33, inset 0 0 120px ${PHOTONECT.ink}CC`
              : `inset 0 0 0 2px ${accent}22, inset 0 0 60px ${PHOTONECT.ink}88`,
        }}
      />
    </AbsoluteFill>
  );
};
