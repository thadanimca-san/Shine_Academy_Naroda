import json

blocks = [
    {
        "id": "KOBJ_NCERT_C10_GEOG_CH4_001",
        "type": "hook",
        "title": "The Backbone of India",
        "title_hi": "भारत की रीढ़",
        "title_gu": "ભારતની કરોડરજ્જુ",
        "body": "When you sit down to eat your favourite meal—whether it's a hot chapati, a bowl of rice, or a cup of sweet tea—do you ever wonder where it comes from? India is an agriculturally important country. Two-thirds of its population is engaged in agricultural activities. It not only produces most of the food we consume, but also produces raw materials for various industries. How do millions of farmers across different climates grow so many different crops? Let's explore the world of Indian agriculture.",
        "body_hi": "जब आप अपना पसंदीदा भोजन खाने बैठते हैं—चाहे वह गर्म चपाती हो, चावल का कटोरा हो, या एक कप मीठी चाय हो—क्या आप कभी सोचते हैं कि यह कहाँ से आता है? भारत एक कृषि प्रधान देश है। इसकी दो-तिहाई आबादी कृषि गतिविधियों में लगी हुई है। यह न केवल हमारे द्वारा उपभोग किए जाने वाले अधिकांश भोजन का उत्पादन करता है, बल्कि विभिन्न उद्योगों के लिए कच्चा माल भी पैदा करता है। विभिन्न जलवायु वाले लाखों किसान इतनी अलग-अलग फसलें कैसे उगाते हैं? आइए भारतीय कृषि की दुनिया का अन्वेषण करें।",
        "body_gu": "જ્યારે તમે તમારું મનપસંદ ભોજન ખાવા બેસો છો - પછી ભલે તે ગરમ રોટલી હોય, ચોખાનો બાઉલ હોય કે મીઠી ચાનો કપ હોય - શું તમે ક્યારેય વિચાર્યું છે કે તે ક્યાંથી આવે છે? ભારત ખેતીની દ્રષ્ટિએ મહત્વનો દેશ છે. તેની બે તૃતીયાંશ વસ્તી ખેતીની પ્રવૃત્તિઓમાં રોકાયેલી છે. તે માત્ર આપણે વાપરીએ છીએ તે મોટાભાગનો ખોરાક જ ઉત્પન્ન કરતું નથી, પરંતુ વિવિધ ઉદ્યોગો માટે કાચો માલ પણ ઉત્પન્ન કરે છે. વિવિધ આબોહવા ધરાવતા લાખો ખેડૂતો આટલા અલગ-અલગ પાક કેવી રીતે ઉગાડે છે? ચાલો ભારતીય કૃષિની દુનિયાનું અન્વેષણ કરીએ."
    },
    {
        "id": "KOBJ_NCERT_C10_GEOG_CH4_002",
        "type": "theory",
        "title": "Types of Farming",
        "title_hi": "खेती के प्रकार",
        "title_gu": "ખેતીના પ્રકારો",
        "body": "Farming varies from subsistence to commercial type.\n1. Primitive Subsistence Farming: Practised on small patches of land with primitive tools like hoe and digging sticks, using family labour. It depends on monsoon and natural fertility of the soil. (e.g., 'Slash and burn' agriculture or Jhumming).\n2. Intensive Subsistence Farming: Practised in areas of high population pressure on land. It is labour-intensive farming, where high doses of biochemical inputs and irrigation are used for obtaining higher production.\n3. Commercial Farming: The main characteristic is the use of higher doses of modern inputs (HYV seeds, chemical fertilizers, insecticides) to obtain higher productivity. \nPlantation is a type of commercial farming where a single crop is grown on a large area (e.g., tea in Assam, coffee in Karnataka, rubber in Kerala).",
        "body_hi": "खेती निर्वाह (subsistence) से लेकर वाणिज्यिक (commercial) प्रकार तक भिन्न होती है।\n1. प्रारंभिक निर्वाह कृषि (Primitive Subsistence Farming): भूमि के छोटे टुकड़ों पर आदिम औजारों जैसे कुदाल (hoe) और खुदाई करने वाली छड़ियों से परिवार के श्रम का उपयोग करके की जाती है। यह मानसून और मिट्टी की प्राकृतिक उर्वरता पर निर्भर करती है। (जैसे, 'काटो और जलाओ' (slash and burn) कृषि या झूमिंग)।\n2. गहन निर्वाह कृषि (Intensive Subsistence Farming): भूमि पर उच्च जनसंख्या दबाव वाले क्षेत्रों में की जाती है। यह श्रम-गहन खेती है, जहाँ उच्च उत्पादन प्राप्त करने के लिए जैव रासायनिक आदानों और सिंचाई की उच्च खुराक का उपयोग किया जाता है।\n3. वाणिज्यिक कृषि (Commercial Farming): मुख्य विशेषता उच्च उत्पादकता प्राप्त करने के लिए आधुनिक आदानों (HYV बीज, रासायनिक उर्वरक, कीटनाशक) की उच्च खुराक का उपयोग है।\nवृक्षारोपण (Plantation) एक प्रकार की व्यावसायिक खेती है जहाँ एक बड़े क्षेत्र में एकल फसल उगाई जाती है (जैसे, असम में चाय, कर्नाटक में कॉफी)।",
        "body_gu": "ખેતી નિર્વાહથી (subsistence) લઈને વ્યાપારી (commercial) પ્રકાર સુધી બદલાય છે.\n1. પ્રાથમિક નિર્વાહ ખેતી (Primitive Subsistence Farming): પરિવારના મજૂરોનો ઉપયોગ કરીને કોદાળી (hoe) અને ખોદવાની લાકડીઓ જેવા આદિમ સાધનો વડે જમીનના નાના ટુકડાઓ પર કરવામાં આવે છે. તે ચોમાસા અને જમીનની કુદરતી ફળદ્રુપતા પર આધાર રાખે છે. (દા.ત., 'સ્લેશ અને બર્ન' ખેતી અથવા ઝૂમિંગ).\n2. સઘન નિર્વાહ ખેતી (Intensive Subsistence Farming): જમીન પર ઉચ્ચ વસ્તીનું દબાણ ધરાવતા વિસ્તારોમાં કરવામાં આવે છે. તે શ્રમ-સઘન ખેતી છે, જ્યાં વધુ ઉત્પાદન મેળવવા માટે બાયોકેમિકલ ઇનપુટ્સ અને સિંચાઈના ઊંચા ડોઝનો ઉપયોગ થાય છે.\n3. વાણિજ્યિક ખેતી (Commercial Farming): મુખ્ય લાક્ષણિકતા ઉચ્ચ ઉત્પાદકતા મેળવવા માટે આધુનિક ઇનપુટ્સ (HYV બિયારણ, રાસાયણિક ખાતરો, જંતુનાશકો) નો ઉપયોગ છે.\nબાગાયતી ખેતી (Plantation) એ વ્યાપારી ખેતીનો એક પ્રકાર છે જ્યાં મોટા વિસ્તારમાં એક જ પાક ઉગાડવામાં આવે છે (દા.ત., આસામમાં ચા, કર્ણાટકમાં કોફી)."
    },
    {
        "id": "KOBJ_NCERT_C10_GEOG_CH4_003",
        "type": "theory",
        "title": "Cropping Pattern in India",
        "title_hi": "भारत में फसल पैटर्न",
        "title_gu": "ભારતમાં પાકની પદ્ધતિ",
        "body": "India has three distinct cropping seasons:\n1. Rabi: Sown in winter from October to December and harvested in summer from April to June. Important crops: wheat, barley, peas, gram and mustard.\n2. Kharif: Grown with the onset of monsoon in different parts of the country and harvested in September-October. Important crops: paddy (rice), maize, jowar, bajra, tur (arhar), moong, urad, cotton, jute, groundnut and soyabean.\n3. Zaid: In between the rabi and the kharif seasons, there is a short season during the summer months known as the Zaid season. Crops: watermelon, muskmelon, cucumber, vegetables and fodder crops.",
        "body_hi": "भारत में तीन अलग-अलग फसल मौसम (cropping seasons) हैं:\n1. रबी (Rabi): सर्दियों में अक्टूबर से दिसंबर तक बोई जाती है और गर्मियों में अप्रैल से जून तक काटी जाती है। महत्वपूर्ण फसलें: गेहूं, जौ, मटर, चना और सरसों।\n2. खरीफ (Kharif): देश के विभिन्न हिस्सों में मानसून की शुरुआत के साथ उगाई जाती है और सितंबर-अक्टूबर में काटी जाती है। महत्वपूर्ण फसलें: धान (चावल), मक्का, ज्वार, बाजरा, अरहर, मूंग, उड़द, कपास, जूट, मूंगफली और सोयाबीन।\n3. जायद (Zaid): रबी और खरीफ मौसम के बीच, गर्मी के महीनों के दौरान एक छोटा मौसम होता है जिसे जायद मौसम के रूप में जाना जाता है। फसलें: तरबूज, खरबूजा, ककड़ी, सब्जियां और चारे की फसलें।",
        "body_gu": "ભારતમાં ત્રણ અલગ-અલગ પાકની ઋતુઓ છે:\n1. રવિ (Rabi): શિયાળામાં ઓક્ટોબરથી ડિસેમ્બર સુધી વાવવામાં આવે છે અને ઉનાળામાં એપ્રિલથી જૂન સુધી લણણી કરવામાં આવે છે. અગત્યના પાકો: ઘઉં, જવ, વટાણા, ચણા અને રાઈ.\n2. ખરીફ (Kharif): દેશના જુદા જુદા ભાગોમાં ચોમાસાની શરૂઆત સાથે ઉગાડવામાં આવે છે અને સપ્ટેમ્બર-ઓક્ટોબરમાં લણણી કરવામાં આવે છે. મહત્વના પાકો: ડાંગર (ચોખા), મકાઈ, જુવાર, બાજરી, તુવેર, મગ, અડદ, કપાસ, શણ, મગફળી અને સોયાબીન.\n3. ઝાયદ (Zaid): રવિ અને ખરીફ ઋતુઓ વચ્ચે, ઉનાળાના મહિનાઓ દરમિયાન એક ટૂંકી ઋતુ હોય છે જેને ઝાયદ ઋતુ તરીકે ઓળખવામાં આવે છે. પાક: તરબૂચ, ટેટી, કાકડી, શાકભાજી અને ચારાના પાક."
    },
    {
        "id": "KOBJ_NCERT_C10_GEOG_CH4_004",
        "type": "theory",
        "title": "Major Crops of India",
        "title_hi": "भारत की प्रमुख फसलें",
        "title_gu": "ભારતના મુખ્ય પાકો",
        "body": "1. Rice: It is the staple food crop of a majority of the people in India. It is a kharif crop which requires high temperature (above 25°C) and high humidity with annual rainfall above 100 cm.\n2. Wheat: This is the second most important cereal crop and the main food crop in the north and north-western parts of India. It is a rabi crop that requires a cool growing season and bright sunshine at the time of ripening.\n3. Millets: Jowar, bajra and ragi are the important millets grown in India. They are known as coarse grains but have very high nutritional value.\n4. Tea: An important beverage crop introduced by the British. It grows well in tropical and sub-tropical climates with deep and fertile well-drained soil, rich in humus. Assam is the major tea producing state.",
        "body_hi": "1. चावल (Rice): यह भारत में अधिकांश लोगों की मुख्य खाद्य फसल है। यह एक खरीफ फसल है जिसके लिए उच्च तापमान (25 डिग्री सेल्सियस से ऊपर) और 100 सेमी से ऊपर वार्षिक वर्षा के साथ उच्च आर्द्रता (humidity) की आवश्यकता होती है।\n2. गेहूँ (Wheat): यह दूसरी सबसे महत्वपूर्ण अनाज की फसल है और भारत के उत्तर और उत्तर-पश्चिमी भागों में मुख्य खाद्य फसल है। यह एक रबी फसल है जिसे पकने के समय ठंडे मौसम और तेज धूप की आवश्यकता होती है।\n3. बाजरा/मोटे अनाज (Millets): ज्वार, बाजरा और रागी भारत में उगाए जाने वाले महत्वपूर्ण मोटे अनाज हैं। इन्हें मोटे अनाज के रूप में जाना जाता है लेकिन इनका पोषण मूल्य बहुत अधिक होता है।\n4. चाय (Tea): अंग्रेजों द्वारा पेश की गई एक महत्वपूर्ण पेय फसल। यह गहरी और उपजाऊ अच्छी जल निकासी वाली मिट्टी (well-drained soil) के साथ उष्णकटिबंधीय (tropical) और उप-उष्णकटिबंधीय जलवायु में अच्छी तरह से बढ़ती है। असम प्रमुख चाय उत्पादक राज्य है।",
        "body_gu": "1. ચોખા (Rice): તે ભારતમાં મોટાભાગના લોકોનો મુખ્ય ખાદ્ય પાક છે. તે ખરીફ પાક છે જેને ઊંચા તાપમાન (25°C થી ઉપર) અને 100 સેમીથી વધુ વાર્ષિક વરસાદ સાથે ઉચ્ચ ભેજની (humidity) જરૂર હોય છે.\n2. ઘઉં (Wheat): આ બીજા ક્રમનો સૌથી મહત્વનો ધાન્ય પાક છે અને ભારતના ઉત્તર અને ઉત્તર-પશ્ચિમ ભાગોમાં મુખ્ય ખાદ્ય પાક છે. તે રવિ પાક છે જેને વૃદ્ધિ માટે ઠંડી ઋતુ અને પાકતી વખતે તેજસ્વી સૂર્યપ્રકાશની જરૂર હોય છે.\n3. બાજરી/બરછટ અનાજ (Millets): જુવાર, બાજરી અને રાગી ભારતમાં ઉગાડવામાં આવતા મહત્વના બરછટ અનાજ છે. તેઓ બરછટ અનાજ તરીકે ઓળખાય છે પરંતુ તેનું પોષણ મૂલ્ય ખૂબ જ ઊંચું છે.\n4. ચા (Tea): અંગ્રેજો દ્વારા રજૂ કરાયેલ એક મહત્વપૂર્ણ પીણાનો પાક. તે ઉષ્ણકટિબંધીય (tropical) અને ઉપ-ઉષ્ણકટિબંધીય આબોહવામાં ઊંડી અને ફળદ્રુપ સારી રીતે નીતારવાળી જમીનમાં (well-drained soil) સારી રીતે ઉગે છે. આસામ મુખ્ય ચા ઉત્પાદક રાજ્ય છે."
    },
    {
        "id": "KOBJ_NCERT_C10_GEOG_CH4_005",
        "type": "socratic_question",
        "title": "Technological and Institutional Reforms",
        "title_hi": "तकनीकी और संस्थागत सुधार",
        "title_gu": "તકનીકી અને સંસ્થાકીય સુધારાઓ",
        "question": "Indian farmers face many risks like droughts, floods, and crop diseases. Often, they have to take loans from moneylenders at very high interest rates. To protect farmers from these problems, which of the following is a major 'institutional reform' introduced by the Government of India?",
        "question_hi": "भारतीय किसानों को सूखे, बाढ़ और फसल की बीमारियों जैसे कई जोखिमों का सामना करना पड़ता है। अक्सर, उन्हें साहूकारों से बहुत अधिक ब्याज दरों पर ऋण लेना पड़ता है। किसानों को इन समस्याओं से बचाने के लिए, भारत सरकार द्वारा शुरू किया गया प्रमुख 'संस्थागत सुधार' (institutional reform) निम्नलिखित में से कौन सा है?",
        "question_gu": "ભારતીય ખેડૂતોને દુષ્કાળ, પૂર અને પાકના રોગો જેવા ઘણા જોખમોનો સામનો કરવો પડે છે. ઘણીવાર, તેઓએ શાહુકારો પાસેથી ઊંચા વ્યાજ દરે લોન લેવી પડે છે. ખેડૂતોને આ સમસ્યાઓથી બચાવવા માટે, ભારત સરકાર દ્વારા નીચેનામાંથી કયો મોટો 'સંસ્થાકીય સુધારો' (institutional reform) રજૂ કરવામાં આવ્યો છે?",
        "options": [
            "Forcing all farmers to grow only one crop (like rice) everywhere.",
            "Establishment of Grameen banks, cooperative societies, and Kissan Credit Cards (KCC) to provide loans at low interest rates.",
            "Banning the use of tractors and asking farmers to only use bullocks.",
            "Removing all taxes on foreign agricultural imports."
        ],
        "options_hi": [
            "सभी किसानों को हर जगह केवल एक फसल (जैसे चावल) उगाने के लिए मजबूर करना।",
            "कम ब्याज दरों पर ऋण प्रदान करने के लिए ग्रामीण बैंकों, सहकारी समितियों और किसान क्रेडिट कार्ड (KCC) की स्थापना।",
            "ट्रैक्टरों के उपयोग पर प्रतिबंध लगाना और किसानों को केवल बैलों का उपयोग करने के लिए कहना।",
            "विदेशी कृषि आयात पर सभी करों को हटाना।"
        ],
        "options_gu": [
            "તમામ ખેડૂતોને દરેક જગ્યાએ માત્ર એક જ પાક (જેમ કે ચોખા) ઉગાડવાની ફરજ પાડવી.",
            "ઓછા વ્યાજ દરે લોન પૂરી પાડવા માટે ગ્રામીણ બેંકો, સહકારી મંડળીઓ અને કિસાન ક્રેડિટ કાર્ડ (KCC) ની સ્થાપના.",
            "ટ્રેક્ટરના ઉપયોગ પર પ્રતિબંધ મૂકવો અને ખેડૂતોને માત્ર બળદનો ઉપયોગ કરવા કહેવું.",
            "વિદેશી કૃષિ આયાત પરના તમામ કર દૂર કરવા."
        ],
        "correct_index": 1,
        "explanation": "To help farmers, the government introduced several institutional reforms in the 1980s and 1990s. These included provision for crop insurance against drought, flood, fire and disease, establishment of Grameen banks, cooperative societies and banks for providing loan facilities to the farmers at lower rates of interest. Kissan Credit Card (KCC) was also introduced.",
        "explanation_hi": "किसानों की मदद के लिए, सरकार ने 1980 और 1990 के दशक में कई संस्थागत सुधार पेश किए। इनमें सूखे, बाढ़, आग और बीमारी के खिलाफ फसल बीमा (crop insurance) का प्रावधान, किसानों को कम ब्याज दरों पर ऋण सुविधा प्रदान करने के लिए ग्रामीण बैंकों, सहकारी समितियों और बैंकों की स्थापना शामिल थी। किसान क्रेडिट कार्ड (KCC) भी पेश किया गया था।",
        "explanation_gu": "ખેડૂતોને મદદ કરવા માટે, સરકારે 1980 અને 1990 ના દાયકામાં ઘણા સંસ્થાકીય સુધારાઓ રજૂ કર્યા. આમાં દુષ્કાળ, પૂર, આગ અને રોગ સામે પાક વીમાની (crop insurance) જોગવાઈ, ખેડૂતોને ઓછા વ્યાજ દરે લોનની સુવિધા પૂરી પાડવા માટે ગ્રામીણ બેંકો, સહકારી મંડળીઓ અને બેંકોની સ્થાપનાનો સમાવેશ થાય છે. કિસાન ક્રેડિટ કાર્ડ (KCC) પણ રજૂ કરવામાં આવ્યું હતું."
    },
    {
        "id": "KOBJ_NCERT_C10_GEOG_CH4_006",
        "type": "mcq",
        "title": "NCERT Exercise Q1_i",
        "title_hi": "NCERT अभ्यास Q1_i",
        "title_gu": "NCERT સ્વાધ્યાય Q1_i",
        "question": "Which one of the following describes a system of agriculture where a single crop is grown on a large area?",
        "question_hi": "निम्नलिखित में से कौन कृषि की एक प्रणाली का वर्णन करता है जहां एक बड़े क्षेत्र में एकल फसल (single crop) उगाई जाती है?",
        "question_gu": "નીચેનામાંથી કયું ખેતીની એવી સિસ્ટમનું વર્ણન કરે છે જ્યાં મોટા વિસ્તાર પર એક જ પાક (single crop) ઉગાડવામાં આવે છે?",
        "options": [
            "Shifting Agriculture",
            "Plantation Agriculture",
            "Horticulture",
            "Intensive Agriculture"
        ],
        "options_hi": [
            "स्थानांतरित कृषि (Shifting Agriculture)",
            "वृक्षारोपण कृषि (Plantation Agriculture)",
            "बागवानी (Horticulture)",
            "गहन कृषि (Intensive Agriculture)"
        ],
        "options_gu": [
            "સ્થળાંતરિત ખેતી (Shifting Agriculture)",
            "બાગાયતી ખેતી (Plantation Agriculture)",
            "બાગાયત (Horticulture)",
            "સઘન ખેતી (Intensive Agriculture)"
        ],
        "correct_index": 1,
        "explanation": "Plantation is a type of commercial farming where a single crop is grown on a large area. Examples include tea plantations in Assam or rubber plantations in Kerala.",
        "explanation_hi": "वृक्षारोपण (Plantation) एक प्रकार की व्यावसायिक खेती है जहां एक बड़े क्षेत्र में एकल फसल उगाई जाती है। उदाहरणों में असम में चाय के बागान या केरल में रबर के बागान शामिल हैं।",
        "explanation_gu": "બાગાયતી ખેતી (Plantation) એ વ્યાપારી ખેતીનો એક પ્રકાર છે જ્યાં મોટા વિસ્તારમાં એક જ પાક ઉગાડવામાં આવે છે. ઉદાહરણોમાં આસામમાં ચાના બગીચા અથવા કેરળમાં રબરના બગીચા સામેલ છે."
    },
    {
        "id": "KOBJ_NCERT_C10_GEOG_CH4_007",
        "type": "mcq",
        "title": "NCERT Exercise Q1_ii",
        "title_hi": "NCERT अभ्यास Q1_ii",
        "title_gu": "NCERT સ્વાધ્યાય Q1_ii",
        "question": "Which one of the following is a rabi crop?",
        "question_hi": "निम्नलिखित में से कौन सी एक रबी फसल है?",
        "question_gu": "નીચેનામાંથી કયો રવિ પાક છે?",
        "options": [
            "Rice",
            "Gram",
            "Millets",
            "Cotton"
        ],
        "options_hi": [
            "चावल",
            "चना",
            "बाजरा",
            "कपास"
        ],
        "options_gu": [
            "ચોખા",
            "ચણા",
            "બાજરી",
            "કપાસ"
        ],
        "correct_index": 1,
        "explanation": "Gram (Chana) is a rabi crop, sown in winter from October to December and harvested in summer. Rice, millets, and cotton are kharif crops grown during the monsoon.",
        "explanation_hi": "चना (Gram) एक रबी फसल है, जिसे सर्दियों में अक्टूबर से दिसंबर तक बोया जाता है और गर्मियों में काटा जाता है। चावल, बाजरा और कपास मानसून के दौरान उगाई जाने वाली खरीफ फसलें हैं।",
        "explanation_gu": "ચણા (Gram) એ રવિ પાક છે, જે શિયાળામાં ઓક્ટોબરથી ડિસેમ્બર સુધી વાવવામાં આવે છે અને ઉનાળામાં લણવામાં આવે છે. ચોખા, બાજરી અને કપાસ ચોમાસા દરમિયાન ઉગાડવામાં આવતા ખરીફ પાકો છે."
    },
    {
        "id": "KOBJ_NCERT_C10_GEOG_CH4_008",
        "type": "mcq",
        "title": "NCERT Exercise Q1_iii",
        "title_hi": "NCERT अभ्यास Q1_iii",
        "title_gu": "NCERT સ્વાધ્યાય Q1_iii",
        "question": "Which one of the following is a leguminous crop?",
        "question_hi": "निम्नलिखित में से कौन सी फलीदार (leguminous) फसल है?",
        "question_gu": "નીચેનામાંથી કયો કઠોળ (leguminous) પાક છે?",
        "options": [
            "Pulses",
            "Jawar",
            "Millets",
            "Sesamum"
        ],
        "options_hi": [
            "दालें (Pulses)",
            "ज्वार",
            "बाजरा",
            "तिल (Sesamum)"
        ],
        "options_gu": [
            "કઠોળ (Pulses)",
            "જુવાર",
            "બાજરી",
            "તલ (Sesamum)"
        ],
        "correct_index": 0,
        "explanation": "Pulses (like tur, urad, moong, masur, peas and gram) are leguminous crops. Except for arhar, all these crops help in restoring soil fertility by fixing nitrogen from the air.",
        "explanation_hi": "दालें (जैसे अरहर, उड़द, मूंग, मसूर, मटर और चना) फलीदार फसलें हैं। अरहर को छोड़कर, ये सभी फसलें हवा से नाइट्रोजन को ठीक करके मिट्टी की उर्वरता बहाल करने में मदद करती हैं।",
        "explanation_gu": "કઠોળ (જેમ કે તુવેર, અડદ, મગ, મસૂર, વટાણા અને ચણા) કઠોળ વર્ગના પાક છે. તુવેર સિવાય, આ તમામ પાકો હવામાંથી નાઇટ્રોજન મેળવીને જમીનની ફળદ્રુપતા પુનઃસ્થાપિત કરવામાં મદદ કરે છે."
    },
    {
        "id": "KOBJ_NCERT_C10_GEOG_CH4_009",
        "type": "mcq",
        "title": "NCERT Exercise Q1_iv",
        "title_hi": "NCERT अभ्यास Q1_iv",
        "title_gu": "NCERT સ્વાધ્યાય Q1_iv",
        "question": "Which one of the following is announced by the government in support of a crop?",
        "question_hi": "किसी फसल के समर्थन में सरकार द्वारा निम्नलिखित में से किसकी घोषणा की जाती है?",
        "question_gu": "પાકના સમર્થનમાં સરકાર દ્વારા નીચેનામાંથી કઈ જાહેરાત કરવામાં આવે છે?",
        "options": [
            "Maximum support price",
            "Minimum support price",
            "Moderate support price",
            "Influential support price"
        ],
        "options_hi": [
            "अधिकतम समर्थन मूल्य",
            "न्यूनतम समर्थन मूल्य (Minimum support price)",
            "मध्यम समर्थन मूल्य",
            "प्रभावशाली समर्थन मूल्य"
        ],
        "options_gu": [
            "મહત્તમ ટેકાના ભાવ",
            "લઘુત્તમ ટેકાના ભાવ (Minimum support price)",
            "મધ્યમ ટેકાના ભાવ",
            "પ્રભાવશાળી ટેકાના ભાવ"
        ],
        "correct_index": 1,
        "explanation": "The government announces the Minimum Support Price (MSP), remunerative and procurement prices for important crops to check the exploitation of farmers by speculators and middlemen.",
        "explanation_hi": "सरकार सट्टेबाजों और बिचौलियों द्वारा किसानों के शोषण को रोकने के लिए महत्वपूर्ण फसलों के लिए न्यूनतम समर्थन मूल्य (MSP), पारिश्रमिक और खरीद मूल्य की घोषणा करती है।",
        "explanation_gu": "સરકાર સટોડિયાઓ અને વચેટિયાઓ દ્વારા ખેડૂતોના શોષણને રોકવા માટે મહત્વપૂર્ણ પાકો માટે લઘુત્તમ ટેકાના ભાવ (MSP), મહેનતાણું અને પ્રાપ્તિ કિંમતોની જાહેરાત કરે છે."
    }
]

data = {
    "metadata": {
        "id": "ncert_class10_geography_ch4",
        "title": "Geography Chapter 4: Agriculture",
        "subject": "Social Science",
        "grade": "10"
    },
    "blocks": blocks
}

output_path = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_geography_ch4.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Successfully wrote {len(blocks)} blocks to {output_path}")
