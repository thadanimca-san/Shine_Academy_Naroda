import '../models/chapter.dart';
import '../models/practice_question.dart';
import '../models/reading_passage.dart';

const class3Reading = ReadingLibrary(
  id: 'class3_reading',
  title: 'Reading Passages',
  grade: 'Class 3',
  passages: [
    ReadingPassage(
      id: 'class3_reading_squirrel',
      title: 'The Little Squirrel',
      emoji: '🐿️',
      grade: 'Class 3',
      difficulty: Difficulty.easy,
      body: 'A small squirrel lived in a big mango tree. Every morning, she jumped from branch to branch '
          'to find food. One day, she found a shiny red mango. She was very happy. But the mango was too '
          'heavy for her to carry alone. A little bird saw her and helped her push the mango to her nest. '
          'The squirrel thanked the bird. From that day, the squirrel and the bird became good friends and '
          'shared their food every day.',
      bodyHi: 'एक बड़े आम के पेड़ पर एक छोटी सी गिलहरी रहती थी। हर सुबह, वह भोजन खोजने के लिए एक शाखा से दूसरी शाखा पर छलांग लगाती थी। एक दिन, उसे एक चमकदार लाल आम मिला। वह बहुत खुश थी. लेकिन आम उसके अकेले ले जाने के लिए बहुत भारी था। एक छोटी सी चिड़िया ने उसे देखा और आम को घोंसले में धकेलने में उसकी मदद की। गिलहरी ने पक्षी को धन्यवाद दिया। उस दिन से, गिलहरी और पक्षी अच्छे दोस्त बन गए और हर दिन अपना भोजन साझा करते थे।',
      bodyGu: '''એક નાની ખિસકોલી આંબાના મોટા ઝાડ પર રહેતી હતી. દરરોજ સવારે, તે ખોરાક શોધવા માટે એક ડાળીથી બીજી ડાળી પર કૂદકો મારતી હતી. એક દિવસ, તેને એક ચમકતી લાલ કેરી મળી. તે ખૂબ ખુશ હતી. પરંતુ કેરી તેના માટે એકલા લઈ જવા માટે ખૂબ ભારે હતી. એક નાના પક્ષીએ તેને જોઈ અને કેરીને તેના માળામાં ધકેલવામાં તેની મદદ કરી. ખિસકોલીએ પક્ષીનો આભાર માન્યો. તે દિવસથી, ખિસકોલી અને પક્ષી સારા મિત્રો બની ગયા અને દરરોજ તેમનો ખોરાક વહેંચવા લાગ્યા.''',
      questions: [
        PracticeQuestion(
          prompt: 'In which place did the squirrel live?',
          options: ['In a garden', 'In a house', 'In a hole', 'In a big mango tree'],
          correctIndex: 3,
          explanation: 'The passage says the squirrel lived in a big mango tree.',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'What did the squirrel find?',
          options: ['A banana', 'A nut', 'An apple', 'A red mango'],
          correctIndex: 3,
          explanation: 'The passage says she found a shiny red mango.',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'Who helped the squirrel carry the mango?',
          options: ['A boy', 'A dog', 'Another squirrel', 'A little bird'],
          correctIndex: 3,
          explanation: 'The passage says a little bird saw her and helped her push the mango.',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'What happened after the bird helped the squirrel?',
          options: [
            'The bird flew away sadly.',
            'They became good friends.',
            'They fought over the mango.',
            'The squirrel ran away.',
          ],
          correctIndex: 1,
          explanation: 'The last sentence says the squirrel and the bird became good friends.',
          difficulty: Difficulty.medium,
        ),
      ],
      glosses: [
        InlineGloss(word: 'squirrel', meaningHi: 'गिलहरी', hiTransliteration: 'gilahari', meaningGu: 'ખિસકોલી', guTransliteration: 'khisakoli'),
        InlineGloss(word: 'branch', meaningHi: 'पेड़ की डाली', hiTransliteration: 'ped ki daali', meaningGu: 'ડાળી', guTransliteration: 'daali'),
        InlineGloss(word: 'shiny', meaningHi: 'चमकदार', hiTransliteration: 'chamakdar', meaningGu: 'ચમકતી', guTransliteration: 'chamkati'),
        InlineGloss(word: 'heavy', meaningHi: 'भारी', hiTransliteration: 'bhaari', meaningGu: 'ભારે', guTransliteration: 'bhare'),
        InlineGloss(word: 'nest', meaningHi: 'घोंसला', hiTransliteration: 'ghonsla', meaningGu: 'માળો', guTransliteration: 'maalo'),
        InlineGloss(word: 'thanked', meaningHi: 'धन्यवाद कहा', hiTransliteration: 'dhanyavaad kaha', meaningGu: 'આભાર માન્યો', guTransliteration: 'aabhar manyo'),
        InlineGloss(word: 'shared', meaningHi: 'बाँटा', hiTransliteration: 'baanta', meaningGu: 'વહેંચ્યું', guTransliteration: 'vahenchyum'),
      ],
    ),
    ReadingPassage(
      id: 'class3_reading_grandmother',
      title: 'A Visit to Grandmother\'s House',
      emoji: '👵',
      grade: 'Class 3',
      difficulty: Difficulty.easy,
      body: 'Every summer, Aarav went to his grandmother\'s house in a small village. His grandmother lived '
          'in a little house with a garden full of flowers. She told him funny stories every night before '
          'bed. In the morning, they fed the hens together and picked fresh vegetables from the garden. '
          'Aarav loved these visits the most because his grandmother always made his favourite sweet, '
          'ladoo, just for him.',
      bodyHi: 'हर गर्मियों में, आरव एक छोटे से गाँव में अपनी दादी के घर जाता था। उनकी दादी फूलों से भरे बगीचे वाले एक छोटे से घर में रहती थीं। वह हर रात सोने से पहले उसे मजेदार कहानियाँ सुनाती थी। सुबह में, उन्होंने एक साथ मुर्गियों को खाना खिलाया और बगीचे से ताज़ी सब्जियाँ उठाईं। आरव को ये मुलाकातें सबसे ज्यादा पसंद थीं क्योंकि उसकी दादी हमेशा उसके लिए उसकी पसंदीदा मिठाई, लड्डू बनाती थीं।',
      bodyGu: '''દર ઉનાળામાં, આરવ એક નાના ગામમાં તેની દાદીના ઘરે જતો હતો. તેની દાદી ફૂલોથી ભરેલા બગીચા સાથેના નાના ઘરમાં રહેતી હતી. તે દરરોજ રાત્રે સૂતા પહેલા તેને રમુજી વાર્તાઓ કહેતી. સવારે, તેઓ એકસાથે મરઘીઓને ખવડાવતા અને બગીચામાંથી તાજા શાકભાજી લેતા. આરવને આ મુલાકાતો સૌથી વધુ ગમતી હતી કારણ કે તેની દાદી હંમેશા તેના માટે તેની મનપસંદ મીઠાઈ, લાડુ બનાવતી હતી.''',
      questions: [
        PracticeQuestion(
          prompt: 'When did Aarav visit his grandmother?',
          options: ['Every winter', 'Every Sunday', 'Every summer', 'Only once'],
          correctIndex: 2,
          explanation: 'The passage says Aarav went to his grandmother\'s house every summer.',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'What did the grandmother tell Aarav every night?',
          options: ['Funny stories', 'Riddles', 'Poems', 'Songs'],
          correctIndex: 0,
          explanation: 'The passage says she told him funny stories every night before bed.',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'What did Aarav and his grandmother do in the morning?',
          options: [
            'They cleaned the house.',
            'They watched television.',
            'They fed the hens and picked vegetables.',
            'They went to the market.',
          ],
          correctIndex: 2,
          explanation: 'The passage says they fed the hens together and picked fresh vegetables.',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'What sweet did the grandmother make for Aarav?',
          options: ['Halwa', 'Jalebi', 'Barfi', 'Ladoo'],
          correctIndex: 3,
          explanation: 'The passage says his grandmother always made ladoo just for him.',
          difficulty: Difficulty.easy,
        ),
      ],
      glosses: [
        InlineGloss(word: 'village', meaningHi: 'गाँव', hiTransliteration: 'gaanv', meaningGu: 'ગામ', guTransliteration: 'gaam'),
        InlineGloss(word: 'funny', meaningHi: 'मज़ेदार', hiTransliteration: 'mazedaar', meaningGu: 'રમુજી', guTransliteration: 'ramuji'),
        InlineGloss(word: 'hens', meaningHi: 'मुर्गियाँ', hiTransliteration: 'murgiyaan', meaningGu: 'મરઘીઓ', guTransliteration: 'marghio'),
        InlineGloss(word: 'fresh', meaningHi: 'ताज़ा', hiTransliteration: 'taaza', meaningGu: 'તાજા', guTransliteration: 'taja'),
        InlineGloss(word: 'vegetables', meaningHi: 'सब्ज़ियाँ', hiTransliteration: 'sabziyaan', meaningGu: 'શાકભાજી', guTransliteration: 'shakbhaji'),
        InlineGloss(word: 'favourite', meaningHi: 'पसंदीदा', hiTransliteration: 'pasandeeda', meaningGu: 'મનપસંદ', guTransliteration: 'manpasand'),
      ],
    ),
    ReadingPassage(
      id: 'class3_reading_broken_toy',
      title: 'Kavya\'s Kind Heart',
      emoji: '🧸',
      grade: 'Class 3',
      difficulty: Difficulty.easy,
      body: 'At school, Kavya saw a new girl named Sana sitting alone. Sana had dropped her toy and it had '
          'broken. She looked very sad. Kavya walked up to her and smiled. She gave Sana one of her own '
          'toys to play with. Sana was surprised and happy. They played together the whole day. By the end '
          'of school, Sana had a new friend, and she was not sad anymore.',
      bodyHi: 'स्कूल में काव्या ने सना नाम की एक नई लड़की को अकेले बैठे देखा। सना ने अपना खिलौना गिरा दिया था और वह टूट गया था। वह बहुत उदास लग रही थी. काव्या उसके पास गई और मुस्कुराई। उसने सना को खेलने के लिए अपना एक खिलौना दिया। सना हैरान भी थी और खुश भी. वे पूरे दिन एक साथ खेलते रहे। स्कूल ख़त्म होने तक सना को एक नई दोस्त मिल गई और अब उसे कोई दुःख नहीं था।',
      bodyGu: '''શાળામાં, કાવ્યાએ સના નામની એક નવી છોકરીને એકલી બેઠેલી જોઈ. સનાનું રમકડું નીચે પડી ગયું હતું અને તે તૂટી ગયું હતું. તે ખૂબ ઉદાસ લાગતી હતી. કાવ્યા તેની પાસે ગઈ અને મલકાઈ. તેણે સનાને રમવા માટે પોતાનું એક રમકડું આપ્યું. સના આશ્ચર્યચકિત અને ખુશ થઈ. તેઓ આખો દિવસ સાથે રમ્યા. શાળા પૂરી થઈ ત્યાં સુધીમાં, સનાને એક નવી મિત્ર મળી ગઈ હતી, અને હવે તે ઉદાસ ન હતી.''',
      questions: [
        PracticeQuestion(
          prompt: 'Who was the new girl at school?',
          options: ['Meera', 'Riya', 'Sana', 'Kavya'],
          correctIndex: 2,
          explanation: 'The passage names the new girl as "Sana".',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'Why was Sana sad?',
          options: [
            'Her toy had broken.',
            'She forgot her lunch.',
            'She lost her bag.',
            'She was late for school.',
          ],
          correctIndex: 0,
          explanation: 'The passage says Sana had dropped her toy and it had broken.',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'What did Kavya do to help Sana?',
          options: [
            'She ignored her.',
            'She gave Sana one of her own toys.',
            'She told the teacher.',
            'She laughed at her.',
          ],
          correctIndex: 1,
          explanation: 'The passage says Kavya gave Sana one of her own toys to play with.',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'How did Sana feel by the end of school?',
          options: ['Scared', 'Still sad', 'Angry', 'Not sad anymore'],
          correctIndex: 3,
          explanation: 'The last sentence says Sana was not sad anymore after making a new friend.',
          difficulty: Difficulty.medium,
        ),
      ],
      glosses: [
        InlineGloss(word: 'alone', meaningHi: 'अकेला', hiTransliteration: 'akela', meaningGu: 'એકલા', guTransliteration: 'ekla'),
        InlineGloss(word: 'dropped', meaningHi: 'गिरा दिया', hiTransliteration: 'gira diya', meaningGu: 'પાડી દીધું', guTransliteration: 'padi didhu'),
        InlineGloss(word: 'broken', meaningHi: 'टूटा हुआ', hiTransliteration: 'toota hua', meaningGu: 'તૂટેલું', guTransliteration: 'tutelu'),
        InlineGloss(word: 'surprised', meaningHi: 'हैरान', hiTransliteration: 'hairaan', meaningGu: 'આશ્ચર્યચકિત', guTransliteration: 'aashcharyachakit'),
        InlineGloss(word: 'anymore', meaningHi: 'अब और नहीं', hiTransliteration: 'ab aur nahi', meaningGu: 'હવે નહીં', guTransliteration: 'have nahi'),
      ],
    ),
    ReadingPassage(
      id: 'class3_reading_rainbow',
      title: 'The Rainbow After the Rain',
      emoji: '🌈',
      grade: 'Class 3',
      difficulty: Difficulty.easy,
      body: 'One evening, it rained heavily near Naroda. Priya stood by her window and watched the raindrops '
          'fall. When the rain stopped, the sky turned orange and pink. Suddenly, Priya saw a big rainbow '
          'across the sky. It had many colours — red, yellow, green, and blue. Priya called her little '
          'brother to see it too. They counted the colours together and smiled at the beautiful sky.',
      bodyHi: 'एक शाम नरोदा के निकट भारी वर्षा हुई। प्रिया अपनी खिड़की के पास खड़ी होकर बारिश की बूंदों को गिरती हुई देख रही थी। जब बारिश रुकी तो आसमान नारंगी और गुलाबी हो गया। अचानक प्रिया को आसमान में एक बड़ा इंद्रधनुष दिखाई दिया। इसके कई रंग थे - लाल, पीला, हरा और नीला। प्रिया ने इसे देखने के लिए अपने छोटे भाई को भी बुलाया। उन्होंने एक साथ रंग गिने और सुंदर आकाश को देखकर मुस्कुराये।',
      bodyGu: '''એક સાંજે, નરોડા નજીક ભારે વરસાદ પડ્યો. પ્રિયા તેની બારી પાસે ઊભી રહી અને વરસાદના ટીપાં પડતાં જોતી રહી. જ્યારે વરસાદ બંધ થયો, ત્યારે આકાશ નારંગી અને ગુલાબી થઈ ગયું. અચાનક, પ્રિયાએ આકાશમાં એક મોટું મેઘધનુષ્ય જોયું. તેમાં ઘણા રંગો હતા - લાલ, પીળો, લીલો અને વાદળી. પ્રિયાએ તેના નાના ભાઈને પણ જોવા માટે બોલાવ્યો. તેઓએ એકસાથે રંગો ગણ્યા અને સુંદર આકાશ તરફ જોઈને મલકાયા.''',
      questions: [
        PracticeQuestion(
          prompt: 'Where did it rain heavily?',
          options: ['Near Naroda', 'Near Goa', 'Near Mumbai', 'Near Delhi'],
          correctIndex: 0,
          explanation: 'The passage says it rained heavily near Naroda.',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'What did Priya see after the rain stopped?',
          options: ['A rainbow', 'A kite', 'A bird', 'The moon'],
          correctIndex: 0,
          explanation: 'The passage says Priya saw a big rainbow across the sky.',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'What colours does the passage mention in the rainbow?',
          options: [
            'Black and white',
            'Red, yellow, green, and blue',
            'Pink and purple',
            'Only red',
          ],
          correctIndex: 1,
          explanation: 'The passage lists the colours red, yellow, green, and blue in the rainbow.',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'Who did Priya call to see the rainbow?',
          options: ['Her friend', 'Her teacher', 'Her mother', 'Her little brother'],
          correctIndex: 3,
          explanation: 'The passage says Priya called her little brother to see it too.',
          difficulty: Difficulty.easy,
        ),
      ],
      glosses: [
        InlineGloss(word: 'heavily', meaningHi: 'ज़ोर से', hiTransliteration: 'zor se', meaningGu: 'ખૂબ જોરથી', guTransliteration: 'khoob jorthi'),
        InlineGloss(word: 'raindrops', meaningHi: 'बारिश की बूंदें', hiTransliteration: 'baarish ki boondein', meaningGu: 'વરસાદના ટીપાં', guTransliteration: 'varsadna tipa'),
        InlineGloss(word: 'suddenly', meaningHi: 'अचानक', hiTransliteration: 'achanak', meaningGu: 'અચાનક', guTransliteration: 'achanak'),
        InlineGloss(word: 'colours', meaningHi: 'रंग', hiTransliteration: 'rang', meaningGu: 'રંગો', guTransliteration: 'rango'),
        InlineGloss(word: 'counted', meaningHi: 'गिने', hiTransliteration: 'gine', meaningGu: 'ગણ્યા', guTransliteration: 'ganya'),
        InlineGloss(word: 'beautiful', meaningHi: 'सुंदर', hiTransliteration: 'sundar', meaningGu: 'સુંદર', guTransliteration: 'sundar'),
      ],
    ),
    ReadingPassage(
      id: 'class3_reading_diwali_lamps',
      title: 'Diwali Lamps for Everyone',
      emoji: '🪔',
      grade: 'Class 3',
      difficulty: Difficulty.easy,
      body: 'Diwali was coming, and Ishaan\'s house was full of colours and lights. His mother bought many '
          'clay diyas from the market to decorate the house. Ishaan noticed that the old potter who made '
          'the diyas looked tired and worried, for very few people were buying from him this year. Ishaan '
          'asked his mother if they could buy more diyas than usual. His mother agreed, and they bought '
          'diyas for their neighbours too as gifts. The potter smiled brightly and thanked them. On Diwali '
          'night, every house on the street glowed with the potter\'s handmade diyas, and Ishaan felt proud '
          'that he had helped make the festival brighter for someone else.',
      bodyHi: 'दिवाली आ रही थी और ईशान का घर रंगों और रोशनी से भरा हुआ था। उनकी मां ने घर को सजाने के लिए बाजार से कई मिट्टी के दीये खरीदे. ईशान ने देखा कि दीये बनाने वाला बूढ़ा कुम्हार थका हुआ और चिंतित लग रहा था, क्योंकि इस साल बहुत कम लोग उससे खरीदारी कर रहे थे। ईशान ने अपनी मां से पूछा कि क्या वे सामान्य से अधिक दीये खरीद सकते हैं। उनकी मां सहमत हो गईं और उन्होंने अपने पड़ोसियों के लिए भी उपहार के रूप में दीये खरीदे। कुम्हार ने मुस्कुराते हुए उन्हें धन्यवाद दिया। दिवाली की रात, सड़क पर हर घर कुम्हार के हाथ से बने दीयों से जगमगा रहा था, और ईशान को गर्व महसूस हुआ कि उसने किसी और के लिए त्योहार को उज्ज्वल बनाने में मदद की है।',
      bodyGu: '''દિવાળી આવી રહી હતી, અને ઈશાનનું ઘર રંગો અને રોશનીથી ભરેલું હતું. તેની માતાએ ઘરને સજાવવા માટે બજારમાંથી માટીના ઘણા દીવા ખરીદ્યા. ઈશાને જોયું કે દીવા બનાવનાર વૃદ્ધ કુંભાર થાકેલો અને ચિંતિત દેખાતો હતો, કારણ કે આ વર્ષે બહુ ઓછા લોકો તેની પાસેથી ખરીદી રહ્યા હતા. ઈશાને તેની માતાને પૂછ્યું કે શું તેઓ સામાન્ય કરતાં વધુ દીવા ખરીદી શકે છે. તેની માતા સંમત થઈ, અને તેઓએ તેમના પડોશીઓ માટે પણ ભેટ તરીકે દીવા ખરીદ્યા. કુંભારે તેજસ્વી રીતે સ્મિત કર્યું અને તેમનો આભાર માન્યો. દિવાળીની રાત્રે, શેરીમાં દરેક ઘર કુંભારના હાથથી બનાવેલા દીવાઓથી ઝળહળી ઉઠ્યું, અને ઈશાનને ગર્વ અનુભવાયો કે તેણે બીજા કોઈ માટે તહેવારને વધુ ઉજ્જવળ બનાવવામાં મદદ કરી.''',
      questions: [
        PracticeQuestion(
          prompt: 'What festival was coming in the story?',
          options: ['Eid', 'Holi', 'Navratri', 'Diwali'],
          correctIndex: 3,
          explanation: 'The passage begins by saying Diwali was coming.',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'Why did the old potter look worried?',
          options: [
            'Very few people were buying from him.',
            'He had lost his shop.',
            'He had no clay left.',
            'His diyas were broken.',
          ],
          correctIndex: 0,
          explanation: 'The passage says the potter looked worried because very few people were buying from him this year.',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'What did Ishaan ask his mother to do?',
          options: [
            'Buy electric lights instead',
            'Buy more diyas than usual',
            'Ask for a discount',
            'Not buy any diyas',
          ],
          correctIndex: 1,
          explanation: 'The passage says Ishaan asked his mother if they could buy more diyas than usual.',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'How did Ishaan feel at the end of the story?',
          options: ['Angry', 'Bored', 'Sad', 'Proud that he helped'],
          correctIndex: 3,
          explanation: 'The last sentence says Ishaan felt proud that he had helped make the festival brighter for someone else.',
          difficulty: Difficulty.medium,
        ),
      ],
      glosses: [
        InlineGloss(word: 'clay diyas', meaningHi: 'मिट्टी के दीये', hiTransliteration: 'mitti ke diye', meaningGu: 'માટીના દીવા', guTransliteration: 'matina diva'),
        InlineGloss(word: 'potter', meaningHi: 'कुम्हार', hiTransliteration: 'kumhaar', meaningGu: 'કુંભાર', guTransliteration: 'kumbhar'),
        InlineGloss(word: 'worried', meaningHi: 'चिंतित', hiTransliteration: 'chintit', meaningGu: 'ચિંતિત', guTransliteration: 'chintit'),
        InlineGloss(word: 'neighbours', meaningHi: 'पड़ोसी', hiTransliteration: 'padosi', meaningGu: 'પડોશીઓ', guTransliteration: 'padoshio'),
        InlineGloss(word: 'brightly', meaningHi: 'चमकते हुए', hiTransliteration: 'chamakte hue', meaningGu: 'તેજસ્વી રીતે', guTransliteration: 'tejasvi rite'),
        InlineGloss(word: 'glowed', meaningHi: 'रोशनी से जगमगाया', hiTransliteration: 'roshni se jagmagaya', meaningGu: 'ઝળહળી ઉઠ્યું', guTransliteration: 'zalhali uthyu'),
        InlineGloss(word: 'festival', meaningHi: 'त्योहार', hiTransliteration: 'tyohaar', meaningGu: 'તહેવાર', guTransliteration: 'tahevar'),
      ],
    ),
    ReadingPassage(
      id: 'class3_reading_race_friendship',
      title: 'The Race and the Fall',
      emoji: '🏃',
      grade: 'Class 3',
      difficulty: Difficulty.easy,
      body: 'On Sports Day, Dev and Om were the fastest runners in Class 3. Both wanted to win the running '
          'race very badly. When the whistle blew, they ran as fast as they could. Suddenly, Om tripped over '
          'a small stone and fell down, hurting his knee. Dev was ahead and could have easily won the race. '
          'But he stopped, turned back, and helped Om stand up. They crossed the finish line together, last '
          'of all the runners. Their teacher smiled and said that true sportsmanship was worth more than any '
          'medal. Dev and Om laughed and promised to race again the next year.',
      bodyHi: 'खेल दिवस पर, देव और ओम कक्षा 3 में सबसे तेज़ धावक थे। दोनों दौड़ की दौड़ को बहुत बुरी तरह से जीतना चाहते थे। जब सीटी बजी तो वे जितनी तेजी से भाग सकते थे दौड़े। अचानक, ओम एक छोटे पत्थर से फिसल गया और नीचे गिर गया, जिससे उसके घुटने में चोट लग गई। देव आगे था और आसानी से रेस जीत सकता था। लेकिन वह रुका, पीछे मुड़ा और ओम को खड़ा होने में मदद की। उन्होंने सभी धावकों में से सबसे अंत में एक साथ फिनिश लाइन पार की। उनके शिक्षक मुस्कुराए और कहा कि सच्ची खेल भावना किसी भी पदक से अधिक मूल्यवान है। देव और ओम हँसे और अगले साल फिर से दौड़ लगाने का वादा किया।',
      bodyGu: '''રમતગમત દિવસ પર, દેવ અને ઓમ ધોરણ 3 માં સૌથી ઝડપી દોડવીર હતા. બંને દોડવાની સ્પર્ધા ખૂબ જ ખરાબ રીતે જીતવા માંગતા હતા. જ્યારે સિસોટી વાગી, ત્યારે તેઓ બને તેટલી ઝડપથી દોડ્યા. અચાનક, ઓમ એક નાના પથ્થર સાથે અથડાઈને નીચે પડી ગયો, અને તેના ઘૂંટણમાં ઈજા થઈ. દેવ આગળ હતો અને તે સરળતાથી રેસ જીતી શક્યો હોત. પરંતુ તે અટક્યો, પાછો ફર્યો, અને ઓમને ઊભા થવામાં મદદ કરી. તેઓએ એકસાથે ફિનિશ લાઇન પાર કરી, બધા દોડવીરોમાં સૌથી છેલ્લે. તેમના શિક્ષક હસ્યા અને કહ્યું કે સાચી ખેલદિલી કોઈ પણ મેડલ કરતાં વધુ મૂલ્યવાન છે. દેવ અને ઓમ હસ્યા અને આવતા વર્ષે ફરીથી દોડવાનું વચન આપ્યું.''',
      questions: [
        PracticeQuestion(
          prompt: 'What happened to Om during the race?',
          options: [
            'He won the race.',
            'He tripped over a stone and fell.',
            'He stopped running on purpose.',
            'He left the race early.',
          ],
          correctIndex: 1,
          explanation: 'The passage says Om tripped over a small stone and fell down, hurting his knee.',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'What did Dev do when he saw Om fall?',
          options: [
            'He kept running to win.',
            'He laughed at Om.',
            'He stopped and helped Om stand up.',
            'He called for the teacher.',
          ],
          correctIndex: 2,
          explanation: 'The passage says Dev stopped, turned back, and helped Om stand up.',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'How did Dev and Om finish the race?',
          options: [
            'Dev finished first alone.',
            'They crossed the finish line together, last of all.',
            'Neither of them finished.',
            'Om finished first alone.',
          ],
          correctIndex: 1,
          explanation: 'The passage says they crossed the finish line together, last of all the runners.',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'What did the teacher say was worth more than a medal?',
          options: ['Speed', 'True sportsmanship', 'Prize money', 'Fame'],
          correctIndex: 1,
          explanation: 'The passage says the teacher smiled and said that true sportsmanship was worth more than any medal.',
          difficulty: Difficulty.medium,
        ),
      ],
      glosses: [
        InlineGloss(word: 'fastest', meaningHi: 'सबसे तेज़', hiTransliteration: 'sabse tez', meaningGu: 'સૌથી ઝડપી', guTransliteration: 'sauthi jhadapi'),
        InlineGloss(word: 'whistle', meaningHi: 'सीटी', hiTransliteration: 'seeti', meaningGu: 'સિસોટી', guTransliteration: 'sisoti'),
        InlineGloss(word: 'tripped', meaningHi: 'ठोकर खाकर गिरना', hiTransliteration: 'thokar khaakar girna', meaningGu: 'ઠોકર ખાવી', guTransliteration: 'thokar khavi'),
        InlineGloss(word: 'hurting', meaningHi: 'चोट लगना', hiTransliteration: 'chot lagna', meaningGu: 'ઈજા પહોંચાડવી', guTransliteration: 'ija pahonchadvi'),
        InlineGloss(word: 'ahead', meaningHi: 'आगे', hiTransliteration: 'aage', meaningGu: 'આગળ', guTransliteration: 'aagal'),
        InlineGloss(word: 'sportsmanship', meaningHi: 'खेल भावना', hiTransliteration: 'khel bhaavna', meaningGu: 'ખેલદિલી', guTransliteration: 'kheldili'),
        InlineGloss(word: 'medal', meaningHi: 'पदक', hiTransliteration: 'padak', meaningGu: 'ચંદ્રક', guTransliteration: 'chandrak'),
      ],
    ),
    ReadingPassage(
      id: 'class3_reading_ant_line',
      title: 'The Line of Ants',
      emoji: '🐜',
      grade: 'Class 3',
      difficulty: Difficulty.easy,
      body: 'While eating an orange in the garden, Diya dropped a small piece on the ground. Within minutes, '
          'a line of tiny ants appeared from a crack near the wall. Diya sat still and watched carefully. '
          'One ant found the piece of orange first and touched another ant with its feelers. Soon, many more '
          'ants came in a straight line, working together to carry the piece back to their hole. Diya was '
          'amazed that such tiny creatures could carry something bigger than themselves by helping each '
          'other. She ran to tell her father, who explained that ants always work as a team and never leave '
          'a job unfinished. Diya decided to watch the ants every day after that.',
      bodyHi: 'बगीचे में संतरा खाते समय दीया ने एक छोटा सा टुकड़ा जमीन पर गिरा दिया। कुछ ही मिनटों में दीवार के पास एक दरार से छोटी-छोटी चींटियों की एक कतार दिखाई दी। दीया शांत बैठी रही और ध्यान से देखती रही। एक चींटी को सबसे पहले संतरे का टुकड़ा मिला और उसने अपने फीलर्स से दूसरी चींटी को छुआ। जल्द ही, कई और चींटियाँ एक सीधी रेखा में आ गईं, और टुकड़े को अपने बिल में वापस ले जाने के लिए एक साथ काम करने लगीं। दीया इस बात से आश्चर्यचकित थी कि इतने छोटे जीव एक-दूसरे की मदद करके अपने से भी बड़ी चीज़ ले जा सकते हैं। वह दौड़कर अपने पिता को बताने गई, जिन्होंने समझाया कि चींटियाँ हमेशा एक टीम के रूप में काम करती हैं और कभी भी कोई काम अधूरा नहीं छोड़तीं। इसके बाद दीया ने हर दिन चींटियों को देखने का फैसला किया।',
      bodyGu: '''બગીચામાં નારંગી ખાતી વખતે દિયાએ એક નાનો ટુકડો જમીન પર પાડી દીધો. થોડીવારમાં દિવાલ પાસેની તિરાડમાંથી નાની કીડીઓની લાઈન દેખાઈ. દિયા શાંત બેસી રહી અને ધ્યાનથી જોતી રહી. એક કીડીને પહેલા નારંગીનો ટુકડો મળ્યો અને તેણે તેના સ્પર્શકોથી બીજી કીડીને સ્પર્શ કર્યો. થોડી જ વારમાં બીજી ઘણી કીડીઓ સીધી લાઇનમાં આવી, અને ટુકડાને પાછા તેમના દરમાં લઈ જવા માટે સાથે મળીને કામ કરવા લાગી. દિયાને નવાઈ લાગી કે આવા નાના જીવો એકબીજાને મદદ કરીને પોતાના કરતા પણ મોટી વસ્તુ ઉઠાવી શકે છે. તે દોડીને તેના પિતાને કહેવા ગઈ, જેમણે સમજાવ્યું કે કીડીઓ હંમેશા એક ટીમ તરીકે કામ કરે છે અને ક્યારેય કોઈ કામ અધૂરું છોડતી નથી. દિયાએ તે પછી દરરોજ કીડીઓ જોવાનું નક્કી કર્યું.''',
      questions: [
        PracticeQuestion(
          prompt: 'What did Diya drop on the ground?',
          options: ['A piece of orange', 'A flower', 'A leaf', 'A biscuit'],
          correctIndex: 0,
          explanation: 'The passage says Diya dropped a small piece of orange on the ground.',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'How did the first ant tell the others about the food?',
          options: [
            'It carried the food alone.',
            'It touched another ant with its feelers.',
            'It made a loud sound.',
            'It ran back to the hole silently.',
          ],
          correctIndex: 1,
          explanation: 'The passage says the ant touched another ant with its feelers to tell it about the food.',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'What amazed Diya about the ants?',
          options: [
            'They could fly.',
            'They lived inside the orange.',
            'They could carry something bigger than themselves by helping each other.',
            'They were very colourful.',
          ],
          correctIndex: 2,
          explanation: 'The passage says Diya was amazed that tiny creatures could carry something bigger than themselves by helping each other.',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'According to Diya\'s father, how do ants always work?',
          options: ['Very slowly', 'Only at night', 'As a team', 'Alone'],
          correctIndex: 2,
          explanation: 'The passage says her father explained that ants always work as a team and never leave a job unfinished.',
          difficulty: Difficulty.easy,
        ),
      ],
      glosses: [
        InlineGloss(word: 'appeared', meaningHi: 'दिखाई दिया', hiTransliteration: 'dikhai diya', meaningGu: 'દેખાઈ', guTransliteration: 'dekhai'),
        InlineGloss(word: 'crack', meaningHi: 'दरार', hiTransliteration: 'daraar', meaningGu: 'તિરાડ', guTransliteration: 'tirad'),
        InlineGloss(word: 'feelers', meaningHi: 'कीड़े के स्पर्श अंग', hiTransliteration: 'keede ke sparsh ang', meaningGu: 'સ્પર્શકો', guTransliteration: 'sparshako'),
        InlineGloss(word: 'amazed', meaningHi: 'हैरान', hiTransliteration: 'hairaan', meaningGu: 'આશ્ચર્યચકિત', guTransliteration: 'aashcharyachakit'),
        InlineGloss(word: 'creatures', meaningHi: 'जीव', hiTransliteration: 'jeev', meaningGu: 'જીવો', guTransliteration: 'jeevo'),
        InlineGloss(word: 'unfinished', meaningHi: 'अधूरा', hiTransliteration: 'adhoora', meaningGu: 'અધૂરું', guTransliteration: 'adhuru'),
      ],
    ),
    ReadingPassage(
      id: 'class3_reading_old_neighbour',
      title: 'Helping Mrs. Fernandes',
      emoji: '🛒',
      grade: 'Class 3',
      difficulty: Difficulty.easy,
      body: 'Mrs. Fernandes was an elderly lady who lived alone next door to Sameer\'s family. She walked '
          'slowly with a stick and found it hard to carry heavy bags. One afternoon, Sameer saw her '
          'struggling to carry a big bag of vegetables from the gate to her door. He ran over quickly and '
          'offered to carry the bag for her. Mrs. Fernandes was grateful and invited him in for a glass of '
          'cold lemonade. After that day, Sameer began visiting her every evening to check if she needed any '
          'help with shopping or small chores. Mrs. Fernandes told Sameer\'s mother that he had become like a '
          'grandson to her, and Sameer felt very happy to hear that.',
      bodyHi: 'श्रीमती फर्नांडिस एक बुजुर्ग महिला थीं जो समीर के परिवार के बगल में अकेली रहती थीं। वह छड़ी के सहारे धीरे-धीरे चलती थी और उसे भारी बैग उठाने में कठिनाई होती थी। एक दोपहर, समीर ने उसे गेट से अपने दरवाजे तक सब्जियों का एक बड़ा बैग ले जाने के लिए संघर्ष करते देखा। वह तेजी से भागा और उसके लिए बैग ले जाने की पेशकश की। श्रीमती फर्नांडिस आभारी थीं और उन्होंने उन्हें एक गिलास ठंडे नींबू पानी के लिए आमंत्रित किया। उस दिन के बाद, समीर हर शाम उसके पास यह देखने के लिए जाने लगा कि क्या उसे खरीदारी या छोटे-मोटे कामों में किसी मदद की ज़रूरत है। श्रीमती फर्नांडिस ने समीर की मां को बताया कि वह उनके लिए पोते की तरह बन गया है, यह सुनकर समीर को बहुत खुशी हुई।',
      bodyGu: '''શ્રીમતી ફર્નાન્ડિસ એક વૃદ્ધ મહિલા હતા જે સમીરના પરિવારની બાજુમાં એકલા રહેતા હતા. તે લાકડીના ટેકે ધીમે ધીમે ચાલતા હતા અને તેમને ભારે બેગ ઉપાડવામાં મુશ્કેલી પડતી હતી. એક બપોરે, સમીરે તેમને ગેટથી તેમના દરવાજા સુધી શાકભાજીની એક મોટી બેગ લઈ જવા માટે સંઘર્ષ કરતા જોયા. તે ઝડપથી દોડી ગયો અને તેમના માટે બેગ લઈ જવાની ઓફર કરી. શ્રીમતી ફર્નાન્ડિસ આભારી હતા અને તેમણે તેને એક ગ્લાસ ઠંડા લીંબુ શરબત માટે અંદર બોલાવ્યો. તે દિવસ પછી, સમીરે દરરોજ સાંજે તેમની મુલાકાત લેવાનું શરૂ કર્યું જેથી તે જોઈ શકે કે તેમને ખરીદી કે નાના કામોમાં કોઈ મદદની જરૂર છે કે નહીં. શ્રીમતી ફર્નાન્ડિસે સમીરની માતાને કહ્યું કે તે તેમના માટે પૌત્ર જેવો બની ગયો છે, અને તે સાંભળીને સમીરને ખૂબ આનંદ થયો.''',
      questions: [
        PracticeQuestion(
          prompt: 'Why did Mrs. Fernandes find it hard to carry heavy bags?',
          options: [
            'She did not like carrying bags.',
            'She had an injured hand.',
            'She was in a hurry.',
            'She was elderly and walked slowly with a stick.',
          ],
          correctIndex: 3,
          explanation: 'The passage says she was an elderly lady who walked slowly with a stick and found it hard to carry heavy bags.',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'What did Sameer do when he saw her struggling?',
          options: [
            'He offered to carry the bag for her.',
            'He walked away.',
            'He called his mother instead.',
            'He asked her to carry it herself.',
          ],
          correctIndex: 0,
          explanation: 'The passage says Sameer ran over quickly and offered to carry the bag for her.',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'What did Sameer start doing every evening after that day?',
          options: [
            'Visiting Mrs. Fernandes to help with shopping or chores',
            'Going to the market alone',
            'Playing video games',
            'Avoiding his neighbours',
          ],
          correctIndex: 0,
          explanation: 'The passage says Sameer began visiting her every evening to check if she needed any help with shopping or small chores.',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'What did Mrs. Fernandes say about Sameer to his mother?',
          options: [
            'That he was too busy to visit',
            'That he should study more',
            'That he was too noisy',
            'That he had become like a grandson to her',
          ],
          correctIndex: 3,
          explanation: 'The passage says Mrs. Fernandes told Sameer\'s mother that he had become like a grandson to her.',
          difficulty: Difficulty.medium,
        ),
      ],
      glosses: [
        InlineGloss(word: 'elderly', meaningHi: 'बुज़ुर्ग', hiTransliteration: 'buzurg', meaningGu: 'વૃદ્ધ', guTransliteration: 'vruddh'),
        InlineGloss(word: 'struggling', meaningHi: 'मुश्किल से कर पाना', hiTransliteration: 'mushkil se kar paana', meaningGu: 'સંઘર્ષ કરતા', guTransliteration: 'sangharsh karta'),
        InlineGloss(word: 'offered', meaningHi: 'पेशकश की', hiTransliteration: 'peshkash ki', meaningGu: 'ઓફર કરી', guTransliteration: 'offer kari'),
        InlineGloss(word: 'grateful', meaningHi: 'आभारी', hiTransliteration: 'aabhaari', meaningGu: 'આભારી', guTransliteration: 'aabhari'),
        InlineGloss(word: 'lemonade', meaningHi: 'नींबू पानी', hiTransliteration: 'neembu paani', meaningGu: 'લીંબુ શરબત', guTransliteration: 'limbu sharbat'),
        InlineGloss(word: 'chores', meaningHi: 'घर के छोटे-मोटे काम', hiTransliteration: 'ghar ke chote-mote kaam', meaningGu: 'નાના કામો', guTransliteration: 'nana kamo'),
        InlineGloss(word: 'grandson', meaningHi: 'पोता', hiTransliteration: 'pota', meaningGu: 'પૌત્ર', guTransliteration: 'pautra'),
      ],
    ),
  ],
);
