import json
import os

def generate_supreme_gseb_ss_ch16():
    chapter_id = "gseb_class10_social_science_ch16"
    title = "Chapter 16: Economic Liberalization and Globalization"
    
    metadata = {
        "id": chapter_id,
        "title": title,
        "subtitle": "The Ultimate Board Exam Mastery & Conceptual Discovery Guide",
        "subject": "Social Science",
        "grade": "10",
        "board": "GSEB/NCERT",
        "curriculum": ["GSEB", "NCERT", "CBSE", "Universal"],
        "language": "English/Hindi/Gujarati (Bilingual)",
        "difficulty": "Advanced",
        "estimated_minutes": 180,
        "version": "3.0.0-SUPREME-PEDAGOGY",
        "author": "Shine Academy Chief Academic Architect",
        "reviewed_by": "Chief Academic Architect & Board Examination Committee",
        "last_updated": "2026-08-16",
        "tags": [
            "economics",
            "social_science",
            "liberalization",
            "privatization",
            "globalization",
            "lpg_reforms_1991",
            "wto",
            "sustainable_development",
            "environment_protection",
            "gseb_class10",
            "board_special",
            "bilingual"
        ],
        "learning_outcomes": [
            "Understand the historical backdrop and financial crisis of 1991 that necessitated the New Economic Policy (NEP).",
            "Master the three foundational pillars of economic reform: Liberalization, Privatization, and Globalization (LPG).",
            "Analyze the advantages, limitations, and real-world socioeconomic impacts of Liberalization and Privatization on Indian enterprise.",
            "Evaluate the multifaceted role of Multinational Corporations (MNCs) and Foreign Direct Investment (FDI) in accelerating Globalization.",
            "Explain the establishment, objectives, functions, and direct consequences of the World Trade Organization (WTO) for India.",
            "Formulate actionable strategies for Sustainable Development to balance industrial growth with ecological equilibrium.",
            "Summarize national and international legal frameworks for Environmental Protection from the Stockholm Conference to contemporary India."
        ],
        "ai_context": {
            "learning_goal": "Transform high school learners from rote memorizers into astute economic thinkers. Guide them through the 1991 financial crisis, show how market reforms revolutionized everyday life, evaluate the trade-offs of globalization, and connect economic expansion with environmental stewardship.",
            "common_misconceptions": [
                "Students often believe Liberalization means zero government regulations. (Fact: It means removing unnecessary licenses and red tape, while maintaining essential regulatory standards).",
                "Students confuse Privatization with Disinvestment. (Fact: Disinvestment is one of the specific financial methods used to achieve Privatization).",
                "Students assume Globalization only benefits developing nations or only harms them. (Fact: It is a double-edged sword offering technological access and export markets while creating stiff competition for cottage industries).",
                "Students think WTO dictates Indian laws. (Fact: WTO provides a multilateral negotiating framework and dispute resolution platform based on treaty consensus)."
            ],
            "tutor_hint": "Use the story of India's 1991 gold airlift to hook students on the urgency of reforms. Contrast the pre-1991 'waiting list for a landline telephone' with today's smartphone revolution to make LPG concepts tangible.",
            "next_topics": [
                "gseb_class10_social_science_ch17",
                "gseb_class10_social_science_ch18"
            ]
        }
    }
    
    blocks = []
    
    # =========================================================================
    # MODULE 1: THE DRAMATIC 1991 CRISIS & THE BIRTH OF LPG REFORMS
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "Imagine waking up one morning to learn that your country has only enough foreign money left to pay for **two weeks** of essential food, petrol `(पेट्रोल / પેટ્રોલ)`, and medicine imports! In July 1991, India faced a catastrophic financial crisis `(वित्तीय संकट / નાણાકીય કટોકટી)`. Our foreign exchange reserves `(विदेशी मुद्रा भंडार / વિદેશી હૂંડિયામણ ભંડાર)` dried up to barely $1.2 billion. To avoid national bankruptcy, India had to physically pledge and airlift **47 tonnes of gold bullion** to the Bank of England and Union Bank of Switzerland as emergency collateral! \n\nHow did our nation rise like a phoenix from the brink of total collapse to become one of the fastest-growing major economies on the planet? Welcome to the incredible story of the **New Economic Policy of 1991 (नई आर्थिक नीति 1991 / નવી આર્થિક નીતિ 1991)** and the revolutionary trio: **Liberalization, Privatization, and Globalization (LPG)**!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "### 📊 The 1991 Economic Turning Point (LPG Architecture)\n```\n                    ┌─────────────────────────────────────────┐\n                    │  1991 BALANCE OF PAYMENTS CRISIS        │\n                    │  (Severe Forex Depletion & Fiscal Debt) │\n                    └────────────────────┬────────────────────┘\n                                         │\n                                         ▼\n                    ┌─────────────────────────────────────────┐\n                    │    NEW ECONOMIC POLICY (NEP) - JULY 1991│\n                    │   (Under PM Narasimha Rao & FM Manmohan)│\n                    └────────────────────┬────────────────────┘\n                                         │\n        ┌────────────────────────────────┼────────────────────────────────┐\n        │                                │                                │\n        ▼                                ▼                                ▼\n┌──────────────────────┐ ┌──────────────────────┐ ┌──────────────────────┐\n│   LIBERALIZATION     │ │    PRIVATIZATION     │ │    GLOBALIZATION     │\n│ (उदारीकरण / ઉદારીકરણ)│ │  (निजीकरण / ખાનગીકરણ) │ │(वैश्वीकरण / વૈશ્વિકીકરણ)│\n│                      │ │                      │ │                      │\n│ • Abolish License Raj│ │ • Disinvestment      │ │ • Reduce Import Duty │\n│ • Ease Production Cap│ │ • De-reservation     │ │ • Attract FDI & MNCs │\n│ • Free Pricing Policy│ │ • Private Management │ │ • Open Foreign Trade │\n└──────────────────────┘ └──────────────────────┘ └──────────────────────┘\n```",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "theory",
        "content": "### 🏛️ The Historic Need for Economic Reforms\nAfter gaining independence in 1947, India adopted a **Mixed Economy `(मिश्रित अर्थव्यवस्था / મિશ્ર અર્થતંત્ર)`** model with an overwhelming emphasis on state-controlled planning. The government built heavy public sector enterprises, while the private sector was tightly shackled under a web of permits, quotas, and bureaucracy known as the **'License-Permit Raj' `(लाइसेंस राज / લાયસન્સ રાજ)`**.\n\nBy 1990-1991, several structural flaws brought the economy to its knees:\n1. **Severe Fiscal Deficit `(राजकोषीय घाटा / રાજકોષીય ખાધ)`:** Government expenditures drastically outpaced revenues due to inefficient public enterprises and heavy subsidies.\n2. **Adverse Balance of Payments `(प्रतिकूल भुगतान संतुलन / પ્રતિકૂળ ચૂકવણી સંતુલન)`:** Imports (especially crude oil during the Gulf War) skyrocketed while exports remained sluggish.\n3. **Exhaustion of Foreign Exchange Reserves `(विदेशी मुद्रा भंडार का संकट / વિદેશી હૂંડિયામણ ભંડારનું સંકટ)`:** Reserves sank to a critical low, barely adequate for 14 days of imports.\n4. **High Inflation `(मुद्रास्फीति / ફુગાવો - ભાવવધારો)`:** Double-digit price hikes crippled household purchasing power.\n\nIn July 1991, Prime Minister P.V. Narasimha Rao and Finance Minister Dr. Manmohan Singh ushered in sweeping structural adjustment programmes `(संरचनात्मक सुधार / માળખાકીય સુધારાઓ)` backed by the World Bank and the International Monetary Fund (IMF) `(अंतर्राष्ट्रीय मुद्रा कोष / આંતરરાષ્ટ્રીય ચલણ ભંડોળ)`. This historic policy framework became known as the **LPG Model**.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "ai_tutor_prompt",
        "content": "### 🧠 Quick Concept Check\nWhy was the Indian government forced to introduce the New Economic Policy in July 1991?",
        "options": [
            "Due to an acute shortage of foreign exchange reserves and unsustainable balance of payments deficit.",
            "Because the United Nations ordered all Asian nations to close down public factories.",
            "To completely ban foreign trade and close all international borders.",
            "Because Indian private companies were earning too much profit."
        ],
        "correct_answer": "Due to an acute shortage of foreign exchange reserves and unsustainable balance of payments deficit.",
        "explanation": "In 1991, India's foreign exchange reserves plummeted to approximately $1.2 billion (barely enough for two weeks of imports), compelling the government to seek IMF/World Bank assistance and introduce comprehensive structural reforms.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    # =========================================================================
    # MODULE 2: PILLAR 1 — ECONOMIC LIBERALIZATION (ઉદારીકરણ)
    # =========================================================================
    blocks.append({
        "type": "theory",
        "content": "### 🔓 What is Economic Liberalization `(आर्थिक उदारीकरण / આર્થિક ઉદારીકરણ)`?\n**Economic Liberalization** refers to the systematic relaxation and gradual dismantling of rigid government controls, excessive bureaucratic restrictions `(लालफीताशाही / લાલફીતાશાહી)`, licensing regulations, and trade barriers to foster open market competition and empower private entrepreneurship `(निजी उद्यमशीलता / ખાનગી સાહસિકતા)`.\n\n#### 🔑 Major Steps Undertaken Under Liberalization in India:\n1. **Abolition of Industrial Licensing `(औद्योगिक लाइसेंसिंग की समाप्ति / ઔદ્યોગિક લાયસન્સિંગની નાબૂદી)`:** Mandatory government licenses were scrapped for almost all industries, except a few sensitive sectors (such as defense equipment, atomic energy, hazardous chemicals, and alcoholic beverages).\n2. **Relaxation of MRTP Act `(एमआरटीपी अधिनियम में ढील / એમઆરટીપી એક્ટમાં છૂટછાટ)`:** The *Monopolies and Restrictive Trade Practices Act* was overhauled to allow business groups to expand production capacity, merge, and establish new units without endless bureaucratic permissions.\n3. **Freedom to Import Capital Goods & Technology `(पूंजीगत वस्तुओं और प्रौद्योगिकी का मुक्त आयात / મૂડીગત ચીજો અને ટેકનોલોજીની મુક્ત આયાત)`:** Indian manufacturers were permitted to import modern foreign machinery and advanced technologies freely.\n4. **Deregulation of Interest Rates & Financial Markets `(वित्तीय बाजार का विनियमन / નાણાકીય બજારનું ડિરેગ્યુલેશન)`:** Banks and non-banking financial institutions gained operational flexibility in setting interest rates and managing loans.\n5. **Tax Reforms `(कर सुधार / કરવેરા સુધારણા)`:** Rationalization and lowering of corporate taxes, customs duties, and excise taxes to encourage voluntary tax compliance.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "diagram",
        "content": "### ⚖️ Balance Sheet of Liberalization: Advantages vs Limitations\n\n| Parameters | 🌟 Advantages (લાભ / फायदे) | ⚠️ Limitations (ખામીઓ / सीमाएं) |\n| :--- | :--- | :--- |\n| **Industrial Growth** | Surge in private investment, boost in industrial production & GDP growth rate. | Monopolistic dominance of large corporate conglomerates; neglect of small cottage industries. |\n| **Consumer Welfare** | Abundant product choices, superior international quality, competitive market pricing. | Excessive production of luxury consumer goods rather than mass essential welfare goods. |\n| **Foreign Trade** | Massive increase in exports, accumulation of healthy foreign exchange reserves. | Widening trade deficit during initial import surge; foreign debt vulnerabilities. |\n| **Employment** | Modern service sector boom (IT, telecom, banking, logistics). | Neglect of the agricultural sector `(कृषि क्षेत्र की उपेक्षा / કૃષિ ક્ષેત્રની ઉપેક્ષા)` where 60%+ population depended. |",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Teacher's Master Insight for Board Exams:**\nWhen writing answers on Liberalization, never say 'the government stopped controlling everything'. Use the precise academic phrasing: *'The government transitioned from being a direct owner/controller (नियंत्रक / નિયંત્રક) to a facilitator and regulator (सुविधा प्रदाता और नियामक / સુવિધા પ્રદાતા અને નિયામક)'*.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HIGH-FREQUENCY QUESTION (3 Marks):**\n*\"Explain any three major advantages and two limitations of Economic Liberalization in India.\"*\n\n**Answer Structure Blueprint:**\n- **Definition:** Define liberalization as the gradual removal of government restrictions on private enterprise.\n- **Advantages (Any 3):** \n  1. Rapid increase in industrial output and private capital formation.\n  2. Expansion of global export competitiveness and foreign currency reserves.\n  3. Wide variety of superior-quality goods available to domestic consumers at competitive prices.\n- **Limitations (Any 2):**\n  1. Relative neglect of agriculture, leading to rural-urban economic disparity.\n  2. Emergence of private monopolies and concentration of wealth in select corporate groups.",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    # =========================================================================
    # MODULE 3: PILLAR 2 — PRIVATIZATION (ખાનગીકરણ)
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "Think back to the 1980s: If you wanted a landline phone connection from the government telecom department, you had to register and wait for **5 to 7 years**! Today, private telecom giants provide high-speed 5G connectivity and digital streaming instantly at your doorstep. What changed the game? **Privatization `(निजीकरण / ખાનગીકરણ)`**!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "theory",
        "content": "### 🏢 What is Privatization `(निजीकरण / ખાનગીકરણ)`?\n**Privatization** is the strategic process of transferring the ownership, management, equity, and operational control of state-owned Public Sector Enterprises (PSEs) `(सार्वजनिक क्षेत्र के उपक्रम / જાહેર ક્ષેત્રના એકમો)` to private entrepreneurs and corporate entities.\n\n#### 🛠️ Three Primary Methods of Privatization in India:\n1. **De-reservation of Public Sector `(सार्वजनिक क्षेत्र का अनारक्षण / જાહેર ક્ષેત્રનું બિન-અનામતકરણ)`:** Opening up industries that were previously exclusive government monopolies (like aviation, mining, power generation, and telecommunications) to private enterprises.\n2. **Disinvestment `(विनिवेश / વિનિવેશ)`:** The government sells a portion or majority of its equity shares in public sector undertakings to private companies, mutual funds, or the general public (e.g., selling stakes in Maruti Udyog, VSNL, Air India).\n3. **Transfer of Management Control `(प्रबंधन का हस्तांतरण / સંચાલનનું હસ્તાંતરણ)`:** The government retains ownership of the underlying assets but contracts out day-to-day management and operations to experienced private corporations (Public-Private Partnership / PPP model).",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "diagram",
        "content": "### 🔄 The Three Channels of Privatization\n```\n                          ┌─────────────────────────────────────┐\n                          │    PRIVATIZATION METHODS IN INDIA   │\n                          └──────────────────┬──────────────────┘\n                                             │\n            ┌────────────────────────────────┼────────────────────────────────┐\n            │                                │                                │\n            ▼                                ▼                                ▼\n┌────────────────────────┐       ┌────────────────────────┐       ┌────────────────────────┐\n│     DE-RESERVATION     │       │     DISINVESTMENT      │       │  MANAGEMENT HANDOVER   │\n│ (બિન-અનામતકરણ / अनारक्षण)│       │  (વિનિવેશ / विनिवेश)   │       │(સંચાલન સોંપણી / प्रबंधन)│\n│                        │       │                        │       │                        │\n│ Private firms entered  │       │ Govt sells PSU shares  │       │ Govt retains ownership │\n│ Airlines, Telecom,     │       │ to public & private    │       │ but private team runs  │\n│ Banking & Power sectors│       │ corporate buyers       │       │ day-to-day operations  │\n└────────────────────────┘       └────────────────────────┘       └────────────────────────┘\n```",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "theory",
        "content": "### ⚖️ Benefits and Drawbacks of Privatization\n\n#### 🌟 Major Benefits:\n- **Enhanced Operating Efficiency `(कार्यकुशलता में सुधार / કાર્યક્ષમતામાં સુધારો)`:** Private companies operate on profit motive, customer satisfaction, accountability, and merit-based performance, eliminating red-tape sluggishness.\n- **Technological Upgradation `(आधुनिक तकनीक का समावेश / આધુનિક ટેકનોલોજીનો સમાવેશ)`:** Private capital infuses world-class machinery, automation, and digital management systems.\n- **Reduction in Fiscal Burden `(सरकारी वित्तीय बोझ में कमी / સરકારી નાણાકીય બોજમાં ઘટાડો)`:** Disinvestment proceeds generate non-debt capital revenue for the state treasury, while loss-making public enterprises cease draining taxpayer funds.\n\n#### ⚠️ Critical Drawbacks & Societal Concerns:\n- **Concentration of Economic Wealth `(आर्थिक सत्ता का केंद्रीकरण / આર્થિક સત્તાનું કેન્દ્રીકરણ)`:** Strategic public assets can get concentrated in the hands of a few dominant industrial houses.\n- **Neglect of Social Welfare & Public Service `(सामाजिक कल्याण की उपेक्षा / સામાજિક કલ્યાણની ઉપેક્ષા)`:** Private firms avoid non-profitable remote rural areas and focus solely on high-margin urban markets.\n- **Fear of Layoffs and Job Insecurity `(रोजगार असुरक्षा और छंटनी / નોકરીની અસુરક્ષા અને છટણી)`:** Rationalization and corporate restructuring frequently lead to workforce reductions.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    blocks.append({
        "type": "common_mistakes",
        "content": "⚠️ **COMMON EXAM PITFALL:**\nDo not confuse **Liberalization** with **Privatization**!\n- **Liberalization:** Freeing businesses from unnecessary rules, quotas, and licensing hurdles (Rule change).\n- **Privatization:** Shifting ownership and management of state-owned enterprises into private corporate hands (Ownership change).",
        "difficulty": "Intermediate",
        "bloom": "Analyze"
    })

    blocks.append({
        "type": "ai_tutor_prompt",
        "content": "### 🧠 Concept Mastery Question\nWhen the government sells a 26% or 51% stake of its public sector enterprise (PSE) to private investors on the stock exchange, what is this process specifically termed as?",
        "options": [
            "Disinvestment (विनिवेश / વિનિવેશ)",
            "Nationalization (राष्ट्रीयकरण / રાષ્ટ્રીયકરણ)",
            "Subsidization (राजसहायता / સબસિડીકરણ)",
            "Demonetization (विमुद्रीकरण / નોટબંધી)"
        ],
        "correct_answer": "Disinvestment (विनिवेश / વિનિવેશ)",
        "explanation": "Disinvestment is the dilution or sale of government equity holdings in public sector undertakings to private corporate entities or the public.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    # =========================================================================
    # MODULE 4: PILLAR 3 — GLOBALIZATION (વૈશ્વિકીકરણ)
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "Look at the shoes on your feet, the automobile driving past your window, or the Korean web series streaming on your phone. Cotton grown by a farmer in Surendranagar `(સુરેન્દ્રનગર)` may be woven into denim in Ahmedabad, styled by designers in Paris, stitched in Vietnam, and sold across London! This interconnected web is the reality of **Globalization `(वैश्वीकरण / વૈશ્વિકીકરણ)`**.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "theory",
        "content": "### 🌐 What is Globalization `(वैश्वीकरण / વૈશ્વિકીકરણ)`?\n**Globalization** is the seamless integration of a domestic country's economy with the global economy, allowing unhindered, borderless movement of **goods, services, capital, technology, and human labour `(वस्तुएं, सेवाएं, पूंजी, प्रौद्योगिकी और श्रम / ચીજવસ્તુઓ, સેવાઓ, મૂડી, ટેકનોલોજી અને શ્રમ)`** across international boundaries.\n\n#### 🚢 Core Policy Measures Implemented for Globalization in India:\n1. **Reduction in Customs Tariffs `(आयात-निर्यात प्रशुल्क में भारी कटौती / કસ્ટમ્સ ડ્યુટીમાં ઘટાડો)`:** Import duties on raw materials, electronics, and industrial components were scaled down drastically to match world levels.\n2. **Elimination of Quantitative Restrictions `(मात्रात्मक प्रतिबंधों की समाप्ति / આયાત ક્વોટાની નાબૂદી)`:** Quantitative import quotas `(आयात कोटा / આયાત ક્વોટા)` on manufactured and consumer items were phased out.\n3. **Encouragement to Foreign Direct Investment (FDI) `(प्रत्यक्ष विदेशी निवेश को प्रोत्साहन / પ્રત્યક્ષ વિદેશી રોકાણને પ્રોત્સાહન)`:** Automatic FDI clearance routes up to 51%, 74%, or 100% were introduced across automobiles, pharmaceuticals, telecommunications, and retail.\n4. **Current Account Convertibility of Rupee `(रुपये की परिवर्तनीयता / રૂપિયાની પરિવર્તનક્ષમતા)`:** Full convertibility of the Indian Rupee on current account transactions for trade and business travel.\n5. **Special Economic Zones (SEZs) `(विशेष आर्थिक क्षेत्र / વિશેષ આર્થિક ક્ષેત્ર)`:** Creation of duty-free manufacturing hubs with tax holidays and world-class infrastructure to power export-oriented industries.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "theory",
        "content": "### 🏢 The Engines of Globalization: Multinational Corporations (MNCs)\n**Multinational Corporations (MNCs) `(बहुराष्ट्रीय कंपनियां / બહુરાષ્ટ્રીય કંપનીઓ)`** are mega enterprises that own, manage, and control production facilities in more than one nation (e.g., Apple, Samsung, Tata Motors, Toyota, Unilever).\n\n#### Why do MNCs setup global operations?\n- To manufacture goods where raw materials and labor are cheapest, minimizing production cost.\n- To access vast consumer markets and bypass local transportation bottlenecks.\n- To harness specialized regional engineering and software talent (such as India's IT hubs in Bengaluru, Hyderabad, and Pune).\n\n#### ⚖️ Impact of Globalization on India:\n- **Positive Impacts (હકારાત્મક અસરો / सकारात्मक प्रभाव):** Massive surge in foreign capital investments; phenomenal boom in IT, software, and BPO service exports; access to state-of-the-art consumer goods at affordable price points; large-scale employment creation in urban tertiary sectors.\n- **Negative Impacts (નકારાત્મક અસરો / नकारात्मक प्रभाव):** Unforgiving competition forced many indigenous cottage, artisan, and small-scale industries `(कुटीर एवं लघु उद्योग / કુટીર અને લઘુ ઉદ્યોગો)` to shut down; growing economic inequality between skilled urban professionals and unskilled rural workforce; vulnerability to global financial contagions.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HIGH-FREQUENCY TOPIC (3 Marks):**\n*\"Explain the effects of Globalization on Indian Cottage and Small-Scale Industries.\"*\n\n**Key Points to Score Full Marks:**\n1. Cottage and village industries lacked automated machinery, modern marketing networks, and massive capital.\n2. Influx of cheaper, machine-finished, and aesthetically appealing mass-produced goods from MNCs captured domestic market share.\n3. Many traditional handicraft, handloom, clay pottery, and brass metal workshops suffered severe revenue decline and distress closures.",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    # =========================================================================
    # MODULE 5: WORLD TRADE ORGANIZATION (WTO / વિશ્વ વ્યાપાર સંગઠન)
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "If two sovereign countries get into a fierce tariff dispute over mango exports, textile taxes, or software royalties, who acts as the supreme international court to arbitrate and resolve their fight? That global referee is the **World Trade Organization (WTO) `(विश्व व्यापार संगठन / વિશ્વ વ્યાપાર સંગઠન)`**!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "theory",
        "content": "### 🏛️ Establishment & Profile of WTO\n- **Date of Establishment:** **1st January 1995**\n- **Predecessor Organization:** Replaced the **GATT** (*General Agreement on Tariffs and Trade* `(गैट / ગેટ)` - formed in 1948).\n- **Headquarters:** **Geneva, Switzerland `(जिनेवा, स्विट्जरलैंड / જિનીવા, સ્વિટ્ઝર્લૅન્ડ)`**\n- **India's Status:** India is one of the founding charter members of the WTO.\n\n#### 🎯 Four Primary Objectives of WTO `(विश्व व्यापार संगठन के उद्देश्य / વિશ્વ વ્યાપાર સંગઠનના ઉદ્દેશો)`:\n1. **Eliminate International Trade Barriers `(व्यापार बाधाओं को दूर करना / આંતરરાષ્ટ્રીય વ્યાપારના અવરોધો દૂર કરવા)`:** To progressively dismantle tariffs, duties, and quota restrictions on cross-border trade.\n2. **Promote Free and Fair Multilateral Trade `(मुक्त एवं निष्पक्ष व्यापार को बढ़ावा देना / મુક્ત અને ન્યાયી વ્યાપારને પ્રોત્સાહન)`:** To establish legally binding, non-discriminatory international trade conventions for all member states.\n3. **Optimal Utilization of World Resources `(वैश्विक संसाधनों का इष्टतम उपयोग / વિશ્વના સંસાધનોનો શ્રેષ્ઠ ઉપયોગ)`:** To expand the production and exchange of goods while ensuring sustainable economic growth.\n4. **Amicable Settlement of Trade Disputes `(व्यापार विवादों का शांतिपूर्ण समाधान / વ્યાપારી વિવાદોનું નિવારણ)`:** To act as an impartial international forum for resolving trade conflicts and reviewing national trade policies.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "diagram",
        "content": "### 🌐 WTO Overview & Operational Matrix\n```\n┌─────────────────────────────────────────────────────────────────────────┐\n│                     WORLD TRADE ORGANIZATION (WTO)                      │\n│                Established: 1 Jan 1995 | HQ: Geneva, Switzerland        │\n└────────────────────────────────────┬────────────────────────────────────┘\n                                     │\n      ┌──────────────────────────────┼──────────────────────────────┐\n      │                              │                              │\n      ▼                              ▼                              ▼\n┌──────────────────────────┐ ┌──────────────────────────┐ ┌──────────────────────────┐\n│   TRADE RULEMAKING       │ │    DISPUTE SETTLEMENT    │ │    MONITORING POLICIES   │\n│ Multilateral agreements  │ │ Binding arbitration panel│ │ Periodic Trade Policy    │\n│ on Goods (GATT), Services│ │ resolves cross-border    │ │ Reviews (TPRM) to prevent│\n│ (GATS) & Patents (TRIPS) │ │ tariff & export disputes │ │ protectionist barriers   │\n└──────────────────────────┘ └──────────────────────────┘ └──────────────────────────┘\n```",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "theory",
        "content": "### 🇮🇳 What Has Been the Impact of WTO on India?\n\n#### 📈 Opportunities & Gains for India:\n- **Export Expansion:** Lower tariff barriers globally allowed Indian garments, gems and jewelry, chemicals, spices, and IT services to penetrate worldwide markets effortlessly.\n- **Global Integration:** India's share in global international merchandise and services trade rose significantly from 0.5% in 1991 to nearly 2% in recent decades.\n- **Foreign Investment Influx:** Clear multilateral rules boosted investor confidence, spurring record inflows of FDI into Indian manufacturing and service sectors.\n\n#### 📉 Challenges & Disadvantages for India:\n- **Agricultural Subsidies Disparity `(कृषि सब्सिडी विवाद / કૃષિ સબસિડી વિવાદ)`:** Developed countries (USA, EU) grant massive financial subsidies to their domestic farmers while pressuring developing nations like India to reduce minimum support prices (MSP) and farm input subsidies.\n- **Patent Regime & TRIPS `(बौद्धिक संपदा कानून और दवाइयां / પેટન્ટ કાયદો - ટ્રીપ્સ)`:** Strict intellectual property rules have raised the prices of patented life-saving pharmaceutical drugs and seeds, posing challenges for affordable healthcare and small farmers.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    blocks.append({
        "type": "ai_tutor_prompt",
        "content": "### 🧠 Quick Concept Check on WTO\nWhere is the headquarters of the World Trade Organization (WTO) situated?",
        "options": [
            "Geneva, Switzerland (जिनेवा, स्विट्जरलैंड / જિનીવા, સ્વિટ્ઝર્લૅન્ડ)",
            "New York, USA (न्यूयॉर्क, अमेरिका / ન્યૂયોર્ક, અમેરિકા)",
            "Paris, France (पेरिस, फ्रांस / પેરિસ, ફ્રાન્સ)",
            "Tokyo, Japan (टोक्यो, जापान / ટોક્યો, જાપાન)"
        ],
        "correct_answer": "Geneva, Switzerland (जिनेवा, स्विट्जरलैंड / જિનીવા, સ્વિટ્ઝર્લૅન્ડ)",
        "explanation": "The World Trade Organization (WTO) was founded on 1st January 1995 with its permanent global headquarters in Geneva, Switzerland.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    # =========================================================================
    # MODULE 6: SUSTAINABLE DEVELOPMENT (ટકાઉ / સુપોષિત વિકાસ)
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "*\"The Earth provides enough to satisfy every man's needs, but not every man's greed.\"* — Mahatma Gandhi.\n\nIf we cut down all pristine forests to build factories today, exhaust all underground water reserves `(भूजल भंडार / ભૂગર્ભ જળ ભંડાર)`, and burn all fossil fuels `(जीवाश्म ईंधन / અશ્મિભૂત બળતણ)` for quick profits, what will our children and future generations inherit? Empty deserts and toxic air! How do we grow rich without destroying the planet? The answer is **Sustainable Development `(सतत विकास / ટકાઉ અથવા સુપોષિત વિકાસ)`**.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "theory",
        "content": "### 🌱 Definition of Sustainable Development `(सतत विकास / સુપોષિત વિકાસ)`\nAccording to the famous Brundtland Commission Report (1987):\n> **\"Sustainable Development is development that meets the needs of the present generation without compromising the ability of future generations to meet their own needs.\"**\n\nIt demands a harmonious synthesis between **Economic Growth `(आर्थिक विकास / આર્થિક વિકાસ)`**, **Social Equity `(सामाजिक समानता / સામાજિક સમાનતા)`**, and **Environmental Conservation `(पर्यावरण संरक्षण / પર્યાવરણ સંરક્ષણ)`**.\n\n#### 🧭 Five Strategic Pillars for Sustainable Development:\n1. **Prudent Utilization of Natural Resources `(प्राकृतिक संसाधनों का विवेकपूर्ण उपयोग / કુદરતી સંસાધનોનો વિવેકપૂર્ણ ઉપયોગ)`:** Differentiate between renewable resources (soil, forests, water) and non-renewable resources (coal, petroleum, mineral ores), strictly optimizing their extraction rates.\n2. **Shift Toward Non-Conventional Renewable Energy `(गैर-पारंपरिक ऊर्जा स्रोतों का उपयोग / બિન-પરંપરાગત ઊર્જા સ્ત્રોતોનો ઉપયોગ)`:** Rapidly transition from fossil fuel thermal power plants to solar power `(सौर ऊर्जा / સૌર ઊર્જા)`, wind energy `(पवन ऊर्जा / પવન ઊર્જા)`, hydro-electricity, and bio-gas `(बायोगैस / બાયોગેસ)`.\n3. **Adoption of 3R Principles & Waste Management `(पुनर्चक्रण एवं अपशिष्ट प्रबंधन / રિસાઈકલિંગ અને કચરા વ્યવસ્થાપન)`:** Implement *Reduce, Reuse, and Recycle* across industrial effluents, domestic sewage, plastic packaging, and e-waste.\n4. **Eco-Friendly Agricultural Practices `(पर्यावरण-अनुकूल कृषि पद्धतियां / પર્યાવરણ-અનુકૂળ કૃષિ પદ્ધતિઓ)`:** Shift from toxic chemical fertilizers and pesticides to organic farming `(जैविक खेती / જૈવિક ખેતી)`, bio-fertilizers, crop rotation, and precision drip irrigation `(टपक सिंचाई / ટપક સિંચાઈ)`.\n5. **Strict Pollution Control & Green Audits `(कठोर प्रदूषण नियंत्रण कानून / કડક પ્રદૂષણ નિયંત્રણ નિયમો)`:** Impose mandatory effluent treatment plants (ETP) for chemical factories, implement carbon emission taxes, and penalize toxic dumping into rivers.",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    blocks.append({
        "type": "diagram",
        "content": "### ♻️ The Golden Triangle of Sustainability\n```\n                             ┌─────────────────────────┐\n                             │   SUSTAINABLE DEVELOPMENT│\n                             │   (ટકાઉ / સુપોષિત વિકાસ) │\n                             └────────────┬────────────┘\n                                          │\n             ┌────────────────────────────┼────────────────────────────┐\n             │                            │                            │\n             ▼                            ▼                            ▼\n┌─────────────────────────┐  ┌─────────────────────────┐  ┌─────────────────────────┐\n│     ECONOMIC VIABILITY  │  │      SOCIAL EQUITY      │  │  ECOLOGICAL INTEGRITY   │\n│ • Industrial Innovation │  │ • Eradicate Poverty     │  │ • Zero Carbon Emissions │\n│ • Resource Efficiency   │  │ • Universal Healthcare  │  │ • Afforestation Drives  │\n│ • Clean Tech Jobs       │  │ • Inter-generational    │  │ • Solar & Wind Energy   │\n│                         │  │   Fairness              │  │ • Rainwater Harvesting  │\n└─────────────────────────┘  └─────────────────────────┘  └─────────────────────────┘\n```",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Mnemonics Trick to Ace Sustainable Strategies in Exams:**\nRemember **S-O-L-A-R**:\n- **S**olar & Wind Renewable Energy adoption\n- **O**ptimum and prudent resource extraction\n- **L**aws and strict industrial pollution penalties\n- **A**griculture with organic fertilizers & drip irrigation\n- **R**ecycle, Reuse, and Reduce waste management",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    # =========================================================================
    # MODULE 7: ENVIRONMENTAL PROTECTION & GLOBAL INITIATIVES (પર્યાવરણ સુરક્ષા)
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "Did you know that clouds carrying sulfur dioxide emitted from industrial smokestacks in one country can precipitate as toxic acid rain `(अम्लीय वर्षा / એસિડ વર્ષા)` hundreds of kilometers away in another country? Nature recognizes no national passports! That is why environmental defense demands united global action.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "theory",
        "content": "### 🌍 Landmark International Environmental Milestones\n1. **Stockholm Conference (1972) `(स्टॉकहोम सम्मेलन 1972 / સ્ટોકહોમ પરિષદ 1972)`:** The United Nations convened the first landmark conference on the Human Environment in Stockholm, Sweden, to sound the global alarm on environmental degradation `(पर्यावरणीय क्षरण / પર્યાવરણીય અધોગતિ)`.\n2. **World Environment Day `(विश्व पर्यावरण दिवस / વિશ્વ પર્યાવરણ દિવસ)`:** To commemorate the Stockholm Conference, **5th June** `(5 जून / 5 જૂન)` was designated as World Environment Day, celebrated annually across the globe.\n3. **Earth Summit at Rio de Janeiro (1992) `(रियो पृथ्वी सम्मेलन 1992 / રિયો પૃથ્વી પરિષદ 1992)`:** Over 170 nations assembled in Brazil to sign the historic **Agenda 21**, setting comprehensive targets for biodiversity preservation, climate stabilization, and sustainable forestry.\n\n#### 🇮🇳 Proactive Measures Implemented by the Government of India:\n- **Constitutional Commitment:** Under Article 48A and 51A(g), environmental protection was made a fundamental duty of every citizen and state policy.\n- **Establishment of Pollution Control Boards:** Formation of the **Central Pollution Control Board (CPCB) `(केंद्रीय प्रदूषण नियंत्रण बोर्ड / કેન્દ્રીય પ્રદૂષણ નિયંત્રણ બોર્ડ)`** and State Pollution Control Boards (GPCB in Gujarat) to monitor ambient air quality, water effluents, and industrial emissions.\n- **Environment Protection Act (1986) `(पर्यावरण संरक्षण अधिनियम 1986 / પર્યાવરણ સુરક્ષા કાયદો 1986)`:** Comprehensive umbrella legislation granting sweeping regulatory powers to close polluting industries and mandate Environmental Impact Assessments (EIA).\n- **Clean Energy & Transport Transitions:** Mandatory switch to Compressed Natural Gas (CNG) and Electric Vehicles (EVs) in metropolitan public transport; enforcement of stringent Bharat Stage VI (BS-VI) emission norms.\n- **Renewable Energy Expansion:** Launch of the National Solar Mission, Green Hydrogen initiatives, large-scale canal-top solar projects in Gujarat, and massive afforestation programs.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM OBJECTIVE HOTSPOTS (1 Mark Questions):**\n- **Question:** On which date is World Environment Day celebrated globally?\n  *Answer:* **5th June (5 જૂન / 5 जून)**.\n- **Question:** Where was the first Earth Summit held in 1992?\n  *Answer:* **Rio de Janeiro, Brazil (રિયો ડી જાનેરો, બ્રાઝિલ)**.\n- **Question:** What is the full form of CPCB?\n  *Answer:* **Central Pollution Control Board (કેન્દ્રીય પ્રદૂષણ નિયંત્રણ બોર્ડ)**.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    # =========================================================================
    # MODULE 8: BOARD EXAM MASTERY & HIGH ORDER THINKING SKILLS (HOTS)
    # =========================================================================
    blocks.append({
        "type": "board_questions",
        "content": "### 🎯 Complete Board Exam Mastery: Key Questions & Perfect Scoring Model\n\n#### ❓ Question 1 (2 Marks): Differentiate between Liberalization and Globalization.\n- **Liberalization:** Refers to the removal of unnecessary domestic rules, quotas, and licensing restrictions to foster freedom for private businesses within the country.\n- **Globalization:** Refers to integrating the domestic economy with the world economy through the unrestricted cross-border flow of goods, services, capital, and technology.\n\n#### ❓ Question 2 (3 Marks): State three objectives of the World Trade Organization (WTO).\n1. To eliminate tariffs and quantitative barriers in international commerce.\n2. To promote non-discriminatory, open multilateral trade among all member countries.\n3. To amicably arbitrate and settle international trade and commercial disputes.\n\n#### ❓ Question 3 (4 Marks / HOTS): \"Globalization has proven to be a mixed blessing for developing nations like India.\" Justify with balanced arguments.\n- **Gains:** Inflow of Foreign Direct Investment (FDI), modern technological advancements, boom in IT/BPO service exports, superior product quality and competitive pricing for consumers.\n- **Challenges:** Fierce market competition damaged unorganized cottage and small industries, created regional inequality, and heightened vulnerability to international economic crises.",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    blocks.append({
        "type": "summary",
        "content": "### 📝 Chapter 16 In a Nutshell: Master Revision Blueprint\n- **1991 Crisis:** Triggered by soaring fiscal deficits, balance of payments crisis, and forex reserves depleting to 14 days of imports.\n- **Liberalization (ઉદારીકરણ):** Abolished License Raj, relaxed MRTP restrictions, and freed industrial expansion and pricing.\n- **Privatization (ખાનગીકરણ):** De-reserved state monopolies, conducted disinvestment of PSU shares, and injected private management efficiency.\n- **Globalization (વૈશ્વિકીકરણ):** Slashed import tariffs, welcomed FDI and MNCs, boosted IT exports, but challenged local small-scale industries.\n- **WTO (વિશ્વ વ્યાપાર સંગઠન):** Founded on 1 Jan 1995 in Geneva to manage multilateral trade agreements and arbitrate global disputes.\n- **Sustainable Development (ટકાઉ વિકાસ):** Meeting present needs without compromising future generations via solar/wind power, 3R waste management, and organic farming.\n- **Environment Day:** Celebrated globally on **5th June** following the 1972 Stockholm Conference.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    # Save to GSEB destination
    gseb_out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_social_science_ch16.json"
    os.makedirs(os.path.dirname(gseb_out_path), exist_ok=True)
    with open(gseb_out_path, "w", encoding="utf-8") as f:
        json.dump(final_json, f, indent=2, ensure_ascii=False)
        
    # Also save to NCERT destination
    ncert_out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_social_science_ch16.json"
    final_json["metadata"]["id"] = "ncert_class10_social_science_ch16"
    final_json["metadata"]["board"] = "NCERT/CBSE/GSEB"
    with open(ncert_out_path, "w", encoding="utf-8") as f:
        json.dump(final_json, f, indent=2, ensure_ascii=False)
        
    print(f"Supreme GSEB SS Chapter 16 successfully generated at:\n - {gseb_out_path}\n - {ncert_out_path}")

if __name__ == "__main__":
    generate_supreme_gseb_ss_ch16()
