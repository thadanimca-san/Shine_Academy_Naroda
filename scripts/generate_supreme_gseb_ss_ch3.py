import json
import os

def generate_supreme_gseb_ss_ch3():
    chapter_id = "gseb_class10_social_science_ch3"
    title = "Chapter 3: Cultural Heritage of India: Sculpture and Architecture"
    
    metadata = {
        "id": chapter_id,
        "title": title,
        "subtitle": "Ancient Town Planning, Stupas, Caves, Temples, Stepwells & Medieval Marvels",
        "subject": "Social Science",
        "grade": "10",
        "board": "GSEB / Universal",
        "curriculum": ["GSEB", "NCERT", "CBSE", "Universal"],
        "language": "English/Hindi/Gujarati (Bilingual)",
        "difficulty": "Intermediate",
        "estimated_minutes": 150,
        "version": "3.0.0-SUPREME-SS",
        "author": "Antigravity Supreme Academic Intelligence",
        "reviewed_by": "Chief Academic Architect",
        "tags": [
            "social_science",
            "class10",
            "gseb",
            "sculpture_architecture",
            "town_planning",
            "mohenjo_daro",
            "harappa",
            "dholavira",
            "lothal",
            "stupas",
            "pillars_of_ashoka",
            "sarnath_pillar",
            "cave_architecture",
            "caves_of_gujarat",
            "chariot_temples",
            "temple_architecture",
            "modhera_sun_temple",
            "stepwells_of_gujarat",
            "rani_ki_vav",
            "adalaj_vav",
            "sidi_saiyyed_jali",
            "board_special",
            "bilingual"
        ],
        "learning_outcomes": [
            "Define and distinguish clearly between Sculpture `(शिल्पकला / શિલ્પકલા)` and Architecture `(स्थापत्य / સ્થાપત્ય)`.",
            "Master the sophisticated Town Planning of the Indus Valley Civilization: Mohenjo-daro, Harappa, Dholavira, and Lothal.",
            "Explain the architectural components of Buddhist Stupas `(હર્મિકા, મેધી, પ્રદક્ષિણા પથ, તોરણ)` and the Lion Capital of Sarnath `(સારનાથનો સિંહસ્તંભ)`.",
            "Analyze Ancient Cave Architecture across India (Ajanta, Ellora, Elephanta) and the distinctive rock-cut Caves of Gujarat `(જૂનાગઢ, તળાજા, સાણા, ખંભાલીડા, કડિયા ડુંગર)`.",
            "Understand the monolithic Chariot Temples `(રથ મંદિરો)` of Mahabalipuram and glorious Hindu Temple Architecture (Modhera Sun Temple, Konark, Brihadeeshwara).",
            "Examine Medieval Architecture, Islamic monuments `(સિદી સૈયદની જાળી, ઝૂલતા મિનારા)`, and the unique Stepwells `(વાવ સ્થાપત્ય)` of Gujarat (Rani ki Vav, Adalaj Vav).",
            "Excel in Board Exam MCQs, architectural distinction tables, structural diagrams, and high-yield structured questions."
        ],
        "ai_context": {
            "learning_goal": "Equip students with supreme mastery over India's sculpture, ancient town planning, stupas, cave complexes, temples, and stepwells using vivid blueprints, memory tricks, and bilingual terminology.",
            "common_misconceptions": [
                "Students confuse Sculpture (art of carving feelings with chisel/hammer) with Architecture (art of construction/Vastu).",
                "Students confuse Dholavira's Rainwater Harvesting with Lothal's Tidal Dockyard.",
                "Students confuse the 4 types of Stepwells (Nanda=1, Bhadra=2, Jaya=3, Vijaya=4 entrances) with number of storeys.",
                "Students mix up parts of a Stupa (Harmika, Medhi, Toran) with parts of a Temple (Garbhagriha, Mandapa, Shikhara, Gopuram)."
            ],
            "tutor_hint": "Anchor concepts in real engineering: Mohenjo-daro had covered underground drainage 4,500 years ago! For stepwell types, use mnemonic N-B-J-V (1-2-3-4 entrances). For Modhera Sun Temple, emphasize Bhimdev I (1026 AD), Iranian style, and the 108 shrines around Suryakund."
        }
    }
    
    blocks = []
    
    # ==========================================
    # MODULE 1: SCULPTURE VS ARCHITECTURE
    # ==========================================
    blocks.append({
        "type": "hook",
        "title": "The Art of Breathing Life into Stone & Constructing Timeless Cities",
        "content": "Imagine standing in front of a cold, silent block of rock. With nothing more than a chisel and a hammer `(ટાંકણું અને હથોડી / छेनी और हथौड़ी)`, an ancient artist chips away until a lifelike goddess or a roaring lion emerges! At the same time, ancient Indian engineers planned cities with double-storey brick houses, wide paved roads, and covered underground sewers `(ગટર વ્યવસ્થા / भूमिगत जल निकासी)` over **4,500 years ago** when most of the world lived in primitive huts.\n\nWelcome to **Chapter 3: Sculpture and Architecture `(શિલ્પ અને સ્થાપત્ય / शिल्प और स्थापत्यकला)`**—where we discover the artistic genius and unmatched engineering skills of ancient India!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "definition",
        "title": "1. What is Sculpture? (શિલ્પકલા / शिल्पकला)",
        "content": "**Sculpture `(શિલ્પકલા / शिल्पकલા)`** is the art of shaping and carving one's feelings, emotions, ideas, and aesthetic beauty on **stone `(પથ્થર / पत्थर)`**, **wood `(લાકડું / लकड़ी)`**, or **clay `(માટી / मिट्टी)`** using a **chisel and hammer `(ટાંકણું અને હથોડી / छेनी और हथौड़ी)`**.\n\n- The artist who carves the sculpture is known as a **Shilpi / Sculptor `(શિલ્પી / मूर्तिकार)`**.\n- Sculptures capture human, animal, divine, and abstract figures with deep aesthetic expressions.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "definition",
        "title": "2. What is Architecture? (સ્થાપત્ય / वास्तुकला)",
        "content": "In simple terms, **Architecture `(સ્થાપત્ય / वास्तुकલા)`** means the **art of construction `(બાંધકામ કરવાની કળા / निर्माण कला)`**.\n\n### Etymology & Root Meaning:\n- In Sanskrit, architecture is called **'Vastu' `(વાસ્તુ / वास्तु)`**, which is derived from the root word meaning **'to reside / to dwell' `(વસવાટ કરવો / निवास करना)`**.\n- Ancient Indian scriptures like *Vastu Shastra* govern the sacred rules for constructing dwellings, palaces, and sacred spaces.\n- Architecture encompasses the design and construction of **houses `(મકાનો)`**, **towns `(નગરો)`**, **forts `(કિલ્લાઓ)`**, **temples `(મંદિરો)`**, **mosques `(મસ્જિદો)`**, **stepwells `(વાવ)`**, **bridges `(પુલ)`**, and **minarets `(મિનારા)`**.\n- The master builder/architect is known as a **Sthapati `(સ્થપતિ / वास्तुकार)`**.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "title": "Sculpture vs Architecture: The Fundamental Difference",
        "content": "```\n┌───────────────────────────────────────┬───────────────────────────────────────┐\n│         SCULPTURE (શિલ્પકલા)           │        ARCHITECTURE (સ્થાપત્ય / વાસ્તુ) │\n├───────────────────────────────────────┼───────────────────────────────────────┤\n│ • Art of carving & sculpting          │ • Art of planning & construction      │\n│ • Medium: Stone, Wood, Clay, Metal    │ • Medium: Bricks, Mortar, Stones, Wood│\n│ • Tools: Chisel & Hammer (ટાંકણું-હથોડી)│ • Tools: Engineering, Masonry, Design │\n│ • Creator: Shilpi (શિલ્પી / मूर्तिकार)  │ • Creator: Sthapati (સ્થપતિ / वास्तुकार)│\n│ • Examples: Sarnath Lion, Nataraja    │ • Examples: Mohenjo-daro, Modhera Sun │\n│   statue, Trimurti of Elephanta       │   Temple, Rani ki Vav, Taj Mahal      │\n└───────────────────────────────────────┴───────────────────────────────────────┘\n```",
        "image_url": "assets/images/ss_ch3_sculpture_vs_architecture.jpg",
        "alt_text": "Comparison chart between Sculpture and Architecture"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "question": "The Gujarati word 'Sthapatya' (Architecture) is closely associated with which Sanskrit word meaning 'to dwell'?",
        "options": [
            "Shilpa",
            "Vastu",
            "Stupa",
            "Kala"
        ],
        "correct_answer": "Vastu",
        "correct_index": 1,
        "explanation": "In Sanskrit, architecture is called 'Vastu' (વાસ્તુ), which directly relates to dwelling or habitation (નિવાસ). A person who plans and builds is called a Sthapati (સ્થપતિ)."
    })
    
    blocks.append({
        "type": "teacher_tip",
        "title": "Teacher's Memory Trick: Shilpi vs Sthapati",
        "content": "💡 **Quick Memory Hook:**\n- **Shilpi `(શિલ્પી)`** ⟶ Holds a **Chisel & Hammer** to carve statues.\n- **Sthapati `(સ્થપતિ)`** ⟶ Draws **Blueprints** and builds structures.\n\n*Always mention the Sanskrit term 'Vastu' when defining Sthapatya in your board exam 2-mark answers!*",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    # ==========================================
    # MODULE 2: ANCIENT INDIAN TOWN PLANNING (MOHENJO-DARO & HARAPPA)
    # ==========================================
    blocks.append({
        "type": "theory",
        "title": "3. Ancient Indian Town Planning (પ્રાચીન ભારતનું નગર આયોજન)",
        "content": "Ancient India possessed extraordinary expertise in town planning. Ancient towns were divided into **Three Major Sections `(ત્રણ મુખ્ય વિભાગો / तीन प्रमुख भाग)`**:\n\n1. **Fort of Rulers (Citadel / શાસક અધિકારીઓનો ગઢ - સિટાડલ)**:\n   - Situated on the elevated **Western side `(પશ્ચિમ ભાગ)`** of the town.\n   - Enclosed by strong, tall protective fort walls `(સુરક્ષિત કિલ્લેબંધી)`.\n\n2. **Upper Town / Residences of Administrative Officers `(અન્ય અધિકારીઓના મકાનો / અન્ય પ્રશાસનિક આવાસ)`**:\n   - Situated on the upper eastern side, also fortified for safety.\n   - Contained spacious residential quarters with **2 to 5 rooms `(બે થી પાંચ ઓરડાવાળાં મકાનો)`**.\n\n3. **Lower Town / Common People's Residences `(સામાન્ય નગરજનોના આવાસ / સામાન્ય નાગરિકોના મકાન)`**:\n   - Situated on the lower ground on the **Eastern side `(પૂર્વ ભાગ)`**.\n   - Built with high-quality **burnt bricks `(હાથે ઘડેલી પાકી ઈંટો / पक्की ईंटें)`**.\n   - Constructed on elevated plinths `(ઊંચા ઓટલા / ઊંચી પીઠિકા)` to protect from dampness `(ભેજ / सीलन)` and floods `(પૂર / बाढ़)`.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "title": "4. Mohenjo-Daro Town Planning (મોહેં-જો-દડોનું નગર આયોજન)",
        "content": "In **1922**, archeologists **Rakhaldas Banerjee `(રાખાલદાસ બેનરજી)`** and **Dayaram Sahni `(દયારામ સહની)`** discovered the colossal ancient civilization of **Mohenjo-daro `(મોહેં-જો-દડો)`** in the Larkana district of Sindh (now in Pakistan) under the direction of Sir John Marshall.\n\n### Key Features of Mohenjo-Daro:\n\n#### A. Roads `(રસ્તાઓ / सड़कें)`:\n- Broad, straight roads measuring **9.75 meters wide `(૯.૭૫ મીટર પહોળા)`**.\n- Small lanes intersected main roads strictly at **90-degree right angles `(કાટખૂણે / समकोण)`**.\n- The roads were wide enough for multiple carts to pass simultaneously without congestion.\n- Pits along the roads indicate the existence of **street-lighting lamp posts `(રાત્રિ પ્રકાશ માટે થાંભલાના ખાડા)`**.\n\n#### B. Residential Houses `(મકાનો / आवास)`:\n- Houses were constructed on high plinths `(ઊંચા ઓટલા)` to protect against river floods and subsoil dampness.\n- Rich citizens lived in **double-storeyed houses with 5 to 7 rooms**, while ordinary citizens lived in **single-storeyed houses with 2 to 3 rooms**.\n- **Intelligent Privacy Design:** The main entrance of every house opened into internal side lanes `(નાની ગલીઓમાં)` rather than on the noisy main public roads.\n- Every house had its own courtyard, kitchen, well `(કૂવો)`, and bathroom `(સ્નાનાગાર)`.\n\n#### C. Underground Drainage System `(ગટર આયોજન / जल निकासी व्यवस्था)`:\n- The **most unique and crowning glory** of Mohenjo-daro town planning!\n- Such an advanced drainage system did not exist anywhere in the contemporary ancient world, except on the **Island of Crete `(ક્રીટ ટાપુ)`** in the Mediterranean Sea.\n- Every house had a **cesspool / soak pit `(ખાળકૂવો)`** for domestic waste. When waste water reached a certain level, it automatically discharged into small covered drains.\n- Small drains emptied into large master sewers, which carried sewage outside the city perimeter.\n- Drains were covered with removable stone/brick slabs with inspection holes `(કચરો સાફ કરવાના ઢાંકણાં)` to prevent blockages and airborne diseases.\n\n#### D. Public Bath `(જાહેર સ્નાનાગાર / सार्वजनिक स्नानागार)`:\n- A massive rectangular swimming pool constructed with baked bricks.\n- Plastered with **bitumen / natural asphalt `(ડામરનો લેપ / डामर का लेप)`** to make the floor and walls completely water-tight.\n- Paved steps on the North and South sides leading into the water.\n- Surrounded by small changing rooms `(ઓરડીઓ)` and supplied with fresh well water, with separate outlets to drain out used water.\n\n#### E. Public Buildings & Granaries `(જાહેર મકાનો અને અન્નભંડાર)`:\n- Huge town halls used as administrative headquarters, assemblies, and state granaries `(અનાજના કોઠારો)`.",
        "difficulty": "Intermediate",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "diagram",
        "title": "Mohenjo-Daro Town Planning Blueprint",
        "content": "```\n                           ▲ NORTH\n   ┌───────────────────────────────────────────────────────────┐\n   │                   CITADEL (શાસક ગઢ)                       │\n   │   • High Fortified Wall     • Public Bath (સ્નાનાગાર)     │\n   │   • Granaries (અનાજ કોઠાર)  • Administrative Assembly    │\n   └─────────────────────────────┬─────────────────────────────┘\n                                 │\n            9.75 m Wide Roads    │   Intersecting at 90°\n   ◄─────────────────────────────┼────────────────────────────►\n                                 │\n   ┌─────────────────────────────┴─────────────────────────────┐\n   │                 LOWER TOWN (સામાન્ય નગર)                  │\n   │   • High Plinth Brick Houses (ભેજ-પૂર રક્ષણ)               │\n   │   • Doors open in side lanes (એકાંત અને શાંતિ)             │\n   │   • Domestic Cesspools (ખાળકૂવા) ⟶ Covered Sewers (ગટર)   │\n   └───────────────────────────────────────────────────────────┘\n                           ▼ SOUTH\n```",
        "image_url": "assets/images/ss_ch3_mohenjo_daro_layout.jpg",
        "alt_text": "Architectural layout of Mohenjo-Daro Town Planning"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "question": "A drainage system identical to the sophisticated underground sewer system of Mohenjo-daro was found in which island of the Mediterranean Sea?",
        "options": [
            "Island of Sicily",
            "Island of Crete",
            "Island of Cyprus",
            "Island of Malta"
        ],
        "correct_answer": "Island of Crete",
        "correct_index": 1,
        "explanation": "Apart from the Indus Valley Civilization (Mohenjo-daro), such a contemporary sophisticated underground covered drainage system was found only on the Island of Crete (ક્રીટ ટાપુ) in the Mediterranean Sea."
    })
    
    blocks.append({
        "type": "teacher_tip",
        "title": "Teacher's Board Exam Formula: Mohenjo-Daro 4-Pillar Answer",
        "content": "💡 **4-Mark Board Question:** *\"Explain the Town Planning of Mohenjo-daro.\"*\n\n**Topper Structure (Write 4 distinct headings):**\n1. **Roads `(રસ્તાઓ)`**: 9.75 m wide, straight, 90° right angles, night lamp posts.\n2. **Houses `(મકાનો)`**: High plinth protection, 2-storey (rich) / 1-storey (poor), doors open in side lanes.\n3. **Drainage System `(ગટર આયોજન)`**: Domestic cesspools `(ખાળકૂવા)`, underground covered sewers, Crete island comparison.\n4. **Public Bath `(જાહેર સ્નાનાગાર)`**: Bitumen water-proofing, steps on North/South, changing rooms.",
        "difficulty": "Beginner",
        "bloom": "Apply"
    })

    # ==========================================
    # MODULE 3: HARAPPAN MARVELS OF GUJARAT (DHOLAVIRA & LOTHAL)
    # ==========================================
    blocks.append({
        "type": "theory",
        "title": "5. Harappan Civilization & Key Sites of Gujarat",
        "content": "In **1921**, archeologist **Dayaram Sahni `(દયારામ સહની)`** discovered the first ancient settlement of the Indus Valley at **Harappa `(હડપ્પા)`** in the Montgomery district of Punjab (near Ravi river). Hence, this entire culture is proudly named the **Harappan Civilization `(હડપ્પીય સંસ્કૃતિ)`**.\n\nGujarat holds a place of prime international pride with two world-class Harappan metropolitan centers:\n\n---\n\n### A. Dholavira `(ધોળાવીરા / धोलावीरा - Khadirbet, Kutch)`:\n- Located in **Khadirbet `(ખદીરબેટ)`**, Bhachau taluka, Kutch district, amidst the Great Rann of Kutch.\n- Systematically excavated in **1990** under the leadership of **Ravindra Singh Bisht (R.S. Bisht)** of the Archeological Survey of India.\n- **3-Tier Town Planning `(ત્રિસ્તરીય નગર રચના)`**:\n  1. Citadel (Ruler's Palace / કિલ્લો)\n  2. Upper Town (અન્ય અધિકારીઓના આવાસ)\n  3. Lower Town (સામાન્ય નગરજનોના આવાસ)\n- **White-Washed Fort Walls**: The citadel walls were fortified and painted with a radiant white clay/gypsum polish.\n- **Rainwater Harvesting & Water Management `(પાણી સંગ્રહ અને શુદ્ધિકરણની વ્યવસ્થા)`**:\n  - The most magnificent engineering feat of Dholavira!\n  - Stone-built reservoirs, stepped tanks, and channels designed to collect, filter, and conserve every single drop of rainwater in the dry desert climate.\n- **Ancient Signboard**: A grand wooden inscription board bearing **10 large Indus script characters** was discovered near the northern gateway.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "title": "6. Lothal: The World's Earliest International Port & Dockyard (લોથલ)",
        "content": "### B. Lothal `(લોથલ / लोथल - The Ancient Tidal Port)`:\n- Situated in **Dholka Taluka `(ધોળકા તાલુકો)`**, Ahmedabad district, nestled between two perennial rivers: the **Bhogavo `(ભોગાવો)`** and the **Sabarmati `(સાબરમતી)`**, 18 km from the Gulf of Khambhat.\n\n#### The World's First Engineered Tidal Dockyard `(ધક્કો / ગોદી - Dockyard)`:\n- Built with sturdy, kiln-fired baked bricks on the eastern edge of the city.\n- During high tide `(ભરતી / ज्वार)`, ocean water entered through a sluice gate channel, allowing merchant cargo ships `(વેપારી વહાણો)` to sail into the dockyard basin for safe anchorage, loading, and unloading.\n\n#### Warehouses & Industrial Bead Factory `(વખારો અને મણકાની ફેક્ટરી)`:\n- Massive raised storage warehouses `(વખારો / गोदाम)` protected valuable export goods from moisture and tides.\n- Lothal had a world-renowned **bead-making factory `(મણકા બનાવવાનું કારખાનું)`**, crafting exquisite jewelry from agate `(અકીક)`, carnelian, shell, ivory, and gold.\n- Lothal served as a prosperous **international trade port `(આંતરરાષ્ટ્રીય બંદર)`**, directly connecting ancient Gujarat to civilizations in Mesopotamia, Egypt, and the Persian Gulf.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "diagram",
        "title": "Comparison: Dholavira vs Lothal",
        "content": "```\n┌────────────────────────────────────────┬────────────────────────────────────────┐\n│         DHOLAVIRA (ધોળાવીરા)           │           LOTHAL (લોથલ)                │\n├────────────────────────────────────────┼────────────────────────────────────────┤\n│ • Location: Khadirbet, Bhachau (Kutch) │ • Location: Dholka Taluka (Ahmedabad)  │\n│ • Excavator: R.S. Bisht (1990)         │ • Excavator: S.R. Rao (1954)           │\n│ • Speciality: 3-Tier Town Planning     │ • Speciality: Earliest Tidal Dockyard  │\n│ • Marvel: Rainwater Harvesting & Tanks │ • Marvel: Brick Dockyard (ધક્કો / ગોદી)│\n│ • Key Find: 10-Letter Indus Signboard  │ • Key Find: Bead Factory & Warehouses  │\n│ • Nature: Desert Fortified Metropolis  │ • Nature: Thriving International Port  │\n└────────────────────────────────────────┴────────────────────────────────────────┘\n```",
        "image_url": "assets/images/ss_ch3_dholavira_vs_lothal.jpg",
        "alt_text": "Comparison chart between Dholavira and Lothal"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "question": "Which ancient Harappan port city in Gujarat featured a colossal brick dockyard (ધક્કો / ગોદી) used for docking ships during high tide?",
        "options": [
            "Dholavira",
            "Lothal",
            "Rangpur",
            "Rojdi"
        ],
        "correct_answer": "Lothal",
        "correct_index": 1,
        "explanation": "Lothal (in Dholka taluka, Ahmedabad) featured the world's earliest engineered tidal dockyard (ધક્કો) made of baked bricks to moor ships and facilitate international maritime trade."
    })
    
    blocks.append({
        "type": "common_mistakes",
        "title": "Common Mistake Alert: Dholavira vs Lothal",
        "content": "⚠️ **Don't Mix Up Gujarat's Harappan Marvels:**\n- **Dholavira** ⟶ Think **WATER HARVESTING & 3-TIER TOWN** in Kutch.\n- **Lothal** ⟶ Think **DOCKYARD (ધક્કો) & PORT TRADE** in Ahmedabad.\n\n*If the question asks about a 'Signboard with 10 characters', the answer is strictly Dholavira!*",
        "difficulty": "Intermediate",
        "bloom": "Analyze"
    })

    # ==========================================
    # MODULE 4: MAURYA ART: STUPAS & SARNATH LION CAPITAL
    # ==========================================
    blocks.append({
        "type": "theory",
        "title": "7. Maurya Art & Stupa Architecture (મૌર્યકાલીન કલા અને સ્તૂપ)",
        "content": "During the **Maurya Period `(મૌર્ય યુગ)`**, under the patronage of Emperor Ashoka, Indian art and sculpture reached sublime heights.\n\n### What is a Stupa? (સ્તૂપ એટલે શું?):\n- A **Stupa `(સ્તૂપ / स्तूप)`** is an oval or dome-shaped earthen/stone mound built over the sacred **bodily relics / ashes `(અસ્થિ કે અવશેષો / अस्थि-अवशेष)`** of Lord Buddha.\n\n### 5 Famous Stupas of Emperor Ashoka's Reign:\n1. **Sanchi Stupa `(સાંચીનો સ્તૂપ)`** (Madhya Pradesh) - The largest and most grand stupa.\n2. **Sarnath Stupa `(સારનાથનો સ્તૂપ - ધર્મરાજિકા)`** (Uttar Pradesh).\n3. **Nandangarh Stupa `(નંદનગઢનો સ્તૂપ - લૌરિયા)`** (Bihar).\n4. **Bairat Stupa `(બૈરાટનો સ્તૂપ)`** (Rajasthan).\n5. **Stupas in Gujarat**: **Devni Mori Stupa `(દેવની મોરીનો સ્તૂપ - શામળાજી નજીક, અરવલ્લી)`**, and stupas near Girnar (Intwa/Junagadh).\n\n---\n\n### 4 Essential Structural Components of a Stupa `(સ્તૂપના મુખ્ય ૪ અંગો)`:\n1. **Harmika `(હર્મિકા)`**:\n   - The square railing or balcony-like structure situated on the **very top of the dome `(અંડાકાર ટોચ પર)`** enclosing the sacred relic casket.\n2. **Medhi `(મેધી)`**:\n   - The elevated circular platform or terrace around the base of the stupa used for circumambulation.\n3. **Pradakshina Path `(પ્રદક્ષિણા પથ)`**:\n   - The circular paved walkway surrounding the stupa. Devotees walk clockwise, keeping the stupa on their **right side `(જમણી બાજુ)`** out of reverence.\n4. **Toran `(તોરણ / तोरण)`**:\n   - The ornate, ceremonial arched entrance gateway resting on two tall vertical stone pillars connected by horizontal carved architraves.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "title": "Anatomy of a Buddhist Stupa",
        "content": "```\n                            [ Chhatra / છત્ર ]\n                                  │\n                           ┌──────┴──────┐  ◄── HARMIKA (હર્મિકા - Top Railing)\n                        ┌──┴─────────────┴──┐\n                      ┌─┘                   └─┐\n                     │       ANDA / DOME       │  (અર્ધગોળાકાર ઈંટોનો ઘુમ્મટ)\n                     │     (Relics Inside)     │\n                     └──┬───────────────────┬──┘\n   TORAN (તોરણ)         │   MEDHI (મેધી)    │     CIRCUMAMBULATION\n   (Carved Gateway) ──► └───────────────────┘ ◄── PRADAKSHINA PATH (પ્રદક્ષિણા પથ)\n```",
        "image_url": "assets/images/ss_ch3_stupa_architecture.jpg",
        "alt_text": "Structural diagram of a Buddhist Stupa showing Harmika, Medhi, Pradakshina Path, and Toran"
    })
    
    blocks.append({
        "type": "theory",
        "title": "8. The Pillar of Sarnath: Crown Jewel of Indian Sculpture (સારનાથનો સ્તંભ)",
        "content": "The **Sarnath Pillar `(સારનાથનો સિંહસ્તંભ / सारनाथ का सिंह स्तंभ)`** is recognized worldwide as the absolute masterpiece of ancient Indian sculpture.\n\n### Architectural & Artistic Marvels:\n1. **Single Monolithic Stone `(એકાશ્મ પથ્થર)`**:\n   - Carved entirely out of a single monolithic pillar of Chunar sandstone `(ચૂનારનો રેતીયો પથ્થર)`.\n   - Polished with such supreme skill that it shines like gleaming metal / glass even after 2,300 years.\n2. **Four Back-to-Back Lions `(પરસ્પર પીઠ ટેકવીને બેઠેલા ચાર સિંહો)`**:\n   - On top of the pillar, four majestic lions sit back-to-back facing the four cardinal directions, symbolizing sovereign strength, courage, and pride.\n3. **The Dharma Chakra `(ધર્મચક્ર / धर्मचक्र - ૨૪ આરા)`**:\n   - Below the lions on the circular base sits the **Dharma Chakra** with **24 spokes** symbolizing the triumph of righteousness and continuous progress.\n   - Carved between the wheels are figures of **four animals: Elephant `(હાથી)`, Horse `(ઘોડો)`, Bull `(આખલો / બળદ)`, and Lion `(સિંહ)`**.\n4. **Inverted Lotus `(ઊંધો કમળ / अधोमुखी कमल)`**:\n   - The entire capital rests gracefully on an inverted lotus base.\n\n### National Significance of the Sarnath Capital:\n- The four-lion sculpture was chosen as the **National Emblem of India `(ભારતનું રાષ્ટ્રીય પ્રતીક / રાષ્ટ્રમુદ્રા)`**.\n- The 24-spoke Dharma Chakra was honored with a permanent place in the center of the **Indian National Flag `(ભારતીય રાષ્ટ્રધ્વજ / ત્રિરંગો)`**.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "question": "Which part of the Buddhist Stupa refers to the railing surrounding the top of the dome enclosing the sacred relic casket?",
        "options": [
            "Medhi",
            "Harmika",
            "Toran",
            "Gopuram"
        ],
        "correct_answer": "Harmika",
        "correct_index": 1,
        "explanation": "Harmika (હર્મિકા) is the square balcony/railing situated at the top of the stupa dome that encloses and protects the sacred relics of Lord Buddha."
    })
    
    blocks.append({
        "type": "teacher_tip",
        "title": "Teacher's Board Exam Golden Tip: Sarnath Lion Capital",
        "content": "💡 **Board Exam Must-Remember Facts:**\n- Carved from: **Chunar Sandstone `(ચૂનારનો પથ્થર)`**.\n- Number of spokes in Dharma Chakra: **24 spokes `(૨૪ આરા)`**.\n- Four animals on circular base: **Elephant, Horse, Bull, Lion** (Mnemonic: **E-H-B-L**).\n- National honors: 4 Lions = **National Emblem**; Dharma Chakra = Center of **National Flag**.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    # ==========================================
    # MODULE 5: CAVE ARCHITECTURE OF INDIA & GUJARAT
    # ==========================================
    blocks.append({
        "type": "theory",
        "title": "9. Cave Architecture of India (ભારતનું ગુફા સ્થાપત્ય)",
        "content": "Cave architecture represents the pinnacle of rock-cut sculpture, where entire mountains were hollowed out into majestic temples, viharas (monasteries), and chaityas (prayer halls).\n\n### Major Caves of India:\n1. **Ajanta & Ellora Caves `(અજંતા-ઇલોરાની ગુફાઓ, ઔરંગાબાદ - મહારાષ્ટ્ર)`**:\n   - **Ajanta Caves**: World-famous for Buddhist wall frescoes `(ભીંતચિત્રો)` and sculptures.\n   - **Ellora Cave No. 16 - Kailasa Temple `(કૈલાસ મંદિર)`**: Carved from the top downwards out of a single monolithic rock cliff! Measures 50 m long, 33 m wide, and 30 m high. A miracle of global architecture.\n2. **Elephanta Caves `(એલિફન્ટાની ગુફાઓ, મુંબઈ નજીક)`**:\n   - Situated on an island in the Arabian Sea. Named 'Elephanta' by the Portuguese after seeing a stone elephant.\n   - **Trimurti Sculpture `(ત્રિમૂર્તિ - બ્રહ્મા, વિષ્ણુ, મહેશ)`** in Cave No. 1 is hailed among the finest sculptures in the world.\n3. **Udayagiri & Khandagiri Caves `(ઉદયગિરી અને ખંડગિરી, ઓડિશા)`**:\n   - Famous for the inscriptions of King Kharavela.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "title": "10. Famous Caves of Gujarat (ગુજરાતનું ગુફા સ્થાપત્ય)",
        "content": "Gujarat boasts a stunning array of ancient rock-cut cave complexes:\n\n1. **Junagadh Caves `(જૂનાગઢની ગુફાઓ)`** (3 Distinct Groups):\n   - **Bawa Pyara Caves `(બાવા પ્યારાનો ગુફા સમૂહ)`**: 16 caves arranged in three tiers intersecting at right angles.\n   - **Uparkot Caves `(ઉપરકોટની ગુફાઓ)`**: Double-storeyed rock-cut caves with carved pillars and light-shaft windows.\n   - **Khapra-Kodiya Caves `(ખાપરા-કોડિયાની ગુફાઓ)`**: Carved into rock beds with water cisterns.\n\n2. **Khambhalida Caves `(ખંભાલીડાની ગુફાઓ - ગોંડલ, રાજકોટ)`**:\n   - Discovered in **1959** by P.P. Pandya near Gondal.\n   - Features a central Chaitya hall flanked by life-size standing sculptures of Bodhisattva Avalokiteshvara and Padmapani.\n\n3. **Talaja Caves `(તળાજાની ગુફાઓ - ભાવનગર)`**:\n   - Located near the mouth of the Shetrunji river on the holy hill of *Tal-dhvajgiri*.\n   - Complex of **30 rock-cut caves**. Highlights include the colossal assembly hall named **Ebhal Mandap `(એભલ મંડપ)`** and an ornate Chaitya Griha.\n\n4. **Sana Caves `(સાણાની ગુફાઓ - ગીર સોમનાથ)`**:\n   - Located near Vankiya village in Una taluka.\n   - A cluster of **62 caves** carved across hilltops, resembling a massive beehive `(મધપૂડાની જેમ પથરાયેલી)`.\n\n5. **Dhank Caves `(ઢાંક ગુફાઓ - ઉપલેટા, રાજકોટ)`**:\n   - Situated on Dhankgiri hill, containing Jain Tirthankara figures.\n\n6. **Jhingurijhar Caves `(ઝીંઝુરીઝર ગુફાઓ - પોરબંદર)`**:\n   - Located in the Dhasuk ravines near Siddhasar (1st–2nd century AD Buddhist caves).\n\n7. **Kadiya Dungar Caves `(કડિયા ડુંગર ગુફાઓ - ઝઘડિયા, ભરૂચ)`**:\n   - Complex of 3 Buddhist caves on Kadiya Dungar.\n   - Features a magnificent **11-foot monolithic lion pillar `(એકાશ્મ સિંહસ્તંભ)`** with **two distinct lion bodies joined into one single roaring head `(બે શરીર અને એક મુખવાળો સિંહ)`**.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "diagram",
        "title": "Mapping the Caves of Gujarat",
        "content": "```\n┌────────────────────────────┬─────────────────────────────┬────────────────────────────────────────┐\n│ CAVE COMPLEX (ગુફા સમૂહ)   │ DISTRICT / LOCATION         │ UNIQUE HIGHLIGHT / KEY ATTRACTION      │\n├────────────────────────────┼─────────────────────────────┼────────────────────────────────────────┤\n│ 1. Junagadh Caves          │ Junagadh (ઉપરકોટ/બાવા પ્યારા)│ Double-storeyed & 3-tier cave groups   │\n│ 2. Khambhalida Caves       │ Gondal, Rajkot (1959)       │ Bodhisattva & Padmapani sculptures     │\n│ 3. Talaja Caves            │ Tal-dhvajgiri, Bhavnagar    │ 30 caves with massive 'Ebhal Mandap'   │\n│ 4. Sana Caves              │ Una, Gir Somnath            │ 62 caves spread like a beehive         │\n│ 5. Dhank Caves             │ Upleta, Rajkot              │ Dhankgiri Jain sculptures              │\n│ 6. Jhingurijhar Caves      │ Siddhasar, Porbandar        │ Ancient 1st-2nd century Buddhist caves │\n│ 7. Kadiya Dungar Caves     │ Jhagadia, Bharuch           │ 11-ft pillar: 2 lion bodies + 1 head   │\n└────────────────────────────┴─────────────────────────────┴────────────────────────────────────────┘\n```",
        "image_url": "assets/images/ss_ch3_gujarat_caves_map.jpg",
        "alt_text": "Mapping chart of famous Caves of Gujarat"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "question": "At which cave site in Gujarat can you find an 11-foot high monolithic stone pillar featuring two lion bodies joined with a single head?",
        "options": [
            "Talaja Caves (Bhavnagar)",
            "Sana Caves (Gir Somnath)",
            "Kadiya Dungar Caves (Bharuch)",
            "Khambhalida Caves (Rajkot)"
        ],
        "correct_answer": "Kadiya Dungar Caves (Bharuch)",
        "correct_index": 2,
        "explanation": "The Kadiya Dungar Caves in Jhagadia taluka, Bharuch district, feature a unique 11-foot monolithic lion pillar with two bodies and one common face (બે શરીર અને એક મુખવાળો સિંહસ્તંભ)."
    })

    # ==========================================
    # MODULE 6: CHARIOT TEMPLES & TEMPLE ARCHITECTURE
    # ==========================================
    blocks.append({
        "type": "theory",
        "title": "11. Chariot Temples & Classical Temple Architecture (રથ મંદિરો અને મંદિર સ્થાપત્ય)",
        "content": "### A. Monolithic Chariot Temples of South India `(દક્ષિણ ભારતના રથ મંદિરો)`:\n- Built under the illustrious **Pallava Dynasty `(પલ્લવ વંશ)`** at **Mahabalipuram / Mamallapuram `(મહાબલીપુરમ)`** on the coast of Tamil Nadu.\n- Carved entirely out of single massive rock boulders `(એક જ વિશાળ ખડકમાંથી કંડારેલા એકાશ્મ રથ મંદિરો)`.\n- Named after the heroes of Mahabharata:\n  - **Dharmaraja Chariot `(ધર્મરાજ રથ / યુધિષ્ઠિર રથ)`** ⟶ The **largest** chariot temple.\n  - **Draupadi Chariot `(દ્રૌપદી રથ)`** ⟶ The **smallest** chariot temple.\n\n---\n\n### B. Essential Parts of Hindu Temples `(હિન્દુ મંદિર સ્થાપત્યના મુખ્ય અંગો)`:\n1. **Garbhagriha `(ગર્ભગૃહ / गर्भगृह - Sanctum Sanctorum)`**:\n   - The dark, sacred, square inner chamber where the principal deity's idol `(મુખ્ય પ્રતિમા)` is consecrated.\n2. **Mandapa `(મંડપ / મંડપ)`**:\n   - The spacious pillared assembly hall in front of the sanctum where devotees sit and pray.\n3. **Shikhara `(શિખર / शिखर - Spire)`**:\n   - The towering pyramidical or stepped spire constructed directly above the Garbhagriha.\n4. **Antarala `(અંતરાલ)`**:\n   - The transitional hallway/vestibule connecting the Garbhagriha to the Mandapa.\n5. **Gopuram `(ગોપુરમ / गोपुरम)`**:\n   - The colossal, artistically sculpted **entrance gateway `(ભવ્ય પ્રવેશદ્વાર)`** of South Indian Dravidian temples (e.g., Meenakshi Temple, Madurai).",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "title": "12. Sun Temple of Modhera: Architectural Pride of Gujarat (મોઢેરાનું સૂર્યમંદિર)",
        "content": "The **Sun Temple of Modhera `(મોઢેરાનું સૂર્યમંદિર)`** in Mehsana district, Gujarat, built on the banks of the Pushpavati river, represents the golden pinnacle of Solanki architecture.\n\n### Key Architectural & Astronomical Wonders:\n1. **Built in 1026 AD**:\n   - Constructed by King **Bhimdev I `(ભીમદેવ સોલંકી ૧)`** of the Solanki dynasty.\n2. **The Astronomical Wonder of Sunrise `(સૂર્યોદયનો અદભુત ચમત્કાર)`**:\n   - The temple's eastern entrance was engineered with such supreme astronomical accuracy that on equinox days, the **very first ray of the rising sun `(સૂર્યનું પ્રથમ કિરણ)`** traveled through the Sabha Mandap and pierced directly into the Garbhagriha, falling onto the **gem mounted on the crown of the Sun God's idol `(સૂર્યપ્રતિમાના મુકુટની મધ્યમાં રહેલા મણિ પર)`**!\n   - This illuminated the entire sanctum in a divine golden radiance.\n3. **12 Forms of Sun God & Iranian Style**:\n   - 12 different sculpted forms of the Sun God adorn the temple walls, executed in an elegant Iranian/Solanki artistic style.\n4. **Suryakund & 108 Shrines `(સૂર્યકુંડ અને ૧૦૮ નાનાં મંદિરો)`**:\n   - Outside the temple lies the **Suryakund `(સૂર્યકુંડ / રામકુંડ)`**, a massive stepped water tank.\n   - Along the steps of the tank sit **108 small exquisite miniature temples `(૧૦૮ નાનાં-નાનાં કલાત્મક મંદિરો)`**.\n   - During dusk and dawn, when earthen oil lamps are lit across all 108 shrines, the reflection in the water creates an unforgettable, heavenly sight!",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "theory",
        "title": "13. Other Iconic Temples of India",
        "content": "- **Sun Temple of Konark `(કોણાર્કનું સૂર્યમંદિર - કાળો પેગોડા / Black Pagoda)`** (Odisha):\n  - Built by King Narasimhadeva I (Ganga Dynasty).\n  - Designed in the shape of a colossal chariot of the Sun God with **12 pairs of massive carved stone wheels `(૧૨ જોડ વિશાળ પૈડાં)`** (symbolizing 12 months) pulled by **7 spirited stone horses `(૭ ઘોડા)`**.\n- **Brihadeeshwara Temple `(બૃહદેશ્વર મંદિર / રાજરાજેશ્વર મંદિર)`** (Thanjavur, Tamil Nadu):\n  - Built by Chola King **Rajaraja I `(રાજરાજ પ્રથમ)`**.\n  - Its 200-foot high towering Vimana is crowned with an 80-tonne single granite capstone (*Kumbham*), constructed so ingeniously that its **shadow never falls on the ground at noon**!\n- **Khajuraho Temples `(ખજુરાહોના મંદિરો)`** (Madhya Pradesh):\n  - Built by Chandel Rajput rulers, famed for exquisite Nagara-style stone carvings.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "question": "During whose reign and in which year was the world-famous Sun Temple of Modhera constructed in Gujarat?",
        "options": [
            "Siddhraj Jaisinh in 1120 AD",
            "Bhimdev I (Solanki Dynasty) in 1026 AD",
            "Kumarapala in 1150 AD",
            "Mulraj I in 990 AD"
        ],
        "correct_answer": "Bhimdev I (Solanki Dynasty) in 1026 AD",
        "correct_index": 1,
        "explanation": "The Sun Temple of Modhera was built in 1026 AD during the golden rule of King Bhimdev I of the Solanki dynasty in Gujarat."
    })
    
    blocks.append({
        "type": "teacher_tip",
        "title": "Teacher's Exam Focus: Modhera Sun Temple 3-Mark Checklist",
        "content": "💡 **3-Mark Question Formula for Modhera Sun Temple:**\n1. **Year & King**: 1026 AD, King Bhimdev I (Solanki dynasty).\n2. **Sunrise Ray Phenomenon**: First ray hits the gem on Sun God's crown.\n3. **Style & Sculptures**: Iranian style, 12 manifestations of Sun God.\n4. **Suryakund**: Stepped tank with 108 miniature temples creating a divine sight during evening aarti.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    # ==========================================
    # MODULE 7: STEPWELLS (VAV) & MEDIEVAL ARCHITECTURE OF GUJARAT
    # ==========================================
    blocks.append({
        "type": "theory",
        "title": "14. The Stepwell Architecture of Gujarat (ગુજરાતનું વાવ સ્થાપત્ય)",
        "content": "A **Vav `(વાવ / बावड़ी - Stepwell)`** is a uniquely Indian subterranean architectural marvel—a step-well with pavilions, pillared galleries, and stone stairs leading down to the water table.\n\n### The 4 Types of Stepwells Based on Entrances `(પ્રવેશદ્વાર આધારિત વાવના ૪ પ્રકારો)`:\n1. **Nanda `(નંદા)`** ⟶ Stepwell with **1 Entrance `(૧ પ્રવેશદ્વાર)`**.\n2. **Bhadra `(ભદ્રા)`** ⟶ Stepwell with **2 Entrances `(૨ પ્રવેશદ્વાર)`**.\n3. **Jaya `(જયા)`** ⟶ Stepwell with **3 Entrances `(૩ પ્રવેશદ્વાર)`**.\n4. **Vijaya `(વિજયા)`** ⟶ Stepwell with **4 Entrances `(૪ પ્રવેશદ્વાર)`**.\n\n---\n\n### World-Famous Stepwells of Gujarat:\n\n#### A. Rani ki Vav `(રાણકી વાવ / रानी की वाव - Patan)`:\n- Built by **Queen Udayamati `(રાણી ઉદયમતી)`**, wife of King Bhimdev I Solanki, to solve the water crisis of Patan.\n- A breathtaking **7-storeyed subterranean marvel `(સાત માળની ભવ્ય વાવ)`**.\n- Adorned with more than **500 exquisite principal sculptures** depicting Lord Vishnu's Dashavatara, celestial nymphs (Apsaras), and deities.\n- In **2014**, UNESCO declared Rani ki Vav a **World Heritage Site `(યુનેસ્કો વૈશ્વિક વારસો)`**.\n\n#### B. Adalaj Stepwell `(અડાલજની વાવ - Gandhinagar)`:\n- Built in **1499 AD** by **Queen Rudabai `(રાણી રૂડાબાઈ)`** in loving memory of her husband King Virsinh Vaghela.\n- A 5-storeyed stepwell celebrated for its magnificent floral, geometric, and Indo-Islamic fusion carvings.\n\n#### Other Renowned Stepwells:\n- **Adi-Kadi Vav and Navghan Kuwo `(અડી-કડી વાવ અને નવઘણ કૂવો)`** in Junagadh.\n- **Dada Harir Vav `(દાદા હરિની વાવ)`** in Ahmedabad, and **Madhavav `(માધાવાવ)`** in Wadhwan.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "title": "15. Medieval Islamic & Stone Lattice Architecture (મધ્યકાલીન સ્થાપત્ય)",
        "content": "During the medieval Sultanate era, Gujarat became a hub of world-class Islamic and fusion architecture:\n\n### A. Sidi Saiyyed Mosque & Jali `(સિદી સૈયદની જાળી / સીદી સૈયદ કી જાલી - Ahmedabad)`:\n- Built in **1572 AD** in Ahmedabad.\n- The stone screens on the mosque windows feature **intricate stone filigree lattice carving `(પથ્થરમાં કંડારેલી અત્યંત બારીક નકશીદાર જાળી)`** depicting tree branches, foliage, and geometric vines.\n- Renowned worldwide as one of the most sublime masterpieces of stone carving.\n\n### B. Shaking Minarets `(ઝૂલતા મિનારા / Jhulta Minar - Ahmedabad)`:\n- Located at Rajpur-Gomtipur, Ahmedabad (Sidi Bashir Mosque).\n- **Engineering Mystery**: When one minaret is gently rocked/shaken, the other minaret also begins to vibrate in synchrony, while the connecting archway remains completely unharmed!\n- The mystery behind this vibration-damping engineering remains unsolved.\n\n### C. Jami Masjid `(જામી મસ્જિદ - Ahmedabad)`:\n- Built in **1423 AD** by **Sultan Ahmed Shah** near Manek Chowk.\n- Features **260 intricately carved stone pillars `(૨૬૦ સ્તંભો)`** supporting **15 magnificent domes `(૧૫ ઘુમ્મટો)`**.\n\n### Other Marvels:\n- **Sarkhej Roza `(સરખેજ રોઝા)`**, **Rani Sipri Mosque `(રાણી સિપ્રીની મસ્જિદ / મસ્જિદે નગીના)`**, and the exquisite **Hathisingh Jain Temples `(હઠીસિંહનાં દેરાં)`**.",
        "difficulty": "Intermediate",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "diagram",
        "title": "Stepwell Types (Nanda, Bhadra, Jaya, Vijaya) & Gujarat Vavs",
        "content": "```\n┌──────────────────────┬────────────────────────┬────────────────────────────────────────┐\n│ STEPWELL TYPE (પ્રકાર)│ ENTRANCES (પ્રવેશદ્વાર) │ MEMORY MNEMONIC (યાદ રાખવાની રીત)     │\n├──────────────────────┼────────────────────────┼────────────────────────────────────────┤\n│ 1. NANDA (નંદા)       │ 1 Entrance (૧ દ્વાર)   │ 'N' = 1                                │\n│ 2. BHADRA (ભદ્રા)     │ 2 Entrances (૨ દ્વાર)  │ 'B' = 2                                │\n│ 3. JAYA (જયા)        │ 3 Entrances (૩ દ્વાર)  │ 'J' = 3                                │\n│ 4. VIJAYA (વિજયા)    │ 4 Entrances (૪ દ્વાર)  │ 'V' = 4                                │\n├──────────────────────┴────────────────────────┴────────────────────────────────────────┤\n│ • Rani ki Vav (Patan)     ⟶ 7 Storeys, Queen Udayamati (UNESCO World Heritage 2014)    │\n│ • Adalaj Vav (Gandhinagar) ⟶ 5 Storeys, Queen Rudabai (1499 AD)                         │\n│ • Adi-Kadi & Navghan Kuwo ⟶ Junagadh ancient rock-cut water heritage                   │\n└────────────────────────────────────────────────────────────────────────────────────────┘\n```",
        "image_url": "assets/images/ss_ch3_stepwells_of_gujarat.jpg",
        "alt_text": "Chart showing 4 types of Stepwells and famous Vavs of Gujarat"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "question": "A stepwell (Vav) with 3 entrances is known by which specific architectural name?",
        "options": [
            "Nanda",
            "Bhadra",
            "Jaya",
            "Vijaya"
        ],
        "correct_answer": "Jaya",
        "correct_index": 2,
        "explanation": "According to ancient architectural classification, stepwells are categorized based on their entrances: Nanda (1 entrance), Bhadra (2 entrances), Jaya (3 entrances), and Vijaya (4 entrances)."
    })

    # ==========================================
    # MODULE 8: BOARD EXAM MASTERY & CHAPTER SUMMARY
    # ==========================================
    blocks.append({
        "type": "exam_tips",
        "title": "GSEB Class 10 Board Exam: High-Yield Distinction & Questions Checklist",
        "content": "🔥 **GUARANTEED BOARD EXAM TOPICS (વારંવાર પૂછાતા પ્રશ્નો):**\n\n### Top High-Yield Questions Checklist:\n1. **Town Planning of Mohenjo-daro (4 Marks)**: Cover Roads (9.75 m), Houses (high plinths, side lanes), Covered Drainage (Crete island), and Public Bath (bitumen plaster).\n2. **Sun Temple of Modhera (3 Marks)**: King Bhimdev I (1026 AD), sunrise ray on gem, Iranian style, 108 shrines around Suryakund.\n3. **Caves of Gujarat (3 Marks)**: Junagadh, Khambhalida, Talaja (Ebhal Mandap), Sana (62 beehive caves), and Kadiya Dungar (11-ft 2-body lion pillar).\n4. **Stepwells of Gujarat (3 Marks)**: Classification (Nanda, Bhadra, Jaya, Vijaya) and details of Rani ki Vav (7 storeys, Queen Udayamati, UNESCO).\n5. **Sarnath Lion Pillar (2/3 Marks)**: Chunar stone, 4 Lions (National Emblem), 24-spoke Dharma Chakra (National Flag), and 4 animals (Elephant, Horse, Bull, Lion).\n6. **Short Notes**: Dholavira (3-tier town, Rainwater harvesting), Lothal (Tidal dockyard, port trade), Sidi Saiyyed Jali (stone filigree), Shaking Minarets.",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })
    
    blocks.append({
        "type": "summary",
        "title": "Chapter Summary: Sculpture and Architecture",
        "content": "✨ **Mastery Recap:**\n- **Sculpture `(શિલ્પકલા)`** is chiseling feelings onto stone/wood/clay; **Architecture `(સ્થાપત્ય / વાસ્તુ)`** is the art of structural construction.\n- **Mohenjo-daro** stunned the world with 9.75 m roads, flood-proof houses, underground covered sewers, and bitumen-plastered public baths.\n- **Dholavira** excelled in 3-tier town planning and rainwater harvesting; **Lothal** was the world's earliest international tidal dockyard port.\n- **Buddhist Stupas** consist of Harmika (relic railing), Medhi (terrace), Pradakshina Path (pathway), and Toran (ornate gateway).\n- **Sarnath Pillar** carved from Chunar sandstone gave India its National Emblem (4 Lions) and the 24-spoke Dharma Chakra.\n- **Gujarat Caves** span Junagadh, Khambhalida, Talaja (Ebhal Mandap), Sana (62 caves), and Kadiya Dungar (2-bodied lion pillar).\n- **Temples**: Modhera Sun Temple (1026 AD, Bhimdev I, 108 shrines) and Konark Sun Temple (chariot with 12 pairs of wheels).\n- **Stepwells (Vav)** are categorized into Nanda (1), Bhadra (2), Jaya (3), Vijaya (4). **Rani ki Vav** (Patan, 7 storeys) is a UNESCO World Heritage site.\n- **Medieval Gujarat** marvels at the intricate stone lattice of **Sidi Saiyyed Jali** and the acoustic wonder of **Shaking Minarets**.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    # Target 1: GSEB Class 10 Social Science Ch 3
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_social_science_ch3.json"
    os.makedirs(os.path.dirname(gseb_path), exist_ok=True)
    with open(gseb_path, "w", encoding="utf-8") as f:
        json.dump(final_json, f, indent=2, ensure_ascii=False)
    print(f"Generated GSEB Chapter JSON at: {gseb_path}")
    
    # Target 2: NCERT Class 10 Social Science Ch 3 (Sync copy with updated ID)
    ncert_json = dict(final_json)
    ncert_json["metadata"] = dict(final_json["metadata"])
    ncert_json["metadata"]["id"] = "ncert_class10_social_science_ch3"
    ncert_json["metadata"]["board"] = "NCERT/CBSE/GSEB"
    
    ncert_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_social_science_ch3.json"
    with open(ncert_path, "w", encoding="utf-8") as f:
        json.dump(ncert_json, f, indent=2, ensure_ascii=False)
    print(f"Generated NCERT Chapter JSON at: {ncert_path}")
    
    # Target 3: CBSE Class 10 Social Science Ch 3 (Sync copy)
    cbse_json = dict(final_json)
    cbse_json["metadata"] = dict(final_json["metadata"])
    cbse_json["metadata"]["id"] = "cbse_class10_social_science_ch3"
    cbse_json["metadata"]["board"] = "CBSE/GSEB/NCERT"
    
    cbse_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/cbse_class10_social_science_ch3.json"
    with open(cbse_path, "w", encoding="utf-8") as f:
        json.dump(cbse_json, f, indent=2, ensure_ascii=False)
    print(f"Generated CBSE Chapter JSON at: {cbse_path}")

if __name__ == "__main__":
    generate_supreme_gseb_ss_ch3()
