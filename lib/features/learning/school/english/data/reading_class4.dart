import '../models/chapter.dart' show InlineGloss;
import '../models/practice_question.dart';
import '../models/reading_passage.dart';

const class4Reading = ReadingLibrary(
  id: 'class4_reading',
  title: 'Reading Passages',
  grade: 'Class 4',
  passages: [
    ReadingPassage(
      id: 'class4_reading_elephant',
      title: 'The Kind Elephant',
      emoji: '🐘',
      grade: 'Class 4',
      difficulty: Difficulty.easy,
      body: 'Raju was a big grey elephant who lived near a small village. Every morning, he walked to the '
          'river to drink water. One day, Raju saw a little girl crying beside the river. Her ball had '
          'fallen into the water and floated far from the bank. Raju walked slowly into the river, picked '
          'up the ball gently with his long trunk, and placed it in the girl\'s hands. The girl smiled and '
          'thanked Raju. After that day, the girl visited Raju every evening with fresh fruits.',
      bodyHi: 'राजू एक बड़ा भूरा हाथी था जो एक छोटे से गाँव के पास रहता था। वह हर सुबह पानी पीने के लिए नदी पर जाता था। एक दिन, राजू ने एक छोटी लड़की को नदी के किनारे रोते हुए देखा। उसकी गेंद पानी में गिर गई थी और किनारे से बहुत दूर तैर गई थी। राजू धीरे-धीरे नदी में चला गया, अपनी लंबी सूंड से गेंद को धीरे से उठाया और लड़की के हाथों में रख दिया। लड़की ने मुस्कुराते हुए राजू को धन्यवाद दिया। उस दिन के बाद, लड़की हर शाम ताजे फल लेकर राजू के पास जाती थी।',
      bodyGu: '''રાજુ એક મોટો ભૂખરો હાથી હતો જે એક નાના ગામ પાસે રહેતો હતો. તે રોજ સવારે પાણી પીવા માટે નદીએ જતો. એક દિવસ, રાજુએ એક નાની છોકરીને નદી કિનારે રડતી જોઈ. તેનો દડો પાણીમાં પડી ગયો હતો અને કિનારાથી ખૂબ દૂર તરવા લાગ્યો હતો. રાજુ ધીમે ધીમે નદીમાં ગયો, પોતાની લાંબી સૂંઢથી દડાને હળવેથી ઉઠાવ્યો અને છોકરીના હાથમાં મૂકી દીધો. છોકરીએ હસીને રાજુનો આભાર માન્યો. તે દિવસ પછી, છોકરી રોજ સાંજે તાજા ફળ લઈને રાજુ પાસે જતી.''',
      questions: [
        PracticeQuestion(
          prompt: 'What is the name of the elephant in the story?',
          options: ['Ravi', 'Ramu', 'Raja', 'Raju'],
          correctIndex: 3,
          explanation: 'The passage names the elephant "Raju" in the very first sentence.',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'Why was the little girl crying?',
          options: [
            'She was lost in the village.',
            'She had hurt her leg.',
            'Her ball had fallen into the river.',
            'She was afraid of the elephant.',
          ],
          correctIndex: 2,
          explanation: 'The passage says her ball had fallen into the water and floated away, which made her cry.',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'How did Raju pick up the ball?',
          options: ['With his trunk', 'With his feet', 'With his mouth', 'He could not pick it up'],
          correctIndex: 0,
          explanation: 'The passage says Raju "picked up the ball gently with his long trunk".',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'What did the girl do every evening after that day?',
          options: [
            'She told her friends to stay away from Raju.',
            'She played with her ball alone.',
            'She visited Raju with fresh fruits.',
            'She avoided the river.',
          ],
          correctIndex: 2,
          explanation: 'The last sentence says she visited Raju every evening with fresh fruits.',
          difficulty: Difficulty.medium,
        ),
      ],
      glosses: [
        InlineGloss(word: 'grey', meaningHi: 'धूसर रंग का', hiTransliteration: 'dhoosar rang ka', meaningGu: 'ભૂખરો રંગ', guTransliteration: 'bhukhro rang'),
        InlineGloss(word: 'village', meaningHi: 'गाँव', hiTransliteration: 'gaanv', meaningGu: 'ગામ', guTransliteration: 'gaam'),
        InlineGloss(word: 'floated', meaningHi: 'तैरना', hiTransliteration: 'tairna', meaningGu: 'તરવા લાગ્યો / તર્યું', guTransliteration: 'tarva laagyo / taryu'),
        InlineGloss(word: 'bank', meaningHi: 'नदी का किनारा', hiTransliteration: 'nadi ka kinara', meaningGu: 'નદીનો કિનારો', guTransliteration: 'nadino kinaro'),
        InlineGloss(word: 'gently', meaningHi: 'धीरे से, प्यार से', hiTransliteration: 'dheere se, pyaar se', meaningGu: 'ધીમેથી, હળવેથી', guTransliteration: 'dhimethi, halwethi'),
        InlineGloss(word: 'trunk', meaningHi: 'हाथी की सूंड', hiTransliteration: 'haathi ki soond', meaningGu: 'હાથીની સૂંઢ', guTransliteration: 'haathini sundh'),
        InlineGloss(word: 'thanked', meaningHi: 'धन्यवाद कहा', hiTransliteration: 'dhanyavaad kaha', meaningGu: 'આભાર માન્યો', guTransliteration: 'aabhar maanyo'),
      ],
    ),
    ReadingPassage(
      id: 'class4_reading_farmer',
      title: 'Kisan and the Rainy Season',
      emoji: '🌾',
      grade: 'Class 4',
      difficulty: Difficulty.easy,
      body: 'Kisan was a farmer who lived in a small village near Naroda. Every year, before the monsoon '
          'arrived, he ploughed his field and prepared it for sowing wheat. This year, the rain came early. '
          'Dark clouds filled the sky, and soon it began to pour. Kisan smiled, because rain meant good crops. '
          'He and his family worked together, planting seeds row by row under a light drizzle. By evening, '
          'the whole field was ready, and a bright rainbow appeared across the sky.',
      bodyHi: 'किसन एक किसान था जो नरोदा के पास एक छोटे से गाँव में रहता था। हर साल, मानसून आने से पहले, वह अपने खेत की जुताई करके उसे गेहूं की बुआई के लिए तैयार करता था। इस साल बारिश जल्दी हो गई. आसमान में काले बादल छा गए और जल्द ही बारिश शुरू हो गई। किसान मुस्कुराया, क्योंकि बारिश का मतलब था अच्छी फसल। उन्होंने और उनके परिवार ने एक साथ काम किया, हल्की बूंदाबांदी के तहत पंक्ति दर पंक्ति बीज बोए। शाम तक, पूरा मैदान तैयार हो गया, और आकाश में एक चमकीला इंद्रधनुष दिखाई दिया।',
      bodyGu: '''કિસન એક ખેડૂત હતો જે નરોડા પાસેના એક નાના ગામમાં રહેતો હતો. દર વર્ષે, ચોમાસું આવતા પહેલા, તે તેના ખેતરને ખેડીને ઘઉં વાવવા માટે તૈયાર કરતો હતો. આ વર્ષે વરસાદ વહેલો આવી ગયો. આકાશમાં કાળા વાદળો છવાઈ ગયા અને ટૂંક સમયમાં વરસાદ શરૂ થઈ ગયો. કિસાન મલકાયો, કારણ કે વરસાદનો અર્થ સારો પાક હતો. તેણે અને તેના પરિવારે સાથે મળીને કામ કર્યું, હળવા ઝરમર વરસાદ હેઠળ હારબંધ બીજ વાવ્યા. સાંજ સુધીમાં, આખું ખેતર તૈયાર થઈ জ্ঞું, અને આકાશમાં એક ચમકતું મેઘધનુષ્ય દેખાયું.''',
      questions: [
        PracticeQuestion(
          prompt: 'What is Kisan\'s job?',
          options: ['Doctor', 'Driver', 'Farmer', 'Teacher'],
          correctIndex: 2,
          explanation: 'The first sentence says "Kisan was a farmer".',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'What did Kisan prepare his field for?',
          options: ['Building a house', 'Playing cricket', 'Keeping cattle', 'Sowing wheat'],
          correctIndex: 3,
          explanation: 'The passage says he "prepared it for sowing wheat".',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'Why was Kisan happy when it started raining?',
          options: [
            'Because his friends were visiting.',
            'Because he wanted to stop working.',
            'Because rain meant good crops.',
            'Because he liked getting wet.',
          ],
          correctIndex: 2,
          explanation: 'The passage says "Kisan smiled, because rain meant good crops."',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'What appeared in the sky by evening?',
          options: ['A kite', 'The moon', 'A rainbow', 'Snow'],
          correctIndex: 2,
          explanation: 'The last sentence mentions "a bright rainbow appeared across the sky".',
          difficulty: Difficulty.easy,
        ),
      ],
      glosses: [
        InlineGloss(word: 'monsoon', meaningHi: 'बारिश का मौसम', hiTransliteration: 'baarish ka mausam', meaningGu: 'ચોમાસું', guTransliteration: 'chomasu'),
        InlineGloss(word: 'ploughed', meaningHi: 'हल चलाना', hiTransliteration: 'hal chalana', meaningGu: 'ખેડ્યું', guTransliteration: 'khedyu'),
        InlineGloss(word: 'sowing', meaningHi: 'बीज बोना', hiTransliteration: 'beej bona', meaningGu: 'વાવણી', guTransliteration: 'vavni'),
        InlineGloss(word: 'pour', meaningHi: 'ज़ोर से बरसना', hiTransliteration: 'zor se barasna', meaningGu: 'ધોધમાર વરસવું', guTransliteration: 'dhodhmar varasvu'),
        InlineGloss(word: 'crops', meaningHi: 'फसल', hiTransliteration: 'fasal', meaningGu: 'પાક', guTransliteration: 'paak'),
        InlineGloss(word: 'drizzle', meaningHi: 'हल्की बूंदाबांदी', hiTransliteration: 'halki boondaabaandi', meaningGu: 'ઝરમર વરસાદ', guTransliteration: 'zharmar varsad'),
        InlineGloss(word: 'rainbow', meaningHi: 'इंद्रधनुष', hiTransliteration: 'indradhanush', meaningGu: 'મેઘધનુષ્ય', guTransliteration: 'meghdhanushya'),
      ],
    ),
    ReadingPassage(
      id: 'class4_reading_school_day',
      title: 'Meera\'s First Day at a New School',
      emoji: '🎒',
      grade: 'Class 4',
      difficulty: Difficulty.medium,
      body: 'Meera felt nervous as she walked through the gates of her new school. Her family had just '
          'moved to Naroda, and everything felt unfamiliar. In her classroom, she sat quietly near the '
          'window, holding her new notebook tightly. During recess, a girl named Ishita offered to share '
          'her lunch with Meera and asked her to join a game in the playground. By the end of the day, '
          'Meera had made her first friend, and her new school did not feel so strange anymore.',
      bodyHi: 'जब मीरा अपने नए स्कूल के द्वार से गुज़री तो उसे घबराहट महसूस हुई। उसका परिवार अभी-अभी नरोदा आया था, और सब कुछ अपरिचित लग रहा था। अपनी कक्षा में, वह अपनी नई नोटबुक को कसकर पकड़े हुए, खिड़की के पास चुपचाप बैठी थी। अवकाश के दौरान, इशिता नाम की एक लड़की ने मीरा के साथ अपना दोपहर का भोजन साझा करने की पेशकश की और उसे खेल के मैदान में एक खेल में शामिल होने के लिए कहा। दिन के अंत तक, मीरा ने अपनी पहली दोस्त बना ली थी, और उसका नया स्कूल अब इतना अजीब नहीं लग रहा था।',
      bodyGu: '''જ્યારે મીરા તેના નવા શાળાના દરવાજામાંથી પસાર થઈ ત્યારે તેને ગભરામણ અનુભવાઈ. તેનો પરિવાર હમણાં જ નરોડા આવ્યો હતો, અને બધું અજાણ્યું લાગી રહ્યું હતું. તેના વર્ગખંડમાં, તે તેની નવી નોટબુકને મજબૂતાઈથી પકડીને બારી પાસે શાંતિથી બેઠી હતી. રિસેસ દરમિયાન, ઇશિતા નામની એક છોકરીએ મીરા સાથે તેનું બપોરનું ભોજન વહેંચવાની ઓફર કરી અને તેને રમતના મેદાનમાં એક રમતમાં જોડાવા માટે કહ્યું. દિવસના અંત સુધીમાં, મીરાએ તેની પહેલી મિત્ર બનાવી લીધી હતી, અને તેની નવી શાળા હવે એટલી અજીબ નહોતી લાગી રહી.''',
      questions: [
        PracticeQuestion(
          prompt: 'Why did Meera feel nervous?',
          options: [
            'It was her first day at a new school.',
            'She forgot her homework.',
            'She lost her notebook.',
            'She was late for class.',
          ],
          correctIndex: 0,
          explanation: 'The passage opens with Meera feeling nervous on her first day at the new school.',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'Where did Meera and her family recently move?',
          options: ['Goa', 'Naroda', 'Mumbai', 'Delhi'],
          correctIndex: 1,
          explanation: 'The passage says "Her family had just moved to Naroda."',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'What did Ishita do during recess?',
          options: [
            'She ignored Meera.',
            'She asked the teacher for help.',
            'She left the classroom.',
            'She shared her lunch and invited Meera to play.',
          ],
          correctIndex: 3,
          explanation: 'The passage says Ishita "offered to share her lunch...and asked her to join a game".',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'How did Meera feel by the end of the day?',
          options: [
            'Happy, because she made a friend',
            'Angry with her classmates',
            'Ready to go back to her old school',
            'Still lonely and scared',
          ],
          correctIndex: 0,
          explanation: 'The passage says her new school "did not feel so strange anymore" after making a friend.',
          difficulty: Difficulty.medium,
        ),
      ],
      glosses: [
        InlineGloss(word: 'nervous', meaningHi: 'घबराया हुआ', hiTransliteration: 'ghabraaya hua', meaningGu: 'ગભરાયેલું', guTransliteration: 'gabharaayelu'),
        InlineGloss(word: 'gates', meaningHi: 'फाटक, गेट', hiTransliteration: 'phaatak, get', meaningGu: 'દરવાજા, ગેટ', guTransliteration: 'darvaja, get'),
        InlineGloss(word: 'unfamiliar', meaningHi: 'अनजाना, नया-नया', hiTransliteration: 'anjaana, naya-naya', meaningGu: 'અજાણ્યું', guTransliteration: 'ajaanyu'),
        InlineGloss(word: 'recess', meaningHi: 'स्कूल में खेलने की छुट्टी', hiTransliteration: 'school mein khelne ki chhutti', meaningGu: 'રિસેસ, વિરામનો સમય', guTransliteration: 'rises, viramno samay'),
        InlineGloss(word: 'offered', meaningHi: 'पेशकश की, दिया', hiTransliteration: 'peshkash ki, diya', meaningGu: 'ઓફર કરી, પ્રસ્તાવ મૂક્યો', guTransliteration: 'ofar kari, prastav mukyo'),
        InlineGloss(word: 'strange', meaningHi: 'अजीब, अनजाना', hiTransliteration: 'ajeeb, anjaana', meaningGu: 'અજીબ, વિચિત્ર', guTransliteration: 'ajib, vichitra'),
      ],
    ),
    ReadingPassage(
      id: 'class4_reading_market',
      title: 'A Trip to the Vegetable Market',
      emoji: '🥕',
      grade: 'Class 4',
      difficulty: Difficulty.medium,
      body: 'Every Sunday morning, Arjun went to the vegetable market with his mother. The market was full '
          'of colours — red tomatoes, green spinach, orange carrots, and purple brinjals were stacked in '
          'neat piles. Arjun\'s mother carefully chose fresh vegetables, checking each one before putting it '
          'in her basket. Arjun loved helping her carry the smaller bags. On the way home, they stopped at a '
          'small stall to buy sweet, juicy mangoes, Arjun\'s favourite fruit.',
      bodyHi: 'हर रविवार सुबह अर्जुन अपनी मां के साथ सब्जी बाजार जाता था। बाज़ार रंगों से भरा हुआ था - लाल टमाटर, हरी पालक, नारंगी गाजर, और बैंगनी बैंगन साफ-सुथरे ढेरों में रखे हुए थे। अर्जुन की माँ ने सावधानी से ताज़ी सब्जियाँ चुनीं, अपनी टोकरी में रखने से पहले हर एक की जाँच की। अर्जुन को छोटे बैग ले जाने में उसकी मदद करना बहुत पसंद था। घर के रास्ते में, वे मीठे, रसीले आम, अर्जुन का पसंदीदा फल खरीदने के लिए एक छोटी सी दुकान पर रुके।',
      bodyGu: '''દર રવિવારે સવારે, અર્જુન તેની માતા સાથે શાકભાજી માર્કેટમાં જતો હતો. માર્કેટ રંગોથી ભરેલું હતું - લાલ ટામેટાં, લીલી પાલક, નારંગી ગાજર અને જાંબલી રીંગણ સાફ-સુથરા ઢગલાઓમાં રાખેલા હતા. અર્જુનની માતાએ કાળજીપૂર્વક તાજા શાકભાજી પસંદ કર્યા, દરેકને પોતાની ટોપલીમાં મૂકતા પહેલા તેની તપાસ કરી. અર્જુનને નાની થેલીઓ ઊંચકવામાં તેમની મદદ કરવાનું ખૂબ ગમતું હતું. ઘરે જવાના રસ્તે, તેઓ અર્જુનના સૌથી મનપસંદ ફળ, મીઠી અને રસદાર કેરી ખરીદવા માટે એક નાની દુકાન પર રોકાયા.''',
      questions: [
        PracticeQuestion(
          prompt: 'When did Arjun go to the market with his mother?',
          options: ['Every Sunday morning', 'Every Monday evening', 'Only during summer', 'Once a year'],
          correctIndex: 0,
          explanation: 'The passage begins with "Every Sunday morning, Arjun went to the vegetable market".',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'Which vegetable is described as purple in the passage?',
          options: ['Tomatoes', 'Spinach', 'Carrots', 'Brinjals'],
          correctIndex: 3,
          explanation: 'The passage lists "purple brinjals" among the vegetables at the market.',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'What did Arjun like to help his mother with?',
          options: [
            'Cooking dinner',
            'Carrying the smaller bags',
            'Paying the shopkeeper',
            'Choosing vegetables',
          ],
          correctIndex: 1,
          explanation: 'The passage says "Arjun loved helping her carry the smaller bags."',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'What is Arjun\'s favourite fruit?',
          options: ['Guava', 'Apple', 'Banana', 'Mango'],
          correctIndex: 3,
          explanation: 'The last sentence calls mangoes "Arjun\'s favourite fruit".',
          difficulty: Difficulty.easy,
        ),
      ],
      glosses: [
        InlineGloss(word: 'spinach', meaningHi: 'पालक', hiTransliteration: 'paalak', meaningGu: 'પાલક', guTransliteration: 'paalak'),
        InlineGloss(word: 'brinjals', meaningHi: 'बैंगन', hiTransliteration: 'baingan', meaningGu: 'રીંગણ', guTransliteration: 'ringan'),
        InlineGloss(word: 'stacked', meaningHi: 'ढेर लगाकर रखा हुआ', hiTransliteration: 'dher lagaakar rakha hua', meaningGu: 'ઢગલો કરીને મૂકેલું', guTransliteration: 'dhaglo karine mukelu'),
        InlineGloss(word: 'neat piles', meaningHi: 'करीने से लगे ढेर', hiTransliteration: 'kareene se lage dher', meaningGu: 'વ્યવસ્થિત ઢગલા', guTransliteration: 'vyavasthit dhagla'),
        InlineGloss(word: 'basket', meaningHi: 'टोकरी', hiTransliteration: 'tokri', meaningGu: 'ટોપલી', guTransliteration: 'topli'),
        InlineGloss(word: 'stall', meaningHi: 'छोटी दुकान, ठेला', hiTransliteration: 'chhoti dukaan, thela', meaningGu: 'નાની દુકાન, લારી', guTransliteration: 'nani dukan, lari'),
        InlineGloss(word: 'juicy', meaningHi: 'रसीला', hiTransliteration: 'rasila', meaningGu: 'રસદાર', guTransliteration: 'rasdaar'),
        InlineGloss(word: 'favourite', meaningHi: 'सबसे पसंदीदा', hiTransliteration: 'sabse pasandeeda', meaningGu: 'સૌથી મનપસંદ', guTransliteration: 'sauthi manpasand'),
      ],
    ),
    ReadingPassage(
      id: 'class4_reading_race',
      title: 'The School Sports Day Race',
      emoji: '🏃',
      grade: 'Class 4',
      difficulty: Difficulty.medium,
      body: 'Shine Academy held its Sports Day every winter, and Tanvi had been practising the 200-metre race '
          'for a whole month. She woke up early every day to run laps around the park before school. On the '
          'day of the race, Tanvi felt her legs shaking as she stood at the starting line beside four other '
          'runners, including her best friend Priya. When the whistle blew, Tanvi ran as fast as she could, '
          'but halfway through the race, Priya stumbled over a small stone and fell to the ground. Tanvi '
          'looked back and saw her friend struggling to get up, tears forming in her eyes. Without a second '
          'thought, Tanvi slowed down, ran back, and helped Priya to her feet. They finished the race together, '
          'crossing the line last, hand in hand. Tanvi\'s coach was surprised to see her walk away from an '
          'easy win, but the headmistress announced a special prize that day for sportsmanship, and gave it '
          'to Tanvi in front of the whole school. Tanvi learned that a true sportsperson cares for others, '
          'and that some victories matter more than a medal.',
      bodyHi: 'शाइन अकादमी हर सर्दियों में अपना खेल दिवस आयोजित करती थी, और तन्वी पूरे एक महीने से 200 मीटर दौड़ का अभ्यास कर रही थी। वह हर दिन स्कूल से पहले पार्क में दौड़ने के लिए जल्दी उठती थी। दौड़ के दिन, जब तन्वी अपनी सबसे अच्छी दोस्त प्रिया सहित चार अन्य धावकों के साथ शुरुआती पंक्ति में खड़ी थी, तो उसने महसूस किया कि उसके पैर कांप रहे हैं। जब सीटी बजी, तन्वी जितनी तेजी से भाग सकती थी, दौड़ी, लेकिन आधी दौड़ के दौरान प्रिया एक छोटे पत्थर से लड़खड़ा गई और जमीन पर गिर गई। तन्वी ने पीछे मुड़कर देखा तो उसकी सहेली उठने के लिए संघर्ष कर रही थी, उसकी आँखों में आँसू आ रहे थे। बिना कुछ सोचे, तन्वी धीमी हो गई, पीछे भागी और प्रिया को उसके पैरों पर खड़ा होने में मदद की। उन्होंने हाथ में हाथ डाले सबसे आखिर में लाइन पार करते हुए एक साथ दौड़ पूरी की। तन्वी के कोच उसे आसान जीत से दूर जाते देख आश्चर्यचकित थे, लेकिन प्रधानाध्यापिका ने उस दिन खेल भावना के लिए एक विशेष पुरस्कार की घोषणा की और पूरे स्कूल के सामने तन्वी को दिया। तन्वी ने सीखा कि एक सच्चा खिलाड़ी दूसरों की परवाह करता है और कुछ जीतें पदक से ज्यादा मायने रखती हैं।',
      bodyGu: '''શાઇન એકેડેમી દર શિયાળામાં પોતાનો રમતગમત દિવસ યોજતી હતી, અને તન્વી પૂરા એક મહિનાથી 200 મીટર દોડનો અભ્યાસ કરી રહી હતી. તે દરરોજ શાળાએ જતા પહેલા બગીચામાં દોડવા માટે વહેલી ઊઠતી હતી. દોડના દિવસે, જ્યારે તન્વી તેની સૌથી સારી મિત્ર પ્રિયા સહિત અન્ય ચાર દોડવીરો સાથે શરૂઆતની લાઇન પર ઊભી હતી, ત્યારે તેને લાગ્યું કે તેના પગ ધ્રૂજી રહ્યા છે. જ્યારે સિસોટી વાગી, ત્યારે તન્વી જેટલી ઝડપથી દોડી શકતી હતી તેટલી ઝડપથી દોડી, પરંતુ અડધી દોડ દરમિયાન પ્રિયા એક નાના પથ્થરથી ઠોકર ખાઈને જમીન પર પડી ગઈ. તન્વીએ પાછળ વળીને જોયું તો તેની મિત્ર ઊભા થવા માટે સંઘર્ષ કરી રહી હતી, તેની આંખોમાં આંસુ આવી રહ્યા હતા. કંઈપણ વિચાર્યા વિના, તન્વી ધીમી પડી ગઈ, પાછળ દોડી અને પ્રિયાને પગ પર ઊભા થવામાં મદદ કરી. તેઓએ હાથમાં હાથ પરોવી સૌથી છેલ્લે લાઇન પાર કરતા એકસાથે દોડ પૂરી કરી. તન્વીના કોચ તેને આસાન જીતથી દૂર જતી જોઈને આશ્ચર્યચકિત હતા, પરંતુ આચાર્યાએ તે દિવસે ખેલદિલી માટે એક વિશેષ પુરસ્કારની જાહેરાત કરી અને આખી શાળાની સામે તન્વીને આપ્યો. તન્વીએ શીખ્યું કે એક સાચો ખેલાડી બીજાની પરવા કરે છે અને કેટલીક જીત ચંદ્રક કરતાં વધુ મહત્વની હોય છે.''',
      questions: [
        PracticeQuestion(
          prompt: 'How long had Tanvi been practising for the race?',
          options: ['Two days', 'One year', 'One month', 'One week'],
          correctIndex: 2,
          explanation: 'The passage says Tanvi "had been practising the 200-metre race for a whole month".',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'What happened to Priya during the race?',
          options: [
            'She stumbled over a stone and fell.',
            'She left the race before it started.',
            'She stopped running on purpose.',
            'She won the race easily.',
          ],
          correctIndex: 0,
          explanation: 'The passage says "Priya stumbled over a small stone and fell to the ground."',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'Why did Tanvi slow down during the race?',
          options: [
            'She was too tired to continue.',
            'She twisted her ankle.',
            'The coach told her to stop.',
            'She wanted to help her fallen friend.',
          ],
          correctIndex: 3,
          explanation: 'The passage says Tanvi "slowed down, ran back, and helped Priya to her feet" instead of finishing first.',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'What is the main lesson of this story?',
          options: [
            'Sports Day is not important for students.',
            'Winning is the only thing that matters in a race.',
            'A true sportsperson cares for others, not just winning.',
            'Runners should never help each other.',
          ],
          correctIndex: 2,
          explanation: 'The last line states Tanvi learned "a true sportsperson cares for others, and that some victories matter more than a medal."',
          difficulty: Difficulty.medium,
        ),
      ],
      glosses: [
        InlineGloss(word: 'stumbled', meaningHi: 'ठोकर खाकर गिरना', hiTransliteration: 'thokar khaakar girna', meaningGu: 'ઠોકર ખાઈને પડવું', guTransliteration: 'thokar khaaine padvu'),
        InlineGloss(word: 'whistle', meaningHi: 'सीटी', hiTransliteration: 'seeti', meaningGu: 'સિસોટી', guTransliteration: 'sisoti'),
        InlineGloss(word: 'struggling', meaningHi: 'जूझना, मुश्किल से कोशिश करना', hiTransliteration: 'joojhna, mushkil se koshish karna', meaningGu: 'સંઘર્ષ કરવો, મુશ્કેલીથી પ્રયાસ કરવો', guTransliteration: 'sangharsh karvo, mushkelithi prayas karvo'),
        InlineGloss(word: 'headmistress', meaningHi: 'स्कूल की प्रधानाचार्या', hiTransliteration: 'school ki pradhaanaacharya', meaningGu: 'શાળાનાં આચાર્યા', guTransliteration: 'shaalana aacharya'),
        InlineGloss(word: 'sportsmanship', meaningHi: 'खेल भावना, अच्छा खिलाड़ी होने का गुण', hiTransliteration: 'khel bhaavna, achha khiladi hone ka gun', meaningGu: 'ખેલદિલી, સારા ખેલાડી હોવાનો ગુણ', guTransliteration: 'kheldili, saara kheladi hovano gun'),
        InlineGloss(word: 'victories', meaningHi: 'जीत', hiTransliteration: 'jeet', meaningGu: 'જીત, વિજય', guTransliteration: 'jeet, vijay'),
        InlineGloss(word: 'medal', meaningHi: 'पदक', hiTransliteration: 'padak', meaningGu: 'ચંદ્રક, મેડલ', guTransliteration: 'chandrak, medal'),
      ],
    ),
    ReadingPassage(
      id: 'class4_reading_invention',
      title: 'Dev\'s Homemade Fan',
      emoji: '💡',
      grade: 'Class 4',
      difficulty: Difficulty.medium,
      body: 'Dev was always curious about how machines worked. Whenever an appliance broke down at home, he '
          'would ask his father if he could look inside it before it was thrown away. One hot summer afternoon, '
          'the electricity in his house in Naroda went out, and Dev sat sweating on the floor with no fan to '
          'cool him. Instead of complaining, he began wondering how he could make his own fan using things '
          'lying around the house. He found an old toy motor, a few plastic spoons, and a small battery in his '
          'toolbox. Carefully, Dev cut the spoons into blade shapes and glued them around the motor\'s spindle, '
          'then connected the wires to the battery. At first, nothing happened, and Dev checked every '
          'connection twice, feeling frustrated. Finally, he noticed one wire was loose, and after fixing it, '
          'the little blades began to spin, sending a soft breeze across his face. His mother laughed with '
          'delight and called the whole family to see his invention. Dev\'s teacher was so impressed when he '
          'brought it to school that she asked him to explain how it worked to the entire class. Dev realised '
          'that patience and curiosity could turn even a power cut into an exciting discovery.',
      bodyHi: 'देव हमेशा इस बात को लेकर उत्सुक रहते थे कि मशीनें कैसे काम करती हैं। जब भी घर में कोई उपकरण खराब हो जाता था, तो वह अपने पिता से पूछता था कि क्या वह इसे फेंकने से पहले इसके अंदर देख सकता है। एक गर्म गर्मी की दोपहर में, नरोदा में उनके घर की बिजली चली गई, और देव बिना पंखे के फर्श पर पसीना बहाते हुए बैठ गए, जिससे उन्हें ठंडक मिल सके। शिकायत करने के बजाय, वह सोचने लगा कि वह घर में पड़ी चीज़ों का उपयोग करके अपना पंखा कैसे बना सकता है। उसे अपने टूलबॉक्स में एक पुरानी खिलौना मोटर, कुछ प्लास्टिक के चम्मच और एक छोटी बैटरी मिली। सावधानी से, देव ने चम्मचों को ब्लेड के आकार में काटा और उन्हें मोटर की धुरी के चारों ओर चिपका दिया, फिर तारों को बैटरी से जोड़ दिया। पहले तो, कुछ नहीं हुआ, और देव ने निराश होकर प्रत्येक कनेक्शन की दो बार जाँच की। आख़िरकार, उसने देखा कि एक तार ढीला था, और उसे ठीक करने के बाद, छोटे ब्लेड घूमने लगे, जिससे उसके चेहरे पर हल्की हवा आ रही थी। उनकी माँ ख़ुशी से हँसी और पूरे परिवार को उनके आविष्कार को देखने के लिए बुलाया। जब देव इसे स्कूल लेकर आए तो उनकी शिक्षिका इतनी प्रभावित हुईं कि उन्होंने उनसे यह समझाने के लिए कहा कि यह पूरी कक्षा में कैसे काम करता है। देव को एहसास हुआ कि धैर्य और जिज्ञासा बिजली कटौती को भी एक रोमांचक खोज में बदल सकती है।',
      bodyGu: '''દેવ હંમેશા એ જાણવા માટે ઉત્સુક રહેતો હતો કે મશીનો કેવી રીતે કામ કરે છે. જ્યારે પણ ઘરમાં કોઈ ઉપકરણ ખરાબ થઈ જતું, તો તે પોતાના પિતાને પૂછતો કે શું તે તેને ફેંકતા પહેલા તેની અંદર જોઈ શકે છે. ઉનાળાની એક ગરમ બપોરે, નરોડામાં તેમના ઘરની વીજળી જતી રહી, અને દેવ પંખા વગર પરસેવે રેબઝેબ થઈને ભોંયતળિયે બેસી રહ્યો, જેથી તેને ઠંડક મળી શકે. ફરિયાદ કરવાને બદલે, તે વિચારવા લાગ્યો કે ઘરમાં પડેલી વસ્તુઓનો ઉપયોગ કરીને તે પોતાનો પંખો કેવી રીતે બનાવી શકે છે. તેને તેના ટૂલબોક્સમાં એક જૂની રમકડાની મોટર, કેટલીક પ્લાસ્ટિકની ચમચીઓ અને એક નાની બેટરી મળી. સાવધાનીથી, દેવે ચમચીઓને બ્લેડના આકારમાં કાપી અને તેમને મોટરની ધરીની આસપાસ ચોંટાડી દીધી, પછી વાયરોને બેટરી સાથે જોડી દીધા. પહેલા તો, કંઈ ન થયું, અને દેવે નિરાશ થઈને દરેક કનેક્શનની બે વાર તપાસ કરી. છેવટે, તેણે જોયું કે એક વાયર ઢીલો હતો, અને તેને ઠીક કર્યા પછી, નાના બ્લેડ ફરવા લાગ્યા, જેનાથી તેના ચહેરા પર હળવી હવા આવવા લાગી. તેની માતા ખુશીથી હસી અને આખા પરિવારને તેની શોધ જોવા માટે બોલાવ્યા. જ્યારે દેવ તેને શાળાએ લઈને આવ્યો ત્યારે તેના શિક્ષિકા એટલા પ્રભાવિત થયા કે તેમણે તેને આખા વર્ગને તે કેવી રીતે કામ કરે છે તે સમજાવવા કહ્યું. દેવને અહેસાસ થયો કે ધીરજ અને જિજ્ઞાસા વીજળીના કાપને પણ એક રોમાંચક શોધમાં બદલી શકે છે.''',
      questions: [
        PracticeQuestion(
          prompt: 'Why did Dev decide to build his own fan?',
          options: [
            'His teacher asked him to build one.',
            'The electricity went out and he had no fan to cool him.',
            'He wanted to sell fans in the market.',
            'His father ordered him to build one.',
          ],
          correctIndex: 1,
          explanation: 'The passage says the electricity went out and Dev "began wondering how he could make his own fan" because he had no way to cool down.',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'What did Dev use to make the fan blades?',
          options: ['Plastic spoons', 'Metal sheets', 'Paper', 'Cardboard'],
          correctIndex: 0,
          explanation: 'The passage says Dev "cut the spoons into blade shapes and glued them around the motor\'s spindle".',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'Why did the fan not work at first?',
          options: [
            'One wire was loose.',
            'The motor was broken.',
            'The battery had no charge.',
            'The blades were too heavy.',
          ],
          correctIndex: 0,
          explanation: 'The passage says Dev "noticed one wire was loose, and after fixing it, the little blades began to spin".',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'What did Dev learn from this experience?',
          options: [
            'Patience and curiosity can turn a problem into an exciting discovery.',
            'Machines are too difficult to understand.',
            'Only adults can fix broken appliances.',
            'Power cuts are always bad.',
          ],
          correctIndex: 0,
          explanation: 'The last sentence says Dev realised "patience and curiosity could turn even a power cut into an exciting discovery."',
          difficulty: Difficulty.medium,
        ),
      ],
      glosses: [
        InlineGloss(word: 'appliance', meaningHi: 'बिजली से चलने वाला उपकरण', hiTransliteration: 'bijli se chalne wala upkaran', meaningGu: 'વીજળીથી ચાલતું ઉપકરણ', guTransliteration: 'vijalithi chalatu upakaran'),
        InlineGloss(word: 'toolbox', meaningHi: 'औज़ारों का डिब्बा', hiTransliteration: 'auzaaron ka dibba', meaningGu: 'ઓજારોની પેટી', guTransliteration: 'ojaroni peti'),
        InlineGloss(word: 'spindle', meaningHi: 'धुरी', hiTransliteration: 'dhuri', meaningGu: 'ધરી', guTransliteration: 'dhari'),
        InlineGloss(word: 'frustrated', meaningHi: 'निराश, चिड़चिड़ा', hiTransliteration: 'niraash, chidchida', meaningGu: 'નિરાશ, ચિડાયેલું', guTransliteration: 'nirash, chidayelu'),
        InlineGloss(word: 'breeze', meaningHi: 'हल्की हवा', hiTransliteration: 'halki hawa', meaningGu: 'હળવી હવા', guTransliteration: 'halavi hava'),
        InlineGloss(word: 'delight', meaningHi: 'बहुत खुशी', hiTransliteration: 'bahut khushi', meaningGu: 'ખૂબ ખુશી', guTransliteration: 'khoob khushi'),
        InlineGloss(word: 'invention', meaningHi: 'आविष्कार, नई खोज', hiTransliteration: 'aavishkaar, nayi khoj', meaningGu: 'શોધ, આવિષ્કાર', guTransliteration: 'shodh, aavishkar'),
        InlineGloss(word: 'curiosity', meaningHi: 'जानने की इच्छा', hiTransliteration: 'jaanne ki ichha', meaningGu: 'જાણવાની ઈચ્છા', guTransliteration: 'janavani ichchha'),
      ],
    ),
    ReadingPassage(
      id: 'class4_reading_neighbor',
      title: 'Helping Old Mr. Solanki',
      emoji: '🤝',
      grade: 'Class 4',
      difficulty: Difficulty.easy,
      body: 'Mr. Solanki was an elderly man who lived alone in the house next to Aditi\'s in Naroda. His '
          'children lived in another city, and he often struggled to carry heavy grocery bags or reach the '
          'top shelf of his kitchen cupboard. Aditi noticed him limping back from the market one afternoon, '
          'his walking stick in one hand and two heavy bags in the other. She ran over immediately and offered '
          'to carry his bags home. From that day, Aditi began visiting Mr. Solanki every afternoon after '
          'school, helping him water his small garden of marigolds and reading the newspaper aloud to him '
          'since his eyes had grown weak. In return, Mr. Solanki told her wonderful stories about his childhood '
          'village and taught her how to play chess. Aditi\'s parents were proud of her kindness and often '
          'joined her on weekends to help Mr. Solanki with bigger chores like cleaning the terrace. Slowly, '
          'other neighbours also began stopping by to check on him, and Mr. Solanki\'s house, once quiet and '
          'lonely, became a cheerful place full of visitors. Aditi understood that even small acts of '
          'kindness could make someone\'s life much happier.',
      bodyHi: 'श्री सोलंकी एक बुजुर्ग व्यक्ति थे जो नरोदा में अदिति के बगल वाले घर में अकेले रहते थे। उनके बच्चे दूसरे शहर में रहते थे, और उन्हें अक्सर किराने के भारी बैग ले जाने या अपनी रसोई की अलमारी के शीर्ष शेल्फ तक पहुंचने के लिए संघर्ष करना पड़ता था। एक दोपहर अदिति ने उसे लंगड़ाते हुए बाजार से लौटते हुए देखा, उसके एक हाथ में उसकी छड़ी और दूसरे हाथ में दो भारी बैग थे। वह तुरंत भागी और उसका बैग घर ले जाने की पेशकश की। उस दिन से, अदिति स्कूल के बाद हर दोपहर श्री सोलंकी के पास जाने लगी, गेंदे के फूलों के उनके छोटे से बगीचे में पानी देने में उनकी मदद करने लगी और उन्हें अखबार पढ़कर सुनाने लगी क्योंकि उनकी आंखें कमजोर हो गई थीं। बदले में, श्री सोलंकी ने उसे अपने बचपन के गाँव के बारे में अद्भुत कहानियाँ सुनाईं और शतरंज खेलना सिखाया। अदिति के माता-पिता को उसकी दयालुता पर गर्व था और अक्सर सप्ताहांत में छत की सफाई जैसे बड़े कामों में श्री सोलंकी की मदद करने के लिए उसके साथ शामिल होते थे। धीरे-धीरे, अन्य पड़ोसी भी उनका हालचाल लेने के लिए रुकने लगे और श्री सोलंकी का घर, जो कभी शांत और अकेला था, आगंतुकों से भरा एक खुशहाल स्थान बन गया। अदिति समझ गई कि दयालुता के छोटे-छोटे कार्य भी किसी के जीवन को अधिक खुशहाल बना सकते हैं।',
      bodyGu: '''શ્રી સોલંકી એક વૃદ્ધ વ્યક્તિ હતા જે નરોડામાં અદિતિના ઘરની બાજુમાં એકલા રહેતા હતા. તેમનાં બાળકો બીજા શહેરમાં રહેતા હતા, અને તેમને ઘણીવાર કરિયાણાની ભારે થેલીઓ ઊંચકવામાં અથવા તેમના રસોડાના કબાટના ઉપરના છાજલી સુધી પહોંચવામાં મુશ્કેલી પડતી હતી. એક બપોરે અદિતિએ તેમને બજારથી પાછા ફરતી વખતે લંગડાતા જોયા, તેમના એક હાથમાં લાકડી અને બીજા હાથમાં બે ભારે થેલીઓ હતી. તે તરત જ દોડી ગઈ અને તેમની થેલીઓ ઘરે લઈ જવાની ઓફર કરી. તે દિવસથી, અદિતિ શાળા પછી દરરોજ બપોરે શ્રી સોલંકીની મુલાકાત લેવા લાગી, તેમના ગલગોટાના નાના બગીચામાં પાણી પીવડાવવામાં મદદ કરવા લાગી અને તેમની આંખો નબળી પડી ગઈ હોવાથી તેમને મોટેથી અખબાર વાંચી સંભળાવવા લાગી. બદલામાં, શ્રી સોલંકીએ તેને તેમના બાળપણના ગામ વિશે અદ્ભુત વાર્તાઓ કહી અને તેને ચેસ રમતા શીખવ્યું. અદિતિના માતાપિતાને તેની દયા પર ગર્વ હતો અને ઘણીવાર સપ્તાહના અંતે શ્રી સોલંકીને અગાસી સાફ કરવા જેવા મોટા કામોમાં મદદ કરવા માટે તેની સાથે જોડાતા હતા. ધીરે ધીરે, અન્ય પડોશીઓએ પણ તેમની ખબર-અંતર પૂછવા માટે રોકાવાનું શરૂ કર્યું, અને શ્રી સોલંકીનું ઘર, જે ક્યારેક શાંત અને એકલું હતું, તે મુલાકાતીઓથી ભરેલી ખુશખુશાલ જગ્યા બની ગયું. અદિતિ સમજી ગઈ કે દયાના નાના કાર્યો પણ કોઈનું જીવન ઘણું ખુશખુશાલ બનાવી શકે છે.''',
      questions: [
        PracticeQuestion(
          prompt: 'Where did Mr. Solanki\'s children live?',
          options: ['Abroad', 'With him in Naroda', 'The passage does not say', 'In another city'],
          correctIndex: 3,
          explanation: 'The passage says "His children lived in another city."',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'What made Aditi first decide to help Mr. Solanki?',
          options: [
            'She saw him limping home with heavy bags.',
            'Her teacher gave her a school project.',
            'Mr. Solanki asked her for help directly.',
            'Her parents ordered her to.',
          ],
          correctIndex: 0,
          explanation: 'The passage says Aditi "noticed him limping back from the market...she ran over immediately and offered to carry his bags home."',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'Why did Aditi read the newspaper aloud to Mr. Solanki?',
          options: [
            'He had no newspaper of his own.',
            'He enjoyed hearing her voice.',
            'His eyes had grown weak.',
            'He could not read English.',
          ],
          correctIndex: 2,
          explanation: 'The passage says she read the newspaper aloud to him "since his eyes had grown weak."',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'What happened to Mr. Solanki\'s house over time?',
          options: [
            'It became a cheerful place full of visitors.',
            'It was sold to another family.',
            'It remained quiet and lonely.',
            'He decided to move away.',
          ],
          correctIndex: 0,
          explanation: 'The passage says his house, "once quiet and lonely, became a cheerful place full of visitors."',
          difficulty: Difficulty.medium,
        ),
      ],
      glosses: [
        InlineGloss(word: 'elderly', meaningHi: 'बुज़ुर्ग', hiTransliteration: 'buzurg', meaningGu: 'વૃદ્ધ', guTransliteration: 'vruddh'),
        InlineGloss(word: 'struggled', meaningHi: 'मुश्किल से किया, कठिनाई हुई', hiTransliteration: 'mushkil se kiya, kathinaai hui', meaningGu: 'મુશ્કેલી પડી, સંઘર્ષ કર્યો', guTransliteration: 'mushkeli padi, sangharsh karyo'),
        InlineGloss(word: 'limping', meaningHi: 'लंगड़ाकर चलना', hiTransliteration: 'langdaakar chalna', meaningGu: 'લંગડાતા ચાલવું', guTransliteration: 'langdata chalvu'),
        InlineGloss(word: 'marigolds', meaningHi: 'गेंदे के फूल', hiTransliteration: 'gainde ke phool', meaningGu: 'ગલગોટાના ફૂલ', guTransliteration: 'galgotana phool'),
        InlineGloss(word: 'chores', meaningHi: 'घर के छोटे-मोटे काम', hiTransliteration: 'ghar ke chhote-mote kaam', meaningGu: 'ઘરનાં પરચૂરણ કામ', guTransliteration: 'gharna parchuran kaam'),
        InlineGloss(word: 'neighbours', meaningHi: 'पड़ोसी', hiTransliteration: 'padosi', meaningGu: 'પડોશીઓ', guTransliteration: 'padoshio'),
        InlineGloss(word: 'cheerful', meaningHi: 'खुशहाल, ख़ुशी से भरा', hiTransliteration: 'khushhaal, khushi se bhara', meaningGu: 'ખુશખુશાલ, આનંદિત', guTransliteration: 'khushkhushal, anandit'),
        InlineGloss(word: 'kindness', meaningHi: 'दयालुता, अच्छाई', hiTransliteration: 'dayaaluta, achhaai', meaningGu: 'દયાળુતા, ભલાઈ', guTransliteration: 'dayaluta, bhalai'),
      ],
    ),
    ReadingPassage(
      id: 'class4_reading_festival',
      title: 'The First Rains of Navratri',
      emoji: '🪔',
      grade: 'Class 4',
      difficulty: Difficulty.medium,
      body: 'As autumn approached, the whole neighbourhood in Naroda began preparing for Navratri, nine nights '
          'of music, dance, and celebration. Jiya and her friends had been practising garba steps every evening '
          'in the society ground, twirling with colourful dandiya sticks to the beat of dhol drums. Jiya\'s '
          'grandmother helped her stitch a new chaniya choli decorated with tiny mirrors, and Jiya could hardly '
          'wait to wear it on the first night. On the evening of the festival, dark clouds suddenly gathered '
          'overhead, and just as the drummers began playing, rain started pouring down heavily. Everyone rushed '
          'for shelter, and Jiya feared the whole celebration was ruined. The society committee, however, did '
          'not give up. Within an hour, they set up a large tent with the help of several fathers and uncles, '
          'moving the sound system and lights underneath it. As soon as the tent was ready, people returned in '
          'their festive clothes, laughing about the rain instead of complaining. Jiya danced late into the '
          'night, her mirrored skirt sparkling under the tent lights, and she realised that the unexpected rain '
          'had actually brought the whole neighbourhood closer together.',
      bodyHi: 'जैसे-जैसे शरद ऋतु नजदीक आई, नरोदा का पूरा इलाका संगीत, नृत्य और उत्सव की नौ रातों वाली नवरात्रि की तैयारी करने लगा। जिया और उसकी सहेलियाँ हर शाम सोसायटी के मैदान में ढोल नगाड़ों की थाप पर रंगीन डांडिया स्टिक के साथ गरबा का अभ्यास करती थीं। जिया की दादी ने उसे छोटे दर्पणों से सजी एक नई चनिया चोली सिलने में मदद की, और जिया पहली रात इसे पहनने के लिए शायद ही इंतजार कर सकी। उत्सव की शाम को अचानक काले बादल छा गए और जैसे ही ढोल बजाने वालों ने बजाना शुरू किया, भारी बारिश होने लगी। हर कोई आश्रय के लिए दौड़ा, और जिया को डर था कि पूरा उत्सव बर्बाद हो जाएगा। हालाँकि, समाज समिति ने हार नहीं मानी। एक घंटे के भीतर, उन्होंने कई पिताओं और चाचाओं की मदद से एक बड़ा तम्बू स्थापित किया, उसके नीचे ध्वनि प्रणाली और रोशनी स्थापित की। जैसे ही तंबू तैयार हो गया, लोग अपने उत्सव के कपड़ों में शिकायत करने के बजाय बारिश के बारे में हँसते हुए लौट आए। जिया ने देर रात तक नृत्य किया, उसकी शीशे वाली स्कर्ट टेंट की रोशनी में चमक रही थी, और उसे एहसास हुआ कि अप्रत्याशित बारिश ने वास्तव में पूरे पड़ोस को एक साथ ला दिया है।',
      bodyGu: '''જેમ જેમ શરદ ઋતુ નજીક આવી, નરોડાનો આખો વિસ્તાર સંગીત, નૃત્ય અને ઉત્સવની નવ રાતો વાળી નવરાત્રિની તૈયારી કરવા લાગ્યો. જિયા અને તેની બહેનપણીઓ દરરોજ સાંજે સોસાયટીના મેદાનમાં ઢોલના તાલે રંગબેરંગી દાંડિયા સાથે ગરબાનો અભ્યાસ કરતી હતી. જિયાના દાદીએ તેને નાના અરીસાઓથી શણગારેલી નવી ચણિયાચોળી સીવવામાં મદદ કરી, અને જિયા પહેલી રાત્રે તેને પહેરવા માટે ભાગ્યે જ રાહ જોઈ શકી. ઉત્સવની સાંજે અચાનક કાળા વાદળો છવાઈ ગયા અને ડ્રમ વગાડનારાઓએ વગાડવાનું શરૂ કરતા જ ભારે વરસાદ પડવા લાગ્યો. દરેક જણ આશ્રય માટે દોડ્યા, અને જિયાને ડર હતો કે આખો ઉત્સવ બરબાદ થઈ જશે. જોકે, સોસાયટી કમિટીએ હાર માની નહીં. એક કલાકની અંદર, તેઓએ ઘણા પિતાઓ અને કાકાઓની મદદથી એક મોટો તંબુ ઊભો કર્યો, તેની નીચે સાઉન્ડ સિસ્ટમ અને લાઈટો લગાવી. તંબુ તૈયાર થતાં જ, લોકો વરસાદ વિશે ફરિયાદ કરવાને બદલે હસતાં હસતાં તેમના ઉત્સવના કપડાંમાં પાછા ફર્યા. જિયા મોડી રાત સુધી નાચી, તેનો અરીસાવાળો સ્કર્ટ ટેન્ટની લાઇટમાં ચમકી રહ્યો હતો, અને તેને સમજાયું કે અણધાર્યા વરસાદે ખરેખર આખા પડોશને એકસાથે લાવી દીધો છે.''',
      questions: [
        PracticeQuestion(
          prompt: 'What had Jiya and her friends been practising every evening?',
          options: ['Cricket', 'Garba steps', 'Painting', 'Singing'],
          correctIndex: 1,
          explanation: 'The passage says they "had been practising garba steps every evening in the society ground".',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'Who helped Jiya prepare her new outfit?',
          options: ['Her friend Priya', 'A shopkeeper', 'Her grandmother', 'Her teacher'],
          correctIndex: 2,
          explanation: 'The passage says "Jiya\'s grandmother helped her stitch a new chaniya choli."',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'What problem occurred on the evening of the festival?',
          options: [
            'Jiya lost her dandiya sticks.',
            'The drummers did not arrive.',
            'The lights stopped working.',
            'Heavy rain suddenly started pouring.',
          ],
          correctIndex: 3,
          explanation: 'The passage says "rain started pouring down heavily" just as the drummers began playing.',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'How did the society committee solve the problem?',
          options: [
            'They moved the festival to another day.',
            'They cancelled the festival completely.',
            'They asked everyone to go home.',
            'They set up a large tent so the celebration could continue.',
          ],
          correctIndex: 3,
          explanation: 'The passage says "they set up a large tent...moving the sound system and lights underneath it", so the celebration continued.',
          difficulty: Difficulty.medium,
        ),
      ],
      glosses: [
        InlineGloss(word: 'neighbourhood', meaningHi: 'आस-पड़ोस, मोहल्ला', hiTransliteration: 'aas-pados, mohalla', meaningGu: 'આસપાસનો વિસ્તાર, મહોલ્લો', guTransliteration: 'aaspasno vistaar, mahollo'),
        InlineGloss(word: 'twirling', meaningHi: 'घूमना, चक्कर लगाना', hiTransliteration: 'ghoomna, chakkar lagaana', meaningGu: 'ગોળ ગોળ ફરવું, ચક્કર લગાવવું', guTransliteration: 'gol gol farvu, chakkar lagavvu'),
        InlineGloss(word: 'chaniya choli', meaningHi: 'गरबा में पहना जाने वाला पारंपरिक घाघरा-चोली', hiTransliteration: 'garba mein pehna jaane wala paramparik ghaaghra-choli', meaningGu: 'ગરબામાં પહેરવામાં આવતો પારંપરિક ચણિયાચોળી', guTransliteration: 'garbaman paheravaman aavto paramparik chaniyacholi'),
        InlineGloss(word: 'gathered', meaningHi: 'इकट्ठा होना', hiTransliteration: 'ikattha hona', meaningGu: 'ભેગા થવું, એકત્ર થવું', guTransliteration: 'bhega thavu, ekatra thavu'),
        InlineGloss(word: 'shelter', meaningHi: 'आश्रय, छत के नीचे बचाव', hiTransliteration: 'aashray, chhat ke neeche bachaav', meaningGu: 'આશ્રય, છત નીચે બચાવ', guTransliteration: 'aashray, chhat niche bachaav'),
        InlineGloss(word: 'ruined', meaningHi: 'बर्बाद हो जाना', hiTransliteration: 'barbaad ho jaana', meaningGu: 'બરબાદ થઈ જવું', guTransliteration: 'barbaad thai javu'),
        InlineGloss(word: 'committee', meaningHi: 'समिति, प्रबंधन करने वाला समूह', hiTransliteration: 'samiti, prabandhan karne wala samooh', meaningGu: 'સમિતિ, સંચાલન કરતું જૂથ', guTransliteration: 'samiti, sanchalan kartu jutha'),
        InlineGloss(word: 'sparkling', meaningHi: 'चमकना', hiTransliteration: 'chamakna', meaningGu: 'ચમકવું, ઝળહળવું', guTransliteration: 'chamakvu, jhalhalvu'),
      ],
    ),
  ],
);
