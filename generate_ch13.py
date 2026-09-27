import json

blocks = [
    {
        "id": "KOBJ_NCERT_C10_SCI_CH13_001",
        "type": "hook",
        "title": "The Invisible Web of Life",
        "title_hi": "जीवन का अदृश्य जाल",
        "title_gu": "જીવનનું અદૃશ્ય જાળું",
        "body": "Have you ever wondered what happens to a fallen leaf in a forest? It doesn't just disappear. It becomes food for tiny insects, which are eaten by frogs, which are then eaten by snakes. Every living being on Earth, from the smallest bacteria to the largest whale, is connected in a giant, invisible web of life. If one thread breaks, the whole web shakes!",
        "body_hi": "क्या आपने कभी सोचा है कि जंगल में गिरे हुए पत्ते का क्या होता है? वह ऐसे ही गायब नहीं हो जाता। यह छोटे कीड़ों का भोजन बन जाता है, जिन्हें मेंढक खाते हैं, जिन्हें फिर सांप खा जाते हैं। पृथ्वी पर हर जीवित प्राणी, सबसे छोटे जीवाणु से लेकर सबसे बड़ी व्हेल तक, जीवन के एक विशाल, अदृश्य जाल में जुड़ा हुआ है। यदि एक धागा टूटता है, तो पूरा जाल हिल जाता है!",
        "body_gu": "શું તમે ક્યારેય વિચાર્યું છે કે જંગલમાં પડેલા પાંદડાનું શું થાય છે? તે માત્ર અદૃશ્ય થઈ જતું નથી. તે નાના જંતુઓ માટે ખોરાક બની જાય છે, જેને દેડકા ખાય છે, જેને પછી સાપ ખાય છે. પૃથ્વી પરનો દરેક જીવ, નાનામાં નાના બેક્ટેરિયાથી લઈને સૌથી મોટી વ્હેલ સુધી, જીવનની એક વિશાળ, અદૃશ્ય જાળમાં જોડાયેલો છે. જો એક દોરો તૂટી જાય, તો આખી જાળ હલી જાય છે!"
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH13_002",
        "type": "theory",
        "title": "Ecosystem and its Components",
        "title_hi": "पारिस्थितिक तंत्र और इसके घटक",
        "title_gu": "નિવસનતંત્ર અને તેના ઘટકો",
        "body": "An Ecosystem is a self-sustaining system where all living organisms (biotic components like plants, animals, bacteria) interact with each other and their non-living environment (abiotic components like air, water, soil, sunlight).\nOrganisms are grouped based on how they get food:\n1. Producers: Make their own food using sunlight (Autotrophs like green plants).\n2. Consumers: Eat other organisms (Herbivores, Carnivores, Omnivores, Parasites).\n3. Decomposers: Break down dead remains and waste products (Bacteria, Fungi), returning nutrients to the soil.",
        "body_hi": "पारिस्थितिक तंत्र (Ecosystem) एक स्व-टिकाऊ प्रणाली है जहाँ सभी जीवित जीव (जैविक घटक जैसे पौधे, जानवर, बैक्टीरिया) एक-दूसरे और अपने निर्जीव पर्यावरण (अजैविक घटक जैसे हवा, पानी, मिट्टी, धूप) के साथ बातचीत करते हैं।\nजीवों को उनके भोजन प्राप्त करने के तरीके के आधार पर समूहीकृत किया जाता है:\n1. उत्पादक (Producers): सूर्य के प्रकाश का उपयोग करके अपना भोजन स्वयं बनाते हैं (हरे पौधों की तरह स्वपोषी)।\n2. उपभोक्ता (Consumers): अन्य जीवों को खाते हैं (शाकाहारी, मांसाहारी, सर्वाहारी, परजीवी)।\n3. अपघटक (Decomposers): मृत अवशेषों और अपशिष्ट उत्पादों (बैक्टीरिया, कवक) को तोड़कर मिट्टी में पोषक तत्वों को वापस लाते हैं।",
        "body_gu": "નિવસનતંત્ર (Ecosystem) એક સ્વ-ટકાઉ પ્રણાલી છે જ્યાં તમામ સજીવો (જૈવિક ઘટકો જેમ કે વનસ્પતિ, પ્રાણીઓ, બેક્ટેરિયા) એકબીજા સાથે અને તેમના નિર્જીવ પર્યાવરણ (અજૈવિક ઘટકો જેમ કે હવા, પાણી, જમીન, સૂર્યપ્રકાશ) સાથે આંતરક્રિયા કરે છે.\nસજીવોને તેઓ કેવી રીતે ખોરાક મેળવે છે તેના આધારે જૂથબદ્ધ કરવામાં આવે છે:\n1. ઉત્પાદકો (Producers): સૂર્યપ્રકાશનો ઉપયોગ કરીને પોતાનો ખોરાક જાતે બનાવે છે (લીલી વનસ્પતિઓ જેવા સ્વયંપોષીઓ).\n2. ઉપભોગીઓ (Consumers): અન્ય સજીવોને ખાય છે (તૃણાહારી, માંસાહારી, મિશ્રાહારી, પરોપજીવીઓ).\n3. વિઘટકો (Decomposers): મૃત અવશેષો અને નકામા ઉત્પાદનો (બેક્ટેરિયા, ફૂગ) નું વિઘટન કરે છે, પોષક તત્વોને જમીનમાં પરત કરે છે."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH13_003",
        "type": "theory",
        "title": "Food Chains and Food Webs",
        "title_hi": "खाद्य श्रृंखला और खाद्य जाल",
        "title_gu": "આહારશૃંખલા અને આહારજાળ",
        "body": "A Food Chain is a series of organisms in which one organism eats another. Each step forms a Trophic Level (e.g., Grass -> Deer -> Tiger).\nImportant Energy Rule: The 10% Law. When energy is passed from one trophic level to the next, only 10% of the energy is transferred. The rest is lost as heat. Because of this huge loss, food chains usually have only 3 or 4 steps.\nA Food Web is a network of many interconnected food chains, because most organisms eat more than one type of food.",
        "body_hi": "खाद्य श्रृंखला (Food Chain) जीवों की एक श्रृंखला है जिसमें एक जीव दूसरे को खाता है। प्रत्येक चरण एक पोषी स्तर (Trophic Level) बनाता है (जैसे, घास -> हिरण -> बाघ)।\nमहत्वपूर्ण ऊर्जा नियम: 10% का नियम। जब ऊर्जा एक पोषी स्तर से अगले स्तर पर जाती है, तो केवल 10% ऊर्जा ही स्थानांतरित होती है। बाकी गर्मी के रूप में खो जाती है। इस भारी नुकसान के कारण, खाद्य श्रृंखलाओं में आमतौर पर केवल 3 या 4 चरण होते हैं।\nखाद्य जाल (Food Web) कई आपस में जुड़ी खाद्य श्रृंखलाओं का एक नेटवर्क है, क्योंकि अधिकांश जीव एक से अधिक प्रकार का भोजन खाते हैं।",
        "body_gu": "આહારશૃંખલા (Food Chain) એ સજીવોની એક શ્રેણી છે જેમાં એક સજીવ બીજાને ખાય છે. દરેક પગથિયું એક પોષક સ્તર (Trophic Level) બનાવે છે (દા.ત., ઘાસ -> હરણ -> વાઘ).\nમહત્વપૂર્ણ ઉર્જાનો નિયમ: 10% નો નિયમ. જ્યારે ઉર્જા એક પોષક સ્તરમાંથી બીજા સ્તરમાં જાય છે, ત્યારે માત્ર 10% ઉર્જા જ વહન પામે છે. બાકીની ઉર્જા ઉષ્મા તરીકે વેડફાય છે. આ મોટા નુકસાનને કારણે, આહારશૃંખલામાં સામાન્ય રીતે માત્ર 3 અથવા 4 પગથિયાં હોય છે.\nઆહારજાળ (Food Web) એ ઘણી એકબીજા સાથે જોડાયેલી આહારશૃંખલાઓનું નેટવર્ક છે, કારણ કે મોટાભાગના સજીવો એક કરતાં વધુ પ્રકારનો ખોરાક ખાય છે."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH13_004",
        "type": "socratic_question",
        "title": "Biological Magnification",
        "title_hi": "जैविक आवर्धन (Biological Magnification)",
        "title_gu": "જૈવિક વિશાલન (Biological Magnification)",
        "question": "Farmers spray pesticides to kill insects. These chemicals enter the plants. The plants are eaten by insects, insects by frogs, frogs by snakes, and snakes by eagles. Who will have the highest amount of poisonous chemicals in their body?",
        "question_hi": "किसान कीड़ों को मारने के लिए कीटनाशकों (pesticides) का छिड़काव करते हैं। ये रसायन पौधों में प्रवेश करते हैं। पौधों को कीड़े खाते हैं, कीड़ों को मेंढक, मेंढकों को सांप और सांपों को चील खाते हैं। किसके शरीर में जहरीले रसायनों की मात्रा सबसे अधिक होगी?",
        "question_gu": "ખેડૂતો જંતુઓને મારવા માટે જંતુનાશકો (pesticides) નો છંટકાવ કરે છે. આ રસાયણો વનસ્પતિમાં પ્રવેશે છે. વનસ્પતિને જંતુઓ ખાય છે, જંતુઓને દેડકા, દેડકાને સાપ અને સાપને ગરુડ ખાય છે. કોના શરીરમાં ઝેરી રસાયણોનું પ્રમાણ સૌથી વધુ હશે?",
        "options": [
            "The Plants",
            "The Insects",
            "The Frogs",
            "The Eagles"
        ],
        "options_hi": [
            "पौधों में",
            "कीड़ों में",
            "मेंढकों में",
            "चीलों में"
        ],
        "options_gu": [
            "વનસ્પતિમાં",
            "જંતુઓમાં",
            "દેડકાઓમાં",
            "ગરુડમાં"
        ],
        "correct_index": 3,
        "explanation": "This is Biological Magnification! Toxic chemicals are not broken down by the body, so they accumulate. As you go higher up the food chain, the concentration of these harmful chemicals increases. The top predator (Eagle/Human) gets the maximum concentration of poison.",
        "explanation_hi": "यही जैविक आवर्धन (Biological Magnification) है! जहरीले रसायन शरीर द्वारा तोड़े नहीं जाते हैं, इसलिए वे जमा हो जाते हैं। जैसे-जैसे आप खाद्य श्रृंखला में ऊपर जाते हैं, इन हानिकारक रसायनों की सांद्रता (concentration) बढ़ती जाती है। शीर्ष शिकारी (चील/इंसान) को जहर की अधिकतम सांद्रता मिलती है।",
        "explanation_gu": "આ જ જૈવિક વિશાલન (Biological Magnification) છે! ઝેરી રસાયણો શરીર દ્વારા વિઘટન પામતા નથી, તેથી તે જમા થાય છે. જેમ તમે આહારશૃંખલામાં ઉપર જાઓ છો, તેમ આ હાનિકારક રસાયણોની સાંદ્રતા (concentration) વધે છે. ટોચના શિકારી (ગરુડ/માણસ) ને ઝેરની મહત્તમ સાંદ્રતા મળે છે."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH13_005",
        "type": "theory",
        "title": "Ozone Depletion and Garbage Management",
        "title_hi": "ओजोन क्षरण और कचरा प्रबंधन",
        "title_gu": "ઓઝોન સ્તરનું વિઘટન અને કચરાનું વ્યવસ્થાપન",
        "body": "Ozone (O3) is a deadly poison on the ground, but high up in the atmosphere, it forms a protective shield that blocks the sun's harmful Ultraviolet (UV) rays. UV rays can cause skin cancer. Synthetic chemicals like CFCs (Chlorofluorocarbons, used in old fridges) destroy the ozone layer.\nGarbage Management: We generate two types of waste:\n1. Biodegradable: Broken down by biological processes (bacteria/fungi). E.g., food waste, paper.\n2. Non-biodegradable: Cannot be broken down by nature. E.g., Plastics, glass, pesticides. These persist in the environment and cause severe pollution.",
        "body_hi": "ओजोन (O3) जमीन पर एक घातक जहर है, लेकिन वायुमंडल में बहुत ऊपर, यह एक सुरक्षा कवच बनाता है जो सूर्य की हानिकारक पराबैंगनी (UV) किरणों को रोकता है। UV किरणें त्वचा कैंसर का कारण बन सकती हैं। CFCs (क्लोरोफ्लोरोकार्बन, पुराने फ्रिज में प्रयुक्त) जैसे सिंथेटिक रसायन ओजोन परत को नष्ट कर देते हैं।\nकचरा प्रबंधन: हम दो प्रकार का कचरा उत्पन्न करते हैं:\n1. जैव-निम्नीकरणीय (Biodegradable): जैविक प्रक्रियाओं (बैक्टीरिया/कवक) द्वारा तोड़ा जा सकता है। जैसे, भोजन का कचरा, कागज।\n2. अजैव-निम्नीकरणीय (Non-biodegradable): प्रकृति द्वारा तोड़ा नहीं जा सकता। जैसे, प्लास्टिक, कांच, कीटनाशक। ये पर्यावरण में बने रहते हैं और गंभीर प्रदूषण का कारण बनते हैं।",
        "body_gu": "ઓઝોન (O3) જમીન પર એક ઘાતક ઝેર છે, પરંતુ વાતાવરણમાં ખૂબ ઊંચે, તે એક રક્ષણાત્મક કવચ બનાવે છે જે સૂર્યના હાનિકારક અલ્ટ્રાવાયોલેટ (UV) કિરણોને રોકે છે. UV કિરણો ત્વચાના કેન્સરનું કારણ બની શકે છે. CFCs (ક્લોરોફ્લોરોકાર્બન, જૂના ફ્રિજમાં વપરાતા) જેવા સિન્થેટિક રસાયણો ઓઝોન સ્તરનો નાશ કરે છે.\nકચરાનું વ્યવસ્થાપન: આપણે બે પ્રકારનો કચરો ઉત્પન્ન કરીએ છીએ:\n1. જૈવ-વિઘટનીય (Biodegradable): જૈવિક પ્રક્રિયાઓ (બેક્ટેરિયા/ફૂગ) દ્વારા વિઘટન થઈ શકે છે. દા.ત., ખોરાકનો કચરો, કાગળ.\n2. જૈવ-અવિઘટનીય (Non-biodegradable): પ્રકૃતિ દ્વારા વિઘટન થઈ શકતું નથી. દા.ત., પ્લાસ્ટિક, કાચ, જંતુનાશકો. તે પર્યાવરણમાં લાંબા સમય સુધી રહે છે અને ગંભીર પ્રદૂષણનું કારણ બને છે."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH13_006",
        "type": "mcq",
        "title": "NCERT Exercise Q1",
        "title_hi": "NCERT अभ्यास Q1",
        "title_gu": "NCERT સ્વાધ્યાય Q1",
        "question": "Which of the following groups contains only biodegradable items?",
        "question_hi": "निम्नलिखित में से किस समूह में केवल जैव-निम्नीकरणीय (biodegradable) वस्तुएं शामिल हैं?",
        "question_gu": "નીચેનામાંથી કયા જૂથમાં માત્ર જૈવ-વિઘટનીય (biodegradable) વસ્તુઓનો સમાવેશ થાય છે?",
        "options": [
            "Grass, wood and plastic",
            "Fruit-peels, cake and lime-juice",
            "Polythene bags, grass, flowers",
            "Cake, wood, and glass"
        ],
        "options_hi": [
            "घास, लकड़ी और प्लास्टिक",
            "फलों के छिलके, केक और नींबू का रस",
            "पॉलिथीन बैग, घास, फूल",
            "केक, लकड़ी, और कांच"
        ],
        "options_gu": [
            "ઘાસ, લાકડું અને પ્લાસ્ટિક",
            "ફળોની છાલ, કેક અને લીંબુનો રસ",
            "પોલિથીન બેગ, ઘાસ, ફૂલો",
            "કેક, લાકડું અને કાચ"
        ],
        "correct_index": 1,
        "explanation": "Biodegradable items are those that can be broken down naturally by microorganisms. Fruit-peels, cake, and lime-juice are all organic and can be decomposed. Plastic, polythene bags, and glass are non-biodegradable.",
        "explanation_hi": "जैव-निम्नीकरणीय (Biodegradable) वस्तुएं वे हैं जिन्हें सूक्ष्मजीवों द्वारा स्वाभाविक रूप से तोड़ा जा सकता है। फलों के छिलके, केक और नींबू का रस सभी कार्बनिक (organic) हैं और इन्हें विघटित किया जा सकता है। प्लास्टिक, पॉलिथीन बैग और कांच अजैव-निम्नीकरणीय हैं।",
        "explanation_gu": "જૈવ-વિઘટનીય વસ્તુઓ એ છે જે સૂક્ષ્મજીવો દ્વારા કુદરતી રીતે વિઘટન પામી શકે છે. ફળોની છાલ, કેક અને લીંબુનો રસ બધું જ કાર્બનિક છે અને તેનું વિઘટન થઈ શકે છે. પ્લાસ્ટિક, પોલિથીન બેગ અને કાચ જૈવ-અવિઘટનીય છે."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH13_007",
        "type": "mcq",
        "title": "NCERT Exercise Q2",
        "title_hi": "NCERT अभ्यास Q2",
        "title_gu": "NCERT સ્વાધ્યાય Q2",
        "question": "Which of the following constitutes a food-chain?",
        "question_hi": "निम्नलिखित में से कौन एक खाद्य श्रृंखला (food-chain) का निर्माण करता है?",
        "question_gu": "નીચેનામાંથી કયું આહારશૃંખલા (food-chain) ની રચના કરે છે?",
        "options": [
            "Grass, wheat and mango",
            "Grass, goat and human",
            "Goat, cow and elephant",
            "Grass, fish and goat"
        ],
        "options_hi": [
            "घास, गेहूं और आम",
            "घास, बकरी और इंसान",
            "बकरी, गाय और हाथी",
            "घास, मछली और बकरी"
        ],
        "options_gu": [
            "ઘાસ, ઘઉં અને કેરી",
            "ઘાસ, બકરી અને માણસ",
            "બકરી, ગાય અને હાથી",
            "ઘાસ, માછલી અને બકરી"
        ],
        "correct_index": 1,
        "explanation": "A food chain shows 'who eats whom'. Grass (Producer) is eaten by a Goat (Primary Consumer), which in turn can be eaten by a Human (Secondary Consumer). The other options do not show a correct eating sequence.",
        "explanation_hi": "खाद्य श्रृंखला दिखाती है कि 'कौन किसको खाता है'। घास (उत्पादक) को एक बकरी (प्राथमिक उपभोक्ता) द्वारा खाया जाता है, जिसे बदले में इंसान (द्वितीयक उपभोक्ता) द्वारा खाया जा सकता है। अन्य विकल्प सही खाने का क्रम नहीं दिखाते हैं।",
        "explanation_gu": "આહારશૃંખલા દર્શાવે છે કે 'કોણ કોને ખાય છે'. ઘાસ (ઉત્પાદક) ને બકરી (પ્રાથમિક ઉપભોગી) દ્વારા ખાવામાં આવે છે, જે બદલામાં માણસ (દ્વિતીય ઉપભોગી) દ્વારા ખાઈ શકાય છે. અન્ય વિકલ્પો ખાવાનો સાચો ક્રમ દર્શાવતા નથી."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH13_008",
        "type": "mcq",
        "title": "NCERT Exercise Q3",
        "title_hi": "NCERT अभ्यास Q3",
        "title_gu": "NCERT સ્વાધ્યાય Q3",
        "question": "Which of the following are environment-friendly practices?",
        "question_hi": "निम्नलिखित में से कौन पर्यावरण के अनुकूल (environment-friendly) प्रथाएं हैं?",
        "question_gu": "નીચેનામાંથી કઈ પર્યાવરણને અનુકૂળ (environment-friendly) પદ્ધતિઓ છે?",
        "options": [
            "Carrying cloth-bags to put purchases in while shopping",
            "Switching off unnecessary lights and fans",
            "Walking to school instead of using a vehicle",
            "All of the above"
        ],
        "options_hi": [
            "खरीदारी करते समय सामान रखने के लिए कपड़े के बैग ले जाना",
            "अनावश्यक लाइट और पंखे बंद करना",
            "वाहन का उपयोग करने के बजाय स्कूल पैदल जाना",
            "उपर्युक्त सभी"
        ],
        "options_gu": [
            "ખરીદી કરતી વખતે સામાન મૂકવા માટે કાપડની થેલીઓ સાથે લઈ જવી",
            "બિનજરૂરી લાઇટ અને પંખા બંધ કરવા",
            "વાહનનો ઉપયોગ કરવાને બદલે શાળાએ ચાલીને જવું",
            "ઉપરના તમામ"
        ],
        "correct_index": 3,
        "explanation": "All these practices reduce pollution, save electricity (which reduces coal burning), and limit the use of harmful plastics, making them highly eco-friendly.",
        "explanation_hi": "ये सभी प्रथाएं प्रदूषण को कम करती हैं, बिजली बचाती हैं (जिससे कोयला जलना कम होता है), और हानिकारक प्लास्टिक के उपयोग को सीमित करती हैं, जिससे वे अत्यधिक पर्यावरण के अनुकूल हो जाती हैं।",
        "explanation_gu": "આ તમામ પદ્ધતિઓ પ્રદૂષણ ઘટાડે છે, વીજળી બચાવે છે (જે કોલસાનું દહન ઘટાડે છે), અને હાનિકારક પ્લાસ્ટિકનો ઉપયોગ મર્યાદિત કરે છે, જે તેમને પર્યાવરણ માટે ખૂબ અનુકૂળ બનાવે છે."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH13_009",
        "type": "mcq",
        "title": "NCERT Exercise Q4",
        "title_hi": "NCERT अभ्यास Q4",
        "title_gu": "NCERT સ્વાધ્યાય Q4",
        "question": "What would happen if we kill all the organisms in one trophic level of a food chain?",
        "question_hi": "यदि हम खाद्य श्रृंखला के एक पोषी स्तर (trophic level) के सभी जीवों को मार दें तो क्या होगा?",
        "question_gu": "જો આપણે આહારશૃંખલાના એક પોષક સ્તર (trophic level) ના તમામ સજીવોને મારી નાખીએ તો શું થશે?",
        "options": [
            "Only that specific trophic level will be affected.",
            "The organisms in the next higher trophic level will thrive and multiply rapidly.",
            "The population of the previous trophic level will increase, while the next trophic level will starve and die out.",
            "The ecosystem will quickly adapt and create a new organism to replace them."
        ],
        "options_hi": [
            "केवल वह विशिष्ट पोषी स्तर प्रभावित होगा।",
            "अगले उच्च पोषी स्तर के जीव पनपेंगे और तेजी से बढ़ेंगे।",
            "पिछले पोषी स्तर की आबादी बढ़ जाएगी, जबकि अगले पोषी स्तर के जीव भूखे मर जाएंगे।",
            "पारिस्थितिक तंत्र जल्दी से अनुकूल हो जाएगा और उन्हें बदलने के लिए एक नया जीव बनाएगा।"
        ],
        "options_gu": [
            "માત્ર તે ચોક્કસ પોષક સ્તર જ પ્રભાવિત થશે.",
            "આગળના ઉચ્ચ પોષક સ્તરના સજીવો ખીલશે અને ઝડપથી વધશે.",
            "અગાઉના પોષક સ્તરની વસ્તી વધશે, જ્યારે આગળના પોષક સ્તરના સજીવો ભૂખે મરી જશે.",
            "નિવસનતંત્ર ઝડપથી અનુકૂળ થઈ જશે અને તેમને બદલવા માટે નવો સજીવ બનાવશે."
        ],
        "correct_index": 2,
        "explanation": "If a trophic level is removed, the balance is destroyed. The level below it will overpopulate (because their predators are gone), destroying their food source. The level above it will starve to death because they have no food.",
        "explanation_hi": "यदि एक पोषी स्तर हटा दिया जाता है, तो संतुलन नष्ट हो जाता है। इसके नीचे का स्तर अधिक आबादी वाला हो जाएगा (क्योंकि उनके शिकारी चले गए हैं), जिससे उनके भोजन का स्रोत नष्ट हो जाएगा। इसके ऊपर का स्तर भूख से मर जाएगा क्योंकि उनके पास भोजन नहीं है।",
        "explanation_gu": "જો પોષક સ્તર દૂર કરવામાં આવે, તો સંતુલન નાશ પામે છે. તેની નીચેનું સ્તર વધુ વસ્તીવાળું બનશે (કારણ કે તેમના શિકારીઓ ગયા છે), જેનાથી તેમના ખોરાકનો સ્ત્રોત નાશ પામશે. તેની ઉપરનું સ્તર ભૂખે મરી જશે કારણ કે તેમની પાસે ખોરાક નથી."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH13_010",
        "type": "mcq",
        "title": "NCERT Exercise Q9",
        "title_hi": "NCERT अभ्यास Q9",
        "title_gu": "NCERT સ્વાધ્યાય Q9",
        "question": "Why is the depletion of the ozone layer a major cause for global concern?",
        "question_hi": "ओजोन परत का क्षरण वैश्विक चिंता का एक प्रमुख कारण क्यों है?",
        "question_gu": "ઓઝોન સ્તરનું વિઘટન એ વૈશ્વિક ચિંતાનું મુખ્ય કારણ શા માટે છે?",
        "options": [
            "Because it allows harmful UV radiation from the sun to reach the Earth, causing skin cancer.",
            "Because it blocks sunlight and makes the Earth colder.",
            "Because it increases the oxygen levels in the air, causing forest fires.",
            "Because it stops the water cycle."
        ],
        "options_hi": [
            "क्योंकि यह सूर्य से हानिकारक UV विकिरण को पृथ्वी तक पहुंचने देता है, जिससे त्वचा कैंसर होता है।",
            "क्योंकि यह सूरज की रोशनी को रोकता है और पृथ्वी को ठंडा बनाता है।",
            "क्योंकि यह हवा में ऑक्सीजन के स्तर को बढ़ाता है, जिससे जंगल में आग लग जाती है।",
            "क्योंकि यह जल चक्र को रोकता है।"
        ],
        "options_gu": [
            "કારણ કે તે સૂર્યના હાનિકારક UV કિરણોને પૃથ્વી સુધી પહોંચવા દે છે, જેનાથી ત્વચાનું કેન્સર થાય છે.",
            "કારણ કે તે સૂર્યપ્રકાશને રોકે છે અને પૃથ્વીને ઠંડી બનાવે છે.",
            "કારણ કે તે હવામાં ઓક્સિજનનું સ્તર વધારે છે, જેનાથી જંગલમાં આગ લાગે છે.",
            "કારણ કે તે જળચક્રને અટકાવે છે."
        ],
        "correct_index": 0,
        "explanation": "The ozone shield protects us from harmful Ultraviolet (UV) radiation. Without it, UV rays would severely damage humans (skin cancer, cataracts) and also harm plants and marine ecosystems.",
        "explanation_hi": "ओजोन कवच हमें हानिकारक पराबैंगनी (UV) विकिरण से बचाता है। इसके बिना, UV किरणें मनुष्यों (त्वचा कैंसर, मोतियाबिंद) को गंभीर रूप से नुकसान पहुंचाएंगी और पौधों और समुद्री पारिस्थितिक तंत्र को भी नुकसान पहुंचाएंगी।",
        "explanation_gu": "ઓઝોન કવચ આપણને હાનિકારક અલ્ટ્રાવાયોલેટ (UV) કિરણોથી બચાવે છે. તેના વિના, UV કિરણો મનુષ્યોને (ત્વચાનું કેન્સર, મોતિયો) ગંભીર નુકસાન પહોંચાડશે અને વનસ્પતિઓ અને દરિયાઈ નિવસનતંત્રને પણ નુકસાન પહોંચાડશે."
    }
]

data = {
    "metadata": {
        "id": "ncert_class10_science_ch13",
        "title": "Chapter 13: Our Environment",
        "subject": "Science",
        "grade": "10"
    },
    "blocks": blocks
}

output_path = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_science_ch13.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Successfully wrote {len(blocks)} blocks to {output_path}")
