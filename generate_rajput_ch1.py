import json

blocks = []

def b(type_val, **kwargs):
    d = {"type": type_val}
    d.update(kwargs)
    blocks.append(d)

# METADATA
b("chapter_title", 
  title="Rajput Age: New Rulers and States", 
  title_hi="राजपूत युग: नए शासक और राज्य", 
  title_gu="રાજપૂત યુગ: નવા શાસકો અને રાજ્યો", 
  id="KOBJ_CLAS7_SSCI_CH1_META_001")

# TOPIC 1: Rajputs
b("hook", 
  title="The Brave Defenders", title_hi="बहादुर रक्षक", title_gu="બહાદુર રક્ષકો",
  body="Imagine a time when kings fought not just for land, but for honor. A time when words like bravery and loyalty meant more than life itself! Who were these legendary warriors?",
  body_hi="एक ऐसे समय की कल्पना करें जब राजा केवल जमीन के लिए नहीं, बल्कि सम्मान के लिए लड़ते थे। एक ऐसा समय जब बहादुरी और वफादारी जैसे शब्दों का अर्थ जीवन से भी बढ़कर था! ये महान योद्धा कौन थे?",
  body_gu="એવા સમયની કલ્પના કરો જ્યારે રાજાઓ માત્ર જમીન માટે જ નહીં, પણ સન્માન માટે લડ્યા હતા. એવો સમય જ્યારે બહાદુરી અને વફાદારી જેવા શબ્દોનો અર્થ જીવન કરતા પણ વધુ હતો! આ મહાન યોદ્ધાઓ કોણ હતા?",
  id="KOBJ_CLAS7_SSCI_CH1_HOOK_001")

b("socratic_question",
  question="If an enemy offered you money to surrender, would you accept it or fight to the end for your kingdom's pride?",
  question_hi="यदि कोई दुश्मन आपको आत्मसमर्पण करने के लिए पैसे की पेशकश करता है, तो क्या आप इसे स्वीकार करेंगे या अपने राज्य के गौरव के लिए अंत तक लड़ेंगे?",
  question_gu="જો કોઈ દુશ્મન તમને આત્મસમર્પણ કરવા માટે પૈસા આપે, તો શું તમે તેને સ્વીકારશો કે તમારા રાજ્યના ગૌરવ માટે અંત સુધી લડશો?",
  id="KOBJ_CLAS7_SSCI_CH1_SOCR_001")

b("discovery",
  title="The Code of Honor", title_hi="सम्मान की संहिता", title_gu="સન્માનની સંહિતા",
  body="For the Rajput warriors, the answer was always to fight! They followed strict rules: never attack someone by trickery, always protect the weak, and never run away from a battle.",
  body_hi="राजपूत योद्धाओं के लिए, जवाब हमेशा लड़ना था! उन्होंने कड़े नियमों का पालन किया: कभी धोखे से किसी पर हमला न करें, हमेशा कमजोरों की रक्षा करें, और कभी भी युद्ध से न भागें।",
  body_gu="રાજપૂત યોદ્ધાઓ માટે, જવાબ હંમેશા લડવાનો હતો! તેઓ કડક નિયમોનું પાલન કરતા: ક્યારેય છેતરપિંડીથી કોઈ પર હુમલો ન કરવો, હંમેશા નબળાઓનું રક્ષણ કરવું, અને ક્યારેય યુદ્ધમાંથી ભાગવું નહીં.",
  id="KOBJ_CLAS7_SSCI_CH1_DISC_001")

b("theory",
  title="Characteristics of Rajputs", title_hi="राजपूतों की विशेषताएं", title_gu="રાજપૂતોની લાક્ષણિકતાઓ",
  body="Rajputs were exceptionally brave, proud, and loyal to their word. They preferred dying on the battlefield over retreating or surrendering. They were known as the protectors of cows, Brahmins, and the needy ('Gau-Brahmin Pratipalak'). They followed strict rules of warfare, never using deceitful tactics, and always protected those who sought refuge.",
  body_hi="राजपूत असाधारण रूप से बहादुर, गौरवान्वित और अपने वचन के प्रति वफादार थे। उन्होंने पीछे हटने या आत्मसमर्पण करने के बजाय युद्ध के मैदान में मरना पसंद किया। उन्हें गायों, ब्राह्मणों और जरूरतमंदों के रक्षक ('गौ-ब्राह्मण प्रतिपालक') के रूप में जाना जाता था। उन्होंने युद्ध के कड़े नियमों का पालन किया, कभी भी छलपूर्ण रणनीति का इस्तेमाल नहीं किया, और हमेशा शरण मांगने वालों की रक्षा की।",
  body_gu="રાજપૂતો અપવાદરૂપે બહાદુર, ગૌરવશાળી અને તેમના શબ્દ પ્રત્યે વફાદાર હતા. તેઓએ પીછેહઠ કરવા અથવા શરણાગતિ સ્વીકારવાને બદલે યુદ્ધના મેદાનમાં મરવાનું પસંદ કર્યું. તેઓ ગાયો, બ્રાહ્મણો અને જરૂરિયાતમંદોના રક્ષક ('ગૌ-બ્રાહ્મણ પ્રતિપાલક') તરીકે ઓળખાતા હતા. તેઓ યુદ્ધના કડક નિયમોનું પાલન કરતા હતા, ક્યારેય છેતરપિંડીની યુક્તિઓનો ઉપયોગ કરતા ન હતા, અને હંમેશા આશ્રય માંગનારાઓનું રક્ષણ કરતા હતા.",
  id="KOBJ_CLAS7_SSCI_CH1_THEO_001")

# Ex Q2: Characteristics of Rajputs
b("mcq",
  question="Which of the following is NOT a characteristic of the Rajputs?",
  question_hi="निम्नलिखित में से कौन राजपूतों की विशेषता नहीं है?",
  question_gu="નીચેનામાંથી કઈ રાજપૂતોની લાક્ષણિકતા નથી?",
  options=["They were protectors of cows and Brahmins", "They preferred dying over surrendering", "They used deceitful tactics in battle", "They were exceptionally brave and loyal"],
  options_hi=["वे गायों और ब्राह्मणों के रक्षक थे", "उन्होंने आत्मसमर्पण करने के बजाय मरना पसंद किया", "वे युद्ध में छलपूर्ण रणनीति का इस्तेमाल करते थे", "वे असाधारण रूप से बहादुर और वफादार थे"],
  options_gu=["તેઓ ગાયો અને બ્રાહ્મણોના રક્ષક હતા", "તેઓએ શરણાગતિ સ્વીકારવાને બદલે મરવાનું પસંદ કર્યું", "તેઓ યુદ્ધમાં છેતરપિંડીની યુક્તિઓનો ઉપયોગ કરતા હતા", "તેઓ અપવાદરૂપે બહાદુર અને વફાદાર હતા"],
  correct_index=2,
  explanation="Rajputs followed strict rules of chivalry and never used deceitful tactics in battle.",
  explanation_hi="राजपूत शौर्य के कड़े नियमों का पालन करते थे और युद्ध में कभी भी छलपूर्ण रणनीति का उपयोग नहीं करते थे।",
  explanation_gu="રાજપૂતો શૌર્યના કડક નિયમોનું પાલન કરતા હતા અને યુદ્ધમાં ક્યારેય છેતરપિંડીની યુક્તિઓનો ઉપયોગ કરતા ન હતા.",
  id="KOBJ_CLAS7_SSCI_CH1_MCQ_001")


# TOPIC 2: North India & Gujarat
b("hook",
  title="The Lost Cities of Gujarat", title_hi="गुजरात के खोए हुए शहर", title_gu="ગુજરાતના ખોવાયેલા શહેરો",
  body="Who built the grand stepwells of Gujarat? How did cities like Patan become massive centers of wealth and trade? Let's discover the golden era of Gujarat!",
  body_hi="गुजरात की भव्य बावड़ियों (stepwells) का निर्माण किसने किया? पाटन जैसे शहर धन और व्यापार के विशाल केंद्र कैसे बने? आइए गुजरात के स्वर्ण युग की खोज करें!",
  body_gu="ગુજરાતની ભવ્ય વાવ કોણે બનાવી? પાટણ જેવા શહેરો સંપત્તિ અને વેપારના વિશાળ કેન્દ્રો કેવી રીતે બન્યા? ચાલો ગુજરાતના સુવર્ણ યુગની શોધ કરીએ!",
  id="KOBJ_CLAS7_SSCI_CH1_HOOK_002")

b("theory",
  title="Anhilwad Patan and The Solankis", title_hi="अन्हिलवाड़ पाटन और सोलंकी", title_gu="અણહિલવાડ પાટણ અને સોલંકીઓ",
  body="Vanraj Chavda founded Anhilwad Patan on the banks of the Saraswati River in 746 AD. Later, the Solanki dynasty ruled Gujarat. During the Solanki rule, Queen Udayamati (wife of King Bhimdev I) built the famous 'Rani ki Vav' (Queen's Stepwell) to solve the drinking water problem for the people of Patan.",
  body_hi="वनराज चावड़ा ने 746 ईस्वी में सरस्वती नदी के तट पर अन्हिलवाड़ पाटन की स्थापना की। बाद में, सोलंकी राजवंश ने गुजरात पर शासन किया। सोलंकी शासन के दौरान, रानी उदयमती (राजा भीमदेव प्रथम की पत्नी) ने पाटन के लोगों के लिए पीने के पानी की समस्या को हल करने के लिए प्रसिद्ध 'रानी की वाव' (रानी की बावड़ी) का निर्माण किया।",
  body_gu="વનરાજ ચાવડાએ 746 એડીમાં સરસ્વતી નદીના કિનારે અણહિલવાડ પાટણની સ્થાપના કરી. બાદમાં, સોલંકી રાજવંશે ગુજરાત પર શાસન કર્યું. સોલંકી શાસન દરમિયાન, રાણી ઉદયમતી (રાજા ભીમદેવ પ્રથમની પત્ની) એ પાટણના લોકો માટે પીવાના પાણીની સમસ્યા હલ કરવા માટે પ્રખ્યાત 'રાણી ની વાવ' બનાવી.",
  id="KOBJ_CLAS7_SSCI_CH1_THEO_002")

# Ex Q1: Who built Rani ki Vav and why?
b("mcq",
  question="Who built 'Rani ki Vav' (Queen's Stepwell) and why?",
  question_hi="किसने 'रानी की वाव' (रानी की बावड़ी) का निर्माण किया और क्यों?",
  question_gu="કોણે 'રાણી ની વાવ' બનાવી અને શા માટે?",
  options=["Rajmata Minaldevi to collect taxes", "Queen Udayamati to solve the drinking water problem", "Vanraj Chavda to build a fort", "Muzaffar Shah to celebrate victory"],
  options_hi=["राजमाता मीनलदेवी ने कर वसूलने के लिए", "रानी उदयमती ने पीने के पानी की समस्या को हल करने के लिए", "वनराज चावड़ा ने एक किला बनाने के लिए", "मुजफ्फर शाह ने जीत का जश्न मनाने के लिए"],
  options_gu=["રાજમાતા મીનલદેવીએ કર ઉઘરાવવા માટે", "રાણી ઉદયમતીએ પીવાના પાણીની સમસ્યા હલ કરવા માટે", "વનરાજ ચાવડાએ કિલ્લો બનાવવા માટે", "મુઝફ્ફર શાહે જીતની ઉજવણી કરવા માટે"],
  correct_index=1,
  explanation="Udayamati, queen of King Bhimdev I, built Rani ki Vav to solve the severe drinking water problem in Patan.",
  explanation_hi="राजा भीमदेव प्रथम की रानी उदयमती ने पाटन में पीने के पानी की गंभीर समस्या को हल करने के लिए रानी की वाव का निर्माण किया।",
  explanation_gu="રાજા ભીમદેવ પ્રથમની રાણી ઉદયમતીએ પાટણમાં પીવાના પાણીની ગંભીર સમસ્યા હલ કરવા રાણી ની વાવ બનાવી.",
  id="KOBJ_CLAS7_SSCI_CH1_MCQ_002")

# Ex Q1: Who founded Anhilwad Patan?
b("mcq",
  question="Who founded Anhilwad Patan on the banks of the Saraswati River in 746 AD?",
  question_hi="746 ईस्वी में सरस्वती नदी के तट पर अन्हिलवाड़ पाटन की स्थापना किसने की?",
  question_gu="746 એડીમાં સરસ્વતી નદીના કિનારે અણહિલવાડ પાટણની સ્થાપના કોણે કરી?",
  options=["King Bhimdev I", "Siddharaj Jaisinh", "Vanraj Chavda", "Muzaffar Shah"],
  options_hi=["राजा भीमदेव प्रथम", "सिद्धराज जयसिंह", "वनराज चावड़ा", "मुजफ्फर शाह"],
  options_gu=["રાજા ભીમદેવ પ્રથમ", "સિદ્ધરાજ જયસિંહ", "વનરાજ ચાવડા", "મુઝફ્ફર શાહ"],
  correct_index=2,
  explanation="Vanraj Chavda founded Anhilwad Patan in 746 AD.",
  explanation_hi="वनराज चावड़ा ने 746 ईस्वी में अन्हिलवाड़ पाटन की स्थापना की।",
  explanation_gu="વનરાજ ચાવડાએ 746 એડીમાં અણહિલવાડ પાટણની સ્થાપના કરી.",
  id="KOBJ_CLAS7_SSCI_CH1_MCQ_003")

b("theory",
  title="Public Welfare Works of Rajmata Minaldevi", title_hi="राजमाता मीनलदेवी के जनकल्याण कार्य", title_gu="રાજમાતા મીનલદેવીના લોકકલ્યાણ કાર્યો",
  body="Rajmata Minaldevi, mother of Siddharaj Jaisinh, was an ideal and benevolent queen. She abolished the pilgrim tax collected from devotees visiting the sacred Somnath Temple! She also built Malav Lake in Dholka and Munsar Lake in Viramgam to solve severe drinking water scarcities.",
  body_hi="सिद्धराज जयसिंह की माँ, राजमाता मीनलदेवी, एक आदर्श और परोपकारी रानी थीं। उन्होंने पवित्र सोमनाथ मंदिर जाने वाले भक्तों से लिया जाने वाला तीर्थ यात्रा कर समाप्त कर दिया! उन्होंने पीने के पानी की गंभीर समस्याओं को हल करने के लिए ढोलका में मालव झील और वीरमगाम में मुनसर झील का भी निर्माण किया।",
  body_gu="સિદ્ધરાજ જયસિંહની માતા, રાજમાતા મીનલદેવી, એક આદર્શ અને પરોપકારી રાણી હતા. તેમણે પવિત્ર સોમનાથ મંદિરની મુલાકાત લેતા ભક્તો પાસેથી લેવામાં આવતો યાત્રા વેરો નાબૂદ કર્યો! તેમણે પીવાના પાણીની ગંભીર સમસ્યાઓ હલ કરવા માટે ધોળકામાં માલવ તળાવ અને વિરમગામમાં મુનસર તળાવ પણ બનાવ્યું.",
  id="KOBJ_CLAS7_SSCI_CH1_THEO_003")

# Ex Q2: Public Welfare Works of Rajmata Minaldevi
b("mcq",
  question="Which of the following is a public welfare work done by Rajmata Minaldevi?",
  question_hi="निम्नलिखित में से कौन सा राजमाता मीनलदेवी द्वारा किया गया जनकल्याण कार्य है?",
  question_gu="નીચેનામાંથી કયું રાજમાતા મીનલદેવી દ્વારા કરવામાં આવેલ લોકકલ્યાણ કાર્ય છે?",
  options=["She built the Rani ki Vav", "She abolished the pilgrim tax at Somnath Temple", "She fought wars against foreign invaders", "She founded the city of Anhilwad Patan"],
  options_hi=["उन्होंने रानी की वाव का निर्माण किया", "उन्होंने सोमनाथ मंदिर में तीर्थ यात्रा कर समाप्त कर दिया", "उन्होंने विदेशी आक्रमणकारियों के खिलाफ युद्ध लड़े", "उन्होंने अन्हिलवाड़ पाटन शहर की स्थापना की"],
  options_gu=["તેમણે રાણી ની વાવ બનાવી", "તેમણે સોમનાથ મંદિરમાં યાત્રા વેરો નાબૂદ કર્યો", "તેમણે વિદેશી આક્રમણકારો સામે યુદ્ધ લડ્યા", "તેમણે અણહિલવાડ પાટણ શહેરની સ્થાપના કરી"],
  correct_index=1,
  explanation="Rajmata Minaldevi was known for justice. She waived the pilgrim tax and built lakes like Malav and Munsar.",
  explanation_hi="राजमाता मीनलदेवी न्याय के लिए जानी जाती थीं। उन्होंने तीर्थ यात्रा कर माफ कर दिया और मालव और मुनसर जैसी झीलों का निर्माण किया।",
  explanation_gu="રાજમાતા મીનલદેવી ન્યાય માટે જાણીતા હતા. તેમણે યાત્રા વેરો માફ કર્યો અને માલવ અને મુનસર જેવા તળાવો બનાવ્યા.",
  id="KOBJ_CLAS7_SSCI_CH1_MCQ_004")

b("theory",
  title="The Sultanate Period", title_hi="सल्तनत काल", title_gu="સલ્તનત કાળ",
  body="After the end of Rajput rule in Gujarat, the Sultanate period began. The first independent Sultan of Gujarat was Muzaffar Shah (whose original name was Zafar Khan).",
  body_hi="गुजरात में राजपूत शासन के अंत के बाद, सल्तनत काल शुरू हुआ। गुजरात के पहले स्वतंत्र सुल्तान मुजफ्फर शाह (जिनका मूल नाम जफर खान था) थे।",
  body_gu="ગુજરાતમાં રાજપૂત શાસનના અંત પછી, સલ્તનત કાળ શરૂ થયો. ગુજરાતના પ્રથમ સ્વતંત્ર સુલતાન મુઝફ્ફર શાહ (જેમનું મૂળ નામ ઝફર ખાન હતું) હતા.",
  id="KOBJ_CLAS7_SSCI_CH1_THEO_004")

# Ex Q1: First Sultan of Gujarat
b("mcq",
  question="Who was the first independent Sultan of Gujarat?",
  question_hi="गुजरात का पहला स्वतंत्र सुल्तान कौन था?",
  question_gu="ગુજરાતના પ્રથમ સ્વતંત્ર સુલતાન કોણ હતા?",
  options=["Zafar Khan (Muzaffar Shah)", "Ahmed Shah", "Mahmud Begada", "Qutubuddin Aibak"],
  options_hi=["जफर खान (मुजफ्फर शाह)", "अहमद शाह", "महमूद बेगड़ा", "कुतुबुद्दीन ऐबक"],
  options_gu=["ઝફર ખાન (મુઝફ્ફર શાહ)", "અહેમદ શાહ", "મહમૂદ બેગડા", "કુતુબુદ્દીન ઐબક"],
  correct_index=0,
  explanation="Muzaffar Shah, originally named Zafar Khan, was the first independent Sultan of Gujarat.",
  explanation_hi="मुजफ्फर शाह, जिनका मूल नाम जफर खान था, गुजरात के पहले स्वतंत्र सुल्तान थे।",
  explanation_gu="મુઝફ્ફર શાહ, જેનું મૂળ નામ ઝફર ખાન હતું, ગુજરાતના પ્રથમ સ્વતંત્ર સુલતાન હતા.",
  id="KOBJ_CLAS7_SSCI_CH1_MCQ_005")

# TOPIC 3: Trade and Administration
b("discovery",
  title="Money and Markets", title_hi="धन और बाज़ार", title_gu="નાણાં અને બજારો",
  body="How did these large kingdoms get money to build massive stepwells and lakes? They collected taxes! But they didn't collect modern paper money. Farmers had to give a part of their crops to the king.",
  body_hi="इन बड़े राज्यों को विशाल बावड़ियों और झीलों के निर्माण के लिए धन कैसे मिला? उन्होंने कर एकत्र किया! लेकिन उन्होंने आधुनिक कागजी मुद्रा एकत्र नहीं की। किसानों को अपनी फसलों का एक हिस्सा राजा को देना पड़ता था।",
  body_gu="આ મોટા રાજ્યોને વિશાળ વાવ અને તળાવો બનાવવા માટે પૈસા કેવી રીતે મળ્યા? તેઓએ કર વસૂલ કર્યો! પરંતુ તેઓએ આધુનિક કાગળના નાણાં એકત્રિત કર્યા ન હતા. ખેડૂતોએ તેમના પાકનો એક ભાગ રાજાને આપવો પડતો હતો.",
  id="KOBJ_CLAS7_SSCI_CH1_DISC_002")

b("theory",
  title="Trade and Administration", title_hi="व्यापार और प्रशासन", title_gu="વેપાર અને વહીવટ",
  body="The state revenue was managed strictly. The primary land tax was called 'Bhag', which was usually 1/6th of the total agricultural produce. Taxes were actively collected at three main points: city check-posts, irrigation facilities, and trading ports.\n\nGujarat was rich because of international overseas trade! The biggest trading ports were Khambhat (Stambhtirth) and Bharuch (Bhrigukachchha).",
  body_hi="राज्य के राजस्व का कड़ाई से प्रबंधन किया जाता था। प्राथमिक भूमि कर को 'भाग' कहा जाता था, जो आमतौर पर कुल कृषि उपज का 1/6 वां हिस्सा होता था। शहर की चौकियों, सिंचाई सुविधाओं और व्यापारिक बंदरगाहों पर कर सक्रिय रूप से एकत्र किए जाते थे।\n\nअंतर्राष्ट्रीय विदेशी व्यापार के कारण गुजरात समृद्ध था! सबसे बड़े व्यापारिक बंदरगाह खंभात (स्तंभतीर्थ) और भरूच (भृगुकच्छ) थे।",
  body_gu="રાજ્યની આવકનું કડક સંચાલન થતું હતું. પ્રાથમિક જમીન કરને 'ભાગ' કહેવામાં આવતો હતો, જે સામાન્ય રીતે કુલ ખેતીના ઉત્પાદનનો 1/6મો ભાગ હતો. શહેરની ચેકપોસ્ટ, સિંચાઈ સુવિધાઓ અને વેપારી બંદરો પર કર સક્રિય રીતે વસૂલવામાં આવતા હતા.\n\nઆંતરરાષ્ટ્રીય વિદેશી વેપારને કારણે ગુજરાત સમૃદ્ધ હતું! સૌથી મોટા વેપારી બંદરો ખંભાત (સ્તંભતીર્થ) અને ભરૂચ (ભૃગુકચ્છ) હતા.",
  id="KOBJ_CLAS7_SSCI_CH1_THEO_005")

# Ex Q2: Trade and commerce
b("mcq",
  question="During the Rajput era, what was the primary land tax called, and how much was it?",
  question_hi="राजपूत काल के दौरान, प्राथमिक भूमि कर को क्या कहा जाता था, और वह कितना था?",
  question_gu="રાજપૂત યુગ દરમિયાન, પ્રાથમિક જમીન કરને શું કહેવામાં આવતું હતું, અને તે કેટલો હતો?",
  options=["'Tax' - 1/4th of produce", "'Bhag' - 1/6th of produce", "'Lagaan' - 1/2 of produce", "'Zakat' - 1/10th of produce"],
  options_hi=["'कर' - उपज का 1/4 हिस्सा", "'भाग' - उपज का 1/6 हिस्सा", "'लगान' - उपज का 1/2 हिस्सा", "'जकात' - उपज का 1/10 हिस्सा"],
  options_gu=["'કર' - ઉત્પાદનનો 1/4 ભાગ", "'ભાગ' - ઉત્પાદનનો 1/6 ભાગ", "'લગાન' - ઉત્પાદનનો 1/2 ભાગ", "'ઝકાત' - ઉત્પાદનનો 1/10 ભાગ"],
  correct_index=1,
  explanation="The primary land tax collected was known as 'Bhag', which amounted to 1/6th of the agricultural produce.",
  explanation_hi="प्राथमिक भूमि कर को 'भाग' के रूप में जाना जाता था, जो कृषि उपज का 1/6 वां हिस्सा था।",
  explanation_gu="પ્રાથમિક જમીન કર 'ભાગ' તરીકે ઓળખાતો હતો, જે ખેતીના ઉત્પાદનના 1/6મો ભાગ હતો.",
  id="KOBJ_CLAS7_SSCI_CH1_MCQ_006")

b("mcq",
  question="Which two cities served as prominent international sea ports in Gujarat during this era?",
  question_hi="इस युग के दौरान गुजरात में किन दो शहरों ने प्रमुख अंतर्राष्ट्रीय समुद्री बंदरगाहों के रूप में काम किया?",
  question_gu="આ યુગ દરમિયાન ગુજરાતમાં કયા બે શહેરો પ્રમુખ આંતરરાષ્ટ્રીય દરિયાઈ બંદરો તરીકે કામ કરતા હતા?",
  options=["Ahmedabad and Surat", "Khambhat and Bharuch", "Rajkot and Jamnagar", "Bhavnagar and Porbandar"],
  options_hi=["अहमदाबाद और सूरत", "खंभात और भरूच", "राजकोट और जामनगर", "भावनगर और पोरबंदर"],
  options_gu=["અમદાવાદ અને સુરત", "ખંભાત અને ભરૂચ", "રાજકોટ અને જામનગર", "ભાવનગર અને પોરબंदर"],
  correct_index=1,
  explanation="Khambhat (Stambhtirth) and Bharuch (Bhrigukachchha) were the thriving overseas trade hubs.",
  explanation_hi="खंभात (स्तंभतीर्थ) और भरूच (भृगुकच्छ) संपन्न विदेशी व्यापार केंद्र थे।",
  explanation_gu="ખંભાત (સ્તંભતીર્થ) અને ભરૂચ (ભૃગુકચ્છ) સમૃદ્ધ વિદેશી વેપાર કેન્દ્રો હતા.",
  id="KOBJ_CLAS7_SSCI_CH1_MCQ_007")

# TOPIC 4: South India & Match the Columns
b("theory",
  title="Major Dynasties of South India", title_hi="दक्षिण भारत के प्रमुख राजवंश", title_gu="દક્ષિણ ભારતના પ્રમુખ રાજવંશો",
  body="While Rajputs ruled the North, powerful empires controlled the South. Three major dynasties of South India during the medieval period were the Chalukya dynasty, the Pallava dynasty (ruled from Kanchi), and the Chola dynasty. There were also the Rashtrakutas (ruling from Manyakheta). \n\nDifferent dynasties ruled specific regions: Sen Dynasty ruled Bengal, Solankis ruled Gujarat, and Chauhans ruled Shakambhari (Ajmer).",
  body_hi="जबकि राजपूत उत्तर पर शासन करते थे, शक्तिशाली साम्राज्यों ने दक्षिण को नियंत्रित किया। मध्ययुगीन काल के दौरान दक्षिण भारत के तीन प्रमुख राजवंश चालुक्य राजवंश, पल्लव राजवंश (कांची से शासित) और चोल राजवंश थे। राष्ट्रकूट (मान्यखेत से शासन करने वाले) भी थे।\n\nविभिन्न राजवंशों ने विशिष्ट क्षेत्रों पर शासन किया: सेन राजवंश ने बंगाल पर शासन किया, सोलंकियों ने गुजरात पर और चौहानों ने शाकम्भरी (अजमेर) पर शासन किया।",
  body_gu="જ્યારે રાજપૂતોએ ઉત્તર પર શાસન કર્યું, શક્તિશાળી સામ્રાજ્યોએ દક્ષિણને નિયંત્રિત કર્યું. મધ્યયુગીન કાળ દરમિયાન દક્ષિણ ભારતના ત્રણ પ્રમુખ રાજવંશો ચાલુક્ય રાજવંશ, પલ્લવ રાજવંશ (કાંચીથી શાસન કરતા) અને ચોલ રાજવંશ હતા. રાષ્ટ્રકૂટ (માન્યખેટથી શાસન કરતા) પણ હતા.\n\nવિવિધ રાજવંશોએ ચોક્કસ પ્રદેશો પર શાસન કર્યું: સેન રાજવંશે બંગાળ પર શાસન કર્યું, સોલંકીઓએ ગુજરાત પર અને ચૌહાણોએ શાકંભરી (અજમેર) પર શાસન કર્યું.",
  id="KOBJ_CLAS7_SSCI_CH1_THEO_006")

# Ex Q1: Three major dynasties of South India
b("mcq",
  question="Name any three major dynasties of South India during the medieval period.",
  question_hi="मध्ययुगीन काल के दौरान दक्षिण भारत के किन्हीं तीन प्रमुख राजवंशों के नाम बताइए।",
  question_gu="મધ્યયુગીન કાળ દરમિયાન દક્ષિણ ભારતના કોઈપણ ત્રણ પ્રમુખ રાજવંશોના નામ આપો.",
  options=["Solanki, Chauhan, and Chavda", "Chalukya, Pallava, and Chola", "Mughal, Maurya, and Gupta", "Sen, Paramara, and Pratihara"],
  options_hi=["सोलंकी, चौहान, और चावड़ा", "चालुक्य, पल्लव, और चोल", "मुगल, मौर्य, और गुप्त", "सेन, परमार, और प्रतिहार"],
  options_gu=["સોલંકી, ચૌહાણ, અને ચાવડા", "ચાલુક્ય, પલ્લવ, અને ચોલ", "મુઘલ, મૌર્ય, અને ગુપ્ત", "સેન, પરમાર, અને પ્રતિહાર"],
  correct_index=1,
  explanation="The major dynasties of South India were Chalukya, Pallava, and Chola (also Chera, Pandya, Rashtrakuta).",
  explanation_hi="दक्षिण भारत के प्रमुख राजवंश चालुक्य, पल्लव और चोल थे।",
  explanation_gu="દક્ષિણ ભારતના પ્રમુખ રાજવંશો ચાલુક્ય, પલ્લવ અને ચોલ હતા.",
  id="KOBJ_CLAS7_SSCI_CH1_MCQ_008")

# Ex Q3: Match the columns correctly
b("activity",
  content="**Mastery Challenge: Match the Kingdom**\n\nCan you correctly match these dynasties to the state or region they ruled?\n\n1. Sen Dynasty\n2. Solanki Dynasty\n3. Pallava Dynasty\n4. Rashtrakuta Dynasty\n5. Chauhan Dynasty\n\n**Regions to match:** Gujarat, Kanchi, Shakambhari (Ajmer), Bengal, Manyakheta.\n\n*Check your answers! (Sen -> Bengal, Solanki -> Gujarat, Pallava -> Kanchi, Rashtrakuta -> Manyakheta, Chauhan -> Shakambhari)*",
  id="KOBJ_CLAS7_SSCI_CH1_ACTI_001")


with open('app_core/chapters/gseb_class7_social_science_ch1.json', 'w', encoding='utf-8') as f:
    json.dump(blocks, f, indent=2, ensure_ascii=False)

print("Rajput Age JSON generated successfully!")
