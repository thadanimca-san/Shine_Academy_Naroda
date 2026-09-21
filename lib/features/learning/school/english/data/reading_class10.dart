import '../models/chapter.dart' show InlineGloss;
import '../models/practice_question.dart';
import '../models/reading_passage.dart';

const class10Reading = ReadingLibrary(
  id: 'class10_reading',
  title: 'Reading Passages',
  grade: 'Class 10',
  passages: [
    ReadingPassage(
      id: 'class10_reading_antibiotics',
      title: 'A Race Against Resistance',
      emoji: '🦠',
      grade: 'Class 10',
      difficulty: Difficulty.hard,
      body: 'When antibiotics first became widely available in the mid-twentieth century, they were '
          'celebrated, with good reason, as one of medicine\'s most transformative achievements, turning '
          'previously fatal bacterial infections into conditions treatable within days rather than death '
          'sentences requiring weeks of uncertain recovery or none at all. Decades later, however, physicians '
          'worldwide face a troubling reversal of this progress: bacteria evolving resistance to these once-'
          'reliable drugs faster than pharmaceutical research can develop meaningful replacements.\n\n'
          'The mechanism behind this crisis is neither mysterious nor particularly complicated, though its '
          'implications are genuinely alarming. Every time antibiotics are used, whether appropriately for a '
          'genuine bacterial infection or inappropriately for viral illnesses that antibiotics cannot actually '
          'treat, surviving bacteria carrying chance genetic mutations that confer resistance gain a '
          'significant survival advantage, reproducing while their more vulnerable counterparts are eliminated. '
          'Over enough generations, and bacteria reproduce remarkably quickly, resistant strains can come to '
          'dominate entire bacterial populations.\n\n'
          'Dr. Rajiv Malhotra, a microbiologist studying resistance patterns in Indian hospitals, explained '
          'that this problem is compounded significantly by widespread antibiotic misuse: patients frequently '
          'stopping courses early once symptoms improve rather than completing the full prescribed duration, '
          'inappropriate prescriptions for viral infections where antibiotics offer no genuine benefit, and '
          'extensive agricultural use of antibiotics in livestock farming, which creates additional selective '
          'pressure favouring resistant bacterial strains across entire ecosystems.\n\n'
          'Addressing this crisis, Dr. Malhotra argued, required coordinated action across multiple fronts '
          'simultaneously: stricter regulation of antibiotic prescriptions, sustained public education about '
          'completing prescribed courses properly, renewed pharmaceutical investment in developing genuinely '
          'new antibiotic classes despite limited commercial incentive given these drugs\' relatively short-term '
          'use compared to medications for chronic conditions, and international cooperation, since resistant '
          'bacteria, unconstrained by any border, could spread rapidly between countries through travel and '
          'trade alike.',
      bodyHi: 'जब बीसवीं शताब्दी के मध्य में एंटीबायोटिक्स पहली बार व्यापक रूप से उपलब्ध हो गए, तो उन्हें अच्छे कारण के साथ, दवा की सबसे परिवर्तनकारी उपलब्धियों में से एक के रूप में मनाया गया, जिसने पहले के घातक जीवाणु संक्रमण को मौत की सजा के बजाय दिनों के भीतर इलाज योग्य स्थिति में बदल दिया, जिसके लिए हफ्तों की अनिश्चित वसूली की आवश्यकता थी या बिल्कुल भी नहीं। हालाँकि, दशकों बाद, दुनिया भर के चिकित्सकों को इस प्रगति के एक परेशान करने वाले उलटफेर का सामना करना पड़ रहा है: फार्मास्युटिकल अनुसंधान की तुलना में बैक्टीरिया इन एक बार विश्वसनीय दवाओं के लिए तेजी से प्रतिरोध विकसित कर रहे हैं, जो सार्थक प्रतिस्थापन विकसित कर सकते हैं।\n\nइस संकट के पीछे का तंत्र न तो रहस्यमय है और न ही विशेष रूप से जटिल है, हालांकि इसके निहितार्थ वास्तव में चिंताजनक हैं। हर बार जब एंटीबायोटिक्स का उपयोग किया जाता है, चाहे वास्तविक जीवाणु संक्रमण के लिए उचित रूप से या वायरल बीमारियों के लिए अनुचित रूप से, जिनका एंटीबायोटिक्स वास्तव में इलाज नहीं कर सकते हैं, आनुवंशिक उत्परिवर्तन वाले जीवित बैक्टीरिया जो प्रतिरोध प्रदान करते हैं, एक महत्वपूर्ण अस्तित्व लाभ प्राप्त करते हैं, प्रजनन करते हैं जबकि उनके अधिक कमजोर समकक्ष समाप्त हो जाते हैं। पर्याप्त पीढ़ियों तक, और बैक्टीरिया उल्लेखनीय रूप से तेजी से प्रजनन करते हैं, प्रतिरोधी उपभेद संपूर्ण बैक्टीरिया आबादी पर हावी हो सकते हैं।\n\nडॉ. भारतीय अस्पतालों में प्रतिरोध पैटर्न का अध्ययन करने वाले एक माइक्रोबायोलॉजिस्ट राजीव मल्होत्रा ने बताया कि यह समस्या बड़े पैमाने पर एंटीबायोटिक के दुरुपयोग से काफी बढ़ गई है: रोगी पूरी निर्धारित अवधि पूरी करने के बजाय लक्षणों में सुधार होने पर बार-बार कोर्स बंद कर देते हैं, वायरल संक्रमण के लिए अनुपयुक्त नुस्खे जहां एंटीबायोटिक्स कोई वास्तविक लाभ नहीं देते हैं, और पशुधन खेती में एंटीबायोटिक दवाओं का व्यापक कृषि उपयोग, जो पूरे पारिस्थितिक तंत्र में प्रतिरोधी बैक्टीरिया उपभेदों के पक्ष में अतिरिक्त चयनात्मक दबाव बनाता है।\n\nइस संकट को संबोधित करते हुए, डॉ. मल्होत्रा ने तर्क दिया, एक साथ कई मोर्चों पर समन्वित कार्रवाई की आवश्यकता है: एंटीबायोटिक का सख्त विनियमन: नुस्खे, निर्धारित पाठ्यक्रमों को ठीक से पूरा करने के बारे में निरंतर सार्वजनिक शिक्षा, पुरानी स्थितियों के लिए दवाओं की तुलना में इन दवाओं के अपेक्षाकृत अल्पकालिक उपयोग को देखते हुए सीमित वाणिज्यिक प्रोत्साहन के बावजूद वास्तव में नए एंटीबायोटिक वर्गों को विकसित करने में नए सिरे से फार्मास्युटिकल निवेश, और अंतरराष्ट्रीय सहयोग, क्योंकि प्रतिरोधी बैक्टीरिया, किसी भी सीमा से अप्रतिबंधित, यात्रा और व्यापार के माध्यम से देशों के बीच तेजी से फैल सकता है।',
      bodyGu: '''જ્યારે વીસમી સદીના મધ્યમાં એન્ટિબાયોટિક્સ પ્રથમ વખત વ્યાપકપણે ઉપલબ્ધ બન્યા, ત્યારે તેમને યોગ્ય કારણ સાથે, દવાની સૌથી ક્રાંતિકારી સિદ્ધિઓમાંની એક તરીકે ઉજવવામાં આવ્યા, જેણે પહેલાના જીવલેણ બેક્ટેરિયલ ચેપને મૃત્યુદંડની સજાને બદલે દિવસોની અંદર સારવાર યોગ્ય સ્થિતિમાં બદલી દીધો, જેના માટે અઠવાડિયાની અનિશ્ચિત રિકવરીની જરૂર હતી અથવા બિલકુલ નહોતી. જોકે, દાયકાઓ પછી, વિશ્વભરના તબીબોને આ પ્રગતિના એક ચિંતાજનક ઉલટાપણાનો સામનો કરવો પડી રહ્યો છે: ફાર્માસ્યુટિકલ સંશોધનની સરખામણીમાં બેક્ટેરિયા આ એક સમયે વિશ્વસનીય દવાઓ સામે ઝડપથી પ્રતિકાર વિકસાવી રહ્યા છે, જે સાર્થક વિકલ્પો વિકસાવી શકે છે.

આ કટોકટી પાછળની પદ્ધતિ ન તો રહસ્યમય છે કે ન તો ખાસ જટિલ છે, જોકે તેની અસરો ખરેખર ચિંતાજનક છે. દર વખતે જ્યારે એન્ટિબાયોટિક્સનો ઉપયોગ કરવામાં આવે છે, પછી ભલે વાસ્તવિક બેક્ટેરિયલ ચેપ માટે યોગ્ય રીતે અથવા વાયરલ બીમારીઓ માટે અયોગ્ય રીતે, જેની એન્ટિબાયોટિક્સ ખરેખર સારવાર કરી શકતા નથી, આનુવંશિક પરિવર્તન ધરાવતા જીવંત બેક્ટેરિયા જે પ્રતિકાર પ્રદાન કરે છે, તેઓ નોંધપાત્ર અસ્તિત્વનો લાભ મેળવે છે, પ્રજનન કરે છે જ્યારે તેમના વધુ નબળા સમકક્ષ નાશ પામે છે. પૂરતી પેઢીઓ સુધી, અને બેક્ટેરિયા નોંધપાત્ર રીતે ઝડપથી પ્રજનન કરે છે, પ્રતિરોધક જાતો સમગ્ર બેક્ટેરિયલ વસ્તી પર પ્રભુત્વ મેળવી શકે છે.

ભારતીય હોસ્પિટલોમાં પ્રતિકારની પેટર્નનો અભ્યાસ કરતા માઇક્રોબાયોલોજિસ્ટ ડૉ. રાજીવ મલ્હોત્રાએ સમજાવ્યું કે આ સમસ્યા મોટા પાયે એન્ટિબાયોટિકના દુરુપયોગથી નોંધપાત્ર રીતે વધી છે: દર્દીઓ સંપૂર્ણ નિર્ધારિત સમયગાળો પૂર્ણ કરવાને બદલે લક્ષણોમાં સુધારો થવા પર વારંવાર કોર્સ અધવચ્ચે અટકાવી દે છે, વાયરલ ચેપ માટે અયોગ્ય પ્રિસ્ક્રિપ્શન જ્યાં એન્ટિબાયોટિક્સ કોઈ વાસ્તવિક લાભ આપતા નથી, અને પશુપાલનમાં એન્ટિબાયોટિક દવાઓનો વ્યાપક કૃષિ ઉપયોગ, જે સમગ્ર ઇકોસિસ્ટમમાં પ્રતિરોધક બેક્ટેરિયાની જાતોની તરફેણમાં વધારાનું પસંદગીયુક્ત દબાણ ઊભું કરે છે.

આ કટોકટીને સંબોધતા, ડૉ. મલ્હોત્રાએ દલીલ કરી, એકસાથે અનેક મોરચે સંકલિત કાર્યવાહીની જરૂર છે: એન્ટિબાયોટિક પ્રિસ્ક્રિપ્શનનું કડક નિયમન, નિર્ધારિત કોર્સને યોગ્ય રીતે પૂર્ણ કરવા વિશે સતત જાહેર શિક્ષણ, જૂની બીમારીઓ માટેની દવાઓની સરખામણીમાં આ દવાઓના પ્રમાણમાં ટૂંકા ગાળાના ઉપયોગને જોતા મર્યાદિત વ્યાપારી પ્રોત્સાહન હોવા છતાં ખરેખર નવા એન્ટિબાયોટિક વર્ગો વિકસાવવા માટે નવેસરથી ફાર્માસ્યુટિકલ રોકાણ, અને આંતરરાષ્ટ્રીય સહકાર, કારણ કે પ્રતિરોધક બેક્ટેરિયા, કોઈપણ સરહદથી મુક્ત, મુસાફરી અને વેપાર દ્વારા દેશો વચ્ચે ઝડપથી ફેલાઈ શકે છે.''',
      questions: [
        PracticeQuestion(
          prompt: 'Why were antibiotics initially considered one of medicine\'s most transformative achievements?',
          options: [
            'They cured all diseases instantly.',
            'They turned previously fatal bacterial infections into conditions treatable within days.',
            'They were the first medicines ever discovered.',
            'They eliminated the need for hospitals.',
          ],
          correctIndex: 1,
          explanation: 'The passage states they turned fatal infections "into conditions treatable within days rather than death sentences."',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'According to the passage, how does antibiotic resistance actually develop in bacteria?',
          options: [
            'Antibiotics directly create new bacteria.',
            'Bacteria with chance resistant mutations survive antibiotic use and reproduce, gradually dominating the population.',
            'Resistance only develops in hospitals, nowhere else.',
            'All bacteria become resistant simultaneously and instantly.',
          ],
          correctIndex: 1,
          explanation: 'The passage explains resistant bacteria "gain a significant survival advantage, reproducing while their more vulnerable counterparts are eliminated."',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'What three examples of antibiotic misuse does Dr. Malhotra mention?',
          options: [
            'Overpricing, underproduction, and poor storage.',
            'Stopping courses early, inappropriate prescriptions for viral infections, and agricultural use in livestock.',
            'Using antibiotics only in emergencies, never routinely.',
            'Refusing to prescribe antibiotics at all.',
          ],
          correctIndex: 1,
          explanation: 'The passage lists exactly these three factors as compounding the resistance problem.',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'Why does the passage suggest pharmaceutical companies have limited incentive to develop new antibiotics?',
          options: [
            'Because antibiotics are illegal to sell.',
            'Because these drugs are used relatively short-term, unlike medications for chronic conditions, reducing their long-term commercial value.',
            'Because bacteria cannot be studied properly.',
            'Because governments ban all new antibiotic research.',
          ],
          correctIndex: 1,
          explanation: 'The passage notes limited commercial incentive "given these drugs\' relatively short-term use compared to medications for chronic conditions."',
          difficulty: Difficulty.hard,
        ),
      ],
      glosses: [
        InlineGloss(word: 'transformative', meaningHi: 'क्रांतिकारी परिवर्तन लाने वाला', hiTransliteration: 'kraantikaari parivartan laane wala', meaningGu: 'ક્રાંતિકારી પરિવર્તન લાવનાર', guTransliteration: 'krantikari parivartan lavnar'),
        InlineGloss(word: 'resistance', meaningHi: 'प्रतिरोध', hiTransliteration: 'pratirodh', meaningGu: 'પ્રતિકાર', guTransliteration: 'pratikar'),
        InlineGloss(word: 'mutations', meaningHi: 'उत्परिवर्तन (आनुवंशिक बदलाव)', hiTransliteration: 'utparivartan (aanuvanshik badlaav)', meaningGu: 'ઉત્પરિવર્તન (આનુવંશિક ફેરફાર)', guTransliteration: 'utparivartan (aanuvanshik ferfar)'),
        InlineGloss(word: 'confer', meaningHi: 'प्रदान करना', hiTransliteration: 'pradaan karna', meaningGu: 'પ્રદાન કરવું', guTransliteration: 'pradan karvu'),
        InlineGloss(word: 'compounded', meaningHi: 'और अधिक गंभीर बनाया गया', hiTransliteration: 'aur adhik gambhir banaya gaya', meaningGu: 'વધુ ગંભીર બનાવવામાં આવ્યું', guTransliteration: 'vadhu gambhir banavvama aavyu'),
        InlineGloss(word: 'selective pressure', meaningHi: 'चयनात्मक दबाव', hiTransliteration: 'chayanaatmak dabaav', meaningGu: 'પસંદગીયુક્ત દબાણ', guTransliteration: 'pasandgiyukt daban'),
        InlineGloss(word: 'unconstrained', meaningHi: 'बिना किसी बंधन के', hiTransliteration: 'bina kisi bandhan ke', meaningGu: 'કોઈપણ બંધન વિના', guTransliteration: 'koipan bandhan vina'),
      ],
    ),
    ReadingPassage(
      id: 'class10_reading_urbanplanning',
      title: 'The City That Redesigned Itself',
      emoji: '🏙️',
      grade: 'Class 10',
      difficulty: Difficulty.hard,
      body: 'A decade ago, the mid-sized city of Kolar faced a transportation crisis familiar to urban planners '
          'across rapidly growing Indian cities: traffic congestion so severe during peak hours that average '
          'commute times had nearly tripled within just five years, while public bus services, chronically '
          'underfunded and unreliable, carried a shrinking share of daily commuters as anyone who could afford '
          'a private vehicle abandoned public transport almost entirely.\n\n'
          'Rather than pursuing the conventional response of widening roads, an approach traffic engineers had '
          'increasingly recognised tended to attract more vehicles rather than genuinely reducing congestion, '
          'Kolar\'s newly appointed transportation commissioner, Deepa Rajagopal, proposed a fundamentally '
          'different strategy centred on making public transport genuinely competitive with private vehicles '
          'rather than simply accommodating ever-increasing car ownership.\n\n'
          'Her plan involved substantial upfront investment that initially drew considerable political '
          'criticism: dedicated bus lanes physically separated from general traffic, a real-time tracking '
          'system allowing commuters to know precisely when buses would arrive rather than waiting '
          'indefinitely, and a unified payment card usable across buses, the city\'s newly constructed metro '
          'line, and shared bicycle stations, eliminating the friction of separate tickets for each transport '
          'mode. Critics argued the investment diverted funds from more immediately visible road-widening '
          'projects that voters more readily associated with tangible progress.\n\n'
          'Five years after implementation, independent transportation surveys found average commute times had '
          'decreased by nearly thirty percent despite the city\'s population continuing to grow substantially '
          'during the same period, and public transport ridership had more than doubled. Rajagopal, now '
          'frequently invited to advise other cities facing similar challenges, has consistently emphasised '
          'that her approach succeeded not because of any single innovative technology, but because it treated '
          'public transport users as customers whose time and convenience genuinely mattered, rather than as a '
          'population simply expected to tolerate whatever service happened to be provided.',
      bodyHi: 'एक दशक पहले, कोलार के मध्यम आकार के शहर को तेजी से बढ़ते भारतीय शहरों में शहरी योजनाकारों से परिचित एक परिवहन संकट का सामना करना पड़ा था: पीक ऑवर्स के दौरान यातायात की भीड़ इतनी गंभीर थी कि औसत आवागमन का समय केवल पांच वर्षों के भीतर लगभग तीन गुना हो गया था, जबकि सार्वजनिक बस सेवाएं, जो लंबे समय से कम वित्तपोषित और अविश्वसनीय थीं, उनमें दैनिक यात्रियों की संख्या कम हो गई थी, क्योंकि जो कोई भी निजी वाहन खरीद सकता था उसने सार्वजनिक परिवहन को लगभग पूरी तरह से छोड़ दिया था। वास्तव में भीड़भाड़ को कम करने के बजाय, कोलार की नवनियुक्त परिवहन आयुक्त, दीपा राजगोपाल ने सार्वजनिक परिवहन को निजी वाहनों के साथ वास्तव में प्रतिस्पर्धी बनाने पर केंद्रित एक मौलिक रूप से अलग रणनीति का प्रस्ताव दिया, न कि केवल बढ़ती कार स्वामित्व को समायोजित करने के बजाय।\n\nउनकी योजना में पर्याप्त अग्रिम निवेश शामिल था, जिसकी शुरुआत में काफी राजनीतिक आलोचना हुई: समर्पित बस लेन भौतिक रूप से सामान्य यातायात से अलग, एक वास्तविक समय ट्रैकिंग प्रणाली जो यात्रियों को अनिश्चित काल तक इंतजार करने के बजाय सटीक रूप से जानने की अनुमति देती है कि बसें कब आएंगी, और बसों में उपयोग करने योग्य एक एकीकृत भुगतान कार्ड। शहर की नवनिर्मित मेट्रो लाइन, और साझा साइकिल स्टेशन, प्रत्येक परिवहन मोड के लिए अलग-अलग टिकटों की झंझट को समाप्त करते हैं। आलोचकों का तर्क है कि निवेश ने तत्काल दिखाई देने वाली सड़क-चौड़ीकरण परियोजनाओं से धन को हटा दिया, जिससे मतदाता मूर्त प्रगति के साथ अधिक आसानी से जुड़ गए।\n\nकार्यान्वयन के पांच साल बाद, स्वतंत्र परिवहन सर्वेक्षण में पाया गया कि औसत आवागमन समय में लगभग तीस प्रतिशत की कमी आई है, जबकि इसी अवधि के दौरान शहर की आबादी लगातार बढ़ती जा रही है, और सार्वजनिक परिवहन सवारियों की संख्या दोगुनी से अधिक हो गई है। राजगोपाल, जिन्हें अब इसी तरह की चुनौतियों का सामना करने वाले अन्य शहरों को सलाह देने के लिए अक्सर आमंत्रित किया जाता है, ने लगातार इस बात पर जोर दिया है कि उनका दृष्टिकोण किसी एक नवीन तकनीक के कारण सफल नहीं हुआ, बल्कि इसलिए कि उन्होंने सार्वजनिक परिवहन उपयोगकर्ताओं को ऐसे ग्राहकों के रूप में माना, जिनका समय और सुविधा वास्तव में मायने रखती थी, न कि एक आबादी के रूप में जो भी प्रदान की जाने वाली सेवा को सहन करने की अपेक्षा करती है।',
      bodyGu: '''એક દાયકા પહેલાં, કોલારના મધ્યમ કદના શહેરને ઝડપથી વિકસતા ભારતીય શહેરોના શહેરી આયોજકો માટે પરિચિત એવા પરિવહન સંકટનો સામનો કરવો પડ્યો હતો: પીક અવર્સ દરમિયાન ટ્રાફિકની ભીડ એટલી ગંભીર હતી કે સરેરાશ મુસાફરીનો સમય માત્ર પાંચ વર્ષમાં લગભગ ત્રણ ગણો વધી ગયો હતો, જ્યારે સાર્વજનિક બસ સેવાઓ, જે લાંબા સમયથી ઓછા ભંડોળવાળી અને અવિશ્વસનીય હતી, તેમાં દૈનિક મુસાફરોની સંખ્યા ઘટી ગઈ હતી, કારણ કે જે કોઈ પણ ખાનગી વાહન ખરીદી શકતું હતું તેણે સાર્વજનિક પરિવહનને લગભગ સંપૂર્ણપણે છોડી દીધું હતું. વાસ્તવમાં ભીડભાડ ઘટાડવાને બદલે, કોલારના નવા નિયુક્ત પરિવહન કમિશનર, દીપા રાજગોપાલે સાર્વજનિક પરિવહનને ખાનગી વાહનો સાથે વાસ્તવમાં સ્પર્ધાત્મક બનાવવા પર કેન્દ્રિત એક મૂળભૂત રીતે અલગ વ્યૂહરચનાનો પ્રસ્તાવ મૂક્યો, નહીં કે માત્ર વધતી જતી કારની માલિકીને સમાયોજિત કરવાને બદલે.

તેમની યોજનામાં નોંધપાત્ર અગ્રિમ રોકાણ સામેલ હતું, જેની શરૂઆતમાં ઘણી રાજકીય ટીકા થઈ હતી: સામાન્ય ટ્રાફિકથી ભૌતિક રીતે અલગ સમર્પિત બસ લેન, એક રિયલ-ટાઇમ ટ્રેકિંગ સિસ્ટમ જે મુસાફરોને અનિશ્ચિત સમય સુધી રાહ જોવાને બદલે બસો ક્યારે આવશે તે બરાબર જાણવાની મંજૂરી આપે છે, અને બસોમાં ઉપયોગ કરી શકાય તેવું એકીકૃત ચુકવણી કાર્ડ. શહેરની નવી બનેલી મેટ્રો લાઇન, અને શેર કરેલા સાયકલ સ્ટેશન, દરેક પરિવહન મોડ માટે અલગ-અલગ ટિકિટોની ઝંઝટને દૂર કરે છે. ટીકાકારોની દલીલ છે કે રોકાણે તાત્કાલિક દેખાતા રસ્તા-પહોળા કરવાના પ્રોજેક્ટ્સમાંથી ભંડોળ વાળ્યું, જેની સાથે મતદાતાઓ મૂર્ત પ્રગતિ સાથે વધુ સરળતાથી જોડાયા હતા.

અમલીકરણના પાંચ વર્ષ પછી, સ્વતંત્ર પરિવહન સર્વેક્ષણમાં જાણવા મળ્યું કે સરેરાશ મુસાફરીના સમયમાં લગભગ ત્રીસ ટકાનો ઘટાડો થયો છે, જ્યારે સમાન સમયગાળા દરમિયાન શહેરની વસ્તીમાં સતત વધારો થતો રહ્યો છે, અને સાર્વજનિક પરિવહનના મુસાફરોની સંખ્યા બમણાથી વધુ થઈ ગઈ છે. રાજગોપાલ, જેમને હવે સમાન પડકારોનો સામનો કરી રહેલા અન્ય શહેરોને સલાહ આપવા માટે વારંવાર આમંત્રિત કરવામાં આવે છે, તેમણે સતત એ વાત પર ભાર મૂક્યો છે કે તેમનો અભિગમ કોઈ એક નવીન તકનીકને કારણે સફળ થયો નથી, પરંતુ એટલા માટે કે તેમણે સાર્વજનિક પરિવહન વપરાશકર્તાઓને એવા ગ્રાહકો તરીકે માન્યા, જેમનો સમય અને સુવિધા ખરેખર મહત્વની હતી, ન કે એવી વસ્તી તરીકે જે પણ સેવા આપવામાં આવે તેને સહન કરવાની અપેક્ષા રાખે.''',
      questions: [
        PracticeQuestion(
          prompt: 'What transportation problem did Kolar face before the redesign?',
          options: [
            'The city had no roads at all.',
            'Severe traffic congestion with commute times nearly tripling, while public bus services were underfunded and unreliable.',
            'Too few private vehicles on the road.',
            'The metro line was overcrowded from the start.',
          ],
          correctIndex: 1,
          explanation: 'The passage describes "traffic congestion so severe...commute times had nearly tripled" and buses that were "chronically underfunded and unreliable."',
          difficulty: Difficulty.easy,
        ),
        PracticeQuestion(
          prompt: 'Why did Rajagopal avoid the conventional approach of widening roads?',
          options: [
            'It was too expensive to consider at all.',
            'Traffic engineers had recognised that widening roads tended to attract more vehicles rather than reducing congestion.',
            'The city had no space to widen any roads.',
            'The government banned road construction.',
          ],
          correctIndex: 1,
          explanation: 'The passage notes this approach "tended to attract more vehicles rather than genuinely reducing congestion."',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'What three elements made up Rajagopal\'s public transport plan?',
          options: [
            'Higher fares, fewer buses, and longer routes.',
            'Dedicated bus lanes, real-time tracking, and a unified payment card across transport modes.',
            'Free public transport for all citizens.',
            'Banning private vehicles entirely from the city.',
          ],
          correctIndex: 1,
          explanation: 'The passage lists exactly these three specific elements of her plan.',
          difficulty: Difficulty.medium,
        ),
        PracticeQuestion(
          prompt: 'According to Rajagopal, what was the real reason her approach succeeded?',
          options: [
            'A single innovative piece of technology solved everything.',
            'It treated public transport users as customers whose time and convenience genuinely mattered.',
            'It was simply the cheapest available option.',
            'It received unanimous political support from the start.',
          ],
          correctIndex: 1,
          explanation: 'She emphasises success came "not because of any single innovative technology, but because it treated public transport users as customers."',
          difficulty: Difficulty.hard,
        ),
      ],
      glosses: [
        InlineGloss(word: 'congestion', meaningHi: 'भीड़भाड़', hiTransliteration: 'bheedbhaad', meaningGu: 'ભીડભાડ', guTransliteration: 'bheedbhaad'),
        InlineGloss(word: 'chronically', meaningHi: 'लगातार / दीर्घकालिक रूप से', hiTransliteration: 'lagatar / deerghkaalik roop se', meaningGu: 'સતત / લાંબા સમયથી', guTransliteration: 'satat / lamba samaythi'),
        InlineGloss(word: 'conventional', meaningHi: 'पारंपरिक', hiTransliteration: 'paramparik', meaningGu: 'પારંપરિક', guTransliteration: 'paramparik'),
        InlineGloss(word: 'friction', meaningHi: 'बाधा / रुकावट', hiTransliteration: 'baadha / rukaawat', meaningGu: 'અડચણ / મુશ્કેલી', guTransliteration: 'adachan / mushkeli'),
        InlineGloss(word: 'ridership', meaningHi: 'सवारियों की संख्या', hiTransliteration: 'sawaariyon ki sankhya', meaningGu: 'મુસાફરોની સંખ્યા', guTransliteration: 'musafaroni sankhya'),
        InlineGloss(word: 'tangible', meaningHi: 'ठोस / स्पष्ट रूप से दिखने वाला', hiTransliteration: 'thos / spasht roop se dikhne wala', meaningGu: 'મૂર્ત / સ્પષ્ટ દેખાતું', guTransliteration: 'moort / spasht dekhatu'),
      ],
    ),
  ],
);
