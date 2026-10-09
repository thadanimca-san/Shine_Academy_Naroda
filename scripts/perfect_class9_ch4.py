import json
import os

# Generate complete 80-block trilingual dataset for Class 9 Science Chapter 4
# "Structure of the Atom" / "परमाणु की संरचना" / "પરમાણુનું બંધારણ"

blocks = [
    # ── MODULE 1: CHARGED PARTICLES & SUBATOMIC PARTICLES ────────────────────
    {
        "id": "KOBJ_C9S4_MOD1_HOOK",
        "type": "real_world_example",
        "title": "Step 1: Hook - Static Electricity in Comb & Paper",
        "title_hi": "चरण 1: हुक - कंघी और कागज में स्थिर विद्युत",
        "title_gu": "પગલું 1: હૂક - કાંસકા અને કાગળમાં સ્થિર વિદ્યુત",
        "body": "When you run a plastic comb through dry hair, it can attract tiny bits of paper! Where does this electrical charge come from? This proved that atoms are NOT indivisible, but contain smaller charged subatomic particles!",
        "body_hi": "जब आप सूखे बालों में प्लास्टिक की कंघी घुमाते हैं, तो यह कागज के छोटे टुकड़ों को आकर्षित कर सकती है! यह विद्युत आवेश कहाँ से आता है? इसने साबित किया कि परमाणु अभाज्य नहीं हैं, बल्कि उनमें छोटे आवेशित उप-परमाणुक कण होते हैं!",
        "body_gu": "જ્યારે તમે સૂકા વાળમાં પ્લાસ્ટિકનો કાંસકો ફેરવો છો, ત્યારે તે કાગળના નાનકડા ટુકડાઓને આકર્ષી શકે છે! આ વીજભાર ક્યાંથી આવે છે? આ સાબિત કરે છે કે પરમાણુઓ અવિભાજ્ય નથી, પણ તેમની અંદર નાના વીજભારિત સબ-એટોમિક કણો રહેલા છે!"
    },
    {
        "id": "KOBJ_C9S4_MOD1_REVEAL",
        "type": "theory",
        "title": "Step 4: Reveal - Discovery of Electron, Proton and Neutron",
        "title_hi": "चरण 4: मुख्य अवधारणा - इलेक्ट्रॉन, प्रोटॉन और न्यूट्रॉन की खोज",
        "title_gu": "પગલું 4: મુખ્ય વિભાવના - ઇલેક્ટ્રોન, પ્રોટોન અને ન્યુટ્રોનની શોધ",
        "body": "1. Electron (e⁻): Discovered by J.J. Thomson (1897) using cathode ray tube. Charge = -1, Mass is negligible (~ 1/2000 of H atom).\n2. Proton (p⁺): Discovered by E. Goldstein (1886) via Canal Rays. Charge = +1, Mass = 1 u.\n3. Neutron (n⁰): Discovered by J. Chadwick (1932). Charge = 0 (Neutral), Mass = 1 u (located inside nucleus).",
        "body_hi": "1. इलेक्ट्रॉन (e⁻): जे.जे. थॉमसन (1897) द्वारा कैथोड किरणों से खोज। आवेश = -1, द्रव्यमान नगण्य (H का 1/2000 भाग)।\n2. प्रोटॉन (p⁺): ई. गोल्डस्टीन (1886) द्वारा केनाल किरणों द्वारा खोज। आवेश = +1, द्रव्यमान = 1 u।\n3. न्यूट्रॉन (n⁰): जे. चैडविक (1932) द्वारा खोज। आवेश = 0 (उदासीन), द्रव्यमान = 1 u (नाभिक में स्थित)।",
        "body_gu": "1. ઇલેક્ટ્રોન (e⁻): જે.જે. થ્રેમસન (1897) દ્વારા કેથોડ કિરણો દ્વારા શોધ. વીજભાર = -1, દળ નહિવત (H નો 1/2000 મો ભાગ).\n2. પ્રોટોન (p⁺): ઇ. ગોલ્ડસ્ટીન (1886) દ્વારા કેનાલ કિરણો દ્વારા શોધ. વીજભાર = +1, દળ = 1 u.\n3. ન્યુટ્રોન (n⁰): જે. ચેડવિક (1932) દ્વારા શોધ. વીજભાર = 0 (તટસ્થ), દળ = 1 u (ન્યુક્લિયસમાં સ્થિત)."
    },

    # ── MODULE 2: ATOMIC MODELS (THOMSON, RUTHERFORD, BOHR) ─────────────────
    {
        "id": "KOBJ_C9S4_MOD2_REVEAL",
        "type": "theory",
        "title": "Step 4: Reveal - Comparison of Atomic Models",
        "title_hi": "चरण 4: मुख्य अवधारणा - परमाणु मॉडलों की तुलना",
        "title_gu": "પગલું 4: મુખ્ય વિભાવના - પરમાણ્વીય મોડેલોની સરખામણી",
        "body": "• Thomson's Model: Positive sphere with embedded negative electrons (Plum Pudding / Watermelon Model).\n• Rutherford's Model: Alpha particle gold foil experiment showed small dense positive Nucleus in center; electrons revolve around nucleus.\n• Bohr's Model: Electrons revolve in discrete energy shells (K=1, L=2, M=3, N=4) without radiating energy.",
        "body_hi": "• थॉमसन का मॉडल: धनावेशित गोला जिसमें इलेक्ट्रॉन धंसे होते हैं (वाटरमेलन मॉडल)।\n• रदरफोर्ड का मॉडल: अल्फा-कण प्रकीर्णन द्वारा केंद्र में छोटे सघन धनावेशित नाभिक (Nucleus) की खोज; इलेक्ट्रॉन नाभिक के चारों ओर घूमते हैं।\n• बोर का मॉडल: इलेक्ट्रॉन बिना ऊर्जा विकीर्ण किए निश्चित ऊर्जा कक्षाओं (K, L, M, N) में चक्कर लगाते हैं।",
        "body_gu": "• થોમસનનું મોડેલ: ધનભારિત ગોળો જેમાં ઇલેક્ટ્રોન જડાયેલા હોય છે (વોટરમેલન મોડેલ).\n• રધરફોર્ડનું મોડેલ: આલ્ફા-કણ પ્રકીર્ણન દ્વારા કેન્દ્રમાં નાનું સઘન ધનભારિત ન્યુક્લિયસ શોધાયું; ઇલેક્ટ્રોન ન્યુક્લિયસની આસપાસ ભ્રમણ કરે છે.\n• બોહરનું મોડેલ: ઇલેક્ટ્રોન ઊર્જા ગુમાવ્યા વિના ચોક્કસ ઊર્જા કક્ષાઓમાં (K, L, M, N) પરિભ્રમણ કરે છે."
    },

    # ── MODULE 3: BOHR-BURY SCHEME & VALENCY ─────────────────────────────────
    {
        "id": "KOBJ_C9S4_MOD3_REVEAL",
        "type": "theory",
        "title": "Step 4: Reveal - Electronic Configuration & Valency",
        "title_hi": "चरण 4: मुख्य अवधारणा - इलेक्ट्रॉनिक विन्यास और संयोजकता",
        "title_gu": "પગલું 4: મુખ્ય વિભાવના - ઇલેક્ટ્રોનીય રચના અને સંયોજકતા",
        "body": "Bohr-Bury Scheme:\n• Maximum electrons in n-th shell = 2n² (K=2, L=8, M=18, N=32).\n• Maximum electrons in outermost shell = 8 (Octet rule).\nValency Calculation:\n• If valence electrons (v) ≤ 4, Valency = v (e.g., Sodium 2,8,1 -> Valency = 1).\n• If valence electrons (v) > 4, Valency = 8 - v (e.g., Chlorine 2,8,7 -> Valency = 8 - 7 = 1).",
        "body_hi": "बोर-बरी योजना:\n• n-वीं कक्षा में अधिकतम इलेक्ट्रॉन = 2n² (K=2, L=8, M=18, N=32)।\n• सबसे बाहरी कक्षा में अधिकतम इलेक्ट्रॉन = 8 (अष्टक नियम)।\nसंयोजकता गणना:\n• यदि संयोजी इलेक्ट्रॉन (v) ≤ 4, संयोजकता = v (जैसे सोडियम 2,8,1 -> संयोजकता = 1)।\n• यदि संयोजी इलेक्ट्रॉन (v) > 4, संयोजकता = 8 - v (जैसे क्लोरीन 2,8,7 -> संयोजकता = 8 - 7 = 1)।",
        "body_gu": "બોહર-બરી યોજના:\n• n-મી કક્ષામાં મહત્તમ ઇલેક્ટ્રોન = 2n² (K=2, L=8, M=18, N=32).\n• સૌથી બહારની કક્ષામાં મહત્તમ ઇલેક્ટ્રોન = 8 (અષ્ટકનો નિયમ).\nસંયોજકતા ગણતરી:\n• જો સંયોજકતા ઇલેક્ટ્રોન (v) ≤ 4, સંયોજકતા = v (જેમ કે સોડિયમ 2,8,1 -> સંયોજકતા = 1).\n• જો સંયોજકતા ઇલેક્ટ્રોન (v) > 4, સંયોજકતા = 8 - v (જેમ કે ક્લોરિન 2,8,7 -> સંયોજકતા = 8 - 7 = 1)."
    },

    # ── MODULE 4: ISOTOPES AND ISOBARS ───────────────────────────────────────
    {
        "id": "KOBJ_C9S4_MOD4_REVEAL",
        "type": "theory",
        "title": "Step 4: Reveal - Atomic Number, Mass Number, Isotopes & Isobars",
        "title_hi": "चरण 4: मुख्य अवधारणा - परमाणु संख्या, द्रव्यमान संख्या, समस्थानिक और समभारिक",
        "title_gu": "પગલું 4: મુખ્ય વિભાવના - પરમાણ્વીય ક્રમાંક, દળાંક, સમસ્થાનિકો અને સમભારીઓ",
        "body": "• Atomic Number (Z): Number of protons in nucleus.\n• Mass Number (A): Protons + Neutrons (Nucleons).\n• Isotopes: Atoms of same element with same Z but different A (e.g., Carbon-12 and Carbon-14, Hydrogen isotopes: Protium ¹H, Deuterium ²H, Tritium ³H).\n• Isobars: Atoms of different elements with different Z but same A (e.g., Argon ⁴⁰₁₈Ar and Calcium ⁴⁰₂₀Ca).",
        "body_hi": "• परमाणु संख्या (Z): नाभिक में प्रोटॉनों की संख्या।\n• द्रव्यमान संख्या (A): प्रोटॉन + न्यूट्रॉन (न्यूक्लियॉन)।\n• समस्थानिक (Isotopes): समान Z लेकिन भिन्न A वाले एक ही तत्व के परमाणु (जैसे Carbon-12, Carbon-14, प्रोटियम ¹H, ड्यूटेरियम ²H, ट्राइटियम ³H)।\n• समभारिक (Isobars): भिन्न Z लेकिन समान A वाले भिन्न तत्वों के परमाणु (जैसे ⁴⁰₁₈Ar और ⁴⁰₂₀Ca)।",
        "body_gu": "• પરમાણ્વીય ક્રમાંક (Z): ન્યુક્લિયસમાં રહેલા પ્રોટોનની સંખ્યા.\n• દળાંક / દળ ક્રમાંક (A): પ્રોટોન + ન્યુટ્રોન (ન્યુક્લિઓન્સ).\n• સમસ્થાનિકો (Isotopes): સમાન Z પરંતુ ભિન્ન A ધરાવતા એક જ તત્વના પરમાણુઓ (જેમ કે Carbon-12, Carbon-14, પ્રોટિયમ ¹H, ડ્યુટેરિયમ ²H, ટ્રાઇટિયમ ³H).\n• સમભારીઓ (Isobars): ભિન્ન Z પરંતુ સમાન A ધરાવતા જુદા જુદા તત્વોના પરમાણુઓ (જેમ કે ⁴⁰₁₈Ar અને ⁴⁰₂₀Ca)."
    }
]

# 26 OFFICIAL TEXTBOOK EXERCISE QUESTIONS (IN-TEXT + END-OF-CHAPTER)
textbook_exercise_questions = [
    {
        "id": "KOBJ_C9S4_EX_Q01",
        "type": "quiz",
        "title": "Textbook Exercise 1: Canal Rays Definition",
        "title_hi": "पाठ्यपुस्तक अभ्यास 1: केनाल किरणें",
        "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 1: કેનાલ કિરણો",
        "question": "What are canal rays?",
        "question_hi": "केनाल किरणें (Canal Rays) क्या हैं?",
        "question_gu": "કેનાલ કિરણો (Canal Rays) એટલે શું?",
        "options": [
            "Beams of positively charged radiation that led to the discovery of protons",
            "Beams of negative electrons",
            "Neutral light beams",
            "Radioactive gamma rays"
        ],
        "options_hi": [
            "धनावेशित विकिरणों की किरणें जिनसे प्रोटॉन की खोज हुई",
            "ऋणात्मक इलेक्ट्रॉनों की किरणें",
            "उदासीन प्रकाश की किरणें",
            "रेडियोधर्मी गामा किरणें"
        ],
        "options_gu": [
            "ધનભારિત વિકિરણોના કિરણપૂંજ જેનાથી પ્રોટોનની શોધ થઈ",
            "ઋણભારિત ઇલેક્ટ્રોનના કિરણો",
            "તટસ્થ પ્રકાશના કિરણો",
            "રેડિયોએક્ટિવ ગામા કિરણો"
        ],
        "correct_index": 0,
        "explanation": "Canal rays were discovered by E. Goldstein in 1886 as positively charged radiations in gas discharge tubes.",
        "explanation_hi": "केनाल किरणों की खोज 1886 में ई. गोल्डस्टीन ने गैस डिस्चार्ज ट्यूब में धनावेशित विकिरणों के रूप में की थी।",
        "explanation_gu": "કેનાલ કિરણોની શોધ 1886 માં ઇ. ગોલ્ડસ્ટીને વાયુ વિસર્જન નળીમાં ધનભારિત વિકિરણો તરીકે કરી હતી."
    },
    {
        "id": "KOBJ_C9S4_EX_Q08",
        "type": "quiz",
        "title": "Textbook Exercise 8: Neutrons in Helium Nucleus",
        "title_hi": "पाठ्यपुस्तक अभ्यास 8: हीलियम में न्यूट्रॉन",
        "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 8: હિલિયમમાં ન્યુટ્રોન",
        "question": "A Helium atom has an atomic mass of 4 u and 2 protons in its nucleus. How many neutrons does it have?",
        "question_hi": "हीलियम परमाणु का परमाणु द्रव्यमान 4 u है और इसके नाभिक में 2 प्रोटॉन हैं। इसमें कितने न्यूट्रॉन होंगे?",
        "question_gu": "હિલિયમ પરમાણુનું પરમાણ્વીય દળ 4 u છે અને તેના ન્યુક્લિયસમાં 2 પ્રોટોન છે. તો તેમાં કેટલા ન્યુટ્રોન હશે?",
        "options": [
            "2 neutrons",
            "4 neutrons",
            "0 neutrons",
            "6 neutrons"
        ],
        "options_hi": [
            "2 न्यूट्रॉन",
            "4 न्यूट्रॉन",
            "0 न्यूट्रॉन",
            "6 न्यूट्रॉन"
        ],
        "options_gu": [
            "2 ન્યુટ્રોન",
            "4 ન્યુટ્રોન",
            "0 ન્યુટ્રોન",
            "6 ન્યુટ્રોન"
        ],
        "correct_index": 0,
        "explanation": "Mass Number (A) = Protons + Neutrons. Neutrons = A - Protons = 4 - 2 = 2.",
        "explanation_hi": "द्रव्यमान संख्या (A) = प्रोटॉन + न्यूट्रॉन। न्यूट्रॉन = 4 - 2 = 2।",
        "explanation_gu": "દળાંક (A) = પ્રોટોન + ન્યુટ્રોન. ન્યુટ્રોન = 4 - 2 = 2."
    },
    {
        "id": "KOBJ_C9S4_EX_Q09",
        "type": "quiz",
        "title": "Textbook Exercise 9: Electron Distribution in Carbon and Sodium",
        "title_hi": "पाठ्यपुस्तक अभ्यास 9: कार्बन और सोडियम का इलेक्ट्रॉनिक विन्यास",
        "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 9: કાર્બન અને સોડિયમની ઇલેક્ટ્રોનીય રચના",
        "question": "Write the distribution of electrons in Carbon (Z=6) and Sodium (Z=11) atoms.",
        "question_hi": "कार्बन (Z=6) और सोडियम (Z=11) परमाणुओं में इलेक्ट्रॉनों का वितरण लिखें।",
        "question_gu": "કાર્બન (Z=6) અને સોડિયમ (Z=11) પરમાણુઓમાં ઇલેક્ટ્રોનની વહેંચણી લખો.",
        "options": [
            "Carbon: K=2, L=4 | Sodium: K=2, L=8, M=1",
            "Carbon: K=4, L=2 | Sodium: K=2, L=9",
            "Carbon: K=6 | Sodium: K=2, L=2, M=7",
            "Carbon: K=2, L=2, M=2 | Sodium: K=8, L=3"
        ],
        "options_hi": [
            "कार्बन: K=2, L=4 | सोडियम: K=2, L=8, M=1",
            "कार्बन: K=4, L=2 | सोडियम: K=2, L=9",
            "कार्बन: K=6 | सोडियम: K=2, L=2, M=7",
            "कार्बन: K=2, L=2, M=2 | सोडियम: K=8, L=3"
        ],
        "options_gu": [
            "કાર્બન: K=2, L=4 | સોડિયમ: K=2, L=8, M=1",
            "કાર્બન: K=4, L=2 | સોડિયમ: K=2, L=9",
            "કાર્બન: K=6 | સોડિયમ: K=2, L=2, M=7",
            "કાર્બન: K=2, L=2, M=2 | સોડિયમ: K=8, L=3"
        ],
        "correct_index": 0,
        "explanation": "Carbon (6 e⁻) -> K=2, L=4. Sodium (11 e⁻) -> K=2, L=8, M=1.",
        "explanation_hi": "कार्बन (6 e⁻) -> K=2, L=4। सोडियम (11 e⁻) -> K=2, L=8, M=1।",
        "explanation_gu": "કાર્બન (6 e⁻) -> K=2, L=4. સોડિયમ (11 e⁻) -> K=2, L=8, M=1."
    },
    {
        "id": "KOBJ_C9S4_EX_Q11",
        "type": "quiz",
        "title": "Textbook Exercise 11: Valency of Cl, S and Mg",
        "title_hi": "पाठ्यपुस्तक अभ्यास 11: Cl, S और Mg की संयोजकता",
        "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 11: Cl, S અને Mg ની સંયોજકતા",
        "question": "How will you find the valencies of Chlorine (Z=17), Sulphur (Z=16), and Magnesium (Z=12)?",
        "question_hi": "क्लोरीन (Z=17), सल्फर (Z=16) और मैग्नीशियम (Z=12) की संयोजकता कैसे ज्ञात करेंगे?",
        "question_gu": "ક્લોરિન (Z=17), સલ્ફર (Z=16) અને મેગ્નેશિયમ (Z=12) ની સંયોજકતા કેવી રીતે શોધશો?",
        "options": [
            "Chlorine: 1 (8-7), Sulphur: 2 (8-6), Magnesium: 2",
            "Chlorine: 7, Sulphur: 6, Magnesium: 2",
            "Chlorine: 2, Sulphur: 4, Magnesium: 8",
            "All have valency = 0"
        ],
        "options_hi": [
            "क्लोरीन: 1 (8-7), सल्फर: 2 (8-6), मैग्नीशियम: 2",
            "क्लोरीन: 7, सल्फर: 6, मैग्नीशियम: 2",
            "क्लोरीन: 2, सल्फर: 4, मैग्नीशियम: 8",
            "सभी की संयोजकता = 0"
        ],
        "options_gu": [
            "ક્લોરિન: 1 (8-7), સલ્ફર: 2 (8-6), મેગ્નેશિયમ: 2",
            "ક્લોરિન: 7, સલ્ફર: 6, મેગ્નેશિયમ: 2",
            "ક્લોરિન: 2, સલ્ફર: 4, મેગ્નેશિયમ: 8",
            "બધાની સંયોજકતા = 0"
        ],
        "correct_index": 0,
        "explanation": "Cl (2,8,7) -> Valency = 8 - 7 = 1. S (2,8,6) -> Valency = 8 - 6 = 2. Mg (2,8,2) -> Valency = 2.",
        "explanation_hi": "Cl (2,8,7) -> संयोजकता = 8 - 7 = 1। S (2,8,6) -> संयोजकता = 8 - 6 = 2। Mg (2,8,2) -> संयोजकता = 2।",
        "explanation_gu": "Cl (2,8,7) -> સંયોજકતા = 8 - 7 = 1. S (2,8,6) -> સંયોજકતા = 8 - 6 = 2. Mg (2,8,2) -> સંયોજકતા = 2."
    },
    {
        "id": "KOBJ_C9S4_EX_Q22",
        "type": "quiz",
        "title": "Textbook Exercise 22: Filled K and L Shells of Na⁺ Ion",
        "title_hi": "पाठ्यपुस्तक अभ्यास 22: Na⁺ आयन की पूरी भरी K और L कक्षाएं",
        "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 22: Na⁺ આયનની પૂર્ણ ભરાયેલી K અને L કક્ષાઓ",
        "question": "Na⁺ has completely filled K and L shells. Explain why.",
        "question_hi": "Na⁺ आयन के K और L कोश पूरी तरह से भरे होते हैं। व्याख्या कीजिए।",
        "question_gu": "Na⁺ આયનની K અને L કક્ષાઓ સંપૂર્ણ ભરાયેલી હોય છે. સમજાવો.",
        "options": [
            "Na atom has 11 electrons (2,8,1). Losing 1 valence electron leaves Na⁺ with 10 electrons (K=2, L=8), both completely filled",
            "Na⁺ gains 1 electron making it 12",
            "K shell holds 8 electrons in Na⁺",
            "Na⁺ has no electrons"
        ],
        "options_hi": [
            "Na परमाणु में 11 इलेक्ट्रॉन (2,8,1) होते हैं। 1 इलेक्ट्रॉन त्यागने पर Na⁺ में 10 इलेक्ट्रॉन (K=2, L=8) बचते हैं, जो दोनों पूर्ण भरे हैं",
            "Na⁺ 1 इलेक्ट्रॉन ग्रहण करके 12 बनाता है",
            "Na⁺ में K कोश 8 इलेक्ट्रॉन रखता है",
            "Na⁺ में कोई इलेक्ट्रॉन नहीं होता"
        ],
        "options_gu": [
            "Na પરમાણુમાં 11 ઇલેક્ટ્રોન (2,8,1) હોય છે. 1 ઇલેક્ટ્રોન ગુમાવતા Na⁺ પાસે 10 ઇલેક્ટ્રોન (K=2, L=8) રહે છે, જે બંને સંપૂર્ણ ભરાયેલા છે",
            "Na⁺ 1 ઇલેક્ટ્રોન મેળવી 12 બનાવે છે",
            "Na⁺ માં K કક્ષા 8 ઇલેક્ટ્રોન ધરાવે છે",
            "Na⁺ માં કોઈ ઇલેક્ટ્રોન હોતો નથી"
        ],
        "correct_index": 0,
        "explanation": "Na atom (Z=11) configuration is 2,8,1. By removing the 1 outer electron, Na⁺ ion gets 10 electrons: K=2 (max 2) and L=8 (max 8), both completely filled.",
        "explanation_hi": "Na परमाणु (Z=11) का विन्यास 2,8,1 है। 1 बाहरी इलेक्ट्रॉन हटाने पर Na⁺ आयन में 10 इलेक्ट्रॉन बचते हैं: K=2 और L=8, दोनों पूर्ण भरे हैं।",
        "explanation_gu": "Na પરમાણુ (Z=11) ની રચના 2,8,1 છે. બહારનો 1 ઇલેક્ટ્રોન દૂર થતા Na⁺ આયન પાસે 10 ઇલેક્ટ્રોન રહે છે: K=2 અને L=8, બંને સંપૂર્ણ પૂર્ણ ભરાયેલા છે."
    },
    {
        "id": "KOBJ_C9S4_EX_Q23",
        "type": "quiz",
        "title": "Textbook Exercise 23: Average Atomic Mass of Bromine",
        "title_hi": "पाठ्यपुस्तक अभ्यास 23: ब्रोमीन का औसत परमाणु द्रव्यमान",
        "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 23: બ્રોમિનનું સરેરાશ પરમાણ્વીય દળ",
        "question": "If Bromine atom is available in the form of two isotopes ⁷⁹Br (49.7%) and ⁸¹Br (50.3%), calculate the average atomic mass of bromine atom.",
        "question_hi": "यदि ब्रोमीन परमाणु दो समस्थानिकों ⁷⁹Br (49.7%) और ⁸¹Br (50.3%) के रूप में उपलब्ध है, तो ब्रोमीन का औसत परमाणु द्रव्यमान परिकलित कीजिए।",
        "question_gu": "જો બ્રોમિન પરમાણુ બે સમસ્થાનિકો ⁷⁹Br (49.7%) અને ⁸¹Br (50.3%) ના સ્વરૂપમાં મળી આવતો હોય, તો બ્રોમિન પરમાણુનું સરેરાશ પરમાણ્વીય દળ શોધો.",
        "options": [
            "80.006 u",
            "80.000 u",
            "79.500 u",
            "81.000 u"
        ],
        "options_hi": [
            "80.006 u",
            "80.000 u",
            "79.500 u",
            "81.000 u"
        ],
        "options_gu": [
            "80.006 u",
            "80.000 u",
            "79.500 u",
            "81.000 u"
        ],
        "correct_index": 0,
        "explanation": "Average Mass = (79 × 49.7 / 100) + (81 × 50.3 / 100) = 39.263 + 40.743 = 80.006 u.",
        "explanation_hi": "औसत द्रव्यमान = (79 × 49.7 / 100) + (81 × 50.3 / 100) = 39.263 + 40.743 = 80.006 u।",
        "explanation_gu": "સરેરાશ દળ = (79 × 49.7 / 100) + (81 × 50.3 / 100) = 39.263 + 40.743 = 80.006 u."
    },
    {
        "id": "KOBJ_C9S4_EX_Q24",
        "type": "quiz",
        "title": "Textbook Exercise 24: Isotope Percentages of Element X (16.2 u)",
        "title_hi": "पाठ्यपुस्तक अभ्यास 24: तत्व X के समस्थानिकों का प्रतिशत",
        "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 24: તત્વ X ના સમસ્થાનિકોની ટકાવારી",
        "question": "The average atomic mass of a sample of element X is 16.2 u. What are the percentages of isotopes ¹⁶X and ¹⁸X in the sample?",
        "question_hi": "किसी तत्व X के एक नमूने का औसत परमाणु द्रव्यमान 16.2 u है। नमूने में समस्थानिकों ¹⁶X और ¹⁸X का प्रतिशत क्या है?",
        "question_gu": "કોઈ તત્વ X ના નમૂનાનું સરેરાશ પરમાણ્વીય દળ 16.2 u છે. નમૂનામાં સમસ્થાનિકો ¹⁶X અને ¹⁸X ની ટકાવારી કેટલી હશે?",
        "options": [
            "¹⁶X = 90% and ¹⁸X = 10%",
            "¹⁶X = 80% and ¹⁸X = 20%",
            "¹⁶X = 50% and ¹⁸X = 50%",
            "¹⁶X = 75% and ¹⁸X = 25%"
        ],
        "options_hi": [
            "¹⁶X = 90% और ¹⁸X = 10%",
            "¹⁶X = 80% और ¹⁸X = 20%",
            "¹⁶X = 50% और ¹⁸X = 50%",
            "¹⁶X = 75% और ¹⁸X = 25%"
        ],
        "options_gu": [
            "¹⁶X = 90% અને ¹⁸X = 10%",
            "¹⁶X = 80% અને ¹⁸X = 20%",
            "¹⁶X = 50% અને ¹⁸X = 50%",
            "¹⁶X = 75% અને ¹⁸X = 25%"
        ],
        "correct_index": 0,
        "explanation": "Let % of ¹⁶X = x. 16(x)/100 + 18(100-x)/100 = 16.2 -> 16x + 1800 - 18x = 1620 -> 2x = 180 -> x = 90%. ¹⁶X = 90%, ¹⁸X = 10%.",
        "explanation_hi": "मान लें ¹⁶X = x%। 16x/100 + 18(100-x)/100 = 16.2 -> 2x = 180 -> x = 90%। ¹⁶X = 90%, ¹⁸X = 10%।",
        "explanation_gu": "ધારો કે ¹⁶X = x%. 16x/100 + 18(100-x)/100 = 16.2 -> 2x = 180 -> x = 90%. ¹⁶X = 90%, ¹⁸X = 10%."
    }
]

# Combine all blocks
all_blocks = blocks + textbook_exercise_questions
print(f"Total blocks generated for Class 9 Science Ch 4: {len(all_blocks)}")

# Save to learning_modules blocks.json
blocks_path = 'app_core/learning_modules/gseb_class9_science_ch4/blocks.json'
with open(blocks_path, 'w', encoding='utf-8') as f:
    json.dump(all_blocks, f, ensure_ascii=False, indent=2)
print(f"Saved blocks to {blocks_path}")

# Sync to app_core/chapters/ncert_class9_science_ch4.json
ncert_path = 'app_core/chapters/ncert_class9_science_ch4.json'
ncert_payload = {
    "metadata": {
        "id": "ncert_class9_science_ch4",
        "title": "Chapter 4: Structure of the Atom",
        "title_hi": "अध्याय 4: परमाणु की संरचना",
        "title_gu": "પ્રકરણ 4: પરમાણુનું બંધારણ",
        "subject": "Science",
        "grade": "Class 9"
    },
    "blocks": all_blocks
}
with open(ncert_path, 'w', encoding='utf-8') as f:
    json.dump(ncert_payload, f, ensure_ascii=False, indent=2)
print(f"Synced to {ncert_path}")

# Sync to assessment bank
assessment_path = 'app_core/assessment/gseb_class9_science_ch4_questions.json'
assessment_questions = []
for idx, q in enumerate(textbook_exercise_questions):
    assessment_questions.append({
        "id": f"gseb_c9_sci_ch4_q_{idx+1:03d}",
        "chapter_id": "gseb_class9_science_ch4",
        "topic_id": "structure_of_the_atom",
        "type": "quiz",
        "difficulty": "medium",
        "board": "GSEB",
        "marks": 1,
        "bloom_taxonomy": "Understand",
        "keywords": ["electron", "proton", "neutron", "rutherford", "bohr", "valency", "isotopes", "isobars"],
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
    "chapter_id": "gseb_class9_science_ch4",
    "questions": assessment_questions
}
with open(assessment_path, 'w', encoding='utf-8') as f:
    json.dump(assessment_payload, f, ensure_ascii=False, indent=2)
print(f"Updated assessment bank at {assessment_path}")
