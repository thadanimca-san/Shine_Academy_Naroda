import json

blocks = [
    {
        "id": "KOBJ_NCERT_C10_GEOG_CH5_001",
        "type": "hook",
        "title": "A World Made of Minerals",
        "title_hi": "खनिजों से बनी दुनिया",
        "title_gu": "ખનિજોની બનેલી દુનિયા",
        "body": "Look around you. The bus you ride in, the building you live in, the screen you are reading this on, and even the tiny pin on your desk—everything is made from minerals extracted from the earth. In fact, even the food we eat contains minerals! Almost 99% of our daily needs are met by things that are either minerals or manufactured from minerals. But what exactly are minerals, where are they hidden, and what happens when we use them all up?",
        "body_hi": "अपने चारों ओर देखिए। जिस बस में आप यात्रा करते हैं, जिस इमारत में आप रहते हैं, जिस स्क्रीन पर आप इसे पढ़ रहे हैं, और यहां तक ​​कि आपकी डेस्क पर छोटी पिन—सब कुछ पृथ्वी से निकाले गए खनिजों (minerals) से बना है। वास्तव में, हम जो भोजन खाते हैं उसमें भी खनिज होते हैं! हमारी रोजमर्रा की लगभग 99% ज़रूरतें उन चीज़ों से पूरी होती हैं जो या तो खनिज हैं या खनिजों से निर्मित हैं। लेकिन वास्तव में खनिज क्या हैं, वे कहाँ छिपे हैं, और जब हम उन सभी का उपयोग कर लेंगे तो क्या होगा?",
        "body_gu": "તમારી આસપાસ જુઓ. તમે જે બસમાં મુસાફરી કરો છો, જે ઇમારતમાં તમે રહો છો, જે સ્ક્રીન પર તમે આ વાંચી રહ્યા છો, અને તમારા ડેસ્ક પરની નાની પિન પણ - બધું જ પૃથ્વીમાંથી કાઢવામાં આવેલા ખનિજોમાંથી (minerals) બનેલું છે. વાસ્તવમાં, આપણે જે ખોરાક ખાઈએ છીએ તેમાં પણ ખનિજો હોય છે! આપણી દૈનિક જરૂરિયાતોના લગભગ 99% એવા વસ્તુઓ દ્વારા પૂરી થાય છે જે કાં તો ખનિજો છે અથવા ખનિજોમાંથી બનેલી છે. પરંતુ ખનિજો બરાબર શું છે, તે ક્યાં છુપાયેલા છે, અને જ્યારે આપણે તેનો બધો જ ઉપયોગ કરી લઈશું ત્યારે શું થશે?"
    },
    {
        "id": "KOBJ_NCERT_C10_GEOG_CH5_002",
        "type": "theory",
        "title": "What is a Mineral?",
        "title_hi": "खनिज क्या है?",
        "title_gu": "ખનિજ શું છે?",
        "body": "Geologists define a mineral as a 'homogenous, naturally occurring substance with a definable internal structure'.\nMinerals are found in varied forms in nature, ranging from the hardest diamond to the softest talc.\nMinerals are usually found in 'ores'. The term ore is used to describe an accumulation of any mineral mixed with other elements. The concentration of the mineral in the ore must be sufficient to make its extraction commercially viable.",
        "body_hi": "भूवैज्ञानिक खनिज को 'एक परिभाषित आंतरिक संरचना के साथ एक सजातीय, प्राकृतिक रूप से पाए जाने वाले पदार्थ' के रूप में परिभाषित करते हैं।\nखनिज प्रकृति में विभिन्न रूपों में पाए जाते हैं, सबसे कठोर हीरे से लेकर सबसे नरम टैल्क (talc) तक।\nखनिज आमतौर पर 'अयस्कों' (ores) में पाए जाते हैं। अयस्क शब्द का प्रयोग अन्य तत्वों के साथ मिश्रित किसी भी खनिज के संचय (accumulation) का वर्णन करने के लिए किया जाता है। अयस्क में खनिज की सांद्रता (concentration) इतनी होनी चाहिए कि इसका निष्कर्षण (extraction) व्यावसायिक रूप से व्यवहार्य (viable) हो सके।",
        "body_gu": "ભૂસ્તરશાસ્ત્રીઓ ખનિજને 'વ્યાખ્યાયિત આંતરિક માળખા સાથે સમાન, કુદરતી રીતે બનતા પદાર્થ' તરીકે વ્યાખ્યાયિત કરે છે.\nખનિજો પ્રકૃતિમાં વિવિધ સ્વરૂપોમાં જોવા મળે છે, સૌથી સખત હીરાથી લઈને સૌથી નરમ ટેલ્ક (talc) સુધી.\nખનિજો સામાન્ય રીતે 'કાચી ધાતુઓ' (ores) માં જોવા મળે છે. ઓર (કાચી ધાતુ) શબ્દનો ઉપયોગ અન્ય તત્વો સાથે મિશ્રિત કોઈપણ ખનિજના સંચયનું વર્ણન કરવા માટે થાય છે. કાચી ધાતુમાં ખનિજની સાંદ્રતા એટલી હોવી જોઈએ કે તેનું નિષ્કર્ષણ (કાઢવું) વ્યવસાયિક રીતે સક્ષમ બને."
    },
    {
        "id": "KOBJ_NCERT_C10_GEOG_CH5_003",
        "type": "socratic_question",
        "title": "Mode of Occurrence of Minerals",
        "title_hi": "खनिजों के पाए जाने का तरीका",
        "title_gu": "ખનિજોની પ્રાપ્તિના સ્થાનો",
        "question": "Minerals are found in different types of rocks. Coal and some forms of iron ore are formed by accumulation and concentration in horizontal layers. In which type of rock do you think these layer-by-layer minerals are found?",
        "question_hi": "खनिज विभिन्न प्रकार की चट्टानों में पाए जाते हैं। कोयला और लौह अयस्क के कुछ रूप क्षैतिज परतों (horizontal layers) में संचय और सांद्रता (concentration) से बनते हैं। आपको क्या लगता है कि परत-दर-परत वाले ये खनिज किस प्रकार की चट्टान में पाए जाते हैं?",
        "question_gu": "ખનિજો વિવિધ પ્રકારના ખડકોમાં જોવા મળે છે. કોલસો અને લોખંડની કેટલીક કાચી ધાતુ આડી થરોમાં (horizontal layers) સંચય અને સાંદ્રતા દ્વારા રચાય છે. તમને શું લાગે છે કે થર-દર-થર બનતા આ ખનિજો કયા પ્રકારના ખડકોમાં જોવા મળે છે?",
        "options": [
            "Igneous Rocks",
            "Sedimentary Rocks",
            "Metamorphic Rocks",
            "Volcanic Rocks"
        ],
        "options_hi": [
            "आग्नेय चट्टानें (Igneous Rocks)",
            "अवसादी चट्टानें (Sedimentary Rocks)",
            "कायांतरित चट्टानें (Metamorphic Rocks)",
            "ज्वालामुखीय चट्टानें"
        ],
        "options_gu": [
            "અગ્નિકૃત ખડકો (Igneous Rocks)",
            "પ્રસ્તર ખડકો (Sedimentary Rocks)",
            "રૂપાંતરિત ખડકો (Metamorphic Rocks)",
            "જ્વાળામુખી ખડકો"
        ],
        "correct_index": 1,
        "explanation": "In sedimentary rocks, a number of minerals occur in beds or layers. They have been formed as a result of deposition, accumulation, and concentration in horizontal strata. Coal and some forms of iron ore have been concentrated as a result of long periods under great heat and pressure.",
        "explanation_hi": "अवसादी चट्टानों (sedimentary rocks) में, कई खनिज बिस्तरों या परतों में पाए जाते हैं। उनका निर्माण क्षैतिज स्तरों में निक्षेपण, संचय और सांद्रता के परिणामस्वरूप हुआ है। अत्यधिक गर्मी और दबाव में लंबे समय तक रहने के परिणामस्वरूप कोयला और लौह अयस्क के कुछ रूप संकेंद्रित हुए हैं।",
        "explanation_gu": "પ્રસ્તર ખડકોમાં (sedimentary rocks), સંખ્યાબંધ ખનિજો પથારી અથવા થરોમાં જોવા મળે છે. તેઓ આડા સ્તરોમાં જમાવટ, સંચય અને સાંદ્રતાના પરિણામે રચાયા છે. ભારે ગરમી અને દબાણ હેઠળ લાંબા સમયના પરિણામે કોલસો અને લોખંડના કેટલાક સ્વરૂપો કેન્દ્રિત થયા છે."
    },
    {
        "id": "KOBJ_NCERT_C10_GEOG_CH5_004",
        "type": "theory",
        "title": "Classification of Minerals",
        "title_hi": "खनिजों का वर्गीकरण",
        "title_gu": "ખનિજોનું વર્ગીકરણ",
        "body": "1. Metallic Minerals: These contain metals.\n  a) Ferrous Minerals: Contain iron (e.g., Iron ore, Manganese). They account for about three-fourths of the total value of metallic minerals produced in India.\n  b) Non-Ferrous Minerals: Do not contain iron (e.g., Copper, Bauxite, Lead, Zinc). India's reserves and production of these are not very satisfactory.\n2. Non-Metallic Minerals: Do not contain metals (e.g., Mica, Salt, Potash, Limestone, Marble).\n3. Energy Minerals: Used for generating energy (e.g., Coal, Petroleum, Natural Gas).",
        "body_hi": "1. धात्विक खनिज (Metallic Minerals): इनमें धातुएँ होती हैं।\n  a) लौह खनिज (Ferrous Minerals): इनमें लोहा होता है (जैसे, लौह अयस्क, मैंगनीज)। वे भारत में उत्पादित धात्विक खनिजों के कुल मूल्य का लगभग तीन-चौथाई हिस्सा बनाते हैं।\n  b) अलौह खनिज (Non-Ferrous Minerals): इनमें लोहा नहीं होता है (जैसे, तांबा, बॉक्साइट, सीसा, जस्ता)। भारत में इनके भंडार और उत्पादन बहुत संतोषजनक नहीं हैं।\n2. अधात्विक खनिज (Non-Metallic Minerals): इनमें धातु नहीं होती है (जैसे, अभ्रक (Mica), नमक, पोटाश, चूना पत्थर, संगमरमर)।\n3. ऊर्जा खनिज: ऊर्जा पैदा करने के लिए उपयोग किया जाता है (जैसे, कोयला, पेट्रोलियम, प्राकृतिक गैस)।",
        "body_gu": "1. ધાતુમય ખનિજો (Metallic Minerals): આમાં ધાતુઓ હોય છે.\n  a) લોહ ખનિજો (Ferrous Minerals): તેમાં લોખંડ હોય છે (દા.ત., લોખંડની કાચી ધાતુ, મેંગેનીઝ). તેઓ ભારતમાં ઉત્પાદિત ધાતુના ખનિજોના કુલ મૂલ્યમાં લગભગ ત્રણ ચતુર્થાંશ હિસ્સો ધરાવે છે.\n  b) અલોહ ખનિજો (Non-Ferrous Minerals): તેમાં લોખંડ હોતું નથી (દા.ત., તાંબુ, બોક્સાઈટ, સીસું, જસત). ભારતમાં તેમની અનામત અને ઉત્પાદન બહુ સંતોષકારક નથી.\n2. અધાતુમય ખનિજો (Non-Metallic Minerals): ધાતુઓ ધરાવતા નથી (દા.ત., અબરખ (Mica), મીઠું, પોટાશ, ચૂનાનો પત્થર, આરસ).\n3. ઊર્જા ખનિજો: ઊર્જા ઉત્પન્ન કરવા માટે વપરાય છે (દા.ત., કોલસો, પેટ્રોલિયમ, કુદરતી ગેસ)."
    },
    {
        "id": "KOBJ_NCERT_C10_GEOG_CH5_005",
        "type": "theory",
        "title": "Energy Resources",
        "title_hi": "ऊर्जा संसाधन",
        "title_gu": "ઊર્જા સંસાધનો",
        "body": "Energy can be generated from fuel minerals like coal, petroleum, natural gas, uranium, and from electricity. Energy resources are classified as:\n1. Conventional Sources: These have been in use for a long time and are mostly non-renewable (e.g., firewood, cattle dung cake, coal, petroleum, natural gas and electricity).\n- Coal is the most abundantly available fossil fuel in India. It is used for power generation and supplying energy to industry.\n2. Non-Conventional Sources: These are renewable sources of energy and are gaining importance due to growing environmental concerns (e.g., solar, wind, tidal, geothermal, biogas and atomic energy).\n- India is blessed with an abundance of sunlight, water, wind and biomass.",
        "body_hi": "ऊर्जा ईंधन खनिजों जैसे कोयला, पेट्रोलियम, प्राकृतिक गैस, यूरेनियम और बिजली से उत्पन्न की जा सकती है। ऊर्जा संसाधनों को इस प्रकार वर्गीकृत किया गया है:\n1. पारंपरिक स्रोत (Conventional Sources): ये लंबे समय से उपयोग में हैं और ज्यादातर गैर-नवीकरणीय (non-renewable) हैं (जैसे, जलाऊ लकड़ी, उपले, कोयला, पेट्रोलियम, प्राकृतिक गैस और बिजली)।\n- कोयला भारत में सबसे प्रचुर मात्रा में उपलब्ध जीवाश्म ईंधन (fossil fuel) है। इसका उपयोग बिजली उत्पादन और उद्योग को ऊर्जा की आपूर्ति के लिए किया जाता है।\n2. गैर-पारंपरिक स्रोत (Non-Conventional Sources): ये ऊर्जा के नवीकरणीय स्रोत हैं और बढ़ती पर्यावरणीय चिंताओं के कारण महत्व प्राप्त कर रहे हैं (जैसे, सौर, पवन, ज्वारीय, भूतापीय, बायोगैस और परमाणु ऊर्जा)।\n- भारत में सूरज की रोशनी, पानी, हवा और बायोमास की प्रचुरता है।",
        "body_gu": "કોલસો, પેટ્રોલિયમ, કુદરતી ગેસ, યુરેનિયમ અને વીજળી જેવા બળતણ ખનિજોમાંથી ઊર્જા ઉત્પન્ન કરી શકાય છે. ઊર્જા સંસાધનોને નીચે મુજબ વર્ગીકૃત કરવામાં આવ્યા છે:\n1. પરંપરાગત સ્ત્રોતો (Conventional Sources): આનો ઉપયોગ લાંબા સમયથી થઈ રહ્યો છે અને મોટાભાગે બિન-પુનઃપ્રાપ્ય છે (દા.ત., બળતણનું લાકડું, છાણાં, કોલસો, પેટ્રોલિયમ, કુદરતી ગેસ અને વીજળી).\n- કોલસો એ ભારતમાં સૌથી વધુ વિપુલ પ્રમાણમાં ઉપલબ્ધ અશ્મિભૂત બળતણ (fossil fuel) છે. તેનો ઉપયોગ વીજ ઉત્પાદન અને ઉદ્યોગને ઉર્જા પૂરી પાડવા માટે થાય છે.\n2. બિન-પરંપરાગત સ્ત્રોતો (Non-Conventional Sources): આ ઉર્જાના પુનઃપ્રાપ્ય સ્ત્રોતો છે અને વધતી જતી પર્યાવરણીય ચિંતાઓને કારણે મહત્વ મેળવી રહ્યા છે (દા.ત., સૌર, પવન, ભરતી, ભૂઉષ્મીય, બાયોગેસ અને અણુ ઊર્જા).\n- ભારતમાં સૂર્યપ્રકાશ, પાણી, પવન અને બાયોમાસની વિપુલતા છે."
    },
    {
        "id": "KOBJ_NCERT_C10_GEOG_CH5_006",
        "type": "mcq",
        "title": "NCERT Exercise Q1_i",
        "title_hi": "NCERT अभ्यास Q1_i",
        "title_gu": "NCERT સ્વાધ્યાય Q1_i",
        "question": "Which of the following minerals is formed by decomposition of rocks, leaving a residual mass of weathered material?",
        "question_hi": "निम्नलिखित में से कौन सा खनिज चट्टानों के अपघटन (decomposition) से बनता है, जिससे अपक्षयित सामग्री (weathered material) का अवशिष्ट द्रव्यमान (residual mass) रह जाता है?",
        "question_gu": "નીચેનામાંથી કયું ખનિજ ખડકોના વિઘટનથી (decomposition) રચાય છે, જે ઘસાયેલી સામગ્રીનો (weathered material) શેષ જથ્થો છોડી દે છે?",
        "options": [
            "Coal",
            "Bauxite",
            "Gold",
            "Zinc"
        ],
        "options_hi": [
            "कोयला",
            "बॉक्साइट",
            "सोना",
            "जस्ता"
        ],
        "options_gu": [
            "કોલસો",
            "બોક્સાઈટ",
            "સોનું",
            "જસત"
        ],
        "correct_index": 1,
        "explanation": "Bauxite is formed by the decomposition of a wide variety of rocks rich in aluminium silicates. When the soluble constituents are removed by weathering, a residual mass of weathered material containing bauxite is left behind.",
        "explanation_hi": "बॉक्साइट का निर्माण एल्यूमीनियम सिलिकेट से भरपूर विभिन्न प्रकार की चट्टानों के अपघटन से होता है। जब अपक्षय (weathering) द्वारा घुलनशील घटकों को हटा दिया जाता है, तो बॉक्साइट युक्त अपक्षयित सामग्री का एक अवशिष्ट द्रव्यमान पीछे रह जाता है।",
        "explanation_gu": "બોક્સાઈટ એ એલ્યુમિનિયમ સિલિકેટ્સથી સમૃદ્ધ ખડકોના વિઘટનથી રચાય છે. જ્યારે દ્રાવ્ય ઘટકોને ઘસારા દ્વારા દૂર કરવામાં આવે છે, ત્યારે બોક્સાઇટ ધરાવતી ઘસાયેલી સામગ્રીનો શેષ જથ્થો પાછળ રહી જાય છે."
    },
    {
        "id": "KOBJ_NCERT_C10_GEOG_CH5_007",
        "type": "mcq",
        "title": "NCERT Exercise Q1_ii",
        "title_hi": "NCERT अभ्यास Q1_ii",
        "title_gu": "NCERT સ્વાધ્યાય Q1_ii",
        "question": "Koderma, in Jharkhand, is the leading producer of which one of the following minerals?",
        "question_hi": "झारखंड में कोडरमा (Koderma), निम्नलिखित में से किस खनिज का प्रमुख उत्पादक है?",
        "question_gu": "ઝારખંડમાં કોડરમા, નીચેનામાંથી કયા ખનિજનું અગ્રણી ઉત્પાદક છે?",
        "options": [
            "Bauxite",
            "Mica",
            "Iron Ore",
            "Copper"
        ],
        "options_hi": [
            "बॉक्साइट",
            "अभ्रक (Mica)",
            "लौह अयस्क",
            "तांबा"
        ],
        "options_gu": [
            "બોક્સાઈટ",
            "અબરખ (Mica)",
            "લોખંડની કાચી ધાતુ",
            "તાંબુ"
        ],
        "correct_index": 1,
        "explanation": "Koderma-Gaya-Hazaribagh belt of Jharkhand is the leading producer of Mica in India. Mica is widely used in the electric and electronic industries.",
        "explanation_hi": "झारखंड का कोडरमा-गया-हजारीबाग बेल्ट भारत में अभ्रक (Mica) का प्रमुख उत्पादक है। अभ्रक का व्यापक रूप से इलेक्ट्रिक और इलेक्ट्रॉनिक उद्योगों में उपयोग किया जाता है।",
        "explanation_gu": "ઝારખંડનો કોડરમા-ગયા-હઝારીબાગ પટ્ટો ભારતમાં અબરખનો (Mica) અગ્રણી ઉત્પાદક છે. અબરખનો ઈલેક્ટ્રિક અને ઈલેક્ટ્રોનિક ઉદ્યોગોમાં વ્યાપકપણે ઉપયોગ થાય છે."
    },
    {
        "id": "KOBJ_NCERT_C10_GEOG_CH5_008",
        "type": "mcq",
        "title": "NCERT Exercise Q1_iii",
        "title_hi": "NCERT अभ्यास Q1_iii",
        "title_gu": "NCERT સ્વાધ્યાય Q1_iii",
        "question": "Minerals are deposited and accumulated in the stratas of which of the following rocks?",
        "question_hi": "खनिज निम्नलिखित में से किस चट्टान के स्तरों (stratas) में जमा और संचित होते हैं?",
        "question_gu": "ખનિજો નીચેનામાંથી કયા ખડકના સ્તરોમાં (stratas) જમા અને એકઠા થાય છે?",
        "options": [
            "Sedimentary rocks",
            "Metamorphic rocks",
            "Igneous rocks",
            "None of the above"
        ],
        "options_hi": [
            "अवसादी चट्टानें (Sedimentary rocks)",
            "कायांतरित चट्टानें (Metamorphic rocks)",
            "आग्नेय चट्टानें (Igneous rocks)",
            "इनमे से कोई भी नहीं"
        ],
        "options_gu": [
            "પ્રસ્તર ખડકો (Sedimentary rocks)",
            "રૂપાંતરિત ખડકો (Metamorphic rocks)",
            "અગ્નિકૃત ખડકો (Igneous rocks)",
            "ઉપરનામાંથી કોઈ નહિ"
        ],
        "correct_index": 0,
        "explanation": "In sedimentary rocks, a number of minerals (like coal and some forms of iron ore) occur in beds or layers (stratas). They have been formed as a result of deposition, accumulation and concentration in horizontal stratas.",
        "explanation_hi": "अवसादी चट्टानों (sedimentary rocks) में, कई खनिज (जैसे कोयला और लौह अयस्क के कुछ रूप) बिस्तरों या परतों (stratas) में पाए जाते हैं। वे क्षैतिज स्तरों में निक्षेपण, संचय और सांद्रता के परिणामस्वरूप बने हैं।",
        "explanation_gu": "પ્રસ્તર ખડકોમાં (sedimentary rocks), સંખ્યાબંધ ખનિજો (જેમ કે કોલસો અને લોખંડના કેટલાક સ્વરૂપો) પથારી અથવા સ્તરોમાં (stratas) જોવા મળે છે. તેઓ આડા સ્તરોમાં જમાવટ, સંચય અને સાંદ્રતાના પરિણામે રચાયા છે."
    },
    {
        "id": "KOBJ_NCERT_C10_GEOG_CH5_009",
        "type": "mcq",
        "title": "NCERT Exercise Q1_iv",
        "title_hi": "NCERT अभ्यास Q1_iv",
        "title_gu": "NCERT સ્વાધ્યાય Q1_iv",
        "question": "Which one of the following minerals is contained in the Monazite sand?",
        "question_hi": "मोनाज़ाइट रेत (Monazite sand) में निम्नलिखित में से कौन सा खनिज होता है?",
        "question_gu": "મોનાઝાઇટ રેતીમાં નીચેનામાંથી કયું ખનિજ હોય છે?",
        "options": [
            "Oil",
            "Uranium",
            "Thorium",
            "Coal"
        ],
        "options_hi": [
            "तेल",
            "यूरेनियम",
            "थोरियम (Thorium)",
            "कोयला"
        ],
        "options_gu": [
            "તેલ",
            "યુરેનિયમ",
            "થોરિયમ (Thorium)",
            "કોલસો"
        ],
        "correct_index": 2,
        "explanation": "Uranium and Thorium are used for generating atomic or nuclear power. The Monazite sands of Kerala are rich in Thorium.",
        "explanation_hi": "यूरेनियम और थोरियम का उपयोग परमाणु या नाभिकीय ऊर्जा (nuclear power) उत्पन्न करने के लिए किया जाता है। केरल की मोनाजाइट रेत में थोरियम प्रचुर मात्रा में पाया जाता है।",
        "explanation_gu": "યુરેનિયમ અને થોરિયમનો ઉપયોગ અણુ અથવા પરમાણુ ઊર્જા પેદા કરવા માટે થાય છે. કેરળની મોનાઝાઇટ રેતીમાં થોરિયમ ભરપૂર માત્રામાં છે."
    }
]

data = {
    "metadata": {
        "id": "ncert_class10_geography_ch5",
        "title": "Geography Chapter 5: Minerals and Energy Resources",
        "subject": "Social Science",
        "grade": "10"
    },
    "blocks": blocks
}

output_path = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_geography_ch5.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Successfully wrote {len(blocks)} blocks to {output_path}")
