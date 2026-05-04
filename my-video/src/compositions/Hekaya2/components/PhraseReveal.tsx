import React from "react";
import { interpolate, useCurrentFrame, Easing } from "remotion";
import { HEKAYA_PALETTE } from "../schema";

interface Props {
  text: string;
  /** Local frame inside the Sequence at which the reveal starts. */
  startFrame: number;
  /** How many frames the phrase stays on screen before fading. */
  durationFrames: number;
  /** Word inside `text` to flash gold at completion of the reveal. */
  keyWord?: string;
  /** Pixel font size. Default 56. */
  fontSize?: number;
  /** Max text width in px. Default 920. */
  maxWidth?: number;
  /** Right-to-left rendering. Default true (Arabic). */
  rtl?: boolean;
  /** Center alignment override. Default false (right-align for RTL). */
  center?: boolean;
}

/**
 * Phrase-by-phrase masked reveal — the core kinetic-typography element.
 *
 * Reveals 0→100% over the first 14 frames via a clip-path inset wipe
 * from the right edge (RTL-correct for Arabic), holds, then fades out
 * over the last 10 frames. The keyWord briefly flashes gold for 4
 * frames at the moment the phrase completes its reveal — the eye's
 * attention anchor.
 *
 * Why phrase-by-phrase, not letter-by-letter: Arabic uses connected
 * letterforms. Letter-by-letter reveals break ligatures and read as
 * Roman cosplay. Phrase-by-phrase preserves shaping and looks like
 * ink flowing into the page.
 */
export const PhraseReveal: React.FC<Props> = ({
  text,
  startFrame,
  durationFrames,
  keyWord,
  fontSize = 56,
  maxWidth = 920,
  rtl = true,
  center = false,
}) => {
  const frame = useCurrentFrame();
  const localFrame = frame - startFrame;

  // Out of window — render nothing
  if (localFrame < 0 || localFrame > durationFrames) return null;

  // Mask wipe: clip-path inset from right (100%) to left (0%) in 14 frames
  const reveal = interpolate(localFrame, [0, 14], [100, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.bezier(0.25, 0, 0.25, 1),
  });

  // Fade out at end of phrase duration — last 10 frames
  const fadeOut = interpolate(
    localFrame,
    [durationFrames - 10, durationFrames],
    [1, 0],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" },
  );

  // KeyWord gold flash — frames 14-18 just after reveal completes
  const highlightActive = localFrame >= 14 && localFrame <= 18;

  const renderText = () => {
    if (!keyWord || !text.includes(keyWord)) return text;
    const parts = text.split(keyWord);
    return (
      <>
        {parts.map((part, i) => (
          <React.Fragment key={i}>
            {part}
            {i < parts.length - 1 && (
              <span
                style={{
                  color: highlightActive
                    ? HEKAYA_PALETTE.gold
                    : HEKAYA_PALETTE.ivory,
                  transition: "color 80ms ease-out",
                }}
              >
                {keyWord}
              </span>
            )}
          </React.Fragment>
        ))}
      </>
    );
  };

  return (
    <div
      dir={rtl ? "rtl" : "ltr"}
      style={{
        fontFamily: "Tajawal, system-ui, sans-serif",
        fontSize,
        fontWeight: 700,
        color: HEKAYA_PALETTE.ivory,
        maxWidth,
        lineHeight: 1.4,
        textAlign: center ? "center" : rtl ? "right" : "left",
        // RTL clip-path: wipes from right edge to left
        clipPath: rtl
          ? `inset(0 ${reveal}% 0 0)`
          : `inset(0 0 0 ${reveal}%)`,
        opacity: fadeOut,
        textShadow: `0 4px 18px ${HEKAYA_PALETTE.shadow}cc`,
      }}
    >
      {renderText()}
    </div>
  );
};
