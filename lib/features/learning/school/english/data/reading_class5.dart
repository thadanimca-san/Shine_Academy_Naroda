import '../models/chapter.dart' show InlineGloss;
import '../models/practice_question.dart';
import '../models/reading_passage.dart';

const class5Reading = ReadingLibrary(
  id: 'class5_reading',
  title: 'Reading Passages',
  grade: 'Class 5',
  passages: [
    ReadingPassage(
      id: 'class5_reading_potter',
      title: 'The Potter\'s Patience',
      emoji: '🏺',
      grade: 'Class 5',
      difficulty: Difficulty.medium,
      body: 'In a small village near Bhuj, an old potter named Devji had spent forty years shaping clay into '
          'beautiful pots. His grandson, Karan, often watched him work but grew impatient whenever his own '
          'attempts collapsed on the wheel. "I will never learn this," Karan grumbled one evening, pushing '
          'away a lump of clay that had crumbled for the fifth time. Devji did not scold him. Instead, he '
          'placed a fresh lump of clay before his grandson and said, "The wheel does not care how many times '
          'you fail. It only asks whether you will try again." Karan sighed but picked up the clay once more. '
          'Devji showed him, slowly and patiently, how to centre the clay before shaping it, explaining that '
          'rushing was the true reason for most failures. Days turned into weeks. Karan\'s pots wobbled less, '
          'and cracks appeared less often. One monsoon morning, after nearly two months of practice, Karan '
          'lifted a small, evenly shaped water pot off the wheel without a single flaw. His hands were caked '
          'in wet clay, but his face glowed with pride. Devji examined the pot carefully, turning it in the '
          'morning light, and nodded with quiet satisfaction. "You did not become a potter today," he said, '
          '"you simply stopped giving up. That is the real skill." Karan understood then that his grandfather\'s '
          'calm patience, more than any single lesson, was what had truly taught him. From that day, whenever '
          'his younger cousins visited and grew frustrated with their own attempts, Karan would smile and '
          'repeat his grandfather\'s words, passing on the same quiet lesson that had once rescued him from giving up.',
      bodyHi: 'भुज के पास एक छोटे से गाँव में, देवजी नाम के एक बूढ़े कुम्हार ने मिट्टी को सुंदर बर्तनों में आकार देने में चालीस साल बिताए थे। उनका पोता, करण, अक्सर उन्हें काम करते हुए देखता था, लेकिन जब भी उनके खुद के प्रयास विफल हो जाते थे, तो वह अधीर हो जाते थे। "मैं यह कभी नहीं सीख पाऊंगा," करण ने एक शाम बड़बड़ाते हुए मिट्टी के एक ढेर को पांचवीं बार हटाते हुए कहा। देवजी ने उसे डाँटा नहीं। इसके बजाय, उन्होंने अपने पोते के सामने मिट्टी का एक ताज़ा ढेला रखा और कहा, "पहिया को परवाह नहीं है कि आप कितनी बार असफल हुए। यह केवल पूछता है कि क्या आप दोबारा प्रयास करेंगे।" करण ने आह भरी लेकिन एक बार फिर मिट्टी उठा ली। देवजी ने उसे धीरे-धीरे और धैर्यपूर्वक दिखाया कि मिट्टी को आकार देने से पहले उसे कैसे केन्द्रित किया जाए, और समझाया कि जल्दबाजी अधिकांश विफलताओं का असली कारण है। दिन हफ़्तों में बदल गए. करण के बर्तन कम डगमगाते थे और दरारें भी कम दिखाई देती थीं। एक मानसून की सुबह, लगभग दो महीने के अभ्यास के बाद, करण ने बिना किसी दोष के एक छोटे, समान आकार के पानी के बर्तन को पहिये से उठा लिया। उसके हाथ गीली मिट्टी में सने हुए थे, लेकिन उसका चेहरा गर्व से चमक रहा था। देवजी ने बर्तन को सुबह की रोशनी में घुमाकर ध्यान से देखा और शांत संतुष्टि के साथ सिर हिलाया। "आप आज कुम्हार नहीं बने," उन्होंने कहा, "आपने हार मानना ​​बंद कर दिया है। यही असली कौशल है।" करण को तब समझ में आया कि उसके दादाजी का शांत धैर्य, किसी भी एक पाठ से अधिक, वही था जो उसने वास्तव में उसे सिखाया था। उस दिन से, जब भी उसके छोटे चचेरे भाई आते और अपने प्रयासों से निराश हो जाते, करण मुस्कुराता और अपने दादाजी के शब्दों को दोहराता, वही शांत पाठ सुनाता जिसने एक बार उसे हार मानने से बचाया था।',
      bodyGu: '''ભુજ પાસેના એક નાના ગામમાં, દેવજી નામના એક વૃદ્ધ કુંભારે માટીને સુંદર વાસણોનો આકાર આપવામાં ચાલીસ વર્ષ વિતાવ્યા હતા. તેમનો પૌત્ર, કરણ, ઘણીવાર તેમને કામ કરતા જોતો હતો, પરંતુ જ્યારે પણ તેના પોતાના પ્રયત્નો નિષ્ફળ જતા ત્યારે તે અધીરો થઈ જતો. "હું આ ક્યારેય શીખી શકીશ નહીં," કરણે એક સાંજે બડબડાટ કરતા માટીના ઢગલાને પાંચમી વખત હટાવતા કહ્યું. દેવજીએ તેને ઠપકો આપ્યો નહીં. તેના બદલે, તેમણે પોતાના પૌત્રની સામે માટીનો એક તાજો ઢગલો મૂક્યો અને કહ્યું, "ચાકડાને પરવા નથી કે તું કેટલી વાર નિષ્ફળ ગયો. તે માત્ર એટલું જ પૂછે છે કે શું તું ફરી પ્રયત્ન કરીશ." કરણે નિસાસો નાખ્યો પણ ફરી એકવાર માટી હાથમાં લીધી. દેવજીએ તેને ધીમે ધીમે અને ધીરજપૂર્વક બતાવ્યું કે માટીને આકાર આપતા પહેલા તેને કેવી રીતે કેન્દ્રિત કરવી, અને સમજાવ્યું કે ઉતાવળ કરવી એ મોટાભાગની નિષ્ફળતાઓનું સાચું કારણ છે. દિવસો અઠવાડિયામાં ફેરવાઈ ગયા. કરણના વાસણો ઓછા ડગમગતા હતા અને તિરાડો પણ ઓછી દેખાતી હતી. એક ચોમાસાની સવારે, લગભગ બે મહિનાના અભ્યાસ પછી, કરણે કોઈપણ ખામી વિનાના નાના, સમાન આકારના પાણીના વાસણને ચાકડા પરથી ઉઠાવ્યું. તેના હાથ ભીની માટીથી ખરડાયેલા હતા, પરંતુ તેનો ચહેરો ગર્વથી ચમકી રહ્યો હતો. દેવજીએ સવારના પ્રકાશમાં વાસણને ફેરવીને ધ્યાનથી જોયું અને શાંત સંતોષ સાથે માથું હલાવ્યું. "તું આજે કુંભાર નથી બન્યો," તેમણે કહ્યું, "તેં હાર માનવાનું છોડી દીધું છે. એ જ સાચું કૌશલ્ય છે." કરણને ત્યારે સમજાયું કે તેના દાદાની શાંત ધીરજ, કોઈપણ એક પાઠ કરતાં વધુ, તે જ હતી જેણે ખરેખર તેને શીખવ્યું હતું. તે દિવસથી, જ્યારે પણ તેના નાના પિતરાઈ ભાઈ-બહેનો આવતા અને પોતાના પ્રયત્નોથી નિરાશ થઈ જતા, કરણ હસતો અને તેના દાદાના શબ્દોનું પુનરાવર્તન કરતો, એ જ શાંત પાઠ સંભળાવતો જેણે તેને એકવાર હાર માનતા બચાવ્યો હતો.''',
      questions: [
        PracticeQuestion(
          prompt: 'Where did Devji and his grandson Karan live?',
          options: ['Near Bhuj', 'Near Vadodara', 'Near Rajkot', 'Near Surat'],
          correctIndex: 0,
          explanation: 'The passage opens by placing the story "in a small village near Bhuj".',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'Why did Karan feel like giving up at first?',
          options: [
            'He wanted to play instead of working.',
            'His grandfather scolded him harshly.',
            'His pots kept collapsing on the wheel.',
            'He did not like clay.',
          ],
          correctIndex: 2,
          explanation: 'The passage says his attempts "collapsed on the wheel" repeatedly, which frustrated him.',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'What did Devji say was the real reason most pots failed?',
          options: [
            'Not having the right wheel',
            'Using the wrong clay',
            'Rushing instead of centring the clay carefully',
            'Working outdoors in the rain',
          ],
          correctIndex: 2,
          explanation: 'The passage explains that Devji said "rushing was the true reason for most failures".',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'What lesson did Karan pass on to his younger cousins later?',
          options: [
            'That giving up quickly saves time',
            'That clay pots are not worth making anymore',
            'That not giving up, with patience, is the real skill',
            'That only talented people can make pots',
          ],
          correctIndex: 2,
          explanation: 'The final lines show Karan repeating his grandfather\'s words about patience and not giving up.',
          difficulty: Difficulty.medium,
        ),
      ],
      glosses: [
        InlineGloss(word: 'potter', meaningHi: 'कुम्हार', hiTransliteration: 'kumhaar', meaningGu: 'કુંભાર', guTransliteration: 'kumbhaar'),
        InlineGloss(word: 'impatient', meaningHi: 'बेसब्र / अधीर', hiTransliteration: 'besabra / adheer', meaningGu: 'અધીર', guTransliteration: 'adheer'),
        InlineGloss(word: 'grumbled', meaningHi: 'बड़बड़ाया', hiTransliteration: 'badbadaaya', meaningGu: 'બડબડાટ કર્યો', guTransliteration: 'badbadaat karyo'),
        InlineGloss(word: 'crumbled', meaningHi: 'बिखर गया / टूट गया', hiTransliteration: 'bikhar gaya / toot gaya', meaningGu: 'વિખેરાઈ ગયું / તૂટી ગયું', guTransliteration: 'vikheraai gayu / tuti gayu'),
        InlineGloss(word: 'scold', meaningHi: 'डांटना', hiTransliteration: 'daantna', meaningGu: 'ઠપકો આપવો', guTransliteration: 'thapko aapvo'),
        InlineGloss(word: 'centre the clay', meaningHi: 'मिट्टी को बीच में जमाना', hiTransliteration: 'mitti ko beech mein jamaana', meaningGu: 'માટીને કેન્દ્રમાં ગોઠવવી', guTransliteration: 'matine kendrama gothvavi'),
        InlineGloss(word: 'wobbled', meaningHi: 'डगमगाए', hiTransliteration: 'dagmagaaye', meaningGu: 'ડગમગ્યું', guTransliteration: 'dagmagyu'),
        InlineGloss(word: 'flaw', meaningHi: 'खामी / कमी', hiTransliteration: 'khaami / kami', meaningGu: 'ખામી / ત્રુટિ', guTransliteration: 'khaami / truti'),
        InlineGloss(word: 'quiet satisfaction', meaningHi: 'शांत संतोष', hiTransliteration: 'shaant santosh', meaningGu: 'શાંત સંતોષ', guTransliteration: 'shaant santosh'),
        InlineGloss(word: 'frustrated', meaningHi: 'निराश', hiTransliteration: 'niraash', meaningGu: 'નિરાશ / હતાશ', guTransliteration: 'niraash / hataash'),
      ],
    ),
    ReadingPassage(
      id: 'class5_reading_lost_wallet',
      title: 'The Wallet on Platform Two',
      emoji: '👛',
      grade: 'Class 5',
      difficulty: Difficulty.medium,
      body: 'Aisha and her older brother Zaid were waiting for their train at a busy railway station when '
          'Aisha spotted a brown leather wallet lying near a bench on platform two. She picked it up and '
          'opened it carefully. Inside were several crisp banknotes, a railway pass, and a photograph of a '
          'smiling family. Zaid immediately suggested they keep the money and simply hand in the empty wallet '
          'later, arguing that no one would ever know the difference. Aisha frowned and shook her head. "That '
          'money belongs to someone else," she said firmly. "Imagine how worried they must be feeling right '
          'now." Zaid grumbled that they could have bought sweets and comics with it, but Aisha insisted they '
          'find the owner immediately. They walked along the platform, asking passengers if anyone had lost a '
          'wallet, until an anxious-looking man came rushing toward them, patting his pockets frantically. When '
          'he saw the wallet in Aisha\'s hands, his shoulders relaxed with relief. He explained that the money '
          'was meant for his daughter\'s school fees, which were due that very afternoon. Overjoyed, he thanked '
          'the children again and again and offered them a reward, but Aisha politely refused, saying that '
          'doing the right thing was reward enough. As their train finally arrived, Zaid admitted quietly that '
          'his sister had been right all along, and that the man\'s relieved smile felt better than any sweets '
          'or comics ever could have.',
      bodyHi: 'आयशा और उसका बड़ा भाई ज़ैद एक व्यस्त रेलवे स्टेशन पर अपनी ट्रेन का इंतज़ार कर रहे थे, तभी आयशा ने प्लेटफ़ॉर्म दो पर एक बेंच के पास एक भूरे रंग का चमड़े का बटुआ पड़ा हुआ देखा। उसने उसे उठाया और ध्यान से खोला। अंदर कई साफ-सुथरे नोट, एक रेलवे पास और एक मुस्कुराते हुए परिवार की तस्वीर थी। ज़ैद ने तुरंत सुझाव दिया कि वे पैसे रख लें और बाद में खाली बटुआ सौंप दें, यह तर्क देते हुए कि किसी को भी अंतर पता नहीं चलेगा। आयशा ने भौंहें चढ़ा लीं और सिर हिला दिया। "वह पैसा किसी और का है," उसने दृढ़ता से कहा। "कल्पना कीजिए कि वे इस समय कितना चिंतित महसूस कर रहे होंगे।" ज़ैद ने शिकायत की कि वे इसके साथ मिठाइयाँ और कॉमिक्स खरीद सकते थे, लेकिन आयशा ने जोर देकर कहा कि वे मालिक को तुरंत खोजें। वे प्लेटफ़ॉर्म पर चलते रहे और यात्रियों से पूछते रहे कि क्या किसी का बटुआ खो गया है, तभी एक चिंतित दिखने वाला आदमी उनकी ओर दौड़ता हुआ आया और अपनी जेबें जोर-जोर से थपथपाने लगा। जब उसने आयशा के हाथ में बटुआ देखा, तो उसके कंधे राहत से ढीले हो गए। उन्होंने बताया कि यह पैसा उनकी बेटी की स्कूल फीस के लिए था, जो उसी दोपहर को देय थी। बहुत खुश होकर, उसने बच्चों को बार-बार धन्यवाद दिया और उन्हें इनाम देने की पेशकश की, लेकिन आयशा ने विनम्रता से यह कहते हुए मना कर दिया कि सही काम करना ही काफी इनाम है। जैसे ही उनकी ट्रेन पहुंची, ज़ैद ने चुपचाप स्वीकार किया कि उसकी बहन बिल्कुल सही थी, और उस आदमी की राहत भरी मुस्कान किसी भी मिठाई या कॉमिक्स से बेहतर महसूस हुई।',
      bodyGu: '''આયશા અને તેનો મોટો ભાઈ ઝૈદ એક વ્યસ્ત રેલ્વે સ્ટેશન પર તેમની ટ્રેનની રાહ જોઈ રહ્યા હતા, ત્યારે જ આયશાએ પ્લેટફોર્મ બે પર એક બેંચ પાસે એક ભૂરા રંગનું ચામડાનું પાકીટ પડેલું જોયું. તેણે તેને ઉપાડ્યું અને ધ્યાનથી ખોલ્યું. અંદર ઘણા નવા-નવા કડક નોટ, એક રેલ્વે પાસ અને એક હસતા પરિવારનો ફોટો હતો. ઝૈદે તરત જ સૂચન કર્યું કે તેઓ પૈસા રાખી લે અને પછીથી ખાલી પાકીટ જમા કરાવી દે, એમ કહીને કે કોઈને પણ તફાવત ખબર પડશે નહીં. આયશાએ ભવાં ચડાવ્યા અને માથું હલાવ્યું. "તે પૈસા કોઈ બીજાના છે," તેણે મક્કમતાથી કહ્યું. "કલ્પના કરો કે તેઓ આ સમયે કેટલા ચિંતિત અનુભવતા હશે." ઝૈદે ફરિયાદ કરી કે તેઓ તેની સાથે મીઠાઈઓ અને કોમિક્સ ખરીદી શકતા હતા, પરંતુ આયશાએ ભારપૂર્વક કહ્યું કે તેઓ માલિકને તરત જ શોધી કાઢે. તેઓ પ્લેટફોર્મ પર ચાલતા રહ્યા અને મુસાફરોને પૂછતા રહ્યા કે શું કોઈનું પાકીટ ખોવાઈ ગયું છે, ત્યારે જ એક ચિંતિત દેખાતો માણસ તેમની તરફ દોડતો આવ્યો અને પોતાના ખિસ્સા જોર-જોરથી થપથપાવવા લાગ્યો. જ્યારે તેણે આયશાના હાથમાં પાકીટ જોયું, ત્યારે તેના ખભા રાહતથી ઢીલા થઈ ગયા. તેણે જણાવ્યું કે આ પૈસા તેની દીકરીની સ્કૂલ ફી માટે હતા, જે એ જ બપોરે ચૂકવવાની હતી. ખૂબ ખુશ થઈને, તેણે બાળકોનો વારંવાર આભાર માન્યો અને તેમને ઈનામ આપવાની રજૂઆત કરી, પરંતુ આયશાએ નમ્રતાપૂર્વક એમ કહીને ના પાડી દીધી કે સાચું કામ કરવું એ જ પૂરતું ઈનામ છે. જેમ જ તેમની ટ્રેન આવી, ઝૈદે ચૂપચાપ સ્વીકાર્યું કે તેની બહેન બિલકુલ સાચી હતી, અને તે માણસની રાહત ભરેલી મુસ્કાન કોઈપણ મીઠાઈ અથવા કોમિક્સ કરતા વધુ સારી અનુભવાઈ.''',
      questions: [
        PracticeQuestion(
          prompt: 'Where did Aisha find the wallet?',
          options: ['On platform two at a railway station', 'On a bus', 'Inside a shop', 'In a park'],
          correctIndex: 0,
          explanation: 'The passage says Aisha "spotted a brown leather wallet lying near a bench on platform two".',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'What did Zaid initially want to do with the wallet?',
          options: [
            'Throw it away',
            'Give all the money to the poor',
            'Keep the money and hand in the empty wallet',
            'Give it to the police immediately',
          ],
          correctIndex: 2,
          explanation: 'The passage says Zaid suggested keeping the money and returning only the empty wallet.',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'Why was the money in the wallet important to its owner?',
          options: [
            'It was a gift for his own birthday.',
            'It was meant for his daughter\'s school fees due that afternoon.',
            'It was meant to buy a train ticket.',
            'It was his salary for the whole year.',
          ],
          correctIndex: 1,
          explanation: 'The passage explains the money "was meant for his daughter\'s school fees, which were due that very afternoon".',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'How did Zaid feel by the end of the story?',
          options: [
            'He wished they had kept the money.',
            'He was disappointed in the man\'s reaction.',
            'Angry that they missed buying sweets',
            'He admitted his sister had been right all along.',
          ],
          correctIndex: 3,
          explanation: 'The last sentence says Zaid "admitted quietly that his sister had been right all along".',
          difficulty: Difficulty.medium,
        ),
      ],
      glosses: [
        InlineGloss(word: 'leather', meaningHi: 'चमड़ा', hiTransliteration: 'chamda', meaningGu: 'ચામડું', guTransliteration: 'chaamdu'),
        InlineGloss(word: 'crisp banknotes', meaningHi: 'नए-नए, कड़क नोट', hiTransliteration: 'naye-naye, kadak note', meaningGu: 'નવા-નવા, કડક નોટ', guTransliteration: 'nava-nava, kadak note'),
        InlineGloss(word: 'anxious-looking', meaningHi: 'चिंतित दिखने वाला', hiTransliteration: 'chintit dikhne waala', meaningGu: 'ચિંતિત દેખાતો', guTransliteration: 'chintit dekhato'),
        InlineGloss(word: 'frantically', meaningHi: 'घबराहट में तेज़ी से', hiTransliteration: 'ghabrahat mein tezi se', meaningGu: 'ગભરાહટમાં ઝડપથી', guTransliteration: 'gabhrahatma jhadapthi'),
        InlineGloss(word: 'relief', meaningHi: 'राहत', hiTransliteration: 'raahat', meaningGu: 'રાહત', guTransliteration: 'rahat'),
        InlineGloss(word: 'overjoyed', meaningHi: 'बहुत खुश', hiTransliteration: 'bahut khush', meaningGu: 'ખૂબ ખુશ', guTransliteration: 'khoob khush'),
        InlineGloss(word: 'reward', meaningHi: 'इनाम', hiTransliteration: 'inaam', meaningGu: 'ઈનામ', guTransliteration: 'inaam'),
        InlineGloss(word: 'politely refused', meaningHi: 'विनम्रता से मना कर दिया', hiTransliteration: 'vinamrata se mana kar diya', meaningGu: 'નમ્રતાપૂર્વક ના પાડી દીધી', guTransliteration: 'namratapoorvak na paadi didhi'),
        InlineGloss(word: 'admitted', meaningHi: 'मान लिया / स्वीकार किया', hiTransliteration: 'maan liya / sweekaar kiya', meaningGu: 'સ્વીકાર્યું / માની લીધું', guTransliteration: 'svikaaryu / maani lidhu'),
      ],
    ),
    ReadingPassage(
      id: 'class5_reading_riverbank',
      title: 'Saving the Riverbank',
      emoji: '🌱',
      grade: 'Class 5',
      difficulty: Difficulty.medium,
      body: 'Every year during the monsoon, the river beside Nandpur village used to flood the nearby fields, '
          'washing away crops and topsoil. Govind sir, the new science teacher at the village school, noticed '
          'that the riverbank had almost no trees left, since most had been cut down over the years for '
          'firewood and timber. He explained to his students that tree roots normally hold soil together, and '
          'without them, the loose earth simply slid into the river during heavy rain. Inspired by his lesson, '
          'a group of students led by a girl named Farida decided to start a project to protect their village. '
          'They collected sapling seeds of native trees, borrowed spades from their families, and spent every '
          'Sunday morning for three months planting rows of young trees along the riverbank. Some villagers '
          'were doubtful at first, wondering whether a handful of children could really make a difference '
          'against something as powerful as a flooding river. Farida\'s group did not argue; they simply kept '
          'watering the saplings every week, even during the dry months when the sun scorched the fields. Two '
          'years later, when the monsoon rains returned heavily, the young trees had grown tall enough for '
          'their roots to grip the soil firmly. The flooding that year was far less severe, and very little '
          'farmland was damaged. The village elders, who had once doubted the children, now proudly called the '
          'strip of trees "Farida\'s Forest." Other nearby villages heard about the project and began planting '
          'their own riverbank trees, hoping to prevent the same damage the rains had caused for generations.',
      bodyHi: 'हर साल मानसून के दौरान, नंदपुर गांव के बगल की नदी आसपास के खेतों में बाढ़ ला देती थी, जिससे फसलें और ऊपरी मिट्टी बह जाती थी। गाँव के स्कूल में नए विज्ञान शिक्षक, गोविंद सर ने देखा कि नदी के किनारे लगभग कोई पेड़ नहीं बचा था, क्योंकि पिछले कुछ वर्षों में अधिकांश को जलाऊ लकड़ी और इमारती लकड़ी के लिए काट दिया गया था। उन्होंने अपने छात्रों को समझाया कि पेड़ों की जड़ें आम तौर पर मिट्टी को एक साथ रखती हैं, और उनके बिना, भारी बारिश के दौरान ढीली मिट्टी आसानी से नदी में बह जाती है। उनके पाठ से प्रेरित होकर, फ़रीदा नाम की एक लड़की के नेतृत्व में छात्रों के एक समूह ने अपने गाँव की सुरक्षा के लिए एक परियोजना शुरू करने का फैसला किया। उन्होंने देशी पेड़ों के बीज एकत्र किए, अपने परिवारों से कुदाल उधार ली और तीन महीने तक हर रविवार की सुबह नदी के किनारे युवा पेड़ों की कतारें लगाते रहे। कुछ ग्रामीण पहले तो आशंकित थे, सोच रहे थे कि क्या मुट्ठी भर बच्चे बाढ़ जैसी शक्तिशाली नदी के खिलाफ वास्तव में कोई बदलाव ला सकते हैं। फरीदा के समूह ने बहस नहीं की; वे हर हफ्ते पौधों को पानी देते रहे, यहाँ तक कि सूखे महीनों के दौरान भी जब सूरज खेतों को झुलसा देता था। दो साल बाद, जब मानसून की भारी बारिश हुई, तो युवा पेड़ इतने ऊँचे हो गए कि उनकी जड़ें मिट्टी को मजबूती से पकड़ने लगीं। उस वर्ष बाढ़ बहुत कम गंभीर थी, और बहुत कम कृषि भूमि क्षतिग्रस्त हुई थी। गाँव के बुजुर्ग, जो कभी बच्चों पर संदेह करते थे, अब गर्व से पेड़ों की पट्टी को "फरीदा का जंगल" कहते हैं। आस-पास के अन्य गाँवों ने इस परियोजना के बारे में सुना और अपने स्वयं के नदी तट पर पेड़ लगाना शुरू कर दिया, इस उम्मीद में कि बारिश के कारण पीढ़ियों से होने वाली क्षति को रोका जा सके।',
      bodyGu: '''દર વર્ષે ચોમાસા દરમિયાન, નંદપુર ગામની બાજુમાં આવેલી નદીમાં પૂર આવતું હતું, જેનાથી પાક અને ઉપરની માટી ધોવાઈ જતી હતી. ગામની શાળાના નવા વિજ્ઞાન શિક્ષક, ગોવિંદ સરે જોયું કે નદીના કિનારે લગભગ કોઈ વૃક્ષો બચ્યા ન હતા, કારણ કે મોટાભાગનાને બળતણ અને ઈમારતી લાકડા માટે કાપી નાખવામાં આવ્યા હતા. તેમણે તેમના વિદ્યાર્થીઓને સમજાવ્યું કે વૃક્ષોના મૂળ સામાન્ય રીતે માટીને જકડી રાખે છે, અને તેમના વિના, ભારે વરસાદ દરમિયાન ઢીલી માટી સરળતાથી નદીમાં વહી જાય છે. તેમના પાઠથી પ્રેરિત થઈને, ફરીદા નામની એક છોકરીના નેતૃત્વમાં વિદ્યાર્થીઓના એક જૂથે તેમના ગામની સુરક્ષા માટે એક પ્રોજેક્ટ શરૂ કરવાનો નિર્ણય લીધો. તેમણે દેશી વૃક્ષોના બીજ ભેગા કર્યા, તેમના પરિવારો પાસેથી કોદાળીઓ ઉધાર લીધી અને ત્રણ મહિના સુધી દર રવિવારે સવારે નદીના કિનારે નાના વૃક્ષોની હારમાળાઓ વાવી. કેટલાક ગ્રામજનો પહેલા તો શંકાસ્પદ હતા, એ વિચારીને કે શું મુઠ્ઠીભર બાળકો પૂર જેવી શક્તિશાળી નદી સામે ખરેખર કોઈ ફેરફાર લાવી શકે છે. ફરીદાના જૂથે દલીલ ન કરી; તેઓ દર અઠવાડિયે છોડને પાણી આપતા રહ્યા, સૂકા મહિનાઓ દરમિયાન પણ જ્યારે સૂર્ય ખેતરોને દઝાડી દેતો હતો. બે વર્ષ પછી, જ્યારે ચોમાસાનો ભારે વરસાદ પાછો ફર્યો, ત્યારે નાના વૃક્ષો એટલા ઊંચા થઈ ગયા હતા કે તેમના મૂળ માટીને મજબૂતાઈથી પકડી શકતા હતા. તે વર્ષે પૂર ખૂબ ઓછું ગંભીર હતું, અને ખૂબ જ ઓછી ખેતીલાયક જમીનને નુકસાન થયું હતું. ગામના વડીલો, જેઓ ક્યારેક બાળકો પર શંકા કરતા હતા, તેઓ હવે ગર્વથી વૃક્ષોની પટ્ટીને "ફરીદાનું જંગલ" કહે છે. આસપાસના અન્ય ગામોએ આ પ્રોજેક્ટ વિશે સાંભળ્યું અને વરસાદને કારણે પેઢીઓથી થતા નુકસાનને અટકાવવાની આશા સાથે પોતાના નદી કિનારે વૃક્ષો વાવવાનું શરૂ કર્યું.''',
      questions: [
        PracticeQuestion(
          prompt: 'Why did the river near Nandpur village flood the fields every monsoon?',
          options: [
            'Because the villagers built a dam incorrectly',
            'Because the river was too narrow',
            'Because the fields were built too close to the school',
            'Because there were almost no trees left to hold the soil together',
          ],
          correctIndex: 3,
          explanation: 'The passage explains that without tree roots to hold it, "the loose earth simply slid into the river during heavy rain".',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'Who led the group of students that started the tree-planting project?',
          options: ['The school principal', 'Govind sir', 'A village elder', 'Farida'],
          correctIndex: 3,
          explanation: 'The passage says "a group of students led by a girl named Farida decided to start a project".',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'How did the students care for the saplings, even during difficult months?',
          options: [
            'They watered them every week, even during the dry months.',
            'They ignored them until the rains came.',
            'They asked the government to water them.',
            'They planted new ones every week instead of watering.',
          ],
          correctIndex: 0,
          explanation: 'The passage says the group "kept watering the saplings every week, even during the dry months".',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'What did the village elders call the strip of trees after two years?',
          options: ['The Green Wall', 'The Monsoon Line', 'The School Garden', 'Farida\'s Forest'],
          correctIndex: 3,
          explanation: 'The passage says the elders "now proudly called the strip of trees \'Farida\'s Forest\'".',
          difficulty: Difficulty.easy,
        ),
      ],
      glosses: [
        InlineGloss(word: 'monsoon', meaningHi: 'बारिश का मौसम', hiTransliteration: 'baarish ka mausam', meaningGu: 'ચોમાસું', guTransliteration: 'chomasu'),
        InlineGloss(word: 'topsoil', meaningHi: 'ऊपरी मिट्टी', hiTransliteration: 'oopari mitti', meaningGu: 'ઉપરની માટી', guTransliteration: 'uparni mati'),
        InlineGloss(word: 'firewood', meaningHi: 'जलाने की लकड़ी', hiTransliteration: 'jalaane ki lakdi', meaningGu: 'બળતણ', guTransliteration: 'baltan'),
        InlineGloss(word: 'timber', meaningHi: 'लकड़ी / इमारती लकड़ी', hiTransliteration: 'lakdi / imaarati lakdi', meaningGu: 'ઈમારતી લાકડું', guTransliteration: 'imarati lakdu'),
        InlineGloss(word: 'sapling', meaningHi: 'पौधे का छोटा पेड़', hiTransliteration: 'paudhe ka chhota ped', meaningGu: 'નાનો છોડ', guTransliteration: 'nano chhod'),
        InlineGloss(word: 'spades', meaningHi: 'फावड़े', hiTransliteration: 'faavde', meaningGu: 'કોદાળીઓ', guTransliteration: 'kodalio'),
        InlineGloss(word: 'doubtful', meaningHi: 'संदेह करने वाला', hiTransliteration: 'sandeh karne waala', meaningGu: 'શંકાસ્પદ', guTransliteration: 'shankaspad'),
        InlineGloss(word: 'scorched', meaningHi: 'झुलसाया / तपाया', hiTransliteration: 'jhulsaaya / tapaaya', meaningGu: 'દઝાડી દીધું', guTransliteration: 'dazadi didhu'),
        InlineGloss(word: 'severe', meaningHi: 'गंभीर / भयंकर', hiTransliteration: 'gambheer / bhayankar', meaningGu: 'ગંભીર', guTransliteration: 'gambhir'),
      ],
    ),
    ReadingPassage(
      id: 'class5_reading_kite_team',
      title: 'The Kite That Needed a Team',
      emoji: '🪁',
      grade: 'Class 5',
      difficulty: Difficulty.medium,
      body: 'Every January, the rooftops of Naroda buzzed with excitement during the kite festival, and Vikram '
          'had been determined to build the biggest kite anyone in his lane had ever flown. He spent two weeks '
          'cutting bamboo strips, stretching colourful paper, and knotting string, refusing help from anyone, '
          'convinced that a truly great kite had to be made entirely alone. On the morning of the festival, '
          'Vikram climbed to his rooftop, holding his enormous kite proudly, only to discover that flying '
          'something so large required far more than one pair of hands. The moment the wind caught the kite, '
          'it lurched wildly, nearly dragging him toward the rooftop\'s edge. His friend Tanvi, watching from '
          'the next rooftop, called out that she would come over to help hold the spool steady. Vikram, still '
          'stubborn, insisted he could manage alone, but after the kite crashed twice into a neighbour\'s '
          'clothesline, he reluctantly agreed to let her help. Together, Tanvi held the spool firmly while '
          'Vikram controlled the string\'s tension, and slowly, carefully, they worked out a rhythm between them. '
          'Two more friends, Om and Sanaa, soon joined, one steadying the kite\'s tail and another watching for '
          'gusts of wind from across the rooftops. With four of them working together, the enormous kite '
          'finally rose steadily into the sky, higher than any other kite on the lane that day. Vikram, breathless '
          'and grinning, admitted that he could never have managed it by himself. As the kite soared above '
          'Naroda, he realised that some achievements are not meant to be accomplished alone, and that sharing '
          'the effort had made the moment far more joyful than any solo triumph could have been.',
      bodyHi: 'हर जनवरी में, पतंग उत्सव के दौरान नरोदा की छतें उत्साह से भर जाती थीं, और विक्रम अपनी गली में अब तक उड़ाई गई सबसे बड़ी पतंग बनाने के लिए कृतसंकल्प थे। उन्होंने बांस की पट्टियों को काटने, रंगीन कागज खींचने और डोरी गांठने में दो सप्ताह बिताए, किसी की भी मदद लेने से इनकार कर दिया, और आश्वस्त हो गए कि वास्तव में एक महान पतंग पूरी तरह से अकेले ही बनाई जानी चाहिए। त्योहार की सुबह, विक्रम अपनी विशाल पतंग को गर्व से पकड़कर अपनी छत पर चढ़ गया, लेकिन उसे पता चला कि इतनी बड़ी चीज़ को उड़ाने के लिए एक जोड़ी से अधिक हाथों की आवश्यकता होती है। जैसे ही हवा ने पतंग को अपनी चपेट में लिया, वह बेतहाशा उछल पड़ी और उसे लगभग छत के किनारे तक खींच ले गई। उसकी दोस्त तन्वी, जो बगल की छत से देख रही थी, ने आवाज़ लगाई कि वह स्पूल को स्थिर रखने में मदद करने के लिए आएगी। विक्रम, जो अभी भी जिद्दी था, ने जोर देकर कहा कि वह अकेले ही काम संभाल सकता है, लेकिन जब पतंग दो बार पड़ोसी की कपड़े की डोरी से टकराई, तो वह अनिच्छा से उसकी मदद करने के लिए तैयार हो गया। साथ में, तन्वी ने स्पूल को मजबूती से पकड़ लिया जबकि विक्रम ने स्ट्रिंग के तनाव को नियंत्रित किया, और धीरे-धीरे, सावधानी से, उन्होंने अपने बीच एक लय बना ली। दो और दोस्त, ओम और सना, जल्द ही शामिल हो गए, एक पतंग की पूंछ को स्थिर कर रहा था और दूसरा छतों के पार से हवा के झोंकों का इंतजार कर रहा था। उनमें से चार के एक साथ काम करने से, अंततः विशाल पतंग तेजी से आकाश में उड़ गई, जो उस दिन गली में किसी भी अन्य पतंग की तुलना में अधिक ऊंची थी। विक्रम ने हांफते हुए और मुस्कुराते हुए स्वीकार किया कि वह इसे अकेले कभी भी प्रबंधित नहीं कर सकता था। जैसे ही पतंग नरोदा के ऊपर उड़ी, उसे एहसास हुआ कि कुछ उपलब्धियाँ अकेले हासिल करने के लिए नहीं होती हैं, और प्रयास साझा करने से वह क्षण किसी भी एकल विजय की तुलना में कहीं अधिक आनंददायक हो सकता था।',
      bodyGu: '''દર જાન્યુઆરીમાં, પતંગ ઉત્સવ દરમિયાન નરોડાની છતો ઉત્સાહથી ભરાઈ જતી હતી, અને વિક્રમ પોતાની ગલીમાં અત્યાર સુધી ઉડાડવામાં આવેલી સૌથી મોટી પતંગ બનાવવા માટે કૃતનિશ્ચયી હતો. તેણે વાંસની પટ્ટીઓ કાપવામાં, રંગીન કાગળ ખેંચવામાં અને દોરી બાંધવામાં બે અઠવાડિયા વિતાવ્યા, કોઈની પણ મદદ લેવાનો ઇનકાર કર્યો, અને ખાતરીપૂર્વક માનતો હતો કે ખરેખર એક મહાન પતંગ સંપૂર્ણપણે એકલા જ બનાવવી જોઈએ. તહેવારની સવારે, વિક્રમ પોતાની વિશાળ પતંગને ગર્વથી પકડીને પોતાની છત પર ચઢી ગયો, પરંતુ તેને ખબર પડી કે આટલી મોટી વસ્તુને ઉડાડવા માટે એક જોડી કરતા વધુ હાથની જરૂર પડે છે. જેવી હવાએ પતંગને પોતાની લપેટમાં લીધી, તે બેતહાશા ઉછળી પડી અને તેને લગભગ છતની કિનારી સુધી ખેંચી ગઈ. તેની મિત્ર તન્વી, જે બાજુની છત પરથી જોઈ રહી હતી, તેણે બૂમ પાડી કે તે ફિરકીને સ્થિર રાખવામાં મદદ કરવા માટે આવશે. વિક્રમ, જે હજુ પણ જિદ્દી હતો, તેણે ભારપૂર્વક કહ્યું કે તે એકલો જ કામ સંભાળી શકે છે, પરંતુ જ્યારે પતંગ બે વખત પડોશીની કપડાં સુકવવાની દોરી સાથે ટકરાઈ, ત્યારે તે અનિચ્છાએ તેની મદદ કરવા માટે તૈયાર થઈ ગયો. સાથે મળીને, તન્વીએ ફિરકીને મજબૂતીથી પકડી લીધી જ્યારે વિક્રમે દોરીના તણાવને નિયંત્રિત કર્યો, અને ધીરે-ધીરે, સાવધાનીથી, તેમણે પોતાની વચ્ચે એક લય બનાવી લીધી. બે વધુ મિત્રો, ઓમ અને સના, જલ્દી જ જોડાઈ ગયા, એક પતંગની પૂંછડીને સ્થિર કરી રહ્યો હતો અને બીજો છતોની પેલે પારથી આવતા હવાના ઝપાટાની રાહ જોઈ રહ્યો હતો. તેઓ ચારના એકસાથે કામ કરવાથી, અંતે વિશાળ પતંગ ઝડપથી આકાશમાં ઉડી ગઈ, જે તે દિવસે ગલીમાં અન્ય કોઈપણ પતંગ કરતા વધુ ઊંચી હતી. વિક્રમે હાંફતા અને મુસ્કુરાતા સ્વીકાર્યું કે તે તેને ક્યારેય એકલો સંભાળી શક્યો ન હોત. જેવી પતંગ નરોડાની ઉપર ઉડી, તેને અહેસાસ થયો કે કેટલીક સિદ્ધિઓ એકલા હાંસલ કરવા માટે હોતી નથી, અને પ્રયત્નો વહેંચવાથી તે ક્ષણ કોઈપણ એકલ વિજય કરતા ક્યાંય વધુ આનંદદાયક હોઈ શકે છે.''',
      questions: [
        PracticeQuestion(
          prompt: 'What was Vikram determined to do before the festival?',
          options: [
            'Buy the most expensive kite in the market',
            'Win a cooking competition',
            'Teach his friends how to make kites',
            'Build the biggest kite anyone in his lane had flown',
          ],
          correctIndex: 3,
          explanation: 'The passage says Vikram "had been determined to build the biggest kite anyone in his lane had ever flown".',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'Why did Vikram initially refuse help from his friends?',
          options: [
            'His friends were busy with their own kites.',
            'He did not have any friends nearby.',
            'He believed a great kite had to be made and flown entirely alone.',
            'He was too shy to ask for help.',
          ],
          correctIndex: 2,
          explanation: 'The passage says he was "convinced that a truly great kite had to be made entirely alone".',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'What made Vikram finally accept help from Tanvi?',
          options: [
            'The kite crashed twice into a neighbour\'s clothesline.',
            'He got bored of flying it alone.',
            'His mother told him to share.',
            'Tanvi offered him money for the kite.',
          ],
          correctIndex: 0,
          explanation: 'The passage says that after the kite "crashed twice into a neighbour\'s clothesline", he reluctantly agreed to accept help.',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'What did Vikram realise by the end of the story?',
          options: [
            'That kites are too difficult to fly in Naroda',
            'That flying alone is always better',
            'That Tanvi, Om, and Sanaa were better kite-makers than him',
            'That some achievements are more joyful when shared with others',
          ],
          correctIndex: 3,
          explanation: 'The passage ends by saying he realised "sharing the effort had made the moment far more joyful than any solo triumph could have been".',
          difficulty: Difficulty.medium,
        ),
      ],
      glosses: [
        InlineGloss(word: 'bamboo', meaningHi: 'बांस', hiTransliteration: 'baans', meaningGu: 'વાંસ', guTransliteration: 'vaans'),
        InlineGloss(word: 'knotting', meaningHi: 'गांठ बांधना', hiTransliteration: 'gaanth baandhna', meaningGu: 'ગાંઠ બાંધવી', guTransliteration: 'gaanth baandhvi'),
        InlineGloss(word: 'lurched', meaningHi: 'अचानक झटके से हिला', hiTransliteration: 'achaanak jhatke se hila', meaningGu: 'અચાનક ઝટકાથી હલવું', guTransliteration: 'achaanak jhatkaathi halvu'),
        InlineGloss(word: 'stubborn', meaningHi: 'ज़िद्दी', hiTransliteration: 'ziddi', meaningGu: 'જિદ્દી', guTransliteration: 'jiddi'),
        InlineGloss(word: 'clothesline', meaningHi: 'कपड़े सुखाने की डोरी', hiTransliteration: 'kapde sukhaane ki dori', meaningGu: 'કપડાં સુકવવાની દોરી', guTransliteration: 'kapda sukavavani dori'),
        InlineGloss(word: 'reluctantly', meaningHi: 'अनमने मन से', hiTransliteration: 'anmane man se', meaningGu: 'અનિચ્છાએ', guTransliteration: 'anichchhae'),
        InlineGloss(word: 'spool', meaningHi: 'फिरकी / चरखी', hiTransliteration: 'firki / charkhi', meaningGu: 'ફિરકી', guTransliteration: 'firki'),
        InlineGloss(word: 'tension', meaningHi: 'खिंचाव / तनाव', hiTransliteration: 'khinchaav / tanaav', meaningGu: 'ખેંચાણ / તણાવ', guTransliteration: 'khenchaan / tanaav'),
        InlineGloss(word: 'gusts of wind', meaningHi: 'हवा के तेज़ झोंके', hiTransliteration: 'hawa ke tez jhonke', meaningGu: 'હવાના તેજ ઝપાટા', guTransliteration: 'havaana tej jhapaata'),
        InlineGloss(word: 'triumph', meaningHi: 'जीत / विजय', hiTransliteration: 'jeet / vijay', meaningGu: 'જીત / વિજય', guTransliteration: 'jeet / vijay'),
      ],
    ),
    ReadingPassage(
      id: 'class5_reading_broken_arm',
      title: 'The Race with a Broken Arm',
      emoji: '🏃',
      grade: 'Class 5',
      difficulty: Difficulty.medium,
      body: 'Meera had trained for the district running championship for almost six months, waking up before '
          'sunrise every day to practise on the dusty ground behind her school in Anand. Three weeks before the '
          'race, while helping her mother carry water, she slipped on the wet steps and fractured her left arm. '
          'The doctor fitted a heavy plaster cast and told her firmly that she must rest and avoid any strain '
          'until it healed completely. Meera was devastated, certain that her months of early mornings and '
          'aching legs had been wasted. Her coach, Kashish ma\'am, visited her at home and reminded her that a '
          'broken arm did not mean broken legs, and that running mainly depended on strong legs and steady '
          'breathing, not her arms. Encouraged, Meera began gentle practice again, carefully balancing her cast '
          'against her body as she jogged short distances, gradually increasing her speed as the days passed. '
          'Some classmates whispered that she should simply withdraw from the championship, since competing '
          'with an injury seemed pointless and even risky. Meera ignored their doubts and kept training, wearing '
          'a sling to protect her arm during the final stretch of practice. On the day of the race, she stood at '
          'the starting line with her arm still bandaged, her heart pounding louder than the starting whistle. '
          'She ran with careful, determined strides, ignoring the throbbing ache whenever her arm swung too '
          'fast. Meera crossed the finish line in third place, not first, but the loudest cheer of the day came '
          'from her coach and classmates, who understood exactly how much courage that bronze medal represented.',
      bodyHi: 'मीरा ने जिला दौड़ चैंपियनशिप के लिए लगभग छह महीने तक प्रशिक्षण लिया था, वह प्रतिदिन सूर्योदय से पहले उठकर आनंद में अपने स्कूल के पीछे धूल भरी जमीन पर अभ्यास करती थी। दौड़ से तीन सप्ताह पहले, अपनी माँ को पानी ढोने में मदद करते समय, वह गीली सीढ़ियों पर फिसल गई और उसके बाएँ हाथ में फ्रैक्चर हो गया। डॉक्टर ने एक भारी प्लास्टर लगाया और उसे दृढ़ता से कहा कि जब तक यह पूरी तरह से ठीक नहीं हो जाता, उसे आराम करना चाहिए और किसी भी तनाव से बचना चाहिए। मीरा तबाह हो गई थी, उसे यकीन था कि उसकी सुबह-सुबह उठने और पैरों में दर्द होने के कई महीने बर्बाद हो गए थे। उनकी कोच, कशिश मैडम, उनसे घर पर मिलीं और उन्हें याद दिलाया कि टूटे हुए हाथ का मतलब टूटे हुए पैर नहीं हैं, और दौड़ना मुख्य रूप से मजबूत पैरों और स्थिर सांसों पर निर्भर करता है, न कि उनकी बाहों पर। प्रोत्साहित होकर, मीरा ने फिर से धीरे-धीरे अभ्यास शुरू किया, ध्यानपूर्वक अपने शरीर के साथ अपनी कास्ट को संतुलित करते हुए उसने कम दूरी तक जॉगिंग की, जैसे-जैसे दिन बीतते गए, धीरे-धीरे उसकी गति बढ़ती गई। कुछ सहपाठियों ने फुसफुसाकर कहा कि उसे चैंपियनशिप से हट जाना चाहिए, क्योंकि चोट के साथ प्रतिस्पर्धा करना व्यर्थ और जोखिम भरा भी लग रहा था। मीरा ने उनकी शंकाओं को नजरअंदाज कर दिया और अभ्यास के अंतिम चरण के दौरान अपनी बांह की रक्षा के लिए स्लिंग पहनकर प्रशिक्षण जारी रखा। दौड़ के दिन, वह शुरुआती पंक्ति में खड़ी थी और उसके हाथ पर अभी भी पट्टी बंधी हुई थी, उसका दिल शुरुआती सीटी की तुलना में ज़ोर से धड़क रहा था। जब भी उसकी बांह बहुत तेजी से घूमती थी तो वह धड़कते दर्द को नजरअंदाज करते हुए सावधानीपूर्वक, दृढ़ कदमों से दौड़ती थी। मीरा ने पहले स्थान पर नहीं, बल्कि तीसरे स्थान पर फिनिश लाइन पार की, लेकिन दिन का सबसे जोरदार उत्साह उसके कोच और सहपाठियों से आया, जो वास्तव में समझते थे कि कांस्य पदक कितने साहस का प्रतिनिधित्व करता है।',
      bodyGu: '''મીરાએ જિલ્લા દોડ ચેમ્પિયનશિપ માટે લગભગ છ મહિના સુધી તાલીમ લીધી હતી, તે દરરોજ સૂર્યોદય પહેલાં ઉઠીને આણંદમાં તેની શાળાની પાછળ ધૂળવાળા મેદાન પર પ્રેક્ટિસ કરતી હતી. દોડના ત્રણ અઠવાડિયા પહેલા, તેની માતાને પાણી ઊંચકવામાં મદદ કરતી વખતે, તે ભીના પગથિયાં પરથી લપસી ગઈ અને તેના ડાબા હાથમાં ફ્રેક્ચર થઈ ગયું. ડૉક્ટરે ભારે પ્લાસ્ટર બાંધ્યું અને તેને મક્કમતાથી કહ્યું કે જ્યાં સુધી તે સંપૂર્ણપણે સાજી ન થાય ત્યાં સુધી તેણે આરામ કરવો જોઈએ અને કોઈપણ પ્રકારના શ્રમથી બચવું જોઈએ. મીરા ખૂબ નિરાશ થઈ ગઈ હતી, તેને ખાતરી હતી કે વહેલી સવારે ઉઠવાની અને પગમાં દુખાવો સહન કરવાની તેની મહિનાઓની મહેનત વેડફાઈ ગઈ છે. તેના કોચ, કશિશ મેડમ, તેને ઘરે મળ્યા અને યાદ અપાવ્યું કે તૂટેલા હાથનો અર્થ તૂટેલા પગ નથી, અને દોડવું મુખ્યત્વે મજબૂત પગ અને સ્થિર શ્વાસ પર આધારિત છે, નહીં કે તેના હાથ પર. પ્રોત્સાહિત થઈને, મીરાએ ધીમે ધીમે ફરીથી પ્રેક્ટિસ શરૂ કરી, તેના શરીર સાથે પ્લાસ્ટરને કાળજીપૂર્વક સંતુલિત કરીને તેણે ટૂંકા અંતર સુધી જોગિંગ કર્યું, જેમ જેમ દિવસો વીતતા ગયા તેમ ધીમે ધીમે તેની ઝડપ વધવા લાગી. કેટલાક સહપાઠીઓએ ધીમેથી કહ્યું કે તેણે ચેમ્પિયનશિપમાંથી ખસી જવું જોઈએ, કારણ કે ઈજા સાથે સ્પર્ધા કરવી વ્યર્થ અને જોખમભરી પણ લાગી રહી હતી. મીરાએ તેમની શંકાઓને અવગણી અને પ્રેક્ટિસના અંતિમ તબક્કા દરમિયાન તેના હાથના રક્ષણ માટે સ્લિંગ પહેરીને તાલીમ ચાલુ રાખી. દોડના દિવસે, તે શરૂઆતની લાઇન પર ઉભી હતી અને તેના હાથ પર હજી પણ પાટો બાંધેલો હતો, તેનું હૃદય શરૂઆતની સીટી કરતાં પણ વધુ જોરથી ધબકી રહ્યું હતું. જ્યારે પણ તેનો હાથ ખૂબ ઝડપથી હલતો ત્યારે થતા અસહ્ય દુખાવાને અવગણીને તે કાળજીપૂર્વક અને મક્કમ પગલાં સાથે દોડી. મીરાએ પહેલા નહીં, પણ ત્રીજા સ્થાને ફિનિશ લાઇન પાર કરી, પરંતુ તે દિવસનો સૌથી મોટો ઉત્સાહ તેના કોચ અને સહપાઠીઓ તરફથી આવ્યો, જેઓ ખરેખર સમજતા હતા કે તે બ્રોન્ઝ મેડલ કેટલી હિંમતનું પ્રતિનિધિત્વ કરે છે.''',
      questions: [
        PracticeQuestion(
          prompt: 'How did Meera injure her arm before the championship?',
          options: [
            'She fell while running on the school ground.',
            'She slipped on wet steps while carrying water.',
            'She hurt it while lifting weights.',
            'She was hurt during a practice race.',
          ],
          correctIndex: 1,
          explanation: 'The passage says she "slipped on the wet steps and fractured her left arm" while helping her mother carry water.',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'What did Kashish ma\'am remind Meera to encourage her?',
          options: [
            'That the doctor was wrong about her injury',
            'That a broken arm did not mean broken legs, and running depended on legs and breathing',
            'That she should wait for next year\'s championship instead',
            'That her classmates would help her train',
          ],
          correctIndex: 1,
          explanation: 'The passage says he reminded her "that a broken arm did not mean broken legs, and that running mainly depended on strong legs and steady breathing".',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'How did some classmates react to Meera continuing to train?',
          options: [
            'They cheered her on immediately.',
            'They whispered that she should withdraw from the championship.',
            'They asked the coach to stop her.',
            'They offered to carry her bag every day.',
          ],
          correctIndex: 1,
          explanation: 'The passage says "some classmates whispered that she should simply withdraw from the championship".',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'Why did the loudest cheer come for Meera even though she finished third?',
          options: [
            'Because she was the fastest runner overall',
            'Because the race was cancelled and restarted',
            'Because the other runners had cheated',
            'Because everyone understood how much courage her bronze medal represented',
          ],
          correctIndex: 3,
          explanation: 'The passage ends by saying her coach and classmates "understood exactly how much courage that bronze medal represented".',
          difficulty: Difficulty.medium,
        ),
      ],
      glosses: [
        InlineGloss(word: 'championship', meaningHi: 'प्रतियोगिता / चैंपियनशिप', hiTransliteration: 'pratiyogita / championship', meaningGu: 'ચેમ્પિયનશિપ / સ્પર્ધા', guTransliteration: 'championship / spardha'),
        InlineGloss(word: 'fractured', meaningHi: 'टूट गई (हड्डी)', hiTransliteration: 'toot gayi (haddi)', meaningGu: 'ફ્રેક્ચર થયું / હાડકું તૂટી ગયું', guTransliteration: 'fracture thayu / hadaku tuti gayu'),
        InlineGloss(word: 'plaster cast', meaningHi: 'प्लास्टर की पट्टी', hiTransliteration: 'plaster ki patti', meaningGu: 'પ્લાસ્ટરનો પાટો', guTransliteration: 'plaster no pato'),
        InlineGloss(word: 'strain', meaningHi: 'ज़ोर / दबाव', hiTransliteration: 'zor / dabaav', meaningGu: 'શ્રમ / તાણ', guTransliteration: 'shram / taan'),
        InlineGloss(word: 'devastated', meaningHi: 'बहुत निराश / टूट गई', hiTransliteration: 'bahut niraash / toot gayi', meaningGu: 'ખૂબ નિરાશ / ભાંગી પડેલી', guTransliteration: 'khub nirash / bhangi padeli'),
        InlineGloss(word: 'sling', meaningHi: 'बांह बांधने की पट्टी', hiTransliteration: 'baanh baandhne ki patti', meaningGu: 'હાથ લટકાવવાનો પાટો (સ્લિંગ)', guTransliteration: 'hath latkavavano pato (sling)'),
        InlineGloss(word: 'withdraw', meaningHi: 'पीछे हट जाना', hiTransliteration: 'peeche hat jaana', meaningGu: 'પાછા હટી જવું / નામ પાછું ખેંચવું', guTransliteration: 'pacha hati javu / naam pachu khenchavu'),
        InlineGloss(word: 'strides', meaningHi: 'बड़े-बड़े कदम', hiTransliteration: 'bade-bade kadam', meaningGu: 'લાંબા ડગલાં', guTransliteration: 'lamba dagala'),
        InlineGloss(word: 'throbbing ache', meaningHi: 'धड़कता हुआ दर्द', hiTransliteration: 'dhadakta hua dard', meaningGu: 'સખત ધબકતો દુખાવો', guTransliteration: 'sakhat dhabakto dukhavo'),
        InlineGloss(word: 'courage', meaningHi: 'हिम्मत', hiTransliteration: 'himmat', meaningGu: 'હિંમત / સાહસ', guTransliteration: 'himmat / sahas'),
      ],
    ),
    ReadingPassage(
      id: 'class5_reading_science_fair',
      title: 'The Water-Saving Machine',
      emoji: '🔬',
      grade: 'Class 5',
      difficulty: Difficulty.medium,
      body: 'When the annual school science fair was announced in Rajkot, most students in Class 5 chose to '
          'build simple volcano models or paper circuits, but a quiet boy named Dhruv had a different idea. He '
          'had noticed his grandmother collecting the water that ran from the kitchen tap while it heated up, '
          'using it later to water her plants instead of letting it drain away uselessly. Dhruv wondered whether '
          'this small household habit could somehow be built into an actual working device. For weeks, he '
          'sketched designs in his notebook, experimenting with old pipes, a discarded bucket, and a simple '
          'valve his father found in the garage. His first three attempts leaked water everywhere, and his '
          'mother teased that their kitchen floor had never been so wet. Undiscouraged, Dhruv studied why each '
          'version failed, adjusting the angle of the pipes and sealing the joints more carefully each time. '
          'On the fourth attempt, water that would normally have gone straight down the drain flowed instead '
          'into a collection tank, ready to be reused for washing or watering plants. At the science fair, judges '
          'walked past the taller, flashier volcano models and paused thoughtfully at Dhruv\'s modest wooden '
          'stand, asking him detailed questions about how much water his device could save in a single day. '
          'Dhruv explained calmly, using numbers he had measured himself over a whole week at home. To everyone\'s '
          'surprise, his simple water-saving device won first prize, and the judges praised him for solving a '
          'real problem instead of merely demonstrating something already known. Dhruv realised that a good '
          'invention did not need to be complicated, only useful.',
      bodyHi: 'जब राजकोट में वार्षिक स्कूल विज्ञान मेले की घोषणा की गई, तो कक्षा 5 के अधिकांश छात्रों ने सरल ज्वालामुखी मॉडल या पेपर सर्किट बनाने का विकल्प चुना, लेकिन ध्रुव नाम के एक शांत लड़के का विचार अलग था। उसने देखा था कि उसकी दादी रसोई के नल से बहने वाले पानी को गर्म होने पर इकट्ठा करती थीं, और बाद में उसे बेकार बहने देने के बजाय अपने पौधों को पानी देने के लिए उपयोग करती थीं। ध्रुव को आश्चर्य हुआ कि क्या इस छोटी घरेलू आदत को किसी तरह वास्तविक कार्यशील उपकरण में बनाया जा सकता है। हफ्तों तक, उन्होंने अपनी नोटबुक में पुराने पाइपों, एक फेंकी हुई बाल्टी और अपने पिता को गैरेज में मिले एक साधारण वाल्व के साथ प्रयोग करते हुए डिज़ाइन बनाए। उनके पहले तीन प्रयासों से हर जगह पानी लीक हो गया, और उनकी माँ ने चिढ़ाते हुए कहा कि उनकी रसोई का फर्श कभी इतना गीला नहीं था। निराश हुए बिना, ध्रुव ने अध्ययन किया कि प्रत्येक संस्करण विफल क्यों हुआ, पाइपों के कोण को समायोजित किया और हर बार जोड़ों को अधिक सावधानी से सील किया। चौथे प्रयास में, जो पानी आम तौर पर सीधे नाली में चला जाता था वह एक संग्रह टैंक में बह गया, जो पौधों को धोने या पानी देने के लिए पुन: उपयोग के लिए तैयार था। विज्ञान मेले में, न्यायाधीश ऊंचे, चमकदार ज्वालामुखी मॉडलों के पास से गुजरे और ध्रुव के मामूली लकड़ी के स्टैंड पर सोच-समझकर रुके, और उनसे विस्तृत प्रश्न पूछे कि उनका उपकरण एक दिन में कितना पानी बचा सकता है। ध्रुव ने शांति से समझाया, उन संख्याओं का उपयोग करके जो उसने पूरे सप्ताह घर पर खुद को मापा था। हर किसी को आश्चर्यचकित करते हुए, उनके सरल जल-बचत उपकरण ने प्रथम पुरस्कार जीता, और न्यायाधीशों ने केवल पहले से ज्ञात कुछ का प्रदर्शन करने के बजाय एक वास्तविक समस्या को हल करने के लिए उनकी प्रशंसा की। ध्रुव को एहसास हुआ कि एक अच्छे आविष्कार के लिए जटिल होना जरूरी नहीं है, केवल उपयोगी होना जरूरी है।',
      bodyGu: '''જ્યારે રાજકોટમાં વાર્ષિક શાળા વિજ્ઞાન મેળાની જાહેરાત કરવામાં આવી, ત્યારે ધોરણ 5 ના મોટાભાગના વિદ્યાર્થીઓએ સરળ જ્વાળામુખી મોડલ અથવા પેપર સર્કિટ બનાવવાનું પસંદ કર્યું, પરંતુ ધ્રુવ નામના એક શાંત છોકરાનો વિચાર અલગ હતો. તેણે જોયું હતું કે તેની દાદી રસોડાના નળમાંથી વહેતું પાણી જ્યારે ગરમ થતું હોય ત્યારે તેને ભેગું કરતી હતી, અને બાદમાં તેને નકામું વહી જવા દેવાને બદલે પોતાના છોડને પાણી આપવા માટે તેનો ઉપયોગ કરતી હતી. ધ્રુવને વિચાર આવ્યો કે શું આ નાની ઘરગથ્થુ આદતને કોઈ રીતે વાસ્તવિક કાર્યશીલ ઉપકરણમાં ફેરવી શકાય છે. અઠવાડિયાઓ સુધી, તેણે પોતાની નોટબુકમાં જૂની પાઈપો, એક ફેંકી દીધેલી ડોલ અને તેના પિતાને ગેરેજમાંથી મળેલા એક સાધારણ વાલ્વ સાથે પ્રયોગ કરતા ડિઝાઇન બનાવી. તેના પહેલા ત્રણ પ્રયાસોમાં બધે પાણી લીક થઈ ગયું, અને તેની માતાએ ચીડવતા કહ્યું કે તેમના રસોડાનું ભોંયતળિયું ક્યારેય આટલું ભીનું નહોતું. નિરાશ થયા વિના, ધ્રુવે અભ્યાસ કર્યો કે દરેક સંસ્કરણ શા માટે નિષ્ફળ ગયું, પાઈપોના ખૂણાને ગોઠવ્યા અને દર વખતે સાંધાઓને વધુ કાળજીપૂર્વક સીલ કર્યા. ચોથા પ્રયાસમાં, જે પાણી સામાન્ય રીતે સીધું ગટરમાં જતું હતું તે એક સંગ્રહ ટાંકીમાં વહી ગયું, જે છોડને ધોવા અથવા પાણી આપવા માટે પુનઃઉપયોગ માટે તૈયાર હતું. વિજ્ઞાન મેળામાં, નિર્ણાયકો ઊંચા, ચમકદાર જ્વાળામુખી મોડલો પાસેથી પસાર થયા અને ધ્રુવના સાધારણ લાકડાના સ્ટેન્ડ પાસે વિચારપૂર્વક ઊભા રહ્યા, અને તેમને વિસ્તૃત પ્રશ્નો પૂછ્યા કે તેમનું ઉપકરણ એક દિવસમાં કેટલું પાણી બચાવી શકે છે. ધ્રુવે શાંતિથી સમજાવ્યું, તે સંખ્યાઓનો ઉપયોગ કરીને જે તેણે આખા અઠવાડિયા દરમિયાન ઘરે જાતે માપી હતી. દરેકને આશ્ચર્યચકિત કરતા, તેના સરળ જળ-બચત ઉપકરણે પ્રથમ ઇનામ જીત્યું, અને નિર્ણાયકોએ માત્ર પહેલાથી જ્ઞાત કંઈકનું પ્રદર્શન કરવાને બદલે એક વાસ્તવિક સમસ્યાને હલ કરવા બદલ તેની પ્રશંસા કરી. ધ્રુવને અહેસાસ થયો કે એક સારા આવિષ્કાર માટે જટિલ હોવું જરૂરી નથી, માત્ર ઉપયોગી હોવું જરૂરી છે.''',
      questions: [
        PracticeQuestion(
          prompt: 'What gave Dhruv the idea for his invention?',
          options: [
            'A machine he saw at a shop',
            'His grandmother collecting water that ran from the tap while it heated up',
            'A video his teacher showed the class',
            'A book he read at the library',
          ],
          correctIndex: 1,
          explanation: 'The passage says he noticed his grandmother "collecting the water that ran from the kitchen tap while it heated up" to reuse it.',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'What happened during Dhruv\'s first three attempts at building his device?',
          options: [
            'They leaked water everywhere.',
            'They worked perfectly the first time.',
            'His parents refused to let him try.',
            'They were too expensive to complete.',
          ],
          correctIndex: 0,
          explanation: 'The passage says "his first three attempts leaked water everywhere", and his mother teased him about the wet floor.',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'How did Dhruv improve his device after each failed attempt?',
          options: [
            'He studied why each version failed and adjusted the pipes and joints.',
            'He bought a ready-made kit instead.',
            'He asked the judges to help him build it.',
            'He gave up and copied a friend\'s idea.',
          ],
          correctIndex: 0,
          explanation: 'The passage says he kept "studying why each version failed, adjusting the angle of the pipes and sealing the joints more carefully each time".',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'Why did the judges praise Dhruv\'s project over the flashier volcano models?',
          options: [
            'Because he used more expensive materials',
            'Because his stand was decorated the best',
            'Because it was the biggest project at the fair',
            'Because he solved a real problem instead of merely demonstrating something already known',
          ],
          correctIndex: 3,
          explanation: 'The passage says the judges praised him "for solving a real problem instead of merely demonstrating something already known".',
          difficulty: Difficulty.medium,
        ),
      ],
      glosses: [
        InlineGloss(word: 'volcano models', meaningHi: 'ज्वालामुखी के मॉडल', hiTransliteration: 'jwaalaamukhi ke model', meaningGu: 'જ્વાળામુખીના મોડલ', guTransliteration: 'jwaalaamukhina model'),
        InlineGloss(word: 'discarded bucket', meaningHi: 'फेंकी हुई बाल्टी', hiTransliteration: 'phenki hui baalti', meaningGu: 'ફેંકી દીધેલી ડોલ', guTransliteration: 'fenki didheli dol'),
        InlineGloss(word: 'valve', meaningHi: 'वाल्व / निकास द्वार', hiTransliteration: 'valve / nikaas dwaar', meaningGu: 'વાલ્વ / નિકાસ દ્વાર', guTransliteration: 'valve / nikaas dwaar'),
        InlineGloss(word: 'undiscouraged', meaningHi: 'बिना हिम्मत हारे', hiTransliteration: 'bina himmat haare', meaningGu: 'નિરાશ થયા વિના / હિંમત હાર્યા વિના', guTransliteration: 'niraash thaya vina / himmat haarya vina'),
        InlineGloss(word: 'sealing the joints', meaningHi: 'जोड़ों को बंद करना', hiTransliteration: 'jodon ko band karna', meaningGu: 'સાંધાઓને બંધ કરવા', guTransliteration: 'saandhao ne bandh karva'),
        InlineGloss(word: 'collection tank', meaningHi: 'पानी जमा करने की टंकी', hiTransliteration: 'paani jama karne ki tanki', meaningGu: 'પાણી જમા કરવાની ટાંકી', guTransliteration: 'paani jama karvani tanki'),
        InlineGloss(word: 'flashier', meaningHi: 'ज़्यादा चमकदार / दिखावटी', hiTransliteration: 'zyaada chamakdaar / dikhaavati', meaningGu: 'વધારે ચમકદાર / દેખાવડું', guTransliteration: 'vadhare chamakdaar / dekhavdu'),
        InlineGloss(word: 'modest', meaningHi: 'साधारण / सादा', hiTransliteration: 'saadhaaran / saada', meaningGu: 'સાધારણ / સાદું', guTransliteration: 'saadharan / saadu'),
        InlineGloss(word: 'invention', meaningHi: 'आविष्कार', hiTransliteration: 'aavishkaar', meaningGu: 'આવિષ્કાર / શોધ', guTransliteration: 'aavishkar / shodh'),
      ],
    ),
    ReadingPassage(
      id: 'class5_reading_well_repair',
      title: 'The Village Well Repair',
      emoji: '🪣',
      grade: 'Class 5',
      difficulty: Difficulty.medium,
      body: 'The old stepwell at the edge of Khedgaon had served the village for generations, but one dry '
          'summer, cracks appeared along its inner walls, and the water inside turned murky and unsafe to drink. '
          'The village panchayat announced that repairing it properly would take months and a large sum of money '
          'that the village simply did not have that year. Many families began the tiring daily walk to a '
          'distant handpump instead, carrying heavy pots under the harsh sun. A shopkeeper named Rasheed '
          'suggested that instead of waiting for outside funds, the villagers should pool together whatever '
          'time, skill, and small savings they could each spare. At first, only a handful of people volunteered, '
          'unsure whether their small contributions would matter against such a large repair. Rasheed organised '
          'a meeting at the village square, where a retired mason named Bhagwan Kaka offered to guide the work '
          'for free, having built similar structures decades earlier. Slowly, more villagers joined: farmers '
          'donated bricks left over from their own construction, women organised meals for the workers, and '
          'children helped clear debris after school hours. Over six weekends, the community repaired the '
          'cracked walls, cleared the sediment at the bottom, and built a small fence to keep the water clean. '
          'When the first bucket of clear water was drawn up, the entire village gathered to celebrate, and '
          'even families who had not contributed directly came to thank those who had. Rasheed reminded everyone '
          'that the well had not been rebuilt by money alone, but by dozens of small efforts joined together, '
          'proving that a community working as one could achieve what had once seemed impossible.',
      bodyHi: 'खेड़गांव के किनारे पर स्थित पुरानी बावड़ी पीढ़ियों से गांव की सेवा कर रही थी, लेकिन एक शुष्क गर्मी में, इसकी भीतरी दीवारों में दरारें आ गईं और अंदर का पानी गंदा हो गया और पीने के लिए असुरक्षित हो गया। ग्राम पंचायत ने घोषणा की कि इसकी ठीक से मरम्मत करने में कई महीने लगेंगे और इतनी बड़ी धनराशि भी खर्च होगी जो उस वर्ष गाँव के पास नहीं थी। कई परिवारों ने कड़ी धूप में भारी बर्तन लेकर दूर स्थित हैंडपंप तक रोजाना की थका देने वाली पैदल यात्रा शुरू कर दी। रशीद नाम के एक दुकानदार ने सुझाव दिया कि बाहरी धन की प्रतीक्षा करने के बजाय, ग्रामीणों को जो भी समय, कौशल और छोटी बचत हो सकती है, उसे इकट्ठा करना चाहिए। सबसे पहले, केवल कुछ मुट्ठी भर लोगों ने ही स्वेच्छा से काम किया, वे अनिश्चित थे कि इतनी बड़ी मरम्मत के लिए उनका छोटा योगदान मायने रखेगा या नहीं। रशीद ने गांव के चौराहे पर एक बैठक आयोजित की, जहां भगवान काका नाम के एक सेवानिवृत्त राजमिस्त्री ने मुफ्त में काम का मार्गदर्शन करने की पेशकश की, जिसने दशकों पहले इसी तरह की संरचनाओं का निर्माण किया था। धीरे-धीरे, अधिक ग्रामीण शामिल हो गए: किसानों ने अपने स्वयं के निर्माण से बची हुई ईंटें दान कर दीं, महिलाओं ने श्रमिकों के लिए भोजन की व्यवस्था की, और बच्चों ने स्कूल के समय के बाद मलबा हटाने में मदद की। छह सप्ताहांतों में, समुदाय ने टूटी हुई दीवारों की मरम्मत की, तल पर तलछट को साफ किया, और पानी को साफ रखने के लिए एक छोटी बाड़ का निर्माण किया। जब साफ़ पानी की पहली बाल्टी निकाली गई, तो पूरा गाँव जश्न मनाने के लिए इकट्ठा हो गया, और यहाँ तक कि जिन परिवारों ने सीधे योगदान नहीं दिया था, वे उन लोगों को धन्यवाद देने आए जिन्होंने योगदान दिया था। रशीद ने सभी को याद दिलाया कि कुएं का पुनर्निर्माण केवल पैसे से नहीं किया गया था, बल्कि दर्जनों छोटे-छोटे प्रयासों को मिलाकर किया गया था, जिससे यह साबित हुआ कि एक समुदाय के रूप में काम करने से वह हासिल किया जा सकता है जो एक समय असंभव लगता था।',
      bodyGu: '''ખેડગાંવના છેવાડે આવેલી જૂની વાવ પેઢીઓથી ગામની સેવા કરી રહી હતી, પરંતુ એક સૂકા ઉનાળામાં, તેની અંદરની દીવાલોમાં તિરાડો પડી ગઈ અને અંદરનું પાણી ગંદુ થઈ ગયું અને પીવા માટે અસુરક્ષિત થઈ ગયું. ગ્રામ પંચાયતે જાહેરાત કરી કે તેનું યોગ્ય રીતે સમારકામ કરવામાં મહિનાઓ લાગશે અને મોટી રકમનો ખર્ચ થશે જે તે વર્ષે ગામ પાસે નહોતી. ઘણા પરિવારોએ કાળઝાળ તડકામાં ભારે વાસણો લઈને દૂર આવેલા હેન્ડપંપ સુધી રોજની થકવી નાખનારી પગપાળા યાત્રા શરૂ કરી. રશીદ નામના એક દુકાનદારે સૂચન કર્યું કે બહારના ભંડોળની રાહ જોવાને બદલે, ગ્રામજનોએ જે પણ સમય, કૌશલ્ય અને નાની બચત હોઈ શકે, તે ભેગી કરવી જોઈએ. શરૂઆતમાં, માત્ર મુઠ્ઠીભર લોકોએ સ્વેચ્છાએ કામ કર્યું, તેઓ અનિશ્ચિત હતા કે આવા મોટા સમારકામ માટે તેમનું નાનું યોગદાન મહત્વનું રહેશે કે કેમ. રશીદે ગામના ચોકમાં એક મીટિંગનું આયોજન કર્યું, જ્યાં ભગવાન કાકા નામના નિવૃત્ત કડિયાએ મફતમાં કામનું માર્ગદર્શન આપવાની ઓફર કરી, જેમણે દાયકાઓ પહેલા આવા જ બાંધકામો બનાવ્યા હતા. ધીરે ધીરે, વધુ ગ્રામજનો જોડાયા: ખેડૂતોએ તેમના પોતાના બાંધકામમાંથી વધેલી ઇંટોનું દાન કર્યું, મહિલાઓએ કામદારો માટે ભોજનની વ્યવસ્થા કરી, અને બાળકોએ શાળાના સમય પછી કાટમાળ સાફ કરવામાં મદદ કરી. છ સપ્તાહાંતમાં, સમુદાયે તિરાડવાળી દીવાલોનું સમારકામ કર્યું, તળિયે જામેલો કાંપ સાફ કર્યો, અને પાણીને સ્વચ્છ રાખવા માટે એક નાની વાડ બનાવી. જ્યારે સ્વચ્છ પાણીની પહેલી ડોલ બહાર કાઢવામાં આવી, ત્યારે આખું ગામ ઉજવણી કરવા માટે ભેગું થયું, અને જે પરિવારોએ સીધું યોગદાન નહોતું આપ્યું તેઓ પણ યોગદાન આપનારાઓનો આભાર માનવા આવ્યા. રશીદે બધાને યાદ અપાવ્યું કે કૂવાનું પુનઃનિર્માણ માત્ર પૈસાથી નહોતું થયું, પરંતુ ડઝનબંધ નાના પ્રયાસોને ભેગા કરીને કરવામાં આવ્યું હતું, જે સાબિત કરે છે કે એક સમુદાય તરીકે કામ કરવાથી તે પ્રાપ્ત કરી શકાય છે જે એક સમયે અશક્ય લાગતું હતું.''',
      questions: [
        PracticeQuestion(
          prompt: 'Why did the villagers stop using the old stepwell that summer?',
          options: [
            'Cracks appeared and the water turned murky and unsafe to drink.',
            'A new handpump was built nearby.',
            'The well had completely dried up.',
            'The panchayat closed it for a festival.',
          ],
          correctIndex: 0,
          explanation: 'The passage says "cracks appeared along its inner walls, and the water inside turned murky and unsafe to drink".',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'What did Rasheed suggest instead of waiting for outside funds?',
          options: [
            'Moving the whole village to a new location',
            'Pooling together whatever time, skill, and small savings the villagers could spare',
            'Digging an entirely new well instead',
            'Asking a nearby city to send free water tankers',
          ],
          correctIndex: 1,
          explanation: 'The passage says Rasheed suggested "the villagers should pool together whatever time, skill, and small savings they could each spare".',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'Who guided the repair work using his past experience?',
          options: ['Rasheed himself', 'A government engineer', 'Bhagwan Kaka, a retired mason', 'A school teacher'],
          correctIndex: 2,
          explanation: 'The passage says "a retired mason named Bhagwan Kaka offered to guide the work for free, having built similar structures decades earlier".',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'What lesson did Rasheed point out after the well was repaired?',
          options: [
            'That only skilled workers should be trusted with repairs',
            'That the well had been rebuilt by dozens of small efforts joined together',
            'That money alone solves every problem',
            'That the village should now build a second well',
          ],
          correctIndex: 1,
          explanation: 'The passage ends with Rasheed reminding everyone "that the well had not been rebuilt by money alone, but by dozens of small efforts joined together".',
          difficulty: Difficulty.medium,
        ),
      ],
      glosses: [
        InlineGloss(word: 'stepwell', meaningHi: 'बावड़ी / सीढ़ीदार कुआं', hiTransliteration: 'baavdi / seedhidaar kuaan', meaningGu: 'વાવ / પગથિયાં વાળો કૂવો', guTransliteration: 'vav / pagathiya valo kuvo'),
        InlineGloss(word: 'murky', meaningHi: 'गंदा / धुंधला', hiTransliteration: 'ganda / dhundhla', meaningGu: 'ગંદુ / ધૂંધળું', guTransliteration: 'gandu / dhundhlu'),
        InlineGloss(word: 'panchayat', meaningHi: 'ग्राम पंचायत', hiTransliteration: 'gram panchayat', meaningGu: 'ગ્રામ પંચાયત', guTransliteration: 'gram panchayat'),
        InlineGloss(word: 'handpump', meaningHi: 'हैंडपंप', hiTransliteration: 'handpump', meaningGu: 'હેન્ડપંપ', guTransliteration: 'handpump'),
        InlineGloss(word: 'volunteered', meaningHi: 'स्वेच्छा से आगे आए', hiTransliteration: 'swechha se aage aaye', meaningGu: 'સ્વેચ્છાએ આગળ આવ્યા', guTransliteration: 'svechchhae aagal avya'),
        InlineGloss(word: 'mason', meaningHi: 'राजमिस्त्री', hiTransliteration: 'raajmistri', meaningGu: 'કડીયો', guTransliteration: 'kadiyo'),
        InlineGloss(word: 'debris', meaningHi: 'मलबा', hiTransliteration: 'malba', meaningGu: 'કાટમાળ', guTransliteration: 'katmal'),
        InlineGloss(word: 'sediment', meaningHi: 'तलछट / नीचे जमी मिट्टी', hiTransliteration: 'talchhat / neeche jami mitti', meaningGu: 'કાંપ / નીચે જામેલી માટી', guTransliteration: 'kamp / niche jameli mati'),
        InlineGloss(word: 'contributed', meaningHi: 'योगदान दिया', hiTransliteration: 'yogdaan diya', meaningGu: 'યોગદાન આપ્યું', guTransliteration: 'yogdan apyu'),
      ],
    ),
    ReadingPassage(
      id: 'class5_reading_garba_grandmother',
      title: 'Grandmother\'s Garba Steps',
      emoji: '💃',
      grade: 'Class 5',
      difficulty: Difficulty.medium,
      body: 'Every year during Navratri, the courtyard outside Simran\'s house in Vadodara transformed into a '
          'circle of swirling colour, as neighbours gathered each evening to perform garba around a small clay '
          'lamp. Simran loved watching the dance but felt embarrassed to join in, worried that her clumsy steps '
          'would look foolish next to the graceful movements of the older women. Her grandmother, Ba, noticed '
          'her hesitation on the very first night of the festival and gently asked why she stood at the edge of '
          'the circle instead of dancing. Simran admitted her fear of appearing awkward in front of everyone. '
          'Ba laughed softly and explained that garba had never been about perfect steps, but about the entire '
          'community moving together in celebration of the same rhythm, generation after generation. She told '
          'Simran stories of dancing in this very courtyard as a young girl, wearing a simple cotton chaniya her '
          'own mother had stitched, long before the sequinned outfits and loudspeakers of today. Encouraged by '
          'these stories, Simran agreed to try, and Ba patiently taught her the basic three-step pattern, '
          'correcting her gently whenever she turned the wrong way. By the third night, Simran\'s steps had grown '
          'steadier, and she found herself laughing freely instead of worrying about mistakes. She noticed that '
          'even the older dancers occasionally missed a beat, yet nobody around the circle seemed to mind or '
          'even notice. On the final night of Navratri, Simran danced confidently beside her grandmother under '
          'the string lights, understanding at last that the tradition survived not because everyone danced '
          'perfectly, but because everyone chose to join in together, year after year, keeping the rhythm alive.',
      bodyHi: 'हर साल नवरात्रि के दौरान, वडोदरा में सिमरन के घर के बाहर का आंगन घूमते रंगों के घेरे में बदल जाता था, क्योंकि पड़ोसी हर शाम मिट्टी के एक छोटे से दीपक के चारों ओर गरबा करने के लिए इकट्ठा होते थे। सिमरन को नृत्य देखना बहुत पसंद था लेकिन उसे इसमें शामिल होने में शर्मिंदगी महसूस होती थी, उसे चिंता थी कि बड़ी उम्र की महिलाओं की सुंदर हरकतों के आगे उसके अनाड़ी कदम मूर्खतापूर्ण लगेंगे। उसकी दादी बा ने उत्सव की पहली रात को उसकी झिझक को देखा और धीरे से पूछा कि वह नृत्य करने के बजाय घेरे के किनारे पर क्यों खड़ी थी। सिमरन ने स्वीकार किया कि उसे सबके सामने अजीब दिखने का डर था। बा धीरे से हँसे और समझाया कि गरबा कभी भी सही चरणों के बारे में नहीं था, बल्कि पूरे समुदाय के पीढ़ी दर पीढ़ी एक ही लय में जश्न मनाने के लिए एक साथ आगे बढ़ने के बारे में था। उन्होंने सिमरन को एक युवा लड़की के रूप में इसी आंगन में नृत्य करने की कहानियाँ सुनाईं, एक साधारण सूती चनिया पहनकर जो उसकी अपनी माँ ने सिलवाया था, आज के सेक्विन वाले परिधानों और लाउडस्पीकरों से बहुत पहले। इन कहानियों से प्रोत्साहित होकर, सिमरन प्रयास करने के लिए सहमत हो गई, और बा ने धैर्यपूर्वक उसे बुनियादी तीन-चरणीय पैटर्न सिखाया, जब भी वह गलत रास्ते पर गई तो उसे धीरे से सही किया। तीसरी रात तक, सिमरन के कदम स्थिर हो गए थे, और उसने गलतियों के बारे में चिंता करने के बजाय खुद को खुलकर हंसते हुए पाया। उसने देखा कि उम्रदराज़ नर्तक भी कभी-कभी एक ताल चूक जाते थे, फिर भी मंडली में मौजूद किसी को भी इस बात पर ध्यान नहीं जाता था या ध्यान भी नहीं देता था। नवरात्रि की आखिरी रात को, सिमरन ने स्ट्रिंग लाइट्स के नीचे अपनी दादी के साथ आत्मविश्वास से नृत्य किया, आखिरकार यह समझ में आया कि यह परंपरा इसलिए नहीं बची है क्योंकि हर कोई पूरी तरह से नृत्य करता है, बल्कि इसलिए क्योंकि सभी ने लय को जीवित रखते हुए, साल-दर-साल एक साथ शामिल होने का फैसला किया।',
      bodyGu: '''દર વર્ષે નવરાત્રી દરમિયાન, વડોદરામાં સિમરનના ઘરની બહારનું આંગણું ફરતા રંગોના વર્તુળમાં ફેરવાઈ જતું હતું, કારણ કે પડોશીઓ દરરોજ સાંજે માટીના નાના દીવાની આસપાસ ગરબા રમવા માટે ભેગા થતા હતા. સિમરનને નૃત્ય જોવું ખૂબ ગમતું પણ તેમાં જોડાવામાં શરમ આવતી હતી, તેને ચિંતા હતી કે મોટી ઉંમરની સ્ત્રીઓની સુંદર હલનચલન સામે તેના અણઘડ પગલાં મૂર્ખામીભર્યા લાગશે. તેના દાદી બાએ તહેવારની પહેલી જ રાતે તેનો ખચકાટ જોયો અને ધીમેથી પૂછ્યું કે તે નૃત્ય કરવાને બદલે વર્તુળની કિનારે કેમ ઉભી છે. સિમરને કબૂલાત કરી કે તેને બધાની સામે અજીબ દેખાવાનો ડર હતો. બા ધીમેથી હસ્યા અને સમજાવ્યું કે ગરબા ક્યારેય પણ માત્ર સાચા પગલાં વિશે ન હતા, પરંતુ આખા સમુદાયના પેઢી દર પેઢી એક જ લયમાં ઉજવણી કરવા માટે એકસાથે આગળ વધવા વિશે હતા. તેમણે સિમરનને એક યુવાન છોકરી તરીકે આ જ આંગણામાં નૃત્ય કરવાની વાર્તાઓ કહી, એક સાધારણ સુતરાઉ ચણિયા પહેરીને જે તેની પોતાની માતાએ સિવડાવ્યો હતો, આજના સિક્વિનવાળા પોશાકો અને લાઉડસ્પીકરો પહેલાં. આ વાર્તાઓથી પ્રોત્સાહિત થઈને, સિમરન પ્રયત્ન કરવા સંમત થઈ, અને બાએ ધીરજપૂર્વક તેને મૂળભૂત ત્રણ-પગલાંની પેટર્ન શીખવી, જ્યારે પણ તે ખોટી દિશામાં ગઈ ત્યારે તેને ધીમેથી સુધારી. ત્રીજી રાત સુધીમાં, સિમરનના પગલાં સ્થિર થઈ ગયા હતા, અને તેણે ભૂલો વિશે ચિંતા કરવાને બદલે પોતાને મુક્તપણે હસતી જોઈ. તેણે નોંધ્યું કે મોટી ઉંમરના નર્તકો પણ ક્યારેક તાલ ચૂકી જતા હતા, છતાં વર્તુળમાં કોઈને વાંધો ન હતો અથવા તો ધ્યાન પણ નહોતું આપતું. નવરાત્રીની છેલ્લી રાતે, સિમરને તેની દાદી સાથે સ્ટ્રિંગ લાઈટ્સ નીચે આત્મવિશ્વાસથી નૃત્ય કર્યું, આખરે એ સમજાયું કે આ પરંપરા એટલા માટે નથી ટકી કે દરેક જણ સંપૂર્ણપણે નૃત્ય કરે છે, પરંતુ એટલા માટે કે બધાએ લયને જીવંત રાખીને, વર્ષ-દર-વર્ષ એકસાથે જોડાવાનું પસંદ કર્યું છે.''',
      questions: [
        PracticeQuestion(
          prompt: 'Why did Simran feel embarrassed to join the garba dancing at first?',
          options: [
            'Her grandmother told her not to dance.',
            'She did not like the music being played.',
            'She was not allowed outside in the evening.',
            'She worried her clumsy steps would look foolish next to the older women.',
          ],
          correctIndex: 3,
          explanation: 'The passage says she was "worried that her clumsy steps would look foolish next to the graceful movements of the older women".',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'What did Ba say garba had always truly been about?',
          options: [
            'Following strict, unchanging steps without mistakes',
            'Wearing the most expensive outfit',
            'The entire community moving together in celebration of the same rhythm',
            'Competing to find the best dancer',
          ],
          correctIndex: 2,
          explanation: 'Ba explained that garba "had never been about perfect steps, but about the entire community moving together in celebration of the same rhythm".',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'What did Simran notice about even the older, experienced dancers?',
          options: [
            'They occasionally missed a beat, and nobody seemed to mind.',
            'They never made any mistakes at all.',
            'They refused to dance with beginners.',
            'They stopped dancing after the second night.',
          ],
          correctIndex: 0,
          explanation: 'The passage says she noticed "even the older dancers occasionally missed a beat, yet nobody around the circle seemed to mind or even notice".',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'What did Simran finally understand about why the tradition survived?',
          options: [
            'That it survived because dancing perfectly was required',
            'That it survived because of loudspeakers and sequinned outfits',
            'That it survived because everyone chose to join in together, year after year',
            'That it survived only because of her grandmother\'s effort alone',
          ],
          correctIndex: 2,
          explanation: 'The passage ends by saying she understood the tradition survived "because everyone chose to join in together, year after year, keeping the rhythm alive".',
          difficulty: Difficulty.medium,
        ),
      ],
      glosses: [
        InlineGloss(word: 'Navratri', meaningHi: 'नवरात्रि (नौ रातों का त्योहार)', hiTransliteration: 'Navratri (nau raaton ka tyohaar)', meaningGu: 'નવરાત્રી (નવ રાતોનો તહેવાર)', guTransliteration: 'Navratri (nav raatono tahevaar)'),
        InlineGloss(word: 'garba', meaningHi: 'गरबा नृत्य', hiTransliteration: 'garba nritya', meaningGu: 'ગરબા નૃત્ય', guTransliteration: 'garba nrutya'),
        InlineGloss(word: 'clumsy', meaningHi: 'अनाड़ी / भद्दा', hiTransliteration: 'anaadi / bhadda', meaningGu: 'અણઘડ / બેડોળ', guTransliteration: 'anghad / bedol'),
        InlineGloss(word: 'graceful', meaningHi: 'सुंदर और सधे हुए', hiTransliteration: 'sundar aur sadhe hue', meaningGu: 'આકર્ષક / સુંદર', guTransliteration: 'aakarshak / sundar'),
        InlineGloss(word: 'hesitation', meaningHi: 'झिझक', hiTransliteration: 'jhijhak', meaningGu: 'ખચકાટ / સંકોચ', guTransliteration: 'khachkaat / sankoch'),
        InlineGloss(word: 'awkward', meaningHi: 'अटपटा / असहज', hiTransliteration: 'atpata / asahaj', meaningGu: 'વિચિત્ર / અસહજ', guTransliteration: 'vichitra / asahaj'),
        InlineGloss(word: 'chaniya', meaningHi: 'घाघरा / लहंगा', hiTransliteration: 'ghaaghra / lehnga', meaningGu: 'ચણિયા / ઘાઘરો', guTransliteration: 'chaniya / ghaghro'),
        InlineGloss(word: 'sequinned', meaningHi: 'चमकीले सितारों वाला', hiTransliteration: 'chamkeele sitaaron waala', meaningGu: 'ચમકતા તારલાવાળું (સિક્વિનવાળું)', guTransliteration: 'chamakta taarlavaalu (sequinvaalu)'),
        InlineGloss(word: 'confidently', meaningHi: 'आत्मविश्वास से', hiTransliteration: 'aatmavishwaas se', meaningGu: 'આત્મવિશ્વાસથી', guTransliteration: 'aatmavishvaasthi'),
      ],
    ),
  ],
);
