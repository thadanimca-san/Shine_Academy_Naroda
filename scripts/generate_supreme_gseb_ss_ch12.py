import json
import os

def generate_supreme_gseb_ss_ch12():
    chapter_id = "gseb_class10_social_science_ch12"
    title = "Chapter 12: India: Minerals and Energy Resources"
    
    metadata = {
        "id": chapter_id,
        "title": title,
        "subtitle": "The Ultimate Board Exam Mastery Guide & Socratic Discovery Arc",
        "subject": "Social Science",
        "grade": "10",
        "board": "GSEB/NCERT",
        "curriculum": ["GSEB", "CBSE", "Universal"],
        "language": "English/Hindi/Gujarati (Bilingual)",
        "difficulty": "Advanced",
        "estimated_minutes": 180,
        "version": "3.0.0-SUPREME-PEDAGOGY",
        "author": "Antigravity Supreme Intelligence",
        "reviewed_by": "Chief Academic Architect",
        "tags": [
            "social_science",
            "geography",
            "minerals",
            "energy_resources",
            "metallic_minerals",
            "non_metallic_minerals",
            "coal",
            "petroleum",
            "natural_gas",
            "solar_energy",
            "nuclear_energy",
            "gujarat_resources",
            "board_special",
            "bilingual"
        ],
        "learning_outcomes": [
            "Understand the definition of minerals and trace the evolutionary mineral ages of human civilization.",
            "Classify minerals into metallic (precious, light, general use, alloy formers), non-metallic, and energy minerals.",
            "Locate and explain the distribution, extraction, and industrial significance of major metallic minerals (Iron Ore, Manganese, Copper, Bauxite) and non-metallic minerals (Mica, Limestone, Gypsum) across India and Gujarat.",
            "Distinguish between conventional energy resources (Coal types, Petroleum fields, Natural Gas pipelines) and non-conventional renewable energy (Solar, Wind, Biogas, Geothermal, Tidal, Nuclear).",
            "Identify key map locations for Board Exams including major mines, oilfields, refineries, and nuclear power stations (Kakrapar, Tarapur, Kudremukh, Ankleshwar, Jharia, Digboi, Charanka).",
            "Formulate strategic approaches for mineral conservation and sustainable development using the 4R framework."
        ],
        "ai_context": {
            "learning_goal": "Transform the student from a memorizer to an insightful board topper in Social Science Geography. Integrate Socratic questioning, real-world connections, map-pointing mnemonics, and bilingual translations.",
            "common_misconceptions": [
                "Students confuse Bauxite (ore) with Aluminium (pure metal).",
                "Students mix up Coal grades (Anthracite vs Lignite) and their carbon percentages.",
                "Students assume Petroleum is found in igneous rocks instead of sedimentary anticlinal traps.",
                "Students confuse the locations of Kakrapar (Gujarat), Tarapur (Maharashtra), and Rawatbhata (Rajasthan) on the map.",
                "Students forget that Brass is Copper + Zinc while Bronze is Copper + Tin."
            ],
            "tutor_hint": "If a student struggles with mineral classifications, guide them through the practical items in their home: utensils (Iron/Aluminium/Copper), wires (Copper), toothpaste (Limestone/Mica), vehicle fuel (Petroleum). Connect every concept to daily life."
        }
    }
    
    blocks = []
    
    # =========================================================================
    # MODULE 1: THE MYSTERY OF MINERALS & HUMAN CIVILIZATION AGES
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "Take a look at the smartphone `(स्मार्टफोन / સ્માર્ટફોન)` in your hand, the vehicle on the road, or the building standing tall outside. Did you know that a single smartphone contains over 30 different **Minerals `(खनिज / ખનીજ)`**—from copper in its motherboard, gold and silver in micro-connectors, lithium in its battery, to quartz in its touch screen? Human history itself is not divided by kings or wars, but by the minerals humans learned to master! Let us embark on a thrilling discovery into the Earth's hidden treasure chest.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "socratic_question",
        "content": "Why do historians name entire human eras as the 'Stone Age', 'Bronze Age', and 'Iron Age'? What makes minerals the true benchmark of human progress and national power `(राष्ट्रीय शक्ति / રાષ્ટ્રીય શક્તિ)`?",
        "difficulty": "Beginner",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "theory",
        "content": "### What is a Mineral? `(खनिज क्या है? / ખનીજ એટલે શું?)`\n\nA **Mineral `(खनिज / ખનીજ)`** is a naturally occurring inorganic substance `(अकार्बनिक पदार्थ / અકાર્બનિક પદાર્થ)` with a definite chemical composition `(निश्चित रासायनिक संरचना / ચોક્કસ રાસાયણિક બંધારણ)` and a distinct crystalline physical structure `(क्रिस्टलीय संरचना / સ્ફટિકમય રચના)` formed through geological processes over millions of years.\n\nMinerals in the Earth's crust are found in three principal rock types:\n1. **Igneous Rocks `(आग्नेय चट्टानें / આગ્નેય ખડકો)`:** Minerals like iron, copper, zinc, gold, and diamond form when molten magma cools and solidifies in cracks and crevices.\n2. **Sedimentary Rocks `(अवसादी / प्रस्तर चट्टानें / પ્રસ્તર ખડકો)`:** Minerals like coal, petroleum, limestone, and gypsum deposit in horizontal strata `(परतें / સ્તરો)` through prolonged accumulation and compression.\n3. **Metamorphic Rocks `(कायांतरित / रूपांतरित चट्टानें / રૂપાંતરિત ખડકો)`:** Under extreme heat and pressure, minerals recrystallize into new forms, such as marble from limestone and slate from clay.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "The Evolutionary Timeline of Human Mineral Ages: From flint stones to atomic fission reactors.",
        "image_url": "assets/images/ss_ch12_mineral_ages_timeline.jpg",
        "alt_text": "Timeline showing Stone Age, Copper Age, Bronze Age, Iron Age, and Modern Atomic Age."
    })
    
    blocks.append({
        "type": "theory",
        "content": "### Evolutionary Stages of Mineral Usage in Human History\n\nHuman civilization has evolved through five progressive mineral epochs `(खनिज युग / ખનીજ યુગ)`:\n1. **Stone Age `(पाषाण युग / પાષાણ યુગ)`:** Early humans hunted with crude stone tools and flint pebbles.\n2. **Copper Age `(ताम्र युग / તામ્ર યુગ)`:** Copper was the **first metal discovered and used** by humans for knives and pots.\n3. **Bronze Age `(कांस्य युग / કાંસ્ય યુગ)`:** Humans learned metallurgy by alloying copper with tin to make tougher weapons and sculptures (e.g., Indus Valley Dancing Girl).\n4. **Iron Age `(लौह युग / લોહ યુગ)`:** Enabled massive deforestation, deep agriculture, railway networks, and industrial revolutions.\n5. **Atomic / Modern Age `(परमाणु / अंतरिक्ष युग / અણુ અને અંતરીક્ષ યુગ)`:** Utilization of uranium, thorium, rare earth elements, and silicon for nuclear energy, supercomputers, and space exploration.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Teacher's Secret:** Remember this chronological sequence for Board MCQs: **Stone ⟶ Copper ⟶ Bronze ⟶ Iron ⟶ Atomic**. Remember that **Copper** was humanity's first discovered metal, NOT Iron!",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "mcq",
        "question_text": "Which was the first metal used by humans in civilization?",
        "options": [
            "Iron `(लोहा / લોખંડ)`",
            "Copper `(तांबा / તાંબુ)`",
            "Aluminium `(एल्युमिनियम / એલ્યુમિનિયમ)`",
            "Gold `(सोना / સોનું)`"
        ],
        "correct_answer": "Copper `(तांबा / તાંબુ)`",
        "explanation": "Copper was the first metal discovered and shaped by prehistoric humans, marking the transition from the Stone Age to the Copper Age (Chalcolithic Period).",
        "distractor_rationale": "Iron was mastered much later due to its higher melting point; Aluminium was isolated only in the 19th century.",
        "bloom": "Remember",
        "difficulty": "Beginner"
    })
    
    # =========================================================================
    # MODULE 2: CLASSIFICATION OF MINERALS (METALLIC, NON-METALLIC, ENERGY)
    # =========================================================================
    blocks.append({
        "type": "diagram",
        "content": "Comprehensive Classification Tree of Minerals: Metallic, Non-Metallic, and Energy Minerals.",
        "image_url": "assets/images/ss_ch12_mineral_classification_chart.jpg",
        "alt_text": "Flowchart classifying minerals into Metallic (Precious, Light, General, Alloys), Non-Metallic, and Energy Minerals."
    })
    
    blocks.append({
        "type": "theory",
        "content": "### Systematic Classification of Minerals `(खनिजों का वर्गीकरण / ખનીજોનું વર્ગીકરણ)`\n\nMinerals are broadly classified into three major categories based on their physical and chemical properties:\n\n#### 1. Metallic Minerals `(धात्विक खनिज / ધાતુમય ખનીજો)`\nMinerals containing raw metals that can be melted and molded:\n- **(a) Precious Metallic Minerals `(कीमती धातुमय खनिज / કીમતી ધાતુમય ખનીજો)`:** Gold `(सोना / સોનું)`, Silver `(चांदी / ચાંદી)`, Platinum `(प्लैटिनम / પ્લેટિનમ)`.\n- **(b) Light Metallic Minerals `(हल्की धातुमय खनिज / હલકી ધાતુમય ખનીજો)`:** Magnesium `(मैग्नीशियम / મેગ્નેશિયમ)`, Bauxite `(बॉक्साइट / બોક્સાઈટ)`, Titanium `(टाइटेनियम / ટાઇટેનિયમ)`.\n- **(c) Minerals of General Use `(सामान्य उपयोग वाले खनिज / સામાન્ય ઉપયોગમાં લેવાતા ખનીજો)`:** Iron `(लोहा / લોખંડ)`, Copper `(तांबा / તાંબુ)`, Lead `(सीसा / સીસું)`, Zinc `(जस्ता / જસત)`, Tin `(टिन / કલાઈ)`, Nickel `(निकल / નિકલ)`.\n- **(d) Minerals Used as Alloys `(मिश्र धातु बनाने वाले खनिज / મિશ્રધાતુ બનાવવામાં વપરાતા ખનીજો)`:** Chromium `(क्रोमियम / ક્રોમિયમ)`, Manganese `(मैंगनीज / મેંગેનીઝ)`, Tungsten `(टंगस्टन / ટંગસ્ટન)`, Vanadium `(वेनेडियम / વેનેડિયમ)`.\n\n#### 2. Non-Metallic Minerals `(अधात्विक खनिज / અધાતુમય ખનીજો)`\nMinerals that do not contain metals and break or crumble when hammered:\n- Limestone `(चूना पत्थर / ચૂનાનો પથ્થર)`, Mica `(अभ्रक / અબરખ)`, Gypsum `(जिप्सम / ચિરોડી)`, Calcite `(कैल्साइट / કેલ્સાઇટ)`, Silica/Quartz `(सिलिका / સિલિકા)`, Asbestos `(एस्बेस्टस / એસ્બેસ્ટોસ)`, Fluorite/Fluorspar `(फ्लोराइट / ફ્લોરસ્પાર)`.\n\n#### 3. Energy Minerals `(ऊर्जा संसाधन खनिज / ઊર્જા ખનીજો)`\nMinerals used to generate mechanical power, heat, and electricity:\n- **Conventional:** Coal `(कोयला / કોલસો)`, Mineral Oil/Petroleum `(खनिज तेल / ખનીજ તેલ)`, Natural Gas `(प्राकृतिक गैस / કુદરતી વાયુ)`.\n- **Nuclear:** Uranium `(यूरेनियम / યુરેનિયમ)`, Thorium `(थोरियम / થોરિયમ)`.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "memory_trick",
        "content": "🧠 **Mnemonic for Light Metallic Minerals:** **'B-M-T'** (Like Big Mountain Trek) ⟶ **B**auxite, **M**agnesium, **T**itanium!\n\n🧠 **Mnemonic for Alloy Forming Minerals:** **'C-M-T-V'** (Colour Music TV) ⟶ **C**hromium, **M**anganese, **T**ungsten, **V**anadium!",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "common_mistakes",
        "content": "⚠️ **BOARD EXAM PITFALL:** Many students mistakenly classify Coal and Petroleum as 'Non-Metallic Minerals'. In the GSEB/NCERT schema, they belong specifically to the **Energy Minerals `(ऊर्जा खनिज / ઊર્જા ખનીજો)`** category!",
        "difficulty": "Intermediate",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "mcq",
        "question_text": "Which of the following is classified as a 'Light Metallic Mineral' `(हल्की धातुमय खनिज / હલકી ધાતુમય ખનીજ)`?",
        "options": [
            "Lead `(सीसा / સીસું)`",
            "Bauxite `(बॉक्साइट / બોક્સાઈટ)`",
            "Tungsten `(टंगस्टन / ટંગસ્ટન)`",
            "Mica `(अभ्रक / અબરખ)`"
        ],
        "correct_answer": "Bauxite `(बॉक्साइट / બોક્સાઈટ)`",
        "explanation": "Bauxite is the primary ore of Aluminium, known worldwide for its lightweight, low density, and high tensile strength.",
        "distractor_rationale": "Lead is a heavy general use metal; Tungsten is an alloy former; Mica is non-metallic.",
        "bloom": "Remember",
        "difficulty": "Beginner"
    })
    
    # =========================================================================
    # MODULE 3: MAJOR METALLIC MINERALS OF INDIA
    # =========================================================================
    blocks.append({
        "type": "theory",
        "content": "### 1. Iron Ore `(लौह अयस्क / લોખંડ અયસ્ક)`: The Backbone of Modern Industry\n\nIron ore is the foundation of modern heavy engineering, railways, bridges, and defense machines. India possesses vast reserves of high-grade iron ore.\n\n#### Types of Iron Ore (Based on Iron Content):\n1. **Magnetite `(मैग्नेटाइट / મેગ્નેટાઇટ)`:** Purest ore with up to **70% iron content**. Possesses exceptional magnetic qualities `(चुंबकीय गुण / ચુંબકીય ગુણધર્મો)`.\n2. **Hematite `(हेमेटाइट / હેમેટાઇટ)`:** Most widely used industrial ore with **50% to 60% iron content**.\n3. **Limonite `(लिमोनाइट / લિમોનાઇટ)`:** Yellowish-brown ore with **40% to 50% iron content**.\n4. **Siderite `(साइडराइट / સાઇડેરાઇટ)`:** Carbonate iron ore with **20% to 40% iron content**.\n\n#### Major Iron Ore Belts in India:\n- **Odisha-Jharkhand Belt:** High-grade hematite ore found in Badampahar mines in Mayurbhanj and Kendujhar (Odisha) and Gua/Noamundi in Singhbhum district (Jharkhand).\n- **Durg-Bastar-Chandrapur Belt:** World-class super-high-grade hematite found in the famous **Bailadila Hills `(बैलाडीला पहाड़ियां / બૈલાડીલા ટેકરીઓ)`** in Bastar (Chhattisgarh), exported to Japan and South Korea via Visakhapatnam port.\n- **Ballari-Chitradurga-Chikkamagaluru-Tumakuru Belt (Karnataka):** Features the world-renowned **Kudremukh `(कुद्रेमुख / કુદ્રેમુખ)` mines** (100% export unit). Ore is transported as liquid slurry `(घोल / સ્લરી)` through pipelines to Mangaluru port!\n- **Maharashtra-Goa Belt:** Marmagao port handles iron exports from Goa and Ratnagiri.",
        "difficulty": "Advanced",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Map of India highlighting major Iron Ore belts, Bauxite clusters, and Copper mining centers.",
        "image_url": "assets/images/ss_ch12_metallic_minerals_map.jpg",
        "alt_text": "Geographical map of India marking Bailadila, Kudremukh, Singhbhum, Khetri, and Balaghat."
    })
    
    blocks.append({
        "type": "theory",
        "content": "### 2. Manganese `(मैंगनीज / મેંગેનીઝ)`: The Steel Strengthener\n\n- **Industrial Role:** Manganese is primarily used in the manufacturing of **Steel `(इस्पात / પોલાદ)`**. Approximately **10 kg of manganese** is required to manufacture 1 tonne of steel!\n- **Other Uses:** Used in bleaching powder `(ब्लीचिंग पाउडर / બ્લીચિંગ પાઉડર)`, insecticides `(कीटनाशक / જંતુનાશકો)`, dry battery cells `(शुष्क सेल / સૂકા કોષ)`, paints, and glass.\n- **Leading States:** Odisha is the largest producer, followed by Karnataka, Madhya Pradesh, Maharashtra, and Andhra Pradesh.\n\n---\n\n### 3. Copper `(तांबा / તાંબુ)`: The Electric Lifeline\n\n- **Properties:** Extremely malleable `(आघातवर्धनीय / ટીપાવપાત્ર)`, ductile `(तन्य / તન્ય)`, and an exceptional conductor of electricity and heat.\n- **Alloys `(मिश्र धातुएं / મિશ્રધાતુઓ)`:**\n  - **Brass `(पीतल / પીતળ)`** = Copper + Zinc `(तांबा + जस्ता / તાંબુ + જસત)`\n  - **Bronze `(कांसा / કાંસું)`** = Copper + Tin `(तांबा + कलाई / તાંબુ + કલાઈ)`\n  - **German Silver** = Copper + Zinc + Nickel\n- **Leading Producers:** Madhya Pradesh (**Balaghat mines** produces ~52% of India's copper), Rajasthan (**Khetri mines** in Jhunjhunu), and Jharkhand (**Singhbhum district**).\n\n---\n\n### 4. Bauxite `(बॉक्साइट / બોક્સાઈટ)`: The Ore of Aluminium\n\n- **Properties of Aluminium:** Lightweight like plastic, strong like steel, rust-proof, and an excellent conductor.\n- **Leading States in India:** **Odisha** is the single largest producer (Panchpatmali deposits in Koraput & Kalahandi), followed by Gujarat, Jharkhand, Maharashtra, and Chhattisgarh.\n- **Gujarat's Rich Bauxite Belts:** Jamnagar, Devbhumi Dwarka, Junagadh, Kutch, Bhavnagar, and Sabarkantha.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Alloy Equation Cheat-Code for Exams:**\n- **Brass = Cu + Zn** *(Remember: 'Brother Cuz' ⟶ Brass = Copper + Zinc)*\n- **Bronze = Cu + Sn** *(Remember: 'Bronze Medalist Tin' ⟶ Bronze = Copper + Tin)*\nBoard papers frequently ask this 1-mark identification question!",
        "difficulty": "Intermediate",
        "bloom": "Apply"
    })
    
    blocks.append({
        "type": "mcq",
        "question_text": "How much Manganese is approximately required to manufacture 1 tonne of steel?",
        "options": [
            "100 kg",
            "10 kg",
            "50 kg",
            "2 kg"
        ],
        "correct_answer": "10 kg",
        "explanation": "Around 10 kilograms of manganese ore is required as a deoxidizing and strengthening agent to manufacture one tonne of steel.",
        "distractor_rationale": "100 kg is too high; 2 kg is insufficient to alter steel tensile characteristics.",
        "bloom": "Remember",
        "difficulty": "Intermediate"
    })
    
    # =========================================================================
    # MODULE 4: NON-METALLIC MINERALS (MICA, LIMESTONE, GYPSUM)
    # =========================================================================
    blocks.append({
        "type": "theory",
        "content": "### 1. Mica `(अभ्रक / અબરખ)`: The Insulator of the Electronics World\n\n- **Special Properties:** Mica is made up of a series of plates or leaves. It splits easily into wafer-thin transparent sheets. It has excellent **dielectric strength `(परावैद्युत शक्ति / ડાઇઇલેક્ટ્રિક ક્ષમતા)`**, low power loss factor, insulating properties `(अचालक गुण / અવાહક ગુણધર્મ)`, and resistance to extreme high voltages.\n- **Global Position:** India is the **world's largest producer** of Sheet Mica (Muscovite Mica).\n- **Major Belts:**\n  - **Jharkhand:** Koderma-Gaya-Hazaribagh belt (known as the 'Mica Capital of the World').\n  - **Andhra Pradesh:** Nellore belt.\n  - **Rajasthan:** Bhilwara, Jaipur, and Ajmer.\n\n---\n\n### 2. Limestone `(चूना पत्थर / ચૂનાનો પથ્થર)`: The Foundation of Cement\n\n- **Usage:** Essential raw material for the **Cement Industry `(सीमेंट उद्योग / સિમેન્ટ ઉદ્યોગ)`** and a smelting flux in blast furnaces for iron manufacturing.\n- **Occurrence:** Associated with sedimentary rocks composed of calcium carbonates or calcium-magnesium carbonates.\n- **Gujarat's Contribution:** Gujarat is one of India's leading producers of high-quality limestone, found in **Jamnagar, Junagadh, Porbandar, Kutch, Amreli, and Surat** districts.\n\n---\n\n### 3. Gypsum `(जिप्सम / ચિરોડી)`\n\n- **Usage:** Critical in regulating the setting time of cement, manufacturing Plaster of Paris (POP), chemical fertilizers, and soil reclamation.\n- **Major Producers:** Rajasthan (produces over 90% of India's gypsum), followed by Jammu & Kashmir and Gujarat (Kutch, Jamnagar).",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "real_world_example",
        "content": "✨ **Sparkle in Your Toothpaste:** Have you ever noticed the sparkling glitter in modern white toothpaste or cosmetic creams? That shimmering sparkle comes from finely ground **Mica `(अभ्रक / અબરખ)`**! Meanwhile, the abrasive cleaning agent that cleans your teeth is **Limestone `(चूना पत्थर / ચૂનાનો પથ્થર)`**!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "mcq",
        "question_text": "Which mineral is indispensable in the electrical and electronic industries due to its high dielectric strength and insulating capability?",
        "options": [
            "Mica `(अभ्रक / અબરખ)`",
            "Gypsum `(जिप्सम / ચિરોડી)`",
            "Bauxite `(बॉक्साइट / બોક્સાઈટ)`",
            "Limestone `(चूना पत्थर / ચૂનાનો પથ્થર)`"
        ],
        "correct_answer": "Mica `(अभ्रक / અબરખ)`",
        "explanation": "Mica's resistance to high voltage, low power loss, and superior thermal insulation make it irreplaceable in capacitors, transformers, and electronic circuitry.",
        "distractor_rationale": "Gypsum and Limestone are non-conductive construction minerals; Bauxite yields aluminium which is a conductor.",
        "bloom": "Understand",
        "difficulty": "Intermediate"
    })
    
    # =========================================================================
    # MODULE 5: CONVENTIONAL ENERGY RESOURCES (COAL, PETROLEUM, NATURAL GAS)
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "Imagine the world suddenly waking up with zero electricity, no petrol in cars, and no cooking gas in kitchen cylinders. Civilization would grind to an immediate halt! Where does all this energy come from? Deep inside the Earth's belly, millions of years of compressed sunlight and ancient forests have been stored as **Fossil Fuels `(जीवाश्म ईंधन / અશ્મિભૂત બળતણ)`**.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "content": "### 1. Coal `(कोयला / કોલસો)`: The Black Gold\n\nCoal is the most abundantly available fossil fuel in India, fulfilling over 55% of our nation's commercial energy needs.\n\n#### The 4 Grades of Coal (Classified by Carbon Content & Heat Value):\n1. **Anthracite `(एंथ्रेसाइट / એન્થ્રેસાઇટ)`:**\n   - **Carbon Content:** Above **80% to 90%**.\n   - **Characteristics:** Hardest, glossy black, smokeless burning, highest calorific heat value. Found only in small quantities in Jammu & Kashmir.\n2. **Bituminous `(बिटुमिनस / બિટ્યુમિનસ)`:**\n   - **Carbon Content:** **70% to 80%**.\n   - **Characteristics:** Most popular commercial and metallurgical coal used in thermal power plants and smelting iron.\n3. **Lignite `(लिग्नाइट / લિગ્નાઇટ - Brown Coal)`:**\n   - **Carbon Content:** **40% to 55%**.\n   - **Characteristics:** Soft, high moisture, low heating power. Major reserves at **Neyveli (Tamil Nadu)** and **Panandhro, Umarsar, Rajpardi (Gujarat)**.\n4. **Peat `(पीट / પીટ)`:**\n   - **Carbon Content:** Less than **40%**.\n   - **Characteristics:** First stage of wood decay, low heat capacity, emits heavy smoke.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "memory_trick",
        "content": "🧠 **Memory Code for Coal Quality:** Alphabetical Order **A ⟶ B ⟶ L ⟶ P**\n- **A** = Anthracite (Best Quality, >80% Carbon)\n- **B** = Bituminous (Commercial Standard, 70-80% Carbon)\n- **L** = Lignite (Brown Coal, 40-55% Carbon)\n- **P** = Peat (Poor Quality, <40% Carbon)",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "theory",
        "content": "### Geological Eras of Indian Coal:\n- **Gondwana Coal `(गोंडवाना कोयला / ગોંડવાના કોલસો)`:** Over 200 million years old, metallurgical coal located in the Damodar Valley (Jharkhand-West Bengal border: **Jharia, Raniganj, Bokaro**), Mahanadi Valley, and Godavari Valley.\n- **Tertiary Coal `(टर्शियरी कोयला / ટર્શિયરી કોલસો)`:** Approximately 55 million years old, found in Assam, Meghalaya, Arunachal Pradesh, Nagaland, and Gujarat.\n\n---\n\n### 2. Mineral Oil & Petroleum `(खनिज तेल एवं पेट्रोलियम / ખનીજ તેલ અને પેટ્રોલિયમ)`\n\n- **Geological Occurrence:** Formed from ancient marine organisms buried in sedimentary anticlines `(अपनति / ઊર્ધ્વવળાંક)` and fault traps. Liquid petroleum floats above water, while natural gas collects at the very top under impervious cap rocks.\n- **History:** First drilled in India at **Makum (Assam) in 1867**. **Digboi (Assam)** is the oldest continuously operating oilfield in Asia!\n\n#### Major Oil Fields of India:\n1. **Mumbai High `(मुंबई हाई / મુંબઈ હાઈ)`:** Offshore field 176 km off Mumbai in the Arabian Sea (discovered in 1974), operated using the giant floating jack-up rig **'Sagar Samrat' `(सागर सम्राट / સાગર સમ્રાટ)`**. Produces ~60% of India's indigenous crude.\n2. **Gujarat Oil Fields:**\n   - **Ankleshwar `(अंकलेश्वर / અંકલેશ્વર)`:** Largest onshore field in Gujarat, fondly called *'Vasudhara'* (Stream of Wealth) by Pandit Nehru.\n   - **Other Gujarat Fields:** Kalol, Nawagam, Mehsana, Gandhar, Lunej (first well in Gujarat drilled in 1958), and Aliabet island.\n3. **Eastern Coast:** Krishna-Godavari and Cauvery offshore basins.\n\n#### Major Oil Refineries `(तेल शोधनशालाएं / તેલ શુદ્ધિકરણ શાળાઓ)`:\n- **Jamnagar Refinery (Gujarat):** Operated by Reliance Industries, it is the **world's largest grassroots petroleum refining complex**!\n- **Koyali Refinery (Vadodara, Gujarat):** Major public sector refinery by Indian Oil Corporation (IOCL).\n- Other key refineries: Trombay, Mathura, Panipat, Barauni, Haldia, Digboi, Kochi.",
        "difficulty": "Advanced",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Geological cross-section of an anticlinal oil and natural gas trap deep inside sedimentary strata.",
        "image_url": "assets/images/ss_ch12_petroleum_trap_geology.jpg",
        "alt_text": "Diagram showing non-porous rock layer trapping natural gas at the top, crude oil in the middle, and saline water at the bottom."
    })
    
    blocks.append({
        "type": "theory",
        "content": "### 3. Natural Gas `(प्राकृतिक गैस / કુદરતી વાયુ)`: The Clean Fuel of the 21st Century\n\n- **Eco-Friendly Advantages:** Burns cleanly with minimal carbon emissions, negligible ash, and zero toxic smoke. Used as **CNG (Compressed Natural Gas)** for pollution-free transport and **PNG (Piped Natural Gas)** for domestic kitchens.\n- **HVJ Gas Pipeline:** India's landmark **1,750 km Hazira-Vijaipur-Jagdishpur (HVJ)** arterial pipeline connects Hazira in Gujarat across Madhya Pradesh to Jagdishpur in Uttar Pradesh, supplying gas to fertilizer and power complexes.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "mcq",
        "question_text": "Which offshore oil exploration platform is deployed at Mumbai High in the Arabian Sea?",
        "options": [
            "Sagar Samrat `(सागर सम्राट / સાગર સમ્રાટ)`",
            "Sagar Kanya `(सागर कन्या / સાગર કન્યા)`",
            "Samudra Ratna `(समुद्र रत्न / સમુદ્ર રત્ન)`",
            "Vikrant `(विक्रांत / વિક્રાંત)`"
        ],
        "correct_answer": "Sagar Samrat `(सागर सम्राट / સાગર સમ્રાટ)`",
        "explanation": "Sagar Samrat is India's famous self-propelled jack-up offshore drilling rig that helped discover and tap the immense Mumbai High oilfields in 1974.",
        "distractor_rationale": "Sagar Kanya is a research vessel; Vikrant is an aircraft carrier.",
        "bloom": "Remember",
        "difficulty": "Intermediate"
    })
    
    # =========================================================================
    # MODULE 6: NON-CONVENTIONAL / RENEWABLE ENERGY RESOURCES
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "Fossil fuels are running out fast and polluting our planet. But every single morning, the Sun bathes India in endless cosmic energy, coastal winds roar along our 7,500 km coastline, and deep subterranean heat boils hot water springs. Welcome to the limitless realm of **Non-Conventional & Renewable Energy `(गैर-पारंपरिक एवं नवीकरणीय ऊर्जा / બિન-પરંપરાગત અને પુનઃપ્રાપ્ય ઊર્જા)`**!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "content": "### 1. Solar Energy `(सौर ऊर्जा / સૌર ઊર્જા)`\n- **Mechanism:** Photovoltaic cells `(फोटोवोल्टाइक सेल / ફોટોવોલ્ટેઇક સેલ)` convert sunlight photons directly into electrical DC voltage.\n- **India's Advantage:** Located near the Tropic of Cancer, India enjoys over 300 clear sunny days per year (~5,000 trillion kWh annual solar irradiation).\n- **Gujarat's Leadership:** Home to the mega **Charanka Solar Park `(चारणका सोलर पार्क / ચારણકા સોલર પાર્ક)`** in Patan district and massive rooftop solar adoption under the Surya Gujarat scheme.\n\n---\n\n### 2. Wind Energy `(पवन ऊर्जा / પવન ઊર્જા)`\n- **Mechanism:** Kinetic energy of ocean breezes drives large turbine blades to turn electricity generators.\n- **India's Position:** India ranks among the top global wind energy producers.\n- **Major Centers:** Muppandal wind farm cluster in Tamil Nadu (largest operational site); **Lamba wind farm near Porbandar** and **Mandvi coast in Gujarat**.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "content": "### 3. Biogas `(बायोगैस / બાયોગેસ)`: Clean Rural Energy & Organic Fertilizer\n- **Process:** Anaerobic digestion `(अवायवीय अपघटन / અજારક વિઘટન)` of cattle dung (gobar), farm waste, and domestic sewage by bacteria produces **Methane Gas `(मीथेन गैस / મિથેન વાયુ)` (~60-70%)** and carbon dioxide.\n- **Double Benefit:** Provides smoke-free cooking fuel in rural homes and yields high-grade organic nitrogen-rich fertilizer `(जैविक खाद / જૈવિક ખાતર)`.\n- **Gujarat's Pioneer Project:** **Methan village `(मेथान गाँव / મેથાણ ગામ)`** in Sidhpur taluka (Patan district) operates one of India's largest community-based rural biogas plants!\n\n---\n\n### 4. Geothermal Energy `(भू-तापीय ऊर्जा / ભૂ-તાપીય ઊર્જા)`\n- **Concept:** Harnessing underground thermal heat and high-pressure steam generated where groundwater contacts boiling magma chambers.\n- **Key Locations:** Manikaran (Parvati Valley, Himachal Pradesh) and Puga Valley (Ladakh).\n- **Natural Hot Springs in Gujarat `(गुजरात के गर्म पानी के कुंड / ગુજરાતના ગરમ પાણીના કુંડ)`:**\n  - **Unhai `(उनाई / ઉનાઈ)`** (Navsari)\n  - **Tuwa `(टुवा / ટુવા)`** (Panchmahal)\n  - **Tulsi Shyam `(तुलसी श्याम / તુલસી શ્યામ)`** (Gir Somnath)\n  - **Lasundra `(लसुंद्रा / લસુંદ્રા)`** (Kheda)\n\n---\n\n### 5. Tidal Energy `(ज्वारीय ऊर्जा / ભરતી ઊર્જા)`\n- Oceanic tides forced through narrow coastal estuaries turn reversible hydraulic turbines during high and low tides.\n- **Promising Hubs in Gujarat:** The **Gulf of Kutch `(कच्छ की खाड़ी / કચ્છનો અખાત)`** and **Gulf of Khambhat `(खंभात की खाड़ी / ખંભાતનો અખાત)`** possess India's highest tidal power generation potential.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Map of India highlighting all 6 Strategic Nuclear Power Plants and Major Renewable Hubs.",
        "image_url": "assets/images/ss_ch12_nuclear_power_plants_map.jpg",
        "alt_text": "Map of India showing Kakrapar, Tarapur, Rawatbhata, Narora, Kalpakkam, Kaiga, and Charanka Solar Park."
    })
    
    blocks.append({
        "type": "theory",
        "content": "### 6. Atomic / Nuclear Energy `(परमाणु ऊर्जा / પરમાણુ ઊર્જા)`\n\nNuclear energy is generated by the controlled splitting (nuclear fission `(नाभिकीय विखंडन / ન્યુક્લિયર વિખંડન)`) of atoms of heavy radioactive minerals: **Uranium `(यूरेनियम / યુરેનિયમ)`** (mined at Jaduguda in Jharkhand) and **Thorium `(थोरियम / થોરિયમ)`** (obtained from Monazite beach sands of Kerala and Tamil Nadu).\n\n#### The 6 Must-Know Nuclear Power Stations in India (Board Exam Map Pointing):\n1. **Kakrapar `(काकरापार / કાકરાપાર)`:** Located in **Gujarat** (on the banks of river Tapi near Surat).\n2. **Tarapur `(तारापुर / તારાપુર)`:** Located in **Maharashtra** (India's first commercial nuclear power plant, established in 1969).\n3. **Rawatbhata `(रावतभाटा / રાવતભાટા)`:** Located in **Rajasthan** (near Kota on the Chambal river).\n4. **Narora `(नरौरा / નરોરા)`:** Located in **Uttar Pradesh** (on the Ganga river in Bulandshahr).\n5. **Kalpakkam / Kudankulam `(कलपक्कम / कुडनकुलम / કલપક્કમ અને કુડનકુલમ)`:** Located in **Tamil Nadu**.\n6. **Kaiga `(कैगा / કૈગા)`:** Located in **Karnataka** (on the Kali river).",
        "difficulty": "Advanced",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Nuclear Power Plants Memory Master Trick: 'K-T-R-N-K-K'**\n- **K**akrapar ⟶ **G**ujarat *(Kite Festival in Gujarat)*\n- **T**arapur ⟶ **M**aharashtra *(Tara belongs to Mumbai/MH)*\n- **R**awatbhata ⟶ **R**ajasthan *(R matches with R!)*\n- **N**arora ⟶ **U**ttar Pradesh *(North in UP)*\n- **K**aiga ⟶ **K**arnataka *(K matches with K!)*\n- **K**alpakkam / **K**udankulam ⟶ **T**amil Nadu",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "mcq",
        "question_text": "In which state of India is the Kakrapar Nuclear Power Station located?",
        "options": [
            "Rajasthan `(राजस्थान / રાજસ્થાન)`",
            "Maharashtra `(महाराष्ट्र / મહારાષ્ટ્ર)`",
            "Gujarat `(गुजरात / ગુજરાત)`",
            "Karnataka `(कर्नाटक / કર્ણાટક)`"
        ],
        "correct_answer": "Gujarat `(गुजरात / ગુજરાત)`",
        "explanation": "Kakrapar Nuclear Power Plant is located in Surat district of Gujarat along the Tapi river.",
        "distractor_rationale": "Rajasthan hosts Rawatbhata; Maharashtra hosts Tarapur; Karnataka hosts Kaiga.",
        "bloom": "Remember",
        "difficulty": "Beginner"
    })
    
    # =========================================================================
    # MODULE 7: CONSERVATION OF MINERALS & THE 4R STRATEGY
    # =========================================================================
    blocks.append({
        "type": "theory",
        "content": "### Conservation of Mineral & Energy Resources `(खनिजों का संरक्षण / ખનીજોનું સંરક્ષણ)`\n\nWhy is conservation an urgent national imperative?\n1. **Finite and Exhaustible `(सीमित और अनवीकरणीय / મર્યાદિત અને પુનઃઅપ્રાપ્ય)`:** Geological processes require millions of years to form mineral deposits, whereas human consumption takes only decades.\n2. **Increasing Extraction Costs:** As rich surface ores get depleted, deeper mining requires exorbitant capital and degrades ore quality.\n3. **Ecological Damage:** Unregulated open-cast mining causes air pollution, deforestation, acid mine drainage, and land degradation.\n\n### The 4R Strategic Blueprint for Sustainable Mineral Use:\n1. **Reduce `(खपत कम करना / વપરાશ ઘટાડવો)`:** Adopt high-efficiency smelting and cutting-edge mining technologies to minimize wastage at processing plants.\n2. **Reuse `(पुनः उपयोग / પુનઃઉપયોગ)`:** Extend the operational lifecycle of metallic machinery and structural components.\n3. **Recycle `(पुनर्चक्रण / પુનઃચક્રીકરણ)`:** Melt and recycle scrap metals (scrap iron, aluminium cans, copper wires, and lead-acid batteries).\n4. **Replace / Substitute `(वैकल्पिक स्रोत / વૈકલ્પિક સ્ત્રોતો અપનાવવા)`:** Replace fossil fuels with solar, wind, and green hydrogen; replace scarce heavy metals with aluminium alloys, engineered ceramics, and biodegradable polymers.",
        "difficulty": "Intermediate",
        "bloom": "Evaluate"
    })
    
    blocks.append({
        "type": "mind_map",
        "content": "```\n                           MINERALS & ENERGY RESOURCES\n                                       │\n         ┌─────────────────────────────┼─────────────────────────────┐\n         ▼                             ▼                             ▼\n   METALLIC MINERALS          NON-METALLIC MINERALS           ENERGY RESOURCES\n   ├─ Precious (Au, Ag, Pt)   ├─ Mica (Insulator)            ├─ Conventional\n   ├─ Light (Bauxite, Mg, Ti) ├─ Limestone (Cement)          │  ├─ Coal (A, B, L, P)\n   ├─ General (Fe, Cu, Pb)    ├─ Gypsum (POP)                │  ├─ Petroleum (Mumbai High, Ankleshwar)\n   └─ Alloys (Mn, Cr, W, V)   └─ Calcite, Silica             │  └─ Natural Gas (HVJ Pipeline)\n                                                             └─ Non-Conventional\n                                                                ├─ Solar (Charanka Park)\n                                                                ├─ Wind (Muppandal, Lamba)\n                                                                ├─ Biogas (Methan Village)\n                                                                ├─ Geothermal (Unhai, Tuwa)\n                                                                ├─ Tidal (Gulf of Kutch)\n                                                                └─ Nuclear (Kakrapar, Tarapur, etc.)\n```",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    # =========================================================================
    # MODULE 8: BOARD EXAM MASTERY & MAP-POINTING SUPER GUIDE
    # =========================================================================
    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM TOPPER'S MAP-POINTING GUIDE (Guaranteed 4 Marks):**\n\nEnsure you can pinpoint these exact locations on an outline map of India for the Board Examination:\n1. **Iron Ore Mine:** **Bailadila** (Chhattisgarh) or **Kudremukh** (Karnataka).\n2. **Coal Mine:** **Jharia** / **Bokaro** (Jharkhand) or **Raniganj** (West Bengal) or **Neyveli** (Lignite in Tamil Nadu).\n3. **Oilfield:** **Digboi** (Assam) or **Ankleshwar** (Gujarat) or **Mumbai High** (Arabian Sea).\n4. **Oil Refinery:** **Jamnagar** or **Koyali** (Gujarat).\n5. **Nuclear Power Station:** **Kakrapar** (Gujarat) or **Tarapur** (Maharashtra) or **Rawatbhata** (Rajasthan) or **Narora** (UP).\n6. **Solar Park:** **Charanka** (Patan, Gujarat).\n7. **Bauxite Region:** **Jamnagar/Junagadh** (Gujarat) or **Koraput** (Odisha).",
        "difficulty": "Advanced",
        "bloom": "Apply"
    })
    
    blocks.append({
        "type": "mcq",
        "question_text": "Which village in Gujarat is famous for having one of India's largest community-based rural biogas plants?",
        "options": [
            "Charanka `(चारणका / ચારણકા)`",
            "Methan `(मेथान / મેથાણ)`",
            "Lamba `(लांबा / લાંબા)`",
            "Ankleshwar `(अंकलेश्वर / અંકલેશ્વર)`"
        ],
        "correct_answer": "Methan `(मेथान / મેથાણ)`",
        "explanation": "Methan village in Sidhpur taluka of Patan district is celebrated as a national pioneer in collective community biogas generation.",
        "distractor_rationale": "Charanka is a solar park; Lamba is a wind farm; Ankleshwar is an oilfield.",
        "bloom": "Remember",
        "difficulty": "Intermediate"
    })
    
    blocks.append({
        "type": "summary",
        "content": "### Chapter 12 High-Yield Revision Summary:\n- Minerals are natural inorganic substances with fixed crystalline compositions.\n- Civilization progressed through Stone ⟶ Copper ⟶ Bronze ⟶ Iron ⟶ Atomic Ages.\n- Iron ore: Magnetite (>70% Fe), Hematite (50-60% Fe); Bailadila & Kudremukh are world-class mines.\n- 10 kg Manganese is needed per tonne of steel.\n- Brass = Cu + Zn; Bronze = Cu + Sn; Balaghat & Khetri lead copper production.\n- Mica is the supreme electrical insulator; India leads global sheet mica export.\n- Coal grades: Anthracite (>80%), Bituminous (70-80%), Lignite (40-55%), Peat (<40%).\n- Mumbai High (Sagar Samrat) & Ankleshwar are premier oilfields; Jamnagar houses the world's largest refinery.\n- Gujarat shines in green energy: Charanka (Solar), Lamba (Wind), Methan (Biogas), Unhai/Tuwa (Hot Springs), Kakrapar (Nuclear).\n- Mineral conservation demands the strict practice of the 4R framework: Reduce, Reuse, Recycle, Replace.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    # Save to GSEB destination
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_social_science_ch12.json"
    os.makedirs(os.path.dirname(gseb_path), exist_ok=True)
    with open(gseb_path, "w", encoding="utf-8") as f:
        json.dump(final_json, f, indent=2, ensure_ascii=False)
        
    # Save to NCERT destination
    ncert_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_social_science_ch12.json"
    final_json["metadata"]["id"] = "ncert_class10_social_science_ch12"
    with open(ncert_path, "w", encoding="utf-8") as f:
        json.dump(final_json, f, indent=2, ensure_ascii=False)
        
    print(f"Generated Supreme GSEB & NCERT Class 10 Social Science Ch 12 with {len(blocks)} blocks successfully!")

if __name__ == "__main__":
    generate_supreme_gseb_ss_ch12()
