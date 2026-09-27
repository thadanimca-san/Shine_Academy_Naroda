import json
import os

def generate_supreme_gseb_ss_ch7():
    chapter_id = "gseb_class10_social_science_ch7"
    title = "Chapter 7: Preservation of Our Heritage"
    
    metadata = {
        "id": chapter_id,
        "title": title,
        "subtitle": "The Supreme Board Exam Mastery & Heritage Conservation Guide",
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
            "class10",
            "heritage_preservation",
            "gseb",
            "ncert",
            "asi",
            "unesco",
            "monuments",
            "fundamental_duties",
            "article_51a",
            "museums_of_gujarat",
            "board_special",
            "bilingual"
        ],
        "learning_outcomes": [
            "Understand why preserving cultural and natural heritage is indispensable for national identity, ecology, and global pride.",
            "Analyze the socio-economic impacts of the tourism industry and India's heritage preservation ecosystem.",
            "Identify major natural and human-induced threats causing deterioration and damage to ancient monuments.",
            "Master key Constitutional provisions (Article 51A(f), 51A(g), Article 49) governing heritage protection.",
            "Evaluate key heritage laws including AMASR Act 1958 (prohibited and regulated buffer zones) and the role of ASI.",
            "Memorize the premier museums of India and Gujarat (Calico, L.D. Institute, B.J. Institute, Mahavir Jain Aradhana Kendra).",
            "Examine scientific conservation case studies: Taj Mahal (Fuller's earth), Sun Temple Konark (sand filling), and Rani ki Vav.",
            "Formulate model, high-scoring answers for 1-mark, 2-mark, 3-mark, and 4-mark Board Examination questions."
        ],
        "ai_context": {
            "learning_goal": "Transform the student from a memorizer into a critical thinker and high-scoring board scholar in Heritage Preservation. Use the 8-Step Socratic Learning Cycle, rich visual analogies, memory tricks, case studies, and bilingual terminology for smart filtering.",
            "common_misconceptions": [
                "Students confuse Article 51A(f) (Composite Cultural Heritage) with Article 51A(g) (Natural Environment & Wildlife).",
                "Students confuse the 100m Prohibited Area with the 200m Regulated Area under the AMASR Act 1958.",
                "Students mistakenly assume ASI was founded post-independence (Fact: ASI was founded in 1861 by Sir Alexander Cunningham).",
                "Students confuse the locations and specialties of famous Gujarat museums (e.g. Calico vs L.D. Institute vs Mahavir Jain Aradhana Kendra Koba)."
            ],
            "tutor_hint": "If a student struggles with constitutional articles, use the mnemonic 'F for Fine Cultural Heritage (51A-f)' and 'G for Green Forests & Wildlife (51A-g)'. For laws, emphasize the 100m Prohibited vs 200m Regulated zone boundary rules."
        }
    }
    
    blocks = []
    
    # =========================================================================
    # MODULE 1: WHY MUST WE PRESERVE OUR HERITAGE? (IMPORTANCE & SIGNIFICANCE)
    # =========================================================================
    blocks.append({
        "type": "hook",
        "title": "The Whispering Stones: Why Does Our Past Matter?",
        "content": "Imagine standing before the towering grandeur of the **Taj Mahal `(ताजमहल / તાજમહેલ)`**, descending into the subterranean sculptural splendour of **Rani ki Vav `(रानी की वाव / રાણકી વાવ)`**, or touching the weathered bricks of a 4,500-year-old dockyard at **Lothal `(लोथल / લોથલ)`**.\n\nWhy do millions of travelers from every corner of the planet travel thousands of miles to gaze upon our ancient monuments? What makes centuries-old carved sandstone, delicate palm-leaf manuscripts, and sacred cave frescoes more valuable than all the gold in the world?\n\nOur heritage is not just dead stone; it is the living **identity `(पहचान / ઓળખ)`**, **glory `(गौरव / ગૌરવ)`**, and **cultural DNA `(सांस्कृतिक पहचान / સાંસ્કૃતિક ઓળખ)`** of our civilization. Welcome to **Preservation of Our Heritage `(विरासत का संरक्षण / આપણા વારસાનું જતન)`**!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "title": "Classification: Cultural vs Natural Heritage",
        "content": "India's heritage is bifurcated into two mutually reinforcing pillars: Cultural Heritage (man-made marvels, literature, arts) and Natural Heritage (biodiversity, rivers, landscapes).",
        "image_url": "assets/images/gseb_ss_ch7_heritage_types.jpg",
        "alt_text": "Mindmap showing Cultural Heritage (Monuments, Sculptures, Inscriptions, Traditions) and Natural Heritage (Mountains, Rivers, Wildlife, Flora and Fauna)."
    })
    
    blocks.append({
        "type": "theory",
        "title": "Crucial Need and Significance of Preserving Our Heritage",
        "content": "Heritage is an invaluable **national asset `(राष्ट्रीय संपत्ति / રાષ્ટ્રીય સંપત્તિ)`**. Its preservation is vital due to the following core reasons:\n\n1. **National Identity and Global Pride `(राष्ट्रीय पहचान और वैश्विक गौरव / રાષ્ટ્રીય ઓળખ અને વૈશ્વિક ગૌરવ)`:**\n   - Heritage reflects our glorious history, unmatched architectural brilliance, and philosophical wisdom.\n   - It creates an inspiring bridge between our illustrious ancestors and future generations.\n\n2. **Guide for the Future `(भविष्य का मार्गदर्शक / ભવિષ્યનો માર્ગદર્શક)`:**\n   - Heritage acts as an eternal compass. By understanding our ancestors' achievements, town planning, and sustainable lifestyles, modern society can avoid historical blunders and build a resilient future.\n\n3. **Preservation of Ecological Balance `(पारिस्थितिक संतुलन का संरक्षण / પારિસ્થિતિક સંતુલનની જાળવણી)`:**\n   - Natural heritage—including pristine forests `(प्राकृतिक वन / કુદરતી જંગલો)`, wildlife sanctuaries, and sacred rivers—preserves environmental equilibrium and safeguards biodiversity from irreversible extinction.\n\n4. **Symbol of Unity in Diversity `(विविधता में एकता का प्रतीक / વિવિધતામાં એકતાનું પ્રતીક)`:**\n   - India's composite culture `(सामासिक संस्कृति / સમન્વિત સંસ્કૃતિ)` represents the harmonious assimilation of diverse religions, architectural styles, languages, and philosophies across millennia.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "Why is cultural heritage considered an indispensable guide for future generations?",
            "options": [
                "It serves as a blueprint of architectural, social, and cultural evolution that fosters national pride and sustainable progress",
                "It helps the country sell antique sculptures to international private collectors",
                "It replaces modern industrial technology with primitive hand tools",
                "It eliminates the need for environmental protection laws"
            ],
            "correct_answer": "It serves as a blueprint of architectural, social, and cultural evolution that fosters national pride and sustainable progress",
            "explanation": "Heritage is our historical compass: it demonstrates human ingenuity, cultural continuity, and socio-environmental harmony, guiding modern society towards sustainable development."
        },
        "difficulty": "Intermediate",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Teacher's Master Insight:** When writing a Board Exam answer for *'Need for Preservation of Heritage'*, always structure your points into four clear dimensions: **(1) Cultural & Historical Identity**, **(2) Economic Growth via Tourism**, **(3) Ecological Balance**, and **(4) Inspiration for Future Generations**. This ensures full marks from the examiner!"
    })

    # =========================================================================
    # MODULE 2: TOURISM INDUSTRY AND OUR HERITAGE
    # =========================================================================
    blocks.append({
        "type": "hook",
        "title": "Economic Catalyst: How Monuments Drive Prosperity",
        "content": "Did you know that heritage tourism is one of India's biggest engines for earning **foreign exchange `(विदेशी मुद्रा / વિદેશી હૂંડિયામણ)`** and creating millions of local jobs?\n\nWhen a foreign traveler visits the Sun Temple of Modhera or the Ajanta Caves, who benefits? Not just the ticket counter! The airline, hotel, local auto driver, heritage guide, tea vendor, and local handicraft artisan all earn their livelihood. How does cultural preservation translate directly into national economic power?",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "title": "The Economic Ripple Effect of Heritage Tourism",
        "content": "Tourists visit Heritage Monuments ➔ Boost Hospitality & Transportation ➔ Flourish Local Handicrafts & Folk Arts ➔ Generate Massive Employment ➔ Foreign Exchange Enriches National Economy.",
        "image_url": "assets/images/gseb_ss_ch7_tourism_economy.jpg",
        "alt_text": "Flowchart illustrating the economic cycle of heritage tourism from travelers to local artisans and national GDP."
    })
    
    blocks.append({
        "type": "theory",
        "title": "Tourism Industry and Heritage: Synergistic Growth",
        "content": "India's rich cultural and natural heritage has positioned the country as a world-class tourism hotspot `(पर्यटन केंद्र / પ્રવાસન કેન્દ્ર)`.\n\n**Key Economic and Cultural Benefits of Tourism:**\n1. **Foreign Exchange Inflow `(विदेशी मुद्रा का आगमन / વિદેશી હૂંડિયામણની આવક)`:**\n   - International tourists spend extensively on lodging, travel, cultural exhibitions, and souvenirs, significantly bolstering foreign exchange reserves.\n2. **Generation of Massive Employment `(विशाल रोजगार सृजन / વિશાળ રોજગારીનું સર્જન)`:**\n   - Tourism is labor-intensive. It generates direct and indirect employment for tourist guides `(पर्यटन गाइड / ટૂરિસ્ટ ગાઇડ)`, hospitality personnel, transport operators, and souvenir manufacturers.\n3. **Revival of Local Crafts and Performing Arts `(स्थानीय हस्तशिल्प और लोककलाओं का पुनरुद्धार / સ્થાનિક હસ્તકલા અને લોકકળાઓનું પુનરુત્થાન)`:**\n   - High demand from tourists breathes new economic life into dying traditional handicrafts, regional embroidery (like Patola of Patan, Bandhani of Kutch), and folk performances.\n4. **Infrastructure Development `(बुनियादी ढांचे का विकास / પાયાની સુવિધાઓનો વિકાસ)`:**\n   - To accommodate tourists, governments build highways, airports, sanitation systems, eco-resorts, and modern digital connectivity around historical hubs.\n5. **India's Cultural Ambassador: 'Atithi Devo Bhava' `(अतिथि देवो भव / અતિથિ દેવો ભવ)`:**\n   - India showcases its timeless ethos of hospitality, spreading global awareness, brotherhood, and appreciation for Indian culture worldwide.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "Which traditional Indian craft of Gujarat receives major economic revival directly through heritage tourism?",
            "options": [
                "Patola weaving of Patan and Bandhani of Kutch",
                "Synthetic nylon manufacturing",
                "Machine-made plastic pottery",
                "Automobile engine casting"
            ],
            "correct_answer": "Patola weaving of Patan and Bandhani of Kutch",
            "explanation": "Heritage tourism directly boosts authentic regional handicrafts such as Patan's world-famous double-ikkat Patola and Kutch's vibrant Bandhani and Rogan art."
        },
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Memory Trick (The 4E Model of Tourism):** Remember the fourfold impact of heritage tourism:\n- **E**arning foreign exchange `(विदेशी मुद्रा / વિદેશી હૂંડિયામણ)`\n- **E**mployment for locals `(स्थानीय रोजगार / સ્થાનિક રોજગારી)`\n- **E**mpowerment of traditional artisans `(हस्तशिल्प पुनरुद्धार / હસ્તકલા પુનરુત્થાન)`\n- **E**xcellence in global reputation `(वैश्विक साख / વૈશ્વિક પ્રતિષ્ઠા)`"
    })

    # =========================================================================
    # MODULE 3: THREATS, DETERIORATION & DAMAGE TO HERITAGE
    # =========================================================================
    blocks.append({
        "type": "hook",
        "title": "Monuments in Peril: The Tragic Scars of Neglect",
        "content": "Look closely at the walls of an ancient stepwell or a centuries-old fort. You will often see modern names crudely scratched onto ancient frescoes, paan stains on intricately carved jali work, and plastic wrappers scattered in temple courtyards.\n\nEven worse, historical stone figures have been hacked off by illegal smugglers, and industrial smog turns pristine white marble yellow! How are human carelessness and natural weathering destroying our priceless legacy?",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "title": "Dual Threats to Cultural Heritage: Man vs Nature",
        "content": "Heritage monuments face severe degradation caused by two contrasting forces: Human Vandalism & Pollution versus Natural Elements & Biological Overgrowth.",
        "image_url": "assets/images/gseb_ss_ch7_threats_diagram.jpg",
        "alt_text": "Diagram categorizing threats into Human Factors (Vandalism, Scribbling, Pollution, Smuggling) and Natural Factors (Acid Rain, Weathering, Earthquakes, Roots of Vegetation)."
    })
    
    blocks.append({
        "type": "theory",
        "title": "Detailed Analysis of Threats to Heritage",
        "content": "The deterioration of our cultural and natural heritage occurs due to two major categories of hazards:\n\n### A. Human-Induced Damages `(मानव-जनित नुकसान / માનવસર્જિત નુકસાન)`:\n1. **Vandalism and Defacement `(तोड़फोड़ और विरूपण / ભાંગફોડ અને વિકૃતિ)`:**\n   - Tourists and miscreants carving names, writing phone numbers, or scratching walls of historical forts, caves, and minarets.\n2. **Uncivic Habits and Pollution `(अस्वच्छता और प्रदूषण / અસ્વચ્છતા અને પ્રદૂષણ)`:**\n   - Spitting paan, tobacco, and gutkha on heritage premises; dumping single-use plastics, leftover food, and sewage into historic stepwells and riverbanks.\n3. **Industrial Pollution & Acid Rain `(औद्योगिक प्रदूषण और अम्लीय वर्षा / ઔદ્યોગિક પ્રદૂષણ અને એસિડ વર્ષા)`:**\n   - Toxic chemical fumes from nearby factories cause chemical weathering. For example, sulfur dioxide and nitrogen dioxide released from the **Mathura Oil Refinery `(मथुरा तेल रिफाइनरी / મથુરા ઓઇલ રિફાઇનરી)`** caused acid rain, turning the pristine white marble of the **Taj Mahal `(ताजमहल / તાજમહેલ)`** yellowish (*Stone Leprosy / Marble Cancer*).\n4. **Illegal Smuggling and Theft of Antiquities `(प्राचीन मूर्तियों की तस्करी और चोरी / પ્રાચીન મૂર્તિઓની તસ્કરી અને ચોરી)`:**\n   - Clandestine gangs break and steal antique stone idols, metallic bronzes, and prehistoric coins to sell in international black markets.\n5. **Unplanned Urban Encroachment `(अनियोजित शहरी अतिक्रमण / અનિયોજિત શહેરી દબાણ)`:**\n   - Construction of illegal commercial shops and concrete towers directly surrounding ancient monuments, destroying their aesthetic buffer.\n\n### B. Natural Damages `(प्राकृतिक आपदाएं और नुकसान / કુદરતી આપદાઓ અને નુકસાન)`:\n1. **Weathering and Climatic Extremes `(अपक्षय और जलवायु प्रभाव / અપક્ષય અને આબોહવાની અસરો)`:**\n   - Intense heat, torrential rains, frost, and salty sea winds cause scaling and cracking of rock surfaces (e.g. sea spray eroding the Sun Temple at Konark).\n2. **Natural Calamities `(प्राकृतिक आपदाएं / કુદરતી હોનારતો)`:**\n   - Severe earthquakes `(भूकंप / ધરતીકંપ)`, floods, cyclones, and tsunamis can instantly topple ancient domes, pillars, and stepwells.\n3. **Vegetation and Root Penetration `(वनस्पति और जड़ों का फैलाव / વનસ્પતિ અને મૂળનું વિસ્તરણ)`:**\n   - Seeds of Banyan `(बरगद / વડ)` and Peepal `(पीपल / પીપળો)` trees germinate inside stone crevices. As roots thicken, they split stone blocks apart, causing structural collapse.",
        "difficulty": "Intermediate",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "exam_tips",
        "title": "🔥 Board Exam Hot Topic: The Taj Mahal Case Study",
        "content": "⚠️ **Frequent 2-Mark Board Question:** *Why did the white marble of the Taj Mahal turn pale/yellow, and what was the remedial action taken?*\n\n**Model Answer:**\n1. **Cause:** Air pollutants (Sulphur dioxide & Nitrogen oxides) emitted by the nearby **Mathura Oil Refinery** and foundries reacted with atmospheric moisture to form acid rain, corroding and yellowing the white marble.\n2. **Remedial Action:** The Government established the **Taj Trapezium Zone (TTZ)**, ordered industries to switch from coal to clean Natural Gas (CNG/PNG), banned diesel vehicles within a 500m perimeter, and applied chemical mud packs (**Fuller's Earth / मुल्तानी मिट्टी**) to absorb surface grime."
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "Which environmental phenomenon caused by Mathura Oil Refinery emissions affected the Taj Mahal's marble?",
            "options": [
                "Acid rain caused by sulphur dioxide reacting with atmospheric moisture",
                "Depletion of ground water beneath the Yamuna basin",
                "Tectonic plate subduction under the Indo-Gangetic plain",
                "Excessive accumulation of Himalayan glacial frost"
            ],
            "correct_answer": "Acid rain caused by sulphur dioxide reacting with atmospheric moisture",
            "explanation": "Sulfur dioxide emissions combined with atmospheric moisture to form sulfuric acid rain, chemically degrading marble (calcium carbonate) into calcium sulfate, turning it pale yellowish."
        },
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    # =========================================================================
    # MODULE 4: CONSTITUTIONAL PROVISIONS & FUNDAMENTAL DUTIES
    # =========================================================================
    blocks.append({
        "type": "hook",
        "title": "The Supreme Law of the Land: Heritage as a Constitutional Duty",
        "content": "Is preserving a historical temple, a stepwell, or a lush wildlife sanctuary merely an act of kindness, or is it our **sacred legal and constitutional obligation `(संवैधानिक दायित्व / બંધારણીય ફરજ)`**?\n\nThe visionary framers of our Indian Constitution realized that laws alone cannot save a nation's soul unless every single citizen feels personally responsible. Let us explore the constitutional articles dedicated to preserving our heritage!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "title": "Constitutional Trinity for Heritage Preservation",
        "content": "Article 51A(f) [Cultural Heritage Duty] + Article 51A(g) [Natural Environment Duty] + Article 49 [State Obligation for Monuments].",
        "image_url": "assets/images/gseb_ss_ch7_constitution_articles.jpg",
        "alt_text": "Diagram showing Article 51A(f), Article 51A(g), and Article 49 of the Constitution of India."
    })
    
    blocks.append({
        "type": "theory",
        "title": "Constitutional Provisions for Heritage Protection",
        "content": "The Constitution of India explicitly mandates the protection of cultural and natural heritage through both **Fundamental Duties `(मौलिक कर्तव्य / મૂળભૂત ફરજો)`** and **Directive Principles of State Policy `(राज्य के नीति निर्देशक तत्व / રાજ્યના નીતિનિર્દેશક સિદ્ધાંતો)`**:\n\n### 1. Fundamental Duties of Citizens (Article 51-A, Part IV-A):\n- **Article 51A(f) `(अनुच्छेद 51A(च) / કલમ 51A(છ))`:**\n  - *\"It shall be the duty of every citizen of India to value and preserve the rich heritage of our composite culture `(सामासिक संस्कृति की गौरवशाली परंपरा का महत्व समझना और उसका परिरक्षण करना / આપણી સમન્વિત સંસ્કૃતિના સમૃદ્ધ વારસાનું મૂલ્ય સમજી તેનું જતન કરવું)`.\"*\n- **Article 51A(g) `(अनुच्छेद 51A(छ) / કલમ 51A(જ))`:**\n  - *\"To protect and improve the natural environment including forests, lakes, rivers, and wildlife, and to have compassion for living creatures `(प्राकृतिक पर्यावरण की रक्षा करना और सभी जीवों के प्रति दयाभाव रखना / જંગલો, તળાવો, નદીઓ અને વન્યજીવો સહિત કુદરતી પર્યાવરણનું રક્ષણ કરવું અને જીવો પ્રત્યે અનુકંપા રાખવી)`.\"*\n- **Article 51A(h):**\n  - To develop the scientific temper, humanism, and the spirit of inquiry and reform.\n\n### 2. Directive Principles of State Policy (Article 49):\n- **Article 49 `(अनुच्छेद 49 / કલમ 49)`:**\n  - Imposes an unambiguous obligation upon the State to protect every monument, place, or object of artistic or historic interest (declared by or under law made by Parliament to be of national importance) from spoliation, disfigurement, destruction, removal, disposal, or export.",
        "difficulty": "Advanced",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "Which sub-clause of Article 51A specifically mandates citizens 'to value and preserve the rich heritage of our composite culture'?",
            "options": [
                "Article 51A(f)",
                "Article 51A(g)",
                "Article 51A(a)",
                "Article 51A(k)"
            ],
            "correct_answer": "Article 51A(f)",
            "explanation": "Article 51A(f) mandates the preservation of composite cultural heritage, whereas Article 51A(g) deals with natural environmental protection (forests, lakes, rivers, and wildlife)."
        },
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Unbeatable Mnemonic for Board Exams:**\n- **'F' in 51A(f)** stands for **'Fine Composite Heritage'** `(सामासिक संस्कृति / સમન્વિત સંસ્કૃતિ)`.\n- **'G' in 51A(g)** stands for **'Green Nature & Wildlife'** `(हरा-भरा पर्यावरण / લીલુંછમ પર્યાવરણ)`.\n- **Article 49** = **'State's Shield for Monuments'** `(स्मारकों का राज्य संरक्षण / સ્મારકોનું રાજ્ય રક્ષણ)`.\nNever mix up (f) and (g) in your multiple-choice questions!"
    })

    # =========================================================================
    # MODULE 5: KEY HERITAGE ACTS & ARCHAEOLOGICAL SURVEY OF INDIA (ASI)
    # =========================================================================
    blocks.append({
        "type": "hook",
        "title": "Guardians of History: How the Law Protects Monuments",
        "content": "Can anyone construct a 10-storey apartment complex right next to the Sun Temple of Modhera or Qutub Minar? Absolutely NOT! The law strictly forbids unauthorized construction around our national treasures.\n\nWho creates these strict boundaries? What is the **Archaeological Survey of India (ASI) `(भारतीय पुरातत्व सर्वेक्षण / ભારતીય પુરાતત્વ સર્વેક્ષણ)`** and how does it protect over 3,600 historical monuments across India?",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "title": "Buffer Zones under AMASR Act 1958",
        "content": "Monument Core ➔ 0 to 100 meters: Prohibited Area (Zero Construction) ➔ 100 to 300 meters: Regulated Area (Special Permit Required).",
        "image_url": "assets/images/gseb_ss_ch7_amasr_buffer_zones.jpg",
        "alt_text": "Diagram showing concentric safety circles around a protected heritage monument: 100m Prohibited Zone and outer 200m Regulated Zone."
    })
    
    blocks.append({
        "type": "theory",
        "title": "Key Legal Frameworks and the Role of ASI",
        "content": "To safeguard historical treasures from encroachment, vandalism, and smuggling, the Government of India enacted major landmark laws:\n\n### 1. The Ancient Monuments and Archaeological Sites and Remains (AMASR) Act, 1958:\n- Enacted in **1958** to preserve ancient monuments, sculptures, rock inscriptions, and archaeological sites.\n- **Two-Tier Protection Zones:**\n  - **Prohibited Area `(निषिद्ध क्षेत्र / પ્રતિબંધિત વિસ્તાર)`:** An area of **100 meters** around any protected monument in all directions is strictly prohibited for any type of private construction or mining activity.\n  - **Regulated Area `(विनियमित क्षेत्र / નિયમનકારી વિસ્તાર)`:** An extended zone of **200 meters beyond the prohibited area** (i.e. up to 300m from monument perimeter) where construction/repair is tightly regulated and requires prior approval from statutory authorities (**National Monuments Authority - NMA**).\n\n### 2. The Antiquities and Art Treasures Act, 1972:\n- Regulates domestic trade and completely bans the illegal export of antiquities `(पुरावशेष / પુરાવશેષો)`.\n- Any manuscript, coin, painting, or sculpture older than **100 years** (and manuscripts older than 75 years) is classified as an antiquity and must be registered with the government.\n\n### 3. Role of Archaeological Survey of India (ASI):\n- Established in **1861** by **Sir Alexander Cunningham `(सर अलेक्जेंडर कनिंघम)`** (the first Director-General, regarded as the Father of Indian Archaeology).\n- ASI is under the **Ministry of Culture, Government of India**.\n- Protects over **3,690+ monuments and sites of national importance**.\n- Conducts archaeological excavations, chemical cleaning `(रासायनिक उपचार / રાસાયણિક ઉપચાર)`, structural consolidation, and scientific restoration of crumbling edifices.",
        "difficulty": "Advanced",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "Under the AMASR Act 1958, what is the exact radius of the 'Prohibited Area' surrounding a protected monument where all construction is banned?",
            "options": [
                "100 meters",
                "200 meters",
                "500 meters",
                "50 meters"
            ],
            "correct_answer": "100 meters",
            "explanation": "Under the AMASR Act 1958, an area extending 100 meters in all directions from the protected monument is strictly designated as a Prohibited Area where no new construction is allowed."
        },
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Common Mistake Alert:** Do not confuse the founding year of **ASI (1861)** with the **AMASR Act (1958)** or the **Antiquities Act (1972)**. In board exams, match-the-following questions frequently test these exact years!"
    })

    # =========================================================================
    # MODULE 6: ROLE OF MUSEUMS & KEY INSTITUTIONS OF GUJARAT & INDIA
    # =========================================================================
    blocks.append({
        "type": "hook",
        "title": "Time Machines on Earth: The Treasuries of Our Heritage",
        "content": "Where can you see 4,000-year-old terracotta dancing figures, rare golden Mughal coins, original palm-leaf handwritten Jain scriptures, and the royal robes of emperors?\n\nMuseums `(संग्रहालय / સંગ્રહાલયો)` are living vaults of human civilization! Let us explore the world-famous museums of India and the crown jewel cultural storehouses right here in **Gujarat**!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "title": "Premier Heritage Museums: India & Gujarat Map",
        "content": "Key National Museums (New Delhi, Kolkata, Mumbai, Hyderabad) and Gujarat's Specialized Heritage Institutes (Ahmedabad, Gandhinagar, Vadodara).",
        "image_url": "assets/images/gseb_ss_ch7_museums_map.jpg",
        "alt_text": "Map showing National Museum New Delhi, Indian Museum Kolkata, Salar Jung Museum Hyderabad, and Gujarat institutes: Calico, L.D. Indology, B.J. Institute, Mahavir Jain Koba."
    })
    
    blocks.append({
        "type": "theory",
        "title": "Premier Museums of India and Gujarat",
        "content": "Museums preserve fragile antiquities under temperature-controlled, secure scientific environments:\n\n### A. World-Renowned National Museums of India:\n1. **National Museum `(राष्ट्रीय संग्रहालय / રાષ્ટ્રીય સંગ્રહાલય)`** — New Delhi.\n2. **Indian Museum `(भारतीय संग्रहालय / ભારતીય સંગ્રહાલય)`** — Kolkata (Oldest and largest museum in India, founded in 1814).\n3. **Chhatrapati Shivaji Maharaj Vastu Sangrahalaya `(छत्रपति शिवाजी महाराज वास्तु संग्रहालय)`** (formerly Prince of Wales Museum) — Mumbai.\n4. **Salar Jung Museum `(सालार जंग संग्रहालय / સાલારજંગ સંગ્રહાલય)`** — Hyderabad (Famous for one of the world's largest one-man collections of antiques).\n5. **Rashtriya Manav Sangrahalaya `(राष्ट्रीय मानव संग्रहालय)`** — Bhopal (Anthropological museum).\n\n### B. Celebrated Museums and Research Institutes of Gujarat `(गुजरात के प्रमुख संग्रहालय / ગુજરાતના જાણીતા સંગ્રહાલયો)`:\n1. **Calico Museum of Textiles `(कैलिको टेक्सटाइल म्यूजियम / કેલિકો ટેક્સટાઇલ મ્યુઝિયમ)`** — Ahmedabad:\n   - Renowned globally for an extraordinary collection of antique Indian textiles, handwoven tapestries, royal costumes, and wooden block prints.\n2. **L.D. Institute of Indology (Lalbhai Dalpatbhai) `(एल.डी. इंडोलॉजी / એલ.ડી. ઇન્સ્ટિટ્યૂટ ઓફ ઇન્ડોલોજી)`** — Ahmedabad:\n   - Houses over 75,000 rare palm-leaf `(ताड़पत्र / તાડપત્ર)` and paper manuscripts, stone sculptures, miniature paintings, and Jain bronzes.\n3. **B.J. Institute of Learning and Research (Bholabhai Jesingbhai) `(बी.जे. विद्याभवन / બી.જે. વિદ્યાભવન)`** — Ahmedabad:\n   - Renowned center for Indological research, ancient Sanskrit, Gujarati, and Persian manuscripts, rare coins, and epigraphs.\n4. **Shri Mahavir Jain Aradhana Kendra `(श्री महावीर जैन आराधना केंद्र)`** — Koba, Gandhinagar:\n   - Massive repository preserving hundreds of thousands of invaluable ancient Jain manuscripts, religious treatises, and philosophical literature.\n5. **Baroda Museum & Picture Gallery `(बड़ौदा म्यूजियम / બરોડા મ્યુઝિયમ)`** — Vadodara:\n   - Displays rare European oil paintings, Asian art, Harappan artifacts, and Egyptian mummies.\n\n### C. INTACH (Indian National Trust for Art and Cultural Heritage):\n- Established in **1984** in New Delhi as an autonomous non-governmental organization (NGO).\n- Works actively with citizens, architects, and schools for the restoration of unprotected architectural structures, organizing heritage walks, and raising grassroots awareness.",
        "difficulty": "Advanced",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "Where is the world-renowned 'Calico Museum of Textiles' situated in Gujarat?",
            "options": [
                "Ahmedabad",
                "Surat",
                "Vadodara",
                "Rajkot"
            ],
            "correct_answer": "Ahmedabad",
            "explanation": "The Calico Museum of Textiles, globally famous for its antique hand-woven fabrics, tapestries, and royal garments, is located in Ahmedabad."
        },
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Board Exam Direct Match-The-Following Table:**\n- **Calico Museum:** Famous Indian Textiles (Ahmedabad)\n- **L.D. Institute of Indology:** Rare Manuscripts & Jain Bronzes (Ahmedabad)\n- **B.J. Institute of Learning & Research:** Ancient Manuscripts & Coins (Ahmedabad)\n- **Shri Mahavir Jain Aradhana Kendra:** Invaluable Jain Literature (Koba, Gandhinagar)\n- **Baroda Museum:** Picture Gallery & Royal Collections (Vadodara)\n- **Salar Jung Museum:** World-Famous Art Collections (Hyderabad)"
    })

    # =========================================================================
    # MODULE 7: SCIENTIFIC CONSERVATION CASE STUDIES IN INDIA
    # =========================================================================
    blocks.append({
        "type": "hook",
        "title": "Saving Marvels: Modern Science Rescues Ancient Wonders",
        "content": "How do conservation engineers stop sea waves from dissolving an ancient temple, extract decades of greasy soot from marble without scratching it, or rescue an underground stepwell buried in river silt for 700 years?\n\nConservation is an exquisite union of **archaeology, structural engineering, chemistry, and history `(पुरातत्व, रसायन और इंजीनियरिंग का संगम / પુરાતત્વ, રસાયણ અને ઇજનેરીનો સંગમ)`**! Let us investigate India's greatest conservation triumphs.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "title": "Major Scientific Conservation Projects in India",
        "content": "Fuller's Earth on Taj Mahal ➔ Sand Filling at Sun Temple Konark ➔ Desilting & Chemical Biocide at Rani ki Vav ➔ Climate Control at Ajanta Caves.",
        "image_url": "assets/images/gseb_ss_ch7_conservation_case_studies.jpg",
        "alt_text": "Infographic depicting four conservation projects: Taj Mahal mud pack, Konark sand filling, Rani ki Vav excavation, and Ajanta cave lighting."
    })
    
    blocks.append({
        "type": "theory",
        "title": "Master Case Studies in Scientific Heritage Conservation",
        "content": "India has pioneered several globally acclaimed conservation techniques:\n\n### 1. The Taj Mahal (Agra, Uttar Pradesh):\n- **Challenge:** Acid rain and oily soot from refineries caused yellowing of marble.\n- **Scientific Remedy:** Application of **Fuller's Earth (Multani Mitti) pack `(मुल्तानी मिट्टी का लेप / મુલતાની માટીનો લેપ)`**.\n  - The non-abrasive clay paste is applied to marble walls, left to dry, and gently washed with distilled water.\n  - The clay draws out embedded pollutants, sulfur deposits, and grease without harming the delicate marble surface.\n\n### 2. Sun Temple of Konark (Odisha):\n- **Challenge:** Salty maritime winds and structural weakness threatened to collapse the towering *Jagamohan* (assembly hall).\n- **Scientific Remedy:** The British and later ASI conservationists carefully filled the interior hollow chamber of the Jagamohan with **clean sand** in the early 20th century to provide solid internal structural counter-weight and prevent catastrophic roof collapse.\n\n### 3. Rani ki Vav (Patan, Gujarat):\n- **Challenge:** The 11th-century seven-storey stepwell was submerged and completely choked under deep layers of Saraswati River silt for over 700 years.\n- **Scientific Remedy:** ASI carried out monumental desilting excavations, safely retrieving and re-assembling hundreds of exquisitely carved Vishnu sculptures, and applied chemical biocidal washes to prevent moss, algae, and fungal deterioration.\n- **Reward:** In **2014**, Rani ki Vav was recognized as a **UNESCO World Heritage Site**.\n\n### 4. Ajanta and Ellora Caves (Maharashtra):\n- **Challenge:** Microorganisms, humidity, bat excreta, and visitors' breath deteriorated delicate mural paintings.\n- **Scientific Remedy:** Humidity sensors, strict visitor quotas, special anti-fungal chemical coatings, and heat-free optic fiber illumination were installed to preserve the glowing ancient organic vegetable dyes.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "What engineering method was implemented to prevent structural collapse of the Jagamohan at the Sun Temple of Konark?",
            "options": [
                "Filling the interior assembly hall with sand to provide internal structural support",
                "Demolishing the surrounding stone pillars",
                "Replacing sandstone blocks with reinforced concrete beams",
                "Flooding the sanctum with sea water"
            ],
            "correct_answer": "Filling the interior assembly hall with sand to provide internal structural support",
            "explanation": "Conservation engineers filled the hollow interior of the Sun Temple's Jagamohan with sand to prevent its massive stone superstructure from collapsing under its own weight."
        },
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Teacher's Secret:** When discussing scientific conservation in exams, mention terms like **'Fuller's Earth pack'**, **'Chemical biocides'**, **'Desilting'**, and **'Buffer zones'**. Using precise technical terminology immediately signals high academic mastery to the evaluator!"
    })

    # =========================================================================
    # MODULE 8: OUR SACRED ROLE AS RESPONSIBLE CITIZENS
    # =========================================================================
    blocks.append({
        "type": "hook",
        "title": "Every Citizen a Guardian: What Will You Leave Behind?",
        "content": "Our ancestors poured decades of devotion, artistic genius, and sweat into creating immortal marvels using nothing more than simple iron chisels and hammers.\n\nIf they could create such eternal splendor with ancient technology, is it not our sacred moral obligation to protect it with all our modern knowledge and love? What simple daily steps can every student take to become a true guardian of India's heritage?",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "title": "The Citizen's Code for Heritage Preservation",
        "content": "5 Golden Rules: (1) Zero Defacement ➔ (2) Zero Littering ➔ (3) Respect Antiquities ➔ (4) Report Vandalism ➔ (5) Spread Heritage Literacy.",
        "image_url": "assets/images/gseb_ss_ch7_citizen_role.jpg",
        "alt_text": "Illustration showing responsible tourists keeping monument grounds clean, avoiding scribbling on walls, and participating in heritage walks."
    })
    
    blocks.append({
        "type": "theory",
        "title": "Duties of Citizens Towards Preservation of Heritage",
        "content": "Every enlightened citizen and student must actively practice the following code of conduct:\n\n1. **Zero Vandalism and Defacement `(दीवारों पर कुरेदने या लिखने से बचना / દીવાલો પર લખાણ કે કોતરકામ ન કરવું)`:**\n   - Never write, scratch names, or paint graffiti on monuments, historical pillars, fort walls, or cave paintings.\n2. **Maintain Strict Cleanliness and Sanitation `(स्वच्छता बनाए रखना / સ્વચ્છતા જાળવવી)`:**\n   - Do not litter plastic bottles, wrappers, or food waste on heritage premises. Always dispose of garbage in designated recycling bins.\n3. **Prohibition of Spitting `(थूकने पर पूर्ण प्रतिबंध / થૂંકવા પર સંપૂર્ણ પ્રતિબંધ)`:**\n   - Strictly avoid chewing or spitting paan, gutkha, and tobacco, which permanently stain stone and lime plaster surfaces.\n4. **Prevent Theft, Smuggling, and Encroachment `(चोरी, तस्करी और अतिक्रमण को रोकना / ચોરી, તસ્કરી અને દબાણ અટકાવવું)`:**\n   - If any illegal digging, defacement, or idol theft is observed, immediately notify the local police, ASI officials, or village panchayat.\n5. **Promotion of Heritage Awareness in Schools `(विद्यालयों में विरासत जागरूकता / શાળાઓમાં વારસાની જાગૃતિ)`:**\n   - Educational institutions should organize Heritage Walks `(हेरिटेज वॉक / હેરિટેજ વૉક)`, historical quizzes, photography exhibitions, and adopt-a-monument cleanliness drives.\n6. **Eco-Friendly Tourism Practices `(पर्यावरण-अनुकूल पर्यटन / પર્યાવરણ-અનુકૂળ પ્રવાસન)`:**\n   - Use electric vehicles, bicycles, or walk around sensitive monument zones to reduce vehicular carbon emissions.",
        "difficulty": "Intermediate",
        "bloom": "Apply"
    })
    
    blocks.append({
        "type": "reflection",
        "title": "Socratic Reflection for Future Leaders",
        "content": "💭 *\"A nation that forgets its past has no future.\"* \n\nReflect on this: When you visit a monument, you are not a mere spectator; you are a temporary custodian holding a sacred heritage in trust for generations not yet born. Will you leave a scar on history, or will you help preserve its immortal glow?",
        "difficulty": "Beginner",
        "bloom": "Evaluate"
    })

    # =========================================================================
    # MODULE 9: BOARD EXAM MASTERY (PYQS, HOTS & MODEL ANSWERS)
    # =========================================================================
    blocks.append({
        "type": "exam_tips",
        "title": "🔥 Board Exam Mastery: High-Yield Question Bank",
        "content": "### 📌 Question 1 (4 Marks - High Priority): Explain the measures taken for the preservation and protection of our cultural and natural heritage.\n\n**Structured Board Model Answer:**\n1. **Constitutional Safeguards:** Under **Article 51A(f)** and **51A(g)**, valuing composite heritage and protecting natural environment are fundamental duties of every citizen. **Article 49** directs the State to protect historic monuments.\n2. **Legislative Measures:**\n   - **AMASR Act, 1958:** Enforces a 100m Prohibited Zone (no construction) and an additional 200m Regulated Zone around protected monuments.\n   - **Antiquities and Art Treasures Act, 1972:** Prohibits unauthorized sale and illegal export of antique relics older than 100 years.\n   - **Wildlife Protection Act, 1972 & Forest Conservation Act, 1980:** Protects flora, fauna, national parks, and biodiversity reserves.\n3. **Institutional Conservation (ASI & INTACH):**\n   - **ASI (est. 1861)** carries out scientific chemical treatment, structural consolidation, and maintenance of 3,690+ national monuments.\n   - **INTACH (est. 1984)** mobilizes citizen participation and conserves unprotected regional heritage.\n4. **Role of Museums:** Preservation of delicate palm-leaf manuscripts, sculptures, and coins under controlled environments (e.g., Calico Museum, L.D. Indology, National Museum).\n5. **Citizen Participation:** Mass awareness campaigns, Heritage Walks, cleanliness drives, and reporting vandalism.\n\n---\n\n### 📌 Question 2 (3 Marks): Write a short note on the role of tourism in preserving our heritage.\n**Model Points:**\n- Generates massive **foreign exchange reserves** and stimulates national economic growth.\n- Creates extensive **direct and indirect employment** (guides, transport, hoteliers, artisans).\n- Revives dying **traditional handicrafts** (e.g. Patola, Bandhani, woodwork, stone carving).\n- Encourages governments to upgrade public transport, highways, sanitation, and safety.\n- Promotes India's cultural richness globally under the ethos of *'Atithi Devo Bhava'*.\n\n---\n\n### 📌 Question 3 (2 Marks): State the importance of any two premier museums of Gujarat.\n**Model Points:**\n1. **Calico Museum of Textiles (Ahmedabad):** Globally acclaimed for exhibiting rare antique Indian hand-woven textiles, tapestries, and royal costumes.\n2. **L.D. Institute of Indology (Ahmedabad):** Houses over 75,000 ancient palm-leaf and paper manuscripts, rare Jain bronzes, and classical sculptures.",
        "difficulty": "Advanced",
        "bloom": "Create"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "Which autonomous NGO established in 1984 actively works with citizens for the conservation of India's architectural and cultural heritage?",
            "options": [
                "INTACH (Indian National Trust for Art and Cultural Heritage)",
                "UNESCO World Heritage Committee",
                "Archaeological Survey of India (ASI)",
                "National Monuments Authority (NMA)"
            ],
            "correct_answer": "INTACH (Indian National Trust for Art and Cultural Heritage)",
            "explanation": "INTACH was founded in 1984 in New Delhi as a pioneer non-governmental organization to spearhead heritage awareness, citizen engagement, and conservation of unprotected heritage structures."
        },
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    # Target output directories
    out_dir = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters"
    os.makedirs(out_dir, exist_ok=True)
    
    # 1. Output to GSEB Class 10 Social Science Chapter 7
    gseb_path = os.path.join(out_dir, "gseb_class10_social_science_ch7.json")
    with open(gseb_path, "w", encoding="utf-8") as f:
        json.dump(final_json, f, indent=2, ensure_ascii=False)
        
    # 2. Output to NCERT Class 10 Social Science Chapter 7
    ncert_path = os.path.join(out_dir, "ncert_class10_social_science_ch7.json")
    final_json_ncert = json.loads(json.dumps(final_json))
    final_json_ncert["metadata"]["id"] = "ncert_class10_social_science_ch7"
    with open(ncert_path, "w", encoding="utf-8") as f:
        json.dump(final_json_ncert, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully generated Supreme Pedagogy files:\n1. {gseb_path}\n2. {ncert_path}")

if __name__ == "__main__":
    generate_supreme_gseb_ss_ch7()
