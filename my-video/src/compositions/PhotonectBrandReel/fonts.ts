import { loadFont as loadInter } from "@remotion/google-fonts/Inter";
import { loadFont as loadPlexAr } from "@remotion/google-fonts/IBMPlexSansArabic";

const { fontFamily: interFamily } = loadInter("normal", {
  weights: ["400", "500", "700", "900"],
  subsets: ["latin"],
});

const { fontFamily: plexArFamily } = loadPlexAr("normal", {
  weights: ["400", "500", "700"],
  subsets: ["arabic"],
});

export const FONT_LATIN = interFamily;
export const FONT_ARABIC = plexArFamily;
