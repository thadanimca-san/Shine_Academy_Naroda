import json
import os

def generate_supreme_gseb_ss_ch4():
    chapter_id = "gseb_class10_social_science_ch4"
    title = "Chapter 4: Cultural Heritage of India: Literature"
    
    metadata = {
        "id": chapter_id,
        "title": title,
        "subtitle": "The Ultimate Board Exam Mastery & Heritage Deep-Dive",
        "subject": "Social Science",
        "grade": "10",
        "board": "GSEB / NCERT",
        "curriculum": ["GSEB", "CBSE", "Universal"],
        "language": "English/Hindi/Gujarati (Bilingual)",
        "difficulty": "Advanced",
        "estimated_minutes": 180,
        "version": "3.0.0-SUPREME-VISUAL",
        "author": "Antigravity Supreme Intelligence",
        "reviewed_by": "Chief Academic Architect",
        "tags": [
            "social_science",
            "heritage",
            "literature",
            "vedas",
            "upanishads",
            "epics",
            "mahabharata",
            "ramayana",
            "kalidasa",
            "sangam_literature",
            "medieval_literature",
            "nalanda",
            "takshashila",
            "vallabhi",
            "varanasi",
            "board_special",
            "bilingual"
        ],
        "learning_outcomes": [
            "Understand the origin, evolution, and significance of Indian languages and literature.",
            "Master the four Vedas, Upanishads, Brahmanas, Aranyakas, Vedangas, and Smritis.",
            "Analyze the monumental epics (Ramayana & Mahabharata) and Buddhist/Jain sacred canons.",
            "Explore Classical Sanskrit literature (Kalidasa, Bhasa, Bhavabhuti, Banabhatta) and Sangam literature.",
            "Examine Medieval literature across North, South (Kannada, Telugu), Bhakti saints, and Persian/Urdu works.",
            "Evaluate the glorious ancient universities of India (Nalanda, Takshashila, Varanasi, Vallabhi).",
            "Score 100% in GSEB/CBSE Class 10 Board exam objective, 2-mark, 3-mark, and 5-mark subjective questions."
        ],
        "ai_context": {
            "learning_goal": "Transform the student into a Board topper in Indian Literature & Ancient Universities through vivid storytelling, structured comparisons, bilingual terminology, and rigorous pedagogy.",
            "common_misconceptions": [
                "Students often confuse Rigveda (oldest hymns) with Samaveda (music) or Atharvaveda (rituals and healing).",
                "Students confuse the locations and founders of ancient universities (Nalanda in Bihar vs. Vallabhi in Gujarat vs. Takshashila in Gandhara/Rawalpindi).",
                "Students mix up Sangam literature classics (Silappadikaram vs. Manimekalai vs. Tirukkural).",
                "Students think Sanskrit was the only literary language, overlooking Pali, Prakrit, Ardhamagadhi, Tamil, Kannada, and Persian/Urdu."
            ],
            "tutor_hint": "When explaining Vedas, use the Tree of Wisdom analogy. For universities, connect Vallabhi to Gujarat's pride (Maitraka dynasty) and Nalanda to its world-famous library Dharmaganja."
        }
    }
    
    blocks = []
    
    # =========================================================================
    # MODULE 1: THE GENESIS OF LANGUAGE & ANCIENT INDIAN SCRIPTS
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "Imagine a world without written words `(लिखित शब्द / લેખિત શબ્દો)`—how would ancient sages pass down the deepest secrets of astronomy, medicine, philosophy, and spirituality across thousands of years? Through pristine sound vibrations, extraordinary human memory, and the creation of sacred scripts! India possesses one of the richest and most diverse literary treasures in human history `(साहित्यिक विरासत / સાહિત્યિક વારસો)`. Let us embark on a breathtaking journey through the ancient chants of the Vedas, the immortal epics of Ramayana and Mahabharata, the world-conquering plays of Kalidasa, the soul-stirring Sangam poetry, and the glorious international universities of Nalanda and Vallabhi!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Evolutionary Tree of Indian Languages & Literature: From Vedic Sanskrit to Classical Sanskrit, Pali, Prakrit, Dravidian languages (Tamil, Telugu, Kannada, Malayalam), Medieval regional languages, and Persian-Urdu confluence.",
        "image_url": "assets/images/gseb_ss_ch4_language_tree.jpg",
        "alt_text": "Diagram showing the evolution of ancient Indian scripts and languages"
    })
    
    blocks.append({
        "type": "theory",
        "title": "Language, Scripts, and the Mastery of Sanskrit",
        "content": "Language is the supreme medium through which human beings express their thoughts, feelings, emotions, and experiences `(विचार, भावनाएं और अनुभव / વિચારો, લાગણીઓ અને અનુભવો)`.\n\n1. **Development of Scripts `(लिपि का विकास / લિપિનો વિકાસ)`:** In ancient times, people invented gestures, sounds, and visual symbols. Over millennia, these symbols evolved into phonetic scripts `(ध्वन्यात्मक लिपियां / ધ્વન્યાત્મક લિપિઓ)`, giving birth to written literature.\n2. **Sanskrit — The Mother of Aryan Languages `(संस्कृत - आर्य भाषाओं की जननी / સંસ્કૃત - આર્ય ભાષાઓની જનની)`:** Sanskrit is universally recognized as the foundational mother tongue of the Indo-Aryan language family. It was the chosen vehicle for high philosophy, science, mathematics, spirituality, and statecraft.\n3. **Maharshi Panini — The Greatest Grammarian `(महर्षि पाणिनि / મહર્ષિ પાણિનિ)`:** Around the 4th century BCE, Maharshi Panini authored **Ashtadhyayi `(अष्टाध्यायी / અષ્ટાધ્યાયી)`**, a monumental treatise on Sanskrit grammar consisting of eight chapters and nearly 4,000 algebraic rules (*sutras*). It is universally celebrated as the most rigorous and scientific linguistic work in human civilization.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Teacher's Secret Insight: Why Computer Scientists Love Sanskrit!**\nModern computational linguists and artificial intelligence researchers consider Sanskrit to be one of the most logically structured, unambiguous, and rule-based languages on Earth. Panini's *Ashtadhyayi* laid down formal generative grammar rules 2,400 years before modern computer programming languages like Python and C++ were conceived!"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "Which monumental treatise on Sanskrit grammar was authored by Maharshi Panini in the 4th century BCE?",
            "options": [
                "Ashtadhyayi",
                "Arthashastra",
                "Charaka Samhita",
                "Rajatarangini"
            ],
            "correct_answer": "Ashtadhyayi",
            "explanation": "Maharshi Panini composed 'Ashtadhyayi' (consisting of 8 chapters), which is considered the supreme masterpiece of Sanskrit grammar and formal linguistics."
        },
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    # =========================================================================
    # MODULE 2: THE VEDIC LITERATURE (VEDAS, UPANISHADS, BRAHMANAS, ARANYAKAS)
    # =========================================================================
    blocks.append({
        "type": "theory",
        "title": "The Four Vedas — The Eternal Fount of Indian Wisdom",
        "content": "The word **Veda `(वेद / વેદ)`** originates from the Sanskrit root *'Vid'*, which means *'to know'* or *'supreme knowledge'* `(ज्ञान / જ્ઞાન)`. There are four Vedas:\n\n1. **Rigveda `(ऋग्वेद / ઋગ્વેદ)` — The Oldest Book of Humankind:**\n   - Contains **1028 Suktas (hymns) `(सूक्त / સ્તોત્રો)`** divided into **10 Mandalas (chapters) `(मंडल / મંડળો)`**.\n   - Most verses are sacred prayers dedicated to cosmic forces and deities such as Agni (Fire), Indra (Thunder/Rain), Varuna (Water), and Usha (Dawn).\n   - The hymns addressed to **Usha `(उषा की स्तुति / ઉષાની સ્તુતિ)`** (the goddess of dawn) are renowned for their sublime poetic beauty.\n\n2. **Samaveda `(सामवेद / સામવેદ)` — The Gangotri of Indian Music `(संगीत की गंगोत्री / સંગીતની ગંગોત્રી)`:**\n   - Contains verses from the Rigveda set to musical rhythm and melodic notes (*swaras*).\n   - It is the foundation of Indian classical music, explaining how sacred mantras must be recited melodiously during yajnas.\n\n3. **Yajurveda `(यजुर्वेद / યજુર્વેદ)` — The Veda of Rituals and Yajnas:**\n   - Composed in both prose `(गद्य / ગદ્ય)` and verse `(पद्य / પદ્ય)`.\n   - Provides comprehensive guidelines and chants for performing yajnas, sacrificial ceremonies `(यज्ञ और अनुष्ठान / યજ્ઞ અને વિધિઓ)`, and societal rites.\n\n4. **Atharvaveda `(अथर्ववेद / અથર્વવેદ)` — The Veda of Everyday Life and Sciences:**\n   - Contains a rich repository of rituals, social customs, sanskars, peace incantations, and medicinal remedies using herbal healing `(रोग निवारण और औषधियां / રોગ નિવારણ અને ઔષધિઓ)` to ward off physical and mental afflictions.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "The Four Vedas and their Core Essence: Rigveda (Hymns of Creation & Nature), Samaveda (Musical Chanting & Swaras), Yajurveda (Ritual Formulae & Prose), Atharvaveda (Daily Life, Health & Sanskars).",
        "image_url": "assets/images/gseb_ss_ch4_four_vedas.jpg",
        "alt_text": "Illustration of the Four Vedas written on ancient palm-leaf manuscripts"
    })
    
    blocks.append({
        "type": "theory",
        "title": "Brahmanas, Aranyakas, Upanishads & Vedangas",
        "content": "Following the four Vedas, ancient scholars created an extraordinary hierarchy of explanatory and philosophical literature:\n\n- **Brahmanical Texts `(ब्राह्मण ग्रंथ / બ્રાહ્મણ ગ્રંથો)`:** Detailed prose commentaries explaining the inner meaning and correct procedural execution of Vedic hymns and yajnas.\n- **Aranyakas `(आरण्यक / આરણ્યકો)`:** Derived from *Aranya* (Forest `(जंगल / અરણ્ય-જંગલ)`). These philosophical treatises were composed and meditated upon by sages in the calm seclusion of forest hermitages during the twilight of their lives (*Vanaprasthashrama*).\n- **Upanishads `(उपनिषद / ઉપનિષદો)`:** The pinnacle of Indian philosophy (*Vedanta* `(वेदांत / વેદાંત)`). The term means *'sitting down devotedly near a guru'* to absorb esoteric truth. They explore the deepest inquiries: The nature of the Cosmos `(ब्रह्मांड / બ્રહ્માંડ)`, the Individual Soul `(Atma / આત્મા)`, the Supreme Reality `(Brahma / પરબ્રહ્મ)`, birth, karma, and liberation (*Moksha*).\n  - Major Upanishads include *Katha, Kena, Isa, Prasna, Mundaka, Mandukya, Taittiriya, Aitareya, Chandogya,* and *Brihadaranyaka*.\n  - India's national motto, **'Satyameva Jayate' `(सत्यमेव जयते - Truth Alone Triumphs / સત્યમેવ જયતે)`**, is inscribed in the Devanagari script from the sacred **Mundaka Upanishad `(मुंडक उपनिषद / મુંડક ઉપનિષદ)`**!\n  - The *Muktika Upanishad* lists **108 Upanishads** in total.\n- **Vedangas `(वेदांग / વેદાંગો)`:** The six auxiliary limbs essential for understanding and applying the Vedas correctly:\n  1. *Shiksha `(शिक्षा / શિક્ષા)`* - Phonetics and Pronunciation\n  2. *Kalpa `(कल्प / કલ્પ)`* - Ritual Procedures and Law\n  3. *Vyakarana `(व्याकरण / વ્યાકરણ)`* - Grammar\n  4. *Nirukta `(निरुक्त / નિરુક્ત)`* - Etymology (Origins of Words)\n  5. *Chhandas `(छंद / છંદ)`* - Meter and Poetic Rhythm\n  6. *Jyotisha `(ज्योतिष / જ્યોતિષ)`* - Astronomy and Auspicious Timings.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "memory_trick",
        "content": "🧠 **Mnemonic to Remember the 6 Vedangas (S-K-V-N-C-J):**\n*'**S**mart **K**ids **V**alue **N**oble **C**haracter & **J**oy'*\n- **S**hiksha (Phonetics)\n- **K**alpa (Rituals)\n- **V**yakarana (Grammar)\n- **N**irukta (Etymology)\n- **C**hhandas (Meter)\n- **J**yotisha (Astronomy)"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "Which Veda is universally celebrated as the 'Gangotri of Indian Music'?",
            "options": [
                "Samaveda",
                "Rigveda",
                "Yajurveda",
                "Atharvaveda"
            ],
            "correct_answer": "Samaveda",
            "explanation": "Samaveda focuses on the melodic chanting and musical recitation of Vedic hymns, earning it the title 'Gangotri of Music' (સંગીતની ગંગોત્રી)."
        },
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    # =========================================================================
    # MODULE 3: THE GREAT EPICS (RAMAYANA & MAHABHARATA) & BHAGAVAD GITA
    # =========================================================================
    blocks.append({
        "type": "theory",
        "title": "The Two Monumental Epics — Ramayana and Mahabharata",
        "content": "The two immortal epics of India, **Ramayana `(रामायण / રામાયણ)`** and **Mahabharata `(महाभारत / મહાભારત)`**, have nurtured the moral, spiritual, and cultural soul of Indian society for millennia.\n\n1. **The Ramayana `(रामायण / રામાયણ)`:**\n   - Composed by **Maharshi Valmiki `(महर्षि वाल्मीकि / મહર્ષિ વાલ્મીકિ)`**, revered as the *Adi Kavi* (First Poet).\n   - Narrates the noble life and virtues of Lord Rama, the prince of Ayodhya, portraying ideals of filial duty, truth, sacrifice, fraternal bond, and ideal governance (*Ramrajya*).\n   - Though shorter than the Mahabharata, it is rich in sublime poetic emotion (*Karuna Rasa*).\n\n2. **The Mahabharata `(महाभारत / મહાભારત)`:**\n   - Composed by **Maharshi Ved Vyasa `(महर्षि वेद व्यास / મહર્ષિ વેદ વ્યાસ)`**.\n   - It is the **largest epic in world literature**, containing approximately **1,00,000 shlokas (verses) `(एक लाख श्लोक / એક લાખ શ્લોક)`**.\n   - Its original, earliest form was called **Jaya Samhita `(जय संहिता / જય સંહિતા)`**, which later expanded into *Bharata* (24,000 verses) and finally the monumental *Mahabharata*.\n   - It depicts the epic struggle between virtue (Pandavas) and righteousness vs. injustice (Kauravas), presenting deep insights into human psychology, politics, morality, and dharma.\n\n3. **The Srimad Bhagavad Gita `(श्रीमद् भगवद्गीता / શ્રીમદ્ ભગવદ્ ગીતા)`:**\n   - A holy crown jewel embedded within the *Bhishma Parva* of the Mahabharata.\n   - Comprises **18 Chapters and 700 Verses** of divine dialogue between Lord Krishna and Arjuna on the battlefield of Kurukshetra.\n   - Harmonizes three profound paths of spiritual liberation: **Jnana Yoga `(ज्ञान योग / જ્ઞાન યોગ - Path of Wisdom)`**, **Bhakti Yoga `(भक्ति योग / ભક્તિ યોગ - Path of Devotion)`**, and **Karma Yoga `(कर्म योग / કર્મ યોગ - Path of Selfless Action)`**.\n   - Core message: *Perform your duty fearlessly and selflessly without being attached to the fruit of actions (Nishkama Karma).*",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "The Architecture of Mahabharata: From Jaya Samhita (8,800 verses) to Bharata (24,000 verses) to Mahabharata (1,00,000 verses), housing the divine 700-verse Bhagavad Gita.",
        "image_url": "assets/images/gseb_ss_ch4_epics_gita.jpg",
        "alt_text": "Lord Krishna delivering the Bhagavad Gita to Arjuna at Kurukshetra"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "What was the original, earliest name of the epic Mahabharata before it expanded to 1,00,000 verses?",
            "options": [
                "Jaya Samhita",
                "Raghuvamsham",
                "Harshacharita",
                "Panchatantra"
            ],
            "correct_answer": "Jaya Samhita",
            "explanation": "Mahabharata originally comprised around 8,800 verses and was named 'Jaya Samhita'. With successive additions, it grew to 24,000 verses (Bharata) and finally 1,00,000 verses (Mahabharata)."
        },
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })
    
    # =========================================================================
    # MODULE 4: BUDDHIST & JAIN CANONICAL LITERATURE
    # =========================================================================
    blocks.append({
        "type": "theory",
        "title": "Buddhist Canonical Literature — The Tripitaka",
        "content": "Early Buddhist literature was composed in the **Pali `(पाली भाषा / પાલી ભાષા)`** language, which was the spoken tongue of the common masses during Lord Buddha's era.\n\nThe most sacred Buddhist canon is organized into three collections collectively known as **Tripitaka `(त्रिपिटक / ત્રિપિટક - Three Baskets)`**:\n\n1. **Vinaya Pitaka `(विनय पिटक / વિનય પિટક)`:** Contains the strict code of conduct, monastic rules, discipline, and daily lifestyle regulations prescribed for Buddhist monks (*Bhikkhus*) and nuns (*Bhikkhunis*) residing in the Sangha `(बौद्ध संघ के नियम / બૌદ્ધ સંઘના નિયમો)`.\n2. **Sutta (Sutra) Pitaka `(सुत्त पिटक / સુત્ત પિટક)`:** Contains the core religious discourses, moral teachings, parables, and philosophical dialogues delivered by Lord Buddha.\n3. **Abhidhamma Pitaka `(अभिधम्म पिटक / અભિધમ્મ પિટક)`:** Explores deep metaphysics, psychological insights, analysis of mind, matter, and the nature of consciousness `(दार्शनिक और मनोवैज्ञानिक सिद्धांत / દાર્શનિક અને મનોવૈજ્ઞાનિક સિદ્ધાંતો)`.\n\n- **Jataka Tales `(जातक कथाएं / જાતક કથાઓ)`:** 547 captivating folk stories narrating the previous incarnations of the Bodhisattva before attaining Buddhahood, emphasizing universal virtues like compassion, generosity, and truth.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "title": "Jain Literature — The Sacred Agamas",
        "content": "Jain canonical literature was predominantly composed in **Ardhamagadhi `(अर्धमागधी / અર્ધમાગધી)`** and Prakrit dialects.\n\n- **The Agamas `(आगम ग्रंथ / આગમ ગ્રંથો)`:** The fundamental sacred scripture of Jainism consisting of **12 Angas `(12 अंग / ૧૨ અંગ)`** and **12 Upangas `(12 उपांग / ૧૨ ઉપાંગ)`**.\n- They meticulously document the sermons, code of ethics, metaphysical doctrines, and vows prescribed by Lord Mahavira (the 24th Tirthankara) and senior Ganadharas.\n- Core Jain principles expounded: **Ahimsa `(अहिंसा / અહિંસા - Non-violence)`**, **Satya `(सत्य - Truth)`**, **Asteya `(अस्तेय - Non-stealing)`**, **Brahmacharya `(ब्रह्मचर्य)`**, and **Aparigraha `(अपरिग्रह - Non-possession)`**, alongside the profound philosophy of **Anekantavada `(अनेकांतवाद - Relativity of Truth)`**.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "Which section of the Buddhist Tripitaka contains the rules, monastic discipline, and code of conduct for monks and nuns in the Sangha?",
            "options": [
                "Vinaya Pitaka",
                "Sutta Pitaka",
                "Abhidhamma Pitaka",
                "Jataka Tales"
            ],
            "correct_answer": "Vinaya Pitaka",
            "explanation": "Vinaya Pitaka is dedicated specifically to the monastic rules and code of discipline for monks and nuns living in the Buddhist Sangha."
        },
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })
    
    # =========================================================================
    # MODULE 5: GOLDEN AGE OF CLASSICAL SANSKRIT LITERATURE & DRAMA
    # =========================================================================
    blocks.append({
        "type": "theory",
        "title": "Classical Sanskrit Literature — The Gupta Golden Age",
        "content": "The **Gupta Period (4th–6th Century CE)** is universally celebrated as the **Golden Age of Sanskrit Literature `(संस्कृत साहित्य का स्वर्ण युग / સંસ્કૃત સાહિત્યનો સુવર્ણ યુગ)`**. During this era, master playwrights, lyricists, and storytellers elevated Sanskrit poetry, prose, and drama to artistic perfection.\n\n1. **Mahakavi Kalidasa `(महाकवि कालिदास / મહાકવિ કાલિદાસ)` — The Shakespeare of India:**\n   - Renowned for unmatched poetic similes (*'Upama Kalidasasya' `(उपमा कालिदासस्य / ઉપમા કાલિદાસસ્ય)`*), aesthetic grandeur, and romantic drama.\n   - **World-Famous Plays:**\n     - *Abhijnanasakuntalam `(अभिज्ञानशाकुंतलम्)`* — The tragic romance of King Dushyanta and Shakuntala, acclaimed globally and translated into numerous European languages.\n     - *Malavikagnimitram `(मालविकाग्निमित्रम्)`* & *Vikramorvasiyam `(विक्रमोर्वशीयम्)`*.\n   - **Mahakavyas (Grand Epics):**\n     - *Raghuvamsham `(रघुवंशम्)`* — Chronicle of the Solar dynasty kings, including Lord Rama.\n     - *Kumarasambhavam `(कुमारसम्भवम्)`* — The divine courtship of Shiva and Parvati and the birth of warrior god Kartikeya.\n   - **Khandakavyas (Lyric Poems):**\n     - *Meghadootam `(मेघदूतम्)`* — An exiled Yaksha sends messages of love to his wife across mountains via a rain-bearing cloud.\n     - *Ritusamharam `(ऋतुसंहारम्)`* — Vivid descriptions of India's six seasons.",
        "difficulty": "Advanced",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "title": "Master Playwrights & Storytellers of Ancient India",
        "content": "India's classical Sanskrit heritage was illuminated by numerous other legendary authors:\n\n- **Bhasa `(भास / ભાસ)`:** Predecessor to Kalidasa; authored 13 master plays based on the epics, including *Svapnavasavadattam `(स्वप्नवासवदत्तम्)`*, *Karnabharam `(कर्णभारम्)`*, and *Urubhanga `(ऊरुभङ्गम्)`*.\n- **Bhavabhuti `(भवभूति / ભવભૂતિ)`:** Master of pathos (*Karuna Rasa*); authored *Uttararamacharita `(उत्तररामचरितम्)`*, *Malatimadhava `(मालतीमाधवम्)`*, and *Mahaviracharita*.\n- **Shudraka `(शूद्रक / શૂદ્રક)`:** Authored the realistic social drama **Mrichhakatikam `(मृच्छकटिकम् - The Little Clay Cart / માટીની ગાડી)`**, depicting the love between impoverished merchant Charudatta and noble courtesan Vasantasena.\n- **Vishakhadatta `(विशाखदत्त / વિશાખાદત્ત)`:** Authored the gripping political drama **Mudrarakshasa `(मुद्राराक्षस / મુદ્રારાક્ષસ)`**, detailing how Acharya Chanakya strategically overthrew the Nanda dynasty and secured Chandragupta Maurya's empire.\n- **Dandin `(दंडी / દંડી)`:** Authored *Dashakumaracharita `(दशकुमारचरितम् - Tales of Ten Princes)`* and *Kavyadarsha*.\n- **Banabhatta `(बाणभट्ट / બાણભટ્ટ)`:** Celebrated court poet of Emperor Harshavardhana; authored **Harshacharita `(हर्षचरितम्)`** (first historical biography in Sanskrit) and **Kadambari `(कादम्बरी)`** (one of the world's earliest prose romantic novels).\n- **Emperor Harshavardhana `(सम्राट हर्षवर्धन / સમ્રાટ હર્ષવર્ધન)`:** A royal scholar who penned three acclaimed plays: *Priyadarshika `(प्रियदर्शिका)`*, *Ratnavali `(रत्नावली)`*, and *Nagananda `(नागानन्द)`*.\n- **Vishnu Sharma `(विष्णु शर्मा / વિષ્ણુ શર્મા)`:** Authored the immortal **Panchatantra `(पंचतंत्र / પંચતંત્ર)`**, a five-part treasure of animal fables designed to impart practical worldly wisdom (*Niti*) to young princes.\n- **Narayana Pandit `(नारायण पंडित / નારાયણ પંડિત)`:** Authored *Hitopadesha `(हितोपदेश / હિતોપદેશ)`*, another renowned collection of moral fables.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Master Table of Classical Sanskrit Authors & Their Immortal Works: Kalidasa (Abhijnanasakuntalam, Meghadootam), Banabhatta (Harshacharita, Kadambari), Shudraka (Mrichhakatikam), Vishakhadatta (Mudrarakshasa), Vishnu Sharma (Panchatantra).",
        "image_url": "assets/images/gseb_ss_ch4_sanskrit_authors.jpg",
        "alt_text": "Comparative chart of ancient Sanskrit playwrights and authors with their masterpieces"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "Match the following authors with their monumental literary creations:\n1. Vishakhadatta — (A) Kadambari\n2. Shudraka — (B) Mudrarakshasa\n3. Banabhatta — (C) Mrichhakatikam\n4. Vishnu Sharma — (D) Panchatantra",
            "options": [
                "1-B, 2-C, 3-A, 4-D",
                "1-A, 2-B, 3-C, 4-D",
                "1-C, 2-B, 3-D, 4-A",
                "1-D, 2-C, 3-B, 4-A"
            ],
            "correct_answer": "1-B, 2-C, 3-A, 4-D",
            "explanation": "Vishakhadatta wrote 'Mudrarakshasa', Shudraka wrote 'Mrichhakatikam', Banabhatta wrote 'Kadambari', and Vishnu Sharma authored 'Panchatantra'."
        },
        "difficulty": "Intermediate",
        "bloom": "Analyze"
    })
    
    # =========================================================================
    # MODULE 6: SANGAM LITERATURE & ANCIENT DRAVIDIAN LANGUAGES
    # =========================================================================
    blocks.append({
        "type": "theory",
        "title": "Sangam Literature — The Soul of Dravidian Heritage",
        "content": "South India developed an extraordinary literary tradition rooted in the **four Dravidian languages `(द्रविड़ कुल की भाषाएं / દ્રવિડ કુળની ભાષાઓ)`**:\n1. **Tamil `(तमिल / તમિલ)`** — The oldest Dravidian language with an independent literary lineage dating back over two millennia.\n2. **Telugu `(तेलुगु / તેલુગુ)`**\n3. **Kannada `(कन्नड़ / કન્નડ)`**\n4. **Malayalam `(मलयालम / મલયાલમ)`**\n\n**The Sangam Assemblies `(संगम साहित्य / સંગમ સાહિત્ય)`:**\n- According to tradition, three great literary academies (*Sangams*) of poets, scholars, and bards were convened in **Madurai** under the royal patronage of the **Pandya kings `(पांड्य राजा / પાંડ્ય રાજાઓ)`**.\n- The literature produced in these assemblies reflected real-world themes: love (*Agam*), war and valor (*Puram*), trade, governance, ethics, and nature.\n\n**Three Monumental Sangam Collections:**\n1. **Tolkappiyam `(तोलकाप्पियम / તોલકાપ્પિયમ)`:** Authored by **Tolkappiyar `(तोलकाप्पियर / તોલકાપ્પિયર)`**. It is the earliest surviving Tamil work, treating phonetics, grammar, and poetics in extraordinary depth.\n2. **Ettuttokai `(एत्तुत्तोकै / એત્તુતોકાઈ)`:** An anthology of Eight Works, including *Purananuru* and *Akananuru*.\n3. **Pattuppattu `(पत्तूप्पात्तू / પત્તુપ્પાત્તુ)`:** The Ten Idylls (longer narrative and descriptive poems).\n\n**Tirukkural `(तिरुक्कुरल / તિરુક્કુરલ)` — The Tamil Veda:**\n- Authored by the revered philosopher-poet **Thiruvalluvar `(तिरुवल्लुवर / તિરુવલ્લુવર)`**.\n- Comprises 1,330 couplets categorized into three sections: *Aram* (Virtue/Dharma `(धर्म / ધર્મ)`), *Porul* (Wealth/Artha `(अर्थ / અર્થ)`), and *Inbam* (Love/Kama `(काम / કામ)`). It is universally hailed as an ethical guide for all humanity.\n\n**The Two Great Tamil Epics `(तमिल महाकाव्य / તમિલ મહાકાવ્યો)`:**\n- **Silappadikaram `(शिलप्पादिकारम / શિલાપ્પદિકારમ - The Jewelled Anklet)`:** Composed by prince-poet **Ilango Adigal `(इलांगो आदिगल / ઇલાંગો આદિગલ)`**. It tells the moving tragedy of Kovalan, his devoted wife Kannagi, and courtesan Madhavi, celebrating Kannagi's ultimate moral retribution in Madurai.\n- **Manimekalai `(मणिमेखलै / મણિમેખલાઈ)`:** Composed by **Chithalai Chathanar `(सीतलै सात्तनार / સીતલઈ સાથનાર)`**. A continuation that follows Manimekalai (daughter of Kovalan and Madhavi) as she renounces worldly pursuits to embrace Buddhist philosophy.",
        "difficulty": "Advanced",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Board Exam Distinction Alert!**\nFrequently asked in GSEB Class 10 Board exams:\n- Who wrote **Tirukkural**? 👉 **Thiruvalluvar**\n- Who wrote **Silappadikaram**? 👉 **Ilango Adigal**\n- Who wrote **Manimekalai**? 👉 **Chithalai Chathanar**\n- Name the oldest Dravidian language 👉 **Tamil**"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "Which immortal Tamil ethical treatise consisting of 1,330 couplets on virtue, wealth, and love was composed by Saint Thiruvalluvar?",
            "options": [
                "Tirukkural",
                "Silappadikaram",
                "Manimekalai",
                "Tolkappiyam"
            ],
            "correct_answer": "Tirukkural",
            "explanation": "'Tirukkural' was composed by Saint Thiruvalluvar and is celebrated as the Tamil Veda, providing universal ethical guidelines on Dharma, Artha, and Kama."
        },
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    # =========================================================================
    # MODULE 7: MEDIEVAL INDIAN LITERATURE (NORTH, SOUTH, BHAKTI & GUJARATI)
    # =========================================================================
    blocks.append({
        "type": "theory",
        "title": "Medieval Sanskrit & North Indian Literature",
        "content": "During the medieval period, literature flourished across royal courts and pilgrimage hubs:\n\n1. **Kashmir's Historical Literature:**\n   - **Somadeva `(सोमदेव / સોમદેવ)`** authored **Kathasaritsagara `(कथासरित्सागर / કથાસરિત્સાગર - Ocean of Story Streams)`**, a massive treasury of folk tales.\n   - **Kalhana `(कल्हण / કલ્હણ)`** composed **Rajatarangini `(राजतरंगिणी / રાજતરંગિણી - River of Kings)`** in the 12th century. It chronicles the royal dynasties of Kashmir and is celebrated as **India's first authentic, scientific historical treatise `(भारत का प्रथम प्रामाणिक ऐतिहासिक ग्रंथ / ભારતનો પ્રથમ પ્રમાણિત ઐતિહાસિક ગ્રંથ)`**.\n\n2. **Devotional Lyricism:**\n   - **Jayadeva `(जयदेव / જયદેવ)`** authored the sublime devotional lyric masterpiece **Gita Govinda `(गीत गोविंद / ગીત ગોવિંદ)`**, singing the divine romance of Radha and Krishna in melodious Sanskrit.\n\n3. **Heroic Hindi Epics:**\n   - **Chand Bardai `(चंदबरदाई / ચંદબરદાઈ)`** composed **Prithviraj Raso `(पृथ्वीराज रासो / પૃથ્વીરાજ રાસો)`**, the first major heroic epic in early Hindi (*Braj/Dingal*), immortalizing the bravery of Rajput King Prithviraj Chauhan.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "title": "Medieval South Indian & Bhakti Movement Literature",
        "content": "1. **Kannada Literature — The Trio of Gems (*Ratnatraya* `(त्रिरत्न / ત્રિરત્ન)`):**\n   - **Pampa `(पंपा / પંપા)`:** Authored *Adipurana* (life of first Jain Tirthankara Rishabhadeva) and *Vikramarjuna Vijaya* (Pampa Bharata).\n   - **Ponna `(पोन्ना / પોન્ના)`:** Authored *Shanthipurana* (life of 16th Tirthankara Shantinatha).\n   - **Ranna `(रन्ना / રન્ના)`:** Authored *Ajitnath Purana* and the dramatic *Gadayuddha*.\n\n2. **Telugu Golden Age — Vijayanagara Empire:**\n   - The illustrious Vijayanagara Emperor **Krishnadevaraya `(कृष्णदेवराय / કૃષ્ણદેવરાય)`** was a supreme patron of arts and an accomplished scholar himself.\n   - Authored the renowned Telugu epic **Amuktamalyada `(आमुक्तमाल्यदा / આમુકતમાલ્યદા)`** (story of Andal and Lord Ranganatha).\n   - His royal court was adorned by eight eminent poets known as the **Ashtadiggajas `(अष्टदिग्गज / અષ્ટદિગ્ગજ)`** (including Allasani Peddana and Tenali Rama).\n   - In Tamil, poet **Kamban `(कंबन / કમ્બન)`** composed the famous *Kamba Ramayanam*.\n\n3. **The Bhakti Movement & Regional Masters `(भक्ति आंदोलन / ભક્તિ આંદોલન)`:**\n   - **Kabir `(कबीर / કબીર)`:** Composed soul-stirring Dohas `(दोहे / દોહા)` and *Bijak* in *Sadhukkadi* dialect, attacking religious dogmas and emphasizing universal love.\n   - **Goswami Tulsidas `(तुलसीदास / તુલસીદાસ)`:** Authored the timeless **Ramcharitmanas `(रामचरितमानस / રામચરિતમાનસ)`** in Awadhi, making the Ramayana accessible to every Indian household, along with *Vinaya Patrika*.\n   - **Surdas `(सूरदास / સૂરદાસ)`:** Authored *Sursagar `(सूरसागर / સૂરસાગર)`* celebrating Krishna's childhood leelas in Brajbhasha.\n   - **Mirabai `(मीराबाई / મીરાંબાઈ)`:** Expressed intense devotion to *Girdhar Gopal* through emotional padas in Rajasthani and Gujarati.\n   - **Narsinh Mehta `(नरसिंह मेहता / નરસિંહ મહેતા)`:** The *Adi Kavi* of Gujarat who composed immortal *Prabhatiya `(प्रभातियां / પ્રભાતિયાં)`* and the world-famous hymn **'Vaishnav Jan To Tene Kahiye' `(वैष्णव जन तो तेने कहिये / વૈષ્ણવ જન તો તેને કહિયે)`**.\n   - **Gujarati Literary Masters:**\n     - *Hemchandracharya `(हेमचंद्राचार्य / હેમચંદ્રાચાર્ય)`* authored the first Gujarati-Prakrit grammar text *Siddhahema Shabdanushasana `(सिद्धहेમ शब्दानुशासन / સિદ્ધહેમ શબ્દાનુશાસન)`*.\n     - *Akho `(अखो / અખો)`* authored witty social satires (*Chhappa `(छप्पा / છપ્પા)`*).\n     - *Premanand `(प्रेमानंद / પ્રેમાનંદ)`* popularized the *Akhyana `(आख्यान / આખ્યાન)`* style.\n     - *Dayaram `(दयाराम / દયારામ)`* composed romantic-devotional *Garbi `(गरबी / ગરબી)`* songs.\n     - *Kavi Narmad `(कवि नर्मद / કવિ નર્મદ)`* became the pioneer of modern Gujarati prose.\n   - **Maharashtra:** *Saint Dnyaneshwar* authored *Dnyaneshwari* (Bhavartha Dipika) and *Saint Tukaram* composed devotional *Abhangas `(अभंग / અભંગ)`*.\n   - **Sikh Sacred Canon:** *Guru Arjan Dev* compiled the holy **Guru Granth Sahib `(गुरु ग्रंथ साहिब / ગુરુ ગ્રંથ સાહેબ)`** in Gurmukhi.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "Which historic work composed by Kalhana in the 12th century is recognized as India's first authentic, scientific historical treatise?",
            "options": [
                "Rajatarangini",
                "Kathasaritsagara",
                "Prithviraj Raso",
                "Gita Govinda"
            ],
            "correct_answer": "Rajatarangini",
            "explanation": "Kalhana's 'Rajatarangini' (River of Kings), chronicling the kings of Kashmir, is celebrated as India's first genuine historical research work."
        },
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })
    
    # =========================================================================
    # MODULE 8: PERSIAN, SULTANATE, MUGHAL & URDU LITERATURE
    # =========================================================================
    blocks.append({
        "type": "theory",
        "title": "Persian & Sultanate Literature — Amir Khusro",
        "content": "During the Delhi Sultanate and Mughal periods, **Persian `(फ़ारसी / ફારસી)`** served as the courtly and administrative language `(दरबारी भाषा / દરબારી ભાષા)`.\n\n**Amir Khusro `(अमीर खुसरो / અમીર ખુસરો)` — The Parrot of India (*Tuti-e-Hind* `(तूती-ए-हिंद / તૂતી-એ-હિન્દ)`):**\n- A disciple of Sufi Saint Hazrat Nizamuddin Auliya, Amir Khusro was a versatile genius: poet, historian, mystic, and father of Qawwali and Khayal music.\n- Masterpieces include *Kirana-us-Sadain `(किरान-उस-सादैन)`*, *Nuh Sipihr `(नुह सिपिहर)`*, *Miftah-ul-Futuh*, *Ashiqa*, and *Tughlaqnama*.\n- In his work *Nuh Sipihr*, he praised India extravagantly, stating that India's climate, fauna, beauty, and wisdom made it an earthly paradise `(धरती का स्वर्ग / પૃથ્વી પરનું સ્વર્ગ)`.\n- He pioneered poetry in **Hindavi `(हिन्दवी / હિન્દવી)`** (the language of common people) and composed famous riddles `(पहेलियां / ઉખાણાં)` and dual-language verses blending Persian and Hindi.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "title": "Mughal Literature & The Rise of Urdu",
        "content": "The Mughal era produced magnificent autobiographies, historical chronicles, and translations:\n\n1. **Babur `(बाबर / બાબર)`:** Wrote his candid autobiography **Baburnama `(बाबरनामा / બાબરનામા)`** (*Tuzuk-i-Baburi*) in Chagatai Turkish (later translated into Persian by Abdur Rahim Khan-i-Khana).\n2. **Gulbadan Begum `(गुलबदन बेगम / ગુલબદન બેગમ)`:** Sister of Humayun, authored **Humayun-nama `(हुमायूंनामा / હુમાયૂંનામા)`**.\n3. **Abul Fazl `(अबुल फजल / અબુલ ફઝલ)`:** Court historian of Emperor Akbar; authored **Akbarnama `(अकबरनामा / અકબરનામા)`** and its administrative masterpiece **Ain-i-Akbari `(आईन-ए-अकबरी / આઇને અકબરી)`** (providing unmatched statistical details on Mughal governance, army, revenue, crops, and culture). Abul Fazl also translated the *Bhagavad Gita* and *Panchatantra* (*Anwar-i-Suhaili*) into Persian.\n4. **Jahangir `(जहांगीर / જહાંગીર)`:** Wrote his memoirs in **Tuzuk-i-Jahangiri `(तुजुक-ए-जहांगीरी)`**.\n5. **Dara Shikoh `(दारा शिकोह / દારા શિકોહ)`:** Eldest son of Shah Jahan and an enlightened philosopher-prince. A master of Sanskrit and Persian, he translated **50 Upanishads** into Persian under the title **Sirr-i-Akbar `(सिर्र-ए-अकबर - The Great Secret)`** and authored **Majma-ul-Bahrain `(मजमा-उल-बहरीन - Mingling of the Two Oceans)`**, proving the fundamental spiritual unity between Hinduism and Islam.\n\n**The Rise of Urdu `(उर्दू भाषा का जन्म / ઉર્દૂ ભાષાનો ઉદય)`:**\n- Born from the cultural confluence of Persian and Hindavi/Hindi dialects in military encampments and urban bazaars.\n- Developed into a rich literary language with legendary poets: **Vali Gujarati `(वली गुजराती / વલી ગુજરાતી)`** (Father of Urdu Ghazal), **Mir Taqi Mir**, **Khwaja Mir Dard**, **Mirza Ghalib `(मिर्ज़ा ग़ालिब / મિર્ઝા ગાલિબ)`**, **Bahadur Shah Zafar**, and **Sir Muhammad Iqbal `(अल्लामा इक़बाल / અલ્લામા ઇકબાલ)`** (author of *'Sare Jahan Se Achha Hindustan Hamara'*).",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "Which enlightened Mughal prince translated 50 Upanishads into Persian under the title 'Sirr-i-Akbar' (The Great Secret)?",
            "options": [
                "Dara Shikoh",
                "Abul Fazl",
                "Amir Khusro",
                "Abdur Rahim Khan-i-Khana"
            ],
            "correct_answer": "Dara Shikoh",
            "explanation": "Dara Shikoh, the eldest son of Shah Jahan, was a great scholar who translated 50 Upanishads into Persian under the title 'Sirr-i-Akbar' (The Great Secret)."
        },
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })
    
    # =========================================================================
    # MODULE 9: THE ANCIENT UNIVERSITIES OF INDIA (NALANDA, TAKSHASHILA, VARANASI, VALLABHI)
    # =========================================================================
    blocks.append({
        "type": "theory",
        "title": "Ancient Indian Universities — Global Hubs of Knowledge",
        "content": "Long before Oxford, Cambridge, or Harvard existed, India pioneered world-class residential universities (*Vidyapeethas* `(विद्यापीठ / વિદ્યાપીઠો)`) that attracted thousands of scholars from all corners of Asia.\n\n### 1. Nalanda University `(नालंदा विद्यापीठ / નાલંદા વિદ્યાપીઠ - Badgaon, Patna/Rajgir, Bihar)`:\n- **Foundation:** Established during the 5th century CE under the patronage of Gupta Emperor **Kumaragupta I `(कुमारगुप्त प्रथम / કુમારગુપ્ત પ્રથમ)`**.\n- **International Stature:** Housed over **10,000 students and 2,000 teachers** from China, Japan, Korea, Tibet, Central Asia, and Southeast Asia.\n- **Free Education:** King Kumaragupta and subsequent rulers donated the revenues of 100+ surrounding villages to ensure free education, boarding, lodging, and books for all students.\n- **The Grand Library — Dharmaganja `(धर्मगंज / ધર્મગંજ - Mountain of Truth)`:** Comprised three multi-storey architectural wonders named **Ratnasagara `(रत्नसागर)`**, **Ratnodadhi `(रत्नोदधि)`**, and **Ratnaranjaka `(रत्नरंजक)`**, housing hundreds of thousands of handwritten manuscripts.\n- **Hiuen Tsang's Visit:** The Chinese Buddhist monk **Hiuen Tsang (Xuanzang) `(ह्वेन त्साંગ / હ્યુઅન ત્સાંગ)`** studied Mahayana Buddhism at Nalanda for 5 years and transported **657 Sanskrit manuscripts** back to China on 20 horses.\n- **Curriculum:** Mahayana & Hinayana Buddhism, Vedic Philosophy, Logic (*Nyaya*), Grammar, Medicine (*Ayurveda*), Astronomy, Metallurgy.\n- **Tragic Destruction:** Destroyed in the late 12th century by Bakhtiyar Khilji's invasion.\n\n---\n\n### 2. Takshashila University `(तक्षशिला विद्यापीठ / તક્ષશિલા વિદ્યાપીઠ - Rawalpindi, Pakistan)`:\n- **Location & Heritage:** Located in ancient Gandhara near the northwestern gateway of India, at the crossroads of the Silk Route.\n- **Curriculum:** Offered instruction in **68 different disciplines**, including the Vedas, Military Arts & Archery (*Dhanurveda* `(धनुर्विद्या / ધનુર્વિદ્યા)`), Politics, Law, Surgery, Astronomy, Commerce, and Elephant Lore.\n- **Legendary Alumni & Faculty:**\n  - **Acharya Chanakya (Kautilya) `(आचार्य चाणक्य / આચાર્ય ચાણક્ય)`:** Taught statecraft and authored the world-famous **Arthashastra `(अर्थशास्त्र / અર્થશાસ્ત્ર)`** while mentoring young Chandragupta Maurya.\n  - **Maharshi Panini `(महर्षि पाणिनિ / મહર્ષિ પાણિનિ)`:** Mastered and codified Sanskrit grammar (*Ashtadhyayi*).\n  - **Jivaka `(जीवक / જીવક)`:** Renowned royal physician of Magadha King Bimbisara and personal doctor to Lord Buddha; mastered medicine and surgery here.\n  - **King Prasenjit** of Kosala.\n  - **Charaka `(चरक / ચરક)`:** Pioneer of Indian medicine and author of *Charaka Samhita*.\n\n---\n\n### 3. Varanasi (Kashi) `(वाराणसी - काशी / વારાણસી - કાશી - Uttar Pradesh)`:\n- **Spiritual & Vedic Capital:** The eternal pilgrimage center and focal point of Vedic learning since the Upanishadic period.\n- **Philosophical Debates:** Kings like Ajatashatru promoted deep philosophical discourses here. Great philosophers like **Adi Shankaracharya**, **Vallabhacharya**, and **Chaitanya Mahaprabhu** traveled to Kashi to gain scholarly validation for their philosophical doctrines.\n- **Literary Cradle:** Birthplace and spiritual abode of saint-poet Kabir and Goswami Tulsidas.\n\n---\n\n### 4. Vallabhi University `(वल्लभी विद्यापीठ / વલ્લભી વિદ્યાપીઠ - Bhavnagar, Gujarat)`:\n- **Pride of Gujarat:** Flourished between the 5th and 8th centuries CE in **Vallabhi (near modern Vallabhipur, Bhavnagar district, Gujarat) `(भावनगर, गुजरात / ભાવનગર, ગુજરાત)`** as the vibrant capital of the **Maitraka Dynasty `(मैत्रक वंश / મૈત્રક વંશ)`**.\n- **Buddhist & Vedic Convergence:** While celebrated globally as the supreme international seat of **Hinayana Buddhism `(हीनयान बौद्ध धर्म / હીનયાન બૌદ્ધ ધર્મ)`**, it equally provided advanced education in Vedic philosophy, administrative sciences, law, and commerce.\n- **Illustrious Acharyas:** Famous Buddhist scholars **Sthiramati `(स्थिरमति / સ્થિરમતિ)`** and **Gunamati `(गुणमति / ગુણમતિ)`** presided as the leading acharyas.\n- **Chinese Travelers' Testimony:** Chinese pilgrims **Hiuen Tsang** and **I-Tsing (Itsing) `(इत्सिंग / ઇત્સિંગ)`** visited Vallabhi and recorded that its academic rigor, library, and glory were completely equal to Nalanda University!\n- **Entrance Gate of Fame:** Admission was intensely competitive with tough entrance debates (*Dvara-Panditas*). The names of scholars who achieved top distinction were **inscribed in gold at the main university portal `(मुख्य द्वार पर स्वर्णाक्षरों में नाम / મુખ્ય પ્રવેશદ્વાર પર સુવર્ણાક્ષરે નામ અંકિત થતાં)`**, and graduates were immediately appointed to high administrative offices by kings.\n- **Patronage:** Loyally nurtured by the Buddhist-friendly Maitraka kings (such as Dhruvasena and Dharasena) and funded by the generous charity of wealthy Gujarati merchants (*Sheths* / *Shreshthis* `(गुजराती श्रेष्ठी / ગુજરાતી શ્રેષ્ઠીઓ)`).",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Master Matrix of Ancient Indian Universities: Nalanda (Bihar - Kumaragupta I, 10k students, Dharmaganja library, Hiuen Tsang), Takshashila (Gandhara - Chanakya, Panini, Jivaka, 68 subjects), Varanasi (UP - Vedic hub, Shankaracharya, Tulsidas), Vallabhi (Gujarat - Maitraka dynasty, Hinayana hub, Sthiramati & Gunamati, I-Tsing).",
        "image_url": "assets/images/gseb_ss_ch4_universities_matrix.jpg",
        "alt_text": "Comparative matrix of Nalanda, Takshashila, Varanasi, and Vallabhi universities"
    })
    
    blocks.append({
        "type": "common_mistakes",
        "content": "⚠️ **COMMON BOARD EXAM CONFUSIONS TO AVOID:**\n1. **Nalanda vs. Vallabhi:** Nalanda was primarily a center of **Mahayana Buddhism** in Bihar funded by the Guptas; Vallabhi was the supreme seat of **Hinayana Buddhism** in Gujarat funded by the Maitrakas.\n2. **Nalanda's Library Name:** The library was **Dharmaganja** (comprising 3 towers: *Ratnasagara, Ratnodadhi, Ratnaranjaka*). Do not confuse the towers with the whole library name.\n3. **Takshashila Alumni:** Chanakya, Panini, and Jivaka studied at **Takshashila**, NOT Nalanda (Nalanda was founded centuries later during the Gupta era)."
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "Which famous university of Gujarat was the capital of the Maitraka Dynasty and a world-renowned center of Hinayana Buddhism visited by Chinese pilgrims Hiuen Tsang and I-Tsing?",
            "options": [
                "Vallabhi University",
                "Nalanda University",
                "Takshashila University",
                "Vikramashila University"
            ],
            "correct_answer": "Vallabhi University",
            "explanation": "Vallabhi University, located in Bhavnagar district of Gujarat, was the capital of the Maitraka dynasty and a world-renowned seat of Hinayana Buddhism visited by Hiuen Tsang and I-Tsing."
        },
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    # =========================================================================
    # MODULE 10: BOARD EXAM MASTERY (PYQS & HIGH-YIELD TOPICS)
    # =========================================================================
    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM TOP SCORING FORMULA (Chapter 4):**\n\n1. **4-Mark / 5-Mark Must-Prepare Long Answers:**\n   - **Write a detailed note on Nalanda University / Vallabhi University:** Structure your answer with Headings: *Location, Founder/Dynasty, Capacity & International Students, Library (Dharmaganja), Chinese Travelers' Account, Subjects Taught*.\n   - **Discuss the Four Vedas and Upanishads:** Define *Veda*, describe Rigveda, Samaveda, Yajurveda, Atharvaveda, and explain the philosophical inquiry of Upanishads with *'Satyameva Jayate'*.\n   - **Describe Ancient Indian Epics:** Compare *Ramayana* (Valmiki, 24k verses) and *Mahabharata* (Ved Vyasa, 1 lakh verses, *Jaya Samhita*, *Bhagavad Gita*).\n   - **Explain Classical Sanskrit Drama & Literature:** Highlight *Kalidasa* (Abhijnanasakuntalam, Meghadootam), *Banabhatta* (Kadambari, Harshacharita), *Vishakhadatta* (Mudrarakshasa), and *Shudraka* (Mrichhakatikam).\n   - **Write a note on Sangam Literature & Dravidian Languages:** Tamil (oldest), Tolkappiyam, Ettuttokai, Pattuppattu, Tirukkural (Thiruvalluvar), Silappadikaram, Manimekalai.\n\n2. **1-Mark / 2-Mark Frequent Board Questions:**\n   - Who wrote *Ashtadhyayi*? 👉 **Maharshi Panini**\n   - What are the three parts of *Tripitaka*? 👉 **Vinaya, Sutta, Abhidhamma**\n   - Which is the first scientific historical book of India? 👉 **Rajatarangini by Kalhana**\n   - Who wrote *Amuktamalyada*? 👉 **Emperor Krishnadevaraya**\n   - Who wrote *Ain-i-Akbari*? 👉 **Abul Fazl**\n   - Who translated 50 Upanishads as *Sirr-i-Akbar*? 👉 **Dara Shikoh**",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })
    
    blocks.append({
        "type": "summary",
        "content": "📌 **Chapter Quick Summary:**\n- **Vedic Heritage:** 4 Vedas (Rigveda, Samaveda, Yajurveda, Atharvaveda), Brahmanas, Aranyakas, 108 Upanishads (Mundaka: *Satyameva Jayate*), 6 Vedangas.\n- **Epics:** Valmiki's Ramayana & Ved Vyasa's Mahabharata (1,00,000 shlokas, *Jaya Samhita*, 700-shloka Bhagavad Gita).\n- **Heterodox Canons:** Buddhist *Tripitaka* (Pali) and Jain *Agamas* (Ardhamagadhi).\n- **Classical Sanskrit:** Kalidasa (*Abhijnanasakuntalam*), Banabhatta (*Harshacharita, Kadambari*), Shudraka (*Mrichhakatikam*), Vishakhadatta (*Mudrarakshasa*), Vishnu Sharma (*Panchatantra*).\n- **Dravidian & Sangam:** Tamil, Telugu, Kannada, Malayalam; *Tolkappiyam*, *Tirukkural* (Thiruvalluvar), *Silappadikaram*, *Manimekalai*.\n- **Medieval & Bhakti:** Kalhana (*Rajatarangini*), Jayadeva (*Gita Govinda*), Chand Bardai (*Prithviraj Raso*), Kannada *Ratnatraya*, Krishnadevaraya (*Amuktamalyada*), Kabir, Tulsidas (*Ramcharitmanas*), Narsinh Mehta.\n- **Persian & Urdu:** Amir Khusro (*Tuti-e-Hind*), Abul Fazl (*Ain-i-Akbari*), Dara Shikoh (*Sirr-i-Akbar*), Vali Gujarati, Ghalib.\n- **Ancient Universities:** Nalanda (Bihar - Dharmaganja, Hiuen Tsang), Takshashila (Gandhara - Chanakya, Panini, Jivaka), Varanasi, Vallabhi (Gujarat - Maitraka dynasty, Hinayana, I-Tsing).",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "reflection",
        "content": "✨ **Reflective Quest:** If you were a scholar in ancient India, would you choose to study medicine at Takshashila with Acharya Jivaka, astronomy and philosophy at Nalanda with the Dharmaganja manuscripts, or administration and debate at Vallabhi under the golden gates? How can preserving our rich multilingual literary heritage empower India in the 21st century?",
        "difficulty": "Intermediate",
        "bloom": "Create"
    })
    
    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    # Save to GSEB Class 10 Social Science Ch4
    gseb_out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_social_science_ch4.json"
    os.makedirs(os.path.dirname(gseb_out_path), exist_ok=True)
    with open(gseb_out_path, "w", encoding="utf-8") as f:
        json.dump(final_json, f, indent=2, ensure_ascii=False)
        
    # Also save to NCERT Class 10 Social Science Ch4
    ncert_out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_social_science_ch4.json"
    final_json["metadata"]["id"] = "ncert_class10_social_science_ch4"
    with open(ncert_out_path, "w", encoding="utf-8") as f:
        json.dump(final_json, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully generated Supreme Chapter 4 for GSEB and NCERT Social Science!")

if __name__ == "__main__":
    generate_supreme_gseb_ss_ch4()
