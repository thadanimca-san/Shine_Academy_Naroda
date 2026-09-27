import json

blocks = []

def b(type_val, **kwargs):
    d = {"type": type_val}
    d.update(kwargs)
    blocks.append(d)

# METADATA
b("chapter_title", 
  title="The Delhi Sultanate", 
  title_hi="दिल्ली सल्तनत", 
  title_gu="દિલ્હી સલ્તનત", 
  id="KOBJ_CLAS7_SSCI_CH2_META_001")

# TOPIC 1: Slave Dynasty and Early Rulers
b("hook", 
  title="The Rule of Slaves?", title_hi="गुलामों का शासन?", title_gu="ગુલામોનું શાસન?",
  body="Imagine being a slave, bought and sold in a market, but rising up to become the powerful King of India! This sounds like a movie, right? But it actually happened during the Delhi Sultanate. Let's find out how!",
  body_hi="कल्पना कीजिए कि एक गुलाम जिसे बाजार में खरीदा और बेचा जाता है, वह ऊपर उठकर भारत का शक्तिशाली राजा बन जाता है! यह एक फिल्म जैसा लगता है, है ना? लेकिन वास्तव में दिल्ली सल्तनत के दौरान ऐसा ही हुआ था। आइए जानें कैसे!",
  body_gu="કલ્પના કરો કે એક ગુલામ જેને બજારમાં ખરીદવામાં અને વેચવામાં આવે છે, તે ઉપર ઉઠીને ભારતનો શક્તિશાળી રાજા બની જાય છે! આ એક ફિલ્મ જેવું લાગે છે, ખરું ને? પરંતુ વાસ્તવમાં દિલ્હી સલ્તનત દરમિયાન આવું જ થયું હતું. ચાલો જાણીએ કેવી રીતે!",
  id="KOBJ_CLAS7_SSCI_CH2_HOOK_001")

b("theory",
  title="The Slave Dynasty and Qutb-ud-din Aibak", title_hi="गुलाम वंश और कुतुबुद्दीन ऐबक", title_gu="ગુલામ વંશ અને કુતુબુદ્દીન ઐબક",
  body="The foundation of the Delhi Sultanate was laid by the Slave Dynasty. The founder of the Slave Dynasty was Qutb-ud-din Aibak, who started as a military slave. He began the construction of a massive minaret in Mehrauli, Delhi, which we know today as the Qutub Minar. After his death, the construction was completed by his successor, Iltutmish.",
  body_hi="दिल्ली सल्तनत की नींव गुलाम वंश ने रखी थी। गुलाम वंश के संस्थापक कुतुबुद्दीन ऐबक थे, जिन्होंने एक सैन्य दास के रूप में शुरुआत की थी। उन्होंने दिल्ली के महरौली में एक विशाल मीनार का निर्माण शुरू किया, जिसे आज हम कुतुब मीनार के रूप में जानते हैं। उनकी मृत्यु के बाद, इस निर्माण को उनके उत्तराधिकारी इल्तुतमिश ने पूरा किया।",
  body_gu="દિલ્હી સલ્તનતનો પાયો ગુલામ વંશ દ્વારા નાખવામાં આવ્યો હતો. ગુલામ વંશના સ્થાપક કુતુબુદ્દીન ઐબક હતા, જેમણે લશ્કરી ગુલામ તરીકે શરૂઆત કરી હતી. તેમણે દિલ્હીના મહેરૌલીમાં એક વિશાળ મીનારાનું બાંધકામ શરૂ કર્યું, જેને આજે આપણે કુતુબ મીનાર તરીકે ઓળખીએ છીએ. તેમના મૃત્યુ પછી, આ બાંધકામ તેમના અનુગામી ઇલ્તુત્મિશ દ્વારા પૂર્ણ કરવામાં આવ્યું હતું.",
  id="KOBJ_CLAS7_SSCI_CH2_THEO_001")

# Ex Q1.1: Where is Qutub Minar located?
b("mcq",
  question="Where is the Qutub Minar located, and who completed its construction?",
  question_hi="कुतुब मीनार कहाँ स्थित है, और इसका निर्माण किसने पूरा किया?",
  question_gu="કુતુબ મીનાર ક્યાં આવેલો છે, અને તેનું બાંધકામ કોણે પૂર્ણ કર્યું?",
  options=["Agra, completed by Akbar", "Mehrauli (Delhi), completed by Iltutmish", "Lahore, completed by Babur", "Ajmer, completed by Alauddin Khilji"],
  options_hi=["आगरा, अकबर द्वारा पूरा किया गया", "महरौली (दिल्ली), इल्तुतमिश द्वारा पूरा किया गया", "लाहौर, बाबर द्वारा पूरा किया गया", "अजमेर, अलाउद्दीन खिलजी द्वारा पूरा किया गया"],
  options_gu=["આગરા, અકબર દ્વારા પૂર્ણ", "મહેરૌલી (દિલ્હી), ઇલ્તુત્મિશ દ્વારા પૂર્ણ", "લાહોર, બાબર દ્વારા પૂર્ણ", "અજમેર, અલાઉદ્દીન ખિલજી દ્વારા પૂર્ણ"],
  correct_index=1,
  explanation="The Qutub Minar is located in Mehrauli, Delhi. Its construction was started by Qutb-ud-din Aibak and completed by Iltutmish.",
  explanation_hi="कुतुब मीनार दिल्ली के महरौली में स्थित है। इसका निर्माण कुतुबुद्दीन ऐबक ने शुरू किया था और इल्तुतमिश ने इसे पूरा किया था।",
  explanation_gu="કુતુબ મીનાર દિલ્હીના મહેરૌલીમાં આવેલો છે. તેનું બાંધકામ કુતુબુદ્દીન ઐબકે શરૂ કર્યું હતું અને ઇલ્તુત્મિશે પૂર્ણ કર્યું હતું.",
  id="KOBJ_CLAS7_SSCI_CH2_MCQ_001")

# Ex Q3.1: Founder of slave dynasty
b("mcq",
  question="Who was the founder of the Slave Dynasty?",
  question_hi="गुलाम वंश का संस्थापक कौन था?",
  question_gu="ગુલામ વંશના સ્થાપક કોણ હતા?",
  options=["Iltutmish", "Qutb-ud-din Aibak", "Razia Sultana", "Alauddin Khilji"],
  options_hi=["इल्तुतमिश", "कुतुबुद्दीन ऐबक", "रजिया सुल्ताना", "अलाउद्दीन खिलजी"],
  options_gu=["ઇલ્તુત્મિશ", "કુતુબુદ્દીન ઐબક", "રઝિયા સુલતાના", "અલાઉદ્દીન ખિલજી"],
  correct_index=1,
  explanation="The founder of the Slave Dynasty was Qutb-ud-din Aibak.",
  explanation_hi="गुलाम वंश के संस्थापक कुतुबुद्दीन ऐबक थे।",
  explanation_gu="ગુલામ વંશના સ્થાપક કુતુબુદ્દીન ઐબક હતા.",
  id="KOBJ_CLAS7_SSCI_CH2_MCQ_002")

b("theory",
  title="The First Female Ruler", title_hi="पहली महिला शासक", title_gu="પ્રથમ મહિલા શાસક",
  body="After Iltutmish, his daughter Razia Sultana took the throne. Razia Sultana was the first female ruler to occupy the throne of Delhi! In a time when women were mostly kept behind the veil, she led armies and ruled fiercely.",
  body_hi="इल्तुतमिश के बाद, उनकी बेटी रजिया सुल्ताना ने गद्दी संभाली। रजिया सुल्ताना दिल्ली के सिंहासन पर बैठने वाली पहली महिला शासक थीं! ऐसे समय में जब महिलाओं को ज्यादातर पर्दे के पीछे रखा जाता था, उन्होंने सेनाओं का नेतृत्व किया और पूरी ताकत से शासन किया।",
  body_gu="ઇલ્તુત્મિશ પછી, તેમની પુત્રી રઝિયા સુલતાનાએ ગાદી સંભાળી. રઝિયા સુલતાના દિલ્હીની ગાદી પર બેસનાર પ્રથમ મહિલા શાસક હતા! એવા સમયે જ્યારે સ્ત્રીઓને મોટે ભાગે પડદા પાછળ રાખવામાં આવતી હતી, તેમણે સૈન્યનું નેતૃત્વ કર્યું અને પૂરી તાકાતથી શાસન કર્યું.",
  id="KOBJ_CLAS7_SSCI_CH2_THEO_002")

# Ex Q3.2: Razia sultana
b("mcq",
  question="Who was the first female ruler to occupy the throne of Delhi?",
  question_hi="दिल्ली के सिंहासन पर बैठने वाली पहली महिला शासक कौन थीं?",
  question_gu="દિલ્હીની ગાદી પર બેસનાર પ્રથમ મહિલા શાસક કોણ હતા?",
  options=["Nur Jahan", "Mumtaz Mahal", "Razia Sultana", "Rani Lakshmibai"],
  options_hi=["नूरजहाँ", "मुमताज महल", "रजिया सुल्ताना", "रानी लक्ष्मीबाई"],
  options_gu=["નૂરજહાં", "મુમતાઝ મહેલ", "રઝિયા સુલતાના", "રાણી લક્ષ્મીબાઈ"],
  correct_index=2,
  explanation="Razia Sultana was the daughter of Iltutmish and became the first female ruler of Delhi.",
  explanation_hi="रजिया सुल्ताना इल्तुतमिश की बेटी थीं और दिल्ली की पहली महिला शासक बनीं।",
  explanation_gu="રઝિયા સુલતાના ઇલ્તુત્મિશની પુત્રી હતા અને દિલ્હીના પ્રથમ મહિલા શાસક બન્યા.",
  id="KOBJ_CLAS7_SSCI_CH2_MCQ_003")

# TOPIC 2: Khilji Dynasty
b("theory",
  title="The Khilji Dynasty and Siri", title_hi="खिलजी वंश और सिरी", title_gu="ખિલજી વંશ અને સિરી",
  body="Next came the Khilji Dynasty. One of its most famous and powerful rulers was Alauddin Khilji. He wanted to make his capital beautiful and strong against Mongol attacks. So, the city of Siri was built by Alauddin Khilji. During his reign, he also built a grand and beautiful entrance to the Quwwat-ul-Islam Mosque known as the Alai Darwaza.",
  body_hi="इसके बाद खिलजी वंश आया। इसके सबसे प्रसिद्ध और शक्तिशाली शासकों में से एक अलाउद्दीन खिलजी थे। वह मंगोल हमलों के खिलाफ अपनी राजधानी को सुंदर और मजबूत बनाना चाहते थे। इसलिए, अलाउद्दीन खिलजी ने सिरी शहर का निर्माण करवाया था। अपने शासनकाल के दौरान, उन्होंने कुव्वत-उल-इस्लाम मस्जिद के लिए एक भव्य और सुंदर प्रवेश द्वार भी बनवाया जिसे अलाई दरवाजा के नाम से जाना जाता है।",
  body_gu="આગળ ખિલજી વંશ આવ્યો. તેના સૌથી પ્રખ્યાત અને શક્તિશાળી શાસકોમાંના એક અલાઉદ્દીન ખિલજી હતા. તે પોતાની રાજધાનીને મંગોલ હુમલાઓ સામે સુંદર અને મજબૂત બનાવવા માંગતા હતા. તેથી, સિરી શહેર અલાઉદ્દીન ખિલજી દ્વારા બનાવવામાં આવ્યું હતું. તેમના શાસન દરમિયાન, તેમણે કુવ્વત-ઉલ-ઇસ્લામ મસ્જિદ માટે એક ભવ્ય અને સુંદર પ્રવેશદ્વાર પણ બનાવ્યો જે અલાઈ દરવાજા તરીકે ઓળખાય છે.",
  id="KOBJ_CLAS7_SSCI_CH2_THEO_003")

# Ex Q3.3: Siri city built by
b("mcq",
  question="Which ruler built the city of Siri?",
  question_hi="सिरी शहर का निर्माण किस शासक ने करवाया था?",
  question_gu="સિરી શહેર કોણે બનાવ્યું હતું?",
  options=["Qutb-ud-din Aibak", "Alauddin Khilji", "Muhammad bin Tughlaq", "Ibrahim Lodi"],
  options_hi=["कुतुबुद्दीन ऐबक", "अलाउद्दीन खिलजी", "मुहम्मद बिन तुगलक", "इब्राहिम लोदी"],
  options_gu=["કુતુબુદ્દીન ઐબક", "અલાઉદ્દીન ખિલજી", "મુહમ્મદ બિન તુગલક", "ઇબ્રાહિમ લોદી"],
  correct_index=1,
  explanation="The city of Siri was built by Alauddin Khilji to protect the population from Mongol invasions.",
  explanation_hi="मंगोल आक्रमणों से आबादी को बचाने के लिए अलाउद्दीन खिलजी द्वारा सिरी शहर का निर्माण किया गया था।",
  explanation_gu="મંગોલ આક્રમણોથી વસ્તીને બચાવવા માટે અલાઉદ્દીન ખિલજી દ્વારા સિરી શહેર બનાવવામાં આવ્યું હતું.",
  id="KOBJ_CLAS7_SSCI_CH2_MCQ_004")

# Ex Q1.3: Alai Darwaza
b("mcq",
  question="In whose time was the Alai Darwaza built?",
  question_hi="अलाई दरवाजा किसके समय में बनाया गया था?",
  question_gu="અલાઈ દરવાજા કોના સમયમાં બનાવવામાં આવ્યો હતો?",
  options=["Iltutmish", "Ghiyasuddin Tughlaq", "Alauddin Khilji", "Babur"],
  options_hi=["इल्तुतमिश", "गयासुद्दीन तुगलक", "अलाउद्दीन खिलजी", "बाबर"],
  options_gu=["ઇલ્તુત્મિશ", "ગિયાસુદ્દીન તુગલક", "અલાઉદ્દીન ખિલજી", "બાબર"],
  correct_index=2,
  explanation="The Alai Darwaza was built during the reign of Alauddin Khilji as a grand entrance to the Quwwat-ul-Islam Mosque.",
  explanation_hi="अलाई दरवाजा का निर्माण अलाउद्दीन खिलजी के शासनकाल के दौरान कुव्वत-उल-इस्लाम मस्जिद के भव्य प्रवेश द्वार के रूप में किया गया था।",
  explanation_gu="અલાઈ દરવાજા અલાઉદ્દીન ખિલજીના શાસન દરમિયાન કુવ્વત-ઉલ-ઇસ્લામ મસ્જિદના ભવ્ય પ્રવેશદ્વાર તરીકે બનાવવામાં આવ્યો હતો.",
  id="KOBJ_CLAS7_SSCI_CH2_MCQ_005")

# TOPIC 3: Tughlaq Dynasty & Public Works
b("socratic_question",
  question="If you were a king, and you wanted to completely change your country's money from gold coins to copper coins overnight, what problems do you think might happen?",
  question_hi="यदि आप एक राजा होते, और आप रातोंरात अपने देश के धन को सोने के सिक्कों से तांबे के सिक्कों में पूरी तरह से बदलना चाहते, तो आपको क्या लगता है कि क्या समस्याएँ हो सकती हैं?",
  question_gu="જો તમે રાજા હોવ, અને તમે રાતોરાત તમારા દેશના નાણાંને સોનાના સિક્કામાંથી તાંબાના સિક્કામાં સંપૂર્ણપણે બદલવા માંગતા હોવ, તો તમને શું લાગે છે કે કઈ સમસ્યાઓ થઈ શકે છે?",
  id="KOBJ_CLAS7_SSCI_CH2_SOCR_001")

b("theory",
  title="The Tughlaq Dynasty's Wild Experiments", title_hi="तुगलक वंश के अजीब प्रयोग", title_gu="તુગલક વંશના અજીબ પ્રયોગો",
  body="The internal administration under the Tughlaq dynasty (like Ghiyasuddin and Muhammad bin Tughlaq) was known for ambitious but chaotic experiments. Muhammad bin Tughlaq introduced 'Tarangi Schemes' (eccentric policies). He tried changing the capital from Delhi to Daulatabad (forcing everyone to walk 1500 km!) and introduced copper currency tokens instead of silver. Due to a lack of planning and proper execution, these schemes failed terribly, causing total chaos.",
  body_hi="तुगलक वंश (जैसे गयासुद्दीन और मुहम्मद बिन तुगलक) के तहत आंतरिक प्रशासन महत्वाकांक्षी लेकिन अराजक प्रयोगों के लिए जाना जाता था। मुहम्मद बिन तुगलक ने 'तरंगी योजनाएं' (सनकी नीतियां) पेश कीं। उन्होंने राजधानी को दिल्ली से दौलताबाद (सभी को 1500 किमी चलने के लिए मजबूर किया!) में बदलने की कोशिश की और चांदी के बजाय तांबे की मुद्रा टोकन पेश किए। उचित योजना और निष्पादन की कमी के कारण, ये योजनाएँ बुरी तरह विफल रहीं, जिससे प्रशासन में भारी अराजकता फैल गई।",
  body_gu="તુગલક વંશ (જેમ કે ગિયાસુદ્દીન અને મુહમ્મદ બિન તુગલક) હેઠળ આંતરિક વહીવટ મહત્વાકાંક્ષી પરંતુ અસ્તવ્યસ્ત પ્રયોગો માટે જાણીતો હતો. મુહમ્મદ બિન તુગલકે 'તરંગી યોજનાઓ' (વિચિત્ર નીતિઓ) રજૂ કરી. તેણે રાજધાનીને દિલ્હીથી દોલતાબાદ (બધાને 1500 કિમી ચાલવા માટે મજબૂર કર્યા!) બદલવાનો પ્રયાસ કર્યો અને ચાંદીના બદલે તાંબાના ચલણ ટોકન રજૂ કર્યા. યોગ્ય આયોજન અને અમલીકરણના અભાવને કારણે, આ યોજનાઓ ખરાબ રીતે નિષ્ફળ ગઈ, જેના કારણે ભારે અરાજકતા ફેલાઈ.",
  id="KOBJ_CLAS7_SSCI_CH2_THEO_004")

# Ex Q2.1: Tughlaq internal administration
b("mcq",
  question="What were the administrative policies of Muhammad bin Tughlaq, like shifting the capital and introducing copper currency, known as?",
  question_hi="मुहम्मद बिन तुगलक की प्रशासनिक नीतियां, जैसे राजधानी बदलना और तांबे की मुद्रा शुरू करना, किस नाम से जानी जाती थीं?",
  question_gu="મુહમ્મદ બિન તુગલકની વહીવટી નીતિઓ, જેમ કે રાજધાની બદલવી અને તાંબાનું ચલણ રજૂ કરવું, કયા નામે ઓળખાતી હતી?",
  options=["Golden Age Policies", "Tarangi Schemes", "Siri Development Plan", "Daulatabad Rules"],
  options_hi=["स्वर्ण युग की नीतियां", "तरंगी योजनाएं", "सिरी विकास योजना", "दौलताबाद के नियम"],
  options_gu=["સુવર્ણ યુગની નીતિઓ", "તરંગી યોજનાઓ", "સિરી વિકાસ યોજના", "દોલતાબાદના નિયમો"],
  correct_index=1,
  explanation="His ambitious but poorly executed policies were called 'Tarangi Schemes', and they caused massive chaos in the administration.",
  explanation_hi="उनकी महत्वाकांक्षी लेकिन खराब तरीके से लागू की गई नीतियों को 'तरंगी योजनाएं' कहा जाता था, और उन्होंने प्रशासन में भारी अराजकता पैदा की।",
  explanation_gu="તેમની મહત્વાકાંક્ષી પરંતુ ખરાબ રીતે અમલમાં મુકાયેલી નીતિઓને 'તરંગી યોજનાઓ' કહેવામાં આવતી હતી, અને તેઓએ વહીવટમાં ભારે અરાજકતા ફેલાવી હતી.",
  id="KOBJ_CLAS7_SSCI_CH2_MCQ_006")

b("theory",
  title="Public Works of the Sultanate", title_hi="सल्तनत के सार्वजनिक कार्य", title_gu="સલ્તનતના જાહેર કાર્યો",
  body="Despite some failed experiments, the Sultans built amazing public utilities and grand structures to fortify and beautify their empire. They constructed massive forts, mosques, minarets, palaces, public baths (hammams), tombs, wells, and sarais (inns) for travelers. Important architectural wonders include the Qutub Minar, Adhai Din Ka Jhonpra mosque, Siri Fort, Hauz Khas, and new cities like Firozabad and Tughlaqabad.",
  body_hi="कुछ विफल प्रयोगों के बावजूद, सुल्तानों ने अपने साम्राज्य को मजबूत करने और सुंदर बनाने के लिए अद्भुत सार्वजनिक उपयोगिताओं और भव्य संरचनाओं का निर्माण किया। उन्होंने विशाल किलों, मस्जिदों, मीनारों, महलों, सार्वजनिक स्नानागार (हम्माम), मकबरों, कुओं और यात्रियों के लिए सरायों का निर्माण किया। महत्वपूर्ण वास्तुशिल्प चमत्कारों में कुतुब मीनार, अढ़ाई दिन का झोपड़ा मस्जिद, सिरी फोर्ट, हौज़ खास और फिरोजाबाद और तुगलकाबाद जैसे नए शहर शामिल हैं।",
  body_gu="કેટલાક નિષ્ફળ પ્રયોગો છતાં, સુલતાનોએ તેમના સામ્રાજ્યને મજબૂત અને સુંદર બનાવવા માટે અદ્ભુત જાહેર ઉપયોગિતાઓ અને ભવ્ય રચનાઓ બનાવી. તેઓએ વિશાળ કિલ્લાઓ, મસ્જિદો, મીનારાઓ, મહેલો, જાહેર સ્નાનાગાર (હમ્મામ), મકબરાઓ, કુવાઓ અને મુસાફરો માટે સરાય (ધર્મશાળાઓ) બનાવ્યા. મહત્વપૂર્ણ સ્થાપત્ય અજાયબીઓમાં કુતુબ મીનાર, અઢી દિન કા ઝોંપડા મસ્જિદ, સિરી ફોર્ટ, હોઝ ખાસ અને ફિરોઝાબાદ અને તુગલકાબાદ જેવા નવા શહેરો સામેલ છે.",
  id="KOBJ_CLAS7_SSCI_CH2_THEO_005")

# Ex Q2.2: Public works
b("mcq",
  question="Which of the following is NOT an example of a public work carried out during the Delhi Sultanate?",
  question_hi="निम्नलिखित में से कौन सा दिल्ली सल्तनत के दौरान किए गए सार्वजनिक कार्य का उदाहरण नहीं है?",
  question_gu="નીચેનામાંથી કયું દિલ્હી સલ્તનત દરમિયાન કરવામાં આવેલ જાહેર કાર્યનું ઉદાહરણ નથી?",
  options=["Constructing public baths (hammams) and wells", "Building the Taj Mahal", "Building sarais (inns) for travelers", "Constructing Hauz Khas and Siri Fort"],
  options_hi=["सार्वजनिक स्नानागार (हम्माम) और कुओं का निर्माण", "ताजमहल का निर्माण", "यात्रियों के लिए सराय का निर्माण", "हौज़ खास और सिरी फोर्ट का निर्माण"],
  options_gu=["જાહેર સ્નાનાગાર (હમ્મામ) અને કુવાઓનું નિર્માણ", "તાજમહેલનું નિર્માણ", "મુસાફરો માટે સરાય (ધર્મશાળાઓ) નું નિર્માણ", "હોઝ ખાસ અને સિરી ફોર્ટનું નિર્માણ"],
  correct_index=1,
  explanation="The Taj Mahal was built much later by the Mughals, not during the Delhi Sultanate. The Sultans built mosques, minarets, sarais, and forts.",
  explanation_hi="ताजमहल का निर्माण बहुत बाद में मुगलों द्वारा किया गया था, न कि दिल्ली सल्तनत के दौरान। सुल्तानों ने मस्जिदें, मीनारें, सराय और किले बनवाए।",
  explanation_gu="તાજમહેલનું નિર્માણ ખૂબ પાછળથી મુઘલો દ્વારા કરવામાં આવ્યું હતું, દિલ્હી સલ્તનત દરમિયાન નહીં. સુલતાનોએ મસ્જિદો, મીનારા, સરાય અને કિલ્લાઓ બનાવ્યા.",
  id="KOBJ_CLAS7_SSCI_CH2_MCQ_007")

# TOPIC 4: The End of the Sultanate & Bahmani Kingdom
b("theory",
  title="The End of the Sultanate", title_hi="सल्तनत का अंत", title_gu="સલ્તનતનો અંત",
  body="The power of the Delhi Sultanate eventually faded. In 1347 AD, the Bahmani Kingdom was established in the Deccan by Zafar Khan, who assumed the title of Alauddin Hasan Bahman Shah. Finally, in the north, the last ruler of the Delhi Sultanate was Ibrahim Lodi. In 1526 AD, the first Battle of Panipat took place between Ibrahim Lodi and Babur. Babur won this battle, crushing the Sultanate and establishing the great Mughal Empire in India.",
  body_hi="दिल्ली सल्तनत की शक्ति अंततः कम हो गई। 1347 ईस्वी में, दक्कन में जफर खान द्वारा बहमनी साम्राज्य की स्थापना की गई थी, जिन्होंने अलाउद्दीन हसन बहमन शाह की उपाधि धारण की थी। अंत में, उत्तर में, दिल्ली सल्तनत का अंतिम शासक इब्राहिम लोदी था। 1526 ईस्वी में, इब्राहिम लोदी और बाबर के बीच पानीपत की पहली लड़ाई हुई। बाबर ने यह लड़ाई जीती, सल्तनत को कुचल दिया और भारत में महान मुगल साम्राज्य की स्थापना की।",
  body_gu="દિલ્હી સલ્તનતની સત્તા આખરે ઓછી થઈ ગઈ. 1347 એડીમાં, દખ્ખનમાં ઝફર ખાન દ્વારા બહમની સામ્રાજ્યની સ્થાપના કરવામાં આવી હતી, જેમણે અલાઉદ્દીન હસન બહમન શાહનું બિરુદ ધારણ કર્યું હતું. છેવટે, ઉત્તરમાં, દિલ્હી સલ્તનતનો છેલ્લો શાસક ઇબ્રાહિમ લોદી હતો. 1526 એડીમાં, ઇબ્રાહિમ લોદી અને બાબર વચ્ચે પાણીપતનું પ્રથમ યુદ્ધ થયું. બાબરે આ યુદ્ધ જીત્યું, સલ્તનતને કચડી નાખી અને ભારતમાં મહાન મુઘલ સામ્રાજ્યની સ્થાપના કરી.",
  id="KOBJ_CLAS7_SSCI_CH2_THEO_006")

# Ex Q1.4: Bahmani Kingdom
b("mcq",
  question="Who established the Bahmani Kingdom in 1347 AD?",
  question_hi="1347 ईस्वी में बहमनी साम्राज्य की स्थापना किसने की?",
  question_gu="1347 એડીમાં બહમની સામ્રાજ્યની સ્થાપના કોણે કરી?",
  options=["Ibrahim Lodi", "Zafar Khan (Alauddin Hasan Bahman Shah)", "Babur", "Muhammad bin Tughlaq"],
  options_hi=["इब्राहिम लोदी", "जफर खान (अलाउद्दीन हसन बहमन शाह)", "बाबर", "मुहम्मद बिन तुगलक"],
  options_gu=["ઇબ્રાહિમ લોદી", "ઝફર ખાન (અલાઉદ્દીન હસન બહમન શાહ)", "બાબર", "મુહમ્મદ બિન તુગલક"],
  correct_index=1,
  explanation="The Bahmani Kingdom was established by Zafar Khan (Alauddin Hasan Bahman Shah) in 1347 AD.",
  explanation_hi="बहमनी साम्राज्य की स्थापना 1347 ईस्वी में जफर खान (अलाउद्दीन हसन बहमन शाह) ने की थी।",
  explanation_gu="બહમની સામ્રાજ્યની સ્થાપના 1347 એડીમાં ઝફર ખાન (અલાઉદ્દીન હસન બહમન શાહ) દ્વારા કરવામાં આવી હતી.",
  id="KOBJ_CLAS7_SSCI_CH2_MCQ_008")

# Ex Q3.4: Last ruler of Delhi Sultanate
b("mcq",
  question="Who was the last ruler of the Delhi Sultanate?",
  question_hi="दिल्ली सल्तनत का अंतिम शासक कौन था?",
  question_gu="દિલ્હી સલ્તનતનો છેલ્લો શાસક કોણ હતો?",
  options=["Sikandar Lodi", "Bahlol Lodi", "Ibrahim Lodi", "Babur"],
  options_hi=["सिकंदर लोदी", "बहलोल लोदी", "इब्राहिम लोदी", "बाबर"],
  options_gu=["સિકંદર લોદી", "બહલોલ લોદી", "ઇબ્રાહિમ લોદી", "બાબર"],
  correct_index=2,
  explanation="The last ruler of the Delhi Sultanate was Ibrahim Lodi, who was defeated by Babur.",
  explanation_hi="दिल्ली सल्तनत का अंतिम शासक इब्राहिम लोदी था, जिसे बाबर ने हराया था।",
  explanation_gu="દિલ્હી સલ્તનતનો છેલ્લો શાસક ઇબ્રાહિમ લોદી હતો, જેને બાબરે હરાવ્યો હતો.",
  id="KOBJ_CLAS7_SSCI_CH2_MCQ_009")

# Ex Q1.2: Battle of Panipat
b("mcq",
  question="Between whom was the first Battle of Panipat fought in 1526 AD?",
  question_hi="1526 ईस्वी में पानीपत की पहली लड़ाई किसके बीच लड़ी गई थी?",
  question_gu="1526 એડીમાં પાણીપતનું પ્રથમ યુદ્ધ કોની વચ્ચે લડાયું હતું?",
  options=["Akbar and Hemu", "Ibrahim Lodi and Babur", "Alauddin Khilji and the Mongols", "Ghiyasuddin and Zafar Khan"],
  options_hi=["अकबर और हेमू", "इब्राहिम लोदी और बाबर", "अलाउद्दीन खिलजी और मंगोल", "गयासुद्दीन और जफर खान"],
  options_gu=["અકબર અને હેમુ", "ઇબ્રાહિમ લોદી અને બાબર", "અલાઉદ્દીન ખિલજી અને મંગોલો", "ગિયાસુદ્દીન અને ઝફર ખાન"],
  correct_index=1,
  explanation="The first Battle of Panipat was fought between Ibrahim Lodi and Babur. Babur won, establishing the Mughal Empire.",
  explanation_hi="पानीपत की पहली लड़ाई इब्राहिम लोदी और बाबर के बीच लड़ी गई थी। बाबर ने जीत हासिल की, जिससे मुगल साम्राज्य की स्थापना हुई।",
  explanation_gu="પાણીપતનું પ્રથમ યુદ્ધ ઇબ્રાહિમ લોદી અને બાબર વચ્ચે લડાયું હતું. બાબરે જીત મેળવી, મુઘલ સામ્રાજ્યની સ્થાપના કરી.",
  id="KOBJ_CLAS7_SSCI_CH2_MCQ_010")

with open('app_core/chapters/gseb_class7_social_science_ch2.json', 'w', encoding='utf-8') as f:
    json.dump(blocks, f, indent=2, ensure_ascii=False)

print("Delhi Sultanate JSON generated successfully!")
