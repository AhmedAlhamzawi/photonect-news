import React from "react";
import {
  AbsoluteFill, Audio, Sequence, staticFile,
  interpolate, spring, useCurrentFrame, useVideoConfig, Easing,
} from "remotion";
import { loadFont as loadCairo } from "@remotion/google-fonts/Cairo";
import { loadFont as loadPlexAr } from "@remotion/google-fonts/IBMPlexSansArabic";
import { FONT_LATIN } from "../PhotonectBrandReel/fonts";
import { ChatReelProps, ChatTurn } from "./schema";

// ── the chat-native visual system (tenant: Cha Dude) ────────────────────────
const INK = "#231F20";        // canvas ground — Photonect's own black
const INK_RAISED = "#2E2A2B"; // customer bubbles
const REPLY = "#24E07E";      // the signature: the agent replied
const AMBER = "#FDBB11";      // big numbers
const TEXT = "#F4F2F0";
const DIM = "#9A9491";
const DEAD = "#5C5654";       // the unanswered grey tick

const { fontFamily: CAIRO } = loadCairo("normal", { weights: ["800", "900"], subsets: ["arabic", "latin"] });
const { fontFamily: PLEX } = loadPlexAr("normal", { weights: ["400", "600"], subsets: ["arabic", "latin"] });


/** Header: avatar, name, "online" — reads as a real WhatsApp chat, not a poster. */
const Header: React.FC<{ name: string; letter: string; status: string; clock: string }> = ({ name, letter, status, clock }) => (
  <div style={{
    position: "absolute", top: 0, left: 0, right: 0, height: 200, background: "#1B1819",
    borderBottom: "1px solid #3A3536", direction: "rtl",
  }}>
    {/* status bar */}
    <div style={{ position: "absolute", top: 22, right: 44, left: 44, display: "flex", justifyContent: "space-between",
      fontFamily: FONT_LATIN, fontWeight: 600, fontSize: 30, color: TEXT }}>
      <span>{clock}</span>
      <span style={{ color: DIM, letterSpacing: 2 }}>●●●● ▲ 🔋</span>
    </div>
    <div style={{ position: "absolute", top: 82, right: 44, display: "flex", alignItems: "center", gap: 22 }}>
      <div style={{ width: 92, height: 92, borderRadius: 999, background: REPLY, display: "flex", alignItems: "center",
        justifyContent: "center", fontFamily: CAIRO, fontWeight: 900, fontSize: 54, color: INK, boxShadow: `0 0 0 5px ${INK}, 0 0 0 8px ${REPLY}` }}>
        {letter}
      </div>
      <div>
        <div style={{ fontFamily: CAIRO, fontWeight: 900, fontSize: 46, color: TEXT, lineHeight: 1.1 }}>{name}</div>
        <div style={{ fontFamily: PLEX, fontWeight: 400, fontSize: 28, color: REPLY, marginTop: 4, display: "flex", alignItems: "center", gap: 10 }}>
          <span style={{ width: 14, height: 14, borderRadius: 999, background: REPLY, display: "inline-block" }} />{status}
        </div>
      </div>
    </div>
  </div>
);

const TypingDots: React.FC = () => {
  const frame = useCurrentFrame();
  return (
    <div style={{ display: "flex", gap: 10, padding: "6px 4px" }}>
      {[0, 1, 2].map((i) => {
        const o = 0.35 + 0.65 * Math.max(0, Math.sin((frame / 6) - i * 0.9));
        return <span key={i} style={{ width: 16, height: 16, borderRadius: 999, background: DIM, opacity: o, display: "inline-block" }} />;
      })}
    </div>
  );
};

const Bubble: React.FC<{ t: ChatTurn }> = ({ t }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const isAgent = t.who === "agent";
  const typing = isAgent && t.typingF > 0 && frame >= t.startF - t.typingF && frame < t.startF;
  if (frame < t.startF - (isAgent ? t.typingF : 0)) return null;

  if (t.who === "divider") {
    const o = interpolate(frame, [t.startF, t.startF + 8], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
    return (
      <div style={{ alignSelf: "center", margin: "26px 0", opacity: o, background: "#3A3536", color: TEXT,
        fontFamily: CAIRO, fontWeight: 800, fontSize: 34, padding: "10px 28px", borderRadius: 999 }}>{t.text}</div>
    );
  }

  const s = typing ? 1 : spring({ frame: frame - t.startF, fps, config: { damping: 14, stiffness: 190, mass: 0.6 } });
  const ticked = frame >= t.startF + 12;
  return (
    <div style={{
      alignSelf: isAgent ? "flex-start" : "flex-end",
      maxWidth: "78%", margin: "12px 0",
      transform: `scale(${0.85 + 0.15 * s}) translateY(${(1 - s) * 14}px)`,
      transformOrigin: isAgent ? "left bottom" : "right bottom",
      opacity: typing ? 1 : Math.min(1, s * 1.3),
      position: "relative",
    }}>
      {isAgent && !typing && t.latencyS !== undefined ? (
        <div style={{ position: "absolute", top: -22, left: 10, background: INK, border: `2px solid ${REPLY}`, color: REPLY,
          fontFamily: PLEX, fontWeight: 600, fontSize: 24, padding: "2px 14px", borderRadius: 999, whiteSpace: "nowrap" }}>
          ⚡ {t.latencyS < 0.05 ? "فوراً" : `${t.latencyS.toFixed(1)} ث`}
        </div>
      ) : null}
      <div style={{
        background: isAgent ? REPLY : INK_RAISED, color: isAgent ? "#0A1F14" : TEXT,
        borderRadius: 26, borderBottomLeftRadius: isAgent ? 6 : 26, borderBottomRightRadius: isAgent ? 26 : 6,
        padding: typing ? "14px 22px" : "18px 26px 30px",
        fontFamily: PLEX, fontWeight: 400, fontSize: 36, lineHeight: 1.5, direction: "rtl", textAlign: "right",
        whiteSpace: "pre-wrap", boxShadow: "0 6px 18px rgba(0,0,0,.35)",
      }}>
        {typing ? <TypingDots /> : t.text}
        {!typing ? (
          <div style={{ position: "absolute", bottom: 8, left: 18, display: "flex", gap: 8, alignItems: "center",
            fontFamily: FONT_LATIN, fontSize: 22, color: isAgent ? "#0A1F14aa" : DIM }}>
            <span>{t.time}</span>
            {!isAgent ? <span style={{ color: t.unanswered ? DEAD : (ticked ? "#53BDEB" : DIM), fontSize: 24, letterSpacing: -6 }}>
              {t.unanswered ? "✓" : "✓✓"}
            </span> : null}
          </div>
        ) : null}
      </div>
    </div>
  );
};

/** Big stopwatch during the first reply window — the research's proof device. */
const Stopwatch: React.FC<{ t: ChatTurn }> = ({ t }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const start = t.startF - t.typingF;
  if (frame < start || frame > t.startF + 40) return null;
  const secs = Math.min((frame - start) / fps, t.latencyS ?? 0);
  const landed = frame >= t.startF;
  const fade = interpolate(frame, [t.startF + 20, t.startF + 40], [1, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  return (
    <div style={{ position: "absolute", top: 232, left: 0, right: 0, textAlign: "center", opacity: fade }}>
      <div style={{ display: "inline-block", background: landed ? REPLY : "#1B1819", color: landed ? INK : TEXT,
        border: `3px solid ${REPLY}`, borderRadius: 999, padding: "8px 34px", fontFamily: FONT_LATIN, fontWeight: 800,
        fontSize: 44, letterSpacing: 1 }}>
        ⏱ {secs.toFixed(1)} ث
      </div>
    </div>
  );
};

const Hook: React.FC<{ text: string; frames: number }> = ({ text, frames }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const inS = spring({ frame, fps, config: { damping: 16, stiffness: 160 } });
  const out = interpolate(frame, [frames - 12, frames], [1, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  if (frame > frames) return null;
  return (
    <div style={{ position: "absolute", top: 240, left: 60, right: 60, textAlign: "center", direction: "rtl",
      opacity: Math.min(1, inS * 1.2) * out, transform: `translateY(${(1 - inS) * 30}px)` }}>
      <div style={{ display: "inline-block", background: AMBER, color: INK, fontFamily: CAIRO, fontWeight: 900,
        fontSize: 64, lineHeight: 1.25, padding: "18px 34px", borderRadius: 18, boxShadow: "0 14px 40px rgba(0,0,0,.5)" }}>
        {text}
      </div>
    </div>
  );
};

const EndCard: React.FC<{ p: ChatReelProps }> = ({ p }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = interpolate(frame, [0, 12], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.out(Easing.cubic) });
  const num = spring({ frame: frame - 10, fps, config: { damping: 12, stiffness: 140 } });
  return (
    <AbsoluteFill style={{ background: INK, opacity: t }}>
      <div style={{ position: "absolute", inset: 0, display: "flex", flexDirection: "column", alignItems: "center",
        justifyContent: "center", gap: 30, padding: "0 80px", direction: "rtl", textAlign: "center" }}>
        <div style={{ fontFamily: CAIRO, fontWeight: 900, fontSize: 74, color: TEXT, lineHeight: 1.25 }}>{p.endcard.title}</div>
        {p.endcard.sub ? <div style={{ fontFamily: PLEX, fontWeight: 400, fontSize: 36, color: DIM }}>{p.endcard.sub}</div> : null}
        <div style={{ transform: `scale(${0.8 + 0.2 * num})`, background: REPLY, color: INK, borderRadius: 24, padding: "22px 46px",
          fontFamily: FONT_LATIN, fontWeight: 900, fontSize: 76, letterSpacing: 2, direction: "ltr" }}>
          {p.endcard.number}
        </div>
        {p.endcard.cta ? <div style={{ fontFamily: CAIRO, fontWeight: 800, fontSize: 40, color: AMBER, marginTop: 8 }}>{p.endcard.cta}</div> : null}
        <div style={{ marginTop: 26, display: "flex", alignItems: "center", gap: 14 }}>
          <div style={{ width: 12, height: 12, borderRadius: 8, background: "#D72638" }} />
          <span style={{ fontFamily: FONT_LATIN, fontWeight: 900, fontSize: 30, letterSpacing: 3, color: TEXT }}>PHOTONECT</span>
        </div>
        {p.endcard.small ? <div style={{ fontFamily: PLEX, fontSize: 24, color: DEAD, marginTop: 6 }}>{p.endcard.small}</div> : null}
      </div>
    </AbsoluteFill>
  );
};

export const ChatReel: React.FC<ChatReelProps> = (p) => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  const firstAgent = p.turns.find((t) => t.who === "agent" && t.typingF > 0);
  const inChat = frame < p.endcardStartF;

  return (
    <AbsoluteFill style={{ backgroundColor: INK }}>
      {p.voClips.map((c, i) => <Sequence key={i} from={c.atF}><Audio src={staticFile(c.src)} /></Sequence>)}
      {p.bed ? (
        <Audio src={staticFile(p.bed)} loop volume={(f) =>
          interpolate(f, [0, 20, durationInFrames - 30, durationInFrames], [0, p.bedVolume, p.bedVolume, 0],
            { extrapolateLeft: "clamp", extrapolateRight: "clamp" })} />
      ) : null}
      {p.sfx ? p.turns.filter((t) => t.who !== "divider").map((t, i) => (
        <Sequence key={`s${i}`} from={t.startF}>
          <Audio src={staticFile(t.who === "agent" ? "sfx/pop_out.wav" : "sfx/pop_in.wav")} volume={0.7} />
        </Sequence>
      )) : null}

      {inChat ? (
        <>
          {/* chat area — newest at the bottom, oldest scroll off the top like a real live chat */}
          <div style={{ position: "absolute", top: 200, left: 0, right: 0, bottom: 150, overflow: "hidden",
            backgroundImage: "radial-gradient(circle at 1px 1px, rgba(255,255,255,0.035) 1px, transparent 1.6px)", backgroundSize: "26px 26px" }}>
            <div style={{ position: "absolute", left: 40, right: 40, bottom: 20, display: "flex", flexDirection: "column", justifyContent: "flex-end" }}>
              {p.turns.map((t, i) => <Bubble key={i} t={t} />)}
            </div>
          </div>
          {/* input bar */}
          <div style={{ position: "absolute", left: 0, right: 0, bottom: 0, height: 150, background: "#1B1819", borderTop: "1px solid #3A3536",
            display: "flex", alignItems: "center", padding: "0 40px", gap: 20, direction: "rtl" }}>
            <div style={{ flex: 1, height: 84, borderRadius: 999, background: INK_RAISED, display: "flex", alignItems: "center",
              padding: "0 30px", fontFamily: PLEX, fontSize: 30, color: DIM }}>رسالة</div>
            <div style={{ width: 84, height: 84, borderRadius: 999, background: REPLY, display: "flex", alignItems: "center", justifyContent: "center", fontSize: 36 }}>🎤</div>
          </div>
          <Header name={p.contactName} letter={p.avatarLetter} status={p.statusLine} clock={p.clockLabel} />
          {p.stopwatchOnFirst && firstAgent ? <Stopwatch t={firstAgent} /> : null}
          <Hook text={p.hook} frames={p.hookFrames} />
        </>
      ) : null}

      <Sequence from={p.endcardStartF} durationInFrames={Math.max(1, p.totalFrames - p.endcardStartF)} name="endcard">
        <EndCard p={p} />
      </Sequence>
    </AbsoluteFill>
  );
};
