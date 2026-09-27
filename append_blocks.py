import json

new_blocks = [
    {
      "id": "KOBJ_GSEB_C7_SOC_CH3_EX1_1",
      "type": "flashcard",
      "title": "Exercise 1.1",
      "title_hi": "अभ्यास 1.1",
      "title_gu": "સ્વાધ્યાય 1.1",
      "front": "When and between whom was the 1st battle of Panipat fought?",
      "front_hi": "पानीपत का प्रथम युद्ध कब और किसके बीच लड़ा गया था?",
      "front_gu": "પાણિપતનું પ્રથમ યુદ્ધ ક્યારે અને કોની વચ્ચે લડાયું હતું?",
      "back": "The first battle of Panipat was fought on 20th April 1526 between Babur and Ibrahim Lodi.",
      "back_hi": "पानीपत का पहला युद्ध 20 अप्रैल 1526 को बाबर और इब्राहिम लोदी के बीच लड़ा गया था।",
      "back_gu": "પાણિપતનું પ્રથમ યુદ્ધ 20 એપ્રિલ 1526ના રોજ બાબર અને ઇબ્રાહિમ લોદી વચ્ચે લડાયું હતું."
    },
    {
      "id": "KOBJ_GSEB_C7_SOC_CH3_EX1_2",
      "type": "flashcard",
      "title": "Exercise 1.2",
      "title_hi": "अभ्यास 1.2",
      "title_gu": "સ્વાધ્યાય 1.2",
      "front": "Describe the architecture during the rule of Sher Shah.",
      "front_hi": "शेरशाह के शासनकाल के दौरान वास्तुकला का वर्णन करें।",
      "front_gu": "શેરશાહના શાસનકાળ દરમિયાન સ્થાપત્યનું વર્ણન કરો.",
      "back": "During the rule of Sher Shah, he built a tomb at Sasaram and a mosque at Delhi.",
      "back_hi": "शेरशाह के शासनकाल के दौरान, उसने सासाराम में एक मकबरा और दिल्ली में एक मस्जिद का निर्माण करवाया था।",
      "back_gu": "શેરશાહના શાસનકાળ દરમિયાન, તેણે સાસારામમાં એક મકબરો અને દિલ્હીમાં એક મસ્જિદનું નિર્માણ કરાવ્યું હતું."
    },
    {
      "id": "KOBJ_GSEB_C7_SOC_CH3_EX1_3",
      "type": "flashcard",
      "title": "Exercise 1.3",
      "title_hi": "अभ्यास 1.3",
      "title_gu": "સ્વાધ્યાય 1.3",
      "front": "Name the great musician-singer at the time of Akbar.",
      "front_hi": "अकबर के समय के महान संगीतकार-गायक का नाम बताइए।",
      "front_gu": "અકબરના સમયના મહાન સંગીતકાર-ગાયકનું નામ જણાવો.",
      "back": "Tansen was the great classical musician-singer at the time of Akbar.",
      "back_hi": "अकबर के समय में तानसेन महान शास्त्रीय संगीतकार-गायक थे।",
      "back_gu": "અકબરના સમયમાં તાનસેન મહાન શાસ્ત્રીય સંગીતકાર-ગાયક હતા."
    },
    {
      "id": "KOBJ_GSEB_C7_SOC_CH3_EX1_4",
      "type": "flashcard",
      "title": "Exercise 1.4",
      "title_hi": "अभ्यास 1.4",
      "title_gu": "સ્વાધ્યાય 1.4",
      "front": "Name the painter of Jahangir.",
      "front_hi": "जहाँगीर के चित्रकार का नाम बताइए।",
      "front_gu": "જહાંગીરના ચિત્રકારનું નામ જણાવો.",
      "back": "Mansoor was the world famous painter in the court of Jahangir.",
      "back_hi": "मंसूर जहाँगीर के दरबार में विश्व प्रसिद्ध चित्रकार था।",
      "back_gu": "મન્સૂર જહાંગીરના દરબારમાં વિશ્વ પ્રસિદ્ધ ચિત્રકાર હતો."
    },
    {
      "id": "KOBJ_GSEB_C7_SOC_CH3_EX1_5",
      "type": "flashcard",
      "title": "Exercise 1.5",
      "title_hi": "अभ्यास 1.5",
      "title_gu": "સ્વાધ્યાય 1.5",
      "front": "Where and when was Chhatrapati Shivaji born?",
      "front_hi": "छत्रपति शिवाजी का जन्म कब और कहाँ हुआ था?",
      "front_gu": "છત્રપતિ શિવાજીનો જન્મ ક્યારે અને ક્યાં થયો હતો?",
      "back": "Chhatrapati Shivaji Maharaja was born in 1627 or 1630 A.D in Shivneri (Maharashtra).",
      "back_hi": "छत्रपति शिवाजी महाराज का जन्म 1627 या 1630 ई. में शिवनेरी (महाराष्ट्र) में हुआ था।",
      "back_gu": "છત્રપતિ શિવાજી મહારાજનો જન્મ 1627 અથવા 1630 ઈ.સ.માં શિવનેરી (મહારાષ્ટ્ર) માં થયો હતો."
    },
    {
      "id": "KOBJ_GSEB_C7_SOC_CH3_EX2_1",
      "type": "flashcard",
      "title": "Exercise 2.1",
      "title_hi": "अभ्यास 2.1",
      "title_gu": "સ્વાધ્યાય 2.1",
      "front": "Give the outline of Mughal administration.",
      "front_hi": "मुगल प्रशासन की रूपरेखा दीजिए।",
      "front_gu": "મુઘલ વહીવટીતંત્રની રૂપરેખા આપો.",
      "back": "The Mughal Administration was systematically established by Akbar. The emperor was the supreme commander and judge. A vazir (Diwan-e-Wazir-e-Kul) coordinated between the emperor and administration. Mirbaksh was the head of the army, Mir-e-Saman looked after personal needs of the emperor, and Kazi was the head of the judiciary.",
      "back_hi": "मुगल प्रशासन व्यवस्थित रूप से अकबर द्वारा स्थापित किया गया था। सम्राट सर्वोच्च सेनापति और न्यायाधीश था। एक वज़ीर (दीवान-ए-वज़ीर-ए-कुल) सम्राट और प्रशासन के बीच समन्वय करता था। मीरबख्श सेना का प्रमुख था, मीर-ए-सामान सम्राट की व्यक्तिगत जरूरतों की देखभाल करता था, और काज़ी न्यायपालिका का प्रमुख था।",
      "back_gu": "મુઘલ વહીવટીતંત્રની વ્યવસ્થિત સ્થાપના અકબર દ્વારા કરવામાં આવી હતી. સમ્રાટ સર્વોચ્ચ સેનાપતિ અને ન્યાયાધીશ હતા. એક વઝીર (દીવાન-એ-વઝીર-એ-કુલ) સમ્રાટ અને વહીવટીતંત્ર વચ્ચે સંકલન કરતો હતો. મીરબક્ષ સેનાનો વડો હતો, મીર-એ-સામન સમ્રાટની વ્યક્તિગત જરૂરિયાતોનું ધ્યાન રાખતો હતો અને કાઝી ન્યાયતંત્રનો વડો હતો."
    },
    {
      "id": "KOBJ_GSEB_C7_SOC_CH3_EX2_2",
      "type": "flashcard",
      "title": "Exercise 2.2",
      "title_hi": "अभ्यास 2.2",
      "title_gu": "સ્વાધ્યાય 2.2",
      "front": "Write a note on Mughal architecture.",
      "front_hi": "मुगल वास्तुकला पर एक टिप्पणी लिखिए।",
      "front_gu": "મુઘલ સ્થાપત્ય પર એક નોંધ લખો.",
      "back": "Mughal architecture flourished under various rulers. Babur set up gardens in Agra and Lahore. Shershah built a tomb at Sasaram and a mosque at Delhi. Akbar built the Agra fort, and Fatehpur Sikri including Buland Darwaza. Shah Jahan's period is the golden age of architecture (built Taj Mahal, Red Fort). Aurangzeb built Bibi ka Makbara.",
      "back_hi": "विभिन्न शासकों के अधीन मुगल वास्तुकला फली-फूली। बाबर ने आगरा और लाहौर में उद्यान स्थापित किए। शेरशाह ने सासाराम में एक मकबरा और दिल्ली में एक मस्जिद का निर्माण करवाया। अकबर ने आगरा का किला और फतेहपुर सीकरी (बुलंद दरवाजा सहित) बनवाया। शाहजहाँ का काल वास्तुकला का स्वर्ण युग है (ताज महल, लाल किला बनवाया)। औरंगजेब ने बीवी का मकबरा बनवाया।",
      "back_gu": "વિવિધ શાસકો હેઠળ મુઘલ સ્થાપત્યનો વિકાસ થયો. બાબરે આગ્રા અને લાહોરમાં બગીચાઓ બનાવ્યા. શેરશાહે સાસારામમાં મકબરો અને દિલ્હીમાં મસ્જિદ બનાવી. અકબરે આગ્રાનો કિલ્લો અને ફતેહપુર સીકરી (બુલંદ દરવાજા સહિત) બનાવ્યા. શાહજહાંનો સમય સ્થાપત્યનો સુવર્ણ યુગ છે (તાજમહેલ, લાલ કિલ્લો બનાવ્યા). ઔરંગઝેબે બીબી કા મકબરા બનાવ્યો."
    },
    {
      "id": "KOBJ_GSEB_C7_SOC_CH3_EX2_3",
      "type": "flashcard",
      "title": "Exercise 2.3",
      "title_hi": "अभ्यास 2.3",
      "title_gu": "સ્વાધ્યાય 2.3",
      "front": "Write a note on victories of Chhatrapati Shivaji.",
      "front_hi": "छत्रपति शिवाजी की विजयों पर एक टिप्पणी लिखिए।",
      "front_gu": "છત્રપતિ શિવાજીના વિજયો પર એક નોંધ લખો.",
      "back": "Chhatrapati Shivaji conquered more than 40 forts to expand the Maratha kingdom. He successfully fought against the Mughal emperor Aurangzeb and Adilshah of Bijapur for a long time. He even escaped Aurangzeb's imprisonment, fought back, won, and was coronated in 1674 A.D at Rajgarh.",
      "back_hi": "छत्रपति शिवाजी ने मराठा साम्राज्य के विस्तार के लिए 40 से अधिक किलों पर विजय प्राप्त की। उन्होंने लंबे समय तक मुगल सम्राट औरंगजेब और बीजापुर के आदिलशाह के खिलाफ सफलतापूर्वक लड़ाई लड़ी। वह औरंगजेब की कैद से भी बच निकले, वापस लड़े, जीते और 1674 ई. में राजगढ़ में उनका राज्याभिषेक हुआ।",
      "back_gu": "છત્રપતિ શિવાજીએ મરાઠા સામ્રાજ્યના વિસ્તરણ માટે 40 થી વધુ કિલ્લાઓ જીત્યા. તેમણે મુઘલ સમ્રાટ ઔરંગઝેબ અને બીજાપુરના આદિલશાહ સામે લાંબા સમય સુધી સફળતાપૂર્વક યુદ્ધ કર્યું. તેઓ ઔરંગઝેબની કેદમાંથી પણ છટકી ગયા, પાછા લડ્યા, જીત્યા અને 1674 ઈ.સ.માં રાજગઢમાં તેમનો રાજ્યાભિષેક થયો."
    },
    {
      "id": "KOBJ_GSEB_C7_SOC_CH3_EX2_4",
      "type": "flashcard",
      "title": "Exercise 2.4",
      "title_hi": "अभ्यास 2.4",
      "title_gu": "સ્વાધ્યાય 2.4",
      "front": "Discuss the religious policy of Akbar.",
      "front_hi": "अकबर की धार्मिक नीति पर चर्चा करें।",
      "front_gu": "અકબરની ધાર્મિક નીતિની ચર્ચા કરો.",
      "back": "Akbar adopted a liberal and secular religious policy. He established good social relations with Hindus, abolished pilgrim taxes, and banned forced religious conversions. He established a sect called 'Din-e-Ilahi' which brought together the best elements of all religions.",
      "back_hi": "अकबर ने एक उदार और धर्मनिरपेक्ष धार्मिक नीति अपनाई। उसने हिंदुओं के साथ अच्छे सामाजिक संबंध स्थापित किए, तीर्थयात्रा कर समाप्त कर दिए और जबरन धर्म परिवर्तन पर प्रतिबंध लगा दिया। उसने 'दीन-ए-इलाही' नामक एक संप्रदाय की स्थापना की, जिसमें सभी धर्मों के सर्वोत्तम तत्वों को एक साथ लाया गया था।",
      "back_gu": "અકબરે ઉદાર અને બિનસાંપ્રદાયિક ધાર્મિક નીતિ અપનાવી. તેણે હિંદુઓ સાથે સારા સામાજિક સંબંધો સ્થાપ્યા, યાત્રાવેરો નાબૂદ કર્યો અને બળજબરીથી થતા ધર્માંતરણ પર પ્રતિબંધ મૂક્યો. તેણે 'દીન-એ-ઈલાહી' નામના સંપ્રદાયની સ્થાપના કરી, જેમાં તમામ ધર્મોના શ્રેષ્ઠ તત્વોનો સમાવેશ થતો હતો."
    },
    {
      "id": "KOBJ_GSEB_C7_SOC_CH3_EX2_5",
      "type": "flashcard",
      "title": "Exercise 2.5",
      "title_hi": "अभ्यास 2.5",
      "title_gu": "સ્વાધ્યાય 2.5",
      "front": "Discuss the reforms done by Sher Shah.",
      "front_hi": "शेरशाह द्वारा किए गए सुधारों पर चर्चा करें।",
      "front_gu": "શેરશાહ દ્વારા કરવામાં આવેલા સુધારાઓની ચર્ચા કરો.",
      "back": "Sher Shah Suri was a great reformer. He established peace by controlling bandits, introduced a new postal system, built inns for traders and pilgrims, introduced the currency of the rupee, formed a huge army, and built the famous 'Grand Trunk Road' connecting Bengal to North India.",
      "back_hi": "शेरशाह सूरी एक महान सुधारक था। उसने डाकुओं को नियंत्रित करके शांति स्थापित की, एक नई डाक प्रणाली शुरू की, व्यापारियों और तीर्थयात्रियों के लिए सराय बनवाई, रुपये की मुद्रा शुरू की, एक विशाल सेना बनाई और बंगाल को उत्तर भारत से जोड़ने वाली प्रसिद्ध 'ग्रैंड ट्रंक रोड' का निर्माण किया।",
      "back_gu": "શેરશાહ સૂરી એક મહાન સુધારક હતો. તેણે ડાકુઓને નિયંત્રિત કરીને શાંતિ સ્થાપી, નવી ટપાલ વ્યવસ્થા શરૂ કરી, વેપારીઓ અને યાત્રાળુઓ માટે ધર્મશાળાઓ બનાવી, રૂપિયાના સિક્કા શરૂ કર્યા, વિશાળ સૈન્યની રચના કરી અને બંગાળને ઉત્તર ભારત સાથે જોડતો પ્રખ્યાત 'ગ્રાન્ડ ટ્રંક રોડ' બનાવ્યો."
    },
    {
      "id": "KOBJ_GSEB_C7_SOC_CH3_EX3_1",
      "type": "mcq",
      "title": "Exercise 3.1",
      "title_hi": "अभ्यास 3.1",
      "title_gu": "સ્વાધ્યાય 3.1",
      "question": "II battle of Panipat was fought between ......... and ......... .",
      "question_hi": "पानीपत का दूसरा युद्ध ......... और ......... के बीच लड़ा गया था।",
      "question_gu": "પાણિપતનું બીજું યુદ્ધ ......... અને ......... વચ્ચે લડાયું હતું.",
      "options": [
        "Akbar-Shivaji",
        "Akbar-Hemu",
        "Babur-Ibrahim Lodi",
        "Mughal-Maratha"
      ],
      "options_hi": [
        "अकबर-शिवाजी",
        "अकबर-हेमू",
        "बाबर-इब्राहिम लोदी",
        "मुगल-मराठा"
      ],
      "options_gu": [
        "અકબર-શિવાજી",
        "અકબર-હેમુ",
        "બાબર-ઇબ્રાહિમ લોદી",
        "મુઘલ-મરાઠા"
      ],
      "correct_index": 1,
      "explanation": "The Second battle of Panipat took place between Akbar and Hemu in 1556 A.D.",
      "explanation_hi": "पानीपत का दूसरा युद्ध 1556 ई. में अकबर और हेमू के बीच हुआ था।",
      "explanation_gu": "પાણિપતનું બીજું યુદ્ધ 1556 ઈ.સ.માં અકબર અને હેમુ વચ્ચે થયું હતું."
    },
    {
      "id": "KOBJ_GSEB_C7_SOC_CH3_EX3_2",
      "type": "mcq",
      "title": "Exercise 3.2",
      "title_hi": "अभ्यास 3.2",
      "title_gu": "સ્વાધ્યાય 3.2",
      "question": "Who constructed the Bulund Darwaza ?",
      "question_hi": "बुलंद दरवाजा का निर्माण किसने करवाया था?",
      "question_gu": "બુલંદ દરવાજાનું નિર્માણ કોણે કરાવ્યું હતું?",
      "options": [
        "Akbar",
        "Jahangir",
        "ShahJahan",
        "Aurangzeb"
      ],
      "options_hi": [
        "अकबर",
        "जहाँगीर",
        "शाहजहाँ",
        "औरंगज़ेब"
      ],
      "options_gu": [
        "અકબર",
        "જહાંગીર",
        "શાહજહાં",
        "ઔરંગઝેબ"
      ],
      "correct_index": 0,
      "explanation": "Akbar built the Buland Darwaza at Fatehpur Sikri in memory of his victory over Gujarat.",
      "explanation_hi": "अकबर ने गुजरात पर अपनी विजय की स्मृति में फतेहपुर सीकरी में बुलंद दरवाजा बनवाया था।",
      "explanation_gu": "અકબરે ગુજરાત પરના પોતાના વિજયની યાદમાં ફતેહપુર સીકરી ખાતે બુલંદ દરવાજાનું નિર્માણ કરાવ્યું હતું."
    },
    {
      "id": "KOBJ_GSEB_C7_SOC_CH3_EX3_3",
      "type": "mcq",
      "title": "Exercise 3.3",
      "title_hi": "अभ्यास 3.3",
      "title_gu": "સ્વાધ્યાય 3.3",
      "question": "Red Fort of Delhi was constructed by ......... ;",
      "question_hi": "दिल्ली के लाल किले का निर्माण ......... द्वारा करवाया गया था;",
      "question_gu": "દિલ્હીના લાલ કિલ્લાનું નિર્માણ ......... દ્વારા કરવામાં આવ્યું હતું;",
      "options": [
        "Babur",
        "Akbar",
        "Humayun",
        "ShahJahan"
      ],
      "options_hi": [
        "बाबर",
        "अकबर",
        "हुमायूँ",
        "शाहजहाँ"
      ],
      "options_gu": [
        "બાબર",
        "અકબર",
        "હુમાયુ",
        "શાહજહાં"
      ],
      "correct_index": 3,
      "explanation": "Shah Jahan built the famous Red Fort in Delhi during his reign.",
      "explanation_hi": "शाहजहाँ ने अपने शासनकाल के दौरान दिल्ली में प्रसिद्ध लाल किले का निर्माण करवाया था।",
      "explanation_gu": "શાહજહાંએ પોતાના શાસનકાળ દરમિયાન દિલ્હીમાં પ્રખ્યાત લાલ કિલ્લાનું નિર્માણ કરાવ્યું હતું."
    },
    {
      "id": "KOBJ_GSEB_C7_SOC_CH3_EX3_4",
      "type": "mcq",
      "title": "Exercise 3.4",
      "title_hi": "अभ्यास 3.4",
      "title_gu": "સ્વાધ્યાય 3.4",
      "question": "Akbar was born at ......... ,",
      "question_hi": "अकबर का जन्म ......... में हुआ था,",
      "question_gu": "અકબરનો જન્મ ......... ખાતે થયો હતો,",
      "options": [
        "Amarkot",
        "Iran",
        "Delhi",
        "Jaipur"
      ],
      "options_hi": [
        "अमरकोट",
        "ईरान",
        "दिल्ली",
        "जयपुर"
      ],
      "options_gu": [
        "અમરકોટ",
        "ઈરાન",
        "દિલ્હી",
        "જયપુર"
      ],
      "correct_index": 0,
      "explanation": "Akbar was born in 1542 A.D in the home of a Hindu Rajput ruler in Amarkot.",
      "explanation_hi": "अकबर का जन्म 1542 ई. में अमरकोट में एक हिंदू राजपूत शासक के घर हुआ था।",
      "explanation_gu": "અકબરનો જન્મ 1542 ઈ.સ.માં અમરકોટમાં એક હિંદુ રાજપૂત શાસકના ઘરે થયો હતો."
    }
]

with open('/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class7_social_science_ch3.json', 'r+', encoding='utf-8') as f:
    data = json.load(f)
    data['blocks'].extend(new_blocks)
    f.seek(0)
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.truncate()

print("Appended blocks successfully.")
