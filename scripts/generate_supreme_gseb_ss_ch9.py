import json
import os

def generate_supreme_gseb_ss_ch9():
    chapter_id = "gseb_class10_social_science_ch9"
    title = "Chapter 9: Forest and Wildlife Resources (વન અને વન્યજીવ સંસાધન)"
    
    metadata = {
        "id": chapter_id,
        "title": title,
        "subtitle": "The Supreme Gold Standard Board Exam Mastery Guide",
        "subject": "Social Science",
        "grade": "10",
        "board": "GSEB/NCERT",
        "curriculum": ["GSEB", "CBSE", "Universal"],
        "language": "English/Hindi/Gujarati (Bilingual)",
        "difficulty": "Advanced",
        "estimated_minutes": 180,
        "version": "3.0.0-SUPREME-GOLD",
        "author": "Antigravity Supreme Intelligence",
        "reviewed_by": "Chief Academic Architect",
        "tags": [
            "social_science",
            "geography",
            "forests",
            "wildlife",
            "conservation",
            "national_parks",
            "sanctuaries",
            "biosphere_reserves",
            "project_tiger",
            "gseb_class10",
            "board_special",
            "bilingual"
        ],
        "learning_outcomes": [
            "Master the classification of forests based on administration, ownership, and management.",
            "Understand the root causes, ecological impacts, and remedial measures for deforestation.",
            "Explore the rich biodiversity of India and Gujarat along with endangered species.",
            "Analyze wildlife conservation projects including Project Tiger, Lion, Rhino, and Elephant.",
            "Clearly distinguish between Wildlife Sanctuaries, National Parks, and Biosphere Reserves."
        ],
        "ai_context": {
            "learning_goal": "Transform the student into a Board Exam topper in Social Science Chapter 9 by using the 8-Step Socratic Discovery Cycle, high-yield comparative tables, mnemonic tricks, and precise bilingual terms.",
            "common_misconceptions": [
                "Students often confuse Wildlife Sanctuaries with National Parks regarding human activities and grazing rights.",
                "Students confuse the Administrative classification (Reserved, Protected, Unclassified) with the Ownership classification (State, Community, Private).",
                "Students mistakenly assume Biosphere Reserves are smaller than National Parks, whereas Biosphere Reserves span over 5,000 sq km.",
                "Students forget that the Asiatic Lion is found in the wild ONLY in Gir, Gujarat in all of Asia."
            ],
            "tutor_hint": "Always remind students of the 3-step hierarchy: Sanctuary (least restricted) -> National Park (strictly protected) -> Biosphere Reserve (global ecosystem scale). Use local Gujarat examples like Velavadar, Gir, and Nal Sarovar to anchor memory."
        }
    }
    
    blocks = []
    
    # =========================================================================
    # MODULE 1: HOOK & INTRODUCTION TO FOREST RESOURCES
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "Imagine standing in the dense woods of the Western Ghats `(पश्चिमी घाट / પશ્ચિમ ઘાટ)` at dawn. The air is crisp, filled with the aroma of damp earth and the musical chorus of hornbills and cicadas. Trees are not just wood; they are the giant green lungs `(फेफड़े / ફેફસાં)` of mother Earth!\n\nFrom the medicine in your first-aid box to the textbook in your bag and the oxygen keeping you alive right this second—everything traces back to **Forest Resources `(वन संसाधन / વન સંસાધન)`**.\n\nYet, what will happen if this green canopy vanishes? Let's embark on an eye-opening journey through India's forests and wildlife!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "A multi-layered forest ecosystem acts as a carbon sink `(कार्बन अवशोषક / કાર્બન સંગ્રહક)`, regulates monsoon rain cycles, and prevents destructive floods.",
        "image_url": "assets/images/ss_ch9_forest_canopy_layers.jpg",
        "alt_text": "Diagram showing the forest layers from forest floor to emergent canopy"
    })
    
    blocks.append({
        "type": "theory",
        "title": "Significance of Forests & India's Forest Cover",
        "content": "Forests represent a renewable natural resource `(नवीकरणीय प्राकृतिक संसाधन / પુનઃપ્રાપ્ય કુદરતી સંસાધન)` that maintains ecological equilibrium `(पारिस्थितिक संतुलन / પારિસ્થિતિક સંતુલન)`.\n\n### 🌳 Key Functions of Forests:\n1. **Environmental Balance:** Absorb toxic carbon dioxide and release life-giving oxygen through photosynthesis.\n2. **Hydrological Cycle `(जल चक्र / જળ ચક્ર)`:** Aid cloud condensation and precipitation `(वर्षा / વરસાદ)`, reducing drought intensity.\n3. **Soil Conservation `(मृदा संरक्षण / જમીન સંરક્ષણ)`:** Tree root networks bind soil particles tightly, preventing topsoil erosion `(मृदा अपरदन / જમીનનું ધોવાણ)`.\n4. **Economic Wealth:** Supply industrial timber (Teak `(सागौन / સાગ)`, Sal `(शाल / સાલ)`), bamboo `(बांस / વાંસ)`, paper pulp, rubber, resins, lac, kattha, honey, and medicinal herbs (Amla, Harde, Baheda).\n\n### 📊 National Forest Statistics:\n- According to the **National Forest Policy of 1952 `(राष्ट्रीय वन नीति 1952 / રાષ્ટ્રીય વન નીતિ 1952)`**, forests should ideally cover **33%** of the total geographical area of a nation.\n- In India, forest cover is currently approximately **24.6%**.\n- In Gujarat, forest cover is around **10% to 11%**, highlighting the urgent need for intensive afforestation `(वनीकरण / વનીકરણ)`.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Teacher's Secret Insight:** Always remember the benchmark number **33%** for board exam MCQs! If asked in True/False or Fill-in-the-blanks, the National Forest Policy 1952 target is 33%, while India's actual coverage is ~24.6%."
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "According to the National Forest Policy (1952), what percentage of a nation's total land area should ideally be under forest cover?",
            "options": [
                "20%",
                "24.6%",
                "33%",
                "50%"
            ],
            "correct_answer": "33%",
            "explanation": "The National Forest Policy of 1952 stipulated that 33% of the total geographic area must be under forest cover to maintain ecological stability."
        },
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    # =========================================================================
    # MODULE 2: CLASSIFICATION OF FORESTS
    # =========================================================================
    blocks.append({
        "type": "theory",
        "title": "Classification of Forests (વહીવટી અને માલિકીની દ્રષ્ટિએ જંગલોનું વર્ગીકરણ)",
        "content": "In India, forests are classified under two primary frameworks:\n\n---\n\n### A. Classification According to Administration `(प्रशासन की दृष्टि से / વહીવટી દ્રષ્ટિએ)`:\n\n1. **Reserved Forests `(आरक्षित वन / આરક્ષિત જંગલો)`:**\n   - Under the direct and strict supervision of the government.\n   - **Complete Prohibition:** Felling of trees `(वृक्ष काटना / વૃક્ષ કાપવા)`, timber collection, and animal grazing `(पशु चराई / પશુ ચરાણ)` are strictly prohibited.\n\n2. **Protected Forests `(संरक्षित वन / સંરક્ષિત જંગલો)`:**\n   - Looked after by the Forest Administration `(वन प्रशासन / વન તંત્ર)`.\n   - Local inhabitants are permitted to gather fallen dry wood and graze cattle **without inflicting harm** upon living trees.\n\n3. **Unclassified Forests `(अवर्गीकृत वन / અવર્ગીકૃત જંગલો)`:**\n   - Remote, dense, or rugged terrain forests that are not yet officially categorized.\n   - There is no formal restriction on tree cutting or cattle grazing.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "title": "Classification According to Ownership and Management",
        "content": "### B. Classification According to Ownership & Control `(स्वामित्व और प्रबंधन की दृष्टि से / માલિકી, વહીવટ અને વ્યવસ્થાપનની દ્રષ્ટિએ)`:\n\n1. **State Forest `(राज्य वन / રાજ્ય માલિકીનું જંગલ)`:**\n   - Fully controlled and managed by Central or State Governments.\n   - The overwhelming majority of India's forest territory falls into this category.\n\n2. **Community Forest / Communal Forest `(सामुदायिक वन / સામુદાયિક જંગલ)`:**\n   - Administered and governed by local self-government institutions `(स्थानीय स्वशासन संस्थाएं / સ્થાનિક સ્વરાજ્યની સંસ્થાઓ)` such as Gram Panchayats, Municipalities `(नगरपालिका / નગરપાલિકા)`, and Municipal Corporations `(महानगरपालिका / મહાનગરપાલિકા)`.\n\n3. **Private Forest `(निजी वन / ખાનગી જંગલ)`:**\n   - Owned by private individuals or families.\n   - Found in states like Odisha, Meghalaya, Punjab, and Himachal Pradesh.\n   - Due to reckless exploitation, many private forests are today in a severely eroded or barren state `(क्षत-विक्षत अवस्था / ઉજ્જડ સ્થિતિ)`.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Forest Classification Tree: Administrative (Reserved, Protected, Unclassified) vs Ownership (State, Community, Private).",
        "image_url": "assets/images/ss_ch9_forest_classification_tree.jpg",
        "alt_text": "Hierarchy chart showing classification of Indian forests"
    })
    
    blocks.append({
        "type": "memory_trick",
        "content": "🧠 **Super Mnemonic to Ace Forest Types:**\n- **Administrative:** **R**escue **P**rotect **U**niverse ➔ **R**eserved, **P**rotected, **U**nclassified.\n- **Ownership:** **S**ave **C**ommon **P**lanet ➔ **S**tate, **C**ommunity, **P**rivate."
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "In which type of forest are tree felling, lumbering, and cattle grazing strictly forbidden by government decree?",
            "options": [
                "Protected Forests",
                "Unclassified Forests",
                "Reserved Forests",
                "Community Forests"
            ],
            "correct_answer": "Reserved Forests",
            "explanation": "Reserved Forests are under direct government administration where all felling, wood collection, and grazing activities are totally banned."
        },
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    # =========================================================================
    # MODULE 3: DEFORESTATION - CAUSES, IMPACTS & REMEDIES
    # =========================================================================
    blocks.append({
        "type": "theory",
        "title": "Deforestation (નિર્વનીકરણ / વન નષ્ટ થવું): Causes and Ecological Disasters",
        "content": "**Deforestation `(निर्वनीकरण / નિર્વનીકરણ)`** refers to the large-scale cutting down and destruction of forests on a permanent basis.\n\n### 🚜 Root Causes of Deforestation:\n1. **Human Ambition & Infrastructure:** Expansion of highways, railway networks, airports, and industrial townships `(औद्योगिक बस्तियां / ઔદ્યોગિક વસાહતો)`.\n2. **Multi-Purpose River Valley Projects `(बहुउद्देशीय नदी घाटी परियोजनाएं / બહુહેતુક યોજનાઓ)`:** Massive dam reservoirs submerge vast tracts of virgin forest.\n3. **Shifting Cultivation / Jhum Agriculture `(झूम खेती / સ્થળાંતરિત ખેતી)`:** Slashing and burning forests for short-term agriculture by tribal populations in North-Eastern India.\n4. **Surging Demand for Fuel & Timber:** Logging for paper mills, furniture, and residential fuel.\n5. **Wild Forest Fires `(दावानल / દાવાનળ)`:** Lightning strikes and human negligence ignite infernos that incinerate millions of flora and fauna.\n\n### ⚠️ Catastrophic Impacts `(विनाशकारी प्रभाव / વિનાશક અસરો)`:\n- **Soil Erosion & Desertification:** Without root anchors, fertile topsoil washes away during heavy rain, expanding arid wastelands.\n- **Global Warming & Climate Anomaly:** Rise in atmospheric $CO_2$ intensifies the greenhouse effect `(ग्रीनहाउस प्रभाव / ગ્રીનહાઉસ અસર)`, causing erratic monsoons.\n- **Plummeting Groundwater Levels:** Loss of spongy forest soil drastically reduces rainwater percolation `(जल पुनर्भरण / ભૂગર્ભ જળ રિચાર્જ)`.\n- **Human-Wildlife Conflicts:** Displaced wild carnivores enter rural villages and attack livestock and humans due to loss of natural habitat `(प्राकृतिक आवास / કુદરતી રહેઠાણ)`.",
        "difficulty": "Intermediate",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "The Destructive Cycle: Deforestation ➔ Topsoil Erosion ➔ Flash Floods ➔ Desertification ➔ Climate Crises.",
        "image_url": "assets/images/ss_ch9_deforestation_impact_cycle.jpg",
        "alt_text": "Flowchart showing chain reactions triggered by deforestation"
    })
    
    blocks.append({
        "type": "theory",
        "title": "Remedies for Forest Conservation (વન સંરક્ષણના ઉપાયો)",
        "content": "To reverse the alarming rate of forest depletion, comprehensive remedies must be implemented:\n\n1. **Developing Alternative Energy Resources:** Encourage Solar Cookers, Biogas `(बायोगैस / બાયોગેસ)`, and LPG in rural belts to replace fuel-wood `(जलाऊ लकड़ी / બળતણનું લાકડું)`.\n2. **Afforestation & Tree Plantation `(वृक्षारोपण / વૃક્ષારોપણ)`:** Mandate planting two saplings for every single tree cut down for unavoidable developmental reasons.\n3. **Social Forestry `(सामाजिक वानिकी / સામાજિક વનીકરણ)` & Agro-Forestry `(कृषि वानिकी / કૃષિ વનીકરણ)`:** Plant fast-growing fodder and timber trees along canal banks, railway lines, roadsides, and agricultural boundaries.\n4. **Strict Legal Enforcement:** Impose severe punitive fines and imprisonment against illegal logging and forest encroachers `(अवैध अतिक्रमणकारी / ગેરકાયદે દબાણકારો)`.\n5. **Specialized Forest Firefighting Squads:** Deploy aerial water bombers, drone surveillance, and dedicated fire-lines to extinguish forest fires `(दावानल / દાવાનળ)` rapidly.\n6. **Eco-Tourism Regulations:** Prevent reckless plastic pollution, loud vehicle horns, and littering in sensitive wildlife zones.\n7. **Mass Environmental Education:** Celebrate festivals like **Van Mahotsav `(वन महोत्सव)`** and integrate environmental stewardship into school curricula.",
        "difficulty": "Advanced",
        "bloom": "Apply"
    })
    
    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM TOPPER TIP (4 Marks Guaranteed Question):**\nWhen asked to explain *'Remedies for Forest Conservation' (વન સંરક્ષણના ઉપાયો)*, structure your answer into **6 crisp bullet points** with bold headings: \n1. Alternative Energy Resources\n2. Social Forestry & Agro-Forestry\n3. Strict Enforcement of Laws\n4. Forest Fire Prevention (दावानल शमन)\n5. Regulating Eco-tourism\n6. Mass Public Awareness (Van Mahotsav)."
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "Which of the following agricultural methods is a major cause of deforestation in hilly and tribal regions?",
            "options": [
                "Terrace farming",
                "Jhum (Shifting) cultivation",
                "Drip irrigation farming",
                "Intensive commercial farming"
            ],
            "correct_answer": "Jhum (Shifting) cultivation",
            "explanation": "Jhum (shifting) cultivation involves cutting down and burning forest plots for brief farming cycles, directly leading to forest degradation."
        },
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    # =========================================================================
    # MODULE 4: DIVERSE WILDLIFE OF INDIA & GUJARAT
    # =========================================================================
    blocks.append({
        "type": "theory",
        "title": "Wildlife Diversity in India (ભારતનું વૈવિધ્યસભર વન્યજીવન)",
        "content": "India boasts one of the richest biological treasure troves in the entire world, ranking among the top **12 mega-biodiversity countries** globally with over **81,000 recorded animal species**!\n\n### 🐾 Unique Wildlife Highlights Across India:\n- **Royal Bengal Tiger `(रॉयल बंगाल टाइगर / રોયલ બંગાળ વાઘ)`:** Found in West Bengal (Sundarbans), Madhya Pradesh, and Uttarakhand.\n- **Asiatic Lion `(एशियाई शेर / એશિયાટીક સિંહ)`:** Inhabits **only the Gir Forest of Gujarat** in the entire continent of Asia!\n- **One-Horned Indian Rhinoceros `(एक सींग वाला गैंडा / એક શિંગી ગેંડો)`:** Flourishes in the marshy wetlands `(दलदली क्षेत्र / કાદવ-કીચડવાળા વિસ્તારો)` of Kaziranga (Assam) and Sundarbans.\n- **Asian Elephants `(भारतीय हाथी / એશિયાઈ હાથી)`:** Roam the evergreen rainforests of Karnataka, Kerala, Tamil Nadu, and Assam.\n- **Indian Wild Ass - Ghudkhar `(घुड़खर / ઘુડખર)`:** Found exclusively in the **Little Rann of Kutch (કચ્છનું નાનું રણ)** in Gujarat.\n- **Snow Leopard `(हिम तेंदुआ / હિમ દીપડો)`:** Prowls the snow-capped Himalayan ranges above 3,000 meters.\n- **Great Indian Bustard - Ghorad `(घोराड़ / ઘોરાડ)`:** A majestic desert bird found in the arid grasslands of Gujarat and Rajasthan.\n- **Flamingos - Surkhab `(सुलखाब / સુરખાબ)`:** The official **State Bird of Gujarat**, nesting in the mud mounds of the Greater Rann of Kutch.\n- **Marine Biodiversity in Gujarat:** Dugong `(समुद्री गाय / દરિયાઈ ગાય)`, dolphins, whale sharks, and delicate coral reefs `(मूंगा चट्टानें / પરવાળાના ખડકો)` around Pirotan Island in the Gulf of Kutch.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Geographical Wildlife Map: Gir (Asiatic Lion), Kutch (Ghudkhar & Flamingos), Kaziranga (One-horned Rhino), Sundarbans (Royal Bengal Tiger), Himalayas (Snow Leopard).",
        "image_url": "assets/images/ss_ch9_india_wildlife_map.jpg",
        "alt_text": "Map of India highlighting major wildlife habitats and endemic animals"
    })
    
    blocks.append({
        "type": "teacher_tip",
        "content": "🦁 **Gujarat Board Special Fact:** \n- State Animal of Gujarat: **Asiatic Lion (એશિયાટિક સિંહ)**\n- State Bird of Gujarat: **Greater Flamingo / Surkhab (સુરખાબ)**\n- Endemic Habitat of Ghudkhar: **Little Rann of Kutch (કચ્છનું નાનું રણ)**"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "Which animal is found in its natural habitat in the wild ONLY in Gujarat's Gir forest in the entire Asian continent?",
            "options": [
                "Royal Bengal Tiger",
                "Asiatic Lion",
                "Snow Leopard",
                "One-horned Rhinoceros"
            ],
            "correct_answer": "Asiatic Lion",
            "explanation": "The Gir National Park and Wildlife Sanctuary in Gujarat is the only remaining natural habitat for the Asiatic Lion (Panthera leo persica) in Asia."
        },
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    # =========================================================================
    # MODULE 5: WILDLIFE EXTINCTION & THREATENED SPECIES
    # =========================================================================
    blocks.append({
        "type": "theory",
        "title": "Endangered Species & Reasons for Wildlife Destruction",
        "content": "Human greed and industrial intrusion have pushed hundreds of magnificent species to the brink of extinction `(विलुप्ति की कगार / લુપ્ત થવાના આરે)`.\n\n### 🛑 Extinct & Critically Endangered Species in India:\n- **Cheetah `(चीता / ચિત્તો)`:** Completely declared extinct in the wild in India since 1952 due to unrestrained trophy hunting `(शिकार / શિકાર)`.\n- **Vanishing Birds:** Pink-headed duck `(गुलाबी सिर वाली बत्तख / ગુલાબી ડોકવાળી બતક)`, Mountain Quail `(पहाड़ी बटेर / પહાડી બટેર)`, Forest Owlet, and Great Indian Bustard.\n- **Aquatic & Riverine Animals:** Gangetic River Dolphin `(गंगा डॉल्फिन / ગંગા ડોલ્ફિન)`, Gharial `(घड़ियाल / ઘડિયાળ મગર)`.\n\n### ⚡ Prime Factors for Wildlife Destruction:\n1. **Habitat Fragmentation `(आवास विखंडन / કુદરતી રહેઠાણોનો નાશ)`:** Clearing forests for reservoirs, mining `(खनन / ખનન)`, highways, and power grids breaks migration corridors.\n2. **Poaching and Illegal Wildlife Trade:** Slaughtering tigers and leopards for skins and bones, elephants for ivory tusks `(हाथीदांत / હાથીદાંત)`, rhinos for horns `(सींग / શિંગડાં)`, musk deer for musk `(कस्तूरी / કસ્તુરી)`, and pangolins for scales.\n3. **Toxic Chemical Contamination (The Vulture Crisis):** The veterinary painkiller drug **Diclofenac `(डाइक्लोफेनाक)`** administered to cattle caused acute kidney failure in vultures when they fed on animal carcasses, wiping out over **95%** of India's vulture population!\n4. **Forest Fires:** Destroys nests, eggs, and infant wildlife unable to flee the flames.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "The Human-Wildlife Conflict: Habitat Destruction ➔ Prey Depletion ➔ Carnivores entering human settlements ➔ Retaliatory killing.",
        "image_url": "assets/images/ss_ch9_human_wildlife_conflict.jpg",
        "alt_text": "Illustration showing habitat encroachment leading to human-animal conflicts"
    })
    
    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD HOT TOPIC: The Vulture Crisis (ગીધ લુપ્ત થવાનું કારણ):**\nVultures are nature's scavengers `(प्रकृति के सफाईकर्मी / કુદરતના સફાઈ કામદાર)` that consume dead animal carcasses. They plummeted into danger because of feeding on cattle treated with the anti-inflammatory drug **Diclofenac**."
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "Which animal was declared completely extinct in the wild in India in 1952?",
            "options": [
                "Snow Leopard",
                "Asiatic Cheetah",
                "One-horned Rhinoceros",
                "Ghudkhar (Wild Ass)"
            ],
            "correct_answer": "Asiatic Cheetah",
            "explanation": "The Asiatic Cheetah was declared officially extinct in India in 1952 due to excessive hunting and habitat destruction."
        },
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })
    
    # =========================================================================
    # MODULE 6: WILDLIFE CONSERVATION PROJECTS
    # =========================================================================
    blocks.append({
        "type": "theory",
        "title": "Special Wildlife Protection Projects (વન્યજીવ સંરક્ષણ યોજનાઓ)",
        "content": "To safeguard critically endangered flagship species, the Government of India has instituted dedicated, time-bound conservation initiatives:\n\n---\n\n### 1. Project Tiger `(बाघ परियोजना / વાઘ પરિયોજના - 1973)`:\n- Launched in **1973** when tiger numbers plummeted below 2,000.\n- Established strictly regulated tiger reserves across India with core, buffer, and transition zones.\n- Today, over **50+ Tiger Reserves** operate across India (e.g., Corbett, Ranthambore, Kanha, Sundarbans).\n\n### 2. Asiatic Lion Project `(सिंह परियोजना / સિંહ પરિયોજના - 1972)`:\n- Initiated in **1972** at Gir Forest, Gujarat, when the lion population had fallen drastically to around 180.\n- Strict anti-poaching squads, veterinary care, and relocation of Maldhari tribal settlements out of the core national park boosted the lion population past **670+** today!\n\n### 3. Project Elephant `(हाथी परियोजना / હાથી પરિયોજના - 1992)`:\n- Launched in **1992** to protect Asian Elephants, manage their migratory corridors `(हाथी गलियारे / હાથી ગલિયારા)`, and train domestic working elephants.\n\n### 4. Project Rhino `(गेंडा परियोजना / ગેંડા પરિયોજના)`:\n- Formulated as **Rhino Vision 2020** to save the single-horned Indian Rhino from poachers targeting their valuable horns for pseudo-medicines.\n\n### 5. Project Crocodile `(मगरमच्छ परियोजना / મગરમચ્છ પરિયોજના)`:\n- Launched in the 1970s to breed and rehabilitate freshwater Gharials and Marsh Crocodiles `(मगर / મગર)` in river sanctuaries like National Chambal Sanctuary.\n\n### 6. Project Vulture `(गिद्ध परियोजना / ગીધ પરિયોજના - 2004)`:\n- Commenced in **2004** with vulture conservation breeding centres (Pincore, Bhopal, Guwahati) and a nationwide ban on veterinary Diclofenac.\n\n### 7. Project Snow Leopard `(हिम तेंदुआ परियोजना / હિમ દીપડા પરિયોજના - 2000)`:\n- Launched in **2000** to protect high-altitude Himalayan ecosystems and generate eco-tourism awareness among local mountain communities.",
        "difficulty": "Advanced",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Timeline of India's Flagship Conservation Projects: Lion (1972) ➔ Tiger (1973) ➔ Crocodile (1975) ➔ Elephant (1992) ➔ Snow Leopard (2000) ➔ Vulture (2004).",
        "image_url": "assets/images/ss_ch9_wildlife_projects_timeline.jpg",
        "alt_text": "Timeline infographic showing years of launch for wildlife projects in India"
    })
    
    blocks.append({
        "type": "memory_trick",
        "content": "🧠 **Chronological Launch Order Memory Trick:**\n- **1972:** Lion (King of Jungle steps up first!)\n- **1973:** Tiger (Right after the Lion!)\n- **1992:** Elephant (The giant enters 20 years later!)\n- **2000:** Snow Leopard (New Millennium in snowy peaks!)\n- **2004:** Vulture (Saving the sky scavengers!)"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "In which year was 'Project Tiger' officially launched by the Government of India?",
            "options": [
                "1971",
                "1972",
                "1973",
                "1985"
            ],
            "correct_answer": "1973",
            "explanation": "Project Tiger was officially launched in 1973 to arrest the rapid decline of Royal Bengal Tigers in India."
        },
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    # =========================================================================
    # MODULE 7: SANCTUARIES, NATIONAL PARKS & BIOSPHERE RESERVES
    # =========================================================================
    blocks.append({
        "type": "theory",
        "title": "Sanctuary vs National Park vs Biosphere Reserve (સૌથી મહત્વનો તફાવત)",
        "content": "Protected areas are categorized into three tiers based on legal restrictions, administrative authority, and conservation scope:\n\n---\n\n| Parameter | Wildlife Sanctuary `(अभयारण्य / અભયારણ્ય)` | National Park `(राष्ट्रीय उद्यान / રાષ્ટ્રીય ઉદ્યાન)` | Biosphere Reserve `(जैव आरक्षित क्षेत्र / જૈવ આરક્ષિત ક્ષેત્ર)` |\n| :--- | :--- | :--- | :--- |\n| **1. Focus Area** | Focused on protection of a **single particular species** (e.g., Sloth bear, Bird). | Protects the **entire natural ecosystem** (flora, fauna, landscape, history). | Protects overall **physical and cultural diversity** including indigenous tribal lifestyles. |\n| **2. Human Activities & Grazing** | **Permitted within limits**; livestock grazing allowed with official permission. | **Strictly prohibited**; zero grazing, zero human settlement, no private land rights. | **Total ban** on all external human interference in the Core Zone; research permitted in Buffer. |\n| **3. Declaring Authority** | Declared by the **State Government**. | Established through coordination of **State and Central Governments**. | Declared according to **International UNESCO (MAB) Norms**. |\n| **4. Average Area** | Variable (Modest size). | Moderately large (hundreds of sq km). | Massive scale (**Exceeds 5,000 sq km**). |\n| **5. Prime Examples** | Nal Sarovar (Gujarat), Periyar (Kerala), Balaram Sanctuary (Gujarat). | Gir National Park, Velavadar Blackbuck National Park, Kaziranga, Corbett. | Nilgiri, Sundarbans, Great Nicobar, **Great Rann of Kutch (2008)**. |",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Concentric Zonation of a Biosphere Reserve: Core Zone (Zero Human Interference) ➔ Buffer Zone (Education & Research) ➔ Transition Zone (Sustainable Human Settlement).",
        "image_url": "assets/images/ss_ch9_biosphere_reserve_zones.jpg",
        "alt_text": "Zonation of Biosphere Reserve showing Core, Buffer and Transition zones"
    })
    
    blocks.append({
        "type": "theory",
        "title": "Four Major National Parks of Gujarat (ગુજરાતના 4 મુખ્ય રાષ્ટ્રીય ઉદ્યાનો)",
        "content": "Every GSEB Class 10 student must memorize Gujarat's **4 National Parks**:\n\n1. **Gir National Park `(ગીર રાષ્ટ્રીય ઉદ્યાન)`:**\n   - *District:* Junagadh / Gir Somnath\n   - *Key Wildlife:* Asiatic Lion, Leopard, Chital, Sambar, Four-horned Antelope.\n\n2. **Blackbuck National Park, Velavadar `(વેળાવદર કાળિયાર રાષ્ટ્રીય ઉદ્યાન)`:**\n   - *District:* Bhavnagar\n   - *Key Wildlife:* Blackbuck `(काला हिरण / કાળિયાર)`, Indian Wolf `(भेड़िया / વરુ)`, Lesser Florican `(खड़मोर / ખડમોર)`.\n\n3. **Vansda National Park `(વાંસદા રાષ્ટ્રીય ઉદ્યાન)`:**\n   - *District:* Navsari\n   - *Key Wildlife:* Leopard, Pangolin `(कीड़ीखाऊ / કીડીખાઉ)`, Giant Flying Squirrel `(उड़ती गिलहरी / ઉડતી ખિસકોલી)`.\n\n4. **Marine National Park `(દરિયાઈ રાષ્ટ્રીય ઉદ્યાન)`:**\n   - *District:* Gulf of Kutch / Jamnagar (Pirotan Island)\n   - *Key Wildlife:* Coral reefs `(परवाल / પરવાળા)`, Sea anemones, Dugong (Sea cow), Jellyfish, Octopus, Dolphins.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "teacher_tip",
        "content": "📍 **Map Question Alert for Board Exams:**\nOn the Outline Map of India, locate:\n1. **Gir National Park** ➔ Saurashtra, Gujarat\n2. **Velavadar National Park** ➔ Bhavnagar, Gujarat\n3. **Kaziranga National Park** ➔ Assam\n4. **Sundarbans Biosphere Reserve** ➔ West Bengal\n5. **Corbett National Park** ➔ Uttarakhand"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "Which National Park in Gujarat is internationally acclaimed for the conservation of Blackbucks (કાળિયાર) and Lesser Floricans (ખડમોર)?",
            "options": [
                "Gir National Park",
                "Vansda National Park",
                "Velavadar National Park",
                "Marine National Park"
            ],
            "correct_answer": "Velavadar National Park",
            "explanation": "Velavadar National Park in Bhavnagar district is globally renowned for its thriving population of Blackbucks (Kaliyar) and the endangered Lesser Florican bird."
        },
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    # =========================================================================
    # MODULE 8: BOARD EXAM MASTERY & REVISION SUITE
    # =========================================================================
    blocks.append({
        "type": "exam_tips",
        "content": "🏆 **BOARD EXAM TOPPER'S MASTER REVISION SHEET:**\n\n1. **Forest Administrative Classification:** Reserved (Zero access), Protected (Supervised fallen wood collection/grazing), Unclassified (No restriction).\n2. **Forest Ownership Classification:** State (Govt), Community (Panchayat/Nagar Palika), Private (Individual).\n3. **National Forest Target:** 33% (National Forest Policy 1952) | India: ~24.6% | Gujarat: ~10-11%.\n4. **Endemic Treasures of Gujarat:** Asiatic Lion (Gir), Ghudkhar (Little Rann of Kutch), Flamingo (Surkhab - State Bird).\n5. **Extinct in India:** Asiatic Cheetah (1952).\n6. **Vulture Mortality Cause:** Diclofenac drug in livestock.\n7. **Key Project Launch Years:** Asiatic Lion (1972), Tiger (1973), Elephant (1992), Snow Leopard (2000), Vulture (2004).\n8. **Gujarat Biosphere Reserve:** Great Rann of Kutch (Declared in 2008, area > 12,400 sq km)."
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "In which year was the Rann of Kutch declared as a Biosphere Reserve according to international norms?",
            "options": [
                "1972",
                "1992",
                "2004",
                "2008"
            ],
            "correct_answer": "2008",
            "explanation": "The Great Rann of Kutch in Gujarat was officially declared a Biosphere Reserve in 2008 for its distinct desert and wetland biodiversity."
        },
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "reflection",
        "content": "🌱 **Citizen's Green Pledge:**\nForests and wildlife are not inherited from our ancestors; they are borrowed from our future generations. What 2 concrete actions will you take this week to conserve resources?\n1. Say NO to single-use plastics that choke rivers and forests.\n2. Plant and adopt a indigenous native tree sapling (Neem, Peepal, Banyan) in your neighbourhood!"
    })
    
    # Assemble Final JSON Payload
    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    # Define Target Output Paths
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    chapters_dir = os.path.join(base_dir, "app_core", "chapters")
    os.makedirs(chapters_dir, exist_ok=True)
    
    gseb_output_path = os.path.join(chapters_dir, "gseb_class10_social_science_ch9.json")
    ncert_output_path = os.path.join(chapters_dir, "ncert_class10_social_science_ch9.json")
    
    # Save GSEB chapter
    final_json["metadata"]["id"] = "gseb_class10_social_science_ch9"
    with open(gseb_output_path, "w", encoding="utf-8") as f:
        json.dump(final_json, f, indent=2, ensure_ascii=False)
        
    # Save NCERT chapter
    final_json["metadata"]["id"] = "ncert_class10_social_science_ch9"
    with open(ncert_output_path, "w", encoding="utf-8") as f:
        json.dump(final_json, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully generated Supreme GSEB/NCERT Social Science Chapter 9:")
    print(f"  -> {gseb_output_path}")
    print(f"  -> {ncert_output_path}")

if __name__ == "__main__":
    generate_supreme_gseb_ss_ch9()
