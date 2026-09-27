import json
import os

def generate_supreme_gseb_ss_ch2():
    chapter_id = "gseb_class10_social_science_ch2"
    title = "Chapter 2: Cultural Heritage of India: Traditional Handicrafts and Fine Arts"
    
    metadata = {
        "id": chapter_id,
        "title": title,
        "subtitle": "The Ultimate GSEB & NCERT Board Exam Mastery Guide",
        "subject": "Social Science",
        "grade": "10",
        "board": "GSEB/NCERT",
        "curriculum": ["GSEB", "NCERT", "CBSE"],
        "language": "English/Gujarati/Hindi (Bilingual)",
        "difficulty": "Advanced",
        "estimated_minutes": 240,
        "version": "3.0.0-SUPREME-SS",
        "author": "Antigravity Supreme Intelligence",
        "reviewed_by": "Chief Academic Architect",
        "tags": [
            "social_science",
            "cultural_heritage",
            "traditional_handicrafts",
            "fine_arts",
            "clay_work",
            "patan_patola",
            "double_ikat",
            "embroidery_mutwa",
            "leather_work",
            "meenakari",
            "jari_surat",
            "metal_work",
            "wood_carving",
            "jadtar_bikaner",
            "akik_khambhat",
            "indian_music",
            "classical_dance",
            "bharatanatyam",
            "kuchipudi",
            "kathakali",
            "kathak",
            "manipuri",
            "bhavai",
            "gujarat_folk_dance",
            "garba",
            "dhamaal_siddhi",
            "padhar_dance",
            "gseb_class10",
            "board_special",
            "bilingual"
        ],
        "learning_outcomes": [
            "Distinguish clearly between Biological Heritage `(જૈવિક વારસો / जैविक विरासत)`, Material Heritage `(ભૌતિક વારસો / भौतिक विरासत)`, and Cultural Heritage `(સાંસ્કૃતિક વારસો / सांस्कृतिक विरासत)`.",
            "Explain ancient Indian traditional handicrafts: Clay Work, Weaving, Embroidery, Leather Work, Diamond & Enamel Work, Jari Work, Metal Work, Wood Carving, Inlay (Jadtar), and Akik Work.",
            "Master the historical significance and craftsmanship of Dhaka's Muslin, Patan's Patola (`Double Ikat`), and Bandhani.",
            "Analyze the 3 ancient classical music treatises: Sangeet Makarand, Sangeet Ratnakar, and Sangeet Parijat, along with 7 Swaras and 5 Ragas.",
            "Compare the 5 Classical Dance Forms of India (Bharatanatyam, Kuchipudi, Kathakali, Kathak, Manipuri) by origins, texts, and famous exponents.",
            "Understand the 700-year-old Gujarati theatrical art of Bhavai and the folk/tribal dances of Gujarat (Garba, Garbi, Ras, Dhamaal of Siddhis, Padhar, Chharo)."
        ],
        "ai_context": {
            "learning_goal": "Transform the student into a top-performing scholar in GSEB Class 10 Social Science Chapter 2. Use vivid cultural narratives, geographic associations, mnemonic memory tricks, and inline bilingual translations for tough terms.",
            "common_misconceptions": [
                "Students confuse the 3 ancient music treatises and their authors (Narad: Makarand; Sarangdev: Ratnakar; Ahobale: Parijat).",
                "Students mix up the foundational texts of Bharatanatyam (Natya Shastra & Abhinav Darpan) with Kuchipudi.",
                "Students think Double Ikat (Bevad Ikt) is simple block printing rather than warp-and-weft dyed weaving.",
                "Students confuse the geographic origin of Jadtar (Bikaner) and Akik polishing (Khambhat)."
            ],
            "tutor_hint": "Anchor every craft and dance with its geographic home and key Sanskrit/Gujarati root words (e.g., Patan = Patola = Double Ikat; Khambhat = Akik; Bikaner = Jadtar; Asait Thakar = Bhavai = Bhungal; Tanjore = Bharatanatyam)."
        }
    }
    
    blocks = []
    
    # =========================================================================
    # MODULE 1: THE SPECTRUM OF HERITAGE & INDIA'S 64 ARTS
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "Why was ancient India called the 'Golden Bird' `(સોને કી ચિડિયા / सोने की चिड़िया)` by world travelers? It wasn't just because of gold reserves; it was because Indian master artisans possessed extraordinary secrets of 64 traditional arts `(૬૪ કલાઓ / ६४ कलाएं)`—from weaving gossamer cloth that could pass through a finger ring to crafting bronze sculptures praised globally. Welcome to the breathtaking saga of **Cultural Heritage of India: Traditional Handicrafts and Fine Arts `(ભારતનો સાંસ્કૃતિક વારસો: પરંપરાગત હસ્ત અને લલિતકલાઓ / भारत की सांस्कृतिक विरासत: परंपरागत हस्तकला और ललित कलाएं)`**!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "The Three Pillars of Indian Heritage: Biological Heritage `(જૈવિક વારસો / जैविक विरासत)` + Material Heritage `(ભૌતિક વારસો / भौतिक विरासत)` + Cultural Heritage `(સાંસ્કૃતિક વારસો / सांस्कृतिक विरासत)`.",
        "image_url": "assets/images/heritage_three_pillars.jpg",
        "alt_text": "Conceptual flowchart dividing Indian heritage into Biological, Material, and Cultural streams with examples."
    })
    
    blocks.append({
        "type": "theory",
        "content": "India's heritage is classified into three fundamental categories:\n\n1. **Biological Heritage `(જૈવિક વારસો / जैविक विरासत)`:** Physical and genetic traits `(શારીરિક અને માનસિક લક્ષણો / शारीरिक और मानसिक लक्षण)` received by a child from parents by birth (e.g., skin color, height, eye color, facial structure).\n\n2. **Material / Physical Heritage `(ભૌતિક વારસો / भौतिक विरासत)`:** Tangible properties inherited from ancestors `(પૂર્વજો તરફથી મળેલી મિલકત / पूर्वजों से प्राप्त संपत्ति)` such as houses, agricultural land, estates, vehicles, and physical wealth.\n\n3. **Cultural Heritage `(સાંસ્કૃતિક વારસો / सांस्कृतिक विरासत)`:** Whatever human beings create, discover, produce, or invent using their own intellect `(બુદ્ધિ / बुद्धि)`, wisdom `(આવડત / समझ)`, skill `(કલા-કૌશલ્ય / कला-कौशल)`, and craftsmanship. Ancient Indian literature documents **64 Traditional Arts `(૬૪ કલાઓ / ६४ कलाएं)`** encompassing handicrafts, sculpture, architecture, painting, music, dance, and dramatic art.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Teacher's Secret:** In GSEB board exams, a very frequent 2-mark question asks: *'Differentiate between Biological Heritage and Material Heritage.'* Always provide the definition AND 2 real-life examples for each!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "mcq",
        "content": "What type of heritage includes the physical and mental characteristics inherited from parents at birth?",
        "options": [
            "Material Heritage `(ભૌતિક વારસો / भौतिक विरासत)`",
            "Biological Heritage `(જૈવિક વારસો / जैविक विरासत)`",
            "Cultural Heritage `(સાંસ્કૃતિક વારસો / सांस्कृतिक विरासत)`",
            "Natural Heritage `(પ્રાકૃતિક વારસો / प्राकृतिक विरासत)`"
        ],
        "correct_answer": "Biological Heritage `(જૈવિક વારસો / जैविक विरासत)`",
        "explanation": "Biological heritage refers to genetic and physical/mental traits inherited directly from parents at the time of birth.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    # =========================================================================
    # MODULE 2: ART OF CLAY WORK (માટીકામ / मिट्टी कला)
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "Think about our relationship with mother earth: From the clay toy in a baby's cradle `(પારણું / पालना)` to the clay urn after cremation `(સ્મશાન / श्मशान)`, human life in India has been intimately bound with clay from **cradle to grave `(જન્મથી મરણ સુધી / जन्म से मरण तक)`**! Before metals were discovered, clay was our ultimate technology.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "diagram",
        "content": "Potter's Wheel `(કુંભારનો ચાકડો / कुम्हार का चाक)` - India's earliest machine for mass manufacturing baked clay `(Terracotta / પકવેલી માટી)` utensils.",
        "image_url": "assets/images/ancient_potters_wheel_terracotta.jpg",
        "alt_text": "Ancient artisan shaping clay pots on a rotating potter's wheel with terracotta artifacts in background."
    })

    blocks.append({
        "type": "theory",
        "content": "**The Golden Legacy of Clay Work `(માટીકામ / मिट्टी कला)`:**\n- **India's First Machine:** The Potter's Wheel `(કુંભારનો ચાકડો / कुम्हार का चाक)` is considered the earliest machine in Indian civilization for handicrafts.\n- **Everyday Utility:** In ancient times, utensils for cooking, storing water (`માટલું / मटका`), earthen lamps (`કોડિયું / दीया`), curd pots (`કુલડી / कुल्हड़`), churners, and grain storage bins (`કોઠાર / कोठार`) were crafted entirely of clay.\n- **House Plastering:** Walls of village houses were plastered with a protective mixture of clay and cow dung `(લીંપણ / लीपना)` to maintain natural insulation against extreme heat and cold.\n- **Terracotta `(પકવેલી માટી / पकी हुई मिट्टी)`:** Ancient India was world-famous for producing both unbaked `(કાચી માટી / कच्ची मिट्टी)` and baked clay artifacts `(Terracotta)`.\n- **Key Archaeological Sites:**\n  1. **Laghnaj `(લાંઘણજ)`:** Located in Mehsana district, Gujarat (remains of ancient handmade clay utensils).\n  2. **Nagarjuna Konda `(નાગાર્જુન કોંડા)`:** Famous South Indian archaeological site for ancient pottery.\n  3. **Harappa & Mohen-jo-Daro:** Excavations revealed red-clay utensils with black geometric and animal designs.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "memory_trick",
        "content": "🧠 **Mnemonic for Ancient Clay Sites:** \nRemember **'L-N' (Laghnaj to Nagarjuna)**:\n- **L**aghnaj = Mehsana (Gujarat)\n- **N**agarjuna Konda = South India\nBoth prove ancient Indian mastery over unbaked and baked clay (Terracotta)!",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "mcq",
        "content": "Which ancient archaeological site in Mehsana district (Gujarat) yielded famous remains of ancient handmade clay utensils?",
        "options": [
            "Lothal `(લોથલ / लोथल)`",
            "Laghnaj `(લાંઘણજ / लांघणज)`",
            "Dholavira `(ધોળાવીરા / धोलावीरा)`",
            "Rangpur `(રંગપુર / रंगपुर)`"
        ],
        "correct_answer": "Laghnaj `(લાંઘણજ / लांघણજ)`",
        "explanation": "Laghnaj in Mehsana district of Gujarat is a prominent prehistoric site where ancient handmade clay utensils were excavated.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    # =========================================================================
    # MODULE 3: ART OF WEAVING & TEXTILE HERITAGE (વણાટકામ અને કાપડકલા)
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "Could you imagine a royal 20-meter saree so feather-light and exquisite that the entire garment could pass effortlessly through a tiny finger ring `(વીંટીમાંથી પસાર થવું / अंगूठी से निकलना)` and fold neatly inside a small matchbox `(માચીસની પેટી / माचिस की डिब्बी)`? This was not fantasy—this was the world-renowned **Dhaka Muslin `(ઢાકાનું મલમલ / ढाका की मलमल)`** of ancient India!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "diagram",
        "content": "Patan's Master Weavers creating Patola on traditional wooden looms using the complex Double Ikat `(બેવડ ઈક્ત / द्विपक्षीय इकत)` technique.",
        "image_url": "assets/images/patan_patola_double_ikat.jpg",
        "alt_text": "Close-up of vibrant silk Patan Patola saree showing identical geometric motifs on both sides."
    })

    blocks.append({
        "type": "theory",
        "content": "**Mastering Indian Textile & Weaving `(વણાટકામ અને કાપડકલા / बुनाई और वस्त्र कला)`:**\n\n1. **Art of Spinning `(કાંતણ / कताई)`:** Drawing long, delicate strands of thread from raw cotton balls and twisting them together onto a spindle (`તકલી / तकली`) or spinning wheel (`ચરખો / चरखा`). Mahatma Gandhi transformed spinning into a national movement of self-reliance (Swadeshi `સ્વદેશી`).\n\n2. **Dhaka Muslin `(ઢાકાનું મલમલ / ढाका की मलमल)`:** Renowned across the globe for supreme softness and fineness—an entire saree could slide through a ring or pack inside a matchbox.\n\n3. **Patola of Patan `(પાટણના પટોળાં / पाटण के पटोला)`:**\n   - **Golden Era:** During the reign of King Siddharaj Jaisinh `(સિદ્ધરાજ જયસિંહ)` in Gujarat's Solanki era `(સોલંકી યુગ)`, master weavers called **Salvis `(સાળવીઓ)`** migrated and settled in Patan.\n   - **Double Ikat `(બેવડ ઈક્ત / द्विपक्षीय इकत)`:** 'Ikat' means weaving/dyeing (`ઈક્ત એટલે વણાટ`). 'Bevad Ikat' means the warp `(તાણા)` and weft `(વાણા)` are both tie-dyed before weaving so that the design and colors appear **100% identical on both sides**. It can be worn from either side!\n   - **Longevity:** Colored with natural herbal and mineral dyes, Patola lasts for hundreds of years without tearing or color fading.\n   - **Legendary Proverb:** *'પડી પટોળે ભાત, ફાટે પણ ફીટે નહિ'* (`Padi Patole bhat, fate pan fite nahi` — The design dyed into a Patola may wear out with centuries, but its colors will never fade).\n\n4. **Other Legendary Indian Textiles:**\n   - **Bandhani `(બાંધણી / बंधेज / Tie-Dye)`:** Famous centers in Gujarat include **Jamnagar, Jetpur, Bhuj, and Mandvi** with traditional motifs of Elephant (`હાથી`), Puppet (`પૂતળી`), Pitcher (`ઘડો`), and geometric dots.\n   - **Kanchipuram Silk `(કાંચીપુરમ)`:** Tamil Nadu's heavy gold-bordered silk.\n   - **Banarasi Silk `(બનારસી સાડી)`:** Famous brocade and zari sarees of Varanasi.\n   - **Kashmiri Carpets `(કાશ્મીરી ગલીચા / कालीन)`:** Hand-knotted pure wool and silk carpets.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC (GSEB 3 Marks):** Write a detailed short note on **'Patola of Patan'**.\n\n**Topper's Answer Structure:**\n1. Historical Context: Solanki era & King Siddharaj Jaisinh; Salvi master craftsmen.\n2. Technical Definition: Double Ikat (`બેવડ ઈક્ત`) where 'Ikat' means weaving; identical on both sides.\n3. Unique Traits: Natural dyes, lasts over 300 years, reversible wear.\n4. Cultural Proverb: Quote *'પડી પટોળે ભાત, ફાટે પણ ફીટે નહિ'*.",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    blocks.append({
        "type": "mcq",
        "content": "What is the specialized weaving technique of Patan's Patola called, in which the design is identical on both sides?",
        "options": [
            "Single Warp `(એકલ તાણા / एकल ताना)`",
            "Double Ikat / Bevad Ikt `(બેવડ ઈક્ત / द्विपक्षीय इकत)`",
            "Zardosi `(જરદોશી / ज़रदोज़ी)`",
            "Bandhani `(બાંધણી / बंधेज)`"
        ],
        "correct_answer": "Double Ikat / Bevad Ikt `(બેવડ ઈક્ત / द्विपक्षीय इकत)`",
        "explanation": "Double Ikat (Bevad Ikt) is the complex weaving technique where both warp and weft threads are dyed beforehand, creating an identical pattern on both sides.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    # =========================================================================
    # MODULE 4: ART OF EMBROIDERY (ભરતગૂંથણ કલા / कसीदाकारी)
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "When archaeologists unearthed statues from the 5,000-year-old Indus Valley civilization at Harappa and Mohen-jo-Daro, they were stunned to find the statues draped in shawls with intricate floral embroidery `(ભરતગૂંથણ / कसीदाकारी)`! How did this needlework evolve into Gujarat's most celebrated rural art?",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "diagram",
        "content": "Traditional Kutch Toran and Chakla featuring mirror-work `(આભલાંકામ)` and geometric needlework by the Mutwa community.",
        "image_url": "assets/images/kutch_banni_embroidery.jpg",
        "alt_text": "Vibrant handcrafted Gujarati Toran with colorful threads and embedded circular mirrors."
    })

    blocks.append({
        "type": "theory",
        "content": "**Art of Embroidery `(ભરતગૂંથણ કલા / कसीदाकारी / कशीदाकारी)` in Gujarat:**\n- **Regional Centers:** **Kutch `(કચ્છ)`** and **Saurashtra `(સૌરાષ્ટ્ર)`** are the epicenters of traditional Gujarati embroidery.\n- **The Mutwa Community of Banni `(બન્ની વિસ્તારના મુતવા સમુદાય)`:** The Banni region in Kutch is internationally celebrated for the exquisite, fine geometric and floral needlecraft practiced by women of the Mutwa community.\n- **Traditional Household Articles:**\n  1. **Toran `(તોરણ / तोरण)`:** Decorative hangings for auspicious home entrances.\n  2. **Chakla `(ચાકળા / चकले)`:** Square embroidered wall hangings.\n  3. **Todaliya `(તોડલિયા)`:** Embroidered door frame ornaments.\n  4. **Chandarva `(ચંદરવા)`:** Embroidered cloth canopies hung during celebrations.\n  5. **Dharaniya & Pillow Covers `(ધરણિયા અને ઓશિકાં)`:** Bedding decorations.\n  6. **Traditional Attire:** Ghaghra-Choli, Kediya `(કેડિયું / अंगरखा)`, and Rajput/Ahir male jackets.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "mcq",
        "content": "Which community of the Banni region in Kutch is world-renowned for their unique geometric and floral needle embroidery?",
        "options": [
            "Salvi Community `(સાળવી સમુદાય / सालवी समुदाय)`",
            "Mutwa Community `(મુતવા સમુદાય / मुतवा समुदाय)`",
            "Siddhi Community `(સિદ્દી સમુદાય / सिद्दी समुदाय)`",
            "Padhar Community `(પઢાર સમુદાય / प Contemporaryार समुदाय)`"
        ],
        "correct_answer": "Mutwa Community `(મુતવા સમુદાય / मुतवा समुदाय)`",
        "explanation": "The women of the Mutwa community residing in the Banni area of Kutch are globally recognized for their master embroidery work.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    # =========================================================================
    # MODULE 5: LEATHER INDUSTRY (ચર્મકામ / चर्म उद्योग)
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "From the water carrier's bag `(Mashak / મશક)` quenching the thirst of travelers in deserts to the roaring battle drums `(Nagara / નગારું)` and blacksmith's roaring fire bellows `(Dhaman / ધમણ)`—leather was ancient India's multi-utility industrial wonder!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "diagram",
        "content": "Versatile applications of processed leather in ancient India: Mashak, Kos, Dholak, Rajasthan's royal Mojdis, and shields.",
        "image_url": "assets/images/leather_craft_mashak_mojdi.jpg",
        "alt_text": "Infographic showing traditional leather tanning, handcrafted mojdis, and musical instruments."
    })

    blocks.append({
        "type": "theory",
        "content": "**The Traditional Leather Industry `(ચર્મકામ / चर्म उद्योग)`:**\n- **Traditional Tanning `(ચામડું કમાવવું / चमड़ा पकाना)`:** In ancient India, skin of dead domestic animals was cured using natural barks, vegetable tannins, and salts without cruelty to live animals.\n- **Agricultural & Domestic Use:**\n  1. **Kos `(કોસ / चरस)`:** Huge leather bucket attached to ropes and bullocks to lift irrigation water from deep wells.\n  2. **Mashak & Pakhal `(મશક અને પખાલ / मशक)`:** Airtight leather water-bags used for carrying drinking water across long distances.\n- **Musical Instruments:** Animal hides were essential for crafting rhythm instruments like **Dholak `(ઢોલક)`, Tabla `(તબલા)`, Nagara `(નગારું)`, Damru `(ડમરુ)`, and Dhol `(ઢોલ)`**.\n- **Industrial & Martial Uses:**\n  1. **Blacksmith's Bellows `(લુહારની ધમણ / लोहार की धौंकनी)`:** Pumping continuous airflow to melt iron and bronze.\n  2. **Defensive Shields `(ઢાલ / ढाल)`:** Hardened leather shields used by warriors in battles.\n  3. **Footwear & Saddlery:** Rajasthan's artistic embroidered **Mojdis `(મોજડી / मोजड़ी)`**, belts, purses, and leather saddles `(સાજ / પલાણ)` for horses and camels.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Teacher's Secret:** Keep these two distinct terms straight in your exam answers:\n- **Kos `(કોસ)`** = Leather bucket to draw water from wells for farming.\n- **Mashak `(મશક)`** = Portable leather bag for carrying drinking water.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "mcq",
        "content": "Which traditional leather equipment was utilized by blacksmiths to pump continuous air into forge furnaces?",
        "options": [
            "Mashak `(મશક / मशक)`",
            "Dhaman / Bellows `(ધમણ / धौंकनी)`",
            "Kos `(કોસ / चरस)`",
            "Mojdi `(મોજડી / मोजड़ी)`"
        ],
        "correct_answer": "Dhaman / Bellows `(ધમણ / धौंकनी)`",
        "explanation": "Dhaman (bellows) made of leather was used by blacksmiths to blow continuous air into fires to heat and forge metals.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    # =========================================================================
    # MODULE 6: DIAMOND, BEAD WORK, ENAMEL (MEENAKARI) & JARI WORK
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "India has a majestic coastline stretching **7,517 km `(૭૫૧૭ કિમી દરિયાકિનારો)`**. This oceanic highway enabled ancient Indian merchants to trade diamonds, lustrous pearls, and gemstones to Rome, Egypt, and Mesopotamia! Legendary gems like the **Koh-i-Noor `(કોહિનૂર)`** and **Great Mughal `(ગ્રેટ મુઘલ)`** were discovered right here in Indian soil.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "diagram",
        "content": "The Centers of Enamel Art (Meenakari `મીનાકારી`): Jaipur/Delhi (Red & Green), Lucknow (Blue & Green), Varanasi (Pink), and Hyderabad.",
        "image_url": "assets/images/meenakari_enamel_centers_map.jpg",
        "alt_text": "Map of India highlighting Jaipur, Delhi, Lucknow, Varanasi, and Hyderabad with samples of Meenakari jewelry."
    })

    blocks.append({
        "type": "theory",
        "content": "**Precious Crafts: Diamond, Bead, Enamel & Jari Art:**\n\n1. **Diamond & Pearl Heritage `(હીરા અને મોતીકામ / हीरा और मोती)`:**\n   - Indian kings and emperors decorated royal thrones, crowns, palanquins, and ornaments with 9 precious gems (*Navratnas*).\n   - **Gujarat's Bead Work `(મોતીકામ)`:** Gujarat is unique for artistic pearl/bead craft: making decorative **Toran `(તોરણ)`, Pachhit `(પછીત)`, Indhoni `(ઈંઢોણી - head rings for water pots)`, Modhiya `(મોઢિયા)`, Dhoolkothi, Kalash decorations, and Hand fans `(હાથપંખા)`**.\n\n2. **Enamel Work / Meenakari `(મીનાકારી / मीनाकारी)`:**\n   - **Definition:** The art of engraving gold and silver ornaments and filling the cavities with bright, vitreous enamel colors (red, green, blue, pink).\n   - **Leading Centers in India:**\n     - **Jaipur and Delhi:** Master craftsmen in vibrant **Red and Green `(લાલ અને લીલો રંગ)`** enamel.\n     - **Lucknow:** Famous for **Green and Blue `(લીલો અને વાદળી રંગ)`** enamel.\n     - **Varanasi:** Globally famous for rare **Lotus Pink `(ગુલાબી રંગ)`** enamel on gold.\n     - **Hyderabad:** Renowned for royal dark enamel patterns.\n\n3. **Jari Work of Surat `(સુરતનું જરીકામ / सूरत का ज़री काम)`:**\n   - **Surat `(સુરત)`** has been India's undisputed capital of gold and silver thread embroidery (Jari work) since medieval times.\n   - **Zardosi Work `(જરદોશી / ज़रदोज़ी)`:** Heavy, dimensional gold embroidery on royal robes, bridal **Panetar `(પાણેતર)`**, **Gharchola `(ઘરચોળા)`**, and border lace (`કાંગરી / કિનારી`).",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    blocks.append({
        "type": "memory_trick",
        "content": "🧠 **Meenakari Color Matcher:**\n- **Varanasi = Pink** (Think: Pink Lotus / Gulabi Meenakari)\n- **Jaipur & Delhi = Red & Green** (Think: Royal Rajasthani Gem colors)\n- **Lucknow = Blue & Green** (Think: Peacock shades)\n- **Surat = Jari Capital**",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "mcq",
        "content": "Which city of Gujarat has been globally famous for Zardosi and Jari work on bridal Panetar and Gharchola sarees?",
        "options": [
            "Ahmedabad `(અમદાવાદ / अहमदाबाद)`",
            "Surat `(સુરત / सूरत)`",
            "Rajkot `(રાજકોટ / राजकोट)`",
            "Vadodara `(વડોદરા / वडोदरा)`"
        ],
        "correct_answer": "Surat `(સુરત / सूरत)`",
        "explanation": "Surat is the prominent historical center for Jari and Zardosi embroidery in Gujarat and across India.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    # =========================================================================
    # MODULE 7: METAL, WOOD, INLAY (JADTAR) & AKIK ART
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "Imagine a river pebble transformed into a glowing ruby-like gem in Khambhat, or a chunk of teak carved into an ornate royal swing in Sankheda! Let's explore how Indian artisans turned metal, wood, and stones into timeless treasures.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "diagram",
        "content": "Bronze Nataraja statue of Chola Dynasty alongside Sankheda's lacquered wooden furniture and Khambhat's polished Akik stones.",
        "image_url": "assets/images/metal_wood_akik_crafts.jpg",
        "alt_text": "Split image showing Nataraja bronze sculpture, Sankheda wooden swing, and polished carnelian Akik beads."
    })

    blocks.append({
        "type": "theory",
        "content": "**Metal Work, Wood Carving, Inlay (Jadtar), and Akik Art:**\n\n1. **Metal Work `(ધાતુકામ / धातु कला)`:**\n   - Succeeded the Stone Age `(પાષાણ યુગ)`. Lothal artisans crafted drills, curved saws, needles, and sickles from copper and bronze.\n   - **Masterpieces:** The Bronze **Dancing Girl** of Mohen-jo-Daro, the world-famous **Nataraja bronze statue `(તાંડવ નૃત્ય કરતા નટરાજનું કાંસાનું શિલ્પ)`** of the Chola period, and the 7.5-foot high copper Buddha statue at Sultanganj (Bihar).\n\n2. **Wooden Art `(કાષ્ઠકલા / काष्ठ कला)`:**\n   - Evolved from firewood to wooden pillars, ceilings, temple jharokhas, and idols.\n   - **Sankheda `(સંખેડા - Chhota Udepur district)`:** Globally famous for lacquered artistic wooden furniture and swings `(હીંચકા)`.\n   - **Idar `(ઈડર)` and Mahuva `(મહુવા)`:** Celebrated for wooden toys `(રમકડાં)`.\n\n3. **Inlay Work / Jadtar `(જડતર કામ / जड़तर काम)`:**\n   - The delicate art of embedding uncut diamonds, pearls, rubies, and emeralds into solid gold and silver jewelry.\n   - **Bikaner `(બીકાનેર - Rajasthan)`** is the undisputed capital of royal Jadtar jewelry.\n\n4. **Akik Work `(અકીક કામ / अकीक - Agate & Carnelian)`:**\n   - **Composition:** Akik is a semi-precious stone, primarily Chalcedony mixed with Silica, formed by volcanic activity in river valleys of Gujarat (Surat, Ranpur, Ahmedabad).\n   - **Khambhat `(ખંભાત)`:** The raw stones are sent to Khambhat, where master lapidaries bake, chisel, cut, and polish them into lustrous beads, rosaries, and necklaces.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT PAIRING:** Match these locations instantly in MCQ/Match the Column:\n1. **Sankheda** ⟶ Wooden swings & furniture `(લાકડાના હીંચકા અને ફર્નિચર)`\n2. **Khambhat** ⟶ Akik stone polishing `(અકીક કામ)`\n3. **Bikaner** ⟶ Jadtar / Inlay work `(જડતર કામ)`\n4. **Idar & Mahuva** ⟶ Wooden toys `(લાકડાના રમકડાં)`",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "mcq",
        "content": "Which town in Gujarat is the world-famous center where raw Akik (agate) stones from riverbeds are polished and crafted into jewelry?",
        "options": [
            "Sankheda `(સંખેડા / संखेड़ा)`",
            "Khambhat `(ખંભાત / खंभात)`",
            "Patan `(પાટણ / पाटण)`",
            "Mahuva `(મહુવા / महुआ)`"
        ],
        "correct_answer": "Khambhat `(ખંભાત / खंभात)`",
        "explanation": "Raw Akik stones from Surat and Ranpur are sent to Khambhat, where skilled artisans polish them into lustrous ornaments and beads.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    # =========================================================================
    # MODULE 8: PAINTING / FINE ARTS (ચિત્રકલા / चित्रकला)
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "Can an art form convey human emotions without uttering a single spoken word? Painting `(ચિત્રકલા / चित्रकला)` holds the highest supreme rank among all fine arts because it expresses life's deepest feelings purely through **lines and colors `(રેખાઓ અને રંગો / रेखाओं और रंगों)`**!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "diagram",
        "content": "Prehistoric rock paintings of Bhimbetka Caves (Madhya Pradesh) alongside world-famous Ajanta murals (Bodhisattva Padmapani).",
        "image_url": "assets/images/bhimbetka_ajanta_paintings.jpg",
        "alt_text": "Side by side comparison of Bhimbetka cave petroglyphs and exquisite colorful Ajanta cave fresco."
    })

    blocks.append({
        "type": "theory",
        "content": "**The Heritage of Indian Painting `(ચિત્રકલા / चित्रकला)`:**\n- **Supreme Position:** Among all 64 arts, Painting occupies the topmost rank because it has the power to manifest visual reality, natural forms, and inner emotions through lines and colors.\n- **Prehistoric Rock Art:** The earliest evidence of Indian painting (5,000+ years old) was discovered in the **Bhimbetka Caves `(ભીમબેટકાની ગુફાઓ - Madhya Pradesh)`**, drawn by Stone Age humans depicting wild animals, birds, and hunting scenes with mineral colors.\n- **Ajanta-Ellora Murals `(અજંતા-ઈલોરાના ચિત્રો)`:** The Buddhist frescoes at Ajanta (Maharashtra), especially **Bodhisattva Padmapani `(પદ્મપાણિનું ચિત્ર)`**, represent the golden pinnacle of world art.\n- **Auspicious Folk Paintings:** Indian traditions include drawing **Rangoli `(સાથિયા / રંગોળી)`** at doorsteps, Swastik symbols, and Ganesha figures during festivals.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "mcq",
        "content": "Which prehistoric cave site in Madhya Pradesh contains the oldest cave paintings of animals and birds drawn by Stone Age humans?",
        "options": [
            "Ajanta Caves `(અજંતા ગુફાઓ / अजंता गुफाएं)`",
            "Bhimbetka Caves `(ભીમબેટકા ગુફાઓ / भीमबेटका गुफाएं)`",
            "Elephanta Caves `(એલિફન્ટા ગુફાઓ / एलिफेंटा गुफाएं)`",
            "Ellora Caves `(ઇલોરા ગુફાઓ / एलोरा गुफाएं)`"
        ],
        "correct_answer": "Bhimbetka Caves `(ભીમબેટકા ગુફાઓ / भीमबेटका गुफाएं)`",
        "explanation": "Bhimbetka in Madhya Pradesh is a UNESCO World Heritage site known for Stone Age rock paintings depicting animals and hunting scenes.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    # =========================================================================
    # MODULE 9: THE HERITAGE OF MUSIC (સંગીત કલા / संगीत कला)
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "Did you know that while global music divides itself simply into sound and rhythm, Indian music is uniquely spiritual, uniting **Swara `(સ્વર)`, Raga `(રાગ)`, and Taal `(તાલ)`**? The **Samaveda `(સામવેદ)`** is revered as the mother fountainhead—the *Gangotri* of world music!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "diagram",
        "content": "The Three Pillars of Music Treatises: Sangeet Makarand (Narad, 900 BC), Sangeet Ratnakar (Sarangdev), and Sangeet Parijat (Ahobale, 1665).",
        "image_url": "assets/images/indian_classical_music_treatises.jpg",
        "alt_text": "Chart summarizing the 7 Swaras, 5 Ragas from Shiva's mouth, and comparison of the 3 ancient music texts."
    })

    blocks.append({
        "type": "theory",
        "content": "**Indian Classical Music `(સંગીત કલા / संगीत कला)`:**\n- **Two Traditions:** Indian music is bifurcated into **Classical Music `(શાસ્ત્રીય સંગીત)`** and **Folk Music `(લોકસંગીત)`**.\n- **Seven Swaras `(સાત સ્વર)`:** Sa, Re, Ga, Ma, Pa, Dha, Ni `(સા, રે, ગ, મ, પ, ધ, ની)`.\n- **Five Primary Ragas:** Believed to have originated from the five sacred faces of Lord Shiva `(ભગવાન શિવના પંચમુખમાંથી)`:\n  1. **Shree `(શ્રી)`**\n  2. **Deepak `(દીપક)`**\n  3. **Hindol `(હિંદોળ)`**\n  4. **Megh `(મેઘ)`**\n  5. **Bhairavi `(ભૈરવી)`**.\n\n**The Three Master Treatises on Indian Music:**\n\n1. **Sangeet Makarand `(સંગીત મકરંદ)`:**\n   - Written by **Sage Narad `(નારદ)`** around 900 BC.\n   - Describes **19 types of Veenas `(૧૯ પ્રકારની વીણા)`** and **101 types of Taals `(૧૦૧ પ્રકારના તાલ)`**.\n\n2. **Sangeet Ratnakar `(સંગીત રત્નાકર)`:**\n   - Composed by **Pandit Sarangdev `(પંડિત સારંગદેવ)`** who lived in Daulatabad (Devgiri) and understood both North and South Indian music.\n   - Pandit Vishnu Narayan Bhatkhande termed it the **'Most Authentic Book on Music' `(સંગીતનો સૌથી પ્રમાણભૂત ગ્રંથ)`** and the *'Soul of Music'*.\n\n3. **Sangeet Parijat `(સંગીત પારિજાત)`:**\n   - Written by **Pandit Ahobale `(પંડિત અહોબલે)`** in 1665 AD for Northern Classical Music.\n   - Identified that every raga has its own distinct signature and recorded **29 individual swaras `(૨૯ પ્રકારના સ્વરો)`**.\n\n**Great Musical Legends:**\n- **Amir Khusro `(અમીર ખુસરો)`:** 13th-century polymath conferred with the title *'Tuti-e-Hind'* `(તુતી-એ-હિન્દ / Parrot of India)` during Alauddin Khilji's reign.\n- **Bhakti Era:** Swami Haridas, Tansen, Baiju Bawra, and the brave musician sisters of Vadnagar (Gujarat)—**Tana and Riri `(તાના અને રીરી)`** who sacrificed their lives to protect Raga Malhar.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Teacher's Mnemonic for 3 Music Treatises:**\n- **N-M-19** ⟶ **N**arad wrote **M**akarand (**19** Veenas, 101 Taals).\n- **S-R-Soul** ⟶ **S**arangdev wrote **R**atnakar (**S**oul of Music).\n- **A-P-29** ⟶ **A**hobale wrote **P**arijat (**29** Swaras in 1665).",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "mcq",
        "content": "Which music treatise written by Sage Narad around 900 BC describes 19 varieties of Veenas and 101 varieties of Taals?",
        "options": [
            "Sangeet Ratnakar `(સંગીત રત્નાકર / संगीत रत्नाकर)`",
            "Sangeet Parijat `(સંગીત પારિજાત / संगीत पारिजात)`",
            "Sangeet Makarand `(સંગીત મકરંદ / संगीत मकरंद)`",
            "Natya Shastra `(નાટ્યશાસ્ત્ર / नाट्यशास्त्र)`"
        ],
        "correct_answer": "Sangeet Makarand `(સંગીત મકરંદ / संगीत मकरंद)`",
        "explanation": "Sangeet Makarand, authored by Sage Narad around 900 BC, documents 19 types of veenas and 101 types of rhythmic taals.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    # =========================================================================
    # MODULE 10: CLASSICAL DANCES OF INDIA (શાસ્ત્રીય નૃત્યો)
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "The word 'Dance' originates from the Sanskrit root **'Nrit' `(નૃત્)`**. In Indian cosmology, **Lord Shiva `(ભગવાન શિવ)`** is reverently worshipped as **Nataraja `(નટરાજ)`**—the supreme Lord of Cosmic Dance, who brought celestial dance to mortal humans on earth. Let's tour the 5 glorious classical dances of India!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "diagram",
        "content": "Comparative visual matrix of the 5 Classical Dances: Bharatanatyam, Kuchipudi, Kathakali, Kathak, and Manipuri.",
        "image_url": "assets/images/five_classical_dances_india.jpg",
        "alt_text": "Visual guide illustrating traditional postures, distinct costumes, and state origins of all 5 classical dances."
    })

    blocks.append({
        "type": "theory",
        "content": "**The 5 Classical Dance Forms of India:**\n\n1. **Bharatanatyam `(ભરતનાટ્યમ)`:**\n   - **Origin:** Tanjore district `(તાંજોર જિલ્લો)`, Tamil Nadu.\n   - **Foundational Texts:** Bharat Muni's *Natya Shastra* `(નાટ્યશાસ્ત્ર)` and Nandikeshwara's *Abhinav Darpan* `(અભિનવ દર્પણ)`.\n   - **Celebrated Exponents:** Mrinalini Sarabhai `(મૃણાલિની સારાભાઈ)`, Vaijayantimala `(વૈજયંતીમાલા)`, and Hema Malini `(હેમા માલિની)`.\n\n2. **Kuchipudi `(કુચિપુડી)`:**\n   - **Origin:** 15th century in Kuchipudi village, Andhra Pradesh.\n   - **Creator:** Guru Siddhendra Yogi `(સિદ્ધેન્દ્ર યોગી)`.\n   - **Characteristics:** Rooted in Natya Shastra, performed by both male and female dancers using expressive mudras.\n   - **Celebrated Exponents:** Guru Prahlad Sarma, Raja-Radha Reddy, and Shobha Naidu.\n\n3. **Kathakali `(કથકળી)`:**\n   - **Origin:** Kerala `(કેરળ)`.\n   - **Characteristics:** Based on epics (Mahabharata and Ramayana). Dancers wear elaborate facial makeup called **Mukhatrika `(મુખત્રિકા / મુખોટા)`**, regal decorated crowns `(કિરીટ / મુકુટ)`, and grand colorful flared skirts `(ઘેરદાર વસ્ત્રો)`.\n   - **Celebrated Exponents:** Poet Vallathol `(કવિ વલ્લથોળ - founder of Kerala Kalamandalam)`, Kalamandalam Gopi, and Krishnaprasad.\n\n4. **Kathak `(કથક)`:**\n   - **Origin:** Northern India `(ઉત્તર ભારત)`.\n   - **Golden Proverb:** *'કથન કરે સો કથક કહાવે'* (`Kathan kare so kathak kahave` — One who narrates a sacred story through rhythmic movement is a Kathak).\n   - **Characteristics:** Depicts the divine love and Rasleela of Lord Krishna and Radha. Famous for rapid pirouettes (spins) on one heel.\n   - **Celebrated Exponents:** Pandit Birju Maharaj `(પંડિત બિરજુ મહારાજ)`, Sitara Devi, and Kumudini Lakhia `(કુમુદિની લાખિયા)`.\n\n5. **Manipuri `(મણિપુરી)`:**\n   - **Origin:** Manipur (North-East India).\n   - **Theme:** Exclusively dedicated to Radha-Krishna's celestial Rasleela.\n   - **Costume:** Dancers wear a stiff cylindrical embroidered green skirt called **Kumin `(કુમિન / कुमिन)`**, paired with a velvet blouse and transparent veil.\n   - **Celebrated Exponents:** Guru Amobi Singh, Atomba Singh, Charu Mathur, and Nirmala Mehta.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM SUPER HOT TABLE:**\n| Classical Dance | Origin State | Key Distinctive Trait / Text |\n|---|---|---|\n| **Bharatanatyam** | Tamil Nadu (Tanjore) | Abhinav Darpan & Natya Shastra |\n| **Kuchipudi** | Andhra Pradesh | Founded by Guru Siddhendra Yogi |\n| **Kathakali** | Kerala | Mukhatrika makeup & Kirita crown |\n| **Kathak** | North India | 'Kathan kare so kathak kahave' |\n| **Manipuri** | Manipur | Cylindrical green skirt called 'Kumin' |",
        "difficulty": "Intermediate",
        "bloom": "Evaluate"
    })

    blocks.append({
        "type": "mcq",
        "content": "In which classical dance form do dancers wear a distinctive cylindrical green skirt called 'Kumin' to enact the Rasleela of Radha-Krishna?",
        "options": [
            "Kathakali `(કથકળી / कथकली)`",
            "Manipuri `(મણિપુરી / मणिपुरी)`",
            "Kuchipudi `(કુચિપુડી / कुचिपुड़ी)`",
            "Bharatanatyam `(ભરતનાટ્યમ / भरतनाट्यम)`"
        ],
        "correct_answer": "Manipuri `(મણિપુરી / मणिपुरी)`",
        "explanation": "Manipuri classical dancers wear the specialized stiff green cylindrical skirt known as 'Kumin' during Radha-Krishna Rasleela performances.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    # =========================================================================
    # MODULE 11: DRAMATIC ART & GUJARAT'S BHAVAI (નાટ્યકલા અને ભવાઈ)
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "Sage Bharat Muni declared 2,000 years ago: *'There is no knowledge, no scripture, no art, no action that is not found in Dramatic Art!'* And in Gujarat, this art took the form of **Bhavai `(ભવાઈ)`**—a 700-year-old open-air theatre that educated and entertained generations through humor and biting social satire!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "diagram",
        "content": "Traditional Bhavai troupe performing in a village square with the musical brass pipe called Bhungal `(ભૂંગળ)` and characters Rangla-Rangli.",
        "image_url": "assets/images/bhavai_gujarat_bhungal.jpg",
        "alt_text": "Vibrant Bhavai folk theatre artists performing with traditional costumes, musical pipe Bhungal, and expressive comedic masks."
    })

    blocks.append({
        "type": "theory",
        "content": "**Dramatic Art `(નાટ્યકલા)` and Gujarat's Bhavai `(ભવાઈ)`:**\n\n1. **Indian Dramatic Heritage `(નાટ્યકલા / नाट्य कला)`:**\n   - Amalgamation of audio, visual, literature, music, and performance. Its primary goal is entertainment with moral instruction.\n   - **First Sanskrit Play:** Bharat Muni authored the play **'Devasur Sangram' `(દેવાસુર સંગ્રામ)`**.\n   - **Great Classical Playwrights:**\n     - **Mahakavi Bhasa `(મહાકવિ ભાસ)`:** Wrote 13 legendary plays (*Bhasa Natak Chakram*) including *Karnabhar*, *Urubhanga*, and *Dutavakyam* based on the Mahabharata.\n     - **Mahakavi Kalidasa `(મહાકવિ કાલિદાસ)`:** World's greatest Sanskrit dramatist, authored *Abhijnana Shakuntalam* `(અભિજ્ઞાન શાકુન્તલમ્)`, *Malavikagnimitram*, and *Vikramorvashiyam*.\n\n2. **Bhavai of Gujarat `(ગુજરાતની ભવાઈ / भवाई)`:**\n   - **Origins:** A **700-year-old** unique folk drama tradition initiated by **Asait Thakar `(અસાત ઠાકર / असैत ठाकर)`** during the Solanki era.\n   - **Musical Instrument:** Performed in open grounds accompanied by the signature wind horn pipe called **Bhungal `(ભૂંગળ / भूंगल)`**.\n   - **Social Education:** Famous themes (Veshas) include *Ramdevpir no Vesha*, *Jhanda Jhoolan no Vesha*, and *Kajoda no Vesha*. Modern Bhavai promotes girl child education (*Kanya Kelavani / Beti Bachao*) through iconic humorous characters **Rangla and Rangli `(રંગલો અને રંગલી)`**.",
        "difficulty": "Advanced",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "mcq",
        "content": "Who was the founder of Gujarat's 700-year-old emotion-oriented theatrical folk art known as Bhavai?",
        "options": [
            "Poet Dayaram `(કવિ દયારામ / कवि दयाराम)`",
            "Asait Thakar `(અસાત ઠાકર / असैत ठाकर)`",
            "Narsinh Mehta `(નરસિંહ મહેતા / नरसिंह मेहता)`",
            "Pandit Sarangdev `(પંડિત સારંગદેવ / पंडित सारंगदेव)`"
        ],
        "correct_answer": "Asait Thakar `(અસાત ઠાકર / असैत ठाकर)`",
        "explanation": "Asait Thakar founded the 700-year-old Gujarati folk theatre form called Bhavai during the 14th century.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    # =========================================================================
    # MODULE 12: FOLK & TRIBAL DANCES OF GUJARAT (ગુજરાતના લોકનૃત્યો)
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "When autumn breezes arrive, millions of people across Gujarat swirl under midnight skies in rhythmic circles. But Gujarat's dance heritage goes far beyond Garba—from the African-origin **Dhamaal dance** of Gir's Siddhis to the wave-like **Padhar dance** of Nalkantha! Let's explore Gujarat's vibrant folk rhythms.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "diagram",
        "content": "Folk & Tribal Dance Map of Gujarat: Garba, Dhamaal of Jambur, Padhar of Surendranagar, and Chharo of Dangs.",
        "image_url": "assets/images/gujarat_folk_dances_map.jpg",
        "alt_text": "Cultural map of Gujarat depicting regions of Garba, Siddhi Dhamaal dance with Mashira, Padhar dance, and Dangi Chharo."
    })

    blocks.append({
        "type": "theory",
        "content": "**Folk and Tribal Dances of Gujarat `(ગુજરાતના લોકનૃત્યો અને આદિવાસી નૃત્યો)`:**\n\n1. **Garba `(ગરબા)`:**\n   - Derived from the Sanskrit root **'Garbhadip' `(ગર્ભદીપ)`** — an earthen pot with perforations (holes) containing an illuminated ghee/oil lamp inside.\n   - Women balance the pot on their heads or place it in the center, singing hymns dedicated to Mother Goddess **Adyashakti `(આદ્યશક્તિ / અંબાજી)`** during the 9 nights of **Navratri `(નવરાત્રી)`** (Ashwin Sud 1 to Ashwin Sud 9/10).\n\n2. **Garbi `(ગરબી)`:**\n   - Devotional dancing and singing predominantly performed by men, associated with **Lord Krishna Bhakti `(કૃષ્ણ ભક્તિ)`**, popularized by Gujarat's famous poet **Dayaram `(દયારામ)`**.\n\n3. **Ras `(રાસ / દાંડિયા રાસ)`:**\n   - Performed in circular formations with sticks (Dandiya). Saint Narsinh Mehta witnessed Lord Krishna's divine Rasleela in Junagadh.\n\n4. **Tribal & Specialized Regional Folk Dances:**\n   - **Dhamaal Dance of Siddhis `(સિદ્દીઓનું ધમાલ નૃત્ય)`:** Practiced by the Siddhi community residing in **Jambur village `(જાંબુર ગામ)`** in the heart of Gir forest (originally from Africa). They dance holding **Mashira `(મશીરા)`**—a coconut shell filled with cowries, covered with green cloth and peacock feathers—striking rhythmic beats and uttering high-pitched shouts of *'Ho... Ho...'* imitating wild animal sounds in dense forests.\n   - **Padhar Dance `(પઢાર નૃત્ય)`:** Performed by the Padhar community around the **Nalkantha `(નળકાંઠા)`** region in Surendranagar district. Dancers sit and rise in synchrony holding Dandiya and Manjira, mimicking the ebb and flow of **sea waves `(સાગરના મોજાં)`** and rowers rowing a boat `(નાવ ચલાવવી)`.\n   - **Dangs Chharo Dance `(ડાંગનો ચાળો)`:** Performed in the forested Dangs district. Tribal dancers imitate the sounds and movements of birds and animals like peacocks, sparrows, and deer in dances like *Mali no Chhalo* and *Thakrya Chhalo*.\n   - **Koli and Mer Dances of Saurashtra `(કોળી અને મેર નૃત્ય)`:** Dancers wear embroidered head-turbans (*Madhasio*), mirror-work jackets, and colorful waist-belts (*Bhet*).",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM FAVORITE (3 Marks):** Write a short note on the **'Dhamaal Dance of Siddhis'**.\n\n**Topper's Key Points:**\n1. **Community & Origin:** Siddhis of Jambur village in Gir forest (African ancestry).\n2. **Prop:** *Mashira* `(મશીરા)` (coconut shell filled with cowries, peacock feathers).\n3. **Style & Rhythm:** Fast tempo, rhythmic shaking of Mashira, shouts of *'Ho... Ho...'*, animal sound imitations.",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    blocks.append({
        "type": "mcq",
        "content": "Which traditional dance performed around Nalkantha (Surendranagar) mimics the motion of sea waves and rowing boats?",
        "options": [
            "Dhamaal Dance `(ધમાલ નૃત્ય / धमाल नृत्य)`",
            "Padhar Dance `(પઢાર નૃત્ય / प Contemporaryार नृत्य)`",
            "Chharo Dance `(ચાળો નૃત્ય / चालो नृत्य)`",
            "Garba `(ગરબા / गरबा)`"
        ],
        "correct_answer": "Padhar Dance `(પઢાર નૃત્ય / प Contemporaryार नृत्य)`",
        "explanation": "The Padhar dance of Nalkantha features dancers holding Manjira and sitting/rising in rhythm like ocean waves and boat rowers.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    # =========================================================================
    # MODULE 13: SUMMARY & BOARD EXAM HIGH-YIELD REVIEW
    # =========================================================================
    blocks.append({
        "type": "summary",
        "content": "🎯 **Chapter 2 Master Review (Board Exam Quick Recall):**\n- **3 Heritages:** Biological (Genetics) | Material (Inherited property) | Cultural (Intellectual & artistic creations).\n- **Clay Work:** Laghnaj (Mehsana) & Nagarjuna Konda (South India) terracotta sites.\n- **Textile Masterpieces:** Dhaka Muslin (ring test) | Patan Patola (Solanki era, Double Ikat, reversible) | Bandhani (Jamnagar, Jetpur, Bhuj, Mandvi).\n- **Emroidery & Leather:** Mutwa community of Banni (Kutch) | Leather Mashak, Kos, Dholak, and Mojdi.\n- **Gem & Metal Crafts:** Meenakari (Jaipur/Delhi, Lucknow, Varanasi, Hyderabad) | Surat Jari & Zardosi | Sankheda lacquered furniture | Bikaner Jadtar | Khambhat Akik.\n- **Music Treatises:** Sangeet Makarand (Narad - 19 veenas, 101 taals) | Sangeet Ratnakar (Sarangdev - Soul of music) | Sangeet Parijat (Ahobale - 29 swaras).\n- **5 Classical Dances:** Bharatanatyam (Tamil Nadu) | Kuchipudi (Andhra Pradesh) | Kathakali (Kerala) | Kathak (North India) | Manipuri (Manipur - Kumin skirt).\n- **Theatre & Folk Dance:** Bhavai (Asait Thakar, 700 years, Bhungal horn) | Garba (Garbhadip) | Siddhi Dhamaal (Mashira, Jambur) | Padhar (Nalkantha waves).",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "board_questions",
        "content": "📋 **GSEB Board Exam Question Bank (PYQs & Model Questions):**\n\n**2-Mark Questions:**\n1. Explain the difference between Biological Heritage and Material Heritage with examples.\n2. Why is Samaveda called the 'Gangotri of Indian Music'?\n3. Describe the specialty of Patan's Patola weaving.\n4. Name the five ragas born from the five faces of Lord Shiva.\n\n**3-Mark Questions:**\n5. Write a short note on the ancient Art of Clay Work in India.\n6. Describe the Dhamaal Dance of Siddhis and Padhar Dance of Surendranagar.\n7. Compare Sangeet Makarand, Sangeet Ratnakar, and Sangeet Parijat.\n\n**4-Mark Long Answer Questions:**\n8. Give a comprehensive description of the 5 Classical Dance Forms of India with their origins, texts, and famous exponents.\n9. Explain the various traditional handicrafts of Gujarat (Textiles, Beadwork, Jari, Wood, and Akik).",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    # Path 1: Output to GSEB Chapter location
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_social_science_ch2.json"
    with open(gseb_path, "w", encoding="utf-8") as f:
        json.dump(final_json, f, indent=2, ensure_ascii=False)
    print(f"Generated GSEB Chapter 2 at: {gseb_path}")
        
    # Path 2: Output to NCERT Chapter location
    ncert_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_social_science_ch2.json"
    final_json_ncert = json.loads(json.dumps(final_json))
    final_json_ncert["metadata"]["id"] = "ncert_class10_social_science_ch2"
    with open(ncert_path, "w", encoding="utf-8") as f:
        json.dump(final_json_ncert, f, indent=2, ensure_ascii=False)
    print(f"Generated NCERT Chapter 2 at: {ncert_path}")
    
    # Also write ncert_class10_social_science_ch2.json in current directory if specified
    local_ncert_path = "ncert_class10_social_science_ch2.json"
    with open(local_ncert_path, "w", encoding="utf-8") as f:
        json.dump(final_json_ncert, f, indent=2, ensure_ascii=False)
    print(f"Generated local NCERT Chapter 2 at: {local_ncert_path}")

if __name__ == "__main__":
    generate_supreme_gseb_ss_ch2()
