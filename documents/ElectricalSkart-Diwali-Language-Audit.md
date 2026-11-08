# ભાષા-ઑડિટ અહેવાલ · Language Audit Report

દિવાળી ૨૦૨૬ ગ્રીટિંગ સમૂહ — કાર્ડ, લેટર, ઈમેલ અને ઈ-કાર્ડ · Diwali 2026 greeting suite — cards, letters, e-mails and the e-card.

તપાસ તારીખ / Audited: ૮ નવેમ્બર ૨૦૨૬ · 8 November 2026 · બ્રાન્ચ / branch: arena/5a8becb6-diwali-getting (આધાર / base: main @ c8ea6bb)

કુલ શોધ / findings: 27  ·  ઉચ્ચ / high: 7  ·  મધ્યમ / medium: 12  ·  નીચું / low: 8. દરેક શોધ નીચે «જે હતું → જે કર્યું» સ્વરૂપે છે અને બધી સુધારેલી ફાઈલોમાં લાગુ પડી છે.

## ૧. શોધની યાદી · Findings

### #1 · જોડણી અને શબ્દ પસંદગી · [ઉચ્ચ / high]

ફાઈલ / file: tools/content.py · ecard/index.html

જે હતું / before: ચાણંદેલિયર

જે કર્યું / after: ઝુમ્મર

અંગ્રેજી chandelier નું ખોટું લિપ્યંતરણ. ગુજરાતી શબ્દકોશ (ગુજરાતીલેક્સિકોન) પ્રમાણે છત પર લટકતી બત્તીઓવાળા સુશોભનનો યોગ્ય શબ્દ «ઝુમ્મર» છે.

> A garbled transliteration of 'chandelier'; the dictionary Gujarati word is «ઝુમ્મર».

### #2 · જોડણી (માત્રા) · [ઉચ્ચ / high]

ફાઈલ / file: tools/content.py · ecard/index.html

જે હતું / before: લાઇટ્સ (લ + ા + ઇ + ટ — સ્વતંત્ર અક્ષર ઇ)

જે કર્યું / after: લાઈટો / લાઈટ્સ (માત્રા ી)

શબ્દની વચ્ચે સ્વતંત્ર સ્વર અક્ષર «ઇ» (U+0A87) વપરાયો હતો, માત્રા નહીં. ગુજરાતી લેખનમાં «light» = «લાઈટ» (માત્રા ી, U+0AC0) અને બહુવચન «લાઈટો» લખાય છે.

> An independent vowel letter (ઇ, U+0A87) sat mid-word instead of the vowel sign; correct is લાઈટ / લાઈટો.

### #3 · જોડણી · [ઉચ્ચ / high]

ફાઈલ / file: tools/content.py (ગુજરાતી લેટર)

જે હતું / before: ઉર્જા-કાર્યક્ષમ

જે કર્યું / after: ઊર્જા-કાર્યક્ષમ

સંસ્કૃત/હિંદી મૂળ શબ્દ (ūrjā) = ગુજરાતી «ઊર્જા» (દીર્ઘ ઊ). ટૂંકા «ઉ» થી લખાયું હતું.

> Energy is «ઊર્જા» (long ઊ), not «ઉર્જા».

### #4 · વ્યાકરણ (ક્રિયાપદ) · [ઉચ્ચ / high]

ફાઈલ / file: ecard/index.html (ટીપ ૧)

જે હતું / before: ફેરી લાઇટ્સના લગાડતા પહેલા

જે કર્યું / after: ઝાલર (ફેરી લાઈટો) લગાવતાં પહેલાં

«લગાડવું» એ પ્રમાણભૂત ક્રિયાપદ નથી; યોગ્ય રૂપ «લગાવવું» છે. તેમજ ક્રિયાવિશેષણ «પહેલાં» માં અનુસ્વાર જોઈએ («પહેલા» = પહેલો/પ્રથમ).

> 'લગાડવું' is not a standard verb (correct: લગાવવું); the adverb needs the anusvara: પહેલાં.

### #5 · અર્થ (વાક્ય ખોટો અર્થ આપે છે) · [ઉચ્ચ / high]

ફાઈલ / file: ecard/index.html (ટીપ ૩)

જે હતું / before: ઓર્ડર કરો અને તહેવાર પહેલા ઘર આવો

જે કર્યું / after: ઓર્ડર કરો અને તહેવાર પહેલાં તમારા ઘર સુધી પહોંચાડીએ

મૂળ વાક્યનો અર્થ થતો હતો કે ગ્રાહકે ઘરે આવવું! હેતુ એ હતો કે માલ તહેવાર પહેલાં ઘર સુધી પહોંચે.

> The original read 'come home before the festival'; the intent is delivery to the home.

### #6 · વ્યાકરણ (મેળ) · [ઉચ્ચ / high]

ફાઈલ / file: ecard/index.html (ટીપ ૩)

જે હતું / before: આખું ઇન્ડિયા

જે કર્યું / after: આખા ભારતમાં

«આખું ઇન્ડિયા» માં વિશેષણ-નામનો મેળ બેસતો નથી; સાથે ગુજરાતી લેખમાં «ભારત» વધુ યોગ્ય છે.

> Adjective–noun agreement was wrong, and «ભારત» is preferred over «ઇન્ડિયા» in Gujarati prose.

### #7 · વ્યાકરણ (વિભક્તિ) · [ઉચ્ચ / high]

ફાઈલ / file: tools/content.py (ગુજરાતી ઈમેલ P.S.)

જે હતું / before: આ ઝગમગ તહેવાર પરિવાર સાથે શેર કરો!

જે કર્યું / after: આ ઝગમગાટ પરિવાર સાથે શેર કરો!

«ઝગમગ» ક્રિયાપદનું મૂળ છે, નામ નહીં; નામ «ઝગમગાટ» છે. વધુમાં કર્મપદ માટે «ને» વિભક્તિ જોઈએ.

> 'ઝગમગ' is a verb stem, not a noun; the noun is «ઝગમગાટ».

### #8 · વ્યાકરણ (લિંગ-મેળ) · [મધ્યમ / medium]

ફાઈલ / file: ecard/index.html (ટીપ ૧)

જે હતું / before: ISI માર્કવાળી પ્રોડક્ટ જ પસંદ કરો

જે કર્યું / after: ISI માર્કવાળાં ઉત્પાદનો જ પસંદ કરો

«ઉત્પાદન» નપુંસકલિંગ છે, તેથી બહુવચનમાં «માર્કવાળાં ઉત્પાદનો». «પ્રોડક્ટ» ને બદલે ગુજરાતી «ઉત્પાદન» વાપર્યું.

> ઉત્પાદન is neuter, so the adjective takes -આં; the English loan 'પ્રોડક્ટ' was replaced.

### #9 · શબ્દ પસંદગી · [મધ્યમ / medium]

ફાઈલ / file: tools/content.py · ecard

જે હતું / before: મૂલ્યવાન ગ્રાહક

જે કર્યું / after: આદરણીય ગ્રાહકશ્રી / પ્રિય શ્રી {નામ}

«મૂલ્યવાન ગ્રાહક» એ અંગ્રેજી 'valued customer' નું શબ્દશઃ ભાષાન્તર છે. ગુજરાતી વ્યાવસાયિક પત્રમાં «આદરણીય ગ્રાહકશ્રી» કે «પ્રિય ગ્રાહક મિત્ર» વપરાય; નામ હોય ત્યારે «પ્રિય શ્રી …».

> A literal calque of 'valued customer'; Gujarati business letters use આદરણીય ગ્રાહકશ્રી / પ્રિય શ્રી …

### #10 · શબ્દ પસંદગી (અર્થ) · [મધ્યમ / medium]

ફાઈલ / file: tools/content.py (ગુજરાતી + બાયલિંગ્વલ ઈમેલ)

જે હતું / before: અધિકૃત ઉત્પાદનો

જે કર્યું / after: અસલી ઉત્પાદનો

«અધિકૃત» એટલે authorised/official; 'genuine products' માટે «અસલી» યોગ્ય છે.

> 'અધિકૃત' means authorised; 'genuine products' should be «અસલી ઉત્પાદનો».

### #11 · શબ્દ પસંદગી (અર્થ) · [મધ્યમ / medium]

ફાઈલ / file: tools/content.py (ગુજરાતી + બાયલિંગ્વલ)

જે હતું / before: હળવી સેવા

જે કર્યું / after: હસમુખ સેવા

«હળવી સેવા» નો શાબ્દિક અર્થ 'gentle/soft service' થાય. 'warm, friendly service' માટે «હસમુખ સેવા» યોગ્ય છે.

> 'હળવી સેવા' reads as 'light service'; 'warm, friendly service' is «હસમુખ સેવા».

### #12 · શબ્દ પસંદગી (અર્થ) · [મધ્યમ / medium]

ફાઈલ / file: tools/content.py (ગુજરાતી લેટર P.S.)

જે હતું / before: સલામતી જ દિવાળીનો સૌથી મોટો પુરુષાર્થ છે

જે કર્યું / after: સલામતી એ જ દિવાળીની સૌથી મોટી ભેટ છે

«પુરુષાર્થ» એટલે પ્રયત્ન/ધ્યેય (purushartha) — અહીં અર્થ બેસતો નથી. હેતુ 'સલામતી સૌથી મોટી ભેટ/અગ્રતા' એવો હતો.

> 'પુરુષાર્થ' means endeavour/goal — wrong here; 'safety is the greatest gift'.

### #13 · એકરૂપતા · [મધ્યમ / medium]

ફાઈલ / file: tools/content.py

જે હતું / before: પ્રમાણિક ભાવો (ઈમેલ) vs વાજબી ભાવો (લેટર)

જે કર્યું / after: બધે વાજબી ભાવ

એક જ અર્થ ('honest prices') માટે બે જુદા શબ્દો હતા. «વાજબી ભાવ» એ ગુજરાતી વ્યાવસાયિક રૂઢિ છે, તેથી બધે એક જ રાખ્યું.

> Two different terms for 'honest prices'; standardised on વાજબી ભાવ.

### #14 · એકરૂપતા · [મધ્યમ / medium]

ફાઈલ / file: tools/content.py

જે હતું / before: શુભકામનાઓ vs શુભેચ્છાઓ

જે કર્યું / after: બધે શુભેચ્છાઓ

એક જ દસ્તાવેજ સમૂહમાં બે રૂપ હતા; «શુભેચ્છાઓ» વધુ પ્રચલિત હોવાથી એકરૂપ કર્યું.

> Standardised on the more common શુભેચ્છાઓ.

### #15 · શબ્દ પસંદગી · [મધ્યમ / medium]

ફાઈલ / file: tools/content.py (ગુજરાતી ઈમેલ)

જે હતું / before: સ્માર્ટ હોમ ગિયર

જે કર્યું / after: સ્માર્ટ હોમ ઉપકરણો

«ગિયર» (gear) ગુજરાતી વાચકને અજાણ્યો શબ્દ છે; «ઉપકરણો» સ્પષ્ટ છે.

> 'ગિયર' is opaque; «ઉપકરણો» (devices) is clear.

### #16 · શબ્દ પસંદગી · [મધ્યમ / medium]

ફાઈલ / file: tools/content.py (ગુજરાતી લેટર)

જે હતું / before: છજ્જા માટે તહેવારની ફેરી લાઇટ્સ

જે કર્યું / after: બાલ્કની માટે તહેવારની ઝાલર (ફેરી લાઈટો)

«છજ્જો» એ છતની કિનારી/છાપરો છે; balcony માટે ગુજરાતીમાં «બાલ્કની» કે «અગાશી» વપરાય. «ફેરી» શબ્દનો ગુજરાતી અર્થ 'ફેરીવાળો/હોકર' થાય, તેથી સજાવટની લાઈટો માટે «ઝાલર» વાપર્યું અને કૌંસમાં અંગ્રેજી નામ રાખ્યું.

> «છજ્જો» is an eave, not a balcony; and «ફેરી» suggests a hawker — string lights are «ઝાલર».

### #17 · એકરૂપતા · [મધ્યમ / medium]

ફાઈલ / file: tools/content.py · cards

જે હતું / before: દીપો (લેટર/કાર્ડ) vs દીવા (ઈકાર્ડ)

જે કર્યું / after: બધે દીવા

માટીના દીવા માટે ગુજરાતીમાં «દીવો/દીવા» સ્વાભાવિક છે; «દીપ/દીપો» કાવ્યાત્મક છે. આખા સમૂહમાં એક જ રૂપ રાખ્યું.

> Standardised the everyday word દીવા across letters, cards and the e-card.

### #18 · શૈલી (પુનરાવર્તન) · [મધ્યમ / medium]

ફાઈલ / file: tools/build_cards.py (બાયલિંગ્વલ કાર્ડ)

જે હતું / before: દીપોનો પ્રકાશ તમારા જીવનને પ્રકાશિત કરે

જે કર્યું / after: દીવાનો પ્રકાશ તમારું જીવન ઝળહળાવે

એક જ વાક્યમાં «પ્રકાશ … પ્રકાશિત કરે» પુનરાવર્તન હતું; ટૂંકું અને સુંદર રૂપ આપ્યું.

> Removed the light/light-up repetition in one line.

### #19 · શૈલી (કેલ્ક) · [મધ્યમ / medium]

ફાઈલ / file: tools/content.py

જે હતું / before: બધું જ તમને એક ક્લિક દૂર છે

જે કર્યું / after: બધું જ માત્ર એક ક્લિકના અંતરે છે

અંગ્રેજી 'a click away' નું શબ્દશઃ ભાષાન્તર; ગુજરાતીમાં «એક ક્લિકના અંતરે» સ્વાભાવિક છે.

> De-calqued 'a click away'.

### #20 · શૈલી (શીર્ષક) · [નીચું / low]

ફાઈલ / file: ecard/index.html

જે હતું / before: દિવાળીમાં ત્રણ ધ્યાનની વાતો

જે કર્યું / after: દિવાળીમાં ધ્યાન રાખવાની ત્રણ બાબતો

«ત્રણ ધ્યાનની વાતો» અધૂરું બંધારણ હતું; યોગ્ય: «ધ્યાન રાખવાની ત્રણ બાબતો».

> Completed the heading construction.

### #21 · વ્યાકરણ (કૃદંત) · [નીચું / low]

ફાઈલ / file: ecard/index.html (ટીપ ૨)

જે હતું / before: ઝગમગ ઘર, સાચો ભાવ

જે કર્યું / after: ઝગમગતું ઘર, વાજબી ભાવ

વર્તમાન કૃદંત «ઝગમગતું» જોઈએ; સાથે «સાચો ભાવ» → «વાજબી ભાવ» (એકરૂપતા).

> Added the present participle and standardised the price word.

### #22 · એકરૂપતા (લિંગ) · [નીચું / low]

ફાઈલ / file: tools/content.py

જે હતું / before: ISI માર્કવાળા વાયર / માર્કવાળી વાયરિંગ

જે કર્યું / after: ISI માર્કવાળા વાયર / ISI માર્કવાળી વાયરિંગ (સ્પષ્ટ)

«વાયર» અને «વાયરિંગ» બંને માટે લિંગ અસંગત હતું; હવે વાયર (પુ.) અને વાયરિંગ (સ્ત્રી.) સ્પષ્ટ રાખ્યાં છે.

> Made the gender of વાયર / વાયરિંગ consistent.

### #23 · શબ્દ પસંદગી · [નીચું / low]

ફાઈલ / file: tools/content.py

જે હતું / before: શ્રી ગણપતિ

જે કર્યું / after: શ્રી ગણેશજી

બંને યોગ્ય છે, પણ ગુજરાતી વ્યવહારમાં «ગણેશજી» વધુ પ્રચલિત અને આપ્યો છે; વૈકલ્પિક સુધારો.

> Preferred the more idiomatic Gujarati honorific (optional change).

### #24 · અંગ્રેજી (વિષય-રેખા) · [નીચું / low]

ફાઈલ / file: tools/content.py (અંગ્રેજી ઈમેલ)

જે હતું / before: Subject: શુભ દિવાળી | Happy Diwali from ElectricalSkart.com

જે કર્યું / after: Subject: Happy Diwali from ElectricalSkart.com

અંગ્રેજી-માત્ર ઈમેલની વિષય-રેખામાં ગુજરાતી હતું; અંગ્રેજી ગ્રાહક માટે અંગ્રેજી-માત્ર રાખી. (બાયલિંગ્વલ ઈમેલમાં બંને ભાષા યથાવત છે.)

> The English-only e-mail had a Gujarati subject line; now English-only.

### #25 · અંગ્રેજી (ટોન) · [નીચું / low]

ફાઈલ / file: tools/content.py (લેટર + ઈમેલ)

જે હતું / before: Warm regards & sparklers, / With festive love,

જે કર્યું / after: Warm regards, / With warm festive wishes,

વ્યાવસાયિક પત્રમાં «sparklers» અને «festive love» અતિ-અનૌપચારિક હતાં; સંતુલિત ટોન આપી.

> Toned down overly playful closings for a business letter.

### #26 · અંગ્રેજી (કોલોકેશન) · [નીચું / low]

ફાઈલ / file: tools/content.py (અંગ્રેજી ઈમેલ + લેટર)

જે હતું / before: genuine products with honest prices … just as always / we are just a click away

જે કર્યું / after: genuine products at honest prices … as always / everything is just a click away

કિંમત સાથે 'at' વપરાય ('with' નહીં); અને યાદી વિષયક હોવાથી કર્તા 'everything' યોગ્ય છે.

> Prices take 'at'; the subject of the click-away sentence is now 'everything'.

### #27 · જોડણી/એકરૂપતા (README) · [નીચું / low]

ફાઈલ / file: README.md

જે હતું / before: ઈંગ્લિશ · ઇમેજ · એડિટ · રેન્ડર થયેલ છે

જે કર્યું / after: અંગ્રેજી · છબી · સંપાદન · રેન્ડર થયેલું છે

«ઇંગ્લિશ/ઇમેજ/એડિટ» ને બદલે ગુજરાતી શબ્દો; «પેજ … થયેલ» → «થયેલું» (નપુંસકલિંગ મેળ).

> Replaced English loans with Gujarati terms and fixed neuter agreement.

## ૨. નામ લખવાની જગ્યા · The name field

### ગ્રીટિંગ ફાઈલોમાં નામની જગ્યા ન હતી

હવે દરેક લેટર/ઈમેલ (.docx, .pdf, .txt) ની ટોચ પર સોનેરી ફ્રેમવાળી હાર છે: «ગ્રાહકનું નામ / Customer Name : …………» — નામ ન આપો તો લખવા માટે ખાલી લીટી છપાય, અને સંબોધન પણ «પ્રિય ગ્રાહકશ્રી …………,» સ્વરૂપે છપાય.

### નામ આપીને ફાઈલો બનાવવી

python3 tools/build_documents.py --name "રમેશ પટેલ"  →  documents/personal/ માં નામવાળી .docx/.pdf/.txt; સંબોધન «પ્રિય શ્રી રમેશ પટેલ,» / «Dear Ramesh Patel,» થાય.

### કાર્ડ પર નામની જગ્યા

cards/*-ForName.jpg = નામ લખવા માટે ખાલી ડોટેડ લાઇનવાળાં કાર્ડ; python3 tools/build_cards.py --name "રમેશ પટેલ" → cards/personal/ માં નામ છપેલાં કાર્ડ.

### ઈ-કાર્ડમાં નામ

ecard/index.html માં «નામ લખો / Write a name» બોક્સ; નામ લખતાં શુભેચ્છા, દીવા-સંદેશ અને શેર-ટેક્સ્ટ એ નામે બદલાય. લિંકમાં ?to=નામ મૂકી શકાય.

### એક જ કમાન્ડથી બધું

python3 tools/personalize.py --name "રમેશ પટેલ"  (અથવા --csv names.csv થી થોકમાં)

## ૩. આ અહેવાલ ફરી બનાવવો · Regenerating this report

python3 tools/build_extras.py   (સ્રોત / source: tools/audit_content.py)

ભૂલોનો સ્રોત-ડેટા audit_content.py માં છે, તેથી અહેવાલના .md, .docx અને .pdf હંમેશા એકસમાન રહે છે.
