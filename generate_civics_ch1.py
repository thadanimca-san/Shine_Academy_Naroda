import json

blocks = [
    {
        "id": "KOBJ_NCERT_C10_CIVICS_CH1_001",
        "type": "hook",
        "title": "Who Gets the Power?",
        "title_hi": "सत्ता (Power) किसे मिलती है?",
        "title_gu": "સત્તા (Power) કોને મળે છે?",
        "body": "Imagine a classroom where only the tallest students are allowed to make rules, and the shorter students must simply obey. Would the shorter students be happy? Probably not. They might even rebel! A country is much like a large classroom. In a democracy, there are people of different religions, languages, and cultures. If the majority group takes all the power and ignores the minority, it leads to conflict, violence, and even civil war. But what if they decide to share the power? Let's look at two real countries—Belgium and Sri Lanka—to see what happens when power is shared, and what happens when it is not.",
        "body_hi": "एक ऐसी कक्षा की कल्पना करें जहां केवल सबसे लंबे छात्रों को नियम बनाने की अनुमति है, और छोटे छात्रों को केवल पालन करना चाहिए। क्या छोटे छात्र खुश होंगे? शायद नहीं। वे विद्रोह भी कर सकते हैं! एक देश काफी हद तक एक बड़ी कक्षा की तरह होता है। एक लोकतंत्र (democracy) में अलग-अलग धर्म, भाषा और संस्कृति के लोग होते हैं। यदि बहुसंख्यक (majority) समूह सारी सत्ता हथिया लेता है और अल्पसंख्यक (minority) की उपेक्षा करता है, तो इससे संघर्ष, हिंसा और यहां तक ​​कि गृहयुद्ध (civil war) भी होता है। लेकिन क्या होगा अगर वे सत्ता साझा करने (power sharing) का फैसला करें? आइए दो वास्तविक देशों—बेल्जियम और श्रीलंका—को देखें कि जब सत्ता साझा की जाती है तो क्या होता है, और जब ऐसा नहीं होता है तो क्या होता है।",
        "body_gu": "એવા વર્ગખંડની કલ્પના કરો કે જ્યાં માત્ર સૌથી ઊંચા વિદ્યાર્થીઓને જ નિયમો બનાવવાની છૂટ છે, અને નાના વિદ્યાર્થીઓએ ફક્ત પાલન કરવું જોઈએ. શું નાના વિદ્યાર્થીઓ ખુશ થશે? કદાચ નહીં. તેઓ બળવો પણ કરી શકે છે! દેશ ઘણો ખરો મોટા વર્ગખંડ જેવો છે. લોકશાહીમાં (democracy) વિવિધ ધર્મ, ભાષા અને સંસ્કૃતિના લોકો છે. જો બહુમતી (majority) જૂથ બધી સત્તા લે છે અને લઘુમતીની (minority) અવગણના કરે છે, તો તે સંઘર્ષ, હિંસા અને ગૃહ યુદ્ધ (civil war) તરફ દોરી જાય છે. પરંતુ જો તેઓ સત્તા વહેંચવાનું (power sharing) નક્કી કરે તો શું? ચાલો બે વાસ્તવિક દેશો-બેલ્જિયમ અને શ્રીલંકા-ને જોઈએ કે જ્યારે સત્તા વહેંચાય છે ત્યારે શું થાય છે, અને જ્યારે એવું નથી થતું ત્યારે શું થાય છે."
    },
    {
        "id": "KOBJ_NCERT_C10_CIVICS_CH1_002",
        "type": "theory",
        "title": "Belgium and Sri Lanka",
        "title_hi": "बेल्जियम और श्रीलंका",
        "title_gu": "બેલ્જિયમ અને શ્રીલંકા",
        "body": "Belgium is a small country in Europe. Its ethnic composition is complex: 59% speak Dutch, 40% speak French, and 1% speak German. However, in the capital city Brussels, 80% speak French and 20% speak Dutch. The minority French-speaking community was relatively rich and powerful, causing tension with the Dutch-speaking majority.\nSri Lanka is an island nation. It has 74% Sinhala speakers (mostly Buddhist) and 18% Tamil speakers (Hindu or Muslim). The Tamils are divided into 'Sri Lankan Tamils' and 'Indian Tamils'. What if the Sinhala majority forced their will on the Tamils?",
        "body_hi": "बेल्जियम यूरोप का एक छोटा सा देश है। इसकी जातीय संरचना जटिल है: 59% डच बोलते हैं, 40% फ्रेंच बोलते हैं, और 1% जर्मन बोलते हैं। हालाँकि, राजधानी ब्रुसेल्स में, 80% लोग फ्रेंच बोलते हैं और 20% डच बोलते हैं। अल्पसंख्यक फ्रेंच भाषी समुदाय अपेक्षाकृत अमीर और शक्तिशाली था, जिससे डच भाषी बहुमत के साथ तनाव पैदा हो गया।\nश्रीलंका एक द्वीप राष्ट्र है। इसमें 74% सिंहली भाषी (ज्यादातर बौद्ध) और 18% तमिल भाषी (हिंदू या मुस्लिम) हैं। तमिलों को 'श्रीलंकाई तमिल' और 'भारतीय तमिल' में विभाजित किया गया है। क्या होगा यदि सिंहली बहुमत तमिलों पर अपनी इच्छा थोप दे?",
        "body_gu": "બેલ્જિયમ યુરોપનો એક નાનો દેશ છે. તેની વંશીય રચના જટિલ છે: 59% ડચ બોલે છે, 40% ફ્રેન્ચ બોલે છે, અને 1% જર્મન બોલે છે. જો કે, રાજધાની બ્રસેલ્સમાં, 80% લોકો ફ્રેન્ચ બોલે છે અને 20% ડચ બોલે છે. લઘુમતી ફ્રેન્ચ બોલતો સમુદાય પ્રમાણમાં સમૃદ્ધ અને શક્તિશાળી હતો, જેના કારણે ડચ બોલતા બહુમતી સાથે તણાવ ઊભો થયો.\nશ્રીલંકા એક ટાપુ રાષ્ટ્ર છે. તેમાં 74% સિંહલા બોલનારા (મોટાભાગે બૌદ્ધ) અને 18% તમિલ બોલનારા (હિન્દુ અથવા મુસ્લિમ) છે. તમિલોને 'શ્રીલંકન તમિલો' અને 'ભારતીય તમિલો'માં વિભાજિત કરવામાં આવ્યા છે. જો સિંહલી બહુમતી તમિલો પર તેમની ઇચ્છા લાદે તો શું?"
    },
    {
        "id": "KOBJ_NCERT_C10_CIVICS_CH1_003",
        "type": "theory",
        "title": "Majoritarianism in Sri Lanka",
        "title_hi": "श्रीलंका में बहुसंख्यकवाद (Majoritarianism)",
        "title_gu": "શ્રીલંકામાં બહુમતીવાદ (Majoritarianism)",
        "body": "In 1956, Sri Lanka passed an Act to recognise Sinhala as the only official language, disregarding Tamil. The governments followed preferential policies that favoured Sinhala applicants for university positions and government jobs. A new constitution stipulated that the state shall protect and foster Buddhism.\nThese 'majoritarian' measures gradually increased the feeling of alienation among the Sri Lankan Tamils. The distrust between the two communities turned into widespread conflict. It soon turned into a Civil War. As a result, thousands of people of both communities have been killed.",
        "body_hi": "1956 में, श्रीलंका ने तमिल की उपेक्षा करते हुए सिंहली को एकमात्र आधिकारिक भाषा (official language) के रूप में मान्यता देने के लिए एक अधिनियम पारित किया। सरकारों ने ऐसी अधिमान्य (preferential) नीतियों का पालन किया जो विश्वविद्यालय के पदों और सरकारी नौकरियों के लिए सिंहली आवेदकों का पक्ष लेती थीं। एक नए संविधान में यह निर्धारित किया गया कि राज्य बौद्ध धर्म की रक्षा और उसे बढ़ावा देगा।\nइन 'बहुसंख्यकवादी' (majoritarian) उपायों ने धीरे-धीरे श्रीलंकाई तमिलों के बीच अलगाव (alienation) की भावना को बढ़ा दिया। दोनों समुदायों के बीच अविश्वास व्यापक संघर्ष में बदल गया। जल्द ही यह गृहयुद्ध (Civil War) में बदल गया। नतीजतन, दोनों समुदायों के हजारों लोग मारे गए हैं।",
        "body_gu": "1956 માં, શ્રીલંકાએ તમિલની અવગણના કરીને સિંહલાને એકમાત્ર સત્તાવાર ભાષા (official language) તરીકે માન્યતા આપવા માટે એક કાયદો પસાર કર્યો. સરકારોએ પસંદગીની નીતિઓ અનુસરી જે યુનિવર્સિટીના હોદ્દા અને સરકારી નોકરીઓ માટે સિંહલા અરજદારોની તરફેણ કરતી હતી. એક નવા બંધારણમાં એવું નિર્ધારિત કરવામાં આવ્યું છે કે રાજ્ય બૌદ્ધ ધર્મનું રક્ષણ અને પ્રોત્સાહન આપશે.\nઆ 'બહુમતીવાદી' (majoritarian) પગલાંઓએ ધીમે ધીમે શ્રીલંકન તમિલોમાં પરાયાપણાની (alienation) ભાવનામાં વધારો કર્યો. બંને સમુદાયો વચ્ચેનો અવિશ્વાસ વ્યાપક સંઘર્ષમાં ફેરવાઈ ગયો. ટૂંક સમયમાં તે ગૃહ યુદ્ધમાં (Civil War) ફેરવાઈ ગયું. પરિણામે, બંને સમુદાયોના હજારો લોકો માર્યા ગયા છે."
    },
    {
        "id": "KOBJ_NCERT_C10_CIVICS_CH1_004",
        "type": "socratic_question",
        "title": "Accommodation in Belgium",
        "title_hi": "बेल्जियम में समझदारी",
        "title_gu": "બેલ્જિયમમાં સમજદારી",
        "question": "Instead of majority rule, Belgium amended its constitution four times between 1970 and 1993 to work out an arrangement that would enable everyone to live together within the same country. They decided that the number of Dutch and French-speaking ministers shall be equal in the central government. Which of the following is ANOTHER unique form of power sharing introduced in Belgium?",
        "question_hi": "बहुमत के शासन के बजाय, बेल्जियम ने 1970 और 1993 के बीच चार बार अपने संविधान में संशोधन किया ताकि एक ऐसी व्यवस्था तैयार की जा सके जो सभी को एक ही देश में एक साथ रहने में सक्षम बनाए। उन्होंने तय किया कि केंद्र सरकार में डच और फ्रेंच भाषी मंत्रियों की संख्या बराबर होगी। निम्नलिखित में से कौन सा बेल्जियम में पेश किया गया सत्ता साझेदारी का एक और अनूठा रूप है?",
        "question_gu": "બહુમતી શાસનને બદલે, બેલ્જિયમે 1970 અને 1993 ની વચ્ચે તેના બંધારણમાં ચાર વખત સુધારો કર્યો જેથી એવી વ્યવસ્થા તૈયાર કરી શકાય જે દરેકને એક જ દેશમાં સાથે રહેવા સક્ષમ બનાવે. તેઓએ નક્કી કર્યું કે કેન્દ્ર સરકારમાં ડચ અને ફ્રેન્ચ બોલતા પ્રધાનોની સંખ્યા સમાન રહેશે. નીચેનામાંથી કયું બેલ્જિયમમાં રજૂ કરવામાં આવેલ સત્તા વહેંચણીનું બીજું અનોખું સ્વરૂપ છે?",
        "options": [
            "They created a 'Community Government' elected by people belonging to one language community (Dutch, French and German) to handle cultural and educational issues.",
            "They banned the German language completely to reduce tension.",
            "They split the country into two separate independent nations.",
            "They decided that only the richest people would vote in elections."
        ],
        "options_hi": [
            "उन्होंने सांस्कृतिक और शैक्षिक मुद्दों को संभालने के लिए एक भाषा समुदाय (डच, फ्रेंच और जर्मन) से संबंधित लोगों द्वारा चुनी गई एक 'सामुदायिक सरकार' (Community Government) बनाई।",
            "उन्होंने तनाव कम करने के लिए जर्मन भाषा पर पूरी तरह प्रतिबंध लगा दिया।",
            "उन्होंने देश को दो अलग-अलग स्वतंत्र राष्ट्रों में विभाजित कर दिया।",
            "उन्होंने तय किया कि चुनावों में केवल सबसे अमीर लोग ही वोट देंगे।"
        ],
        "options_gu": [
            "તેઓએ સાંસ્કૃતિક અને શૈક્ષણિક મુદ્દાઓને સંભાળવા માટે એક ભાષા સમુદાયના (ડચ, ફ્રેન્ચ અને જર્મન) લોકો દ્વારા ચૂંટાયેલી 'સમુદાય સરકાર' (Community Government) બનાવી.",
            "તણાવ ઘટાડવા માટે તેઓએ જર્મન ભાષા પર સંપૂર્ણ પ્રતિબંધ મૂક્યો.",
            "તેઓએ દેશને બે અલગ સ્વતંત્ર રાષ્ટ્રોમાં વિભાજિત કર્યો.",
            "તેઓએ નક્કી કર્યું કે ચૂંટણીમાં માત્ર સૌથી અમીર લોકો જ મત આપશે."
        ],
        "correct_index": 0,
        "explanation": "The Belgian model included equal representation in the central government, separate government for Brussels with equal representation, and a third kind of government called 'Community Government' elected by people of one language community to handle culture, education, and language-related issues.",
        "explanation_hi": "बेल्जियम मॉडल में केंद्र सरकार में समान प्रतिनिधित्व, समान प्रतिनिधित्व के साथ ब्रुसेल्स के लिए अलग सरकार, और एक तीसरे प्रकार की सरकार शामिल है जिसे 'सामुदायिक सरकार' (Community Government) कहा जाता है जो एक भाषा समुदाय के लोगों द्वारा संस्कृति, शिक्षा और भाषा से संबंधित मुद्दों को संभालने के लिए चुनी जाती है।",
        "explanation_gu": "બેલ્જિયમ મોડલમાં કેન્દ્ર સરકારમાં સમાન પ્રતિનિધિત્વ, સમાન પ્રતિનિધિત્વ સાથે બ્રસેલ્સ માટે અલગ સરકાર, અને સંસ્કૃતિ, શિક્ષણ અને ભાષા સંબંધિત મુદ્દાઓનું સંચાલન કરવા માટે એક ભાષા સમુદાયના લોકો દ્વારા ચૂંટાયેલી 'સમુદાય સરકાર' (Community Government) નામની ત્રીજી પ્રકારની સરકારનો સમાવેશ થાય છે."
    },
    {
        "id": "KOBJ_NCERT_C10_CIVICS_CH1_005",
        "type": "theory",
        "title": "Why power sharing is desirable?",
        "title_hi": "सत्ता की साझेदारी वांछनीय (desirable) क्यों है?",
        "title_gu": "સત્તાની વહેંચણી શા માટે ઈચ્છનીય (desirable) છે?",
        "body": "There are two sets of reasons for power sharing:\n1. Prudential Reasons: Power sharing is good because it helps to reduce the possibility of conflict between social groups. Since social conflict often leads to violence and political instability, power sharing is a good way to ensure the stability of political order.\n2. Moral Reasons: Power sharing is the very spirit of democracy. A democratic rule involves sharing power with those affected by its exercise, and who have to live with its effects. People have a right to be consulted on how they are to be governed.",
        "body_hi": "सत्ता की साझेदारी के लिए दो तरह के कारण हैं:\n1. युक्तिपरक कारण (Prudential Reasons): सत्ता की साझेदारी अच्छी है क्योंकि यह सामाजिक समूहों के बीच संघर्ष (conflict) की संभावना को कम करने में मदद करती है। चूंकि सामाजिक संघर्ष अक्सर हिंसा और राजनीतिक अस्थिरता (instability) की ओर ले जाता है, इसलिए सत्ता की साझेदारी राजनीतिक व्यवस्था की स्थिरता सुनिश्चित करने का एक अच्छा तरीका है।\n2. नैतिक कारण (Moral Reasons): सत्ता की साझेदारी लोकतंत्र (democracy) की मूल भावना है। एक लोकतांत्रिक शासन में सत्ता को उन लोगों के साथ साझा करना शामिल है जो इसके अभ्यास से प्रभावित होते हैं, और जिन्हें इसके प्रभावों के साथ रहना पड़ता है। लोगों को यह अधिकार है कि उनसे परामर्श (consult) किया जाए कि उन पर कैसे शासन किया जाए।",
        "body_gu": "સત્તાની વહેંચણી માટે બે પ્રકારના કારણો છે:\n1. સમજદારીપૂર્ણ કારણો (Prudential Reasons): સત્તાની વહેંચણી સારી છે કારણ કે તે સામાજિક જૂથો વચ્ચે સંઘર્ષની (conflict) શક્યતા ઘટાડવામાં મદદ કરે છે. કારણ કે સામાજિક સંઘર્ષ ઘણીવાર હિંસા અને રાજકીય અસ્થિરતા (instability) તરફ દોરી જાય છે, તેથી સત્તાની વહેંચણી રાજકીય વ્યવસ્થાની સ્થિરતા સુનિશ્ચિત કરવાનો સારો માર્ગ છે.\n2. નૈતિક કારણો (Moral Reasons): સત્તાની વહેંચણી એ લોકશાહીની (democracy) મૂળ ભાવના છે. લોકશાહી શાસનમાં સત્તાની વહેંચણી તે લોકો સાથે સંકળાયેલી છે જેઓ તેના અમલથી પ્રભાવિત થાય છે, અને જેઓ તેની અસરો સાથે જીવતા હોય છે. લોકો પાસે એવો અધિકાર છે કે તેમની સાથે સલાહ (consult) લેવામાં આવે કે તેમના પર કેવી રીતે શાસન કરવામાં આવે."
    },
    {
        "id": "KOBJ_NCERT_C10_CIVICS_CH1_006",
        "type": "theory",
        "title": "Forms of Power Sharing",
        "title_hi": "सत्ता की साझेदारी के रूप",
        "title_gu": "સત્તાની વહેંચણીના સ્વરૂપો",
        "body": "In modern democracies, power sharing arrangements can take many forms:\n1. Horizontal distribution: Power is shared among different organs of government, such as the legislature, executive and judiciary. It allows different organs placed at the same level to exercise different powers (System of checks and balances).\n2. Vertical distribution: Power can be shared among governments at different levels – a general government for the entire country (Federal/Central Government) and governments at the provincial or regional level (State Governments, Municipalities, Panchayats).\n3. Power sharing among social groups: Power may also be shared among different social groups such as the religious and linguistic groups (e.g., 'Community government' in Belgium, reserved constituencies in India).\n4. Power sharing among political parties, pressure groups and movements: This ensures that power does not remain in one hand. E.g., Coalition governments.",
        "body_hi": "आधुनिक लोकतंत्रों में, सत्ता की साझेदारी (power sharing) के कई रूप हो सकते हैं:\n1. क्षैतिज वितरण (Horizontal distribution): सरकार के विभिन्न अंगों, जैसे विधायिका (legislature), कार्यपालिका (executive) और न्यायपालिका (judiciary) के बीच सत्ता साझा की जाती है। यह समान स्तर पर रखे गए विभिन्न अंगों को विभिन्न शक्तियों का प्रयोग करने की अनुमति देता है (नियंत्रण और संतुलन की प्रणाली)।\n2. ऊर्ध्वाधर वितरण (Vertical distribution): सत्ता को विभिन्न स्तरों पर सरकारों के बीच साझा किया जा सकता है - पूरे देश के लिए एक सामान्य सरकार (संघीय/केंद्र सरकार) और प्रांतीय या क्षेत्रीय स्तर पर सरकारें (राज्य सरकारें, नगरपालिकाएं, पंचायतें)।\n3. सामाजिक समूहों के बीच सत्ता की साझेदारी: सत्ता को विभिन्न सामाजिक समूहों जैसे धार्मिक और भाषाई समूहों के बीच भी साझा किया जा सकता है (जैसे, बेल्जियम में 'सामुदायिक सरकार', भारत में आरक्षित निर्वाचन क्षेत्र (reserved constituencies))।\n4. राजनीतिक दलों, दबाव समूहों और आंदोलनों के बीच सत्ता की साझेदारी: यह सुनिश्चित करता है कि सत्ता एक हाथ में न रहे। उदा., गठबंधन सरकारें (Coalition governments)।",
        "body_gu": "આધુનિક લોકશાહીમાં, સત્તાની વહેંચણી (power sharing) ઘણા સ્વરૂપો લઈ શકે છે:\n1. આડું વિતરણ (Horizontal distribution): સરકારના વિવિધ અંગો, જેમ કે ધારાસભા (legislature), કારોબારી (executive) અને ન્યાયતંત્ર (judiciary) વચ્ચે સત્તાની વહેંચણી કરવામાં આવે છે. તે સમાન સ્તરે મૂકવામાં આવેલા વિવિધ અંગોને વિવિધ સત્તાઓનો ઉપયોગ કરવાની મંજૂરી આપે છે (નિયંત્રણ અને સંતુલનની સિસ્ટમ).\n2. ઊભું વિતરણ (Vertical distribution): સત્તાને વિવિધ સ્તરે સરકારો વચ્ચે વહેંચી શકાય છે - સમગ્ર દેશ માટે સામાન્ય સરકાર (ફેડરલ/કેન્દ્ર સરકાર) અને પ્રાંતીય અથવા પ્રાદેશિક સ્તરે સરકારો (રાજ્ય સરકારો, નગરપાલિકાઓ, પંચાયતો).\n3. સામાજિક જૂથો વચ્ચે સત્તાની વહેંચણી: સત્તાને વિવિધ સામાજિક જૂથો જેમ કે ધાર્મિક અને ભાષાકીય જૂથો વચ્ચે પણ વહેંચવામાં આવી શકે છે (દા.ત., બેલ્જિયમમાં 'સમુદાય સરકાર', ભારતમાં આરક્ષિત મતવિસ્તારો (reserved constituencies)).\n4. રાજકીય પક્ષો, દબાણ જૂથો અને આંદોલનો વચ્ચે સત્તાની વહેંચણી: આ ખાતરી કરે છે કે સત્તા એક હાથમાં ન રહે. દા.ત., ગઠબંધન સરકારો (Coalition governments)."
    },
    {
        "id": "KOBJ_NCERT_C10_CIVICS_CH1_007",
        "type": "mcq",
        "title": "NCERT Exercise Q1",
        "title_hi": "NCERT अभ्यास Q1",
        "title_gu": "NCERT સ્વાધ્યાય Q1",
        "question": "Which of the following is NOT a form of power sharing in modern democracies?",
        "question_hi": "आधुनिक लोकतंत्रों में निम्नलिखित में से कौन सा सत्ता की साझेदारी का रूप नहीं है?",
        "question_gu": "આધુનિક લોકશાહીમાં નીચેનામાંથી કયું સત્તા વહેંચણીનું સ્વરૂપ નથી?",
        "options": [
            "Vertical division of power among different levels of government",
            "Horizontal division of power among different organs of government",
            "Concentration of all power in the hands of the military",
            "Power sharing among different social and linguistic groups"
        ],
        "options_hi": [
            "सरकार के विभिन्न स्तरों के बीच सत्ता का ऊर्ध्वाधर (Vertical) विभाजन",
            "सरकार के विभिन्न अंगों के बीच सत्ता का क्षैतिज (Horizontal) विभाजन",
            "सभी शक्ति का सेना के हाथों में एकाग्रता (Concentration)",
            "विभिन्न सामाजिक और भाषाई समूहों के बीच सत्ता की साझेदारी"
        ],
        "options_gu": [
            "સરકારના વિવિધ સ્તરો વચ્ચે સત્તાનું ઊભું (Vertical) વિભાજન",
            "સરકારના વિવિધ અંગો વચ્ચે સત્તાનું આડું (Horizontal) વિભાજન",
            "લશ્કરના હાથમાં તમામ સત્તાનું એકત્રીકરણ (Concentration)",
            "વિવિધ સામાજિક અને ભાષાકીય જૂથો વચ્ચે સત્તાની વહેંચણી"
        ],
        "correct_index": 2,
        "explanation": "Democracy relies on sharing power among various groups and institutions to prevent dictatorship. Concentration of power in the hands of the military is a feature of a military dictatorship, not a democracy.",
        "explanation_hi": "तानाशाही (dictatorship) को रोकने के लिए लोकतंत्र विभिन्न समूहों और संस्थानों के बीच सत्ता साझा करने पर निर्भर करता है। सेना के हाथों में सत्ता का केंद्रीकरण एक सैन्य तानाशाही की विशेषता है, लोकतंत्र की नहीं।",
        "explanation_gu": "સરમુખત્યારશાહી (dictatorship) અટકાવવા લોકશાહી વિવિધ જૂથો અને સંસ્થાઓ વચ્ચે સત્તા વહેંચવા પર આધાર રાખે છે. સૈન્યના હાથમાં સત્તાનું કેન્દ્રીકરણ એ લશ્કરી સરમુખત્યારશાહીનું લક્ષણ છે, લોકશાહીનું નથી."
    },
    {
        "id": "KOBJ_NCERT_C10_CIVICS_CH1_008",
        "type": "mcq",
        "title": "NCERT Exercise Q2",
        "title_hi": "NCERT अभ्यास Q2",
        "title_gu": "NCERT સ્વાધ્યાય Q2",
        "question": "What is the official religion of Sri Lanka according to its constitution?",
        "question_hi": "इसके संविधान के अनुसार श्रीलंका का आधिकारिक धर्म (official religion) कौन सा है?",
        "question_gu": "તેના બંધારણ મુજબ શ્રીલંકાનો સત્તાવાર ધર્મ કયો છે?",
        "options": [
            "Hinduism",
            "Islam",
            "Buddhism",
            "Christianity"
        ],
        "options_hi": [
            "हिंदू धर्म",
            "इसलाम",
            "बौद्ध धर्म (Buddhism)",
            "ईसाई धर्म"
        ],
        "options_gu": [
            "હિન્દુ ધર્મ",
            "ઇસ્લામ",
            "બૌદ્ધ ધર્મ (Buddhism)",
            "ખ્રિસ્તી ધર્મ"
        ],
        "correct_index": 2,
        "explanation": "A new constitution in Sri Lanka stipulated that the state shall protect and foster Buddhism, which is followed mostly by the Sinhala-speaking majority.",
        "explanation_hi": "श्रीलंका में एक नए संविधान ने यह निर्धारित किया कि राज्य बौद्ध धर्म की रक्षा और बढ़ावा देगा, जिसका पालन ज्यादातर सिंहली भाषी बहुसंख्यक करते हैं।",
        "explanation_gu": "શ્રીલંકામાં નવા બંધારણમાં એવું નિર્ધારિત કરવામાં આવ્યું છે કે રાજ્ય બૌદ્ધ ધર્મનું રક્ષણ અને પ્રોત્સાહન આપશે, જે મોટાભાગે સિંહલા બોલતા બહુમતી દ્વારા અનુસરવામાં આવે છે."
    },
    {
        "id": "KOBJ_NCERT_C10_CIVICS_CH1_009",
        "type": "mcq",
        "title": "NCERT Exercise Q3",
        "title_hi": "NCERT अभ्यास Q3",
        "title_gu": "NCERT સ્વાધ્યાય Q3",
        "question": "Which of the following describes the system of 'checks and balances'?",
        "question_hi": "निम्नलिखित में से कौन 'नियंत्रण और संतुलन' (checks and balances) की प्रणाली का वर्णन करता है?",
        "question_gu": "નીચેનામાંથી કયું 'નિયંત્રણ અને સંતુલન' (checks and balances) સિસ્ટમનું વર્ણન કરે છે?",
        "options": [
            "Vertical division of power",
            "Horizontal division of power",
            "Community government",
            "Coalition government"
        ],
        "options_hi": [
            "सत्ता का ऊर्ध्वाधर (Vertical) विभाजन",
            "सत्ता का क्षैतिज (Horizontal) विभाजन",
            "सामुदायिक सरकार (Community government)",
            "गठबंधन सरकार (Coalition government)"
        ],
        "options_gu": [
            "સત્તાનું ઊભું (Vertical) વિભાજન",
            "સત્તાનું આડું (Horizontal) વિભાજન",
            "સમુદાય સરકાર (Community government)",
            "ગઠબંધન સરકાર (Coalition government)"
        ],
        "correct_index": 1,
        "explanation": "Horizontal division of power allows different organs of government (legislature, executive, and judiciary) placed at the same level to exercise different powers. Each organ checks the others. This results in a balance of power among various institutions, known as a system of checks and balances.",
        "explanation_hi": "सत्ता का क्षैतिज (Horizontal) विभाजन सरकार के विभिन्न अंगों (विधायिका, कार्यपालिका और न्यायपालिका) को एक ही स्तर पर रखकर विभिन्न शक्तियों का प्रयोग करने की अनुमति देता है। प्रत्येक अंग दूसरों की जाँच करता है। इसके परिणामस्वरूप विभिन्न संस्थानों के बीच शक्ति का संतुलन होता है, जिसे नियंत्रण और संतुलन (checks and balances) की प्रणाली के रूप में जाना जाता है।",
        "explanation_gu": "સત્તાનું આડું (Horizontal) વિભાજન સરકારના વિવિધ અંગોને (ધારાસભા, કારોબારી અને ન્યાયતંત્ર) સમાન સ્તરે મૂકીને વિવિધ સત્તાઓનો ઉપયોગ કરવાની મંજૂરી આપે છે. દરેક અંગ અન્યની તપાસ કરે છે. આના પરિણામે વિવિધ સંસ્થાઓ વચ્ચે સત્તાનું સંતુલન થાય છે, જે નિયંત્રણ અને સંતુલનની સિસ્ટમ તરીકે ઓળખાય છે."
    }
]

data = {
    "metadata": {
        "id": "ncert_class10_civics_ch1",
        "title": "Civics Chapter 1: Power Sharing",
        "subject": "Social Science",
        "grade": "10"
    },
    "blocks": blocks
}

output_path = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_civics_ch1.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Successfully wrote {len(blocks)} blocks to {output_path}")
