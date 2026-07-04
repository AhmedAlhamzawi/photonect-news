import type { TravelReelMotionProps } from "./schema";

const C = "clips/sindibad-iraq";

export const SINDIBAD_MOTION_PROPS: TravelReelMotionProps = {
  brand: {
    name: "السندباد",
    crimson: "#CD0037",
    cream: "#FFFCFA",
    ink: "#1A0610",
    logo: "brand/sindibad-logo.svg",
    handle: "sindibad.iq",
  },
  audio: "audio/mood_mideast.mp3",
  audioStartFrom: 0,
  hook: {
    clip: `${C}/hero.mp4`,
    startFrom: 14,
    line1: "العراق",
    line2: "أجمل مما تتخيّل",
    save: "احفظ للرحلة القادمة 📌",
  },
  scenes: [
    { clip: `${C}/marsh.mp4`, startFrom: 26, name: "أهوار الجنوب", tag: "تراث عالمي" },
    { clip: `${C}/waterfall.mp4`, startFrom: 18, name: "جبال كردستان", tag: "طبيعة خلّابة" },
    { clip: `${C}/citadel.mp4`, startFrom: 16, name: "قلعة أربيل", tag: "تاريخ حيّ" },
    { clip: `${C}/gorge.mp4`, startFrom: 24, name: "وديان الشمال", tag: "هواء وماء" },
  ],
  outro: {
    headline: "رحلتك تبدأ من هنا",
    subline: "قارن واحجز بثقة عبر السندباد",
  },
};
