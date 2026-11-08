# દિવાળી ૨૦૨૬ · Diwali 2026 — ElectricalSkart.com 🪔

**ElectricalSkart.com તરફથી દિવાળીના ગ્રીટીંગ કાર્ડ, ઈમેલ અને લેટર — ગુજરાતી, અંગ્રેજી અને બાયલિંગ્વલ (ગુજરાતી + અંગ્રેજી).**
Diwali greeting assets for [ElectricalSkart.com](https://www.ElectricalSkart.com) — cards, e-mail and letter — in **Gujarati**, **English** and **Bilingual**.

તારીખ: **૮ નવેમ્બર ૨૦૨૬ · 8 November 2026** (લક્ષ્મી પૂજા / Lakshmi Puja, Diwali 2026)

---

## 📁 શું મળશે / What's inside

```
├── cards/                              ગ્રીટીંગ કાર્ડ (share-ready, ~2816×1536 & 2000×2000)
│   ├── ElectricalSkart-Diwali-Card-GU.jpg         શુભ દિવાળી (square, social/WhatsApp)
│   ├── ElectricalSkart-Diwali-Card-GU-Banner.jpg  શુભ દિવાળી (wide banner)
│   ├── ElectricalSkart-Diwali-Card-EN.jpg         Happy Diwali (square)
│   ├── ElectricalSkart-Diwali-Card-EN-Banner.jpg  Happy Diwali (banner)
│   ├── ElectricalSkart-Diwali-Card-BI.jpg         શુભ દિવાળી · Happy Diwali (square)
│   └── ElectricalSkart-Diwali-Card-BI-Banner.jpg  શુભ દિવાળી · Happy Diwali (banner)
│
├── documents/                          લેટર અને ઈમેલ — Letter & E-mail
│   ├── ElectricalSkart-Diwali-Letter-{Gujarati,English,Bilingual}.docx / .pdf / .txt
│   ├── ElectricalSkart-Diwali-Email-{Gujarati,English,Bilingual}.docx / .pdf / .txt
│   └── ElectricalSkart-Diwali-2026-Letters-and-Emails-All.pdf   (બધું એક જ PDF)
│
├── ecard/                              🇮🇳 ઇન્ટરેક્ટિવ e-card (HTML) — language toggle,
│   └── index.html                      દિવો પ્રગટાવો, fireworks, marigold petals
│
├── assets/                             artwork, letterhead, fonts (static instances + OFL)
├── tools/                              build scripts (python3 + ImageMagick)
└── README.md
```

## 🃏 ગ્રીટીંગ કાર્ડ / The Cards

AI-રચિત દીવા-ચાંદની આર્ટવર્ક + ImageMagick ટેક્સ્ટ લેયર્સ — ગુજરાતી ટાઈપોગ્રાફી Noto Serif/Sans Gujaratiમાં, ઈંગ્લિશ Playfair Displayમાં.
- **Square (2000×2000)** — WhatsApp, Instagram post
- **Banner (2816×1536)** — Facebook/Twitter header, e-mail hero

## ✉️ ઈમેલ અને લેટર / E-mail & Letter

- **.docx** — સંપાદનયોગ્ય, બ્રાન્ડેડ લેટરહેડ (ElectricalSkart બોલ્ટ લોગો, દીવા ફૂટર) સાથે — Word/Google Docs/LibreOffice માં ખૂલે છે
- **.pdf** — છાપવા માટે તૈયાર, A4
- **.txt** — ઇમેઇલમાં સીધા કોપી-પેસ્ટ કરવા માટે
- ઈમેલ ડોક્યુમેન્ટમાં સંબંધિત ભાષાનું **કાર્ડ (banner)** હீரો ઇમેજ તરીકે જોડાયેલું છે
- PDF પેજ ઇમેજ તરીકે રેન્ડર થયેલ છે, તેને Word માં એડિટ કરી શકાય નહીં → સંપાદન માટે .docx વાપરો

## 🌐 E-card લાઇવ ઍક્સેસ / Viewing the e-card

```bash
python3 -m http.server 8080
# ખોલો / open:  http://localhost:8080/ecard/
```

E-card માં ગુજરાતી / English / બંને ટોગલ, ફટાકડા (ફાયરવર્ક કેનવાસ — ક્લિક કરો), 5 દીવા પ્રગટાવવાની ઇન્ટરેક્શન, મરીગોલ્ડ પાંદડીઓ; `prefers-reduced-motion` સન્માને છે.

## 🔨 ફરી બનાવવા માટે / Rebuild from source

જરૂરી: `python3`, `ImageMagick 6` (pango/fontconfig ડેલિગેટ્સ સાથે), ગુજરાતી ફોન્ટ્સ `assets/fonts-static/`માં પહેલેથી છે.

```bash
python3 tools/make_letterhead.py     # letterhead assets
python3 tools/build_cards.py         # cards/*.jpg
python3 tools/build_documents.py     # documents/*.{docx,pdf,txt} + combined PDF
```

ફોન્ટ લાયસન્સ: Noto Sans/Serif Gujarati, Playfair Display — SIL Open Font License (`assets/fonts-static/*-OFL.txt`).

---
*ELECTRICALSKART.COM — તમારા ઘર માટે ઈલેક્ટ્રિકલ સોલ્યુશન · Electrical solutions for a brighter home*
