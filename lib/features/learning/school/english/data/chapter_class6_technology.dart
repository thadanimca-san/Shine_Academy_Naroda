import '../models/chapter.dart';

/// Draft chapter — written to match typical Class 6 English-medium reader
/// style and difficulty, not copied from an actual GSEB/CBSE textbook.
const chapterClass6Technology = Chapter(
  id: 'chapter_class6_technology',
  title: 'The Drone That Found the Leak',
  grade: 'Class 6',
  emoji: '🛰️',
  chapterText:
      'Naina\'s father managed the water supply network for their small industrial town, a tangled system of '
      'underground pipes stretching for kilometres beneath the streets. For months, the municipal office had '
      'noticed that large amounts of water were disappearing somewhere between the reservoir and the taps, yet no '
      'worker sent to dig along the suspected route could locate the actual leak. Every excavation cost time and '
      'money, and residents were growing impatient with the rationed water supply that resulted from the shortage.\n\n'
      'Naina, who had recently joined her school\'s robotics club, suggested an unusual idea during dinner: why not '
      'use a small thermal-imaging drone, similar to the one her club had built for a competition, to scan the '
      'ground from above? Leaking water, she explained, often cooled or heated the soil above a pipe in a pattern '
      'invisible to the naked eye but detectable through a thermal camera. Her father was doubtful that a school '
      'project could succeed where trained engineers had failed, but with no better options remaining, he agreed to '
      'let her try over a weekend.\n\n'
      'Naina and her robotics club spent two days calibrating the drone\'s camera and mapping out a grid over the '
      'suspected stretch of pipeline. The first flight revealed nothing unusual, and Naina worried that her theory '
      'had been wrong all along. On the second flight, flown early in the morning when temperature differences were '
      'sharpest, the thermal images showed a faint, elongated patch of unusually cool soil running diagonally across '
      'a field that no one had considered part of the pipeline\'s route, since old municipal maps showed the pipe '
      'running elsewhere entirely.\n\n'
      'When engineers dug carefully at the exact spot Naina\'s drone had identified, they discovered a forgotten '
      'branch pipe, installed decades earlier and left off newer maps, cracked along a joint and leaking steadily '
      'into the soil. Repairing it restored nearly a third of the town\'s lost water supply within a single week. '
      'The municipal office later invited Naina to demonstrate her method to engineers from neighbouring towns, and '
      'her father, once skeptical, proudly admitted that sometimes the newest technology, placed in curious young '
      'hands, could solve problems that years of traditional methods had failed to fix.',
  hindiText: '''शाइन एकेडमी नारोडा के हमारे युवा छात्रों के लिए अनुवाद:

नैना के पिता अपने छोटे से औद्योगिक शहर के जल आपूर्ति नेटवर्क को संभालते थे, जो सड़कों के नीचे किलोमीटरों तक फैले हुए भूमिगत पाइपों का एक उलझा हुआ जाल था। महीनों से नगर पालिका कार्यालय ने ध्यान दिया था कि जलाशय और नलों के बीच कहीं बड़ी मात्रा में पानी गायब हो रहा है, फिर भी संदिग्ध मार्ग के साथ खुदाई के लिए भेजे गए किसी भी कर्मचारी को वास्तविक रिसाव का पता नहीं चल रहा था। हर खुदाई में समय और पैसा खर्च होता था, और इस कमी के परिणामस्वरूप मिलने वाली राशन वाली पानी की आपूर्ति से निवासी अधीर हो रहे थे।

नैना, जो हाल ही में अपने स्कूल के रोबोटिक्स क्लब में शामिल हुई थी, ने रात के खाने के दौरान एक अजीब सा विचार सुझाया: क्यों न ऊपर से जमीन को स्कैन करने के लिए एक छोटे थर्मल-इमेजिजिंग ड्रोन का उपयोग किया जाए, जो उसके क्लब ने प्रतियोगिता के लिए बनाए गए ड्रोन जैसा ही हो? उसने समझाया कि बहता हुआ पानी अक्सर पाइप के ऊपर की मिट्टी को ऐसे पैटर्न में ठंडा या गर्म कर देता है जो नग्न आंखों से दिखाई नहीं देता लेकिन थर्मल कैमरे से पता लगाया जा सकता है। उसके पिता को संदेह था कि कोई स्कूली प्रोजेक्ट वहां सफल हो सकता है जहां प्रशिक्षित इंजीनियर असफल हो गए थे, लेकिन कोई बेहतर विकल्प न होने के कारण, उन्होंने उसे एक सप्ताहांत में कोशिश करने की अनुमति दे दी।

नैना और उसके रोबोटिक्स क्लब ने ड्रोन के कैमरे को कैलिब्रेट करने और पाइपलाइन के संदिग्ध हिस्से पर एक ग्रिड तैयार करने में दो दिन बिताए। पहली उड़ान में कुछ भी असामान्य नहीं दिखा, और नैना को चिंता हुई कि उसका सिद्धांत शुरू से ही गलत था। दूसरी उड़ान में, जो सुबह-सुबह उड़ाई गई थी जब तापमान का अंतर सबसे तेज था, थर्मल छवियों से असामान्य रूप से ठंडी मिट्टी का एक धुंधला, लंबा पैच दिखाई दिया जो एक ऐसे खेत के पार तिरछे रूप से चल रहा था जिसे किसी ने पाइपलाइन के मार्ग का हिस्सा नहीं माना था, क्योंकि पुराने नगरपालिका नक्शे दिखाते थे कि पाइप पूरी तरह से कहीं और से गुजर रहा था।

जब इंजीनियरों ने नैना के ड्रोन द्वारा पहचानी गई सटीक जगह पर सावधानी से खुदाई की, तो उन्होंने एक भूली हुई शाखा पाइप की खोज की, जिसे दशकों पहले स्थापित किया गया था और नए नक्शों से हटा दिया गया था, जो एक जोड़ पर दरार खा गई थी और मिट्टी में लगातार रिस रही थी। इसे ठीक करने से एक सप्ताह के भीतर शहर की खोई हुई पानी की आपूर्ति का लगभग एक तिहाई हिस्सा बहाल हो गया। नगर पालिका कार्यालय ने बाद में नैना को पड़ोसी शहरों के इंजीनियरों को अपनी पद्धति का प्रदर्शन करने के लिए आमंत्रित किया, और उसके पिता ने, जो कभी संकोच कर रहे थे, गर्व से स्वीकार किया कि कभी-कभी सबसे नई तकनीक, जिज्ञासु युवा हाथों में दिए जाने पर, उन समस्याओं को हल कर सकती है जिन्हें पारंपरिक तरीकों के वर्षों हल करने में असफल रहे थे।''',
  gujaratiText: '''शाइन एकेडमी नरोडाના અમારા યુવાન વિદ્યાર્થીઓ માટે અનુવાદ:

નૈનાના પિતા તેમના નાના ઔદ્યોગિક શહેર માટે પાણી પુરવઠા નેટવર્ક સંભાળતા હતા, જે રસ્તાઓ નીચે કિલોમીટરો સુધી ફેલાયેલી ભૂગર્ભ પાઈપોની એક ગૂંચવાયેલી સિસ્ટમ હતી. મહિનાઓથી, મ્યુનિસિપલ કચેરીએ નોંધ્યું હતું કે જળાશય અને નળ વચ્ચે ક્યાંક પાણીનો મોટો જથ્થો ગાયબ થઈ રહ્યો છે, છતાં શંકાસ્પદ માર્ગ પર ખોદકામ કરવા માટે મોકલાયેલ કોઈ પણ કામદાર વાસ્તવિક લીકેજ શોધી શક્યો ન હતો. દરેક ખોદકામમાં સમય અને પૈસા ખર્ચ થતા હતા, અને આ અછતના પરિણામે મળતા રેસનવાળા પાણીના પુરવઠાથી રહેવાસીઓ અધીરા થઈ રહ્યા હતા.

નૈના, જે તાજેતરમાં જ તેની શાળાના રોબોટિક્સ ક્લબમાં જોડાઈ હતી, તેણે રાત્રિભोजन દરમિયાન એક અસામાન્ય વિચાર સૂચવ્યો: શા માટે ઉપરથી જમીનને સ્કેન કરવા માટે નાના થર્મલ-ઇમેજિંગ ડ્રોનનો ઉપયોગ ન કરવામાં આવે, જે તેના ક્લબે સ્પર્ધા માટે બનાવ્યો હતો તેના જેવું જ? તેણે સમજાવ્યું કે લીક થતું પાણી ઘણીવાર પાઈપની ઉપરની માટીને એવા પેટર્નમાં ઠંડુ કે ગરમ કરે છે જે નરી આંખે દેખાતું નથી પરંતુ થર્મલ કેમેરા દ્વારા શોધી શકાય છે. તેના પિતાને શંકા હતી કે શાળાનો કોઈ પ્રોજેક્ટ ત્યાં સફળ થઈ શકે છે જ્યાં પ્રશિક્ષિત ઇજનેરો નિષ્ફળ ગયા હતા, પરંતુ કોઈ સારો વિકલ્પ બાકી ન હોવાથી, તેણે તેને સપ્તાહના અંતે પ્રયાસ કરવાની મંજૂરી આપી.

નૈના અને તેની રોબોટિક્સ ક્લબે ડ્રોનના કેમેરાને કેલિબ્રેટ કરવામાં અને પાઇપલાઇનના શંકાસ્પદ ભાગ પર ગ્રીડ મેપિંગ કરવામાં બે દિવસ વિતાવ્યા. પહેલી ઉડાનમાં કંઈ અસામાન્ય દેખાયું નહીં, અને નૈના ચિંતિત થઈ કે તેનો સિદ્ધાંત શરૂઆતથી જ ખોટો હતો. બીજી ઉડાનમાં, જે વહેલી સવારે ઉડાડવામાં આવી હતી જ્યારે તાપમાનનો તફાવત સૌથી તીક્ષ્ણ હતો, થર્મલ છબીઓ દ્વારા અસામાન્ય રીતે ઠંડી માટીનો એક ઝાંખો, લાંબો પેચ જોવા મળ્યો જે એક ખેતરની આડમાં ત્રાંસા રૂપે ચાલી રહ્યો હતો જેને કોઈએ પાઇપલાઇનના માર્ગનો ભાગ ગણ્યો ન હતો, કારણ કે જૂના મ્યુનિસિપલ નશાઓ દર્શાવતા હતા કે પાઇપ સંપૂર્ણપણે ક્યાંક બીજેથી પસાર થતી હતી.

જ્યારે ઇજનેરોએ નૈનાના ડ્રોન દ્વારા ઓળખવામાં આવેલી ચોક્કસ જગ્યા પર કાળજીપૂર્વક ખોદકામ કર્યું, ત્યારે તેમને દાયકાઓ પહેલાં સ્થાપિત અને નવા નકશામાંથી છોડી દેવાયેલી એક ભુલાઈ ગયેલી બ્રાન્ચ પાઇપ મળી, જે સાંધા પર તિરાડ પડી ગઈ હતી અને જમીનમાં સતત લીક થઈ રહી હતી. તેને સુધારવાથી એક અઠવાડિયાની અંદર શહેરના ખોવાયેલા પાણી પુરવઠાનો લગભગ ત્રીજા ભાગનો હિસ્સો પુનઃસ્થાપિત થયો. મ્યુનિસિપલ કચેરીએ પછીથી નૈનાને નજીકના શહેરોના ઇજનેરો સમક્ષ તેની પદ્ધતિનું પ્રદર્શન કરવા માટે આમંત્રણ આપ્યું, અને તેના પિતાએ, જેઓ એકવાર શંકાશીલ હતા, ગર્વથી સ્વીકાર્યું કે ક્યારેક નવીનતમ તકનીક, જિજ્ઞાસુ યુવાન હાથોમાં મૂકવામાં આવે ત્યારે, એવી સમસ્યાઓ હલ કરી શકે છે જે વર્ષોની પરંપરાગત પદ્ધતિઓ હલ કરવામાં નિષ્ફળ રહી હતી.''',
  hindiSummary:
      'यह कहानी नैना की है, जिसके पिता शहर के पानी की आपूर्ति व्यवस्था संभालते हैं। पाइपलाइन में कहीं पानी लीक हो रहा था, जिसे इंजीनियर '
      'ढूंढ नहीं पा रहे थे। नैना अपने रोबोटिक्स क्लब के थर्मल-इमेजिंग ड्रोन का उपयोग करने का सुझाव देती है, क्योंकि लीक होता पानी मिट्टी के '
      'तापमान को बदल देता है। दूसरी उड़ान में ड्रोन एक भूली हुई पुरानी पाइप का पता लगाता है जो नक़्शों में नहीं थी। इंजीनियर उसे ठीक करते हैं '
      'और शहर का बहुत सारा पानी बचता है। यह कहानी दिखाती है कि नई तकनीक और जिज्ञासा पुरानी समस्याओं को भी हल कर सकती है।',
  gujaratiSummary:
      'આ નૈનાની વાર્તા છે, જેના પિતા શહેરની પાણી પુરવઠા વ્યવસ્થાનું સંચાલન કરે છે. પાઈપલાઈનમાં ક્યાંક પાણી લીક થઈ રહ્યું હતું, જેને શોધી કાઢવામાં એન્જિનિયરો અસમર્થ હતા. નૈના તેના રોબોટિક્સ ક્લબના થર્મલ-ઇમેજિંગ ડ્રોનનો ઉપયોગ કરવાનું સૂચન કરે છે, કારણ કે પાણી લીક થવાથી જમીનનું તાપમાન બદલાય છે. બીજી ફ્લાઇટમાં ડ્રોનને એક ભૂલી ગયેલી જૂની પાઇપ મળે છે જે નકશા પર ન હતી. ઇજનેરો તેને ઠીક કરે છે અને શહેરમાં પાણીની ઘણી બચત થાય છે. આ વાર્તા બતાવે છે કે નવી ટેક્નોલોજી અને જિજ્ઞાસા જૂની સમસ્યાઓ પણ ઉકેલી શકે છે.',
  glosses: [
    InlineGloss(word: 'reservoir', meaningHi: 'जलाशय', hiTransliteration: 'jalashay', meaningGu: 'જળાશય', guTransliteration: 'jalashay'),
    InlineGloss(word: 'excavation', meaningHi: 'खुदाई', hiTransliteration: 'khudai', meaningGu: 'ખોદવું', guTransliteration: 'khudai'),
    InlineGloss(word: 'thermal-imaging', meaningHi: 'ताप-चित्रण (गर्मी से चित्र बनाने वाला)', hiTransliteration: 'taap-chitran', meaningGu: 'થર્મલ ઇમેજિંગ', guTransliteration: 'taap-chitran'),
    InlineGloss(word: 'calibrating', meaningHi: 'सही सेटिंग करना', hiTransliteration: 'sahi setting karna', meaningGu: 'તેને બરાબર સેટ કરો', guTransliteration: 'sahi setting karna'),
    InlineGloss(word: 'elongated', meaningHi: 'लंबा फैला हुआ', hiTransliteration: 'lamba faila hua', meaningGu: 'લાંબો ફેલાવો', guTransliteration: 'lamba faila hua'),
    InlineGloss(word: 'diagonally', meaningHi: 'तिरछे तरीके से', hiTransliteration: 'tirchhe tareeke se', meaningGu: 'ત્રાંસી રીતે', guTransliteration: 'tirchhe tareeke se'),
    InlineGloss(word: 'municipal', meaningHi: 'नगरपालिका संबंधी', hiTransliteration: 'nagarpalika sambandhi', meaningGu: 'મ્યુનિસિપલ સંબંધિત', guTransliteration: 'nagarpalika sambandhi'),
    InlineGloss(word: 'skeptical', meaningHi: 'संदेह करने वाला', hiTransliteration: 'sandeh karne wala', meaningGu: 'શંકાસ્પદ', guTransliteration: 'sandeh karne wala'),
    InlineGloss(word: 'rationed', meaningHi: 'सीमित मात्रा में बाँटा गया', hiTransliteration: 'seemit matra mein baanta gaya', meaningGu: 'મર્યાદિત માત્રામાં વિતરિત', guTransliteration: 'seemit matra mein baanta gaya'),
    InlineGloss(word: 'restored', meaningHi: 'फिर से बहाल किया', hiTransliteration: 'phir se bahaal kiya', meaningGu: 'ફરીથી પુનઃસ્થાપિત', guTransliteration: 'phir se bahaal kiya'),
    InlineGloss(word: 'grid', meaningHi: 'खानों वाला नक़्शा', hiTransliteration: 'khaanon wala naksha', meaningGu: 'ખાણ નકશો', guTransliteration: 'khaanon wala naksha'),
    InlineGloss(word: 'joint', meaningHi: 'जोड़', hiTransliteration: 'jod', meaningGu: 'સંયુક્ત', guTransliteration: 'jod'),
  ],
);
