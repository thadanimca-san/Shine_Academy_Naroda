import json

blocks = []

def b(type_val, **kwargs):
    d = {"type": type_val}
    d.update(kwargs)
    blocks.append(d)

# METADATA
b("chapter_title", 
  title="The Mughal Empire", 
  title_hi="मुगल साम्राज्य", 
  title_gu="મુઘલ સામ્રાજ્ય", 
  id="KOBJ_CLAS7_SSCI_CH3_META_001")

# TOPIC 1: Foundation by Babur
b("hook", 
  title="The New Invaders", title_hi="नए आक्रमणकारी", title_gu="નવા આક્રમણકારો",
  body="Imagine being vastly outnumbered by an enemy army, but still winning because you brought something they had never seen before: cannons! This is exactly how the great Mughal Empire began in India.",
  body_hi="कल्पना करें कि दुश्मन सेना की संख्या आपसे बहुत अधिक है, लेकिन फिर भी आप जीत जाते हैं क्योंकि आप कुछ ऐसा लाए हैं जो उन्होंने पहले कभी नहीं देखा था: तोपें! बिल्कुल इसी तरह भारत में महान मुगल साम्राज्य की शुरुआत हुई थी।",
  body_gu="કલ્પના કરો કે દુશ્મન સૈન્યની સંખ્યા તમારા કરતા ઘણી વધારે છે, પરંતુ તેમ છતાં તમે જીતી જાઓ છો કારણ કે તમે કંઈક એવું લાવ્યા છો જે તેઓએ પહેલાં ક્યારેય જોયું ન હતું: તોપો! બરાબર આ રીતે ભારતમાં મહાન મુઘલ સામ્રાજ્યની શરૂઆત થઈ હતી.",
  id="KOBJ_CLAS7_SSCI_CH3_HOOK_001")

b("theory",
  title="Babur and The First Battle of Panipat", title_hi="बाबर और पानीपत की पहली लड़ाई", title_gu="બાબર અને પાણીપતનું પ્રથમ યુદ્ધ",
  body="Babur was the founder of the Mughal Empire in India. He established it after defeating the Sultan of Delhi, Ibrahim Lodi, in the First Battle of Panipat in 1526 A.D. Babur was a highly educated, deeply religious man, and a regular writer. He even wrote his famous autobiography called 'Tuzuk-e-Babri' (Babarnama).",
  body_hi="बाबर भारत में मुगल साम्राज्य का संस्थापक था। उसने 1526 ईस्वी में पानीपत की पहली लड़ाई में दिल्ली के सुल्तान इब्राहिम लोदी को हराने के बाद इसकी स्थापना की। बाबर एक उच्च शिक्षित, अत्यधिक धार्मिक व्यक्ति और नियमित लेखक था। उसने अपनी प्रसिद्ध आत्मकथा 'तुज़ुक-ए-बाबरी' (बाबरनामा) भी लिखी।",
  body_gu="બાબર ભારતમાં મુઘલ સામ્રાજ્યનો સ્થાપક હતો. તેણે 1526 એડીમાં પાણીપતના પ્રથમ યુદ્ધમાં દિલ્હીના સુલતાન ઇબ્રાહિમ લોદીને હરાવ્યા પછી તેની સ્થાપના કરી. બાબર અત્યંત શિક્ષિત, ઊંડા ધાર્મિક વ્યક્તિ અને નિયમિત લેખક હતો. તેણે પોતાની પ્રખ્યાત આત્મકથા 'તુઝુક-એ-બાબરી' (બાબરનામા) પણ લખી હતી.",
  id="KOBJ_CLAS7_SSCI_CH3_THEO_001")

# Ex Q1.1: Founder of Mughal Empire
b("mcq",
  question="Who was the founder of the Mughal Empire?",
  question_hi="मुगल साम्राज्य का संस्थापक कौन था?",
  question_gu="મુઘલ સામ્રાજ્યના સ્થાપક કોણ હતા?",
  options=["Akbar", "Humayun", "Babur", "Shah Jahan"],
  options_hi=["अकबर", "हुमायूँ", "बाबर", "शाहजहाँ"],
  options_gu=["અકબર", "હુમાયુ", "બાબર", "શાહજહાં"],
  correct_index=2,
  explanation="Babur was the founder of the Mughal Empire in India.",
  explanation_hi="बाबर भारत में मुगल साम्राज्य का संस्थापक था।",
  explanation_gu="બાબર ભારતમાં મુઘલ સામ્રાજ્યનો સ્થાપક હતો.",
  id="KOBJ_CLAS7_SSCI_CH3_MCQ_001")

# Ex Q1.2: First Battle of Panipat
b("mcq",
  question="Between whom was the First Battle of Panipat fought?",
  question_hi="पानीपत की पहली लड़ाई किसके बीच लड़ी गई थी?",
  question_gu="પાણીપતનું પ્રથમ યુદ્ધ કોની વચ્ચે લડાયું હતું?",
  options=["Akbar and Hemu", "Babur and Ibrahim Lodi", "Sher Shah and Humayun", "Shivaji and Aurangzeb"],
  options_hi=["अकबर और हेमू", "बाबर और इब्राहिम लोदी", "शेर शाह और हुमायूँ", "शिवाजी और औरंगजेब"],
  options_gu=["અકબર અને હેમુ", "બાબર અને ઇબ્રાહિમ લોદી", "શેર શાહ અને હુમાયુ", "શિવાજી અને ઔરંગઝેબ"],
  correct_index=1,
  explanation="The First Battle of Panipat (1526 A.D.) was fought between Babur and Ibrahim Lodi.",
  explanation_hi="पानीपत की पहली लड़ाई (1526 ईस्वी) बाबर और इब्राहिम लोदी के बीच लड़ी गई थी।",
  explanation_gu="પાણીપતનું પ્રથમ યુદ્ધ (1526 એડી) બાબર અને ઇબ્રાહિમ લોદી વચ્ચે લડાયું હતું.",
  id="KOBJ_CLAS7_SSCI_CH3_MCQ_002")

# Ex Q3.2: Babur autobiography
b("mcq",
  question="Which Mughal emperor was highly educated, deeply religious, and a regular writer (author of 'Tuzuk-e-Babri')?",
  question_hi="कौन सा मुगल सम्राट उच्च शिक्षित, अत्यधिक धार्मिक और नियमित लेखक ('तुज़ुक-ए-बाबरी' का लेखक) था?",
  question_gu="કયો મુઘલ સમ્રાટ અત્યંત શિક્ષિત, ઊંડો ધાર્મિક અને નિયમિત લેખક ('તુઝુક-એ-બાબરી' નો લેખક) હતો?",
  options=["Babur", "Akbar", "Aurangzeb", "Bahadur Shah"],
  options_hi=["बाबर", "अकबर", "औरंगजेब", "बहादुर शाह"],
  options_gu=["બાબર", "અકબર", "ઔરંગઝેબ", "બહાદુર શાહ"],
  correct_index=0,
  explanation="Babur was highly educated and wrote his autobiography, 'Tuzuk-e-Babri'.",
  explanation_hi="बाबर उच्च शिक्षित था और उसने अपनी आत्मकथा 'तुज़ुक-ए-बाबरी' लिखी थी।",
  explanation_gu="બાબર અત્યંત શિક્ષિત હતો અને તેણે પોતાની આત્મકથા 'તુઝુક-એ-બાબરી' લખી હતી.",
  id="KOBJ_CLAS7_SSCI_CH3_MCQ_003")

# TOPIC 2: Humayun and Sher Shah Suri
b("theory",
  title="Humayun and Sher Shah Suri", title_hi="हुमायूँ और शेर शाह सूरी", title_gu="હુમાયુ અને શેર શાહ સૂરી",
  body="After Babur, his son Humayun became the emperor. However, he faced a fierce rival named Sher Shah Suri. Sher Shah defeated Humayun in the battles of Chausa and Kannauj, forcing Humayun to flee. Sher Shah Suri became a great ruler and introduced massive reforms. He curbed dacoits for peace, introduced a new postal system, built rest houses (sarais) for travelers, constructed the famous Grand Trunk Road connecting Bengal and North India, and introduced a new uniform silver coin currency.",
  body_hi="बाबर के बाद उसका बेटा हुमायूँ सम्राट बना। हालाँकि, उसे शेर शाह सूरी नामक एक भयंकर प्रतिद्वंद्वी का सामना करना पड़ा। शेर शाह ने चौसा और कन्नौज के युद्धों में हुमायूँ को हराया, जिससे हुमायूँ को भागने पर मजबूर होना पड़ा। शेर शाह सूरी एक महान शासक बना और उसने बड़े पैमाने पर सुधार किए। उसने शांति के लिए डकैतों पर अंकुश लगाया, एक नई डाक प्रणाली शुरू की, यात्रियों के लिए सराय (विश्राम गृह) बनवाए, बंगाल और उत्तर भारत को जोड़ने वाली प्रसिद्ध ग्रांड ट्रंक रोड का निर्माण किया, और एक नई समान चांदी के सिक्के की मुद्रा पेश की।",
  body_gu="બાબર પછી તેનો પુત્ર હુમાયુ સમ્રાટ બન્યો. જોકે, તેને શેર શાહ સૂરી નામના ભયંકર હરીફનો સામનો કરવો પડ્યો. શેર શાહે ચૌસા અને કન્નૌજના યુદ્ધોમાં હુમાયુને હરાવ્યો, જેથી હુમાયુને ભાગવાની ફરજ પડી. શેર શાહ સૂરી એક મહાન શાસક બન્યો અને તેણે મોટા પાયે સુધારા કર્યા. તેણે શાંતિ માટે ડાકુઓ પર અંકુશ લગાવ્યો, નવી ટપાલ વ્યવસ્થા શરૂ કરી, મુસાફરો માટે સરાય (આરામગૃહ) બનાવ્યા, બંગાળ અને ઉત્તર ભારતને જોડતો પ્રખ્યાત ગ્રાન્ડ ટ્રંક રોડ બનાવ્યો, અને સમાન ચાંદીના સિક્કાનું નવું ચલણ રજૂ કર્યું.",
  id="KOBJ_CLAS7_SSCI_CH3_THEO_002")

# Ex Q3.1: Who defeated Humayun
b("mcq",
  question="Who defeated Humayun in the Battle of Chausa and Kannauj?",
  question_hi="चौसा और कन्नौज के युद्ध में हुमायूँ को किसने हराया था?",
  question_gu="ચૌસા અને કન્નૌજના યુદ્ધમાં હુમાયુને કોણે હરાવ્યો?",
  options=["Akbar", "Sher Shah Suri", "Jahangir", "Shah Jahan"],
  options_hi=["अकबर", "शेर शाह सूरी", "जहाँगीर", "शाहजहाँ"],
  options_gu=["અકબર", "શેર શાહ સૂરી", "જહાંગીર", "શાહજહાં"],
  correct_index=1,
  explanation="Sher Shah Suri defeated Humayun at Chausa and Kannauj.",
  explanation_hi="शेर शाह सूरी ने चौसा और कन्नौज में हुमायूँ को हराया था।",
  explanation_gu="શેર શાહ સૂરીએ ચૌસા અને કન્નૌજમાં હુમાયુને હરાવ્યો હતો.",
  id="KOBJ_CLAS7_SSCI_CH3_MCQ_004")

# Ex Q1.3: Sher Shah Suri reforms
b("mcq",
  question="Which of the following reforms was NOT introduced by Sher Shah Suri?",
  question_hi="निम्नलिखित में से कौन सा सुधार शेर शाह सूरी द्वारा पेश नहीं किया गया था?",
  question_gu="નીચેનામાંથી કયો સુધારો શેર શાહ સૂરી દ્વારા દાખલ કરવામાં આવ્યો ન હતો?",
  options=["Built the Grand Trunk Road", "Introduced a new postal system", "Introduced the Mansabdari system", "Introduced a uniform silver coin"],
  options_hi=["ग्रांड ट्रंक रोड का निर्माण किया", "एक नई डाक प्रणाली शुरू की", "मनसबदारी प्रणाली शुरू की", "समान चांदी का सिक्का पेश किया"],
  options_gu=["ગ્રાન્ડ ટ્રંક રોડ બનાવ્યો", "નવી ટપાલ વ્યવસ્થા શરૂ કરી", "મનસબદારી પ્રથા શરૂ કરી", "સમાન ચાંદીનો સિક્કો રજૂ કર્યો"],
  correct_index=2,
  explanation="Sher Shah built roads, sarais, and introduced silver coins. The Mansabdari system was introduced later by Akbar.",
  explanation_hi="शेर शाह ने सड़कें, सराय बनाईं और चांदी के सिक्के चलाए। मनसबदारी व्यवस्था बाद में अकबर द्वारा शुरू की गई थी।",
  explanation_gu="શેર શાહે રસ્તાઓ, સરાય બનાવ્યા અને ચાંદીના સિક્કા રજૂ કર્યા. મનસબદારી પ્રથા પાછળથી અકબર દ્વારા દાખલ કરવામાં આવી હતી.",
  id="KOBJ_CLAS7_SSCI_CH3_MCQ_005")

# TOPIC 3: Akbar & Haldighati
b("theory",
  title="The Great Akbar and Maharana Pratap", title_hi="महान अकबर और महाराणा प्रताप", title_gu="મહાન અકબર અને મહારાણા પ્રતાપ",
  body="Akbar was one of the greatest Mughal emperors. However, he faced fierce resistance from a true Rajput hero: Maharana Pratap of Mewar. In 1576 A.D., they fought the famous Battle of Haldighati. Akbar's massive army was led by Raja Man Singh. Maharana Pratap fought valiantly alongside his trusted commanders and his incredibly loyal horse, Chetak! Although Akbar won due to his large army, Maharana Pratap refused to surrender. He retreated to the hills and fought a guerrilla war against the Mughals for the rest of his life.",
  body_hi="अकबर महान मुगल सम्राटों में से एक था। हालाँकि, उसे एक सच्चे राजपूत नायक: मेवाड़ के महाराणा प्रताप से भयंकर प्रतिरोध का सामना करना पड़ा। 1576 ईस्वी में, उन्होंने हल्दीघाटी का प्रसिद्ध युद्ध लड़ा। अकबर की विशाल सेना का नेतृत्व राजा मान सिंह ने किया था। महाराणा प्रताप अपने भरोसेमंद कमांडरों और अपने अविश्वसनीय रूप से वफादार घोड़े, चेतक के साथ बहादुरी से लड़े! हालाँकि अपनी बड़ी सेना के कारण अकबर जीत गया, महाराणा प्रताप ने आत्मसमर्पण करने से इनकार कर दिया। वे पहाड़ियों में पीछे हट गए और जीवन भर मुगलों के खिलाफ गुरिल्ला युद्ध लड़ा।",
  body_gu="અકબર મહાન મુઘલ સમ્રાટોમાંના એક હતા. જોકે, તેમને એક સાચા રાજપૂત હીરો: મેવાડના મહારાણા પ્રતાપ તરફથી ઉગ્ર પ્રતિકારનો સામનો કરવો પડ્યો. 1576 એડીમાં, તેઓએ હલ્દીઘાટીનું પ્રખ્યાત યુદ્ધ લડ્યું. અકબરની વિશાળ સેનાનું નેતૃત્વ રાજા માન સિંહે કર્યું હતું. મહારાણા પ્રતાપ તેમના વિશ્વાસુ કમાન્ડરો અને તેમના અત્યંત વફાદાર ઘોડા, ચેતક સાથે બહાદુરીપૂર્વક લડ્યા! જોકે અકબર તેની મોટી સેનાને કારણે જીત્યો, મહારાણા પ્રતાપે શરણાગતિ સ્વીકારવાનો ઇનકાર કર્યો. તેઓ ટેકરીઓમાં પીછેહઠ કરી ગયા અને બાકીનું જીવન મુઘલો સામે ગેરિલા યુદ્ધ લડ્યા.",
  id="KOBJ_CLAS7_SSCI_CH3_THEO_003")

# Ex Q2.1: Haldighati
b("mcq",
  question="When was the Battle of Haldighati fought, and between whom?",
  question_hi="हल्दीघाटी का युद्ध कब और किसके बीच लड़ा गया था?",
  question_gu="હલ્દીઘાટીનું યુદ્ધ ક્યારે અને કોની વચ્ચે લડાયું હતું?",
  options=["1526 A.D. between Babur and Lodi", "1576 A.D. between Akbar and Maharana Pratap", "1674 A.D. between Shivaji and Aurangzeb", "1556 A.D. between Hemu and Akbar"],
  options_hi=["1526 ई. में बाबर और लोदी के बीच", "1576 ई. में अकबर और महाराणा प्रताप के बीच", "1674 ई. में शिवाजी और औरंगजेब के बीच", "1556 ई. में हेमू और अकबर के बीच"],
  options_gu=["1526 એડીમાં બાબર અને લોદી વચ્ચે", "1576 એડીમાં અકબર અને મહારાણા પ્રતાપ વચ્ચે", "1674 એડીમાં શિવાજી અને ઔરંગઝેબ વચ્ચે", "1556 એડીમાં હેમુ અને અકબર વચ્ચે"],
  correct_index=1,
  explanation="The Battle of Haldighati was fought in 1576 A.D. between Akbar and Maharana Pratap.",
  explanation_hi="हल्दीघाटी का युद्ध 1576 ईस्वी में अकबर और महाराणा प्रताप के बीच लड़ा गया था।",
  explanation_gu="હલ્દીઘાટીનું યુદ્ધ 1576 એડીમાં અકબર અને મહારાણા પ્રતાપ વચ્ચે લડાયું હતું.",
  id="KOBJ_CLAS7_SSCI_CH3_MCQ_006")

# TOPIC 4: Akbar's Administration
b("theory",
  title="Akbar's Administration System", title_hi="अकबर की प्रशासनिक व्यवस्था", title_gu="અકબરની વહીવટી વ્યવસ્થા",
  body="Akbar established a very strong centralized administration. He appointed a Prime Minister called the Wazir to look after financial revenue. The head of the military was called Mir Bakshi. Akbar's famous revenue minister was Todar Mal! Akbar also introduced the 'Mansabdari System'. A 'Mansab' meant a rank. A Mansabdar was a noble responsible for maintaining a specific army group and collecting local revenue.",
  body_hi="अकबर ने एक बहुत ही मजबूत केंद्रीकृत प्रशासन की स्थापना की। उसने वित्तीय राजस्व की देखभाल के लिए वज़ीर नामक प्रधान मंत्री की नियुक्ति की। सेना के प्रमुख को मीर बख्शी कहा जाता था। अकबर के प्रसिद्ध राजस्व मंत्री टोडरमल थे! अकबर ने 'मनसबदारी व्यवस्था' भी शुरू की। 'मनसब' का अर्थ है पद। मनसबदार एक रईस होता था जो एक विशिष्ट सेना समूह को बनाए रखने और स्थानीय कर वसूलने के लिए जिम्मेदार होता था।",
  body_gu="અકબરે ખૂબ જ મજબૂત કેન્દ્રિય વહીવટની સ્થાપના કરી. તેણે નાણાકીય મહેસૂલની દેખરેખ માટે વઝીર નામના વડા પ્રધાનની નિમણૂક કરી. સૈન્યના વડાને મીર બખ્શી કહેવાતા. અકબરના પ્રખ્યાત મહેસૂલ મંત્રી ટોડરમલ હતા! અકબરે 'મનસબદારી પ્રથા' પણ શરૂ કરી. 'મનસબ' એટલે પદ. મનસબદાર એક ઉમરાવ હતો જે ચોક્કસ સૈન્ય જૂથ જાળવવા અને સ્થાનિક મહેસૂલ એકત્રિત કરવા માટે જવાબદાર હતો.",
  id="KOBJ_CLAS7_SSCI_CH3_THEO_004")

# Ex Q3.3: Todar Mal
b("mcq",
  question="Who was Akbar's famous revenue minister?",
  question_hi="अकबर का प्रसिद्ध राजस्व मंत्री कौन था?",
  question_gu="અકબરના પ્રખ્યાત મહેસૂલ મંત્રી કોણ હતા?",
  options=["Birbal", "Tansen", "Todar Mal", "Man Singh"],
  options_hi=["बीरबल", "तानसेन", "टोडरमल", "मान सिंह"],
  options_gu=["બીરબલ", "તાનસેન", "ટોડરમલ", "માન સિંહ"],
  correct_index=2,
  explanation="Todar Mal was the famous revenue minister of Akbar.",
  explanation_hi="टोडरमल अकबर का प्रसिद्ध राजस्व मंत्री था।",
  explanation_gu="ટોડરમલ અકબરના પ્રખ્યાત મહેસૂલ મંત્રી હતા.",
  id="KOBJ_CLAS7_SSCI_CH3_MCQ_007")

# Ex Q2.2: Administration keywords
b("mcq",
  question="In Akbar's administration, what was the head of the military department called?",
  question_hi="अकबर के प्रशासन में सैन्य विभाग के प्रमुख को क्या कहा जाता था?",
  question_gu="અકબરના વહીવટમાં સૈન્ય વિભાગના વડાને શું કહેવામાં આવતું હતું?",
  options=["Wazir", "Mir Bakshi", "Mansabdar", "Sultan"],
  options_hi=["वज़ीर", "मीर बख्शी", "मनसबदार", "सुल्तान"],
  options_gu=["વઝીર", "મીર બખ્શી", "મનસબદાર", "સુલતાન"],
  correct_index=1,
  explanation="The head of the military department was called Mir Bakshi.",
  explanation_hi="सैन्य विभाग के प्रमुख को मीर बख्शी कहा जाता था।",
  explanation_gu="સૈન્ય વિભાગના વડાને મીર બખ્શી કહેવામાં આવતા હતા.",
  id="KOBJ_CLAS7_SSCI_CH3_MCQ_008")

# TOPIC 5: Art, Literature, and Architecture
b("theory",
  title="The Golden Age of Art and Architecture", title_hi="कला और वास्तुकला का स्वर्ण युग", title_gu="કલા અને સ્થાપત્યનો સુવર્ણ યુગ",
  body="The Mughal period saw amazing art! Akbar and Jahangir set up painting studios with world-famous painters like Jaswant, Basavan, and Mansoor. Authors like Abul Fazl wrote historical masterpieces (Akbarnama and Ain-i-Akbari). Valuable Hindu texts like the Mahabharata and Ramayana were translated into Persian! \n\nEmperor Shah Jahan became known as the 'Builder of Palaces'. He built the world-famous Taj Mahal in Agra, and the Red Fort (containing Diwan-i-Aam, Diwan-i-Khas, and Moti Masjid) and Jama Masjid in Delhi.",
  body_hi="मुगल काल में अद्भुत कला देखने को मिली! अकबर और जहाँगीर ने जसवंत, बसावन और मंसूर जैसे विश्व प्रसिद्ध चित्रकारों के साथ पेंटिंग स्टूडियो स्थापित किए। अबुल फजल जैसे लेखकों ने ऐतिहासिक कृतियाँ (अकबरनामा और आइन-ए-अकबरी) लिखीं। महाभारत और रामायण जैसे मूल्यवान हिंदू ग्रंथों का फारसी में अनुवाद किया गया!\n\nसम्राट शाहजहाँ को 'महलों के निर्माता' के रूप में जाना जाने लगा। उसने आगरा में विश्व प्रसिद्ध ताजमहल, और दिल्ली में लाल किला (जिसमें दीवान-ए-आम, दीवान-ए-खास और मोती मस्जिद है) तथा जामा मस्जिद का निर्माण करवाया।",
  body_gu="મુઘલ કાળમાં અદ્ભુત કલા જોવા મળી! અકબર અને જહાંગીરે જસવંત, બસાવન અને મનસૂર જેવા વિશ્વવિખ્યાત ચિત્રકારો સાથે પેઇન્ટિંગ સ્ટુડિયો સ્થાપ્યા. અબુલ ફઝલ જેવા લેખકોએ ઐતિહાસિક કૃતિઓ (અકબરનામા અને આઈન-એ-અકબરી) લખી. મહાભારત અને રામાયણ જેવા મૂલ્યવાન હિંદુ ગ્રંથોનો ફારસીમાં અનુવાદ થયો!\n\nસમ્રાટ શાહજહાં 'મહેલોના નિર્માતા' તરીકે જાણીતા બન્યા. તેમણે આગ્રામાં વિશ્વવિખ્યાત તાજમહેલ અને દિલ્હીમાં લાલ કિલ્લો (જેમાં દીવાન-એ-આમ, દીવાન-એ-ખાસ અને મોતી મસ્જિદ છે) અને જામા મસ્જિદ બનાવ્યા.",
  id="KOBJ_CLAS7_SSCI_CH3_THEO_005")

# Ex Q1.4: Shah Jahan's monuments
b("mcq",
  question="Which of these monuments was NOT built by Shah Jahan?",
  question_hi="इनमें से किस स्मारक का निर्माण शाहजहाँ ने नहीं करवाया था?",
  question_gu="આમાંથી કયા સ્મારકનું નિર્માણ શાહજહાં દ્વારા કરવામાં આવ્યું ન હતું?",
  options=["Taj Mahal", "Red Fort in Delhi", "Jama Masjid", "Qutub Minar"],
  options_hi=["ताजमहल", "दिल्ली का लाल किला", "जामा मस्जिद", "कुतुब मीनार"],
  options_gu=["તાજમહેલ", "દિલ્હીનો લાલ કિલ્લો", "જામા મસ્જિદ", "કુતુબ મીનાર"],
  correct_index=3,
  explanation="The Qutub Minar was built by Qutb-ud-din Aibak and Iltutmish (Slave Dynasty), not by Shah Jahan.",
  explanation_hi="कुतुब मीनार का निर्माण कुतुबुद्दीन ऐबक और इल्तुतमिश (गुलाम वंश) ने करवाया था, शाहजहाँ ने नहीं।",
  explanation_gu="કુતુબ મીનારનું નિર્માણ કુતુબુદ્દીન ઐબક અને ઇલ્તુત્મિશ (ગુલામ વંશ) દ્વારા કરવામાં આવ્યું હતું, શાહજહાં દ્વારા નહીં.",
  id="KOBJ_CLAS7_SSCI_CH3_MCQ_009")

# TOPIC 6: Chhatrapati Shivaji
b("theory",
  title="The Great Maratha King", title_hi="महान मराठा राजा", title_gu="મહાન મરાઠા રાજા",
  body="While the Mughals ruled the north, a mighty power rose in the Deccan. Chhatrapati Shivaji, a brilliant and fearless leader, fought against the Mughals (especially Aurangzeb) using guerrilla warfare. He was guided by his spiritual guru, Samarth Ramdas. Shivaji was finally coronated as an independent king at the Raigad Fort in 1674 A.D., where he assumed the grand title of 'Chhatrapati'.",
  body_hi="जबकि मुगलों ने उत्तर पर शासन किया, दक्कन में एक शक्तिशाली शक्ति का उदय हुआ। एक शानदार और निडर नेता, छत्रपति शिवाजी ने गुरिल्ला युद्ध का उपयोग करके मुगलों (विशेषकर औरंगजेब) के खिलाफ लड़ाई लड़ी। उनका मार्गदर्शन उनके आध्यात्मिक गुरु, समर्थ रामदास ने किया था। शिवाजी का अंततः 1674 ईस्वी में रायगढ़ किले में एक स्वतंत्र राजा के रूप में राज्याभिषेक किया गया, जहाँ उन्होंने 'छत्रपति' की भव्य उपाधि धारण की।",
  body_gu="જ્યારે મુઘલોએ ઉત્તર પર શાસન કર્યું, ત્યારે દખ્ખનમાં એક શક્તિશાળી શક્તિ ઉભરી આવી. એક તેજસ્વી અને નિર્ભય નેતા, છત્રપતિ શિવાજીએ ગેરિલા યુદ્ધનો ઉપયોગ કરીને મુઘલો (ખાસ કરીને ઔરંગઝેબ) સામે લડ્યા. તેમને તેમના આધ્યાત્મિક ગુરુ સમર્થ રામદાસ દ્વારા માર્ગદર્શન આપવામાં આવ્યું હતું. છેવટે 1674 એડીમાં રાયગઢ કિલ્લામાં શિવાજીનો એક સ્વતંત્ર રાજા તરીકે રાજ્યાભિષેક કરવામાં આવ્યો, જ્યાં તેમણે 'છત્રપતિ' નું ભવ્ય બિરુદ ધારણ કર્યું.",
  id="KOBJ_CLAS7_SSCI_CH3_THEO_006")

# Ex Q1.5: Shivaji Coronation
b("mcq",
  question="Where and when was Chhatrapati Shivaji coronated?",
  question_hi="छत्रपति शिवाजी का राज्याभिषेक कहाँ और कब हुआ था?",
  question_gu="છત્રપતિ શિવાજીનો રાજ્યાભિષેક ક્યાં અને ક્યારે થયો હતો?",
  options=["At Red Fort in 1674 A.D.", "At Raigad Fort in 1674 A.D.", "At Agra Fort in 1576 A.D.", "At Chittor Fort in 1526 A.D."],
  options_hi=["1674 ईस्वी में लाल किले में", "1674 ईस्वी में रायगढ़ किले में", "1576 ईस्वी में आगरा किले में", "1526 ईस्वी में चित्तौड़ किले में"],
  options_gu=["1674 એડીમાં લાલ કિલ્લા પર", "1674 એડીમાં રાયગઢ કિલ્લા પર", "1576 એડીમાં આગ્રા કિલ્લા પર", "1526 એડીમાં ચિત્તોડ કિલ્લા પર"],
  correct_index=1,
  explanation="Chhatrapati Shivaji was coronated at the Raigad Fort in the year 1674 A.D.",
  explanation_hi="छत्रपति शिवाजी का राज्याभिषेक वर्ष 1674 ईस्वी में रायगढ़ किले में हुआ था।",
  explanation_gu="છત્રપતિ શિવાજીનો રાજ્યાભિષેક વર્ષ 1674 એડીમાં રાયગઢ કિલ્લા પર થયો હતો.",
  id="KOBJ_CLAS7_SSCI_CH3_MCQ_010")

# Ex Q3.4: Shivaji Spiritual Guru
b("mcq",
  question="Who was the spiritual guru of Chhatrapati Shivaji?",
  question_hi="छत्रपति शिवाजी के आध्यात्मिक गुरु कौन थे?",
  question_gu="છત્રપતિ શિવાજીના આધ્યાત્મિક ગુરુ કોણ હતા?",
  options=["Ramdas", "Tukaram", "Eknath", "Jnandev"],
  options_hi=["रामदास", "तुकाराम", "एकनाथ", "ज्ञानदेव"],
  options_gu=["રામદાસ", "તુકારામ", "એકનાથ", "જ્ઞાનદેવ"],
  correct_index=0,
  explanation="Samarth Ramdas was the spiritual guru of Chhatrapati Shivaji.",
  explanation_hi="समर्थ रामदास छत्रपति शिवाजी के आध्यात्मिक गुरु थे।",
  explanation_gu="સમર્થ રામદાસ છત્રપતિ શિવાજીના આધ્યાત્મિક ગુરુ હતા.",
  id="KOBJ_CLAS7_SSCI_CH3_MCQ_011")


with open('app_core/chapters/gseb_class7_social_science_ch3.json', 'w', encoding='utf-8') as f:
    json.dump(blocks, f, indent=2, ensure_ascii=False)

print("Mughal Empire JSON generated successfully!")
