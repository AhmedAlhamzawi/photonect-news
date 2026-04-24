// Instagram Reels + TikTok safe-area insets for a 1080×1920 canvas.
// Derived empirically from platform screenshots (2026-04-17):
//   - IG Reels: top ~status+back, bottom ~caption+music, left ~profile avatar
//   - TikTok:   top ~status+back, bottom ~caption+music, right ~action rail
// Use the UNION of both — anything drawn inside PLATFORM_SAFE is visible on both.
//
// Background media (hero/broll) may bleed edge-to-edge. Only overlay chrome and
// text content must respect these insets.

export const PLATFORM_SAFE = {
  top: 280,     // status bar + back/search button
  bottom: 400,  // caption drawer + music strip + profile bubble (IG)
  left: 120,    // IG profile avatar overlay
  right: 160,   // TikTok action rail (like/comment/share/profile)
} as const;

// Canvas geometry.
export const CANVAS_WIDTH = 1080;
export const CANVAS_HEIGHT = 1920;

// Height of the TopStrip chrome that sits just inside the top safe line.
export const TOP_STRIP_HEIGHT = 64;

// Vertical offset where content can start (below top chrome + a small gap).
export const CONTENT_TOP = PLATFORM_SAFE.top + TOP_STRIP_HEIGHT + 20; // 364

// The absolute bottom line text must NOT cross. IG caption drawer overlays
// the bottom 400px. Anything below y = 1920-400 = 1520 is invisible.
export const CONTENT_BOTTOM = CANVAS_HEIGHT - PLATFORM_SAFE.bottom; // 1520

// Vertical content area height (between top chrome and IG caption strip).
export const CONTENT_HEIGHT = CONTENT_BOTTOM - CONTENT_TOP; // 1156

// CSS padding shorthand for content containers: "top right bottom left".
export const CONTENT_PADDING = `${CONTENT_TOP}px ${PLATFORM_SAFE.right}px ${PLATFORM_SAFE.bottom}px ${PLATFORM_SAFE.left}px`;

// Max content width (1080 - left - right) — headline maxWidth should cap at this.
export const CONTENT_WIDTH = 1080 - PLATFORM_SAFE.left - PLATFORM_SAFE.right; // 800

// Max stat text width — leave some breathing room vs CONTENT_WIDTH so giant
// stats do not kiss the right safe-line.
export const STAT_MAX_WIDTH = CONTENT_WIDTH - 40; // 760

// V5: For variant B (KINETIC-SPLIT), the content sits in the BOTTOM HALF only,
// minus the IG bottom safe zone. That gives us y = 960 → 1520 = 560px of
// vertical canvas for content. Subtract internal padding (44 top + 28 bottom)
// and you have ~488px for actual text — room for pill + heading + ONE stat.
//
// Any component that composes inside the bottom-half must cap its content to
// SPLIT_BOTTOM_HEIGHT so nothing slides into the caption-drawer zone.
export const SPLIT_TOP_HEIGHT = CANVAS_HEIGHT / 2; // 960
export const SPLIT_BOTTOM_HEIGHT = CANVAS_HEIGHT - SPLIT_TOP_HEIGHT - PLATFORM_SAFE.bottom; // 560

// Adaptive font-size helper: given a fontSize and character count, shrink the
// fontSize so the rendered width stays under maxPx (assumes ~0.55em avg char).
// Used by BeatA bigStat to defend against overflow on long values like "$9.0T".
export const adaptiveFontSize = (
  base: number,
  charCount: number,
  maxPx: number,
): number => {
  const estWidth = charCount * base * 0.55;
  if (estWidth <= maxPx) return base;
  return Math.floor((maxPx / estWidth) * base);
};
