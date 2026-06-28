import React from "react";
import {
  AbsoluteFill,
  Audio,
  OffthreadVideo,
  Sequence,
  staticFile,
  interpolate,
  useCurrentFrame,
  useVideoConfig,
  Easing,
} from "remotion";
import { FONT_ARABIC, FONT_LATIN } from "../PhotonectBrandReel/fonts";
import { GrainOverlay, Vignette } from "../PhotonectBrandReel/GrainOverlay";
import { EqBars } from "./EqBars";
import {
  EssayProps,
  EssaySegment,
  EssayCounter,
  ESSAY_TRANSITION_FRAMES,
  computeEssayDuration,
} from "./schema";

const C = {
  ink: "#08080C",
  yellow: "#FFC217",
  red: "#D72638",
  paper: "#F6F6F1",
};
const TONE: Record<string, string> = { cyan: "#36E0FF", amber: "#FFC217", red: "#D72638" };

// Back-to-back starts with a one-dissolve overlap between neighbours.
const segmentStarts = (segs: EssaySegment[]): number[] => {
  const starts: number[] = [];
  let cur = 0;
  for (const s of segs) {
    starts.push(cur);
    cur += s.durationFrames - ESSAY_TRANSITION_FRAMES;
  }
  return starts;
};

// ── Persistent top brand strip ───────────────────────────────────────────────
const TopStrip: React.FC<{ kicker: string; titleArabic: string; dateLabel: string }> = ({
  kicker,
  titleArabic,
  dateLabel,
}) => {
  const frame = useCurrentFrame();
  const pulse = 0.55 + 0.45 * Math.abs(Math.sin(frame / 14));
  return (
    <div
      style={{
        position: "absolute",
        top: 0,
        left: 0,
        right: 0,
        padding: "46px 54px 70px",
        background: "linear-gradient(to bottom, rgba(8,8,12,0.92) 0%, rgba(8,8,12,0.0) 100%)",
        display: "flex",
        alignItems: "center",
        justifyContent: "space-between",
        zIndex: 30,
      }}
    >
      <div style={{ display: "flex", alignItems: "center", gap: 16 }}>
        <div
          style={{
            width: 16,
            height: 16,
            borderRadius: 8,
            background: C.red,
            boxShadow: `0 0 ${10 + pulse * 14}px ${C.red}`,
            opacity: pulse,
          }}
        />
        <div
          style={{
            fontFamily: FONT_LATIN,
            fontWeight: 900,
            fontSize: 30,
            letterSpacing: 4,
            color: C.paper,
          }}
        >
          PHOTONECT
          <span style={{ color: C.yellow }}> ·</span>
        </div>
        <div
          style={{
            fontFamily: FONT_ARABIC,
            fontWeight: 800,
            fontSize: 30,
            color: C.yellow,
          }}
        >
          {kicker}
        </div>
      </div>
      <div
        style={{
          fontFamily: FONT_LATIN,
          fontWeight: 700,
          fontSize: 22,
          letterSpacing: 2,
          color: "rgba(246,246,241,0.6)",
        }}
      >
        {dateLabel}
      </div>
    </div>
  );
};

// ── Sourced number counters for a beat ──────────────────────────────────────
const CounterChips: React.FC<{ counters: EssayCounter[]; localFrame: number }> = ({
  counters,
  localFrame,
}) => {
  return (
    <div
      style={{
        display: "flex",
        flexWrap: "wrap",
        gap: 14,
        justifyContent: "center",
        marginBottom: 26,
        direction: "rtl",
      }}
    >
      {counters.map((c, i) => {
        const appear = interpolate(localFrame, [8 + i * 7, 22 + i * 7], [0, 1], {
          extrapolateLeft: "clamp",
          extrapolateRight: "clamp",
          easing: Easing.out(Easing.cubic),
        });
        return (
          <div
            key={i}
            style={{
              transform: `translateY(${(1 - appear) * 18}px)`,
              opacity: appear,
              background: "rgba(8,8,12,0.66)",
              border: `1.5px solid ${C.yellow}`,
              borderRadius: 14,
              padding: "12px 18px",
              backdropFilter: "blur(6px)",
              maxWidth: 440,
            }}
          >
            <div
              style={{
                fontFamily: FONT_LATIN,
                fontWeight: 900,
                fontSize: 34,
                color: C.yellow,
                lineHeight: 1.05,
                direction: "ltr",
                textAlign: "center",
              }}
            >
              {c.value}
            </div>
            <div
              style={{
                fontFamily: FONT_ARABIC,
                fontWeight: 500,
                fontSize: 17,
                color: "rgba(246,246,241,0.92)",
                marginTop: 3,
                textAlign: "center",
              }}
            >
              {c.label_ar}
            </div>
            <div
              style={{
                fontFamily: FONT_LATIN,
                fontWeight: 600,
                fontSize: 12,
                color: "rgba(246,246,241,0.5)",
                marginTop: 4,
                direction: "ltr",
                textAlign: "center",
              }}
            >
              {c.source}
              {c.as_of ? ` · ${c.as_of}` : ""}
            </div>
          </div>
        );
      })}
    </div>
  );
};

// ── Cycling RTL caption (pairs of bars advance across the beat) ──────────────
const Caption: React.FC<{ text: string; durationFrames: number; localFrame: number }> = ({
  text,
  durationFrames,
  localFrame,
}) => {
  const lines = text.split(" / ").map((l) => l.trim()).filter(Boolean);
  // group into pairs
  const groups: string[][] = [];
  for (let i = 0; i < lines.length; i += 2) groups.push(lines.slice(i, i + 2));
  const usable = durationFrames - ESSAY_TRANSITION_FRAMES;
  const groupDur = usable / groups.length;
  const idx = Math.min(groups.length - 1, Math.max(0, Math.floor(localFrame / groupDur)));
  const within = localFrame - idx * groupDur;
  const fade = interpolate(
    within,
    [0, 10, groupDur - 10, groupDur],
    [0, 1, 1, 0],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" },
  );
  const group = groups[idx] ?? [];
  return (
    <div style={{ minHeight: 150, display: "flex", flexDirection: "column", justifyContent: "center", gap: 8 }}>
      {group.map((ln, i) => (
        <div
          key={`${idx}-${i}`}
          style={{
            fontFamily: FONT_ARABIC,
            fontWeight: 800,
            fontSize: 46,
            lineHeight: 1.35,
            color: C.paper,
            textAlign: "center",
            direction: "rtl",
            opacity: fade,
            textShadow: "0 3px 22px rgba(0,0,0,0.95)",
          }}
        >
          {ln}
        </div>
      ))}
    </div>
  );
};

// ── One beat: full-bleed video + scrim + counters + caption, cross-dissolved ─
const SegmentLayer: React.FC<{ seg: EssaySegment; isFirst: boolean; isLast: boolean }> = ({
  seg,
  isFirst,
  isLast,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const T = ESSAY_TRANSITION_FRAMES;
  const fadeIn = isFirst ? 1 : interpolate(frame, [0, T], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  const fadeOut = isLast
    ? 1
    : interpolate(frame, [seg.durationFrames - T, seg.durationFrames], [1, 0], {
        extrapolateLeft: "clamp",
        extrapolateRight: "clamp",
      });
  const opacity = fadeIn * fadeOut;
  const scale = interpolate(frame, [0, seg.durationFrames], [1.04, 1.13], { extrapolateRight: "clamp" });
  // stretch the source clip to fill the beat (slow-mo hides AI seams)
  const playbackRate = Math.max(0.2, (seg.brollSeconds * fps) / seg.durationFrames);
  // Duck the per-beat vocal at the cross-dissolve seams so neighbours don't double up.
  const voVol = (f: number) => {
    const fi = isFirst ? 1 : interpolate(f, [0, T], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
    const fo = isLast ? 1 : interpolate(f, [seg.durationFrames - T, seg.durationFrames], [1, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
    return Math.max(0, fi * fo);
  };

  return (
    <AbsoluteFill style={{ opacity, backgroundColor: C.ink }}>
      {seg.vo ? (
        <Audio src={staticFile(seg.vo)} startFrom={Math.round(seg.voLeadIn * fps)} volume={voVol} />
      ) : null}
      <AbsoluteFill style={{ transform: `scale(${scale})` }}>
        <OffthreadVideo
          src={staticFile(seg.broll)}
          muted
          playbackRate={playbackRate}
          style={{ width: "100%", height: "100%", objectFit: "cover" }}
        />
      </AbsoluteFill>
      {/* bottom scrim */}
      <div
        style={{
          position: "absolute",
          bottom: 0,
          left: 0,
          right: 0,
          height: "58%",
          background:
            "linear-gradient(to top, rgba(8,8,12,0.96) 0%, rgba(8,8,12,0.82) 42%, rgba(8,8,12,0.0) 100%)",
        }}
      />
      {/* content in lower band */}
      <div
        style={{
          position: "absolute",
          bottom: 168,
          left: 0,
          right: 0,
          padding: "0 56px",
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
        }}
      >
        <CounterChips counters={seg.counters} localFrame={frame} />
        <Caption text={seg.arabic_vo} durationFrames={seg.durationFrames} localFrame={frame} />
      </div>
    </AbsoluteFill>
  );
};

// ── EQ layer: picks the active beat's tone from the global frame ─────────────
const EqLayer: React.FC<{ audioSrc: string; segs: EssaySegment[] }> = ({ audioSrc, segs }) => {
  const frame = useCurrentFrame();
  const starts = segmentStarts(segs);
  let active = 0;
  for (let i = 0; i < starts.length; i++) if (frame >= starts[i]) active = i;
  const tone = (segs[active]?.eq_tone ?? "cyan") as "cyan" | "amber" | "red";
  return (
    <div style={{ position: "absolute", bottom: 64, left: 0, right: 0, zIndex: 20, opacity: 0.92 }}>
      <EqBars audioSrc={audioSrc} tone={tone} />
    </div>
  );
};

export const Essay: React.FC<EssayProps> = (props) => {
  const { durationInFrames } = useVideoConfig();
  const { segments, audio, musicBed, musicBedVolume, audioFadeOutFrames } = props;
  const starts = segmentStarts(segments);
  const bedSrc = musicBed || audio;
  // Bed sits low under the per-beat vocals; if it's the ONLY track (no per-beat vo
  // yet), play it full so the render isn't near-silent.
  const hasVo = segments.some((s) => s.vo);
  const bedVol = hasVo ? musicBedVolume : 1;

  return (
    <AbsoluteFill style={{ backgroundColor: C.ink }}>
      <Audio
        src={staticFile(bedSrc)}
        loop
        volume={(f) =>
          interpolate(
            f,
            [0, 20, durationInFrames - audioFadeOutFrames, durationInFrames],
            [0, bedVol, bedVol, 0],
            { extrapolateLeft: "clamp", extrapolateRight: "clamp" },
          )
        }
      />

      {segments.map((seg, i) => (
        <Sequence key={i} from={starts[i]} durationInFrames={seg.durationFrames} name={seg.beat_role}>
          <SegmentLayer seg={seg} isFirst={i === 0} isLast={i === segments.length - 1} />
        </Sequence>
      ))}

      <EqLayer audioSrc={bedSrc} segs={segments} />

      <TopStrip kicker={props.kicker} titleArabic={props.titleArabic} dateLabel={props.dateLabel} />

      {/* persistent handle */}
      <div
        style={{
          position: "absolute",
          bottom: 30,
          right: 54,
          fontFamily: FONT_LATIN,
          fontWeight: 700,
          fontSize: 20,
          letterSpacing: 1,
          color: "rgba(246,246,241,0.55)",
          zIndex: 30,
        }}
      >
        {props.handle}
      </div>

      <Vignette />
      <GrainOverlay />
    </AbsoluteFill>
  );
};

export { computeEssayDuration };
