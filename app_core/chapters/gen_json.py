import json
import os

data = {
    "id": "KOBJ_GSEB_12_EN_SUP_CH11",
    "title_en": "I Keep My Tryst with Everest",
    "title_hi": "मैं एवरेस्ट (Everest) के साथ अपनी भेंट रखता हूँ",
    "title_gu": "હું એવરેસ્ટ (Everest) સાથે મારી મુલાકાત રાખું છું",
    "class_level": 12,
    "subject": "English",
    "board": "GSEB",
    "blocks": [
        {
            "id": "KOBJ_GSEB_12_EN_SUP_CH11_HOOK",
            "type": "theory",
            "subtype": "hook",
            "title_en": "The Ultimate Challenge",
            "title_hi": "अंतिम चुनौती (Ultimate Challenge)",
            "title_gu": "અંતિમ પડકાર (Ultimate Challenge)",
            "body_en": "Imagine waking up at 4:00 a.m. on the highest mountain in the world, melting snow just to make tea. Outside, the wind is howling and the temperature is deadly cold. This is exactly what Bachendri Pal experienced on her way to the summit of Mount Everest. Let's find out how she conquered the peak!",
            "body_hi": "कल्पना कीजिए कि आप दुनिया के सबसे ऊंचे पहाड़ पर सुबह 4:00 बजे उठते हैं, और चाय बनाने के लिए बर्फ पिघलाते हैं। बाहर, हवा चल रही है और तापमान बेहद ठंडा है। बछेंद्री पाल (Bachendri Pal) ने माउंट एवरेस्ट (Mount Everest) के शिखर पर जाते समय ठीक ऐसा ही अनुभव किया था। आइए जानें कि उन्होंने चोटी पर कैसे विजय प्राप्त की!",
            "body_gu": "કલ્પના કરો કે તમે વિશ્વના સૌથી ઊંચા પર્વત પર સવારે 4:00 વાગ્યે ઉઠો છો, અને ચા બનાવવા માટે બરફ ઓગાળો છો. બહાર, પવન ફૂંકાય છે અને તાપમાન ખૂબ ઠંડુ છે. બચેન્દ્રી પાલ (Bachendri Pal) એ માઉન્ટ એવરેસ્ટ (Mount Everest) ના શિખર પર જતા સમયે બરાબર આવો જ અનુભવ કર્યો હતો. ચાલો જાણીએ કે તેમણે શિખર પર કેવી રીતે વિજય મેળવ્યો!"
        },
        {
            "id": "KOBJ_GSEB_12_EN_SUP_CH11_SOCRATIC",
            "type": "theory",
            "subtype": "socratic_question",
            "title_en": "Think About It",
            "title_hi": "इसके बारे में सोचें (Think About It)",
            "title_gu": "આના વિશે વિચારો (Think About It)",
            "body_en": "Why do you think climbers need to carry oxygen cylinders, and what would happen if someone decided to climb without one?",
            "body_hi": "आपको क्या लगता है कि पर्वतारोहियों को ऑक्सीजन सिलेंडर ले जाने की आवश्यकता क्यों है, और क्या होगा यदि कोई बिना ऑक्सीजन सिलेंडर के चढ़ने का फैसला करे?",
            "body_gu": "તમને શું લાગે છે કે પર્વતારોહકોને ઓક્સિજન સિલિન્ડર સાથે રાખવાની જરૂર કેમ પડે છે, અને જો કોઈ ઓક્સિજન સિલિન્ડર વિના ચઢવાનું નક્કી કરે તો શું થશે?"
        },
        {
            "id": "KOBJ_GSEB_12_EN_SUP_CH11_DISCOVERY",
            "type": "theory",
            "subtype": "discovery",
            "title_en": "The Freezing Reality",
            "title_hi": "जमा देने वाली वास्तविकता (Freezing Reality)",
            "title_gu": "ઠંડી વાસ્તવિકતા (Freezing Reality)",
            "body_en": "At extreme heights, the air is thin and the cold is intense. A climber without oxygen might suffer from frostbite, where their feet and hands get too cold, forcing them to turn back quickly to survive.",
            "body_hi": "अत्यधिक ऊंचाइयों पर, हवा पतली होती है और ठंड तीव्र होती है। ऑक्सीजन के बिना एक पर्वतारोही फ्रॉस्टबाइट (frostbite) से पीड़ित हो सकता है, जहां उनके पैर और हाथ बहुत ठंडे हो जाते हैं, जिससे उन्हें जीवित रहने के लिए जल्दी वापस लौटने के लिए मजबूर होना पड़ता है।",
            "body_gu": "ખૂબ ઊંચાઈ પર, હવા પાતળી હોય છે અને ઠંડી તીવ્ર હોય છે. ઓક્સિજન વિના પર્વતારોહક હિમ ડંખ (frostbite) થી પીડાઈ શકે છે, જ્યાં તેમના પગ અને હાથ ખૂબ ઠંડા થઈ જાય છે, જેનાથી તેમને જીવિત રહેવા માટે ઝડપથી પાછા ફરવાની ફરજ પડે છે."
        },
        {
            "id": "KOBJ_GSEB_12_EN_SUP_CH11_REVEAL",
            "type": "theory",
            "subtype": "reveal",
            "title_en": "The Final Climb",
            "title_hi": "अंतिम चढ़ाई (Final Climb)",
            "title_gu": "અંતિમ ચઢાઈ (Final Climb)",
            "body_en": "Bachendri Pal left her tent at 5:30 a.m. with Ang Dorjee, who was climbing without oxygen. They faced steep frozen slopes hard as glass and had to use ice-axes. Lhatoo joined them, bringing a rope for balance and increasing Bachendri's oxygen flow, which made the steep stretches easier. After battling strong winds and icy powder snow near the South Summit and Hillary's Step, the slope eased off. At 1:07 p.m. on 23 May, 1984, she stood on top of Everest, becoming the first Indian woman to achieve this feat.",
            "body_hi": "बछेंद्री पाल (Bachendri Pal) सुबह 5:30 बजे अपने टेंट से आंग दोरजी (Ang Dorjee) के साथ निकलीं, जो बिना ऑक्सीजन के चढ़ाई कर रहे थे। उन्होंने कांच की तरह सख्त खड़ी जमी हुई ढलानों का सामना किया और उन्हें कुल्हाड़ी का उपयोग करना पड़ा। ल्हाटू (Lhatoo) उनके साथ जुड़ गए, जो संतुलन के लिए एक रस्सी लाए और बछेंद्री के ऑक्सीजन प्रवाह को बढ़ाया, जिससे खड़ी चढ़ाई आसान हो गई। दक्षिण शिखर (South Summit) और हिलेरी स्टेप (Hillary's Step) के पास तेज हवाओं और बर्फीली पाउडर बर्फ का सामना करने के बाद, ढलान आसान हो गई। 23 मई, 1984 को दोपहर 1:07 बजे, वह एवरेस्ट के शीर्ष पर खड़ी थीं, और यह उपलब्धि हासिल करने वाली पहली भारतीय महिला बन गईं।",
            "body_gu": "બચેન્દ્રી પાલ (Bachendri Pal) સવારે 5:30 વાગ્યે તેમના ટેન્ટમાંથી આંગ દોરજી (Ang Dorjee) સાથે નીકળ્યા, જે ઓક્સિજન વિના ચઢાણ કરી રહ્યા હતા. તેઓએ કાચ જેવા સખત ઢોળાવનો સામનો કરવો પડ્યો અને તેમને કુહાડીનો ઉપયોગ કરવો પડ્યો. લ્હાટુ (Lhatoo) તેમની સાથે જોડાયા, જે સંતુલન માટે એક દોરડું લાવ્યા અને બચેન્દ્રીના ઓક્સિજન પ્રવાહમાં વધારો કર્યો, જેનાથી સખત ચઢાણ સરળ બન્યું. દક્ષિણ શિખર (South Summit) અને હિલેરી સ્ટેપ (Hillary's Step) પાસે ભારે પવન અને બર્ફીલા પાવડર બરફનો સામનો કર્યા પછી, ઢોળાવ સરળ બન્યો. 23 મે, 1984 ના રોજ બપોરે 1:07 વાગ્યે, તેણી એવરેસ્ટની ટોચ પર ઉભી હતી, અને આ સિદ્ધિ મેળવનારી પ્રથમ ભારતીય મહિલા બની."
        },
        {
            "id": "KOBJ_GSEB_12_EN_SUP_CH11_KNOWLEDGE_CHECK",
            "type": "mcq",
            "question_en": "Who climbed without oxygen?",
            "question_hi": "बिना ऑक्सीजन के किसने चढ़ाई की?",
            "question_gu": "ઓક્સિજન વિના કોણે ચઢાણ કર્યું?",
            "options_en": ["Bachendri Pal", "Ang Dorjee", "Lhatoo", "Hillary"],
            "options_hi": ["बछेंद्री पाल", "आंग दोरजी", "ल्हाटू", "हिलेरी"],
            "options_gu": ["બચેન્દ્રી પાલ", "આંગ દોરજી", "લ્હાટુ", "હિલેરી"],
            "correct_index": 1,
            "explanation_en": "Ang Dorjee climbed without oxygen, which made him susceptible to cold feet.",
            "explanation_hi": "आंग दोरजी ने बिना ऑक्सीजन के चढ़ाई की, जिससे उनके पैर ठंडे हो सकते थे।",
            "explanation_gu": "આંગ દોરજીએ ઓક્સિજન વિના ચઢાણ કર્યું, જેનાથી તેમના પગ ઠંડા થઈ શકતા હતા."
        },
        {
            "id": "KOBJ_GSEB_12_EN_SUP_CH11_REFLECTION",
            "type": "theory",
            "subtype": "reflection",
            "title_en": "Self Reflection",
            "title_hi": "आत्म-प्रतिबिंब (Self Reflection)",
            "title_gu": "સ્વ-ચિંતન (Self Reflection)",
            "body_en": "What do you think went through Bachendri Pal's mind when she realized there was no upward climb left and the slope plunged steeply down?",
            "body_hi": "आपको क्या लगता है कि बछेंद्री पाल के मन में क्या चल रहा होगा जब उन्हें एहसास हुआ कि ऊपर चढ़ने के लिए कोई जगह नहीं बची है और ढलान तेजी से नीचे की ओर गिर रही है?",
            "body_gu": "તમને શું લાગે છે કે બચેન્દ્રી પાલના મનમાં શું ચાલતું હશે જ્યારે તેમને સમજાયું કે ઉપર ચઢવા માટે કોઈ જગ્યા બાકી નથી અને ઢોળાવ ઝડપથી નીચેની તરફ જાય છે?"
        },
        {
            "id": "KOBJ_GSEB_12_EN_SUP_CH11_CONNECTION",
            "type": "theory",
            "subtype": "connection",
            "title_en": "Making Connections",
            "title_hi": "संबंध बनाना (Making Connections)",
            "title_gu": "સંબંધો બનાવવા (Making Connections)",
            "body_en": "The determination shown here is similar to many great explorers who risked their lives in extreme conditions, such as those exploring Antarctica or the depths of the oceans.",
            "body_hi": "यहाँ दिखाया गया दृढ़ संकल्प कई महान खोजकर्ताओं के समान है जिन्होंने अत्यधिक परिस्थितियों में अपनी जान जोखिम में डाली, जैसे कि अंटार्कटिका (Antarctica) या महासागरों की गहराई की खोज करने वाले।",
            "body_gu": "અહીં દર્શાવેલ દૃઢ સંકલ્પ ઘણા મહાન સંશોધકો સમાન છે જેમણે અત્યંત મુશ્કેલ પરિસ્થિતિઓમાં પોતાનો જીવ જોખમમાં મૂક્યો, જેમ કે એન્ટાર્કટિકા (Antarctica) અથવા મહાસાગરોની ઊંડાઈની શોધખોળ કરનારા."
        },
        {
            "id": "KOBJ_GSEB_12_EN_SUP_CH11_MASTERY",
            "type": "theory",
            "subtype": "mastery",
            "title_en": "Mastery Challenge",
            "title_hi": "महारत चुनौती (Mastery Challenge)",
            "title_gu": "નિપુણતા પડકાર (Mastery Challenge)",
            "body_en": "Write a short paragraph describing a difficult challenge you have faced and how you overcame it with determination, similar to Bachendri Pal's climb.",
            "body_hi": "एक संक्षिप्त पैराग्राफ लिखें जिसमें आपके द्वारा सामना की गई एक कठिन चुनौती का वर्णन हो और यह भी बताएं कि आपने दृढ़ संकल्प के साथ उस पर कैसे विजय प्राप्त की, बछेंद्री पाल की चढ़ाई के समान।",
            "body_gu": "એક ટૂંકો ફકરો લખો જેમાં તમે સામનો કરેલા મુશ્કેલ પડકારનું વર્ણન હોય અને એ પણ જણાવો કે તમે દૃઢ સંકલ્પ સાથે તેના પર કેવી રીતે વિજય મેળવ્યો, બચેન્દ્રી પાલની ચઢાઈની જેમ."
        },
        {
            "id": "KOBJ_GSEB_12_EN_SUP_CH11_EX1_A_1",
            "type": "theory",
            "title_en": "Exercise 1(A).1",
            "title_hi": "अभ्यास 1(A).1 (Exercise 1(A).1)",
            "title_gu": "સ્વાધ્યાય 1(A).1 (Exercise 1(A).1)",
            "body_en": "Find out words for the following description from the lesson:\n(1) Viewing Mt. Everest Banchendri Pal felt shocked.\nAnswer: thrilled",
            "body_hi": "पाठ से निम्नलिखित विवरण के लिए शब्द खोजें:\n(1) माउंट एवरेस्ट को देखकर बछेंद्री पाल हैरान रह गईं।\nउत्तर: रोमांचित (thrilled)",
            "body_gu": "પાઠમાંથી નીચેના વર્ણન માટે શબ્દો શોધો:\n(1) માઉન્ટ એવરેસ્ટ જોઈને બચેન્દ્રી પાલ આશ્ચર્યચકિત થઈ ગયા.\nજવાબ: રોમાંચિત (thrilled)"
        },
        {
            "id": "KOBJ_GSEB_12_EN_SUP_CH11_EX1_A_2",
            "type": "theory",
            "title_en": "Exercise 1(A).2",
            "title_hi": "अभ्यास 1(A).2 (Exercise 1(A).2)",
            "title_gu": "સ્વાધ્યાય 1(A).2 (Exercise 1(A).2)",
            "body_en": "(2) Ang Dorjee had decided to climb without gas.\nAnswer: oxygen",
            "body_hi": "(2) आंग दोरजी ने बिना गैस के चढ़ने का फैसला किया था।\nउत्तर: ऑक्सीजन (oxygen)",
            "body_gu": "(2) આંગ દોરજીએ ગેસ વિના ચઢવાનું નક્કી કર્યું હતું.\nજવાબ: ઓક્સિજન (oxygen)"
        },
        {
            "id": "KOBJ_GSEB_12_EN_SUP_CH11_EX1_A_3",
            "type": "theory",
            "title_en": "Exercise 1(A).3",
            "title_hi": "अभ्यास 1(A).3 (Exercise 1(A).3)",
            "title_gu": "સ્વાધ્યાય 1(A).3 (Exercise 1(A).3)",
            "body_en": "(3) The steep frozen slopes were hard and brittle they had to use a tool to climb.\nAnswer: ice-axe",
            "body_hi": "(3) खड़ी जमी हुई ढलानें सख्त और भुरभुरी थीं, उन्हें चढ़ने के लिए एक उपकरण का उपयोग करना पड़ा।\nउत्तर: कुल्हाड़ी (ice-axe)",
            "body_gu": "(3) સખત ઢોળાવ સખત અને બરડ હતો, તેઓને ચઢવા માટે એક સાધનનો ઉપયોગ કરવો પડ્યો.\nજવાબ: કુહાડી (ice-axe)"
        },
        {
            "id": "KOBJ_GSEB_12_EN_SUP_CH11_EX1_A_4",
            "type": "theory",
            "title_en": "Exercise 1(A).4",
            "title_hi": "अभ्यास 1(A).4 (Exercise 1(A).4)",
            "title_gu": "સ્વાધ્યાય 1(A).4 (Exercise 1(A).4)",
            "body_en": "(4) Lhatoo had brought a thick string.\nAnswer: nylon rope",
            "body_hi": "(4) ल्हाटू एक मोटा तार (स्ट्रिंग) लाया था।\nउत्तर: नायलॉन की रस्सी (nylon rope)",
            "body_gu": "(4) લ્હાટુ જાડી દોરી લાવ્યા હતા.\nજવાબ: નાયલોન દોરડું (nylon rope)"
        },
        {
            "id": "KOBJ_GSEB_12_EN_SUP_CH11_EX1_A_5",
            "type": "theory",
            "title_en": "Exercise 1(A).5",
            "title_hi": "अभ्यास 1(A).5 (Exercise 1(A).5)",
            "title_gu": "સ્વાધ્યાય 1(A).5 (Exercise 1(A).5)",
            "body_en": "(5) Beyond the south summit the breeze rise.\nAnswer: increased",
            "body_hi": "(5) दक्षिण शिखर के परे हवा तेज हो गई।\nउत्तर: बढ़ गई (increased)",
            "body_gu": "(5) દક્ષિણ શિખરની બહાર પવન વધ્યો.\nજવાબ: વધ્યો (increased)"
        },
        {
            "id": "KOBJ_GSEB_12_EN_SUP_CH11_EX1_B_1",
            "type": "theory",
            "title_en": "Exercise 1(B)",
            "title_hi": "अभ्यास 1(B) (Exercise 1(B))",
            "title_gu": "સ્વાધ્યાય 1(B) (Exercise 1(B))",
            "body_en": "Find the opposite words and use them both in a sentence:\n1. terrify x comfort\n2. avoid x confront\n3. near x far\n4. erect x crouch\n5. exposure x protection\n6. hard x soft\n7. melt x freeze\n8. thrilled x bored\n9. secure x loose\n10. deep x shallow",
            "body_hi": "विपरीत शब्द खोजें और दोनों का वाक्य में उपयोग करें:\n1. डराना (terrify) x आराम देना (comfort)\n2. बचना (avoid) x सामना करना (confront)\n3. पास (near) x दूर (far)\n4. सीधा खड़ा होना (erect) x झुकना (crouch)\n5. जोखिम (exposure) x सुरक्षा (protection)\n6. कठोर (hard) x नरम (soft)\n7. पिघलना (melt) x जमना (freeze)\n8. रोमांचित (thrilled) x ऊबा हुआ (bored)\n9. सुरक्षित (secure) x ढीला (loose)\n10. गहरा (deep) x उथला (shallow)",
            "body_gu": "વિરોધી શબ્દો શોધો અને બંનેનો વાક્યમાં ઉપયોગ કરો:\n1. ડરાવવું (terrify) x આરામ આપવો (comfort)\n2. ટાળવું (avoid) x સામનો કરવો (confront)\n3. નજીક (near) x દૂર (far)\n4. સીધા ઉભા રહેવું (erect) x ઝૂકવું (crouch)\n5. જોખમ (exposure) x રક્ષણ (protection)\n6. સખત (hard) x નરમ (soft)\n7. ઓગળવું (melt) x જામી જવું (freeze)\n8. રોમાંચિત (thrilled) x કંટાળેલું (bored)\n9. સુરક્ષિત (secure) x ઢીલું (loose)\n10. ઊંડું (deep) x છીછરું (shallow)"
        },
        {
            "id": "KOBJ_GSEB_12_EN_SUP_CH11_EX2_A_1",
            "type": "theory",
            "title_en": "Exercise 2(A).1",
            "title_hi": "अभ्यास 2(A).1 (Exercise 2(A).1)",
            "title_gu": "સ્વાધ્યાય 2(A).1 (Exercise 2(A).1)",
            "body_en": "Answer the following questions:\n(1) What would happen to Ang Dorjee if he climbed without oxygen?\nAnswer: If he climbed without oxygen, his feet would get very cold, making him vulnerable to frostbite.",
            "body_hi": "निम्नलिखित प्रश्नों के उत्तर दें:\n(1) आंग दोरजी के बिना ऑक्सीजन के चढ़ने पर क्या होगा?\nउत्तर: यदि वह बिना ऑक्सीजन के चढ़ते, तो उनके पैर बहुत ठंडे हो जाते, जिससे उन्हें फ्रॉस्टबाइट का खतरा होता।",
            "body_gu": "નીચેના પ્રશ્નોના જવાબ આપો:\n(1) જો આંગ દોરજી ઓક્સિજન વિના ચઢે તો શું થશે?\nજવાબ: જો તે ઓક્સિજન વિના ચઢે, તો તેમના પગ ખૂબ ઠંડા થઈ જશે, જેનાથી તેમને હિમ ડંખનો ખતરો રહેશે."
        },
        {
            "id": "KOBJ_GSEB_12_EN_SUP_CH11_EX2_A_2",
            "type": "theory",
            "title_en": "Exercise 2(A).2",
            "title_hi": "अभ्यास 2(A).2 (Exercise 2(A).2)",
            "title_gu": "સ્વાધ્યાય 2(A).2 (Exercise 2(A).2)",
            "body_en": "(2) What would he have to do?\nAnswer: He had to either get to the peak and back to the South Col the same day or abandon the attempt.",
            "body_hi": "(2) उसे क्या करना होगा?\nउत्तर: उसे या तो उसी दिन चोटी पर पहुंचकर वापस साउथ कोल (South Col) आना था या प्रयास छोड़ना था।",
            "body_gu": "(2) તેણે શું કરવું પડશે?\nજવાબ: તેણે કાં તો તે જ દિવસે શિખર પર પહોંચીને પાછા સાઉથ કોલ (South Col) આવવું પડશે અથવા પ્રયાસ છોડી દેવો પડશે."
        },
        {
            "id": "KOBJ_GSEB_12_EN_SUP_CH11_EX2_A_3",
            "type": "theory",
            "title_en": "Exercise 2(A).3",
            "title_hi": "अभ्यास 2(A).3 (Exercise 2(A).3)",
            "title_gu": "સ્વાધ્યાય 2(A).3 (Exercise 2(A).3)",
            "body_en": "(3) Describe the climbing of the writer at 6:20.\nAnswer: At 6:20, the writer stepped out from the South Col. It was a perfect day with a gentle breeze but intense cold. She was warm in her climbing gear and climbed unroped, keeping up with Ang Dorjee's steady pace.",
            "body_hi": "(3) 6:20 पर लेखिका की चढ़ाई का वर्णन करें।\nउत्तर: 6:20 पर, लेखिका साउथ कोल से बाहर निकलीं। यह एक सही दिन था, जिसमें हल्की हवा चल रही थी लेकिन ठंड बहुत ज्यादा थी। वह अपने चढ़ने के कपड़ों में गर्म थीं और बिना रस्सी के चढ़ीं, आंग दोरजी की स्थिर गति के साथ।",
            "body_gu": "(3) 6:20 વાગ્યે લેખિકાની ચઢાઈનું વર્ણન કરો.\nજવાબ: 6:20 વાગ્યે, લેખિકા સાઉથ કોલમાંથી બહાર નીકળ્યા. તે એક સારો દિવસ હતો, જેમાં હળવો પવન હતો પણ ઠંડી ખૂબ હતી. તે પોતાના ચઢાણના કપડાંમાં ગરમ ​​હતા અને દોરડા વિના ચઢ્યા, આંગ દોરજીની સ્થિર ગતિ સાથે કદમ મિલાવીને."
        },
        {
            "id": "KOBJ_GSEB_12_EN_SUP_CH11_EX2_A_4",
            "type": "theory",
            "title_en": "Exercise 2(A).4",
            "title_hi": "अभ्यास 2(A).4 (Exercise 2(A).4)",
            "title_gu": "સ્વાધ્યાય 2(A).4 (Exercise 2(A).4)",
            "body_en": "(4) How did Lhatoo help the climbers?\nAnswer: Lhatoo brought a nylon rope for balance and increased the oxygen flow on the writer's regulator, making the steeper stretches easier.",
            "body_hi": "(4) ल्हाटू ने पर्वतारोहियों की कैसे मदद की?\nउत्तर: ल्हाटू संतुलन के लिए नायलॉन की रस्सी लाया और लेखिका के रेगुलेटर पर ऑक्सीजन का प्रवाह बढ़ा दिया, जिससे खड़ी चढ़ाई आसान हो गई।",
            "body_gu": "(4) લ્હાટુએ પર્વતારોહકોને કેવી રીતે મદદ કરી?\nજવાબ: લ્હાટુ સંતુલન માટે નાયલોન દોરડું લાવ્યા અને લેખિકાના રેગ્યુલેટર પર ઓક્સિજનનો પ્રવાહ વધાર્યો, જેનાથી સખત ચઢાણ સરળ બન્યું."
        },
        {
            "id": "KOBJ_GSEB_12_EN_SUP_CH11_EX2_A_5",
            "type": "theory",
            "title_en": "Exercise 2(A).5",
            "title_hi": "अभ्यास 2(A).5 (Exercise 2(A).5)",
            "title_gu": "સ્વાધ્યાય 2(A).5 (Exercise 2(A).5)",
            "body_en": "(5) What special efforts had the writer to make her upward journey beyond the South Summit?\nAnswer: The writer had to get into a crouching position to face the icy wind, dig her ice-axe deep to stand on a knife-edge ridge, and attach her waist-strap to the ice-axe head for security.",
            "body_hi": "(5) दक्षिण शिखर के परे अपनी ऊपर की यात्रा को पूरा करने के लिए लेखिका को क्या विशेष प्रयास करने पड़े?\nउत्तर: बर्फीली हवा का सामना करने के लिए लेखिका को झुकना पड़ा, एक तेज धार वाली चोटी पर खड़े होने के लिए अपनी कुल्हाड़ी को गहराई से गाड़ना पड़ा, और सुरक्षा के लिए कुल्हाड़ी के सिर से अपने कमर-स्ट्रैप को जोड़ना पड़ा।",
            "body_gu": "(5) દક્ષિણ શિખરની બહાર તેમની ઉપરની મુસાફરી પૂર્ણ કરવા માટે લેખિકાએ કયા વિશેષ પ્રયત્નો કરવા પડ્યા?\nજવાબ: બર્ફીલા પવનનો સામનો કરવા માટે લેખિકાએ ઝૂકવું પડ્યું, એક તીક્ષ્ણ ધારવાળી ચોટી પર ઉભા રહેવા માટે પોતાની કુહાડીને ઊંડે સુધી ખોડવી પડી, અને સુરક્ષા માટે કુહાડીના માથા સાથે પોતાના કમર-સ્ટ્રેપને જોડવું પડ્યું."
        },
        {
            "id": "KOBJ_GSEB_12_EN_SUP_CH11_EX2_A_6",
            "type": "theory",
            "title_en": "Exercise 2(A).6",
            "title_hi": "अभ्यास 2(A).6 (Exercise 2(A).6)",
            "title_gu": "સ્વાધ્યાય 2(A).6 (Exercise 2(A).6)",
            "body_en": "(6) When did the writer feel thrilled?\nAnswer: The writer felt thrilled when Ang Dorjee gesticulated towards the top, signaling that the goal was near.",
            "body_hi": "(6) लेखिका को कब रोमांचित महसूस हुआ?\nउत्तर: लेखिका को तब रोमांच महसूस हुआ जब आंग दोरजी ने चोटी की ओर इशारा किया, जो यह संकेत दे रहा था कि लक्ष्य निकट था।",
            "body_gu": "(6) લેખિકાને ક્યારે રોમાંચિત લાગ્યું?\nજવાબ: લેખિકાને ત્યારે રોમાંચિત લાગ્યું જ્યારે આંગ દોરજીએ ટોચ તરફ ઈશારો કર્યો, જે દર્શાવતું હતું કે લક્ષ્ય નજીક છે."
        },
        {
            "id": "KOBJ_GSEB_12_EN_SUP_CH11_EX2_A_7",
            "type": "theory",
            "title_en": "Exercise 2(A).7",
            "title_hi": "अभ्यास 2(A).7 (Exercise 2(A).7)",
            "title_gu": "સ્વાધ્યાય 2(A).7 (Exercise 2(A).7)",
            "body_en": "(7) How did she complete the remaining climbing to the peak?\nAnswer: With renewed vigour, she climbed the rest quickly as the snow was softer there. They trudged in heavy powder snow until the slope plunged steeply down, signifying she had reached the top.",
            "body_hi": "(7) उसने चोटी तक की शेष चढ़ाई कैसे पूरी की?\nउत्तर: नए जोश के साथ, उसने बाकी की चढ़ाई जल्दी पूरी की क्योंकि वहां बर्फ नरम थी। वे भारी पाउडर वाली बर्फ में चलते रहे जब तक कि ढलान तेजी से नीचे की ओर नहीं गिरने लगी, जिसका अर्थ था कि वह चोटी पर पहुंच गई थी।",
            "body_gu": "(7) તેણે શિખર સુધીની બાકીની ચઢાઈ કેવી રીતે પૂરી કરી?\nજવાબ: નવા ઉત્સાહ સાથે, તેણે બાકીની ચઢાઈ ઝડપથી પૂરી કરી કારણ કે ત્યાં બરફ નરમ હતો. તેઓ ભારે પાવડર વાળા બરફમાં ચાલતા રહ્યા જ્યાં સુધી ઢોળાવ ઝડપથી નીચેની તરફ ન જવા લાગ્યો, જેનો અર્થ હતો કે તે ટોચ પર પહોંચી ગઈ છે."
        },
        {
            "id": "KOBJ_GSEB_12_EN_SUP_CH11_EX2_B",
            "type": "theory",
            "title_en": "Exercise 2(B)",
            "title_hi": "अभ्यास 2(B) (Exercise 2(B))",
            "title_gu": "સ્વાધ્યાય 2(B) (Exercise 2(B))",
            "body_en": "Number the sentences and join them for the writer's vertical climbing Mt. Everest:\nCorrect sequence: \n4. Ang Dorjee was standing outside.\n5. Beside no one else was ready to move at that time.\n2. I took every step very deliberately on the dangerous stretches.\n6. After drinking some tea, we moved on.\n1. The goal was near.\n7. We trudged in the heavy powder snow for sometime.\n3. My heart stood still.",
            "body_hi": "वाक्यों को क्रमबद्ध करें और लेखिका की माउंट एवरेस्ट की खड़ी चढ़ाई के लिए उन्हें जोड़ें:\nसही क्रम:\n4. आंग दोरजी बाहर खड़े थे।\n5. इसके अलावा उस समय कोई और चलने को तैयार नहीं था।\n2. मैंने खतरनाक रास्तों पर हर कदम बहुत सोच-समझकर उठाया।\n6. कुछ चाय पीने के बाद, हम आगे बढ़े।\n1. लक्ष्य निकट था।\n7. हम कुछ समय के लिए भारी पाउडर बर्फ में चले।\n3. मेरा दिल ठहर गया।",
            "body_gu": "વાક્યોને ક્રમમાં ગોઠવો અને લેખિકાની માઉન્ટ એવરેસ્ટની ચઢાઈ માટે તેમને જોડો:\nસાચો ક્રમ:\n4. આંગ દોરજી બહાર ઉભા હતા.\n5. આ ઉપરાંત તે સમયે બીજું કોઈ ચાલવા તૈયાર નહોતું.\n2. મેં ખતરનાક રસ્તાઓ પર દરેક પગલું ખૂબ જ સમજી વિચારીને ભર્યું.\n6. થોડી ચા પીધા પછી, અમે આગળ વધ્યા.\n1. લક્ષ્ય નજીક હતું.\n7. અમે થોડા સમય માટે ભારે પાવડર બરફમાં ચાલ્યા.\n3. મારું હૃદય થંભી ગયું."
        }
    ]
}

with open('/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class12_english_sup_ch11.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
