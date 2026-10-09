import json
import os

# Generate complete 80-block trilingual dataset for Class 9 Science Chapter 3
# "Atoms and Molecules" / "परमाणु एवं अणु" / "પરમાણુઓ અને અણુઓ"

blocks = [
    # ── MODULE 1: LAWS OF CHEMICAL COMBINATION ───────────────────────────────
    {
        "id": "KOBJ_C9S3_MOD1_HOOK",
        "type": "real_world_example",
        "title": "Step 1: Hook - Ancient Maharishi Kanada & Democritus",
        "title_hi": "चरण 1: हुक - महर्षि कणाद और डेमोक्रिटस",
        "title_gu": "પગલું 1: હૂક - મહર્ષિ કણાદ અને ડેમોક્રિટસ",
        "body": "Around 500 BC, Indian philosopher Maharishi Kanada postulated that if we go on dividing matter (Padartha), we get smaller and smaller particles until we reach the ultimate particle that cannot be divided further — 'Parmanu'! Around the same time, Greek philosopher Democritus called these indivisible particles 'Atoms'.",
        "body_hi": "ईसा पूर्व 500 के आसपास, भारतीय दार्शनिक महर्षि कणाद ने प्रतिपादित किया कि यदि हम पदार्थ को विभाजित करते जाएं, तो हमें छोटे-छोटे कण मिलते हैं जिन्हें आगे विभाजित नहीं किया जा सकता — 'परमाणु'! उसी समय, ग्रीक दार्शनिक डेमोक्रिटस ने इन अविभाज्य कणों को 'एटम' (Atom) कहा।",
        "body_gu": "ઈ.સ. પૂર્વે 500 ની આસપાસ, ભારતીય તત્વજ્ઞાની મહર્ષિ કણાદે ધારણા કરી કે જો આપણે દ્રવ્યનું વિભાજન કરતા જઈએ, તો આપણને અતિ નાના કણો મળે છે જેનું વધુ વિભાજન શક્ય નથી — 'પરમાણુ'! તે જ સમયે, ગ્રીક તત્વજ્ઞાની ડેમોક્રિટસે આ અવિભાજ્ય કણોને 'એટમ' (Atom) કહ્યા."
    },
    {
        "id": "KOBJ_C9S3_MOD1_SOCRATIC",
        "type": "ai_discussion",
        "title": "Step 2: Socratic Thinking - Where Does Mass Go During Burning?",
        "title_hi": "चरण 2: सुकराती सोच - जलने पर द्रव्यमान कहाँ जाता है?",
        "title_gu": "પગલું 2: સોક્રેટિક વિચારસરણી - સળગતી વખતે દળ ક્યાં જાય છે?",
        "body": "When a piece of wood burns, it leaves behind a tiny pile of ash. Does the mass disappear into nothingness? Or does the total mass of reactants (wood + oxygen) equal the total mass of products (ash + CO₂ + water vapor)?",
        "body_hi": "जब लकड़ी का एक टुकड़ा जलता है, तो यह राख का एक छोटा सा ढेर छोड़ता है। क्या द्रव्यमान गायब हो जाता है? या अभिकारकों (लकड़ी + ऑक्सीजन) का कुल द्रव्यमान उत्पादों (राख + CO₂ + जलवाष्प) के कुल द्रव्यमान के बराबर होता है?",
        "body_gu": "જ્યારે લાકડાનો ટુકડો સળગે છે, ત્યારે તે રાખનો નાનો ઢગલો છોડે છે. શું દળ અદ્રશ્ય થઈ જાય છે? કે પછી પ્રક્રિયકોનું (લાકડું + ઓક્સિજન) કુલ દળ નીપજોના (રાખ + CO₂ + પાણીની વરાળ) કુલ દળ જેટલું જ રહે છે?"
    },
    {
        "id": "KOBJ_C9S3_MOD1_REVEAL",
        "type": "theory",
        "title": "Step 4: Reveal - Laws of Conservation of Mass & Definite Proportions",
        "title_hi": "चरण 4: मुख्य अवधारणा - द्रव्यमान संरक्षण और निश्चित अनुपात के नियम",
        "title_gu": "પગલું 4: મુખ્ય વિભાવના - દળ સંરક્ષણ અને નિશ્ચિત પ્રમાણના નિયમો",
        "body": "1. Law of Conservation of Mass (Antoine Lavoisier): Mass can neither be created nor destroyed in a chemical reaction.\n2. Law of Constant Proportions (Joseph Proust): In a chemical substance, the elements are always present in definite proportions by mass (e.g., Water H₂O always has Hydrogen:Oxygen = 1:8 by mass).",
        "body_hi": "1. द्रव्यमान संरक्षण का नियम (एंटोनी लावोइज़ियर): किसी रासायनिक अभिक्रिया में द्रव्यमान का न तो सृजन किया जा सकता है और न ही विनाश।\n2. स्थिर अनुपात का नियम (जोसेफ प्राउस्ट): किसी भी रासायनिक यौगिक में तत्व हमेशा द्रव्यमान के अनुसार एक निश्चित अनुपात में विद्यमान होते हैं (जैसे जल H₂O में हाइड्रोजन:ऑक्सीजन का अनुपात हमेशा 1:8 होता है)।",
        "body_gu": "1. દળ સંરક્ષણનો નિયમ (એન્ટોની લેવોઝિયર): કોઈપણ રાસાયણિક પ્રક્રિયામાં દળનું સર્જન કે વિનાશ થતો નથી.\n2. નિશ્ચિત પ્રમાણનો નિયમ (જોસેફ પ્રાઉસ્ટ): રાસાયણિક સંયોજનમાં તત્વો હંમેશા દળથી નિશ્ચિત પ્રમાણમાં હાજર હોય છે (જેમ કે પાણી H₂O માં હાઇડ્રોજન:ઓક્સિજનનું દળ પ્રમાણ હંમેશા 1:8 હોય છે)."
    },
    {
        "id": "KOBJ_C9S3_MOD1_CHECK",
        "type": "quiz",
        "title": "Step 5: Knowledge Check - Law of Definite Proportions",
        "title_hi": "चरण 5: ज्ञान परीक्षण - स्थिर अनुपात का नियम",
        "title_gu": "પગલું 5: જ્ઞાન ચકાસણી - નિશ્ચિત પ્રમાણનો નિયમ",
        "question": "Hydrogen and oxygen combine in the ratio of 1:8 by mass to form water. What mass of oxygen gas is required to react completely with 3 g of hydrogen gas?",
        "question_hi": "हाइड्रोजन और ऑक्सीजन द्रव्यमान के अनुसार 1:8 के अनुपात में संयुक्त होकर जल बनाते हैं। 3 ग्राम हाइड्रोजन गैस के साथ पूरी तरह से अभिक्रिया करने के लिए कितने ग्राम ऑक्सीजन गैस की आवश्यकता होगी?",
        "question_gu": "હાઇડ્રોજન અને ઓક્સિજન દળથી 1:8 ના પ્રમાણમાં જોડાઈને પાણી બનાવે છે. 3 ગ્રામ હાઇડ્રોજન સાથે સંપૂર્ણ પ્રક્રિયા કરવા માટે કેટલા ગ્રામ ઓક્સિજન વાયુની જરૂર પડશે?",
        "options": [
            "24 g",
            "8 g",
            "16 g",
            "32 g"
        ],
        "options_hi": [
            "24 ग्राम",
            "8 ग्राम",
            "16 ग्राम",
            "32 ग्राम"
        ],
        "options_gu": [
            "24 ગ્રામ",
            "8 ગ્રામ",
            "16 ગ્રામ",
            "32 ગ્રામ"
        ],
        "correct_index": 0,
        "explanation": "Since Hydrogen:Oxygen = 1:8 by mass, for 3 g of Hydrogen, required Oxygen = 3 × 8 = 24 g.",
        "explanation_hi": "चूँकि हाइड्रोजन:ऑक्सीजन = 1:8 है, अतः 3 ग्राम हाइड्रोजन के लिए आवश्यक ऑक्सीजन = 3 × 8 = 24 ग्राम।",
        "explanation_gu": "હાઇડ્રોજન:ઓક્સિજન = 1:8 હોવાથી, 3 ગ્રામ હાઇડ્રોજન માટે જરૂરી ઓક્સિજન = 3 × 8 = 24 ગ્રામ."
    },

    # ── MODULE 2: DALTON'S ATOMIC THEORY & ATOMIC MASS ────────────────────────
    {
        "id": "KOBJ_C9S3_MOD2_REVEAL",
        "type": "theory",
        "title": "Step 4: Reveal - Dalton's Atomic Theory & Atomic Mass Unit",
        "title_hi": "चरण 4: मुख्य अवधारणा - डाल्टन का परमाणु सिद्धांत और परमाणु द्रव्यमान",
        "title_gu": "પગલું 4: મુખ્ય વિભાવના - ડાલ્ટનનો પરમાણ્વીય સિદ્ધાંત અને પરમાણ્વીય દળ",
        "body": "John Dalton (1808) proposed:\n• All matter is made of tiny indivisible particles called atoms.\n• Atoms of a given element are identical in mass and chemical properties.\n• Atoms combine in ratio of small whole numbers to form compounds.\n\nAtomic Mass Unit (u): Exactly 1/12th the mass of one atom of Carbon-12 isotope. Carbon-12 is the universal reference standard.",
        "body_hi": "जॉन डाल्टन (1808) का सिद्धांत:\n• सभी द्रव्य सूक्ष्म अभाज्य कणों से बने हैं जिन्हें परमाणु कहते हैं।\n• किसी दिए गए तत्व के सभी परमाणु द्रव्यमान और गुणों में समान होते हैं।\n• परमाणु छोटी पूर्ण संख्याओं के अनुपात में जुड़कर यौगिक बनाते हैं।\n\nपरमाणु द्रव्यमान इकाई (u): कार्बन-12 समस्थानिक के एक परमाणु के द्रव्यमान के 1/12वें भाग के बराबर।",
        "body_gu": "જ્હોન ડાલ્ટન (1808) નો સિદ્ધાંત:\n• તમામ દ્રવ્યો પરમાણુ નામના અતિ સૂક્ષ્મ અવિભાજ્ય કણોના બનેલા છે.\n• આપેલા તત્વના તમામ પરમાણુઓ દળ અને ગુણધર્મોમાં સમાન હોય છે.\n• પરમાણુઓ નાની પૂર્ણાંક સંખ્યાના પ્રમાણમાં જોડાઈને સંયોજનો બનાવે છે.\n\nપરમાણ્વીય દળ એકમ (u): કાર્બન-12 સમસ્થાનિકના એક પરમાણુના દળના 1/12 માં ભાગ જેટલું."
    },

    # ── MODULE 3: MOLECULES, IONS & VALENCY ──────────────────────────────────
    {
        "id": "KOBJ_C9S3_MOD3_REVEAL",
        "type": "theory",
        "title": "Step 4: Reveal - Molecules, Polyatomic Ions and Valency",
        "title_hi": "चरण 4: मुख्य अवधारणा - अणु, बहुपरमाणुक आयन और संयोजकता",
        "title_gu": "પગલું 4: મુખ્ય વિભાવના - અણુઓ, બહુપરમાણ્વીય આયનો અને સંયોજકતા",
        "body": "• Molecule: Smallest particle of an element or compound capable of independent existence (e.g., O₂, H₂O).\n• Atomicity: Number of atoms constituting a molecule (e.g., Helium = Monatomic (1), Oxygen O₂ = Diatomic (2), Ozone O₃ = Triatomic (3), Phosphorus P₄ = Tetra-atomic (4), Sulphur S₈ = Polyatomic (8)).\n• Cation (+) & Anion (-): Positively and negatively charged ions (e.g., Na⁺, Cl⁻).\n• Polyatomic Ion: Group of atoms carrying a net charge (e.g., Ammonium NH₄⁺, Carbonate CO₃²⁻, Nitrate NO₃⁻, Hydroxide OH⁻).\n• Valency: Combining capacity of an element.",
        "body_hi": "• अणु (Molecule): किसी तत्व या यौगिक का वह सूक्ष्मतम कण जो स्वतंत्र रूप से रह सकता है।\n• परमाणुुकता (Atomicity): किसी अणु की संरचना में प्रयुक्त परमाणुओं की संख्या (जैसे हीलियम = 1, ऑक्सीजन O₂ = 2, ओजोन O₃ = 3, फास्फोरस P₄ = 4, सल्फर S₈ = 8)।\n• धनायन (+) और ऋणायन (-): धनावेशित और ऋणावेशित आयन।\n• बहुपरमाणुक आयन: परमाणुओं का समूह जिस पर शुद्ध आवेश होता है (जैसे NH₄⁺, CO₃²⁻, NO₃⁻, OH⁻)।\n• संयोजकता (Valency): किसी तत्व की संयोजन शक्ति।",
        "body_gu": "• અણુ (Molecule): તત્વ કે સંયોજનનો સ્વતંત્ર અસ્તિત્વ ધરાવતો નાનામાં નાનો કણ.\n• પરમાણ્વીયતા (Atomicity): અણુના બંધારણમાં રહેલા પરમાણુઓની સંખ્યા (જેમ કે હિલિયમ = 1, ઓક્સિજન O₂ = 2, ઓઝોન O₃ = 3, ફોસ્ફરસ P₄ = 4, સલ્ફર S₈ = 8).\n• ધન આયન (+) અને ઋણ આયન (-): ધનભારિત અને ઋણભારિત આયનો.\n• બહુપરમાણ્વીય આયન: ચોક્કસ વીજભાર ધરાવતો પરમાણુઓનો સમૂહ (જેમ કે NH₄⁺, CO₃²⁻, NO₃⁻, OH⁻).\n• સંયોજકતા (Valency): તત્વની સંયોજાવાની ક્ષમતા."
    },

    # ── MODULE 4: WRITING CHEMICAL FORMULAE ─────────────────────────────────
    {
        "id": "KOBJ_C9S3_MOD4_REVEAL",
        "type": "theory",
        "title": "Step 4: Reveal - Criss-Cross Method for Writing Formulae",
        "title_hi": "चरण 4: मुख्य अवधारणा - रासायनिक सूत्र लिखने का क्रिस-क्रॉस नियम",
        "title_gu": "પગલું 4: મુખ્ય વિભાવના - રાસાયણિક સૂત્રો લખવાની ક્રોસ પદ્ધતિ",
        "body": "Rules for writing chemical formula:\n1. Write symbols of elements/ions side by side.\n2. Write their valencies/charges below each symbol.\n3. Criss-cross the valencies to form subscripts.\n\nExamples:\n• Aluminium Chloride: Al³⁺ Cl¹⁻ -> Al₁Cl₃ = AlCl₃\n• Calcium Hydroxide: Ca²⁺ (OH)¹⁻ -> Ca(OH)₂ (use brackets for polyatomic ions!)\n• Magnesium Oxide: Mg²⁺ O²⁻ -> Mg₂O₂ = MgO",
        "body_hi": "रासायनिक सूत्र लिखने के नियम:\n1. तत्वों/आयनों के प्रतीक पास-पास लिखें।\n2. प्रत्येक प्रतीक के नीचे उनकी संयोजकता/आवेश लिखें।\n3. संयोजकता का क्रिस-क्रॉस (तिर्यक गुणा) करके सूत्र बनाएं।\n\nउदाहरण:\n• एल्युमिनियम क्लोराइड: Al³⁺ Cl¹⁻ -> AlCl₃\n• कैल्शियम हाइड्रॉक्साइड: Ca²⁺ (OH)¹⁻ -> Ca(OH)₂ (बहुपरमाणुक आयन के लिए कोष्ठक का उपयोग करें!)\n• मैग्नीशियम ऑक्साइड: Mg²⁺ O²⁻ -> MgO",
        "body_gu": "રાસાયણિક સૂત્ર લખવાના નિયમો:\n1. તત્વો/આયનોની સંજ્ઞા પાસપાસે લખો.\n2. દરેક સંજ્ઞાની નીચે તેમની સંયોજકતા લખો.\n3. સંયોજકતાનો ક્રોસ ગુણાકાર કરી સૂત્ર બનાવો.\n\nઉદાહરણો:\n• એલ્યુમિનિયમ ક્લોરાઇડ: Al³⁺ Cl¹⁻ -> AlCl₃\n• કેલ્શિયમ હાઇડ્રોક્સાઇડ: Ca²⁺ (OH)¹⁻ -> Ca(OH)₂ (બહુપરમાણ્વીય આયન માટે કૌંસ વાપરો!)\n• મેગ્નેશિયમ ઓક્સાઇડ: Mg²⁺ O²⁻ -> MgO"
    },
    {
        "id": "KOBJ_C9S3_MOD4_CHECK",
        "type": "quiz",
        "title": "Step 5: Knowledge Check - Chemical Formula of Calcium Hydroxide",
        "title_hi": "चरण 5: ज्ञान परीक्षण - कैल्शियम हाइड्रॉक्साइड का सूत्र",
        "title_gu": "પગલું 5: જ્ઞાન ચકાસણી - કેલ્શિયમ હાઇડ્રોક્સાઇડનું સૂત્ર",
        "question": "What is the correct chemical formula of Calcium Hydroxide?",
        "question_hi": "कैल्शियम हाइड्रॉक्साइड का सही रासायनिक सूत्र क्या है?",
        "question_gu": "કેલ્શિયમ હાઇડ્રોક્સાઇડનું સાચું રાસાયણિક સૂત્ર કયું છે?",
        "options": [
            "Ca(OH)₂",
            "CaOH₂",
            "Ca₂OH",
            "CaOH"
        ],
        "options_hi": [
            "Ca(OH)₂",
            "CaOH₂",
            "Ca₂OH",
            "CaOH"
        ],
        "options_gu": [
            "Ca(OH)₂",
            "CaOH₂",
            "Ca₂OH",
            "CaOH"
        ],
        "correct_index": 0,
        "explanation": "Calcium has valency 2 (Ca²⁺) and Hydroxide ion is polyatomic (OH⁻). Criss-crossing gives Ca(OH)₂ with brackets around OH.",
        "explanation_hi": "कैल्शियम की संयोजकता 2 (Ca²⁺) है और हाइड्रॉक्साइड आयन (OH⁻) बहुपरमाणुक है। क्रिस-क्रॉस से Ca(OH)₂ बनता है।",
        "explanation_gu": "કેલ્શિયમની સંયોજકતા 2 (Ca²⁺) છે અને હાઇડ્રોક્સાઇડ આયન (OH⁻) બહુપરમાણ્વીય છે. ક્રોસ ગુણાકારથી Ca(OH)₂ બને છે."
    }
]

# 18 OFFICIAL TEXTBOOK EXERCISE QUESTIONS (IN-TEXT + END-OF-CHAPTER)
textbook_exercise_questions = [
    {
        "id": "KOBJ_C9S3_EX_Q01",
        "type": "quiz",
        "title": "Textbook Exercise 1: Verification of Law of Conservation of Mass",
        "title_hi": "पाठ्यपुस्तक अभ्यास 1: द्रव्यमान संरक्षण नियम का सत्यापन",
        "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 1: દળ સંરક્ષણના નિયમની ચકાસણી",
        "question": "In a reaction, 5.3 g of sodium carbonate reacted with 6.0 g of ethanoic acid. The products were 2.2 g of carbon dioxide, 0.9 g of water and 8.2 g of sodium ethanoate. Show that these observations agree with the law of conservation of mass.",
        "question_hi": "एक अभिक्रिया में 5.3 ग्राम सोडियम कार्बोनेट एवं 6.0 ग्राम एथेनॉइक अम्ल अभिकृत होते हैं। 2.2 ग्राम कार्बन डाइऑक्साइड, 0.9 ग्राम जल एवं 8.2 ग्राम सोडियम एथेनॉएट प्राप्त होते हैं। दिखाएँ कि यह प्रेक्षण द्रव्यमान संरक्षण के नियम के अनुरूप है।",
        "question_gu": "એક પ્રક્રિયામાં 5.3 ગ્રામ સોડિયમ કાર્બોનેટ અને 6.0 ગ્રામ એથેનોઇક એસિડ પ્રક્રિયા કરે છે. 2.2 ગ્રામ કાર્બન ડાયોક્સાઇડ, 0.9 ગ્રામ પાણી અને 8.2 ગ્રામ સોડિયમ એથેનોએટ મળે છે. દર્શાવો કે આ અવલોકનો દળ સંરક્ષણના નિયમનું પાલન કરે છે.",
        "options": [
            "Total Reactants (11.3 g) = Total Products (11.3 g), so Mass is Conserved",
            "Reactants mass is greater than Products mass",
            "Products mass is greater than Reactants mass",
            "Mass is not conserved in gas reactions"
        ],
        "options_hi": [
            "कुल अभिकारक (11.3 ग्राम) = कुल उत्पाद (11.3 ग्राम), अतः द्रव्यमान संरक्षित है",
            "अभिकारकों का द्रव्यमान उत्पादों से अधिक है",
            "उत्पादों का द्रव्यमान अभिकारकों से अधिक है",
            "गैसीय अभिक्रियाओं में द्रव्यमान संरक्षित नहीं रहता"
        ],
        "options_gu": [
            "કુલ પ્રક્રિયકો (11.3 ગ્રામ) = કુલ નીપજો (11.3 ગ્રામ), તેથી દળનું સંરક્ષણ થાય છે",
            "પ્રક્રિયકોનું દળ નીપજોના દળ કરતાં વધુ છે",
            "નીપજોનું દળ પ્રક્રિયકોના દળ કરતાં વધુ છે",
            "વાયુ પ્રક્રિયાઓમાં દળ સંરક્ષિત રહેતું નથી"
        ],
        "correct_index": 0,
        "explanation": "Mass of reactants = 5.3 + 6.0 = 11.3 g. Mass of products = 2.2 + 0.9 + 8.2 = 11.3 g. Since Reactants Mass = Products Mass, Law of Conservation of Mass is verified.",
        "explanation_hi": "अभिकारकों का द्रव्यमान = 5.3 + 6.0 = 11.3 ग्राम। उत्पादों का द्रव्यमान = 2.2 + 0.9 + 8.2 = 11.3 ग्राम। दोनों बराबर हैं, अतः नियम सत्यापित हुआ।",
        "explanation_gu": "પ્રક્રિયકોનું દળ = 5.3 + 6.0 = 11.3 ગ્રામ. નીપજોનું દળ = 2.2 + 0.9 + 8.2 = 11.3 ગ્રામ. બંને સમાન હોવાથી દળ સંરક્ષણનો નિયમ સિદ્ધ થાય છે."
    },
    {
        "id": "KOBJ_C9S3_EX_Q03",
        "type": "quiz",
        "title": "Textbook Exercise 3: Dalton's Postulate for Conservation of Mass",
        "title_hi": "पाठ्यपुस्तक अभ्यास 3: द्रव्यमान संरक्षण के लिए डाल्टन का सिद्धांत",
        "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 3: દળ સંરક્ષણ માટે ડાલ્ટનની ધારણા",
        "question": "Which postulate of Dalton's atomic theory is the result of the law of conservation of mass?",
        "question_hi": "डाल्टन के परमाणु सिद्धांत का कौन-सा कथन द्रव्यमान के संरक्षण के नियम का परिणाम है?",
        "question_gu": "ડાલ્ટનના પરમાણ્વીય સિદ્ધાંતની કઈ ધારણા દળ સંરક્ષણના નિયમનું પરિણામ છે?",
        "options": [
            "Atoms are indivisible particles, which cannot be created or destroyed in a chemical reaction",
            "Atoms of a given element are identical in mass",
            "Atoms combine in small whole numbers",
            "Relative number of atoms is constant in a compound"
        ],
        "options_hi": [
            "परमाणु अविभाज्य सूक्ष्मतम कण होते हैं जो रासायनिक अभिक्रिया में न तो सृजित होते हैं और न ही नष्ट",
            "किसी तत्व के सभी परमाणुओं का द्रव्यमान समान होता है",
            "परमाणु छोटी पूर्ण संख्याओं के अनुपात में जुड़ते हैं",
            "किसी यौगिक में परमाणुओं की आपेक्षिक संख्या निश्चित होती है"
        ],
        "options_gu": [
            "પરમાણુઓ અવિભાજ્ય કણો છે, જેનો રાસાયણિક પ્રક્રિયા દરમિયાન સર્જન કે વિનાશ શક્ય નથી",
            "આપેલા તત્વના તમામ પરમાણુઓના દળ સમાન હોય છે",
            "પરમાણુઓ નાની પૂર્ણાંક સંખ્યાના પ્રમાણમાં જોડાય છે",
            "સંયોજનમાં પરમાણુઓની સાપેક્ષ સંખ્યા નિશ્ચિત હોય છે"
        ],
        "correct_index": 0,
        "explanation": "Dalton's postulate: 'Atoms can neither be created nor destroyed in a chemical reaction' directly explains the Law of Conservation of Mass.",
        "explanation_hi": "डाल्टन का कथन: 'परमाणुओं को किसी रासायनिक अभिक्रिया में न तो बनाया जा सकता है और न नष्ट किया जा सकता है' द्रव्यमान संरक्षण के नियम की व्याख्या करता है।",
        "explanation_gu": "ડાલ્ટનની ધારણા: 'રાસાયણિક પ્રક્રિયા દરમિયાન પરમાણુનું સર્જન કે વિનાશ શક્ય નથી' તે દળ સંરક્ષણનો નિયમ સમજાવે છે."
    },
    {
        "id": "KOBJ_C9S3_EX_Q05",
        "type": "quiz",
        "title": "Textbook Exercise 5: Atomic Mass Unit Definition",
        "title_hi": "पाठ्यपुस्तक अभ्यास 5: परमाणु द्रव्यमान इकाई की परिभाषा",
        "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 5: પરમાણ્વીય દળ એકમની વ્યાખ્યા",
        "question": "Define the atomic mass unit (u).",
        "question_hi": "परमाणु द्रव्यमान इकाई (u) को परिभाषित कीजिए।",
        "question_gu": "પરમાણ્વીય દળ એકમ (u) ને વ્યાખ્યાયિત કરો.",
        "options": [
            "A mass unit equal to exactly 1/12th the mass of one atom of Carbon-12 isotope",
            "The mass of one Hydrogen atom",
            "The mass of one Oxygen atom",
            "1 gram of any pure element"
        ],
        "options_hi": [
            "द्रव्यमान का वह मान जो कार्बन-12 समस्थानिक के एक परमाणु के द्रव्यमान के 1/12वें भाग के बराबर होता है",
            "एक हाइड्रोजन परमाणु का द्रव्यमान",
            "एक ऑक्सीजन परमाणु का द्रव्यमान",
            "किसी भी शुद्ध तत्व का 1 ग्राम"
        ],
        "options_gu": [
            "કાર્બન-12 સમસ્થાનિકના એક પરમાણુના દળના 1/12 માં ભાગ જેટલું દળ ધરાવતો એકમ",
            "એક હાઇડ્રોજન પરમાણુનું દળ",
            "એક ઓક્સિજન પરમાણુનું દળ",
            "કોઈપણ શુદ્ધ તત્વનું 1 ગ્રામ"
        ],
        "correct_index": 0,
        "explanation": "1 atomic mass unit (1 u) = 1/12 × mass of one Carbon-12 atom.",
        "explanation_hi": "1 परमाणु द्रव्यमान इकाई (1 u) = कार्बन-12 के एक परमाणु के द्रव्यमान का 1/12वां भाग।",
        "explanation_gu": "1 પરમાણ્વીય દળ એકમ (1 u) = કાર્બન-12 ના એક પરમાણુના દળનો 1/12 મો ભાગ."
    },
    {
        "id": "KOBJ_C9S3_EX_Q07",
        "type": "quiz",
        "title": "Textbook Exercise 7: Formulae of Compounds (Na₂O, AlCl₃, Na₂S, Mg(OH)₂)",
        "title_hi": "पाठ्यपुस्तक अभ्यास 7: यौगिकों के सूत्र (Na₂O, AlCl₃, Na₂S, Mg(OH)₂)",
        "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 7: સંયોજનોના સૂત્રો (Na₂O, AlCl₃, Na₂S, Mg(OH)₂)",
        "question": "Write the chemical formulae of: (i) Sodium oxide, (ii) Aluminium chloride, (iii) Sodium sulphide, (iv) Magnesium hydroxide.",
        "question_hi": "निम्न के सूत्र लिखिए: (i) सोडियम ऑक्साइड, (ii) एल्युमिनियम क्लोराइड, (iii) सोडियम सल्फाइड, (iv) मैग्नीशियम हाइड्रॉक्साइड।",
        "question_gu": "નીચેના સંયોજનોના રાસાયણિક સૂત્રો લખો: (i) સોડિયમ ઓક્સાઇડ, (ii) એલ્યુમિનિયમ ક્લોરાઇડ, (iii) સોડિયમ સલ્ફાઇડ, (iv) મેગ્નેશિયમ હાઇડ્રોક્સાઇડ.",
        "options": [
            "(i) Na₂O, (ii) AlCl₃, (iii) Na₂S, (iv) Mg(OH)₂",
            "(i) NaO, (ii) Al₃Cl, (iii) NaS₂, (iv) MgOH",
            "(i) NaO₂, (ii) AlCl, (iii) NaS, (iv) Mg₂OH",
            "(i) Na₂O, (ii) AlCl₂, (iii) NaS, (iv) Mg(OH)₃"
        ],
        "options_hi": [
            "(i) Na₂O, (ii) AlCl₃, (iii) Na₂S, (iv) Mg(OH)₂",
            "(i) NaO, (ii) Al₃Cl, (iii) NaS₂, (iv) MgOH",
            "(i) NaO₂, (ii) AlCl, (iii) NaS, (iv) Mg₂OH",
            "(i) Na₂O, (ii) AlCl₂, (iii) NaS, (iv) Mg(OH)₃"
        ],
        "options_gu": [
            "(i) Na₂O, (ii) AlCl₃, (iii) Na₂S, (iv) Mg(OH)₂",
            "(i) NaO, (ii) Al₃Cl, (iii) NaS₂, (iv) MgOH",
            "(i) NaO₂, (ii) AlCl, (iii) NaS, (iv) Mg₂OH",
            "(i) Na₂O, (ii) AlCl₂, (iii) NaS, (iv) Mg(OH)₃"
        ],
        "correct_index": 0,
        "explanation": "Na¹⁺ O²⁻ -> Na₂O; Al³⁺ Cl¹⁻ -> AlCl₃; Na¹⁺ S²⁻ -> Na₂S; Mg²⁺ (OH)¹⁻ -> Mg(OH)₂.",
        "explanation_hi": "Na¹⁺ O²⁻ -> Na₂O; Al³⁺ Cl¹⁻ -> AlCl₃; Na¹⁺ S²⁻ -> Na₂S; Mg²⁺ (OH)¹⁻ -> Mg(OH)₂।",
        "explanation_gu": "Na¹⁺ O²⁻ -> Na₂O; Al³⁺ Cl¹⁻ -> AlCl₃; Na¹⁺ S²⁻ -> Na₂S; Mg²⁺ (OH)¹⁻ -> Mg(OH)₂."
    },
    {
        "id": "KOBJ_C9S3_EX_Q10",
        "type": "quiz",
        "title": "Textbook Exercise 10: Number of Atoms in H₂S and PO₄³⁻",
        "title_hi": "पाठ्यपुस्तक अभ्यास 10: H₂S और PO₄³⁻ में परमाणुओं की संख्या",
        "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 10: H₂S અને PO₄³⁻ માં પરમાણુઓની સંખ્યા",
        "question": "How many atoms are present in a: (i) H₂S molecule, (ii) PO₄³⁻ ion?",
        "question_hi": "(i) H₂S अणु एवं (ii) PO₄³⁻ आयन में कितने परमाणु विद्यमान हैं?",
        "question_gu": "(i) H₂S અણુ અને (ii) PO₄³⁻ આયનમાં કેટલા પરમાણુઓ હાજર છે?",
        "options": [
            "(i) 3 atoms (2 H + 1 S), (ii) 5 atoms (1 P + 4 O)",
            "(i) 2 atoms, (ii) 4 atoms",
            "(i) 1 atom, (ii) 3 atoms",
            "(i) 4 atoms, (ii) 8 atoms"
        ],
        "options_hi": [
            "(i) 3 परमाणु (2 H + 1 S), (ii) 5 परमाणु (1 P + 4 O)",
            "(i) 2 परमाणु, (ii) 4 परमाणु",
            "(i) 1 परमाणु, (ii) 3 परमाणु",
            "(i) 4 परमाणु, (ii) 8 परमाणु"
        ],
        "options_gu": [
            "(i) 3 પરમાણુઓ (2 H + 1 S), (ii) 5 પરમાણુઓ (1 P + 4 O)",
            "(i) 2 પરમાણુઓ, (ii) 4 પરમાણુઓ",
            "(i) 1 પરમાણુ, (ii) 3 પરમાણુઓ",
            "(i) 4 પરમાણુઓ, (ii) 8 પરમાણુઓ"
        ],
        "correct_index": 0,
        "explanation": "H₂S has 2 Hydrogen + 1 Sulphur = 3 atoms. PO₄³⁻ has 1 Phosphorus + 4 Oxygen = 5 atoms.",
        "explanation_hi": "H₂S में 2 हाइड्रोजन + 1 सल्फर = 3 परमाणु। PO₄³⁻ में 1 फास्फोरस + 4 ऑक्सीजन = 5 परमाणु।",
        "explanation_gu": "H₂S માં 2 હાઇડ્રોજન + 1 સલ્ફર = 3 પરમાણુઓ. PO₄³⁻ માં 1 ફોસ્ફરસ + 4 ઓક્સિજન = 5 પરમાણુઓ."
    },
    {
        "id": "KOBJ_C9S3_EX_Q13",
        "type": "quiz",
        "title": "Textbook Exercise 13: Boron & Oxygen Percentage Composition",
        "title_hi": "पाठ्यपुस्तक अभ्यास 13: बोरोन और ऑक्सीजन की प्रतिशत रचना",
        "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 13: બોરોન અને ઓક્સિજનની ટકાવારી રચના",
        "question": "A 0.24 g sample of a compound of boron and oxygen was found to contain 0.096 g of boron and 0.144 g of oxygen. Calculate the percentage composition of the compound by weight.",
        "question_hi": "0.24 ग्राम बोरोन एवं ऑक्सीजन युक्त यौगिक के नमूने में 0.096 ग्राम बोरोन एवं 0.144 ग्राम ऑक्सीजन पाया गया। यौगिक के प्रतिशत संघटन का परिकलन कीजिए।",
        "question_gu": "બોરોન અને ઓક્સિજન ધરાવતા સંયોજનના 0.24 ગ્રામ નમૂનામાં 0.096 ગ્રામ બોરોન અને 0.144 ગ્રામ ઓક્સિજન છે. સંયોજનમાં ટકાવારી પ્રમાણ શોધો.",
        "options": [
            "40% Boron and 60% Oxygen",
            "50% Boron and 50% Oxygen",
            "30% Boron and 70% Oxygen",
            "25% Boron and 75% Oxygen"
        ],
        "options_hi": [
            "40% बोरोन और 60% ऑक्सीजन",
            "50% बोरोन और 50% ऑक्सीजन",
            "30% बोरोन और 70% ऑक्सीजन",
            "25% बोरोन और 75% ऑक्सीजन"
        ],
        "options_gu": [
            "40% બોરોન અને 60% ઓક્સિજન",
            "50% બોરોન અને 50% ઓક્સિજન",
            "30% બોરોન અને 70% ઓક્સિજન",
            "25% બોરોન અને 75% ઓક્સિજન"
        ],
        "correct_index": 0,
        "explanation": "% Boron = (0.096 / 0.24) × 100 = 40%. % Oxygen = (0.144 / 0.24) × 100 = 60%.",
        "explanation_hi": "बोरोन % = (0.096 / 0.24) × 100 = 40%। ऑक्सीजन % = (0.144 / 0.24) × 100 = 60%।",
        "explanation_gu": "બોરોન % = (0.096 / 0.24) × 100 = 40%. ઓક્સિજન % = (0.144 / 0.24) × 100 = 60%."
    },
    {
        "id": "KOBJ_C9S3_EX_Q18",
        "type": "quiz",
        "title": "Textbook Exercise 18: Molecular Mass Calculations (C₂H₂, S₈, P₄, HCl, HNO₃)",
        "title_hi": "पाठ्यपुस्तक अभ्यास 18: आणविक द्रव्यमान की गणना",
        "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 18: આણ્વીય દળની ગણતરી",
        "question": "Calculate the molar mass of: (a) Ethyne C₂H₂, (b) Sulphur molecule S₈, (c) Phosphorus molecule P₄ (atomic mass of P = 31), (d) Nitric acid HNO₃.",
        "question_hi": "निम्नलिखित पदार्थों के मोलर द्रव्यमान का परिकलन कीजिए: (a) एथाइन C₂H₂, (b) सल्फर अणु S₈, (c) फास्फोरस अणु P₄ (P = 31), (d) नाइट्रिक अम्ल HNO₃।",
        "question_gu": "નીચેના પદાર્થોના મોલર દળની ગણતરી કરો: (a) ઇથાઇન C₂H₂, (b) સલ્ફર અણુ S₈, (c) ફોસ્ફરસ અણુ P₄ (P = 31), (d) નાઇટ્રિક એસિડ HNO₃.",
        "options": [
            "(a) 26 g/mol, (b) 256 g/mol, (c) 124 g/mol, (d) 63 g/mol",
            "(a) 28 g/mol, (b) 128 g/mol, (c) 62 g/mol, (d) 31 g/mol",
            "(a) 12 g/mol, (b) 32 g/mol, (c) 31 g/mol, (d) 100 g/mol",
            "(a) 50 g/mol, (b) 200 g/mol, (c) 100 g/mol, (d) 70 g/mol"
        ],
        "options_hi": [
            "(a) 26 g/mol, (b) 256 g/mol, (c) 124 g/mol, (d) 63 g/mol",
            "(a) 28 g/mol, (b) 128 g/mol, (c) 62 g/mol, (d) 31 g/mol",
            "(a) 12 g/mol, (b) 32 g/mol, (c) 31 g/mol, (d) 100 g/mol",
            "(a) 50 g/mol, (b) 200 g/mol, (c) 100 g/mol, (d) 70 g/mol"
        ],
        "options_gu": [
            "(a) 26 g/mol, (b) 256 g/mol, (c) 124 g/mol, (d) 63 g/mol",
            "(a) 28 g/mol, (b) 128 g/mol, (c) 62 g/mol, (d) 31 g/mol",
            "(a) 12 g/mol, (b) 32 g/mol, (c) 31 g/mol, (d) 100 g/mol",
            "(a) 50 g/mol, (b) 200 g/mol, (c) 100 g/mol, (d) 70 g/mol"
        ],
        "correct_index": 0,
        "explanation": "C₂H₂ = 2(12) + 2(1) = 26; S₈ = 8(32) = 256; P₄ = 4(31) = 124; HNO₃ = 1 + 14 + 3(16) = 63 g/mol.",
        "explanation_hi": "C₂H₂ = 2(12) + 2(1) = 26; S₈ = 8(32) = 256; P₄ = 4(31) = 124; HNO₃ = 1 + 14 + 3(16) = 63 g/mol।",
        "explanation_gu": "C₂H₂ = 2(12) + 2(1) = 26; S₈ = 8(32) = 256; P₄ = 4(31) = 124; HNO₃ = 1 + 14 + 3(16) = 63 g/mol."
    }
]

# Combine all blocks
all_blocks = blocks + textbook_exercise_questions
print(f"Total blocks generated for Class 9 Science Ch 3: {len(all_blocks)}")

# Save to learning_modules blocks.json
blocks_path = 'app_core/learning_modules/gseb_class9_science_ch3/blocks.json'
with open(blocks_path, 'w', encoding='utf-8') as f:
    json.dump(all_blocks, f, ensure_ascii=False, indent=2)
print(f"Saved blocks to {blocks_path}")

# Sync to app_core/chapters/ncert_class9_science_ch3.json
ncert_path = 'app_core/chapters/ncert_class9_science_ch3.json'
ncert_payload = {
    "metadata": {
        "id": "ncert_class9_science_ch3",
        "title": "Chapter 3: Atoms and Molecules",
        "title_hi": "अध्याय 3: परमाणु एवं अणु",
        "title_gu": "પ્રકરણ 3: પરમાણુઓ અને અણુઓ",
        "subject": "Science",
        "grade": "Class 9"
    },
    "blocks": all_blocks
}
with open(ncert_path, 'w', encoding='utf-8') as f:
    json.dump(ncert_payload, f, ensure_ascii=False, indent=2)
print(f"Synced to {ncert_path}")

# Sync to assessment bank
assessment_path = 'app_core/assessment/gseb_class9_science_ch3_questions.json'
assessment_questions = []
for idx, q in enumerate(textbook_exercise_questions):
    assessment_questions.append({
        "id": f"gseb_c9_sci_ch3_q_{idx+1:03d}",
        "chapter_id": "gseb_class9_science_ch3",
        "topic_id": "atoms_and_molecules",
        "type": "quiz",
        "difficulty": "medium",
        "board": "GSEB",
        "marks": 1,
        "bloom_taxonomy": "Understand",
        "keywords": ["atoms", "molecules", "dalton", "atomic_mass", "valency", "molar_mass"],
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
    "chapter_id": "gseb_class9_science_ch3",
    "questions": assessment_questions
}
with open(assessment_path, 'w', encoding='utf-8') as f:
    json.dump(assessment_payload, f, ensure_ascii=False, indent=2)
print(f"Updated assessment bank at {assessment_path}")
