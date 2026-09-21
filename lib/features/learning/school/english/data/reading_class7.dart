import '../models/chapter.dart' show InlineGloss;
import '../models/practice_question.dart';
import '../models/reading_passage.dart';

const class7Reading = ReadingLibrary(
  id: 'class7_reading',
  title: 'Reading Passages',
  grade: 'Class 7',
  passages: [
    ReadingPassage(
      id: 'class7_reading_kiteseller',
      title: 'The Kite Seller\'s Apprentice',
      emoji: '🪁',
      grade: 'Class 7',
      difficulty: Difficulty.medium,
      body: 'Old Nazir had been making kites in his tiny shop for nearly forty years, and his skill was famous '
          'throughout the old quarter of the city, especially in the weeks before the annual kite festival. '
          'His hands, though wrinkled and slightly unsteady, could still cut bamboo into perfectly balanced '
          'spines and stretch tissue paper so tight that not a single wrinkle remained. Twelve-year-old Salma, '
          'his neighbour\'s daughter, had been begging him for an entire summer to teach her the craft, though '
          'Nazir had always insisted that kite-making required patience no child possessed.\n\n'
          'Reluctantly, Nazir finally agreed to let Salma watch him work one afternoon, warning her sternly not '
          'to touch anything without permission. She observed silently for hours, noticing details she had '
          'never considered before: how he tested the bamboo\'s flexibility by bending it gently near his ear, '
          'listening for a particular creak that apparently signalled good quality, or how he always cut the '
          'tail slightly longer than seemed necessary to keep the kite stable in strong winds.\n\n'
          'When Nazir finally allowed her to attempt gluing a simple frame together, her first three attempts '
          'collapsed embarrassingly, the paper tearing or the spine snapping under uneven pressure. Rather than '
          'mocking her, Nazir simply handed her more paper and bamboo without a word, letting her discover for '
          'herself exactly where her technique had gone wrong. By her fifth attempt, she produced a small, '
          'slightly lopsided kite that nonetheless caught the wind and rose steadily above the rooftops.\n\n'
          'On the morning of the festival, Salma proudly flew her own kite alongside Nazir\'s magnificent '
          'creations, and several children asked eagerly whether she might teach them too. Nazir, watching from '
          'his shop doorway, allowed himself a rare smile, remarking that perhaps patience was not something a '
          'child lacked entirely, but something the craft itself could teach, one torn paper at a time.',
      bodyHi: 'बूढ़ा नज़ीर लगभग चालीस वर्षों से अपनी छोटी सी दुकान में पतंगें बना रहा था, और उसका कौशल शहर के पुराने हिस्से में प्रसिद्ध था, खासकर वार्षिक पतंग उत्सव से पहले के हफ्तों में। उसके हाथ, हालांकि झुर्रीदार और थोड़े अस्थिर थे, फिर भी बांस को पूरी तरह से संतुलित कांटों में काट सकते थे और टिशू पेपर को इतना कसकर खींच सकते थे कि एक भी शिकन न रहे। उसके पड़ोसी की बारह वर्षीय बेटी सलमा पूरी गर्मी से उसे यह कला सिखाने के लिए विनती कर रही थी, हालाँकि नज़ीर ने हमेशा इस बात पर जोर दिया था कि पतंग बनाने के लिए किसी बच्चे के पास धैर्य की आवश्यकता नहीं होती है।\n\nअनिच्छा से, नज़ीर अंततः सलमा को एक दोपहर उसे काम करते हुए देखने देने के लिए सहमत हो गया, और उसे सख्त चेतावनी दी कि वह बिना अनुमति के किसी भी चीज़ को न छुए। वह घंटों तक चुपचाप देखती रही, उन विवरणों पर गौर करते हुए जिन पर उसने पहले कभी विचार नहीं किया था: कैसे उसने बांस को अपने कान के पास धीरे से झुकाकर उसके लचीलेपन का परीक्षण किया, एक विशेष चरमराहट को सुना जो स्पष्ट रूप से अच्छी गुणवत्ता का संकेत देती थी, या कैसे वह हमेशा तेज हवाओं में पतंग को स्थिर रखने के लिए पूंछ को आवश्यक से थोड़ा अधिक लंबा काटता था।\n\nजब नजीर ने अंततः उसे एक साधारण फ्रेम को एक साथ चिपकाने का प्रयास करने की अनुमति दी, तो उसके पहले तीन प्रयास शर्मनाक तरीके से विफल हो गए, कागज फट गया या रीढ़ की हड्डी असमान दबाव में टूट गई। उसका मज़ाक उड़ाने के बजाय, नज़ीर ने बिना कुछ कहे उसे और अधिक कागज़ और बाँस थमा दिए, जिससे उसे खुद पता चल गया कि उसकी तकनीक कहाँ गलत हो गई थी। अपने पांचवें प्रयास में, उसने एक छोटी, थोड़ी टेढ़ी-मेढ़ी पतंग बनाई, जो फिर भी हवा को पकड़ लेती थी और छतों से तेजी से ऊपर उठती थी।\n\nत्यौहार की सुबह, सलमा ने गर्व से नज़ीर की शानदार रचनाओं के साथ अपनी पतंग उड़ाई, और कई बच्चों ने उत्सुकता से पूछा कि क्या वह उन्हें भी सिखा सकती है। नज़ीर ने, अपनी दुकान के दरवाज़े से देखते हुए, एक दुर्लभ मुस्कान दी, और टिप्पणी की कि शायद धैर्य कोई ऐसी चीज़ नहीं है जिसका एक बच्चे में पूरी तरह से अभाव है, बल्कि कुछ ऐसा है जो शिल्प खुद सिखा सकता है, एक समय में एक फटा हुआ कागज।',
      bodyGu: '''વૃદ્ધ નઝીર લગભગ ચાલીસ વર્ષથી તેની નાની દુકાનમાં પતંગો બનાવતો હતો, અને તેનું કૌશલ્ય શહેરના જૂના ભાગમાં પ્રખ્યાત હતું, ખાસ કરીને વાર્ષિક પતંગ મહોત્સવ પહેલાના અઠવાડિયામાં. તેના હાથ, જોકે કરચલીવાળા અને થોડા અસ્થિર હતા, છતાં વાંસને સંપૂર્ણ સંતુલિત સળીઓમાં કાપી શકતા હતા અને ટિશ્યુ પેપરને એટલું કડક ખેંચી શકતા હતા કે એક પણ કરચલી ન રહે. તેના પડોશીની બાર વર્ષની પુત્રી સલમા આખી ગરમીની ઋતુથી તેને આ કળા શીખવવા માટે વિનંતી કરી રહી હતી, જોકે નઝીરે હંમેશા એ વાત પર ભાર મૂક્યો હતો કે પતંગ બનાવવા માટે જરૂરી ધીરજ કોઈ બાળકમાં હોતી નથી.

અનિચ્છાએ, નઝીર આખરે સલમાને એક બપોરે તેને કામ કરતા જોવા દેવા માટે સંમત થયો, અને તેને સખત ચેતવણી આપી કે તે પરવાનગી વિના કોઈપણ વસ્તુને અડકે નહીં. તે કલાકો સુધી શાંતિથી જોતી રહી, એવા કસબ પર ધ્યાન આપતી જેનો તેણે પહેલાં ક્યારેય વિચાર નહોતો કર્યો: કેવી રીતે તેણે વાંસને પોતાના કાન પાસે ધીમેથી વાળીને તેની લવચીકતાનું પરીક્ષણ કર્યું, એક ખાસ અવાજ સાંભળ્યો જે સ્પષ્ટપણે સારી ગુણવત્તાનો સંકેત આપતો હતો, અથવા કેવી રીતે તે હંમેશા તેજ પવનમાં પતંગને સ્થિર રાખવા માટે પૂંછડીને જરૂરિયાત કરતાં થોડી લાંબી કાપતો હતો.

જ્યારે નઝીરે આખરે તેને એક સાધારણ ફ્રેમને એકસાથે ચોંટાડવાનો પ્રયાસ કરવાની મંજૂરી આપી, ત્યારે તેના પહેલા ત્રણ પ્રયાસો શરમજનક રીતે નિષ્ફળ ગયા, કાગળ ફાટી ગયો અથવા અસમાન દબાણ હેઠળ સળી તૂટી ગઈ. તેની મજાક ઉડાવવાને બદલે, નઝીરે કંઈ બોલ્યા વિના તેને વધુ કાગળ અને વાંસ આપી દીધા, જેથી તેને જાતે જ ખબર પડે કે તેની તકનીક ક્યાં ખોટી પડી છે. તેના પાંચમા પ્રયાસમાં, તેણે એક નાની, થોડી વાંકી પતંગ બનાવી, જે તેમ છતાં પવન પકડી લેતી હતી અને છતોથી ઝડપથી ઉપર જતી હતી.

તહેવારની સવારે, સલમાએ ગર્વથી નઝીરની શાનદાર રચનાઓ સાથે પોતાની પતંગ ઉડાડી, અને ઘણા બાળકોએ ઉત્સુકતાપૂર્વક પૂછ્યું કે શું તે તેમને પણ શીખવી શકે છે. નઝીરે, પોતાની દુકાનના દરવાજેથી જોતા, એક દુર્લભ સ્મિત આપ્યું, અને ટિપ્પણી કરી કે કદાચ ધીરજ એવી વસ્તુ નથી જેનો બાળકમાં સંપૂર્ણપણે અભાવ હોય, પરંતુ કંઈક એવું છે જે કલા પોતે શીખવી શકે છે, એક સમયે એક ફાટેલો કાગળ.''',
      questions: [
        PracticeQuestion(
          prompt: 'Why had Nazir been unwilling to teach Salma at first?',
          options: [
            'He did not like children visiting his shop.',
            'He believed kite-making required a patience that children did not have.',
            'He was planning to retire and close the shop.',
            'He thought Salma was interested only in flying kites, not making them.',
          ],
          correctIndex: 1,
          explanation: 'The passage states Nazir "had always insisted that kite-making required patience no child possessed."',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'What did Salma notice while watching Nazir work?',
          options: [
            'That he used only modern tools instead of bamboo.',
            'Small details like testing bamboo flexibility by ear and cutting a longer tail for stability.',
            'That he never spoke while working.',
            'That he made every kite exactly the same size.',
          ],
          correctIndex: 1,
          explanation: 'The passage describes her noticing how he tested bamboo "bending it gently near his ear" and cut "the tail slightly longer than seemed necessary".',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'How did Nazir respond when Salma\'s first attempts at making a kite failed?',
          options: [
            'He scolded her and told her to stop trying.',
            'He finished the kite for her.',
            'He silently gave her more materials, letting her learn from her own mistakes.',
            'He asked her to watch him for another full year first.',
          ],
          correctIndex: 2,
          explanation: 'The passage says Nazir "simply handed her more paper and bamboo without a word, letting her discover for herself" what had gone wrong.',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'What lesson does Nazir seem to draw from Salma\'s success at the end of the passage?',
          options: [
            'That kite-making is easier than people think.',
            'That the craft itself can teach patience, rather than patience being something a child already needs to have.',
            'That children should not be allowed in kite shops.',
            'That Salma was naturally gifted and needed no practice.',
          ],
          correctIndex: 1,
          explanation: 'Nazir remarks "that perhaps patience was not something a child lacked entirely, but something the craft itself could teach."',
          difficulty: Difficulty.hard,
        ),
      ],
      glosses: [
        InlineGloss(word: 'apprentice', meaningHi: 'शिष्य / सीखने वाला', hiTransliteration: 'shishya / seekhne wala', meaningGu: 'શિષ્ય / શીખનાર', guTransliteration: 'shishya / shikhnar'),
        InlineGloss(word: 'reluctantly', meaningHi: 'अनिच्छा से', hiTransliteration: 'anichha se', meaningGu: 'અનિચ્છાએ / કમને', guTransliteration: 'anichhae / kamane'),
        InlineGloss(word: 'flexibility', meaningHi: 'लचीलापन', hiTransliteration: 'lachilapan', meaningGu: 'લવચીકતા / સ્થિતિસ્થાપકતા', guTransliteration: 'lavchikta / sthitisthapakta'),
        InlineGloss(word: 'lopsided', meaningHi: 'टेढ़ा / असंतुलित', hiTransliteration: 'tedha / asantulit', meaningGu: 'વાંકું / અસંતુલિત', guTransliteration: 'vanku / asantulit'),
        InlineGloss(word: 'magnificent', meaningHi: 'शानदार', hiTransliteration: 'shaandaar', meaningGu: 'શાનદાર / ભવ્ય', guTransliteration: 'shandaar / bhavya'),
      ],
    ),
    ReadingPassage(
      id: 'class7_reading_powercut',
      title: 'The Night the Lights Went Out',
      emoji: '🕯️',
      grade: 'Class 7',
      difficulty: Difficulty.easy,
      body: 'When the electricity failed across our entire neighbourhood during a fierce thunderstorm, my first '
          'reaction was frustration, since I had been right in the middle of an important video call for a '
          'school project. My mother, however, seemed almost pleased by the sudden darkness, quickly locating a '
          'box of candles she kept for exactly such occasions and setting them carefully around the living room.\n\n'
          'As the flickering candlelight filled the room, my grandmother, who usually retired early to her room '
          'with a book, wandered out and settled into her favourite chair, saying that power cuts reminded her '
          'of her own childhood, when electricity had not yet reached her village at all. She began telling us '
          'stories about walking two kilometres to school every morning and studying by the light of an oil '
          'lamp after sunset, details I had somehow never asked her about before that evening.\n\n'
          'My younger brother, initially annoyed that his cartoons had been interrupted, grew increasingly '
          'fascinated by her stories, especially one about a mischievous goat that used to steal vegetables '
          'from her family\'s garden. Even I found myself setting my phone aside completely, something that '
          'rarely happened, simply to listen more closely to the way her voice changed when she described '
          'chasing that goat down a muddy lane.\n\n'
          'When the electricity finally returned nearly two hours later, nobody rushed to switch on the '
          'television or reach for their devices immediately. For a few extra minutes, we all sat together in '
          'the settling quiet, and I remember thinking that the storm had taken away our lights but had somehow '
          'given us something we rarely made time for otherwise.',
      bodyHi: 'जब भयंकर तूफान के दौरान हमारे पूरे पड़ोस में बिजली गुल हो गई, तो मेरी पहली प्रतिक्रिया निराशा थी, क्योंकि मैं एक स्कूल प्रोजेक्ट के लिए एक महत्वपूर्ण वीडियो कॉल के ठीक बीच में था। हालाँकि, मेरी माँ, अचानक हुए अँधेरे से लगभग प्रसन्न लग रही थी, उसने तुरंत मोमबत्तियों का एक डिब्बा ढूँढ़ निकाला और उन्हें लिविंग रूम के चारों ओर सावधानी से रख दिया।\n\nजैसे ही टिमटिमाती मोमबत्ती की रोशनी ने कमरे को भर दिया, मेरी दादी, जो आमतौर पर एक किताब के साथ अपने कमरे में जल्दी चली जाती थीं, बाहर निकलीं और अपनी पसंदीदा कुर्सी पर बैठ गईं, उन्होंने कहा कि बिजली कटौती ने उन्हें अपने बचपन की याद दिला दी, जब बिजली अभी तक उनके गाँव तक नहीं पहुँची थी। वह हमें हर सुबह स्कूल जाने के लिए दो किलोमीटर पैदल चलने और सूर्यास्त के बाद तेल के दीपक की रोशनी में पढ़ाई करने की कहानियाँ सुनाने लगी, जिनके बारे में मैंने उस शाम से पहले कभी नहीं पूछा था।\n\nमेरा छोटा भाई, शुरू में इस बात से नाराज़ था कि उसके कार्टूनों में रुकावट आ गई थी, लेकिन उसकी कहानियों से उसकी रुचि बढ़ती गई, विशेष रूप से एक शरारती बकरी के बारे में जो उसके परिवार के बगीचे से सब्जियाँ चुराती थी। यहां तक ​​कि मैंने खुद को अपना फोन पूरी तरह से अलग रख दिया, कुछ ऐसा जो शायद ही कभी हुआ हो, बस यह देखने के लिए कि जब वह कीचड़ भरी गली में उस बकरी का पीछा करने का वर्णन करती है तो उसकी आवाज कैसे बदल जाती है।\n\nजब बिजली आखिरकार लगभग दो घंटे बाद आई, तो कोई भी तुरंत टेलीविजन चालू करने या अपने उपकरणों तक पहुंचने के लिए नहीं दौड़ा। कुछ अतिरिक्त मिनटों के लिए, हम सभी शांति से एक साथ बैठे थे, और मुझे याद है कि तूफान ने हमारी रोशनी छीन ली थी, लेकिन किसी तरह हमें कुछ ऐसा दिया था जिसके लिए हम शायद ही कभी समय निकाल पाते थे।',
      bodyGu: '''જ્યારે ભયંકર વાવાઝોડા દરમિયાન અમારા આખા પડોશમાં વીજળી ડુલ થઈ ગઈ, ત્યારે મારી પહેલી પ્રતિક્રિયા નિરાશા હતી, કારણ કે હું શાળાના પ્રોજેક્ટ માટે એક મહત્વપૂર્ણ વિડિઓ કૉલની બરાબર વચ્ચે હતો. જોકે, મારી માતા અચાનક થયેલા અંધારાથી લગભગ ખુશ જણાતી હતી, તેણે તરત જ મીણબત્તીઓનું એક બોક્સ શોધી કાઢ્યું જે તે બરાબર આવા પ્રસંગો માટે જ રાખતી હતી અને તેમને લિવિંગ રૂમની ચારે બાજુ સાવચેતીથી મૂકી દીધી.

જેવી ટમટમતી મીણબત્તીની રોશનીથી રૂમ ભરાઈ ગયો, મારા દાદી, જેઓ સામાન્ય રીતે પુસ્તક લઈને પોતાના રૂમમાં જલ્દી જતા રહેતા હતા, બહાર આવ્યા અને તેમની મનપસંદ ખુરશી પર બેસી ગયા, અને કહ્યું કે વીજળી કાપે તેમને તેમના પોતાના બાળપણની યાદ અપાવી દીધી, જ્યારે તેમના ગામમાં હજુ સુધી વીજળી પહોંચી ન હતી. તેમણે અમને દરરોજ સવારે શાળાએ જવા માટે બે કિલોમીટર ચાલવાની અને સૂર્યાસ્ત પછી તેલના દીવાની રોશનીમાં અભ્યાસ કરવાની વાર્તાઓ કહેવાનું શરૂ કર્યું, એવી વિગતો જેના વિશે મેં તેમને તે સાંજ પહેલાં ક્યારેય પૂછ્યું ન હતું.

મારો નાનો ભાઈ, જે શરૂઆતમાં તેના કાર્ટૂનમાં વિક્ષેપ પડવાથી નારાજ હતો, તેમની વાર્તાઓથી વધુને વધુ પ્રભાવિત થતો ગયો, ખાસ કરીને એક તોફાની બકરી વિશે જે તેમના પરિવારના બગીચામાંથી શાકભાજી ચોરી લેતી હતી. મેં પણ મારો ફોન સંપૂર્ણપણે એક બાજુ મૂકી દીધો, એવું કંઈક જે ભાગ્યે જ બનતું હતું, માત્ર એ સાંભળવા માટે કે જ્યારે તે કાદવવાળી ગલીમાં તે બકરીનો પીછો કરવાનું વર્ણન કરે છે ત્યારે તેમનો અવાજ કેવી રીતે બદલાય છે.

જ્યારે લગભગ બે કલાક પછી અંતે વીજળી પાછી આવી, ત્યારે કોઈએ પણ તરત જ ટેલિવિઝન ચાલુ કરવા કે પોતાના ઉપકરણો લેવા માટે ઉતાવળ ન કરી. થોડી વધારાની મિનિટો માટે, અમે બધા શાંતિથી એકસાથે બેસી રહ્યા, અને મને યાદ છે કે વાવાઝોડાએ આપણી રોશની છીનવી લીધી હતી, પરંતુ કોઈક રીતે આપણને એવું કંઈક આપ્યું હતું જેના માટે આપણે ભાગ્યે જ સમય કાઢી શકતા હતા.''',
      questions: [
        PracticeQuestion(
          prompt: 'What was the narrator doing when the electricity failed?',
          options: [
            'Reading a book',
            'Taking part in a video call for a school project',
            'Cooking dinner',
            'Sleeping',
          ],
          correctIndex: 1,
          explanation: 'The passage states the narrator "had been right in the middle of an important video call for a school project."',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'Why did the power cut remind the grandmother of her childhood?',
          options: [
            'Because she used to enjoy thunderstorms as a child.',
            'Because electricity had not yet reached her village when she was young.',
            'Because she disliked using candles.',
            'Because her school was closed during storms.',
          ],
          correctIndex: 1,
          explanation: 'She says power cuts remind her of her childhood "when electricity had not yet reached her village at all."',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'How did the younger brother\'s attitude change during the passage?',
          options: [
            'He remained annoyed throughout the power cut.',
            'He fell asleep immediately.',
            'He went from being annoyed about his cartoons to becoming fascinated by grandmother\'s stories.',
            'He left the room to play outside.',
          ],
          correctIndex: 2,
          explanation: 'The passage describes him as "initially annoyed" but "increasingly fascinated by her stories."',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'What does the narrator suggest the family gained from the power cut?',
          options: [
            'A new appreciation for electricity.',
            'Time spent together, listening and talking, that they rarely made time for otherwise.',
            'A chance to fix broken appliances.',
            'An opportunity to sleep earlier than usual.',
          ],
          correctIndex: 1,
          explanation: 'The narrator reflects that the storm "had somehow given us something we rarely made time for otherwise" — time together listening to stories.',
          difficulty: Difficulty.hard,
        ),
      ],
      glosses: [
        InlineGloss(word: 'frustration', meaningHi: 'निराशा / खीज', hiTransliteration: 'niraasha / kheej', meaningGu: 'નિરાશા / ખીજ', guTransliteration: 'niraashaa / kheej'),
        InlineGloss(word: 'flickering', meaningHi: 'टिमटिमाना', hiTransliteration: 'timtimaana', meaningGu: 'ટમટમતું / ઝબકતું', guTransliteration: 'tamtamtu / zhabaktu'),
        InlineGloss(word: 'mischievous', meaningHi: 'शरारती', hiTransliteration: 'shararti', meaningGu: 'તોફાની / શરારતી', guTransliteration: 'tofaani / sharaarati'),
        InlineGloss(word: 'settling', meaningHi: 'शांत होता हुआ', hiTransliteration: 'shaant hota hua', meaningGu: 'શાંત થતું / સ્થિર થતું', guTransliteration: 'shaant thatu / sthir thatu'),
      ],
    ),
    ReadingPassage(
      id: 'class7_reading_beekeeper',
      title: 'The Reluctant Beekeeper',
      emoji: '🐝',
      grade: 'Class 7',
      difficulty: Difficulty.hard,
      body: 'When Grandfather Joseph fell ill and could no longer manage his small apiary at the edge of the '
          'coffee plantation, the responsibility unexpectedly fell to his sixteen-year-old grandson, Thomas, '
          'who had always been secretly terrified of bees. For years, Thomas had watched his grandfather move '
          'calmly among the wooden hives without any protective gear, seemingly immune to stings that would '
          'have sent Thomas running in the opposite direction.\n\n'
          'His grandfather, propped up in bed but still sharp-minded, patiently explained over several days '
          'that bees rarely stung without reason, and that most beekeeping accidents happened because people '
          'moved too quickly or panicked at the wrong moment, provoking a defensive response. He taught Thomas '
          'to approach the hives slowly, to breathe calmly even when a bee landed on his hand, and to use a '
          'smoker device that calmed the colony by masking the alarm signals bees release when threatened.\n\n'
          'Thomas\'s early visits to the apiary were disasters of nervous fumbling; he dropped a frame of '
          'honeycomb on his very first attempt, and the resulting commotion earned him two stings that '
          'confirmed every fear he had carried since childhood. Yet his grandfather\'s health depended on '
          'someone maintaining the hives, and the coffee plantation\'s owners had explained that the bees were '
          'essential for pollinating the coffee blossoms each season, so Thomas forced himself back day after '
          'day despite his fear.\n\n'
          'By the end of the coffee season, Thomas had not only kept the colonies alive but had discovered an '
          'unexpected fascination with their intricate social structure, the way worker bees communicated '
          'through movement, and the surprising gentleness of a colony approached correctly. When his '
          'grandfather finally recovered enough to visit the apiary again, he found Thomas confidently lifting '
          'a frame without gloves, and simply nodded, saying that fear faced patiently rarely remained fear '
          'for very long.',
      bodyHi: 'जब दादाजी जोसेफ बीमार पड़ गए और कॉफी बागान के किनारे पर अपने छोटे से मधुमक्खी पालन गृह का प्रबंधन नहीं कर सके, तो जिम्मेदारी अप्रत्याशित रूप से उनके सोलह वर्षीय पोते, थॉमस पर आ गई, जो हमेशा मधुमक्खियों से गुप्त रूप से डरता था। वर्षों तक, थॉमस ने अपने दादाजी को बिना किसी सुरक्षात्मक उपकरण के लकड़ी के छत्ते के बीच शांति से घूमते हुए देखा था, ऐसा प्रतीत होता है कि उन डंकों से प्रतिरक्षित थे जो थॉमस को विपरीत दिशा में दौड़ने के लिए प्रेरित करते थे।\n\nउनके दादाजी, बिस्तर पर लेटे हुए थे, लेकिन फिर भी तेज दिमाग वाले थे, उन्होंने कई दिनों तक धैर्यपूर्वक समझाया कि मधुमक्खियां शायद ही कभी बिना किसी कारण के डंक मारती हैं, और अधिकांश मधुमक्खी पालन दुर्घटनाएं इसलिए हुईं क्योंकि लोग बहुत तेजी से आगे बढ़े या गलत समय पर घबरा गए, जिससे रक्षात्मक प्रतिक्रिया हुई। उन्होंने थॉमस को धीरे-धीरे छत्तों के पास जाना, मधुमक्खी के हाथ पर आ जाने पर भी शांति से सांस लेना और एक धूम्रपान करने वाले उपकरण का उपयोग करना सिखाया, जो धमकी मिलने पर मधुमक्खियों द्वारा छोड़े जाने वाले अलार्म संकेतों को छिपाकर कॉलोनी को शांत कर देता था। अपने पहले ही प्रयास में उसने छत्ते का एक फ्रेम गिरा दिया, और परिणामस्वरूप हुए हंगामे के कारण उसे दो डंक लगे, जिससे उसके बचपन से चले आ रहे हर डर की पुष्टि हो गई। फिर भी उनके दादाजी का स्वास्थ्य छत्तों की देखभाल करने वाले पर निर्भर था, और कॉफी बागान के मालिकों ने समझाया था कि मधुमक्खियां हर मौसम में कॉफी के फूलों को परागित करने के लिए आवश्यक थीं, इसलिए थॉमस ने अपने डर के बावजूद दिन-ब-दिन खुद को वापस आने के लिए मजबूर किया।\n\nकॉफी सीजन के अंत तक, थॉमस ने न केवल उपनिवेशों को जीवित रखा था, बल्कि उनकी जटिल सामाजिक संरचना के साथ एक अप्रत्याशित आकर्षण की खोज की थी, जिस तरह से श्रमिक मधुमक्खियां आंदोलन के माध्यम से संचार करती थीं, और कॉलोनी की आश्चर्यजनक सौम्यता सही ढंग से सामने आती थी। जब उनके दादा अंततः फिर से मधुशाला में जाने के लिए पर्याप्त रूप से स्वस्थ हो गए, तो उन्होंने थॉमस को आत्मविश्वास से बिना दस्ताने के एक फ्रेम उठाते हुए पाया, और बस सिर हिलाते हुए कहा कि धैर्यपूर्वक सामना किया गया डर शायद ही कभी बहुत लंबे समय तक डर बना रहता है।',
      bodyGu: '''જ્યારે દાદાજી જોસેફ બીમાર પડ્યા અને કોફી બાગાનના કિનારે તેમના નાના મધમાખી પાલન કેન્દ્રનું સંચાલન કરી શક્યા નહીં, ત્યારે જવાબદારી અણધારી રીતે તેમના સોળ વર્ષના પૌત્ર, થોમસ પર આવી ગઈ, જે હંમેશાં મધમાખીઓથી ગુપ્ત રીતે ડરતો હતો. વર્ષો સુધી, થોમસે તેના દાદાજીને કોઈપણ રક્ષણાત્મક સાધનો વિના લાકડાના મધપૂડાની વચ્ચે શાંતિથી ફરતા જોયા હતા, એવું લાગતું હતું કે તેઓ તે ડંખથી સુરક્ષિત હતા જે થોમસને વિરુદ્ધ દિશામાં દોડવા માટે મજબૂર કરતા હતા.

તેના દાદાજી, જે પથારીમાં સૂતા હતા છતાં તીક્ષ્ણ મગજના હતા, તેમણે ઘણા દિવસો સુધી ધીરજપૂર્વક સમજાવ્યું કે મધમાખીઓ ભાગ્યે જ કોઈ કારણ વિના ડંખ મારે છે, અને મોટાભાગના મધમાખી પાલનના અકસ્માતો એટલા માટે થયા કારણ કે લોકો ખૂબ ઝડપથી આગળ વધ્યા અથવા ખોટા સમયે ગભરાઈ ગયા, જેનાથી રક્ષણાત્મક પ્રતિક્રિયા થઈ. તેમણે થોમસને ધીમે ધીમે મધપૂડા પાસે જતાં, હાથ પર મધમાખી આવી જાય તો પણ શાંતિથી શ્વાસ લેતાં અને ધુમાડો કરનાર સાધનનો ઉપયોગ કરતાં શીખવ્યું, જે જોખમ અનુભવાય ત્યારે મધમાખીઓ દ્વારા છોડવામાં આવતા એલાર્મ સંકેતોને છુપાવીને વસાહતને શાંત કરી દેતું હતું. તેના પ્રથમ પ્રયાસમાં જ તેણે મધપૂડાની એક ફ્રેમ પાડી દીધી, અને તેના પરિણામે થયેલા હોબાળાને કારણે તેને બે ડંખ વાગ્યા, જેણે તેના બાળપણથી ચાલ્યા આવતા દરેક ડરની પુષ્ટિ કરી. તેમ છતાં તેના દાદાજીનું સ્વાસ્થ્ય મધપૂડાની દેખરેખ રાખનાર પર નિર્ભર હતું, અને કોફી બાગાનના માલિકોએ સમજાવ્યું હતું કે મધમાખીઓ દરેક ઋતુમાં કોફીના ફૂલોના પરાગનયન માટે જરૂરી છે, તેથી થોમસે પોતાના ડર છતાં દિવસ-પ્રતિદિવસ પાછા આવવા માટે પોતાની જાતને મજબૂર કરી.

કોફી સીઝનના અંત સુધીમાં, થોમસે માત્ર વસાહતોને જીવંત રાખી ન હતી, પરંતુ તેમની જટિલ સામાજિક રચના સાથે એક અણધાર્યા આકર્ષણની શોધ કરી હતી, જે રીતે કામદાર મધમાખીઓ હલનચલન દ્વારા વાતચીત કરતી હતી, અને જ્યારે યોગ્ય રીતે સંપર્ક કરવામાં આવે ત્યારે વસાહતની આશ્ચર્યજનક સૌમ્યતા દેખાતી હતી. જ્યારે તેના દાદાજી આખરે ફરીથી મધમાખી પાલન કેન્દ્રની મુલાકાત લેવા માટે પૂરતા સ્વસ્થ થઈ ગયા, ત્યારે તેમણે થોમસને આત્મવિશ્વાસથી મોજા વિના ફ્રેમ ઉપાડતો જોયો, અને ફક્ત માથું હલાવીને કહ્યું કે ધીરજપૂર્વક સામનો કરવામાં આવેલ ડર ભાગ્યે જ લાંબા સમય સુધી ડર બની રહે છે.''',
      questions: [
        PracticeQuestion(
          prompt: 'Why did the responsibility for the apiary fall to Thomas?',
          options: [
            'He had always wanted to become a beekeeper.',
            'His grandfather fell ill and could no longer manage it.',
            'His grandfather retired and moved away.',
            'The plantation owners asked him directly.',
          ],
          correctIndex: 1,
          explanation: 'The passage states the responsibility "unexpectedly fell to his sixteen-year-old grandson" when his grandfather "fell ill and could no longer manage his small apiary."',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'According to Grandfather Joseph, why do most beekeeping accidents happen?',
          options: [
            'Because bees are naturally aggressive.',
            'Because people move too quickly or panic, provoking a defensive response.',
            'Because hives are built too close together.',
            'Because beekeepers do not use enough smoke.',
          ],
          correctIndex: 1,
          explanation: 'He explained "most beekeeping accidents happened because people moved too quickly or panicked at the wrong moment, provoking a defensive response."',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'Why did Thomas continue visiting the apiary despite his fear?',
          options: [
            'He was being paid to do so.',
            'His grandfather\'s health depended on the hives, and the bees were essential for pollinating the coffee blossoms.',
            'He wanted to prove he was braver than his friends.',
            'The plantation owners threatened to fire his family.',
          ],
          correctIndex: 1,
          explanation: 'The passage explains "his grandfather\'s health depended on someone maintaining the hives" and the bees were "essential for pollinating the coffee blossoms".',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'What does grandfather\'s final remark, "fear faced patiently rarely remained fear for very long," suggest about the passage\'s message?',
          options: [
            'That fear should always be avoided completely.',
            'That facing a fear patiently and repeatedly can eventually overcome it.',
            'That only experienced people can work with bees.',
            'That Thomas was never really afraid of bees.',
          ],
          correctIndex: 1,
          explanation: 'Thomas\'s fear gradually turned into fascination and confidence through patient, repeated practice — matching his grandfather\'s closing remark.',
          difficulty: Difficulty.hard,
        ),
      ],
      glosses: [
        InlineGloss(word: 'apiary', meaningHi: 'मधुमक्खी पालन गृह', hiTransliteration: 'madhumakkhi paalan grih', meaningGu: 'મધમાખી પાલન કેન્દ્ર', guTransliteration: 'madhamakhi paalan kendra'),
        InlineGloss(word: 'immune', meaningHi: 'प्रतिरक्षित / असर न होना', hiTransliteration: 'pratiraksit / asar na hona', meaningGu: 'સુરક્ષિત / અસર ન થવી', guTransliteration: 'surakshit / asar na thavi'),
        InlineGloss(word: 'provoking', meaningHi: 'भड़काना', hiTransliteration: 'bhadkaana', meaningGu: 'ઉશ્કેરવું', guTransliteration: 'ushkeravu'),
        InlineGloss(word: 'fumbling', meaningHi: 'अनाड़ीपन से करना', hiTransliteration: 'anaadipan se karna', meaningGu: 'અણઆવડતથી કરવું / ફાંફાં મારવા', guTransliteration: 'anaavadatathi karavu / faanfaa maarava'),
        InlineGloss(word: 'commotion', meaningHi: 'हलचल / हंगामा', hiTransliteration: 'halchal / hangama', meaningGu: 'હોબાળો / ધાંધલધમાલ', guTransliteration: 'hobaalo / dhaandhaldhamaal'),
        InlineGloss(word: 'pollinating', meaningHi: 'परागण करना', hiTransliteration: 'paraagan karna', meaningGu: 'પરાગનયન કરવું', guTransliteration: 'paraaganayan karavu'),
        InlineGloss(word: 'intricate', meaningHi: 'जटिल', hiTransliteration: 'jatil', meaningGu: 'જટિલ / ગૂંચવણભર્યું', guTransliteration: 'jatil / gunchavanbharyu'),
      ],
    ),
  ],
);
