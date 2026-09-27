import json
import os

def generate_supreme_gseb_ss_ch17():
    chapter_id = "gseb_class10_social_science_ch17"
    title = "Chapter 17: Economic Problems and Challenges: Poverty and Unemployment"
    
    metadata = {
        "id": chapter_id,
        "title": title,
        "subtitle": "The Ultimate Board Exam Mastery Guide",
        "subject": "Social Science",
        "grade": "10",
        "board": "GSEB/NCERT",
        "curriculum": ["GSEB", "Universal"],
        "language": "English/Hindi/Gujarati (Bilingual)",
        "difficulty": "Advanced",
        "estimated_minutes": 180,
        "version": "3.0.0-SUPREME-SS",
        "author": "Antigravity Supreme Intelligence",
        "reviewed_by": "Chief Academic Architect",
        "tags": [
            "social_science",
            "economics",
            "poverty",
            "unemployment",
            "mgnrega",
            "bpl",
            "disguised_unemployment",
            "gseb_class10",
            "board_special",
            "bilingual"
        ],
        "learning_outcomes": [
            "Understand the concepts, criteria, and measurement standards of Poverty and BPL.",
            "Differentiate clearly between Absolute Poverty and Relative Poverty with real-world examples.",
            "Analyze the root causes of Poverty and evaluate key Government Poverty Alleviation Programmes (MGNREGA, PMAY, PMKSY, NFSA).",
            "Identify and explain the 7 major types of Unemployment, especially Disguised and Seasonal Unemployment.",
            "Master effective policy measures, skill development schemes (Skill India, MUDRA), and Employment Exchange systems to solve Unemployment.",
            "Score maximum marks in GSEB/CBSE Class 10 Board Exam 2-mark, 3-mark, 4-mark questions, and HOTS."
        ],
        "ai_context": {
            "learning_goal": "Transform students into board exam toppers by breaking down complex socio-economic realities using the 8-Step Socratic Learning Cycle, rich visual diagrams, memory mnemonics, inline bilingual translations, and practical case studies.",
            "common_misconceptions": [
                "Students confuse Relative Poverty with starvation/absolute destitution. (Fact: Relative poverty measures income inequality among groups, while Absolute poverty is the inability to afford basic survival food/clothing/shelter).",
                "Students confuse Disguised Unemployment with Seasonal Unemployment. (Fact: Disguised unemployment has zero marginal productivity with surplus workers on the same job, whereas Seasonal unemployment means total lack of work during dry/off-season months).",
                "Students think MGNREGA guarantees 100 days of work per individual. (Fact: MGNREGA guarantees 100 days of unskilled manual wage employment per rural household, with 1/3 reservation for women)."
            ],
            "tutor_hint": "If the student struggles with poverty measurement, explain the '2400 rural vs 2100 urban calorie rule' using the physical labour analogy. If they struggle with unemployment types, use the '5 brothers on a 1-acre farm' example for Disguised Unemployment."
        }
    }
    
    blocks = []
    
    # =========================================================================
    # MODULE 1: THE DUAL CRISES OF INDIAN ECONOMY (HOOK & OVERVIEW)
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "Look at the extraordinary paradox `(विरोधाभास / વિરોધાભાસ)` of modern India: on one hand, our nation launches interplanetary rockets to the Moon (Chandrayaan) and builds world-leading software; on the other hand, millions of families struggle every night without two square meals, and educated youth holding university degrees queue up for manual jobs. Why does this happen? The answer lies in the two most stubborn socio-economic monsters of developing nations: **Poverty `(गरीबी / ગરીબી)`** and **Unemployment `(बेरोज़गारी / બેરોજગારી)`**. Let us master these crucial challenges!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "The Vicious Cycle of Poverty `(गरीबी का दुષ્ચક્ર / ગરીબીનું વિષચક્ર)`: Low Income ➔ Low Savings ➔ Low Investment & Capital ➔ Low Productivity ➔ Low Income. Breaking this cycle requires massive state intervention through education, skill-building, and employment generation!",
        "image_url": "assets/images/ss_ch17_vicious_cycle_poverty.jpg",
        "alt_text": "A circular infographic depicting the Vicious Cycle of Poverty in developing economies."
    })
    
    blocks.append({
        "type": "theory",
        "title": "Major Economic Problems Facing India",
        "content": "The Indian economy faces numerous structural challenges `(संरचनात्मक चुनौतियाँ / માળખાકીય પડકારો)` which are divided into two main categories:\n\n1. **Economic Challenges:** \n- **Poverty `(गरीबी / ગરીબી)`**\n- **Unemployment `(बेरोज़गारी / બેરોજગારી)`**\n- **Price Rise / Inflation `(मूल्य वृद्धि / ભાવવધારો)`**\n- **Population Explosion `(जनसंख्या विस्फोट / વસ્તી વિસ્ફોટ)`**\n\n2. **Social Challenges:**\n- Illiteracy `(निरक्षरता / નિરક્ષરતા)`\n- Corruption `(भ्रष्टाचार / ભ્રષ્ટાચાર)`\n- Communalism & Social Disparities `(सांप्रदायिकता और सामाजिक विषमता / કોમવાદ અને સામાજિક અસમાનતા)`\n\nPoverty and Unemployment are twin problems `(जुड़वां समस्याएँ / જોડિયાં દૂષણો)` that act as both cause and consequence of each other: an unemployed person has no income and falls into poverty; a poor person lacks education/health and remains unemployed!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Teacher's Secret Insight:** In Board Exams, examiners love to ask: *\"Why are Poverty and Unemployment considered two sides of the same coin `(एक ही सिक्के के दो पहलू / એક જ સિક્કાની બે બાજુ)`?\"* Always answer by demonstrating the feedback loop: Lack of employment ➔ Zero purchasing power ➔ Poverty ➔ Malnutrition & No schooling ➔ Lack of skills ➔ Chronic unemployment!",
        "difficulty": "Intermediate",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "Which of the following describes the relationship between Poverty and Unemployment in India?",
            "options": [
                "They are completely independent of each other with no shared causes.",
                "They are inter-connected twin problems acting as both cause and effect of each other.",
                "Poverty only exists in urban cities while unemployment only exists in villages.",
                "Unemployment increases national income while poverty decreases it."
            ],
            "correct_answer": "They are inter-connected twin problems acting as both cause and effect of each other.",
            "explanation": "Poverty and Unemployment feed into each other in a vicious cycle: lack of employment leads to loss of income (Poverty), while poverty deprives families of education and vocational training, causing continued unemployment."
        },
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    # =========================================================================
    # MODULE 2: CONCEPT OF POVERTY, BPL CRITERIA & MEASUREMENT STANDARDS
    # =========================================================================
    blocks.append({
        "type": "theory",
        "title": "Concept of Poverty and BPL (Below Poverty Line)",
        "content": "**Poverty `(गरीबी / ગરીબી)`** is a socio-economic situation in which a significant proportion of society is deprived of satisfying their minimum basic requirements of life, such as:\n- **Food `(अन्न / આહાર)`**\n- **Clothing `(वस्त्र / કપડાં)`**\n- **Shelter / Housing `(आवास / રહેઠાણ)`**\n- **Primary Education `(प्राथमिक शिक्षा / શિક્ષણ)`**\n- **Healthcare Services `(स्वास्थ्य सेवाएँ / આરોગ્ય સુવિધાઓ)`**\n\nPeople living under such conditions are termed as living **Below the Poverty Line `(गरीबी रेखा से नीचे / ગરીબી રેખા હેઠળ - BPL)`**.\n\n### Origin of the Poverty Line Concept:\nThe concept of the 'Poverty Line' was first propounded by **Lord Boyd Orr `(लॉर्ड बॉयड ओर / લોર્ડ બોયડ ઓર)`**, the first Director-General of the Food and Agriculture Organization (FAO). It is a benchmark line based on minimum consumption expenditure `(न्यूनतम उपभोग व्यय / લઘુત્તમ વપરાશી ખર્ચ)` required for human survival and working capacity.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "theory",
        "title": "Major Characteristics of People Living Below Poverty Line (BPL)",
        "content": "People living in BPL conditions exhibit the following distinct characteristics:\n1. **Inability to secure two square meals a day `(दो वक्त का भोजन न मिलना / બે ટંકનું પૂરતું ભોજન ન મળવું)`**.\n2. **Compelled to live in unhygienic, deteriorated slum environments `(गंदी बस्तियों में रहने की मजबूरी / ગંદી અને બિનઆરોગ્યપ્રદ વસાહતો)`**.\n3. **Deprived of medical treatment and healthcare facilities**, leading to high susceptibility to diseases.\n4. **High rate of illiteracy `(उच्च निरक्षरता दर / ઊંચો નિરક્ષરતા દર)`**.\n5. **Low Life Expectancy `(कम औसत आयु / નીચું સરેરાશ આયુષ્ય)`** due to malnutrition `(कुपोषण / કુપોષણ)`.\n6. **Forced reliance on Child Labour `(बाल मजदूरी की विवशता / બાળમજૂરી કરવાની ફરજ)`**: Children are pulled out of school to support family earnings.\n7. **High Infant Mortality Rate `(उच्च शिशु मृत्यु दर / ઊંચો બાળ મૃત્યુદર)`**.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Calorie Consumption Benchmarks for Poverty Line: Rural Area requires **2400 Calories/person/day** (due to hard physical agricultural labour `(शारीरिक श्रम / શારીરિક શ્રમ)`), whereas Urban Area requires **2100 Calories/person/day** (due to less manual exertion in service/desk jobs).",
        "image_url": "assets/images/ss_ch17_calorie_standards.jpg",
        "alt_text": "Comparison chart of Rural 2400 kcal vs Urban 2100 kcal nutritional requirements."
    })
    
    blocks.append({
        "type": "memory_trick",
        "content": "🧠 **Memory Mnemonic: '24 Rural, 21 City'**\n- **Rural (2400 kcal):** Village farmers toil under the blazing sun, lifting ploughs and harvesting crops (more physical sweat ➔ **Higher Calories: 2400**).\n- **Urban (2100 kcal):** City workers commute by bus/train and work indoors (less physical exertion ➔ **Lower Calories: 2100**).",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "theory",
        "title": "Measurement Criteria: Tendulkar Committee Recommendations",
        "content": "In India, poverty measurement evolved from mere calorie intake to Per Capita Monthly Consumption Expenditure `(प्रति व्यक्ति मासिक उपभोग व्यय / માથાદીઠ માસિક વપરાશી ખર્ચ)` recommended by the **Prof. Suresh Tendulkar Committee (2011-12)**:\n\n- **Rural Areas:** **₹816 per person per month** (₹27 per day). For a family of 5 members = **₹4,080 per month**.\n- **Urban Areas:** **₹1,000 per person per month** (₹33 per day). For a family of 5 members = **₹5,000 per month**.\n\nAny individual or household spending less than this designated minimum threshold is officially classified as poor.",
        "difficulty": "Advanced",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "What are the per person daily calorie benchmarks prescribed for defining the poverty line in Rural and Urban areas respectively in India?",
            "options": [
                "2100 calories for Rural and 2400 calories for Urban",
                "2400 calories for Rural and 2100 calories for Urban",
                "1800 calories for Rural and 2500 calories for Urban",
                "3000 calories for Rural and 3000 calories for Urban"
            ],
            "correct_answer": "2400 calories for Rural and 2100 calories for Urban",
            "explanation": "Rural residents require 2400 calories/day due to rigorous manual agricultural labour, while urban residents require 2100 calories/day."
        },
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    # =========================================================================
    # MODULE 3: ABSOLUTE VS RELATIVE POVERTY & REGIONAL DIMENSIONS
    # =========================================================================
    blocks.append({
        "type": "theory",
        "title": "Absolute Poverty vs Relative Poverty",
        "content": "To understand poverty scientifically, economists classify it into two vital categories:\n\n### 1. Absolute Poverty `(निरपेक्ष गरीबी / નિરપેક્ષ ગરીબી)`:\n- When people are **unable to satisfy even the bare minimum requirements** (food, clothing, shelter, clean water) due to lack of minimum income/expenditure.\n- They live below the absolute physical subsistence level `(न्यूनतम जीवन निर्वाह स्तर / ન્યૂનતમ જીવનનિર્વાહ સ્તર)`.\n- **Prevalence:** Highly common in developing and underdeveloped countries like India, Bangladesh, and Sub-Saharan African nations.\n\n### 2. Relative Poverty `(सापेक्ष गरीबी / સાપેક્ષ ગરીબી)`:\n- It is a measure of **Income Inequality `(आय की असमानता / આવકની અસમાનતા)`** between different income classes in society.\n- A group of people having lower income is considered 'relatively poor' in comparison to another group with higher income, even though their basic survival needs are fulfilled!\n- **Example:** \n  - Person A earns ₹10,000/month\n  - Person B earns ₹50,000/month\n  - Person C earns ₹2,00,000/month\n  *Here, Person A is relatively poor compared to Person B and C, and Person B is relatively poor compared to Person C!*\n- **Prevalence:** Primarily used in developed countries like the USA, UK, and Germany to assess economic disparity.",
        "difficulty": "Intermediate",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "common_mistakes",
        "content": "⚠️ **COMMON EXAM CONFUSION:**\nStudents often write that *'Relative poverty means people are starving and dying of hunger'*. \n**CORRECT CONCEPT:** Relative poverty has NOTHING to do with starvation! A person driving a Honda car is 'relatively poor' compared to someone owning a private jet. Absolute poverty is about **Survival**, whereas Relative poverty is about **Inequality**!",
        "difficulty": "Intermediate",
        "bloom": "Evaluate"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Poverty Disparity Map in India: Highest poverty rate is in **Chhattisgarh (39.93%)**, followed by Jharkhand (36.96%), Bihar (33.74%), and Odisha (32.59%). Lowest poverty rate is in **Goa (5.09%)**, Kerala (7.05%), and Himachal Pradesh (8.06%). Gujarat stands at **16.63%**.",
        "image_url": "assets/images/ss_ch17_india_poverty_map.jpg",
        "alt_text": "Infographic showing state-wise poverty percentages across Indian states."
    })
    
    blocks.append({
        "type": "theory",
        "title": "Poverty Dimensions in India (Census & NITI Aayog Data)",
        "content": "According to the Planning Commission (2011-12):\n- The total number of poor in India was **26.93 Crore (21.9% of total population)**.\n- Rural Poverty stood at **25.7%**, while Urban Poverty stood at **13.7%**.\n- **State-wise Variations:**\n  - States with poverty exceeding 30%: Chhattisgarh `(39.93%)`, Jharkhand `(36.96%)`, Bihar `(33.74%)`, Odisha `(32.59%)`, Assam `(31.98%)`, Uttar Pradesh, Madhya Pradesh.\n  - States with lowest poverty (below 10%): Goa `(5.09%)`, Kerala `(7.05%)`, Himachal Pradesh `(8.06%)`, Punjab `(8.26%)`.\n  - **Gujarat `(गुजरात / ગુજરાત)`**: Approximately **16.63%** of the population lived below the poverty line.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "Which Indian state recorded the highest percentage of poverty according to the 2011-12 Planning Commission report?",
            "options": [
                "Bihar (33.74%)",
                "Chhattisgarh (39.93%)",
                "Odisha (32.59%)",
                "Gujarat (16.63%)"
            ],
            "correct_answer": "Chhattisgarh (39.93%)",
            "explanation": "Chhattisgarh had the highest proportion of poor population in India at 39.93%, while Goa had the lowest at 5.09%."
        },
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    # =========================================================================
    # MODULE 4: REASONS & CAUSES OF POVERTY IN INDIA
    # =========================================================================
    blocks.append({
        "type": "theory",
        "title": "Causes of Poverty in India (गरीबी के कारण / ગરીબીના કારણો)",
        "content": "Why does poverty persist in India despite massive planned development? The chief causes are:\n\n1. **Agricultural Backwardness & Low Productivity:**\n   - Heavy dependence on unpredictable monsoons `(मानसून की अनिश्चितता / ચોમાસાની અનિયમિતતા)`.\n   - Lack of modern irrigation facilities, small fragmented landholdings, and outdated farming tools.\n\n2. **Lack of Alternative Non-Farm Rural Employment:**\n   - Village and cottage industries declined due to machine-made factory competition, leaving rural workers jobless outside harvest seasons.\n\n3. **Rapid Population Explosion `(तीव्र जनसंख्या वृद्धि / ઝડપી વસ્તી વધારો)`:**\n   - Medical advancements lowered death rates, but birth rates remained high. The supply of labour vastly exceeded job opportunities, decreasing per capita income `(प्रति व्यक्ति आय / માથાદીઠ આવક)`.\n\n4. **High Inflation & Price Rise `(मूल्य वृद्धि और मुद्रास्फीति / ભાવવધારો)`:**\n   - Continuous rise in prices of essential commodities drastically reduced the real purchasing power `(क्रय शक्ति / ખરીદ શક્તિ)` of daily wage earners.\n\n5. **Illiteracy and Lack of Vocational Skills `(निरक्षरता और कौशल की कमी / નિરક્ષરતા અને કૌશલ્યનો અભાવ)`:**\n   - Uneducated workers are trapped in low-paying unorganized manual labour without upward career mobility.\n\n6. **Social Customs and Generational Debt Traps `(सामाजिक कुरीतियां और ऋणग्रस्तता / સામાજિક કુરિવાજો અને દેવાદારી)`:**\n   - Poor families spend lavishly beyond their means on marriages, funeral rites, and superstitions by borrowing from local moneylenders `(साहूकार / શાહુકાર)` at exorbitant interest rates, plunging them into permanent debt traps.\n\n7. **Skewed Distribution of Wealth `(धन और संपत्ति का असमान वितरण / સંપત્તિની અસમાન વહેંચણી)`:**\n   - Wealth and productive assets remained concentrated in the hands of a rich minority, leaving the bottom 50% impoverished.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "memory_trick",
        "content": "🧠 **Memory Mnemonic for 7 Causes of Poverty: 'PAID-SLIM'**\n- **P** - **P**opulation explosion\n- **A** - **A**gricultural backwardness & monsoon failure\n- **I** - **I**nflation & price rise eroding purchasing power\n- **D** - **D**ebt trap from moneylenders\n- **S** - **S**ocial rituals, traditions & caste rigidity\n- **L** - **L**ack of non-farm alternative jobs\n- **I** - **I**lliteracy & lack of training\n- **M** - **M**aldistribution of wealth & resources",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM 4-MARK QUESTION ALERT:**\n*\"Explain the socio-economic causes responsible for poverty in India.\"*\n\n**Top Scorer's Structure:**\n- Divide your answer into 3 headings: (1) **Agricultural Factors**, (2) **Demographic & Economic Factors**, and (3) **Social & Cultural Factors**.\n- Under Social Factors, highlight expenditure on rituals and exploitation by moneylenders `(साहूकारों का शोषण / શાહુકારોનું શોષણ)`.",
        "difficulty": "Advanced",
        "bloom": "Apply"
    })

    # =========================================================================
    # MODULE 5: POVERTY ALLEVIATION PROGRAMMES (PAPs) & WELFARE SCHEMES
    # =========================================================================
    blocks.append({
        "type": "theory",
        "title": "Government Strategy & Poverty Alleviation Programmes (PAPs)",
        "content": "The Government of India and the State Governments launched structured multi-dimensional programmes to eradicate poverty. These are categorized under five major strategies:\n\n### 1. Wage-Employment & Self-Employment Programmes:\n- **MGNREGA (Mahatma Gandhi National Rural Employment Guarantee Act - 2005) `(मनरेगा)`:**\n  - **Legal Guarantee:** Guarantees a minimum of **100 days of wage employment** in a financial year to every rural household whose adult members volunteer to do unskilled manual labour `(अकुशल शारीरिक श्रम / અકુશળ શારીરિક શ્રમ)`.\n  - **Women Reservation:** Mandatory **1/3 (33%) reservation for women**.\n  - **Workplace Proximity:** Work provided within a **5 km radius** of the village. If beyond 5 km, an additional **10% extra wage** is provided for travel.\n  - **Unemployment Allowance `(बेरोज़गारी भत्ता / બેરોજગારી ભથ્થું)`:** If the government fails to provide employment within **15 days of application**, it is legally bound to pay daily unemployment allowance!\n  - **Asset Creation:** Construction of village ponds, canals, tree plantations, flood control, rural roads, water conservation.\n\n### 2. Agriculture & Irrigation Schemes:\n- **Pradhan Mantri Krishi Sinchayee Yojana (PMKSY) `(प्रधानमंत्री कृषि सिंचाई योजना)`:**\n  - Motto: *'Har Khet Ko Pani'* (Water to every farm) and *'More Crop Per Drop'*. Promotes drip irrigation `(टपक सिंचाई / ટપક સિંચાઈ)` and check dams.\n- **Pradhan Mantri Fasal Bima Yojana (PMFBY) `(प्रधानमंत्री फसल बीमा योजना)`:**\n  - Comprehensive crop insurance protecting farmers against drought, flood, pests, and natural disasters.\n\n### 3. Food Security & Nutrition:\n- **National Food Security Act (NFSA - 2013) / Maa Annapurna Yojana:**\n  - Supplies highly subsidized food grains through Fair Price Shops (PDS / PDS Shops):\n    - **Rice @ ₹3 per kg**\n    - **Wheat @ ₹2 per kg**\n    - **Coarse grains @ ₹1 per kg**\n  - Under **Antyodaya Anna Yojana (AAY)**, the poorest of the poor families receive **35 kg food grains per family per month** for free or nominal rates.\n\n### 4. Housing & Infrastructure:\n- **Pradhan Mantri Awas Yojana (PMAY - Gramin & Urban) `(प्रधानमंत्री आवास योजना)`:**\n  - Provides financial assistance to construct permanent pucca houses `(पक्के मकान / પાકાં મકાનો)` equipped with toilets, electricity, and clean drinking water.\n\n### 5. Women Empowerment & Rural Livelihoods:\n- **Mission Mangalam / Sakhi Mandals (SHGs - Self Help Groups) `(मिशन मंगलम / સખી મંડળ)`:**\n  - Mobilizes rural women into self-help groups for micro-financing, skill training, and producing items like papad, pickles, incense sticks `(अगरबत्ती / અગરબત્તી)`, and handicraft items.\n- **Dattopant Thengadi Artisan Interest Subsidy Scheme & Jyotigram Yojana (Gujarat State):**\n  - Financial credit and 24x7 rural power supply for cottage and village industries.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "The Pillars of MGNREGA: 100 Days Guaranteed Wage Employment ➔ 1/3 Women Quota ➔ Within 5 km Radius ➔ 15-Day Unemployment Allowance Rule ➔ Creation of Durable Rural Water & Soil Assets.",
        "image_url": "assets/images/ss_ch17_mgnrega_pillars.jpg",
        "alt_text": "Pillars of MGNREGA visual infographic showing key statutory provisions."
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "Under the MGNREGA scheme, if an applicant is not provided wage employment within 15 days of applying, what legal provision comes into effect?",
            "options": [
                "The applicant is allotted free agricultural land.",
                "The government must pay a daily Unemployment Allowance to the applicant.",
                "The application is automatically cancelled.",
                "The applicant is shifted to an urban industrial factory."
            ],
            "correct_answer": "The government must pay a daily Unemployment Allowance to the applicant.",
            "explanation": "MGNREGA is an enforceable legal right: if work is not allotted within 15 days of demand, the state government must pay a statutory Unemployment Allowance (बेरोज़गारी भत्ता / બેરોજગારી ભથ્થું)."
        },
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    # =========================================================================
    # MODULE 6: CONCEPT OF UNEMPLOYMENT & 7 MAJOR TYPES
    # =========================================================================
    blocks.append({
        "type": "theory",
        "title": "Concept of Unemployment (बेरोज़गारी की परिभाषा)",
        "content": "An individual is defined as **Unemployed `(बेरोज़गार / બેરોજગાર)`** when:\n1. He/she belongs to the active working age group of **15 to 60 years**.\n2. Is physically and mentally **capable of working `(काम करने में समर्थ / કામ કરવા માટે સક્ષમ)`**.\n3. Is **willing to work `(काम करने की इच्छा / કામ કરવાની ઇચ્છા)`** at the prevailing market wage rate `(प्रचलित वेतन दर / પ્રવર્તમાન વેતન દર)`.\n4. Is **actively seeking work `(काम की तलाश में / કામની શોધમાં)`**, but fails to obtain employment.\n\n### Who is NOT counted as Unemployed?\n- Children below 15 years and elderly above 60 years.\n- Physically challenged or sick persons incapable of work.\n- Housewives engaged voluntarily in domestic chores.\n- Wealthy or lazy individuals who do not wish to work despite being capable.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "title": "The 7 Major Types of Unemployment in India",
        "content": "Unemployment in India manifests in 7 distinct forms:\n\n1. **Seasonal Unemployment `(मौसमी बेरोज़गारी / મોસમી બેરોજગારી)`:**\n   - In rural India, due to lack of perennial irrigation facilities and dependence on rainfall, farmers and agricultural labourers find work only during sowing and harvesting seasons. For **3 to 5 months** during the dry season, they remain completely jobless.\n\n2. **Disguised / Hidden Unemployment `(प्रच्छन्न या छुपी हुई बेरोज़गारी / પ્રચ્છન્ન બેરોજગારી)`:**\n   - A situation where **more workers are engaged in an activity than actually required**.\n   - If surplus workers are withdrawn from the work, **total production does NOT decrease at all**!\n   - In economic terms: **The Marginal Productivity `(सीमांत उत्पादकता / સીમાંત ઉત્પાદકતા)` of surplus labour is ZERO**.\n   - *Example:* On a 2-acre farm, 4 family members are sufficient to produce 50 quintals of wheat. But all 8 family members are working on the same field, producing the exact same 50 quintals. Those 4 extra persons are disguisedly unemployed!\n\n3. **Frictional Unemployment `(घर्षणात्मक बेरोज़गारी / ઘર્ષણાત્મક બેરોજગારી)`:**\n   - Occurs when workers are in the process of moving from old technology to new technology, or transitioning between jobs.\n   - *Example:* When computerized accounting was introduced, manual bookkeepers remained temporarily unemployed until they learned computer accounting software.\n\n4. **Structural Unemployment `(ढांचागत बेरोज़गारी / માળખાગત બેરોજગારી)`:**\n   - Arises from deep-rooted structural backwardness `(मांग और आपूर्ति का असंतुलન / માળખાકીય પછાતપણું)`, obsolete technology, orthodox social customs, or a mismatch between available worker skills and required industry jobs.\n\n5. **Industrial Unemployment `(औद्योगिक बेरोज़गारी / ઔદ્યોગિક બેરોજગારી)`:**\n   - Occurs in industrial urban sectors when workers lose jobs due to industrial closures, raw material shortages, power cuts, or recessions in the manufacturing sector.\n\n6. **Educated Unemployment `(शिक्षित बेरोज़गारी / શિક્ષિત બેરોજગારી)`:**\n   - When individuals who have acquired at least secondary education (Matriculation/10th pass), higher secondary, or university graduation degrees fail to secure suitable employment matching their qualifications.\n\n7. **Cyclical Unemployment `(चक्रीय बेरोज़गारी / ચક્રીય બેરોજગારી)`:**\n   - Generated by macroeconomic business cycles of **Boom `(तेजी / તેજી)`** and **Recession / Depression `(मंदी / મંદી)`** in capitalist market economies. During a depression, consumer demand crashes, factories cut production, and mass layoffs occur.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Disguised Unemployment Illustrated: 8 Workers on a farm ➔ Total Output = 50 Bags of Wheat. 4 Workers removed ➔ Total Output is STILL 50 Bags of Wheat! The 4 extra workers contributed ZERO additional output (Marginal Productivity = 0).",
        "image_url": "assets/images/ss_ch17_disguised_unemployment.jpg",
        "alt_text": "Visual illustration of disguised unemployment showing zero marginal productivity."
    })
    
    blocks.append({
        "type": "memory_trick",
        "content": "🧠 **Memory Mnemonic for 7 Types of Unemployment: 'S-F-S-I-D-E-C'**\n- **S** - **S**easonal `(मौसमी)`\n- **F** - **F**rictional `(घर्षणात्मक)`\n- **S** - **S**tructural `(ढांचागत)`\n- **I** - **I**ndustrial `(औद्योगिक)`\n- **D** - **D**isguised `(प्रच्छन्न / छुपी हुई)`\n- **E** - **E**ducated `(शिक्षित)`\n- **C** - **C**yclical `(चक्रीय)`",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "If removing 3 workers from an agricultural farm causes no decrease in total farm output, what type of unemployment were those 3 workers experiencing?",
            "options": [
                "Cyclical Unemployment",
                "Frictional Unemployment",
                "Disguised (Hidden) Unemployment",
                "Educated Unemployment"
            ],
            "correct_answer": "Disguised (Hidden) Unemployment",
            "explanation": "Disguised unemployment occurs when excess workers are employed whose marginal contribution to total output is zero (removing them does not reduce total production)."
        },
        "difficulty": "Intermediate",
        "bloom": "Apply"
    })

    # =========================================================================
    # MODULE 7: CAUSES OF UNEMPLOYMENT & REMEDIAL MEASURES
    # =========================================================================
    blocks.append({
        "type": "theory",
        "title": "Causes of Unemployment in India",
        "content": "Why is unemployment mounting in India? Key causes include:\n\n1. **Demographic Pressure:** Enormous population growth creating millions of new job aspirants every year far outpacing job creation.\n2. **Theoretical & Flawed Education System:** School and college curricula emphasize rote memorization and degree accumulation without practical, technical, or vocational skills `(व्यावहारिक और व्यावसायिक कौशल / વ્યવહારુ અને વ્યાવસાયિક કૌશલ્ય)`.\n3. **Preference for Capital-Intensive Methods `(पूंजी-प्रधान तकनीक / મૂડી-પ્રધાન ઉત્પાદન પદ્ધતિ)`:** Increasing reliance on automation, heavy machinery, and computers in industries replaces human labour, causing jobless growth.\n4. **Decay of Cottage and Village Industries:** Lack of credit, modern marketing, and design support ruined traditional rural handicraft livelihoods.\n5. **Immobility of Labour `(श्रम की गतिहीनता / શ્રમની ગતિહીનતા)`:** Linguistic barriers, family ties, caste attachments, and lack of housing prevent rural youth from migrating to urban job centers.\n6. **Lack of Entrepreneurship & Risk-Taking Spirit:** Students are conditioned to seek government or secure corporate white-collar jobs rather than creating enterprises.",
        "difficulty": "Intermediate",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "theory",
        "title": "Remedial Measures & Policy Solutions to Reduce Unemployment",
        "content": "To systematically eradicate unemployment, the government has adopted comprehensive policy measures:\n\n### 1. Promotion of Labour-Intensive Techniques `(श्रम-प्रधान उत्पादन पद्धति / શ્રમ-પ્રધાન પદ્ધતિ)`:\n- Prioritizing small-scale, cottage, handloom, and agro-processing industries (MSMEs) that generate maximum employment per unit of capital invested.\n\n### 2. Vocationalisation of Education & Skill Development:\n- Transforming the education system through the **National Skill Development Mission**, setting up ITIs (Industrial Training Institutes), and **Kaushalya Vardhan Kendras (KVK)** in Gujarat.\n- **Pradhan Mantri Kaushal Vikas Yojana (PMKVY)** providing certified vocational training in electronics, plumbing, automotive, IT, and healthcare.\n\n### 3. Fostering Entrepreneurship and Self-Employment:\n- **Start-Up India `(स्टार्ट-अप इंडिया)`** and **Stand-Up India `(स्टैंड-अप इंडिया)`**: Providing tax holidays, incubation, and mentorship to young innovators.\n- **Pradhan Mantri MUDRA Yojana (PMMY) `(मुद्रा योजना)`**: Offering collateral-free loans to micro-enterprises across three categories: **Shishu** (up to ₹50,000), **Kishore** (₹50,000 to ₹5 Lakhs), and **Tarun** (₹5 Lakhs to ₹10 Lakhs).\n\n### 4. Rural Infrastructure & Agro-allied Industries:\n- Expanding animal husbandry, dairy farming, poultry, fisheries, horticulture, organic farming, and food processing to create year-round rural jobs.\n\n### 5. Employment Exchange Centers & Digital Portals:\n- **Employment Exchanges `(रोज़गार विनिमय केंद्र / રોજગાર વિનિમય કેન્દ્રો)`** registered across all districts register job-seekers and match them with public/private employers.\n- Modernization via the **National Career Service (NCS) portal** and state portals (such as Rojgar Setu / Anubandham app in Gujarat) providing online job fairs, aptitude tests, and career counseling.",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "The 4-Way Policy Engine to Cure Unemployment: Labour-Intensive MSMEs + Vocational Skill Training (PMKVY) + Collateral-Free Loans (MUDRA) + Digital Job Placement (National Career Service).",
        "image_url": "assets/images/ss_ch17_unemployment_solutions.jpg",
        "alt_text": "Strategic diagram of governmental measures to eradicate unemployment in India."
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "Which scheme provides collateral-free institutional credit up to ₹10 Lakhs to micro-entrepreneurs under Shishu, Kishore, and Tarun categories?",
            "options": [
                "Pradhan Mantri Fasal Bima Yojana",
                "Pradhan Mantri MUDRA Yojana",
                "Mission Mangalam",
                "Sansad Adarsh Gram Yojana"
            ],
            "correct_answer": "Pradhan Mantri MUDRA Yojana",
            "explanation": "Pradhan Mantri MUDRA Yojana (PMMY) provides collateral-free loans for self-employment and micro-enterprises under three categories: Shishu (up to ₹50k), Kishore (₹50k-₹5L), and Tarun (₹5L-₹10L)."
        },
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    # =========================================================================
    # MODULE 8: BOARD EXAM MASTERY, HOTS & MODEL ANSWERS
    # =========================================================================
    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **SUPER-HOT BOARD EXAM QUESTIONS (Repeated in Board Papers):**\n\n1. **Q: Write a short note on MGNREGA.** (4 Marks)\n   - *Checklist for 4/4 marks:* Mention full name + 2005 year, 100 days wage guarantee, unskilled manual labour, 1/3 quota for women, within 5 km rule (10% extra wage if beyond), and 15-day Unemployment Allowance rule.\n\n2. **Q: Differentiate between Absolute Poverty and Relative Poverty with examples.** (3 Marks)\n   - *Checklist for 3/3 marks:* Draw a clear 2-column table comparing Concept, Minimum Subsistence vs Inequality, and Countries where prevalent (Developing vs Developed).\n\n3. **Q: Explain Disguised Unemployment with an agricultural example.** (2-3 Marks)\n   - *Checklist:* Define surplus workers, explain that marginal productivity equals zero, and use the 2-acre farm family example.",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "Which of the following is a key objective of Kaushalya Vardhan Kendras (KVK) established in Gujarat?",
            "options": [
                "To distribute free agricultural land to urban dwellers.",
                "To impart job-oriented vocational and technical skill training to rural youth.",
                "To operate international stock exchanges.",
                "To manage commercial airlines."
            ],
            "correct_answer": "To impart job-oriented vocational and technical skill training to rural youth.",
            "explanation": "Kaushalya Vardhan Kendras (KVK) in Gujarat were set up to provide short-term, employment-oriented vocational training to rural youth according to local market needs."
        },
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "summary",
        "content": "📌 **CHAPTER 17 RECAP SUMMARY:**\n- **Poverty** = Inability to fulfill basic needs (food, clothing, shelter, education, healthcare). BPL benchmark first proposed by Lord Boyd Orr.\n- **Calorie Standard** = 2400 kcal (Rural) vs 2100 kcal (Urban). Tendulkar Line = ₹816 (Rural) vs ₹1000 (Urban) per month.\n- **Absolute Poverty** = Deprivation below subsistence; **Relative Poverty** = Income inequality between groups.\n- **Poverty Rate** = India 21.9%, Highest in Chhattisgarh (39.93%), Lowest in Goa (5.09%), Gujarat (16.63%).\n- **Key PAP Schemes** = MGNREGA (100 days work guarantee, 1/3 women), PMKSY ('More crop per drop'), NFSA/Maa Annapurna (Rice @ ₹3, Wheat @ ₹2), PMAY (Pucca houses), Sakhi Mandals.\n- **Unemployment** = Age 15-60, capable, willing, searching at current wages, but unable to find work.\n- **7 Types** = Seasonal, Disguised (Marginal Product = 0), Frictional, Structural, Industrial, Educated, Cyclical.\n- **Solutions** = Labour-intensive techniques, PMKVY skill training, MUDRA loans (Shishu, Kishore, Tarun), Start-Up India, Employment Exchanges & National Career Service portal.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_dir = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters"
    os.makedirs(out_dir, exist_ok=True)
    
    # Save for GSEB
    gseb_path = os.path.join(out_dir, "gseb_class10_social_science_ch17.json")
    with open(gseb_path, "w", encoding="utf-8") as f:
        json.dump(final_json, f, indent=2, ensure_ascii=False)
        
    # Save for NCERT / Universal
    ncert_path = os.path.join(out_dir, "ncert_class10_social_science_ch17.json")
    final_json_ncert = json.loads(json.dumps(final_json))
    final_json_ncert["metadata"]["id"] = "ncert_class10_social_science_ch17"
    with open(ncert_path, "w", encoding="utf-8") as f:
        json.dump(final_json_ncert, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully generated Supreme SS Chapter 17 files:\n1. {gseb_path}\n2. {ncert_path}")

if __name__ == "__main__":
    generate_supreme_gseb_ss_ch17()
