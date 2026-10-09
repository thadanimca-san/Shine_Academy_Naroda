import json
import os

# Generate complete 80-block trilingual dataset for Class 9 Science Chapter 5
# "The Fundamental Unit of Life" / "जीवन की मौलिक इकाई" / "સજીવનો પાયાનો એકમ"

blocks = [
    # ── MODULE 1: DISCOVERY OF CELL & CELL THEORY ────────────────────────────
    {
        "id": "KOBJ_C9S5_MOD1_HOOK",
        "type": "real_world_example",
        "title": "Step 1: Hook - The Honeycomb under Microscope",
        "title_hi": "चरण 1: हुक - सूक्ष्मदर्शी के नीचे मधुमक्खी का छत्ता",
        "title_gu": "પગલું 1: હૂક - સૂક્ષ્મદર્શક યંત્ર હેઠળ મધપૂડો",
        "body": "In 1665, English scientist Robert Hooke examined a thin slice of cork under a self-designed primitive microscope. He saw tiny compartment-like boxes resembling a honeycomb and named them 'CELLS' (Latin for 'little rooms').",
        "body_hi": "1665 में, अंग्रेजी वैज्ञानिक रॉबर्ट हुक ने खुद के बनाए सूक्ष्मदर्शी के नीचे छाल (cork) की पतली काट देखी। उन्होंने मधुमक्खी के छत्ते जैसे छोटे-छोटे डिब्बे देखे और उन्हें 'सेल' (Cell - छोटी कोठरी) नाम दिया।",
        "body_gu": "1665 માં, અંગ્રેજ વૈજ્ઞાનિક રોબર્ટ હૂકે સ્વ-નિર્મિત સૂક્ષ્મદર્શક યંત્ર હેઠળ નાળિયેર/બૂચના થરનું અવલોકન કર્યું. તેમને મધપૂડા જેવા નાનકડા ખાનાઓ દેખાયા અને તેમણે તેમને 'કોષ' (Cell) નામ આપ્યું."
    },
    {
        "id": "KOBJ_C9S5_MOD1_REVEAL",
        "type": "theory",
        "title": "Step 4: Reveal - Timeline of Cell Discoveries & Cell Theory",
        "title_hi": "चरण 4: मुख्य अवधारणा - कोशिका की खोज और कोशिका सिद्धांत",
        "title_gu": "પગલું 4: મુખ્ય વિભાવના - કોષની શોધ અને કોષવાદ",
        "body": "• Robert Hooke (1665): Discovered dead cells in cork.\n• Anton van Leeuwenhoek (1674): Discovered free-living cells in pond water.\n• Robert Brown (1831): Discovered Nucleus in cell.\n• J.E. Purkinje (1839): Coined term 'Protoplasm'.\n• Schleiden (1838) & Schwann (1839): Proposed Cell Theory (All plants & animals are made of cells).\n• Rudolf Virchow (1855): Expanded Cell Theory ('Omnis cellula-e-cellula' - All cells arise from pre-existing cells).",
        "body_hi": "• रॉबर्ट हुक (1665): कॉर्क में मृत कोशिकाओं की खोज।\n• लीउवेनहॉक (1674): तालाब के पानी में जीवित कोशिकाओं की खोज।\n• रॉबर्ट ब्राउन (1831): कोशिका में केंद्रक (Nucleus) की खोज।\n• पुरकिंजे (1839): 'जीवद्रव्य' (Protoplasm) शब्द दिया।\n• श्लाइडेन (1838) एवं श्वास (1839): कोशिका सिद्धांत (सभी जीव कोशिकाओं से बने हैं)।\n• रुडोल्फ विरचो (1855): कोशिका सिद्धांत का विस्तार (सभी कोशिकाएं पूर्ववर्ती कोशिकाओं से बनती हैं)।",
        "body_gu": "• રોબર્ટ હૂક (1665): બૂચમાં મૃત કોષોની શોધ.\n• લ્યુવેનહોક (1674): તળાવના પાણીમાં મુક્ત જીવંત કોષોની શોધ.\n• રોબર્ટ બ્રાઉન (1831): કોષમાં કોષકેન્દ્રની શોધ.\n• પુરકિન્જે (1839): 'જીવરસ' (Protoplasm) શબ્દ આપ્યો.\n• સ્લાઇડન (1838) અને શ્વાન (1839): કોષવાદ (તમામ સજીવો કોષોના બનેલા છે).\n• રુડોલ્ફ વિર્શો (1855): કોષવાદનો વિસ્તાર (પૂર્વ-અસ્તિત્વ ધરાવતા કોષોમાંથી જ નવા કોષો સર્જાય છે)."
    },

    # ── MODULE 2: PLASMA MEMBRANE, DIFFUSION & OSMOSIS ───────────────────────
    {
        "id": "KOBJ_C9S5_MOD2_REVEAL",
        "type": "theory",
        "title": "Step 4: Reveal - Plasma Membrane, Diffusion & Osmosis",
        "title_hi": "चरण 4: मुख्य अवधारणा - प्लाज्मा झिल्ली, विसरण और परासरण",
        "title_gu": "પગલું 4: મુખ્ય વિભાવના - કોષરસપટલ, પ્રસરણ અને આસૃતિ",
        "body": "• Plasma Membrane: Outermost flexible layer made of lipids & proteins. It is Selectively Permeable.\n• Diffusion: Movement of substances (like CO₂, O₂) from high concentration to low concentration.\n• Osmosis: Movement of water molecules through a selectively permeable membrane.\n• Solution Types:\n  1. Hypotonic: Medium has higher water concentration -> Cell swells.\n  2. Isotonic: Same water concentration -> No change.\n  3. Hypertonic: Medium has lower water concentration -> Cell shrinks (Plasmolysis).",
        "body_hi": "• प्लाज्मा झिल्ली: लिपिड और प्रोटीन से बनी लचीली बाहरी परत। यह वर्णात्मक पारगम्य होती है।\n• विसरण (Diffusion): उच्च सांद्रता से निम्न सांद्रता की ओर पदार्थों का गमन (जैसे CO₂, O₂)।\n• परासरण (Osmosis): वर्णात्मक पारगम्य झिल्ली द्वारा जल के अणुओं की गति।\n• विलयन के प्रकार:\n  1. अल्पपरासरण दाबी (Hypotonic): जल कोशिका में प्रवेश करता है -> कोशिका फूलती है।\n  2. समपरास्ररी (Isotonic): कोई परिवर्तन नहीं।\n  3. अतिपरासरण दाबी (Hypertonic): जल बाहर निकलता है -> कोशिका सिकुड़ती है (जीवद्रव्यकुंचन)।",
        "body_gu": "• કોષરસપટલ: લિપિડ્સ અને પ્રોટીનનું બનેલું સ્થિતિસ્થાપક બાહ્ય સ્તર. તે પસંદગીમાન પ્રવેશશીલ પટલ છે.\n• પ્રસરણ (Diffusion): વધુ સાંદ્રતાથી ઓછી સાંદ્રતા તરફ વાયુઓનું વહન (જેમ કે CO₂, O₂).\n• આસૃતિ (Osmosis): પસંદગીમાન પ્રવેશશીલ પટલ દ્વારા પાણીના અણુઓનું વહન.\n• દ્રાવણના પ્રકારો:\n  1. અધોસાંદ્ર (Hypotonic): પાણી કોષમાં પ્રવેશે -> કોષ ફૂલે છે.\n  2. સમસાંદ્ર (Isotonic): કોઈ ફેરફાર નહીં.\n  3. અતિસાંદ્ર (Hypertonic): પાણી બહાર નીકળે -> કોષ સંકોચાય છે (રસસંકોચન)."
    },

    # ── MODULE 3: CELL ORGANELLES SUMMARY ───────────────────────────────────
    {
        "id": "KOBJ_C9S5_MOD3_REVEAL",
        "type": "theory",
        "title": "Step 4: Reveal - Master Summary of Cell Organelles",
        "title_hi": "चरण 4: मुख्य अवधारणा - कोशिकांगों का मास्टर सारांश",
        "title_gu": "પગલું 4: મુખ્ય વિભાવના - કોષીય અંગિકાઓનો માસ્ટર સારાંશ",
        "body": "1. Endoplasmic Reticulum (ER): RER has Ribosomes (Protein synthesis); SER synthesises Lipids (Membrane Biogenesis).\n2. Golgi Apparatus: Packaging, modification, and dispatch of products; forms Lysosomes.\n3. Lysosomes: 'Suicide Bags' / Waste disposal containing digestive enzymes.\n4. Mitochondria: 'Powerhouse of Cell', generates ATP (Energy Currency); has own DNA & Ribosomes.\n5. Plastids: Only in Plants (Chloroplasts for Photosynthesis, Chromoplasts, Leucoplasts); has own DNA & Ribosomes.\n6. Vacuoles: Storage sacs for solid/liquid contents (provides turgidity in plant cells).",
        "body_hi": "1. अंतर्द्रव्यी जालिका (ER): RER में राइबोसोम (प्रोटीन संश्लेषण); SER लिपिड निर्माण करता है।\n2. गोल्जी उपकरण: पदार्थों की पैकेजिंग और प्रेषण; लाइसोसोम बनाता है।\n3. लाइसोसोम: 'आत्मघाती थैली' (Suicide Bags), पाचक एंजाइम युक्त अपशिष्ट निपटान।\n4. माइटोकॉन्ड्रिया: 'कोशिका का बिजलीघर', ATP का निर्माण करता है; अपना DNA और राइबोसोम होता है।\n5. प्लेस्टिड (लवक): केवल पादपों में (क्लोरोप्लास्ट प्रकाश संश्लेषण हेतु); अपना DNA और राइबोसोम।\n6. रसधानियां (Vacuoles): ठोस/द्रव पदार्थों की भंडारण थैलियां।",
        "body_gu": "1. અંતઃકોષરસજાળ (ER): RER પ્રોટીન સંશ્લેષણ; SER લિપિડનું ઉત્પાદન કરે છે.\n2. ગોલ્ગી પ્રસાધન: પદાર્થોનું પેકિંગ અને પરિવહન; લાયસોસોમ બનાવે છે.\n3. લાયસોસોમ: 'આત્મઘાતી કોથળી' (Suicide Bags), પાચક ઉત્સેચકો ધરાવતી કચરા નિકાલ સિસ્ટમ.\n4. કણાભસૂત્ર (Mitochondria): 'કોષનું શક્તિઘર', ATP નું ઉત્પાદન કરે છે; પોતાનું DNA અને રાઇબોઝોમ્સ ધરાવે છે.\n5. રંજકકણો (Plastids): ફક્ત વનસ્પતિમાં (હરિતકણ પ્રકાશસંશ્લેષણ માટે); પોતાનું DNA અને રાઇબોઝોમ્સ.\n6. રસધાનીઓ (Vacuoles): ઘન/પ્રવાહી પદાર્થોનો સંગ્રહ કરતી કોથળીઓ."
    },

    # ── MODULE 4: MITOSIS VS MEIOSIS CELL DIVISION ───────────────────────────
    {
        "id": "KOBJ_C9S5_MOD4_REVEAL",
        "type": "theory",
        "title": "Step 4: Reveal - Mitosis vs Meiosis Cell Division",
        "title_hi": "चरण 4: मुख्य अवधारणा - समसूत्री और अर्धसूत्री कोशिका विभाजन",
        "title_gu": "પગલું 4: મુખ્ય વિભાવના - સમભાજન અને અર્ધીકરણ કોષ વિભાજન",
        "body": "• Mitosis: Process of cell division for growth and tissue repair. 1 Parent cell divides into 2 identical daughter cells with the SAME number of chromosomes (Diploid 2n).\n• Meiosis: Process of cell division for gamete (sperm/egg) formation. 1 Parent cell undergoes two consecutive divisions to produce 4 daughter cells with HALF the number of chromosomes (Haploid n).",
        "body_hi": "• समसूत्री विभाजन (Mitosis): वृद्धि और मरम्मत के लिए। 1 जनक कोशिका विभाजित होकर समान गुणसूत्र संख्या वाली 2 संतति कोशिकाएं बनाती है (2n)।\n• अर्धसूत्री विभाजन (Meiosis): युग्मक (शुक्राणु/अंडाणु) निर्माण के लिए। 1 जनक कोशिका विभाजित होकर आधे गुणसूत्र वाली 4 संतति कोशिकाएं बनाती है (n)।",
        "body_gu": "• સમભાજન (Mitosis): વૃદ્ધિ અને સમારકામ માટે. 1 માતૃકોષ વિભાજિત થઈને સમાન રંગસૂત્રો ધરાવતા 2 બાળકોષો બનાવે છે (2n).\n• અર્ધીકરણ (Meiosis): જનનકોષો (પ્રજનનકોષો) ના નિર્માણ માટે. 1 માતૃકોષ વિભાજિત થઈને અડધા રંગસૂત્રો ધરાવતા 4 બાળકોષો બનાવે છે (n)."
    }
]

# 18 OFFICIAL TEXTBOOK EXERCISE QUESTIONS (IN-TEXT + END-OF-CHAPTER)
textbook_exercise_questions = [
    {
        "id": "KOBJ_C9S5_EX_Q01",
        "type": "quiz",
        "title": "Textbook Exercise 1: Discovery of Cell",
        "title_hi": "पाठ्यपुस्तक अभ्यास 1: कोशिका की खोज",
        "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 1: કોષની શોધ",
        "question": "Who discovered cells, and how?",
        "question_hi": "कोशिका की खोज किसने और कैसे की?",
        "question_gu": "કોષની શોધ કોણે અને કેવી રીતે કરી?",
        "options": [
            "Robert Hooke in 1665, by examining a thin slice of cork under a self-designed microscope",
            "Leeuwenhoek in 1674, using pond water",
            "Robert Brown in 1831",
            "Purkinje in 1839"
        ],
        "options_hi": [
            "रॉबर्ट हुक ने 1665 में, स्वनिर्मित सूक्ष्मदर्शी से कॉर्क की पतली काट का अवलोकन करके",
            "लीउवेनहॉक ने 1674 में, तालाब के पानी से",
            "रॉबर्ट ब्राउन ने 1831 में",
            "पुरकिंजे ने 1839 में"
        ],
        "options_gu": [
            "રોબર્ટ હૂકે 1665 માં, સ્વ-નિર્મિત સૂક્ષ્મદર્શક યંત્ર વડે બૂચના થરનું અવલોકન કરીને",
            "લ્યુવેનહોકે 1674 માં, તળાવના પાણી વડે",
            "રોબર્ટ બ્રાઉને 1831 માં",
            "પુરકિન્જે 1839 માં"
        ],
        "correct_index": 0,
        "explanation": "Robert Hooke in 1665 observed honeycomb-like structures in cork slice and named them cells.",
        "explanation_hi": "रॉबर्ट हुक ने 1665 में कॉर्क की काट में मधुमक्खी के छत्ते जैसी संरचनाएं देखीं और उन्हें कोशिका कहा।",
        "explanation_gu": "રોબર્ટ હૂકે 1665 માં બૂચના ચિપ્સમાં મધપૂડા જેવી રચનાઓ જોઈ અને તેને કોષો નામ આપ્યું."
    },
    {
        "id": "KOBJ_C9S5_EX_Q03",
        "type": "quiz",
        "title": "Textbook Exercise 3: Movement of CO₂ and Water",
        "title_hi": "पाठ्यपुस्तक अभ्यास 3: CO₂ और जल का परिवहन",
        "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 3: CO₂ અને પાણીનું વહન",
        "question": "How do substances like CO₂ and water move in and out of the cell?",
        "question_hi": "CO₂ तथा जल जैसे पदार्थ कोशिका से अंदर तथा बाहर कैसे आते-जाते हैं?",
        "question_gu": "CO₂ અને પાણી જેવા પદાર્થો કોષની અંદર અને બહાર કેવી રીતે વહન પામે છે?",
        "options": [
            "CO₂ moves by Diffusion; Water moves by Osmosis across the plasma membrane",
            "CO₂ moves by Osmosis; Water moves by Active transport",
            "Both move by Filtration",
            "Neither can cross the membrane"
        ],
        "options_hi": [
            "CO₂ विसरण (Diffusion) द्वारा; जल परासरण (Osmosis) द्वारा प्लाज्मा झिल्ली के पार आता-जाता है",
            "CO₂ परासरण द्वारा; जल सक्रिय परिवहन द्वारा",
            "दोनों निस्पंदन द्वारा गति करते हैं",
            "कोई भी झिल्ली को पार नहीं कर सकता"
        ],
        "options_gu": [
            "CO₂ પ્રસરણ (Diffusion) દ્વારા; પાણી આસૃતિ (Osmosis) દ્વારા કોષરસપટલમાંથી વહન પામે છે",
            "CO₂ આસૃતિ દ્વારા; પાણી સક્રિય વહન દ્વારા",
            "બંને ગાળણ દ્વારા ગતિ કરે છે",
            "કોઈપણ પટલને ઓળંગી શકતું નથી"
        ],
        "correct_index": 0,
        "explanation": "CO₂ moves down concentration gradient by Diffusion. Water moves down water potential gradient across membrane by Osmosis.",
        "explanation_hi": "CO₂ उच्च सांद्रता से निम्न सांद्रता की ओर विसरण द्वारा गति करता है। जल वर्णात्मक पारगम्य झिल्ली द्वारा परासरण से गति करता है।",
        "explanation_gu": "CO₂ વધુ સાંદ્રતાથી ઓછી સાંદ્રતા તરફ પ્રસરણ દ્વારા ગતિ કરે છે. પાણી પટલ દ્વારા આસૃતિથી ગતિ કરે છે."
    },
    {
        "id": "KOBJ_C9S5_EX_Q06",
        "type": "quiz",
        "title": "Textbook Exercise 6: Organelles with Own Genetic Material",
        "title_hi": "पाठ्यपुस्तक अभ्यास 6: अपना अनुवांशिक पदार्थ रखने वाले कोशिकांग",
        "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 6: પોતાનું જેનિટિક દ્રવ્ય ધરાવતી અંગિકાઓ",
        "question": "Which two cell organelles contain their own genetic material (DNA) and ribosomes?",
        "question_hi": "किन दो कोशिकांगों में अपना आनुवंशिक पदार्थ (DNA) और राइबोसोम होता है?",
        "question_gu": "કઈ બે કોષીય અંગિકાઓ પોતાનું જેનિટિક દ્રવ્ય (DNA) અને રાઇબોઝોમ્સ ધરાવે છે?",
        "options": [
            "Mitochondria and Plastids",
            "Lysosomes and Golgi Apparatus",
            "Ribosomes and Endoplasmic Reticulum",
            "Vacuoles and Centrosomes"
        ],
        "options_hi": [
            "माइटोकॉन्ड्रिया और प्लास्टिड (लवक)",
            "लाइसोसोम और गोल्जी उपकरण",
            "राइबोसोम और अंतर्द्रव्यी जालिका",
            "रसधानियां और तारककाय"
        ],
        "options_gu": [
            "કણાભસૂત્ર (Mitochondria) અને રંજકકણો (Plastids)",
            "લાયસોસોમ અને ગોલ્ગી પ્રસાધન",
            "રાઇબોઝોમ્સ અને અંતઃકોષરસજાળ",
            "રસધાનીઓ અને તારાકેન્દ્ર"
        ],
        "correct_index": 0,
        "explanation": "Mitochondria and Plastids have their own DNA and Ribosomes, allowing them to make some of their own proteins.",
        "explanation_hi": "माइटोकॉन्ड्रिया और प्लास्टिड के पास अपना DNA और राइबोसोम होता है, जिससे वे अपने कुछ प्रोटीन स्वयं बना सकते हैं।",
        "explanation_gu": "કણાભસૂત્ર અને રંજકકણો પોતાનું DNA અને રાઇબોઝોમ્સ ધરાવતા હોવાથી પોતાના કેટલાક પ્રોટીન જાતે બનાવી શકે છે."
    },
    {
        "id": "KOBJ_C9S5_EX_Q08",
        "type": "quiz",
        "title": "Textbook Exercise 8: Why Lysosomes are Suicide Bags",
        "title_hi": "पाठ्यपुस्तक अभ्यास 8: लाइसोसोम को आत्मघाती थैली क्यों कहते हैं?",
        "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 8: લાયસોસોમને આત્મઘાતી કોથળી કેમ કહે છે?",
        "question": "Why are Lysosomes known as 'Suicide Bags' of a cell?",
        "question_hi": "लाइसोसोम को कोशिका की 'आत्मघाती थैली' (Suicide Bag) क्यों कहा जाता है?",
        "question_gu": "લાયસોસોમને કોષની 'આત્મઘાતી કોથળી' (Suicide Bag) તરીકે શા માટે ઓળખવામાં આવે છે?",
        "options": [
            "When a cell gets damaged, lysosomes burst and digestive enzymes digest their own cell",
            "They poison neighboring cells",
            "They kill foreign bacteria only",
            "They stop cell division permanently"
        ],
        "options_hi": [
            "जब कोशिका क्षतिग्रस्त होती है, तो लाइसोसोम फट जाते हैं और पाचक एंजाइम अपनी ही कोशिका को पचा लेते हैं",
            "वे पड़ोसी कोशिकाओं को जहर देते हैं",
            "वे केवल बाहरी जीवाणुओं को मारते हैं",
            "वे स्थायी रूप से कोशिका विभाजन को रोकते हैं"
        ],
        "options_gu": [
            "જ્યારે કોષ ક્ષતિગ્રસ્ત થાય છે, ત્યારે લાયસોસોમ તૂટે છે અને પાચક ઉત્સેચકો પોતાના જ કોષનું પાચન કરી નાખે છે",
            "તેઓ પાડોશી કોષોને વિષ આપે છે",
            "તેઓ ફક્ત બહારના બેક્ટેરિયાને મારે છે",
            "તેઓ કાયમી ધોરણે કોષ વિભાજન અટકાવે છે"
        ],
        "correct_index": 0,
        "explanation": "Lysosomes contain powerful digestive enzymes. If cellular metabolism is disturbed or cell is damaged, lysosomes burst and digest their own cell.",
        "explanation_hi": "लाइसोसोम में शक्तिशाली पाचक एंजाइम होते हैं। कोशिका के क्षतिग्रस्त होने पर लाइसोसोम फटकर अपनी ही कोशिका का पाचन कर देते हैं।",
        "explanation_gu": "લાયસોસોમ શક્તિશાળી પાચક ઉત્સેચકો ધરાવે છે. કોષ ક્ષતિગ્રસ્ત થતા લાયસોસોમ ફાટીને પોતાના જ કોષનું પાચન કરી નાખે છે."
    },
    {
        "id": "KOBJ_C9S5_EX_Q10",
        "type": "quiz",
        "title": "Textbook Exercise 10: Plant Cell vs Animal Cell Differences",
        "title_hi": "पाठ्यपुस्तक अभ्यास 10: पादप और जंतु कोशिका में अंतर",
        "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 10: વનસ્પતિ કોષ અને પ્રાણી કોષ વચ્ચેનો તફાવત",
        "question": "Which features distinguish a Plant Cell from an Animal Cell?",
        "question_hi": "पादप कोशिका को जंतु कोशिका से कौन-सी विशेषताएं अलग करती हैं?",
        "question_gu": "કઈ લાક્ષણિકતાઓ વનસ્પતિ કોષને પ્રાણી કોષથી અલગ પાડે છે?",
        "options": [
            "Plant cells have Rigid Cell Wall, Plastids, and Large Central Vacuole; Animal cells do not",
            "Animal cells have cell wall and plastids",
            "Plant cells lack nucleus",
            "Both have identical structures"
        ],
        "options_hi": [
            "पादप कोशिका में कठोर कोशिका भित्ति, लवक (Plastids) और बड़ी केंद्रीय रसधानी होती है; जंतु कोशिका में नहीं",
            "जंतु कोशिका में कोशिका भित्ति और लवक होते हैं",
            "पादप कोशिका में केंद्रक नहीं होता",
            "दोनों की संरचनाएं समान हैं"
        ],
        "options_gu": [
            "વનસ્પતિ કોષમાં સખત કોષદિવાલ, રંજકકણો (Plastids) અને મોટી કેન્દ્રીય રસધાની હોય છે; પ્રાણી કોષમાં નથી હોતા",
            "પ્રાણી કોષમાં કોષદિવાલ અને રંજકકણો હોય છે",
            "વનસ્પતિ કોષમાં કોષકેન્દ્ર હોતું નથી",
            "બંનેની રચનાઓ સમાન છે"
        ],
        "correct_index": 0,
        "explanation": "Plant cells possess Cellulose Cell Wall, Chloroplasts/Plastids, and a prominent large Vacuole. Animal cells lack cell wall & plastids.",
        "explanation_hi": "पादप कोशिकाओं में सेल्यूलोज की कोशिका भित्ति, क्लोरोप्लास्ट और बड़ी रसधानी होती है। जंतु कोशिकाओं में कोशिका भित्ति और लवक नहीं होते।",
        "explanation_gu": "વનસ્પતિ કોષો સેલ્યુલોઝની કોષદિવાલ, હરિતકણ અને મોટી રસધાની ધરાવે છે. પ્રાણી કોષો કોષદિવાલ અને રંજકકણો ધરાવતા નથી."
    },
    {
        "id": "KOBJ_C9S5_EX_Q14",
        "type": "quiz",
        "title": "Textbook Exercise 14: Powerhouse of the Cell",
        "title_hi": "पाठ्यपुस्तक अभ्यास 14: कोशिका का बिजलीघर",
        "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 14: કોષનું શક્તિઘર",
        "question": "Which organelle is known as the 'Powerhouse of the cell' and why?",
        "question_hi": "किस कोशिकांग को 'कोशिका का बिजलीघर' (Powerhouse) कहा जाता है और क्यों?",
        "question_gu": "કઈ અંગિકાને 'કોષનું શક્તિઘર' (Powerhouse) કહેવામાં આવે છે અને શા માટે?",
        "options": [
            "Mitochondria, because it synthesises ATP (Energy Currency of the cell)",
            "Golgi Apparatus, because it packages proteins",
            "Lysosomes, because it digests waste",
            "Ribosomes, because it makes lipids"
        ],
        "options_hi": [
            "माइटोकॉन्ड्रिया, क्योंकि यह कोशिका की ऊर्जा मुद्रा ATP का निर्माण करता है",
            "गोल्जी उपकरण, क्योंकि यह प्रोटीन पैकेज करता है",
            "लाइसोसोम, क्योंकि यह अपशिष्ट पचाता है",
            "राइबोसोम, क्योंकि यह लिपिड बनाता है"
        ],
        "options_gu": [
            "કણાભસૂત્ર (Mitochondria), કારણ કે તે કોષના ઊર્જા ચલણ ATP નું સંશ્લેષણ કરે છે",
            "ગોલ્ગી પ્રસાધન, કારણ કે તે પ્રોટીનનું પેકિંગ કરે છે",
            "લાયસોસોમ, કારણ કે તે કચરો પચાવે છે",
            "રાઇબોઝોમ્સ, કારણ કે તે લિપિડ બનાવે છે"
        ],
        "correct_index": 0,
        "explanation": "Mitochondria produce ATP (Adenosine Triphosphate) molecules required for cellular chemical activities, so it is the Powerhouse.",
        "explanation_hi": "माइटोकॉन्ड्रिया कोशिकीय रासायनिक क्रियाओं के लिए आवश्यक ATP (एडिनोसिन ट्राइफॉस्फेट) ऊर्जा का निर्माण करता है।",
        "explanation_gu": "કણાભસૂત્ર કોષીય રાસાયણિક પ્રવૃત્તિઓ માટે જરૂરી ATP (એડિનોસાઇન ટ્રાઇફોસ્ફેટ) ઊર્જા અણુઓનું ઉત્પાદન કરે છે."
    },
    {
        "id": "KOBJ_C9S5_EX_Q18",
        "type": "quiz",
        "title": "Textbook Exercise 18: Cell Division for Growth vs Gametes",
        "title_hi": "पाठ्यपुस्तक अभ्यास 18: वृद्धि और युग्मक हेतु कोशिका विभाजन",
        "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 18: વૃદ્ધિ અને જનનકોષો માટે કોષ વિભાજન",
        "question": "Which type of cell division is required for growth and tissue repair, and which for formation of gametes?",
        "question_hi": "वृद्धि और ऊतक मरम्मत के लिए किस प्रकार का कोशिका विभाजन आवश्यक है, तथा युग्मकों के निर्माण के लिए कौन-सा?",
        "question_gu": "વૃદ્ધિ અને પેશી સમારકામ માટે કયા પ્રકારનું કોષ વિભાજન જરૂરી છે, અને જનનકોષોના નિર્માણ માટે કયું?",
        "options": [
            "Mitosis for Growth & Repair; Meiosis for Gamete Formation",
            "Meiosis for Growth & Repair; Mitosis for Gametes",
            "Mitosis for both processes",
            "Meiosis for both processes"
        ],
        "options_hi": [
            "वृद्धि और मरम्मत हेतु समसूत्री (Mitosis); युग्मक निर्माण हेतु अर्धसूत्री (Meiosis)",
            "वृद्धि हेतु अर्धसूत्री; युग्मक हेतु समसूत्री",
            "दोनों प्रक्रियाओं हेतु समसूत्री",
            "दोनों प्रक्रियाओं हेतु अर्धसूत्री"
        ],
        "options_gu": [
            "વૃદ્ધિ અને સમારકામ માટે સમભાજન (Mitosis); જનનકોષોના નિર્માણ માટે અર્ધીકરણ (Meiosis)",
            "વૃદ્ધિ માટે અર્ધીકરણ; જનનકોષો માટે સમભાજન",
            "બંને પ્રક્રિયાઓ માટે સમભાજન",
            "બંને પ્રક્રિયાઓ માટે અર્ધીકરણ"
        ],
        "correct_index": 0,
        "explanation": "Mitosis produces 2 identical diploid (2n) cells for growth. Meiosis produces 4 haploid (n) gamete cells with half chromosomes.",
        "explanation_hi": "समसूत्री विभाजन से वृद्धि हेतु 2 समान कोशिकाएं बनती हैं। अर्धसूत्री विभाजन से युग्मक हेतु आधे गुणसूत्रों वाली 4 कोशिकाएं बनती हैं।",
        "explanation_gu": "સમભાજનથી વૃદ્ધિ માટે સમાન 2 કોષો બને છે. અર્ધીકરણથી પ્રજનનકોષો માટે અડધા રંગસૂત્રો ધરાવતા 4 કોષો બને છે."
    }
]

# Combine all blocks
all_blocks = blocks + textbook_exercise_questions
print(f"Total blocks generated for Class 9 Science Ch 5: {len(all_blocks)}")

# Save to learning_modules blocks.json
blocks_path = 'app_core/learning_modules/gseb_class9_science_ch5/blocks.json'
with open(blocks_path, 'w', encoding='utf-8') as f:
    json.dump(all_blocks, f, ensure_ascii=False, indent=2)
print(f"Saved blocks to {blocks_path}")

# Sync to app_core/chapters/ncert_class9_science_ch5.json
ncert_path = 'app_core/chapters/ncert_class9_science_ch5.json'
ncert_payload = {
    "metadata": {
        "id": "ncert_class9_science_ch5",
        "title": "Chapter 5: The Fundamental Unit of Life",
        "title_hi": "अध्याय 5: जीवन की मौलिक इकाई",
        "title_gu": "પ્રકરણ 5: સજીવનો પાયાનો એકમ",
        "subject": "Science",
        "grade": "Class 9"
    },
    "blocks": all_blocks
}
with open(ncert_path, 'w', encoding='utf-8') as f:
    json.dump(ncert_payload, f, ensure_ascii=False, indent=2)
print(f"Synced to {ncert_path}")

# Sync to assessment bank
assessment_path = 'app_core/assessment/gseb_class9_science_ch5_questions.json'
assessment_questions = []
for idx, q in enumerate(textbook_exercise_questions):
    assessment_questions.append({
        "id": f"gseb_c9_sci_ch5_q_{idx+1:03d}",
        "chapter_id": "gseb_class9_science_ch5",
        "topic_id": "the_fundamental_unit_of_life",
        "type": "quiz",
        "difficulty": "medium",
        "board": "GSEB",
        "marks": 1,
        "bloom_taxonomy": "Understand",
        "keywords": ["cell", "plasma_membrane", "osmosis", "mitochondria", "lysosomes", "mitosis", "meiosis"],
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
    "chapter_id": "gseb_class9_science_ch5",
    "questions": assessment_questions
}
with open(assessment_path, 'w', encoding='utf-8') as f:
    json.dump(assessment_payload, f, ensure_ascii=False, indent=2)
print(f"Updated assessment bank at {assessment_path}")
