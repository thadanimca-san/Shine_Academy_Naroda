import json

blocks = [
    {
        "id": "KOBJ_NCERT_C10_SCI_CH11_001",
        "type": "hook",
        "title": "The Invisible River of Power",
        "title_hi": "शक्ति की अदृश्य नदी",
        "title_gu": "શક્તિની અદૃશ્ય નદી",
        "body": "Imagine a world without electricity. No smartphones, no internet, no lights at night, no refrigerators. Electricity is like an invisible river of energy that flows through solid metal wires to power our entire modern civilization. But what exactly is flowing inside those solid wires?",
        "body_hi": "बिजली के बिना दुनिया की कल्पना करें। कोई स्मार्टफोन नहीं, कोई इंटरनेट नहीं, रात में कोई रोशनी नहीं, कोई फ्रिज नहीं। बिजली ऊर्जा की एक अदृश्य नदी की तरह है जो हमारी पूरी आधुनिक सभ्यता को शक्ति प्रदान करने के लिए ठोस धातु के तारों से होकर बहती है। लेकिन उन ठोस तारों के अंदर वास्तव में क्या बह रहा है?",
        "body_gu": "વીજળી વિનાની દુનિયાની કલ્પના કરો. કોઈ સ્માર્ટફોન નહીં, કોઈ ઈન્ટરનેટ નહીં, રાત્રે કોઈ લાઈટ નહીં, કોઈ રેફ્રિજરેટર નહીં. વીજળી એ ઉર્જાની એક અદૃશ્ય નદી જેવી છે જે આપણી આખી આધુનિક સભ્યતાને શક્તિ આપવા માટે નક્કર ધાતુના વાયરોમાંથી વહે છે. પરંતુ તે નક્કર વાયરોની અંદર ખરેખર શું વહી રહ્યું છે?"
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH11_002",
        "type": "theory",
        "title": "Electric Current and Potential Difference",
        "title_hi": "विद्युत धारा और विभवांतर",
        "title_gu": "વિદ્યુતપ્રવાહ અને વિદ્યુતસ્થિતિમાનનો તફાવત",
        "body": "1. Electric Current (I): It is the rate of flow of electric charges (electrons). I = Q / t. The SI unit is Ampere (A). Current is measured by an Ammeter connected in series.\n2. Potential Difference (V): Water only flows in a pipe if there is a pressure difference. Similarly, electrons only flow if there is an electric pressure difference, called Potential Difference (Voltage). V = Work (W) / Charge (Q). The SI unit is Volt (V). It is measured by a Voltmeter connected in parallel.",
        "body_hi": "1. विद्युत धारा (I): यह विद्युत आवेशों (इलेक्ट्रॉनों) के प्रवाह की दर है। I = Q / t। SI इकाई एम्पीयर (A) है। धारा को श्रेणीक्रम (series) में जुड़े एमीटर द्वारा मापा जाता है।\n2. विभवांतर (V): पानी पाइप में तभी बहता है जब दबाव में अंतर हो। इसी तरह, इलेक्ट्रॉन तभी प्रवाहित होते हैं जब विद्युत दबाव में अंतर होता है, जिसे विभवांतर (वोल्टेज) कहा जाता है। V = कार्य (W) / आवेश (Q)। SI इकाई वोल्ट (V) है। इसे समानांतर (parallel) में जुड़े वोल्टमीटर द्वारा मापा जाता है।",
        "body_gu": "1. વિદ્યુતપ્રવાહ (I): તે વિદ્યુતભારો (ઇલેક્ટ્રોન) ના વહનનો દર છે. I = Q / t. તેનો SI એકમ એમ્પીયર (A) છે. પ્રવાહને શ્રેણીમાં જોડેલા એમીટર દ્વારા માપવામાં આવે છે.\n2. વિદ્યુતસ્થિતિમાનનો તફાવત (V): જો દબાણનો તફાવત હોય તો જ પાઇપમાં પાણી વહે છે. તેવી જ રીતે, ઇલેક્ટ્રોન ત્યારે જ વહે છે જ્યારે વિદ્યુત દબાણનો તફાવત હોય, જેને વિદ્યુતસ્થિતિમાનનો તફાવત (વોલ્ટેજ) કહે છે. V = કાર્ય (W) / વિદ્યુતભાર (Q). તેનો SI એકમ વોલ્ટ (V) છે. તેને સમાંતર જોડેલા વોલ્ટમીટર દ્વારા માપવામાં આવે છે."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH11_003",
        "type": "theory",
        "title": "Ohm's Law and Resistance",
        "title_hi": "ओम का नियम और प्रतिरोध",
        "title_gu": "ઓહ્મનો નિયમ અને અવરોધ",
        "body": "Ohm's Law states that at a constant temperature, the current flowing through a conductor is directly proportional to the potential difference across its ends: V = IR.\nResistance (R) is the property of a conductor to resist the flow of charges. Its SI unit is Ohm (Ω).\nFactors affecting Resistance:\n1. Length (l): R is directly proportional to l.\n2. Area of cross-section (A): R is inversely proportional to A (Thicker wires have less resistance).\n3. Material: Depends on Resistivity (ρ).\nFormula: R = ρ(l/A).",
        "body_hi": "ओम का नियम कहता है कि निरंतर तापमान पर, एक चालक के माध्यम से बहने वाली धारा उसके सिरों के बीच विभवांतर के सीधे आनुपातिक होती है: V = IR।\nप्रतिरोध (R) एक चालक का वह गुण है जो आवेशों के प्रवाह का विरोध करता है। इसकी SI इकाई ओम (Ω) है।\nप्रतिरोध को प्रभावित करने वाले कारक:\n1. लंबाई (l): R, l के सीधे आनुपातिक है।\n2. अनुप्रस्थ काट का क्षेत्रफल (A): R, A के व्युत्क्रमानुपाती है (मोटे तारों में कम प्रतिरोध होता है)।\n3. सामग्री: प्रतिरोधकता (ρ) पर निर्भर करता है।\nसूत्र: R = ρ(l/A)।",
        "body_gu": "ઓહ્મનો નિયમ જણાવે છે કે અચળ તાપમાને, વાહકમાંથી પસાર થતો વિદ્યુતપ્રવાહ તેના છેડા વચ્ચેના વિદ્યુતસ્થિતિમાનના તફાવતના સમપ્રમાણમાં હોય છે: V = IR.\nઅવરોધ (R) એ વાહકનો એવો ગુણધર્મ છે જે વિદ્યુતભારોના વહનનો વિરોધ કરે છે. તેનો SI એકમ ઓહ્મ (Ω) છે.\nઅવરોધ પર અસર કરતા પરિબળો:\n1. લંબાઈ (l): R એ l ના સમપ્રમાણમાં છે.\n2. આડછેદનું ક્ષેત્રફળ (A): R એ A ના વ્યસ્ત પ્રમાણમાં છે (જાડા વાયરોમાં ઓછો અવરોધ હોય છે).\n3. દ્રવ્યની જાત: અવરોધકતા (ρ) પર આધાર રાખે છે.\nસૂત્ર: R = ρ(l/A)."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH11_004",
        "type": "socratic_question",
        "title": "Connecting Resistors",
        "title_hi": "प्रतिरोधकों को जोड़ना",
        "title_gu": "અવરોધોનું જોડાણ",
        "question": "If you connect three bulbs in a line one after another (series) and one bulb fuses, what will happen to the other two bulbs?",
        "question_hi": "यदि आप एक के बाद एक लाइन में (श्रेणीक्रम में) तीन बल्ब जोड़ते हैं और एक बल्ब फ्यूज हो जाता है, तो अन्य दो बल्बों का क्या होगा?",
        "question_gu": "જો તમે એક પછી એક લાઈનમાં (શ્રેણીમાં) ત્રણ બલ્બ જોડો અને એક બલ્બ ફ્યુઝ થઈ જાય, તો અન્ય બે બલ્બનું શું થશે?",
        "options": [
            "They will glow brighter.",
            "They will continue to glow normally.",
            "They will stop glowing because the circuit is broken.",
            "Only one of them will stop glowing."
        ],
        "options_hi": [
            "वे अधिक चमकेंगे।",
            "वे सामान्य रूप से चमकते रहेंगे।",
            "वे चमकना बंद कर देंगे क्योंकि सर्किट टूट गया है।",
            "उनमें से केवल एक ही चमकना बंद करेगा।"
        ],
        "options_gu": [
            "તેઓ વધુ તેજસ્વી રીતે પ્રકાશશે.",
            "તેઓ સામાન્ય રીતે પ્રકાશતા રહેશે.",
            "તેઓ પ્રકાશવાનું બંધ કરશે કારણ કે પરિપથ તૂટી ગયો છે.",
            "તેમાંથી માત્ર એક જ પ્રકાશવાનું બંધ કરશે."
        ],
        "correct_index": 2,
        "explanation": "In a Series circuit, there is only one path for the current to flow. If one component fails, the circuit is broken and current stops entirely. This is why homes are wired in Parallel circuits, where each appliance has its own separate path.",
        "explanation_hi": "श्रेणीक्रम (Series) सर्किट में, धारा प्रवाहित होने के लिए केवल एक ही रास्ता होता है। यदि कोई एक घटक विफल हो जाता है, तो सर्किट टूट जाता है और धारा पूरी तरह से रुक जाती है। यही कारण है कि घरों में समानांतर (Parallel) सर्किट में वायरिंग की जाती है, जहां प्रत्येक उपकरण का अपना अलग रास्ता होता है।",
        "explanation_gu": "શ્રેણી (Series) પરિપથમાં, પ્રવાહ વહેવા માટે માત્ર એક જ રસ્તો હોય છે. જો કોઈ એક ઘટક બગડે, તો પરિપથ તૂટી જાય છે અને પ્રવાહ સંપૂર્ણપણે અટકી જાય છે. આ જ કારણ છે કે ઘરોમાં સમાંતર (Parallel) પરિપથમાં વાયરિંગ કરવામાં આવે છે, જ્યાં દરેક ઉપકરણનો પોતાનો અલગ રસ્તો હોય છે."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH11_005",
        "type": "theory",
        "title": "Heating Effect and Electric Power",
        "title_hi": "तापीय प्रभाव और विद्युत शक्ति",
        "title_gu": "તાપીય અસર અને વિદ્યુત પાવર",
        "body": "When current flows through a high resistance wire (like Nichrome in a heater), it becomes very hot. This is Joule's Law of Heating: Heat (H) = I²Rt.\nElectric Power (P) is the rate at which electrical energy is consumed. \nP = VI = I²R = V²/R.\nThe commercial unit of electrical energy is kilowatt-hour (kWh), commonly known as a 'unit' on your electricity bill. \n1 kWh = 1000 W × 3600 s = 3.6 × 10⁶ Joules.",
        "body_hi": "जब धारा उच्च प्रतिरोध वाले तार (हीटर में नाइक्रोम की तरह) से प्रवाहित होती है, तो यह बहुत गर्म हो जाता है। यह जूल का तापन नियम है: ऊष्मा (H) = I²Rt।\nविद्युत शक्ति (P) वह दर है जिस पर विद्युत ऊर्जा की खपत होती है।\nP = VI = I²R = V²/R।\nविद्युत ऊर्जा की व्यावसायिक इकाई किलोवाट-घंटा (kWh) है, जिसे आमतौर पर आपके बिजली बिल पर 'यूनिट' के रूप में जाना जाता है।\n1 kWh = 1000 W × 3600 s = 3.6 × 10⁶ जूल।",
        "body_gu": "જ્યારે ઉચ્ચ અવરોધવાળા વાયર (જેમ કે હીટરમાં નિક્રોમ) માંથી પ્રવાહ વહે છે, ત્યારે તે ખૂબ ગરમ થાય છે. આ જુલનો તાપીય નિયમ છે: ઉષ્મા (H) = I²Rt.\nવિદ્યુત પાવર (P) એ વિદ્યુત ઊર્જા વપરાશનો દર છે.\nP = VI = I²R = V²/R.\nવિદ્યુત ઉર્જાનો વ્યાવસાયિક એકમ કિલોવોટ-અવર (kWh) છે, જે સામાન્ય રીતે તમારા લાઇટ બિલ પર 'યુનિટ' તરીકે ઓળખાય છે.\n1 kWh = 1000 W × 3600 s = 3.6 × 10⁶ જુલ."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH11_006",
        "type": "mcq",
        "title": "NCERT Exercise Q1",
        "title_hi": "NCERT अभ्यास Q1",
        "title_gu": "NCERT સ્વાધ્યાય Q1",
        "question": "A piece of wire of resistance R is cut into five equal parts. These parts are then connected in parallel. If the equivalent resistance of this combination is R', then the ratio R/R' is:",
        "question_hi": "R प्रतिरोध वाले तार के एक टुकड़े को पांच बराबर भागों में काटा जाता है। फिर इन भागों को समानांतर क्रम में जोड़ा जाता है। यदि इस संयोजन का समतुल्य प्रतिरोध R' है, तो अनुपात R/R' क्या है?",
        "question_gu": "R અવરોધ ધરાવતા વાયરના ટુકડાને પાંચ સરખા ભાગોમાં કાપવામાં આવે છે. પછી આ ભાગોને સમાંતર જોડવામાં આવે છે. જો આ જોડાણનો સમતુલ્ય અવરોધ R' હોય, તો ગુણોત્તર R/R' શું છે?",
        "options": [
            "1/25",
            "1/5",
            "5",
            "25"
        ],
        "options_hi": [
            "1/25",
            "1/5",
            "5",
            "25"
        ],
        "options_gu": [
            "1/25",
            "1/5",
            "5",
            "25"
        ],
        "correct_index": 3,
        "explanation": "Resistance is proportional to length. Cutting the wire into 5 parts makes the resistance of each part R/5. Connecting 5 such parts in parallel: 1/R' = (5/R) + (5/R) + (5/R) + (5/R) + (5/R) = 25/R. Therefore, R' = R/25. Thus, R/R' = 25.",
        "explanation_hi": "प्रतिरोध लंबाई के आनुपातिक होता है। तार को 5 भागों में काटने से प्रत्येक भाग का प्रतिरोध R/5 हो जाता है। ऐसे 5 भागों को समानांतर में जोड़ने पर: 1/R' = 5 * (5/R) = 25/R। इसलिए, R' = R/25। इस प्रकार, R/R' = 25।",
        "explanation_gu": "અવરોધ લંબાઈના સમપ્રમાણમાં હોય છે. વાયરને 5 ભાગોમાં કાપવાથી દરેક ભાગનો અવરોધ R/5 બને છે. આવા 5 ભાગોને સમાંતર જોડતા: 1/R' = 5 * (5/R) = 25/R. તેથી, R' = R/25. આમ, R/R' = 25."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH11_007",
        "type": "mcq",
        "title": "NCERT Exercise Q2",
        "title_hi": "NCERT अभ्यास Q2",
        "title_gu": "NCERT સ્વાધ્યાય Q2",
        "question": "Which of the following terms does not represent electrical power in a circuit?",
        "question_hi": "निम्नलिखित में से कौन सा पद किसी परिपथ में विद्युत शक्ति (Electrical Power) का निरूपण नहीं करता है?",
        "question_gu": "નીચેનામાંથી કયું પદ પરિપથમાં વિદ્યુત પાવર દર્શાવતું નથી?",
        "options": [
            "I²R",
            "IR²",
            "VI",
            "V²/R"
        ],
        "options_hi": [
            "I²R",
            "IR²",
            "VI",
            "V²/R"
        ],
        "options_gu": [
            "I²R",
            "IR²",
            "VI",
            "V²/R"
        ],
        "correct_index": 1,
        "explanation": "Electric Power P = VI. By Ohm's law, V = IR, so P = (IR)I = I²R. Alternatively, since I = V/R, P = V(V/R) = V²/R. IR² is not a valid formula for power.",
        "explanation_hi": "विद्युत शक्ति P = VI। ओम के नियम से, V = IR, इसलिए P = (IR)I = I²R। वैकल्पिक रूप से, चूँकि I = V/R, P = V(V/R) = V²/R। शक्ति के लिए IR² कोई वैध सूत्र नहीं है।",
        "explanation_gu": "વિદ્યુત પાવર P = VI. ઓહ્મના નિયમ મુજબ, V = IR, તેથી P = (IR)I = I²R. વૈકલ્પિક રીતે, કારણ કે I = V/R, P = V(V/R) = V²/R. પાવર માટે IR² એ માન્ય સૂત્ર નથી."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH11_008",
        "type": "mcq",
        "title": "NCERT Exercise Q3",
        "title_hi": "NCERT अभ्यास Q3",
        "title_gu": "NCERT સ્વાધ્યાય Q3",
        "question": "An electric bulb is rated 220 V and 100 W. When it is operated on 110 V, the power consumed will be:",
        "question_hi": "कोई विद्युत बल्ब 220 V और 100 W पर निर्धारित (rated) है। जब इसे 110 V पर प्रचालित करते हैं, तब इसके द्वारा उपभुक्त शक्ति कितनी होती है?",
        "question_gu": "એક વિદ્યુત બલ્બનું રેટિંગ 220 V અને 100 W છે. જ્યારે તેને 110 V પર ચલાવવામાં આવે છે, ત્યારે વપરાતો પાવર કેટલો હશે?",
        "options": [
            "100 W",
            "75 W",
            "50 W",
            "25 W"
        ],
        "options_hi": [
            "100 W",
            "75 W",
            "50 W",
            "25 W"
        ],
        "options_gu": [
            "100 W",
            "75 W",
            "50 W",
            "25 W"
        ],
        "correct_index": 3,
        "explanation": "Resistance of the bulb remains constant. R = V²/P = (220)² / 100 = 484 Ω. When operated at 110 V, new power P' = (V')² / R = (110)² / 484 = 12100 / 484 = 25 W.",
        "explanation_hi": "बल्ब का प्रतिरोध स्थिर रहता है। R = V²/P = (220)² / 100 = 484 Ω। जब इसे 110 V पर संचालित किया जाता है, तो नई शक्ति P' = (V')² / R = (110)² / 484 = 12100 / 484 = 25 W।",
        "explanation_gu": "બલ્બનો અવરોધ અચળ રહે છે. R = V²/P = (220)² / 100 = 484 Ω. જ્યારે 110 V પર ચલાવવામાં આવે છે, ત્યારે નવો પાવર P' = (V')² / R = (110)² / 484 = 12100 / 484 = 25 W."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH11_009",
        "type": "mcq",
        "title": "NCERT Exercise Q4",
        "title_hi": "NCERT अभ्यास Q4",
        "title_gu": "NCERT સ્વાધ્યાય Q4",
        "question": "Two conducting wires of the same material and of equal lengths and equal diameters are first connected in series and then parallel in a circuit across the same potential difference. The ratio of heat produced in series and parallel combinations would be:",
        "question_hi": "समान पदार्थ, समान लंबाई और समान व्यास वाले दो चालक तारों को पहले किसी परिपथ में समान विभवांतर के पार श्रेणीक्रम में और फिर समानांतर में जोड़ा जाता है। श्रेणीक्रम और समानांतर संयोजनों में उत्पन्न ऊष्मा का अनुपात क्या होगा?",
        "question_gu": "સમાન દ્રવ્ય, સમાન લંબાઈ અને સમાન વ્યાસ ધરાવતા બે વાહક વાયરોને સમાન વિદ્યુતસ્થિતિમાનના તફાવત હેઠળ પરિપથમાં પહેલા શ્રેણીમાં અને પછી સમાંતર જોડવામાં આવે છે. શ્રેણી અને સમાંતર જોડાણોમાં ઉત્પન્ન થતી ઉષ્માનો ગુણોત્તર શું હશે?",
        "options": [
            "1:2",
            "2:1",
            "1:4",
            "4:1"
        ],
        "options_hi": [
            "1:2",
            "2:1",
            "1:4",
            "4:1"
        ],
        "options_gu": [
            "1:2",
            "2:1",
            "1:4",
            "4:1"
        ],
        "correct_index": 2,
        "explanation": "Let resistance of one wire be R. Series resistance Rs = 2R. Parallel resistance Rp = R/2. Heat H = V²t/R. Therefore, Hs = V²t / 2R and Hp = V²t / (R/2) = 2V²t / R. Ratio Hs/Hp = (1/2) / 2 = 1/4. So, 1:4.",
        "explanation_hi": "मान लीजिए एक तार का प्रतिरोध R है। श्रेणी प्रतिरोध Rs = 2R। समानांतर प्रतिरोध Rp = R/2। ऊष्मा H = V²t/R। इसलिए, Hs = V²t / 2R और Hp = V²t / (R/2) = 2V²t / R। अनुपात Hs/Hp = (1/2) / 2 = 1/4। तो, 1:4।",
        "explanation_gu": "ધારો કે એક વાયરનો અવરોધ R છે. શ્રેણી અવરોધ Rs = 2R. સમાંતર અવરોધ Rp = R/2. ઉષ્મા H = V²t/R. તેથી, Hs = V²t / 2R અને Hp = V²t / (R/2) = 2V²t / R. ગુણોત્તર Hs/Hp = (1/2) / 2 = 1/4. આમ, 1:4."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH11_010",
        "type": "mcq",
        "title": "NCERT Exercise Q5",
        "title_hi": "NCERT अभ्यास Q5",
        "title_gu": "NCERT સ્વાધ્યાય Q5",
        "question": "How is a voltmeter connected in the circuit to measure the potential difference between two points?",
        "question_hi": "दो बिंदुओं के बीच विभवांतर मापने के लिए वोल्टमीटर को परिपथ में कैसे जोड़ा जाता है?",
        "question_gu": "બે બિંદુઓ વચ્ચેનો વિદ્યુતસ્થિતિમાનનો તફાવત માપવા માટે પરિપથમાં વોલ્ટમીટરને કેવી રીતે જોડવામાં આવે છે?",
        "options": [
            "In series with the component",
            "In parallel across the two points",
            "Either in series or parallel",
            "Directly to the battery terminals only"
        ],
        "options_hi": [
            "घटक के साथ श्रेणीक्रम (series) में",
            "दोनों बिंदुओं के आर-पार समानांतर (parallel) में",
            "श्रेणीक्रम या समानांतर में से कोई भी",
            "सीधे केवल बैटरी टर्मिनलों से"
        ],
        "options_gu": [
            "ઘટકની સાથે શ્રેણીમાં",
            "બંને બિંદુઓ વચ્ચે સમાંતર જોડાણમાં",
            "શ્રેણીમાં અથવા સમાંતરમાં ગમે તેમ",
            "માત્ર બેટરીના છેડાઓ સાથે સીધું જ"
        ],
        "correct_index": 1,
        "explanation": "A voltmeter is always connected in PARALLEL across the two points where the potential difference is to be measured, because it has very high resistance and takes negligible current from the circuit.",
        "explanation_hi": "वोल्टमीटर हमेशा उन दो बिंदुओं के पार समानांतर (PARALLEL) में जुड़ा होता है जहां विभवांतर मापा जाना है, क्योंकि इसमें बहुत अधिक प्रतिरोध होता है और यह परिपथ से नगण्य (negligible) धारा लेता है।",
        "explanation_gu": "જ્યાં વિદ્યુતસ્થિતિમાનનો તફાવત માપવાનો હોય તે બે બિંદુઓ વચ્ચે વોલ્ટમીટર હંમેશા સમાંતર (PARALLEL) જોડવામાં આવે છે, કારણ કે તેનો અવરોધ ખૂબ વધારે હોય છે અને તે પરિપથમાંથી નહિવત પ્રવાહ લે છે."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH11_011",
        "type": "mcq",
        "title": "NCERT Exercise Q8",
        "title_hi": "NCERT अभ्यास Q8",
        "title_gu": "NCERT સ્વાધ્યાય Q8",
        "question": "When a 12 V battery is connected across an unknown resistor, there is a current of 2.5 mA in the circuit. Find the value of the resistance of the resistor.",
        "question_hi": "जब एक 12 V बैटरी को एक अज्ञात प्रतिरोधक से जोड़ा जाता है, तो परिपथ में 2.5 mA की धारा प्रवाहित होती है। प्रतिरोधक के प्रतिरोध का मान ज्ञात कीजिए।",
        "question_gu": "જ્યારે 12 V ની બેટરીને અજ્ઞાત અવરોધ સાથે જોડવામાં આવે છે, ત્યારે પરિપથમાં 2.5 mA નો પ્રવાહ વહે છે. અવરોધનું મૂલ્ય શોધો.",
        "options": [
            "4.8 Ω",
            "480 Ω",
            "4800 Ω",
            "48000 Ω"
        ],
        "options_hi": [
            "4.8 Ω",
            "480 Ω",
            "4800 Ω",
            "48000 Ω"
        ],
        "options_gu": [
            "4.8 Ω",
            "480 Ω",
            "4800 Ω",
            "48000 Ω"
        ],
        "correct_index": 2,
        "explanation": "According to Ohm's Law: R = V/I. Here, V = 12 V, I = 2.5 mA = 2.5 x 10^-3 A. So, R = 12 / (2.5 x 10^-3) = 12000 / 2.5 = 4800 Ω.",
        "explanation_hi": "ओम के नियम के अनुसार: R = V/I। यहाँ, V = 12 V, I = 2.5 mA = 2.5 x 10^-3 A। इसलिए, R = 12 / (2.5 x 10^-3) = 12000 / 2.5 = 4800 Ω।",
        "explanation_gu": "ઓહ્મના નિયમ મુજબ: R = V/I. અહીં, V = 12 V, I = 2.5 mA = 2.5 x 10^-3 A. તેથી, R = 12 / (2.5 x 10^-3) = 12000 / 2.5 = 4800 Ω."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH11_012",
        "type": "mcq",
        "title": "NCERT Exercise Q9",
        "title_hi": "NCERT अभ्यास Q9",
        "title_gu": "NCERT સ્વાધ્યાય Q9",
        "question": "A battery of 9 V is connected in series with resistors of 0.2 Ω, 0.3 Ω, 0.4 Ω, 0.5 Ω and 12 Ω, respectively. How much current would flow through the 12 Ω resistor?",
        "question_hi": "9 V की किसी बैटरी को 0.2 Ω, 0.3 Ω, 0.4 Ω, 0.5 Ω तथा 12 Ω के प्रतिरोधकों के साथ श्रेणीक्रम में संयोजित किया गया है। 12 Ω के प्रतिरोधक से कितनी धारा प्रवाहित होगी?",
        "question_gu": "9 V ની બેટરીને અનુક્રમે 0.2 Ω, 0.3 Ω, 0.4 Ω, 0.5 Ω અને 12 Ω ના અવરોધો સાથે શ્રેણીમાં જોડવામાં આવે છે. 12 Ω ના અવરોધમાંથી કેટલો પ્રવાહ પસાર થશે?",
        "options": [
            "0.50 A",
            "0.67 A",
            "0.75 A",
            "1.2 A"
        ],
        "options_hi": [
            "0.50 A",
            "0.67 A",
            "0.75 A",
            "1.2 A"
        ],
        "options_gu": [
            "0.50 A",
            "0.67 A",
            "0.75 A",
            "1.2 A"
        ],
        "correct_index": 1,
        "explanation": "Total resistance in series Rs = 0.2 + 0.3 + 0.4 + 0.5 + 12 = 13.4 Ω. Total current I = V / Rs = 9 / 13.4 = 0.67 A. Since they are in series, the same current flows through all resistors, including the 12 Ω one.",
        "explanation_hi": "श्रेणीक्रम में कुल प्रतिरोध Rs = 0.2 + 0.3 + 0.4 + 0.5 + 12 = 13.4 Ω। कुल धारा I = V / Rs = 9 / 13.4 = 0.67 A। चूंकि वे श्रेणीक्रम में हैं, 12 Ω वाले सहित सभी प्रतिरोधकों से समान धारा प्रवाहित होती है।",
        "explanation_gu": "શ્રેણીમાં કુલ અવરોધ Rs = 0.2 + 0.3 + 0.4 + 0.5 + 12 = 13.4 Ω. કુલ પ્રવાહ I = V / Rs = 9 / 13.4 = 0.67 A. તેઓ શ્રેણીમાં હોવાથી, 12 Ω સહિત તમામ અવરોધોમાંથી સમાન પ્રવાહ વહે છે."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH11_013",
        "type": "mcq",
        "title": "NCERT Exercise Q10",
        "title_hi": "NCERT अभ्यास Q10",
        "title_gu": "NCERT સ્વાધ્યાય Q10",
        "question": "How many 176 Ω resistors (in parallel) are required to carry 5 A on a 220 V line?",
        "question_hi": "220 V की लाइन पर 5 A धारा ले जाने के लिए (समानांतर क्रम में) कितने 176 Ω प्रतिरोधकों की आवश्यकता होगी?",
        "question_gu": "220 V લાઇન પર 5 A પ્રવાહ વહેવડાવવા માટે (સમાંતરમાં) કેટલા 176 Ω ના અવરોધોની જરૂર પડશે?",
        "options": [
            "2",
            "3",
            "4",
            "5"
        ],
        "options_hi": [
            "2",
            "3",
            "4",
            "5"
        ],
        "options_gu": [
            "2",
            "3",
            "4",
            "5"
        ],
        "correct_index": 2,
        "explanation": "Required equivalent resistance R_eq = V / I = 220 / 5 = 44 Ω. If 'n' resistors of 176 Ω are in parallel, R_eq = 176 / n. So, 44 = 176 / n => n = 176 / 44 = 4 resistors.",
        "explanation_hi": "आवश्यक समतुल्य प्रतिरोध R_eq = V / I = 220 / 5 = 44 Ω। यदि 176 Ω के 'n' प्रतिरोधक समानांतर में हैं, R_eq = 176 / n। तो, 44 = 176 / n => n = 176 / 44 = 4 प्रतिरोधक।",
        "explanation_gu": "જરૂરી સમતુલ્ય અવરોધ R_eq = V / I = 220 / 5 = 44 Ω. જો 176 Ω ના 'n' અવરોધો સમાંતર હોય, તો R_eq = 176 / n. તેથી, 44 = 176 / n => n = 176 / 44 = 4 અવરોધો."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH11_014",
        "type": "mcq",
        "title": "NCERT Exercise Q12",
        "title_hi": "NCERT अभ्यास Q12",
        "title_gu": "NCERT સ્વાધ્યાય Q12",
        "question": "Several electric bulbs designed to be used on a 220 V electric supply line, are rated 10 W. How many lamps can be connected in parallel with each other across the two wires of 220 V line if the maximum allowable current is 5 A?",
        "question_hi": "220 V विद्युत आपूर्ति लाइन पर उपयोग किए जाने के लिए डिज़ाइन किए गए कई इलेक्ट्रिक बल्ब 10 W रेट किए गए हैं। यदि अधिकतम स्वीकार्य धारा 5 A है, तो 220 V लाइन के दो तारों के आर-पार कितने लैंप समानांतर में जोड़े जा सकते हैं?",
        "question_gu": "220 V વિદ્યુત સપ્લાય લાઇન પર ઉપયોગ કરવા માટે રચાયેલ કેટલાક વિદ્યુત બલ્બનું રેટિંગ 10 W છે. જો મહત્તમ સ્વીકાર્ય પ્રવાહ 5 A હોય, તો 220 V લાઇનમાં એકબીજા સાથે સમાંતરમાં કેટલા બલ્બ જોડી શકાય?",
        "options": [
            "11",
            "50",
            "110",
            "220"
        ],
        "options_hi": [
            "11",
            "50",
            "110",
            "220"
        ],
        "options_gu": [
            "11",
            "50",
            "110",
            "220"
        ],
        "correct_index": 2,
        "explanation": "Total max power allowed P_total = V × I = 220 V × 5 A = 1100 W. Since each bulb takes 10 W, the number of bulbs = Total Power / Power per bulb = 1100 / 10 = 110 bulbs.",
        "explanation_hi": "अनुमत कुल अधिकतम शक्ति P_total = V × I = 220 V × 5 A = 1100 W। चूंकि प्रत्येक बल्ब 10 W लेता है, बल्बों की संख्या = कुल शक्ति / प्रति बल्ब शक्ति = 1100 / 10 = 110 बल्ब।",
        "explanation_gu": "મહત્તમ સ્વીકાર્ય કુલ પાવર P_total = V × I = 220 V × 5 A = 1100 W. દરેક બલ્બ 10 W વાપરે છે, તેથી બલ્બની સંખ્યા = કુલ પાવર / એક બલ્બનો પાવર = 1100 / 10 = 110 બલ્બ."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH11_015",
        "type": "mcq",
        "title": "NCERT Exercise Q15",
        "title_hi": "NCERT अभ्यास Q15",
        "title_gu": "NCERT સ્વાધ્યાય Q15",
        "question": "Two lamps, one rated 100 W at 220 V, and the other 60 W at 220 V, are connected in parallel to electric mains supply. What current is drawn from the line if the supply voltage is 220 V?",
        "question_hi": "दो लैंप, जिनमें से एक 220 V पर 100 W और दूसरा 220 V पर 60 W रेटेड है, बिजली की मुख्य आपूर्ति के समानांतर जुड़े हुए हैं। यदि आपूर्ति वोल्टेज 220 V है तो लाइन से कितनी धारा ली जाती है?",
        "question_gu": "બે લેમ્પ, જેમાંથી એકનું રેટિંગ 220 V પર 100 W અને બીજાનું 220 V પર 60 W છે, તેમને ઇલેક્ટ્રિક મેઇન સપ્લાય સાથે સમાંતર જોડવામાં આવે છે. જો સપ્લાય વોલ્ટેજ 220 V હોય તો લાઇનમાંથી કેટલો પ્રવાહ ખેંચાશે?",
        "options": [
            "0.727 A",
            "1.25 A",
            "0.27 A",
            "2.5 A"
        ],
        "options_hi": [
            "0.727 A",
            "1.25 A",
            "0.27 A",
            "2.5 A"
        ],
        "options_gu": [
            "0.727 A",
            "1.25 A",
            "0.27 A",
            "2.5 A"
        ],
        "correct_index": 0,
        "explanation": "In parallel, voltages are equal. Current by 1st lamp I1 = P1/V = 100/220 = 5/11 A. Current by 2nd lamp I2 = P2/V = 60/220 = 3/11 A. Total current I = I1 + I2 = 5/11 + 3/11 = 8/11 A = 0.727 A.",
        "explanation_hi": "समानांतर में, वोल्टेज समान होते हैं। पहले लैंप द्वारा धारा I1 = P1/V = 100/220 = 5/11 A। दूसरे लैंप द्वारा धारा I2 = P2/V = 60/220 = 3/11 A। कुल धारा I = I1 + I2 = 5/11 + 3/11 = 8/11 A = 0.727 A।",
        "explanation_gu": "સમાંતરમાં, વોલ્ટેજ સમાન હોય છે. પ્રથમ લેમ્પ દ્વારા લેવાતો પ્રવાહ I1 = P1/V = 100/220 = 5/11 A. બીજા લેમ્પ દ્વારા લેવાતો પ્રવાહ I2 = P2/V = 60/220 = 3/11 A. કુલ પ્રવાહ I = I1 + I2 = 5/11 + 3/11 = 8/11 A = 0.727 A."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH11_016",
        "type": "mcq",
        "title": "NCERT Exercise Q16",
        "title_hi": "NCERT अभ्यास Q16",
        "title_gu": "NCERT સ્વાધ્યાય Q16",
        "question": "Which uses more energy, a 250 W TV set in 1 hr, or a 1200 W toaster in 10 minutes?",
        "question_hi": "किसमें अधिक ऊर्जा का उपयोग होता है, 1 घंटे में 250 W टीवी सेट में, या 10 मिनट में 1200 W टोस्टर में?",
        "question_gu": "કોનામાં વધુ ઊર્જા વપરાય છે, 1 કલાકમાં 250 W ના ટીવી સેટમાં કે 10 મિનિટમાં 1200 W ના ટોસ્ટરમાં?",
        "options": [
            "The toaster uses more energy.",
            "The TV set uses more energy.",
            "Both use the exact same amount of energy.",
            "Cannot be determined."
        ],
        "options_hi": [
            "टोस्टर अधिक ऊर्जा का उपयोग करता है।",
            "टीवी सेट अधिक ऊर्जा का उपयोग करता है।",
            "दोनों बिल्कुल समान मात्रा में ऊर्जा का उपयोग करते हैं।",
            "निर्धारित नहीं किया जा सकता।"
        ],
        "options_gu": [
            "ટોસ્ટર વધુ ઉર્જા વાપરે છે.",
            "ટીવી સેટ વધુ ઉર્જા વાપરે છે.",
            "બંને બરાબર સમાન માત્રામાં ઉર્જા વાપરે છે.",
            "નક્કી કરી શકાય નહીં."
        ],
        "correct_index": 1,
        "explanation": "Energy = Power × Time. For TV: E = 250 W × 1 hr = 250 Watt-hours (Wh). For toaster: 10 mins = 10/60 = 1/6 hr. E = 1200 W × (1/6) hr = 200 Wh. 250 Wh > 200 Wh. Thus, the TV uses more energy.",
        "explanation_hi": "ऊर्जा = शक्ति × समय। टीवी के लिए: E = 250 W × 1 घंटा = 250 वाट-घंटा (Wh)। टोस्टर के लिए: 10 मिनट = 10/60 = 1/6 घंटा। E = 1200 W × (1/6) घंटा = 200 Wh। 250 Wh > 200 Wh। इस प्रकार, टीवी अधिक ऊर्जा का उपयोग करता है।",
        "explanation_gu": "ઊર્જા = પાવર × સમય. ટીવી માટે: E = 250 W × 1 કલાક = 250 વોટ-અવર (Wh). ટોસ્ટર માટે: 10 મિનિટ = 10/60 = 1/6 કલાક. E = 1200 W × (1/6) કલાક = 200 Wh. 250 Wh > 200 Wh. આમ, ટીવી વધુ ઊર્જા વાપરે છે."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH11_017",
        "type": "mcq",
        "title": "NCERT Exercise Q18",
        "title_hi": "NCERT अभ्यास Q18",
        "title_gu": "NCERT સ્વાધ્યાય Q18",
        "question": "Why are conductors of electric heating devices, such as bread-toasters and electric irons, made of an alloy rather than a pure metal?",
        "question_hi": "ब्रेड-टोस्टर और इलेक्ट्रिक आयरन जैसे विद्युत ताप उपकरणों के चालक शुद्ध धातु के बजाय मिश्र धातु (alloy) के क्यों बने होते हैं?",
        "question_gu": "બ્રેડ-ટોસ્ટર અને ઇલેક્ટ્રિક ઇસ્ત્રી જેવા વિદ્યુત તાપીય ઉપકરણોના વાહકો શુદ્ધ ધાતુને બદલે મિશ્રધાતુ (alloy) ના શા માટે બનેલા હોય છે?",
        "options": [
            "Because alloys are cheaper to manufacture.",
            "Because alloys have lower resistivity and conduct better.",
            "Because alloys have higher resistivity than pure metals and do not oxidize (burn) readily at high temperatures.",
            "Because pure metals cannot be shaped into coils."
        ],
        "options_hi": [
            "क्योंकि मिश्र धातुएँ बनाने में सस्ती होती हैं।",
            "क्योंकि मिश्र धातुओं में प्रतिरोधकता कम होती है और वे बेहतर चालक होती हैं।",
            "क्योंकि मिश्र धातुओं में शुद्ध धातुओं की तुलना में उच्च प्रतिरोधकता होती है और वे उच्च तापमान पर आसानी से ऑक्सीकृत (जलती) नहीं होती हैं।",
            "क्योंकि शुद्ध धातुओं को कुंडलियों (coils) का आकार नहीं दिया जा सकता है।"
        ],
        "options_gu": [
            "કારણ કે મિશ્રધાતુઓ બનાવવામાં સસ્તી હોય છે.",
            "કારણ કે મિશ્રધાતુઓની અવરોધકતા ઓછી હોય છે અને તે વધુ સારું વહન કરે છે.",
            "કારણ કે મિશ્રધાતુઓની અવરોધકતા શુદ્ધ ધાતુઓ કરતાં વધુ હોય છે અને ઊંચા તાપમાને તે સરળતાથી ઓક્સિડાઇઝ (બળી) થતી નથી.",
            "કારણ કે શુદ્ધ ધાતુઓને કોઈલમાં આકાર આપી શકાતો નથી."
        ],
        "correct_index": 2,
        "explanation": "Alloys like Nichrome are used because they have higher resistivity (producing more heat) and they do not undergo oxidation (burn) easily even when they get red hot.",
        "explanation_hi": "नाइक्रोम जैसी मिश्र धातुओं का उपयोग इसलिए किया जाता है क्योंकि उनकी प्रतिरोधकता अधिक होती है (अधिक गर्मी पैदा करती है) और लाल गर्म होने पर भी उनका ऑक्सीकरण (जलना) आसानी से नहीं होता है।",
        "explanation_gu": "નિક્રોમ જેવી મિશ્રધાતુઓનો ઉપયોગ કરવામાં આવે છે કારણ કે તેમની અવરોધકતા વધુ હોય છે (વધુ ગરમી પેદા કરે છે) અને લાલ ગરમ થાય ત્યારે પણ તેઓ સરળતાથી ઓક્સિડાઇઝ (બળી જતી) થતી નથી."
    }
]

data = {
    "metadata": {
        "id": "ncert_class10_science_ch11",
        "title": "Chapter 11: Electricity",
        "subject": "Science",
        "grade": "10"
    },
    "blocks": blocks
}

output_path = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_science_ch11.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Successfully wrote {len(blocks)} blocks to {output_path}")
