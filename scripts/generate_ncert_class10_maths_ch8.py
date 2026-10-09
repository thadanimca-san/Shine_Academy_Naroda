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
        "id": "ncert_class10_maths_ch8",
        "title": "Chapter 8: Introduction to Trigonometry",
        "title_hi": "अध्याय 8: त्रिकोणमिति का परिचय",
        "title_gu": "પ્રકરણ 8: ત્રિકોણમિતિનો પરિચય",
        "subject": "Mathematics",
        "grade": "10",
        "board": "CBSE/GSEB",
        "curriculum": ["CBSE", "NCERT", "GSEB"],
        "language": "English, Hindi, Gujarati",
        "difficulty": "Intermediate",
        "estimated_minutes": 200,
        "version": "2.0.0",
        "author": "Shine Academy EduOS",
        "last_updated": "2026-10-01",
        "tags": [
            "trigonometry",
            "trigonometric_ratios",
            "sin_cos_tan",
            "pythagorean_identities",
            "specific_angles",
            "board_exam"
        ]
    }

# =========================================================================
# PART 1: TRIGONOMETRIC RATIOS & EXERCISE 8.1
# =========================================================================
def get_part1_blocks():
    blocks = []

    # 1. Hook (Step 1)
    blocks.append(make_theory(
        "C10M_CH8_1",
        "Measuring the Unreachable: The Secret of Trigonometry",
        "पहुँच से बाहर की माप: त्रिकोणमिति का रहस्य",
        "પહોંચ બહારનું માપન: ત્રિકોણમિતિનું રહસ્ય",
        "How did ancient astronomers calculate the distance from Earth to the Moon without a tape measure? How did Radhanath Sikdar and Sir George Everest calculate the exact height of Mount Everest (8,848 m) without ever climbing to its peak?\n\nThe answer lies in **Trigonometry (त्रिकोणमिति / ત્રિકોણમિતિ)** — derived from the Greek words *tri* (three), *gon* (sides), and *metron* (measure). It is the branch of mathematics that explores the profound relationship between the angles and lengths of sides in triangles.\n\nWhenever you cannot physically climb or reach an object — whether it is the tip of a cellular antenna, the height of a sky-piercing pyramid, or the width of a roaring river — trigonometry allows you to measure it using a simple angle of sight and a baseline distance!",
        "प्राचीन खगोलविदों ने बिना किसी फीते के पृथ्वी से चंद्रमा की दूरी की गणना कैसे की? राधानाथ सिकदर और सर जॉर्ज एवरेस्ट ने बिना चोटी पर चढ़े माउंट एवरेस्ट की सटीक ऊँचाई (8,848 मीटर) की गणना कैसे की?\n\nइसका उत्तर है **त्रिकोणमिति (Trigonometry)** — जो ग्रीक शब्दों *त्रि* (तीन), *गोन* (भुजाएँ) और *मेट्रॉन* (माप) से मिलकर बना है। यह गणित की वह शाखा है जो त्रिभुजों के कोणों और उनकी भुजाओं की लंबाइयों के बीच के गहरे संबंध का अध्ययन करती है।\n\nजब भी आप किसी वस्तु पर शारीरिक रूप से नहीं चढ़ सकते — चाहे वह मोबाइल टॉवर का शिखर हो, आकाश छूते पिरामिड की ऊँचाई हो, या किसी विशाल नदी की चौड़ाई — त्रिकोणमिति केवल दृष्टि कोण और जमीन पर मापी गई दूरी की सहायता से सटीक गणना करने की शक्ति देती है!",
        "પ્રાચીન ખગોળશાસ્ત્રીઓએ મેઝરિંગ ટેપ વગર પૃથ્વીથી ચંદ્રનું અંતર કેવી રીતે માપ્યું? રાધાનાથ સિકદર અને સર જ્યોર્જ એવરેસ્ટે શિખર પર ચઢ્યા વિના જ માઉન્ટ એવરેસ્ટની ચોક્કસ ઊંચાઈ (8,848 મીટર) કેવી રીતે શોધી?\n\nઆનો ઉત્તર છે **ત્રિકોણમિતિ (Trigonometry)** — જે ગ્રીક શબ્દો *ટ્રાય* (ત્રણ), *ગોન* (બાજુઓ) અને *મેટ્રોન* (માપ) પરથી બન્યો છે. તે ત્રિકોણના ખૂણાઓ અને બાજુઓની લંબાઈ વચ્ચેના ગાણિતિક સંબંધોનો અભ્યાસ કરે છે.\n\nજ્યારે તમે કોઈ વસ્તુ પર પ્રત્યક્ષ રીતે ચઢી કે પહોંચી શકતા નથી — જેમ કે મોબાઈલ ટાવરની ટોચ, પિરામિડની ઊંચાઈ કે વિશાળ નદીની પહોળાઈ — ત્યારે ત્રિકોણમિતિ દ્રષ્ટિ કોણ અને જમીન પરના અંતરની મદદથી સચોટ માપન કરવાની શક્તિ આપે છે!",
        btype="hook",
        bloom="Understand",
        diff="Beginner",
        mins=3
    ))

    # 2. Socratic Question (Step 2)
    blocks.append(make_socratic(
        "C10M_CH8_2",
        "Think Carefully: If you have a small right triangle with a 30° angle, and another giant right triangle also with a 30° angle (whose sides are 10 times longer), what happens to the ratio of the side opposite to 30° divided by the hypotenuse?",
        "ध्यान से सोचिए: यदि आपके पास 30° कोण वाला एक छोटा समकोण त्रिभुज है, और 30° कोण वाला ही एक विशाल समकोण त्रिभुज है (जिसकी भुजाएँ 10 गुना लंबी हैं), तो 30° के सम्मुख भुजा और कर्ण के अनुपात पर क्या प्रभाव पड़ेगा?",
        "ધ્યાનથી વિચારો: જો તમારી પાસે 30° ખૂણો ધરાવતો એક નાનો કાટકોણ ત્રિકોણ હોય, અને 30° ખૂણો જ ધરાવતો બીજો એક વિશાળ કાટકોણ ત્રિકોણ હોય (જેની બાજુઓ 10 ગણી મોટી છે), તો 30° ની સામેની બાજુ અને કર્ણના ગુણોત્તરનું શું થશે?",
        [
            "The ratio remains exactly the same in both triangles",
            "The ratio becomes 10 times larger in the giant triangle",
            "The ratio becomes 10 times smaller in the giant triangle",
            "The ratio depends on the area of the triangle"
        ],
        [
            "दोनों त्रिभुजों में अनुपात बिल्कुल समान रहता है",
            "विशाल त्रिभुज में अनुपात 10 गुना बड़ा हो जाता है",
            "विशाल त्रिभुज में अनुपात 10 गुना छोटा हो जाता है",
            "अनुपात त्रिभुज के क्षेत्रफल पर निर्भर करता है"
        ],
        [
            "બંને ત્રિકોણમાં ગુણોત્તર બિલકુલ સમાન રહે છે",
            "વિશાળ ત્રિકોણમાં ગુણોત્તર 10 ગણો મોટો થઈ જાય છે",
            "વિશાળ ત્રિકોણમાં ગુણોત્તર 10 ગણો નાનો થઈ જાય છે",
            "ગુણોત્તર ત્રિકોણના ક્ષેત્રફળ પર આધાર રાખે છે"
        ],
        0,
        "By AAA similarity criterion, all right-angled triangles with the same acute angle (here 30°) are similar to each other! Therefore, the ratios of their corresponding sides are constant, regardless of the size of the triangle. This constant ratio is the foundation of Trigonometry!",
        "AAA समरूपता कसौटी के अनुसार, समान न्यूनकोण (यहाँ 30°) वाले सभी समकोण त्रिभुज आपस में समरूप होते हैं! इसलिए, उनकी संगत भुजाओं का अनुपात हमेशा स्थिर रहता है, चाहे त्रिभुज का आकार कितना भी बड़ा या छोटा क्यों न हो। यही स्थिर अनुपात त्रिकोणमिति का आधार है!",
        "AAA સમરૂપતા શરત મુજબ, સમાન લઘુકોણ (અહીં 30°) ધરાવતા તમામ કાટકોણ ત્રિકોણો સમરૂપ હોય છે! તેથી, ત્રિકોણનું કદ ગમે તેટલું મોટું કે નાનું હોય, તેમની અનુરૂપ બાજુઓનો ગુણોત્તર હંમેશા અચળ રહે છે. આ જ અચળ ગુણોત્તર ત્રિકોણમિતિનો પાયો છે!",
        bloom="Analyze",
        diff="Beginner",
        mins=2
    ))

    # 3. Discovery: The Right Triangle Framework (Step 3)
    blocks.append(make_theory(
        "C10M_CH8_3",
        "Discovery: Identifying Sides Relative to the Angle of Interest",
        "खोज: अभीष्ट कोण के सापेक्ष भुजाओं की सही पहचान",
        "શોધ: સંદર્ભ ખૂણાની સાપેક્ષે બાજુઓની સાચી ઓળખ",
        "In a right-angled triangle $\\triangle ABC$, right-angled at $B$:\n\n1. **Hypotenuse (कर्ण / કર્ણ):** The longest side, always opposite to the $90^\\circ$ right angle ($AC$).\n2. **Opposite Side (सम्मुख भुजा / સામેની બાજુ):** The side directly opposite to the angle you are looking at. For angle $A$, the opposite side is $BC$.\n3. **Adjacent Side (संलग्न भुजा / પાસેની બાજુ):** The side next to the angle (other than the hypotenuse). For angle $A$, the adjacent side is $AB$.\n\n**CRITICAL PERSPECTIVE SHIFT:**\nIf you shift your perspective to angle $C$:\n- The opposite side of $\\angle C$ is $AB$!\n- The adjacent side of $\\angle C$ is $BC$!\n- The hypotenuse $AC$ never changes.\n\n*Never think of 'base' and 'perpendicular' as fixed vertical or horizontal lines! They depend entirely on which acute angle you are observing.*",
        "समकोण त्रिभुज $\\triangle ABC$ में, जिसका कोण $B$ समकोण है:\n\n1. **कर्ण (Hypotenuse):** सबसे लंबी भुजा, जो हमेशा $90^\\circ$ समकोण के सम्मुख होती है ($AC$)।\n2. **सम्मुख भुजा (Opposite Side):** वह भुजा जो आपके द्वारा देखे जा रहे कोण के ठीक सामने होती है। कोण $A$ के लिए सम्मुख भुजा $BC$ है।\n3. **संलग्न भुजा (Adjacent Side):** वह भुजा जो कोण के साथ लगी होती है (कर्ण को छोड़कर)। कोण $A$ के लिए संलग्न भुजा $AB$ है।\n\n**दृष्टिकोण का महत्वपूर्ण परिवर्तन:**\nयदि आप अपना ध्यान कोण $C$ पर ले जाते हैं:\n- $\\angle C$ की सम्मुख भुजा $AB$ बन जाती है!\n- $\\angle C$ की संलग्न भुजा $BC$ बन जाती है!\n- कर्ण $AC$ कभी नहीं बदलता।\n\n*कभी भी 'आधार' और 'लंब' को निश्चित क्षैतिज या ऊर्ध्वाधर रेखाएँ न मानें! वे पूरी तरह इस बात पर निर्भर करते हैं कि आप किस न्यूनकोण के दृष्टिकोण से देख रहे हैं।*",
        "કાટકોણ ત્રિકોણ $\\triangle ABC$ માં, જ્યાં ખૂણો $B$ કાટખૂણો છે:\n\n1. **કર્ણ (Hypotenuse):** સૌથી મોટી બાજુ, જે હંમેશા $90^\\circ$ કાટખૂણાની સામે આવેલી હોય છે ($AC$).\n2. **સામેની બાજુ (Opposite Side):** તમે જે ખૂણાને સંદર્ભ તરીકે લો છો તેની બરાબર સામેની બાજુ. ખૂણા $A$ માટે સામેની બાજુ $BC$ છે.\n3. **પાસેની બાજુ (Adjacent Side):** ખૂણા સાથે જોડાયેલી બાજુ (કર્ણ સિવાયની). ખૂણા $A$ માટે પાસેની બાજુ $AB$ છે.\n\n**ખૂબ જ મહત્વનો ફેરફાર:**\nજો તમે ખૂણા $C$ ના સંદર્ભમાં વિચાર કરો:\n- $\\angle C$ ની સામેની બાજુ $AB$ બને છે!\n- $\\angle C$ ની પાસેની બાજુ $BC$ બને છે!\n- કર્ણ $AC$ ક્યારેય બદલાતો નથી.\n\n*ક્યારેય 'પાયો' કે 'વેધ' ને સ્થિર ન માનો! તે સંપૂર્ણપણે તમે કયો લઘુકોણ ધ્યાનમાં લો છો તેના પર આધારિત છે.*",
        btype="discovery",
        bloom="Understand",
        diff="Beginner",
        mins=3
    ))

    # 4. Reveal / Theory: The 6 Trigonometric Ratios (Step 4)
    blocks.append(make_theory(
        "C10M_CH8_4",
        "The Six Trigonometric Ratios: Definitions & Relationships",
        "छह त्रिकोणमितीय अनुपात: परिभाषाएँ और पारस्परिक संबंध",
        "છ ત્રિકોણમિતીય ગુણોત્તરો: વ્યાખ્યાઓ અને પરસ્પર સંબંધો",
        "For an acute angle $A$ in right triangle $\\triangle ABC$ (right-angled at $B$):\n\n### 1. The Three Primary Ratios\n- **Sine of $\\angle A$ (sin A):** $\\frac{\\text{Side opposite to } \\angle A}{\\text{Hypotenuse}} = \\frac{BC}{AC}$\n- **Cosine of $\\angle A$ (cos A):** $\\frac{\\text{Side adjacent to } \\angle A}{\\text{Hypotenuse}} = \\frac{AB}{AC}$\n- **Tangent of $\\angle A$ (tan A):** $\\frac{\\text{Side opposite to } \\angle A}{\\text{Side adjacent to } \\angle A} = \\frac{BC}{AB}$\n\n### 2. The Three Reciprocal Ratios\n- **Cosecant of $\\angle A$ (cosec A):** $\\frac{1}{\\sin A} = \\frac{\\text{Hypotenuse}}{\\text{Side opposite to } \\angle A} = \\frac{AC}{BC}$\n- **Secant of $\\angle A$ (sec A):** $\\frac{1}{\\cos A} = \\frac{\\text{Hypotenuse}}{\\text{Side adjacent to } \\angle A} = \\frac{AC}{AB}$\n- **Cotangent of $\\angle A$ (cot A):** $\\frac{1}{\\tan A} = \\frac{\\text{Side adjacent to } \\angle A}{\\text{Side opposite to } \\angle A} = \\frac{AB}{BC}$\n\n### 3. Quotient Relations\n$$\\tan A = \\frac{\\sin A}{\\cos A}, \\quad \\cot A = \\frac{\\cos A}{\\sin A}$$\n\n*Notation Note:* $(\\sin A)^2$ is written as $\\sin^2 A$, NOT $\\sin A^2$. Also, $\\sin A$ is NOT $\\sin \\times A$; 'sin' has no meaning without an angle.",
        "समकोण त्रिभुज $\\triangle ABC$ में न्यूनकोण $A$ के लिए (जहाँ $B$ समकोण है):\n\n### 1. तीन प्राथमिक अनुपात\n- **Sine (sin A):** $\\frac{\\text{कोण } A \\text{ की सम्मुख भुजा}}{\\text{कर्ण}} = \\frac{BC}{AC}$\n- **Cosine (cos A):** $\\frac{\\text{कोण } A \\text{ की संलग्न भुजा}}{\\text{कर्ण}} = \\frac{AB}{AC}$\n- **Tangent (tan A):** $\\frac{\\text{कोण } A \\text{ की सम्मुख भुजा}}{\\text{कोण } A \\text{ की संलग्न भुजा}} = \\frac{BC}{AB}$\n\n### 2. तीन व्युत्क्रम अनुपात\n- **Cosecant (cosec A):** $\\frac{1}{\\sin A} = \\frac{\\text{कर्ण}}{\\text{सम्मुख भुजा}} = \\frac{AC}{BC}$\n- **Secant (sec A):** $\\frac{1}{\\cos A} = \\frac{\\text{कर्ण}}{\\text{संलग्न भुजा}} = \\frac{AC}{AB}$\n- **Cotangent (cot A):** $\\frac{1}{\\tan A} = \\frac{\\text{संलग्न भुजा}}{\\text{सम्मुख भुजा}} = \\frac{AB}{BC}$\n\n### 3. भागफल संबंध\n$$\\tan A = \\frac{\\sin A}{\\cos A}, \\quad \\cot A = \\frac{\\cos A}{\\sin A}$$\n\n*संकेतन नियम:* $(\\sin A)^2$ को $\\sin^2 A$ लिखा जाता है, $\\sin A^2$ नहीं। साथ ही, $\\sin A$ का अर्थ $\\sin \\times A$ नहीं है; कोण के बिना 'sin' का कोई स्वतंत्र अस्तित्व नहीं है।",
        "કાટકોણ ત્રિકોણ $\\triangle ABC$ માં લઘુકોણ $A$ માટે (જ્યાં $B$ કાટખૂણો છે):\n\n### 1. ત્રણ મુખ્ય ગુણોત્તરો\n- **Sine (sin A):** $\\frac{\\angle A \\text{ ની સામેની બાજુ}}{\\text{કર્ણ}} = \\frac{BC}{AC}$\n- **Cosine (cos A):** $\\frac{\\angle A \\text{ ની પાસેની બાજુ}}{\\text{કર્ણ}} = \\frac{AB}{AC}$\n- **Tangent (tan A):** $\\frac{\\angle A \\text{ ની સામેની બાજુ}}{\\angle A \\text{ ની પાસેની બાજુ}} = \\frac{BC}{AB}$\n\n### 2. ત્રણ વ્યસ્ત ગુણોત્તરો\n- **Cosecant (cosec A):** $\\frac{1}{\\sin A} = \\frac{\\text{કર્ણ}}{\\text{સામેની બાજુ}} = \\frac{AC}{BC}$\n- **Secant (sec A):** $\\frac{1}{\\cos A} = \\frac{\\text{કર્ણ}}{\\text{પાસેની બાજુ}} = \\frac{AC}{AB}$\n- **Cotangent (cot A):** $\\frac{1}{\\tan A} = \\frac{\\text{પાસેની બાજુ}}{\\text{સામેની બાજુ}} = \\frac{AB}{BC}$\n\n### 3. ભાગાકાર સંબંધો\n$$\\tan A = \\frac{\\sin A}{\\cos A}, \\quad \\cot A = \\frac{\\cos A}{\\sin A}$$\n\n*ગાણિતિક સંકેત:* $(\\sin A)^2$ ને $\\sin^2 A$ લખાય છે, $\\sin A^2$ નહીં. વળી, $\\sin A$ નો અર્થ $\\sin \\times A$ નથી; ખૂણા વગર 'sin' નો કોઈ સ્વતંત્ર અર્થ નથી.",
        btype="theory",
        bloom="Remember",
        diff="Beginner",
        mins=4
    ))

    # 5. Teacher Tip (Step 5)
    blocks.append(make_theory(
        "C10M_CH8_5",
        "Teacher Tip: The Magic Mnemonics for Trigonometric Ratios",
        "शिक्षक युक्ति: त्रिकोणमितीय अनुपातों को याद रखने के जादुई सूत्र",
        "શિક્ષકની સલાહ: ત્રિકોણમિતીય ગુણોત્તરો યાદ રાખવાની સરળ યુક્તિ",
        "To remember the ratios instantly, Indian and Global students use these unforgettable mnemonics:\n\n**English: SOH CAH TOA**\n- **SOH:** $\\sin = \\frac{\\text{Opposite}}{\\text{Hypotenuse}}$\n- **CAH:** $\\cos = \\frac{\\text{Adjacent}}{\\text{Hypotenuse}}$\n- **TOA:** $\\tan = \\frac{\\text{Opposite}}{\\text{Adjacent}}$\n\n**Hindi: पंडित बद्री प्रसाद हर हर बोले (PBP / HHB)**\n- $\\sin = P/H$ (पंडित / हर)\n- $\\cos = B/H$ (बद्री / हर)\n- $\\tan = P/B$ (प्रसाद / बोले)\n\n**Gujarati: સાક પાક સાપા**\n- $\\sin = \\text{સા/ક}$ (સામેની બાજુ / કર્ણ)\n- $\\cos = \\text{પા/ક}$ (પાસેની બાજુ / કર્ણ)\n- $\\tan = \\text{સા/પા}$ (સામેની બાજુ / પાસેની બાજુ)\n\n*Golden Rule:* Once you know any ONE trigonometric ratio, use the Pythagoras Theorem ($a^2 + b^2 = c^2$) to find the third side, and then write down all 5 remaining ratios!",
        "अनुपातों को तुरंत याद रखने के लिए ये लोकप्रिय और आसान सूत्र उपयोग करें:\n\n**अंग्रेजी: SOH CAH TOA**\n- **SOH:** $\\sin = \\text{Opposite}/\\text{Hypotenuse}$\n- **CAH:** $\\cos = \\text{Adjacent}/\\text{Hypotenuse}$\n- **TOA:** $\\tan = \\text{Opposite}/\\text{Adjacent}$\n\n**हिंदी: पंडित बद्री प्रसाद हर हर बोले (PBP / HHB)**\n- $\\sin = P/H$ (लंब / कर्ण)\n- $\\cos = B/H$ (आधार / कर्ण)\n- $\\tan = P/B$ (लंब / आधार)\n\n**गुजराती: સાક પાક સાપા**\n- $\\sin = \\text{સા/ક}$ (સામેની બાજુ / કર્ણ)\n- $\\cos = \\text{પા/ક}$ (પાસેની બાજુ / કર્ણ)\n- $\\tan = \\text{સા/પા}$ (સામેની બાજુ / પાસેની બાજુ)\n\n*स्वर्ण नियम:* यदि आपको कोई एक त्रिकोणमितीय अनुपात ज्ञात हो, तो पाइथागोरस प्रमेय द्वारा तीसरी भुजा ज्ञात करके शेष सभी 5 अनुपात आसानी से निकाल सकते हैं!",
        "ગુણોત્તરો સરળતાથી યાદ રાખવા માટે આ શ્રેષ્ઠ ટ્રીક અપનાવો:\n\n**અંગ્રેજી: SOH CAH TOA**\n- **SOH:** $\\sin = \\text{Opposite}/\\text{Hypotenuse}$\n- **CAH:** $\\cos = \\text{Adjacent}/\\text{Hypotenuse}$\n- **TOA:** $\\tan = \\text{Opposite}/\\text{Adjacent}$\n\n**હિન્દી: પંડિત બદ્રી પ્રસાદ હર હર બોલે (PBP / HHB)**\n- $\\sin = P/H$ (લંબ / કર્ણ)\n- $\\cos = B/H$ (પાયો / કર્ણ)\n- $\\tan = P/B$ (લંબ / પાયો)\n\n**ગુજરાતી: સાક પાક સાપા**\n- $\\sin = \\text{સા/ક}$ (સામેની બાજુ / કર્ણ)\n- $\\cos = \\text{પા/ક}$ (પાસેની બાજુ / કર્ણ)\n- $\\tan = \\text{સા/પા}$ (સામેની બાજુ / પાસેની બાજુ)\n\n*સુવર્ણ નિયમ:* કોઈપણ એક ગુણોત્તર આપેલો હોય ત્યારે પાયથાગોરસ પ્રમેયથી ત્રીજી બાજુ શોધીને બાકીના પાંચેય ગુણોત્તરો સરળતાથી મળી જાય છે!",
        btype="teacher_tip",
        bloom="Remember",
        diff="Beginner",
        mins=2
    ))

    # 6. NCERT Example 1
    blocks.append(make_quiz(
        "C10M_CH8_EG1",
        "NCERT Example 1: Given tan A = 4/3, find the other trigonometric ratios of the angle A.",
        "NCERT उदाहरण 1: यदि tan A = 4/3, तो कोण A के अन्य त्रिकोणमितीय अनुपात ज्ञात कीजिए।",
        "NCERT ઉદાહરણ 1: જો tan A = 4/3 હોય, તો ખૂણા A ના અન્ય ત્રિકોણમિતીય ગુણોત્તરો શોધો.",
        [
            "sin A = 4/5, cos A = 3/5, cosec A = 5/4, sec A = 5/3, cot A = 3/4",
            "sin A = 3/5, cos A = 4/5, cosec A = 5/3, sec A = 5/4, cot A = 3/4",
            "sin A = 4/5, cos A = 3/4, cosec A = 5/4, sec A = 4/3, cot A = 4/3",
            "sin A = 3/4, cos A = 4/5, cosec A = 4/3, sec A = 5/4, cot A = 1"
        ],
        [
            "sin A = 4/5, cos A = 3/5, cosec A = 5/4, sec A = 5/3, cot A = 3/4",
            "sin A = 3/5, cos A = 4/5, cosec A = 5/3, sec A = 5/4, cot A = 3/4",
            "sin A = 4/5, cos A = 3/4, cosec A = 5/4, sec A = 4/3, cot A = 4/3",
            "sin A = 3/4, cos A = 4/5, cosec A = 4/3, sec A = 5/4, cot A = 1"
        ],
        [
            "sin A = 4/5, cos A = 3/5, cosec A = 5/4, sec A = 5/3, cot A = 3/4",
            "sin A = 3/5, cos A = 4/5, cosec A = 5/3, sec A = 5/4, cot A = 3/4",
            "sin A = 4/5, cos A = 3/4, cosec A = 5/4, sec A = 4/3, cot A = 4/3",
            "sin A = 3/4, cos A = 4/5, cosec A = 4/3, sec A = 5/4, cot A = 1"
        ],
        0,
        "Let BC = 4k and AB = 3k. By Pythagoras theorem:\nAC = √(AB² + BC²) = √((3k)² + (4k)²) = √(9k² + 16k²) = √25k² = 5k.\nNow:\nsin A = BC/AC = 4k/5k = 4/5\ncos A = AB/AC = 3k/5k = 3/5\ncot A = 1/tan A = 3/4\ncosec A = 1/sin A = 5/4\nsec A = 1/cos A = 5/3.",
        "माना BC = 4k और AB = 3k। पाइथागोरस प्रमेय से:\nAC = √(AB² + BC²) = √(9k² + 16k²) = √25k² = 5k।\nअतः:\nsin A = BC/AC = 4/5\ncos A = AB/AC = 3/5\ncot A = 1/tan A = 3/4\ncosec A = 1/sin A = 5/4\nsec A = 1/cos A = 5/3।",
        "ધારો કે BC = 4k અને AB = 3k. પાયથાગોરસ પ્રમેય મુજબ:\nAC = √(AB² + BC²) = √(9k² + 16k²) = √25k² = 5k.\nઆથી:\nsin A = BC/AC = 4/5\ncos A = AB/AC = 3/5\ncot A = 1/tan A = 3/4\ncosec A = 1/sin A = 5/4\nsec A = 1/cos A = 5/3.",
        bloom="Apply",
        diff="Beginner",
        mins=2
    ))

    # 7. NCERT Example 2
    blocks.append(make_theory(
        "C10M_CH8_EG2",
        "NCERT Example 2: Equal Sine Ratios Imply Equal Angles",
        "NCERT उदाहरण 2: समान साइन अनुपात समान कोण दर्शाते हैं",
        "NCERT ઉદાહરણ 2: સમાન સાઈન ગુણોત્તર સમાન ખૂણા દર્શાવે છે",
        "**Problem:** If $\\angle B$ and $\\angle Q$ are acute angles such that $\\sin B = \\sin Q$, then prove that $\\angle B = \\angle Q$.\n\n**Proof:**\nConsider two right triangles $\\triangle ABC$ and $\\triangle PQR$ where $\\angle C = \\angle R = 90^\\circ$.\nGiven: $\\sin B = \\sin Q \\implies \\frac{AC}{AB} = \\frac{PR}{PQ} = k$.\nSo $AC = k \\cdot PR$ and $AB = k \\cdot PQ$.\nBy Pythagoras theorem:\n$$BC = \\sqrt{AB^2 - AC^2}, \\quad QR = \\sqrt{PQ^2 - PR^2}$$\n$$\\frac{BC}{QR} = \\frac{\\sqrt{k^2 PQ^2 - k^2 PR^2}}{\\sqrt{PQ^2 - PR^2}} = \\frac{k\\sqrt{PQ^2 - PR^2}}{\\sqrt{PQ^2 - PR^2}} = k$$\nSince $\\frac{AC}{PR} = \\frac{AB}{PQ} = \\frac{BC}{QR} = k$, by SSS similarity criterion, $\\triangle ABC \\sim \\triangle PQR$.\nCorresponding angles are equal: $\\angle B = \\angle Q$.",
        "**प्रश्न:** यदि $\\angle B$ और $\\angle Q$ ऐसे न्यूनकोण हैं कि $\\sin B = \\sin Q$, तो सिद्ध कीजिए कि $\\angle B = \\angle Q$।\n\n**उपपत्ति:**\nदो समकोण त्रिभुजों $\\triangle ABC$ और $\\triangle PQR$ पर विचार करें जहाँ $\\angle C = \\angle R = 90^\\circ$ है।\nदिया है: $\\sin B = \\sin Q \\implies \\frac{AC}{AB} = \\frac{PR}{PQ} = k$।\nअतः $AC = k \\cdot PR$ और $AB = k \\cdot PQ$।\nपाइथागोरस प्रमेय से:\n$$BC = \\sqrt{AB^2 - AC^2}, \\quad QR = \\sqrt{PQ^2 - PR^2}$$\n$$\\frac{BC}{QR} = \\frac{\\sqrt{k^2(PQ^2 - PR^2)}}{\\sqrt{PQ^2 - PR^2}} = k$$\nचूँकि $\\frac{AC}{PR} = \\frac{AB}{PQ} = \\frac{BC}{QR} = k$, SSS समरूपता कसौटी से $\\triangle ABC \\sim \\triangle PQR$।\nसंगत कोण बराबर होंगे: $\\angle B = \\angle Q$।",
        "**પ્રશ્ન:** જો $\\angle B$ અને $\\angle Q$ એવા લઘુકોણો હોય કે જેથી $\\sin B = \\sin Q$, તો સાબિત કરો કે $\\angle B = \\angle Q$.\n\n**સાબિતી:**\nબે કાટકોણ ત્રિકોણ $\\triangle ABC$ અને $\\triangle PQR$ ધ્યાનમાં લો જ્યાં $\\angle C = \\angle R = 90^\\circ$ છે.\nઆપેલ છે: $\\sin B = \\sin Q \\implies \\frac{AC}{AB} = \\frac{PR}{PQ} = k$.\nતેથી $AC = k \\cdot PR$ અને $AB = k \\cdot PQ$.\nપાયથાગોરસ પ્રમેય મુજબ:\n$$BC = \\sqrt{AB^2 - AC^2}, \\quad QR = \\sqrt{PQ^2 - PR^2}$$\n$$\\frac{BC}{QR} = \\frac{k\\sqrt{PQ^2 - PR^2}}{\\sqrt{PQ^2 - PR^2}} = k$$\nઆમ $\\frac{AC}{PR} = \\frac{AB}{PQ} = \\frac{BC}{QR} = k$ હોવાથી, SSS સમરૂપતા શરત મુજબ $\\triangle ABC \\sim \\triangle PQR$ થાય.\nઅનુરૂપ ખૂણા સમાન થાય: $\\angle B = \\angle Q$.",
        btype="theory",
        bloom="Analyze",
        diff="Intermediate",
        mins=3
    ))

    # 8. NCERT Example 3
    blocks.append(make_quiz(
        "C10M_CH8_EG3",
        "NCERT Example 3: Consider △ACB, right-angled at C, in which AB = 29 units, BC = 21 units and ∠ABC = θ. Determine the value of (i) cos²θ + sin²θ and (ii) cos²θ - sin²θ.",
        "NCERT उदाहरण 3: △ACB लीजिए जिसका कोण C समकोण है, जिसमें AB = 29 इकाई, BC = 21 इकाई और ∠ABC = θ है। (i) cos²θ + sin²θ और (ii) cos²θ - sin²θ का मान ज्ञात कीजिए।",
        "NCERT ઉદાહરણ 3: △ACB ધ્યાનમાં લો, જ્યાં ખૂણો C કાટખૂણો છે, જેમાં AB = 29 એકમ, BC = 21 એકમ અને ∠ABC = θ છે. (i) cos²θ + sin²θ અને (ii) cos²θ - sin²θ નું મૂલ્ય શોધો.",
        [
            "(i) 1, (ii) 41/841",
            "(i) 1, (ii) 21/29",
            "(i) 2, (ii) 40/841",
            "(i) 1, (ii) 400/841"
        ],
        [
            "(i) 1, (ii) 41/841",
            "(i) 1, (ii) 21/29",
            "(i) 2, (ii) 40/841",
            "(i) 1, (ii) 400/841"
        ],
        [
            "(i) 1, (ii) 41/841",
            "(i) 1, (ii) 21/29",
            "(i) 2, (ii) 40/841",
            "(i) 1, (ii) 400/841"
        ],
        0,
        "In right △ACB, AC = √(AB² - BC²) = √(29² - 21²) = √(841 - 441) = √400 = 20 units.\nTherefore, sin θ = AC/AB = 20/29 and cos θ = BC/AB = 21/29.\n(i) cos²θ + sin²θ = (21/29)² + (20/29)² = (441 + 400)/841 = 841/841 = 1.\n(ii) cos²θ - sin²θ = (21/29)² - (20/29)² = (441 - 400)/841 = 41/841.",
        "समकोण △ACB में, AC = √(AB² - BC²) = √(841 - 441) = √400 = 20 इकाई।\nअतः sin θ = 20/29 और cos θ = 21/29।\n(i) cos²θ + sin²θ = (21/29)² + (20/29)² = (441 + 400)/841 = 841/841 = 1।\n(ii) cos²θ - sin²θ = 441/841 - 400/841 = 41/841।",
        "કાટકોણ △ACB માં, AC = √(AB² - BC²) = √(841 - 441) = √400 = 20 એકમ.\nતેથી sin θ = 20/29 અને cos θ = 21/29.\n(i) cos²θ + sin²θ = (21/29)² + (20/29)² = 841/841 = 1.\n(ii) cos²θ - sin²θ = (441 - 400)/841 = 41/841.",
        bloom="Apply",
        diff="Intermediate",
        mins=2
    ))

    # 9. NCERT Example 4
    blocks.append(make_quiz(
        "C10M_CH8_EG4",
        "NCERT Example 4: In a right triangle ABC, right-angled at B, if tan A = 1, verify that 2 sin A cos A = 1.",
        "NCERT उदाहरण 4: एक समकोण त्रिभुज ABC में जिसका कोण B समकोण है, यदि tan A = 1, तो सत्यापित कीजिए कि 2 sin A cos A = 1।",
        "NCERT ઉદાહરણ 4: કાટકોણ ત્રિકોણ ABC માં, જ્યાં ખૂણો B કાટખૂણો છે, જો tan A = 1 હોય, તો ચકાસો કે 2 sin A cos A = 1.",
        [
            "Verified: sin A = 1/√2, cos A = 1/√2, so 2(1/√2)(1/√2) = 1",
            "False: 2 sin A cos A = 2",
            "False: 2 sin A cos A = 1/2",
            "Cannot be verified without side lengths"
        ],
        [
            "सत्यापित: sin A = 1/√2, cos A = 1/√2, अतः 2(1/√2)(1/√2) = 1",
            "असत्य: 2 sin A cos A = 2",
            "असत्य: 2 sin A cos A = 1/2",
            "भुजाओं की लंबाई के बिना सत्यापित नहीं किया जा सकता"
        ],
        [
            "ચકાસાયેલ: sin A = 1/√2, cos A = 1/√2, તેથી 2(1/√2)(1/√2) = 1",
            "ખોટું: 2 sin A cos A = 2",
            "ખોટું: 2 sin A cos A = 1/2",
            "બાજુઓની લંબાઈ વગર ચકાસી શકાતું નથી"
        ],
        0,
        "tan A = BC/AB = 1 ⇒ BC = AB = k.\nBy Pythagoras theorem, AC = √(AB² + BC²) = √(k² + k²) = k√2.\nSo sin A = BC/AC = k/(k√2) = 1/√2 and cos A = AB/AC = 1/√2.\nTherefore, 2 sin A cos A = 2 × (1/√2) × (1/√2) = 2 × (1/2) = 1. Verified!",
        "tan A = BC/AB = 1 ⇒ BC = AB = k।\nपाइथागोरस प्रमेय से, AC = √(k² + k²) = k√2।\nअतः sin A = 1/√2 तथा cos A = 1/√2।\nइसलिए 2 sin A cos A = 2 × (1/√2) × (1/√2) = 1। सत्यापित!",
        "tan A = BC/AB = 1 ⇒ BC = AB = k.\nપાયથાગોરસ પ્રમેય મુજબ, AC = √(k² + k²) = k√2.\nતેથી sin A = 1/√2 અને cos A = 1/√2.\nઆથી 2 sin A cos A = 2 × (1/√2) × (1/√2) = 1. ચકાસાયેલ!",
        bloom="Apply",
        diff="Beginner",
        mins=2
    ))

    # 10. NCERT Example 5
    blocks.append(make_quiz(
        "C10M_CH8_EG5",
        "NCERT Example 5: In △OPQ, right-angled at P, OP = 7 cm and OQ - PQ = 1 cm. Determine the values of sin Q and cos Q.",
        "NCERT उदाहरण 5: △OPQ में जिसका कोण P समकोण है, OP = 7 सेमी और OQ - PQ = 1 सेमी। sin Q और cos Q का मान ज्ञात कीजिए।",
        "NCERT ઉદાહરણ 5: △OPQ માં, જ્યાં ખૂણો P કાટખૂણો છે, OP = 7 સેમી અને OQ - PQ = 1 સેમી છે. sin Q અને cos Q નું મૂલ્ય શોધો.",
        [
            "sin Q = 7/25, cos Q = 24/25",
            "sin Q = 24/25, cos Q = 7/25",
            "sin Q = 7/24, cos Q = 24/7",
            "sin Q = 1/25, cos Q = 7/25"
        ],
        [
            "sin Q = 7/25, cos Q = 24/25",
            "sin Q = 24/25, cos Q = 7/25",
            "sin Q = 7/24, cos Q = 24/7",
            "sin Q = 1/25, cos Q = 7/25"
        ],
        [
            "sin Q = 7/25, cos Q = 24/25",
            "sin Q = 24/25, cos Q = 7/25",
            "sin Q = 7/24, cos Q = 24/7",
            "sin Q = 1/25, cos Q = 7/25"
        ],
        0,
        "In right △OPQ, OQ² = OP² + PQ².\nSince OQ = 1 + PQ, we have:\n(1 + PQ)² = OP² + PQ²\n1 + 2PQ + PQ² = 7² + PQ²\n1 + 2PQ = 49 ⇒ 2PQ = 48 ⇒ PQ = 24 cm.\nOQ = 1 + 24 = 25 cm.\nFor angle Q: opposite side = OP = 7 cm, adjacent = PQ = 24 cm, hypotenuse = OQ = 25 cm.\nThus, sin Q = OP/OQ = 7/25, cos Q = PQ/OQ = 24/25.",
        "समकोण △OPQ में, OQ² = OP² + PQ²।\nचूँकि OQ = 1 + PQ:\n(1 + PQ)² = 7² + PQ²\n1 + 2PQ + PQ² = 49 + PQ²\n2PQ = 48 ⇒ PQ = 24 सेमी।\nOQ = 1 + 24 = 25 सेमी।\nअतः sin Q = OP/OQ = 7/25 और cos Q = PQ/OQ = 24/25।",
        "કાટકોણ △OPQ માં, OQ² = OP² + PQ².\nOQ = 1 + PQ હોવાથી:\n(1 + PQ)² = 7² + PQ²\n1 + 2PQ + PQ² = 49 + PQ²\n2PQ = 48 ⇒ PQ = 24 સેમી.\nOQ = 1 + 24 = 25 સેમી.\nઆથી sin Q = OP/OQ = 7/25 અને cos Q = PQ/OQ = 24/25.",
        bloom="Apply",
        diff="Intermediate",
        mins=2
    ))

    # 11. Exercise 8.1 Q1
    blocks.append(make_quiz(
        "C10M_CH8_EX8.1_Q1",
        "Exercise 8.1 Q1: In △ABC, right-angled at B, AB = 24 cm, BC = 7 cm. Determine: (i) sin A, cos A, (ii) sin C, cos C.",
        "प्रश्नावली 8.1 Q1: △ABC में जिसका कोण B समकोण है, AB = 24 सेमी और BC = 7 सेमी है। निम्नलिखित का मान ज्ञात कीजिए: (i) sin A, cos A, (ii) sin C, cos C।",
        "સ્વાધ્યાય 8.1 Q1: △ABC માં, ખૂણો B કાટખૂણો છે, AB = 24 સેમી, BC = 7 સેમી છે. નીચેનાના મૂલ્યો શોધો: (i) sin A, cos A, (ii) sin C, cos C.",
        [
            "(i) sin A = 7/25, cos A = 24/25; (ii) sin C = 24/25, cos C = 7/25",
            "(i) sin A = 24/25, cos A = 7/25; (ii) sin C = 7/25, cos C = 24/25",
            "(i) sin A = 7/24, cos A = 24/7; (ii) sin C = 24/7, cos C = 7/24",
            "(i) sin A = 7/25, cos A = 24/25; (ii) sin C = 7/25, cos C = 24/25"
        ],
        [
            "(i) sin A = 7/25, cos A = 24/25; (ii) sin C = 24/25, cos C = 7/25",
            "(i) sin A = 24/25, cos A = 7/25; (ii) sin C = 7/25, cos C = 24/25",
            "(i) sin A = 7/24, cos A = 24/7; (ii) sin C = 24/7, cos C = 7/24",
            "(i) sin A = 7/25, cos A = 24/25; (ii) sin C = 7/25, cos C = 24/25"
        ],
        [
            "(i) sin A = 7/25, cos A = 24/25; (ii) sin C = 24/25, cos C = 7/25",
            "(i) sin A = 24/25, cos A = 7/25; (ii) sin C = 7/25, cos C = 24/25",
            "(i) sin A = 7/24, cos A = 24/7; (ii) sin C = 24/7, cos C = 7/24",
            "(i) sin A = 7/25, cos A = 24/25; (ii) sin C = 7/25, cos C = 24/25"
        ],
        0,
        "By Pythagoras theorem, AC = √(AB² + BC²) = √(24² + 7²) = √(576 + 49) = √625 = 25 cm.\n(i) For angle A: Opposite side = BC = 7 cm, Adjacent side = AB = 24 cm, Hypotenuse = AC = 25 cm.\nsin A = BC/AC = 7/25, cos A = AB/AC = 24/25.\n(ii) For angle C: Opposite side = AB = 24 cm, Adjacent side = BC = 7 cm, Hypotenuse = AC = 25 cm.\nsin C = AB/AC = 24/25, cos C = BC/AC = 7/25.",
        "पाइथागोरस प्रमेय से, AC = √(24² + 7²) = √625 = 25 सेमी।\n(i) कोण A के लिए: सम्मुख भुजा = BC = 7, संलग्न भुजा = AB = 24, कर्ण = 25।\nsin A = 7/25, cos A = 24/25।\n(ii) कोण C के लिए: सम्मुख भुजा = AB = 24, संलग्न भुजा = BC = 7, कर्ण = 25।\nsin C = 24/25, cos C = 7/25।",
        "પાયથાગોરસ પ્રમેય મુજબ, AC = √(24² + 7²) = √625 = 25 સેમી.\n(i) ખૂણા A માટે: સામેની બાજુ = BC = 7, પાસેની બાજુ = AB = 24, કર્ણ = 25.\nsin A = 7/25, cos A = 24/25.\n(ii) ખૂણા C માટે: સામેની બાજુ = AB = 24, પાસેની બાજુ = BC = 7, કર્ણ = 25.\nsin C = 24/25, cos C = 7/25.",
        bloom="Apply",
        diff="Beginner",
        mins=2
    ))

    # 12. Exercise 8.1 Q2
    blocks.append(make_quiz(
        "C10M_CH8_EX8.1_Q2",
        "Exercise 8.1 Q2: In right triangle PQR right-angled at Q, PQ = 12 cm and PR = 13 cm. Find tan P - cot R.",
        "प्रश्नावली 8.1 Q2: समकोण त्रिभुज PQR में जिसका कोण Q समकोण है, PQ = 12 सेमी और PR = 13 सेमी है। tan P - cot R का मान ज्ञात कीजिए।",
        "સ્વાધ્યાય 8.1 Q2: કાટકોણ ત્રિકોણ PQR માં ખૂણો Q કાટખૂણો છે, PQ = 12 સેમી અને PR = 13 સેમી છે. tan P - cot R નું મૂલ્ય શોધો.",
        [
            "0",
            "1",
            "5/12",
            "-5/12"
        ],
        [
            "0",
            "1",
            "5/12",
            "-5/12"
        ],
        [
            "0",
            "1",
            "5/12",
            "-5/12"
        ],
        0,
        "By Pythagoras theorem in right △PQR:\nQR = √(PR² - PQ²) = √(13² - 12²) = √(169 - 144) = √25 = 5 cm.\nFor angle P: tan P = Opposite/Adjacent = QR/PQ = 5/12.\nFor angle R: cot R = Adjacent/Opposite = QR/PQ = 5/12.\nTherefore, tan P - cot R = 5/12 - 5/12 = 0.",
        "पाइथागोरस प्रमेय से, QR = √(13² - 12²) = √25 = 5 सेमी।\nकोण P के लिए: tan P = QR/PQ = 5/12।\nकोण R के लिए: cot R = QR/PQ = 5/12।\nअतः tan P - cot R = 5/12 - 5/12 = 0।",
        "પાયથાગોરસ પ્રમેય મુજબ, QR = √(13² - 12²) = √25 = 5 સેમી.\nખૂણા P માટે: tan P = QR/PQ = 5/12.\nખૂણા R માટે: cot R = QR/PQ = 5/12.\nતેથી, tan P - cot R = 5/12 - 5/12 = 0.",
        bloom="Apply",
        diff="Beginner",
        mins=2
    ))

    # 13. Exercise 8.1 Q3
    blocks.append(make_quiz(
        "C10M_CH8_EX8.1_Q3",
        "Exercise 8.1 Q3: If sin A = 3/4, calculate cos A and tan A.",
        "प्रश्नावली 8.1 Q3: यदि sin A = 3/4, तो cos A और tan A का मान परिकलित कीजिए।",
        "સ્વાધ્યાય 8.1 Q3: જો sin A = 3/4 હોય, તો cos A અને tan A ની ગણતરી કરો.",
        [
            "cos A = √7/4, tan A = 3/√7",
            "cos A = 4/√7, tan A = √7/3",
            "cos A = 3/5, tan A = 4/5",
            "cos A = √7/3, tan A = 3/4"
        ],
        [
            "cos A = √7/4, tan A = 3/√7",
            "cos A = 4/√7, tan A = √7/3",
            "cos A = 3/5, tan A = 4/5",
            "cos A = √7/3, tan A = 3/4"
        ],
        [
            "cos A = √7/4, tan A = 3/√7",
            "cos A = 4/√7, tan A = √7/3",
            "cos A = 3/5, tan A = 4/5",
            "cos A = √7/3, tan A = 3/4"
        ],
        0,
        "sin A = Opposite/Hypotenuse = 3/4. Let opposite = 3k, hypotenuse = 4k.\nBy Pythagoras theorem, Adjacent = √((4k)² - (3k)²) = √(16k² - 9k²) = k√7.\ncos A = Adjacent/Hypotenuse = k√7 / 4k = √7/4.\ntan A = Opposite/Adjacent = 3k / k√7 = 3/√7.",
        "sin A = लंब/कर्ण = 3/4। माना लंब = 3k, कर्ण = 4k।\nपाइथागोरस प्रमेय से, आधार = √(16k² - 9k²) = k√7।\ncos A = आधार/कर्ण = √7/4।\ntan A = लंब/आधार = 3/√7।",
        "sin A = સામેની બાજુ/કર્ણ = 3/4. ધારો કે સામેની બાજુ = 3k, કર્ણ = 4k.\nપાયથાગોરસ પ્રમેય મુજબ, પાસેની બાજુ = √(16k² - 9k²) = k√7.\ncos A = પાસેની બાજુ/કર્ણ = √7/4.\ntan A = સામેની બાજુ/પાસેની બાજુ = 3/√7.",
        bloom="Apply",
        diff="Beginner",
        mins=2
    ))

    # 14. Exercise 8.1 Q4
    blocks.append(make_quiz(
        "C10M_CH8_EX8.1_Q4",
        "Exercise 8.1 Q4: Given 15 cot A = 8, find sin A and sec A.",
        "प्रश्नावली 8.1 Q4: यदि 15 cot A = 8 हो, तो sin A और sec A का मान ज्ञात कीजिए।",
        "સ્વાધ્યાય 8.1 Q4: આપેલ છે કે 15 cot A = 8, તો sin A અને sec A શોધો.",
        [
            "sin A = 15/17, sec A = 17/8",
            "sin A = 8/17, sec A = 15/8",
            "sin A = 15/8, sec A = 17/15",
            "sin A = 17/15, sec A = 8/17"
        ],
        [
            "sin A = 15/17, sec A = 17/8",
            "sin A = 8/17, sec A = 15/8",
            "sin A = 15/8, sec A = 17/15",
            "sin A = 17/15, sec A = 8/17"
        ],
        [
            "sin A = 15/17, sec A = 17/8",
            "sin A = 8/17, sec A = 15/8",
            "sin A = 15/8, sec A = 17/15",
            "sin A = 17/15, sec A = 8/17"
        ],
        0,
        "15 cot A = 8 ⇒ cot A = 8/15.\ncot A = Adjacent/Opposite ⇒ Adjacent = 8k, Opposite = 15k.\nHypotenuse = √((8k)² + (15k)²) = √(64k² + 225k²) = √289k² = 17k.\nsin A = Opposite/Hypotenuse = 15k/17k = 15/17.\nsec A = Hypotenuse/Adjacent = 17k/8k = 17/8.",
        "15 cot A = 8 ⇒ cot A = 8/15 = आधार/लंब।\nकर्ण = √(8² + 15²) = √(64 + 225) = √289 = 17k।\nsin A = लंब/कर्ण = 15/17।\nsec A = कर्ण/आधार = 17/8।",
        "15 cot A = 8 ⇒ cot A = 8/15 = પાસેની બાજુ/સામેની બાજુ.\nકર્ણ = √(8² + 15²) = √289 = 17k.\nsin A = સામેની બાજુ/કર્ણ = 15/17.\nsec A = કર્ણ/પાસેની બાજુ = 17/8.",
        bloom="Apply",
        diff="Beginner",
        mins=2
    ))

    # 15. Exercise 8.1 Q5
    blocks.append(make_quiz(
        "C10M_CH8_EX8.1_Q5",
        "Exercise 8.1 Q5: Given sec θ = 13/12, calculate all other trigonometric ratios.",
        "प्रश्नावली 8.1 Q5: यदि sec θ = 13/12 हो, तो अन्य सभी त्रिकोणमितीय अनुपात परिकलित कीजिए।",
        "સ્વાધ્યાય 8.1 Q5: આપેલ છે કે sec θ = 13/12, તો અન્ય તમામ ત્રિકોણમિતીય ગુણોત્તરો શોધો.",
        [
            "sin θ = 5/13, cos θ = 12/13, tan θ = 5/12, cosec θ = 13/5, cot θ = 12/5",
            "sin θ = 12/13, cos θ = 5/13, tan θ = 12/5, cosec θ = 13/12, cot θ = 5/12",
            "sin θ = 5/12, cos θ = 13/12, tan θ = 5/13, cosec θ = 12/5, cot θ = 13/5",
            "sin θ = 5/13, cos θ = 12/13, tan θ = 12/5, cosec θ = 5/13, cot θ = 5/12"
        ],
        [
            "sin θ = 5/13, cos θ = 12/13, tan θ = 5/12, cosec θ = 13/5, cot θ = 12/5",
            "sin θ = 12/13, cos θ = 5/13, tan θ = 12/5, cosec θ = 13/12, cot θ = 5/12",
            "sin θ = 5/12, cos θ = 13/12, tan θ = 5/13, cosec θ = 12/5, cot θ = 13/5",
            "sin θ = 5/13, cos θ = 12/13, tan θ = 12/5, cosec θ = 5/13, cot θ = 5/12"
        ],
        [
            "sin θ = 5/13, cos θ = 12/13, tan θ = 5/12, cosec θ = 13/5, cot θ = 12/5",
            "sin θ = 12/13, cos θ = 5/13, tan θ = 12/5, cosec θ = 13/12, cot θ = 5/12",
            "sin θ = 5/12, cos θ = 13/12, tan θ = 5/13, cosec θ = 12/5, cot θ = 13/5",
            "sin θ = 5/13, cos θ = 12/13, tan θ = 12/5, cosec θ = 5/13, cot θ = 5/12"
        ],
        0,
        "sec θ = Hypotenuse/Adjacent = 13/12. Let Hypotenuse = 13k, Adjacent = 12k.\nOpposite = √((13k)² - (12k)²) = √(169k² - 144k²) = √25k² = 5k.\nTherefore:\nsin θ = 5/13, cos θ = 1/sec θ = 12/13, tan θ = 5/12,\ncosec θ = 1/sin θ = 13/5, cot θ = 1/tan θ = 12/5.",
        "sec θ = कर्ण/आधार = 13/12। लंब = √(13² - 12²) = √25 = 5k।\nअतः sin θ = 5/13, cos θ = 12/13, tan θ = 5/12, cosec θ = 13/5, cot θ = 12/5।",
        "sec θ = કર્ણ/પાસેની બાજુ = 13/12. સામેની બાજુ = √(13² - 12²) = √25 = 5k.\nતેથી sin θ = 5/13, cos θ = 12/13, tan θ = 5/12, cosec θ = 13/5, cot θ = 12/5.",
        bloom="Apply",
        diff="Beginner",
        mins=2
    ))

    # 16. Exercise 8.1 Q6
    blocks.append(make_theory(
        "C10M_CH8_EX8.1_Q6",
        "Exercise 8.1 Q6: If cos A = cos B, Show That ∠A = ∠B",
        "प्रश्नावली 8.1 Q6: यदि cos A = cos B, तो दर्शाइए कि ∠A = ∠B",
        "સ્વાધ્યાય 8.1 Q6: જો cos A = cos B હોય, તો સાબિત કરો કે ∠A = ∠B",
        "**Problem:** If $\\angle A$ and $\\angle B$ are acute angles such that $\\cos A = \\cos B$, then show that $\\angle A = \\angle B$.\n\n**Solution:**\nConsider right-angled triangle $\\triangle ABC$, where $\\angle C = 90^\\circ$.\nFrom definition of cosine:\n$$\\cos A = \\frac{\\text{Side adjacent to } \\angle A}{\\text{Hypotenuse}} = \\frac{AC}{AB}$$\n$$\\cos B = \\frac{\\text{Side adjacent to } \\angle B}{\\text{Hypotenuse}} = \\frac{BC}{AB}$$\n\nGiven $\\cos A = \\cos B$:\n$$\\frac{AC}{AB} = \\frac{BC}{AB} \\implies AC = BC$$\n\nIn $\\triangle ABC$, since sides opposite to equal angles are equal (or angles opposite to equal sides are equal):\n$$AC = BC \\implies \\angle B = \\angle A$$\nHence, $\\angle A = \\angle B$. Proved!",
        "**प्रश्न:** यदि $\\angle A$ और $\\angle B$ न्यूनकोण हैं जहाँ $\\cos A = \\cos B$, तो दर्शाइए कि $\\angle A = \\angle B$।\n\n**हल:**\nसमकोण त्रिभुज $\\triangle ABC$ लीजिए जिसका कोण $C$ समकोण ($90^\\circ$) है।\nकोसाइन की परिभाषा से:\n$$\\cos A = \\frac{AC}{AB}, \\quad \\cos B = \\frac{BC}{AB}$$\n\nदिया है $\\cos A = \\cos B$:\n$$\\frac{AC}{AB} = \\frac{BC}{AB} \\implies AC = BC$$\n\nकिसी त्रिभुज में समान भुजाओं के सम्मुख कोण बराबर होते हैं:\n$$AC = BC \\implies \\angle B = \\angle A$$\nअतः $\\angle A = \\angle B$ सिद्ध हुआ!",
        "**પ્રશ્ન:** જો $\\angle A$ અને $\\angle B$ લઘુકોણ હોય કે જેથી $\\cos A = \\cos B$, તો દર્શાવો કે $\\angle A = \\angle B$.\n\n**ઉકેલ:**\nકાટકોણ ત્રિકોણ $\\triangle ABC$ લો જેમાં $\\angle C = 90^\\circ$ છે.\nકોસાઈનની વ્યાખ્યા પરથી:\n$$\\cos A = \\frac{AC}{AB}, \\quad \\cos B = \\frac{BC}{AB}$$\n\nઆપેલ છે $\\cos A = \\cos B$:\n$$\\frac{AC}{AB} = \\frac{BC}{AB} \\implies AC = BC$$\n\nત્રિકોણમાં સમાન બાજુઓની સામેના ખૂણા સમાન હોય છે:\n$$AC = BC \\implies \\angle B = \\angle A$$\nઆમ, $\\angle A = \\angle B$ સાબિત થાય છે!",
        btype="theory",
        bloom="Understand",
        diff="Beginner",
        mins=2
    ))

    # 17. Exercise 8.1 Q7
    blocks.append(make_quiz(
        "C10M_CH8_EX8.1_Q7",
        "Exercise 8.1 Q7: If cot θ = 7/8, evaluate: (i) (1 + sin θ)(1 - sin θ) / [(1 + cos θ)(1 - cos θ)], (ii) cot²θ.",
        "प्रश्नावली 8.1 Q7: यदि cot θ = 7/8, तो मान निकालिए: (i) (1 + sin θ)(1 - sin θ) / [(1 + cos θ)(1 - cos θ)], (ii) cot²θ।",
        "સ્વાધ્યાય 8.1 Q7: જો cot θ = 7/8 હોય, તો મૂલ્ય શોધો: (i) (1 + sin θ)(1 - sin θ) / [(1 + cos θ)(1 - cos θ)], (ii) cot²θ.",
        [
            "(i) 49/64, (ii) 49/64",
            "(i) 64/49, (ii) 64/49",
            "(i) 7/8, (ii) 49/64",
            "(i) 1, (ii) 49/64"
        ],
        [
            "(i) 49/64, (ii) 49/64",
            "(i) 64/49, (ii) 64/49",
            "(i) 7/8, (ii) 49/64",
            "(i) 1, (ii) 49/64"
        ],
        [
            "(i) 49/64, (ii) 49/64",
            "(i) 64/49, (ii) 64/49",
            "(i) 7/8, (ii) 49/64",
            "(i) 1, (ii) 49/64"
        ],
        0,
        "Using algebraic identity (a + b)(a - b) = a² - b²:\n(1 + sin θ)(1 - sin θ) / [(1 + cos θ)(1 - cos θ)] = (1 - sin²θ) / (1 - cos²θ).\nSince 1 - sin²θ = cos²θ and 1 - cos²θ = sin²θ:\ncos²θ / sin²θ = (cos θ / sin θ)² = cot²θ = (7/8)² = 49/64.\n(ii) cot²θ = (7/8)² = 49/64. Both answers are 49/64!",
        "बीजगणितीय सर्वसमिका (a + b)(a - b) = a² - b² का उपयोग करने पर:\n(1 - sin²θ)/(1 - cos²θ) = cos²θ/sin²θ = cot²θ = (7/8)² = 49/64।\n(ii) cot²θ = (7/8)² = 49/64। दोनों भागों का मान 49/64 है!",
        "બીજગણિતીય નિત્યસમ (a + b)(a - b) = a² - b² નો ઉપયોગ કરતાં:\n(1 - sin²θ)/(1 - cos²θ) = cos²θ/sin²θ = cot²θ = (7/8)² = 49/64.\n(ii) cot²θ = (7/8)² = 49/64. બંને જવાબો 49/64 આવે છે!",
        bloom="Apply",
        diff="Intermediate",
        mins=2
    ))

    # 18. Exercise 8.1 Q8
    blocks.append(make_quiz(
        "C10M_CH8_EX8.1_Q8",
        "Exercise 8.1 Q8: If 3 cot A = 4, check whether (1 - tan²A)/(1 + tan²A) = cos²A - sin²A or not.",
        "प्रश्नावली 8.1 Q8: यदि 3 cot A = 4, तो जाँच कीजिए कि (1 - tan²A)/(1 + tan²A) = cos²A - sin²A है या नहीं।",
        "સ્વાધ્યાય 8.1 Q8: જો 3 cot A = 4 હોય, તો ચકાસો કે (1 - tan²A)/(1 + tan²A) = cos²A - sin²A છે કે નહીં.",
        [
            "Yes, both sides equal 7/25",
            "No, LHS = 7/25 and RHS = 1",
            "No, LHS = 16/25 and RHS = 7/25",
            "Yes, both sides equal 25/7"
        ],
        [
            "हाँ, दोनों पक्ष 7/25 के बराबर हैं",
            "नहीं, LHS = 7/25 और RHS = 1",
            "नहीं, LHS = 16/25 और RHS = 7/25",
            "हाँ, दोनों पक्ष 25/7 के बराबर हैं"
        ],
        [
            "હા, બંને બાજુ 7/25 બરાબર છે",
            "ના, ડા.બા. = 7/25 અને જ.બા. = 1",
            "ના, ડા.બા. = 16/25 અને જ.બા. = 7/25",
            "હા, બંને બાજુ 25/7 બરાબર છે"
        ],
        0,
        "3 cot A = 4 ⇒ cot A = 4/3 ⇒ tan A = 3/4.\nIn right triangle, Adjacent = 4, Opposite = 3, Hypotenuse = √(4² + 3²) = 5.\ncos A = 4/5, sin A = 3/5.\nLHS = [1 - (3/4)²] / [1 + (3/4)²] = [1 - 9/16] / [1 + 9/16] = (7/16) / (25/16) = 7/25.\nRHS = cos²A - sin²A = (4/5)² - (3/5)² = 16/25 - 9/25 = 7/25.\nSince LHS = RHS = 7/25, they are equal!",
        "3 cot A = 4 ⇒ cot A = 4/3 ⇒ tan A = 3/4।\nआधार = 4, लंब = 3, कर्ण = 5।\ncos A = 4/5, sin A = 3/5।\nLHS = (1 - 9/16)/(1 + 9/16) = (7/16)/(25/16) = 7/25।\nRHS = cos²A - sin²A = 16/25 - 9/25 = 7/25।\nचूँकि LHS = RHS = 7/25, अतः दोनों पक्ष बराबर हैं!",
        "3 cot A = 4 ⇒ cot A = 4/3 ⇒ tan A = 3/4.\nપાસેની બાજુ = 4, સામેની બાજુ = 3, કર્ણ = 5.\ncos A = 4/5, sin A = 3/5.\nડા.બા. = (1 - 9/16)/(1 + 9/16) = 7/25.\nજ.બા. = 16/25 - 9/25 = 7/25.\nડા.બા. = જ.બા. = 7/25 હોવાથી બંને સમાન છે!",
        bloom="Apply",
        diff="Intermediate",
        mins=2
    ))

    # 19. Exercise 8.1 Q9
    blocks.append(make_quiz(
        "C10M_CH8_EX8.1_Q9",
        "Exercise 8.1 Q9: In △ABC, right-angled at B, if tan A = 1/√3, find the values of: (i) sin A cos C + cos A sin C, (ii) cos A cos C - sin A sin C.",
        "प्रश्नावली 8.1 Q9: △ABC में जिसका कोण B समकोण है, यदि tan A = 1/√3, तो मान ज्ञात कीजिए: (i) sin A cos C + cos A sin C, (ii) cos A cos C - sin A sin C।",
        "સ્વાધ્યાય 8.1 Q9: △ABC માં ખૂણો B કાટખૂણો છે, જો tan A = 1/√3 હોય, તો મૂલ્ય શોધો: (i) sin A cos C + cos A sin C, (ii) cos A cos C - sin A sin C.",
        [
            "(i) 1, (ii) 0",
            "(i) 0, (ii) 1",
            "(i) 1/2, (ii) √3/2",
            "(i) 1, (ii) -1"
        ],
        [
            "(i) 1, (ii) 0",
            "(i) 0, (ii) 1",
            "(i) 1/2, (ii) √3/2",
            "(i) 1, (ii) -1"
        ],
        [
            "(i) 1, (ii) 0",
            "(i) 0, (ii) 1",
            "(i) 1/2, (ii) √3/2",
            "(i) 1, (ii) -1"
        ],
        0,
        "tan A = BC/AB = 1/√3. Let BC = 1k, AB = √3k.\nAC = √(BC² + AB²) = √(1k² + 3k²) = √4k² = 2k.\nFor angle A: sin A = 1/2, cos A = √3/2.\nFor angle C: sin C = AB/AC = √3/2, cos C = BC/AC = 1/2.\n(i) sin A cos C + cos A sin C = (1/2)(1/2) + (√3/2)(√3/2) = 1/4 + 3/4 = 4/4 = 1.\n(ii) cos A cos C - sin A sin C = (√3/2)(1/2) - (1/2)(√3/2) = √3/4 - √3/4 = 0.",
        "tan A = 1/√3 ⇒ BC = 1k, AB = √3k, AC = 2k।\nsin A = 1/2, cos A = √3/2।\nsin C = √3/2, cos C = 1/2।\n(i) (1/2)(1/2) + (√3/2)(√3/2) = 1/4 + 3/4 = 1।\n(ii) (√3/2)(1/2) - (1/2)(√3/2) = √3/4 - √3/4 = 0।",
        "tan A = 1/√3 ⇒ BC = 1k, AB = √3k, AC = 2k.\nsin A = 1/2, cos A = √3/2.\nsin C = √3/2, cos C = 1/2.\n(i) (1/2)(1/2) + (√3/2)(√3/2) = 1/4 + 3/4 = 1.\n(ii) (√3/2)(1/2) - (1/2)(√3/2) = √3/4 - √3/4 = 0.",
        bloom="Apply",
        diff="Intermediate",
        mins=2
    ))

    # 20. Exercise 8.1 Q10
    blocks.append(make_quiz(
        "C10M_CH8_EX8.1_Q10",
        "Exercise 8.1 Q10: In △PQR, right-angled at Q, PR + QR = 25 cm and PQ = 5 cm. Determine the values of sin P, cos P and tan P.",
        "प्रश्नावली 8.1 Q10: △PQR में जिसका कोण Q समकोण है, PR + QR = 25 सेमी और PQ = 5 सेमी है। sin P, cos P और tan P के मान ज्ञात कीजिए।",
        "સ્વાધ્યાય 8.1 Q10: △PQR માં ખૂણો Q કાટખૂણો છે, PR + QR = 25 સેમી અને PQ = 5 સેમી છે. sin P, cos P અને tan P ના મૂલ્યો શોધો.",
        [
            "sin P = 12/13, cos P = 5/13, tan P = 12/5",
            "sin P = 5/13, cos P = 12/13, tan P = 5/12",
            "sin P = 12/25, cos P = 5/25, tan P = 12/5",
            "sin P = 7/25, cos P = 24/25, tan P = 7/24"
        ],
        [
            "sin P = 12/13, cos P = 5/13, tan P = 12/5",
            "sin P = 5/13, cos P = 12/13, tan P = 5/12",
            "sin P = 12/25, cos P = 5/25, tan P = 12/5",
            "sin P = 7/25, cos P = 24/25, tan P = 7/24"
        ],
        [
            "sin P = 12/13, cos P = 5/13, tan P = 12/5",
            "sin P = 5/13, cos P = 12/13, tan P = 5/12",
            "sin P = 12/25, cos P = 5/25, tan P = 12/5",
            "sin P = 7/25, cos P = 24/25, tan P = 7/24"
        ],
        0,
        "Let QR = x cm, then PR = (25 - x) cm.\nBy Pythagoras theorem:\nPR² = PQ² + QR²\n(25 - x)² = 5² + x²\n625 - 50x + x² = 25 + x²\n50x = 600 ⇒ x = 12 cm (QR = 12 cm).\nPR = 25 - 12 = 13 cm.\nFor angle P: Opposite = QR = 12, Adjacent = PQ = 5, Hypotenuse = PR = 13.\nTherefore, sin P = 12/13, cos P = 5/13, tan P = 12/5.",
        "माना QR = x सेमी, तो PR = (25 - x) सेमी।\nपाइथागोरस प्रमेय से: (25 - x)² = 5² + x²\n625 - 50x + x² = 25 + x²\n50x = 600 ⇒ x = 12 सेमी (QR = 12)।\nPR = 25 - 12 = 13 सेमी।\nअतः sin P = 12/13, cos P = 5/13, tan P = 12/5।",
        "ધારો કે QR = x સેમી, તો PR = (25 - x) સેમી.\nપાયથાગોરસ પ્રમેય મુજબ: (25 - x)² = 5² + x²\n625 - 50x + x² = 25 + x²\n50x = 600 ⇒ x = 12 સેમી (QR = 12).\nPR = 25 - 12 = 13 સેમી.\nતેથી sin P = 12/13, cos P = 5/13, tan P = 12/5.",
        bloom="Apply",
        diff="Intermediate",
        mins=2
    ))

    # 21. Exercise 8.1 Q11 (All 5 True/False Subparts)
    blocks.append(make_theory(
        "C10M_CH8_EX8.1_Q11",
        "Exercise 8.1 Q11: Conceptual True / False Analysis",
        "प्रश्नावली 8.1 Q11: वैचारिक सत्य/असत्य विश्लेषण",
        "સ્વાધ્યાય 8.1 Q11: વૈચારિક ખરા/ખોટા નું વિશ્લેષણ",
        "### Exercise 8.1 Question 11: State whether the following are true or false with justification:\n\n1. **The value of tan A is always less than 1.**\n   - **FALSE.** In a right triangle, the opposite side can be longer than the adjacent side (e.g., 4/3 = 1.33 > 1). Also $\\tan 60^\\circ = \\sqrt{3} \\approx 1.732 > 1$.\n\n2. **sec A = 12/5 for some value of angle A.**\n   - **TRUE.** Since $\\sec A = \\text{Hypotenuse}/\\text{Adjacent}$ and the hypotenuse is always the longest side, $\\sec A \\ge 1$. Here $12/5 = 2.4 > 1$, which is valid.\n\n3. **cos A is the abbreviation used for the cosecant of angle A.**\n   - **FALSE.** $\\cos A$ is the abbreviation for the **cosine** of angle $A$. The abbreviation for cosecant is $\\operatorname{cosec} A$.\n\n4. **cot A is the product of cot and A.**\n   - **FALSE.** $\\cot A$ is the cotangent of the angle $A$. 'cot' separated from $A$ has no mathematical meaning.\n\n5. **sin θ = 4/3 for some angle θ.**\n   - **FALSE.** $\\sin \\theta = \\text{Opposite}/\\text{Hypotenuse}$. Since the hypotenuse is the longest side of a right triangle, the opposite side can never exceed the hypotenuse. Thus, $\\sin \\theta \\le 1$. But $4/3 = 1.33 > 1$, which is impossible.",
        "### प्रश्नावली 8.1 प्रश्न 11: कारण सहित बताइए कि कथन सत्य हैं या असत्य:\n\n1. **tan A का मान सदैव 1 से कम होता है।**\n   - **असत्य।** समकोण त्रिभुज में सम्मुख भुजा संलग्न भुजा से बड़ी हो सकती है (जैसे 4/3 = 1.33 > 1)। $\\tan 60^\\circ = \\sqrt{3} \\approx 1.732 > 1$ होता है।\n\n2. **कोण A के किसी मान के लिए sec A = 12/5 हो सकता है।**\n   - **सत्य।** चूँकि $\\sec A = \\text{कर्ण}/\\text{संलग्न भुजा}$ और कर्ण सबसे लंबी भुजा होती है, अतः $\\sec A \\ge 1$ होना चाहिए। यहाँ $12/5 = 2.4 > 1$ है, जो संभव है।\n\n3. **cos A, कोण A के cosecant के लिए प्रयुक्त एक संक्षिप्त रूप है।**\n   - **असत्य।** $\\cos A$ कोण $A$ के **cosine** का संक्षिप्त रूप है। Cosecant का संक्षिप्त रूप $\\operatorname{cosec} A$ होता है।\n\n4. **cot A, cot और A का गुणनफल होता है।**\n   - **असत्य।** $\\cot A$ कोण $A$ का कोटैंजेंट है। कोण $A$ से अलग होने पर 'cot' का कोई गणितीय अर्थ नहीं होता।\n\n5. **किसी भी कोण θ के लिए sin θ = 4/3 हो सकता है।**\n   - **असत्य।** $\\sin \\theta = \\text{लंब}/\\text{कर्ण}$। समकोण त्रिभुज में कर्ण सबसे लंबी भुजा होती है, इसलिए लंब कभी कर्ण से बड़ा नहीं हो सकता। अतः $\\sin \\theta \\le 1$ होना चाहिए, जबकि $4/3 > 1$ है।",
        "### સ્વાધ્યાય 8.1 પ્રશ્ન 11: કારણ આપી જણાવો કે નીચેના વિધાનો ખરા છે કે ખોટા:\n\n1. **tan A નું મૂલ્ય હંમેશા 1 કરતાં ઓછું હોય છે.**\n   - **ખોટું.** કાટકોણ ત્રિકોણમાં સામેની બાજુ પાસેની બાજુ કરતાં મોટી હોઈ શકે છે (દા.ત. 4/3 = 1.33 > 1). વળી $\\tan 60^\\circ = \\sqrt{3} \\approx 1.732 > 1$ છે.\n\n2. **ખૂણા A ના કોઈ મૂલ્ય માટે sec A = 12/5 હોઈ શકે.**\n   - **ખરું.** $\\sec A = \\text{કર્ણ}/\\text{પાસેની બાજુ}$ અને કર્ણ હંમેશા સૌથી મોટી બાજુ હોવાથી $\\sec A \\ge 1$ હોવો જોઈએ. અહીં $12/5 = 2.4 > 1$ હોવાથી શક્ય છે.\n\n3. **cos A એ ખૂણા A ના cosecant માટે વપરાતું સંક્ષિપ્ત રૂપ છે.**\n   - **ખોટું.** $\\cos A$ એ ખૂણા $A$ ના **cosine** નું સંક્ષિપ્ત રૂપ છે. Cosecant નું સંક્ષિપ્ત રૂપ $\\operatorname{cosec} A$ છે.\n\n4. **cot A એ cot અને A નો ગુણાકાર છે.**\n   - **ખોટું.** $\\cot A$ એ ખૂણા $A$ નો કોટેન્જન્ટ છે. $A$ વિના 'cot' નો કોઈ સ્વતંત્ર ગાણિતિક અર્થ નથી.\n\n5. **કોઈ ખૂણા θ માટે sin θ = 4/3 શક્ય છે.**\n   - **ખોટું.** $\\sin \\theta = \\text{સામેની બાજુ}/\\text{કર્ણ}$. કાટકોણ ત્રિકોણમાં કર્ણ સૌથી મોટી બાજુ હોવાથી સામેની બાજુ ક્યારેય કર્ણ કરતાં મોટી ન હોઈ શકે. તેથી $\\sin \\theta \\le 1$ જ હોય, જ્યારે $4/3 > 1$ છે.",
        btype="theory",
        bloom="Analyze",
        diff="Beginner",
        mins=3
    ))

    return blocks

# =========================================================================
# PART 2: SPECIFIC ANGLES (0°, 30°, 45°, 60°, 90°) & EXERCISE 8.2
# =========================================================================
def get_part2_blocks():
    blocks = []

    # 22. Hook: Special Angles in Architecture and Stars
    blocks.append(make_theory(
        "C10M_CH8_22",
        "The Geometry of Special Angles: Why 30°, 45°, and 60°?",
        "विशिष्ट कोणों की ज्यामिति: 30°, 45° और 60° ही क्यों?",
        "વિશેષ ખૂણાઓનું ભૂમિતિ: 30°, 45° અને 60° જ શા માટે?",
        "Why are angles like $30^\\circ$, $45^\\circ$, and $60^\\circ$ the superstar angles of engineering and architecture? \n\nBecause they originate directly from the two most symmetrical polygons in nature:\n1. **The Square:** Cut diagonally in half, a square creates a $45^\\circ - 45^\\circ - 90^\\circ$ triangle.\n2. **The Equilateral Triangle:** Cut vertically in half from top vertex to base, an equilateral triangle creates a $30^\\circ - 60^\\circ - 90^\\circ$ triangle!\n\nBecause of this perfect geometric symmetry, we do not need approximations or calculators to find their trigonometric ratios. We can derive their exact mathematical values using simple geometry!",
        "इंजीनियरिंग और वास्तुकला में $30^\\circ$, $45^\\circ$ और $60^\\circ$ जैसे कोण इतने महत्वपूर्ण क्यों हैं?\n\nक्योंकि ये प्रकृति के दो सबसे सममित बहुभुजों से सीधे उत्पन्न होते हैं:\n1. **वर्ग (Square):** विकर्ण से आधा काटने पर वर्ग $45^\\circ - 45^\\circ - 90^\\circ$ का त्रिभुज बनाता है।\n2. **समबाहु त्रिभुज (Equilateral Triangle):** शीर्ष से आधार पर लंब खींचकर आधा करने पर समबाहु त्रिभुज $30^\\circ - 60^\\circ - 90^\\circ$ का त्रिभुज बनाता है!\n\nइस पूर्ण ज्यामितीय सममिति के कारण, हमें इनके त्रिकोणमितीय अनुपातों के लिए किसी कैलकुलेटर की आवश्यकता नहीं होती। हम सरल ज्यामिति से इनके सटीक मान सिद्ध कर सकते हैं!",
        "એન્જિનિયરિંગ અને સ્થાપત્યમાં $30^\\circ$, $45^\\circ$ અને $60^\\circ$ જેવા ખૂણાઓ આટલા લોકપ્રિય શા માટે છે?\n\nકારણ કે તેઓ કુદરતના બે સૌથી સમપ્રમાણ બહુકોણમાંથી સીધા જ ઉદ્ભવે છે:\n1. **ચોરસ:** વિકર્ણથી અડધો કાપતાં ચોરસમાંથી $45^\\circ - 45^\\circ - 90^\\circ$ નો કાટકોણ ત્રિકોણ બને છે.\n2. **સમબાજુ ત્રિકોણ:** શિરોબિંદુથી લંબ દોરી અડધો કરતાં તેમાંથી $30^\\circ - 60^\\circ - 90^\\circ$ નો ત્રિકોણ બને છે!\n\nઆ સંપૂર્ણ ભૌમિતિક સંમિતિના કારણે આપણને કોઈ કેલ્ક્યુલેટરની જરૂર પડતી નથી. આપણે સરળ ભૂમિતિ દ્વારા તેમના ચોક્કસ મૂલ્યો મેળવી શકીએ છીએ!",
        btype="hook",
        bloom="Understand",
        diff="Beginner",
        mins=3
    ))

    # 23. Discovery: Geometric Derivation of 45°, 30°, and 60°
    blocks.append(make_theory(
        "C10M_CH8_23",
        "Discovery: Deriving Values for 45°, 30°, and 60°",
        "खोज: 45°, 30° और 60° के मानों की ज्यामितीय व्युत्पत्ति",
        "શોધ: 45°, 30° અને 60° ના મૂલ્યોની ભૌમિતિક સાબિતી",
        "### 1. Ratios of 45° (Isosceles Right Triangle)\nConsider an isosceles right triangle with base = $a$ and height = $a$.\nBy Pythagoras theorem, Hypotenuse = $\\sqrt{a^2 + a^2} = a\\sqrt{2}$.\n$$\\sin 45^\\circ = \\frac{a}{a\\sqrt{2}} = \\frac{1}{\\sqrt{2}}, \\quad \\cos 45^\\circ = \\frac{a}{a\\sqrt{2}} = \\frac{1}{\\sqrt{2}}, \\quad \\tan 45^\\circ = \\frac{a}{a} = 1$$\n\n### 2. Ratios of 30° and 60° (Equilateral Triangle)\nConsider an equilateral triangle $ABC$ with each side of length $2a$. Draw altitude $AD \\perp BC$.\nThen $BD = a$, and $\\angle BAD = 30^\\circ$, $\\angle B = 60^\\circ$.\nBy Pythagoras theorem: $AD = \\sqrt{(2a)^2 - a^2} = \\sqrt{3a^2} = a\\sqrt{3}$.\n- **For 30°:** Opposite = $BD = a$, Adjacent = $AD = a\\sqrt{3}$, Hypotenuse = $2a$.\n  $$\\sin 30^\\circ = \\frac{a}{2a} = \\frac{1}{2}, \\quad \\cos 30^\\circ = \\frac{a\\sqrt{3}}{2a} = \\frac{\\sqrt{3}}{2}, \\quad \\tan 30^\\circ = \\frac{a}{a\\sqrt{3}} = \\frac{1}{\\sqrt{3}}$$\n- **For 60°:** Opposite = $AD = a\\sqrt{3}$, Adjacent = $BD = a$, Hypotenuse = $2a$.\n  $$\\sin 60^\\circ = \\frac{\\sqrt{3}}{2}, \\quad \\cos 60^\\circ = \\frac{1}{2}, \\quad \\tan 60^\\circ = \\sqrt{3}$$\n\n### 3. Limiting Cases: 0° and 90°\n- As angle $\\theta \\to 0^\\circ$, Opposite side shrinks to $0$ and Adjacent side approaches Hypotenuse. Thus $\\sin 0^\\circ = 0, \\cos 0^\\circ = 1, \\tan 0^\\circ = 0$.\n- As angle $\\theta \\to 90^\\circ$, Adjacent side shrinks to $0$ and Opposite side equals Hypotenuse. Thus $\\sin 90^\\circ = 1, \\cos 90^\\circ = 0, \\tan 90^\\circ = \\text{Not Defined}$.",
        "### 1. 45° के अनुपात (समद्विबाहु समकोण त्रिभुज)\nआधार = $a$, लंब = $a$। कर्ण = $\\sqrt{a^2 + a^2} = a\\sqrt{2}$।\n$$\\sin 45^\\circ = \\frac{1}{\\sqrt{2}}, \\quad \\cos 45^\\circ = \\frac{1}{\\sqrt{2}}, \\quad \\tan 45^\\circ = 1$$\n\n### 2. 30° और 60° के अनुपात (समबाहु त्रिभुज)\n$2a$ भुजा वाला समबाहु त्रिभुज लें। शीर्षलंब $AD \\perp BC$ खींचने पर $BD = a$ और $AD = a\\sqrt{3}$।\n- **30° के लिए:** $\\sin 30^\\circ = \\frac{1}{2}, \\quad \\cos 30^\\circ = \\frac{\\sqrt{3}}{2}, \\quad \\tan 30^\\circ = \\frac{1}{\\sqrt{3}}$\n- **60° के लिए:** $\\sin 60^\\circ = \\frac{\\sqrt{3}}{2}, \\quad \\cos 60^\\circ = \\frac{1}{2}, \\quad \\tan 60^\\circ = \\sqrt{3}$\n\n### 3. सीमांत स्थितियाँ: 0° और 90°\n- जब कोण $0^\\circ$ की ओर अग्रसर होता है, लंब $0$ हो जाता है और आधार कर्ण के बराबर होता है: $\\sin 0^\\circ = 0, \\cos 0^\\circ = 1, \\tan 0^\\circ = 0$।\n- जब कोण $90^\\circ$ की ओर अग्रसर होता है, आधार $0$ हो जाता है: $\\sin 90^\\circ = 1, \\cos 90^\\circ = 0, \\tan 90^\\circ = \\text{अपरिभाषित}$।",
        "### 1. 45° ના ગુણોત્તરો (સમદ્વિબાજુ કાટકોણ ત્રિકોણ)\nપાયો = $a$, લંબ = $a$. કર્ણ = $a\\sqrt{2}$.\n$$\\sin 45^\\circ = \\frac{1}{\\sqrt{2}}, \\quad \\cos 45^\\circ = \\frac{1}{\\sqrt{2}}, \\quad \\tan 45^\\circ = 1$$\n\n### 2. 30° અને 60° ના ગુણોત્તરો (સમબાજુ ત્રિકોણ)\n$2a$ બાજુવાળો સમબાજુ ત્રિકોણ લો. વેધ $AD$ દોરતાં $BD = a$ અને $AD = a\\sqrt{3}$.\n- **30° માટે:** $\\sin 30^\\circ = \\frac{1}{2}, \\quad \\cos 30^\\circ = \\frac{\\sqrt{3}}{2}, \\quad \\tan 30^\\circ = \\frac{1}{\\sqrt{3}}$\n- **60° માટે:** $\\sin 60^\\circ = \\frac{\\sqrt{3}}{2}, \\quad \\cos 60^\\circ = \\frac{1}{2}, \\quad \\tan 60^\\circ = \\sqrt{3}$\n\n### 3. સીમાંત પરિસ્થિતિઓ: 0° અને 90°\n- જ્યારે ખૂણો $0^\\circ$ બને છે ત્યારે સામેની બાજુ $0$ બને છે: $\\sin 0^\\circ = 0, \\cos 0^\\circ = 1, \\tan 0^\\circ = 0$.\n- જ્યારે ખૂણો $90^\\circ$ બને છે ત્યારે પાસેની બાજુ $0$ બને છે: $\\sin 90^\\circ = 1, \\cos 90^\\circ = 0, \\tan 90^\\circ = \\text{અવ્યાખ્યાયિત}$.",
        btype="discovery",
        bloom="Analyze",
        diff="Intermediate",
        mins=4
    ))

    # 24. Theory: The Master Values Table
    blocks.append(make_theory(
        "C10M_CH8_24",
        "The Master Values Table: 0°, 30°, 45°, 60°, and 90°",
        "विशिष्ट कोणों की मास्टर सारणी: 0°, 30°, 45°, 60° और 90°",
        "વિશિષ્ટ ખૂણાઓનું માસ્ટર કોષ્ટક: 0°, 30°, 45°, 60° અને 90°",
        "### Complete Trigonometric Table\n\n| Ratio / Angle | 0° | 30° | 45° | 60° | 90° |\n| :---: | :---: | :---: | :---: | :---: | :---: |\n| **sin θ** | 0 | 1/2 | 1/√2 | √3/2 | 1 |\n| **cos θ** | 1 | √3/2 | 1/√2 | 1/2 | 0 |\n| **tan θ** | 0 | 1/√3 | 1 | √3 | Not Defined |\n| **cosec θ** | Not Defined | 2 | √2 | 2/√3 | 1 |\n| **sec θ** | 1 | 2/√3 | √2 | 2 | Not Defined |\n| **cot θ** | Not Defined | √3 | 1 | 1/√3 | 0 |\n\n### Important Behavioral Patterns to Remember for Board Exams:\n1. **sin θ increases** from $0$ to $1$ as $\\theta$ increases from $0^\\circ$ to $90^\\circ$.\n2. **cos θ decreases** from $1$ to $0$ as $\\theta$ increases from $0^\\circ$ to $90^\\circ$.\n3. At $\\theta = 45^\\circ$, $\\sin 45^\\circ = \\cos 45^\\circ = \\frac{1}{\\sqrt{2}}$ and $\\tan 45^\\circ = \\cot 45^\\circ = 1$.\n4. Notice that the $\\cos$ row is simply the $\\sin$ row written in reverse order!",
        "### पूर्ण त्रिकोणमितीय सारणी\n\n| अनुपात / कोण | 0° | 30° | 45° | 60° | 90° |\n| :---: | :---: | :---: | :---: | :---: | :---: |\n| **sin θ** | 0 | 1/2 | 1/√2 | √3/2 | 1 |\n| **cos θ** | 1 | √3/2 | 1/√2 | 1/2 | 0 |\n| **tan θ** | 0 | 1/√3 | 1 | √3 | अपरिभाषित |\n| **cosec θ** | अपरिभाषित | 2 | √2 | 2/√3 | 1 |\n| **sec θ** | 1 | 2/√3 | √2 | 2 | अपरिभाषित |\n| **cot θ** | अपरिभाषित | √3 | 1 | 1/√3 | 0 |\n\n### बोर्ड परीक्षा हेतु महत्वपूर्ण नियम:\n1. जैसे-जैसे $\\theta$ का मान $0^\\circ$ से $90^\\circ$ बढ़ता है, **sin θ का मान 0 से 1 तक बढ़ता है**।\n2. जैसे-जैसे $\\theta$ का मान $0^\\circ$ से $90^\\circ$ बढ़ता है, **cos θ का मान 1 से 0 तक घटता है**।\n3. $45^\\circ$ पर $\\sin 45^\\circ = \\cos 45^\\circ = 1/\\sqrt{2}$ और $\\tan 45^\\circ = \\cot 45^\\circ = 1$ होता है।\n4. ध्यान दें: $\\cos$ की पंक्ति वास्तव में $\\sin$ की पंक्ति का उलटा क्रम है!",
        "### સંપૂર્ણ ત્રિકોણમિતીય કોષ્ટક\n\n| ગુણોત્તર / ખૂણો | 0° | 30° | 45° | 60° | 90° |\n| :---: | :---: | :---: | :---: | :---: | :---: |\n| **sin θ** | 0 | 1/2 | 1/√2 | √3/2 | 1 |\n| **cos θ** | 1 | √3/2 | 1/√2 | 1/2 | 0 |\n| **tan θ** | 0 | 1/√3 | 1 | √3 | અવ્યાખ્યાયિત |\n| **cosec θ** | અવ્યાખ્યાયિત | 2 | √2 | 2/√3 | 1 |\n| **sec θ** | 1 | 2/√3 | √2 | 2 | અવ્યાખ્યાયિત |\n| **cot θ** | અવ્યાખ્યાયિત | √3 | 1 | 1/√3 | 0 |\n\n### બોર્ડ પરીક્ષા માટે મહત્વના નિયમો:\n1. જેમ જેમ ખૂણો $\\theta$, $0^\\circ$ થી $90^\\circ$ વધે છે, તેમ **sin θ નું મૂલ્ય 0 થી 1 વધે છે**.\n2. જેમ જેમ ખૂણો $\\theta$, $0^\\circ$ થી $90^\\circ$ વધે છે, તેમ **cos θ નું મૂલ્ય 1 થી 0 ઘટે છે**.\n3. $45^\\circ$ આગળ $\\sin 45^\\circ = \\cos 45^\\circ = 1/\\sqrt{2}$ અને $\\tan 45^\\circ = \\cot 45^\\circ = 1$ થાય છે.\n4. નોંધ: $\\cos$ ની હરોળ એ $\\sin$ ની હરોળનો ઊલટો ક્રમ છે!",
        btype="theory",
        bloom="Remember",
        diff="Beginner",
        mins=3
    ))

    # 25. Teacher Tip: The Left-Hand Palm Trick
    blocks.append(make_theory(
        "C10M_CH8_25",
        "Teacher Tip: The 5-Finger Palm Trick to Recreate the Table in 5 Seconds",
        "शिक्षक युक्ति: 5 सेकंड में सारणी बनाने की हथेली ट्रिक",
        "શિક્ષકની સલાહ: માત્ર 5 સેકન્ડમાં કોષ્ટક બનાવવાની હથેળી ટ્રીક",
        "Forget rote memorization! Open your left hand facing you:\n- **Thumb:** $0^\\circ$\n- **Index Finger:** $30^\\circ$\n- **Middle Finger:** $45^\\circ$\n- **Ring Finger:** $60^\\circ$\n- **Little Finger:** $90^\\circ$\n\n### The Golden Formulas:\n$$\\sin \\theta = \\frac{\\sqrt{\\text{Number of fingers BELOW}}}{2}$$\n$$\\cos \\theta = \\frac{\\sqrt{\\text{Number of fingers ABOVE}}}{2}$$\n$$\\tan \\theta = \\sqrt{\\frac{\\text{Fingers BELOW}}{\\text{Fingers ABOVE}}}$$\n\n*Quick Check for 60° (Ring Finger):*\n- Fingers below = 3 (Thumb, Index, Middle) $\\implies \\sin 60^\\circ = \\frac{\\sqrt{3}}{2}$.\n- Fingers above = 1 (Little finger) $\\implies \\cos 60^\\circ = \\frac{\\sqrt{1}}{2} = \\frac{1}{2}$.\n- $\\tan 60^\\circ = \\sqrt{3/1} = \\sqrt{3}$. Instant and 100% foolproof in exams!",
        "रटने की कोई आवश्यकता नहीं है! अपनी बाईं हथेली को अपने सामने खोलें:\n- **अंगूठा:** $0^\\circ$\n- **तर्जनी:** $30^\\circ$\n- **मध्यमा:** $45^\\circ$\n- **अनामिका:** $60^\\circ$\n- **कनिष्ठिका:** $90^\\circ$\n\n### जादुई सूत्र:\n$$\\sin \\theta = \\frac{\\sqrt{\\text{नीचे की उँगलियों की संख्या}}}{2}$$\n$$\\cos \\theta = \\frac{\\sqrt{\\text{ऊपर की उँगलियों की संख्या}}}{2}$$\n$$\\tan \\theta = \\sqrt{\\frac{\\text{नीचे की उँगलियाँ}}{\\text{ऊपर की उँगलियाँ}}}$$\n\n*60° के लिए त्वरित जाँच (अनामिका):*\n- नीचे 3 उँगलियाँ हैं $\\implies \\sin 60^\\circ = \\frac{\\sqrt{3}}{2}$।\n- ऊपर 1 उँगली है $\\implies \\cos 60^\\circ = \\frac{\\sqrt{1}}{2} = \\frac{1}{2}$।\n- $\\tan 60^\\circ = \\sqrt{3/1} = \\sqrt{3}$। परीक्षा में समय बचाने की अचूक विधि!",
        "ગોખવાની બિલકુલ જરૂર નથી! તમારી ડાબી હથેળી તમારી સામે રાખો:\n- **અંગૂઠો:** $0^\\circ$\n- **પહેલી આંગળી:** $30^\\circ$\n- **વચલી આંગળી:** $45^\\circ$\n- **અનામિકા:** $60^\\circ$\n- **ટચલી આંગળી:** $90^\\circ$\n\n### જાદુઈ સૂત્રો:\n$$\\sin \\theta = \\frac{\\sqrt{\\text{નીચેની આંગળીઓની સંખ્યા}}}{2}$$\n$$\\cos \\theta = \\frac{\\sqrt{\\text{ઉપરની આંગળીઓની સંખ્યા}}}{2}$$\n$$\\tan \\theta = \\sqrt{\\frac{\\text{નીચેની આંગળીઓ}}{\\text{ઉપરની આંગળીઓ}}}$$\n\n*60° માટે ચકાસણી (અનામિકા):*\n- નીચે 3 આંગળીઓ છે $\\implies \\sin 60^\\circ = \\frac{\\sqrt{3}}{2}$.\n- ઉપર 1 આંગળી છે $\\implies \\cos 60^\\circ = \\frac{\\sqrt{1}}{2} = \\frac{1}{2}$.\n- $\\tan 60^\\circ = \\sqrt{3/1} = \\sqrt{3}$. પરીક્ષામાં રોકડિયા માર્ક્સ મેળવવાની બેસ્ટ ટ્રીક!",
        btype="teacher_tip",
        bloom="Remember",
        diff="Beginner",
        mins=2
    ))

    # 26. NCERT Example 6
    blocks.append(make_quiz(
        "C10M_CH8_EG6",
        "NCERT Example 6: In △ABC, right-angled at B, AB = 5 cm and ∠ACB = 30°. Determine the lengths of the sides BC and AC.",
        "NCERT उदाहरण 6: △ABC में जिसका कोण B समकोण है, AB = 5 सेमी और ∠ACB = 30° है। भुजाओं BC और AC की लंबाइयाँ ज्ञात कीजिए।",
        "NCERT ઉદાહરણ 6: △ABC માં ખૂણો B કાટખૂણો છે, AB = 5 સેમી અને ∠ACB = 30° છે. બાજુઓ BC અને AC ની લંબાઈ શોધો.",
        [
            "BC = 5√3 cm, AC = 10 cm",
            "BC = 10 cm, AC = 5√3 cm",
            "BC = 5 cm, AC = 10√3 cm",
            "BC = 5/√3 cm, AC = 10 cm"
        ],
        [
            "BC = 5√3 cm, AC = 10 cm",
            "BC = 10 cm, AC = 5√3 cm",
            "BC = 5 cm, AC = 10√3 cm",
            "BC = 5/√3 cm, AC = 10 cm"
        ],
        [
            "BC = 5√3 cm, AC = 10 cm",
            "BC = 10 cm, AC = 5√3 cm",
            "BC = 5 cm, AC = 10√3 cm",
            "BC = 5/√3 cm, AC = 10 cm"
        ],
        0,
        "For angle C = 30°:\ntan 30° = AB/BC ⇒ 1/√3 = 5/BC ⇒ BC = 5√3 cm.\nsin 30° = AB/AC ⇒ 1/2 = 5/AC ⇒ AC = 10 cm.\nAlternatively, by Pythagoras: AC = √(AB² + BC²) = √(25 + 75) = √100 = 10 cm.",
        "कोण C = 30° के लिए:\ntan 30° = AB/BC ⇒ 1/√3 = 5/BC ⇒ BC = 5√3 सेमी।\nsin 30° = AB/AC ⇒ 1/2 = 5/AC ⇒ AC = 10 सेमी।",
        "ખૂણા C = 30° માટે:\ntan 30° = AB/BC ⇒ 1/√3 = 5/BC ⇒ BC = 5√3 સેમી.\nsin 30° = AB/AC ⇒ 1/2 = 5/AC ⇒ AC = 10 સેમી.",
        bloom="Apply",
        diff="Beginner",
        mins=2
    ))

    # 27. NCERT Example 7
    blocks.append(make_quiz(
        "C10M_CH8_EG7",
        "NCERT Example 7: In △PQR, right-angled at Q, PQ = 3 cm and PR = 6 cm. Determine ∠QPR and ∠PRQ.",
        "NCERT उदाहरण 7: △PQR में जिसका कोण Q समकोण है, PQ = 3 सेमी और PR = 6 सेमी है। ∠QPR और ∠PRQ का मान ज्ञात कीजिए।",
        "NCERT ઉદાહરણ 7: △PQR માં ખૂણો Q કાટખૂણો છે, PQ = 3 સેમી અને PR = 6 સેમી છે. ∠QPR અને ∠PRQ ના મૂલ્યો નક્કી કરો.",
        [
            "∠PRQ = 30°, ∠QPR = 60°",
            "∠PRQ = 60°, ∠QPR = 30°",
            "∠PRQ = 45°, ∠QPR = 45°",
            "∠PRQ = 30°, ∠QPR = 30°"
        ],
        [
            "∠PRQ = 30°, ∠QPR = 60°",
            "∠PRQ = 60°, ∠QPR = 30°",
            "∠PRQ = 45°, ∠QPR = 45°",
            "∠PRQ = 30°, ∠QPR = 30°"
        ],
        [
            "∠PRQ = 30°, ∠QPR = 60°",
            "∠PRQ = 60°, ∠QPR = 30°",
            "∠PRQ = 45°, ∠QPR = 45°",
            "∠PRQ = 30°, ∠QPR = 30°"
        ],
        0,
        "sin R = PQ/PR = 3/6 = 1/2.\nSince sin 30° = 1/2, we have ∠PRQ = 30°.\nSince the sum of angles in a triangle is 180°:\n∠QPR = 180° - (90° + 30°) = 60°.",
        "sin R = PQ/PR = 3/6 = 1/2।\nचूँकि sin 30° = 1/2, अतः ∠PRQ = 30°।\nत्रिभुज के कोणों का योग: ∠QPR = 180° - 120° = 60°।",
        "sin R = PQ/PR = 3/6 = 1/2.\nsin 30° = 1/2 હોવાથી ∠PRQ = 30°.\nત્રિકોણના ત્રણેય ખૂણાનો સરવાળો 180°: ∠QPR = 180° - 120° = 60°.",
        bloom="Apply",
        diff="Beginner",
        mins=2
    ))

    # 28. NCERT Example 8
    blocks.append(make_quiz(
        "C10M_CH8_EG8",
        "NCERT Example 8: If sin(A - B) = 1/2, cos(A + B) = 1/2, where 0° < A + B ≤ 90° and A > B, find A and B.",
        "NCERT उदाहरण 8: यदि sin(A - B) = 1/2, cos(A + B) = 1/2, जहाँ 0° < A + B ≤ 90° तथा A > B, तो A और B ज्ञात कीजिए।",
        "NCERT ઉદાહરણ 8: જો sin(A - B) = 1/2, cos(A + B) = 1/2, જ્યાં 0° < A + B ≤ 90° અને A > B, તો A અને B શોધો.",
        [
            "A = 45°, B = 15°",
            "A = 60°, B = 30°",
            "A = 50°, B = 20°",
            "A = 45°, B = 45°"
        ],
        [
            "A = 45°, B = 15°",
            "A = 60°, B = 30°",
            "A = 50°, B = 20°",
            "A = 45°, B = 45°"
        ],
        [
            "A = 45°, B = 15°",
            "A = 60°, B = 30°",
            "A = 50°, B = 20°",
            "A = 45°, B = 45°"
        ],
        0,
        "sin(A - B) = 1/2 ⇒ A - B = 30°  ... (1)\ncos(A + B) = 1/2 ⇒ A + B = 60°  ... (2)\nAdding equations (1) and (2):\n2A = 90° ⇒ A = 45°.\nSubstituting A = 45° into (2):\n45° + B = 60° ⇒ B = 15°.",
        "sin(A - B) = 1/2 ⇒ A - B = 30° ... (1)\ncos(A + B) = 1/2 ⇒ A + B = 60° ... (2)\nसमीकरण (1) और (2) को जोड़ने पर:\n2A = 90° ⇒ A = 45°।\nB = 60° - 45° = 15°।",
        "sin(A - B) = 1/2 ⇒ A - B = 30° ... (1)\ncos(A + B) = 1/2 ⇒ A + B = 60° ... (2)\nબંને સમીકરણોનો સરવાળો કરતાં:\n2A = 90° ⇒ A = 45°.\nB = 60° - 45° = 15°.",
        bloom="Apply",
        diff="Intermediate",
        mins=2
    ))

    # 29. Exercise 8.2 Q1(i)
    blocks.append(make_quiz(
        "C10M_CH8_EX8.2_Q1_1",
        "Exercise 8.2 Q1(i): Evaluate: sin 60° cos 30° + sin 30° cos 60°.",
        "प्रश्नावली 8.2 Q1(i): मान निकालिए: sin 60° cos 30° + sin 30° cos 60°।",
        "સ્વાધ્યાય 8.2 Q1(i): મૂલ્ય શોધો: sin 60° cos 30° + sin 30° cos 60°.",
        [
            "1",
            "0",
            "1/2",
            "√3/2"
        ],
        [
            "1",
            "0",
            "1/2",
            "√3/2"
        ],
        [
            "1",
            "0",
            "1/2",
            "√3/2"
        ],
        0,
        "sin 60° = √3/2, cos 30° = √3/2, sin 30° = 1/2, cos 60° = 1/2.\nExpression = (√3/2)(√3/2) + (1/2)(1/2) = 3/4 + 1/4 = 4/4 = 1.",
        "मान रखने पर: (√3/2)(√3/2) + (1/2)(1/2) = 3/4 + 1/4 = 1।",
        "કિંમતો મૂકતાં: (√3/2)(√3/2) + (1/2)(1/2) = 3/4 + 1/4 = 1.",
        bloom="Apply",
        diff="Beginner",
        mins=1
    ))

    # 30. Exercise 8.2 Q1(ii)
    blocks.append(make_quiz(
        "C10M_CH8_EX8.2_Q1_2",
        "Exercise 8.2 Q1(ii): Evaluate: 2 tan²45° + cos²30° - sin²60°.",
        "प्रश्नावली 8.2 Q1(ii): मान निकालिए: 2 tan²45° + cos²30° - sin²60°।",
        "સ્વાધ્યાય 8.2 Q1(ii): મૂલ્ય શોધો: 2 tan²45° + cos²30° - sin²60°.",
        [
            "2",
            "1",
            "0",
            "√3"
        ],
        [
            "2",
            "1",
            "0",
            "√3"
        ],
        [
            "2",
            "1",
            "0",
            "√3"
        ],
        0,
        "tan 45° = 1, cos 30° = √3/2, sin 60° = √3/2.\nExpression = 2(1)² + (√3/2)² - (√3/2)² = 2 + 3/4 - 3/4 = 2.",
        "मान रखने पर: 2(1)² + (√3/2)² - (√3/2)² = 2 + 3/4 - 3/4 = 2।",
        "કિંમતો મૂકતાં: 2(1)² + (√3/2)² - (√3/2)² = 2 + 3/4 - 3/4 = 2.",
        bloom="Apply",
        diff="Beginner",
        mins=1
    ))

    # 31. Exercise 8.2 Q1(iii)
    blocks.append(make_quiz(
        "C10M_CH8_EX8.2_Q1_3",
        "Exercise 8.2 Q1(iii): Evaluate: cos 45° / (sec 30° + cosec 30°).",
        "प्रश्नावली 8.2 Q1(iii): मान निकालिए: cos 45° / (sec 30° + cosec 30°)।",
        "સ્વાધ્યાય 8.2 Q1(iii): મૂલ્ય શોધો: cos 45° / (sec 30° + cosec 30°).",
        [
            "(3√2 - √6) / 8",
            "(√6 - √2) / 4",
            "(3√2 + √6) / 8",
            "√3 / (2√2 + 2)"
        ],
        [
            "(3√2 - √6) / 8",
            "(√6 - √2) / 4",
            "(3√2 + √6) / 8",
            "√3 / (2√2 + 2)"
        ],
        [
            "(3√2 - √6) / 8",
            "(√6 - √2) / 4",
            "(3√2 + √6) / 8",
            "√3 / (2√2 + 2)"
        ],
        0,
        "cos 45° = 1/√2, sec 30° = 2/√3, cosec 30° = 2.\nDenominator = 2/√3 + 2 = (2 + 2√3)/√3 = 2(√3 + 1)/√3.\nExpression = (1/√2) / [2(√3 + 1)/√3] = √3 / [2√2(√3 + 1)] = √3 / [2(√6 + √2)].\nRationalize denominator by multiplying numerator and denominator by (√6 - √2):\n√3(√6 - √2) / [2(6 - 2)] = (√18 - √6) / (2 × 4) = (3√2 - √6) / 8.",
        "मान रखने पर: (1/√2) / (2/√3 + 2) = √3 / [2(√6 + √2)]।\n(√6 - √2) से अंश व हर में गुणा करके परिमेयकरण करने पर:\n(√18 - √6) / [2(6 - 2)] = (3√2 - √6) / 8।",
        "કિંમતો મૂકતાં: (1/√2) / (2/√3 + 2) = √3 / [2(√6 + √2)].\n(√6 - √2) વડે અંશ અને છેદને ગુણી સંમેયીકરણ કરતાં:\n(3√2 - √6) / 8.",
        bloom="Apply",
        diff="Intermediate",
        mins=3
    ))

    # 32. Exercise 8.2 Q1(iv)
    blocks.append(make_quiz(
        "C10M_CH8_EX8.2_Q1_4",
        "Exercise 8.2 Q1(iv): Evaluate: (sin 30° + tan 45° - cosec 60°) / (sec 30° + cos 60° + cot 45°).",
        "प्रश्नावली 8.2 Q1(iv): मान निकालिए: (sin 30° + tan 45° - cosec 60°) / (sec 30° + cos 60° + cot 45°)।",
        "સ્વાધ્યાય 8.2 Q1(iv): મૂલ્ય શોધો: (sin 30° + tan 45° - cosec 60°) / (sec 30° + cos 60° + cot 45°).",
        [
            "(43 - 24√3) / 11",
            "(43 + 24√3) / 11",
            "(24√3 - 43) / 11",
            "1"
        ],
        [
            "(43 - 24√3) / 11",
            "(43 + 24√3) / 11",
            "(24√3 - 43) / 11",
            "1"
        ],
        [
            "(43 - 24√3) / 11",
            "(43 + 24√3) / 11",
            "(24√3 - 43) / 11",
            "1"
        ],
        0,
        "Numerator = 1/2 + 1 - 2/√3 = 3/2 - 2/√3 = (3√3 - 4) / 2√3.\nDenominator = 2/√3 + 1/2 + 1 = 2/√3 + 3/2 = (4 + 3√3) / 2√3 = (3√3 + 4) / 2√3.\nFraction = (3√3 - 4) / (3√3 + 4).\nRationalize by multiplying by (3√3 - 4):\n(3√3 - 4)² / [(3√3)² - 4²] = (27 - 24√3 + 16) / (27 - 16) = (43 - 24√3) / 11.",
        "अंश = (3√3 - 4) / 2√3, हर = (3√3 + 4) / 2√3।\nभिन्न = (3√3 - 4) / (3√3 + 4)।\nपरिमेयकरण करने पर:\n(3√3 - 4)² / (27 - 16) = (27 + 16 - 24√3) / 11 = (43 - 24√3) / 11।",
        "અંશ = (3√3 - 4) / 2√3, છેદ = (3√3 + 4) / 2√3.\nભાગાકાર = (3√3 - 4) / (3√3 + 4).\nસંમેયીકરણ કરતાં:\n(3√3 - 4)² / 11 = (43 - 24√3) / 11.",
        bloom="Apply",
        diff="Intermediate",
        mins=3
    ))

    # 33. Exercise 8.2 Q1(v)
    blocks.append(make_quiz(
        "C10M_CH8_EX8.2_Q1_5",
        "Exercise 8.2 Q1(v): Evaluate: (5 cos²60° + 4 sec²30° - tan²45°) / (sin²30° + cos²30°).",
        "प्रश्नावली 8.2 Q1(v): मान निकालिए: (5 cos²60° + 4 sec²30° - tan²45°) / (sin²30° + cos²30°)।",
        "સ્વાધ્યાય 8.2 Q1(v): મૂલ્ય શોધો: (5 cos²60° + 4 sec²30° - tan²45°) / (sin²30° + cos²30°).",
        [
            "67/12",
            "55/12",
            "67/16",
            "1"
        ],
        [
            "67/12",
            "55/12",
            "67/16",
            "1"
        ],
        [
            "67/12",
            "55/12",
            "67/16",
            "1"
        ],
        0,
        "cos 60° = 1/2, sec 30° = 2/√3, tan 45° = 1, sin 30° = 1/2, cos 30° = √3/2.\nDenominator = sin²30° + cos²30° = (1/2)² + (√3/2)² = 1/4 + 3/4 = 1.\nNumerator = 5(1/2)² + 4(2/√3)² - 1² = 5(1/4) + 4(4/3) - 1 = 5/4 + 16/3 - 1.\nTaking LCM = 12: (15 + 64 - 12) / 12 = 67/12.\nResult = (67/12) / 1 = 67/12.",
        "हर = sin²30° + cos²30° = 1/4 + 3/4 = 1।\nअंश = 5(1/4) + 4(4/3) - 1 = 5/4 + 16/3 - 1 = (15 + 64 - 12)/12 = 67/12।\nअतः मान = 67/12।",
        "છેદ = sin²30° + cos²30° = 1/4 + 3/4 = 1.\nઅંશ = 5(1/4) + 4(4/3) - 1 = 5/4 + 16/3 - 1 = (15 + 64 - 12)/12 = 67/12.\nઆમ પરિણામ = 67/12.",
        bloom="Apply",
        diff="Intermediate",
        mins=2
    ))

    # 34. Exercise 8.2 Q2(i)
    blocks.append(make_quiz(
        "C10M_CH8_EX8.2_Q2_1",
        "Exercise 8.2 Q2(i): 2 tan 30° / (1 + tan²30°) is equal to:",
        "प्रश्नावली 8.2 Q2(i): 2 tan 30° / (1 + tan²30°) बराबर है:",
        "સ્વાધ્યાય 8.2 Q2(i): 2 tan 30° / (1 + tan²30°) બરાબર છે:",
        [
            "sin 60°",
            "cos 60°",
            "tan 60°",
            "sin 30°"
        ],
        [
            "sin 60°",
            "cos 60°",
            "tan 60°",
            "sin 30°"
        ],
        [
            "sin 60°",
            "cos 60°",
            "tan 60°",
            "sin 30°"
        ],
        0,
        "tan 30° = 1/√3.\n2 tan 30° / (1 + tan²30°) = [2(1/√3)] / [1 + (1/√3)²] = (2/√3) / (1 + 1/3) = (2/√3) / (4/3) = (2/√3) × (3/4) = 3/(2√3) = √3/2.\nSince sin 60° = √3/2, the correct option is sin 60°.",
        "मान रखने पर: [2(1/√3)] / [1 + 1/3] = (2/√3) / (4/3) = √3/2 = sin 60°।",
        "કિંમતો મૂકતાં: (2/√3) / (4/3) = √3/2 = sin 60°.",
        bloom="Apply",
        diff="Beginner",
        mins=1
    ))

    # 35. Exercise 8.2 Q2(ii)
    blocks.append(make_quiz(
        "C10M_CH8_EX8.2_Q2_2",
        "Exercise 8.2 Q2(ii): (1 - tan²45°) / (1 + tan²45°) is equal to:",
        "प्रश्नावली 8.2 Q2(ii): (1 - tan²45°) / (1 + tan²45°) बराबर है:",
        "સ્વાધ્યાય 8.2 Q2(ii): (1 - tan²45°) / (1 + tan²45°) બરાબર છે:",
        [
            "0",
            "tan 90°",
            "1",
            "sin 45°"
        ],
        [
            "0",
            "tan 90°",
            "1",
            "sin 45°"
        ],
        [
            "0",
            "tan 90°",
            "1",
            "sin 45°"
        ],
        0,
        "tan 45° = 1.\n(1 - tan²45°) / (1 + tan²45°) = (1 - 1²) / (1 + 1²) = (1 - 1) / (1 + 1) = 0/2 = 0.",
        "tan 45° = 1 रखने पर: (1 - 1)/(1 + 1) = 0/2 = 0।",
        "tan 45° = 1 મૂકતાં: (1 - 1)/(1 + 1) = 0/2 = 0.",
        bloom="Apply",
        diff="Beginner",
        mins=1
    ))

    # 36. Exercise 8.2 Q2(iii)
    blocks.append(make_quiz(
        "C10M_CH8_EX8.2_Q2_3",
        "Exercise 8.2 Q2(iii): sin 2A = 2 sin A is true when A equals:",
        "प्रश्नावली 8.2 Q2(iii): sin 2A = 2 sin A तब सत्य होता है, जबकि A बराबर है:",
        "સ્વાધ્યાય 8.2 Q2(iii): sin 2A = 2 sin A ત્યારે જ સાચું થાય જ્યારે A બરાબર હોય:",
        [
            "0°",
            "30°",
            "45°",
            "60°"
        ],
        [
            "0°",
            "30°",
            "45°",
            "60°"
        ],
        [
            "0°",
            "30°",
            "45°",
            "60°"
        ],
        0,
        "Substitute A = 0°:\nLHS = sin(2 × 0°) = sin 0° = 0.\nRHS = 2 sin 0° = 2 × 0 = 0.\nLHS = RHS. For A = 30°, LHS = sin 60° = √3/2, RHS = 2 sin 30° = 1 (not equal). Thus A = 0°.",
        "A = 0° रखने पर: LHS = sin(0°) = 0, RHS = 2 sin 0° = 0। अतः A = 0° पर ही यह सत्य है।",
        "A = 0° મૂકતાં: ડા.બા. = sin 0° = 0, જ.બા. = 2(0) = 0. આમ A = 0° સાચો જવાબ છે.",
        bloom="Apply",
        diff="Beginner",
        mins=1
    ))

    # 37. Exercise 8.2 Q2(iv)
    blocks.append(make_quiz(
        "C10M_CH8_EX8.2_Q2_4",
        "Exercise 8.2 Q2(iv): 2 tan 30° / (1 - tan²30°) is equal to:",
        "प्रश्नावली 8.2 Q2(iv): 2 tan 30° / (1 - tan²30°) बराबर है:",
        "સ્વાધ્યાય 8.2 Q2(iv): 2 tan 30° / (1 - tan²30°) બરાબર છે:",
        [
            "tan 60°",
            "cos 60°",
            "sin 60°",
            "sin 30°"
        ],
        [
            "tan 60°",
            "cos 60°",
            "sin 60°",
            "sin 30°"
        ],
        [
            "tan 60°",
            "cos 60°",
            "sin 60°",
            "sin 30°"
        ],
        0,
        "tan 30° = 1/√3.\n2 tan 30° / (1 - tan²30°) = [2(1/√3)] / [1 - (1/√3)²] = (2/√3) / (1 - 1/3) = (2/√3) / (2/3) = (2/√3) × (3/2) = 3/√3 = √3.\nSince tan 60° = √3, the answer is tan 60°.",
        "मान रखने पर: (2/√3) / (2/3) = √3 = tan 60°।",
        "કિંમતો મૂકતાં: (2/√3) / (2/3) = √3 = tan 60°.",
        bloom="Apply",
        diff="Beginner",
        mins=1
    ))

    # 38. Exercise 8.2 Q3
    blocks.append(make_quiz(
        "C10M_CH8_EX8.2_Q3",
        "Exercise 8.2 Q3: If tan(A + B) = √3 and tan(A - B) = 1/√3, where 0° < A + B ≤ 90° and A > B, find A and B.",
        "प्रश्नावली 8.2 Q3: यदि tan(A + B) = √3 और tan(A - B) = 1/√3, जहाँ 0° < A + B ≤ 90° और A > B, तो A और B का मान ज्ञात कीजिए।",
        "સ્વાધ્યાય 8.2 Q3: જો tan(A + B) = √3 અને tan(A - B) = 1/√3, જ્યાં 0° < A + B ≤ 90° અને A > B હોય, તો A અને B ના મૂલ્યો શોધો.",
        [
            "A = 45°, B = 15°",
            "A = 60°, B = 30°",
            "A = 50°, B = 10°",
            "A = 40°, B = 20°"
        ],
        [
            "A = 45°, B = 15°",
            "A = 60°, B = 30°",
            "A = 50°, B = 10°",
            "A = 40°, B = 20°"
        ],
        [
            "A = 45°, B = 15°",
            "A = 60°, B = 30°",
            "A = 50°, B = 10°",
            "A = 40°, B = 20°"
        ],
        0,
        "tan(A + B) = √3 ⇒ A + B = 60°  ... (1)\ntan(A - B) = 1/√3 ⇒ A - B = 30°  ... (2)\nAdding (1) and (2): 2A = 90° ⇒ A = 45°.\nFrom (1): B = 60° - 45° = 15°.",
        "tan(A + B) = √3 ⇒ A + B = 60° ... (1)\ntan(A - B) = 1/√3 ⇒ A - B = 30° ... (2)\nजोड़ने पर: 2A = 90° ⇒ A = 45° और B = 15°।",
        "tan(A + B) = √3 ⇒ A + B = 60° ... (1)\ntan(A - B) = 1/√3 ⇒ A - B = 30° ... (2)\nસરવાળો કરતાં: 2A = 90° ⇒ A = 45° અને B = 15°.",
        bloom="Apply",
        diff="Intermediate",
        mins=2
    ))

    # 39. Exercise 8.2 Q4 (True / False Justifications)
    blocks.append(make_theory(
        "C10M_CH8_EX8.2_Q4",
        "Exercise 8.2 Q4: Conceptual True / False Analysis",
        "प्रश्नावली 8.2 Q4: वैचारिक सत्य/असत्य विश्लेषण",
        "સ્વાધ્યાય 8.2 Q4: વૈચારિક ખરા/ખોટા નું વિશ્લેષણ",
        "### Exercise 8.2 Question 4: State whether the following are true or false with justification:\n\n1. **sin(A + B) = sin A + sin B.**\n   - **FALSE.** Let $A = 30^\\circ, B = 60^\\circ$.\n     $\\text{LHS} = \\sin(30^\\circ + 60^\\circ) = \\sin 90^\\circ = 1$.\n     $\\text{RHS} = \\sin 30^\\circ + \\sin 60^\\circ = 1/2 + \\sqrt{3}/2 = \\frac{1 + \\sqrt{3}}{2} \\ne 1$.\n\n2. **The value of sin θ increases as θ increases.**\n   - **TRUE.** For acute angles ($0^\\circ \\le \\theta \\le 90^\\circ$):\n     $\\sin 0^\\circ = 0, \\sin 30^\\circ = 0.5, \\sin 45^\\circ = 0.707, \\sin 60^\\circ = 0.866, \\sin 90^\\circ = 1$. It strictly increases.\n\n3. **The value of cos θ increases as θ increases.**\n   - **FALSE.** For acute angles ($0^\\circ \\le \\theta \\le 90^\\circ$):\n     $\\cos 0^\\circ = 1, \\cos 30^\\circ = 0.866, \\cos 45^\\circ = 0.707, \\cos 60^\\circ = 0.5, \\cos 90^\\circ = 0$. It decreases from 1 to 0.\n\n4. **sin θ = cos θ for all values of θ.**\n   - **FALSE.** It is ONLY true when $\\theta = 45^\\circ$ (where both equal $1/\\sqrt{2}$). For $\\theta = 30^\\circ$, $\\sin 30^\\circ = 1/2 \\ne \\cos 30^\\circ = \\sqrt{3}/2$.\n\n5. **cot A is not defined for A = 0°.**\n   - **TRUE.** $\\cot 0^\\circ = \\frac{\\cos 0^\\circ}{\\sin 0^\\circ} = \\frac{1}{0}$, which is undefined (division by zero).",
        "### प्रश्नावली 8.2 प्रश्न 4: कारण सहित बताइए कि कथन सत्य हैं या असत्य:\n\n1. **sin(A + B) = sin A + sin B।**\n   - **असत्य।** माना $A = 30^\\circ, B = 60^\\circ$। $\\sin(90^\\circ) = 1$, जबकि $\\sin 30^\\circ + \\sin 60^\\circ = (1 + \\sqrt{3})/2 \\ne 1$।\n\n2. **θ में वृद्धि होने के साथ sin θ के मान में भी वृद्धि होती है।**\n   - **सत्य।** $0^\\circ$ से $90^\\circ$ तक $\\sin \\theta$ का मान 0 से बढ़कर 1 हो जाता है।\n\n3. **θ में वृद्धि होने के साथ cos θ के मान में भी वृद्धि होती है।**\n   - **असत्य।** $0^\\circ$ से $90^\\circ$ तक $\\cos \\theta$ का मान 1 से घटकर 0 हो जाता है।\n\n4. **θ के सभी मानों पर sin θ = cos θ।**\n   - **असत्य।** यह केवल $\\theta = 45^\\circ$ पर सत्य होता है। $30^\\circ$ पर $\\sin 30^\\circ = 1/2 \\ne \\cos 30^\\circ = \\sqrt{3}/2$।\n\n5. **A = 0° पर cot A अपरिभाषित नहीं है (या cot A अपरिभाषित है)।**\n   - **सत्य।** $\\cot 0^\\circ = \\cos 0^\\circ / \\sin 0^\\circ = 1/0$, जो अपरिभाषित है।",
        "### સ્વાધ્યાય 8.2 પ્રશ્ન 4: કારણ આપી જણાવો કે નીચેના વિધાનો ખરા છે કે ખોટા:\n\n1. **sin(A + B) = sin A + sin B.**\n   - **ખોટું.** ધારો કે $A = 30^\\circ, B = 60^\\circ$. $\\sin 90^\\circ = 1$, પરંતુ $\\sin 30^\\circ + \\sin 60^\\circ = (1 + \\sqrt{3})/2 \\ne 1$.\n\n2. **જેમ જેમ θ વધે તેમ sin θ નું મૂલ્ય વધે છે.**\n   - **ખરું.** $0^\\circ$ થી $90^\\circ$ માં $\\sin \\theta$ નું મૂલ્ય 0 થી વધીને 1 થાય છે.\n\n3. **જેમ જેમ θ વધે તેમ cos θ નું મૂલ્ય વધે છે.**\n   - **ખોટું.** $0^\\circ$ થી $90^\\circ$ માં $\\cos \\theta$ નું મૂલ્ય 1 થી ઘટીને 0 થાય છે.\n\n4. **θ ના તમામ મૂલ્યો માટે sin θ = cos θ.**\n   - **ખોટું.** આ માત્ર $\\theta = 45^\\circ$ આગળ જ સાચું છે. $30^\\circ$ આગળ બંને સરખા નથી.\n\n5. **A = 0° આગળ cot A અવ્યાખ્યાયિત છે.**\n   - **ખરું.** $\\cot 0^\\circ = \\cos 0^\\circ / \\sin 0^\\circ = 1/0$, જે અવ્યાખ્યાયિત છે.",
        btype="theory",
        bloom="Analyze",
        diff="Beginner",
        mins=3
    ))

    return blocks

# =========================================================================
# PART 3: TRIGONOMETRIC IDENTITIES & EXERCISE 8.3 (FORMERLY 8.4) + HOTS
# =========================================================================
def get_part3_blocks():
    blocks = []

    # 40. Hook: Equations vs Identities
    blocks.append(make_theory(
        "C10M_CH8_40",
        "The Power of Identities: Mathematical Truths that Never Fail",
        "सर्वसमिकाओं की शक्ति: गणितीय सत्य जो कभी गलत नहीं होते",
        "નિત્યસમની શક્તિ: ક્યારેય ખોટા ન પડતા ગાણિતિક સત્યો",
        "What is the difference between an **Equation** and an **Identity**?\n\n- An equation like $2x + 1 = 7$ is true for only ONE specific value of $x$ ($x = 3$).\n- An algebraic identity like $(a + b)^2 = a^2 + 2ab + b^2$ is true for **EVERY POSSIBLE NUMBER** you substitute into it!\n\nSimilarly, a **Trigonometric Identity (त्रिकोणमितीय सर्वसमिका / ત્રિકોણમિતીય નિત્યસમ)** is an equation involving trigonometric ratios of an angle that holds true for **every single angle $\\theta$** for which the ratios are defined.\n\nMastering identities is like holding an algebraic key: you can transform complicated expressions into elegant, simple numbers, solve calculus problems, and prove breathtaking geometric relations!",
        "एक **समीकरण (Equation)** और एक **सर्वसमिका (Identity)** में क्या अंतर है?\n\n- $2x + 1 = 7$ जैसा समीकरण केवल $x$ के एक विशिष्ट मान ($x = 3$) के लिए सत्य होता है।\n- परंतु $(a + b)^2 = a^2 + 2ab + b^2$ जैसी सर्वसमिका चर के **प्रत्येक संभव मान** के लिए सत्य होती है!\n\nइसी प्रकार, एक **त्रिकोणमितीय सर्वसमिका (Trigonometric Identity)** वह समीकरण है जो कोण के उन सभी मानों के लिए सत्य होता है जिनके लिए वे अनुपात परिभाषित हैं।\n\nसर्वसमिकाओं में महारत हासिल करना बीजगणित की जादुई कुंजी हासिल करने जैसा है: जटिल से जटिल व्यंजकों को चुटकियों में सरल बनाना और कलन (Calculus) के द्वार खोलना!",
        "એક **સમીકરણ** અને **નિત્યસમ** વચ્ચે શું તફાવત છે?\n\n- $2x + 1 = 7$ જેવું સમીકરણ માત્ર $x$ ની એક જ ચોક્કસ કિંમત ($x = 3$) માટે સાચું પડે છે.\n- પરંતુ $(a + b)^2 = a^2 + 2ab + b^2$ જેવો નિત્યસમ ચલની **કોઈપણ કિંમત** માટે હંમેશા સાચો જ રહે છે!\n\nઆ જ રીતે, **ત્રિકોણમિતીય નિત્યસમ** એ એવું સમીકરણ છે જે તેમાં આવતા ખૂણાના **તમામ શક્ય મૂલ્યો** માટે હંમેશા સત્ય સાબિત થાય છે.\n\nઆ નિત્યસમો અતિ જટિલ દાખલાઓને સરળ બનાવવાની અને ઉચ્ચ ગણિત શીખવાની ચાવી છે!",
        btype="hook",
        bloom="Understand",
        diff="Beginner",
        mins=3
    ))

    # 41. Discovery: Deriving the Three Fundamental Pythagorean Identities
    blocks.append(make_theory(
        "C10M_CH8_41",
        "Discovery: Deriving the 3 Master Pythagorean Identities",
        "खोज: 3 मूल पाइथागोरस सर्वसमिकाओं की व्युत्पत्ति",
        "શોધ: પાયથાગોરસના 3 મુખ્ય ત્રિકોણમિતીય નિત્યસમોની તારવણી",
        "Let us take a right-angled triangle $\\triangle ABC$ right-angled at $B$. By the Pythagoras Theorem:\n$$AB^2 + BC^2 = AC^2 \\quad \\text{--- (Equation 1)}$$\n\n### Identity 1: Dividing Eq. 1 by $AC^2$\n$$\\frac{AB^2}{AC^2} + \\frac{BC^2}{AC^2} = \\frac{AC^2}{AC^2} \\implies \\left(\\frac{AB}{AC}\\right)^2 + \\left(\\frac{BC}{AC}\\right)^2 = 1$$\nSince $\\frac{BC}{AC} = \\sin A$ and $\\frac{AB}{AC} = \\cos A$:\n$$\\mathbf{\\sin^2 A + \\cos^2 A = 1} \\quad (\\text{True for all } 0^\\circ \\le A \\le 90^\\circ)$$\n\n### Identity 2: Dividing Eq. 1 by $AB^2$\n$$\\frac{AB^2}{AB^2} + \\frac{BC^2}{AB^2} = \\frac{AC^2}{AB^2} \\implies 1 + \\left(\\frac{BC}{AB}\\right)^2 = \\left(\\frac{AC}{AB}\\right)^2$$\n$$\\mathbf{1 + \\tan^2 A = \\sec^2 A} \\quad (\\text{True for } 0^\\circ \\le A < 90^\\circ)$$\n\n### Identity 3: Dividing Eq. 1 by $BC^2$\n$$\\frac{AB^2}{BC^2} + \\frac{BC^2}{BC^2} = \\frac{AC^2}{BC^2} \\implies \\left(\\frac{AB}{BC}\\right)^2 + 1 = \\left(\\frac{AC}{BC}\\right)^2$$\n$$\\mathbf{1 + \\cot^2 A = \\operatorname{cosec}^2 A} \\quad (\\text{True for } 0^\\circ < A \\le 90^\\circ)$$",
        "समकोण त्रिभुज $\\triangle ABC$ में पाइथागोरस प्रमेय से: $AB^2 + BC^2 = AC^2$ ... (समीकरण 1)\n\n### सर्वसमिका 1: समीकरण 1 को $AC^2$ से भाग देने पर\n$$\\frac{AB^2}{AC^2} + \\frac{BC^2}{AC^2} = 1 \\implies \\mathbf{\\sin^2 A + \\cos^2 A = 1}$$\n\n### सर्वसमिका 2: समीकरण 1 को $AB^2$ से भाग देने पर\n$$1 + \\frac{BC^2}{AB^2} = \\frac{AC^2}{AB^2} \\implies \\mathbf{1 + \\tan^2 A = \\sec^2 A}$$\n\n### सर्वसमिका 3: समीकरण 1 को $BC^2$ से भाग देने पर\n$$\\frac{AB^2}{BC^2} + 1 = \\frac{AC^2}{BC^2} \\implies \\mathbf{1 + \\cot^2 A = \\operatorname{cosec}^2 A}$$",
        "કાટકોણ ત્રિકોણ $\\triangle ABC$ માં પાયથાગોરસ પ્રમેય મુજબ: $AB^2 + BC^2 = AC^2$ ... (સમીકરણ 1)\n\n### નિત્યસમ 1: સમીકરણ 1 ને $AC^2$ વડે ભાગતાં\n$$\\frac{AB^2}{AC^2} + \\frac{BC^2}{AC^2} = 1 \\implies \\mathbf{\\sin^2 A + \\cos^2 A = 1}$$\n\n### નિત્યસમ 2: સમીકરણ 1 ને $AB^2$ વડે ભાગતાં\n$$1 + \\frac{BC^2}{AB^2} = \\frac{AC^2}{AB^2} \\implies \\mathbf{1 + \\tan^2 A = \\sec^2 A}$$\n\n### નિત્યસમ 3: સમીકરણ 1 ને $BC^2$ વડે ભાગતાં\n$$\\frac{AB^2}{BC^2} + 1 = \\frac{AC^2}{BC^2} \\implies \\mathbf{1 + \\cot^2 A = \\operatorname{cosec}^2 A}$$",
        btype="discovery",
        bloom="Analyze",
        diff="Intermediate",
        mins=4
    ))

    # 42. Theory: The Alternate Forms of the 3 Identities
    blocks.append(make_theory(
        "C10M_CH8_42",
        "The Transformed Shapes of Identities for Fast Problem Solving",
        "शीघ्र प्रश्न हल करने हेतु सर्वसमिकाओं के रूपांतरित रूप",
        "ઝડપી દાખલા ગણવા માટે નિત્યસમોના વિવિધ રૂપાંતરો",
        "Every identity has equivalent algebraic rearrangements that you must recognize instantly:\n\n### 1. From $\\sin^2\\theta + \\cos^2\\theta = 1$:\n- $\\sin^2\\theta = 1 - \\cos^2\\theta = (1 - \\cos\\theta)(1 + \\cos\\theta)$\n- $\\cos^2\\theta = 1 - \\sin^2\\theta = (1 - \\sin\\theta)(1 + \\sin\\theta)$\n\n### 2. From $1 + \\tan^2\\theta = \\sec^2\\theta$:\n- $\\sec^2\\theta - \\tan^2\\theta = 1$\n- $(\\sec\\theta - \\tan\\theta)(\\sec\\theta + \\tan\\theta) = 1 \\implies \\sec\\theta - \\tan\\theta = \\frac{1}{\\sec\\theta + \\tan\\theta}$\n*(Very popular in Board Exam HOTS questions!)*\n\n### 3. From $1 + \\cot^2\\theta = \\operatorname{cosec}^2\\theta$:\n- $\\operatorname{cosec}^2\\theta - \\cot^2\\theta = 1$\n- $(\\operatorname{cosec}\\theta - \\cot\\theta)(\\operatorname{cosec}\\theta + \\cot\\theta) = 1 \\implies \\operatorname{cosec}\\theta - \\cot\\theta = \\frac{1}{\\operatorname{cosec}\\theta + \\cot\\theta}$",
        "प्रत्येक सर्वसमिका के पक्षांतरित रूपों को तुरंत पहचानना आवश्यक है:\n\n### 1. $\\sin^2\\theta + \\cos^2\\theta = 1$ से:\n- $\\sin^2\\theta = 1 - \\cos^2\\theta = (1 - \\cos\\theta)(1 + \\cos\\theta)$\n- $\\cos^2\\theta = 1 - \\sin^2\\theta = (1 - \\sin\\theta)(1 + \\sin\\theta)$\n\n### 2. $1 + \\tan^2\\theta = \\sec^2\\theta$ से:\n- $\\sec^2\\theta - \\tan^2\\theta = 1$\n- $\\sec\\theta - \\tan\\theta = \\frac{1}{\\sec\\theta + \\tan\\theta}$ *(बोर्ड HOTS प्रश्नों में अत्यंत उपयोगी!)*\n\n### 3. $1 + \\cot^2\\theta = \\operatorname{cosec}^2\\theta$ से:\n- $\\operatorname{cosec}^2\\theta - \\cot^2\\theta = 1$\n- $\\operatorname{cosec}\\theta - \\cot\\theta = \\frac{1}{\\operatorname{cosec}\\theta + \\cot\\theta}$",
        "દરેક નિત્યસમના વિવિધ સ્વરૂપોને ઝડપથી ઓળખતા શીખો:\n\n### 1. $\\sin^2\\theta + \\cos^2\\theta = 1$ પરથી:\n- $\\sin^2\\theta = 1 - \\cos^2\\theta = (1 - \\cos\\theta)(1 + \\cos\\theta)$\n- $\\cos^2\\theta = 1 - \\sin^2\\theta = (1 - \\sin\\theta)(1 + \\sin\\theta)$\n\n### 2. $1 + \\tan^2\\theta = \\sec^2\\theta$ પરથી:\n- $\\sec^2\\theta - \\tan^2\\theta = 1$\n- $\\sec\\theta - \\tan\\theta = \\frac{1}{\\sec\\theta + \\tan\\theta}$ *(બોર્ડ પરીક્ષાના અઘરા પ્રશ્નો માટે ખૂબ મહત્વનું!)*\n\n### 3. $1 + \\cot^2\\theta = \\operatorname{cosec}^2\\theta$ પરથી:\n- $\\operatorname{cosec}^2\\theta - \\cot^2\\theta = 1$\n- $\\operatorname{cosec}\\theta - \\cot\\theta = \\frac{1}{\\operatorname{cosec}\\theta + \\cot\\theta}$",
        btype="theory",
        bloom="Remember",
        diff="Intermediate",
        mins=3
    ))

    # 43. Teacher Tip: The 4-Step Strategy for Proving Identities
    blocks.append(make_theory(
        "C10M_CH8_43",
        "Teacher Tip: The 4 Master Strategies to Prove ANY Identity",
        "शिक्षक युक्ति: किसी भी सर्वसमिका को सिद्ध करने की 4 अचूक रणनीतियाँ",
        "શિક્ષકની સલાહ: કોઈપણ નિત્યસમ સાબિત કરવાની 4 માસ્ટર ટ્રીક",
        "Students often panic when asked to 'Prove the following identity'. Follow this 4-step checklist:\n\n**Strategy 1: The Golden Escape Rule (Convert to sin and cos)**\nIf the question involves $\\tan, \\cot, \\sec,$ or $\\operatorname{cosec}$, convert everything into $\\sin\\theta$ and $\\cos\\theta$:\n$$\\tan\\theta = \\frac{\\sin\\theta}{\\cos\\theta}, \\quad \\cot\\theta = \\frac{\\cos\\theta}{\\sin\\theta}, \\quad \\sec\\theta = \\frac{1}{\\cos\\theta}, \\quad \\operatorname{cosec}\\theta = \\frac{1}{\\sin\\theta}$$\n\n**Strategy 2: Rationalize the Conjugate**\nWhenever you see $1 \\pm \\sin\\theta$ or $1 \\pm \\cos\\theta$ in the denominator, multiply top and bottom by its conjugate ($1 \\mp \\sin\\theta$ or $1 \\mp \\cos\\theta$) to create $\\cos^2\\theta$ or $\\sin^2\\theta$!\n\n**Strategy 3: Algebraic Factoring**\nWatch out for standard algebraic expansions:\n- $a^2 - b^2 = (a - b)(a + b)$\n- $a^3 - b^3 = (a - b)(a^2 + ab + b^2)$\n- $(a + b)^2 = a^2 + 2ab + b^2$\n\n**Strategy 4: Simplify LHS and RHS Separately**\nIf starting from LHS doesn't reach RHS directly, simplify LHS to its simplest form, then simplify RHS to its simplest form. If both equal the same expression, proof is complete!",
        "विद्यार्थी अक्सर 'सिद्ध कीजिए' वाले प्रश्नों से डरते हैं। यह 4-चरणीय चेकलिस्ट अपनाएँ:\n\n**रणनीति 1: स्वर्ण नियम (sin और cos में बदलें)**\nयदि प्रश्न में $\\tan, \\cot, \\sec$ या $\\operatorname{cosec}$ हो, तो सबको $\\sin\\theta$ और $\\cos\\theta$ में बदल दें।\n\n**रणनीति 2: संयुग्मी से परिमेयकरण**\nजब भी हर में $1 \\pm \\sin\\theta$ या $1 \\pm \\cos\\theta$ दिखे, तो अंश व हर को संयुग्मी ($1 \\mp \\sin\\theta$ या $1 \\mp \\cos\\theta$) से गुणा करें ताकि हर में $\\cos^2\\theta$ या $\\sin^2\\theta$ बन सके!\n\n**रणनीति 3: बीजगणितीय गुणनखंड**\n- $a^2 - b^2 = (a - b)(a + b)$\n- $a^3 - b^3 = (a - b)(a^2 + ab + b^2)$\n\n**रणनीति 4: दोनों पक्षों को अलग-अलग हल करें**\nयदि LHS से सीधे RHS न मिले, तो LHS को सरल करें और RHS को भी सरल करें। दोनों के समान आने पर उपपत्ति पूर्ण!",
        "સાબિતીના દાખલાઓમાં આ 4 સોનેરી નિયમો હંમેશા યાદ રાખો:\n\n**નિયમ 1: સુવર્ણ નિયમ (sin અને cos માં ફેરવો)**\nજો દાખલામાં $\\tan, \\cot, \\sec$ કે $\\operatorname{cosec}$ હોય, તો તેને તરત $\\sin\\theta$ અને $\\cos\\theta$ માં ફેરવી નાખો.\n\n**નિયમ 2: અનુબદ્ધ કરણી વડે સંમેયીકરણ**\nજ્યારે પણ છેદમાં $1 \\pm \\sin\\theta$ કે $1 \\pm \\cos\\theta$ દેખાય ત્યારે અંશ અને છેદને તેની વિરુદ્ધ નિશાનીવાળા પદ વડે ગુણો.\n\n**નિયમ 3: બીજગણિતીય અવયવોનો ઉપયોગ**\n- $a^2 - b^2 = (a - b)(a + b)$\n- $a^3 - b^3 = (a - b)(a^2 + ab + b^2)$\n\n**નિયમ 4: ડા.બા. અને જ.બા. બંનેને અલગથી સાદુરૂપ આપો**\nજો ડાબી બાજુ પરથી સીધી જમણી બાજુ ન મળે, તો બંને બાજુઓને સ્વતંત્ર રીતે સાદુરૂપ આપી સમાન સાબિત કરો!",
        btype="teacher_tip",
        bloom="Analyze",
        diff="Intermediate",
        mins=3
    ))

    # 44. NCERT Example 9 (Rationalized)
    blocks.append(make_quiz(
        "C10M_CH8_EG9",
        "NCERT Example 9: Express the ratios cos A, tan A and sec A in terms of sin A.",
        "NCERT उदाहरण 9: अनुपातों cos A, tan A और sec A को sin A के पदों में व्यक्त कीजिए।",
        "NCERT ઉદાહરણ 9: cos A, tan A અને sec A ને sin A ના સ્વરૂપમાં દર્શાવો.",
        [
            "cos A = √(1 - sin²A), tan A = sin A / √(1 - sin²A), sec A = 1 / √(1 - sin²A)",
            "cos A = 1 - sin A, tan A = sin A / (1 - sin A), sec A = 1 / (1 - sin A)",
            "cos A = √(1 + sin²A), tan A = √(1 - sin²A) / sin A, sec A = √(1 - sin²A)",
            "cos A = 1 / sin A, tan A = sin²A, sec A = 1 - sin²A"
        ],
        [
            "cos A = √(1 - sin²A), tan A = sin A / √(1 - sin²A), sec A = 1 / √(1 - sin²A)",
            "cos A = 1 - sin A, tan A = sin A / (1 - sin A), sec A = 1 / (1 - sin A)",
            "cos A = 1 - sin A, tan A = sin A / (1 - sin A), sec A = 1 / (1 - sin A)",
            "cos A = 1 / sin A, tan A = sin²A, sec A = 1 - sin²A"
        ],
        [
            "cos A = √(1 - sin²A), tan A = sin A / √(1 - sin²A), sec A = 1 / √(1 - sin²A)",
            "cos A = 1 - sin A, tan A = sin A / (1 - sin A), sec A = 1 / (1 - sin A)",
            "cos A = 1 - sin A, tan A = sin A / (1 - sin A), sec A = 1 / (1 - sin A)",
            "cos A = 1 / sin A, tan A = sin²A, sec A = 1 - sin²A"
        ],
        0,
        "Since sin²A + cos²A = 1, cos²A = 1 - sin²A ⇒ cos A = √(1 - sin²A).\ntan A = sin A / cos A = sin A / √(1 - sin²A).\nsec A = 1 / cos A = 1 / √(1 - sin²A).",
        "sin²A + cos²A = 1 ⇒ cos A = √(1 - sin²A)।\ntan A = sin A / cos A = sin A / √(1 - sin²A)।\nsec A = 1 / cos A = 1 / √(1 - sin²A)।",
        "sin²A + cos²A = 1 ⇒ cos A = √(1 - sin²A).\ntan A = sin A / cos A = sin A / √(1 - sin²A).\nsec A = 1 / cos A = 1 / √(1 - sin²A).",
        bloom="Apply",
        diff="Beginner",
        mins=2
    ))

    # 45. NCERT Example 10 (Rationalized)
    blocks.append(make_quiz(
        "C10M_CH8_EG10",
        "NCERT Example 10: Prove that sec A(1 - sin A)(sec A + tan A) equals:",
        "NCERT उदाहरण 10: सिद्ध कीजिए कि sec A(1 - sin A)(sec A + tan A) का मान बराबर है:",
        "NCERT ઉદાહરણ 10: સાબિત કરો કે sec A(1 - sin A)(sec A + tan A) ની કિંમત બરાબર છે:",
        [
            "1",
            "0",
            "sec²A",
            "2"
        ],
        [
            "1",
            "0",
            "sec²A",
            "2"
        ],
        [
            "1",
            "0",
            "sec²A",
            "2"
        ],
        0,
        "LHS = sec A(1 - sin A)(sec A + tan A)\n= (1/cos A)(1 - sin A)(1/cos A + sin A/cos A)\n= [(1 - sin A)/cos A] × [(1 + sin A)/cos A]\n= (1 - sin²A) / cos²A\n= cos²A / cos²A = 1 = RHS. Proved!",
        "LHS = (1/cos A)(1 - sin A)[(1 + sin A)/cos A]\n= (1 - sin²A)/cos²A = cos²A/cos²A = 1 = RHS।",
        "ડા.બા. = (1/cos A)(1 - sin A)[(1 + sin A)/cos A]\n= (1 - sin²A)/cos²A = cos²A/cos²A = 1 = જ.બા.",
        bloom="Apply",
        diff="Beginner",
        mins=2
    ))

    # 46. NCERT Example 11 (Rationalized)
    blocks.append(make_theory(
        "C10M_CH8_EG11",
        "NCERT Example 11: Prove (cot A - cos A) / (cot A + cos A) = (cosec A - 1) / (cosec A + 1)",
        "NCERT उदाहरण 11: सिद्ध कीजिए कि (cot A - cos A) / (cot A + cos A) = (cosec A - 1) / (cosec A + 1)",
        "NCERT ઉદાહરણ 11: સાબિત કરો કે (cot A - cos A) / (cot A + cos A) = (cosec A - 1) / (cosec A + 1)",
        "**Problem:** Prove that $\\frac{\\cot A - \\cos A}{\\cot A + \\cos A} = \\frac{\\operatorname{cosec} A - 1}{\\operatorname{cosec} A + 1}$.\n\n**Proof:**\nExpress $\\cot A$ as $\\frac{\\cos A}{\\sin A}$:\n$$\\text{LHS} = \\frac{\\frac{\\cos A}{\\sin A} - \\cos A}{\\frac{\\cos A}{\\sin A} + \\cos A}$$\nFactor out $\\cos A$ from both numerator and denominator:\n$$\\text{LHS} = \\frac{\\cos A \\left(\\frac{1}{\\sin A} - 1\\right)}{\\cos A \\left(\\frac{1}{\\sin A} + 1\\right)} = \\frac{\\frac{1}{\\sin A} - 1}{\\frac{1}{\\sin A} + 1}$$\nSince $\\frac{1}{\\sin A} = \\operatorname{cosec} A$:\n$$\\text{LHS} = \\frac{\\operatorname{cosec} A - 1}{\\operatorname{cosec} A + 1} = \\text{RHS}$$\nHence proved!",
        "**उपपत्ति:**\n$\\cot A = \\frac{\\cos A}{\\sin A}$ रखने पर:\n$$\\text{LHS} = \\frac{\\frac{\\cos A}{\\sin A} - \\cos A}{\\frac{\\cos A}{\\sin A} + \\cos A} = \\frac{\\cos A\\left(\\frac{1}{\\sin A} - 1\\right)}{\\cos A\\left(\\frac{1}{\\sin A} + 1\\right)}$$\n$\\cos A$ निरस्त करने पर:\n$$= \\frac{\\operatorname{cosec} A - 1}{\\operatorname{cosec} A + 1} = \\text{RHS}।$$",
        "**સાબિતી:**\n$\\cot A = \\frac{\\cos A}{\\sin A}$ મૂકતાં:\n$$\\text{ડા.બા.} = \\frac{\\frac{\\cos A}{\\sin A} - \\cos A}{\\frac{\\cos A}{\\sin A} + \\cos A} = \\frac{\\cos A\\left(\\frac{1}{\\sin A} - 1\\right)}{\\cos A\\left(\\frac{1}{\\sin A} + 1\\right)}$$\n$\\cos A$ સામાન્ય લઈને કેન્સલ કરતાં:\n$$= \\frac{\\operatorname{cosec} A - 1}{\\operatorname{cosec} A + 1} = \\text{જ.બા.}$$",
        btype="theory",
        bloom="Analyze",
        diff="Intermediate",
        mins=2
    ))

    # 47. Exercise 8.3 Q1 (Rationalized, former 8.4)
    blocks.append(make_theory(
        "C10M_CH8_EX8.3_Q1",
        "Exercise 8.3 Q1: Express sin A, sec A and tan A in terms of cot A",
        "प्रश्नावली 8.3 Q1: sin A, sec A और tan A को cot A के पदों में व्यक्त कीजिए",
        "સ્વાધ્યાય 8.3 Q1: sin A, sec A અને tan A ને cot A ના સ્વરૂપમાં દર્શાવો",
        "### Exercise 8.3 Q1 Solution:\n\n1. **For tan A:**\n   $$\\tan A = \\frac{1}{\\cot A}$$\n\n2. **For sin A:**\n   Using the identity $\\operatorname{cosec}^2 A = 1 + \\cot^2 A$:\n   $$\\sin^2 A = \\frac{1}{\\operatorname{cosec}^2 A} = \\frac{1}{1 + \\cot^2 A} \\implies \\sin A = \\frac{1}{\\sqrt{1 + \\cot^2 A}}$$\n\n3. **For sec A:**\n   Using the identity $\\sec^2 A = 1 + \\tan^2 A = 1 + \\frac{1}{\\cot^2 A} = \\frac{\\cot^2 A + 1}{\\cot^2 A}$:\n   $$\\sec A = \\sqrt{\\frac{1 + \\cot^2 A}{\\cot^2 A}} = \\frac{\\sqrt{1 + \\cot^2 A}}{\\cot A}$$",
        "### प्रश्नावली 8.3 Q1 हल:\n\n1. **tan A के लिए:** $\\tan A = \\frac{1}{\\cot A}$\n2. **sin A के लिए:** $\\operatorname{cosec}^2 A = 1 + \\cot^2 A \\implies \\sin A = \\frac{1}{\\sqrt{1 + \\cot^2 A}}$\n3. **sec A के लिए:** $\\sec^2 A = 1 + \\tan^2 A = 1 + \\frac{1}{\\cot^2 A} = \\frac{\\cot^2 A + 1}{\\cot^2 A} \\implies \\sec A = \\frac{\\sqrt{1 + \\cot^2 A}}{\\cot A}$",
        "### સ્વાધ્યાય 8.3 Q1 ઉકેલ:\n\n1. **tan A માટે:** $\\tan A = \\frac{1}{\\cot A}$\n2. **sin A માટે:** $\\operatorname{cosec}^2 A = 1 + \\cot^2 A \\implies \\sin A = \\frac{1}{\\sqrt{1 + \\cot^2 A}}$\n3. **sec A માટે:** $\\sec^2 A = 1 + \\tan^2 A = \\frac{1 + \\cot^2 A}{\\cot^2 A} \\implies \\sec A = \\frac{\\sqrt{1 + \\cot^2 A}}{\\cot A}$",
        btype="theory",
        bloom="Apply",
        diff="Intermediate",
        mins=3
    ))

    # 48. Exercise 8.3 Q2
    blocks.append(make_theory(
        "C10M_CH8_EX8.3_Q2",
        "Exercise 8.3 Q2: Write All Other Trigonometric Ratios of ∠A in terms of sec A",
        "प्रश्नावली 8.3 Q2: ∠A के अन्य सभी त्रिकोणमितीय अनुपातों को sec A के पदों में लिखिए",
        "સ્વાધ્યાય 8.3 Q2: ખૂણા A ના બાકીના તમામ ત્રિકોણમિતીય ગુણોત્તરોને sec A ના સ્વરૂપમાં દર્શાવો",
        "### All ratios in terms of sec A:\n\n1. **cos A:** $\\cos A = \\frac{1}{\\sec A}$\n2. **sin A:** $\\sin A = \\sqrt{1 - \\cos^2 A} = \\sqrt{1 - \\frac{1}{\\sec^2 A}} = \\frac{\\sqrt{\\sec^2 A - 1}}{\\sec A}$\n3. **tan A:** $1 + \\tan^2 A = \\sec^2 A \\implies \\tan A = \\sqrt{\\sec^2 A - 1}$\n4. **cosec A:** $\\operatorname{cosec} A = \\frac{1}{\\sin A} = \\frac{\\sec A}{\\sqrt{\\sec^2 A - 1}}$\n5. **cot A:** $\\cot A = \\frac{1}{\\tan A} = \\frac{1}{\\sqrt{\\sec^2 A - 1}}$",
        "### sec A के पदों में सभी अनुपात:\n\n1. $\\cos A = \\frac{1}{\\sec A}$\n2. $\\sin A = \\frac{\\sqrt{\\sec^2 A - 1}}{\\sec A}$\n3. $\\tan A = \\sqrt{\\sec^2 A - 1}$\n4. $\\operatorname{cosec} A = \\frac{\\sec A}{\\sqrt{\\sec^2 A - 1}}$\n5. $\\cot A = \\frac{1}{\\sqrt{\\sec^2 A - 1}}$",
        "### sec A ના સ્વરૂપમાં તમામ ગુણોત્તરો:\n\n1. $\\cos A = \\frac{1}{\\sec A}$\n2. $\\sin A = \\frac{\\sqrt{\\sec^2 A - 1}}{\\sec A}$\n3. $\\tan A = \\sqrt{\\sec^2 A - 1}$\n4. $\\operatorname{cosec} A = \\frac{\\sec A}{\\sqrt{\\sec^2 A - 1}}$\n5. $\\cot A = \\frac{1}{\\sqrt{\\sec^2 A - 1}}$",
        btype="theory",
        bloom="Apply",
        diff="Intermediate",
        mins=3
    ))

    # 49. Exercise 8.3 Q3(i) [MCQ]
    blocks.append(make_quiz(
        "C10M_CH8_EX8.3_Q3_1",
        "Exercise 8.3 Q3(i): 9 sec²A - 9 tan²A equals:",
        "प्रश्नावली 8.3 Q3(i): 9 sec²A - 9 tan²A बराबर है:",
        "સ્વાધ્યાય 8.3 Q3(i): 9 sec²A - 9 tan²A બરાબર છે:",
        [
            "9",
            "1",
            "8",
            "0"
        ],
        [
            "9",
            "1",
            "8",
            "0"
        ],
        [
            "9",
            "1",
            "8",
            "0"
        ],
        0,
        "9 sec²A - 9 tan²A = 9(sec²A - tan²A).\nSince sec²A - tan²A = 1, we have 9 × 1 = 9.",
        "9(sec²A - tan²A) = 9(1) = 9।",
        "9(sec²A - tan²A) = 9(1) = 9.",
        bloom="Apply",
        diff="Beginner",
        mins=1
    ))

    # 50. Exercise 8.3 Q3(ii) [MCQ]
    blocks.append(make_quiz(
        "C10M_CH8_EX8.3_Q3_2",
        "Exercise 8.3 Q3(ii): (1 + tan θ + sec θ)(1 + cot θ - cosec θ) equals:",
        "प्रश्नावली 8.3 Q3(ii): (1 + tan θ + sec θ)(1 + cot θ - cosec θ) बराबर है:",
        "સ્વાધ્યાય 8.3 Q3(ii): (1 + tan θ + sec θ)(1 + cot θ - cosec θ) બરાબર છે:",
        [
            "2",
            "0",
            "1",
            "-1"
        ],
        [
            "2",
            "0",
            "1",
            "-1"
        ],
        [
            "2",
            "0",
            "1",
            "-1"
        ],
        0,
        "Convert to sin θ and cos θ:\n(1 + sin θ/cos θ + 1/cos θ)(1 + cos θ/sin θ - 1/sin θ)\n= [(cos θ + sin θ + 1)/cos θ] × [(sin θ + cos θ - 1)/sin θ]\n= [(cos θ + sin θ)² - 1²] / (sin θ cos θ)\n= (cos²θ + sin²θ + 2 sin θ cos θ - 1) / (sin θ cos θ)\n= (1 + 2 sin θ cos θ - 1) / (sin θ cos θ) = 2 sin θ cos θ / (sin θ cos θ) = 2.",
        "sin और cos में बदलने पर: [(sin θ + cos θ + 1)/cos θ][(sin θ + cos θ - 1)/sin θ]\n= [(sin θ + cos θ)² - 1] / (sin θ cos θ) = (1 + 2 sin θ cos θ - 1) / (sin θ cos θ) = 2।",
        "sin અને cos માં ફેરવતાં: [(sin θ + cos θ)² - 1] / (sin θ cos θ) = 2 sin θ cos θ / (sin θ cos θ) = 2.",
        bloom="Apply",
        diff="Intermediate",
        mins=2
    ))

    # 51. Exercise 8.3 Q3(iii) [MCQ]
    blocks.append(make_quiz(
        "C10M_CH8_EX8.3_Q3_3",
        "Exercise 8.3 Q3(iii): (sec A + tan A)(1 - sin A) equals:",
        "प्रश्नावली 8.3 Q3(iii): (sec A + tan A)(1 - sin A) बराबर है:",
        "સ્વાધ્યાય 8.3 Q3(iii): (sec A + tan A)(1 - sin A) બરાબર છે:",
        [
            "cos A",
            "sec A",
            "sin A",
            "cosec A"
        ],
        [
            "cos A",
            "sec A",
            "sin A",
            "cosec A"
        ],
        [
            "cos A",
            "sec A",
            "sin A",
            "cosec A"
        ],
        0,
        "(sec A + tan A)(1 - sin A) = (1/cos A + sin A/cos A)(1 - sin A)\n= [(1 + sin A)/cos A](1 - sin A) = (1 - sin²A)/cos A = cos²A/cos A = cos A.",
        "(1/cos A + sin A/cos A)(1 - sin A) = (1 - sin²A)/cos A = cos²A/cos A = cos A।",
        "(1/cos A + sin A/cos A)(1 - sin A) = (1 - sin²A)/cos A = cos²A/cos A = cos A.",
        bloom="Apply",
        diff="Beginner",
        mins=2
    ))

    # 52. Exercise 8.3 Q3(iv) [MCQ]
    blocks.append(make_quiz(
        "C10M_CH8_EX8.3_Q3_4",
        "Exercise 8.3 Q3(iv): (1 + tan²A) / (1 + cot²A) equals:",
        "प्रश्नावली 8.3 Q3(iv): (1 + tan²A) / (1 + cot²A) बराबर है:",
        "સ્વાધ્યાય 8.3 Q3(iv): (1 + tan²A) / (1 + cot²A) બરાબર છે:",
        [
            "tan²A",
            "sec²A",
            "-1",
            "cot²A"
        ],
        [
            "tan²A",
            "sec²A",
            "-1",
            "cot²A"
        ],
        [
            "tan²A",
            "sec²A",
            "-1",
            "cot²A"
        ],
        0,
        "1 + tan²A = sec²A and 1 + cot²A = cosec²A.\nsec²A / cosec²A = (1/cos²A) / (1/sin²A) = sin²A / cos²A = tan²A.",
        "sec²A / cosec²A = (1/cos²A)/(1/sin²A) = sin²A/cos²A = tan²A।",
        "sec²A / cosec²A = (1/cos²A)/(1/sin²A) = sin²A/cos²A = tan²A.",
        bloom="Apply",
        diff="Beginner",
        mins=1
    ))

    # 53. Exercise 8.3 Q4(i) [Proof 1]
    blocks.append(make_theory(
        "C10M_CH8_EX8.3_Q4_1",
        "Exercise 8.3 Q4(i): Prove (cosec θ - cot θ)² = (1 - cos θ) / (1 + cos θ)",
        "प्रश्नावली 8.3 Q4(i): सिद्ध कीजिए कि (cosec θ - cot θ)² = (1 - cos θ) / (1 + cos θ)",
        "સ્વાધ્યાય 8.3 Q4(i): સાબિત કરો કે (cosec θ - cot θ)² = (1 - cos θ) / (1 + cos θ)",
        "**Proof:**\n$$\\text{LHS} = (\\operatorname{cosec}\\theta - \\cot\\theta)^2 = \\left(\\frac{1}{\\sin\\theta} - \\frac{\\cos\\theta}{\\sin\\theta}\\right)^2 = \\frac{(1 - \\cos\\theta)^2}{\\sin^2\\theta}$$\nSubstitute $\\sin^2\\theta = 1 - \\cos^2\\theta$:\n$$\\text{LHS} = \\frac{(1 - \\cos\\theta)^2}{1 - \\cos^2\\theta} = \\frac{(1 - \\cos\\theta)(1 - \\cos\\theta)}{(1 - \\cos\\theta)(1 + \\cos\\theta)}$$\nCancel $(1 - \\cos\\theta)$ from numerator and denominator:\n$$\\text{LHS} = \\frac{1 - \\cos\\theta}{1 + \\cos\\theta} = \\text{RHS}$$\nHence proved!",
        "**उपपत्ति:**\n$$\\text{LHS} = \\left(\\frac{1 - \\cos\\theta}{\\sin\\theta}\\right)^2 = \\frac{(1 - \\cos\\theta)^2}{\\sin^2\\theta} = \\frac{(1 - \\cos\\theta)^2}{1 - \\cos^2\\theta}$$\n$$= \\frac{(1 - \\cos\\theta)(1 - \\cos\\theta)}{(1 - \\cos\\theta)(1 + \\cos\\theta)} = \\frac{1 - \\cos\\theta}{1 + \\cos\\theta} = \\text{RHS}।$$",
        "**સાબિતી:**\n$$\\text{ડા.બા.} = \\left(\\frac{1 - \\cos\\theta}{\\sin\\theta}\\right)^2 = \\frac{(1 - \\cos\\theta)^2}{\\sin^2\\theta} = \\frac{(1 - \\cos\\theta)^2}{1 - \\cos^2\\theta}$$\n$$= \\frac{(1 - \\cos\\theta)(1 - \\cos\\theta)}{(1 - \\cos\\theta)(1 + \\cos\\theta)} = \\frac{1 - \\cos\\theta}{1 + \\cos\\theta} = \\text{જ.બા.}$$",
        btype="theory",
        bloom="Analyze",
        diff="Intermediate",
        mins=2
    ))

    # 54. Exercise 8.3 Q4(ii) [Proof 2]
    blocks.append(make_theory(
        "C10M_CH8_EX8.3_Q4_2",
        "Exercise 8.3 Q4(ii): Prove cos A / (1 + sin A) + (1 + sin A) / cos A = 2 sec A",
        "प्रश्नावली 8.3 Q4(ii): सिद्ध कीजिए कि cos A / (1 + sin A) + (1 + sin A) / cos A = 2 sec A",
        "સ્વાધ્યાય 8.3 Q4(ii): સાબિત કરો કે cos A / (1 + sin A) + (1 + sin A) / cos A = 2 sec A",
        "**Proof:**\n$$\\text{LHS} = \\frac{\\cos A}{1 + \\sin A} + \\frac{1 + \\sin A}{\\cos A}$$\nTaking common denominator $(1 + \\sin A)\\cos A$:\n$$\\text{LHS} = \\frac{\\cos^2 A + (1 + \\sin A)^2}{(1 + \\sin A)\\cos A} = \\frac{\\cos^2 A + 1 + 2\\sin A + \\sin^2 A}{(1 + \\sin A)\\cos A}$$\nUsing $\\sin^2 A + \\cos^2 A = 1$:\n$$\\text{LHS} = \\frac{1 + 1 + 2\\sin A}{(1 + \\sin A)\\cos A} = \\frac{2 + 2\\sin A}{(1 + \\sin A)\\cos A} = \\frac{2(1 + \\sin A)}{(1 + \\sin A)\\cos A}$$\nCancel $(1 + \\sin A)$:\n$$\\text{LHS} = \\frac{2}{\\cos A} = 2\\sec A = \\text{RHS}$$\nHence proved!",
        "**उपपत्ति:**\nलघुत्तम समापवर्त्य लेने पर:\n$$\\text{LHS} = \\frac{\\cos^2 A + (1 + \\sin A)^2}{(1 + \\sin A)\\cos A} = \\frac{(\\cos^2 A + \\sin^2 A) + 1 + 2\\sin A}{(1 + \\sin A)\\cos A}$$\n$$= \\frac{1 + 1 + 2\\sin A}{(1 + \\sin A)\\cos A} = \\frac{2(1 + \\sin A)}{(1 + \\sin A)\\cos A} = \\frac{2}{\\cos A} = 2\\sec A = \\text{RHS}।$$",
        "**સાબિતી:**\nલ.સા.અ. લેતાં:\n$$\\text{ડા.બા.} = \\frac{\\cos^2 A + (1 + \\sin A)^2}{(1 + \\sin A)\\cos A} = \\frac{1 + 1 + 2\\sin A}{(1 + \\sin A)\\cos A}$$\n$$= \\frac{2(1 + \\sin A)}{(1 + \\sin A)\\cos A} = \\frac{2}{\\cos A} = 2\\sec A = \\text{જ.બા.}$$",
        btype="theory",
        bloom="Analyze",
        diff="Intermediate",
        mins=2
    ))

    # 55. Exercise 8.3 Q4(iii) [Proof 3]
    blocks.append(make_theory(
        "C10M_CH8_EX8.3_Q4_3",
        "Exercise 8.3 Q4(iii): Prove tan θ / (1 - cot θ) + cot θ / (1 - tan θ) = 1 + sec θ cosec θ",
        "प्रश्नावली 8.3 Q4(iii): सिद्ध कीजिए कि tan θ / (1 - cot θ) + cot θ / (1 - tan θ) = 1 + sec θ cosec θ",
        "સ્વાધ્યાય 8.3 Q4(iii): સાબિત કરો કે tan θ / (1 - cot θ) + cot θ / (1 - tan θ) = 1 + sec θ cosec θ",
        "**Proof:**\nConvert all ratios into $\\sin\\theta$ and $\\cos\\theta$:\n$$\\frac{\\frac{\\sin\\theta}{\\cos\\theta}}{1 - \\frac{\\cos\\theta}{\\sin\\theta}} + \\frac{\\frac{\\cos\\theta}{\\sin\\theta}}{1 - \\frac{\\sin\\theta}{\\cos\\theta}} = \\frac{\\sin^2\\theta}{\\cos\\theta(\\sin\\theta - \\cos\\theta)} - \\frac{\\cos^2\\theta}{\\sin\\theta(\\sin\\theta - \\cos\\theta)}$$\nTake common denominator $\\sin\\theta\\cos\\theta(\\sin\\theta - \\cos\\theta)$:\n$$= \\frac{\\sin^3\\theta - \\cos^3\\theta}{\\sin\\theta\\cos\\theta(\\sin\\theta - \\cos\\theta)}$$\nUsing $a^3 - b^3 = (a - b)(a^2 + ab + b^2)$:\n$$= \\frac{(\\sin\\theta - \\cos\\theta)(\\sin^2\\theta + \\sin\\theta\\cos\\theta + \\cos^2\\theta)}{\\sin\\theta\\cos\\theta(\\sin\\theta - \\cos\\theta)}$$\n$$= \\frac{1 + \\sin\\theta\\cos\\theta}{\\sin\\theta\\cos\\theta} = \\frac{1}{\\sin\\theta\\cos\\theta} + \\frac{\\sin\\theta\\cos\\theta}{\\sin\\theta\\cos\\theta} = \\operatorname{cosec}\\theta\\sec\\theta + 1 = \\text{RHS}$$\nHence proved!",
        "**उपपत्ति:**\n$\\sin$ और $\\cos$ में बदलने पर:\n$$= \\frac{\\sin^2\\theta}{\\cos\\theta(\\sin\\theta - \\cos\\theta)} - \\frac{\\cos^2\\theta}{\\sin\\theta(\\sin\\theta - \\cos\\theta)} = \\frac{\\sin^3\\theta - \\cos^3\\theta}{\\sin\\theta\\cos\\theta(\\sin\\theta - \\cos\\theta)}$$\n$a^3 - b^3$ सूत्र लगाने पर:\n$$= \\frac{(\\sin\\theta - \\cos\\theta)(1 + \\sin\\theta\\cos\\theta)}{\\sin\\theta\\cos\\theta(\\sin\\theta - \\cos\\theta)} = \\frac{1}{\\sin\\theta\\cos\\theta} + 1 = 1 + \\sec\\theta\\operatorname{cosec}\\theta = \\text{RHS}।$$",
        "**સાબિતી:**\n$\\sin$ અને $\\cos$ માં ફેરવતાં:\n$$= \\frac{\\sin^3\\theta - \\cos^3\\theta}{\\sin\\theta\\cos\\theta(\\sin\\theta - \\cos\\theta)}$$\n$a^3 - b^3 = (a - b)(a^2 + ab + b^2)$ સૂત્ર વાપરતાં:\n$$= \\frac{1 + \\sin\\theta\\cos\\theta}{\\sin\\theta\\cos\\theta} = 1 + \\sec\\theta\\operatorname{cosec}\\theta = \\text{જ.બા.}$$",
        btype="theory",
        bloom="Analyze",
        diff="Advanced",
        mins=3
    ))

    # 56. Exercise 8.3 Q4(iv) [Proof 4]
    blocks.append(make_theory(
        "C10M_CH8_EX8.3_Q4_4",
        "Exercise 8.3 Q4(iv): Prove (1 + sec A) / sec A = sin²A / (1 - cos A)",
        "प्रश्नावली 8.3 Q4(iv): सिद्ध कीजिए कि (1 + sec A) / sec A = sin²A / (1 - cos A)",
        "સ્વાધ્યાય 8.3 Q4(iv): સાબિત કરો કે (1 + sec A) / sec A = sin²A / (1 - cos A)",
        "**Proof (Simplifying LHS & RHS):**\n$$\\text{LHS} = \\frac{1 + \\sec A}{\\sec A} = \\frac{1 + \\frac{1}{\\cos A}}{\\frac{1}{\\cos A}} = \\frac{\\frac{\\cos A + 1}{\\cos A}}{\\frac{1}{\\cos A}} = 1 + \\cos A$$\n\nNow simplify RHS:\n$$\\text{RHS} = \\frac{\\sin^2 A}{1 - \\cos A} = \\frac{1 - \\cos^2 A}{1 - \\cos A} = \\frac{(1 - \\cos A)(1 + \\cos A)}{1 - \\cos A} = 1 + \\cos A$$\n\nSince $\\text{LHS} = \\text{RHS} = 1 + \\cos A$, the identity is proved!",
        "**उपपत्ति:**\n$$\\text{LHS} = \\frac{1 + 1/\\cos A}{1/\\cos A} = 1 + \\cos A$$\n$$\\text{RHS} = \\frac{\\sin^2 A}{1 - \\cos A} = \\frac{1 - \\cos^2 A}{1 - \\cos A} = \\frac{(1 - \\cos A)(1 + \\cos A)}{1 - \\cos A} = 1 + \\cos A$$\nचूँकि LHS = RHS, अतः सिद्ध हुआ!",
        "**સાબિતી:**\n$$\\text{ડા.બા.} = \\frac{1 + 1/\\cos A}{1/\\cos A} = 1 + \\cos A$$\n$$\\text{જ.બા.} = \\frac{\\sin^2 A}{1 - \\cos A} = \\frac{(1 - \\cos A)(1 + \\cos A)}{1 - \\cos A} = 1 + \\cos A$$\nડા.બા. = જ.બા. હોવાથી સાબિત થાય છે!",
        btype="theory",
        bloom="Analyze",
        diff="Intermediate",
        mins=2
    ))

    # 57. Exercise 8.3 Q4(v) [Proof 5 - The Classic Board Question]
    blocks.append(make_theory(
        "C10M_CH8_EX8.3_Q4_5",
        "Exercise 8.3 Q4(v): Prove (cos A - sin A + 1) / (cos A + sin A - 1) = cosec A + cot A",
        "प्रश्नावली 8.3 Q4(v): सिद्ध कीजिए कि (cos A - sin A + 1) / (cos A + sin A - 1) = cosec A + cot A",
        "સ્વાધ્યાય 8.3 Q4(v): સાબિત કરો કે (cos A - sin A + 1) / (cos A + sin A - 1) = cosec A + cot A",
        "**Proof (Board Exam Master Problem):**\nDivide each term of numerator and denominator by $\\sin A$:\n$$\\text{LHS} = \\frac{\\frac{\\cos A}{\\sin A} - 1 + \\frac{1}{\\sin A}}{\\frac{\\cos A}{\\sin A} + 1 - \\frac{1}{\\sin A}} = \\frac{\\cot A + \\operatorname{cosec} A - 1}{\\cot A - \\operatorname{cosec} A + 1}$$\nIn the numerator, substitute $1 = \\operatorname{cosec}^2 A - \\cot^2 A$:\n$$= \\frac{(\\operatorname{cosec} A + \\cot A) - (\\operatorname{cosec}^2 A - \\cot^2 A)}{\\cot A - \\operatorname{cosec} A + 1}$$\n$$= \\frac{(\\operatorname{cosec} A + \\cot A) - [(\\operatorname{cosec} A - \\cot A)(\\operatorname{cosec} A + \\cot A)]}{\\cot A - \\operatorname{cosec} A + 1}$$\nFactor out $(\\operatorname{cosec} A + \\cot A)$:\n$$= \\frac{(\\operatorname{cosec} A + \\cot A)[1 - (\\operatorname{cosec} A - \\cot A)]}{\\cot A - \\operatorname{cosec} A + 1} = \\frac{(\\operatorname{cosec} A + \\cot A)(1 - \\operatorname{cosec} A + \\cot A)}{\\cot A - \\operatorname{cosec} A + 1}$$\nCancel the common factor $(1 - \\operatorname{cosec} A + \\cot A)$:\n$$= \\operatorname{cosec} A + \\cot A = \\text{RHS}$$\nHence proved!",
        "**उपपत्ति:**\nअंश और हर को $\\sin A$ से भाग देने पर:\n$$= \\frac{\\cot A + \\operatorname{cosec} A - 1}{\\cot A - \\operatorname{cosec} A + 1}$$\nअंश में $1 = \\operatorname{cosec}^2 A - \\cot^2 A$ रखने पर:\n$$= \\frac{(\\operatorname{cosec} A + \\cot A)[1 - (\\operatorname{cosec} A - \\cot A)]}{\\cot A - \\operatorname{cosec} A + 1} = \\operatorname{cosec} A + \\cot A = \\text{RHS}।$$",
        "**સાબિતી:**\nઅંશ અને છેદને $\\sin A$ વડે ભાગતાં:\n$$= \\frac{\\cot A + \\operatorname{cosec} A - 1}{\\cot A - \\operatorname{cosec} A + 1}$$\nઅંશમાં $1 = \\operatorname{cosec}^2 A - \\cot^2 A$ મૂકતાં:\n$$= \\frac{(\\operatorname{cosec} A + \\cot A)[1 - (\\operatorname{cosec} A - \\cot A)]}{\\cot A - \\operatorname{cosec} A + 1} = \\operatorname{cosec} A + \\cot A = \\text{જ.બા.}$$",
        btype="theory",
        bloom="Analyze",
        diff="Advanced",
        mins=4
    ))

    # 58. Exercise 8.3 Q4(vi) [Proof 6]
    blocks.append(make_theory(
        "C10M_CH8_EX8.3_Q4_6",
        "Exercise 8.3 Q4(vi): Prove √[(1 + sin A) / (1 - sin A)] = sec A + tan A",
        "प्रश्नावली 8.3 Q4(vi): सिद्ध कीजिए कि √[(1 + sin A) / (1 - sin A)] = sec A + tan A",
        "સ્વાધ્યાય 8.3 Q4(vi): સાબિત કરો કે √[(1 + sin A) / (1 - sin A)] = sec A + tan A",
        "**Proof:**\nMultiply numerator and denominator inside the square root by $(1 + \\sin A)$:\n$$\\text{LHS} = \\sqrt{\\frac{(1 + \\sin A)(1 + \\sin A)}{(1 - \\sin A)(1 + \\sin A)}} = \\sqrt{\\frac{(1 + \\sin A)^2}{1 - \\sin^2 A}}$$\nSince $1 - \\sin^2 A = \\cos^2 A$:\n$$\\text{LHS} = \\sqrt{\\frac{(1 + \\sin A)^2}{\\cos^2 A}} = \\frac{1 + \\sin A}{\\cos A} = \\frac{1}{\\cos A} + \\frac{\\sin A}{\\cos A} = \\sec A + \\tan A = \\text{RHS}$$\nHence proved!",
        "**उपपत्ति:**\nकरणी के अंदर $(1 + \\sin A)$ से अंश व हर में गुणा करने पर:\n$$\\text{LHS} = \\sqrt{\\frac{(1 + \\sin A)^2}{1 - \\sin^2 A}} = \\sqrt{\\frac{(1 + \\sin A)^2}{\\cos^2 A}} = \\frac{1 + \\sin A}{\\cos A} = \\sec A + \\tan A = \\text{RHS}।$$",
        "**સાબિતી:**\nવર્ગમૂળની અંદર $(1 + \\sin A)$ વડે અંશ અને છેદને ગુણતાં:\n$$\\text{ડા.બા.} = \\sqrt{\\frac{(1 + \\sin A)^2}{1 - \\sin^2 A}} = \\frac{1 + \\sin A}{\\cos A} = \\sec A + \\tan A = \\text{જ.બા.}$$",
        btype="theory",
        bloom="Analyze",
        diff="Beginner",
        mins=2
    ))

    # 59. Exercise 8.3 Q4(vii) [Proof 7]
    blocks.append(make_theory(
        "C10M_CH8_EX8.3_Q4_7",
        "Exercise 8.3 Q4(vii): Prove (sin θ - 2 sin³θ) / (2 cos³θ - cos θ) = tan θ",
        "प्रश्नावली 8.3 Q4(vii): सिद्ध कीजिए कि (sin θ - 2 sin³θ) / (2 cos³θ - cos θ) = tan θ",
        "સ્વાધ્યાય 8.3 Q4(vii): સાબિત કરો કે (sin θ - 2 sin³θ) / (2 cos³θ - cos θ) = tan θ",
        "**Proof:**\nFactor out $\\sin\\theta$ from numerator and $\\cos\\theta$ from denominator:\n$$\\text{LHS} = \\frac{\\sin\\theta(1 - 2\\sin^2\\theta)}{\\cos\\theta(2\\cos^2\\theta - 1)}$$\nIn the numerator, substitute $1 = \\sin^2\\theta + \\cos^2\\theta$:\n$$1 - 2\\sin^2\\theta = (\\sin^2\\theta + \\cos^2\\theta) - 2\\sin^2\\theta = \\cos^2\\theta - \\sin^2\\theta$$\nIn the denominator:\n$$2\\cos^2\\theta - 1 = 2\\cos^2\\theta - (\\sin^2\\theta + \\cos^2\\theta) = \\cos^2\\theta - \\sin^2\\theta$$\nTherefore:\n$$\\text{LHS} = \\frac{\\sin\\theta(\\cos^2\\theta - \\sin^2\\theta)}{\\cos\\theta(\\cos^2\\theta - \\sin^2\\theta)} = \\frac{\\sin\\theta}{\\cos\\theta} = \\tan\\theta = \\text{RHS}$$\nHence proved!",
        "**उपपत्ति:**\n$$\\text{LHS} = \\frac{\\sin\\theta(1 - 2\\sin^2\\theta)}{\\cos\\theta(2\\cos^2\\theta - 1)}$$\n$1 = \\sin^2\\theta + \\cos^2\\theta$ रखने पर दोनों कोष्ठक $(\\cos^2\\theta - \\sin^2\\theta)$ बन जाते हैं:\n$$= \\frac{\\sin\\theta(\\cos^2\\theta - \\sin^2\\theta)}{\\cos\\theta(\\cos^2\\theta - \\sin^2\\theta)} = \\frac{\\sin\\theta}{\\cos\\theta} = \\tan\\theta = \\text{RHS}।$$",
        "**સાબિતી:**\n$$\\text{ડા.બા.} = \\frac{\\sin\\theta(1 - 2\\sin^2\\theta)}{\\cos\\theta(2\\cos^2\\theta - 1)}$$\n$1 = \\sin^2\\theta + \\cos^2\\theta$ મૂકતાં બંને કૌંસ $(\\cos^2\\theta - \\sin^2\\theta)$ બને છે:\n$$= \\frac{\\sin\\theta}{\\cos\\theta} = \\tan\\theta = \\text{જ.બા.}$$",
        btype="theory",
        bloom="Analyze",
        diff="Intermediate",
        mins=2
    ))

    # 60. Exercise 8.3 Q4(viii) [Proof 8]
    blocks.append(make_theory(
        "C10M_CH8_EX8.3_Q4_8",
        "Exercise 8.3 Q4(viii): Prove (sin A + cosec A)² + (cos A + sec A)² = 7 + tan²A + cot²A",
        "प्रश्नावली 8.3 Q4(viii): सिद्ध कीजिए कि (sin A + cosec A)² + (cos A + sec A)² = 7 + tan²A + cot²A",
        "સ્વાધ્યાય 8.3 Q4(viii): સાબિત કરો કે (sin A + cosec A)² + (cos A + sec A)² = 7 + tan²A + cot²A",
        "**Proof:**\nExpand both squared binomials using $(a + b)^2 = a^2 + 2ab + b^2$:\n$$\\text{LHS} = (\\sin^2 A + 2\\sin A\\operatorname{cosec} A + \\operatorname{cosec}^2 A) + (\\cos^2 A + 2\\cos A\\sec A + \\sec^2 A)$$\nSince $\\sin A\\operatorname{cosec} A = 1$ and $\\cos A\\sec A = 1$:\n$$= (\\sin^2 A + \\cos^2 A) + 2(1) + 2(1) + \\operatorname{cosec}^2 A + \\sec^2 A$$\n$$= 1 + 2 + 2 + \\operatorname{cosec}^2 A + \\sec^2 A = 5 + \\operatorname{cosec}^2 A + \\sec^2 A$$\nNow substitute identities $\\operatorname{cosec}^2 A = 1 + \\cot^2 A$ and $\\sec^2 A = 1 + \\tan^2 A$:\n$$= 5 + (1 + \\cot^2 A) + (1 + \\tan^2 A) = 7 + \\tan^2 A + \\cot^2 A = \\text{RHS}$$\nHence proved!",
        "**उपपत्ति:**\nविस्तार करने पर:\n$$\\text{LHS} = \\sin^2 A + 2(1) + \\operatorname{cosec}^2 A + \\cos^2 A + 2(1) + \\sec^2 A$$\n$$= (\\sin^2 A + \\cos^2 A) + 4 + \\operatorname{cosec}^2 A + \\sec^2 A = 5 + (1 + \\cot^2 A) + (1 + \\tan^2 A) = 7 + \\tan^2 A + \\cot^2 A = \\text{RHS}।$$",
        "**સાબિતી:**\nવિસ્તરણ કરતાં:\n$$\\text{ડા.બા.} = (\\sin^2 A + \\cos^2 A) + 2 + 2 + \\operatorname{cosec}^2 A + \\sec^2 A$$\n$$= 1 + 4 + (1 + \\cot^2 A) + (1 + \\tan^2 A) = 7 + \\tan^2 A + \\cot^2 A = \\text{જ.બા.}$$",
        btype="theory",
        bloom="Analyze",
        diff="Intermediate",
        mins=2
    ))

    # 61. Exercise 8.3 Q4(ix) [Proof 9]
    blocks.append(make_theory(
        "C10M_CH8_EX8.3_Q4_9",
        "Exercise 8.3 Q4(ix): Prove (cosec A - sin A)(sec A - cos A) = 1 / (tan A + cot A)",
        "प्रश्नावली 8.3 Q4(ix): सिद्ध कीजिए कि (cosec A - sin A)(sec A - cos A) = 1 / (tan A + cot A)",
        "સ્વાધ્યાય 8.3 Q4(ix): સાબિત કરો કે (cosec A - sin A)(sec A - cos A) = 1 / (tan A + cot A)",
        "**Proof (Simplifying LHS & RHS):**\n$$\\text{LHS} = \\left(\\frac{1}{\\sin A} - \\sin A\\right)\\left(\\frac{1}{\\cos A} - \\cos A\\right) = \\left(\\frac{1 - \\sin^2 A}{\\sin A}\\right)\\left(\\frac{1 - \\cos^2 A}{\\cos A}\\right)$$\n$$= \\left(\\frac{\\cos^2 A}{\\sin A}\\right)\\left(\\frac{\\sin^2 A}{\\cos A}\\right) = \\cos A \\sin A$$\n\nNow simplify RHS:\n$$\\text{RHS} = \\frac{1}{\\tan A + \\cot A} = \\frac{1}{\\frac{\\sin A}{\\cos A} + \\frac{\\cos A}{\\sin A}} = \\frac{1}{\\frac{\\sin^2 A + \\cos^2 A}{\\sin A\\cos A}} = \\frac{1}{\\frac{1}{\\sin A\\cos A}} = \\sin A\\cos A$$\nSince $\\text{LHS} = \\text{RHS} = \\sin A\\cos A$, the identity is proved!",
        "**उपपत्ति:**\n$$\\text{LHS} = \\left(\\frac{\\cos^2 A}{\\sin A}\\right)\\left(\\frac{\\sin^2 A}{\\cos A}\\right) = \\sin A\\cos A$$\n$$\\text{RHS} = \\frac{1}{\\frac{\\sin A}{\\cos A} + \\frac{\\cos A}{\\sin A}} = \\frac{1}{\\frac{\\sin^2 A + \\cos^2 A}{\\sin A\\cos A}} = \\sin A\\cos A$$\nचूँकि LHS = RHS, अतः सिद्ध हुआ!",
        "**સાબિતી:**\n$$\\text{ડા.બા.} = \\left(\\frac{\\cos^2 A}{\\sin A}\\right)\\left(\\frac{\\sin^2 A}{\\cos A}\\right) = \\sin A\\cos A$$\n$$\\text{જ.બા.} = \\frac{1}{\\frac{\\sin A}{\\cos A} + \\frac{\\cos A}{\\sin A}} = \\frac{1}{\\frac{1}{\\sin A\\cos A}} = \\sin A\\cos A$$\nડા.બા. = જ.બા. હોવાથી સાબિત થાય છે!",
        btype="theory",
        bloom="Analyze",
        diff="Intermediate",
        mins=2
    ))

    # 62. Exercise 8.3 Q4(x) [Proof 10]
    blocks.append(make_theory(
        "C10M_CH8_EX8.3_Q4_10",
        "Exercise 8.3 Q4(x): Prove (1 + tan²A) / (1 + cot²A) = [(1 - tan A) / (1 - cot A)]² = tan²A",
        "प्रश्नावली 8.3 Q4(x): सिद्ध कीजिए कि (1 + tan²A) / (1 + cot²A) = [(1 - tan A) / (1 - cot A)]² = tan²A",
        "સ્વાધ્યાય 8.3 Q4(x): સાબિત કરો કે (1 + tan²A) / (1 + cot²A) = [(1 - tan A) / (1 - cot A)]² = tan²A",
        "**Proof:**\n**Part 1:**\n$$\\frac{1 + \\tan^2 A}{1 + \\cot^2 A} = \\frac{\\sec^2 A}{\\operatorname{cosec}^2 A} = \\frac{1/\\cos^2 A}{1/\\sin^2 A} = \\frac{\\sin^2 A}{\\cos^2 A} = \\tan^2 A$$\n\n**Part 2:**\n$$\\left(\\frac{1 - \\tan A}{1 - \\cot A}\\right)^2 = \\left(\\frac{1 - \\tan A}{1 - \\frac{1}{\\tan A}}\\right)^2 = \\left(\\frac{1 - \\tan A}{\\frac{\\tan A - 1}{\\tan A}}\\right)^2$$\n$$= \\left(\\frac{1 - \\tan A}{-(1 - \\tan A)} \\times \\tan A\\right)^2 = (-\\tan A)^2 = \\tan^2 A$$\nThus, both expressions equal $\\tan^2 A$. Hence proved!",
        "**उपपत्ति:**\n**भाग 1:** $\\frac{\\sec^2 A}{\\operatorname{cosec}^2 A} = \\frac{\\sin^2 A}{\\cos^2 A} = \\tan^2 A$।\n**भाग 2:** $\\left(\\frac{1 - \\tan A}{1 - 1/\\tan A}\\right)^2 = \\left(\\frac{1 - \\tan A}{\\frac{\\tan A - 1}{\\tan A}}\\right)^2 = (-\\tan A)^2 = \\tan^2 A$।\nअतः दोनों व्यंजक $\\tan^2 A$ के बराबर हैं!",
        "**સાબિતી:**\n**ભાગ 1:** $\\frac{\\sec^2 A}{\\operatorname{cosec}^2 A} = \\frac{\\sin^2 A}{\\cos^2 A} = \\tan^2 A$.\n**ભાગ 2:** $\\left(\\frac{1 - \\tan A}{1 - 1/\\tan A}\\right)^2 = (-\\tan A)^2 = \\tan^2 A$.\nબંને પદો $\\tan^2 A$ બરાબર સાબિત થાય છે!",
        btype="theory",
        bloom="Analyze",
        diff="Intermediate",
        mins=2
    ))

    # 63. Board HOTS Challenge 1
    blocks.append(make_quiz(
        "C10M_CH8_HOTS_Q1",
        "Board HOTS: If sec θ + tan θ = p, what is the value of sin θ?",
        "बोर्ड परीक्षा HOTS: यदि sec θ + tan θ = p, तो sin θ का मान क्या होगा?",
        "બોર્ડ HOTS પ્રશ્ન: જો sec θ + tan θ = p હોય, તો sin θ નું મૂલ્ય શું થાય?",
        [
            "(p² - 1) / (p² + 1)",
            "(p² + 1) / (p² - 1)",
            "(p² - 1) / 2p",
            "2p / (p² + 1)"
        ],
        [
            "(p² - 1) / (p² + 1)",
            "(p² + 1) / (p² - 1)",
            "(p² - 1) / 2p",
            "2p / (p² + 1)"
        ],
        [
            "(p² - 1) / (p² + 1)",
            "(p² + 1) / (p² - 1)",
            "(p² - 1) / 2p",
            "2p / (p² + 1)"
        ],
        0,
        "We know sec²θ - tan²θ = 1 ⇒ (sec θ - tan θ)(sec θ + tan θ) = 1.\nGiven sec θ + tan θ = p ⇒ sec θ - tan θ = 1/p.\nAdding the two equations: 2 sec θ = p + 1/p = (p² + 1)/p ⇒ sec θ = (p² + 1)/2p.\nSubtracting the two equations: 2 tan θ = p - 1/p = (p² - 1)/p ⇒ tan θ = (p² - 1)/2p.\nTherefore, sin θ = tan θ / sec θ = [(p² - 1)/2p] / [(p² + 1)/2p] = (p² - 1) / (p² + 1).",
        "sec θ + tan θ = p तथा sec θ - tan θ = 1/p।\nजोड़ने पर: sec θ = (p² + 1)/2p।\nघटाने पर: tan θ = (p² - 1)/2p।\nsin θ = tan θ / sec θ = (p² - 1) / (p² + 1)।",
        "sec θ + tan θ = p અને sec θ - tan θ = 1/p.\nસરવાળો કરતાં: sec θ = (p² + 1)/2p.\nબાદબાકી કરતાં: tan θ = (p² - 1)/2p.\nsin θ = tan θ / sec θ = (p² - 1) / (p² + 1).",
        bloom="Apply",
        diff="Advanced",
        mins=3
    ))

    # 64. Board HOTS Challenge 2
    blocks.append(make_quiz(
        "C10M_CH8_HOTS_Q2",
        "Board HOTS: If x = a sin θ + b cos θ and y = a cos θ - b sin θ, find the value of x² + y².",
        "बोर्ड परीक्षा HOTS: यदि x = a sin θ + b cos θ और y = a cos θ - b sin θ, तो x² + y² का मान ज्ञात कीजिए।",
        "બોર્ડ HOTS પ્રશ્ન: જો x = a sin θ + b cos θ અને y = a cos θ - b sin θ હોય, તો x² + y² નું મૂલ્ય શોધો.",
        [
            "a² + b²",
            "a² - b²",
            "1",
            "2ab"
        ],
        [
            "a² + b²",
            "a² - b²",
            "1",
            "2ab"
        ],
        [
            "a² + b²",
            "a² - b²",
            "1",
            "2ab"
        ],
        0,
        "x² = (a sin θ + b cos θ)² = a² sin²θ + b² cos²θ + 2ab sin θ cos θ.\ny² = (a cos θ - b sin θ)² = a² cos²θ + b² sin²θ - 2ab sin θ cos θ.\nAdding x² and y²:\nx² + y² = a²(sin²θ + cos²θ) + b²(cos²θ + sin²θ) + (2ab sin θ cos θ - 2ab sin θ cos θ)\n= a²(1) + b²(1) + 0 = a² + b².",
        "x² और y² का विस्तार करके जोड़ने पर:\nx² + y² = a²(sin²θ + cos²θ) + b²(cos²θ + sin²θ) = a² + b²।",
        "x² અને y² નો સરવાળો કરતાં:\nx² + y² = a²(sin²θ + cos²θ) + b²(cos²θ + sin²θ) = a² + b².",
        bloom="Apply",
        diff="Advanced",
        mins=3
    ))

    # 65. Board HOTS Challenge 3
    blocks.append(make_quiz(
        "C10M_CH8_HOTS_Q3",
        "Board HOTS: If sin θ + sin²θ = 1, find the value of the expression (cos²θ + cos⁴θ).",
        "बोर्ड परीक्षा HOTS: यदि sin θ + sin²θ = 1, तो व्यंजक (cos²θ + cos⁴θ) का मान ज्ञात कीजिए।",
        "બોર્ડ HOTS પ્રશ્ન: જો sin θ + sin²θ = 1 હોય, તો (cos²θ + cos⁴θ) નું મૂલ્ય શોધો.",
        [
            "1",
            "0",
            "2",
            "-1"
        ],
        [
            "1",
            "0",
            "2",
            "-1"
        ],
        [
            "1",
            "0",
            "2",
            "-1"
        ],
        0,
        "Given: sin θ + sin²θ = 1 ⇒ sin θ = 1 - sin²θ.\nSince 1 - sin²θ = cos²θ, we have:\nsin θ = cos²θ.\nSquaring both sides:\nsin²θ = (cos²θ)² = cos⁴θ.\nNow substitute into the required expression:\ncos²θ + cos⁴θ = sin θ + sin²θ.\nSince sin θ + sin²θ is given as 1, the value is exactly 1!",
        "दिया है: sin θ = 1 - sin²θ = cos²θ।\nदोनों पक्षों का वर्ग करने पर: sin²θ = cos⁴θ।\nअतः cos²θ + cos⁴θ = sin θ + sin²θ = 1।",
        "આપેલ છે: sin θ = 1 - sin²θ = cos²θ.\nબંને બાજુ વર્ગ કરતાં: sin²θ = cos⁴θ.\nતેથી cos²θ + cos⁴θ = sin θ + sin²θ = 1.",
        bloom="Apply",
        diff="Intermediate",
        mins=2
    ))

    # 66. Reflection Block (Step 6)
    blocks.append(make_theory(
        "C10M_CH8_44",
        "Reflection: The Socratic Triangle of Understanding",
        "चिंतन: समझ का सुकराती त्रिकोण",
        "ચિંતન: સમજણનો સોક્રેટીક ત્રિકોણ",
        "Take a quiet moment to reflect on your journey through Chapter 8:\n\n1. **The Core Philosophy:** Trigonometry is not about memorizing mysterious syllables (sin, cos, tan). It is the simple recognition that in any right triangle with a fixed angle, the ratios of sides never change, whether the triangle is drawn on a tiny postage stamp or connects three stars in deep space.\n2. **The Golden Bridge:** When you know one angle and one side, you can find ALL sides and angles! This is the superpower that makes modern engineering possible.\n3. **Can you explain to a friend:** Why is $\\sin^2\\theta + \\cos^2\\theta$ always equal to $1$? (Because it is literally the Pythagoras theorem $a^2 + b^2 = c^2$ divided by $c^2$!).",
        "अध्याय 8 की अपनी यात्रा पर कुछ क्षण विचार करें:\n\n1. **मूल दर्शन:** त्रिकोणमिति रहस्यमयी सूत्रों को रटने का विषय नहीं है। यह केवल यह बोध है कि किसी समकोण त्रिभुज में निश्चित कोण के लिए भुजाओं का अनुपात कभी नहीं बदलता — चाहे वह डाक टिकट पर बना हो या अंतरिक्ष के तीन तारों को जोड़ता हो।\n2. **सुनहरा सेतु:** यदि आपको एक कोण और एक भुजा ज्ञात हो, तो आप त्रिभुज की सभी भुजाएँ और कोण ज्ञात कर सकते हैं!\n3. **क्या आप अपने मित्र को समझा सकते हैं:** $\\sin^2\\theta + \\cos^2\\theta$ हमेशा 1 क्यों होता है? (क्योंकि यह वास्तव में पाइथागोरस प्रमेय $a^2 + b^2 = c^2$ को $c^2$ से भाग देने पर प्राप्त होता है!)।",
        "પ્રકરણ 8 માં તમે જે શીખ્યા તેના પર શાંતિથી વિચાર કરો:\n\n1. **મૂળભૂત સિદ્ધાંત:** ત્રિકોણમિતિ એ માત્ર સૂત્રો ગોખવાનો વિષય નથી. તે એ સાદી સમજ છે કે કોઈપણ કાટકોણ ત્રિકોણમાં જો ખૂણો નિશ્ચિત હોય તો બાજુઓનો ગુણોત્તર ક્યારેય બદલાતો નથી.\n2. **સુવર્ણ સેતુ:** જ્યારે તમને એક ખૂણો અને એક બાજુ ખબર હોય, ત્યારે તમે બાકીની બધી જ બાજુઓ અને ખૂણા શોધી શકો છો!\n3. **શું તમે મિત્રને સમજાવી શકો:** $\\sin^2\\theta + \\cos^2\\theta = 1$ હંમેશા કેમ થાય છે? (કારણ કે તે વાસ્તવમાં પાયથાગોરસ પ્રમેય $a^2 + b^2 = c^2$ ને $c^2$ વડે ભાગવાનું પરિણામ છે!).",
        btype="theory",
        bloom="Understand",
        diff="Beginner",
        mins=2
    ))

    # 67. Knowledge Graph Connection (Step 7)
    blocks.append(make_theory(
        "C10M_CH8_45",
        "Connection: Where Does Trigonometry Lead in Science & Life?",
        "संबंध: विज्ञान और जीवन में त्रिकोणमिति का भविष्य",
        "જોડાણ: વિજ્ઞાન અને વાસ્તવિક જીવનમાં ત્રિકોણમિતિ ક્યાં વપરાય છે?",
        "Trigonometry is the mathematical language of waves, cycles, and space:\n\n- **Chapter 9 (Some Applications of Trigonometry):** You will use $\\tan\\theta$ and $\\sin\\theta$ to find heights of lighthouses, distances of ships at sea, and widths of rivers using Angles of Elevation and Depression!\n- **Physics (Vectors & Projectiles):** Breaking velocity into horizontal ($v\\cos\\theta$) and vertical ($v\\sin\\theta$) components.\n- **Audio & Sound Waves:** Every musical note, speech signal, and radio wave is a pure sine wave ($y = A\\sin(\\omega t)$).\n- **Computer Graphics & Game Development:** Character rotation, camera angles in Unreal Engine and Unity, and ray tracing in games all run on trigonometric matrices!\n- **Space Exploration (ISRO & NASA):** Orbital mechanics, satellite trajectories, and planetary alignment calculations rely 100% on trigonometry.",
        "त्रिकोणमिति तरंगों, आवर्ती गतियों और अंतरिक्ष की सार्वभौमिक गणितीय भाषा है:\n\n- **अध्याय 9 (त्रिकोणमिति के कुछ अनुप्रयोग):** आप उन्नयन और अवनमन कोणों की सहायता से प्रकाशस्तंभों की ऊँचाई, जहाजों की दूरी और नदियों की चौड़ाई ज्ञात करेंगे!\n- **भौतिकी (सदिश और प्रक्षेप्य गति):** वेग को क्षैतिज ($v\\cos\\theta$) और ऊर्ध्वाधर ($v\\sin\\theta$) घटकों में वियोजित करना।\n- **ध्वनि और संगीत:** प्रत्येक संगीत स्वर और रेडियो तरंग एक शुद्ध साइन तरंग ($y = A\\sin(\\omega t)$) होती है।\n- **कंप्यूटर ग्राफिक्स और 3D गेमिंग:** वीडियो गेम में पात्रों का घूमना और कैमरा एंगल त्रिकोणमिति से ही नियंत्रित होते हैं।\n- **अंतरिक्ष विज्ञान (ISRO):** उपग्रहों की कक्षा और रॉकेट प्रक्षेपण त्रिकोणमिति के बिना असंभव हैं।",
        "ત્રિકોણમિતિ એ તરંગો, ચક્રીય ગતિ અને બ્રહ્માંડની ગાણિતિક ભાષા છે:\n\n- **પ્રકરણ 9 (ત્રિકોણમિતિના કેટલાક ઉપયોગો):** તમે ઉત્સેધકોણ અને અવસેધકોણનો ઉપયોગ કરીને ટાવરની ઊંચાઈ, વહાણો વચ્ચેનું અંતર અને નદીની પહોળાઈ શોધશો!\n- **ભૌતિક વિજ્ઞાન (સદિશો અને પ્રક્ષિપ્ત ગતિ):** વેગના સમક્ષિતિજ ($v\\cos\\theta$) અને શિરોલંબ ($v\\sin\\theta$) ઘટકો પાડવા.\n- **ધ્વનિ તરંગો અને સંગીત:** દરેક અવાજ અને રેડિયો તરંગ એ સાઈન તરંગ ($y = A\\sin(\\omega t)$) નું સ્વરૂપ છે.\n- **કોમ્પ્યુટર ગ્રાફિક્સ અને 3D ગેમિંગ:** વિડિયો ગેમ્સમાં 3D એનિમેશન અને કેમેરા એંગલ ત્રિકોણમિતિ દ્વારા સંચાલિત થાય છે.\n- **અવકાશ વિજ્ઞાન (ISRO):** ઉપગ્રહોની ભ્રમણકક્ષા અને રોકેટનું માર્ગ-દર્શન ત્રિકોણમિતિ પર આધારિત છે.",
        btype="theory",
        bloom="Understand",
        diff="Beginner",
        mins=2
    ))

    # 68. Mastery / Board Exam Blueprint (Step 8)
    blocks.append(make_theory(
        "C10M_CH8_46",
        "Mastery Blueprint: Guaranteed Board Exam Success Formula",
        "मास्टरी ब्लूप्रिंट: बोर्ड परीक्षा में शत-प्रतिशत सफलता का फॉर्मूला",
        "માસ્ટરી બ્લુપ્રિન્ટ: બોર્ડ પરીક્ષામાં સંપૂર્ણ ગુણ મેળવવાની ચાવી",
        "To score full marks (100%) in Introduction to Trigonometry in your Board Exam:\n\n1. **Label the Diagram First:** Always draw the right triangle clearly and mark the reference angle $\\theta$ before writing down ratios. Never confuse opposite side with adjacent side!\n2. **The 3-Second Verification:** Remember that $\\sin\\theta$ and $\\cos\\theta$ can NEVER be greater than $1$. If you get $\\sin\\theta = 5/4$, stop immediately and check your arithmetic!\n3. **Proving Identities:** Write 'LHS =' clearly. Convert all composite ratios to $\\sin\\theta$ and $\\cos\\theta$ if you don't immediately see a direct identity.\n4. **Rationalizing Denominators:** Always rationalize square roots in final answers (write $\\frac{3\\sqrt{2}}{2}$ instead of $\\frac{3}{\\sqrt{2}}$).\n5. **Unit Discipline:** Check if sides have units (cm, m). Angles must always have the degree symbol ($^\\circ$).",
        "बोर्ड परीक्षा में त्रिकोणमिति में शत-प्रतिशत अंक प्राप्त करने की महत्वपूर्ण रणनीतियाँ:\n\n1. **चित्र अवश्य बनाएँ:** अनुपात लिखने से पहले समकोण त्रिभुज बनाएँ और अभीष्ट कोण को स्पष्ट रूप से अंकित करें। सम्मुख और संलग्न भुजा में कभी भ्रमित न हों!\n2. **3 सेकंड की त्वरित जाँच:** $\\sin\\theta$ और $\\cos\\theta$ का मान कभी भी 1 से अधिक नहीं हो सकता। यदि आपका मान $5/4$ आए, तो तुरंत अपनी गणना पुनः जाँचें!\n3. **सर्वसमिका सिद्ध करना:** स्पष्ट रूप से 'LHS =' लिखें। यदि सीधा सूत्र न दिखे तो सभी पदों को $\\sin$ और $\\cos$ में बदल दें।\n4. **अंतिम उत्तर का परिमेयकरण:** अंतिम उत्तर में हर में अपरिमेय संख्या न छोड़ें।\n5. **इकाई का ध्यान रखें:** भुजाओं की इकाइयाँ (सेमी, मीटर) और कोणों पर डिग्री ($^\\circ$) का चिह्न अवश्य लगाएँ।",
        "બોર્ડ પરીક્ષામાં ત્રિકોણમિતિમાં પૂરા ગુણ મેળવવાની શ્રેષ્ઠ વ્યૂહરચના:\n\n1. **આકૃતિ અનિવાર્ય દોરો:** ગુણોત્તર લખતાં પહેલાં કાટકોણ ત્રિકોણ દોરી સંદર્ભ ખૂણો દર્શાવો. સામેની અને પાસેની બાજુમાં ક્યારેય ગૂંચવાશો નહીં!\n2. **ઝડપી ચકાસણી:** $\\sin\\theta$ અને $\\cos\\theta$ નું મૂલ્ય ક્યારેય 1 કરતાં મોટું ન હોઈ શકે. જો જવાબ 1 થી મોટો આવે તો તરત ગણતરી ફરી તપાસો!\n3. **નિત્યસમની સાબિતી:** સ્પષ્ટપણે 'ડા.બા. =' લખો. સીધો નિત્યસમ ન દેખાય તો બધા પદોને $\\sin$ અને $\\cos$ માં ફેરવી નાખો.\n4. **છેદનું સંમેયીકરણ:** અંતિમ જવાબમાં છેદમાં અસંમેય સંખ્યા ન રહેવી જોઈએ.\n5. **એકમોની કાળજી:** લંબાઈના એકમ (સેમી, મીટર) અને ખૂણા માટે અંશ ($^\\circ$) દર્શાવવાનું ક્યારેય ચૂકશો નહીં.",
        btype="theory",
        bloom="Apply",
        diff="Beginner",
        mins=2
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
    target_path = os.path.join(output_dir, 'ncert_class10_maths_ch8.json')
    
    with open(target_path, 'w', encoding='utf-8') as f:
        json.dump(chapter_data, f, indent=2, ensure_ascii=False)
        
    print(f"Generated {target_path} successfully with {len(chapter_data['blocks'])} blocks!")

if __name__ == "__main__":
    generate_chapter()
