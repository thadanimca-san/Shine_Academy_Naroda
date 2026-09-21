import '../models/chapter.dart';

/// Draft chapter — written to match typical Class 8 English-medium reader
/// style and difficulty, not copied from an actual GSEB/CBSE textbook.
const chapterClass8Robotics = Chapter(
  id: 'chapter_class8_robotics',
  title: 'The Robot That Learned to Listen',
  grade: 'Class 8',
  emoji: '🤖',
  chapterText:
      'When the state-level robotics competition announced its theme, "Machines for the Differently Abled," '
      'Ananya\'s team decided almost immediately to build a robotic arm that could assist people with limited '
      'hand mobility in everyday tasks. Their initial design, cobbled together from spare servo motors and '
      'a second-hand microcontroller, could grip a cup reasonably well but fumbled badly whenever the object\'s '
      'shape or weight changed even slightly.\n\n'
      'Frustrated after weeks of adjustments that barely improved performance, the team visited a local '
      'rehabilitation centre at their mentor\'s suggestion, hoping simply to observe how existing assistive '
      'devices worked in practice. There, they met Mr. Fernandes, a retired mechanic who had lost most function '
      'in his right hand after a stroke, and who patiently described exactly which everyday movements frustrated '
      'him most: turning door handles, holding a spoon steady, and buttoning his shirt collar.\n\n'
      'This conversation completely changed the team\'s approach. Rather than continuing to design a generic '
      'gripping arm, they began building sensors that could detect an object\'s texture and adjust grip pressure '
      'accordingly, since Mr. Fernandes had explained that many devices either crushed soft objects or dropped '
      'delicate ones. They also added simple voice commands, since he sometimes struggled with small buttons '
      'and switches on existing devices.\n\n'
      'On competition day, the team\'s device successfully lifted a paper cup, a metal spoon, and a soft cloth '
      'without dropping or crushing any of them, earning them the top prize in their category. Ananya later '
      'admitted to a local reporter that the most valuable lesson from the entire project had nothing to do '
      'with circuits or code: it was learning to listen carefully to the actual person a design was meant to '
      'help, rather than assuming what they might need.',
  hindiText: '''जब राज्य-स्तरीय रोबोटिक्स प्रतियोगिता ने अपनी थीम "विशेष रूप से सक्षम लोगों के लिए मशीनें" की घोषणा की, तो अनन्या की टीम ने लगभग तुरंत ही एक ऐसा रोबोटिक हाथ बनाने का फैसला किया जो सीमित हाथ गतिशीलता वाले लोगों को रोजमर्रा के कामों में सहायता कर सके। उनका शुरुआती डिज़ाइन, जो स्पेयर सर्वो मोटर्स और एक सेकंड-हैंड माइक्रोकंट्रोलर से मिलकर बनाया गया था, एक कप को ठीक-ठाक पकड़ सकता था, लेकिन जब भी वस्तु के आकार या वजन में थोड़ा सा भी बदलाव होता था, तो वह बुरी तरह विफल हो जाता था।

प्रदर्शन में मुश्किल से सुधार करने वाले हफ्तों के संशोधनों के बाद निराश होकर, टीम ने अपने मेंटर के सुझाव पर एक स्थानीय पुनर्वास केंद्र का दौरा किया, यह उम्मीद करते हुए कि वे केवल यह देख सकें कि मौजूदा सहायक उपकरण व्यावहारिक रूप से कैसे काम करते हैं। वहां वे श्री फर्नांडिस से मिले, जो एक सेवानिवृत्त मैकेनिक थे, जिन्होंने स्ट्रोक के बाद अपने दाहिने हाथ की अधिकांश कार्यक्षमता खो दी थी, और जिन्होंने धैर्यपूर्वक ठीक-ठीक बताया कि कौन सी रोजमर्रा की हरकतें उन्हें सबसे ज्यादा परेशान करती हैं: दरवाजे के हैंडल घुमाना, चम्मच को स्थिर रखना, और अपनी शर्ट का कॉलर बंद करना।

इस बातचीत ने टीम के दृष्टिकोण को पूरी तरह से बदल दिया। एक सामान्य ग्रिपिंग आर्म डिजाइन करना जारी रखने के बजाय, उन्होंने ऐसे सेंसर बनाना शुरू किया जो किसी वस्तु की बनावट का पता लगा सकें और उसके अनुसार पकड़ के दबाव को समायोजित कर सकें, क्योंकि श्री फर्नांडिस ने समझाया था कि कई उपकरण या तो नरम वस्तुओं को कुचल देते हैं या नाजुक वस्तुओं को गिरा देते हैं। उन्होंने सरल आवाज कमांड भी जोड़े, क्योंकि उन्हें कभी-कभी मौजूदा उपकरणों पर छोटे बटन और स्विच के साथ संघर्ष करना पड़ता था।

प्रतियोगिता के दिन, टीम के उपकरण ने बिना किसी को गिराए या कुचलए एक पेपर कप, एक धातु का चम्मच, और एक नरम कपड़ा सफलतापूर्वक उठाया, जिससे उन्हें अपनी श्रेणी में शीर्ष पुरस्कार मिला। अनन्या ने बाद में एक स्थानीय रिपोर्टर को स्वीकार किया कि पूरे प्रोजेक्ट का सबसे मूल्यवान सबक सर्किट या कोड से कोई लेना-देना नहीं था: यह किसी डिज़ाइन की मदद के लिए बनाए गए वास्तविक व्यक्ति को ध्यान से सुनना सीखना था, न कि यह मान लेना कि उन्हें क्या चाहिए।''',
  gujaratiText: '''જ્યારે રાજ્ય-સ્તરીય રોબોટિક્સ સ્પર્ધાએ તેની થીમ "દિવ્યાંગો માટે મશીનો" ની જાહેરાત કરી, ત્યારે અનન્યાની ટીમએ લગભગ તરત જ એક રોબોટિક હાથ બનાવવાનું નક્કી કર્યું જે હાથની મર્યાદિત હિલચાલ ધરાવતા લોકોને રોજિંદા કાર્યોમાં મદદ કરી શકે. તેમની પ્રારંભિક ડિઝાઇન, જે વધારાની સર્વો મોટર્સ અને સેકન્ડ-હૅન્ડ માઇક્રોકંટ્રોલરથી ભેગી કરવામાં આવી હતી, તે કપને યોગ્ય રીતે પકડી શકતી હતી પરંતુ જ્યારે પણ વસ્તુના આકાર અથવા વજનમાં થોડો પણ ફેરફાર થતો હતો ત્યારે તે ખરાબ રીતે નિષ્ફળ જતી હતી.

પ્રદર્શનમાં માંડ સુધારો કરતા અઠવાડિયાના ફેરફારો પછી નિરાશ થઈને, ટીમએ તેમના μένтор (માર્ગદર્શક) ના સૂચન પર સ્થાનિક પુનર્વસન કેન્દ્રની મુલાકાત લીધી, ફક્ત એ જોવાની આશા રાખી કે હાલના સહાયક ઉપકરણો વ્યવહારમાં કેવી રીતે કામ કરે છે. ત્યાં તેઓ શ્રી ફર્નાન્ડિઝને મળ્યા, જેઓ એક નિવૃત્ત મિકેનિક હતા જેમણે સ્ટ્રોક પછી તેમના જમણા હાથની મોટાભાગની કાર્યક્ષમતા ગુમાવી દીધી હતી, અને જેમણે ધીરજપૂર્વક બરાબર વર્ણન કર્યું કે કઈ રોજિંદા હિલચાલ તેમને સૌથી વધુ પરેશાન કરે છે: દરવાજાના હેન્ડલ ફેરવવા, ચમચી સ્થિર પકડી રાખવી, અને તેમની શર્ટનું બટન બંધ કરવું.

આ વાતચીતે ટીમનો અભિગમ સંપૂર્ણપણે બદલી નાખ્યો. સામાન્ય ગ્રિપિંગ આર્મ ડિઝાઇન કરવાનું ચાલુ રાખવાને બદલે, તેમણે એવા સેન્સર બનાવવાનું શરૂ કર્યું જે વસ્તુની બનાવટ શોધી શકે અને તે મુજબ પકડનું દબાણ સમાયોજિત કરી શકે, કારણ કે શ્રી ફર્નાન્ડિઝે સમજાવ્યું હતું કે ઘણા ઉપકરણો કાં તો નરમ વસ્તુઓને કચડી નાખે છે અથવા નાજુક વસ્તુઓને છોડી દે છે. તેમણે સરળ વૉઇસ કમાન્ડ્સ પણ ઉમેર્યા, કારણ કે તેમને ક્યારેક હાલના ઉપકરણો પરના નાના બટનો અને સ્વીચો સાથે મુશ્કેલી પડતી હતી.

સ્પર્ધાના દિવસે, ટીમના ઉપકરણએ કોઈપણ વસ્તુને પાડ્યા કે કચડ્યા વિના પેપર કપ, ધાતુની ચમચી અને નરમ કાપડ સફળતાપૂર્વક ઊંચું કર્યું, જેનાથી તેમને તેમની શ્રેણીમાં સર્વોચ્ચ પુરસ્કાર મળ્યો. અનન્યાએ પાછળથી એક સ્થાનિક રિપોર્ટરને સ્વીકાર્યું કે સમગ્ર પ્રોજેક્ટમાંથી સૌથી મૂલ્યવાન પાઠ સર્કિટ કે કોડ સાથે કોઈ લેવાદેવા નહોતો: તે વાસ્તવિક વ્યક્તિને ધ્યાનથી સાંભળવાનું શીખવાનું હતું જેને ડિઝાઇન મદદ કરવા માટે બનાવવામાં આવી હતી, તેના બદલે એ ધારણા કરવાને બદલે કે તેમને શું જરૂર પડી શકે છે.''',
  hindiSummary:
      'यह कहानी अनन्या की टीम की है, जो एक रोबोटिक भुजा बनाती है जो दिव्यांग लोगों की मदद कर सके। शुरुआती डिज़ाइन असफल '
      'रहता है, लेकिन एक पुनर्वास केंद्र में मिस्टर फर्नांडीस से बातचीत के बाद टीम अपने डिज़ाइन में बड़े बदलाव करती है। '
      'अंततः उनका उपकरण प्रतियोगिता में पहला स्थान जीतता है। यह कहानी सिखाती है कि किसी भी समस्या को हल करने से पहले '
      'असली ज़रूरत को समझना कितना ज़रूरी है।',
  gujaratiSummary:
      'આ વાર્તા અનન્યાની ટીમની છે, જે એક રોબોટિક હાથ બનાવે છે જેથી દિવ્યાંગ લોકોની મદદ કરી શકાય. '
      'શરૂઆતની ડિઝાઇન નિષ્ફળ જાય છે, પરંતુ પુનર્વસન કેન્દ્રમાં મિસ્ટર ફર્નાન્ડિસ સાથે વાતચીત કર્યા પછી ટીમ પોતાની ડિઝાઇનમાં મોટા ફેરફારો કરે છે. '
      'અંતે તેમનું ઉપકરણ સ્પર્ધામાં પ્રથમ સ્થાન જીતે છે. '
      'આ વાર્તા શીખવે છે કે કોઈપણ સમસ્યાને ઉકેલતા પહેલા તેની સાચી જરૂરિયાતને સમજવી કેટલી જરૂરી છે.',
  glosses: [
    InlineGloss(word: 'cobbled together', meaningHi: 'जल्दबाज़ी में जोड़कर बनाया', hiTransliteration: 'jaldbaazi mein jodkar banaya'),
    InlineGloss(word: 'microcontroller', meaningHi: 'सूक्ष्म नियंत्रक (छोटी कंप्यूटर चिप)', hiTransliteration: 'sookshm niyantrak (chhoti computer chip)'),
    InlineGloss(word: 'fumbled', meaningHi: 'अनाड़ीपन से संभाला', hiTransliteration: 'anaadipan se sambhaala'),
    InlineGloss(word: 'rehabilitation centre', meaningHi: 'पुनर्वास केंद्र', hiTransliteration: 'punarvaas kendra'),
    InlineGloss(word: 'assistive devices', meaningHi: 'सहायक उपकरण', hiTransliteration: 'sahayak upkaran'),
    InlineGloss(word: 'texture', meaningHi: 'बनावट / सतह की प्रकृति', hiTransliteration: 'banaawat / satah ki prakriti'),
    InlineGloss(word: 'delicate', meaningHi: 'नाज़ुक', hiTransliteration: 'naazuk'),
  ],
);
