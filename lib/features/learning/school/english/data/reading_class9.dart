import '../models/chapter.dart' show InlineGloss;
import '../models/practice_question.dart';
import '../models/reading_passage.dart';

const class9Reading = ReadingLibrary(
  id: 'class9_reading',
  title: 'Reading Passages',
  grade: 'Class 9',
  passages: [
    ReadingPassage(
      id: 'class9_reading_seedbank',
      title: 'The Vault at the Edge of the World',
      emoji: '🌱',
      grade: 'Class 9',
      difficulty: Difficulty.hard,
      body: 'Deep inside a mountain on a remote Arctic island, far from the conflicts, natural disasters, and '
          'political instability that periodically threaten agriculture in different parts of the world, lies '
          'a facility designed to outlast most of human civilisation\'s ordinary institutions: a seed vault '
          'capable of storing millions of crop seed samples at a constant sub-zero temperature, largely '
          'independent of external power failures thanks to the surrounding permafrost.\n\n'
          'The vault\'s purpose is neither romantic nor purely symbolic, though its imagery, an isolated door '
          'embedded in an icy hillside, certainly captures public imagination. Agricultural researchers deposit '
          'duplicate samples of seeds already stored in national and regional gene banks worldwide, creating a '
          'backup system against the very real possibility that a local gene bank might be damaged by war, '
          'funding cuts, natural disaster, or simple mismanagement, potentially destroying genetic diversity '
          'accumulated over centuries of careful crop breeding.\n\n'
          'This diversity matters enormously for reasons that extend well beyond nostalgia for traditional '
          'farming. As climate patterns shift unpredictably and new crop diseases emerge, breeders often need '
          'access to older, less commercially popular seed varieties that may carry genetic resistance traits '
          'modern high-yield varieties have lost through generations of selective breeding focused narrowly on '
          'productivity. A seed variety considered commercially obsolete today might contain precisely the '
          'genetic resistance needed to survive tomorrow\'s previously unknown crop disease.\n\n'
          'The vault has already proven its worth once: after a regional seed bank in a conflict-affected area '
          'was severely damaged, researchers successfully withdrew their deposited duplicate samples to rebuild '
          'their collection elsewhere. This real-world demonstration confirmed what the vault\'s designers had '
          'always argued: that preserving agricultural diversity was not an abstract, distant concern, but an '
          'immediate form of insurance against genuinely unpredictable future crises.',
      bodyHi: 'सुदूर आर्कटिक द्वीप पर एक पहाड़ के अंदर, संघर्षों, प्राकृतिक आपदाओं और राजनीतिक अस्थिरता से दूर, जो समय-समय पर दुनिया के विभिन्न हिस्सों में कृषि को खतरे में डालती है, मानव सभ्यता के अधिकांश सामान्य संस्थानों को खत्म करने के लिए डिज़ाइन की गई एक सुविधा है: एक बीज तिजोरी जो लगातार उप-शून्य तापमान पर लाखों फसल के बीज के नमूने संग्रहीत करने में सक्षम है, जो आसपास के पर्माफ्रॉस्ट के कारण बाहरी बिजली विफलताओं से काफी हद तक स्वतंत्र है।\n\nतिजोरी का उद्देश्य न तो रोमांटिक है और न ही पूरी तरह से प्रतीकात्मक है, हालांकि इसकी कल्पना, एक अलग दरवाजा है बर्फीली पहाड़ी में स्थित, निश्चित रूप से सार्वजनिक कल्पना को आकर्षित करता है। कृषि शोधकर्ता दुनिया भर के राष्ट्रीय और क्षेत्रीय जीन बैंकों में पहले से ही संग्रहीत बीजों के डुप्लिकेट नमूने जमा करते हैं, जिससे इस वास्तविक संभावना के खिलाफ एक बैकअप सिस्टम तैयार होता है कि स्थानीय जीन बैंक युद्ध, फंडिंग में कटौती, प्राकृतिक आपदा, या साधारण कुप्रबंधन से क्षतिग्रस्त हो सकता है, जो संभावित रूप से सावधानीपूर्वक फसल प्रजनन के सदियों से जमा आनुवंशिक विविधता को नष्ट कर सकता है। जैसे-जैसे जलवायु पैटर्न अप्रत्याशित रूप से बदलता है और नई फसल की बीमारियाँ उभरती हैं, प्रजनकों को अक्सर पुराने, कम व्यावसायिक रूप से लोकप्रिय बीज किस्मों तक पहुंच की आवश्यकता होती है, जिनमें आनुवंशिक प्रतिरोध लक्षण हो सकते हैं, आधुनिक उच्च उपज वाली किस्में उत्पादकता पर केंद्रित चयनात्मक प्रजनन की पीढ़ियों के माध्यम से खो गई हैं। आज व्यावसायिक रूप से अप्रचलित मानी जाने वाली बीज किस्म में कल की अज्ञात फसल बीमारी से बचने के लिए आवश्यक आनुवंशिक प्रतिरोध हो सकता है।\n\nतिजोरी ने पहले ही एक बार अपना महत्व साबित कर दिया है: संघर्ष प्रभावित क्षेत्र में एक क्षेत्रीय बीज बैंक के गंभीर रूप से क्षतिग्रस्त होने के बाद, शोधकर्ताओं ने अपने संग्रह को कहीं और फिर से बनाने के लिए अपने जमा किए गए डुप्लिकेट नमूनों को सफलतापूर्वक वापस ले लिया। वास्तविक दुनिया के इस प्रदर्शन ने उस बात की पुष्टि की जो तिजोरी के डिजाइनरों ने हमेशा तर्क दिया था: कि कृषि विविधता को संरक्षित करना एक अमूर्त, दूर की चिंता नहीं थी, बल्कि वास्तव में अप्रत्याशित भविष्य के संकटों के खिलाफ बीमा का एक तात्कालिक रूप था।',
      bodyGu: '''દૂરના આર્કટિક ટાપુ પર પર્વતની અંદર, સંઘર્ષો, કુદરતી આફતો અને રાજકીય અસ્થિરતાથી દૂર, જે સમયાંતરે વિશ્વના વિવિધ ભાગોમાં કૃષિને જોખમમાં મૂકે છે, ત્યાં માનવ સભ્યતાની મોટાભાગની સામાન્ય સંસ્થાઓથી પણ લાંબુ ટકી શકે તેવી સુવિધા આવેલી છે: એક બીજ વૉલ્ટ જે સતત શૂન્યથી નીચેના તાપમાને લાખો પાકના બીજના નમૂનાઓ સંગ્રહિત કરવામાં સક્ષમ છે, જે આસપાસના પર્માફ્રોસ્ટ (કાયમી થીજેલી જમીન) ના કારણે બાહ્ય પાવર નિષ્ફળતાથી મોટાભાગે સ્વતંત્ર છે.

આ વૉલ્ટનો હેતુ ન તો રોમેન્ટિક છે કે ન તો સંપૂર્ણ રીતે પ્રતીકાત્મક છે, જોકે તેની છબી, બર્ફીલા પહાડમાં સ્થિત એક અલગ દરવાજો, ચોક્કસપણે લોકોની કલ્પનાને આકર્ષિત કરે છે. કૃષિ સંશોધકો વિશ્વભરની રાષ્ટ્રીય અને પ્રાદેશિક જનીન બેંકોમાં પહેલેથી જ સંગ્રહિત બીજના ડુપ્લિકેટ નમૂના જમા કરે છે, જેથી એવી વાસ્તવિક સંભાવના સામે બેકઅપ સિસ્ટમ તૈયાર થાય કે સ્થાનિક જનીન બેંક યુદ્ધ, ભંડોળમાં કાપ, કુદરતી આફત અથવા સામાન્ય ગેરવહીવટથી નુકસાન પામી શકે છે, જે સંભવિતપણે સદીઓના કાળજીપૂર્વકના પાક સંવર્ધનથી જમા થયેલી આનુવંશિક વિવિધતાને નષ્ટ કરી શકે છે. જેમ જેમ આબોહવાની પેટર્ન અણધારી રીતે બદલાય છે અને પાકની નવી બીમારીઓ ઉભરી આવે છે, સંવર્ધકોને વારંવાર જૂની, ઓછી વ્યાવસાયિક રીતે લોકપ્રિય બીજની જાતોની ઍક્સેસની જરૂર પડે છે જેમાં આનુવંશિક પ્રતિકારક લક્ષણો હોઈ શકે છે જે આધુનિક ઉચ્ચ ઉપજ આપતી જાતો ઉત્પાદકતા પર ધ્યાન કેન્દ્રિત કરતી પસંદગીયુક્ત સંવર્ધનની પેઢીઓ દ્વારા ગુમાવી બેઠી છે. આજે વ્યાવસાયિક રીતે અપ્રચલિત માનવામાં આવતી બીજની જાતમાં કદાચ આવતીકાલની અજ્ઞાત પાકની બીમારીથી બચવા માટે જરૂરી આનુવંશિક પ્રતિકાર હોઈ શકે છે.

વૉલ્ટે પહેલાથી જ એકવાર પોતાનું મહત્વ સાબિત કરી દીધું છે: સંઘર્ષગ્રસ્ત વિસ્તારમાં એક પ્રાદેશિક બીજ બેંકને ભારે નુકસાન થયા પછી, સંશોધકોએ તેમના સંગ્રહને બીજે ક્યાંક ફરીથી બનાવવા માટે તેમના જમા કરેલા ડુપ્લિકેટ નમૂના સફળતાપૂર્વક પાછા ખેંચી લીધા. આ વાસ્તવિક દુનિયાના પ્રદર્શને વૉલ્ટના ડિઝાઇનરોએ હંમેશા જે દલીલ કરી હતી તેની પુષ્ટિ કરી: કે કૃષિ વિવિધતાનું સંરક્ષણ કરવું એ કોઈ અમૂર્ત, દૂરની ચિંતા નહોતી, પરંતુ ખરેખર અણધારી ભવિષ્યની કટોકટી સામે વીમાનું એક તાત્કાલિક સ્વરૂપ હતું.''',
      questions: [
        PracticeQuestion(
          prompt: 'Why was the seed vault built in such a remote Arctic location?',
          options: [
            'Because it is cheaper to build there than elsewhere.',
            'To be far from conflicts, disasters, and political instability, using natural cold and permafrost for preservation.',
            'Because no other suitable land existed.',
            'To attract tourists to the region.',
          ],
          correctIndex: 1,
          explanation: 'The passage explains it is "far from the conflicts, natural disasters, and political instability" and uses "surrounding permafrost" for natural cooling.',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'What is the vault\'s actual function, according to the passage?',
          options: [
            'It replaces all national seed banks entirely.',
            'It stores duplicate samples as a backup against damage to national and regional gene banks.',
            'It is mainly a tourist attraction with symbolic value.',
            'It only stores seeds for one specific country.',
          ],
          correctIndex: 1,
          explanation: 'The passage states researchers "deposit duplicate samples...creating a backup system" against potential damage to original gene banks.',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'Why might a "commercially obsolete" seed variety still be valuable?',
          options: [
            'It could contain genetic resistance traits that modern varieties have lost through breeding focused on productivity.',
            'It is always more profitable than modern varieties.',
            'It requires no water to grow.',
            'It is easier to transport than other seeds.',
          ],
          correctIndex: 0,
          explanation: 'The passage explains such varieties "may carry genetic resistance traits modern high-yield varieties have lost."',
          difficulty: Difficulty.hard,
        ),
        PracticeQuestion(
          prompt: 'How did the vault demonstrate its real-world value, according to the passage?',
          options: [
            'It has never actually been used for withdrawals.',
            'After a regional seed bank was damaged in a conflict-affected area, researchers successfully withdrew duplicate samples to rebuild their collection.',
            'It was used to grow crops directly inside the vault.',
            'It was sold to a private company for profit.',
          ],
          correctIndex: 1,
          explanation: 'The passage describes exactly this event as proof "that preserving agricultural diversity was not an abstract, distant concern."',
          difficulty: Difficulty.hard,
        ),
      ],
      glosses: [
        InlineGloss(word: 'permafrost', meaningHi: 'सदैव जमी हुई भूमि', hiTransliteration: 'sadaiv jami hui bhoomi', meaningGu: 'કાયમી થીજેલી જમીન', guTransliteration: 'kaayami thijeli jamin'),
        InlineGloss(word: 'genetic diversity', meaningHi: 'आनुवंशिक विविधता', hiTransliteration: 'aanuvanshik vividhta', meaningGu: 'આનુવંશિક વિવિધતા', guTransliteration: 'aanuvanshik vividhata'),
        InlineGloss(word: 'obsolete', meaningHi: 'अप्रचलित / पुराना', hiTransliteration: 'aprachalit / puraana', meaningGu: 'અપ્રચલિત / જૂનું', guTransliteration: 'aprachalit / junu'),
        InlineGloss(word: 'resistance traits', meaningHi: 'प्रतिरोधक गुण', hiTransliteration: 'pratirodhak gun', meaningGu: 'પ્રતિકારક લક્ષણો', guTransliteration: 'pratikarak lakshano'),
        InlineGloss(word: 'insurance', meaningHi: 'बीमा / सुरक्षा उपाय', hiTransliteration: 'beema / suraksha upaay', meaningGu: 'વીમો / સુરક્ષા ઉપાય', guTransliteration: 'vimo / suraksha upay'),
      ],
    ),
    ReadingPassage(
      id: 'class9_reading_translator',
      title: 'Lost and Found in Translation',
      emoji: '📚',
      grade: 'Class 9',
      difficulty: Difficulty.hard,
      body: 'When the publishing house first approached Deepti to translate a celebrated Marathi novel into '
          'English, she assumed the work would primarily involve finding accurate English equivalents for '
          'Marathi words, a task she felt reasonably confident about given her fluency in both languages since '
          'childhood. Within her first week of translating, however, she encountered a problem far more '
          'complex than simple vocabulary matching.\n\n'
          'The novel\'s opening chapter relied heavily on a specific term of address between the two central '
          'characters, an aunt and niece, that carried layers of affection, informal intimacy, and generational '
          'respect simultaneously, concepts that no single English word captured without losing some essential '
          'nuance. Translating it as simply "aunt" felt clinically distant, while attempting a literal '
          'explanation disrupted the novel\'s natural rhythm entirely, turning fluid dialogue into something '
          'resembling a textbook footnote.\n\n'
          'Deepti spent nearly three days experimenting with different approaches before settling on a solution '
          'her editor initially questioned: retaining the original Marathi term throughout the English text, '
          'trusting readers to absorb its meaning gradually through context rather than through direct '
          'translation, the same way English readers had grown comfortable with untranslated words from other '
          'languages appearing in literary fiction. This decision required a delicate balance, since too many '
          'untranslated terms could alienate readers unfamiliar with Marathi entirely.\n\n'
          'When the translated novel was eventually published, several reviewers specifically praised this '
          'choice, noting that it preserved something authentic about the original relationship that a purely '
          'English equivalent would have inevitably flattened. Deepti later reflected that translation, she had '
          'come to realise, was rarely about finding perfect equivalents at all, but about making careful, '
          'sometimes uncomfortable choices about what could be preserved and what would inevitably be lost in '
          'moving between two different ways of seeing the world.',
      bodyHi: 'जब प्रकाशन गृह ने पहली बार एक प्रसिद्ध मराठी उपन्यास का अंग्रेजी में अनुवाद करने के लिए दीप्ति से संपर्क किया, तो उन्होंने मान लिया कि काम में मुख्य रूप से मराठी शब्दों के लिए सटीक अंग्रेजी समकक्ष ढूंढना शामिल होगा, एक ऐसा कार्य जिसे लेकर वह बचपन से ही दोनों भाषाओं में उनके प्रवाह को देखते हुए काफी आश्वस्त महसूस करती थीं। हालाँकि, अनुवाद करने के पहले सप्ताह के भीतर, उसे साधारण शब्दावली मिलान की तुलना में कहीं अधिक जटिल समस्या का सामना करना पड़ा।\n\nउपन्यास का शुरुआती अध्याय दो केंद्रीय पात्रों, एक चाची और भतीजी, के बीच संबोधन के एक विशिष्ट शब्द पर बहुत अधिक निर्भर करता है, जिसमें एक साथ स्नेह, अनौपचारिक अंतरंगता और पीढ़ीगत सम्मान की परतें होती हैं, ऐसी अवधारणाएँ जिन्हें कोई भी अंग्रेजी शब्द कुछ आवश्यक बारीकियों को खोए बिना नहीं पकड़ सकता है। इसे केवल "आंटी" के रूप में अनुवाद करने से चिकित्सकीय रूप से दूर महसूस हुआ, जबकि शाब्दिक व्याख्या के प्रयास ने उपन्यास की प्राकृतिक लय को पूरी तरह से बाधित कर दिया, तरल संवाद को एक पाठ्यपुस्तक फुटनोट जैसा कुछ बना दिया।\n\nदीप्ति ने उस समाधान पर निर्णय लेने से पहले विभिन्न दृष्टिकोणों के साथ प्रयोग करने में लगभग तीन दिन बिताए, जिस पर उनके संपादक ने शुरू में सवाल उठाया था: पूरे अंग्रेजी पाठ में मूल मराठी शब्द को बनाए रखना, पाठकों पर सीधे अनुवाद के बजाय संदर्भ के माध्यम से धीरे-धीरे इसके अर्थ को अवशोषित करने का भरोसा करना, उसी तरह अंग्रेजी पाठक अन्य भाषाओं के अअनुवादित शब्दों के साथ सहज हो गए थे। साहित्यिक कथा साहित्य में. इस निर्णय के लिए एक नाजुक संतुलन की आवश्यकता थी, क्योंकि बहुत से अअनुवादित शब्द पूरी तरह से मराठी से अपरिचित पाठकों को अलग-थलग कर सकते थे।\n\nजब अनुवादित उपन्यास अंततः प्रकाशित हुआ, तो कई समीक्षकों ने विशेष रूप से इस विकल्प की प्रशंसा की, यह देखते हुए कि इसने मूल संबंध के बारे में कुछ प्रामाणिक संरक्षित किया है जो कि पूरी तरह से अंग्रेजी समकक्ष अनिवार्य रूप से सपाट हो जाएगा। दीप्ति ने बाद में उस अनुवाद पर विचार किया, उसे एहसास हुआ था कि यह शायद ही कभी बिल्कुल सही समकक्ष खोजने के बारे में था, बल्कि सावधानीपूर्वक, कभी-कभी असुविधाजनक विकल्प चुनने के बारे में था कि क्या संरक्षित किया जा सकता है और दुनिया को देखने के दो अलग-अलग तरीकों के बीच जाने पर क्या अनिवार्य रूप से खो जाएगा।',
      bodyGu: '''જ્યારે પ્રકાશન ગૃહે પહેલીવાર એક પ્રખ્યાત મરાઠી નવલકથાનો અંગ્રેજીમાં અનુવાદ કરવા માટે દીપ્તિનો સંપર્ક કર્યો, ત્યારે તેણે માની લીધું કે કામમાં મુખ્યત્વે મરાઠી શબ્દો માટે સચોટ અંગ્રેજી સમકક્ષ શોધવાનો સમાવેશ થશે, એક એવું કાર્ય જેને લઈને તે બાળપણથી જ બંને ભાષાઓમાં તેના પ્રવાહને જોતાં ખૂબ આત્મવિશ્વાસ અનુભવતી હતી. જો કે, અનુવાદ કરવાના પહેલા જ અઠવાડિયામાં, તેને સામાન્ય શબ્દભંડોળની મેળવણી કરતાં ઘણી વધુ જટિલ સમસ્યાનો સામનો કરવો પડ્યો.

નવલકથાનો શરૂઆતનો અધ્યાય બે મુખ્ય પાત્રો, એક કાકી અને ભત્રીજી, વચ્ચે સંબોધનના એક વિશિષ્ટ શબ્દ પર ખૂબ આધાર રાખે છે, જેમાં એકસાથે સ્નેહ, અનૌપચારિક આત્મીયતા અને પેઢીગત સન્માનના સ્તરો હોય છે, એવી વિભાવનાઓ કે જેને કોઈ પણ અંગ્રેજી શબ્દ કેટલીક આવશ્યક બારીકીઓ ગુમાવ્યા વિના પકડી શકતો નથી. તેનો માત્ર "આન્ટી" તરીકે અનુવાદ કરવાથી ભાવનાહીન અંતરનો અનુભવ થયો, જ્યારે શાબ્દિક સમજૂતીના પ્રયાસે નવલકથાની કુદરતી લયને સંપૂર્ણપણે ખોરવી નાખી, પ્રવાહી સંવાદને એક પાઠ્યપુસ્તકની ફૂટનોટ જેવું કંઈક બનાવી દીધું.

દીપ્તિએ એવા ઉકેલ પર નિર્ણય લેતા પહેલાં વિવિધ અભિગમો સાથે પ્રયોગ કરવામાં લગભગ ત્રણ દિવસ વિતાવ્યા, જેના પર તેના સંપાદકે શરૂઆતમાં સવાલ ઉઠાવ્યો હતો: આખા અંગ્રેજી લખાણમાં મૂળ મરાઠી શબ્દ જાળવી રાખવો, વાચકો પર સીધા અનુવાદને બદલે સંદર્ભ દ્વારા ધીમે ધીમે તેનો અર્થ ગ્રહણ કરવાનો ભરોસો કરવો, એ જ રીતે જેમ અંગ્રેજી વાચકો સાહિત્યિક કથાઓમાં અન્ય ભાષાઓના અનુવાદિત ન થયેલા શબ્દો સાથે સહજ થઈ ગયા હતા. આ નિર્ણય માટે એક નાજુક સંતુલનની જરૂર હતી, કારણ કે ઘણા બધા અનુવાદ વિનાના શબ્દો મરાઠીથી સંપૂર્ણપણે અજાણ્યા વાચકોને અલગ કરી શકતા હતા.

જ્યારે અનુવાદિત નવલકથા આખરે પ્રકાશિત થઈ, ત્યારે ઘણા સમીક્ષકોએ ખાસ કરીને આ પસંદગીની પ્રશંસા કરી, એ નોંધ્યું કે તેણે મૂળ સંબંધ વિશે કંઈક અધિકૃત સાચવી રાખ્યું છે જે સંપૂર્ણપણે અંગ્રેજી સમકક્ષ અનિવાર્યપણે સપાટ કરી દેત. દીપ્તિએ પાછળથી તે અનુવાદ પર વિચાર કર્યો, તેને અહેસાસ થયો કે આ ભાગ્યે જ બિલકુલ સચોટ સમકક્ષ શોધવા વિશે હતું, પરંતુ કાળજીપૂર્વક, ક્યારેક અસુવિધાજનક પસંદગીઓ કરવા વિશે હતું કે શું સાચવી શકાય છે અને દુનિયાને જોવાની બે અલગ અલગ રીતો વચ્ચે જતી વખતે અનિવાર્યપણે શું ગુમાવવું પડશે.''',
      questions: [
        PracticeQuestion(
          prompt: 'What problem did Deepti encounter beyond simple vocabulary matching?',
          options: [
            'She could not read Marathi fluently.',
            'A specific term of address carried layers of meaning that no single English word could capture.',
            'The publisher refused to pay her.',
            'The novel had no dialogue to translate.',
          ],
          correctIndex: 1,
          explanation: 'The passage describes a term carrying "layers of affection, informal intimacy, and generational respect simultaneously" with no direct English equivalent.',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'What solution did Deepti eventually choose for this term?',
          options: [
            'She removed the term from the text entirely.',
            'She retained the original Marathi term, trusting readers to understand it through context.',
            'She replaced it with a long English explanation each time.',
            'She asked the author to rewrite the chapter.',
          ],
          correctIndex: 1,
          explanation: 'The passage states she settled on "retaining the original Marathi term throughout the English text."',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'What risk did Deepti need to balance when making this choice?',
          options: [
            'That too many untranslated terms could alienate readers unfamiliar with Marathi.',
            'That the publisher might reject the book entirely.',
            'That the novel might become too short.',
            'That other translators might copy her approach.',
          ],
          correctIndex: 0,
          explanation: 'The passage notes "this decision required a delicate balance, since too many untranslated terms could alienate readers."',
          difficulty: Difficulty.hard,
        ),
        PracticeQuestion(
          prompt: 'What does Deepti conclude about translation by the end of the passage?',
          options: [
            'That translation is simply a mechanical process of matching words.',
            'That translation involves careful choices about what can be preserved and what will inevitably be lost between languages.',
            'That some languages cannot be translated at all.',
            'That translators should always avoid using foreign words.',
          ],
          correctIndex: 1,
          explanation: 'She reflects that translation "was rarely about finding perfect equivalents at all, but about making careful...choices about what could be preserved and what would inevitably be lost."',
          difficulty: Difficulty.hard,
        ),
      ],
      glosses: [
        InlineGloss(word: 'equivalents', meaningHi: 'समकक्ष शब्द', hiTransliteration: 'samkaksh shabd', meaningGu: 'સમકક્ષ શબ્દો', guTransliteration: 'samkaksh shabdo'),
        InlineGloss(word: 'nuance', meaningHi: 'सूक्ष्म भेद / बारीकी', hiTransliteration: 'sookshm bhed / baariki', meaningGu: 'બારીકી / સૂક્ષ્મ ભેદ', guTransliteration: 'baariki / sookshma bhed'),
        InlineGloss(word: 'clinically', meaningHi: 'भावनारहित तरीके से', hiTransliteration: 'bhaavnaarahit tarike se', meaningGu: 'ભાવનાહીન રીતે', guTransliteration: 'bhavnahin rite'),
        InlineGloss(word: 'alienate', meaningHi: 'दूर कर देना / अलगाव पैदा करना', hiTransliteration: 'door kar dena / algaav paida karna', meaningGu: 'દૂર કરી દેવું / અળગા કરવું', guTransliteration: 'door kari devu / alga karvu'),
        InlineGloss(word: 'flattened', meaningHi: 'सपाट बना देना (गहराई खत्म करना)', hiTransliteration: 'sapaat bana dena (gehraai khatam karna)', meaningGu: 'સપાટ બનાવી દેવું (ઊંડાણ ખતમ કરવું)', guTransliteration: 'sapaat banavi devu (undan khatam karvu)'),
      ],
    ),
  ],
);
