#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Shine Academy EduOS - Supreme Pedagogy Content Generator
Chapter: GSEB Class 10 Social Science - Chapter 6: Places of Indian Cultural Heritage
Chapter ID: gseb_class10_social_science_ch6 / ncert_class10_social_science_ch6

Adheres strictly to:
- MASTER_CONTENT_STANDARD.yaml
- CHAPTER_STANDARD.yaml
- QUESTION_STANDARD.yaml
- MEDIA_STANDARD.yaml
- EduOS Gold Pedagogy Standard v2.0 (8-Step Learning Cycle, Socratic Discovery Arc, Bilingual Inline Translations)
"""

import json
import os

def generate_supreme_gseb_ss_ch6():
    chapter_id = "gseb_class10_social_science_ch6"
    title = "Chapter 6: Places of Indian Cultural Heritage"
    subtitle = "The Ultimate Board Exam Mastery Guide to India's Monuments, Caves, Temples & Gujarat's Architectural Marvels"

    metadata = {
        "id": chapter_id,
        "title": title,
        "subtitle": subtitle,
        "subject": "Social Science",
        "grade": "10",
        "board": "GSEB/NCERT",
        "curriculum": ["GSEB", "NCERT", "CBSE", "Universal"],
        "language": "English/Hindi/Gujarati (Bilingual)",
        "difficulty": "Advanced",
        "estimated_minutes": 180,
        "version": "3.0.0-SUPREME-PEDAGOGY",
        "author": "Antigravity Supreme Intelligence",
        "reviewed_by": "Chief Academic Architect",
        "tags": [
            "social_science",
            "cultural_heritage",
            "ajanta_caves",
            "ellora_caves",
            "elephanta",
            "mahabalipuram",
            "konark_sun_temple",
            "brihadisvara_temple",
            "qutb_minar",
            "hampi",
            "humayuns_tomb",
            "agra_fort",
            "taj_mahal",
            "red_fort",
            "fatehpur_sikri",
            "modhera_sun_temple",
            "rani_ki_vav",
            "sidi_saiyyed_jali",
            "vadnagar",
            "champaner",
            "char_dham",
            "jyotirlinga",
            "unesco_world_heritage",
            "board_special",
            "bilingual"
        ],
        "learning_outcomes": [
            "Analyze the architectural brilliance, iconography, and historical significance of ancient cave architecture in India (Ajanta, Ellora, and Elephanta).",
            "Understand the Dravidian and Kalinga temple styles including Mahabalipuram Rathas, Konark Sun Temple (Black Pagoda), and Thanjavur's Brihadisvara Temple.",
            "Trace the evolution of Indo-Islamic and Mughal architecture through Qutb Minar, Hampi, Humayun's Tomb, Agra Fort, Taj Mahal, Red Fort, and Fatehpur Sikri.",
            "Explore the rich cultural and architectural heritage of Gujarat including the Modhera Sun Temple, Rani ki Vav (UNESCO World Heritage), Rudra Mahalaya, Sidi Saiyyed Jali, and Vadnagar's Kirti Toran.",
            "Identify India's sacred pilgrimage circuits (Char Dham, 12 Jyotirlingas, 51 Shaktipeeths, Parikramas) and articulate citizens' constitutional duty to preserve heritage under Article 51A(f)."
        ],
        "ai_context": {
            "learning_goal": "Transform the student from a memorizer into a cultural connoisseur and board exam topper. Use vivid hooks, socratic inquiry, architectural breakdown, mnemonics, and bilingual translations `(Hindi / Gujarati)` for complex vocabulary.",
            "common_misconceptions": [
                "Students confuse Kailash Temple (Ellora Cave 16 - rock-cut monolithic) with structural temples built from stone blocks.",
                "Students often mix up Konark Sun Temple (Odisha - Narasimhadeva I) with Modhera Sun Temple (Gujarat - Bhimdev I).",
                "Students confuse Chaityas (Buddhist prayer halls with stupas) with Viharas (residential monasteries for monks).",
                "Students misattribute the construction of Qutb Minar solely to Qutb-ud-din Aibak, forgetting Iltutmish and Firoz Shah Tughlaq.",
                "Students forget that Rani ki Vav is of the 'Jaya' stepwell type with 7 storeys and is depicted on the ₹100 banknote."
            ],
            "tutor_hint": "When students struggle with dates and dynasties, link each monument to a vivid story: the top-down rock chiseling of Kailash Temple, the 24 sundial chariot wheels of Konark, or the 6 km earthen ramp used to hoist the 80-tonne capstone of Brihadisvara."
        }
    }

    blocks = []

    # =========================================================================
    # MODULE 1: THE SOUL OF INDIA'S CAVE ARCHITECTURE (AJANTA, ELLORA, ELEPHANTA)
    # =========================================================================
    
    # Step 1: Hook
    blocks.append({
        "id": "ss_ch6_b01_hook_caves",
        "type": "hook",
        "content": "Imagine standing in pitch darkness inside a massive volcanic cliff over 1,500 years ago. You have no electricity, no modern lasers, and no cranes. Using only a `chisel` `(छेनी / છીણી)`, a `hammer` `(हथौड़ा / હથોડી)`, and bronze mirrors to reflect sunlight into the dark cavern, ancient master sculptors carved out colossal multi-storey monasteries, towering statues of meditating Buddha, and entire monolithic temples out of a single mountain! Welcome to the awe-inspiring world of **Places of Indian Cultural Heritage** `(भारत के सांस्कृतिक विरासत के स्थल / ભારતના સાંસ્કૃતિક વારસાનાં સ્થળો)`!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    # Step 2: Diagram
    blocks.append({
        "id": "ss_ch6_b02_diagram_caves",
        "type": "diagram",
        "content": "Visualizing the two primary types of Buddhist rock-cut cave architecture: **Chaitya** `(चैत्य / ચૈત્ય - Buddhist Prayer Hall with a Stupa at the end)` versus **Vihara** `(विહાર / વિહાર - Residential Monastery with cells for Buddhist monks)`.",
        "image_url": "assets/images/heritage_ajanta_ellora_caves.jpg",
        "alt_text": "Architectural cross-section of Buddhist Chaitya prayer hall and Vihara monastic living quarters carved into mountain rock."
    })

    # Step 3: Theory - Ajanta Caves
    blocks.append({
        "id": "ss_ch6_b03_theory_ajanta",
        "type": "theory",
        "content": "### 1. Ajanta Caves `(अजंता की गुफाएँ / અજંતાની ગુફાઓ)`\n\n* **Location `(स्थान / સ્થળ)`:** Aurangabad (Chhatrapati Sambhaji Nagar) district, Maharashtra, carved along a horseshoe-shaped gorge of the Waghora River.\n* **Total Number of Caves:** **29 rock-cut caves** `(29 शैलकर्तित गुफाएँ / 29 ગુફાઓ)`.\n* **Classification by Function `(કાર્યાત્મક વર્ગીકરણ)`:**\n  1. **Chaityas `(ચૈત્ય - પ્રાર્થના ગૃહ)`:** Cave Numbers **9, 10, 19, 26, and 29** are Chaityas (prayer and worship halls with an apse and stupa).\n  2. **Viharas `(વિહાર - મઠ/નિવાસ સ્થાન)`:** The remaining 24 caves are Viharas (monasteries with central halls and monk cells).\n* **Classification by Period `(કાળક્રમ અનુસાર)`:**\n  * *First Phase:* Built under the **Satavahana dynasty** `(सातवाहन वंश / સાતવાહન વંશ)` (2nd Century BCE).\n  * *Second Phase:* Flourished under the **Vakataka dynasty** `(वाकाटक वंश / વાકાટક વંશ)` (5th Century CE), particularly under King Harishena.\n* **World-Famous Murals & Wall Paintings `(भित्तिचित्र / ભીંતચિત્રો)`:**\n  * Ajanta is globally celebrated for its fresco tempera paintings depicting the life of Lord Buddha and **Jataka Tales** `(जातक कथाएँ / જાતક કથાઓ)`.\n  * Caves **1, 2, 10, 16, and 17** contain the finest masterpieces, including the serene **Bodhisattva Padmapani** `(बोधिसत्व पद्मपाणि / બોધિસત્વ પદ્મપાણિ - Lotus Bearer)` and the moving 'Dying Princess'.\n* **Rediscovery `(પુનઃશોધ)`:** Forgotten for centuries under dense jungle overgrowth, the caves were rediscovered in **1819 CE** by British cavalry officer **Captain John Smith** `(કેપ્ટન જ્હોન સ્મિથ)` during a tiger hunt.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    # Step 4: Theory - Ellora & Elephanta Caves
    blocks.append({
        "id": "ss_ch6_b04_theory_ellora_elephanta",
        "type": "theory",
        "content": "### 2. Ellora Caves `(एलोरा की गुफाएँ / ઇલોરાની ગુફાઓ)`\n\n* **Location:** Aurangabad district, Maharashtra. Total of **34 rock-cut caves** representing a unique confluence of three major Indian faiths:\n  1. **Buddhist Caves `(બૌદ્ધ ગુફાઓ)`:** Caves **1 to 12** (built during 5th–7th Century CE).\n  2. **Hindu Caves `(હિન્દુ ગુફાઓ)`:** Caves **13 to 29** (built during 6th–8th Century CE under Rashtrakuta and Kalachuri patronage).\n  3. **Jain Caves `(જૈન ગુફાઓ)`:** Caves **30 to 34** (built during 9th–10th Century CE, belonging to Digambara sect; famous for Indra Sabha).\n* **Kailash Temple `(कैलाश मंदिर / કૈલાશ મંદિર - Cave No. 16)`:**\n  * The supreme pinnacle of ancient Indian rock-cut architecture!\n  * **Monolithic Wonder `(એકાશ્મ અજાયબી)`:** Carved out of a single monolithic basalt rock cliff, chiselled **from top to bottom** `(ऊपर से नीचे की ओर / ઉપરથી નીચે તરફ)`.\n  * **Dimensions `(માપ)`:** Length = **50 meters**, Width = **33 meters**, Height = **30 meters**.\n  * Commissioned by the **Rashtrakuta King Krishna I** `(રાષ્ટ્રકૂટ રાજા કૃષ્ણ પ્રથમ)` in the 8th century CE, dedicated to Lord Shiva.\n\n---\n\n### 3. Elephanta Caves `(एलिफेंटा की गुफाएँ / એલિફન્ટાની ગુફાઓ)`\n\n* **Location:** Located on Gharapuri Island `(ધારાપુરી ટાપુ)` in the Arabian Sea, 12 km east of Mumbai harbour, Maharashtra.\n* **Origin of Name:** Portuguese voyagers named the island 'Elephanta' after discovering a colossal monolithic stone elephant sculpture near the landing dock.\n* **Number of Caves:** Total of **7 rock-cut caves** dedicated primarily to Lord Shiva.\n* **The Masterpiece - Trimurti Sculpture `(त्रिमूर्ति प्रतिमा / ત્રિમૂર્તિ શિલ્પ - Cave No. 1)`:**\n  * A towering **6-meter (20-foot) high** monolithic sculpture depicting the three cosmic aspects of the Supreme Divinity:\n    1. *Brahma* - The Creator `(સર્જનહાર)`\n    2. *Vishnu* - The Preserver `(પાલનહાર)`\n    3. *Mahesh (Shiva)* - The Destroyer/Transformer `(સંહારક)`\n  * Regarded as one of the world's greatest sculptural achievements. Declared a **UNESCO World Heritage Site** in **1987**.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    # Step 5: Teacher Tip
    blocks.append({
        "id": "ss_ch6_b05_teacher_tip_caves",
        "type": "teacher_tip",
        "content": "💡 **Teacher's Memory Formula:** \n* **Ajanta** = 29 caves = ONLY Buddhism (Chaityas + Viharas).\n* **Ellora** = 34 caves = 3 Religions: **B**uddhist (1-12) + **H**indu (13-29) + **J**ain (30-34). Mnemonic: **BHJ = 12 + 17 + 5 = 34**!\n* **Elephanta** = 7 caves on Gharapuri Island = Famous for 20-foot **Trimurti** (Brahma-Vishnu-Mahesh in Cave 1).",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    # Step 6: Knowledge Check MCQs
    blocks.append({
        "id": "ss_ch6_b06_mcq_kailash",
        "type": "mcq",
        "question": "The world-famous monolithic Kailash Temple (Cave No. 16) at Ellora was carved from top to bottom under the patronage of which dynasty?",
        "options": [
            {"id": "o1", "text": "Rashtrakuta Dynasty (King Krishna I)"},
            {"id": "o2", "text": "Gupta Dynasty (Chandragupta II)"},
            {"id": "o3", "text": "Chola Dynasty (Rajaraja I)"},
            {"id": "o4", "text": "Pallava Dynasty (Narasimhavarman I)"}
        ],
        "correct_option_id": "o1",
        "explanation": "Kailash Temple (Cave 16) at Ellora was commissioned by the Rashtrakuta King Krishna I in the 8th century CE. It is an extraordinary monolithic marvel carved entirely from a single massive rock cliff from top to bottom.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    blocks.append({
        "id": "ss_ch6_b07_mcq_elephanta",
        "type": "mcq",
        "question": "What was the original local name of the island where Elephanta Caves are located in Maharashtra?",
        "options": [
            {"id": "o1", "text": "Salsette Island"},
            {"id": "o2", "text": "Gharapuri Island"},
            {"id": "o3", "text": "Elephanta Island"},
            {"id": "o4", "text": "Bet Dwarka Island"}
        ],
        "correct_option_id": "o2",
        "explanation": "The local inhabitants called the island 'Gharapuri'. Portuguese explorers named it 'Elephanta' after spotting a huge stone statue of an elephant near the shore.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    # =========================================================================
    # MODULE 2: MAJESTIC TEMPLES OF SOUTH & EAST INDIA (MAHABALIPURAM, KONARK, BRIHADISVARA)
    # =========================================================================

    # Step 1: Hook
    blocks.append({
        "id": "ss_ch6_b08_hook_temples",
        "type": "hook",
        "content": "How did ancient architects design a monumental temple in the shape of a colossal chariot with **24 stone wheels** so intricately engineered that the shadows cast by their spokes can tell the exact time of day down to the minute? And how was an **80-tonne solid granite capstone** hoisted to the top of a 216-foot tower in 1010 CE without modern machinery? Let us explore India's glorious temple architecture!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    # Step 2: Diagram
    blocks.append({
        "id": "ss_ch6_b09_diagram_konark_wheel",
        "type": "diagram",
        "content": "The Sundial Wheel of Konark Sun Temple: 12 pairs of wheels represent the 12 months, 7 horses represent the days of the week, and 8 major spokes in each wheel represent the 8 Prahars (3-hour periods) of the 24-hour day.",
        "image_url": "assets/images/heritage_konark_brihadisvara_temples.jpg",
        "alt_text": "Detailed architectural drawing of the Konark Sun Temple chariot wheel with 8 major and 8 minor spokes functioning as a sundial."
    })

    # Step 3: Theory - Mahabalipuram, Konark, and Brihadisvara
    blocks.append({
        "id": "ss_ch6_b10_theory_temples",
        "type": "theory",
        "content": "### 4. Mahabalipuram / Mamallapuram `(महाबलीपुरम / મહાબલીપુરમ)`\n\n* **Location:** Coastal town in Tamil Nadu, 60 km south of Chennai, overlooking the Bay of Bengal.\n* **Patronage:** Established by Pallava King **Narasimhavarman I** `(પલ્લવ રાજા નરસિંહવર્મન પ્રથમ)`, who held the royal title *Mahamalla* `(મહામલ્લ - મહાન યોદ્ધા)`.\n* **Monolithic Ratha Temples `(રથ મંદિરો)`:**\n  * Carved out of single massive granite boulders, named after the Pandavas and Draupadi.\n  * **Dharmaraja Ratha `(ધર્મરાજ રથ)`:** The largest, multi-storeyed and exquisitely sculpted ratha.\n  * **Draupadi Ratha `(દ્રૌપદી રથ)`:** The smallest, shaped like a simple hut.\n  * Originally there were 7 rathas (known as the Seven Pagodas); 2 are believed to be submerged in the sea, while 5 stand prominently.\n* **Open-Air Rock Reliefs:** Features the world's largest open-air bas-relief sculpture: **'Descent of the Ganges'** or **'Arjuna's Penance'** `(ભગીરથની તપસ્યા / અર્જુનનું તપ)` carved on two huge adjacent boulders (27m × 9m), alongside the iconic seaside **Shore Temple** `(તટીય મંદિર)`.\n\n---\n\n### 5. Sun Temple of Konark `(कोणार्क का सूर्य मंदिर / કોણાર્કનું સૂર્યમંદિર)`\n\n* **Location:** Puri district, Odisha, near the coast of the Bay of Bengal.\n* **Construction & Patronage:** Built in the 13th Century CE (around 1250 CE) by **King Narasimhadeva I** `(રાજા નરસિંહદેવ પ્રથમ)` of the **Eastern Ganga Dynasty** `(પૂર્વ ગંગ વંશ)`.\n* **Architectural Conception `(સ્થાપત્ય સંકલ્પના)`:**\n  * Designed in the grand shape of a colossal **Chariot of Surya (Sun God)** `(સૂર્યદેવનો ભવ્ય રથ)`.\n  * **12 Pairs of Intricately Carved Stone Wheels `(12 જોડી પૈડાં = 24 પૈડાં)`:** Symbolize the **12 months of the year**.\n  * **7 Galloping Horses `(7 અશ્વો)`:** Symbolize the **7 days of the week**.\n  * **8 Major Spokes `(8 મુખ્ય આરા)` in each wheel:** Represent the **8 Prahars** `(8 પ્રહર = 24 કલાક)` of the day. The wheels act as an accurate **Astronomical Sundial** `(ધૂપ ઘડી / સૂર્ય ઘડિયાળ)`!\n* **'Black Pagoda' `(કાળા પેગોડા / काला पैगोडा)`:** European sailors referred to this temple as the 'Black Pagoda' because of its dark granite-chlorite stones and prominent dark silhouette seen from the sea.\n\n---\n\n### 6. Brihadisvara Temple `(बृहदेश्वर मंदिर / બૃહદેશ્વર મંદિર)`\n\n* **Location:** Thanjavur (Tanjore), Tamil Nadu.\n* **Patronage:** Built between 1003 and 1010 CE by the great Chola Emperor **Rajaraja I** `(ચોલ સમ્રાટ રાજરાજ પ્રથમ)`. Hence, it is also known as the **Rajarajeswaram Temple**.\n* **Key Architectural Features `(સ્થાપત્યની વિશેષતાઓ)`:**\n  * Dedicated to **Lord Shiva** `(શિવ સમર્પિત - બૃહદીશ્વર એટલે મહાદેવ)`.\n  * **Vimana (Tower) Height:** Soars to a majestic **65 meters (approx. 216 feet)**, making it one of the tallest temple towers in the ancient world.\n  * **The 80-Tonne Shikhara (Apex Capstone):** The single-stone monolithic dome atop the tower weighs **approx. 80 tonnes (80,000 kg)**. To install it in 1010 CE, engineers constructed a gentle **6-kilometer-long inclined earthen ramp `(6 કિમી લાંબો ઢાળવાળો માર્ગ)`** from a nearby village (Sarapallam) to roll the stone to the summit!\n  * Constructed entirely of solid granite in classic **Dravidian architectural style** `(દ્રવિડ સ્થાપત્ય શૈલી)`.",
        "difficulty": "Advanced",
        "bloom": "Understand"
    })

    # Step 4: Exam Tips
    blocks.append({
        "id": "ss_ch6_b11_exam_tips_temples",
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM TOP SCORING SECRETS:**\n1. **Konark Wheel Breakdown:** Total wheels = **24 (12 pairs)**. Meaning: 12 pairs = 12 months. 7 horses = 7 days of the week. 8 major spokes per wheel = 8 prahars (each prahar = 3 hours).\n2. **Black Pagoda vs White Pagoda:** Konark Sun Temple is called 'Black Pagoda' `(કાળા પેગોડા)`, whereas the Jagannath Temple at Puri is called 'White Pagoda' `(સફેદ પેગોડા)`.\n3. **Brihadisvara Temple:** Builder = Chola King Rajaraja I. Height = 65m (216 ft). Capstone = 80 tonnes.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    # Step 5: Knowledge Check MCQs
    blocks.append({
        "id": "ss_ch6_b12_mcq_konark",
        "type": "mcq",
        "question": "In the chariot design of the Konark Sun Temple, what do the 8 major spokes in each wheel symbolize?",
        "options": [
            {"id": "o1", "text": "8 directions of the universe"},
            {"id": "o2", "text": "8 Prahars (3-hour periods) of the 24-hour day"},
            {"id": "o3", "text": "8 planets in the solar system"},
            {"id": "o4", "text": "8 seasons of the ancient calendar"}
        ],
        "correct_option_id": "o2",
        "explanation": "Each of the 24 wheels in Konark Sun Temple features 8 major spokes representing the 8 Prahars of the day (each prahar is approx. 3 hours), serving as an astronomical sundial to measure exact solar time.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "id": "ss_ch6_b13_mcq_brihadisvara",
        "type": "mcq",
        "question": "Which great Chola emperor constructed the majestic Brihadisvara Temple at Thanjavur?",
        "options": [
            {"id": "o1", "text": "Rajendra Chola I"},
            {"id": "o2", "text": "Rajaraja Chola I"},
            {"id": "o3", "text": "Karikala Chola"},
            {"id": "o4", "text": "Kulothunga Chola I"}
        ],
        "correct_option_id": "o2",
        "explanation": "Brihadisvara Temple was constructed between 1003 and 1010 CE by Emperor Rajaraja I of the Chola Dynasty, which is why it was historically known as the Rajarajeswaram Temple.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    # =========================================================================
    # MODULE 3: MEDIEVAL CAPITALS & MONUMENTS (QUTB MINAR, HAMPI, HUMAYUN'S TOMB)
    # =========================================================================

    # Step 1: Hook
    blocks.append({
        "id": "ss_ch6_b14_hook_medieval",
        "type": "hook",
        "content": "Did you know that the capital of the Vijayanagara Empire, **Hampi**, was once so prosperous that diamonds, pearls, and emeralds were sold openly in street market stalls by the kilogram? And did you know that the famous **Humayun's Tomb** in Delhi was the revolutionary architectural 'laboratory' that inspired the design of the Taj Mahal 60 years later? Let's explore these medieval marvels!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    # Step 2: Diagram
    blocks.append({
        "id": "ss_ch6_b15_diagram_qutb_hampi",
        "type": "diagram",
        "content": "Comparing the towering fluted sandstone architecture of **Qutb Minar** in Delhi with the iconic monolithic **Stone Chariot** and musical pillars of Vitthala Temple at **Hampi**.",
        "image_url": "assets/images/heritage_qutb_minar_hampi.jpg",
        "alt_text": "Elevation view of Qutb Minar showing tapering storeys alongside the monolithic Stone Chariot at Hampi."
    })

    # Step 3: Theory - Qutb Minar, Hampi, Humayun's Tomb
    blocks.append({
        "id": "ss_ch6_b16_theory_medieval",
        "type": "theory",
        "content": "### 7. Qutb Minar `(कुतुब मीनार / કુતુબ મિનાર)`\n\n* **Location:** Mehrauli, New Delhi. The world's tallest stone minaret.\n* **Builders & Construction History `(નિર્માણ ઇતિહાસ)`:**\n  * Begun in **1199 CE** by **Qutb-ud-din Aibak** `(કુતુબુદ્દીન ઐબક)` (founder of the Slave/Mamluk Dynasty), who completed only the ground floor.\n  * Completed up to the 4th storey by his son-in-law and successor **Shams-ud-din Iltutmish** `(શમ્સુદ્દીન ઇલ્તુત્મિશ)`.\n  * Later damaged by lightning, the upper storeys were repaired and rebuilt with marble and sandstone by **Firoz Shah Tughlaq** `(ફિરોઝશાહ તુઘલક)`.\n* **Dimensions `(માપ)`:**\n  * **Height:** **72.5 meters** (238 feet).\n  * **Base Circumference/Diameter:** **14.5 meters** at the base, tapering gracefully to **2.75 meters** at the top summit.\n* **Architectural Style:** Fluted red sandstone with balconies supported by stalactite-like brackets, inscribed with elegant Quranic verses in Naskh calligraphy.\n\n---\n\n### 8. Hampi `(हम्पी / હમ્પી)`\n\n* **Location:** Bellary (now Vijayanagara) district, Karnataka, situated on the southern bank of the sacred **Tungabhadra River** `(તુંગભદ્રા નદી)`.\n* **Capital of the Vijayanagara Empire `(વિજયનગર સામ્રાજ્યની રાજધાની)`:**\n  * Flourished from **1336 to 1565 CE**.\n  * Reached its golden apex of glory, art, and literature during the reign of Emperor **Krishnadevaraya** `(રાજા કૃષ્ણદેવરાય - 1509-1529 CE)`.\n* **Key Monuments `(મુખ્ય સ્મારકો)`:**\n  * **Vitthala Temple `(વિઠ્ઠલ મંદિર)`:** Houses the world-renowned monolithic **Stone Chariot `(ગરુડ રથ / પથ્થરનો રથ)`** and 56 musical pillars `(સંગીતમય સ્તંભો)` that emit musical notes (Sa-Re-Ga-Ma) when tapped.\n  * **Virupaksha Temple `(વિરૂપાક્ષ મંદિર)`:** Dedicated to Lord Shiva, with a soaring gopuram (gateway tower).\n  * **Hazara Rama Temple `(હજાર રામ મંદિર)`:** Known for bas-reliefs depicting scenes from the Ramayana.\n\n---\n\n### 9. Humayun's Tomb `(हुमायूँ का मकबरा / હુમાયુનો મકબરો)`\n\n* **Location:** Nizamuddin East, New Delhi.\n* **Patronage:** Built in **1565–1572 CE** by Humayun's senior widow, **Empress Bega Begum** (popularly known as **Haji Begum** `(હાજી બેગમ)`).\n* **Architect:** Designed by Persian master architect **Mirak Mirza Ghiyas** `(મિરાક મિર્ઝા ઘિયાસ)`.\n* **Architectural Significance:**\n  * The **first grand garden-tomb** on the Indian subcontinent, introducing the Persian **Charbagh** `(ચારબાગ શૈલી - ચાર ભાગમાં વિભાજિત બગીચો)` layout.\n  * The first major monument in India to use **red sandstone combined with white marble inlay** and a majestic **double dome** `(બેવડો ગુંબજ)`.\n  * **Prototype of the Taj Mahal:** Served as the direct architectural inspiration and design predecessor for Shah Jahan's Taj Mahal!",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    # Step 4: Teacher Tip
    blocks.append({
        "id": "ss_ch6_b17_teacher_tip_medieval",
        "type": "teacher_tip",
        "content": "💡 **Teacher's Quick Revision Table:**\n* **Qutb Minar:** Height = 72.5 m | Base = 14.5 m | Top = 2.75 m | Started by Aibak, completed by Iltutmish.\n* **Hampi:** River = Tungabhadra | King = Krishnadevaraya | Key feature = Stone Chariot & Musical Pillars at Vitthala Temple.\n* **Humayun's Tomb:** Patron = Haji Begum (Bega Begum) | Style = Charbagh + Double Dome | Known as = 'Precursor to Taj Mahal'.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    # Step 5: Knowledge Check MCQs
    blocks.append({
        "id": "ss_ch6_b18_mcq_hampi",
        "type": "mcq",
        "question": "The legendary ruined city of Hampi, famous for its Stone Chariot, is situated on the banks of which river?",
        "options": [
            {"id": "o1", "text": "Kaveri River"},
            {"id": "o2", "text": "Tungabhadra River"},
            {"id": "o3", "text": "Krishna River"},
            {"id": "o4", "text": "Godavari River"}
        ],
        "correct_option_id": "o2",
        "explanation": "Hampi, the magnificent capital of the Vijayanagara Empire, is situated on the southern banks of the Tungabhadra River in Karnataka.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    blocks.append({
        "id": "ss_ch6_b19_mcq_humayun",
        "type": "mcq",
        "question": "Who commissioned the construction of Humayun's Tomb in Delhi, which served as the prototype for the Taj Mahal?",
        "options": [
            {"id": "o1", "text": "Nur Jahan"},
            {"id": "o2", "text": "Mumtaz Mahal"},
            {"id": "o3", "text": "Haji Begum (Bega Begum)"},
            {"id": "o4", "text": "Gulbadan Begum"}
        ],
        "correct_option_id": "o3",
        "explanation": "Humayun's Tomb was commissioned by Humayun's senior widow Empress Bega Begum (Haji Begum) in 1565 CE, designed in the Persian Charbagh style by architect Mirak Mirza Ghiyas.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    # =========================================================================
    # MODULE 4: THE GOLDEN AGE OF MUGHAL ARCHITECTURE (AGRA FORT, TAJ MAHAL, RED FORT, FATEHPUR SIKRI)
    # =========================================================================

    # Step 1: Hook
    blocks.append({
        "id": "ss_ch6_b20_hook_mughal",
        "type": "hook",
        "content": "Imagine a structure of such breathtaking perfection that the world calls it an eternal 'Poem in White Marble'. Over 20,000 master craftsmen from across Asia worked for 22 years to build it. Yet, the emperor who built it spent the last years of his life as a prisoner in an octagonal marble tower of Agra Fort, gazing through a small window across the Yamuna River at his beloved's tomb. Let's delve into the immortal saga of Mughal architecture!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    # Step 2: Diagram
    blocks.append({
        "id": "ss_ch6_b21_diagram_taj_redfort",
        "type": "diagram",
        "content": "Architectural Layout of Mughal Grandeur: The symmetrical Charbagh complex of the **Taj Mahal** on the Yamuna riverbank, and the fortified bastions of the **Red Fort** and **Fatehpur Sikri's Buland Darwaza**.",
        "image_url": "assets/images/heritage_taj_mahal_red_fort.jpg",
        "alt_text": "Detailed architectural elevations of the Taj Mahal, Agra Fort, Red Fort of Delhi, and Buland Darwaza of Fatehpur Sikri."
    })

    # Step 3: Theory - Agra Fort, Taj Mahal, Red Fort, Fatehpur Sikri
    blocks.append({
        "id": "ss_ch6_b22_theory_mughal",
        "type": "theory",
        "content": "### 10. Agra Fort `(आगरा का किला / આગ્રાનો કિલ્લો)`\n\n* **Location:** Agra, Uttar Pradesh, on the right bank of the Yamuna River.\n* **Patronage:** Built in **1565 CE** by Mughal Emperor **Akbar** `(અકબર)` using vibrant red sandstone.\n* **Architectural Features:**\n  * Enclosed by a 70-foot-high massive double-fortified wall.\n  * **Jahangiri Mahal `(જહાંગીરી મહેલ)`:** Built by Akbar for his son Jahangir, showcasing a harmonious blend of Bengali and Gujarati architectural motifs with wooden beams.\n  * **Musamman Burj `(મુસમ્મન બુરજ)`:** A delicate octagonal marble tower overlooking the Yamuna River where **Shah Jahan** was confined during his final 8 years by his son Aurangzeb, gazing wistfully at the Taj Mahal.\n\n---\n\n### 11. Taj Mahal `(ताज महल / તાજ મહાલ)`\n\n* **Location:** Agra, Uttar Pradesh, on the banks of the Yamuna River.\n* **Patronage & Dedication:** Built by Mughal Emperor **Shah Jahan** `(શાહજહાં)` in eternal memory of his beloved wife **Mumtaz Mahal** `(મુમતાઝ મહલ - Arjumand Banu Begum)`, who passed away in 1631 CE.\n* **Construction Timeline:** Started in **1631 CE** and completed in **1653 CE** (took **22 years** and over 20,000 artisans). Chief architect was **Ustad Ahmad Lahori** `(ઉસ્તાદ અહમદ લાહોરી)`.\n* **Architectural Masterpiece:**\n  * Built entirely of pure white **Makrana marble** `(મકરાણાનો સફેદ આરસપહાણ)` brought from Rajasthan.\n  * Set upon a massive elevated marble plinth, flanked by 4 slender minarets slightly tilted outwards (so they would not fall on the main dome in an earthquake).\n  * Decorated with intricate **Pietra Dura** `(पच्चीकारी / પચ્ચીકારી - जड़ाऊ काम)` inlay of precious and semi-precious stones forming floral arabesques.\n  * Inscribed over the grand entrance gate: *'Pious hearts are welcomed into the Garden of Paradise'* `(સ્વર્ગના બગીચામાં પવિત્ર દિલોનું સ્વાગત છે)`.\n  * Recognized globally as one of the **Seven Wonders of the Modern World** and a UNESCO World Heritage Site.\n\n---\n\n### 12. Red Fort of Delhi `(लाल किला, दिल्ली / લાલ કિલ્લો, દિલ્હી)`\n\n* **Location:** Old Delhi (Shahjahanabad).\n* **Patronage:** Built in **1638 CE** by **Shah Jahan** when he relocated the Mughal imperial capital from Agra to Delhi.\n* **Key Palaces & Structures:**\n  * Built of sturdy red sandstone in an irregular octagonal shape.\n  * **Diwan-i-Aam `(દીવાન-એ-આમ)`:** Hall of public audience.\n  * **Diwan-i-Khas `(દીવાન-એ-ખાસ)`:** Hall of private audience with exquisite marble pillars, once inscribed with the Persian couplet: *'If there is a paradise on earth, it is here, it is here, it is here.'*\n  * **Takht-e-Taoos (Peacock Throne) `(मयूर सिंहासन / મયૂર સિંહાસન)`:** The legendary gold and jewel-encrusted throne crafted by **Bebadal Khan** `(બેબદલ ખાન)`, later looted by Persian invader **Nadir Shah** `(નાદિર શાહ)` in 1739 CE.\n  * **National Significance:** Every year on **Independence Day (15th August)**, the Prime Minister of India unfurls the National Tricolour `(રાષ્ટ્રધ્વજ ફરકાવે છે)` and addresses the nation from the ramparts of the Red Fort.\n\n---\n\n### 13. Fatehpur Sikri `(फतेहपुर सीकरी / ફતેહપુર સીકરી)`\n\n* **Location:** 26 miles (approx. 40 km) west of Agra, Uttar Pradesh.\n* **Patronage:** Founded in **1569 CE** by Emperor **Akbar** in honour of the venerated Sufi Saint **Sheikh Salim Chishti** `(શેખ સલીમ ચિશ્તી)`.\n* **Buland Darwaza `(बुलंद दरवाज़ा / બુલંદ દરવાજો)`:**\n  * The **highest and grandest gateway in the world**!\n  * **Dimensions:** **50 meters high** and **43 meters wide**.\n  * Built by Akbar in 1573 CE to commemorate his historic **Victory over Gujarat `(ગુજરાત વિજયની યાદમાં)`**.\n* **Other Major Structures:** White marble Tomb of Sheikh Salim Chishti, Panch Mahal (5-storey tiered palace), Jodha Bai's Palace, Birbal's Palace, and the **Ibadat Khana** `(ઇબાદતખાના - પ્રાર્થના અને ધર્મચર્ચા ગૃહ)`.",
        "difficulty": "Advanced",
        "bloom": "Understand"
    })

    # Step 4: Exam Tips
    blocks.append({
        "id": "ss_ch6_b23_exam_tips_mughal",
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM GUARANTEED QUESTIONS:**\n1. **Buland Darwaza:** Built by Akbar at Fatehpur Sikri to celebrate his **Gujarat Victory**. Height = **50 meters**, Width = **43 meters**.\n2. **Peacock Throne (Takht-e-Taoos):** Placed in Diwan-i-Khas of Delhi Red Fort, created by Bebadal Khan, plundered by Nadir Shah.\n3. **Taj Mahal Chief Architect:** Ustad Ahmad Lahori. Construction time = 22 years (1631–1653 CE).",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    # Step 5: Knowledge Check MCQs
    blocks.append({
        "id": "ss_ch6_b24_mcq_buland_darwaza",
        "type": "mcq",
        "question": "Why did Emperor Akbar construct the majestic Buland Darwaza (50m high) at Fatehpur Sikri?",
        "options": [
            {"id": "o1", "text": "To celebrate his military victory over Gujarat"},
            {"id": "o2", "text": "To commemorate the birth of Prince Salim"},
            {"id": "o3", "text": "To mark his coronation as Emperor of India"},
            {"id": "o4", "text": "To celebrate the treaty with Mewar"}
        ],
        "correct_option_id": "o1",
        "explanation": "Akbar constructed the Buland Darwaza (the highest gateway in the world, 50m high and 43m wide) at Fatehpur Sikri in 1573 CE to commemorate his decisive conquest of Gujarat.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    blocks.append({
        "id": "ss_ch6_b25_mcq_peacock_throne",
        "type": "mcq",
        "question": "Which foreign invader plundered the legendary Peacock Throne (Takht-e-Taoos) from the Red Fort of Delhi in 1739 CE?",
        "options": [
            {"id": "o1", "text": "Ahmad Shah Abdali"},
            {"id": "o2", "text": "Nadir Shah of Persia"},
            {"id": "o3", "text": "Timur Lang"},
            {"id": "o4", "text": "Mahmud of Ghazni"}
        ],
        "correct_option_id": "o2",
        "explanation": "The Persian ruler Nadir Shah invaded Delhi in 1739 CE and plundered the gemstone-studded Peacock Throne (Takht-e-Taoos) along with the Koh-i-Noor diamond from the Red Fort.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    # =========================================================================
    # MODULE 5: ARCHITECTURAL JEWELS & HERITAGE OF GUJARAT
    # =========================================================================

    # Step 1: Hook
    blocks.append({
        "id": "ss_ch6_b26_hook_gujarat",
        "type": "hook",
        "content": "Step inside an underground palace of water—a 7-storey subterranean inverted temple carved deep into the earth, adorned with over 500 sculpted masterpieces of Lord Vishnu. So breathtaking is this monument that UNESCO declared it a World Heritage Site, and the Reserve Bank of India placed its image on the ₹100 banknote! Welcome to the glorious heritage of our home state, **Gujarat**!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    # Step 2: Diagram
    blocks.append({
        "id": "ss_ch6_b27_diagram_gujarat_heritage",
        "type": "diagram",
        "content": "The Architectural Treasures of Gujarat: The solar-aligned sanctum of **Modhera Sun Temple**, the 7-level subterranean **Rani ki Vav** in Patan, the delicate filigree of **Sidi Saiyyed Jali**, and **Vadnagar's Kirti Toran**.",
        "image_url": "assets/images/heritage_gujarat_modhera_rani_ki_vav.jpg",
        "alt_text": "Collage of Gujarat's architectural marvels: Modhera Sun Temple, Rani ki Vav stepwell, Sidi Saiyyed Jali stone latticework, and Kirti Toran at Vadnagar."
    })

    # Step 3: Theory - Gujarat's Cultural Heritage Sites
    blocks.append({
        "id": "ss_ch6_b28_theory_gujarat",
        "type": "theory",
        "content": "### 14. Cultural Heritage Places of Gujarat `(ગુજરાતના સાંસ્કૃતિક વારસાનાં સ્થળો)`\n\n#### A. Modhera Sun Temple `(મોઢેરાનું સૂર્યમંદિર)`\n* **Location:** Modhera, Mehsana district, Gujarat, on the banks of the Pushpavati River.\n* **Patronage:** Built in **1026–27 CE** during the golden reign of **King Bhimdev I** `(સોલંકી રાજા ભીમદેવ પ્રથમ)` of the Solanki (Chalukya) Dynasty.\n* **Astronomical Precision `(ખગોળીય રચના)`:**\n  * The sanctum is oriented precisely east so that on the equinoxes, the **first ray of the rising sun** `(સૂર્યનું પ્રથમ કિરણ)` pierced directly into the Garbhagriha to illuminate the gemstone on the crown of the Sun God's idol, lighting up the entire sanctum!\n  * The exterior walls display **12 distinct carved forms of Aditya (Sun God)** `(સૂર્યની 12 વિવિધ મૂર્તિઓ)` showcasing Iranian sculptural influence.\n* **Surya Kund `(સૂર્યકુંડ)`:** A magnificent rectangular stepped water tank in front of the temple surrounded by **108 miniature carved shrines** `(108 નાનાં મંદિરો)` creating a dazzling sight during twilight.\n\n---\n\n#### B. Rani ki Vav, Patan `(રાણકી વાવ, પાટણ)`\n* **Patronage:** Built in the 11th century (approx. 1063 CE) by **Queen Udayamati** `(રાણી ઉદયમતી)` in loving memory of her deceased husband King Bhimdev I.\n* **Architectural Marvel:**\n  * A **7-storeyed subterranean stepwell** `(સાત માળની ભવ્ય વાવ)` built in the Maru-Gurjara architectural style.\n  * Classified as a **Jaya-type stepwell** `(જયા પ્રકારની વાવ - ત્રણ પ્રવેશદ્વાર)`.\n  * Features over **500 principal sculptures** `(500 થી વધુ મુખ્ય શિલ્પો)` and 1,000 minor ones, predominantly depicting the **Dashavatara** `(દશાવતાર - 10 avatars of Lord Vishnu)` including Varaha, Vamana, Narasimha, and Rama, along with celestial Apsaras.\n* **Global Recognition:** Declared a **UNESCO World Heritage Site in 2014**, and proudly featured on the reverse side of India's new **₹100 banknote** `(₹100 ની નવી ચલણી નોટ પર સ્થાન)`.\n\n---\n\n#### C. Rudra Mahalaya, Siddhpur `(રુદ્ર મહાલય, સિદ્ધપુર)`\n* **Location:** Siddhpur, Patan district, on the banks of the Saraswati River.\n* **Patronage:** Initiated by **Mulraj Solanki** `(મૂળરાજ સોલંકી)` and completed in grandeur by **Siddharaj Jaisinh** `(સિદ્ધરાજ જયસિંહ)`.\n* Dedicated to Lord Shiva (Rudra). Though in ruins today, its soaring pillars, torans, and multi-storeyed sanctum reflect the unmatched scale of Solanki architecture.\n\n---\n\n#### D. Vadnagar `(વડનગર)`\n* An ancient historic town in Mehsana district with over 2,500 years of unbroken continuous habitation.\n* Famous for the **Kirti Toran `(કીર્તિ તોરણ)`** - two majestic ornamental triumphal gateway arches (40 feet high) carved out of yellow sandstone without mortar.\n* Home to the serene Sharmistha Lake and the samadhi/memorial of the legendary twin music sisters **Tana and Riri `(તાના અને રીરી)`**, who sang Raga Malhar to save Tansen from the burning fire caused by singing Raga Deepak.\n\n---\n\n#### E. Sidi Saiyyed Mosque, Ahmedabad `(સીદી સૈયદની જાળી, અમદાવાદ)`\n* Built in **1572–73 CE** by Sidi Saiyyed in the reign of Shams-ud-din Muzaffar Shah III.\n* World-renowned for its exquisite **semi-circular stone latticework screens** `(સીદી સૈયદની જાળી / Tree of Life)` carved with filigree precision from single slabs of yellow sandstone depicting intertwining tree branches and foliage.\n\n---\n\n#### F. Champaner `(ચાંપાનેર)`\n* Located at the foot of Pavagadh hill in Panchmahal district.\n* Captured in 1484 CE by **Sultan Mahmud Begada** `(સુલતાન મહમૂદ બેગડો)`, who made it his capital and named it **Muhammadabad** `(મહમૂદાબાદ)`.\n* Famous for the Jami Masjid, Sahar ki Masjid, and fortified gates. Designated as Gujarat's **first UNESCO World Heritage Site in 2004**.\n\n---\n\n#### G. Other Iconic Cultural Heritage in Gujarat:\n* **Dholavira `(ધોળાવીરા - કચ્છ)`:** Harappan planned city with world's oldest rainwater harvesting reservoirs, 3-tier town planning, and 10-letter sign board (UNESCO World Heritage 2021).\n* **Lothal `(લોથલ - અમદાવાદ)`:** World's oldest known tidal dockyard `(ધક્કો / ગોદી)` and maritime trade port of the Indus Valley Civilization.\n* **Junagadh `(જૂનાગઢ)`:** Uparkot Fort, Rock Edicts of Emperor Ashoka `(અશોકનો શિલાલેખ - બ્રાહ્મી લિપિ)`, Buddhist Caves of Khambhalida and Talaja, Adi-Kadi Vav, and Navghan Kuvo.\n* **Palitana `(પાલીતાણા - ભાવનગર)`:** Situated on Shatrunjaya Hills, featuring **863 marble Jain temples** `(863 જૈન મંદિરોનું પવિત્ર ધામ)`.",
        "difficulty": "Advanced",
        "bloom": "Understand"
    })

    # Step 4: Teacher Tip
    blocks.append({
        "id": "ss_ch6_b29_teacher_tip_vavs",
        "type": "teacher_tip",
        "content": "💡 **Types of Stepwells (Vavs) in Ancient Indian Vastu Shastra:**\n1. **Nanda `(નંદા)`:** 1 entrance `(એક પ્રવેશદ્વાર)`\n2. **Bhadra `(ભદ્રા)`:** 2 entrances `(બે પ્રવેશદ્વાર)`\n3. **Jaya `(જયા)`:** 3 entrances `(ત્રણ પ્રવેશદ્વાર - Example: Rani ki Vav, Patan)`\n4. **Vijaya `(વિજયા)`:** 4 entrances `(ચાર પ્રવેશદ્વાર)`",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    # Step 5: Knowledge Check MCQs
    blocks.append({
        "id": "ss_ch6_b30_mcq_rani_ki_vav",
        "type": "mcq",
        "question": "Which queen of the Solanki Dynasty constructed the world-famous 7-storeyed stepwell 'Rani ki Vav' at Patan?",
        "options": [
            {"id": "o1", "text": "Queen Minaldevi"},
            {"id": "o2", "text": "Queen Udayamati"},
            {"id": "o3", "text": "Queen Naikidevi"},
            {"id": "o4", "text": "Queen Jodha Bai"}
        ],
        "correct_option_id": "o2",
        "explanation": "Rani ki Vav at Patan was commissioned in the 11th century by Queen Udayamati in memory of her late husband King Bhimdev I. It was declared a UNESCO World Heritage Site in 2014.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    blocks.append({
        "id": "ss_ch6_b31_mcq_modhera",
        "type": "mcq",
        "question": "During whose reign was the Sun Temple of Modhera constructed in 1026-27 CE?",
        "options": [
            {"id": "o1", "text": "Siddharaj Jaisinh"},
            {"id": "o2", "text": "Bhimdev I (Solanki Dynasty)"},
            {"id": "o3", "text": "Mulraj Solanki"},
            {"id": "o4", "text": "Kumarapala"}
        ],
        "correct_option_id": "o2",
        "explanation": "The Sun Temple of Modhera in Mehsana district was constructed in 1026–27 CE during the reign of King Bhimdev I of the Solanki Dynasty.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    # =========================================================================
    # MODULE 6: SACRED PILGRIMAGES, CIRCUITS & PRESERVING OUR HERITAGE
    # =========================================================================

    # Step 1: Hook
    blocks.append({
        "id": "ss_ch6_b32_hook_pilgrimage",
        "type": "hook",
        "content": "From the snow-covered peaks of Badrinath in the north to the roaring ocean waves of Rameshwaram in the south, ancient Indians wove our vast nation together through sacred pilgrimage trails known as the **Char Dham** and **12 Jyotirlingas**. Why did our ancestors place these spiritual anchors at the four corners of India? Let's discover the sacred geography of India!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    # Step 2: Diagram
    blocks.append({
        "id": "ss_ch6_b33_diagram_char_dham",
        "type": "diagram",
        "content": "Map of India's Sacred Pilgrimage Geography: The Four Cardinal Abodes of **Char Dham** and the sacred **12 Jyotirlingas** connecting every region of India.",
        "image_url": "assets/images/heritage_char_dham_jyotirlinga_map.jpg",
        "alt_text": "Geographical map of India illustrating the locations of Badrinath, Dwarka, Puri, Rameshwaram, and the 12 Jyotirlingas."
    })

    # Step 3: Theory - Pilgrimages & Heritage Preservation
    blocks.append({
        "id": "ss_ch6_b34_theory_pilgrimages",
        "type": "theory",
        "content": "### 15. Sacred Pilgrimage Places of India `(ભારતનાં તીર્થસ્થાનો)`\n\n#### A. The Four Cardinal Abodes - Char Dham `(ચાર ધામ)`:\nEstablished by Adi Shankaracharya in the 8th century CE to unite India spiritually:\n1. **North `(ઉત્તર)`:** **Badrinath** `(બદ્રીનાથ - ઉત્તરાખંડ)` - Dedicated to Lord Vishnu.\n2. **West `(પશ્ચિમ)`:** **Dwarkadhish** `(દ્વારકાધીશ - ગુજરાત)` - On the Gomti River/Arabian Sea.\n3. **East `(પૂર્વ)`:** **Jagannath Puri** `(જગન્નાથ પુરી - ઓડિશા)` - Dedicated to Lord Jagannath.\n4. **South `(દક્ષિણ)`:** **Rameshwaram** `(રામેશ્વરમ - તમિળનાડુ)` - Dedicated to Lord Shiva (Ramanathaswamy).\n\n---\n\n#### B. The 12 Sacred Jyotirlingas `(૧૨ પવિત્ર જ્યોતિર્લિંગ)`:\n* **Somnath `(સોમનાથ - પ્રભાસ પાટણ, ગુજરાત)`:** The very first `(પ્રથમ જ્યોતિર્લિંગ)` of all 12 Jyotirlingas.\n* **Nageshwar `(નાગેશ્વર - દ્વારકા નજીક, ગુજરાત)`**\n* **Mallikarjuna** (Srisailam, Andhra Pradesh), **Mahakaleshwar** (Ujjain, MP), **Omkareshwar** (MP), **Kedarnath** (Uttarakhand), **Bhimashankar** (Maharashtra), **Kashi Vishwanath** (Varanasi, UP), **Trimbakeshwar** (Nashik, Maharashtra), **Vaidyanath** (Deoghar, Jharkhand), **Rameshwaram** (Tamil Nadu), **Grishneshwar** (Ellora, Maharashtra).\n\n---\n\n#### C. Sacred Parikramas `(પવિત્ર પરિક્રમાઓ)`:\n* **Narmada Parikrama `(નર્મદા પરિક્રમા)`:** The circumnavigation of the sacred Narmada River.\n* **Girnar Lili Parikrama `(ગિરનારની લીલી પરિક્રમા - જૂનાગઢ)`:** Annual circumambulation of Mount Girnar covering 36 km during Kartik Sud 11 to 15.\n* **Shatrunjaya Parikrama `(શેત્રુંજય પરિક્રમા - પાલીતાણા)`**.\n\n---\n\n### 16. Preservation of Heritage & Constitutional Duty `(વારસાનું જતન અને બંધારણીય ફરજ)`\n\n* **Article 51A(f) of the Constitution of India `(ભારતીય બંધારણની કલમ 51A(f))`:**\n  * It is the fundamental duty of every citizen of India to *'value and preserve the rich heritage of our composite culture'* `(આપણી સમન્વિત સંસ્કૃતિના સમૃદ્ધ વારસાનું મૂલ્ય સમજી તેનું જતન કરવાની પ્રત્યેક નાગરિકની મૂળભૂત ફરજ છે)`.\n* **Why Must We Preserve Our Heritage?**\n  1. Our monuments are the living identity and pride of our glorious civilization.\n  2. Heritage tourism generates massive foreign exchange and employment for millions.\n  3. They serve as timeless inspirations for art, science, engineering, and cultural unity.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    # Step 4: Summary & Board Exam HOTS
    blocks.append({
        "id": "ss_ch6_b35_hots_summary",
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HIGH-ORDER THINKING (HOTS) MASTER TABLE:**\n\n| Monument | State / Location | Builder / Dynasty | Unique Feature |\n| :--- | :--- | :--- | :--- |\n| **Ajanta Caves** | Aurangabad, MH | Satavahana & Vakataka | 29 Caves (Buddhist), Padmapani Bodhisattva |\n| **Ellora Caves** | Aurangabad, MH | Rashtrakuta (Krishna I) | 34 Caves (3 Religions), Monolithic Kailash Temple |\n| **Elephanta** | Mumbai, MH | Silhara / Rashtrakuta | 7 Caves, 20-foot Trimurti (Cave 1) |\n| **Mahabalipuram** | Tamil Nadu | Narasimhavarman I (Pallava) | 5 Rathas (Dharmaraja largest), Arjuna's Penance |\n| **Konark Sun Temple**| Puri, Odisha | Narasimhadeva I (Ganga) | Black Pagoda, 24 wheels (sundials), 7 horses |\n| **Brihadisvara** | Thanjavur, TN | Rajaraja I (Chola) | 65m tower, 80-tonne single granite capstone |\n| **Qutb Minar** | New Delhi | Qutb-ud-din Aibak & Iltutmish | 72.5m tall stone minaret, fluted sandstone |\n| **Hampi** | Karnataka | Krishnadevaraya (Vijayanagara)| Stone Chariot, 56 Musical Pillars at Vitthala Temple |\n| **Humayun's Tomb** | New Delhi | Haji Begum (Mirak Mirza Ghiyas)| Charbagh garden tomb, Precursor to Taj Mahal |\n| **Taj Mahal** | Agra, UP | Shah Jahan (Ustad Ahmad Lahori)| White Makrana marble, 22 years, 7 Wonders |\n| **Buland Darwaza** | Fatehpur Sikri, UP | Akbar | 50m high (Highest Gateway), Gujarat Victory |\n| **Modhera Sun Temple**| Mehsana, Gujarat | Bhimdev I (Solanki) | Solstice sun alignment, 108 shrines in Surya Kund |\n| **Rani ki Vav** | Patan, Gujarat | Queen Udayamati | 7-storey Jaya stepwell, UNESCO 2014, ₹100 note |\n| **Sidi Saiyyed Jali** | Ahmedabad, Gujarat | Sidi Saiyyed | Tree of Life stone filigree latticework |",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    # Step 5: Final Comprehensive Practice MCQs
    blocks.append({
        "id": "ss_ch6_b36_mcq_char_dham",
        "type": "mcq",
        "question": "Which of the following is NOT one of the traditional Four Cardinal Cardinal Abodes (Char Dham) established in India?",
        "options": [
            {"id": "o1", "text": "Badrinath (Uttarakhand)"},
            {"id": "o2", "text": "Dwarkadhish (Gujarat)"},
            {"id": "o3", "text": "Jagannath Puri (Odisha)"},
            {"id": "o4", "text": "Ujjain Mahakaleshwar (Madhya Pradesh)"}
        ],
        "correct_option_id": "o4",
        "explanation": "The traditional Char Dham at the four corners of India are Badrinath (North), Dwarkadhish (West), Jagannath Puri (East), and Rameshwaram (South). Ujjain Mahakaleshwar is one of the 12 Jyotirlingas, not one of the Char Dham.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "id": "ss_ch6_b37_mcq_article51a",
        "type": "mcq",
        "question": "Which Article of the Indian Constitution makes it the fundamental duty of every citizen to value and preserve our rich composite cultural heritage?",
        "options": [
            {"id": "o1", "text": "Article 21"},
            {"id": "o2", "text": "Article 51A(f)"},
            {"id": "o3", "text": "Article 44"},
            {"id": "o4", "text": "Article 19(1)(a)"}
        ],
        "correct_option_id": "o2",
        "explanation": "Article 51A(f) of the Constitution of India explicitly mandates that it shall be the duty of every citizen of India to value and preserve the rich heritage of our composite culture.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    # Final Chapter Payload Assembly
    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }

    # Target Output 1: GSEB Class 10 Social Science Chapter 6
    gseb_output_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_social_science_ch6.json"
    os.makedirs(os.path.dirname(gseb_output_path), exist_ok=True)
    with open(gseb_output_path, "w", encoding="utf-8") as f:
        json.dump(final_json, f, indent=2, ensure_ascii=False)
    print(f"Successfully generated: {gseb_output_path}")

    # Target Output 2: NCERT Class 10 Social Science Chapter 6
    ncert_output_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_social_science_ch6.json"
    final_json_ncert = json.loads(json.dumps(final_json))
    final_json_ncert["metadata"]["id"] = "ncert_class10_social_science_ch6"
    with open(ncert_output_path, "w", encoding="utf-8") as f:
        json.dump(final_json_ncert, f, indent=2, ensure_ascii=False)
    print(f"Successfully synced: {ncert_output_path}")

if __name__ == "__main__":
    generate_supreme_gseb_ss_ch6()
