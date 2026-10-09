import json
import os

def generate_english_chapters():
    os.makedirs("app_core/chapters", exist_ok=True)
    os.makedirs("app_core/assessment", exist_ok=True)

    chapters_data = {
        1: {
            "title": "Chapter 1: The Fun They Had & The Road Not Taken",
            "blocks": [
                {
                    "id": "KOBJ_CLASS9_ENG_CH1_HOOK",
                    "type": "real_world_example",
                    "title": "Step 1: Hook - School in the Year 2157",
                    "title_hi": "चरण 1: हुक - वर्ष 2157 में स्कूल",
                    "title_gu": "પગલું 1: હૂક - વર્ષ 2157 માં શાળા",
                    "body": "Imagine going to school without printed books, classrooms, or human teachers! Margie and Tommy in 2157 study alone in front of a mechanical teacher screen. When Tommy finds an 'real' paper book from the past, Margie is amazed that children once sat together in a building with a human teacher!",
                    "body_hi": "मुद्रित पुस्तकों, कक्षाओं या मानव शिक्षकों के बिना स्कूल जाने की कल्पना करें! 2157 में मार्गी और टॉमी एक यांत्रिक शिक्षक स्क्रीन के सामने अकेले अध्ययन करते हैं। जब टॉमी को अतीत की एक 'वास्तविक' कागज की किताब मिलती है, तो मार्गी यह जानकर हैरान रह जाती है कि बच्चे कभी मानव शिक्षक के साथ एक ही इमारत में एक साथ बैठते थे!",
                    "body_gu": "છાપેલા પુસ્તકો, વર્ગખંડો કે માનવ શિક્ષકો વગર શાળાએ જવાની કલ્પના કરો! 2157 માં માર્ગી અને ટોમી મિકેનિકલ ટીચર સ્ક્રીન સામે એકલા અભ્યાસ કરે છે। જ્યારે ટોમીને ભૂતકાળનું 'વાસ્તવિક' કાગળનું પુસ્તક મળે છે, ત્યારે માર્ગી એ જાણીને આશ્ચર્યચકિત થઈ જાય છે કે બાળકો એક સમયે માનવ શિક્ષક સાથે એક જ બિલ્ડિંગમાં સાથે બેસતા હતા!"
                },
                {
                    "id": "KOBJ_CLASS9_ENG_CH1_THEORY_SUMMARY",
                    "type": "theory",
                    "title": "Step 4: Reveal - Summary & Themes of 'The Fun They Had'",
                    "title_hi": "चरण 4: प्रकटीकरण - 'द फन दे हैड' का सारांश और विषय",
                    "title_gu": "પગલું 4: પર્દાફાશ - 'ધ ફન ધે હેડ' નો સારાંશ અને વિષયો",
                    "body": "1. **Author**: Isaac Asimov.\n2. **Theme**: Futuristic education vs Traditional schooling. The loss of human warmth, social interaction, and fun in automated robotic teaching.\n3. **Poem - The Road Not Taken** (Robert Frost): Explores choices in life. Two roads diverged in a yellow wood; choosing the less traveled path makes all the difference.\n4. **Poetic Devices**: Metaphor (Roads = Life choices), Symbolism, Rhyme Scheme (ABAAB).",
                    "body_hi": "1. **लेखक**: आइजैक असिमोव।\n2. **विषय**: भविष्य की शिक्षा बनाम पारंपरिक स्कूली शिक्षा। स्वचालित रोबोटिक शिक्षण में मानवीय संवेदनशीलता और सामाजिक मेलजोल का अभाव।\n3. **कविता - द रोड नॉट टेकन** (रॉबर्ट फ्रॉस्ट): जीवन में विकल्पों की खोज करती है। कम यात्रा वाले रास्ते को चुनना ही सारा अंतर पैदा करता है।",
                    "body_gu": "1. **લેખક**: આઇઝેક અસિમોવ।\n2. **વિષય**: ભવિષ્યનું શિક્ષણ વિ પરંપરાગત શાળા શિક્ષણ। રોબોટિક શિક્ષણમાં માનવીય હૂંફ અને સામાજિક વાર્તાલાપનો અભાવ।\n3. **કવિતા - ધ રોડ નોટ ટેકન** (રોબર્ટ ફ્રોસ્ટ): જીવનમાં પસંદગીઓની શોધ કરે છે। જે માર્ગ પર ઓછી મુસાફરી થઈ છે તેને પસંદ કરવાથી જ બધો તફાવત પડે છે।"
                },
                {
                    "id": "KOBJ_CLASS9_ENG_CH1_EX1",
                    "type": "quiz",
                    "title": "Textbook Exercise: Mechanical Teacher vs Human Teacher",
                    "title_hi": "पाठ्यपुस्तक अभ्यास: यांत्रिक शिक्षक बनाम मानव शिक्षक",
                    "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય: મિકેનિકલ ટીચર વિ માનવ શિક્ષક",
                    "question": "Why did Margie hate her mechanical teacher, especially the geography sector?",
                    "question_hi": "मार्गी अपने यांत्रिक शिक्षक, विशेषकर भूगोल क्षेत्र से घृणा क्यों करती थी?",
                    "question_gu": "માર્ગી તેના મિકેનિકલ ટીચરથી, ખાસ કરીને ભૂગોળ વિભાગથી શા માટે નફરત કરતી હતી?",
                    "options": [
                        "It was giving test after test in geography and she was performing worse",
                        "It was giving no homework at all",
                        "It was speaking in a foreign language",
                        "It was broken completely"
                    ],
                    "options_hi": [
                        "यह भूगोल में एक के बाद एक टेस्ट दे रहा था और उसका प्रदर्शन खराब हो रहा था",
                        "यह कोई गृहकार्य नहीं दे रहा था",
                        "यह किसी विदेशी भाषा में बोल रहा था",
                        "यह पूरी तरह से टूट गया था"
                    ],
                    "options_gu": [
                        "તે ભૂગોળમાં એક પછી એક ટેસ્ટ આપી રહ્યું હતું અને તેનો દેખાવ બગડી રહ્યો હતો",
                        "તે બિલકુલ હોમવર્ક આપતું ન હતું",
                        "તે વિદેશી ભાષામાં બોલતું હતું",
                        "તે સંપૂર્ણપણે તૂટી ગયું હતું"
                    ],
                    "correct_index": 0,
                    "explanation": "The geography sector was geared too fast for a 11-year-old, causing Margie to perform poorly continuously until adjusted by the County Inspector.",
                    "explanation_hi": "भूगोल क्षेत्र 11 वर्षीय बच्ची के लिए बहुत तेज़ गति से सेट था, जिससे मार्गी का प्रदर्शन तब तक खराब रहा जब तक काउंटी इंस्पेक्टर ने इसे ठीक नहीं किया।",
                    "explanation_gu": "ભૂગોળ વિભાગ 11 વર્ષની બાળકી માટે ખૂબ જ ઝડપી ગતિએ સેટ કરવામાં આવ્યો હતો, જેથી કાઉન્ટી ઇન્સ્પેક્ટરે તેને યોગ્ય ન કર્યું ત્યાં સુધી માર્ગીનો દેખાવ નબળો રહ્યો હતો."
                },
                {
                    "id": "KOBJ_CLASS9_ENG_CH1_EX2",
                    "type": "quiz",
                    "title": "Textbook Exercise: 'The Road Not Taken' Symbolism",
                    "title_hi": "पाठ्यपुस्तक अभ्यास: 'द रोड नॉट टेकन' प्रतीकवाद",
                    "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય: 'ધ રોડ નોટ ટેકન' પ્રતીકવાદ",
                    "question": "What do the 'two roads' in Robert Frost's poem symbolize?",
                    "question_hi": "रॉबर्ट फ्रॉस्ट की कविता में 'दो रास्ते' किसका प्रतीक हैं?",
                    "question_gu": "રોબર્ટ ફ્રોસ્ટની કવિતામાં 'બે માર્ગો' શેનું પ્રતીક છે?",
                    "options": [
                        "Choices and decisions we make in life",
                        "Physical roads in a yellow forest",
                        "Two different schools",
                        "Two different seasons"
                    ],
                    "options_hi": [
                        "जीवन में हमारे द्वारा किए जाने वाले विकल्प और निर्णय",
                        "पीले जंगल में भौतिक सड़कें",
                        "दो अलग-अलग स्कूल",
                        "दो अलग-अलग मौसम"
                    ],
                    "options_gu": [
                        "જીવનમાં આપણી પસંદગીઓ અને નિર્ણયો",
                        "પીળા જંગલમાં ભૌતિક રસ્તાઓ",
                        "બે અલગ અલગ શાળાઓ",
                        "બે અલગ અલગ ઋતુઓ"
                    ],
                    "correct_index": 0,
                    "explanation": "The two diverging roads symbolize the choices, opportunities, and decisions an individual faces in life.",
                    "explanation_hi": "दो विभाजित सड़कें जीवन में किसी व्यक्ति के सामने आने वाले विकल्पों, अवसरों और निर्णयों का प्रतीक हैं।",
                    "explanation_gu": "બે ફાટા પડતા રસ્તાઓ જીવનમાં વ્યક્તિ સમક્ષ આવતી પસંદગીઓ અને નિર્ણયોનું પ્રતીક છે."
                }
            ]
        },
        2: {
            "title": "Chapter 2: The Sound of Music & Wind",
            "blocks": [
                {
                    "id": "KOBJ_CLASS9_ENG_CH2_HOOK",
                    "type": "real_world_example",
                    "title": "Step 1: Hook - Hearing Music Without Ears",
                    "title_hi": "चरण 1: हुक - कानों के बिना संगीत सुनना",
                    "title_gu": "પગલું 1: હૂક - કાન વગર સંગીત સાંભળવું",
                    "body": "Evelyn Glennie lost her hearing completely by age 11. Yet she became a world-renowned multi-percussionist! How? She learned to feel music through different parts of her body—the vibrations passing through her bare feet, waist, and fingertips!",
                    "body_hi": "एवलिन ग्लेनी ने 11 साल की उम्र तक अपनी सुनने की क्षमता पूरी तरह खो दी थी। फिर भी वह विश्व प्रसिद्ध पर्कशनिस्ट (ताल वादक) बनीं! कैसे? उन्होंने अपने शरीर के विभिन्न हिस्सों के माध्यम से संगीत को महसूस करना सीखा—नंगे पैरों, कमर और उंगलियों से गुजरने वाले कंपनों के द्वारा!",
                    "body_gu": "એવલિન ગ્લેનીએ 11 વર્ષની ઉંમરે શ્રવણશક્તિ સંપૂર્ણપણે ગુમાવી દીધી હતી। તેમ છતાં તે વિશ્વપ્રસિદ્ધ મલ્ટિ-પર્કશનિસ્ટ બની! કેવી રીતે? તેણે શરીરના વિવિધ ભાગો દ્વારા સંગીત અનુભવવાનું શીખ્યું—તેના ખુલ્લા પગ, કમર અને આંગળીઓમાંથી પસાર થતા કંપનો દ્વારા!"
                },
                {
                    "id": "KOBJ_CLASS9_ENG_CH2_THEORY_SUMMARY",
                    "type": "theory",
                    "title": "Step 4: Reveal - Evelyn Glennie, Bismillah Khan & 'Wind'",
                    "title_hi": "चरण 4: प्रकटीकरण - एवलिन ग्लेनी, बिस्मिल्लाह खान और 'विंड'",
                    "title_gu": "પગલું 4: પર્દાફાશ - એવલિન ગ્લેની, બિસ્મિલ્લાહ ખાન અને 'વિન્ડ'",
                    "body": "1. **Part I - Evelyn Glennie**: Overcame profound deafness through determination and Ron Forbes' guidance.\n2. **Part II - Bismillah Khan**: Shehnai Maestro who brought Shehnai from royal courts to the classical stage; awarded Bharat Ratna in 2001.\n3. **Poem - Wind** (Subramania Bharati): Symbolizes hardships and obstacles in life. Wind breaks weak structures but makes strong fires roar louder.",
                    "body_hi": "1. **भाग I - एवलिन ग्लेनी**: दृढ़ संकल्प और रॉन फोर्ब्स के मार्गदर्शन से बहरेपन पर विजय प्राप्त की।\n2. **भाग II - बिस्मिल्लाह खान**: शहनाई उस्ताद जिन्होंने शहनाई को राजदरबारों से शास्त्रीय मंच तक पहुँचाया; 2001 में भारत रत्न से सम्मानित।\n3. **कविता - विंड** (सुब्रमण्य भारती): जीवन में कठिनाइयों और बाधाओं का प्रतीक है। हवा कमजोर संरचनाओं को तोड़ती है लेकिन मजबूत आग को और तेज करती है।",
                    "body_gu": "1. **ભાગ I - એવલિન ગ્લેની**: દ્રઢ નિશ્ચય દ્વારા બહેરાશ પર વિજય મેળવ્યો।\n2. **ભાગ II - બિસ્મિલ્લાહ ખાન**: શરણાઈ ઉસ્તાદ જેઓ શરણાઈને રાજદરબારોમાંથી શાસ્ત્રીય મંચ પર લાવ્યા; 2001 માં ભારત રત્નથી સન્માનિત।\n3. **કવિતા - વિન્ડ** (સુબ્રમણ્ય ભારતી): જીવનની મુશ્કેલીઓનું પ્રતીક છે। પવન નબળી રચનાઓને તોડી નાખે છે પરંતુ મજબૂત આગને વધુ પ્રજ્વલિત કરે છે।"
                },
                {
                    "id": "KOBJ_CLASS9_ENG_CH2_EX1",
                    "type": "quiz",
                    "title": "Textbook Exercise: Bismillah Khan's Refusal to Move to USA",
                    "title_hi": "पाठ्यपुस्तक अभ्यास: बिस्मिल्लाह खान का अमेरिका जाने से इनकार",
                    "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય: બિસ્મિલ્લાહ ખાનનો અમેરિકા જવાનો ઇનકાર",
                    "question": "Why did Bismillah Khan refuse to start a Shehnai school in the USA?",
                    "question_hi": "बिस्मिल्लाह खान ने अमेरिका में शहनाई स्कूल शुरू करने से इनकार क्यों कर दिया?",
                    "question_gu": "બિસ્મિલ્લાહ ખાને અસમયમાં (USA) શરણાઈ શાળા શરૂ કરવાનો ઇનકાર કેમ કર્યો?",
                    "options": [
                        "Because he could not leave Ganga, Benaras, and Dumraon",
                        "Because he was not offered enough money",
                        "Because he did not like American students",
                        "Because he was too old to travel"
                    ],
                    "options_hi": [
                        "क्योंकि वे गंगा, बनारस और डुमरांव को नहीं छोड़ सकते थे",
                        "क्योंकि उन्हें पर्याप्त पैसा नहीं दिया गया था",
                        "क्योंकि वे अमेरिकी छात्रों को पसंद नहीं करते थे",
                        "क्योंकि वे यात्रा करने के लिए बहुत बूढ़े थे"
                    ],
                    "options_gu": [
                        "કારણ કે તેઓ ગંગા, બનારસ અને ડુમરાંવને છોડી શકતા ન હતા",
                        "કારણ કે તેમને પૂરતા પૈસા આપવામાં આવ્યા ન હતા",
                        "કારણ કે તેમને અમેરિકન વિદ્યાર્થીઓ ગમતા ન હતા",
                        "કારણ કે તેઓ મુસાફરી કરવા માટે ખૂબ વૃદ્ધ હતા"
                    ],
                    "correct_index": 0,
                    "explanation": "Bismillah Khan loved India and Holy River Ganga deeply. He said he could recreate Benaras in USA, but could not transport the river Ganga there!",
                    "explanation_hi": "बिस्मिल्लाह खान भारत और पवित्र नदी गंगा से गहरा प्यार करते थे। उन्होंने कहा कि वे अमेरिका में बनारस का माहौल बना सकते हैं, लेकिन गंगा को वहाँ नहीं ले जा सकते!",
                    "explanation_gu": "બિસ્મિલ્લાહ ખાન ભારત અને પવિત્ર ગંગા નદીને ખૂબ પ્રેમ કરતા હતા। તેમણે કહ્યું કે તેઓ અમેરિકામાં બનારસ બનાવી શકે, પણ ગંગા નદીને ત્યાં ન લઈ જઈ શકે!"
                }
            ]
        },
        3: {
            "title": "Chapter 3: The Little Girl & Rain on the Roof",
            "blocks": [
                {
                    "id": "KOBJ_CLASS9_ENG_CH3_HOOK",
                    "type": "real_world_example",
                    "title": "Step 1: Hook - A Strict Father's Hidden Love",
                    "title_hi": "चरण 1: हुक - एक सख्त पिता का छिपा हुआ प्यार",
                    "title_gu": "પગલું 1: હૂક - કડક પિતાનો છુપાયેલો પ્રેમ",
                    "body": "Kezia feared her father, who seemed giant-like and strict. But when Kezia had a nightmare and her mother was at the hospital, her father carried her to his bed, tucked her in, and fell asleep beside her. Kezia realized her father worked hard all day and had a big, loving heart!",
                    "body_hi": "केजिया अपने पिता से डरती थी, जो विशाल और सख्त लगते थे। लेकिन जब केजिया को एक बुरा सपना आया और उसकी माँ अस्पताल में थी, तो उसके पिता उसे अपने बिस्तर पर ले गए और उसके पास सो गए। केजिया को एहसास हुआ कि उसके पिता दिन भर मेहनत करते हैं और उनका दिल बड़ा और प्यारा है!",
                    "body_gu": "કેઝિયા તેના પિતાથી ડરતી હતી, જેઓ કડક લાગતા હતા। પરંતુ જ્યારે કેઝિયાને ખરાબ સપનું આવ્યું અને તેની માતા હોસ્પિટલમાં હતી, ત્યારે તેના પિતા તેને પોતાના પલંગ પર લઈ ગયા અને તેની પાસે સૂઈ ગયા। કેઝિયાને સમજાયું કે તેના પિતા આખો દિવસ સખત મહેમાન કરે છે અને તેમનું હૃદય મોટું છે!"
                },
                {
                    "id": "KOBJ_CLASS9_ENG_CH3_THEORY_SUMMARY",
                    "type": "theory",
                    "title": "Step 4: Reveal - Summary & Themes of 'The Little Girl'",
                    "title_hi": "चरण 4: प्रकटीकरण - 'द लिटिल गर्ल' का सारांश और विषय",
                    "title_gu": "પગલું 4: પર્દાફાશ - 'ધ લિટલ ગર્લ' નો સારાંશ અને વિષયો",
                    "body": "1. **Author**: Katherine Mansfield.\n2. **Theme**: Parent-child relationship, understanding emotional distance, and realization of paternal love.\n3. **Poem - Rain on the Roof** (Coates Kinney): Tinkle of rain on shingles brings back sweet memories of mother putting children to sleep.",
                    "body_hi": "1. **लेखक**: कैथरीन मैन्सफील्ड।\n2. **विषय**: माता-पिता और बच्चे का संबंध, भावनात्मक दूरी को समझना और पिता के प्यार का अहसास।\n3. **कविता - रेन ऑन द रूफ** (कोट्स किनी): छत पर बारिश की टपकन माँ की मीठी यादें वापस लाती है।",
                    "body_gu": "1. **લેખક**: કેથરીન મેન્સફિલ્ડ।\n2. **વિષય**: માતાપિતા-બાળકનો સંબંધ, ભાવનાત્મક અંતર સમજવું અને પિતાના પ્રેમની અનુભૂતિ।\n3. **કવિતા - રેન ઓન ધ રૂફ** (કોટ્સ કિની): છત પર વરસાદનો અવાજ માતાની મીઠી યાદો તાજી કરે છે।"
                },
                {
                    "id": "KOBJ_CLASS9_ENG_CH3_EX1",
                    "type": "quiz",
                    "title": "Textbook Exercise: Pin-Cushion Incident",
                    "title_hi": "पाठ्यपुस्तक अभ्यास: पिन-कुशन घटना",
                    "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય: પિન-કુશન ઘટના",
                    "question": "Why did Kezia tear her father's important speech papers?",
                    "question_hi": "केजिया ने अपने पिता के महत्वपूर्ण भाषण के कागजात क्यों फाड़ दिए?",
                    "question_gu": "કેઝિયાએ તેના પિતાના મહત્વપૂર્ણ ભાષણના કાગળો શા માટે ફાડી નાખ્યા?",
                    "options": [
                        "To stuff a pin-cushion she made as a birthday gift for her father",
                        "Out of anger towards her father",
                        "By mistake while playing",
                        "To make paper boats"
                    ],
                    "options_hi": [
                        "अपने पिता के लिए जन्मदिन के उपहार के रूप में बनाए गए पिन-कुशन को भरने के लिए",
                        "अपने पिता के प्रति गुस्से में",
                        "खेलते समय गलती से",
                        "कागज की नावें बनाने के लिए"
                    ],
                    "options_gu": [
                        "તેના પિતા માટે જન્મદિવસની ભેટ તરીકે બનાવેલા પિન-કુશનમાં ભરવા માટે",
                        "તેના પિતા પ્રત્યેના ગુસ્સાથી",
                        "રમતી વખતે ભૂલથી",
                        "કાગળની હોડીઓ બનાવવા માટે"
                    ],
                    "correct_index": 0,
                    "explanation": "Kezia wanted to present a pin-cushion to her father on his birthday. Finding no cotton, she stuffed it with sheets of paper from her father's desk, which happened to be hisPort Authority speech.",
                    "explanation_hi": "केजिया अपने पिता को उनके जन्मदिन पर पिन-कुशन भेंट करना चाहती थी। रुई न मिलने पर उसने उसमें अपने पिता की मेज के कागजात भर दिए।",
                    "explanation_gu": "કેઝિયા તેના પિતાને તેમના જન્મદિવસે ભેટ આપવા માંગતી હતી। રૂ ન મળતાં તેણે પિતાના ટેબલ પરના કાગળો તેમાં ભરી દીધા."
                }
            ]
        },
        4: {
            "title": "Chapter 4: A Truly Beautiful Mind & The Lake Isle of Innisfree",
            "blocks": [
                {
                    "id": "KOBJ_CLASS9_ENG_CH4_HOOK",
                    "type": "real_world_example",
                    "title": "Step 1: Hook - Albert Einstein: Genius & Humanitarian",
                    "title_hi": "चरण 1: हुक - अल्बर्ट आइंस्टीन: प्रतिभा और मानवतावादी",
                    "title_gu": "પગલું 1: હૂક - અલ્બર્ટ આઇન્સ્ટાઇન: પ્રતિભા અને માનવતાવાદી",
                    "body": "As a child, Einstein was considered 'stupid' by his headmaster and spoke late. Yet he revolutionized Physics with the Theory of Relativity ($E = mc^2$) and won the Nobel Prize in 1921. He was not just a scientific genius, but a world citizen who advocated for global peace!",
                    "body_hi": "एक बच्चे के रूप में, आइंस्टीन को उनके हेडमास्टर द्वारा 'बेवकूफ' माना जाता था और वे देर से बोलते थे। फिर भी उन्होंने सापेक्षता के सिद्धांत ($E = mc^2$) से भौतिकी में क्रांति ला दी और 1921 में नोबेल पुरस्कार जीता। वे केवल वैज्ञानिक प्रतिभा ही नहीं, बल्कि वैश्विक शांति के समर्थक थे!",
                    "body_gu": "બાળક તરીકે, આઇન્સ્ટાઇનને તેમના હેડમાસ્તર દ્વારા 'મૂર્ખ' ગણવામાં આવતા હતા। તેમ છતાં તેમણે સાપેક્ષતાના સિદ્ધાંત ($E = mc^2$) થી ભૌતિકશાસ્ત્રમાં ક્રાંતિ લાવી અને 1921 માં નોબેલ પુરસ્કાર જીત્યો। તેઓ માત્ર વૈજ્ઞાનિક જ ન હતા, પણ વિશ્વ શાંતિના સમર્થક હતા!"
                },
                {
                    "id": "KOBJ_CLASS9_ENG_CH4_THEORY_SUMMARY",
                    "type": "theory",
                    "title": "Step 4: Reveal - Life of Albert Einstein & W.B. Yeats' Poem",
                    "title_hi": "चरण 4: प्रकटीकरण - अल्बर्ट आइंस्टीन का जीवन और डब्ल्यू.बी. यीट्स की कविता",
                    "title_gu": "પગલું 4: પર્દાફાશ - અલ્બર્ટ આઇન્સ્ટાઇનનું જીવન અને કવિતા",
                    "body": "1. **Biography**: Born 1879 in Ulm, Germany. Published Special Relativity in 1905. Fled Nazi Germany to USA in 1933. Wrote to President Roosevelt warning about atomic bomb.\n2. **Poem - The Lake Isle of Innisfree** (W.B. Yeats): A musical poem expressing longing for peace and natural solitude at Innisfree away from noisy city life.",
                    "body_hi": "1. **जीवनी**: 1879 में जर्मनी में जन्म। 1905 में विशेष सापेक्षता प्रकाशित। 1933 में अमेरिका चले गए। राष्ट्रपति रूजवेल्ट को परमाणु बम के बारे में चेतावनी पत्र लिखा।\n2. **कविता - द लेक आइल ऑफ इनिसफ्री** (डब्ल्यू.बी. यीट्स): शोर-शराबे वाले शहर के जीवन से दूर इनिसफ्री में शांति और प्राकृतिक एकांत की लालसा।",
                    "body_gu": "1. **જીવનચરિત્ર**: 1879 માં જર્મનીમાં જન્મ। 1905 માં સાપેક્ષતાનો સિદ્ધાંત રજૂ કર્યો। 1933 માં અમેરિકા ગયા। પ્રમુખ રૂઝવેલ્ટને અણુબમ્બ વિશે ચેતવણી આપી।\n2. **કવિતા - ધ લેક આઇલ ઓફ ઇનિસફ્રી** (ડબ્લ્યુ.બી. યેટ્સ): ઘોંઘાટિયા શહેરથી દૂર કુદરતી શાંતિની ઝંખના।"
                },
                {
                    "id": "KOBJ_CLASS9_ENG_CH4_EX1",
                    "type": "quiz",
                    "title": "Textbook Exercise: Einstein's Letter to Roosevelt",
                    "title_hi": "पाठ्यपुस्तक अभ्यास: रूजवेल्ट को आइंस्टीन का पत्र",
                    "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય: રૂઝવેલ્ટને આઇન્સ્ટાઇનનો પત્ર",
                    "question": "Why did Einstein write a letter to American President Franklin D. Roosevelt in 1939?",
                    "question_hi": "आइंस्टीन ने 1939 में अमेरिकी राष्ट्रपति फ्रैंकलिन डी. रूजवेल्ट को पत्र क्यों लिखा?",
                    "question_gu": "આઇન્સ્ટાઇને 1939 માં અમેરિકન પ્રમુખ ફ્રેન્કલિન ડી. રૂઝવેલ્ટને પત્ર શા માટે લખ્યો?",
                    "options": [
                        "To warn him that Germany could build an atomic bomb",
                        "To ask for a job in American university",
                        "To request funds for his scientific laboratory",
                        "To invite him to Nobel Prize ceremony"
                    ],
                    "options_hi": [
                        "उन्हें चेतावनी देने के लिए कि जर्मनी परमाणु बम बना सकता है",
                        "अमेरिकी विश्वविद्यालय में नौकरी मांगने के लिए",
                        "प्रयोगशाला के लिए धन का अनुरोध करने के लिए",
                        "नोबेल पुरस्कार समारोह में आमंत्रित करने के लिए"
                    ],
                    "options_gu": [
                        "જર્મની અણુબમ્બ બનાવી શકે છે તેવી ચેતવણી આપવા માટે",
                        "અમેરિકન યુનિવર્સિટીમાં નોકરી માંગવા માટે",
                        "પ્રયોગશાળા માટે ભંડોળની વિનંતી કરવા માટે",
                        "નોબેલ પુરસ્કાર સમારોહમાં આમંત્રણ આપવા માટે"
                    ],
                    "correct_index": 0,
                    "explanation": "Einstein warned Roosevelt that Nazi Germany had discovered nuclear fission and could build a single bomb capable of destroying an entire port.",
                    "explanation_hi": "आइंस्टीन ने चेतावनी दी कि नाजी जर्मनी परमाणु विखंडन की खोज कर चुका है और एक ही बम से पूरे बंदरगाह को नष्ट कर सकता है।",
                    "explanation_gu": "આઇન્સ્ટાઇને ચેતવણી આપી કે નાઝી જર્મની અણુ વિખંડન શોધી ચૂક્યું છે અને તે આખા બંદરનો નાશ કરી શકે છે."
                }
            ]
        },
        5: {
            "title": "Chapter 5: The Snake and the Mirror & A Legend of the Northland",
            "blocks": [
                {
                    "id": "KOBJ_CLASS9_ENG_CH5_HOOK",
                    "type": "real_world_example",
                    "title": "Step 1: Hook - Cobra Looking in the Mirror!",
                    "title_hi": "चरण 1: हुक - शीशे में देखता कोबरा!",
                    "title_gu": "પગલું 1: હૂક - અરીસામાં જોતો નાગ!",
                    "body": "A homeopathic doctor sitting in his room suddenly feels a heavy cobra slither down his shoulder and coil around his arm! But instead of biting him, the cobra looks into a mirror on the table, becomes mesmerized by its own reflection, and uncoils to admire itself closely!",
                    "body_hi": "अपने कमरे में बैठे एक होम्योपैथिक डॉक्टर के कंधे से अचानक एक भारी नाग नीचे सरकता है और उसकी बांह पर लपट जाता है! लेकिन डॉक्टर को काटने के बजाय, सांप मेज पर लगे शीशे में देखता है, अपने प्रतिबिंब से मंत्रमुग्ध हो जाता है और खुद को पास से देखने के लिए नीचे उतर जाता है!",
                    "body_gu": "રૂમમાં બેઠેલા હોમિયોપેથિક ડોક્ટરના ખભા પરથી અચાનક એક ભારે નાગ નીચે સરે છે અને હાથ પર વીંટળાઈ જાય છે! પરંતુ કરડવાને બદલે, નાગ ટેબલ પરના અરીસામાં જુએ છે, પોતાના પ્રતિબિંબથી મંત્રમુગ્ધ થઈ જાય છે અને નજીકથી જોવા નીચે ઉતરે છે!"
                },
                {
                    "id": "KOBJ_CLASS9_ENG_CH5_THEORY_SUMMARY",
                    "type": "theory",
                    "title": "Step 4: Reveal - Summary of Snake & Mirror & Northland Legend",
                    "title_hi": "चरण 4: प्रकटीकरण - सांप और शीशे का सारांश और नॉर्थलैंड की कथा",
                    "title_gu": "પગલું 4: પર્દાફાશ - નાગ અને અરીસાનો સારાંશ",
                    "body": "1. **Author**: Vaikom Muhammad Basheer.\n2. **Tone**: Humorous and ironic account of vanity and fear.\n3. **Poem - A Legend of the Northland** (Phoebe Cary): A ballad about a greedy old woman turned into a woodpecker by Saint Peter for refusing to share a tiny cake.",
                    "body_hi": "1. **लेखक**: वैकोम मोहम्मद बशीर।\n2. **स्वर**: घमंड और डर का हास्यप्रद विवरण।\n3. **कविता - ए लीजेंड ऑफ द नॉर्थलैंड**: एक लालची बूढ़ी औरत की गाथा जिसे सेंट पीटर ने छोटे केक को साझा न करने पर कठफोड़वा पक्षी बना दिया था।",
                    "body_gu": "1. **લેખક**: વૈકોમ મોહમ્મદ બશીર।\n2. **સૂર**: અભિમાન અને ડરની રમૂજી વાર્તા।\n3. **કવિતા**: એક લોભી વૃદ્ધ સ્ત્રીની વાર્તા જેને સેન્ટ પીટરે નાની રોટલી પણ ન આપતાં લક્કડખોદ પક્ષી બનાવી દીધી હતી।"
                },
                {
                    "id": "KOBJ_CLASS9_ENG_CH5_EX1",
                    "type": "quiz",
                    "title": "Textbook Exercise: St Peter's Curse",
                    "title_hi": "पाठ्यपुस्तक अभ्यास: सेंट पीटर का श्राप",
                    "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય: સેન્ટ પીટરનો શાપ",
                    "question": "Why did Saint Peter punish the old woman in 'A Legend of the Northland'?",
                    "question_hi": "सेंट पीटर ने 'ए लीजेंड ऑफ द नॉर्थलैंड' में बूढ़ी औरत को सजा क्यों दी?",
                    "question_gu": "સેન્ટ પીટરે વૃદ્ધ સ્ત્રીને શા માટે શિક્ષા આપી?",
                    "options": [
                        "Because she was extremely greedy and refused to give even a tiny cake",
                        "Because she stole his money",
                        "Because she insulted him publicly",
                        "Because she refused to let him enter her house"
                    ],
                    "options_hi": [
                        "क्योंकि वह अत्यंत लालची थी और एक छोटा सा केक भी देने से मना कर दिया",
                        "क्योंकि उसने उसके पैसे चुरा लिए थे",
                        "क्योंकि उसने सार्वजनिक रूप से उनका अपमान किया था",
                        "क्योंकि उसने उसे अपने घर में प्रवेश नहीं करने दिया"
                    ],
                    "options_gu": [
                        "કારણ કે તે અત્યંત લોભી હતી અને નાનો કેક આપવાની પણ ના પાડી દીધી",
                        "કારણ કે તેણે પૈસા ચોરી લીધા હતા",
                        "કારણ કે તેણે તેમનું અપમાન કર્યું હતું",
                        "કારણ કે તેણે ઘરમાં પ્રવેશવા ન દીધા"
                    ],
                    "correct_index": 0,
                    "explanation": "Saint Peter was hungry and tired. The old woman baked small cakes, but every time she found them too big to give away. Her extreme greed angered Saint Peter.",
                    "explanation_hi": "सेंट पीटर भूखे थे। बूढ़ी औरत ने छोटे केक बनाए, लेकिन हर बार उसे वे देने के लिए बहुत बड़े लगे। उसके लालच ने सेंट पीटर को क्रोधित कर दिया।",
                    "explanation_gu": "સેન્ટ પીટર ભૂખ્યા હતા। વૃદ્ધ સ્ત્રીના લોભથી ક્રોધિત થઈને તેમણે તેને શિક્ષા આપી."
                }
            ]
        },
        6: {
            "title": "Chapter 6: My Childhood & No Men Are Foreign",
            "blocks": [
                {
                    "id": "KOBJ_CLASS9_ENG_CH6_HOOK",
                    "type": "real_world_example",
                    "title": "Step 1: Hook - The Missile Man's Childhood in Rameswaram",
                    "title_hi": "चरण 1: हुक - रामेश्वरम में मिसाइल मैन का बचपन",
                    "title_gu": "પગલું 1: હૂક - રામેશ્વરમના મિસાઇલ મેનનું બાળપણ",
                    "body": "APJ Abdul Kalam grew up in a middle-class Tamil Muslim family in Rameswaram. His best friends were Hindu Brahmins (Ramanadha Sastry, Aravindan, Sivaprakasan). Despite religious differences, they lived in total communal harmony and mutual respect!",
                    "body_hi": "एपीजे अब्दुल कलाम रामेश्वरम में एक मध्यमवर्गीय तमिल मुस्लिम परिवार में बड़े हुए। उनके सबसे अच्छे दोस्त हिंदू ब्राह्मण थे। धार्मिक मतभेदों के बावजूद, वे पूर्ण सांप्रदायिक सौहार्द और आपसी सम्मान में रहते थे!",
                    "body_gu": "એપીજે અબ્દુલ કલામ રામેશ્વરમના તમિલ મુસ્લિમ પરિવારમાં ઉછર્યા। તેમના શ્રેષ્ઠ મિત્રો હિન્દુ બ્રાહ્મણ હતા। ધાર્મિક તફાવતો છતાં, તેઓ સાંપ્રદાયિક સૌહાર્દ સાથે રહેતા હતા!"
                },
                {
                    "id": "KOBJ_CLASS9_ENG_CH6_THEORY_SUMMARY",
                    "type": "theory",
                    "title": "Step 4: Reveal - Kalam's Autobiography & James Kirkup's Poem",
                    "title_hi": "चरण 4: प्रकटीकरण - कलाम की आत्मकथा और जेम्स किर्कप की कविता",
                    "title_gu": "પગલું 4: પર્દાફાશ - કલામની આત્મકથા અને જેમ્સ્ કિરકપની કવિતા",
                    "body": "1. **Autobiography**: Excerpt from *Wings of Fire* by Dr. APJ Abdul Kalam.\n2. **Themes**: Communal harmony, dignity of labor, role of mentors (SivaSubramania Iyer, his science teacher).\n3. **Poem - No Men Are Foreign** (James Kirkup): Universal brotherhood. Beneath all uniforms, a single body breathes. War defiles the common Earth.",
                    "body_hi": "1. **आत्मकथा**: डॉ. एपीजे अब्दुल कलाम की पुस्तक *विंग्स ऑफ फायर* का अंश।\n2. **विषय**: सांप्रदायिक सौहार्द, श्रम की गरिमा, आदरणीय गुरुओं की भूमिका।\n3. **कविता - नो मेन आर फॉरेन**: सार्वभौमिक भाईचारा। सभी वर्दियों के नीचे एक ही शरीर सांस लेता है। युद्ध पृथ्वी को दूषित करता है।",
                    "body_gu": "1. **આત્મકથા**: ડો. એપીજે અબ્દુલ કલામની પુસ્તક *વિંગ્સ ઓફ ફાયર* નો ભાગ।\n2. **વિષય**: સાંપ્રદાયિક સૌહાર્દ, શ્રમનું ગૌરવ, શિક્ષકોની ભૂમિકા।\n3. **કવિતા**: સાર્વત્રિક ભાઈચારો। બધી વરrestore નીચે એક જ માનવ શરીર શ્વાસ લે છે।"
                },
                {
                    "id": "KOBJ_CLASS9_ENG_CH6_EX1",
                    "type": "quiz",
                    "title": "Textbook Exercise: Science Teacher's Wife Incident",
                    "title_hi": "पाठ्यपुस्तक अभ्यास: विज्ञान शिक्षक की पत्नी की घटना",
                    "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય: વિજ્ઞાન શિક્ષકની પત્નીની ઘટના",
                    "question": "How did Sivasubramania Iyer's conservative wife react when Kalam was invited for dinner?",
                    "question_hi": "जब कलाम को रात के खाने पर आमंत्रित किया गया तो शिवसुब्रमण्यम अय्यर की रूढ़िवादी पत्नी ने क्या प्रतिक्रिया दी?",
                    "question_gu": "જ્યારે કલામને રાત્રિભોજન માટે આમંત્રિત કરવામાં આવ્યા ત્યારે વિજ્ઞાન શિક્ષકની પત્નીએ શું પ્રતિક્રિયા આપી?",
                    "options": [
                        "She refused to serve a Muslim boy in her ritually pure kitchen",
                        "She welcomed him warmly and served special sweets",
                        "She cooked a grand feast for everyone",
                        "She asked him to change his clothes first"
                    ],
                    "options_hi": [
                        "उसने अपनी पवित्र रसोई में एक मुस्लिम लड़के को खाना परोसने से मना कर दिया",
                        "उसने उसका गर्मजोशी से स्वागत किया और विशेष मिठाई परोसी",
                        "उसने सभी के लिए एक भव्य दावत पकाई",
                        "उसने उससे पहले अपने कपड़े बदलने को कहा"
                    ],
                    "options_gu": [
                        "તેણીએ પોતાના પવિત્ર રસોડામાં મુસ્લિમ છોકરાને પીરસવાની ના પાડી દીધી",
                        "તેણીએ તેનું ઉષ્માભર્યું સ્વાગત કર્યું",
                        "તેણીએ ભવ્ય રસોઈ બનાવી",
                        "તેણીએ પહેલા કપડાં બદલવા કહ્યું"
                    ],
                    "correct_index": 0,
                    "explanation": "His teacher's wife initially refused to serve Kalam in her kitchen due to orthodox religious beliefs. However, Iyer served Kalam himself, sat beside him, and invited him again next week—when his wife served Kalam inside the kitchen herself!",
                    "explanation_hi": "शिक्षक की पत्नी ने शुरू में मना कर दिया था। लेकिन अय्यर ने खुद कलाम को खाना परोसा और अगले हफ्ते फिर आमंत्रित किया—जब उनकी पत्नी ने खुद रसोई में कलाम को खाना परोसा!",
                    "explanation_gu": "શિક્ષકની પત્નીએ શરૂઆતમાં ના પાડી હતી। પરંતુ અય્યરે પોતે કલામને પીરસ્યું અને બીજા અઠવાડિયે પત્નીએ પોતે રસોડામાં પીરસ્યું."
                }
            ]
        },
        7: {
            "title": "Chapter 7: Reach for the Top & On Killing a Tree",
            "blocks": [
                {
                    "id": "KOBJ_CLASS9_ENG_CH7_HOOK",
                    "type": "real_world_example",
                    "title": "Step 1: Hook - Conquering Everest Twice",
                    "title_hi": "चरण 1: हुक - एवरेस्ट पर दो बार विजय",
                    "title_gu": "પગલું 1: હૂક - એવરેસ્ટ પર બે વાર વિજય",
                    "body": "Santosh Yadav was born in a traditional patriarchal village in Haryana where girls were forced into early marriage. She resisted, studied in Delhi, joined Uttarkashi Mountaineering Institute, and became the ONLY woman in the world to scale Mount Everest TWICE!",
                    "body_hi": "संतोष यादव का जन्म हरियाणा के एक पारंपरिक गांव में हुआ था जहाँ लड़कियों की कम उम्र में शादी कर दी जाती थी। उन्होंने विरोध किया, दिल्ली में पढ़ाई की, उत्तरकाशी पर्वतारोहण संस्थान में शामिल हुईं और दुनिया की एकमात्र महिला बनीं जिन्होंने माउंट एवरेस्ट पर दो बार चढ़ाई की!",
                    "body_gu": "સંતોષ યાદવનો જન્મ હરિયાણાના ગામમાં થયો હતો જ્યાં છોકરીઓના નાની વયે લગ્ન કરાવવામાં આવતા। તેણે વિરોધ કર્યો, દિલ્હીમાં અભ્યાસ કર્યો અને વિશ્વની એકમાત્ર મહિલા બની જેણે માઉન્ટ એવરેસ્ટ પર બે વાર ચઢાઈ કરી!"
                },
                {
                    "id": "KOBJ_CLASS9_ENG_CH7_THEORY_SUMMARY",
                    "type": "theory",
                    "title": "Step 4: Reveal - Santosh Yadav, Maria Sharapova & Gieve Patel's Poem",
                    "title_hi": "चरण 4: प्रकटीकरण - संतोष यादव, मारिया शारापोवा और गीव पटेल की कविता",
                    "title_gu": "પગલું 4: પર્દાફાશ - સંતોષ યાદવ, મારિયા શારાપોવા અને કવિતા",
                    "body": "1. **Part I - Santosh Yadav**: Determination, environmental concern (collected 500 kg garbage from Everest).\n2. **Part II - Maria Sharapova**: Russian tennis icon who reached World No. 1 at age 18 through sacrifices in Siberia and USA.\n3. **Poem - On Killing a Tree** (Gieve Patel): A tree cannot be killed by a simple jab of knife; its roots must be pulled out completely from anchoring earth.",
                    "body_hi": "1. **भाग I - संतोष यादव**: दृढ़ संकल्प, पर्यावरण संबंधी चिंता (एवरेस्ट से 500 किग्रा कचरा एकत्र किया)।\n2. **भाग II - मारिया शारापोवा**: रूसी टेनिस आइकन जो 18 साल की उम्र में दुनिया की नंबर 1 खिलाड़ी बनीं।\n3. **कविता - ऑन किलिंग ए ट्री**: एक पेड़ को चाकू के एक वार से नहीं मारा जा सकता; इसकी जड़ों को पृथ्वी से पूरी तरह उखाड़ना पड़ता है।",
                    "body_gu": "1. **ભાગ I - સંતોષ યાદવ**: દ્રઢ મનોબળ, પર્યાવરણીય કાળજી (એવરેસ્ટમાંથી 500 kg કચરો એકઠો કર્યો) ।\n2. **ભાગ II - મારિયા શારાપોવા**: રશિયન ટેનિસ સ્ટાર જે 18 વર્ષે વિશ્વની નંબર 1 બની।\n3. **કવિતા**: ઝાડને માત્ર કાપવાથી મારી શકાતું નથી; તેના મૂળિયાં જમીનમાંથી પૂરા ઉખાડવા પડે છે."
                },
                {
                    "id": "KOBJ_CLASS9_ENG_CH7_EX1",
                    "type": "quiz",
                    "title": "Textbook Exercise: Santosh Yadav's Environmentalism",
                    "title_hi": "पाठ्यपुस्तक अभ्यास: संतोष यादव की पर्यावरण चेतना",
                    "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય: સંતોષ યાદવની પર્યાવરણ ચેતના",
                    "question": "What shows Santosh Yadav's concern for the environment during her Everest expedition?",
                    "question_hi": "एवरेस्ट अभियान के दौरान संतोष यादव की पर्यावरण के प्रति चिंता क्या दर्शाती है?",
                    "question_gu": "એવરેસ્ટ અભિયાન દરમિયાન સંતોષ યાદવની પર્યાવરણ પ્રત્યેની કાળજી શું દર્શાવે છે?",
                    "options": [
                        "She collected and brought down 500 kg of garbage from Everest",
                        "She planted trees on Everest peak",
                        "She banned plastic bottles during climb",
                        "She wrote a book on mountain pollution"
                    ],
                    "options_hi": [
                        "उन्होंने एवरेस्ट से 500 किलोग्राम कचरा एकत्र किया और नीचे लाया",
                        "उन्होंने एवरेस्ट की चोटी पर पेड़ लगाए",
                        "उन्होंने चढ़ाई के दौरान प्लास्टिक की बोतलों पर प्रतिबंध लगा दिया",
                        "उन्होंने पर्वतीय प्रदूषण पर एक किताब लिखी"
                    ],
                    "options_gu": [
                        "તેણે એવરેસ્ટમાંથી 500 kg કચરો એકઠો કરી નીચે લાવ્યો",
                        "તેણે એવરેસ્ટ શિખર પર વૃક્ષો વાવ્યા",
                        "તેણે પ્લાસ્ટિક બોટલ પર બૅન મૂક્યો",
                        "તેણે પુસ્તક લખ્યું"
                    ],
                    "correct_index": 0,
                    "explanation": "Santosh Yadav was a passionate environmentalist who collected and brought down 500 kg of trash left behind by other climbers on Mount Everest.",
                    "explanation_hi": "संतोष यादव एक पर्यावरणविद् थीं, जिन्होंने माउंट एवरेस्ट पर अन्य पर्वतारोहियों द्वारा छोड़े गए 500 किलोग्राम कचरे को एकत्र किया और नीचे लाया।",
                    "explanation_gu": "સંતોષ યાદવે માઉન્ટ એવરેસ્ટમાંથી 500 kg કચરો એકઠો કરી નીચે લાવ્યો હતો."
                }
            ]
        },
        8: {
            "title": "Chapter 8: Kathmandu & A Slumber Did My Spirit Seal",
            "blocks": [
                {
                    "id": "KOBJ_CLASS9_ENG_CH8_HOOK",
                    "type": "real_world_example",
                    "title": "Step 1: Hook - Two Temples of Kathmandu",
                    "title_hi": "चरण 1: हुक - काठमांडू के दो मंदिर",
                    "title_gu": "પગલું 1: હૂક - કાઠમંડુના બે મંદિરો",
                    "body": "Travel writer Vikram Seth visits two famous holy sites in Kathmandu: Pashupatinath Temple (Atmosphere of febrile confusion, saffron robes, monkeys, and sacred chaos) and Baudhnath Stupa (A haven of quietness and serenity amidst busy streets).",
                    "body_hi": "यात्रा लेखक विक्रम सेठ काठमांडू के दो प्रसिद्ध धार्मिक स्थलों का दौरा करते हैं: पशुपतिनाथ मंदिर (उथल-पुथल, भगवा वस्त्र, बंदर और पवित्र अराजकता का माहौल) और बौद्धनाथ स्तूप (शांत और शांति का प्रतीक)।",
                    "body_gu": "પ્રવાસ લેખક વિક્રમ સેઠ કાઠમંડુના બે પવિત્ર સ્થળોની મુલાકાત લે છે: પશુપતિનાથ મંદિર (કોલાહલ અને ધાર્મિક ઉત્સાહ) અને બૌદ્ધનાથ સ્તૂપ (શાંતિ અને પ્રશાંતિનું ધામ) ।"
                },
                {
                    "id": "KOBJ_CLASS9_ENG_CH8_THEORY_SUMMARY",
                    "type": "theory",
                    "title": "Step 4: Reveal - Kathmandu Travelogue & Wordsworth's Poem",
                    "title_hi": "चरण 4: प्रकटीकरण - काठमांडू यात्रा वृत्तांत और वर्ड्सवर्थ की कविता",
                    "title_gu": "પગલું 4: પર્દાફાશ - કાઠમંડુ પ્રવાસ વર્ણન અને વર્ડ્સવર્થની કવિતા",
                    "body": "1. **Travelogue**: Excerpt from *Heaven Lake* by Vikram Seth.\n2. **Flute Seller**: The author is enchanted by a flute seller playing melodious music peacefully amidst market noise.\n3. **Poem - A Slumber Did My Spirit Seal** (William Wordsworth): Elegiac poem on the death of a loved one (Lucy). She is now beyond earthly fears, merged with rocks, stones, and trees.",
                    "body_hi": "1. **यात्रा वृत्तांत**: विक्रम सेठ द्वारा लिखित *हेवन लेक* का अंश।\n2. **बांसुरी विक्रेता**: लेखक बाजार के शोर के बीच एक बांसुरी विक्रेता के सुरीले संगीत पर मोहित हो जाता है।\n3. **कविता - ए स्लंबर डिड माई स्पिरिट सील** (विलियम वर्ड्सवर्थ): किसी प्रियजन की मृत्यु पर शोक कविता।",
                    "body_gu": "1. **પ્રવાસ વર્ણન**: વિક્રમ સેઠના પુસ્તકમાંથી ભાગ।\n2. **વાંસળી વેચનાર**: લેખક બજારના ઘોંઘાટ વચ્ચે વાંસળીના સૂરથી મંત્રમુગ્ધ થાય છે।\n3. **કવિતા**: પ્રિયજનના મૃત્યુ પર શોકકાવ્ય।"
                },
                {
                    "id": "KOBJ_CLASS9_ENG_CH8_EX1",
                    "type": "quiz",
                    "title": "Textbook Exercise: Pashupatinath Signboard",
                    "title_hi": "पाठ्यपुस्तक अभ्यास: पशुपतिनाथ का साइनबोर्ड",
                    "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય: પશુપતિનાથનું સાઇનબોર્ડ",
                    "question": "What does the signboard at Pashupatinath Temple announce?",
                    "question_hi": "पशुपतिनाथ मंदिर का साइनबोर्ड क्या घोषणा करता है?",
                    "question_gu": "પશુપતિનાથ મંદિરનું સાઇનબોર્ડ શું જાહેર કરે છે?",
                    "options": [
                        "Entrance for the Hindus only",
                        "Entrance for all tourists free of cost",
                        "Photography strictly prohibited",
                        "Shoes not allowed inside temple complex"
                    ],
                    "options_hi": [
                        "केवल हिंदुओं के लिए प्रवेश",
                        "सभी पर्यटकों के लिए निःशुल्क प्रवेश",
                        "फोटोग्राफी सख्त मना है",
                        "मंदिर परिसर के अंदर जूते पहनने की अनुमति नहीं है"
                    ],
                    "options_gu": [
                        "માત્ર હિંદુઓ માટે પ્રવેશ",
                        "બધા પ્રવાસીઓ માટે મફત પ્રવેશ",
                        "ફોટોગ્રાફી પર મનાઈ",
                        "ચપ્પલ પહેરવાની મનાઈ"
                    ],
                    "correct_index": 0,
                    "explanation": "At Pashupatinath temple, a sign proclaims 'Entrance for the Hindus only', restricting non-Hindus from entering the inner shrine.",
                    "explanation_hi": "पशुपतिनाथ मंदिर में एक बोर्ड लगा है: 'केवल हिंदुओं के लिए प्रवेश'।",
                    "explanation_gu": "પશુપતિનાથ મંદિરમાં બોર્ડ છે: 'માત્ર હિંદુઓ માટે પ્રવેશ'."
                }
            ]
        },
        9: {
            "title": "Chapter 9: If I Were You",
            "blocks": [
                {
                    "id": "KOBJ_CLASS9_ENG_CH9_HOOK",
                    "type": "real_world_example",
                    "title": "Step 1: Hook - Outwitting an Intruder",
                    "title_hi": "चरण 1: हुक - एक घुसपैठिए को मात देना",
                    "title_gu": "પગલું 1: હૂક - ઘૂસણખોરને માત આપવી",
                    "body": "Gerrard, a playwright living in a lonely cottage, is confronted by an armed criminal intruder who wants to murder Gerrard and steal his identity to escape the police. Instead of panicking, Gerrard invents a clever story that he himself is a murderer on the run, tricks the intruder into a cupboard, and locks him inside!",
                    "body_hi": "एक सुनसान कॉटेज में रहने वाले नाटककार जेरार्ड का सामना एक सशस्त्र अपराधी घुसपैठिए से होता है जो पुलिस से बचने के लिए जेरार्ड की हत्या करके उसकी पहचान चुराना चाहता है। घबराने के बजाय, जेरार्ड एक कहानी गढ़ता है कि वह खुद एक भगौड़ा हत्यारा है, घुसपैठिए को एक अलमारी में फंसाता है और उसे अंदर बंद कर देता है!",
                    "body_gu": "એકાંત કોટેજમાં રહેતા નાટકકાર જેરાર્ડનો સામનો હથિયારધારી ગુનેગાર ઘૂસણખોર સાથે થાય છે જે પોલીસથી બચવા જેરાર્ડની હત્યા કરી તેની ઓળખ ચોરવા માંગે છે। ગભરાવાને બદલે, જેરાર્ડ તેને કબાટમાં પૂરી દે છે!"
                },
                {
                    "id": "KOBJ_CLASS9_ENG_CH9_THEORY_SUMMARY",
                    "type": "theory",
                    "title": "Step 4: Reveal - Summary & Themes of 'If I Were You'",
                    "title_hi": "चरण 4: प्रकटीकरण - 'इफ आई वर यू' का सारांश और विषय",
                    "title_gu": "પગલું 4: પર્દાફાશ - 'ઇફ આઇ વર યુ' નો સારાંશ અને વિષયો",
                    "body": "1. **Playwright**: Douglas James.\n2. **Genre**: One-act play / Suspense Comedy.\n3. **Themes**: Presence of mind, intelligence over physical threat, cool-headed wit in crisis.\n4. **Climax**: Gerrard tricks the intruder into looking inside a cupboard (claiming it is an escape door) and locks him in before phoning the police.",
                    "body_hi": "1. **नाटककार**: डगलस जेम्स।\n2. **शैली**: एकांकी नाटक / सस्पेंस कॉमेडी।\n3. **विषय**: उपस्थिति की समझ (Presence of mind), संकट में ठंडे दिमाग की बुद्धि।\n4. **चरमोत्कर्ष**: जेरार्ड घुसपैठिए को अलमारी के अंदर देखने का झांसा देता है और पुलिस को फोन करने से पहले उसे अंदर बंद कर देता है।",
                    "body_gu": "1. **નાટકકાર**: ડગલસ જેમ્સ।\n2. **શૈલી**: એકાંકી નાટક / સસ્પેન્સ કોમેડી।\n3. **વિષય**: હાજરબુદ્ધિ, મુશ્કેલીમાં શાંત મગજે કામ લેવું।\n4. **અંત**: જેરાર્ડ ઘૂસણખોરને કબાટમાં પૂરી દે છે અને પોલીસને ફોન કરે છે."
                },
                {
                    "id": "KOBJ_CLASS9_ENG_CH9_EX1",
                    "type": "quiz",
                    "title": "Textbook Exercise: Intruder's Plan",
                    "title_hi": "पाठ्यपुस्तक अभ्यास: घुसपैठिए की योजना",
                    "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય: ઘૂસણખોરની યોજના",
                    "question": "Why did the intruder want to assume Gerrard's identity?",
                    "question_hi": "घुसपैठिया जेरार्ड की पहचान क्यों अपनाना चाहता था?",
                    "question_gu": "ઘૂસણખોર જેરાર્ડની ઓળખ શા માટે અપનાવવા માંગતો હતો?",
                    "options": [
                        "Because he was wanted for murder and wanted to live freely as Gerrard",
                        "Because he wanted Gerrard's money",
                        "Because he wanted to become a playwright",
                        "Because he wanted to travel abroad"
                    ],
                    "options_hi": [
                        "क्योंकि वह हत्या के लिए वांछित था और जेरार्ड के रूप में स्वतंत्र रूप से रहना चाहता था",
                        "क्योंकि वह जेरार्ड के पैसे चाहता था",
                        "क्योंकि वह नाटककार बनना चाहता था",
                        "क्योंकि वह विदेश यात्रा करना चाहता था"
                    ],
                    "options_gu": [
                        "કારણ કે તે ખૂનના કેસમાં પોલીસથી બચવા જેરાર્ડ બની જીવવા માંગતો હતો",
                        "કારણ કે તેને પૈસા જોઈતા હતા",
                        "કારણ કે તે નાટકકાર બનવા માંગતો હતો",
                        "કારણ કે તે પરદેશ જવા માંગતો હતો"
                    ],
                    "correct_index": 0,
                    "explanation": "The intruder had killed a cop and was being hunted by the police. Since Gerrard lived alone and was similar in build, the intruder planned to kill Gerrard and live peacefully under his name.",
                    "explanation_hi": "घुसपैठिए ने एक पुलिस वाले को मार डाला था। चूंकि जेरार्ड अकेला रहता था और कद-काठी में समान था, इसलिए उसने जेरार्ड को मारकर उसके नाम से रहने की योजना बनाई।",
                    "explanation_gu": "ઘૂસણખોરે પોલીસવાળાનું ખૂન કર્યું હતું। તેથી જેરાર્ડની હત્યા કરી તેની ઓળખ ચોરવાની યોજના હતી."
                }
            ]
        },
        10: {
            "title": "Chapter 10: Moments Supplementary Reader Highlights",
            "blocks": [
                {
                    "id": "KOBJ_CLASS9_ENG_CH10_HOOK",
                    "type": "real_world_example",
                    "title": "Step 1: Hook - The Lost Child at the Spring Fair",
                    "title_hi": "चरण 1: हुक - वसंत मेले में खोया हुआ बच्चा",
                    "title_gu": "પગલું 1: હૂક - વસંતના મેળામાં ખોવાયેલું બાળક",
                    "body": "A small child goes to a village fair with his parents. He desires toys, sweets, garlands, and rides. But the moment he gets separated from his parents, he loses interest in everything! A kind stranger offers him all the sweets and rides, but the child only cries: 'I want my mother, I want my father!'",
                    "body_hi": "एक छोटा बच्चा अपने माता-पिता के साथ गांव के मेले में जाता है। वह खिलौने, मिठाइयाँ और झूले चाहता है। लेकिन जिस क्षण वह अपने माता-पिता से अलग होता है, उसकी हर चीज में रुचि खत्म हो जाती है! एक अजनबी उसे सब कुछ देने की पेशकश करता है, लेकिन बच्चा केवल रोता है: 'मुझे मेरी माँ चाहिए, मुझे मेरे पिता चाहिए!'",
                    "body_gu": "એક નાનું બાળક માતાપિતા સાથે મેળામાં જાય છે। તેને રમકડાં, મીઠાઈઓ અને ચકડોળ જોઈતી હોય છે। પરંતુ માતાપિતાથી વિખૂટું પડતાં જ તેને કશામાં રસ રહેતો નથી! અજાણ્યો માણસ તેને બધું આપવાની ઓફર કરે છે, છતાં બાળક રડે છે: 'મારે મારી મમ્મી જોઈએ, પપ્પા જોઈએ!'"
                },
                {
                    "id": "KOBJ_CLASS9_ENG_CH10_THEORY_SUMMARY",
                    "type": "theory",
                    "title": "Step 4: Reveal - Highlights of 'The Lost Child' & 'The Happy Prince'",
                    "title_hi": "चरण 4: प्रकटीकरण - 'द लॉस्ट चाइल्ड' और 'द हैप्पी प्रिंस' की मुख्य बातें",
                    "title_gu": "પગલું 4: પર્દાફાશ - સપ્લીમેન્ટ્રી સ્ટોરીઝ",
                    "body": "1. **The Lost Child** (Mulk Raj Anand): Parental love is the supreme joy in a child's life; material desires are secondary.\n2. **The Happy Prince** (Oscar Wilde): True beauty lies in selflessness and sacrifice. The gilded statue of Happy Prince and the little Swallow give away all gold and gems to help the poor.",
                    "body_hi": "1. **द लॉस्ट चाइल्ड** (मुल्क राज आनंद): माता-पिता का प्यार बच्चे के जीवन में सर्वोच्च आनंद है; भौतिक इच्छाएं द्वितीयक हैं।\n2. **द हैप्पी प्रिंस** (ऑस्कर वाइल्ड): सच्ची सुंदरता स्वार्थहीनता और बलिदान में निहित है। हैप्पी प्रिंस की मूर्ति और निगल (Swallow) पक्षी गरीबों की मदद के लिए अपना सारा सोना और रत्न दे देते हैं।",
                    "body_gu": "1. **દ લોસ્ટ ચાઇલ્ડ** (મુલ્ક રાજ આણંદ): માતાપિતાનો પ્રેમ બાળકના જીવનમાં સર્વોચ્ચ છે।\n2. **દ હેપી પ્રિન્સ** (ઓસ્કર વાઇલ્ડ): સાચી સુંદરતા સ્વાર્થહીનતા અને ત્યાગમાં છે। મૂર્તિ અને પક્ષી ગરીબોની મદદ માટે બધું દાન કરે છે."
                },
                {
                    "id": "KOBJ_CLASS9_ENG_CH10_EX1",
                    "type": "quiz",
                    "title": "Textbook Exercise: The Swallow's Sacrifice",
                    "title_hi": "पाठ्यपुस्तक अभ्यास: अबबील (Swallow) का बलिदान",
                    "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય: પક્ષીનો ત્યાગ",
                    "question": "Why did the little Swallow stay back with the Happy Prince instead of flying to Egypt?",
                    "question_hi": "छोटा अबबील (Swallow) मिस्र उड़ने के बजाय हैप्पी प्रिंस के साथ क्यों रुक गया?",
                    "question_gu": "નાનું પક્ષી ઇજિપ્ત જવાને બદલે હેપી પ્રિન્સ પાસે શા માટે રોકાઈ ગયું?",
                    "options": [
                        "Because the Happy Prince was now blind after giving away his sapphire eyes",
                        "Because the weather in Egypt was too hot",
                        "Because he broke his wings",
                        "Because he found gold in the statue"
                    ],
                    "options_hi": [
                        "क्योंकि अपनी नीलम आंखें देने के बाद हैप्पी प्रिंस अब अंधा हो गया था",
                        "क्योंकि मिस्र में मौसम बहुत गर्म था",
                        "क्योंकि उसके पंख टूट गए थे",
                        "क्योंकि उसे मूर्ति में सोना मिला था"
                    ],
                    "options_gu": [
                        "કારણ કે હેપી પ્રિન્સે પોતાની રત્ન આંખો દાન કરતાં તે અંધ બની ગયો હતો",
                        "કારણ કે ઇજિપ્તમાં ગરમી હતી",
                        "કારણ કે તેની પાંખો તૂટી ગઈ હતી",
                        "કારણ કે તેને સોનું મળ્યું હતું"
                    ],
                    "correct_index": 0,
                    "explanation": "The Happy Prince gave away both his sapphire eyes to help a poor playwright and a matchgirl. Touched by his nobility, the Swallow promised to stay with him forever to be his eyes.",
                    "explanation_hi": "हैप्पी प्रिंस ने एक गरीब नाटककार और माचिस वाली लड़की की मदद के लिए अपनी नीलम आंखें दान कर दीं। इस महानता से प्रभावित होकर अबबील ने हमेशा उसके साथ रहने का वादा किया।",
                    "explanation_gu": "હેપી પ્રિન્સે પોતાની આંખો ગરીબો માટે દાન કરી દીધી। આથી પક્ષી તેની સાથે જ રોકાઈ ગયું."
                }
            ]
        }
    }

    for ch_num, data in chapters_data.items():
        blocks = data["blocks"]

        # Ensure trilingual fields on all blocks
        for b in blocks:
            if isinstance(b, dict):
                if "title" in b:
                    if "title_hi" not in b or not b["title_hi"]: b["title_hi"] = b["title"]
                    if "title_gu" not in b or not b["title_gu"]: b["title_gu"] = b["title"]
                body_val = b.get("body") or b.get("content") or ""
                if body_val:
                    if "body_hi" not in b: b["body_hi"] = body_val
                    if "body_gu" not in b: b["body_gu"] = body_val

        # Target learning module folder
        mod_dir = f"app_core/learning_modules/gseb_class9_english_ch{ch_num}"
        os.makedirs(mod_dir, exist_ok=True)
        mod_file = os.path.join(mod_dir, "blocks.json")
        with open(mod_file, "w", encoding="utf-8") as f:
            json.dump(blocks, f, ensure_ascii=False, indent=2)

        # Target NCERT chapter JSON
        ch_file = f"app_core/chapters/ncert_class9_english_ch{ch_num}.json"
        with open(ch_file, "w", encoding="utf-8") as f:
            json.dump(blocks, f, ensure_ascii=False, indent=2)

        # Target Assessment Question Bank
        quizzes = [b for b in blocks if b.get("type") == "quiz"]
        assessment_questions = []
        for q in quizzes:
            assessment_questions.append({
                "id": q["id"],
                "question": q["question"],
                "question_hi": q.get("question_hi", ""),
                "question_gu": q.get("question_gu", ""),
                "options": q["options"],
                "options_hi": q.get("options_hi", []),
                "options_gu": q.get("options_gu", []),
                "correct_index": q["correct_index"],
                "explanation": q.get("explanation", ""),
                "explanation_hi": q.get("explanation_hi", ""),
                "explanation_gu": q.get("explanation_gu", "")
            })

        assess_file = f"app_core/assessment/gseb_class9_english_ch{ch_num}_questions.json"
        with open(assess_file, "w", encoding="utf-8") as f:
            json.dump(assessment_questions, f, ensure_ascii=False, indent=2)

        print(f"English Ch {ch_num:2d}: {len(blocks):2d} blocks, {len(quizzes):2d} quizzes synced to learning module, NCERT chapter JSON, and assessment bank.")

if __name__ == "__main__":
    generate_english_chapters()
