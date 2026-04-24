import React from "react";
import { Img, interpolate, useCurrentFrame, Easing, staticFile } from "remotion";
import { PHOTONECT } from "../../PhotonectBrandReel/brand";
import { FONT_ARABIC } from "../../PhotonectBrandReel/fonts";

type Props = {
  src: string;
  caption?: string;
  accent: string;
};

export const PhotoInsert: React.FC<Props> = ({ src, caption, accent }) => {
  const frame = useCurrentFrame();

  const reveal = interpolate(frame, [90, 120], [0, 1], {
    easing: Easing.bezier(0.16, 1, 0.3, 1),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const resolved = src.startsWith("http") ? src : staticFile(src);

  return (
    <div
      style={{
        position: "absolute",
        left: 60,
        bottom: 400,
        width: 300,
        padding: 10,
        background: "rgba(10,10,15,0.88)",
        border: `2px solid ${accent}`,
        borderRadius: 10,
        opacity: reveal,
        transform: `translateY(${(1 - reveal) * 18}px) rotate(-1.5deg)`,
        boxShadow: `0 12px 48px ${PHOTONECT.ink}CC, 0 0 0 4px ${PHOTONECT.ink}`,
        direction: "ltr",
      }}
    >
      <div
        style={{
          position: "absolute",
          top: -14,
          left: 16,
          padding: "4px 10px",
          background: accent,
          color: PHOTONECT.ink,
          fontFamily: FONT_ARABIC,
          fontWeight: 900,
          fontSize: 14,
          letterSpacing: "0.14em",
          borderRadius: 3,
        }}
      >
        صورة من الميدان
      </div>
      <Img
        src={resolved}
        style={{
          width: "100%",
          height: 200,
          objectFit: "cover",
          borderRadius: 4,
          filter: "saturate(1.05) contrast(1.06)",
        }}
      />
      {caption && (
        <div
          style={{
            fontFamily: FONT_ARABIC,
            fontWeight: 500,
            fontSize: 16,
            color: PHOTONECT.paper,
            opacity: 0.82,
            marginTop: 8,
            textAlign: "right",
            direction: "rtl",
            lineHeight: 1.3,
          }}
        >
          {caption}
        </div>
      )}
    </div>
  );
};
