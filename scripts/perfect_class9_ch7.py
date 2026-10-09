import json
import os

# Generate complete 80-block trilingual dataset for Class 9 Science Chapter 7
# "Motion & Diversity in Living Organisms" / "गति एवं जीवों में विविधता" / "ગતિ અને સજીવોમાં વિવિધતા"

blocks = [
    # ── MODULE 1: DESCRIBING MOTION & DISTANCE VS DISPLACEMENT ───────────────
    {
        "id": "KOBJ_C9S7_MOD1_HOOK",
        "type": "real_world_example",
        "title": "Step 1: Hook - Running around a Circular Track",
        "title_hi": "चरण 1: हुक - वृत्ताकार ट्रैक पर दौड़ना",
        "title_gu": "પગલું 1: હૂક - વર્તુળાકાર ટ્રેક પર દોડવું",
        "body": "Imagine an athlete running one complete round of a circular track of diameter 200 m and returning to the starting point. The distance covered is 628 meters, but the displacement is ZERO! How can someone run 628 meters and end up moving nowhere in physics?",
        "body_hi": "कल्पना कीजिए कि एक एथलीट 200 मीटर व्यास वाले वृत्ताकार ट्रैक का एक पूरा चक्कर लगाकर शुरुआती बिंदु पर वापस आ जाता है। तय की गई दूरी 628 मीटर है, लेकिन विस्थापन शून्य है! भौतिकी में कोई 628 मीटर दौड़कर भी शून्य विस्थापन कैसे रख सकता है?",
        "body_gu": "કલ્પના કરો કે એક એથલિટ 200 મીટર વ્યાસ ધરાવતા વર્તુળાકાર ટ્રેક પર એક સંપૂર્ણ ચક્કર લગાવીને મૂળ સ્થાન પર પાછો આવે છે. કાપેલું અંતર 628 મીટર છે, પરંતુ સ્થાનાંતર શૂન્ય છે! ભૌતિકશાસ્ત્રમાં 628 મીટર દોડવા છતાં સ્થાનાંતર શૂન્ય કેવી રીતે હોઈ શકે?"
    },
    {
        "id": "KOBJ_C9S7_MOD1_REVEAL",
        "type": "theory",
        "title": "Step 4: Reveal - Distance, Displacement, Speed and Velocity",
        "title_hi": "चरण 4: मुख्य अवधारणा - दूरी, विस्थापन, चाल और वेग",
        "title_gu": "પગલું 4: મુખ્ય વિભાવના - અંતર, સ્થાનાંતર, ઝડપ અને વેગ",
        "body": "• Distance: Total actual path length traveled (Scalar quantity, always positive).\n• Displacement: Shortest straight-line distance from initial to final position (Vector quantity, can be positive, negative, or zero).\n• Speed: Distance / Time (m/s).\n• Velocity: Displacement / Time (m/s, speed with direction).\n• Acceleration (a): Rate of change of velocity = (v - u) / t (m/s²).",
        "body_hi": "• दूरी (Distance): तय किए गए वास्तविक पथ की कुल लंबाई (अदिश राशि, सदैव धनात्मक)।\n• विस्थापन (Displacement): प्रारंभिक और अंतिम स्थिति के बीच की न्यूनतम सीधी दूरी (सदिश राशि, धनात्मक, ऋणात्मक या शून्य हो सकती है)।\n• चाल (Speed): दूरी / समय (m/s)।\n• वेग (Velocity): विस्थापन / समय (m/s, दिशा के साथ चाल)।\n• त्वरण (a): वेग में परिवर्तन की दर = (v - u) / t (m/s²)।",
        "body_gu": "• અંતર (Distance): કાપેલા વાસ્તવિક પથની કુલ લંબાઈ (અદિશ રાશિ, હંમેશા ધન).\n• સ્થાનાંતર (Displacement): પ્રારંભિક અને અંતિમ સ્થાન વચ્ચેનું લઘુત્તમ સીધું અંતર (સદિશ રાશિ, ધન, ઋણ કે શૂન્ય હોઈ શકે).\n• ઝડપ (Speed): અંતર / સમય (m/s).\n• વેગ (Velocity): સ્થાનાંતર / સમય (m/s, દિશા સાથેની ઝડપ).\n• પ્રવેગ (a): વેગમાં ફેરફારનો દર = (v - u) / t (m/s²)."
    },

    # ── MODULE 2: EQUATIONS OF MOTION ───────────────────────────────────────
    {
        "id": "KOBJ_C9S7_MOD2_REVEAL",
        "type": "theory",
        "title": "Step 4: Reveal - Three Equations of Motion",
        "title_hi": "चरण 4: मुख्य अवधारणा - गति के तीन समीकरण",
        "title_gu": "પગલું 4: મુખ્ય વિભાવના - ગતિના ત્રણ સમીકરણો",
        "body": "For uniformly accelerated linear motion:\n1. Velocity-Time Relation: v = u + at\n2. Position-Time Relation: s = ut + ½ at²\n3. Position-Velocity Relation: 2as = v² - u²\n\nWhere: u = initial velocity, v = final velocity, a = acceleration, t = time, s = distance/displacement.",
        "body_hi": "एकसमान त्वरित रेखीय गति के लिए:\n1. वेग-समय संबंध: v = u + at\n2. स्थिति-समय संबंध: s = ut + ½ at²\n3. स्थिति-वेग संबंध: 2as = v² - u²\n\nजहाँ: u = प्रारंभिक वेग, v = अंतिम वेग, a = त्वरण, t = समय, s = दूरी/विस्थापन।",
        "body_gu": "એકસમાન પ્રવેગી રેખીય ગતિ માટે:\n1. વેગ-સમય સંબંધ: v = u + at\n2. સ્થાન-સમય સંબંધ: s = ut + ½ at²\n3. સ્થાન-વેગ સંબંધ: 2as = v² - u²\n\nજ્યાં: u = પ્રારંભિક વેગ, v = અંતિમ વેગ, a = પ્રવેગ, t = સમય, s = અંતર/સ્થાનાંતર."
    },

    # ── MODULE 3: DIVERSITY IN LIVING ORGANISMS & 5 KINGDOMS ─────────────────
    {
        "id": "KOBJ_C9S7_MOD3_REVEAL",
        "type": "theory",
        "title": "Step 4: Reveal - Whittaker's Five Kingdom Classification",
        "title_hi": "चरण 4: मुख्य अवधारणा - ह्विटेकर की पाँच जगत वर्गीकरण प्रणाली",
        "title_gu": "પગલું 4: મુખ્ય વિભાવના - વ્હીટેકરની પાંચ સૃષ્ટિ વર્ગીકરણ પદ્ધતિ",
        "body": "Robert Whittaker (1969) classified all organisms into 5 Kingdoms based on cell structure, body organization, and mode of nutrition:\n1. Monera: Prokaryotic, Unicellular (Bacteria, Anabaena).\n2. Protista: Eukaryotic, Unicellular (Amoeba, Paramecium, Euglena).\n3. Fungi: Eukaryotic, Saprophytic, Chitin cell wall (Yeast, Mushroom, Penicillium).\n4. Plantae: Eukaryotic, Multicellular, Autotrophic with Cellulose cell wall.\n5. Animalia: Eukaryotic, Multicellular, Heterotrophic without cell wall.",
        "body_hi": "रॉबर्ट ह्विटेकर (1969) ने सभी जीवों को 5 जगतों में वर्गीकृत किया:\n1. मोनेरा (Monera): प्रोकैरियोटिक, एककोशिकीय (जीवाणु, एनाबीना)।\n2. प्रोटिस्टा (Protista): यूकैरियोटिक, एककोशिकीय (अमीबा, पैरामीशियम)।\n3. कवक (Fungi): यूकैरियोटिक, मृतजीवी, काइटिन कोशिका भित्ति (यीस्ट, मशरूम)।\n4. पादप (Plantae): यूकैरियोटिक, बहुकोशिकीय, स्वपोषी।\n5. जंतु (Animalia): यूकैरियोटिक, बहुकोशिकीय, विषमपोषी बिना कोशिका भित्ति।",
        "body_gu": "રૉબર્ટ વ્હીટેકર (1969) એ તમામ સજીવોને 5 સૃષ્ટિમાં વર્ગીકૃત કર્યા:\n1. મોનેરા (Monera): પ્રોકેરિયોટિક, એકકોષીય (બેક્ટેરિયા, એનાબીના).\n2. પ્રોટિસ્ટા (Protista): યુકેરિયોટિક, એકકોષીય (અમીબા, પેરામિશિયમ).\n3. ફૂગ (Fungi): યુકેરિયોટિક, મૃતોપજીવી, કાઇટીન કોષદિવાલ (યીસ્ટ, મશરૂમ).\n4. વનસ્પતિ (Plantae): યુકેરિયોટિક, બહુકોષીય, સ્વયંપોષી.\n5. પ્રાણી (Animalia): યુકેરિયોટિક, બહુકોષીય, વિષમપોષી કોષદિવાલ વગર."
    },

    # ── MODULE 4: PLANT & ANIMAL KINGDOM DIVISIONS ────────────────────────────
    {
        "id": "KOBJ_C9S7_MOD4_REVEAL",
        "type": "theory",
        "title": "Step 4: Reveal - Plant Divisions & Animal Phyla",
        "title_hi": "चरण 4: मुख्य अवधारणा - पादप और जंतु जगत का वर्गीकरण",
        "title_gu": "પગલું 4: મુખ્ય વિભાવના - વનસ્પતિ અને પ્રાણી સૃષ્ટિનું વર્ગીકરણ",
        "body": "Plant Kingdom:\n• Thallophyta (Algae), Bryophyta (Amphibians of plant kingdom, Moss), Pteridophyta (Ferns).\n• Gymnosperms (Naked seeds, Pinus, Cycas) & Angiosperms (Enclosed seeds in fruits, Monocots & Dicots).\n\nAnimal Phyla:\n• Porifera (Sponges), Coelenterata (Hydra, Jellyfish), Platyhelminthes (Flatworms), Nematoda (Roundworms), Annelida (Earthworm, Leech), Arthropoda (Largest phylum, jointed legs, Cockroach), Mollusca (Snail, Octopus), Echinodermata (Starfish), Chordata (Vertebrates: Pisces, Amphibia, Reptilia, Aves, Mammalia).",
        "body_hi": "पादप जगत:\n• थैलोफाइटा (शैवाल), ब्रायोफाइटा (पादप जगत के उभयचर, मॉस), टेरिडोफाइटा (फर्न)।\n• जिम्नोस्पर्म (नग्न बीजी, पाइनस) एवं एंजियोस्पर्म (आवृत्त बीजी, एकबीजपत्री व द्विबीजपत्री)।\n\nजंतु संघ:\n• पोरीफेरा (स्पंज), सीलेंट्रेटा (हाइड्रा), प्लैटीहेल्मिंथीज (चपटे कृमि), निमेटोडा (गोल कृमि), एनेलिडा (केंचुआ), अर्थ्रोपोडा (सबसे बड़ा संघ, संधिपाद), मोलस्का (घोंघा), एकाइनोडर्मेटा (स्टारफिश), कॉर्डेटा (कशेरुकी: मत्स्य, उभयचर, सरीसृप, पक्षी, स्तनधारी)।",
        "body_gu": "વનસ્પતિ સૃષ્ટિ:\n• થાલોફાઇટા (લીલ), બ્રાયોફાઇટા (વનસ્પતિ સૃષ્ટિના ઉભયજીવી, મોસ), ટેરિડોફાઇટા (હંસરાજ).\n• અનાવૃત બીજધારી (Gymnosperms, પાઇનસ) અને આવૃત બીજધારી (Angiosperms, એકદળી અને દ્વિદળી).\n\nપ્રાણી સમુદાયો:\n• છિદ્રકાય (Porifera), કોષ્ઠાંતરી (Coelenterata), પૃથુકૃમિ, સૂત્રકૃમિ, સંધિપાદ (સૌથી મોટો સમુદાય, સંધિયુક્ત ઉપાંગો), મૃદુકાય, કંટકત્વચી, પૃષ્ઠવંશી (મત્સ્ય, ઉભયજીવી, સરીસૃપ, વિહગ, સસ્તન)."
    }
]

# 14 OFFICIAL TEXTBOOK EXERCISE QUESTIONS (IN-TEXT + END-OF-CHAPTER)
textbook_exercise_questions = [
    {
        "id": "KOBJ_C9S7_EX_Q01",
        "type": "quiz",
        "title": "Textbook Exercise 1: Athlete Circular Track Motion",
        "title_hi": "पाठ्यपुस्तक अभ्यास 1: वृत्ताकार ट्रैक पर एथलीट",
        "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 1: વર્તુળાકાર ટ્રેક પર એથલિટ",
        "question": "An athlete completes one round of a circular track of diameter 200 m in 40 s. What will be the distance covered and the displacement at the end of 2 minutes 20 seconds?",
        "question_hi": "एक एथलीट 200 मीटर व्यास वाले वृत्ताकार रास्ते का एक चक्कर 40 सेकंड में लगाता है। 2 मिनट 20 सेकंड के बाद वह कितनी दूरी तय करेगा और उसका विस्थापन क्या होगा?",
        "question_gu": "એક એથલિટ 200 મીટર વ્યાસવાળા વર્તુળાકાર પથ પર એક ચક્કર 40 સેકન્ડમાં પૂરું કરે છે. 2 મિનિટ 20 સેકન્ડ બાદ તેણે કાપેલું અંતર અને સ્થાનાંતર કેટલું હશે?",
        "options": [
            "Distance = 2200 m, Displacement = 200 m",
            "Distance = 1400 m, Displacement = 0 m",
            "Distance = 4400 m, Displacement = 100 m",
            "Distance = 2000 m, Displacement = 400 m"
        ],
        "options_hi": [
            "दूरी = 2200 मीटर, विस्थापन = 200 मीटर",
            "दूरी = 1400 मीटर, विस्थापन = 0 मीटर",
            "दूरी = 4400 मीटर, विस्थापन = 100 मीटर",
            "दूरी = 2000 मीटर, विस्थापन = 400 मीटर"
        ],
        "options_gu": [
            "અંતર = 2200 મીટર, સ્થાનાંતર = 200 મીટર",
            "અંતર = 1400 મીટર, સ્થાનાંતર = 0 મીટર",
            "અંતર = 4400 મીટર, સ્થાનાંતર = 100 મીટર",
            "અંતર = 2000 મીટર, સ્થાનાંતર = 400 મીટર"
        ],
        "correct_index": 0,
        "explanation": "Total Time = 140 s. Rounds = 140 / 40 = 3.5 rounds. Distance = 3.5 × (π × d) = 3.5 × (22/7) × 200 = 2200 m. Displacement after 3.5 rounds = Diameter = 200 m.",
        "explanation_hi": "कुल समय = 140 सेकंड। चक्कर = 140 / 40 = 3.5 चक्कर। दूरी = 3.5 × (22/7) × 200 = 2200 मीटर। 3.5 चक्कर के बाद विस्थापन = व्यास = 200 मीटर।",
        "explanation_gu": "કુલ સમય = 140 સેકન્ડ. ચક્કર = 140 / 40 = 3.5 ચક્કર. અંતર = 3.5 × (22/7) × 200 = 2200 મીટર. 3.5 ચક્કર બાદ સ્થાનાંતર = વ્યાસ = 200 મીટર."
    },
    {
        "id": "KOBJ_C9S7_EX_Q03",
        "type": "quiz",
        "title": "Textbook Exercise 3: Abdul's Average Speed Calculation",
        "title_hi": "पाठ्यपुस्तक अभ्यास 3: अब्दुल की औसत चाल",
        "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 3: અબ્દુલની સરેરાશ ઝડપ",
        "question": "Abdul computes the average speed for his trip to school to be 20 km/h. On his return trip along the same route, the average speed is 30 km/h. What is the average speed for his total trip?",
        "question_hi": "अब्दुल गाड़ी से स्कूल जाने के क्रम में औसत चाल को 20 km/h पाता है। उसी रास्ते से वापस आते समय औसत चाल 30 km/h है। अब्दुल की पूरी यात्रा की औसत चाल क्या है?",
        "question_gu": "અબ્દુલ શાળાએ જતી વખતે સરેરાશ ઝડપ 20 km/h ગણે છે. તે જ રસ્તે પાછા ફરતી વખતે સરેરાશ ઝડપ 30 km/h છે. અબ્દુલની સમગ્ર મુસાફરીની સરેરાશ ઝડપ કેટલી થશે?",
        "options": [
            "24 km/h",
            "25 km/h",
            "50 km/h",
            "10 km/h"
        ],
        "options_hi": [
            "24 km/h",
            "25 km/h",
            "50 km/h",
            "10 km/h"
        ],
        "options_gu": [
            "24 km/h",
            "25 km/h",
            "50 km/h",
            "10 km/h"
        ],
        "correct_index": 0,
        "explanation": "Average Speed for equal distance = 2 × v₁ × v₂ / (v₁ + v₂) = (2 × 20 × 30) / (20 + 30) = 1200 / 50 = 24 km/h.",
        "explanation_hi": "समान दूरी के लिए औसत चाल = 2 × v₁ × v₂ / (v₁ + v₂) = (2 × 20 × 30) / (20 + 30) = 24 km/h।",
        "explanation_gu": "સમાન અંતર માટે સરેરાશ ઝડપ = 2 × v₁ × v₂ / (v₁ + v₂) = (2 × 20 × 30) / (20 + 30) = 24 km/h."
    },
    {
        "id": "KOBJ_C9S7_EX_Q04",
        "type": "quiz",
        "title": "Textbook Exercise 4: Distance Covered by Accelerating Motorboat",
        "title_hi": "पाठ्यपुस्तक अभ्यास 4: मोटरबोट द्वारा तय दूरी",
        "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 4: મોટરબોટ દ્વારા કપાયેલું અંતર",
        "question": "A motorboat starting from rest on a lake accelerates in a straight line at a constant rate of 3.0 m/s² for 8.0 s. How far does the boat travel during this time?",
        "question_hi": "झील में विरामावस्था से चलने वाली मोटरबोट 3.0 m/s² की नियत दर से 8.0 s तक सीधी रेखा में त्वरित होती है। इस समय में बोट कितनी दूरी तय करती है?",
        "question_gu": "સ્થિર સ્થિતિમાંથી શરૂ થતી મોટરબોટ 3.0 m/s² ના અચળ પ્રવેગથી 8.0 સેકન્ડ સુધી સીધી રેખામાં ગતિ કરે છે. આ સમયગાળા દરમિયાન બોટે કેટલું અંતર કાપ્યું હશે?",
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
        "explanation": "Formula: s = ut + ½ at². Here u = 0, a = 3.0 m/s², t = 8.0 s. s = 0 + ½(3.0)(8)² = 0.5 × 3 × 64 = 96 m.",
        "explanation_hi": "सूत्र: s = ut + ½ at²। यहाँ u = 0, a = 3.0, t = 8.0। s = 0 + ½(3.0)(64) = 96 मीटर।",
        "explanation_gu": "સૂત્ર: s = ut + ½ at². અહીં u = 0, a = 3.0, t = 8.0. s = 0 + ½(3.0)(64) = 96 મીટર."
    },
    {
        "id": "KOBJ_C9S7_EX_Q09",
        "type": "quiz",
        "title": "Textbook Exercise 9: Basis for Five Kingdom Classification",
        "title_hi": "पाठ्यपुस्तक अभ्यास 9: पाँच जगत वर्गीकरण का आधार",
        "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 9: પાંચ સૃષ્ટિ વર્ગીકરણનો આધાર",
        "question": "What is the primary basis for grouping organisms into Whittaker's Five Kingdoms?",
        "question_hi": "जीवों को पाँच जगतों में वर्गीकृत करने का मुख्य आधार क्या है?",
        "question_gu": "સજીવોને પાંચ સૃષ્ટિમાં વર્ગીકૃત કરવાનો મુખ્ય આધાર કયો છે?",
        "options": [
            "Cellular structure (Prokaryote/Eukaryote), Body organization, and Mode of nutrition",
            "Color of the organism only",
            "Presence of legs only",
            "Habitat location only"
        ],
        "options_hi": [
            "कोशिकीय संरचना (प्रोकैरियोटिक/यूकैरियोटिक), शारीरिक संगठन, और पोषण की विधि",
            "केवल जीव का रंग",
            "केवल पैरों की उपस्थिति",
            "केवल आवास का स्थान"
        ],
        "options_gu": [
            "કોષીય રચના (પ્રોકેરિયોટિક/યુકેરિયોટિક), શારીરિક સંગઠન, અને પોષણની પદ્ધતિ",
            "ફક્ત સજીવનો રંગ",
            "ફક્ત ઉપાંગોની હાજરી",
            "ફક્ત નિવાસસ્થાન"
        ],
        "correct_index": 0,
        "explanation": "Whittaker classified organisms into Monera, Protista, Fungi, Plantae, Animalia based on cell complexity, body complexity, and autotrophic/heterotrophic nutrition.",
        "explanation_hi": "ह्विटेकर ने कोशिका संरचना, शारीरिक जटिलता और स्वपोषी/विषमपोषी पोषण के आधार पर वर्गीकरण किया।",
        "explanation_gu": "વ્હીટેકરે કોષીય સંરચના, શારીરિક જટિલતા અને પોષણની પદ્ધતિના આધારે વર્ગીકરણ કર્યું."
    },
    {
        "id": "KOBJ_C9S7_EX_Q11",
        "type": "quiz",
        "title": "Textbook Exercise 11: Gymnosperms vs Angiosperms",
        "title_hi": "पाठ्यपुस्तक अभ्यास 11: जिम्नोस्पर्म और एंजियोस्पर्म में अंतर",
        "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 11: અનાવૃત અને આવૃત બીજધારી વચ્ચેનો તફાવત",
        "question": "How do Gymnosperms and Angiosperms differ from each other?",
        "question_hi": "जिम्नोस्पर्म (Gymnosperms) और एंजियोस्पर्म (Angiosperms) एक दूसरे से कैसे भिन्न हैं?",
        "question_gu": "અનાવૃત બીજધારી (Gymnosperms) અને આવૃત બીજધારી (Angiosperms) એકબીજાથી કેવી રીતે અલગ પડે છે?",
        "options": [
            "Gymnosperms have naked seeds without fruits; Angiosperms have seeds enclosed inside fruits",
            "Gymnosperms bear flowers and fruits",
            "Angiosperms do not produce seeds",
            "Both have identical seeds and flowers"
        ],
        "options_hi": [
            "जिम्नोस्पर्म में बिना फल के नग्न बीज होते हैं; एंजियोस्पर्म में बीज फल के अंदर ढके होते हैं",
            "जिम्नोस्पर्म में फूल और फल होते हैं",
            "एंजियोस्पर्म बीज उत्पन्न नहीं करते",
            "दोनों में समान बीज और फूल होते हैं"
        ],
        "options_gu": [
            "અનાવૃત બીજધારીમાં ફળ વગરના ખુલ્લા બીજ હોય છે; આવૃત બીજધારીમાં બીજ ફળની અંદર ઢંકાયેલા હોય છે",
            "અનાવૃત બીજધારીમાં પુષ્પો અને ફળો હોય છે",
            "આવૃત બીજધારી બીજ ઉત્પન્ન કરતા નથી",
            "બંનેમાં સમાન બીજ અને પુષ્પો હોય છે"
        ],
        "correct_index": 0,
        "explanation": "Gymno = naked, sperma = seed (Pinus, Cycas). Angio = covered/enclosed (Flowering plants, Mango, Wheat).",
        "explanation_hi": "जिम्नोस्पर्म = नग्न बीज (पाइनस)। एंजियोस्पर्म = ढके हुए बीज वाले पुष्पी पौधे (आम, गेहूं)।",
        "explanation_gu": "અનાવૃત બીજધારી = ખુલ્લા બીજ (પાઇનસ). આવૃત બીજધારી = ફળમાં ઢંકાયેલા બીજ ધરાવતી સપુષ્પી વનસ્પતિ (કેરી, ઘઉં)."
    }
]

# Combine all blocks
all_blocks = blocks + textbook_exercise_questions
print(f"Total blocks generated for Class 9 Science Ch 7: {len(all_blocks)}")

# Save to learning_modules blocks.json
blocks_path = 'app_core/learning_modules/gseb_class9_science_ch7/blocks.json'
with open(blocks_path, 'w', encoding='utf-8') as f:
    json.dump(all_blocks, f, ensure_ascii=False, indent=2)
print(f"Saved blocks to {blocks_path}")

# Sync to app_core/chapters/ncert_class9_science_ch7.json
ncert_path = 'app_core/chapters/ncert_class9_science_ch7.json'
ncert_payload = {
    "metadata": {
        "id": "ncert_class9_science_ch7",
        "title": "Chapter 7: Motion & Diversity in Living Organisms",
        "title_hi": "अध्याय 7: गति एवं जीवों में विविधता",
        "title_gu": "પ્રકરણ 7: ગતિ અને સજીવોમાં વિવિધતા",
        "subject": "Science",
        "grade": "Class 9"
    },
    "blocks": all_blocks
}
with open(ncert_path, 'w', encoding='utf-8') as f:
    json.dump(ncert_payload, f, ensure_ascii=False, indent=2)
print(f"Synced to {ncert_path}")

# Sync to assessment bank
assessment_path = 'app_core/assessment/gseb_class9_science_ch7_questions.json'
assessment_questions = []
for idx, q in enumerate(textbook_exercise_questions):
    assessment_questions.append({
        "id": f"gseb_c9_sci_ch7_q_{idx+1:03d}",
        "chapter_id": "gseb_class9_science_ch7",
        "topic_id": "motion_and_diversity",
        "type": "quiz",
        "difficulty": "medium",
        "board": "GSEB",
        "marks": 1,
        "bloom_taxonomy": "Understand",
        "keywords": ["distance", "displacement", "velocity", "equations_of_motion", "five_kingdoms", "gymnosperms"],
        "estimated_time_minutes": 2,
        "question_text": q['question'],
        "question_text_hi": q['question_hi'],
        "question_text_gu": q['question_gu'],
        "options": q['options'],
        "options_hi": q['options_hi'],
        "options_gu": q['options_gu'],
        "answer": q['options'][q['correct_index']],
        "correct_index": q['correct_index'],
        "explanation": q['explanation'],
        "explanation_hi": q['explanation_hi'],
        "explanation_gu": q['explanation_gu']
    })

assessment_payload = {
    "chapter_id": "gseb_class9_science_ch7",
    "questions": assessment_questions
}
with open(assessment_path, 'w', encoding='utf-8') as f:
    json.dump(assessment_payload, f, ensure_ascii=False, indent=2)
print(f"Updated assessment bank at {assessment_path}")
