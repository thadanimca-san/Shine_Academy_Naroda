import json

def update_json(file_path, new_blocks):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    data['blocks'].extend(new_blocks)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Updated {file_path} successfully!")

def update_part1_ch5():
    # Adding Adarsh Nivasi and Vinayak Cycle letters
    blocks = [
        {
            "type": "numerical",
            "question": "Adarsh Nivasi Chhatralaya, Kheralu wants to purchase specific furniture from Jay Hind Furniture Mart, Patan. Write a letter on behalf of them inviting quotation for the purchase of specific furniture and terms of payment.",
            "question_hi": "आदर्श निवासी छात्रालय, खेरालू जय हिंद फर्नीचर मार्ट, पाटन से विशिष्ट फर्नीचर खरीदना चाहता है। उनकी ओर से विशिष्ट फर्नीचर की खरीद और भुगतान की शर्तों के लिए कोटेशन आमंत्रित करते हुए एक पत्र लिखें।",
            "question_gu": "આદર્શ નિવાસી છાત્રાલય, ખેરાલુ જય હિંદ ફર્નિચર માર્ટ, પાટણ પાસેથી ચોક્કસ ફર્નિચર ખરીદવા માંગે છે. તેમના વતી ચોક્કસ ફર્નિચરની ખરીદી અને ચુકવણીની શરતો માટે ક્વોટેશન આમંત્રિત કરતો પત્ર લખો.",
            "solution": "**ADARSH NIVASI CHHATRALAYA**\nStation Road, Kheralu - 384325\nDate: 26th September, 2026\n\nTo,\nThe Manager,\nJay Hind Furniture Mart,\nPatan - 384265\n\n**Subject: Inquiry for quotation for specific furniture.**\n\nRespected Sir,\n\nOur hostel, Adarsh Nivasi Chhatralaya, is expanding and we require new furniture for 50 student rooms.\n\nWe require quotations for the following specific items:\n1. Iron single beds (Size: 6x3 ft) - 50 units\n2. Wooden study tables (Size: 4x2 ft) - 50 units\n3. Plastic molded chairs - 50 units\n\nKindly send us your best quotation, mentioning the lowest prices, terms of payment, and the estimated time required for delivery to Kheralu.\n\nYours faithfully,\n\n(Signature)\n(Warden)\nAdarsh Nivasi Chhatralaya",
            "solution_hi": "(अंग्रेजी समाधान देखें। यह फर्नीचर के लिए एक पूछताछ पत्र है।)",
            "solution_gu": "(અંગ્રેજી ઉકેલ જુઓ. આ ફર્નિચર માટેનો પૂછપરછ પત્ર છે.)",
            "id": "KOBJ_GSEB_11SPCC_P1C5_NUME_004"
        },
        {
            "type": "numerical",
            "question": "Jay Hind Furniture Mart, Patan has received a letter inquiring about quotation and price-list as well as terms of payment for the purchase of furniture. Draft a suitable reply for it to Adarsh Nivasi Chhatralaya, Kheralu.",
            "question_hi": "जय हिंद फर्नीचर मार्ट, पाटन को फर्नीचर की खरीद के लिए कोटेशन और मूल्य-सूची के साथ-साथ भुगतान की शर्तों के बारे में पूछताछ करने वाला एक पत्र मिला है। आदर्श निवासी छात्रालय, खेरालू के लिए इसका उपयुक्त उत्तर तैयार करें।",
            "question_gu": "જય હિંદ ફર્નિચર માર્ટ, પાટણને ફર્નિચરની ખરીદી માટે ક્વોટેશન અને ભાવ-સૂચિ તેમજ ચુકવણીની શરતો વિશે પૂછપરછ કરતો પત્ર મળ્યો છે. આદર્શ નિવાસી છાત્રાલય, ખેરાલુ માટે તેનો યોગ્ય પ્રત્યુત્તર તૈયાર કરો.",
            "solution": "**JAY HIND FURNITURE MART**\nMain Market, Patan - 384265\nDate: 29th September, 2026\n\nTo,\nThe Warden,\nAdarsh Nivasi Chhatralaya,\nKheralu - 384325\n\n**Subject: Quotation for hostel furniture.**\n**Reference: Your inquiry letter dated 26th September, 2026.**\n\nRespected Sir,\n\nThank you for your inquiry. We are pleased to provide the quotation for the furniture items you require.\n\n1. Iron single beds: ₹2,500 per unit\n2. Wooden study tables: ₹1,800 per unit\n3. Plastic molded chairs: ₹450 per unit\n\nSince this is a bulk order for an educational institution, we are happy to offer an additional 5% discount on the total bill.\n\n**Terms of Payment:** 40% advance with the order, balance on delivery.\n**Delivery:** Within 10 days of order confirmation.\n\nWe assure you of the best quality and service.\n\nYours faithfully,\n\n(Signature)\n(Manager)\nJay Hind Furniture Mart",
            "solution_hi": "(अंग्रेजी समाधान देखें। यह जय हिंद फर्नीचर मार्ट की ओर से उत्तर (Reply) है।)",
            "solution_gu": "(અંગ્રેજી ઉકેલ જુઓ. આ જય હિંદ ફર્નિચર માર્ટ તરફથી પ્રત્યુત્તર (Reply) છે.)",
            "id": "KOBJ_GSEB_11SPCC_P1C5_NUME_005"
        },
        {
            "type": "numerical",
            "question": "Write an inquiry letter on behalf of Vinayak Cycle Co., Anand to National Cycle Co., New Delhi with reference to their advertisement of Superspeed Cycle on television.",
            "question_hi": "विनायक साइकिल कंपनी, आनंद की ओर से नेशनल साइकिल कंपनी, नई दिल्ली को टेलीविजन पर सुपरस्पीड साइकिल के उनके विज्ञापन के संदर्भ में एक पूछताछ पत्र लिखें।",
            "question_gu": "વિનાયક સાયકલ કંપની, આણંદ વતી નેશનલ સાયકલ કંપની, નવી દિલ્હીને ટેલિવિઝન પર સુપરસ્પીડ સાયકલની તેમની જાહેરાતના સંદર્ભમાં પૂછપરછ પત્ર લખો.",
            "solution": "**VINAYAK CYCLE CO.**\nMG Road, Anand - 388001\nDate: 25th September, 2026\n\nTo,\nThe Sales Manager,\nNational Cycle Co.,\nNew Delhi - 110001\n\n**Subject: Inquiry regarding 'Superspeed Cycle' advertised on TV.**\n\nRespected Sir,\n\nWe are a prominent bicycle dealer in Anand district. We recently watched the television advertisement for your newly launched 'Superspeed Cycle' and were highly impressed by its features.\n\nWe anticipate a huge demand for this model in our region. We are interested in placing a bulk order of 100 units to begin with.\n\nKindly send us the complete catalogue, dealer price list, and terms of business regarding payment and transportation.\n\nYours faithfully,\n\n(Signature)\n(Proprietor)\nVinayak Cycle Co.",
            "solution_hi": "(अंग्रेजी समाधान देखें। यह साइकिल की खरीद के लिए एक पूछताछ पत्र है।)",
            "solution_gu": "(અંગ્રેજી ઉકેલ જુઓ. આ સાયકલની ખરીદી માટેનો પૂછપરછ પત્ર છે.)",
            "id": "KOBJ_GSEB_11SPCC_P1C5_NUME_006"
        },
        {
            "type": "numerical",
            "question": "National Cycle Co., New Delhi has received a letter from Vinayak Cycle Co., Anand inquiring about their recently launched Superspeed Cycle. Write a suitable reply for it.",
            "question_hi": "नेशनल साइकिल कंपनी, नई दिल्ली को विनायक साइकिल कंपनी, आनंद से उनकी हाल ही में लॉन्च की गई सुपरस्पीड साइकिल के बारे में पूछताछ करने वाला एक पत्र मिला है। इसके लिए एक उपयुक्त उत्तर लिखें।",
            "question_gu": "નેશનલ સાયકલ કંપની, નવી દિલ્હીને વિનાયક સાયકલ કંપની, આણંદ તરફથી તેમની તાજેતરમાં લોન્ચ કરાયેલ સુપરસ્પીડ સાયકલ વિશે પૂછપરછ કરતો પત્ર મળ્યો છે. તેના માટે યોગ્ય પ્રત્યુત્તર લખો.",
            "solution": "**NATIONAL CYCLE CO.**\nIndustrial Estate, New Delhi - 110001\nDate: 30th September, 2026\n\nTo,\nThe Proprietor,\nVinayak Cycle Co.,\nAnand - 388001\n\n**Subject: Reply regarding Superspeed Cycle inquiry.**\n**Reference: Your letter dated 25th September, 2026.**\n\nRespected Sir,\n\nWe thank you for your interest in our newly launched 'Superspeed Cycle'. We are glad that our television campaign has reached valued dealers like you.\n\nAs requested, we have enclosed the comprehensive catalogue and the special dealer price list. The base price of one unit is ₹4,500. For a bulk order of 100 units, we offer a flat 15% trade discount.\n\n**Payment Terms:** 100% advance payment via Bank Transfer.\n**Transportation:** Transport costs to Anand will be borne by us.\n\nWe hope to establish a long and profitable business relationship with you.\n\nYours faithfully,\n\n(Signature)\n(Sales Manager)\nNational Cycle Co.\n\n**Enclosure:** Catalogue and Dealer Price List.",
            "solution_hi": "(अंग्रेजी समाधान देखें। यह नेशनल साइकिल कंपनी की ओर से उत्तर (Reply) है।)",
            "solution_gu": "(અંગ્રેજી ઉકેલ જુઓ. આ નેશનલ સાયકલ કંપની તરફથી પ્રત્યુત્તર (Reply) છે.)",
            "id": "KOBJ_GSEB_11SPCC_P1C5_NUME_007"
        }
    ]
    update_json('app_core/chapters/gseb_class11_spcc_part1_ch5.json', blocks)

def update_part2_ch4():
    # Adding Liability clause, Aroma Company name change, etc.
    blocks = [
        {
            "type": "quiz",
            "question": "Socratic Question: Aroma Private Company wants to change its name to Aroma Limited. What guidance can you give regarding this?",
            "question_hi": "सॉक्रेटिक प्रश्न: एरोमा प्राइवेट कंपनी अपना नाम बदलकर एरोमा लिमिटेड करना चाहती है। इस संबंध में आप क्या मार्गदर्शन दे सकते हैं?",
            "question_gu": "સોક્રેટિક પ્રશ્ન: એરોમા પ્રાઇવેટ કંપની તેનું નામ બદલીને એરોમા લિમિટેડ કરવા માંગે છે. આ અંગે તમે શું માર્ગદર્શન આપી શકો?",
            "options": [
                "It must convert from a Private company to a Public company by passing a special resolution and obtaining Government approval.",
                "It can simply change the board outside its office.",
                "It is impossible to change a company's name once registered.",
                "Only the Prime Minister can approve this change."
            ],
            "options_hi": [
                "इसे एक विशेष प्रस्ताव पारित करके और सरकार की मंजूरी प्राप्त करके एक निजी (Private) कंपनी से एक सार्वजनिक (Public) कंपनी में परिवर्तित होना होगा।",
                "यह केवल अपने कार्यालय के बाहर का बोर्ड बदल सकता है।",
                "एक बार पंजीकृत होने के बाद किसी कंपनी का नाम बदलना असंभव है।",
                "केवल प्रधान मंत्री ही इस परिवर्तन को मंजूरी दे सकते हैं।"
            ],
            "options_gu": [
                "તેણે વિશેષ ઠરાવ પસાર કરીને અને સરકારની મંજૂરી મેળવીને ખાનગી (Private) કંપનીમાંથી જાહેર (Public) કંપનીમાં રૂપાંતરિત થવું પડશે.",
                "તે માત્ર તેની ઓફિસની બહારનું બોર્ડ બદલી શકે છે.",
                "એકવાર નોંધણી થયા પછી કંપનીનું નામ બદલવું અશક્ય છે.",
                "માત્ર વડાપ્રધાન જ આ ફેરફારને મંજૂરી આપી શકે છે."
            ],
            "correct_index": 0,
            "explanation": "The word 'Private' is legally tied to its status as a private company. To remove 'Private' and become 'Aroma Limited', it must legally convert into a Public Company following the Companies Act procedures.",
            "explanation_hi": "'प्राइवेट' शब्द कानूनी रूप से एक निजी कंपनी के रूप में इसकी स्थिति से जुड़ा हुआ है। 'प्राइवेट' को हटाने और 'एरोमा लिमिटेड' बनने के लिए, इसे कंपनी अधिनियम प्रक्रियाओं का पालन करते हुए कानूनी रूप से एक सार्वजनिक कंपनी में बदलना होगा।",
            "explanation_gu": "'પ્રાઇવેટ' શબ્દ કાયદેસર રીતે ખાનગી કંપની તરીકેના તેના દરજ્જા સાથે જોડાયેલો છે. 'પ્રાઇવેટ' ને દૂર કરવા અને 'એરોમા લિમિટેડ' બનવા માટે, તેણે કંપની ધારાની પ્રક્રિયાઓને અનુસરીને કાયદેસર રીતે જાહેર કંપનીમાં રૂપાંતરિત થવું પડશે.",
            "id": "KOBJ_GSEB_11SPCC_P2C4_QUIZ_005"
        },
        {
            "type": "theory",
            "content": "**Changing the Liability Clause**\nThe Liability clause states whether the shareholders' liability is limited by shares, limited by guarantee, or unlimited. \nTo change the Liability Clause, the company must pass a **Unanimous Resolution** (100% agreement from all members) in the general meeting. It cannot be changed if even one member disagrees, because it directly affects the financial risk of every shareholder.",
            "content_hi": "**दायित्व खंड (Liability Clause) को बदलना**\nदायित्व खंड यह बताता है कि शेयरधारकों का दायित्व शेयरों द्वारा सीमित है, गारंटी द्वारा सीमित है, या असीमित है।\nदायित्व खंड को बदलने के लिए, कंपनी को आम बैठक में **सर्वसम्मत प्रस्ताव (Unanimous Resolution)** (सभी सदस्यों की 100% सहमति) पारित करना होगा। इसे तब तक नहीं बदला जा सकता जब तक कि एक भी सदस्य असहमत न हो, क्योंकि यह सीधे तौर पर प्रत्येक शेयरधारक के वित्तीय जोखिम को प्रभावित करता है।",
            "content_gu": "**જવાબદારીની કલમ (Liability Clause) બદલવી**\nજવાબદારીની કલમ જણાવે છે કે શેરધારકોની જવાબદારી શેર દ્વારા મર્યાદિત છે, ગેરંટી દ્વારા મર્યાદિત છે અથવા અમર્યાદિત છે.\nજવાબદારીની કલમ બદલવા માટે, કંપનીએ સામાન્ય સભામાં **સર્વાનુમતે ઠરાવ (Unanimous Resolution)** (તમામ સભ્યોની 100% સંમતિ) પસાર કરવો આવશ્યક છે. જો એક પણ સભ્ય અસંમત હોય તો તેને બદલી શકાતો નથી, કારણ કે તે દરેક શેરધારકના નાણાકીય જોખમને સીધી અસર કરે છે.",
            "id": "KOBJ_GSEB_11SPCC_P2C4_THEO_006"
        }
    ]
    update_json('app_core/chapters/gseb_class11_spcc_part2_ch4.json', blocks)

if __name__ == "__main__":
    update_part1_ch5()
    update_part2_ch4()
