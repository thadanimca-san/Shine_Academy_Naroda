import json
import os

def generate_supreme_gseb_ss_ch10():
    chapter_id = "gseb_class10_social_science_ch10"
    title = "Chapter 10: India: Agriculture"
    
    metadata = {
        "id": chapter_id,
        "title": title,
        "subtitle": "The Ultimate Board Exam Mastery Guide (ભારત: કૃષિ / भारत: कृषि)",
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
            "geography",
            "india_agriculture",
            "farming_types",
            "kharif_rabi_zaid",
            "food_grains",
            "cash_crops",
            "oilseeds",
            "green_revolution",
            "institutional_reforms",
            "technical_reforms",
            "board_special",
            "bilingual"
        ],
        "learning_outcomes": [
            "Understand the pivotal role and contribution of agriculture in India's national economy.",
            "Classify and distinguish between the 6 major farming types (Subsistence, Dry, Wet, Shifting, Plantation, Intensive).",
            "Analyze modern eco-friendly farming methods including Organic farming, Sustainable farming, and Mixed farming.",
            "Identify the climatic, soil, and geographical requirements of major food grains, pulses, oilseeds, beverages, and cash crops.",
            "Evaluate Technical and Institutional reforms introduced in Indian agriculture (KCC, APMC, MSP, PMFBY, Soil Health Card).",
            "Explain the genesis and impact of the Green Revolution and examine India's food security and globalization challenges.",
            "Locate and label major agricultural crop regions on the political map of India for Board Examinations."
        ],
        "ai_context": {
            "learning_goal": "Transform the student from a beginner to a board-exam topper in India: Agriculture using the 8-step EduOS Gold Learning Cycle, Socratic questioning, real-world examples, and bilingual terminology.",
            "common_misconceptions": [
                "Students confuse Kharif (Monsoon) and Rabi (Winter) cropping seasons and sowing/harvesting months.",
                "Students assume all pulses fix nitrogen equally (Fact: Arhar/Tur does not fix nitrogen after harvesting as efficiently).",
                "Students mistake Subsistence farming for Organic farming (Fact: Subsistence is poverty-driven with low yield, whereas Organic is a scientific method avoiding synthetic chemicals).",
                "Students confuse Technical reforms (machines, seeds, irrigation, tech apps) with Institutional reforms (laws, tenancy, land ceiling, banks, MSP, APMC)."
            ]
        }
    }
    
    blocks = []
    
    # ==========================================
    # MODULE 1: HOOK & IMPORTANCE OF AGRICULTURE
    # ==========================================
    blocks.append({
        "type": "hook",
        "title": "The Beating Heart of 1.4 Billion People",
        "content": "Imagine a nation where over 1.4 billion people sit down for breakfast, lunch, and dinner every single day without fail. Where does all that food come from? What if nearly 60% of an entire nation's workforce is dedicated to cultivating the soil?\n\nAgriculture `(कृषि / ખેતી)` is not just an occupation in India; it is the ancient foundation of our civilization, culture, festivals, and national economy `(राष्ट्रीय अर्थव्यवस्था / રાષ્ટ્રીય અર્થતંત્ર)`!\n\nLet us embark on a journey across India's fertile plains, golden wheat bowls, lush green tea slopes, and cotton belts to master **Chapter 10: India: Agriculture**.",
        "body": "Imagine a nation where over 1.4 billion people sit down for breakfast, lunch, and dinner every single day without fail. Where does all that food come from? What if nearly 60% of an entire nation's workforce is dedicated to cultivating the soil?\n\nAgriculture `(कृषि / ખેતી)` is not just an occupation in India; it is the ancient foundation of our civilization, culture, festivals, and national economy `(राष्ट्रीय अर्थव्यवस्था / રાષ્ટ્રીય અર્થતંત્ર)`!\n\nLet us embark on a journey across India's fertile plains, golden wheat bowls, lush green tea slopes, and cotton belts to master **Chapter 10: India: Agriculture**.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "title": "Indian Agricultural Diversity",
        "content": "Diverse agro-climatic zones across India enable the cultivation of almost every known crop on Earth—from tropical paddy in the south to temperate apples in Kashmir.",
        "body": "Diverse agro-climatic zones across India enable the cultivation of almost every known crop on Earth—from tropical paddy in the south to temperate apples in Kashmir.",
        "image_url": "assets/images/ss_ch10_agriculture_overview.jpg",
        "alt_text": "Lush green agricultural fields in India showing diverse farming activities across different states."
    })
    
    blocks.append({
        "type": "theory",
        "title": "Significance of Agriculture in the Indian Economy",
        "content": "Agriculture has been the primary economic activity `(प्राथमिक आर्थिक गतिविधि / પ્રાથમિક આર્થિક પ્રવૃત્તિ)` in India since ancient times. Its vital importance can be understood through the following pillars:\n\n1. **Employment Provider `(रोजगार प्रदाता / રોજગારી આપનાર)`:** About **60%** of India's working population `(कार्यशील जनसंख्या / કાર્યકારી વસ્તી)` depends directly or indirectly on agriculture for their livelihood.\n2. **National Income & GDP Contribution `(राष्ट्रीय आय एवं सकल घरेलू उत्पाद में योगदान / રાષ્ટ્રીય આવક અને જીડીપીમાં પ્રદાન)`:** Agriculture contributes approximately **16% to 17%** to India's Gross Domestic Product (GDP).\n3. **Food Security `(खाद्य सुरक्षा / અન્ન સુરક્ષા)`:** It produces food grains `(खाद्यान्न / અનાજ)`—such as rice, wheat, maize, millets, and pulses—to feed India's massive population of over 1.4 billion people.\n4. **Raw Material for Industries `(उद्योगों के लिए कच्चा माल / ઉદ્યોગો માટે કાચો માલ)`:** Key agro-based manufacturing industries `(कृषि आधारित उद्योग / કૃષિ આધારિત ઉદ્યોગો)` depend entirely on agriculture for raw materials:\n   - Cotton textile industry `(सूती वस्त्र उद्योग / સુતરાઉ કાપડ ઉદ્યોગ)` depends on cotton.\n   - Jute industry `(पटसन उद्योग / શણ ઉદ્યોગ)` depends on raw jute.\n   - Sugar industry `(चीनी उद्योग / ખાંડ ઉદ્યોગ)` depends on sugarcane.\n   - Edible oil industry `(खाद्य तेल उद्योग / ખાદ્યતેલ ઉદ્યોગ)` depends on oilseeds like groundnut, mustard, and sesame.\n   - Paper, rubber, and food processing industries.\n5. **Foreign Exchange Earner `(विदेशी मुद्रा अर्जक / વિદેશી હૂંડિયામણ કમાવનાર)`:** Agricultural products and processed agro-goods account for about **18%** of India's total exports `(निर्यात / નિકાસ)`. Key exports include Tea `(चाय / ચા)`, Basmati Rice, Spices `(मसाले / મસાલા)`, Tobacco `(तंबाकू / તમાકુ)`, Jute goods, Cotton, and Oil meals.",
        "body": "Agriculture has been the primary economic activity `(प्राथमिक आर्थिक गतिविधि / પ્રાથમિક આર્થિક પ્રવૃત્તિ)` in India since ancient times. Its vital importance can be understood through the following pillars:\n\n1. **Employment Provider `(रोजगार प्रदाता / રોજગારી આપનાર)`:** About **60%** of India's working population `(कार्यशील जनसंख्या / કાર્યકારી વસ્તી)` depends directly or indirectly on agriculture for their livelihood.\n2. **National Income & GDP Contribution `(राष्ट्रीय आय एवं सकल घरेलू उत्पाद में योगदान / રાષ્ટ્રીય આવક અને જીડીપીમાં પ્રદાન)`:** Agriculture contributes approximately **16% to 17%** to India's Gross Domestic Product (GDP).\n3. **Food Security `(खाद्य सुरक्षा / અન્ન સુરક્ષા)`:** It produces food grains `(खाद्यान्न / અનાજ)`—such as rice, wheat, maize, millets, and pulses—to feed India's massive population of over 1.4 billion people.\n4. **Raw Material for Industries `(उद्योगों के लिए कच्चा माल / ઉદ્યોગો માટે કાચો માલ)`:** Key agro-based manufacturing industries `(कृषि आधारित उद्योग / કૃષિ આધારિત ઉદ્યોગો)` depend entirely on agriculture for raw materials:\n   - Cotton textile industry `(सूती वस्त्र उद्योग / સુતરાઉ કાપડ ઉદ્યોગ)` depends on cotton.\n   - Jute industry `(पटसन उद्योग / શણ ઉદ્યોગ)` depends on raw jute.\n   - Sugar industry `(चीनी उद्योग / ખાંડ ઉદ્યોગ)` depends on sugarcane.\n   - Edible oil industry `(खाद्य तेल उद्योग / ખાદ્યતેલ ઉદ્યોગ)` depends on oilseeds like groundnut, mustard, and sesame.\n   - Paper, rubber, and food processing industries.\n5. **Foreign Exchange Earner `(विदेशी मुद्रा अर्जक / વિદેશી હૂંડિયામણ કમાવનાર)`:** Agricultural products and processed agro-goods account for about **18%** of India's total exports `(निर्यात / નિકાસ)`. Key exports include Tea `(चाय / ચા)`, Basmati Rice, Spices `(मसाले / મસાલા)`, Tobacco `(तंबाकू / તમાકુ)`, Jute goods, Cotton, and Oil meals.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "teacher_tip",
        "title": "Teacher's Cultural Insight",
        "content": "💡 **Cultural Connection:** In India, agriculture is deeply intertwined with culture. Almost all major harvest festivals celebrate agricultural cycles: **Makar Sankranti / Uttarayan** (Winter harvest), **Baisakhi** in Punjab (Rabi wheat harvest), **Pongal** in Tamil Nadu, **Onam** in Kerala, and **Bihu** in Assam! When crops flourish, the nation rejoices.",
        "body": "💡 **Cultural Connection:** In India, agriculture is deeply intertwined with culture. Almost all major harvest festivals celebrate agricultural cycles: **Makar Sankranti / Uttarayan** (Winter harvest), **Baisakhi** in Punjab (Rabi wheat harvest), **Pongal** in Tamil Nadu, **Onam** in Kerala, and **Bihu** in Assam! When crops flourish, the nation rejoices."
    })
    
    blocks.append({
        "type": "knowledge_check",
        "question": "What percentage of India's working population is engaged in agriculture, and what share of total exports do agricultural goods account for?",
        "options": [
            "40% working population, 5% exports",
            "About 60% working population, about 18% exports",
            "75% working population, 50% exports",
            "25% working population, 10% exports"
        ],
        "correct_index": 1,
        "correct_answer": "About 60% working population, about 18% exports",
        "explanation": "According to the GSEB Class 10 curriculum, about 60% of India's working population is engaged in agriculture, and agricultural products account for approximately 18% of India's total export earnings.",
        "feedback_correct": "Correct! Agriculture employs ~60% of our workforce and generates ~18% of export earnings.",
        "feedback_incorrect": "Incorrect. In India, ~60% of the working population depends on agriculture, contributing ~18% to total exports.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    # ==========================================
    # MODULE 2: TYPES OF FARMING IN INDIA
    # ==========================================
    blocks.append({
        "type": "theory",
        "title": "Types of Farming in India (કૃષિના પ્રકારો / कृषि के प्रकार)",
        "content": "Due to diverse physical features, soil types, rainfall patterns, irrigation facilities, and socio-economic conditions, six distinct types of farming are practiced across India:\n\n### 1. Subsistence Farming `(जीवन निर्वाह कृषि / જીવન નિર્વાહ ખેતી)`\n- **Nature:** Farming done primarily to fulfill the basic food requirements of the farmer's own family.\n- **Features:** Small and fragmented landholdings `(छोटे व खंडित खेत / નાના અને વિભાજિત ખેતરો)`, poor economic condition of farmers, use of traditional implements (wooden plough `(लकड़ी का हल / લાકડાનું હળ)`, sickle `(दरांती / દાતરડું)`), low application of fertilizers, and reliance on family labor.\n- **Output:** Almost the entire crop yield is consumed by the family; negligible or zero marketable surplus `(बाजार अधिशेष / બજાર વેચાણ)`.\n\n### 2. Dry Farming `(शुष्क कृषि / સૂકી ખેતી)`\n- **Nature:** Practiced in regions where rainfall is inadequate `(अल्प वर्षा / ઓછો વરસાદ)` (less than 75 cm) and irrigation facilities are scarce.\n- **Features:** Farming depends entirely on residual soil moisture `(मिट्टी की नमी / જમીનનો ભેજ)`. Only one crop is taken in an entire year.\n- **Crops:** Drought-tolerant crops like Jowar `(ज्वार / જુવાર)`, Bajra `(बाजरा / બાજરી)`, and Pulses `(दलहन / કઠોળ)`.\n- **Special Gujarat Feature:** In Gujarat's **Bhal region `(भाल क्षेत्र / ભાલ પ્રદેશ)`**, after the monsoon water recedes, the conserved soil moisture is used to cultivate premium **Bhalia Wheat `(भालिया गेहूँ / ભાલિયા ઘઉં)`** (Chasiya wheat) and Gram `(चना / ચણા)` without artificial irrigation!\n\n### 3. Wet / Humid Farming `(आर्द्र कृषि / ભીની ખેતી)`\n- **Nature:** Practiced in areas with heavy rainfall (>100 cm) or assured, abundant irrigation `(प्रचुर सिंचाई / વિપુલ સિંચાઈ)`.\n- **Features:** Multiple cropping `(बहुफसली प्रणाली / બહુવિધ પાક પદ્ધતિ)` is practiced; 2 to 3 crops are harvested per year from the same land.\n- **Crops:** Water-intensive crops like Paddy `(धान / ડાંગર)`, Sugarcane `(गन्ना / શેરડી)`, Cotton `(कपास / કપાસ)`, Wheat `(गेहूँ / ઘઉં)`, and Jute `(पटसन / શણ)`.\n\n### 4. Shifting / Jhum Cultivation `(स्थानांतरित अथवा झूम कृषि / સ્થળાંતરિત અથવા ઝૂમ ખેતી)`\n- **Nature:** Traditional slash-and-burn farming practiced by tribal communities in dense forest tracts.\n- **Method:** Trees and bushes are cut down and burnt `(जंगल काटकर जलाना / વૃક્ષો કાપીને બાળવા)`. Seeds are sown in the ash-enriched soil. Crops are grown for 2–3 years until natural soil fertility declines `(उर्वरता कम होना / ફળદ્રુપતા ઘટવી)`. Farmers then abandon the plot and move to a new forest patch.\n- **Drawback:** Per-hectare yield is very low, and it leads to heavy deforestation `(वनों की कटाई / જંગલોનો વિનાશ)`.\n\n### 5. Plantation Agriculture `(बागानी कृषि / બાગાયતી ખેતી)`\n- **Nature:** Large-scale commercial cultivation of a single perennial tree or bush crop over vast estates `(विशाल बागान / વિશાળ બગીચાઓ)`.\n- **Features:** Demands massive capital investment `(भारी पूंजी निवेश / વિશાળ મૂડીરોકાણ)`, technical expertise `(तकनीकी विशेषज्ञता / તકનીકી નિપુણતા)`, modern machinery, chemical fertilizers, insect control, rapid transport networks, and specialized on-site processing units `(प्रसंस्करण इकाइयाँ / પ્રક્રિયા એકમો)`.\n- **Crops:** Tea `(चाय / ચા)`, Coffee `(कॉफ़ी / કોફી)`, Rubber `(रबर / રબર)`, Cocoa `(कोको / કોકો)`, Coconut `(नारियल / નાળિયેર)`, Mango `(आम / કેરી)`, Apple `(सेब / સફરજન)`, Grapes `(अंगूर / દ્રાક્ષ)`, and Spices.\n\n### 6. Intensive Farming `(सघन कृषि / સઘન ખેતી)`\n- **Nature:** Highly mechanized, modern commercial farming designed to extract maximum output per hectare `(प्रति हेक्टेयर अधिकतम उत्पादन / હેક્ટર દીઠ મહત્તમ ઉત્પાદન)`.\n- **Features:** Extensive use of High Yielding Variety (HYV) seeds, chemical fertilizers, advanced insecticides, tube wells/canals, tractors, and modern combine harvesters.\n- **Cash Crop Dominance:** Farmers focus on profitable cash crops `(नकदी फसलें / રોકડિયા પાકો)` (Cotton, Sugarcane, Tobacco, Oilseeds). Also referred to as Commercial Farming `(व्यापारिक कृषि / વ્યાપારી ખેતી)`.",
        "body": "Due to diverse physical features, soil types, rainfall patterns, irrigation facilities, and socio-economic conditions, six distinct types of farming are practiced across India:\n\n### 1. Subsistence Farming `(जीवन निर्वाह कृषि / જીવન નિર્વાહ ખેતી)`\n- **Nature:** Farming done primarily to fulfill the basic food requirements of the farmer's own family.\n- **Features:** Small and fragmented landholdings `(छोटे व खंडित खेत / નાના અને વિભાજિત ખેતરો)`, poor economic condition of farmers, use of traditional implements (wooden plough `(लकड़ी का हल / લાકડાનું હળ)`, sickle `(दरांती / દાતરડું)`), low application of fertilizers, and reliance on family labor.\n- **Output:** Almost the entire crop yield is consumed by the family; negligible or zero marketable surplus `(बाजार अधिशेष / બજાર વેચાણ)`.\n\n### 2. Dry Farming `(शुष्क कृषि / સૂકી ખેતી)`\n- **Nature:** Practiced in regions where rainfall is inadequate `(अल्प वर्षा / ઓછો વરસાદ)` (less than 75 cm) and irrigation facilities are scarce.\n- **Features:** Farming depends entirely on residual soil moisture `(मिट्टी की नमी / જમીનનો ભેજ)`. Only one crop is taken in an entire year.\n- **Crops:** Drought-tolerant crops like Jowar `(ज्वार / જુવાર)`, Bajra `(बाजरा / બાજરી)`, and Pulses `(दलहन / કઠોળ)`.\n- **Special Gujarat Feature:** In Gujarat's **Bhal region `(भाल क्षेत्र / ભાલ પ્રદેશ)`**, after the monsoon water recedes, the conserved soil moisture is used to cultivate premium **Bhalia Wheat `(भालिया गेहूँ / ભાલિયા ઘઉં)`** (Chasiya wheat) and Gram `(चना / ચણા)` without artificial irrigation!\n\n### 3. Wet / Humid Farming `(आर्द्र कृषि / ભીની ખેતી)`\n- **Nature:** Practiced in areas with heavy rainfall (>100 cm) or assured, abundant irrigation `(प्रचुर सिंचाई / વિપુલ સિંચાઈ)`.\n- **Features:** Multiple cropping `(बहुफसली प्रणाली / બહુવિધ પાક પદ્ધતિ)` is practiced; 2 to 3 crops are harvested per year from the same land.\n- **Crops:** Water-intensive crops like Paddy `(धान / ડાંગર)`, Sugarcane `(गन्ना / શેરડી)`, Cotton `(कपास / કપાસ)`, Wheat `(गेहूँ / ઘઉં)`, and Jute `(पटसन / શણ)`.\n\n### 4. Shifting / Jhum Cultivation `(स्थानांतरित अथवा झूम कृषि / સ્થળાંતરિત અથવા ઝૂમ ખેતી)`\n- **Nature:** Traditional slash-and-burn farming practiced by tribal communities in dense forest tracts.\n- **Method:** Trees and bushes are cut down and burnt `(जंगल काटकर जलाना / વૃક્ષો કાપીને બાળવા)`. Seeds are sown in the ash-enriched soil. Crops are grown for 2–3 years until natural soil fertility declines `(उर्वरता कम होना / ફળદ્રુપતા ઘટવી)`. Farmers then abandon the plot and move to a new forest patch.\n- **Drawback:** Per-hectare yield is very low, and it leads to heavy deforestation `(वनों की कटाई / જંગલોનો વિનાશ)`.\n\n### 5. Plantation Agriculture `(बागानी कृषि / બાગાયતી ખેતી)`\n- **Nature:** Large-scale commercial cultivation of a single perennial tree or bush crop over vast estates `(विशाल बागान / વિશાળ બગીચાઓ)`.\n- **Features:** Demands massive capital investment `(भारी पूंजी निवेश / વિશાળ મૂડીરોકાણ)`, technical expertise `(तकनीकी विशेषज्ञता / તકનીકી નિપુણતા)`, modern machinery, chemical fertilizers, insect control, rapid transport networks, and specialized on-site processing units `(प्रसंस्करण इकाइयाँ / પ્રક્રિયા એકમો)`.\n- **Crops:** Tea `(चाय / ચા)`, Coffee `(कॉफ़ी / કોફી)`, Rubber `(रबर / રબર)`, Cocoa `(कोको / કોકો)`, Coconut `(नारियल / નાળિયેર)`, Mango `(आम / કેરી)`, Apple `(सेब / સફરજન)`, Grapes `(अंगूर / દ્રાક્ષ)`, and Spices.\n\n### 6. Intensive Farming `(सघन कृषि / સઘન ખેતી)`\n- **Nature:** Highly mechanized, modern commercial farming designed to extract maximum output per hectare `(प्रति हेक्टेयर अधिकतम उत्पादन / હેક્ટર દીઠ મહત્તમ ઉત્પાદન)`.\n- **Features:** Extensive use of High Yielding Variety (HYV) seeds, chemical fertilizers, advanced insecticides, tube wells/canals, tractors, and modern combine harvesters.\n- **Cash Crop Dominance:** Farmers focus on profitable cash crops `(नकदी फसलें / રોકડિયા પાકો)` (Cotton, Sugarcane, Tobacco, Oilseeds). Also referred to as Commercial Farming `(व्यापारिक कृषि / વ્યાપારી ખેતી)`.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "teacher_tip",
        "title": "GSEB Board Special: Bhal Region Wheat",
        "content": "⭐ **GSEB Board Golden Question:** *How is wheat grown in the Bhal region of Gujarat without irrigation?*\n**Answer Blueprint:** In Gujarat's Bhal region (spread across Ahmedabad, Bhavnagar, and Anand districts), monsoon rainwater accumulates in the flat clayey plains. After the water recedes post-monsoon (September-October), the conserved soil moisture `(जमीन का नमी / જમીનનો સંગ્રહાયેલો ભેજ)` is utilized to sow **Bhalia Wheat (Chasiya wheat)**. It grows purely on moisture without a single drop of canal or well irrigation!",
        "body": "⭐ **GSEB Board Golden Question:** *How is wheat grown in the Bhal region of Gujarat without irrigation?*\n**Answer Blueprint:** In Gujarat's Bhal region (spread across Ahmedabad, Bhavnagar, and Anand districts), monsoon rainwater accumulates in the flat clayey plains. After the water recedes post-monsoon (September-October), the conserved soil moisture `(जमीन का नमी / જમીનનો સંગ્રહાયેલો ભેજ)` is utilized to sow **Bhalia Wheat (Chasiya wheat)**. It grows purely on moisture without a single drop of canal or well irrigation!"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "question": "Which type of farming involves clearing forest land by burning trees, growing crops for 2-3 years, and moving to a new plot when fertility drops?",
        "options": [
            "Plantation Agriculture",
            "Shifting / Jhum Cultivation",
            "Intensive Farming",
            "Dry Farming"
        ],
        "correct_index": 1,
        "correct_answer": "Shifting / Jhum Cultivation",
        "explanation": "Shifting cultivation (also known as Jhum cultivation) is a traditional slash-and-burn method where forest patches are cleared, cultivated for a few years, and then abandoned when soil fertility declines.",
        "feedback_correct": "Spot on! Shifting / Jhum cultivation is the slash-and-burn farming method.",
        "feedback_incorrect": "Incorrect. Shifting or Jhum cultivation involves slashing and burning forest patches and shifting when fertility declines.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    # ==========================================
    # MODULE 3: FARMING METHODS & SYSTEMS
    # ==========================================
    blocks.append({
        "type": "theory",
        "title": "Farming Methods (કૃષિ પદ્ધતિઓ / कृषि पद्धतियाँ)",
        "content": "To safeguard ecology, soil fertility, and human health, Indian agriculture utilizes three key sustainable farming methods:\n\n### 1. Organic Farming `(जैविक कृषि / સજીવ ખેતી)`\n- **Core Principle:** Complete avoidance of chemical fertilizers `(रासायनिक उर्वरक / રાસાયણિક ખાતરો)` (Urea, DAP) and synthetic toxic insecticides `(जहरीले कीटनाशक / ઝેરી જંતુનાશકો)`.\n- **Natural Nutrients:** Uses cow dung manure `(गोबर की खाद / છાણીયું ખાતર)`, earthworm manure / vermicompost `(केंचुआ खाद / અળસિયાનું ખાતર)`, farm compost `(कंपोस्ट खाद / કમ્પોસ્ટ ખાતર)`, and oil cakes.\n- **Natural Pest Control:** Neem solution `(नीम का काढ़ा / લીમડાનું અર્ક)`, sour buttermilk `(खट्टी छाछ / ખાટી છાશ)`, and cow urine `(गोमूत्र / ગૌમૂત્ર)` protect crops from insects and fungal diseases.\n- **Benefits:** Retains natural taste, sweetness, aroma, and high nutritional value. Organic food commands premium market prices and has immense export demand worldwide.\n\n### 2. Sustainable Farming `(संधारणीय कृषि / ટકાઉ ખેતી)`\n- **Goal:** Maintaining soil fertility `(मिट्टी की उर्वरता / જમીનની ફળદ્રુપતા)` intact for generations while meeting present agricultural needs.\n- **Key Practices:**\n  - Systematic Crop Rotation `(फसल चक्र / પાકની ફેરબદલી)` (e.g., alternating cereals with nitrogen-fixing pulses).\n  - Balanced use of chemical nutrients only when needed, supplemented by bio-fertilizers `(जैव उर्वरक / જૈવિક ખાતરો)`.\n  - Water harvesting, drip irrigation, and soil moisture conservation `(नमी संरक्षण / ભેજ સંરક્ષણ)`.\n  - Integrated Pest Management (IPM) using biological predator insects.\n\n### 3. Mixed Farming `(मिश्रित कृषि / મિશ્ર ખેતી)`\n- **Concept:** Cultivating crops simultaneously alongside allied agricultural activities `(संबद्ध कृषि गतिविधियाँ / સહાયક કૃષિ પ્રવૃત્તિઓ)` on the same farm.\n- **Allied Activities Include:**\n  - Cattle rearing & Dairy farming `(पशुपालन एवं डेयरी उद्योग / પશુપાલન અને ડેરી ઉદ્યોગ)`\n  - Poultry farming `(मुर्गी पालन / મરઘાં પાલન)`\n  - Sericulture / Silk farming `(रेशम कीट पालन / રેશમ કીડા ઉછેર)`\n  - Apiculture / Beekeeping `(मधुमक्खी पालन / મધમાખી પાલન)`\n  - Pisciculture / Fish farming `(मत्स्य पालन / મત્સ્ય પાલન)`\n- **Advantage:** Provides year-round supplementary income `(पूरक आय / પૂરક આવક)` to farmers and reduces risks associated with crop failure.",
        "body": "To safeguard ecology, soil fertility, and human health, Indian agriculture utilizes three key sustainable farming methods:\n\n### 1. Organic Farming `(जैविक कृषि / સજીવ ખેતી)`\n- **Core Principle:** Complete avoidance of chemical fertilizers `(रासायनिक उर्वरक / રાસાયણિક ખાતરો)` (Urea, DAP) and synthetic toxic insecticides `(जहरीले कीटनाशक / ઝેરી જંતુનાશકો)`.\n- **Natural Nutrients:** Uses cow dung manure `(गोबर की खाद / છાણીયું ખાતર)`, earthworm manure / vermicompost `(केंचुआ खाद / અળસિયાનું ખાતર)`, farm compost `(कंपोस्ट खाद / કમ્પોસ્ટ ખાતર)`, and oil cakes.\n- **Natural Pest Control:** Neem solution `(नीम का काढ़ा / લીમડાનું અર્ક)`, sour buttermilk `(खट्टी छाछ / ખાટી છાશ)`, and cow urine `(गोमूत्र / ગૌમૂત્ર)` protect crops from insects and fungal diseases.\n- **Benefits:** Retains natural taste, sweetness, aroma, and high nutritional value. Organic food commands premium market prices and has immense export demand worldwide.\n\n### 2. Sustainable Farming `(संधारणीय कृषि / ટકાઉ ખેતી)`\n- **Goal:** Maintaining soil fertility `(मिट्टी की उर्वरता / જમીનની ફળદ્રુપતા)` intact for generations while meeting present agricultural needs.\n- **Key Practices:**\n  - Systematic Crop Rotation `(फसल चक्र / પાકની ફેરબદલી)` (e.g., alternating cereals with nitrogen-fixing pulses).\n  - Balanced use of chemical nutrients only when needed, supplemented by bio-fertilizers `(जैव उर्वरक / જૈવિક ખાતરો)`.\n  - Water harvesting, drip irrigation, and soil moisture conservation `(नमी संरक्षण / ભેજ સંરક્ષણ)`.\n  - Integrated Pest Management (IPM) using biological predator insects.\n\n### 3. Mixed Farming `(मिश्रित कृषि / મિશ્ર ખેતી)`\n- **Concept:** Cultivating crops simultaneously alongside allied agricultural activities `(संबद्ध कृषि गतिविधियाँ / સહાયક કૃષિ પ્રવૃત્તિઓ)` on the same farm.\n- **Allied Activities Include:**\n  - Cattle rearing & Dairy farming `(पशुपालन एवं डेयरी उद्योग / પશુપાલન અને ડેરી ઉદ્યોગ)`\n  - Poultry farming `(मुर्गी पालन / મરઘાં પાલન)`\n  - Sericulture / Silk farming `(रेशम कीट पालन / રેશમ કીડા ઉછેર)`\n  - Apiculture / Beekeeping `(मधुमक्खी पालन / મધમાખી પાલન)`\n  - Pisciculture / Fish farming `(मत्स्य पालन / મત્સ્ય પાલન)`\n- **Advantage:** Provides year-round supplementary income `(पूरक आय / પૂરક આવક)` to farmers and reduces risks associated with crop failure.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "teacher_tip",
        "title": "Why Vermicompost is Earth's Black Gold",
        "content": "🌱 **Teacher's Secret:** Earthworms (`अळसिया / केंचुआ`) digest organic farm waste and convert it into vermicompost rich in nitrogen, phosphorus, and potassium. In organic farming, earthworms loosen the soil and aerate the root zones, acting as the 'Farmer's Best Friend'!",
        "body": "🌱 **Teacher's Secret:** Earthworms (`अळसिया / केंचुआ`) digest organic farm waste and convert it into vermicompost rich in nitrogen, phosphorus, and potassium. In organic farming, earthworms loosen the soil and aerate the root zones, acting as the 'Farmer's Best Friend'!"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "question": "Which of the following natural materials are used for insect and disease protection in Organic Farming?",
        "options": [
            "Urea and Diammonium Phosphate (DAP)",
            "DDT and Endosulfan spray",
            "Neem extract, sour buttermilk, and cow urine",
            "Synthetic chemical hormones"
        ],
        "correct_index": 2,
        "correct_answer": "Neem extract, sour buttermilk, and cow urine",
        "explanation": "Organic farming strictly avoids synthetic pesticides and uses natural plant protection solutions like Neem extract (Arka), sour buttermilk (Chhash), and cow urine (Gaumutra).",
        "feedback_correct": "Excellent! Organic farming relies on natural bio-pesticides like Neem water, buttermilk, and gaumutra.",
        "feedback_incorrect": "Incorrect. Organic farming avoids chemicals like Urea or DDT, using neem extract, buttermilk, and cow urine instead.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    # ==========================================
    # MODULE 4: AGRICULTURAL CROPPING SEASONS
    # ==========================================
    blocks.append({
        "type": "diagram",
        "title": "India's Three Cropping Seasons",
        "content": "India's agricultural calendar is divided into three distinct seasons: Kharif (Monsoon), Rabi (Winter), and Zaid (Summer).",
        "body": "India's agricultural calendar is divided into three distinct seasons: Kharif (Monsoon), Rabi (Winter), and Zaid (Summer).",
        "image_url": "assets/images/ss_ch10_cropping_seasons.jpg",
        "alt_text": "Infographic showing Kharif, Rabi, and Zaid seasons with sowing, harvesting months and crop examples."
    })
    
    blocks.append({
        "type": "theory",
        "title": "Agricultural Seasons of India (ભારતની કૃષિ ઋતુઓ / भारत की कृषि ऋतुएँ)",
        "content": "India enjoys three well-defined agricultural cropping seasons:\n\n| Feature | Kharif Crops `(खरीफ फसल / ખરીફ પાક)` | Rabi Crops `(रबी फसल / રવિ પાક)` | Zaid Crops `(जायद फसल / જાયદ પાક)` |\n| :--- | :--- | :--- | :--- |\n| **Season** | Monsoon season `(मानसून / ચોમાસું)` | Winter season `(शीतकाल / શિયાળો)` | Summer season `(ग्रीष्मकाल / ઉનાળો)` |\n| **Sowing Time** | June – July `(जून - जुलाई / જૂન - જુલાઈ)` | October – November `(अक्टूबर - नवंबर / ઓક્ટોબર - નવેમ્બર)` | March – April `(मार्च - अप्रैल / માર્ચ - એપ્રિલ)` |\n| **Harvesting Time** | October – November `(अक्टूबर - नवंबर / ઓક્ટોબર - નવેમ્બર)` | March – April `(मार्च - अप्रैल / માર્ચ - એપ્રિલ)` | May – June `(मई - जून / મે - જૂન)` |\n| **Major Crops** | Paddy `(धान / ડાંગર)`, Jowar `(ज्वार / જુવાર)`, Bajra `(बाजरा / બાજરી)`, Maize `(मक्का / મકાઈ)`, Cotton `(कपास / કપાસ)`, Groundnut `(मूंगफली / મગફળી)`, Sesame `(तिल / તલ)`, Soybean `(सोयाबीन / સોયાબીન)`, Moong `(मूँग / મગ)`, Math `(मठ)` | Wheat `(गेहूँ / ઘઉં)`, Gram `(चना / ચણા)`, Mustard `(सरसों / સરસવ કે રાઈ)`, Barley `(जौ / જવ)`, Linseed `(अलसी / અળસી)`, Peas `(मटर / વટાણા)` | Watermelon `(तरबूज / તરબૂચ)`, Muskmelon `(खरबूजा / શક્કરટેટી)`, Cucumber `(खीरा / કાકડી)`, Bottle Gourd `(लौकी / દૂધી)`, Summer vegetables |\n| **Climate Need** | Warm, humid, rainy climate | Cool, dry climate with bright sunshine | Warm, dry climate with irrigation |",
        "body": "India enjoys three well-defined agricultural cropping seasons:\n\n| Feature | Kharif Crops `(खरीफ फसल / ખરીફ પાક)` | Rabi Crops `(रबी फसल / રવિ પાક)` | Zaid Crops `(जायद फसल / જાયદ પાક)` |\n| :--- | :--- | :--- | :--- |\n| **Season** | Monsoon season `(मानसून / ચોમાસું)` | Winter season `(शीतकाल / શિયાળો)` | Summer season `(ग्रीष्मकाल / ઉનાળો)` |\n| **Sowing Time** | June – July `(जून - जुलाई / જૂન - જુલાઈ)` | October – November `(अक्टूबर - नवंबर / ઓક્ટોબર - નવેમ્બર)` | March – April `(मार्च - अप्रैल / માર્ચ - એપ્રિલ)` |\n| **Harvesting Time** | October – November `(अक्टूबर - नवंबर / ઓક્ટોબર - નવેમ્બર)` | March – April `(मार्च - अप्रैल / માર્ચ - એપ્રિલ)` | May – June `(मई - जून / મે - જૂન)` |\n| **Major Crops** | Paddy `(धान / ડાંગર)`, Jowar `(ज्वार / જુવાર)`, Bajra `(बाजरा / બાજરી)`, Maize `(मक्का / મકાઈ)`, Cotton `(कपास / કપાસ)`, Groundnut `(मूंगफली / મગફળી)`, Sesame `(तिल / તલ)`, Soybean `(सोयाबीन / સોયાબીન)`, Moong `(मूँग / મગ)`, Math `(मठ)` | Wheat `(गेहूँ / ઘઉં)`, Gram `(चना / ચણા)`, Mustard `(सरसों / સરસવ કે રાઈ)`, Barley `(जौ / જવ)`, Linseed `(अलसी / અળસી)`, Peas `(मटर / વટાણા)` | Watermelon `(तरबूज / તરબૂચ)`, Muskmelon `(खरबूजा / શક્કરટેટી)`, Cucumber `(खीरा / કાકડી)`, Bottle Gourd `(लौकी / દૂધી)`, Summer vegetables |\n| **Climate Need** | Warm, humid, rainy climate | Cool, dry climate with bright sunshine | Warm, dry climate with irrigation |",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "teacher_tip",
        "title": "Mnemonic to Master Sowing & Harvesting",
        "content": "🧠 **Board Exam Memory Trick:**\n- **Kharif:** Starts with Monsoon clouds (**K**aale Badal) in **June/July**, harvested before Diwali (**Oct/Nov**).\n- **Rabi:** Sown during Winter **R**efreshing chills (**Oct/Nov**), harvested at Holi time in Spring (**March/April**).\n- **Zaid:** Sown in burning **Z**ummer heat (**March/April**), harvested before monsoon (**May/June**).",
        "body": "🧠 **Board Exam Memory Trick:**\n- **Kharif:** Starts with Monsoon clouds (**K**aale Badal) in **June/July**, harvested before Diwali (**Oct/Nov**).\n- **Rabi:** Sown during Winter **R**efreshing chills (**Oct/Nov**), harvested at Holi time in Spring (**March/April**).\n- **Zaid:** Sown in burning **Z**ummer heat (**March/April**), harvested before monsoon (**May/June**)."
    })
    
    blocks.append({
        "type": "knowledge_check",
        "question": "Which of the following pairs correctly matches the crop with its agricultural season?",
        "options": [
            "Wheat : Kharif crop",
            "Paddy (Rice) : Rabi crop",
            "Watermelon : Zaid crop",
            "Mustard : Zaid crop"
        ],
        "correct_index": 2,
        "correct_answer": "Watermelon : Zaid crop",
        "explanation": "Watermelon is a classic summer (Zaid) crop grown between March and June. Wheat and Mustard are Rabi (winter) crops, while Paddy is a Kharif (monsoon) crop.",
        "feedback_correct": "Correct! Watermelon, cucumber, and muskmelon are Zaid summer crops.",
        "feedback_incorrect": "Incorrect. Watermelon is grown during summer (Zaid). Wheat is Rabi, and Paddy is Kharif.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    # ==========================================
    # MODULE 5: MAJOR FOOD GRAINS OF INDIA
    # ==========================================
    blocks.append({
        "type": "theory",
        "title": "Major Food Grains: Paddy & Wheat (ધાન્ય પાકો / प्रमुख खाद्यान्न)",
        "content": "Food grains occupy about **75%** of India's total cultivated area and contribute **50%** of total agricultural production.\n\n### 1. Paddy / Rice `(धान / चावल / ડાંગર / ચોખા)`\n- **Status:** Most important crop of India; staple food for more than **50%** of the Indian population.\n- **Global Rank:** India ranks **2nd in the world** in rice production after China. Rice occupies 1/4th of India's total cropped area.\n- **Geographical Conditions:**\n  - **Climate:** Tropical hot and humid `(उष्ण एवं आर्द्र / ઉષ્ણ અને ભેજવાળી)`. Requires temperature above **20°C to 25°C**.\n  - **Rainfall:** High rainfall of **100 cm or more**. In areas with less rain (Punjab, Haryana, Western UP), it is grown successfully using canal and tubewell irrigation.\n  - **Soil:** Fertile alluvial clayey soil `(कांपयुक्त चिकनी मिट्टी / કાંપવાળી ચીકણી ગોરાડુ જમીન)` that can retain standing water.\n- **Leading Producing States:** **West Bengal `(पश्चिम बंगाल / પશ્ચિમ બંગાળ)`** is the leading producer, followed by Uttar Pradesh, Andhra Pradesh, Punjab, Tamil Nadu, Bihar, and Odisha.\n- **Leading Districts in Gujarat:** Kheda, Vadodara, Ahmedabad, Surat, Valsad.\n\n---\n\n### 2. Wheat `(गेहूँ / ઘઉં)`\n- **Status:** Second most important food crop of India; crowned as the **\"King of Food Grains\" `(अनाजों का राजा / અનાજનો રાજા)`**.\n- **Geographical Conditions:**\n  - **Climate:** Temperate climate `(समशीतोष्ण जलवायु / સમશીતોષ્ણ આબોહવા)`. Requires cool weather during growth and bright, warm sunshine during ripening.\n  - **Rainfall:** **75 cm** annual rainfall. (Excess rainfall or waterlogging is harmful).\n  - **Soil:** Black or fertile loamy soil `(काली अथवा उपजाऊ दोमट मिट्टी / કાળી અથવા ફળદ્રુપ ગોરાડુ જમીન)`.\n  - **Threat:** Frost and heavy fog `(पाला और कोहरा / હિમ અને ઝાકળ)` cause serious damage to the wheat crop.\n- **\"Wheat Bowl of India\" `(भारत का गेहूँ का कटोरा / ઘઉંનો કોઠાર)`:** **Punjab** is called the Wheat Bowl of India because per-hectare yield is highest due to extensive canal irrigation networks (Bhakra Nangal) and modern Green Revolution practices.\n- **Leading Producing States:** Uttar Pradesh (highest total production and area), Punjab (highest per-hectare yield), Haryana, Madhya Pradesh, Rajasthan, Gujarat.\n- **Gujarat Special:** The **Bhal region `(ભાલ પ્રદેશ)`** of Gujarat is famous for its nutritious, naturally sweet **Bhalia Wheat `(ભાલિયા ઘઉં)`** (Daudkhani wheat), rich in protein.",
        "body": "Food grains occupy about **75%** of India's total cultivated area and contribute **50%** of total agricultural production.\n\n### 1. Paddy / Rice `(धान / चावल / ડાંગર / ચોખા)`\n- **Status:** Most important crop of India; staple food for more than **50%** of the Indian population.\n- **Global Rank:** India ranks **2nd in the world** in rice production after China. Rice occupies 1/4th of India's total cropped area.\n- **Geographical Conditions:**\n  - **Climate:** Tropical hot and humid `(उष्ण एवं आर्द्र / ઉષ્ણ અને ભેજવાળી)`. Requires temperature above **20°C to 25°C**.\n  - **Rainfall:** High rainfall of **100 cm or more**. In areas with less rain (Punjab, Haryana, Western UP), it is grown successfully using canal and tubewell irrigation.\n  - **Soil:** Fertile alluvial clayey soil `(कांपयुक्त चिकनी मिट्टी / કાંપવાળી ચીકણી ગોરાડુ જમીન)` that can retain standing water.\n- **Leading Producing States:** **West Bengal `(पश्चिम बंगाल / પશ્ચિમ બંગાળ)`** is the leading producer, followed by Uttar Pradesh, Andhra Pradesh, Punjab, Tamil Nadu, Bihar, and Odisha.\n- **Leading Districts in Gujarat:** Kheda, Vadodara, Ahmedabad, Surat, Valsad.\n\n---\n\n### 2. Wheat `(गेहूँ / ઘઉં)`\n- **Status:** Second most important food crop of India; crowned as the **\"King of Food Grains\" `(अनाजों का राजा / અનાજનો રાજા)`**.\n- **Geographical Conditions:**\n  - **Climate:** Temperate climate `(समशीतोष्ण जलवायु / સમશીતોષ્ણ આબોહવા)`. Requires cool weather during growth and bright, warm sunshine during ripening.\n  - **Rainfall:** **75 cm** annual rainfall. (Excess rainfall or waterlogging is harmful).\n  - **Soil:** Black or fertile loamy soil `(काली अथवा उपजाऊ दोमट मिट्टी / કાળી અથવા ફળદ્રુપ ગોરાડુ જમીન)`.\n  - **Threat:** Frost and heavy fog `(पाला और कोहरा / હિમ અને ઝાકળ)` cause serious damage to the wheat crop.\n- **\"Wheat Bowl of India\" `(भारत का गेहूँ का कटोरा / ઘઉંનો કોઠાર)`:** **Punjab** is called the Wheat Bowl of India because per-hectare yield is highest due to extensive canal irrigation networks (Bhakra Nangal) and modern Green Revolution practices.\n- **Leading Producing States:** Uttar Pradesh (highest total production and area), Punjab (highest per-hectare yield), Haryana, Madhya Pradesh, Rajasthan, Gujarat.\n- **Gujarat Special:** The **Bhal region `(ભાલ પ્રદેશ)`** of Gujarat is famous for its nutritious, naturally sweet **Bhalia Wheat `(ભાલિયા ઘઉં)`** (Daudkhani wheat), rich in protein.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "title": "Coarse Grains / Millets (બરછટ અનાજ / मोटे अनाज / श्री अन्न)",
        "content": "Millets are drought-resistant, highly nutritious coarse grains rich in minerals, vitamins, and roughage:\n\n### 1. Jowar `(ज्वार / જુવાર)`\n- **Rank:** Third most important food grain in India after Paddy and Wheat.\n- **Nature:** Grown as both Kharif and Rabi crop. Thrives in dry areas with temperatures of 25°–30°C and 50 cm rain.\n- **Leading States:** **Maharashtra `(महाराष्ट्र)`** is the leading producer in India, followed by Karnataka, Madhya Pradesh, and Andhra Pradesh. In Gujarat: Surat and Tapi districts.\n\n### 2. Bajra `(बाजरा / બાજરી)`\n- **Status:** Considered the staple food of the labor class and dry regions; high caloric and iron content.\n- **Conditions:** Sandy and shallow loamy soils `(रेतीली व हल्की दोमट मिट्टी / રેતાળ અને ગોરાડુ જમીન)`; 25°–30°C temperature; 40–50 cm rain.\n- **Leading States:** **Rajasthan `(राजस्थान)`** is the #1 producer in India, followed by Gujarat, Uttar Pradesh, and Haryana.\n- **In Gujarat:** **Banaskantha `(બનાસકાંઠા)`** district is the leading producer of Bajra in Gujarat.\n\n### 3. Maize `(मक्का / મકાઈ)`\n- **Nature:** Kharif crop; rich in starch, oil, protein, and glucose.\n- **Uses:** Human food and industrial animal feed (for poultry and livestock), and corn oil extraction.\n- **Leading States:** Karnataka, Rajasthan, Uttar Pradesh, Bihar, Andhra Pradesh, Madhya Pradesh.\n- **In Gujarat:** Widely cultivated in tribal hilly districts: **Panchmahal, Dahod, Sabarkantha, and Aravalli**.",
        "body": "Millets are drought-resistant, highly nutritious coarse grains rich in minerals, vitamins, and roughage:\n\n### 1. Jowar `(ज्वार / જુવાર)`\n- **Rank:** Third most important food grain in India after Paddy and Wheat.\n- **Nature:** Grown as both Kharif and Rabi crop. Thrives in dry areas with temperatures of 25°–30°C and 50 cm rain.\n- **Leading States:** **Maharashtra `(महाराष्ट्र)`** is the leading producer in India, followed by Karnataka, Madhya Pradesh, and Andhra Pradesh. In Gujarat: Surat and Tapi districts.\n\n### 2. Bajra `(बाजरा / બાજરી)`\n- **Status:** Considered the staple food of the labor class and dry regions; high caloric and iron content.\n- **Conditions:** Sandy and shallow loamy soils `(रेतीली व हल्की दोमट मिट्टी / રેતાળ અને ગોરાડુ જમીન)`; 25°–30°C temperature; 40–50 cm rain.\n- **Leading States:** **Rajasthan `(राजस्थान)`** is the #1 producer in India, followed by Gujarat, Uttar Pradesh, and Haryana.\n- **In Gujarat:** **Banaskantha `(બનાસકાંઠા)`** district is the leading producer of Bajra in Gujarat.\n\n### 3. Maize `(मक्का / મકાઈ)`\n- **Nature:** Kharif crop; rich in starch, oil, protein, and glucose.\n- **Uses:** Human food and industrial animal feed (for poultry and livestock), and corn oil extraction.\n- **Leading States:** Karnataka, Rajasthan, Uttar Pradesh, Bihar, Andhra Pradesh, Madhya Pradesh.\n- **In Gujarat:** Widely cultivated in tribal hilly districts: **Panchmahal, Dahod, Sabarkantha, and Aravalli**.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "question": "Which state is known as the 'Wheat Bowl of India' and why?",
        "options": [
            "Uttar Pradesh, because it has the largest land area under cultivation",
            "Punjab, because of high per-hectare yield enabled by canal irrigation",
            "West Bengal, because of highest rainfall",
            "Rajasthan, because of drought-tolerant wheat"
        ],
        "correct_index": 1,
        "correct_answer": "Punjab, because of high per-hectare yield enabled by canal irrigation",
        "explanation": "Punjab is called the 'Wheat Bowl of India' because its per-hectare yield of wheat is the highest in the country, thanks to extensive canal irrigation from the Bhakra Nangal project and Green Revolution technologies.",
        "feedback_correct": "Spot on! Punjab is called the Wheat Bowl of India due to its unmatched per-hectare yield.",
        "feedback_incorrect": "Incorrect. Punjab is called the 'Wheat Bowl of India' due to its highest per-hectare wheat productivity.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    # ==========================================
    # MODULE 6: PULSES & OILSEEDS OF INDIA
    # ==========================================
    blocks.append({
        "type": "theory",
        "title": "Pulses: The Protein Powerhouse (કઠોળ / दलहन)",
        "content": "Pulses are the primary source of protein `(प्रोटीन का मुख्य स्रोत / પ્રોટીનનો મુખ્ય સ્રોત)` for the predominantly vegetarian Indian population.\n\n### Major Varieties\n- **Kharif Pulses:** Tur / Pigeon Pea `(अरहर / तुवेर / તુવેર)`, Moong `(मूँग / મગ)`, Urad `(उड़द / અડદ)`, Math `(मठ)`.\n- **Rabi Pulses:** Gram `(चना / ચણા)`, Peas `(मटर / વટાણા)`, Masoor / Lentil `(मसूर / મસૂર)`.\n\n### Ecological Superpower: Nitrogen Fixation `(नाइट्रोजन स्थिरीकरण / નાઇટ્રોજનનું સ્થાપન)`\n- Leguminous pulse plants have root nodules `(मूल ग्रंथियां / મૂળગંડિકાઓ)` harboring *Rhizobium* bacteria.\n- These bacteria capture atmospheric nitrogen and fix it directly into the soil, naturally restoring soil fertility `(मिट्टी की उर्वरता की पुनर्स्थापना / જમીનની ફળદ્રુપતા પુનઃ સ્થાપિત કરવી)`.\n- Therefore, pulses are grown as rotational crops `(फसल चक्र / પાકની ફેરબદલી)` with soil-exhausting cereal crops like wheat and paddy.\n\n### Leading Producing Regions\n- **India:** Madhya Pradesh (#1 pulse producer), Rajasthan, Maharashtra, Uttar Pradesh, Karnataka.\n- **Gujarat:**\n  - **Vadodara `(વડોદરા)`** district is famous for **Tur (Tuver dal)**.\n  - **Banaskantha `(બનાસકાંઠા)`** district leads in **Urad**.\n  - **Kutch `(કચ્છ)`** district leads in **Moong and Math**.",
        "body": "Pulses are the primary source of protein `(प्रोटीन का मुख्य स्रोत / પ્રોટીનનો મુખ્ય સ્રોત)` for the predominantly vegetarian Indian population.\n\n### Major Varieties\n- **Kharif Pulses:** Tur / Pigeon Pea `(अरहर / तुवेर / તુવેર)`, Moong `(मूँग / મગ)`, Urad `(उड़द / અડદ)`, Math `(मठ)`.\n- **Rabi Pulses:** Gram `(चना / ચણા)`, Peas `(मटर / વટાણા)`, Masoor / Lentil `(मसूर / મસૂર)`.\n\n### Ecological Superpower: Nitrogen Fixation `(नाइट्रोजन स्थिरीकरण / નાઇટ્રોજનનું સ્થાપન)`\n- Leguminous pulse plants have root nodules `(मूल ग्रंथियां / મૂળગંડિકાઓ)` harboring *Rhizobium* bacteria.\n- These bacteria capture atmospheric nitrogen and fix it directly into the soil, naturally restoring soil fertility `(मिट्टी की उर्वरता की पुनर्स्थापना / જમીનની ફળદ્રુપતા પુનઃ સ્થાપિત કરવી)`.\n- Therefore, pulses are grown as rotational crops `(फसल चक्र / પાકની ફેરબદલી)` with soil-exhausting cereal crops like wheat and paddy.\n\n### Leading Producing Regions\n- **India:** Madhya Pradesh (#1 pulse producer), Rajasthan, Maharashtra, Uttar Pradesh, Karnataka.\n- **Gujarat:**\n  - **Vadodara `(વડોદરા)`** district is famous for **Tur (Tuver dal)**.\n  - **Banaskantha `(બનાસકાંઠા)`** district leads in **Urad**.\n  - **Kutch `(કચ્છ)`** district leads in **Moong and Math**.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "title": "Oilseeds of India: Gujarat's Golden Supremacy (તેલીબિયાં / तिलहन)",
        "content": "Oilseeds are cultivated to extract edible oils for cooking and non-edible oils for industrial lubricants, soaps, and paints:\n\n### 1. Groundnut `(मूंगफली / મગફળી)`\n- **Status:** Most important oilseed of India, accounting for the largest share of edible oil production.\n- **Conditions:** Black lava soil, sandy loam, 20°–25°C temperature, 50–70 cm rain. Kharif crop (and grown as summer crop under irrigation).\n- **Global Rank:** India is the **2nd largest producer in the world** after China.\n- **Gujarat is #1 in India:** **Gujarat produces the largest quantity of groundnut in India!**\n- **Key Gujarat Districts:** Junagadh, Gir Somnath, Amreli, Rajkot, Bhavnagar. Groundnut oil (*Singtel / સીંગતેલ*) is Gujarat's primary cooking medium.\n\n### 2. Sesame / Til `(तिल / તલ)`\n- **Specialty:** Contains the **highest oil content** among all oilseeds.\n- **Global Prestige:** India is the **world's largest exporter of sesame**!\n- **Leading States:** **Gujarat ranks #1 in India** in sesame production (Banaskantha leads in Gujarat), followed by West Bengal, Rajasthan, and MP.\n\n### 3. Mustard / Rapeseed `(सरसों / राई / સરસવ / રાઈ)`\n- **Nature:** Major Rabi oilseed crop of Northern India.\n- **Uses:** Cooking oil (Sarson ka tel), pickling, and Ayurvedic medicines.\n- **Leading States:** Rajasthan (#1 producer), Madhya Pradesh, Haryana, UP, West Bengal. In Gujarat: Patan and Banaskantha.\n\n### 4. Castor / Diveli `(अरंडी / દિવેલા / એરંડા)`\n- **Industrial Value:** Non-edible industrial oil used in aviation lubricants, high-grade cosmetics, medicines, and plastics.\n- **India's Global Monopoly:** India produces **64% of the entire world's castor output**!\n- **Gujarat's National Monopoly:** **Gujarat produces about 80% of India's total castor crop!**\n- **Key Districts in Gujarat:** Banaskantha, Sabarkantha, Junagadh, Mehsana, Patan.\n\n### 5. Soybean `(सोयाबीन / સોયાબીન)` & Others\n- Rich in plant protein (40%) and oil (20%). Madhya Pradesh and Maharashtra produce the vast majority.",
        "body": "Oilseeds are cultivated to extract edible oils for cooking and non-edible oils for industrial lubricants, soaps, and paints:\n\n### 1. Groundnut `(मूंगफली / મગફળી)`\n- **Status:** Most important oilseed of India, accounting for the largest share of edible oil production.\n- **Conditions:** Black lava soil, sandy loam, 20°–25°C temperature, 50–70 cm rain. Kharif crop (and grown as summer crop under irrigation).\n- **Global Rank:** India is the **2nd largest producer in the world** after China.\n- **Gujarat is #1 in India:** **Gujarat produces the largest quantity of groundnut in India!**\n- **Key Gujarat Districts:** Junagadh, Gir Somnath, Amreli, Rajkot, Bhavnagar. Groundnut oil (*Singtel / સીંગતેલ*) is Gujarat's primary cooking medium.\n\n### 2. Sesame / Til `(तिल / તલ)`\n- **Specialty:** Contains the **highest oil content** among all oilseeds.\n- **Global Prestige:** India is the **world's largest exporter of sesame**!\n- **Leading States:** **Gujarat ranks #1 in India** in sesame production (Banaskantha leads in Gujarat), followed by West Bengal, Rajasthan, and MP.\n\n### 3. Mustard / Rapeseed `(सरसों / राई / સરસવ / રાઈ)`\n- **Nature:** Major Rabi oilseed crop of Northern India.\n- **Uses:** Cooking oil (Sarson ka tel), pickling, and Ayurvedic medicines.\n- **Leading States:** Rajasthan (#1 producer), Madhya Pradesh, Haryana, UP, West Bengal. In Gujarat: Patan and Banaskantha.\n\n### 4. Castor / Diveli `(अरंडी / દિવેલા / એરંડા)`\n- **Industrial Value:** Non-edible industrial oil used in aviation lubricants, high-grade cosmetics, medicines, and plastics.\n- **India's Global Monopoly:** India produces **64% of the entire world's castor output**!\n- **Gujarat's National Monopoly:** **Gujarat produces about 80% of India's total castor crop!**\n- **Key Districts in Gujarat:** Banaskantha, Sabarkantha, Junagadh, Mehsana, Patan.\n\n### 5. Soybean `(सोयाबीन / સોયાબીન)` & Others\n- Rich in plant protein (40%) and oil (20%). Madhya Pradesh and Maharashtra produce the vast majority.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "teacher_tip",
        "title": "Gujarat's Triple #1 Rank in Oilseeds",
        "content": "🏆 **Teacher's Golden Fact for GSEB Exams:**\nGujarat holds the **#1 Rank in India** for:\n1. **Groundnut `(મગફળી)`** (Dominates Saurashtra: Junagadh, Gir Somnath, Amreli, Rajkot)\n2. **Castor / Diveli `(દિવેલા)`** (~80% of India's total production!)\n3. **Sesame / Til `(તલ)`** (Highest oil percentage and global export leader!)",
        "body": "🏆 **Teacher's Golden Fact for GSEB Exams:**\nGujarat holds the **#1 Rank in India** for:\n1. **Groundnut `(મગફળી)`** (Dominates Saurashtra: Junagadh, Gir Somnath, Amreli, Rajkot)\n2. **Castor / Diveli `(દિવેલા)`** (~80% of India's total production!)\n3. **Sesame / Til `(તલ)`** (Highest oil percentage and global export leader!)"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "question": "What percentage of India's total castor (Diveli) production comes from Gujarat?",
        "options": [
            "About 25%",
            "About 50%",
            "About 80%",
            "About 99%"
        ],
        "correct_index": 2,
        "correct_answer": "About 80%",
        "explanation": "Gujarat produces approximately 80% of India's total castor (Diveli / Eranda) output, making it the undisputed castor capital of the world.",
        "feedback_correct": "Correct! Gujarat produces ~80% of India's total castor crop.",
        "feedback_incorrect": "Incorrect. Gujarat produces roughly 80% of all castor in India.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    # ==========================================
    # MODULE 7: BEVERAGE CROPS & PLANTATION CROPS
    # ==========================================
    blocks.append({
        "type": "diagram",
        "title": "Plantation Agriculture: Tea & Coffee",
        "content": "Tea requires well-drained sloppy mountain soil with frequent light showers, while coffee is grown strictly under canopy shade to shield it from harsh direct sunlight.",
        "body": "Tea requires well-drained sloppy mountain soil with frequent light showers, while coffee is grown strictly under canopy shade to shield it from harsh direct sunlight.",
        "image_url": "assets/images/ss_ch10_tea_coffee_plantations.jpg",
        "alt_text": "Tea gardens in Assam/Darjeeling showing tea pluckers and shaded coffee plantations in Coorg, Karnataka."
    })
    
    blocks.append({
        "type": "theory",
        "title": "Beverage Crops: Tea, Coffee & Cocoa (પીણાં / पेय फसलें)",
        "content": "### 1. Tea `(चाय / ચા)`\n- **Nature:** Perennial bush; tropical and subtropical plantation crop. Tender green leaves and buds are plucked, processed, and fermented.\n- **Geographical Conditions:**\n  - **Terrain:** Gentle mountain slopes `(पहाड़ी ढलान / પહાડી ઢોળાવ)` with excellent drainage. **Water stagnation near roots destroys the tea plant!**\n  - **Soil:** Deep, fertile, acidic soil rich in iron and humus.\n  - **Climate:** Warm and humid climate throughout the year; temperature **20°C to 30°C**.\n  - **Rainfall:** Heavy rainfall of **200 cm or more**, distributed evenly throughout the year as frequent light showers `(फव्वारे / ઝરમર વરસાદ)` for the continuous sprouting of tender leaves.\n  - **Labor:** Highly labor-intensive; requires skilled and patient workforce to pluck tender two leaves and a bud `(दो पत्तियां और एक कली / બે પાંદડાં અને એક કૂંપળ)`.\n- **Leading States:** **Assam `(असम)`** (#1 in India, producing >50% of total tea), **West Bengal `(पश्चिम बंगाल)`** (Darjeeling tea is world-famous for its unique muscatel flavor), Tamil Nadu (Nilgiri hills), Kerala.\n\n---\n\n### 2. Coffee `(कॉफ़ी / કોફી)`\n- **Nature:** Shade-loving mountain plantation shrub `(छायादार वृक्ष / છાંયડામાં ઊગતો છોડ)`. Coffee trees are planted under large canopy shade trees because direct scorching sunlight damages coffee berries.\n- **Geographical Conditions:**\n  - **Climate:** Temperature **15°C to 28°C**; Rainfall **150 to 200 cm**.\n  - **Terrain:** Mountain slopes between 1000m to 1500m altitude.\n- **Three Varieties:** Arabica `(अरेबिका)`, Robusta `(रोबस्टा)`, Liberica `(लिबेरिका)`. India's Arabica coffee is globally acclaimed.\n- **Leading Region:** **Karnataka `(कर्नाटक)`** is the leading producer (produces ~70% of India's coffee). The **Coorg / Kodagu region `(कुर्ग क्षेत्र / કુર્ગ પ્રદેશ)`** of Karnataka is world-famous for coffee, followed by Wayanad (Kerala) and Nilgiris (Tamil Nadu).\n\n---\n\n### 3. Cocoa `(कोको / કોકો)`\n- **Source:** Extracted from the fermented and dried seeds of the cocoa pod tree.\n- **Uses:** Base ingredient for chocolates, cocoa powder, butter, and confectionery.\n- **Producing States:** Kerala, Karnataka, Tamil Nadu, Andhra Pradesh.",
        "body": "### 1. Tea `(चाय / ચા)`\n- **Nature:** Perennial bush; tropical and subtropical plantation crop. Tender green leaves and buds are plucked, processed, and fermented.\n- **Geographical Conditions:**\n  - **Terrain:** Gentle mountain slopes `(पहाड़ी ढलान / પહાડી ઢોળાવ)` with excellent drainage. **Water stagnation near roots destroys the tea plant!**\n  - **Soil:** Deep, fertile, acidic soil rich in iron and humus.\n  - **Climate:** Warm and humid climate throughout the year; temperature **20°C to 30°C**.\n  - **Rainfall:** Heavy rainfall of **200 cm or more**, distributed evenly throughout the year as frequent light showers `(फव्वारे / ઝરમર વરસાદ)` for the continuous sprouting of tender leaves.\n  - **Labor:** Highly labor-intensive; requires skilled and patient workforce to pluck tender two leaves and a bud `(दो पत्तियां और एक कली / બે પાંદડાં અને એક કૂંપળ)`.\n- **Leading States:** **Assam `(असम)`** (#1 in India, producing >50% of total tea), **West Bengal `(पश्चिम बंगाल)`** (Darjeeling tea is world-famous for its unique muscatel flavor), Tamil Nadu (Nilgiri hills), Kerala.\n\n---\n\n### 2. Coffee `(कॉफ़ी / કોફી)`\n- **Nature:** Shade-loving mountain plantation shrub `(छायादार वृक्ष / છાંયડામાં ઊગતો છોડ)`. Coffee trees are planted under large canopy shade trees because direct scorching sunlight damages coffee berries.\n- **Geographical Conditions:**\n  - **Climate:** Temperature **15°C to 28°C**; Rainfall **150 to 200 cm**.\n  - **Terrain:** Mountain slopes between 1000m to 1500m altitude.\n- **Three Varieties:** Arabica `(अरेबिका)`, Robusta `(रोबस्टा)`, Liberica `(लिबेरिका)`. India's Arabica coffee is globally acclaimed.\n- **Leading Region:** **Karnataka `(कर्नाटक)`** is the leading producer (produces ~70% of India's coffee). The **Coorg / Kodagu region `(कुर्ग क्षेत्र / કુર્ગ પ્રદેશ)`** of Karnataka is world-famous for coffee, followed by Wayanad (Kerala) and Nilgiris (Tamil Nadu).\n\n---\n\n### 3. Cocoa `(कोको / કોકો)`\n- **Source:** Extracted from the fermented and dried seeds of the cocoa pod tree.\n- **Uses:** Base ingredient for chocolates, cocoa powder, butter, and confectionery.\n- **Producing States:** Kerala, Karnataka, Tamil Nadu, Andhra Pradesh.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "teacher_tip",
        "title": "Why Tea Thrives on Slopes",
        "content": "☕ **Critical Board Reasoning:** *Why is tea cultivated on hill slopes despite requiring heavy rainfall (200+ cm)?*\n**Answer:** Tea plants need massive moisture, but their root system is extremely sensitive. If rainwater stagnates around the roots `(पानी का जमाव / પાણી ભરાઈ રહેવું)`, root rot occurs and the entire bush dies. Mountain slopes ensure instant water drainage while keeping the soil moist!",
        "body": "☕ **Critical Board Reasoning:** *Why is tea cultivated on hill slopes despite requiring heavy rainfall (200+ cm)?*\n**Answer:** Tea plants need massive moisture, but their root system is extremely sensitive. If rainwater stagnates around the roots `(पानी का जमाव / પાણી ભરાઈ રહેવું)`, root rot occurs and the entire bush dies. Mountain slopes ensure instant water drainage while keeping the soil moist!"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "question": "Which region of India is globally famous for its shade-grown coffee plantations?",
        "options": [
            "Darjeeling (West Bengal)",
            "Coorg / Kodagu (Karnataka)",
            "Kanam (Gujarat)",
            "Bhal (Gujarat)"
        ],
        "correct_index": 1,
        "correct_answer": "Coorg / Kodagu (Karnataka)",
        "explanation": "Coorg (Kodagu) in Karnataka is India's most famous coffee-growing region, producing premium Arabica and Robusta varieties under forest shade.",
        "feedback_correct": "Spot on! Coorg in Karnataka is India's coffee capital.",
        "feedback_incorrect": "Incorrect. Coorg (Karnataka) is famous for coffee; Darjeeling is famous for tea.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    # ==========================================
    # MODULE 8: MAJOR CASH CROPS
    # ==========================================
    blocks.append({
        "type": "theory",
        "title": "Major Cash Crops (રોકડિયા પાકો / प्रमुख नकदी फसलें)",
        "content": "Cash crops are grown commercially for sale in the market and as raw materials for giant manufacturing industries:\n\n### 1. Cotton `(कपास / કપાસ)`\n- **Title:** Famously celebrated as **\"White Gold\" `(सफेद सोना / સફેદ સોનું)`**.\n- **Nature:** Kharif cash crop (takes 6 to 8 months to mature).\n- **Geographical Conditions:**\n  - **Soil:** Deep, moisture-retentive **Black Lava Soil (Regur Soil `(रेगुर मिट्टी / રેગુર જમીન)`/ Black Cotton Soil)**.\n  - **Climate:** Warm and dry climate; temperature **20°C to 35°C**; rainfall **50 to 100 cm**.\n  - **Crucial Condition:** Requires **210 frost-free days `(पाला-मुक्त दिन / હિમમુક્ત દિવસો)`** and clear bright sunshine during boll opening.\n- **Gujarat is #1 in India:** **Gujarat ranks #1 in India** in cotton production, sown area, and productivity.\n- **The Kanam Region `(कानम क्षेत्र / કાનમ પ્રદેશ)`:** The **Kanam plain of Bharuch district** in Gujarat is world-famous for producing supreme quality **long-staple cotton `(लंबे रेशे वाला कपास / લાંબા તારનો કપાસ)`**.\n- **Other Gujarat Districts:** Surendranagar, Rajkot, Vadodara, Ahmedabad, Bhavnagar, Mehsana.\n\n---\n\n### 2. Sugarcane `(गन्ना / શેરડી)`\n- **Nature:** Major cash crop; duration 10 to 12 months. Raw material for Sugar, Jaggery / Gur `(गुड़ / ગોળ)`, Khandsari, and Molasses (alcohol/ethanol).\n- **Global Rank:** India is the **2nd largest producer in the world** after Brazil, but **#1 in sugar and gur consumption**.\n- **Conditions:** Hot and humid climate; 21°–27°C temperature; 75–100 cm rainfall; fertile alluvial and black lava soil.\n- **Leading States:** **Uttar Pradesh** has the largest sown area and total sugarcane output; **Maharashtra** has higher sugar recovery rate.\n- **In Gujarat:** Widely cultivated in **South Gujarat** (Surat, Navsari, Valsad, Bharuch) and Saurashtra (Gir Somnath).\n\n---\n\n### 3. Jute `(पटसन / શણ)`\n- **Title:** Celebrated as the **\"Golden Fibre\" `(सुनहरा रेशा / સુવર્ણ તાંતણો)`**.\n- **Uses:** Gunny bags `(बोरी / કંતાન)`, ropes, carpets, packaging sacks, eco-friendly handicrafts.\n- **Conditions:** Hot and humid climate (30°–40°C), heavy rainfall (>100 cm), fertile flood plain alluvial silt soils `(जलोढ़ मिट्टी / કાંપવાળી જમીન)` that are renewed every year by river floods. Abundant fresh water is needed for retting `(सड़ाकर रेशा निकालना / શણના રેસા છૂટા પાડવાની પ્રક્રિયા)`.\n- **Leading State:** **West Bengal `(पश्चिम बंगाल)`** leads India (centered around the Hooghly river basin), followed by Bihar, Assam, and Odisha.\n\n---\n\n### 4. Tobacco `(तंबाकू / તમાકુ)`\n- **Soil Decisive Factor:** Soil is more decisive than climate for tobacco quality! Requires well-drained sandy loam soil `(रेतीली दोमट मिट्टी / રેતાળ ગોરાડુ જમીન)`, 20°C temperature, and 100 cm rain.\n- **Leading States:** Andhra Pradesh, Gujarat, Uttar Pradesh, Karnataka.\n- **The Charotar Region `(चरोतर क्षेत्र / ચરોતર પ્રદેશ)`:** In Gujarat, the fertile region between the Mahi and Shedhi rivers in **Kheda and Anand districts** is famously known as the **\"Pot of Tobacco\" / \"Golden Bowl of Tobacco\" `(तंबाकू का कटोरा / તમાકુનો ગલગોટો / તમાકુની સોનાની દાબડી)`**!\n\n---\n\n### 5. Rubber `(रबर / રબર)`\n- **Source:** Extracted from the milky sap (latex `(दूधिया रस / લેટેક્સ)`) of the *Hevea brasiliensis* tree by tapping the bark.\n- **Conditions:** Equatorial hot and humid climate; temperature >30°C; heavy rainfall >300 cm.\n- **Leading State:** **Kerala `(केरल)`** produces more than **90%** of India's total natural rubber, followed by Tamil Nadu, Karnataka, and Tripura.",
        "body": "Cash crops are grown commercially for sale in the market and as raw materials for giant manufacturing industries:\n\n### 1. Cotton `(कपास / કપાસ)`\n- **Title:** Famously celebrated as **\"White Gold\" `(सफेद सोना / સફેદ સોનું)`**.\n- **Nature:** Kharif cash crop (takes 6 to 8 months to mature).\n- **Geographical Conditions:**\n  - **Soil:** Deep, moisture-retentive **Black Lava Soil (Regur Soil `(रेगुर मिट्टी / રેગુર જમીન)`/ Black Cotton Soil)**.\n  - **Climate:** Warm and dry climate; temperature **20°C to 35°C**; rainfall **50 to 100 cm**.\n  - **Crucial Condition:** Requires **210 frost-free days `(पाला-मुक्त दिन / હિમમુક્ત દિવસો)`** and clear bright sunshine during boll opening.\n- **Gujarat is #1 in India:** **Gujarat ranks #1 in India** in cotton production, sown area, and productivity.\n- **The Kanam Region `(कानम क्षेत्र / કાનમ પ્રદેશ)`:** The **Kanam plain of Bharuch district** in Gujarat is world-famous for producing supreme quality **long-staple cotton `(लंबे रेशे वाला कपास / લાંબા તારનો કપાસ)`**.\n- **Other Gujarat Districts:** Surendranagar, Rajkot, Vadodara, Ahmedabad, Bhavnagar, Mehsana.\n\n---\n\n### 2. Sugarcane `(गन्ना / શેરડી)`\n- **Nature:** Major cash crop; duration 10 to 12 months. Raw material for Sugar, Jaggery / Gur `(गुड़ / ગોળ)`, Khandsari, and Molasses (alcohol/ethanol).\n- **Global Rank:** India is the **2nd largest producer in the world** after Brazil, but **#1 in sugar and gur consumption**.\n- **Conditions:** Hot and humid climate; 21°–27°C temperature; 75–100 cm rainfall; fertile alluvial and black lava soil.\n- **Leading States:** **Uttar Pradesh** has the largest sown area and total sugarcane output; **Maharashtra** has higher sugar recovery rate.\n- **In Gujarat:** Widely cultivated in **South Gujarat** (Surat, Navsari, Valsad, Bharuch) and Saurashtra (Gir Somnath).\n\n---\n\n### 3. Jute `(पटसन / શણ)`\n- **Title:** Celebrated as the **\"Golden Fibre\" `(सुनहरा रेशा / સુવર્ણ તાંતણો)`**.\n- **Uses:** Gunny bags `(बोरी / કંતાન)`, ropes, carpets, packaging sacks, eco-friendly handicrafts.\n- **Conditions:** Hot and humid climate (30°–40°C), heavy rainfall (>100 cm), fertile flood plain alluvial silt soils `(जलोढ़ मिट्टी / કાંપવાળી જમીન)` that are renewed every year by river floods. Abundant fresh water is needed for retting `(सड़ाकर रेशा निकालना / શણના રેસા છૂટા પાડવાની પ્રક્રિયા)`.\n- **Leading State:** **West Bengal `(पश्चिम बंगाल)`** leads India (centered around the Hooghly river basin), followed by Bihar, Assam, and Odisha.\n\n---\n\n### 4. Tobacco `(तंबाकू / તમાકુ)`\n- **Soil Decisive Factor:** Soil is more decisive than climate for tobacco quality! Requires well-drained sandy loam soil `(रेतीली दोमट मिट्टी / રેતાળ ગોરાડુ જમીન)`, 20°C temperature, and 100 cm rain.\n- **Leading States:** Andhra Pradesh, Gujarat, Uttar Pradesh, Karnataka.\n- **The Charotar Region `(चरोतर क्षेत्र / ચરોતર પ્રદેશ)`:** In Gujarat, the fertile region between the Mahi and Shedhi rivers in **Kheda and Anand districts** is famously known as the **\"Pot of Tobacco\" / \"Golden Bowl of Tobacco\" `(तंबाकू का कटोरा / તમાકુનો ગલગોટો / તમાકુની સોનાની દાબડી)`**!\n\n---\n\n### 5. Rubber `(रबर / રબર)`\n- **Source:** Extracted from the milky sap (latex `(दूधिया रस / લેટેક્સ)`) of the *Hevea brasiliensis* tree by tapping the bark.\n- **Conditions:** Equatorial hot and humid climate; temperature >30°C; heavy rainfall >300 cm.\n- **Leading State:** **Kerala `(केरल)`** produces more than **90%** of India's total natural rubber, followed by Tamil Nadu, Karnataka, and Tripura.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "teacher_tip",
        "title": "Geographical Nicknames to Memorize",
        "content": "🎯 **GSEB Board Match-the-Following Gold Mine:**\n- **White Gold `(સફેદ સોનું)`** ➔ Cotton `(કપાસ)` (Gujarat #1; Bharuch Kanam region for long-staple cotton)\n- **Golden Fibre `(સુવર્ણ તાંતણો)`** ➔ Jute `(શણ)` (West Bengal #1; Hooghly basin)\n- **Pot of Tobacco `(તમાકુનો ગલગોટો)`** ➔ Charotar region `(ચરોતર પ્રદેશ)` (Kheda & Anand)\n- **Bhalia Wheat `(ભાલિયા ઘઉં)`** ➔ Bhal region `(ભાલ પ્રદેશ)` (Ahmedabad/Bhavnagar)",
        "body": "🎯 **GSEB Board Match-the-Following Gold Mine:**\n- **White Gold `(સફેદ સોનું)`** ➔ Cotton `(કપાસ)` (Gujarat #1; Bharuch Kanam region for long-staple cotton)\n- **Golden Fibre `(સુવર્ણ તાંતણો)`** ➔ Jute `(શણ)` (West Bengal #1; Hooghly basin)\n- **Pot of Tobacco `(તમાકુનો ગલગોટો)`** ➔ Charotar region `(ચરોતર પ્રદેશ)` (Kheda & Anand)\n- **Bhalia Wheat `(ભાલિયા ઘઉં)`** ➔ Bhal region `(ભાલ પ્રદેશ)` (Ahmedabad/Bhavnagar)"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "question": "Which region of Gujarat is world-famous as the 'Pot of Tobacco' (તમાકુનો ગલગોટો)?",
        "options": [
            "Kanam region (Bharuch)",
            "Bhal region (Ahmedabad)",
            "Charotar region (Kheda and Anand)",
            "Gir region (Junagadh)"
        ],
        "correct_index": 2,
        "correct_answer": "Charotar region (Kheda and Anand)",
        "explanation": "The Charotar region of Kheda and Anand districts in Gujarat is famously called the 'Pot of Tobacco' because of its extensive and high-quality bidi and chewing tobacco production.",
        "feedback_correct": "Correct! Charotar (Kheda/Anand) is the Pot of Tobacco.",
        "feedback_incorrect": "Incorrect. Charotar in Kheda/Anand is called the Pot of Tobacco; Kanam is famous for cotton.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    # ==========================================
    # MODULE 9: SPICES, MEDICINAL & HORTICULTURE
    # ==========================================
    blocks.append({
        "type": "theory",
        "title": "Spices, Condiments, Medicinal Plants & Fruits (મસાલા, ઔષધિઓ અને બાગાયતી પાકો)",
        "content": "### 1. Spices & Condiments `(मसाला फसलें / મસાલા પાકો)`\n- **Gujarat's Global Supremacy:** Gujarat ranks **#1 in India and the world** in the production and export of:\n  - **Cumin Seeds `(जीरा / જીરું)`**\n  - **Fennel Seeds `(सौंफ / વરિયાળી)`**\n  - **Isabgol `(इसबगोल / ઈસબગુલ)`** (Psyllium husk used globally in pharmaceuticals)\n- **Other Major Spices:** Coriander `(धनिया / ધાણા)`, Fenugreek `(मेथी / મેથી)`, Mustard `(राई / રાઈ)`, Ajwain `(अजवाइन / અજમો)`, Garlic `(लहसुन / લસણ)`, Black Pepper `(काली मिर्च / મરી)`, Cardamom `(इलायची / એલચી)`, Ginger `(अदरक / આદું)`, and Turmeric `(हल्दी / હળદર)`.\n\n### 2. Medicinal Plants `(औषधीय पौधे / ઔષધીય વનસ્પતિઓ)`\n- India is the cradle of Ayurveda. Major cultivated medicinal plants include:\n  - **Isabgol, Ashwagandha, Tulsi, Ardusi, Kariyatu, Aloe Vera `(घृतकुमारी / કુવારપાઠું)`, Shatavari, Senna `(सनाय / સોનામુખી)`, and Gokhru**.\n\n### 3. Horticulture: Fruits, Vegetables & Flowers `(बागवानी / બાગાયત)`\n- **Fruits:** India ranks **2nd in the world** in fruit production after China.\n  - **Mango `(आम / કેરી)`:** **Kesar Mango `(केसर आम / કેસર કેરી)`** of Gir Talala (Junagadh/Gir Somnath) and **Alphonso / Hapus `(हापुस आम / હાફૂસ કેરી)`** of Valsad hold Geographical Indication (GI) fame.\n  - **Banana `(केला / કેળ / કેળાં)`:** Tamil Nadu, Maharashtra, Gujarat (Bharuch, Anand, Mahuva).\n  - **Apple `(सेब / સફરજન)`:** Jammu & Kashmir and Himachal Pradesh.\n  - **Grapes `(अंगूर / દ્રાક્ષ)`:** Maharashtra (Nashik - Wine Capital), Andhra Pradesh, Tamil Nadu.\n  - **Guava `(अमरूद / જામફળ)`:** Dholka (Gujarat), Allahabad (UP).\n  - **Pomegranate `(अनार / દાડમ)`:** Kutch and Bhavnagar in Gujarat.",
        "body": "### 1. Spices & Condiments `(मसाला फसलें / મસાલા પાકો)`\n- **Gujarat's Global Supremacy:** Gujarat ranks **#1 in India and the world** in the production and export of:\n  - **Cumin Seeds `(जीरा / જીરું)`**\n  - **Fennel Seeds `(सौंफ / વરિયાળી)`**\n  - **Isabgol `(इसबगोल / ઈસબગુલ)`** (Psyllium husk used globally in pharmaceuticals)\n- **Other Major Spices:** Coriander `(धनिया / ધાણા)`, Fenugreek `(मेथी / મેથી)`, Mustard `(राई / રાઈ)`, Ajwain `(अजवाइन / અજમો)`, Garlic `(लहसुन / લસણ)`, Black Pepper `(काली मिर्च / મરી)`, Cardamom `(इलायची / એલચી)`, Ginger `(अदरक / આદું)`, and Turmeric `(हल्दी / હળદર)`.\n\n### 2. Medicinal Plants `(औषधीय पौधे / ઔષધીય વનસ્પતિઓ)`\n- India is the cradle of Ayurveda. Major cultivated medicinal plants include:\n  - **Isabgol, Ashwagandha, Tulsi, Ardusi, Kariyatu, Aloe Vera `(घृतकुमारी / કુવારપાઠું)`, Shatavari, Senna `(सनाय / સોનામુખી)`, and Gokhru**.\n\n### 3. Horticulture: Fruits, Vegetables & Flowers `(बागवानी / બાગાયત)`\n- **Fruits:** India ranks **2nd in the world** in fruit production after China.\n  - **Mango `(आम / કેરી)`:** **Kesar Mango `(केसर आम / કેસર કેરી)`** of Gir Talala (Junagadh/Gir Somnath) and **Alphonso / Hapus `(हापुस आम / હાફૂસ કેરી)`** of Valsad hold Geographical Indication (GI) fame.\n  - **Banana `(કેળાં / केला)`:** Tamil Nadu, Maharashtra, Gujarat (Bharuch, Anand, Mahuva).\n  - **Apple `(सेब / સફરજન)`:** Jammu & Kashmir and Himachal Pradesh.\n  - **Grapes `(अंगूर / દ્રાક્ષ)`:** Maharashtra (Nashik - Wine Capital), Andhra Pradesh, Tamil Nadu.\n  - **Guava `(अमरूद / જામફળ)`:** Dholka (Gujarat), Allahabad (UP).\n  - **Pomegranate `(अनार / દાડમ)`:** Kutch and Bhavnagar in Gujarat.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "teacher_tip",
        "title": "North Gujarat's Isabgol Processing Hub",
        "content": "🌿 **Industry Insight:** More than 80% of the world's exported medicinal Isabgol husk is processed and packed in North Gujarat (Unjha, Mehsana, Patan). The Unjha Agricultural Produce Market Committee (APMC) is Asia's largest spice trading market!",
        "body": "🌿 **Industry Insight:** More than 80% of the world's exported medicinal Isabgol husk is processed and packed in North Gujarat (Unjha, Mehsana, Patan). The Unjha Agricultural Produce Market Committee (APMC) is Asia's largest spice trading market!"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "question": "Gujarat ranks first in India and the world in the production and export of which three spices/condiments?",
        "options": [
            "Tea, Coffee, and Cocoa",
            "Cumin seeds (Jeeru), Fennel seeds (Variyali), and Isabgol",
            "Cardamom, Black Pepper, and Clove",
            "Saffron, Apple, and Walnut"
        ],
        "correct_index": 1,
        "correct_answer": "Cumin seeds (Jeeru), Fennel seeds (Variyali), and Isabgol",
        "explanation": "Gujarat holds the #1 rank in India and globally in the cultivation and export of Cumin (Jeeru), Fennel (Variyali), and Isabgol.",
        "feedback_correct": "Correct! Gujarat is #1 in Cumin, Fennel, and Isabgol.",
        "feedback_incorrect": "Incorrect. Gujarat leads globally in Cumin (Jeeru), Fennel (Variyali), and Isabgol.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    # ==========================================
    # MODULE 10: INSTITUTIONAL & TECHNICAL REFORMS
    # ==========================================
    blocks.append({
        "type": "theory",
        "title": "Technical Reforms in Agriculture (ટેકનિકલ સુધારાઓ / तकनीकी सुधार)",
        "content": "Technical reforms refer to changes and modernizations made in farming implements, seeds, fertilizers, irrigation, and digital technologies:\n\n1. **Mechanization `(यांत्रिकीकरण / યાંત્રિકીકરણ)`:** Replacement of traditional wooden ploughs and bullocks with modern tractors, rotavators, power tillers, threshers, and combine harvesters.\n2. **High Yielding Variety (HYV) Seeds `(उन्नत बीज / સુધારેલાં બિયારણો)`:** Widespread distribution of certified hybrid and genetically improved seeds to boost yield per acre.\n3. **Modern Irrigation Systems `(आधुनिक सिंचाई प्रणालियाँ / આધુનિક સિંચાઈ પદ્ધતિઓ)`:** Massive promotion of **Drip Irrigation `(टपक सिंचाई / ટપક સિંચાઈ)`** and **Sprinkler Irrigation `(फव्वारा सिंचाई / ફુવારા પદ્ધતિ)`**, which save 40% to 60% water while preventing soil salinity.\n4. **Chemical & Bio-Fertilizers `(रासायनिक व जैविक उर्वरक / રાસાયણિક અને જૈવિક ખાતરો)`:** Subsidized distribution of balanced fertilizers (Urea, DAP, NPK) along with bio-fertilizers and micronutrients.\n5. **Plant Protection `(पादप संरक्षण / પાક સંરક્ષણ)`:** Integrated Pest Management (IPM), bio-pesticides, and safe insecticides.\n6. **Soil Health Card Scheme `(मृदा स्वास्थ्य कार्ड / જમીન સ્વાસ્થ્ય પત્રિકા)`:** Soil samples are scientifically tested in laboratories, and farmers receive a customized report advising exact nutrient deficiencies and required fertilizer dosage, preventing soil degradation.\n7. **Digital Agriculture & Guidance `(डिजिटल कृषि / ડિજિટલ માર્ગદર્શન)`:**\n   - **Kisan Call Center:** Toll-free nationwide phone number **`1800-180-1551`** providing real-time expert agronomic advice in regional languages.\n   - **Doordarshan DD Kisan Channel** and **All India Radio Kisan Vani** broadcasting daily weather forecasts, modern farming techniques, and mandi market rates.\n   - **Gujarat Government's i-Khedut Portal `(આઈ-ખેડૂત પોર્ટલ)`:** Single-window online portal where farmers register for tractor subsidies, drip kits, seeds, and financial assistance.\n8. **Agricultural Universities `(कृषि विश्वविद्यालय / કૃષિ યુનિવર્સિટીઓ)`:** Four dedicated agricultural universities in Gujarat (**Anand, Junagadh, Navsari, and Sardarkrushinagar Dantiwada**) conducting research and training under the Indian Council of Agricultural Research (ICAR).",
        "body": "Technical reforms refer to changes and modernizations made in farming implements, seeds, fertilizers, irrigation, and digital technologies:\n\n1. **Mechanization `(यांत्रिकीकरण / યાંત્રિકીકરણ)`:** Replacement of traditional wooden ploughs and bullocks with modern tractors, rotavators, power tillers, threshers, and combine harvesters.\n2. **High Yielding Variety (HYV) Seeds `(उन्नत बीज / સુધારેલાં બિયારણો)`:** Widespread distribution of certified hybrid and genetically improved seeds to boost yield per acre.\n3. **Modern Irrigation Systems `(आधुनिक सिंचाई प्रणालियाँ / આધુનિક સિંચાઈ પદ્ધતિઓ)`:** Massive promotion of **Drip Irrigation `(टपक सिंचाई / ટપક સિંચાઈ)`** and **Sprinkler Irrigation `(फव्वारा सिंचाई / ફુવારા પદ્ધતિ)`**, which save 40% to 60% water while preventing soil salinity.\n4. **Chemical & Bio-Fertilizers `(रासायनिक व जैविक उर्वरक / રાસાયણિક અને જૈવિક ખાતરો)`:** Subsidized distribution of balanced fertilizers (Urea, DAP, NPK) along with bio-fertilizers and micronutrients.\n5. **Plant Protection `(पादप संरक्षण / પાક સંરક્ષણ)`:** Integrated Pest Management (IPM), bio-pesticides, and safe insecticides.\n6. **Soil Health Card Scheme `(मृदा स्वास्थ्य कार्ड / જમીન સ્વાસ્થ્ય પત્રિકા)`:** Soil samples are scientifically tested in laboratories, and farmers receive a customized report advising exact nutrient deficiencies and required fertilizer dosage, preventing soil degradation.\n7. **Digital Agriculture & Guidance `(डिजिटल कृषि / ડિજિટલ માર્ગદર્શન)`:**\n   - **Kisan Call Center:** Toll-free nationwide phone number **`1800-180-1551`** providing real-time expert agronomic advice in regional languages.\n   - **Doordarshan DD Kisan Channel** and **All India Radio Kisan Vani** broadcasting daily weather forecasts, modern farming techniques, and mandi market rates.\n   - **Gujarat Government's i-Khedut Portal `(આઈ-ખેડૂત પોર્ટલ)`:** Single-window online portal where farmers register for tractor subsidies, drip kits, seeds, and financial assistance.\n8. **Agricultural Universities `(कृषि विश्वविद्यालय / કૃષિ યુનિવર્સિટીઓ)`:** Four dedicated agricultural universities in Gujarat (**Anand, Junagadh, Navsari, and Sardarkrushinagar Dantiwada**) conducting research and training under the Indian Council of Agricultural Research (ICAR).",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "title": "Institutional Reforms in Agriculture (સંસ્થાગત સુધારાઓ / संस्थागत सुधार)",
        "content": "Institutional reforms refer to legal, organizational, financial, and marketing changes enacted by the government to empower farmers and eliminate exploitation:\n\n### 1. Land Reforms `(भूमि सुधार / જમીન સુધારણા)`\n- **Abolition of Zamindari System `(ज़मींदारी प्रथा का उन्मूलन / જમીનદારી પ્રથાની નાબૂદી)`:** Ended landlord exploitation and made farmers direct landowners.\n- **Land to the Tiller `(जोतने वाले को भूमि / ખેડે તેની જમીન)`:** Enacted under the Land Tenancy Act `(काश्तकारी कानून / ગણોત ધારો)`, giving permanent ownership rights to actual cultivating tenants.\n- **Land Ceiling Act `(भूमि हदबंदी अधिनियम / જમીન ટોચ મર્યાદા ધારો)`:** Placed a legal ceiling on maximum agricultural land ownership to curb wealth concentration and distribute surplus land to landless laborers.\n- **Land Consolidation `(चकबंदी / જમીન એકત્રીકરણ)`:** Small, scattered land fragments of a farmer are consolidated into one single viable farm block, making mechanization feasible.\n\n### 2. Credit and Financial Support `(ऋण एवं वित्तीय सहायता / ધિરાણ અને આર્થિક સહાય)`\n- **Kisan Credit Card (KCC) `(किसान क्रेडिट कार्ड / કિસાન ક્રેડિટ કાર્ડ)`:** Provides farmers with hassle-free, low-interest crop loans from nationalized, rural, and cooperative banks.\n- **Subsidized Bank Credit:** Primary Agricultural Credit Societies (PACS), Regional Rural Banks (RRBs), District Central Cooperative Banks, and **NABARD** (National Bank for Agriculture and Rural Development).\n\n### 3. Crop Insurance: PMFBY `(फसल बीमा / પાક વીમો)`\n- **Pradhan Mantri Fasal Bima Yojana (PMFBY) `(प्रधानमंत्री फसल बीमा योजना / પ્રધાનમંત્રી ફસલ બીમા યોજના)`:** Provides comprehensive financial protection against crop damage caused by natural calamities (drought, unseasonal rain, floods, pest outbreaks).\n\n### 4. Regulated Markets & APMC `(विनियमित मंडियां / ખેતીવાડી ઉત્પન્ન બજાર સમિતિ)`\n- **Agricultural Produce Market Committees (APMC) `(खेतीबाड़ी उत्पन्न बाजार समिति / ખેતીવાડી ઉત્પન્ન બજાર સમિતિ)`:** State-regulated mandis that protect farmers from deceitful middlemen and traders through:\n  - Open public auction `(खुली नीलामी / ખુલ્લી હરાજી)`\n  - Certified electronic weighing\n  - Immediate digital payments\n  - Storage godowns and cold storages.\n\n### 5. Minimum Support Price (MSP) `(न्यूनतम समर्थन मूल्य / ટેકાના ભાવ)`\n- The government fixes and announces **MSP** before the sowing season for major crops.\n- If open market prices crash below MSP, government agencies step in to purchase the produce at the guaranteed MSP, ensuring farmers never face bankruptcy.\n- **Key Government Procurement Agencies:**\n  1. **NAFED:** National Agricultural Cooperative Marketing Federation of India\n  2. **GROFED:** Gujarat State Cooperative Oilseeds Growers' Federation\n  3. **NDDB:** National Dairy Development Board\n  4. **FCI:** Food Corporation of India",
        "body": "Institutional reforms refer to legal, organizational, financial, and marketing changes enacted by the government to empower farmers and eliminate exploitation:\n\n### 1. Land Reforms `(भूमि सुधार / જમીન સુધારણા)`\n- **Abolition of Zamindari System `(ज़मींदारी प्रथा का उन्मूलन / જમીનદારી પ્રથાની નાબૂદી)`:** Ended landlord exploitation and made farmers direct landowners.\n- **Land to the Tiller `(जोतने वाले को भूमि / ખેડે તેની જમીન)`:** Enacted under the Land Tenancy Act `(काश्तकारी कानून / ગણોત ધારો)`, giving permanent ownership rights to actual cultivating tenants.\n- **Land Ceiling Act `(भूमि हदबंदी अधिनियम / જમીન ટોચ મર્યાદા ધારો)`:** Placed a legal ceiling on maximum agricultural land ownership to curb wealth concentration and distribute surplus land to landless laborers.\n- **Land Consolidation `(चकबंदी / જમીન એકત્રીકરણ)`:** Small, scattered land fragments of a farmer are consolidated into one single viable farm block, making mechanization feasible.\n\n### 2. Credit and Financial Support `(ऋण एवं वित्तीय सहायता / ધિરાણ અને આર્થિક સહાય)`\n- **Kisan Credit Card (KCC) `(किसान क्रेडिट कार्ड / કિસાન ક્રેડિટ કાર્ડ)`:** Provides farmers with hassle-free, low-interest crop loans from nationalized, rural, and cooperative banks.\n- **Subsidized Bank Credit:** Primary Agricultural Credit Societies (PACS), Regional Rural Banks (RRBs), District Central Cooperative Banks, and **NABARD** (National Bank for Agriculture and Rural Development).\n\n### 3. Crop Insurance: PMFBY `(फसल बीमा / પાક વીમો)`\n- **Pradhan Mantri Fasal Bima Yojana (PMFBY) `(प्रधानमंत्री फसल बीमा योजना / પ્રધાનમંત્રી ફસલ બીમા યોજના)`:** Provides comprehensive financial protection against crop damage caused by natural calamities (drought, unseasonal rain, floods, pest outbreaks).\n\n### 4. Regulated Markets & APMC `(विनियमित मंडियां / ખેતીવાડી ઉત્પન્ન બજાર સમિતિ)`\n- **Agricultural Produce Market Committees (APMC) `(खेतीबाड़ी उत्पन्न बाजार समिति / ખેતીવાડી ઉત્પન્ન બજાર સમિતિ)`:** State-regulated mandis that protect farmers from deceitful middlemen and traders through:\n  - Open public auction `(खुली नीलामी / ખુલ્લી હરાજી)`\n  - Certified electronic weighing\n  - Immediate digital payments\n  - Storage godowns and cold storages.\n\n### 5. Minimum Support Price (MSP) `(न्यूनतम समर्थन मूल्य / ટેકાના ભાવ)`\n- The government fixes and announces **MSP** before the sowing season for major crops.\n- If open market prices crash below MSP, government agencies step in to purchase the produce at the guaranteed MSP, ensuring farmers never face bankruptcy.\n- **Key Government Procurement Agencies:**\n  1. **NAFED:** National Agricultural Cooperative Marketing Federation of India\n  2. **GROFED:** Gujarat State Cooperative Oilseeds Growers' Federation\n  3. **NDDB:** National Dairy Development Board\n  4. **FCI:** Food Corporation of India",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "teacher_tip",
        "title": "5/5 Board Exam Blueprint: Technical vs Institutional",
        "content": "🔥 **Board Exam Topper Strategy:**\nNever mix Technical and Institutional reforms in exam answers!\n- **Technical = Tools & Technology:** Seeds (HYV), Tractors, Drip irrigation, Fertilizers, Soil Health Card, Kisan Call Center (1800-180-1551), i-Khedut.\n- **Institutional = Laws & Institutions:** Land Tenancy Act (Land to the Tiller), Land Ceiling, KCC loans, PMFBY insurance, APMC market yard, MSP (NAFED/GROFED/FCI).",
        "body": "🔥 **Board Exam Topper Strategy:**\nNever mix Technical and Institutional reforms in exam answers!\n- **Technical = Tools & Technology:** Seeds (HYV), Tractors, Drip irrigation, Fertilizers, Soil Health Card, Kisan Call Center (1800-180-1551), i-Khedut.\n- **Institutional = Laws & Institutions:** Land Tenancy Act (Land to the Tiller), Land Ceiling, KCC loans, PMFBY insurance, APMC market yard, MSP (NAFED/GROFED/FCI)."
    })
    
    blocks.append({
        "type": "knowledge_check",
        "question": "Which of the following is categorized under 'Institutional Reforms' (સંસ્થાગત સુધારાઓ) in Indian agriculture?",
        "options": [
            "Use of Drip and Sprinkler irrigation",
            "Introduction of high-yielding hybrid seeds (HYV)",
            "Land to the Tiller Act and Kisan Credit Card (KCC)",
            "Soil Health Card laboratory testing"
        ],
        "correct_index": 2,
        "correct_answer": "Land to the Tiller Act and Kisan Credit Card (KCC)",
        "explanation": "Land reforms (Land to the Tiller / Khede Teni Jameen) and banking credit facilities (KCC, NABARD) are Institutional reforms. Seeds, drip irrigation, and soil testing are Technical reforms.",
        "feedback_correct": "Correct! Land laws and banking credit cards are Institutional reforms.",
        "feedback_incorrect": "Incorrect. Land to the Tiller and KCC are Institutional reforms; drip irrigation and seeds are Technical reforms.",
        "difficulty": "Intermediate",
        "bloom": "Analyze"
    })
    
    # ==========================================
    # MODULE 11: GREEN REVOLUTION & FOOD SECURITY
    # ==========================================
    blocks.append({
        "type": "theory",
        "title": "The Green Revolution & Food Security (હરિયાળી ક્રાંતિ અને અન્ન સુરક્ષા)",
        "content": "### 1. The Green Revolution `(हरित क्रांति / હરિયાળી ક્રાંતિ)`\n- **Genesis:** In the 1960s, India faced severe food grain shortages, frequent famines, and humiliating dependence on food imports from the USA under the **PL-480** scheme (ship-to-mouth existence).\n- **The Breakthrough:** Introduction of High Yielding Variety (HYV) semi-dwarf wheat seeds (developed by Nobel laureate **Dr. Norman Borlaug** in Mexico) and miracle rice (IR-8 from Philippines), combined with:\n  - Expanded canal and tubewell irrigation\n  - Chemical fertilizers (Urea, DAP)\n  - Effective insecticides and pesticides\n  - Farm mechanization (tractors, threshers)\n  - Guaranteed MSP procurement\n- **Father of Green Revolution in India:** **Dr. M. S. Swaminathan `(डॉ. एम. एस. स्वामीनाथन / ડૉ. એમ. એસ. સ્વામિનાથન)`**.\n- **Phenomenal Impact:**\n  - India witnessed a record-breaking multi-fold increase in food grain output, especially in **Wheat and Rice**.\n  - **Self-Reliance `(स्वावलंबन / સ્વાવલંબન)`:** India transformed from a begging bowl food-deficit nation into a completely self-sufficient food exporter with vast buffer stocks!\n  - Punjab, Haryana, and Western UP led this historic economic miracle.\n\n---\n\n### 2. Food Security & Buffer Stock `(खाद्य सुरक्षा एवं बफर स्टॉक / અન્ન સુરક્ષા અને બફર સ્ટોક)`\n- **Food Security Concept:** Ensuring every citizen of India has physical, social, and economic access to sufficient, safe, and nutritious food at all times.\n- **FCI Buffer Stock:** The Food Corporation of India (FCI) procures wheat and rice at MSP and stores millions of tonnes in scientific silos and godowns.\n- **Public Distribution System (PDS) `(सार्वजनिक वितरण प्रणाली / જાહેર વિતરણ પ્રણાલી)`:** Subsidized food grains, sugar, and kerosene are distributed to poor families via **Fair Price Shops (FPS / Ration shops `(उचित मूल्य की दुकानें / વાજબી ભાવની દુકાનો)`)** under the National Food Security Act (NFSA).\n- **Strategic Value:** Buffer stocks protect the nation during severe droughts, floods, crop failures, pandemics, and war emergencies.\n\n---\n\n### 3. Impact of Globalization on Indian Agriculture `(वैश्वीकरण का प्रभाव / વૈશ્વિકીકરણની અસરો)`\n- **Opportunities:** Global export markets opened up for Indian organic produce, basmati rice, spices, fruits, and flowers.\n- **Challenges:**\n  - Indian farmers must compete with heavily subsidized farm produce from developed nations (USA, European Union).\n  - Need for strict intellectual property protection and **Patenting `(पेटेंट / પેટન્ટ)`** of Indian traditional varieties (Neem, Basmati, Turmeric) against biopiracy.\n  - Need for cost-effective, high-tech, and sustainable production to remain globally competitive.",
        "body": "### 1. The Green Revolution `(हरित क्रांति / હરિયાળી ક્રાંતિ)`\n- **Genesis:** In the 1960s, India faced severe food grain shortages, frequent famines, and humiliating dependence on food imports from the USA under the **PL-480** scheme (ship-to-mouth existence).\n- **The Breakthrough:** Introduction of High Yielding Variety (HYV) semi-dwarf wheat seeds (developed by Nobel laureate **Dr. Norman Borlaug** in Mexico) and miracle rice (IR-8 from Philippines), combined with:\n  - Expanded canal and tubewell irrigation\n  - Chemical fertilizers (Urea, DAP)\n  - Effective insecticides and pesticides\n  - Farm mechanization (tractors, threshers)\n  - Guaranteed MSP procurement\n- **Father of Green Revolution in India:** **Dr. M. S. Swaminathan `(डॉ. एम. एस. स्वामीनाथन / ડૉ. એમ. એસ. સ્વામિનાથન)`**.\n- **Phenomenal Impact:**\n  - India witnessed a record-breaking multi-fold increase in food grain output, especially in **Wheat and Rice**.\n  - **Self-Reliance `(स्वावलंबन / સ્વાવલંબન)`:** India transformed from a begging bowl food-deficit nation into a completely self-sufficient food exporter with vast buffer stocks!\n  - Punjab, Haryana, and Western UP led this historic economic miracle.\n\n---\n\n### 2. Food Security & Buffer Stock `(खाद्य सुरक्षा एवं बफर स्टॉक / અન્ન સુરક્ષા અને બફર સ્ટોક)`\n- **Food Security Concept:** Ensuring every citizen of India has physical, social, and economic access to sufficient, safe, and nutritious food at all times.\n- **FCI Buffer Stock:** The Food Corporation of India (FCI) procures wheat and rice at MSP and stores millions of tonnes in scientific silos and godowns.\n- **Public Distribution System (PDS) `(सार्वजनिक वितरण प्रणाली / જાહેર વિતરણ પ્રણાલી)`:** Subsidized food grains, sugar, and kerosene are distributed to poor families via **Fair Price Shops (FPS / Ration shops `(उचित मूल्य की दुकानें / વાજબી ભાવની દુકાનો)`)** under the National Food Security Act (NFSA).\n- **Strategic Value:** Buffer stocks protect the nation during severe droughts, floods, crop failures, pandemics, and war emergencies.\n\n---\n\n### 3. Impact of Globalization on Indian Agriculture `(वैश्वीकरण का प्रभाव / વૈશ્વિકીકરણની અસરો)`\n- **Opportunities:** Global export markets opened up for Indian organic produce, basmati rice, spices, fruits, and flowers.\n- **Challenges:**\n  - Indian farmers must compete with heavily subsidized farm produce from developed nations (USA, European Union).\n  - Need for strict intellectual property protection and **Patenting `(पेटेंट / પેટન્ટ)`** of Indian traditional varieties (Neem, Basmati, Turmeric) against biopiracy.\n  - Need for cost-effective, high-tech, and sustainable production to remain globally competitive.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "teacher_tip",
        "title": "Dr. Swaminathan's Evergreen Revolution",
        "content": "🌾 **Academic Vision:** Dr. M. S. Swaminathan emphasized transitioning from the Green Revolution to an **'Evergreen Revolution' (સદાબહાર ક્રાંતિ)**—increasing agricultural productivity in perpetuity without causing ecological or social damage!",
        "body": "🌾 **Academic Vision:** Dr. M. S. Swaminathan emphasized transitioning from the Green Revolution to an **'Evergreen Revolution' (સદાબહાર ક્રાંતિ)**—increasing agricultural productivity in perpetuity without causing ecological or social damage!"
    })
    
    blocks.append({
        "type": "knowledge_check",
        "question": "Who is recognized as the Father of the Green Revolution in India?",
        "options": [
            "Dr. Verghese Kurien",
            "Dr. M. S. Swaminathan",
            "Dr. Homi Bhabha",
            "Dr. A. P. J. Abdul Kalam"
        ],
        "correct_index": 1,
        "correct_answer": "Dr. M. S. Swaminathan",
        "explanation": "Dr. M. S. Swaminathan is universally revered as the Father of the Green Revolution in India for introducing HYV wheat varieties and modern agricultural packages.",
        "feedback_correct": "Correct! Dr. M. S. Swaminathan led the Indian Green Revolution.",
        "feedback_incorrect": "Incorrect. Dr. M. S. Swaminathan is the Father of the Green Revolution (Dr. Kurien led the White/Milk Revolution).",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    # ==========================================
    # MODULE 12: BOARD EXAM SPECIAL BLUEPRINT & MAP WORK
    # ==========================================
    blocks.append({
        "type": "exam_tips",
        "title": "BOARD EXAM MASTER BLUEPRINT & MAP WORK",
        "content": "🔥 **GSEB & NCERT BOARD EXAM HIGH-FREQUENCY QUESTIONS & MODEL BLUEPRINTS**\n\n### Q1. Distinguish between Kharif and Rabi crops. (3 Marks)\n- **Kharif Crops:** Monsoon season (June-July to Oct-Nov); warm and rainy climate; Crops: Paddy, Jowar, Bajra, Cotton, Groundnut.\n- **Rabi Crops:** Winter season (Oct-Nov to March-April); cool and dry climate with bright sun; Crops: Wheat, Gram, Mustard, Barley.\n\n### Q2. Explain the Institutional Reforms in Indian Agriculture. (5 Marks)\n- **Answer Blueprint:** (1) Abolition of Zamindari system, (2) Land to the Tiller Act (Land Tenancy Act), (3) Land Ceiling Act to curb inequality, (4) Land Consolidation, (5) Kisan Credit Card (KCC) low-interest loans, (6) PMFBY Crop Insurance, (7) APMC Market Yards, (8) Minimum Support Price (MSP) through NAFED, GROFED, NDDB, FCI.\n\n### Q3. Explain the Technical Reforms in Indian Agriculture. (5 Marks)\n- **Answer Blueprint:** (1) Mechanization with tractors/harvesters, (2) HYV hybrid seeds, (3) Drip and Sprinkler irrigation systems, (4) Chemical & Bio-fertilizers, (5) Plant protection & IPM, (6) Soil Health Card laboratory testing, (7) Kisan Call Center (1800-180-1551) & DD Kisan, (8) i-Khedut portal & Agricultural Universities.\n\n### Q4. Describe the geographical conditions required for Paddy and Wheat. (4 Marks)\n- **Paddy:** Tropical hot & humid; >20°-25°C; >100 cm rain; fertile alluvial clayey soil; West Bengal leads.\n- **Wheat:** Temperate cool & sunny; 75 cm rain; black/loamy soil; frost is harmful; UP & Punjab lead.\n\n---\n\n🗺️ **BOARD EXAM MAP WORK GUIDE (ભારતનો રેખાંકિત નકશો / मानचित्र कार्य):**\n1. **Major Wheat Producing State** ➔ **Punjab / Uttar Pradesh**\n2. **Major Paddy Producing State** ➔ **West Bengal**\n3. **Major Groundnut Producing State** ➔ **Gujarat (Junagadh / Saurashtra)**\n4. **Major Cotton Producing State** ➔ **Gujarat (Bharuch / Kanam Region)**\n5. **Major Tea Producing State** ➔ **Assam / West Bengal (Darjeeling)**\n6. **Major Coffee Producing Region** ➔ **Karnataka (Coorg / Kodagu)**\n7. **Major Sugarcane Producing State** ➔ **Uttar Pradesh**\n8. **Major Jute Producing State** ➔ **West Bengal (Hooghly Basin)**\n9. **Major Rubber Producing State** ➔ **Kerala**\n10. **Major Tobacco Region in Gujarat** ➔ **Charotar (Kheda / Anand)**",
        "body": "🔥 **GSEB & NCERT BOARD EXAM HIGH-FREQUENCY QUESTIONS & MODEL BLUEPRINTS**\n\n### Q1. Distinguish between Kharif and Rabi crops. (3 Marks)\n- **Kharif Crops:** Monsoon season (June-July to Oct-Nov); warm and rainy climate; Crops: Paddy, Jowar, Bajra, Cotton, Groundnut.\n- **Rabi Crops:** Winter season (Oct-Nov to March-April); cool and dry climate with bright sun; Crops: Wheat, Gram, Mustard, Barley.\n\n### Q2. Explain the Institutional Reforms in Indian Agriculture. (5 Marks)\n- **Answer Blueprint:** (1) Abolition of Zamindari system, (2) Land to the Tiller Act (Land Tenancy Act), (3) Land Ceiling Act to curb inequality, (4) Land Consolidation, (5) Kisan Credit Card (KCC) low-interest loans, (6) PMFBY Crop Insurance, (7) APMC Market Yards, (8) Minimum Support Price (MSP) through NAFED, GROFED, NDDB, FCI.\n\n### Q3. Explain the Technical Reforms in Indian Agriculture. (5 Marks)\n- **Answer Blueprint:** (1) Mechanization with tractors/harvesters, (2) HYV hybrid seeds, (3) Drip and Sprinkler irrigation systems, (4) Chemical & Bio-fertilizers, (5) Plant protection & IPM, (6) Soil Health Card laboratory testing, (7) Kisan Call Center (1800-180-1551) & DD Kisan, (8) i-Khedut portal & Agricultural Universities.\n\n### Q4. Describe the geographical conditions required for Paddy and Wheat. (4 Marks)\n- **Paddy:** Tropical hot & humid; >20°-25°C; >100 cm rain; fertile alluvial clayey soil; West Bengal leads.\n- **Wheat:** Temperate cool & sunny; 75 cm rain; black/loamy soil; frost is harmful; UP & Punjab lead.\n\n---\n\n🗺️ **BOARD EXAM MAP WORK GUIDE (ભારતનો રેખાંકિત નકશો / मानचित्र कार्य):**\n1. **Major Wheat Producing State** ➔ **Punjab / Uttar Pradesh**\n2. **Major Paddy Producing State** ➔ **West Bengal**\n3. **Major Groundnut Producing State** ➔ **Gujarat (Junagadh / Saurashtra)**\n4. **Major Cotton Producing State** ➔ **Gujarat (Bharuch / Kanam Region)**\n5. **Major Tea Producing State** ➔ **Assam / West Bengal (Darjeeling)**\n6. **Major Coffee Producing Region** ➔ **Karnataka (Coorg / Kodagu)**\n7. **Major Sugarcane Producing State** ➔ **Uttar Pradesh**\n8. **Major Jute Producing State** ➔ **West Bengal (Hooghly Basin)**\n9. **Major Rubber Producing State** ➔ **Kerala**\n10. **Major Tobacco Region in Gujarat** ➔ **Charotar (Kheda / Anand)**",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })
    
    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_dir = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters"
    os.makedirs(out_dir, exist_ok=True)
    
    # 1. Output GSEB JSON
    gseb_path = os.path.join(out_dir, "gseb_class10_social_science_ch10.json")
    final_json_gseb = json.loads(json.dumps(final_json))
    final_json_gseb["metadata"]["id"] = "gseb_class10_social_science_ch10"
    with open(gseb_path, "w", encoding="utf-8") as f:
        json.dump(final_json_gseb, f, indent=2, ensure_ascii=False)
        
    # 2. Output NCERT JSON
    ncert_path = os.path.join(out_dir, "ncert_class10_social_science_ch10.json")
    final_json_ncert = json.loads(json.dumps(final_json))
    final_json_ncert["metadata"]["id"] = "ncert_class10_social_science_ch10"
    with open(ncert_path, "w", encoding="utf-8") as f:
        json.dump(final_json_ncert, f, indent=2, ensure_ascii=False)
        
    print("Supreme GSEB/NCERT Social Science Chapter 10 'India: Agriculture' Script Ready!")

if __name__ == "__main__":
    generate_supreme_gseb_ss_ch10()
