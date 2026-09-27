import json
import os

def generate_supreme_gseb_ss_ch8():
    chapter_id = "gseb_class10_social_science_ch8"
    title = "Chapter 8: Natural Resources"
    
    metadata = {
        "id": chapter_id,
        "title": title,
        "subtitle": "The Ultimate Board Exam Mastery Guide",
        "subject": "Social Science",
        "grade": "10",
        "board": "GSEB/NCERT",
        "curriculum": ["GSEB", "NCERT", "CBSE"],
        "language": "English/Hindi/Gujarati (Bilingual)",
        "difficulty": "Advanced",
        "estimated_minutes": 180,
        "version": "3.0.0-SUPREME-PEDAGOGY",
        "author": "Antigravity Supreme Intelligence",
        "reviewed_by": "Chief Academic Architect",
        "tags": [
            "social_science",
            "geography",
            "natural_resources",
            "soils_of_india",
            "alluvial_soil",
            "black_soil",
            "regur",
            "laterite_soil",
            "soil_erosion",
            "soil_conservation",
            "board_special",
            "bilingual"
        ],
        "learning_outcomes": [
            "Define what constitutes a Natural Resource `(प्राकृतिक संसाधन / કુદરતી સંસાધનો)` and analyze its 3 vital uses.",
            "Classify resources based on Ownership `(स्वामित्व / માલિકી)`, Distribution `(वितरण / વિતરણ)`, and Renewability `(नवीकरणीयता / નવીનીકરણક્ષમતા)`.",
            "Master the genesis, chemical properties, and crop suitability of all 8 ICAR soil types in India.",
            "Analyze the root causes of Soil Erosion `(मृदा अपरदन / જમીનનું ધોવાણ)` and formulate 5 actionable Soil Conservation `(मृदा संरक्षण / જમીન સંરક્ષણ)` strategies.",
            "Solve Board Exam HOTS, Assertion-Reasoning questions, and high-frequency PYQs with model scoring keys."
        ],
        "ai_context": {
            "learning_goal": "Guide Class 10 students to complete mastery of Natural Resources and Soil Geography through Socratic discovery, visual diagrams, memory tricks, and bilingual English/Hindi/Gujarati clarity.",
            "common_misconceptions": [
                "Students confuse Solitary (Unique) resources with Rare resources. (Clarification: Cryolite found only in Greenland is Solitary; Minerals like Coal/Uranium found in a few countries are Rare).",
                "Students assume Black Soil is ruined when it cracks in summer. (Clarification: Cracks cause self-aeration; Black Soil is exceptionally fertile with unmatched moisture retention!).",
                "Students confuse Laterite leaching with normal soil erosion. (Clarification: Leaching is vertical percolation of silica under heavy rainfall, leaving iron-aluminum oxides)."
            ],
            "tutor_hint": "If a student struggles with the 8 soil types, remind them of the mnemonic 'A R B L D M F P'. For soil conservation, invoke real-world hill slope and desert shelter belt imagery."
        }
    }
    
    blocks = []
    
    # =========================================================================
    # MODULE 1: THE CONCEPT & MEANING OF RESOURCES (સંસાધન એટલે શું?)
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "Imagine a barren riverbank thousands of years ago covered with ordinary stones, mud, and wild trees. Early humans walked over them without a second thought. But the moment human beings learned how to shape those stones into hunting tools, melt rocks into iron, and grow grains in the mud, those ordinary elements transformed into **Resources `(संसाधन / સંસાધન)`**! What made the difference? The magic touch of human knowledge, skill, and technology!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Look at how nature's raw elements convert into valuable economic resources through human intellectual and technological intervention.",
        "image_url": "assets/images/ss_ch8_resource_transformation.jpg",
        "alt_text": "Diagram showing Raw Elements + Human Intellect + Technology = Natural Resource"
    })
    
    blocks.append({
        "type": "theory",
        "content": "A **Resource `(संसाधन / સંસાધન)`** is anything in the environment that can satisfy human needs, provided it is technologically accessible, economically feasible, and culturally acceptable.\n\nEvery natural substance must fulfill **Three Essential Criteria `(ત્રણ આવશ્યક શરતો)`** to become a resource:\n1. **Utility `(उपयोगिता / ઉપયોગિતા)`:** It must be capable of fulfilling human needs directly or indirectly.\n2. **Human Physical & Intellectual Capacity `(मानव क्षमता / માનવીય ક્ષમતા)`:** Humans must have the knowledge and capability to utilize it.\n3. **Technological Application `(तकनीकी अनुप्रयोग / તકનીકી ઉપયોગ)`:** Tools and machinery must exist to extract and process it.\n\n*Historical Insight:* Thousands of minerals lay hidden deep under the Earth for centuries. They were NOT resources to primitive humans because technology did not exist to extract them. They became resources only when human civilization developed mining and metallurgy!",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Master Teacher's Secret:** In Board Exams, examiners look for the phrase: *'Nature, Man, and Technology interact dynamically to create Resources.'* Never write that resources are merely free gifts of nature—they are the result of human interaction with nature!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "mcq",
        "content": "Which of the following conditions is mandatory for a natural substance to be classified as a 'Resource'?",
        "options": [
            "It must simply exist in large quantities on Earth.",
            "It must satisfy human needs through human knowledge and technological capability `(માનવીય ક્ષમતા અને તકનીક)`.",
            "It must be completely non-renewable.",
            "It must be owned exclusively by the government."
        ],
        "correct_answer": "It must satisfy human needs through human knowledge and technological capability `(માનવીય ક્ષમતા અને તકનીક)`.",
        "explanation": "A natural material becomes a resource only when human skills and technology are applied to use it for satisfying human needs `(उपयोगिता और तकनीकी क्षमता)`.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    # =========================================================================
    # MODULE 2: THE THREE CHIEF USES OF RESOURCES (સંસાધનોના ઉપયોગો)
    # =========================================================================
    blocks.append({
        "type": "theory",
        "content": "Human life and civilization are entirely dependent on natural resources. We utilize resources across **Three Primary Dimensions `(સંસાધનોના ત્રણ મુખ્ય ઉપયોગો)`**:\n\n1. **Resource as Food `(भोजन के रूप में संसाधन / ખોરાક તરીકે)`:**\n   - Various agricultural crops (wheat, rice, pulses).\n   - Naturally grown fruits, honey collected from forests, milk and meat from domestic animals, and fish from water bodies.\n\n2. **Resource as a Source of Raw Materials `(कच्चे माल का स्रोत / કાચા માલના સ્ત્રોત તરીકે)`:**\n   - **Forest Products:** Timber `(ઇમારતી લાકડું)`, gum, resin, bamboo, and medicinal herbs `(ઔષધિઓ)`.\n   - **Agro-based Products:** Cotton for textile mills, sugarcane for sugar factories, and jute for packaging.\n   - **Mineral Ores:** Iron ore for steel plants, bauxite for aluminum smelters, and crude oil for petrochemicals.\n   - **Animal By-products:** Wool `(ઊન)`, leather/hides `(ચામડું)`, and bones.\n\n3. **Resource as Energy Resources `(ऊर्जा संसाधन / ઊર્જાના સ્ત્રોત તરીકે)`:**\n   - **Conventional (Commercial) Fuels:** Coal `(કોલસો)`, Mineral Oil / Petroleum `(ખનીજ તેલ)`, and Natural Gas `(કુદરતી વાયુ)`.\n   - **Non-Conventional / Renewable Energy:** Solar Energy `(સૌર ઊર્જા)`, Wind Energy `(પવન ઊર્જા)`, Hydroelectricity `(જળ વિદ્યુત)`, Tidal Energy `(ભરતી ઊર્જા)`, and Geothermal Energy `(ભૂ-તાપીય ઊર્જા)`.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Visual map categorizing Natural Resources into Food, Industrial Raw Materials, and Energy Sources.",
        "image_url": "assets/images/ss_ch8_uses_of_resources.jpg",
        "alt_text": "Triangular chart of Resource Uses: Food, Raw Material, Energy"
    })
    
    blocks.append({
        "type": "real_world_example",
        "content": "🌾 **Real World Connection:** Think of a sugarcane stalk in Gujarat. As food, you chew its sweet juice. As raw material, sugar mills convert it into refined sugar and distilleries convert its molasses into bio-ethanol fuel. As energy, the leftover crushed cane stalk (bagasse) is burned in boilers to generate green electricity! One single resource serves all three dimensions!",
        "difficulty": "Intermediate",
        "bloom": "Apply"
    })
    
    blocks.append({
        "type": "mcq",
        "content": "Which of the following sets represents resources used exclusively as 'Industrial Raw Materials' `(કાચા માલના સ્ત્રોતો)`?",
        "options": [
            "Honey, Milk, Wheat",
            "Coal, Solar Rays, Petroleum",
            "Cotton, Iron Ore, Timber `(કપાસ, લોખંડની કાચી ધાતુ, લાકડું)`",
            "Tidal waves, Biogas, Geothermal steam"
        ],
        "correct_answer": "Cotton, Iron Ore, Timber `(કપાસ, લોખંડની કાચી ધાતુ, લાકડું)`",
        "explanation": "Cotton (textiles), Iron Ore (steel manufacturing), and Timber (furniture/paper) are raw materials processed in factories to produce finished goods.",
        "difficulty": "Beginner",
        "bloom": "Analyze"
    })
    
    # =========================================================================
    # MODULE 3: CLASSIFICATION OF RESOURCES (સંસાધનોનું વર્ગીકરણ)
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "Who owns the sunlight shining in your backyard? Nobody, it belongs to everyone! Who owns your house? Your family. Who owns the Indian Army and the national highway? The Nation. And who owns a rare mineral that exists in only ONE frozen island on Earth? Let's explore the scientific classification of all resources across Ownership, Distribution, and Availability!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "content": "**A. Classification Based on Ownership `(स्वामित्व के आधार पर / માલિકીના આધારે)`:**\n1. **Individual Resource `(व्यक्तिगत संसाधन / વ્યક્તિગત સંસાધન)`:** Owned by a single person or family.\n   - *Examples:* Private land, residential house, private vehicle.\n2. **National Resource `(राष्ट्रीय संसाधन / રાષ્ટ્રીય સંસાધન)`:** Owned and managed by a country or nation for public welfare.\n   - *Examples:* Military assets, public railways, national highways, domestic rivers, minerals within national boundaries, territorial sea up to 12 nautical miles `(દરિયાઈ સીમા)`.\n3. **Global / Universal Resource `(वैश्विक संसाधन / વૈશ્વિક સંસાધન)`:** Physical resources owned collectively by humanity for common global welfare.\n   - *Examples:* The High Seas / International waters `(આંતરરાષ્ટ્રીય જળસીમા)`, Antarctica, the Earth's atmosphere, outer space.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "content": "**B. Classification Based on Distribution Area `(वितरण क्षेत्र के आधार पर / વિતરણ ક્ષેત્રના આધારે)`:**\n1. **Ubiquitous / Universal Resources `(सर्वसुलभ संसाधन / સર્વસુલભ સંસાધન)`:** Useful gases available everywhere in the atmosphere.\n   - *Examples:* Nitrogen `(નાઇટ્રોજન)` and Oxygen `(ઓક્સિજન)`.\n2. **General Resources `(सामान्य सुलभ संसाधन / સામાન્ય સુલભ સંસાધન)`:** Easily available across most geographical terrains.\n   - *Examples:* Agricultural land, soil, fresh water `(જળ)`, pasture land `(ગૌચર)`.\n3. **Rare Resources `(विरल संसाधन / વિરલ સંસાધન)`:** Minerals found only at a few limited places on Earth.\n   - *Examples:* Coal, Petroleum, Copper `(તાંબું)`, Gold, Uranium, Thorium.\n4. **Solitary / Unique Resources `(एकल संसाधन / એકલ સંસાધન)`:** Minerals found at only ONE or TWO isolated locations in the entire world!\n   - *Super Star Example:* **Cryolite Mineral `(क्रायोलाइट खनिज / ક્રાયોલાઇટ ખનીજ)`**, which is naturally found ONLY in Greenland!",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "memory_trick",
        "content": "**🧠 Board Exam Mnemonic for Distribution Types:**\nRemember: **'U - G - R - S'** (You Grow Real Smart!)\n- **U**biquitous `(સર્વસુલભ)` - Air everywhere (Oxygen, Nitrogen)\n- **G**eneral `(સામાન્ય સુલભ)` - Land & Water\n- **R**are `(વિરલ)` - Gold & Petroleum (Few places)\n- **S**olitary `(એકલ)` - Cryolite in Greenland (Single place!)",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "theory",
        "content": "**C. Classification Based on Renewability `(पुनःप्राप्यता के आधार पर / નવીનીકરણના આધારે)`:**\n1. **Renewable / Inexhaustible Resources `(नवीकरणीय / નવીનીકરણીય અથવા અખૂટ સંસાધનો)`:**\n   - Resources that reproduce themselves naturally within a reasonable time span and do not get exhausted upon use.\n   - *Examples:* Solar radiation, wind, running water, forests, wildlife, biomass.\n2. **Non-Renewable / Exhaustible Resources `(अनवीकरणीय / અનવીનીકરણીય અથવા ક્ષયશીલ સંસાધનો)`:**\n   - Resources that take millions of years of geological heat and pressure to form. Once consumed, they cannot be regenerated or reused.\n   - *Examples:* Coal, Crude Petroleum, Natural Gas, Mineral ores.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM 1-MARK GUARANTEED QUESTION:**\n*Question:* Name the mineral that is an example of a 'Solitary Resource' `(એકલ સંસાધન)` and where it is found.\n*Perfect Answer:* **Cryolite Mineral `(ક્રાયોલાઇટ ખનીજ)`**, found naturally only in **Greenland `(ગ્રીનલેન્ડ)`**.",
        "difficulty": "Advanced",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "mcq",
        "content": "Cryolite mineral `(ક્રાયોલાઇટ ખનીજ)` is classified under which category of resources on the basis of distribution?",
        "options": [
            "Ubiquitous Resource `(સર્વસુલભ સંસાધન)`",
            "General Resource `(સામાન્ય સુલભ સંસાધન)`",
            "Rare Resource `(વિરલ સંસાધન)`",
            "Solitary / Unique Resource `(એકલ સંસાધન)`"
        ],
        "correct_answer": "Solitary / Unique Resource `(એકલ સંસાધન)`",
        "explanation": "Because Cryolite is available naturally in only one place in the entire world (Greenland), it is a classic example of a Solitary/Unique Resource `(एकल संसाधन)`.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })
    
    # =========================================================================
    # MODULE 4: PLANNING AND CONSERVATION OF RESOURCES (સંસાધનોનું આયોજન અને સંરક્ષણ)
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "What would happen if humanity burns all remaining petroleum and coal in the next 40 years? Machines would stop, airplanes would be grounded, and industries would collapse. As Mahatma Gandhi famously warned: *'The Earth provides enough to satisfy every man's need, but not every man's greed!'* How do we balance modern development with the survival of our future generations?",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "content": "**Resource Conservation `(संसाधन संरक्षण / સંસાધન સંરક્ષણ)`** means the rational, judicious, and sustainable utilization of resources without reckless wastage, while protecting them from depletion for future generations.\n\n**Key Steps in Resource Planning & Conservation `(સંસાધન આયોજનના સોપાનો)`:**\n1. **Comprehensive Inventory & Survey:** Prepare maps, estimate the quantity, quality, and geographical reserves of all domestic resources.\n2. **Prioritization of Scarcity:** Non-renewable and scarce resources `(અછતવાળા સંસાધનો)` must be utilized only when absolutely indispensable.\n3. **Development of Eco-Friendly Substitutes `(વૈકલ્પિક સ્ત્રોતોનો વિકાસ)`:** Shift rapidly from fossil fuels to solar, wind, and green hydrogen power.\n4. **Application of the 3Rs Principle:** **Reduce** consumption, **Reuse** discarded items, and **Recycle** metals, plastics, and industrial wastewater.\n5. **Strict Enforcement of Environmental Legislation:** Impose heavy penalties and legal restrictions on illegal mining, unauthorized deforestation, and industrial pollution.\n6. **Fostering Public Awareness:** Educate citizens regarding the prudent and responsible consumption of water, electricity, and mineral products.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Master Teacher's Formula for 3-Mark Question on Conservation:** Always divide your answer into: (1) Definition of Conservation, (2) Technological steps (Renewables & 3Rs), and (3) Legal & Civic steps (Laws & Public Awareness). This guarantees 100% full marks!",
        "difficulty": "Intermediate",
        "bloom": "Apply"
    })
    
    blocks.append({
        "type": "mcq",
        "content": "What is the primary philosophy behind 'Resource Conservation' `(સંસાધન સંરક્ષણ)`?",
        "options": [
            "Completely stopping the use of all natural resources immediately.",
            "Rational, judicious, and sustainable utilization of resources to prevent wastage and secure future generations `(વિવેકપૂર્ણ અને ટકાઉ ઉપયોગ)`.",
            "Consuming non-renewable resources as quickly as possible before they lose value.",
            "Exporting all domestic mineral reserves to foreign nations."
        ],
        "correct_answer": "Rational, judicious, and sustainable utilization of resources to prevent wastage and secure future generations `(વિવેકપૂર્ણ અને ટકાઉ ઉપયોગ)`.",
        "explanation": "Conservation does not imply hoarding resources without use; it means using them prudently (વિવેકપૂર્ણ ઉપયોગ) and sustaining them for the future.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    # =========================================================================
    # MODULE 5: SOIL AND SOIL FORMATION (જમીન અને જમીન નિર્માણ)
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "Did you know that it takes Mother Nature between **500 to 1,000 years** to generate just **1 single centimeter** of fertile topsoil? Yet, a single torrential rainstorm or careless farmer can wash it away in a few hours! What is this precious thin skin of the Earth that feeds 8 billion human beings?",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "content": "**What is Soil? `(મૃદા / જમીન એટલે શું?)`:**\nSoil is the uppermost, thin layer of the Earth's crust composed of mineral particles `(ખનીજ કણો)` and decomposed organic matter / humus `(સેન્દ્રિય દ્રવ્યો)`, which supports plant life and agricultural crops.\n\n**The Process of Soil Formation (Pedogenesis) `(જમીન નિર્માણની પ્રક્રિયા)`:**\nSoil is formed through the physical and chemical breakdown of parental bedrock over centuries under the influence of climate.\n\n$$\\text{Parent Bedrock} \\xrightarrow{\\text{Weathering & Erosion}} \\text{Fine Mineral Particles} + \\text{Biotic Humus} \\xrightarrow{\\text{Time}} \\text{Fertile Soil}$$\n\n**The Four Master Controlling Factors:**\n1. **Parent Rock `(मूल चट्टान / મૂળ ખડકો)`:** Dictates the initial mineral composition, texture, and colour of the soil.\n2. **Climate `(जलवायु / આબોહવા)`:** The most dominant factor! Temperature fluctuations and rainfall regulate the speed and intensity of rock weathering `(ખવાણ)`.\n   - *Golden Rule:* Rocks with different origins will produce the **same type of soil** under identical climatic conditions! Conversely, identical rocks under different climates produce completely different soils!\n3. **Biotic Elements / Humus `(जीवांश / સેન્દ્રિય દ્રવ્યો-હ્યુમસ)`:** Decaying leaves, roots, bacteria, and dead insects add essential nitrogen, carbon, and moisture-holding spongy humus.\n4. **Time & Topography `(સમય અને ભૂપૃષ્ઠ)`:** Steeper slopes have thin, immature soil layers, while flat plains allow deep, well-developed soil horizons to mature.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Diagram illustrating the Soil Profile showing Horizon A (Topsoil with Humus), Horizon B (Subsoil), Horizon C (Weathered Parent Material), and Horizon D (Bedrock).",
        "image_url": "assets/images/ss_ch8_soil_profile.jpg",
        "alt_text": "Soil Profile layers from Topsoil to solid Bedrock"
    })
    
    blocks.append({
        "type": "memory_trick",
        "content": "**🧠 Pedogenesis Factors Formula:**\nRemember: **'C - L - O - R - P - T'**\n- **Cl**imate `(આબોહવા - Most Important!)`\n- **O**rganisms / Humus `(સેન્દ્રિય તત્વો)`\n- **R**elief / Topography `(ભૂપૃષ્ઠ)`\n- **P**arent Rock `(મૂળ ખડક)`\n- **T**ime `(સમયગાળો)`",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "mcq",
        "content": "Which factor plays the MOST decisive and dominant role in determining the type of soil formed over time?",
        "options": [
            "Human agricultural fertilizers",
            "Climate (Temperature and Rainfall) `(આબોહવા - તાપમાન અને વરસાદ)`",
            "The shape of ocean currents",
            "The gravitational pull of the moon"
        ],
        "correct_answer": "Climate (Temperature and Rainfall) `(આબોહવા - તાપમાન અને વરસાદ)`",
        "explanation": "Climate governs the rate of mechanical weathering and chemical decomposition of rocks. Under the same climate, different rocks yield identical soil types.",
        "difficulty": "Intermediate",
        "bloom": "Analyze"
    })
    
    # =========================================================================
    # MODULE 6: THE 8 SOILS OF INDIA - PART 1 (THE AGRICULTURAL POWERHOUSES)
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "The Indian Council of Agricultural Research (ICAR) classifies Indian soils into **8 Distinct Types `(ભારતની જમીનના ૮ પ્રકારો)`**. Let's examine the three greatest agricultural soils that produce over 80% of India's food grains and cotton!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "content": "### 1. Alluvial Soil `(जलोढ़ मिट्टी / કાંપવાળી જમીન)`\n- **Acreage & Spread:** Covers approximately **43%** of India's total geographical area (Largest soil group!).\n- **Geographical Distribution:** Northern river plains from Punjab in the west to Assam in the east, and the coastal deltas of Mahanadi, Godavari, Krishna, and Kaveri rivers.\n- **Formation:** Formed by the continuous deposition of fine alluvial silt `(કાંપ)` carried by the Himalayan rivers (Indus, Ganga, Brahmaputra).\n- **Chemical Characteristics:** Highly rich in **Potash `(પોટાશ)`**, **Phosphoric Acid `(ફોસ્ફોરિક એસિડ)`**, and **Lime `(ચૂનો)`**. However, it is deficient in **Nitrogen `(નાઇટ્રોજન)`** and **Humus `(હ્યુમસ)`**.\n- **Two Sub-types:**\n  1. **Khadar `(ખાદર)`:** New alluvial soil deposited by annual river floods. Fine-grained, light-coloured, and extremely fertile.\n  2. **Bhangar `(બાંગર)`:** Old alluvium found in higher river terraces. Contains calcium nodules (Kankar `(કંકર)`) and is coarse-textured.\n- **Suitable Crops:** Wheat `(ઘઉં)`, Paddy/Rice `(ડાંગર)`, Sugarcane `(શેરડી)`, Jute `(શણ)`, Cotton, Maize, and Oilseeds.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "content": "### 2. Black Soil / Regur / Black Cotton Soil `(काली मिट्टी / કાળી અથવા રેગુર જમીન)`\n- **Acreage & Spread:** Covers approximately **15%** of India's total land area.\n- **Geographical Distribution:** Entire Deccan Lava Plateau `(દક્ષિણનો લાવામય ઉચ્ચપ્રદેશ)` covering Maharashtra, Western Madhya Pradesh, parts of Karnataka, Andhra Pradesh, and extensively in Gujarat (Surat, Bharuch, Vadodara, Bhavnagar).\n- **Formation:** Formed by the weathering of basaltic volcanic lava rocks `(દક્ષિણના લાવારસના ખડકો)` under hot, semi-arid climatic conditions.\n- **Unique Superpowers:**\n  - **Tremendous Moisture Retention `(અદ્ભુત ભેજ સંગ્રહણ શક્તિ)`:** It is extremely clayey `(ચીકણી)`. It holds moisture for months!\n  - **Self-Ploughing Phenomenon `(આપમેળે ખેડાતી જમીન)`:** When wet, it swells and becomes exceptionally sticky. When dry in scorching summer heat, it shrinks and develops **deep fissures and wide cracks `(ઊંડી તિરાડો)`**. As wind blows loose organic matter into these cracks, the soil aerates itself naturally without mechanical ploughing!\n- **Chemical Composition:** Exceptionally rich in **Iron `(લોહ)`**, **Lime `(ચૂનો)`**, **Calcium Carbonate**, **Potash**, and **Magnesium**.\n- **Suitable Crops:** **Cotton `(કપાસ)`** (Hence named 'Black Cotton Soil'), Tobacco, Groundnut `(મગફળી)`, Sugarcane, Soybean, and Wheat.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "theory",
        "content": "### 3. Red & Yellow Soil `(लाल और पीली मिट्टी / રાતી અથવા લાલ જમીન)`\n- **Acreage & Spread:** Covers approximately **19%** of India's total geographical area.\n- **Geographical Distribution:** Extends from Tamil Nadu in the south to Bundelkhand in the north, and from Rajmahal hills in the east to Kutch in the west. Prominent in Odisha, Chhattisgarh, and Chota Nagpur plateau.\n- **Formation:** Formed due to the weathering of ancient crystalline igneous and metamorphic rocks `(અગ્નિકૃત અને રૂપાંતરિત ખડકો)` in regions of low rainfall.\n- **Distinctive Colour:** Its fiery red colour is caused by the presence of **Ferric Oxide `(ફેરીક ઓક્સાઇડ / લોહ તત્વ)`**. In hydrated deeper layers, it turns yellowish in appearance.\n- **Characteristics & Crops:** Porous and friable texture. Lacks lime, kankar, and carbonates; deficient in magnesium, nitrogen, and humus. Yields excellent crops with fertilizers.\n- **Suitable Crops:** Bajra / Pearl Millet `(બાજરી)`, Ragi, Groundnut, Pulses `(કઠોળ)`, Tobacco, and Cotton.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT REASONING QUESTION:**\n*Question:* Why does Black Soil develop deep cracks during dry summer seasons, and why is this advantageous to farmers?\n*Answer:* Black soil contains high clay content. Upon losing moisture in summer, it contracts significantly, creating wide fissures. This allows sunlight and atmospheric air to penetrate deep into the lower soil horizons (natural aeration / self-ploughing). When the first monsoon rains fall, moisture easily seeps deep into the subsoil!",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })
    
    blocks.append({
        "type": "mcq",
        "content": "Which unique soil type develops deep fissures/cracks during summer and possesses unmatched moisture-retention capability?",
        "options": [
            "Desert Soil `(રણ પ્રકારની જમીન)`",
            "Black / Regur Soil `(કાળી અથવા રેગુર જમીન)`",
            "Mountain Soil `(પર્વતીય જમીન)`",
            "Laterite Soil `(લેટેરાઇટ જમીન)`"
        ],
        "correct_answer": "Black / Regur Soil `(કાળી અથવા રેગુર જમીન)`",
        "explanation": "Black soil's high clay density causes it to expand when wet and contract into deep fissures when dry, giving it its famous moisture retention and self-aerating qualities.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    # =========================================================================
    # MODULE 7: THE 8 SOILS OF INDIA - PART 2 (SPECIALIZED & REGIONAL SOILS)
    # =========================================================================
    blocks.append({
        "type": "theory",
        "content": "### 4. Laterite or Leached Soil `(लेटराइट या पडखाऊ मिट्टी / લેટેરાઇટ અથવા પડખાઉ જમીન)`\n- **Etymology:** Derived from the Latin word **'Later'**, which translates to **'Brick `(ईंट / ઈંટ)`**.\n- **Formation (The Leaching Process / નિક્ષાલન):** Formed in tropical regions characterized by alternating heavy monsoon rains and high temperatures. Heavy rainfall washes down the soluble silica and lime minerals into lower strata (called **Leaching `(ધોવાણ / નિક્ષાલન)`**), leaving insoluble Iron and Aluminum oxides on the surface.\n- **Characteristics:** When wet, it becomes soft and slippery like butter `(માખણ જેવી મુલાયમ)`. But when it dries under the sun, it hardens like a red building brick!\n- **Distribution:** Western Ghats (Sahyadri), Eastern Ghats, plateau of Meghalaya, parts of Kerala, Karnataka, and Odisha.\n- **Suitable Crops:** Acidic and low in natural fertility. With proper chemical fertilizers and irrigation, it is the best soil for plantation crops: **Tea `(ચા)`**, **Coffee `(કોફી)`**, **Cashew `(કાજુ)`**, and **Rubber**.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "theory",
        "content": "### 5. Desert / Arid Soil `(मरुस्थलीय मिट्टी / રણ પ્રકારની જમીન)`\n- **Formation & Traits:** Formed under arid and semi-arid conditions with high temperatures and rapid evaporation rates. Coarse, sandy, and porous texture. High in soluble salts `(ક્ષારિય)` and deficient in moisture and humus.\n- **Distribution:** Thar Desert of Rajasthan, Northern Gujarat (Kutch, Saurashtra, Banaskantha), Southern Haryana and Punjab.\n- **Suitable Crops:** With modern drip and canal irrigation, farmers grow hardy crops: **Bajra `(બાજરી)`**, **Jowar `(જુવાર)`**, Pulses, and Castor `(દિવેલા)`.\n\n### 6. Mountain Soil `(पर्वतीय मिट्टी / પર્વતીય જમીન)`\n- **Distribution:** Valleys and steep slopes of the Himalayas at altitudes between **2,700 meters to 3,000 meters**.\n- **Characteristics:** Thin and immature layer. In coniferous forest belts (Deodar, Pine, Spruce), decomposing needles provide a thick layer of acidic organic humus.\n- **Suitable Crops:** **Tea, Coffee, Spices, Orchard Fruits** (Kashmiri Apples `(સફરજન)`, Peaches, Plums, Apricots).\n\n### 7. Forest Soil `(वन मृदा / જંગલ પ્રકારની જમીન)`\n- **Distribution:** Sub-Himalayan belt between **3,000 to 3,100 meters** altitude, Sahyadri, and Eastern Ghats.\n- **Characteristics:** The upper surface is blanketed by dead fallen leaves. Decaying leaves make the topsoil dark black, while the sub-surface layer is reddish-blue.\n- **Suitable Crops:** Cardamom `(એલચી)`, Black Pepper, Tea, Coffee, Barley, Maize.\n\n### 8. Marshy or Peaty Soil `(दलदली या पीट मिट्टी / દલદલીય કે પીટ પ્રકારની જમીન)`\n- **Formation:** Developed in humid coastal zones experiencing continuous waterlogging and accumulation of undecomposed organic matter `(જૈવિક પદાર્થોનું સંચય)`.\n- **Characteristics:** Organic content accounts for 40% to 50% of the soil mass! Highly alkaline, deficient in phosphate and potash.\n- **Distribution:** Sundarbans delta in West Bengal, coastal Odisha, coastal Tamil Nadu, Almora district of Uttarakhand, northern Bihar.\n- **Crop:** In monsoons it remains submerged under water; once water recedes, **Paddy / Rice `(ડાંગર-ચોખા)`** is cultivated extensively.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Geographical overview map showing the regional distribution of all 8 ICAR soil types across the Indian subcontinent.",
        "image_url": "assets/images/ss_ch8_india_soil_map.jpg",
        "alt_text": "Map of India displaying Alluvial, Black, Red, Laterite, Desert, Mountain, Forest, and Peaty Soil zones"
    })
    
    blocks.append({
        "type": "memory_trick",
        "content": "**🧠 Master Mnemonic for All 8 Soils of India:**\nRecite: **'A - R - B - L - D - M - F - P'**\n*(“All Rivers Bring Life Down Mountain Forest Plains”)*\n- **A**lluvial `(કાંપવાળી જમીન - 43%)`\n- **R**ed `(રાતી જમીન - 19%)`\n- **B**lack `(કાળી / રેગુર જમીન - 15%)`\n- **L**aterite `(લેટેરાઇટ / પડખાઉ જમીન)`\n- **D**esert `(રણ પ્રકારની જમીન)`\n- **M**ountain `(પર્વતીય જમીન)`\n- **F**orest `(જંગલ પ્રકારની જમીન)`\n- **P**eaty / Marshy `(દલદલીય કે પીટ જમીન)`",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "mcq",
        "content": "The name 'Laterite Soil' `(લેટેરાઇટ જમીન)` is derived from the Latin root word 'Later', which means:",
        "options": [
            "Fertile river silt `(કાંપ)`",
            "Brick `(ईंट / ઈંટ)`",
            "Volcanic black lava `(લાવા)`",
            "Forest leaf humus `(સેન્દ્રિય દ્રવ્ય)`"
        ],
        "correct_answer": "Brick `(ईंट / ઈંટ)`",
        "explanation": "Laterite comes from the Latin word 'Later' (meaning Brick) because upon drying, the soil hardens into rock-solid brick-like blocks.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    # =========================================================================
    # MODULE 8: SOIL EROSION - THE SILENT THIEF (જમીનનું ધોવાણ)
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "Imagine a thief sneaking into our country every single year and stealing thousands of acres of our most fertile food-producing land without making a single sound. That thief is **Soil Erosion `(मृदा अपरदन / જમીનનું ધોવાણ)`**! Every monsoon, rushing rivers wash billions of tons of fertile topsoil straight into the Arabian Sea and Bay of Bengal. How does this happen, and what destruction does it leave behind?",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "content": "**What is Soil Erosion? `(મૃદા અપરદન / જમીન ધોવાણ એટલે શું?)`:**\nSoil Erosion is the physical detachment, displacement, and transportation of topsoil particles from one place to another by rapid natural forces like **Fast-Flowing Water `(ઝડપી વહેતું પાણી)`** and **High-Velocity Wind `(તીવ્ર પવન)`**.\n\n**Two Chief Mechanisms of Water Erosion:**\n1. **Sheet Erosion `(चादरी अपरदन / પડ ધોવાણ)`:** Raindrops dislodge the top layer, and surface runoff washes away a uniform thin sheet of top fertile soil over vast flat areas. Often invisible to the naked eye until crop yields collapse!\n2. **Gully Erosion `(अवनालिका अपरदन / કોતર ધોવાણ)`:** Fast-moving runoff cuts deep vertical trenches, channels, and canyons into bare land. Over time, it turns fertile agricultural land into useless, barren badlands/ravines (e.g., the infamous **Chambal Ravines `(ચંબલના કોતરો)`**).\n\n**Human Causes Accelerating Soil Erosion:**\n- **Deforestation `(જંગલોનો વિનાશ)`:** Tree roots bind soil particles together; stripping tree cover leaves soil naked to rain.\n- **Overgrazing `(અતિ ચરાણ)`:** Livestock herds eat away grass cover and their hooves pulverize the soil surface.\n- **Faulty Agricultural Practices:** Ploughing straight up and down hill slopes acts as drainage pipes for rainwater, accelerating erosion.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Visual diagram comparing Sheet Erosion (uniform top layer stripping) vs Gully Erosion (deep ravine carving).",
        "image_url": "assets/images/ss_ch8_soil_erosion_types.jpg",
        "alt_text": "Comparison of Sheet Erosion and Deep Gully Erosion in agricultural fields"
    })
    
    blocks.append({
        "type": "mcq",
        "content": "The cutting of deep ravines and trenches in agricultural land by fast-flowing surface runoff is known as:",
        "options": [
            "Sheet Erosion `(પડ ધોવાણ)`",
            "Gully Erosion `(કોતર ધોવાણ / अवनालिका अपरदन)`",
            "Pedogenesis `(જમીન નિર્માણ)`",
            "Humification `(હ્યુમસ નિર્માણ)`"
        ],
        "correct_answer": "Gully Erosion `(કોતર ધોવાણ / अवनालिका अपरदन)`",
        "explanation": "Gully erosion occurs when runoff carves deep channels into unanchored soil, transforming fertile farmland into unusable badland ravines.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    # =========================================================================
    # MODULE 9: SOIL CONSERVATION STRATEGIES (જમીન સંરક્ષણના ઉપાયો)
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "If soil erosion is the disease, **Soil Conservation `(મૃદા સંરક્ષણ)`** is the master cure! How can smart engineering, terraced farming, and biological green shields preserve our farmlands forever? Let's master the 5 battle-tested remedies approved by agricultural scientists!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "content": "**Soil Conservation `(मृदा संरक्षण / જમીન સંરક્ષણ)`** refers to the prevention of soil loss from erosion and the preservation of soil fertility through deliberate scientific, agronomic, and engineering measures.\n\n**The 5 Master Measures to Prevent Soil Erosion `(જમીન ધોવાણ અટકાવવાના ૫ મુખ્ય ઉપાયો)`:**\n1. **Regulation of Pasture Grazing `(ચરિયાણ પ્રવૃત્તિઓનું નિયમન)`:** Control excessive animal grazing on hill slopes and public pastures to allow grass roots to anchor the soil firmly.\n2. **Contour Bunding & Terrace Farming `(સમોચ્ચ રેખીય ખેતી અને સીડીદાર ખેતરો)`:** On mountain slopes, build step-like terraces `(સીડીદાર ખેતરો)` and plow along contour lines `(સમોચ્ચ રેખાઓ)`. This reduces the velocity of descending rainwater, allowing water to percolate gently into the soil rather than washing it away.\n3. **Planting Shelter Belts / Windbreaks `(રક્ષક મેખલા / વૃક્ષારોપણ)`:** In arid desert regions and coastal plains, plant dense parallel rows of trees perpendicular to the prevailing wind direction. This breaks the force of violent desert winds and halts sand encroachment `(રણ આગળ વધતું અટકાવે છે)`.\n4. **Construction of Check Dams & Bandharas `(ચેકડેમ અને આડબંધ નિર્માણ)`:** Build small check dams across seasonal streams, nullahs, and gullies. This obstructs water runoff velocity, traps fertile silt, and recharges underground water tables.\n5. **Deep Ploughing & Mulching `(ઊંડી ખેડ અને જમીન પર સેન્દ્રિય આવરણ)`:** Practice deep furrow ploughing to facilitate deep moisture seepage, and cover open soil with crop residues/mulch to retain surface moisture and prevent wind detachment.",
        "difficulty": "Advanced",
        "bloom": "Apply"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Illustrated guide showing Terrace Farming on hill slopes, Shelter Belts in arid plains, and Check Dams across streams.",
        "image_url": "assets/images/ss_ch8_soil_conservation_methods.jpg",
        "alt_text": "Engineering and Agronomic methods of Soil Conservation: Terracing, Shelter Belts, Check Dams"
    })
    
    blocks.append({
        "type": "real_world_example",
        "content": "🌱 **Gujarat Soil Conservation Triumph:** In the arid regions of Saurashtra and Kutch, thousands of check dams `(ચેકડેમ)` constructed under community watershed initiatives have prevented devastating soil erosion, recharged dried borewells, and allowed farmers to cultivate lush green cotton and groundnut crops in former desert zones!",
        "difficulty": "Intermediate",
        "bloom": "Apply"
    })
    
    blocks.append({
        "type": "mcq",
        "content": "Which soil conservation method is MOST effective in preventing wind erosion and halting desert advancement in arid zones like Rajasthan and Kutch?",
        "options": [
            "Over-irrigation with saline water",
            "Planting dense Shelter Belts / Rows of trees `(રક્ષક મેખલા / વૃક્ષારોપણ)`",
            "Removing all wild grass and shrubs",
            "Ploughing straight up and down hill slopes"
        ],
        "correct_answer": "Planting dense Shelter Belts / Rows of trees `(રક્ષક મેખલા / વૃક્ષારોપણ)`",
        "explanation": "Shelter belts (rows of trees) dramatically reduce wind speed, preventing wind from blowing away topsoil and checking the expansion of deserts (રણ આગળ વધતું અટકાવવું).",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    # =========================================================================
    # MODULE 10: BOARD EXAM MASTERY & HOTS VAULT (બોર્ડ પરીક્ષા વિશેષ)
    # =========================================================================
    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM TOP 5-MARK MODEL ANSWER STRUCTURE:**\n\n**Question:** Describe the classification of Indian soils, giving detailed characteristics of Alluvial Soil and Black Soil.\n\n**Examiner Scoring Rubric:**\n1. **Introductory Statement (1 Mark):** Name ICAR and list the 8 soil types using the mnemonic 'A R B L D M F P'.\n2. **Alluvial Soil Core Breakdown (2 Marks):**\n   - 43% area coverage.\n   - Formed by Himalayan/Peninsular river silt deposition.\n   - Rich in Potash/Lime; deficient in Nitrogen/Humus.\n   - Difference between Khadar (New) and Bhangar (Old).\n   - Major crops: Wheat, Paddy, Sugarcane, Jute.\n3. **Black Soil Core Breakdown (2 Marks):**\n   - 15% area coverage (Deccan Lava Plateau, Gujarat, Maharashtra).\n   - Volcanic basaltic origin.\n   - High clay density, outstanding moisture retention, self-ploughing fissures.\n   - King crop: Cotton (Black Cotton Soil / Regur).\n\nFollow this structured point-by-point format to secure 100% full marks!",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })
    
    blocks.append({
        "type": "common_mistakes",
        "content": "⚠️ **TOP 3 BOARD EXAM BLUNDERS TO AVOID:**\n1. **Mistake 1:** Writing that Khadar is old alluvium and Bhangar is new alluvium. *(Correction: Khadar = New alluvium, Bhangar = Old alluvium with kankar).* \n2. **Mistake 2:** Confusing Leaching with Surface Erosion. *(Correction: Leaching in Laterite soil is the vertical downwards percolation of silica under heavy rainfall).* \n3. **Mistake 3:** Forgetting to mention 'Cryolite in Greenland' when asked for a Solitary Resource example.",
        "difficulty": "Intermediate",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "summary",
        "content": "📌 **CHAPTER 8 REVISION CAPSULE:**\n- **Resource Definition:** Nature + Human Skills + Technology satisfying human needs.\n- **3 Chief Uses:** Food, Industrial Raw Materials, Energy Sources.\n- **Ownership Classes:** Individual, National, Global.\n- **Distribution Classes:** Ubiquitous (Oxygen), General (Land/Water), Rare (Gold/Coal), Solitary (Cryolite in Greenland).\n- **8 Soils of India (ICAR):** Alluvial (43%), Red (19%), Black (15%), Laterite, Desert, Mountain, Forest, Peaty.\n- **Soil Erosion:** Detachment and transport of topsoil by running water (Sheet & Gully) and wind.\n- **Conservation Remedies:** Terrace farming, Contour bunding, Shelter belts, Check dams, Controlled grazing.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    # Write to GSEB path
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_social_science_ch8.json"
    with open(gseb_path, "w", encoding="utf-8") as f:
        json.dump(final_json, f, indent=2, ensure_ascii=False)
        
    # Write to NCERT path
    ncert_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_social_science_ch8.json"
    final_json_ncert = json.loads(json.dumps(final_json))
    final_json_ncert["metadata"]["id"] = "ncert_class10_social_science_ch8"
    final_json_ncert["metadata"]["board"] = "NCERT/CBSE/GSEB"
    with open(ncert_path, "w", encoding="utf-8") as f:
        json.dump(final_json_ncert, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully generated Supreme GSEB SS Ch8 for {gseb_path} and {ncert_path}!")

if __name__ == "__main__":
    generate_supreme_gseb_ss_ch8()
