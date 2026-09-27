import json

file_path = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class7_social_science_ch1.json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

new_blocks = [
    {
        "type": "flashcard",
        "front": "Where did the rulers of Chauhan dynasty initially rule?",
        "front_hi": "चौहान वंश के शासकों ने प्रारंभ में कहाँ शासन किया?",
        "front_gu": "ચૌહાણ વંશના શાસકોએ શરૂઆતમાં ક્યાં શાસન કર્યું?",
        "back": "In Shakambhari, a place located to the North of Ajmer.",
        "back_hi": "शाकम्भरी में, जो अजमेर के उत्तर में स्थित एक स्थान है।",
        "back_gu": "શાકંભરીમાં, જે અજમેરની ઉત્તરે આવેલું સ્થળ છે.",
        "hint": "It is near Sambhar lake.",
        "hint_hi": "यह सांभर झील के पास है।",
        "hint_gu": "તે સાંભર તળાવ પાસે છે.",
        "id": "KOBJ_CLAS7_SSCI_CH1_FLASH_001"
    },
    {
        "type": "flashcard",
        "front": "Who was the last ruler of Vaghela dynasty?",
        "front_hi": "वाघेला वंश का अंतिम शासक कौन था?",
        "front_gu": "વાઘેલા વંશનો છેલ્લો શાસક કોણ હતો?",
        "back": "Karandev Vaghela.",
        "back_hi": "करणदेव वाघेला।",
        "back_gu": "કરણદેવ વાઘેલા.",
        "hint": "Delhi Sultanate was established after him.",
        "hint_hi": "उनके बाद दिल्ली सल्तनत की स्थापना हुई।",
        "hint_gu": "તેમના પછી દિલ્હી સલ્તનતની સ્થાપના થઈ.",
        "id": "KOBJ_CLAS7_SSCI_CH1_FLASH_002"
    },
    {
        "type": "flashcard",
        "front": "Write a short note on characteristics of the Rajputs.",
        "front_hi": "राजपूतों की विशेषताओं पर एक संक्षिप्त टिप्पणी लिखें।",
        "front_gu": "રાજપૂતોની લાક્ષણિકતાઓ પર ટૂંકી નોંધ લખો.",
        "back": "Rajputs were brave, kept their promises, and would rather die than show their back to the enemy. They protected Gau Brahmins and the surrendered, never practicing unrighteousness in battle.",
        "back_hi": "राजपूत बहादुर थे, अपना वादा निभाते थे, और दुश्मन को पीठ दिखाने के बजाय मरना पसंद करते थे। वे गौ ब्राह्मणों और आत्मसमर्पण करने वालों की रक्षा करते थे, युद्ध में कभी भी अधर्म का अभ्यास नहीं करते थे।",
        "back_gu": "રાજપૂતો બહાદુર હતા, તેમના વચનો પાળતા હતા, અને દુશ્મનને પીઠ બતાવવા કરતાં મરવાનું પસંદ કરતા હતા. તેઓ ગૌ બ્રાહ્મણો અને શરણાગતિ સ્વીકારનારાઓનું રક્ષણ કરતા હતા, યુદ્ધમાં ક્યારેય અધર્મનું આચરણ કરતા ન હતા.",
        "hint": "Focus on bravery, promises, and protection.",
        "hint_hi": "बहादुरी, वादों और सुरक्षा पर ध्यान दें।",
        "hint_gu": "બહાદુરી, વચનો અને રક્ષણ પર ધ્યાન કેન્દ્રિત કરો.",
        "id": "KOBJ_CLAS7_SSCI_CH1_FLASH_003"
    },
    {
        "type": "flashcard",
        "front": "Write a short note on trade and commerce during the Rajput era.",
        "front_hi": "राजपूत काल के दौरान व्यापार और वाणिज्य पर एक संक्षिप्त टिप्पणी लिखें।",
        "front_gu": "રાજપૂત યુગ દરમિયાન વેપાર અને વાણિજ્ય પર ટૂંકી નોંધ લખો.",
        "back": "There was a separate department for commerce. Taxes were collected from foreign trade, land (Bhag - 1/6th), ports, and irrigation. Stambhtirth (Khambhat) and Bhrigukutch (Bharuch) were famous ports.",
        "back_hi": "वाणिज्य के लिए एक अलग विभाग था। विदेशी व्यापार, भूमि (भाग - 1/6), बंदरगाहों और सिंचाई से कर एकत्र किया जाता था। स्तंभतीर्थ (खंभात) और भृगुकच्छ (भरूच) प्रसिद्ध बंदरगाह थे।",
        "back_gu": "વાણિજ્ય માટે એક અલગ વિભાગ હતો. વિદેશી વેપાર, જમીન (ભાગ - 1/6), બંદરો અને સિંચાઈમાંથી કર વસૂલવામાં આવતો હતો. સ્તંભતીર્થ (ખંભાત) અને ભૃગુકચ્છ (ભરૂચ) પ્રખ્યાત બંદરો હતા.",
        "hint": "Mention the tax 'Bhag' and major ports.",
        "hint_hi": "'भाग' कर और प्रमुख बंदरगाहों का उल्लेख करें।",
        "hint_gu": "'ભાગ' કર અને પ્રમુખ બંદરોનો ઉલ્લેખ કરો.",
        "id": "KOBJ_CLAS7_SSCI_CH1_FLASH_004"
    },
    {
        "type": "flashcard",
        "front": "Name any three major dynasties of North India.",
        "front_hi": "उत्तर भारत के किन्हीं तीन प्रमुख राजवंशों के नाम बताइए।",
        "front_gu": "ઉત્તર ભારતના કોઈપણ ત્રણ પ્રમુખ રાજવંશોના નામ આપો.",
        "back": "Gurjar Pratihaar, Gadhwal, Chandel, Parmar, Chauhan, Solanki. (Any three)",
        "back_hi": "गुर्जर प्रतिहार, गढ़वाल, चंदेल, परमार, चौहान, सोलंकी। (कोई भी तीन)",
        "back_gu": "ગુર્જર પ્રતિહાર, ગઢવાલ, ચંદેલ, પરમાર, ચૌહાણ, સોલંકી. (કોઈપણ ત્રણ)",
        "hint": "Think of Kannauj, Bundelkhand, Malwa.",
        "hint_hi": "कन्नौज, बुंदेलखंड, मालवा के बारे में सोचें।",
        "hint_gu": "કન્નૌજ, બુંદેલખંડ, માલવા વિશે વિચારો.",
        "id": "KOBJ_CLAS7_SSCI_CH1_FLASH_005"
    },
    {
        "type": "flashcard",
        "front": "Name any three major dynasties of South India.",
        "front_hi": "दक्षिण भारत के किन्हीं तीन प्रमुख राजवंशों के नाम बताइए।",
        "front_gu": "દક્ષિણ ભારતના કોઈપણ ત્રણ પ્રમુખ રાજવંશોના નામ આપો.",
        "back": "Chalukya, Rashtrakuta, Pallav, Chola, Pandya, Chera. (Any three)",
        "back_hi": "चालुक्य, राष्ट्रकूट, पल्लव, चोल, पांड्य, चेर। (कोई भी तीन)",
        "back_gu": "ચાલુક્ય, રાષ્ટ્રકૂટ, પલ્લવ, ચોલ, પાંડ્ય, ચેર. (કોઈપણ ત્રણ)",
        "hint": "Think of kingdoms south of the Narmada river.",
        "hint_hi": "नर्मदा नदी के दक्षिण के राज्यों के बारे में सोचें।",
        "hint_gu": "નર્મદા નદીની દક્ષિણે આવેલા રાજ્યો વિશે વિચારો.",
        "id": "KOBJ_CLAS7_SSCI_CH1_FLASH_006"
    },
    {
        "type": "flashcard",
        "front": "Who built 'Rani ki Vav'?",
        "front_hi": "'रानी की वाव' किसने बनवाई?",
        "front_gu": "'રાણી ની વાવ' કોણે બનાવી?",
        "back": "Rani Udaymati, the wife of Bhimdev-I Solanki.",
        "back_hi": "भीमदेव-प्रथम सोलंकी की पत्नी रानी उदयमती ने।",
        "back_gu": "ભીમદેવ-પ્રથમ સોલંકીની પત્ની રાણી ઉદયમતીએ.",
        "hint": "She built it in Patan.",
        "hint_hi": "उसने इसे पाटन में बनवाया था।",
        "hint_gu": "તેણીએ તે પાટણમાં બનાવી હતી.",
        "id": "KOBJ_CLAS7_SSCI_CH1_FLASH_007"
    },
    {
        "type": "flashcard",
        "front": "Who founded Anhilwad Patan?",
        "front_hi": "अन्हिलवाड़ पाटन की स्थापना किसने की?",
        "front_gu": "અણહિલવાડ પાટણની સ્થાપના કોણે કરી?",
        "back": "Vanraj Chavda founded Anhilwad Patan in 756 A.D.",
        "back_hi": "वनराज चावड़ा ने 756 ई. में अन्हिलवाड़ पाटन की स्थापना की।",
        "back_gu": "વનરાજ ચાવડાએ 756 એડીમાં અણહિલવાડ પાટણની સ્થાપના કરી.",
        "hint": "He named it after his childhood friend Anhil Bharwad.",
        "hint_hi": "उन्होंने इसका नाम अपने बचपन के दोस्त अन्हिल भरवाड़ के नाम पर रखा।",
        "hint_gu": "તેણે તેનું નામ તેના બાળપણના મિત્ર અણહિલ ભરવાડના નામ પરથી રાખ્યું.",
        "id": "KOBJ_CLAS7_SSCI_CH1_FLASH_008"
    },
    {
        "type": "flashcard",
        "front": "Who was the first Sultan of Gujarat?",
        "front_hi": "गुजरात का पहला सुल्तान कौन था?",
        "front_gu": "ગુજરાતનો પ્રથમ સુલતાન કોણ હતો?",
        "back": "Muzaffar Shah (originally Zafar Khan) was the first Sultan.",
        "back_hi": "मुजफ्फर शाह (मूल रूप से जफर खान) पहले सुल्तान थे।",
        "back_gu": "મુઝફ્ફર શાહ (મૂળ નામ ઝફર ખાન) પ્રથમ સુલતાન હતા.",
        "hint": "He changed his name in 1407 A.D.",
        "hint_hi": "उन्होंने 1407 ई. में अपना नाम बदल लिया था।",
        "hint_gu": "તેણે 1407 એડીમાં પોતાનું નામ બદલ્યું.",
        "id": "KOBJ_CLAS7_SSCI_CH1_FLASH_009"
    },
    {
        "type": "flashcard",
        "front": "Which public welfare works were done by Rajmata Meenaldevi?",
        "front_hi": "राजमाता मीनलदेवी ने कौन से लोक कल्याणकारी कार्य किए?",
        "front_gu": "રાજમાતા મીનલદેવીએ કયા લોકકલ્યાણ કાર્યો કર્યા?",
        "back": "She stopped the pilgrimage tax at Somnath and constructed Malav lake in Dholka and Munsar lake in Viramgam.",
        "back_hi": "उन्होंने सोमनाथ में तीर्थयात्रा कर बंद कर दिया और ढोलका में मालव झील तथा वीरमगाम में मुनसर झील का निर्माण कराया।",
        "back_gu": "તેણે સોમનાથમાં યાત્રા વેરો બંધ કરાવ્યો અને ધોળકામાં માલવ તળાવ અને વિરમગામમાં મુનસર તળાવનું નિર્માણ કરાવ્યું.",
        "hint": "She did this for justice to the people.",
        "hint_hi": "उन्होंने यह लोगों को न्याय दिलाने के लिए किया।",
        "hint_gu": "તેણે આ લોકો માટે ન્યાય ખાતર કર્યું.",
        "id": "KOBJ_CLAS7_SSCI_CH1_FLASH_010"
    },
    {
        "type": "mcq",
        "question": "After the death of which king in North India, small states became independent?",
        "question_hi": "उत्तर भारत में किस राजा की मृत्यु के बाद छोटे राज्य स्वतंत्र हो गए?",
        "question_gu": "ઉત્તર ભારતમાં કયા રાજાના મૃત્યુ પછી નાના રાજ્યો સ્વતંત્ર થયા?",
        "options": [
            "Harshvardhan",
            "Pulkeshi-II",
            "Mihirbhoj",
            "Ashok"
        ],
        "options_hi": [
            "हर्षवर्धन",
            "पुलकेशी-द्वितीय",
            "मिहिरभोज",
            "अशोक"
        ],
        "options_gu": [
            "હર્ષવર્ધન",
            "પુલકેશી-બીજા",
            "મિહિરભોજ",
            "અશોક"
        ],
        "correct_index": 0,
        "explanation": "After the death of Harshvardhan, his vast empire was divided into small independent states.",
        "explanation_hi": "हर्षवर्धन की मृत्यु के बाद, उनका विशाल साम्राज्य छोटे स्वतंत्र राज्यों में विभाजित हो गया।",
        "explanation_gu": "હર્ષવર્ધનના મૃત્યુ પછી, તેમનું વિશાળ સામ્રાજ્ય નાના સ્વતંત્ર રાજ્યોમાં વહેંચાયેલું હતું.",
        "id": "KOBJ_CLAS7_SSCI_CH1_MCQ_009"
    },
    {
        "type": "mcq",
        "question": "Bundelkhand was known by which name later on?",
        "question_hi": "बुंदेलखंड को बाद में किस नाम से जाना गया?",
        "question_gu": "બુંદેલખંડને પાછળથી કયા નામથી ઓળખવામાં આવતું હતું?",
        "options": [
            "Jejakabhukti",
            "Ujjaini",
            "Pratihar",
            "Chalukya"
        ],
        "options_hi": [
            "जेजाकभुक्ति",
            "उज्जयिनी",
            "प्रतिहार",
            "चालुक्य"
        ],
        "options_gu": [
            "જેજાકભુક્તિ",
            "ઉજ્જૈની",
            "પ્રતિહાર",
            "ચાલુક્ય"
        ],
        "correct_index": 0,
        "explanation": "The state of Chandels of Bundelkhand region was known as 'Jejakabhukti'.",
        "explanation_hi": "बुंदेलखंड क्षेत्र के चंदेलों के राज्य को 'जेजाकभुक्ति' के नाम से जाना जाता था।",
        "explanation_gu": "બુંદેલખંડ પ્રદેશના ચંદેલોનું રાજ્ય 'જેજાકભુક્તિ' તરીકે ઓળખાતું હતું.",
        "id": "KOBJ_CLAS7_SSCI_CH1_MCQ_010"
    },
    {
        "type": "mcq",
        "question": "Which of the following rulers is not among the rulers of the Parmar dynasty of Malwa?",
        "question_hi": "निम्नलिखित में से कौन सा शासक मालवा के परमार वंश के शासकों में से नहीं है?",
        "question_gu": "નીચેનામાંથી કયો શાસક માલવાના પરમાર વંશના શાસકોમાંનો નથી?",
        "options": [
            "Kumarpal",
            "Bhoj",
            "Siyuk",
            "Munj"
        ],
        "options_hi": [
            "कुमारपाल",
            "भोज",
            "सीयुक",
            "मुंज"
        ],
        "options_gu": [
            "કુમારપાળ",
            "ભોજ",
            "સીયુક",
            "મુંજ"
        ],
        "correct_index": 0,
        "explanation": "Kumarpal was a ruler of the Solanki dynasty of Gujarat.",
        "explanation_hi": "कुमारपाल गुजरात के सोलंकी वंश के शासक थे।",
        "explanation_gu": "કુમારપાળ ગુજરાતના સોલંકી વંશના શાસક હતા.",
        "id": "KOBJ_CLAS7_SSCI_CH1_MCQ_011"
    },
    {
        "type": "mcq",
        "question": "Which dynasty ruled Bengal in the 8th century?",
        "question_hi": "8वीं शताब्दी में बंगाल पर किस वंश ने शासन किया?",
        "question_gu": "8મી સદીમાં બંગાળ પર કયા વંશે શાસન કર્યું?",
        "options": [
            "Chandel dynasty",
            "Parmar dynasty",
            "Pala dynasty",
            "Pratihars"
        ],
        "options_hi": [
            "चंदेल वंश",
            "परमार वंश",
            "पाल वंश",
            "प्रतिहार"
        ],
        "options_gu": [
            "ચંદેલ વંશ",
            "પરમાર વંશ",
            "પાલ વંશ",
            "પ્રતિહાર"
        ],
        "correct_index": 2,
        "explanation": "Bengal was ruled by the Pala dynasty in the middle of the eighth century.",
        "explanation_hi": "आठवीं शताब्दी के मध्य में बंगाल पर पाल वंश का शासन था।",
        "explanation_gu": "આઠમી સદીના મધ્યમાં બંગાળ પર પાલ વંશનું શાસન હતું.",
        "id": "KOBJ_CLAS7_SSCI_CH1_MCQ_012"
    },
    {
        "type": "mcq",
        "question": "'Rani ni Vav' was constructed during the reign of which dynasty?",
        "question_hi": "'रानी नी वाव' का निर्माण किस राजवंश के शासनकाल के दौरान किया गया था?",
        "question_gu": "'રાણી ની વાવ' કયા વંશના શાસનકાળ દરમિયાન બનાવવામાં આવી હતી?",
        "options": [
            "Chavda dynasty",
            "Solanki dynasty",
            "Vaghela dynasty",
            "Maitrak dynasty"
        ],
        "options_hi": [
            "चावड़ा वंश",
            "सोलंकी वंश",
            "वाघेला वंश",
            "मैत्रक वंश"
        ],
        "options_gu": [
            "ચાવડા વંશ",
            "સોલંકી વંશ",
            "વાઘેલા વંશ",
            "મૈત્રક વંશ"
        ],
        "correct_index": 1,
        "explanation": "It was built by Queen Udaymati, wife of Bhimdev-I of the Solanki dynasty.",
        "explanation_hi": "इसका निर्माण सोलंकी वंश के भीमदेव-प्रथम की पत्नी रानी उदयमती ने करवाया था।",
        "explanation_gu": "તે સોલંકી વંશના ભીમદેવ-પ્રથમની પત્ની રાણી ઉદયમતી દ્વારા બનાવવામાં આવી હતી.",
        "id": "KOBJ_CLAS7_SSCI_CH1_MCQ_013"
    },
    {
        "type": "mcq",
        "question": "Which ruler belongs to Sen dynasty?",
        "question_hi": "कौन सा शासक सेन वंश से संबंधित है?",
        "question_gu": "કયો શાસક સેન વંશનો છે?",
        "options": [
            "Gopal",
            "Govind-III",
            "Vijaysen-I",
            "Kumarpal"
        ],
        "options_hi": [
            "गोपाल",
            "गोविंद-तृतीय",
            "विजयसेन-प्रथम",
            "कुमारपाल"
        ],
        "options_gu": [
            "ગોપાલ",
            "ગોવિંદ-ત્રીજા",
            "વિજયસેન-પ્રથમ",
            "કુમારપાળ"
        ],
        "correct_index": 2,
        "explanation": "Vijaysen-I was the first eminent king of the Sen dynasty.",
        "explanation_hi": "विजयसेन-प्रथम सेन वंश के पहले प्रख्यात राजा थे।",
        "explanation_gu": "વિજયસેન-પ્રથમ સેન વંશના પ્રથમ પ્રખ્યાત રાજા હતા.",
        "id": "KOBJ_CLAS7_SSCI_CH1_MCQ_014"
    },
    {
        "type": "mcq",
        "question": "Which ruler belongs to Solanki dynasty?",
        "question_hi": "कौन सा शासक सोलंकी वंश से संबंधित है?",
        "question_gu": "કયો શાસક સોલંકી વંશનો છે?",
        "options": [
            "Narsinhverman-II",
            "Govind-III",
            "Gopal",
            "Kumarpal"
        ],
        "options_hi": [
            "नरसिंहवर्मन-द्वितीय",
            "गोविंद-तृतीय",
            "गोपाल",
            "कुमारपाल"
        ],
        "options_gu": [
            "નરસિંહવર્મન-બીજા",
            "ગોવિંદ-ત્રીજા",
            "ગોપાલ",
            "કુમારપાળ"
        ],
        "correct_index": 3,
        "explanation": "Kumarpal was a prominent ruler of the Solanki dynasty.",
        "explanation_hi": "कुमारपाल सोलंकी वंश के एक प्रमुख शासक थे।",
        "explanation_gu": "કુમારપાળ સોલંકી વંશના પ્રમુખ શાસક હતા.",
        "id": "KOBJ_CLAS7_SSCI_CH1_MCQ_015"
    },
    {
        "type": "mcq",
        "question": "Which ruler belongs to Pala dynasty?",
        "question_hi": "कौन सा शासक पाल वंश से संबंधित है?",
        "question_gu": "કયો શાસક પાલ વંશનો છે?",
        "options": [
            "Kumarpal",
            "Gopal",
            "Vijaysen-I",
            "Govind-III"
        ],
        "options_hi": [
            "कुमारपाल",
            "गोपाल",
            "विजयसेन-प्रथम",
            "गोविंद-तृतीय"
        ],
        "options_gu": [
            "કુમારપાળ",
            "ગોપાલ",
            "વિજયસેન-પ્રથમ",
            "ગોવિંદ-ત્રીજા"
        ],
        "correct_index": 1,
        "explanation": "The Pala dynasty was founded by a king named Gopal.",
        "explanation_hi": "पाल वंश की स्थापना गोपाल नामक राजा ने की थी।",
        "explanation_gu": "પાલ વંશની સ્થાપના ગોપાલ નામના રાજા દ્વારા કરવામાં આવી હતી.",
        "id": "KOBJ_CLAS7_SSCI_CH1_MCQ_016"
    },
    {
        "type": "mcq",
        "question": "Which ruler belongs to Rashtrakuta dynasty?",
        "question_hi": "कौन सा शासक राष्ट्रकूट वंश से संबंधित है?",
        "question_gu": "કયો શાસક રાષ્ટ્રકૂટ વંશનો છે?",
        "options": [
            "Vijaysen-I",
            "Gopal",
            "Kumarpal",
            "Govind-III"
        ],
        "options_hi": [
            "विजयसेन-प्रथम",
            "गोपाल",
            "कुमारपाल",
            "गोविंद-तृतीय"
        ],
        "options_gu": [
            "વિજયસેન-પ્રથમ",
            "ગોપાલ",
            "કુમારપાળ",
            "ગોવિંદ-ત્રીજા"
        ],
        "correct_index": 3,
        "explanation": "Govind-III was the most powerful ruler of the Rashtrakuta dynasty.",
        "explanation_hi": "गोविंद-तृतीय राष्ट्रकूट वंश के सबसे शक्तिशाली शासक थे।",
        "explanation_gu": "ગોવિંદ-ત્રીજા રાષ્ટ્રકૂટ વંશના સૌથી શક્તિશાળી શાસક હતા.",
        "id": "KOBJ_CLAS7_SSCI_CH1_MCQ_017"
    },
    {
        "type": "mcq",
        "question": "Which ruler belongs to Pallava dynasty?",
        "question_hi": "कौन सा शासक पल्लव वंश से संबंधित है?",
        "question_gu": "કયો શાસક પલ્લવ વંશનો છે?",
        "options": [
            "Gopal",
            "Narsinhverman-II",
            "Govind-III",
            "Kumarpal"
        ],
        "options_hi": [
            "गोपाल",
            "नरसिंहवर्मन-द्वितीय",
            "गोविंद-तृतीय",
            "कुमारपाल"
        ],
        "options_gu": [
            "ગોપાલ",
            "નરસિંહવર્મન-બીજા",
            "ગોવિંદ-ત્રીજા",
            "કુમારપાળ"
        ],
        "correct_index": 1,
        "explanation": "Narsinhverman-II was an important ruler of the Pallava dynasty.",
        "explanation_hi": "नरसिंहवर्मन-द्वितीय पल्लव वंश के एक महत्वपूर्ण शासक थे।",
        "explanation_gu": "નરસિંહવર્મન-બીજા પલ્લવ વંશના મહત્વપૂર્ણ શાસક હતા.",
        "id": "KOBJ_CLAS7_SSCI_CH1_MCQ_018"
    }
]

data['blocks'].extend(new_blocks)

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Added successfully!")
