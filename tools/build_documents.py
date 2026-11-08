#!/usr/bin/env python3
"""Build ElectricalSkart Diwali 2026 documents:
   .docx (editable), .pdf (print-ready, IM-rendered pages), .txt (copy-paste)."""
import os, re, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import CONTENT, CARD_FOR

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTS = os.path.join(ROOT, "assets", "fonts-static")
ASSETS = os.path.join(ROOT, "assets")
CARDS = os.path.join(ROOT, "cards")
DOCS = os.path.join(ROOT, "documents")
TMP = os.path.join(ROOT, ".build", "tmp")
os.makedirs(DOCS, exist_ok=True)
os.makedirs(TMP, exist_ok=True)
_fc = os.path.join(ROOT, ".build", "fonts.conf")
os.makedirs(os.path.dirname(_fc), exist_ok=True)
if not os.path.exists(_fc) or os.path.getmtime(_fc) < os.path.getmtime(__file__) - 1e9:
    pass  # content (re)written below every run
with open(_fc, "w", encoding="utf-8") as _f:
    _f.write('<?xml version="1.0"?>\n<!DOCTYPE fontconfig SYSTEM "fonts.dtd">\n<fontconfig>\n'
             f'  <dir>{os.path.join(ROOT, "assets", "fonts-static")}</dir>\n'
             f'  <cachedir>{os.path.join(ROOT, ".build", "fontcache")}</cachedir>\n</fontconfig>\n')
os.environ["FONTCONFIG_FILE"] = _fc

F_SERIF_XB = FONTS + "/NotoSerifGujarati-ExtraBold.ttf"
F_SERIF_SB = FONTS + "/NotoSerifGujarati-SemiBold.ttf"
F_SERIF    = FONTS + "/NotoSerifGujarati-Regular.ttf"
F_SANS     = FONTS + "/NotoSansGujarati-Regular.ttf"
F_SANS_B   = FONTS + "/NotoSansGujarati-Bold.ttf"
F_PLAY_BLK = FONTS + "/PlayfairDisplay-Black.ttf"
F_PLAY_B   = FONTS + "/PlayfairDisplay-Bold.ttf"
F_PLAY     = FONTS + "/PlayfairDisplay-Regular.ttf"
F_PLAY_IT  = FONTS + "/PlayfairDisplay-SemiBoldItalic.ttf"

INK      = "#2c2721"
MAROON   = "#4a1030"
GOLD     = "#ffd166"
GOLD_D   = "#a4761c"
GOLD_R   = "#c9a24b"
SOFT     = "#e9cfa4"
GRAY     = "#55504a"
IVORY    = "#fffdf6"

def im(*args, check=True):
    subprocess.run(["convert", *args], check=check)

_metric_cache = {}
def text_width(font, size, text):
    key = (font, size, text)
    if key in _metric_cache:
        return _metric_cache[key]
    r = subprocess.run(["convert", "-size", "10x10", "xc:none", "-font", font,
                        "-pointsize", str(size), "-debug", "annotate", "-fill", "white",
                        "-annotate", "+0+0", text, "null:"],
                       capture_output=True, text=True)
    w = 0.0
    for line in (r.stdout + r.stderr).splitlines():
        if "Metrics:" in line:
            for part in line.split(";"):
                part = part.strip()
                if part.startswith("width:"):
                    w = float(part.split(":")[1].strip())
    _metric_cache[key] = w
    return w

def wrap(text, font, size, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if text_width(font, size, trial) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def draw(src, out, text, font, size, fill, y, anchor="west", x=160, page_w=1654):
    if anchor == "center":
        im(src, "-font", font, "-pointsize", str(size), "-fill", fill,
           "-gravity", "north", "-annotate", f"+0+{y}", text, out)
    elif anchor == "east":
        im(src, "-font", font, "-pointsize", str(size), "-fill", fill,
           "-gravity", "northeast", "-annotate", f"+{x}+{y}", text, out)
    else:
        im(src, "-font", font, "-pointsize", str(size), "-fill", fill,
           "-gravity", "northwest", "-annotate", f"+{x}+{y}", text, out)

def body_font_for(text, style):
    if style == "en":
        return F_PLAY_IT, 27
    if style == "gu":
        return F_SERIF, 30
    return (F_SERIF if any('\u0a80' <= ch <= '\u0aff' for ch in text) else F_PLAY), 30

# ---------------- PDF page rendering (IM -> PNG, reportlab -> PDF) ----------------
PAGE_W, PAGE_H = 1654, 2339
STRIP_H = 313
BOTTOM_LIMIT = PAGE_H - STRIP_H - 66   # keep clear of diya strip + footer
MX = 160
TEXT_W = PAGE_W - 2 * MX

class PageBuilder:
    def __init__(self, tag):
        self.tag = tag
        self.pages = []
        self.new_page()

    def new_page(self):
        self.idx = len(self.pages)
        path = os.path.join(TMP, f"doc_{self.tag}_{self.idx}.jpg")
        im("-size", f"{PAGE_W}x{PAGE_H}", f"xc:{IVORY}", path)
        self.pages.append(path)
        self.y = 0

    @property
    def path(self):
        return self.pages[-1]

    def paste(self, img, x, y, w=None):
        args = [self.path, img]
        if w:
            args = [self.path, "(", img, "-resize", f"{w}x", ")"]
        im(*args, "-geometry", f"+{x}+{y}", "-composite", self.path)

    def line(self, y=None):
        pass

    def ensure(self, needed):
        if self.y + needed > BOTTOM_LIMIT:
            self.new_page()
            draw(self.path, self.path, "ElectricalSkart.com — દિવાળી ૨૦૨૬ · Diwali 2026",
                 F_SANS, 24, GOLD_D, 46, anchor="east", x=MX)
            self.y = 110

    def para(self, text, font, size, fill, gap_before=0, gap_after=22, line_h=None, bold=False, anchor="west"):
        line_h = line_h or int(size * 1.52)
        for ln in wrap(text, font, size, TEXT_W):
            self.ensure(line_h)
            draw(self.path, self.path, ln, font, size, fill, self.y + gap_before, anchor=anchor, x=MX)
            self.y += line_h
        self.y += gap_after

    def rule(self, color=GOLD_R, thickness=5, gap_after=16, width=None):
        w = width or TEXT_W
        im(self.path, "-fill", color, "-draw", f"rectangle {MX},{self.y} {MX+w-1},{self.y+thickness-1}", self.path)
        self.y += thickness + gap_after

def render_page_bg(pb, kind):
    top = os.path.join(ASSETS, "letterhead-top.png")
    strip = os.path.join(ASSETS, "letterhead-diya.jpg")
    pb.paste(top, 0, 0, w=PAGE_W)
    pb.y = 252
    return STRIP_H

def build_pdf_pages(kind, lang, data):
    tag = f"{kind}_{lang}".lower()
    pb = PageBuilder(tag)
    strip_h = render_page_bg(pb, kind)

    if kind == "Email":
        # kicker + date row
        draw(pb.path, pb.path, "E M A I L   ·   ઈમેલ", F_SANS_B, 24, GOLD_D, pb.y, anchor="west", x=MX)
        draw(pb.path, pb.path, "૮ નવેમ્બર ૨૦૨૬  ·  8 November 2026", F_SANS, 22, GRAY, pb.y + 2, anchor="east", x=MX)
        pb.y += 46
        pb.para(data["subject"], F_SERIF_XB, 33, MAROON, gap_after=10, line_h=50)
        pb.rule(GOLD_R, 5, gap_after=18)
        # hero card (the email's Diwali card)
        card = os.path.join(CARDS, CARD_FOR[lang])
        hero_w = 1310
        hero_h = int(hero_w * 1536 / 2816)
        pb.ensure(hero_h + 20)
        pb.paste(card, (PAGE_W - hero_w) // 2, pb.y, w=hero_w)
        pb.y += hero_h + 34
    else:
        draw(pb.path, pb.path, data["date"], F_SANS, 24, GRAY, pb.y, anchor="east", x=MX)
        pb.y += 54
        draw(pb.path, pb.path, data["salutation"], F_SERIF_XB, 31, MAROON, pb.y, anchor="west", x=MX)
        pb.y += 58

    if kind == "Email":
        draw(pb.path, pb.path, data["salutation"], F_SERIF_XB, 27, INK, pb.y, anchor="west", x=MX)
        pb.y += 52

    bi = lang == "Bilingual"
    for text, style in data["paragraphs"]:
        font, size = body_font_for(text, style)
        if style == "en":
            pb.para(text, font, size, GRAY, gap_after=18, line_h=42)
        else:
            pb.para(text, font, size, INK, gap_after=(4 if bi else 22), line_h=48)

    # closing block
    pb.y += 6
    closing = data["closing"]
    for i, ln in enumerate(closing):
        pb.ensure(46)
        if i == 0:
            draw(pb.path, pb.path, ln, F_SERIF, 29, INK, pb.y, anchor="west", x=MX)
        elif i == 1:
            draw(pb.path, pb.path, ln, F_SERIF_XB, 31, MAROON, pb.y, anchor="west", x=MX)
        elif ln.startswith("ELECTRICALSKART"):
            draw(pb.path, pb.path, ln, F_PLAY_B, 26, GOLD_D, pb.y, anchor="west", x=MX)
        else:
            draw(pb.path, pb.path, ln, F_SANS, 24, GRAY, pb.y, anchor="west", x=MX)
        pb.y += 43
    # P.S.
    pb.y += 10
    ps_font = F_SERIF if any('\u0a80' <= ch <= '\u0aff' for ch in data["ps"]) else F_PLAY_IT
    pb.para(data["ps"], ps_font, 24, GRAY, gap_after=0, line_h=40)

    # decorate all pages with diya strip + footer
    for p in pb.pages:
        strip = os.path.join(ASSETS, "letterhead-diya.jpg")
        im(p, "(", strip, "-resize", f"{PAGE_W}x", ")", "-geometry", f"+0+{PAGE_H-STRIP_H}", "-composite", p)
    # footer line on each page
    for p in pb.pages:
        draw(p, p,
             "ELECTRICALSKART.COM  ·  www.ElectricalSkart.com  ·  શુભ દિવાળી ૨૦૨૬  ·  Happy Diwali 2026",
             F_SERIF_XB, 20, GOLD_D, PAGE_H - STRIP_H - 32, anchor="center")
    return pb.pages

def png_pages_to_pdf(pages, out_pdf):
    from reportlab.pdfgen import canvas as rl_canvas
    from reportlab.lib.pagesizes import A4
    c = rl_canvas.Canvas(out_pdf, pagesize=A4)
    w, h = A4
    for p in pages:
        c.drawImage(p, 0, 0, width=w, height=h)
        c.showPage()
    c.save()
    print("saved", out_pdf)

# ---------------- DOCX ----------------
def build_docx(kind, lang, data, out_path):
    import docx
    from docx import Document
    from docx.shared import Pt, Cm, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
    from docx.enum.table import WD_TABLE_ALIGNMENT
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement

    MAROON_RGB = RGBColor(0x4A, 0x10, 0x30)
    GOLDD_RGB  = RGBColor(0xA4, 0x76, 0x1C)
    INK_RGB    = RGBColor(0x2C, 0x27, 0x21)
    GRAY_RGB   = RGBColor(0x55, 0x50, 0x4A)

    def set_run(run, size, bold=False, color=INK_RGB, italic=False, latin="Georgia", guj="Nirmala UI", caps=False):
        run.font.size = Pt(size)
        run.font.bold = bold
        run.font.italic = italic
        run.font.color.rgb = color
        run.font.name = latin
        rPr = run._element.get_or_add_rPr()
        rFonts = rPr.find(qn('w:rFonts'))
        if rFonts is None:
            rFonts = OxmlElement('w:rFonts')
            rPr.append(rFonts)
        rFonts.set(qn('w:ascii'), latin); rFonts.set(qn('w:hAnsi'), latin)
        rFonts.set(qn('w:cs'), guj); rFonts.set(qn('w:eastAsia'), guj)

    def add_para(doc, text, size, bold=False, color=INK_RGB, italic=False,
                 align=WD_ALIGN_PARAGRAPH.LEFT, before=0, after=8, line=1.18):
        p = doc.add_paragraph()
        p.alignment = align
        pf = p.paragraph_format
        pf.space_before = Pt(before); pf.space_after = Pt(after); pf.line_spacing = line
        r = p.add_run(text)
        set_run(r, size, bold, color, italic)
        return p

    def bottom_border(p, color="C9A24B", size=18):
        pPr = p._element.get_or_add_pPr()
        borders = OxmlElement('w:pBdr')
        bottom = OxmlElement('w:bottom')
        bottom.set(qn('w:val'), 'single'); bottom.set(qn('w:sz'), str(size))
        bottom.set(qn('w:space'), '6'); bottom.set(qn('w:color'), color)
        borders.append(bottom); pPr.append(borders)

    doc = Document()
    # page setup
    for section in doc.sections:
        section.page_width, section.page_height = Cm(21.0), Cm(29.7)
        section.left_margin, section.right_margin = Cm(1.9), Cm(1.9)
        section.top_margin, section.bottom_margin = Cm(1.4), Cm(1.3)
    style = doc.styles['Normal']
    style.font.name = 'Georgia'; style.font.size = Pt(11); style.font.color.rgb = INK_RGB

    # letterhead
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(10)
    p.add_run().add_picture(os.path.join(ASSETS, "letterhead-top.png"), width=Cm(17.2))

    if kind == "Email":
        # kicker + date
        p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(2)
        set_run(p.add_run("E M A I L   ·   ઈ મે લ"), 10.5, True, GOLDD_RGB)
        p2 = doc.add_paragraph(); p2.paragraph_format.space_after = Pt(6)
        set_run(p2.add_run("૮ નવેમ્બર ૨૦૨૬  ·  8 November 2026"), 9, False, GRAY_RGB)
        p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(4)
        set_run(p.add_run(data["subject"]), 16, True, MAROON_RGB)
        bottom_border(p, "C9A24B", 20)
        # hero card (resized for a lean document)
        hero = os.path.join(TMP, f"hero_{lang}.jpg")
        im(os.path.join(CARDS, CARD_FOR[lang]), "-resize", "1900x", "-quality", "90", hero)
        p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(10); p.paragraph_format.space_after = Pt(12)
        p.add_run().add_picture(hero, width=Cm(16.4))
        add_para(doc, data["salutation"], 11.5, True, INK_RGB, after=8)
    else:
        add_para(doc, data["date"], 9.5, False, GRAY_RGB, align=WD_ALIGN_PARAGRAPH.RIGHT, after=14)
        add_para(doc, data["salutation"], 12.5, True, MAROON_RGB, after=12, line=1.25)

    bi = lang == "Bilingual"
    for text, st in data["paragraphs"]:
        if st == "en":
            add_para(doc, text, 10.5, False, GRAY_RGB, italic=True, after=10, line=1.28)
        elif st == "gu":
            add_para(doc, text, 11, False, INK_RGB, after=3, line=1.3)
        else:
            add_para(doc, text, 11, False, INK_RGB, after=8, line=1.3)

    closing = data["closing"]
    for i, ln in enumerate(closing):
        if i == 0:
            add_para(doc, ln, 11, False, INK_RGB, before=6, after=2, line=1.3)
        elif i == 1:
            add_para(doc, ln, 12, True, MAROON_RGB, after=2, line=1.3)
        elif ln.startswith("ELECTRICALSKART"):
            add_para(doc, ln, 10.5, True, GOLDD_RGB, after=2, line=1.3)
        else:
            add_para(doc, ln, 9.5, False, GRAY_RGB, after=2, line=1.25)
    add_para(doc, data["ps"], 9.5, False, GRAY_RGB, italic=True, before=10, after=0, line=1.3)

    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(14); p.paragraph_format.space_after = Pt(2)
    p.add_run().add_picture(os.path.join(ASSETS, "letterhead-diya.jpg"), width=Cm(17.2))
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(0)
    set_run(p.add_run("ELECTRICALSKART.COM  ·  www.ElectricalSkart.com  ·  શુભ દિવાળી ૨૦૨૬"), 7.5, True, GOLDD_RGB)

    # metadata
    core = doc.core_properties
    core.title = f"ElectricalSkart.com — Diwali 2026 {kind} ({lang})"
    core.author = "ElectricalSkart.com"
    core.subject = "Diwali 2026 Greeting"
    core.company = "ElectricalSkart.com"
    doc.save(out_path)
    print("saved", out_path)

def build_txt(kind, lang, data):
    lines = ["ELECTRICALSKART.COM — www.ElectricalSkart.com",
             "દિવાળી ૨૦૨૬ · Diwali 2026", ""]
    if kind == "Email":
        lines += [f"Subject: {data['subject']}", ""]
    else:
        lines += [data["date"], ""]
    lines += [data["salutation"], ""]
    for text, st in data["paragraphs"]:
        lines += [text, ""]
    lines += data["closing"] + ["", data["ps"], "", "— www.ElectricalSkart.com"]
    out = os.path.join(DOCS, f"ElectricalSkart-Diwali-{kind}-{lang}.txt")
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(lines).strip() + "\n")
    print("saved", out)

def main():
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    pdf_pages = {}
    for kind in ["Letter", "Email"]:
        for lang in ["Gujarati", "English", "Bilingual"]:
            data = CONTENT[kind][lang]
            base = f"ElectricalSkart-Diwali-{kind}-{lang}"
            if which in ("all", "docx"):
                build_docx(kind, lang, data, os.path.join(DOCS, base + ".docx"))
            if which in ("all", "txt"):
                build_txt(kind, lang, data)
            if which in ("all", "pdf"):
                pages = build_pdf_pages(kind, lang, data)
                pdf_pages[(kind, lang)] = pages
                png_pages_to_pdf(pages, os.path.join(DOCS, base + ".pdf"))
    if which in ("all", "pdf"):
        # combined PDF: letters then emails
        from reportlab.pdfgen import canvas as rl_canvas
        from reportlab.lib.pagesizes import A4
        out = os.path.join(DOCS, "ElectricalSkart-Diwali-2026-Letters-and-Emails-All.pdf")
        c = rl_canvas.Canvas(out, pagesize=A4)
        w, h = A4
        for kind in ["Letter", "Email"]:
            for lang in ["Gujarati", "English", "Bilingual"]:
                for p in pdf_pages[(kind, lang)]:
                    c.drawImage(p, 0, 0, width=w, height=h)
                    c.showPage()
        c.save()
        print("saved", out)

if __name__ == "__main__":
    main()
