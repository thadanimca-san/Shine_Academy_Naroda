import json
import os

def generate_supreme_gseb_ss_ch18():
    chapter_id = "gseb_class10_social_science_ch18"
    title = "Chapter 18: Price Rise and Consumer Awareness"
    
    metadata = {
        "id": chapter_id,
        "title": title,
        "subtitle": "The Ultimate Board Exam Mastery Guide (Supreme Pedagogy)",
        "subject": "Social Science",
        "grade": "10",
        "board": "GSEB / NCERT",
        "curriculum": ["Universal", "GSEB", "CBSE"],
        "language": "English/Hindi/Gujarati (Bilingual)",
        "difficulty": "Advanced",
        "estimated_minutes": 180,
        "version": "3.0.0-SUPREME-SS",
        "author": "Antigravity Supreme Intelligence",
        "reviewed_by": "Chief Academic Architect",
        "tags": [
            "economics",
            "social_science",
            "price_rise",
            "inflation",
            "consumer_awareness",
            "copra",
            "consumer_rights",
            "quality_marks",
            "agmark",
            "isi_bis",
            "hallmark",
            "three_tier_court",
            "board_special",
            "bilingual"
        ],
        "learning_outcomes": [
            "Understand the economic concept of Price Rise (`inflation` `(मुद्रास्फीति / ફુગાવો)`) and differentiate between healthy price stability and destructive inflation.",
            "Analyze the primary economic, demographic, and artificial causes of Price Rise including deficit financing and hoarding.",
            "Evaluate the socio-economic ill-effects of Price Rise on different income classes and national balance of payments.",
            "Master Monetary, Fiscal, and Administrative measures used by the Government and RBI to control inflation.",
            "Identify various forms and root causes of Consumer Exploitation (`उपभोक्ता शोषण / ગ્રાહક શોષણ`) in modern markets.",
            "Memorize the 6 Fundamental Consumer Rights and essential Consumer Duties under COPRA.",
            "Identify and recognize Standard Quality Certification Marks (ISI/BIS, AGMARK, FPO/FSSAI, Hallmark, Eco Mark).",
            "Navigate the Three-Tier Quasi-Judicial Consumer Redressal Mechanism (District, State, and National Commissions) for dispute resolution."
        ],
        "ai_context": {
            "learning_goal": "Transform the student into an economics topper and an empowered, vigilant consumer. Provide deep conceptual clarity on macroeconomics (inflation & monetary policy) and legal consumer protection with bilingual explanations.",
            "common_misconceptions": [
                "Students think ANY price rise is bad for the economy (Fact: Mild, stable price rise stimulates investment, production, and employment; runaway hyperinflation is harmful).",
                "Students confuse AGMARK (agricultural products) with Hallmark (precious jewelry) or ISI/BIS (industrial/electronic products).",
                "Students confuse the pecuniary jurisdiction limits of District, State, and National Consumer Commissions under the Consumer Protection Act.",
                "Students confuse World Consumer Rights Day (15th March) with India's National Consumer Day (24th December)."
            ],
            "tutor_hint": "Use the 'Scale of Supply & Demand' analogy for price rise and the 'Shield of Rights' for consumer protection. Connect monetary policy with real-life examples like bank loan interest rates and ration shops."
        }
    }
    
    blocks = []
    
    # =========================================================================
    # MODULE 1: PRICE RISE — AN ECONOMIC PHENOMENON
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "Imagine you went to your favorite snack stall 5 years ago with a ₹100 note `(सौ रुपये का नोट / સો રૂપિયાની નોટ)` and bought snacks for your entire family. Today, that same ₹100 note cannot even buy two plates of snacks! Why does paper money lose its power over time? Where does that lost value go? Welcome to the fascinating and critical economic concept of **Price Rise (`inflation` `(मुद्रास्फीति / ફુગાવો)`)**!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Price Rise occurs when the aggregate demand for goods exceeds the total supply available in the market, causing currency value to decline and prices to surge.",
        "image_url": "assets/images/ss_ch18_demand_supply_inflation.jpg",
        "alt_text": "Seesaw showing High Demand on one side and Low Supply on the other causing Price Levels to rise."
    })

    blocks.append({
        "type": "ai_tutor_prompt",
        "content": "Is every single price increase bad for a country? What would happen if prices remained completely frozen forever—would business owners ever have an incentive to invest money, build new factories, or hire more workers?",
        "options": [
            "Yes, all price rise is always 100% destructive to everyone.",
            "No, a mild and stable price rise acts as a tonic that encourages producers to invest and generate employment.",
            "Prices never affect production or employment."
        ],
        "correct_answer": "No, a mild and stable price rise acts as a tonic that encourages producers to invest and generate employment.",
        "explanation": "A slow, predictable rise in prices increases profit margins for producers, motivating them to invest capital `(पूँजी / મૂડી)` and hire more workers. However, continuous and steep price rise across all sectors disrupts the entire economy."
    })
    
    blocks.append({
        "type": "theory",
        "content": "### What is Price Rise?\n\nIn an economy, continuous and persistent increase in the price of goods and services across all sectors over a prolonged period is called **Price Rise (`inflation` `(मुद्रास्फीति / ફુગાવો)`)**.\n\n* **Healthy Price Rise vs Destructive Inflation:**\n  1. **Price Rise with Stability (`स्थिरता के साथ मूल्य वृद्धि / સ્થિરતા સાથે ભાવવૃદ્ધિ`):** When prices rise slowly at a steady, controlled rate, it boosts profits, encourages new industrial investment `(औद्योगिक निवेश / ઔદ્યોગિક મૂડીરોકાણ)`, and generates employment opportunities. Hence, mild price rise is called a **tonic for economic development**.\n  2. **Runaway / Uncontrolled Price Rise (`अनियंत्रित मूल्य वृद्धि / અનિયંત્રિત ભાવવૃદ્ધિ`):** When prices of essential commodities rise sharply and continuously, the purchasing power `(क्रय शक्ति / ખરીદશક્તિ)` of money plummets, causing extreme distress to common citizens.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Teacher's Secret Insight:** Remember the crucial difference for board exams! A seasonal increase in the price of tomatoes after heavy rain is NOT general inflation. Inflation occurs only when there is a **continuous, widespread, and sustained rise** across almost all goods and services in the economy.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "mcq",
        "content": "Why is a mild and steady price rise considered a 'tonic' for an economy?",
        "options": [
            "It decreases government tax collection.",
            "It motivates producers to increase investment and creates new jobs.",
            "It makes domestic products impossible to export.",
            "It reduces the wages of all industrial workers."
        ],
        "correct_index": 1,
        "explanation": "Mild price rise boosts profit expectations of manufacturers, prompting them to invest more capital and generate new employment opportunities.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    # =========================================================================
    # MODULE 2: CAUSES OF PRICE RISE
    # =========================================================================
    blocks.append({
        "type": "theory",
        "content": "### Main Reasons for Price Rise (`ભાવવૃદ્ધિના કારણો / मूल्य वृद्धि के कारण`)\n\nPrice rise is primarily driven by two fundamental macroeconomic forces: **Increase in Total Demand** and **Shortage in Total Supply**.\n\n1. **Increase in Supply of Money (`मुद्रा आपूर्ति में वृद्धि / નાણાના પુરવઠામાં વધારો`):**\n   - **Deficit Financing (`घाटे का वित्तपोषण / ખાદ્ય પુરાવણી`):** When government expenditure exceeds its revenue, the government prints new currency notes, increasing money circulation in the market.\n   - **Increase in Velocity of Money:** Rapid circulation of loans and credit increases disposable income among buyers.\n   - **Black Money (`काला धन / કાળું નાણું`):** Unaccounted, untaxed money that is spent recklessly on luxury goods and real estate, inflating general prices.\n\n2. **High Population Growth (`तीव्र जनसंख्या वृद्धि / ઝડપી વસ્તી વૃદ્ધિ`):**\n   - India's population increases rapidly, continuously escalating the aggregate consumer demand for food, housing, clothing, and energy.\n\n3. **Increase in Exports (`निर्यात में वृद्धि / નિકાસમાં વધારો`):**\n   - When high volumes of domestic produce (e.g., onions, sugar, spices) are exported abroad to earn foreign exchange, supply in the domestic market decreases, triggering domestic price spikes.\n\n4. **Shortage of Raw Materials (`कच्चे माल की कमी / કાચા માલની અછત`):**\n   - High prices of raw materials, fuel (crude oil), electricity, and transportation raise the cost of production `(उत्पादन लागत / ઉત્પાદન ખર્ચ)`, leading to cost-push price rise.\n\n5. **Natural Calamities & Supply Shocks (`प्राकृतिक आपदाएँ / કુદરતી આપત્તિઓ`):**\n   - Droughts `(सूखा / દુષ્કાળ)`, floods, earthquakes, pests, or human factors like industrial strikes and wars disrupt production cycles.\n\n6. **Anti-Social Market Evils:**\n   - **Hoarding (`जमाखोरी / સંગ્રહખોરી`):** Greedy traders hide stock in warehouses to create artificial scarcity `(कृत्रिम कमी / કૃત્રિમ અછત)` and sell later at exorbitant rates.\n   - **Black Marketing (`कालाबाजारी / કાળાબજાર`):** Selling scarce commodities covertly at illegal, inflated prices.\n   - **Smuggling (`तस्करी / દાણચોરી`):** Illicit transit of goods evading taxes.\n\n7. **Government Administered Prices (`सरकार द्वारा मूल्य निर्धारण / સરકારી ભાવ નિર્ધારણ`):**\n   - Periodic revisions in the **Minimum Support Price (`MSP` `(न्यूनतम समर्थन मूल्य / ટેકાના ભાવ)`)** for agricultural crops, and price hikes in petrol, diesel, cooking gas (LPG), and railway freight tariffs directly inflate the prices of all related commodities.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    blocks.append({
        "type": "diagram",
        "content": "Overview of the primary demand-side, supply-side, and artificial factors that fuel price rise in India.",
        "image_url": "assets/images/ss_ch18_causes_of_price_rise_tree.jpg",
        "alt_text": "Conceptual mind map detailing Money Supply, Deficit Financing, Population, Hoarding, and Administrative Price Hikes."
    })

    blocks.append({
        "type": "memory_trick",
        "content": "**Mnemonic to Remember the Causes of Price Rise:**\n**M - P - E - R - A - G - S**\n- **M** -> **M**oney supply increase & Deficit Financing\n- **P** -> **P**opulation surge\n- **E** -> **E**xports increase (domestic shortages)\n- **R** -> **R**aw material cost escalation\n- **A** -> **A**nti-social hoarding & Black marketing\n- **G** -> **G**overnment MSP & Fuel price revisions\n- **S** -> **S**upply disruptions & Natural calamities",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "mcq",
        "content": "When greedy merchants intentionally hide stocks of food grains in godowns to create an artificial shortage and charge high prices, what is this malpractice called?",
        "options": [
            "Deficit Financing `(घाटे का वित्तपोषण)`",
            "Hoarding `(जमाखोरी / સંગ્રહખોરી)`",
            "Export Promotion `(निर्यात प्रोत्साहन)`",
            "Open Market Operation `(खुले बाजार की प्रक्रिया)`"
        ],
        "correct_index": 1,
        "explanation": "Hoarding `(जमाखोरी / સંગ્રહખોરી)` is the illegal practice of accumulating and concealing essential stock to create artificial scarcity and inflate market prices.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    # =========================================================================
    # MODULE 3: EFFECTS OF PRICE RISE
    # =========================================================================
    blocks.append({
        "type": "theory",
        "content": "### Ill-Effects of Price Rise on Society & Economy (`ભાવવૃદ્ધિની અસરો`)\n\nPersistent inflation acts as an invisible tax that erodes the foundation of an economy:\n\n1. **Severe Blow to Fixed Income Groups (`निश्चित आय वर्ग पर कुठाराघात / નિશ્ચિત આવક ધરાવતા વર્ગ પર ફટકો`):**\n   - Salaried employees, pensioners, and daily wage laborers suffer because their income remains fixed while living costs skyrocket, leading to a fall in their standard of living.\n\n2. **Decline in Savings & Capital Formation (`बचत और पूँजी निर्माण में कमी / બચત અને મૂડી સર્જનમાં ઘટાડો`):**\n   - As families spend almost all earnings on basic survival (food, health, rent), household savings dry up, reducing capital investment in productive industries.\n\n3. **Distortion of Production Priorities (`उत्पादन प्राथमिकताओं में विकृति`):**\n   - Capital shifts away from producing essential consumer necessities towards highly profitable luxury goods consumed by the ultra-rich.\n\n4. **Adverse Impact on Foreign Trade (`विदेश व्यापार पर प्रतिकूल प्रभाव / વિદેશી વેપાર પર વિપરીત અસર`):**\n   - Domestic goods become expensive, making exports less competitive in the international market, while cheaper foreign imports flood the country. This creates a severe **Foreign Exchange Deficit (`विदेशी मुद्रा संकट / વિદેશી હૂંડિયામણની તંગી`)**.\n\n5. **Widening Gap Between Rich and Poor (`अमीर-गरीब के बीच बढ़ती खाई`):**\n   - Speculators, hoarders, and big traders make windfall profits, whereas poor and middle-class citizens sink deeper into poverty and debt.\n\n6. **Moral and Social Degradation (`नैतिक पतन / નૈતિક અધઃપતન`):**\n   - Inability to meet daily household expenses drives people towards corruption `(भ्रष्टाचार / ભ્રષ્ટાચાર)`, bribery, black marketing, theft, adulteration `(मिलावट / ભેળસેળ)`, and crime.",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM TOPPER TIP (Frequently Asked 4-Mark Question):**\n'Price rise is an obstacle in economic development. Explain.'\n\n**Topper Answer Blueprint:**\n1. **Define Price Rise:** Continuous, multi-sectoral price hike reducing the purchasing power of money.\n2. **Point 1 - Reduced Savings:** High living costs eliminate domestic savings and industrial capital creation.\n3. **Point 2 - Export Deficit:** High production costs make domestic exports uncompetitive, depleting foreign exchange reserves.\n4. **Point 3 - Inequality:** Widens economic disparity between rich asset owners and poor salaried workers.\n5. **Point 4 - Social Unrest:** Encourages black marketing, hoarding, and moral decay.",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    blocks.append({
        "type": "mcq",
        "content": "Which segment of society is harmed the MOST by continuous, uncontrolled price rise?",
        "options": [
            "Large real estate owners and speculators",
            "Fixed-salary employees, pensioners, and daily wage workers",
            "Wholesale black marketers and hoarders",
            "Luxury goods manufacturers"
        ],
        "correct_index": 1,
        "explanation": "Fixed-income earners and daily wage laborers suffer the most because their income does not rise proportionally with skyrocketing prices, destroying their purchasing power.",
        "difficulty": "Intermediate",
        "bloom": "Analyze"
    })

    # =========================================================================
    # MODULE 4: MEASURES TO CONTROL PRICE RISE
    # =========================================================================
    blocks.append({
        "type": "theory",
        "content": "### Measures to Control Price Rise (`ભાવ નિયંત્રણના ઉપાયો`)\n\nThe Government of India and the Reserve Bank of India (`RBI` `(भारतीय रिज़र्व बैंक / ભારતીય રિઝર્વ બેંક)`) jointly implement five major strategies to stabilize prices:\n\n1. **Monetary Measures by Central Bank (RBI) (`मौद्रिक उपाय / નાણાકીય પગલાં`):**\n   - **Increasing Bank Rate & Repo Rate:** RBI increases lending rates to commercial banks. Consequently, banks raise interest rates on loans for businesses and consumers, discouraging unnecessary borrowing and reducing excess money in the market.\n   - **Increasing Cash Reserve Ratio (`CRR` `(नकद आरक्षित अनुपात / રોકડ અનામત ગુણોત્તર)`):** Banks must keep more reserves with RBI, reducing their capacity to disburse liberal credit.\n   - **Open Market Operations (`खुले बाजार की प्रक्रियाएं / ખુલ્લા બજારની નીતિ`):** RBI sells government securities and bonds in the open market to absorb excess cash liquidity from the public.\n\n2. **Fiscal Measures by Government (`राजकोषीय उपाय / રાજકોષીય પગલાં`):**\n   - **Curtailing Non-Essential Public Spending:** Government postpones non-developmental, wasteful expenditures.\n   - **Direct Taxation:** Imposing higher direct taxes on wealthy individuals and high-profit corporations to reduce excessive disposable purchasing power.\n   - **Mobilizing Public Loans & Savings:** Launching attractive long-term national savings schemes (like PPF, Kisan Vikas Patra) to encourage citizens to save rather than spend.\n\n3. **Control on Capital Investment (`पूँजी निवेश पर नियंत्रण`):**\n   - Banning or heavily taxing speculative capital in luxury and unproductive assets, while directing subsidies and licenses towards essential mass-consumption items.\n\n4. **Public Distribution System (PDS) / Rationing (`सार્વજનિક વિતરણ પ્રણાલી / જાહેર વિતરણ પ્રણાલી`):**\n   - Setting up **Fair Price Shops (`FPS` `(उचित दर की दुकानें / વ્યાજબી ભાવની દુકાનો)`)** to supply essential food grains (wheat, rice), sugar, and kerosene at subsidized, affordable rates to Below Poverty Line (BPL) and middle-class families.\n\n5. **Administrative Measures & Legal Acts (`પ્રશાસનિક ઉપાયો અને કાયદાકીય પગલાં`):**\n   - **Essential Commodities Act, 1955 (`आवश्यक वस्तु अधिनियम, 1955`):** Empowers the government to fix ceiling prices on vital goods like grains, pulses, life-saving medicines, and edible oils.\n   - **Prevention of Black Marketing and Maintenance of Supplies of Essential Commodities Act (PBM Act / PASA / પાસા):** Empowers police authorities to conduct anti-hoarding raids, confiscate black-market stocks, and detain economic offenders.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    blocks.append({
        "type": "diagram",
        "content": "The dual-lever anti-inflation machinery in India: Monetary policy driven by the RBI and Fiscal/Administrative policy executed by the Government.",
        "image_url": "assets/images/ss_ch18_control_measures_rbi_govt.jpg",
        "alt_text": "Illustration showing RBI controlling interest rates and money supply, and Government managing PDS Fair Price Shops and Anti-Hoarding Laws."
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Teacher's Easy Logic:** Think of the economy like a flooded river of money. If there is too much money chasing too few goods, prices rise. To fix this:\n- **RBI acts as a Dam:** It raises interest rates on car/home loans so people borrow less money.\n- **Government acts as a Channel:** It opens Fair Price Shops (`વ્યાજબી ભાવની દુકાનો`) to provide cheap food grains directly to the needy!",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "mcq",
        "content": "Which statutory body in India regulates currency supply and raises interest rates (Repo Rate) to control excessive liquidity and inflation?",
        "options": [
            "Ministry of Agriculture",
            "Reserve Bank of India (RBI)",
            "Bureau of Indian Standards (BIS)",
            "National Consumer Commission (NCDRC)"
        ],
        "correct_index": 1,
        "explanation": "The Reserve Bank of India (RBI) is the central monetary authority responsible for framing monetary policy, setting repo/bank rates, and controlling credit liquidity.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    # =========================================================================
    # MODULE 5: CONSUMER AWARENESS — EXPLOITATION & FORMS
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "Have you ever bought a sealed packet of chips that felt full of air but had only 5 chips inside? Or bought a branded chocolate marked ₹50 where the shopkeeper demanded ₹55 claiming 'refrigerator cooling charge'? You were a victim of **Consumer Exploitation (`उपभोक्ता शोषण / ગ્રાહક શોષણ`)**! In theory, the customer is king; but in reality, an uninformed consumer is easily cheated.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "theory",
        "content": "### Who is a Consumer? (`ગ્રાહક કોણ છે? / उपभोक्ता कौन है?`)\n\nA **Consumer (`उपभोक्ता / ગ્રાહક`)** is any individual who purchases goods or hires services by paying money or promising to pay money in the future for personal consumption (not for resale or commercial profit).\n\n### Forms of Consumer Exploitation (`ગ્રાહક શોષણના પ્રકારો`)\n\n1. **Under-Weighing and Under-Measuring (`कम तौलना या मापना / ઓછું વજન કે માપ`):** Using tampered electronic scales, hollow-bottom weights, or short measuring tapes.\n2. **Adulteration & Substandard Quality (`मिलावट और घटिया गुणवत्ता / ભેળસેળ અને હલકી ગુણવત્તા`):** Mixing harmful chemicals, starch in milk, brick powder in chili, or supplying expired and fake medicines.\n3. **Charging More than MRP (`MRP से अधिक मूल्य वसूलना / છાપેલી કિંમત કરતાં વધુ ભાવ`):** Charging above the **Maximum Retail Price (`MRP` `(अधिकतम खुदरा मूल्य / મહત્તમ છૂટક કિંમત)`)** under the guise of cooling or transportation fees.\n4. **Misleading & Deceptive Advertisements (`भ्रामक विज्ञापन / ભ્રામક જાહેરાતો`):** Television and online ads making false claims of instant fairness in 7 days, miraculous weight loss, or 100% hair regrowth.\n5. **Poor After-Sales Service & Hidden Conditions (`बिक्री के बाद खराब सेवा / વેચાણ પછીની નબળી સેવા`):** Refusing warranty repair, delaying maintenance of home appliances, and citing hidden fine-print clauses.\n6. **Neglect of Safety Standards (`सुरक्षा मानकों की उपेक्षा / સલામતીના ધોરણોની ઉપેક્ષા`):** Selling non-certified electrical appliances or uninspected LPG regulators that cause life-threatening short circuits or fire hazards.\n\n### Reasons for Consumer Exploitation (`ગ્રાહક શોષણના કારણો`)\n- **Consumer Ignorance & Illiteracy (`उपभोक्ता अज्ञानता / ગ્રાહકની અજ્ઞાનતા`):** Lack of knowledge regarding consumer rights, quality seals, and legal procedures.\n- **Unorganized Consumers (`असंगठित उपभोक्ता / અસંગઠિત ગ્રાહકો`):** Individual buyers lack a collective voice compared to wealthy corporate producers.\n- **Lack of Genuine Bills (`पक्के बिल का अभाव / પાકા બિલનો અભાવ`):** Buying goods without a cash memo leaves no legal proof of purchase in court.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "ai_tutor_prompt",
        "content": "A local retail vendor refuses to give you a cash memo `(पक्का बिल / પાકું બિલ)` for an electric heater, saying: 'If you take a bill, you must pay 18% GST extra. Without a bill, it is ₹500 cheaper!' Should you agree? Why?",
        "options": [
            "Agree immediately, because saving ₹500 is the smartest consumer decision.",
            "Refuse and demand a tax invoice, because without a valid bill, you have zero warranty protection and cannot file a legal case if the heater bursts.",
            "Ask the shopkeeper for a verbal handshake guarantee instead."
        ],
        "correct_answer": "Refuse and demand a tax invoice, because without a valid bill, you have zero warranty protection and cannot file a legal case if the heater bursts.",
        "explanation": "A printed Cash Memo / Tax Invoice is the indispensable legal proof of transaction. Without it, consumer dispute forums will reject your compensation claim."
    })

    blocks.append({
        "type": "mcq",
        "content": "Which of the following constitutes an unfair trade practice and consumer exploitation?",
        "options": [
            "Providing a printed tax invoice with every purchase",
            "Clearly printing the expiry date and batch number on a medicine pack",
            "Charging ₹35 for a cold drink bottle marked with MRP ₹30 citing refrigeration costs",
            "Offering a manufacturer replacement for a defective product under warranty"
        ],
        "correct_index": 2,
        "explanation": "Charging even one rupee above the Maximum Retail Price (MRP) printed on the commodity is illegal under the Consumer Protection Act.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    # =========================================================================
    # MODULE 6: THE CONSUMER MOVEMENT & 6 MASTER RIGHTS
    # =========================================================================
    blocks.append({
        "type": "theory",
        "content": "### History of the Consumer Movement (`ગ્રાહક આંદોલનનો ઇતિહાસ`)\n\n- **Ralph Nader (`राल्फ नादर`):** Renowned American activist recognized globally as the **'Father of the Consumer Movement'** for campaigning against unsafe automobile manufacturing.\n- **15th March 1962:** US President **John F. Kennedy** proclaimed 4 basic consumer rights in the US Congress. Hence, **15th March** is celebrated worldwide every year as **World Consumer Rights Day (`विश्व उपभोक्ता अधिकार दिवस / વિશ્વ ગ્રાહક અધિકાર દિન`)**.\n- **24th December 1986:** The President of India signed the landmark **Consumer Protection Act, 1986 (`COPRA` `(उपभोक्ता संरक्षण अधिनियम, 1986 / ગ્રાહક સુરક્ષા અધિનિયમ, 1986)`)**. Hence, **24th December** is commemorated every year as **National Consumer Rights Day (`राष्ट्रीय उपभोक्ता अधिकार दिवस / રાષ્ટ્રીય ગ્રાહક અધિકાર દિન`)**.\n\n---\n\n### The 6 Fundamental Consumer Rights (`ગ્રાહકના 6 મૂળભૂત અધિકારો`)\n\n1. **Right to Safety (`सुरक्षा का अधिकार / સલામતીનો અધિકાર`):**\n   - Protection against goods, production processes, and services that are hazardous to physical health, life, or property (e.g., defective electrical wiring, spurious drugs).\n\n2. **Right to Information (`सूचना पाने का अधिकार / માહિતી મેળવવાનો અધિકાર`):**\n   - The right to be informed about the quality, quantity, purity, potency, standard, manufacturing date, expiry date, ingredients, and MRP of goods.\n\n3. **Right to Choose (`पसंद / चयन का अधिकार / પસંદગીનો અધિકાર`):**\n   - Freedom of choice to select from a variety of competitive goods and services at fair prices without monopolistic coercion or compulsory bundling.\n\n4. **Right to be Heard / Representation (`सुने जाने / प्रतिनिधित्व का अधिकार / રજૂઆત કરવાનો અધિકાર`):**\n   - The right to voice grievances and receive due consideration at appropriate non-governmental and governmental consumer forums.\n\n5. **Right to Redressal (`निवारण का अधिकार / નિવારણ મેળવવાનો અધિકાર`):**\n   - The right to seek fair settlement and legal remedies against unfair trade practices, including product repair, replacement, full refund, or monetary compensation for damages.\n\n6. **Right to Consumer Education (`उपभोक्ता शिक्षा का अधिकार / ગ્રાહક શિક્ષણનો અધિકાર`):**\n   - The right to acquire lifelong knowledge, skill, and awareness to remain an informed, conscious consumer throughout life (*'Jago Grahak Jago'* `(जागो ग्राहक जागो / જાગો ગ્રાહક જાગો)`).",
        "difficulty": "Advanced",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "diagram",
        "content": "The 6 Fundamental Consumer Rights established under the Consumer Protection Act (COPRA).",
        "image_url": "assets/images/ss_ch18_6_consumer_rights_shield.jpg",
        "alt_text": "Hexagonal shield displaying Safety, Information, Choice, Heard, Redressal, and Consumer Education."
    })

    blocks.append({
        "type": "memory_trick",
        "content": "**Mnemonic to Memorize the 6 Consumer Rights:**\n**S - I - C - H - R - E**\n- **S** -> **S**afety (`સલામતી / सुरक्षा`)\n- **I** -> **I**nformation (`માહિતી / सूचना`)\n- **C** -> **C**hoice (`પસંદગી / चयन`)\n- **H** -> **H**eard / Representation (`રજૂઆત / सुने जाने का अधिकार`)\n- **R** -> **R**edressal (`નિવારણ / निवारण`)\n- **E** -> **E**ducation (`શિક્ષણ / उपभोक्ता शिक्षा`)",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM FAVORITE (DO NOT CONFUSE THESE DATES!):**\n- **World Consumer Rights Day:** **15th March** `(15 માર્ચ / 15 मार्च)` (Marks John F. Kennedy's 1962 Declaration).\n- **National Consumer Rights Day (India):** **24th December** `(24 ડિસેમ્બર / 24 दिसंबर)` (Marks the presidential approval of COPRA in 1986).\n*Students often mix up these two dates in objective MCQs!*",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "mcq",
        "content": "Under which Consumer Right does a buyer have the legal entitlement to read the ingredients, manufacturing date, and expiry date printed on a food carton?",
        "options": [
            "Right to Safety",
            "Right to Information",
            "Right to Representation",
            "Right to Redressal"
        ],
        "correct_index": 1,
        "explanation": "The Right to Information guarantees that consumers are provided all vital data regarding the contents, date of manufacture, expiration, weight, and usage guidelines of a product.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    # =========================================================================
    # MODULE 7: DUTIES OF A CONSCIOUS CONSUMER
    # =========================================================================
    blocks.append({
        "type": "theory",
        "content": "### Duties & Responsibilities of an Enlightened Consumer (`જાગૃત ગ્રાહકની ફરજો`)\n\nRights cannot exist without duties. A smart consumer must practice the following:\n\n1. **Insist on a Cash Memo & Warranty Card (`पक्का बिल और वारंटी कार्ड लेना / પાકું બિલ અને વોરંટી કાર્ડ લેવું`):**\n   - Always demand a printed Tax Invoice with GST details, signed and stamped warranty/guarantee cards from the seller.\n2. **Look for Standard Quality Certification Marks (`मानक गुणवत्ता चिह्न जाँचना / પ્રમાણિત ચિહ્નો તપાસવા`):**\n   - Buy only certified goods carrying marks like **ISI / BIS**, **AGMARK**, **FSSAI / FPO**, or **Hallmark**.\n3. **Inspect Packaging Information Thoroughly (`पैकिंग विवरण की जाँच / પેકિંગ વિગતોની તપાસ`):**\n   - Verify Net Weight, Batch Number, MRP, Manufacturing Date, Best Before / Expiry Date, and seal integrity before paying.\n4. **Never Fall for Misleading Ads & Schemes (`भ्रामक विज्ञापनों से सावधान / લલચામણી જાહેરાતોથી સાવધ`):**\n   - Do not purchase goods based blindly on celebrity endorsements or unrealistic 'Free Gift' promotional gimmicks.\n5. **Report Fraud & File Complaints Promptly (`धोखाधड़ी की शिकायत दर्ज करना / ફરિયાદ નોંધાવવી`):**\n   - Do not stay silent if cheated over small amounts. Form consumer groups and file complaints before consumer forums to protect the public.",
        "difficulty": "Intermediate",
        "bloom": "Apply"
    })

    blocks.append({
        "type": "case_study",
        "content": "### Real-Life Case Study: Ankit's Unfortunate Geyser Purchase\n\nAnkit bought an unbranded electric water heater from a local hardware shop for ₹2,500. To save ₹300, he did not demand a cash memo or bill. Two weeks later, due to poor internal wiring, the geyser suffered an electrical short circuit and exploded, damaging the bathroom wall.\n\nWhen Ankit approached the District Consumer Forum for compensation:\n- **Outcome:** The consumer court rejected his petition at the admission stage!\n- **Reason:** Ankit had no Cash Memo or tax invoice to legally prove he purchased that specific geyser from the defendant shop.\n- **Moral:** Never sacrifice a genuine bill for a small instant discount!",
        "difficulty": "Intermediate",
        "bloom": "Analyze"
    })

    # =========================================================================
    # MODULE 8: STANDARD QUALITY CERTIFICATION MARKS
    # =========================================================================
    blocks.append({
        "type": "theory",
        "content": "### Standard Quality Certification Marks (`ગુણવત્તા પ્રમાણપત્ર ચિહ્નો`)\n\nTo protect consumer health and ensure quality, government and international organizations issue specialized certification seals:\n\n1. **ISI / BIS (`Bureau of Indian Standards` `(भारतीय मानक ब्यूरो / ભારતીય માનક બ્યુરો)`):**\n   - Printed on industrial and consumer manufactured products, electronic items (irons, geysers), cement, steel bars, LPG cylinders, packaged drinking water, and safety helmets.\n\n2. **AGMARK (`Agricultural Marketing`):**\n   - Issued by the **Directorate of Marketing and Inspection (`DMI`)** under the Agricultural Produce (Grading and Marking) Act, 1937.\n   - Compulsory quality mark for agricultural produce: pure ghee, edible oils, honey, ground spices, flours, and pulses.\n\n3. **FSSAI / FPO (`Food Safety and Standards Authority of India` / `Fruit Products Order`):**\n   - Mandatory statutory license mark on all packaged edible food products, fruit juices, jams, canned vegetables, sauces, and snacks.\n\n4. **Hallmark (BIS 916):**\n   - Certifies the exact purity of Gold and Silver jewelry.\n   - **The 4 Hallmark Elements:** BIS triangular logo, Carat purity grade (**916** for 22 Karat / **750** for 18 Karat), Assaying & Hallmarking Centre's mark, and a unique 6-digit alphanumeric **HUID (`Hallmark Unique Identification`)** code.\n\n5. **Silk Mark & Woolmark:**\n   - **Silk Mark:** Affixed to 100% natural, pure silk sarees and fabrics.\n   - **Woolmark:** Affixed to pure virgin wool textiles (International Wool Secretariat).\n\n6. **Eco Mark (`इको मार्क / ઇકો માર્ક`):**\n   - Issued by BIS to environment-friendly, non-polluting consumer goods (like soaps, detergents, paper, paints).\n   - **Symbol:** An **Earthen Pot (`मिट्टी का घड़ा / માટીનો ઘડો`)** representing harmony with Mother Earth.\n\n---\n\n### International Quality Standards Bodies (`આંતરરાષ્ટ્રીય ગુણવત્તા સંસ્થાઓ`)\n- **ISO (`International Organization for Standardization`):** Headquartered in **Geneva, Switzerland** (established in 1947). Formulates universal international management standards (e.g., ISO 9001 for quality management, ISO 14001 for environment).\n- **CAC (`Codex Alimentarius Commission`):** Established jointly by **FAO** and **WHO** in **Rome, Italy** (established in 1963) to set global food quality and safety benchmarks.",
        "difficulty": "Advanced",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "diagram",
        "content": "Visual guide to standard quality certification marks in India: ISI, AGMARK, FSSAI, Hallmark, Eco Mark, Silk Mark, and Woolmark.",
        "image_url": "assets/images/ss_ch18_standard_quality_marks.jpg",
        "alt_text": "Collection of logos: BIS ISI mark, AGMARK seal, FSSAI logo, Gold Hallmark 916, and Eco Mark earthen pot."
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Decoding Gold Jewelry Hallmark (Memorize for MCQs!):**\n- **24 Karat (100% pure gold):** Marked as **999**\n- **22 Karat (Standard jewelry gold):** Marked as **916** (meaning 91.6% pure gold + 8.4% copper/silver alloy)\n- **18 Karat (Diamond setting gold):** Marked as **750** (75% pure gold)",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "mcq",
        "content": "Which standard quality certification mark must you look for when purchasing agricultural edible products like pure ghee, turmeric powder, and mustard oil?",
        "options": [
            "ISI Mark",
            "AGMARK",
            "Woolmark",
            "Silk Mark"
        ],
        "correct_index": 1,
        "explanation": "AGMARK (issued by the Directorate of Marketing and Inspection) is the statutory quality certification mark for all agricultural and food produce in India.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "mcq",
        "content": "What is the official logo symbol of the 'Eco Mark' issued by the Bureau of Indian Standards (BIS) for environment-friendly products?",
        "options": [
            "A Green Leaf",
            "An Earthen Pot `(मिट्टी का घड़ा / માટીનો ઘડો)`",
            "A Solar Panel",
            "A Water Drop"
        ],
        "correct_index": 1,
        "explanation": "The Eco Mark logo features an Earthen Pot (Matka), symbolizing eco-friendliness, recyclable nature, and harmony with the environment.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    # =========================================================================
    # MODULE 9: THREE-TIER CONSUMER DISPUTE REDRESSAL MECHANISM
    # =========================================================================
    blocks.append({
        "type": "theory",
        "content": "### Three-Tier Quasi-Judicial Consumer Redressal Machinery (`ત્રિ-સ્તરીય ગ્રાહક તકરાર નિવારણ તંત્ર`)\n\nUnder the Consumer Protection Act, a special 3-tier quasi-judicial court system has been established to provide swift, simple, and inexpensive justice to exploited consumers:\n\n```\n                    [ SUPREME COURT OF INDIA ]\n                                ▲ (Appeal within 30 days)\n                                │\n             [ NATIONAL CONSUMER COMMISSION (NCDRC) ]\n                     • New Delhi | Claims > ₹10 Crore\n                                ▲ (Appeal within 30-45 days)\n                                │\n              [ STATE CONSUMER COMMISSION (SCDRC) ]\n                • State Capital | Claims ₹1 Crore - ₹10 Crore\n                                ▲ (Appeal within 45 days, 50% deposit)\n                                │\n             [ DISTRICT CONSUMER COMMISSION (DCDRC) ]\n                   • Every District | Claims Up to ₹1 Crore\n```\n\n#### 1. District Consumer Disputes Redressal Commission (`જિલ્લા ગ્રાહક આયોગ / जिला उपभोक्ता आयोग`):\n- **Jurisdiction (`कार्यक्षेत्र`):** Covers complaints where the value of goods/services and compensation claim is **up to ₹1 Crore** `(1 करोड़ रुपये तक / ₹1 કરોડ સુધી)`. *(Under the historic 1986 Act, this limit was up to ₹20 Lakhs)*.\n- **Appeal (`अपील`):** If a party is dissatisfied with the District Commission's verdict, they can appeal to the State Commission within **45 days** by depositing 50% of the awarded penalty amount.\n\n#### 2. State Consumer Disputes Redressal Commission (`રાજ્ય ગ્રાહક આયોગ / राज्य उपभोक्ता आयोग`):\n- **Location:** Established at the respective State Capital (e.g., Gandhinagar / Ahmedabad for Gujarat).\n- **Jurisdiction (`कार्यक्षेत्र`):** Covers original claims between **₹1 Crore and ₹10 Crore** `(1 करोड़ से 10 करोड़ रुपये / ₹1 કરોડથી ₹10 કરોડ)`. *(Under the historic 1986 Act, this was ₹20 Lakhs to ₹1 Crore)*.\n- **Appeal (`अपील`):** Appeals against State Commission orders can be submitted to the National Commission within **30-45 days**.\n\n#### 3. National Consumer Disputes Redressal Commission - NCDRC (`રાષ્ટ્રીય ગ્રાહક આયોગ / राष्ट्रीय उपभोक्ता आयोग`):\n- **Location:** Apex body located in **New Delhi**.\n- **Jurisdiction (`कार्यक्षेत्र`):** Covers original claims exceeding **₹10 Crore** `(10 करोड़ रुपये से अधिक / ₹10 કરોડથી વધુ)`. *(Under the historic 1986 Act, this was above ₹1 Crore)*.\n- **Final Appeal (`अंतिम अपील`):** Aggrieved parties can appeal against the NCDRC verdict directly before the **Supreme Court of India (`सर्वोच्च न्यायालय / સર્વોચ્ચ અદાલત`)** within **30 days**.\n\n---\n\n### How to File a Consumer Complaint (`ફરિયાદ દાખલ કરવાની સરળ રીત`)\n- **No Advocate Mandatory:** A consumer can represent themselves or file via an authorized representative on a simple written application.\n- **Nominal Fee:** Very low statutory court fee (or free for BPL consumers).\n- **Online Filing (`e-Daakhil`):** Complaints can be submitted digitally via the national portal `edaakhil.nic.in` or registered via the National Consumer Helpline toll-free number **1915**.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    blocks.append({
        "type": "diagram",
        "content": "Pyramid architecture of the Three-Tier Consumer Dispute Redressal Machinery showing District Commission, State Commission, National Commission, and Supreme Court.",
        "image_url": "assets/images/ss_ch18_three_tier_consumer_court.jpg",
        "alt_text": "3-Tier Consumer Redressal Hierarchy indicating financial jurisdiction limits and appellate paths."
    })

    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HIGH-YIELD FORMULA (Jurisdiction Limits Summary):**\n- **District Commission (`જિલ્લા આયોગ`):** Claim value **Up to ₹1 Crore**\n- **State Commission (`રાજ્ય આયોગ`):** Claim value **₹1 Crore to ₹10 Crore**\n- **National Commission (`રાષ્ટ્રીય આયોગ`):** Claim value **Above ₹10 Crore**\n*Remember: If a patient dies due to hospital negligence and seeks ₹12 Crore compensation, the case goes DIRECTLY to the National Commission in New Delhi!*",
        "difficulty": "Advanced",
        "bloom": "Apply"
    })

    blocks.append({
        "type": "mcq",
        "content": "A builder sells a defective penthouse flat to a customer for ₹3.5 Crore, and the structure develops severe cracks. In which consumer forum must the customer file the original complaint?",
        "options": [
            "District Consumer Commission",
            "State Consumer Disputes Redressal Commission",
            "National Consumer Commission (NCDRC)",
            "Local Municipality Office"
        ],
        "correct_index": 1,
        "explanation": "Claims with a compensation value between ₹1 Crore and ₹10 Crore fall under the original pecuniary jurisdiction of the State Consumer Commission.",
        "difficulty": "Intermediate",
        "bloom": "Apply"
    })

    blocks.append({
        "type": "mcq",
        "content": "If a consumer is aggrieved by a judgment delivered by the District Consumer Commission, within how many days can an appeal be filed before the State Consumer Commission?",
        "options": [
            "10 days",
            "45 days",
            "90 days",
            "180 days"
        ],
        "correct_index": 1,
        "explanation": "An appeal against an order of the District Commission can be preferred before the State Commission within 45 days along with a 50% deposit of the awarded amount.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    # =========================================================================
    # MODULE 10: BOARD EXAM HOTS & SUMMARY
    # =========================================================================
    blocks.append({
        "type": "board_questions",
        "content": "### Most Important Board Exam Questions (HOTS & 4-Markers)\n\n1. **Q1 (4 Marks):** Explain the main monetary and fiscal measures implemented by the Government and RBI to control price rise in India.\n2. **Q2 (4 Marks):** Describe the 6 fundamental consumer rights provided under the Consumer Protection Act.\n3. **Q3 (3 Marks):** Detail the structure and pecuniary jurisdiction limits of the Three-Tier Consumer Dispute Redressal Machinery.\n4. **Q4 (3 Marks):** Differentiate between AGMARK, ISI mark, Hallmark, and Eco Mark with their respective product categories.\n5. **Q5 (2 Marks):** Why is 15th March celebrated as World Consumer Rights Day and 24th December as National Consumer Day in India?",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    blocks.append({
        "type": "summary",
        "content": "### Chapter 18 Quick Revision Matrix (`સારાંશ`)\n\n- **Price Rise (Inflation):** Continuous, widespread increase in general prices. Mild price rise fuels growth; uncontrolled inflation destroys purchasing power.\n- **Causes of Inflation:** Money supply expansion (deficit financing, black money), population surge, hoarding, high raw material costs, and export surges.\n- **Control Remedies:** RBI raises interest rates (Repo/Bank Rate) and CRR; Government uses PDS Fair Price Shops and the Essential Commodities Act.\n- **Consumer Protection:** Ralph Nader (Father of Movement). COPRA enacted on 24 Dec 1986.\n- **6 Master Rights:** Safety, Information, Choice, Heard, Redressal, Education.\n- **Quality Seals:** ISI (industrial/electrical), AGMARK (agricultural), FSSAI (food), Hallmark 916 (gold), Eco Mark (earthen pot).\n- **3-Tier Courts:** District (Up to ₹1 Cr) ➔ State (₹1 Cr to ₹10 Cr) ➔ National (> ₹10 Cr) ➔ Supreme Court.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    # Save GSEB Version
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_social_science_ch18.json"
    os.makedirs(os.path.dirname(gseb_path), exist_ok=True)
    with open(gseb_path, "w", encoding="utf-8") as f:
        json.dump(final_json, f, indent=2, ensure_ascii=False)
    print(f"Successfully generated GSEB chapter at: {gseb_path}")
    
    # Save NCERT Version
    ncert_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_social_science_ch18.json"
    final_json["metadata"]["id"] = "ncert_class10_social_science_ch18"
    final_json["metadata"]["board"] = "NCERT / CBSE"
    with open(ncert_path, "w", encoding="utf-8") as f:
        json.dump(final_json, f, indent=2, ensure_ascii=False)
    print(f"Successfully synced NCERT chapter at: {ncert_path}")

if __name__ == "__main__":
    generate_supreme_gseb_ss_ch18()
