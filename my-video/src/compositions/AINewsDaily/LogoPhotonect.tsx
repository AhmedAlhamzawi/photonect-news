import React from "react";
import { FONT_LATIN } from "../PhotonectBrandReel/fonts";

/**
 * Photonect wordmark — canonical brand lockup.
 *
 * Layout: "PHOTO" stacked over "NECT", bold sans, tight leading.
 * A small red rectangle bar sits above the final "O" of PHOTO
 * (a macron/exposure-bar motif — light meeting logic).
 *
 * Two variants:
 *  - "dark"  → white letters + red bar (for dark video backgrounds)
 *  - "light" → ink letters + red bar (for light backgrounds)
 */
export const PHOTONECT_RED = "#D72638";
export const PHOTONECT_INK = "#1A1A1A";

type Props = {
  size: number; // pixel height of a single line ("PHOTO" cap height ≈ size)
  variant?: "dark" | "light";
  orientation?: "stacked" | "inline"; // stacked = PHOTO over NECT, inline = "PHOTONECT"
};

export const LogoPhotonect: React.FC<Props> = ({
  size,
  variant = "dark",
  orientation = "stacked",
}) => {
  const letterColor = variant === "dark" ? "#FFFFFF" : PHOTONECT_INK;
  const fontSize = size;
  // Typographic tuning — matched to Inter 900 measured vs reference
  const lineHeight = 0.92;
  const letterSpacing = "-0.045em";

  if (orientation === "inline") {
    const barWidth = fontSize * 0.27;
    const barHeight = fontSize * 0.11;
    return (
      <div
        style={{
          display: "inline-block",
          position: "relative",
          fontFamily: FONT_LATIN,
          fontWeight: 900,
          fontSize,
          letterSpacing,
          color: letterColor,
          lineHeight: 1,
          whiteSpace: "nowrap",
          paddingTop: barHeight * 1.3,
        }}
      >
        PHOTONECT
        {/* Red bar above the final O of PHOTO (index 4 of 9 letters) */}
        <div
          style={{
            position: "absolute",
            // PHOTONECT has 9 glyphs — final O of PHOTO is at index 4.
            // With letter-spacing -0.045em each glyph ≈ 0.58em wide for Inter Black.
            // Center of glyph #4 ≈ 4.5 * 0.58em = 2.61em from left edge of first glyph.
            left: `${4.5 * 0.54}em`,
            top: 0,
            width: barWidth,
            height: barHeight,
            background: PHOTONECT_RED,
            transform: "translateX(-50%)",
            borderRadius: 1,
          }}
        />
      </div>
    );
  }

  // Stacked: PHOTO over NECT, visually centered
  const barWidth = fontSize * 0.27;
  const barHeight = fontSize * 0.11;

  return (
    <div
      style={{
        display: "inline-block",
        position: "relative",
        fontFamily: FONT_LATIN,
        fontWeight: 900,
        fontSize,
        color: letterColor,
        lineHeight,
        letterSpacing,
        textAlign: "center",
        paddingTop: barHeight * 1.4,
      }}
    >
      <div style={{ position: "relative", display: "inline-block" }}>
        PHOTO
        {/* Red bar over the final O (index 4 of PHOTO = last letter) */}
        <div
          style={{
            position: "absolute",
            // Final O center ≈ 4.5 glyphs from left, glyph ≈ 0.58em
            left: `${4.5 * 0.54}em`,
            top: -barHeight * 1.1,
            width: barWidth,
            height: barHeight,
            background: PHOTONECT_RED,
            transform: "translateX(-50%)",
            borderRadius: 1,
          }}
        />
      </div>
      <div style={{ marginTop: -fontSize * 0.1 }}>NECT</div>
    </div>
  );
};

/** Compact single-line "PHOTONECT" lockup + red bar, for header strips */
export const LogoPhotonectInline: React.FC<{ size: number; variant?: "dark" | "light" }> = ({
  size,
  variant,
}) => <LogoPhotonect size={size} variant={variant} orientation="inline" />;
