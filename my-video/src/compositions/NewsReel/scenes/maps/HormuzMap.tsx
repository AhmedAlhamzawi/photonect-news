import React from "react";
import { interpolate, useCurrentFrame, Easing } from "remotion";
import { PHOTONECT } from "../../../PhotonectBrandReel/brand";
import { FONT_ARABIC, FONT_LATIN } from "../../../PhotonectBrandReel/fonts";

type Props = { accent: string };

export const HormuzMap: React.FC<Props> = ({ accent }) => {
  const frame = useCurrentFrame();

  const r = (s: number, e: number, sf: number, ef: number) =>
    interpolate(frame, [sf, ef], [s, e], {
      easing: Easing.bezier(0.16, 1, 0.3, 1),
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    });

  const mapReveal = r(0, 1, 0, 30);
  const perimeterDash = r(1800, 0, 20, 90);
  const shipX = r(-60, 420, 40, 200);
  const pulse = Math.sin(frame * 0.22) * 0.4 + 0.6;

  return (
    <div
      style={{
        width: 640,
        height: 360,
        position: "relative",
        opacity: mapReveal,
        transform: `translateY(${(1 - mapReveal) * 20}px)`,
      }}
    >
      <svg
        viewBox="0 0 640 360"
        width="640"
        height="360"
        style={{ position: "absolute", inset: 0 }}
      >
        <defs>
          <linearGradient id="sea" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#0A1628" />
            <stop offset="100%" stopColor="#051018" />
          </linearGradient>
          <radialGradient id="hotspot" cx="50%" cy="50%">
            <stop offset="0%" stopColor={accent} stopOpacity="0.45" />
            <stop offset="100%" stopColor={accent} stopOpacity="0" />
          </radialGradient>
        </defs>

        {/* Sea */}
        <rect width="640" height="360" fill="url(#sea)" />

        {/* Iran coast (north) */}
        <path
          d="M 0,60 L 110,55 L 180,72 L 260,50 L 360,60 L 460,40 L 560,55 L 640,45 L 640,0 L 0,0 Z"
          fill="#1a2a1e"
          stroke={accent}
          strokeWidth="1.5"
          opacity="0.85"
        />
        <text
          x="120"
          y="40"
          fill={accent}
          fontFamily={FONT_LATIN}
          fontSize="18"
          fontWeight="900"
          letterSpacing="3"
        >
          IRAN
        </text>

        {/* Oman/UAE coast (south) */}
        <path
          d="M 0,300 L 90,310 L 180,295 L 280,320 L 380,310 L 480,330 L 580,315 L 640,325 L 640,360 L 0,360 Z"
          fill="#2a1f12"
          stroke="#d4a76a"
          strokeWidth="1.5"
          opacity="0.85"
        />
        <text
          x="80"
          y="345"
          fill="#d4a76a"
          fontFamily={FONT_LATIN}
          fontSize="14"
          fontWeight="900"
          letterSpacing="2"
        >
          OMAN • UAE
        </text>

        {/* Strait narrowest point marker */}
        <line
          x1="320"
          y1="80"
          x2="320"
          y2="300"
          stroke={accent}
          strokeWidth="1"
          strokeDasharray="4 6"
          opacity="0.4"
        />
        <text
          x="322"
          y="200"
          fill={PHOTONECT.paper}
          fontFamily={FONT_LATIN}
          fontSize="11"
          fontWeight="700"
          letterSpacing="2"
          opacity="0.6"
        >
          STRAIT OF HORMUZ
        </text>

        {/* Blockade perimeter — animated dash */}
        <ellipse
          cx="320"
          cy="190"
          rx="110"
          ry="60"
          fill="none"
          stroke={accent}
          strokeWidth="2.5"
          strokeDasharray="8 6"
          strokeDashoffset={perimeterDash}
          opacity="0.95"
        />

        {/* Hotspot pulse at blockade center */}
        <circle
          cx="320"
          cy="190"
          r={60 + pulse * 30}
          fill="url(#hotspot)"
          opacity={pulse}
        />
        <circle cx="320" cy="190" r="5" fill={accent} opacity="0.95" />

        {/* Tanker icon animating west→east */}
        <g transform={`translate(${shipX}, 180)`}>
          <rect x="0" y="0" width="36" height="8" rx="2" fill={PHOTONECT.paper} opacity="0.9" />
          <rect x="10" y="-6" width="10" height="6" fill={PHOTONECT.paper} opacity="0.9" />
          <circle cx="44" cy="4" r="3" fill={accent} opacity={pulse}>
          </circle>
        </g>

        {/* Iranian petrochem shutdown label */}
        <g opacity={r(0, 1, 90, 120)}>
          <circle cx="100" cy="90" r="6" fill="#ff4d6d" />
          <line x1="100" y1="90" x2="145" y2="75" stroke="#ff4d6d" strokeWidth="1.5" />
          <text
            x="148"
            y="72"
            fill="#ff4d6d"
            fontFamily={FONT_LATIN}
            fontSize="11"
            fontWeight="900"
            letterSpacing="1.5"
          >
            PETROCHEM HALT
          </text>
        </g>

        {/* USS Tripoli marker */}
        <g opacity={r(0, 1, 110, 140)}>
          <circle cx="380" cy="240" r="5" fill={accent} />
          <line x1="380" y1="240" x2="440" y2="265" stroke={accent} strokeWidth="1.5" />
          <text
            x="443"
            y="270"
            fill={accent}
            fontFamily={FONT_LATIN}
            fontSize="11"
            fontWeight="900"
            letterSpacing="1.5"
          >
            USS TRIPOLI
          </text>
        </g>

        {/* Spoofing vessels (multiple dots) */}
        {[240, 290, 350, 400].map((x, i) => (
          <circle
            key={i}
            cx={x}
            cy={210 + (i % 2) * 10}
            r="3"
            fill="#ff4d6d"
            opacity={r(0, 1, 50 + i * 5, 80 + i * 5) * pulse}
          />
        ))}
      </svg>

      <div
        style={{
          position: "absolute",
          top: -36,
          right: 0,
          fontFamily: FONT_ARABIC,
          fontWeight: 700,
          fontSize: 20,
          color: accent,
          letterSpacing: "0.06em",
          direction: "rtl",
        }}
      >
        خريطة الحصار ومواقع التزييف
      </div>
    </div>
  );
};

export const LebanonMap: React.FC<Props> = ({ accent }) => {
  const frame = useCurrentFrame();

  const r = (s: number, e: number, sf: number, ef: number) =>
    interpolate(frame, [sf, ef], [s, e], {
      easing: Easing.bezier(0.16, 1, 0.3, 1),
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    });

  const mapReveal = r(0, 1, 0, 30);
  const blueLineDash = r(2400, 0, 20, 110);
  const pulse = Math.sin(frame * 0.22) * 0.4 + 0.6;

  // 70 strike markers distributed in a band north of the Blue Line
  const strikes = Array.from({ length: 70 }, (_, i) => ({
    x: 60 + (i * 37) % 520,
    y: 110 + ((i * 53) % 60),
    delay: 30 + (i % 50),
  }));

  return (
    <div
      style={{
        width: 640,
        height: 360,
        position: "relative",
        opacity: mapReveal,
        transform: `translateY(${(1 - mapReveal) * 20}px)`,
      }}
    >
      <svg
        viewBox="0 0 640 360"
        width="640"
        height="360"
        style={{ position: "absolute", inset: 0 }}
      >
        <defs>
          <linearGradient id="sea_lb" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#0A1628" />
            <stop offset="100%" stopColor="#051018" />
          </linearGradient>
          <radialGradient id="hotspot_lb" cx="50%" cy="50%">
            <stop offset="0%" stopColor={accent} stopOpacity="0.45" />
            <stop offset="100%" stopColor={accent} stopOpacity="0" />
          </radialGradient>
          <linearGradient id="strike_lb" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#ff4d6d" stopOpacity="0.85" />
            <stop offset="100%" stopColor="#ff4d6d" stopOpacity="0.1" />
          </linearGradient>
        </defs>

        {/* Sea (west) */}
        <rect width="640" height="360" fill="url(#sea_lb)" />

        {/* Lebanon landmass (north) */}
        <path
          d="M 40,0 L 180,0 L 260,15 L 360,20 L 460,12 L 560,30 L 640,25 L 640,175 L 560,180 L 460,190 L 360,195 L 260,200 L 180,205 L 40,200 Z"
          fill="#1a2a1e"
          stroke={accent}
          strokeWidth="1.5"
          opacity="0.85"
        />
        <text
          x="120"
          y="55"
          fill={accent}
          fontFamily={FONT_LATIN}
          fontSize="18"
          fontWeight="900"
          letterSpacing="3"
        >
          LEBANON
        </text>

        {/* Israel landmass (south) */}
        <path
          d="M 40,220 L 180,225 L 260,220 L 360,215 L 460,210 L 560,205 L 640,210 L 640,360 L 40,360 Z"
          fill="#2a1f12"
          stroke="#d4a76a"
          strokeWidth="1.5"
          opacity="0.85"
        />
        <text
          x="120"
          y="330"
          fill="#d4a76a"
          fontFamily={FONT_LATIN}
          fontSize="14"
          fontWeight="900"
          letterSpacing="2"
        >
          ISRAEL
        </text>

        {/* Mediterranean label */}
        <text
          x="10"
          y="180"
          fill={PHOTONECT.paper}
          fontFamily={FONT_LATIN}
          fontSize="9"
          fontWeight="600"
          letterSpacing="2"
          opacity="0.35"
        >
          MEDITERRANEAN
        </text>

        {/* Blue Line (UN border) — animated dash */}
        <path
          d="M 40,205 L 180,210 L 260,210 L 360,208 L 460,205 L 560,207 L 640,210"
          fill="none"
          stroke="#5B8FF9"
          strokeWidth="2.5"
          strokeDasharray="10 6"
          strokeDashoffset={blueLineDash}
          opacity="0.95"
        />
        <text
          x="500"
          y="225"
          fill="#5B8FF9"
          fontFamily={FONT_LATIN}
          fontSize="10"
          fontWeight="900"
          letterSpacing="1.5"
        >
          BLUE LINE
        </text>

        {/* Litani River reference (dashed) — buffer zone southern edge */}
        <path
          d="M 40,130 L 180,135 L 260,130 L 360,135 L 460,130 L 560,132 L 640,130"
          fill="none"
          stroke={accent}
          strokeWidth="1"
          strokeDasharray="3 5"
          opacity="0.4"
        />
        <text
          x="10"
          y="127"
          fill={accent}
          fontFamily={FONT_LATIN}
          fontSize="9"
          fontWeight="700"
          letterSpacing="1.5"
          opacity="0.6"
        >
          LITANI (buffer)
        </text>

        {/* 70 strike markers (staggered fade-in) */}
        {strikes.map((s, i) => (
          <circle
            key={i}
            cx={s.x}
            cy={s.y}
            r="2.5"
            fill="url(#strike_lb)"
            opacity={r(0, 1, s.delay, s.delay + 12) * pulse}
          />
        ))}

        {/* Bint Jbeil — pulsing focal point */}
        <circle
          cx="320"
          cy="175"
          r={18 + pulse * 8}
          fill="url(#hotspot_lb)"
          opacity={pulse}
        />
        <circle cx="320" cy="175" r="5" fill="#ff4d6d" opacity="0.95" />
        <text
          x="326"
          y="175"
          fill="#ff4d6d"
          fontFamily={FONT_LATIN}
          fontSize="11"
          fontWeight="900"
          letterSpacing="1.5"
          opacity={r(0, 1, 60, 90)}
        >
          BINT JBEIL
        </text>

        {/* 70 sites stat label */}
        <g opacity={r(0, 1, 90, 120)}>
          <circle cx="80" cy="95" r="4" fill="#ff4d6d" />
          <line x1="80" y1="95" x2="130" y2="80" stroke="#ff4d6d" strokeWidth="1.5" />
          <text
            x="133"
            y="77"
            fill="#ff4d6d"
            fontFamily={FONT_LATIN}
            fontSize="12"
            fontWeight="900"
            letterSpacing="1.5"
          >
            70 HEZBOLLAH SITES
          </text>
        </g>
      </svg>

      <div
        style={{
          position: "absolute",
          top: -36,
          right: 0,
          fontFamily: FONT_ARABIC,
          fontWeight: 700,
          fontSize: 20,
          color: accent,
          letterSpacing: "0.06em",
          direction: "rtl",
        }}
      >
        خريطة الضربات ومنطقة الليطاني
      </div>
    </div>
  );
};

export const FlightEuropeMap: React.FC<Props> = ({ accent }) => {
  const frame = useCurrentFrame();

  const r = (s: number, e: number, sf: number, ef: number) =>
    interpolate(frame, [sf, ef], [s, e], {
      easing: Easing.bezier(0.16, 1, 0.3, 1),
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    });

  const mapReveal = r(0, 1, 0, 30);
  const pulse = Math.sin(frame * 0.22) * 0.4 + 0.6;

  // Major airports to flag with cancellation crosses
  const airports = [
    { x: 200, y: 130, code: "LHR" }, // London Heathrow
    { x: 260, y: 170, code: "CDG" }, // Paris
    { x: 340, y: 150, code: "FRA" }, // Frankfurt
    { x: 390, y: 200, code: "MUC" }, // Munich
    { x: 370, y: 250, code: "FCO" }, // Rome
    { x: 460, y: 180, code: "VIE" }, // Vienna
  ];

  return (
    <div
      style={{
        width: 640,
        height: 360,
        position: "relative",
        opacity: mapReveal,
        transform: `translateY(${(1 - mapReveal) * 20}px)`,
      }}
    >
      <svg
        viewBox="0 0 640 360"
        width="640"
        height="360"
        style={{ position: "absolute", inset: 0 }}
      >
        <defs>
          <linearGradient id="sea_eu" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#0A1628" />
            <stop offset="100%" stopColor="#051018" />
          </linearGradient>
          <radialGradient id="hotspot_eu" cx="50%" cy="50%">
            <stop offset="0%" stopColor={accent} stopOpacity="0.35" />
            <stop offset="100%" stopColor={accent} stopOpacity="0" />
          </radialGradient>
        </defs>

        {/* Sea */}
        <rect width="640" height="360" fill="url(#sea_eu)" />

        {/* Europe landmass — stylized */}
        <path
          d="M 80,80 L 160,70 L 220,85 L 280,80 L 340,90 L 400,85 L 460,100 L 520,95 L 580,110 L 600,180 L 560,220 L 490,260 L 420,280 L 340,285 L 280,275 L 220,280 L 160,265 L 110,240 L 80,200 Z"
          fill="#1a2a1e"
          stroke={accent}
          strokeWidth="1.5"
          opacity="0.85"
        />
        <text
          x="270"
          y="110"
          fill={accent}
          fontFamily={FONT_LATIN}
          fontSize="18"
          fontWeight="900"
          letterSpacing="4"
        >
          EUROPE
        </text>

        {/* Hormuz arrow — fuel origin marker coming from east */}
        <g opacity={r(0, 1, 30, 70)}>
          <path
            d="M 640,240 Q 590,220 540,200"
            fill="none"
            stroke="#ff4d6d"
            strokeWidth="2"
            strokeDasharray="6 4"
          />
          <circle cx="640" cy="240" r="4" fill="#ff4d6d" opacity={pulse} />
          <text
            x="585"
            y="260"
            fill="#ff4d6d"
            fontFamily={FONT_LATIN}
            fontSize="10"
            fontWeight="900"
            letterSpacing="1.5"
            textAnchor="middle"
          >
            FROM HORMUZ →
          </text>
        </g>

        {/* Airport markers with X (cancelled) */}
        {airports.map((a, i) => {
          const fadeIn = r(0, 1, 50 + i * 8, 70 + i * 8);
          return (
            <g key={a.code} opacity={fadeIn}>
              <circle cx={a.x} cy={a.y} r={10 + pulse * 3} fill="url(#hotspot_eu)" />
              <circle cx={a.x} cy={a.y} r="4" fill="#ff4d6d" />
              {/* X cross */}
              <line
                x1={a.x - 7}
                y1={a.y - 7}
                x2={a.x + 7}
                y2={a.y + 7}
                stroke="#ff4d6d"
                strokeWidth="2"
              />
              <line
                x1={a.x - 7}
                y1={a.y + 7}
                x2={a.x + 7}
                y2={a.y - 7}
                stroke="#ff4d6d"
                strokeWidth="2"
              />
              <text
                x={a.x + 12}
                y={a.y + 4}
                fill={PHOTONECT.paper}
                fontFamily={FONT_LATIN}
                fontSize="11"
                fontWeight="900"
                letterSpacing="1"
              >
                {a.code}
              </text>
            </g>
          );
        })}

        {/* +34% jet fuel label */}
        <g opacity={r(0, 1, 100, 130)}>
          <rect
            x="50"
            y="300"
            width="200"
            height="38"
            rx="4"
            fill="#ff4d6d"
            opacity="0.15"
          />
          <text
            x="60"
            y="324"
            fill="#ff4d6d"
            fontFamily={FONT_LATIN}
            fontSize="18"
            fontWeight="900"
            letterSpacing="1.5"
          >
            JET FUEL +34%
          </text>
        </g>
      </svg>

      <div
        style={{
          position: "absolute",
          top: -36,
          right: 0,
          fontFamily: FONT_ARABIC,
          fontWeight: 700,
          fontSize: 20,
          color: accent,
          letterSpacing: "0.06em",
          direction: "rtl",
        }}
      >
        خريطة المطارات الأوروبية المعرّضة
      </div>
    </div>
  );
};

type MapProps = { overlay: "hormuz" | "lebanon" | "flight_europe"; accent: string };

export const NewsMap: React.FC<MapProps> = ({ overlay, accent }) => {
  if (overlay === "hormuz") return <HormuzMap accent={accent} />;
  if (overlay === "lebanon") return <LebanonMap accent={accent} />;
  if (overlay === "flight_europe") return <FlightEuropeMap accent={accent} />;
  return null;
};
