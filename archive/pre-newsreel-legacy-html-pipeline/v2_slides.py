#!/usr/bin/env python3
"""
PHOTONECT NEWS V2 — Middle East 24h Recap Carousel
International infographic level. Rich charts, graphs, visual density.
8 slides, 1080x1350px, Arabic RTL
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import arabic_reshaper
from bidi.algorithm import get_display
import math
import os

# === DIMENSIONS ===
W, H = 1080, 1350

# === COLORS ===
DARK = (43, 43, 43)
DARK2 = (35, 35, 35)
DARK3 = (28, 28, 28)
CARD_BG = (52, 52, 52)
CARD_BORDER = (72, 72, 72)
RED = (215, 38, 56)
RED_DIM = (120, 30, 40)
RED_GLOW = (180, 30, 45)
GOLD = (255, 194, 23)
GOLD_DIM = (180, 140, 20)
WHITE = (255, 255, 255)
WHITE_80 = (210, 210, 210)
WHITE_60 = (160, 160, 160)
WHITE_40 = (110, 110, 110)
WHITE_20 = (65, 65, 65)
LIGHT_BG = (245, 245, 245)
ACCENT_GREEN = (76, 175, 80)
ACCENT_ORANGE = (255, 152, 0)

OUT = "/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE/slides_v2"
os.makedirs(OUT, exist_ok=True)

# === FONTS ===
FDIR = "/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE"
FONT_CACHE = {}

def font(name, size):
    key = (name, size)
    if key in FONT_CACHE:
        return FONT_CACHE[key]
    paths = {
        'ar_black': f'{FDIR}/tajawal_black.ttf',
        'ar_xbold': f'{FDIR}/tajawal_extrabold.ttf',
        'ar_bold': f'{FDIR}/tajawal_bold.ttf',
        'ar_med': f'{FDIR}/tajawal_medium.ttf',
        'ar': f'{FDIR}/tajawal_regular.ttf',
        'en_bold': f'{FDIR}/../Library/Application Support/Claude/local-agent-mode-sessions/skills-plugin/c8a099e6-fe45-4fa6-8487-50b77cbca08d/541afcd9-298c-46d5-8595-82f0773c887c/skills/canvas-design/canvas-fonts/Outfit-Bold.ttf',
        'en': f'{FDIR}/../Library/Application Support/Claude/local-agent-mode-sessions/skills-plugin/c8a099e6-fe45-4fa6-8487-50b77cbca08d/541afcd9-298c-46d5-8595-82f0773c887c/skills/canvas-design/canvas-fonts/Outfit-Regular.ttf',
        'mono': f'{FDIR}/../Library/Application Support/Claude/local-agent-mode-sessions/skills-plugin/c8a099e6-fe45-4fa6-8487-50b77cbca08d/541afcd9-298c-46d5-8595-82f0773c887c/skills/canvas-design/canvas-fonts/GeistMono-Bold.ttf',
        'mono_r': f'{FDIR}/../Library/Application Support/Claude/local-agent-mode-sessions/skills-plugin/c8a099e6-fe45-4fa6-8487-50b77cbca08d/541afcd9-298c-46d5-8595-82f0773c887c/skills/canvas-design/canvas-fonts/GeistMono-Regular.ttf',
    }
    try:
        f = ImageFont.truetype(paths.get(name, paths['ar']), size)
    except:
        f = ImageFont.load_default()
    FONT_CACHE[key] = f
    return f

def ar(text):
    return get_display(arabic_reshaper.reshape(text))

def tw(draw, text, f):
    bb = draw.textbbox((0, 0), text, font=f)
    return bb[2] - bb[0]

def th(draw, text, f):
    bb = draw.textbbox((0, 0), text, font=f)
    return bb[3] - bb[1]

def center_text(draw, text, y, f, fill, w=W):
    t = tw(draw, text, f)
    draw.text(((w - t) // 2, y), text, font=f, fill=fill)

def right_text(draw, text, x, y, f, fill):
    t = tw(draw, text, f)
    draw.text((x - t, y), text, font=f, fill=fill)

# === DRAWING PRIMITIVES ===
def rrect(draw, box, r, fill=None, outline=None, ow=1):
    x1, y1, x2, y2 = box
    r = min(r, (x2-x1)//2, (y2-y1)//2)
    if r < 1: r = 0
    if r == 0:
        if fill: draw.rectangle(box, fill=fill)
        if outline: draw.rectangle(box, outline=outline, width=ow)
        return
    if fill:
        draw.rectangle([x1+r, y1, x2-r, y2], fill=fill)
        draw.rectangle([x1, y1+r, x2, y2-r], fill=fill)
        draw.pieslice([x1, y1, x1+2*r, y1+2*r], 180, 270, fill=fill)
        draw.pieslice([x2-2*r, y1, x2, y1+2*r], 270, 360, fill=fill)
        draw.pieslice([x1, y2-2*r, x1+2*r, y2], 90, 180, fill=fill)
        draw.pieslice([x2-2*r, y2-2*r, x2, y2], 0, 90, fill=fill)
    if outline:
        draw.arc([x1, y1, x1+2*r, y1+2*r], 180, 270, fill=outline, width=ow)
        draw.arc([x2-2*r, y1, x2, y1+2*r], 270, 360, fill=outline, width=ow)
        draw.arc([x1, y2-2*r, x1+2*r, y2], 90, 180, fill=outline, width=ow)
        draw.arc([x2-2*r, y2-2*r, x2, y2], 0, 90, fill=outline, width=ow)
        draw.line([x1+r, y1, x2-r, y1], fill=outline, width=ow)
        draw.line([x1+r, y2, x2-r, y2], fill=outline, width=ow)
        draw.line([x1, y1+r, x1, y2-r], fill=outline, width=ow)
        draw.line([x2, y1+r, x2, y2-r], fill=outline, width=ow)

def gradient_rect(img, box, color_top, color_bot):
    x1, y1, x2, y2 = box
    draw = ImageDraw.Draw(img)
    for y in range(y1, y2):
        t = (y - y1) / max(1, y2 - y1)
        r = int(color_top[0] + (color_bot[0] - color_top[0]) * t)
        g = int(color_top[1] + (color_bot[1] - color_top[1]) * t)
        b = int(color_top[2] + (color_bot[2] - color_top[2]) * t)
        draw.line([x1, y, x2, y], fill=(r, g, b))

def draw_bar_chart(draw, x, y, w, h, values, labels, colors, max_val=None):
    """Draw a horizontal bar chart"""
    if max_val is None:
        max_val = max(values)
    bar_h = min(40, (h - 10 * len(values)) // len(values))
    gap = (h - bar_h * len(values)) // (len(values) + 1)

    for i, (val, label, color) in enumerate(zip(values, labels, colors)):
        by = y + gap + i * (bar_h + gap)
        bar_w = int((val / max_val) * (w - 160))

        # Bar background track
        rrect(draw, (x + 140, by, x + w, by + bar_h), 6, fill=WHITE_20)
        # Bar fill
        if bar_w > 12:
            rrect(draw, (x + 140, by, x + 140 + bar_w, by + bar_h), 6, fill=color)

        # Label (right-aligned before bar)
        lbl = ar(label)
        right_text(draw, lbl, x + 130, by + 4, font('ar_bold', 16), WHITE_60)

        # Value on bar
        vt = ar(str(val))
        vtw = tw(draw, vt, font('ar_black', 18))
        vx = x + 140 + bar_w + 10 if bar_w < w - 220 else x + 140 + bar_w - vtw - 10
        vc = WHITE if bar_w >= w - 220 else color
        draw.text((vx, by + 4), vt, font=font('ar_black', 18), fill=vc)

def draw_donut(draw, cx, cy, r_outer, r_inner, percentage, color, bg_color=WHITE_20):
    """Draw a donut/ring chart"""
    # Background ring
    draw.arc([cx-r_outer, cy-r_outer, cx+r_outer, cy+r_outer], 0, 360, fill=bg_color, width=r_outer-r_inner)
    # Fill arc (start from top = -90)
    angle = int(percentage / 100 * 360)
    if angle > 0:
        draw.arc([cx-r_outer, cy-r_outer, cx+r_outer, cy+r_outer], -90, -90+angle, fill=color, width=r_outer-r_inner)

def draw_progress_bar(draw, x, y, w, h, pct, color, bg=WHITE_20):
    """Draw a progress bar"""
    rrect(draw, (x, y, x+w, y+h), h//2, fill=bg)
    fill_w = int(w * pct / 100)
    if fill_w > h:
        rrect(draw, (x, y, x+fill_w, y+h), h//2, fill=color)

def draw_line_chart(draw, x, y, w, h, points, color, fill_color=None):
    """Draw a mini line chart with area fill"""
    if len(points) < 2:
        return
    max_v = max(points)
    min_v = min(points)
    rng = max_v - min_v if max_v != min_v else 1

    coords = []
    for i, v in enumerate(points):
        px = x + int(i / (len(points)-1) * w)
        py = y + h - int((v - min_v) / rng * h)
        coords.append((px, py))

    # Area fill
    if fill_color and len(coords) >= 2:
        poly = list(coords) + [(coords[-1][0], y+h), (coords[0][0], y+h)]
        draw.polygon(poly, fill=fill_color)

    # Line
    for i in range(len(coords)-1):
        draw.line([coords[i], coords[i+1]], fill=color, width=3)

    # Dots at key points
    for i in [0, len(coords)//2, len(coords)-1]:
        if i < len(coords):
            px, py = coords[i]
            draw.ellipse([px-4, py-4, px+4, py+4], fill=color)

def draw_grid_pattern(draw, x, y, w, h, spacing=40, color=(45, 45, 45)):
    """Draw subtle grid pattern for texture"""
    for gx in range(x, x+w, spacing):
        draw.line([gx, y, gx, y+h], fill=color, width=1)
    for gy in range(y, y+h, spacing):
        draw.line([x, gy, x+w, gy], fill=color, width=1)

def draw_dot_pattern(draw, x, y, w, h, spacing=24, color=(50, 50, 50)):
    """Draw dot pattern for texture"""
    for gx in range(x, x+w, spacing):
        for gy in range(y, y+h, spacing):
            draw.ellipse([gx, gy, gx+2, gy+2], fill=color)

def draw_logo(draw, x, y, scale=1.0):
    """PHOTONECT + red rect + NEWS"""
    fs = int(24 * scale)
    ss = int(12 * scale)
    rw = int(26 * scale)
    rh = int(8 * scale)

    f_main = font('en_bold', fs)
    f_sub = font('en_bold', ss)
    txt = "PHOTONECT"
    w = tw(draw, txt, f_main)

    # Red rectangle
    rx = x + int(w * 0.52) - rw // 2
    draw.rectangle([rx, y, rx+rw, y+rh], fill=RED)

    # Text
    draw.text((x, y + rh + 3), txt, font=f_main, fill=WHITE)

    # NEWS
    ns = "NEWS"
    nw = tw(draw, ns, f_sub)
    draw.text((x + (w - nw)//2, y + rh + 3 + fs + 2), ns, font=f_sub, fill=GOLD)
    return w

def draw_page_indicator(draw, current, total, y):
    """Draw page dots at bottom"""
    dot_r = 5
    gap = 16
    total_w = total * (dot_r * 2) + (total - 1) * gap
    sx = (W - total_w) // 2
    for i in range(total):
        dx = sx + i * (dot_r * 2 + gap)
        fill = GOLD if i == current else WHITE_20
        draw.ellipse([dx, y, dx + dot_r*2, y + dot_r*2], fill=fill)


# ============================================================
# SLIDE 1: COVER — Hero with glowing stats
# ============================================================
def slide_1():
    img = Image.new('RGB', (W, H), DARK3)
    draw = ImageDraw.Draw(img)

    # Textured background
    draw_dot_pattern(draw, 0, 0, W, H, 20, (32, 32, 32))

    # Top accent line
    gradient_rect(img, (0, 0, W, 5), RED, RED)
    draw = ImageDraw.Draw(img)  # re-acquire after gradient

    # Header bar
    rrect(draw, (0, 5, W, 90), 0, fill=(35, 35, 35))
    draw.line([0, 90, W, 90], fill=WHITE_20, width=1)

    # Logo
    draw_logo(draw, 55, 18, 1.0)

    # Date badge with live dot
    date_f = font('ar_bold', 18)
    dt = ar("٧ أبريل ٢٠٢٦")
    dtw = tw(draw, dt, date_f)
    bx = W - 65 - dtw - 45
    rrect(draw, (bx, 28, W-50, 68), 10, fill=(55, 55, 55), outline=WHITE_20)
    draw.ellipse([bx+14, 42, bx+24, 52], fill=RED)
    draw.text((bx+32, 34), dt, font=date_f, fill=WHITE)

    # === HERO SECTION ===
    # Subtle radial glow behind text
    for r in range(200, 0, -2):
        alpha = int(8 * (1 - r/200))
        c = (43 + alpha, 35 + alpha, 28 + alpha)
        draw.ellipse([W//2-r, 380-r//2, W//2+r, 380+r//2], fill=c)

    # Category label
    center_text(draw, ar("ملخص ٢٤ ساعة"), 310, font('ar_bold', 20), GOLD)

    # Thin decorative line
    draw.line([W//2-80, 345, W//2+80, 345], fill=GOLD, width=2)

    # Main title
    center_text(draw, ar("الشرق الأوسط الآن"), 370, font('ar_black', 72), WHITE)

    # Subtitle with bullet separators
    sub_parts = ["غزة", "لبنان", "إيران", "الضفة الغربية"]
    sub_text = "  |  ".join(sub_parts)  # use regular pipe
    center_text(draw, ar(sub_text), 470, font('ar_med', 22), WHITE_40)

    # Horizontal rule
    draw.line([120, 530, W-120, 530], fill=WHITE_20, width=1)

    # === THREE STAT CARDS ===
    cards = [
        ("+72,302", ar("شهيد في غزة"), ar("منذ أكتوبر ٢٠٢٣"), RED, [10,25,40,55,70,72]),
        ("1.2M", ar("نازح في لبنان"), ar("منذ ٢ مارس ٢٠٢٦"), GOLD, [0,0,0,0,5,50,120]),
        ("$116", ar("سعر برميل النفط"), ar("بسبب إغلاق هرمز"), RED, [65,68,72,75,80,95,116]),
    ]

    card_w = (W - 160) // 3
    card_h = 320

    for i, (num, label, sub, color, chart_data) in enumerate(cards):
        cx = 60 + i * (card_w + 20)
        cy = 570

        # Card with subtle border
        rrect(draw, (cx, cy, cx+card_w, cy+card_h), 16, fill=CARD_BG, outline=WHITE_20)

        # Top accent bar
        draw.rectangle([cx+2, cy+1, cx+card_w-2, cy+4], fill=color)

        # Number — large
        nf = font('en_bold', 42)
        nw = tw(draw, num, nf)
        draw.text((cx + (card_w-nw)//2, cy+25), num, font=nf, fill=color)

        # Mini sparkline chart
        chart_y = cy + 90
        chart_h = 60
        chart_x = cx + 20
        chart_w_px = card_w - 40

        # Area fill
        fill_c = (color[0]//5, color[1]//5, color[2]//5)
        draw_line_chart(draw, chart_x, chart_y, chart_w_px, chart_h, chart_data, color, fill_c)

        # Divider
        draw.line([cx+20, cy+170, cx+card_w-20, cy+170], fill=WHITE_20, width=1)

        # Arabic label
        lw = tw(draw, label, font('ar_bold', 18))
        draw.text((cx + (card_w-lw)//2, cy+185), label, font=font('ar_bold', 18), fill=WHITE_80)

        # Sub label
        sw = tw(draw, sub, font('ar', 14))
        draw.text((cx + (card_w-sw)//2, cy+218), sub, font=font('ar', 14), fill=WHITE_40)

        # Bottom mini stat bar showing proportion
        bar_y = cy + 260
        draw_progress_bar(draw, cx+20, bar_y, card_w-40, 8, min(100, int(float(num.replace('+','').replace('$','').replace(',','').replace('M','')) / 1.2 * 100) if 'M' not in num else 85), color)

    # === BOTTOM SECTION ===
    # Conflict map silhouette suggestion (abstract dots)
    map_y = 940
    draw.line([60, map_y, W-60, map_y], fill=WHITE_20, width=1)

    # 4 region indicators
    regions = [
        (ar("غزة"), RED, 85),
        (ar("لبنان"), ACCENT_ORANGE, 70),
        (ar("إيران"), GOLD, 95),
        (ar("الضفة"), RED_DIM, 45),
    ]
    rw = (W - 160) // 4
    for i, (name, color, intensity) in enumerate(regions):
        rx = 60 + i * (rw + 13)
        ry = map_y + 20

        # Pulsing circle (static representation)
        cr = int(intensity * 0.4)
        # Outer glow
        for ring in range(cr, cr+15):
            alpha = max(0, 25 - (ring - cr) * 2)
            gc = (color[0]*alpha//100, color[1]*alpha//100, color[2]*alpha//100)
            draw.ellipse([rx+rw//2-ring, ry+40-ring, rx+rw//2+ring, ry+40+ring], outline=gc)
        # Core dot
        draw.ellipse([rx+rw//2-cr, ry+40-cr, rx+rw//2+cr, ry+40+cr], fill=color)

        # Label
        nw = tw(draw, name, font('ar_bold', 16))
        draw.text((rx + (rw-nw)//2, ry + 80), name, font=font('ar_bold', 16), fill=WHITE_60)

        # Intensity bar
        draw_progress_bar(draw, rx+10, ry+110, rw-20, 6, intensity, color)

    # Severity legend
    legend_y = map_y + 160
    draw.line([60, legend_y, W-60, legend_y], fill=WHITE_20, width=1)
    center_text(draw, ar("مستوى التصعيد"), legend_y + 10, font('ar', 14), WHITE_40)

    # Bottom gold strip
    strip_y = H - 75
    draw.rectangle([0, strip_y, W, H], fill=GOLD)

    draw.text((65, strip_y + 22), ar("اسحب لقراءة التفاصيل"), font=font('ar_bold', 20), fill=DARK3)
    # Arrow
    draw.text((55, strip_y + 22), "<", font=font('en_bold', 22), fill=DARK3)

    # Page dots
    draw_page_indicator(draw, 0, 8, strip_y + 50)

    img.save(os.path.join(OUT, "01_cover.png"), quality=95)
    print("  Slide 1 saved")
    return img


# ============================================================
# SLIDE 2: STRAIT OF HORMUZ
# ============================================================
def slide_2():
    img = Image.new('RGB', (W, H), DARK3)
    draw = ImageDraw.Draw(img)
    draw_dot_pattern(draw, 0, 0, W, H, 20, (32, 32, 32))

    # Red header section with gradient
    gradient_rect(img, (0, 0, W, 330), (180, 25, 40), (140, 20, 35))
    draw = ImageDraw.Draw(img)

    # Nav bar on red
    rrect(draw, (W-160, 28, W-55, 58), 15, fill=(100, 15, 25))
    center_text(draw, ar("عاجل"), 31, font('ar_bold', 16), WHITE, w=W-55+W-160)
    draw.text((60, 34), "2 / 8", font=font('en_bold', 14), fill=(200,180,180))
    draw_logo(draw, W//2 - 70, 15, 0.8)

    # Title
    center_text(draw, ar("مضيق هرمز"), 100, font('ar_black', 58), WHITE)
    center_text(draw, ar("مهلة ترامب تنتهي الليلة — والعالم يترقب"), 180, font('ar_med', 20), (255,220,220))

    # Oil price line chart in header
    oil_data = [65, 68, 70, 72, 75, 80, 85, 92, 100, 108, 112, 116]
    draw_line_chart(draw, 100, 230, W-200, 70, oil_data, GOLD, (80, 60, 10))
    # Label on chart
    draw.text((110, 240), ar("سعر النفط"), font=font('ar', 12), fill=(200,180,150))

    # === CONTENT ===
    y = 350

    # DEADLINE BOX — dramatic
    rrect(draw, (50, y, W-50, y+200), 18, fill=(50, 25, 30), outline=RED, ow=3)

    # Flashing indicator dots
    for dot_x in range(80, W-80, 40):
        draw.rectangle([dot_x, y+4, dot_x+20, y+8], fill=RED)

    center_text(draw, ar("الموعد النهائي"), y+25, font('ar_bold', 16), RED)

    # Time display — large monospace feel
    time_text = "8:00 PM ET"
    center_text(draw, time_text, y+55, font('mono', 52), WHITE)
    center_text(draw, ar("الثلاثاء — بتوقيت واشنطن"), y+120, font('ar_bold', 20), GOLD)
    center_text(draw, ar("ترامب يهدد بتدمير محطات الكهرباء والجسور"), y+155, font('ar', 17), WHITE_60)

    # === OIL PRICE CARDS ===
    y2 = y + 225
    cw = (W - 140) // 2

    for i, (name, price, change, pct) in enumerate([
        (ar("خام برنت"), "$110.66", "+0.81%", 78),
        (ar("خام غرب تكساس"), "$116.22", "+3.0%", 88),
    ]):
        cx = 50 + i * (cw + 40)
        rrect(draw, (cx, y2, cx+cw, y2+160), 16, fill=CARD_BG, outline=WHITE_20)

        # Oil icon (simple barrel shape)
        bx = cx + cw//2
        draw.rectangle([bx-12, y2+15, bx+12, y2+35], fill=GOLD, outline=DARK3)
        draw.line([bx-14, y2+20, bx+14, y2+20], fill=DARK3, width=2)
        draw.line([bx-14, y2+30, bx+14, y2+30], fill=DARK3, width=2)

        nw_val = tw(draw, name, font('ar_med', 15))
        draw.text((cx + (cw-nw_val)//2, y2+42), name, font=font('ar_med', 15), fill=WHITE_40)

        pw = tw(draw, price, font('mono', 36))
        draw.text((cx + (cw-pw)//2, y2+65), price, font=font('mono', 36), fill=GOLD)

        # Change badge
        cw_val = tw(draw, change, font('mono_r', 14))
        badge_x = cx + (cw-cw_val)//2 - 10
        rrect(draw, (badge_x, y2+110, badge_x+cw_val+20, y2+132), 6, fill=(30, 60, 35))
        draw.text((badge_x+10, y2+112), change, font=font('mono_r', 14), fill=ACCENT_GREEN)

        # Progress bar
        draw_progress_bar(draw, cx+15, y2+142, cw-30, 6, pct, GOLD)

    # === INFO BULLETS ===
    y3 = y2 + 185
    bullets = [
        ("01", ar("٢٠٪ من إمدادات النفط العالمية"), ar("كانت تمر عبر المضيق — أكبر انقطاع في تاريخ النفط")),
        ("02", ar("إيران ترفض المقترح الأمريكي"), ar("وتقدم خطة من ١٠ نقاط تشمل وقف دائم ورفع العقوبات")),
        ("03", ar("إيران تنفي المفاوضات المباشرة"), ar("رغم تصريحات ترامب بأن إيران تتفاوض بجدية")),
    ]

    for i, (num, title, desc) in enumerate(bullets):
        by = y3 + i * 115
        rrect(draw, (50, by, W-50, by+100), 14, fill=CARD_BG)
        # Gold accent
        draw.rectangle([W-54, by+10, W-50, by+90], fill=GOLD)

        # Number badge
        rrect(draw, (W-120, by+28, W-75, by+68), 8, fill=GOLD)
        nw_b = tw(draw, num, font('mono', 18))
        draw.text((W-97-nw_b//2, by+32), num, font=font('mono', 18), fill=DARK3)

        # Title + desc
        draw.text((70, by+15), title, font=font('ar_bold', 18), fill=WHITE)
        draw.text((70, by+50), desc, font=font('ar', 15), fill=WHITE_40)

    # Bottom bar
    rrect(draw, (0, H-65, W, H), 0, fill=(45, 40, 28))
    draw.line([0, H-65, W, H-65], fill=GOLD_DIM, width=1)

    # 20% stat as donut
    draw_donut(draw, 90, H-33, 18, 10, 20, GOLD)
    draw.text((120, H-48), ar("٢٠٪ من النفط العالمي محتجز"), font=font('ar_bold', 15), fill=GOLD)

    draw_page_indicator(draw, 1, 8, H-22)

    img.save(os.path.join(OUT, "02_hormuz.png"), quality=95)
    print("  Slide 2 saved")
    return img


# ============================================================
# SLIDE 3: LEBANON
# ============================================================
def slide_3():
    img = Image.new('RGB', (W, H), LIGHT_BG)
    draw = ImageDraw.Draw(img)

    # Dark header
    gradient_rect(img, (0, 0, W, 290), DARK3, DARK)
    draw = ImageDraw.Draw(img)

    # Nav
    rrect(draw, (W-150, 28, W-55, 55), 14, fill=RED)
    nt = tw(draw, ar("لبنان"), font('ar_bold', 14))
    draw.text((W-102-nt//2, 30), ar("لبنان"), font=font('ar_bold', 14), fill=WHITE)
    draw.text((60, 34), "3 / 8", font=font('en_bold', 14), fill=WHITE_40)
    draw_logo(draw, W//2-65, 15, 0.8)

    center_text(draw, ar("الحرب على لبنان"), 85, font('ar_black', 52), WHITE)

    # Duration badge
    dur_text = ar("٣٦ يوماً")
    dw = tw(draw, dur_text, font('ar_black', 24))
    rrect(draw, (W//2-dw//2-20, 160, W//2+dw//2+20, 195), 10, fill=GOLD)
    center_text(draw, dur_text, 163, font('ar_black', 22), DARK3)
    center_text(draw, ar("منذ ٢ مارس ٢٠٢٦"), 210, font('ar_med', 17), WHITE_60)

    # Horizontal progress showing 36 of ~365 days
    draw_progress_bar(draw, 120, 248, W-240, 8, 10, RED, WHITE_20)
    draw.text((W-120, 240), ar("اليوم ٣٦"), font=font('ar', 12), fill=WHITE_40)

    # === STAT CARDS — 2x2 grid ===
    y = 310
    cw = (W - 130) // 2
    ch = 175
    gap = 10

    stats = [
        ("+1,400", ar("قتيل"), ar("مدنيين ومقاتلين"), RED, 60),
        ("1.2M", ar("نازح"), ar("٢٠٪ من سكان لبنان"), GOLD_DIM, 20),
        ("126", ar("طفل قُتل"), ar("وفق السلطات اللبنانية"), RED, 8),
        ("1/10", ar("من مساحة لبنان"), ar("خطة الاحتلال"), DARK, 10),
    ]

    for i, (num, label, sub, accent, donut_pct) in enumerate(stats):
        col, row = i % 2, i // 2
        cx = 50 + col * (cw + 30)
        cy = y + row * (ch + gap)

        rrect(draw, (cx, cy, cx+cw, cy+ch), 16, fill=WHITE)
        draw.rectangle([cx+2, cy, cx+cw-2, cy+5], fill=accent)

        # Donut chart
        draw_donut(draw, cx+cw-50, cy+50, 28, 18, donut_pct, accent, (230,230,230))

        # Number
        nf = font('en_bold', 42)
        draw.text((cx+25, cy+20), num, font=nf, fill=accent if accent != DARK else DARK)

        # Labels
        draw.text((cx+25, cy+80), label, font=font('ar_black', 20), fill=DARK)
        draw.text((cx+25, cy+115), sub, font=font('ar', 14), fill=(140,140,140))

        # Bottom micro bar
        draw_progress_bar(draw, cx+25, cy+150, cw-50, 5, donut_pct, accent, (230,230,230))

    # === TIMELINE ===
    tl_y = y + 2*(ch+gap) + 20

    # Section header
    draw.line([50, tl_y, W-50, tl_y], fill=(200,200,200), width=1)
    center_text(draw, ar("آخر الأحداث"), tl_y + 8, font('ar_bold', 16), (140,140,140))

    events = [
        ("01 APR", ar("غارة على بيروت تقتل قائداً في حزب الله"), RED),
        ("04 APR", ar("غارات تلحق أضراراً بمستشفى في صور"), ACCENT_ORANGE),
        ("05 APR", ar("١٤ قتيلاً في غارات متفرقة على لبنان"), RED),
        ("06 APR", ar("تدمير بلدات واستهداف مناطق آمنة"), RED),
    ]

    for i, (date, event, color) in enumerate(events):
        ey = tl_y + 40 + i * 72

        # Timeline dot + line
        dot_x = W - 80
        if i < len(events)-1:
            draw.line([dot_x, ey+12, dot_x, ey+72], fill=(200,200,200), width=2)
        draw.ellipse([dot_x-7, ey+5, dot_x+7, ey+19], fill=color)

        # Date
        draw.text((dot_x-70, ey+2), date, font=font('mono_r', 11), fill=(140,140,140))

        # Event card
        rrect(draw, (50, ey, dot_x-90, ey+55), 10, fill=WHITE)
        draw.rectangle([50, ey+2, 54, ey+53], fill=color)
        draw.text((65, ey+12), event, font=font('ar_med', 16), fill=DARK)

    # Bottom
    draw.rectangle([0, H-60, W, H], fill=DARK)
    draw.text((65, H-44), ar("٦٠٠ ألف ممنوعون من العودة لمنازلهم"), font=font('ar_bold', 14), fill=GOLD)
    draw_page_indicator(draw, 2, 8, H-22)

    img.save(os.path.join(OUT, "03_lebanon.png"), quality=95)
    print("  Slide 3 saved")
    return img


# ============================================================
# SLIDE 4: GAZA
# ============================================================
def slide_4():
    img = Image.new('RGB', (W, H), DARK3)
    draw = ImageDraw.Draw(img)
    draw_dot_pattern(draw, 0, 0, W, H, 20, (32, 32, 32))

    # Nav
    rrect(draw, (W-140, 28, W-55, 55), 14, fill=RED)
    draw.text((W-110, 30), ar("غزة"), font=font('ar_bold', 14), fill=WHITE)
    draw.text((60, 34), "4 / 8", font=font('en_bold', 14), fill=WHITE_40)
    draw_logo(draw, W//2-65, 15, 0.8)

    center_text(draw, ar("غزة — هدنة هشّة"), 85, font('ar_black', 50), WHITE)
    center_text(draw, ar("وقف إطلاق النار لم يوقف القتل"), 155, font('ar_med', 20), GOLD)

    # === BIG NUMBER with context ===
    y = 210
    rrect(draw, (50, y, W-50, y+250), 20, fill=(55, 25, 30), outline=RED_DIM, ow=2)

    # Glow effect behind number
    for r in range(120, 0, -3):
        alpha = int(5 * (1 - r/120))
        c = (55 + alpha*3, 25, 30)
        draw.ellipse([W//2-r, y+60-r//3, W//2+r, y+60+r//3], fill=c)

    center_text(draw, "72,302+", y+20, font('mono', 80), RED)
    center_text(draw, ar("شهيد منذ ٧ أكتوبر ٢٠٢٣"), y+120, font('ar_bold', 22), WHITE_80)

    # Comparison bar: official vs estimated
    bar_y = y + 165
    draw.text((W-120, bar_y), ar("رسمي"), font=font('ar', 12), fill=WHITE_40)
    draw_progress_bar(draw, 80, bar_y+5, W-220, 12, 72, RED)

    draw.text((W-120, bar_y+25), ar("تقديري"), font=font('ar', 12), fill=WHITE_40)
    draw_progress_bar(draw, 80, bar_y+30, W-220, 12, 100, ACCENT_ORANGE)

    draw.text((80, bar_y+50), ar("التقديرات المستقلة تتجاوز ١٠٠,٠٠٠"), font=font('ar', 13), fill=WHITE_40)

    # === SUB STATS with donuts ===
    y2 = y + 280
    sub_cards = [
        ("716+", ar("قُتلوا منذ الهدنة"), RED, 15),
        ("1,990", ar("أصيبوا منذ أكتوبر"), GOLD, 30),
        ("13", ar("قُتلوا في أسبوع"), ACCENT_ORANGE, 5),
    ]
    scw = (W - 140) // 3

    for i, (num, label, color, dpct) in enumerate(sub_cards):
        sx = 50 + i * (scw + 20)
        rrect(draw, (sx, y2, sx+scw, y2+170), 14, fill=CARD_BG, outline=WHITE_20)

        # Donut
        draw_donut(draw, sx+scw//2, y2+50, 32, 20, dpct, color)
        # Number in center of donut
        nf = font('mono', 18)
        nw = tw(draw, num, nf)
        draw.text((sx+scw//2-nw//2, y2+38), num, font=nf, fill=color)

        # Label
        lw = tw(draw, label, font('ar_med', 14))
        draw.text((sx+(scw-lw)//2, y2+100), label, font=font('ar_med', 14), fill=WHITE_60)

        # Bar
        draw_progress_bar(draw, sx+15, y2+145, scw-30, 6, dpct*2, color)

    # === CEASEFIRE STATUS ===
    y3 = y2 + 200
    rrect(draw, (50, y3, W-50, y3+160), 16, fill=(50, 45, 28), outline=GOLD_DIM)

    # Status indicator
    draw.ellipse([W-95, y3+18, W-80, y3+33], fill=GOLD)
    right_text(draw, ar("المرحلة الثانية من الهدنة"), W-105, y3+15, font('ar_bold', 19), GOLD)

    # Phase progress
    phases = [ar("المرحلة ١"), ar("المرحلة ٢"), ar("المرحلة ٣")]
    phase_w = (W - 160) // 3
    for i, phase in enumerate(phases):
        px = 70 + i * phase_w
        color = ACCENT_GREEN if i == 0 else GOLD if i == 1 else WHITE_20
        draw_progress_bar(draw, px, y3+55, phase_w-20, 10, 100 if i==0 else 30 if i==1 else 0, color)
        pw = tw(draw, phase, font('ar', 13))
        draw.text((px+(phase_w-20-pw)//2, y3+70), phase, font=font('ar', 13), fill=WHITE_40)

    draw.text((70, y3+100), ar("حكومة تكنوقراط بقيادة علي شعث تحت إشراف مجلس السلام الدولي"), font=font('ar', 15), fill=WHITE_60)
    draw.text((70, y3+125), ar("مصر وتركيا وقطر ترحب. إسرائيل أغلقت المعابر ما عدا كرم أبو سالم"), font=font('ar', 14), fill=WHITE_40)

    # === DISARMAMENT BOX ===
    y4 = y3 + 185
    rrect(draw, (50, y4, W-50, y4+130), 14, fill=CARD_BG)
    draw.rectangle([W-54, y4+10, W-50, y4+120], fill=RED)

    draw.text((70, y4+12), ar("نقطة الخلاف: نزع سلاح حماس"), font=font('ar_bold', 18), fill=RED)
    draw.text((70, y4+48), ar("الجناح العسكري يرفض المناقشة قبل تنفيذ إسرائيل"), font=font('ar', 15), fill=WHITE_60)
    draw.text((70, y4+75), ar("للمرحلة الأولى بالكامل"), font=font('ar', 15), fill=WHITE_60)

    # Conflict meter
    draw.text((70, y4+100), ar("مستوى التوتر"), font=font('ar', 12), fill=WHITE_40)
    draw_progress_bar(draw, 200, y4+105, W-280, 8, 75, RED)

    # Bottom
    draw.rectangle([0, H-60, W, H], fill=RED)
    draw.text((65, H-44), ar("كرم أبو سالم — المعبر الوحيد المفتوح"), font=font('ar_bold', 14), fill=WHITE)
    draw_page_indicator(draw, 3, 8, H-22)

    img.save(os.path.join(OUT, "04_gaza.png"), quality=95)
    print("  Slide 4 saved")
    return img


# ============================================================
# SLIDE 5: IRAN TIMELINE
# ============================================================
def slide_5():
    img = Image.new('RGB', (W, H), DARK3)
    draw = ImageDraw.Draw(img)
    draw_grid_pattern(draw, 0, 300, W, H-360, 50, (33, 33, 33))

    # Header
    gradient_rect(img, (0, 0, W, 270), (40, 35, 35), DARK3)
    draw = ImageDraw.Draw(img)

    rrect(draw, (W-150, 28, W-55, 55), 14, fill=RED)
    draw.text((W-115, 30), ar("إيران"), font=font('ar_bold', 14), fill=WHITE)
    draw.text((60, 34), "5 / 8", font=font('en_bold', 14), fill=WHITE_40)
    draw_logo(draw, W//2-65, 15, 0.8)

    center_text(draw, ar("حرب إيران ٢٠٢٦"), 85, font('ar_black', 52), WHITE)

    # Day counter
    day_text = "DAY 38"
    dw_val = tw(draw, day_text, font('mono', 32))
    rrect(draw, (W//2-dw_val//2-20, 155, W//2+dw_val//2+20, 195), 10, fill=RED)
    center_text(draw, day_text, 158, font('mono', 30), WHITE)

    center_text(draw, ar("٣٨ يوماً غيّرت خارطة الشرق الأوسط"), 210, font('ar_med', 18), GOLD)

    # === VERTICAL TIMELINE ===
    tl_x = W - 100  # Timeline axis
    y = 290

    events = [
        ("28 FEB", ar("الضربة الأولى"), ar("غارات أمريكية-إسرائيلية مفاجئة"), ar("اغتيال خامنئي ومسؤولين كبار"), RED, True),
        ("01 MAR", ar("الرد الإيراني"), ar("صواريخ ومسيّرات على إسرائيل"), ar("إغلاق مضيق هرمز"), GOLD, True),
        ("02 MAR", ar("حزب الله يدخل"), ar("صواريخ على إسرائيل دعماً لإيران"), ar("بدء القصف والاجتياح البري"), ACCENT_ORANGE, False),
        ("08 MAR", ar("قيادة جديدة"), ar("مجتبى خامنئي مرشداً أعلى"), ar("الحرس الثوري يبايع"), WHITE_60, False),
        ("07 APR", ar("الموعد النهائي"), ar("مهلة ترامب لفتح المضيق"), ar("إيران تقدم خطة من ١٠ نقاط"), RED, True),
    ]

    for i, (date, title, desc1, desc2, color, important) in enumerate(events):
        ey = y + i * 165

        # Timeline line
        if i < len(events) - 1:
            for ly in range(ey+20, ey+165):
                t = (ly - ey - 20) / 145
                c = tuple(int(color[j] * (1-t) + events[i+1][4][j] * t) // 3 for j in range(3))
                draw.line([tl_x, ly, tl_x, ly+1], fill=c)

        # Timeline node
        node_r = 12 if important else 8
        draw.ellipse([tl_x-node_r, ey+8-node_r, tl_x+node_r, ey+8+node_r], fill=color)
        if important:
            draw.ellipse([tl_x-node_r+3, ey+8-node_r+3, tl_x+node_r-3, ey+8+node_r-3], fill=DARK3)
            draw.ellipse([tl_x-4, ey+4, tl_x+4, ey+12], fill=color)

        # Date badge
        rrect(draw, (tl_x-85, ey-5, tl_x-15, ey+22), 6, fill=color if important else CARD_BG)
        dtw = tw(draw, date, font('mono_r', 11))
        draw.text((tl_x-50-dtw//2, ey-1), date, font=font('mono_r', 11), fill=WHITE if important or color == WHITE_60 else DARK3)

        # Content card
        card_bg = (55, 28, 32) if color == RED else CARD_BG
        rrect(draw, (50, ey-10, tl_x-105, ey+135), 14, fill=card_bg, outline=WHITE_20 if not important else color)

        # Accent bar
        draw.rectangle([tl_x-109, ey, tl_x-105, ey+125], fill=color)

        # Title
        draw.text((65, ey+5), title, font=font('ar_black', 20), fill=color if color != WHITE_60 else WHITE)

        # Descriptions
        draw.text((65, ey+40), desc1, font=font('ar_med', 16), fill=WHITE_80)
        draw.text((65, ey+70), desc2, font=font('ar', 15), fill=WHITE_40)

        # Impact meter for key events
        if important:
            draw.text((65, ey+100), ar("التأثير"), font=font('ar', 12), fill=WHITE_40)
            impact = 95 if i == 0 else 85 if i == 1 else 90
            draw_progress_bar(draw, 130, ey+105, tl_x-250, 8, impact, color)

    # Bottom
    draw.rectangle([0, H-60, W, H], fill=RED)
    draw.text((65, H-44), ar("٣٨ يوماً من التصعيد المتواصل"), font=font('ar_bold', 14), fill=WHITE)
    draw_page_indicator(draw, 4, 8, H-22)

    img.save(os.path.join(OUT, "05_iran.png"), quality=95)
    print("  Slide 5 saved")
    return img


# ============================================================
# SLIDE 6: WEST BANK
# ============================================================
def slide_6():
    img = Image.new('RGB', (W, H), LIGHT_BG)
    draw = ImageDraw.Draw(img)

    # Header
    gradient_rect(img, (0, 0, W, 280), DARK3, DARK)
    draw = ImageDraw.Draw(img)

    rrect(draw, (W-190, 28, W-55, 55), 14, fill=GOLD)
    draw.text((W-140, 30), ar("الضفة الغربية"), font=font('ar_bold', 14), fill=DARK)
    draw.text((60, 34), "6 / 8", font=font('en_bold', 14), fill=WHITE_40)
    draw_logo(draw, W//2-65, 15, 0.8)

    center_text(draw, ar("الأزمة الصامتة"), 90, font('ar_black', 52), WHITE)
    center_text(draw, ar("عنف المستوطنين بأرقام غير مسبوقة"), 165, font('ar_med', 19), GOLD)

    # Escalation arrow indicator
    draw.line([200, 230, W-200, 230], fill=RED, width=3)
    for ax in range(200, W-200, 40):
        draw.polygon([(ax+20, 225), (ax+30, 230), (ax+20, 235)], fill=RED)

    # === BAR CHART — Settler violence comparison ===
    y = 310
    rrect(draw, (50, y, W-50, y+270), 18, fill=WHITE)

    center_text(draw, ar("المعدل الشهري لإصابات الفلسطينيين"), y+15, font('ar_bold', 17), DARK)
    center_text(draw, ar("في هجمات المستوطنين"), y+42, font('ar', 14), (140,140,140))

    # Vertical bar chart
    chart_x = 120
    chart_y = y + 80
    chart_h = 150
    chart_w = W - 240

    bars = [
        ("2024", 30, (180,180,180)),
        ("2025", 69, (140,140,140)),
        ("2026", 105, RED),
    ]

    max_val = 120
    bar_w = chart_w // (len(bars) * 2 + 1)
    gap = bar_w

    for i, (year, val, color) in enumerate(bars):
        bx = chart_x + gap + i * (bar_w + gap)
        bar_h = int(val / max_val * chart_h)
        by = chart_y + chart_h - bar_h

        # Bar
        rrect(draw, (bx, by, bx+bar_w, chart_y+chart_h), 6, fill=color)

        # Value on top
        vt = str(val)
        vw = tw(draw, vt, font('en_bold', 22))
        draw.text((bx+(bar_w-vw)//2, by-30), vt, font=font('en_bold', 22), fill=color)

        # Year below
        yw = tw(draw, year, font('mono_r', 13))
        draw.text((bx+(bar_w-yw)//2, chart_y+chart_h+8), year, font=font('mono_r', 13), fill=(140,140,140))

    # +250% badge
    pct_badge_w = 130
    rrect(draw, (W//2-pct_badge_w//2, chart_y+chart_h+35, W//2+pct_badge_w//2, chart_y+chart_h+65), 8, fill=RED)
    center_text(draw, "+250%", chart_y+chart_h+38, font('mono', 20), WHITE)

    # === DISPLACEMENT FACTS ===
    y2 = y + 290
    facts = [
        ("1,697", ar("فلسطيني مهجّر في ٢٠٢٦"), ar("تجاوز إجمالي عام ٢٠٢٥ بالكامل"), RED, 100),
        ("600K+", ar("ممنوعون من العودة"), ar("في المنطقة الأمنية المخطط لها بلبنان"), ACCENT_ORANGE, 60),
    ]

    for i, (num, title, sub, color, pct) in enumerate(facts):
        fy = y2 + i * 135
        rrect(draw, (50, fy, W-50, fy+120), 14, fill=WHITE)
        draw.rectangle([W-54, fy+10, W-50, fy+110], fill=color)

        # Number
        draw.text((W-90, fy+10), num, font=font('mono', 34), fill=color)

        # Text
        draw.text((65, fy+18), title, font=font('ar_bold', 18), fill=DARK)
        draw.text((65, fy+50), sub, font=font('ar', 15), fill=(140,140,140))

        # Bar
        draw_progress_bar(draw, 65, fy+90, W-180, 8, pct, color, (230,230,230))

    # === OCHA NOTE ===
    y3 = y2 + 290
    rrect(draw, (50, y3, W-50, y3+80), 14, fill=(255,240,240))
    draw.rectangle([W-54, y3+10, W-50, y3+70], fill=RED)

    draw.text((65, y3+10), ar("مكتب الأمم المتحدة OCHA:"), font=font('ar_bold', 16), fill=RED)
    draw.text((65, y3+40), ar("تصاعد العنف يترافق مع توسع استيطاني غير مسبوق"), font=font('ar', 15), fill=DARK)

    # Bottom
    draw.rectangle([0, H-60, W, H], fill=DARK)
    draw.text((65, H-44), ar("المصدر: مكتب الأمم المتحدة لتنسيق الشؤون الإنسانية"), font=font('ar', 13), fill=GOLD)
    draw_page_indicator(draw, 5, 8, H-22)

    img.save(os.path.join(OUT, "06_westbank.png"), quality=95)
    print("  Slide 6 saved")
    return img


# ============================================================
# SLIDE 7: GLOBAL IMPACT
# ============================================================
def slide_7():
    img = Image.new('RGB', (W, H), DARK3)
    draw = ImageDraw.Draw(img)
    draw_dot_pattern(draw, 0, 300, W, 600, 20, (32, 32, 32))

    # Header
    gradient_rect(img, (0, 0, W, 260), (35, 32, 28), DARK3)
    draw = ImageDraw.Draw(img)

    rrect(draw, (W-195, 28, W-55, 55), 14, fill=GOLD)
    draw.text((W-145, 30), ar("التأثير العالمي"), font=font('ar_bold', 14), fill=DARK)
    draw.text((60, 34), "7 / 8", font=font('en_bold', 14), fill=WHITE_40)
    draw_logo(draw, W//2-65, 15, 0.8)

    center_text(draw, ar("كيف يؤثر هذا عليك؟"), 90, font('ar_black', 48), WHITE)
    center_text(draw, ar("الأرقام التي تهمّك"), 160, font('ar_med', 19), GOLD)

    # Thin gold line
    draw.line([W//2-60, 200, W//2+60, 200], fill=GOLD, width=2)

    # === IMPACT GRID 2x2 with charts ===
    y = 230
    cw = (W - 130) // 2
    ch = 175

    impacts = [
        ("$116", ar("سعر النفط الأمريكي"), ar("ارتفاع +٤٠٪ عن ما قبل الحرب"), RED, [65,70,75,80,92,108,116]),
        ("20%", ar("من النفط العالمي"), ar("كان يمر عبر مضيق هرمز"), GOLD, None),
        ("3+", ar("دول في حالة حرب"), ar("إسرائيل — إيران — لبنان"), RED, None),
        ("2.2M+", ar("نازح في المنطقة"), ar("غزة + لبنان مجتمعين"), GOLD, [0,10,50,200,500,1200,2200]),
    ]

    for i, (num, l1, l2, color, chart_data) in enumerate(impacts):
        col, row = i % 2, i // 2
        cx = 50 + col * (cw + 30)
        cy = y + row * (ch + 14)

        rrect(draw, (cx, cy, cx+cw, cy+ch), 16, fill=CARD_BG, outline=WHITE_20)

        # Mini chart if available
        if chart_data:
            fill_c = (color[0]//6, color[1]//6, color[2]//6)
            draw_line_chart(draw, cx+15, cy+10, cw-30, 50, chart_data, color, fill_c)

        # Number
        nf = font('mono', 38)
        nw_val = tw(draw, num, nf)
        draw.text((cx+(cw-nw_val)//2, cy+65), num, font=nf, fill=color)

        # Labels
        lw1 = tw(draw, l1, font('ar_bold', 15))
        draw.text((cx+(cw-lw1)//2, cy+115), l1, font=font('ar_bold', 15), fill=WHITE_60)
        lw2 = tw(draw, l2, font('ar', 13))
        draw.text((cx+(cw-lw2)//2, cy+140), l2, font=font('ar', 13), fill=WHITE_40)

    # === WHAT TO WATCH ===
    y2 = y + 2*(ch+14) + 25
    rrect(draw, (50, y2, W-50, y2+400), 18, fill=(48, 43, 28), outline=GOLD_DIM)

    draw.text((W-80, y2+15), ar("ما الذي نراقبه؟"), font=font('ar_black', 24), fill=GOLD)

    # Decorative line under title
    draw.line([W-80, y2+52, W-250, y2+52], fill=GOLD_DIM, width=2)

    watch = [
        (ar("الليلة"), ar("هل ستفتح إيران المضيق قبل الموعد؟"), RED, 95),
        (ar("هذا الأسبوع"), ar("جلسة مجلس الأمن حول فلسطين — البحرين"), GOLD, 70),
        (ar("الاجتياح البري"), ar("فرقة إسرائيلية ثانية في جنوب لبنان"), ACCENT_ORANGE, 80),
        (ar("غزة"), ar("مفاوضات متعثرة. حماس تعلن عن ٢٠ رهينة"), RED, 60),
    ]

    for i, (label, desc, color, urgency) in enumerate(watch):
        wy = y2 + 70 + i * 80

        # Urgency indicator
        draw_donut(draw, 85, wy+20, 16, 10, urgency, color)

        # Label
        draw.text((110, wy), label, font=font('ar_bold', 18), fill=color)
        draw.text((110, wy+30), desc, font=font('ar', 15), fill=WHITE_60)

        # Urgency bar
        draw_progress_bar(draw, 110, wy+55, W-210, 4, urgency, color)

    # Bottom gold strip
    draw.rectangle([0, H-65, W, H], fill=GOLD)
    draw.text((65, H-48), ar("الصفحة التالية: المصادر"), font=font('ar_bold', 17), fill=DARK3)
    draw_page_indicator(draw, 6, 8, H-22)

    img.save(os.path.join(OUT, "07_impact.png"), quality=95)
    print("  Slide 7 saved")
    return img


# ============================================================
# SLIDE 8: SOURCES
# ============================================================
def slide_8():
    img = Image.new('RGB', (W, H), DARK3)
    draw = ImageDraw.Draw(img)
    draw_dot_pattern(draw, 0, 200, W, 800, 24, (30, 30, 30))

    # Logo section
    draw_logo(draw, W//2-85, 30, 1.3)

    draw.line([120, 120, W-120, 120], fill=WHITE_20, width=1)

    center_text(draw, ar("المصادر"), 135, font('ar_black', 40), WHITE)
    center_text(draw, ar("نحن لا نكذب — تحقق بنفسك"), 185, font('ar_med', 18), WHITE_40)

    draw.line([120, 225, W-120, 225], fill=WHITE_20, width=1)

    # Sources list
    y = 245
    sources = [
        ("01", "Al Jazeera", "aljazeera.com", ar("تغطية مباشرة للأحداث")),
        ("02", "Security Council Report", "securitycouncilreport.org", ar("تقارير مجلس الأمن")),
        ("03", "CNBC", "cnbc.com", ar("أسواق النفط والطاقة")),
        ("04", "WAFA", "english.wafa.ps", ar("وكالة الأنباء الفلسطينية")),
        ("05", "OCHA", "ochaopt.org", ar("الشؤون الإنسانية")),
        ("06", "Washington Post", "washingtonpost.com", ar("تحليلات وتقارير")),
        ("07", "Wikipedia", "en.wikipedia.org", ar("جداول زمنية وإحصائيات")),
        ("08", "Human Rights Watch", "hrw.org", ar("حقوق الإنسان")),
        ("09", "PBS News", "pbs.org", ar("تحليل السياسة الأمريكية")),
        ("10", "The Lancet", "thelancet.com", ar("دراسات الوفيات المستقلة")),
    ]

    for i, (num, name, url, desc_ar) in enumerate(sources):
        sy = y + i * 72
        rrect(draw, (50, sy, W-50, sy+62), 12, fill=CARD_BG)
        draw.rectangle([W-54, sy+6, W-50, sy+56], fill=GOLD)

        # Number circle
        rrect(draw, (W-110, sy+14, W-72, sy+48), 8, fill=GOLD)
        nw_val = tw(draw, num, font('mono', 14))
        draw.text((W-91-nw_val//2, sy+18), num, font=font('mono', 14), fill=DARK3)

        # Source name
        draw.text((70, sy+8), name, font=font('en_bold', 17), fill=WHITE)

        # URL
        draw.text((70, sy+32), url, font=font('mono_r', 11), fill=WHITE_40)

        # Arabic desc
        draw.text((300, sy+32), desc_ar, font=font('ar', 13), fill=WHITE_40)

    # === BOTTOM SECTION ===
    by = H - 180
    draw.line([50, by, W-50, by], fill=WHITE_20, width=1)

    # Logo
    draw_logo(draw, W//2-75, by+15, 1.0)

    # Follow CTA
    center_text(draw, ar("تابعنا — الأخبار كل ساعتين"), by+80, font('ar_med', 17), WHITE_40)

    # Handle with gold
    handle = "@PhotonectNEWS"
    hw = tw(draw, handle, font('en_bold', 26))
    draw.text(((W-hw)//2, by+110), handle, font=font('en_bold', 26), fill=GOLD)

    center_text(draw, ar("أخبار بلا تحيّز — معلومات تستحق وقتك"), by+148, font('ar', 15), WHITE_20)

    draw_page_indicator(draw, 7, 8, H-18)

    img.save(os.path.join(OUT, "08_sources.png"), quality=95)
    print("  Slide 8 saved")
    return img


# ============================================================
if __name__ == "__main__":
    print("PHOTONECT NEWS V2 — Building carousel...")
    print("=" * 50)
    for fn in [slide_1, slide_2, slide_3, slide_4, slide_5, slide_6, slide_7, slide_8]:
        fn()
    print("=" * 50)
    print(f"All slides saved to: {OUT}")
    for f in sorted(os.listdir(OUT)):
        if f.endswith('.png'):
            sz = os.path.getsize(os.path.join(OUT, f))
            print(f"  {f} ({sz//1024}KB)")
