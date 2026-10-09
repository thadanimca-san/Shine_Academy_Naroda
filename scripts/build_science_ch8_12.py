import json
import os

def create_ch8_force():
    return [
        # Step 1: Hook
        {
            "id": "KOBJ_CLASS9_SCI_CH8_HOOK",
            "type": "real_world_example",
            "title": "Step 1: Hook - Why Do Seatbelts Save Lives?",
            "title_hi": "चरण 1: हुक - सीटबेल्ट जीवन क्यों बचाते हैं?",
            "title_gu": "પગલું 1: હૂક - સીટબિલ્ટ શા માટે જીવન બચાવે છે?",
            "body": "When a fast-moving car brakes suddenly, your body keeps moving forward! Why? Because of Inertia—the resistance of any physical object to any change in its velocity.",
            "body_hi": "जब एक तेज गति से चलती कार अचानक ब्रेक लगाती है, तो आपका शरीर आगे बढ़ता रहता है! क्यों? जड़त्व (Inertia) के कारण—किसी भी भौतिक वस्तु का अपने वेग में परिवर्तन का विरोध।",
            "body_gu": "જ્યારે ખૂબ જ ઝડપથી ચાલતી કાર અચાનક બ્રેક મારે છે, ત્યારે તમારું શરીર આગળ વધતું રહે છે! શા માટે? જડત્વ (Inertia) ને કારણે—કોઈપણ ભૌતિક પદાર્થનો તેના વેગમાં ફેરફારનો પ્રતિકાર।",
            "visual_prompt": "Animation of a dummy in a car crash test demonstrating inertia without and with a seatbelt."
        },
        # Step 2: Socratic
        {
            "id": "KOBJ_CLASS9_SCI_CH8_SOCRATIC_1",
            "type": "quiz",
            "title": "Step 2: Socratic Thinking - Balanced vs Unbalanced Force",
            "title_hi": "चरण 2: सुकराती सोच - संतुलित बनाम असंतुलित बल",
            "title_gu": "પગલું 2: સોક્રેટિક વિચારણા - સંતુલિત વિ અસંતુલિત બળ",
            "question": "Two teams pull a rope in Tug-of-War with equal force of 500 N in opposite directions. What happens to the rope?",
            "question_hi": "रस्साकशी के खेल में दो टीमें विपरीत दिशाओं में 500 N के समान बल से रस्सी खींचती हैं। रस्सी का क्या होता है?",
            "question_gu": "દોડમદોડ (ટગ-ઓફ-વોર) માં બે ટીમો વિરુદ્ધ દિશાઓમાં 500 N ના સમાન બળથી દોરડું ખેંચે છે। દોરડાનું શું થાય છે?",
            "options": [
                "It accelerates to the left",
                "It accelerates to the right",
                "It remains stationary because net force is zero",
                "It breaks immediately"
            ],
            "options_hi": [
                "यह बाईं ओर त्वरित होता है",
                "यह दाईं ओर त्वरित होता है",
                "यह स्थिर रहता है क्योंकि परिणामी बल शून्य है",
                "यह तुरंत टूट जाता है"
            ],
            "options_gu": [
                "તે ડાબી તરફ પ્રવેગિત થાય છે",
                "તે જમણી તરફ પ્રવેગિત થાય છે",
                "તે સ્થિર રહે છે કારણ કે પરિણામી બળ શૂન્ય છે",
                "તે તરત જ તૂટી જાય છે"
            ],
            "correct_index": 2,
            "explanation": "Balanced forces have equal magnitude and opposite directions, resulting in zero net force. An unbalanced force is required to change an object's state of motion.",
            "explanation_hi": "संतुलित बलों का परिमाण समान और दिशा विपरीत होती है, जिसके परिणामस्वरूप कुल बल शून्य होता है। किसी वस्तु की गति की स्थिति को बदलने के लिए असंतुलित बल की आवश्यकता होती है।",
            "explanation_gu": "સંતુલિત બળોનું મૂલ્ય સમાન અને દિશા વિરુદ્ધ હોય છે, જેના પરિણામે પરિણામી બળ શૂન્ય થાય છે। પદાર્થની ગતિની સ્થિતિ બદલવા માટે અસંતુલિત બળ જરૂરી છે।"
        },
        # Step 4: Theory - Newton's 1st Law & Inertia
        {
            "id": "KOBJ_CLASS9_SCI_CH8_THEORY_1ST_LAW",
            "type": "theory",
            "title": "Step 4: Reveal - Newton's First Law of Motion & Inertia",
            "title_hi": "चरण 4: प्रकटीकरण - न्यूटन का गति का पहला नियम और जड़त्व",
            "title_gu": "પગલું 4: પર્દાફાશ - ન્યૂટનનો ગતિનો પ્રથમ નિયમ અને જડત્વ",
            "body": "1. **Newton's First Law**: An object remains in a state of rest or of uniform motion in a straight line unless acted upon by an external unbalanced force.\n\n2. **Inertia**: The natural tendency of objects to resist a change in their state of rest or motion. Mass is the measure of inertia. Heavy objects have more inertia.",
            "body_hi": "1. **न्यूटन का पहला नियम**: प्रत्येक वस्तु अपनी विरामवस्था या एक सीधी रेखा में एकसमान गति की अवस्था में बनी रहती है जब तक कि उस पर कोई बाहरी असंतुलित बल कार्य न करे।\n\n2. **जड़त्व (Inertia)**: वस्तुओं की अपनी विरामवस्था या गति की अवस्था में परिवर्तन का विरोध करने की प्राकृतिक प्रवृत्ति। द्रव्यमान जड़त्व की माप है। भारी वस्तुओं में अधिक जड़त्व होता है।",
            "body_gu": "1. **ન્યૂટનનો પ્રથમ નિયમ**: દરેક પદાર્થ જ્યાં સુધી તેના પર કોઈ બાહ્ય અસંતુલિત બળ ન લાગે ત્યાં સુધી સ્થિર અવસ્થામાં અથવા સીધી રેખામાં એકસમાન ગતિની અવસ્થામાં જળવાઈ રહે છે।\n\n2. **જડત્વ (Inertia)**: પદાર્થોની પોતાની સ્થિર અવસ્થા અથવા ગતિની અવસ્થામાં ફેરફારનો પ્રતિકાર કરવાની કુદરતી વૃત્તિ। દ્રવ્યમાન એ જડત્વનું માપ છે। ભારે પદાર્થોમાં વધુ જડત્વ હોય છે।"
        },
        # Step 4: Theory - Newton's 2nd Law & Momentum
        {
            "id": "KOBJ_CLASS9_SCI_CH8_THEORY_2ND_LAW",
            "type": "theory",
            "title": "Step 4: Reveal - Momentum & Newton's Second Law",
            "title_hi": "चरण 4: प्रकटीकरण - संवेग और न्यूटन का दूसरा नियम",
            "title_gu": "પગલું 4: પર્દાફાશ - સંવેગ અને ન્યૂટનનો બીજો નિયમ",
            "body": "1. **Momentum ($p$)**: The product of mass ($m$) and velocity ($v$).\n$$p = m \\cdot v$$\nSI Unit: $\\text{kg m/s}$. Vector quantity.\n\n2. **Newton's Second Law**: The rate of change of momentum of an object is proportional to the applied unbalanced force in the direction of force.\n$$F = m \\cdot a$$\nWhere $F$ = Force in Newtons (N), $m$ = mass (kg), $a$ = acceleration ($\\text{m/s}^2$). SI Unit: Newton (N) or $\\text{kg m/s}^2$.",
            "body_hi": "1. **संवेग ($p$)**: द्रव्यमान ($m$) और वेग ($v$) का गुणनफल।\n$$p = m \\cdot v$$\nSI इकाई: $\\text{kg m/s}$। सदिश राशि।\n\n2. **न्यूटन का दूसरा नियम**: किसी वस्तु के संवेग में परिवर्तन की दर उस पर लगाए गए असंतुलित बल के समानुपाती होती है।\n$$F = m \\cdot a$$\nजहाँ $F$ = बल (N), $m$ = द्रव्यमान (kg), $a$ = त्वरण ($\\text{m/s}^2$)। SI इकाई: न्यूटन (N)।",
            "body_gu": "1. **સંવેગ ($p$)**: દ્રવ્યમાન ($m$) અને વેગ ($v$) નો ગુણાકાર।\n$$p = m \\cdot v$$\nSI એકમ: $\\text{kg m/s}$। સદિશ રાશિ।\n\n2. **ન્યૂટનનો બીજો નિયમ**: પદાર્થના સંવેગમાં થતા ફેરફારનો દર તેના પર લાગતા અસંતુલિત બળના સમપ્રમાણમાં હોય છે।\n$$F = m \\cdot a$$\nજ્યાં $F$ = બળ (N), $m$ = દ્રવ્યમાન (kg), $a$ = પ્રવેગ ($\\text{m/s}^2$) । SI એકમ: ન્યૂટન (N) ।"
        },
        # Step 4: Theory - Newton's 3rd Law & Conservation of Momentum
        {
            "id": "KOBJ_CLASS9_SCI_CH8_THEORY_3RD_LAW",
            "type": "theory",
            "title": "Step 4: Reveal - Newton's Third Law & Conservation of Momentum",
            "title_hi": "चरण 4: प्रकटीकरण - न्यूटन का तीसरा नियम और संवेग संरक्षण",
            "title_gu": "પગલું 4: પર્દાફાશ - ન્યૂટનનો ત્રીજો નિયમ અને સંવેગનું સંરક્ષણ",
            "body": "1. **Newton's Third Law**: To every action, there is an equal and opposite reaction, and they act on two different bodies.\nExample: Rocket propulsion, Recoil of a gun.\n\n2. **Law of Conservation of Momentum**: In an isolated system (no external force), total momentum before collision equals total momentum after collision.\n$$m_1 u_1 + m_2 u_2 = m_1 v_1 + m_2 v_2$$",
            "body_hi": "1. **न्यूटन का तीसरा नियम**: प्रत्येक क्रिया के बराबर और विपरीत प्रतिक्रिया होती है, और वे दो अलग-अलग पिंडों पर कार्य करती हैं।\nउदाहरण: रॉकेट प्रणोदन, बंदूक का पीछे हटना (Recoil)।\n\n2. **संवेग संरक्षण का नियम**: किसी पृथक निकाय में, टक्कर से पहले का कुल संवेग टक्कर के बाद के कुल संवेग के बराबर होता है।\n$$m_1 u_1 + m_2 u_2 = m_1 v_1 + m_2 v_2$$",
            "body_gu": "1. **ન્યૂટનનો ત્રીજો નિયમ**: દરેક ક્રિયાબળ સામે સમાન મૂલ્યનું અને વિરુદ્ધ દિશાનું અપ્રત્યાઘાતી પ્રતિક્રિયાબળ હોય છે, અને તે બે અલગ પદાર્થો પર લાગે છે।\nઉદાહરણ: રોકેટ પ્રક્ષેપણ, બંદૂકનો પાછળ તરફનો આંચકો (Recoil) ।\n\n2. **સંવેગ સંરક્ષણનો નિયમ**: કોઈ અલગ કરેલા તંત્રમાં, અથડામણ પહેલાંનો કુલ સંવેગ અથડામણ પછીના કુલ સંવેગ જેટલો જ હોય છે।\n$$m_1 u_1 + m_2 u_2 = m_1 v_1 + m_2 v_2$$"
        },
        # Textbook Exercises
        {
            "id": "KOBJ_CLASS9_SCI_CH8_EX_1",
            "type": "quiz",
            "title": "Textbook Exercise 1: Force Required to Accelerate Mass",
            "title_hi": "पाठ्यपुस्तक अभ्यास 1: द्रव्यमान को त्वरित करने के लिए आवश्यक बल",
            "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 1: દ્રવ્યમાનને પ્રવેગિત કરવા જરૂરી બળ",
            "question": "Which would require a greater force: accelerating a 2 kg mass at 5 m/s² or a 4 kg mass at 2 m/s²?",
            "question_hi": "किसमें अधिक बल की आवश्यकता होगी: 2 kg द्रव्यमान को 5 m/s² पर त्वरित करना या 4 kg द्रव्यमान को 2 m/s² पर त्वरित करना?",
            "question_gu": "કોના માટે વધુ બળની જરૂર પડશે: 2 kg દ્રવ્યમાનને 5 m/s² પર પ્રવેગિત કરવા કે 4 kg દ્રવ્યમાનને 2 m/s² પર પ્રવેગિત કરવા?",
            "options": [
                "Accelerating 2 kg mass at 5 m/s² (10 N vs 8 N)",
                "Accelerating 4 kg mass at 2 m/s² (8 N vs 10 N)",
                "Both require equal force of 10 N",
                "Both require equal force of 8 N"
            ],
            "options_hi": [
                "2 kg द्रव्यमान को 5 m/s² पर त्वरित करना (10 N बनाम 8 N)",
                "4 kg द्रव्यमान को 2 m/s² पर त्वरित करना (8 N बनाम 10 N)",
                "दोनों को 10 N के समान बल की आवश्यकता होती है",
                "दोनों को 8 N के समान बल की आवश्यकता होती है"
            ],
            "options_gu": [
                "2 kg દ્રવ્યમાનને 5 m/s² પર પ્રવેગિત કરવું (10 N વિ 8 N)",
                "4 kg દ્રવ્યમાનને 2 m/s² પર પ્રવેગિત કરવું (8 N વિ 10 N)",
                "બંને માટે 10 N ના સમાન બળની જરૂર છે",
                "બંને માટે 8 N ના સમાન બળની જરૂર છે"
            ],
            "correct_index": 0,
            "explanation": "F1 = m1 × a1 = 2 × 5 = 10 N. F2 = m2 × a2 = 4 × 2 = 8 N. Therefore, accelerating a 2 kg mass at 5 m/s² requires greater force (10 N > 8 N).",
            "explanation_hi": "F1 = 2 × 5 = 10 N। F2 = 4 × 2 = 8 N। इसलिए, 2 kg द्रव्यमान को 5 m/s² पर त्वरित करने में अधिक बल लगता है (10 N > 8 N)।",
            "explanation_gu": "F1 = 2 × 5 = 10 N। F2 = 4 × 2 = 8 N। તેથી 2 kg દ્રવ્યમાનને 5 m/s² પર પ્રવેગિત કરવા વધુ બળ જરૂરી છે (10 N > 8 N) ।"
        },
        {
            "id": "KOBJ_CLASS9_SCI_CH8_EX_2",
            "type": "quiz",
            "title": "Textbook Exercise 2: Recoil Velocity of Gun",
            "title_hi": "पाठ्यपुस्तक अभ्यास 2: बंदूक का प्रतिक्षेप वेग",
            "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 2: બંદૂકનો રીકોઇલ વેગ",
            "question": "A bullet of mass 20 g is horizontally fired with a velocity 150 m/s from a pistol of mass 2 kg. What is the recoil velocity of the pistol?",
            "question_hi": "2 kg की पिस्टल से 20 ग्राम की गोली 150 m/s के वेग से क्षैतिज रूप से दागी जाती है। पिस्टल का प्रतिक्षेप वेग (Recoil Velocity) क्या है?",
            "question_gu": "2 kg ની પિસ્તોલમાંથી 20 g ની ગોળી 150 m/s ના વેગથી છોડવામાં આવે છે। પિસ્તોલનો રીકોઇલ વેગ કેટલો હશે?",
            "options": [
                "-1.5 m/s",
                "-15 m/s",
                "1.5 m/s",
                "-3.0 m/s"
            ],
            "options_hi": [
                "-1.5 m/s",
                "-15 m/s",
                "1.5 m/s",
                "-3.0 m/s"
            ],
            "options_gu": [
                "-1.5 m/s",
                "-15 m/s",
                "1.5 m/s",
                "-3.0 m/s"
            ],
            "correct_index": 0,
            "explanation": "Mass of bullet m1 = 0.02 kg, velocity v1 = 150 m/s. Mass of pistol m2 = 2 kg, recoil velocity v2. Total initial momentum = 0. By conservation of momentum: m1*v1 + m2*v2 = 0 => (0.02 * 150) + 2*v2 = 0 => 3 + 2*v2 = 0 => v2 = -1.5 m/s.",
            "explanation_hi": "गोली का द्रव्यमान m1 = 0.02 kg, v1 = 150 m/s। पिस्टल का द्रव्यमान m2 = 2 kg। m1*v1 + m2*v2 = 0 => 3 + 2*v2 = 0 => v2 = -1.5 m/s।",
            "explanation_gu": "ગોળીનું દ્રવ્યમાન m1 = 0.02 kg, v1 = 150 m/s। પિસ્તોલનું દ્રવ્યમાન m2 = 2 kg। m1*v1 + m2*v2 = 0 => 3 + 2*v2 = 0 => v2 = -1.5 m/s।"
        },
        # Reflection, Connection, Mastery
        {
            "id": "KOBJ_CLASS9_SCI_CH8_REFLECTION",
            "type": "reflection",
            "title": "Step 6: Reflection - Action and Reaction",
            "title_hi": "चरण 6: विचार-विमर्श - क्रिया और प्रतिक्रिया",
            "title_gu": "પગલું 6: મનન - ક્રિયા અને પ્રતિક્રિયા",
            "body": "If action and reaction forces are always equal and opposite, why don't they cancel each other out? (Hint: They act on two completely different objects!)",
            "body_hi": "यदि क्रिया और प्रतिक्रिया बल हमेशा बराबर और विपरीत होते हैं, तो वे एक-दूसरे को निरस्त क्यों नहीं करते? (संकेत: वे दो पूरी तरह से अलग-अलग वस्तुओं पर कार्य करते हैं!)",
            "body_gu": "જો ક્રિયાબળ અને પ્રતિક્રિયાબળ હંમેશાં સમાન અને વિરુદ્ધ હોય, તો તેઓ એકબીજાની અસર કેમ રદ કરતા નથી? (સંકેત: તેઓ બે અલગ અલગ પદાર્થો પર લાગે છે!)"
        },
        {
            "id": "KOBJ_CLASS9_SCI_CH8_CONNECTION",
            "type": "connection",
            "title": "Step 7: Knowledge Graph Connection",
            "title_hi": "चरण 7: ज्ञान ग्राफ संबंध",
            "title_gu": "પગલું 7: જ્ઞાન ગ્રાફ જોડાણ",
            "body": "Prerequisite: Motion (Kinematics). Next Chapter: Gravitation (Universal force of attraction). Future Topics: Work, Energy & Impulse.",
            "body_hi": "पूर्व-आवश्यकता: गति। अगला अध्याय: गुरुत्वाकर्षण। भविष्य के विषय: कार्य, ऊर्जा और आवेग।",
            "body_gu": "પૂર્વ-જરૂરિયાત: ગતિ। આગળનું પ્રકરણ: ગુરુત્વાકર્ષણ। ભવિષ્યના વિષયો: કાર્ય, ઊર્જા અને આવેગ।"
        },
        {
            "id": "KOBJ_CLASS9_SCI_CH8_MASTERY",
            "type": "mastery",
            "title": "Step 8: Mastery - Rocket Science Challenge",
            "title_hi": "चरण 8: महारत - रॉकेट विज्ञान चुनौती",
            "title_gu": "પગલું 8: માસ્ટરી - રોકેટ વિજ્ઞાન પડકાર",
            "body": "Explain rocket launch using Newton's Third Law: The high-speed backward ejection of hot exhaust gases (Action) creates a massive forward thrust on the rocket (Reaction).",
            "body_hi": "न्यूटन के तीसरे नियम का उपयोग करके रॉकेट प्रक्षेपण की व्याख्या करें: गर्म निकास गैसों की उच्च गति से पीछे की ओर निकास (क्रिया) रॉकेट पर एक बड़ा आगे की ओर प्रणोद (प्रतिक्रिया) पैदा करता है।",
            "body_gu": "ન્યૂટનના ત્રીજા નિયમનો ઉપયોગ કરીને રોકેટ લૉન્ચ સમજાવો: ગરમ વાયુઓનું પાછળની તરફ વેગથી બહાર નીકળવું (ક્રિયા) રોકેટ પર આગળ તરફ મોટો ધક્કો (પ્રતિક્રિયા) પેદા કરે છે।"
        }
    ]

def create_ch9_gravitation():
    return [
        {
            "id": "KOBJ_CLASS9_SCI_CH9_HOOK",
            "type": "real_world_example",
            "title": "Step 1: Hook - Why Doesn't the Moon Fall onto Earth?",
            "title_hi": "चरण 1: हुक - चंद्रमा पृथ्वी पर क्यों नहीं गिरता?",
            "title_gu": "પગલું 1: હૂક - ચંદ્ર પૃથ્વી પર કેમ પડતો નથી?",
            "body": "An apple falls to the Earth, but the Moon revolves around Earth continuously! Why? Gravity provides the centripetal force required to keep the Moon in its orbit without letting it crash into Earth.",
            "body_hi": "एक सेब पृथ्वी पर गिरता है, लेकिन चंद्रमा लगातार पृथ्वी का चक्कर लगाता है! क्यों? गुरुत्वाकर्षण चंद्रमा को अपनी कक्षा में बनाए रखने के लिए आवश्यक अभिकेंद्री बल (Centripetal force) प्रदान करता है।",
            "body_gu": "સફરજન પૃથ્વી પર પડે છે, પરંતુ ચંદ્ર સતત પૃથ્વીની આસપાસ ફરે છે! શા માટે? ગુરુત્વાકર્ષણ ચંદ્રને તેની કક્ષામાં રાખવા જરૂરી કેન્દ્રગામી બળ (Centripetal force) પૂરું પાડે છે।"
        },
        {
            "id": "KOBJ_CLASS9_SCI_CH9_THEORY_GRAVITATION_LAW",
            "type": "theory",
            "title": "Step 4: Reveal - Universal Law of Gravitation",
            "title_hi": "चरण 4: प्रकटीकरण - गुरुत्वाकर्षण का सार्वत्रिक नियम",
            "title_gu": "પગલું 4: પર્દાફાશ - ગુરુત્વાકર્ષણનો સાર્વત્રિક નિયમ",
            "body": "Every object in the universe attracts every other object with a force proportional to the product of their masses and inversely proportional to the square of the distance between them.\n$$F = G \\frac{M \\cdot m}{d^2}$$\nWhere $G = 6.673 \\times 10^{-11} \\text{ N m}^2/\\text{kg}^2$ (Universal Gravitational Constant).",
            "body_hi": "ब्रमांड का प्रत्येक पिंड प्रत्येक अन्य पिंड को एक बल से आकर्षित करता है जो उनके द्रव्यमान के गुणनफल के समानुपाती और उनके बीच की दूरी के वर्ग के व्युत्क्रमानुपाती होता है।\n$$F = G \\frac{M \\cdot m}{d^2}$$\nजहाँ $G = 6.673 \\times 10^{-11} \\text{ N m}^2/\\text{kg}^2$ (सार्वत्रिक गुरुत्वाकर्षण नियतांक)।",
            "body_gu": "વિશ્વનો દરેક પદાર્થ બીજા દરેક પદાર્થ પર આકર્ષણ બળ લગાડે છે, જે બંને પદાર્થોના દ્રવ્યમાનના ગુણાકારના સમપ્રમાણમાં અને તેમની વચ્ચેના અંતરના વર્ગના વ્યસ્ત પ્રમાણમાં હોય છે।\n$$F = G \\frac{M \\cdot m}{d^2}$$\nજ્યાં $G = 6.673 \\times 10^{-11} \\text{ N m}^2/\\text{kg}^2$ (સાર્વત્રિક ગુરુત્વાકર્ષણ અચળાંક) ।"
        },
        {
            "id": "KOBJ_CLASS9_SCI_CH9_THEORY_G_ACCELERATION",
            "type": "theory",
            "title": "Step 4: Reveal - Free Fall, Acceleration due to Gravity & Weight",
            "title_hi": "चरण 4: प्रकटीकरण - मुक्त पतन, गुरुत्वीय त्वरण और भार",
            "title_gu": "પગલું 4: પર્દાફાશ - મુક્ત પતન, ગુરુત્વપ્રવેગ અને વજન",
            "body": "1. **Free Fall**: Motion under influence of Earth's gravity alone.\n2. **Acceleration due to Gravity ($g$)**:\n$$g = \\frac{G M}{R^2} \\approx 9.8 \\text{ m/s}^2 \\text{ on Earth surface}$$\n3. **Mass vs Weight**:\n- **Mass ($m$)**: Quantity of matter. Constant everywhere. SI Unit: kg.\n- **Weight ($W$)**: Gravitational force pulling object towards Earth center ($W = m \\cdot g$). Changes with location. SI Unit: Newton (N).\nWeight on Moon = $\\frac{1}{6} \\times \\text{Weight on Earth}$.",
            "body_hi": "1. **मुक्त पतन**: केवल पृथ्वी के गुरुत्वाकर्षण के प्रभाव में गति।\n2. **गुरुत्वीय त्वरण ($g$)**:\n$$g = \\frac{G M}{R^2} \\approx 9.8 \\text{ m/s}^2 \\text{ (पृथ्वी की सतह पर)}$$\n3. **द्रव्यमान बनाम भार**:\n- **द्रव्यमान ($m$)**: पदार्थ की मात्रा। हर जगह स्थिर। SI इकाई: kg।\n- **भार ($W$)**: गुरुत्वाकर्षण बल ($W = m \\cdot g$)। स्थान के साथ बदलता है। SI इकाई: न्यूटन (N)।\nचंद्रमा पर भार = $\\frac{1}{6} \\times \\text{पृथ्वी पर भार}$।",
            "body_gu": "1. **મુક્ત પતન**: માત્ર પૃથ્વીના ગુરુત્વાકર્ષણ બળની અસર હેઠળ ગતિ।\n2. **ગુરુત્વપ્રવેગ ($g$)**:\n$$g = \\frac{G M}{R^2} \\approx 9.8 \\text{ m/s}^2 \\text{ (પૃથ્વીની સપાટી પર)}$$\n3. **દ્રવ્યમાન વિ વજન**:\n- **દ્રવ્યમાન ($m$)**: દ્રવ્યનો જથ્થો। બધે જ અચળ। SI એકમ: kg।\n- **વજન ($W$)**: ગુરુત્વાકર્ષણ બળ ($W = m \\cdot g$) । સ્થળ સાથે બદલાય છે। SI એકમ: ન્યૂટન (N) ।\nચંદ્ર પર વજન = $\\frac{1}{6} \\times \\text{પૃથ્વી પર વજન}$।"
        },
        {
            "id": "KOBJ_CLASS9_SCI_CH9_THEORY_ARCHIMEDES",
            "type": "theory",
            "title": "Step 4: Reveal - Thrust, Pressure & Archimedes' Principle",
            "title_hi": "चरण 4: प्रकटीकरण - प्रणोद, दाब और आर्किमिडीज का सिद्धांत",
            "title_gu": "પગલું 4: પર્દાફાશ - ધક્કો, દબાણ અને આર્કિમિડીઝનો સિદ્ધાંત",
            "body": "1. **Thrust & Pressure**: Pressure = $\\frac{\\text{Thrust}}{\\text{Area}}$. SI unit: Pascal (Pa) or $\\text{N/m}^2$.\n2. **Buoyancy**: Upward force exerted by a fluid on an immersed object.\n3. **Archimedes' Principle**: When a body is immersed fully or partially in a fluid, it experiences an upward buoyant force equal to the weight of the fluid displaced by it.",
            "body_hi": "1. **प्रणोद और दाब**: दाब = $\\frac{\\text{प्रणोद}}{\\text{क्षेत्रफल}}$। SI इकाई: पास्कल (Pa) या $\\text{N/m}^2$।\n2. **उत्प्लावकता (Buoyancy)**: तरल द्वारा डूबी हुई वस्तु पर ऊपर की ओर लगाया गया बल।\n3. **आर्किमिडीज का सिद्धांत**: जब किसी पिंड को किसी तरल में पूर्ण या आंशिक रूप से डुबोया जाता है, तो वह उसके द्वारा विस्थापित तरल के भार के बराबर ऊपर की ओर उत्प्लावन बल का अनुभव करता है।",
            "body_gu": "1. **ધક્કો અને દબાણ**: દબાણ = $\\frac{\\text{ધક્કો}}{\\text{ક્ષેત્રફળ}}$। SI એકમ: પાસ્કલ (Pa) અથવા $\\text{N/m}^2$।\n2. **ઉત્પ્લાવકતા (Buoyancy)**: પ્રવાહી દ્વારા ડૂબેટેલા પદાર્થ પર ઉપર તરફ લાગતું બળ।\n3. **આર્કિમિડીઝનો સિદ્ધાંત**: જ્યારે કોઈ પદાર્થને પ્રવાહીમાં અંશતઃ કે સંપૂર્ણપણે ડૂબાડવામાં આવે છે, ત્યારે તેના પર લાગતું ઉત્પ્લાવક બળ તેણે ખસેડેલા પ્રવાહીના વજન જેટલું હોય છે।"
        },
        {
            "id": "KOBJ_CLASS9_SCI_CH9_EX_1",
            "type": "quiz",
            "title": "Textbook Exercise 1: Mass and Weight on Moon",
            "title_hi": "पाठ्यपुस्तक अभ्यास 1: चंद्रमा पर द्रव्यमान और भार",
            "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 1: ચંદ્ર પર દ્રવ્યમાન અને વજન",
            "question": "An object has mass 10 kg on Earth. What is its mass and weight on the Moon? (g_earth = 9.8 m/s²)",
            "question_hi": "पृथ्वी पर एक वस्तु का द्रव्यमान 10 kg है। चंद्रमा पर इसका द्रव्यमान और भार क्या होगा? (g_earth = 9.8 m/s²)",
            "question_gu": "પૃથ્વી પર પદાર્થનું દ્રવ્યમાન 10 kg છે। ચંદ્ર પર તેનું દ્રવ્યમાન અને વજન કેટલું હશે? (g_earth = 9.8 m/s²)",
            "options": [
                "Mass = 10 kg, Weight = 16.3 N",
                "Mass = 1.67 kg, Weight = 98 N",
                "Mass = 10 kg, Weight = 98 N",
                "Mass = 60 kg, Weight = 16.3 N"
            ],
            "options_hi": [
                "द्रव्यमान = 10 kg, भार = 16.3 N",
                "द्रव्यमान = 1.67 kg, भार = 98 N",
                "द्रव्यमान = 10 kg, भार = 98 N",
                "द्रव्यमान = 60 kg, भार = 16.3 N"
            ],
            "options_gu": [
                "દ્રવ્યમાન = 10 kg, વજન = 16.3 N",
                "દ્રવ્યમાન = 1.67 kg, વજન = 98 N",
                "દ્રવ્યમાન = 10 kg, વજન = 98 N",
                "દ્રવ્યમાન = 60 kg, વજન = 16.3 N"
            ],
            "correct_index": 0,
            "explanation": "Mass remains constant (10 kg). Weight on Earth = 10 × 9.8 = 98 N. Weight on Moon = (1/6) × 98 = 16.33 N.",
            "explanation_hi": "द्रव्यमान स्थिर रहता है (10 kg)। पृथ्वी पर भार = 98 N। चंद्रमा पर भार = (1/6) × 98 = 16.33 N।",
            "explanation_gu": "દ્રવ્યમાન અચળ રહે છે (10 kg) । પૃથ્વી પર વજન = 98 N। ચંદ્ર પર વજન = (1/6) × 98 = 16.33 N।"
        },
        {
            "id": "KOBJ_CLASS9_SCI_CH9_EX_2",
            "type": "quiz",
            "title": "Textbook Exercise 2: Stone Thrown Vertically Upward",
            "title_hi": "पाठ्यपुस्तक अभ्यास 2: लंबवत ऊपर की ओर फेंका गया पत्थर",
            "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 2: લંબરૂપે ઉપર ફેંકેલો પથ્થર",
            "question": "A stone is thrown vertically upward with a velocity of 40 m/s. Taking g = 10 m/s², find the maximum height reached by the stone.",
            "question_hi": "एक पत्थर को 40 m/s के वेग से लंबवत ऊपर की ओर फेंका जाता है। g = 10 m/s² लेते हुए पत्थर द्वारा तय की गई अधिकतम ऊंचाई ज्ञात कीजिए।",
            "question_gu": "એક પથ્થરને 40 m/s ના વેગથી લંબરૂપે ઉપર ફેંકવામાં આવે છે। g = 10 m/s² લઈને પથ્થરે મેળવેલી મહત્તમ ઊંચાઈ શોધો।",
            "options": [
                "80 m",
                "160 m",
                "40 m",
                "100 m"
            ],
            "options_hi": [
                "80 मीटर",
                "160 मीटर",
                "40 मीटर",
                "100 मीटर"
            ],
            "options_gu": [
                "80 મીટર",
                "160 મીટર",
                "40 મીટર",
                "100 મીટર"
            ],
            "correct_index": 0,
            "explanation": "u = 40 m/s, v = 0 m/s, a = -g = -10 m/s². v² = u² + 2as => 0 = 1600 - 20*s => 20s = 1600 => s = 80 m.",
            "explanation_hi": "u = 40, v = 0, a = -10। v² = u² + 2as => 0 = 1600 - 20s => s = 80 मीटर।",
            "explanation_gu": "u = 40, v = 0, a = -10। v² = u² + 2as => 0 = 1600 - 20s => s = 80 મીટર।"
        },
        {
            "id": "KOBJ_CLASS9_SCI_CH9_REFLECTION",
            "type": "reflection",
            "title": "Step 6: Reflection - Gravitational Constant vs g",
            "title_hi": "चरण 6: विचार-विमर्श - गुरुत्वाकर्षण नियतांक बनाम g",
            "title_gu": "પગલું 6: મનન - ગુરુત્વાકર્ષણ અચળાંક વિ g",
            "body": "What is the key difference between G (Gravitational constant) and g (acceleration due to gravity)? G is universal constant everywhere, while g varies with height, depth, and heavenly body!",
            "body_hi": "G (गुरुत्वाकर्षण नियतांक) और g (गुरुत्वीय त्वरण) में क्या मुख्य अंतर है? G हर जगह सार्वत्रिक नियतांक है, जबकि g ऊंचाई, गहराई और खगोलीय पिंड के साथ बदलता है!",
            "body_gu": "G (ગુરુત્વાકર્ષણ અચળાંક) અને g (ગુરુત્વપ્રવેગ) વચ્ચે શું મુખ્ય તફાવત છે? G બધે સાર્વત્રિક અચળાંક છે, જ્યારે g ઊંચાઈ, ઊંડાઈ અને અવકાશી પદાર્થ સાથે બદલાય છે!"
        },
        {
            "id": "KOBJ_CLASS9_SCI_CH9_CONNECTION",
            "type": "connection",
            "title": "Step 7: Knowledge Graph Connection",
            "title_hi": "चरण 7: ज्ञान ग्राफ संबंध",
            "title_gu": "પગલું 7: જ્ઞાન ગ્રાફ જોડાણ",
            "body": "Prerequisite: Laws of Motion. Next Chapter: Work and Energy. Future Topics: Planetary Motion & Satellite Orbits.",
            "body_hi": "पूर्व-आवश्यकता: गति के नियम। अगला अध्याय: कार्य और ऊर्जा। भविष्य के विषय: ग्रहीय गति और उपग्रह कक्षाएं।",
            "body_gu": "પૂર્વ-જરૂરિયાત: ગતિના નિયમો। આગળનું પ્રકરણ: કાર્ય અને ઊર્જા। ભવિષ્યના વિષયો: ગ્રહોની ગતિ અને ઉપગ્રહ કક્ષાઓ।"
        },
        {
            "id": "KOBJ_CLASS9_SCI_CH9_MASTERY",
            "type": "mastery",
            "title": "Step 8: Mastery - Submarine & Ship Buoyancy",
            "title_hi": "चरण 8: महारत - पनडुब्बी और जहाज की उत्प्लावकता",
            "title_gu": "પગલું 8: માસ્ટરી - સબમરીન અને જહાજની ઉત્પ્લાવકતા",
            "body": "How does a heavy iron ship float while a small iron nail sinks? The hollow shape of the ship displaces a volume of water whose weight is far greater than the total weight of the ship!",
            "body_hi": "लोहे का भारी जहाज पानी पर क्यों तैरता है जबकि लोहे की छोटी कील डूब जाती है? जहाज का खोखला आकार पानी की इतनी मात्रा को विस्थापित करता है जिसका भार जहाज के कुल भार से अधिक होता है!",
            "body_gu": "લોખંડનું ભારે જહાજ પાણી પર કેમ તરે છે જ્યારે નાની ખીલી ડૂબી જાય છે? જહાજનો પોલો આકાર એટલા પાણીના જથ્થાને ખસેડે છે જેનું વજન જહાજના કુલ વજન કરતાં વધુ હોય છે!"
        }
    ]

def create_ch10_work_energy():
    return [
        {
            "id": "KOBJ_CLASS9_SCI_CH10_HOOK",
            "type": "real_world_example",
            "title": "Step 1: Hook - Pushing a Wall for 2 Hours = Zero Work?",
            "title_hi": "चरण 1: हुक - 2 घंटे तक दीवार को धक्का देना = शून्य कार्य?",
            "title_gu": "પગલું 1: હૂક - 2 કલાક સુધી દીવાલને ધક્કો મારવો = શૂન્ય કાર્ય?",
            "body": "If you push a solid brick wall for hours and get exhausted, scientific work done is ZERO! Why? Because in Physics, Work requires both Force AND Displacement in the direction of force!",
            "body_hi": "यदि आप घंटों तक ईंट की दीवार को धक्का देते हैं और थक जाते हैं, तो किया गया वैज्ञानिक कार्य शून्य है! क्यों? क्योंकि भौतिकी में कार्य के लिए बल और बल की दिशा में विस्थापन दोनों की आवश्यकता होती है!",
            "body_gu": "જો તમે કલાકો સુધી ઈંટની દીવાલને ધક્કો મારો અને થાકી જાઓ, તો વિજ્ઞાનની દ્રષ્ટિએ થયેલું કાર્ય શૂન્ય છે! શા માટે? કારણ કે ભૌતિકશાસ્ત્રમાં કાર્ય માટે બળ અને બળની દિશામાં સ્થાનાંતર બંને જરૂરી છે!"
        },
        {
            "id": "KOBJ_CLASS9_SCI_CH10_THEORY_WORK",
            "type": "theory",
            "title": "Step 4: Reveal - Scientific Concept of Work",
            "title_hi": "चरण 4: प्रकटीकरण - कार्य की वैज्ञानिक अवधारणा",
            "title_gu": "પગલું 4: પર્દાફાશ - કાર્યનો વૈજ્ઞાનિક ખ્યાલ",
            "body": "Work ($W$) done by a constant force ($F$) acting on an object causing displacement ($s$):\n$$W = F \\cdot s$$\nSI Unit: Joule (J) or $\\text{N m}$.\n1 Joule is the amount of work done when a force of 1 N displaces an object by 1 m in force direction.\n- **Positive Work**: Force and displacement in same direction.\n- **Negative Work**: Force and displacement in opposite directions (e.g., Friction).\n- **Zero Work**: Displacement is zero, or Force is perpendicular to displacement.",
            "body_hi": "वस्तु पर लगे अचर बल ($F$) द्वारा किया गया कार्य ($W$) जो विस्थापन ($s$) उत्पन्न करता है:\n$$W = F \\cdot s$$\nSI इकाई: जूल (J) या $\\text{N m}$।\n1 जूल कार्य की वह मात्रा है जब 1 N का बल किसी वस्तु को बल की दिशा में 1 m विस्थापित करता है।\n- **धनात्मक कार्य**: बल और विस्थापन एक ही दिशा में।\n- **ऋणात्मक कार्य**: बल और विस्थापन विपरीत दिशा में (जैसे घर्षण)।\n- **शून्य कार्य**: विस्थापन शून्य है, या बल विस्थापन के लंबवत है।",
            "body_gu": "પદાર્થ પર લાગતા અચળ બળ ($F$) દ્વારા થતું કાર્ય ($W$) જે સ્થાનાંતર ($s$) પ્રેરિત કરે છે:\n$$W = F \\cdot s$$\nSI એકમ: જૂલ (J) અથવા $\\text{N m}$।\n1 જૂલ એ એવું કાર્ય છે જ્યારે 1 N બળ પદાર્થને બળની દિશામાં 1 m ખસેડે છે।\n- **ધન કાર્ય**: બળ અને સ્થાનાંતર એક જ દિશામાં।\n- **ઋણ કાર્ય**: બળ અને સ્થાનાંતર વિરુદ્ધ દિશામાં (દા.ત. ઘર્ષણ) ।\n- **શૂન્ય કાર્ય**: સ્થાનાંતર શૂન્ય હોય અથવા બળ સ્થાનાંતરને લંબ હોય।"
        },
        {
            "id": "KOBJ_CLASS9_SCI_CH10_THEORY_ENERGY",
            "type": "theory",
            "title": "Step 4: Reveal - Kinetic Energy, Potential Energy & Power",
            "title_hi": "चरण 4: प्रकटीकरण - गतिज ऊर्जा, स्थितिज ऊर्जा और शक्ति",
            "title_gu": "પગલું 4: પર્દાફાશ - ગતિઊર્જા, સ્થિતિઊર્જા અને પાવર",
            "body": "1. **Kinetic Energy ($E_k$)**: Energy possessed due to motion.\n$$E_k = \\frac{1}{2} m v^2$$\n2. **Potential Energy ($E_p$)**: Energy possessed due to position or shape.\n$$E_p = m g h$$\n3. **Law of Conservation of Energy**: Energy can neither be created nor destroyed; it can only be transformed from one form to another. Total Mechanical Energy = $E_k + E_p = \\text{Constant}$.\n4. **Power ($P$)**: Rate of doing work or rate of energy consumption.\n$$P = \\frac{W}{t}$$\nSI Unit: Watt (W) or $\\text{J/s}$. Commercial unit: $1 \\text{ kWh} = 3.6 \\times 10^6 \\text{ Joules}$.",
            "body_hi": "1. **गतिज ऊर्जा ($E_k$)**: गति के कारण ऊर्जा।\n$$E_k = \\frac{1}{2} m v^2$$\n2. **स्थितिज ऊर्जा ($E_p$)**: स्थिति या आकार के कारण ऊर्जा।\n$$E_p = m g h$$\n3. **ऊर्जा संरक्षण का नियम**: ऊर्जा न तो उत्पन्न की जा सकती है और न ही नष्ट; इसे केवल एक रूप से दूसरे रूप में बदला जा सकता है।\n4. **शक्ति ($P$)**: कार्य करने की दर।\n$$P = \\frac{W}{t}$$\nSI इकाई: वाट (W)। व्यावसायिक इकाई: $1 \\text{ kWh} = 3.6 \\times 10^6 \\text{ जूल}$।",
            "body_gu": "1. **ગતિઊર્જા ($E_k$)**: ગતિના કારણે ધરાવતી ઊર્જા।\n$$E_k = \\frac{1}{2} m v^2$$\n2. **સ્થિતિઊર્જા ($E_p$)**: સ્થાન અથવા આકારના કારણે ધરાવતી ઊર્જા।\n$$E_p = m g h$$\n3. **ઊર્જા સંરક્ષણનો નિયમ**: ઊર્જા ઉત્પન્ન કરી શકાતી નથી કે નાશ પામતી નથી; માત્ર એક સ્વરૂપમાંથી બીજા સ્વરૂપમાં રૂપાંતરિત થાય છે।\n4. **પાવર ($P$)**: કાર્ય કરવાનો દર।\n$$P = \\frac{W}{t}$$\nSI એકમ: વોટ (W) । વ્યાપારી એકમ: $1 \\text{ kWh} = 3.6 \\times 10^6 \\text{ જૂલ}$।"
        },
        {
            "id": "KOBJ_CLASS9_SCI_CH10_EX_1",
            "type": "quiz",
            "title": "Textbook Exercise 1: Kinetic Energy Calculation",
            "title_hi": "पाठ्यपुस्तक अभ्यास 1: गतिज ऊर्जा की गणना",
            "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 1: ગતિઊર્જાની ગણતરી",
            "question": "What is the kinetic energy of an object of mass 15 kg moving with a velocity of 4 m/s?",
            "question_hi": "4 m/s के वेग से गतिमान 15 kg द्रव्यमान की वस्तु की गतिज ऊर्जा क्या है?",
            "question_gu": "4 m/s ના વેગથી ગતિ કરતા 15 kg દ્રવ્યમાનના પદાર્થની ગતિઊર્જા કેટલી હશે?",
            "options": [
                "120 J",
                "60 J",
                "240 J",
                "30 J"
            ],
            "options_hi": [
                "120 J",
                "60 J",
                "240 J",
                "30 J"
            ],
            "options_gu": [
                "120 J",
                "60 J",
                "240 J",
                "30 J"
            ],
            "correct_index": 0,
            "explanation": "m = 15 kg, v = 4 m/s. Ek = 0.5 × m × v² = 0.5 × 15 × 16 = 120 Joules.",
            "explanation_hi": "Ek = 0.5 × 15 × 16 = 120 जूल।",
            "explanation_gu": "Ek = 0.5 × 15 × 16 = 120 જૂલ।"
        },
        {
            "id": "KOBJ_CLASS9_SCI_CH10_EX_2",
            "type": "quiz",
            "title": "Textbook Exercise 2: Electricity Consumption in Units",
            "title_hi": "पाठ्यपुस्तक अभ्यास 2: इकाइयों में बिजली की खपत",
            "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 2: યુનિટમાં વીજળીનો વપરાશ",
            "question": "An electric bulb of 60 W is used for 6 hours per day. Calculate the 'units' of energy consumed in one day by the bulb.",
            "question_hi": "60 W का एक बिजली का बल्ब प्रतिदिन 6 घंटे उपयोग किया जाता है। बल्ब द्वारा एक दिन में खपत की गई ऊर्जा की 'इकाइयों' की गणना कीजिए।",
            "question_gu": "60 W નો એક ઇલેક્ટ્રિક બલ્બ પ્રતિદિન 6 કલાક વપરાય છે। બલ્બ દ્વારા એક દિવસમાં વપરાયેલી ઊર્જાના 'યુનિટ' ગણો।",
            "options": [
                "0.36 units",
                "3.6 units",
                "360 units",
                "0.06 units"
            ],
            "options_hi": [
                "0.36 यूनिट",
                "3.6 यूनिट",
                "360 यूनिट",
                "0.06 यूनिट"
            ],
            "options_gu": [
                "0.36 યુનિટ",
                "3.6 યુનિટ",
                "360 યુનિટ",
                "0.06 યુનિટ"
            ],
            "correct_index": 0,
            "explanation": "Power P = 60 W = 0.06 kW. Time t = 6 hours. Energy E = P × t = 0.06 × 6 = 0.36 kWh = 0.36 units.",
            "explanation_hi": "P = 0.06 kW, t = 6 h। E = 0.06 × 6 = 0.36 kWh (यूनिट)।",
            "explanation_gu": "P = 0.06 kW, t = 6 h। E = 0.06 × 6 = 0.36 kWh (યુનિટ) ।"
        },
        {
            "id": "KOBJ_CLASS9_SCI_CH10_REFLECTION",
            "type": "reflection",
            "title": "Step 6: Reflection - Simple Pendulum Energy",
            "title_hi": "चरण 6: विचार-विमर्श - सरल लोलक ऊर्जा",
            "title_gu": "પગલું 6: મનન - સાદા લોલકની ઊર્જા",
            "body": "As a pendulum bob swings back and forth, energy constantly converts between Kinetic Energy (at bottom position) and Potential Energy (at extreme height points).",
            "body_hi": "जैसे-जैसे एक लोलक आगे और पीछे दोलन करता है, ऊर्जा लगातार गतिज ऊर्जा (नीचे की स्थिति पर) और स्थितिज ऊर्जा (उच्चतम बिंदुओं पर) के बीच परिवर्तित होती है।",
            "body_gu": "જેમ સાદું લોલક હિંચકા ખાય છે, તેમ ઊર્જા સતત ગતિઊર્જા (નીચેની સ્થિતિમાં) અને સ્થિતિઊર્જા (ઉચ્ચતમ બિંદુઓએ) વચ્ચે રૂપાંતરિત થાય છે।"
        },
        {
            "id": "KOBJ_CLASS9_SCI_CH10_CONNECTION",
            "type": "connection",
            "title": "Step 7: Knowledge Graph Connection",
            "title_hi": "चरण 7: ज्ञान ग्राफ संबंध",
            "title_gu": "પગલું 7: જ્ઞાન ગ્રાફ જોડાણ",
            "body": "Prerequisite: Gravitation & Motion. Next Chapter: Sound (Wave energy propagation). Future Topics: Thermodynamics & Electricity.",
            "body_hi": "पूर्व-आवश्यकता: गुरुत्वाकर्षण और गति। अगला अध्याय: ध्वनि। भविष्य के विषय: ऊष्मागतिकी और विद्युत।",
            "body_gu": "પૂર્વ-જરૂરિયાત: ગુરુત્વાકર્ષણ અને ગતિ। આગળનું પ્રકરણ: ધ્વનિ। ભવિષ્યના વિષયો: થર્મોડાયનેમિક્સ અને વિદ્યુત।"
        },
        {
            "id": "KOBJ_CLASS9_SCI_CH10_MASTERY",
            "type": "mastery",
            "title": "Step 8: Mastery - Hydroelectric Power Plant",
            "title_hi": "चरण 8: महारत - जलविद्युत संयंत्र",
            "title_gu": "પગલું 8: માસ્ટરી - જળવિદ્યુત મથક",
            "body": "Trace energy transformation in a dam: Water stored at height (Potential Energy) -> Falling water (Kinetic Energy) -> Turbine rotation (Mechanical Energy) -> Generator output (Electrical Energy)!",
            "body_hi": "बांध में ऊर्जा के रूपांतरण का पता लगाएं: ऊंचाई पर संग्रहीत पानी (स्थितिज ऊर्जा) -> गिरता पानी (गतिज ऊर्जा) -> टरबाइन घूर्णन (यांत्रिक ऊर्जा) -> जनरेटर आउटपुट (विद्युत ऊर्जा)!",
            "body_gu": "ડેમમાં ઊર્જા રૂપાંતરણ શોધો: ઊંચાઈ પર સંગ્રહિત પાણી (સ્થિતિઊર્જા) -> પડતું પાણી (ગતિઊર્જા) -> ટર્બાઇન પરિભ્રમણ (યાંત્રિક ઊર્જા) -> જનરેટર આઉટપુટ (વિદ્યુત ઊર્જા)!"
        }
    ]

def create_ch11_sound():
    return [
        {
            "id": "KOBJ_CLASS9_SCI_CH11_HOOK",
            "type": "real_world_example",
            "title": "Step 1: Hook - Sound Cannot Travel in Space!",
            "title_hi": "चरण 1: हुक - अंतरिक्ष में ध्वनि यात्रा नहीं कर सकती!",
            "title_gu": "પગલું 1: હૂક - અવકાશમાં ધ્વનિ ગતિ કરી શકતો નથી!",
            "body": "In sci-fi movies, space explosions make loud noises. But in real space, absolute silence reigns! Why? Because Sound is a Mechanical Wave that REQUIRES a material medium (solid, liquid, or gas) to propagate!",
            "body_hi": "विज्ञान कथा फिल्मों में, अंतरिक्ष विस्फोट तेज़ आवाज़ करते हैं। लेकिन वास्तविक अंतरिक्ष में, पूर्ण सन्नाटा रहता है! क्यों? क्योंकि ध्वनि एक यांत्रिक तरंग है जिसे संचरण के लिए भौतिक माध्यम की आवश्यकता होती है!",
            "body_gu": "વિજ્ઞાન કથા ફિલ્મોમાં, અવકાશમાં થતા વિસ્ફોટો મોટા અવાજો કરે છે। પરંતુ વાસ્તવિક અવકાશમાં સંપૂર્ણ શાંતિ હોય છે! શા માટે? કારણ કે ધ્વનિ એ યાંત્રિક તરંગ છે જેને પ્રસરણ માટે ભૌતિક માધ્યમની જરૂર પડે છે!"
        },
        {
            "id": "KOBJ_CLASS9_SCI_CH11_THEORY_WAVE",
            "type": "theory",
            "title": "Step 4: Reveal - Sound Waves, Speed & Characteristics",
            "title_hi": "चरण 4: प्रकटीकरण - ध्वनि तरंगें, चाल और अभिलक्षण",
            "title_gu": "પગલું 4: પર્દાફાશ - ધ્વનિ તરંગો, ઝડપ અને લક્ષણો",
            "body": "1. **Longitudinal Wave**: Sound travels as series of Compressions (high pressure) and Rarefactions (low pressure).\n2. **Characteristics**:\n- **Wavelength ($\\lambda$)**: Distance between two consecutive compressions or rarefactions (SI: meter).\n- **Frequency ($\\nu$)**: Number of oscillations per second (SI: Hertz, Hz).\n- **Speed ($v$)**:\n$$v = \\lambda \\cdot \\nu$$\nSpeed of sound is maximum in solids, slower in liquids, slowest in gases (air $\\approx 344 \\text{ m/s}$ at $22^\\circ\\text{C}$).",
            "body_hi": "1. **अनुदैर्ध्य तरंग**: ध्वनि संपीड़न (उच्च दाब) और विरलन (निम्न दाब) की श्रृंखला के रूप में यात्रा करती है।\n2. **अभिलक्षण**:\n- **तरंगदैर्ध्य ($\\lambda$)**: दो क्रमागत संपीड़नों या विरलनों के बीच की दूरी (SI: मीटर)।\n- **आवृत्ति ($\\nu$)**: प्रति सेकंड दोलनों की संख्या (SI: हर्ट्ज़, Hz)।\n- **चाल ($v$)**:\n$$v = \\lambda \\cdot \\nu$$\nध्वनि की चाल ठोसों में अधिकतम, द्रवों में धीमी और गैसों में सबसे धीमी होती है (वायु में $\\approx 344 \\text{ m/s}$)।",
            "body_gu": "1. **સંગત તરંગ**: ધ્વનિ સઘનતા (ઉચ્ચ દબાણ) અને વિઘનતા (નિમ્ન દબાણ) ની શ્રેણી તરીકે પ્રસરણ પામે છે।\n2. **લક્ષણો**:\n- **તરંગલંબાઈ ($\\lambda$)**: બે ક્રમિક સઘનતાઓ કે વિઘનતાઓ વચ્ચેનું અંતર (SI: મીટર) ।\n- **આવૃત્તિ ($\\nu$)**: પ્રતિ સેકન્ડ આંદોલનોની સંખ્યા (SI: હર્ટ્ઝ, Hz) ।\n- **ઝડપ ($v$)**:\n$$v = \\lambda \\cdot \\nu$$\nધ્વનિની ઝડપ ઘન પદાર્થોમાં મહત્તમ, પ્રવાહીમાં ધીમી અને વાયુઓમાં સૌથી ધીમી હોય છે (હવામાં $\\approx 344 \\text{ m/s}$) ।"
        },
        {
            "id": "KOBJ_CLASS9_SCI_CH11_THEORY_ECHO",
            "type": "theory",
            "title": "Step 4: Reveal - Reflection, Echo & Ultrasound",
            "title_hi": "चरण 4: प्रकटीकरण - परावर्तन, प्रतिध्वनि और पराध्वनि",
            "title_gu": "પગલું 4: પર્દાફાશ - પરાવર્તન, પડઘો અને પરાધ્વનિ",
            "body": "1. **Echo**: Reflection of sound. Minimum distance to hear echo clearly = 17.2 m (time gap $\\ge 0.1 \\text{ s}$).\n2. **Reverberation**: Persistence of sound due to repeated reflections.\n3. **Hearing Range**: Human range = 20 Hz to 20,000 Hz (20 kHz).\n- Infrasound: $< 20 \\text{ Hz}$ (Rhinoceros, Whales).\n- Ultrasound: $> 20,000 \\text{ Hz}$ (Bats, Dolphins, SONAR, Medical Ultrasound ECG).",
            "body_hi": "1. **प्रतिध्वनि (Echo)**: ध्वनि का परावर्तन। स्पष्ट प्रतिध्वनि सुनने के लिए न्यूनतम दूरी = 17.2 मीटर (समय अंतराल $\\ge 0.1 \\text{ s}$)।\n2. **अनुरणन (Reverberation)**: बार-बार परावर्तन के कारण ध्वनि का बना रहना।\n3. **श्रव्यता की परास**: मानव परास = 20 Hz से 20,000 Hz।\n- अवश्रव्य (Infrasound): $< 20 \\text{ Hz}$\n- पराध्वनि (Ultrasound): $> 20,000 \\text{ Hz}$ (चमगादड़, सोनार, चिकित्सा अल्ट्रासोनोग्राफी)।",
            "body_gu": "1. **પડઘો (Echo)**: ધ્વનિનું પરાવર્તન। સ્પષ્ટ પડઘો સાંભળવા માટે ન્યૂનતમ અંતર = 17.2 મીટર (સમયગાળો $\\ge 0.1 \\text{ s}$) ।\n2. **અનુરણન (Reverberation)**: વારંવાર પરાવર્તનને કારણે ધ્વનિનું જળવાઈ રહેવું।\n3. **શ્રાવ્ય મર્યાદા**: માનવ મર્યાદા = 20 Hz થી 20,000 Hz।\n- અશ્રાવ્ય (Infrasound): $< 20 \\text{ Hz}$\n- પરાધ્વનિ (Ultrasound): $> 20,000 \\text{ Hz}$ (ચામાચીડિયું, સોનાર, અલ્ટ્રાસાઉન્ડ) ।"
        },
        {
            "id": "KOBJ_CLASS9_SCI_CH11_EX_1",
            "type": "quiz",
            "title": "Textbook Exercise 1: Wavelength Calculation",
            "title_hi": "पाठ्यपुस्तक अभ्यास 1: तरंगदैर्ध्य की गणना",
            "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 1: તરંગલંબાઈની ગણતરી",
            "question": "A sound wave has a frequency of 2 kHz and wavelength 35 cm. How long will it take to travel 1.5 km?",
            "question_hi": "एक ध्वनि तरंग की आवृत्ति 2 kHz और तरंगदैर्ध्य 35 सेमी है। इसे 1.5 किमी की यात्रा करने में कितना समय लगेगा?",
            "question_gu": "એક ધ્વનિ તરંગની આવૃત્તિ 2 kHz અને તરંગલંબાઈ 35 cm છે। 1.5 km નું અંતર કાપવા તેને કેટલો સમય લાગશે?",
            "options": [
                "2.1 s",
                "4.2 s",
                "1.5 s",
                "0.7 s"
            ],
            "options_hi": [
                "2.1 सेकंड",
                "4.2 सेकंड",
                "1.5 सेकंड",
                "0.7 सेकंड"
            ],
            "options_gu": [
                "2.1 સેકન્ડ",
                "4.2 સેકન્ડ",
                "1.5 સેકન્ડ",
                "0.7 સેકન્ડ"
            ],
            "correct_index": 0,
            "explanation": "Frequency ν = 2000 Hz, Wavelength λ = 0.35 m. Speed v = λ × ν = 0.35 × 2000 = 700 m/s. Distance s = 1500 m. Time t = s / v = 1500 / 700 = 2.14 s.",
            "explanation_hi": "v = 0.35 × 2000 = 700 m/s। समय t = 1500 / 700 = 2.14 सेकंड।",
            "explanation_gu": "v = 0.35 × 2000 = 700 m/s। સમય t = 1500 / 700 = 2.14 સેકન્ડ।"
        },
        {
            "id": "KOBJ_CLASS9_SCI_CH11_EX_2",
            "type": "quiz",
            "title": "Textbook Exercise 2: SONAR Depth Calculation",
            "title_hi": "पाठ्यपुस्तक अभ्यास 2: सोनार गहराई की गणना",
            "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 2: સોનાર ઊંડાઈની ગણતરી",
            "question": "A SONAR device on a submarine sends out a signal and receives an echo 3.42 s later. If the speed of sound in seawater is 1531 m/s, what is the distance of the seabed?",
            "question_hi": "एक पनडुब्बी पर लगा सोनार उपकरण संकेत भेजता है और 3.42 सेकंड बाद प्रतिध्वनि प्राप्त करता है। यदि समुद्री जल में ध्वनि की चाल 1531 m/s है, तो समुद्र तल की दूरी क्या है?",
            "question_gu": "સબમરીન પરનું સોનાર સાધન સિગ્નલ મોકલે છે અને 3.42 સેકન્ડ પછી પડઘો મેળવે છે। જો દરિયાઈ પાણીમાં ધ્વનિની ઝડપ 1531 m/s હોય, તો સમુદ્રના તળિયાનું અંતર કેટલું છે?",
            "options": [
                "2618 m",
                "5236 m",
                "1531 m",
                "3000 m"
            ],
            "options_hi": [
                "2618 मीटर",
                "5236 मीटर",
                "1531 मीटर",
                "3000 मीटर"
            ],
            "options_gu": [
                "2618 મીટર",
                "5236 મીટર",
                "1531 મીટર",
                "3000 મીટર"
            ],
            "correct_index": 0,
            "explanation": "Total time t = 3.42 s. Time to reach seabed t' = 3.42 / 2 = 1.71 s. Distance d = v × t' = 1531 × 1.71 = 2618 m.",
            "explanation_hi": "समय t' = 1.71 सेकंड। दूरी d = 1531 × 1.71 = 2618 मीटर।",
            "explanation_gu": "સમય t' = 1.71 સેકન્ડ। અંતર d = 1531 × 1.71 = 2618 મીટર।"
        },
        {
            "id": "KOBJ_CLASS9_SCI_CH11_REFLECTION",
            "type": "reflection",
            "title": "Step 6: Reflection - Flash of Lightning vs Thunderclap",
            "title_hi": "चरण 6: विचार-विमर्श - बिजली की चमक बनाम गर्जन",
            "title_gu": "પગલું 6: મનન - વીજળીનો ચમકારો વિ ગર્જના",
            "body": "Why do we see lightning first and hear thunder a few seconds later, even though both happen simultaneously? Light travels at 300,000,000 m/s while sound travels at only 344 m/s in air!",
            "body_hi": "हम पहले बिजली की चमक क्यों देखते हैं और कुछ सेकंड बाद गर्जन क्यों सुनते हैं? प्रकाश 3,00,000,000 m/s की गति से चलता है जबकि ध्वनि हवा में केवल 344 m/s की गति से चलती है!",
            "body_gu": "આપણે પહેલાં વીજળીનો ચમકારો કેમ જોઈએ છીએ અને થોડી સેકન્ડ પછી ગર્જના કેમ સાંભળીએ છીએ? પ્રકાશ 3,00,000,000 m/s ની ઝડપે ગતિ કરે છે જ્યારે ધ્વનિ હવામાં માત્ર 344 m/s ની ઝડપે ગતિ કરે છે!"
        },
        {
            "id": "KOBJ_CLASS9_SCI_CH11_CONNECTION",
            "type": "connection",
            "title": "Step 7: Knowledge Graph Connection",
            "title_hi": "चरण 7: ज्ञान ग्राफ संबंध",
            "title_gu": "પગલું 7: જ્ઞાન ગ્રાફ જોડાણ",
            "body": "Prerequisite: Work and Energy. Future Topics: Light (Electromagnetic waves), Human Eye, Wave Optics.",
            "body_hi": "पूर्व-आवश्यकता: कार्य और ऊर्जा। भविष्य के विषय: प्रकाश (विद्युत चुंबकीय तरंगें), मानव नेत्र, तरंग प्रकाशिकी।",
            "body_gu": "પૂર્વ-જરૂરિયાત: કાર્ય અને ઊર્જા। ભવિષ્યના વિષયો: પ્રકાશ (વિદ્યુતચુંબકીય તરંગો), માનવ આંખ, તરંગ પ્રકાશશાસ્ત્ર।"
        },
        {
            "id": "KOBJ_CLASS9_SCI_CH11_MASTERY",
            "type": "mastery",
            "title": "Step 8: Mastery - Echolocation in Bats",
            "title_hi": "चरण 8: महारत - चमगादड़ में इकोलोकेशन",
            "title_gu": "પગલું 8: માસ્ટરી - ચામાચીડિયામાં ઇકોલોકેશન",
            "body": "Bats emit ultrasonic squeaks that bounce off prey and obstacles. By sensing the return time and intensity of echo, bats navigate and hunt in total darkness!",
            "body_hi": "चमगादड़ पराश्रव्य चीखें उत्सर्जित करते हैं जो शिकार और बाधाओं से टकराकर वापस आती हैं। प्रतिध्वनि के लौटने के समय और तीव्रता को महसूस करके, चमगादड़ पूर्ण अंधेरे में नेविगेट और शिकार करते हैं!",
            "body_gu": "ચામાચીડિયા પરાધ્વનિક અવાજો બહાર કાઢે છે જે શિકાર અને અવરોધો પરથી પરાવર્તિત થાય છે। પડઘાના પાછા ફરવાના સમય અને તીવ્રતાને અનુભવીને, ચામાચીડિયા સંપૂર્ણ અંધારામાં શિકાર કરે છે!"
        }
    ]

def create_ch12_food():
    return [
        {
            "id": "KOBJ_CLASS9_SCI_CH12_HOOK",
            "type": "real_world_example",
            "title": "Step 1: Hook - Feeding 1.4 Billion People",
            "title_hi": "चरण 1: हुक - 1.4 अरब लोगों का पेट भरना",
            "title_gu": "પગલું 1: હૂક - 1.4 અબજ લોકોને અનાજ પૂરું પાડવું",
            "body": "India's land area is limited, but population is growing! How did India increase food grain production 4 times from 1960 to 2004 with only a 25% increase in cultivated land? Through scientific revolutions: Green Revolution (crops) & White Revolution (milk)!",
            "body_hi": "भारत का भूमि क्षेत्र सीमित है, लेकिन जनसंख्या बढ़ रही है! भारत ने कृषि योग्य भूमि में केवल 25% की वृद्धि के साथ 1960 से 2004 तक खाद्यान्न उत्पादन 4 गुना कैसे बढ़ाया? हरित क्रांति (फसलें) और श्वेत क्रांति (दूध) के माध्यम से!",
            "body_gu": "ભારતનો જમીન વિસ્તાર મર્યાદિત છે, પરંતુ વસ્તી વધી રહી છે! ભારતે 1960 થી 2004 સુધી ખેતીલાયક જમીનમાં માત્ર 25% નો વધારો કરીને ખાદ્યાન્ન ઉત્પાદન 4 ગણું કેવી રીતે વધાર્યું? હરિયાળી ક્રાંતિ (પાક) અને શ્વેત ક્રાંતિ (દૂધ) દ્વારા!"
        },
        {
            "id": "KOBJ_CLASS9_SCI_CH12_THEORY_CROPS",
            "type": "theory",
            "title": "Step 4: Reveal - Crop Variety & Nutrient Management",
            "title_hi": "चरण 4: प्रकटीकरण - फसल किस्म और पोषक तत्व प्रबंधन",
            "title_gu": "પગલું 4: પર્દાફાશ - પાક જાત અને પોષક તત્વ સંચાલન",
            "body": "1. **Crop Seasons**: Kharif (June-Oct, Paddy/Soybean) vs Rabi (Nov-April, Wheat/Gram).\n2. **Nutrient Management**: 16 essential nutrients required by plants.\n- **Macro-nutrients (6)**: Nitrogen, Phosphorus, Potassium, Calcium, Magnesium, Sulfur.\n- **Micro-nutrients (7)**: Iron, Manganese, Boron, Zinc, Copper, Molybdenum, Chlorine.\n3. **Manure vs Fertilizers**: Manure provides organic humus and improves soil structure. Fertilizers supply specific chemical NPK rapidly but overuse degrades soil quality.",
            "body_hi": "1. **फसल फसल ऋतुएँ**: खरीफ (जून-अक्टूबर, धान/सोयाबीन) बनाम रबी (नवंबर-अप्रैल, गेहूं/चना)।\n2. **पोषक तत्व प्रबंधन**: पौधों के लिए 16 आवश्यक पोषक तत्व।\n- **बृहत-पोषक (6)**: नाइट्रोजन, फास्फोरस, पोटेशियम, कैल्शियम, मैग्नीशियम, सल्फर।\n- **सूक्ष्म-पोषक (7)**: लोहा, मैंगनीज, बोरोन, जस्ता, तांबा, मोलिब्डेनम, क्लोरीन।\n3. **खाद बनाम उर्वरक**: खाद जैविक ह्यूमस प्रदान करती है। उर्वरक तेजी से विशिष्ट रासायनिक NPK की आपूर्ति करते हैं।",
            "body_gu": "1. **પાક ઋતુઓ**: ખરીફ (જૂન-ઓક્ટોબર, ડાંગર/સોયાબીન) વિ રવિ (નવેમ્બર-એપ્રિલ, ઘઉં/ચણા) ।\n2. **પોષક તત્વ સંચાલન**: વનસ્પતિ માટે 16 આવશ્યક પોષક તત્વો।\n- **મુખ્ય પોષક તત્વો (6)**: નાઇટ્રોજન, ફોસ્ફરસ, પોટેશિયમ, કેલ્શિયમ, મેગ્નેશિયમ, સલ્ફર।\n- **ગૌણ/સૂક્ષ્મ પોષક તત્વો (7)**: આયર્ન, મેંગેનીઝ, બોરોન, ઝિંક, કોપર, મોલિબ્ડેનમ, ક્લોરીન।\n3. **સેન્દ્રિય ખાતર વિ રાસાયણિક ખાતર**: સેન્દ્રિય ખાતર સેન્દ્રિય પદાર્થો પૂરા પાડે છે। રાસાયણિક ખાતરો ઝડપથી NPK પૂરા પાડે છે।"
        },
        {
            "id": "KOBJ_CLASS9_SCI_CH12_THEORY_ANIMAL",
            "type": "theory",
            "title": "Step 4: Reveal - Animal Husbandry & Poultry",
            "title_hi": "चरण 4: प्रकटीकरण - पशुपालन और कुक्कुट पालन",
            "title_gu": "પગલું 4: પર્દાફાશ - પશુપાલન અને મરઘા પાલન",
            "body": "1. **Cattle Farming**: Milch animals (milk-producing) vs Draught animals (agricultural labor). Cross-breeding Exotic (Jersey, Brown Swiss) with Local breeds (Red Sindhi, Sahiwal).\n2. **Poultry Farming**: Layers (egg production) vs Broilers (meat production).\n3. **Fish Production**: Capture fishing vs Mariculture (marine) & Aquaculture (freshwater).\n4. **Apiculture**: Bee-keeping for honey and wax. Italian bee (*Apis mellifera*) is commonly used due to high honey collection capacity.",
            "body_hi": "1. **पशुपालन**: दुधारू पशु (दूध देने वाले) बनाम भारवाही पशु (कृषि कार्य)। विदेशी किस्मों (जर्सी, ब्राउन स्विस) का स्थानीय किस्मों (रेड सिंधी, साहीवाल) के साथ संकरण।\n2. **कुक्कुट पालन (Poultry)**: लेयर (अंडा उत्पादन) बनाम ब्रायलर (मांस उत्पादन)।\n3. **मत्स्य उत्पादन**: संग्रहण मत्स्यन बनाम समुद्री संवर्धन और जल संवर्धन।\n4. **मधुमक्खी पालन (Apiculture)**: शहद और मोम के लिए। इतालवी मधुमक्खी (*Apis mellifera*) का उपयोग उच्च शहद संग्रह क्षमता के कारण किया जाता है।",
            "body_gu": "1. **પશુપાલન**: દુધાળા પ્રાણીઓ (દૂધ આપતાં) વિ ખેતકામ માટેના પ્રાણીઓ। વિદેશી જાતો (જર્સી, બ્રાઉન સ્વિસ) નું સ્થાનિક જાતો (રેડ સિંધી, સાહીવાલ) સાથે સંકરણ।\n2. **મરઘા પાલન (Poultry)**: લેયર (ઈંડા ઉત્પાદન) વિ બ્રોઇલર (માસ ઉત્પાદન) ।\n3. **મત્સ્ય ઉત્પાદન**: મત્સ્ય ગ્રહણ વિ મરીકલ્ચર (દરિયાઈ) અને એક્વાકલ્ચર (મીઠા પાણીનું) ।\n4. **મધમાખી પાલન (Apiculture)**: મધ અને મીણ માટે। ઇટાલિયન મધમાખી (*Apis mellifera*) નો ઉપયોગ વધુ મધ ઉત્પાદન માટે થાય છે।"
        },
        {
            "id": "KOBJ_CLASS9_SCI_CH12_EX_1",
            "type": "quiz",
            "title": "Textbook Exercise 1: Macro-nutrients for Plants",
            "title_hi": "पाठ्यपुस्तक अभ्यास 1: पौधों के लिए बृहत-पोषक तत्व",
            "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 1: વનસ્પતિ માટે મુખ્ય પોષક તત્વો",
            "question": "Which of the following is a macro-nutrient required by plants?",
            "question_hi": "निम्नलिखित में से कौन सा पौधों द्वारा आवश्यक बृहत-पोषक तत्व है?",
            "question_gu": "નીચેનામાંથી કયું વનસ્પતિ માટે મુખ્ય પોષક તત્વ છે?",
            "options": [
                "Nitrogen",
                "Iron",
                "Zinc",
                "Copper"
            ],
            "options_hi": [
                "नाइट्रोजन",
                "लोहा",
                "जस्ता",
                "तांबा"
            ],
            "options_gu": [
                "નાઇટ્રોજન",
                "આયર્ન",
                "ઝિંક",
                "કોપર"
            ],
            "correct_index": 0,
            "explanation": "Nitrogen is required in large quantities and is one of the 6 macro-nutrients (NPK, Ca, Mg, S). Iron, Zinc, and Copper are micro-nutrients.",
            "explanation_hi": "नाइट्रोजन बड़ी मात्रा में आवश्यक है और 6 बृहत-पोषक तत्वों में से एक है।",
            "explanation_gu": "નાઇટ્રોજન વધુ માત્રામાં જરૂરી છે અને તે 6 મુખ્ય પોષક તત્વોમાંનું એક છે।"
        },
        {
            "id": "KOBJ_CLASS9_SCI_CH12_EX_2",
            "type": "quiz",
            "title": "Textbook Exercise 2: Italian Bee Species",
            "title_hi": "पाठ्यपुस्तक अभ्यास 2: इतालवी मधुमक्खी प्रजाति",
            "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 2: ઇટાલિયન મધમાખી જાતિ",
            "question": "Which Italian bee variety is commonly used for commercial honey production?",
            "question_hi": "व्यावसायिक शहद उत्पादन के लिए आमतौर पर किस इतालवी मधुमक्खी किस्म का उपयोग किया जाता है?",
            "question_gu": "વ્યાપારી મધ ઉત્પાદન માટે સામાન્ય રીતે કઈ ઇટાલિયન મધમાખી જાતનો ઉપયોગ થાય છે?",
            "options": [
                "Apis mellifera",
                "Apis dorsata",
                "Apis cerana indica",
                "Apis florae"
            ],
            "options_hi": [
                "एपिस मेलिफेरा (Apis mellifera)",
                "एपिस डोर्साटा (Apis dorsata)",
                "एपिस सेराना इंडिका (Apis cerana indica)",
                "एपिस फ्लोरी (Apis florae)"
            ],
            "options_gu": [
                "એપિસ મેલિફેરા (Apis mellifera)",
                "એપિસ ડોર્સાટા (Apis dorsata)",
                "એપિસ સેરાના ઇન્ડિકા (Apis cerana indica)",
                "એપિસ ફ્લોરી (Apis florae)"
            ],
            "correct_index": 0,
            "explanation": "Apis mellifera is the Italian bee species favored for commercial honey production due to high honey yield and gentle nature.",
            "explanation_hi": "एपिस मेलिफेरा इतालवी मधुमक्खी प्रजाति है जो उच्च शहद उपज के कारण पसंद की जाती है।",
            "explanation_gu": "એપિસ મેલિફેરા એ ઇટાલિયન મધમાખી જાત છે જે વધુ મધ ઉત્પાદન માટે જાણીતી છે।"
        },
        {
            "id": "KOBJ_CLASS9_SCI_CH12_REFLECTION",
            "type": "reflection",
            "title": "Step 6: Reflection - Organic Farming vs Chemical Fertilizers",
            "title_hi": "चरण 6: विचार-विमर्श - जैविक खेती बनाम रासायनिक उर्वरक",
            "title_gu": "પગલું 6: મનન - જૈવિક ખેતી વિ રાસાયણિક ખાતરો",
            "body": "Why is organic farming gaining global popularity? Organic farming uses bio-fertilizers, neem leaves for bio-pesticides, and crop rotation to preserve long-term soil fertility without chemical pollution.",
            "body_hi": "जैविक खेती वैश्विक लोकप्रियता क्यों हासिल कर रही है? जैविक खेती रासायनिक प्रदूषण के बिना मिट्टी की दीर्घकालिक उर्वरता को बनाए रखने के लिए जैव-उर्वरक, नीम की पत्तियों के जैव-कीटनाशक और फसल चक्र का उपयोग करती है।",
            "body_gu": "જૈવિક ખેતી શા માટે વૈશ્વિક લોકપ્રિયતા મેળવી રહી છે? જૈવિક ખેતી રાસાયણિક પ્રદૂષણ વિના લાંબા ગાળાની જમીનની ફળદ્રુપતા જાળવવા જૈવિક ખાતરો અને લીમડાના જૈવ-કિટકનાશકોનો ઉપયોગ કરે છે."
        },
        {
            "id": "KOBJ_CLASS9_SCI_CH12_CONNECTION",
            "type": "connection",
            "title": "Step 7: Knowledge Graph Connection",
            "title_hi": "चरण 7: ज्ञान ग्राफ संबंध",
            "title_gu": "પગલું 7: જ્ઞાન ગ્રાફ જોડાણ",
            "body": "Prerequisite: Fundamental Unit of Life & Tissues. Future Topics: Ecology, Environmental Science, Sustainable Agriculture.",
            "body_hi": "पूर्व-आवश्यकता: जीवन की मौलिक इकाई और ऊतक। भविष्य के विषय: पारिस्थितिकी, पर्यावरण विज्ञान, सतत कृषि।",
            "body_gu": "પૂર્વ-જરૂરિયાત: જીવનનો મૂળભૂત એકમ અને પેશીઓ। ભવિષ્યના વિષયો: પિરાવરણ વિજ્ઞાન અને સતત કૃષિ।"
        },
        {
            "id": "KOBJ_CLASS9_SCI_CH12_MASTERY",
            "type": "mastery",
            "title": "Step 8: Mastery - Composite Fish Culture System",
            "title_hi": "चरण 8: महारत - मिश्रित मछली संवर्धन प्रणाली",
            "title_gu": "પગલું 8: માસ્ટરી - મિશ્ર મત્સ્ય સંવર્ધન પદ્ધતિ",
            "body": "Explain how composite fish culture uses 5-6 different fish species in a single pond without food competition: Catlas (surface feeders), Rohus (column feeders), Mrigals & Common Carps (bottom feeders)!",
            "body_hi": "बताएं कि कैसे मिश्रित मछली संवर्धन भोजन की प्रतिस्पर्धा के बिना एक ही तालाब में 5-6 अलग-अलग मछली प्रजातियों का उपयोग करता है: कटला (सतह से भोजन), रोहू (मध्य क्षेत्र), म्रिगल और कॉमन कार्प (तलहटी से)!",
            "body_gu": "સમજાવો કે મિશ્ર મત્સ્ય સંવર્ધન ખોરાકની હરીફાઈ વિના એક જ તળાવમાં 5-6 જુદી જુદી જાતોનો ઉપયોગ કેવી રીતે કરે છે: કતલા (સપાટી પરથી), રોહૂ (મધ્ય ભાગમાંથી), મૃગલ (તળિયામાંથી)!"
        }
    ]

def build_all():
    generators = {
        8: create_ch8_force,
        9: create_ch9_gravitation,
        10: create_ch10_work_energy,
        11: create_ch11_sound,
        12: create_ch12_food
    }

    for ch_num, gen_fn in generators.items():
        blocks = gen_fn()
        mod_dir = f"app_core/learning_modules/gseb_class9_science_ch{ch_num}"
        os.makedirs(mod_dir, exist_ok=True)
        blocks_file = os.path.join(mod_dir, "blocks.json")
        with open(blocks_file, "w", encoding="utf-8") as f:
            json.dump(blocks, f, ensure_ascii=False, indent=2)

        # Sync to NCERT chapter
        ch_file = f"app_core/chapters/ncert_class9_science_ch{ch_num}.json"
        os.makedirs("app_core/chapters", exist_ok=True)
        with open(ch_file, "w", encoding="utf-8") as f:
            json.dump(blocks, f, ensure_ascii=False, indent=2)

        # Assessment bank
        quizzes = [b for b in blocks if b["type"] == "quiz"]
        assessment_questions = []
        for q in quizzes:
            assessment_questions.append({
                "id": q["id"],
                "question": q["question"],
                "question_hi": q.get("question_hi", ""),
                "question_gu": q.get("question_gu", ""),
                "options": q["options"],
                "options_hi": q.get("options_hi", []),
                "options_gu": q.get("options_gu", []),
                "correct_index": q["correct_index"],
                "explanation": q.get("explanation", ""),
                "explanation_hi": q.get("explanation_hi", ""),
                "explanation_gu": q.get("explanation_gu", "")
            })

        assess_file = f"app_core/assessment/gseb_class9_science_ch{ch_num}_questions.json"
        os.makedirs("app_core/assessment", exist_ok=True)
        with open(assess_file, "w", encoding="utf-8") as f:
            json.dump(assessment_questions, f, ensure_ascii=False, indent=2)

        print(f"Science Ch {ch_num}: {len(blocks)} blocks, {len(quizzes)} quizzes synced to module, chapter JSON & assessment bank.")

if __name__ == "__main__":
    build_all()
