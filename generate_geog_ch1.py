import json

blocks = [
    {
        "id": "KOBJ_NCERT_C10_GEOG_CH1_001",
        "type": "hook",
        "title": "What Makes the Earth Valuable?",
        "title_hi": "पृथ्वी को क्या मूल्यवान बनाता है?",
        "title_gu": "પૃથ્વીને શું મૂલ્યવાન બનાવે છે?",
        "body": "Look at the things around you: the water you drink, the air you breathe, the metals in your smartphone, the soil that grows your food. Everything available in our environment which can be used to satisfy our needs, provided it is technologically accessible, economically feasible and culturally acceptable, is termed as a 'Resource'. But what if we run out of these? Can human beings survive if the earth loses its soil, forests, and clean water? Let's explore how we use and sometimes misuse the gifts of nature.",
        "body_hi": "अपने आस-पास की चीजों को देखें: वह पानी जो आप पीते हैं, वह हवा जिसमें आप सांस लेते हैं, आपके स्मार्टफोन में धातुएँ, वह मिट्टी जो आपका भोजन उगाती है। हमारे पर्यावरण में उपलब्ध हर चीज जिसका उपयोग हमारी आवश्यकताओं को पूरा करने के लिए किया जा सकता है, बशर्ते वह तकनीकी रूप से सुलभ, आर्थिक रूप से व्यवहार्य और सांस्कृतिक रूप से स्वीकार्य हो, 'संसाधन' (Resource) कहलाती है। लेकिन क्या होगा अगर हम इन्हें खत्म कर दें? क्या इंसान तब जीवित रह सकता है जब पृथ्वी अपनी मिट्टी, जंगल और साफ पानी खो दे? आइए देखें कि हम प्रकृति के उपहारों का उपयोग और कभी-कभी दुरुपयोग कैसे करते हैं।",
        "body_gu": "તમારી આસપાસની વસ્તુઓ જુઓ: તમે પીઓ છો તે પાણી, તમે જે હવા શ્વાસમાં લો છો, તમારા સ્માર્ટફોનમાં રહેલી ધાતુઓ, તમારો ખોરાક ઉગાડતી જમીન. આપણા પર્યાવરણમાં ઉપલબ્ધ દરેક વસ્તુ જેનો ઉપયોગ આપણી જરૂરિયાતો સંતોષવા માટે થઈ શકે છે, જો કે તે તકનીકી રીતે સુલભ, આર્થિક રીતે સક્ષમ અને સાંસ્કૃતિક રીતે સ્વીકાર્ય હોય, તેને 'સંસાધન' (Resource) કહેવામાં આવે છે. પરંતુ જો તે ખતમ થઈ જાય તો શું? જો પૃથ્વી તેની જમીન, જંગલો અને સ્વચ્છ પાણી ગુમાવે તો શું માણસ બચી શકે? ચાલો અન્વેષણ કરીએ કે આપણે કુદરતની ભેટોનો ઉપયોગ અને ક્યારેક દુરુપયોગ કેવી રીતે કરીએ છીએ."
    },
    {
        "id": "KOBJ_NCERT_C10_GEOG_CH1_002",
        "type": "theory",
        "title": "Classification of Resources",
        "title_hi": "संसाधनों का वर्गीकरण",
        "title_gu": "સંસાધનોનું વર્ગીકરણ",
        "body": "Resources can be classified in the following ways:\n1. On the basis of origin: Biotic (obtained from biosphere and have life, e.g., humans, flora and fauna) and Abiotic (composed of non-living things, e.g., rocks and metals).\n2. On the basis of exhaustibility: Renewable (can be renewed by physical, chemical or mechanical processes, e.g., solar energy, wind, forest) and Non-Renewable (occur over a very long geological time and cannot be renewed, e.g., minerals, fossil fuels).\n3. On the basis of ownership: Individual (owned privately), Community (accessible to all members of community), National (belong to the nation), and International (regulated by international institutions).",
        "body_hi": "संसाधनों को निम्नलिखित तरीकों से वर्गीकृत किया जा सकता है:\n1. उत्पत्ति के आधार पर: जैव (Biotic) (जीवमंडल से प्राप्त और जीवन वाले, जैसे, मनुष्य, वनस्पति और जीव) और अजैव (Abiotic) (निर्जीव चीजों से बने, जैसे, चट्टानें और धातुएँ)।\n2. समाप्यता (exhaustibility) के आधार पर: नवीकरणीय (Renewable) (भौतिक, रासायनिक या यांत्रिक प्रक्रियाओं द्वारा नवीनीकृत किया जा सकता है, जैसे, सौर ऊर्जा, हवा, जंगल) और अनवीकरणीय (Non-Renewable) (एक बहुत लंबे भूवैज्ञानिक समय में होते हैं और नवीनीकृत नहीं किए जा सकते, जैसे, खनिज, जीवाश्म ईंधन)।\n3. स्वामित्व (ownership) के आधार पर: व्यक्तिगत, सामुदायिक, राष्ट्रीय और अंतर्राष्ट्रीय।",
        "body_gu": "સંસાધનોનું વર્ગીકરણ નીચે મુજબ કરી શકાય છે:\n1. ઉત્પત્તિના આધારે: જૈવિક (જીવાવરણમાંથી મેળવેલ અને જીવન ધરાવતા, દા.ત., મનુષ્ય, વનસ્પતિ અને પ્રાણીસૃષ્ટિ) અને અજૈવિક (નિર્જીવ વસ્તુઓના બનેલા, દા.ત., ખડકો અને ધાતુઓ).\n2. સમાપ્યતાના (exhaustibility) આધારે: પુનઃપ્રાપ્ય (ભૌતિક, રાસાયણિક અથવા યાંત્રિક પ્રક્રિયાઓ દ્વારા નવીકરણ કરી શકાય છે, દા.ત., સૌર ઉર્જા, પવન, જંગલ) અને બિન-પુનઃપ્રાપ્ય (ખૂબ લાંબા ભૌગોલિક સમયગાળામાં બને છે અને નવીકરણ કરી શકાતા નથી, દા.ત., ખનિજો, અશ્મિભૂત ઇંધણ).\n3. માલિકીના આધારે: વ્યક્તિગત, સામુદાયિક, રાષ્ટ્રીય અને આંતરરાષ્ટ્રીય."
    },
    {
        "id": "KOBJ_NCERT_C10_GEOG_CH1_003",
        "type": "theory",
        "title": "Development of Resources and Agenda 21",
        "title_hi": "संसाधनों का विकास और एजेंडा 21",
        "title_gu": "સંસાધનોનો વિકાસ અને એજન્ડા 21",
        "body": "Resources are vital for human survival, but human beings used them indiscriminately. This led to major problems: depletion of resources, accumulation of wealth in few hands (creating rich and poor), and global ecological crises like global warming and ozone layer depletion.\nSustainable Development means that development should take place without damaging the environment, and development in the present should not compromise with the needs of the future generations.\nRio de Janeiro Earth Summit (1992): More than 100 heads of states met in Brazil and signed the Declaration on Global Climatic Change. They adopted 'Agenda 21' for achieving Sustainable Development in the 21st century.",
        "body_hi": "संसाधन मानव अस्तित्व के लिए महत्वपूर्ण हैं, लेकिन इंसानों ने अंधाधुंध इनका इस्तेमाल किया। इससे बड़ी समस्याएं पैदा हुईं: संसाधनों की कमी, कुछ ही हाथों में धन का संचय (अमीर और गरीब बनाना), और ग्लोबल वार्मिंग और ओजोन परत के क्षरण (depletion) जैसे वैश्विक पारिस्थितिक (ecological) संकट।\nसतत विकास (Sustainable Development) का अर्थ है कि विकास पर्यावरण को नुकसान पहुंचाए बिना होना चाहिए, और वर्तमान में विकास को भविष्य की पीढ़ियों की जरूरतों के साथ समझौता नहीं करना चाहिए।\nरियो डी जनेरियो पृथ्वी शिखर सम्मेलन (1992): ब्राजील में 100 से अधिक राष्ट्राध्यक्षों ने मुलाकात की और वैश्विक जलवायु परिवर्तन पर घोषणा पर हस्ताक्षर किए। उन्होंने 21वीं सदी में सतत विकास प्राप्त करने के लिए 'एजेंडा 21' अपनाया।",
        "body_gu": "માનવ અસ્તિત્વ માટે સંસાધનો મહત્વપૂર્ણ છે, પરંતુ મનુષ્યોએ આડેધડ તેનો ઉપયોગ કર્યો. આનાથી મોટી સમસ્યાઓ ઊભી થઈ: સંસાધનોનો ઘટાડો, થોડા હાથોમાં સંપત્તિનું સંચય (અમીર અને ગરીબ બનાવવું), અને ગ્લોબલ વોર્મિંગ અને ઓઝોન સ્તરના ઘટાડા જેવી વૈશ્વિક ઇકોલોજીકલ કટોકટી.\nટકાઉ વિકાસનો (Sustainable Development) અર્થ એ છે કે પર્યાવરણને નુકસાન પહોંચાડ્યા વિના વિકાસ થવો જોઈએ, અને વર્તમાનમાં વિકાસે ભવિષ્યની પેઢીઓની જરૂરિયાતો સાથે સમાધાન કરવું જોઈએ નહીં.\nરિયો ડી જાનેરો અર્થ સમિટ (1992): બ્રાઝિલમાં 100 થી વધુ રાષ્ટ્રાધ્યક્ષો મળ્યા અને વૈશ્વિક આબોહવા પરિવર્તન પરના ઘોષણાપત્ર પર હસ્તાક્ષર કર્યા. 21મી સદીમાં ટકાઉ વિકાસ હાંસલ કરવા માટે તેઓએ 'એજન્ડા 21' અપનાવ્યો."
    },
    {
        "id": "KOBJ_NCERT_C10_GEOG_CH1_004",
        "type": "socratic_question",
        "title": "Land Degradation",
        "title_hi": "भूमि निम्नीकरण (Land Degradation)",
        "title_gu": "જમીનનું ધોવાણ",
        "question": "We share our land with the past generations and will have to do so with the future generations too. Ninety-five percent of our basic needs for food, shelter and clothing are obtained from land. However, human activities have degraded the land. In states like Jharkhand, Chhattisgarh, and Madhya Pradesh, what human activity do you think is the main cause of severe land degradation?",
        "question_hi": "हम अपनी भूमि को पिछली पीढ़ियों के साथ साझा करते हैं और आने वाली पीढ़ियों के साथ भी ऐसा ही करना होगा। भोजन, आश्रय और कपड़े के लिए हमारी बुनियादी जरूरतों का पचानवे प्रतिशत (95%) भूमि से प्राप्त होता है। हालांकि, मानवीय गतिविधियों ने भूमि को खराब (degrade) कर दिया है। झारखंड, छत्तीसगढ़ और मध्य प्रदेश जैसे राज्यों में, आपको क्या लगता है कि किस मानवीय गतिविधि के कारण गंभीर भूमि निम्नीकरण (land degradation) होता है?",
        "question_gu": "આપણે આપણી જમીન ભૂતકાળની પેઢીઓ સાથે વહેંચીએ છીએ અને ભવિષ્યની પેઢીઓ સાથે પણ આવું કરવું પડશે. ખોરાક, આશ્રય અને કપડાં માટેની આપણી પંચાણું ટકા (95%) મૂળભૂત જરૂરિયાતો જમીનમાંથી મેળવવામાં આવે છે. જો કે, માનવીય પ્રવૃત્તિઓએ જમીનને બગાડી છે. ઝારખંડ, છત્તીસગઢ અને મધ્ય પ્રદેશ જેવા રાજ્યોમાં, તમને શું લાગે છે કે કઈ માનવ પ્રવૃત્તિ ગંભીર જમીનના ધોવાણનું મુખ્ય કારણ છે?",
        "options": [
            "Over-irrigation, which causes water-logging.",
            "Mining, because after excavation work is complete, deep scars and traces of over-burdening are left open.",
            "Overgrazing by cattle and sheep.",
            "Building too many shopping malls."
        ],
        "options_hi": [
            "अत्यधिक सिंचाई, जिससे जल-जमाव होता है।",
            "खनन (Mining), क्योंकि उत्खनन कार्य पूरा होने के बाद, गहरे निशान और मलबे के निशान खुले छोड़ दिए जाते हैं।",
            "मवेशियों और भेड़ों द्वारा अत्यधिक चराई (Overgrazing)।",
            "बहुत सारे शॉपिंग मॉल बनाना।"
        ],
        "options_gu": [
            "વધુ પડતી સિંચાઈ, જેનાથી પાણી ભરાઈ જાય છે.",
            "ખાણકામ (Mining), કારણ કે ખોદકામનું કામ પૂર્ણ થયા પછી, ઊંડા નિશાન અને કાટમાળના નિશાન ખુલ્લા છોડી દેવામાં આવે છે.",
            "ઢોર અને ઘેટાં દ્વારા વધુ પડતું ચરાવવું (Overgrazing).",
            "ઘણા બધા શોપિંગ મોલ બનાવવા."
        ],
        "correct_index": 1,
        "explanation": "In states like Jharkhand, Chhattisgarh, Madhya Pradesh, and Odisha, deforestation due to mining has caused severe land degradation. Mining sites are abandoned after excavation, leaving deep scars. (Over-irrigation is the main cause in Punjab, and overgrazing in Gujarat and Rajasthan).",
        "explanation_hi": "झारखंड, छत्तीसगढ़, मध्य प्रदेश और ओडिशा जैसे राज्यों में खनन के कारण वनों की कटाई से गंभीर भूमि निम्नीकरण हुआ है। खुदाई के बाद खनन स्थलों को छोड़ दिया जाता है, जिससे गहरे निशान रह जाते हैं। (पंजाब में अत्यधिक सिंचाई मुख्य कारण है, और गुजरात और राजस्थान में अत्यधिक चराई)।",
        "explanation_gu": "ઝારખંડ, છત્તીસગઢ, મધ્ય પ્રદેશ અને ઓડિશા જેવા રાજ્યોમાં ખાણકામને કારણે જંગલો કાપવાથી જમીનનું ગંભીર ધોવાણ થયું છે. ખોદકામ પછી ખાણકામની જગ્યાઓ છોડી દેવામાં આવે છે, જે ઊંડા નિશાન પાછળ છોડી દે છે. (પંજાબમાં વધુ પડતી સિંચાઈ મુખ્ય કારણ છે, અને ગુજરાત અને રાજસ્થાનમાં વધુ પડતું ચરાવવું)."
    },
    {
        "id": "KOBJ_NCERT_C10_GEOG_CH1_005",
        "type": "theory",
        "title": "Soil as a Resource",
        "title_hi": "एक संसाधन के रूप में मृदा (मिट्टी)",
        "title_gu": "સંસાધન તરીકે જમીન (માટી)",
        "body": "Soil is the most important renewable natural resource. It is the medium of plant growth and supports different types of living organisms on the earth. It takes millions of years to form soil upto a few cm in depth.\nMajor Types of Soils in India:\n1. Alluvial Soil: Most widely spread and important soil. The entire northern plains are made of alluvial soil deposited by the Indus, Ganga, and Brahmaputra. Very fertile, contains potash, phosphoric acid, and lime.\n2. Black Soil: Black in color, also known as regur soils. Ideal for growing cotton. Found in the Deccan trap (Basalt) region spread over Maharashtra, Saurashtra, Malwa, MP, and Chhattisgarh.\n3. Red and Yellow Soil: Develops on crystalline igneous rocks in areas of low rainfall. Looks red due to diffusion of iron, looks yellow when it occurs in a hydrated form.\n4. Laterite Soil: Develops in areas with high temperature and heavy rainfall. Result of intense leaching. Good for tea, coffee, and cashew nuts.\n5. Arid Soil: Range from red to brown. Sandy in texture, saline in nature. Lacks humus and moisture.\n6. Forest Soil: Found in hilly and mountainous areas where sufficient rain forests are available.",
        "body_hi": "मृदा (मिट्टी) सबसे महत्वपूर्ण नवीकरणीय प्राकृतिक संसाधन है। यह पौधों के विकास का माध्यम है और पृथ्वी पर विभिन्न प्रकार के जीवों का समर्थन करता है। कुछ सेमी गहराई तक मिट्टी बनने में लाखों साल लग जाते हैं।\nभारत में मिट्टी के प्रमुख प्रकार:\n1. जलोढ़ मिट्टी (Alluvial Soil): सबसे अधिक फैली और महत्वपूर्ण मिट्टी। पूरा उत्तरी मैदान सिंधु, गंगा और ब्रह्मपुत्र द्वारा जमा की गई जलोढ़ मिट्टी से बना है। बहुत उपजाऊ होती है।\n2. काली मिट्टी (Black Soil): काले रंग की, जिसे रेगुर मिट्टी भी कहा जाता है। कपास उगाने के लिए आदर्श। दक्कन के पठार में पाई जाती है।\n3. लाल और पीली मिट्टी: कम वर्षा वाले क्षेत्रों में क्रिस्टलीय आग्नेय चट्टानों पर विकसित होती है। लोहे के प्रसार के कारण लाल दिखती है।\n4. लेटराइट मिट्टी: उच्च तापमान और भारी वर्षा वाले क्षेत्रों में विकसित होती है। यह भारी निक्षालन (leaching) का परिणाम है। चाय, कॉफी और काजू के लिए अच्छी है।\n5. शुष्क मिट्टी (Arid Soil): लाल से भूरे रंग की। रेतीली और खारी। नमी की कमी।\n6. वन मिट्टी: पहाड़ी और पर्वतीय क्षेत्रों में पाई जाती है।",
        "body_gu": "માટી (જમીન) એ સૌથી મહત્વપૂર્ણ પુનઃપ્રાપ્ય કુદરતી સંસાધન છે. તે છોડના વિકાસનું માધ્યમ છે અને પૃથ્વી પર વિવિધ પ્રકારના જીવોને ટેકો આપે છે. થોડા સેમી ઊંડાઈ સુધી માટી બનવામાં લાખો વર્ષ લાગે છે.\nભારતમાં જમીનના મુખ્ય પ્રકારો:\n1. કાંપવાળી જમીન (Alluvial Soil): સૌથી વધુ ફેલાયેલી અને મહત્વપૂર્ણ જમીન. સમગ્ર ઉત્તરીય મેદાનો સિંધુ, ગંગા અને બ્રહ્મપુત્રા દ્વારા જમા થયેલી કાંપની જમીનથી બનેલા છે. ખૂબ ફળદ્રુપ હોય છે.\n2. કાળી જમીન (Black Soil): કાળા રંગની, જેને રેગુર જમીન પણ કહેવાય છે. કપાસ ઉગાડવા માટે આદર્શ. દખ્ખણના ઉચ્ચપ્રદેશમાં જોવા મળે છે.\n3. લાલ અને પીળી જમીન: ઓછા વરસાદવાળા વિસ્તારોમાં સ્ફટિકીય અગ્નિકૃત ખડકો પર વિકસે છે. લોખંડના પ્રસારને કારણે લાલ દેખાય છે.\n4. લેટેરાઇટ જમીન: ઉચ્ચ તાપમાન અને ભારે વરસાદવાળા વિસ્તારોમાં વિકસે છે. તે ભારે ધોવાણનું પરિણામ છે. ચા, કોફી અને કાજુ માટે સારી છે.\n5. શુષ્ક જમીન (Arid Soil): લાલ થી ભૂરા રંગની. રેતાળ અને ખારી. ભેજનો અભાવ.\n6. જંગલની જમીન: ડુંગરાળ અને પર્વતીય વિસ્તારોમાં જોવા મળે છે."
    },
    {
        "id": "KOBJ_NCERT_C10_GEOG_CH1_006",
        "type": "theory",
        "title": "Soil Erosion and Conservation",
        "title_hi": "मृदा अपरदन (Soil Erosion) और संरक्षण",
        "title_gu": "જમીનનું ધોવાણ (Soil Erosion) અને સંરક્ષણ",
        "body": "The denudation of the soil cover and subsequent washing down is described as soil erosion. Wind and water are powerful agents of soil erosion.\nWhen running water cuts through clayey soils and makes deep channels, it creates 'gullies'. The land becomes unfit for cultivation and is known as bad land (e.g., ravines in the Chambal basin).\nWhen water flows as a sheet over large areas down a slope, washing away the topsoil, it is called sheet erosion.\nConservation Measures:\n1. Contour ploughing: Ploughing along the contour lines can decelerate the flow of water down the slopes.\n2. Terrace cultivation: Cutting steps on slopes to restrict erosion (common in Western and Central Himalayas).\n3. Strip cropping: Large fields are divided into strips. Strips of grass are left to grow between the crops to break the force of the wind.\n4. Shelter belts: Planting lines of trees to create shelter, which breaks the wind force.",
        "body_hi": "मृदा आवरण के कटने और बह जाने को मृदा अपरदन (soil erosion) कहा जाता है। हवा और पानी मिट्टी के कटाव के शक्तिशाली कारक हैं।\nजब बहता पानी चिकनी मिट्टी को काटता है और गहरी नलिकाएं (channels) बनाता है, तो यह 'अवनालिकाएं' (gullies) बनाता है। भूमि खेती के लिए अनुपयुक्त हो जाती है (जैसे चंबल बेसिन में बीहड़)।\nसंरक्षण के उपाय:\n1. समोच्च जुताई (Contour ploughing): समोच्च रेखाओं के साथ जुताई करने से ढलानों से पानी का बहाव धीमा हो सकता है।\n2. सीढ़ीदार खेती (Terrace cultivation): कटाव को रोकने के लिए ढलानों पर सीढ़ियां काटना (हिमालय में आम)।\n3. पट्टीदार खेती (Strip cropping): हवा के बल को तोड़ने के लिए फसलों के बीच घास की पट्टियां उगने के लिए छोड़ दी जाती हैं।\n4. रक्षक मेखला (Shelter belts): हवा के बल को रोकने के लिए पेड़ों की कतारें लगाना।",
        "body_gu": "માટીના આવરણના કપાવા અને વહી જવાને જમીનનું ધોવાણ (soil erosion) કહેવામાં આવે છે. પવન અને પાણી જમીનના ધોવાણના શક્તિશાળી પરિબળો છે.\nજ્યારે વહેતું પાણી ચીકણી જમીનને કાપીને ઊંડી નહેરો (channels) બનાવે છે, ત્યારે તે 'કોતરો' (gullies) બનાવે છે. જમીન ખેતી માટે અયોગ્ય બની જાય છે (દા.ત. ચંબલ બેસિનમાં કોતરો).\nસંરક્ષણના પગલાં:\n1. સમોચ્ચ ખેડાણ (Contour ploughing): સમોચ્ચ રેખાઓ સાથે ખેડાણ કરવાથી ઢોળાવ નીચે પાણીનો પ્રવાહ ધીમો પડી શકે છે.\n2. સીડીદાર ખેતી (Terrace cultivation): ધોવાણને રોકવા માટે ઢોળાવ પર પગથિયાં કાપવા (હિમાલયમાં સામાન્ય).\n3. પટ્ટીદાર ખેતી (Strip cropping): પવનના બળને તોડવા માટે પાકની વચ્ચે ઘાસની પટ્ટીઓ ઉગવા માટે છોડી દેવામાં આવે છે.\n4. રક્ષક પટ્ટી (Shelter belts): પવનના બળને રોકવા માટે વૃક્ષોની હરોળ વાવવી."
    },
    {
        "id": "KOBJ_NCERT_C10_GEOG_CH1_007",
        "type": "mcq",
        "title": "NCERT Exercise Q1_i",
        "title_hi": "NCERT अभ्यास Q1_i",
        "title_gu": "NCERT સ્વાધ્યાય Q1_i",
        "question": "Which one of the following types of resource is iron ore?",
        "question_hi": "लौह अयस्क (iron ore) निम्नलिखित में से किस प्रकार का संसाधन है?",
        "question_gu": "લોખંડની કાચી ધાતુ (iron ore) નીચેનામાંથી કયા પ્રકારનું સંસાધન છે?",
        "options": [
            "Renewable",
            "Biotic",
            "Flow",
            "Non-renewable"
        ],
        "options_hi": [
            "नवीकरणीय (Renewable)",
            "जैव (Biotic)",
            "प्रवाह (Flow)",
            "अनवीकरणीय (Non-renewable)"
        ],
        "options_gu": [
            "પુનઃપ્રાપ્ય (Renewable)",
            "જૈવિક (Biotic)",
            "પ્રવાહ (Flow)",
            "બિન-પુનઃપ્રાપ્ય (Non-renewable)"
        ],
        "correct_index": 3,
        "explanation": "Iron ore is a mineral that occurs over a very long geological time. Once extracted and used, it cannot be naturally replenished in a short period, making it a non-renewable resource.",
        "explanation_hi": "लौह अयस्क एक खनिज है जो बहुत लंबे भूवैज्ञानिक समय में बनता है। एक बार निकाले और उपयोग किए जाने के बाद, इसे थोड़े समय में स्वाभाविक रूप से फिर से नहीं बनाया जा सकता है, जिससे यह एक गैर-नवीकरणीय (non-renewable) संसाधन बन जाता है।",
        "explanation_gu": "લોખંડની કાચી ધાતુ એક ખનિજ છે જે ખૂબ લાંબા ભૌગોલિક સમયગાળામાં બને છે. એકવાર કાઢીને ઉપયોગમાં લીધા પછી, તેને ટૂંકા ગાળામાં કુદરતી રીતે ફરીથી બનાવી શકાતી નથી, જે તેને બિન-પુનઃપ્રાપ્ય (non-renewable) સંસાધન બનાવે છે."
    },
    {
        "id": "KOBJ_NCERT_C10_GEOG_CH1_008",
        "type": "mcq",
        "title": "NCERT Exercise Q1_iii",
        "title_hi": "NCERT अभ्यास Q1_iii",
        "title_gu": "NCERT સ્વાધ્યાય Q1_iii",
        "question": "Which one of the following is the main cause of land degradation in Punjab?",
        "question_hi": "पंजाब में भूमि निम्नीकरण (land degradation) का मुख्य कारण निम्नलिखित में से कौन सा है?",
        "question_gu": "પંજાબમાં જમીનના ધોવાણનું મુખ્ય કારણ નીચેનામાંથી કયું છે?",
        "options": [
            "Intense cultivation",
            "Deforestation",
            "Over irrigation",
            "Overgrazing"
        ],
        "options_hi": [
            "गहन खेती (Intense cultivation)",
            "वनों की कटाई (Deforestation)",
            "अत्यधिक सिंचाई (Over irrigation)",
            "अत्यधिक चराई (Overgrazing)"
        ],
        "options_gu": [
            "સઘન ખેતી (Intense cultivation)",
            "જંગલો કાપવા (Deforestation)",
            "વધુ પડતી સિંચાઈ (Over irrigation)",
            "વધુ પડતું ચરાવવું (Overgrazing)"
        ],
        "correct_index": 2,
        "explanation": "In states like Punjab, Haryana, and western Uttar Pradesh, over-irrigation is responsible for land degradation due to water logging leading to an increase in salinity and alkalinity in the soil.",
        "explanation_hi": "पंजाब, हरियाणा और पश्चिमी उत्तर प्रदेश जैसे राज्यों में, अत्यधिक सिंचाई भूमि के क्षरण के लिए जिम्मेदार है क्योंकि जल जमाव (water logging) से मिट्टी में लवणता (salinity) और क्षारीयता (alkalinity) बढ़ जाती है।",
        "explanation_gu": "પંજાબ, હરિયાણા અને પશ્ચિમ ઉત્તર પ્રદેશ જેવા રાજ્યોમાં, વધુ પડતી સિંચાઈ જમીનના ધોવાણ માટે જવાબદાર છે કારણ કે પાણી ભરાવાથી જમીનમાં ખારાશ (salinity) અને આલ્કલાઇનિટી (alkalinity) વધે છે."
    },
    {
        "id": "KOBJ_NCERT_C10_GEOG_CH1_009",
        "type": "mcq",
        "title": "NCERT Exercise Q1_iv",
        "title_hi": "NCERT अभ्यास Q1_iv",
        "title_gu": "NCERT સ્વાધ્યાય Q1_iv",
        "question": "In which one of the following states is terrace cultivation practised?",
        "question_hi": "निम्नलिखित में से किस राज्य में सीढ़ीदार खेती (terrace cultivation) की जाती है?",
        "question_gu": "નીચેનામાંથી કયા રાજ્યમાં સીડીદાર ખેતી (terrace cultivation) કરવામાં આવે છે?",
        "options": [
            "Punjab",
            "Plains of Uttar Pradesh",
            "Haryana",
            "Uttarakhand"
        ],
        "options_hi": [
            "पंजाब",
            "उत्तर प्रदेश के मैदान",
            "हरियाणा",
            "उत्तराखंड"
        ],
        "options_gu": [
            "પંજાબ",
            "ઉત્તર પ્રદેશના મેદાનો",
            "હરિયાણા",
            "ઉત્તરાખંડ"
        ],
        "correct_index": 3,
        "explanation": "Terrace cultivation is practiced on hilly slopes to restrict soil erosion. Uttarakhand is a mountainous state in the Himalayas, making it the correct answer.",
        "explanation_hi": "मिट्टी के कटाव को रोकने के लिए पहाड़ी ढलानों पर सीढ़ीदार खेती (Terrace cultivation) की जाती है। उत्तराखंड हिमालय का एक पहाड़ी राज्य है, जो इसे सही उत्तर बनाता है।",
        "explanation_gu": "જમીનનું ધોવાણ રોકવા માટે ડુંગરાળ ઢોળાવ પર સીડીદાર ખેતી (Terrace cultivation) કરવામાં આવે છે. ઉત્તરાખંડ હિમાલયનું એક પર્વતીય રાજ્ય છે, જે તેને સાચો જવાબ બનાવે છે."
    },
    {
        "id": "KOBJ_NCERT_C10_GEOG_CH1_010",
        "type": "mcq",
        "title": "NCERT Exercise Q2a",
        "title_hi": "NCERT अभ्यास Q2a",
        "title_gu": "NCERT સ્વાધ્યાય Q2a",
        "question": "Name the crop which is mainly grown in black soil.",
        "question_hi": "काली मिट्टी में मुख्य रूप से उगाई जाने वाली फसल का नाम बताइए।",
        "question_gu": "કાળી જમીનમાં મુખ્યત્વે કયો પાક ઉગાડવામાં આવે છે તે જણાવો.",
        "options": [
            "Wheat",
            "Rice",
            "Cotton",
            "Tea"
        ],
        "options_hi": [
            "गेहूँ",
            "चावल",
            "कपास",
            "चाय"
        ],
        "options_gu": [
            "ઘઉં",
            "ચોખા",
            "કપાસ",
            "ચા"
        ],
        "correct_index": 2,
        "explanation": "Black soil is black in color and is also known as regur soil. It is ideal for growing cotton and is often called black cotton soil. It is found in states like Maharashtra, Gujarat, and Madhya Pradesh.",
        "explanation_hi": "काली मिट्टी का रंग काला होता है और इसे रेगुर मिट्टी भी कहा जाता है। यह कपास उगाने के लिए आदर्श है और इसे अक्सर काली कपास मिट्टी कहा जाता है। यह महाराष्ट्र, गुजरात और मध्य प्रदेश जैसे राज्यों में पाई जाती है।",
        "explanation_gu": "કાળી જમીનનો રંગ કાળો હોય છે અને તેને રેગુર જમીન પણ કહેવામાં આવે છે. તે કપાસ ઉગાડવા માટે આદર્શ છે અને તેને કાળી કપાસની જમીન પણ કહેવામાં આવે છે. તે મહારાષ્ટ્ર, ગુજરાત અને મધ્ય પ્રદેશ જેવા રાજ્યોમાં જોવા મળે છે."
    },
    {
        "id": "KOBJ_NCERT_C10_GEOG_CH1_011",
        "type": "mcq",
        "title": "NCERT Exercise Q2b",
        "title_hi": "NCERT अभ्यास Q2b",
        "title_gu": "NCERT સ્વાધ્યાય Q2b",
        "question": "What type of soil is found in the river deltas of the eastern coast (Mahanadi, Godavari, Krishna, and Kaveri)?",
        "question_hi": "पूर्वी तट (महानदी, गोदावरी, कृष्णा और कावेरी) के नदी डेल्टाओं में किस प्रकार की मिट्टी पाई जाती है?",
        "question_gu": "પૂર્વીય કિનારાના (મહા નદી, ગોદાવરી, કૃષ્ણા અને કાવેરી) નદીના મુખત્રિકોણ પ્રદેશોમાં કયા પ્રકારની જમીન જોવા મળે છે?",
        "options": [
            "Black Soil",
            "Laterite Soil",
            "Alluvial Soil",
            "Arid Soil"
        ],
        "options_hi": [
            "काली मिट्टी",
            "लेटराइट मिट्टी",
            "जलोढ़ मिट्टी (Alluvial Soil)",
            "शुष्क मिट्टी"
        ],
        "options_gu": [
            "કાળી જમીન",
            "લેટેરાઇટ જમીન",
            "કાંપવાળી જમીન (Alluvial Soil)",
            "શુષ્ક જમીન"
        ],
        "correct_index": 2,
        "explanation": "Alluvial soil is found in the river deltas of the eastern coast. It is extremely fertile, containing adequate proportions of potash, phosphoric acid, and lime, making it ideal for the growth of sugarcane, paddy, and wheat.",
        "explanation_hi": "पूर्वी तट के नदी डेल्टाओं में जलोढ़ मिट्टी (Alluvial soil) पाई जाती है। यह अत्यधिक उपजाऊ होती है, जिसमें पोटाश, फॉस्फोरिक एसिड और चूने का पर्याप्त अनुपात होता है, जो इसे गन्ने, धान और गेहूं के विकास के लिए आदर्श बनाता है।",
        "explanation_gu": "પૂર્વીય કિનારાના નદીના મુખત્રિકોણ પ્રદેશોમાં કાંપવાળી જમીન (Alluvial soil) જોવા મળે છે. તે અત્યંત ફળદ્રુપ છે, જેમાં પોટાશ, ફોસ્ફોરિક એસિડ અને ચૂનાનું પૂરતું પ્રમાણ છે, જે તેને શેરડી, ડાંગર અને ઘઉંના વિકાસ માટે આદર્શ બનાવે છે."
    }
]

data = {
    "metadata": {
        "id": "ncert_class10_geography_ch1",
        "title": "Geography Chapter 1: Resources and Development",
        "subject": "Social Science",
        "grade": "10"
    },
    "blocks": blocks
}

output_path = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_geography_ch1.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Successfully wrote {len(blocks)} blocks to {output_path}")
