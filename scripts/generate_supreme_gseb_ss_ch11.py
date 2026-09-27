import json
import os

def generate_supreme_gseb_ss_ch11():
    chapter_id = "gseb_class10_social_science_ch11"
    title = "Chapter 11: India: Water Resources (ભારત : જળ સંસાધન)"
    
    metadata = {
        "id": chapter_id,
        "title": title,
        "subtitle": "The Supreme Board Exam Mastery & Conceptual Geography Guide",
        "subject": "Social Science",
        "grade": "10",
        "board": "GSEB / NCERT",
        "curriculum": ["GSEB", "NCERT", "CBSE"],
        "language": "English/Hindi/Gujarati (Bilingual)",
        "difficulty": "Advanced",
        "estimated_minutes": 180,
        "version": "3.0.0-SUPREME-SS",
        "author": "Antigravity Supreme Intelligence",
        "reviewed_by": "Chief Academic Architect",
        "tags": [
            "social_science",
            "geography",
            "water_resources",
            "irrigation",
            "multipurpose_projects",
            "rainwater_harvesting",
            "watershed_management",
            "gseb_class10",
            "board_special",
            "bilingual"
        ],
        "learning_outcomes": [
            "Identify the three primary sources of water in India: Rainwater, Surface water, and Groundwater.",
            "Understand the historical evolution and major mediums of irrigation (Wells/Tube-wells, Canals, Tanks).",
            "Analyze major Multi-Purpose River Valley Projects across India, their rivers, and beneficiary states.",
            "Examine the root causes of India's escalating water crisis, declining water tables, and interstate disputes.",
            "Master practical strategies for water conservation including Watershed Management, Rainwater Harvesting, and Micro-Irrigation.",
            "Score 100% on GSEB/NCERT Board objective questions, map pointing, and long analytical 4-mark questions."
        ],
        "ai_context": {
            "learning_goal": "Transform the student into a geography topper in Water Resources through the 8-Step Socratic Learning Cycle. Use detailed explanations, diagrams, comparative tables, and inline bilingual translations with backticks for the Smart Translation Filter.",
            "common_misconceptions": [
                "Students think water is an unlimited resource because Earth is 71% water, forgetting that less than 1% is usable freshwater.",
                "Students confuse the locations and rivers of major multi-purpose projects (e.g., confusing Hirakud on Mahanadi with Nagarjuna Sagar on Krishna).",
                "Students often mix up the primary mediums of irrigation in North India (Wells/Canals) with South India (Tanks/Ponds).",
                "Students overlook the importance of community participation in Watershed Management."
            ],
            "tutor_hint": "If a student struggles to memorize multi-purpose projects, use the mnemonic pairing tricks (e.g., 'Maha-Hira' = Mahanadi-Hirakud; 'Krishna-Arjuna' = Krishna-Nagarjuna Sagar; 'Narmada-Sardar' = Narmada-Sardar Sarovar). Emphasize that Irrigation consumes ~84% of India's total water."
        }
    }
    
    blocks = []
    
    # ==========================================
    # MODULE 1: INTRODUCTION & HOOK (THE BLUE PLANET PARADOX)
    # ==========================================
    blocks.append({
        "type": "hook",
        "content": "Look at a globe or a satellite photograph of Earth. What color dominates? Blue! About **71% of Earth's surface** is covered with water. Yet, every single summer in India, why do millions of people queue up for hours behind water tankers `(पानी के टैंकर / પાણીના ટેન્કર)`? Why are rivers drying up, borewells failing, and farmers protesting for irrigation water?\n\nBecause **97.5%** of Earth's water is saline ocean water `(खारा समुद्री जल / ખારું સમુદ્રી પાણી)`! Out of the remaining tiny 2.5% of freshwater `(मीठा पानी / મીઠું પાણી)`, nearly 70% is locked inside polar ice caps and glaciers. That leaves less than **1% of accessible freshwater** for 8 billion humans, billions of animals, industries, and all agriculture!\n\nIn India, water is not just a natural resource `(प्राकृतिक संसाधन / કુદરતી સંસાધન)`; it is the very foundation of food security, industrial progress, and human existence—*\"Jal hi Jeevan hai\" `(जल ही जीवन है / જળ એ જ જીવન છે)`*! Let us master every concept of **India's Water Resources** for board exam brilliance!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Visualizing Global Water Distribution vs Usable Freshwater. 97.5% Saline Oceans vs 2.5% Freshwater (with glaciers holding 68.7%, groundwater holding 30.1%, and surface lakes/rivers holding only 1.2%).",
        "image_url": "assets/images/water_resources_global_distribution.jpg",
        "alt_text": "Pie chart illustrating global water distribution highlighting less than 1% accessible fresh water."
    })
    
    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Teacher's Secret:** In geography, always remember that water is a **finite resource `(सीमित संसाधन / મર્યાદિત સંસાધન)`**. Unlike synthetic products, no factory on Earth can manufacture water. Its supply is determined strictly by the natural **Hydrological Cycle `(जल चक्र / જળચક્ર)`**.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "What percentage of the Earth's total water is available as accessible, usable freshwater for humans and terrestrial ecosystems?",
            "options": [
                "About 71%",
                "About 25%",
                "Less than 1%",
                "About 10%"
            ],
            "correct_answer": "Less than 1%",
            "explanation": "While water covers ~71% of Earth, 97.5% is salty ocean water. Of the remaining 2.5% freshwater, nearly 70% is frozen in glaciers, leaving less than 1% readily accessible for human use."
        },
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    # ==========================================
    # MODULE 2: SOURCES OF WATER RESOURCES IN INDIA
    # ==========================================
    blocks.append({
        "type": "theory",
        "title": "Three Main Sources of Water in India (ભારતમાં જળ સંસાધનના સ્ત્રોતો)",
        "content": "In India, water resources are classified into **three fundamental sources `(ત્રણ મુખ્ય સ્ત્રોતો / तीन मुख्य स्रोत)`** based on their origin and physical location:\n\n1. **Rainwater / Atmospheric Water `(વૃષ્ટિય જળ / वृष्टि जल)`:**\n   - Rain `(વરસાદ / वर्षा)` is the **primary source `(મૂળભૂત સ્ત્રોત / प्राथमिक स्रोत)`** of all freshwater on Earth.\n   - All surface water and groundwater are recharged exclusively by precipitation `(વૃષ્ટિપાત / वर्षण)` received mainly during the Southwest Monsoon `(નૈઋત્યનું ચોમાસું / दक्षिण-पश्चिम मानसून)`.\n\n2. **Surface Water `(પૃષ્ઠીય જળ / पृष्ठीय जल)`:**\n   - Water found on the surface of the land in rivers `(નદીઓ / नदियां)`, lakes `(સરોવરો / झीलें)`, ponds `(તળાવો / तालाब)`, streams `(ઝરણાં / झरने)`, and wetlands.\n   - Rivers constitute the single largest carrier and source of surface water in India.\n\n3. **Groundwater / Sub-surface Water `(ભૂમિગત જળ / भूमिगत जल)`:**\n   - Water that soaks through the soil and permeable rock layers `(જમીન અને ખડકોમાંથી શોષાઈને / रिसकर)` and accumulates in underground reservoirs called **aquifers `(જળભંડારો / जलभृत)`**.\n   - **Maximum utilization:** The northern alluvial plains `(ઉત્તરના કાંપના મેદાનો / उत्तर के जलोढ़ मैदान)` account for **42% of India's total groundwater** due to loose, porous alluvial soil.\n   - In Southern India, hard crystalline rocks `(સખત પથરાળ ખડકો / कठोर चट्टानें)` reduce infiltration, resulting in comparatively lower groundwater reserves.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Cross-section diagram of groundwater aquifer showing infiltration, water table (જળસ્તર), impermeable bedrock, and tube-well extraction.",
        "image_url": "assets/images/groundwater_aquifer_cross_section.jpg",
        "alt_text": "Diagram showing the infiltration of rainwater into the ground creating the water table and subterranean aquifer."
    })
    
    blocks.append({
        "type": "memory_trick",
        "content": "**Mnemonic to Remember the 3 Water Sources:**\nThink of the acronym **\"3S\"** of Water:\n- **S**ky Water = Rainwater / Atmospheric Water `(વૃષ્ટિય જળ)`\n- **S**urface Water = Rivers, Lakes, and Ponds `(પૃષ્ઠીય જળ)`\n- **S**ub-surface Water = Underground Groundwater `(ભૂમિગત જળ)`",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "Which geographical region in India possesses and utilizes the highest volume of groundwater reserves?",
            "options": [
                "The Thar Desert region of Rajasthan",
                "The Northern Alluvial Plains",
                "The Deccan Peninsular Plateau",
                "The Western Ghats coastal belt"
            ],
            "correct_answer": "The Northern Alluvial Plains",
            "explanation": "The northern river plains formed by the Indus, Ganga, and Brahmaputra have highly porous, deep alluvial soil which facilitates maximum rainwater percolation, holding about 42% of India's total groundwater reserves."
        },
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    # ==========================================
    # MODULE 3: WATER UTILIZATION & IRRIGATION IN INDIA
    # ==========================================
    blocks.append({
        "type": "theory",
        "title": "Sectoral Water Utilization & The Heavy Demand of Agriculture",
        "content": "Water in India is utilized across three major sectors:\n\n1. **Agriculture & Irrigation `(સિંચાઈ / सिंचाई)` — ~84% of Total Consumption:**\n   - India is primarily an agrarian country `(કૃષિપ્રધાન દેશ / कृषि प्रधान देश)`.\n   - Monsoon rainfall in India is highly **uncertain `(અનિશ્ચિત / अनिश्चित)`**, **irregular `(અનિયમિત / अनियमित)`**, and **unevenly distributed `(અસમાન વિતરણ / असमान)`** across regions and seasons.\n   - Certain commercial and staple crops consume gigantic volumes of water:\n     • **1 kg of Wheat `(ઘઉં / गेहूं)`** requires ~1,500 litres of water!\n     • **1 kg of Paddy / Rice `(ડાંગર / धान)`** requires ~3,000 to 5,000 litres of standing water!\n     • **Sugarcane `(શેરડી / गन्ना)`** and **Jute `(શણ / पटसन)`** require round-the-year intensive irrigation.\n\n2. **Domestic & Municipal Needs `(ઘરેલું વપરાશ / घरेलू उपयोग)` — ~9%:**\n   - Drinking `(પીવાનું પાણી)`, cooking, sanitation, washing, and urban municipal supply.\n\n3. **Industrial & Power Generation `(ઔદ્યોગિક અને થર્મલ પાવર વપરાશ)` — ~7%:**\n   - Cooling in thermal power plants `(થર્મલ પાવર પ્લાન્ટ્સ)`, chemical processing, textile manufacturing, and paper industries.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "title": "Historical Irrigation Heritage of India (સિંચાઈનો ઐતિહાસિક વારસો)",
        "content": "Irrigation is not a modern invention in India; it has been practiced since antiquity:\n\n• **Grand Anicut / Kallanai `(કલ્લનઈ / કલ્લનાઇ ડેમ / ग्रैंड अनिकट)`:**\n  - Constructed in the **2nd Century AD** across the **Kaveri River `(કાવેરી નદી)`** in Tamil Nadu by the famous **Chola King Karikala `(ચોલ રાજા કરિકાલ)`**.\n  - It is one of the oldest operational water-diversion and dam structures in the world!\n\n• **Western Yamuna Canal `(પશ્ચિમી યમુના નહેર / पश्चिमी यमुना नहर)`:**\n  - Built in **1873** in northern India (Haryana/UP) to divert Yamuna river waters for widespread agriculture.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "theory",
        "title": "Three Mediums of Irrigation in India (સિંચાઈના ત્રણ માધ્યમો)",
        "content": "There are **three primary mediums of irrigation `(સિંચાઈના ત્રણ મુખ્ય માધ્યમો / सिंचाई के तीन माध्यम)`** in India:\n\n1. **Wells and Tube-wells `(કૂવા અને ટ્યુબવેલ / कुएं और ट्यूबवेल)` — Rank 1:**\n   - Dominant medium of irrigation in India (~55-60% of total irrigated area).\n   - Widely prevalent in the soft alluvial soils of the **Northern Plains** (Punjab, Haryana, Uttar Pradesh, Bihar, Gujarat, and Rajasthan).\n\n2. **Canals `(નહેરો / નહેર સિંચાઈ / नहरें)` — Rank 2:**\n   - Second most important medium of irrigation.\n   - Extensive canal networks exist in the perennial river basins of Northern India (Sutlej, Ganga, Yamuna) and the fertile **deltaic regions `(મુખત્રિકોણ પ્રદેશો / डेल्टाई क्षेत्र)`** of eastern coastal rivers (Mahanadi, Godavari, Krishna, Kaveri).\n\n3. **Ponds / Tanks `(તળાવો / તળાવ સિંચાઈ / तालाब)` — Rank 3:**\n   - Third medium of irrigation.\n   - Highly prominent in the **Peninsular Plateau `(દક્ષિણનો દ્વીપકલ્પીય ઉચ્ચપ્રદેશ / प्रायद्वीपीय पठार)`** and Eastern India (Tamil Nadu, Andhra Pradesh, Karnataka, Odisha).\n   - *Geographical Reason:* The hard, non-porous crystalline and metamorphic rocks prevent water from percolating deep down, making it impossible to dig tube-wells cheaply. Natural rocky depressions easily hold surface runoff, forming ideal storage tanks/ponds.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Teacher's Secret (GSEB Board Reasoning Question):**\n**Q: Why is tank irrigation predominant in Southern India whereas tube-well irrigation is predominant in Northern India?**\n**A:** South India has hard, impermeable rocky terrain where digging deep wells is difficult and costly, but natural rock depressions easily store rain as tanks. In contrast, North India has soft, porous, deep alluvial soil with high groundwater tables fed by perennial snow-fed rivers, making tube-well drilling highly viable.",
        "difficulty": "Intermediate",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "Which historical irrigation structure was constructed in the 2nd Century AD across the Kaveri River by the Chola King Karikala?",
            "options": [
                "Bhakra Dam",
                "Grand Anicut (Kallanai)",
                "Western Yamuna Canal",
                "Sardar Sarovar Dam"
            ],
            "correct_answer": "Grand Anicut (Kallanai)",
            "explanation": "The Grand Anicut (Kallanai) was built across the Kaveri river in Tamil Nadu in the 2nd century AD by the Chola king Karikala and remains one of the world's oldest functional water regulators."
        },
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })
    
    # ==========================================
    # MODULE 4: MULTI-PURPOSE RIVER VALLEY PROJECTS
    # ==========================================
    blocks.append({
        "type": "theory",
        "title": "What are Multi-Purpose Projects? (બહુહેતુક યોજનાઓ એટલે શું?)",
        "content": "A **Multi-Purpose River Valley Project `(બહુહેતુક નદી ખીણ યોજના / बहुउद्देशीय नदी घाटी परियोजना)`** is a grand engineering project involving dams, barrages, and canals constructed on rivers to solve multiple water-related problems and serve numerous developmental goals simultaneously.\n\nIndia's first Prime Minister, **Pandit Jawaharlal Nehru**, famously called these multi-purpose river valley projects the **\"Temples of Modern India\" `(આધુનિક ભારતના મંદિરો / आधुनिक भारत के मंदिर)`** because they integrate agriculture, industry, electricity, and rural economic growth.\n\n**Major Objectives / Benefits `(મુખ્ય ઉદ્દેશો / મુખ્ય ફાયદાઓ)`:**\n1. **Flood Control `(પૂર નિયંત્રણ / बाढ़ नियंत्रण)`:** Preventing devastating seasonal river floods.\n2. **Irrigation `(સિંચાઈની સુવિધા / सिंचाई)`:** Supplying regulated water to vast drought-prone agricultural tracts.\n3. **Hydroelectricity `(જળવિદ્યુત ઉત્પાદન / जलविद्युत)`:** Generating clean, renewable electric power for industries and homes.\n4. **Drinking & Municipal Supply `(પીવાનું શુદ્ધ પાણી / पेयजल आपूर्ति)`:** Providing potable water to parched cities and remote villages.\n5. **Soil Erosion Prevention `(જમીનનું ધોવાણ અટકાવવું / मृदा अपरदन की रोकथाम)`:** Regulating river velocity and stabilizing riverbanks.\n6. **Inland Waterways `(આંતરિક જળપરિવહન / अंतर्देशीय जलमार्ग)`:** Facilitating navigation and freight transit along reservoirs and deep canals.\n7. **Pisciculture / Fish Breeding `(મત્સ્યઉદ્યોગ / મત્સ્યપાલન / मत्स्य पालन)`:** Developing commercial inland fisheries.\n8. **Afforestation & Ecology `(વન્યીકરણ / વનીકરણ / वनीकरण)`:** Promoting green belts and wildlife habitats.\n9. **Tourism & Recreation `(પ્રવાસન અને મનોરંજન / पर्यटन विकास)`:** Creating scenic spots, national parks, and water sports centres.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Map of India highlighting the location of major Multi-Purpose Projects: Bhakra Nangal (Sutlej), Damodar Valley (Damodar), Hirakud (Mahanadi), Sardar Sarovar (Narmada), Nagarjuna Sagar (Krishna), and Tungabhadra.",
        "image_url": "assets/images/india_multipurpose_projects_map.jpg",
        "alt_text": "India map showing major river valley projects across various states and rivers."
    })
    
    blocks.append({
        "type": "theory",
        "title": "Master Table: India's Major Multi-Purpose Projects (GSEB Gold Chart)",
        "content": "Here is the master list of all major Multi-Purpose River Valley Projects in India that appear consistently in GSEB Board MCQs, 1-mark matchings, and map-work:\n\n| No. | Multi-Purpose Project `(યોજના)` | River `(નદી)` | Benefited States `(લાભાન્વિત રાજ્યો)` |\n|:---|:---|:---|:---|\n| 1 | **Bhakra-Nagal `(ભાખરા-નાંગલ)`** | Sutlej `(સતલુજ)` | Punjab, Haryana, Rajasthan |\n| 2 | **Damodar Valley `(દામોદર ખીણ)`** | Damodar `(દામોદર)` | Jharkhand, West Bengal |\n| 3 | **Kosi `(કોસી યોજના)`** | Kosi `(કોસી)` | Bihar (Joint venture with Nepal) |\n| 4 | **Hirakud `(હીરાકુડ યોજના)`** | Mahanadi `(મહાનદી)` | Odisha (Longest earthen dam ~25.8 km) |\n| 5 | **Nagarjuna Sagar `(નાગાર્જુન સાગર)`** | Krishna `(કૃષ્ણા)` | Andhra Pradesh, Telangana |\n| 6 | **Tungabhadra `(તુંગભદ્રા યોજના)`** | Tungabhadra `(તુંગભદ્રા)` | Karnataka, Andhra Pradesh |\n| 7 | **Sardar Sarovar `(સરદાર સરોવર)`** | Narmada `(નર્મદા)` | Gujarat, Madhya Pradesh, Rajasthan, Maharashtra |\n| 8 | **Ukai & Kakrapar `(ઉકાઈ અને કાકરાપાર)`** | Tapi `(તાપી)` | Gujarat |\n| 9 | **Kadana & Wanakbori `(કડાણા અને વણાકબોરી)`** | Mahi `(મહી)` | Gujarat |\n| 10 | **Dharoi `(ધરોઈ યોજના)`** | Sabarmati `(સાબરમતી)` | Gujarat |\n| 11 | **Chambal Valley `(ચંબલ ખીણ)`** | Chambal `(ચંબલ)` | Madhya Pradesh, Rajasthan |\n| 12 | **Rihand `(રિહંદ યોજના)`** | Rihand `(રિહંદ)` | Uttar Pradesh (Govind Ballabh Pant Sagar) |\n| 13 | **Krishnarajasagar / KRS `(કૃષ્ણરાજસાગર)`** | Kaveri `(કાવેરી)` | Karnataka, Tamil Nadu |",
        "difficulty": "Advanced",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "memory_trick",
        "content": "**Super Mnemonic Tricks to Match Rivers and Projects:**\n1. **Krishna + Arjuna = Nagarjuna Sagar** ⟶ Lord Krishna guided Arjuna (River **Krishna** = **Nagarjuna Sagar** dam).\n2. **Maha + Hira = Mahanadi + Hirakud** ⟶ Diamond (Hira) is Great (Maha) (River **Mahanadi** = **Hirakud** dam).\n3. **Narmada + Sardar = Sardar Sarovar** ⟶ Iron Man of India Sardar Patel on the Lifeline River (**Narmada** = **Sardar Sarovar**).\n4. **Sutlej + Bhakra** ⟶ Sutlej's high flow runs the massive **Bhakra Nangal**.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "Which of the following multi-purpose projects is built on the Mahanadi River in Odisha and is known as one of the longest earthen dams in the world?",
            "options": [
                "Bhakra Nangal Project",
                "Damodar Valley Project",
                "Hirakud Project",
                "Tungabhadra Project"
            ],
            "correct_answer": "Hirakud Project",
            "explanation": "The Hirakud Project is constructed across the Mahanadi river in Odisha. It is one of the world's longest earthen dams, serving flood control, irrigation, and power generation."
        },
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })
    
    # ==========================================
    # MODULE 5: REGIONAL DISPARITY IN IRRIGATION DISTRIBUTION
    # ==========================================
    blocks.append({
        "type": "theory",
        "title": "Distribution of Irrigation Area & Inter-State Disparity (સિંચાઈ ક્ષેત્રનું વિતરણ)",
        "content": "There is a massive **regional disparity `(પ્રાદેશિક અસમાનતા / क्षेत्रीय असमानता)`** in the percentage of irrigated agricultural land across Indian states:\n\n• **Vast Disparity in Sown vs Irrigated Area:**\n  - In India, only about **38% to 40% of the total sown agricultural area `(વાવેતર વિસ્તાર / शुद्ध बोया गया क्षेत्र)`** is equipped with artificial irrigation. The remaining 60%+ farming depends entirely on erratic monsoon rains!\n\n• **States with Extremely High Irrigation Coverage:**\n  - **Punjab `(પંજાબ)`:** About **90.8%** of the net cultivated area is irrigated!\n  - **Haryana `(હરિયાણા)`:** Over **80%** of the net cultivated area is irrigated.\n  - *Reason:* Rich perennial snow-fed rivers, massive canal networks (Bhakra-Nangal, Western Yamuna), flat alluvial plains, and widespread adoption of diesel/electric tube-wells during the Green Revolution.\n\n• **States with Extremely Low Irrigation Coverage:**\n  - **Mizoram `(મિઝોરમ)`:** Only **7.3%** of the total cultivated area has irrigation facilities (the lowest in India)!\n  - Other northeastern hilly states like Nagaland, Manipur, and Meghalaya also have very low irrigation percentages due to rugged mountainous terrain `(પર્વતીય ભૂપૃષ્ઠ)` and dependence on shifting/jhum cultivation.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "Which Indian state has the highest percentage (~90.8%) of its net sown area under irrigation?",
            "options": [
                "Gujarat",
                "Mizoram",
                "Punjab",
                "Assam"
            ],
            "correct_answer": "Punjab",
            "explanation": "Punjab has the highest irrigation intensity in India (~90.8% of net sown area) owing to its dense network of canals and extensive tube-well infrastructure."
        },
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    # ==========================================
    # MODULE 6: THE LOOMING WATER CRISIS IN INDIA
    # ==========================================
    blocks.append({
        "type": "theory",
        "title": "Causes and Severe Dimensions of India's Water Crisis (જળ સંકટ)",
        "content": "India supports **18% of the world's population** but possesses only **4% of the world's freshwater resources**. This extreme mismatch has triggered a catastrophic **Water Crisis `(જળ સંકટ / जल संकट)`** across the country.\n\n**Key Factors Behind the Water Crisis `(જળ સંકટના મુખ્ય કારણો)`:**\n\n1. **Population Explosion `(વસ્તી વિસ્ફોટ / जनसंख्या विस्फोट)`:**\n   - Skyrocketing population requires exponential increases in food grains, vegetables, and daily municipal water supply.\n\n2. **Rapid Urbanization & Changing Lifestyles `(ઝડપી શહેરીકરણ / तीव्र शहरीकरण)`:**\n   - Modern urban lifestyle uses 5 to 10 times more water per capita (showers, flush toilets, washing machines, car washing, swimming pools).\n\n3. **Intensive Agriculture & Cash Crops `(રોકડિયા પાકોનું વાવેતર / नकदी फसलें)`:**\n   - Transitioning from drought-resistant traditional crops (Millets/Jowar/Bajra) to water-guzzling cash crops (Paddy, Sugarcane, Cotton) in semi-arid zones.\n\n4. **Over-Extraction of Groundwater `(ભૂમિગત જળનું અતિશોષણ)`:**\n   - Millions of private tube-wells pump out water 24/7 without recharging. This has resulted in a **sharp decline in the water table `(ભૂગર્ભ જળસ્તર સતત ઊંડું જવું)`**, drying up shallow wells and causing land subsidence in some regions.\n\n5. **Water Pollution `(જળ પ્રદૂષણ / जल प्रदूषण)`:**\n   - Discharge of untreated toxic industrial effluents `(ઝેરી ઔદ્યોગિક કચરો)` and raw urban domestic sewage `(ગટરનું ગંદું પાણી)` into holy rivers like Ganga, Yamuna, Sabarmati, and Damodar, turning them into open toxic drains.\n   - Excessive usage of chemical fertilizers `(રાસાયણિક ખાતરો)` and insecticides `(જંતુનાશક દવાઓ)` in agriculture that leach deep into underground aquifers, causing deadly **Nitrate, Arsenic, and Fluoride contamination**.\n\n6. **Salinity Ingress in Coastal Regions `(દરિયાઈ ખારાશનું પ્રવેશવું)`:**\n   - In coastal areas of Gujarat (Saurashtra) and Tamil Nadu, excessive extraction of fresh groundwater has caused saline sea water to seep inland into freshwater aquifers, turning drinking water undrinkable.\n\n7. **Inter-State River Water Disputes `(આંતરરાજ્ય જળ વિવાદો / अंतर्राज्यीय जल विवाद)`:**\n   - As water becomes scarce, neighboring states battle fiercely over river water sharing:\n     • **Cauvery Water Dispute `(કાવેરી જળ વિવાદ)`:** Karnataka vs Tamil Nadu vs Kerala vs Puducherry.\n     • **Krishna Water Dispute `(કૃષ્ણા જળ વિવાદ)`:** Maharashtra vs Karnataka vs Andhra Pradesh/Telangana.\n     • **Narmada Water Dispute `(નર્મદા જળ વિવાદ)`:** Gujarat vs Madhya Pradesh vs Maharashtra vs Rajasthan.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "real_world_example",
        "content": "🌆 **Real-World Case Study (The Day Zero Warning):** In 2019, Chennai became the first major Indian metropolitan city to hit 'Day Zero'—all four of its major reservoirs completely dried up! Millions of citizens relied on expensive private water tankers, IT companies asked employees to work from home, and restaurants shut down. This disaster was caused not just by deficient rainfall, but by the destruction of 80% of the city's traditional lakes and wetlands due to unplanned concrete construction!",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "common_mistakes",
        "content": "⚠️ **Common Student Mistake:** Students often write that *'digging deeper tube-wells is the permanent solution to water scarcity.'* \n**Correction:** Digging deeper borewells actually accelerates groundwater depletion and taps into fossil aquifers rich in toxic fluorides and arsenic. The ONLY true long-term solution is **Artificial Groundwater Recharge `(ભૂગર્ભ જળ રિચાર્જિંગ)`** and **Rainwater Harvesting `(વૃષ્ટિ જળ સંચયન)`**!",
        "difficulty": "Intermediate",
        "bloom": "Evaluate"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "Which of the following is a direct negative consequence of excessive, unregulated groundwater extraction in coastal regions?",
            "options": [
                "Increased frequency of volcanic eruptions",
                "Salinity ingress (sea water seeping into freshwater aquifers)",
                "Increase in atmospheric ozone layer thickness",
                "Decrease in soil erosion along rivers"
            ],
            "correct_answer": "Salinity ingress (sea water seeping into freshwater aquifers)",
            "explanation": "When fresh groundwater near coastal regions is pumped out faster than it recharges, the hydraulic pressure drops, causing saline sea water to infiltrate the underground freshwater aquifers."
        },
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })
    
    # ==========================================
    # MODULE 7: WATER CONSERVATION & WATERSHED MANAGEMENT
    # ==========================================
    blocks.append({
        "type": "theory",
        "title": "Management and Conservation of Water Resources (જળ સંસાધનોની જાળવણી અને વ્યવસ્થાપન)",
        "content": "Water conservation requires a combined strategy of **Engineering, Ecological Preservation, and Community Participation**:\n\n• **Three Golden Pillars of Water Conservation `(જળ સંરક્ષણના ત્રણ સ્તંભો)`:**\n  1. **Judicious & Efficient Use `(વિવેકપૂર્ણ અને કરકસરભર્યો ઉપયોગ)`:** Eliminating wasteful consumption in domestic, agricultural, and industrial processes.\n  2. **Storage Reservoir Construction `(જળાશયોનું નિર્માણ અને સંગ્રહ)`:** Creating check dams, percolation tanks, and reservoirs to capture floodwaters.\n  3. **Inter-basin River Linking `(નદી બેસિન જોડાણ / નદીઓના પાણીનું એકત્રીકરણ)`:** Diverting surplus floodwaters from excess river basins (e.g., Ganga, Brahmaputra) to water-deficient deficit basins (Peninsular rivers, Saurashtra, Rajasthan).",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "title": "Watershed Development / Management (જળપ્લાવિત ક્ષેત્ર વિકાસ / जलसंभर विकास)",
        "content": "A **Watershed `(જળપ્લાવિત ક્ષેત્ર / जलसंभर)`** is a natural hydrological geographical unit where all surface runoff water resulting from rain drains through a network of small streams and rills to converge into a single common stream, river, lake, or wetland.\n\n• **Key Programmes & Activities in Watershed Development:**\n  1. **Soil & Moisture Conservation `(જમીન અને ભેજ સંરક્ષણ)`:** Contour bunding and terracing on hill slopes.\n  2. **Afforestation & Tree Plantation `(વૃક્ષારોપણ / વનીકરણ)`:** Planting native trees on degraded slopes to reduce runoff speed.\n  3. **Construction of Check Dams `(ચેકડેમ / બંધારા / પાળા બાંધવા)`:** Building small stone/concrete barriers across seasonal rivulets to trap water and recharge local wells.\n  4. **Horticulture & Pasture Development `(બાગાયતી ખેતી અને ગોચર વિકાસ)`:** Growing fruit orchards and grass cover to prevent soil erosion.\n  5. **Revival of Village Ponds `(ગામના તળાવોનું ઊંડુંકરણ અને પુનર્જીવન)`:** Desilting local ponds to maximize holding capacity.\n\n• **The Heart of Watershed Management:** **Public Participation `(લોકભાગીદારી / जन सहभागिता)`**! Government schemes alone cannot succeed unless local village communities manage, monitor, and maintain the watershed assets collectively (e.g., the remarkable success of Anna Hazare's Ralegan Siddhi model in Maharashtra).",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Teacher's Secret:** When writing about Watershed Management in GSEB board exams, always emphasize that it is an **Integrated Approach `(સંકલિત અભિગમ)`** that simultaneously protects **Soil (Land)**, **Water**, and **Vegetation (Forests)** while uplifting the rural economy through community self-reliance.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "What is the primary natural unit of land where all precipitation drains through interconnected streams to a single common outlet called?",
            "options": [
                "Plateau Basin",
                "Watershed (જળપ્લાવિત ક્ષેત્ર)",
                "Desert Oasis",
                "Continental Shelf"
            ],
            "correct_answer": "Watershed (જળપ્લાવિત ક્ષેત્ર)",
            "explanation": "A watershed (or catchment basin) is a natural geographical hydrological unit where all surface runoff drains through streams to a single common water body or outlet."
        },
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })
    
    # ==========================================
    # MODULE 8: RAINWATER HARVESTING & MICRO-IRRIGATION
    # ==========================================
    blocks.append({
        "type": "theory",
        "title": "Rainwater Harvesting: Objectives & Methods (વૃષ્ટિ જળ સંચયન)",
        "content": "**Rainwater Harvesting `(વૃષ્ટિ જળ સંચયન / વરસાદી પાણીનો સંગ્રહ / वर्षा जल संचयन)`** is the technique of capturing, diverting, and storing rainwater that falls on building rooftops, open compounds, and farmlands for direct reuse or for recharging subterranean aquifers.\n\n**Primary Objectives `(વૃષ્ટિ જળ સંચયનના મુખ્ય ઉદ્દેશો)`:**\n1. **Stop Runoff Waste `(પાણીનો વ્યય અટકાવવો)`:** Prevent precious rainwater from rushing wastefully into drains and getting lost in the ocean.\n2. **Groundwater Recharge `(ભૂગર્ભ જળ રિચાર્જ / भूजल पुनर्भरण)`:** Inject surface water into depleted aquifers through percolation pits, recharging dried borewells.\n3. **Improve Water Quality `(પાણીની ગુણવત્તા સુધારવી)`:** Dilute underground salinity, fluorides, and contaminants by injecting pure rainwater.\n4. **Mitigate Urban Flooding `(શહેરી પૂર અને જળબંબાકારની સ્થિતિ રોકવી)`:** Reduce waterlogging on city roads during heavy downpours.\n5. **Bridge Summer Water Shortages `(ઉનાળામાં પાણીની અછત નિવારવી)`:** Store surplus water in underground cisterns/tanks `(ટાંકા)` to meet dry-season domestic needs.\n\n**Major Traditional & Modern Harvesting Techniques:**\n• **Rooftop Rainwater Harvesting `(મકાનોની છત પરથી પાણી સંગ્રહ)`:** Rain falling on terraces is filtered through sand-gravel filters and channeled directly into underground storage tanks or recharge borewells.\n• **Farm Ponds / Khet Talavadi `(ખેત તલાવડી / खेत तालाब)`:** Farmers dig small earthen ponds at the lowest corner of their fields to collect surface runoff, which provides life-saving supplemental irrigation to standing crops during monsoon dry spells.\n• **Check Dams / Bandharas `(ચેકડેમ / નાના બંધારા)`:** Small structures constructed across seasonal streams to raise the groundwater level in nearby agricultural wells.\n• **Soak Pits & Percolation Wells `(શોષખાડા અને રિચાર્જિંગ કૂવા)`:** Pits filled with gravel and charcoal that filter storm runoff into deeper soil layers.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Diagram of Rooftop Rainwater Harvesting showing terrace collection pipe, filtration chamber (sand/gravel), and connection to underground storage sump and recharge well.",
        "image_url": "assets/images/rooftop_rainwater_harvesting_system.jpg",
        "alt_text": "Architectural diagram showing rooftop rainwater collection with filtration unit and recharge well."
    })
    
    blocks.append({
        "type": "theory",
        "title": "General Guidelines & Solutions for Water Conservation (જળ સંરક્ષણ માટેના સામાન્ય ઉપાયો)",
        "content": "To avert an existential water catastrophe, the following nationwide measures must be enforced:\n\n1. **Adopt Micro-Irrigation Technologies `(સૂક્ષ્મ સિંચાઈ પદ્ધતિઓ / सूक्ष्म सिंचाई)`:**\n   - **Drip Irrigation `(ટપક સિંચાઈ પદ્ધતિ / ड्रिप सिंचाई)`:** Delivers water directly to crop root zones drop-by-drop, reducing evaporation and saving **40% to 60% water** while boosting crop productivity.\n   - **Sprinkler Irrigation `(ફુવારા પદ્ધતિ / फव्वारा सिंचाई)`:** Simulates natural rain, preventing runoff losses, ideal for undulating/sandy soils.\n\n2. **Recycling and Reuse of Greywater `(વાપરેલા પાણીનો પુનઃઉપયોગ)`:**\n   - Treated industrial and domestic wastewater `(શુદ્ધ કરેલું ગંદું પાણી)` should be recycled for industrial cooling, vehicle washing, construction, and urban gardening.\n\n3. **Strict Pollution Control Laws `(કડક પ્રદૂષણ નિયંત્રણ કાયદા)`:**\n   - Enforce heavy legal penalties and shut down industrial units that dump untreated toxic chemical effluents into rivers and lakes.\n\n4. **Canal Maintenance & Leakage Prevention `(નહેરોનું સમારકામ)`:**\n   - Line irrigation canals with concrete to eliminate heavy seepage losses `(પાણીનો ઝમણ વ્યય)` and repair pipeline bursts immediately.\n\n5. **Mass Awareness Campaigns `(વ્યાપક જનજાગૃતિ અભિયાન)`:**\n   - Educate citizens and school children on turning off taps, installing aerators, harvesting rain, and respecting every drop as liquid gold.",
        "difficulty": "Intermediate",
        "bloom": "Apply"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "What is the primary purpose of constructing a 'Khet Talavadi' (Farm Pond / ખેત તલાવડી) in an agricultural field?",
            "options": [
                "To breed ornamental exotic fish for export",
                "To collect rainwater runoff and provide supplemental irrigation to crops during dry spells",
                "To dump chemical pesticide containers safely",
                "To convert agricultural land into commercial swimming pools"
            ],
            "correct_answer": "To collect rainwater runoff and provide supplemental irrigation to crops during dry spells",
            "explanation": "A Khet Talavadi (farm pond) is excavated in a corner of the farm to collect surface rainwater runoff. This stored water provides crucial life-saving irrigation during monsoon breaks."
        },
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    # ==========================================
    # MODULE 9: BOARD EXAM MASTERY (TIPS, PYQS, HOTS & MAP WORK)
    # ==========================================
    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **GSEB CLASS 10 BOARD EXAM BLUEPRINT & SCORING HACKS:**\n\n1. **4-Mark Long Answer Questions (High Probability):**\n   - *\"What is a Multi-Purpose Project? Explain its main objectives and give examples of 4 major projects in India.\"*\n   - *Structure:* (a) Definition with Nehru's quote (b) 6-8 bullet points of objectives (Flood control, irrigation, power, etc.) (c) Master table showing 4 projects, rivers, and states.\n\n2. **3-Mark Analytical Questions:**\n   - *\"State the reasons for the growing Water Crisis in India.\"* (Focus on population explosion, over-pumping, pollution, and cash crops).\n   - *\"What is Rainwater Harvesting? Mention its 5 key objectives.\"*\n   - *\"Write a short note on Watershed Development (જળપ્લાવિત ક્ષેત્ર વિકાસ).\"*\n\n3. **2-Mark Short Notes & Reasoning:**\n   - *\"Why is Tank irrigation prominent in South India while Tube-wells dominate North India?\"*\n   - *\"Why is Sardar Sarovar considered the Lifeline of Gujarat?\"*\n\n4. **Map-Pointing Practice (Compulsory Board Map Questions):**\n   - Locating **Bhakra-Nangal Dam** (River Sutlej, Punjab/Himachal border).\n   - Locating **Hirakud Dam** (River Mahanadi, Odisha).\n   - Locating **Nagarjuna Sagar Dam** (River Krishna, Andhra/Telangana border).\n   - Locating **Sardar Sarovar Dam** (River Narmada, Gujarat).",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })
    
    blocks.append({
        "type": "board_questions",
        "content": "📝 **PREVIOUS YEARS' BOARD QUESTIONS (PYQs & HOTS):**\n\n**Q1 (GSEB March 2020, 2023):** Explain the measures for water conservation and rainwater harvesting. *(4 Marks)*\n\n**Q2 (GSEB March 2019, 2022):** Name the multi-purpose project on the Narmada River and mention its beneficiary states. *(2 Marks)*\n*Model Answer:* The multi-purpose project on River Narmada is **Sardar Sarovar Project**. The beneficiary states are **Gujarat, Madhya Pradesh, Rajasthan, and Maharashtra**.\n\n**Q3 (HOTS Question):** *'Drip irrigation is a boon for semi-arid regions like Gujarat and Rajasthan.'* Justify the statement.\n*Model Answer:* In semi-arid regions with high evaporation rates and scarce water, flood irrigation wastes 50%+ water through runoff and evaporation. Drip irrigation delivers water and nutrients directly to the root zone drop-by-drop, cutting water usage by 40-60%, preventing weed growth, eliminating soil salinity build-up, and increasing crop yields even in low water conditions.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "summary",
        "content": "📌 **CHAPTER 11 QUICK REVISION RECAP:**\n\n• **3 Sources of Water:** Rainwater (Primary), Surface Water (Rivers/Lakes), Groundwater (Aquifers - 42% in Northern Plains).\n• **Sectoral Consumption:** Agriculture/Irrigation accounts for ~84% of total water consumption in India.\n• **3 Mediums of Irrigation:** 1. Wells & Tube-wells (Rank 1 - North India) 2. Canals (Rank 2 - Northern & Deltaic plains) 3. Tanks/Ponds (Rank 3 - South Peninsular hard rocks).\n• **Temples of Modern India:** Multi-purpose projects named by Pt. Nehru (Bhakra-Nangal, Damodar Valley, Hirakud, Sardar Sarovar, Nagarjuna Sagar).\n• **Irrigation Disparity:** Punjab has highest (~90.8%) while Mizoram has lowest (~7.3%) irrigated area.\n• **Water Crisis Causes:** Population boom, cash crop agriculture, groundwater over-extraction, industrial pollution, salinity ingress.\n• **Solutions:** Watershed management with public participation, Rooftop Rainwater Harvesting, Khet Talavadi, Drip/Sprinkler micro-irrigation, wastewater recycling.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "reflection",
        "content": "🌱 **Socratic Reflection Activity:**\nTake a look around your own household and school today. List three daily activities where clean drinking water is being wasted carelessly (e.g., washing vehicles with running hosepipes, leaking taps, overflowing overhead tanks). If you were appointed as the Municipal Water Commissioner of your city, what two strict policies would you implement to make rainwater harvesting mandatory for every new building?",
        "difficulty": "Beginner",
        "bloom": "Create"
    })
    
    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    # Save to GSEB chapter path
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_social_science_ch11.json"
    os.makedirs(os.path.dirname(gseb_path), exist_ok=True)
    with open(gseb_path, "w", encoding="utf-8") as f:
        json.dump(final_json, f, ensure_ascii=False, indent=2)
    print(f"Successfully generated: {gseb_path}")
    
    # Save to NCERT chapter path
    ncert_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_social_science_ch11.json"
    with open(ncert_path, "w", encoding="utf-8") as f:
        json.dump(final_json, f, ensure_ascii=False, indent=2)
    print(f"Successfully generated: {ncert_path}")

if __name__ == "__main__":
    generate_supreme_gseb_ss_ch11()
