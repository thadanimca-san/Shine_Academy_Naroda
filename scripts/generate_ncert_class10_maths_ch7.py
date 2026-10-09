import os
import json

def make_quiz(id_str, q_en, q_hi, q_gu, opts_en, opts_hi, opts_gu, correct_idx, expl_en, expl_hi, expl_gu, bloom="Apply", diff="Intermediate", mins=2):
    return {
        "id": id_str,
        "type": "quiz",
        "question": q_en,
        "options": opts_en,
        "correct_index": correct_idx,
        "explanation": expl_en,
        "question_hi": q_hi,
        "options_hi": opts_hi,
        "explanation_hi": expl_hi,
        "question_gu": q_gu,
        "options_gu": opts_gu,
        "explanation_gu": expl_gu,
        "bloom": bloom,
        "difficulty": diff,
        "estimated_minutes": mins
    }

def make_socratic(id_str, q_en, q_hi, q_gu, opts_en, opts_hi, opts_gu, correct_idx, expl_en, expl_hi, expl_gu, bloom="Apply", diff="Beginner", mins=2):
    return {
        "id": id_str,
        "type": "socratic_question",
        "question": q_en,
        "options": opts_en,
        "correct_index": correct_idx,
        "explanation": expl_en,
        "question_hi": q_hi,
        "options_hi": opts_hi,
        "explanation_hi": expl_hi,
        "question_gu": q_gu,
        "options_gu": opts_gu,
        "explanation_gu": expl_gu,
        "bloom": bloom,
        "difficulty": diff,
        "estimated_minutes": mins
    }

def make_theory(id_str, title_en, title_hi, title_gu, body_en, body_hi, body_gu, btype="theory", bloom="Understand", diff="Beginner", mins=3):
    return {
        "id": id_str,
        "type": btype,
        "title": title_en,
        "body": body_en,
        "title_hi": title_hi,
        "body_hi": body_hi,
        "title_gu": title_gu,
        "body_gu": body_gu,
        "bloom": bloom,
        "difficulty": diff,
        "estimated_minutes": mins
    }

def get_metadata():
    return {
        "id": "ncert_class10_maths_ch7",
        "title": "Chapter 7: Coordinate Geometry",
        "title_hi": "अध्याय 7: निर्देशांक ज्यामिति",
        "title_gu": "પ્રકરણ 7: યામ ભૂમિતિ",
        "subject": "Mathematics",
        "grade": "10",
        "board": "CBSE/GSEB",
        "curriculum": ["CBSE", "NCERT", "GSEB"],
        "language": "English, Hindi, Gujarati",
        "difficulty": "Intermediate",
        "estimated_minutes": 180,
        "version": "2.0.0",
        "author": "Shine Academy EduOS",
        "last_updated": "2026-10-01",
        "tags": [
            "coordinate_geometry",
            "distance_formula",
            "section_formula",
            "midpoint_formula",
            "cartesian_plane",
            "collinear_points"
        ]
    }

# =========================================================================
# PART 1: THE CARTESIAN BRIDGE, DISTANCE FORMULA & EXERCISE 7.1
# =========================================================================
def get_part1_blocks():
    blocks = []

    # 1. Hook (Step 1)
    blocks.append(make_theory(
        "C10M_CH7_1",
        "The Fly on the Ceiling: How Algebra Met Geometry",
        "छत पर मक्खी: कैसे बीजगणित और ज्यामिति का मिलन हुआ",
        "છત પર માખી: બીજગણિત અને ભૂમિતિનો અદ્ભુત સંગમ",
        "In the early 17th century, the French mathematician and philosopher René Descartes was lying in bed watching a fly crawl across his tiled ceiling. He wondered: *Is there a way to describe the exact position of that fly at any given moment using numbers?*\n\nHe realized that if he measured the distance of the fly from the left wall, and its distance from the bottom wall, the two numbers together $(x, y)$ would pinpoint the fly's location with 100% precision! This brilliant insight created **Coordinate Geometry (Cartesian Geometry)** — the revolutionary bridge connecting Algebra and Geometry.\n\nToday, this very idea powers GPS satellites navigating airplanes, Google Maps guiding your commute, pixels rendering 3D video games, and computer-guided surgical robots!",
        "17वीं शताब्दी की शुरुआत में, फ्रांसीसी गणितज्ञ और दार्शनिक रेने देकार्त बिस्तर पर लेटे हुए अपनी छत की टाइलों पर एक मक्खी को रेंगते हुए देख रहे थे। उन्होंने सोचा: *क्या किसी दिए गए क्षण में उस मक्खी की सटीक स्थिति को संख्याओं का उपयोग करके व्यक्त करने का कोई तरीका है?*\n\nउन्होंने महसूस किया कि यदि वे बाईं दीवार से मक्खी की दूरी और निचली दीवार से उसकी दूरी माप लें, तो ये दो संख्याएँ मिलकर $(x, y)$ मक्खी की स्थिति को 100% सटीकता के साथ निर्धारित कर देंगी! इस शानदार विचार ने **निर्देशांक ज्यामिति (कार्तीसीय ज्यामिति)** को जन्म दिया — जो बीजगणित और ज्यामिति को जोड़ने वाला क्रांतिकारी सेतु है।\n\nआज यही विचार हवाई जहाजों का मार्गदर्शन करने वाले जीपीएस उपग्रहों, गूगल मैप्स, 3D वीडियो गेम ग्राफिक्स और कंप्यूटर-निर्देशित सर्जिकल रोबोट को शक्ति प्रदान करता है!",
        "17મી સદીની શરૂઆતમાં, ફ્રેન્ચ ગણિતશાસ્ત્રી અને ફિલસૂફ રેને દેકાર્ત પથારીમાં સૂતા સૂતા છતની ટાઇલ્સ પર એક માખીને ચાલતી જોઈ રહ્યા હતા. તેમને વિચાર આવ્યો: *શું કોઈ ચોક્કસ ક્ષણે તે માખીનું ચોક્કસ સ્થાન સંખ્યાઓ દ્વારા દર્શાવવાની કોઈ રીત હોઈ શકે?*\n\nતેમને સમજાયું કે જો તેઓ ડાબી દીવાલથી માખીનું અંતર અને નીચેની દીવાલથી તેનું અંતર માપે, તો તે બે સંખ્યાઓ $(x, y)$ મળીને માખીના સ્થાનને 100% ચોકસાઈ સાથે દર્શાવી શકે છે! આ અદ્ભુત વિચારમાંથી **યામ ભૂમિતિ (કાર્તેઝિયન ભૂમિતિ)** નો જન્મ થયો — જે બીજગણિત અને ભૂમિતિને જોડતો ક્રાંતિકારી પુલ છે.\n\nઆજે આ જ સંકલ્પના વિમાનોનું સંચાલન કરતા GPS ઉપગ્રહો, ગૂગલ મેપ્સ, 3D વિડિયો ગેમ ગ્રાફિક્સ અને રોબોટિક સર્જરીમાં વપરાય છે!",
        btype="hook",
        bloom="Understand",
        diff="Beginner",
        mins=3
    ))

    # 2. Socratic Question (Step 2)
    blocks.append(make_socratic(
        "C10M_CH7_2",
        "Imagine you start at the origin (0, 0). You walk 4 units directly East along the x-axis, and then 3 units directly North parallel to the y-axis. What is your direct straight-line distance from the origin?",
        "कल्पना कीजिए कि आप मूलबिंदु (0, 0) से शुरू करते हैं। आप x-अक्ष के अनुदिश सीधे पूर्व दिशा में 4 इकाई चलते हैं, और फिर y-अक्ष के समानांतर सीधे उत्तर दिशा में 3 इकाई चलते हैं। मूलबिंदु से आपकी सीधी रेखा की दूरी कितनी है?",
        "કલ્પના કરો કે તમે ઉગમબિંદુ (0, 0) થી શરૂઆત કરો છો. તમે x-અક્ષ પર પૂર્વ દિશામાં સીધા 4 એકમ ચાલો છો, અને પછી y-અક્ષને સમાંતર ઉત્તર દિશામાં સીધા 3 એકમ ચાલો છો. ઉગમબિંદુથી તમારું સીધું અંતર કેટલું થશે?",
        ["5 units", "7 units", "4 units", "25 units"],
        ["5 इकाई", "7 इकाई", "4 इकाई", "25 इकाई"],
        ["5 એકમ", "7 એકમ", "4 એકમ", "25 એકમ"],
        0,
        "Walking East and then North forms a right-angled triangle where base = 4 units and perpendicular = 3 units. By the Pythagoras theorem: Distance = √(4² + 3²) = √(16 + 9) = √25 = 5 units!",
        "पूर्व और फिर उत्तर की ओर चलने से एक समकोण त्रिभुज बनता है जहाँ आधार = 4 इकाई और लंब = 3 इकाई है। पाइथागोरस प्रमेय द्वारा: दूरी = √(4² + 3²) = √(16 + 9) = √25 = 5 इकाई!",
        "પૂર્વ અને પછી ઉત્તર તરફ ચાલવાથી કાટકોણ ત્રિકોણ બને છે જ્યાં પાયો = 4 એકમ અને વેધ = 3 એકમ છે. પાયથાગોરસના પ્રમેય મુજબ: અંતર = √(4² + 3²) = √(16 + 9) = √25 = 5 એકમ!",
        bloom="Apply",
        diff="Beginner",
        mins=2
    ))

    # 3. Discovery: Building Pythagoras on the Grid (Step 3)
    blocks.append(make_theory(
        "C10M_CH7_3",
        "Discovery: Deriving Distance Between Any Two Points",
        "खोज: किन्हीं दो बिंदुओं के बीच की दूरी ज्ञात करना",
        "શોધ: કોઈપણ બે બિંદુઓ વચ્ચેનું અંતર તારવવું",
        "How do we find the distance between ANY two arbitrary points $P(x_1, y_1)$ and $Q(x_2, y_2)$ in the plane?\n\n1. Let us draw a horizontal line through $P$ and a vertical line through $Q$. They intersect at right angles at point $T(x_2, y_1)$.\n2. The horizontal segment $PT = |x_2 - x_1|$ (the change in x-coordinates, $\\Delta x$).\n3. The vertical segment $QT = |y_2 - y_1|$ (the change in y-coordinates, $\\Delta y$).\n4. Since $\\triangle PTQ$ is a right triangle with right angle at $T$, we apply the **Pythagoras Theorem**:\n$$PQ^2 = PT^2 + QT^2 = (x_2 - x_1)^2 + (y_2 - y_1)^2$$\n\nTaking the square root on both sides gives us the celebrated **Distance Formula**:\n$$PQ = \\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$",
        "तल में स्थित किन्हीं भी दो बिंदुओं $P(x_1, y_1)$ और $Q(x_2, y_2)$ के बीच की दूरी कैसे ज्ञात करें?\n\n1. बिंदु $P$ से एक क्षैतिज रेखा और बिंदु $Q$ से एक ऊर्ध्वाधर रेखा खींचें। वे बिंदु $T(x_2, y_1)$ पर समकोण पर प्रतिच्छेद करते हैं।\n2. क्षैतिज रेखाखंड $PT = |x_2 - x_1|$ (x-निर्देशांकों में अंतर, $\\Delta x$) है।\n3. ऊर्ध्वाधर रेखाखंड $QT = |y_2 - y_1|$ (y-निर्देशांकों में अंतर, $\\Delta y$) है।\n4. चूँकि $\\triangle PTQ$ बिंदु $T$ पर समकोण वाला एक समकोण त्रिभुज है, हम **पाइथागोरस प्रमेय** लागू करते हैं:\n$$PQ^2 = PT^2 + QT^2 = (x_2 - x_1)^2 + (y_2 - y_1)^2$$\n\nदोनों पक्षों का वर्गमूल लेने पर हमें सुप्रसिद्ध **दूरी सूत्र** प्राप्त होता है:\n$$PQ = \\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$",
        "સમતલમાં કોઈપણ બે યાદચ્છિક બિંદુઓ $P(x_1, y_1)$ અને $Q(x_2, y_2)$ વચ્ચેનું અંતર કેવી રીતે શોધી શકાય?\n\n1. બિંદુ $P$ માંથી સમક્ષિતિજ રેખા અને બિંદુ $Q$ માંથી શિરોલંબ રેખા દોરો. તેઓ બિંદુ $T(x_2, y_1)$ આગળ કાટખૂણે છેદે છે.\n2. સમક્ષિતિજ રેખાખંડ $PT = |x_2 - x_1|$ (x-યામોનો તફાવત, $\\Delta x$) છે.\n3. શિરોલંબ રેખાખંડ $QT = |y_2 - y_1|$ (y-યામોનો તફાવત, $\\Delta y$) છે.\n4. $\\triangle PTQ$ એ $T$ આગળ કાટખૂણો ધરાવતો કાટકોણ ત્રિકોણ હોવાથી, આપણે **પાયથાગોરસ પ્રમેય** લાગુ કરીએ:\n$$PQ^2 = PT^2 + QT^2 = (x_2 - x_1)^2 + (y_2 - y_1)^2$$\n\nબંને બાજુ વર્ગમૂળ લેતાં આપણને સુપ્રસિદ્ધ **અંતર સૂત્ર** મળે છે:\n$$PQ = \\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$",
        btype="discovery",
        bloom="Analyze",
        diff="Beginner",
        mins=3
    ))

    # 4. Reveal / Theory: The Distance Formula (Step 4)
    blocks.append(make_theory(
        "C10M_CH7_4",
        "The Distance Formula & Distance from Origin",
        "दूरी सूत्र और मूलबिंदु से दूरी",
        "અંતર સૂત્ર અને ઉગમબિંદુથી અંતર",
        "### 1. Distance Formula\nThe distance between two points $P(x_1, y_1)$ and $Q(x_2, y_2)$ is given by:\n$$d = \\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$\n\nNotice that since $(x_1 - x_2)^2 = (x_2 - x_1)^2$, you can subtract in either order! Just be consistent.\n\n### 2. Distance from the Origin\nThe distance of any point $P(x, y)$ from the origin $O(0, 0)$ is simply:\n$$OP = \\sqrt{(x - 0)^2 + (y - 0)^2} = \\sqrt{x^2 + y^2}$$\n\n### 3. Key Applications in Geometry\n- **Collinear Points:** Three points $A, B, C$ are collinear if the distance between the two farthest points equals the sum of the other two distances (e.g., $AB + BC = AC$).\n- **Equilateral Triangle:** All three side lengths are equal ($AB = BC = CA$).\n- **Isosceles Triangle:** Exactly two side lengths are equal.\n- **Right-angled Triangle:** The square of the longest side equals the sum of the squares of the other two sides ($c^2 = a^2 + b^2$).",
        "### 1. दूरी सूत्र\nदो बिंदुओं $P(x_1, y_1)$ और $Q(x_2, y_2)$ के बीच की दूरी निम्न सूत्र द्वारा दी जाती है:\n$$d = \\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$\n\nध्यान दें कि चूँकि $(x_1 - x_2)^2 = (x_2 - x_1)^2$, आप किसी भी क्रम में घटा सकते हैं! बस दोनों निर्देशांकों में क्रम का ध्यान रखें।\n\n### 2. मूलबिंदु से दूरी\nमूलबिंदु $O(0, 0)$ से किसी बिंदु $P(x, y)$ की दूरी अत्यंत सरल है:\n$$OP = \\sqrt{(x - 0)^2 + (y - 0)^2} = \\sqrt{x^2 + y^2}$$\n\n### 3. ज्यामिति में प्रमुख अनुप्रयोग\n- **संरेखी बिंदु:** तीन बिंदु $A, B, C$ संरेखी होते हैं यदि दो सबसे दूर स्थित बिंदुओं के बीच की दूरी अन्य दो दूरियों के योग के बराबर हो (जैसे, $AB + BC = AC$)।\n- **समबाहु त्रिभुज:** तीनों भुजाओं की लंबाइयाँ बराबर होती हैं ($AB = BC = CA$)।\n- **समद्विबाहु त्रिभुज:** किन्हीं दो भुजाओं की लंबाइयाँ बराबर होती हैं।\n- **समकोण त्रिभुज:** सबसे बड़ी भुजा का वर्ग अन्य दो भुजाओं के वर्गों के योग के बराबर होता है ($c^2 = a^2 + b^2$)।",
        "### 1. અંતર સૂત્ર\nબે બિંદુઓ $P(x_1, y_1)$ અને $Q(x_2, y_2)$ વચ્ચેનું અંતર આ સૂત્ર દ્વારા મળે છે:\n$$d = \\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$\n\nનોંધો કે $(x_1 - x_2)^2 = (x_2 - x_1)^2$ હોવાથી, તમે કોઈપણ ક્રમમાં બાદબાકી કરી શકો છો!\n\n### 2. ઉગમબિંદુથી અંતર\nઉગમબિંદુ $O(0, 0)$ થી કોઈપણ બિંદુ $P(x, y)$ નું અંતર:\n$$OP = \\sqrt{(x - 0)^2 + (y - 0)^2} = \\sqrt{x^2 + y^2}$$\n\n### 3. ભૂમિતિમાં મુખ્ય ઉપયોગો\n- **સમરેખ બિંદુઓ:** ત્રણ બિંદુઓ $A, B, C$ સમરેખ થાય જો સૌથી મોટા રેખાખંડની લંબાઈ બાકીના બે રેખાખંડોના સરવાળા જેટલી હોય (દા.ત., $AB + BC = AC$).\n- **સમબાજુ ત્રિકોણ:** ત્રણેય બાજુઓની લંબાઈ સમાન હોય ($AB = BC = CA$).\n- **સમદ્વિબાજુ ત્રિકોણ:** કોઈપણ બે બાજુઓની લંબાઈ સમાન હોય.\n- **કાટકોણ ત્રિકોણ:** સૌથી મોટી બાજુનો વર્ગ બાકીની બે બાજુઓના વર્ગોના સરવાળા જેટલો હોય ($c^2 = a^2 + b^2$).",
        btype="theory",
        bloom="Remember",
        diff="Beginner",
        mins=3
    ))

    # 5. Theory: Quadrilateral Tests
    blocks.append(make_theory(
        "C10M_CH7_5",
        "Distinguishing Quadrilaterals Using the Distance Formula",
        "दूरी सूत्र द्वारा विभिन्न चतुर्भुजों की पहचान",
        "અંતર સૂત્ર દ્વારા વિવિધ ચતુષ્કોણની ઓળખ",
        "To identify which quadrilateral is formed by four given points $A, B, C, D$, compute all 4 sides and both diagonals ($AC$ and $BD$):\n\n| Quadrilateral | Sides Condition | Diagonals Condition |\n| :--- | :--- | :--- |\n| **Parallelogram** | Opposite sides equal ($AB = CD$, $BC = DA$) | Diagonals NOT equal ($AC \\ne BD$) |\n| **Rectangle** | Opposite sides equal ($AB = CD$, $BC = DA$) | Diagonals ARE equal ($AC = BD$) |\n| **Rhombus** | All 4 sides equal ($AB = BC = CD = DA$) | Diagonals NOT equal ($AC \\ne BD$) |\n| **Square** | All 4 sides equal ($AB = BC = CD = DA$) | Diagonals ARE equal ($AC = BD$) |\n\n*Golden Rule:* Never conclude a shape is a square just because 4 sides are equal; you MUST test whether the diagonals are equal as well!",
        "चार दिए गए बिंदुओं $A, B, C, D$ द्वारा बनने वाले चतुर्भुज की पहचान करने के लिए चारों भुजाओं और दोनों विकर्णों ($AC$ और $BD$) की गणना करें:\n\n| चतुर्भुज | भुजाओं की शर्त | विकर्णों की शर्त |\n| :--- | :--- | :--- |\n| **समांतर चतुर्भुज** | सम्मुख भुजाएँ बराबर ($AB = CD$, $BC = DA$) | विकर्ण बराबर नहीं ($AC \\ne BD$) |\n| **आयत** | सम्मुख भुजाएँ बराबर ($AB = CD$, $BC = DA$) | विकर्ण बराबर होते हैं ($AC = BD$) |\n| **समचतुर्भुज** | चारों भुजाएँ बराबर ($AB = BC = CD = DA$) | विकर्ण बराबर नहीं ($AC \\ne BD$) |\n| **वर्ग** | चारों भुजाएँ बराबर ($AB = BC = CD = DA$) | विकर्ण बराबर होते हैं ($AC = BD$) |\n\n*स्वर्ण नियम:* केवल चारों भुजाएँ बराबर होने पर किसी आकृति को वर्ग न कहें; आपको यह भी जांचना अनिवार्य है कि विकर्ण भी बराबर हैं या नहीं!",
        "આપેલા ચાર બિંદુઓ $A, B, C, D$ દ્વારા બનતા ચતુષ્કોણનો પ્રકાર નક્કી કરવા માટે બધી 4 બાજુઓ અને બંને વિકર્ણો ($AC$ અને $BD$) શોધો:\n\n| ચતુષ્કોણ | બાજુઓની શરત | વિકર્ણોની શરત |\n| :--- | :--- | :--- |\n| **સમાંતરબાજુ ચતુષ્કોણ** | સામસામેની બાજુઓ સમાન ($AB = CD$, $BC = DA$) | વિકર્ણો સમાન નથી ($AC \\ne BD$) |\n| **લંબચોરસ** | સામસામેની બાજુઓ સમાન ($AB = CD$, $BC = DA$) | વિકર્ણો સમાન હોય છે ($AC = BD$) |\n| **સમબાજુ ચતુષ્કોણ** | ચારેય બાજુઓ સમાન ($AB = BC = CD = DA$) | વિકર્ણો સમાન નથી ($AC \\ne BD$) |\n| **ચોરસ** | ચારેય બાજુઓ સમાન ($AB = BC = CD = DA$) | વિકર્ણો સમાન હોય છે ($AC = BD$) |\n\n*સુવર્ણ નિયમ:* માત્ર ચારેય બાજુઓ સમાન જોઈને ચોરસ જાહેર ન કરો; બંને વિકર્ણો સમાન છે કે નહીં તે ચકાસવું અનિવાર્ય છે!",
        btype="theory",
        bloom="Understand",
        diff="Intermediate",
        mins=3
    ))

    # 6. Teacher Tip (Step 5)
    blocks.append(make_theory(
        "C10M_CH7_6",
        "Teacher Tip: The 3 Deadliest Traps in Distance Calculations",
        "शिक्षक युक्ति: दूरी की गणना में 3 सबसे घातक गलतियाँ",
        "શિક્ષકની સલાહ: અંતરની ગણતરીમાં થતી 3 ગંભીર ભૂલો",
        "**Trap 1: The Double Negative Trap**\nWhen subtracting a negative coordinate, remember that $x_2 - (-x_1) = x_2 + x_1$.\n*Example:* If $x_2 = 3$ and $x_1 = -2$, then $(x_2 - x_1) = 3 - (-2) = 3 + 2 = 5$, NOT $3 - 2 = 1$!\n\n**Trap 2: Splitting the Square Root (The Illegal Shortcut)**\nNever write $\\sqrt{a^2 + b^2} = a + b$! This is mathematically false.\n*Example:* $\\sqrt{3^2 + 4^2} = \\sqrt{9 + 16} = \\sqrt{25} = 5$, whereas $3 + 4 = 7$.\n\n**Trap 3: Distance is Always Non-Negative**\nDistance is a physical scalar measurement of length. Hence, distance $d \\ge 0$. While solving $d^2 = 36$, take $d = +6$, not $-6$.",
        "**गलती 1: दोहरे ऋण चिह्न की गलती**\nऋणात्मक निर्देशांक घटाते समय याद रखें कि $x_2 - (-x_1) = x_2 + x_1$ होता है।\n*उदाहरण:* यदि $x_2 = 3$ और $x_1 = -2$, तो $(x_2 - x_1) = 3 - (-2) = 3 + 2 = 5$ होगा, $3 - 2 = 1$ नहीं!\n\n**गलती 2: वर्गमूल को अलग करना (अवैध शॉर्टकट)**\nकभी भी $\\sqrt{a^2 + b^2} = a + b$ न लिखें! यह गणितीय रूप से असत्य है।\n*उदाहरण:* $\\sqrt{3^2 + 4^2} = \\sqrt{9 + 16} = \\sqrt{25} = 5$, जबकि $3 + 4 = 7$ होता है।\n\n**गलती 3: दूरी हमेशा गैर-ऋणात्मक होती है**\nदूरी लंबाई का एक भौतिक माप है। इसलिए दूरी $d \\ge 0$ होती है। $d^2 = 36$ को हल करते समय दूरी $d = +6$ लें, $-6$ नहीं।",
        "**ભૂલ 1: બેવડા ઋણ ચિહ્નની ભૂલ**\nઋણ યામની બાદબાકી કરતી વખતે યાદ રાખો કે $x_2 - (-x_1) = x_2 + x_1$ થાય.\n*ઉદાહરણ:* જો $x_2 = 3$ અને $x_1 = -2$ હોય, તો $(x_2 - x_1) = 3 - (-2) = 3 + 2 = 5$ થાય, $3 - 2 = 1$ નહીં!\n\n**ભૂલ 2: વર્ગમૂળ છૂટું પાડવાની ગેરસમજ**\nક્યારેય $\\sqrt{a^2 + b^2} = a + b$ ન લખો! આ ગાણિતિક રીતે તદ્દન ખોટું છે.\n*ઉદાહરણ:* $\\sqrt{3^2 + 4^2} = \\sqrt{9 + 16} = \\sqrt{25} = 5$, જ્યારે $3 + 4 = 7$ થાય છે.\n\n**ભૂલ 3: અંતર હંમેશા અનૃણ (ધન કે શૂન્ય) જ હોય**\nઅંતર એ લંબાઈનું ભૌતિક માપ છે, તેથી અંતર $d \\ge 0$ હોય. $d^2 = 36$ ઉકેલતી વખતે અંતર $d = +6$ લેવું, $-6$ નહીં.",
        btype="teacher_tip",
        bloom="Analyze",
        diff="Beginner",
        mins=2
    ))

    # 7. NCERT Example 1
    blocks.append(make_quiz(
        "C10M_CH7_EG1",
        "NCERT Example 1: Do the points (3, 2), (-2, -3) and (2, 3) form a triangle? If so, name the type of triangle formed.",
        "NCERT उदाहरण 1: क्या बिंदु (3, 2), (-2, -3) और (2, 3) एक त्रिभुज बनाते हैं? यदि हाँ, तो बताइए कि किस प्रकार का त्रिभुज बनता है।",
        "NCERT ઉદાહરણ 1: શું બિંદુઓ (3, 2), (-2, -3) અને (2, 3) ત્રિકોણ બનાવે છે? જો હા, તો બનતા ત્રિકોણનો પ્રકાર જણાવો.",
        [
            "Yes, a right-angled triangle",
            "Yes, an equilateral triangle",
            "No, the points are collinear",
            "Yes, an obtuse-angled isosceles triangle"
        ],
        [
            "हाँ, एक समकोण त्रिभुज",
            "हाँ, एक समबाहु त्रिभुज",
            "नहीं, बिंदु संरेखी हैं",
            "हाँ, एक अधिककोण समद्विबाहु त्रिभुज"
        ],
        [
            "હા, કાટકોણ ત્રિકોણ",
            "હા, સમબાજુ ત્રિકોણ",
            "ના, બિંદુઓ સમરેખ છે",
            "હા, ગુરુકોણ સમદ્વિબાજુ ત્રિકોણ"
        ],
        0,
        "Let P(3, 2), Q(-2, -3), R(2, 3).\nPQ = √((-2-3)² + (-3-2)²) = √(25 + 25) = √50 ≈ 7.07\nQR = √((2-(-2))² + (3-(-3))²) = √(16 + 36) = √52 ≈ 7.21\nPR = √((2-3)² + (3-2)²) = √(1 + 1) = √2 ≈ 1.41\nSince sum of any two distances is greater than the third, a triangle is formed.\nAlso, PQ² + PR² = 50 + 2 = 52 = QR². By converse of Pythagoras theorem, ∠P = 90°. It is a right-angled triangle!",
        "माना P(3, 2), Q(-2, -3), R(2, 3).\nPQ = √((-2-3)² + (-3-2)²) = √(25 + 25) = √50 ≈ 7.07\nQR = √((2-(-2))² + (3-(-3))²) = √(16 + 36) = √52 ≈ 7.21\nPR = √((2-3)² + (3-2)²) = √(1 + 1) = √2 ≈ 1.41\nचूँकि किन्हीं दो भुजाओं का योग तीसरी भुजा से बड़ा है, अतः त्रिभुज बनता है।\nसाथ ही, PQ² + PR² = 50 + 2 = 52 = QR²। पाइथागोरस प्रमेय के विलोम द्वारा, ∠P = 90° है। यह एक समकोण त्रिभुज है!",
        "ધારો કે P(3, 2), Q(-2, -3), R(2, 3).\nPQ = √((-2-3)² + (-3-2)²) = √(25 + 25) = √50 ≈ 7.07\nQR = √((2-(-2))² + (3-(-3))²) = √(16 + 36) = √52 ≈ 7.21\nPR = √((2-3)² + (3-2)²) = √(1 + 1) = √2 ≈ 1.41\nકોઈપણ બે બાજુઓનો સરવાળો ત્રીજી બાજુ કરતાં મોટો હોવાથી ત્રિકોણ રચાય છે.\nવળી, PQ² + PR² = 50 + 2 = 52 = QR². પાયથાગોરસના પ્રતીપ પ્રમેય મુજબ ∠P = 90° થાય. આથી તે કાટકોણ ત્રિકોણ છે!",
        bloom="Apply",
        diff="Intermediate",
        mins=3
    ))

    # 8. NCERT Example 4
    blocks.append(make_quiz(
        "C10M_CH7_EG4",
        "NCERT Example 4: Find a relation between x and y such that the point (x, y) is equidistant from the points (7, 1) and (3, 5).",
        "NCERT उदाहरण 4: x और y में एक ऐसा संबंध ज्ञात कीजिए ताकि बिंदु (x, y) बिंदुओं (7, 1) और (3, 5) से समदूरस्थ हो।",
        "NCERT ઉદાહરણ 4: x અને y વચ્ચેનો એવો સંબંધ મેળવો કે જેથી બિંદુ (x, y) એ બિંદુઓ (7, 1) અને (3, 5) થી સમાન અંતરે હોય.",
        [
            "x - y = 2",
            "x + y = 2",
            "2x - y = 5",
            "x - 2y = 1"
        ],
        [
            "x - y = 2",
            "x + y = 2",
            "2x - y = 5",
            "x - 2y = 1"
        ],
        [
            "x - y = 2",
            "x + y = 2",
            "2x - y = 5",
            "x - 2y = 1"
        ],
        0,
        "Let P(x, y), A(7, 1), and B(3, 5). Given AP = BP ⇒ AP² = BP².\n(x - 7)² + (y - 1)² = (x - 3)² + (y - 5)²\nx² - 14x + 49 + y² - 2y + 1 = x² - 6x + 9 + y² - 10y + 25\n-14x - 2y + 50 = -6x - 10y + 34\n-14x + 6x - 2y + 10y = 34 - 50\n-8x + 8y = -16 ⇒ Dividing by -8 gives: x - y = 2.",
        "माना P(x, y), A(7, 1) और B(3, 5) हैं। दिया है AP = BP ⇒ AP² = BP²।\n(x - 7)² + (y - 1)² = (x - 3)² + (y - 5)²\nx² - 14x + 49 + y² - 2y + 1 = x² - 6x + 9 + y² - 10y + 25\n-14x - 2y + 50 = -6x - 10y + 34\n-8x + 8y = -16 ⇒ -8 से भाग देने पर: x - y = 2 प्राप्त होता है।",
        "ધારો કે P(x, y), A(7, 1) અને B(3, 5) છે. આપેલ છે AP = BP ⇒ AP² = BP².\n(x - 7)² + (y - 1)² = (x - 3)² + (y - 5)²\nx² - 14x + 49 + y² - 2y + 1 = x² - 6x + 9 + y² - 10y + 25\n-14x - 2y + 50 = -6x - 10y + 34\n-8x + 8y = -16 ⇒ -8 વડે ભાગતાં: x - y = 2 મળે છે.",
        bloom="Apply",
        diff="Intermediate",
        mins=2
    ))

    # 9. Exercise 7.1 Q1(i)
    blocks.append(make_quiz(
        "C10M_CH7_EX7.1_Q1_p1",
        "Exercise 7.1 (Q1.i): Find the distance between the pair of points (2, 3) and (4, 1).",
        "प्रश्नावली 7.1 (Q1.i): बिंदुओं (2, 3) और (4, 1) के बीच की दूरी ज्ञात कीजिए।",
        "સ્વાધ્યાય 7.1 (Q1.i): બિંદુઓની જોડ (2, 3) અને (4, 1) વચ્ચેનું અંતર શોધો.",
        ["2√2 units", "4 units", "√8 units only", "2 units"],
        ["2√2 इकाई", "4 इकाई", "केवल √8 इकाई", "2 इकाई"],
        ["2√2 એકમ", "4 એકમ", "માત્ર √8 એકમ", "2 એકમ"],
        0,
        "Using distance formula: d = √((4 - 2)² + (1 - 3)²) = √(2² + (-2)²) = √(4 + 4) = √8 = 2√2 units.",
        "दूरी सूत्र का उपयोग करने पर: d = √((4 - 2)² + (1 - 3)²) = √(2² + (-2)²) = √(4 + 4) = √8 = 2√2 इकाई।",
        "અંતર સૂત્રનો ઉપયોગ કરતાં: d = √((4 - 2)² + (1 - 3)²) = √(2² + (-2)²) = √(4 + 4) = √8 = 2√2 એકમ.",
        bloom="Apply",
        diff="Beginner",
        mins=2
    ))

    # 10. Exercise 7.1 Q1(ii)
    blocks.append(make_quiz(
        "C10M_CH7_EX7.1_Q1_p2",
        "Exercise 7.1 (Q1.ii): Find the distance between the pair of points (-5, 7) and (-1, 3).",
        "प्रश्नावली 7.1 (Q1.ii): बिंदुओं (-5, 7) और (-1, 3) के बीच की दूरी ज्ञात कीजिए।",
        "સ્વાધ્યાય 7.1 (Q1.ii): બિંદુઓની જોડ (-5, 7) અને (-1, 3) વચ્ચેનું અંતર શોધો.",
        ["4√2 units", "16 units", "√32 units only", "8 units"],
        ["4√2 इकाई", "16 इकाई", "केवल √32 इकाई", "8 इकाई"],
        ["4√2 એકમ", "16 એકમ", "માત્ર √32 એકમ", "8 એકમ"],
        0,
        "d = √((-1 - (-5))² + (3 - 7)²) = √((-1 + 5)² + (-4)²) = √(4² + 16) = √(16 + 16) = √32 = 4√2 units.",
        "d = √((-1 - (-5))² + (3 - 7)²) = √((-1 + 5)² + (-4)²) = √(4² + 16) = √(16 + 16) = √32 = 4√2 इकाई।",
        "d = √((-1 - (-5))² + (3 - 7)²) = √((-1 + 5)² + (-4)²) = √(4² + 16) = √(16 + 16) = √32 = 4√2 એકમ.",
        bloom="Apply",
        diff="Beginner",
        mins=2
    ))

    # 11. Exercise 7.1 Q1(iii)
    blocks.append(make_quiz(
        "C10M_CH7_EX7.1_Q1_p3",
        "Exercise 7.1 (Q1.iii): Find the distance between the pair of points (a, b) and (-a, -b).",
        "प्रश्नावली 7.1 (Q1.iii): बिंदुओं (a, b) और (-a, -b) के बीच की दूरी ज्ञात कीजिए।",
        "સ્વાધ્યાય 7.1 (Q1.iii): બિંદુઓની જોડ (a, b) અને (-a, -b) વચ્ચેનું અંતર શોધો.",
        ["2√(a² + b²)", "√(a² + b²)", "4(a² + b²)", "2(a + b)"],
        ["2√(a² + b²)", "√(a² + b²)", "4(a² + b²)", "2(a + b)"],
        ["2√(a² + b²)", "√(a² + b²)", "4(a² + b²)", "2(a + b)"],
        0,
        "d = √((-a - a)² + (-b - b)²) = √((-2a)² + (-2b)²) = √(4a² + 4b²) = √(4(a² + b²)) = 2√(a² + b²).",
        "d = √((-a - a)² + (-b - b)²) = √((-2a)² + (-2b)²) = √(4a² + 4b²) = √(4(a² + b²)) = 2√(a² + b²)।",
        "d = √((-a - a)² + (-b - b)²) = √((-2a)² + (-2b)²) = √(4a² + 4b²) = √(4(a² + b²)) = 2√(a² + b²).",
        bloom="Apply",
        diff="Intermediate",
        mins=2
    ))

    # 12. Exercise 7.1 Q2
    blocks.append(make_quiz(
        "C10M_CH7_EX7.1_Q2",
        "Exercise 7.1 (Q2): Find the distance between the points (0, 0) and (36, 15). If Town B is located 36 km east and 15 km north of Town A, what is the straight-line distance between Town A and Town B?",
        "प्रश्नावली 7.1 (Q2): बिंदुओं (0, 0) और (36, 15) के बीच की दूरी ज्ञात कीजिए। यदि शहर B, शहर A से 36 किमी पूर्व और 15 किमी उत्तर में स्थित है, तो शहर A और शहर B के बीच की सीधी दूरी कितनी है?",
        "સ્વાધ્યાય 7.1 (Q2): બિંદુઓ (0, 0) અને (36, 15) વચ્ચેનું અંતર શોધો. જો શહેર B એ શહેર A થી 36 કિમી પૂર્વમાં અને 15 કિમી ઉત્તરમાં આવેલું હોય, તો બંને શહેરો વચ્ચેનું સીધું અંતર કેટલું થશે?",
        ["39 km", "51 km", "45 km", "36 km"],
        ["39 किमी", "51 किमी", "45 किमी", "36 किमी"],
        ["39 કિમી", "51 કિમી", "45 કિમી", "36 કિમી"],
        0,
        "Distance from origin: d = √(x² + y²) = √(36² + 15²) = √(1296 + 225) = √1521 = 39 km. The straight-line distance between Town A and Town B is exactly 39 km.",
        "मूलबिंदु से दूरी: d = √(x² + y²) = √(36² + 15²) = √(1296 + 225) = √1521 = 39 किमी। शहर A और शहर B के बीच की सीधी दूरी ठीक 39 किमी है।",
        "ઉગમબિંદુથી અંતર: d = √(x² + y²) = √(36² + 15²) = √(1296 + 225) = √1521 = 39 કિમી. શહેર A અને શહેર B વચ્ચેનું સીધું અંતર બરાબર 39 કિમી છે.",
        bloom="Apply",
        diff="Beginner",
        mins=2
    ))

    # 13. Exercise 7.1 Q3
    blocks.append(make_quiz(
        "C10M_CH7_EX7.1_Q3",
        "Exercise 7.1 (Q3): Determine if the points (1, 5), (2, 3) and (-2, -11) are collinear.",
        "प्रश्नावली 7.1 (Q3): निर्धारित कीजिए कि क्या बिंदु (1, 5), (2, 3) और (-2, -11) संरेखी हैं।",
        "સ્વાધ્યાય 7.1 (Q3): ચકાસો કે શું બિંદુઓ (1, 5), (2, 3) અને (-2, -11) સમરેખ છે?",
        [
            "No, the points are not collinear",
            "Yes, because AB + BC = AC",
            "Yes, because they form an equilateral triangle",
            "Cannot be determined without a graph"
        ],
        [
            "नहीं, बिंदु संरेखी नहीं हैं",
            "हाँ, क्योंकि AB + BC = AC",
            "हाँ, क्योंकि वे एक समबाहु त्रिभुज बनाते हैं",
            "ग्राफ के बिना निर्धारित नहीं किया जा सकता"
        ],
        [
            "ના, બિંદુઓ સમરેખ નથી",
            "હા, કારણ કે AB + BC = AC થાય છે",
            "હા, કારણ કે તેઓ સમબાજુ ત્રિકોણ રચે છે",
            "આલેખ વગર નક્કી કરી શકાતું નથી"
        ],
        0,
        "Let A(1, 5), B(2, 3), C(-2, -11).\nAB = √((2-1)² + (3-5)²) = √(1 + 4) = √5 ≈ 2.24\nBC = √((-2-2)² + (-11-3)²) = √(16 + 196) = √212 = 2√53 ≈ 14.56\nAC = √((-2-1)² + (-11-5)²) = √(9 + 256) = √265 ≈ 16.28\nHere, AB + BC = √5 + √212 ≠ √265 (AC). The sum of any two distances is NOT equal to the third. Hence, the points are NOT collinear.",
        "माना A(1, 5), B(2, 3), C(-2, -11).\nAB = √((2-1)² + (3-5)²) = √(1 + 4) = √5\nBC = √((-2-2)² + (-11-3)²) = √(16 + 196) = √212 = 2√53\nAC = √((-2-1)² + (-11-5)²) = √(9 + 256) = √265\nयहाँ, AB + BC = √5 + 2√53 ≠ √265 (AC)। किन्हीं दो दूरियों का योग तीसरी के बराबर नहीं है। अतः बिंदु संरेखी नहीं हैं।",
        "ધારો કે A(1, 5), B(2, 3), C(-2, -11).\nAB = √((2-1)² + (3-5)²) = √(1 + 4) = √5\nBC = √((-2-2)² + (-11-3)²) = √(16 + 196) = √212 = 2√53\nAC = √((-2-1)² + (-11-5)²) = √(9 + 256) = √265\nઅહીં, AB + BC = √5 + 2√53 ≠ √265 (AC). કોઈપણ બે અંતરોનો સરવાળો ત્રીજા અંતર જેટલો થતો નથી. તેથી આ બિંદુઓ સમરેખ નથી.",
        bloom="Analyze",
        diff="Intermediate",
        mins=3
    ))

    # 14. Exercise 7.1 Q4
    blocks.append(make_quiz(
        "C10M_CH7_EX7.1_Q4",
        "Exercise 7.1 (Q4): Check whether (5, -2), (6, 4) and (7, -2) are the vertices of an isosceles triangle.",
        "प्रश्नावली 7.1 (Q4): जाँच कीजिए कि क्या (5, -2), (6, 4) और (7, -2) एक समद्विबाहु त्रिभुज के शीर्ष हैं।",
        "સ્વાધ્યાય 7.1 (Q4): ચકાસો કે શું (5, -2), (6, 4) અને (7, -2) એ સમદ્વિબાજુ ત્રિકોણના શિરોબિંદુઓ છે?",
        [
            "Yes, because two sides have equal length √37",
            "No, all three sides are unequal",
            "No, it is an equilateral triangle with side 2",
            "No, the points lie on a straight line"
        ],
        [
            "हाँ, क्योंकि दो भुजाओं की लंबाई √37 बराबर है",
            "नहीं, तीनों भुजाएँ असमान हैं",
            "नहीं, यह 2 भुजा वाला एक समबाहु त्रिभुज है",
            "नहीं, बिंदु एक सीधी रेखा पर स्थित हैं"
        ],
        [
            "હા, કારણ કે બે બાજુઓની લંબાઈ √37 સમાન છે",
            "ના, ત્રણેય બાજુઓ અસમાન છે",
            "ના, તે 2 બાજુવાળો સમબાજુ ત્રિકોણ છે",
            "ના, બિંદુઓ સીધી રેખા પર આવેલા છે"
        ],
        0,
        "Let A(5, -2), B(6, 4), C(7, -2).\nAB = √((6-5)² + (4 - (-2))²) = √(1² + 6²) = √(1 + 36) = √37\nBC = √((7-6)² + (-2-4)²) = √(1² + (-6)²) = √(1 + 36) = √37\nCA = √((7-5)² + (-2 - (-2))²) = √(2² + 0²) = √4 = 2\nSince AB = BC = √37 ≠ CA, triangle ABC has two equal sides. Thus, it is an isosceles triangle!",
        "माना A(5, -2), B(6, 4), C(7, -2).\nAB = √((6-5)² + (4 - (-2))²) = √(1² + 6²) = √37\nBC = √((7-6)² + (-2-4)²) = √(1² + (-6)²) = √37\nCA = √((7-5)² + (-2 - (-2))²) = √(2² + 0²) = 2\nचूँकि AB = BC = √37 ≠ CA, अतः त्रिभुज की दो भुजाएँ बराबर हैं। इसलिए यह एक समद्विबाहु त्रिभुज है!",
        "ધારો કે A(5, -2), B(6, 4), C(7, -2).\nAB = √((6-5)² + (4 - (-2))²) = √(1² + 6²) = √37\nBC = √((7-6)² + (-2-4)²) = √(1² + (-6)²) = √37\nCA = √((7-5)² + (-2 - (-2))²) = √(2² + 0²) = 2\nઅહીં AB = BC = √37 ≠ CA હોવાથી, બે બાજુઓ સમાન છે. તેથી તે સમદ્વિબાજુ ત્રિકોણ છે!",
        bloom="Apply",
        diff="Beginner",
        mins=2
    ))

    # 15. Exercise 7.1 Q5
    blocks.append(make_quiz(
        "C10M_CH7_EX7.1_Q5",
        "Exercise 7.1 (Q5): In a classroom, 4 friends are seated at the points A(3, 4), B(6, 7), C(9, 4) and D(6, 1). Champa claims ABCD is a square, while Chameli disagrees. Using the distance formula, determine who is correct.",
        "प्रश्नावली 7.1 (Q5): एक कक्षा में, 4 मित्र बिंदुओं A(3, 4), B(6, 7), C(9, 4) और D(6, 1) पर बैठे हैं। चंपा का दावा है कि ABCD एक वर्ग है, जबकि चमेली इससे असहमत है। दूरी सूत्र का प्रयोग करके बताइए कि कौन सही है।",
        "સ્વાધ્યાય 7.1 (Q5): એક વર્ગખંડમાં 4 મિત્રો A(3, 4), B(6, 7), C(9, 4) અને D(6, 1) બિંદુઓ પર બેઠા છે. ચંપા કહે છે કે ABCD ચોરસ છે, જ્યારે ચમેલી અસહમત થાય છે. અંતર સૂત્રનો ઉપયોગ કરીને નક્કી કરો કે કોણ સાચું છે?",
        [
            "Champa is correct (ABCD is a square because all 4 sides are 3√2 and both diagonals are 6)",
            "Chameli is correct (ABCD is only a rhombus because diagonals are unequal)",
            "Chameli is correct (ABCD is a rectangle with unequal sides)",
            "Neither is correct (the 4 points form an irregular quadrilateral)"
        ],
        [
            "चंपा सही है (ABCD एक वर्ग है क्योंकि चारों भुजाएँ 3√2 हैं और दोनों विकर्ण 6 हैं)",
            "चमेली सही है (ABCD केवल एक समचतुर्भुज है क्योंकि विकर्ण असमान हैं)",
            "चमेली सही है (ABCD असमान भुजाओं वाला एक आयत है)",
            "कोई भी सही नहीं है (चारों बिंदु एक अनियमित चतुर्भुज बनाते हैं)"
        ],
        [
            "ચંપા સાચી છે (ABCD ચોરસ છે કારણ કે બધી 4 બાજુઓ 3√2 અને બંને વિકર્ણો 6 છે)",
            "ચમેલી સાચી છે (ABCD માત્ર સમબાજુ ચતુષ્કોણ છે કારણ કે વિકર્ણો અસમાન છે)",
            "ચમેલી સાચી છે (ABCD અસમાન બાજુઓવાળો લંબચોરસ છે)",
            "કોઈ સાચું નથી (ચાર બિંદુઓ અનિયમિત ચતુષ્કોણ રચે છે)"
        ],
        0,
        "Calculate sides:\nAB = √((6-3)² + (7-4)²) = √(9 + 9) = √18 = 3√2\nBC = √((9-6)² + (4-7)²) = √(9 + 9) = √18 = 3√2\nCD = √((6-9)² + (1-4)²) = √(9 + 9) = √18 = 3√2\nDA = √((3-6)² + (4-1)²) = √(9 + 9) = √18 = 3√2\nAll 4 sides are equal to 3√2.\nCalculate diagonals:\nAC = √((9-3)² + (4-4)²) = √36 = 6\nBD = √((6-6)² + (1-7)²) = √36 = 6\nSince all 4 sides are equal AND both diagonals are equal, ABCD is a square! Therefore, Champa is correct.",
        "भुजाओं की गणना:\nAB = √((6-3)² + (7-4)²) = √18 = 3√2\nBC = √((9-6)² + (4-7)²) = √18 = 3√2\nCD = √((6-9)² + (1-4)²) = √18 = 3√2\nDA = √((3-6)² + (4-1)²) = √18 = 3√2\nचारों भुजाएँ 3√2 के बराबर हैं।\nविकर्णों की गणना:\nAC = √((9-3)² + (4-4)²) = √36 = 6\nBD = √((6-6)² + (1-7)²) = √36 = 6\nचूँकि चारों भुजाएँ बराबर हैं और दोनों विकर्ण भी बराबर हैं, अतः ABCD एक वर्ग है! इसलिए चंपा सही है।",
        "બાજુઓની ગણતરી:\nAB = BC = CD = DA = √((3)² + (3)²) = √18 = 3√2\nચારેય બાજુઓ સમાન છે.\nવિકર્ણોની ગણતરી:\nAC = √((9-3)² + 0²) = √36 = 6\nBD = √(0² + (1-7)²) = √36 = 6\nબધી 4 બાજુઓ સમાન છે અને બંને વિકર્ણો પણ સમાન છે, માટે ABCD ચોરસ છે! તેથી ચંપા સાચી છે.",
        bloom="Analyze",
        diff="Intermediate",
        mins=3
    ))

    # 16. Exercise 7.1 Q6(i)
    blocks.append(make_quiz(
        "C10M_CH7_EX7.1_Q6_p1",
        "Exercise 7.1 (Q6.i): Name the type of quadrilateral formed by the points (-1, -2), (1, 0), (-1, 2) and (-3, 0).",
        "प्रश्नावली 7.1 (Q6.i): बिंदुओं (-1, -2), (1, 0), (-1, 2) और (-3, 0) द्वारा बनने वाले चतुर्भुज का प्रकार बताइए।",
        "સ્વાધ્યાય 7.1 (Q6.i): બિંદુઓ (-1, -2), (1, 0), (-1, 2) અને (-3, 0) દ્વારા રચાતા ચતુષ્કોણનો પ્રકાર જણાવો.",
        [
            "Square",
            "Rhombus (not a square)",
            "Parallelogram",
            "Rectangle (not a square)"
        ],
        [
            "वर्ग",
            "समचतुर्भुज (वर्ग नहीं)",
            "समांतर चतुर्भुज",
            "आयत (वर्ग नहीं)"
        ],
        [
            "ચોરસ",
            "સમબાજુ ચતુષ્કોણ (ચોરસ નથી)",
            "સમાંતરબાજુ ચતુષ્કોણ",
            "લંબચોરસ (ચોરસ નથી)"
        ],
        0,
        "Let A(-1, -2), B(1, 0), C(-1, 2), D(-3, 0).\nAB = √(2² + 2²) = √8 = 2√2\nBC = √((-2)² + 2²) = √8 = 2√2\nCD = √((-2)² + (-2)²) = √8 = 2√2\nDA = √(2² + (-2)²) = √8 = 2√2\nAll 4 sides are equal (2√2).\nDiagonals: AC = √((-1 - (-1))² + (2 - (-2))²) = √(0 + 16) = 4\nBD = √((-3 - 1)² + (0 - 0)²) = √(16 + 0) = 4\nBoth diagonals are equal (4). Since all four sides and both diagonals are equal, ABCD is a Square!",
        "माना A(-1, -2), B(1, 0), C(-1, 2), D(-3, 0).\nAB = BC = CD = DA = √8 = 2√2 (चारों भुजाएँ बराबर हैं)\nविकर्ण: AC = √16 = 4, BD = √16 = 4 (दोनों विकर्ण बराबर हैं)\nचारों भुजाएँ और दोनों विकर्ण बराबर होने के कारण, यह एक वर्ग है!",
        "ધારો કે A(-1, -2), B(1, 0), C(-1, 2), D(-3, 0).\nAB = BC = CD = DA = √8 = 2√2 (ચારેય બાજુઓ સમાન છે)\nવિકર્ણો: AC = 4, BD = 4 (બંને વિકર્ણો સમાન છે)\nચારેય બાજુઓ અને બંને વિકર્ણો સમાન હોવાથી, તે ચોરસ છે!",
        bloom="Apply",
        diff="Intermediate",
        mins=2
    ))

    # 17. Exercise 7.1 Q6(ii)
    blocks.append(make_quiz(
        "C10M_CH7_EX7.1_Q6_p2",
        "Exercise 7.1 (Q6.ii): Name the type of quadrilateral formed by the points (-3, 5), (3, 1), (0, 3) and (-1, -4).",
        "प्रश्नावली 7.1 (Q6.ii): बिंदुओं (-3, 5), (3, 1), (0, 3) और (-1, -4) द्वारा बनने वाले चतुर्भुज का प्रकार बताइए।",
        "સ્વાધ્યાય 7.1 (Q6.ii): બિંદુઓ (-3, 5), (3, 1), (0, 3) અને (-1, -4) દ્વારા રચાતા ચતુષ્કોણનો પ્રકાર જણાવો.",
        [
            "No quadrilateral is formed (three of the points are collinear)",
            "Trapezium",
            "Parallelogram",
            "Kite"
        ],
        [
            "कोई चतुर्भुज नहीं बनता (तीन बिंदु संरेखी हैं)",
            "समलंब चतुर्भुज",
            "समांतर चतुर्भुज",
            "पतंगाकार चतुर्भुज"
        ],
        [
            "કોઈ ચતુષ્કોણ બનતો નથી (ત્રણ બિંદુઓ સમરેખ છે)",
            "સમલંબ ચતુષ્કોણ",
            "સમાંતરબાજુ ચતુષ્કોણ",
            "પતંગાકાર ચતુષ્કોણ"
        ],
        0,
        "Let A(-3, 5), B(3, 1), C(0, 3), D(-1, -4).\nDistance between A(-3, 5) and C(0, 3): AC = √((0 - (-3))² + (3 - 5)²) = √(9 + 4) = √13\nDistance between C(0, 3) and B(3, 1): CB = √((3 - 0)² + (1 - 3)²) = √(9 + 4) = √13\nDistance between A(-3, 5) and B(3, 1): AB = √((3 - (-3))² + (1 - 5)²) = √(36 + 16) = √52 = 2√13\nNotice that AC + CB = √13 + √13 = 2√13 = AB! Points A, C, and B lie on the exact same straight line (collinear). A straight line cannot form a quadrilateral, so NO quadrilateral is formed!",
        "माना A(-3, 5), B(3, 1), C(0, 3), D(-1, -4).\nAC = √((0+3)² + (3-5)²) = √13\nCB = √((3-0)² + (1-3)²) = √13\nAB = √((3+3)² + (1-5)²) = √52 = 2√13\nयहाँ AC + CB = √13 + √13 = 2√13 = AB है! अतः बिंदु A, C और B एक ही सीधी रेखा पर स्थित हैं (संरेखी हैं)। तीन संरेखी बिंदुओं से चतुर्भुज नहीं बन सकता, इसलिए कोई चतुर्भुज नहीं बनता!",
        "ધારો કે A(-3, 5), B(3, 1), C(0, 3), D(-1, -4).\nAC = √13, CB = √13, AB = √52 = 2√13\nઅહીં AC + CB = √13 + √13 = 2√13 = AB થાય છે! એટલે કે બિંદુઓ A, C અને B સમરેખ છે. એક જ રેખા પર ત્રણ બિંદુઓ હોવાથી ચતુષ્કોણ રચી શકાય નહીં, તેથી કોઈ ચતુષ્કોણ બનતો નથી!",
        bloom="Analyze",
        diff="Intermediate",
        mins=3
    ))

    # 18. Exercise 7.1 Q6(iii)
    blocks.append(make_quiz(
        "C10M_CH7_EX7.1_Q6_p3",
        "Exercise 7.1 (Q6.iii): Name the type of quadrilateral formed by the points (4, 5), (7, 6), (4, 3) and (1, 2).",
        "प्रश्नावली 7.1 (Q6.iii): बिंदुओं (4, 5), (7, 6), (4, 3) और (1, 2) द्वारा बनने वाले चतुर्भुज का प्रकार बताइए।",
        "સ્વાધ્યાય 7.1 (Q6.iii): બિંદુઓ (4, 5), (7, 6), (4, 3) અને (1, 2) દ્વારા રચાતા ચતુષ્કોણનો પ્રકાર જણાવો.",
        [
            "Parallelogram (opposite sides equal, diagonals unequal)",
            "Rectangle (opposite sides and diagonals equal)",
            "Rhombus",
            "Square"
        ],
        [
            "समांतर चतुर्भुज (सम्मुख भुजाएँ बराबर, विकर्ण असमान)",
            "आयत (सम्मुख भुजाएँ और विकर्ण बराबर)",
            "समचतुर्भुज",
            "वर्ग"
        ],
        [
            "સમાંતરબાજુ ચતુષ્કોણ (સામસામેની બાજુઓ સમાન, વિકર્ણો અસમાન)",
            "લંબચોરસ (સામસામેની બાજુઓ અને વિકર્ણો સમાન)",
            "સમબાજુ ચતુષ્કોણ",
            "ચોરસ"
        ],
        0,
        "Let A(4, 5), B(7, 6), C(4, 3), D(1, 2).\nAB = √((7-4)² + (6-5)²) = √(9 + 1) = √10\nBC = √((4-7)² + (3-6)²) = √(9 + 9) = √18 = 3√2\nCD = √((1-4)² + (2-3)²) = √(9 + 1) = √10\nDA = √((4-1)² + (5-2)²) = √(9 + 9) = √18 = 3√2\nOpposite sides are equal: AB = CD = √10 and BC = DA = √18.\nDiagonals: AC = √((4-4)² + (3-5)²) = √4 = 2, BD = √((1-7)² + (2-6)²) = √(36 + 16) = √52 = 2√13.\nSince opposite sides are equal but diagonals are unequal (2 ≠ 2√13), ABCD is a Parallelogram!",
        "माना A(4, 5), B(7, 6), C(4, 3), D(1, 2).\nAB = CD = √10 तथा BC = DA = √18 (सम्मुख भुजाएँ बराबर हैं)\nविकर्ण: AC = 2 और BD = √52 = 2√13 (विकर्ण असमान हैं)\nचूँकि सम्मुख भुजाएँ बराबर हैं लेकिन विकर्ण असमान हैं, अतः यह एक समांतर चतुर्भुज है!",
        "ધારો કે A(4, 5), B(7, 6), C(4, 3), D(1, 2).\nAB = CD = √10 અને BC = DA = √18 (સામસામેની બાજુઓ સમાન છે)\nવિકર્ણો: AC = 2 અને BD = √52 = 2√13 (વિકર્ણો અસમાન છે)\nસામસામેની બાજુઓ સમાન પરંતુ વિકર્ણો અસમાન હોવાથી, તે સમાંતરબાજુ ચતુષ્કોણ છે!",
        bloom="Apply",
        diff="Intermediate",
        mins=2
    ))

    # 19. Exercise 7.1 Q7
    blocks.append(make_quiz(
        "C10M_CH7_EX7.1_Q7",
        "Exercise 7.1 (Q7): Find the point on the x-axis which is equidistant from (2, -5) and (-2, 9).",
        "प्रश्नावली 7.1 (Q7): x-अक्ष पर वह बिंदु ज्ञात कीजिए जो (2, -5) और (-2, 9) से समदूरस्थ है।",
        "સ્વાધ્યાય 7.1 (Q7): x-અક્ષ પરનું એવું બિંદુ શોધો જે (2, -5) અને (-2, 9) થી સમાન અંતરે હોય.",
        ["(-7, 0)", "(7, 0)", "(0, -7)", "(-5, 0)"],
        ["(-7, 0)", "(7, 0)", "(0, -7)", "(-5, 0)"],
        ["(-7, 0)", "(7, 0)", "(0, -7)", "(-5, 0)"],
        0,
        "Any point on the x-axis has y-coordinate 0, so let P = (x, 0). Let A = (2, -5) and B = (-2, 9).\nGiven PA² = PB²:\n(x - 2)² + (0 - (-5))² = (x - (-2))² + (0 - 9)²\n(x - 2)² + 25 = (x + 2)² + 81\nx² - 4x + 4 + 25 = x² + 4x + 4 + 81\n-4x + 29 = 4x + 85\n-8x = 85 - 29 = 56 ⇒ x = -7.\nTherefore, the required point on the x-axis is (-7, 0).",
        "x-अक्ष पर किसी भी बिंदु का y-निर्देशांक 0 होता है, अतः माना P(x, 0) है। A(2, -5) और B(-2, 9)।\nPA² = PB²:\n(x - 2)² + 25 = (x + 2)² + 81\nx² - 4x + 29 = x² + 4x + 85\n-8x = 56 ⇒ x = -7.\nअतः x-अक्ष पर अभीष्ट बिंदु (-7, 0) है।",
        "x-અક્ષ પરના કોઈપણ બિંદુનો y-યામ 0 હોય છે, તેથી ધારો કે P(x, 0) છે. A(2, -5) અને B(-2, 9).\nPA² = PB²:\n(x - 2)² + 25 = (x + 2)² + 81\nx² - 4x + 29 = x² + 4x + 85\n-8x = 56 ⇒ x = -7.\nઆમ, x-અક્ષ પરનું માંગેલ બિંદુ (-7, 0) છે.",
        bloom="Apply",
        diff="Intermediate",
        mins=2
    ))

    # 20. Exercise 7.1 Q8
    blocks.append(make_quiz(
        "C10M_CH7_EX7.1_Q8",
        "Exercise 7.1 (Q8): Find the values of y for which the distance between the points P(2, -3) and Q(10, y) is 10 units.",
        "प्रश्नावली 7.1 (Q8): y का वह मान ज्ञात कीजिए जिसके लिए बिंदु P(2, -3) और Q(10, y) के बीच की दूरी 10 मात्रक है।",
        "સ્વાધ્યાય 7.1 (Q8): બિંદુઓ P(2, -3) અને Q(10, y) વચ્ચેનું અંતર 10 એકમ હોય, તો y નું મૂલ્ય શોધો.",
        ["y = 3 or y = -9", "y = -3 or y = 9", "y = 6 or y = -6", "y = 5 or y = -7"],
        ["y = 3 या y = -9", "y = -3 या y = 9", "y = 6 या y = -6", "y = 5 या y = -7"],
        ["y = 3 અથવા y = -9", "y = -3 અથવા y = 9", "y = 6 અથવા y = -6", "y = 5 અથવા y = -7"],
        0,
        "Using distance formula: PQ = 10 ⇒ PQ² = 100\n(10 - 2)² + (y - (-3))² = 100\n8² + (y + 3)² = 100\n64 + (y + 3)² = 100 ⇒ (y + 3)² = 36\nTaking square root: y + 3 = ±6\nIf y + 3 = 6 ⇒ y = 3\nIf y + 3 = -6 ⇒ y = -9\nThus, y = 3 or y = -9.",
        "दूरी सूत्र द्वारा: PQ = 10 ⇒ PQ² = 100\n(10 - 2)² + (y + 3)² = 100\n64 + (y + 3)² = 100 ⇒ (y + 3)² = 36\nवर्गमूल लेने पर: y + 3 = ±6\nयदि y + 3 = 6 ⇒ y = 3\nयदि y + 3 = -6 ⇒ y = -9\nअतः y = 3 या y = -9।",
        "અંતર સૂત્ર મુજબ: PQ = 10 ⇒ PQ² = 100\n(10 - 2)² + (y + 3)² = 100\n64 + (y + 3)² = 100 ⇒ (y + 3)² = 36\nવર્ગમૂળ લેતાં: y + 3 = ±6\nજો y + 3 = 6 ⇒ y = 3\nજો y + 3 = -6 ⇒ y = -9\nઆમ, y = 3 અથવા y = -9.",
        bloom="Apply",
        diff="Intermediate",
        mins=2
    ))

    # 21. Exercise 7.1 Q9
    blocks.append(make_quiz(
        "C10M_CH7_EX7.1_Q9",
        "Exercise 7.1 (Q9): If Q(0, 1) is equidistant from P(5, -3) and R(x, 6), find the values of x. Also find the distance QR.",
        "प्रश्नावली 7.1 (Q9): यदि Q(0, 1) बिंदुओं P(5, -3) और R(x, 6) से समदूरस्थ है, तो x के मान ज्ञात कीजिए। साथ ही दूरी QR भी ज्ञात कीजिए।",
        "સ્વાધ્યાય 7.1 (Q9): જો Q(0, 1) એ P(5, -3) અને R(x, 6) થી સમાન અંતરે હોય, તો x ના મૂલ્યો શોધો. વળી અંતર QR પણ શોધો.",
        [
            "x = ±4; QR = √41",
            "x = ±5; QR = √50",
            "x = 4 only; QR = 41",
            "x = ±2; QR = √29"
        ],
        [
            "x = ±4; QR = √41",
            "x = ±5; QR = √50",
            "केवल x = 4; QR = 41",
            "x = ±2; QR = √29"
        ],
        [
            "x = ±4; QR = √41",
            "x = ±5; QR = √50",
            "માત્ર x = 4; QR = 41",
            "x = ±2; QR = √29"
        ],
        0,
        "QP² = QR² ⇒ (5 - 0)² + (-3 - 1)² = (x - 0)² + (6 - 1)²\n25 + 16 = x² + 25 ⇒ x² = 16 ⇒ x = ±4.\nFor QR: QR = √((±4 - 0)² + (6 - 1)²) = √(16 + 25) = √41.\nWhen x = 4, PR = √((4-5)² + (6-(-3))²) = √(1 + 81) = √82.\nWhen x = -4, PR = √((-4-5)² + (6-(-3))²) = √(81 + 81) = 9√2.",
        "QP² = QR² ⇒ (5 - 0)² + (-3 - 1)² = (x - 0)² + (6 - 1)²\n25 + 16 = x² + 25 ⇒ x² = 16 ⇒ x = ±4।\nQR के लिए: QR = √(16 + 25) = √41।\nजब x = 4, तो PR = √82; और जब x = -4, तो PR = 9√2।",
        "QP² = QR² ⇒ (5 - 0)² + (-3 - 1)² = (x - 0)² + (6 - 1)²\n25 + 16 = x² + 25 ⇒ x² = 16 ⇒ x = ±4.\nQR માટે: QR = √(16 + 25) = √41.\nજ્યારે x = 4 હોય ત્યારે PR = √82 અને x = -4 હોય ત્યારે PR = 9√2.",
        bloom="Apply",
        diff="Intermediate",
        mins=2
    ))

    # 22. Exercise 7.1 Q10
    blocks.append(make_quiz(
        "C10M_CH7_EX7.1_Q10",
        "Exercise 7.1 (Q10): Find a relation between x and y such that the point (x, y) is equidistant from the point (3, 6) and (-3, 4).",
        "प्रश्नावली 7.1 (Q10): x और y में एक ऐसा संबंध ज्ञात कीजिए कि बिंदु (x, y) बिंदु (3, 6) और (-3, 4) से समदूरस्थ हो।",
        "સ્વાધ્યાય 7.1 (Q10): x અને y વચ્ચેનો એવો સંબંધ મેળવો કે જેથી બિંદુ (x, y) એ બિંદુઓ (3, 6) અને (-3, 4) થી સમાન અંતરે હોય.",
        [
            "3x + y - 5 = 0",
            "3x - y + 5 = 0",
            "x + 3y - 5 = 0",
            "3x + y + 5 = 0"
        ],
        [
            "3x + y - 5 = 0",
            "3x - y + 5 = 0",
            "x + 3y - 5 = 0",
            "3x + y + 5 = 0"
        ],
        [
            "3x + y - 5 = 0",
            "3x - y + 5 = 0",
            "x + 3y - 5 = 0",
            "3x + y + 5 = 0"
        ],
        0,
        "Let P(x, y), A(3, 6), B(-3, 4). Given PA² = PB²:\n(x - 3)² + (y - 6)² = (x - (-3))² + (y - 4)²\nx² - 6x + 9 + y² - 12y + 36 = x² + 6x + 9 + y² - 8y + 16\n-6x - 12y + 45 = 6x - 8y + 25\n-6x - 6x - 12y + 8y + 45 - 25 = 0\n-12x - 4y + 20 = 0\nDividing throughout by -4 gives: 3x + y - 5 = 0.",
        "माना P(x, y), A(3, 6) और B(-3, 4)। दिया है PA² = PB²:\n(x - 3)² + (y - 6)² = (x + 3)² + (y - 4)²\nx² - 6x + 9 + y² - 12y + 36 = x² + 6x + 9 + y² - 8y + 16\n-6x - 12y + 45 = 6x - 8y + 25\n-12x - 4y + 20 = 0\n-4 से भाग देने पर: 3x + y - 5 = 0 प्राप्त होता है।",
        "ધારો કે P(x, y), A(3, 6) અને B(-3, 4). આપેલ છે PA² = PB²:\n(x - 3)² + (y - 6)² = (x + 3)² + (y - 4)²\nx² - 6x + 9 + y² - 12y + 36 = x² + 6x + 9 + y² - 8y + 16\n-6x - 12y + 45 = 6x - 8y + 25\n-12x - 4y + 20 = 0\n-4 વડે ભાગતાં: 3x + y - 5 = 0 મળે છે.",
        bloom="Apply",
        diff="Intermediate",
        mins=2
    ))

    return blocks

# =========================================================================
# PART 2: SECTION FORMULA, MID-POINT FORMULA & EXERCISE 7.2
# =========================================================================
def get_part2_blocks():
    blocks = []

    # 23. Section Formula Hook
    blocks.append(make_theory(
        "C10M_CH7_7",
        "The Lever Principle & The Rendezvous Point",
        "उत्तोलक का सिद्धांत और मिलन स्थल",
        "ઉચ્ચાલનનો સિદ્ધાંત અને મિલન બિંદુ",
        "Suppose two friends, Aarav and Diya, live in different parts of a city connected by a straight highway. They want to meet at a cafe located on that highway.\n- If they decide to meet exactly halfway, finding the spot is simple: just take the average of their coordinates!\n- But what if Aarav is riding a bicycle at 10 km/h and Diya is walking at 5 km/h? To arrive at the exact same time, Aarav must cover twice the distance of Diya! The meeting point must divide the route in the ratio **2 : 1**.\n\nIn mathematics, finding the exact coordinates of a point that cuts a segment into any ratio $m_1 : m_2$ is accomplished by the powerful **Section Formula (विभाजन सूत्र / વિભાજન સૂત્ર)**!",
        "मान लीजिए दो मित्र, आरव और दीया, एक सीधे राजमार्ग द्वारा जुड़े एक शहर के विभिन्न हिस्सों में रहते हैं। वे उस राजमार्ग पर स्थित एक कैफे में मिलना चाहते हैं।\n- यदि वे ठीक बीच में मिलने का निर्णय लेते हैं, तो स्थान खोजना बहुत आसान है: बस उनके निर्देशांकों का औसत निकाल लें!\n- लेकिन क्या होगा यदि आरव 10 किमी/घंटा की गति से साइकिल चला रहा है और दीया 5 किमी/घंटा की गति से चल रही है? एक ही समय पर पहुँचने के लिए, आरव को दीया की तुलना में दोगुनी दूरी तय करनी होगी! मिलन स्थल को रास्ते को **2 : 1** के अनुपात में विभाजित करना होगा।\n\nगणित में, किसी रेखाखंड को किसी भी अनुपात $m_1 : m_2$ में विभाजित करने वाले बिंदु के सटीक निर्देशांक ज्ञात करने का कार्य शक्तिशाली **विभाजन सूत्र** द्वारा किया जाता है!",
        "ધારો કે બે મિત્રો, આરવ અને દિયા, સીધા હાઇવેથી જોડાયેલા શહેરના બે અલગ અલગ વિસ્તારોમાં રહે છે. તેઓ હાઇવે પર આવેલા એક કાફેમાં મળવા માંગે છે.\n- જો તેઓ બરાબર વચ્ચે મળવાનું નક્કી કરે, તો તે સ્થળ શોધવું સરળ છે: ફક્ત તેમના યામોની સરેરાશ લો!\n- પરંતુ જો આરવ 10 કિમી/કલાકની ઝડપે સાયકલ ચલાવે છે અને દિયા 5 કિમી/કલાકની ઝડપે ચાલે છે, તો એક જ સમયે પહોંચવા માટે આરવે દિયા કરતાં બમણું અંતર કાપવું પડે! મિલન સ્થળે રસ્તાનું **2 : 1** ના ગુણોત્તરમાં વિભાજન કરવું પડશે.\n\nગણિતમાં, રેખાખંડનું કોઈપણ ગુણોત્તર $m_1 : m_2$ માં વિભાજન કરતા બિંદુના ચોક્કસ યામ મેળવવા માટે શક્તિશાળી **વિભાજન સૂત્ર** નો ઉપયોગ થાય છે!",
        btype="hook",
        bloom="Understand",
        diff="Beginner",
        mins=3
    ))

    # 24. Socratic Question (Midpoint)
    blocks.append(make_socratic(
        "C10M_CH7_8",
        "If a line segment connects A(2, 4) to B(6, 10), what are the coordinates of the exact halfway point (midpoint)?",
        "यदि कोई रेखाखंड A(2, 4) को B(6, 10) से जोड़ता है, तो बिल्कुल मध्य-बिंदु के निर्देशांक क्या होंगे?",
        "જો કોઈ રેખાખંડ A(2, 4) અને B(6, 10) ને જોડતો હોય, તો તેના મધ્યબિંદુના યામ શું થશે?",
        ["(4, 7)", "(3, 5)", "(8, 14)", "(4, 6)"],
        ["(4, 7)", "(3, 5)", "(8, 14)", "(4, 6)"],
        ["(4, 7)", "(3, 5)", "(8, 14)", "(4, 6)"],
        0,
        "The midpoint is simply the arithmetic mean (average) of the coordinates: x = (2 + 6)/2 = 8/2 = 4, and y = (4 + 10)/2 = 14/2 = 7. The midpoint is (4, 7)!",
        "मध्य-बिंदु निर्देशांकों का समांतर माध्य (औसत) होता है: x = (2 + 6)/2 = 4, और y = (4 + 10)/2 = 7। अतः मध्य-बिંદુ (4, 7) है!",
        "મધ્યબિંદુ એ યામોની સરેરાશ હોય છે: x = (2 + 6)/2 = 4, અને y = (4 + 10)/2 = 7. આમ મધ્યબિંદુ (4, 7) છે!",
        bloom="Apply",
        diff="Beginner",
        mins=2
    ))

    # 25. Discovery: Deriving the Section Formula
    blocks.append(make_theory(
        "C10M_CH7_9",
        "Discovery: Deriving the Section Formula using Similar Triangles",
        "खोज: समरूप त्रिभुजों द्वारा विभाजन सूत्र का निगमन",
        "શોધ: સમરૂપ ત્રિકોણની મદદથી વિભાજન સૂત્ર તારવવું",
        "Let $P(x, y)$ divide the line segment joining $A(x_1, y_1)$ and $B(x_2, y_2)$ internally in the ratio $m_1 : m_2$ (i.e. $\\frac{AP}{PB} = \\frac{m_1}{m_2}$).\n\n1. Drop perpendiculars from $A, P, B$ to the x-axis meeting at $R, S, T$.\n2. Draw horizontal lines $AQ \\perp PS$ and $PC \\perp BT$.\n3. Notice that $\\triangle PAQ$ and $\\triangle BPC$ are right-angled triangles and their corresponding angles are equal (corresponding angles of parallel lines). Thus, by **AA Similarity Criterion**:\n$$\\triangle PAQ \\sim \\triangle BPC$$\n\n4. Therefore, the ratio of corresponding sides is equal:\n$$\\frac{PA}{BP} = \\frac{AQ}{PC} = \\frac{PQ}{BC}$$\n$$\\frac{m_1}{m_2} = \\frac{x - x_1}{x_2 - x}$$\n\nCross-multiplying gives: $m_1(x_2 - x) = m_2(x - x_1) \\implies m_1 x_2 - m_1 x = m_2 x - m_2 x_1$\n$$(m_1 + m_2)x = m_1 x_2 + m_2 x_1 \\implies x = \\frac{m_1 x_2 + m_2 x_1}{m_1 + m_2}$$\n\nApplying the exact same reasoning to the vertical sides yields:\n$$y = \\frac{m_1 y_2 + m_2 y_1}{m_1 + m_2}$$",
        "माना $P(x, y)$ बिंदुओं $A(x_1, y_1)$ और $B(x_2, y_2)$ को मिलाने वाले रेखाखंड को आंतरिक रूप से $m_1 : m_2$ के अनुपात में विभाजित करता है (अर्थात $\\frac{AP}{PB} = \\frac{m_1}{m_2}$)।\n\n1. $A, P, B$ से x-अक्ष पर लंब खींचें जो $R, S, T$ पर मिलते हैं।\n2. क्षैतिज रेखाएँ $AQ \\perp PS$ और $PC \\perp BT$ खींचें।\n3. ध्यान दें कि $\\triangle PAQ$ और $\\triangle BPC$ समकोण त्रिभुज हैं और उनके संगत कोण बराबर हैं। अतः **AA समरूपता कसौटी** द्वारा:\n$$\\triangle PAQ \\sim \\triangle BPC$$\n\n4. इसलिए संगत भुजाओं का अनुपात समान होगा:\n$$\\frac{m_1}{m_2} = \\frac{x - x_1}{x_2 - x}$$\n\nवज्र-गुणन करने पर: $m_1(x_2 - x) = m_2(x - x_1) \\implies (m_1 + m_2)x = m_1 x_2 + m_2 x_1$\n$$x = \\frac{m_1 x_2 + m_2 x_1}{m_1 + m_2}$$\n\nइसी प्रकार y-निर्देशांक के लिए प्राप्त होता है:\n$$y = \\frac{m_1 y_2 + m_2 y_1}{m_1 + m_2}$$",
        "ધારો કે બિંદુ $P(x, y)$ એ $A(x_1, y_1)$ અને $B(x_2, y_2)$ ને જોડતા રેખાખંડનું અંદરથી $m_1 : m_2$ ગુણોત્તરમાં વિભાજન કરે છે (એટલે કે $\\frac{AP}{PB} = \\frac{m_1}{m_2}$).\n\n1. $A, P, B$ માંથી x-અક્ષ પર લંબ દોરો જે અનુક્રમે $R, S, T$ આગળ મળે છે.\n2. ક્ષિતિજ રેખાઓ $AQ \\perp PS$ અને $PC \\perp BT$ દોરો.\n3. $\\triangle PAQ$ અને $\\triangle BPC$ કાટકોણ ત્રિકોણ છે અને તેમના અનુરૂપ ખૂણા સમાન છે. આથી **AA સમરૂપતા શરત** મુજબ:\n$$\\triangle PAQ \\sim \\triangle BPC$$\n\n4. તેથી અનુરૂપ બાજુઓનો ગુણોત્તર સમાન થાય:\n$$\\frac{m_1}{m_2} = \\frac{x - x_1}{x_2 - x}$$\n\nચોકડી ગુણાકાર કરતાં: $m_1(x_2 - x) = m_2(x - x_1) \\implies (m_1 + m_2)x = m_1 x_2 + m_2 x_1$\n$$x = \\frac{m_1 x_2 + m_2 x_1}{m_1 + m_2}$$\n\nતે જ રીતે y-યામ માટે:\n$$y = \\frac{m_1 y_2 + m_2 y_1}{m_1 + m_2}$$",
        btype="discovery",
        bloom="Analyze",
        diff="Intermediate",
        mins=3
    ))

    # 26. Reveal / Theory: The Section Formula & Special Cases
    blocks.append(make_theory(
        "C10M_CH7_10",
        "The Section Formula & Its 3 Golden Forms",
        "विभाजन सूत्र और इसके 3 स्वर्णिम रूप",
        "વિભાજન સૂત્ર અને તેના 3 સુવર્ણ સ્વરૂપો",
        "### 1. General Section Formula (Internal Division)\nThe coordinates of point $P(x, y)$ dividing the segment $AB$ joining $A(x_1, y_1)$ and $B(x_2, y_2)$ in the ratio $m_1 : m_2$ are:\n$$P(x, y) = \\left( \\frac{m_1 x_2 + m_2 x_1}{m_1 + m_2}, \\frac{m_1 y_2 + m_2 y_1}{m_1 + m_2} \\right)$$\n\n### 2. The Mid-point Formula ($m_1 : m_2 = 1 : 1$)\nWhen $P$ bisects $AB$ exactly in the middle:\n$$M(x, y) = \\left( \\frac{x_1 + x_2}{2}, \\frac{y_1 + y_2}{2} \\right)$$\n\n### 3. The Ratio $k : 1$ Method (For finding unknown ratios)\nWhenever you need to determine an unknown ratio, assume the ratio to be $k : 1$. Then:\n$$P(x, y) = \\left( \\frac{k x_2 + x_1}{k + 1}, \\frac{k y_2 + y_1}{k + 1} \\right)$$\nThis reduces two unknowns ($m_1, m_2$) to a single variable ($k$), making calculations 50% faster!\n\n### 4. Trisection of a Line Segment\nTrisection means dividing a line segment into **3 equal parts** ($AP = PQ = QB$):\n- Point $P$ divides $AB$ in the ratio **1 : 2**\n- Point $Q$ divides $AB$ in the ratio **2 : 1** (or $Q$ is simply the midpoint of $PB$!)",
        "### 1. व्यापक विभाजन सूत्र (अंतः विभाजन)\nबिंदुओं $A(x_1, y_1)$ और $B(x_2, y_2)$ को मिलाने वाले रेखाखंड को $m_1 : m_2$ के अनुपात में विभाजित करने वाले बिंदु $P(x, y)$ के निर्देशांक:\n$$P(x, y) = \\left( \\frac{m_1 x_2 + m_2 x_1}{m_1 + m_2}, \\frac{m_1 y_2 + m_2 y_1}{m_1 + m_2} \\right)$$\n\n### 2. मध्य-बिंदु सूत्र ($m_1 : m_2 = 1 : 1$)\nजब $P$ रेखाखंड $AB$ को ठीक बीच में समद्वિभाजित करता है:\n$$M(x, y) = \\left( \\frac{x_1 + x_2}{2}, \\frac{y_1 + y_2}{2} \\right)$$\n\n### 3. अनुपात $k : 1$ विधि (अज्ञात अनुपात ज्ञात करने हेतु)\nजब भी अनुपात ज्ञात करना हो, तो अनुपात को $k : 1$ मान लें। तब:\n$$P(x, y) = \\left( \\frac{k x_2 + x_1}{k + 1}, \\frac{k y_2 + y_1}{k + 1} \\right)$$\nयह दो चरों ($m_1, m_2$) को एक ही चर ($k$) में बदल देता है, जिससे गणना बहुत आसान हो जाती है!\n\n### 4. रेखाखंड का समत्रिभाजन\nसमत्रिभाजन का अर्थ है रेखाखंड को **3 बराबर भागों** में बाँटना ($AP = PQ = QB$):\n- बिंदु $P$, रेखाखंड $AB$ को **1 : 2** के अनुपात में विभाजित करता है।\n- बिंदु $Q$, रेखाखंड $AB$ को **2 : 1** के अनुपात में विभाजित करता है (या $Q$, $PB$ का मध्य-बिंदु है!)।",
        "### 1. વ્યાપક વિભાજન સૂત્ર (અંતઃવિભાજન)\n$A(x_1, y_1)$ અને $B(x_2, y_2)$ ને જોડતા રેખાખંડનું $m_1 : m_2$ ગુણોત્તરમાં વિભાજન કરતા બિંદુ $P(x, y)$ ના યામ:\n$$P(x, y) = \\left( \\frac{m_1 x_2 + m_2 x_1}{m_1 + m_2}, \\frac{m_1 y_2 + m_2 y_1}{m_1 + m_2} \\right)$$\n\n### 2. મધ્યબિંદુ સૂત્ર ($m_1 : m_2 = 1 : 1$)\nજ્યારે $P$ એ રેખાખંડ $AB$ નું બરાબર મધ્યમાં વિભાજન કરે:\n$$M(x, y) = \\left( \\frac{x_1 + x_2}{2}, \\frac{y_1 + y_2}{2} \\right)$$\n\n### 3. ગુણોત્તર $k : 1$ ની રીત (અજ્ઞાત ગુણોત્તર શોધવા માટે)\nજ્યારે પણ ગુણોત્તર શોધવાનો હોય, ત્યારે ગુણોત્તર $k : 1$ ધારી લેવો:\n$$P(x, y) = \\left( \\frac{k x_2 + x_1}{k + 1}, \\frac{k y_2 + y_1}{k + 1} \\right)$$\nઆ રીતથી ગણતરી ઘણી ઝડપી અને સરળ બને છે!\n\n### 4. રેખાખંડનું ત્રિભાગીકરણ\nરેખાખંડના **3 સમાન ભાગ** કરવા ($AP = PQ = QB$):\n- બિંદુ $P$ એ $AB$ નું **1 : 2** ના ગુણોત્તરમાં વિભાજન કરે છે.\n- બિંદુ $Q$ એ $AB$ નું **2 : 1** ના ગુણોત્તરમાં વિભાજન કરે છે (અથવા $Q$ એ $PB$ નું મધ્યબિંદુ છે!).",
        btype="theory",
        bloom="Remember",
        diff="Beginner",
        mins=3
    ))

    # 27. Teacher Tip: Cross-Multiplication & Axis Division Traps
    blocks.append(make_theory(
        "C10M_CH7_11",
        "Teacher Tip: The Cross-Pairing Rule & Coordinate Axis Shortcuts",
        "शिक्षक युक्ति: क्रॉस-गुणा का नियम और निर्देशांक अक्ष शॉर्टकट",
        "શિક્ષકની સલાહ: ચોકડી ગુણાકાર નિયમ અને યામાક્ષોના શોર્ટકટ",
        "**The Cross-Pairing Rule (Never pair $m_1$ with $x_1$!):**\nNotice the pattern in $\\frac{m_1 x_2 + m_2 x_1}{m_1 + m_2}$:\n- The left ratio $m_1$ multiplies the RIGHT coordinate $x_2$.\n- The right ratio $m_2$ multiplies the LEFT coordinate $x_1$.\nThey cross over like an 'X'! Pairing $m_1$ with $x_1$ is the #1 student error on board exams.\n\n**Division by the Axes Shortcuts:**\n- If a line segment is divided by the **x-axis**: Set the y-coordinate to zero ($y = 0$).\n- If a line segment is divided by the **y-axis**: Set the x-coordinate to zero ($x = 0$).\n\n**Parallelogram Diagonals Shortcut:**\nThe diagonals of a parallelogram always bisect each other! Therefore:\n$$\\text{Midpoint of diagonal } AC = \\text{Midpoint of diagonal } BD$$\nEquating their x and y coordinates gives you unknown vertices instantly, without any messy quadratic equations!",
        "**क्रॉस-गुणा का नियम ($m_1$ को कभी भी $x_1$ के साथ न जोड़ें!):**\n$\\frac{m_1 x_2 + m_2 x_1}{m_1 + m_2}$ के पैटर्न पर ध्यान दें:\n- बायाँ अनुपात $m_1$, दाएँ निर्देशांक $x_2$ से गुणा होता है।\n- दायाँ अनुपात $m_2$, बाएँ निर्देशांक $x_1$ से गुणा होता है।\nये 'X' की तरह क्रॉस होते हैं! बोर्ड परीक्षा में $m_1$ को $x_1$ से गुणा करना छात्रों की सबसे आम गलती है।\n\n**अक्षों द्वारा विभाजन का शॉर्टकट:**\n- यदि रेखाखंड **x-अक्ष** द्वारा विभाजित होता है: तो y-निर्देशांक को शून्य रखें ($y = 0$)।\n- यदि रेखाखंड **y-अक्ष** द्वारा विभाजित होता है: तो x-निर्देशांक को शून्य रखें ($x = 0$)।\n\n**समांतर चतुर्भुज विकर्ण शॉर्टकट:**\nसमांतर चतुर्भुज के विकर्ण परस्पर समद्विभाजित करते हैं! अतः:\n$$\\text{विकर्ण } AC \\text{ का मध्य-बिंदु} = \\text{विकर्ण } BD \\text{ का मध्य-बिंदु}$$\nदोनों के x और y निर्देशांकों की तुलना करने पर अज्ञात मान तुरंत मिल जाते हैं!",
        "**ચોકડી ગુણાકારનો નિયમ ($m_1$ ને ક્યારેય $x_1$ સાથે ન ગુણો!):**\n$\\frac{m_1 x_2 + m_2 x_1}{m_1 + m_2}$ નું સ્વરૂપ જુઓ:\n- ડાબી બાજુનો ગુણોત્તર $m_1$, જમણી બાજુના યામ $x_2$ સાથે ગુણાય છે.\n- જમણી બાજુનો ગુણોત્તર $m_2$, ડાબી બાજુના યામ $x_1$ સાથે ગુણાય છે.\nતેઓ 'X' ની જેમ ચોકડી બનાવે છે! બોર્ડ પરીક્ષામાં $m_1$ સાથે $x_1$ ગુણવાની ભૂલ ક્યારેય ન કરવી.\n\n**અક્ષો દ્વારા વિભાજનના શોર્ટકટ:**\n- જો રેખાખંડનું **x-અક્ષ** દ્વારા વિભાજન થતું હોય: તો y-યામ = 0 મૂકવો ($y = 0$).\n- જો રેખાખંડનું **y-અક્ષ** દ્વારા વિભાજન થતું હોય: તો x-યામ = 0 મૂકવો ($x = 0$).\n\n**સમાંતરબાજુ ચતુષ્કોણ શોર્ટકટ:**\nસમાંતરબાજુ ચતુષ્કોણના વિકર્ણો પરસ્પર દુભાગે છે! તેથી:\n$$\\text{વિકર્ણ } AC \\text{ નું મધ્યબિંદુ} = \\text{વિકર્ણ } BD \\text{ નું મધ્યબિંદુ}$$\nબંને બાજુના x અને y યામ સરખાવવાથી અજ્ઞાત મૂલ્યો સીધા જ મળી જાય છે!",
        btype="teacher_tip",
        bloom="Analyze",
        diff="Intermediate",
        mins=2
    ))

    # 28. NCERT Example 6
    blocks.append(make_quiz(
        "C10M_CH7_EG6",
        "NCERT Example 6: Find the coordinates of the point which divides the line segment joining the points (4, -3) and (8, 5) in the ratio 3 : 1 internally.",
        "NCERT उदाहरण 6: उस बिंदु के निर्देशांक ज्ञात कीजिए जो बिंदुओं (4, -3) और (8, 5) को जोड़ने वाले रेखाखंड को आंतरिक रूप से 3 : 1 के अनुपात में विभाजित करता है।",
        "NCERT ઉદાહરણ 6: બિંદુઓ (4, -3) અને (8, 5) ને જોડતા રેખાખંડનું 3 : 1 ના ગુણોત્તરમાં અંતઃવિભાજન કરતા બિંદુના યામ શોધો.",
        ["(7, 3)", "(6, 2)", "(7, 2)", "(5, 1)"],
        ["(7, 3)", "(6, 2)", "(7, 2)", "(5, 1)"],
        ["(7, 3)", "(6, 2)", "(7, 2)", "(5, 1)"],
        0,
        "Here x₁ = 4, y₁ = -3, x₂ = 8, y₂ = 5, m₁ = 3, m₂ = 1.\nx = (m₁x₂ + m₂x₁) / (m₁ + m₂) = (3(8) + 1(4)) / (3 + 1) = (24 + 4) / 4 = 28 / 4 = 7\ny = (m₁y₂ + m₂y₁) / (m₁ + m₂) = (3(5) + 1(-3)) / (3 + 1) = (15 - 3) / 4 = 12 / 4 = 3\nThus, the coordinates of the point of division are (7, 3).",
        "यहाँ x₁ = 4, y₁ = -3, x₂ = 8, y₂ = 5, m₁ = 3, m₂ = 1.\nx = (3(8) + 1(4)) / (3 + 1) = 28 / 4 = 7\ny = (3(5) + 1(-3)) / (3 + 1) = 12 / 4 = 3\nअतः विभाजन बिंदु के निर्देशांक (7, 3) हैं।",
        "અહીં x₁ = 4, y₁ = -3, x₂ = 8, y₂ = 5, m₁ = 3, m₂ = 1.\nx = (3(8) + 1(4)) / (3 + 1) = 28 / 4 = 7\ny = (3(5) + 1(-3)) / (3 + 1) = 12 / 4 = 3\nઆમ વિભાજન બિંદુના યામ (7, 3) છે.",
        bloom="Apply",
        diff="Beginner",
        mins=2
    ))

    # 29. NCERT Example 7
    blocks.append(make_quiz(
        "C10M_CH7_EG7",
        "NCERT Example 7: In what ratio does the point (-4, 6) divide the line segment joining the points A(-6, 10) and B(3, -8)?",
        "NCERT उदाहरण 7: बिंदु (-4, 6) बिंदुओं A(-6, 10) और B(3, -8) को जोड़ने वाले रेखाखंड को किस अनुपात में विभाजित करता है?",
        "NCERT ઉદાહરણ 7: બિંદુ (-4, 6) એ બિંદુઓ A(-6, 10) અને B(3, -8) ને જોડતા રેખાખંડનું કયા ગુણોત્તરમાં વિભાજન કરે છે?",
        ["2 : 7", "7 : 2", "3 : 5", "1 : 3"],
        ["2 : 7", "7 : 2", "3 : 5", "1 : 3"],
        ["2 : 7", "7 : 2", "3 : 5", "1 : 3"],
        0,
        "Let the ratio be k : 1. The x-coordinate of the dividing point is given by:\nx = (k(3) + 1(-6)) / (k + 1)\n-4 = (3k - 6) / (k + 1)\n-4(k + 1) = 3k - 6 ⇒ -4k - 4 = 3k - 6\n-4k - 3k = -6 + 4 ⇒ -7k = -2 ⇒ k = 2/7.\nHence, the required ratio is 2 : 7. (You can verify that y = (2(-8) + 7(10))/(2+7) = 54/9 = 6).",
        "माना अनुपात k : 1 है। विभाजन बिंदु का x-निर्देशांक:\n-4 = (3k - 6) / (k + 1)\n-4k - 4 = 3k - 6 ⇒ -7k = -2 ⇒ k = 2/7।\nअतः अभीष्ट अनुपात 2 : 7 है।",
        "ધારો કે ગુણોત્તર k : 1 છે. વિભાજન બિંદુનો x-યામ:\n-4 = (3k - 6) / (k + 1)\n-4k - 4 = 3k - 6 ⇒ -7k = -2 ⇒ k = 2/7.\nઆમ માંગેલ ગુણોત્તર 2 : 7 છે.",
        bloom="Apply",
        diff="Intermediate",
        mins=2
    ))

    # 30. Exercise 7.2 Q1
    blocks.append(make_quiz(
        "C10M_CH7_EX7.2_Q1",
        "Exercise 7.2 (Q1): Find the coordinates of the point which divides the join of (-1, 7) and (4, -3) in the ratio 2 : 3.",
        "प्रश्नावली 7.2 (Q1): उस बिंदु के निर्देशांक ज्ञात कीजिए जो बिंदुओं (-1, 7) और (4, -3) को मिलाने वाले रेखाखंड को 2 : 3 के अनुपात में विभाजित करता है।",
        "સ્વાધ્યાય 7.2 (Q1): બિંદુઓ (-1, 7) અને (4, -3) ને જોડતા રેખાખંડનું 2 : 3 ના ગુણોત્તરમાં વિભાજન કરતા બિંદુના યામ શોધો.",
        ["(1, 3)", "(3, 1)", "(2, 3)", "(-1, 3)"],
        ["(1, 3)", "(3, 1)", "(2, 3)", "(-1, 3)"],
        ["(1, 3)", "(3, 1)", "(2, 3)", "(-1, 3)"],
        0,
        "x₁ = -1, y₁ = 7, x₂ = 4, y₂ = -3, m₁ = 2, m₂ = 3.\nx = (m₁x₂ + m₂x₁) / (m₁ + m₂) = (2(4) + 3(-1)) / (2 + 3) = (8 - 3) / 5 = 5 / 5 = 1\ny = (m₁y₂ + m₂y₁) / (m₁ + m₂) = (2(-3) + 3(7)) / (2 + 3) = (-6 + 21) / 5 = 15 / 5 = 3\nThus, the coordinates are (1, 3).",
        "x = (2(4) + 3(-1)) / (2 + 3) = (8 - 3) / 5 = 5 / 5 = 1\ny = (2(-3) + 3(7)) / (2 + 3) = (-6 + 21) / 5 = 15 / 5 = 3\nअतः अभीष्ट निर्देशांक (1, 3) हैं।",
        "x = (2(4) + 3(-1)) / (2 + 3) = (8 - 3) / 5 = 5 / 5 = 1\ny = (2(-3) + 3(7)) / (2 + 3) = (-6 + 21) / 5 = 15 / 5 = 3\nઆમ માંગેલ યામ (1, 3) છે.",
        bloom="Apply",
        diff="Beginner",
        mins=2
    ))

    # 31. Exercise 7.2 Q2
    blocks.append(make_quiz(
        "C10M_CH7_EX7.2_Q2",
        "Exercise 7.2 (Q2): Find the coordinates of the points of trisection of the line segment joining (4, -1) and (-2, -3).",
        "प्रश्नावली 7.2 (Q2): बिंदुओं (4, -1) और (-2, -3) को जोड़ने वाले रेखाखंड को समत्रिभाजित करने वाले बिंदुओं के निर्देशांक ज्ञात कीजिए।",
        "સ્વાધ્યાય 7.2 (Q2): બિંદુઓ (4, -1) અને (-2, -3) ને જોડતા રેખાખંડના ત્રિભાગ બિંદુઓના યામ શોધો.",
        [
            "(2, -5/3) and (0, -7/3)",
            "(1, -2) and (0, -3)",
            "(2, -1) and (0, -2)",
            "(3, -2) and (-1, -3)"
        ],
        [
            "(2, -5/3) और (0, -7/3)",
            "(1, -2) और (0, -3)",
            "(2, -1) और (0, -2)",
            "(3, -2) और (-1, -3)"
        ],
        [
            "(2, -5/3) અને (0, -7/3)",
            "(1, -2) અને (0, -3)",
            "(2, -1) અને (0, -2)",
            "(3, -2) અને (-1, -3)"
        ],
        0,
        "Let A(4, -1) and B(-2, -3). The trisection points are P and Q.\nPoint P divides AB in ratio 1 : 2:\nx = (1(-2) + 2(4)) / 3 = (-2 + 8) / 3 = 6 / 3 = 2\ny = (1(-3) + 2(-1)) / 3 = (-3 - 2) / 3 = -5/3 ⇒ P(2, -5/3)\nPoint Q divides AB in ratio 2 : 1 (or midpoint of PB):\nx = (2(-2) + 1(4)) / 3 = (-4 + 4) / 3 = 0\ny = (2(-3) + 1(-1)) / 3 = (-6 - 1) / 3 = -7/3 ⇒ Q(0, -7/3)\nHence, the trisection points are (2, -5/3) and (0, -7/3).",
        "माना A(4, -1) और B(-2, -3)। समत्रिभाजन बिंदु P और Q हैं।\nबिंदु P, AB को 1 : 2 के अनुपात में विभाजित करता है:\nx = (1(-2) + 2(4)) / 3 = 6 / 3 = 2\ny = (1(-3) + 2(-1)) / 3 = -5/3 ⇒ P(2, -5/3)\nबिंदु Q, AB को 2 : 1 के अनुपात में विभाजित करता है:\nx = (2(-2) + 1(4)) / 3 = 0\ny = (2(-3) + 1(-1)) / 3 = -7/3 ⇒ Q(0, -7/3)\nअतः समत्रिभाजन बिंदु (2, -5/3) और (0, -7/3) हैं।",
        "ધારો કે A(4, -1) અને B(-2, -3). ત્રિભાગ બિંદુઓ P અને Q છે.\nP એ AB નું 1 : 2 માં વિભાજન કરે છે:\nx = (1(-2) + 2(4)) / 3 = 6 / 3 = 2\ny = (1(-3) + 2(-1)) / 3 = -5/3 ⇒ P(2, -5/3)\nQ એ AB નું 2 : 1 માં વિભાજન કરે છે:\nx = (2(-2) + 1(4)) / 3 = 0\ny = (2(-3) + 1(-1)) / 3 = -7/3 ⇒ Q(0, -7/3)\nઆમ ત્રિભાગ બિંદુઓ (2, -5/3) અને (0, -7/3) છે.",
        bloom="Apply",
        diff="Intermediate",
        mins=3
    ))

    # 32. Exercise 7.2 Q3
    blocks.append(make_quiz(
        "C10M_CH7_EX7.2_Q3",
        "Exercise 7.2 (Q3): On a Sports Day, 100 flower pots are placed at 1 m each along AD = 100 m. Niharika runs 1/4th of AD on the 2nd line and posts a green flag. Preet runs 1/5th of AD on the 8th line and posts a red flag. What is the distance between both flags, and where should Rashmi post a blue flag exactly halfway between them?",
        "प्रश्नावली 7.2 (Q3): खेल दिवस पर AD = 100 मीटर के अनुदिश 1-1 मीटर पर 100 गमले रखे हैं। निहारिका दूसरी पंक्ति में AD के 1/4 भाग के बराबर दौड़कर हरा झंडा गाड़ती है। प्रीत 8वीं पंक्ति में AD के 1/5 भाग के बराबर दौड़कर लाल झंडा गाड़ता है। दोनों झंडों के बीच की दूरी कितनी है, और रश्मि को दोनों के ठीक बीच में नीला झंडा कहाँ गाड़ना चाहिए?",
        "સ્વાધ્યાય 7.2 (Q3): રમતોત્સવમાં AD = 100 મીટર પર 1-1 મીટરે 100 કૂંડાં મુકેલા છે. નિહારિકા 2જી હરોળમાં AD ના 1/4 ભાગ જેટલું દોડી લીલો ધ્વજ રોપે છે. પ્રીત 8મી હરોળમાં AD ના 1/5 ભાગ જેટલું દોડી લાલ ધ્વજ રોપે છે. બંને ધ્વજ વચ્ચેનું અંતર કેટલું અને રશ્મિએ તેમની બરાબર મધ્યમાં વાદળી ધ્વજ ક્યાં રોપવો જોઈએ?",
        [
            "Distance = √61 m; Rashmi should post at (5, 22.5) on the 5th line at 22.5 m",
            "Distance = 61 m; Rashmi should post at (4, 25) on the 4th line",
            "Distance = √65 m; Rashmi should post at (5, 20) on the 5th line",
            "Distance = 5√2 m; Rashmi should post at (6, 22) on the 6th line"
        ],
        [
            "दूरी = √61 मीटर; रश्मि को 5वीं पंक्ति में 22.5 मीटर की दूरी पर (5, 22.5) पर झंडा गाड़ना चाहिए",
            "दूरी = 61 मीटर; रश्मि को 4थी पंक्ति में (4, 25) पर झंडा गाड़ना चाहिए",
            "दूरी = √65 मीटर; रश्मि को 5वीं पंक्ति में (5, 20) पर झंडा गाड़ना चाहिए",
            "दूरी = 5√2 मीटर; रश्मि को 6वीं पंक्ति में (6, 22) पर झंडा गाड़ना चाहिए"
        ],
        [
            "અંતર = √61 મીટર; રશ્મિએ 5મી હરોળમાં 22.5 મીટરના અંતરે (5, 22.5) પર ધ્વજ રોપવો જોઈએ",
            "અંતર = 61 મીટર; રશ્મિએ 4થી હરોળમાં (4, 25) પર ધ્વજ રોપવો જોઈએ",
            "અંતર = √65 મીટર; રશ્મિએ 5મી હરોળમાં (5, 20) પર ધ્વજ રોપવો જોઈએ",
            "અંતર = 5√2 મીટર; રશ્મિએ 6ઠી હરોળમાં (6, 22) પર ધ્વજ રોપવો જોઈએ"
        ],
        0,
        "Niharika's position: Line 2, distance = 1/4 × 100 = 25 m ⇒ N(2, 25).\nPreet's position: Line 8, distance = 1/5 × 100 = 20 m ⇒ P(8, 20).\nDistance between flags: NP = √((8 - 2)² + (20 - 25)²) = √(6² + (-5)²) = √(36 + 25) = √61 m.\nRashmi's blue flag is at the midpoint of NP:\nx = (2 + 8) / 2 = 10 / 2 = 5\ny = (25 + 20) / 2 = 45 / 2 = 22.5\nHence, Rashmi should post her blue flag on the 5th line at a distance of 22.5 m!",
        "निहारिका की स्थिति: N(2, 25) (पंक्ति 2, दूरी = 100/4 = 25)\nप्रीत की स्थिति: P(8, 20) (पंक्ति 8, दूरी = 100/5 = 20)\nदोनों झंडों के बीच की दूरी: NP = √((8-2)² + (20-25)²) = √(36 + 25) = √61 मीटर।\nरश्मि का नीला झंडा NP के मध्य-बिंदु पर होगा:\nx = (2 + 8)/2 = 5, y = (25 + 20)/2 = 22.5\nअतः रश्मि को 5वीं पंक्ति में 22.5 मीटर की दूरी पर झंडा गाड़ना चाहिए!",
        "નિહારિકાનું સ્થાન: N(2, 25) (હરોળ 2, અંતર = 100/4 = 25)\nપ્રીતનું સ્થાન: P(8, 20) (હરોળ 8, અંતર = 100/5 = 20)\nધ્વજ વચ્ચેનું અંતર: NP = √((8-2)² + (20-25)²) = √(36 + 25) = √61 મીટર.\nરશ્મિનો વાદળી ધ્વજ NP ના મધ્યબિંદુ પર:\nx = (2 + 8)/2 = 5, y = (25 + 20)/2 = 22.5\nઆમ રશ્મિએ 5મી હરોળમાં 22.5 મીટરના અંતરે ધ્વજ રોપવો જોઈએ!",
        bloom="Apply",
        diff="Intermediate",
        mins=3
    ))

    # 33. Exercise 7.2 Q4
    blocks.append(make_quiz(
        "C10M_CH7_EX7.2_Q4",
        "Exercise 7.2 (Q4): Find the ratio in which the line segment joining the points (-3, 10) and (6, -8) is divided by (-1, 6).",
        "प्रश्नावली 7.2 (Q4): बिंदुओं (-3, 10) और (6, -8) को जोड़ने वाले रेखाखंड को बिंदु (-1, 6) किस अनुपात में विभाजित करता है?",
        "સ્વાધ્યાય 7.2 (Q4): બિંદુઓ (-3, 10) અને (6, -8) ને જોડતા રેખાખંડનું બિંદુ (-1, 6) કયા ગુણોત્તરમાં વિભાજન કરે છે?",
        ["2 : 7", "7 : 2", "3 : 4", "1 : 2"],
        ["2 : 7", "7 : 2", "3 : 4", "1 : 2"],
        ["2 : 7", "7 : 2", "3 : 4", "1 : 2"],
        0,
        "Let the ratio be k : 1. Using section formula for the x-coordinate:\nx = (k(6) + 1(-3)) / (k + 1)\n-1 = (6k - 3) / (k + 1)\n-1(k + 1) = 6k - 3 ⇒ -k - 1 = 6k - 3\n-k - 6k = -3 + 1 ⇒ -7k = -2 ⇒ k = 2/7.\nHence, the required ratio is 2 : 7.",
        "माना अनुपात k : 1 है। x-निर्देशांक के लिए विभाजन सूत्र का प्रयोग करने पर:\n-1 = (6k - 3) / (k + 1)\n-k - 1 = 6k - 3 ⇒ -7k = -2 ⇒ k = 2/7।\nअतः अभीष्ट अनुपात 2 : 7 है।",
        "ધારો કે ગુણોત્તર k : 1 છે. x-યામ માટે વિભાજન સૂત્ર વાપરતાં:\n-1 = (6k - 3) / (k + 1)\n-k - 1 = 6k - 3 ⇒ -7k = -2 ⇒ k = 2/7.\nઆમ માંગેલ ગુણોત્તર 2 : 7 છે.",
        bloom="Apply",
        diff="Intermediate",
        mins=2
    ))

    # 34. Exercise 7.2 Q5
    blocks.append(make_quiz(
        "C10M_CH7_EX7.2_Q5",
        "Exercise 7.2 (Q5): Find the ratio in which the line segment joining A(1, -5) and B(-4, 5) is divided by the x-axis. Also find the coordinates of the point of division.",
        "प्रश्नावली 7.2 (Q5): वह अनुपात ज्ञात कीजिए जिसमें बिंदुओं A(1, -5) और B(-4, 5) को मिलाने वाला रेखाखंड x-अक्ष से विभाजित होता है। इस विभाजन बिंदु के निर्देशांक भी ज्ञात कीजिए।",
        "સ્વાધ્યાય 7.2 (Q5): x-અક્ષ એ બિંદુઓ A(1, -5) અને B(-4, 5) ને જોડતા રેખાખંડનું કયા ગુણોત્તરમાં વિભાજન કરે છે તે શોધો. વિભાજન બિંદુના યામ પણ શોધો.",
        [
            "Ratio 1 : 1; Point (-3/2, 0)",
            "Ratio 2 : 1; Point (-1, 0)",
            "Ratio 1 : 2; Point (-2, 0)",
            "Ratio 3 : 2; Point (-3/2, 0)"
        ],
        [
            "अनुपात 1 : 1; बिंदु (-3/2, 0)",
            "अनुपात 2 : 1; बिंदु (-1, 0)",
            "अनुपात 1 : 2; बिंदु (-2, 0)",
            "अनुपात 3 : 2; बिंदु (-3/2, 0)"
        ],
        [
            "ગુણોત્તર 1 : 1; બિંદુ (-3/2, 0)",
            "ગુણોત્તર 2 : 1; બિંદુ (-1, 0)",
            "ગુણોત્તર 1 : 2; બિંદુ (-2, 0)",
            "ગુણોત્તર 3 : 2; બિંદુ (-3/2, 0)"
        ],
        0,
        "Any point on the x-axis has y-coordinate = 0, so P = (x, 0). Let the ratio be k : 1.\ny = (k(5) + 1(-5)) / (k + 1)\n0 = (5k - 5) / (k + 1) ⇒ 5k - 5 = 0 ⇒ 5k = 5 ⇒ k = 1.\nSo the ratio is 1 : 1 (the point is the midpoint!).\nNow calculate x:\nx = (1(-4) + 1(1)) / (1 + 1) = (-4 + 1) / 2 = -3/2.\nThus, the ratio is 1 : 1 and the point of division is (-3/2, 0).",
        "x-अक्ष पर बिंदु P(x, 0) होता है। माना अनुपात k : 1 है।\ny = (5k - 5) / (k + 1) ⇒ 0 = 5k - 5 ⇒ k = 1 (अनुपात 1 : 1 है)।\nx-निर्देशांक: x = (-4 + 1) / 2 = -3/2।\nअतः अनुपात 1 : 1 है और विभाजन बिंदु (-3/2, 0) है।",
        "x-અક્ષ પરના બિંદુ માટે y = 0 હોય, P(x, 0). ગુણોત્તર k : 1 ધારતાં:\ny = (5k - 5) / (k + 1) ⇒ 0 = 5k - 5 ⇒ k = 1 (ગુણોત્તર 1 : 1 છે).\nx-યામ: x = (-4 + 1) / 2 = -3/2.\nઆમ ગુણોત્તર 1 : 1 છે અને વિભાજન બિંદુ (-3/2, 0) છે.",
        bloom="Apply",
        diff="Intermediate",
        mins=2
    ))

    # 35. Exercise 7.2 Q6
    blocks.append(make_quiz(
        "C10M_CH7_EX7.2_Q6",
        "Exercise 7.2 (Q6): If (1, 2), (4, y), (x, 6) and (3, 5) are the vertices of a parallelogram taken in order, find the values of x and y.",
        "प्रश्नावली 7.2 (Q6): यदि बिंदु (1, 2), (4, y), (x, 6) और (3, 5) इसी क्रम में लेने पर एक समांतर चतुर्भुज के शीर्ष हों, तो x और y ज्ञात कीजिए।",
        "સ્વાધ્યાય 7.2 (Q6): જો (1, 2), (4, y), (x, 6) અને (3, 5) એ ક્રમમાં સમાંતરબાજુ ચતુષ્કોણના શિરોબિંદુઓ હોય, તો x અને y શોધો.",
        ["x = 6, y = 3", "x = 3, y = 6", "x = 5, y = 2", "x = 7, y = 4"],
        ["x = 6, y = 3", "x = 3, y = 6", "x = 5, y = 2", "x = 7, y = 4"],
        ["x = 6, y = 3", "x = 3, y = 6", "x = 5, y = 2", "x = 7, y = 4"],
        0,
        "Let A(1, 2), B(4, y), C(x, 6), D(3, 5). Diagonals of a parallelogram bisect each other.\nMidpoint of diagonal AC = Midpoint of diagonal BD\n((1 + x) / 2, (2 + 6) / 2) = ((4 + 3) / 2, (y + 5) / 2)\nEquating x-coordinates: (1 + x) / 2 = 7 / 2 ⇒ 1 + x = 7 ⇒ x = 6.\nEquating y-coordinates: 8 / 2 = (y + 5) / 2 ⇒ 8 = y + 5 ⇒ y = 3.\nTherefore, x = 6 and y = 3.",
        "माना A(1, 2), B(4, y), C(x, 6), D(3, 5)। समांतर चतुर्भुज के विकर्ण एक-दूसरे को समद्विभाजित करते हैं।\nAC का मध्य-बिंदु = BD का मध्य-बिंदु\n((1 + x)/2, 8/2) = (7/2, (y + 5)/2)\nx-निर्देशांक: (1 + x)/2 = 7/2 ⇒ x = 6\ny-निर्देशांक: 8/2 = (y + 5)/2 ⇒ y = 3\nअतः x = 6 और y = 3।",
        "સમાંતરબાજુ ચતુષ્કોણના વિકર્ણો પરસ્પર દુભાગે છે.\nAC નું મધ્યબિંદુ = BD નું મધ્યબિંદુ\n((1 + x)/2, 8/2) = (7/2, (y + 5)/2)\nx-યામ સરખાવતાં: (1 + x)/2 = 7/2 ⇒ x = 6\ny-યામ સરખાવતાં: 8/2 = (y + 5)/2 ⇒ y = 3\nઆમ x = 6 અને y = 3.",
        bloom="Apply",
        diff="Intermediate",
        mins=2
    ))

    # 36. Exercise 7.2 Q7
    blocks.append(make_quiz(
        "C10M_CH7_EX7.2_Q7",
        "Exercise 7.2 (Q7): Find the coordinates of a point A, where AB is the diameter of a circle whose centre is (2, -3) and B is (1, 4).",
        "प्रश्नावली 7.2 (Q7): बिंदु A के निर्देशांक ज्ञात कीजिए, जहाँ AB एक वृत्त का व्यास है जिसका केंद्र (2, -3) है तथा B के निर्देशांक (1, 4) हैं।",
        "સ્વાધ્યાય 7.2 (Q7): વર્તુળના વ્યાસ AB નું કેન્દ્ર (2, -3) અને B(1, 4) હોય, તો બિંદુ A ના યામ શોધો.",
        ["(3, -10)", "(-3, 10)", "(3, 10)", "(1, -7)"],
        ["(3, -10)", "(-3, 10)", "(3, 10)", "(1, -7)"],
        ["(3, -10)", "(-3, 10)", "(3, 10)", "(1, -7)"],
        0,
        "The centre C(2, -3) is the midpoint of diameter AB, where A = (x, y) and B = (1, 4).\nMidpoint formula: ((x + 1)/2, (y + 4)/2) = (2, -3)\n(x + 1) / 2 = 2 ⇒ x + 1 = 4 ⇒ x = 3\n(y + 4) / 2 = -3 ⇒ y + 4 = -6 ⇒ y = -10\nTherefore, the coordinates of A are (3, -10).",
        "केंद्र C(2, -3) व्यास AB का मध्य-बिंदु है, जहाँ A = (x, y) और B = (1, 4)।\n(x + 1)/2 = 2 ⇒ x = 3\n(y + 4)/2 = -3 ⇒ y = -10\nअतः बिंदु A के निर्देशांक (3, -10) हैं।",
        "કેન્દ્ર C(2, -3) એ વ્યાસ AB નું મધ્યબિંદુ છે, જ્યાં A(x, y) અને B(1, 4).\n(x + 1)/2 = 2 ⇒ x = 3\n(y + 4)/2 = -3 ⇒ y = -10\nઆમ બિંદુ A ના યામ (3, -10) છે.",
        bloom="Apply",
        diff="Beginner",
        mins=2
    ))

    # 37. Exercise 7.2 Q8
    blocks.append(make_quiz(
        "C10M_CH7_EX7.2_Q8",
        "Exercise 7.2 (Q8): If A and B are (-2, -2) and (2, -4), respectively, find the coordinates of P such that AP = 3/7 AB and P lies on the line segment AB.",
        "प्रश्नावली 7.2 (Q8): यदि A और B क्रमशः (-2, -2) और (2, -4) हों, तो बिंदु P के निर्देशांक ज्ञात कीजिए ताकि AP = 3/7 AB हो और P रेखाखंड AB पर स्थित हो।",
        "સ્વાધ્યાય 7.2 (Q8): જો A અને B અનુક્રમે (-2, -2) અને (2, -4) હોય, જેથી AP = 3/7 AB થાય અને P એ રેખાખંડ AB પર આવેલું હોય, તો બિંદુ P ના યામ શોધો.",
        [
            "(-2/7, -20/7)",
            "(2/7, -20/7)",
            "(-2/7, 20/7)",
            "(3/7, -4/7)"
        ],
        [
            "(-2/7, -20/7)",
            "(2/7, -20/7)",
            "(-2/7, 20/7)",
            "(3/7, -4/7)"
        ],
        [
            "(-2/7, -20/7)",
            "(2/7, -20/7)",
            "(-2/7, 20/7)",
            "(3/7, -4/7)"
        ],
        0,
        "Given AP = (3/7)AB ⇒ PB = AB - AP = AB - (3/7)AB = (4/7)AB.\nThus, AP / PB = (3/7) / (4/7) = 3 / 4. P divides AB in the ratio 3 : 4!\nm₁ = 3, m₂ = 4, A(-2, -2), B(2, -4).\nx = (3(2) + 4(-2)) / (3 + 4) = (6 - 8) / 7 = -2/7\ny = (3(-4) + 4(-2)) / (3 + 4) = (-12 - 8) / 7 = -20/7\nHence, P = (-2/7, -20/7).",
        "दिया है AP = 3/7 AB ⇒ PB = 4/7 AB।\nअतः AP : PB = 3 : 4 (P, AB को 3 : 4 के अनुपात में विभाजित करता है!)।\nx = (3(2) + 4(-2)) / 7 = -2/7\ny = (3(-4) + 4(-2)) / 7 = -20/7\nअतः P के निर्देशांक (-2/7, -20/7) हैं।",
        "આપેલ છે AP = 3/7 AB ⇒ PB = 4/7 AB.\nતેથી AP : PB = 3 : 4 (P એ AB નું 3 : 4 ના ગુણોત્તરમાં વિભાજન કરે છે!).\nx = (3(2) + 4(-2)) / 7 = -2/7\ny = (3(-4) + 4(-2)) / 7 = -20/7\nઆમ P ના યામ (-2/7, -20/7) છે.",
        bloom="Apply",
        diff="Intermediate",
        mins=2
    ))

    # 38. Exercise 7.2 Q9
    blocks.append(make_quiz(
        "C10M_CH7_EX7.2_Q9",
        "Exercise 7.2 (Q9): Find the coordinates of the points which divide the line segment joining A(-2, 2) and B(2, 8) into four equal parts.",
        "प्रश्नावली 7.2 (Q9): बिंदुओं A(-2, 2) और B(2, 8) को जोड़ने वाले रेखाखंड को चार बराबर भागों में विभाजित करने वाले बिंदुओं के निर्देशांक ज्ञात कीजिए।",
        "સ્વાધ્યાય 7.2 (Q9): બિંદુઓ A(-2, 2) અને B(2, 8) ને જોડતા રેખાખંડનું 4 સમાન ભાગોમાં વિભાજન કરતા બિંદુઓના યામ શોધો.",
        [
            "(-1, 7/2), (0, 5), and (1, 13/2)",
            "(-1, 3), (0, 5), and (1, 7)",
            "(0, 4), (1, 5), and (2, 6)",
            "(-1, 4), (0, 5), and (1, 6)"
        ],
        [
            "(-1, 7/2), (0, 5) और (1, 13/2)",
            "(-1, 3), (0, 5) और (1, 7)",
            "(0, 4), (1, 5) और (2, 6)",
            "(-1, 4), (0, 5) और (1, 6)"
        ],
        [
            "(-1, 7/2), (0, 5) અને (1, 13/2)",
            "(-1, 3), (0, 5) અને (1, 7)",
            "(0, 4), (1, 5) અને (2, 6)",
            "(-1, 4), (0, 5) અને (1, 6)"
        ],
        0,
        "Let the three dividing points be P, Q, R.\n1. Q is the exact midpoint of AB:\n   Q = ((-2 + 2)/2, (2 + 8)/2) = (0, 5)\n2. P is the midpoint of AQ (between A(-2, 2) and Q(0, 5)):\n   P = ((-2 + 0)/2, (2 + 5)/2) = (-1, 7/2)\n3. R is the midpoint of QB (between Q(0, 5) and B(2, 8)):\n   R = ((0 + 2)/2, (5 + 8)/2) = (1, 13/2)\nThus, the three points are (-1, 7/2), (0, 5), and (1, 13/2).",
        "माना तीन विभाजन बिंदु P, Q, R हैं।\n1. Q, AB का मध्य-बिंदु है: Q = ((-2+2)/2, (2+8)/2) = (0, 5)\n2. P, AQ का मध्य-बिंदु है: P = ((-2+0)/2, (2+5)/2) = (-1, 7/2)\n3. R, QB का मध्य-बिंदु है: R = ((0+2)/2, (5+8)/2) = (1, 13/2)\nअतः तीनों बिंदु (-1, 7/2), (0, 5) और (1, 13/2) हैं।",
        "ધારો કે ત્રણ વિભાજન બિંદુઓ P, Q, R છે.\n1. Q એ AB નું મધ્યબિંદુ છે: Q = ((-2+2)/2, (2+8)/2) = (0, 5)\n2. P એ AQ નું મધ્યબિંદુ છે: P = ((-2+0)/2, (2+5)/2) = (-1, 7/2)\n3. R એ QB નું મધ્યબિંદુ છે: R = ((0+2)/2, (5+8)/2) = (1, 13/2)\nઆમ ત્રણ બિંદુઓ (-1, 7/2), (0, 5) અને (1, 13/2) છે.",
        bloom="Apply",
        diff="Intermediate",
        mins=3
    ))

    # 39. Exercise 7.2 Q10
    blocks.append(make_quiz(
        "C10M_CH7_EX7.2_Q10",
        "Exercise 7.2 (Q10): Find the area of a rhombus if its vertices are (3, 0), (4, 5), (-1, 4) and (-2, -1) taken in order. [Hint: Area of a rhombus = 1/2 × (product of diagonals)]",
        "प्रश्नावली 7.2 (Q10): एक समचतुर्भुज का क्षेत्रफल ज्ञात कीजिए जिसके शीर्ष, इसी क्रम में (3, 0), (4, 5), (-1, 4) और (-2, -1) हैं। [संकेत: समचतुर्भुज का क्षेत्रफल = 1/2 × (विकर्णों का गुणनफल)]",
        "સ્વાધ્યાય 7.2 (Q10): સમબાજુ ચતુષ્કોણના ક્રમિક શિરોબિંદુઓ (3, 0), (4, 5), (-1, 4) અને (-2, -1) હોય, તો તેનું ક્ષેત્રફળ શોધો. [સંકેત: સમબાજુ ચતુષ્કોણનું ક્ષેત્રફળ = 1/2 × (વિકર્ણોનો ગુણાકાર)]",
        ["24 sq units", "48 sq units", "12 sq units", "36 sq units"],
        ["24 वर्ग मात्रक", "48 वर्ग मात्रक", "12 वर्ग मात्रक", "36 वर्ग मात्रक"],
        ["24 ચોરસ એકમ", "48 ચોરસ એકમ", "12 ચોરસ એકમ", "36 ચોરસ એકમ"],
        0,
        "Let A(3, 0), B(4, 5), C(-1, 4), D(-2, -1).\nDiagonal 1 (AC): d₁ = √((-1 - 3)² + (4 - 0)²) = √((-4)² + 4²) = √(16 + 16) = √32 = 4√2\nDiagonal 2 (BD): d₂ = √((-2 - 4)² + (-1 - 5)²) = √((-6)² + (-6)²) = √(36 + 36) = √72 = 6√2\nArea of rhombus = (1/2) × d₁ × d₂ = (1/2) × (4√2) × (6√2) = (1/2) × 24 × 2 = 24 sq units!",
        "माना A(3, 0), B(4, 5), C(-1, 4), D(-2, -1)।\nविकर्ण AC: d₁ = √((-4)² + 4²) = √32 = 4√2\nविकर्ण BD: d₂ = √((-6)² + (-6)²) = √72 = 6√2\nसमचतुर्भुज का क्षेत्रफल = (1/2) × d₁ × d₂ = (1/2) × 4√2 × 6√2 = (1/2) × 48 = 24 वर्ग मात्रक!",
        "ધારો કે A(3, 0), B(4, 5), C(-1, 4), D(-2, -1).\nવિકર્ણ AC: d₁ = √((-4)² + 4²) = √32 = 4√2\nવિકર્ણ BD: d₂ = √((-6)² + (-6)²) = √72 = 6√2\nસમબાજુ ચતુષ્કોણનું ક્ષેત્રફળ = (1/2) × d₁ × d₂ = (1/2) × 4√2 × 6√2 = (1/2) × 48 = 24 ચોરસ એકમ!",
        bloom="Apply",
        diff="Intermediate",
        mins=2
    ))

    return blocks

# =========================================================================
# PART 3: STEPS 6, 7, 8 & BOARD HOTS CHALLENGES
# =========================================================================
def get_part3_blocks():
    blocks = []

    # 40. Step 6: Reflection
    blocks.append(make_theory(
        "C10M_CH7_12",
        "Reflection: The Language of Space and Numbers",
        "आत्म-चिंतन: स्थान और संख्याओं की भाषा",
        "આત્મ-ચિંતન: અવકાશ અને સંખ્યાઓની અનોખી ભાષા",
        "Take a moment to reflect on what you have mastered in this chapter:\n\n1. **The Algebraic Ruler (Distance Formula):** Before Descartes, finding the distance between two arbitrary points required physical rulers or complex Euclidean constructions. With coordinates, distance becomes simple arithmetic: $\\sqrt{\\Delta x^2 + \\Delta y^2}$!\n\n2. **The Precision Knife (Section Formula):** By combining ratios with coordinates, we can slice any line segment at any exact point in 2D space.\n\n*Question to Ponder:* If you were stranded on an open ocean, how does your phone's GPS use coordinates $(x, y, z)$ from 4 different satellites to calculate your location down to 1 meter? It uses the 3D Distance Formula! In Class 11, you will expand this exact formula into 3D: $\\sqrt{\\Delta x^2 + \\Delta y^2 + \\Delta z^2}$.",
        "इस अध्याय में आपने जो कुछ सीखा है, उस पर एक क्षण विचार करें:\n\n1. **बीजगणितीय पैमाना (दूरी सूत्र):** देकार्त से पहले, दो बिंदुओं के बीच की दूरी मापने के लिए भौतिक पैमाने या जटिल यूक्लिडीय रचनाओं की आवश्यकता होती थी। निर्देशांकों के साथ, दूरी सरल अंकगणित बन जाती है: $\\sqrt{\\Delta x^2 + \\Delta y^2}$!\n\n2. **सटीक विभाजन (विभाजन सूत्र):** अनुपातों को निर्देशांकों के साथ जोड़कर, हम 2D तल में किसी भी रेखाखंड को किसी भी सटीक बिंदु पर विभाजित कर सकते हैं।\n\n*विचारणीय प्रश्न:* यदि आप खुले समुद्र में हों, तो आपके फोन का जीपीएस 4 उपग्रहों के निर्देशांकों का उपयोग करके आपकी स्थिति 1 मीटर की सटीकता के साथ कैसे बताता है? यह 3D दूरी सूत्र का उपयोग करता है! कक्षा 11 में आप इसे 3D में विस्तारित करेंगे: $\\sqrt{\\Delta x^2 + \\Delta y^2 + \\Delta z^2}$।",
        "આ પ્રકરણમાં તમે જે શીખ્યા છો તેના પર એક ક્ષણ વિચાર કરો:\n\n1. **બીજગણિતીય માપપટ્ટી (અંતર સૂત્ર):** દેકાર્ત પહેલાં, બે બિંદુઓ વચ્ચેનું અંતર શોધવા ભૌતિક માપપટ્ટી કે ભૂમિતિની જટિલ રચનાઓ કરવી પડતી. યામ પદ્ધતિથી અંતર શોધવું એ સરળ અંકગણિત બની ગયું: $\\sqrt{\\Delta x^2 + \\Delta y^2}$!\n\n2. **ચોકસાઈભર્યું વિભાજન (વિભાજન સૂત્ર):** ગુણોત્તર અને યામોના સંયોજનથી આપણે સમતલમાં કોઈપણ રેખાખંડનું ચોક્કસ બિંદુ આગળ વિભાજન કરી શકીએ છીએ.\n\n*વિચારવા જેવો પ્રશ્ન:* દરિયામાં તમારા ફોનનું GPS ઉપગ્રહોના યામોની મદદથી તમારું ચોક્કસ સ્થાન 1 મીટરની ચોકસાઈથી કેવી રીતે નક્કી કરે છે? તે 3D અંતર સૂત્ર વાપરે છે! ધોરણ 11 માં તમે આ જ સૂત્રને 3D માં શીખશો: $\\sqrt{\\Delta x^2 + \\Delta y^2 + \\Delta z^2}$.",
        btype="reflection",
        bloom="Analyze",
        diff="Beginner",
        mins=2
    ))

    # 41. Step 7: Connection (Knowledge Graph)
    blocks.append(make_theory(
        "C10M_CH7_13",
        "The Knowledge Web: Coordinate Geometry in Higher Math & Science",
        "ज्ञान सेतु: उच्च गणित और विज्ञान में निर्देशांक ज्यामिति",
        "જ્ઞાન સેતુ: ઉચ્ચ ગણિત અને વિજ્ઞાનમાં યામ ભૂમિતિનો પ્રભાવ",
        "Coordinate Geometry is not an isolated chapter; it is the foundation of modern analytical science:\n\n- **Algebra Meets Geometry (Class 10 Ch 3 & Ch 4):** A linear equation $ax + by + c = 0$ is literally a straight line on the Cartesian plane! Quadratic equations produce parabolas.\n- **Physics (Kinematics & Vectors):** Position, displacement, velocity vectors, and centre of mass ($x_{cm} = \\frac{m_1 x_1 + m_2 x_2}{m_1 + m_2}$) are direct physical manifestations of the Section Formula!\n- **Higher Secondary (Class 11 & 12):** Straight lines, Conic sections (Circles, Parabolas, Ellipses, Hyperbolas), Calculus (derivatives represent the slopes of tangents on coordinate curves), and 3D Vector Algebra.\n- **Modern Engineering:** Computer Graphics, GPS Satellites, Autonomous Self-Driving Cars (LiDAR generates 3D point cloud coordinates), and Computer-Aided Design (CAD).",
        "निर्देशांक ज्यामिति कोई अलग-थलग अध्याय नहीं है; यह आधुनिक विश्लेषणात्मक विज्ञान की आधारशिला है:\n\n- **बीजगणित और ज्यामिति का संगम (कक्षा 10 अ. 3 और 4):** रैखिक समीकरण $ax + by + c = 0$ कार्तीसीय तल पर एक सीधी रेखा का प्रतिनिधित्व करता है! द्विघात समीकरण परवलय (parabola) बनाते हैं।\n- **भौतिकी (गति विज्ञान और सदिश):** स्थिति, विस्थापन, वेग सदिश, और द्रव्यमान केंद्र ($x_{cm} = \\frac{m_1 x_1 + m_2 x_2}{m_1 + m_2}$) सीधे विभाजन सूत्र के भौतिक अनुप्रयोग हैं!\n- **उच्चतर माध्यमिक (कक्षा 11 और 12):** सरल रेखाएँ, शंकु परिच्छेद (वृत्त, परवलय, दीर्घवृत्त, अतिपरवलय), कलन (कलन में अवकलज वक्र की ढाल दर्शाते हैं) और 3D सदिश बीजगणित।\n- **आधुनिक इंजीनियरिंग:** कंप्यूटर ग्राफिक्स, जीपीएस, स्वचालित कारें (LiDAR 3D पॉइंट क्लाउड बनाता है) और CAD सॉफ्टवेयर।",
        "યામ ભૂમિતિ એ કોઈ અલગ પ્રકરણ નથી; તે આધુનિક વિજ્ઞાનનો પાયો છે:\n\n- **બીજગણિત અને ભૂમિતિનો સંગમ (ધોરણ 10 પ્ર. 3 અને 4):** સુરેખ સમીકરણ $ax + by + c = 0$ એ કાર્તેઝિયન સમતલ પર સીધી રેખા દર્શાવે છે! દ્વિઘાત સમીકરણો પરવલય રચે છે.\n- **ભૌતિકવિજ્ઞાન (ગતિશાસ્ત્ર અને સદિશો):** સ્થાન, સ્થાનાંતર, વેગ સદિશો અને દ્રવ્યમાન કેન્દ્ર ($x_{cm} = \\frac{m_1 x_1 + m_2 x_2}{m_1 + m_2}$) એ વિભાજન સૂત્રના ભૌતિક ઉપયોગો છે!\n- **ઉચ્ચતર માધ્યમિક (ધોરણ 11 અને 12):** સુરેખાઓ, શાંકવો (વર્તુળ, પરવલય, ઉપવલય, અતિવલય), કલનશાસ્ત્ર (વિકલન એ વક્રના સ્પર્શકનો ઢાળ દર્શાવે છે) અને 3D સદિશ બીજગણિત.\n- **આધુનિક એન્જિનિયરિંગ:** કોમ્પ્યુટર ગ્રાફિક્સ, GPS, સેલ્ફ-ડ્રાઇવિંગ કાર (LiDAR 3D પોઇન્ટ ક્લાઉડ યામો વાપરે છે) અને CAD સોફ્ટવેર.",
        btype="connection",
        bloom="Understand",
        diff="Beginner",
        mins=2
    ))

    # 42. Step 8: Mastery Summary
    blocks.append(make_theory(
        "C10M_CH7_14",
        "Mastery Summary: The 3 Master Formulas of Coordinate Geometry",
        "दक्षता सारांश: निर्देशांक ज्यामिति के 3 मास्टर सूत्र",
        "પ્રભુત્વ સારાંશ: યામ ભૂમિતિના 3 મહામંત્ર સૂત્રો",
        "Before stepping into your examinations, memorize this essential formula cheat-sheet:\n\n1. **Distance Formula:**\n   $$d = \\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$\n   *Distance from origin:* $OP = \\sqrt{x^2 + y^2}$\n\n2. **Section Formula (Internal Division in ratio $m_1 : m_2$):**\n   $$P(x, y) = \\left( \\frac{m_1 x_2 + m_2 x_1}{m_1 + m_2}, \\frac{m_1 y_2 + m_2 y_1}{m_1 + m_2} \\right)$$\n\n3. **Mid-point Formula:**\n   $$M(x, y) = \\left( \\frac{x_1 + x_2}{2}, \\frac{y_1 + y_2}{2} \\right)$$\n\n**Golden Exam Tips:**\n- If point is on the x-axis, write coordinates as $(x, 0)$.\n- If point is on the y-axis, write coordinates as $(0, y)$.\n- For unknown ratio problems, ALWAYS assume the ratio is $k : 1$.\n- For parallelogram problems, equate midpoints of the two diagonals!",
        "परीक्षा से पहले इन अनिवार्य सूत्रों और युक्तियों को अवश्य याद रखें:\n\n1. **दूरी सूत्र:**\n   $$d = \\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$\n   *मूलबिंदु से दूरी:* $OP = \\sqrt{x^2 + y^2}$\n\n2. **विभाजन सूत्र ($m_1 : m_2$ अनुपात में अंतः विभाजन):**\n   $$P(x, y) = \\left( \\frac{m_1 x_2 + m_2 x_1}{m_1 + m_2}, \\frac{m_1 y_2 + m_2 y_1}{m_1 + m_2} \\right)$$\n\n3. **मध्य-बिंदु सूत्र:**\n   $$M(x, y) = \\left( \\frac{x_1 + x_2}{2}, \\frac{y_1 + y_2}{2} \\right)$$\n\n**परीक्षा के स्वर्णिम नियम:**\n- यदि बिंदु x-अक्ष पर है, तो उसके निर्देशांक $(x, 0)$ लें।\n- यदि बिंदु y-अक्ष पर है, तो उसके निर्देशांक $(0, y)$ लें।\n- अज्ञात अनुपात के प्रश्नों में हमेशा अनुपात $k : 1$ मानें।\n- समांतर चतुर्भुज के प्रश्नों में दोनों विकर्णों के मध्य-बिंदुओं को बराबर रखें!",
        "પરીક્ષામાં જતા પહેલાં આ અનિવાર્ય સૂત્રો અને નિયમો યાદ રાખો:\n\n1. **અંતર સૂત્ર:**\n   $$d = \\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$\n   *ઉગમબિંદુથી અંતર:* $OP = \\sqrt{x^2 + y^2}$\n\n2. **વિભાજન સૂત્ર ($m_1 : m_2$ ગુણોત્તરમાં અંતઃવિભાજન):**\n   $$P(x, y) = \\left( \\frac{m_1 x_2 + m_2 x_1}{m_1 + m_2}, \\frac{m_1 y_2 + m_2 y_1}{m_1 + m_2} \\right)$$\n\n3. **મધ્યબિંદુ સૂત્ર:**\n   $$M(x, y) = \\left( \\frac{x_1 + x_2}{2}, \\frac{y_1 + y_2}{2} \\right)$$\n\n**પરીક્ષાના સુવર્ણ નિયમો:**\n- જો બિંદુ x-અક્ષ પર હોય, તો તેના યામ $(x, 0)$ લેવા.\n- જો બિંદુ y-અક્ષ પર હોય, તો તેના યામ $(0, y)$ લેવા.\n- અજ્ઞાત ગુણોત્તર શોધવા હંમેશા ગુણોત્તર $k : 1$ ધારવો.\n- સમાંતરબાજુ ચતુષ્કોણ માટે બંને વિકર્ણોના મધ્યબિંદુ સરખાવવા!",
        btype="mastery",
        bloom="Create",
        diff="Beginner",
        mins=2
    ))

    # 43. Board HOTS Challenge 1: Line dividing segment
    blocks.append(make_quiz(
        "C10M_CH7_HOTS_Q1",
        "Board HOTS: In what ratio does the line 2x + y - 4 = 0 divide the line segment joining the points A(2, -2) and B(3, 7)?",
        "बोर्ड परीक्षा HOTS: रेखा 2x + y - 4 = 0 बिंदुओं A(2, -2) और B(3, 7) को जोड़ने वाले रेखाखंड को किस अनुपात में विभाजित करती है?",
        "બોર્ડ HOTS પ્રશ્ન: રેખા 2x + y - 4 = 0 એ બિંદુઓ A(2, -2) અને B(3, 7) ને જોડતા રેખાખંડનું કયા ગુણોત્તરમાં વિભાજન કરે છે?",
        ["2 : 9", "9 : 2", "3 : 7", "1 : 4"],
        ["2 : 9", "9 : 2", "3 : 7", "1 : 4"],
        ["2 : 9", "9 : 2", "3 : 7", "1 : 4"],
        0,
        "Let the line divide AB in the ratio k : 1.\nCoordinates of the dividing point P:\nx = (3k + 2) / (k + 1), and y = (7k - 2) / (k + 1)\nSince P lies on the line 2x + y - 4 = 0, substitute x and y:\n2[(3k + 2) / (k + 1)] + [(7k - 2) / (k + 1)] - 4 = 0\nMultiply throughout by (k + 1):\n2(3k + 2) + (7k - 2) - 4(k + 1) = 0\n6k + 4 + 7k - 2 - 4k - 4 = 0\n9k - 2 = 0 ⇒ 9k = 2 ⇒ k = 2/9.\nTherefore, the required ratio is 2 : 9!",
        "माना रेखा AB को k : 1 के अनुपात में विभाजित करती है।\nविभाजन बिंदु P के निर्देशांक: x = (3k + 2)/(k + 1), y = (7k - 2)/(k + 1)\nचूँकि P रेखा 2x + y - 4 = 0 पर स्थित है:\n2(3k + 2) + (7k - 2) - 4(k + 1) = 0\n6k + 4 + 7k - 2 - 4k - 4 = 0\n9k - 2 = 0 ⇒ k = 2/9।\nअतः अभीष्ट अनुपात 2 : 9 है!",
        "ધારો કે રેખા AB નું k : 1 ના ગુણોત્તરમાં વિભાજન કરે છે.\nવિભાજન બિંદુ P ના યામ: x = (3k + 2)/(k + 1), y = (7k - 2)/(k + 1)\nP એ રેખા 2x + y - 4 = 0 પર આવેલું હોવાથી:\n2(3k + 2) + (7k - 2) - 4(k + 1) = 0\n6k + 4 + 7k - 2 - 4k - 4 = 0\n9k - 2 = 0 ⇒ k = 2/9.\nઆમ માંગેલ ગુણોત્તર 2 : 9 છે!",
        bloom="Apply",
        diff="Advanced",
        mins=3
    ))

    # 44. Board HOTS Challenge 2: Circumcentre of a right triangle
    blocks.append(make_quiz(
        "C10M_CH7_HOTS_Q2",
        "Board HOTS: Find the coordinates of the circumcentre of the triangle with vertices (8, 6), (8, -2) and (2, -2).",
        "बोर्ड परीक्षा HOTS: शीर्षों (8, 6), (8, -2) और (2, -2) वाले त्रिभुज के परिकेंद्र के निर्देशांक ज्ञात कीजिए।",
        "બોર્ડ HOTS પ્રશ્ન: શિરોબિંદુઓ (8, 6), (8, -2) અને (2, -2) વાળા ત્રિકોણના પરિકેન્દ્રના યામ શોધો.",
        ["(5, 2)", "(4, 3)", "(5, 1)", "(6, 2)"],
        ["(5, 2)", "(4, 3)", "(5, 1)", "(6, 2)"],
        ["(5, 2)", "(4, 3)", "(5, 1)", "(6, 2)"],
        0,
        "Let A(8, 6), B(8, -2), C(2, -2).\nNotice AB is a vertical line (x = 8) and BC is a horizontal line (y = -2).\nSince horizontal and vertical lines are perpendicular, ∠B = 90°! Triangle ABC is a right-angled triangle.\nBy a fundamental theorem of geometry, the circumcentre of any right-angled triangle is the exact MIDPOINT of its hypotenuse AC!\nHypotenuse endpoints are A(8, 6) and C(2, -2).\nMidpoint = ((8 + 2)/2, (6 + (-2))/2) = (10/2, 4/2) = (5, 2)!\nTherefore, the circumcentre is (5, 2).",
        "माना A(8, 6), B(8, -2), C(2, -2).\nAB एक ऊर्ध्वाधर रेखा है (x = 8) और BC एक क्षैतिज रेखा है (y = -2)।\nक्षैतिज और ऊर्ध्वाधर रेखाएँ परस्पर लंबवत होती हैं, अतः ∠B = 90°! यह एक समकोण त्रिभुज है।\nज्यामिति के मूल प्रमेय के अनुसार, किसी भी समकोण त्रिभुज का परिकेंद्र उसके कर्ण AC का बिल्कुल मध्य-बिंदु होता है!\nकर्ण AC का मध्य-बिंदु = ((8 + 2)/2, (6 - 2)/2) = (10/2, 4/2) = (5, 2)।\nअतः परिकेंद्र (5, 2) है।",
        "ધારો કે A(8, 6), B(8, -2), C(2, -2).\nAB એ શિરોલંબ રેખા છે (x = 8) અને BC એ સમક્ષિતિજ રેખા છે (y = -2).\nઆથી ∠B = 90° થાય, એટલે કે આ કાટકોણ ત્રિકોણ છે!\nભૂમિતિના પ્રમેય મુજબ, કાટકોણ ત્રિકોણનું પરિકેન્દ્ર એ તેના કર્ણ AC નું બરાબર મધ્યબિંદુ હોય છે!\nકર્ણ AC નું મધ્યબિંદુ = ((8 + 2)/2, (6 - 2)/2) = (10/2, 4/2) = (5, 2).\nઆમ પરિકેન્દ્ર (5, 2) છે.",
        bloom="Analyze",
        diff="Advanced",
        mins=3
    ))

    # 45. Board HOTS Challenge 3: Point on line x - y + 2 = 0
    blocks.append(make_quiz(
        "C10M_CH7_HOTS_Q3",
        "Board HOTS: Point P divides the segment joining A(-1, 3) and B(9, 8) in the ratio k : 1. If P also lies on the line x - y + 2 = 0, find the value of k.",
        "बोर्ड परीक्षा HOTS: बिंदु P, A(-1, 3) और B(9, 8) को मिलाने वाले रेखाखंड को k : 1 के अनुपात में विभाजित करता है। यदि P रेखा x - y + 2 = 0 पर भी स्थित है, तो k का मान ज्ञात कीजिए।",
        "બોર્ડ HOTS પ્રશ્ન: બિંદુ P એ A(-1, 3) અને B(9, 8) ને જોડતા રેખાખંડનું k : 1 ના ગુણોત્તરમાં વિભાજન કરે છે. જો P એ રેખા x - y + 2 = 0 પર પણ આવેલું હોય, તો k નું મૂલ્ય શોધો.",
        ["2/3", "3/2", "1/2", "3/4"],
        ["2/3", "3/2", "1/2", "3/4"],
        ["2/3", "3/2", "1/2", "3/4"],
        0,
        "Using the section formula, coordinates of P:\nx = (9k - 1) / (k + 1)\ny = (8k + 3) / (k + 1)\nSubstitute into line equation x - y + 2 = 0:\n(9k - 1) / (k + 1) - (8k + 3) / (k + 1) + 2 = 0\nMultiply by (k + 1):\n(9k - 1) - (8k + 3) + 2(k + 1) = 0\n9k - 1 - 8k - 3 + 2k + 2 = 0\n3k - 2 = 0 ⇒ 3k = 2 ⇒ k = 2/3.",
        "विभाजन सूत्र से P के निर्देशांक:\nx = (9k - 1)/(k + 1), y = (8k + 3)/(k + 1)\nरेखा के समीकरण x - y + 2 = 0 में मान रखने पर:\n(9k - 1) - (8k + 3) + 2(k + 1) = 0\n9k - 1 - 8k - 3 + 2k + 2 = 0\n3k - 2 = 0 ⇒ k = 2/3।",
        "વિભાજન સૂત્ર મુજબ P ના યામ:\nx = (9k - 1)/(k + 1), y = (8k + 3)/(k + 1)\nરેખા સમીકરણ x - y + 2 = 0 માં મૂકતાં:\n(9k - 1) - (8k + 3) + 2(k + 1) = 0\n9k - 1 - 8k - 3 + 2k + 2 = 0\n3k - 2 = 0 ⇒ k = 2/3.",
        bloom="Apply",
        diff="Advanced",
        mins=3
    ))

    return blocks

def generate_blocks():
    return get_part1_blocks() + get_part2_blocks() + get_part3_blocks()

def generate_chapter():
    chapter_data = {
        "metadata": get_metadata(),
        "blocks": generate_blocks()
    }
    
    output_dir = 'app_core/chapters'
    os.makedirs(output_dir, exist_ok=True)
    target_path = os.path.join(output_dir, 'ncert_class10_maths_ch7.json')
    
    with open(target_path, 'w', encoding='utf-8') as f:
        json.dump(chapter_data, f, indent=2, ensure_ascii=False)
        
    print(f"Generated {target_path} successfully with {len(chapter_data['blocks'])} blocks!")

if __name__ == "__main__":
    generate_chapter()
