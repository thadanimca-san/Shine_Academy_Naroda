import json
import os

def generate_supreme_gseb_ss_ch14():
    chapter_id = "gseb_class10_social_science_ch14"
    title = "Chapter 14: Transportation, Communication and Trade (પરિવહન, સંદેશાવ્યવહાર અને વ્યાપાર)"
    
    metadata = {
        "id": chapter_id,
        "title": title,
        "subtitle": "The Supreme Gold Standard Board Exam Mastery Guide",
        "subject": "Social Science",
        "grade": "10",
        "board": "GSEB/NCERT",
        "curriculum": ["GSEB", "CBSE", "Universal"],
        "language": "English/Hindi/Gujarati (Bilingual)",
        "difficulty": "Advanced",
        "estimated_minutes": 180,
        "version": "3.0.0-SUPREME-GOLD",
        "author": "Antigravity Supreme Intelligence",
        "reviewed_by": "Chief Academic Architect",
        "tags": [
            "social_science",
            "geography",
            "transportation",
            "roadways",
            "railways",
            "waterways",
            "airways",
            "pipelines",
            "ropeways",
            "communication",
            "mass_media",
            "postal_system",
            "international_trade",
            "balance_of_trade",
            "ports_of_india",
            "gseb_class10",
            "board_special",
            "bilingual"
        ],
        "learning_outcomes": [
            "Understand why transportation, communication, and trade are called the lifelines of a modern nation's economy.",
            "Classify Indian roadways (National Highways, Golden Quadrilateral, State Highways, District Roads, Village Roads, Border Roads, Expressways).",
            "Analyze the development, gauge systems, and modern advancements of Indian Railways (Vande Bharat, DFC, Bullet Train, Metro).",
            "Evaluate Inland Waterways (NW-1 to NW-5) and Major Oceanic Ports along the Eastern and Western coasts of India and Gujarat.",
            "Explain Airways, Pipeline networks (HVJ Gas Pipeline), and Ropeway transport in hilly terrains and Gujarat.",
            "Differentiate between personal and mass communication media, postal channels, satellite tech (INSAT/IRS/NAVIC), and digital infrastructure.",
            "Master international trade concepts: Exports, Imports, Favourable vs. Unfavourable Balance of Trade, and WTO."
        ],
        "ai_context": {
            "learning_goal": "Transform the student into a Board Exam topper in Social Science Chapter 14 by using the 8-Step Socratic Discovery Cycle, high-yield comparative tables, map identification keys, mnemonic tricks, and precise inline bilingual terms.",
            "common_misconceptions": [
                "Students confuse Favourable Balance of Trade (Exports > Imports) with Unfavourable Balance of Trade (Imports > Exports).",
                "Students often mix up National Waterway 1 (Ganga: Prayagraj to Haldia) with National Waterway 2 (Brahmaputra: Sadiya to Dhubri).",
                "Students confuse Border Roads Organisation (BRO - 1960) with National Highways Authority of India (NHAI - 1995).",
                "Students overlook that pipeline transport incurs high initial laying costs but near-zero subsequent running/maintenance trans-shipment loss.",
                "Students forget that Kandla (Deendayal Port) is a tidal port and India's first Special Economic Zone (SEZ) port."
            ],
            "tutor_hint": "Anchor concepts using practical connectivity examples: The Ahmedabad-Vadodara Expressway (NE-1), Kandla & Mundra ports, the Girnar Ropeway at Junagadh, and the 6 Postal Channels. Use comparative matrices for roadways vs. railways vs. waterways."
        }
    }
    
    blocks = []
    
    # =========================================================================
    # MODULE 1: THE LIFELINES OF A NATION (HOOK & FOUNDATION)
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "Imagine waking up tomorrow morning to find that all delivery trucks, cargo trains, container ships, internet cables, and mobile networks have suddenly stopped working! \n\nNo fresh milk from Amul in Anand `(આણંદ)`, no apples from Kashmir `(કાશ્મીર)`, no petrol for vehicles, and zero text messages. Within 24 hours, society would freeze into total paralysis!\n\nJust as blood vessels `(रक्त वाहिकाएं / રક્તવાહિનીઓ)` circulate oxygen and nutrients throughout the human body, **Transportation `(परिवहन / પરિવહન)`**, **Communication `(संचार / સંદેશાવ્યવહાર)`**, and **Trade `(व्यापार / વ્યાપાર)`** act as the vibrant circulatory system of a modern nation. That is why they are called the **Lifelines of the National Economy `(राष्ट्रीय अर्थव्यवस्था की जीवन रेखाएं / રાષ્ટ્રીય અર્થતંત્રની જીવાદોરીઓ)`**.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "The Interconnected Triad: Transportation carries goods and people; Communication transmits intelligence and instructions; Trade exchanges wealth and commodities. Together, they create socio-economic progress.",
        "image_url": "assets/images/ss_ch14_lifelines_triad.jpg",
        "alt_text": "Triangular diagram showing how Transportation, Communication, and Trade reinforce economic growth"
    })
    
    blocks.append({
        "type": "theory",
        "title": "Evolution & Fundamental Concept of Transportation (પરિવહનનો અર્થ અને વિકાસ)",
        "content": "### 🚚 What is Transportation?\nTransportation is the process of moving human beings, livestock, raw materials `(कच्चा माल / કાચો માલ)`, and finished goods `(तैयाર माल / તૈયાર માલ)` from an area of surplus `(अधिशेष क्षेत्र / પુરાંતવાળા વિસ્તાર)` to an area of deficit or demand `(मांग वाला क्षेत्र / અછત કે માંગવાળા વિસ્તાર)`.\n\n### ⏳ Historical Evolution:\n1. **Primitive Era:** Humans carried loads on their heads and backs, followed by animal beasts of burden `(भारवाहक पशु / ભારવાહક પ્રાણીઓ)` like oxen, horses, camels, and mules.\n2. **Wheel & Steam Engine Revolution:** The invention of the wheel `(पहिया / પૈડું)` and James Watt's steam engine `(भाप का इंजन / વરાળ યંત્ર)` transformed overland and water travel.\n3. **Modern Era:** High-speed electric trains, bullet trains, multilane expressways, giant oceanic container ships `(कंटेनर जहाज / વિશાળ કન્ટેનર જહાજ)`, jet aircraft, space satellites, and cross-country underground pipelines.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Teacher's Exam Golden Rule:** When asked 'Why are transport, communication, and trade complementary to each other?', remember this formulation: \n- **Transport** bridges physical distance `(भौगोलिक दूरी)`. \n- **Communication** bridges informational distance `(सूचनात्मक दूरी)`. \n- **Trade** bridges economic demand-supply distance `(आर्थिक अंतराल)`. \nThey cannot function in isolation!"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "Why are transportation, communication, and trade termed as the 'Lifelines of the National Economy'?",
            "options": [
                "Because they generate all the raw materials directly from agriculture",
                "Because they connect producers to consumers and maintain seamless circulation of goods, services, and information",
                "Because they eliminate the need for international trade",
                "Because they replace heavy manufacturing industries completely"
            ],
            "correct_answer": "Because they connect producers to consumers and maintain seamless circulation of goods, services, and information",
            "explanation": "Just like arteries and veins circulate blood, transport and communication circulate goods, capital, ideas, and people, uniting the country economically and culturally."
        },
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    # =========================================================================
    # MODULE 2: ROAD TRANSPORT IN INDIA (સડક માર્ગો / સડક પરિવહન)
    # =========================================================================
    blocks.append({
        "type": "theory",
        "title": "Roadways: Characteristics and Supremacy over Other Modes",
        "content": "India possesses one of the world's largest road networks `(सड़क नेटवर्क / સડક નેટવર્ક)`, spanning over **60+ lakh kilometers**.\n\n### 🌟 Why Roadways Hold Superiority (સડક માર્ગોની સર્વોપરીતા):\n1. **Door-to-Door Service `(घर-घर तक सेवा / ઘર આંગણા સુધીની સેવા)`:** Only road transport can load goods at a factory doorstep and deliver them right to the consumer's doorstep without intermediate trans-shipment.\n2. **Flexible & Feasible in Tough Terrain:** Roads can negotiate steep slopes `(तीव्र ढलान / તીવ્ર ઢોળાવ)` and sharp curves in mountainous regions (e.g., Himalayas) where laying railway tracks is unfeasible or prohibitively expensive.\n3. **Cost-Effective for Short Distances:** For short journeys and small consignments of perishable items `(नाशवान वस्तुएं - दूध, सब्जियां / નાશવંત વસ્તુઓ - દૂધ, શાકભાજી)`, roadways are faster and cheaper than railways or air transport.\n4. **Feeder Service `(पोषक सेवा / સહાયક સેવા)`:** Roadways act as essential feeders to railway stations, seaports, and airports.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "title": "Classification of Indian Roads (ભારતીય સડક માર્ગોનું વર્ગીકરણ)",
        "content": "In India, roadways are categorized into **6 Strategic Classes** based on administration, capacity, and strategic importance:\n\n---\n\n### 1. 🌟 Golden Quadrilateral Super Highways `(स्वर्णिम चतुर्भुज महामार्ग / સુવર્ણ ચતુર્ભુજ સુપર હાઇવે)`:\n- **Managed by:** National Highways Authority of India (**NHAI**, established 1995).\n- **Structure:** 6-lane express corridors connecting India's 4 major megacities: **Delhi – Mumbai – Chennai – Kolkata** (Total Length: **5,846 km**).\n- **Corridor Projects:**\n  - **North-South Corridor `(उत्तर-दक्षिण गलियारा / ઉત્તર-દક્ષિણ કોરિડોર)`:** Connects **Srinagar** (Jammu & Kashmir) to **Kanyakumari** (Tamil Nadu).\n  - **East-West Corridor `(पूर्व-पश्चिम गलियारा / પૂર્વ-પશ્ચિમ કોરિડોર)`:** Connects **Silchar** (Assam) to **Porbandar** (Gujarat `(પોરબંદર, ગુજરાત)`).\n\n---\n\n### 2. 🏛️ National Highways `(राष्ट्रीय राजमार्ग / રાષ્ટ્રીય ધોરીમાર્ગો)`:\n- **Managed by:** Central Public Works Department (**CPWD / કેન્દ્રીય લોકનિર્માણ વિભાગ**).\n- Primary road systems that connect state capitals, mega industrial zones, strategic frontiers, and major seaports.\n- **Longest National Highway:** **NH-44** (formerly NH-7 extended), running from Srinagar to Kanyakumari (approx. 3,745 km).\n- **NH-48:** Connects Delhi-Jaipur-Ahmedabad-Vadodara-Surat-Mumbai-Bengaluru-Chennai.\n\n---\n\n### 3. 🏢 State Highways `(राज्य राजमार्ग / રાજ્ય ધોરીમાર્ગો)`:\n- **Managed by:** State Public Works Department (**State PWD / રાજ્ય લોકનિર્માણ વિભાગ**).\n- Roads linking state capitals with district headquarters `(जिला मुख्यालय / જિલ્લા મથકો)` and connecting into National Highways.\n\n---\n\n### 4. 🏘️ District Roads `(जिला मार्ग / જિલ્લા માર્ગો)`:\n- **Managed by:** Zilla Parishads / District Panchayats `(जिला पंचायत / જિલ્લા પંચાયત)`.\n- Connect major production centres and Taluka `(તાલુકા)` headquarters to the central district headquarters.\n\n---\n\n### 5. 🌾 Village / Rural Roads `(ग्रामीण सड़कें / ગ્રામીણ સડકો)`:\n- Link remote villages to nearby towns and market mandis.\n- Received massive development under the **Pradhan Mantri Gram Sadak Yojana (PMGSY `(પ્રધાનમંત્રી ગ્રામ સડક યોજના)`)**, ensuring all-weather paved `(पक्की सड़कें / પાકી સડકો)` connectivity.\n\n---\n\n### 6. 🏔️ Border Roads `(सीमा सड़क / સરહદી માર્ગો)`:\n- **Constructed & Maintained by:** **Border Roads Organisation (BRO `(સીમા સડક સંગઠન)`)**, established in **May 1960**.\n- Construct vital strategic roads across sensitive northern and north-eastern border areas (Ladakh, Arunachal Pradesh, Sikkim) in snow-bound, landslide-prone alpine altitudes.",
        "difficulty": "Intermediate",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Map representation of India's Golden Quadrilateral and the North-South (Srinagar-Kanyakumari) and East-West (Silchar-Porbandar) Corridors.",
        "image_url": "assets/images/ss_ch14_golden_quadrilateral_map.jpg",
        "alt_text": "Map showing Golden Quadrilateral connecting Delhi, Mumbai, Chennai, and Kolkata with East-West and North-South corridors"
    })
    
    blocks.append({
        "type": "theory",
        "title": "Expressways & Special Highways in Gujarat (એક્સપ્રેસ-વે અને ગુજરાતના સડક માર્ગો)",
        "content": "### 🏎️ Expressways (દ્રુતગતિ માર્ગો / ઝડપી માર્ગો):\n- Multi-lane (4, 6, or 8-lane) access-controlled express highways built for high-speed, obstacle-free transit without grade crossings `(चौराहे / ક્રોસિંગ)`.\n- Equipped with overbridges, underpasses, automated toll collection (FASTag), and cloverleaf interchanges.\n- **National Expressway 1 (NE-1 `(રાષ્ટ્રીય એક્સપ્રેસ-વે નં. ૧)`):** The **Ahmedabad-Vadodara Expressway** (93 km), an engineering landmark that cut travel time between Gujarat's two economic hubs to under 1 hour!\n- **Delhi-Mumbai Expressway:** World-class 8-lane greenfield expressway passing extensively through Dahod, Vadodara, Bharuch, and Surat in Gujarat.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "memory_trick",
        "content": "🧠 **Super Mnemonic for Road Classes & Managing Authorities:**\n- **G**olden Quadrilateral ➔ **NHAI**\n- **N**ational Highways ➔ **CPWD** (Central)\n- **S**tate Highways ➔ **State PWD**\n- **D**istrict Roads ➔ **District Panchayat / Zilla Parishad**\n- **V**illage Roads ➔ **PMGSY / Gram Panchayat**\n- **B**order Roads ➔ **BRO (1960)**\n*Mnemonic Phrase:* **G**reat **N**ations **S**hine **D**uring **V**ictorious **B**attles!"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "Which organization is responsible for constructing and maintaining strategic roads along India's northern and north-eastern frontiers?",
            "options": [
                "National Highways Authority of India (NHAI)",
                "Border Roads Organisation (BRO)",
                "Central Public Works Department (CPWD)",
                "State Public Works Department (State PWD)"
            ],
            "correct_answer": "Border Roads Organisation (BRO)",
            "explanation": "The Border Roads Organisation (BRO), established in May 1960, constructs and maintains roads in strategically sensitive border areas of the north and north-east."
        },
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "Between which two cities does the East-West Corridor of the Golden Quadrilateral Super Highway run?",
            "options": [
                "Srinagar to Kanyakumari",
                "Silchar (Assam) to Porbandar (Gujarat)",
                "Delhi to Kolkata",
                "Mumbai to Chennai"
            ],
            "correct_answer": "Silchar (Assam) to Porbandar (Gujarat)",
            "explanation": "The East-West Corridor joins Silchar in Assam with Porbandar in Gujarat, while the North-South Corridor joins Srinagar with Kanyakumari."
        },
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })
    
    # =========================================================================
    # MODULE 3: TRAFFIC PROBLEMS, ROAD SAFETY & GREEN MOBILITY
    # =========================================================================
    blocks.append({
        "type": "theory",
        "title": "Traffic Congestion & Road Safety Rules (ટ્રાફિક સમસ્યાઓ અને માર્ગ સલામતી)",
        "content": "### 🚦 Causes of Urban Traffic Congestion `(यातायात की भीड़ / ટ્રાફિક જામ)`:\n1. Exponential rise in personalized two-wheelers and cars versus limited road carriage capacity.\n2. Illegal roadside encroachments `(अवैध अतिक्रमण / ગેરકાયદે દબાણો)` by hawkers and unauthorized parking.\n3. Lack of strict lane discipline `(लेन अनुशासन / લેન શિસ્ત)` and frequent signal jumping.\n\n### 🛡️ Golden Principles of Road Safety (માર્ગ સલામતીના નિયમો):\n- Mandatory use of certified **Helmets `(हेलमेट)`** for two-wheeler riders and **Seatbelts `(सीटबेल्ट)`** for four-wheelers.\n- Strict adherence to traffic signals (Red = Stop, Yellow = Caution/Prepare, Green = Go) and pedestrian Zebra Crossings `(पैदल पारपथ / ઝેબ્રા ક્રોસિંગ)`.\n- **Golden Hour Trauma Care `(गोल्डन ऑवर / ગોલ્ડન અવર)`:** The critical first 60 minutes following a severe road accident where immediate medical attention and dispatch of **108 Emergency Ambulances** can save human life.\n- Zero tolerance for **Drunk Driving** and mobile phone usage while driving.\n- Shift towards **Green Mobility `(हरित गतिशीलता / ગ્રીન મોબિલિટી)`:** Adoption of Electric Vehicles (EVs `(ઇલેક્ટ્રિક વાહનો)`), CNG fuels, and high-capacity Bus Rapid Transit Systems (**BRTS / જનમાર્ગ** in Ahmedabad, Surat, Rajkot).",
        "difficulty": "Intermediate",
        "bloom": "Apply"
    })
    
    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Board Exam Insight:** Questions on 'Measures to Prevent Road Accidents and Traffic Congestion' frequently appear for 3 marks. Make sure to mention: (1) Flyovers and bypasses, (2) Strict licensing and punitive fines, (3) Pedestrian subways/Zebra crossings, (4) Public awareness campaigns and BRTS/Metro mass transit."
    })
    
    # =========================================================================
    # MODULE 4: INDIAN RAILWAYS - THE NATION'S ARTERY (રેલવે પરિવહન)
    # =========================================================================
    blocks.append({
        "type": "theory",
        "title": "Indian Railways: Historic Milestone & Economic Role",
        "content": "Indian Railways `(भारतीय रेल / ભારતીય રેલવે)` is the largest public sector commercial undertaking `(सार्वजनिक उपक्रम / જાહેર ક્ષેત્રનું સાહસ)` in the country.\n\n### 🚂 Historical Inception:\n- The first train in India steamed off on **16th April 1853** between **Mumbai (Bori Bunder / CSMT) and Thane**, covering a historic distance of **34 kilometers**.\n\n### 🌍 Strategic & Economic Importance:\n1. Integrates India's vast diverse culture by enabling millions to travel across states daily.\n2. Bulk carrier for heavy core industries: Transports coal, iron ore, cement, food grains, fertilizers, and petroleum across thousands of kilometers at low cost.\n3. Drives industrialization and agricultural prosperity simultaneously.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "title": "Railway Gauge Systems & Modern Transformations (રેલવે ગેજ અને આધુનિકરણ)",
        "content": "### 📏 Classification by Track Gauge `(रेलवे गेज / રેલવે ગેજ)`:\n1. **Broad Gauge `(ब्रॉड गेज / બ્રોડ ગેજ)`:** Track width = **1.676 meters (5 ft 6 in)**. Covers the overwhelming majority of India's main trunk routes.\n2. **Metre Gauge `(मीटर गेज / મીટર ગેજ)`:** Track width = **1.000 meter (3 ft 3⅜ in)**. Under Project Unigauge `(યુનિગેજ પ્રોજેક્ટ)`, almost all metre gauge lines have been converted to broad gauge.\n3. **Narrow Gauge `(नैरो गेज / નેરો ગેજ)`:** Track width = **0.762 meter or 0.610 meter**. Preserved primarily in heritage mountain railways (e.g., Kalka-Shimla, Darjeeling Himalayan Railway, Nilgiri Mountain Railway, and Matheran Hill Railway).\n\n---\n\n### ⚡ Modern Milestones in Indian Railways:\n- **100% Track Electrification `(विद्युतीकरण / વિદ્યુતીકરણ)`:** Phasing out diesel locomotives to achieve Net Zero carbon emissions.\n- **Vande Bharat Express `(વંદે ભારત એક્સપ્રેસ)`:** Semi-high-speed, indigenously engineered train sets with Kavach safety systems, aerodynamically designed for speeds up to 160-180 km/h.\n- **Dedicated Freight Corridors (DFC `(ડેડિકેટેડ ફ્રેઇટ કોરિડોર)`):** Dedicated high-speed twin-track corridors solely for heavy freight trains (Western DFC connecting Dadri to JNPT Mumbai via Gujarat's Sanand, Palanpur, and Bharuch).\n- **High-Speed Bullet Train Project `(બુલેટ ટ્રેન પ્રોજેક્ટ)`:** Mumbai-Ahmedabad High-Speed Rail Corridor (MAHSR), covering 508 km at 320 km/h with Japanese Shinkansen E5 technology.\n- **Metro Rail & Monorail `(મેટ્રો રેલ)`:** High-speed urban mass transit systems operating in Ahmedabad-Gandhinagar (Gujarat Metro Rail Corporation - GMRC), Delhi, Mumbai, Bengaluru, Kolkata, and Chennai.",
        "difficulty": "Intermediate",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Comparison of Railway Gauge widths (Broad Gauge 1.676m vs Metre Gauge 1.0m vs Narrow Gauge 0.762m) and modern Vande Bharat train layout.",
        "image_url": "assets/images/ss_ch14_railway_gauges_vande_bharat.jpg",
        "alt_text": "Diagram showing Broad Gauge, Metre Gauge, and Narrow Gauge track dimensions alongside high-speed rail"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "When and between which two stations did the first train run in India?",
            "options": [
                "1857: Delhi to Meerut",
                "1853: Mumbai to Thane (34 km)",
                "1901: Ahmedabad to Surat",
                "1869: Kolkata to Howrah"
            ],
            "correct_answer": "1853: Mumbai to Thane (34 km)",
            "explanation": "India's first passenger train started on 16th April 1853 between Mumbai (Bori Bunder) and Thane over a distance of 34 km."
        },
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "What is the standard distance between the rails in a Broad Gauge railway track?",
            "options": [
                "1.000 meter",
                "0.762 meter",
                "1.676 meters",
                "2.100 meters"
            ],
            "correct_answer": "1.676 meters",
            "explanation": "In Broad Gauge (BG), the distance between the inner faces of the two rails is exactly 1.676 meters (5 feet 6 inches)."
        },
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })
    
    # =========================================================================
    # MODULE 5: WATERWAYS & SEAPORTS (જળમાર્ગો અને મુખ્ય બંદરો)
    # =========================================================================
    blocks.append({
        "type": "theory",
        "title": "Waterways: The Most Fuel-Efficient & Eco-Friendly Mode",
        "content": "Water transport is the **oldest and cheapest** mode of transport known to civilization.\n\n### 🌊 Distinct Advantages of Waterways (જળમાર્ગોના વિશિષ્ટ લાભો):\n1. **Zero Infrastructure Cost for Tracks:** Rivers, canals, and oceans are natural pathways; no expenditure is needed for laying rails or tarmac.\n2. **Highest Fuel Efficiency & Heavy Cargo Capacity:** Consumes the least fuel per ton-kilometer, making it ideally suited for transporting massive, bulky, and oversized industrial goods.\n3. **Eco-Friendly `(पर्यावरण अनुकूल / પર્યાવરણને અનુકૂળ)`:** Lowest greenhouse gas emission footprint among all mechanical modes.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "title": "Inland Waterways of India (ભારતના રાષ્ટ્રીય જળમાર્ગો - NW 1 to NW 5)",
        "content": "Managed by the **Inland Waterways Authority of India (IWAI `(ભારતીય આંતરદેશીય જળમાર્ગ પ્રાધિકરણ)` - established 1986)**.\n\n| National Waterway | River / Canal System | Stretch / Route | Total Length |\n| :--- | :--- | :--- | :--- |\n| **NW-1 `(રાષ્ટ્રીય જળમાર્ગ ૧)`** | Ganga - Bhagirathi - Hooghly | **Prayagraj (Allahabad) to Haldia** | **1,620 km** (Longest NW) |\n| **NW-2 `(રાષ્ટ્રીય જળમાર્ગ ૨)`** | Brahmaputra River | **Sadiya to Dhubri** (Assam) | **891 km** |\n| **NW-3 `(રાષ્ટ્રીય જળમાર્ગ ૩)`** | West Coast Canal (Champakara & Udyogmandal canals) | **Kottapuram to Kollam** (Kerala) | **205 km** |\n| **NW-4 `(રાષ્ટ્રીય જળમાર્ગ ૪)`** | Krishna & Godavari Rivers + Canals | **Kakinada to Puducherry** | **1,078 km** |\n| **NW-5 `(રાષ્ટ્રીય જળમાર્ગ ૫)`** | Brahmani River + East Coast Canal | **Talcher to Dhamra / Charbatia** (Odisha) | **588 km** |",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "National Waterways of India highlighting NW-1 (Ganga), NW-2 (Brahmaputra), and NW-3 (Kerala West Coast Canal).",
        "image_url": "assets/images/ss_ch14_national_waterways_map.jpg",
        "alt_text": "Map showing National Waterways NW-1, NW-2, NW-3, NW-4, and NW-5 in India"
    })
    
    blocks.append({
        "type": "theory",
        "title": "Oceanic Routes & Major Seaports of India (ભારતના મુખ્ય દરિયાઈ બંદરો)",
        "content": "India has a vast coastline of **7,516.6 km**, dotted with **12-13 Major Ports `(મુખ્ય બંદરો)`** and over 200 non-major/intermediate ports handling **95% of India's international trade volume** (68% by value).\n\n---\n\n### ⚓ Western Coast Seaports (પશ્ચિમ કિનારાના બંદરો):\n1. **Kandla (Deendayal Port `(દીનદયાળ બંદર - કંડલા, ગુજરાત)`):**\n   - Situated in the Gulf of Kutch `(કચ્છનો અખાત)`.\n   - Developed post-1947 partition to relieve congestion on Mumbai port and compensate for the loss of Karachi port.\n   - India's premier **Tidal Port `(ज्वारीय बंदरगाह / ભરતી બંદર)`** and host to India's first Free Trade Zone / Special Economic Zone (SEZ).\n2. **Mumbai Port `(મુંબઈ બંદર)`:** Largest natural harbor and busiest commercial port of India.\n3. **Jawaharlal Nehru Port (JNPT / Nhava Sheva `(ન્હાવા શેવા)`):** Built opposite Mumbai port; India's largest mechanized container handling port.\n4. **Marmagao Port `(માર્મગોવા, ગોવા)`:** Premier port for iron ore exports from Goa.\n5. **New Mangalore Port `(ન્યૂ મેંગલોર, કર્ણાટક)`:** Exports iron ore concentrates from Kudremukh mines.\n6. **Kochi Port `(કોચી, કેરળ)`:** Natural harbor located at the mouth of the Vembanad lagoon; handles petroleum exports and spice trade.\n\n---\n\n### ⚓ Eastern Coast Seaports (પૂર્વ કિનારાના બંદરો):\n1. **Tuticorin Port (V.O. Chidambaranar `(તૂતીકોરીન, તમિલનાડુ)`):** Deep-sea port on the Gulf of Mannar; handles trade with Sri Lanka and Southeast Asia.\n2. **Chennai Port `(ચેન્નઈ બંદર)`:** One of the oldest **Artificial Ports `(કૃત્રિમ બંદર)`** on the east coast, second to Mumbai in traffic volume.\n3. **Ennore Port (Kamarajar Port):** India's first corporate/public company major port.\n4. **Visakhapatnam Port `(વિશાખાપટ્ટનમ, આંધ્રપ્રદેશ)`:** **Deepest landlocked and fully protected harbor `(સૌથી ઊંડું અને સુરક્ષિત કુદરતી બંદર)`** in India.\n5. **Paradip Port `(પારાદીપ, ઓડિશા)`:** Deep-water port dedicated to exporting iron ore from Odisha and Jharkhand to Japan.\n6. **Kolkata - Haldia Port `(કોલકાતા - હલ્દિયા બંદર)`:** **Riverine Port `(नदी बंदरगाह / નદીય બંદર)`** on the Hooghly river; served by the Haldia dock system to overcome river siltation and tidal bores.",
        "difficulty": "Intermediate",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "theory",
        "title": "Gujarat's Maritime Dominance & Coastal Infrastructure (ગુજરાતનો દરિયાકાંઠો અને બંદરો)",
        "content": "### 🚢 Gujarat: The Maritime Gateway of India:\n- Gujarat boasts India's longest state coastline: **approx. 1,600 km**.\n- Administered by the **Gujarat Maritime Board (GMB `(ગુજરાત મેરીટાઇમ બોર્ડ)` - formed 1982)**.\n- Handles more than **35% to 40%** of India's total national maritime cargo traffic!\n\n### 🌟 Key Maritime Centers in Gujarat:\n- **Mundra Port `(મુન્દ્રા બંદર)`:** India's largest private commercial multi-port and multi-product SEZ operated by Adani Ports.\n- **Pipavav Port `(પીપાવાવ)`:** India's first private-sector port in the Amreli district.\n- **Dahej & Hazira `(દહેજ અને હજીરા)`:** Mega LNG import terminals, chemical ports, and industrial cargo hubs in South Gujarat.\n- **Alang Ship Recycling Yard `(અલંગ શિપ બ્રેકિંગ યાર્ડ, ભાવનગર)`:** The world's largest ship-breaking and scrap metal recovery facility located on the Gulf of Khambhat.\n- **Ro-Ro / Ro-Pax Ferry Services `(રો-રો ફેરી સર્વિસ)`:** Operates between **Ghogha (Bhavnagar) and Hazira (Surat)** across the Gulf of Khambhat, slashing travel distance from 370 km by road to just 90 km by sea and cutting travel time from 10 hours to under 4 hours!",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Teacher's Map Marking Secret:** Every GSEB Class 10 Board Exam includes a 4-mark Map Question! You MUST know the exact coastal locations of:\n1. **Kandla Port** ➔ Gulf of Kutch, Gujarat\n2. **Marmagao Port** ➔ Goa\n3. **Visakhapatnam Port** ➔ Andhra Pradesh coast\n4. **Paradip Port** ➔ Odisha coast\n5. **Haldia Port** ➔ West Bengal on Hooghly river"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "Which is the longest National Waterway in India and over which river does it stretch?",
            "options": [
                "NW-2: Brahmaputra River from Sadiya to Dhubri",
                "NW-1: Ganga River from Prayagraj (Allahabad) to Haldia (1,620 km)",
                "NW-3: West Coast Canal in Kerala",
                "NW-4: Godavari-Krishna rivers"
            ],
            "correct_answer": "NW-1: Ganga River from Prayagraj (Allahabad) to Haldia (1,620 km)",
            "explanation": "National Waterway 1 (NW-1) spans 1,620 km across the Ganga-Bhagirathi-Hooghly river system between Prayagraj and Haldia, making it India's longest inland waterway."
        },
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "Why was Kandla Port (Deendayal Port) in Gujarat developed immediately following India's Independence in 1947?",
            "options": [
                "To export tea directly to Britain",
                "To compensate for the loss of Karachi Port to Pakistan and relieve massive congestion on Mumbai Port",
                "To construct India's first submarine naval shipyard",
                "To serve as a private tourist passenger terminal"
            ],
            "correct_answer": "To compensate for the loss of Karachi Port to Pakistan and relieve massive congestion on Mumbai Port",
            "explanation": "After the partition of 1947, Karachi port went to Pakistan. Kandla was strategically developed as a premier major tidal port on the Gulf of Kutch to cater to north-western India."
        },
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    # =========================================================================
    # MODULE 6: AIRWAYS & PIPELINE TRANSPORT (હવાઈ માર્ગો અને પાઈપલાઈન)
    # =========================================================================
    blocks.append({
        "type": "theory",
        "title": "Airways: The Fastest & Most Prestigious Mode (હવાઈ પરિવહન)",
        "content": "Air transport `(हवाई परिवहन / હવાઈ પરિવહન)` is the fastest, most comfortable, and time-saving mode of transport, capable of scaling across forbidding deserts, dense mountain ranges, and flooded river plains with effortless ease.\n\n### ✈️ Historical Background & Structure:\n- **First Air Flight in India:** Started in **1911** between **Allahabad and Naini** over a distance of 10 km to carry airmail `(હવાઈ ટપાલ)`.\n- **Nationalization (1953):** In 1953, air transport was nationalized under two government corporations:\n  1. **Air India `(એર ઈન્ડિયા)`:** Managed international air travel.\n  2. **Indian Airlines `(ઇન્ડિયન એરલાઇન્સ)`:** Managed domestic and neighbouring South Asian routes.\n  *(Both merged and later privatized back into the Tata Group in 2022).* \n\n### 🚁 Pawan Hans Helicopters Limited `(પવન હંસ હેલિકોપ્ટર લિમિટેડ)`:\n- Provides specialized helicopter logistics to the **Oil and Natural Gas Corporation (ONGC `(ઓ.એન.જી.સી.)`)** for offshore oil rigs (like Mumbai High in the Arabian Sea).\n- Connects inaccessible and remote hilly sectors in the North-East, Jammu & Kashmir, Uttarakhand, and Himachal Pradesh for pilgrim and disaster relief duties.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "title": "Major International Airports of India (ભારતના આંતરરાષ્ટ્રીય હવાઈ મથકો)",
        "content": "India has modernized world-class international airports serving millions of global passengers:\n\n1. **Sardar Vallabhbhai Patel International Airport `(સરદાર વલ્લભભાઈ પટેલ આંતરરાષ્ટ્રીય એરપોર્ટ)`:** Ahmedabad, Gujarat `(અમદાવાદ, ગુજરાત)`.\n2. **Indira Gandhi International Airport (IGI):** New Delhi.\n3. **Chhatrapati Shivaji Maharaj International Airport:** Mumbai.\n4. **Netaji Subhash Chandra Bose International Airport:** Kolkata (Dum Dum).\n5. **Chennai International Airport (Meenambakkam):** Chennai.\n6. **Kempegowda International Airport:** Bengaluru.\n7. **Rajiv Gandhi International Airport:** Hyderabad.\n8. **Sri Guru Ram Dass Jee International Airport:** Amritsar (Raja Sansi).",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "theory",
        "title": "Pipeline Transport: The Invisible Veins of Modern Industry (પાઈપલાઈન પરિવહન)",
        "content": "In earlier times, pipelines `(पाइपलाइन / પાઈપલાઈન)` were used solely for supplying water to cities. Today, they are a frontline transit network for **crude oil `(कच्चा तेल / કાચું ખનીજતેલ)`**, refined petroleum fuels, natural gas, and even solid minerals converted into **slurry `(गाढ़ा घोल / સ્લરી / પ્રવાહી મિશ્રણ)`** (e.g., iron ore slurry from Kudremukh mines to Mangalore port)!\n\n### 🔧 Advantages of Pipelines:\n1. **Zero Trans-shipment Loss:** Eliminates transit leakage, evaporation, and transit theft.\n2. **Uninterrupted 24x7 Supply:** Functions seamlessly regardless of extreme weather, floods, fog, or traffic snarls.\n3. **Low Operating & Maintenance Cost:** Although laying pipeline networks requires high initial capital investment `(प्रारंभिक पूंजीगत व्यय / પ્રારંભિક મૂડીરોકાણ)`, the running operational costs are exceptionally minimal.\n\n### 🛢️ Crucial Pipeline Networks in India:\n1. **Upper Assam Oilfield to Kanpur (UP):** Via Guwahati, Barauni, and Prayagraj.\n2. **Salaya-Mathura Pipeline (SMPL):** Runs from Salaya in Gulf of Kutch (Gujarat) via Viramgam to Mathura refinery, extending further to Panipat and Jalandhar.\n3. **HVJ / HBJ Gas Pipeline `(એચ.વી.જે. ગેસ પાઈપલાઈન)`:** India's landmark cross-country gas pipeline connecting **Hazira (Gujarat) ⟶ Vijaipur (Madhya Pradesh) ⟶ Jagdishpur (Uttar Pradesh)** (over 1,750+ km), supplying gas to fertilizer and power plants.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Schematic of the HVJ Pipeline originating from Hazira in Gujarat, passing through Madhya Pradesh to Uttar Pradesh, powering industries along its corridor.",
        "image_url": "assets/images/ss_ch14_hvj_pipeline_map.jpg",
        "alt_text": "Map showing the Hazira-Vijaipur-Jagdishpur (HVJ) gas pipeline network"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "What is the full expansion of the iconic 'HVJ Pipeline' that transports natural gas from Gujarat across northern India?",
            "options": [
                "Hyderabad - Varanasi - Jalandhar",
                "Hazira (Gujarat) - Vijaipur (MP) - Jagdishpur (UP)",
                "Haridwar - Vadodara - Jamnagar",
                "Haldia - Vishakhapatnam - Jabalpur"
            ],
            "correct_answer": "Hazira (Gujarat) - Vijaipur (MP) - Jagdishpur (UP)",
            "explanation": "The HVJ Gas Pipeline starts at Hazira in Gujarat, passes through Vijaipur in Madhya Pradesh, and reaches Jagdishpur in Uttar Pradesh, supplying natural gas to major fertilizer and industrial units."
        },
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })
    
    # =========================================================================
    # MODULE 7: ROPEWAYS OF INDIA & GUJARAT (રજ્જુમાર્ગ / રોપ-વે)
    # =========================================================================
    blocks.append({
        "type": "theory",
        "title": "Ropeway Transport: Scaling Rugged Peaks (રજ્જુમાર્ગ - રોપ-વે)",
        "content": "In steep mountainous terrains where road or railway construction is technically unfeasible or environmentally catastrophic, **Ropeways `(रज्जुमार्ग / રોપ-વે / રજ્જુમાર્ગ)`** serve as a safe, thrilling, and rapid mode of aerial transit.\n\n### 🚠 Prominent Ropeways in Gujarat:\n1. **Girnar Ropeway `(ગિરનાર રોપ-વે, જૂનાગઢ)`:**\n   - Located at Mount Girnar, Junagadh.\n   - **Asia's longest temple ropeway project** (approx. 2.3 km length), ferrying pilgrims from the foothills to Ambaji temple atop Girnar in just 8-10 minutes (replacing a strenuous climb of nearly 10,000 stone steps!).\n2. **Pavagadh Ropeway (Udan Khatola `(પાવાગઢ રોપ-વે, પંચમહાલ)`):** Operates at Kalika Mata Temple on Pavagadh hill.\n3. **Ambaji Ropeway `(અંબાજી - ગબ્બર રોપ-વે, બનાસકાંઠા)`):** Operates at Gabbar hill pilgrimage.\n4. **Saputara Ropeway `(સાપુતારા રોપ-વે, ડાંગ)`):** Popular tourist aerial tramway at Gujarat's sole hill station in Dang.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Girnar Ropeway cabins gliding over lush green forested ridges to the sacred summit of Mount Girnar in Junagadh.",
        "image_url": "assets/images/ss_ch14_girnar_ropeway.jpg",
        "alt_text": "Photograph/illustration of Girnar Ropeway at Junagadh, Gujarat"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "Which ropeway in Gujarat holds the distinction of being one of Asia's longest temple passenger ropeways?",
            "options": [
                "Pavagadh Ropeway",
                "Saputara Ropeway",
                "Girnar Ropeway (Junagadh)",
                "Ambaji Gabbar Ropeway"
            ],
            "correct_answer": "Girnar Ropeway (Junagadh)",
            "explanation": "The Girnar Ropeway at Junagadh in Gujarat, inaugurated in October 2020 with a track length of 2.3 km, is one of the longest temple passenger ropeways in Asia."
        },
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    # =========================================================================
    # MODULE 8: COMMUNICATION SYSTEMS (સંદેશાવ્યવહાર / સંચાર તંત્ર)
    # =========================================================================
    blocks.append({
        "type": "theory",
        "title": "Communication: Personal vs. Mass Communication (વૈયક્તિક અને સામૂહિક સંચાર)",
        "content": "Communication `(संचार / સંદેશાવ્યવહાર)` is the transmission, exchange, and receipt of messages, emotions, information, and ideas between individuals or large audiences.\n\n### 📱 Categories of Communication:\n1. **Personal Communication `(व्यक्तिगत संचार / વૈયક્તિક સંચાર)`:** Direct one-on-one interchange between two parties. Includes letters, postal postcards, telephone, mobile smartphone calls, SMS, WhatsApp, and private email.\n2. **Mass Communication `(जनसंचार / સામૂહિક સંચાર - માસ મીડિયા)`:** Transmits information, education, and entertainment simultaneously to millions of citizens across the globe.\n   - **Print Media `(मुद्रण माध्यम / મુદ્રણ માધ્યમ)`:** Daily newspapers, weekly journals, periodicals, research magazines, and books.\n   - **Electronic Media `(इलेक्ट्रॉनिक माध्यम / ઇલેક્ટ્રોનિક માધ્યમ)`:** Radio broadcasting (All India Radio / Akashvani), Television (Doordarshan), Cinema/Feature Films, Satellite TV channels, Podcasting, and Web Portals.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "title": "Indian Postal System & The 6 Special Postal Channels (ભારતીય ટપાલ સેવા અને ૬ ટપાલ ચેનલો)",
        "content": "The **Indian Postal Network `(भारतीय डाक प्रणाली / ભારતીય ટપાલ નેટવર્ક)`** is the **largest postal network in the entire world**, operating over 1.55 lakh post offices.\n\n### 📮 PIN Code System (Postal Index Number `(પિન કોડ - ટપાલ સૂચકાંક)`):\n- Introduced on **15th August 1972**.\n- A **6-digit unique numerical code** designed to eliminate errors caused by similar place names, handwritten scripts, and multiple regional languages.\n- First digit indicates the postal region (Gujarat falls under region **3**, with initial digits 36, 37, 38, 39).\n\n### 📨 The 6 Dedicated Fast Mail Channels (ઝડપી ટપાલ ડિલિવરી માટે ૬ ચેનલો):\nTo accelerate mail transit between megacities and towns, India Post operates **6 Dedicated Mail Channels**:\n1. **Rajdhani Channel `(રાજધાની ચેનલ - પીળા રંગની ટપાલ પેટી)`:** Connects New Delhi with state capitals.\n2. **Metro Channel `(મેટ્રો ચેનલ - વાદળી રંગની ટપાલ પેટી)`:** Fast-track delivery between 6 major metropolitan hubs (Delhi, Mumbai, Kolkata, Chennai, Bengaluru, Hyderabad).\n3. **Green Channel `(ગ્રીન ચેનલ - લીલા રંગની ટપાલ પેટી)`:** Priority delivery of local city mail within large urban centres.\n4. **Business Channel `(બિઝનેસ ચેનલ)`:** Bulk corporate business letters and commercial correspondence.\n5. **Bulk Mail Channel `(બલ્ક મેઇલ ચેનલ)`:** Handles massive printed shipments, company annual reports, and advertising circulars.\n6. **Periodical Channel `(પિરિયોડિકલ ચેનલ)`:** Dedicated for regular delivery of registered newspapers, magazines, and periodicals.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "theory",
        "title": "Electronic Media, Cinema & Space Satellite Systems (ઇલેક્ટ્રોનિક મીડિયા અને સેટેલાઇટ ટેકનોલોજી)",
        "content": "### 📻 Radio & Television Broadcasting:\n- **All India Radio (AIR / Akashvani `(આકાશવાણી)`):** National public broadcaster broadcasting educational, cultural, agricultural (Kisan Vani), and news bulletins in 23 languages and 179 dialects.\n- **Doordarshan (DD `(દૂરદર્શન)`):** India's national terrestrial and satellite television network, one of the largest terrestrial broadcast infrastructures on earth.\n\n### 🎬 Indian Cinema (ભારતીય સિનેમા / ચલચિત્ર ઉદ્યોગ):\n- India is the **largest producer of feature films** in the world (Bollywood, Gujarati cinema - Gollywood, Tollywood, etc.).\n- **Central Board of Film Certification (CBFC `(કેન્દ્રીય ફિલ્મ પ્રમાણન બોર્ડ)`):** The statutory authority responsible for reviewing, regulating, and certifying all films for public exhibition in India (U, U/A, A, S certificates).\n\n### 🛰️ Space Satellites & Space Application Centre (ઇસરો અને સેટેલાઇટ):\n- **INSAT / GSAT Series `(ઇનસેટ શ્રેણી)`:** Multi-purpose geostationary satellites for telecommunication, TV broadcasting, cyclone warning, and meteorology.\n- **IRS Series (Indian Remote Sensing Satellites `(દૂરસંવેદન ઉપગ્રહ)`):** Natural resource mapping, ground water surveys, forest cover monitoring, and oceanography.\n- **NavIC (Navigation with Indian Constellation):** India's sovereign satellite navigation system developed by **ISRO** (whose Space Applications Centre - **SAC** is located in Ahmedabad, Gujarat!).",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Board Exam MCQ Alert:** Keep these key numbers and years crystal clear: \n- **PIN Code introduced:** 15th August 1972 (6 digits). \n- **First Train in India:** 1853 (Mumbai-Thane, 34 km). \n- **First Air Flight:** 1911 (Allahabad to Naini). \n- **BRO Founded:** May 1960. \n- **Number of Dedicated Fast Mail Channels:** Exactly 6."
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "In which year was the 6-digit Postal Index Number (PIN Code) system introduced in India?",
            "options": [
                "1947",
                "1953",
                "1972",
                "1991"
            ],
            "correct_answer": "1972",
            "explanation": "The 6-digit PIN Code system was introduced by the Indian Postal Service on 15th August 1972 to facilitate speedy, error-free mail sorting."
        },
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "Which authority in India is legally empowered to certify and regulate Indian and foreign feature films before public release?",
            "options": [
                "Press Council of India (PCI)",
                "Border Roads Organisation (BRO)",
                "Central Board of Film Certification (CBFC)",
                "Inland Waterways Authority of India (IWAI)"
            ],
            "correct_answer": "Central Board of Film Certification (CBFC)",
            "explanation": "The Central Board of Film Certification (CBFC) is the statutory body regulating the public exhibition of films under the provisions of the Cinematograph Act."
        },
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    # =========================================================================
    # MODULE 9: INTERNAL AND INTERNATIONAL TRADE (વ્યાપાર પ્રણાલી)
    # =========================================================================
    blocks.append({
        "type": "theory",
        "title": "Concept of Trade & Internal vs. International Trade (વ્યાપારનો અર્થ અને પ્રકારો)",
        "content": "No single country on Earth produces every single resource or manufactured product it needs. Differences in topography, climate, mineral deposits, and technical skills make **Trade `(व्यापार / વ્યાપાર)`** an inevitable economic reality.\n\n### 🔄 Definition of Trade:\nTrade is the mutual exchange of goods, commodities, services, and capital between buyers and sellers across regional or national borders.\n\n### 🏛️ Types of Trade (વ્યાપારના બે મુખ્ય પ્રકાર):\n1. **Internal / Domestic Trade `(आंतरिक व्यापार / આંતરિક વ્યાપાર)`:**\n   - Occurs strictly **within the political boundaries of a single nation** (between states, cities, or villages).\n   - Examples: Wheat from Punjab transported to Gujarat; Spices from Kerala sold in Uttar Pradesh; Cotton textiles from Ahmedabad dispatched to Bihar.\n   - Transacted in local domestic currency (Indian Rupee - ₹) without customs duties.\n2. **International / Foreign Trade `(अंतर्राष्ट्रीय / विदेशी व्यापार / આંતરરાષ્ટ્રીય વ્યાપાર)`:**\n   - Occurs **between two or more sovereign nations** across international borders.\n   - Involves foreign exchange currencies (US Dollar $, Euro €, Japanese Yen ¥) and adherence to international trade tariffs, import quotas, and WTO conventions.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "title": "Balance of Trade: Favourable vs. Unfavourable (વ્યાપાર તુલા / વ્યાપાર સંતુલન)",
        "content": "The difference in economic value between a country's total **Exports `(निर्यात / નિકાસ)`** and total **Imports `(आयात / આયાત)`** during a given fiscal year is called the **Balance of Trade `(व्यापार संतुलन / વ્યાપાર તુલા)`**.\n\n---\n\n### ⚖️ 1. Favourable Balance of Trade `(अनुकूल व्यापार संतुलन / સાનુકૂળ વ્યાપાર તુલા)`:\n- **Condition:** Value of Exports **>** Value of Imports (Exports exceed Imports).\n- The country earns more foreign exchange currency than it spends, creating a **Trade Surplus `(व्यापार अधिशेष / વ્યાપાર પુરાંત)`**.\n- Indicates strong industrial competitiveness and brings immense national prosperity.\n\n---\n\n### 📉 2. Unfavourable Balance of Trade `(प्रतिकूल व्यापार संतुलन / પ્રતિકૂળ વ્યાપાર તુલા)`:\n- **Condition:** Value of Imports **>** Value of Exports (Imports exceed Exports).\n- The country spends more foreign exchange currency on imports than it earns from exports, leading to a **Trade Deficit `(व्यापार घाटा / વ્યાપાર ખાધ)`** and foreign debt accumulation.\n\n---\n\n### 🌐 World Trade Organization (WTO `(વિશ્વ વ્યાપાર સંગઠન)`):\n- Established on **1st January 1995** (Headquarters: **Geneva, Switzerland**).\n- Promotes free, fair, and rule-based multilateral global trade by reducing import tariffs, quotas, and non-tariff barriers.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Weighing Scale depicting Balance of Trade: Favourable (Exports heavy, bringing foreign wealth) vs Unfavourable (Imports heavy, draining foreign reserves).",
        "image_url": "assets/images/ss_ch14_balance_of_trade_scale.jpg",
        "alt_text": "Weighing scale diagram showing Exports versus Imports for Favourable and Unfavourable Balance of Trade"
    })
    
    blocks.append({
        "type": "theory",
        "title": "India's Foreign Trade Profile: Major Exports & Imports (ભારતની નિકાસ અને આયાત)",
        "content": "### 📦 Major Export Commodities of India (ભારતની મુખ્ય નિકાસ વસ્તુઓ):\n1. **Gems & Jewellery `(रत्न एवं आभूषण / હીરા, ઝવેરાત અને આભૂષણો)`:** Surat `(સુરત)` is the diamond polishing capital of the planet, polishing 9 out of every 10 diamonds worldwide!\n2. **Petroleum Refined Products:** Jamnagar Refinery in Gujarat (Reliance) is the largest grassroots oil refining complex on earth.\n3. **Pharmaceuticals & Drugs `(दवाएं और औषधियां / દવાઓ અને ઔષધો)`:** India is known as the 'Pharmacy of the World'.\n4. **Engineering Goods, Machinery, and Automobiles:** Vehicles, auto parts, industrial machinery.\n5. **Textiles & Readymade Garments:** Cotton textiles, silk, jute, and designer garments.\n6. **Agricultural & Allied Commodities:** Basmati rice, marine seafood (shrimps from Gujarat/Kerala), spices, tea, coffee, tobacco, and castor oil `(દિવેલ / એરંડા)`. \n7. **Software & IT Services:** Exporting billions worth of tech solutions to USA, Europe, and Asia.\n\n---\n\n### 🚢 Major Import Commodities of India (ભારતની મુખ્ય આયાત વસ્તુઓ):\n1. **Crude Petroleum & Natural Gas `(कच्चा खनिज तेल / કાચું પેટ્રોલિયમ ખનીજતેલ)`:** Accounts for the single largest chunk of India's import bill.\n2. **Gold, Silver & Precious Metals `(सोना और चांदी / સોનું અને ચાંદી)`:** Massive demand for jewellery and investment.\n3. **Electronic Hardware, Computers & Telecom Goods:** Silicon chips, mobile components.\n4. **Heavy Capital Machinery & Equipment.**\n5. **Fertilizers & Chemicals `(रासायनिक उर्वरक / રાસાયણિક ખાતરો)`:** Potash, rock phosphate, and urea.\n6. **Edible Vegetable Oils `(खाने का तेल - पाम ऑयल / ખાદ્યતેલ)`:** Palm oil imported from Indonesia/Malaysia and sunflower oil from Ukraine.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Board Exam Distinguish Question (3 Marks):**\n**Differentiate between Favourable and Unfavourable Balance of Trade:**\n- **Exports > Imports** ➔ Favourable Balance of Trade (Brings foreign currency reserves, boosts national GDP).\n- **Imports > Exports** ➔ Unfavourable Balance of Trade (Drains foreign currency reserves, causes trade deficit).\n*Always write both definition and economic impact to get full 3/3 marks!*"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "What is the economic condition called when the total monetary value of a country's exports exceeds the value of its imports?",
            "options": [
                "Unfavourable Balance of Trade",
                "Favourable Balance of Trade",
                "Fiscal Deficit",
                "Internal Domestic Barter"
            ],
            "correct_answer": "Favourable Balance of Trade",
            "explanation": "When export earnings exceed import expenditures (Exports > Imports), the country enjoys a Favourable Balance of Trade with a trade surplus."
        },
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "Which city in Gujarat is internationally recognized as the world's foremost diamond cutting and polishing hub?",
            "options": [
                "Rajkot",
                "Surat",
                "Vadodara",
                "Bhavnagar"
            ],
            "correct_answer": "Surat",
            "explanation": "Surat is the global diamond polishing hub, cutting and polishing over 90% of the world's rough diamonds, making gems and jewellery one of India's premier export earners."
        },
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    # =========================================================================
    # MODULE 10: BOARD EXAM HOTS & MASTER REVISION SUITE
    # =========================================================================
    blocks.append({
        "type": "exam_tips",
        "content": "🏆 **BOARD EXAM TOPPER'S CHAPTER 14 MASTER REVISION SHEET:**\n\n1. **Golden Quadrilateral:** 5,846 km, 6-lane super highway connecting Delhi-Mumbai-Chennai-Kolkata (NHAI).\n2. **Corridors:** North-South (Srinagar to Kanyakumari) | East-West (Silchar to Porbandar).\n3. **First Railway:** 16th April 1853, Mumbai to Thane (34 km).\n4. **Railway Gauges:** Broad Gauge (1.676 m), Metre Gauge (1.000 m), Narrow Gauge (0.762 m / 0.610 m).\n5. **National Waterways:** \n   - **NW-1:** Ganga River (Prayagraj to Haldia, 1,620 km - Longest)\n   - **NW-2:** Brahmaputra River (Sadiya to Dhubri, 891 km)\n   - **NW-3:** West Coast Canal (Kottapuram to Kollam, 205 km)\n6. **Gujarat Seaports:** Kandla (Deendayal - Tidal port, 1st SEZ), Mundra (Largest private port), Alang (World's largest ship recycling yard), Ghogha-Hazira Ro-Ro Ferry.\n7. **Pipelines:** HVJ Gas Pipeline (Hazira ⟶ Vijaipur ⟶ Jagdishpur, 1,750+ km) | SMPL (Salaya-Mathura Pipeline).\n8. **First Flight:** 1911 (Allahabad to Naini airmail).\n9. **Postal PIN Code:** Introduced 15th August 1972 (6 digits, 6 mail channels: Rajdhani, Metro, Green, Business, Bulk Mail, Periodical).\n10. **Trade Balance:** Favourable (Exports > Imports) vs Unfavourable (Imports > Exports).\n11. **WTO:** Established 1st January 1995 in Geneva, Switzerland."
    })
    
    blocks.append({
        "type": "reflection",
        "content": "💡 **Socratic Reflection & Future Thinking:**\nIndia is building the Dedicated Freight Corridors (DFC), the Mumbai-Ahmedabad High-Speed Bullet Train, electric highway corridors, and green hydrogen-powered trains.\n\nHow will these ultra-modern transport technologies transform Gujarat and India's economic growth over the next 20 years? Will they reduce logistics costs and make Indian goods unbeatable globally?"
    })
    
    # Assemble Final JSON Payload
    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    # Define Target Output Paths
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    chapters_dir = os.path.join(base_dir, "app_core", "chapters")
    os.makedirs(chapters_dir, exist_ok=True)
    
    gseb_output_path = os.path.join(chapters_dir, "gseb_class10_social_science_ch14.json")
    ncert_output_path = os.path.join(chapters_dir, "ncert_class10_social_science_ch14.json")
    
    # Save GSEB chapter
    final_json["metadata"]["id"] = "gseb_class10_social_science_ch14"
    with open(gseb_output_path, "w", encoding="utf-8") as f:
        json.dump(final_json, f, indent=2, ensure_ascii=False)
        
    # Save NCERT chapter
    final_json["metadata"]["id"] = "ncert_class10_social_science_ch14"
    with open(ncert_output_path, "w", encoding="utf-8") as f:
        json.dump(final_json, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully generated Supreme GSEB/NCERT Social Science Chapter 14:")
    print(f"  -> {gseb_output_path}")
    print(f"  -> {ncert_output_path}")

if __name__ == "__main__":
    generate_supreme_gseb_ss_ch14()
