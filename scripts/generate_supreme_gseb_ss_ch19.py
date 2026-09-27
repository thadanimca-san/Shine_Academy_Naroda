import json
import os

def generate_supreme_gseb_ss_ch19():
    chapter_id = "gseb_class10_social_science_ch19"
    title = "Chapter 19: Human Development (માનવ વિકાસ / मानव विकास)"
    
    metadata = {
        "id": chapter_id,
        "title": title,
        "subtitle": "The Supreme Gold Standard Board Exam Mastery Guide - Human Capabilities, HDI & Women Empowerment",
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
            "human_development",
            "human_development_index",
            "hdi",
            "undp",
            "hdr",
            "life_expectancy_index",
            "education_index",
            "income_index",
            "gni_per_capita",
            "purchasing_power_parity",
            "amartya_sen",
            "mahbub_ul_haq",
            "four_pillars_of_hd",
            "health_challenges",
            "gender_equality",
            "sex_ratio",
            "women_empowerment",
            "beti_bachao_beti_padhao",
            "gujarat_schemes",
            "vidya_lakshmi_bond",
            "saraswati_sadhana_yojana",
            "chiranjeevi_yojana",
            "181_abhayam_helpline",
            "mission_mangalam",
            "board_special",
            "bilingual"
        ],
        "learning_outcomes": [
            "Define the concept of Human Development `(માનવ વિકાસનો અર્થ / मानव विकास का अर्थ)` and differentiate it clearly from mere Economic Growth `(આર્થિક વૃદ્ધિ / आर्थिक वृद्धि)`.",
            "Understand the Four Pillars of Human Development: Equality `(સમાનતા / समानता)`, Sustainability `(ટકાઉપણું / संधारणीयता)`, Productivity `(ઉત્પાદકતા / उत्पादकता)`, and Empowerment `(સશક્તિકરણ / सशक्तिकरण)`.",
            "Master the calculation methodology and three core dimensions of the Human Development Index (HDI) post-2010: Life Expectancy Index (LEI), Education Index (EI: MYS & EYS), and Income Index (II: GNI per capita in PPP $).",
            "Analyze the 4-tier classification of countries in the Human Development Report (HDR) and evaluate India's medium-tier position in relation to South Asian neighbors.",
            "Critically examine the major challenges to Human Development in India: Public Health, Declining Child Sex Ratio, and Gender Inequality.",
            "Describe the comprehensive national and Gujarat-specific welfare schemes for Women Empowerment (e.g., Beti Bachao Beti Padhao, Vidya Lakshmi Bond, Saraswati Sadhana Yojana, Chiranjeevi Yojana, and 181 Abhayam Helpline).",
            "Achieve top scores in GSEB and CBSE Board Exam questions through structured 4-mark essays, 2-mark distinction formulas, and high-yield objective traps."
        ],
        "ai_context": {
            "learning_goal": "Transform the student into a confident Board Exam topper in Social Science Chapter 19 by utilizing the 8-Step Socratic Discovery Cycle, high-yield comparative tables, mnemonic formulas, and precise bilingual terminology.",
            "common_misconceptions": [
                "Students often confuse Economic Growth (increase in GDP/national income) with Human Development (qualitative expansion of human choices, capabilities, health, education, and dignity).",
                "Students confuse the pre-2010 HDI indicators (Literacy rate, GDP per capita) with post-2010 revised indicators (Mean Years of Schooling, Expected Years of Schooling, GNI per capita in PPP $).",
                "Students mistakenly assume India falls in the 'High Human Development' tier because of rapid GDP growth, whereas India ranks in the 'Medium Human Development' tier (HDI 0.609, Rank 130 in HDR 2015).",
                "Students mix up the specific target age groups of Gujarat welfare schemes (e.g., Vidya Lakshmi Bond is for Class 1 girls in low literacy villages, while Saraswati Sadhana Yojana provides free bicycles to Class 9 secondary school girls)."
            ],
            "tutor_hint": "Anchor memory using core mnemonic pillars: Origin ➔ UNDP 1990 (Mahbub ul Haq & Amartya Sen); 3 Dimensions of HDI ➔ LEI (Max 83.6, Min 20), EI (MYS Max 13.3 + EYS Max 18), II (GNI PPP $ Max 75,000, Min 100); 4 HDI Tiers ➔ Very High (>=0.802, Norway #1), High (0.700-0.801, Sri Lanka #73), Medium (0.550-0.699, India #130), Low (<0.550, Niger #188); Gujarat Schemes ➔ 'V-S-C-A-M' (Vidya Lakshmi, Saraswati Sadhana, Chiranjeevi, Abhayam 181, Mission Mangalam)."
        }
    }

    blocks = []

    # =========================================================================
    # MODULE 1: HOOK & THE TRUE MEANING OF HUMAN DEVELOPMENT
    # =========================================================================
    blocks.append({
        "type": "hook",
        "title": "Wealthy Country vs Happy Citizens: What is True Progress?",
        "content": "Imagine two hypothetical countries:\n- **Country A** has glittering skyscrapers, millionaires, and skyrocketing industrial GDP, but its children suffer from malnutrition, girls are denied schooling, and hospitals lack basic medicines.\n- **Country B** has moderate wealth, but every child goes to a world-class school, citizens enjoy free healthcare, life expectancy is 85 years, and men and women enjoy equal dignity and opportunities.\n\nWhich country is truly developed? For decades, economists wrongly believed that mere **Economic Growth `(आर्थिक वृद्धि / આર્થિક વૃદ્ધિ)`** (money and machines) was enough. But visionary economists like **Nobel Laureate Amartya Sen `(अमर्त्य सेन / અમર્ત્ય સેન)`** and **Dr. Mahbub ul Haq `(महबूब उल हक / મહબૂબ ઉલ હક)`** proved that **Human Development `(मानव विकास / માનવ વિકાસ)`**—the quality, freedom, health, and dignity of human life—is the supreme goal of all civilization!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "diagram",
        "title": "Economic Growth vs Human Development Paradigm Shift",
        "content": "```\n      ┌────────────────────────────────────────────────────────┐\n      │               THE PARADIGM SHIFT IN ECONOMICS          │\n      └───────────────────────────┬────────────────────────────┘\n                                  │\n         ┌────────────────────────┴────────────────────────┐\n         ▼                                                 ▼\n┌────────────────────────────────┐       ┌────────────────────────────────┐\n│      ECONOMIC GROWTH           │       │       HUMAN DEVELOPMENT        │\n│  (आर्थिक वृद्धि / આર્થિક વૃદ્ધિ) │       │   (मानव विकास / માનવ વિકાસ)     │\n├────────────────────────────────┤       ├────────────────────────────────┤\n│ • Quantitative (संख्यात्मक)    │       │ • Qualitative (गुणात्मक)       │\n│ • Focus: Rise in GDP & Income  │       │ • Focus: Health, Knowledge,    │\n│ • Treats humans as a mere      │       │   Freedom, Dignity & Choices   │\n│   'Tool of Production'         │       │ • Treats human well-being as   │\n│ • Money is the End Goal        │       │   the Ultimate Goal (साध्य)    │\n└────────────────────────────────┘       └────────────────────────────────┘\n```\n*Human Development recognizes that Economic Growth is merely a Means `(साधन / સાધન)`, whereas Human Well-being is the Ultimate End `(साध्य / સાધ્ય)`.*",
        "image_url": "assets/images/ss_ch19_growth_vs_development.jpg",
        "alt_text": "Comparison chart showing Economic Growth as quantitative income vs Human Development as qualitative well-being."
    })

    blocks.append({
        "type": "theory",
        "title": "Meaning & Definition of Human Development (માનવ વિકાસનો અર્થ)",
        "content": "### 🌟 What is Human Development?\n\n**Human Development `(मानव विकास / માનવ વિકાસ)`** is not merely a rise in per capita income `(प्रति व्यक्ति आय / માથાદીઠ આવક)`. It is the holistic process of expanding people's freedoms, enlarging their choices, and enhancing their capabilities and living standards so that they can lead healthy, creative, and fulfilling lives with self-respect.\n\n---\n\n### 📖 Official Definition by UNDP (United Nations Development Programme):\n> *\"Human development is a process of enlarging people's choices and raising their level of well-being so that they can lead a long, healthy, meaningful, and creative life with dignity.\"*\n> \n> *(संयुक्त राष्ट्र विकास कार्यक्रम - UNDP के अनुसार: मानव विकास मानव की आकांक्षाओं और आवश्यक जीवन स्तर को विस्तारित करने की एक सतत प्रक्रिया है।)*\n\n---\n\n### 🎯 Core Objectives of Human Development:\n1. **Longevity & Health `(दीर्घायु और स्वस्थ जीवन / દીર્ઘાયુ અને તંદુરસ્ત જીવન)`:** Ensuring every individual enjoys a disease-free life with high life expectancy.\n2. **Knowledge & Education `(ज्ञान और शिक्षा / જ્ઞાન અને શિક્ષણ પ્રાપ્તિ)`:** Guaranteeing universal access to quality schooling, higher education, and vocational skills.\n3. **Decent Standard of Living `(सभ्य जीवन स्तर / સારો જીવનસ્તર)`:** Ensuring access to nutritious food, pure drinking water, hygienic shelter, and essential civic amenities.\n4. **Individual Freedom & Human Rights `(व्यक्तिगत स्वतंत्रता और मानवाधिकार / વ્યક્તિગત સ્વાતંત્ર્ય અને માનવ અધિકારો)`:** Eliminating discrimination based on gender, caste, religion, or economic status, and promoting active participation in democratic governance.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "theory",
        "title": "The Four Grand Pillars of Human Development (માનવ વિકાસના ચાર સ્તંભો)",
        "content": "Just as a majestic monument stands firmly on four solid foundation pillars, Human Development is supported by **Four Essential Pillars `(मानव विकास के चार स्तंभ / માનવ વિકાસના ચાર સ્તંભો)`**:\n\n---\n\n### 🏛️ 1. Equality `(समानता / સમાનતા)`:\n- Providing equal access to opportunities, resources, and public services to every person without any bias of gender `(लिंग / જાતિ)`, race `(जाति / જ્ઞાતિ)`, religion, or economic class.\n- Special focus on eliminating the gender gap `(लैंगिक असमानता / સ્ત્રી-પુરુષ અસમાનતા)`.\n\n### 🌿 2. Sustainability `(संधारणीयता - निरंतरता / ટકાઉપણું - સ્થિરતા)`:\n- Ensuring that opportunities and natural environmental resources are preserved for future generations `(भावी पीढ़ी / ભાવિ પેઢી)`.\n- Development today must not compromise the environmental and economic prospects of tomorrow.\n\n### ⚙️ 3. Productivity `(उत्पादकता / ઉત્પાદકતા)`:\n- Enhancing the capacity, efficiency, and working power of human labor through superior education, healthcare, technical training, and skill-building.\n- People are the most valuable wealth `(मानव पूंजी / માનવ મૂડી)` of any nation.\n\n### ✊ 4. Empowerment `(सशक्तिकरण / સશક્તિકરણ)`:\n- Bestowing real decision-making power, legal rights, and self-reliance upon disadvantaged, poor, and marginalized sections of society—especially **Women `(महिला सशक्तिकरण / મહિલા સશક્તિકરણ)`**.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "teacher_tip",
        "title": "Teacher's Secret: Distinguishing Economic Growth vs Human Development",
        "content": "💡 **Board Exam 2-Mark Distinction Golden Formula:**\n- If the examiner asks: *'Differentiate between Economic Growth and Human Development'*, draw this 3-point table:\n  1. **Nature:** Economic Growth is Quantitative `(मात्रात्मक / પરિમાણાત્મક)`; Human Development is Qualitative `(गुणात्मक / ગુણાત્મક)`.\n  2. **Indicator:** Economic Growth measures rise in National Income / GDP; Human Development measures HDI (Health, Education, Living Standards).\n  3. **Role of Humans:** In Economic Growth, human beings are treated as *Tools of Production* `(उत्पादन का साधन)`; in Human Development, human well-being is the *Ultimate Goal* `(विकास का साध्य)`.",
        "difficulty": "Beginner",
        "bloom": "Analyze"
    })

    blocks.append({
        "type": "mcq",
        "title": "Knowledge Check 1: Concept of Human Development",
        "content": {
            "question": "Which international organization conceptualized and published the world's first Human Development Report (HDR) in the year 1990?",
            "options": [
                "World Bank (વિશ્વ બેંક)",
                "United Nations Development Programme - UNDP (સંયુક્ત રાષ્ટ્ર વિકાસ કાર્યક્રમ)",
                "International Monetary Fund - IMF (આંતરરાષ્ટ્રીય નાણાં ભંડોળ)",
                "World Health Organization - WHO (વિશ્વ આરોગ્ય સંસ્થા)"
            ],
            "correct_answer": "United Nations Development Programme - UNDP (સંયુક્ત રાષ્ટ્ર વિકાસ કાર્યક્રમ)",
            "explanation": "In 1990, the United Nations Development Programme (UNDP) published the first Human Development Report (HDR) under the intellectual leadership of Dr. Mahbub ul Haq and Nobel laureate Prof. Amartya Sen."
        },
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    # =========================================================================
    # MODULE 2: HUMAN DEVELOPMENT INDEX (HDI) - DIMENSIONS & METHODOLOGY
    # =========================================================================
    blocks.append({
        "type": "theory",
        "title": "Human Development Index (HDI / માનવ વિકાસ આંક): Evolution & Methodology",
        "content": "### 📊 The Evolution of HDI Measurement\n\nTo quantify and scientifically rank countries based on human well-being, the **Human Development Index (HDI) `(मानव विकास सूचकांक / માનવ વિકાસ આંક)`** was introduced in **1990** by UNDP.\n\n---\n\n### 🔄 Old Methodology (1990 to 2009) vs Revised Methodology (2010 Onwards):\n- **Prior to 2010:** HDI was calculated using: (1) Life Expectancy, (2) Adult Literacy & Gross Enrollment Ratio, and (3) Per Capita GDP.\n- **From 2010 Onwards (New Standard):** To reflect realistic educational attainment and economic purchasing capacity, UNDP introduced **Three Modern Dimensions & Refined Indicators**:\n\n```\n                         ┌─────────────────────────────────────────┐\n                         │   HUMAN DEVELOPMENT INDEX (HDI)         │\n                         │   (માનવ વિકાસ આંક / मानव विकास सूचकांक) │\n                         └────────────────────┬────────────────────┘\n                                              │\n         ┌────────────────────────────────────┼────────────────────────────────────┐\n         ▼                                    ▼                                    ▼\n┌───────────────────────────────┐ ┌───────────────────────────────┐ ┌───────────────────────────────┐\n│ 1. LIFE EXPECTANCY INDEX (LEI)│ │    2. EDUCATION INDEX (EI)    │ │    3. INCOME INDEX (II)       │\n│ (दीर्घायु / સરેરાશ આયુષ્ય)    │ │   (शिक्षा / શિક્ષણ સૂચકાંક)    │ │ (आय सूचकांक / આવક સૂચકાંક)    │\n├───────────────────────────────┤ ├───────────────────────────────┤ ├───────────────────────────────┤\n│ • Life Expectancy at Birth    │ │ • Mean Years of Schooling     │ │ • Gross National Income (GNI) │\n│   (जन्म समय जीवन प्रत्याशा)   │ │   (MYS - शालकीय औसत वर्ष)     │ │   per capita (માથાદીઠ કુલ GNI)│\n│ • Max: 83.6 yrs | Min: 20 yrs │ │ • Expected Years of Schooling │ │ • Measured in PPP $           │\n│ • India (HDR 2015): 68.0 yrs  │ │   (EYS - अपेक्षित शालकीय वर्ष)│ │ • Max: $75,000 | Min: $100    │\n└───────────────────────────────┘ └───────────────────────────────┘ └───────────────────────────────┘\n```",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "theory",
        "title": "Deep Dive into the 3 Dimensions of HDI (માનવ વિકાસ આંકના 3 પરિમાણો)",
        "content": "Let us examine the exact mathematical definitions and benchmarks for each of the three dimensions:\n\n---\n\n### 🩺 1. Life Expectancy Index (LEI) `(जीवन प्रत्याशा सूचकांक / સરેરાશ આયુષ્ય સૂચકાંક)`:\n- Measures health, sanitation, and longevity at birth.\n- **Definition:** The average number of years a newborn infant is expected to live under prevailing mortality rates.\n- **Global Benchmarks:** Maximum = **83.6 years**, Minimum = **20.0 years**.\n- **India's Status (HDR 2015):** **68.0 years** `(૬૮.૦ વર્ષ)`.\n\n---\n\n### 📚 2. Education Index (EI) `(शिक्षा सूचकाંક / શિક્ષણ સૂચકાંક)`:\n- Education Index is computed using two independent sub-indicators:\n  1. **Mean Years of Schooling (MYS) `(शालकीय औसत वर्ष / શાળાકીય સરેરાશ વર્ષો)`:**\n     - Average years of formal schooling completed by citizens aged **25 years and older**.\n     - Global Benchmarks: Maximum = **13.3 years**, Minimum = **0 years**.\n     - India's Status (HDR 2015): **5.4 years** `(૫.૪ વર્ષ)`.\n  2. **Expected Years of Schooling (EYS) `(अपेक्षित शालकीय वर्ष / અપેક્ષિત શાળાકીય વર્ષો)`:**\n     - The total number of years of schooling that a 5-year-old child entering school can expect to receive throughout their youth.\n     - Global Benchmarks: Maximum = **18.0 years**, Minimum = **0 years**.\n     - India's Status (HDR 2015): **11.7 years** `(૧૧.૭ વર્ષ)`.\n\n---\n\n### 💰 3. Income Index (II) `(आय सूचकांक / આવક સૂચકાંક)`:\n- Measures economic capability and purchasing power.\n- **Indicator:** **Gross National Income (GNI) per capita `(माथાદીઠ કુલ રાષ્ટ્રીય આવક)`** calculated using **Purchasing Power Parity (PPP $) `(समखरीद शक्ति दर / સમખરીદ શક્તિ)`** in US Dollars.\n- **Global Benchmarks:** Maximum = **$75,000**, Minimum = **$100**.\n- **India's Status (HDR 2015):** **$5,497** `(૫,૪૯૭ ડૉલર)`.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    blocks.append({
        "type": "diagram",
        "title": "Geometric Mean Calculation of HDI",
        "content": "```\n                     ┌───────────────────────────────────┐\n                     │     DIMENSION INDICES (0 to 1)    │\n                     │  LEI (Health) ── EI (Education)   │\n                     │         II (Income PPP $)         │\n                     └─────────────────┬─────────────────┘\n                                       │\n                                       ▼\n                     ┌───────────────────────────────────┐\n                     │   GEOMETRIC MEAN CALCULATION      │\n                     │   HDI = ∛( LEI × EI × II )        │\n                     └─────────────────┬─────────────────┘\n                                       │\n                                       ▼\n                     ┌───────────────────────────────────┐\n                     │      FINAL COMPOSITE HDI SCORE    │\n                     │           (Range: 0 to 1)         │\n                     └───────────────────────────────────┘\n```\n*Note: HDI is always expressed on a normalized scale ranging between 0.000 and 1.000.*",
        "image_url": "assets/images/ss_ch19_hdi_calculation.jpg",
        "alt_text": "Formula diagram showing HDI as geometric mean of Life Expectancy, Education, and Income Indices."
    })

    blocks.append({
        "type": "memory_trick",
        "title": "Mnemonic to Memorize HDI Indicators & India's Statistics",
        "content": "🧠 **Super Mnemonic for HDI Dimensions & India's Numbers:**\n- Remember **'L - E - I'** (Like 'Lei' garland):\n  - **L** ➔ **Life Expectancy:** India = **68.0 yrs**\n  - **E** ➔ **Education:** MYS (Adults) = **5.4 yrs** | EYS (Kids) = **11.7 yrs**\n  - **I** ➔ **Income (PPP $):** India = **$5,497**\n\n*Tip: MYS is for 25+ adults (short = 5.4 yrs), while EYS is for 5-year-old school beginners (long = 11.7 yrs)!*",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "mcq",
        "title": "Knowledge Check 2: Education Index Indicators",
        "content": {
            "question": "Under the revised post-2010 Human Development Index (HDI) methodology, what are the two sub-indices used to calculate the Education Index (EI)?",
            "options": [
                "Adult Literacy Rate and Gross Enrollment Ratio",
                "Mean Years of Schooling (MYS) and Expected Years of Schooling (EYS)",
                "Primary School Dropouts and Higher Education Intake",
                "Number of Teachers and Pupil-Teacher Ratio"
            ],
            "correct_answer": "Mean Years of Schooling (MYS) and Expected Years of Schooling (EYS)",
            "explanation": "Since 2010, the Education Index is calculated using Mean Years of Schooling (MYS for adults 25+) and Expected Years of Schooling (EYS for children entering school)."
        },
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    # =========================================================================
    # MODULE 3: GLOBAL CLASSIFICATION OF COUNTRIES (HDR REPORT)
    # =========================================================================
    blocks.append({
        "type": "theory",
        "title": "Global Classification of Countries on Human Development (HDR)",
        "content": "In the **Human Development Report 2015 (HDR 2015)** published by UNDP, a total of **188 member countries** were classified into **Four Distinct Categories `(चार श्रेणियां / ચાર શ્રેણીઓ)`** based on their composite HDI scores:\n\n---\n\n### 🏆 1. Very High Human Development `(उच्चतम मानव विकास / ઉચ્ચતમ માનવ વિકાસ)`:\n- **HDI Score Range:** **0.802 and above** `(૦.૮૦૨ કે તેથી વધુ)`\n- **Ranks Included:** Ranks **1 to 49**\n- **Leading Countries:** **Norway `(नॉर्वे / નૉર્વે - Rank 1, HDI 0.944)`**, Australia (Rank 2), Switzerland (Rank 3), Denmark (Rank 4), Netherlands (Rank 5), Germany (Rank 6), USA (Rank 8), Singapore (Rank 11), Japan (Rank 20), UK (Rank 14).\n\n---\n\n### 📈 2. High Human Development `(उच्च मानव विकास / ઉચ્ચ માનવ વિકાસ)`:\n- **HDI Score Range:** **0.700 to 0.801** `(૦.૭૦૦ થી ૦.૮૦૧)`\n- **Ranks Included:** Ranks **50 to 105**\n- **Leading Countries:** Russia (Rank 50), Malaysia (Rank 62), Iran (Rank 69), **Sri Lanka `(श्रीलंका / શ્રીલંકા - Rank 73, HDI 0.757 - Highest in South Asia!)`**, Mexico (Rank 74), Brazil (Rank 75), China (Rank 90), Thailand (Rank 93).\n\n---\n\n### 📊 3. Medium Human Development `(मध्यम मानव विकास / મધ્યમ માનવ વિકાસ)`:\n- **HDI Score Range:** **0.550 to 0.699** `(૦.૫૫૦ થી ૦.૬૯૯)`\n- **Ranks Included:** Ranks **106 to 155**\n- **Leading Countries:** Indonesia (Rank 110), South Africa (Rank 116), **India `(भारत / ભારત - Rank 130, HDI 0.609)`**, Bhutan (Rank 132), Bangladesh (Rank 142), Nepal (Rank 145), Pakistan (Rank 147), Myanmar (Rank 148), Kenya (Rank 146).\n\n---\n\n### ⚠️ 4. Low Human Development `(निम्न मानव विकास / નિમ્ન માનવ વિકાસ)`:\n- **HDI Score Range:** **Below 0.550** `(૦.૫૫૦ થી નીચે)`\n- **Ranks Included:** Ranks **156 to 188**\n- **Lowest Ranked Countries:** Zimbabwe (Rank 155), Afghanistan (Rank 171), Congo (Rank 176), Chad (Rank 185), Central African Republic (Rank 187), **Niger `(नाइजर / નાઇજર - Rank 188, HDI 0.348 - Lowest in the World!)`**.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "diagram",
        "title": "Global HDI Tiers Pyramid & India's Position",
        "content": "```\n                           ▲\n                          / \\\n                         /   \\  VERY HIGH (≥ 0.802)\n                        / Tier\\  Norway (#1, 0.944), Australia (#2)\n                       /───────\\  Ranks 1 to 49\n                      /  HIGH   \\\n                     /   Tier    \\  Sri Lanka (#73), China (#90), Brazil (#75)\n                    /─────────────\\  0.700 to 0.801 (Ranks 50 to 105)\n                   /    MEDIUM     \\\n                  /      Tier       \\  ★ INDIA (#130, HDI 0.609) ★\n                 /───────────────────\\  Bhutan (#132), Bangladesh (#142), Pak (#147)\n                /         LOW         \\  0.550 to 0.699 (Ranks 106 to 155)\n               /         Tier          \\  Afghanistan (#171), Niger (#188, 0.348)\n              /─────────────────────────\\  Below 0.550 (Ranks 156 to 188)\n```",
        "image_url": "assets/images/ss_ch19_hdi_pyramid.jpg",
        "alt_text": "Pyramid diagram depicting 4 tiers of global Human Development and India's position in the Medium tier."
    })

    blocks.append({
        "type": "theory",
        "title": "India's Human Development Status vs South Asian Neighbors",
        "content": "### 🌏 Comparative Analysis of India and Neighboring Nations (HDR 2015):\n\nUnderstanding India's ranking among South Asian and Asian neighbors is a favorite topic in Board Exam question papers:\n\n| Country `(देश / દેશ)` | Global Rank `(वैश्विक रैंक)` | HDI Score `(HDI अंक)` | Classification Category `(श्रेणी)` |\n| :--- | :---: | :---: | :--- |\n| **Norway** | **1** | **0.944** | Very High `(उच्चतम)` |\n| **Sri Lanka** | **73** | **0.757** | High `(उच्च - South Asian Leader)` |\n| **China** | **90** | **0.727** | High `(उच्च)` |\n| **Maldives** | **104** | **0.706** | High `(उच्च)` |\n| **★ INDIA ★** | **130** | **0.609** | **Medium `(मध्यम मानव विकास)`** |\n| **Bhutan** | **132** | **0.605** | Medium `(मध्यम)` |\n| **Bangladesh** | **142** | **0.570** | Medium `(मध्यम)` |\n| **Nepal** | **145** | **0.548** | Low / Medium Border `(निम्न/मध्यम)` |\n| **Pakistan** | **147** | **0.538** | Low `(निम्न)` |\n| **Myanmar** | **148** | **0.536** | Low `(निम्न)` |\n| **Afghanistan** | **171** | **0.465** | Low `(निम्न)` |\n| **Niger** | **188** | **0.348** | **Low `(निम्नतम - Lowest Rank)`** |\n\n---\n\n### 🔍 Critical Insights for Board Exams:\n1. **Ahead of India:** **Sri Lanka (73)**, **China (90)**, and **Maldives (104)** rank ahead of India in human development.\n2. **Behind India:** **Bhutan (132)**, **Bangladesh (142)**, **Nepal (145)**, **Pakistan (147)**, **Myanmar (148)**, and **Afghanistan (171)** rank behind India.\n3. **India's Journey:** India's HDI score improved steadily from **0.428 in 1990** to **0.609 in 2015**, moving from the Low category to the Medium category.",
        "difficulty": "Intermediate",
        "bloom": "Analyze"
    })

    blocks.append({
        "type": "teacher_tip",
        "title": "Board Exam Trap: Neighboring Countries Ranking",
        "content": "💡 **Teacher's Secret Insight:** In Board Objective/MCQ questions, examiners love to ask: *'Which South Asian country has a higher Human Development Index than India?'*\n- **Correct Answer:** **Sri Lanka `(श्रीलंका / શ્રીલંકા - Rank 73)`** or **Maldives (Rank 104)**!\n- Never get confused by Pakistan or Bangladesh; they rank *below* India.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "mcq",
        "title": "Knowledge Check 3: Global HDI Ranking",
        "content": {
            "question": "According to the Human Development Report 2015 (HDR 2015), which country secured Rank 1 in the world and what was India's rank among 188 countries?",
            "options": [
                "Rank 1: USA | India: Rank 100",
                "Rank 1: Norway | India: Rank 130",
                "Rank 1: Switzerland | India: Rank 142",
                "Rank 1: Denmark | India: Rank 116"
            ],
            "correct_answer": "Rank 1: Norway | India: Rank 130",
            "explanation": "Norway secured the 1st rank with an HDI score of 0.944, while India ranked 130th with an HDI score of 0.609 in the HDR 2015 report."
        },
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    # =========================================================================
    # MODULE 4: CHALLENGES TO HUMAN DEVELOPMENT IN INDIA
    # =========================================================================
    blocks.append({
        "type": "theory",
        "title": "Major Challenges to Human Development in India (માનવ વિકાસના પડકારો)",
        "content": "Despite rapid economic industrialization, India faces **Three Major Challenges `(तीन प्रमुख चुनौतियाँ / ત્રણ મુખ્ય પડકારો)`** that hinder human progress:\n\n---\n\n### 🏥 Challenge 1: Health and Nutrition `(स्वास्थ्य और पोषण / આરોગ્ય અને પોષણ)`:\n- Health is a state of complete physical, mental, and social well-being, not merely the absence of disease.\n- **Infant Mortality Rate (IMR) `(शिशु मृत्यु दर / બાળ મૃત્યુદર)`:** Although declining, child deaths per 1,000 live births due to infections and malnutrition remain a critical concern.\n- **Maternal Mortality Rate (MMR) `(मातृ मृत्यु दर / માતા મૃત્યુદર)`:** Death of pregnant women during delivery due to anemia `(रक्ताल्पता / લોહીની ઉણપ - એનીમિયા)`, lack of institutional delivery, and rural medical infrastructure shortages.\n- **Malnutrition & Stunting `(कुपोषण / કુપોષણ)`:** Over 1/3rd of children and adolescent girls suffer from micronutrient deficiencies.\n- **Communicable & Lifestyle Diseases:** Tuberculosis, Malaria, Dengue, Cancer, and Diabetes place a heavy financial burden on poor families.\n\n---\n\n### ⚖️ Challenge 2: Gender Equality & Declining Sex Ratio `(लैंगिक समानता और घटता लिंगानुपात)`:\n- **Sex Ratio `(लिंगानुपात / જાતિ પ્રમાણ - સ્ત્રી-પુરુષ પ્રમાણ)`:** The number of females per 1,000 males in a population.\n- **The Crisis of Female Foeticide `(कन्या भ्रूण हत्या / સ્ત્રી ભ્રૂણ હત્યા)`:** Abuse of ultrasound sex-determination technology and deep-rooted patriarchal preference for sons `(पुत्र मोह / પુત્ર મોહ)` caused a severe drop in the **Child Sex Ratio (0-6 years)** in several states (e.g., Haryana, Punjab, Gujarat, Rajasthan).\n- **PCPNDT Act:** The government enacted the *Pre-Conception and Pre-Natal Diagnostic Techniques (Prohibition of Sex Selection) Act* making fetal sex determination a severe criminal offense punishable by rigorous imprisonment.\n\n---\n\n### 👩 Challenge 3: Women Empowerment `(महिला सशक्तिकरण / મહિલા સશક્તિકરણ)`:\n- Women constitute approximately **50% of the population**, yet historically faced severe structural disadvantages:\n  1. **Literacy Disparity:** Female literacy is significantly lower than male literacy.\n  2. **Unpaid Domestic Burden:** Endless household chores, child rearing, and cooking are unpaid and undervalued.\n  3. **Economic Dependence:** Lack of inheritance/property rights and lower wages for identical physical labor.\n  4. **Low Political Representation:** Low proportion of female parliamentarians and executives in decision-making bodies.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "diagram",
        "title": "Interlinked Vicious Cycle of Human Development Challenges",
        "content": "```\n                    ┌───────────────────────────────────────┐\n                    │      POOR FEMALE LITERACY & BIAS      │\n                    │   (निरक्षरता और सामाजिक भेदभाव)       │\n                    └───────────────────┬───────────────────┘\n                                        │\n                                        ▼\n                    ┌───────────────────────────────────────┐\n                    │    EARLY MARRIAGE & HIGH FERTILITY    │\n                    │    (कम उम्र में विवाह और मातृत्व)     │\n                    └───────────────────┬───────────────────┘\n                                        │\n                                        ▼\n                    ┌───────────────────────────────────────┐\n                    │      MALNUTRITION & HIGH MMR / IMR    │\n                    │   (माता-शिशु कुपोषण और उच्च मृत्युदर) │\n                    └───────────────────┬───────────────────┘\n                                        │\n                                        ▼\n                    ┌───────────────────────────────────────┐\n                    │     LOW PRODUCTIVITY & POVERTY TRAP   │\n                    │    (कम उत्पादकता और गरीबी का दुष्चक्र)│\n                    └───────────────────────────────────────┘\n```\n*Breaking this vicious cycle requires targeted Women Empowerment, institutional maternal healthcare, and quality female education.*",
        "image_url": "assets/images/ss_ch19_vicious_cycle.jpg",
        "alt_text": "Flowchart showing the vicious cycle linking female illiteracy, early marriage, maternal malnutrition, and poverty."
    })

    blocks.append({
        "type": "teacher_tip",
        "title": "High-Yield Definitions: IMR and MMR",
        "content": "💡 **Exam-Ready Definitions for 1-2 Marks:**\n1. **Infant Mortality Rate (IMR) `(शिशु मृत्यु दर / બાળ મૃત્યુદર)`:** The number of infants dying before reaching **one year of age per 1,000 live births** in a given year.\n2. **Maternal Mortality Rate (MMR) `(मातृ मृत्यु दर / માતા મૃત્યુદર)`:** The number of maternal deaths during pregnancy, delivery, or within 42 days of termination of pregnancy **per 1,00,000 (one lakh) live births**.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "mcq",
        "title": "Knowledge Check 4: Female Foeticide Legislation",
        "content": {
            "question": "Which legal act was enacted in India to strictly prohibit prenatal sex determination and prevent female foeticide?",
            "options": [
                "Domestic Violence Act (ઘરેલું હિંસા નિવારણ અધિનિયમ)",
                "PCPNDT Act - Pre-Conception and Pre-Natal Diagnostic Techniques Act (ગર્ભધારણ પૂર્વ અને પ્રસુતિ પૂર્વ નિદાન તકનીક અધિનિયમ)",
                "Right to Education Act (શિક્ષણનો અધિકાર અધિનિયમ)",
                "Maternity Benefit Act (માતૃત્વ લાભ અધિનિયમ)"
            ],
            "correct_answer": "PCPNDT Act - Pre-Conception and Pre-Natal Diagnostic Techniques Act (ગર્ભધારણ પૂર્વ અને પ્રસુતિ પૂર્વ નિદાન તકનીક અધિનિયમ)",
            "explanation": "The PCPNDT Act criminalizes the use of prenatal diagnostic techniques (such as sonography) for sex determination to eliminate female foeticide."
        },
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    # =========================================================================
    # MODULE 5: WOMEN EMPOWERMENT & WELFARE SCHEMES (NATIONAL & GUJARAT)
    # =========================================================================
    blocks.append({
        "type": "theory",
        "title": "National Initiatives for Women Welfare (ભારત સરકારની યોજનાઓ)",
        "content": "The Government of India has launched landmark constitutional, legislative, and financial programs to empower women:\n\n---\n\n### 🇮🇳 Key Central Government Initiatives:\n1. **National Commission for Women `(राष्ट्रीय महिला आयोग / રાષ્ટ્રીય મહિલા આયોગ)`:** Established in **1992** as a statutory body to safeguard constitutional and legal rights of women.\n2. **National Policy for the Empowerment of Women (2001) `(राष्ट्रीय महिला सशक्तिकरण नीति)`:** Formulated a roadmap for eliminating all forms of discrimination and ensuring equal participation of women in socio-economic and political life.\n3. **73rd and 74th Constitutional Amendments:** Mandated **33% reservation `(३३% आरक्षण / ૩૩% અનામત)`** for women in local self-governing bodies (Gram Panchayats, Municipalities, and Municipal Corporations).\n4. **Beti Bachao, Beti Padhao (2015) `(बेटी बचाओ, बेटी पढ़ाओ / બેટી બચાવો, બેટી પઢાવો)`:** Flagship campaign across vulnerable districts to prevent female foeticide, ensure the survival of girl infants, and guarantee their quality schooling.\n5. **Sukanya Samriddhi Yojana `(सुकन्या समृद्धि योजना)`:** High-interest small deposit savings scheme opened by parents for minor daughters to fund higher education and marriage without debt.\n6. **Pradhan Mantri Matru Vandana Yojana (PMMVY):** Direct cash transfer into bank accounts of pregnant women to compensate for wage loss and ensure adequate nutrition.\n7. **Pradhan Mantri Ujjwala Yojana:** Providing free LPG cooking gas connections to BPL rural women, liberating them from toxic firewood smoke and respiratory diseases.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "theory",
        "title": "Gujarat Government's Pioneering Women Empowerment Schemes (ગુજરાત સરકારની યોજનાઓ)",
        "content": "Gujarat has been a pioneer in creating specialized schemes addressing girls' education, maternal healthcare, emergency rescue, and self-employment:\n\n---\n\n### 🦁 1. Kanya Kelavani Rathyatra & Shala Praveshotsav `(कन्या केळवणी रथयात्रा અને શાળા પ્રવેશોત્સવ)`:\n- Annual statewide mass mobilization festival led by ministers and senior bureaucrats visiting villages to achieve **100% primary school enrollment** of young girls.\n\n### 📜 2. Vidya Lakshmi Bond `(विद्या लक्ष्मी बॉन्ड / વિદ્યાલક્ષ્મી બોન્ડ)`:\n- A financial bond of **₹2,000** given to every girl child enrolling in Standard 1 in villages with low female literacy or urban slum areas. The bond earns interest and matures when she passes Class 8.\n\n### 🚲 3. Saraswati Sadhana Yojana `(सरस्वती साधना योजना / સરસ્વતી સાધના યોજના)`:\n- **Free distribution of bicycles `(मुफ्त साइकिल वितरण / મફત સાયકલ વિતરણ)`** to girls from scheduled castes, scheduled tribes, and economically weaker sections studying in **Standard 9** in secondary schools. This prevents girls from dropping out due to long commuting distances to neighboring village schools.\n\n### 👶 4. Chiranjeevi Yojana `(चिरंजीवी योजना / ચિરંજીવી યોજના)`:\n- Public-Private Partnership (PPP) scheme providing **free institutional delivery and emergency cesarean operations** for BPL and poor pregnant women through empaneled private gynecologists to drastically slash Maternal Mortality Rate (MMR) and Infant Mortality Rate (IMR).\n\n### 🥣 5. Sabla Yojana & Take Home Ration (THR) `(सबला योजना)`:\n- Nutrition and health education program for adolescent girls (aged 11-18 years) providing iron-folic acid supplements and nutritious meals to combat anemia.\n\n### 📞 6. '181 Abhayam' Women Helpline `(૧૮૧ અભયમ મહિલા હેલ્પલાઈન)`:\n- **24×7 Toll-Free Emergency Helpline** across Gujarat offering immediate rescue vans `(रेस्क्यू वैन / રેસ્ક્યૂ વાન)`, legal protection, psychological counseling, and police intervention for women facing domestic violence, eve-teasing, physical abuse, or distress.\n\n### 🤝 7. Mission Mangalam & Sakhi Mandals `(मिशन मंगलम / સખી મંડળો)`:\n- Formation of Women Self-Help Groups (SHGs / Sakhi Mandals) providing micro-credit, banking linkages, and entrepreneurial training to make rural women economically self-reliant.\n\n### 🗳️ 8. 50% Reservation in Local Self-Government `(સ્થાનિક સ્વરાજ્યમાં ૫૦% અનામત)`:\n- Gujarat increased women's reservation from 33% to **50% in Gram Panchayats, Taluka Panchayats, District Panchayats, and Municipalities**, empowering thousands of women village leaders *(Sarpanchs)*.\n\n### 💰 9. Gender Budgeting `(जेंडर बजट / જેન્ડર બજેટ)`:\n- A distinct budgetary mechanism where special government funds are earmarked and audited exclusively for programs directly empowering women.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "diagram",
        "title": "Gujarat Government's Golden Umbrella of Women Welfare",
        "content": "```\n                      ┌─────────────────────────────────────────┐\n                      │  GUJARAT WOMEN EMPOWERMENT SCHEMES      │\n                      │  (ગુજરાત સરકારની નારી કલ્યાણકારી યોજનાઓ)│\n                      └────────────────────┬────────────────────┘\n                                           │\n         ┌──────────────────┬──────────────┴─────┬──────────────────┐\n         ▼                  ▼                    ▼                  ▼\n┌─────────────────┐┌─────────────────┐┌─────────────────┐┌─────────────────┐\n│   EDUCATION     ││   HEALTHCARE    ││EMERGENCY RESCUE ││ SELF-RELIANCE   │\n│ (શિક્ષણ & પ્રવેશ)││(આરોગ્ય & પ્રસુતિ)││ (સુરક્ષા & સહાય) ││ (આર્થિક આઝાદી)  │\n├─────────────────┤├─────────────────┤├─────────────────┤├─────────────────┤\n│• Shala Pravesh- ││• Chiranjeevi    ││• 181 Abhayam    ││• Mission        │\n│  otsav          ││  Yojana (Free   ││  Helpline (24x7 ││  Mangalam       │\n│• Vidya Lakshmi  ││  Delivery)      ││  Rescue Vans)   ││• Sakhi Mandals  │\n│  Bond (Std 1)   ││• Sabla Yojana   ││• Women Police   ││• 50% Panchayat  │\n│• Saraswati      ││  (Adolescent    ││  Stations &     ││  Reservation    │\n│  Sadhana (Bikes)││  Nutrition)     ││  Protection Cell││• Gender Budget  │\n└─────────────────┘└─────────────────┘└─────────────────┘└─────────────────┘\n```",
        "image_url": "assets/images/ss_ch19_gujarat_schemes.jpg",
        "alt_text": "Infographic showing Gujarat Government schemes categorized into Education, Healthcare, Emergency Rescue, and Self-Reliance."
    })

    blocks.append({
        "type": "memory_trick",
        "title": "Super Mnemonic for Gujarat Welfare Schemes: 'V-S-C-A-M'",
        "content": "🧠 **Memory Mnemonic: 'V - S - C - A - M' (Vijayi Striyan):**\n- **V** ➔ **Vidya Lakshmi Bond:** ₹2,000 Bond for Std 1 enrollment.\n- **S** ➔ **Saraswati Sadhana:** Free Bicycles for Std 9 secondary girls.\n- **C** ➔ **Chiranjeevi Yojana:** Free institutional delivery for pregnant mothers.\n- **A** ➔ **Abhayam 181:** 24x7 Emergency helpline & rescue van.\n- **M** ➔ **Mission Mangalam:** Sakhi Mandals for micro-finance & self-reliance.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "mcq",
        "title": "Knowledge Check 5: Gujarat Specific Welfare Schemes",
        "content": {
            "question": "Which scheme of the Gujarat Government provides free bicycles to secondary school girls (Class 9) to prevent dropouts caused by long distance travel to school?",
            "options": [
                "Vidya Lakshmi Bond (વિદ્યાલક્ષ્મી બોન્ડ)",
                "Saraswati Sadhana Yojana (સરસ્વતી સાધના યોજના)",
                "Chiranjeevi Yojana (ચિરંજીવી યોજના)",
                "Sabla Yojana (સબલા યોજના)"
            ],
            "correct_answer": "Saraswati Sadhana Yojana (સરસ્વતી સાધના યોજના)",
            "explanation": "The Saraswati Sadhana Yojana provides free bicycles to girls studying in Class 9 in secondary schools to ensure safe travel and prevent school dropouts."
        },
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    # =========================================================================
    # MODULE 6: BOARD EXAM MASTERY (PYQS, HOTS & ANSWER STRUCTURES)
    # =========================================================================
    blocks.append({
        "type": "exam_tips",
        "title": "Board Exam Top-Scoring Secrets (Class 10 SS Chapter 19)",
        "content": "🔥 **BOARD EXAM SUPER-HOTS & TOPPER ANSWER STRUCTURES:**\n\n### 📝 1. Long Question (4 Marks): 'Explain the indicators used for calculating Human Development Index (HDI) post-2010.'\n- **Structure:**\n  - *Introduction:* Mention UNDP, 1990 introduction by Mahbub ul Haq & Amartya Sen, and geometric mean formula: $HDI = \\sqrt[3]{LEI \\times EI \\times II}$.\n  - *Paragraph 1 (LEI):* Define Life Expectancy Index, Max 83.6 yrs, Min 20 yrs, India 68.0 yrs.\n  - *Paragraph 2 (EI):* Sub-indicator A = Mean Years of Schooling (MYS, 25+ age, Max 13.3 yrs, India 5.4 yrs); Sub-indicator B = Expected Years of Schooling (EYS, 5-yr-old kids, Max 18 yrs, India 11.7 yrs).\n  - *Paragraph 3 (II):* Gross National Income (GNI) per capita in Purchasing Power Parity (PPP $), Max $75,000, Min $100, India $5,497.\n\n---\n\n### 📝 2. Short Note (3 Marks): 'Write a short note on schemes implemented by the Gujarat Government for Women Empowerment.'\n- **Must Include All 5 Core Schemes:**\n  1. *School Entry:* Kanya Kelavani Rathyatra & Shala Praveshotsav.\n  2. *Financial Bond:* Vidya Lakshmi Bond (₹2,000 for Class 1 girls).\n  3. *Mobility:* Saraswati Sadhana Yojana (Bicycles for Class 9 girls).\n  4. *Maternal Care:* Chiranjeevi Yojana (Free private institutional delivery for BPL).\n  5. *Emergency Safety:* 181 Abhayam Women Helpline (24x7 rescue van & counseling).\n  6. *Governance:* 50% reservation in Panchayati Raj.\n\n---\n\n### 🎯 3. Objective 1-Marker Rapid Fire Traps:\n- First Human Development Report published in ➔ **1990**\n- Global Rank 1 Country in HDR 2015 ➔ **Norway (HDI 0.944)**\n- India's Global Rank in HDR 2015 ➔ **Rank 130 (HDI 0.609, Medium Tier)**\n- Highest HDI South Asian Neighbor ➔ **Sri Lanka (Rank 73, HDI 0.757)**\n- Emergency Helpline Number for Women in Gujarat ➔ **181 (Abhayam)**\n- Reservation for Women in Gujarat Panchayati Raj ➔ **50%**\n- Benchmark Max & Min for Life Expectancy ➔ **Max 83.6 yrs, Min 20.0 yrs**\n- Benchmark Max & Min for GNI PPP $ ➔ **Max $75,000, Min $100**",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    blocks.append({
        "type": "reflection",
        "title": "Socratic Thought Challenge: Human Capabilities and Nation Building",
        "content": "🤔 **Socratic Thought Challenge:** \nReflect on the profound words of Nobel Laureate Amartya Sen: *'Development is about expanding the capabilities of human beings, not just increasing the count of industrial commodities.'*\n\nIf you were appointed as the Planning Commissioner of your state today, which single area would you invest in first—building wider highways or providing free healthcare and quality schooling to every girl child? How does educating a woman transform not just her family, but the entire nation for generations to come?",
        "difficulty": "Advanced",
        "bloom": "Create"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }

    # Save to GSEB Class 10 Social Science Chapter 19
    gseb_out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_social_science_ch19.json"
    os.makedirs(os.path.dirname(gseb_out_path), exist_ok=True)
    with open(gseb_out_path, "w", encoding="utf-8") as f:
        json.dump(final_json, f, indent=2, ensure_ascii=False)
    print(f"Generated GSEB Chapter at: {gseb_out_path}")

    # Also save to NCERT Class 10 Social Science Chapter 19 for multi-curriculum synchronization
    ncert_out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_social_science_ch19.json"
    final_json_ncert = dict(final_json)
    final_json_ncert["metadata"] = dict(final_json["metadata"])
    final_json_ncert["metadata"]["id"] = "ncert_class10_social_science_ch19"
    with open(ncert_out_path, "w", encoding="utf-8") as f:
        json.dump(final_json_ncert, f, indent=2, ensure_ascii=False)
    print(f"Generated NCERT Chapter at: {ncert_out_path}")

if __name__ == "__main__":
    generate_supreme_gseb_ss_ch19()
