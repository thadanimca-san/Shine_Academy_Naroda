import json
import os

def generate_supreme_gseb_ss_ch1():
    chapter_id = "gseb_class10_social_science_ch1"
    title = "Chapter 1: Heritage of India"
    
    metadata = {
        "id": chapter_id,
        "title": title,
        "subtitle": "The Golden Heritage of Bharat: Natural & Cultural Treasures",
        "subject": "Social Science",
        "grade": "10",
        "board": "GSEB / Universal",
        "curriculum": ["GSEB", "NCERT", "CBSE", "Universal"],
        "language": "English/Hindi/Gujarati (Bilingual)",
        "difficulty": "Intermediate",
        "estimated_minutes": 120,
        "version": "3.0.0-SUPREME-SS",
        "author": "Antigravity Supreme Academic Intelligence",
        "reviewed_by": "Chief Academic Architect",
        "tags": [
            "social_science",
            "class10",
            "gseb",
            "heritage_of_india",
            "natural_heritage",
            "cultural_heritage",
            "gujarat_heritage",
            "ancient_tribes",
            "dravidians",
            "aryans",
            "fairs_of_gujarat",
            "article_51a",
            "board_special",
            "bilingual"
        ],
        "learning_outcomes": [
            "Understand the ancient geographical extent, identity, and sacred naming of Bharatvarsha from ancient scriptures.",
            "Distinguish clearly between Natural Heritage `(प्राकृतिक विरासत / પ્રાકૃતિક વારસો)` and Cultural Heritage `(सांस्कृतिक विरासत / સાંસ્કૃતિક વારસો)`.",
            "Master the rich Cultural Heritage of Gujarat including Harappan sites, architectural wonders, pilgrimage centers, and traditional fairs.",
            "Analyze the characteristics and cultural contributions of ancient tribes (Negrito, Australoid, Dravidian, Mongoloid, Alpine, Aryan).",
            "Learn the constitutional duties under Article 51(A) for preserving and protecting India's rich composite heritage.",
            "Achieve mastery in GSEB and CBSE Board Exam MCQs, distinction tables, and high-yield structured questions."
        ],
        "ai_context": {
            "learning_goal": "Impart a deep, patriotic appreciation of India's multi-layered heritage with structured conceptual clarity, visual analogies, memory mnemonics, and bilingual translations for ESL learners.",
            "common_misconceptions": [
                "Students often confuse Australoids (Nishad) with Negrito (Habsi).",
                "Students confuse Natural Heritage (Nature-given) with Cultural Heritage (Man-made).",
                "Students forget the exact constitutional clauses under Article 51(A) (clauses f, g, h / ૬, ૭, ૮)."
            ],
            "tutor_hint": "Remind students that Culture is 'a way of life' and Heritage is 'a gift from our ancestors'. For tribes, anchor Negrito=Africa/curly hair, Australoid=SE Asia/clay pottery, Dravidian=Mohenjo-Daro/Shiva-Parvati/Dravidian languages, Aryan=Vedas/nature hymns."
        }
    }
    
    blocks = []
    
    # ==========================================
    # MODULE 1: ANCIENT BHARAT - LOCATION & IDENTITY
    # ==========================================
    blocks.append({
        "type": "hook",
        "title": "The Land of Immense Splendor: Why Bharat Fascinated the World",
        "content": "Imagine a land so rich in culture, knowledge, and natural wealth that travelers, traders, and scholars from every corner of the earth traveled thousands of miles across rugged mountains and treacherous oceans just to reach it! That ancient cradle of civilization is our motherland—**Bharat `(भारत / ભારત)`**.\n\nFrom the snow-clad peaks of the Himalayas to the roaring waves of the Indian Ocean, India's heritage is not just history in textbooks; it is a living, breathing gift of timeless wisdom.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "title": "Ancient Geographical Boundaries of Bharatvarsha",
        "content": "```\n                     ▲ HIMALAYAN MOUNTAINS (उत्तर / ઉત્તર)\n                     │ (Natural Shield & Sacred Abode)\n                     │\n       ◄─────────────┼─────────────►\n   ARABIAN SEA       │       BAY OF BENGAL\n (पश्चिम / પશ્ચિમ)    │     (पूर्व / પૂર્વ)\n                     │\n                     ▼ INDIAN OCEAN (दक्षिण / દક્ષિણ)\n```\n*India is naturally shielded and surrounded by the Himalayas in the North and vast oceans on three sides.*",
        "image_url": "assets/images/ss_ch1_ancient_bharat_map.jpg",
        "alt_text": "Ancient Map of Bharatvarsha bounded by Himalayas and Oceans"
    })
    
    blocks.append({
        "type": "theory",
        "title": "Ancient Identity & The Sacred Vishnu Purana Verse",
        "content": "India has been known since ancient times by glorious names: **Bharatvarsha `(भारतवर्ष / ભારતવર્ષ)`**, **Bharatbhumi `(भारतभूमि / ભારતભૂમિ)`**, **Aryavarta `(आर्यावर्त / આર્યાવર્ત)`**, and **Jambudweepa `(जंबूद्वीप / જંબૂદ્વીપ)`**.\n\nIn our ancient scripture **Vishnu Purana `(विष्णु पुराण / વિષ્ણુ પુરાણ)`**, India's geographical location is described in a profound Sanskrit shloka:\n\n> *\"उत्तरं यत्समुद्रस्य हिमाद्रेश्चैव दक्षिणम्।*\n> *वर्षं तद् भारतं नाम भारती यत्र संततिः॥\"*\n\n**Meaning:** The country that lies **North of the Ocean** (Indian Ocean) and **South of the Snowy Mountains** (Himalayas) is called **Bharat**, and its descendants are called **Bharati `(भारतीय / ભારતીય)`**.\n\n**Key Geographical Facts for Board Exams:**\n- At the start of any auspicious ritual `(शुभ कार्य / શુભ કાર્ય)`, sacred vows (*Sankalpas*) still recite words like *Bharatvarsha* and *Jambudweepa*.\n- **Area Rank:** India is the **7th largest country** in the world by land area.\n- **Population Rank:** India holds the **2nd rank** globally in population (as per textbook census baseline).",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "question": "According to the ancient scripture Vishnu Purana, what is the country situated North of the ocean and South of the Himalayas called?",
        "options": [
            "Aryavarta",
            "Bharat",
            "Jambudweepa",
            "Indravarta"
        ],
        "correct_answer": "Bharat",
        "correct_index": 1,
        "explanation": "The Vishnu Purana explicitly states: 'Uttaram yat samudrasya himadreshchaiva dakshinam, varsham tad bharatam nama bharati yatra santatih' — the land is called Bharat and its descendants are Bharati."
    })
    
    blocks.append({
        "type": "teacher_tip",
        "title": "Teacher's Memory Trick: Ancient Names of India",
        "content": "💡 **Teacher's Secret:** Remember the mnemonic **'B-B-A-J'** for the 4 ancient names of India:\n- **B** ⟶ **Bharatvarsha `(भारतवर्ष / ભારતવર્ષ)`**\n- **B** ⟶ **Bharatbhumi `(भारतभूमि / ભારતભૂમિ)`**\n- **A** ⟶ **Aryavarta `(आर्यावर्त / આર્યાવર્ત)`**\n- **J** ⟶ **Jambudweepa `(जंबूद्वीપ / જંબૂદ્વીપ)`**\n\n*Write these names in your 2-mark introductory answers to impress board examiners!*",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    # ==========================================
    # MODULE 2: MEANING OF CULTURE & HERITAGE
    # ==========================================
    blocks.append({
        "type": "definition",
        "title": "What is Heritage? (विरासत / વારસો)",
        "content": "**Heritage `(विरासत / વારસો)`** means a **valuable gift from our ancestors to us `(पूर्वजों से प्राप्त अमूल्य भेंट / પૂર્વજો તરફથી મળેલી અમૂલ્ય ભેટ)`**.\n\nIn our school daily pledge, we proudly recite: *\"I love my country and I am proud of its rich and varied heritage.\"*\n\nHeritage encompasses all the treasures of intellect, spirituality, art, nature, and customs handed down lovingly from generation to generation.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "theory",
        "title": "What is Culture? (संस्कृति / સંસ્કૃતિ)",
        "content": "**Culture `(संस्कृति / સંસ્કૃતિ)`** is defined as **'A Way of Life `(जीवन जीने की शैली / જીવન જીવવાની રીત)'**.\n\nCulture comprises the sum total of:\n1. Human habits `(मानव आदतें / માનવ ટેવો)`\n2. Values `(मूल्य / મૂલ્યો)`\n3. Customs and traditions `(आचार-विचार और परंपराएँ / રીતરિવાજો અને પરંપરાઓ)`\n4. Living ideals that lead humanity to the highest state of civilized living.\n\nCulture changes and evolves with time as human beings adapt to changing natural and social conditions.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "diagram",
        "title": "The Two Grand Pillars of Indian Heritage",
        "content": "```\n                       ┌─────────────────────────────────┐\n                       │     HERITAGE OF INDIA           │\n                       │   (ભારતનો વારસો / भारत की विरासत)│\n                       └────────────────┬────────────────┘\n                                        │\n               ┌────────────────────────┴────────────────────────┐\n               ▼                                                 ▼\n   ┌───────────────────────┐                         ┌───────────────────────┐\n   │   NATURAL HERITAGE    │                         │   CULTURAL HERITAGE   │\n   │  (प्राकृतिक विरासत)    │                         │  (सांस्कृतिक विरासत)   │\n   │  (પ્રાકૃતિક વારસો)     │                         │  (સાંસ્કૃતિક વારસો)    │\n   ├───────────────────────┤                         ├───────────────────────┤\n   │ • Landscapes (भू-दृश्य)│                         │ • Architecture & Forts│\n   │ • Rivers (Lokmata)    │                         │ • Sculptures & Temples│\n   │ • Flora (Vegetation)  │                         │ • Science & Maths (0) │\n   │ • Fauna (Wildlife)    │                         │ • Fairs & Literature  │\n   └───────────────────────┘                         └───────────────────────┘\n```",
        "image_url": "assets/images/ss_ch1_heritage_pillars.jpg",
        "alt_text": "Diagram showing Two Pillars of Indian Heritage: Natural and Cultural"
    })

    # ==========================================
    # MODULE 3: NATURAL HERITAGE OF INDIA
    # ==========================================
    blocks.append({
        "type": "theory",
        "title": "1. Natural Heritage of India (ભારતનો પ્રાકૃતિક વારસો / भारत की प्राकृतिक विरासत)",
        "content": "**Natural Heritage** is the result of the close, symbiotic relationship between **Nature, Environment, and Human Life `(प्रकृति, पर्यावरण और मानव जीवन / પ્રકૃતિ, પર્યાવરણ અને માનવજીવન)`**. It is a divine gift provided entirely by nature.\n\nIndia's Natural Heritage is classified into **4 Core Elements**:\n\n### A. Landscapes `(भू-दृश्य / ભૂમિ દ્રશ્યો)`\n- Beautiful landforms are created by nature (e.g., the mighty Himalayas).\n- The Himalayas have gifted India with fertile plains, perennial rivers, dense forests, snow-clad mountain peaks, and sacred pilgrimage centers like **Amarnath, Badrinath, Kedarnath**, and peaks like **Nanda Devi**.\n\n### B. Rivers `(नदियाँ / નદીઓ - Lokmata / લોકમાતા)`\n- Since ancient times, rivers have sustained human life. Indian civilization originated and flourished on the banks of the **Indus (सिंधु)** and **Ravi (रावी)** rivers.\n- Great rivers—**Ganga, Yamuna, Saraswati, Narmada, Godavari, Krishna, and Kaveri**—have shaped our agriculture, domestic life, culture, and industries.\n- Because rivers have nurtured our people like a mother, Indian culture honors rivers with the revered title of **'Lokmata `(लोकमाता / લોકમાતા)'**.\n\n### C. Vegetation `(वनस्पति जीवन / વનસ્પતિ જીવન)`\n- Indians have been nature lovers since antiquity. Plants, flowers, and sacred trees are revered.\n- Sacred trees worshipped with deep faith: **Banyan `(बरगद / વડ)`**, **Peepal `(पीपल / પીપળો)`**, and **Basil `(तुलसी / તુલસી)`**. The *Vat Savitri* vow involves worship of the Banyan tree.\n- World-renowned Ayurvedic medicinal plants: **Harde `(हरड़े / હરડે)`**, **Amla `(आँवला / આમળાં)`**, **Baheda `(बहेड़ा / બહેડાં)`**, **Neem `(नीम / લીમડો)`**, **Ardusi**, and **Aloe Vera `(घृतकुमारी / કુંવારપાઠું)`**.\n\n### D. Wildlife `(वन्यजीवन / વન્યજીવ)`\n- India is an animal-loving culture. Tigers, lions, elephants, rhinos, peacocks, eagles, and venomous snakes are protected.\n- Many wild animals were chosen as vehicles (*Vahanas*) of Hindu Gods and Goddesses.\n- **Asiatic Lions `(एशियाई शेर / એશિયાઈ સિંહો)`** in the entire world are found surviving naturally ONLY in the **Gir Forest of Gujarat `(ગીરનું જંગલ)`**.\n- Our **National Emblem `(राष्ट्रीय प्रतीक / રાષ્ટ્રમુદ્રા)`** proudly features **Four Lions, a Horse, and a Bull**.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "teacher_tip",
        "title": "Board Exam Golden Focus: Why are Rivers Called Lokmata?",
        "content": "💡 **High-Yield 2-Mark Question:** *\"Why are rivers called Lokmata in Indian culture?\"*\n\n**Topper Answer Formula:**\n1. Rivers provided drinking water, domestic water, irrigation, and power since prehistoric times.\n2. The cradle of Indian culture (Indus and Ravi river civilizations) was nurtured on riverbanks.\n3. Rivers supported clay pottery, house plastering, and economic prosperity.\n4. Therefore, expressing heartfelt gratitude, our ancestors elevated rivers to the status of a sacred mother (**Lokmata `(लोकमाता / લોકમાતા)`**).",
        "difficulty": "Beginner",
        "bloom": "Apply"
    })

    blocks.append({
        "type": "knowledge_check",
        "question": "Where in the entire world are Asiatic Lions found naturally in their wild habitat?",
        "options": [
            "Jim Corbett National Park (Uttarakhand)",
            "Kaziranga National Park (Assam)",
            "Gir Forest (Gujarat)",
            "Sundarbans (West Bengal)"
        ],
        "correct_answer": "Gir Forest (Gujarat)",
        "correct_index": 2,
        "explanation": "Asiatic Lions (Panthera leo persica) are found naturally only in the Gir National Park and Wildlife Sanctuary in Gujarat, India."
    })

    # ==========================================
    # MODULE 4: CULTURAL HERITAGE OF INDIA
    # ==========================================
    blocks.append({
        "type": "theory",
        "title": "2. Cultural Heritage of India (ભારતનો સાંસ્કૃતિક વારસો / भारत की सांस्कृतिक विरासत)",
        "content": "**Cultural Heritage** is **Man-made Heritage `(मानव निर्मित विरासत / માનવસર્જિત વારસો)`**.\n\n> *\"Whatever is created, earned, or developed by human beings with their intellect, skill, art, and wisdom is called Cultural Heritage `(बुद्धि, कौशल, कला और कारीगरी द्वारा जो कुछ प्राप्त या निर्मित किया जाता है / માનવીએ પોતાની બુદ્ધિ, શક્તિ, આવડત અને કલા-કૌશલ્ય દ્વારા જે કંઈ સર્જ્યું તેને સાંસ્કૃતિક વારસો કહેવાય)`.\"*\n\n### Monumental Wonders of Indian Cultural Heritage:\n- **Palaces, Temples, Mosques, Forts, Stupas, Viharas, Chaityas, and Caves**.\n- **Ancient Indus Valley Towns:** Mohenjo-Daro, Harappa, Lothal, Dholavira with advanced underground drainage systems.\n- **Sculptural Masterpieces:**\n  - Inverted Lotus figure with Bull and Lion capital (Maurya Era).\n  - Statue of Gautama Buddha in meditative posture.\n  - Statues of Jain Tirthankaras and the rock-cut caves of **Ellora and Ajanta** (Rashtrakuta & Gupta eras).\n\n### Revolutionary Indian Contributions to Global Science & Knowledge:\nIndia did not just build monuments; it gifted humanity foundational knowledge:\n- **Mathematics:** Discovery of **Zero `(शून्य / શૂન્ય)`** and **Decimal System `(दशमलव पद्धति / દશાંશ પદ્ધતિ)`** by the great mathematician **Aryabhata `(आर्यभट्ट)`**.\n- **Science & Medicine:** Ayurveda by Charaka and Sushruta (Surgery), Metallurgy `(धातु विज्ञान)`, Astronomy `(खगोल शास्त्र)`, Astrology `(ज्योतिष शास्त्र)`, and Vastu Shastra `(वास्तु शास्त्र)`.\n- **Yoga `(योग / યોગ)`:** India gave the world the gift of holistic wellness. **21st June** is celebrated globally as **International Yoga Day `(विश्व योग दिवस)`**.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "knowledge_check",
        "question": "Which great ancient Indian mathematician is credited with the discovery of Zero (0)?",
        "options": [
            "Varahamihira",
            "Aryabhata",
            "Brahmagupta",
            "Bhaskaracharya"
        ],
        "correct_answer": "Aryabhata",
        "correct_index": 1,
        "explanation": "Aryabhata discovered Zero (0) and made pioneering contributions to the decimal system, trigonometry, and astronomy."
    })

    # ==========================================
    # MODULE 5: CULTURAL HERITAGE OF GUJARAT
    # ==========================================
    blocks.append({
        "type": "theory",
        "title": "3. Cultural Heritage of Gujarat (ગુજરાતનો સાંસ્કૃતિક વારસો / गुजरात की सांस्कृतिक विरासत)",
        "content": "Gujarat possesses a globally celebrated cultural and archaeological heritage:\n\n### A. Archaeological Sites of Ancient Harappan Civilization:\n1. **Lothal `(લોથલ)`:** Situated in Dholka Taluka (Ahmedabad district). Ancient port and commercial hub.\n2. **Rangpur `(રંગપુર)`:** Situated in Limdi Taluka (Surendranagar district).\n3. **Dholavira `(ધોળાવીરા)`:** Situated in Khadirbet, Bhachau Taluka (Kachchh district). Famous for 3-tier town planning and rain harvesting.\n4. **Shrinathgadh / Rozdi `(શ્રીનાથગઢ / રોઝડી)`:** Situated in Rajkot district.\n\n### B. Pilgrimage & Architectural Jewels of Gujarat:\n- **Rani ki Vav `(રાણકી વાવ - પાટણ)`:** Masterpiece of stepwell architecture built by Queen Udayamati; awarded **UNESCO World Heritage Site** status.\n- **Sun Temple of Modhera `(મોઢેરાનું સૂર્યમંદિર)`:** Built during Solanki King Bhimdev I; designed such that the first ray of the rising sun illuminates the inner sanctum gem.\n- **Rudra Mahalaya `(સિદ્ધપુરનો રુદ્ર મહાલય)`:** Grand temple monument at Siddhpur (Patan district).\n- **Sidi Saiyyed Mosque Jali `(સીદી સૈયદની જાળી - અમદાવાદ)`:** World-famous intricate stone latticework.\n- **Shaking Minarets `(ઝૂલતા મિનારા - અમદાવાદ)`:** Famous for mysterious oscillation without damaging adjoining structures.\n- **Toran of Vadnagar `(વડનગરનું કીર્તિતોરણ)`:** Majestic triumphal arch archway.\n- **Rock Edict of Emperor Ashoka `(જૂનાગઢનો અશોકનો શિલાલેખ)`:** Located at the foothills of Mount Girnar.\n- **Pilgrimage Centers:** Somnath Temple (First among 12 Jyotirlingas), Dwarkadhish Temple (Char Dham), Ambaji Temple (Banaskantha), Bahucharaji (Mehsana), Mahakali Temple (Pavagadh, Panchmahal), and Shatrunjaya Jain Temples (Palitana, Bhavnagar).",
        "difficulty": "Advanced",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "theory",
        "title": "Vibrant Fairs of Gujarat (ગુજરાતના મેળાઓ / गुजरात के प्रसिद्ध मेले)",
        "content": "Gujarat's social-cultural fabric is illuminated by traditional fairs `(મેળાઓ)`:\n\n| Fair Name | Place / District | Timing (Gujarati Calendar) |\n| :--- | :--- | :--- |\n| **1. Bhavnath Mahadev Fair** `(ભવનાથનો મેળો)` | Girnar, Junagadh | Maha Vad 9 to 12 `(મહા વદ ૯ થી ૧૨)` |\n| **2. Tarnetar Fair** `(તરણેતરનો મેળો)` | Tarnetar, Surendranagar | Bhadarva Sud 4 to 6 `(ભાદરવા સુદ ૪ થી ૬)` |\n| **3. Vautha Fair** `(વૌઠાનો મેળો - ગધેડાની લે-વેચ)` | Dholka, Ahmedabad | Kartik Sud Punam `(કારતક સુદ પૂનમ)` |\n| **4. Shamlaji Fair** `(શામળાજીનો મેળો)` | Shamlaji, Aravalli | Kartik Sud 11 to Punam `(કારતક સુદ ૧૧ થી પૂનમ)` |\n| **5. Madhavpur Fair** `(માધવપુરનો મેળો)` | Madhavpur, Porbandar | Chaitra Sud 9 to 13 `(ચૈત્ર સુદ ૯ થી ૧૩)` |\n| **6. Ambaji Fair** `(અંબાજીનો ભાદરવી પૂનમનો મેળો)` | Ambaji, Banaskantha | Bhadarvi Punam `(ભાદરવી પૂનમ)` |\n| **7. Gol Gadhedo Fair** `(ગોળ ગધેડાનો મેળો - આદિવાસી મેળો)` | Garbada, Dahod | 5 to 7 days after Holi `(હોળી પછીના ૫ થી ૭ દિવસે)` |",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    blocks.append({
        "type": "knowledge_check",
        "question": "At which fair in Gujarat is the traditional trade/sale of donkeys (ગધેડાની લે-વેચ) famously carried out?",
        "options": [
            "Tarnetar Fair",
            "Bhavnath Fair",
            "Vautha Fair",
            "Madhavpur Fair"
        ],
        "correct_answer": "Vautha Fair",
        "correct_index": 2,
        "explanation": "The Vautha Fair at Dholka taluka (at the confluence of seven rivers/Saptasangam) is famous for the traditional trading of donkeys and camels."
    })

    # ==========================================
    # MODULE 6: INDIA - LAND AND ANCIENT TRIBES
    # ==========================================
    blocks.append({
        "type": "theory",
        "title": "4. India: Land and Ancient People (પ્રાચીન પ્રજાઓ / प्राचीन जनजातियाँ)",
        "content": "India's composite culture `(समन्वित संस्कृति / સમન્વિત સંસ્કૃતિ)` was created through the harmonious blending of various ancient races who migrated to Bharat:\n\n### 1. Negrito / Habsi `(नीग्रिटो / हब्शी / નેગ્રીટો)`:\n- Came to India from **Africa via Baluchistan**.\n- **Physical Features:** Black skin `(શ્યામ રંગ)`, curly hair `(વાંકડિયા વાળ)`, height 4 to 5 feet.\n\n### 2. Australoid / Nishad `(ऑस्ट्रेलॉइड / निषाद / ઓસ્ટ્રેલોઇડ)`:\n- Came from **South-East Asia**.\n- **Physical Features:** Dark skin, broad head, flat nose, short height.\n- Aryans called them **'Nishad `(निषाद / નિષાદ)'**.\n- Tribes like Kol, Munda, Khasis of Assam, and tribes of Nicobar and Myanmar share these traits.\n- **Civilizational Gift:** Making clay utensils `(માટીનાં વાસણો)`, weaving cotton cloth `(સુતરાઉ કાપડનું વણાટકામ)`, and agriculture.\n\n### 3. Dravidians `(द्रविड़ / દ્રવિડ પ્રજા)`:\n- Direct creators of **Mohenjo-Daro (Indus Valley) civilization** and Stone Age culture.\n- Gave the sacred concept of God as Father (Lord Shiva) and Goddess as Mother (Parvati).\n- Introduced worship with **Dhup `(धूप / ધૂપ)`**, **Deep `(दीप / દીપ)`**, and **Aarti `(आरती / આરતી)`**.\n- Followed a **Matriarchal Family System `(मातृसत्तात्मक परिवार प्रणाली / માતૃપ્રધાન કુટુંબ વ્યવસ્થા)`**.\n- Developed boat building, spinning, weaving, and dyeing.\n- Later pushed to South India; their modern languages are **Tamil (oldest), Telugu, Kannada, and Malayalam**.\n\n### 4. Mongoloid / Kirat `(मंगोलॉइड / किरात / મોંગોલોઇડ)`:\n- Came from China via Tibet; settled in North Assam, Sikkim, Bhutan, West Bengal.\n- **Physical Features:** Yellow/golden complexion, flat face, chubby cheeks, almond-shaped eyes.\n- Known as **'Kirat `(किरात / કિરાત)'**.\n\n### 5. Alpine, Dinaric and Armenoid `(आल्पाइन, दिनारिक और अर्मेनोइड / આલ્પાઇન, દિનારિક અને આર્મેનોઇડ)`:\n- Migrated from Central Asia.\n- These traits are widely observed in people of Gujarat, Saurashtra, Maharashtra, Bengal, and Odisha.\n\n### 6. Aryans / Nordic `(आर्य / नॉर्डिक / આર્ય પ્રજા)`:\n- Creators of Vedic culture in India; lived in the fertile region of **'Sapta Sindhu' `(सप्त सिंधु / સપ્ત સિંધુ - 7 Rivers)`**.\n- Nature lovers: composed sacred hymns (*Richas / Mantras*) praising the Sun, Wind, Rain, and Dawn.\n- Welcomed all external influences and harmoniously integrated them into the glorious Indian tapestry.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    blocks.append({
        "type": "diagram",
        "title": "Ancient Tribes of India: Visual Comparative Matrix",
        "content": "```\n┌─────────────────┬──────────────────────┬───────────────────────────────────────────┐\n│ TRIBE NAME      │ ORIGIN REGION        │ KEY DISTINGUISHING TRAIT / CONTRIBUTION   │\n├─────────────────┼──────────────────────┼───────────────────────────────────────────┤\n│ 1. Negrito      │ Africa via           │ Black skin, Curly hair, 4-5 ft height     │\n│    (Habsi)      │ Baluchistan          │                                           │\n├─────────────────┼──────────────────────┼───────────────────────────────────────────┤\n│ 2. Australoid   │ South-East Asia      │ Broad head, Flat nose; Clay pottery &     │\n│    (Nishad)     │                      │ Cotton weaving; Kol & Munda tribes        │\n├─────────────────┼──────────────────────┼───────────────────────────────────────────┤\n│ 3. Dravidians   │ Indigenous /         │ Mohenjo-Daro creators; Shiva-Parvati;     │\n│                 │ Indus Valley         │ Dhup-Deep-Aarti; Matriarchal system; Tamil│\n├─────────────────┼──────────────────────┼───────────────────────────────────────────┤\n│ 4. Mongoloid    │ China via Tibet      │ Yellow skin ('Kirat'), Almond-shaped eyes │\n│    (Kirat)      │                      │ Settled in Assam, Sikkim, Bhutan          │\n├─────────────────┼──────────────────────┼───────────────────────────────────────────┤\n│ 5. Aryans       │ Central Asia /       │ Sapta Sindhu; Rigveda & Vedic hymns;      │\n│    (Nordic)     │ Sapta Sindhu         │ Nature worship (Sun, Rain, Dawn)          │\n└─────────────────┴──────────────────────┴───────────────────────────────────────────┘\n```",
        "image_url": "assets/images/ss_ch1_ancient_tribes_table.jpg",
        "alt_text": "Comparative chart of ancient Indian races"
    })

    blocks.append({
        "type": "knowledge_check",
        "question": "Which ancient people gave Indian culture the ritualistic tradition of worshipping deities with Dhup (incense), Deep (lamp), and Aarti?",
        "options": [
            "Aryans",
            "Negrito",
            "Australoid",
            "Dravidians"
        ],
        "correct_answer": "Dravidians",
        "correct_index": 3,
        "explanation": "The Dravidians contributed the profound devotional tradition of worship with Dhup, Deep, and Aarti, along with the concept of Shiva-Parvati as Father and Mother deities."
    })

    blocks.append({
        "type": "common_mistakes",
        "title": "Common Mistake Alert: Australoid vs Negrito",
        "content": "⚠️ **Don't Lose Marks on Tribes:**\n- **Negrito (Habsi):** Came from **Africa** via Baluchistan. Look for keyword: **'Curly hair' `(વાંકડિયા વાળ)`**.\n- **Australoid (Nishad):** Came from **South-East Asia**. Look for keyword: **'Clay utensils & Cotton cloth weaving' `(માટીનાં વાસણો અને સુતરાઉ કાપડ)`**.\n- **Mongoloid (Kirat):** Came from **China/Tibet**. Look for keyword: **'Yellow complexion & Almond eyes' `(પીળો વાન અને બદામ આકારની આંખો)`**.",
        "difficulty": "Intermediate",
        "bloom": "Analyze"
    })

    # ==========================================
    # MODULE 7: PRESERVATION OF OUR HERITAGE
    # ==========================================
    blocks.append({
        "type": "theory",
        "title": "5. Preservation and Conservation of Heritage (Article 51A)",
        "content": "India's heritage has brought global prestige, prosperity, and identity to our nation. Safeguarding it is the moral and legal duty of every citizen.\n\n### Constitutional Duties under Article 51(A) `(અનુચ્છેદ ૫૧ (ક) / अनुच्छेद 51(क))`:\nUnder **Article 51(A)** of the Indian Constitution, **Fundamental Duties `(મૂળભૂત ફરજો / मौलिक कर्तव्य)`** are prescribed. In particular, sub-clauses **(f), (g), and (h)** (in Gujarati: **૬, ૭, ૮** / chha, ja, jha) emphasize heritage preservation:\n\n1. **Clause (f) / (૬):** To value and preserve the rich heritage of our **composite culture `(સમન્વિત સંસ્કૃતિના સમૃદ્ધ વારસાનું મૂલ્ય સમજી તેનું જતન કરવું / हमारी सामासिक संस्कृति की समृद्ध विरासत का सम्मान और संरक्षण)`**.\n2. **Clause (g) / (૭):** To protect and improve the **natural environment** including forests, lakes, rivers, and wildlife, and to have compassion for all living creatures `(જંગલો, તળાવો, નદીઓ અને વન્યપશુ-પક્ષીઓ સહિત કુદરતી પર્યાવરણનું રક્ષણ કરવું)`.\n3. **Clause (h) / (૮):** To safeguard **public property `(જાહેર મિલકતોનું રક્ષણ કરવું)`** and to abjure violence `(હિંસાનો ત્યાગ કરવો)`.\n\nNature has bestowed unprecedented bounty upon India. It is our foremost duty never to deface monuments, pollute sacred rivers, or harm our wild fauna and flora.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "knowledge_check",
        "question": "Which Article of the Constitution of India specifies the Fundamental Duties of citizens regarding the preservation of our rich composite heritage?",
        "options": [
            "Article 21",
            "Article 44",
            "Article 51(A)",
            "Article 370"
        ],
        "correct_answer": "Article 51(A)",
        "correct_index": 2,
        "explanation": "Article 51(A) (clauses f, g, h / ૬, ૭, ૮) explicitly outlines the fundamental duties to value, protect, and preserve the natural and cultural heritage of India."
    })

    # ==========================================
    # MODULE 8: BOARD EXAM MASTERY & HIGH-YIELD HOTS
    # ==========================================
    blocks.append({
        "type": "exam_tips",
        "title": "GSEB Class 10 Board Exam: Top Distinction Table & High-Yield Questions",
        "content": "🔥 **GUARANTEED BOARD EXAM TOPICS (વારંવાર પૂછાતા પ્રશ્નો):**\n\n### Distinction: Natural Heritage vs Cultural Heritage (2 or 3 Marks)\n\n| Point | Natural Heritage `(પ્રાકૃતિક વારસો)` | Cultural Heritage `(સાંસ્કૃતિક વારસો)` |\n| :--- | :--- | :--- |\n| **Origin** | Created entirely by Nature (Divine gift). | Created by humans using intellect & skills. |\n| **Components** | Mountains, rivers, forests, flora, fauna, minerals. | Temples, forts, palaces, stupas, literature, science. |\n| **Examples** | Himalayas, Ganga, Gir Asiatic Lions, Ayurvedic plants. | Rani ki Vav, Lothal, Sun Temple of Modhera, Taj Mahal. |\n| **Relation** | Forms the environmental foundation of life. | Forms the socio-cultural and artistic identity. |\n\n### Important Board Questions Checklist:\n1. **Describe the cultural heritage of Gujarat.** *(Cover Lothal/Dholavira, Rani ki Vav, Modhera Sun Temple, Sidi Saiyyed Jali, and Fairs)*.\n2. **Explain the contributions of Dravidians to Indian culture.** *(Mohenjo-Daro, Shiva-Parvati, Dhup-Deep-Aarti, Matriarchal system, Tamil/Telugu/Kannada/Malayalam)*.\n3. **What are our constitutional duties for preserving heritage under Article 51(A)?** *(Quote clauses f, g, h / ૬, ૭, ૮)*.\n4. **Short note on Australoid (Nishad) and Negrito (Habsi).**",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    blocks.append({
        "type": "summary",
        "title": "Chapter Summary: Heritage of India",
        "content": "✨ **Mastery Recap:**\n- **Bharatvarsha** is our sacred land, defined in Vishnu Purana as lying North of the ocean and South of the snowy Himalayas.\n- **Heritage** is our ancestral gift; **Culture** is our noble way of life.\n- **Natural Heritage** consists of Landscapes, Rivers (Lokmata), Flora (Vegetation), and Fauna (Wildlife).\n- **Cultural Heritage** includes man-made marvels, ancient Harappan towns, and breakthroughs like Zero and the decimal system.\n- **Gujarat's Heritage** shines with Lothal, Dholavira, Rani ki Vav, Modhera Sun Temple, and vibrant fairs like Bhavnath, Tarnetar, and Vautha.\n- **Ancient Tribes** (Negrito, Australoid, Dravidian, Mongoloid, Alpine, Aryan) fused into a composite civilization.\n- **Article 51(A)** commands every citizen to safeguard, cherish, and preserve Bharat's glory for eternity.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    # Target 1: GSEB Class 10 Social Science Ch 1
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_social_science_ch1.json"
    os.makedirs(os.path.dirname(gseb_path), exist_ok=True)
    with open(gseb_path, "w", encoding="utf-8") as f:
        json.dump(final_json, f, indent=2, ensure_ascii=False)
    print(f"Generated GSEB Chapter JSON at: {gseb_path}")
    
    # Target 2: NCERT Class 10 Social Science Ch 1 (Sync copy with updated ID)
    ncert_json = dict(final_json)
    ncert_json["metadata"] = dict(final_json["metadata"])
    ncert_json["metadata"]["id"] = "ncert_class10_social_science_ch1"
    ncert_json["metadata"]["board"] = "NCERT/CBSE/GSEB"
    
    ncert_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_social_science_ch1.json"
    with open(ncert_path, "w", encoding="utf-8") as f:
        json.dump(ncert_json, f, indent=2, ensure_ascii=False)
    print(f"Generated NCERT Chapter JSON at: {ncert_path}")

if __name__ == "__main__":
    generate_supreme_gseb_ss_ch1()
