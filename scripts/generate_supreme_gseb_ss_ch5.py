import json
import os

def generate_supreme_gseb_ss_ch5():
    chapter_id = "gseb_class10_social_science_ch5"
    title = "Chapter 5: India's Heritage of Science and Technology"
    
    metadata = {
        "id": chapter_id,
        "title": title,
        "subtitle": "The Ultimate Board Exam Mastery Guide - Supreme Gold Pedagogy",
        "subject": "Social Science",
        "grade": "10",
        "board": "GSEB/NCERT",
        "curriculum": ["Universal", "GSEB", "NCERT", "CBSE"],
        "language": "English/Hindi/Gujarati (Bilingual)",
        "difficulty": "Advanced",
        "estimated_minutes": 180,
        "version": "3.0.0-SUPREME-PEDAGOGY",
        "author": "Antigravity Supreme Intelligence",
        "reviewed_by": "Chief Academic Architect",
        "tags": [
            "social_science",
            "heritage_of_science_and_technology",
            "ancient_india",
            "metallurgy",
            "chemistry",
            "nagarjuna",
            "charak",
            "sushrut",
            "aryabhata",
            "varahamihira",
            "vastu_shastra",
            "board_special",
            "bilingual"
        ],
        "learning_outcomes": [
            "Analyze the profound scientific heritage and practical discoveries gifted to humanity by ancient Indian sages `(ऋषि-मुनि / ઋષિમુનિઓ)`.",
            "Explain ancient Indian achievements in Metallurgy `(धातु विद्या / ધાતુવિદ્યા)`, from the Indus Valley Dancing Girl to the rust-free Mehrauli Iron Pillar.",
            "Describe the pioneering chemistry `(रसायन शास्त्र / રસાયણશાસ્ત્ર)` of Acharya Nagarjuna and Nalanda University's research laboratories.",
            "Evaluate ancient Indian mastery in Medical Science `(चिकित्सा विज्ञान / વૈદકવિદ્યા)` and Surgery `(शल्य चिकित्सा / શલ્યચિકિત્સા)` by Maharshi Charak, Maharshi Sushrut, and Vagbhatta.",
            "Understand India's monumental gifts to world Mathematics `(गणित शास्त्र / ગણિતશાસ્ત્ર)`: Zero ('0'), the Decimal System, Algebra, and the value of Pi (π).",
            "Examine the astronomical breakthroughs and astrological classifications by Aryabhata and Varahamihira.",
            "Appreciate the systematic architectural science of Vastu Shastra `(वास्तु शास्त्र / વાસ્તુશાસ્ત્ર)` and its modern global adoption.",
            "Ace GSEB/CBSE Board Exam questions with structured answers, high-order thinking skills (HOTS), and memory mnemonics."
        ],
        "ai_context": {
            "learning_goal": "Transform the student into a confident scholar who appreciates the profound scientific and technological heritage of ancient India. Use step-by-step Socratic inquiry, vivid diagrams, bilingual glossaries with backtick translations, and board exam secrets.",
            "common_misconceptions": [
                "Students mistakenly assume that modern plastic surgery and cataract removal began exclusively in modern Europe, not knowing that Maharshi Sushrut performed rhinoplasty and used 121+ specialized surgical instruments in ancient India.",
                "Students confuse Acharya Nagarjuna (the great chemist and author of Rasaratnakara) with other scholars or mix up Charak Samhita with Sushrut Samhita.",
                "Students confuse Astronomy `(खगोल शास्त्र / ખગોળશાસ્ત્ર)` (scientific study of stars and planets) with Astrology `(ज्योतिष शास्त्र / જ્યોતિષશાસ્ત્ર)` (predictive science based on planetary movements).",
                "Students often mix up the authors of mathematical treatises (e.g., Bhaskaracharya authored Lilavati Ganita and Bijaganita, while Aryabhata authored Aryabhatiya)."
            ],
            "tutor_hint": "Use mnemonic pairing tables: Charak ➔ 2000 Herbs; Sushrut ➔ 121 Surgical Tools & Rhinoplasty; Nagarjuna ➔ Mercury Ash (Parad Bhasma) & Rasaratnakara; Aryabhata ➔ Zero, Pi (3.1416), Earth's Rotation; Varahamihira ➔ Panchasiddhantika, Brihat Samhita (Tantra, Hora, Samhita); Vishwakarma ➔ 8 Sections of Vastu Shastra. Highlight the rust-free Mehrauli Iron Pillar as living proof of advanced ancient metallurgy."
        }
    }

    blocks = []

    # =========================================================================
    # MODULE 1: HOOK & INTRODUCTION TO ANCIENT INDIAN SCIENCE
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "Imagine standing in front of a giant iron pillar `(लौह स्तंभ / લોહસ્તંભ)` standing in open Delhi air for over **1,600 years**—beaten by scorching heat, torrential monsoon rains, and winter frost—yet without a SINGLE speck of rust `(जंग / કાટ)`! How could ancient Indian scientists achieve a metallurgical miracle that even modern metallurgical engineers study with awe? \n\nAncient India was not merely a land of spiritual philosophies and sacred scriptures; it was a vibrant powerhouse of **Science `(विज्ञान / વિજ્ઞાન - Systematic Knowledge)`** and **Technology `(प्रौद्योगिकी / પ્રૌદ્યોગિકી / ટેકનોલોજી - Practical Application)`**. Let's embark on an unforgettable journey through India's glorious heritage of Science and Technology!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "diagram",
        "content": "The Pillars of Ancient Indian Scientific Heritage: How ancient sages seamlessly integrated experimental science, mathematics, medicine, and architecture.",
        "image_url": "assets/images/gseb_ss_ch5_heritage_overview.jpg",
        "alt_text": "Mind map connecting Metallurgy, Chemistry, Surgery, Mathematics, Astronomy, and Vastu Shastra in Ancient India."
    })

    blocks.append({
        "type": "theory",
        "content": "### 🌟 Science and Technology in Ancient India\n\nAncient Indian sages `(ऋषि-मुनि / ઋષિમુનિઓ)` made monumental contributions to world civilization. Western scholars and modern researchers have enthusiastically acknowledged that ancient India pioneered core discoveries across multiple scientific disciplines.\n\n- **Science `(विज्ञान / વિજ્ઞાન)`:** Means systematic, organized knowledge `(व्यवस्थित ज्ञान / વ્યવસ્થિત જ્ઞાન)`.\n- **Technology `(प्रौद्योगिकी / પ્રૌદ્યોગિકી)`:** Means the practical and applied utility of scientific knowledge `(विज्ञान का व्यावहारिक उपयोग / વિજ્ઞાનનો વ્યવહારિક ઉપયોગ)`.\n\nAncient India achieved remarkable breakthroughs in **Metallurgy `(धातु विद्या / ધાતુવિદ્યા)`**, **Chemistry `(रसायन शास्त्र / રસાયણશાસ્ત્ર)`**, **Medical Science `(चिकित्सा विज्ञान / વૈદકવિદ્યા)`**, **Surgery `(शल्य चिकित्सा / શલ્યચિકિત્સા)`**, **Mathematics `(गणित शास्त्र / ગણિતશાસ્ત્ર)`**, **Astronomy `(खगोल शास्त्र / ખગોળશાસ્ત્ર)`**, **Astrology `(ज्योतिष शास्त्र / જ્યોતિષશાસ્ત્ર)`**, and **Vastu Shastra `(वास्तु शास्त्र / વાસ્તુશાસ્ત્ર)`**.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Teacher's Secret Insight:** In Board Exams, questions often ask: *'Explain the difference between Science and Technology and state the branches where ancient India contributed.'* Always write the exact one-line definitions of Science and Technology, followed by bulleted points for all 8 scientific fields!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    # =========================================================================
    # MODULE 2: METALLURGY (धातु विद्या / ધાતુવિદ્યા)
    # =========================================================================
    blocks.append({
        "type": "theory",
        "content": "### ⚒️ 1. Metallurgy `(धातु विद्या / ધાતુવિદ્યા)`\n\nFrom pre-historic times, the people of India applied metallurgy in their practical everyday lives. India's metallurgical heritage is proven by ancient artifacts spanning thousands of years:\n\n1. **Indus Valley Civilization:** A world-famous bronze statue of a **Dancing Girl `(नर्तकी की कांस्य प्रतिमा / નર્તકીની કાંસ્ય પ્રતિમા)`** discovered at Mohenjo-daro proves that metal casting `(धातु ढलाई / ધાતુ ઢાળકામ)` was mastered more than 4,500 years ago.\n2. **Kushan Dynasty (તક્ષશિલા):** Statues of Lord Buddha `(भगवान बुद्ध की प्रतिमाएँ / ભગવાન બુદ્ધની પ્રતિમાઓ)` belonging to the Kushan period were found at Takshashila `(तक्षशिला / તક્ષશિલા)`.\n3. **South India & Chola Dynasty `(चोल काल / ચોલ વંશ)`:** Metal idol craftsmanship reached its golden zenith in South India during the 10th to 11th century.\n   - The internationally acclaimed bronze masterpiece of **Lord Nataraja (Shiva) `(नटराज की मूर्ति / નટરાજની પ્રતિમા)`** in cosmic dance is preserved in the Chennai Museum `(चेन्नई संग्रहालय / ચેન્નઈ સંગ્રહાલય)`.\n   - Another magnificent bronze statue of **Dhanushdhari Rama (Rama holding bow and arrow) `(धनुर्धारी राम / ધનુર્ધારી રામ)`** is also preserved in the Chennai Museum.\n4. **Immense Statues of Lord Buddha:**\n   - **Sultanganj (Bhagalpur, Bihar) `(सुल्तानगंज / સુલતાનગંજ)`:** A copper statue of Lord Buddha standing **7.5 feet high** and weighing **1 ton**.\n   - **Nalanda `(नालंदा / નાલંદા)`:** A colossal copper statue of Lord Buddha standing **18 feet high**.\n5. **Artistic & Household Artifacts:** Exquisitely cast statues of gods, goddesses, animals, birds, artistic oil lamps `(दीपक / દીવાઓ)`, and ornate betel-nut cutters `(सुपारी काटने की सरोती / સોપારી કાપવાની સુડી)`.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "diagram",
        "content": "The Legendary Mehrauli Iron Pillar (Delhi) - 1,600+ years of rust-free metallurgical excellence built during the reign of King Chandragupta II (Vikramaditya).",
        "image_url": "assets/images/gseb_ss_ch5_iron_pillar.jpg",
        "alt_text": "The rust-free Mehrauli Iron Pillar in Delhi standing against the Qutub Minar backdrop."
    })

    blocks.append({
        "type": "theory",
        "content": "### 🏛️ The Wonder of World Metallurgy: Mehrauli Iron Pillar\n\n- **Builder:** Erected by King **Chandragupta II (Vikramaditya) `(चंद्रगुप्त द्वितीय / ચંદ્રગુપ્ત બીજો)`** in Delhi (Mehrauli).\n- **Dimensions & Weight:** It is **24 feet high** and weighs approximately **7 tonnes (approx. 6,500 - 7,000 kg)**.\n- **Unmatched Scientific Feat:** Despite standing in the open atmosphere under intense summer heat, torrential rains, and winter frost for over **1,600 years**, it has not rusted at all `(जंग रहित / કાટ લાગ્યો નથી)`!\n- It remains an astonishing testimony to ancient India's advanced knowledge of protective oxide coatings and iron smelting technology.",
        "difficulty": "Intermediate",
        "bloom": "Analyze"
    })

    blocks.append({
        "type": "mcq",
        "content": "Where is the world-famous bronze statue of Lord Nataraja preserved?",
        "options": [
            "National Museum, New Delhi",
            "Chennai Museum, Tamil Nadu",
            "Nalanda Museum, Bihar",
            "Prince of Wales Museum, Mumbai"
        ],
        "correct_answer": "Chennai Museum, Tamil Nadu",
        "explanation": "The world-renowned bronze statue of Lord Nataraja (cosmic dancer Shiva) and the statue of Dhanushdhari Rama are preserved in the Chennai Museum.",
        "distractor_rationale": "Nalanda Museum holds copper Buddha artifacts; Delhi and Mumbai museums hold other antiquities, but the Chola bronze Nataraja masterpiece is at Chennai Museum."
    })

    blocks.append({
        "type": "mcq",
        "content": "What is the height and weight of the copper statue of Lord Buddha discovered at Sultanganj (Bihar)?",
        "options": [
            "18 feet high, 2 tonnes",
            "7.5 feet high, 1 tonne",
            "24 feet high, 7 tonnes",
            "10 feet high, 500 kg"
        ],
        "correct_answer": "7.5 feet high, 1 tonne",
        "explanation": "The Sultanganj copper Buddha is 7.5 feet high and weighs 1 tonne. (The Nalanda Buddha statue is 18 feet high, and the Mehrauli Iron Pillar is 24 feet high and 7 tonnes).",
        "distractor_rationale": "24 feet and 7 tonnes refers to the Mehrauli Iron Pillar, while 18 feet refers to the Nalanda Buddha statue."
    })

    # =========================================================================
    # MODULE 3: CHEMISTRY (रसायन शास्त्र / રસાયણશાસ્ત્ર)
    # =========================================================================
    blocks.append({
        "type": "theory",
        "content": "### 🧪 2. Chemistry `(रसायन शास्त्र / રસાયણશાસ્ત્ર)`\n\nChemistry is an **applied and experimental science `(प्रयोगात्मक विज्ञान / પ્રયોગાત્મક વિજ્ઞાન)`**. It deals with the study of minerals, plants, agricultural seeds, manufacturing of metals, alloys, and medicinal solutions.\n\n#### 👨‍🔬 Acharya Nagarjuna: The Pioneer of Indian Chemistry\n- **Identity:** A great Buddhist scholar and the pride of **Nalanda University `(नालंदा विश्वविद्यालय / નાલંદા વિદ્યાપીઠ)`**.\n- **Father of Chemistry:** Known as the pioneer / Father of Indian Chemistry `(भारतीय रसशास्त्र के प्रणेता / ભારતીય રસાયણશાસ્ત્રના પ્રણેતા)`.\n- **Monumental Books:** Authored **'Rasaratnakara' `(रस रत्नाकर / રસરત્નાકર)`** and **'Arogyamanjari' `(आरोग्यमंजरी / આરોગ્યમંજરી)`**.\n- **Pioneering Medical Innovation:** Acharya Nagarjuna was the first to advocate the use of **Mercury Ash (Parad Bhasma) `(पारे की भस्म / પારાની ભસ્મ)`** as medicine alongside traditional herbal remedies!\n- **Nalanda's Research Infrastructure:** Nalanda University had its own dedicated chemical laboratories `(रसायनशाला / રસાયણશાળા)` and specialized furnaces `(भट्ठियाँ / ભઠ્ઠીઓ)` for research and experiments.\n- **Treatises & Classifications:** Ancient texts describe **8 main Rasas `(मुख्य रस)`**, **8 Uparasas `(उपरस)`**, **10 types of Poisons `(विष)`**, various Alkalis/Salts `(क्षार)`, and ash of metals `(धातु भस्म)`.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Memory Hook for Acharya Nagarjuna:** \nRemember: **N-R-A-M**\n- **N** ➔ **N**agarjuna\n- **R** ➔ **R**asaratnakara (Book on Chemistry/Alchemy)\n- **A** ➔ **A**rogyamanjari (Book on Health & Medicine)\n- **M** ➔ **M**ercury Ash `(पारे की भस्म / પારાની ભસ્મ)` used as medicine for the first time!",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "mcq",
        "content": "Who advocated the use of Mercury Ash (पारे की भस्म / પારાની ભસ્મ) as medicine for the first time?",
        "options": [
            "Maharshi Charak",
            "Acharya Nagarjuna",
            "Maharshi Sushrut",
            "Varahamihira"
        ],
        "correct_answer": "Acharya Nagarjuna",
        "explanation": "Acharya Nagarjuna of Nalanda University pioneered the use of Mercury Ash (Parad Bhasma) alongside herbal medicines.",
        "distractor_rationale": "Maharshi Charak pioneered herbal medicine (Charak Samhita), Sushrut pioneered surgery, and Varahamihira was an astronomer/astrologer."
    })

    # =========================================================================
    # MODULE 4: MEDICAL SCIENCE & SURGERY (વૈદકવિદ્યા અને શલ્યચિકિત્સા)
    # =========================================================================
    blocks.append({
        "type": "theory",
        "content": "### 🩺 3. Medical Science and Surgery `(चिकित्सा एवं शल्य चिकित्सा / વૈદકવિદ્યા અને શલ્યચિકિત્સા)`\n\nFrom ancient times, India achieved unmatched mastery in medicine and surgery through the **'Trinity of Ayurveda' (Brihat Trayi)**:\n\n1. **Maharshi Charak `(महर्षि चरक / મહર્ષિ ચરક)`:**\n   - Wrote the monumental **'Charak Samhita' `(चरक संहिता / ચરક સંહિતા)`**.\n   - Documented over **2,000 medicinal plants, herbs, and roots `(औषधीय पौधे / ઔષધીય વનસ્પતિઓ)`** with their therapeutic uses.\n\n2. **Maharshi Sushrut `(महर्षि सुश्रुत / મહર્ષિ સુશ્રુત)` - The Father of Surgery:**\n   - Wrote the legendary **'Sushrut Samhita' `(सुश्रुत संहिता / સુશ્રુત સંહિતા)`**.\n   - Described **121+ specialized surgical instruments `(शल्य क्रिया के यंत्र / શસ્ત્રક્રિયાના સાધનો)`**—some so razor-sharp that they could split a single strand of human hair longitudinally into two parts!\n   - Pioneered complex surgical operations: **Plastic Surgery / Rhinoplasty `(प्लास्टिक सर्जरी - नाक और कान की सर्जरी)`**, Cataract removal `(मोतियाबिंद का ऑपरेशन / મોતિયો ઉતારવો)`, extraction of Bladder Stones `(पथरी निकालना / પથરીનું ઓપરેશન)`, Hernia `(हर्निया)`, Cesarean delivery `(प्रसव शल્યક્રિયા / પ્રસૂતિ શસ્ત્રક્રિયા)`, and resetting fractured bones `(हड्डी जोड़ना / હાડકાં સાંધવા)`.\n   - **Training Methods:** Ancient Indian surgeons trained student doctors by performing surgical cuts and dissections on **dead bodies `(शव / મૃતદેહ)`**, wax models, and fruits/vegetables like bottle gourds and watermelons before operating on living patients!\n\n3. **Vagbhatta `(वाग्भट्ट / વાગ્ભટ્ટ)`:**\n   - Wrote **'Ashtanga Hridaya' `(अष्टांग हृदय / અષ્ટાંગ હૃદય)`** and **'Ashtanga Samgraha' `(अष्टांग संग्रह / અષ્ટાંગ સંગ્રહ)`**, creating invaluable diagnostic frameworks for physicians.\n\n4. **Veterinary Science `(पशु चिकित्सा / પશુ ચિકિત્સા)`:**\n   - **Shalihotra `(शालिहोत्र / શાલિહોત્ર)`:** Wrote **'Ashwashastra' / 'Haya Shastra' `(अश्वशास्त्र / અશ્વશાસ્ત્ર)`** on the anatomy and diseases of horses.\n   - **Palakapya `(पालकाप्य / પાલકાપ્ય)`:** Wrote **'Hasti Ayurveda' `(हस्ती आयुर्वेद / હસ્તી આયુર્વેદ)`** on diseases and treatment of elephants.",
        "difficulty": "Advanced",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "diagram",
        "content": "The Ancient Indian Surgical & Medical Arsenal: Sushrut's 121+ surgical instruments and the Ayurvedic Trinity.",
        "image_url": "assets/images/gseb_ss_ch5_sushrut_instruments.jpg",
        "alt_text": "Illustration showing ancient surgical tools from Sushrut Samhita and herbal preparations from Charak Samhita."
    })

    blocks.append({
        "type": "memory_trick",
        "content": "🧠 **Ayurveda Treatises Memory Formula:**\n- **Charak** ➔ **Charak Samhita** (C = Care with Herbs / 2000+ plants)\n- **Sushrut** ➔ **Sushrut Samhita** (S = Surgery / 121+ Sharp Instruments)\n- **Vagbhatta** ➔ **Ashtanga Hridaya** (V = Vital Diagnostic Summary)\n- **Shalihotra** ➔ **Ashwashastra** (Horses `[अश्व / ઘોડા]`)\n- **Palakapya** ➔ **Hasti Ayurveda** (Elephants `[हाथी / હાથી]` - Hasti)",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "mcq",
        "content": "Which ancient scholar wrote 'Hasti Ayurveda', dedicated to the treatment of elephant diseases?",
        "options": [
            "Shalihotra",
            "Palakapya",
            "Vagbhatta",
            "Maharshi Charak"
        ],
        "correct_answer": "Palakapya",
        "explanation": "Palakapya authored 'Hasti Ayurveda' for elephant ailments, while Shalihotra authored 'Ashwashastra' for horses.",
        "distractor_rationale": "Shalihotra is for horses (Ashwashastra); Charak and Vagbhatta focused on human medicine."
    })

    # =========================================================================
    # MODULE 5: MATHEMATICS (गणित शास्त्र / ગણિતશાસ્ત્ર)
    # =========================================================================
    blocks.append({
        "type": "theory",
        "content": "### 🔢 4. Mathematics `(गणित शास्त्र / ગણિતશાસ્ત્ર)`\n\nIndia has gifted humanity its most revolutionary mathematical discoveries: **Zero ('0')**, the **Decimal System `(दशमलव पद्धति / દશાંશ પદ્ધતિ)`**, **Algebra `(बीजगणित / બીજગણિત)`**, **Arithmetic `(अंकगणित / અંકગણિત)`**, and **Geometry `(रेखागणित / શુલ્બ સૂત્ર / ભૂમિતિ)`**.\n\n#### 🌟 Great Indian Mathematicians and Their Breakthroughs:\n\n1. **Discovery of Zero ('0') & Numerals:**\n   - **Zero ('0') `(शून्य / શૂન્ય)`** was discovered in India by **Aryabhata `(आर्यभट्ट / આર્યભટ્ટ)`**.\n   - **Sage Grutsamada `(ऋषि गृत्समद / ઋષિ ગૃતસમદ)`** discovered the method of placing zeroes after numerical figures to write astronomical numbers (up to 53 zeroes behind 1!).\n   - Decimal Place Value System `(दशांश पद्धति)` was devised by ancient Indian mathematicians, enabling global commerce and modern computing.\n\n2. **Aryabhata - The Father of Indian Mathematics:**\n   - Authored the immortal works **'Aryabhatiya' `(आर्यभटीय / આર્યભટીય)`** and **'Daspagitika' `(दशगीतिका / દશગીતિકા)`**.\n   - Calculated the precise mathematical constant **Pi (π)** as **22/7 or 3.1416** (the ratio of a circle's circumference `[परिधि / પરિઘ]` to its diameter `[व्यास / વ્યાસ]`).\n   - Proved that the Earth is spherical and rotates on its own axis `(अपनी धुरी पर घूमना / પોતાની ધરી પર પરિભ્રમણ)`, which causes day and night.\n   - Scientifically proved that a lunar eclipse `(चंद्रग्रहण / ચંદ્રગ્રહણ)` occurs due to the shadow of the Earth falling on the Moon, shattering ancient superstitions of dragons/demons (Rahu-Ketu).\n\n3. **Bhaskaracharya (1150 AD) `(भास्कराचार्य / ભાસ્કરાચાર્ય)`:**\n   - Wrote legendary mathematical treatises: **'Lilavati Ganita' `(लीलावती गणित / લીલાવતી ગણિત)`** (focused on arithmetic) and **'Bijaganita' `(बीजगणित / બીજગણિત)`** (focused on algebra).\n   - Introduced operational signs for **Addition (+)** and **Subtraction (-)**.\n\n4. **Brahmagupta `(ब्रह्मगुप्त / બ્રહ્મગુપ્ત)`:**\n   - Wrote **'Brahmasphuta Siddhanta' `(ब्रह्मस्फुट सिद्धांत / બ્રહ્મસ્ફુટ સિદ્ધાંત)`**, introducing various types of algebraic equations and the mathematical concept of gravitation.\n\n5. **Bodhayana & Apastamba `(बोधायन एवं आपस्तंब / બોધાયન અને આપસ્તંબ)`:**\n   - Wrote **'Shulba Sutras' `(शुल्ब सूत्र / શુલ્બ સૂત્ર)`** (800 BCE), which laid down geometric measurements for designing Vedic sacrificial fire altars (Yajna Kunds) long before Pythagoras.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    blocks.append({
        "type": "diagram",
        "content": "The Value of Pi (π) and Decimal System: Aryabhata's calculation of Circumference / Diameter = 3.1416.",
        "image_url": "assets/images/gseb_ss_ch5_maths_aryabhata.jpg",
        "alt_text": "Mathematical diagram illustrating circle circumference to diameter ratio discovered by Aryabhata."
    })

    blocks.append({
        "type": "mcq",
        "content": "Who calculated the value of Pi (π) as 22/7 (3.1416) in his treatise 'Aryabhatiya'?",
        "options": [
            "Bhaskaracharya",
            "Aryabhata",
            "Brahmagupta",
            "Grutsamada"
        ],
        "correct_answer": "Aryabhata",
        "explanation": "Aryabhata discovered that Pi (π) is the constant ratio of circumference to diameter (3.1416) and authored 'Aryabhatiya'.",
        "distractor_rationale": "Bhaskaracharya wrote Lilavati Ganita; Brahmagupta wrote Brahmasphuta Siddhanta; Grutsamada discovered writing numerals after zero."
    })

    blocks.append({
        "type": "mcq",
        "content": "Which famous mathematical book on arithmetic was written by Bhaskaracharya in 1150 AD?",
        "options": [
            "Aryabhatiya",
            "Lilavati Ganita",
            "Brahmasphuta Siddhanta",
            "Panchasiddhantika"
        ],
        "correct_answer": "Lilavati Ganita",
        "explanation": "Bhaskaracharya authored 'Lilavati Ganita' (Arithmetic) and 'Bijaganita' (Algebra) in 1150 AD.",
        "distractor_rationale": "Aryabhatiya was by Aryabhata; Brahmasphuta Siddhanta was by Brahmagupta; Panchasiddhantika was by Varahamihira."
    })

    # =========================================================================
    # MODULE 6: ASTRONOMY & ASTROLOGY (ખગોળશાસ્ત્ર અને જ્યોતિષશાસ્ત્ર)
    # =========================================================================
    blocks.append({
        "type": "theory",
        "content": "### 🌌 5. Astronomy and Astrology `(खगोल शास्त्र एवं ज्योतिष शास्त्र / ખગોળશાસ્ત્ર અને જ્યોતિષશાસ્ત્ર)`\n\n**Astronomy `(खगोल शास्त्र / ખગોળશાસ્ત્ર)`** is the most ancient of all sciences. Ancient Indian scholars established astronomical observatories `(वेधशालाएँ / વેધશાળાઓ)` to calculate planetary movements, star constellations, eclipses, and time cycles.\n\n#### 🌠 Aryabhata's Astronomical Triumphs:\n- Declared that the Earth rotates on its own axis.\n- Proved that the lunar eclipse occurs due to the Earth's shadow.\n- In recognition of his incomparable contributions to science, independent India named its **first artificial satellite 'Aryabhata'** (launched in 1975)!\n\n#### 🔭 Varahamihira - The Great Astronomer & Astrologer:\n- **Treatises:** Authored the monumental **'Panchasiddhantika' `(पंचसिद्धांतिका / પંચસિદ્ધાંતિકા)`**, **'Brihat Samhita' `(बृहत् संहिता / બૃહત્ સંહિતા)`**, and **'Brihat Jataka' `(बृहत् जातक / બૃહત્ જાતક)`**.\n- **Threefold Division of Astrology:** Varahamihira divided astrology into **three distinct branches**:\n  1. **Tantra `(तंत्र / તંત્ર)`:** Mathematical calculations of celestial bodies and planetary motions.\n  2. **Hora `(होरा / હોરા)`:** Natal astrology and personal horoscopes based on planetary positions at birth.\n  3. **Samhita `(संहिता / સંહિતા)`:** General astrology predicting weather phenomena, rainfall, crop yields, famines, and earthquakes `(भूकंप / ભૂકંપ)` based on celestial configurations.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Exam Golden Tip on Varahamihira:** \nWhenever a 3-mark question asks about Varahamihira's contribution, structure your answer into: \n1. **Treatises:** Panchasiddhantika, Brihat Samhita, Brihat Jataka.\n2. **Three Branches:** Tantra (Maths/Planets), Hora (Horoscope), Samhita (Weather/Earthquakes/Crops).\n3. **Significance:** Showed the planetary influence on human life and nature.",
        "difficulty": "Intermediate",
        "bloom": "Apply"
    })

    blocks.append({
        "type": "mcq",
        "content": "Into how many sections/branches did Varahamihira divide astrology in his treatises?",
        "options": [
            "Two branches (Tantra and Hora)",
            "Three branches (Tantra, Hora, and Samhita)",
            "Four branches (Tantra, Hora, Samhita, and Vastu)",
            "Eight branches (Ashtanga)"
        ],
        "correct_answer": "Three branches (Tantra, Hora, and Samhita)",
        "explanation": "Varahamihira divided astrology into three branches: Tantra (astronomical calculations), Hora (natal astrology), and Samhita (weather and mundane events).",
        "distractor_rationale": "Eight branches refers to Vastu Shastra by Vishwakarma or Ashtanga Ayurveda; Varahamihira divided astrology specifically into 3 parts."
    })

    # =========================================================================
    # MODULE 7: VASTU SHASTRA (વાસ્તુશાસ્ત્ર / वास्तु शास्त्र)
    # =========================================================================
    blocks.append({
        "type": "theory",
        "content": "### 🏛️ 6. Vastu Shastra `(वास्तु शास्त्र / વાસ્તુશાસ્ત્ર)`\n\nVastu Shastra is an invaluable and unique architectural science gifted by ancient India to the world. It combines civil engineering, town planning, direction alignment, energy flow, and spiritual balance.\n\n#### 📜 History and Pioneers of Vastu Shastra:\n- **Pioneering Sages:** Ancient masters like **Brahma, Narada, Brihaspati, Bhrigu, Vashishtha, and Vishwakarma `(विश्वकर्मा / વિશ્વકર્મા)`** developed the principles of Vastu Shastra.\n- **Lord Vishwakarma:** Regarded as the **First Divine Architect of the Universe `(देवताओं के प्रथम शिल्पी / દેવોના પ્રથમ સ્થપતિ)`**. He systematically divided Vastu Shastra into **8 distinct sections `(8 भाग / 8 વિભાગો)`**.\n- **Revival by Rana Kumbha:** In the 15th century, **King Rana Kumbha of Mewar `(मेवाड़ के राणा कुंभा / મેવાડના રાણા કુંભા)`** revived and modernized Vastu Shastra by revising and structuring ancient texts.\n\n#### 📐 Key Topics Covered in Vastu Shastra:\n1. **Selection of Land `(भूमि चयन / જમીનની પસંદગી)`:** Testing soil type, fertility, slope, and surroundings.\n2. **Shapes of Plots `(आकार / પ્લોટનો આકાર)`:** Square, rectangular, etc.\n3. **Internal Layout of Buildings:** Precise positioning of the **Pooja Room `(मंदिर / પૂજા ખંડ)`**, **Kitchen `(रसोईघर / રસોડું - Agni Corner)`**, **Bedrooms `(शयनकक्ष / શયનખંડ)`**, **Treasury `(तिजोरी / તિજોરી - North/Kuber)`**, **Dining Room**, and **Main Entrance `(मुख्य द्वार / મુખ્ય દ્વાર)`**.\n4. **Global Adoption:** In modern times, foreigners and international architectural firms have recognized Vastu Shastra's scientific principles and actively implement it in modern buildings!",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "diagram",
        "content": "Vastu Purusha Mandala & Directional Mapping: Principles of ancient Indian spatial architecture and energy alignment.",
        "image_url": "assets/images/gseb_ss_ch5_vastu_mandala.jpg",
        "alt_text": "Vastu Shastra directional diagram showing Northeast for Pooja, Southeast for Kitchen, Southwest for Master Bedroom, and North for Wealth."
    })

    blocks.append({
        "type": "mcq",
        "content": "Who revived and restructured the ancient science of Vastu Shastra in the 15th century?",
        "options": [
            "King Chandragupta II",
            "King Rana Kumbha of Mewar",
            "Acharya Nagarjuna",
            "King Ashoka"
        ],
        "correct_answer": "King Rana Kumbha of Mewar",
        "explanation": "In the 15th century, King Rana Kumbha of Mewar revived and improved the ancient treatise of Vastu Shastra.",
        "distractor_rationale": "Chandragupta II built the Iron Pillar; Nagarjuna pioneered chemistry; Ashoka built stupas and pillars."
    })

    # =========================================================================
    # MODULE 8: CULTURAL & SCIENTIFIC SYNTHESIS + BOARD EXAM HOTS
    # =========================================================================
    blocks.append({
        "type": "theory",
        "content": "### 🇮🇳 7. Conclusion: Synthesis of Science and Culture\n\nAncient India never viewed Science and Spirituality as enemies. Instead, Indian culture maintained a **holistic and scientific outlook `(समन्वित और वैज्ञानिक दृष्टिकोण / સમન્વયકારી અને વૈજ્ઞાનિક દ્રષ્ટિકોણ)`**:\n\n- Spiritual rituals incorporated profound scientific truths (e.g., copper vessels for purifying drinking water, turmeric and neem for antibacterial healing, Vastu alignment for sunlight and cross-ventilation).\n- India gave the world tolerance, non-violence, zero, surgery, metallurgy, and cosmic astronomy.\n- Today's generation must take immense pride in our rich scientific heritage and strive to lead the world once again in science and technology!",
        "difficulty": "Beginner",
        "bloom": "Evaluate"
    })

    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM TOP SCORING SECRETS (Board Paper Super-HOTS!):**\n\n1. **Long Question (4 Marks): 'Write a detailed note on ancient India's contribution to Medical Science and Surgery.'**\n   - *Structure:* Paragraph 1 for Maharshi Charak (Charak Samhita, 2000 herbs), Paragraph 2 for Maharshi Sushrut (Sushrut Samhita, 121 instruments, plastic surgery, cataract, dead body practice), Paragraph 3 for Vagbhatta (Ashtanga Hridaya), Paragraph 4 for Veterinary Science (Shalihotra & Palakapya).\n\n2. **Short Note (2-3 Marks): 'Explain India's heritage in Metallurgy.'**\n   - *Must Mention:* Indus Valley Dancing Girl, Takshashila Kushan Buddha, Sultanganj 7.5ft Copper Buddha, Nalanda 18ft Buddha, Chennai Museum Bronze Nataraja & Rama, and Delhi Mehrauli 24ft/7 tonne Rust-free Iron Pillar.\n\n3. **Objective 1-Marker Traps:**\n   - Father of Indian Chemistry ➔ Acharya Nagarjuna\n   - Creator of Zero & Pi ➔ Aryabhata\n   - 3 Parts of Astrology ➔ Varahamihira\n   - First Divine Architect / 8 Sections of Vastu ➔ Vishwakarma\n   - Revival of Vastu in 15th Century ➔ Rana Kumbha of Mewar",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    blocks.append({
        "type": "reflection",
        "content": "🤔 **Socratic Thought Challenge:** \nThink about the Mehrauli Iron Pillar standing for 1,600 years without rust, or Sushrut performing plastic surgery without modern electronic machines. What does this tell us about the experimental scientific attitude of our ancient ancestors? How can we apply their spirit of deep research and curiosity in our studies today?",
        "difficulty": "Advanced",
        "bloom": "Create"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }

    # Save to GSEB Class 10 Social Science Chapter 5
    gseb_out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_social_science_ch5.json"
    os.makedirs(os.path.dirname(gseb_out_path), exist_ok=True)
    with open(gseb_out_path, "w", encoding="utf-8") as f:
        json.dump(final_json, f, indent=2, ensure_ascii=False)
    print(f"Generated GSEB Chapter at: {gseb_out_path}")

    # Also save to NCERT Class 10 Social Science Chapter 5 for multi-curriculum synchronization
    ncert_out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_social_science_ch5.json"
    final_json_ncert = dict(final_json)
    final_json_ncert["metadata"] = dict(final_json["metadata"])
    final_json_ncert["metadata"]["id"] = "ncert_class10_social_science_ch5"
    with open(ncert_out_path, "w", encoding="utf-8") as f:
        json.dump(final_json_ncert, f, indent=2, ensure_ascii=False)
    print(f"Generated NCERT Chapter at: {ncert_out_path}")

if __name__ == "__main__":
    generate_supreme_gseb_ss_ch5()
