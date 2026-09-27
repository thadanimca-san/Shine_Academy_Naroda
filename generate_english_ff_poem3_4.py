import json
import os

# POEM 3: A Tiger in the Zoo
poem3_blocks = [
    {
        "id": "KOBJ_NCERT_C10_ENG_FFP_P3_001",
        "type": "hook",
        "title": "A King Behind Bars",
        "title_hi": "सलाखों के पीछे एक राजा",
        "title_gu": "સળિયા પાછળ એક રાજા",
        "body": "When you visit a zoo, you might see a majestic tiger pacing back and forth in a small concrete cage. Have you ever wondered what the tiger is thinking? In the poem 'A Tiger in the Zoo', poet Leslie Norris contrasts the life of a tiger trapped in a cage with the life it should have been living in the wild jungle. The poem makes us feel the silent anger and helplessness of a powerful animal that has been locked up just for human entertainment.",
        "body_hi": "जब आप चिड़ियाघर (zoo) जाते हैं, तो आपको एक छोटे कंक्रीट के पिंजरे में एक राजसी बाघ (majestic tiger) इधर-उधर घूमता हुआ दिखाई दे सकता है। क्या आपने कभी सोचा है कि बाघ क्या सोच रहा है? कविता 'ए टाइगर इन द ज़ू' (A Tiger in the Zoo) में, कवि लेस्ली नोरिस (Leslie Norris) पिंजरे में फंसे बाघ के जीवन की तुलना उस जीवन से करते हैं जो उसे जंगली जंगल में जीना चाहिए था। कविता हमें एक शक्तिशाली जानवर के मूक क्रोध (silent anger) और लाचारी का एहसास कराती है जिसे केवल मानवीय मनोरंजन (human entertainment) के लिए बंद कर दिया गया है।",
        "body_gu": "જ્યારે તમે પ્રાણી સંગ્રહાલયની (zoo) મુલાકાત લો છો, ત્યારે તમે નાના કોંક્રિટ પાંજરામાં એક જાજરમાન વાઘને (majestic tiger) આગળ પાછળ ફરતો જોઈ શકો છો. શું તમે ક્યારેય વિચાર્યું છે કે વાઘ શું વિચારી રહ્યો છે? 'અ ટાઇગર ઇન ધ ઝૂ' (A Tiger in the Zoo) કવિતામાં, કવિ લેસ્લી નોરિસ (Leslie Norris) પાંજરામાં ફસાયેલા વાઘના જીવનની તુલના તેના જંગલી જંગલમાં રહેતા જીવન સાથે કરે છે. કવિતા આપણને શક્તિશાળી પ્રાણીના શાંત ગુસ્સા (silent anger) અને લાચારીનો અનુભવ કરાવે છે જેને માત્ર માનવ મનોરંજન (human entertainment) માટે બંધ કરી દેવામાં આવ્યું છે."
    },
    {
        "id": "KOBJ_NCERT_C10_ENG_FFP_P3_002",
        "type": "theory",
        "title": "Life in the Cage vs. Life in the Wild",
        "title_hi": "पिंजरे में जीवन बनाम जंगल में जीवन",
        "title_gu": "પાંજરામાં જીવન વિ. જંગલમાં જીવન",
        "body": "In the zoo, the tiger stalks in his vivid stripes, taking only a few steps in his cage. He walks quietly on his velvet pads, but inside he is full of 'quiet rage' (silent anger) because his freedom has been taken away.\nThe poet says that in the wild, this tiger should be lurking in the shadows, sliding through long grass near the water hole, waiting to hunt a plump deer. He should be snarling around houses at the edge of the jungle, showing his white fangs and terrorising the village! \nInstead, his strength is locked behind bars. He ignores the visitors and spends his night staring at the brilliant stars, perhaps dreaming of the freedom he lost.",
        "body_hi": "चिड़ियाघर में, बाघ अपनी चमकीली धारियों (vivid stripes) में शान से चलता है, अपने पिंजरे में केवल कुछ कदम चलता है। वह अपने मखमली गद्दों (velvet pads - पंजों) पर चुपचाप चलता है, लेकिन अंदर ही अंदर वह 'शांत क्रोध' (quiet rage) से भरा होता है क्योंकि उसकी आज़ादी छीन ली गई है।\nकवि का कहना है कि जंगल में, इस बाघ को परछाइयों में दुबक कर (lurking), पानी के छेद के पास लंबी घास से फिसलते हुए, एक मोटे हिरण (plump deer) के शिकार का इंतजार करना चाहिए। उसे जंगल के किनारे घरों के आसपास गुर्राना (snarling) चाहिए, अपने सफेद नुकीले दांत (white fangs) दिखाना चाहिए और गांव को आतंकित (terrorising) करना चाहिए!\nइसके बजाय, उसकी ताकत सलाखों के पीछे बंद है। वह आगंतुकों (visitors) को नजरअंदाज करता है और अपनी रात चमकदार सितारों को घूरते हुए बिताता है, शायद उस स्वतंत्रता का सपना देखता है जो उसने खो दी है।",
        "body_gu": "પ્રાણી સંગ્રહાલયમાં, વાઘ તેના પાંજરામાં માત્ર થોડાં પગલાં ભરીને તેના આબેહૂબ પટ્ટાઓમાં (vivid stripes) દાંડી કરે છે. તે તેના મખમલી ગાદીવાળા પગ (velvet pads) પર ચુપચાપ ચાલે છે, પરંતુ અંદર તે 'શાંત ગુસ્સા' (quiet rage) થી ભરેલો છે કારણ કે તેની સ્વતંત્રતા છીનવાઈ ગઈ છે.\nકવિ કહે છે કે જંગલમાં, આ વાઘ પડછાયામાં છુપાયેલો (lurking) હોવો જોઈએ, પાણીના છિદ્રની નજીકના લાંબા ઘાસમાંથી સરકતો હોવો જોઈએ, અને ભરાવદાર હરણનો (plump deer) શિકાર કરવાની રાહ જોતો હોવો જોઈએ. તેણે જંગલની કિનારે ઘરોની આસપાસ ઘૂરકિયાં (snarling) મારવા જોઈએ, તેના સફેદ દાંત (white fangs) બતાવવા જોઈએ અને ગામને આતંકિત (terrorising) કરવું જોઈએ!\nતેના બદલે, તેની તાકાત સળિયા પાછળ બંધ છે. તે મુલાકાતીઓને (visitors) અવગણે છે અને તેની રાત તેજસ્વી તારાઓ તરફ તાકીને વિતાવે છે, કદાચ તેણે ગુમાવેલી સ્વતંત્રતાનું સ્વપ્ન જોયું છે."
    },
    {
        "id": "KOBJ_NCERT_C10_ENG_FFP_P3_003",
        "type": "mcq",
        "title": "NCERT Exercise Q: Quiet Rage",
        "title_hi": "NCERT अभ्यास Q: शांत क्रोध (Quiet Rage)",
        "title_gu": "NCERT સ્વાધ્યાય Q: શાંત ક્રોધ (Quiet Rage)",
        "question": "Why is the tiger in a 'quiet rage'?",
        "question_hi": "बाघ 'शांत क्रोध' (quiet rage) में क्यों है?",
        "question_gu": "વાઘ શા માટે 'શાંત ક્રોધ' (quiet rage) માં છે?",
        "options": [
            "Because he is hungry and the zookeeper hasn't fed him.",
            "Because he is full of anger at being locked in a cage, but he is helpless and cannot show his power.",
            "Because the visitors are throwing stones at him.",
            "Because he wants to sleep but it is too noisy."
        ],
        "options_hi": [
            "क्योंकि वह भूखा है और चिड़ियाघर के रखवाले ने उसे खाना नहीं दिया है।",
            "क्योंकि वह पिंजरे में बंद होने के कारण क्रोध से भरा है, लेकिन वह असहाय (helpless) है और अपनी शक्ति नहीं दिखा सकता है।",
            "क्योंकि आगंतुक उस पर पत्थर फेंक रहे हैं।",
            "क्योंकि वह सोना चाहता है लेकिन बहुत शोर है।"
        ],
        "options_gu": [
            "કારણ કે તે ભૂખ્યો છે અને ઝૂકીપરે તેને ખવડાવ્યું નથી.",
            "કારણ કે તે પાંજરામાં બંધ હોવાના ગુસ્સાથી ભરેલો છે, પરંતુ તે અસહાય (helpless) છે અને પોતાની શક્તિ બતાવી શકતો નથી.",
            "કારણ કે મુલાકાતીઓ તેના પર પથ્થર ફેંકી રહ્યા છે.",
            "કારણ કે તે સૂવા માંગે છે પરંતુ ખૂબ ઘોંઘાટ છે."
        ],
        "correct_index": 1,
        "explanation": "The tiger is in a 'quiet rage' because he is a ferocious and powerful animal, but he is trapped behind the bars of a small concrete cell. He is full of anger (rage) about losing his freedom, but he is helpless and cannot do anything about it, so he keeps his anger 'quiet'.",
        "explanation_hi": "बाघ 'शांत क्रोध' में है क्योंकि वह एक खूंखार और शक्तिशाली जानवर है, लेकिन वह एक छोटी कंक्रीट की कोठरी की सलाखों के पीछे फंसा हुआ है। वह अपनी आज़ादी खोने के कारण गुस्से (rage) से भरा हुआ है, लेकिन वह असहाय है और इसके बारे में कुछ नहीं कर सकता, इसलिए वह अपना गुस्सा 'शांत' (quiet) रखता है।",
        "explanation_gu": "વાઘ 'શાંત ક્રોધ' માં છે કારણ કે તે એક ક્રૂર અને શક્તિશાળી પ્રાણી છે, પરંતુ તે નાના કોંક્રિટ કોષના સળિયા પાછળ ફસાયેલો છે. તે પોતાની સ્વતંત્રતા ગુમાવવાના ગુસ્સાથી (rage) ભરેલો છે, પરંતુ તે લાચાર છે અને તેના વિશે કંઈ કરી શકતો નથી, તેથી તે પોતાનો ગુસ્સો 'શાંત' (quiet) રાખે છે."
    }
]

# POEM 4: How to Tell Wild Animals
poem4_blocks = [
    {
        "id": "KOBJ_NCERT_C10_ENG_FFP_P4_001",
        "type": "hook",
        "title": "A Funny Guide to Wild Animals",
        "title_hi": "जंगली जानवरों के लिए एक मज़ेदार मार्गदर्शिका (Guide)",
        "title_gu": "જંગલી પ્રાણીઓ માટે એક રમુજી માર્ગદર્શિકા (Guide)",
        "body": "If you are walking in the jungle, how do you know if the animal standing in front of you is a lion or a tiger? Poet Carolyn Wells has written a very funny poem to help you out! She suggests some highly dangerous and humorous ways to identify wild animals. For example, her rule is: if an animal roars so loudly that you are dying of fear, it's a lion! And if a yellow animal with black stripes eats you, you can be sure it's a Bengal Tiger! Let's read this hilarious poem.",
        "body_hi": "यदि आप जंगल में चल रहे हैं, तो आपको कैसे पता चलेगा कि आपके सामने खड़ा जानवर शेर है या बाघ? कवयित्री कैरोलिन वेल्स (Carolyn Wells) ने आपकी मदद के लिए एक बहुत ही मज़ेदार कविता लिखी है! वह जंगली जानवरों की पहचान करने के लिए कुछ अत्यधिक खतरनाक और हास्यपूर्ण (humorous) तरीके सुझाती है। उदाहरण के लिए, उनका नियम है: यदि कोई जानवर इतनी जोर से दहाड़ता है कि आप डर के मारे मर रहे हैं, तो वह शेर है! और अगर काली धारियों वाला पीला जानवर आपको खा जाए, तो आप यकीन कर सकते हैं कि यह बंगाल टाइगर है! आइए इस प्रफुल्लित करने वाली कविता को पढ़ें।",
        "body_gu": "જો તમે જંગલમાં ચાલતા હોવ, તો તમને કેવી રીતે ખબર પડે કે તમારી સામે ઉભેલું પ્રાણી સિંહ છે કે વાઘ? કવયિત્રી કેરોલિન વેલ્સે (Carolyn Wells) તમને મદદ કરવા માટે એક ખૂબ જ રમુજી કવિતા લખી છે! તે જંગલી પ્રાણીઓને ઓળખવા માટે કેટલીક અત્યંત જોખમી અને રમૂજી (humorous) રીતો સૂચવે છે. ઉદાહરણ તરીકે, તેણીનો નિયમ છે: જો કોઈ પ્રાણી એટલી જોરથી ગર્જના કરે કે તમે ડરથી મરી રહ્યા છો, તો તે સિંહ છે! અને જો કાળા પટ્ટાઓવાળા પીળા પ્રાણી તમને ખાય છે, તો તમે ખાતરી કરી શકો છો કે તે બંગાળ ટાઇગર છે! ચાલો આ પ્રફુલ્લિત કવિતા વાંચીએ."
    },
    {
        "id": "KOBJ_NCERT_C10_ENG_FFP_P4_002",
        "type": "theory",
        "title": "Identifying the Animals",
        "title_hi": "जानवरों की पहचान (Identifying the Animals)",
        "title_gu": "પ્રાણીઓની ઓળખ (Identifying the Animals)",
        "body": "Here are the funny ways the poet suggests to 'tell' (identify) wild animals:\n* **Asian Lion:** A large, tawny (yellow-brown) beast. If he roars at you and you feel like you are dying, it's an Asian Lion.\n* **Bengal Tiger:** A noble wild beast with black stripes on a yellow ground. If he greets you by eating you, it's a Tiger!\n* **Leopard:** A beast covered in peppered spots. As soon as he leaps on you (again and again), you'll know it's a leopard. Crying with pain won't help.\n* **Bear:** If you meet a creature that hugs you very, very hard, be sure it's a bear.\n* **Hyena vs. Crocodile:** A hyena always comes with a merry smile, but if the creature is weeping tears, it is a crocodile.\n* **Chameleon:** A small lizard-like creature with no ears and not a single wing. If there is nothing on the tree, you are seeing a chameleon (because it changes colour to match the tree!).",
        "body_hi": "यहां कुछ मज़ेदार तरीके दिए गए हैं जो कवि जंगली जानवरों को 'बताने' (पहचानने) के लिए सुझाता है:\n* **एशियाई शेर (Asian Lion):** एक बड़ा, पीले-भूरे रंग (tawny) का जानवर। यदि वह आप पर दहाड़ता है और आपको लगता है कि आप मर रहे हैं, तो यह एक एशियाई शेर है।\n* **बंगाल टाइगर (Bengal Tiger):** पीली ज़मीन पर काली धारियों वाला एक महान जंगली जानवर। यदि वह आपको खाकर आपका अभिवादन करता है, तो वह एक बाघ है!\n* **तेंदुआ (Leopard):** धब्बेदार धब्बों (peppered spots) से ढका हुआ एक जानवर। जैसे ही वह आप पर (बार-बार) छलांग लगाएगा, आपको पता चल जाएगा कि वह तेंदुआ है। दर्द से रोने से कोई मदद नहीं मिलेगी।\n* **भालू (Bear):** यदि आप किसी ऐसे प्राणी से मिलते हैं जो आपको बहुत ज़ोर से गले लगाता है (hugs), तो सुनिश्चित करें कि वह एक भालू है।\n* **हाइना बनाम मगरमच्छ (Hyena vs. Crocodile):** लकड़बग्घा (Hyena) हमेशा एक सुखद मुस्कान के साथ आता है, लेकिन अगर प्राणी आंसू बहा रहा है, तो वह मगरमच्छ (crocodile) है।\n* **गिरगिट (Chameleon):** छिपकली जैसा एक छोटा प्राणी जिसके कान नहीं होते और एक भी पंख नहीं होता। यदि पेड़ पर कुछ भी नहीं है, तो आप गिरगिट देख रहे हैं (क्योंकि यह पेड़ से मेल खाने के लिए रंग बदलता है!)।",
        "body_gu": "અહીં રમુજી રીતો છે જે કવિ જંગલી પ્રાણીઓને 'કહેવા' (ઓળખવા) સૂચવે છે:\n* **એશિયન સિંહ (Asian Lion):** એક મોટો, પીળો-ભુરો (tawny) જાનવર. જો તે તમારા પર ગર્જના કરે છે અને તમને લાગે છે કે તમે મરી રહ્યા છો, તો તે એશિયન સિંહ છે.\n* **બંગાળ ટાઇગર (Bengal Tiger):** પીળી જમીન પર કાળા પટ્ટાવાળા ઉમદા જંગલી જાનવર. જો તે તમને ખાઈને તમારું સ્વાગત કરે છે, તો તે વાઘ છે!\n* **ચિત્તો (Leopard):** મરીના ફોલ્લીઓથી (peppered spots) ઢંકાયેલ પશુ. જલદી તે તમારા પર કૂદકો મારશે (ફરી અને ફરીથી), તમને ખબર પડશે કે તે દીપડો છે. પીડાથી રડવાથી મદદ મળશે નહીં.\n* **રીંછ (Bear):** જો તમે એવા પ્રાણીને મળો છો જે તમને ખૂબ જ સખત આલિંગન (hugs) આપે છે, તો ખાતરી કરો કે તે રીંછ છે.\n* **હાયના વિ. મગર (Hyena vs. Crocodile):** હાયના (Hyena) હંમેશા આનંદી સ્મિત સાથે આવે છે, પરંતુ જો પ્રાણી આંસુ વહાવે છે, તો તે મગર (crocodile) છે.\n* **કાચંડો (Chameleon):** એક નાનું ગરોળી જેવું પ્રાણી જેને કાન નથી અને એક પાંખ નથી. જો ઝાડ પર કંઈ ન હોય, તો તમે કાચંડો જોતા હોવ (કારણ કે તે ઝાડ સાથે મેળ ખાતો રંગ બદલે છે!)."
    },
    {
        "id": "KOBJ_NCERT_C10_ENG_FFP_P4_003",
        "type": "mcq",
        "title": "NCERT Exercise Q: Hyenas and Crocodiles",
        "title_hi": "NCERT अभ्यास Q: लकड़बग्घे और मगरमच्छ (Hyenas and Crocodiles)",
        "title_gu": "NCERT સ્વાધ્યાય Q: હાયનાસ અને મગર (Hyenas and Crocodiles)",
        "question": "According to the poet, how can a novice (beginner) distinguish between a hyena and a crocodile?",
        "question_hi": "कवि के अनुसार, एक नौसिखिया (novice - शुरुआत करने वाला) लकड़बग्घे और मगरमच्छ के बीच अंतर कैसे कर सकता है?",
        "question_gu": "કવિના મતે, શિખાઉ (novice - શિખાઉ માણસ) હાયના અને મગર વચ્ચે કેવી રીતે ભેદ પાડી શકે છે?",
        "options": [
            "A hyena has spots, and a crocodile has stripes.",
            "A hyena comes with merry smiles, whereas crocodiles weep tears.",
            "A hyena hugs you, but a crocodile leaps on you.",
            "A hyena lives in trees, and a crocodile lives in water."
        ],
        "options_hi": [
            "लकड़बग्घे (hyena) के शरीर पर धब्बे होते हैं, और मगरमच्छ (crocodile) के शरीर पर धारियाँ होती हैं।",
            "लकड़बग्घा एक सुखद मुस्कान (merry smiles) के साथ आता है, जबकि मगरमच्छ आंसू (tears) बहाते हैं।",
            "लकड़बग्घा तुम्हें गले लगाता है, लेकिन मगरमच्छ तुम पर छलांग लगाता है।",
            "लकड़बग्घा पेड़ों पर रहता है, और मगरमच्छ पानी में रहता है।"
        ],
        "options_gu": [
            "હાયનામાં (hyena) ફોલ્લીઓ હોય છે, અને મગરની (crocodile) પટ્ટાઓ હોય છે.",
            "હાયના આનંદી સ્મિત (merry smiles) સાથે આવે છે, જ્યારે મગર આંસુ (tears) વહાવે છે.",
            "હાયના તમને આલિંગન આપે છે, પણ મગર તમારા પર કૂદી પડે છે.",
            "હાયના ઝાડમાં રહે છે, અને મગર પાણીમાં રહે છે."
        ],
        "correct_index": 1,
        "explanation": "The poet humorously mentions famous animal myths: 'Crocodile tears' (a false display of sorrow) and the 'laughing hyena'. She says a hyena greets its prey with a smile, while a crocodile sheds tears while eating it.",
        "explanation_hi": "कवि हास्यपूर्ण ढंग से प्रसिद्ध जानवरों के मिथकों (myths) का उल्लेख करता है: 'मगरमच्छ के आंसू' (दुख का झूठा प्रदर्शन) और 'हंसता हुआ लकड़बग्घा'। वह कहती हैं कि लकड़बग्घा मुस्कुराते हुए अपने शिकार का स्वागत करता है, जबकि मगरमच्छ उसे खाते समय आंसू बहाता है।",
        "explanation_gu": "કવિ રમૂજી રીતે પ્રખ્યાત પ્રાણી દંતકથાઓ (myths) નો ઉલ્લેખ કરે છે: 'મગરના આંસુ' (દુઃખનો ખોટો પ્રદર્શન) અને 'હસતી હાયના'. તે કહે છે કે હાયના સ્મિત સાથે તેના શિકારનું સ્વાગત કરે છે, જ્યારે મગર તેને ખાતી વખતે આંસુ વહાવે છે."
    }
]

data3 = {
    "metadata": {
        "id": "ncert_class10_english_ff_poem3",
        "title": "First Flight Poetry 3: A Tiger in the Zoo",
        "subject": "English",
        "grade": "10"
    },
    "blocks": poem3_blocks
}

data4 = {
    "metadata": {
        "id": "ncert_class10_english_ff_poem4",
        "title": "First Flight Poetry 4: How to Tell Wild Animals",
        "subject": "English",
        "grade": "10"
    },
    "blocks": poem4_blocks
}

path3 = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_english_ff_poem3.json'
path4 = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_english_ff_poem4.json'

with open(path3, 'w', encoding='utf-8') as f:
    json.dump(data3, f, ensure_ascii=False, indent=2)
with open(path4, 'w', encoding='utf-8') as f:
    json.dump(data4, f, ensure_ascii=False, indent=2)

print(f"Successfully wrote {len(poem3_blocks)} blocks to {path3}")
print(f"Successfully wrote {len(poem4_blocks)} blocks to {path4}")
