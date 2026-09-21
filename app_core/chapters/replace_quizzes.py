import json

file_path = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_science_ch11.json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Keep everything except the 15 quizzes
blocks = data['blocks'][:-15]

quizzes = [
    {
        "id": "QUIZ_ncert_class10_science_ch11_1",
        "type": "quiz",
        "question": "What is the SI unit of electric current?",
        "question_hi": "विद्युत धारा की SI इकाई क्या है?",
        "options": ["Volt", "Ampere", "Ohm", "Watt"],
        "options_hi": ["वोल्ट", "एम्पीयर", "ओम", "वाट"],
        "correct_index": 1,
        "explanation": "The SI unit of electric current is Ampere (A). It is measured by an ammeter.",
        "explanation_hi": "विद्युत धारा की SI इकाई एम्पीयर (A) है। इसे एमीटर द्वारा मापा जाता है।"
    },
    {
        "id": "QUIZ_ncert_class10_science_ch11_2",
        "type": "quiz",
        "question": "Which of the following represents Ohm's Law?",
        "question_hi": "निम्नलिखित में से कौन ओम के नियम को दर्शाता है?",
        "options": ["V = I / R", "V = I × R", "I = V × R", "R = V × I"],
        "options_hi": ["V = I / R", "V = I × R", "I = V × R", "R = V × I"],
        "correct_index": 1,
        "explanation": "According to Ohm's Law, the potential difference V across a conductor is directly proportional to the current I. Thus, V = I × R.",
        "explanation_hi": "ओम के नियम के अनुसार, एक चालक के सिरों के बीच विभवांतर V उसमें प्रवाहित धारा I के अनुक्रमानुपाती होता है। इसलिए, V = I × R।"
    },
    {
        "id": "QUIZ_ncert_class10_science_ch11_3",
        "type": "quiz",
        "question": "How are an ammeter and a voltmeter connected in an electric circuit?",
        "question_hi": "विद्युत परिपथ में एमीटर और वोल्टमीटर को कैसे जोड़ा जाता है?",
        "options": ["Both in series", "Both in parallel", "Ammeter in series, Voltmeter in parallel", "Ammeter in parallel, Voltmeter in series"],
        "options_hi": ["दोनों श्रेणीक्रम में", "दोनों पार्श्वक्रम में", "एमीटर श्रेणीक्रम में, वोल्टमीटर पार्श्वक्रम में", "एमीटर पार्श्वक्रम में, वोल्टमीटर श्रेणीक्रम में"],
        "correct_index": 2,
        "explanation": "An ammeter is connected in series to measure current, while a voltmeter is connected in parallel to measure potential difference.",
        "explanation_hi": "एमीटर को धारा मापने के लिए श्रेणीक्रम में जोड़ा जाता है, जबकि वोल्टमीटर को विभवांतर मापने के लिए पार्श्वक्रम में जोड़ा जाता है।"
    },
    {
        "id": "QUIZ_ncert_class10_science_ch11_4",
        "type": "quiz",
        "question": "If two resistors of 2 Ω and 3 Ω are connected in series, what is their equivalent resistance?",
        "question_hi": "यदि 2 Ω और 3 Ω के दो प्रतिरोधक श्रेणीक्रम में जुड़े हैं, तो उनका समतुल्य प्रतिरोध क्या होगा?",
        "options": ["5 Ω", "1.2 Ω", "6 Ω", "1 Ω"],
        "options_hi": ["5 Ω", "1.2 Ω", "6 Ω", "1 Ω"],
        "correct_index": 0,
        "explanation": "In series combination, Rs = R1 + R2 = 2 + 3 = 5 Ω.",
        "explanation_hi": "श्रेणीक्रम संयोजन में, Rs = R1 + R2 = 2 + 3 = 5 Ω।"
    },
    {
        "id": "QUIZ_ncert_class10_science_ch11_5",
        "type": "quiz",
        "question": "Which material is generally used for making the filament of an electric bulb?",
        "question_hi": "विद्युत बल्ब का फिलामेंट बनाने के लिए आमतौर पर किस सामग्री का उपयोग किया जाता है?",
        "options": ["Copper", "Aluminium", "Tungsten", "Iron"],
        "options_hi": ["तांबा", "एल्युमिनियम", "टंगस्टन", "लोहा"],
        "correct_index": 2,
        "explanation": "Tungsten is used for making bulb filaments because of its very high melting point and high resistivity.",
        "explanation_hi": "बल्ब के फिलामेंट बनाने के लिए टंगस्टन का उपयोग किया जाता है क्योंकि इसका गलनांक बहुत अधिक होता है और प्रतिरोधकता उच्च होती है।"
    },
    {
        "id": "QUIZ_ncert_class10_science_ch11_6",
        "type": "quiz",
        "question": "What is the commercial unit of electrical energy?",
        "question_hi": "विद्युत ऊर्जा की व्यावसायिक इकाई क्या है?",
        "options": ["Joule", "Watt", "Kilowatt", "Kilowatt-hour (kWh)"],
        "options_hi": ["जूल", "वाट", "किलोवाट", "किलोवाट-घंटा (kWh)"],
        "correct_index": 3,
        "explanation": "The commercial unit of electrical energy is Kilowatt-hour (kWh), commonly known as 'unit'. 1 kWh = 3.6 × 10^6 Joules.",
        "explanation_hi": "विद्युत ऊर्जा की व्यावसायिक इकाई किलोवाट-घंटा (kWh) है, जिसे आम तौर पर 'यूनिट' कहा जाता है। 1 kWh = 3.6 × 10^6 जूल।"
    },
    {
        "id": "QUIZ_ncert_class10_science_ch11_7",
        "type": "quiz",
        "question": "What happens to the resistance of a wire if its length is doubled?",
        "question_hi": "यदि किसी तार की लंबाई दोगुनी कर दी जाए, तो उसके प्रतिरोध पर क्या प्रभाव पड़ेगा?",
        "options": ["It becomes half", "It doubles", "It quadruples", "It remains unchanged"],
        "options_hi": ["यह आधा हो जाता है", "यह दोगुना हो जाता है", "यह चार गुना हो जाता है", "यह अपरिवर्तित रहता है"],
        "correct_index": 1,
        "explanation": "Resistance is directly proportional to length (R ∝ L). If length is doubled, resistance also doubles.",
        "explanation_hi": "प्रतिरोध लंबाई के अनुक्रमानुपाती होता है (R ∝ L)। यदि लंबाई दोगुनी हो जाती है, तो प्रतिरोध भी दोगुना हो जाता है।"
    },
    {
        "id": "QUIZ_ncert_class10_science_ch11_8",
        "type": "quiz",
        "question": "Which of the following terms does NOT represent electrical power in a circuit?",
        "question_hi": "निम्नलिखित में से कौन सा पद किसी परिपथ में विद्युत शक्ति को नहीं दर्शाता है?",
        "options": ["I²R", "IR²", "VI", "V²/R"],
        "options_hi": ["I²R", "IR²", "VI", "V²/R"],
        "correct_index": 1,
        "explanation": "Power P = VI. Substituting V = IR gives P = I²R. Substituting I = V/R gives P = V²/R. Thus, IR² does not represent power.",
        "explanation_hi": "शक्ति P = VI. V = IR रखने पर P = I²R मिलता है। I = V/R रखने पर P = V²/R मिलता है। अतः IR² शक्ति को नहीं दर्शाता है।"
    },
    {
        "id": "QUIZ_ncert_class10_science_ch11_9",
        "type": "quiz",
        "question": "What is the SI unit of electrical resistivity?",
        "question_hi": "विद्युत प्रतिरोधकता की SI इकाई क्या है?",
        "options": ["Ohm (Ω)", "Ohm-meter (Ω·m)", "Ohm/meter (Ω/m)", "Ampere/meter (A/m)"],
        "options_hi": ["ओम (Ω)", "ओम-मीटर (Ω·m)", "ओम/मीटर (Ω/m)", "एम्पीयर/मीटर (A/m)"],
        "correct_index": 1,
        "explanation": "The SI unit of resistivity is Ohm-meter (Ω·m). It is an intrinsic property of the material.",
        "explanation_hi": "प्रतिरोधकता की SI इकाई ओम-मीटर (Ω·m) है। यह सामग्री का एक आंतरिक गुण है।"
    },
    {
        "id": "QUIZ_ncert_class10_science_ch11_10",
        "type": "quiz",
        "question": "Why are alloys like Nichrome used in electrical heating devices?",
        "question_hi": "विद्युत हीटिंग उपकरणों में नाइक्रोम जैसी मिश्र धातुओं का उपयोग क्यों किया जाता है?",
        "options": ["Low resistivity and low melting point", "High resistivity and low melting point", "High resistivity and they do not oxidize easily at high temperatures", "Low resistivity and they do not oxidize easily"],
        "options_hi": ["कम प्रतिरोधकता और कम गलनांक", "उच्च प्रतिरोधकता और कम गलनांक", "उच्च प्रतिरोधकता और वे उच्च तापमान पर आसानी से ऑक्सीकृत नहीं होते", "कम प्रतिरोधकता और वे आसानी से ऑक्सीकृत नहीं होते"],
        "correct_index": 2,
        "explanation": "Alloys have high resistivity and do not undergo oxidation (burn) easily even at high temperatures.",
        "explanation_hi": "मिश्र धातुओं की प्रतिरोधकता उच्च होती है और उच्च तापमान पर भी वे आसानी से ऑक्सीकृत (जलते) नहीं हैं।"
    },
    {
        "id": "QUIZ_ncert_class10_science_ch11_11",
        "type": "quiz",
        "question": "According to Joule's Law of Heating, heat produced in a resistor is directly proportional to:",
        "question_hi": "जूल के तापन नियम के अनुसार, किसी प्रतिरोधक में उत्पन्न ऊष्मा किसके अनुक्रमानुपाती होती है?",
        "options": ["Square of the current (I²)", "Square of the resistance (R²)", "Square root of time (√t)", "Inverse of current (1/I)"],
        "options_hi": ["धारा का वर्ग (I²)", "प्रतिरोध का वर्ग (R²)", "समय का वर्गमूल (√t)", "धारा का व्युत्क्रम (1/I)"],
        "correct_index": 0,
        "explanation": "According to Joule's Law of Heating, H = I²Rt. Thus, heat produced is directly proportional to the square of current.",
        "explanation_hi": "जूल के तापन नियम के अनुसार, H = I²Rt। इस प्रकार, उत्पन्न ऊष्मा धारा के वर्ग के अनुक्रमानुपाती होती है।"
    },
    {
        "id": "QUIZ_ncert_class10_science_ch11_12",
        "type": "quiz",
        "question": "What is the equivalent resistance when two 4 Ω resistors are connected in parallel?",
        "question_hi": "जब दो 4 Ω के प्रतिरोधक पार्श्वक्रम में जुड़े हों, तो समतुल्य प्रतिरोध क्या होगा?",
        "options": ["8 Ω", "2 Ω", "4 Ω", "1 Ω"],
        "options_hi": ["8 Ω", "2 Ω", "4 Ω", "1 Ω"],
        "correct_index": 1,
        "explanation": "In parallel combination, 1/Rp = 1/R1 + 1/R2 = 1/4 + 1/4 = 2/4 = 1/2. Therefore, Rp = 2 Ω.",
        "explanation_hi": "पार्श्वक्रम संयोजन में, 1/Rp = 1/R1 + 1/R2 = 1/4 + 1/4 = 2/4 = 1/2। इसलिए, Rp = 2 Ω।"
    },
    {
        "id": "QUIZ_ncert_class10_science_ch11_13",
        "type": "quiz",
        "question": "An electric iron draws a current of 5 A when connected to a 220 V line. What is its power?",
        "question_hi": "एक विद्युत इस्त्री (iron) 220 V लाइन से जुड़ने पर 5 A की धारा लेती है। इसकी शक्ति क्या है?",
        "options": ["1100 W", "225 W", "44 W", "11000 W"],
        "options_hi": ["1100 W", "225 W", "44 W", "11000 W"],
        "correct_index": 0,
        "explanation": "Power P = V × I = 220 × 5 = 1100 W.",
        "explanation_hi": "शक्ति P = V × I = 220 × 5 = 1100 W।"
    },
    {
        "id": "QUIZ_ncert_class10_science_ch11_14",
        "type": "quiz",
        "question": "Which of the following does NOT affect the resistance of a conductor?",
        "question_hi": "निम्नलिखित में से कौन सा कारक किसी चालक के प्रतिरोध को प्रभावित नहीं करता है?",
        "options": ["Length of the conductor", "Cross-sectional area", "Material of the conductor", "Shape of the cross-section (keeping area constant)"],
        "options_hi": ["चालक की लंबाई", "अनुप्रस्थ काट का क्षेत्रफल", "चालक की सामग्री", "अनुप्रस्थ काट का आकार (क्षेत्रफल समान रखते हुए)"],
        "correct_index": 3,
        "explanation": "Resistance depends on length, cross-sectional area, material nature, and temperature. It does not depend on the specific shape if the total area is unchanged.",
        "explanation_hi": "प्रतिरोध लंबाई, अनुप्रस्थ काट के क्षेत्रफल, सामग्री की प्रकृति और तापमान पर निर्भर करता है। यदि कुल क्षेत्रफल अपरिवर्तित है, तो यह विशिष्ट आकार पर निर्भर नहीं करता है।"
    },
    {
        "id": "QUIZ_ncert_class10_science_ch11_15",
        "type": "quiz",
        "question": "A safety device based on the heating effect of electric current is known as:",
        "question_hi": "विद्युत धारा के तापन प्रभाव पर आधारित सुरक्षा युक्ति को क्या कहा जाता है?",
        "options": ["Electric generator", "Electric fuse", "Electric motor", "Voltmeter"],
        "options_hi": ["विद्युत जनरेटर", "विद्युत फ्यूज", "विद्युत मोटर", "वोल्टमीटर"],
        "correct_index": 1,
        "explanation": "An electric fuse melts and breaks the circuit if excessive current flows, protecting appliances. It is based on Joule's heating effect.",
        "explanation_hi": "अत्यधिक धारा प्रवाहित होने पर विद्युत फ्यूज पिघल जाता है और परिपथ को तोड़ देता है, जिससे उपकरणों की सुरक्षा होती है। यह जूल के तापन प्रभाव पर आधारित है।"
    }
]

data['blocks'] = blocks + quizzes

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
