import json
import os

def generate_supreme_gseb_ss_ch13():
    chapter_id = "gseb_class10_social_science_ch13"
    title = "Chapter 13: Manufacturing Industries"
    
    metadata = {
        "id": chapter_id,
        "title": title,
        "subtitle": "The Ultimate Board Exam Mastery & Concept Discovery Guide",
        "subject": "Social Science",
        "grade": "10",
        "board": "GSEB/NCERT/CBSE",
        "curriculum": ["GSEB", "NCERT", "CBSE", "Universal"],
        "language": "English/Hindi/Gujarati (Bilingual)",
        "difficulty": "Advanced",
        "estimated_minutes": 240,
        "version": "3.0.0-SUPREME-PEDAGOGY",
        "author": "Antigravity Supreme Intelligence",
        "reviewed_by": "Chief Academic Architect",
        "tags": [
            "social_science",
            "geography",
            "manufacturing_industries",
            "gseb_class10",
            "ncert_class10",
            "board_special",
            "bilingual",
            "gujarat_board",
            "indian_economy"
        ],
        "learning_outcomes": [
            "Understand the definition and multidimensional importance of manufacturing industries in national economic development.",
            "Master the 5-fold classification of industries based on raw materials, main role, capital investment, ownership, and weight.",
            "Analyze major Agro-based industries (Cotton, Jute, Silk, Woollen, Synthetic, Sugar, and Paper) including geographic localization factors.",
            "Evaluate major Mineral-based industries (Iron & Steel, Aluminium, Copper Smelting, Chemical, Fertilizer, Cement, Automobile, Railways, Aviation, Shipbuilding, and Electronics/IT).",
            "Examine Gujarat's preeminent position in Textiles, Chemicals, Petrochemicals, Fertilizers, Cement, and Dairy Cooperatives.",
            "Identify the 4 types of industrial pollution and formulate comprehensive sustainable mitigation strategies (NTPC guidelines, effluent treatment).",
            "Score 100% in GSEB/CBSE Board Exams on map-pointing, 3-mark analytical questions, and 5-mark structured long answers."
        ],
        "ai_context": {
            "learning_goal": "Transform the student from a beginner into an academic topper in Class 10 Manufacturing Industries. Use the Gold Socratic Pedagogy Cycle with bilingual translations, mental maps, mnemonics, teacher tips, exam traps, and real-world industrial case studies.",
            "common_misconceptions": [
                "Students think industrialization harms agriculture, whereas modern industries actually modernize agriculture by providing tractors, pumps, and fertilizers.",
                "Students confuse basic/key industries with consumer industries.",
                "Students often believe India produces its own potash fertilizer (Fact: 100% of potash is imported).",
                "Students confuse the locational advantages of the cotton textile industry in Mumbai/Ahmedabad with the jute textile industry in the Hugli basin."
            ],
            "tutor_hint": "Emphasize why industries cluster in specific geographical nodes (raw material, power, water, skilled labour, transport, market, banking). For Gujarat board questions, emphasize Ahmedabad as 'Manchester of the East' and Gujarat's leadership in petrochemicals and chemicals."
        }
    }
    
    blocks = []
    
    # =========================================================================
    # MODULE 1: INTRODUCTION & IMPORTANCE OF MANUFACTURING INDUSTRIES
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "Look around your study desk. Your notebook was once raw wood pulp `(લાકડાનો માવો / लकड़ी की लुगदी)`. The sugar in your morning milk was once dense sugarcane stalks `(શેરડી / गन्ना)`. The bus or bicycle you ride was once raw iron ore `(કાચું લોખંડ / कच्चा लोहा)` buried deep inside rocky hills!\n\nHow do raw, low-value gifts of nature turn into high-value, durable products? Through the magic of **Manufacturing Industries `(ઉત્પાદન ઉદ્યોગો / विनिर्माण उद्योग)`**!\n\n> **The Golden Law of Economics:** The economic strength and prosperity of any country is measured directly by the development and breadth of its manufacturing industries!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Value Addition Chain: From Raw Materials to High-Value Finished Consumer Products.",
        "image_url": "assets/images/ss_ch13_value_addition_chain.jpg",
        "alt_text": "Flowchart showing Raw Cotton -> Yarn Spinning -> Fabric Weaving -> Garment Manufacturing -> High Value Branded Apparel."
    })
    
    blocks.append({
        "type": "theory",
        "title": "1.1 Meaning & Definition of Manufacturing",
        "content": "**Definition:** The process of converting raw materials `(કાચો માલ / कच्चा माल)` into more useful, high-utility and valuable finished goods `(તૈયાર માલ / तैयार माल)` in large quantities using mechanical power and machinery is called **Manufacturing `(ઉત્પાદન / विनिर्माण)`**.\n\n*   Manufacturing belongs to the **Secondary Sector `(દ્વિતીયક ક્ષેત્ર / द्वितीयक क्षेत्र)`** of the economy.\n*   Workers employed in steel factories, car manufacturing, bakeries, textile mills, and breweries belong to this secondary sector.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "theory",
        "title": "1.2 Why Manufacturing is the Backbone of Economic Development",
        "content": "Why is manufacturing considered the primary engine of national development?\n\n1.  **Modernising Agriculture `(કૃષિનું આધુનિકીકરણ / कृषि का आधुनिकीकरण)`:** It does not compete with agriculture; it strengthens it! Industries supply tractors, harvesters, threshers, tube wells, chemical fertilizers `(રાસાયણિક ખાતરો / रासायनिक उर्वरक)`, pesticides, and PVC pipes, multiplying agricultural productivity.\n2.  **Eradicating Poverty & Unemployment `(ગરીબી અને બેરોજગારી નાબૂદી / गरीबी और बेरोजगारी उन्मूलन)`:** Manufacturing creates millions of direct jobs in factories and tens of millions of indirect jobs in transport, logistics, banking, and trade (Tertiary Sector).\n3.  **Boosting Foreign Exchange `(વિદેશી હૂંડિયામણની કમાણી / विदेशी मुद्रा अर्जन)`:** Exporting manufactured and engineered goods brings in precious foreign exchange, strengthening the national currency.\n4.  **National Wealth Transformation `(રાષ્ટ્રીય સંપત્તિમાં વધારો / राष्ट्रीय समृद्धि)`:** Countries that export raw materials remain poor, while countries that transform raw materials into finished goods (like Japan, Germany, USA) become wealthy and prosperous.\n5.  **Regional Balance `(પ્રાદેશિક સંતુલન / क्षेत्रीय संतुलन)`:** Setting up public sector industries in tribal and backward areas (e.g., Bhilai, Rourkela) reduces regional disparities.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Teacher's Master Insight:** Remember the symbiotic relationship! Agriculture and Industry are NOT separate or exclusive; they move hand-in-hand. For example, the agro-industries in India have given a massive boost to agriculture by creating high demand for cash crops (cotton, sugarcane, jute) while returning advanced tools and fertilizers back to farmers.",
        "difficulty": "Beginner",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "Which of the following statements best explains why manufacturing industries are considered the backbone of economic development?",
            "options": [
                "They completely replace agriculture and eliminate farm labor.",
                "They modernize agriculture, reduce unemployment, and earn foreign exchange through manufactured exports.",
                "They only produce luxury goods for the elite class.",
                "They eliminate the need for the service and banking sectors."
            ],
            "correct_answer": "They modernize agriculture, reduce unemployment, and earn foreign exchange through manufactured exports.",
            "explanation": "Manufacturing modernizes agriculture by supplying machinery and fertilizers, generates mass employment in secondary/tertiary sectors, and brings in high foreign exchange by exporting value-added goods."
        },
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    # =========================================================================
    # MODULE 2: CLASSIFICATION OF INDUSTRIES (THE 5-WAY FRAMEWORK)
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "Is a roadside potter making clay pots `(માટીના વાસણો / मिट्टी के बर्तन)` in the same category as a multi-billion dollar Tata Steel plant producing millions of tonnes of hot-rolled coils? \n\nTo understand the vast industrial landscape, economists classify industries using **5 distinct structural criteria**!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "The Complete 5-Dimensional Classification Framework of Manufacturing Industries.",
        "image_url": "assets/images/ss_ch13_industry_classification_mindmap.jpg",
        "alt_text": "Mindmap classifying industries by Raw Materials, Main Role, Capital Investment, Ownership, and Weight/Bulk."
    })
    
    blocks.append({
        "type": "theory",
        "title": "2.1 Classification on the Basis of Raw Materials (કાચા માલના સ્ત્રોત આધારે)",
        "content": "Industries are grouped into two primary classes depending on where they source their raw materials:\n\n*   **1. Agro-Based Industries `(કૃષિ આધારિત ઉદ્યોગો / कृषि आधारित उद्योग)`:** Use agricultural produce as their primary raw input.\n    *   *Examples:* Cotton textiles `(સુતરાઉ કાપડ / सूती वस्त्र)`, Jute textiles `(શણ કાપડ / पटसन वस्त्र)`, Silk, Woollen textiles, Sugar `(ખાંડ / चीनी)`, Edible oil `(ખાદ્ય તેલ / खाद्य तेल)`, Paper.\n*   **2. Mineral-Based Industries `(ખનીજ આધારિત ઉદ્યોગો / खनिज आधारित उद्योग)`:** Use metallic and non-metallic minerals extracted from the earth.\n    *   *Examples:* Iron and Steel `(લોખંડ અને પોલાદ / लोहा और इस्पात)`, Aluminium smelting `(એલ્યુમિનિયમ ગાળણ / एल्युमिनियम प्रगलन)`, Copper smelting, Cement `(સિમેન્ટ / सीमेंट)`, Chemical industries, Fertilizer plants, Heavy machinery, Automobiles.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "theory",
        "title": "2.2 Classification by Main Role, Capital Investment & Weight",
        "content": "**A. According to their Main Role `(મુખ્ય ભૂમિકાના આધારે / मुख्य भूमिका के आधार पर)`:**\n*   **Basic or Key Industries `(મૂળભૂત / આધારભૂત ઉદ્યોગો / आधारभूत उद्योग)`:** Industries that supply their products as raw materials to manufacture other finished products.\n    *   *Examples:* Iron and Steel industry (supplies steel to make car engines, bridges, needles), Copper smelting, Aluminium smelting.\n*   **Consumer Industries `(ઉપભોક્તા ઉદ્યોગો / उपभोक्ता उद्योग)`:** Industries that produce goods for direct consumption by end users.\n    *   *Examples:* Sugar, toothpaste, paper, sewing machines, ceiling fans, soaps.\n\n**B. According to Capital Investment `(મૂડી રોકાણના કદ આધારે / पूंजी निवेश के आधार पर)`:**\n*   **Small Scale Industry `(નાના પાયાના ઉદ્યોગો / लघु उद्योग)`:** Maximum investment allowed on the assets of a unit is up to ₹1 Crore (Micro/Small/Medium thresholds updated per MSME guidelines). Generates high employment per rupee invested.\n*   **Large Scale Industry `(મોટા પાયાના ઉદ્યોગો / बड़े पैमाने के उद्योग)`:** Investment exceeds ₹1 Crore (running into thousands of crores). Employs massive automated machinery and thousands of laborers (e.g., TISCO, Reliance Jamnagar Refinery).\n*   **Cottage / Village Industry `(ગૃહ / કુટિર ઉદ્યોગો / कुटीर उद्योग)`:** Run by family members in their homes with minimal capital and simple hand tools (e.g., handloom, khadi, pottery, basket weaving).\n\n**C. According to Bulk and Weight of Raw Material & Finished Goods:**\n*   **Heavy Industries `(ભારે ઉદ્યોગો / भारी उद्योग)`:** Use bulky, heavy raw materials and produce heavy goods (e.g., Iron and Steel, Shipbuilding, Heavy Engineering).\n*   **Light Industries `(હળવા ઉદ્યોગો / हल्के उद्योग)`:** Use light raw materials and produce light finished products (e.g., Electrical appliances, watches, toys, sewing needles).",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "title": "2.3 Classification on the Basis of Ownership (માલિકીના આધારે)",
        "content": "Who owns, finances, and runs the factory? \n\n1.  **Public Sector `(જાહેર ક્ષેત્ર / सार्वजनिक क्षेत्र)`:** Owned and operated directly by government ministries or government agencies.\n    *   *Examples:* **BHEL** (Bharat Heavy Electricals Ltd), **SAIL** (Steel Authority of India Ltd), **ONGC**, **GAIL**, Indian Railways.\n2.  **Private Sector `(ખાનગી ક્ષેત્ર / निजी क्षेत्र)`:** Owned and operated by individuals or a group of private individuals/corporations.\n    *   *Examples:* **TISCO** (Tata Iron and Steel Company), **Reliance Industries Limited (RIL)**, **Bajaj Auto**, **Dabur**, **Adani Group**.\n3.  **Joint Sector `(સંયુક્ત ક્ષેત્ર / संयुक्त क्षेत्र)`:** Jointly run by the Government (State) and Private individuals/companies together.\n    *   *Example:* **Oil India Limited (OIL)**, Gujarat State Petroleum Corporation joint ventures.\n4.  **Cooperative Sector `(સહકારી ક્ષેત્ર / सहकारी क्षेत्र)`:** Owned, financed, and operated by the primary producers or suppliers of raw materials, factory workers, or both. They pool resources and share profits/losses proportionally.\n    *   *Golden Examples:* **AMUL (Anand Milk Union Limited)** in Gujarat, Sugar mills across Maharashtra, Coir industry in Kerala.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "memory_trick",
        "content": "🧠 **Super Mnemonic to Remember 4 Ownership Types:** \n**P - P - J - C** ⟶ **\"Pure People Join Cooperatives\"**\n*   **P** = **Public Sector** (Government owned like SAIL/BHEL)\n*   **P** = **Private Sector** (Individually owned like Tata/Reliance)\n*   **J** = **Joint Sector** (Govt + Private Partnership like Oil India Ltd)\n*   **C** = **Cooperative Sector** (Producers/Workers owned like AMUL)",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "Which of the following is the best example of a Cooperative Sector Industry in India?",
            "options": [
                "Bharat Heavy Electricals Limited (BHEL)",
                "Tata Iron and Steel Company (TISCO)",
                "AMUL (Anand Milk Union Limited)",
                "Oil India Limited (OIL)"
            ],
            "correct_answer": "AMUL (Anand Milk Union Limited)",
            "explanation": "AMUL is owned and run cooperatively by millions of milk producers and farmers in Gujarat who pool their milk and share the profits proportionally."
        },
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    # =========================================================================
    # MODULE 3: AGRO-BASED TEXTILE INDUSTRIES (COTTON, JUTE, SILK, WOOLLEN, SYNTHETIC)
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "Did you know that in ancient and medieval times, Indian muslin `(ઢાકાનું મલમલ / मलमल)`, calicos, and chintz were world-famous, and Roman aristocrats paid in gold to wear Indian cotton? \n\nToday, the **Textile Industry `(કાપડ ઉદ્યોગ / वस्त्र उद्योग)`** occupies a unique position in the Indian economy because it is completely **self-reliant `(આત્મનિર્ભર / आत्मनिर्भर)`** and value-complete from raw fiber generation to high-fashion garment production!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "title": "3.1 The Cotton Textile Industry (સુતરાઉ કાપડ ઉદ્યોગ)",
        "content": "**Historical Milestones:**\n*   The first successful modern mechanized cotton textile mill was established in **Mumbai in 1854**.\n*   Later, in Gujarat, the first cotton mill was established in **Ahmedabad in 1861** (by Ranchhodlal Chhotalal).\n\n**Why was the Cotton Textile Industry historically concentrated in Maharashtra and Gujarat? (Board Exam Favorite):**\n1.  **Availability of Raw Cotton:** Black regur soil `(કાળી કપાસની જમીન / काली कपासी मिट्टी)` of Maharashtra and Gujarat provides raw cotton at cheap rates.\n2.  **Humid Marine Climate `(ભેજવાળી આબોહવા / नम जलवायु)`:** Coastal climate prevents the cotton yarn from breaking frequently during spinning.\n3.  **Transport & Port Facilities:** Ports like Mumbai, Kandla, and Jawaharlal Nehru Port (JNPT) allow cheap import of machinery and export of cotton textiles.\n4.  **Abundant Labour:** Easy availability of skilled and cheap labor from nearby rural areas.\n5.  **Capital & Banking:** Rich mercantile community and established financial/banking facilities in Mumbai and Ahmedabad.\n6.  **Vast Market:** Huge domestic and international demand for light, breathable cotton clothes.\n\n**Key Indian Hubs:**\n*   **Mumbai:** Known as the **\"Cottonopolis of India\"**.\n*   **Ahmedabad:** Celebrated as the **\"Manchester of the East\"** or **\"Denim City of India\"**.\n*   **Surat:** Famous for weaving, synthetic textiles, embroidery, and zari work.\n*   Other major centers: Coimbatore, Tirupur, Madurai (Tamil Nadu), Kanpur (UP), Kolkata, Indore, Ludhiana.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM 3-MARK HOT TOPIC:** *\"Why is Ahmedabad called the Manchester of the East?\"*\n\n**Model Answer Structure:**\n1.  **Historical Similarity:** Just like Manchester in England flourished due to climate and port access, Ahmedabad developed a massive cluster of mechanized cotton textile mills on the banks of River Sabarmati.\n2.  **Raw Material Proximity:** Located in the heart of Gujarat's rich cotton-growing tracts (Kanam and Saurashtra regions).\n3.  **Ideal Climate & Soft Water:** Humid atmosphere suitable for spinning fine thread without breaking, and abundant soft water from the Sabarmati river for bleaching and dyeing.\n4.  **Transport & Market:** Excellent rail, road connectivity, proximity to Kandla and Mumbai ports, and enterprising Gujarati entrepreneurs.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "theory",
        "title": "3.2 The Jute Textile Industry - \"The Golden Fibre\" (શણ કાપડ ઉદ્યોગ)",
        "content": "India is the **largest producer of raw jute** and jute goods in the world, and stands at **second place as an exporter** after Bangladesh.\n\n*   The first jute mill in India was established at **Rishra near Kolkata in 1855**.\n\n**Why are nearly all Jute Mills concentrated in a narrow belt along the Hugli River (West Bengal)?**\n1.  **Proximity to Jute Growing Areas:** West Bengal and the Ganga-Brahmaputra delta produce the highest quality raw jute.\n2.  **Inexpensive Water Transport:** The Hugli River provides cheap inland water transport supported by a dense network of railways and roads.\n3.  **Abundant Freshwater for Processing:** Re-retting `(શણના રેસા છૂટા પાડવાની પ્રક્રિયા / पटसन के रेशे धोने की प्रक्रिया)` requires millions of gallons of fresh water.\n4.  **Cheap Labour:** Inexpensive labor readily available from West Bengal, Bihar, Odisha, and Uttar Pradesh.\n5.  **Kolkata's Urban Support:** Banking, insurance, export facilities, and port services of Kolkata.\n\n**Challenges & Revival:**\n*   Stiff competition from synthetic plastic substitutes `(કૃત્રિમ પ્લાસ્ટિક વિકલ્પો / सिंथेटिक विकल्प)` and cheaper international producers like Bangladesh, Brazil, Egypt.\n*   **National Jute Policy (2005):** Formulated to increase productivity, improve quality, ensure fair prices to jute farmers, and mandate biodegradable packaging `(બાયોડિગ્રેડેબલ પેકેજિંગ / पर्यावरण-अनुकूल पैकेजिंग)` for foodgrains and sugar.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "title": "3.3 Silk, Woollen & Synthetic Textile Industries",
        "content": "**A. Silk Textile Industry `(રેશમ કાપડ ઉદ્યોગ / रेशम वस्त्र उद्योग)`:**\n*   India produces 4 distinct commercial varieties of natural silk: **Mulberry `(મલબેરી)`**, **Tasar `(તસર)`**, **Eri `(એરી)`**, and **Muga `(મૂંગા - exclusive to Assam)`**.\n*   Major Producing States: **Karnataka** (produces >50% of India's raw silk), West Bengal, Jammu & Kashmir, Tamil Nadu, Andhra Pradesh, and Assam.\n*   Silk weaving centers: Varanasi (Banarasi Sarees), Kanchipuram, Surat, Dharmavaram, Bhagalpur.\n\n**B. Woollen Textile Industry `(ઊન કાપડ ઉદ્યોગ / ऊनी वस्त्र उद्योग)`:**\n*   Historically one of India's oldest cottage industries.\n*   Concentrated in: **Punjab** (Ludhiana - the hosiery capital, Amritsar, Dhariwal), Maharashtra (Mumbai), Gujarat (Jamnagar, Ahmedabad), Rajasthan (Bikaner, Jaipur), and Uttar Pradesh (Mirzapur, Bhadohi - world-renowned for hand-knotted woollen carpets).\n\n**C. Synthetic (Man-Made) Fibre Industry `(કૃત્રિમ કાપડ / सिंथेटिक वस्त्र)`:**\n*   Made from chemical polymers and petrochemical by-products (Nylon, Polyester, Acrylic, Rayon).\n*   **Advantages:** Extremely strong, crease-resistant `(કરચલી મુક્ત / शिकन-मुक्त)`, durable, lustrous, easy to wash, and highly cost-effective.\n*   Major hubs: **Surat** (India's synthetic and artificial silk capital), Mumbai, Ahmedabad, Gwalior, Modinagar.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "Which river basin hosts the highest concentration of Jute Textile mills in India?",
            "options": [
                "Sabarmati Basin (Gujarat)",
                "Hugli Basin (West Bengal)",
                "Cauvery Basin (Tamil Nadu)",
                "Narmada Basin (Madhya Pradesh)"
            ],
            "correct_answer": "Hugli Basin (West Bengal)",
            "explanation": "The Hugli River basin in West Bengal offers abundant water for jute retting, proximity to raw jute fields, cheap labor from WB/Bihar, and Kolkata port export facilities."
        },
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    # =========================================================================
    # MODULE 4: AGRO-BASED SUGAR & PAPER INDUSTRIES
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "Why can't you build a sugar factory in the Himalayas or store cut sugarcane for months before crushing it? \n\nBecause sugarcane is **weight-losing `(વજન ઘટતો કાચો માલ / भार-ह्रासी कच्चा माल)`** and its sucrose content `(ખાંડનું પ્રમાણ / सुक्रोज की मात्रा)` rapidly evaporates if not crushed within 24 hours of harvesting!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "title": "4.1 The Sugar Industry (ખાંડ ઉદ્યોગ)",
        "content": "India ranks **second** in world sugar production, but holds the **first position** in the production of Gur `(ગોળ / गुड़)` and Khandsari `(ખાંડસરી)`.\n\n**Unique Characteristics of Sugar Raw Material:**\n1.  Sugarcane is bulky and heavy.\n2.  It is a weight-losing raw material; hauling it over long distances increases transportation costs.\n3.  Sucrose content begins decreasing rapidly after cutting due to fermentation.\n4.  Therefore, sugar mills MUST be located in the immediate vicinity of sugarcane-producing farms!\n\n**The Great Shift from North to South & Western India (Board Exam High-Yield Concept):**\nIn recent decades, there has been a prominent shift and concentration of sugar mills from Uttar Pradesh/Bihar towards **Maharashtra, Gujarat, Karnataka, and Tamil Nadu**.\n\n*Why?*\n1.  **Higher Sucrose Content:** Tropical maritime climate of southern and western India produces cane with substantially higher sugar percentage.\n2.  **Longer Crushing Season `(પિલાણની લાંબી મોસમ / पेराई का लंबा मौसम)`:** The cooler, coastal maritime climate keeps the sugarcane fresh for a much longer period compared to North India's scorching dry summer.\n3.  **Success of Cooperatives:** Sugar mills in Maharashtra and Gujarat are largely managed by highly organized, efficient **Cooperative Societies `(સહકારી મંડળીઓ / सहकारी समितियां)`**.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "title": "4.2 The Paper Industry (કાગળ ઉદ્યોગ)",
        "content": "Paper is made from softwood trees `(નરમ પોચું લાકડું / नरम लकड़ी)`, bamboo `(વાંસ / बांस)`, wild grass, sugarcane bagasse `(શેરડીના કૂચા / गन्ने की खोई)`, and recycled waste paper.\n\n*   **Major Paper Producing States:** Maharashtra, West Bengal, Andhra Pradesh, Madhya Pradesh, Odisha, Tamil Nadu, and Gujarat.\n*   **Paper Industry in Gujarat:** Highly developed in **Ahmedabad, Vadodara, Surat, Vapi, Valsad, Rajkot, and Bharuch** utilizing bagasse from sugar mills and modern recycling plants.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "Why is the sugar industry shifting towards southern and western states like Maharashtra and Gujarat?",
            "options": [
                "Sugarcane grown there has higher sucrose content and the cooler climate allows a longer crushing season.",
                "North India has banned the cultivation of sugarcane.",
                "Southern states have lower land costs and no water requirements.",
                "Sugar is only consumed in coastal regions."
            ],
            "correct_answer": "Sugarcane grown there has higher sucrose content and the cooler climate allows a longer crushing season.",
            "explanation": "Tropical climate in South/Western India increases sucrose content in cane, cooler coastal weather prevents sucrose drying up, and cooperative management is highly successful."
        },
        "difficulty": "Intermediate",
        "bloom": "Analyze"
    })
    
    # =========================================================================
    # MODULE 5: MINERAL-BASED INDUSTRIES - IRON & STEEL (THE MOTHER INDUSTRY)
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "Look at the gigantic suspension bridges, skyscraper frames, railway locomotives, surgical needles, and military tanks. What do all of these have in common?\n\nThey are all forged from **Steel `(પોલાદ / इस्पात)`**! The Iron and Steel industry is called the **\"Basic or Mother Industry `(મૂળભૂત / આધારભૂત ઉદ્યોગ / आधारभूत उद्योग)`\"** because every other industry (heavy, medium, and light) depends on it for its machines and structural foundation!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "The Exact Raw Material Proportions Required in Iron and Steel Smelting.",
        "image_url": "assets/images/ss_ch13_iron_steel_ratio.jpg",
        "alt_text": "Diagram showing 4 parts Iron Ore + 2 parts Coking Coal + 1 part Limestone + Manganese -> Blast Furnace -> Pig Iron -> Steel."
    })
    
    blocks.append({
        "type": "theory",
        "title": "5.1 Raw Material Equation & Smelting Process",
        "content": "The production of steel requires heavy, bulky raw materials in a strict scientific weight ratio:\n\n$$\\text{Iron Ore } : \\text{ Coking Coal } : \\text{ Limestone} \\approx \\mathbf{4 : 2 : 1}$$\n\n*   **Iron Ore `(કાચું લોખંડ / लौહ अयस्क)` (4 parts):** Provides iron content.\n*   **Coking Coal `(કોકિંગ કોલસો / कोकिंग कोयला)` (2 parts):** Provides intense heat to melt the ore in the blast furnace `(વાતભઠ્ઠી / वात्या भट्टी)`.\n*   **Limestone `(ચૂનાનો પથ્થર / चूना पत्थर)` (1 part):** Acts as a fluxing agent `(સ્લેગ દૂર કરનાર પદાર્થ / गालक)` to remove impurities.\n*   **Manganese `(મેંગેનીઝ / मैंगनीज)`:** A small quantity is added to harden and toughen the molten steel.\n\nBecause all raw materials and finished steel are heavy and bulky, iron and steel plants MUST be located near coalfields and iron ore deposits with an efficient heavy railway transportation network.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "title": "5.2 Historical Milestones & Major Public Sector Steel Plants",
        "content": "**Historical Landmarks:**\n*   The first modern iron manufacturing unit in India was set up at **Porto Novo (Tamil Nadu) in 1830**, but failed.\n*   The first successful modern iron plant was established at **Kulti (West Bengal) in 1874** (Barakar Iron Works).\n*   The true foundation of modern large-scale steel production was laid when Jamshedji Tata established **TISCO (Tata Iron and Steel Company) at Jamshedpur (Jharkhand) in 1907**.\n\n**Major Steel Plants in India:**\n1.  **Jamshedpur (Jharkhand):** TISCO (Private Sector, near Subarnarekha and Kharkai rivers).\n2.  **Bhilai (Chhattisgarh):** Built with Russian collaboration; uses Dalli-Rajhara iron ore and Korba coal.\n3.  **Rourkela (Odisha):** Built with German collaboration; on Brahmani river.\n4.  **Durgapur (West Bengal):** Built with British collaboration; uses Raniganj coal.\n5.  **Bokaro (Jharkhand):** Built with Russian collaboration.\n6.  **Visakhapatnam (Andhra Pradesh):** Modern shore-based integrated steel plant.\n7.  **Salem (Tamil Nadu) & Bhadravati (Karnataka - VISL):** Major South Indian plants.\n\n*   Most Public Sector steel plants market their steel through **SAIL (Steel Authority of India Limited)**.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM 3-MARK QUESTION:** *\"Why is the Chhotanagpur Plateau region known as the Steel Hub of India?\"*\n\n**4 Core Geographical Reasons:**\n1.  **Low Cost of Iron Ore:** Located right beside high-grade hematite iron ore mines in Odisha and Jharkhand (Singhbhum, Mayurbhanj, Keonjhar).\n2.  **High-Grade Coking Coal in Close Proximity:** Jharia, Raniganj, and Bokaro coalfields are adjacent.\n3.  **Limestone & Dolomite Abundance:** Plentiful deposits in Palamu, Sundargarh, and Bilaspur.\n4.  **Cheap Tribal & Rural Labour:** Abundant low-cost manual workforce from Jharkhand, Bihar, and Odisha.\n5.  **Vast Market & Rail Connectivity:** Dense network of South Eastern Railways connecting to the Kolkata port and national industrial markets.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "What is the approximate weight ratio of Iron Ore : Coking Coal : Limestone required to manufacture steel?",
            "options": [
                "1 : 1 : 1",
                "4 : 2 : 1",
                "8 : 4 : 2",
                "2 : 4 : 1"
            ],
            "correct_answer": "4 : 2 : 1",
            "explanation": "To manufacture steel, roughly 4 tonnes of iron ore, 2 tonnes of coking coal, and 1 tonne of limestone are required in a blast furnace, alongside manganese for hardening."
        },
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })
    
    # =========================================================================
    # MODULE 6: METALLURGICAL, CHEMICAL & FERTILIZER INDUSTRIES
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "Did you know that without **Aluminium `(એલ્યુમિનિયમ / एल्युमिनियम)`**, modern aviation would be impossible because steel is too heavy? \nAnd did you know that India imports **100%** of its Potash fertilizers because our soil has zero commercially exploitable potash reserves? \n\nLet's discover India's dynamic metallurgical, chemical, and fertilizer industries!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "title": "6.1 Aluminium Smelting & Copper Smelting",
        "content": "**A. Aluminium Smelting `(એલ્યુમિનિયમ ગાળણ ઉદ્યોગ / एल्युमिनियम प्रगलन)`:**\n*   Aluminium is the **second most important metallurgical industry** in India.\n*   **Properties:** Light in weight, corrosion resistant `(કાટ લાગતો નથી / संक्षारण रोधी)`, exceptional conductor of electricity and heat, highly malleable `(ટીપી શકાય તેવું / लचीला)`, and becomes rock-hard when alloyed with other metals (Duralumin).\n*   **Raw Material:** **Bauxite `(બૉક્સાઇટ / बॉक्साइट)`** (4 to 6 tonnes of bauxite ⟶ 2 tonnes of alumina ⟶ 1 tonne of aluminium).\n*   **Two Critical Locational Factors:**\n    1.  Regular, assured, low-cost supply of massive electrical power (electricity accounts for 30-40% of production cost).\n    2.  Assured source of high-grade raw material (bauxite) at minimal transport cost.\n*   **Major Smelting Plants:** **NALCO** and **HINDALCO** (Odisha), West Bengal, Uttar Pradesh (Renukoot), Chhattisgarh (Korba), Maharashtra, and Tamil Nadu.\n\n**B. Copper Smelting `(તાંબુ ગાળણ ઉદ્યોગ / तांबा प्रगलन)`:**\n*   Copper is ductile, malleable, and an excellent electrical conductor.\n*   Operated primarily by **Hindustan Copper Limited (HCL)** in Ghatsila (Jharkhand) and Khetri (Rajasthan). Gujarat also houses large private copper smelters in **Jhagadia (Bharuch)**.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "title": "6.2 The Chemical Industry (રાસાયણિક ઉદ્યોગ) - Gujarat's Superpower!",
        "content": "The chemical industry in India is fast-growing, highly diversified, and contributes significantly to GDP. It is split into two major branches:\n\n*   **1. Inorganic Chemicals `(અકાર્બનિક રસાયણો / अकार्बनिक रसायन)`:**\n    *   **Sulphuric Acid `(સલ્ફ્યુરિક એસિડ)`:** Used to manufacture fertilizers, synthetic fibers, plastics, paints, dyes.\n    *   **Nitric Acid & Alkalies:** Used in metallurgy, explosives.\n    *   **Soda Ash `(સોડા એશ / धावन सोडा)`:** Used to manufacture glass, soaps, detergents, paper.\n    *   **Caustic Soda `(કોસ્ટિક સોડા)`:** Used in textiles, paper, petroleum refining.\n*   **2. Organic Chemicals `(કાર્બનિક રસાયણો / कार्बनिक रसायन)`:**\n    *   Derived from **Petrochemicals `(પેટ્રોકેમિકલ્સ / पेट्रोकेमिकल्स)`**.\n    *   Used to manufacture synthetic fibers, synthetic rubber, plastics, dye-stuffs, pharmaceuticals, and drugs.\n\n🌟 **Gujarat's Supreme Dominance:**\nGujarat is the undisputed **Chemical and Petrochemical Capital of India**! Major clusters flourish in **Vadodara, Ankleshwar, Bharuch, Dahej (PCPIR region), Surat, Vapi, and Ahmedabad**.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "title": "6.3 The Fertilizer Industry (રાસાયણિક ખાતર ઉદ્યોગ)",
        "content": "The fertilizer industry produces three major plant nutrients:\n1.  **Nitrogenous Fertilizers `(નાઇટ્રોજનયુક્ત ખાતરો / नाइट्रोजनी उर्वरक)`:** Mainly **Urea `(યુરિયા)`** (India is the 3rd largest producer of nitrogenous fertilizers).\n2.  **Phosphatic Fertilizers `(ફોસ્ફેટિક ખાતરો / फॉस्फेटिक उर्वरक)`:** e.g., Diammonium Phosphate (**DAP**).\n3.  **Complex Fertilizers `(સંયુક્ત ખાતરો / मिश्रित उर्वरક)`:** Combination of Nitrogen (N), Phosphate (P), and Potash (K).\n\n⚠️ **Critical Exam Fact on Potash:**\nIndia does **NOT** have any commercial reserves of commercially exploitable **Potash `(પોટાશ / पोटाश)`** or potassium compounds. Therefore, India imports **100% of its Potash requirement** from abroad!\n\n**Post-Green Revolution Expansion:**\nAfter the Green Revolution, fertilizer factories mushroomed across agricultural states.\n*   **Gujarat Leads India:** Mega fertilizer plants located at **Kalol, Hazira, Bharuch, Vadodara, Kandla** operated by giants like **IFFCO, KRIBHCO, GSFC (Gujarat State Fertilizers & Chemicals), and GNFC (Gujarat Narmada Valley Fertilizers & Chemicals)**.",
        "difficulty": "Advanced",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "Which of the following fertilizers is 100% imported by India due to complete lack of indigenous commercial reserves?",
            "options": [
                "Urea (Nitrogenous)",
                "Diammonium Phosphate (DAP)",
                "Potash (Potassium)",
                "Ammonium Sulphate"
            ],
            "correct_answer": "Potash (Potassium)",
            "explanation": "India has no commercially exploitable reserves of potassium compounds or potash; hence 100% of our potash requirement is imported from countries like Russia, Canada, and Jordan."
        },
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })
    
    # =========================================================================
    # MODULE 7: CEMENT, TRANSPORT EQUIPMENT & IT / ELECTRONICS
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "How did Bengaluru transform from a quiet garden city into the vibrant **Silicon Valley of India `(ભારતની સિલિકોન વેલી / भारत की सिलिकॉन वैली)`**? \nAnd how does Gujarat export millions of tonnes of world-class cement to the Middle East and Africa?\n\nLet's explore Cement, Transport Equipment, and the Hi-Tech Electronic Revolution!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "title": "7.1 The Cement Industry (સિમેન્ટ ઉદ્યોગ)",
        "content": "Cement is indispensable for modern construction: building houses, factories, bridges, highways, airports, dams, and modern urban infrastructure.\n\n*   **Raw Materials Required:** Bulky and heavy minerals: **Limestone `(ચૂનાનો પથ્થર / चूना पत्थर)`**, **Silica `(સિલિકા / सिलिका)`**, **Alumina `(એલ્યુમિના / एल्युमिना)`**, and **Gypsum `(ચિરોડી / जिप्सम)`**, alongside heavy supplies of coal and electricity.\n*   **First Cement Plant in India:** Established at **Chennai in 1904**.\n*   **Gujarat's Cement Glory:** Gujarat has achieved phenomenal progress in the cement industry due to vast coastal limestone reserves and direct sea-port access to export cement to Gulf and African nations (e.g., Sikka, Porbandar, Veraval, Dwarka, Ranavav).",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "theory",
        "title": "7.2 Transport Equipment Industry (વાહનવ્યવહાર ઉપકરણ ઉદ્યોગ)",
        "content": "**A. Automobile Industry `(ઓટોમોબાઇલ ઉદ્યોગ / ऑटोमोबाइल उद्योग)`:**\n*   Manufactures trucks, buses, cars, motorcycles, scooters, electric vehicles, and multi-utility vehicles.\n*   Major Hubs: Delhi-Gurugram-Faridabad, Mumbai-Pune, Chennai (Detroit of India), Kolkata, Lucknow, Indore, Hyderabad, Bengaluru, and **Sanand (Gujarat - the emerging auto mega-cluster producing cars like Tata and semiconductor units)**.\n\n**B. Railway Equipment `(રેલવે ઉપકરણ / रेलवे उपकरण)`:**\n*   **Locomotives (Engines):** Chittaranjan Locomotive Works (Electric), Diesel Locomotive Works (Varanasi), Diesel-Loco Modernisation Works (Patiala).\n*   **Passenger Coaches (ડબ્બા):** Integral Coach Factory (ICF, Perambur near Chennai - maker of Vande Bharat trains!), Rail Coach Factory (Kapurthala, Punjab), Modern Coach Factory (Raebareli).\n\n**C. Shipbuilding & Aviation `(વહાણ બાંધકામ અને વિમાન ઉદ્યોગ / जहाज निर्माण एवं विमान उद्योग)`:**\n*   **Major Shipyards:** Visakhapatnam (Hindustan Shipyard), Kolkata (Garden Reach), Mumbai (Mazagon Dock), Kochi (Cochin Shipyard), and Marmagao (Goa).\n*   **Aircraft:** Manufactured by **HAL (Hindustan Aeronautics Limited)** at Bengaluru, Nashik, Koraput, Hyderabad, and Kanpur.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "title": "7.3 Electronic & Information Technology Industry (ઇલેક્ટ્રોનિક્સ અને આઇટી ઉદ્યોગ)",
        "content": "The electronics industry spans everything from tiny transistor sets to television, radars, cellular telecom, computers, and supercomputing servers.\n\n*   **Bengaluru:** Crowned as the **Electronic Capital of India** (India's Silicon Valley).\n*   **Other Major Electronic & IT Hubs:** Hyderabad, Pune, Mumbai, Chennai, Delhi-Noida, Gurugram, Kolkata, and **Gandhinagar/Ahmedabad (GIFT City - Gujarat International Finance Tec-City)**.\n*   **Major Economic Impacts:**\n    1.  **Massive Employment Generation:** Millions of software engineers, data analysts, and BPO professionals.\n    2.  **Women Empowerment:** Over **30% of the workforce** in the IT-BPO sector consists of women.\n    3.  **Foreign Exchange Dynamo:** Constant inflow of international software export earnings.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "Which Indian city is celebrated as the 'Electronic Capital' and 'Silicon Valley' of India?",
            "options": [
                "Hyderabad",
                "Bengaluru",
                "Ahmedabad",
                "Chennai"
            ],
            "correct_answer": "Bengaluru",
            "explanation": "Bengaluru is recognized globally as the Electronic Capital and Silicon Valley of India due to its vast cluster of hardware and IT software industries."
        },
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    # =========================================================================
    # MODULE 8: INDUSTRIAL POLLUTION & ENVIRONMENTAL DEGRADATION
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "On the chilly night of **December 2, 1984**, a deadly gas cloud of Methyl Isocyanate (MIC) leaked from the Union Carbide pesticide plant in **Bhopal**, killing thousands of innocent sleeping citizens in India's worst industrial disaster.\n\nWhile industries bring wealth and technology, unchecked industrialization releases devastating toxins into our air, rivers, and soil. Let's analyze the **4 Pillars of Industrial Pollution**!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "The 4 Types of Industrial Pollution Damaging the Biosphere.",
        "image_url": "assets/images/ss_ch13_four_pollutions.jpg",
        "alt_text": "Illustration showing Air Pollution, Water Pollution, Thermal Pollution, and Noise Pollution caused by factories."
    })
    
    blocks.append({
        "type": "theory",
        "title": "8.1 The Four Types of Industrial Pollution",
        "content": "Industries are responsible for 4 primary types of environmental pollution:\n\n**1. Air Pollution `(હવા પ્રદૂષણ / वायु प्रदूषण)`:**\n*   Caused by the presence of a high proportion of undesirable and toxic gases like **Sulphur Dioxide ($SO_2$)** and **Carbon Monoxide ($CO$)**.\n*   Airborne particulate materials include both solid dust particles and liquid spray/mist emitted by chemical plants, brick kilns, oil refineries, and metallurgical smelting plants.\n*   *Effects:* Chronic respiratory illnesses, asthma, bronchitis, acid rain `(એસિડ વર્ષા / अम्ल वर्षा)`, and global warming.\n\n**2. Water Pollution `(જળ પ્રદૂષણ / जल प्रदूषण)`:**\n*   Caused by the direct discharge of untreated organic and inorganic industrial wastes and toxic effluents into rivers, lakes, and oceans.\n*   Major Culprits: Paper, pulp, chemical, textile, dyeing, petroleum refinery, tannery, and electroplating industries.\n*   *Toxic Pollutants:* Dyes, detergents, acids, salts, heavy toxic metals like **Lead `(સીસું / सीसा)`**, **Mercury `(પારો / पारा)`**, and synthetic pesticides.\n\n**3. Thermal Pollution `(તાપીય પ્રદૂષણ / तापीय प्रदूषण)`:**\n*   Occurs when scalding hot water from thermal power plants, nuclear plants, and factories is drained directly into rivers, lakes, and estuaries before being cooled.\n*   *Effects:* Drastically reduces dissolved oxygen ($DO$), killing aquatic life, fish larvae, and disrupting river ecology. Nuclear plant effluents cause cancers and severe birth defects.\n\n**4. Noise Pollution `(ધ્વનિ પ્રદૂષણ / ध्वनि प्रदूषण)`:**\n*   Caused by heavy industrial machinery, pneumatic drills, sirens, blast furnaces, diesel generators, and metal stamping.\n*   *Effects:* Permanent hearing impairment, high blood pressure, sleep disorders, severe stress, and mental fatigue.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "case_study",
        "content": "🧪 **Historical Environmental Case Study: The Bhopal Gas Tragedy (1984)**\n*   **Event:** Leakage of ~40 tonnes of toxic **Methyl Isocyanate (MIC) `(મિથાઈલ આઇસોસાયનાઇડ)`** gas from the Union Carbide pesticide factory in Bhopal on December 2-3, 1984.\n*   **Root Causes:** Defective safety valves, neglected maintenance, refrigeration system switched off to cut costs, and proximity of dense residential slums around hazardous chemical tanks.\n*   **Crucial Lesson:** Enforce strict industrial zoning laws `(ઔદ્યોગિક ઝોનિંગ કાયદા / औद्योगिक ज़ोनिंग नियम)`, mandatory regular safety audits, zero-tolerance storage regulations, and automatic gas-scrubbing alarms.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "Draining scalding hot water from factories and thermal plants directly into rivers without cooling causes which type of pollution?",
            "options": [
                "Noise Pollution",
                "Thermal Pollution",
                "Air Pollution",
                "Solid Waste Pollution"
            ],
            "correct_answer": "Thermal Pollution",
            "explanation": "Discharging hot water into river streams increases water temperature and depletes dissolved oxygen, causing Thermal Pollution which destroys aquatic ecosystems."
        },
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    # =========================================================================
    # MODULE 9: CONTROL OF ENVIRONMENTAL DEGRADATION & SUSTAINABLE DEVELOPMENT
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "Can an industrial plant run at full capacity and still keep its surrounding rivers crystal clear and air fresh? \n**YES!** Sustainable industrial development `(ટકાઉ ઔદ્યોગિક વિકાસ / सतत पोषणीय औद्योगिक विकास)` is not a dream—it is an engineering science practiced through the **3-Tier Effluent Treatment** and **NTPC Eco-Management Model**!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "title": "9.1 Practical Measures to Control Industrial Pollution (Board Master Answer)",
        "content": "How can industries control and eliminate environmental degradation?\n\n**A. Water Conservation & Treatment (The 3-Step Treatment Process):**\n1.  **Minimizing Water Use:** Reusing and recycling industrial water in successive production cycles.\n2.  **Rainwater Harvesting `(વરસાદી પાણીનો સંગ્રહ / वर्षा जल संचयन)`:** Harvesting rainwater to meet industrial processing and cooling needs.\n3.  **Treatment of Industrial Effluents before River Discharge:**\n    *   *Primary Treatment:* Mechanical screening, grinding, flocculation, and sedimentation to remove solid debris.\n    *   *Secondary Treatment:* Biological treatment using aerobic bacteria to decompose organic wastes.\n    *   *Tertiary Treatment:* Advanced biological, chemical, and physical processes (reverse osmosis, UV disinfection, neutralisation) to recycle treated water.\n\n**B. Air Pollution Control:**\n*   Fitting smoke stacks with **Electrostatic Precipitators `(ઇલેક્ટ્રોસ્ટેટિક પ્રેસિપિટેટર્સ)`**, fabric filters, wet scrubbers, and inertial separators to trap toxic particulate dust.\n*   Replacing polluting coal with clean fuels like **Natural Gas (PNG/CNG)** or green hydrogen.\n\n**C. Noise Pollution Control:**\n*   Fitting industrial machinery and diesel generators with high-efficiency **Silencers `(સાયલેન્સર્સ)`**.\n*   Redesigning equipment to reduce friction and mandating noise-absorbing earplugs for factory workers.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "title": "9.2 The NTPC Green Model (National Thermal Power Corporation)",
        "content": "**NTPC** is a major power generating corporation in India holding **ISO 14001 certification** for Environmental Management Systems.\n\n**NTPC's 5-Point Proactive Eco-Strategy:**\n1.  **Optimum Equipment Utilization:** Modernizing power generating equipment and adopting the latest eco-friendly combustion technologies.\n2.  **Minimizing Waste Generation & Ash Utilization:** Maximizing the utilization of fly ash `(ફ્લાય એશ / राख का उपयोग)` to make cement and bricks.\n3.  **Developing Green Belts `(ગ્રીન બેલ્ટ / हरित पट्टियां)`:** Afforesting extensive green belts around thermal power stations to absorb CO₂ and maintain ecological balance.\n4.  **Ash Pond Management & Water Recycling:** Efficient ash slurry water recycling systems to prevent soil and groundwater contamination.\n5.  **Real-Time Ecological Monitoring:** Continuous online ecological data monitoring and review across all power stations.",
        "difficulty": "Advanced",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM 5-MARK LONG ANSWER BLUEPRINT:** *\"Discuss the steps to be taken to minimize environmental degradation caused by industries.\"*\n\n**Structure Your Answer with these 5 Clear Headings:**\n1.  **Water Management:** 3-tier effluent treatment (Primary, Secondary, Tertiary) and rainwater harvesting.\n2.  **Air Quality Control:** Electrostatic precipitators, bag filters, and switching from coal to natural gas.\n3.  **Noise Abatement:** Generator silencers, acoustic soundproofing, regular machinery lubrication.\n4.  **Solid Waste Utilization:** Fly ash utilization in brick manufacturing and slag utilization in cement.\n5.  **Green Belt Plantation:** Compulsory planting of dense tree belts around all industrial units (NTPC guidelines).",
        "difficulty": "Advanced",
        "bloom": "Create"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "Which device is fitted in factory chimneys and smoke stacks to magnetically trap and remove fine solid particulate matter from emissions?",
            "options": [
                "Silencer",
                "Electrostatic Precipitator",
                "Barometer",
                "Catalytic Converter"
            ],
            "correct_answer": "Electrostatic Precipitator",
            "explanation": "Electrostatic Precipitators use high-voltage electrostatic charges to remove fine soot, dust, and particulate matter from industrial chimney smoke before it enters the atmosphere."
        },
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })
    
    # =========================================================================
    # MODULE 10: BOARD MASTER REVISION & HIGH-YIELD SUMMARY TABLE
    # =========================================================================
    blocks.append({
        "type": "summary",
        "title": "Chapter 13: Supreme High-Yield Quick Revision Table",
        "content": "| Industry Name | Raw Material Type | Key Indian Clusters | Gujarat Special Highlights |\n| :--- | :--- | :--- | :--- |\n| **Cotton Textile** | Agro-based | Mumbai (Cottonopolis), Ahmedabad, Coimbatore | Ahmedabad ('Manchester of the East'), Surat |\n| **Jute Textile** | Agro-based | Hugli Basin (West Bengal) - 1st mill Rishra 1855 | Biodegradable packaging demand |\n| **Sugar Industry** | Agro-based (Weight losing) | Maharashtra, UP, Karnataka, Tamil Nadu | High sucrose cane & cooperative sugar mills |\n| **Iron & Steel** | Mineral-based ($4:2:1$) | Chhotanagpur Plateau (TISCO Jamshedpur, Bhilai, Rourkela, Durgapur, Bokaro) | Steel processing & engineering hubs |\n| **Aluminium Smelting**| Mineral-based (Bauxite) | Odisha (NALCO, HINDALCO), Chhattisgarh, UP | Lightweight alloys for transport/industry |\n| **Chemical Industry** | Mineral & Petrochemicals | Gujarat, Maharashtra, Tamil Nadu | Gujarat #1 in India (Ankleshwar, Dahej, Vapi) |\n| **Fertilizers** | Chemical (100% Potash imported) | Gujarat, UP, Tamil Nadu, Punjab | Mega plants: IFFCO, KRIBHCO, GSFC, GNFC |\n| **Cement Industry** | Mineral (Limestone, Gypsum) | Madhya Pradesh, Rajasthan, Andhra, Gujarat | Coastal plants exporting to Gulf/Africa |\n| **Automobile** | Heavy Engineering | Chennai, Gurugram, Pune, Sanand | Sanand (Mega Auto & EV Hub) |\n| **Electronic & IT** | Silicon / Software | Bengaluru (Silicon Valley), Hyderabad, Pune | GIFT City Gandhinagar (Fintech Hub) |",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "reflection",
        "content": "🤔 **Chief Architect's Socratic Reflection Challenge:** \nImagine you are appointed as the Industrial Development Minister of Gujarat. \n1. How would you balance aggressive industrial expansion with zero environmental pollution (Zero Liquid Discharge)?\n2. Which future green industries (like Green Hydrogen, Solar Panels, Semiconductor Chips at Dholera/Sanand) would you prioritize to lead India's next 25 years of manufacturing?",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })
    
    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    # Save to GSEB target path
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_social_science_ch13.json"
    os.makedirs(os.path.dirname(gseb_path), exist_ok=True)
    with open(gseb_path, "w", encoding="utf-8") as f:
        json.dump(final_json, f, indent=2, ensure_ascii=False)
    print(f"Generated GSEB Chapter JSON at: {gseb_path}")
    
    # Save to NCERT target path
    ncert_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_social_science_ch13.json"
    final_json["metadata"]["id"] = "ncert_class10_social_science_ch13"
    with open(ncert_path, "w", encoding="utf-8") as f:
        json.dump(final_json, f, indent=2, ensure_ascii=False)
    print(f"Generated NCERT Chapter JSON at: {ncert_path}")

if __name__ == "__main__":
    generate_supreme_gseb_ss_ch13()
