# -*- coding: utf-8 -*-
"""All greeting text content for ElectricalSkart Diwali 2026 (GU / EN / BI).

--------------------------------------------------------------------------
નામની જગ્યા / THE NAME FIELD
--------------------------------------------------------------------------
Every greeting keeps *two* salutation forms:

    sal_blank   – printed with a dotted leader so the name can be written
                  by hand ("પ્રિય ગ્રાહકશ્રી ..............,")
    sal_named   – used when a name is supplied on the command line
                  (python3 tools/build_documents.py --name "રમેશ પટેલ")

`resolve_salutation()` picks the right one. The build scripts also print a
labelled name box ("ગ્રાહકનું નામ / Customer Name") at the top of every
letter and e-mail, so there is always a clear place to write a name.

--------------------------------------------------------------------------
ભાષા / LANGUAGE NOTE (audit of 8 Nov 2026)
--------------------------------------------------------------------------
The text below is the language-corrected version. The full list of
corrections — with the earlier wording and the reason for each change —
is in `tools/audit_content.py` and renders to
`documents/ElectricalSkart-Diwali-Language-Audit.{md,docx,pdf}`.
"""

DATE_GU = "તારીખ: ૮ નવેમ્બર ૨૦૨૬ · દિવાળી (લક્ષ્મી પૂજા)"
DATE_EN = "Date: 8 November 2026 · Diwali (Lakshmi Puja)"
DATE_BI = "તારીખ / Date : ૮ નવેમ્બર ૨૦૨૬ · 8 November 2026 · દિવાળી / Diwali (લક્ષ્મી પૂજા / Lakshmi Puja)"

# ---------------------------------------------------------------- name field
NAME_TOKEN = "{name}"
BLANK_PRINT = " " + "." * 30          # dotted leader for DOCX / PDF (write by hand)
BLANK_TXT = " " + "_" * 26            # plain blank for copy-paste .txt
BLANK_HTML = ""                       # the e-card uses a real input box

NAME_FIELD_LABEL = {
    "Gujarati": "ગ્રાહકનું નામ",
    "English": "Customer Name",
    "Bilingual": "ગ્રાહકનું નામ / Customer Name",
}
NAME_FIELD_HINT = {
    "Gujarati": "(અહીં નામ લખો)",
    "English": "(write the name here)",
    "Bilingual": "(અહીં નામ લખો / write the name here)",
}
NAME_EXAMPLE = {"Gujarati": "રમેશ પટેલ", "English": "Ramesh Patel",
                "Bilingual": "રમેશ પટેલ / Ramesh Patel"}

SAL_BLANK = {
    "Gujarati": "પ્રિય ગ્રાહકશ્રી" + NAME_TOKEN + ",",
    "English": "Dear" + NAME_TOKEN + ",",
    "Bilingual": "પ્રિય ગ્રાહકશ્રી" + NAME_TOKEN + " / Dear" + NAME_TOKEN + ",",
}
SAL_NAMED = {
    "Gujarati": "પ્રિય શ્રી" + NAME_TOKEN + ",",
    "English": "Dear" + NAME_TOKEN + ",",
    "Bilingual": "પ્રિય શ્રી" + NAME_TOKEN + " / Dear" + NAME_TOKEN + ",",
}


def resolve_salutation(lang, name=None, blank=BLANK_PRINT):
    """Salutation with a real name, or with a dotted space to write one in."""
    name = (name or "").strip()
    template = SAL_NAMED[lang] if name else SAL_BLANK[lang]
    return template.replace(NAME_TOKEN, " " + name if name else blank)


def name_field(lang, name=None, blank=BLANK_PRINT):
    """The labelled 'write the name here' line used by all documents."""
    label = NAME_FIELD_LABEL[lang]
    value = (name or "").strip() or blank
    return f"{label} : {value}"


EN_LETTER = dict(
    date=DATE_EN,
    salutation="Dear Customer,",           # generic fallback (kept for compatibility)
    paragraphs=[
        ("As a million diyas flicker to life across the country tonight, we at ElectricalSkart.com wish you and your family a very Happy Diwali — may your celebrations sparkle with joy, prosperity and togetherness.", "body"),
        ("Diwali is the festival of lights, and lights are what we know best. Whether you are shopping for a glittering new chandelier for the living room, festive fairy lights for your balcony, an energy-efficient fan, smart switches, or ISI-marked wiring for a safer home — everything is just a click away at www.ElectricalSkart.com.", "body"),
        ("Thank you for trusting us with the light in your home. Your support powers everything we do, and we promise to keep delivering genuine products, honest prices and warm, friendly service — today, tomorrow and every day of the year.", "body"),
        ("May Goddess Lakshmi bless your home with prosperity, may Lord Ganesha remove every obstacle from your path, and may your life shine brighter than ever — this Diwali, and always.", "body"),
    ],
    closing=["Warm regards,", "Team ElectricalSkart", "ELECTRICALSKART.COM", "www.ElectricalSkart.com"],
    ps="P.S. While you light the diyas, do take a moment to check your home's wiring and MCBs — safety is the spark behind every happy Diwali.",
)

GU_LETTER = dict(
    date=DATE_GU,
    salutation="પ્રિય ગ્રાહક મિત્ર,",
    paragraphs=[
        ("આજે દિવાળીની સાંજે દેશભરમાં લાખો દીવા પ્રગટી રહ્યા છે, ત્યારે ElectricalSkart.com પરિવાર તરફથી તમને અને તમારા સમગ્ર પરિવારને દિવાળીના પાવન તહેવારની હાર્દિક શુભેચ્છાઓ — તમારો આ તહેવાર પ્રકાશ, આનંદ અને સમૃદ્ધિથી ભરપૂર રહે.", "body"),
        ("દિવાળી એ પ્રકાશનો તહેવાર છે — અને પ્રકાશ અમારું ક્ષેત્ર છે. લિવિંગ રૂમ માટે ચમકદાર ઝુમ્મર, બાલ્કની માટે તહેવારની ઝાલર (ફેરી લાઈટો), ઊર્જા-કાર્યક્ષમ પંખો કે સ્માર્ટ સ્વિચ, અથવા સુરક્ષિત ઘર માટે ISI માર્કવાળા વાયર — ગમે તે જોઈતું હોય, બધું જ માત્ર એક ક્લિકના અંતરે છે: www.ElectricalSkart.com", "body"),
        ("તમારા ઘરના પ્રકાશની જવાબદારી અમને સોંપવા બદલ આભાર. તમારા વિશ્વાસને અનુરૂપ અમે હંમેશા અસલી ઉત્પાદનો, વાજબી ભાવ અને હસમુખ સેવા આપવા પ્રતિબદ્ધ છીએ.", "body"),
        ("મા લક્ષ્મી તમારા ઘરને ધન-ધાન્યથી ભરપૂર રાખે અને શ્રી ગણેશજી તમારા માર્ગના દરેક વિઘ્નને દૂર કરે — એવી અંતરતમ શુભેચ્છાઓ સાથે, શુભ દિવાળી!", "body"),
    ],
    closing=["હાર્દિક શુભેચ્છાઓ અને પ્રેમ સાથે,", "ટીમ ElectricalSkart", "ELECTRICALSKART.COM", "www.ElectricalSkart.com"],
    ps="P.S. દિવાળીની વ્યસ્તતામાં ઘરની વાયરિંગ અને MCB એક વાર તપાસાવી લો — સલામતી એ જ દિવાળીની સૌથી મોટી ભેટ છે.",
)

BI_LETTER = dict(
    date=DATE_BI,
    salutation="પ્રિય ગ્રાહક મિત્ર / Dear Customer,",
    paragraphs=[
        ("આજે દેશભરમાં લાખો દીવા પ્રગટી રહ્યા છે, ત્યારે અમે તમને દિવાળીની હાર્દિક શુભેચ્છાઓ પાઠવીએ છીએ.", "gu"),
        ("As a million diyas flicker to life across the country tonight, we wish you a very Happy Diwali.", "en"),
        ("દિવાળી પ્રકાશનો તહેવાર છે — અને પ્રકાશ અમારું ક્ષેત્ર છે. ઝુમ્મર, ઝાલર (ફેરી લાઈટો), સ્માર્ટ સ્વિચ કે ISI માર્કવાળા વાયર — બધું જ માત્ર એક ક્લિકના અંતરે છે: www.ElectricalSkart.com", "gu"),
        ("Diwali is the festival of lights — and light is what we know best. From chandeliers and fairy lights to smart switches and ISI-marked wiring, everything is just a click away: www.ElectricalSkart.com", "en"),
        ("તમારા વિશ્વાસને અનુરૂપ અસલી ઉત્પાદનો, વાજબી ભાવ અને હસમુખ સેવા આપવા અમે પ્રતિબદ્ધ છીએ. આભાર.", "gu"),
        ("We are committed to genuine products, honest prices and warm service, always. Thank you for trusting us.", "en"),
        ("મા લક્ષ્મી તમારા ઘરમાં સમૃદ્ધિ લાવે અને શ્રી ગણેશજી તમારા માર્ગના દરેક વિઘ્નને દૂર કરે — શુભ દિવાળી!", "gu"),
        ("May Goddess Lakshmi bless your home with prosperity and may Lord Ganesha remove every obstacle from your path — Happy Diwali!", "en"),
    ],
    closing=["હાર્દિક શુભેચ્છાઓ અને પ્રેમ સાથે / With warm regards,", "ટીમ ElectricalSkart / Team ElectricalSkart", "ELECTRICALSKART.COM", "www.ElectricalSkart.com"],
    ps="P.S. ઘરની વાયરિંગ અને MCB તપાસ્યા વિના દીવા પ્રગટાવશો નહીં — સલામતી પ્રથમ. / Check your wiring and MCBs before the lights go up — safety first, always.",
)

EN_EMAIL = dict(
    subject="Happy Diwali from ElectricalSkart.com",
    salutation="Dear Customer,",
    paragraphs=[
        ("Wishing you and your family a very Happy Diwali! May every diya you light tonight bring health, wealth and happiness into your home.", "body"),
        ("This festive season, explore our Diwali collection — sparkling decorative lights, elegant chandeliers, smart home essentials, ISI-marked wiring and everything electrical, delivered right to your door.", "body"),
        ("Browse the festival range at www.ElectricalSkart.com and enjoy safe, genuine products at honest prices, with warm service — as always.", "body"),
        ("Warm wishes from all of us at ElectricalSkart.com — enjoy the festival, light it up bright and stay safe!", "body"),
    ],
    closing=["With warm festive wishes,", "Team ElectricalSkart", "ELECTRICALSKART.COM · www.ElectricalSkart.com"],
    ps="P.S. Your Diwali card is right above — share the sparkle with your family!",
)

GU_EMAIL = dict(
    subject="શુભ દિવાળી | ElectricalSkart.com તરફથી દિવાળીની હાર્દિક શુભેચ્છાઓ",
    salutation="પ્રિય ગ્રાહક મિત્ર,",
    paragraphs=[
        ("તમને અને તમારા પરિવારને દિવાળીના પાવન તહેવારની હાર્દિક શુભેચ્છાઓ! આજે તમે પ્રગટાવશો તે દરેક દીવો તમારા ઘરમાં આરોગ્ય, સમૃદ્ધિ અને આનંદ લાવે.", "body"),
        ("આ તહેવારની ઋતુમાં અમારો દિવાળી સંગ્રહ જુઓ — ઝગમગતી ડેકોરેટિવ લાઈટો, આકર્ષક ઝુમ્મર, સ્માર્ટ હોમ ઉપકરણો, ISI માર્કવાળા વાયર અને તમામ ઈલેક્ટ્રિકલ સામાન — બધું જ સીધું તમારા ઘર સુધી.", "body"),
        ("www.ElectricalSkart.com પર તહેવારની સંપૂર્ણ રેન્જ જુઓ અને હંમેશાની જેમ વાજબી ભાવ, અસલી ઉત્પાદનો અને હસમુખ સેવાનો લાભ લો.", "body"),
        ("ElectricalSkart.com પરિવાર તરફથી તહેવારની હાર્દિક શુભેચ્છાઓ — તહેવાર માણો, સલામત રહો અને ઝળહળતા રહો!", "body"),
    ],
    closing=["તહેવારની હાર્દિક શુભેચ્છાઓ સાથે,", "ટીમ ElectricalSkart", "ELECTRICALSKART.COM · www.ElectricalSkart.com"],
    ps="P.S. તમારું દિવાળી કાર્ડ ઉપર જ છે — આ ઝગમગાટ પરિવાર સાથે શેર કરો!",
)

BI_EMAIL = dict(
    subject="શુભ દિવાળી | Happy Diwali from ElectricalSkart.com",
    salutation="પ્રિય ગ્રાહક મિત્ર / Dear Customer,",
    paragraphs=[
        ("તમને અને તમારા પરિવારને દિવાળીની હાર્દિક શુભેચ્છાઓ!", "gu"),
        ("Wishing you and your family a very Happy Diwali! May every diya bring health, wealth and happiness into your home.", "en"),
        ("આ તહેવારમાં અમારો દિવાળી સંગ્રહ જુઓ — ઝગમગતી લાઈટો, ઝુમ્મર, સ્માર્ટ ઉપકરણો અને ISI માર્કવાળી વાયરિંગ — બધું જ તમારા ઘર સુધી.", "gu"),
        ("Explore our Diwali collection — sparkling lights, chandeliers, smart home essentials and ISI-marked wiring, delivered to your door.", "en"),
        ("www.ElectricalSkart.com પર સંપૂર્ણ રેન્જ જુઓ — વાજબી ભાવ, અસલી ઉત્પાદનો, હસમુખ સેવા.", "gu"),
        ("See the full range at www.ElectricalSkart.com — honest prices, genuine products, warm service.", "en"),
        ("તહેવાર માણો, સલામત રહો અને ઝળહળતા રહો!", "gu"),
        ("Enjoy the festival, stay safe and keep shining!", "en"),
    ],
    closing=["તહેવારની હાર્દિક શુભેચ્છાઓ સાથે / With warm festive wishes,", "ટીમ ElectricalSkart / Team ElectricalSkart", "ELECTRICALSKART.COM · www.ElectricalSkart.com"],
    ps="P.S. તમારું કાર્ડ ઉપર જ છે — શેર કરો! / Your Diwali card is right above — share the sparkle!",
)

CONTENT = {
    "Letter": {"Gujarati": GU_LETTER, "English": EN_LETTER, "Bilingual": BI_LETTER},
    "Email":  {"Gujarati": GU_EMAIL,  "English": EN_EMAIL,  "Bilingual": BI_EMAIL},
}

CARD_FOR = {"Gujarati": "ElectricalSkart-Diwali-Card-GU-Banner.jpg",
            "English": "ElectricalSkart-Diwali-Card-EN-Banner.jpg",
            "Bilingual": "ElectricalSkart-Diwali-Card-BI-Banner.jpg"}
