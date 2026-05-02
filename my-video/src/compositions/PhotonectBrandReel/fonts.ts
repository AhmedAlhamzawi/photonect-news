import { loadFont as loadInter } from "@remotion/google-fonts/Inter";
import { loadFont as loadTajawal } from "@remotion/google-fonts/Tajawal";

// 2026-05-02: switched FONT_ARABIC from IBM Plex Sans Arabic → Tajawal.
// Per Ahmed: "the arabic font is not nice." Tajawal is part of the original
// Photonect brand (memory: brand_identity → fonts (Tajawal/Cairo)) and pairs
// better with broadcast-grade headlines. Loading the full weight range so
// headlines can hit 800/900 for impact while body sits comfortably at 500.

const { fontFamily: interFamily } = loadInter("normal", {
  weights: ["400", "500", "700", "900"],
  subsets: ["latin"],
});

const { fontFamily: tajawalFamily } = loadTajawal("normal", {
  weights: ["400", "500", "700", "800", "900"],
  subsets: ["arabic"],
});

export const FONT_LATIN = interFamily;
export const FONT_ARABIC = tajawalFamily;
