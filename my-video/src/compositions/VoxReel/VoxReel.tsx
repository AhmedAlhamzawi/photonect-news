import React from "react";
import {
  AbsoluteFill, Audio, Img, Sequence, staticFile,
  interpolate, useCurrentFrame, useVideoConfig, Easing,
} from "remotion";
import { FONT_ARABIC, FONT_LATIN } from "../PhotonectBrandReel/fonts";
import { VoxReelProps, VoxBlock, VOX_ENDCARD_F } from "./schema";
import { PaperTexture, Marker, Bars, Redaction, ThroughLine, pop } from "./VoxKit";

const INK = "#0A0A10";
const Y = "#FFC217";
const R = "#D72638";
const PAPER = "#F6F1E4";

/** One narration block: flat colour field + collage art + Vox devices. */
const Block: React.FC<{ b: VoxBlock; isFirst: boolean }> = ({ b, isFirst }) => {
  const frame = useCurrentFrame();
  const D = b.durationF;

  // whip-in at the block boundary — hard cuts read as one continuous piece
  const whip = isFirst
    ? 1
    : interpolate(frame, [0, 7], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.out(Easing.cubic) });
  const whipX = isFirst ? 0 : interpolate(frame, [0, 7], [9, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.out(Easing.cubic) });

  // slow deliberate camera push + lateral parallax drift
  const push = interpolate(frame, [0, D], [1, 1 + b.pushIn], { extrapolateRight: "clamp" });
  const drift = interpolate(frame, [0, D], [0, b.driftX * 100], { extrapolateRight: "clamp" });

  // the collage art itself pops in with overshoot, like a pasted cutout
  const artPop = pop(frame, 2, 13);

  return (
    <AbsoluteFill style={{ backgroundColor: b.bg, opacity: whip, transform: `translateX(${whipX}%)` }}>
      {/* flat colour field + the escalating through-line motif behind the art */}
      <AbsoluteFill style={{ opacity: 0.5 }}>
        <ThroughLine level={b.throughline} color={R} />
      </AbsoluteFill>

      {/* the collage art, framed as a pasted paper cutout */}
      <AbsoluteFill style={{ transform: `scale(${push}) translateX(${drift}px)` }}>
        <div
          style={{
            position: "absolute",
            left: "50%", top: "48%",
            width: "88%",
            transform: `translate(-50%,-50%) scale(${0.94 + artPop * 0.06}) rotate(${(1 - artPop) * -1.2}deg)`,
            opacity: Math.min(1, artPop * 1.5),
            padding: "1.4%",
            background: "#FCFAF4",
            boxShadow: "0 26px 54px rgba(0,0,0,0.30)",
          }}
        >
          <Img src={staticFile(b.collage)} style={{ width: "100%", display: "block" }} />
        </div>
      </AbsoluteFill>

      {/* Vox devices drawn over the collage */}
      {b.bars ? (
        <Bars values={b.bars.values} x={b.bars.x} y={b.bars.y} w={b.bars.w} h={b.bars.h}
              atFrame={b.bars.atFrame} color={b.bars.color} />
      ) : null}
      {b.annotations.map((a, i) => (
        <Marker key={i} kind={a.kind} x={a.x} y={a.y} w={a.w} h={a.h}
                atFrame={a.atFrame} drawFrames={a.drawFrames} color={a.color} />
      ))}

      <PaperTexture opacity={0.55} />
    </AbsoluteFill>
  );
};

/** Word-synced karaoke captions — our upgrade over Vox's burned subtitles. */
const Captions: React.FC<{ p: VoxReelProps }> = ({ p }) => {
  const frame = useCurrentFrame();
  const line = p.lines.find((l) => frame >= l.startF && frame < l.endF + 5);
  if (!line) return null;
  const appear = interpolate(frame, [line.startF, line.startF + 4], [0, 1], {
    extrapolateLeft: "clamp", extrapolateRight: "clamp",
  });
  return (
    <div style={{
      position: "absolute", bottom: 190, left: 46, right: 46,
      textAlign: "center", direction: "rtl", opacity: appear,
    }}>
      <div style={{
        display: "inline-block", background: INK,
        padding: "16px 24px", boxShadow: "0 12px 30px rgba(0,0,0,.4)",
      }}>
        {line.words.map((w, i) => {
          const on = frame >= w.startF && frame < w.endF + 2;
          return (
            <span key={i} style={{
              fontFamily: FONT_ARABIC, fontWeight: 900, fontSize: 54, lineHeight: 1.45,
              margin: "0 11px", display: "inline-block",
              color: on ? Y : "#F6F1E4",
              transform: on ? "scale(1.07)" : "scale(1)",
            }}>{w.word}</span>
          );
        })}
      </div>
    </div>
  );
};

export const VoxReel: React.FC<VoxReelProps> = (props) => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  const endStart = props.totalFrames - VOX_ENDCARD_F;

  return (
    <AbsoluteFill style={{ backgroundColor: PAPER }}>
      <Audio src={staticFile(props.vo)} />
      {props.audioBed ? (
        <Audio src={staticFile(props.audioBed)} loop volume={(f) =>
          interpolate(f, [0, 20, durationInFrames - 40, durationInFrames],
            [0, props.bedVolume, props.bedVolume, 0],
            { extrapolateLeft: "clamp", extrapolateRight: "clamp" })} />
      ) : null}

      {props.blocks.map((b, i) => (
        <Sequence key={i} from={b.startF} durationInFrames={b.durationF} name={`block-${i + 1}`}>
          <Block b={b} isFirst={i === 0} />
        </Sequence>
      ))}

      {frame < endStart ? <Captions p={props} /> : null}

      {/* persistent brand chip */}
      <div style={{
        position: "absolute", top: 44, right: 46,
        display: "flex", alignItems: "center", gap: 10,
        background: INK, padding: "9px 16px",
      }}>
        <div style={{ width: 11, height: 11, borderRadius: 8, background: R }} />
        <span style={{ fontFamily: FONT_LATIN, fontWeight: 900, fontSize: 21, letterSpacing: 2, color: "#F6F1E4" }}>
          PHOTONECT
        </span>
      </div>

      {/* end card */}
      <Sequence from={endStart} durationInFrames={VOX_ENDCARD_F} name="end">
        <EndCard p={props} />
      </Sequence>
    </AbsoluteFill>
  );
};

const EndCard: React.FC<{ p: VoxReelProps }> = ({ p }) => {
  const frame = useCurrentFrame();
  const t = interpolate(frame, [0, 10], [0, 1], {
    extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.out(Easing.cubic),
  });
  return (
    <AbsoluteFill style={{ background: INK, opacity: t }}>
      <div style={{
        position: "absolute", inset: 0, display: "flex", flexDirection: "column",
        alignItems: "center", justifyContent: "center", gap: 34, padding: "0 70px",
      }}>
        <div style={{
          fontFamily: FONT_ARABIC, fontWeight: 900, fontSize: 66, color: "#F6F1E4",
          textAlign: "center", direction: "rtl", lineHeight: 1.45,
        }}>{p.endQuestion}</div>
        <div style={{ width: 120, height: 7, background: Y }} />
        <div style={{ fontFamily: FONT_ARABIC, fontWeight: 700, fontSize: 30, color: Y, direction: "rtl" }}>
          شاركنا رأيك بالتعليقات 👇
        </div>
        <div style={{ marginTop: 16, display: "flex", alignItems: "center", gap: 14 }}>
          <div style={{ width: 13, height: 13, borderRadius: 8, background: R }} />
          <span style={{ fontFamily: FONT_LATIN, fontWeight: 900, fontSize: 32, letterSpacing: 3, color: "#F6F1E4" }}>
            PHOTONECT
          </span>
          <span style={{ fontFamily: FONT_LATIN, fontWeight: 600, fontSize: 23, color: "rgba(246,241,228,.6)" }}>
            {p.handle}
          </span>
        </div>
        {p.sourcesLine ? (
          <div style={{ fontFamily: FONT_ARABIC, fontSize: 21, color: "rgba(246,241,228,.5)", direction: "rtl", textAlign: "center" }}>
            {p.sourcesLine}
          </div>
        ) : null}
      </div>
    </AbsoluteFill>
  );
};
