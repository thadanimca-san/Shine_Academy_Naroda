import json
import os

def build_ncert_class10_science_ch4():
    chapter_id = "ncert_class10_science_ch4"

    metadata = {
        "id": chapter_id,
        "title": "Chapter 4: Carbon and its Compounds",
        "title_hi": "अध्याय 4: कार्बन एवं उसके यौगिक",
        "title_gu": "પ્રકરણ 4: કાર્બન અને તેના સંયોજનો",
        "subject": "Science",
        "grade": "10",
        "board": "NCERT/CBSE/GSEB",
        "curriculum": ["NCERT", "CBSE", "GSEB"],
        "language": "Trilingual (English/Hindi/Gujarati)",
        "difficulty": "Intermediate",
        "estimated_minutes": 240,
        "version": "2.0.0-GOLD-STANDARD",
        "author": "Chief Academic Architect - Antigravity",
        "reviewed_by": "Gold Pedagogy Standard Review Board",
        "tags": [
            "carbon",
            "covalent_bond",
            "tetravalency",
            "catenation",
            "allotropes",
            "diamond",
            "graphite",
            "fullerene",
            "hydrocarbons",
            "alkanes",
            "alkenes",
            "alkynes",
            "isomers",
            "homologous_series",
            "functional_groups",
            "nomenclature",
            "combustion",
            "oxidation",
            "addition_reaction",
            "substitution_reaction",
            "ethanol",
            "ethanoic_acid",
            "esterification",
            "saponification",
            "soaps",
            "detergents",
            "micelles"
        ],
        "learning_outcomes": [
            "Explain covalent bonding in carbon and why carbon cannot form C4+ or C4- ionic species.",
            "Describe the allotropes of carbon (diamond, graphite, fullerene C60) and relate structures to physical properties.",
            "Understand catenation, tetravalency, saturated vs unsaturated hydrocarbons, and structural isomerism.",
            "Identify heteroatoms, functional groups, and calculate properties across homologous series.",
            "Master IUPAC nomenclature for alkanes, alkenes, alkynes, haloalkanes, alcohols, aldehydes, ketones, and carboxylic acids.",
            "Formulate and balance chemical reactions of carbon compounds: combustion, oxidation, addition (hydrogenation), and substitution.",
            "Analyze properties and reactions of Ethanol and Ethanoic acid (esterification, saponification, reaction with carbonates).",
            "Explain micelle formation, cleansing action of soap, scum formation in hard water, and synthetic detergents.",
            "Master every NCERT in-text question and textbook exercise question with trilingual solutions."
        ],
        "ai_context": {
            "learning_goal": "Master NCERT Class 10 Chapter 4 (Carbon and its Compounds) through the 8-Step Gold Pedagogy Arc.",
            "common_misconceptions": [
                "Students confuse structural isomers with bent conformations of the same chain.",
                "Students confuse aldehydes (-al) with alcohols (-ol) in nomenclature.",
                "Students believe soap forms micelles in all solvents; micelles only form in polar solvents like water, not in ethanol.",
                "Students confuse addition reactions (unsaturated) with substitution reactions (saturated)."
            ],
            "tutor_hint": "Always emphasize the electron sharing diagrams and functional group suffixes."
        }
    }

    blocks = []
    block_counter = 1

    def next_id():
        nonlocal block_counter
        bid = f"KOBJ_NCERT_C10_SCI_CH4_{block_counter:03d}"
        block_counter += 1
        return bid

    # =========================================================================
    # MODULE 1: BONDING IN CARBON & ALLOTROPES (8-STEP PEDAGOGY)
    # =========================================================================

    # 1. Hook
    blocks.append({
        "id": next_id(),
        "type": "hook",
        "title": "The Miracle Element of Life",
        "title_hi": "जीवन का अद्भुत तत्व",
        "title_gu": "જીવનનું અદ્ભુત તત્વ",
        "body": "Look around you: your clothes, medicines, books, food, and even your own body are all made of compounds of a single element — Carbon! Despite making up less than 0.03% of Earth's crust and atmosphere, carbon forms millions of unique compounds. How can one single element be the backbone of almost everything on Earth?",
        "body_hi": "अपने चारों ओर देखिए: आपके कपड़े, दवाएं, पुस्तकें, भोजन और आपका अपना शरीर भी केवल एक तत्व — कार्बन के यौगिकों से बने हैं! पृथ्वी की पपड़ी और वायुमंडल में 0.03% से भी कम मात्रा होने के बावजूद, कार्बन लाखों विशिष्ट यौगिक बनाता है। एक अकेला तत्व पृथ्वी की लगभग हर चीज़ का आधार कैसे हो सकता है?",
        "body_gu": "તમારી આસપાસ જુઓ: તમારા કપડાં, દવાઓ, પુસ્તકો, ખોરાક અને તમારું પોતાનું શરીર પણ એક જ તત્વ — કાર્બનના સંયોજનોથી બનેલું છે! પૃથ્વીના પોપડા અને વાતાવરણમાં 0.03% કરતાં પણ ઓછું પ્રમાણ હોવા છતાં, કાર્બન લાખો વિશિષ્ટ સંયોજનો બનાવે છે. એક જ તત્વ પૃથ્વી પરની લગભગ દરેક વસ્તુનો આધાર કેવી રીતે બની શકે?"
    })

    # 2. Socratic Question
    blocks.append({
        "id": next_id(),
        "type": "socratic_question",
        "question": "Carbon has atomic number 6 (electronic configuration 2,4). To gain stability, why doesn't carbon simply lose 4 electrons to form C4+ or gain 4 electrons to form C4-?",
        "question_hi": "कार्बन की परमाणु संख्या 6 है (इलेक्ट्रॉनिक विन्यास 2,4)। स्थिरता प्राप्त करने के लिए, कार्बन C4+ बनाने के लिए 4 इलेक्ट्रॉन क्यों नहीं खोता या C4- बनाने के लिए 4 इलेक्ट्रॉन क्यों नहीं प्राप्त करता?",
        "question_gu": "કાર્બનનો પરમાણુ ક્રમાંક 6 છે (ઇલેક્ટ્રોન રચના 2,4). સ્થિરતા મેળવવા માટે, કાર્બન C4+ બનાવવા માટે 4 ઇલેક્ટ્રોન શા માટે ગુમાવતો નથી અથવા C4- બનાવવા માટે 4 ઇલેક્ટ્રોન શા માટે મેળવતો નથી?",
        "options": [
            "Losing 4 electrons requires massive energy; holding 10 electrons by 6 protons is extremely unstable.",
            "Carbon is a noble gas and does not form any bonds.",
            "Carbon only bonds with metals through ionic bonds.",
            "Carbon's nucleus has no protons to attract electrons."
        ],
        "options_hi": [
            "4 इलेक्ट्रॉन खोने के लिए अत्यधिक ऊर्जा की आवश्यकता होती है; 6 प्रोटॉन द्वारा 10 इलेक्ट्रॉनों को पकड़ना अत्यधिक अस्थिर है।",
            "कार्बन एक उत्कृष्ट गैस है और कोई बंध नहीं बनाता है।",
            "कार्बन केवल आयनिक बंधों के माध्यम से धातुओं के साथ जुड़ता है।",
            "कार्बन के नाभिक में इलेक्ट्रॉनों को आकर्षित करने के लिए कोई प्रोटॉन नहीं होते हैं।"
        ],
        "options_gu": [
            "4 ઇલેક્ટ્રોન ગુમાવવા માટે વિશાળ ઉર્જાની જરૂર પડે છે; 6 પ્રોટોન દ્વારા 10 ઇલેક્ટ્રોન પકડી રાખવા અત્યંત અસ્થિર છે.",
            "કાર્બન નિષ્ક્રિય વાયુ છે અને કોઈ બંધ બનાવતો નથી.",
            "કાર્બન માત્ર અયાનિક બંધ વડે ધાતુઓ સાથે જોડાય છે.",
            "કાર્બનના કેન્દ્રમાં ઇલેક્ટ્રોનને આકર્ષવા માટે કોઈ પ્રોટોન નથી."
        ],
        "correct_index": 0,
        "explanation": "If carbon gains 4 electrons (C4-), it is hard for 6 protons to hold 10 electrons. If it loses 4 electrons (C4+), it requires a huge amount of energy to remove 4 electrons. Hence, carbon SHARES valence electrons to form covalent bonds!",
        "explanation_hi": "यदि कार्बन 4 इलेक्ट्रॉन प्राप्त करता है (C4-), तो 6 प्रोटॉन के लिए 10 इलेक्ट्रॉनों को पकड़ना कठिन होता है। यदि यह 4 इलेक्ट्रॉन खो देता है (C4+), तो 4 इलेक्ट्रॉनों को निकालने के लिए भारी मात्रा में ऊर्जा की आवश्यकता होती है। इसलिए, कार्बन सहसंयोजक बंध बनाने के लिए वैलेंस इलेक्ट्रॉनों को साझा (SHARE) करता है!",
        "explanation_gu": "જો કાર્બન 4 ઇલેક્ટ્રોન મેળવે (C4-), તો 6 પ્રોટોન માટે 10 ઇલેક્ટ્રોન પકડી રાખવું મુશ્કેલ છે. જો તે 4 ઇલેક્ટ્રોન ગુમાવે (C4+), તો 4 ઇલેક્ટ્રોન દૂર કરવા માટે પ્રચંડ ઉર્જાની જરૂર પડે છે. આથી, કાર્બન સહસંયોજક બંધ બનાવવા માટે ઇલેક્ટ્રોનની ભાગીદારી (SHARE) કરે છે!"
    })

    # 3. Discovery
    blocks.append({
        "id": next_id(),
        "type": "discovery",
        "title": "Covalent Bonds & Electron Dot Structures",
        "title_hi": "सहसंयोजक बंध और इलेक्ट्रॉन बिंदु संरचनाएं",
        "title_gu": "સહસંયોજક બંધ અને ઇલેક્ટ્રોન બિંદુ રચનાઓ",
        "body": "A bond formed by the sharing of an electron pair between two atoms is known as a COVALENT BOND.\n• Single Covalent Bond: Sharing 1 pair of electrons (e.g., H2: H-H; CH4: Methane with 4 single C-H bonds; Cl2, H2O, NH3).\n• Double Covalent Bond: Sharing 2 pairs of electrons (e.g., O2: O=O; CO2: O=C=O; C2H4: Ethene).\n• Triple Covalent Bond: Sharing 3 pairs of electrons (e.g., N2: N≡N; C2H2: Ethyne).\n\nProperties of Covalent Compounds:\n1. Low melting and boiling points because inter-molecular forces are weak (bonds within the molecule are strong, but forces between molecules are weak).\n2. Poor conductors of electricity because no free ions or free electrons are present.",
        "body_hi": "दो परमाणुओं के बीच एक इलेक्ट्रॉन युग्म के साझा करने से बनने वाले बंध को सहसंयोजक बंध (Covalent Bond) कहते हैं।\n• एकल सहसंयोजक बंध: 1 इलेक्ट्रॉन युग्म की साझेदारी (जैसे H2: H-H; CH4: मीथेन में 4 एकल C-H बंध; Cl2, H2O, NH3)।\n• द्वि सहसंयोजक बंध: 2 इलेक्ट्रॉन युग्मों की साझेदारी (जैसे O2: O=O; CO2: O=C=O; C2H4: एथीन)।\n• त्रि सहसंयोजक बंध: 3 इलेक्ट्रॉन युग्मों की साझेदारी (जैसे N2: N≡N; C2H2: एथाइन)।\n\nसहसंयोजक यौगिकों के गुण:\n1. निम्न गलनांक और क्वथनांक, क्योंकि अंतरा-आण्विक बल बहुत कमजोर होते हैं।\n2. विद्युत के दुर्बल चालक या कुचालक, क्योंकि इनमें कोई मुक्त आयन या इलेक्ट्रॉन नहीं होते हैं।",
        "body_gu": "બે પરમાણુઓ વચ્ચે ઇલેક્ટ્રોન યુગ્મની ભાગીદારીથી રચાતા બંધને સહસંયોજક બંધ કહે છે.\n• એકલ સહસંયોજક બંધ: 1 ઇલેક્ટ્રોન યુગ્મની ભાગીદારી (જેમ કે H2, CH4 - મિથેન, Cl2, H2O, NH3).\n• દ્વિ સહસંયોજક બંધ: 2 ઇલેક્ટ્રોન યુગ્મની ભાગીદારી (જેમ કે O2, CO2, C2H4 - ઇથીન).\n• ત્રિ સહસંયોજક બંધ: 3 ઇલેક્ટ્રોન યુગ્મની ભાગીદારી (જેમ કે N2, C2H2 - ઇથાઇન).\n\nસહસંયોજક સંયોજનોના ગુણધર્મો:\n1. નીચા ગલનબિંદુ અને ઉત્કલનબિંદુ, કારણ કે આંતર-આણ્વીય આકર્ષણ બળ નબળું હોય છે.\n2. વિદ્યુતના મંદ વાહક કે અવાહક, કારણ કે તેમાં મુક્ત આયનો કે ઇલેક્ટ્રોન હોતા નથી."
    })

    # 4. Theory
    blocks.append({
        "id": next_id(),
        "type": "theory",
        "title": "Allotropes of Carbon: Diamond, Graphite, and Fullerenes",
        "title_hi": "कार्बन के अपररूप: हीरा, ग्रेफाइट और फुलरीन",
        "title_gu": "કાર્બનના બહુરૂપો: હીરો, ગ્રેફાઇટ અને ફુલરીન",
        "body": "Allotropy is the property by which an element exists in more than one physical form having different physical properties but identical chemical properties.\n\n1. DIAMOND:\n• Each carbon atom is bonded to 4 other carbon atoms forming a rigid, three-dimensional tetrahedral network.\n• Hardest natural substance known; has very high melting point.\n• Poor conductor of electricity (all 4 valence electrons are tightly bonded, no free electrons).\n• Uses: Cutting glass and rock drills, precious jewellery.\n\n2. GRAPHITE:\n• Each carbon atom is bonded to 3 other carbon atoms in the same plane, forming hexagonal planar layers.\n• Layers are held by weak van der Waals forces, allowing them to slide over one another (slippery and smooth to touch).\n• Good conductor of electricity because one valence electron per carbon remains delocalized/free.\n• Uses: Lubricant in high-temperature machines, pencil leads, battery electrodes.\n\n3. FULLERENES:\n• Carbon atoms arranged in the shape of a football (cage-like sphere).\n• Buckminsterfullerene (C60) is the first identified fullerene, named after architect Buckminster Fuller.",
        "body_hi": "अपररूपता वह गुण है जिसके द्वारा कोई तत्व विभिन्न भौतिक रूपों में मौजूद होता है जिनके भौतिक गुण भिन्न लेकिन रासायनिक गुण समान होते हैं।\n\n1. हीरा (Diamond):\n• प्रत्येक कार्बन परमाणु 4 अन्य कार्बन परमाणुओं से जुड़कर एक दृढ़ 3-आयामी चतुष्फलकीय संरचना बनाता है।\n• ज्ञात सबसे कठोर प्राकृतिक पदार्थ; अत्यधिक उच्च गलनांक।\n• विद्युत का कुचालक (सभी 4 संयोजी इलेक्ट्रॉन बंधे होते हैं, कोई मुक्त इलेक्ट्रॉन नहीं)।\n• उपयोग: कांच काटने और चट्टानों में छेद करने वाले ड्रिल, आभूषण।\n\n2. ग्रेफाइट (Graphite):\n• प्रत्येक कार्बन परमाणु उसी तल में 3 अन्य कार्बन परमाणुओं से जुड़ा होता है, जिससे षट्कोणीय परतें बनती हैं।\n• परतें कमजोर बलों द्वारा जुड़ी होती हैं, जिससे वे एक-दूसरे पर फिसल सकती हैं (चिकना और फिसलन भरा स्पर्श)।\n• विद्युत का सुचालक क्योंकि प्रत्येक कार्बन का एक संयोजी इलेक्ट्रॉन मुक्त रहता है।\n• उपयोग: उच्च तापमान स्नेहक, पेंसिल लेड, इलेक्ट्रोड।\n\n3. फुलरीन (Fullerene):\n• फुटबॉल के आकार में व्यवस्थित कार्बन परमाणु। बकमिंस्टरफुलरीन (C60) पहला खोजा गया फुलरीन है।",
        "body_gu": "અપરરૂપતા એવો ગુણધર્મ છે જેમાં કોઈ તત્વ વિવિધ ભૌતિક સ્વરૂપોમાં અસ્તિત્વ ધરાવે છે, જેના ભૌતિક ગુણધર્મો જુદા પરંતુ રાસાયણિક ગુણધર્મો સમાન હોય છે.\n\n1. હીરો (Diamond):\n• દરેક કાર્બન પરમાણુ અન્ય 4 કાર્બન સાથે જોડાઈને ત્રિ-પરિમાણીય ચતુષ્ફલકીય જાળીદાર રચના બનાવે છે.\n• કુદરતનો સૌથી સખત પદાર્થ; ખૂબ ઊંચું ગલનબિંદુ.\n• વિદ્યુતનું અવાહક (કોઈ મુક્ત ઇલેક્ટ્રોન નથી).\n• ઉપયોગ: કાચ કાપવા, ખડકો ડ્રિલ કરવા, ઘરેણાં.\n\n2. ગ્રેફાઇટ (Graphite):\n• દરેક કાર્બન પરમાણુ અન્ય 3 કાર્બન સાથે જોડાઈને ષટ્કોણીય સ્તરો બનાવે છે.\n• સ્તરો એકબીજા પર સરકી શકે છે (ચીકણો અને નરમ સ્પર્શ).\n• વિદ્યુતનું ઉત્તમ સુવાહક કારણ કે દરેક કાર્બન પાસે એક મુક્ત ઇલેક્ટ્રોન હોય છે.\n• ઉપયોગ: ઊંજણ (લુબ્રિકન્ટ), પેન્સિલની અણી, બેટરીના ઇલેક્ટ્રોડ.\n\n3. ફુલરીન (Fullerene):\n• ફૂટબોલ આકારના ગોળાકાર અણુઓ. બકમિનિસ્ટર ફુલરીન (C60) સૌથી જાણીતું સ્વરૂપ છે."
    })

    # Teacher Tip
    blocks.append({
        "id": next_id(),
        "type": "teacher_tip",
        "title": "Teacher Tip: Why Graphite Conducts While Diamond Doesn't",
        "title_hi": "शिक्षक टिप: ग्रेफाइट विद्युत का चालक क्यों है जबकि हीरा कुचालक है?",
        "title_gu": "શિક્ષક ટિપ: ગ્રેફાઇટ વિદ્યુતનું વાહક શા માટે છે જ્યારે હીરો અવાહક છે?",
        "body": "Carbon has 4 valence electrons. In diamond, all 4 electrons form rigid covalent bonds with 4 neighbors (no free electrons -> insulator). In graphite, only 3 electrons form bonds in the hexagonal sheet, leaving the 4th electron free to move across the layer (mobile electrons -> conductor). This exact question appears frequently in board exams!",
        "body_hi": "कार्बन में 4 संयोजी इलेक्ट्रॉन होते हैं। हीरे में, सभी 4 इलेक्ट्रॉन 4 पड़ोसियों के साथ दृढ़ सहसंयोजक बंध बनाते हैं (कोई मुक्त इलेक्ट्रॉन नहीं -> कुचालक)। ग्रेफाइट में, केवल 3 इलेक्ट्रॉन बंध बनाते हैं, जिससे चौथा इलेक्ट्रॉन परत पर घूमने के लिए स्वतंत्र रहता है (गतिशील इलेक्ट्रॉन -> सुचालक)। यह प्रश्न बोर्ड परीक्षा में बार-बार पूछा जाता है!",
        "body_gu": "કાર્બન પાસે 4 સંયોજકતા ઇલેક્ટ્રોન હોય છે. હીરામાં ચારેય ઇલેક્ટ્રોન બંધ બનાવવામાં વપરાય છે (કોઈ મુક્ત ઇલેક્ટ્રોન ન હોવાથી અવાહક). ગ્રેફાઇટમાં માત્ર 3 ઇલેક્ટ્રોન બંધ બનાવે છે, જેથી ચોથો ઇલેક્ટ્રોન મુક્ત રહે છે (મુક્ત ઇલેક્ટ્રોનને લીધે સુવાહક). બોર્ડ પરીક્ષા માટે આ પ્રશ્ન ખૂબ મહત્વનો છે!"
    })

    # Common Mistake
    blocks.append({
        "id": next_id(),
        "type": "teacher_tip",
        "title": "Common Mistake: Confusing Covalent Bonds with Inter-Molecular Forces",
        "title_hi": "सामान्य गलती: सहसंयोजक बंधों को अंतरा-आण्विक बलों के साथ भ्रमित करना",
        "title_gu": "સામાન્ય ભૂલ: સહસંયોજક બંધ અને આંતર-આણ્વીય બળો વચ્ચેની ગેરસમજ",
        "body": "Students often write: 'Covalent compounds have low melting points because covalent bonds are weak.' This is FALSE! Covalent bonds inside the molecule are extremely strong. However, the attractive forces BETWEEN separate molecules (intermolecular forces) are weak, so little heat is needed to separate them.",
        "body_hi": "छात्र अक्सर लिखते हैं: 'सहसंयोजक यौगिकों का गलनांक कम होता है क्योंकि सहसंयोजक बंध कमजोर होते हैं।' यह गलत है! अणु के अंदर सहसंयोजक बंध बहुत मजबूत होते हैं। हालांकि, अलग-अलग अणुओं के बीच आकर्षण बल (अंतरा-आण्विक बल) कमजोर होते हैं, इसलिए उन्हें अलग करने के लिए कम ऊष्मा की आवश्यकता होती है।",
        "body_gu": "વિદ્યાર્થીઓ ઘણીવાર લખે છે: 'સહસંયોજક સંયોજનોના ગલનબિંદુ નીચા હોય છે કારણ કે સહસંયોજક બંધ નબળા હોય છે.' આ વિધાન ખોટું છે! અણુની અંદરના સહસંયોજક બંધ અતિ મજબૂત હોય છે, પરંતુ અણુ-અણુ વચ્ચેના આંતર-આણ્વીય આકર્ષણ બળો નબળા હોવાથી ઓછી ગરમીથી છૂટા પડી જાય છે."
    })

    # 5. Knowledge Check
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "Which of the following allotropes of carbon is a good conductor of electricity?",
        "question_hi": "कार्बन का निम्नलिखित में से कौन सा अपररूप विद्युत का अच्छा सुचालक है?",
        "question_gu": "કાર્બનનું નીચેનામાંથી કયું બહુરૂપ વિદ્યુતનું ઉત્તમ સુવાહક છે?",
        "options": [
            "Graphite",
            "Diamond",
            "Buckminsterfullerene",
            "Charcoal"
        ],
        "options_hi": [
            "ग्रेफाइट",
            "हीरा",
            "बकमिंस्टरफुलरीन",
            "काठकोयला (चारकोल)"
        ],
        "options_gu": [
            "ગ્રેફાઇટ",
            "હીરો",
            "બકમિનિસ્ટર ફુલરીન",
            "ચારકોલ"
        ],
        "correct_index": 0,
        "explanation": "In graphite, each carbon atom is bonded to only three other carbon atoms in hexagonal layers, leaving one free valence electron per atom that moves freely, conducting electricity.",
        "explanation_hi": "ग्रेफाइट में, प्रत्येक कार्बन परमाणु षट्कोणीय परतों में केवल तीन अन्य कार्बन परमाणुओं से बंधा होता है, जिससे प्रति परमाणु एक मुक्त संयोजी इलेक्ट्रॉन बचता है जो स्वतंत्र रूप से घूमता है और बिजली का संचालन करता है।",
        "explanation_gu": "ગ્રેફાઇટમાં દરેક કાર્બન અન્ય ત્રણ કાર્બન સાથે જોડાયેલ હોવાથી ચોથો ઇલેક્ટ્રોન મુક્ત રહે છે, જે વિદ્યુતનું વહન કરે છે."
    })

    # 6. Reflection
    blocks.append({
        "id": next_id(),
        "type": "reflection",
        "title": "Why Did Nature Base Life on Carbon?",
        "title_hi": "प्रकृति ने जीवन को कार्बन पर आधारित क्यों बनाया?",
        "title_gu": "કુદરતે જીવનનો આધાર કાર્બન પર શા માટે રાખ્યો?",
        "body": "Silicon is also tetravalent and right below carbon in the periodic table. Yet life is based on carbon, not silicon. Why? Carbon-carbon bonds are exceptionally strong and stable because carbon's small nucleus holds shared electrons tightly. Silicon-silicon bonds are much weaker and highly reactive towards oxygen and water, making giant stable biomolecules like DNA and proteins impossible.",
        "body_hi": "सिलिकॉन भी चतुःसंयोजी है और आवर्त सारणी में कार्बन के ठीक नीचे है। फिर भी जीवन सिलिकॉन पर नहीं बल्कि कार्बन पर आधारित है। क्यों? कार्बन-कार्बन बंध असाधारण रूप से मजबूत और स्थिर होते हैं क्योंकि कार्बन का छोटा नाभिक साझा इलेक्ट्रॉनों को मजबूती से पकड़ता है। सिलिकॉन-सिलिकॉन बंध बहुत कमजोर होते हैं, जिससे डीएनए और प्रोटीन जैसे विशाल स्थिर जैव-अणु बनाना असंभव है।",
        "body_gu": "સિલિકોન પણ ચતુઃસંયોજક છે અને આવર્ત કોષ્ટકમાં કાર્બનની બરાબર નીચે છે. છતાં જીવન કાર્બન પર આધારિત છે, સિલિકોન પર નહિ. શા માટે? કાર્બન-કાર્બન બંધ અત્યંત મજબૂત અને સ્થિર હોય છે કારણ કે કાર્બનનું નાનું કેન્દ્ર ઇલેક્ટ્રોનને મજબૂતીથી પકડી રાખે છે. સિલિકોન-સિલિકોન બંધ નબળા હોવાથી DNA જેવા જટિલ અણુઓ બની શકતા નથી."
    })

    # 7. Connection
    blocks.append({
        "id": next_id(),
        "type": "connection",
        "title": "From Ancient Charcoal to Modern Nanotechnology",
        "title_hi": "प्राचीन कोयले से लेकर आधुनिक नैनोटेक्नोलॉजी तक",
        "title_gu": "પ્રાચીન કોલસાથી લઈને આધુનિક નેનોટેકનોલોજી સુધી",
        "body": "The same carbon atom that forms brittle charcoal also forms diamond, graphene (single atomic layer of graphite 200 times stronger than steel), and carbon nanotubes. Understanding carbon bonding has revolutionized materials science, aerospace, and medical drug delivery.",
        "body_hi": "वही कार्बन परमाणु जो भंगुर चारकोल बनाता है, हीरा, ग्राफीन (स्टील से 200 गुना मजबूत ग्रेफाइट की एकल परमाणु परत) और कार्बन नैनोट्यूब भी बनाता है। कार्बन बॉन्डिंग को समझने से सामग्री विज्ञान, एयरोस्पेस और चिकित्सा में क्रांति आई है।",
        "body_gu": "જે કાર્બન પરમાણુ બરડ કોલસો બનાવે છે, તે જ હીરો, ગ્રાફીન (સ્ટીલ કરતાં 200 ગણું મજબૂત ગ્રેફાઇટનું સ્તર) અને કાર્બન નેનોટ્યુબ પણ બનાવે છે. કાર્બન બંધારણની સમજથી નેનોટેકનોલોજી અને એરોસ્પેસ ક્ષેત્રે ક્રાંતિ આવી છે."
    })

    # 8. Mastery Challenge
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "Carbon forms a large number of compounds due to its small size and tetravalency. What enables carbon to form exceptionally strong covalent bonds?",
        "question_hi": "कार्बन अपने छोटे आकार और चतुःसंयोजकता के कारण बड़ी संख्या में यौगिक बनाता है। कार्बन को असाधारण रूप से मजबूत सहसंयोजक बंध बनाने में क्या सक्षम बनाता है?",
        "question_gu": "કાર્બન તેના નાના કદ અને ચતુઃસંયોજકતાને કારણે વિશાળ સંખ્યામાં સંયોજનો બનાવે છે. કયું પરિબળ કાર્બનને અત્યંત મજબૂત સહસંયોજક બંધ બનાવવામાં મદદ કરે છે?",
        "options": [
            "Its small atomic radius allows the nucleus to hold shared pairs of electrons firmly.",
            "Its large atomic radius allows electrons to move freely.",
            "Its ability to form ionic bonds with noble gases.",
            "Its tendency to gain four electrons easily to become C4-."
        ],
        "options_hi": [
            "इसकी छोटी परमाणु त्रिज्या नाभिक को साझा इलेक्ट्रॉन जोड़े को मजबूती से पकड़ने की अनुमति देती है।",
            "इसकी बड़ी परमाणु त्रिज्या इलेक्ट्रॉनों को स्वतंत्र रूप से घूमने देती है।",
            "उत्कृष्ट गैसों के साथ आयनिक बंध बनाने की इसकी क्षमता।",
            "C4- बनने के लिए आसानी से चार इलेक्ट्रॉन प्राप्त करने की इसकी प्रवृत्ति।"
        ],
        "options_gu": [
            "તેની નાની પરમાણ્વીય ત્રિજ્યા કેન્દ્રને ભાગીદારી પામેલા ઇલેક્ટ્રોન યુગ્મને મજબૂતીથી જકડી રાખવા દે છે.",
            "તેની મોટી પરમાણ્વીય ત્રિજ્યા.",
            "નિષ્ક્રિય વાયુઓ સાથે આયનિક બંધ બનાવવાની ક્ષમતા.",
            "સરળતાથી C4- આયન બનાવવાની વૃત્તિ."
        ],
        "correct_index": 0,
        "explanation": "Because carbon has a very small atomic size, its positively charged nucleus is very close to the shared electron pairs, holding them with immense electrostatic attraction, making C-C and C-H bonds exceptionally stable.",
        "explanation_hi": "क्योंकि कार्बन का परमाणु आकार बहुत छोटा होता है, इसलिए इसका धनावेशित नाभिक साझा इलेक्ट्रॉन युग्मों के बहुत करीब होता है, जिससे वे अत्यधिक आकर्षण के साथ बंधे रहते हैं और बंध बहुत स्थिर होते हैं।",
        "explanation_gu": "કાર્બનનું કદ ખૂબ નાનું હોવાથી તેનું કેન્દ્ર ભાગીદારી પામેલા ઇલેક્ટ્રોન યુગ્મની નજીક રહે છે અને પ્રબળ આકર્ષણથી જકડી રાખે છે, જેથી બંધ ખૂબ સ્થિર બને છે."
    })

    # =========================================================================
    # MODULE 2: VERSATILE NATURE OF CARBON & ISOMERISM (8-STEP PEDAGOGY)
    # =========================================================================

    # 1. Hook
    blocks.append({
        "id": next_id(),
        "type": "hook",
        "title": "The Endless Chain Maker",
        "title_hi": "अनंत श्रृंखला बनाने वाला जादूगर",
        "title_gu": "અનંત શૃંખલા બનાવનાર જાદુગર",
        "body": "Imagine toy building blocks that can snap together to form straight chains, branched trees, closed rings, and intricate cages without ever collapsing. Carbon is nature's ultimate Lego brick! While other elements rarely link more than 7 or 8 atoms together, carbon atoms can link by the hundreds and thousands. Why does carbon have this extraordinary power?",
        "body_hi": "कल्पना कीजिए ऐसे खिलौनों के ब्लॉकों की जो एक साथ जुड़कर सीधी श्रृंखलाएं, शाखित पेड़, बंद वलय और जटिल पिंजरे बना सकते हैं और कभी टूटते नहीं। कार्बन प्रकृति का सर्वोत्तम लेगो ब्लॉक है! जबकि अन्य तत्व शायद ही कभी 7 या 8 परमाणुओं से अधिक जोड़ पाते हैं, कार्बन परमाणु सैकड़ों और हजारों की संख्या में जुड़ सकते हैं। कार्बन के पास यह असाधारण शक्ति क्यों है?",
        "body_gu": "કલ્પના કરો એવા રમકડાના બ્લોક્સની જે સીધી શૃંખલાઓ, શાખાઓ, વલયો અને જાળીદાર રચનાઓ બનાવી શકે છે અને ક્યારેય તૂટતા નથી. કાર્બન કુદરતનો શ્રેષ્ઠ લેગો બ્લોક છે! અન્ય તત્વો ભાગ્યે જ 7 કે 8 પરમાણુઓને જોડી શકે છે, જ્યારે કાર્બન હજારો પરમાણુઓને જોડી શકે છે. કાર્બન પાસે આ અદ્ભુત શક્તિ કેમ છે?"
    })

    # 2. Socratic Question
    blocks.append({
        "id": next_id(),
        "type": "socratic_question",
        "question": "What are the two unique properties of carbon that lead to the formation of millions of organic compounds?",
        "question_hi": "कार्बन के वे दो अनूठे गुण कौन से हैं जिनके कारण लाखों कार्बनिक यौगिकों का निर्माण होता है?",
        "question_gu": "કાર્બનના એ બે વિશિષ્ટ ગુણધર્મો કયા છે જેના લીધે લાખો કાર્બનિક સંયોજનો બને છે?",
        "options": [
            "Catenation (self-linking ability) and Tetravalency (valency of 4)",
            "High reactivity with noble gases and metallic luster",
            "Radioactive decay and ionic bond formation",
            "Magnetic attraction and low boiling point"
        ],
        "options_hi": [
            "श्रृंखलन (Catenation - स्वयं से जुड़ने की क्षमता) और चतुःसंयोजकता (Tetravalency)",
            "उत्कृष्ट गैसों के साथ उच्च क्रियाशीलता और धात्विक चमक",
            "रेडियोधर्मी क्षय और आयनिक बंध निर्माण",
            "चुंबकीय आकर्षण और निम्न क्वथनांक"
        ],
        "options_gu": [
            "કેટેનેશન (સ્વયં જોડાવાની ક્ષમતા) અને ચતુઃસંયોજકતા (4 સંયોજકતા)",
            "નિષ્ક્રિય વાયુઓ સાથે પ્રતિક્રિયાશીલતા",
            "રેડિયોએક્ટિવ ક્ષય",
            "ચુંબકીય આકર્ષણ"
        ],
        "correct_index": 0,
        "explanation": "Catenation is the unique ability of carbon atoms to form bonds with other carbon atoms to yield large chains, branches, and rings. Tetravalency means carbon can bond with 4 other atoms (H, O, N, halogens, or C). Together, these two factors generate millions of compounds.",
        "explanation_hi": "श्रृंखलन (Catenation) कार्बन परमाणुओं की अन्य कार्बन परमाणुओं के साथ बंध बनाकर लंबी श्रृंखलाएं, शाखाएं और वलय बनाने की अनूठी क्षमता है। चतुःसंयोजकता का अर्थ है कि कार्बन 4 अन्य परमाणुओं से जुड़ सकता है। ये दोनों कारक मिलकर लाखों यौगिक बनाते हैं।",
        "explanation_gu": "કેટેનેશન એ કાર્બન પરમાણુઓની અન્ય કાર્બન સાથે જોડાઈને લાંબી શૃંખલા, શાખા કે વલય બનાવવાની ક્ષમતા છે. ચતુઃસંયોજકતા એટલે કાર્બન અન્ય 4 પરમાણુઓ સાથે જોડાઈ શકે છે. આ બે ગુણધર્મોથી લાખો સંયોજનો બને છે."
    })

    # 3. Discovery
    blocks.append({
        "id": next_id(),
        "type": "discovery",
        "title": "Saturated vs Unsaturated Hydrocarbons",
        "title_hi": "संतृप्त बनाम असंतृप्त हाइड्रोकार्बन",
        "title_gu": "સંતૃપ્ત વિરુદ્ધ અસંતૃપ્ત હાઇડ્રોકાર્બન",
        "body": "Compounds consisting of only carbon and hydrogen are called HYDROCARBONS.\n\n1. Saturated Hydrocarbons (Alkanes):\n• Carbon atoms are joined by ONLY SINGLE BONDS (C-C).\n• General formula: C_n H_{2n+2}\n• Methane (CH4), Ethane (C2H6), Propane (C3H8), Butane (C4H10).\n• Generally less reactive; burn with clean blue flame.\n\n2. Unsaturated Hydrocarbons:\n• Contain at least one DOUBLE BOND (Alkenes) or TRIPLE BOND (Alkynes) between carbon atoms.\n• Alkenes: General formula C_n H_{2n} (e.g., Ethene C2H4, Propene C3H6).\n• Alkynes: General formula C_n H_{2n-2} (e.g., Ethyne C2H2, Propyne C3H4).\n• Much more reactive than alkanes; undergo addition reactions; burn with sooty yellow flame.",
        "body_hi": "केवल कार्बन और हाइड्रोजन से बने यौगिकों को हाइड्रोकार्बन कहते हैं।\n\n1. संतृप्त हाइड्रोकार्बन (ऐल्केन):\n• कार्बन परमाणुओं के बीच केवल एकल बंध (C-C) होता है।\n• सामान्य सूत्र: C_n H_{2n+2}\n• मीथेन (CH4), एथेन (C2H6), प्रोपेन (C3H8), ब्यूटेन (C4H10)।\n• सामान्यतः कम क्रियाशील; नीली स्वच्छ ज्वाला के साथ जलते हैं।\n\n2. असंतृप्त हाइड्रोकार्बन:\n• कार्बन परमाणुओं के बीच कम से कम एक द्वि-बंध (ऐल्कीन) या त्रि-बंध (ऐल्काइन) होता है।\n• ऐल्कीन: सामान्य सूत्र C_n H_{2n} (जैसे एथीन C2H4, प्रोपीन C3H6)।\n• ऐल्काइन: सामान्य सूत्र C_n H_{2n-2} (जैसे एथाइन C2H2, प्रोपाइन C3H4)।\n• ऐल्केन की तुलना में बहुत अधिक क्रियाशील; संकलन अभिक्रियाएं देते हैं; धुएं वाली पीली ज्वाला देते हैं।",
        "body_gu": "માત્ર કાર્બન અને હાઇડ્રોજન ધરાવતા સંયોજનોને હાઇડ્રોકાર્બન કહેવાય છે.\n\n1. સંતૃપ્ત હાઇડ્રોકાર્બન (એલ્કેન):\n• કાર્બન પરમાણુઓ વચ્ચે માત્ર એકલ બંધ (C-C) હોય છે.\n• સામાન્ય સૂત્ર: C_n H_{2n+2}\n• મિથેન (CH4), ઇથેન (C2H6), પ્રોપેન (C3H8), બ્યુટેન (C4H10).\n• ઓછા ક્રિયાશીલ; સ્વચ્છ ભૂરી જ્યોતથી સળગે છે.\n\n2. અસંતૃપ્ત હાઇડ્રોકાર્બન:\n• કાર્બન પરમાણુઓ વચ્ચે ઓછામાં ઓછો એક દ્વિ-બંધ (એલ્કીન) કે ત્રિ-બંધ (એલ્કાઇન) હોય છે.\n• એલ્કીન: સામાન્ય સૂત્ર C_n H_{2n} (ઇથીન C2H4, પ્રોપીન C3H6).\n• એલ્કાઇન: સામાન્ય સૂત્ર C_n H_{2n-2} (ઇથાઇન C2H2, પ્રોપાઇન C3H4).\n• વધુ ક્રિયાશીલ; યોગશીલ પ્રક્રિયા આપે છે; ધુમાડાવાળી પીળી જ્યોતથી સળગે છે."
    })

    # 4. Theory
    blocks.append({
        "id": next_id(),
        "type": "theory",
        "title": "Chains, Branches, Rings & Structural Isomers",
        "title_hi": "श्रृंखलाएं, शाखाएं, वलय और संरचनात्मक समावयव",
        "title_gu": "શૃંખલાઓ, શાખાઓ, વલયો અને બંધારણીય સમઘટકો",
        "body": "Carbon skeletons can take three primary geometries:\n1. Straight Chains: Unbranched sequential carbon backbone (e.g., n-butane, n-pentane, n-hexane).\n2. Branched Chains: One or more carbon atoms branch off the main chain (e.g., Isobutane / 2-methylpropane).\n3. Closed Rings (Cyclic Hydrocarbons):\n• Cyclohexane (C6H12): A saturated six-carbon ring with single bonds.\n• Benzene (C6H6): An unsaturated six-carbon ring with alternating single and double bonds (3 double bonds, 3 single bonds).\n\nSTRUCTURAL ISOMERISM:\nCompounds having the SAME MOLECULAR FORMULA but DIFFERENT STRUCTURAL ARRANGEMENTS are called structural isomers.\n• Butane (C4H10) has 2 isomers: n-butane (straight chain) and isobutane (branched, 2-methylpropane).\n• Pentane (C5H12) has 3 isomers: n-pentane, isopentane (2-methylbutane), and neopentane (2,2-dimethylpropane).",
        "body_hi": "कार्बन कंकाल तीन मुख्य रूपों में हो सकते हैं:\n1. सीधी श्रृंखलाएं (Straight Chains): अशाखित कार्बन रीढ़ (जैसे n-ब्यूटेन, n-पेन्टेन)।\n2. शाखित श्रृंखलाएं (Branched Chains): मुख्य श्रृंखला से शाखाओं का निकलना (जैसे आइसोब्यूटेन / 2-मेथिलप्रोपेन)।\n3. चक्रीय हाइड्रोकार्बन (Rings):\n• साइक्लोहेक्सेन (C6H12): एकल बंधों वाला 6-कार्बन का संतृप्त वलय।\n• बेंजीन (C6H6): एकांतर एकल और द्वि-बंधों वाला असंतृप्त 6-कार्बन वलय (3 द्वि-बंध, 3 एकल बंध)।\n\nसंरचनात्मक समावयवता (Structural Isomerism):\nसमान आणविक सूत्र लेकिन भिन्न संरचनात्मक सूत्रों वाले यौगिकों को संरचनात्मक समावयव (Isomers) कहते हैं।\n• ब्यूटेन (C4H10) के 2 समावयव हैं: n-ब्यूटेन और आइसोब्यूटेन।\n• पेन्टेन (C5H12) के 3 समावयव हैं: n-पेन्टेन, आइसोपेंटेन (2-मेथिलब्यूटेन), और नियोपेंटेन (2,2-डाइमेथिलप्रोपेन)।",
        "body_gu": "કાર્બનનું માળખું ત્રણ મુખ્ય સ્વરૂપો ધરાવી શકે છે:\n1. સીધી શૃંખલા: અશાખિત શૃંખલા (જેમ કે n-બ્યુટેન, n-પેન્ટેન).\n2. શાખિત શૃંખલા: મુખ્ય શૃંખલામાંથી નીકળતી શાખાઓ (જેમ કે આઇસોબ્યુટેન / 2-મિથાઇલપ્રોપેન).\n3. વલયાકાર હાઇડ્રોકાર્બન (Cyclic Rings):\n• સાયક્લોહેક્ઝેન (C6H12): એકલ બંધ ધરાવતું 6 કાર્બનનું સંતૃપ્ત વલય.\n• બેન્ઝિન (C6H6): એકાંતરે એકલ અને દ્વિ-બંધ ધરાવતું 6 કાર્બનનું અસંતૃપ્ત વલય (3 દ્વિ-બંધ, 3 એકલ બંધ).\n\nબંધારણીય સમઘટકતા (Structural Isomerism):\nસમાન આણ્વીય સૂત્ર પરંતુ જુદા જુદા બંધારણીય સૂત્રો ધરાવતા સંયોજનોને બંધારણીય સમઘટકો કહે છે.\n• બ્યુટેન (C4H10) ના 2 સમઘટકો છે: n-બ્યુટેન અને આઇસોબ્યુટેન.\n• પેન્ટેન (C5H12) ના 3 સમઘટકો છે: n-પેન્ટેન, આઇસોપેન્ટેન અને નિયોપેન્ટેન."
    })

    # Teacher Tip
    blocks.append({
        "id": next_id(),
        "type": "teacher_tip",
        "title": "Teacher Tip: How to Check if Two Structures are Truly Isomers",
        "title_hi": "शिक्षक टिप: कैसे जांचें कि दो संरचनाएं वास्तव में समावयव हैं",
        "title_gu": "શિક્ષક ટિપ: બે બંધારણો સાચે જ સમઘટકો છે કે નહિ તે કેવી રીતે ચકાસવું",
        "body": "Simply bending a chain on paper does NOT create an isomer! If you can trace the carbon chain from one end to another with your pencil without lifting it or backtracking, it is the same continuous chain. True isomers must have a different carbon connectivity (e.g., a carbon bonded to 3 other carbons instead of 2).",
        "body_hi": "कागज पर श्रृंखला को केवल मोड़ देने से समावयव नहीं बनता! यदि आप अपनी पेंसिल उठाए बिना या वापस मुड़े बिना एक सिरे से दूसरे सिरे तक कार्बन श्रृंखला का पता लगा सकते हैं, तो वह वही सीधी श्रृंखला है। वास्तविक समावयवों में कार्बन का जुड़ाव भिन्न होना चाहिए।",
        "body_gu": "કાગળ પર શૃંખલાને માત્ર વાળી દેવાથી સમઘટક બનતો નથી! જો તમે પેન્સિલ ઉપાડ્યા વગર એક છેડેથી બીજા છેડા સુધી પહોંચી શકો, તો તે એ જ શૃંખલા છે. સાચા સમઘટકમાં કાર્બનનું જોડાણ બદલાયેલું હોવું જોઈએ."
    })

    # Common Mistake
    blocks.append({
        "id": next_id(),
        "type": "teacher_tip",
        "title": "Common Mistake: Forgetting Double Bonds in Benzene",
        "title_hi": "सामान्य गलती: बेंजीन में द्वि-बंधों को भूलना",
        "title_gu": "સામાન્ય ભૂલ: બેન્ઝિનમાં દ્વિ-બંધ દોરવાનું ભૂલી જવું",
        "body": "Students often confuse Cyclohexane (C6H12) with Benzene (C6H6). Cyclohexane is saturated with 6 C-C single bonds and 12 C-H bonds. Benzene has alternating single and double bonds (C6H6). Drawing a hexagon without the alternating double bonds (or inner circle) is Cyclohexane, NOT Benzene!",
        "body_hi": "विद्यार्थी अक्सर साइक्लोहेक्सेन (C6H12) और बेंजीन (C6H6) में भ्रमित हो जाते हैं। साइक्लोहेक्सेन में केवल एकल बंध होते हैं (C6H12)। बेंजीन में एकांतर एकल और द्वि-बंध होते हैं (C6H6)। बिना द्वि-बंधों के षट्कोण बनाना साइक्लोहेक्सेन है, बेंजीन नहीं!",
        "body_gu": "વિદ્યાર્થીઓ સાયક્લોહેક્ઝેન (C6H12) અને બેન્ઝિન (C6H6) વચ્ચે ઘણીવાર ભૂલ કરે છે. સાયક્લોહેક્ઝેન સંતૃપ્ત છે અને માત્ર એકલ બંધ ધરાવે છે. બેન્ઝિન એકાંતરે એકલ અને દ્વિ-બંધ ધરાવે છે (C6H6). દ્વિ-બંધ વગરનો ષટ્કોણ એ સાયક્લોહેક્ઝેન છે, બેન્ઝિન નહિ!"
    })

    # 5. Knowledge Check
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "How many structural isomers are possible for Pentane (C5H12)?",
        "question_hi": "पेन्टेन (C5H12) के लिए कितने संरचनात्मक समावयव संभव हैं?",
        "question_gu": "પેન્ટેન (C5H12) માટે કેટલા બંધારણીય સમઘટકો શક્ય છે?",
        "options": [
            "3 structural isomers (n-pentane, isopentane, neopentane)",
            "2 structural isomers",
            "4 structural isomers",
            "5 structural isomers"
        ],
        "options_hi": [
            "3 संरचनात्मक समावयव (n-पेन्टेन, आइसोपेंटेन, नियोपेंटेन)",
            "2 संरचनात्मक समावयव",
            "4 संरचनात्मक समावयव",
            "5 संरचनात्मक समावयव"
        ],
        "options_gu": [
            "3 બંધારણીય સમઘટકો (n-પેન્ટેન, આઇસોપેન્ટેન, નિયોપેન્ટેન)",
            "2 બંધારણીય સમઘટકો",
            "4 બંધારણીય સમઘટકો",
            "5 બંધારણીય સમઘટકો"
        ],
        "correct_index": 0,
        "explanation": "Pentane (C5H12) has exactly 3 structural isomers: 1. n-pentane (CH3-CH2-CH2-CH2-CH3), 2. Isopentane / 2-methylbutane (CH3-CH(CH3)-CH2-CH3), and 3. Neopentane / 2,2-dimethylpropane (C(CH3)4).",
        "explanation_hi": "पेन्टेन (C5H12) के ठीक 3 संरचनात्मक समावयव होते हैं: 1. n-पेन्टेन, 2. आइसोपेंटेन (2-मेथिलब्यूटेन), और 3. नियोपेंटेन (2,2-डाइमेथिलप्रोपेन)।",
        "explanation_gu": "પેન્ટેન (C5H12) ના બરાબર 3 બંધારણીય સમઘટકો છે: 1. n-પેન્ટેન, 2. આઇસોપેન્ટેન (2-મિથાઇલબ્યુટેન), અને 3. નિયોપેન્ટેન (2,2-ડાયમિથાઇલપ્રોપેન)."
    })

    # 6. Reflection
    blocks.append({
        "id": next_id(),
        "type": "reflection",
        "title": "Structure Dictates Function in Chemistry",
        "title_hi": "रसायन विज्ञान में संरचना कार्य का निर्धारण करती है",
        "title_gu": "રસાયણશાસ્ત્રમાં બંધારણ ગુણધર્મો નક્કી કરે છે",
        "body": "Even though n-pentane, isopentane, and neopentane all have the exact same chemical formula (C5H12), neopentane boils at 9.5°C while n-pentane boils at 36°C! Why? Spherical branched molecules have less surface area of contact, weakening intermolecular attraction. In organic chemistry, changing shape changes physical behavior completely.",
        "body_hi": "भले ही n-पेन्टेन, आइसोपेंटेन और नियोपेंटेन सभी का रासायनिक सूत्र समान (C5H12) है, फिर भी नियोपेंटेन 9.5°C पर उबलता है जबकि n-पेन्टेन 36°C पर उबलता है! क्यों? शाखित अणुओं का सतही क्षेत्रफल कम होता है, जिससे अंतरा-आण्विक आकर्षण कमजोर हो जाता है।",
        "body_gu": "જોકે n-પેન્ટેન, આઇસોપેન્ટેન અને નિયોપેન્ટેન ત્રણેયનું આણ્વીય સૂત્ર સમાન (C5H12) છે, છતાં નિયોપેન્ટેનનું ઉત્કલનબિંદુ 9.5°C અને n-પેન્ટેનનું 36°C છે! ગોળાકાર શાખિત અણુઓનું સપાટી ક્ષેત્રફળ ઓછું હોવાથી આંતર-આણ્વીય આકર્ષણ ઘટે છે."
    })

    # 7. Connection
    blocks.append({
        "id": next_id(),
        "type": "connection",
        "title": "Hydrocarbons in Everyday Energy: LPG and CNG",
        "title_hi": "दैनिक जीवन में हाइड्रोकार्बन ऊर्जा: एलपीजी और सीएनजी",
        "title_gu": "રોજિંદા જીવનમાં હાઇડ્રોકાર્બન ઊર્જા: LPG અને CNG",
        "body": "The gas cylinder in your kitchen (LPG) consists mainly of Butane (C4H10) and Propane (C3H8) compressed into liquid. The clean vehicle fuel CNG is primarily compressed Methane (CH4). Understanding straight and branched alkanes helps petrochemical refineries optimize octane ratings for vehicle engines.",
        "body_hi": "आपकी रसोई का गैस सिलेंडर (LPG) मुख्य रूप से ब्यूटेन (C4H10) और प्रोपेन (C3H8) का तरल रूप में संपीडित मिश्रण है। स्वच्छ वाहन ईंधन सीएनजी (CNG) मुख्य रूप से मीथेन (CH4) है। पेट्रोकेमिकल रिफाइनरियों में हाइड्रोकार्बन का अध्ययन इंजन ईंधन को बेहतर बनाने में मदद करता है।",
        "body_gu": "રસોઈ ગેસ સિલિન્ડર (LPG) મુખ્યત્વે પ્રવાહીકૃત બ્યુટેન (C4H10) અને પ્રોપેન (C3H8) ધરાવે છે. સીએનજી (CNG) મુખ્યત્વે મિથેન (CH4) વાયુ છે. પેટ્રોકેમિકલ ઉદ્યોગોમાં હાઇડ્રોકાર્બનનું જ્ઞાન ઉત્તમ ગુણવત્તાવાળું બળતણ બનાવવામાં વપરાય છે."
    })

    # 8. Mastery Challenge
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "A cyclic hydrocarbon has the molecular formula C6H12. How many single covalent bonds are present in this molecule?",
        "question_hi": "एक चक्रीय हाइड्रोकार्बन का आणविक सूत्र C6H12 है। इस अणु में कितने एकल सहसंयोजक बंध उपस्थित हैं?",
        "question_gu": "એક ચક્રીય હાઇડ્રોકાર્બનનું આણ્વીય સૂત્ર C6H12 છે. આ અણુમાં કુલ કેટલા એકલ સહસંયોજક બંધ આવેલા છે?",
        "options": [
            "18 single covalent bonds (6 C-C and 12 C-H)",
            "12 single covalent bonds",
            "15 single covalent bonds",
            "6 single covalent bonds"
        ],
        "options_hi": [
            "18 एकल सहसंयोजक बंध (6 C-C और 12 C-H)",
            "12 एकल सहसंयोजक बंध",
            "15 एकल सहसंयोजक बंध",
            "6 एकल सहसंयोजक बंध"
        ],
        "options_gu": [
            "18 એકલ સહસંયોજક બંધ (6 C-C અને 12 C-H)",
            "12 એકલ સહસંયોજક બંધ",
            "15 એકલ સહસંયોજક બંધ",
            "6 એકલ સહસંયોજક બંધ"
        ],
        "correct_index": 0,
        "explanation": "C6H12 is Cyclohexane. In cyclohexane, 6 carbon atoms form a ring with 6 C-C single bonds. Each carbon also bonds to 2 hydrogen atoms, giving 12 C-H single bonds. Total single covalent bonds = 6 + 12 = 18.",
        "explanation_hi": "C6H12 साइक्लोहेक्सेन है। इसमें 6 कार्बन परमाणु 6 C-C एकल बंधों का एक वलय बनाते हैं। प्रत्येक कार्बन 2 हाइड्रोजन से भी जुड़ा होता है, जिससे 12 C-H एकल बंध बनते हैं। कुल एकल बंध = 6 + 12 = 18।",
        "explanation_gu": "C6H12 સાયક્લોહેક્ઝેન છે. તેમાં 6 કાર્બન વચ્ચે 6 C-C એકલ બંધ અને દરેક કાર્બન 2 હાઇડ્રોજન સાથે જોડાતાં 12 C-H એકલ બંધ બને છે. કુલ એકલ બંધ = 6 + 12 = 18."
    })

    # =========================================================================
    # MODULE 3: HOMOLOGOUS SERIES & FUNCTIONAL GROUPS (8-STEP PEDAGOGY)
    # =========================================================================

    # 1. Hook
    blocks.append({
        "id": next_id(),
        "type": "hook",
        "title": "The Chemistry Family Tree",
        "title_hi": "रसायन विज्ञान का पारिवारिक वृक्ष",
        "title_gu": "રસાયણશાસ્ત્રનું પારિવારિક વૃક્ષ",
        "body": "In human families, children inherit characteristics like eye colour or smile from parents while varying in height. In organic chemistry, compounds also belong to tightly-knit families called HOMOLOGOUS SERIES! If you know how the first member of the family behaves, you can predict how every other sibling will react. How does nature achieve this incredible harmony?",
        "body_hi": "मानव परिवारों में, बच्चे माता-पिता से आंखों का रंग या मुस्कान जैसी विशेषताएं प्राप्त करते हैं। कार्बनिक रसायन विज्ञान में भी, यौगिक 'सजातीय श्रेणी' (Homologous Series) नामक परिवारों से संबंधित होते हैं! यदि आप जानते हैं कि परिवार का पहला सदस्य कैसा व्यवहार करता है, तो आप भविष्यवाणी कर सकते हैं कि हर दूसरा सदस्य कैसे प्रतिक्रिया करेगा। प्रकृति इस अविश्वसनीय सामंजस्य को कैसे प्राप्त करती है?",
        "body_gu": "માનવ પરિવારોમાં બાળકો માતા-પિતા જેવા લક્ષણો ધરાવે છે. કાર્બનિક રસાયણશાસ્ત્રમાં પણ સંયોજનો 'સજાતીય શ્રેણી' નામના કુટુંબમાં વહેંચાયેલા હોય છે! જો તમે કુટુંબના પ્રથમ સભ્યના ગુણધર્મો જાણતા હો, તો તમે અન્ય તમામ સભ્યોના વર્તનની આગાહી કરી શકો છો. કુદરત આ સુમેળ કેવી રીતે સાધે છે?"
    })

    # 2. Socratic Question
    blocks.append({
        "id": next_id(),
        "type": "socratic_question",
        "question": "What is the difference in molecular formula and molecular mass between two successive members of any homologous series?",
        "question_hi": "किसी भी सजातीय श्रेणी के दो उत्तरोत्तर सदस्यों के आणविक सूत्र और आणविक द्रव्यमान में क्या अंतर होता है?",
        "question_gu": "કોઈપણ સજાતીય શ્રેણીના બે ક્રમિક સભ્યો વચ્ચે આણ્વીય સૂત્ર અને આણ્વીય દળમાં શો તફાવત હોય છે?",
        "options": [
            "-CH2- unit and 14 u atomic mass difference",
            "-CH3- unit and 15 u atomic mass difference",
            "-CH- unit and 13 u atomic mass difference",
            "-C2H2- unit and 26 u atomic mass difference"
        ],
        "options_hi": [
            "-CH2- इकाई और 14 u द्रव्यमान का अंतर",
            "-CH3- इकाई और 15 u द्रव्यमान का अंतर",
            "-CH- इकाई और 13 u द्रव्यमान का अंतर",
            "-C2H2- इकाई और 26 u द्रव्यमान का अंतर"
        ],
        "options_gu": [
            "-CH2- એકમ અને 14 u દળનો તફાવત",
            "-CH3- એકમ અને 15 u દળનો તફાવત",
            "-CH- એકમ અને 13 u દળનો તફાવત",
            "-C2H2- એકમ અને 26 u દળનો તફાવત"
        ],
        "correct_index": 0,
        "explanation": "Every successive member of a homologous series differs from the previous one by a single carbon atom and two hydrogen atoms (-CH2- methylene unit). Atomic mass difference = 12 (C) + 2(1) (H) = 14 u.",
        "explanation_hi": "सजातीय श्रेणी का प्रत्येक उत्तरोत्तर सदस्य पिछले सदस्य से एक कार्बन और दो हाइड्रोजन परमाणुओं (-CH2- इकाई) से भिन्न होता है। द्रव्यमान का अंतर = 12 + 2(1) = 14 u होता है।",
        "explanation_gu": "સજાતીય શ્રેણીનો દરેક ક્રમિક સભ્ય આગળના સભ્ય કરતાં એક કાર્બન અને બે હાઇડ્રોજન (-CH2- એકમ) વડે જુદો પડે છે. દળનો તફાવત = 12 + 2 = 14 u થાય છે."
    })

    # 3. Discovery
    blocks.append({
        "id": next_id(),
        "type": "discovery",
        "title": "Heteroatoms and Functional Groups",
        "title_hi": "विषमपरमाणु और प्रकार्यात्मक समूह",
        "title_gu": "વિષમપરમાણુ અને ક્રિયાશીલ સમૂહો",
        "body": "In a hydrocarbon chain, one or more hydrogen atoms can be replaced by other elements such that the valency of carbon remains satisfied. These replacing atoms are called HETEROATOMS (e.g., Cl, Br, O, N).\n\nA functional group is an atom or group of atoms that confers characteristic chemical properties to an organic compound, regardless of the length and nature of the carbon chain:\n1. Halo Group (-Cl, -Br): Chloro-, Bromo- (e.g., Chloromethane CH3Cl).\n2. Alcohol Group (-OH): Suffix '-ol' (e.g., Methanol CH3OH, Ethanol C2H5OH).\n3. Aldehyde Group (-CHO): Carbonyl with one terminal H; Suffix '-al' (e.g., Methanal HCHO, Ethanal CH3CHO).\n4. Ketone Group (-CO- / >C=O): Carbonyl bonded to two carbons; Suffix '-one' (e.g., Propanone CH3COCH3).\n5. Carboxylic Acid Group (-COOH): Suffix '-oic acid' (e.g., Methanoic acid HCOOH, Ethanoic acid CH3COOH).",
        "body_hi": "हाइड्रोकार्बन श्रृंखला में, एक या अधिक हाइड्रोजन परमाणुओं को अन्य तत्वों द्वारा इस प्रकार प्रतिस्थापित किया जा सकता है कि कार्बन की संयोजकता संतुष्ट रहे। इन प्रतिस्थापी परमाणुओं को विषमपरमाणु (Heteroatoms) कहते हैं (जैसे Cl, Br, O)।\n\nप्रकार्यात्मक समूह (Functional Group) एक परमाणु या परमाणुओं का समूह है जो कार्बनिक यौगिक को विशिष्ट रासायनिक गुण प्रदान करता है:\n1. हैलो समूह (-Cl, -Br): क्लोरो-, ब्रोमो- (जैसे क्लोरोमीथेन CH3Cl)।\n2. ऐल्कोहॉल समूह (-OH): प्रत्यय '-ol' (जैसे मेथेनॉल CH3OH, एथेनॉल C2H5OH)।\n3. ऐल्डिहाइड समूह (-CHO): प्रत्यय '-al' (जैसे मेथेनल HCHO, एथेनल CH3CHO)।\n4. कीटोन समूह (-CO-): प्रत्यय '-one' (जैसे प्रोपेनॉन CH3COCH3)।\n5. कार्बोक्सिलिक अम्ल समूह (-COOH): प्रत्यय '-oic acid' (जैसे मेथेनॉइक अम्ल HCOOH, एथेनॉइक अम्ल CH3COOH)।",
        "body_gu": "હાઇડ્રોકાર્બન શૃંખલામાં હાઇડ્રોજનનું વિસ્થાપન કરતાં અન્ય તત્વોને વિષમપરમાણુ કહે છે (જેમ કે Cl, Br, O).\n\nક્રિયાશીલ સમૂહ એ પરમાણુ કે પરમાણુઓનો સમૂહ છે જે સંયોજનને વિશિષ્ટ રાસાયણિક ગુણધર્મો આપે છે:\n1. હેલો સમૂહ (-Cl, -Br): ક્લોરો-, બ્રોમો- (ક્લોરોમિથેન CH3Cl).\n2. આલ્કોહોલ સમૂહ (-OH): પ્રત્યય '-ઓલ' (મિથેનોલ CH3OH, ઇથેનોલ C2H5OH).\n3. આલ્ડીહાઇડ સમૂહ (-CHO): પ્રત્યય '-આલ' (મિથેનાલ HCHO, ઇથેનાલ CH3CHO).\n4. કીટોન સમૂહ (-CO-): પ્રત્યય '-ઓન' (પ્રોપેનોન CH3COCH3).\n5. કાર્બોક્સિલિક એસિડ સમૂહ (-COOH): પ્રત્યય '-ઓઇક એસિડ' (મિથેનોઇક એસિડ HCOOH, ઇથેનોઇક એસિડ CH3COOH)."
    })

    # 4. Theory
    blocks.append({
        "id": next_id(),
        "type": "theory",
        "title": "Characteristics of a Homologous Series",
        "title_hi": "सजातीय श्रेणी की मुख्य विशेषताएं",
        "title_gu": "સજાતીય શ્રેણીની મુખ્ય લાક્ષણિકતાઓ",
        "body": "A HOMOLOGOUS SERIES is a series of carbon compounds having the same functional group where members differ sequentially by a -CH2- unit.\n\nKey Characteristics:\n1. Same General Formula: All alkanes share C_n H_{2n+2}; all alkenes share C_n H_{2n}; all alcohols share C_n H_{2n+1}OH.\n2. Constant Formula Difference: Adjacent members differ by -CH2-.\n3. Constant Mass Difference: Adjacent members differ by 14 u.\n4. Identical Chemical Properties: Determined by the shared functional group (e.g., all alcohols react with sodium to release hydrogen gas).\n5. Gradation in Physical Properties: As molecular mass increases, boiling points, melting points, and densities increase gradually due to increasing van der Waals forces.\n6. Uniform Preparation Methods: All members of a series can be synthesized by similar generalized chemical reactions.",
        "body_hi": "सजातीय श्रेणी समान प्रकार्यात्मक समूह वाले कार्बन यौगिकों की एक ऐसी श्रृंखला है जिसमें सदस्य क्रमिक रूप से -CH2- इकाई से भिन्न होते हैं।\n\nमुख्य विशेषताएं:\n1. समान सामान्य सूत्र: सभी ऐल्केन C_n H_{2n+2}; सभी ऐल्कोहॉल C_n H_{2n+1}OH साझा करते हैं।\n2. निश्चित सूत्र अंतर: आस-पास के सदस्यों में -CH2- का अंतर होता है।\n3. निश्चित द्रव्यमान अंतर: सदस्यों में 14 u का अंतर होता है।\n4. समान रासायनिक गुण: समान प्रकार्यात्मक समूह के कारण रासायनिक गुण समान होते हैं।\n5. भौतिक गुणों में क्रमिकता: आणविक द्रव्यमान बढ़ने पर क्वथनांक, गलनांक और घनत्व में क्रमिक वृद्धि होती है।\n6. विरचन की सामान्य विधियाँ: श्रेणी के सभी सदस्यों को समान सामान्य विधियों द्वारा बनाया जा सकता है।",
        "body_gu": "સજાતીય શ્રેણી એ સમાન ક્રિયાશીલ સમૂહ ધરાવતા કાર્બનિક સંયોજનોની એવી શ્રેણી છે જેમાં ક્રમિક સભ્યો -CH2- એકમ વડે જુદા પડે છે.\n\nમુખ્ય લાક્ષણિકતાઓ:\n1. સમાન સામાન્ય સૂત્ર: તમામ એલ્કેન C_n H_{2n+2}; તમામ આલ્કોહોલ C_n H_{2n+1}OH ધરાવે છે.\n2. ચોક્કસ સૂત્ર તફાવત: ક્રમિક સભ્યો વચ્ચે -CH2- નો તફાવત.\n3. ચોક્કસ દળ તફાવત: ક્રમિક સભ્યો વચ્ચે 14 u નો તફાવત.\n4. સમાન રાસાયણિક ગુણધર્મો: સમાન ક્રિયાશીલ સમૂહને કારણે રાસાયણિક પ્રક્રિયાઓ સમાન હોય છે.\n5. ભૌતિક ગુણધર્મોમાં ક્રમબદ્ધતા: આણ્વીય દળ વધતાં ઉત્કલનબિંદુ, ગલનબિંદુ અને ઘનતા ક્રમશઃ વધે છે.\n6. બનાવટની સામાન્ય પદ્ધતિઓ: એક જ શ્રેણીના તમામ સભ્યો સમાન પદ્ધતિથી બનાવી શકાય છે."
    })

    # Teacher Tip
    blocks.append({
        "id": next_id(),
        "type": "teacher_tip",
        "title": "Teacher Tip: Remembering Ketones Must Have at Least 3 Carbons",
        "title_hi": "शिक्षक टिप: याद रखें कि कीटोन में कम से कम 3 कार्बन होने चाहिए",
        "title_gu": "શિક્ષક ટિપ: યાદ રાખો કે કીટોનમાં ઓછામાં ઓછા 3 કાર્બન હોવા જરૂરી છે",
        "body": "In a ketone, the carbonyl group (>C=O) must be flanked by carbon atoms on BOTH sides (R-CO-R'). If a carbonyl group is at the end of a chain with a hydrogen attached, it is an ALDEHYDE (-CHO), not a ketone! Therefore, the simplest possible ketone is Propanone (Acetone, CH3-CO-CH3) with 3 carbons. Methanone and Ethanone do not exist!",
        "body_hi": "कीटोन में, कार्बोनिल समूह (>C=O) के दोनों तरफ कार्बन परमाणु होने चाहिए (R-CO-R')। यदि कार्बोनिल समूह श्रृंखला के अंत में हाइड्रोजन के साथ है, तो वह ऐल्डिहाइड (-CHO) है, कीटोन नहीं! इसलिए सबसे सरल कीटोन प्रोपेनॉन (CH3-CO-CH3) है जिसमें 3 कार्बन होते हैं। मेथेनॉन और एथेनॉन का कोई अस्तित्व नहीं है!",
        "body_gu": "કીટોનમાં કાર્બોનિલ સમૂહ (>C=O) ની બંને બાજુએ કાર્બન જોડાયેલા હોવા જોઈએ. જો છેડે હાઇડ્રોજન હોય તો તે આલ્ડીહાઇડ (-CHO) બની જાય! આથી સૌથી સાદો કીટોન 3 કાર્બન ધરાવતો પ્રોપેનોન (એસિટોન) છે. મિથેનોન કે ઇથેનોન અસ્તિત્વ ધરાવતા નથી!"
    })

    # Common Mistake
    blocks.append({
        "id": next_id(),
        "type": "teacher_tip",
        "title": "Common Mistake: Confusing Suffix '-al' (Aldehyde) with '-ol' (Alcohol)",
        "title_hi": "सामान्य गलती: प्रत्यय '-al' (ऐल्डिहाइड) को '-ol' (ऐल्कोहॉल) समझना",
        "title_gu": "સામાન્ય ભૂલ: '-આલ' (આલ્ડીહાઇડ) અને '-ઓલ' (આલ્કોહોલ) વચ્ચે ગૂંચવાડો",
        "body": "Pay close attention to spelling in exams! Ethanal is an aldehyde (CH3CHO, pungent aroma). Ethanol is an alcohol (C2H5OH, intoxicating liquid). A single vowel changes the functional group, the chemistry, and the entire question's marks!",
        "body_hi": "परीक्षा में वर्तनी (Spelling) पर विशेष ध्यान दें! एथेनल (Ethanal) एक ऐल्डिहाइड है (CH3CHO)। एथेनॉल (Ethanol) एक ऐल्कोहॉल है (C2H5OH)। केवल एक स्वर (Vowel) बदलने से पूरा प्रकार्यात्मक समूह और रासायनिक गुण बदल जाते हैं!",
        "body_gu": "પરીક્ષામાં જોડણી પર ખાસ ધ્યાન આપો! ઇથેનાલ (Ethanal) એ આલ્ડીહાઇડ છે (CH3CHO). ઇથેનોલ (Ethanol) એ આલ્કોહોલ છે (C2H5OH). માત્ર એક અક્ષરના ફેરફારથી ક્રિયાશીલ સમૂહ અને આખો ગુણધર્મ બદલાઈ જાય છે!"
    })

    # 5. Knowledge Check
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "Which of the following belongs to the same homologous series as Propene (C3H6)?",
        "question_hi": "निम्नलिखित में से कौन प्रोपीन (C3H6) की ही सजातीय श्रेणी से संबंधित है?",
        "question_gu": "નીચેનામાંથી કયું પ્રોપીન (C3H6) ની સજાતીય શ્રેણીનું સભ્ય છે?",
        "options": [
            "C4H8 (Butene)",
            "C4H10 (Butane)",
            "C4H6 (Butyne)",
            "C3H8 (Propane)"
        ],
        "options_hi": [
            "C4H8 (ब्यूटीन)",
            "C4H10 (ब्यूटेन)",
            "C4H6 (ब्यूटाइन)",
            "C3H8 (प्रोपेन)"
        ],
        "options_gu": [
            "C4H8 (બ્યુટીન)",
            "C4H10 (બ્યુટેન)",
            "C4H6 (બ્યુટાઇન)",
            "C3H8 (પ્રોપેન)"
        ],
        "correct_index": 0,
        "explanation": "Propene (C3H6) has general formula C_n H_{2n} (Alkene series). For n=4, Alkene is C4H8 (Butene). C4H10 is an Alkane (C_n H_{2n+2}) and C4H6 is an Alkyne (C_n H_{2n-2}).",
        "explanation_hi": "प्रोपीन (C3H6) का सामान्य सूत्र C_n H_{2n} (ऐल्कीन श्रेणी) है। n=4 के लिए, ऐल्कीन C4H8 (ब्यूटीन) है। C4H10 ऐल्केन है और C4H6 ऐल्काइन है।",
        "explanation_gu": "પ્રોપીન (C3H6) એલ્કીન શ્રેણી (C_n H_{2n}) નું સભ્ય છે. n=4 માટે એલ્કીન C4H8 (બ્યુટીન) બને છે. C4H10 એલ્કેન અને C4H6 એલ્કાઇન છે."
    })

    # 6. Reflection
    blocks.append({
        "id": next_id(),
        "type": "reflection",
        "title": "Predictability Reduces Memorization",
        "title_hi": "अनुमान लगाने की क्षमता रटने को कम करती है",
        "title_gu": "અનુમાન ક્ષમતા ગોખણપટ્ટી ઘટાડે છે",
        "body": "Instead of memorizing millions of individual organic reactions, chemists only study a few homologous series. Once you know how ethanol undergoes oxidation to form ethanoic acid, you instantly know that propanol oxidizes to propanoic acid, and butanol to butanoic acid. That is the elegance of organic chemistry.",
        "body_hi": "लाखों व्यक्तिगत कार्बनिक अभिक्रियाओं को याद करने के बजाय, वैज्ञानिक केवल कुछ सजातीय श्रेणियों का अध्ययन करते हैं। एक बार जब आप जान जाते हैं कि एथेनॉल एथेनॉइक अम्ल बनाने के लिए ऑक्सीकृत होता है, तो आप तुरंत जान जाते हैं कि प्रोपेनॉल प्रोपेनॉइक अम्ल बनाएगा।",
        "body_gu": "લાખો પ્રક્રિયાઓ ગોખવાને બદલે રસાયણશાસ્ત્રીઓ માત્ર સજાતીય શ્રેણીઓ શીખે છે. જો ઇથેનોલનું ઓક્સિડેશન ઇથેનોઇક એસિડ આપે, તો પ્રોપેનોલનું ઓક્સિડેશન પ્રોપેનોઇક એસિડ જ આપે. આ કાર્બનિક રસાયણની સુંદરતા છે."
    })

    # 7. Connection
    blocks.append({
        "id": next_id(),
        "type": "connection",
        "title": "Fractional Distillation of Crude Petroleum",
        "title_hi": "कच्चे पेट्रोलियम का प्रभाजी आसवन",
        "title_gu": "ક્રૂડ પેટ્રોલિયમનું વિભાગીય નિસ્યંદન",
        "body": "Because successive members of homologous series have gradually increasing boiling points, oil refineries separate crude oil into petrol (C5-C10), kerosene (C10-C16), diesel (C14-C20), and lubricating wax in a single giant fractionating column using thermal gradient.",
        "body_hi": "क्योंकि सजातीय श्रेणी के उत्तरोत्तर सदस्यों का क्वथनांक धीरे-धीरे बढ़ता है, तेल रिफाइनरियां कच्चे तेल को एक विशाल प्रभाजक स्तंभ में पेट्रोल, केरोसिन, डीजल और स्नेहक मोम में अलग करती हैं।",
        "body_gu": "સજાતીય શ્રેણીના સભ્યોના ઉત્કલનબિંદુ ક્રમશઃ વધતા હોવાથી ઓઇલ રિફાઇનરીઓ ક્રૂડ તેલમાંથી પેટ્રોલ, કેરોસીન, ડીઝલ અને ડામરને વિભાગીય નિસ્યંદન ટાવર વડે અલગ પાડે છે."
    })

    # 8. Mastery Challenge
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "Which of the following organic compounds contains both a carbonyl group (>C=O) and a hydroxyl group (-OH) on the same carbon atom?",
        "question_hi": "निम्नलिखित में से किस कार्बनिक यौगिक में एक ही कार्बन परमाणु पर कार्बोनिल समूह (>C=O) और हाइड्रॉक्सिल समूह (-OH) दोनों होते हैं?",
        "question_gu": "નીચેનામાંથી કયું કાર્બનિક સંયોજન એક જ કાર્બન પરમાણુ પર કાર્બોનિલ (>C=O) અને હાઇડ્રોક્સિલ (-OH) બંને સમૂહો ધરાવે છે?",
        "options": [
            "Carboxylic Acid (-COOH)",
            "Ketone (-CO-)",
            "Alcohol (-OH)",
            "Aldehyde (-CHO)"
        ],
        "options_hi": [
            "कार्बोक्सिलिक अम्ल (-COOH)",
            "कीटोन (-CO-)",
            "ऐल्कोहॉल (-OH)",
            "ऐल्डिहाइड (-CHO)"
        ],
        "options_gu": [
            "કાર્બોક્સિલિક એસિડ (-COOH)",
            "કીટોન (-CO-)",
            "આલ્કોહોલ (-OH)",
            "આલ્ડીહાઇડ (-CHO)"
        ],
        "correct_index": 0,
        "explanation": "Carboxylic acids (-COOH) contain a carbonyl group (>C=O) directly bonded to a hydroxyl group (-OH). This combination creates unique acidic properties.",
        "explanation_hi": "कार्बोक्सिलिक अम्लों (-COOH) में कार्बोनिल समूह (>C=O) सीधे हाइड्रॉक्सिल समूह (-OH) से जुड़ा होता है, जो इसे विशिष्ट अम्लीय गुण प्रदान करता है।",
        "explanation_gu": "કાર્બોક્સિલિક એસિડ (-COOH) માં કાર્બોનિલ સમૂહ (>C=O) અને હાઇડ્રોક્સિલ સમૂહ (-OH) એક જ કાર્બન સાથે જોડાયેલા હોય છે, જે તેને એસિડિક ગુણધર્મો આપે છે."
    })

    # =========================================================================
    # MODULE 4: NOMENCLATURE OF CARBON COMPOUNDS (8-STEP PEDAGOGY)
    # =========================================================================

    # 1. Hook
    blocks.append({
        "id": next_id(),
        "type": "hook",
        "title": "The Universal Language of Chemists",
        "title_hi": "रसायनज्ञों की सार्वभौमिक भाषा",
        "title_gu": "રસાયણશાસ્ત્રીઓની વૈશ્વિક ભાષા",
        "body": "Before international naming standards, a single chemical compound had up to 10 different regional names in France, Germany, India, and Japan, causing total chaos. Then IUPAC (International Union of Pure and Applied Chemistry) stepped in and devised a universal naming code. By reading a single IUPAC name, a chemist anywhere on Earth can sketch the exact 3D molecular structure. How does this code work?",
        "body_hi": "अंतरराष्ट्रीय नामकरण मानकों से पहले, एक ही रासायनिक यौगिक के विभिन्न देशों में 10 अलग-अलग नाम होते थे, जिससे बहुत भ्रम होता था। फिर IUPAC ने एक सार्वभौमिक नामकरण कोड तैयार किया। केवल एक IUPAC नाम पढ़कर, दुनिया का कोई भी रसायनज्ञ सटीक 3D आणविक संरचना बना सकता है। यह कोड कैसे काम करता है?",
        "body_gu": "આંતરરાષ્ટ્રીય નામકરણ પદ્ધતિ પહેલાં એક જ સંયોજનના અલગ અલગ દેશોમાં અનેક નામો હતા, જેનાથી ગૂંચવાડો થતો હતો. પછી IUPAC એ સાર્વત્રિક નિયમો બનાવ્યા. માત્ર એક IUPAC નામ વાંચીને વિશ્વનો કોઈપણ વૈજ્ઞાનિક ચોક્કસ અણુ બંધારણ દોરી શકે છે. આ નિયમો કેવી રીતે કામ કરે છે?"
    })

    # 2. Socratic Question
    blocks.append({
        "id": next_id(),
        "type": "socratic_question",
        "question": "What is the systematic IUPAC name of the compound CH3-CH2-CHO?",
        "question_hi": "यौगिक CH3-CH2-CHO का व्यवस्थित IUPAC नाम क्या है?",
        "question_gu": "સંયોજન CH3-CH2-CHO નું પદ્ધતિસરનું IUPAC નામ શું છે?",
        "options": [
            "Propanal",
            "Propanol",
            "Propanone",
            "Propanoic acid"
        ],
        "options_hi": [
            "प्रोपेनल (Propanal)",
            "प्रोपेनॉल (Propanol)",
            "प्रोपेनॉन (Propanone)",
            "प्रोपेनॉइक अम्ल (Propanoic acid)"
        ],
        "options_gu": [
            "પ્રોપેનાલ (Propanal)",
            "પ્રોપેનોલ (Propanol)",
            "પ્રોપેનોન (Propanone)",
            "પ્રોપેનોઇક એસિડ (Propanoic acid)"
        ],
        "correct_index": 0,
        "explanation": "The compound contains 3 carbon atoms (root word 'Prop-') joined by single bonds ('-an-') and an aldehyde functional group -CHO (suffix '-al'). Combining them yields Propanal.",
        "explanation_hi": "यौगिक में 3 कार्बन परमाणु हैं (मूल शब्द 'Prop-') जो एकल बंधों ('-an-') से जुड़े हैं और एक ऐल्डिहाइड समूह -CHO (प्रत्यय '-al') है। इन्हें मिलाने पर प्रोपेनल बनता है।",
        "explanation_gu": "આ સંયોજનમાં 3 કાર્બન પરમાણુ (પૂર્વગ 'પ્રોપ-'), એકલ બંધ ('-એન-') અને આલ્ડીહાઇડ સમૂહ -CHO (પ્રત્યય '-આલ') છે. આથી તેનું નામ પ્રોપેનાલ બને છે."
    })

    # 3. Discovery
    blocks.append({
        "id": next_id(),
        "type": "discovery",
        "title": "The IUPAC Three-Part Formula",
        "title_hi": "IUPAC का तीन-भाग सूत्र",
        "title_gu": "IUPAC નું ત્રણ-ભાગીય સૂત્ર",
        "body": "Every IUPAC name consists of three basic components:\nPREFIX + ROOT WORD + SUFFIX\n\n1. ROOT WORD (Number of Carbons in Longest Chain):\n• 1 Carbon = Meth-\n• 2 Carbons = Eth-\n• 3 Carbons = Prop-\n• 4 Carbons = But-\n• 5 Carbons = Pent-\n• 6 Carbons = Hex-\n\n2. PRIMARY SUFFIX (Nature of Carbon-Carbon Bond):\n• All single bonds = -ane\n• Double bond = -ene\n• Triple bond = -yne\n\n3. SECONDARY SUFFIX OR PREFIX (Functional Group):\n• Halogen: Prefix 'Chloro-' or 'Bromo-' (e.g., Chloropropane)\n• Alcohol (-OH): Replace '-e' of alkane with '-ol' (e.g., Ethanol)\n• Aldehyde (-CHO): Replace '-e' with '-al' (e.g., Ethanal)\n• Ketone (-CO-): Replace '-e' with '-one' (e.g., Propanone)\n• Carboxylic Acid (-COOH): Replace '-e' with '-oic acid' (e.g., Ethanoic acid)",
        "body_hi": "प्रत्येक IUPAC नाम तीन बुनियादी घटकों से बना होता है:\nपूर्वसर्ग (PREFIX) + मूल शब्द (ROOT WORD) + प्रत्यय (SUFFIX)\n\n1. मूल शब्द (कार्बन परमाणुओं की संख्या):\n• 1 कार्बन = मेथ (Meth-)\n• 2 कार्बन = एथ (Eth-)\n• 3 कार्बन = प्रोप (Prop-)\n• 4 कार्बन = ब्यूट (But-)\n• 5 कार्बन = पेन्ट (Pent-)\n• 6 कार्बन = हेक्स (Hex-)\n\n2. प्राथमिक प्रत्यय (बंध का प्रकार):\n• सभी एकल बंध = -ane (ऐल्केन)\n• द्वि-बंध = -ene (ऐल्कीन)\n• त्रि-बंध = -yne (ऐल्काइन)\n\n3. द्वितीयक प्रत्यय या पूर्वसर्ग (प्रकार्यात्मक समूह):\n• हैलोजन: पूर्वसर्ग 'क्लोरो-' या 'ब्रोमो-'\n• ऐल्कोहॉल (-OH): प्रत्यय '-ol' (जैसे एथेनॉल)\n• ऐल्डिहाइड (-CHO): प्रत्यय '-al' (जैसे एथेनल)\n• कीटोन (-CO-): प्रत्यय '-one' (जैसे प्रोपेनॉन)\n• कार्बोक्सिलिक अम्ल (-COOH): प्रत्यय '-oic acid' (जैसे एथेनॉइक अम्ल)",
        "body_gu": "દરેક IUPAC નામ ત્રણ ભાગોનું બનેલું છે:\nપૂર્વગ (PREFIX) + મૂળ શબ્દ (ROOT WORD) + પ્રત્યય (SUFFIX)\n\n1. મૂળ શબ્દ (કાર્બન સંખ્યા):\n• 1 કાર્બન = મિથ (Meth-)\n• 2 કાર્બન = ઇથ (Eth-)\n• 3 કાર્બન = પ્રોપ (Prop-)\n• 4 કાર્બન = બ્યુટ (But-)\n• 5 કાર્બન = પેન્ટ (Pent-)\n• 6 કાર્બન = હેક્સ (Hex-)\n\n2. પ્રાથમિક પ્રત્યય (બંધનો પ્રકાર):\n• એકલ બંધ = -એન (-ane)\n• દ્વિ-બંધ = -ઇન (-ene)\n• ત્રિ-બંધ = -આઇન (-yne)\n\n3. દ્વિતીયક પ્રત્યય/પૂર્વગ (ક્રિયાશીલ સમૂહ):\n• હેલોજન: પૂર્વગ 'ક્લોરો-' કે 'બ્રોમો-'\n• આલ્કોહોલ (-OH): પ્રત્યય '-ઓલ' (ઇથેનોલ)\n• આલ્ડીહાઇડ (-CHO): પ્રત્યય '-આલ' (ઇથેનાલ)\n• કીટોન (-CO-): પ્રત્યય '-ઓન' (પ્રોપેનોન)\n• કાર્બોક્સિલિક એસિડ (-COOH): પ્રત્યય '-ઓઇક એસિડ' (ઇથેનોઇક એસિડ)"
    })

    # 4. Theory
    blocks.append({
        "id": next_id(),
        "type": "theory",
        "title": "Comprehensive IUPAC Nomenclature Guide",
        "title_hi": "समग्र IUPAC नामकरण मार्गदर्शिका",
        "title_gu": "સમગ્ર IUPAC નામકરણ માર્ગદર્શિકા",
        "body": "Step-by-Step Naming Algorithm:\nStep 1: Identify the longest continuous chain of carbon atoms. This establishes the root word.\nStep 2: Check for presence of functional groups or unsaturation (double/triple bonds).\nStep 3: Number the carbon chain from the end that gives the lowest locant number to the functional group.\nStep 4: If a functional group suffix begins with a vowel (a, e, i, o, u), drop the terminal 'e' from the alkane name (e.g., Propane + ol -> Propanol; Butane + oic acid -> Butanoic acid).\nStep 5: For haloalkanes, use prefix format: e.g., CH3-CH2-Cl is Chloroethane; CH3-CH2-CH2-Br is 1-Bromopropane.\n\nExamples:\n• HCHO: 1 Carbon + Aldehyde = Methanal (Formaldehyde)\n• CH3COOH: 2 Carbons + Carboxylic acid = Ethanoic acid (Acetic acid)\n• CH3COCH3: 3 Carbons + Ketone = Propanone (Acetone)\n• CH3-CH=CH2: 3 Carbons + Double bond = Propene",
        "body_hi": "IUPAC नामकरण के चरण:\nचरण 1: कार्बन परमाणुओं की सबसे लंबी सतत श्रृंखला की पहचान करें (मूल शब्द)।\nचरण 2: प्रकार्यात्मक समूह या द्वि/त्रि-बंध की उपस्थिति की जांच करें।\nचरण 3: कार्बन श्रृंखला को उस सिरे से क्रमांकित करें जिससे प्रकार्यात्मक समूह को न्यूनतम संख्या मिले।\nचरण 4: यदि प्रत्यय स्वर (a, e, i, o, u) से शुरू होता है, तो ऐल्केन नाम के अंत से 'e' हटा दें (जैसे Propane + ol -> Propanol)।\nचरण 5: हैलोऐल्केन के लिए पूर्वसर्ग रूप का उपयोग करें (जैसे CH3CH2Cl -> क्लोरोएथेन)।\n\nमहत्वपूर्ण उदाहरण:\n• HCHO: 1 कार्बन + ऐल्डिहाइड = मेथेनल (फॉर्मेल्डिहाइड)\n• CH3COOH: 2 कार्बन + कार्बोक्सिलिक अम्ल = एथेनॉइक अम्ल (एसिटिक एसिड)\n• CH3COCH3: 3 कार्बन + कीटोन = प्रोपेनॉन (एसीटोन)\n• CH3-CH=CH2: 3 कार्बन + द्वि-बंध = प्रोपीन",
        "body_gu": "IUPAC નામકરણના પગલાં:\nપગલું 1: કાર્બન પરમાણુઓની સૌથી લાંબી સતત શૃંખલા નક્કી કરો (મૂળ શબ્દ).\nપગલું 2: ક્રિયાશીલ સમૂહ અથવા દ્વિ/ત્રિ-બંધ તપાસો.\nપગલું 3: જે છેડેથી ક્રિયાશીલ સમૂહ નજીક હોય તે છેડેથી નંબર આપો.\nપગલું 4: જો પ્રત્યય સ્વરથી શરૂ થતો હોય તો એલ્કેનના નામના છેડેથી 'e' દૂર કરો (જેમ કે Propane + ol -> Propanol).\nપગલું 5: હેલોએલ્કેન માટે પૂર્વગ વાપરો (જેમ કે CH3CH2Cl -> ક્લોરોઇથેન).\n\nમુખ્ય ઉદાહરણો:\n• HCHO: 1 કાર્બન + આલ્ડીહાઇડ = મિથેનાલ (ફોર્માલ્ડિહાઇડ)\n• CH3COOH: 2 કાર્બન + કાર્બોક્સિલિક એસિડ = ઇથેનોઇક એસિડ (એસિટિક એસિડ)\n• CH3COCH3: 3 કાર્બન + કીટોન = પ્રોપેનોન (એસિટોન)\n• CH3-CH=CH2: 3 કાર્બન + દ્વિ-બંધ = પ્રોપીન"
    })

    # Teacher Tip
    blocks.append({
        "id": next_id(),
        "type": "teacher_tip",
        "title": "Teacher Tip: The Carbon in -CHO and -COOH Counts in the Chain!",
        "title_hi": "शिक्षक टिप: -CHO और -COOH का कार्बन भी मुख्य श्रृंखला में गिना जाता है!",
        "title_gu": "શિક્ષક ટિપ: -CHO અને -COOH નો કાર્બન પણ મુખ્ય શૃંખલામાં ગણાય છે!",
        "body": "A very frequent mistake: In CH3-CH2-COOH, students see an ethyl group (2 carbons) and call it 'Ethanoic acid'. WRONG! The carbon inside the -COOH group is Carbon #1! Total carbons = 1 + 2 = 3, so its correct name is PROPANOIC ACID. Always count the carbonyl carbon in -CHO and -COOH!",
        "body_hi": "एक बहुत आम गलती: CH3-CH2-COOH में, छात्र एथिल समूह (2 कार्बन) देखते हैं और इसे 'एथेनॉइक अम्ल' कहते हैं। यह गलत है! -COOH समूह का कार्बन भी गिना जाता है। कुल कार्बन = 3 हैं, इसलिए सही नाम प्रोपेनॉइक अम्ल (Propanoic acid) है।",
        "body_gu": "વારંવાર થતી ભૂલ: CH3-CH2-COOH માં વિદ્યાર્થીઓ 2 કાર્બન જોઈને તેને 'ઇથેનોઇક એસિડ' કહી દે છે. આ ખોટું છે! -COOH ના કાર્બન સહિત કુલ 3 કાર્બન થાય છે, આથી સાચું નામ પ્રોપેનોઇક એસિડ છે."
    })

    # Common Mistake
    blocks.append({
        "id": next_id(),
        "type": "teacher_tip",
        "title": "Common Mistake: Confusing Butanone with Butanal",
        "title_hi": "सामान्य गलती: ब्यूटेनॉन को ब्यूटेनल समझना",
        "title_gu": "સામાન્ય ભૂલ: બ્યુટેનોન અને બ્યુટેનાલ વચ્ચે ગેરસમજ",
        "body": "Butanone (CH3-CO-CH2-CH3) has the >C=O ketone group in the middle of the chain. Butanal (CH3-CH2-CH2-CHO) has the -CHO aldehyde group at the terminal end. They have the same formula (C4H8O) but belong to entirely different functional classes.",
        "body_hi": "ब्यूटेनॉन (CH3-CO-CH2-CH3) में कीटोन समूह श्रृंखला के बीच में होता है। ब्यूटेनल (CH3-CH2-CH2-CHO) में ऐल्डिहाइड समूह किनारे पर होता है। दोनों का सूत्र C4H8O है लेकिन वे पूरी तरह से अलग प्रकार्यात्मक वर्गों से हैं।",
        "body_gu": "બ્યુટેનોન (CH3-CO-CH2-CH3) માં કીટોન સમૂહ વચ્ચે હોય છે. બ્યુટેનાલ (CH3-CH2-CH2-CHO) માં આલ્ડીહાઇડ સમૂહ છેડે હોય છે. બંનેનું સૂત્ર C4H8O છે પરંતુ ક્રિયાશીલ સમૂહ જુદો છે."
    })

    # 5. Knowledge Check
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "What is the correct IUPAC name of the compound CH3-CH2-CH2-CH2-C≡CH?",
        "question_hi": "यौगिक CH3-CH2-CH2-CH2-C≡CH का सही IUPAC नाम क्या है?",
        "question_gu": "સંયોજન CH3-CH2-CH2-CH2-C≡CH નું સાચું IUPAC નામ કયું છે?",
        "options": [
            "Hex-1-yne",
            "Hex-1-ene",
            "Hexane",
            "Pent-1-yne"
        ],
        "options_hi": [
            "हेक्स-1-आइन (Hex-1-yne)",
            "हेक्स-1-ईन (Hex-1-ene)",
            "हेक्सेन (Hexane)",
            "पेन्ट-1-आइन (Pent-1-yne)"
        ],
        "options_gu": [
            "હેક્સ-1-આઇન (Hex-1-yne)",
            "હેક્સ-1-ઇન (Hex-1-ene)",
            "હેક્ઝેન (Hexane)",
            "પેન્ટ-1-આઇન (Pent-1-yne)"
        ],
        "correct_index": 0,
        "explanation": "The molecule has a 6-carbon continuous chain (Hex-) with a triple bond (-yne) at carbon #1. Thus, its systematic name is Hex-1-yne (or 1-hexyne).",
        "explanation_hi": "अणु में 6 कार्बन की श्रृंखला (Hex-) है जिसमें कार्बन #1 पर त्रि-बंध (-yne) है। इसलिए इसका नाम हेक्स-1-आइन (Hex-1-yne) है।",
        "explanation_gu": "આ અણુમાં 6 કાર્બનની શૃંખલા (હેક્સ-) અને પ્રથમ કાર્બન પર ત્રિ-બંધ (-આઇન) આવેલો હોવાથી સાચું નામ હેક્સ-1-આઇન છે."
    })

    # 6. Reflection
    blocks.append({
        "id": next_id(),
        "type": "reflection",
        "title": "Nomenclature is the Foundation of Organic Communication",
        "title_hi": "नामकरण कार्बनिक संचार की आधारशिला है",
        "title_gu": "નામકરણ એ કાર્બનિક રસાયણની સંચાર ભાષા છે",
        "body": "When pharmaceutical companies discover a new drug with 40 carbon atoms and 5 functional groups, the IUPAC name communicates the exact connectivity of every bond and atom without ambiguity, ensuring doctors and pharmacists manufacture the exact lifesaving molecule.",
        "body_hi": "जब फार्मास्युटिकल कंपनियां 40 कार्बन परमाणुओं और 5 प्रकार्यात्मक समूहों वाली एक नई दवा की खोज करती हैं, तो IUPAC नाम बिना किसी अस्पष्टता के हर बंध और परमाणु की सटीक संरचना बताता है, जिससे सटीक जीवनरक्षक दवा बनाई जा सके।",
        "body_gu": "જ્યારે ફાર્માસ્યુટિકલ કંપનીઓ નવી દવા શોધે છે, ત્યારે IUPAC નામ તેના દરેક પરમાણુનું ચોક્કસ જોડાણ દર્શાવે છે જેથી વિશ્વમાં ગમે ત્યાં તે જ સાચી દવા બનાવી શકાય."
    })

    # 7. Connection
    blocks.append({
        "id": next_id(),
        "type": "connection",
        "title": "Commercial Common Names vs Systematic Names",
        "title_hi": "वाणिज्यिक सामान्य नाम बनाम व्यवस्थित नाम",
        "title_gu": "વાણિજ્યિક સામાન્ય નામો વિરુદ્ધ પદ્ધતિસરના નામો",
        "body": "In daily commerce, people use common historical names: Nail polish remover is sold as 'Acetone' (IUPAC: Propanone). Salad dressing uses 'Vinegar' (dilute Ethanoic acid). Ant bites inject 'Formic acid' (IUPAC: Methanoic acid). Knowing both common and IUPAC names bridges everyday life with scientific chemistry.",
        "body_hi": "दैनिक जीवन में लोग सामान्य नामों का उपयोग करते हैं: नेल पॉलिश रिमूवर 'एसीटोन' (IUPAC: प्रोपेनॉन) है। सिरका 'एसिटिक एसिड' (IUPAC: एथेनॉइक अम्ल) है। चींटी के डंक में 'फॉर्मिक एसिड' (IUPAC: मेथेनॉइक अम्ल) होता है।",
        "body_gu": "રોજિંદા જીવનમાં નેઇલ પોલીશ રીમુવર તરીકે 'એસિટોન' (IUPAC: પ્રોપેનોન) વપરાય છે. સરકામાં 'એસિટિક એસિડ' (IUPAC: ઇથેનોઇક એસિડ) હોય છે. કીડીના ડંખમાં 'ફોર્મિક એસિડ' (IUPAC: મિથેનોઇક એસિડ) હોય છે."
    })

    # 8. Mastery Challenge
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "Which of the following represents the correct IUPAC name for CH3-CH(OH)-CH3?",
        "question_hi": "CH3-CH(OH)-CH3 के लिए निम्नलिखित में से कौन सा सही IUPAC नाम दर्शाता है?",
        "question_gu": "CH3-CH(OH)-CH3 માટે નીચેનામાંથી કયું સાચું IUPAC નામ દર્શાવે છે?",
        "options": [
            "Propan-2-ol",
            "Propan-1-ol",
            "Propanal",
            "Propanoic acid"
        ],
        "options_hi": [
            "प्रोपेन-2-ऑल (Propan-2-ol)",
            "प्रोपेन-1-ऑल (Propan-1-ol)",
            "प्रोपेनल (Propanal)",
            "प्रोपेनॉइक अम्ल (Propanoic acid)"
        ],
        "options_gu": [
            "પ્રોપેન-2-ઓલ (Propan-2-ol)",
            "પ્રોપેન-1-ઓલ (Propan-1-ol)",
            "પ્રોપેનાલ (Propanal)",
            "પ્રોપેનોઇક એસિડ (Propanoic acid)"
        ],
        "correct_index": 0,
        "explanation": "The 3-carbon parent chain is Propane. The alcohol -OH functional group is attached to carbon #2. Therefore, the IUPAC name is Propan-2-ol (commonly known as Isopropyl alcohol).",
        "explanation_hi": "3-कार्बन वाली मुख्य श्रृंखला प्रोपेन है। ऐल्कोहॉल -OH समूह कार्बन #2 से जुड़ा है। इसलिए IUPAC नाम प्रोपेन-2-ऑल (Propan-2-ol) है।",
        "explanation_gu": "3 કાર્બનની શૃંખલા પ્રોપેન છે અને બીજા કાર્બન પર -OH સમૂહ આવેલો હોવાથી IUPAC નામ પ્રોપેન-2-ઓલ થાય છે."
    })

    # =========================================================================
    # MODULE 5: CHEMICAL PROPERTIES OF CARBON COMPOUNDS (8-STEP PEDAGOGY)
    # =========================================================================

    # 1. Hook
    blocks.append({
        "id": next_id(),
        "type": "hook",
        "title": "The Fire That Built Human Civilization",
        "title_hi": "वह आग जिसने मानव सभ्यता का निर्माण किया",
        "title_gu": "માનવ સંસ્કૃતિનું નિર્માણ કરનાર અગ્નિ",
        "body": "From the first campfire of prehistoric humans to internal combustion car engines and rocket boosters, almost all energy that powers human civilization comes from burning carbon compounds. But why does wood or wax burn with a yellow, smoky, flickering flame that blackens pots, while LPG burns with a clean, sizzling blue flame? What chemical reactions take place inside carbon flames?",
        "body_hi": "प्रागैतिहासिक मानव की पहली अलाव से लेकर कारों के इंजन और रॉकेट बूस्टर तक, मानव सभ्यता को संचालित करने वाली लगभग सभी ऊर्जा कार्बन यौगिकों के जलने से आती है। लेकिन लकड़ी या मोमबत्ती पीली, धुएँ वाली ज्वाला से क्यों जलती है जो बर्तनों को काला कर देती है, जबकि एलपीजी नीली स्वच्छ ज्वाला से क्यों जलती है?",
        "body_gu": "આદિમાનવના પ્રથમ તાપણાથી લઈને આજના રોકેટ સુધી, માનવ સંસ્કૃતિને ઉર્જા આપતું મુખ્ય બળતણ કાર્બન સંયોજનો છે. પરંતુ મીણબત્તી ધુમાડાવાળી પીળી જ્યોતથી સળગીને વાસણો કાળા કેમ કરે છે, જ્યારે LPG ગેસ સ્વચ્છ ભૂરી જ્યોતથી કેમ સળગે છે?"
    })

    # 2. Socratic Question
    blocks.append({
        "id": next_id(),
        "type": "socratic_question",
        "question": "Why do saturated hydrocarbons burn with a clean blue flame in excess air, while unsaturated hydrocarbons burn with a yellow sooty flame?",
        "question_hi": "हवा की अधिकता में संतृप्त हाइड्रोकार्बन नीली स्वच्छ ज्वाला से क्यों जलते हैं, जबकि असंतृप्त हाइड्रोकार्बन पीली धुएँ वाली ज्वाला से क्यों जलते हैं?",
        "question_gu": "પૂરતી હવા મળતાં સંતૃપ્ત હાઇડ્રોકાર્બન સ્વચ્છ ભૂરી જ્યોતથી કેમ સળગે છે, જ્યારે અસંતૃપ્ત હાઇડ્રોકાર્બન ધુમાડાવાળી પીળી જ્યોત આપે છે?",
        "options": [
            "Unsaturated hydrocarbons have a much higher percentage of carbon, leading to unburnt glowing carbon soot particles.",
            "Saturated hydrocarbons contain non-flammable nitrogen gas.",
            "Unsaturated hydrocarbons cannot react with oxygen at all.",
            "Saturated hydrocarbons have higher density than unsaturated ones."
        ],
        "options_hi": [
            "असंतृप्त हाइड्रोकार्बन में कार्बन का प्रतिशत बहुत अधिक होता है, जिससे बिना जले चमकते कार्बन कण (कालिख) बनते हैं।",
            "संतृप्त हाइड्रोकार्बन में गैर-ज्वलनशील नाइट्रोजन गैस होती है।",
            "असंतृप्त हाइड्रोकार्बन ऑक्सीजन से बिल्कुल भी प्रतिक्रिया नहीं कर सकते।",
            "संतृप्त हाइड्रोकार्बन का घनत्व असंतृप्त से अधिक होता है।"
        ],
        "options_gu": [
            "અસંતૃપ્ત હાઇડ્રોકાર્બનમાં કાર્બનની ટકાવારી ખૂબ ઊંચી હોવાથી અપૂર્ણ દહનને લીધે કાર્બનના કણો (મેશ) ધુમાડા સ્વરૂપે ઊડે છે.",
            "સંતૃપ્ત હાઇડ્રોકાર્બનમાં નાઇટ્રોજન વાયુ હોય છે.",
            "અસંતૃપ્ત હાઇડ્રોકાર્બન સળગી શકતા નથી.",
            "સંતૃપ્ત હાઇડ્રોકાર્બનની ઘનતા વધુ હોય છે."
        ],
        "correct_index": 0,
        "explanation": "Unsaturated hydrocarbons contain double and triple bonds and possess a higher carbon-to-hydrogen ratio. Complete combustion requires more oxygen; in normal air, incomplete combustion occurs, producing incandescent unburnt carbon particles (soot) that emit a luminous yellow flame.",
        "explanation_hi": "असंतृप्त हाइड्रोकार्बन में कार्बन का प्रतिशत अधिक होता है। सामान्य हवा में उनका पूर्ण दहन नहीं हो पाता, जिससे बिना जले कार्बन कण (कालिख) बनते हैं जो पीली धुएँ वाली ज्वाला उत्सर्जित करते हैं।",
        "explanation_gu": "અસંતૃપ્ત હાઇડ્રોકાર્બનમાં કાર્બનનું પ્રમાણ વધુ હોવાથી તેનું સામાન્ય હવામાં સંપૂર્ણ દહન થતું નથી અને ન સળગેલા કાર્બન કણો પીળી ધુમાડાવાળી જ્યોત બનાવે છે."
    })

    # 3. Discovery
    blocks.append({
        "id": next_id(),
        "type": "discovery",
        "title": "The Four Great Reactions of Carbon Chemistry",
        "title_hi": "कार्बन रसायन की चार महान अभिक्रियाएं",
        "title_gu": "કાર્બન રસાયણની ચાર મહાન પ્રક્રિયાઓ",
        "body": "All carbon compounds undergo four fundamental chemical transformations:\n\n1. COMBUSTION:\nCarbon and hydrocarbons burn in oxygen to release CO2, H2O, and huge amounts of heat and light.\n• C + O2 -> CO2 + Heat & Light\n• CH4 + 2O2 -> CO2 + 2H2O + Heat & Light\n\n2. OXIDATION:\nCarbon compounds can be oxidized using strong oxidizing agents such as ALKALINE KMnO4 (Potassium permanganate) or ACIDIFIED K2Cr2O7 (Potassium dichromate).\n• Ethanol is oxidized to Ethanoic acid:\n  CH3-CH2OH --[Alkaline KMnO4 + Heat]--> CH3-COOH\n\n3. ADDITION REACTION:\nUnsaturated hydrocarbons add hydrogen across double/triple bonds in the presence of catalysts like NICKEL (Ni) or PALLADIUM (Pd) to form saturated hydrocarbons:\n• Vegetable Oil (liquid, unsaturated) + H2 --[Ni catalyst]--> Vanaspati Ghee (solid, saturated)\n\n4. SUBSTITUTION REACTION:\nIn saturated hydrocarbons, inert single bonds do not add atoms. However, in presence of SUNLIGHT, Chlorine displaces hydrogen atoms one by one:\n• CH4 + Cl2 --[Sunlight]--> CH3Cl + HCl",
        "body_hi": "सभी कार्बन यौगिक चार मूलभूत रासायनिक अभिक्रियाएं करते हैं:\n\n1. दहन (Combustion):\nकार्बन और हाइड्रोकार्बन ऑक्सीजन में जलकर CO2, जल और अत्यधिक ऊष्मा व प्रकाश देते हैं।\n• CH4 + 2O2 -> CO2 + 2H2O + ऊष्मा और प्रकाश\n\n2. ऑक्सीकरण (Oxidation):\nक्षारीय KMnO4 या अम्लीकृत K2Cr2O7 जैसे प्रबल ऑक्सीकारकों द्वारा ऐल्कोहॉल को कार्बोक्सिलिक अम्ल में बदला जाता है।\n• CH3-CH2OH --[क्षारीय KMnO4 + ऊष्मा]--> CH3-COOH\n\n3. संकलन अभिक्रिया (Addition Reaction):\nनिकेल (Ni) या पैलेडियम उत्प्रेरक की उपस्थिति में असंतृप्त हाइड्रोकार्बन हाइड्रोजन जोड़कर संतृप्त बन जाते हैं (तेलों का हाइड्रोजनकरण)।\n\n4. प्रतिस्थापन अभिक्रिया (Substitution Reaction):\nसूर्य के प्रकाश की उपस्थिति में क्लोरीन संतृप्त हाइड्रोकार्बन से हाइड्रोजन परमाणुओं को एक-एक करके प्रतिस्थापित करती है:\n• CH4 + Cl2 --[सूर्य का प्रकाश]--> CH3Cl + HCl",
        "body_gu": "કાર્બન સંયોજનોની ચાર મુખ્ય રાસાયણિક પ્રક્રિયાઓ:\n\n1. દહન (Combustion):\nહાઇડ્રોકાર્બન ઓક્સિજનમાં સળગીને CO2, પાણી, પુષ્કળ ઉષ્મા અને પ્રકાશ મુક્ત કરે છે.\n• CH4 + 2O2 -> CO2 + 2H2O + ઉષ્મા અને પ્રકાશ\n\n2. ઓક્સિડેશન (Oxidation):\nઆલ્કલાઇન KMnO4 કે એસિડિક K2Cr2O7 જેવા ઓક્સિડેશનકર્તા દ્વારા આલ્કોહોલનું કાર્બોક્સિલિક એસિડમાં રૂપાંતર થાય છે.\n• CH3-CH2OH --[Alkaline KMnO4]--> CH3-COOH\n\n3. યોગશીલ પ્રક્રિયા (Addition Reaction):\nનિકલ (Ni) ઉદ્દીપકની હાજરીમાં અસંતૃપ્ત હાઇડ્રોકાર્બનમાં H2 ઉમેરાઈને સંતૃપ્ત હાઇડ્રોકાર્બન બને છે (વનસ્પતિ તેલમાંથી વનસ્પતિ ઘી).\n\n4. વિસ્થાપન પ્રક્રિયા (Substitution Reaction):\nસૂર્યપ્રકાશની હાજરીમાં ક્લોરિન સંતૃપ્ત હાઇડ્રોકાર્બનમાંથી એક પછી એક હાઇડ્રોજનનું વિસ્થાપન કરે છે:\n• CH4 + Cl2 --[સૂર્યપ્રકાશ]--> CH3Cl + HCl"
    })

    # 4. Theory
    blocks.append({
        "id": next_id(),
        "type": "theory",
        "title": "Industrial Applications: Hydrogenation & Catalysts",
        "title_hi": "औद्योगिक अनुप्रयोग: हाइड्रोजनकरण और उत्प्रेरक",
        "title_gu": "ઔદ્યોગિક ઉપયોગો: હાઇડ્રોજનીકરણ અને ઉદ્દીપકો",
        "body": "Detailed Study of Chemical Reactions:\n\n1. HYDROGENATION OF OILS:\n• Liquid vegetable oils contain long unsaturated carbon chains with double bonds (healthy, containing unsaturated fatty acids).\n• When hydrogen gas is bubbled through vegetable oil at ~200°C in the presence of finely divided Nickel catalyst, the C=C double bonds open up, adding hydrogen atoms to become single bonds (C-C).\n• The resulting product is solid saturated fat (Vanaspati Ghee or margarine).\n• Health Note: Saturated animal fats/ghee are harmful to cardiovascular health; unsaturated vegetable oils should always be chosen for daily cooking.\n\n2. OXIDIZING AGENTS:\nSubstances that add oxygen to or remove hydrogen from other substances are called Oxidizing Agents. Alkaline Potassium Permanganate (KMnO4) and Acidified Potassium Dichromate (K2Cr2O7) supply nascent oxygen to oxidize ethanol.\n\n3. PHOTOCHEMICAL CHLORINATION:\nIn the dark, methane and chlorine do not react. In diffused sunlight, chlorine radicals are formed, causing rapid step-by-step substitution:\nCH4 -> CH3Cl (Chloromethane) -> CH2Cl2 (Dichloromethane) -> CHCl3 (Chloroform) -> CCl4 (Carbon tetrachloride).",
        "body_hi": "रासायनिक अभिक्रियाओं का विस्तृत अध्ययन:\n\n1. तेलों का हाइड्रोजनकरण:\n• वनस्पति तेलों में असंतृप्त कार्बन श्रृंखलाएं होती हैं (स्वास्थ्य के लिए अच्छे असंतृप्त फैटी एसिड)।\n• निकेल (Ni) उत्प्रेरक की उपस्थिति में हाइड्रोजन गैस प्रवाहित करने पर द्वि-बंध एकल बंध में बदल जाते हैं और ठोस वनस्पति घी बनता है।\n• स्वास्थ्य नोट: संतृप्त वसा हृदय स्वास्थ्य के लिए हानिकारक होती है; भोजन पकाने के लिए असंतृप्त तेलों का उपयोग करना चाहिए।\n\n2. ऑक्सीकारक:\nवे पदार्थ जो अन्य पदार्थों को ऑक्सीजन देने में सक्षम होते हैं, ऑक्सीकारक कहलाते हैं (जैसे क्षारीय KMnO4 और अम्लीकृत K2Cr2O7)।\n\n3. मीथेन का क्लोरीनीकरण:\nसूर्य के प्रकाश में क्लोरीन मीथेन के साथ चरणबद्ध प्रतिस्थापन करती है: CH4 -> CH3Cl -> CH2Cl2 -> CHCl3 -> CCl4।",
        "body_gu": "રાસાયણિક પ્રક્રિયાઓનો વિગતવાર અભ્યાસ:\n\n1. તેલનું હાઇડ્રોજનીકરણ:\n• પ્રવાહી વનસ્પતિ તેલ અસંતૃપ્ત કાર્બન શૃંખલા ધરાવે છે જે સ્વાસ્થ્ય માટે હિતકારી છે.\n• નિકલ ઉદ્દીપકની હાજરીમાં હાઇડ્રોજન વાયુ પસાર કરતાં દ્વિ-બંધ તૂટીને સંતૃપ્ત ઘન વનસ્પતિ ઘી બને છે.\n• સ્વાસ્થ્ય નોંધ: સંતૃપ્ત ચરબી હૃદય માટે હાનિકારક છે, રસોઈમાં અસંતૃપ્ત તેલ વાપરવું જોઈએ.\n\n2. ઓક્સિડેશનકર્તા પદાર્થો:\nજે પદાર્થો અન્યને ઓક્સિજન ઉમેરી શકે તેને ઓક્સિડેશનકર્તા કહેવાય છે (જેમ કે આલ્કલાઇન KMnO4 અને એસિડિક K2Cr2O7).\n\n3. મિથેનનું ક્લોરીનેશન:\nસૂર્યપ્રકાશમાં ક્લોરિન ક્રમશઃ હાઇડ્રોજનનું વિસ્થાપન કરી CH3Cl, CH2Cl2, CHCl3 અને CCl4 બનાવે છે."
    })

    # Teacher Tip
    blocks.append({
        "id": next_id(),
        "type": "teacher_tip",
        "title": "Teacher Tip: How to Distinguish Saturated vs Unsaturated Chemically",
        "title_hi": "शिक्षक टिप: संतृप्त और असंतृप्त यौगिकों में रासायनिक अंतर कैसे करें",
        "title_gu": "શિક્ષક ટિપ: સંતૃપ્ત અને અસંતૃપ્ત સંયોજનો વચ્ચે રાસાયણિક કસોટી",
        "body": "The Bromine Water Test is the definitive test! Bromine water is reddish-brown. When shaken with an UNSATURATED compound (like cooking oil, ethene, or propene), the reddish-brown colour rapidly disappears (decolourization via addition reaction). Saturated compounds (like butter or alkanes) show NO reaction and the colour remains reddish-brown.",
        "body_hi": "ब्रोमीन जल परीक्षण निर्णायक परीक्षण है! ब्रोमीन जल लाल-भूरे रंग का होता है। जब इसे असंतृप्त यौगिक (जैसे खाना पकाने का तेल) के साथ हिलाया जाता है, तो लाल-भूरा रंग गायब हो जाता है (रंगहीन)। संतृप्त यौगिक (जैसे मक्खन) ब्रोमीन जल का रंग नहीं उड़ाते।",
        "body_gu": "બ્રોમિન જળ કસોટી સૌથી નિર્ણાયક છે! બ્રોમિન જળ લાલાશ પડતો કથ્થાઈ રંગ ધરાવે છે. અસંતૃપ્ત સંયોજન (રસોઈનું તેલ) સાથે હલાવતાં તેનો રંગ દૂર થઈ જાય છે. સંતૃપ્ત સંયોજન (માખણ) બ્રોમિન જળનો રંગ દૂર કરતું નથી."
    })

    # Common Mistake
    blocks.append({
        "id": next_id(),
        "type": "teacher_tip",
        "title": "Common Mistake: Thinking Alkanes Undergo Addition Reactions",
        "title_hi": "सामान्य गलती: यह सोचना कि ऐल्केन संकलन अभिक्रियाएं करते हैं",
        "title_gu": "સામાન્ય ભૂલ: એલ્કેન યોગશીલ પ્રક્રિયા આપે છે તેવી ગેરસમજ",
        "body": "Students often write that methane or ethane can add hydrogen or chlorine. Impossible! In alkanes, all 4 valence bonds of every carbon are fully occupied by single bonds. There are no spare bonds to open up. Therefore, alkanes CANNOT undergo addition reactions; they ONLY undergo substitution reactions!",
        "body_hi": "छात्र अक्सर लिखते हैं कि मीथेन या एथेन हाइड्रोजन जोड़ सकते हैं। यह असंभव है! ऐल्केन में सभी बंध पूरी तरह से एकल बंधों से भरे होते हैं। इसलिए ऐल्केन संकलन अभिक्रियाएं नहीं कर सकते; वे केवल प्रतिस्थापन अभिक्रियाएं करते हैं!",
        "body_gu": "વિદ્યાર્થીઓ ઘણીવાર માને છે કે મિથેન કે ઇથેન હાઇડ્રોજન ઉમેરી શકે છે. આ અશક્ય છે! એલ્કેનમાં ચારેય સંયોજકતા એકલ બંધથી સંતૃપ્ત હોય છે. તેથી એલ્કેન ક્યારેય યોગશીલ પ્રક્રિયા આપતા નથી, માત્ર વિસ્થાપન પ્રક્રિયા જ આપે છે!"
    })

    # 5. Knowledge Check
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "Which of the following catalysts is commonly used in the industrial hydrogenation of vegetable oils?",
        "question_hi": "वनस्पति तेलों के औद्योगिक हाइड्रोजनकरण में आमतौर पर निम्नलिखित में से किस उत्प्रेरक का उपयोग किया जाता है?",
        "question_gu": "વનસ્પતિ તેલના ઔદ્યોગિક હાઇડ્રોજનીકરણમાં નીચેનામાંથી કયો ઉદ્દીપક સામાન્ય રીતે વપરાય છે?",
        "options": [
            "Nickel (Ni) or Palladium (Pd)",
            "Iron (Fe)",
            "Copper (Cu)",
            "Zinc (Zn)"
        ],
        "options_hi": [
            "निकेल (Ni) या पैलेडियम (Pd)",
            "लोहा (Fe)",
            "तांबा (Cu)",
            "जिंक (Zn)"
        ],
        "options_gu": [
            "નિકલ (Ni) અથવા પેલેડિયમ (Pd)",
            "લોખંડ (Fe)",
            "તાંબુ (Cu)",
            "ઝીંક (Zn)"
        ],
        "correct_index": 0,
        "explanation": "Finely divided Nickel (Ni) or Palladium (Pd) acts as a heterogeneous catalyst to adsorb hydrogen molecules and lower the activation energy for addition across C=C double bonds in vegetable oils.",
        "explanation_hi": "बारीक पिसा हुआ निकेल (Ni) या पैलेडियम (Pd) एक उत्प्रेरक के रूप में कार्य करता है जो हाइड्रोजन को सोखता है और वनस्पति तेलों में C=C द्वि-बंधों पर जुड़ने के लिए सक्रियण ऊर्जा को कम करता है।",
        "explanation_gu": "ઝીણું વહેંચાયેલું નિકલ (Ni) અથવા પેલેડિયમ (Pd) ઉદ્દીપક તરીકે વર્તીને C=C દ્વિ-બંધ પર હાઇડ્રોજન ઉમેરવાની પ્રક્રિયા ઝડપી બનાવે છે."
    })

    # 6. Reflection
    blocks.append({
        "id": next_id(),
        "type": "reflection",
        "title": "Dietary Chemistry: Trans Fats & Heart Health",
        "title_hi": "आहार रसायन: ट्रांस फैट्स और हृदय स्वास्थ्य",
        "title_gu": "આહાર રસાયણશાસ્ત્ર: ટ્રાન્સ ફેટ્સ અને હૃદયનું સ્વાસ્થ્ય",
        "body": "When liquid vegetable oils are partially hydrogenated to create bakery shortenings and vanaspati ghee, unhealthy 'trans-fats' are produced. These raise bad cholesterol (LDL) and clog arteries. Modern health guidelines recommend replacing saturated and trans fats with cold-pressed unsaturated vegetable oils (like mustard, sunflower, and olive oil).",
        "body_hi": "जब वनस्पति तेलों का आंशिक हाइड्रोजनकरण किया जाता है, तो अस्वास्थ्यकर 'ट्रांस-फैट' बनते हैं जो खराब कोलेस्ट्रॉल को बढ़ाते हैं और धमनियों को अवरुद्ध करते हैं। आधुनिक पोषण विशेषज्ञ संतृप्त वसा के स्थान पर असंतृप्त वनस्पति तेलों के उपयोग की सलाह देते हैं।",
        "body_gu": "જ્યારે વનસ્પતિ તેલનું હાઇડ્રોજનીકરણ કરવામાં આવે છે, ત્યારે અનિચ્છનીય 'ટ્રાન્સ ફેટ' બને છે જે હૃદયની નળીઓમાં કોલેસ્ટ્રોલ જમા કરે છે. આથી ખોરાકમાં અસંતૃપ્ત વનસ્પતિ તેલ વાપરવું આરોગ્યપ્રદ છે."
    })

    # 7. Connection
    blocks.append({
        "id": next_id(),
        "type": "connection",
        "title": "Why Chimneys and Stove Burners Have Air Holes",
        "title_hi": "चिमनी और गैस बर्नर में हवा के छेद क्यों होते हैं",
        "title_gu": "ગેસ બર્નર અને ચીમનીમાં હવા માટે કાણાં કેમ હોય છે",
        "body": "Ever notice the small adjustable air holes at the base of your gas stove burner? If food spills and blocks these holes, insufficient oxygen enters. The fuel burns incompletely with a yellow, smoky flame and blackens cooking vessels. Cleaning the holes restores oxygen flow, producing a clean, high-temperature blue flame.",
        "body_hi": "क्या आपने कभी गैस स्टोव बर्नर के नीचे छोटे हवा के छेदों को देखा है? यदि खाना गिरकर इन छेदों को बंद कर देता है, तो अपर्याप्त ऑक्सीजन मिलती है। ईंधन अपूर्ण रूप से जलकर पीली धुएँ वाली ज्वाला देता है और बर्तन काले पड़ जाते हैं। छेदों को साफ करने से फिर से नीली ज्वाला मिलने लगती है।",
        "body_gu": "ગેસના ચૂલાના બર્નરમાં નીચે હવા આવવા માટે કાણાં હોય છે. જો તે કાણાં પૂરાઈ જાય, તો ઓક્સિજન ઓછો મળવાથી પીળી ધુમાડાવાળી જ્યોત થાય છે અને વાસણો કાળા પડે છે. કાણાં સાફ કરતાં ફરી સ્વચ્છ ભૂરી જ્યોત મળે છે."
    })

    # 8. Mastery Challenge
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "Which of the following reactions describes the conversion of Ethanol to Ethanoic acid?",
        "question_hi": "निम्नलिखित में से कौन सी अभिक्रिया एथेनॉल के एथेनॉइक अम्ल में परिवर्तन का वर्णन करती है?",
        "question_gu": "નીચેનામાંથી કઈ પ્રક્રિયા ઇથેનોલનું ઇથેનોઇક એસિડમાં રૂપાંતર દર્શાવે છે?",
        "options": [
            "Oxidation reaction using alkaline KMnO4 or acidified K2Cr2O7",
            "Addition reaction using Nickel catalyst",
            "Substitution reaction using Chlorine in sunlight",
            "Combustion reaction releasing carbon dioxide and water"
        ],
        "options_hi": [
            "क्षारीय KMnO4 या अम्लीकृत K2Cr2O7 का उपयोग करके ऑक्सीकरण अभिक्रिया",
            "निकेल उत्प्रेरक का उपयोग करके संकलन अभिक्रिया",
            "सूर्य के प्रकाश में क्लोरीन का उपयोग करके प्रतिस्थापन अभिक्रिया",
            "कार्बन डाइऑक्साइड और पानी छोड़ने वाली दहन अभिक्रिया"
        ],
        "options_gu": [
            "આલ્કલાઇન KMnO4 અથવા એસિડિક K2Cr2O7 વડે ઓક્સિડેશન પ્રક્રિયા",
            "નિકલ ઉદ્દીપક વડે યોગશીલ પ્રક્રિયા",
            "સૂર્યપ્રકાશમાં ક્લોરિન વડે વિસ્થાપન પ્રક્રિયા",
            "દહન પ્રક્રિયા"
        ],
        "correct_index": 0,
        "explanation": "Converting Ethanol (C2H5OH) to Ethanoic Acid (CH3COOH) involves addition of an oxygen atom and removal of two hydrogen atoms, which is an oxidation reaction catalyzed by alkaline KMnO4 or acidified K2Cr2O7.",
        "explanation_hi": "एथेनॉल (C2H5OH) को एथेनॉइक अम्ल (CH3COOH) में बदलने में ऑक्सीजन का जुड़ना और हाइड्रोजन का हटना शामिल है, जो क्षारीय KMnO4 या अम्लीकृत K2Cr2O7 द्वारा उत्प्रेरित एक ऑक्सीकरण अभिक्रिया है।",
        "explanation_gu": "ઇથેનોલમાંથી ઇથેનોઇક એસિડ બનતી વખતે ઓક્સિજન ઉમેરાય છે અને હાઇડ્રોજન દૂર થાય છે, જે આલ્કલાઇન KMnO4 વડે થતી ઓક્સિડેશન પ્રક્રિયા છે."
    })

    # =========================================================================
    # MODULE 6: ETHANOL & ETHANOIC ACID (8-STEP PEDAGOGY)
    # =========================================================================

    # 1. Hook
    blocks.append({
        "id": next_id(),
        "type": "hook",
        "title": "Two Liquids with Astonishingly Different Personalities",
        "title_hi": "आश्चर्यजनक रूप से भिन्न व्यक्तित्व वाले दो तरल पदार्थ",
        "title_gu": "આશ્ચર્યજનક રીતે અલગ સ્વભાવ ધરાવતા બે પ્રવાહીઓ",
        "body": "In your chemistry laboratory sit two colourless, clear liquids with almost identical numbers of atoms: Ethanol (C2H6O) and Ethanoic acid (C2H4O2). One is an intoxicating solvent used in hand sanitizers and medicines, while the other is the sour, pungent liquid found in kitchen vinegar that turns into solid ice-like crystals on cold winter mornings! How does adding a single oxygen atom create such vastly different worlds?",
        "body_hi": "आपकी रसायन विज्ञान प्रयोगशाला में लगभग समान संख्या में परमाणुओं वाले दो रंगहीन तरल पदार्थ हैं: एथेनॉल (C2H6O) और एथेनॉइक अम्ल (C2H4O2)। एक सैनिटाइज़र और दवाओं में इस्तेमाल होने वाला विलायक है, जबकि दूसरा रसोई के सिरके में पाया जाने वाला खट्टा तरल है जो सर्दियों की सुबह बर्फ जैसे क्रिस्टल में जम जाता है! केवल एक ऑक्सीजन परमाणु जोड़ने से इतनी अलग दुनिया कैसे बन जाती है?",
        "body_gu": "તમારી પ્રયોગશાળામાં બે રંગહીન પ્રવાહી છે: ઇથેનોલ (C2H6O) અને ઇથેનોઇક એસિડ (C2H4O2). એક સેનિટાઇઝર અને દવાઓમાં વપરાતો દ્રાવક છે, જ્યારે બીજો રસોડાના સરકામાં રહેલો ખાટો પ્રવાહી છે જે શિયાળામાં બરફની જેમ જામી જાય છે! માત્ર એક ઓક્સિજનના ઉમેરાથી આટલો મોટો તફાવત કેવી રીતે આવે છે?"
    })

    # 2. Socratic Question
    blocks.append({
        "id": next_id(),
        "type": "socratic_question",
        "question": "How can you distinguish experimentally between Ethanol and Ethanoic acid using a single common laboratory chemical?",
        "question_hi": "प्रयोगशाला के एक सामान्य रसायन का उपयोग करके आप एथेनॉल और एथेनॉइक अम्ल में प्रयोगात्मक रूप से कैसे अंतर कर सकते हैं?",
        "question_gu": "પ્રયોગશાળાના સામાન્ય રસાયણનો ઉપયોગ કરીને તમે ઇથેનોલ અને ઇથેનોઇક એસિડ વચ્ચે પ્રાયોગિક રીતે કેવી રીતે ભેદ પારખી શકો?",
        "options": [
            "Add Sodium Hydrogen Carbonate (NaHCO3): Ethanoic acid produces brisk effervescence of CO2 gas, while Ethanol gives no reaction.",
            "Add water: Ethanol is insoluble while Ethanoic acid dissolves.",
            "Boil them: Ethanol freezes while Ethanoic acid evaporates.",
            "Touch them: Ethanol burns the skin while Ethanoic acid acts as moisturizer."
        ],
        "options_hi": [
            "सोडियम हाइड्रोजन कार्बोनेट (NaHCO3) मिलाएं: एथेनॉइक अम्ल CO2 गैस की तीव्र बुदबुदाहट पैदा करता है, जबकि एथेनॉल कोई प्रतिक्रिया नहीं देता।",
            "पानी मिलाएं: एथेनॉल अघुलनशील है जबकि एथेनॉइक अम्ल घुल जाता है।",
            "उन्हें उबालें: एथेनॉल जम जाता है जबकि एथेनॉइक अम्ल वाष्पित हो जाता है।",
            "उन्हें छुएं: एथेनॉल त्वचा को जलाता है।"
        ],
        "options_gu": [
            "સોડિયમ હાઇડ્રોજન કાર્બોનેટ (NaHCO3) ઉમેરો: ઇથેનોઇક એસિડ ઉભરા સાથે CO2 વાયુ મુક્ત કરે છે, જ્યારે ઇથેનોલ કોઈ પ્રક્રિયા આપતો નથી.",
            "પાણી ઉમેરો: ઇથેનોલ અદ્રાવ્ય છે.",
            "ગરમ કરો: ઇથેનોલ જામી જાય છે.",
            "સ્પર્શ કરો: ઇથેનોલ ત્વચા બાળે છે."
        ],
        "correct_index": 0,
        "explanation": "Carboxylic acids react with carbonates and hydrogencarbonates to liberate carbon dioxide gas with brisk effervescence (CH3COOH + NaHCO3 -> CH3COONa + H2O + CO2↑). Alcohols do not react with bicarbonates.",
        "explanation_hi": "कार्बोक्सिलिक अम्ल कार्बोनेट और बाइकार्बोनेट के साथ प्रतिक्रिया करके तीव्र बुदबुदाहट के साथ CO2 गैस छोड़ते हैं। ऐल्कोहॉल बाइकार्बोनेट के साथ प्रतिक्रिया नहीं करते हैं।",
        "explanation_gu": "કાર્બોક્સિલિક એસિડ બાયકાર્બોનેટ સાથે પ્રક્રિયા કરીને ઉભરા સાથે CO2 વાયુ મુક્ત કરે છે (CH3COOH + NaHCO3 -> CH3COONa + H2O + CO2↑). આલ્કોહોલ આ પ્રક્રિયા આપતા નથી."
    })

    # 3. Discovery
    blocks.append({
        "id": next_id(),
        "type": "discovery",
        "title": "Properties and Reactions of Ethanol (C2H5OH)",
        "title_hi": "एथेनॉल (C2H5OH) के गुण और अभिक्रियाएं",
        "title_gu": "ઇથેનોલ (C2H5OH) ના ગુણધર્મો અને પ્રક્રિયાઓ",
        "body": "ETHANOL (Ethyl Alcohol, C2H5OH):\n• Physical State: Colourless liquid with a pleasant smell and burning taste; boiling point 78°C (351 K); soluble in water in all proportions.\n• Reaction with Sodium: Releases Hydrogen gas with effervescence:\n  2Na + 2CH3CH2OH -> 2CH3CH2ONa (Sodium Ethoxide) + H2↑\n• Dehydration to Ethene: Heating ethanol with excess CONCENTRATED H2SO4 at 443 K (170°C) removes water molecule:\n  CH3-CH2OH --[Hot Conc. H2SO4 at 443 K]--> CH2=CH2 (Ethene) + H2O\n  (Here, concentrated H2SO4 acts as a DEHYDRATING AGENT).\n\nBiological Impact & Denatured Alcohol:\n• Ingesting ethanol depresses the central nervous system, impairs judgment, and causes liver cirrhosis over time.\n• Methanol (CH3OH) is highly poisonous: Even 30 mL can cause blindness (destroys optic nerve) and death (oxidizes to methanal, coagulating cellular protoplasm).\n• Denatured Alcohol: Industrial ethanol is made unfit for drinking by adding poisonous methanol and blue copper sulphate dye.",
        "body_hi": "एथेनॉल (एथिल ऐल्कोहॉल, C2H5OH):\n• भौतिक गुण: सुखद गंध वाला रंगहीन तरल; क्वथनांक 78°C (351 K); जल में सभी अनुपातों में घुलनशील।\n• सोडियम के साथ अभिक्रिया: हाइड्रोजन गैस मुक्त करता है:\n  2Na + 2C2H5OH -> 2C2H5ONa (सोडियम एथॉक्साइड) + H2↑\n• निर्जलीकरण द्वारा एथीन का निर्माण: 443 K पर सांद्र सल्फ्यूरिक अम्ल (H2SO4) के साथ गर्म करने पर जल का अणु निकल जाता है:\n  C2H5OH --[सांद्र H2SO4, 443 K]--> CH2=CH2 + H2O (सांद्र H2SO4 निर्जलीकारक है)।\n\nजैविक प्रभाव और विकृत ऐल्कोहॉल:\n• एथेनॉल का सेवन केंद्रीय तंत्रिका तंत्र को प्रभावित करता है और यकृत को नुकसान पहुंचाता है।\n• मेथेनॉल (CH3OH) अत्यंत विषैला होता है: यह अंधापन और मृत्यु का कारण बन सकता है।\n• विकृत ऐल्कोहॉल (Denatured Alcohol): औद्योगिक ऐल्कोहॉल के दुरुपयोग को रोकने के लिए इसमें विषैला मेथेनॉल और नीला रंग मिला दिया जाता है।",
        "body_gu": "ઇથેનોલ (ઇથાઇલ આલ્કોહોલ, C2H5OH):\n• ભૌતિક ગુણધર્મો: મીઠી વાસવાળું રંગહીન પ્રવાહી; ઉત્કલનબિંદુ 78°C (351 K); પાણીમાં ગમે તે પ્રમાણમાં દ્રાવ્ય.\n• સોડિયમ સાથે પ્રક્રિયા: હાઇડ્રોજન વાયુ મુક્ત કરે છે:\n  2Na + 2C2H5OH -> 2C2H5ONa (સોડિયમ ઇથોક્સાઇડ) + H2↑\n• નિર્જળીકરણ: સાંદ્ર H2SO4 સાથે 443 K તાપમાને ગરમ કરતાં તેમાંથી પાણી દૂર થઈ ઇથીન બને છે:\n  C2H5OH --[સાંદ્ર H2SO4, 443 K]--> CH2=CH2 + H2O (સાંદ્ર H2SO4 નિર્જળીકરણકર્તા છે).\n\nજૈવિક અસરો અને ડીનેચર્ડ આલ્કોહોલ:\n• ઇથેનોલ ચેતાતંત્રને નુકસાન પહોંચાડે છે અને લિવર બગાડે છે.\n• મિથેનોલ (CH3OH) અત્યંત ઝેરી છે: તેનાથી અંધાપો કે મૃત્યુ થઈ શકે છે.\n• ડીનેચર્ડ આલ્કોહોલ: ઔદ્યોગિક આલ્કોહોલ પીવાલાયક ન રહે તે માટે તેમાં ઝેરી મિથેનોલ અને વાદળી રંગ ઉમેરવામાં આવે છે."
    })

    # 4. Theory
    blocks.append({
        "id": next_id(),
        "type": "theory",
        "title": "Properties and Reactions of Ethanoic Acid (CH3COOH)",
        "title_hi": "एथेनॉइक अम्ल (CH3COOH) के गुण और अभिक्रियाएं",
        "title_gu": "ઇથેનોઇક એસિડ (CH3COOH) ના ગુણધર્મો અને પ્રક્રિયાઓ",
        "body": "ETHANOIC ACID (Acetic Acid, CH3COOH):\n• Vinegar: 5% to 8% solution of ethanoic acid in water is called VINEGAR, widely used as a food preservative in pickles.\n• Glacial Acetic Acid: Pure ethanoic acid has a melting point of 290 K (17°C). In cold climates, it freezes into ice-like crystals, hence called GLACIAL acetic acid.\n• Acidity: Ethanoic acid is a weak acid; it does not completely ionize in water (unlike strong mineral acids like HCl).\n\nKey Chemical Reactions:\n1. ESTERIFICATION:\nReaction with alcohols in the presence of an acid catalyst yields sweet-smelling fruit-like compounds called ESTERS:\nCH3COOH + C2H5OH --[Conc. H2SO4]--> CH3COOC2H5 (Ethyl ethanoate) + H2O\n(Esters are used in perfumes and artificial fruit flavourings).\n\n2. SAPONIFICATION (Soap Making):\nWhen an ester is heated with sodium hydroxide (NaOH, a strong base), it hydrolyzes back to alcohol and sodium salt of carboxylic acid:\nCH3COOC2H5 + NaOH -> CH3COONa (Sodium ethanoate) + C2H5OH\n(Because this reaction is used in the preparation of soap, it is called Saponification).\n\n3. REACTION WITH BASES:\nCH3COOH + NaOH -> CH3COONa + H2O\n\n4. REACTION WITH CARBONATES & HYDROGENCARBONATES:\n• 2CH3COOH + Na2CO3 -> 2CH3COONa + H2O + CO2↑\n• CH3COOH + NaHCO3 -> CH3COONa + H2O + CO2↑ (Brisk effervescence).",
        "body_hi": "एथेनॉइक अम्ल (एसिटिक एसिड, CH3COOH):\n• सिरका (Vinegar): जल में एथेनॉइक अम्ल का 5% से 8% विलयन सिरका कहलाता है, जो अचार के परिरक्षक के रूप में काम आता है।\n• ग्लैशियल एसिटिक एसिड: शुद्ध एथेनॉइक अम्ल का गलनांक 290 K (17°C) होता है। सर्दियों में यह बर्फ की तरह जम जाता है, इसलिए इसे ग्लैशियल एसिटिक अम्ल कहते हैं।\n\nप्रमुख रासायनिक अभिक्रियाएं:\n1. एस्टरीकरण (Esterification):\nअम्ल उत्प्रेरक की उपस्थिति में ऐल्कोहॉल के साथ क्रिया करके मीठी गंध वाले एस्टर बनाते हैं:\nCH3COOH + C2H5OH --[सांद्र H2SO4]--> CH3COOC2H5 + H2O\n(एस्टर का उपयोग इत्र और स्वादों में होता है)।\n\n2. साबुनीकरण (Saponification):\nएस्टर को सोडियम हाइड्रॉक्साइड (NaOH) के साथ गर्म करने पर ऐल्कोहॉल और सोडियम लवण प्राप्त होता है:\nCH3COOC2H5 + NaOH -> CH3COONa + C2H5OH\n(इस अभिक्रिया का उपयोग साबुन बनाने में होता है)।\n\n3. कार्बोनेट और हाइड्रोजनकार्बोनेट से अभिक्रिया:\nCH3COOH + NaHCO3 -> CH3COONa + H2O + CO2↑ (तीव्र बुदबुदाहट)।",
        "body_gu": "ઇથેનોઇક એસિડ (એસિટિક એસિડ, CH3COOH):\n• સરકો (Vinegar): પાણીમાં ઇથેનોઇક એસિડના 5% થી 8% દ્રાવણને સરકો કહે છે, જે અથાણાંની જાળવણીમાં વપરાય છે.\n• ગ્લેશિયલ એસિટિક એસિડ: શુદ્ધ એસિટિક એસિડનું ગલનબિંદુ 290 K (17°C) હોવાથી શિયાળામાં તે બરફની જેમ જામી જાય છે, તેથી તેને ગ્લેશિયલ એસિટિક એસિડ કહેવાય છે.\n\nમુખ્ય રાસાયણિક પ્રક્રિયાઓ:\n1. એસ્ટરીકરણ (Esterification):\nએસિડ ઉદ્દીપકની હાજરીમાં આલ્કોહોલ સાથે પ્રક્રિયા કરી મીઠી સુગંધવાળા એસ્ટર બનાવે છે:\nCH3COOH + C2H5OH --[સાંદ્ર H2SO4]--> CH3COOC2H5 + H2O\n(અત્તર અને ફ્લેવરમાં વપરાય છે).\n\n2. સાબુની બનાવટ (Saponification):\nએસ્ટરની NaOH સાથે પ્રક્રિયા કરવાથી આલ્કોહોલ અને કાર્બોક્સિલિક એસિડનો સોડિયમ ક્ષાર બને છે:\nCH3COOC2H5 + NaOH -> CH3COONa + C2H5OH\n(આ પ્રક્રિયા સાબુ બનાવવા વપરાય છે).\n\n3. કાર્બોનેટ અને બાયકાર્બોનેટ સાથે પ્રક્રિયા:\nCH3COOH + NaHCO3 -> CH3COONa + H2O + CO2↑ (ઉભરા સાથે)."
    })

    # Teacher Tip
    blocks.append({
        "id": next_id(),
        "type": "teacher_tip",
        "title": "Teacher Tip: The Role of Concentrated H2SO4 in Esterification",
        "title_hi": "शिक्षक टिप: एस्टरीकरण में सांद्र H2SO4 की दोहरी भूमिका",
        "title_gu": "શિક્ષક ટિપ: એસ્ટરીકરણમાં સાંદ્ર H2SO4 ની બેવડી ભૂમિકા",
        "body": "In esterification, concentrated sulphuric acid acts as BOTH an acid catalyst (speeds up the reaction) AND a dehydrating agent (absorbs water formed, shifting the equilibrium to the right by Le Chatelier's principle to maximize ester yield). Board exams love testing this dual role!",
        "body_hi": "एस्टरीकरण में, सांद्र सल्फ्यूरिक अम्ल अम्ल उत्प्रेरक (अभिक्रिया को तेज करता है) और निर्जलीकारक (बने हुए पानी को सोख लेता है ताकि अधिक एस्टर बन सके) दोनों के रूप में कार्य करता है।",
        "body_gu": "એસ્ટરીકરણમાં સાંદ્ર સલ્ફ્યુરિક એસિડ ઉદ્દીપક (પ્રક્રિયા ઝડપી બનાવે છે) અને નિર્જળીકરણકર્તા (ઉત્પન્ન થયેલું પાણી શોષી લે છે જેથી વધુ એસ્ટર બને) બંને તરીકે કાર્ય કરે છે."
    })

    # Common Mistake
    blocks.append({
        "id": next_id(),
        "type": "teacher_tip",
        "title": "Common Mistake: Thinking Carboxylic Acids are Strong Mineral Acids",
        "title_hi": "सामान्य गलती: यह सोचना कि कार्बोक्सिलिक अम्ल प्रबल खनिज अम्ल हैं",
        "title_gu": "સામાન્ય ભૂલ: કાર્બોક્સિલિક એસિડને પ્રબળ એસિડ માનવા",
        "body": "Ethanoic acid is an organic acid, NOT a strong mineral acid! Hydrochloric acid (HCl) completely dissociates in water (pH ~ 1). Ethanoic acid only partially dissociates into CH3COO- and H+ (pH ~ 3 to 4). It turns blue litmus red, but will not react violently like concentrated mineral acids.",
        "body_hi": "एथेनॉइक अम्ल एक दुर्बल कार्बनिक अम्ल है, प्रबल खनिज अम्ल नहीं! हाइड्रोक्लोरिक अम्ल (HCl) पानी में पूरी तरह से आयनित होता है, जबकि एथेनॉइक अम्ल केवल आंशिक रूप से आयनित होता है। यह नीले लिटमस को लाल करता है लेकिन शांत अम्ल है।",
        "body_gu": "ઇથેનોઇક એસિડ એ નિર્બળ કાર્બનિક એસિડ છે, પ્રબળ એસિડ નથી! હાઇડ્રોક્લોરિક એસિડ પાણીમાં સંપૂર્ણ આયનીકરણ પામે છે, જ્યારે એસિટિક એસિડ આંશિક આયનીકરણ પામે છે."
    })

    # 5. Knowledge Check
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "What is the product formed when Ethanol is heated with excess concentrated Sulphuric acid at 443 K?",
        "question_hi": "443 K पर एथेनॉल को सांद्र सल्फ्यूरिक अम्ल की अधिकता के साथ गर्म करने पर क्या उत्पाद बनता है?",
        "question_gu": "443 K તાપમાને ઇથેનોલને સાંદ્ર સલ્ફ્યુરિક એસિડ સાથે ગરમ કરતાં કઈ નીપજ બને છે?",
        "options": [
            "Ethene (CH2=CH2)",
            "Ethane (C2H6)",
            "Ethanoic acid (CH3COOH)",
            "Diethyl ether"
        ],
        "options_hi": [
            "एथीन (CH2=CH2)",
            "एथेन (C2H6)",
            "एथेनॉइक अम्ल (CH3COOH)",
            "डाइएथिल ईथर"
        ],
        "options_gu": [
            "ઇથીન (CH2=CH2)",
            "ઇથેન (C2H6)",
            "ઇથેનોઇક એસિડ (CH3COOH)",
            "ડાયઇથાઇલ ઇથર"
        ],
        "correct_index": 0,
        "explanation": "Heating ethanol at 443 K with concentrated H2SO4 causes dehydration (loss of a water molecule), producing unsaturated Ethene gas (CH3CH2OH -> CH2=CH2 + H2O).",
        "explanation_hi": "सांद्र H2SO4 के साथ 443 K पर एथेनॉल को गर्म करने पर निर्जलीकरण (जल के अणु की हानि) होता है, जिससे असंतृप्त एथीन गैस (CH2=CH2) बनती है।",
        "explanation_gu": "સાંદ્ર H2SO4 ની હાજરીમાં 443 K તાપમાને ઇથેનોલમાંથી પાણીનો અણુ દૂર થઈ અસંતૃપ્ત ઇથીન વાયુ બને છે."
    })

    # 6. Reflection
    blocks.append({
        "id": next_id(),
        "type": "reflection",
        "title": "Biofuels: Running Engines on Sugar Cane",
        "title_hi": "जैव ईंधन: गन्ने से इंजन चलाना",
        "title_gu": "જૈવિક બળતણ: શેરડીમાંથી એન્જિન ચલાવવું",
        "body": "Sugar cane juice is fermented by yeast into molasses to manufacture Ethanol. Brazil and India blend 10% to 20% ethanol into petrol ('Gasohol'). Ethanol burns cleanly into CO2 and H2O without soot or toxic sulphur emissions, reducing dependence on imported crude oil and lowering air pollution.",
        "body_hi": "गन्ने के रस को खमीर (Yeast) द्वारा किण्वित करके एथेनॉल बनाया जाता है। भारत और ब्राजील पेट्रोल में 10% से 20% एथेनॉल मिलाते हैं। एथेनॉल बिना कालिख या सल्फर के साफ जलता है, जिससे प्रदूषण कम होता है।",
        "body_gu": "શેરડીના રસનું આથવણ કરીને ઇથેનોલ બનાવવામાં આવે છે. ભારતમાં પેટ્રોલમાં 10% થી 20% ઇથેનોલ ભેળવવામાં આવે છે. ઇથેનોલ સ્વચ્છ રીતે સળગે છે અને પ્રદૂષણ ઘટાડે છે."
    })

    # 7. Connection
    blocks.append({
        "id": next_id(),
        "type": "connection",
        "title": "Esters in Fragrances, Food Flavours and Cosmetics",
        "title_hi": "इत्र, खाद्य स्वादों और सौंदर्य प्रसाधनों में एस्टर",
        "title_gu": "અત્તર, ફૂડ ફ્લેવર અને કોસ્મેટિક્સમાં એસ્ટર",
        "body": "The delightful scent of ripe bananas (isoamyl acetate), pineapples (ethyl butyrate), and oranges (octyl acetate) are all natural esters! Chemical manufacturers synthesize identical esters via esterification of alcohols and carboxylic acids for soft drinks, perfumes, candles, and candy.",
        "body_hi": "केले, अनानास और संतरों की मनमोहक सुगंध प्राकृतिक एस्टर हैं! शीतल पेय, इत्र, मोमबत्तियों और कैंडी के लिए रासायनिक कारखानों में ऐल्कोहॉल और कार्बोक्सिलिक एसिड के एस्टरीकरण द्वारा ये स्वाद बनाए जाते हैं।",
        "body_gu": "પાકા કેળા, પાઇનેપલ અને સંતરાની કુદરતી સુગંધ એસ્ટર સંયોજનોને આભારી છે! આ સુગંધ પ્રયોગશાળામાં એસ્ટરીકરણ પ્રક્રિયા વડે બનાવીને અત્તર અને આઇસક્રીમમાં વપરાય છે."
    })

    # 8. Mastery Challenge
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "An organic compound 'X' is a sweet-smelling liquid. On heating 'X' with Sodium Hydroxide solution, it gives back Ethanol and a sodium salt 'Y'. Identify 'X' and the type of reaction.",
        "question_hi": "एक कार्बनिक यौगिक 'X' एक मीठी गंध वाला तरल है। 'X' को सोडियम हाइड्रॉक्साइड विलयन के साथ गर्म करने पर, यह वापस एथेनॉल और एक सोडियम लवण 'Y' देता है। 'X' और अभिक्रिया के प्रकार की पहचान करें।",
        "question_gu": "એક કાર્બનિક સંયોજન 'X' મીઠી વાસવાળું પ્રવાહી છે. 'X' ને સોડિયમ હાઇડ્રોક્સાઇડ સાથે ગરમ કરતાં તે ઇથેનોલ અને સોડિયમ ક્ષાર 'Y' પાછો આપે છે. 'X' અને પ્રક્રિયાનો પ્રકાર ઓળખો.",
        "options": [
            "X = Ethyl ethanoate (Ester); Saponification reaction",
            "X = Ethanoic acid; Neutralization reaction",
            "X = Methane; Substitution reaction",
            "X = Ethene; Addition reaction"
        ],
        "options_hi": [
            "X = एथिल एथेनोएट (एस्टर); साबुनीकरण अभिक्रिया",
            "X = एथेनॉइक अम्ल; उदासीनीकरण अभिक्रिया",
            "X = मीथेन; प्रतिस्थापन अभिक्रिया",
            "X = एथीन; संकलन अभिक्रिया"
        ],
        "options_gu": [
            "X = ઇથાઇલ ઇથેનોએટ (એસ્ટર); સાબુની બનાવટ (Saponification)",
            "X = ઇથેનોઇક એસિડ; તટસ્થીકરણ",
            "X = મિથેન; વિસ્થાપન",
            "X = ઇથીન; યોગશીલ"
        ],
        "correct_index": 0,
        "explanation": "Sweet-smelling liquid 'X' is the ester Ethyl Ethanoate (CH3COOC2H5). Heating an ester with an alkali like NaOH hydrolyzes it back into sodium ethanoate ('Y') and ethanol. This alkaline hydrolysis is called Saponification.",
        "explanation_hi": "मीठी गंध वाला तरल 'X' एस्टर एथिल एथेनोएट (CH3COOC2H5) है। NaOH के साथ गर्म करने पर यह सोडियम एथेनोएट ('Y') और एथेनॉल देता है। इस क्षारीय जलअपघटन को साबुनीकरण कहते हैं।",
        "explanation_gu": "મીઠી વાસવાળું પ્રવાહી 'X' એ એસ્ટર ઇથાઇલ ઇથેનોએટ છે. NaOH સાથે પ્રક્રિયા કરતાં તે ઇથેનોલ અને સોડિયમ ક્ષાર આપે છે, જેને સાબુની બનાવટ (Saponification) પ્રક્રિયા કહે છે."
    })

    # =========================================================================
    # MODULE 7: SOAPS, DETERGENTS & MICELLES (8-STEP PEDAGOGY)
    # =========================================================================

    # 1. Hook
    blocks.append({
        "id": next_id(),
        "type": "hook",
        "title": "The War Against Greasy Dirt",
        "title_hi": "तैलीय मैल के खिलाफ युद्ध",
        "title_gu": "ચીકણા મેલ સામે યુદ્ધ",
        "body": "Try this experiment: Dip your hands in cooking oil and try washing them with pure water alone. The water forms beads and rolls right off, leaving your hands as greasy as before! But the moment you rub a tiny drop of soap, the oil washes away effortlessly into milky rinse water. How can a simple bar of soap dissolve something that water completely rejects?",
        "body_hi": "यह प्रयोग करके देखें: अपने हाथों को तेल में डुबोएं और केवल सादे पानी से धोने का प्रयास करें। पानी की बूंदें फिसल जाएंगी और हाथ तैलीय ही रहेंगे! लेकिन जैसे ही आप साबुन की एक छोटी बूंद लगाते हैं, तेल आसानी से बह जाता है। साबुन उस चीज़ को कैसे घोल देता है जिसे पानी पूरी तरह से अस्वीकार करता है?",
        "body_gu": "એક પ્રયોગ કરો: હાથ તેલવાળા કરીને માત્ર પાણીથી ધોવાનો પ્રયત્ન કરો. પાણીનાં ટીપાં સરકી જશે અને હાથ તેલવાળા જ રહેશે! પરંતુ જેવો સાબુ લગાવશો કે તરત જ તેલ પાણી સાથે ધોવાઈ જશે. સાબુ એવું તે શું કરે છે જે પાણી નથી કરી શકતું?"
    })

    # 2. Socratic Question
    blocks.append({
        "id": next_id(),
        "type": "socratic_question",
        "question": "How does a single soap molecule bridge the chemical gap between water and oil?",
        "question_hi": "साबुन का एक अकेला अणु पानी और तेल के बीच रासायनिक अंतर को कैसे पाटता है?",
        "question_gu": "સાબુનો એક જ અણુ પાણી અને તેલ વચ્ચે રાસાયણિક પુલનું કામ કેવી રીતે કરે છે?",
        "options": [
            "It has two ends: a hydrophilic ionic head that loves water, and a hydrophobic hydrocarbon tail that dissolves in oil.",
            "It converts oil into water by a nuclear reaction.",
            "It boils the water to melt the grease.",
            "It turns the water acidic so oil evaporates."
        ],
        "options_hi": [
            "इसके दो सिरे होते हैं: एक जलरागी आयनिक सिर जो पानी से प्यार करता है, और एक जलविरागी हाइड्रोकार्बन पूंछ जो तेल में घुलती है।",
            "यह परमाणु अभिक्रिया द्वारा तेल को पानी में बदल देता है।",
            "यह ग्रीस को पिघलाने के लिए पानी को उबालता है।",
            "यह पानी को अम्लीय बना देता है जिससे तेल वाष्पित हो जाता है।"
        ],
        "options_gu": [
            "તે બે છેડા ધરાવે છે: જલઅનુરાગી આયનિક છેડો જે પાણીમાં ઓગળે છે, અને જલપ્રતિકારક હાઇડ્રોકાર્બન પૂંછડી જે તેલમાં ઓગળે છે.",
            "તે તેલનું પાણીમાં રૂપાંતર કરે છે.",
            "તે પાણીને ઉકાળે છે.",
            "તે પાણીને એસિડિક બનાવે છે."
        ],
        "correct_index": 0,
        "explanation": "Soap molecules are sodium or potassium salts of long-chain fatty acids (R-COO- Na+). The polar carboxylate head (-COO- Na+) is hydrophilic (water-loving). The long non-polar hydrocarbon tail is hydrophobic (water-fearing) but lipophilic (oil-dissolving).",
        "explanation_hi": "साबुन के अणु लंबी श्रृंखला वाले फैटी एसिड के लवण होते हैं। ध्रुवीय आयनिक सिरा जलरागी (पानी को आकर्षित करने वाला) होता है और गैर-ध्रुवीय हाइड्रोकार्बन पूंछ जलविरागी (तेल में घुलने वाली) होती है।",
        "explanation_gu": "સાબુના અણુઓ લાંબી શૃંખલાવાળા ફેટી એસિડના ક્ષાર છે. ધ્રુવીય આયનિક છેડો જલઅનુરાગી હોય છે અને બિન-ધ્રુવીય હાઇડ્રોકાર્બન પૂંછડી જલપ્રતિકારક પરંતુ તેલમાં દ્રાવ્ય હોય છે."
    })

    # 3. Discovery
    blocks.append({
        "id": next_id(),
        "type": "discovery",
        "title": "Micelle Formation & Mechanism of Cleansing Action",
        "title_hi": "मिसेल निर्माण और सफाई क्रिया की क्रियाविधि",
        "title_gu": "મિસેલ રચના અને સફાઈ પ્રક્રિયાની કાર્યપદ્ધતિ",
        "body": "HOW SOAPS CLEAN CLOTHES (MICELLE MECHANISM):\n1. Micelle Formation:\nWhen soap is dissolved in water, the molecules arrange themselves radially into spherical clusters called MICELLES.\n• The hydrophobic hydrocarbon tails point inwards towards the center of the sphere (away from water).\n• The hydrophilic ionic heads point outwards on the surface of the sphere, interacting with surrounding water molecules.\n\n2. Trapping Oily Dirt:\nGreasy and oily dirt particles on fabric are non-polar. When agitating clothes, the hydrophobic tails dissolve into the oil droplet. The oil droplet is trapped at the center of the micelle.\n\n3. Emulsion Formation & Washing Away:\nBecause the micelle surface is studded with negatively charged ionic heads (-COO-), micelles repel each other due to ion-ion repulsion and do not precipitate. They remain suspended in water as a stable colloidal emulsion. When rinsed with fresh water, the entire micelle carrying the entrapped dirt is washed away.",
        "body_hi": "साबुन कपड़े कैसे साफ करते हैं (मिसेल क्रियाविधि):\n1. मिसेल निर्माण:\nजब साबुन को पानी में घोला जाता है, तो अणु गोलाकार गुच्छों में व्यवस्थित होते हैं जिन्हें मिसेल (Micelles) कहते हैं।\n• जलविरागी हाइड्रोकार्बन पूंछ केंद्र की ओर अंदर की ओर होती है (पानी से दूर)।\n• जलरागी आयनिक सिर बाहर की सतह पर पानी की ओर होते हैं।\n\n2. तैलीय मैल को फंसाना:\nकपड़े पर लगा तैलीय मैल मिसेल के केंद्र में हाइड्रोकार्बन पूंछ द्वारा फंस जाता है।\n\n3. इमल्शन बनना और धुल जाना:\nमिसेल की सतह पर समान ऋणात्मक आवेश होने के कारण वे एक-दूसरे को प्रतिकर्षित करते हैं और अवक्षेपित नहीं होते। वे पानी में पायस (Emulsion) के रूप में तैरते रहते हैं। पानी से खंगालने पर मिसेल में फंसा मैल बह जाता है।",
        "body_gu": "સાબુની સફાઈ પ્રક્રિયા (મિસેલ કાર્યપદ્ધતિ):\n1. મિસેલ રચના:\nસાબુને પાણીમાં ઓગાળતાં અણુઓ ગોળાકાર ઝૂમખાં બનાવે છે જેને મિસેલ કહે છે.\n• જલપ્રતિકારક હાઇડ્રોકાર્બન પૂંછડી કેન્દ્ર તરફ અંદર રહે છે (પાણીથી દૂર).\n• જલઅનુરાગી આયનિક છેડો બહારની સપાટી તરફ પાણી સાથે સંપર્કમાં રહે છે.\n\n2. તેલી મેલને જકડવો:\nકાપડ પરનો તેલી મેલ મિસેલના કેન્દ્રમાં ફસાઈ જાય છે.\n\n3. પાયસ (ઇમલ્શન) અને ધોવાઈ જવું:\nમિસેલની સપાટી પર સમાન વીજભાર હોવાથી મિસેલો એકબીજાને અપાકર્ષે છે અને અવક્ષેપિત થતા નથી. પાણીથી ધોતાં મેલ મિસેલ સાથે વહી જાય છે."
    })

    # 4. Theory
    blocks.append({
        "id": next_id(),
        "type": "theory",
        "title": "Hard Water, Scum & Synthetic Detergents",
        "title_hi": "कठोर जल, स्कम और संश्लेषित डिटर्जेंट",
        "title_gu": "કઠિન પાણી, સ્કમ અને સંશ્લેષિત ડિટર્જન્ટ",
        "body": "SOAP LIMITATION: HARD WATER PROBLEM\n• Hard water contains dissolved calcium and magnesium hydrogencarbonates, chlorides, or sulphates (Ca2+ and Mg2+ ions).\n• When soap is added to hard water, Ca2+ and Mg2+ displace sodium/potassium, forming insoluble curdy white precipitates called SCUM:\n  2C17H35COONa (Soap) + Ca2+ -> (C17H35COO)2Ca↓ (Insoluble Calcium Stearate / Scum) + 2Na+\n• Scum sticks to clothes, causes greying of fabrics, and wastes immense amounts of soap before any lather is formed.\n\nSYNTHETIC DETERGENTS (Soapless Soaps):\n• Detergents are generally ammonium or sulphonate salts of long-chain carboxylic acids (e.g., Sodium alkylbenzene sulphonates).\n• The charged ends of detergents DO NOT form insoluble precipitates with Ca2+ and Mg2+ ions in hard water.\n• Therefore, detergents remain completely effective and foam profusely even in hard water.\n• Uses: Shampoos, dishwashing liquids, washing powders.",
        "body_hi": "साबुन की सीमा: कठोर जल की समस्या\n• कठोर जल में कैल्शियम और मैग्नीशियम के घुलनशील लवण (Ca2+ और Mg2+ आयन) होते हैं।\n• जब साबुन को कठोर जल में मिलाया जाता है, तो Ca2+ और Mg2+ साबुन के साथ प्रतिक्रिया करके 'स्कम' (Scum) नामक एक अघुलनशील चिपचिपा सफेद अवक्षेप बनाते हैं।\n• स्कम कपड़ों पर चिपक जाता है और झाग बनने से पहले बहुत सारा साबुन बर्बाद हो जाता है।\n\nसंश्लेषित डिटर्जेंट (Synthetic Detergents):\n• डिटर्जेंट लंबी श्रृंखला वाले कार्बोक्सिलिक अम्लों के अमोनियम या सल्फोनेट लवण होते हैं।\n• डिटर्जेंट के आवेशित सिरे कठोर जल में मौजूद Ca2+ और Mg2+ आयनों के साथ अघुलनशील अवक्षेप (स्कम) नहीं बनाते हैं।\n• इसलिए डिटर्जेंट कठोर जल में भी आसानी से झाग बनाते हैं और पूरी तरह से प्रभावी रहते हैं।\n• उपयोग: शैम्पू, कपड़े धोने के पाउडर।",
        "body_gu": "સાબુની મર્યાદા: કઠિન પાણીની સમસ્યા\n• કઠિન પાણીમાં કેલ્શિયમ અને મેગ્નેશિયમના ક્ષારો (Ca2+ અને Mg2+ આયનો) ઓગળેલા હોય છે.\n• સાબુ ઉમેરતાં તે Ca2+ અને Mg2+ સાથે પ્રક્રિયા કરી અદ્રાવ્ય સફેદ ચીકણો અવક્ષેપ 'સ્કમ' (Scum) બનાવે છે.\n• સ્કમ કાપડ પર ચોંટી જાય છે અને ફીણ વળતાં પહેલાં પુષ્કળ સાબુ વેડફાઈ જાય છે.\n\nસંશ્લેષિત ડિટર્જન્ટ (Synthetic Detergents):\n• ડિટર્જન્ટ એ લાંબી શૃંખલાવાળા હાઇડ્રોકાર્બનના સલ્ફોનેટ કે એમોનિયમ ક્ષાર છે.\n• ડિટર્જન્ટના આયનો કઠિન પાણીના Ca2+ કે Mg2+ સાથે અદ્રાવ્ય ક્ષાર (સ્કમ) બનાવતા નથી.\n• તેથી ડિટર્જન્ટ કઠિન પાણીમાં પણ ઉત્તમ ફીણ આપે છે અને અસરકારક સફાઈ કરે છે.\n• ઉપયોગ: શેમ્પૂ, ડિટર્જન્ટ પાઉડર."
    })

    # Teacher Tip
    blocks.append({
        "id": next_id(),
        "type": "teacher_tip",
        "title": "Teacher Tip: Why Soap Fails to Form Micelles in Ethanol",
        "title_hi": "शिक्षक टिप: एथेनॉल में साबुन मिसेल क्यों नहीं बनाता?",
        "title_gu": "શિક્ષક ટિપ: ઇથેનોલમાં સાબુ મિસેલ શા માટે બનાવતો નથી?",
        "body": "This question appears repeatedly in board exams! In water (a polar solvent), the non-polar hydrocarbon tail fears water and clusters inwards, forcing micelle formation. But ethanol is an organic solvent that dissolves both the hydrocarbon tail and the ionic head! Because soap is completely soluble in ethanol, no hydrophobic repulsion occurs, and micelles DO NOT form.",
        "body_hi": "यह प्रश्न बोर्ड परीक्षा में बार-बार पूछा जाता है! पानी (ध्रुवीय विलायक) में हाइड्रोकार्बन पूंछ पानी से दूर भागती है और मिसेल बनाती है। लेकिन एथेनॉल एक कार्बनिक विलायक है जिसमें साबुन पूरी तरह से घुल जाता है। इसलिए एथेनॉल में मिसेल नहीं बनते हैं!",
        "body_gu": "બોર્ડ પરીક્ષા માટે મહત્વનો પ્રશ્ન! પાણીમાં હાઇડ્રોકાર્બન પૂંછડી અદ્રાવ્ય હોવાથી અંદર છુપાઈને મિસેલ બનાવે છે. પરંતુ ઇથેનોલમાં સાબુ સંપૂર્ણ ઓગળી જાય છે, તેથી કોઈ અપાકર્ષણ થતું નથી અને મિસેલ બનતા નથી!"
    })

    # Common Mistake
    blocks.append({
        "id": next_id(),
        "type": "teacher_tip",
        "title": "Common Mistake: Testing Hard Water with a Detergent",
        "title_hi": "सामान्य गलती: डिटर्जेंट से कठोर जल का परीक्षण करना",
        "title_gu": "સામાન્ય ભૂલ: ડિટર્જન્ટ વડે કઠિન પાણીની ચકાસણી કરવી",
        "body": "Can you test whether water is hard using a detergent? NO! Because detergents form lather equally well in both soft water and hard water. To test whether water is hard, you MUST use ordinary soap. If curdy white scum forms and lather is delayed, the water is hard.",
        "body_hi": "क्या आप डिटर्जेंट का उपयोग करके जांच सकते हैं कि पानी कठोर है या नहीं? बिल्कुल नहीं! क्योंकि डिटर्जेंट मृदु और कठोर दोनों पानी में समान रूप से झाग बनाता है। पानी की कठोरता जांचने के लिए साधारण साबुन का ही उपयोग करना चाहिए।",
        "body_gu": "શું તમે ડિટર્જન્ટ વડે કઠિન પાણી ચકાસી શકો? ના! કારણ કે ડિટર્જન્ટ નરમ અને કઠિન બંને પાણીમાં ફીણ આપે છે. કઠિન પાણી પારખવા માટે સાદા સાબુનો જ ઉપયોગ કરવો પડે."
    })

    # 5. Knowledge Check
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "What happens when a piece of red litmus paper is dipped into an aqueous solution of soap?",
        "question_hi": "जब लाल लिटमस पत्र के एक टुकड़े को साबुन के जलीय घोल में डुबोया जाता है तो क्या होता है?",
        "question_gu": "જ્યારે લાલ લિટમસ પેપરને સાબુના જલીય દ્રાવણમાં ડૂબાડવામાં આવે ત્યારે શું થાય છે?",
        "options": [
            "Red litmus paper turns blue (soap solution is basic)",
            "Red litmus paper turns green",
            "Red litmus paper remains red",
            "Red litmus paper bleaches white"
        ],
        "options_hi": [
            "लाल लिटमस पत्र नीला हो जाता है (साबुन का घोल क्षारीय होता है)",
            "लाल लिटमस पत्र हरा हो जाता है",
            "लाल लिटमस पत्र लाल ही रहता है",
            "लाल लिटमस पत्र सफेद हो जाता है"
        ],
        "options_gu": [
            "લાલ લિટમસ પેપર ભૂરૂં બને છે (સાબુનું દ્રાવણ બેઝિક હોય છે)",
            "લાલ લિટમસ લીલું બને છે",
            "કોઈ ફેરફાર થતો નથી",
            "સફેદ થઈ જાય છે"
        ],
        "correct_index": 0,
        "explanation": "Soap is a salt of a weak organic fatty acid and a strong base (NaOH/KOH). Upon hydrolysis in water, hydroxide ions (OH-) predominate, making the solution basic, which turns red litmus blue.",
        "explanation_hi": "साबुन एक दुर्बल फैटी एसिड और एक प्रबल क्षार (NaOH/KOH) का लवण है। जलअपघटन पर घोल क्षारीय हो जाता है, जो लाल लिटमस को नीला कर देता है।",
        "explanation_gu": "સાબુ એ નિર્બળ એસિડ અને પ્રબળ બેઝમાંથી બનેલો ક્ષાર હોવાથી તેનું જલીય દ્રાવણ બેઝિક હોય છે, જે લાલ લિટમસને ભૂરૂં બનાવે છે."
    })

    # 6. Reflection
    blocks.append({
        "id": next_id(),
        "type": "reflection",
        "title": "Environmental Impact: Biodegradable Soaps vs Synthetic Detergents",
        "title_hi": "पर्यावरणीय प्रभाव: जैव-अपघटनीय साबुन बनाम संश्लेषित डिटर्जेंट",
        "title_gu": "પર્યાવરણીય અસર: જૈવ-વિઘટનીય સાબુ વિરુદ્ધ સંશ્લેષિત ડિટર્જન્ટ",
        "body": "Soaps are 100% biodegradable because microorganisms in rivers easily break down natural straight hydrocarbon chains. Early synthetic detergents with heavily branched chains could not be degraded by bacteria, creating massive foaming mountains on lakes and rivers. Modern green chemistry requires detergents to have straight chains for rapid biodegradability.",
        "body_hi": "साबुन 100% जैव-अपघटनीय (Biodegradable) होते हैं क्योंकि सूक्ष्मजीव प्राकृतिक हाइड्रोकार्बन श्रृंखलाओं को आसानी से तोड़ देते हैं। प्रारंभिक शाखित डिटर्जेंट नदियों में झाग के विशाल पहाड़ बनाते थे। आधुनिक रसायन विज्ञान तेजी से सड़ने वाले सीधे-श्रृंखला वाले डिटर्जेंट बनाने पर जोर देता है।",
        "body_gu": "સાબુ સંપૂર્ણ જૈવ-વિઘટનીય છે કારણ કે બેક્ટેરિયા તેને સરળતાથી વિઘટિત કરે છે. શરૂઆતના શાખિત ડિટર્જન્ટ વિઘટિત ન થવાથી નદીઓમાં ફીણના પર્વતો બનતા હતા. આજના ડિટર્જન્ટ સરળતાથી વિઘટિત થાય તેવી સીધી શૃંખલાવાળા બનાવાય છે."
    })

    # 7. Connection
    blocks.append({
        "id": next_id(),
        "type": "connection",
        "title": "Why Mechanical Agitation is Essential in Washing",
        "title_hi": "कपड़े धोने में यांत्रिक रगड़ना क्यों आवश्यक है",
        "title_gu": "કપડાં ધોવામાં ઘસવું કે હલાવવું કેમ જરૂરી છે",
        "body": "Soap molecules loosen oily dirt by surrounding it with micelles, but the dirt droplet remains loosely trapped against cloth fibers. Beating clothes with a wooden paddle, rubbing on stone, or centrifugal spinning in a washing machine provides mechanical shear force to pull the micelles completely free into the wash water.",
        "body_hi": "साबुन के अणु तैलीय मैल को मिसेल से घेरकर ढीला कर देते हैं, लेकिन मैल रेशों पर चिपका रहता है। कपड़े को लकड़ी के डंडे से पीटने, पत्थर पर पटकने या वाशिंग मशीन में घुमाने से यांत्रिक बल मिलता है जो मिसेल को पानी में खींच निकालता है।",
        "body_gu": "સાબુના અણુઓ મેલની આસપાસ મિસેલ બનાવીને તેને ઢીલો કરે છે. પરંતુ કાપડના રેસામાંથી મેલને સંપૂર્ણ ખેંચી કાઢવા માટે બ્રશ મારવું, ધોકો પછાડવો કે વોશિંગ મશીનમાં ઘુમાવવું જરૂરી છે."
    })

    # 8. Mastery Challenge
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "What is the curdy white precipitate formed when soap is added to hard water containing Calcium chloride?",
        "question_hi": "कैल्शियम क्लोराइड युक्त कठोर जल में साबुन मिलाने पर बनने वाला दही जैसा सफेद अवक्षेप क्या है?",
        "question_gu": "કેલ્શિયમ ક્લોરાઇડ ધરાવતા કઠિન પાણીમાં સાબુ ઉમેરતાં બનતો દહીં જેવો સફેદ અવક્ષેપ શું છે?",
        "options": [
            "Insoluble Calcium salt of fatty acid (Scum)",
            "Soluble Sodium Chloride",
            "Calcium carbonate gas",
            "Synthetic detergent"
        ],
        "options_hi": [
            "फैटी एसिड का अघुलनशील कैल्शियम लवण (स्कम / Scum)",
            "घुलनशील सोडियम क्लोराइड",
            "कैल्शियम कार्बोनेट गैस",
            "संश्लेषित डिटर्जेंट"
        ],
        "options_gu": [
            "ફેટી એસિડનો અદ્રાવ્ય કેલ્શિયમ ક્ષાર (સ્કમ / Scum)",
            "દ્રાવ્ય સોડિયમ ક્લોરાઇડ",
            "કેલ્શિયમ કાર્બોનેટ વાયુ",
            "ડિટર્જન્ટ"
        ],
        "correct_index": 0,
        "explanation": "Soap (sodium stearate) reacts with Ca2+ ions in hard water to form insoluble calcium stearate: 2C17H35COONa + CaCl2 -> (C17H35COO)2Ca↓ + 2NaCl. This curdy precipitate is called Scum.",
        "explanation_hi": "साबुन कठोर जल में मौजूद Ca2+ आयनों के साथ प्रतिक्रिया करके अघुलनशील कैल्शियम स्टीयरेट (स्कम) बनाता है: 2C17H35COONa + CaCl2 -> (C17H35COO)2Ca↓ + 2NaCl।",
        "explanation_gu": "સાબુ કઠિન પાણીમાં રહેલા Ca2+ આયનો સાથે પ્રક્રિયા કરી અદ્રાવ્ય કેલ્શિયમ સ્ટીયરેટ બનાવે છે જેને સ્કમ કહેવાય છે."
    })

    # =========================================================================
    # NCERT IN-TEXT QUESTIONS (5 COMPREHENSIVE TEXTBOOK SETS)
    # =========================================================================

    # In-Text Set 1 (Page 61)
    blocks.append({
        "id": next_id(),
        "type": "theory",
        "title": "NCERT In-Text Questions (Page 61): Electron Dot Structures of CO2 and Sulphur S8",
        "title_hi": "NCERT पाठ्यपुस्तक इन-टेक्स्ट प्रश्न (पृष्ठ 61): CO2 और सल्फर S8 की इलेक्ट्रॉन बिंदु संरचना",
        "title_gu": "NCERT પાઠ્યપુસ્તક ઇન-ટેક્સ્ટ પ્રશ્નો (પાના 61): CO2 અને સલ્ફર S8 ની ઇલેક્ટ્રોન બિંદુ રચના",
        "body": "• QUESTION 1: What would be the electron dot structure of carbon dioxide which has the formula CO2?\n  Answer:\n  - Carbon (Atomic No. 6): Electronic Configuration (2, 4). Needs 4 electrons to complete octet.\n  - Oxygen (Atomic No. 8): Electronic Configuration (2, 6). Needs 2 electrons to complete octet.\n  - Structure: Central Carbon atom shares two pairs of electrons with each of the two Oxygen atoms, forming two double covalent bonds:\n    :Ö::C::Ö: or O=C=O\n  - Both oxygen atoms and the carbon atom achieve stable noble gas octets (8 valence electrons each).\n\n• QUESTION 2: What would be the electron dot structure of a molecule of sulphur which is made up of eight atoms of sulphur?\n  Answer:\n  - Sulphur (Atomic No. 16): Electronic Configuration (2, 8, 6). Each sulphur atom has 6 valence electrons and needs 2 electrons.\n  - In an S8 molecule, eight sulphur atoms join together in a ring or 'CROWN' shape (puckered ring).\n  - Each sulphur atom forms two single covalent bonds (one with each of its two neighbouring sulphur atoms) by sharing 1 pair of electrons with each neighbour.\n  - This leaves two non-bonding lone pairs on each sulphur atom, satisfying the octet rule for all 8 atoms.",
        "body_hi": "• प्रश्न 1: कार्बन डाइऑक्साइड (CO2) की इलेक्ट्रॉन बिंदु संरचना क्या होगी?\n  उत्तर:\n  - कार्बन (परमाणु क्रमांक 6): विन्यास (2, 4)। अष्टक पूरा करने के लिए 4 इलेक्ट्रॉन चाहिए।\n  - ऑक्सीजन (परमाणु क्रमांक 8): विन्यास (2, 6)। अष्टक पूरा करने के लिए 2 इलेक्ट्रॉन चाहिए।\n  - संरचना: केंद्रीय कार्बन परमाणु दोनों ऑक्सीजन परमाणुओं में से प्रत्येक के साथ दो-दो इलेक्ट्रॉन जोड़े साझा करता है, जिससे दो द्वि-बंध बनते हैं: O=C=O।\n\n• प्रश्न 2: सल्फर के आठ परमाणुओं से बने सल्फर के अणु (S8) की इलेक्ट्रॉन बिंदु संरचना क्या होगी?\n  उत्तर:\n  - सल्फर (परमाणु क्रमांक 16): विन्यास (2, 8, 6)। प्रत्येक सल्फर के पास 6 संयोजी इलेक्ट्रॉन हैं और उसे 2 चाहिए।\n  - S8 अणु में, आठ सल्फर परमाणु एक वलय या 'मुकुट' (Crown) के आकार में एक साथ जुड़ते हैं।\n  - प्रत्येक सल्फर परमाणु अपने दो पड़ोसी सल्फर परमाणुओं के साथ एक-एक इलेक्ट्रॉन साझा करके दो एकल सहसंयोजक बंध बनाता है।",
        "body_gu": "• પ્રશ્ન 1: કાર્બન ડાયોક્સાઇડ (CO2) ની ઇલેક્ટ્રોન બિંદુ રચના શું હશે?\n  જવાબ:\n  - કાર્બન (પરમાણુ ક્રમાંક 6): ઇલેક્ટ્રોન રચના (2, 4). અષ્ટક પૂર્ણ કરવા 4 ઇલેક્ટ્રોન જરૂરી.\n  - ઓક્સિજન (પરમાણુ ક્રમાંક 8): ઇલેક્ટ્રોન રચના (2, 6). અષ્ટક પૂર્ણ કરવા 2 ઇલેક્ટ્રોન જરૂરી.\n  - રચના: કાર્બન બંને ઓક્સિજન પૈકી દરેક સાથે બબ્બે ઇલેક્ટ્રોનની ભાગીદારી કરીને બે દ્વિ-બંધ બનાવે છે: O=C=O.\n\n• પ્રશ્ન 2: સલ્ફરના આઠ પરમાણુઓથી બનેલા સલ્ફરના અણુ (S8) ની ઇલેક્ટ્રોન બિંદુ રચના શું હશે?\n  જવાબ:\n  - સલ્ફર (પરમાણુ ક્રમાંક 16): રચના (2, 8, 6). દરેક સલ્ફર પાસે 6 સંયોજકતા ઇલેક્ટ્રોન હોય છે.\n  - S8 અણુમાં 8 સલ્ફર પરમાણુઓ મુગટ (Crown) આકારના વલયમાં જોડાય છે.\n  - દરેક સલ્ફર પોતાના બંને પાડોશી સલ્ફર સાથે એક-એક ઇલેક્ટ્રોન યુગ્મની ભાગીદારી કરી એકલ બંધ બનાવે છે."
    })

    # In-Text Set 2 (Page 68-69)
    blocks.append({
        "id": next_id(),
        "type": "theory",
        "title": "NCERT In-Text Questions (Page 68-69): Isomers, Catenation, Cyclopentane & Nomenclature",
        "title_hi": "NCERT पाठ्यपुस्तक इन-टेक्स्ट प्रश्न (पृष्ठ 68-69): समावयव, श्रृंखलन, साइक्लोपेन्टेन और नामकरण",
        "title_gu": "NCERT પાઠ્યપુસ્તક ઇન-ટેક્સ્ટ પ્રશ્નો (પાના 68-69): સમઘટકો, કેટેનેશન, સાયક્લોપેન્ટેન અને નામકરણ",
        "body": "• QUESTION 1: How many structural isomers can you draw for pentane?\n  Answer: Exactly THREE structural isomers:\n  1. n-Pentane: CH3-CH2-CH2-CH2-CH3 (straight chain)\n  2. Isopentane (2-Methylbutane): CH3-CH(CH3)-CH2-CH3 (one branch)\n  3. Neopentane (2,2-Dimethylpropane): C(CH3)4 (two branches on central carbon)\n\n• QUESTION 2: What are the two properties of carbon which lead to the huge number of carbon compounds we see around us?\n  Answer:\n  (i) Catenation: The unique ability of carbon atoms to form strong covalent bonds with other carbon atoms to form straight chains, branched chains, and rings.\n  (ii) Tetravalency: Carbon has 4 valence electrons, enabling it to bond with four other monovalent atoms (H, Cl) or with oxygen, nitrogen, and sulphur.\n\n• QUESTION 3: What will be the formula and electron dot structure of cyclopentane?\n  Answer: Molecular formula is C5H10. It is a saturated cyclic ring of 5 carbon atoms, where each carbon is bonded to two neighbouring carbons and two hydrogen atoms (total 5 C-C single bonds and 10 C-H single bonds).\n\n• QUESTION 4: Draw the structures for:\n  (i) Ethanoic acid -> CH3-COOH\n  (ii) Bromopentane -> CH3-CH2-CH2-CH2-CH2Br (structural isomers: 1-bromopentane, 2-bromopentane, 3-bromopentane)\n  (iii) Butanone -> CH3-CO-CH2-CH3\n  (iv) Hexanal -> CH3-CH2-CH2-CH2-CH2-CHO\n\n• QUESTION 5: How would you name the following compounds?\n  (i) CH3-CH2-Br -> Bromoethane\n  (ii) H-CHO -> Methanal (Formaldehyde)\n  (iii) CH3-(CH2)3-C≡CH -> Hex-1-yne",
        "body_hi": "• प्रश्न 1: पेन्टेन के लिए आप कितने संरचनात्मक समावयव बना सकते हैं?\n  उत्तर: ठीक 3 समावयव:\n  1. n-पेन्टेन (सीधी श्रृंखला)\n  2. आइसोपेंटेन / 2-मेथिलब्यूटेन (एक शाखा)\n  3. नियोपेंटेन / 2,2-डाइमेथिलप्रोपेन (दो शाखाएं)\n\n• प्रश्न 2: कार्बन के वे दो गुण कौन से हैं जो कार्बनिक यौगिकों की विशाल संख्या का कारण बनते हैं?\n  उत्तर: (i) श्रृंखलन (Catenation) और (ii) चतुःसंयोजकता (Tetravalency)।\n\n• प्रश्न 3: साइक्लोपेन्टेन का सूत्र और संरचना क्या होगी?\n  उत्तर: आणविक सूत्र C5H10 है। यह 5 कार्बन परमाणुओं का एक वलय है जिसमें 5 C-C एकल बंध और 10 C-H एकल बंध होते हैं।\n\n• प्रश्न 4: संरचनाएं बनाइए: (i) एथेनॉइक अम्ल, (ii) ब्रोमोपेन्टेन, (iii) ब्यूटेनॉन, (iv) हेक्सेनल।\n\n• प्रश्न 5: नामकरण कीजिए:\n  (i) CH3-CH2-Br -> ब्रोमोएथेन\n  (ii) H-CHO -> मेथेनल\n  (iii) CH3-(CH2)3-C≡CH -> हेक्स-1-आइन",
        "body_gu": "• પ્રશ્ન 1: પેન્ટેન માટે કેટલા બંધારણીય સમઘટકો દોરી શકાય?\n  જવાબ: બરાબર 3 સમઘટકો: 1. n-પેન્ટેન, 2. આઇસોપેન્ટેન (2-મિથાઇલબ્યુટેન), 3. નિયોપેન્ટેન (2,2-ડાયમિથાઇલપ્રોપેન).\n\n• પ્રશ્ન 2: કાર્બનના સંયોજનોની વિશાળ સંખ્યા માટે કયા બે ગુણધર્મો જવાબદાર છે?\n  જવાબ: (i) કેટેનેશન (Catenation) અને (ii) ચતુઃસંયોજકતા (Tetravalency).\n\n• પ્રશ્ન 3: સાયક્લોપેન્ટેનનું સૂત્ર શું હશે?\n  જવાબ: આણ્વીય સૂત્ર C5H10 છે. 5 કાર્બનનું વલય જેમાં 5 C-C એકલ બંધ અને 10 C-H એકલ બંધ હોય છે.\n\n• પ્રશ્ન 4: બંધારણ દોરો: (i) ઇથેનોઇક એસિડ, (ii) બ્રોમોપેન્ટેન, (iii) બ્યુટેનોન, (iv) હેક્ઝેનાલ.\n\n• પ્રશ્ન 5: નામ આપો:\n  (i) CH3-CH2-Br -> બ્રોમોઇથેન\n  (ii) H-CHO -> મિથેનાલ\n  (iii) CH3-(CH2)3-C≡CH -> હેક્સ-1-આઇન"
    })

    # In-Text Set 3 (Page 71)
    blocks.append({
        "id": next_id(),
        "type": "theory",
        "title": "NCERT In-Text Questions (Page 71): Oxidation of Ethanol & Oxy-Acetylene Welding",
        "title_hi": "NCERT पाठ्यपुस्तक इन-टेक्स्ट प्रश्न (पृष्ठ 71): एथेनॉल का ऑक्सीकरण और ऑक्सी-एसिटिलीन वेल्डिंग",
        "title_gu": "NCERT પાઠ્યપુસ્તક ઇન-ટેક્સ્ટ પ્રશ્નો (પાના 71): ઇથેનોલનું ઓક્સિડેશન અને ઓક્સી-એસિટિલીન વેલ્ડિંગ",
        "body": "• QUESTION 1: Why is the conversion of ethanol to ethanoic acid an oxidation reaction?\n  Answer:\n  - Chemical Equation: CH3CH2OH + 2[O] --[Alkaline KMnO4 + Heat]--> CH3COOH + H2O\n  - Explanation: In this reaction, one oxygen atom is added to the ethanol molecule, and two hydrogen atoms are removed from it. By definition, oxidation is a process that involves either the addition of oxygen or the removal of hydrogen. Therefore, this transformation is an oxidation reaction.\n\n• QUESTION 2: A mixture of oxygen and ethyne is burnt for welding. Can you tell why a mixture of ethyne and air is not used?\n  Answer:\n  - Ethyne (HC≡CH, Acetylene) is an unsaturated alkyne with a very high percentage of carbon.\n  - Air contains only ~21% oxygen and ~78% inert nitrogen. When ethyne is burnt in air, incomplete combustion occurs due to insufficient oxygen supply, producing an unburnt sooty yellow flame with a low flame temperature (~2200°C), which is insufficient to melt metals for welding.\n  - In pure oxygen (Oxy-acetylene torch), complete combustion occurs: 2C2H2 + 5O2 -> 4CO2 + 2H2O + immense Heat. This produces an extremely hot, clean blue flame reaching temperatures above 3000°C, high enough to easily weld and melt heavy steel.",
        "body_hi": "• प्रश्न 1: एथेनॉल से एथेनॉइक अम्ल में परिवर्तन को ऑक्सीकरण अभिक्रिया क्यों कहते हैं?\n  उत्तर: इस अभिक्रिया में एथेनॉल अणु में एक ऑक्सीजन परमाणु जुड़ता है और दो हाइड्रोजन परमाणु हटते हैं। ऑक्सीजन का जुड़ना या हाइड्रोजन का हटना ऑक्सीकरण कहलाता है।\n\n• प्रश्न 2: वेल्डिंग के लिए ऑक्सीजन और एथाइन के मिश्रण का दहन किया जाता है। क्या आप बता सकते हैं कि एथाइन और हवा के मिश्रण का उपयोग क्यों नहीं किया जाता?\n  उत्तर: एथाइन एक असंतृप्त हाइड्रोकार्बन है। हवा में केवल 21% ऑक्सीजन होती है, जिससे एथाइन का अपूर्ण दहन होता है और कालिख वाली पीली कम गर्म ज्वाला बनती है जो धातु को पिघला नहीं सकती। शुद्ध ऑक्सीजन में पूर्ण दहन होता है और 3000°C से अधिक गर्म नीली ज्वाला बनती है जो वेल्डिंग के लिए उपयुक्त है।",
        "body_gu": "• પ્રશ્ન 1: ઇથેનોલનું ઇથેનોઇક એસિડમાં રૂપાંતર એ ઓક્સિડેશન પ્રક્રિયા શા માટે છે?\n  જવાબ: આ પ્રક્રિયામાં ઇથેનોલમાં ઓક્સિજન ઉમેરાય છે અને હાઇડ્રોજન દૂર થાય છે. ઓક્સિજન ઉમેરાવો અથવા હાઇડ્રોજન દૂર થવો તેને ઓક્સિડેશન કહે છે.\n\n• પ્રશ્ન 2: વેલ્ડિંગ માટે ઓક્સિજન અને ઇથાઇનનું મિશ્રણ વપરાય છે. ઇથાઇન અને હવાનું મિશ્રણ કેમ વપરાતું નથી?\n  જવાબ: હવામાં માત્ર 21% ઓક્સિજન હોવાથી ઇથાઇનનું અપૂર્ણ દહન થાય છે અને ધુમાડાવાળી ઓછી ગરમીવાળી જ્યોત ઉત્પન્ન થાય છે જે ધાતુ ઓગાળી શકતી નથી. શુદ્ધ ઓક્સિજનમાં સંપૂર્ણ દહન થતાં 3000°C થી વધુ તાપમાનવાળી અતિ ગરમ જ્યોત મળે છે જે વેલ્ડિંગ માટે જરૂરી છે."
    })

    # In-Text Set 4 (Page 74)
    blocks.append({
        "id": next_id(),
        "type": "theory",
        "title": "NCERT In-Text Questions (Page 74): Distinguishing Alcohol and Carboxylic Acid & Oxidising Agents",
        "title_hi": "NCERT पाठ्यपुस्तक इन-टेक्स्ट प्रश्न (पृष्ठ 74): ऐल्कोहॉल और कार्बोक्सिलिक अम्ल में विभेद एवं ऑक्सीकारक",
        "title_gu": "NCERT પાઠ્યપુસ્તક ઇન-ટેક્સ્ટ પ્રશ્નો (પાના 74): આલ્કોહોલ અને કાર્બોક્સિલિક એસિડ વચ્ચે ભેદ અને ઓક્સિડેશનકર્તા",
        "body": "• QUESTION 1: How would you distinguish experimentally between an alcohol and a carboxylic acid?\n  Answer: Two reliable experimental tests:\n  1. Sodium Hydrogen Carbonate Test (Bicarbonate Test):\n     - Take small samples of both liquids in separate test tubes and add a pinch of solid Sodium Hydrogen Carbonate (NaHCO3).\n     - Carboxylic Acid: Reacts vigorously to produce brisk effervescence of colourless Carbon Dioxide (CO2) gas, which turns lime water milky.\n       CH3COOH + NaHCO3 -> CH3COONa + H2O + CO2↑\n     - Alcohol: Shows NO reaction, no effervescence, and no gas is evolved.\n  2. Litmus Test:\n     - Carboxylic acid turns moist blue litmus paper red.\n     - Alcohol is neutral and has no effect on blue or red litmus paper.\n\n• QUESTION 2: What are oxidising agents?\n  Answer:\n  - Oxidising agents are substances that have the ability to supply oxygen or remove hydrogen from other reacting substances in a chemical reaction.\n  - Key Examples in Organic Chemistry:\n    1. Alkaline Potassium Permanganate (KMnO4)\n    2. Acidified Potassium Dichromate (K2Cr2O7)\n  - These reagents supply nascent oxygen to oxidize primary alcohols into carboxylic acids.",
        "body_hi": "• प्रश्न 1: आप प्रयोगात्मक रूप से ऐल्कोहॉल और कार्बोक्सिलिक अम्ल में कैसे अंतर करेंगे?\n  उत्तर:\n  1. सोडियम हाइड्रोजन कार्बोनेट परीक्षण: कार्बोक्सिलिक अम्ल NaHCO3 के साथ तीव्र बुदबुदाहट के साथ CO2 गैस छोड़ता है जो चूने के पानी को दूधिया कर देती है। ऐल्कोहॉल कोई अभिक्रिया नहीं करता।\n  2. लिटमस परीक्षण: कार्बोक्सिलिक अम्ल नीले लिटमस को लाल कर देता है, जबकि ऐल्कोहॉल उदासीन होता है।\n\n• प्रश्न 2: ऑक्सीकारक क्या होते हैं?\n  उत्तर: वे पदार्थ जो अन्य पदार्थों को ऑक्सीजन देने या उनसे हाइड्रोजन हटाने की क्षमता रखते हैं, ऑक्सीकारक कहलाते हैं। उदाहरण: क्षारीय पोटैशियम परमैंगनेट (KMnO4) और अम्लीकृत पोटैशियम डाइક્રોमेट (K2Cr2O7)।",
        "body_gu": "• પ્રશ્ન 1: આલ્કોહોલ અને કાર્બોક્સિલિક એસિડ વચ્ચે પ્રાયોગિક રીતે કેવી રીતે ભેદ પારખશો?\n  જવાબ:\n  1. સોડિયમ બાયકાર્બોનેટ કસોટી: કાર્બોક્સિલિક એસિડ NaHCO3 સાથે ઉભરા સાથે CO2 વાયુ મુક્ત કરે છે જે ચૂનાના પાણીને દૂધિયું બનાવે છે. આલ્કોહોલ કોઈ પ્રક્રિયા આપતો નથી.\n  2. લિટમસ કસોટી: કાર્બોક્સિલિક એસિડ ભૂરા લિટમસને લાલ બનાવે છે, જ્યારે આલ્કોહોલ તટસ્થ છે.\n\n• પ્રશ્ન 2: ઓક્સિડેશનકર્તા એટલે શું?\n  જવાબ: જે પદાર્થો અન્ય પદાર્થોમાં ઓક્સિજન ઉમેરવાની અથવા હાઇડ્રોજન દૂર કરવાની ક્ષમતા ધરાવે છે તેને ઓક્સિડેશનકર્તા કહેવાય છે. ઉદાહરણ: આલ્કલાઇન KMnO4 અને એસિડિક K2Cr2O7."
    })

    # In-Text Set 5 (Page 76)
    blocks.append({
        "id": next_id(),
        "type": "theory",
        "title": "NCERT In-Text Questions (Page 76): Testing Hard Water with Detergents & Mechanical Agitation",
        "title_hi": "NCERT पाठ्यपुस्तक इन-टेक्स्ट प्रश्न (पृष्ठ 76): डिटर्जेंट द्वारा कठोर जल परीक्षण और यांत्रिक रगड़ना",
        "title_gu": "NCERT પાઠ્યપુસ્તક ઇન-ટેક્સ્ટ પ્રશ્નો (પાના 76): ડિટર્જન્ટ વડે કઠિન પાણી ચકાસણી અને યાંત્રિક ઘર્ષણ",
        "body": "• QUESTION 1: Would you be able to check if water is hard by using a detergent?\n  Answer:\n  - NO, you would NOT be able to check if water is hard by using a detergent.\n  - Reason: Detergents are sodium salts of sulphonic acids or ammonium salts with chloride/bromide ions. The charged ends of detergents do not form insoluble precipitates (scum) with the Calcium (Ca2+) and Magnesium (Mg2+) ions present in hard water. Detergents lather easily and abundantly in both soft water and hard water. To test for hardness, ordinary soap must be used (soap forms curdy scum in hard water).\n\n• QUESTION 2: People use a variety of methods to wash clothes. Usually after adding the soap, they ‘beat’ the clothes on a stone, or beat it with a paddle, scrub with a brush or the mixture is agitated in a washing machine. Why is agitation necessary to get clean clothes?\n  Answer:\n  - Soap molecules surround oily dirt on clothes to form spherical micelles, with hydrophobic hydrocarbon tails anchored inside the oil droplet and hydrophilic heads facing the water.\n  - However, the trapped oil droplet inside the micelle remains physically tangled in the microscopic fibers of the cloth.\n  - Agitation (beating, scrubbing with a brush, or machine spinning) provides the essential mechanical kinetic energy needed to dislodge, detach, and pull the micelles away from fabric pores into the bulk water so they can be completely washed away during rinsing.",
        "body_hi": "• प्रश्न 1: क्या आप डिटर्जेंट का उपयोग करके यह जांच सकते हैं कि पानी कठोर है या नहीं?\n  उत्तर: नहीं, डिटर्जेंट से कठोर जल की जांच नहीं की जा सकती क्योंकि डिटर्जेंट कठोर और मृदु दोनों जल में आसानी से झाग बनाता है और स्कम नहीं बनाता। कठोरता जांचने के लिए साबुन की आवश्यकता होती है।\n\n• प्रश्न 2: कपड़े धोते समय साबुन लगाने के बाद उन्हें पीटना, रगड़ना या मशीन में हिलाना क्यों आवश्यक है?\n  उत्तर: साबुन के अणु तैलीय मैल के चारों ओर मिसेल बनाते हैं, लेकिन मैल के कण कपड़े के रेशों में फंसे रहते हैं। पीटने या रगड़ने से आवश्यक यांत्रिक बल मिलता है जो मिसेल को रेशों से खींचकर पानी में अलग कर देता है ताकि वे धोने पर बह जाएं।",
        "body_gu": "• પ્રશ્ન 1: શું તમે ડિટર્જન્ટનો ઉપયોગ કરીને પાણી કઠિન છે કે નહિ તે ચકાસી શકો?\n  જવાબ: ના, ડિટર્જન્ટ વડે કઠિન પાણી ચકાસી શકાતું નથી કારણ કે ડિટર્જન્ટ કઠિન અને નરમ બંને પાણીમાં સરળતાથી ફીણ આપે છે અને સ્કમ બનાવતો નથી. કઠિનતા પારખવા સાબુ જ વાપરવો પડે.\n\n• પ્રશ્ન 2: કપડાં ધોતી વખતે સાબુ લગાવ્યા પછી ધોકા મારવા, બ્રશ ઘસવું કે મશીનમાં હલાવવું કેમ જરૂરી છે?\n  જવાબ: સાબુના અણુઓ તેલી મેલની ફરતે મિસેલ બનાવે છે, પરંતુ તે મેલ કાપડના રેસામાં ભરાયેલો રહે છે. યાંત્રિક રીતે ઘસવાથી કે હલાવવાથી મિસેલ રેસામાંથી મુક્ત થઈને પાણીમાં ખેંચાઈ આવે છે અને ધોવાઈ જાય છે."
    })

    # =========================================================================
    # NCERT END-OF-CHAPTER EXERCISES (QUESTIONS 1 TO 15 FULL COVERAGE)
    # =========================================================================

    # NCERT Exercise Q1
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "NCERT Exercise Q1: Ethane, with the molecular formula C2H6, has:",
        "question_hi": "NCERT अभ्यास प्रश्न 1: एथेन, जिसका आणविक सूत्र C2H6 है, में कितने सहसंयोजक बंध हैं?",
        "question_gu": "NCERT સ્વાધ્યાય પ્રશ્ન 1: ઇથેન અણુ (C2H6) માં કેટલા સહસંયોજક બંધ હોય છે?",
        "options": [
            "6 covalent bonds",
            "7 covalent bonds",
            "8 covalent bonds",
            "9 covalent bonds"
        ],
        "options_hi": [
            "6 सहसंयोजक बंध",
            "7 सहसंयोजक बंध",
            "8 सहसंयोजक बंध",
            "9 सहसंयोजक बंध"
        ],
        "options_gu": [
            "6 સહસંયોજક બંધ",
            "7 સહસંયોજક બંધ",
            "8 સહસંયોજક બંધ",
            "9 સહસંયોજક બંધ"
        ],
        "correct_index": 1,
        "explanation": "Ethane (C2H6) has 1 Carbon-Carbon (C-C) single bond and 6 Carbon-Hydrogen (C-H) single bonds, making a total of 1 + 6 = 7 covalent bonds.",
        "explanation_hi": "एथेन (C2H6) में 1 कार्बन-कार्बन (C-C) एकल बंध और 6 कार्बन-हाइड्रोजन (C-H) एकल बंध होते हैं, जिससे कुल 1 + 6 = 7 सहसंयोजक बंध बनते हैं।",
        "explanation_gu": "ઇથેન (C2H6) માં 1 કાર્બન-કાર્બન (C-C) એકલ બંધ અને 6 કાર્બન-હાઇડ્રોજન (C-H) એકલ બંધ હોય છે, આમ કુલ 1 + 6 = 7 સહસંયોજક બંધ બને છે."
    })

    # NCERT Exercise Q2
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "NCERT Exercise Q2: Butanone is a four-carbon compound with the functional group:",
        "question_hi": "NCERT अभ्यास प्रश्न 2: ब्यूटेनॉन चार-कार्बन यौगिक है जिसका प्रकार्यात्मक समूह है:",
        "question_gu": "NCERT સ્વાધ્યાય પ્રશ્ન 2: બ્યુટેનોન એ ચાર કાર્બન ધરાવતું સંયોજન છે જેમાં કયો ક્રિયાશીલ સમૂહ છે?",
        "options": [
            "Carboxylic acid",
            "Aldehyde",
            "Ketone",
            "Alcohol"
        ],
        "options_hi": [
            "कार्बोक्सिलिक अम्ल",
            "ऐल्डिहाइड",
            "कीटोन",
            "ऐल्कोहॉल"
        ],
        "options_gu": [
            "કાર્બોક્સિલિક એસિડ",
            "આલ્ડીહાઇડ",
            "કીટોન",
            "આલ્કોહોલ"
        ],
        "correct_index": 2,
        "explanation": "The suffix '-one' in Butanone indicates the presence of a Ketone functional group (-C=O).",
        "explanation_hi": "ब्यूटेनॉन में प्रत्यय '-ऑन' (one) कीटोन प्रकार्यात्मक समूह (-C=O) की उपस्थिति को दर्शाता है।",
        "explanation_gu": "બ્યુટેનોનમાં નો 'ઓન' (-one) પ્રત્યય કીટોન ક્રિયાશીલ સમૂહ (-C=O) દર્શાવે છે."
    })

    # NCERT Exercise Q3
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "NCERT Exercise Q3: While cooking, if the bottom of the vessel is getting blackened on the outside, it means that:",
        "question_hi": "NCERT अभ्यास प्रश्न 3: खाना बनाते समय यदि बर्तन की तली बाहर से काली हो रही है, तो इसका अर्थ है कि:",
        "question_gu": "NCERT સ્વાધ્યાય પ્રશ્ન 3: રસોઈ બનાવતી વખતે જો વાસણના તળિયાનો બહારનો ભાગ કાળો થતો હોય તો તેનો અર્થ એ થાય કે:",
        "options": [
            "the food is not cooked completely.",
            "the fuel is not burning completely.",
            "the fuel is wet.",
            "the fuel is burning completely."
        ],
        "options_hi": [
            "भोजन पूरी तरह से नहीं पका है।",
            "ईंधन पूरी तरह से नहीं जल रहा है।",
            "ईंधन नम (गीला) है।",
            "ईंधन पूरी तरह से जल रहा है।"
        ],
        "options_gu": [
            "ખોરાક સંપૂર્ણ રીતે રાંધવામાં આવ્યો નથી.",
            "બળતણનું સંપૂર્ણ દહન થતું નથી.",
            "બળતણ ભીનું છે.",
            "બળતણ સંપૂર્ણ રીતે સળગી રહ્યું છે."
        ],
        "correct_index": 1,
        "explanation": "Blackening of vessel bottoms is caused by soot produced during incomplete combustion of fuel due to insufficient oxygen supply.",
        "explanation_hi": "अपर्याप्त ऑक्सीजन आपूर्ति के कारण ईंधन के अपूर्ण दहन के दौरान पैदा होने वाली कालिख के कारण बर्तन की तली काली हो जाती है।",
        "explanation_gu": "અપૂરતા ઓક્સિજનના લીધે બળતણનું અપૂર્ણ દહન થાય છે જેનાથી ઉત્પન્ન થતી મેશ વાસણના તળિયાને કાળું કરે છે."
    })

    # NCERT Exercise Q4
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "NCERT Exercise Q4: In Chloromethane (CH3Cl), how are the covalent bonds formed between carbon, hydrogen, and chlorine?",
        "question_hi": "NCERT अभ्यास प्रश्न 4: क्लोरोमीथेन (CH3Cl) में कार्बन, हाइड्रोजन और क्लोरीन के बीच सहसंयोजक बंध कैसे बनते हैं?",
        "question_gu": "NCERT સ્વાધ્યાય પ્રશ્ન 4: ક્લોરોમિથેન (CH3Cl) માં કાર્બન, હાઇડ્રોજન અને ક્લોરિન વચ્ચે સહસંયોજક બંધ કેવી રીતે બને છે?",
        "options": [
            "Carbon shares 3 electron pairs with 3 Hydrogen atoms and 1 pair with Chlorine atom.",
            "Carbon transfers electrons to Chlorine and Hydrogens.",
            "Chlorine donates electrons to Carbon while Hydrogens share none.",
            "All atoms form ionic bonds by complete electron transfer."
        ],
        "options_hi": [
            "कार्बन 3 हाइड्रोजन परमाणुओं के साथ 3 इलेक्ट्रॉन जोड़े और क्लोरीन परमाणु के साथ 1 जोड़ा साझा करता है।",
            "कार्बन क्लोरीन और हाइड्रोजन को इलेक्ट्रॉन स्थानांतरित करता है।",
            "क्लोरीन कार्बन को इलेक्ट्रॉन दान करता है जबकि हाइड्रोजन कोई साझा नहीं करता है।",
            "सभी परमाणु पूर्ण इलेक्ट्रॉन स्थानांतरण द्वारा आयनिक बंध बनाते हैं।"
        ],
        "options_gu": [
            "કાર્બન 3 હાઇડ્રોજન પરમાણુઓ સાથે 3 ઇલેક્ટ્રોન યુગ્મ અને ક્લોરિન સાથે 1 યુગ્મની ભાગીદારી કરે છે.",
            "કાર્બન ક્લોરિન અને હાઇડ્રોજનને ઇલેક્ટ્રોન આપે છે.",
            "ક્લોરિન કાર્બનને ઇલેક્ટ્રોન દાન કરે છે.",
            "તમામ પરમાણુઓ ઇલેક્ટ્રોનની સંપૂર્ણ આપ-લે દ્વારા અયાનિક બંધ બનાવે છે."
        ],
        "correct_index": 0,
        "explanation": "Carbon (valency 4) shares 1 electron each with three hydrogen atoms and 1 electron with one chlorine atom to achieve noble gas electron configurations.",
        "explanation_hi": "कार्बन (संयोजकता 4) उत्कृष्ट गैस इलेक्ट्रॉन विन्यास प्राप्त करने के लिए तीन हाइड्रोजन परमाणुओं में से प्रत्येक के साथ 1 इलेक्ट्रॉन और एक क्लोरीन परमाणु के साथ 1 इलेक्ट्रॉन साझा करता है।",
        "explanation_gu": "કાર્બન (સંયોજકતા 4) નિષ્ક્રિય વાયુ જેવી રચના મેળવવા માટે ત્રણ હાઇડ્રોજન પૈકી દરેક સાથે 1 અને એક ક્લોરિન પરમાણુ સાથે 1 ઇલેક્ટ્રોનની ભાગીદારી કરે છે."
    })

    # NCERT Exercise Q5
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "NCERT Exercise Q5: Which of the following correctly describes the electron dot structure of Ethanoic Acid (CH3COOH)?",
        "question_hi": "NCERT अभ्यास प्रश्न 5: निम्नलिखित में से कौन एथेनॉइक अम्ल (CH3COOH) की इलेक्ट्रॉन बिंदु संरचना का सही वर्णन करता है?",
        "question_gu": "NCERT સ્વાધ્યાય પ્રશ્ન 5: નીચેનામાંથી કયું ઇથેનોઇક એસિડ (CH3COOH) ની ઇલેક્ટ્રોન બિંદુ રચનાનું સાચું વર્ણન કરે છે?",
        "options": [
            "Methyl carbon forms 3 C-H single bonds & 1 C-C bond; Carboxyl carbon forms 1 C=O double bond, 1 C-O single bond & O-H bond.",
            "Both carbon atoms form double bonds with oxygen atoms only.",
            "Ethanoic acid has 4 ionic bonds and 2 single covalent bonds.",
            "Carboxyl group contains no non-bonding electron pairs."
        ],
        "options_hi": [
            "मेथिल कार्बन 3 C-H एकल बंध और 1 C-C बंध बनाता है; कार्बोक्सिल कार्बन 1 C=O द्वि-बंध, 1 C-O एकल बंध और O-H बंध बनाता है।",
            "दोनों कार्बन परमाणु केवल ऑक्सीजन परमाणुओं के साथ द्वि-बंध बनाते हैं।",
            "एथेनॉइक अम्ल में 4 आयनिक बंध और 2 एकल सहसंयोजक बंध होते हैं।",
            "कार्बोक्सिल समूह में कोई गैर-बंधी इलेक्ट्रॉन जोड़े नहीं होते हैं।"
        ],
        "options_gu": [
            "મિથાઇલ કાર્બન 3 C-H એકલ બંધ અને 1 C-C બંધ બનાવે છે; કાર્બોક્સિલ કાર્બન 1 C=O દ્વિ-બંધ, 1 C-O એકલ બંધ અને O-H બંધ બનાવે છે.",
            "બંને કાર્બન પરમાણુઓ માત્ર ઓક્સિજન સાથે દ્વિ-બંધ બનાવે છે.",
            "ઇથેનોઇક એસિડમાં 4 આયનિક બંધ હોય છે.",
            "કાર્બોક્સિલ સમૂહમાં કોઈ અબંધકારક ઇલેક્ટ્રોન યુગ્મ હોતા નથી."
        ],
        "correct_index": 0,
        "explanation": "In CH3COOH, the first carbon is bonded to 3 H atoms and the second C. The second C forms a double bond with one O, and a single bond with another O which is bonded to H.",
        "explanation_hi": "CH3COOH में, पहला कार्बन 3 H परमाणुओं और दूसरे C से बंधा होता है। दूसरा C एक O के साथ द्वि-बंध और दूसरे O के साथ एकल बंध बनाता है जो H से बंधा होता है।",
        "explanation_gu": "CH3COOH માં, પ્રથમ કાર્બન 3 H પરમાણુઓ અને બીજા C સાથે જોડાયેલ છે. બીજો C એક O સાથે દ્વિ-બંધ અને H સાથે જોડાયેલા બીજા O સાથે એકલ બંધ બનાવે છે."
    })

    # NCERT Exercise Q6
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "NCERT Exercise Q6: What is a homologous series?",
        "question_hi": "NCERT अभ्यास प्रश्न 6: सजातीय श्रेणी क्या है?",
        "question_gu": "NCERT સ્વાધ્યાય પ્રશ્ન 6: સજાતીય શ્રેણી એટલે શું?",
        "options": [
            "A series of organic compounds having the same functional group and similar chemical properties.",
            "A mixture of compounds with different molecular formulas but same physical state.",
            "A series of elements arranged by increasing atomic number.",
            "Compounds having identical boiling points and physical structures."
        ],
        "options_hi": [
            "समान प्रकार्यात्मक समूह और समान रासायनिक गुणों वाले कार्बनिक यौगिकों की एक श्रृंखला।",
            "विभिन्न आणविक सूत्रों वाले लेकिन समान भौतिक अवस्था वाले यौगिकों का मिश्रण।",
            "परमाणु संख्या बढ़ाने के आधार पर व्यवस्थित तत्वों की एक श्रृंखला।",
            "समान क्वथनांक और भौतिक संरचना वाले यौगिक।"
        ],
        "options_gu": [
            "સમાન ક્રિયાશીલ સમૂહ અને સમાન રાસાયણિક ગુણધર્મો ધરાવતા કાર્બનિક સંયોજનોની શ્રેણી.",
            "જુદા જુદા આણ્વીય સૂત્રો પરંતુ સમાન ભૌતિક સ્થિતિ ધરાવતા સંયોજનોનું મિશ્રણ.",
            "વધતા પરમાણુ ક્રમાંક અનુસાર ગોઠવાયેલા તત્વોની શ્રેણી.",
            "સમાન ઉત્કલનબિંદુ ધરાવતા સંયોજનો."
        ],
        "correct_index": 0,
        "explanation": "A homologous series is a group of carbon compounds having the same functional group, similar chemical properties, and consecutive members differing by -CH2-.",
        "explanation_hi": "सजातीय श्रेणी कार्बन यौगिकों का एक समूह है जिसमें समान प्रकार्यात्मक समूह, समान रासायनिक गुण होते हैं, और लगातार सदस्य -CH2- से भिन्न होते हैं।",
        "explanation_gu": "સજાતીય શ્રેણી એ કાર્બન સંયોજનોનું એવું જૂથ છે જે સમાન ક્રિયાશીલ સમૂહ અને સમાન રાસાયણિક ગુણધર્મો ધરાવે છે અને ક્રમિક સભ્યો -CH2- વડે જુદા પડે છે."
    })

    # NCERT Exercise Q7
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "NCERT Exercise Q7: How can Ethanol and Ethanoic acid be differentiated chemically?",
        "question_hi": "NCERT अभ्यास प्रश्न 7: एथेनॉल और एथेनॉइक अम्ल को रासायनिक रूप से कैसे विभेदित किया जा सकता है?",
        "question_gu": "NCERT સ્વાધ્યાય પ્રશ્ન 7: ઇથેનોલ અને ઇથેનોઇક એસિડ વચ્ચે રાસાયણિક રીતે કેવી રીતે ભેદ પાડી શકાય?",
        "options": [
            "Ethanoic acid reacts with Sodium Hydrogen Carbonate releasing CO2 gas (effervescence), whereas Ethanol does not.",
            "Ethanol turns blue litmus red while Ethanoic acid has no effect.",
            "Ethanoic acid turns green on burning while Ethanol turns yellow.",
            "Ethanol reacts with NaOH to give CO2 gas while Ethanoic acid gives H2 gas."
        ],
        "options_hi": [
            "एथेनॉइक अम्ल सोडियम हाइड्रोजन कार्बोनेट के साथ प्रतिक्रिया करके CO2 गैस (बुदबुदाहट) छोड़ता है, जबकि एथेनॉल नहीं करता है।",
            "एथेनॉल नीले लिटमस को लाल कर देता है जबकि एथेनॉइक अम्ल का कोई प्रभाव नहीं पड़ता है।",
            "एथेनॉइक अम्ल जलने पर हरा हो जाता है जबकि एथेनॉल पीला हो जाता है।",
            "एथेनॉल NaOH के साथ प्रतिक्रिया करके CO2 गैस देता है जबकि एथेनॉइक अम्ल H2 गैस देता है।"
        ],
        "options_gu": [
            "ઇથેનોઇક એસિડ સોડિયમ હાઇડ્રોજન કાર્બોનેટ (NaHCO3) સાથે પ્રક્રિયા કરી ઉભરા સાથે CO2 વાયુ મુક્ત કરે છે, જ્યારે ઇથેનોલ આ પ્રક્રિયા આપતો નથી.",
            "ઇથેનોલ ભૂરા લિટમસને લાલ બનાવે છે જ્યારે ઇથેનોઇક એસિડ કોઈ અસર દર્શાવતો નથી.",
            "ઇથેનોઇક એસિડ સળગાવતા લીલો થાય છે.",
            "ઇથેનોલ NaOH સાથે પ્રક્રિયા કરી CO2 આપે છે."
        ],
        "correct_index": 0,
        "explanation": "Carboxylic acids react with carbonates/bicarbonates (e.g., NaHCO3) to liberate CO2 gas with effervescence. Alcohols like Ethanol do not give this reaction.",
        "explanation_hi": "कार्बोक्सिलिक अम्ल कार्बोनेट/बाइकार्बोनेट (जैसे NaHCO3) के साथ प्रतिक्रिया करके बुदबुदाहट के साथ CO2 गैस मुक्त करते हैं। एथेनॉल जैसे ऐल्कोहॉल यह प्रतिक्रिया नहीं देते हैं।",
        "explanation_gu": "કાર્બોક્સિલિક એસિડ કાર્બોનેટ/બાયકાર્બોનેટ (જેમ કે NaHCO3) સાથે પ્રક્રિયા કરી ઉભરા સાથે CO2 વાયુ મુક્ત કરે છે. ઇથેનોલ જેવા આલ્કોહોલ આ પ્રક્રિયા આપતા નથી."
    })

    # NCERT Exercise Q8
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "NCERT Exercise Q8: Why does micelle formation take place when soap is added to water, and will micelles form in ethanol?",
        "question_hi": "NCERT अभ्यास प्रश्न 8: जब पानी में साबुन मिलाया जाता है तो मिसेल का निर्माण क्यों होता है, और क्या एथेनॉल में मिसेल बनेंगे?",
        "question_gu": "NCERT સ્વાધ્યાય પ્રશ્ન 8: જ્યારે સાબુને પાણીમાં ઉમેરવામાં આવે છે ત્યારે મિસેલ શા માટે બને છે, અને શું ઇથેનોલમાં મિસેલ બનશે?",
        "options": [
            "Micelles form in water because the hydrophobic hydrocarbon tail avoids water; micelles will NOT form in ethanol because soap dissolves in ethanol.",
            "Micelles form in ethanol but not in water.",
            "Micelles form equally well in water, ethanol, and petrol.",
            "Micelles form only when water is heated above 100°C."
        ],
        "options_hi": [
            "पानी में मिसेल बनते हैं क्योंकि जलविरागी हाइड्रोकार्बन पूंछ पानी से दूर रहती है; एथेनॉल में मिसेल नहीं बनेंगे क्योंकि साबुन एथेनॉल में पूरी तरह घुल जाता है।",
            "मिसेल एथेनॉल में बनते हैं लेकिन पानी में नहीं।",
            "मिसेल पानी, एथेनॉल और पेट्रोल में समान रूप से बनते हैं।",
            "मिसेल केवल तभी बनते हैं जब पानी को 100°C से ऊपर गर्म किया जाता है।"
        ],
        "options_gu": [
            "પાણીમાં મિસેલ બને છે કારણ કે જલપ્રતિકારક હાઇડ્રોકાર્બન પૂંછડી પાણીથી દૂર રહે છે; ઇથેનોલમાં મિસેલ બનશે નહિ કારણ કે સાબુ ઇથેનોલમાં સંપૂર્ણ ઓગળી જાય છે.",
            "મિસેલ ઇથેનોલમાં બને છે પણ પાણીમાં નહિ.",
            "મિસેલ પાણી અને ઇથેનોલમાં સમાન રીતે બને છે.",
            "પાણીને 100°C થી વધુ ગરમ કરવામાં આવે ત્યારે જ મિસેલ બને છે."
        ],
        "correct_index": 0,
        "explanation": "Soap molecules form micelles in water because of the dual polarity (hydrophilic head & hydrophobic tail). In ethanol, soap is soluble, so hydrophobic tails do not need to cluster away; hence no micelles form.",
        "explanation_hi": "साबुन के अणु दोहरी ध्रुवीयता (जलरागी सिर और जलविरागी पूंछ) के कारण पानी में मिसेल बनाते हैं। एथेनॉल में साबुन घुलनशील होता है, इसलिए मिसेल नहीं बनते हैं।",
        "explanation_gu": "સાબુના અણુઓ તેમની દ્વિધ્રુવીય પ્રકૃતિને લીધે પાણીમાં મિસેલ બનાવે છે. ઇથેનોલમાં સાબુ દ્રાવ્ય હોવાથી મિસેલ બનતા નથી."
    })

    # NCERT Exercise Q9
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "NCERT Exercise Q9: Why are carbon and its compounds used as fuels for most applications?",
        "question_hi": "NCERT अभ्यास प्रश्न 9: अधिकांश अनुप्रयोगों के लिए कार्बन और इसके यौगिकों का उपयोग ईंधन के रूप में क्यों किया जाता है?",
        "question_gu": "NCERT સ્વાધ્યાય પ્રશ્ન 9: મોટાભાગના ઉપયોગો માટે કાર્બન અને તેના સંયોજનોનો ઉપયોગ બળતણ તરીકે શા માટે થાય છે?",
        "options": [
            "They release a large amount of heat energy per unit mass upon combustion and produce manageable ignition temperatures.",
            "They are non-combustible and completely safe.",
            "They produce zero carbon dioxide when burned.",
            "They are metals that conduct high amounts of heat."
        ],
        "options_hi": [
            "वे दहन पर प्रति इकाई द्रव्यमान में बड़ी मात्रा में ऊष्मा ऊर्जा छोड़ते हैं और उनका प्रज्वलन तापमान उपयुक्त होता है।",
            "वे गैर-दहनशील और पूरी तरह से सुरक्षित हैं।",
            "जलने पर वे शून्य कार्बन डाइऑक्साइड पैदा करते हैं।",
            "वे धातुएं हैं जो अत्यधिक ऊष्मा का संचालन करती हैं।"
        ],
        "options_gu": [
            "તેઓ દહન દરમિયાન પ્રતિ એકમ દળ દીઠ ઉચ્ચ ઉષ્મા ઉર્જા આપે છે અને યોગ્ય જ્વલનબિંદુ ધરાવે છે.",
            "તેઓ અદ્રાવ્ય અને અદહનશીલ છે.",
            "તેઓ સળગતા CO2 મુક્ત કરતા નથી.",
            "તેઓ ધાતુઓ છે."
        ],
        "correct_index": 0,
        "explanation": "Carbon compounds have high calorific values, burn easily in air releasing immense heat and light energy, making them ideal fuels.",
        "explanation_hi": "कार्बन यौगिकों का कैलोरी मान उच्च होता है, वे अत्यधिक ऊष्मा और प्रकाश ऊर्जा छोड़ते हुए हवा में आसानी से जलते हैं, जिससे वे आदर्श ईंधन बनते हैं।",
        "explanation_gu": "કાર્બન સંયોજનોનું કેલરી મૂલ્ય ઊંચું હોય છે, તે હવા માં સરળતાથી સળગીને મુશ્કેલી વગર મોટી માત્રામાં ઉષ્મા મુક્ત કરે છે."
    })

    # NCERT Exercise Q10
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "NCERT Exercise Q10: Explain the formation of scum when hard water is treated with soap.",
        "question_hi": "NCERT अभ्यास प्रश्न 10: कठोर जल को साबुन से उपचारित करने पर स्कम बनने की व्याख्या करें।",
        "question_gu": "NCERT સ્વાધ્યાય પ્રશ્ન 10: કઠિન પાણીમાં સાબુ ઉમેરતા બનતા 'સ્કમ' (અવક્ષેપ) ની બનાવટ સમજાવો.",
        "options": [
            "Ca2+ and Mg2+ ions in hard water react with soap molecules to form insoluble calcium and magnesium salts of fatty acids (scum).",
            "Sodium ions react with soap to form insoluble salt.",
            "Soap evaporates leaving behind pure scum.",
            "Hard water turns soap into synthetic detergent."
        ],
        "options_hi": [
            "कठोर जल में Ca2+ और Mg2+ आयन साबुन के अणुओं के साथ प्रतिक्रिया करके फैटी एसिड के अघुलनशील कैल्शियम और मैग्नीशियम लवण (स्कम) बनाते हैं।",
            "सोडियम आयन साबुन के साथ प्रतिक्रिया करके अघुलनशील लवण बनाते हैं।",
            "साबुन वाष्पित हो जाता है और पीछे शुद्ध स्कम छोड़ जाता है।",
            "कठोर जल साबुन को संश्लेषित डिटर्जेंट में बदल देता है।"
        ],
        "options_gu": [
            "કઠિન પાણીમાં રહેલા Ca2+ અને Mg2+ આયનો સાબુ સાથે પ્રક્રિયા કરીને અદ્રાવ્ય કેલ્શિયમ અને મેગ્નેશિયમ ક્ષાર (સ્કમ) બનાવે છે.",
            "સોડિયમ આયનો પ્રક્રિયા કરી અદ્રાવ્ય ક્ષાર બનાવે છે.",
            "સાબુનું બાષ્પીભવન થાય છે.",
            "કઠિન પાણી સાબુને ડિટર્જન્ટમાં બદલે છે."
        ],
        "correct_index": 0,
        "explanation": "Hard water contains soluble Ca2+ and Mg2+ salts. When soap (sodium fatty acid salt) is added, it forms insoluble calcium and magnesium fatty acid precipitates called scum.",
        "explanation_hi": "कठोर जल में घुलनशील Ca2+ और Mg2+ लवण होते हैं। जब साबुन (सोडियम फैटी एसिड लवण) मिलाया जाता है, तो यह अघुलनशील कैल्शियम और मैग्नीशियम फैटी एसिड अवक्षेप बनाता है जिसे स्कम कहा जाता है।",
        "explanation_gu": "કઠિન પાણીમાં Ca2+ અને Mg2+ ક્ષારો ઓગળેલા હોય છે. સાબુ ઉમેરતાં તે અદ્રાવ્ય કેલ્શિયમ અને મેગ્નેશિયમ ક્ષાર બનાવે છે જેને સ્કમ કહેવાય છે."
    })

    # NCERT Exercise Q11
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "NCERT Exercise Q11: What change will you observe if you test soap solution with red and blue litmus paper?",
        "question_hi": "NCERT अभ्यास प्रश्न 11: यदि आप लाल और नीले लिटमस पत्र से साबुन के घोल का परीक्षण करते हैं तो आप क्या परिवर्तन देखेंगे?",
        "question_gu": "NCERT સ્વાધ્યાય પ્રશ્ન 11: જો તમે લાલ અને ભૂરા લિટમસ પેપર વડે સાબુના દ્રાવણની ચકાસણી કરો તો શું ફેરફાર જોવા મળશે?",
        "options": [
            "Red litmus turns blue; blue litmus remains blue (Soap solution is basic in nature).",
            "Blue litmus turns red; red litmus remains red.",
            "Both litmus papers turn green.",
            "No change in either litmus paper."
        ],
        "options_hi": [
            "लाल लिटमस नीला हो जाता है; नीला लिटमस नीला ही रहता है (साबुन का घोल प्रकृति में क्षारीय होता है)।",
            "नीला लिटमस लाल हो जाता है; लाल लिटमस लाल ही रहता है।",
            "दोनों लिटमस पत्र हरे हो जाते हैं।",
            "किसी भी लिटमस पत्र में कोई परिवर्तन नहीं होता।"
        ],
        "options_gu": [
            "લાલ લિટમસ ભૂરૂં બને છે; ભૂરૂં લિટમસ ભૂરૂં જ રહે છે (સાબુનું દ્રાવણ બેઝિક પ્રકૃતિ ધરાવે છે).",
            "ભૂરૂં લિટમસ લાલ બને છે.",
            "બંને લિટમસ લીલા બને છે.",
            "કોઈ ફેરફાર થતો નથી."
        ],
        "correct_index": 0,
        "explanation": "Soap is a salt of a weak acid (fatty acid) and a strong base (NaOH/KOH). Hence, its aqueous solution is basic and turns red litmus blue.",
        "explanation_hi": "साबुन एक दुर्बल अम्ल (फैटी एसिड) और एक प्रबल क्षार (NaOH/KOH) का लवण है। इसलिए, इसका जलीय घोल क्षारीय होता है और लाल लिटमस को नीला कर देता है।",
        "explanation_gu": "સાબુ એ નિર્બળ એસિડ અને પ્રબળ બેઝમાંથી બનેલો ક્ષાર છે. આથી તેનું જલીય દ્રાવણ બેઝિક હોય છે જે લાલ લિટમસને ભૂરૂં બનાવે છે."
    })

    # NCERT Exercise Q12
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "NCERT Exercise Q12: What is hydrogenation and what is its industrial application?",
        "question_hi": "NCERT अभ्यास प्रश्न 12: हाइड्रोजनकरण क्या है और इसका औद्योगिक अनुप्रयोग क्या है?",
        "question_gu": "NCERT સ્વાધ્યાય પ્રશ્ન 12: હાઇડ્રોજનીકરણ એટલે શું અને તેનો ઔદ્યોગિક ઉપયોગ શું છે?",
        "options": [
            "Addition of H2 to unsaturated hydrocarbons using Ni/Pd catalyst to form saturated fats; used to convert vegetable oil to Vanaspati Ghee.",
            "Removal of H2 from saturated hydrocarbons to form alkenes; used in plastic manufacturing.",
            "Reaction of carbon with oxygen to produce water.",
            "Conversion of sugar into ethanol by fermentation."
        ],
        "options_hi": [
            "संतृप्त वसा बनाने के लिए Ni/Pd उत्प्रेरक का उपयोग करके असंतृप्त हाइड्रोकार्बन में H2 का संकलन; वनस्पति तेल को वनस्पति घी में बदलने के लिए उपयोग किया जाता है।",
            "ऐल्कीन बनाने के लिए संतृप्त हाइड्रोकार्बन से H2 को हटाना।",
            "पानी बनाने के लिए कार्बन की ऑक्सीजन के साथ प्रतिक्रिया।",
            "किण्वन द्वारा शर्करा का एथेनॉल में परिवर्तन।"
        ],
        "options_gu": [
            "Ni/Pd ઉદ્દીપકની હાજરીમાં અસંતૃપ્ત હાઇડ્રોકાર્બનમાં H2 ઉમેરી સંતૃપ્ત ચરબી બનાવવી; વનસ્પતિ તેલમાંથી વનસ્પતિ ઘી બનાવવામાં વપરાય છે.",
            "સંતૃપ્ત હાઇડ્રોકાર્બનમાંથી H2 દૂર કરવાની પ્રક્રિયા.",
            "કાર્બનની ઓક્સિજન સાથેની પ્રક્રિયા.",
            "આથવણ દ્વારા ખાંડનું ઇથેનોલમાં રૂપાંતર."
        ],
        "correct_index": 0,
        "explanation": "Hydrogenation is the addition of hydrogen to unsaturated hydrocarbons in the presence of nickel catalyst. Industrially, liquid vegetable oils are hydrogenated to form solid Vanaspati ghee.",
        "explanation_hi": "हाइड्रोजनकरण निकेल उत्प्रेरक की उपस्थिति में असंतृप्त हाइड्रोकार्बन में हाइड्रोजन का जुड़ना है। औद्योगिक रूप से, तरल वनस्पति तेलों का हाइड्रोजनकरण करके ठोस वनस्पति घी बनाया जाता है।",
        "explanation_gu": "હાઇડ્રોજનીકરણ એ નિકલ ઉદ્દીપકની હાજરીમાં અસંતૃપ્ત હાઇડ્રોકાર્બનમાં હાઇડ્રોજન ઉમેરવાની પ્રક્રિયા છે. વનસ્પતિ તેલમાંથી વનસ્પતિ ઘી બનાવવામાં આનો ઉપયોગ થાય છે."
    })

    # NCERT Exercise Q13
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "NCERT Exercise Q13: Which of the following hydrocarbons undergo addition reactions: C2H6, C3H8, C3H6, C2H2, CH4?",
        "question_hi": "NCERT अभ्यास प्रश्न 13: निम्नलिखित में से कौन से हाइड्रोकार्बन संकलन (addition) अभिक्रियाएं करते हैं: C2H6, C3H8, C3H6, C2H2, CH4?",
        "question_gu": "NCERT સ્વાધ્યાય પ્રશ્ન 13: નીચેનામાંથી કયા હાઇડ્રોકાર્બન યોગશીલ પ્રક્રિયા આપશે: C2H6, C3H8, C3H6, C2H2, CH4?",
        "options": [
            "C3H6 (Propene) and C2H2 (Ethyne)",
            "C2H6 (Ethane) and CH4 (Methane)",
            "C3H8 (Propane) and C2H6 (Ethane)",
            "All of the above"
        ],
        "options_hi": [
            "C3H6 (प्रोपीन) और C2H2 (एथाइन)",
            "C2H6 (एथेन) और CH4 (मीथेन)",
            "C3H8 (प्रोपेन) और C2H6 (एथेन)",
            "उपरोक्त सभी"
        ],
        "options_gu": [
            "C3H6 (પ્રોપીન) અને C2H2 (ઇથાઇન)",
            "C2H6 (ઇથેન) અને CH4 (મિથેન)",
            "C3H8 (પ્રોપેન) અને C2H6 (ઇથેન)",
            "આપેલ તમામ"
        ],
        "correct_index": 0,
        "explanation": "Only unsaturated hydrocarbons (alkenes and alkynes) undergo addition reactions. C3H6 is Propene (alkene) and C2H2 is Ethyne (alkyne). C2H6, C3H8, and CH4 are saturated alkanes.",
        "explanation_hi": "केवल असंतृप्त हाइड्रोकार्बन (ऐल्कीन और ऐल्काइन) ही संकलन अभिक्रियाएं करते हैं। C3H6 प्रोपीन है और C2H2 एथाइन है। C2H6, C3H8, और CH4 संतृप्त ऐल्केन हैं।",
        "explanation_gu": "માત્ર અસંતૃપ્ત હાઇડ્રોકાર્બન (એલ્કીન અને એલ્કાઇન) જ યોગશીલ પ્રક્રિયા આપે છે. C3H6 (પ્રોપીન) અને C2H2 (ઇથાઇન) અસંતૃપ્ત છે."
    })

    # NCERT Exercise Q14
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "NCERT Exercise Q14: Which chemical test can differentiate between butter and cooking oil?",
        "question_hi": "NCERT अभ्यास प्रश्न 14: मक्खन (butter) और खाना पकाने के तेल (cooking oil) के बीच विभेद करने के लिए किस रासायनिक परीक्षण का उपयोग किया जा सकता है?",
        "question_gu": "NCERT સ્વાધ્યાય પ્રશ્ન 14: માખણ અને રસોઈના તેલ વચ્ચે રાસાયણિક ભેદ પારખવા કઈ કસોટી વપરાય છે?",
        "options": [
            "Bromine Water Test: Cooking oil decolourizes bromine water (unsaturated), whereas butter does not (saturated).",
            "Litmus Paper Test: Cooking oil turns red litmus blue.",
            "Sodium Hydroxide Test: Butter releases H2 gas.",
            "Flame Test: Cooking oil burns with green flame."
        ],
        "options_hi": [
            "ब्रोमीन जल परीक्षण: खाना पकाने का तेल ब्रोमीन जल को रंगहीन कर देता है (असंतृप्त), जबकि मक्खन नहीं करता (संतृप्त)।",
            "लिटमस पत्र परीक्षण: खाना पकाने का तेल लाल लिटमस को नीला कर देता है।",
            "सोडियम हाइड्रोक्साइड परीक्षण: मक्खन H2 गैस छोड़ता है।",
            "ज्वाला परीक्षण: खाना पकाने का तेल हरी ज्वाला के साथ जलता है।"
        ],
        "options_gu": [
            "બ્રોમિન જળ કસોટી: રસોઈનું તેલ અસંતૃપ્ત હોવાથી બ્રોમિન જળનો રંગ દૂર કરે છે, જ્યારે સંતૃપ્ત માખણ રંગ દૂર કરતું નથી.",
            "લિટમસ પેપર કસોટી.",
            "સોડિયમ હાઇડ્રોક્સાઇડ કસોટી.",
            "જ્યોત કસોટી."
        ],
        "correct_index": 0,
        "explanation": "Cooking oil contains unsaturated fats which decolourize bromine water via addition reaction. Butter contains saturated fats and does not decolourize bromine water.",
        "explanation_hi": "खाना पकाने के तेल में असंतृप्त वसा होती है जो संकलन अभिक्रिया के माध्यम से ब्रोमीन पानी को रंगहीन कर देती है। मक्खन में संतृप्त वसा होती है और यह ब्रोमीन जल को रंगहीन नहीं करता है।",
        "explanation_gu": "રસોઈના તેલમાં અસંતૃપ્ત ચરબી હોય છે જે યોગશીલ પ્રક્રિયા દ્વારા બ્રોમિન જળનો રંગ દૂર કરે છે. માખણમાં સંતૃપ્ત ચરબી હોવાથી તે રંગ દૂર કરતું નથી."
    })

    # NCERT Exercise Q15
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "NCERT Exercise Q15: What is the key mechanism of the cleaning action of soaps?",
        "question_hi": "NCERT अभ्यास प्रश्न 15: साबुन की सफाई क्रिया का मुख्य तंत्र क्या है?",
        "question_gu": "NCERT સ્વાધ્યાય પ્રશ્ન 15: સાબુની સફાઈ પ્રક્રિયાની મુખ્ય કાર્યપદ્ધતિ શું છે?",
        "options": [
            "Hydrophobic tails attach to oily dirt while hydrophilic ionic heads face outward in water, forming micelles that entrap dirt.",
            "Soap dissolves cloth fibers to release dirt particles.",
            "Soap neutralizes dirt by converting all dirt into gas.",
            "Hydrophilic heads attach to oily dirt while hydrophobic tails face water."
        ],
        "options_hi": [
            "जलविरागी पूंछ तैलीय मैल से जुड़ती है जबकि जलरागी आयनिक सिर पानी में बाहर की ओर रहते हैं, मिसेल बनाते हैं जो मैल को फंसा लेते हैं।",
            "मैल के कणों को छोड़ने के लिए साबुन कपड़े के रेशों को घोल देता है।",
            "साबुन सभी मैल को गैस में बदलकर बेअसर कर देता है।",
            "जलरागी सिर तैलीय मैल से जुड़ते हैं जबकि जलविरागी पूंछ पानी का सामना करती है।"
        ],
        "options_gu": [
            "જલપ્રતિકારક પૂંછડી તેલી મેલ સાથે જોડાય છે જ્યારે જલઅનુરાગી છેડો બહાર પાણી તરફ રહે છે, જે મિસેલ રચના બનાવી મેલને ખેંચી કાઢે છે.",
            "સાબુ કાપડના રેસા ઓગાળી નાખે છે.",
            "સાબુ મેલનું વાયુમાં રૂપાંતર કરે છે.",
            "જલઅનુરાગી છેડો તેલ સાથે જોડાય છે."
        ],
        "correct_index": 0,
        "explanation": "Soap molecules form spherical micelles where hydrophobic hydrocarbon tails point inward toward the oil drop and hydrophilic ionic heads face water. Upon rinsing, micelles containing grease are lifted away.",
        "explanation_hi": "साबुन के अणु गोलाकार मिसेल बनाते हैं जहाँ जलविरागी हाइड्रोकार्बन पूंछ अंदर तेल की बूंद की ओर इशारा करती है और जलरागी आयनिक सिर पानी की ओर होते हैं। धोने पर, ग्रीस वाले मिसेल बह जाते हैं।",
        "explanation_gu": "સાબુના અણુઓ ગોળાકાર મિસેલ બનાવે છે જ્યાં જલપ્રતિકારક હાઇડ્રોકાર્બન પૂંછડી તેલ તરફ અને જલઅનુરાગી છેડો પાણી તરફ રહે છે. પાણીથી ધોતાં મેલ મિસેલ સાથે દૂર થાય છે."
    })

    # =========================================================================
    # BOARD EXAM MASTERY CHALLENGES
    # =========================================================================

    # Board Mastery 1
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "Which of the following allotropes of carbon has a cage-like spherical structure consisting of twenty hexagons and twelve pentagons?",
        "question_hi": "कार्बन के निम्नलिखित में से किस अपररूप में बीस षट्कोणों और बारह पंचकोणों से युक्त पिंजरे जैसी गोलाकार संरचना होती है?",
        "question_gu": "કાર્બનનું કયું બહુરૂપ વીસ ષટ્કોણ અને બાર પંચકોણ ધરાવતી પિંજરા જેવી ગોળાકાર રચના ધરાવે છે?",
        "options": [
            "Buckminsterfullerene (C60)",
            "Diamond",
            "Graphite",
            "Carbon Nanotubes"
        ],
        "options_hi": [
            "बकमिंस्टरफुलरीन (C60)",
            "हीरा",
            "ग्रेफाइट",
            "कार्बन नैनोट्यूब"
        ],
        "options_gu": [
            "બકમિનિસ્ટર ફુલરીન (C60)",
            "હીરો",
            "ગ્રેફાઇટ",
            "કાર્બન નેનોટ્યુબ"
        ],
        "correct_index": 0,
        "explanation": "Buckminsterfullerene (C60) consists of 60 carbon atoms arranged in 20 hexagonal and 12 pentagonal rings, resembling a geodesic soccer ball.",
        "explanation_hi": "बकमिंस्टरफुलरीन (C60) में 20 षट्कोणीय और 12 पंचकोणीय वलयों में व्यवस्थित 60 कार्बन परमाणु होते हैं, जो एक सॉकर बॉल से मिलते-जुलते हैं।",
        "explanation_gu": "બકમિનિસ્ટર ફુલરીન (C60) માં 20 ષટ્કોણ અને 12 પંચકોણમાં ગોઠવાયેલા 60 કાર્બન પરમાણુઓ ફૂટબોલ જેવી રચના બનાવે છે."
    })

    # Board Mastery 2
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "Vinegar used in our kitchen as a food preservative is a solution of:",
        "question_hi": "खाद्य परिरक्षक के रूप में हमारी रसोई में उपयोग किया जाने वाला सिरका किसका विलयन है?",
        "question_gu": "ખોરાકની જાળવણી માટે રસોડામાં વપરાતો સરકો એ કોનું દ્રાવણ છે?",
        "options": [
            "5-8% solution of Ethanoic acid in water",
            "50% solution of Ethanoic acid in water",
            "100% pure glacial acetic acid",
            "5-8% solution of Ethanol in water"
        ],
        "options_hi": [
            "जल में एथेनॉइक अम्ल का 5-8% विलयन",
            "जल में एथेनॉइक अम्ल का 50% विलयन",
            "100% शुद्ध ग्लैशियल एसिटिक अम्ल",
            "जल में एथेनॉल का 5-8% विलयन"
        ],
        "options_gu": [
            "પાણીમાં ઇથેનોઇક એસિડનું 5-8% દ્રાવણ",
            "પાણીમાં ઇથેનોઇક એસિડનું 50% દ્રાવણ",
            "100% શુદ્ધ ગ્લેશિયલ એસિટિક એસિડ",
            "પાણીમાં ઇથેનોલનું 5-8% દ્રાવણ"
        ],
        "correct_index": 0,
        "explanation": "Vinegar is commercially prepared as a 5% to 8% aqueous solution of Ethanoic acid (acetic acid) in water.",
        "explanation_hi": "सिरका व्यावसायिक रूप से पानी में एथेनॉइक अम्ल (एसिटिक एसिड) के 5% से 8% जलीय घोल के रूप में तैयार किया जाता है।",
        "explanation_gu": "સરકો વ્યાપારી રીતે પાણીમાં ઇથેનોઇક એસિડના 5% થી 8% દ્રાવણ તરીકે બનાવાય છે."
    })

    # Board Mastery 3
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "Which of the following statements about soaps and detergents is FALSE?",
        "question_hi": "साबुन और डिटर्जेंट के बारे में निम्नलिखित में से कौन सा कथन असत्य है?",
        "question_gu": "સાબુ અને ડિટર્જન્ટ અંગે નીચેનામાંથી કયું વિધાન ખોટું છે?",
        "options": [
            "Soaps work efficiently and lather abundantly in hard water.",
            "Soaps are sodium salts of long-chain fatty acids.",
            "Synthetic detergents do not form scum in hard water.",
            "Soap molecules form spherical micelles in aqueous solutions."
        ],
        "options_hi": [
            "साबुन कठोर जल में कुशलतापूर्वक काम करते हैं और प्रचुर मात्रा में झाग बनाते हैं।",
            "साबुन लंबी श्रृंखला वाले फैटी एसिड के सोडियम लवण हैं।",
            "संश्लेषित डिटर्जेंट कठोर जल में स्कम नहीं बनाते हैं।",
            "साबुन के अणु जलीय घोल में गोलाकार मिसेल बनाते हैं।"
        ],
        "options_gu": [
            "સાબુ કઠિન પાણીમાં અસરકારક રીતે કામ કરે છે અને પુષ્કળ ફીણ આપે છે.",
            "સાબુ ફેટી એસિડના સોડિયમ ક્ષાર છે.",
            "સંશ્લેષિત ડિટર્જન્ટ કઠિન પાણીમાં સ્કમ બનાવતા નથી.",
            "સાબુના અણુઓ પાણીમાં મિસેલ બનાવે છે."
        ],
        "correct_index": 0,
        "explanation": "Statement A is FALSE: Soaps react with Ca2+ and Mg2+ in hard water to form insoluble scum, which destroys lather and wastes soap. Synthetic detergents work well in hard water.",
        "explanation_hi": "कथन A असत्य है: साबुन कठोर जल में Ca2+ और Mg2+ के साथ अघुलनशील स्कम बनाते हैं, जिससे झाग नष्ट होता है। कठोर जल में डिटर्जेंट अच्छा काम करते हैं।",
        "explanation_gu": "વિધાન A ખોટું છે: સાબુ કઠિન પાણીમાં અદ્રાવ્ય ક્ષાર 'સ્કમ' બનાવે છે, જેથી ફીણ થતું નથી. કઠિન પાણીમાં ડિટર્જન્ટ જ સારું કામ કરે છે."
    })

    final_payload = {
        "metadata": metadata,
        "blocks": blocks
    }

    # Output to NCERT chapter path
    output_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_science_ch4.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(final_payload, f, ensure_ascii=False, indent=2)
    print(f"✅ Generated {len(blocks)} blocks successfully in {output_path}")

    # Output to GSEB chapter path for full syllabus parity
    gseb_output_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_science_ch4.json"
    gseb_payload = dict(final_payload)
    gseb_payload["metadata"] = dict(metadata)
    gseb_payload["metadata"]["id"] = "gseb_class10_science_ch4"
    gseb_payload["metadata"]["board"] = "GSEB"
    with open(gseb_output_path, "w", encoding="utf-8") as f:
        json.dump(gseb_payload, f, ensure_ascii=False, indent=2)
    print(f"✅ Generated GSEB copy in {gseb_output_path}")

if __name__ == "__main__":
    build_ncert_class10_science_ch4()
