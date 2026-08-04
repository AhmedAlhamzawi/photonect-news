import React from "react";
import {
  AbsoluteFill, OffthreadVideo, Audio, Img, staticFile,
  interpolate, useCurrentFrame, useVideoConfig, Easing, spring,
} from "remotion";
import { TransitionSeries, linearTiming } from "@remotion/transitions";
import { fade } from "@remotion/transitions/fade";
import { loadFont } from "@remotion/google-fonts/Cairo";
import { z } from "zod";

const { fontFamily } = loadFont();
const TEAL = "#1FFCC1";
const CHAR = "#222931";
const EASE = Easing.bezier(0.16, 1, 0.3, 1);

export const tvcFlagshipSchema = z.object({
  hero: z.string().default("fedshi/tvc/hero.mp4"),
  bloom: z.string().default("fedshi/tvc/bloom.mp4"),
  icon: z.string().default("fedshi/brand/icon.png"),
  audio: z.string().default("audio/bed_pulse_syn.mp3"),
});
export type TVCFlagshipProps = z.infer<typeof tvcFlagshipSchema>;

const FPS = 30;
export const TVC_DUR = 426; // ~14.2s after transition overlaps

// caption that enters (up+fade) and exits (fade)
const Cap: React.FC<{ dur: number; children: React.ReactNode; bottom?: number }> = ({ dur, children, bottom = 230 }) => {
  const f = useCurrentFrame();
  const enter = interpolate(f, [0, 0.4 * FPS], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: EASE });
  const exit = interpolate(f, [dur - 0.3 * FPS, dur], [1, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  const y = interpolate(enter, [0, 1], [40, 0]);
  return (
    <div style={{ position: "absolute", left: 0, right: 0, bottom, padding: "0 70px", textAlign: "center", direction: "rtl", fontFamily, opacity: enter * exit, transform: `translateY(${y}px)` }}>
      {children}
    </div>
  );
};

const LogoBug: React.FC<{ icon: string }> = ({ icon }) => {
  const f = useCurrentFrame();
  const o = interpolate(f, [4, 20], [0, 0.92], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  return <Img src={staticFile(icon)} style={{ position: "absolute", top: 54, left: 50, width: 88, height: 88, borderRadius: 20, opacity: o }} />;
};

const bottomGrad = { position: "absolute" as const, inset: 0, background: `linear-gradient(to bottom, transparent 55%, ${CHAR}F2 100%)` };

// ── Scene 1: cold open ──────────────────────────────────────────────
const ColdOpen: React.FC<{ icon: string }> = ({ icon }) => {
  const f = useCurrentFrame();
  const s = spring({ frame: f, fps: FPS, config: { damping: 14, mass: 0.7 } });
  const scale = interpolate(s, [0, 1], [0.6, 1]);
  const glow = interpolate(f, [0, 30, 60], [0, 1, 0.7], { extrapolateRight: "clamp" });
  const textO = interpolate(f, [22, 40, 62, 72], [0, 1, 1, 0], { extrapolateRight: "clamp" });
  return (
    <AbsoluteFill style={{ backgroundColor: "#0C1013", alignItems: "center", justifyContent: "center", fontFamily }}>
      <div style={{ position: "absolute", width: 460, height: 460, borderRadius: "50%", background: TEAL, filter: "blur(120px)", opacity: 0.18 * glow }} />
      <Img src={staticFile(icon)} style={{ width: 220, height: 220, borderRadius: 44, transform: `scale(${scale})`, boxShadow: `0 0 60px ${TEAL}55` }} />
      <div style={{ position: "absolute", bottom: 640, color: "#fff", fontWeight: 800, fontSize: 62, opacity: textO, direction: "rtl" }}>الحياة صعبة 😮‍💨</div>
    </AbsoluteFill>
  );
};

// ── Scene 2: bloom (real footage) ───────────────────────────────────
const Bloom: React.FC<{ bloom: string; icon: string }> = ({ bloom, icon }) => (
  <AbsoluteFill style={{ backgroundColor: CHAR }}>
    <OffthreadVideo src={staticFile(bloom)} muted style={{ width: "100%", height: "100%", objectFit: "cover" }} />
    <AbsoluteFill style={bottomGrad} />
    <LogoBug icon={icon} />
    <Cap dur={96}><div style={{ color: TEAL, fontWeight: 900, fontSize: 82, textShadow: "0 6px 30px rgba(0,0,0,0.7)" }}>خلّيها تِضوّي 🌈</div></Cap>
  </AbsoluteFill>
);

// ── Scene 3: cinematic hero (Kie) ───────────────────────────────────
const Hero: React.FC<{ hero: string; icon: string }> = ({ hero, icon }) => {
  const f = useCurrentFrame();
  return (
    <AbsoluteFill style={{ backgroundColor: "#000" }}>
      <OffthreadVideo src={staticFile(hero)} muted style={{ width: "100%", height: "100%", objectFit: "cover" }} />
      <AbsoluteFill style={bottomGrad} />
      <LogoBug icon={icon} />
      {f < 110 ? (
        <Cap dur={110}><div style={{ color: "#fff", fontWeight: 800, fontSize: 74, textShadow: "0 6px 30px rgba(0,0,0,0.8)" }}>سبيكر كرستال يضوّي بالألوان</div></Cap>
      ) : (
        <div style={{ position: "absolute", inset: 0 }}>
          <div style={{ position: "absolute", left: 0, right: 0, bottom: 230, textAlign: "center", direction: "rtl", fontFamily }}>
            <div style={{ color: "#fff", fontWeight: 800, fontSize: 68, textShadow: "0 6px 30px rgba(0,0,0,0.8)", opacity: interpolate(f, [110, 128], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" }) }}>صوت خرافي 🔊 وإضاءة تغيّر جوّك 🔥</div>
          </div>
        </div>
      )}
    </AbsoluteFill>
  );
};

// ── Scene 4: end card ───────────────────────────────────────────────
const EndCard: React.FC<{ icon: string }> = ({ icon }) => {
  const f = useCurrentFrame();
  const pill = spring({ frame: f - 6, fps: FPS, config: { damping: 12 } });
  const o = interpolate(f, [0, 14], [0, 1], { extrapolateRight: "clamp" });
  return (
    <AbsoluteFill style={{ backgroundColor: CHAR, alignItems: "center", justifyContent: "center", fontFamily, direction: "rtl", opacity: o }}>
      <Img src={staticFile(icon)} style={{ width: 150, height: 150, borderRadius: 32, marginBottom: 34 }} />
      <div style={{ background: TEAL, color: "#08120F", fontWeight: 900, fontSize: 104, padding: "12px 60px", borderRadius: 30, transform: `scale(${interpolate(pill, [0, 1], [0.7, 1])})`, boxShadow: `0 14px 46px ${TEAL}55` }}>
        ٢٥,٠٠٠ <span style={{ fontSize: 48 }}>دينار</span>
      </div>
      <div style={{ color: "#fff", fontWeight: 700, fontSize: 46, marginTop: 26 }}>الدفع عند الاستلام ✅ · توصيل لكل العراق 🚗</div>
      <div style={{ color: TEAL, fontWeight: 900, fontSize: 72, marginTop: 30 }}>اطلب هسه 👇</div>
    </AbsoluteFill>
  );
};

export const TVCFlagship: React.FC<TVCFlagshipProps> = (p) => {
  const t = () => linearTiming({ durationInFrames: 12 });
  return (
    <AbsoluteFill style={{ backgroundColor: "#000" }}>
      <TransitionSeries>
        <TransitionSeries.Sequence durationInFrames={72}><ColdOpen icon={p.icon} /></TransitionSeries.Sequence>
        <TransitionSeries.Transition presentation={fade()} timing={t()} />
        <TransitionSeries.Sequence durationInFrames={96}><Bloom bloom={p.bloom} icon={p.icon} /></TransitionSeries.Sequence>
        <TransitionSeries.Transition presentation={fade()} timing={t()} />
        <TransitionSeries.Sequence durationInFrames={210}><Hero hero={p.hero} icon={p.icon} /></TransitionSeries.Sequence>
        <TransitionSeries.Transition presentation={fade()} timing={t()} />
        <TransitionSeries.Sequence durationInFrames={84}><EndCard icon={p.icon} /></TransitionSeries.Sequence>
      </TransitionSeries>
      <Audio src={staticFile(p.audio)} volume={0.7} />
    </AbsoluteFill>
  );
};
