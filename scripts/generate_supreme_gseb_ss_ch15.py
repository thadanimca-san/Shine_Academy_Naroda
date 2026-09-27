import json
import os

def generate_supreme_gseb_ss_ch15():
    chapter_id = "gseb_class10_social_science_ch15"
    title = "Chapter 15: Economic Development"
    
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
            "economics",
            "economic_development",
            "economic_growth",
            "developing_economy",
            "primary_secondary_service_sectors",
            "factors_of_production",
            "market_system",
            "socialist_system",
            "mixed_economy",
            "board_special",
            "bilingual"
        ],
        "learning_outcomes": [
            "Differentiate between Economic Growth `(આર્થિક વૃદ્ધિ / आर्थिक वृद्धि)` and Economic Development `(આર્થિક વિકાસ / आर्थिक विकास)` across qualitative, quantitative, and global perspectives.",
            "Analyze the 9 core characteristics of a Developing Economy `(વિકાસશીલ અર્થતંત્રના લક્ષણો / विकासशील अर्थव्यवस्था के लक्षण)` including Dual Economy, Per Capita Income (< $735), and Population Growth.",
            "Distinguish clearly between Economic Activities `(આર્થિક પ્રવૃત્તિઓ / आर्थिक गतिविधियाँ)` and Non-Economic Activities `(બિન-આર્થિક પ્રવૃત્તિઓ / गैर-आर्थिक गतिविधियाँ)` with real-life examples.",
            "Master the three sectors of Indian Economy: Primary `(પ્રાથમિક ક્ષેત્ર / प्राथमिक क्षेत्र)`, Secondary `(માધ્યમિક / ઉદ્યોગ ક્ષેત્ર / द्वितीयक क्षेत्र)`, and Service `(સેવા ક્ષેત્ર / सेवा क्षेत्र)` and their transition during development.",
            "Evaluate the 4 Factors of Production: Land `(જમીન / भूमि)`, Capital `(મૂડી / पूंजी)`, Labour `(શ્રમ / श्रम)`, and Entrepreneur `(નિયોજક / उद्यमी)` along with their economic rewards (Rent, Interest, Wages, Profit).",
            "Understand the fundamental economic problem of Resource Allocation `(સાધનોની ફાળવણી / साधनों का आवंटन)` based on unlimited wants and alternative uses.",
            "Critically compare the three global economic systems: Market System `(બજાર પદ્ધતિ / बाजार प्रणाली)`, Socialist System `(સમાજવાદી પદ્ધતિ / समाजवादी प्रणाली)`, and Mixed Economy `(મિશ્ર અર્થતંત્ર / मिश्रित अर्थव्यवस्था)` as practiced in India.",
            "Ace GSEB/CBSE Board Exam questions with structured answer frameworks, high-order thinking skills (HOTS), and memory mnemonics."
        ],
        "ai_context": {
            "learning_goal": "Empower the student to master foundational economics with supreme clarity. Break down abstract concepts into tangible analogies (street vendor vs supermall, farming vs IT services), vivid diagrams, bilingual glossaries with backtick translations, and board exam scoring blueprints.",
            "common_misconceptions": [
                "Students often use 'Economic Growth' and 'Economic Development' interchangeably, not realizing Growth is purely quantitative (GDP rise) while Development is qualitative (standard of living, structural shift, health, education).",
                "Students confuse the rewards of factors of production (e.g., assigning profit to capital instead of interest, or rent to labour).",
                "Students mistakenly assume that India is a purely Capitalist or purely Socialist country, rather than a pioneering Mixed Economy.",
                "Students confuse Disguised Unemployment `(પ્રચ્છન્ન બેરોજગારી / छिपी हुई बेरोजगारी)` with Seasonal Unemployment."
            ],
            "tutor_hint": "Use mnemonic formula tables: 4 Factors ➔ L-C-L-E (Land, Capital, Labour, Entrepreneur); Rewards ➔ R-I-W-P (Rent, Interest, Wages, Profit); 3 Sectors ➔ Primary (Raw Nature), Secondary (Factory Transformation), Service (Support & Intangibles); 3 Systems ➔ Market (Profit & Price Mechanism), Socialist (Social Welfare & Central Planning), Mixed (Coexistence of Public & Private). Highlight Kautilya's Arthashastra to ground modern economics in timeless Indian wisdom."
        }
    }

    blocks = []

    # =========================================================================
    # MODULE 1: HOOK & INTRODUCTION TO ECONOMIC DEVELOPMENT
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "Every morning, when you step out of your house, look around: a street vendor `(ફેરીયો / फेरीवाला)` sells fresh vegetables from a wooden cart, a software engineer codes applications on a laptop inside an air-conditioned skyscraper, a farmer plows his fertile field in a village, and a giant cargo truck transports industrial goods on a six-lane highway. \n\nWhy do some people live in luxury with modern amenities while others struggle for their daily bread `(રોજીરોટી / आजीविका)`? Why are nations like the USA and Japan called 'Developed', while India is called 'Developing'? \n\nThe answer lies in one powerful, life-shaping subject: **Economic Development `(આર્થિક વિકાસ / आर्थिक विकास)`**! From ancient Indian economic treatises like **Kautilya's Arthashastra `(કૌટિલ્યનું અર્થશાસ્ત્ર / कौटिल्य का अर्थशास्त्र)`** to modern global markets, let us decode how wealth is created, distributed, and transformed to uplift human life!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "diagram",
        "content": "The Spectrum of Economic Development: From basic survival needs (Food, Clothing, Shelter) to comprehensive human prosperity (Education, Healthcare, Technology, High Standard of Living).",
        "image_url": "assets/images/gseb_ss_ch15_economic_development_overview.jpg",
        "alt_text": "Visual diagram comparing a developing economy with agricultural roots to a modern developed economy with advanced industries and high living standards."
    })

    blocks.append({
        "type": "theory",
        "content": "### 🌟 What is Economic Development?\n\nIn the modern world, every nation continuously strives to achieve rapid economic progress. However, economic progress is not merely about printing more currency notes.\n\n**Economic Development `(આર્થિક વિકાસ / आर्थिक विकास)`** is a multi-dimensional continuous process that indicates:\n1. **Continuous increase in National Income `(રાષ્ટ્રીય આવકમાં સતત વધારો / राष्ट्रीय आय में निरंतर वृद्धि)`** of a country.\n2. **Continuous increase in Per Capita Income `(માથાદીઠ આવકમાં સતત વધારો / प्रति व्यक्ति आय में निरंतर वृद्धि)`** of the citizens.\n3. **Qualitative improvement in the Standard of Living `(લોકોના જીવનધોરણમાં સુધારો / लोगों के जीवन स्तर में सुधार)`**.\n\n#### 📊 Key Economic Terms:\n- **National Income `(રાષ્ટ્રીય આવક / राष्ट्रीय आय)`:** The total monetary value of all final goods and services produced in a country in a single financial year `(દેશની કુલ વાર્ષિક આવક / देश की कुल वार्षिक आय)`.\n- **Per Capita Income `(માથાદીઠ આવક / प्रति व्यक्ति आय)`:** The average income earned per person in a given nation, calculated as:\n  $$\\text{Per Capita Income} = \\frac{\\text{Total National Income}}{\\text{Total Population of the Country}}$$\n- **Standard of Living `(જીવનધોરણ / जीवन स्तर)`:** Refers to the quality and availability of basic necessities and comforts, including nutritious food `(ખોરાક / पौष्टिक भोजन)`, clean drinking water `(પીવાનું શુદ્ધ પાણી / स्वच्छ पेयजल)`, clothing `(કપડાં / वस्त्र)`, proper housing `(રહેઠાણ / आवास)`, quality education `(શિક્ષણ / शिक्षा)`, healthcare facilities `(આરોગ્ય સેવાઓ / स्वास्थ्य सेवाएं)`, electricity `(વીજળી / बिजली)`, and transportation `(વાહનવ્યવહાર / परिवहन)`.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Teacher's Secret Insight:** In Board Exams, questions often ask: *'What is Economic Development? Explain with reference to standard of living.'* Always state the 3 core pillars: (1) Rise in National Income, (2) Rise in Per Capita Income, and (3) Tangible improvement in living conditions (Food, Health, Education, Shelter)!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    # =========================================================================
    # MODULE 2: ECONOMIC GROWTH VS ECONOMIC DEVELOPMENT
    # =========================================================================
    blocks.append({
        "type": "theory",
        "content": "### ⚖️ Economic Growth vs Economic Development\n\nIn everyday language, 'Growth' and 'Development' are often treated as synonyms. But in economics, there is a fundamental and profound difference between **Economic Growth `(આર્થિક વૃદ્ધિ / आर्थिक वृद्धि)`** and **Economic Development `(આર્થિક વિકાસ / आर्थिक विकास)`**!\n\nWe can differentiate them on three distinct grounds:\n\n#### 1. On the Basis of Development Process `(વિકાસની પ્રક્રિયાના આધારે / विकास प्रक्रिया के आधार पर)`:\n- **Economic Development is Qualitative `(ગુણાત્મક / गुणात्मक)`:** It is the **first stage** of change. It involves structural changes, modern technology adoption, institutional reforms, and overall social transformation.\n- **Economic Growth is Quantitative `(પરિમાણાત્મક / परिमाणात्मक)`:** It is the **result or outcome** of economic development. It simply measures the numeric expansion of GDP without necessarily reflecting institutional or social reforms.\n\n#### 2. According to Changes Taking Place in the Economy `(અર્થતંત્રમાં થતા પરિવર્તનને આધારે / अर्थव्यवस्था में परिवर्तनों के आधार पर)`:\n- When agricultural production increases due to **new technological research, hybrid seeds `(હાઈબ્રિડ બિયારણ / संकर बीज)`, and modern irrigation**, it is called **Economic Development**.\n- When agricultural production increases merely by bringing **more barren land under cultivation `(ખેડાણ હેઠળની જમીનમાં વધારો / अधिक भूमि पर खेती)`** without any new technology or innovation, it is called **Economic Growth**.\n\n#### 3. In Relation to Developed and Developing Nations `(વિકસિત અને વિકાસશીલ દેશોના સંદર્ભમાં / विकसित और विकासशील देशों के संदर्भ में)`:\n- An increase in national income in **Developed Nations `(વિકસિત દેશો / विकसित देश)`** (like USA, UK, Germany, Japan) is termed **Economic Growth**, because their basic economic systems and infrastructure are already fully mature.\n- An increase in national income in **Developing Nations `(વિકાસશીલ દેશો / विकासशील देश)`** (like India, Brazil, South Africa) is termed **Economic Development**, because it builds new institutions and eradicates poverty and backwardness.",
        "difficulty": "Intermediate",
        "bloom": "Analyze"
    })

    blocks.append({
        "type": "diagram",
        "content": "Comparison Matrix: Economic Growth (Quantitative, Numerical GDP rise, Mature economies) vs Economic Development (Qualitative, Structural Shift, Standard of Living, Developing economies).",
        "image_url": "assets/images/gseb_ss_ch15_growth_vs_development.jpg",
        "alt_text": "Comparison chart showing Economic Growth as a smaller subset of broader Economic Development."
    })

    blocks.append({
        "type": "memory_trick",
        "content": "🧠 **Growth vs Development Memory Formula:**\n- **Development = D = Deep / Discovery / Qualitative / Developing Nations / First Stage (Seed grows into a tree).**\n- **Growth = G = Giant numbers / Quantitative / Developed Nations / Outcome (Tree producing more leaves).**",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "mcq",
        "content": "Which of the following statements correctly differentiates Economic Development from Economic Growth?",
        "options": [
            "Economic Growth is qualitative, while Economic Development is purely quantitative.",
            "Economic Development is the first stage and qualitative, while Economic Growth is quantitative and the outcome.",
            "Economic Growth occurs only in developing nations, while Economic Development occurs in developed nations.",
            "Both terms are identical with no economic distinction."
        ],
        "correct_answer": "Economic Development is the first stage and qualitative, while Economic Growth is quantitative and the outcome.",
        "explanation": "Economic Development is a qualitative first-stage process involving structural reforms and improved standard of living, whereas Economic Growth is a quantitative result.",
        "distractor_rationale": "Option A reverses the definitions; Option C reverses developed and developing nations; Option D incorrectly claims they are identical."
    })

    # =========================================================================
    # MODULE 3: CHARACTERISTICS OF A DEVELOPING ECONOMY (9 PILLARS)
    # =========================================================================
    blocks.append({
        "type": "theory",
        "content": "### 🌐 Characteristics of a Developing Economy `(વિકાસશીલ અર્થતંત્રના લક્ષણો / विकासशील अर्थव्यवस्था के लक्षण)`\n\nAccording to the **World Bank's 2004 World Development Report `(વિશ્વ બેંકનો 2004નો અહેવાલ / विश्व बैंक की विकास रिपोर्ट 2004)`**, countries having a Per Capita Income of **less than $735 (US Dollars)** are categorized as **Developing Economies `(વિકાસશીલ અર્થતંત્ર / विकासशील अर्थव्यवस्था)`**.\n\nA developing economy exhibits **9 distinct characteristics**:\n\n1. **Low Per Capita Income `(નીચી માથાદીઠ આવક / कम प्रति व्यक्ति आय)`:**\n   - High population growth rate combined with modest national income keeps the per capita income low. Consequently, the standard of living of people remains poor.\n\n2. **High Population Growth `(વસ્તી વૃદ્ધિ / जनसंख्या वृद्धि)`:**\n   - In developing nations, the population growth rate is very high—typically **2% or more per year `(2% કે તેથી વધુ / 2% या उससे अधिक)`**.\n\n3. **Dependence on Agriculture `(ખેતી પર નિર્ભરતા / कृषि पर निर्भरता)`:**\n   - Agriculture is the primary occupation. More than **60% of the total population** depends on agriculture for employment, and agriculture contributes approximately **26% to the National Income**.\n\n4. **Unequal Distribution of Income `(આવકની અસમાન વહેંચણી / आय का असमान वितरण)`:**\n   - Severe disparity exists between the affluent and the impoverished. The **top 20% richest population** garners about **40% of national income**, while the **bottom 20% poorest population** receives a mere **10% of national income**.\n\n5. **High Unemployment `(બેરોજગારીનું ઊંચું પ્રમાણ / उच्च बेरोजगारी)`:**\n   - Unemployment accounts for more than **3% of the total labour force**. Prevalent forms include:\n     - **Seasonal Unemployment `(મોસમી બેરોજગારી / मौसमी बेरोजगारी)`:** Farmers remain idle during non-farming seasons (3 to 5 months).\n     - **Disguised / Hidden Unemployment `(પ્રચ્છન્ન બેરોજગારી / छिपी हुई बेरोजगारी)`:** More laborers work on a farm than needed; removing extra workers does not reduce total output.\n     - **Structural Unemployment `(માળખાગત બેરોજગારી / संरचनात्मक बेरोजगारी)`:** Caused by backward social structures and obsolete technologies.\n\n6. **Widespread Poverty `(ગરીબી / गरीबी)`:**\n   - Nearly **one-third (approx. 30%) of the total population** lives below the poverty line, unable to secure basic physiological needs like food, clothing, shelter, education, and healthcare.\n\n7. **Dual Economy `(દ્વિમુખી અર્થતંત્ર / दोहरी अर्थव्यवस्था)`:**\n   - Coexistence of two contrasting socioeconomic structures:\n     - *Rural/Backward Sector:* Primitive farming, bullock carts, obsolete tools, illiteracy, and orthodox traditions.\n     - *Urban/Modern Sector:* Advanced factories, computerized services, luxury lifestyles, and modern transportation.\n\n8. **Inadequate Basic Infrastructure `(પાયાની સેવાઓનો અભાવ / बुनियादी सुविधाओं का अभाव)`:**\n   - Critical shortage of electricity `(વીજળી / बिजली)`, paved roads, public transport, modern communication `(સંદેશાવ્યવહાર / संचार)`, tap water, hospitals, and banking networks.\n\n9. **Deficit in Foreign Trade `(વિદેશ વેપારનું સ્વરૂપ અને ખાધ / विदेशी व्यापार का घाटा)`:**\n   - Developing nations export primary agricultural crops, raw minerals, and handicrafts at low international prices, while importing expensive manufactured industrial equipment, vehicles, and petroleum, creating an adverse balance of trade and ballooning **Foreign Debt `(વિદેશી દેવું / विदेशी ऋण)`**.",
        "difficulty": "Advanced",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "diagram",
        "content": "The 9 Characteristics of a Developing Economy: Low Income, Population Surge (>2%), Agriculture (>60%), Disparity, Unemployment (>3%), Poverty (1/3rd), Dual Economy, Infrastructure Deficit, and Trade Imbalance.",
        "image_url": "assets/images/gseb_ss_ch15_developing_characteristics.jpg",
        "alt_text": "Infographic depicting the 9 hallmarks of developing nations with icons for agriculture, poverty, population, and dual economy."
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Super-Mnemonic for 9 Characteristics (Board Exam 4-Marker Guarantee!):** \nRemember the acronym: **P-A-D-P-U-P-I-F-D**\n- **P** ➔ **P**er capita income is low (< $735)\n- **A** ➔ **A**griculture dependence (>60% workforce)\n- **D** ➔ **D**ual Economy (Bullock carts in villages vs Metro trains in cities)\n- **P** ➔ **P**opulation growth (>2% per year)\n- **U** ➔ **U**nequal income distribution (Top 20% have 40% income)\n- **P** ➔ **P**overty (1/3rd population)\n- **I** ➔ **I**nfrastructure inadequacy (Power, Transport, Health)\n- **F** ➔ **F**oreign trade deficit\n- **D** ➔ **D**isguised / Structural Unemployment (>3%)",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "mcq",
        "content": "According to the World Bank's 2004 World Development Report, what is the Per Capita Income benchmark for classifying a nation as a developing economy?",
        "options": [
            "Less than $735",
            "Less than $1,500",
            "Less than $250",
            "Less than $5,000"
        ],
        "correct_answer": "Less than $735",
        "explanation": "The World Bank 2004 report categorized countries with a Per Capita Income below $735 as developing nations.",
        "distractor_rationale": "Values like $1,500 or $5,000 belong to middle-income brackets; $735 is the exact figure mentioned in the GSEB textbook."
    })

    blocks.append({
        "type": "mcq",
        "content": "What is the phenomenon where more workers are engaged in an agricultural field than actually needed, such that removing some does not reduce total output?",
        "options": [
            "Seasonal Unemployment",
            "Disguised / Hidden Unemployment",
            "Industrial Unemployment",
            "Frictional Unemployment"
        ],
        "correct_answer": "Disguised / Hidden Unemployment",
        "explanation": "Disguised unemployment (પ્રચ્છન્ન બેરોજગારી) occurs when excess workers contribute zero marginal productivity, typical in Indian agriculture.",
        "distractor_rationale": "Seasonal unemployment is tied to off-season periods; Industrial unemployment occurs due to technological changes in factories."
    })

    # =========================================================================
    # MODULE 4: ECONOMIC ACTIVITIES VS NON-ECONOMIC ACTIVITIES
    # =========================================================================
    blocks.append({
        "type": "theory",
        "content": "### 💼 Economic Activities vs Non-Economic Activities\n\nAll human activities conducted in daily life can be categorized into two distinct groups based on their underlying **intention and monetary motive `(આર્થિક ઉદ્દેશ / मौद्रिक उद्देश्य)`**:\n\n| Feature | Economic Activity `(આર્થિક પ્રવૃત્તિ / आर्थिक गतिविधि)` | Non-Economic Activity `(બિન-આર્થિક પ્રવૃત્તિ / गैर-आर्थिक गतिविधि)` |\n| :--- | :--- | :--- |\n| **Definition** | An activity performed with the intention of earning income, obtaining monetary return, or acquiring goods and services `(નાણાકીય વળતર મેળવવાના હેતુથી થતી પ્રવૃત્તિ)` | An activity performed without any aim of monetary reward or financial benefit `(નાણાકીય વળતર કે આવક મેળવવાનો ઉદ્દેશ ન હોય)` |\n| **Driving Motive** | Profit, salary, wages, monetary gain `(નફો, પગાર, આવક)` | Love, affection, compassion, moral duty, patriotism, social service `(પ્રેમ, દયા, લાગણી, સામાજિક સેવા)` |\n| **Core Real-Life Examples** | - A farmer cultivating crops for sale in the market `(ખેડૂત દ્વારા અનાજનું ઉત્પાદન)`<br>- A doctor treating patients in his private clinic `(ડૉક્ટર દ્વારા દર્દીની સારવાર)`<br>- A teacher teaching in a school for salary `(શિક્ષકનું અધ્યાપન કાર્ય)`<br>- A carpenter crafting furniture for customers | - A mother nursing and cooking food for her own children `(માતા દ્વારા બાળકનો ઉછેર)`<br>- A social worker distributing food packets to flood victims `(પૂરપીડિતોની સેવા)`<br>- Voluntary blood donation `(રક્તદાન)`<br>- Helping an elderly visually-impaired person cross a busy road |",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "diagram",
        "content": "Economic Activity (Doctor charging clinic fee / Farmer selling produce) vs Non-Economic Activity (Mother caring for her child / Social worker serving humanity).",
        "image_url": "assets/images/gseb_ss_ch15_economic_vs_noneconomic.jpg",
        "alt_text": "Split diagram showing paid economic work on the left and selfless social work on the right."
    })

    blocks.append({
        "type": "mcq",
        "content": "A mother raising and nurturing her child is classified under which type of human activity?",
        "options": [
            "Economic Activity",
            "Non-Economic Activity",
            "Secondary Sector Activity",
            "Commercial Activity"
        ],
        "correct_answer": "Non-Economic Activity",
        "explanation": "A mother's care is driven by pure love and affection with zero monetary motive, making it a Non-Economic Activity.",
        "distractor_rationale": "Economic and commercial activities involve financial transactions and remuneration, which are absent in maternal care."
    })

    # =========================================================================
    # MODULE 5: STRUCTURE OF INDIAN ECONOMY (THREE SECTORS)
    # =========================================================================
    blocks.append({
        "type": "theory",
        "content": "### 🏭 Structure of the Economy: The Three Pillars\n\nEconomic activities in any country are classified into **three broad sectors `(અર્થતંત્રના ત્રણ ક્ષેત્રો / अर्थव्यवस्था के तीन क्षेत्र)`**:\n\n```\n                                THE ECONOMY\n                                     │\n        ┌────────────────────────────┼────────────────────────────┐\n        ▼                            ▼                            ▼\n  PRIMARY SECTOR              SECONDARY SECTOR              SERVICE SECTOR\n (Direct Nature)           (Manufacturing/Industry)     (Support & Intangibles)\n  • Agriculture              • Small & Large Factories    • Banking & Insurance\n  • Animal Husbandry         • Construction               • Transport & Telecom\n  • Fisheries & Poultry      • Electricity & Gas          • Education & Health\n  • Mining & Forestry        • From Pin to Aeroplane      • Tourism & IT\n```\n\n#### 1. Primary Sector `(પ્રાથમિક ક્ષેત્ર / प्राथमिक क्षेत्र)`:\n- Consists of activities directly dependent on **nature and natural resources**.\n- *Key Activities:* Agriculture `(ખેતી / कृषि)`, Animal Husbandry `(પશુપાલન / पशुपालन)`, Cattle breeding, Poultry farming `(મરઘા-બતકાં ઉછેર / मुर्गी पालन)`, Fisheries `(મત્સ્ય ઉદ્યોગ / मत्स्य पालन)`, Forestry / collection of forest produce `(વન્ય પેદાશો / वन उत्पाद)`, and extraction of raw minerals `(કાચી ધાતુઓનું ખોદકામ / कच्ची धातुओं का खनन)`.\n\n#### 2. Secondary Sector / Industrial Sector `(માધ્યમિક અથવા ઉદ્યોગ ક્ષેત્ર / द्वितीयक क्षेत्र)`:\n- Consists of activities that transform raw materials produced by nature into finished, usable consumer goods through manual labor and machinery.\n- *Key Activities:* Small-scale cottage industries `(લઘુ ઉદ્યોગો / लघु उद्योग)`, heavy industrial factories `(મોટા કારખાના / बड़े उद्योग)`, Construction industry `(બાંધકામ ઉદ્યોગ / निर्माण उद्योग)`, Electricity, Gas, and Water supply.\n- *Scope:* Produces everything from a **small safety pin `(ટાંકણી / छोटी पिन)`** to gigantic **aeroplanes, ships, and satellites `(વિમાન અને જહાજ / विशालकाय विमान)`**.\n\n#### 3. Service Sector / Tertiary Sector `(સેવા ક્ષેત્ર / તૃતીયક ક્ષેત્ર / सेवा क्षेत्र)`:\n- Does not produce tangible physical goods directly, but provides essential support services to the Primary and Secondary sectors, as well as to society at large.\n- *Key Activities:* Trade and Commerce `(વેપાર / व्यापार)`, Transportation `(વાહનવ્યવહાર / परिवहन)`, Telecommunication `(સંદેશાવ્યવહાર / संचार)`, Banking and Insurance `(બેંકિંગ અને વીમો / बैंकिंग और बीमा)`, Education `(શિક્ષણ / शिक्षा)`, Healthcare `(આરોગ્ય / स्वास्थ्य)`, Tourism and Hospitality `(પ્રવાસન / पर्यटन)`.\n\n#### 📈 Structural Transition Dynamics during Economic Development:\n- In developing nations like India, the **Primary Sector initially dominates** in both employment and national income contribution.\n- As economic development accelerates, the **relative share of the Primary sector declines**, while the shares of the **Secondary (Industrial) and Service sectors steadily increase**.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "diagram",
        "content": "The Interconnected Economic Web: Primary Sector provides raw materials ➔ Secondary Sector manufactures finished goods ➔ Service Sector transports, finances, and markets them.",
        "image_url": "assets/images/gseb_ss_ch15_three_sectors.jpg",
        "alt_text": "Flowchart showing raw cotton from primary sector moving to textile mill in secondary sector and being sold via retail and banking in service sector."
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Board Exam Classification Hack:**\n- If it comes **directly out of the earth/nature** (Crops, Fish, Milk, Wood, Ore) ➔ **Primary Sector**\n- If it was **made/processed in a workshop or factory** (Sugar, Cloth, Cement, Car, Steel) ➔ **Secondary Sector**\n- If it is an **intangible service, connection, or knowledge** (Doctor, Teacher, Bus, Bank, 5G Internet) ➔ **Service Sector**",
        "difficulty": "Beginner",
        "bloom": "Apply"
    })

    blocks.append({
        "type": "mcq",
        "content": "Which sector includes activities like Banking, Insurance, Education, and Transportation?",
        "options": [
            "Primary Sector",
            "Secondary Sector",
            "Service Sector (Tertiary Sector)",
            "Agricultural Sector"
        ],
        "correct_answer": "Service Sector (Tertiary Sector)",
        "explanation": "Banking, insurance, education, and transport do not produce physical goods; they offer support services, falling under the Service Sector.",
        "distractor_rationale": "Primary sector covers raw extraction (farming, fishing); Secondary sector covers manufacturing and construction."
    })

    # =========================================================================
    # MODULE 6: FACTORS OF PRODUCTION & THEIR REWARDS (4 PILLARS)
    # =========================================================================
    blocks.append({
        "type": "theory",
        "content": "### 🧱 The 4 Factors of Production `(ઉત્પાદનના સાધનો / उत्पादन के चार साधन)`\n\nProduction is the creative process of combining raw resources to create utility goods and services that satisfy human wants. In economics, all productive resources are categorized into **4 essential Factors of Production**:\n\n$$\\text{Total Production} = \\text{Land} + \\text{Capital} + \\text{Labour} + \\text{Entrepreneur}$$\n\n| Factor of Production | Economic Definition & Scope | Reward / Remuneration `(વળતર / प्रतिफल)` |\n| :--- | :--- | :--- |\n| **1. Land `(જમીન / भूमि)`** | In economics, Land does not merely mean the topsoil. It encompasses **ALL natural resources** provided freely by nature: fertile soil, forests, rivers, oceans, mountains, mineral deposits, sunlight, and air. | **Rent `(ભાડું / लगान - किराया)`** |\n| **2. Capital `(મૂડી / पूंजी)`** | Includes all **man-made physical assets and wealth** utilized in the production process: machinery, tractors, industrial tools, factory buildings, transport vehicles, and financial capital. | **Interest `(વ્યાજ / ब्याज)`** |\n| **3. Labour `(શ્રમ / श्रम)`** | Any **physical or mental human effort** undertaken with the specific objective of earning monetary remuneration. Labour is a living, perishable factor that cannot be stored. (e.g., agricultural laborers, carpenters, engineers, accountants). | **Wages / Salary `(વેતન / મહેનતાણું / मजदूरी - वेतन)`** |\n| **4. Entrepreneur / Organizer `(નિયોજક / સંયોજક / उद्यमी - आयोजक)`** | The visionary person or enterprise that efficiently coordinates and combines the other three factors (Land, Capital, Labour) and courageously bears the **ultimate risk of profit or loss** in business. | **Profit `(નફો / लाभ - मुनाफा)`** |",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "diagram",
        "content": "The Factors of Production Circle: Land earns Rent, Capital earns Interest, Labour earns Wages, and Entrepreneur earns Profit.",
        "image_url": "assets/images/gseb_ss_ch15_factors_of_production.jpg",
        "alt_text": "Visual wheel linking the four factors of production with their respective economic returns."
    })

    blocks.append({
        "type": "memory_trick",
        "content": "🧠 **Memory Match for Factors and Rewards:**\n- **L**and ➔ **R**ent `(જમીન ➔ ભાડું)`\n- **C**apital ➔ **I**nterest `(મૂડી ➔ વ્યાજ)`\n- **L**abour ➔ **W**ages `(શ્રમ ➔ વેતન)`\n- **E**ntrepreneur ➔ **P**rofit `(નિયોજક ➔ નફો)`\n\n*Shortcut: **LCLE** earns **RIWP**!*",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "mcq",
        "content": "What is the economic reward (remuneration) earned by an Entrepreneur for organizing production and bearing business risk?",
        "options": [
            "Rent",
            "Interest",
            "Wages",
            "Profit"
        ],
        "correct_answer": "Profit",
        "explanation": "An Entrepreneur coordinates land, capital, and labor, bearing commercial risk in return for Profit.",
        "distractor_rationale": "Rent is the reward for Land; Interest is for Capital; Wages are for Labour."
    })

    # =========================================================================
    # MODULE 7: ALLOCATION OF RESOURCES (4 FUNDAMENTAL CONSIDERATIONS)
    # =========================================================================
    blocks.append({
        "type": "theory",
        "content": "### 🎯 Allocation of Factors of Production `(સાધનોની ફાળવણી / साधनों का आवंटन)`\n\nEvery household, business, and government on Earth faces a universal economic dilemma: **Human wants are endless, but the resources to satisfy them are limited!** \n\nTherefore, every economy must make careful choices when allocating factors of production, guided by **4 fundamental principles**:\n\n#### 1. Unlimited Wants `(અમર્યાદિત જરૂરિયાતો / असीमित आवश्यकताएं)`:\n- Human desires are boundless and recurring. Satisfying one desire immediately gives birth to multiple new desires.\n- Technological progress, social competition, and lifestyle aspirations continuously create new needs (e.g., from basic feature phone to 5G smartphone to laptop).\n\n#### 2. Priority Order in Wants `(જરૂરિયાતોમાં અગ્રતાક્રમ / आवश्यकताओं में प्राथमिकता क्रम)`:\n- Because resources are scarce, an individual and a society must prioritize urgent needs over luxury desires.\n- *Example:* A nation must first allocate funds for food security, primary education, and emergency healthcare before building luxury golf courses or amusement parks.\n\n#### 3. Limited Resources `(મર્યાદિત સાધનો / सीमित संसाधन)`:\n- Natural resources (fertile land, fossil fuels, fresh water) and capital assets (machinery, finance) are strictly finite and limited in supply.\n\n#### 4. Alternative Uses of Resources `(સાધનોના વૈકલ્પિક ઉપયોગો / साधनों के वैकल्पिक उपयोग)`:\n- Most productive resources can be put to more than one use, but using a resource for one specific purpose means sacrificing its other potential uses!\n- *Example:* If a 10-acre plot of fertile land is used to cultivate **Wheat `(ઘઉં / गेहूँ)`**, it cannot simultaneously be used to grow **Cotton `(કપાસ / कपास)`** or build a manufacturing plant. Choosing one alternative means giving up the other.",
        "difficulty": "Intermediate",
        "bloom": "Analyze"
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Real-World Thought Experiment:** Imagine your parents give you ₹500 pocket money. You want to buy a textbook (₹300), watch a movie (₹250), and eat a pizza (₹200). You cannot satisfy all three! You must rank your priorities. That is the exact economic problem of **Resource Allocation** faced by entire nations!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "mcq",
        "content": "Why does the economic problem of allocating resources arise in all nations?",
        "options": [
            "Because resources are unlimited and human wants are few.",
            "Because human wants are unlimited while productive resources are limited and have alternative uses.",
            "Because governments prohibit the production of consumer goods.",
            "Because money has no purchasing power in modern markets."
        ],
        "correct_answer": "Because human wants are unlimited while productive resources are limited and have alternative uses.",
        "explanation": "The fundamental economic problem stems from the scarcity of resources with alternative uses facing infinite human wants.",
        "distractor_rationale": "Option A is factually opposite; Options C and D are completely incorrect assumptions."
    })

    # =========================================================================
    # MODULE 8: ECONOMIC SYSTEMS (MARKET, SOCIALIST, AND MIXED ECONOMY)
    # =========================================================================
    blocks.append({
        "type": "theory",
        "content": "### 🏛️ Methods of Allocating Resources: The 3 Economic Systems\n\nAcross world history, nations have adopted three primary economic systems to organize production and distribute goods:\n\n```\n                             ECONOMIC SYSTEMS\n                                     │\n        ┌────────────────────────────┼────────────────────────────┐\n        ▼                            ▼                            ▼\n  MARKET SYSTEM               SOCIALIST SYSTEM              MIXED ECONOMY\n(Capitalist / Free)           (Command / State)         (Public + Private)\n  • Private Ownership          • State/Public Ownership    • Coexistence of Both\n  • Profit Motive              • Social Welfare Motive     • Heavy Sector: Public\n  • Price Mechanism            • Central Planning          • Consumer Sector: Private\n  • Consumer Sovereignty       • Zero Monopolies           • India, France, UK\n  • USA, Japan                 • Russia, China (Past)      • Controlled Economy\n```\n\n---\n\n### 🏢 1. Market System / Capitalist System `(બજાર પદ્ધતિ / મુક્ત અર્થતંત્ર / बाजार प्रणाली)`\n- **Ownership:** Factors of production are owned privately by individuals and private corporations.\n- **Driving Force:** **Profit `(નફો / लाभ)`** is the supreme motivating factor behind all production and investments.\n- **Price Mechanism `(ભાવતંત્ર / કિંમત પદ્ધતિ / मूल्य तंत्र)`:** Prices of commodities and services are determined automatically by free market forces of **Demand and Supply** (Adam Smith's 'Invisible Hand').\n- **Consumer Sovereignty `(ગ્રાહકનું સાર્વભૌમત્વ / उपभोक्ता की संप्रभुता)`:** The consumer is King. Producers manufacture only what consumers demand.\n- **State Role:** Zero direct government interference in economic affairs (*Laissez-faire*).\n- *Examples:* **USA `(અમેરિકા)`**, **Japan `(જાપાન)`**, **Germany `(જર્મની)`**, **UK `(ઇંગ્લેન્ડ)`**.\n- **Merits `(લાભ / गुण)`:** High efficiency, intense competition boosts product quality, rapid technological innovation, freedom of enterprise.\n- **Demerits / Limitations `(ગેરલાભ / ખામીઓ / दोष)`:**\n  1. Emergence of private **Monopolies `(ઈજારાશાહી / एकाधिकार)`** leading to consumer exploitation.\n  2. Extreme widening of **Income Inequality `(આવકની અસમાનતા / आय की असमानता)`** (rich become richer, poor become poorer).\n  3. Neglect of public welfare, environment, and basic goods in pursuit of maximum luxury profits.\n\n---\n\n### 🚩 2. Socialist System / Command Economy `(સમાજવાદી પદ્ધતિ / समाजवादी प्रणाली)`\n- **Ownership:** All factors of production, land, factories, and resources are **owned exclusively by the State / Government `(રાજ્ય / સરકાર / राज्य का स्वामित्व)`**.\n- **Driving Force:** **Social Welfare `(સમાજ કલ્યાણ / જાહેર હિત / सामाजिक कल्याण)`**, not personal profit.\n- **Central Planning `(કેન્દ્રીય આયોજન / केंद्रीय नियोजन)`:** All decisions regarding what to produce, how much to produce, and at what price are dictated by the State's Central Planning Authority.\n- *Examples:* **Russia (former USSR) `(રશિયા)`**, **China `(ચીન)`** (historically).\n- **Merits `(લાભ / गुण)`:** Production focuses on essential public needs; eliminates private monopolies; reduces income disparity; eliminates exploitation of workers.\n- **Demerits / Limitations `(ગેરલાભ / ખામીઓ / दोष)`:**\n  1. **Lack of Individual Freedom `(વ્યક્તિગત સ્વાતંત્ર્યનો અભાવ / व्यक्तिगत स्वतंत्रता का अभाव)`** for consumers and entrepreneurs.\n  2. Absence of profit incentive often leads to **lethargy, inefficiency, and lack of innovation**.\n  3. **Bureaucratic Red Tape `(અમલદારશાહીનું નિયંત્રણ / लालफीताशाही)`** and delays in execution.\n\n---\n\n### 🤝 3. Mixed Economy `(મિશ્ર અર્થતંત્ર / मिश्रित अर्थव्यवस्था)`\n- **The Golden Synthesis:** Combines the merits of both the Market System and the Socialist System while minimizing their defects!\n- **Coexistence of Public and Private Sectors `(જાહેર અને ખાનગી ક્ષેત્રનું સહઅસ્તિત્વ / सार्वजनिक और निजी क्षेत्र का सह-अस्तित्व)`**:\n  - *Public Sector (Government Owned):* Strategic and heavy industries—Defense and weapons `(સંરક્ષણ / रक्षा)`, Railways `(રેલવે / रेलवे)`, Atomic Energy `(અણુ ઊર્જા / परमाणु ऊर्जा)`, Heavy steel plants, Electricity generation, and major public infrastructure.\n  - *Private Sector (Individual Owned):* Consumer goods, Agriculture `(ખેતી / कृषि)`, Small and Medium Scale Enterprises, Retail Trade, and Hospitality.\n- **Economic Planning & Controlled Framework `(નિયંત્રિત અર્થતંત્ર / नियंत्रित अर्थव्यवस्था)`:** The government uses tax incentives, industrial licensing, and subsidies to guide private investment toward national welfare and curb harmful monopolies.\n- *Examples:* **India `(ભારત / भारत)`**, **France `(ફ્રાન્સ)`**, **England `(ઇંગ્લેન્ડ)`**.\n- **Challenges:** Economic instability, bureaucratic delays in project clearance, and coordination gaps between public and private enterprises.",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    blocks.append({
        "type": "diagram",
        "content": "The Three Economic Systems Matrix: Market System (Private + Profit), Socialist System (Government + Social Welfare), and Mixed Economy (Coexistence + Balanced Growth).",
        "image_url": "assets/images/gseb_ss_ch15_economic_systems_matrix.jpg",
        "alt_text": "Comparative diagram illustrating the three economic models with their ownership, motives, and country examples."
    })

    blocks.append({
        "type": "mcq",
        "content": "Which economic system is characterized by the coexistence of both Public and Private sectors, as practiced in India?",
        "options": [
            "Pure Market System",
            "Pure Socialist System",
            "Mixed Economy (મિશ્ર અર્થતંત્ર)",
            "Feudal Economy"
        ],
        "correct_answer": "Mixed Economy (મિશ્ર અર્થતંત્ર)",
        "explanation": "India operates as a Mixed Economy where the public sector manages strategic heavy industries while the private sector manages consumer goods and agriculture.",
        "distractor_rationale": "Pure Market system has no public sector; Pure Socialist system has no private sector."
    })

    blocks.append({
        "type": "mcq",
        "content": "In a Pure Market System (Capitalist Economy), what serves as the supreme driving force behind all economic decisions?",
        "options": [
            "Social Welfare",
            "Profit Motive (નફો)",
            "Government Directives",
            "Equal Income Distribution"
        ],
        "correct_answer": "Profit Motive (નફો)",
        "explanation": "In a market system, private entrepreneurs invest and produce purely to maximize monetary profit.",
        "distractor_rationale": "Social welfare and government directives drive the socialist system; equal distribution is an objective of socialism."
    })

    # =========================================================================
    # MODULE 9: CULTURAL INTEGRATION & ANCIENT INDIAN ECONOMIC WISDOM
    # =========================================================================
    blocks.append({
        "type": "theory",
        "content": "### 🇮🇳 Timeless Indian Economic Wisdom: Kautilya's Arthashastra\n\nLong before modern European economists debated capitalism and socialism, ancient India possessed a sophisticated understanding of holistic wealth creation and governance:\n\n- **The Four Purusharthas `(ચાર પુરુષાર્થ / चार पुरुषार्थ)`:** Indian philosophy identifies four pillars of human life: **Dharma `(ધર્મ - Righteous Conduct)`**, **Artha `(અર્થ - Material Wealth & Economic Livelihood)`**, **Kama `(કામ - Fulfillment of Desires)`**, and **Moksha `(મોક્ષ - Spiritual Liberation)`**.\n- **Kautilya's Arthashastra (300 BCE) `(કૌટિલ્યનું અર્થશાસ્ત્ર / कौटिल्य का अर्थशास्त्र)`:** Acharya Chanakya declared:\n  > *\"सुखस्य मूलं धर्मः, धर्मस्य मूलमर्थः, अर्थस्य मूलं राज्यम्...\"*\n  > *(The root of human happiness is righteousness/Dharma; the root of Dharma is ethical wealth creation/Artha; the root of wealth is good governance/State).* \n- **The Ancient Science of 'Varta' `(વાર્તા વિદ્યા / वार्ता विद्या)`:** In Vedic texts, the economic science encompassing **Agriculture `(કૃષિ / कृषि)`**, **Cattle Rearing `(પશુપાલન / पशुपालन)`**, and **Trade `(વાણિજ્ય / व्यापार)`** was termed *Varta*. Without Varta, a nation cannot survive.\n- **Sustainable Prosperity `(સર્વે ભવન્તુ સુખિનઃ / સર્વજન હિતાય)`:** Ancient Indian economic philosophy always championed ethical wealth generation where private enterprise coexists with social dharma—the spiritual ancestor of India's modern **Mixed Economy**!",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    # =========================================================================
    # MODULE 10: BOARD EXAM MASTERY (PYQS, HOTS & SCORING BLUEPRINTS)
    # =========================================================================
    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM TOP SCORING SECRETS (Super-HOTS & Marking Schemes):**\n\n### 📌 1. Long Answer (4 Marks): 'Explain the Characteristics of a Developing Economy.'\n- **Winning Answer Blueprint:**\n  1. *Introduction:* Mention World Bank 2004 Report benchmark (Per Capita Income < $735).\n  2. *9 Points with Subheadings & Key Data:* Low Per Capita Income, High Population Growth (>2%), Agriculture Dominance (>60% workforce, 26% GDP), Dual Economy (bullock carts vs modern cities), Unemployment (>3%, Disguised & Seasonal), Unequal Income Distribution (Top 20% hold 40%, Bottom 20% hold 10%), Poverty (approx 30%), Infrastructure Shortage, Foreign Trade Deficit.\n  3. *Conclusion:* Note that India is rapidly transitioning with expanding manufacturing and service sectors.\n\n### 📌 2. Comparison Question (3 Marks): 'Differentiate between Market System and Socialist System.'\n- *Draw a neat 3-column table with parameters:* Ownership of Resources, Central Motive (Profit vs Social Welfare), Price Determination (Price Mechanism vs Government Planning), Consumer Freedom, and Country Examples.\n\n### 📌 3. Conceptual Distinction (2 Marks): 'Economic Growth vs Economic Development.'\n- *Points:* Qualitative vs Quantitative, First Stage vs Result, Technology Shift vs Land Expansion, Developing Nations vs Developed Nations.\n\n### 📌 4. High-Yield 1-Marker Traps:\n- Per Capita Income threshold for developing nations ➔ **< $735 (World Bank 2004)**\n- Primary sector workforce share in developing countries ➔ **> 60%**\n- Coexistence of bullock cart agriculture and modern industries ➔ **Dual Economy `(દ્વિમુખી અર્થતંત્ર)`**\n- Reward of Entrepreneur ➔ **Profit `(નફો)`**\n- India's economic system ➔ **Mixed Economy `(મિશ્ર અર્થતંત્ર)`**",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    blocks.append({
        "type": "reflection",
        "content": "🤔 **Socratic Thought Challenge:** \nIf a billionaire opens 10 new software factories in a city, the GDP of the country will instantly rise (Economic Growth). But if the nearby village still lacks clean drinking water, schools, and hospitals, has true **Economic Development** occurred? As a future citizen and leader, how will you ensure that economic growth translates into real development for every citizen?",
        "difficulty": "Advanced",
        "bloom": "Create"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }

    # Save to GSEB Class 10 Social Science Chapter 15
    gseb_out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_social_science_ch15.json"
    os.makedirs(os.path.dirname(gseb_out_path), exist_ok=True)
    with open(gseb_out_path, "w", encoding="utf-8") as f:
        json.dump(final_json, f, indent=2, ensure_ascii=False)
    print(f"Generated GSEB Chapter at: {gseb_out_path}")

    # Also save to NCERT Class 10 Social Science Chapter 15 for multi-curriculum synchronization
    ncert_out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_social_science_ch15.json"
    final_json_ncert = dict(final_json)
    final_json_ncert["metadata"] = dict(final_json["metadata"])
    final_json_ncert["metadata"]["id"] = "ncert_class10_social_science_ch15"
    with open(ncert_out_path, "w", encoding="utf-8") as f:
        json.dump(final_json_ncert, f, indent=2, ensure_ascii=False)
    print(f"Generated NCERT Chapter at: {ncert_out_path}")

if __name__ == "__main__":
    generate_supreme_gseb_ss_ch15()
