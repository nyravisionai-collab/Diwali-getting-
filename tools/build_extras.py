#!/usr/bin/env python3
"""Build the two standalone documents of the Diwali 2026 suite:

  1. documents/ElectricalSkart-Diwali-Language-Audit.{md,docx,pdf}
       – every language error found in `main`, with before → after and why
  2. documents/ElectricalSkart-Diwali-Greeting-Master.{md,txt,docx,pdf}
       – one tidy document holding all six greetings, each with a proper
         space to write the recipient's name

Run:  python3 tools/build_extras.py
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import audit_content as AC
import build_documents as BD
from content import CONTENT, resolve_salutation, name_field, NAME_FIELD_LABEL, NAME_FIELD_HINT, BLANK_PRINT, BLANK_TXT

ROOT = os.path.dirname(HERE)
DOCS = os.path.join(ROOT, "documents")
os.makedirs(DOCS, exist_ok=True)

FOOTER = "ELECTRICALSKART.COM  ·  www.ElectricalSkart.com  ·  શુભ દિવાળી ૨૦૨૬  ·  Happy Diwali 2026"


# ───────────────────────────── markdown ─────────────────────────────
def md_render(blocks):
    out = []
    for b in blocks:
        kind = b[0]
        if kind == "h1":
            out += [f"# {b[1]}", ""]
        elif kind == "h2":
            out += [f"## {b[1]}", ""]
        elif kind == "h3":
            out += [f"### {b[1]}", ""]
        elif kind == "p":
            out += [b[1], ""]
        elif kind == "quote":
            out += [f"> {b[1]}", ""]
        elif kind == "table":
            header, rows = b[1], b[2]
            out += ["| " + " | ".join(header) + " |",
                    "|" + "|".join(["---"] * len(header)) + "|"]
            for r in rows:
                out += ["| " + " | ".join(c.replace("|", "\\|").replace("\n", "<br>") for c in r) + " |"]
            out += [""]
        elif kind == "bullets":
            out += [f"- {x}" for x in b[1]] + [""]
        elif kind == "gap":
            out += [""]
    return "\n".join(out).strip() + "\n"


# ───────────────────────────── docx ─────────────────────────────
def docx_render(path, blocks, title):
    from docx import Document
    from docx.shared import Pt, Cm, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.enum.table import WD_TABLE_ALIGNMENT
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement

    MAROON = RGBColor(0x4A, 0x10, 0x30)
    GOLDD = RGBColor(0xA4, 0x76, 0x1C)
    INK = RGBColor(0x2C, 0x27, 0x21)
    GRAY = RGBColor(0x55, 0x50, 0x4A)

    def set_run(r, size, bold=False, color=INK, italic=False):
        r.font.size = Pt(size)
        r.font.bold = bold
        r.font.italic = italic
        r.font.color.rgb = color
        r.font.name = "Georgia"
        rPr = r._element.get_or_add_rPr()
        rFonts = rPr.find(qn('w:rFonts'))
        if rFonts is None:
            rFonts = OxmlElement('w:rFonts'); rPr.append(rFonts)
        rFonts.set(qn('w:ascii'), 'Georgia'); rFonts.set(qn('w:hAnsi'), 'Georgia')
        rFonts.set(qn('w:cs'), 'Nirmala UI'); rFonts.set(qn('w:eastAsia'), 'Nirmala UI')

    def para(text, size, bold=False, color=INK, italic=False, align=None, before=0, after=8):
        p = doc.add_paragraph()
        if align is not None:
            p.alignment = align
        p.paragraph_format.space_before = Pt(before)
        p.paragraph_format.space_after = Pt(after)
        p.paragraph_format.line_spacing = 1.28
        set_run(p.add_run(text), size, bold, color, italic)
        return p

    doc = Document()
    for s in doc.sections:
        s.page_width, s.page_height = Cm(21.0), Cm(29.7)
        s.left_margin, s.right_margin = Cm(1.9), Cm(1.9)
        s.top_margin, s.bottom_margin = Cm(1.5), Cm(1.4)
    st = doc.styles['Normal']
    st.font.name = 'Georgia'; st.font.size = Pt(10.5); st.font.color.rgb = INK

    for b in blocks:
        kind = b[0]
        if kind == "h1":
            para(b[1], 18, True, MAROON, align=WD_ALIGN_PARAGRAPH.CENTER, after=4)
            p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_after = Pt(14)
            set_run(p.add_run(" ELECTRICALSKART.COM ⚡"), 8.5, True, GOLDD)
        elif kind == "h2":
            para(b[1], 13.5, True, MAROON, before=10, after=6)
        elif kind == "h3":
            para(b[1], 11.5, True, GOLDD, before=8, after=4)
        elif kind == "p":
            para(b[1], 10.5, False, INK)
        elif kind == "quote":
            para(b[1], 10, False, GRAY, italic=True)
        elif kind == "bullets":
            for x in b[1]:
                para("•  " + x, 10.5, False, INK, after=4)
        elif kind == "table":
            header, rows = b[1], b[2]
            t = doc.add_table(rows=1, cols=len(header))
            t.alignment = WD_TABLE_ALIGNMENT.CENTER
            t.style = 'Table Grid'
            for i, h in enumerate(header):
                c = t.rows[0].cells[i]
                c.text = ""
                set_run(c.paragraphs[0].add_run(h), 9.5, True, RGBColor(0xFF, 0xFF, 0xFF))
                shd = OxmlElement('w:shd'); shd.set(qn('w:val'), 'clear')
                shd.set(qn('w:fill'), '4A1030')
                c._tc.get_or_add_tcPr().append(shd)
            for r in rows:
                cells = t.add_row().cells
                for i, val in enumerate(r):
                    cells[i].text = ""
                    set_run(cells[i].paragraphs[0].add_run(val), 9)
            doc.add_paragraph().paragraph_format.space_after = Pt(4)
        elif kind == "gap":
            doc.add_paragraph().paragraph_format.space_after = Pt(2)

    core = doc.core_properties
    core.title = title
    core.author = "ElectricalSkart.com"
    core.subject = "Diwali 2026 Greeting Suite"
    core.company = "ElectricalSkart.com"
    doc.save(path)
    print("saved", path)


# ───────────────────────────── pdf ─────────────────────────────
def pdf_decorate(pb):
    strip = os.path.join(ROOT, "assets", "letterhead-diya.jpg")
    for p in pb.pages:
        BD.im(p, "(", strip, "-resize", f"{BD.PAGE_W}x", ")",
              "-geometry", f"+0+{BD.PAGE_H - BD.STRIP_H}", "-composite", p)
        BD.draw(p, p, FOOTER, BD.F_SERIF_XB, 20, BD.GOLD_D,
                BD.PAGE_H - BD.STRIP_H - 32, anchor="center")


def pdf_heading(pb, text, size, font, color, gap_after=16, align="west"):
    for ln in BD.wrap(text, font, size, BD.TEXT_W):
        pb.ensure(int(size * 1.45))
        BD.draw(pb.path, pb.path, ln, font, size, color, pb.y,
                anchor="center" if align == "center" else "west", x=BD.MX)
        pb.y += int(size * 1.45)
    pb.y += gap_after


def pdf_para(pb, text, style="gu", size=None, color=None, gap_after=12):
    # Playfair (the Latin italic) has no Gujarati glyphs — fall back when needed
    if style == "en" and any("\u0a80" <= ch <= "\u0aff" for ch in text):
        style = "bi"
    font, sz = BD.body_font_for(text, style)
    if size:
        sz = size
    col = color if color else (BD.GRAY if style == "en" else BD.INK)
    pb.para(text, font, sz, col, gap_after=gap_after, line_h=int(sz * 1.5))


def pdf_render(path, blocks):
    pb = BD.PageBuilder("extras")
    BD.render_page_bg(pb, "Letter")
    pb.y += 10
    for b in blocks:
        kind = b[0]
        if kind == "h1":
            pdf_heading(pb, b[1], 40, BD.F_SERIF_XB, BD.MAROON, gap_after=6, align="center")
            pdf_heading(pb, "ELECTRICALSKART.COM  ·  DIWALI 2026", 20, BD.F_PLAY_B,
                        BD.GOLD_D, gap_after=20, align="center")
        elif kind == "h2":
            pdf_heading(pb, b[1], 30, BD.F_SERIF_XB, BD.MAROON, gap_after=10)
        elif kind == "h3":
            pdf_heading(pb, b[1], 25, BD.F_SERIF_SB, BD.GOLD_D, gap_after=8)
        elif kind == "p":
            pdf_para(pb, b[1], style="bi")
        elif kind == "quote":
            pdf_para(pb, b[1], style="en", size=24, color=BD.GRAY)
        elif kind == "bullets":
            for x in b[1]:
                pdf_para(pb, "•  " + x, style="bi", gap_after=8)
        elif kind == "table":
            header, rows = b[1], b[2]
            for r in rows:
                pdf_para(pb, f"{header[0]} {r[0]}", style="bi", size=26, color=BD.MAROON, gap_after=2)
                rest = "  |  ".join(r[1:])
                pdf_para(pb, rest, style="bi", gap_after=10)
        elif kind == "gap":
            pb.y += 10
    pdf_decorate(pb)
    BD.png_pages_to_pdf(pb.pages, path)


# ───────────────────────────── audit document ─────────────────────────────
def audit_blocks():
    n = len(AC.FINDINGS)
    hi = sum(1 for f in AC.FINDINGS if f["sev"].startswith("ઉચ્ચ"))
    me = sum(1 for f in AC.FINDINGS if f["sev"].startswith("મધ્યમ"))
    lo = sum(1 for f in AC.FINDINGS if f["sev"].startswith("નીચું"))
    b = [
        ("h1", "ભાષા-ઑડિટ અહેવાલ · Language Audit Report"),
        ("p", "દિવાળી ૨૦૨૬ ગ્રીટિંગ સમૂહ — કાર્ડ, લેટર, ઈમેલ અને ઈ-કાર્ડ · "
              "Diwali 2026 greeting suite — cards, letters, e-mails and the e-card."),
        ("p", "તપાસ તારીખ / Audited: ૮ નવેમ્બર ૨૦૨૬ · 8 November 2026 · "
              "બ્રાન્ચ / branch: arena/5a8becb6-diwali-getting (આધાર / base: main @ c8ea6bb)"),
        ("p", f"કુલ શોધ / findings: {n}  ·  ઉચ્ચ / high: {hi}  ·  મધ્યમ / medium: {me}  ·  નીચું / low: {lo}. "
              "દરેક શોધ નીચે «જે હતું → જે કર્યું» સ્વરૂપે છે અને બધી સુધારેલી ફાઈલોમાં લાગુ પડી છે."),
        ("h2", "૧. શોધની યાદી · Findings"),
    ]
    for f in AC.FINDINGS:
        b += [
            ("h3", f"#{f['id']} · {f['cat']} · [{f['sev']}]"),
            ("p", f"ફાઈલ / file: {f['where']}"),
            ("p", f"જે હતું / before: {f['before']}"),
            ("p", f"જે કર્યું / after: {f['after']}"),
            ("p", f"{f['gu']}"),
            ("quote", f["en"]),
        ]
    b += [("h2", "૨. નામ લખવાની જગ્યા · The name field")]
    for title, body in AC.NAME_FIELD_NOTES:
        b += [("h3", title), ("p", body)]
    b += [("h2", "૩. આ અહેવાલ ફરી બનાવવો · Regenerating this report"),
          ("p", "python3 tools/build_extras.py   (સ્રોત / source: tools/audit_content.py)"),
          ("p", "ભૂલોનો સ્રોત-ડેટા audit_content.py માં છે, તેથી અહેવાલના .md, .docx અને .pdf "
                "હંમેશા એકસમાન રહે છે.")]
    return b


# ───────────────────────────── master greeting document ─────────────────────────────
def master_blocks(blank):
    b = [
        ("h1", "ગ્રીટિંગ માસ્ટર ડોક્યુમેન્ટ · Greeting Master"),
        ("p", "દિવાળી ૨૦૬ — ElectricalSkart.com · છ વર્ઝન એક જ ફાઈલમાં: "
              "લેટર (ગુજરાતી / અંગ્રેજી / બાયલિંગ્વલ) અને ઈમેલ (ગુજરાતી / અંગ્રેજી / બાયલિંગ્વલ)."),
        ("h2", "નામ કેવી રીતે ભરવું · How to fill in the name"),
        ("bullets", [
            "દરેક ગ્રીટિંગની ટોચ પર «ગ્રાહકનું નામ / Customer Name» ની ખાલી લીટી છે — તેમાં નામ લખો.",
            "સંબોધનની લીટીમાં પણ ખાલી જગ્યા છે: «પ્રિય ગ્રાહકશ્રી …………,» / «Dear …………,».",
            "કમ્પ્યુટર પર ભરવું હોય તો: python3 tools/build_documents.py --name \"રમેશ પટેલ\" "
            "→ નામ આપોઆપ બધે છપાય (documents/personal/).",
            "કાર્ડ માટે: cards/*-ForName.jpg પર નામની ખાલી લાઇન છે; અથવા "
            "python3 tools/build_cards.py --name \"રમેશ પટેલ\".",
            "ઈ-કાર્ડમાં «નામ લખો / Write a name» બોક્સ છે; લિંકમાં ?to=નામ પણ મૂકી શકાય.",
        ]),
    ]
    order = [("Letter", "લેટર · Letter"), ("Email", "ઈમેલ · E-mail")]
    langnames = {"Gujarati": "ગુજરાતી", "English": "અંગ્રેજી", "Bilingual": "બાયલિંગ્વલ"}
    for kind, kind_gu in order:
        for lang in ["Gujarati", "English", "Bilingual"]:
            data = CONTENT[kind][lang]
            b += [("h2", f"{kind_gu} — {langnames[lang]} ({lang})"),
                  ("p", name_field(lang, None, blank)),
                  ("p", resolve_salutation(lang, None, blank))]
            if kind == "Email":
                b += [("p", "Subject: " + data["subject"])]
            else:
                b += [("p", data["date"])]
            for text, style in data["paragraphs"]:
                b += [("p", text)]
            for ln in data["closing"]:
                b += [("p", ln)]
            b += [("quote", data["ps"]), ("gap",)]
    return b


def master_txt(blocks, path):
    lines = []
    for b in blocks:
        kind = b[0]
        if kind == "h1":
            lines += [b[1].upper(), "=" * 60, ""]
        elif kind == "h2":
            lines += ["", b[1], "-" * 50, ""]
        elif kind == "h3":
            lines += ["", b[1], ""]
        elif kind in ("p", "quote"):
            lines += [b[1], ""]
        elif kind == "bullets":
            lines += ["- " + x for x in b[1]] + [""]
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines).strip() + "\n")
    print("saved", path)


def main():
    # ---- audit
    blocks = audit_blocks()
    md = os.path.join(DOCS, "ElectricalSkart-Diwali-Language-Audit.md")
    with open(md, "w", encoding="utf-8") as f:
        f.write(md_render(blocks))
    print("saved", md)
    docx_render(os.path.join(DOCS, "ElectricalSkart-Diwali-Language-Audit.docx"),
                blocks, "ElectricalSkart.com — Diwali 2026 Language Audit")
    pdf_render(os.path.join(DOCS, "ElectricalSkart-Diwali-Language-Audit.pdf"), blocks)

    # ---- master greeting document (write-in blanks)
    blocks = master_blocks(BLANK_PRINT)
    md = os.path.join(DOCS, "ElectricalSkart-Diwali-Greeting-Master.md")
    with open(md, "w", encoding="utf-8") as f:
        f.write(md_render(blocks))
    print("saved", md)
    docx_render(os.path.join(DOCS, "ElectricalSkart-Diwali-Greeting-Master.docx"),
                blocks, "ElectricalSkart.com — Diwali 2026 Greeting Master")
    pdf_render(os.path.join(DOCS, "ElectricalSkart-Diwali-Greeting-Master.pdf"), blocks)
    master_txt(master_blocks(BLANK_TXT),
               os.path.join(DOCS, "ElectricalSkart-Diwali-Greeting-Master.txt"))


if __name__ == "__main__":
    main()
