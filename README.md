# દિવાળી ૨૦૨૬ · Diwali 2026 — ElectricalSkart.com 🪔

**ElectricalSkart.com તરફથી દિવાળીના ગ્રીટીંગ કાર્ડ, ઈમેલ અને લેટર — ગુજરાતી, અંગ્રેજી અને બાયલિંગ્વલ (ગુજરાતી + અંગ્રેજી).**
Diwali greeting assets for [ElectricalSkart.com](https://www.ElectricalSkart.com) — cards, e-mail and letter — in **Gujarati**, **English** and **Bilingual**.

તારીખ: **૮ નવેમ્બર ૨૦૬ · 8 November 2026** (લક્ષ્મી પૂજા / Lakshmi Puja, Diwali 2026)

---

## 📁 શું મળશે / What's inside

```
├── cards/                              ગ્રીટીંગ કાર્ડ (share-ready, ~2816×1536 & 2000×2000)
│   ├── ElectricalSkart-Diwali-Card-GU.jpg         શુભ દિવાળી (square, social/WhatsApp)
│   ├── ElectricalSkart-Diwali-Card-GU-Banner.jpg  શુભ દિવાળી (wide banner)
│   ├── ElectricalSkart-Diwali-Card-EN.jpg         Happy Diwali (square)
│   ├── ElectricalSkart-Diwali-Card-EN-Banner.jpg  Happy Diwali (banner)
│   ├── ElectricalSkart-Diwali-Card-BI.jpg         શુભ દિવાળી · Happy Diwali (square)
│   ├── ElectricalSkart-Diwali-Card-BI-Banner.jpg  શુભ દિવાળી · Happy Diwali (banner)
│   ├── …-ForName.jpg / …-Banner-ForName.jpg       🖋️ નામ લખવાની ખાલી લાઇનવાળાં કાર્ડ
│   └── personal/                                  નામ છપેલાં કાર્ડ (--name થી બને)
│
├── documents/                          લેટર અને ઈમેલ — Letter & E-mail
│   ├── ElectricalSkart-Diwali-Letter-{Gujarati,English,Bilingual}.docx / .pdf / .txt
│   ├── ElectricalSkart-Diwali-Email-{Gujarati,English,Bilingual}.docx / .pdf / .txt
│   ├── ElectricalSkart-Diwali-2026-Letters-and-Emails-All.pdf   (બધું એક જ PDF)
│   ├── ElectricalSkart-Diwali-Greeting-Master.{docx,pdf,md,txt}  છ વર્ઝન એક ફાઈલમાં + નામની જગ્યા
│   ├── ElectricalSkart-Diwali-Language-Audit.{docx,pdf,md}       ભાષા-ઑડિટ અહેવાલ
│   └── personal/                                 નામવાળા લેટર/ઈમેલ (--name થી બને)
│
├── ecard/                              🇮 સંવાદાત્મક e-card (HTML) — ભાષા ટોગલ,
│   └── index.html                      «નામ લખો» બોક્સ, દિવો પ્રગટાવો, ફટાકડા, મરીગોલ્ડ પાંદડીઓ
│
├── assets/                             artwork, letterhead, fonts (static instances + OFL)
├── tools/                              build scripts (python3 + ImageMagick)
└── README.md
```

## 🖋️ નામની જગ્યા / The name field

ગ્રીટિંગ ફાઈલોમાં પહેલાં નામ લખવાની કોઈ જગ્યા ન હતી — હવે દરેક જગ્યાએ છે:

- **લેટર / ઈમેલ (.docx, .pdf, .txt):** ટોચ પર સોનેરી ફ્રેમવાળી હાર —
  `ગ્રાહકનું નામ / Customer Name : ………………` — અને સંબોધન પણ ખાલી લાઇન સાથે:
  `પ્રિય ગ્રાહકશ્રી ………………,` / `Dear ………………,` (હાથે લખવા માટે).
- **નામ છાપવું હોય તો:**
  `python3 tools/build_documents.py --name "રમેશ પટેલ"` → `documents/personal/`
  (સંબોધન આપોઆપ `પ્રિય શ્રી રમેશ પટેલ,` / `Dear Ramesh Patel,` થાય).
- **કાર્ડ:** `cards/*-ForName.jpg` પર નામની ખાલી ડોટેડ લાઇન છે;
  `python3 tools/build_cards.py --name "રમેશ પટેલ"` → `cards/personal/` માં નામ છપેલાં કાર્ડ.
- **ઈ-કાર્ડ:** હીરોમાં «નામ લખો / Write a name» બોક્સ — નામ લખતાં શુભેચ્છા, દીવા-સંદેશ અને
  શેર-ટેક્સ્ટ એ નામે બદલાય; લિંકમાં `?to=નામ` મૂકીને મોકલી શકાય.
- **એક જ કમાન્ડથી બધું:** `python3 tools/personalize.py --name "રમેશ પટેલ"`
  (અથવા `--csv names.csv` થી થોકમાં).

## 📄 અલગ આપેલા ડોક્યુમેન્ટ / Standalone documents

- **`documents/ElectricalSkart-Diwali-Greeting-Master.docx`** (તેમજ .pdf/.md/.txt) —
  છ વર્ઝન (લેટર × ૩ ભાષા, ઈમેલ × ૩ ભાષા) એક જ વ્યવસ્થિત ફાઈલમાં, દરેકની ટોચ પર નામ લખવાની જગ્યા.
- **`documents/ElectricalSkart-Diwali-Language-Audit.docx`** (તેમજ .pdf/.md) —
  ભાષા-ઑડિટ: મળેલી દરેક ભૂલ, «જે હતું → જે કર્યું» અને કારણ સહિત.

## 🃏 ગ્રીટિંગ કાર્ડ / The Cards

AI-રચિત દીવા-ચાંદની આર્ટવર્ક + ImageMagick ટેક્સ્ટ લેયર્સ — ગુજરાતી ટાઈપોગ્રાફી Noto Serif/Sans Gujaratiમાં, અંગ્રેજી Playfair Displayમાં.
- **Square (2000×2000)** — WhatsApp, Instagram post
- **Banner (2816×1536)** — Facebook/Twitter header, e-mail hero

## ✉️ ઈમેલ અને લેટર / E-mail & Letter

- **.docx** — સંપાદનયોગ્ય, બ્રાન્ડેડ લેટરહેડ (ElectricalSkart બોલ્ટ લોગો, દીવા ફૂટર) સાથે — Word/Google Docs/LibreOffice માં ખૂલે છે
- **.pdf** — છાપવા માટે તૈયાર, A4
- **.txt** — ઈમેલમાં સીધા કોપી-પેસ્ટ કરવા માટે
- ઈમેલ ડોક્યુમેન્ટમાં સંબંધિત ભાષાનું **કાર્ડ (banner)** હીરો છબી તરીકે જોડાયેલું છે
- PDF પેજ છબી તરીકે રેન્ડર થયેલું છે, તેને Word માં સંપાદિત કરી શકાય નહીં → સંપાદન માટે .docx વાપરો

## 🌐 ઈ-કાર્ડ જોવાની રીત / Viewing the e-card

```bash
python3 -m http.server 8080
# ખોલો / open:  http://localhost:8080/ecard/
```

ઈ-કાર્ડમાં ગુજરાતી / English / બંને ટોગલ, «નામ લખો» બોક્સ, ફટાકડા (ફાયરવર્ક કેનવાસ — ક્લિક કરો), 5 દીવા પ્રગટાવવાની ઇન્ટરેક્શન, મરીગોલ્ડ પાંદડીઓ; `prefers-reduced-motion` સન્માને છે.

## 🔨 ફરી બનાવવા માટે / Rebuild from source

જરૂરી: `python3`, `ImageMagick 6` (pango/fontconfig ડેલિગેટ્સ સાથે), `pip install python-docx reportlab`, ગુજરાતી ફોન્ટ્સ `assets/fonts-static/`માં પહેલેથી છે.

```bash
python3 tools/make_letterhead.py     # letterhead assets
python3 tools/build_cards.py         # cards/*.jpg (+ -ForName variants)
python3 tools/build_documents.py     # documents/*.{docx,pdf,txt} + combined PDF
python3 tools/build_extras.py        # Greeting-Master + Language-Audit documents
python3 tools/personalize.py --name "રમેશ પટેલ"   # optional: named copies
```

ફોન્ટ લાયસન્સ: Noto Sans/Serif Gujarati, Playfair Display — SIL Open Font License (`assets/fonts-static/*-OFL.txt`).

---
*ELECTRICALSKART.COM — તમારા ઘર માટે ઈલેક્ટ્રિકલ સોલ્યુશન · Electrical solutions for a brighter home*
