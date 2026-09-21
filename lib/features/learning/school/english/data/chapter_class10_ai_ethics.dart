import '../models/chapter.dart';

/// Draft chapter — written to match typical Class 10 English-medium reader
/// style and difficulty, not copied from an actual GSEB/CBSE textbook.
const chapterClass10AiEthics = Chapter(
  id: 'chapter_class10_ai_ethics',
  title: 'The Algorithm That Learned to Discriminate',
  grade: 'Class 10',
  emoji: '⚖️',
  chapterText:
      'When the multinational technology firm first deployed its automated hiring system, designed to screen '
      'thousands of job applications far faster than any human recruitment team could manage, executives '
      'presented it confidently as a triumph of objectivity, a tool supposedly immune to the unconscious human '
      'biases that had long troubled traditional hiring processes. Within eighteen months, however, an internal '
      'audit revealed a deeply troubling pattern: the system was systematically ranking female candidates lower '
      'than equally qualified male candidates for technical roles.\n\n'
      'Investigating engineers eventually traced the problem to its training data rather than any deliberately '
      'programmed bias. The algorithm had learned its evaluation criteria by analysing a decade of the '
      'company\'s previous successful hires, a dataset overwhelmingly dominated by male employees due to the '
      'technology industry\'s historical gender imbalance. Rather than correcting for this imbalance, the '
      'system had effectively learned to treat "maleness" itself as a subtle marker of hiring success, '
      'penalising resumes that even mentioned participation in women\'s technical clubs or all-women\'s '
      'colleges.\n\n'
      'This case, once made public, ignited considerable debate among technologists and ethicists alike about '
      'a deceptively simple-sounding question: could a machine, lacking any conscious intention to discriminate '
      'whatsoever, still be considered biased, and who bore genuine responsibility when it inevitably was? Some '
      'engineers argued the fault lay entirely with historical data reflecting genuine past inequality rather '
      'than the algorithm\'s design itself, while ethicists countered that deploying such a system without '
      'rigorous testing for exactly this kind of bias represented a serious failure of responsibility '
      'regardless of original intent.\n\n'
      'The company ultimately discontinued the automated system, replacing it with a hybrid process combining '
      'algorithmic screening with mandatory human review specifically trained to catch such patterns. The '
      'incident became a widely cited case study in technology ethics courses, illustrating a principle '
      'increasingly relevant to a world in which algorithms are trusted to guide consequential decisions: a '
      'system trained uncritically on biased historical patterns will typically reproduce and sometimes '
      'intensify that same bias, however sophisticated or "objective" it may initially appear.',
  hindiText: '''जब बहुराष्ट्रीय प्रौद्योगिकी फर्म ने अपनी स्वचालित भर्ती प्रणाली को पहली बार लागू किया, जिसे हजारों नौकरी के आवेदनों को किसी भी मानव भर्ती टीम की तुलना में कहीं अधिक तेजी से छांटने के लिए डिज़ाइन किया गया था, तो अधिकारियों ने आत्मविश्वासी होकर इसे निष्पक्षता की एक जीत के रूप में प्रस्तुत किया - एक ऐसा उपकरण जिसे कथित तौर पर उन अचेतन मानवीय पूर्वाग्रहों से मुक्त माना गया था, जिन्होंने लंबे समय से पारंपरिक भर्ती प्रक्रियाओं को परेशान किया था। हालांकि, अठारह महीनों के भीतर, एक आंतरिक ऑडिट ने एक बेहद परेशान करने वाला पैटर्न उजागर किया: यह प्रणाली तकनीकी भूमिकाओं के लिए समान रूप से योग्य पुरुष उम्मीदवारों की तुलना में महिला उम्मीदवारों को व्यवस्थित रूप से कम रैंक दे रही थी।

जांच कर रहे इंजीनियरों ने आखिरकार इस समस्या का पता जानबूझकर प्रोग्राम किए गए किसी पूर्वाग्रह के बजाय इसके प्रशिक्षण डेटा में लगाया। एल्गोरिथ्म ने कंपनी के पिछले एक दशक के सफल नियुक्तियों का विश्लेषण करके अपने मूल्यांकन मानदंडों को सीखा था, जो प्रौद्योगिकी उद्योग के ऐतिहासिक लैंगिक असंतुलन के कारण भारी रूप से पुरुष कर्मचारियों द्वारा वर्चस्व वाला डेटासेट था। इस असंतुलन को सुधारने के बजाय, प्रणाली ने प्रभावी रूप से \'पुरुष होने\' को ही भर्ती की सफलता का एक सूक्ष्म संकेत मानना सीख लिया था, और उन रिज्यूमे को भी दंडित कर रही थी जिनमें महिलाओं के तकनीकी क्लबों या केवल महिलाओं के कॉलेजों में भागीदारी का उल्लेख था।

एक बार सार्वजनिक होने पर, इस मामले ने प्रौद्योगिकीविदों और नीतिशास्त्रियों के बीच एक भ्रामक रूप से सरल लगने वाले प्रश्न पर काफी बहस छेड़ दी: क्या बिना किसी भेदभाव के किसी भीचेतन इरादे के बिना एक मशीन को अभी भी पक्षपाती माना जा सकता है, और जब यह अपरिहार्य रूप से ऐसा हुआ तो इसके लिए वास्तविक ज़िम्मेदारी किसकी थी? कुछ इंजीनियरों ने तर्क दिया कि दोष पूरी तरह से एल्गोरिथ्म के डिज़ाइन के बजाय वास्तविक अतीत की असमानता को दर्शाने वाले ऐतिहासिक डेटा में था, जबकि नीतिशास्त्रियों ने जवाब दिया कि मूल इरादे की परवाह किए बिना ठीक इस प्रकार के पूर्वाग्रह के लिए कठोर परीक्षण के बिना ऐसी प्रणाली को तैनात करना ज़िम्मेदारी की एक गंभीर विफलता का प्रतिनिधित्व करता है।

कंपनी ने अंततः स्वचालित प्रणाली को बंद कर दिया, और इसे ऐसे पैटर्न को पकड़ने के लिए विशेष रूप से प्रशिक्षित अनिवार्य मानव समीक्षा के साथ एल्गोरिथम स्क्रीनिंग को मिलाने वाली एक हाइब्रिड प्रक्रिया से बदल दिया। यह घटना प्रौद्योगिकी नीतिशास्त्र पाठ्यक्रमों में व्यापक रूप से उद्धृत एक केस स्टडी बन गई, जो एक ऐसे दुनिया में तेजी से प्रासंगिक सिद्धांत को दर्शाती है जहाँ महत्वपूर्ण निर्णयों का मार्गदर्शन करने के लिए एल्गोरिदम पर भरोसा किया जाता है: एक प्रणाली जिसे पक्षपाती ऐतिहासिक पैटर्न पर बिना सोचे-समझे प्रशिक्षित किया जाता है, वह आम तौर पर उसी पूर्वाग्रह को पुनउत्पादित करेगी और कभी-कभी तीव्र करेगी, चाहे वह शुरू में कितना भी परिष्कृत या \'उद्देश्यपूर्ण\' क्यों न दिखाई दे।''',
  gujaratiText: '''જ્યારે બહુરાષ્ટ્રીય ટેકનોલોજી ફર્મે તેની સ્વચાલિત ભરતી પ્રણાલીને પ્રથમવાર રજૂ કરી, જેને કોઈપણ માનવ ભરતી ટીમ કરતાં ઘણી ઝડપથી હજારો નોકરીની અરજીઓનું સ્ક્રિનિંગ કરવા માટે ડિઝાઇન કરવામાં આવી હતી, ત્યારે અધિકારીઓએ આત્મવિશ્વાસપૂર્વક તેને નિષ્पक्षताની જીત તરીકે રજૂ કરી, એક એવું સાધન જે પરંપરાગત ભરતી પ્રક્રિયાઓને લાંબા સમયથી પરેશાન કરતા અચેતન માનવીય પૂર્વગ્રહોથી કથિત રીતે મુક્ત હતું. જો કે, અਠાર મહિનાની અંદર, એક આંતરિક ઓડિટે ખૂબ જ ચિંતાજનક પેટર્ન બહાર પાડી: આ સિસ્ટમ ટેકનિકલ ભૂમિકાઓ માટે સમાન રીતે લાયક પુરૂષ ઉમેદવારોની સરખામણીમાં સ્ત્રી ઉમેદવારોને પદ્ધતિસર નીચો ક્રમ આપી રહી હતી.

તપાસ કરી રહેલા ઇજનેરોએ આખરે આ સમસ્યાનું કારણ જાણી જોઈને પ્રોગ્રામ કરેલા પૂર્વગ્રહને બદલે તેના તાલીમ ડેટામાં શોધી કાઢ્યું. ટેકનોલોજી ઉદ્યોગના ઐતિહાસિક લિંગ અસંતુલનને કારણે પુરૂષ કર્મચારીઓનું ભારે વર્ચસ્વ ધરાવતા કંપનીના પાછલા દાયકાની સફળ નિમણૂકોના ડેટાસેટનું વિશ્લેષણ કરીને આલ્ગોરિધમે તેના મૂલ્યાંકન માપદંડો શીખ્યા હતા. આ અસંતુલનને સુધારવાને બદલે, સિસ્ટમે અસરકારક રીતે \'પુરુષ હોવાપણા\' ને જ ભરતીની સફળતાના સૂક્ષ્મ સંકેત તરીકે ગણવાનું શીખી લીધું હતું, અને મહિલાઓના ટેકનિકલ ક્લબ્સ અથવા ફક્ત મહિલાઓની કોલેજોમાં ભાગીદારીનો ઉલ્લેખ કરતા રિઝ્યુમ્સને પણ દંડિત કરી રહી હતી.

આ કેસ, એકવાર જાહેર થયા પછી, ટેકનોલોજીવિદો અને નીતિશાસ્ત્રીઓ વચ્ચે એક સરળ જણાતા પ્રશ્ન પર ભારે ચર્ચા જગાવી: શું ભેદભાવ કરવાનો કોઈ પણ અચેતન ઈરાદો ન ધરાવતું મશીન હજુ પણ પક્ષપાતી માની શકાય, અને જ્યારે તે અનિવાર્યપણે પક્ષપાતી બન્યું ત્યારે વાસ્તવિક જવાબદારી કોની હતી? કેટલાક ઇજનેરોએ દલીલ કરી કે દોષ આલ્ગોરિધમની પોતાની ડિઝાઇનને બદલે વાસ્તવિક ભૂતકાળની અસમાનતાને પ્રતિબિંબિત કરતા ઐતિહાસિક ડેટાનો હતો, જ્યારે નીતિશાસ્ત્રીઓએ પ્રતિવાદ કર્યો કે મૂળ ઈરાદાને ધ્યાનમાં લીધા વિના બરાબર આ પ્રકારના પૂર્વગ્રહ માટે સખત પરીક્ષણ વગર આવી સિસ્ટમ તૈનાત કરવી એ જવાબદારીની ગંભીર નિષ્ફળતા દર્શાવે છે.

કંપનીએ આખરે સ્વચાલિત સિસ્ટમને બંધ કરી દીધી, અને આવા પેટર્નને પકડવા માટે ખાસ પ્રશિક્ષિત ફરજિયાત માનવ સમીક્ષા સાથે આલ્ગોરિધમિક સ્ક્રિનિંગને જોડતી હાઇબ્રિડ પ્રક્રિયા સાથે તેને બદલી દીધી. આ ઘટના ટેકનોલોજી એથિક્સ અભ્યાસક્રમોમાં વ્યાપકપણે ટાંકવામાં આવેલ કેસ સ્ટડી બની ગઈ, જે એવી દુનિયામાં વધુને વધુ સુસંગત સિદ્ધાંત દર્શાવે છે જ્યાં નિર્ણાયક નિર્ણયોનું માર્ગદર્શન કરવા માટે આલ્ગોરિધમ્સ પર વિશ્વાસ કરવામાં આવે છે: પક્ષપાતી ઐતિહાસિક પેટર્ન પર અવिवेકી રીતે પ્રશિક્ષિત સિસ્ટમ સામાન્ય રીતે તે જ પૂર્વગ્રહને પુનઃઉત્પાદિત કરશે અને ક્યારેક તીવ્ર બનાવશે, ભલે તે શરૂઆતમાં ગમે તેટલી परिष्કૃત અથવા \'ઉદ્દેશ્યપૂર્ણ\' દેખાય.''',
  hindiSummary:
      'यह कहानी एक बड़ी टेक्नोलॉजी कंपनी की है, जिसका स्वचालित भर्ती सिस्टम धीरे-धीरे महिला उम्मीदवारों के साथ भेदभाव '
      'करने लगता है। जाँच से पता चलता है कि यह पुराने आँकड़ों से सीखा गया पूर्वाग्रह था, जानबूझकर नहीं। इससे यह बहस '
      'छिड़ती है कि मशीन की गलती के लिए ज़िम्मेदार कौन है। कंपनी अंततः इंसानी समीक्षा को भी शामिल करती है। यह कहानी '
      'तकनीक और नैतिकता के महत्वपूर्ण सवालों को उठाती है।',
  gujaratiSummary:
      'આ વાર્તા એક મોટી ટેક્નોલોજી કંપનીની છે, જેની સ્વચાલિત ભરતી સિસ્ટમ ધીમે ધીમે મહિલા ઉમેદવારો સાથે ભેદભાવ કરવા લાગે છે. તપાસમાં જાણવા મળે છે કે આ જૂના ડેટામાંથી શીખેલો પૂર્વગ્રહ હતો, જાણીજોઈને કરેલો નહીં. તેનાથી એ ચર્ચા શરૂ થાય છે કે મશીનની ભૂલ માટે કોણ જવાબદાર છે. કંપની અંતે માનવીય સમીક્ષાનો પણ સમાવેશ કરે છે. આ વાર્તા ટેક્નોલોજી અને નૈતિકતાના મહત્વના પ્રશ્નો ઉઠાવે છે.',
  glosses: [
    InlineGloss(word: 'deployed', meaningHi: 'लागू किया', hiTransliteration: 'laagu kiya'),
    InlineGloss(word: 'unconscious biases', meaningHi: 'अचेतन पूर्वाग्रह', hiTransliteration: 'achetan poorvaagrah'),
    InlineGloss(word: 'audit', meaningHi: 'लेखा-जोखा / जाँच', hiTransliteration: 'lekha-jokha / jaanch'),
    InlineGloss(word: 'training data', meaningHi: 'प्रशिक्षण डेटा', hiTransliteration: 'prashikshan data'),
    InlineGloss(word: 'discriminate', meaningHi: 'भेदभाव करना', hiTransliteration: 'bhedbhaav karna'),
    InlineGloss(word: 'ethicists', meaningHi: 'नैतिकता के विशेषज्ञ', hiTransliteration: 'naitikta ke visheshagya'),
    InlineGloss(word: 'hybrid', meaningHi: 'मिश्रित (दो प्रकार का संयोजन)', hiTransliteration: 'mishrit (do prakaar ka sanyojan)'),
    InlineGloss(word: 'sophisticated', meaningHi: 'उन्नत / जटिल', hiTransliteration: 'unnat / jatil'),
  ],
);
