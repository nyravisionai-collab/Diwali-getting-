#!/usr/bin/env python3
"""Build ElectricalSkart Diwali greeting cards from the AI artwork + IM text layers."""
import os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ART = os.path.join(ROOT, "assets", "diwali-art.jpg")
FONTS = os.path.join(ROOT, "assets", "fonts-static")
TMP = os.path.join(ROOT, ".build", "tmp")
OUT = os.path.join(ROOT, "cards")
os.makedirs(TMP, exist_ok=True)
os.makedirs(OUT, exist_ok=True)
_fc = os.path.join(ROOT, ".build", "fonts.conf")
os.makedirs(os.path.dirname(_fc), exist_ok=True)
if not os.path.exists(_fc) or os.path.getmtime(_fc) < os.path.getmtime(__file__) - 1e9:
    pass  # content (re)written below every run
with open(_fc, "w", encoding="utf-8") as _f:
    _f.write('<?xml version="1.0"?>\n<!DOCTYPE fontconfig SYSTEM "fonts.dtd">\n<fontconfig>\n'
             f'  <dir>{os.path.join(ROOT, "assets", "fonts-static")}</dir>\n'
             f'  <cachedir>{os.path.join(ROOT, ".build", "fontcache")}</cachedir>\n</fontconfig>\n')
os.environ["FONTCONFIG_FILE"] = _fc

F_SERIF_XB = os.path.join(FONTS, "NotoSerifGujarati-ExtraBold.ttf")
F_SERIF_SB = os.path.join(FONTS, "NotoSerifGujarati-SemiBold.ttf")
F_SANS_B   = os.path.join(FONTS, "NotoSansGujarati-Bold.ttf")
F_SANS     = os.path.join(FONTS, "NotoSansGujarati-Regular.ttf")
F_PLAY_BLK = os.path.join(FONTS, "PlayfairDisplay-Black.ttf")
F_PLAY_B   = os.path.join(FONTS, "PlayfairDisplay-Bold.ttf")

GOLD, GOLD2, CREAM, SOFT = "#ffd166", "#f4a261", "#ffedc9", "#f6d9a0"

def im(*args, check=True):
    args = list(args)
    out = args[-1]
    if isinstance(out, str) and out.lower().endswith(".jpg"):
        args = args[:-1] + ["-quality", "92"] + [out]
    subprocess.run(["convert", *args], check=check)

def text_width(font, size, text):
    r = subprocess.run(["convert", "-size", "10x10", "xc:none", "-font", font,
                        "-pointsize", str(size), "-debug", "annotate", "-fill", "white",
                        "-annotate", "+0+0", text, "null:"],
                       capture_output=True, text=True)
    for line in (r.stdout + r.stderr).splitlines():
        if "Metrics:" in line:
            for part in line.split(";"):
                part = part.strip()
                if part.startswith("width:"):
                    return float(part.split(":")[1].strip())
    return 0.0

def fit_size(font, size, text, max_width):
    s = size
    while s > 12 and text_width(font, s, text) > max_width:
        s -= 2
    return s

HALO = []
for _dx in (-3, 0, 3):
    for _dy in (-3, 0, 3):
        if (_dx, _dy) != (0, 0):
            HALO.append((_dx, _dy))

def annotate(src, out, lines):
    """Draw centered text lines. halo=<color> draws an 8-direction hard halo,
    shadow=(dx,dy,color) draws a single drop shadow. No blur operators anywhere."""
    args = [src]
    for ln in lines:
        if ln.get("halo"):
            for dx, dy in HALO:
                args += ["-font", ln["font"], "-pointsize", str(ln["size"]), "-fill", ln["halo"],
                         "-gravity", "north", "-annotate", f"+{dx}+{ln['y']+dy}", ln["text"]]
        sh = ln.get("shadow")
        if sh:
            dx, dy, color = sh
            args += ["-font", ln["font"], "-pointsize", str(ln["size"]), "-fill", color,
                     "-gravity", "north", "-annotate", f"+{dx}+{ln['y']+dy}", ln["text"]]
    for ln in lines:
        args += ["-font", ln["font"], "-pointsize", str(ln["size"]), "-fill", ln["fill"],
                 "-gravity", "north", "-annotate", f"+0+{ln['y']}", ln["text"]]
    im(*args, out)

def dots(path, cx, y, r=7, gap=52, color=GOLD):
    args = [path]
    for dx in (-gap, 0, gap):
        args += ["-fill", color, "-draw", f"circle {cx+dx},{y} {cx+dx},{y+r}"]
    im(*args, path)

def bolt_points(cx, cy, s):
    rel = [(0.36, -1.0), (-0.42, 0.14), (0.02, 0.14), (-0.34, 1.0),
           (0.46, -0.14), (0.04, -0.14), (0.62, -1.0)]
    return " ".join(f"{cx + rx*s:.0f},{cy + ry*s:.0f}" for rx, ry in rel)

def add_bolt(src, out, cx, cy, s, fill=GOLD):
    im(src, "-fill", fill, "-stroke", "#6b3f00", "-strokewidth", str(max(2, s // 16)),
       "-draw", f"polygon {bolt_points(cx, cy, s)}", "-stroke", "none", out)

LANGS = {
    "gu": dict(greet="શુભ દિવાળી", sub="દીપોના પ્રકાશ સાથે તમારા જીવનમાં ખુશી અને સમૃદ્ધિ પથરાય",
               tag="તમારા ઘર માટે — ઈલેક્ટ્રિકલ સોલ્યુશન",
               big_font=F_SERIF_XB, big_size=200, greet2=None),
    "en": dict(greet="Happy Diwali", sub="May the festival of lights fill your home with joy & prosperity.",
               tag="Electrical solutions for a brighter home",
               big_font=F_PLAY_BLK, big_size=225, greet2=None),
    "bi": dict(greet="શુભ દિવાળી", greet2="HAPPY DIWALI",
               sub="દીપોનો પ્રકાશ તમારા જીવનને પ્રકાશિત કરે · May your life keep shining bright",
               tag="તમારા ઘર માટે ઈલેક્ટ્રિકલ સોલ્યુશન · Electrical solutions for a brighter home",
               big_font=F_SERIF_XB, big_size=155),
}
BRAND = "E L E C T R I C A L S K A R T . C O M"

def landscape(key):
    W, H = 2816, 1536
    bg = os.path.join(TMP, f"land_bg_{key}.png")
    im(ART, "-resize", f"{W}x{H}!", bg)
    L = LANGS[key]
    lines = [dict(text=BRAND, font=F_PLAY_B, size=44, fill=SOFT, y=128, shadow=(0,4,"#12030c"))]
    if L["greet2"]:
        lines.append(dict(text=L["greet"], font=L["big_font"], size=180, fill=GOLD, y=258, halo="#7a3c00"))
        lines.append(dict(text=L["greet2"], font=F_PLAY_BLK, size=96, fill=CREAM, y=600, shadow=(0,4,"#12030c")))
        dots_y = 756
    else:
        lines.append(dict(text=L["greet"], font=L["big_font"], size=L["big_size"], fill=GOLD, y=300, halo="#7a3c00"))
        dots_y = 712
    sub_size = fit_size(F_SANS_B, 46, L["sub"], W - 760)
    tag_size = fit_size(F_SANS, 37, L["tag"], W - 900)
    lines.append(dict(text=L["sub"], font=F_SANS_B, size=sub_size, fill=CREAM, y=dots_y + 32, shadow=(0,4,"#12030c")))
    lines.append(dict(text=L["tag"], font=F_SANS, size=tag_size, fill=GOLD2, y=dots_y + 126, shadow=(0,4,"#12030c")))
    mid = os.path.join(TMP, f"land_mid_{key}.png")
    annotate(bg, mid, lines)
    dots(mid, W // 2, dots_y, r=6, gap=46)
    final = os.path.join(OUT, f"ElectricalSkart-Diwali-Card-{key.upper()}-Banner.jpg")
    add_bolt(mid, final, W // 2, 72, 32)
    print("saved", final)

def square(key):
    S = 2000
    bg = os.path.join(TMP, f"sq_bg_{key}.png")
    art_w = S - 220
    art_h = int(art_w * 768 / 1408)
    arty = 205
    # gradient background + soft radial glow
    glow_img = os.path.join(TMP, f"sq_radial_{key}.png")
    im("-size", f"{S}x{S}", "gradient:#33112c-#150512", bg)
    im("-size", f"{S}x{S}", "radial-gradient:#5c2440-#00000000", glow_img)
    im(bg, glow_img, "-compose", "screen", "-composite", bg)
    # artwork as a gold-matted panel (no alpha ops: crisp & deterministic)
    art = os.path.join(TMP, f"sq_art_{key}.png")
    im(ART, "-resize", f"{art_w}x{art_h}!", art)
    artx = (S - art_w) // 2
    pad = 16
    im(bg, "-fill", GOLD2, "-stroke", "#6b3f00", "-strokewidth", "3",
       "-draw", f"roundrectangle {artx-pad},{arty-pad} {artx+art_w+pad},{arty+art_h+pad} 26,26",
       "-stroke", "none", bg)
    im(bg, "-fill", "#571d33",
       "-draw", f"roundrectangle {artx-6},{arty-6} {artx+art_w+6},{arty+art_h+6} 20,20", bg)
    im(bg, art, "-geometry", f"+{artx}+{arty}", "-composite", bg)
    art_bottom = arty + art_h
    L = LANGS[key]
    lines = [dict(text=BRAND, font=F_PLAY_B, size=36, fill=SOFT, y=100, shadow=(0,4,"#12030c"))]
    if L["greet2"]:
        lines.append(dict(text=L["greet"], font=L["big_font"], size=132, fill=GOLD,
                          y=art_bottom + 66, halo="#7a3c00"))
        lines.append(dict(text=L["greet2"], font=F_PLAY_BLK, size=70, fill=CREAM,
                          y=art_bottom + 256, shadow=(0,4,"#12030c")))
        dots_y = art_bottom + 392
    else:
        gsize = fit_size(L["big_font"], L["big_size"], L["greet"], S - 340)
        lines.append(dict(text=L["greet"], font=L["big_font"], size=gsize, fill=GOLD,
                          y=art_bottom + 76, halo="#7a3c00"))
        dots_y = art_bottom + 398
    sub_size = fit_size(F_SANS_B, 33, L["sub"], S - 260)
    tag_size = fit_size(F_SANS, 26, L["tag"], S - 240)
    lines.append(dict(text=L["sub"], font=F_SANS_B, size=sub_size, fill=CREAM, y=dots_y + 24, shadow=(0,4,"#12030c")))
    lines.append(dict(text=L["tag"], font=F_SANS, size=tag_size, fill=GOLD2, y=dots_y + 108, shadow=(0,4,"#12030c")))
    mid = os.path.join(TMP, f"sq_mid_{key}.png")
    annotate(bg, mid, lines)
    dots(mid, S // 2, dots_y, r=5, gap=38)
    framed = os.path.join(TMP, f"sq_frame_{key}.png")
    im(mid, "-stroke", GOLD2, "-strokewidth", "6", "-fill", "none",
       "-draw", "rectangle 30,30 1969,1969",
       "-stroke", GOLD, "-strokewidth", "2", "-draw", "rectangle 52,52 1947,1947", framed)
    final = os.path.join(OUT, f"ElectricalSkart-Diwali-Card-{key.upper()}.jpg")
    # lightning-bolt medallion astride the top frame
    med = os.path.join(TMP, f"sq_med_{key}.png")
    im("-size", f"{S}x{S}", "xc:none",
       "-fill", "#3a1030", "-stroke", GOLD2, "-strokewidth", "7",
       "-draw", f"circle {S//2},41 {S//2},81",
       "-stroke", "none", med)
    im(framed, med, "-geometry", "+0+0", "-composite", med)
    add_bolt(med, final, S // 2, 41, 25)
    print("saved", final)

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    for k in ["gu", "en", "bi"]:
        if which in ("all", "landscape"):
            landscape(k)
        if which in ("all", "square"):
            square(k)
