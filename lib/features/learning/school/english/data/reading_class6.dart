import '../models/chapter.dart' show InlineGloss;
import '../models/practice_question.dart';
import '../models/reading_passage.dart';

const class6Reading = ReadingLibrary(
  id: 'class6_reading',
  title: 'Reading Passages',
  grade: 'Class 6',
  passages: [
    ReadingPassage(
      id: 'class6_reading_coral',
      title: 'The Coral Reef Detective',
      emoji: '🪸',
      grade: 'Class 6',
      difficulty: Difficulty.medium,
      body: 'Dr. Anjali Menon had spent fifteen years studying the coral reefs along India\'s southern coast, '
          'but nothing had prepared her for what she found near the Gulf of Kutch that monsoon season. Diving '
          'through the shallow, sunlit water, she noticed a strange, pale patch of coral that seemed to glow '
          'faintly even in daylight. Most corals she had catalogued were either vividly colourful or, when '
          'unhealthy, bleached completely white. This coral was different: a soft lavender, spreading in a neat '
          'ring like a crown on the seabed.\n\n'
          'Back at her research station, Anjali examined water samples and temperature readings from the spot. '
          'She discovered that the coral was producing a natural pigment in response to slightly warmer water, '
          'almost like a sunscreen protecting itself from the changing climate. If this was true, these corals '
          'might be naturally adapting to survive rising sea temperatures that had destroyed reefs elsewhere in '
          'the world. It was a discovery that could change how scientists thought about ocean conservation.\n\n'
          'Anjali knew she could not celebrate alone. She spent the next three weeks training local fishermen '
          'and students from a nearby coastal school to monitor the reef carefully, teaching them how to measure '
          'water temperature and record any changes in the coral\'s colour. The fishermen, who depended on the '
          'reef\'s fish population for their livelihood, quickly understood why protecting this fragile ring of '
          'coral mattered so much. Together, they built a small floating marker to keep boats from anchoring too '
          'close to the reef.\n\n'
          'Months later, Anjali published her findings, describing the lavender coral as a possible sign of hope '
          'for reefs worldwide. Marine biologists from other countries wrote to her, eager to search their own '
          'coastlines for similar adaptations. Anjali often told her students that the greatest discoveries were '
          'not always made in laboratories far away, but sometimes right along the shores where people had lived '
          'and fished for generations, if only someone took the time to look closely enough.',
      bodyHi: 'डॉ. अंजलि मेनन ने भारत के दक्षिणी तट पर मूंगा चट्टानों का अध्ययन करने में पंद्रह साल बिताए थे, लेकिन उस मानसून के मौसम में कच्छ की खाड़ी के पास उन्हें जो कुछ मिला, उसके लिए उन्हें किसी भी चीज़ ने तैयार नहीं किया था। उथले, सूरज की रोशनी वाले पानी में गोता लगाते हुए, उसने मूंगे का एक अजीब, पीला टुकड़ा देखा जो दिन के उजाले में भी हल्का चमकता हुआ लग रहा था। उनके द्वारा सूचीबद्ध किए गए अधिकांश मूंगे या तो बहुत रंगीन थे या, अस्वस्थ होने पर, पूरी तरह से सफेद हो गए थे। यह मूंगा अलग था: एक नरम लैवेंडर, जो समुद्र तल पर एक मुकुट की तरह एक साफ रिंग में फैला हुआ था।\n\nअपने अनुसंधान केंद्र पर वापस, अंजलि ने मौके से पानी के नमूने और तापमान रीडिंग की जांच की। उसने पाया कि मूंगा थोड़े गर्म पानी की प्रतिक्रिया में एक प्राकृतिक रंगद्रव्य का उत्पादन कर रहा था, जो लगभग एक सनस्क्रीन की तरह खुद को बदलती जलवायु से बचाता है। यदि यह सच है, तो ये मूंगे समुद्र के बढ़ते तापमान से बचने के लिए स्वाभाविक रूप से अनुकूल हो सकते हैं, जिसने दुनिया में अन्य जगहों पर चट्टानों को नष्ट कर दिया है। यह एक ऐसी खोज थी जो समुद्र संरक्षण के बारे में वैज्ञानिकों की सोच को बदल सकती थी।\n\nअंजलि को पता था कि वह अकेले जश्न नहीं मना सकती। उन्होंने अगले तीन सप्ताह स्थानीय मछुआरों और पास के एक तटीय स्कूल के छात्रों को चट्टान की सावधानीपूर्वक निगरानी करने के लिए प्रशिक्षित करने, उन्हें पानी का तापमान मापने और मूंगे के रंग में किसी भी बदलाव को रिकॉर्ड करने का तरीका सिखाया। मछुआरे, जो अपनी आजीविका के लिए चट्टान की मछली की आबादी पर निर्भर थे, जल्दी ही समझ गए कि मूंगे की इस नाजुक अंगूठी की रक्षा करना इतना महत्वपूर्ण क्यों है। साथ में, उन्होंने नावों को चट्टान के बहुत करीब आने से रोकने के लिए एक छोटा तैरता हुआ मार्कर बनाया।\n\nमहीनों बाद, अंजलि ने अपने निष्कर्ष प्रकाशित किए, जिसमें लैवेंडर कोरल को दुनिया भर में चट्टानों के लिए आशा का एक संभावित संकेत बताया गया। अन्य देशों के समुद्री जीवविज्ञानियों ने उन्हें पत्र लिखा, जो समान अनुकूलन के लिए अपने स्वयं के समुद्र तट की खोज करने के लिए उत्सुक थे। अंजलि अक्सर अपने छात्रों से कहती थीं कि सबसे बड़ी खोजें हमेशा दूर की प्रयोगशालाओं में नहीं की जातीं, बल्कि कभी-कभी समुद्र के किनारे भी की जाती हैं, जहां लोग पीढ़ियों से रहते थे और मछली पकड़ते थे, अगर किसी ने समय निकालकर करीब से देखा हो।',
      bodyGu: '''ડૉ. અંજલિ મેનને ભારતના દક્ષિણ કાંઠે પરવાળાના ખડકોનો અભ્યાસ કરવામાં પંદર વર્ષ વિતાવ્યા હતા, પરંતુ તે ચોમાસાની ઋતુમાં કચ્છના અખાત પાસે તેમને જે કંઈ મળ્યું, તેના માટે તેમને કોઈ પણ બાબતે તૈયાર કર્યા ન હતા. છીછરા, સૂર્યપ્રકાશવાળા પાણીમાં ડૂબકી લગાવતી વખતે, તેણે પરવાળાનો એક વિચિત્ર, આછો ટુકડો જોયો જે ધોળા દિવસે પણ હળવો ચમકતો હોય તેવું લાગતું હતું. તેમના દ્વારા સૂચિબદ્ધ કરવામાં આવેલા મોટાભાગના પરવાળા કાં તો ખૂબ રંગીન હતા અથવા, અસ્વસ્થ થવા પર, સંપૂર્ણપણે સફેદ થઈ ગયા હતા. આ પરવાળું અલગ હતું: એક નરમ લવંડર, જે સમુદ્રતળ પર એક મુગટની જેમ ચોખ્ખી રીંગમાં ફેલાયેલું હતું.

પોતાના સંશોધન કેન્દ્ર પર પાછા ફરીને, અંજલિએ તે જગ્યાના પાણીના નમૂના અને તાપમાનના રીડિંગની તપાસ કરી. તેણે જોયું કે પરવાળું થોડા ગરમ પાણીની પ્રતિક્રિયામાં એક કુદરતી રંજકદ્રવ્યનું ઉત્પાદન કરી રહ્યું હતું, જે લગભગ એક સનસ્ક્રીનની જેમ પોતાને બદલાતી આબોહવાથી બચાવે છે. જો આ સાચું છે, તો આ પરવાળા સમુદ્રના વધતા તાપમાનથી બચવા માટે સ્વાભાવિક રીતે જ અનુકૂળ થઈ શકે છે, જેણે દુનિયામાં અન્ય જગ્યાઓ પર ખડકોને નષ્ટ કરી દીધા છે. આ એક એવી શોધ હતી જે સમુદ્ર સંરક્ષણ વિશે વૈજ્ઞાનિકોની વિચારસરણીને બદલી શકે તેમ હતી.

અંજલિને ખબર હતી કે તે એકલી ઉજવણી કરી શકે નહીં. તેણે આગામી ત્રણ અઠવાડિયા સ્થાનિક માછીમારો અને નજીકની એક દરિયાકાંઠાની શાળાના વિદ્યાર્થીઓને ખડકની સાવચેતીપૂર્વક દેખરેખ રાખવા માટે તાલીમ આપવા, તેમને પાણીનું તાપમાન માપવા અને પરવાળાના રંગમાં કોઈપણ ફેરફારને નોંધવાની રીત શીખવી. માછીમારો, જે પોતાની આજીવિકા માટે ખડકની માછલીઓની વસ્તી પર નિર્ભર હતા, તેઓ ઝડપથી સમજી ગયા કે પરવાળાની આ નાજુક રીંગનું રક્ષણ કરવું આટલું મહત્વપૂર્ણ કેમ છે. સાથે મળીને, તેઓએ હોડીઓને ખડકની ખૂબ નજીક આવતી રોકવા માટે એક નાનું તરતું માર્કર બનાવ્યું.

મહિનાઓ પછી, અંજલિએ પોતાના તારણો પ્રકાશિત કર્યા, જેમાં લવંડર કોરલ (પરવાળા) ને દુનિયાભરમાં ખડકો માટે આશાનો એક સંભવિત સંકેત ગણાવ્યો હતો. અન્ય દેશોના દરિયાઈ જીવવિજ્ઞાનીઓએ તેમને પત્ર લખ્યા, જેઓ સમાન અનુકૂલન માટે પોતાના જ દરિયાકાંઠાની શોધ કરવા માટે આતુર હતા. અંજલિ વારંવાર પોતાના વિદ્યાર્થીઓને કહેતી હતી કે સૌથી મોટી શોધો હંમેશા દૂરની પ્રયોગશાળાઓમાં નથી થતી, પરંતુ ક્યારેક દરિયાકિનારે પણ થાય છે, જ્યાં લોકો પેઢીઓથી રહેતા હોય અને માછલી પકડતા હોય, જો કોઈએ સમય કાઢીને નજીકથી જોયું હોય.''',
      questions: [
        PracticeQuestion(
          prompt: 'What made the coral Anjali found unusual compared to the corals she had seen before?',
          options: [
            'It was found far away from any coastline.',
            'It was bright red and very large.',
            'It was a soft lavender colour and glowed faintly, unlike typical colourful or bleached corals.',
            'It had completely disappeared from the seabed.',
          ],
          correctIndex: 2,
          explanation: 'The passage describes the coral as "a soft lavender" that "seemed to glow faintly", unlike the usual colourful or bleached-white corals she had catalogued.',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'According to Anjali\'s research, why might the coral have been producing the lavender pigment?',
          options: [
            'As a possible natural response to protect itself from warmer water, like a sunscreen.',
            'To attract more fish to the reef.',
            'Because it was dying from pollution.',
            'To change colour with the seasons for camouflage.',
          ],
          correctIndex: 0,
          explanation: 'The passage explains she found the coral "producing a natural pigment in response to slightly warmer water, almost like a sunscreen protecting itself".',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'Why did Anjali train local fishermen and students to monitor the reef?',
          options: [
            'Because the fishermen already knew more about coral than she did.',
            'Because she planned to leave the research station permanently.',
            'Because she wanted to stop fishing in the area entirely.',
            'Because monitoring the fragile coral needed ongoing help, and the fishermen\'s livelihoods depended on the reef.',
          ],
          correctIndex: 3,
          explanation: 'The passage says she trained them because she "could not celebrate alone" and the fishermen "depended on the reef\'s fish population for their livelihood".',
          difficulty: Difficulty.hard,
        ),
        PracticeQuestion(
          prompt: 'What is the main message Anjali often shared with her students, according to the last paragraph?',
          options: [
            'Great discoveries only happen in advanced laboratories overseas.',
            'Important discoveries can be made close to home, by people who look closely at familiar places.',
            'Coral reefs cannot survive climate change no matter what is done.',
            'Fishing should be banned everywhere to protect coral reefs.',
          ],
          correctIndex: 1,
          explanation: 'The final sentence states that "the greatest discoveries were not always made in laboratories far away, but sometimes right along the shores... if only someone took the time to look closely enough."',
          difficulty: Difficulty.hard,
        ),
      ],
      glosses: [
        InlineGloss(word: 'catalogued', meaningHi: 'सूची में दर्ज किया', hiTransliteration: 'suchi mein darj kiya', meaningGu: 'યાદીમાં નોંધ્યું / સૂચિબદ્ધ કર્યું', guTransliteration: 'yaadima nondhyu / suchibaddh karyu'),
        InlineGloss(word: 'bleached', meaningHi: 'रंग उड़ा हुआ / सफेद पड़ा हुआ', hiTransliteration: 'rang uda hua / safed pada hua', meaningGu: 'રંગ ઉડી ગયેલો / સફેદ પડી ગયેલું', guTransliteration: 'rang udi gayelo / safed padi gayelu'),
        InlineGloss(word: 'pigment', meaningHi: 'रंग बनाने वाला तत्व', hiTransliteration: 'rang banane wala tatva', meaningGu: 'રંગદ્રવ્ય / રંગ બનાવનારું તત્વ', guTransliteration: 'rangdravya / rang banavnaru tatva'),
        InlineGloss(word: 'adapting', meaningHi: 'खुद को ढाल लेना', hiTransliteration: 'khud ko dhaal lena', meaningGu: 'પોતાને અનુકૂળ બનાવવું / ઢાળી લેવું', guTransliteration: 'potane anukul banavvu / dhali levu'),
        InlineGloss(word: 'conservation', meaningHi: 'संरक्षण / बचाव', hiTransliteration: 'sanrakshan / bachaav', meaningGu: 'સંરક્ષણ / બચાવ', guTransliteration: 'sanrakshan / bachaav'),
        InlineGloss(word: 'fragile', meaningHi: 'नाज़ुक', hiTransliteration: 'naazuk', meaningGu: 'નાજુક / તૂટી જાય તેવું', guTransliteration: 'naajuk / tuti jaay tevu'),
        InlineGloss(word: 'anchoring', meaningHi: 'नाव को लंगर डालकर रोकना', hiTransliteration: 'naav ko langar daalkar rokna', meaningGu: 'હોડીને લંગર નાખીને રોકવી', guTransliteration: 'hodine langar nakhine rokvi'),
        InlineGloss(word: 'biologists', meaningHi: 'जीव विज्ञानी', hiTransliteration: 'jeev vigyani', meaningGu: 'જીવવિજ્ઞાનીઓ', guTransliteration: 'jeevvigyanio'),
        InlineGloss(word: 'coastlines', meaningHi: 'समुद्र तट', hiTransliteration: 'samudra tat', meaningGu: 'દરિયાકિનારો / સમુદ્રતટ', guTransliteration: 'dariyakinaro / samudratat'),
        InlineGloss(word: 'livelihood', meaningHi: 'रोज़ी-रोटी / जीविका', hiTransliteration: 'rozi-roti / jeevika', meaningGu: 'રોજીરોટી / આજીવિકા', guTransliteration: 'rojiroti / aajivika'),
      ],
    ),
    ReadingPassage(
      id: 'class6_reading_lantern',
      title: 'The Lantern Maker\'s Choice',
      emoji: '🏮',
      grade: 'Class 6',
      difficulty: Difficulty.hard,
      body: 'In the old quarter of a small Gujarati town, Devraj had inherited his grandfather\'s lantern workshop '
          'when he was barely eighteen. For years, the family had made brass and paper lanterns for Diwali, each '
          'one hand-painted with patterns passed down through three generations. Business had always been modest '
          'but steady, enough to support Devraj, his mother, and his younger sister, who dreamed of becoming a '
          'doctor.\n\n'
          'One autumn, a large trading company offered Devraj a contract that would triple his income overnight. '
          'They wanted him to abandon his handmade lanterns and instead assemble cheap plastic ones on a machine '
          'they would install in his workshop. The money would easily pay for his sister\'s medical college fees, '
          'something Devraj had worried about for months. Yet something about the offer troubled him deeply. His '
          'grandfather\'s designs, the careful brushstrokes learned over childhood evenings, would vanish from the '
          'workshop forever, replaced by identical plastic shells stamped out by machines.\n\n'
          'Devraj spent three sleepless nights weighing his decision. He spoke with old customers who still bought '
          'his lanterns each year, not merely for light, but for the memory of his grandfather\'s hands shaping the '
          'brass. He spoke with his mother, who reminded him gently that a craft dies the moment no one is willing '
          'to sacrifice for it, but also that a daughter\'s future should never be sacrificed for a tradition '
          'alone.\n\n'
          'In the end, Devraj proposed something neither his mother nor the company expected. He would keep making '
          'his handmade lanterns, but he would also take a smaller, second contract to paint decorative brass '
          'fittings for the company\'s furniture line, work that used his real skill without erasing it. The income '
          'was less than the original offer, but enough, combined with a scholarship his sister later earned, to '
          'support her studies. Word of his handmade lanterns eventually reached shopkeepers in other cities, and '
          'slowly, the workshop grew known not for cheap convenience, but for a craft that had chosen to survive on '
          'its own terms.',
      bodyHi: 'एक छोटे से गुजराती शहर के पुराने क्वार्टर में, देवराज को अपने दादा की लालटेन कार्यशाला विरासत में मिली थी जब वह केवल अठारह वर्ष के थे। वर्षों से, परिवार ने दिवाली के लिए पीतल और कागज के लालटेन बनाए थे, प्रत्येक को तीन पीढ़ियों से चले आ रहे पैटर्न के साथ हाथ से चित्रित किया गया था। व्यवसाय हमेशा सामान्य लेकिन स्थिर था, जो देवराज, उनकी मां और उनकी छोटी बहन का समर्थन करने के लिए पर्याप्त था, जो डॉक्टर बनने का सपना देखते थे।\n\nएक शरद ऋतु में, एक बड़ी व्यापारिक कंपनी ने देवराज को एक अनुबंध की पेशकश की, जिससे उनकी आय रातोंरात तीन गुना हो जाएगी। वे चाहते थे कि वह अपने हाथ से बने लालटेन को छोड़ दें और इसके बजाय सस्ते प्लास्टिक के लालटेन को एक मशीन पर असेंबल करें जिसे वे अपनी कार्यशाला में स्थापित करेंगे। इस पैसे से उसकी बहन की मेडिकल कॉलेज की फीस आसानी से चुकाई जा सकेगी, इस बात को लेकर देवराज कई महीनों से चिंतित था। फिर भी प्रस्ताव के बारे में कुछ बात ने उसे बहुत परेशान किया। उनके दादाजी के डिज़ाइन, बचपन की शामों में सीखे गए सावधानीपूर्वक ब्रशस्ट्रोक, कार्यशाला से हमेशा के लिए गायब हो जाते थे, उनकी जगह मशीनों द्वारा मुद्रित समान प्लास्टिक के गोले ले लेते थे।\n\nदेवराज ने अपने निर्णय पर विचार करते हुए तीन रातों की नींद हराम कर दी। उन्होंने पुराने ग्राहकों से बात की, जो अभी भी हर साल उनकी लालटेन खरीदते थे, न केवल रोशनी के लिए, बल्कि अपने दादाजी के हाथों द्वारा पीतल को आकार देने की स्मृति के लिए। उन्होंने अपनी मां से बात की, जिन्होंने उन्हें धीरे से याद दिलाया कि एक शिल्प उसी क्षण मर जाता है जब कोई इसके लिए बलिदान देने को तैयार नहीं होता है, लेकिन यह भी कि एक बेटी के भविष्य को केवल एक परंपरा के लिए बलिदान नहीं किया जाना चाहिए।\n\nअंत में, देवराज ने कुछ ऐसा प्रस्ताव रखा जिसकी न तो उनकी मां को उम्मीद थी और न ही कंपनी को। वह अपने हाथ से बने लालटेन बनाना जारी रखेगा, लेकिन वह कंपनी की फ़र्निचर लाइन के लिए सजावटी पीतल की फिटिंग को पेंट करने का एक छोटा, दूसरा अनुबंध भी लेगा, इस काम में उसके वास्तविक कौशल को मिटाए बिना इस्तेमाल किया जाएगा। आय मूल प्रस्ताव से कम थी, लेकिन उसकी बहन को बाद में मिली छात्रवृत्ति के साथ मिलकर उसकी पढ़ाई में मदद करने के लिए पर्याप्त थी। उनके हस्तनिर्मित लालटेन की बात अंततः दूसरे शहरों के दुकानदारों तक पहुँची, और धीरे-धीरे, कार्यशाला सस्ती सुविधा के लिए नहीं, बल्कि एक ऐसे शिल्प के लिए जानी जाने लगी, जिसने अपनी शर्तों पर जीवित रहने का विकल्प चुना था।',
      bodyGu: '''એક નાના ગુજરાતી શહેરના જૂના વિસ્તારમાં, દેવરાજને તેના દાદાની ફાનસ બનાવવાની દુકાન વારસામાં મળી હતી જ્યારે તે માત્ર અઢાર વર્ષનો હતો. વર્ષોથી, આ પરિવારે દિવાળી માટે પિત્તળ અને કાગળના ફાનસ બનાવ્યા હતા, જે દરેક ત્રણ પેઢીથી ચાલી આવતી ડિઝાઇન સાથે હાથેથી રંગવામાં આવ્યા હતા. વ્યવસાય હંમેશાં સાધારણ પરંતુ સ્થિર હતો, જે દેવરાજ, તેની માતા અને તેની નાની બહેનનું ભરણપોષણ કરવા માટે પૂરતો હતો, જે ડૉક્ટર બનવાનું સ્વપ્ન જોતી હતી.

એક પાનખરમાં, એક મોટી વેપારી કંપનીએ દેવરાજને એક કરારની ઓફર કરી, જેનાથી તેની આવક રાતોરાત ત્રણ ગણી થઈ જશે. તેઓ ઈચ્છતા હતા કે તે તેના હાથે બનાવેલા ફાનસ છોડી દે અને તેના બદલે સસ્તા પ્લાસ્ટિકના ફાનસને એક મશીન પર એસેમ્બલ કરે જે તેઓ તેની વર્કશોપમાં સ્થાપિત કરશે. આ પૈસાથી તેની બહેનની મેડિકલ કૉલેજની ફી સરળતાથી ભરી શકાશે, આ વાતને લઈને દેવરાજ ઘણા મહિનાઓથી ચિંતિત હતો. તેમ છતાં આ પ્રસ્તાવ વિશેની કોઈક બાબતે તેને ખૂબ પરેશાન કર્યો. તેના દાદાની ડિઝાઇન, બાળપણની સાંજમાં શીખેલા સાવચેતીપૂર્વકના બ્રશસ્ટ્રોક, વર્કશોપમાંથી કાયમ માટે ગાયબ થઈ જશે, અને તેની જગ્યાએ મશીનો દ્વારા બનાવવામાં આવેલા એકસમાન પ્લાસ્ટિકના શેલ લઈ લેશે.

દેવરાજે તેના નિર્ણય પર વિચાર કરતા ત્રણ રાતની ઊંઘ હરામ કરી દીધી. તેણે જૂના ગ્રાહકો સાથે વાત કરી, જેઓ હજી પણ દર વર્ષે તેમના ફાનસ ખરીદતા હતા, માત્ર પ્રકાશ માટે જ નહીં, પરંતુ તેના દાદાના હાથ દ્વારા પિત્તળને આકાર આપવાની યાદ માટે પણ. તેણે તેની માતા સાથે વાત કરી, જેણે તેને ધીમેથી યાદ અપાવ્યું કે કળા એ જ ક્ષણે મરી જાય છે જ્યારે કોઈ તેના માટે બલિદાન આપવા તૈયાર ન હોય, પરંતુ એ પણ કે એક દીકરીના ભવિષ્યને માત્ર એક પરંપરા માટે બલિદાન ન આપવું જોઈએ.

અંતે, દેવરાજે કંઈક એવો પ્રસ્તાવ મૂક્યો જેની ન તો તેની માતાને અપેક્ષા હતી કે ન તો કંપનીને. તે તેના હાથે બનાવેલા ફાનસ બનાવવાનું ચાલુ રાખશે, પરંતુ તે કંપનીની ફર્નિચર લાઇન માટે સુશોભિત પિત્તળના ફિટિંગને રંગવાનો એક નાનો, બીજો કરાર પણ લેશે, જે કામમાં તેની વાસ્તવિક કુશળતા ભૂંસાયા વિના ઉપયોગમાં લેવાશે. આવક મૂળ પ્રસ્તાવ કરતા ઓછી હતી, પરંતુ તેની બહેનને પાછળથી મળેલી શિષ્યવૃત્તિ સાથે મળીને તેના અભ્યાસમાં મદદ કરવા માટે પૂરતી હતી. તેના હાથથી બનાવેલા ફાનસની વાત આખરે અન્ય શહેરોના દુકાનદારો સુધી પહોંચી, અને ધીમે ધીમે, આ દુકાન સસ્તી સુવિધા માટે નહીં, પરંતુ એક એવી કળા માટે જાણીતી બની, જેણે પોતાની શરતો પર જીવંત રહેવાનું પસંદ કર્યું હતું.''',
      questions: [
        PracticeQuestion(
          prompt: 'What difficult choice did Devraj face in the story?',
          options: [
            'Whether to accept a lucrative offer that meant giving up his family\'s handmade lantern craft.',
            'Whether to stop selling lanterns during Diwali.',
            'Whether to move to a different town.',
            'Whether to close the workshop and find another job.',
          ],
          correctIndex: 0,
          explanation: 'The passage describes a company offering to triple his income if he abandoned handmade lanterns for machine-made plastic ones — a conflict between money and preserving his craft.',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'Why did Devraj initially feel tempted to accept the company\'s full offer?',
          options: [
            'He no longer enjoyed making lanterns.',
            'The extra money would easily cover his sister\'s medical college fees.',
            'His grandfather had asked him to modernise the business.',
            'He wanted to travel and see other cities.',
          ],
          correctIndex: 1,
          explanation: 'The passage states "The money would easily pay for his sister\'s medical college fees, something Devraj had worried about for months."',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'What compromise did Devraj eventually choose?',
          options: [
            'He gave up lantern-making entirely and only worked for the company.',
            'He asked his mother to take over the workshop.',
            'He rejected the company completely and refused any new income.',
            'He kept making handmade lanterns and took a smaller contract painting brass fittings, using his real skill.',
          ],
          correctIndex: 3,
          explanation: 'The passage says he "would keep making his handmade lanterns, but he would also take a smaller, second contract to paint decorative brass fittings... work that used his real skill without erasing it."',
          difficulty: Difficulty.hard,
        ),
        PracticeQuestion(
          prompt: 'What did Devraj\'s mother mean when she said "a craft dies the moment no one is willing to sacrifice for it"?',
          options: [
            'Traditions survive only if someone is willing to make sacrifices to protect them.',
            'Crafts should always be abandoned for better-paying jobs.',
            'Sacrifice has nothing to do with keeping traditions alive.',
            'Only wealthy families can afford to preserve traditional crafts.',
          ],
          correctIndex: 0,
          explanation: 'Her statement suggests that traditions and crafts require someone to choose to preserve them, even at a cost, or they will disappear — which is exactly the dilemma Devraj faced.',
          difficulty: Difficulty.hard,
        ),
      ],
      glosses: [
        InlineGloss(word: 'inherited', meaningHi: 'विरासत में पाया', hiTransliteration: 'viraasat mein paaya', meaningGu: 'વારસામાં મળેલું', guTransliteration: 'varasama malelu'),
        InlineGloss(word: 'modest', meaningHi: 'सामान्य / मामूली', hiTransliteration: 'samanya / mamuli', meaningGu: 'સાધારણ / મામૂલી', guTransliteration: 'sadharan / mamuli'),
        InlineGloss(word: 'contract', meaningHi: 'अनुबंध / करार', hiTransliteration: 'anubandh / karaar', meaningGu: 'કરાર', guTransliteration: 'karar'),
        InlineGloss(word: 'abandon', meaningHi: 'छोड़ देना', hiTransliteration: 'chhod dena', meaningGu: 'છોડી દેવું', guTransliteration: 'chhodi devu'),
        InlineGloss(word: 'troubled', meaningHi: 'परेशान / चिंतित', hiTransliteration: 'pareshaan / chintit', meaningGu: 'પરેશાન / ચિંતિત', guTransliteration: 'pareshan / chintit'),
        InlineGloss(word: 'brushstrokes', meaningHi: 'कूँची के निशान / रंग लगाने का हुनर', hiTransliteration: 'kunchi ke nishaan / rang lagane ka hunar', meaningGu: 'પીંછીના નિશાન / રંગ લગાવવાની કળા', guTransliteration: 'pinchina nishan / rang lagavavani kala'),
        InlineGloss(word: 'sacrifice', meaningHi: 'त्याग / कुर्बानी', hiTransliteration: 'tyaag / qurbaani', meaningGu: 'બલિદાન / ત્યાગ', guTransliteration: 'balidan / tyag'),
        InlineGloss(word: 'decorative', meaningHi: 'सजावटी', hiTransliteration: 'sajaawati', meaningGu: 'સુશોભિત / સજાવટી', guTransliteration: 'sushobhit / sajavati'),
        InlineGloss(word: 'scholarship', meaningHi: 'छात्रवृत्ति', hiTransliteration: 'chhatravritti', meaningGu: 'શિષ્યવૃત્તિ', guTransliteration: 'shishyavrutti'),
        InlineGloss(word: 'convenience', meaningHi: 'सुविधा', hiTransliteration: 'suvidha', meaningGu: 'સગવડ / સુવિધા', guTransliteration: 'sagavad / suvidha'),
      ],
    ),
    ReadingPassage(
      id: 'class6_reading_dandi',
      title: 'A Letter from the Dandi March',
      emoji: '🧂',
      grade: 'Class 6',
      difficulty: Difficulty.hard,
      body: 'March 1930. Twelve-year-old Kanta sat by the window of her family\'s small home in a village along '
          'the route to Dandi, watching a long line of people walk past in the dusty afternoon heat. Her father had '
          'told her that morning that the marchers were following a man everyone called Bapu, who believed that '
          'even the making of salt, something so small and everyday, could become a way to challenge an unfair law. '
          'The British government had made it illegal for ordinary people to make or sell their own salt, forcing '
          'them to buy it instead, heavily taxed, from official stores.\n\n'
          'Kanta could hardly believe that salt, the very thing her mother sprinkled into the evening dal without '
          'a second thought, was at the centre of such a serious protest. Her father explained that the march was '
          'not really about salt alone; it was about showing that people could stand together peacefully against '
          'rules they considered unjust, without lifting a single weapon. Kanta watched as women from her own '
          'village joined the marchers carrying pots of water, while children ran alongside, offering wilted but '
          'welcome garlands of flowers.\n\n'
          'That evening, Kanta wrote in the small notebook her teacher had given her: "Today I saw history walk '
          'past our door. The marchers\' feet were covered in dust, and some limped from the long distance already '
          'travelled, yet no one turned back." She described how her own grandmother, usually too frail to leave '
          'her cot, had insisted on being carried to the roadside just to watch the marchers pass, saying she wanted '
          'to tell her grandchildren someday that she had witnessed it with her own eyes.\n\n'
          'Weeks later, news reached the village that the marchers had finally reached the sea at Dandi, where '
          'Bapu had picked up a handful of natural salt from the shore, breaking the law openly in front of thousands '
          'of witnesses and journalists. Kanta\'s father read the newspaper report aloud on their veranda, his voice '
          'thick with emotion. Kanta did not fully understand every detail of the law being broken, but she understood, '
          'perhaps for the first time, that a single small act, done together with courage and patience, could carry '
          'the weight of an entire nation\'s hope.',
      bodyHi: 'मार्च 1930। बारह वर्षीय कांता दांडी के रास्ते के एक गाँव में अपने परिवार के छोटे से घर की खिड़की के पास बैठी, धूल भरी दोपहर की गर्मी में लोगों की एक लंबी कतार को देख रही थी। उसके पिता ने उस सुबह उसे बताया था कि मार्च करने वाले लोग एक ऐसे व्यक्ति का पीछा कर रहे थे जिसे सब लोग बापू कहते थे, जिसका मानना ​​था कि नमक बनाना, जो इतना छोटा और रोजमर्रा का काम है, एक अनुचित कानून को चुनौती देने का एक तरीका बन सकता है। ब्रिटिश सरकार ने आम लोगों के लिए अपना नमक बनाना या बेचना गैरकानूनी बना दिया था, जिससे उन्हें आधिकारिक दुकानों से भारी कर लगाकर इसे खरीदने के लिए मजबूर किया गया था। उसके पिता ने समझाया कि मार्च वास्तव में केवल नमक के बारे में नहीं था; यह यह दिखाने के बारे में था कि लोग एक भी हथियार उठाए बिना उन नियमों के खिलाफ शांतिपूर्वक एक साथ खड़े हो सकते हैं जिन्हें वे अन्यायपूर्ण मानते हैं। कांता ने देखा कि उसके गांव की महिलाएं पानी के बर्तन लेकर मार्च करने वालों में शामिल हो गईं, जबकि बच्चे फूलों की मुरझाई लेकिन स्वागत योग्य मालाएं चढ़ाते हुए उनके साथ-साथ दौड़ रहे थे।\n\nउस शाम, कांता ने अपने शिक्षक द्वारा दी गई छोटी नोटबुक में लिखा: "आज मैंने इतिहास को अपने दरवाजे से गुजरते हुए देखा। मार्च करने वालों के पैर धूल से ढके हुए थे, और कुछ लोग पहले से ही लंबी दूरी तय करने के कारण लंगड़ा रहे थे, फिर भी कोई पीछे नहीं लौटा।" उन्होंने वर्णन किया कि कैसे उनकी अपनी दादी, जो आमतौर पर अपनी खाट छोड़ने में बहुत कमजोर होती थीं, ने जुलूस को गुजरते हुए देखने के लिए सड़क के किनारे ले जाने पर जोर दिया था, उन्होंने कहा था कि वह किसी दिन अपने पोते-पोतियों को बताना चाहती थीं कि उन्होंने इसे अपनी आंखों से देखा है।\n\nहफ्तों बाद, गांव में खबर पहुंची कि मार्च करने वाले आखिरकार दांडी में समुद्र तक पहुंच गए थे, जहां बापू ने किनारे से मुट्ठी भर प्राकृतिक नमक उठाया था, और हजारों गवाहों और पत्रकारों के सामने खुले तौर पर कानून तोड़ दिया था। कांता के पिता ने अपने बरामदे में अखबार की रिपोर्ट जोर से पढ़ी, उनकी आवाज भावुकता से भरी हुई थी। कांता को कानून तोड़े जाने की हर बात पूरी तरह से समझ में नहीं आई, लेकिन शायद पहली बार उसे समझ में आया कि साहस और धैर्य के साथ मिलकर किया गया एक छोटा सा कार्य, पूरे देश की आशा का भार उठा सकता है।',
      bodyGu: '''માર્ચ ૧૯૩૦. બાર વર્ષની કાંતા દાંડીના રસ્તે આવેલા એક ગામમાં પોતાના પરિવારના નાના ઘરની બારી પાસે બેઠી હતી અને ધૂળભરી બપોરની ગરમીમાં લોકોની લાંબી કતારને પસાર થતી જોઈ રહી હતી. તેના પિતાએ તે સવારે તેને જણાવ્યું હતું કે કૂચ કરનારા લોકો એક એવી વ્યક્તિની પાછળ જઈ રહ્યા છે જેને બધા બાપુ કહે છે. તેમનું માનવું હતું કે મીઠું બનાવવું, જે ખૂબ નાનું અને રોજિંદું કામ છે, તે પણ અન્યાયી કાયદાને પડકારવાનો એક રસ્તો બની શકે છે. બ્રિટિશ સરકારે સામાન્ય લોકો માટે પોતાનું મીઠું બનાવવું અથવા વેચવું ગેરકાયદેસર બનાવ્યું હતું, જેના કારણે તેમને સત્તાવાર દુકાનોમાંથી ભારે કર ચૂકવીને મીઠું ખરીદવાની ફરજ પડી હતી.

કાંતાને માનવામાં નહોતું આવતું કે જે મીઠું તેની માતા જરા પણ વિચાર્યા વિના સાંજની દાળમાં નાખે છે, તે આવા ગંભીર વિરોધના કેન્દ્રમાં છે. તેના પિતાએ સમજાવ્યું કે આ કૂચ ખરેખર માત્ર મીઠા વિશે નહોતી; આ કૂચ એ બતાવવા માટે હતી કે લોકો એકપણ હથિયાર ઉપાડ્યા વિના એવા નિયમો સામે શાંતિપૂર્વક એકસાથે ઊભા રહી શકે છે જેને તેઓ અન્યાયી માને છે. કાંતાએ જોયું કે તેના ગામની સ્ત્રીઓ પાણીના વાસણો લઈને કૂચ કરનારાઓ સાથે જોડાઈ હતી, જ્યારે બાળકો કરમાયેલી પણ આવકારદાયક ફૂલોની માળાઓ અર્પણ કરતા તેમની સાથે દોડી રહ્યા હતા.

તે સાંજે, કાંતાએ તેના શિક્ષકે આપેલી નાની નોટબુકમાં લખ્યું: "આજે મેં ઇતિહાસને અમારા દરવાજેથી પસાર થતો જોયો. કૂચ કરનારાઓના પગ ધૂળથી ખરડાયેલા હતા, અને કેટલાક લોકો લાંબુ અંતર કાપી ચૂક્યા હોવાથી લંગડાઈ રહ્યા હતા, છતાં કોઈ પાછું ફર્યું નહીં." તેણે વર્ણન કર્યું કે કેવી રીતે તેની પોતાની દાદી, જેઓ સામાન્ય રીતે પોતાનો ખાટલો છોડવા માટે ખૂબ નબળા હતા, તેમણે કૂચ કરનારાઓને પસાર થતા જોવા માટે રસ્તાના કિનારે લઈ જવાનો આગ્રહ રાખ્યો હતો. તેમણે કહ્યું હતું કે તેઓ કોઈક દિવસ તેમના પૌત્ર-પૌત્રીઓને કહેવા માંગે છે કે તેમણે આ બધું પોતાની આંખોથી જોયું છે.

અઠવાડિયાં પછી, ગામમાં સમાચાર પહોંચ્યા કે કૂચ કરનારાઓ આખરે દાંડીના દરિયાકિનારે પહોંચી ગયા છે, જ્યાં બાપુએ કિનારેથી ખોબો ભરીને કુદરતી મીઠું ઉપાડ્યું હતું અને હજારો સાક્ષીઓ તેમજ પત્રકારોની સામે ખુલ્લેઆમ કાયદો તોડ્યો હતો. કાંતાના પિતાએ તેમના વરંડામાં અખબારનો અહેવાલ મોટેથી વાંચ્યો, તેમનો અવાજ ભાવનાઓથી ભરાઈ ગયો હતો. કાંતાને કાયદો તોડવાની દરેક વિગત પૂરેપૂરી સમજાઈ ન હતી, પરંતુ કદાચ પહેલીવાર તેને સમજાયું કે હિંમત અને ધીરજ સાથે મળીને કરવામાં આવેલું એક નાનું કામ પણ આખા દેશની આશાનો ભાર ઉઠાવી શકે છે.''',
      questions: [
        PracticeQuestion(
          prompt: 'What law were the marchers protesting against?',
          options: [
            'A law about paying taxes on land.',
            'A law banning the growing of wheat.',
            'A law that made it illegal for ordinary people to make or sell their own salt.',
            'A law that stopped children from going to school.',
          ],
          correctIndex: 2,
          explanation: 'The passage explains "The British government had made it illegal for ordinary people to make or sell their own salt, forcing them to buy it instead, heavily taxed, from official stores."',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'According to Kanta\'s father, what was the deeper purpose of the march, beyond salt itself?',
          options: [
            'To show that people could protest peacefully together against unjust rules.',
            'To demand better roads for the village.',
            'To collect money for the marchers\' families.',
            'To celebrate a religious festival.',
          ],
          correctIndex: 0,
          explanation: 'The passage states the march "was not really about salt alone; it was about showing that people could stand together peacefully against rules they considered unjust, without lifting a single weapon."',
          difficulty: Difficulty.hard,
        ),
        PracticeQuestion(
          prompt: 'Why did Kanta\'s grandmother insist on being carried to the roadside?',
          options: [
            'She was looking for a lost family member among the marchers.',
            'She wanted to witness the historic march herself so she could tell her grandchildren about it later.',
            'She wanted fresh air after being unwell.',
            'She wanted to join the marchers permanently.',
          ],
          correctIndex: 1,
          explanation: 'The passage says her grandmother wanted "to tell her grandchildren someday that she had witnessed it with her own eyes."',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'What did Kanta come to understand by the end of the passage?',
          options: [
            'That the march had failed to achieve anything.',
            'That only adults could take part in important events.',
            'That a small, shared act of courage could represent the hopes of an entire nation.',
            'That salt was not an important resource for her village.',
          ],
          correctIndex: 2,
          explanation: 'The final line says she understood "that a single small act, done together with courage and patience, could carry the weight of an entire nation\'s hope."',
          difficulty: Difficulty.hard,
        ),
      ],
      glosses: [
        InlineGloss(word: 'marchers', meaningHi: 'यात्रा में शामिल लोग / पदयात्री', hiTransliteration: 'yatra mein shaamil log / padyatri', meaningGu: 'કૂચ કરનારાઓ / પદયાત્રીઓ', guTransliteration: 'kooch karnarao / padayatriyo'),
        InlineGloss(word: 'unjust', meaningHi: 'अन्यायपूर्ण', hiTransliteration: 'anyaaypurn', meaningGu: 'અન્યાયી', guTransliteration: 'anyaayi'),
        InlineGloss(word: 'protest', meaningHi: 'विरोध', hiTransliteration: 'virodh', meaningGu: 'વિરોધ', guTransliteration: 'virodh'),
        InlineGloss(word: 'garlands', meaningHi: 'माला / हार', hiTransliteration: 'maala / haar', meaningGu: 'ફૂલોની માળા / હાર', guTransliteration: 'phooloni maala / haar'),
        InlineGloss(word: 'frail', meaningHi: 'कमज़ोर / निर्बल', hiTransliteration: 'kamzor / nirbal', meaningGu: 'નબળું / અશક્ત', guTransliteration: 'nabalu / ashakt'),
        InlineGloss(word: 'witnessed', meaningHi: 'अपनी आँखों से देखा', hiTransliteration: 'apni aankhon se dekha', meaningGu: 'નજરે જોયું / સાક્ષી બન્યા', guTransliteration: 'najare joyu / saakshi banya'),
        InlineGloss(word: 'courage', meaningHi: 'साहस / हिम्मत', hiTransliteration: 'saahas / himmat', meaningGu: 'હિંમત / સાહસ', guTransliteration: 'himmat / saahas'),
        InlineGloss(word: 'patience', meaningHi: 'धैर्य / सब्र', hiTransliteration: 'dhairya / sabr', meaningGu: 'ધીરજ', guTransliteration: 'dhiraj'),
        InlineGloss(word: 'veranda', meaningHi: 'बरामदा', hiTransliteration: 'baramda', meaningGu: 'વરંડો / ઓટલો', guTransliteration: 'varando / otlo'),
        InlineGloss(word: 'journalists', meaningHi: 'पत्रकार', hiTransliteration: 'patrakaar', meaningGu: 'પત્રકારો', guTransliteration: 'patrakaro'),
        InlineGloss(word: 'taxed', meaningHi: 'जिस पर कर लगाया गया', hiTransliteration: 'jis par kar lagaya gaya', meaningGu: 'કર લાદેલો', guTransliteration: 'kar laadelo'),
      ],
    ),
    ReadingPassage(
      id: 'class6_reading_wetland',
      title: 'The Vanishing Wetland',
      emoji: '🦢',
      grade: 'Class 6',
      difficulty: Difficulty.medium,
      body: 'For as long as anyone in Bhavna\'s family could remember, flocks of migratory birds arrived at the '
          'wetland behind their farm every winter, flying thousands of kilometres from as far as Siberia to escape '
          'the freezing cold. Her grandfather often told stories of counting more than a hundred different bird '
          'species as a boy, their calls filling the misty mornings before sunrise. But this year, when Bhavna '
          'walked to the wetland with her binoculars, she noticed something troubling: the water level had dropped '
          'dramatically, leaving cracked, dry mud where reeds and shallow pools used to be.\n\n'
          'Concerned, Bhavna brought her observations to her school\'s environmental club, where her teacher, '
          'Kajal ma\'am, explained that wetlands like this one absorbed excess rainwater, filtered pollutants, and '
          'provided a resting ground for exhausted migratory birds after their long journeys. Without healthy '
          'wetlands, the birds might skip the region entirely, and nearby farms could lose the natural flood '
          'protection the wetland provided during heavy monsoon rains. He suspected that a new housing project '
          'upstream had diverted much of the water that once fed the wetland.\n\n'
          'Rather than simply worrying, Bhavna\'s club decided to investigate further. They collected water samples, '
          'photographed the shrinking wetland weekly, and interviewed elderly villagers, including Bhavna\'s '
          'grandfather, about how the wetland had changed over the decades. They compiled everything into a detailed '
          'report, complete with maps showing the water levels from ten years earlier compared to now, and presented '
          'it to the local municipal council.\n\n'
          'The council was initially hesitant to interfere with the housing project, citing the jobs and homes it '
          'would create. However, the students\' careful research, combined with the testimony of villagers who '
          'depended on the wetland for fishing and flood protection, eventually convinced officials to redesign the '
          'project\'s drainage system so that a portion of the water would continue flowing to the wetland. The '
          'following winter, though the flocks were smaller than in her grandfather\'s stories, Bhavna counted '
          'thirty-two species returning to the muddy banks, and she understood that protecting a home for wild '
          'creatures often meant becoming their patient, determined voice among humans.',
      bodyHi: 'जब तक भावना के परिवार में से किसी को भी याद है, हर सर्दियों में प्रवासी पक्षियों के झुंड जमा देने वाली ठंड से बचने के लिए साइबेरिया तक से हजारों किलोमीटर की दूरी तय करके उनके खेत के पीछे आर्द्रभूमि में आते थे। उनके दादाजी अक्सर एक लड़के के रूप में सौ से अधिक विभिन्न प्रजातियों के पक्षियों की गिनती की कहानियाँ सुनाते थे, उनकी आवाज़ें सूर्योदय से पहले धुंध भरी सुबह को भर देती थीं। लेकिन इस साल, जब भावना अपनी दूरबीन के साथ आर्द्रभूमि की ओर चली, तो उसने कुछ परेशान करने वाली बात देखी: पानी का स्तर नाटकीय रूप से गिर गया था, जहां नरकट और उथले पूल हुआ करते थे, वहां दरारें, सूखी मिट्टी रह गई थी।\n\nचिंतित, भावना अपने अवलोकनों को अपने स्कूल के पर्यावरण क्लब में ले गई, जहां उसकी शिक्षिका काजल मैडम ने बताया कि इस तरह की आर्द्रभूमि अतिरिक्त वर्षा जल को अवशोषित करती है, प्रदूषकों को फ़िल्टर करती है, और लंबे समय के बाद थके हुए प्रवासी पक्षियों के लिए एक विश्राम स्थल प्रदान करती है। यात्राएँ स्वस्थ आर्द्रभूमि के बिना, पक्षी इस क्षेत्र को पूरी तरह से छोड़ सकते हैं, और आस-पास के खेत भारी मानसूनी बारिश के दौरान आर्द्रभूमि द्वारा प्रदान की जाने वाली प्राकृतिक बाढ़ सुरक्षा खो सकते हैं। उन्हें संदेह था कि नदी के ऊपर एक नई आवासीय परियोजना ने उस पानी का अधिकांश हिस्सा मोड़ दिया है जो कभी आर्द्रभूमि को मिलता था।\n\nसिर्फ चिंता करने के बजाय, भावना के क्लब ने आगे की जांच करने का फैसला किया। उन्होंने पानी के नमूने एकत्र किए, सिकुड़ती हुई आर्द्रभूमि की साप्ताहिक तस्वीरें खींचीं और भावना के दादा सहित बुजुर्ग ग्रामीणों का साक्षात्कार लिया कि दशकों में आर्द्रभूमि कैसे बदल गई है। उन्होंने सब कुछ एक विस्तृत रिपोर्ट में संकलित किया, जिसमें अब की तुलना में दस साल पहले के जल स्तर को दर्शाने वाले मानचित्र शामिल थे, और इसे स्थानीय नगरपालिका परिषद को प्रस्तुत किया।\n\nपरिषद शुरू में नौकरियों और घरों का हवाला देते हुए आवास परियोजना में हस्तक्षेप करने से झिझक रही थी। हालाँकि, मछली पकड़ने और बाढ़ से सुरक्षा के लिए आर्द्रभूमि पर निर्भर रहने वाले ग्रामीणों की गवाही के साथ छात्रों के सावधानीपूर्वक शोध ने अंततः अधिकारियों को परियोजना की जल निकासी प्रणाली को फिर से डिजाइन करने के लिए मना लिया ताकि पानी का एक हिस्सा आर्द्रभूमि में बहता रहे। अगली सर्दियों में, हालांकि झुंड उसके दादाजी की कहानियों की तुलना में छोटे थे, भावना ने बत्तीस प्रजातियों की गिनती की जो कीचड़ भरे तटों पर लौट रही थीं, और वह समझ गई कि जंगली प्राणियों के लिए घर की रक्षा करने का मतलब अक्सर मनुष्यों के बीच उनकी धैर्यवान, दृढ़ आवाज बनना है।',
      bodyGu: '''જ્યાં સુધી ભાવનાના પરિવારમાં કોઈને પણ યાદ છે, દર શિયાળામાં પ્રવાસી પક્ષીઓના ટોળા જમાવી દે તેવી ઠંડીથી બચવા માટે સાઇબિરીયાથી હજારો કિલોમીટરની મુસાફરી કરીને તેમના ખેતરની પાછળની આર્દ્રભૂમિ (વેટલેન્ડ) માં આવતા હતા. તેના દાદાજી વારંવાર એક છોકરા તરીકે સો કરતાં વધુ વિવિધ પ્રજાતિઓના પક્ષીઓની ગણતરી કરવાની વાર્તાઓ સંભળાવતા હતા, તેઓનો અવાજ સૂર્યોદય પહેલાંની ધુમ્મસવાળી સવારને ભરી દેતો હતો. પરંતુ આ વર્ષે, જ્યારે ભાવના તેના બાયનોક્યુલર (દૂરબીન) સાથે આર્દ્રભૂમિ તરફ ચાલી, ત્યારે તેણે એક ચિંતાજનક બાબત જોઈ: પાણીનું સ્તર નાટકીય રીતે નીચે ગયું હતું, જ્યાં અગાઉ બરુ (રીડ્સ) અને છીછરા ખાબોચિયા હતા, ત્યાં હવે માત્ર તિરાડોવાળી, સૂકી માટી રહી ગઈ હતી.

ચિંતિત થઈને, ભાવનાએ તેના અવલોકનો તેની શાળાના પર્યાવરણ ક્લબ સમક્ષ રજૂ કર્યા, જ્યાં તેના શિક્ષક કાજલ મેડમે સમજાવ્યું કે આવી આર્દ્રભૂમિ વરસાદના વધારાના પાણીને શોષી લે છે, પ્રદૂષકોને ફિલ્ટર કરે છે અને લાંબી મુસાફરી પછી થાકેલા પ્રવાસી પક્ષીઓને આરામ કરવાનું સ્થળ પૂરું પાડે છે. સ્વસ્થ આર્દ્રભૂમિ વિના, પક્ષીઓ આ વિસ્તારને સંપૂર્ણપણે છોડી શકે છે, અને નજીકના ખેતરો ભારે ચોમાસાના વરસાદ દરમિયાન આર્દ્રભૂમિ દ્વારા પૂરી પાડવામાં આવતી કુદરતી પૂર સુરક્ષા ગુમાવી શકે છે. તેમને શંકા હતી કે નદીના ઉપરવાસમાં એક નવા આવાસ પ્રોજેક્ટ દ્વારા મોટા ભાગનું પાણી વાળી દેવામાં આવ્યું હતું જે પહેલાં આર્દ્રભૂમિને મળતું હતું.

ફક્ત ચિંતા કરવાને બદલે, ભાવનાની ક્લબે આગળ તપાસ કરવાનું નક્કી કર્યું. તેઓએ પાણીના નમૂનાઓ એકત્રિત કર્યા, સંકોચાઈ રહેલી આર્દ્રભૂમિના સાપ્તાહિક ફોટોગ્રાફ લીધા અને ભાવનાના દાદા સહિત વૃદ્ધ ગ્રામજનોના ઇન્ટરવ્યુ લીધા કે દાયકાઓમાં આર્દ્રભૂમિ કેવી રીતે બદલાઈ ગઈ છે. તેઓએ આ બધી માહિતીને એક વિગતવાર રિપોર્ટમાં સંકલિત કરી, જેમાં દસ વર્ષ પહેલાંના પાણીના સ્તરની સરખામણી હાલના સ્તર સાથે દર્શાવતા નકશા સામેલ હતા, અને તેને સ્થાનિક મ્યુનિસિપલ કાઉન્સિલ સમક્ષ રજૂ કર્યો.

કાઉન્સિલ શરૂઆતમાં નોકરીઓ અને ઘરોનું કારણ આપીને હાઉસિંગ પ્રોજેક્ટમાં દખલ કરતા અચકાતી હતી. જોકે, માછીમારી અને પૂર સુરક્ષા માટે આર્દ્રભૂમિ પર નિર્ભર ગ્રામજનોની જુબાની સાથે વિદ્યાર્થીઓના કાળજીપૂર્વક સંશોધને આખરે અધિકારીઓને પ્રોજેક્ટની ડ્રેનેજ સિસ્ટમને ફરીથી ડિઝાઇન કરવા મનાવી લીધા, જેથી પાણીનો એક ભાગ આર્દ્રભૂમિમાં વહેતો રહે. આવતા શિયાળામાં, જોકે તેના દાદાજીની વાર્તાઓની તુલનામાં ટોળાં નાના હતા, ભાવનાએ કાદવવાળા કાંઠા પર પાછા ફરતી બત્રીસ પ્રજાતિઓની ગણતરી કરી, અને તે સમજી ગઈ કે જંગલી પ્રાણીઓ માટેના ઘરનું રક્ષણ કરવાનો અર્થ ઘણીવાર મનુષ્યો વચ્ચે તેમનો ધીરજવાન, દૃઢ અવાજ બનવાનો છે.''',
      questions: [
        PracticeQuestion(
          prompt: 'What change did Bhavna notice in the wetland compared to previous years?',
          options: [
            'New species of fish had appeared in the water.',
            'The wetland had been fenced off completely.',
            'The water level had dropped dramatically, leaving cracked, dry mud.',
            'The wetland had grown much larger than before.',
          ],
          correctIndex: 2,
          explanation: 'The passage describes her noticing "the water level had dropped dramatically, leaving cracked, dry mud where reeds and shallow pools used to be."',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'According to Kajal ma\'am, what important roles do wetlands play?',
          options: [
            'They have no real effect on nearby farms.',
            'They absorb excess rainwater, filter pollutants, and give migratory birds a place to rest.',
            'They only provide scenery for tourists.',
            'They are used only for growing crops.',
          ],
          correctIndex: 1,
          explanation: 'The passage says wetlands "absorbed excess rainwater, filtered pollutants, and provided a resting ground for exhausted migratory birds after their long journeys."',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'What action did Bhavna\'s environmental club take to address the problem?',
          options: [
            'They released more birds into the wetland themselves.',
            'They ignored the issue since it was not their responsibility.',
            'They asked the government to shut down the housing project entirely.',
            'They collected data, interviewed villagers, and presented a detailed report to the municipal council.',
          ],
          correctIndex: 3,
          explanation: 'The passage describes them collecting "water samples, photographed the shrinking wetland weekly, and interviewed elderly villagers... compiled everything into a detailed report... presented it to the local municipal council."',
          difficulty: Difficulty.hard,
        ),
        PracticeQuestion(
          prompt: 'What was the eventual outcome of the students\' efforts?',
          options: [
            'The housing project was cancelled completely.',
            'The council redesigned the drainage system so some water still reached the wetland, and birds returned the following winter.',
            'Nothing changed, and the birds stopped coming entirely.',
            'The council ignored the report and built over the wetland.',
          ],
          correctIndex: 1,
          explanation: 'The passage states officials were convinced "to redesign the project\'s drainage system so that a portion of the water would continue flowing to the wetland," and birds returned the next winter.',
          difficulty: Difficulty.medium,
        ),
      ],
      glosses: [
        InlineGloss(word: 'migratory', meaningHi: 'प्रवासी (मौसम के अनुसार उड़ने वाले)', hiTransliteration: 'pravasi (mausam ke anusaar udne wale)', meaningGu: 'પ્રવાસી (ઋતુ અનુસાર ઉડનારા)', guTransliteration: 'pravasi (rutu anusar udnara)'),
        InlineGloss(word: 'species', meaningHi: 'प्रजाति', hiTransliteration: 'prajaati', meaningGu: 'પ્રજાતિ', guTransliteration: 'prajati'),
        InlineGloss(word: 'dramatically', meaningHi: 'बहुत ज़्यादा / नाटकीय रूप से', hiTransliteration: 'bahut zyada / naatkiya roop se', meaningGu: 'નાટકીય રીતે / ખૂબ જ વધારે', guTransliteration: 'natkiya rite / khub ja vadhare'),
        InlineGloss(word: 'absorbed', meaningHi: 'सोख लिया', hiTransliteration: 'sokh liya', meaningGu: 'શોષી લીધું', guTransliteration: 'shoshi lidhu'),
        InlineGloss(word: 'pollutants', meaningHi: 'प्रदूषक तत्व', hiTransliteration: 'pradushak tatva', meaningGu: 'પ્રદૂષક તત્વો', guTransliteration: 'pradushak tatvo'),
        InlineGloss(word: 'diverted', meaningHi: 'दिशा बदल दी', hiTransliteration: 'disha badal di', meaningGu: 'દિશા બદલી નાખી / વાળી દીધું', guTransliteration: 'disha badli nakhi / vali didhu'),
        InlineGloss(word: 'testimony', meaningHi: 'गवाही / बयान', hiTransliteration: 'gawahi / bayaan', meaningGu: 'જુબાની / નિવેદન', guTransliteration: 'jubani / nivedan'),
        InlineGloss(word: 'drainage', meaningHi: 'पानी की निकासी', hiTransliteration: 'paani ki nikaasi', meaningGu: 'પાણીના નિકાલની વ્યવસ્થા / ગટર', guTransliteration: 'panina nikalni vyavastha / gatar'),
        InlineGloss(word: 'hesitant', meaningHi: 'हिचकिचाने वाला', hiTransliteration: 'hichkichaane wala', meaningGu: 'અચકાતો / ખચકાટ અનુભવતો', guTransliteration: 'achkato / khachkat anubhavto'),
        InlineGloss(word: 'municipal', meaningHi: 'नगर पालिका से जुड़ा', hiTransliteration: 'nagar palika se juda', meaningGu: 'નગરપાલિકાને લગતું', guTransliteration: 'nagarpalikane lagtu'),
      ],
    ),
    ReadingPassage(
      id: 'class6_reading_robotics',
      title: 'The Robot That Learned to Listen',
      emoji: '🤖',
      grade: 'Class 6',
      difficulty: Difficulty.medium,
      body: 'Aryan had always been the quietest boy in his class, more comfortable with circuit boards and code '
          'than with conversation. For the district science fair, he decided to build a robot that could help his '
          'grandmother, who was slowly losing her hearing and often missed the doorbell or the whistle of the '
          'pressure cooker. Most robotics projects at the fair involved robots that could walk or pick up objects, '
          'but Aryan wanted his invention to solve a problem he saw every single day at home.\n\n'
          'For three months, Aryan worked in the corner of his family\'s small living room, surrounded by wires, '
          'a discarded speaker, and a second-hand microcontroller his father had helped him order online. He '
          'programmed the device to recognise the specific sound patterns of the doorbell, the cooker whistle, and '
          'a knock on the door, then flash a bright light and vibrate a small pad his grandmother could keep in her '
          'pocket. The hardest part was not the coding itself, but teaching the device to ignore ordinary household '
          'noise, like the television or his little cousin\'s laughter, so it would not trigger false alerts all day '
          'long.\n\n'
          'When Aryan finally tested the finished device, it failed twice in a row, buzzing wildly at the sound of '
          'a passing motorbike outside. Frustrated but unwilling to give up, he stayed up late adjusting the '
          'sensitivity settings, comparing sound graphs on his father\'s old laptop until the device could reliably '
          'tell the difference between a doorbell and traffic noise. On the third attempt, when his grandmother '
          'rang a small bell from the next room, the pad in his pocket buzzed instantly, and she looked up, smiling, '
          'before he had even said a word.\n\n'
          'At the science fair, judges were less impressed by fancy movements and more moved by Aryan\'s explanation '
          'of why he built the device and how it had already changed his grandmother\'s daily life. He did not win '
          'the top prize that year, but a representative from a local assistive technology company approached him '
          'afterward, asking whether he would be interested in helping design similar devices for other elderly '
          'people in the community. Aryan realised that the best technology was not always the most complicated, '
          'but the kind built by paying close attention to a real person\'s needs.',
      bodyHi: 'आर्यन हमेशा अपनी कक्षा का सबसे शांत लड़का था, बातचीत की तुलना में सर्किट बोर्ड और कोड के साथ अधिक सहज था। जिला विज्ञान मेले के लिए, उन्होंने एक रोबोट बनाने का फैसला किया जो उनकी दादी की मदद कर सके, जो धीरे-धीरे अपनी सुनने की शक्ति खो रही थीं और अक्सर दरवाजे की घंटी या प्रेशर कुकर की सीटी नहीं बजा पाती थीं। मेले में अधिकांश रोबोटिक्स परियोजनाओं में ऐसे रोबोट शामिल थे जो चल सकते थे या वस्तुओं को उठा सकते थे, लेकिन आर्यन चाहता था कि उसका आविष्कार उस समस्या का समाधान हो जो वह घर पर हर दिन देखता था।\n\nतीन महीने तक, आर्यन ने अपने परिवार के छोटे से रहने वाले कमरे के कोने में तारों से घिरा हुआ काम किया, एक बेकार स्पीकर और एक सेकेंड-हैंड माइक्रोकंट्रोलर जिसे उसके पिता ने ऑनलाइन ऑर्डर करने में मदद की थी। उन्होंने डिवाइस को दरवाजे की घंटी, कुकर की सीटी और दरवाजे पर दस्तक के विशिष्ट ध्वनि पैटर्न को पहचानने के लिए प्रोग्राम किया, फिर एक चमकदार रोशनी चमकाई और एक छोटे से पैड को कंपन किया जिसे उनकी दादी अपनी जेब में रख सकती थीं। सबसे कठिन हिस्सा खुद कोडिंग नहीं था, बल्कि डिवाइस को टेलीविजन या उसके छोटे चचेरे भाई की हंसी जैसे सामान्य घरेलू शोर को नजरअंदाज करना सिखाना था, ताकि यह पूरे दिन गलत अलर्ट ट्रिगर न करे।\n\nजब आर्यन ने अंततः तैयार डिवाइस का परीक्षण किया, तो यह लगातार दो बार विफल रहा, बाहर से गुजरती मोटरसाइकिल की आवाज पर बेतहाशा गूंज रहा था। निराश लेकिन हार मानने को तैयार नहीं, वह संवेदनशीलता सेटिंग्स को समायोजित करने के लिए देर तक जागता रहा, अपने पिता के पुराने लैपटॉप पर ध्वनि ग्राफ़ की तुलना करता रहा जब तक कि डिवाइस विश्वसनीय रूप से दरवाजे की घंटी और ट्रैफ़िक शोर के बीच अंतर नहीं बता सका। तीसरे प्रयास में, जब उसकी दादी ने अगले कमरे से एक छोटी सी घंटी बजाई, तो उसकी जेब में रखा पैड तुरंत बज उठा, और उसने मुस्कुराते हुए ऊपर देखा, इससे पहले कि वह एक शब्द भी कहता।\n\nविज्ञान मेले में, जज फैंसी गतिविधियों से कम प्रभावित हुए और आर्यन के स्पष्टीकरण से अधिक प्रभावित हुए कि उसने यह उपकरण क्यों बनाया और इसने उसकी दादी के दैनिक जीवन को कैसे बदल दिया है। उन्होंने उस वर्ष शीर्ष पुरस्कार नहीं जीता, लेकिन एक स्थानीय सहायक प्रौद्योगिकी कंपनी के एक प्रतिनिधि ने बाद में उनसे संपर्क किया और पूछा कि क्या वह समुदाय के अन्य बुजुर्ग लोगों के लिए समान उपकरणों को डिजाइन करने में मदद करने में रुचि रखेंगे। आर्यन को एहसास हुआ कि सबसे अच्छी तकनीक हमेशा सबसे जटिल नहीं होती, बल्कि वास्तविक व्यक्ति की जरूरतों पर बारीकी से ध्यान देकर बनाई गई होती है।',
      bodyGu: '''આર્યન હંમેશા તેના વર્ગનો સૌથી શાંત છોકરો હતો, તે વાતચીત કરતાં સર્કિટ બોર્ડ અને કોડ સાથે વધુ સહજ હતો. જિલ્લા વિજ્ઞાન મેળા માટે, તેણે એક રોબોટ બનાવવાનું નક્કી કર્યું જે તેની દાદીને મદદ કરી શકે, જેઓ ધીમે ધીમે તેમની સાંભળવાની શક્તિ ગુમાવી રહ્યા હતા અને ઘણીવાર દરવાજાની ઘંટડી અથવા પ્રેશર કૂકરની સીટી સાંભળી શકતા ન હતા. મેળામાં મોટાભાગના રોબોટિક્સ પ્રોજેક્ટ્સમાં એવા રોબોટ્સ સામેલ હતા જે ચાલી શકતા હતા અથવા વસ્તુઓ ઉપાડી શકતા હતા, પરંતુ આર્યન ઇચ્છતો હતો કે તેની શોધ તે સમસ્યાનો ઉકેલ બને જે તે દરરોજ ઘરે જોતો હતો.

ત્રણ મહિના સુધી, આર્યને તેના પરિવારના નાના લિવિંગ રૂમના ખૂણામાં કામ કર્યું, વાયરોથી ઘેરાયેલો, એક નકામું સ્પીકર અને એક સેકન્ડ-હેન્ડ માઇક્રોકન્ટ્રોલર જેને તેના પિતાએ ઓનલાઇન ઓર્ડર કરવામાં મદદ કરી હતી. તેણે ડિવાઇસને દરવાજાની ઘંટડી, કૂકરની સીટી અને દરવાજા પરની દસ્તકના ચોક્કસ ધ્વનિ પેટર્નને ઓળખવા માટે પ્રોગ્રામ કર્યું, પછી એક તેજસ્વી પ્રકાશ ચમકાવ્યો અને એક નાના પેડને વાઇબ્રેટ કર્યું જેને તેની દાદી તેમના ખિસ્સામાં રાખી શકતા હતા. સૌથી મુશ્કેલ ભાગ માત્ર કોડિંગ ન હતો, પરંતુ ડિવાઇસને ટેલિવિઝન અથવા તેના નાના પિતરાઈ ભાઈના હાસ્ય જેવા સામાન્ય ઘરેલુ અવાજને અવગણતા શીખવવું હતું, જેથી તે આખો દિવસ ખોટા એલર્ટ્સ ટ્રિગર ન કરે.

જ્યારે આર્યને આખરે તૈયાર ડિવાઇસનું પરીક્ષણ કર્યું, ત્યારે તે સળંગ બે વાર નિષ્ફળ ગયું, બહારથી પસાર થતી મોટરસાઇકલના અવાજ પર જંગલી રીતે ગુંજી રહ્યું હતું. નિરાશ પરંતુ હાર ન માનવા માટે તૈયાર, તેણે સંવેદનશીલતા સેટિંગ્સને સમાયોજિત કરવા માટે મોડે સુધી જાગ્યો, તેના પિતાના જૂના લેપટોપ પર ધ્વનિ ગ્રાફની સરખામણી કરી જ્યાં સુધી ડિવાઇસ વિશ્વસનીય રીતે દરવાજાની ઘંટડી અને ટ્રાફિકના અવાજ વચ્ચેનો તફાવત ન જણાવી શકે. ત્રીજા પ્રયાસમાં, જ્યારે તેની દાદીએ બાજુના રૂમમાંથી એક નાની ઘંટડી વગાડી, ત્યારે તેના ખિસ્સામાં રહેલું પેડ તરત જ વાગી ઉઠ્યું, અને તેણીએ સ્મિત સાથે ઉપર જોયું, તે એક શબ્દ પણ બોલે તે પહેલાં.

વિજ્ઞાન મેળામાં, નિર્ણાયકો ફેન્સી હલનચલનથી ઓછા પ્રભાવિત થયા હતા અને આર્યનની સમજૂતીથી વધુ પ્રભાવિત થયા હતા કે તેણે આ ઉપકરણ શા માટે બનાવ્યું અને તેણે તેની દાદીના રોજિંદા જીવનમાં કેવી રીતે બદલાવ લાવ્યો છે. તેણે તે વર્ષે ટોચનો પુરસ્કાર જીત્યો ન હતો, પરંતુ એક સ્થાનિક સહાયક તકનીકી કંપનીના પ્રતિનિધિએ પછીથી તેનો સંપર્ક કર્યો અને પૂછ્યું કે શું તે સમુદાયના અન્ય વૃદ્ધ લોકો માટે સમાન ઉપકરણો ડિઝાઇન કરવામાં મદદ કરવામાં રસ ધરાવશે. આર્યનને અહેસાસ થયો કે શ્રેષ્ઠ ટેકનોલોજી હંમેશા સૌથી જટિલ હોતી નથી, પરંતુ વાસ્તવિક વ્યક્તિની જરૂરિયાતો પર પૂરતું ધ્યાન આપીને બનાવવામાં આવે છે.''',
      questions: [
        PracticeQuestion(
          prompt: 'What problem did Aryan want his robot to solve?',
          options: [
            'Helping robots walk faster in competitions.',
            'Translating spoken language into text.',
            'Cleaning the house automatically.',
            'Alerting his grandmother, who was losing her hearing, to sounds like the doorbell and cooker whistle.',
          ],
          correctIndex: 3,
          explanation: 'The passage says Aryan built the device to help his grandmother, who "was slowly losing her hearing and often missed the doorbell or the whistle of the pressure cooker."',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'What was the hardest part of building the device, according to the passage?',
          options: [
            'Getting permission to enter the science fair.',
            'Convincing his grandmother to wear the vibrating pad.',
            'Finding a discarded speaker to use.',
            'Teaching the device to ignore ordinary household noise so it would not give false alerts.',
          ],
          correctIndex: 3,
          explanation: 'The passage states "the hardest part was not the coding itself, but teaching the device to ignore ordinary household noise... so it would not trigger false alerts all day long."',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'How did Aryan respond after the device failed during testing?',
          options: [
            'He gave up on the project completely.',
            'He blamed his father\'s old laptop for the failure.',
            'He stayed up late adjusting the sensitivity settings until the device worked reliably.',
            'He entered a different invention into the science fair instead.',
          ],
          correctIndex: 2,
          explanation: 'The passage says he "stayed up late adjusting the sensitivity settings, comparing sound graphs... until the device could reliably tell the difference between a doorbell and traffic noise."',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'What lesson did Aryan take away from his experience at the science fair?',
          options: [
            'Winning first prize matters more than solving a real problem.',
            'Assistive technology companies are not interested in student projects.',
            'The best technology often comes from paying close attention to a real person\'s needs, not complexity.',
            'Only complicated inventions impress judges.',
          ],
          correctIndex: 2,
          explanation: 'The final line states Aryan "realised that the best technology was not always the most complicated, but the kind built by paying close attention to a real person\'s needs."',
          difficulty: Difficulty.hard,
        ),
      ],
      glosses: [
        InlineGloss(word: 'microcontroller', meaningHi: 'छोटा कंप्यूटर चिप जो उपकरण को नियंत्रित करता है', hiTransliteration: 'chhota computer chip jo upkaran ko niyantrit karta hai', meaningGu: 'નાની કમ્પ્યુટર ચિપ જે ઉપકરણને નિયંત્રિત કરે છે', guTransliteration: 'naani computer chip je upkaranne niyantrit kare chhe'),
        InlineGloss(word: 'recognise', meaningHi: 'पहचानना', hiTransliteration: 'pehchaanna', meaningGu: 'ઓળખવું', guTransliteration: 'olakhvu'),
        InlineGloss(word: 'trigger', meaningHi: 'चालू कर देना / भड़का देना', hiTransliteration: 'chaalu kar dena / bhadka dena', meaningGu: 'ચાલુ કરી દેવું / ભડકાવવું', guTransliteration: 'chaalu kari devu / bhadkaavvu'),
        InlineGloss(word: 'sensitivity', meaningHi: 'संवेदनशीलता', hiTransliteration: 'sanvedansheelta', meaningGu: 'સંવેદનશીલતા', guTransliteration: 'samvedanshilta'),
        InlineGloss(word: 'assistive', meaningHi: 'मदद करने वाली (तकनीक)', hiTransliteration: 'madad karne wali (takneek)', meaningGu: 'મદદ કરવાવાળી (ટેકનોલોજી)', guTransliteration: 'madad karvavali (technology)'),
        InlineGloss(word: 'frustrated', meaningHi: 'निराश / खीझा हुआ', hiTransliteration: 'niraash / kheejha hua', meaningGu: 'નિરાશ / હતાશ', guTransliteration: 'niraash / hataash'),
        InlineGloss(word: 'invention', meaningHi: 'आविष्कार', hiTransliteration: 'aavishkaar', meaningGu: 'શોધ', guTransliteration: 'shodh'),
        InlineGloss(word: 'reliably', meaningHi: 'भरोसेमंद तरीके से', hiTransliteration: 'bharosemand tareeke se', meaningGu: 'ભરોસાપાત્ર રીતે', guTransliteration: 'bharosapatra rite'),
        InlineGloss(word: 'elderly', meaningHi: 'बुज़ुर्ग', hiTransliteration: 'buzurg', meaningGu: 'વૃદ્ધ', guTransliteration: 'vruddh'),
        InlineGloss(word: 'complicated', meaningHi: 'जटिल / पेचीदा', hiTransliteration: 'jatil / pechida', meaningGu: 'જટિલ / અઘરું', guTransliteration: 'jatil / agharu'),
      ],
    ),
    ReadingPassage(
      id: 'class6_reading_marathon',
      title: 'The Last Kilometre',
      emoji: '🏃',
      grade: 'Class 6',
      difficulty: Difficulty.medium,
      body: 'Meera had trained for the state junior marathon for nearly a year, running before sunrise along the '
          'dusty road outside her village so that she could finish her chores before school began. Her coach, a '
          'retired athlete named Govind sir, often reminded her that marathons were not won in the final sprint '
          'but in the quiet, disciplined mornings when nobody else was watching. Meera believed him completely, '
          'until the day of the race itself, when everything she had prepared for seemed to fall apart at once.\n\n'
          'At the ten-kilometre mark, Meera felt a sharp pain shoot through her ankle after stepping awkwardly on a '
          'loose stone. She slowed to a limp, watching runner after runner overtake her, including two girls from '
          'her own school whom she had always finished ahead of during practice. A part of her wanted to stop right '
          'there, to sit by the roadside and accept that her year of early mornings had been wasted on a single bad '
          'step. Instead, she remembered Govind sir\'s words about mornings nobody else saw, and told herself that '
          'giving up now would erase all of that quiet effort in an instant.\n\n'
          'She adjusted her stride, shifting more weight onto her uninjured leg, and continued at a slower, careful '
          'pace, wincing with almost every step. Spectators along the route, noticing her obvious pain, called out '
          'encouragement, and a volunteer offered to bandage her ankle at a water station without asking her to '
          'withdraw from the race. Meera accepted the bandage but refused to stop, reasoning that finishing, even '
          'slowly, meant more to her than any position on a results sheet.\n\n'
          'She crossed the finish line nearly twenty minutes after the winner, in a position far lower than she had '
          'once dreamed of, her ankle swollen and her legs trembling with exhaustion. Yet the loudest cheer she '
          'received that day came not for her placement, but from Govind sir, who told her afterward that the '
          'girl who finished the race on an injured ankle had learned something no trophy could teach: that '
          'finishing what you start, even imperfectly, is its own kind of victory.',
      bodyHi: 'मीरा ने राज्य जूनियर मैराथन के लिए लगभग एक साल तक प्रशिक्षण लिया था, वह अपने गाँव के बाहर धूल भरी सड़क पर सूर्योदय से पहले दौड़ती थी ताकि वह स्कूल शुरू होने से पहले अपना काम पूरा कर सके। उनके कोच, गोविंद सर नाम के एक सेवानिवृत्त एथलीट, अक्सर उन्हें याद दिलाते थे कि मैराथन अंतिम स्प्रिंट में नहीं बल्कि शांत, अनुशासित सुबह में जीते जाते हैं जब कोई और नहीं देख रहा होता है। मीरा ने उस पर पूरा विश्वास किया, दौड़ के दिन तक, जब उसने जो कुछ भी तैयार किया था वह एक ही बार में बिखर गया।\n\nदस किलोमीटर के निशान पर, एक ढीले पत्थर पर अजीब तरह से कदम रखने के बाद, मीरा को अपने टखने में तेज दर्द महसूस हुआ। एक के बाद एक धावकों को अपने से आगे निकलते देख वह धीरे-धीरे लंगड़ाने लगी, जिसमें उसके अपने स्कूल की दो लड़कियाँ भी शामिल थीं, जिनसे वह अभ्यास के दौरान हमेशा आगे रहती थी। उसका एक हिस्सा वहीं रुकना चाहता था, सड़क के किनारे बैठकर यह स्वीकार करना चाहता था कि उसकी शुरुआती सुबह का साल एक बुरे कदम के कारण बर्बाद हो गया। इसके बजाय, उसे सुबह के बारे में गोविंद सर के शब्द याद आए जो किसी और ने नहीं देखे थे, और उसने खुद से कहा कि अब हार मानने से उस शांत प्रयास को एक पल में मिटा दिया जाएगा।\n\nउसने अपने कदमों को समायोजित किया, अपने बिना चोट वाले पैर पर अधिक वजन डाला, और धीमी, सावधान गति से चलती रही, लगभग हर कदम पर लड़खड़ाती रही। रास्ते में मौजूद दर्शकों ने, उसके स्पष्ट दर्द को देखकर, उसे प्रोत्साहित किया और एक स्वयंसेवक ने उसे दौड़ से हटने के लिए कहे बिना एक जल स्टेशन पर उसके टखने पर पट्टी बाँधने की पेशकश की। मीरा ने पट्टी बांधना स्वीकार कर लिया, लेकिन रुकने से इनकार कर दिया, यह तर्क देते हुए कि फिनिशिंग, भले ही धीरे-धीरे, उसके लिए परिणाम शीट पर किसी भी स्थिति से अधिक मायने रखती है।\n\nविजेता के लगभग बीस मिनट बाद उसने फिनिश लाइन को पार कर लिया, जो कि उसने कभी सपने में भी नहीं सोचा था, उसके टखने सूज गए थे और उसके पैर थकावट से कांप रहे थे। फिर भी उस दिन उसे जो सबसे जोरदार उत्साह मिला, वह उसके स्थान के लिए नहीं, बल्कि गोविंद सर से आया, जिन्होंने बाद में उसे बताया कि जिस लड़की ने घायल टखने पर दौड़ पूरी की थी, उसने कुछ ऐसा सीखा है जो कोई ट्रॉफी नहीं सिखा सकती: कि आप जो शुरू करते हैं, उसे पूरा करना, भले ही अपूर्ण तरीके से, अपनी तरह की जीत है।',
      bodyGu: '''મીરાએ રાજ્ય જુનિયર મેરેથોન માટે લગભગ એક વર્ષ સુધી તાલીમ લીધી હતી, તે શાળા શરૂ થતાં પહેલાં પોતાનું કામ પૂરું કરી શકે તે માટે સૂર્યોદય પહેલાં પોતાના ગામની બહાર ધૂળવાળા રસ્તા પર દોડતી હતી. તેના કોચ, ગોવિંદ સર નામના એક નિવૃત્ત એથલીટ, વારંવાર તેને યાદ અપાવતા હતા કે મેરેથોન અંતિમ સ્પ્રિન્ટમાં નહીં પરંતુ શાંત, શિસ્તબદ્ધ સવારમાં જીતવામાં આવે છે જ્યારે કોઈ અન્ય જોઈ રહ્યું હોતું નથી. મીરાએ તેના પર પૂરો વિશ્વાસ કર્યો, દોડના દિવસ સુધી, જ્યારે તેણે જે કંઈ પણ તૈયાર કર્યું હતું તે બધું એક જ વારમાં વિખેરાઈ ગયું.

દસ કિલોમીટરના નિશાન પર, એક છૂટા પથ્થર પર અજીબ રીતે પગ મૂક્યા પછી, મીરાને તેની ઘૂંટીમાં સખત દુખાવો અનુભવાયો. એક પછી એક દોડવીરોને પોતાનાથી આગળ નીકળતા જોઈને તે ધીમે ધીમે લંગડાવા લાગી, જેમાં તેની પોતાની શાળાની બે છોકરીઓ પણ સામેલ હતી, જેનાથી તે પ્રેક્ટિસ દરમિયાન હંમેશા આગળ રહેતી હતી. તેનો એક ભાગ ત્યાં જ રોકાઈ જવા માંગતો હતો, રસ્તાના કિનારે બેસીને એ સ્વીકારવા માંગતો હતો કે તેની શરૂઆતની સવારનું વર્ષ એક ખરાબ પગલાને કારણે બરબાદ થઈ ગયું. તેના બદલે, તેને સવાર વિશે ગોવિંદ સરના શબ્દો યાદ આવ્યા જે અન્ય કોઈએ જોયા ન હતા, અને તેણે પોતાની જાતને કહ્યું કે હવે હાર માનવાથી તે શાંત પ્રયાસ એક ક્ષણમાં ભૂંસાઈ જશે.

તેણે પોતાના પગલાંને સમાયોજિત કર્યા, પોતાના ઇજા વગરના પગ પર વધુ વજન નાખ્યું, અને ધીમી, સાવચેત ગતિએ ચાલતી રહી, લગભગ દરેક ડગલે લથડિયા ખાતી રહી. રસ્તામાં હાજર દર્શકોએ, તેનો સ્પષ્ટ દુખાવો જોઈને, તેને પ્રોત્સાહિત કરી અને એક સ્વયંસેવકે તેને દોડમાંથી હટી જવા માટે કહ્યા વિના એક જળ સ્ટેશન પર તેની ઘૂંટી પર પાટો બાંધવાની રજૂઆત કરી. મીરાએ પાટો બાંધવાનું સ્વીકારી લીધું, પરંતુ રોકાવાનો ઇનકાર કરી દીધો, એ તર્ક આપતા કે ફિનિશિંગ, ભલે ધીમે ધીમે હોય, તેના માટે પરિણામ શીટ પર કોઈપણ સ્થાન કરતાં વધુ મહત્વ ધરાવે છે.

વિજેતાના લગભગ વીસ મિનિટ પછી તેણે ફિનિશ લાઇન પાર કરી લીધી, જેનું તેણે ક્યારેય સપનામાં પણ વિચાર્યું ન હતું, તેની ઘૂંટી સુજી ગઈ હતી અને તેના પગ થાકથી ધ્રૂજી રહ્યા હતા. તેમ છતાં તે દિવસે તેને જે સૌથી જોરદાર પ્રોત્સાહન મળ્યું, તે તેના સ્થાન માટે નહીં, પરંતુ ગોવિંદ સર તરફથી આવ્યું, જેમણે પછીથી તેને જણાવ્યું કે જે છોકરીએ ઘાયલ ઘૂંટી પર દોડ પૂરી કરી હતી, તેણે કંઈક એવું શીખ્યું છે જે કોઈ ટ્રોફી શીખવી શકતી નથી: કે તમે જે શરૂ કરો છો, તેને પૂરું કરવું, ભલે અપૂર્ણ રીતે, પોતાની રીતે એક જીત છે.''',
      questions: [
        PracticeQuestion(
          prompt: 'What had Govind sir often told Meera about marathons?',
          options: [
            'That marathons should be run without any coach.',
            'That finishing position does not matter at all.',
            'That marathons are won in the quiet, disciplined mornings when nobody else is watching, not the final sprint.',
            'That marathons are won only through natural talent.',
          ],
          correctIndex: 2,
          explanation: 'The passage states he reminded her "that marathons were not won in the final sprint but in the quiet, disciplined mornings when nobody else was watching."',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'What happened to Meera at the ten-kilometre mark?',
          options: [
            'She lost her way on the route.',
            'She collapsed from exhaustion.',
            'She ran out of water.',
            'She felt a sharp pain in her ankle after stepping on a loose stone.',
          ],
          correctIndex: 3,
          explanation: 'The passage says "Meera felt a sharp pain shoot through her ankle after stepping awkwardly on a loose stone."',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'Why did Meera decide not to give up after her injury?',
          options: [
            'She was afraid of disappointing the spectators.',
            'She realised her injury was not serious at all.',
            'A volunteer forced her to keep running.',
            'She remembered her coach\'s words and felt stopping would erase her year of quiet effort.',
          ],
          correctIndex: 3,
          explanation: 'The passage says she "remembered Govind sir\'s words about mornings nobody else saw, and told herself that giving up now would erase all of that quiet effort in an instant."',
          difficulty: Difficulty.hard,
        ),
        PracticeQuestion(
          prompt: 'What did Govind sir say Meera had learned by finishing the race despite her injury?',
          options: [
            'That winning is the only thing that matters in a race.',
            'That coaches are more important than athletes.',
            'That finishing what you start, even imperfectly, is its own kind of victory.',
            'That she should never run a marathon again.',
          ],
          correctIndex: 2,
          explanation: 'The passage ends with Govind sir telling her she had learned "that finishing what you start, even imperfectly, is its own kind of victory."',
          difficulty: Difficulty.medium,
        ),
      ],
      glosses: [
        InlineGloss(word: 'disciplined', meaningHi: 'अनुशासित', hiTransliteration: 'anushasit', meaningGu: 'શિસ્તબદ્ધ', guTransliteration: 'shistbaddh'),
        InlineGloss(word: 'overtake', meaningHi: 'आगे निकल जाना', hiTransliteration: 'aage nikal jaana', meaningGu: 'આગળ નીકળી જવું', guTransliteration: 'aagal nikli javu'),
        InlineGloss(word: 'wincing', meaningHi: 'दर्द से चेहरा सिकोड़ना', hiTransliteration: 'dard se chehra sikodna', meaningGu: 'પીડાથી ચહેરો સંકોચવો', guTransliteration: 'peedathi chahero sankochvo'),
        InlineGloss(word: 'spectators', meaningHi: 'दर्शक', hiTransliteration: 'darshak', meaningGu: 'દર્શકો', guTransliteration: 'darshako'),
        InlineGloss(word: 'withdraw', meaningHi: 'हट जाना / पीछे हट जाना', hiTransliteration: 'hat jaana / peeche hat jaana', meaningGu: 'પાછા હટવું', guTransliteration: 'pacha hatvu'),
        InlineGloss(word: 'exhaustion', meaningHi: 'थकावट', hiTransliteration: 'thakaawat', meaningGu: 'થાક', guTransliteration: 'thaak'),
        InlineGloss(word: 'trembling', meaningHi: 'काँपना', hiTransliteration: 'kaanpna', meaningGu: 'ધ્રૂજવું', guTransliteration: 'dhrujavu'),
        InlineGloss(word: 'stride', meaningHi: 'चाल / कदम रखने का तरीका', hiTransliteration: 'chaal / kadam rakhne ka tareeka', meaningGu: 'ચાલ / ડગલું', guTransliteration: 'chaal / daglu'),
        InlineGloss(word: 'victory', meaningHi: 'जीत', hiTransliteration: 'jeet', meaningGu: 'જીત', guTransliteration: 'jeet'),
        InlineGloss(word: 'awkwardly', meaningHi: 'अजीब ढंग से / बेढंगे तरीके से', hiTransliteration: 'ajeeb dhang se / bedhange tareeke se', meaningGu: 'અજીબ રીતે', guTransliteration: 'ajeeb rite'),
      ],
    ),
    ReadingPassage(
      id: 'class6_reading_bhabha',
      title: 'The Scientist Who Dreamed of Atoms',
      emoji: '⚛️',
      grade: 'Class 6',
      difficulty: Difficulty.hard,
      body: 'Long before India built its first nuclear research reactor, a young physicist named Homi Bhabha was '
          'already convinced that the country did not need to wait for other nations to hand it modern science. '
          'Born into a wealthy Mumbai family in 1909, Bhabha could easily have pursued a comfortable career '
          'abroad after studying at Cambridge University, where his brilliance in physics was quickly noticed by '
          'some of the greatest scientists of his time. Instead, a visit home during his holidays, combined with '
          'the outbreak of the Second World War, meant he stayed in India far longer than planned, and it changed '
          'the direction of his entire life.\n\n'
          'Stranded in India during the war, Bhabha began working at the Indian Institute of Science in Bangalore, '
          'frustrated that the country lacked laboratories capable of serious research in nuclear physics, a field '
          'he believed would shape the future of energy, medicine, and technology. Rather than simply complaining '
          'about the gap, he wrote directly to a wealthy industrialist, arguing passionately that India must build '
          'its own scientific institutions instead of depending entirely on foreign universities. His persistence '
          'led to the founding of the Tata Institute of Fundamental Research in 1945, an institution that would '
          'train generations of Indian scientists.\n\n'
          'Bhabha did not stop there. He believed strongly that atomic energy could be used peacefully, to '
          'generate electricity for millions of Indian homes rather than only for weapons, at a time when much of '
          'the world associated nuclear science mainly with the devastation of war. He convinced the newly '
          'independent Indian government to establish the Atomic Energy Commission, becoming its first chairman '
          'and guiding the construction of India\'s earliest nuclear research reactors with a mixture of scientific '
          'rigour and quiet diplomatic persuasion.\n\n'
          'Bhabha\'s life ended suddenly in a plane crash in 1966, before he could see many of his boldest plans '
          'fully realised, yet the institutions he built continued training scientists for decades afterward. '
          'Today, students who walk through the research centres that bear his name rarely think of the young man '
          'who once had every reason to build his career overseas, but chose instead to gamble on the idea that '
          'India could become a serious scientific power on its own terms.',
      bodyHi: 'भारत द्वारा अपना पहला परमाणु अनुसंधान रिएक्टर बनाने से बहुत पहले, होमी भाभा नामक एक युवा भौतिक विज्ञानी पहले से ही आश्वस्त थे कि देश को आधुनिक विज्ञान सौंपने के लिए अन्य देशों की प्रतीक्षा करने की आवश्यकता नहीं है। 1909 में मुंबई के एक धनी परिवार में जन्मे, भाभा कैम्ब्रिज विश्वविद्यालय में अध्ययन करने के बाद आसानी से विदेश में एक आरामदायक करियर बना सकते थे, जहाँ भौतिकी में उनकी प्रतिभा को उनके समय के कुछ महानतम वैज्ञानिकों ने तुरंत नोटिस किया था। इसके बजाय, द्वितीय विश्व युद्ध के फैलने के साथ अपनी छुट्टियों के दौरान घर आने का मतलब था कि वह योजना से कहीं अधिक समय तक भारत में रहे, और इसने उनके पूरे जीवन की दिशा बदल दी।\n\nयुद्ध के दौरान भारत में फंसे, भाभा ने बैंगलोर में भारतीय विज्ञान संस्थान में काम करना शुरू किया, इस बात से निराश होकर कि देश में परमाणु भौतिकी में गंभीर शोध करने में सक्षम प्रयोगशालाओं की कमी है, उनका मानना ​​था कि यह क्षेत्र ऊर्जा, चिकित्सा और प्रौद्योगिकी के भविष्य को आकार देगा। केवल अंतर के बारे में शिकायत करने के बजाय, उन्होंने सीधे एक धनी उद्योगपति को लिखा, और जोश से तर्क दिया कि भारत को पूरी तरह से विदेशी विश्वविद्यालयों पर निर्भर रहने के बजाय अपने स्वयं के वैज्ञानिक संस्थान बनाने चाहिए। उनकी दृढ़ता के कारण 1945 में टाटा इंस्टीट्यूट ऑफ फंडामेंटल रिसर्च की स्थापना हुई, एक ऐसी संस्था जो भारतीय वैज्ञानिकों की पीढ़ियों को प्रशिक्षित करेगी।\n\nभाभा यहीं नहीं रुके। उनका दृढ़ विश्वास था कि परमाणु ऊर्जा का उपयोग केवल हथियारों के बजाय लाखों भारतीय घरों के लिए बिजली पैदा करने के लिए शांतिपूर्वक किया जा सकता है, ऐसे समय में जब दुनिया के अधिकांश लोग परमाणु विज्ञान को मुख्य रूप से युद्ध की तबाही से जोड़ते थे। उन्होंने नव स्वतंत्र भारत सरकार को परमाणु ऊर्जा आयोग की स्थापना के लिए राजी किया, इसके पहले अध्यक्ष बने और वैज्ञानिक कठोरता और शांत राजनयिक अनुनय के मिश्रण के साथ भारत के शुरुआती परमाणु अनुसंधान रिएक्टरों के निर्माण का मार्गदर्शन किया।\n\nभाभा का जीवन 1966 में एक विमान दुर्घटना में अचानक समाप्त हो गया, इससे पहले कि वे अपनी कई साहसिक योजनाओं को पूरी तरह से साकार होते देख पाते, फिर भी उन्होंने जो संस्थान बनाए वे दशकों तक वैज्ञानिकों को प्रशिक्षण देते रहे। आज, जो छात्र उनके नाम वाले अनुसंधान केंद्रों से गुजरते हैं, वे शायद ही उस युवा व्यक्ति के बारे में सोचते हैं जिसके पास एक बार विदेश में अपना करियर बनाने का हर कारण था, लेकिन उसने इस विचार पर जुआ खेलने का फैसला किया कि भारत अपनी शर्तों पर एक गंभीर वैज्ञानिक शक्ति बन सकता है।',
      bodyGu: '''ભારત દ્વારા પોતાનું પ્રથમ પરમાણુ સંશોધન રિએક્ટર બનાવવામાં આવ્યું તેના ઘણા સમય પહેલાં, હોમી ભાભા નામના એક યુવા ભૌતિકશાસ્ત્રીને પહેલેથી જ ખાતરી હતી કે દેશે આધુનિક વિજ્ઞાન મેળવવા માટે અન્ય દેશો પર આધાર રાખવાની જરૂર નથી. ૧૯૦૯માં મુંબઈના એક શ્રીમંત પરિવારમાં જન્મેલા ભાભા, કેમ્બ્રિજ યુનિવર્સિટીમાં અભ્યાસ કર્યા પછી સરળતાથી વિદેશમાં આરામદાયક કારકિર્દી બનાવી શક્યા હોત, જ્યાં ભૌતિકશાસ્ત્રમાં તેમની તેજસ્વીતાની નોંધ તેમના સમયના કેટલાક મહાન વૈજ્ઞાનિકોએ તરત જ લીધી હતી. તેના બદલે, બીજા વિશ્વયુદ્ધ ફાટી નીકળવાને કારણે, રજાઓમાં ઘરે આવવાનો અર્થ એ થયો કે તેઓ ધારી હતી તેના કરતા વધુ સમય સુધી ભારતમાં રહ્યા, અને તેનાથી તેમના સમગ્ર જીવનની દિશા બદલાઈ ગઈ.

યુદ્ધ દરમિયાન ભારતમાં ફસાયેલા ભાભાએ બેંગ્લોરમાં આવેલી 'ઇન્ડિયન ઇન્સ્ટિટ્યૂટ ઓફ સાયન્સ'માં કામ કરવાનું શરૂ કર્યું. તેઓ એ વાતથી નિરાશ હતા કે દેશમાં પરમાણુ ભૌતિકશાસ્ત્રમાં ગંભીર સંશોધન કરવા સક્ષમ પ્રયોગશાળાઓનો અભાવ હતો, જ્યારે તેઓ માનતા હતા કે આ ક્ષેત્ર ઊર્જા, દવા અને ટેક્નોલોજીના ભવિષ્યને આકાર આપશે. માત્ર ફરિયાદ કરવાને બદલે, તેમણે સીધો એક શ્રીમંત ઉદ્યોગપતિને પત્ર લખ્યો, અને જુસ્સાભેર દલીલ કરી કે ભારતે સંપૂર્ણપણે વિદેશી યુનિવર્સિટીઓ પર આધાર રાખવાને બદલે પોતાની વૈજ્ઞાનિક સંસ્થાઓ ઊભી કરવી જોઈએ. તેમની દ્રઢતાને કારણે ૧૯૪૫માં 'ટાટા ઇન્સ્ટિટ્યૂટ ઓફ ફંડામેન્ટલ રિસર્ચ'ની સ્થાપના થઈ, એક એવી સંસ્થા જે ભારતીય વૈજ્ઞાનિકોની અનેક પેઢીઓને તાલીમ આપવાની હતી.

ભાભા અહીં જ ન અટક્યા. તેમનો દ્રઢ વિશ્વાસ હતો કે પરમાણુ ઊર્જાનો ઉપયોગ માત્ર હથિયારો માટે નહીં, પણ લાખો ભારતીય ઘરો માટે વીજળી પેદા કરવા માટે શાંતિપૂર્ણ રીતે થઈ શકે છે, એવા સમયે જ્યારે વિશ્વના મોટાભાગના લોકો પરમાણુ વિજ્ઞાનને મુખ્યત્વે યુદ્ધની તબાહી સાથે જોડતા હતા. તેમણે નવસ્વતંત્ર ભારત સરકારને 'એટોમિક એનર્જી કમિશન' (પરમાણુ ઊર્જા પંચ) ની સ્થાપના કરવા મનાવી, તેના પ્રથમ અધ્યક્ષ બન્યા અને વૈજ્ઞાનિક સચોટતા અને શાંત રાજદ્વારી સમજાવટના મિશ્રણથી ભારતના પ્રારંભિક પરમાણુ સંશોધન રિએક્ટરોના નિર્માણનું માર્ગદર્શન કર્યું.

૧૯૬૬માં એક વિમાન દુર્ઘટનામાં ભાભાનું જીવન અચાનક સમાપ્ત થઈ ગયું, તે પહેલાં કે તેઓ તેમની ઘણી હિંમતભરી યોજનાઓને સંપૂર્ણપણે સાકાર થતી જોઈ શકે. છતાં તેમણે બનાવેલી સંસ્થાઓ દાયકાઓ સુધી વૈજ્ઞાનિકોને તાલીમ આપતી રહી. આજે, જે વિદ્યાર્થીઓ તેમના નામવાળા સંશોધન કેન્દ્રોમાંથી પસાર થાય છે, તેઓ ભાગ્યે જ એ યુવાન વિશે વિચારે છે જેની પાસે એક સમયે વિદેશમાં પોતાની કારકિર્દી બનાવવાના તમામ કારણો હતા, પરંતુ તેણે એ વિચાર પર મોટું જોખમ ઉઠાવવાનું પસંદ કર્યું કે ભારત પોતાની શરતો પર એક ગંભીર વૈજ્ઞાનિક શક્તિ બની શકે છે.''',
      questions: [
        PracticeQuestion(
          prompt: 'Why did Homi Bhabha end up staying in India far longer than he had originally planned?',
          options: [
            'A visit home during the holidays combined with the outbreak of the Second World War kept him there.',
            'He was never actually planning to study abroad.',
            'The Indian government refused to let him leave the country.',
            'He failed his examinations at Cambridge University.',
          ],
          correctIndex: 0,
          explanation: 'The passage explains "a visit home during his holidays, combined with the outbreak of the Second World War, meant he stayed in India far longer than planned."',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'What frustrated Bhabha while he worked at the Indian Institute of Science?',
          options: [
            'The government\'s refusal to fund any of his projects.',
            'The absence of any interested students.',
            'His inability to understand advanced physics concepts.',
            'The lack of laboratories capable of serious nuclear physics research in the country.',
          ],
          correctIndex: 3,
          explanation: 'The passage says he was "frustrated that the country lacked laboratories capable of serious research in nuclear physics."',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'What was Bhabha\'s vision for the peaceful use of atomic energy?',
          options: [
            'To use it only for building weapons.',
            'To generate electricity for millions of Indian homes rather than only for weapons.',
            'To keep nuclear science research secret from the public.',
            'To sell nuclear technology exclusively to other countries.',
          ],
          correctIndex: 1,
          explanation: 'The passage states he believed atomic energy "could be used peacefully, to generate electricity for millions of Indian homes rather than only for weapons."',
          difficulty: Difficulty.hard,
        ),
        PracticeQuestion(
          prompt: 'What is the passage\'s overall message about Bhabha\'s choices?',
          options: [
            'He regretted not building his career overseas.',
            'His plans were considered unrealistic and were never carried out.',
            'He chose to build India\'s scientific institutions rather than pursue an easier career abroad.',
            'He worked entirely alone without support from the government.',
          ],
          correctIndex: 2,
          explanation: 'The final paragraph describes him as someone who "had every reason to build his career overseas, but chose instead to gamble on the idea that India could become a serious scientific power on its own terms."',
          difficulty: Difficulty.hard,
        ),
      ],
      glosses: [
        InlineGloss(word: 'physicist', meaningHi: 'भौतिक विज्ञानी', hiTransliteration: 'bhautik vigyani', meaningGu: 'ભૌતિકશાસ્ત્રી', guTransliteration: 'bhautikshastri'),
        InlineGloss(word: 'brilliance', meaningHi: 'प्रतिभा / तेज़ बुद्धि', hiTransliteration: 'pratibha / tez buddhi', meaningGu: 'પ્રતિભા / તેજસ્વીતા', guTransliteration: 'pratibha / tejasvita'),
        InlineGloss(word: 'stranded', meaningHi: 'फँसा हुआ', hiTransliteration: 'fansa hua', meaningGu: 'ફસાયેલા / અટવાયેલા', guTransliteration: 'fasayela / atvayela'),
        InlineGloss(word: 'persistence', meaningHi: 'दृढ़ता / लगातार कोशिश', hiTransliteration: 'dridhta / lagatar koshish', meaningGu: 'દ્રઢતા / સતત પ્રયાસ', guTransliteration: 'dradhta / satat prayas'),
        InlineGloss(word: 'industrialist', meaningHi: 'बड़ा उद्योगपति', hiTransliteration: 'bada udyogpati', meaningGu: 'મોટા ઉદ્યોગપતિ', guTransliteration: 'mota udyogpati'),
        InlineGloss(word: 'institutions', meaningHi: 'संस्थान', hiTransliteration: 'sansthaan', meaningGu: 'સંસ્થાઓ', guTransliteration: 'sansthao'),
        InlineGloss(word: 'devastation', meaningHi: 'भारी तबाही', hiTransliteration: 'bhaari tabaahi', meaningGu: 'ભારે તબાહી / વિનાશ', guTransliteration: 'bhare tabahi / vinash'),
        InlineGloss(word: 'diplomatic', meaningHi: 'कूटनीतिक / समझदारी भरा', hiTransliteration: 'kootneetik / samajhdaari bhara', meaningGu: 'રાજદ્વારી / સમજદારીભર્યું', guTransliteration: 'rajdvari / samajdaribharyu'),
        InlineGloss(word: 'rigour', meaningHi: 'सख्ती / सटीकता', hiTransliteration: 'sakhti / sateekta', meaningGu: 'સખતાઈ / સચોટતા', guTransliteration: 'sakhatai / sachotata'),
        InlineGloss(word: 'gamble', meaningHi: 'जोखिम उठाना', hiTransliteration: 'jokhim uthaana', meaningGu: 'જોખમ ઉઠાવવું', guTransliteration: 'jokhim uthavavu'),
      ],
    ),
    ReadingPassage(
      id: 'class6_reading_vultures',
      title: 'Bringing Back the Vultures',
      emoji: '🦅',
      grade: 'Class 6',
      difficulty: Difficulty.medium,
      body: 'Ritvik\'s grandfather often spoke about the enormous flocks of vultures that once circled above the '
          'fields near their Gujarat village, cleaning up the carcasses of dead cattle within hours and keeping '
          'disease from spreading. By the time Ritvik was old enough to notice birds at all, those flocks had '
          'nearly vanished, and the few vultures anyone saw were sick, weak, or already dying near the village '
          'well. Nobody in the village understood why, until a team of wildlife veterinarians arrived one summer to '
          'investigate the mysterious decline.\n\n'
          'The veterinarians explained a discovery that shocked the entire village: a common medicine given to '
          'sick cattle to relieve their pain was deadly to vultures that later fed on the carcasses of treated '
          'animals that had died. The medicine caused fatal kidney failure in the birds within days, and because '
          'vultures fed in large groups, a single treated carcass could wipe out dozens of birds at once. Ritvik '
          'found it strange and sad that a medicine meant to ease suffering in one animal could cause so much harm '
          'to another.\n\n'
          'The team asked for the village\'s help in a conservation effort, urging farmers to switch to a safer '
          'alternative medicine for their cattle and requesting that any dead animals be reported quickly so '
          'veterinarians could test whether they were safe for vultures to feed on. Ritvik\'s father, initially '
          'skeptical that changing one medicine could really matter, agreed to try it after the veterinarians '
          'explained how close the vultures were to disappearing entirely from the region.\n\n'
          'It took nearly six years of the whole village cooperating, along with a specially built vulture '
          'breeding centre nearby, before Ritvik saw his first real change: a pair of vultures nesting on the '
          'cliff edge outside the village for the first time since his grandfather was young. His grandfather, '
          'now too old to walk far, asked to be taken to see the nest, saying quietly that he had feared he would '
          'never again see the sky the way it had looked in his childhood, crowded with slow, circling wings that '
          'kept the village and its fields clean and healthy.',
      bodyHi: 'ऋत्विक के दादाजी अक्सर गिद्धों के विशाल झुंडों के बारे में बात करते थे जो कभी उनके गुजरात गांव के पास के खेतों के ऊपर चक्कर लगाते थे, मृत मवेशियों के शवों को कुछ ही घंटों में साफ कर देते थे और बीमारी को फैलने से रोकते थे। जब ऋत्विक इतना बड़ा हुआ कि उसने पक्षियों को बिल्कुल भी नोटिस नहीं किया, तो वे झुंड लगभग गायब हो गए थे, और जो कुछ गिद्ध किसी ने देखे थे वे बीमार, कमजोर थे, या पहले से ही गाँव के कुएं के पास मर रहे थे। गांव में कोई भी यह नहीं समझ पाया कि क्यों, जब तक कि एक गर्मियों में वन्यजीव पशु चिकित्सकों की एक टीम रहस्यमय गिरावट की जांच करने के लिए नहीं पहुंची।\n\nपशु चिकित्सकों ने एक ऐसी खोज के बारे में बताया जिसने पूरे गांव को चौंका दिया: बीमार मवेशियों को उनके दर्द से राहत देने के लिए दी जाने वाली एक सामान्य दवा गिद्धों के लिए घातक थी, जो बाद में इलाज किए गए जानवरों के शवों को खाते थे जो मर गए थे। इस दवा के कारण कुछ ही दिनों में पक्षियों की किडनी घातक रूप से खराब हो गई, और क्योंकि गिद्ध बड़े समूहों में भोजन करते थे, एक उपचारित शव एक ही बार में दर्जनों पक्षियों का सफाया कर सकता था। ऋत्विक को यह अजीब और दुखद लगा कि एक जानवर की पीड़ा कम करने वाली दवा दूसरे जानवर को इतना नुकसान पहुंचा सकती है।\n\nटीम ने संरक्षण के प्रयास में गांव की मदद मांगी, किसानों से अपने मवेशियों के लिए सुरक्षित वैकल्पिक दवा अपनाने का आग्रह किया और अनुरोध किया कि किसी भी मृत जानवर की सूचना तुरंत दी जाए ताकि पशुचिकित्सक परीक्षण कर सकें कि क्या वे गिद्धों के भोजन के लिए सुरक्षित हैं। ऋत्विक के पिता को शुरू में संदेह था कि एक दवा को बदलने से वास्तव में कोई फर्क पड़ सकता है, पशु चिकित्सकों द्वारा यह समझाने के बाद कि गिद्ध इस क्षेत्र से पूरी तरह से गायब होने के कितने करीब हैं, इसे आजमाने के लिए सहमत हुए।\n\nपूरे गांव के साथ-साथ पास में एक विशेष रूप से निर्मित गिद्ध प्रजनन केंद्र के सहयोग से लगभग छह साल लग गए, इससे पहले कि ऋत्विक ने अपना पहला वास्तविक परिवर्तन देखा: गिद्धों का एक जोड़ा अपने दादा के युवा होने के बाद पहली बार गांव के बाहर चट्टान के किनारे पर घोंसला बना रहा था। उनके दादाजी, जो अब दूर तक चलने के लिए बहुत बूढ़े थे, ने घोंसले को देखने के लिए ले जाने के लिए कहा, उन्होंने धीरे से कहा कि उन्हें डर है कि वह कभी भी आकाश को उस तरह नहीं देख पाएंगे जैसा कि बचपन में दिखता था, धीमे, चक्करदार पंखों से भरा हुआ जो गांव और उसके खेतों को साफ और स्वस्थ रखता था।',
      bodyGu: '''ઋત્વિકના દાદાજી અવારનવાર ગીધના વિશાળ ટોળાઓ વિશે વાત કરતા હતા જે એક સમયે તેમના ગુજરાતના ગામ નજીકના ખેતરો પર ચક્કર લગાવતા હતા, મૃત પશુઓના શબને ગણતરીના કલાકોમાં સાફ કરતા અને રોગને ફેલાતો અટકાવતા હતા. જ્યારે ઋત્વિક એટલો મોટો થયો કે તેણે પક્ષીઓને બિલકુલ પણ નોંધવાનું શરૂ કર્યું, ત્યાં સુધીમાં તે ટોળાઓ લગભગ ગાયબ થઈ ગયા હતા, અને જે થોડા ગીધ કોઈએ જોયા હતા તે બીમાર, નબળા અથવા ગામના કૂવા પાસે મરી રહ્યા હતા. ગામમાં કોઈ પણ સમજી શક્યું નહીં કે શા માટે, જ્યાં સુધી એક ઉનાળામાં વન્યજીવ પશુ ચિકિત્સકોની એક ટીમ આ રહસ્યમય ઘટાડાની તપાસ કરવા માટે ન આવી.

પશુ ચિકિત્સકોએ એક એવી શોધ વિશે જણાવ્યું જેણે આખા ગામને ચોંકાવી દીધું: બીમાર પશુઓને તેમની પીડામાંથી રાહત આપવા માટે આપવામાં આવતી એક સામાન્ય દવા ગીધ માટે ઘાતક હતી, જે પછીથી સારવાર કરાયેલા પ્રાણીઓના શબને ખાતા હતા જે મરી ગયા હતા. આ દવાને કારણે થોડા જ દિવસોમાં પક્ષીઓની કિડની ઘાતક રીતે ખરાબ થઈ ગઈ, અને કારણ કે ગીધ મોટા જૂથોમાં ખોરાક ખાતા હતા, એક સારવાર કરાયેલ શબ એક જ વારમાં ડઝનબંધ પક્ષીઓનો સફાયો કરી શકતું હતું. ઋત્વિકને તે વિચિત્ર અને દુઃખદ લાગ્યું કે એક પ્રાણીની પીડા ઓછી કરવાવાળી દવા બીજા પ્રાણીને આટલું નુકસાન પહોંચાડી શકે છે.

ટીમે સંરક્ષણના પ્રયાસમાં ગામની મદદ માંગી, ખેડૂતોને તેમના પશુઓ માટે સુરક્ષિત વૈકલ્પિક દવા અપનાવવાનો આગ્રહ કર્યો અને વિનંતી કરી કે કોઈ પણ મૃત પ્રાણીની માહિતી તરત જ આપવામાં આવે જેથી પશુ ચિકિત્સકો પરીક્ષણ કરી શકે કે શું તે ગીધના ખોરાક માટે સુરક્ષિત છે. ઋત્વિકના પિતાને શરૂઆતમાં શંકા હતી કે એક દવા બદલવાથી ખરેખર કોઈ ફરક પડી શકે છે, પરંતુ પશુ ચિકિત્સકો દ્વારા એ સમજાવ્યા પછી કે ગીધ આ વિસ્તારમાંથી સંપૂર્ણપણે ગાયબ થવાની કેટલી નજીક છે, તેઓ તેને અજમાવવા માટે સંમત થયા.

આખા ગામ તેમજ નજીકમાં એક ખાસ બનાવવામાં આવેલ ગીધ પ્રજનન કેન્દ્રના સહયોગથી લગભગ છ વર્ષ લાગ્યા, તે પહેલાં ઋત્વિકે પોતાનો પહેલો વાસ્તવિક ફેરફાર જોયો: ગીધની એક જોડી તેના દાદાના યુવાન હોવા પછી પહેલીવાર ગામની બહાર ખડકના કિનારે માળો બનાવી રહી હતી. તેના દાદાજી, જે હવે દૂર સુધી ચાલવા માટે ખૂબ વૃદ્ધ થઈ ગયા હતા, તેમણે માળો જોવા લઈ જવાનું કહ્યું, તેમણે ધીમેથી કહ્યું કે તેમને ડર હતો કે તેઓ ક્યારેય આકાશને એવું નહીં જોઈ શકે જેવું તે બાળપણમાં દેખાતું હતું, ધીમી, ચક્કર લગાવતી પાંખોથી ભરેલું જે ગામ અને તેના ખેતરોને સ્વચ્છ અને સ્વસ્થ રાખતું હતું.''',
      questions: [
        PracticeQuestion(
          prompt: 'What role did vultures traditionally play near Ritvik\'s village, according to his grandfather?',
          options: [
            'They protected the village from other predators.',
            'They helped farmers plough their fields.',
            'They pollinated crops in the fields.',
            'They cleaned up the carcasses of dead cattle quickly and helped prevent disease from spreading.',
          ],
          correctIndex: 3,
          explanation: 'The passage says the vultures were "cleaning up the carcasses of dead cattle within hours and keeping disease from spreading."',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'What did the veterinarians discover was causing the vulture deaths?',
          options: [
            'Hunters were killing the vultures for their feathers.',
            'A common cattle medicine was fatally poisoning vultures that fed on treated carcasses.',
            'Farmers were destroying the vultures\' nesting sites.',
            'The vultures were dying from a natural disease unrelated to humans.',
          ],
          correctIndex: 1,
          explanation: 'The passage explains "a common medicine given to sick cattle... was deadly to vultures that later fed on the carcasses of treated animals," causing fatal kidney failure.',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'How did Ritvik\'s father initially react to the veterinarians\' request to change medicines?',
          options: [
            'He was skeptical at first but agreed to try it after learning how close the vultures were to disappearing.',
            'He immediately agreed without any hesitation.',
            'He refused outright and never changed his mind.',
            'He asked the veterinarians to leave the village.',
          ],
          correctIndex: 0,
          explanation: 'The passage says he was "initially skeptical that changing one medicine could really matter" but "agreed to try it after the veterinarians explained how close the vultures were to disappearing entirely."',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'What moment showed that the conservation effort was finally succeeding?',
          options: [
            'Ritvik\'s grandfather stopped talking about the past.',
            'A pair of vultures nested on the cliff edge outside the village for the first time in decades.',
            'The veterinarians left the village permanently.',
            'The village stopped keeping cattle altogether.',
          ],
          correctIndex: 1,
          explanation: 'The passage describes Ritvik seeing "a pair of vultures nesting on the cliff edge outside the village for the first time since his grandfather was young" after six years of effort.',
          difficulty: Difficulty.hard,
        ),
      ],
      glosses: [
        InlineGloss(word: 'carcasses', meaningHi: 'मरे हुए जानवर का शरीर', hiTransliteration: 'mare hue janwar ka shareer', meaningGu: 'મૃત પ્રાણીનું શબ', guTransliteration: 'mrit praninu shab'),
        InlineGloss(word: 'decline', meaningHi: 'गिरावट / कमी', hiTransliteration: 'giraawat / kami', meaningGu: 'ઘટાડો', guTransliteration: 'ghatado'),
        InlineGloss(word: 'veterinarians', meaningHi: 'पशु चिकित्सक', hiTransliteration: 'pashu chikitsak', meaningGu: 'પશુ ચિકિત્સક', guTransliteration: 'pashu chikitsak'),
        InlineGloss(word: 'fatal', meaningHi: 'जानलेवा', hiTransliteration: 'jaanleva', meaningGu: 'ઘાતક / જીવલેણ', guTransliteration: 'ghatak / jivlen'),
        InlineGloss(word: 'skeptical', meaningHi: 'शंका करने वाला / संदेह करने वाला', hiTransliteration: 'shanka karne wala / sandeh karne wala', meaningGu: 'શંકાશીલ', guTransliteration: 'shankashil'),
        InlineGloss(word: 'cooperating', meaningHi: 'मिलकर सहयोग करना', hiTransliteration: 'milkar sahyog karna', meaningGu: 'સહકાર આપવો', guTransliteration: 'sahkar aapvo'),
        InlineGloss(word: 'breeding', meaningHi: 'प्रजनन', hiTransliteration: 'prajanan', meaningGu: 'પ્રજનન', guTransliteration: 'prajanan'),
        InlineGloss(word: 'nesting', meaningHi: 'घोंसला बनाना', hiTransliteration: 'ghonsla banana', meaningGu: 'માળો બનાવવો', guTransliteration: 'maalo banavvo'),
        InlineGloss(word: 'disappearing', meaningHi: 'लुप्त हो जाना / गायब हो जाना', hiTransliteration: 'lupt ho jaana / gaayab ho jaana', meaningGu: 'ગાયબ થઈ જવું / લુપ્ત થવું', guTransliteration: 'gayab thai javu / lupt thavu'),
        InlineGloss(word: 'conservation', meaningHi: 'संरक्षण / बचाव', hiTransliteration: 'sanrakshan / bachaav', meaningGu: 'સંરક્ષણ / બચાવ', guTransliteration: 'sanrakshan / bachaav'),
      ],
    ),
  ],
);
