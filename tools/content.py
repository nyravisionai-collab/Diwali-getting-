# -*- coding: utf-8 -*-
"""All greeting text content for ElectricalSkart Diwali 2026 (GU / EN / BI)."""

DATE_GU = "તારીખ: ૮ નવેમ્બર ૨૦૨૬ · દિવાળી (લક્ષ્મી પૂજા)"
DATE_EN = "Date: 8 November 2026 · Diwali (Lakshmi Puja)"
DATE_BI = "તારીખ / Date : ૮ નવેમ્બર ૨૦૨૬ · 8 November 2026 · દિવાળી / Diwali (લક્ષ્મી પૂજા / Lakshmi Puja)"

EN_LETTER = dict(
    date=DATE_EN,
    salutation="Dear Valued Customer,",
    paragraphs=[
        ("As a million diyas flicker to life across the country tonight, we at ElectricalSkart.com wish you and your family a very Happy Diwali — may your celebrations sparkle with joy, prosperity and togetherness.", "body"),
        ("Diwali is the festival of lights, and lights are what we know best. Whether you are shopping for a glittering new chandelier for the living room, festive fairy lights for your balcony, an energy-efficient fan, smart switches, or ISI-marked wiring for a safer home — we are just a click away at www.ElectricalSkart.com.", "body"),
        ("Thank you for trusting us with the light in your home. Your support powers everything we do, and we promise to keep delivering genuine products, honest prices and warm, friendly service — today, tomorrow and every day of the year.", "body"),
        ("May Goddess Lakshmi bless your home with prosperity, may Lord Ganesha remove every obstacle from your path, and may your life shine brighter than ever — this Diwali, and always.", "body"),
    ],
    closing=["Warm regards & sparklers,", "Team ElectricalSkart", "ELECTRICALSKART.COM", "www.ElectricalSkart.com"],
    ps="P.S. While you light the diyas, do take a moment to check your home's wiring and MCBs — safety is the spark behind every happy Diwali.",
)

GU_LETTER = dict(
    date=DATE_GU,
    salutation="પ્રિય મૂલ્યવાન ગ્રાહક,",
    paragraphs=[
        ("દેશભરમાં લાખો દીપો પ્રગટી રહ્યા છે ત્યારે ElectricalSkart.com તરફથી અમે તમને અને તમારા સમગ્ર પરિવારને દિવાળીના પાવન તહેવારની હાર્દિક શુભેચ્છા પાઠવીએ છીએ — તમારો આ તહેવાર પ્રકાશ, ખુશી અને સમૃદ્ધિથી ભરપૂર રહે.", "body"),
        ("દિવાળી એ પ્રકાશનો તહેવાર છે — અને પ્રકાશ અમારું ક્ષેત્ર છે. લિવિંગ રૂમ માટે નવો ચમકદાર ચાણંદેલિયર મંગાવવો હોય, છજ્જા માટે તહેવારની ફેરી લાઇટ્સ લગાવવી હોય, ઉર્જા-કાર્યક્ષમ પંખો કે સ્માર્ટ સ્વિચ અપગ્રેડ કરવાં હોય, કે સુરક્ષિત ઘર માટે ISI માર્કવાળા વાયર જોતાં હોય — બધું જ તમને એક ક્લિક દૂર છે: www.ElectricalSkart.com", "body"),
        ("તમારા ઘરના પ્રકાશની જવાબદારી અમને સોંપવા બદલ આભાર. તમારા વિશ્વાસને અનુરૂપ અમે હંમેશા સાચા ઉત્પાદનો, વાજબી ભાવો અને હળવા સ્મિત સાથેની સેવા આપવા પ્રતિબદ્ધ છીએ.", "body"),
        ("મા લક્ષ્મી તમારા ઘરને ધન-ધાન્યથી ભરપૂર રાખે, શ્રી ગણપતિ તમારા માર્ગના દરેક વિઘ્નને દૂર કરે, એવી અંતરતમ શુભેચ્છાઓ સાથે — શુભ દિવાળી!", "body"),
    ],
    closing=["દીપો અને પ્રેમ સાથે,", "ટીમ ElectricalSkart", "ELECTRICALSKART.COM", "www.ElectricalSkart.com"],
    ps="P.S. દિવાળીની વ્યસ્તતામાં ઘરની વાયરિંગ અને MCB એક વાર તપાસાવી લો — સલામતી જ દિવાળીનો સૌથી મોટો પુરુષાર્થ છે.",
)

BI_LETTER = dict(
    date=DATE_BI,
    salutation="પ્રિય મૂલ્યવાન ગ્રાહક / Dear Valued Customer,",
    paragraphs=[
        ("દેશભરમાં લાખો દીપો પ્રગટી રહ્યા છે ત્યારે અમે તમને દિવાળીની હાર્દિક શુભેચ્છા પાઠવીએ છીએ.", "gu"),
        ("As a million diyas flicker to life across the country, we wish you a very Happy Diwali.", "en"),
        ("દિવાળી પ્રકાશનો તહેવાર છે — અને પ્રકાશ અમારું ક્ષેત્ર છે. ચાણંદેલિયર, ફેરી લાઇટ્સ, સ્માર્ટ સ્વિચ કે ISI માર્કવાળા વાયર — બધું જ એક ક્લિક દૂર છે: www.ElectricalSkart.com", "gu"),
        ("Diwali is the festival of lights — and light is what we know best. From chandeliers and fairy lights to smart switches and ISI-marked wiring, everything is just a click away: www.ElectricalSkart.com", "en"),
        ("તમારા વિશ્વાસને અનુરૂપ સાચા ઉત્પાદનો, વાજબી ભાવો અને સ્મિત સાથેની સેવા આપવા અમે પ્રતિબદ્ધ છીએ. આભાર.", "gu"),
        ("We are committed to genuine products, honest prices and warm service, always. Thank you for trusting us.", "en"),
        ("મા લક્ષ્મી તમારા ઘરમાં સમૃદ્ધિ લાવે, શ્રી ગણપતિ તમારા માર્ગના વિઘ્નો દૂર કરે — શુભ દિવાળી!", "gu"),
        ("May Goddess Lakshmi bless your home with prosperity and may Lord Ganesha remove every obstacle from your path — Happy Diwali!", "en"),
    ],
    closing=["દીપો અને પ્રેમ સાથે / Warm regards & sparklers,", "ટીમ ElectricalSkart / Team ElectricalSkart", "ELECTRICALSKART.COM", "www.ElectricalSkart.com"],
    ps="P.S. ઘરની વાયરિંગ અને MCB તપાસ્યા વિના દીપો પ્રગટાવશો નહીં — સલામતી પ્રથમ. / Check your wiring and MCBs before the lights go up — safety first, always.",
)

EN_EMAIL = dict(
    subject="શુભ દિવાળી | Happy Diwali from ElectricalSkart.com",
    salutation="Dear Valued Customer,",
    paragraphs=[
        ("Wishing you and your family a very Happy Diwali! May every diya you light tonight bring health, wealth and happiness into your home.", "body"),
        ("This festive season, explore our Diwali collection — sparkling decorative lights, elegant chandeliers, smart home essentials, ISI-marked wiring and everything electrical, delivered right to your door.", "body"),
        ("Browse the festival range at www.ElectricalSkart.com and enjoy safe, genuine products with honest prices and warm service — just as always.", "body"),
        ("Warm wishes from all of us at ElectricalSkart.com — enjoy the festival, light it up bright and stay safe!", "body"),
    ],
    closing=["With festive love,", "Team ElectricalSkart", "ELECTRICALSKART.COM · www.ElectricalSkart.com"],
    ps="P.S. Your Diwali card is right above — share the sparkle with your family!",
)

GU_EMAIL = dict(
    subject="શુભ દિવાળી | ElectricalSkart.com તરફથી દિવાળીની હાર્દિક શુભેચ્છાઓ",
    salutation="પ્રિય મૂલ્યવાન ગ્રાહક,",
    paragraphs=[
        ("તમને અને તમારા પરિવારને દિવાળીના પાવન તહેવારની હાર્દિક શુભકામનાઓ! આજે પ્રગટાવશો તે દરેક દીવો તમારા ઘરમાં આરોગ્ય, સમૃદ્ધિ અને ખુશી લાવે.", "body"),
        ("આ તહેવારોની ઋતુમાં અમારો દિવાળી સંગ્રહ જુઓ — ચમકતી ડિકોરેટિવ લાઇટ્સ, આકર્ષક ચાણંદેલિયર, સ્માર્ટ હોમ ગિયર, ISI માર્કવાળા વાયર અને તમામ ઈલેક્ટ્રિકલ વસ્તુઓ, સીધી તમારા ઘર સુધી.", "body"),
        ("www.ElectricalSkart.com પર સંપૂર્ણ તહેવાર રેન્જ જુઓ અને હંમેશાની જેમ પ્રમાણિક ભાવો, અધિકૃત ઉત્પાદનો અને હળવી સેવાનો લાભ લો.", "body"),
        ("ElectricalSkart.com ના સમગ્ર પરિવાર તરફથી તહેવારની હાર્દિક શુભેચ્છાઓ — તહેવાર માણો, સલામત રહો અને ઝળહળતા રહો!", "body"),
    ],
    closing=["તહેવારના પ્રેમ સાથે,", "ટીમ ElectricalSkart", "ELECTRICALSKART.COM · www.ElectricalSkart.com"],
    ps="P.S. તમારું દિવાળી કાર્ડ ઉપર જ છે — આ ઝગમગ તહેવાર પરિવાર સાથે શેર કરો!",
)

BI_EMAIL = dict(
    subject="શુભ દિવાળી | Happy Diwali from ElectricalSkart.com",
    salutation="પ્રિય મૂલ્યવાન ગ્રાહક / Dear Valued Customer,",
    paragraphs=[
        ("તમને અને તમારા પરિવારને દિવાળીની હાર્દિક શુભકામનાઓ!", "gu"),
        ("Wishing you and your family a very Happy Diwali! May every diya bring health, wealth and happiness into your home.", "en"),
        ("આ તહેવારોમાં અમારો દિવાળી સંગ્રહ જુઓ — ચમકતી લાઇટ્સ, ચાણંદેલિયર, સ્માર્ટ ગિયર અને ISI માર્કવાળી વાયરિંગ — બધું જ તમારા ઘર સુધી.", "gu"),
        ("Explore our Diwali collection — sparkling lights, chandeliers, smart gear and ISI-marked wiring, delivered to your door.", "en"),
        ("www.ElectricalSkart.com પર સંપૂર્ણ રેન્જ જુઓ — પ્રમાણિક ભાવો, અધિકૃત ઉત્પાદનો, હળવી સેવા.", "gu"),
        ("See the full range at www.ElectricalSkart.com — honest prices, genuine products, warm service.", "en"),
        ("તહેવાર માણો, સલામત રહો અને ઝળહળતા રહો!", "gu"),
        ("Enjoy the festival, stay safe and keep shining!", "en"),
    ],
    closing=["તહેવારના પ્રેમ સાથે / With festive love,", "ટીમ ElectricalSkart / Team ElectricalSkart", "ELECTRICALSKART.COM · www.ElectricalSkart.com"],
    ps="P.S. તમારું કાર્ડ ઉપર છે — શેર કરો! / Your Diwali card is right above — share the sparkle!",
)

CONTENT = {
    "Letter": {"Gujarati": GU_LETTER, "English": EN_LETTER, "Bilingual": BI_LETTER},
    "Email":  {"Gujarati": GU_EMAIL,  "English": EN_EMAIL,  "Bilingual": BI_EMAIL},
}

CARD_FOR = {"Gujarati": "ElectricalSkart-Diwali-Card-GU-Banner.jpg",
            "English": "ElectricalSkart-Diwali-Card-EN-Banner.jpg",
            "Bilingual": "ElectricalSkart-Diwali-Card-BI-Banner.jpg"}
