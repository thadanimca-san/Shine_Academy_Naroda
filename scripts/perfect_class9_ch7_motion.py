import json
import os

def generate_ch7_motion():
    blocks = [
        # --- STEP 1: HOOK ---
        {
            "id": "KOBJ_CLASS9_SCI_CH7_HOOK",
            "type": "real_world_example",
            "title": "Step 1: Hook - Are You Moving Right Now?",
            "title_hi": "चरण 1: हुक - क्या आप अभी गति कर रहे हैं?",
            "title_gu": "પગલું 1: હૂક - શું તમે અત્યારે ગતિ કરી રહ્યા છો?",
            "body": "Imagine sitting quietly on a chair reading this screen. You feel completely still. But relative to the Sun, you and the Earth are zooming through space at 107,000 km/h! Motion is not absolute; it depends on your frame of reference.",
            "body_hi": "कल्पना कीजिए कि आप एक कुर्सी पर बैठकर यह स्क्रीन पढ़ रहे हैं। आप पूरी तरह से स्थिर महसूस करते हैं। लेकिन सूर्य के सापेक्ष, आप और पृथ्वी 107,000 किमी/घंटा की गति से अंतरिक्ष में घूम रहे हैं! गति निरपेक्ष नहीं है; यह आपके संदर्भ फ्रेम पर निर्भर करती है।",
            "body_gu": "કલ્પના કરો કે તમે ખુરશી પર બેસીને આ સ્ક્રીન વાંચી રહ્યા છો। તમે સંપૂર્ણપણે સ્થિર અનુભવો છો। પરંતુ સૂર્યની સાપેક્ષમાં, તમે અને પૃથ્વી 107,000 કિમી/કલાકની ઝડપે અવકાશમાં ગતિ કરી રહ્યા છો! ગતિ નિરપેક્ષ નથી; તે તમારા સંદર્ભ ફ્રેમ પર આધાર રાખે છે।",
            "visual_prompt": "An animation showing a person sitting inside a moving train - from inside the train they are stationary, but to a person standing outside on the platform, they are moving rapidly."
        },

        # --- STEP 2: SOCRATIC THINKING ---
        {
            "id": "KOBJ_CLASS9_SCI_CH7_SOCRATIC_1",
            "type": "quiz",
            "title": "Step 2: Socratic Thinking - Distance vs Displacement",
            "title_hi": "चरण 2: सुकराती सोच - दूरी बनाम विस्थापन",
            "title_gu": "પગલું 2: સોક્રેટિક વિચારણા - અંતર વિસ્થાપન",
            "question": "An athlete runs around a 400-meter circular track and returns to the exact starting point. What is the distance covered and what is the displacement?",
            "question_hi": "एक एथलीट 400 मीटर के वृत्ताकार ट्रैक पर दौड़ता है और ठीक शुरुआती बिंदु पर लौट आता है। तय की गई दूरी कितनी है और विस्थापन कितना है?",
            "question_gu": "એક એથ્લેટ 400 મીટરના વર્તુળાકાર ટ્રેક પર દોડે છે અને મૂળ શરૂઆતના બિંદુએ પાછો આવે છે। કાપેલું અંતર કેટલું છે અને સ્થાનાંતર કેટલું છે?",
            "options": [
                "Distance = 400 m, Displacement = 400 m",
                "Distance = 400 m, Displacement = 0 m",
                "Distance = 0 m, Displacement = 400 m",
                "Distance = 0 m, Displacement = 0 m"
            ],
            "options_hi": [
                "दूरी = 400 मीटर, विस्थापन = 400 मीटर",
                "दूरी = 400 मीटर, विस्थापन = 0 मीटर",
                "दूरी = 0 मीटर, विस्थापन = 400 मीटर",
                "दूरी = 0 मीटर, विस्थापन = 0 मीटर"
            ],
            "options_gu": [
                "અંતર = 400 મીટર, સ્થાનાંતર = 400 મીટર",
                "અંતર = 400 મીટર, સ્થાનાંતર = 0 મીટર",
                "અંતર = 0 મીટર, સ્થાનાંતર = 400 મીટર",
                "અંતર = 0 મીટર, સ્થાનાંતર = 0 મીટર"
            ],
            "correct_index": 1,
            "explanation": "Distance is the total path length traveled (400 m). Displacement is the shortest straight-line distance between initial and final position. Since initial and final points are the same, displacement is 0 m.",
            "explanation_hi": "दूरी तय किए गए कुल पथ की लंबाई (400 मीटर) है। विस्थापन प्रारंभिक और अंतिम स्थिति के बीच की सबसे छोटी सीधी रेखा की दूरी है। चूंकि शुरुआती और अंतिम बिंदु समान हैं, विस्थापन 0 मीटर है।",
            "explanation_gu": "અંતર એ કાપેલા કુલ માર્ગની લંબાઈ (400 મીટર) છે। સ્થાનાંતર એ પ્રારંભિક અને અંતિમ સ્થાન વચ્ચેનું સૌથી ટૂંકું સીધું અંતર છે। પ્રારંભિક અને અંતિમ બિંદુઓ સમાન હોવાથી, સ્થાનાંતર 0 મીટર છે।"
        },

        # --- STEP 3: DISCOVERY - DISTANCE AND DISPLACEMENT ---
        {
            "id": "KOBJ_CLASS9_SCI_CH7_DISCOVERY_1",
            "type": "theory",
            "title": "Step 3 & 4: Discovery & Reveal - Distance vs Displacement",
            "title_hi": "चरण 3 और 4: खोज और प्रकटीकरण - दूरी और विस्थापन",
            "title_gu": "પગલું 3 અને 4: શોધ અને પર્દાફાશ - અંતર અને સ્થાનાંતર",
            "body": "1. **Distance**: The actual total length of the path covered by a moving body in any direction. It is a **Scalar Quantity** (has magnitude only, no direction). SI Unit: meter (m).\n\n2. **Displacement**: The shortest distance measured from the initial position to the final position of an object along with direction. It is a **Vector Quantity** (has both magnitude and direction). SI Unit: meter (m).\n\n*Key Difference*: Distance is always positive and non-zero for a moving body. Displacement can be positive, zero, or negative.",
            "body_hi": "1. **दूरी**: किसी भी दिशा में गतिमान वस्तु द्वारा तय किए गए पथ की वास्तविक कुल लंबाई। यह एक **अदिश राशि (Scalar Quantity)** है (केवल परिमाण होता है, दिशा नहीं)। SI इकाई: मीटर (m)।\n\n2. **विस्थापन**: प्रारंभिक स्थिति से अंतिम स्थिति तक दिशा के साथ मापी गई सबसे छोटी दूरी। यह एक **सदिश राशि (Vector Quantity)** है (परिमाण और दिशा दोनों होते हैं)। SI इकाई: मीटर (m)।\n\n*मुख्य अंतर*: गतिमान पिंड के लिए दूरी हमेशा धनात्मक और गैर-शून्य होती है। विस्थापन धनात्मक, शून्य या ऋणात्मक हो सकता है।",
            "body_gu": "1. **અંતર**: કોઈપણ દિશામાં ગતિમાન પદાર્થ દ્વારા કાપેલા માર્ગની વાસ્તવિક કુલ લંબાઈ। તે એક **અદિશ રાશિ (Scalar Quantity)** છે (ફક્ત મૂલ્ય હોય છે, દિશા નહીં)। SI એકમ: મીટર (m) ।\n\n2. **સ્થાનાંતર**: પ્રારંભિક સ્થાનથી અંતિમ સ્થાન સુધી દિશા સાથે માપવામાં આવતું સૌથી ટૂંકું અંતર। તે એક **સદિશ રાશિ (Vector Quantity)** છે (મૂલ્ય અને દિશા બંને હોય છે) । SI એકમ: મીટર (m) ।\n\n*મુખ્ય તફાવત*: ગતિમાન પદાર્થ માટે અંતર હંમેશા ધન અને બિન-શૂન્ય હોય છે। સ્થાનાંતર ધન, શૂન્ય અથવા ઋણ હોઈ શકે છે।"
        },

        # --- SPEED AND VELOCITY ---
        {
            "id": "KOBJ_CLASS9_SCI_CH7_THEORY_SPEED_VELOCITY",
            "type": "theory",
            "title": "Step 4: Reveal - Speed, Velocity & Acceleration",
            "title_hi": "चरण 4: प्रकटीकरण - चाल, वेग और त्वरण",
            "title_gu": "પગલું 4: પર્દાફાશ - ઝડપ, વેગ અને પ્રવેગ",
            "body": "1. **Speed**: Distance traveled per unit time.\n$$\\text{Speed } v = \\frac{\\text{Distance } s}{\\text{Time } t}$$\nSI unit: $\\text{m/s}$ or $\\text{ms}^{-1}$. Speed is a scalar quantity.\n\n2. **Velocity**: Speed in a specific direction (Displacement per unit time).\n$$\\text{Velocity } v = \\frac{\\text{Displacement } s}{\\text{Time } t}$$\nVelocity is a vector quantity. Average Velocity = $\\frac{u + v}{2}$ for uniform acceleration.\n\n3. **Acceleration ($a$)**: Rate of change of velocity per unit time.\n$$a = \\frac{v - u}{t}$$\nWhere $u$ = initial velocity, $v$ = final velocity, $t$ = time.\nSI Unit: $\\text{m/s}^2$ or $\\text{ms}^{-2}$.",
            "body_hi": "1. **चाल (Speed)**: प्रति इकाई समय में तय की गई दूरी।\n$$\\text{चाल } v = \\frac{\\text{दूरी } s}{\\text{समय } t}$$\nSI इकाई: $\\text{m/s}$। चाल एक अदिश राशि है।\n\n2. **वेग (Velocity)**: एक निर्दिष्ट दिशा में चाल (प्रति इकाई समय विस्थापन)।\n$$\\text{वेग } v = \\frac{\\text{विस्थापन } s}{\\text{समय } t}$$\nवेग एक सदिश राशि है। औसत वेग = $\\frac{u + v}{2}$ (समान त्वरण के लिए)।\n\n3. **त्वरण ($a$)**: प्रति इकाई समय में वेग में परिवर्तन की दर।\n$$a = \\frac{v - u}{t}$$\nजहाँ $u$ = प्रारंभिक वेग, $v$ = अंतिम वेग, $t$ = समय।\nSI इकाई: $\\text{m/s}^2$।",
            "body_gu": "1. **ઝડપ (Speed)**: એકમ સમયમાં કાપેલું અંતર।\n$$\\text{ઝડપ } v = \\frac{\\text{અંતર } s}{\\text{સમય } t}$$\nSI એકમ: $\\text{m/s}$। ઝડપ અદિશ રાશિ છે।\n\n2. **વેગ (Velocity)**: ચોક્કસ દિશામાં ઝડપ (એકમ સમયમાં સ્થાનાંતર) ।\n$$\\text{વેગ } v = \\frac{\\text{સ્થાનાંતર } s}{\\text{સમય } t}$$\nવેગ સદિશ રાશિ છે। સરેરાશ વેગ = $\\frac{u + v}{2}$ (સમાન પ્રવેગ માટે) ।\n\n3. **પ્રવેગ ($a$)**: એકમ સમયમાં વેગમાં થતા ફેરફારનો દર।\n$$a = \\frac{v - u}{t}$$\nજ્યાં $u$ = પ્રારંભિક વેગ, $v$ = અંતિમ વેગ, $t$ = સમય।\nSI એકમ: $\\text{m/s}^2$ ।"
        },

        # --- THREE EQUATIONS OF MOTION ---
        {
            "id": "KOBJ_CLASS9_SCI_CH7_THEORY_EQUATIONS_MOTION",
            "type": "theory",
            "title": "Step 4: Reveal - The Three Equations of Motion",
            "title_hi": "चरण 4: प्रकटीकरण - गति के तीन समीकरण",
            "title_gu": "પગલું 4: પર્દાફાશ - ગતિના ત્રણ સમીકરણો",
            "body": "When an object moves along a straight line with uniform acceleration $a$, its motion is governed by three fundamental equations:\n\n1. **First Equation of Motion (Velocity-Time Relation)**:\n$$v = u + at$$\n\n2. **Second Equation of Motion (Position-Time Relation)**:\n$$s = ut + \\frac{1}{2}at^2$$\n\n3. **Third Equation of Motion (Position-Velocity Relation)**:\n$$2as = v^2 - u^2$$\n\nWhere:\n- $u$ = Initial velocity ($\text{m/s}$)\n- $v$ = Final velocity ($\text{m/s}$)\n- $a$ = Uniform acceleration ($\text{m/s}^2$)\n- $t$ = Time interval ($\text{s}$)\n- $s$ = Distance / Displacement ($\text{m}$)",
            "body_hi": "जब कोई वस्तु समान त्वरण $a$ के साथ एक सीधी रेखा में चलती है, तो उसकी गति तीन मौलिक समीकरणों द्वारा नियंत्रित होती है:\n\n1. **गति का पहला समीकरण (वेग-समय संबंध)**:\n$$v = u + at$$\n\n2. **गति का दूसरा समीकरण (स्थिति-समय संबंध)**:\n$$s = ut + \\frac{1}{2}at^2$$\n\n3. **गति का तीसरा समीकरण (स्थिति-वेग संबंध)**:\n$$2as = v^2 - u^2$$\n\nजहाँ:\n- $u$ = प्रारंभिक वेग ($\text{m/s}$)\n- $v$ = अंतिम वेग ($\text{m/s}$)\n- $a$ = समान त्वरण ($\text{m/s}^2$)\n- $t$ = समय अंतराल ($\text{s}$)\n- $s$ = दूरी / विस्थापन ($\text{m}$)",
            "body_gu": "જ્યારે કોઈ પદાર્થ સમાન પ્રવેગ $a$ સાથે સીધી રેખામાં ગતિ કરે છે, ત્યારે તેની ગતિ ત્રણ મૂળભૂત સમીકરણો દ્વારા સંચાલિત થાય છે:\n\n1. **ગતિનું પ્રથમ સમીકરણ (વેગ-સમય સંબંધ)**:\n$$v = u + at$$\n\n2. **ગતિનું દ્વિતીય સમીકરણ (સ્થાન-સમય સંબંધ)**:\n$$s = ut + \\frac{1}{2}at^2$$\n\n3. **ગતિનું તૃતીય સમીકરણ (સ્થાન-વેગ સંબંધ)**:\n$$2as = v^2 - u^2$$\n\nજ્યાં:\n- $u$ = પ્રારંભિક વેગ ($\text{m/s}$)\n- $v$ = અંતિમ વેગ ($\text{m/s}$)\n- $a$ = સમાન પ્રવેગ ($\text{m/s}^2$)\n- $t$ = સમયગાળો ($\text{s}$)\n- $s$ = અંતર / સ્થાનાંતર ($\text{m}$)"
        },

        # --- UNIFORM CIRCULAR MOTION ---
        {
            "id": "KOBJ_CLASS9_SCI_CH7_THEORY_CIRCULAR_MOTION",
            "type": "theory",
            "title": "Step 4: Reveal - Uniform Circular Motion",
            "title_hi": "चरण 4: प्रकटीकरण - एकसमान वृत्तीय गति",
            "title_gu": "પગલું 4: પર્દાફાશ - એકસમાન વર્તુળાકાર ગતિ",
            "body": "When an object moves in a circular path with constant speed, its direction changes continuously at every point. Therefore, its velocity changes continuously, making it an **accelerated motion**.\n\n$$\\text{Speed in circular path } v = \\frac{2\\pi r}{t}$$\n\nwhere $r$ is the radius of the circular path and $t$ is the time taken for one full revolution.",
            "body_hi": "जब कोई वस्तु स्थिर चाल से वृत्ताकार पथ पर चलती है, तो उसकी दिशा हर बिंदु पर लगातार बदलती रहती है। इसलिए, इसका वेग लगातार बदलता रहता है, जिससे यह एक **त्वरित गति (accelerated motion)** बन जाती है।\n\n$$\\text{वृत्ताकार पथ में चाल } v = \\frac{2\\pi r}{t}$$\n\nजहाँ $r$ वृत्ताकार पथ की त्रिज्या है और $t$ एक पूर्ण चक्कर लगाने में लगा समय है।",
            "body_gu": "જ્યારે કોઈ પદાર્થ અચળ ઝડપ સાથે વર્તુળાકાર માર્ગ પર ગતિ કરે છે, ત્યારે દરેક બિંદુએ તેની દિશા સતત બદલાય છે। તેથી, તેનો વેગ સતત બદલાય છે, જે તેને **પ્રવેગી ગતિ (accelerated motion)** બનાવે છે।\n\n$$\\text{વર્તુળાકાર માર્ગમાં ઝડપ } v = \\frac{2\\pi r}{t}$$\n\nજ્યાં $r$ વર્તુળાકાર માર્ગની ત્રિજ્યા છે અને $t$ એક પૂર્ણ પરિભ્રમણ માટે લીધેલ સમય છે।"
        },

        # --- IN-TEXT QUESTION 1: ODOMETER ---
        {
            "id": "KOBJ_CLASS9_SCI_CH7_INTEXT_1",
            "type": "quiz",
            "title": "In-Text Question: Automobile Odometer",
            "title_hi": "पाठ्यनिहित प्रश्न: ऑटोमोबाइल ओडोमीटर",
            "title_gu": "પાઠ્યપુસ્તક પ્રશ્ન: ઓટોમોબાઈલ ઓડોમીટર",
            "question": "What does the odometer of an automobile measure?",
            "question_hi": "स्वचालित वाहन का ओडोमीटर क्या मापता है?",
            "question_gu": "ઓટોમોબાઈલનું ઓડોમીટર શું માપે છે?",
            "options": [
                "Speed of the vehicle",
                "Total distance traveled by the vehicle",
                "Acceleration of the vehicle",
                "Displacement of the vehicle"
            ],
            "options_hi": [
                "वाहन की चाल",
                "वाहन द्वारा तय की गई कुल दूरी",
                "वाहन का त्वरण",
                "वाहन का विस्थापन"
            ],
            "options_gu": [
                "વાહન ની ઝડપ",
                "વાહન દ્વારા કાપેલું કુલ અંતર",
                "વાહન નો પ્રવેગ",
                "વાહન નું સ્થાનાંતર"
            ],
            "correct_index": 1,
            "explanation": "An odometer measures the total distance traveled by an automobile. Speed is measured by a speedometer.",
            "explanation_hi": "ओडोमीटर वाहन द्वारा तय की गई कुल दूरी को मापता है। चाल को स्पीडोमीटर द्वारा मापा जाता है।",
            "explanation_gu": "ઓડોમીટર ઓટોમોબાઈલ દ્વારા કાપેલું કુલ અંતર માપે છે। ઝડપ સ્પીડોમીટર દ્વારા માપવામાં આવે છે।"
        },

        # --- IN-TEXT QUESTION 2: SIGNAL FROM SPACESHIP ---
        {
            "id": "KOBJ_CLASS9_SCI_CH7_INTEXT_2",
            "type": "quiz",
            "title": "In-Text Question: Signal from Spaceship",
            "title_hi": "पाठ्यनिहित प्रश्न: अंतरिक्ष यान से संकेत",
            "title_gu": "પાઠ્યપુસ્તક પ્રશ્ન: સ્પેસશિપમાંથી સિગ્નલ",
            "question": "During an experiment, a signal from a spaceship reached the ground station in 5 minutes. What was the distance of the spaceship from the ground station? (Speed of signal = 3 × 10^8 m/s)",
            "question_hi": "एक प्रयोग के दौरान, अंतरिक्ष यान से एक संकेत 5 मिनट में ग्राउंड स्टेशन पहुंचा। ग्राउंड स्टेशन से अंतरिक्ष यान की दूरी क्या थी? (संकेत की चाल = 3 × 10^8 m/s)",
            "question_gu": "એક પ્રયોગ દરમિયાન, સ્પેસશિપમાંથી સિગ્નલ 5 મિનિટમાં ગ્રાઉન્ડ સ્ટેશન પર પહોંચ્યું। ગ્રાઉન્ડ સ્ટેશનથી સ્પેસશિપનું અંતર કેટલું હતું? (સિગ્નલની ઝડપ = 3 × 10^8 m/s)",
            "options": [
                "9 × 10^10 m",
                "1.5 × 10^9 m",
                "9 × 10^8 m",
                "1.5 × 10^11 m"
            ],
            "options_hi": [
                "9 × 10^10 मीटर",
                "1.5 × 10^9 मीटर",
                "9 × 10^8 मीटर",
                "1.5 × 10^11 मीटर"
            ],
            "options_gu": [
                "9 × 10^10 મીટર",
                "1.5 × 10^9 મીટર",
                "9 × 10^8 મીટર",
                "1.5 × 10^11 મીટર"
            ],
            "correct_index": 0,
            "explanation": "Time t = 5 min = 5 × 60 = 300 s. Speed v = 3 × 10^8 m/s. Distance s = v × t = (3 × 10^8) × 300 = 9 × 10^10 m.",
            "explanation_hi": "समय t = 5 मिनट = 5 × 60 = 300 सेकंड। चाल v = 3 × 10^8 m/s। दूरी s = v × t = (3 × 10^8) × 300 = 9 × 10^10 मीटर।",
            "explanation_gu": "સમય t = 5 મિનિટ = 5 × 60 = 300 સેકન્ડ। ઝડપ v = 3 × 10^8 m/s। અંતર s = v × t = (3 × 10^8) × 300 = 9 × 10^10 મીટર।"
        },

        # --- IN-TEXT QUESTION 3: BUS ACCELERATION ---
        {
            "id": "KOBJ_CLASS9_SCI_CH7_INTEXT_3",
            "type": "quiz",
            "title": "In-Text Question: Bus Decreasing Speed",
            "title_hi": "पाठ्यनिहित प्रश्न: बस की चाल में कमी",
            "title_gu": "પાઠ્યપુસ્તક પ્રશ્ન: બસની ઝડપમાં ઘટાડો",
            "question": "A bus decreases its speed from 80 km/h to 60 km/h in 5 s. What is the acceleration of the bus?",
            "question_hi": "एक बस 5 सेकंड में अपनी चाल 80 किमी/घंटा से घटाकर 60 किमी/घंटा कर देती है। बस का त्वरण क्या है?",
            "question_gu": "એક બસ 5 સેકન્ડમાં તેની ઝડપ 80 km/h થી ઘટાડીને 60 km/h કરે છે। બસનો પ્રવેગ કેટલો છે?",
            "options": [
                "-1.11 m/s²",
                "-2.22 m/s²",
                "1.11 m/s²",
                "-4.00 m/s²"
            ],
            "options_hi": [
                "-1.11 m/s²",
                "-2.22 m/s²",
                "1.11 m/s²",
                "-4.00 m/s²"
            ],
            "options_gu": [
                "-1.11 m/s²",
                "-2.22 m/s²",
                "1.11 m/s²",
                "-4.00 m/s²"
            ],
            "correct_index": 0,
            "explanation": "u = 80 km/h = 80 × (5/18) = 22.22 m/s. v = 60 km/h = 60 × (5/18) = 16.67 m/s. t = 5 s. Acceleration a = (v - u)/t = (16.67 - 22.22)/5 = -1.11 m/s².",
            "explanation_hi": "u = 80 × (5/18) = 22.22 m/s। v = 60 × (5/18) = 16.67 m/s। t = 5 s। त्वरण a = (16.67 - 22.22)/5 = -1.11 m/s²।",
            "explanation_gu": "u = 80 × (5/18) = 22.22 m/s। v = 60 × (5/18) = 16.67 m/s। t = 5 s। પ્રવેગ a = (16.67 - 22.22)/5 = -1.11 m/s²।"
        },

        # --- TEXTBOOK EXERCISE 1: ATHLETE ---
        {
            "id": "KOBJ_CLASS9_SCI_CH7_EX_1",
            "type": "quiz",
            "title": "Textbook Exercise 1: Athlete on Circular Track",
            "title_hi": "पाठ्यपुस्तक अभ्यास 1: वृत्ताकार ट्रैक पर एथलीट",
            "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 1: વર્તુળાકાર ટ્રેક પર એથ્લેટ",
            "question": "An athlete completes one round of a circular track of diameter 200 m in 40 s. What will be the distance covered and the displacement at the end of 2 minutes 20 s?",
            "question_hi": "एक एथलीट 200 मीटर व्यास वाले वृत्ताकार ट्रैक का एक चक्कर 40 सेकंड में पूरा करता है। 2 मिनट 20 सेकंड के अंत में तय की गई दूरी और विस्थापन क्या होगा?",
            "question_gu": "એક એથ્લેટ 200 મીટર વ્યાસવાળા વર્તુળાકાર ટ્રેકનું એક ચક્કર 40 સેકન્ડમાં પૂરું કરે છે। 2 મિનિટ 20 સેકન્ડના અંતે કાપેલું અંતર અને સ્થાનાંતર કેટલું હશે?",
            "options": [
                "Distance = 2200 m, Displacement = 200 m",
                "Distance = 1400 m, Displacement = 0 m",
                "Distance = 2200 m, Displacement = 0 m",
                "Distance = 4400 m, Displacement = 100 m"
            ],
            "options_hi": [
                "दूरी = 2200 मीटर, विस्थापन = 200 मीटर",
                "दूरी = 1400 मीटर, विस्थापन = 0 मीटर",
                "दूरी = 2200 मीटर, विस्थापन = 0 मीटर",
                "दूरी = 4400 मीटर, विस्थापन = 100 मीटर"
            ],
            "options_gu": [
                "અંતર = 2200 મીટર, સ્થાનાંતર = 200 મીટર",
                "અંતર = 1400 મીટર, સ્થાનાંતર = 0 મીટર",
                "અંતર = 2200 મીટર, સ્થાનાંતર = 0 મીટર",
                "અંતર = 4400 મીટર, સ્થાનાંતર = 100 મીટર"
            ],
            "correct_index": 0,
            "explanation": "Radius r = 100 m. Time t = 2 min 20 s = 140 s. Rounds = 140 / 40 = 3.5 rounds. Distance = 3.5 × 2πr = 3.5 × 2 × (22/7) × 100 = 2200 m. After 3.5 rounds, athlete is at opposite end of diameter, so displacement = diameter = 200 m.",
            "explanation_hi": "त्रिज्या r = 100 मीटर। समय t = 140 सेकंड। चक्कर = 140 / 40 = 3.5 चक्कर। दूरी = 3.5 × 2πr = 2200 मीटर। 3.5 चक्कर के बाद विस्थापन = व्यास = 200 मीटर।",
            "explanation_gu": "ત્રિજ્યા r = 100 મીટર। સમય t = 140 સેકન્ડ। ચક્કર = 140 / 40 = 3.5 ચક્કર। અંતર = 3.5 × 2πr = 2200 મીટર। 3.5 ચક્કર પછી સ્થાનાંતર = વ્યાસ = 200 મીટર।"
        },

        # --- TEXTBOOK EXERCISE 2: JOSEPH JOGGING ---
        {
            "id": "KOBJ_CLASS9_SCI_CH7_EX_2",
            "type": "quiz",
            "title": "Textbook Exercise 2: Joseph's Jogging",
            "title_hi": "पाठ्यपुस्तक अभ्यास 2: जोसेफ की जॉगिंग",
            "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 2: જોસેફની જોગિંગ",
            "question": "Joseph jogs from A to B (300 m straight in 2 min 30 s) then turns back to C (100 m in 1 min). What is his average speed and average velocity from A to C?",
            "question_hi": "जोसेफ A से B (2 मिनट 30 सेकंड में 300 मीटर सीधा) जॉगिंग करता है और फिर C पर वापस आता है (1 मिनट में 100 मीटर)। A से C तक उसकी औसत चाल और औसत वेग क्या है?",
            "question_gu": "જોસેફ A થી B (2 મિનિટ 30 સેકન્ડમાં 300 મીટર સીધું) જોગિંગ કરે છે અને પછી C તરફ પાછો ફરે છે (1 મિનિટમાં 100 મીટર) । A થી C સુધી તેની સરેરાશ ઝડપ અને સરેરાશ વેગ કેટલો છે?",
            "options": [
                "Average speed = 1.90 m/s, Average velocity = 0.95 m/s",
                "Average speed = 2.00 m/s, Average velocity = 2.00 m/s",
                "Average speed = 1.50 m/s, Average velocity = 1.00 m/s",
                "Average speed = 0.95 m/s, Average velocity = 1.90 m/s"
            ],
            "options_hi": [
                "औसत चाल = 1.90 m/s, औसत वेग = 0.95 m/s",
                "औसत चाल = 2.00 m/s, औसत वेग = 2.00 m/s",
                "औसत चाल = 1.50 m/s, औसत वेग = 1.00 m/s",
                "औसत चाल = 0.95 m/s, औसत वेग = 1.90 m/s"
            ],
            "options_gu": [
                "સરેરાશ ઝડપ = 1.90 m/s, સરેરાશ વેગ = 0.95 m/s",
                "સરેરાશ ઝડપ = 2.00 m/s, સરેરાશ વેગ = 2.00 m/s",
                "સરેરાશ ઝડપ = 1.50 m/s, સરેરાશ વેગ = 1.00 m/s",
                "સરેરાશ ઝડપ = 0.95 m/s, સરેરાશ વેગ = 1.90 m/s"
            ],
            "correct_index": 0,
            "explanation": "From A to C: Total Distance = 300 + 100 = 400 m. Displacement = 300 - 100 = 200 m. Total Time = 150 s + 60 s = 210 s. Average Speed = 400 / 210 = 1.90 m/s. Average Velocity = 200 / 210 = 0.95 m/s.",
            "explanation_hi": "कुल दूरी = 400 मीटर, विस्थापन = 200 मीटर, कुल समय = 210 सेकंड। औसत चाल = 400/210 = 1.90 m/s। औसत वेग = 200/210 = 0.95 m/s।",
            "explanation_gu": "કુલ અંતર = 400 મીટર, સ્થાનાંતર = 200 મીટર, કુલ સમય = 210 સેકન્ડ। સરેરાશ ઝડપ = 400/210 = 1.90 m/s। સરેરાશ વેગ = 200/210 = 0.95 m/s।"
        },

        # --- TEXTBOOK EXERCISE 3: ABDUL'S TRIP ---
        {
            "id": "KOBJ_CLASS9_SCI_CH7_EX_3",
            "type": "quiz",
            "title": "Textbook Exercise 3: Abdul's Average Speed",
            "title_hi": "पाठ्यपुस्तक अभ्यास 3: अब्दुल की औसत चाल",
            "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 3: અબ્દુલની સરેરાશ ઝડપ",
            "question": "Abdul drives to school at an average speed of 20 km/h. On the return trip along the same route, average speed is 30 km/h. What is the average speed for the whole trip?",
            "question_hi": "अब्दुल 20 किमी/घंटा की औसत चाल से स्कूल जाता है। उसी रास्ते से लौटते समय औसत चाल 30 किमी/घंटा है। पूरी यात्रा के लिए औसत चाल क्या है?",
            "question_gu": "અબ્દુલ 20 km/h ની સરેરાશ ઝડપે શાળાએ જાય છે। તે જ માર્ગે પાછા ફરતી વખતે સરેરાશ ઝડપ 30 km/h છે। આખી મુસાફરી માટે સરેરાશ ઝડપ કેટલી છે?",
            "options": [
                "25 km/h",
                "24 km/h",
                "22.5 km/h",
                "26 km/h"
            ],
            "options_hi": [
                "25 किमी/घंटा",
                "24 किमी/घंटा",
                "22.5 किमी/घंटा",
                "26 किमी/घंटा"
            ],
            "options_gu": [
                "25 km/h",
                "24 km/h",
                "22.5 km/h",
                "26 km/h"
            ],
            "correct_index": 1,
            "explanation": "Let distance be d. Time going t1 = d/20. Time returning t2 = d/30. Total distance = 2d. Total time = d/20 + d/30 = (5d)/60 = d/12. Average speed = 2d / (d/12) = 24 km/h.",
            "explanation_hi": "मान लीजिए दूरी d है। समय t1 = d/20, t2 = d/30। कुल दूरी = 2d। कुल समय = d/12। औसत चाल = 2d / (d/12) = 24 किमी/घंटा।",
            "explanation_gu": "ધારો કે અંતર d છે। સમય t1 = d/20, t2 = d/30। કુલ અંતર = 2d। કુલ સમય = d/12। સરેરાશ ઝડપ = 2d / (d/12) = 24 km/h।"
        },

        # --- TEXTBOOK EXERCISE 4: MOTORBOAT ---
        {
            "id": "KOBJ_CLASS9_SCI_CH7_EX_4",
            "type": "quiz",
            "title": "Textbook Exercise 4: Motorboat Distance",
            "title_hi": "पाठ्यपुस्तक अभ्यास 4: मोटरबोट की दूरी",
            "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 4: મોટરબોટનું અંતર",
            "question": "A motorboat starting from rest accelerates in a straight line at 3.0 m/s² for 8.0 s. How far does the boat travel during this time?",
            "question_hi": "विरामवस्था से शुरू होने वाली एक मोटरबोट 8.0 सेकंड के लिए 3.0 m/s² की दर से सीधी रेखा में त्वरित होती है। इस दौरान नाव कितनी दूरी तय करती है?",
            "question_gu": "સ્થિર સ્થિતિમાંથી શરૂ થતી મોટરબોટ 8.0 સેકન્ડ માટે 3.0 m/s² ના દરથી સીધી રેખામાં પ્રવેગિત થાય છે। આ સમય દરમિયાન બોટ કેટલું અંતર કાપે છે?",
            "options": [
                "96 m",
                "48 m",
                "24 m",
                "192 m"
            ],
            "options_hi": [
                "96 मीटर",
                "48 मीटर",
                "24 मीटर",
                "192 मीटर"
            ],
            "options_gu": [
                "96 મીટર",
                "48 મીટર",
                "24 મીટર",
                "192 મીટર"
            ],
            "correct_index": 0,
            "explanation": "u = 0 m/s, a = 3.0 m/s², t = 8.0 s. Using s = ut + (1/2)at² = 0 + 0.5 × 3 × (8)² = 0.5 × 3 × 64 = 96 m.",
            "explanation_hi": "u = 0, a = 3.0 m/s², t = 8 s। s = ut + (1/2)at² = 0 + 0.5 × 3 × 64 = 96 मीटर।",
            "explanation_gu": "u = 0, a = 3.0 m/s², t = 8 s। s = ut + (1/2)at² = 0 + 0.5 × 3 × 64 = 96 મીટર।"
        },

        # --- TEXTBOOK EXERCISE 7: DROPPED BALL ---
        {
            "id": "KOBJ_CLASS9_SCI_CH7_EX_7",
            "type": "quiz",
            "title": "Textbook Exercise 7: Ball Dropped from Height",
            "title_hi": "पाठ्यपुस्तक अभ्यास 7: ऊंचाई से गिराई गई गेंद",
            "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 7: ઊંચાઈએથી ફેંકેલો દડો",
            "question": "A ball is gently dropped from a height of 20 m. If its velocity increases uniformly at 10 m/s², with what velocity and after what time will it strike the ground?",
            "question_hi": "एक गेंद को 20 मीटर की ऊंचाई से धीरे से गिराया जाता है। यदि इसका वेग 10 m/s² की दर से बढ़ता है, तो यह किस वेग से और कितने समय बाद जमीन से टकराएगी?",
            "question_gu": "એક દડાને 20 મીટરની ઊંચાઈએથી ધીમેથી છોડવામાં આવે છે। જો તેનો વેગ 10 m/s² ના દરે વધે છે, તો તે કયા વેગથી અને કેટલા સમય પછી જમીન સાથે અથડાશે?",
            "options": [
                "Velocity = 20 m/s, Time = 2 s",
                "Velocity = 10 m/s, Time = 1 s",
                "Velocity = 40 m/s, Time = 4 s",
                "Velocity = 20 m/s, Time = 4 s"
            ],
            "options_hi": [
                "वेग = 20 m/s, समय = 2 सेकंड",
                "वेग = 10 m/s, समय = 1 सेकंड",
                "वेग = 40 m/s, समय = 4 सेकंड",
                "वेग = 20 m/s, समय = 4 सेकंड"
            ],
            "options_gu": [
                "વેગ = 20 m/s, સમય = 2 સેકન્ડ",
                "વેગ = 10 m/s, સમય = 1 સેકન્ડ",
                "વેગ = 40 m/s, સમય = 4 સેકન્ડ",
                "વેગ = 20 m/s, સમય = 4 સેકન્ડ"
            ],
            "correct_index": 0,
            "explanation": "u = 0, s = 20 m, a = 10 m/s². v² = u² + 2as = 0 + 2(10)(20) = 400 => v = 20 m/s. Time t = (v - u)/a = (20 - 0)/10 = 2 s.",
            "explanation_hi": "u = 0, s = 20, a = 10। v² = 2as = 400 => v = 20 m/s। समय t = v/a = 20/10 = 2 सेकंड।",
            "explanation_gu": "u = 0, s = 20, a = 10। v² = 2as = 400 => v = 20 m/s। સમય t = v/a = 20/10 = 2 સેકન્ડ।"
        },

        # --- TEXTBOOK EXERCISE 10: ARTIFICIAL SATELLITE ---
        {
            "id": "KOBJ_CLASS9_SCI_CH7_EX_10",
            "type": "quiz",
            "title": "Textbook Exercise 10: Artificial Satellite Speed",
            "title_hi": "पाठ्यपुस्तक अभ्यास 10: कृत्रिम उपग्रह की चाल",
            "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 10: કૃત્રિમ ઉપગ્રહની ઝડપ",
            "question": "An artificial satellite is moving in a circular orbit of radius 42250 km. Calculate its speed if it takes 24 hours to revolve around the Earth.",
            "question_hi": "एक कृत्रिम उपग्रह 42250 किमी त्रिज्या की वृत्ताकार कक्षा में घूम रहा है। यदि इसे पृथ्वी का चक्कर लगाने में 24 घंटे लगते हैं तो इसकी चाल की गणना कीजिए।",
            "question_gu": "એક કૃત્રિમ ઉપગ્રહ 42250 km ત્રિજ્યાની વર્તુળાકાર કક્ષામાં ભ્રમણ કરી રહ્યો છે। જો તેને પૃથ્વીની આસપાસ ફરતા 24 કલાક લાગે તો તેની ઝડપ શોધો।",
            "options": [
                "3.07 km/s",
                "11.05 km/s",
                "1.54 km/s",
                "5.21 km/s"
            ],
            "options_hi": [
                "3.07 किमी/सेकंड",
                "11.05 किमी/सेकंड",
                "1.54 किमी/सेकंड",
                "5.21 किमी/सेकंड"
            ],
            "options_gu": [
                "3.07 km/s",
                "11.05 km/s",
                "1.54 km/s",
                "5.21 km/s"
            ],
            "correct_index": 0,
            "explanation": "r = 42250 km. Circumference = 2πr = 2 × 3.1416 × 42250 = 265464.57 km. Time t = 24 hours = 24 × 3600 s = 86400 s. Speed v = 265464.57 / 86400 = 3.07 km/s.",
            "explanation_hi": "r = 42250 किमी। परिधि = 2πr = 265464.57 किमी। समय t = 86400 सेकंड। चाल v = 265464.57 / 86400 = 3.07 किमी/सेकंड।",
            "explanation_gu": "r = 42250 km। પરિધ = 2πr = 265464.57 km। સમય t = 86400 સેકન્ડ। ઝડપ v = 265464.57 / 86400 = 3.07 km/s।"
        },

        # --- STEP 6: REFLECTION ---
        {
            "id": "KOBJ_CLASS9_SCI_CH7_REFLECTION",
            "type": "reflection",
            "title": "Step 6: Reflection - Motion in Daily Life",
            "title_hi": "चरण 6: विचार-विमर्श - दैनिक जीवन में गति",
            "title_gu": "પગલું 6: મનન - દૈનિક જીવનમાં ગતિ",
            "body": "Reflect on how we experience motion daily:\n1. Why does a passenger fall backward when a bus suddenly starts moving forward?\n2. Why do race cars require high acceleration rather than just high speed?\n3. Can a body have zero velocity but still have acceleration? (Hint: Think of a stone thrown straight up at its peak height!).",
            "body_hi": "विचार करें कि हम प्रतिदिन गति का अनुभव कैसे करते हैं:\n1. जब बस अचानक आगे चलती है तो यात्री पीछे की ओर क्यों गिरता है?\n2. रेस कारों को केवल उच्च चाल के बजाय उच्च त्वरण की आवश्यकता क्यों होती है?\n3. क्या किसी पिंड का वेग शून्य हो सकता है लेकिन फिर भी उसमें त्वरण हो सकता है? (संकेत: उच्चतम ऊंचाई पर ऊपर की ओर फेंके गए पत्थर के बारे में सोचें!)।",
            "body_gu": "આપણે દૈનિક જીવનમાં ગતિનો અનુભવ કેવી રીતે કરીએ છીએ તે વિશે વિચાર કરો:\n1. જ્યારે બસ અચાનક આગળ વધે છે ત્યારે મુસાફર પાછળ કેમ નમે છે?\n2. રેસ કારોને માત્ર ઊંચી ઝડપને બદલે ઊંચા પ્રવેગની કેમ જરૂર હોય છે?\n3. શું પદાર્થનો વેગ શૂન્ય હોવા છતાં તેમાં પ્રવેગ હોઈ શકે? (સંકેત: મહત્તમ ઊંચાઈએ ઉપર તરફ ફેંકેલા પથ્થર વિશે વિચારો!)।"
        },

        # --- STEP 7: CONNECTION ---
        {
            "id": "KOBJ_CLASS9_SCI_CH7_CONNECTION",
            "type": "connection",
            "title": "Step 7: Knowledge Graph Connection",
            "title_hi": "चरण 7: ज्ञान ग्राफ संबंध",
            "title_gu": "પગલું 7: જ્ઞાન ગ્રાફ જોડાણ",
            "body": "Motion forms the bedrock of Physics:\n- **Prerequisite**: Basic Measurement (Distance, Time, Units).\n- **Next Chapter**: Force and Laws of Motion (Newton's 1st, 2nd, and 3rd laws explain *why* motion changes).\n- **Future Topics**: Gravitation (free fall under g = 9.8 m/s²), Work & Energy, Planetary Orbits.",
            "body_hi": "गति भौतिकी का आधार बनती है:\n- **पूर्व-आवश्यकता**: मूल मापन (दूरी, समय, इकाइयाँ)।\n- **अगला अध्याय**: बल तथा गति के नियम (न्यूटन के नियम बताते हैं कि गति क्यों बदलती है)।\n- **भविष्य के विषय**: गुरुत्वाकर्षण, कार्य तथा ऊर्जा, ग्रहीय कक्षाएँ।",
            "body_gu": "ગતિ એ ભૌતિકશાસ્ત્રનો પાયો છે:\n- **પૂર્વ-જરૂરિયાત**: મૂળભૂત માપન (અંતર, સમય, એકમો) ।\n- **આગળનું પ્રકરણ**: બળ તથા ગતિના નિયમો (ન્યૂટનના નિયમો સમજાવે છે કે ગતિ શા માટે બદલાય છે) ।\n- **ભવિષ્યના વિષયો**: ગુરુત્વાકર્ષણ, કાર્ય અને ઊર્જા, ગ્રહોની કક્ષાઓ।"
        },

        # --- STEP 8: MASTERY ---
        {
            "id": "KOBJ_CLASS9_SCI_CH7_MASTERY",
            "type": "mastery",
            "title": "Step 8: Mastery - Application Challenge",
            "title_hi": "चरण 8: महारत - अनुप्रयोग चुनौती",
            "title_gu": "પગલું 8: માસ્ટરી - એપ્લિકેશન પડકાર",
            "body": "Mastery Challenge: Analyze a car moving on a highway.\n1. Graph Reading: Draw a Velocity-Time graph for a car accelerating from 0 to 20 m/s in 10 s, maintaining 20 m/s for 20 s, and braking to stop in 5 s.\n2. Calculate the total displacement by finding the area under the V-T trapezoid graph!\n(Area of Trapezoid = 0.5 × (Sum of parallel sides) × Height = 0.5 × (35 + 20) × 20 = 550 meters).",
            "body_hi": "महारत चुनौती: हाईवे पर चलती कार का विश्लेषण करें।\n1. ग्राफ पठन: 10 सेकंड में 0 से 20 m/s तक त्वरित होने वाली, 20 सेकंड तक 20 m/s बनाए रखने वाली और 5 सेकंड में रुकने वाली कार के लिए वेग-समय ग्राफ बनाएं।\n2. V-T समलम्ब ग्राफ के तहत क्षेत्रफल ज्ञात करके कुल विस्थापन की गणना करें!\n(समलम्ब का क्षेत्रफल = 0.5 × (समांतर भुजाओं का योग) × ऊंचाई = 0.5 × (35 + 20) × 20 = 550 मीटर)।",
            "body_gu": "માસ્ટરી પડકાર: હાઇવે પર ચાલતી કારનું વિશ્લેષણ કરો।\n1. આલેખ વાંચન: 10 સેકન્ડમાં 0 થી 20 m/s સુધી પ્રવેગિત થતી, 20 સેકન્ડ માટે 20 m/s જાળવી રાખતી અને 5 સેકન્ડમાં બ્રેક મારીને રોકાતી કાર માટે વેગ-સમય આલેખ દોરો।\n2. V-T સમલંબ આલેખ હેઠળનું ક્ષેત્રફળ શોધીને કુલ સ્થાનાંતરની ગણતરી કરો!\n(સમલંબનું ક્ષેત્રફળ = 0.5 × (સમાંતર બાજુઓનો સરવાળો) × ઊંચાઈ = 0.5 × (35 + 20) × 20 = 550 મીટર) ।"
        }
    ]

    # Target directories
    mod_dir = "app_core/learning_modules/gseb_class9_science_ch7"
    os.makedirs(mod_dir, exist_ok=True)
    blocks_file = os.path.join(mod_dir, "blocks.json")

    with open(blocks_file, "w", encoding="utf-8") as f:
        json.dump(blocks, f, ensure_ascii=False, indent=2)

    # Sync to ncert_class9_science_ch7.json
    ncert_file = "app_core/chapters/ncert_class9_science_ch7.json"
    os.makedirs("app_core/chapters", exist_ok=True)
    with open(ncert_file, "w", encoding="utf-8") as f:
        json.dump(blocks, f, ensure_ascii=False, indent=2)

    # Build Assessment Bank
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

    assess_file = "app_core/assessment/gseb_class9_science_ch7_questions.json"
    os.makedirs("app_core/assessment", exist_ok=True)
    with open(assess_file, "w", encoding="utf-8") as f:
        json.dump(assessment_questions, f, ensure_ascii=False, indent=2)

    print(f"Total blocks generated for Class 9 Science Ch 7 (Motion): {len(blocks)}")
    print(f"Saved blocks to {blocks_file}")
    print(f"Synced to {ncert_file}")
    print(f"Updated assessment bank at {assess_file}")

if __name__ == "__main__":
    generate_ch7_motion()
