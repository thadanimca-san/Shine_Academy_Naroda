import json

file_path = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class11_spcc_part2_ch4.json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

new_blocks = [
    {
        "type": "numerical",
        "question": "Ashoka Company wants to move its registered office from Bapunagar area of Ahmedabad to Satellite area of Ahmedabad, so what process does the company have to go through?",
        "question_hi": "अशोका कंपनी अपना पंजीकृत कार्यालय अहमदाबाद के बापू नगर क्षेत्र से अहमदाबाद के सैटेलाइट क्षेत्र में ले जाना चाहती है, तो कंपनी को किस प्रक्रिया से गुजरना होगा?",
        "question_gu": "અશોકા કંપની તેની નોંધાયેલ ઓફિસ અમદાવાદના બાપુનગર વિસ્તારમાંથી અમદાવાદના સેટેલાઇટ વિસ્તારમાં ખસેડવા માંગે છે, તો કંપનીએ કઈ પ્રક્રિયામાંથી પસાર થવું પડશે?",
        "solution": "Moving the registered office from one area to another within the same city (e.g., Bapunagar to Satellite in Ahmedabad) is a simple internal process.\nThe company just needs to pass a resolution in the Board of Directors meeting. After passing the resolution, the company must inform the Registrar of Companies about the new address within 15 days.",
        "solution_hi": "पंजीकृत कार्यालय को एक ही शहर के भीतर एक क्षेत्र से दूसरे क्षेत्र (जैसे अहमदाबाद में बापू नगर से सैटेलाइट) में ले जाना एक सरल आंतरिक प्रक्रिया है।\nकंपनी को केवल निदेशक मंडल (Board of Directors) की बैठक में एक प्रस्ताव पारित करने की आवश्यकता है। प्रस्ताव पारित होने के 15 दिनों के भीतर, कंपनी को नए पते के बारे में कंपनी रजिस्ट्रार को सूचित करना होगा।",
        "solution_gu": "નોંધાયેલ ઓફિસને સમાન શહેરની અંદર એક વિસ્તારમાંથી બીજા વિસ્તારમાં ખસેડવી (જેમ કે અમદાવાદમાં બાપુનગરથી સેટેલાઇટ) એ એક સરળ આંતરિક પ્રક્રિયા છે.\nકંપનીએ બોર્ડ ઓફ ડિરેક્ટર્સની મીટિંગમાં માત્ર એક ઠરાવ પસાર કરવાની જરૂર છે. ઠરાવ પસાર કર્યા પછી, કંપનીએ 15 દિવસની અંદર કંપનીઓના રજિસ્ટ્રારને નવા સરનામા વિશે જાણ કરવી પડશે.",
        "id": "KOBJ_GSEB_11SPCC_P2C4_NUME_007"
    },
    {
        "type": "numerical",
        "question": "How can Liability Clause be changed?",
        "question_hi": "दायित्व खंड (Liability Clause) को कैसे बदला जा सकता है?",
        "question_gu": "જવાબદારીની કલમ (Liability Clause) કેવી રીતે બદલી શકાય?",
        "solution": "The Liability Clause defines the financial risk of the shareholders. Because it directly affects the members, it is the hardest clause to change.\nTo change the Liability Clause, the company must pass a Unanimous Resolution (100% agreement) from all its members in a general meeting. If even a single member objects, this clause cannot be changed.",
        "solution_hi": "दायित्व खंड शेयरधारकों के वित्तीय जोखिम को परिभाषित करता है। क्योंकि यह सीधे सदस्यों को प्रभावित करता है, यह बदलना सबसे कठिन खंड है।\nदायित्व खंड को बदलने के लिए, कंपनी को आम बैठक में अपने सभी सदस्यों से एक सर्वसम्मत प्रस्ताव (Unanimous Resolution - 100% सहमति) पारित करना होगा। यदि एक भी सदस्य आपत्ति करता है, तो इस खंड को नहीं बदला जा सकता है।",
        "solution_gu": "જવાબદારીની કલમ શેરધારકોના નાણાકીય જોખમને વ્યાખ્યાયિત કરે છે. કારણ કે તે સીધી સભ્યોને અસર કરે છે, તેને બદલવી સૌથી મુશ્કેલ કલમ છે.\nજવાબદારીની કલમ બદલવા માટે, કંપનીએ સામાન્ય સભામાં તેના તમામ સભ્યોનો સર્વાનુમતે ઠરાવ (Unanimous Resolution - 100% સંમતિ) પસાર કરવો આવશ્યક છે. જો એક પણ સભ્ય વાંધો ઉઠાવે, તો આ કલમ બદલી શકાતી નથી.",
        "id": "KOBJ_GSEB_11SPCC_P2C4_NUME_008"
    },
    {
        "type": "numerical",
        "question": "\"The most important clause in the Memorandum of Association is considered the Object Clause.\" Explain.",
        "question_hi": "\"संस्था के ज्ञापन (MoA) में सबसे महत्वपूर्ण खंड उद्देश्य खंड (Object Clause) माना जाता है।\" स्पष्ट करें।",
        "question_gu": "\"આવેદનપત્ર (MoA) માં સૌથી મહત્વપૂર્ણ કલમ ઉદ્દેશની કલમ (Object Clause) માનવામાં આવે છે.\" સમજાવો.",
        "solution": "The Object Clause defines the core purpose and business activities of the company. It restricts the company's operational boundaries.\nIt is the most important clause because a company cannot engage in any business activity outside its Object Clause. Any act done beyond these defined objectives is legally termed 'Ultra Vires' (beyond powers) and is completely void.\nThis protects the shareholders' investments, ensuring their money is not used in unapproved, risky businesses.",
        "solution_hi": "उद्देश्य खंड कंपनी के मुख्य उद्देश्य और व्यावसायिक गतिविधियों को परिभाषित करता है। यह कंपनी की परिचालन सीमाओं को प्रतिबंधित करता है।\nयह सबसे महत्वपूर्ण खंड है क्योंकि एक कंपनी अपने उद्देश्य खंड के बाहर किसी भी व्यावसायिक गतिविधि में शामिल नहीं हो सकती है। इन परिभाषित उद्देश्यों से परे किए गए किसी भी कार्य को कानूनी रूप से 'अल्ट्रा वायर्स' (अधिकारों से परे) कहा जाता है और यह पूरी तरह से शून्य है।\nयह शेयरधारकों के निवेश की रक्षा करता है, यह सुनिश्चित करता है कि उनका पैसा अनधिकृत, जोखिम भरे व्यवसायों में उपयोग न हो।",
        "solution_gu": "ઉદ્દેશની કલમ કંપનીનો મુખ્ય હેતુ અને વ્યવસાયિક પ્રવૃત્તિઓને વ્યાખ્યાયિત કરે છે. તે કંપનીની ઓપરેશનલ સીમાઓને પ્રતિબંધિત કરે છે.\nઆ સૌથી મહત્વપૂર્ણ કલમ છે કારણ કે કંપની તેની ઉદ્દેશ કલમની બહાર કોઈપણ વ્યવસાયિક પ્રવૃત્તિમાં સામેલ થઈ શકતી નથી. આ નિર્ધારિત ઉદ્દેશોની બહાર કરવામાં આવેલ કોઈપણ કાર્ય કાયદેસર રીતે 'અલ્ટ્રા વાયર્સ' (સત્તા બહારનું) કહેવાય છે અને તે સંપૂર્ણપણે રદબાતલ છે.\nઆ શેરધારકોના રોકાણોનું રક્ષણ કરે છે, તે સુનિશ્ચિત કરે છે કે તેમના નાણાંનો ઉપયોગ અસ્વીકૃત, જોખમી વ્યવસાયોમાં ન થાય.",
        "id": "KOBJ_GSEB_11SPCC_P2C4_NUME_009"
    },
    {
        "type": "numerical",
        "question": "\"For everyone who has a relationship with Binaca Company, the Memorandum of Association of its company is a important documents.\" Explain.",
        "question_hi": "\"बिनाका कंपनी के साथ संबंध रखने वाले हर व्यक्ति के लिए, उसकी कंपनी का संस्था का ज्ञापन (MoA) एक महत्वपूर्ण दस्तावेज है।\" स्पष्ट करें।",
        "question_gu": "\"બિનાકા કંપની સાથે સંબંધ ધરાવતા દરેક વ્યક્તિ માટે, તેની કંપનીનું આવેદનપત્ર (MoA) એ એક મહત્વપૂર્ણ દસ્તાવેજ છે.\" સમજાવો.",
        "solution": "The Memorandum of Association (MoA) is a public document. It defines the constitution, powers, and operational boundaries of 'Binaca Company'.\nFor anyone dealing with the company—whether it's an investor buying shares, a bank giving a loan, a supplier providing raw materials, or the general public—the MoA informs them about the company's legal status, its registered office, its financial limits (capital), and what business it is authorized to do.\nTherefore, it acts as a safeguard and a crucial reference document for all stakeholders.",
        "solution_hi": "संस्था का ज्ञापन (MoA) एक सार्वजनिक दस्तावेज है। यह 'बिनाका कंपनी' के संविधान, शक्तियों और परिचालन सीमाओं को परिभाषित करता है।\nकंपनी के साथ व्यवहार करने वाले किसी भी व्यक्ति के लिए—चाहे वह शेयर खरीदने वाला निवेशक हो, ऋण देने वाला बैंक हो, कच्चा माल उपलब्ध कराने वाला आपूर्तिकर्ता हो, या आम जनता हो—MoA उन्हें कंपनी की कानूनी स्थिति, उसके पंजीकृत कार्यालय, उसकी वित्तीय सीमाओं (पूंजी), और उसे कौन सा व्यवसाय करने के लिए अधिकृत किया गया है, के बारे में सूचित करता है।\nइसलिए, यह सभी हितधारकों के लिए एक सुरक्षा उपाय और एक महत्वपूर्ण संदर्भ दस्तावेज के रूप में कार्य करता है।",
        "solution_gu": "આવેદનપત્ર (MoA) એક સાર્વજનિક દસ્તાવેજ છે. તે 'બિનાકા કંપની' ના બંધારણ, સત્તાઓ અને ઓપરેશનલ સીમાઓને વ્યાખ્યાયિત કરે છે.\nકંપની સાથે વ્યવહાર કરતા કોઈપણ વ્યક્તિ માટે—પછી ભલે તે શેર ખરીદતો રોકાણકાર હોય, લોન આપતી બેંક હોય, કાચો માલ પૂરો પાડતો સપ્લાયર હોય, અથવા સામાન્ય જનતા હોય—MoA તેમને કંપનીની કાનૂની સ્થિતિ, તેની નોંધાયેલ ઓફિસ, તેની નાણાકીય મર્યાદાઓ (મૂડી), અને તેને કયો વ્યવસાય કરવા માટે અધિકૃત કરવામાં આવ્યો છે તે વિશે માહિતગાર કરે છે.\nતેથી, તે તમામ હિતધારકો માટે સલામતી અને નિર્ણાયક સંદર્ભ દસ્તાવેજ તરીકે કાર્ય કરે છે.",
        "id": "KOBJ_GSEB_11SPCC_P2C4_NUME_010"
    },
    {
        "type": "numerical",
        "question": "\"Aroma Private Company wants to change its name to Aroma Limited, so what guidance can you give regarding this?",
        "question_hi": "\"एरोमा प्राइवेट कंपनी अपना नाम बदलकर एरोमा लिमिटेड करना चाहती है, तो आप इस संबंध में क्या मार्गदर्शन दे सकते हैं?",
        "question_gu": "\"એરોમા પ્રાઇવેટ કંપની તેનું નામ બદલીને એરોમા લિમિટેડ કરવા માંગે છે, તો આ અંગે તમે શું માર્ગદર્શન આપી શકો?",
        "solution": "The word 'Private' at the end of the name indicates the company is a Private Limited Company. By changing the name to just 'Aroma Limited', the company is effectively changing its legal structure to a Public Limited Company.\nGuidance:\n1. The company cannot just simply erase the word 'Private' from its name board.\n2. It must pass a Special Resolution in a general meeting of shareholders to convert from a Private to a Public company.\n3. It must apply to the Central Government / Registrar of Companies for approval and alter its Memorandum and Articles of Association accordingly.",
        "solution_hi": "नाम के अंत में 'प्राइवेट' शब्द इंगित करता है कि कंपनी एक प्राइवेट लिमिटेड कंपनी है। नाम को केवल 'एरोमा लिमिटेड' में बदलकर, कंपनी प्रभावी रूप से अपनी कानूनी संरचना को पब्लिक लिमिटेड कंपनी में बदल रही है।\nमार्गदर्शन:\n1. कंपनी केवल अपने नाम बोर्ड से 'प्राइवेट' शब्द को मिटा नहीं सकती है।\n2. इसे एक प्राइवेट (Private) से पब्लिक (Public) कंपनी में परिवर्तित करने के लिए शेयरधारकों की आम बैठक में एक विशेष प्रस्ताव (Special Resolution) पारित करना होगा।\n3. इसे मंजूरी के लिए केंद्र सरकार / कंपनी रजिस्ट्रार को आवेदन करना होगा और तदनुसार अपने मेमोरेंडम और आर्टिकल्स ऑफ एसोसिएशन में बदलाव करना होगा।",
        "solution_gu": "નામના અંતે 'પ્રાઇવેટ' શબ્દ સૂચવે છે કે કંપની એક પ્રાઇવેટ લિમિટેડ કંપની છે. નામ બદલીને માત્ર 'એરોમા લિમિટેડ' કરવાથી, કંપની અસરકારક રીતે તેનું કાનૂની માળખું પબ્લિક લિમિટેડ કંપનીમાં બદલી રહી છે.\nમાર્ગદર્શન:\n1. કંપની માત્ર તેના નામ બોર્ડમાંથી 'પ્રાઇવેટ' શબ્દ ભૂંસી શકતી નથી.\n2. પ્રાઇવેટમાંથી પબ્લિક કંપનીમાં રૂપાંતરિત થવા માટે તેણે શેરધારકોની સામાન્ય સભામાં વિશેષ ઠરાવ (Special Resolution) પસાર કરવો પડશે.\n3. તેણે મંજૂરી માટે કેન્દ્ર સરકાર / કંપનીઓના રજિસ્ટ્રારને અરજી કરવી પડશે અને તે મુજબ તેના આવેદનપત્ર અને નિયમનપત્રમાં ફેરફાર કરવો પડશે.",
        "id": "KOBJ_GSEB_11SPCC_P2C4_NUME_011"
    },
    {
        "type": "numerical",
        "question": "To test the knowledge, the subject teacher asks the class representative Sanjay which type of company is exempt from writing the word Limited or Private Limited?",
        "question_hi": "ज्ञान का परीक्षण करने के लिए, विषय शिक्षक कक्षा प्रतिनिधि संजय से पूछते हैं कि किस प्रकार की कंपनी को लिमिटेड या प्राइवेट लिमिटेड शब्द लिखने से छूट दी गई है?",
        "question_gu": "જ્ઞાનની ચકાસણી કરવા માટે, વિષય શિક્ષક વર્ગ પ્રતિનિધિ સંજયને પૂછે છે કે કયા પ્રકારની કંપનીને લિમિટેડ અથવા પ્રાઇવેટ લિમિટેડ શબ્દ લખવામાંથી મુક્તિ આપવામાં આવી છે?",
        "solution": "Sanjay's answer would be:\nCompanies that are formed strictly for promoting art, science, commerce, charity, religion, or sports (non-profit organizations registered under Section 8 of the Companies Act) are exempt from adding the word 'Limited' or 'Private Limited' at the end of their name.\nThis is because their objective is not to make a profit or distribute dividends to their members.",
        "solution_hi": "संजय का उत्तर होगा:\nजो कंपनियाँ विशुद्ध रूप से कला, विज्ञान, वाणिज्य, दान, धर्म या खेल को बढ़ावा देने के लिए बनाई जाती हैं (कंपनी अधिनियम की धारा 8 के तहत पंजीकृत गैर-लाभकारी संगठन), उन्हें अपने नाम के अंत में 'लिमिटेड' या 'प्राइवेट लिमिटेड' शब्द जोड़ने से छूट प्राप्त है।\nऐसा इसलिए है क्योंकि उनका उद्देश्य लाभ कमाना या अपने सदस्यों को लाभांश (dividend) वितरित करना नहीं है।",
        "solution_gu": "સંજયનો જવાબ હશે:\nજે કંપનીઓ શુદ્ધ રીતે કલા, વિજ્ઞાન, વાણિજ્ય, ચેરિટી, ધર્મ અથવા રમતગમતને પ્રોત્સાહન આપવા માટે રચવામાં આવી છે (કંપની ધારાની કલમ 8 હેઠળ નોંધાયેલ બિન-નફાકારક સંસ્થાઓ) તેમને તેમના નામના અંતે 'લિમિટેડ' અથવા 'પ્રાઇવેટ લિમિટેડ' શબ્દ ઉમેરવામાંથી મુક્તિ આપવામાં આવી છે.\nઆ એટલા માટે છે કારણ કે તેમનો ઉદ્દેશ્ય નફો કમાવવાનો કે તેમના સભ્યોને ડિવિડન્ડ વહેંચવાનો નથી.",
        "id": "KOBJ_GSEB_11SPCC_P2C4_NUME_012"
    }
]

data['blocks'].extend(new_blocks)

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Part 2 Chapter 4 updated with user questions!")
