import json

file_path = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class11_spcc_part1_ch3.json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

new_blocks = [
    {
        "type": "numerical",
        "question": "What kind of quality paper is used for commercial letter writing? Why?",
        "question_hi": "व्यावसायिक पत्र लेखन के लिए किस प्रकार के गुणवत्ता वाले कागज का उपयोग किया जाता है? क्यों?",
        "question_gu": "વાણિજ્યિક પત્ર લેખન માટે કયા પ્રકારના ગુણવત્તાવાળા કાગળનો ઉપયોગ થાય છે? શા માટે?",
        "solution": "High-quality paper is used for commercial letter writing. \n\nReason: A business letter represents the company. High-quality paper leaves a positive impression on the receiver and reflects professionalism. Furthermore, poor-quality paper can cause ink to spread (blotting) making the letter unreadable, and it may tear easily while filing or during transportation.",
        "solution_hi": "व्यावसायिक पत्र लेखन के लिए उच्च गुणवत्ता वाले कागज का उपयोग किया जाता है।\n\nकारण: एक व्यावसायिक पत्र कंपनी का प्रतिनिधित्व करता है। उच्च गुणवत्ता वाला कागज प्राप्तकर्ता पर सकारात्मक प्रभाव छोड़ता है और व्यावसायिकता (professionalism) को दर्शाता है। इसके अलावा, खराब गुणवत्ता वाले कागज के कारण स्याही फैल सकती है जिससे पत्र अपठनीय हो जाता है, और फाइल करते समय या परिवहन के दौरान यह आसानी से फट सकता है।",
        "solution_gu": "વાણિજ્યિક પત્ર લેખન માટે ઉચ્ચ ગુણવત્તાવાળા કાગળનો ઉપયોગ થાય છે.\n\nકારણ: વાણિજ્યિક પત્ર કંપનીનું પ્રતિનિધિત્વ કરે છે. ઉચ્ચ ગુણવત્તાવાળો કાગળ મેળવનાર પર સકારાત્મક છાપ છોડે છે અને વ્યાવસાયિકતા (professionalism) દર્શાવે છે. વધુમાં, નબળી ગુણવત્તાવાળા કાગળને કારણે શાહી ફેલાઈ શકે છે જે પત્રને વાંચી ન શકાય તેવો બનાવે છે, અને ફાઇલ કરતી વખતે અથવા પરિવહન દરમિયાન તે સરળતાથી ફાટી શકે છે.",
        "id": "KOBJ_GSEB_11SPCC_P1C3_NUME_005"
    },
    {
        "type": "numerical",
        "question": "On which side of the letter is the margin kept and what size is it?",
        "question_hi": "पत्र के किस ओर हाशिया (margin) रखा जाता है और उसका आकार क्या होता है?",
        "question_gu": "પત્રની કઈ બાજુએ માર્જિન (margin) રાખવામાં આવે છે અને તેનું કદ કેટલું હોય છે?",
        "solution": "Margins are kept on all four sides of the letter, but mostly on the left and right sides.\n- **Left Margin:** Usually 1.5 inches. A broader margin is kept on the left side so that the text doesn't get hidden or torn when the letter is punched and filed.\n- **Right Margin:** Usually 1 inch.\n- **Top and Bottom Margins:** Typically 1 inch to 1.5 inches to make the letter look balanced and attractive.",
        "solution_hi": "हाशिये (Margins) पत्र के चारों तरफ रखे जाते हैं, लेकिन मुख्य रूप से बाईं और दाईं ओर।\n- **बायां हाशिया (Left Margin):** आमतौर पर 1.5 इंच। बाईं ओर एक चौड़ा हाशिया रखा जाता है ताकि जब पत्र को पंच और फाइल किया जाए तो पाठ (text) छिप न जाए या फट न जाए।\n- **दायां हाशिया (Right Margin):** आमतौर पर 1 इंच।\n- **ऊपर और नीचे का हाशिया:** पत्र को संतुलित और आकर्षक बनाने के लिए आम तौर पर 1 इंच से 1.5 इंच तक रखा जाता है।",
        "solution_gu": "માર્જિન પત્રની ચારેય બાજુએ રાખવામાં આવે છે, પરંતુ મોટે ભાગે ડાબી અને જમણી બાજુએ.\n- **ડાબું માર્જિન (Left Margin):** સામાન્ય રીતે 1.5 ઇંચ. ડાબી બાજુએ વ્યાપક માર્જિન રાખવામાં આવે છે જેથી પત્રને પંચ અને ફાઇલ કરવામાં આવે ત્યારે લખાણ છુપાઈ કે ફાટી ન જાય.\n- **જમણું માર્જિન (Right Margin):** સામાન્ય રીતે 1 ઇંચ.\n- **ઉપર અને નીચેનું માર્જિન:** પત્રને સંતુલિત અને આકર્ષક બનાવવા માટે સામાન્ય રીતે 1 ઇંચ થી 1.5 ઇંચ સુધી રાખવામાં આવે છે.",
        "id": "KOBJ_GSEB_11SPCC_P1C3_NUME_006"
    },
    {
        "type": "numerical",
        "question": "Briefly provide information on the general practice of folding commercial paper.",
        "question_hi": "वाणिज्यिक कागज को मोड़ने (folding) के सामान्य अभ्यास (general practice) के बारे में संक्षेप में जानकारी प्रदान करें।",
        "question_gu": "વાણિજ્યિક કાગળને વાળવાની (folding) સામાન્ય પ્રથા વિશે ટૂંકમાં માહિતી આપો.",
        "solution": "Folding a commercial letter properly ensures it fits perfectly into the envelope without getting crumpled. The general practice is:\n1. The letter should have maximum three to four folds.\n2. The first fold is usually made vertically (leaving a slight margin) so it matches the size of the envelope.\n3. Then, two or three horizontal folds are made to reduce its height.\n4. When folded correctly, the receiver can easily unfold it in sequence without tearing the letter.",
        "solution_hi": "एक व्यावसायिक पत्र को ठीक से मोड़ने से यह सुनिश्चित होता है कि यह बिना सिकुड़े लिफाफे में पूरी तरह से फिट बैठता है। सामान्य अभ्यास है:\n1. पत्र में अधिकतम तीन से चार तह (folds) होनी चाहिए।\n2. पहली तह आमतौर पर लंबवत (vertically) बनाई जाती है (थोड़ा हाशिया छोड़कर) ताकि यह लिफाफे के आकार से मेल खाए।\n3. फिर, इसकी ऊंचाई कम करने के लिए दो या तीन क्षैतिज (horizontal) तह बनाई जाती हैं।\n4. जब इसे सही ढंग से मोड़ा जाता है, तो प्राप्तकर्ता पत्र को फाड़े बिना आसानी से इसे क्रम में खोल सकता है।",
        "solution_gu": "વાણિજ્યિક પત્રને યોગ્ય રીતે વાળવાથી તે કરચલી પડ્યા વિના પરબીડિયામાં સંપૂર્ણ રીતે બંધબેસે છે. સામાન્ય પ્રથા છે:\n1. પત્રમાં વધુમાં વધુ ત્રણથી ચાર ગડી (folds) હોવી જોઈએ.\n2. પહેલી ગડી સામાન્ય રીતે ઊભી (vertically) બનાવવામાં આવે છે (થોડું માર્જિન છોડીને) જેથી તે પરબીડિયાના કદ સાથે મેળ ખાય.\n3. પછી, તેની ઊંચાઈ ઘટાડવા માટે બે કે ત્રણ આડી (horizontal) ગડી બનાવવામાં આવે છે.\n4. જ્યારે તેને યોગ્ય રીતે વાળવામાં આવે છે, ત્યારે મેળવનાર પત્ર ફાટ્યા વિના સરળતાથી તેને ક્રમમાં ખોલી શકે છે.",
        "id": "KOBJ_GSEB_11SPCC_P1C3_NUME_007"
    },
    {
        "type": "numerical",
        "question": "Briefly explain the important parts of the writing on the envelope.",
        "question_hi": "लिफाफे पर लिखे जाने वाले महत्वपूर्ण भागों की संक्षेप में व्याख्या कीजिए।",
        "question_gu": "પરબીડિયા પર લખાણના મહત્વપૂર્ણ ભાગો ટૂંકમાં સમજાવો.",
        "solution": "The writing on the envelope must be clear and accurate to ensure proper delivery. Important parts include:\n1. **Receiver's Address:** Written in the center or slightly to the right side. It includes the receiver's name, designation, company name, address, and Pin code.\n2. **Sender's Address:** Written on the top-left corner or at the back flap of the envelope, so the letter can be returned if undelivered.\n3. **Mailing Instructions:** Instructions like \"By Speed Post\", \"By Registered AD\", \"Urgent\", or \"Personal\" are written on the top right corner.\n4. **Postage Stamps:** Affixed on the top right corner.",
        "solution_hi": "उचित डिलीवरी सुनिश्चित करने के लिए लिफाफे पर लिखावट स्पष्ट और सटीक होनी चाहिए। महत्वपूर्ण भागों में शामिल हैं:\n1. **प्राप्तकर्ता का पता:** केंद्र में या थोड़ा दाईं ओर लिखा जाता है। इसमें प्राप्तकर्ता का नाम, पदनाम, कंपनी का नाम, पता और पिन कोड शामिल है।\n2. **प्रेषक का पता:** लिफाफे के ऊपरी-बाएं कोने में या पीछे की तरफ लिखा जाता है, ताकि यदि पत्र वितरित नहीं होता है तो उसे वापस किया जा सके।\n3. **मेलिंग निर्देश:** \"बाय स्पीड पोस्ट\", \"बाय रजिस्टर्ड एडी\", \"अर्जेंट\" या \"पर्सनल\" जैसे निर्देश ऊपर दाईं ओर लिखे जाते हैं।\n4. **डाक टिकट:** ऊपर दाईं ओर चिपकाए जाते हैं।",
        "solution_gu": "યોગ્ય ડિલિવરી સુનિશ્ચિત કરવા માટે પરબીડિયા પર લખાણ સ્પષ્ટ અને સચોટ હોવું જોઈએ. મહત્વપૂર્ણ ભાગોમાં શામેલ છે:\n1. **મેળવનારનું સરનામું:** મધ્યમાં અથવા સહેજ જમણી બાજુએ લખાયેલું. તેમાં મેળવનારનું નામ, હોદ્દો, કંપનીનું નામ, સરનામું અને પિન કોડ શામેલ છે.\n2. **મોકલનારનું સરનામું:** પરબીડિયાના ઉપરના ડાબા ખૂણે અથવા પાછળના ભાગે લખેલું, જેથી જો પત્ર વિતરિત ન થાય તો તેને પાછો આપી શકાય.\n3. **મેઇલિંગ સૂચનાઓ:** \"બાય સ્પીડ પોસ્ટ\", \"બાય રજિસ્ટર્ડ એડી\", \"અર્જન્ટ\" અથવા \"પર્સનલ\" જેવી સૂચનાઓ ઉપરના જમણા ખૂણે લખવામાં આવે છે.\n4. **ટપાલ ટિકિટ:** ઉપર જમણા ખૂણે ચોંટાડવામાં આવે છે.",
        "id": "KOBJ_GSEB_11SPCC_P1C3_NUME_008"
    },
    {
        "type": "numerical",
        "question": "Name the different types of envelopes.",
        "question_hi": "विभिन्न प्रकार के लिफाफों के नाम बताइए।",
        "question_gu": "વિવિધ પ્રકારના પરબીડિયાના નામ જણાવો.",
        "solution": "The main types of envelopes used in commercial correspondence are:\n1. Window Envelope\n2. Closed Envelope\n3. Open Rectangular Envelope",
        "solution_hi": "व्यावसायिक पत्राचार में उपयोग किए जाने वाले मुख्य प्रकार के लिफाफे हैं:\n1. विंडो लिफाफा (Window Envelope)\n2. बंद लिफाफा (Closed Envelope)\n3. खुला आयताकार लिफाफा (Open Rectangular Envelope)",
        "solution_gu": "વાણિજ્યિક પત્રવ્યવહારમાં વપરાતા મુખ્ય પ્રકારના પરબીડિયા નીચે મુજબ છે:\n1. બારીવાળું પરબીડિયું (Window Envelope)\n2. બંધ પરબીડિયું (Closed Envelope)\n3. ખુલ્લું લંબચોરસ પરબીડિયું (Open Rectangular Envelope)",
        "id": "KOBJ_GSEB_11SPCC_P1C3_NUME_009"
    },
    {
        "type": "numerical",
        "question": "When are windowed envelopes, closed envelopes and open rectangular envelopes used?",
        "question_hi": "विंडो लिफाफे, बंद लिफाफे और खुले आयताकार लिफाफे का उपयोग कब किया जाता है?",
        "question_gu": "બારીવાળા પરબીડિયા, બંધ પરબીડિયા અને ખુલ્લા લંબચોરસ પરબીડિયાનો ઉપયોગ ક્યારે થાય છે?",
        "solution": "1. **Window Envelopes:** Used mostly by banks, insurance companies, and mutual funds for sending bills or statements. They have a transparent cut-out so the receiver's address printed on the letter is visible, saving the time required to write the address again on the envelope.\n2. **Closed Envelopes:** Used for sending regular and confidential business letters. The flap is completely sealed to maintain privacy.\n3. **Open Rectangular Envelopes:** Used for sending circulars, greeting cards, or printed matters. Since they are not fully sealed, postal charges for these envelopes are comparatively lower.",
        "solution_hi": "1. **विंडो लिफाफे (Window Envelopes):** बिल या स्टेटमेंट भेजने के लिए ज्यादातर बैंकों, बीमा कंपनियों और म्यूचुअल फंड द्वारा उपयोग किया जाता है। इनमें एक पारदर्शी कट-आउट होता है जिससे पत्र पर छपा प्राप्तकर्ता का पता दिखाई देता है, जिससे लिफाफे पर दोबारा पता लिखने में लगने वाला समय बचता है।\n2. **बंद लिफाफे (Closed Envelopes):** नियमित और गोपनीय व्यावसायिक पत्र भेजने के लिए उपयोग किया जाता है। गोपनीयता बनाए रखने के लिए इसे पूरी तरह से सील कर दिया जाता है।\n3. **खुले आयताकार लिफाफे (Open Rectangular Envelopes):** परिपत्र (circulars), ग्रीटिंग कार्ड या मुद्रित सामग्री भेजने के लिए उपयोग किया जाता है। चूंकि वे पूरी तरह से सील नहीं होते हैं, इसलिए इन लिफाफों के लिए डाक शुल्क तुलनात्मक रूप से कम होता है।",
        "solution_gu": "1. **બારીવાળા પરબીડિયા (Window Envelopes):** બિલ અથવા સ્ટેટમેન્ટ મોકલવા માટે મોટે ભાગે બેંકો, વીમા કંપનીઓ અને મ્યુચ્યુઅલ ફંડ દ્વારા ઉપયોગમાં લેવાય છે. તેમાં પારદર્શક કટ-આઉટ હોય છે જેથી પત્ર પર છાપેલ મેળવનારનું સરનામું જોઈ શકાય છે, અને પરબીડિયા પર ફરીથી સરનામું લખવાનો સમય બચે છે.\n2. **બંધ પરબીડિયા (Closed Envelopes):** નિયમિત અને ગોપનીય વાણિજ્યિક પત્રો મોકલવા માટે વપરાય છે. ગોપનીયતા જાળવવા માટે તેને સંપૂર્ણપણે સીલ કરવામાં આવે છે.\n3. **ખુલ્લા લંબચોરસ પરબીડિયા (Open Rectangular Envelopes):** પરિપત્રો, ગ્રીટિંગ કાર્ડ્સ અથવા મુદ્રિત બાબતો મોકલવા માટે વપરાય છે. કારણ કે તે સંપૂર્ણપણે સીલ કરેલા નથી, આ પરબીડિયા માટે ટપાલ ખર્ચ તુલનાત્મક રીતે ઓછો હોય છે.",
        "id": "KOBJ_GSEB_11SPCC_P1C3_NUME_010"
    }
]

data['blocks'].extend(new_blocks)

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Part 1 Chapter 3 updated with user questions!")
