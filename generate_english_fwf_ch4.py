import json

blocks = [
    {
        "id": "KOBJ_NCERT_C10_ENG_FWF_CH4_001",
        "type": "hook",
        "title": "The Perfect Thief?",
        "title_hi": "परफेक्ट चोर? (The Perfect Thief?)",
        "title_gu": "સંપૂર્ણ ચોર? (The Perfect Thief?)",
        "body": "Usually, we think of thieves as dangerous criminals who steal constantly. But what if a thief is actually a successful, respectable businessman who only steals once a year to buy rare books? \nMeet Horace Danby. He is a lock-maker who plans his robberies with 100% perfection. He never leaves a single fingerprint behind. He is about to rob a house called Shotover Grange, and his plan is flawless. But then, a simple bowl of flowers and a beautiful young lady in a red dress completely ruin his perfect plan. Does the lady catch him? Or is there a bigger twist? Let's read 'A Question of Trust' to find out what happens when a thief trusts another thief.",
        "body_hi": "आमतौर पर, हम चोरों को खतरनाक अपराधी मानते हैं जो लगातार चोरी करते हैं। लेकिन क्या होगा यदि एक चोर वास्तव में एक सफल, सम्मानित व्यवसायी (respectable businessman) हो जो दुर्लभ (rare) किताबें खरीदने के लिए साल में केवल एक बार चोरी करता हो?\nमिलिए होरेस डैनबी (Horace Danby) से। वह एक ताला बनाने वाला (lock-maker) है जो अपनी डकैतियों (robberies) की योजना 100% पूर्णता (perfection) के साथ बनाता है। वह कभी एक भी उंगली का निशान (fingerprint) पीछे नहीं छोड़ता। वह शॉटओवर ग्रेंज (Shotover Grange) नामक घर को लूटने वाला है, और उसकी योजना दोषरहित (flawless) है। लेकिन फिर, फूलों का एक साधारण कटोरा और लाल पोशाक में एक खूबसूरत युवा महिला उसकी आदर्श योजना को पूरी तरह से बर्बाद कर देती है। क्या महिला उसे पकड़ लेती है? या इसमें कोई बड़ा मोड़ (twist) है? आइए यह जानने के लिए 'ए क्वेश्चन ऑफ ट्रस्ट' (A Question of Trust - विश्वास का प्रश्न) पढ़ें कि जब एक चोर दूसरे चोर पर भरोसा करता है तो क्या होता है।",
        "body_gu": "સામાન્ય રીતે, આપણે ચોરોને ખતરનાક ગુનેગારો માનીએ છીએ જેઓ સતત ચોરી કરે છે. પરંતુ શું જો એક ચોર વાસ્તવમાં એક સફળ, આદરણીય ઉદ્યોગપતિ (respectable businessman) છે જે દુર્લભ (rare) પુસ્તકો ખરીદવા માટે વર્ષમાં માત્ર એક જ વાર ચોરી કરે છે?\nહોરેસ ડેન્બીને (Horace Danby) મળો. તે તાળા બનાવનાર (lock-maker) છે જે પોતાની લૂંટનું (robberies) આયોજન 100% પૂર્ણતા (perfection) સાથે કરે છે. તે ક્યારેય એક પણ ફિંગરપ્રિન્ટ (fingerprint) પાછળ છોડતો નથી. તે શૉટઓવર ગ્રેન્જ (Shotover Grange) નામના ઘરને લૂંટવાનો છે, અને તેની યોજના દોષરહિત (flawless) છે. પરંતુ પછી, ફૂલોનો એક સરળ બાઉલ અને લાલ ડ્રેસમાં સુંદર યુવતી તેની સંપૂર્ણ યોજનાને સંપૂર્ણપણે બરબાદ કરી દે છે. શું સ્ત્રી તેને પકડી લે છે? અથવા તેમાં કોઈ મોટો વળાંક (twist) છે? જ્યારે એક ચોર બીજા ચોર પર વિશ્વાસ કરે છે ત્યારે શું થાય છે તે શોધવા માટે ચાલો 'એ ક્વેશ્ચન ઓફ ટ્રસ્ટ' (A Question of Trust - વિશ્વાસનો પ્રશ્ન) વાંચીએ."
    },
    {
        "id": "KOBJ_NCERT_C10_ENG_FWF_CH4_002",
        "type": "theory",
        "title": "Horace Danby's Secret",
        "title_hi": "होरेस डैनबी का रहस्य",
        "title_gu": "હોરેસ ડેન્બીનું રહસ્ય",
        "body": "Everyone thought Horace Danby was a good, honest citizen. He was about fifty years old and unmarried, living with a housekeeper. He made locks and was successful enough to have two helpers. However, Horace was not *completely* honest.\nFifteen years ago, he had served his first and only sentence in a prison library. He loved rare and expensive books. To buy them, he robbed a safe every year. Each year he planned carefully just what he would do, stole enough to last for twelve months, and secretly bought the books he loved through an agent. \nThis year, he had studied a house at Shotover Grange for two weeks, looking at its rooms, its electric wiring, its paths, and its garden.",
        "body_hi": "हर किसी ने सोचा कि होरेस डैनबी (Horace Danby) एक अच्छा, ईमानदार नागरिक (honest citizen) था। वह लगभग पचास वर्ष का था और अविवाहित था, एक हाउसकीपर के साथ रहता था। उसने ताले (locks) बनाए और वह इतना सफल था कि उसके दो सहायक थे। हालाँकि, होरेस *पूरी तरह से* ईमानदार नहीं था।\nपंद्रह साल पहले, उसने अपनी पहली और एकमात्र सजा एक जेल के पुस्तकालय (prison library) में काटी थी। उसे दुर्लभ (rare) और महँगी किताबें बहुत पसंद थीं। उन्हें खरीदने के लिए वह हर साल एक तिजोरी (safe) लूटता था। हर साल वह सावधानीपूर्वक योजना बनाता था कि वह क्या करेगा, बारह महीने तक चलने के लिए पर्याप्त चोरी करता था, और एक एजेंट के माध्यम से चुपके से अपनी पसंदीदा किताबें खरीदता था।\nइस वर्ष, उसने दो सप्ताह तक शॉटओवर ग्रेंज (Shotover Grange) के एक घर का अध्ययन किया था, इसके कमरों, इसकी बिजली के तारों, इसके रास्तों और इसके बगीचे को देखा था।",
        "body_gu": "બધાને લાગતું કે હોરેસ ડેન્બી (Horace Danby) સારો, પ્રામાણિક નાગરિક (honest citizen) છે. તે પચાસેક વર્ષનો હતો અને અપરિણીત હતો, ઘરની સંભાળ રાખનાર સાથે રહેતો હતો. તેણે તાળાઓ (locks) બનાવ્યા અને એટલો સફળ થયો કે બે મદદગારો હતા. જો કે, હોરેસ *સંપૂર્ણપણે* પ્રામાણિક ન હતો.\nપંદર વર્ષ પહેલાં, તેણે તેની પ્રથમ અને એકમાત્ર સજા જેલની લાઇબ્રેરીમાં (prison library) ભોગવી હતી. તેને દુર્લભ (rare) અને મોંઘા પુસ્તકો ગમતા. તેમને ખરીદવા માટે, તે દર વર્ષે તિજોરી (safe) લૂંટતો હતો. દર વર્ષે તે સાવચેતીપૂર્વક આયોજન કરતો કે તે શું કરશે, બાર મહિના સુધી ચાલે તેટલી ચોરી કરી અને એક એજન્ટ દ્વારા ગુપ્ત રીતે તેને ગમતા પુસ્તકો ખરીદ્યા.\nઆ વર્ષે, તેણે બે અઠવાડિયા સુધી શોટઓવર ગ્રેન્જ (Shotover Grange) ખાતેના ઘરનો અભ્યાસ કર્યો હતો, તેના રૂમ, તેના ઇલેક્ટ્રિક વાયરિંગ, તેના રસ્તાઓ અને તેના બગીચાને જોતા હતા."
    },
    {
        "id": "KOBJ_NCERT_C10_ENG_FWF_CH4_003",
        "type": "theory",
        "title": "The Allergy and the Lady in Red",
        "title_hi": "एलर्जी और लाल रंग की महिला",
        "title_gu": "એલર્જી અને લાલ રંગમાં લેડી",
        "body": "The family was in London, and the two servants had gone to the movies. Horace put on his gloves (so he wouldn't leave fingerprints) and entered the house. The safe was in the drawing room, hidden behind a poor painting. \nBut Horace had a problem: he suffered from hay fever, an allergy to flowers. There was a large bowl of flowers on the table. The smell tickled his nose, and he began to sneeze repeatedly. \nSuddenly, a voice said, \"Is it a cold or hay fever?\" \nHorace turned and saw a young, pretty woman dressed in red. She stroked the family dog, Sherry, lovingly. She told Horace she was the lady of the house and had returned suddenly because she needed her jewels to wear to a party that night.",
        "body_hi": "परिवार लंदन में था, और दो नौकर फिल्म देखने गए थे। होरेस ने अपने दस्ताने (gloves) पहने (ताकि वह उंगलियों के निशान न छोड़े) और घर में प्रवेश किया। तिजोरी (safe) ड्राइंग रूम में एक खराब पेंटिंग के पीछे छिपी हुई थी।\nलेकिन होरेस को एक समस्या थी: वह हे फीवर (hay fever) से पीड़ित था, जो फूलों से होने वाली एक एलर्जी (allergy) है। मेज़ पर फूलों का एक बड़ा कटोरा था। गंध ने उसकी नाक में गुदगुदी की, और वह बार-बार छींकने (sneeze) लगा।\nअचानक, एक आवाज़ आई, \"क्या यह सर्दी है या हे फीवर?\"\nहोरेस ने मुड़कर देखा तो लाल कपड़े पहने एक युवा, खूबसूरत महिला थी। उसने परिवार के कुत्ते, शेरी (Sherry) को प्यार से सहलाया (stroked)। उसने होरेस को बताया कि वह घर की मालकिन (lady of the house) थी और अचानक लौट आई थी क्योंकि उसे उस रात एक पार्टी में पहनने के लिए अपने गहनों की आवश्यकता थी।",
        "body_gu": "પરિવાર લંડનમાં હતો, અને બે નોકર પિક્ચર જોવા ગયા હતા. હોરેસે તેના ગ્લોવ્ઝ (gloves) પહેર્યા (જેથી તે ફિંગરપ્રિન્ટ્સ છોડે નહીં) અને ઘરમાં પ્રવેશ કર્યો. તિજોરી (safe) ડ્રોઇંગ રૂમમાં, ખરાબ પેઇન્ટિંગની પાછળ છુપાયેલી હતી.\nપરંતુ હોરેસને એક સમસ્યા હતી: તે પરાગરજ તાવથી (hay fever) પીડાતો હતો, ફૂલોની એલર્જી (allergy). ટેબલ પર ફૂલોનો મોટો બાઉલ હતો. ગંધથી તેના નાકમાં ગલીપચી થઈ, અને તેને વારંવાર છીંક (sneeze) આવવા લાગી.\nઅચાનક, એક અવાજ આવ્યો, \"શું તે શરદી છે કે પરાગરજ તાવ?\"\nહોરેસે વળીને લાલ કપડાં પહેરેલી એક યુવાન, સુંદર સ્ત્રીને જોઈ. તેણીએ પરિવારના કૂતરા, શેરીને (Sherry) પ્રેમથી સ્ટ્રોક (stroked) કર્યો. તેણીએ હોરેસને કહ્યું કે તે ઘરની મહિલા (lady of the house) છે અને અચાનક પાછી ફરી છે કારણ કે તેને તે રાત્રે પાર્ટીમાં પહેરવા માટે તેના ઝવેરાતની જરૂર છે."
    },
    {
        "id": "KOBJ_NCERT_C10_ENG_FWF_CH4_004",
        "type": "theory",
        "title": "A Fatal Mistake",
        "title_hi": "एक घातक गलती (A Fatal Mistake)",
        "title_gu": "જીવલેણ ભૂલ (A Fatal Mistake)",
        "body": "The woman told Horace that she had forgotten the numbers to open the safe. She gave him an offer: if he broke the safe open for her, she would let him go and not call the police. \nHorace, terrified of going to prison, eagerly agreed. He was so happy that he forgot his usual carefulness. He took off his gloves to offer her a cigarette lighter and then proceeded to pick the lock of the safe *with his bare hands*. He gave her the jewels and walked out happily, thinking he was safe.\nTwo days later, the police arrested Horace for the jewel robbery at Shotover Grange.",
        "body_hi": "महिला ने होरेस को बताया कि वह तिजोरी (safe) खोलने के नंबर भूल गई है। उसने उसे एक प्रस्ताव (offer) दिया: यदि वह उसके लिए तिजोरी खोल दे, तो वह उसे जाने देगी और पुलिस को नहीं बुलाएगी।\nजेल जाने से डरे होरेस (Horace) ने उत्सुकता से (eagerly) सहमति व्यक्त की। वह इतना खुश था कि वह अपनी सामान्य सावधानी भूल गया। उसने उसे सिगरेट लाइटर देने के लिए अपने दस्ताने (gloves) उतार दिए और फिर *अपने नंगे हाथों से* तिजोरी का ताला खोलने लगा। उसने उसे गहने दिए और खुशी-खुशी बाहर चला गया, यह सोचकर कि वह सुरक्षित है।\nदो दिन बाद, पुलिस ने शॉटओवर ग्रेंज में गहनों की डकैती (jewel robbery) के आरोप में होरेस को गिरफ्तार कर लिया।",
        "body_gu": "સ્ત્રીએ હોરેસને કહ્યું કે તે તિજોરી (safe) ખોલવા માટેના નંબર ભૂલી ગઈ છે. તેણીએ તેને એક ઓફર (offer) આપી: જો તે તેના માટે તિજોરી તોડી નાખે, તો તે તેને જવા દેશે અને પોલીસને બોલાવશે નહીં.\nજેલમાં જવાના ડરથી હોરેસ (Horace) આતુરતાથી (eagerly) સંમત થયો. તે એટલો ખુશ હતો કે તે તેની સામાન્ય સાવધાની ભૂલી ગયો. તેણે તેને સિગારેટ લાઇટર આપવા માટે તેના મોજા (gloves) ઉતારી દીધા અને પછી *તેના ખુલ્લા હાથો વડે* તિજોરીનું તાળું તોડવા આગળ વધ્યો. તેણે તેને ઝવેરાત આપ્યા અને ખુશીથી બહાર નીકળી ગયો, એમ વિચારીને કે તે સુરક્ષિત છે.\nબે દિવસ પછી, પોલીસે શૉટઓવર ગ્રેન્જમાં જ્વેલ લૂંટના (jewel robbery) કેસમાં હોરેસની ધરપકડ કરી."
    },
    {
        "id": "KOBJ_NCERT_C10_ENG_FWF_CH4_005",
        "type": "socratic_question",
        "title": "NCERT Exercise Q: The Real Twist",
        "title_hi": "NCERT अभ्यास Q: असली ट्विस्ट (The Real Twist)",
        "title_gu": "NCERT સ્વાધ્યાય Q: ધ રિયલ ટ્વિસ્ટ (The Real Twist)",
        "question": "When Horace was arrested, the police told him that his fingerprints were all over the room. Horace argued that the lady of the house had asked him to open the safe. Why didn't anyone believe his story?",
        "question_hi": "जब होरेस को गिरफ्तार किया गया, तो पुलिस ने उसे बताया कि पूरे कमरे में उसकी उंगलियों के निशान (fingerprints) हैं। होरेस ने तर्क दिया कि घर की मालकिन ने उसे तिजोरी खोलने के लिए कहा था। किसी ने उसकी कहानी पर विश्वास क्यों नहीं किया?",
        "question_gu": "જ્યારે હોરેસની ધરપકડ કરવામાં આવી, ત્યારે પોલીસે તેને કહ્યું કે તેના ફિંગરપ્રિન્ટ્સ (fingerprints) આખા રૂમમાં છે. હોરેસે દલીલ કરી કે ઘરની મહિલાએ તેને સેફ ખોલવાનું કહ્યું હતું. શા માટે કોઈએ તેની વાર્તા પર વિશ્વાસ ન કર્યો?",
        "options": [
            "Because he was a known criminal and liars are never trusted.",
            "Because the real lady of the house was not the young woman in red, but a sixty-year-old woman with grey hair and a sharp tongue.",
            "Because the lady in red was actually an undercover police officer who lied to him.",
            "Because there was no safe in the house in the first place."
        ],
        "options_hi": [
            "क्योंकि वह एक जाना-माना अपराधी था और झूठ बोलने वालों पर कभी भरोसा नहीं किया जाता।",
            "क्योंकि घर की असली मालकिन लाल रंग की युवा महिला नहीं थी, बल्कि साठ साल की (sixty-year-old) महिला थी जिसके बाल भूरे थे और जुबान तेज़ (sharp tongue) थी।",
            "क्योंकि लाल रंग की महिला वास्तव में एक अंडरकवर पुलिस अधिकारी थी जिसने उससे झूठ बोला था।",
            "क्योंकि घर में सबसे पहले कोई तिजोरी ही नहीं थी।"
        ],
        "options_gu": [
            "કારણ કે તે જાણીતો ગુનેગાર હતો અને જૂઠા લોકો પર ક્યારેય વિશ્વાસ કરવામાં આવતો નથી.",
            "કારણ કે ઘરની વાસ્તવિક મહિલા લાલ રંગની યુવતી ન હતી, પરંતુ ભૂખરા વાળ અને તીક્ષ્ણ જીભ (sharp tongue) વાળી સાઠ વર્ષની (sixty-year-old) મહિલા હતી.",
            "કારણ કે લાલ રંગમાં લેડી વાસ્તવમાં અંડરકવર પોલીસ અધિકારી હતી જેણે તેની સાથે જૂઠું બોલ્યું હતું.",
            "કારણ કે ઘરમાં પહેલી જગ્યાએ કોઈ સેફ નહોતું."
        ],
        "correct_index": 1,
        "explanation": "Horace had been completely tricked! The young lady in red was not the owner of the house; she was another thief. She acted confidently, petting the dog and sounding authoritative, so Horace trusted her. She got him to open the safe without his gloves, took the jewels, and left all the blame (and fingerprints) on Horace.",
        "explanation_hi": "होरेस पूरी तरह से छला (tricked) गया था! लाल रंग की युवती घर की मालकिन नहीं थी; वह एक और चोर थी। उसने आत्मविश्वास से काम लिया, कुत्ते को पाला और आधिकारिक (authoritative) लहजे में बात की, इसलिए होरेस ने उस पर भरोसा किया। उसने उसे बिना दस्ताने के तिजोरी खोलने के लिए मजबूर किया, गहने ले लिए, और सारा दोष (और उंगलियों के निशान) होरेस पर छोड़ दिया।",
        "explanation_gu": "હોરેસ સંપૂર્ણપણે છેતરાયો (tricked) હતો! લાલ રંગની યુવતી ઘરની માલિક ન હતી; તેણી બીજી ચોર હતી. તેણીએ આત્મવિશ્વાસથી અભિનય કર્યો, કૂતરાને માર્યો અને અધિકૃત (authoritative) લાગતી હતી, તેથી હોરેસે તેના પર વિશ્વાસ કર્યો. તેણીએ તેને ગ્લોવ્સ વિના તિજોરી ખોલાવ્યું, ઝવેરાત લીધા, અને તમામ દોષ (અને ફિંગરપ્રિન્ટ્સ) હોરેસ પર છોડી દીધા."
    },
    {
        "id": "KOBJ_NCERT_C10_ENG_FWF_CH4_006",
        "type": "theory",
        "title": "Honour Among Thieves?",
        "title_hi": "चोरों के बीच सम्मान? (Honour Among Thieves?)",
        "title_gu": "ચોરો વચ્ચે સન્માન? (Honour Among Thieves?)",
        "body": "Horace is now back in prison, serving as the assistant librarian. He often thinks of the charming, clever young lady who was in his own profession and who tricked him so brilliantly. \nThere is an old saying: \"There is honour among thieves\" (meaning thieves will not cheat each other). But Horace was cheated by a fellow thief who took advantage of his fear. Now, whenever someone talks about 'honour among thieves', Horace gets very angry.",
        "body_hi": "होरेस अब जेल में वापस आ गया है, सहायक लाइब्रेरियन (assistant librarian) के रूप में कार्यरत है। वह अक्सर उस आकर्षक, चतुर युवा महिला (clever young lady) के बारे में सोचता है जो उसी के पेशे में थी और जिसने उसे इतनी चतुराई से धोखा दिया (tricked) था।\nएक पुरानी कहावत है: \"चोरों के बीच सम्मान होता है\" (Honour among thieves - जिसका अर्थ है कि चोर एक-दूसरे को धोखा नहीं देंगे)। लेकिन होरेस को एक साथी चोर ने धोखा दिया जिसने उसके डर का फायदा उठाया। अब, जब भी कोई 'चोरों के बीच सम्मान' की बात करता है, तो होरेस बहुत क्रोधित हो जाता है।",
        "body_gu": "હોરેસ હવે જેલમાં પાછો ફર્યો છે, મદદનીશ ગ્રંથપાલ (assistant librarian) તરીકે સેવા આપી રહ્યો છે. તે વારંવાર મોહક, ચતુર યુવતી (clever young lady) વિશે વિચારે છે જે તેના પોતાના વ્યવસાયમાં હતી અને જેણે તેને આટલી તેજસ્વી રીતે છેતર્યો (tricked) હતો.\nએક જૂની કહેવત છે: \"ચોરોમાં સન્માન હોય છે\" (Honour among thieves - જેનો અર્થ થાય છે કે ચોર એકબીજા સાથે છેતરપિંડી કરશે નહીં). પરંતુ હોરેસને તેના ડરનો ફાયદો ઉઠાવનાર સાથી ચોર દ્વારા છેતરવામાં આવ્યો હતો. હવે જ્યારે પણ કોઈ 'ચોરો વચ્ચે સન્માન'ની વાત કરે છે ત્યારે હોરેસ ખૂબ ગુસ્સે થઈ જાય છે."
    }
]

data = {
    "metadata": {
        "id": "ncert_class10_english_fwf_ch4",
        "title": "Footprints Without Feet Chapter 4: A Question of Trust",
        "subject": "English",
        "grade": "10"
    },
    "blocks": blocks
}

output_path = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_english_fwf_ch4.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Successfully wrote {len(blocks)} blocks to {output_path}")
