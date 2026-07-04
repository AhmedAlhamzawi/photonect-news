import type { BrandTravelReelProps } from "./schema";

const IMG = "images/news/2026-06-28-sindibad-iraq";

// Sindibad brand kit: crimson #CD0037, cream, sand, Cairo font.
// Copy register: regional MSA with light warmth (audience is pan-Arab, not
// Iraqi-only) — no heavy colloquial in the public on-screen text.
export const SINDIBAD_TRAVEL_PROPS: BrandTravelReelProps = {
  brand: {
    name: "السندباد",
    crimson: "#CD0037",
    cream: "#FFFCFA",
    sand: "#E8C994",
    ink: "#1A0610",
    logo: "brand/sindibad-logo.svg",
    handle: "sindibad.iq",
  },
  audio: "audio/music_01.mp3",
  intro: {
    image: `${IMG}/hero.jpg`,
    kicker: "اكتشف العراق",
    hook: "العراق أكبر\nمن بغداد وأربيل",
    subhead: "وجهات ساحرة تستحق الزيارة",
  },
  destinations: [
    {
      image: `${IMG}/broll_1.jpg`,
      index: "01",
      tag: "طبيعة جبلية",
      name: "حلبجة",
      descriptor: "جبال خضراء وشلالات في الربيع",
    },
    {
      image: `${IMG}/broll_2.jpg`,
      index: "02",
      tag: "تراث عالمي",
      name: "أهوار الجنوب",
      descriptor: "على ضفاف الماء، إرث يمتد لآلاف السنين",
    },
    {
      image: `${IMG}/broll_3.jpg`,
      index: "03",
      tag: "تاريخ حيّ",
      name: "قلعة أربيل",
      descriptor: "من أقدم المدن المأهولة في العالم",
    },
    {
      image: `${IMG}/broll_alt_bekhal.jpg`,
      index: "04",
      tag: "وجهة منعشة",
      name: "شلالات بيخال",
      descriptor: "هدير الماء بين صخور الجبل",
    },
  ],
  outro: {
    headline: "رحلتك تبدأ من هنا",
    subline: "قارن واحجز بثقة — أوثق منصة سفر في العراق",
  },
};
