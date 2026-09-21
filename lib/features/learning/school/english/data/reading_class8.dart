import '../models/chapter.dart' show InlineGloss;
import '../models/practice_question.dart';
import '../models/reading_passage.dart';

const class8Reading = ReadingLibrary(
  id: 'class8_reading',
  title: 'Reading Passages',
  grade: 'Class 8',
  passages: [
    ReadingPassage(
      id: 'class8_reading_solarlamp',
      title: 'Light After Sunset',
      emoji: '💡',
      grade: 'Class 8',
      difficulty: Difficulty.medium,
      body: 'For the residents of Kharol, a small hamlet perched on a hillside with no direct road access, '
          'electricity had remained an elusive promise for over two decades, with successive government surveys '
          'concluding that connecting the village to the grid was simply too expensive for its modest '
          'population. Children studied by kerosene lamps that left their eyes stinging and their notebooks '
          'smudged with soot, while shopkeepers closed early each evening once daylight faded completely.\n\n'
          'When a nonprofit organisation focused on rural energy access visited Kharol, they proposed an '
          'alternative that villagers initially received with polite scepticism: small solar-powered lamps, '
          'affordable enough for most families and requiring no wiring or connection to any distant power '
          'station. The organisation offered to train two local youths, including nineteen-year-old Meera, as '
          'technicians who could maintain and repair the lamps themselves rather than depending on outside '
          'visits whenever something malfunctioned.\n\n'
          'Meera approached her new responsibility seriously, learning not just how to fix broken lamps but also '
          'how to explain their maintenance clearly to families who had never owned any electronic device before. '
          'She discovered that patiently demonstrating each step, rather than simply completing repairs herself, '
          'built genuine confidence among villagers, who gradually began attempting simple fixes independently '
          'rather than waiting anxiously for her visits.\n\n'
          'Within a year, nearly every household in Kharol owned at least one solar lamp, and the change proved '
          'far more significant than simply extending the hours in which people could see. Children reported '
          'improved grades, attributing it to more comfortable evening study sessions, and two shopkeepers '
          'extended their business hours meaningfully for the first time in years. Meera, once uncertain about '
          'her ability to master unfamiliar technology, now regularly trains technicians in neighbouring '
          'villages facing the very same challenges Kharol once did.',
      bodyHi: 'खारोल के निवासियों के लिए, एक पहाड़ी पर बसा एक छोटा सा गांव जहां कोई सीधी सड़क पहुंच नहीं थी, बिजली दो दशकों से अधिक समय से एक मायावी वादा बनी हुई थी, लगातार सरकारी सर्वेक्षणों से यह निष्कर्ष निकला कि गांव को ग्रिड से जोड़ना इसकी मामूली आबादी के लिए बहुत महंगा था। बच्चे मिट्टी के तेल के लैंप में पढ़ाई करते थे, जिससे उनकी आंखें चुभने लगती थीं और उनकी नोटबुक कालिख से सनी हो जाती थीं, जबकि दिन की रोशनी पूरी तरह से कम हो जाने पर दुकानदार हर शाम जल्दी बंद हो जाते थे।\n\nजब ग्रामीण ऊर्जा पहुंच पर ध्यान केंद्रित करने वाले एक गैर-लाभकारी संगठन ने खारोल का दौरा किया, तो उन्होंने एक विकल्प का प्रस्ताव रखा, जिसे ग्रामीणों ने शुरू में विनम्र संदेह के साथ स्वीकार किया: छोटे सौर ऊर्जा से चलने वाले लैंप, जो अधिकांश परिवारों के लिए काफी किफायती थे और किसी भी दूर के बिजली स्टेशन से तार या कनेक्शन की आवश्यकता नहीं थी। संगठन ने उन्नीस वर्षीय मीरा सहित दो स्थानीय युवाओं को तकनीशियनों के रूप में प्रशिक्षित करने की पेशकश की, जो कुछ खराबी होने पर बाहरी दौरे पर निर्भर रहने के बजाय स्वयं लैंप का रखरखाव और मरम्मत कर सकते थे।\n\nमीरा ने अपनी नई ज़िम्मेदारी को गंभीरता से लिया, न केवल टूटे हुए लैंप को ठीक करना सीखा, बल्कि उन परिवारों को उनके रखरखाव के बारे में स्पष्ट रूप से कैसे समझाया, जिनके पास पहले कभी कोई इलेक्ट्रॉनिक उपकरण नहीं था। उन्होंने पाया कि स्वयं मरम्मत पूरी करने के बजाय धैर्यपूर्वक हर कदम का प्रदर्शन करने से ग्रामीणों में वास्तविक विश्वास पैदा हुआ, जिन्होंने धीरे-धीरे उनकी यात्राओं के लिए उत्सुकता से इंतजार करने के बजाय स्वतंत्र रूप से सरल सुधारों का प्रयास करना शुरू कर दिया।\n\nएक वर्ष के भीतर, खारोल में लगभग हर घर में कम से कम एक सौर लैंप था, और यह बदलाव लोगों को देखने के घंटों को बढ़ाने की तुलना में कहीं अधिक महत्वपूर्ण साबित हुआ। बच्चों ने ग्रेड में सुधार की सूचना दी, इसका श्रेय अधिक आरामदायक शाम के अध्ययन सत्र को दिया, और दो दुकानदारों ने वर्षों में पहली बार अपने व्यावसायिक घंटों को सार्थक रूप से बढ़ाया। मीरा, जो एक समय अपरिचित प्रौद्योगिकी में महारत हासिल करने की अपनी क्षमता के बारे में अनिश्चित थी, अब नियमित रूप से पड़ोसी गांवों में तकनीशियनों को प्रशिक्षित करती है और उन्हीं चुनौतियों का सामना कर रही है जो कभी खारोल ने किया था।',
      bodyGu: '''ખારોલના રહેવાસીઓ માટે, એક ટેકરી પર આવેલું એક નાનકડું ગામ જ્યાં કોઈ સીધો રસ્તો નહોતો, વીજળી બે દાયકાથી વધુ સમયથી એક માયાવી વચન બની રહી હતી, કારણ કે સતત સરકારી સર્વેક્ષણો પરથી એ નિષ્કર્ષ નીકળ્યો હતો કે ગામને ગ્રીડ સાથે જોડવું તેની ઓછી વસ્તી માટે ખૂબ ખર્ચાળ હતું. બાળકો કેરોસીનના દીવાઓ પાસે ભણતા હતા, જેનાથી તેમની આંખોમાં બળતરા થતી હતી અને તેમની નોટબુકમાં કાળશ લાગી જતી હતી, જ્યારે દિવસનો પ્રકાશ સંપૂર્ણપણે ઓછો થઈ જતાં દુકાનદારો દરરોજ સાંજે દુકાનો વહેલી બંધ કરી દેતા હતા.

જ્યારે ગ્રામીણ ઊર્જા પહોંચ પર ધ્યાન કેન્દ્રિત કરતી એક બિન-નફાકારક સંસ્થાએ ખારોલની મુલાકાત લીધી, ત્યારે તેમણે એક વિકલ્પનો પ્રસ્તાવ મૂક્યો, જે ગામવાળાઓએ શરૂઆતમાં નમ્ર શંકા સાથે સ્વીકાર્યો: નાના સૌર ઊર્જાથી ચાલતા દીવાઓ, જે મોટાભાગના પરિવારો માટે ખૂબ જ સસ્તા હતા અને તેમાં કોઈપણ દૂરના પાવર સ્ટેશનથી વાયરિંગ અથવા કનેક્શનની જરૂર નહોતી. સંસ્થાએ ઓગણીસ વર્ષીય મીરા સહિત બે સ્થાનિક યુવાનોને ટેકનિશિયન તરીકે તાલીમ આપવાની ઓફર કરી, જે કંઈક ખરાબી થાય ત્યારે બહારની મુલાકાતો પર નિર્ભર રહેવાને બદલે જાતે જ દીવાઓની જાળવણી અને સમારકામ કરી શકે.

મીરાએ પોતાની નવી જવાબદારી ગંભીરતાથી લીધી, માત્ર તૂટેલા દીવાઓને કેવી રીતે ઠીક કરવા તે જ નહીં, પરંતુ જે પરિવારો પાસે પહેલાં ક્યારેય કોઈ ઇલેક્ટ્રોનિક ઉપકરણ નહોતું તેમને સ્પષ્ટપણે તેની જાળવણી કેવી રીતે કરવી તે પણ સમજાવ્યું. તેણે જોયું કે માત્ર પોતે જ સમારકામ પૂર્ણ કરવાને બદલે ધીરજપૂર્વક દરેક પગલું દર્શાવવાથી ગામવાળાઓમાં વાસ્તવિક આત્મવિશ્વાસ પેદા થયો, જેમણે ધીમે ધીમે તેની મુલાકાતોની આતુરતાથી રાહ જોવાને બદલે સ્વતંત્ર રીતે સરળ સુધારાઓ કરવાનો પ્રયાસ શરૂ કર્યો.

એક વર્ષની અંદર, ખારોલના લગભગ દરેક ઘરમાં ઓછામાં ઓછો એક સોલાર લેમ્પ હતો, અને આ પરિવર્તન લોકો માટે ફક્ત પ્રકાશ જોવાનો સમય વધારવા કરતાં ઘણું વધુ મહત્વનું સાબિત થયું. બાળકોએ તેમના ગ્રેડમાં સુધારો નોંધાવ્યો, જેનો શ્રેય સાંજની વધુ આરામદાયક અભ્યાસ બેઠકોને આપવામાં આવ્યો, અને બે દુકાનદારોએ વર્ષોમાં પ્રથમ વખત તેમના વ્યવસાયિક કલાકોમાં સાર્થક રીતે વધારો કર્યો. મીરા, જે એક સમયે અજાણી ટેક્નોલોજીમાં નિપુણતા મેળવવાની પોતાની ક્ષમતા વિશે અનિશ્ચિત હતી, તે હવે નિયમિતપણે પાડોશી ગામોમાં ટેકનિશિયનોને તાલીમ આપે છે અને એવા જ પડકારોનો સામનો કરી રહી છે જેનો ખારોલએ એક સમયે સામનો કર્યો હતો.''',
      questions: [
        PracticeQuestion(
          prompt: 'Why had Kharol never been connected to the electricity grid?',
          options: [
            'The villagers refused the offer of a connection.',
            'Government surveys concluded it was too expensive given the village\'s small population.',
            'The village had no interest in electricity.',
            'A previous connection had been destroyed.',
          ],
          correctIndex: 1,
          explanation: 'The passage states surveys "concluded that connecting the village to the grid was simply too expensive for its modest population."',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'What made the solar lamp solution different from earlier attempts to bring electricity?',
          options: [
            'It required a direct connection to the power station.',
            'It required no wiring or connection to a distant power station, and villagers could maintain the lamps themselves.',
            'It was more expensive than a grid connection.',
            'It only worked during the day.',
          ],
          correctIndex: 1,
          explanation: 'The passage explains the lamps needed "no wiring or connection to any distant power station" and local technicians could maintain them.',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'What approach did Meera take that built genuine confidence among villagers?',
          options: [
            'She fixed every lamp herself without explanation.',
            'She avoided visiting the village too often.',
            'She patiently demonstrated each repair step instead of just completing it herself.',
            'She refused to teach anyone else the skills.',
          ],
          correctIndex: 2,
          explanation: 'The passage states "patiently demonstrating each step, rather than simply completing repairs herself, built genuine confidence."',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'What does the passage suggest was the wider impact of the solar lamps beyond providing light?',
          options: [
            'It had no impact beyond lighting.',
            'It improved children\'s study habits, extended shopkeepers\' business hours, and gave Meera new skills she now shares with other villages.',
            'It made the villagers dependent on the nonprofit organisation.',
            'It caused the village to lose interest in getting a real electricity connection.',
          ],
          correctIndex: 1,
          explanation: 'The passage describes improved grades, extended shop hours, and Meera training technicians elsewhere as wider effects.',
          difficulty: Difficulty.hard,
        ),
      ],
      glosses: [
        InlineGloss(word: 'elusive', meaningHi: 'मायावी / न मिल पाने वाला', hiTransliteration: 'maayaavi / na mil paane wala', meaningGu: 'માયાવી / પકડમાં ન આવે તેવું', guTransliteration: 'maayaavi / pakadma na aave tevu'),
        InlineGloss(word: 'soot', meaningHi: 'कालिख', hiTransliteration: 'kaalikh', meaningGu: 'કાળશ / મેશ', guTransliteration: 'kaalash / mesh'),
        InlineGloss(word: 'scepticism', meaningHi: 'संदेह', hiTransliteration: 'sandeh', meaningGu: 'શંકા', guTransliteration: 'shanka'),
        InlineGloss(word: 'malfunctioned', meaningHi: 'खराब हो गया', hiTransliteration: 'kharaab ho gaya', meaningGu: 'બગડી ગયું', guTransliteration: 'bagadi gayu'),
        InlineGloss(word: 'attributing', meaningHi: 'श्रेय देना', hiTransliteration: 'shrey dena', meaningGu: 'શ્રેય આપવું', guTransliteration: 'shrey aapvu'),
      ],
    ),
    ReadingPassage(
      id: 'class8_reading_orphanedelephant',
      title: 'The Calf Nobody Wanted',
      emoji: '🐘',
      grade: 'Class 8',
      difficulty: Difficulty.hard,
      body: 'When forest rangers discovered the young elephant calf wandering alone near the edge of the '
          'reserve, badly dehydrated and clearly separated from her herd for several days, most experienced '
          'wildlife workers privately doubted she would survive the week. Orphaned elephant calves rarely '
          'thrived without their mother\'s milk and constant social contact, and the nearest rehabilitation '
          'centre equipped to handle such a young animal lay nearly two hundred kilometres away.\n\n'
          'Dr. Priyamvada Rao, the reserve\'s veterinarian, made the unconventional decision to attempt hand-'
          'rearing the calf on-site rather than risking the long, stressful journey to the distant centre. This '
          'meant establishing a feeding schedule every three hours, day and night, using a specially formulated '
          'milk substitute that had to be prepared fresh each time, and finding staff willing to maintain this '
          'exhausting routine for months without any guarantee of success.\n\n'
          'The calf, eventually named Chhoti, proved remarkably resilient but presented an unexpected '
          'complication: she began forming an intense attachment to Dr. Rao specifically, following her '
          'everywhere and becoming distressed whenever separated, which worried the team since wild elephants '
          'ideally should not become overly dependent on a single human. Dr. Rao gradually introduced other '
          'staff members into the feeding rotation and, crucially, arranged supervised visits with an older, '
          'gentle female elephant already living at the reserve, hoping Chhoti would eventually transfer some '
          'of her attachment toward her own species.\n\n'
          'Eighteen months later, Chhoti had fully integrated into a small herd at the reserve, though she still '
          'occasionally approached Dr. Rao\'s jeep when it passed nearby, momentarily pausing before rejoining '
          'her adoptive herd. Dr. Rao later remarked that Chhoti\'s recovery taught her something she now shares '
          'with every trainee: that saving an animal\'s life was often only the first, and sometimes easier, '
          'half of the real work involved.',
      bodyHi: 'जब वन रेंजरों ने युवा हाथी के बच्चे को रिजर्व के किनारे अकेले भटकते हुए पाया, बुरी तरह से निर्जलित और कई दिनों से अपने झुंड से स्पष्ट रूप से अलग, तो अधिकांश अनुभवी वन्यजीव कार्यकर्ताओं ने निजी तौर पर संदेह किया कि वह इस सप्ताह जीवित रह पाएगी। अनाथ हाथी के बच्चे शायद ही कभी अपनी माँ के दूध और निरंतर सामाजिक संपर्क के बिना पनपते थे, और ऐसे युवा जानवर को संभालने के लिए सुसज्जित निकटतम पुनर्वास केंद्र लगभग दो सौ किलोमीटर दूर था।\n\nडॉ. रिज़र्व की पशुचिकित्सक प्रियंवदा राव ने दूर के केंद्र की लंबी, तनावपूर्ण यात्रा को जोखिम में डालने के बजाय बछड़े को हाथ से पालने का प्रयास करने का अपरंपरागत निर्णय लिया। इसका मतलब था हर तीन घंटे, दिन और रात में एक भोजन कार्यक्रम स्थापित करना, एक विशेष रूप से तैयार किए गए दूध के विकल्प का उपयोग करना जिसे हर बार ताजा तैयार करना पड़ता था, और ऐसे कर्मचारियों को ढूंढना जो सफलता की गारंटी के बिना महीनों तक इस थका देने वाली दिनचर्या को बनाए रखने के लिए तैयार हों।\n\nबछिया, जिसे अंततः छोटी नाम दिया गया, उल्लेखनीय रूप से लचीला साबित हुआ लेकिन एक अप्रत्याशित जटिलता पेश की: उसने विशेष रूप से डॉ. राव के प्रति गहरा लगाव बनाना शुरू कर दिया, हर जगह उसका पीछा करना और जब भी अलग हो जाता था तो व्यथित हो जाता था, जिससे टीम चिंतित थी क्योंकि आदर्श रूप से जंगली हाथियों को एक ही इंसान पर अत्यधिक निर्भर नहीं होना चाहिए। डॉ. राव ने धीरे-धीरे अन्य स्टाफ सदस्यों को भोजन देने के चक्र में शामिल किया और, महत्वपूर्ण रूप से, रिजर्व में पहले से ही रह रही एक वृद्ध, सौम्य मादा हाथी के साथ पर्यवेक्षित दौरे की व्यवस्था की, उम्मीद थी कि छोटी अंततः अपनी प्रजाति के प्रति अपना कुछ लगाव स्थानांतरित कर लेगी।\n\nअठारह महीने बाद, छोटी पूरी तरह से रिजर्व में एक छोटे झुंड में एकीकृत हो गई थी, हालांकि वह अभी भी कभी-कभी डॉ. राव की जीप के पास पहुंचती थी जब वह पास से गुजरती थी, अपने गोद लिए हुए झुंड में फिर से शामिल होने से पहले क्षण भर के लिए रुकती थी। डॉ. राव ने बाद में टिप्पणी की कि छोटी की रिकवरी ने उसे कुछ सिखाया जो वह अब हर प्रशिक्षु के साथ साझा करती है: किसी जानवर की जान बचाना अक्सर पहला, और कभी-कभी आसान होता है, इसमें वास्तविक काम का आधा हिस्सा शामिल होता है।',
      bodyGu: '''જ્યારે ફોરેસ્ટ રેન્જરોએ યુવાન હાથીના બચ્ચાને રિઝર્વના કિનારે એકલા ભટકતા જોયું, ત્યારે તે ગંભીર રીતે નિર્જળિત (ડીહાઇડ્રેટેડ) હતું અને સ્પષ્ટપણે ઘણા દિવસોથી તેના ટોળાથી અલગ પડી ગયું હતું. મોટાભાગના અનુભવી વન્યજીવ કાર્યકરોને વ્યક્તિગત રીતે શંકા હતી કે તે આ અઠવાડિયે જીવિત રહી શકશે. અનાથ હાથીના બચ્ચા ભાગ્યે જ તેમની માતાના દૂધ અને સતત સામાજિક સંપર્ક વિના વિકાસ પામે છે, અને આવા યુવાન પ્રાણીને સંભાળવા માટે સુસજ્જ સૌથી નજીકનું પુનર્વસન કેન્દ્ર લગભગ બસો કિલોમીટર દૂર હતું.

રિઝર્વના પશુચિકિત્સક ડો. પ્રિયંવદા રાવે દૂરના કેન્દ્રની લાંબી, તણાવપૂર્ણ યાત્રાનું જોખમ લેવાને બદલે બચ્ચાને પોતાના હાથે ઉછેરવાનો અસામાન્ય નિર્ણય લીધો. આનો અર્થ એ હતો કે દર ત્રણ કલાકે, દિવસ અને રાત માટે એક ભોજન કાર્યક્રમ નક્કી કરવો, વિશેષ રૂપે તૈયાર કરેલા દૂધના વિકલ્પનો ઉપયોગ કરવો જેને દરેક વખતે તાજું બનાવવું પડતું હતું, અને એવા કર્મચારીઓ શોધવા જેઓ સફળતાની કોઈ ગેરંટી વિના મહિનાઓ સુધી આ થકવી નાખતી દિનચર્યા જાળવી રાખવા તૈયાર હોય.

બચ્ચું, જેને અંતે છોટી નામ આપવામાં આવ્યું, નોંધપાત્ર રીતે મજબૂત (સ્થિતિસ્થાપક) સાબિત થયું પરંતુ તેણે એક અણધારી જટિલતા ઊભી કરી: તેણે ખાસ કરીને ડો. રાવ પ્રત્યે ઊંડો લગાવ કેળવવાનું શરૂ કર્યું, દરેક જગ્યાએ તેમની પાછળ ફરવું અને જ્યારે પણ અલગ પડે ત્યારે દુઃખી થઈ જવું. આનાથી ટીમ ચિંતિત હતી કારણ કે આદર્શ રીતે જંગલી હાથીઓ કોઈ એક માણસ પર વધુ પડતા નિર્ભર ન હોવા જોઈએ. ડો. રાવે ધીમે ધીમે અન્ય સ્ટાફ સભ્યોને ભોજન આપવાની પ્રક્રિયામાં સામેલ કર્યા અને, મહત્વપૂર્ણ રીતે, રિઝર્વમાં પહેલેથી જ રહેતી એક વૃદ્ધ, સૌમ્ય માદા હાથી સાથે દેખરેખ હેઠળ મુલાકાતો ગોઠવી, એ આશા સાથે કે છોટી છેવટે તેની પોતાની પ્રજાતિ તરફ તેનો થોડો લગાવ સ્થાનાંતરિત કરશે.

અઢાર મહિના પછી, છોટી સંપૂર્ણપણે રિઝર્વમાં એક નાના ટોળામાં ભળી ગઈ હતી, જોકે તે હજુ પણ ક્યારેક ક્યારેક ડો. રાવની જીપ પાસેથી પસાર થતી વખતે તેની પાસે જતી હતી, તેના દત્તક લીધેલા ટોળામાં ફરી જોડાતા પહેલા ક્ષણભર માટે ઊભી રહેતી. ડો. રાવે પાછળથી ટિપ્પણી કરી કે છોટીની રિકવરીએ તેમને કંઈક શીખવ્યું જે તેઓ હવે દરેક તાલીમાર્થી સાથે શેર કરે છે: પ્રાણીનો જીવ બચાવવો એ ઘણીવાર માત્ર પહેલું, અને ક્યારેક સરળ કામ હોય છે, અસલ કામ તો ત્યારબાદ શરૂ થાય છે.''',
      questions: [
        PracticeQuestion(
          prompt: 'Why did most wildlife workers initially doubt the calf would survive?',
          options: [
            'She showed no signs of injury.',
            'Orphaned elephant calves rarely thrive without their mother\'s milk and social contact, and the rehabilitation centre was far away.',
            'The reserve had no veterinarian available.',
            'She was already fully grown.',
          ],
          correctIndex: 1,
          explanation: 'The passage explains orphaned calves "rarely thrived without their mother\'s milk and constant social contact," and the centre was "nearly two hundred kilometres away."',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'Why did Dr. Rao decide to hand-rear the calf on-site instead of sending her to the rehabilitation centre?',
          options: [
            'The centre refused to accept the calf.',
            'She wanted to avoid the long, stressful journey to the distant centre.',
            'The centre had closed permanently.',
            'She did not know about the centre.',
          ],
          correctIndex: 1,
          explanation: 'The passage states she made this decision "rather than risking the long, stressful journey to the distant centre."',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'What unexpected problem arose during Chhoti\'s recovery?',
          options: [
            'She refused to eat the milk substitute.',
            'She became intensely and worryingly attached to Dr. Rao specifically.',
            'She attacked the other staff members.',
            'She tried to escape the reserve.',
          ],
          correctIndex: 1,
          explanation: 'The passage describes her "intense attachment to Dr. Rao specifically," which worried the team.',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'What does Dr. Rao\'s closing remark suggest about caring for rescued animals?',
          options: [
            'That saving an animal is always the hardest part of the process.',
            'That the emotional and social work of helping an animal readjust can be just as important, or harder, than saving its life initially.',
            'That rescued animals should never be released back to the wild.',
            'That veterinarians should avoid forming any bond with the animals they treat.',
          ],
          correctIndex: 1,
          explanation: 'She remarks that "saving an animal\'s life was often only the first, and sometimes easier, half of the real work involved" — pointing to the social reintegration process.',
          difficulty: Difficulty.hard,
        ),
      ],
      glosses: [
        InlineGloss(word: 'dehydrated', meaningHi: 'निर्जलित (पानी की कमी से पीड़ित)', hiTransliteration: 'nirjalit (paani ki kami se peedit)', meaningGu: 'નિર્જળિત (પાણીની અછતથી પીડિત)', guTransliteration: 'nirjalit (paanini achhatthi peedit)'),
        InlineGloss(word: 'unconventional', meaningHi: 'असामान्य / पारंपरिक न होना', hiTransliteration: 'asamaanya / paramparik na hona', meaningGu: 'અસામાન્ય / પરંપરાગત ન હોય તેવું', guTransliteration: 'asaamaanya / paramparagat na hoy tevu'),
        InlineGloss(word: 'resilient', meaningHi: 'लचीला / जल्दी उबरने वाला', hiTransliteration: 'lachila / jaldi ubarne wala', meaningGu: 'સ્થિતિસ્થાપક / ઝડપથી સાજા થનારું', guTransliteration: 'sthitishaapak / jhadapthi saaja thanaru'),
        InlineGloss(word: 'complication', meaningHi: 'जटिलता', hiTransliteration: 'jatilta', meaningGu: 'જટિલતા / મુશ્કેલી', guTransliteration: 'jatilta / mushkeli'),
        InlineGloss(word: 'integrated', meaningHi: 'शामिल हो गया', hiTransliteration: 'shaamil ho gaya', meaningGu: 'સામેલ થઈ ગયું / એકીકૃત', guTransliteration: 'saamel thai gayu / ekikrut'),
        InlineGloss(word: 'adoptive', meaningHi: 'गोद लिया हुआ', hiTransliteration: 'god liya hua', meaningGu: 'દત્તક લીધેલું', guTransliteration: 'dattak lidhelu'),
      ],
    ),
  ],
);
