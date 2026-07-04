import { loadFont } from "@remotion/google-fonts/Cairo";

// Sindibad brand font is Cairo (per brand kit). Loaded at module top-level so
// glyphs are ready at frame 0 (avoids the "Arabic renders as boxes" failure).
export const { fontFamily: CAIRO } = loadFont("normal", {
  weights: ["400", "600", "700", "900"],
  subsets: ["arabic", "latin"],
});
