import '../models/chapter.dart';

/// Draft chapter — written to match typical Class 9 English-medium reader
/// style and difficulty, not copied from an actual GSEB/CBSE textbook.
const chapterClass9Startup = Chapter(
  id: 'chapter_class9_startup',
  title: 'The App That Almost Wasn\'t',
  grade: 'Class 9',
  emoji: '💻',
  chapterText:
      'Sameer and his cousin Isha had spent nearly the entire summer building a mobile application intended to '
      'connect local farmers directly with small grocery stores, cutting out the layers of middlemen that '
      'typically reduced farmers\' profits while inflating prices for shopkeepers. Their working prototype '
      'performed reasonably well during testing, and both were confident enough to submit it to a prestigious '
      'national school innovation competition, certain their idea addressed a genuinely important problem.\n\n'
      'The rejection email, when it arrived, was almost clinically brief: their submission had not advanced '
      'past the preliminary round, with feedback noting that similar applications already existed commercially '
      'and that judges found insufficient evidence the app solved problems existing solutions had not already '
      'addressed. Isha wanted to abandon the project entirely, arguing that competing against established '
      'companies was clearly pointless for two school students working with borrowed laptops and no funding.\n\n'
      'Sameer, however, insisted on requesting detailed feedback before giving up completely, eventually '
      'learning that existing apps, while technically similar, largely ignored farmers in remote areas with '
      'unreliable internet connectivity, a gap their own research had actually uncovered but failed to '
      'emphasise clearly in their submission. Rather than abandoning their work, they spent the following month '
      'redesigning the app specifically around offline functionality, allowing farmers to log produce and '
      'prices even without a stable connection, syncing automatically whenever signal became available.\n\n'
      'When a regional agricultural technology fair invited school innovators to present projects six months '
      'later, Sameer and Isha\'s redesigned app, now explicitly targeting connectivity-poor farming '
      'communities, won recognition from an actual agricultural cooperative interested in piloting it. Isha '
      'later admitted that the original rejection, which had once felt like proof they should quit, turned out '
      'to be the exact information they needed to build something genuinely useful instead of merely similar '
      'to what already existed.',
  hindiText: '''समीर और उसकी चचेरी बहन ईशा ने लगभग पूरी गर्मियाँ एक ऐसा मोबाइल एप्लिकेशन बनाने में बिताई थीं, जिसका उद्देश्य स्थानीय किसानों को सीधे छोटे किराना स्टोर से जोड़ना था। इससे बिचौलियों की वे परतें खत्म हो जाती थीं, जो आमतौर पर किसानों का मुनाफा कम करती थीं और दुकानदारों के लिए कीमतें बढ़ा देती थीं। परीक्षण के दौरान उनका काम करने वाला प्रोटोटाइप काफी अच्छा रहा और दोनों को एक प्रतिष्ठित राष्ट्रीय स्कूल नवाचार प्रतियोगिता में इसे भेजने का पूरा भरोसा था, क्योंकि उन्हें यकीन था कि उनका विचार एक वाकई महत्वपूर्ण समस्या का समाधान करता है।

अस्वीकृति का ईमेल जब आया, तो वह बेहद संक्षिप्त था: उनका आवेदन प्रारंभिक दौर से आगे नहीं बढ़ पाया था और फीडबैक में यह कहा गया था कि इस तरह के ऐप व्यावसायिक रूप से पहले से ही मौजूद हैं और जजों को इस बात के पर्याप्त सबूत नहीं मिले कि यह ऐप ऐसी समस्याओं का समाधान करता है जिनका समाधान पहले से मौजूद समाधानों ने नहीं किया है। ईशा इस प्रोजेक्ट को पूरी तरह से छोड़ने चाहती थी, उसका तर्क था कि उधार के लैपटॉप और बिना किसी फंड के काम करने वाले दो स्कूली छात्रों के लिए स्थापित कंपनियों के खिलाफ मुकाबला करना स्पष्ट रूप से व्यर्थ है।

हालाँकि, समीर ने पूरी तरह से हार मानने से पहले विस्तृत फीडबैक मांगने पर जोर दिया। आखिरकार उसे पता चला कि मौजूदा ऐप, तकनीकी रूप से समान होने के बावजूद, कमज़ोर इंटरनेट कनेक्टिविटी वाले दूरदराज के क्षेत्रों के किसानों को बड़े पैमाने पर नजरअंदाज कर रहे थे। यह एक ऐसा अंतर था जिसे उनके अपने शोध ने खोजा था लेकिन वे अपने आवेदन में इसे स्पष्ट रूप से उजागर करने में असफल रहे थे। अपने काम को छोड़ने के बजाय, उन्होंने अगले महीने ऐप को विशेष रूप से ऑफलाइन काम करने के लिए फिर से डिज़ाइन किया, जिससे किसानों को स्थिर कनेक्शन न होने पर भी उपज और कीमतों को दर्ज करने की अनुमति मिल गई, और सिग्नल मिलते ही डेटा अपने आप सिंक हो जाता था।

जब छह महीने बाद एक क्षेत्रीय कृषि प्रौद्योगिकी मेले ने स्कूली नवप्रवर्तकों को अपनी परियोजनाएं प्रस्तुत करने के लिए आमंत्रित किया, तो समीर और ईशा का नया रूप दिया गया ऐप, जो अब विशेष रूप से कम कनेक्टिविटी वाले कृषक समुदायों को लक्षित कर रहा था, उसे एक वास्तविक कृषि सहकारी समिति से मान्यता मिली जो इसका परीक्षण करने में रुचि रखती थी। ईशा ने बाद में स्वीकार किया कि वह शुरुआती अस्वीकृति, जो कभी इस बात का प्रमाण लगी थी कि उन्हें हार मान लेना चाहिए, वास्तव में वह सटीक जानकारी साबित हुई जिसकी उन्हें केवल पहले से मौजूद चीज़ों जैसा बनाने के बजाय कुछ वाकई उपयोगी बनाने के लिए आवश्यकता थी।''',
  gujaratiText: '''સमीर અને તેની પિત્રાઈ બહેન ઈશાએ લગભગ આખો ઉનાળો એક એવી મોબાઈલ એપ્લિકેશન બનાવવામાં વિતાવ્યો હતો, જેનો હેતુ સ્થાનિક ખેડૂતોને સીધા જ નાની કરિયાણાની દુકાનો સાથે જોડવાનો હતો, જેનાથી વચેટિયાઓની એ કડીઓ નીકળી જાય જે સામાન્ય રીતે ખેડૂતોના નફાને ઘટાડતી હતી અને દુકાનદારો માટે ભાવ વધારતી હતી. પરીક્ષણ દરમિયાન તેમનું કાર્યશીલ પ્રોટોટાઇપ ખૂબ જ સારું રહ્યું અને બંનેને પ્રતિષ્ઠિત રાષ્ટ્રીય શાળા નવીનતા સ્પર્ધામાં તેને સબમિટ કરવાનો પૂરો વિશ્વાસ હતો, કારણ કે તેઓ ચોક્કસ હતા કે તેમનો વિચાર ખરેખર એક મહત્વપૂર્ણ સમસ્યાનું સમાધાન કરે છે.

જ્યારે અસ્વીકારનો ઇમેઇલ આવ્યો, ત્યારે તે ખૂબ જ ટૂંકો હતો: તેમની એન્ટ્રી પ્રારંભિક રાઉન્ડથી આગળ વધી શકી ન હતી, અને પ્રતિસાદમાં એવું નોંધવામાં આવ્યું હતું કે સમાન એપ્લિકેશનો વ્યવસાયિક રીતે પહેલેથી જ અસ્તિત્વમાં છે અને ન્યાયાધીશોને પૂરતા પુરાવા મળ્યા નથી કે આ એપ્લિકેશને એવી સમસ્યાઓ હલ કરી છે જે અગાઉના ઉકેલો દ્વારા હલ કરવામાં આવી ન હતી. ઈશા આ પ્રોજેક્ટને સંપૂર્ણપણે છોડી દેવા માંગતી હતી, તેનો તર્ક હતો કે ઉછીના લેપટોપ અને કોઈ ભંડોળ વગર કામ કરતા બે શાળાના વિદ્યાર્થીઓ માટે સ્થાપિત કંપનીઓ સામે સ્પર્ધા કરવી સ્પષ્ટપણે વ્યર્થ છે.

જોકે, સવારે સંપૂર્ણપણે હાર માનતા પહેલા વિગતવાર પ્રતિસાદ માંગવાનો આગ્રહ રાખ્યો, અને અંતે જાણવા મળ્યું કે હાલની એપ્લિકેશનો, તકનીકી રીતે સમાન હોવા છતાં, અવ્યવસ્થિત ઇન્ટરનેટ કનેક્ટિવિટી ધરાવતા દૂરના વિસ્તારોના ખેડૂતોની મોટાભાગે અવગણના કરતી હતી, જે એક એવી ખામી હતી જે તેમના પોતાના સંશોધને શોધી કાઢી હતી પરંતુ તેઓ તેમની સબમિશનમાં તેને સ્પષ્ટપણે દર્શાવવામાં નિષ્ફળ ગયા હતા. તેમના કામને છોડી દેવાને બદલે, તેઓએ આગામી મહિને એપ્લિકેશንን ખાસ કરીને ઓફલાઇન કાર્યક્ષમતાની આસપાસ ફરીથી ડિઝાઇન કરવામાં વિતાવ્યો, જેનાથી ખેડૂતોને સ્થિર કનેક્શન ન હોય ત્યારે પણ પાક અને કિંમતો લોગ કરવાની મંજૂરી મળી, અને સિગ્નલ ઉપલબ્ધ થતાં જ તે આપમેળે સિન્ક થઈ જતું હતું.

જ્યારે છ મહિના પછી એક પ્રાદેશિક કૃષિ તકનીકી મેળાએ શાળાના ઇનોવેટર્સને પ્રોજેક્ટ્સ રજૂ કરવા આમંત્રિત કર્યા, ત્યારે સમીર અને ઈશાની ફરીથી ડિઝાઇન કરાયેલ એપ્લિકેશન, જે હવે ખાસ કરીને કનેક્ટિવિટી-નબળા કૃષિ સમુદાયોને લક્ષ્ય બનાવી રહી હતી, તેને વાસ્તવિક કૃષિ સહકારી સંસ્થા તરફથી માન્યતા મળી જે તેનું પાયલોટિંગ કરવામાં રસ ધરાવતી હતી. ઈશાએ પાછળથી સ્વીકાર્યું કે મૂળ અસ્વીકાર, જે એક સમયે એ વાતનો પુરાવો લાગતો હતો કે તેમણે હાર માનવી જોઈએ, તે બરાબર એ જ માહિતી સાબિત થઈ જે તેમને પહેલેથી અસ્તિત્વમાં છે તેના જેવું જ કંઈક બનાવવાને બદલે ખરેખર ઉપયોગી બને તેવી ચીજ વિકસાવવા માટે જરૂરી હતી.''',
  hindiSummary:
      'यह कहानी समीर और उसकी चचेरी बहन ईशा की है, जो किसानों और दुकानदारों को सीधे जोड़ने वाला एक ऐप बनाते हैं, लेकिन '
      'एक प्रतियोगिता में उनका आवेदन अस्वीकार हो जाता है। समीर हार नहीं मानता और प्रतिक्रिया माँगता है, जिससे पता चलता है '
      'कि दूरदराज़ के किसानों के लिए ऑफलाइन सुविधा ज़रूरी है। वे ऐप में सुधार करते हैं और अंततः पहचान पाते हैं। यह कहानी '
      'असफलता से सीखने के महत्व को दर्शाती है।',
  gujaratiSummary:
      'આ વાર્તા સમીર અને તેની પિતરાઈ બહેન ઈશાની છે, જેઓ ખેડૂતો અને દુકાનદારોને સીધા જોડવા માટે એક એપ બનાવે છે, પરંતુ એક સ્પર્ધામાં તેમની અરજી નકારી કાઢવામાં આવે છે. સમીર હાર માનતો નથી અને પ્રતિસાદ માંગે છે, જેનાથી ખબર પડે છે કે દૂરના વિસ્તારોના ખેડૂતો માટે ઓફલાઈન સુવિધા જરૂરી છે. તેઓ એપમાં સુધારો કરે છે અને અંતે ઓળખ મેળવે છે. આ વાર્તા નિષ્ફળતામાંથી શીખવાના મહત્વને દર્શાવે છે.',
  glosses: [
    InlineGloss(word: 'prototype', meaningHi: 'आरंभिक नमूना', hiTransliteration: 'aarambhik namoona'),
    InlineGloss(word: 'clinically', meaningHi: 'बिना भावना के / सीधे तरीके से', hiTransliteration: 'bina bhaavna ke / seedhe tarike se'),
    InlineGloss(word: 'preliminary round', meaningHi: 'प्रारंभिक चरण', hiTransliteration: 'praarambhik charan'),
    InlineGloss(word: 'connectivity', meaningHi: 'संपर्क सुविधा (इंटरनेट)', hiTransliteration: 'sampark suvidha (internet)'),
    InlineGloss(word: 'syncing', meaningHi: 'डेटा को स्वतः मिलाना', hiTransliteration: 'data ko swatah milaana'),
    InlineGloss(word: 'cooperative', meaningHi: 'सहकारी समिति', hiTransliteration: 'sahkaari samiti'),
  ],
);
