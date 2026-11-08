#!/usr/bin/env python3
"""Generate letterhead assets for the ElectricalSkart Diwali letters/emails."""
import os, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ART = os.path.join(ROOT, "assets", "diwali-art.jpg")
FONTS = os.path.join(ROOT, "assets", "fonts-static")
OUT = os.path.join(ROOT, "assets")
_fc = os.path.join(ROOT, ".build", "fonts.conf")
os.makedirs(os.path.dirname(_fc), exist_ok=True)
if not os.path.exists(_fc) or os.path.getmtime(_fc) < os.path.getmtime(__file__) - 1e9:
    pass  # content (re)written below every run
with open(_fc, "w", encoding="utf-8") as _f:
    _f.write('<?xml version="1.0"?>\n<!DOCTYPE fontconfig SYSTEM "fonts.dtd">\n<fontconfig>\n'
             f'  <dir>{os.path.join(ROOT, "assets", "fonts-static")}</dir>\n'
             f'  <cachedir>{os.path.join(ROOT, ".build", "fontcache")}</cachedir>\n</fontconfig>\n')
os.environ["FONTCONFIG_FILE"] = _fc
W = 2400

def im(*a):
    subprocess.run(["convert", *a], check=True)

# ---------- top brand band ----------
top = os.path.join(OUT, "letterhead-top.png")
im("-size", f"{W}x340", "gradient:#43102f-#26081f", top)
# subtle corner glow
im("-size", f"{W}x340", "radial-gradient:#6d2b44-#00000000", os.path.join(ROOT, ".build", "tmp", "lh_glow.png"))
im(top, os.path.join(ROOT, ".build", "tmp", "lh_glow.png"), "-compose", "screen", "-composite", top)
bolt = [(0.36,-1.0),(-0.42,0.14),(0.02,0.14),(-0.34,1.0),(0.46,-0.14),(0.04,-0.14),(0.62,-1.0)]
bx, by, s = W//2, 86, 46
pts = " ".join(f"{bx+rx*s:.0f},{by+ry*s:.0f}" for rx, ry in bolt)
im(top, "-fill", "#ffd166", "-stroke", "#6b3f00", "-strokewidth", "4", "-draw", f"polygon {pts}", "-stroke", "none", top)
im(top,
   "-font", FONTS + "/PlayfairDisplay-Black.ttf", "-pointsize", "72", "-fill", "#ffd166",
   "-gravity", "north", "-annotate", "+0+128", "E L E C T R I C A L S K A R T . C O M",
   top)
im(top,
   "-font", FONTS + "/NotoSansGujarati-Regular.ttf", "-pointsize", "23", "-fill", "#e9cfa4",
   "-gravity", "north", "-annotate", "+0+225", "તમારા ઘર માટે — ઈલેક્ટ્રિકલ સોલ્યુશન  ·  Electrical solutions for a brighter home",
   top)
# double gold rule at the very bottom of the band
im(top, "-fill", "#c9a24b", "-draw", f"rectangle 0,310 {W-1},316", top)
im(top, "-fill", "#ffd166", "-draw", f"rectangle 0,322 {W-1},325", top)
print("saved", top)

# ---------- bottom diya strip ----------
strip = os.path.join(OUT, "letterhead-diya.jpg")
crop = os.path.join(ROOT, ".build", "tmp", "lh_crop.png")
im(ART, "-crop", "1408x268+0+476", "+repage", crop)     # thali of diyas + rangoli top
im(crop, "-resize", "2000x", "-quality", "90", strip)
print("saved", strip)

# ---------- favicon-ish bolt on maroon (for ecard) ----------
print("letterhead assets done")
