import json
import os

terms_data = [
    ("Partnership", "साझेदारी", "ભાગીદારી", "A business owned by two or more people.", "दो या दो से अधिक लोगों का व्यापार।", "બે કે તેથી વધુ લોકોનો વ્યવસાય.", "Relation between persons who have agreed to share profits of a business carried on by all or any of them acting for all.", "noun"),
    ("Goodwill", "ख्याति", "પાઘડી", "The good reputation of a business.", "व्यापार की अच्छी प्रतिष्ठा।", "વ્યવસાયની સારી પ્રતિષ્ઠા.", "An intangible asset associated with the purchase of one company by another, representing the value of brand name, good customer relations, etc.", "noun"),
    ("Revaluation Account", "पुनर्मूल्यांकन खाता", "પુનઃમૂલ્યાંકન ખાતું", "An account to record changes in asset and liability values.", "संपत्ति और देनदारियों के मूल्य में परिवर्तन दर्ज करने का खाता।", "સંપત્તિ અને જવાબદારીઓના મૂલ્યમાં ફેરફાર નોંધવાનું ખાતું.", "A nominal account prepared to bring the assets and liabilities of the firm to their true values and to find out the profit or loss arising therefrom.", "noun"),
    ("Debenture", "ऋणपत्र", "ડિબેન્ચર", "A long-term loan taken by a company from the public.", "जनता से कंपनी द्वारा लिया गया दीर्घकालिक ऋण।", "જાહેર જનતા પાસેથી કંપનીએ લીધેલી લાંબા ગાળાની લોન.", "A document issued by a company under its common seal acknowledging a debt and containing provisions as regards repayment of principal and interest.", "noun"),
    ("Cash Flow Statement", "नकद प्रवाह विवरण", "રોકડ પ્રવાહ પત્રક", "A statement showing how much cash comes in and goes out.", "एक विवरण जो दिखाता है कि कितनी नकदी आती है और जाती है।", "એક પત્રક જે દર્શાવે છે કે કેટલી રોકડ આવે છે અને જાય છે.", "A statement that shows the inflow and outflow of cash and cash equivalents during a specific period.", "noun"),
    ("Share Capital", "शेयर पूंजी", "શેર મૂડી", "Money raised by a company by selling shares.", "शेयर बेचकर कंपनी द्वारा जुटाई गई धनराशि।", "શેર વેચીને કંપની દ્વારા એકત્ર કરાયેલ નાણાં.", "The capital of a company, or the part of its capital, derived from the issue of shares.", "noun"),
    ("Dissolution", "विघटन", "વિસર્જન", "Closing down a business forever.", "व्यापार को हमेशा के लिए बंद करना।", "વ્યવસાય કાયમ માટે બંધ કરવો.", "The process by which the legal existence of a partnership firm comes to an end.", "noun"),
    ("Authorized Capital", "अधिकृत पूंजी", "અધિકૃત મૂડી", "The maximum capital a company can raise.", "अधिकतम पूंजी जो एक कंपनी जुटा सकती है।", "મહત્તમ મૂડી જે કંપની એકત્ર કરી શકે છે.", "The maximum amount of share capital that the company is authorised by its memorandum of association to issue.", "noun"),
    ("Issued Capital", "निर्गमित पूंजी", "બહાર પાડેલ મૂડી", "The part of capital offered to the public.", "जनता को पेश की गई पूंजी का हिस्सा।", "જાહેર જનતાને ઓફર કરાયેલ મૂડીનો ભાગ.", "The part of the authorised capital which is actually issued to the public for subscription.", "noun"),
    ("Subscribed Capital", "प्रार्थित पूंजी", "ભરાયેલી મૂડી", "The part of issued capital bought by the public.", "जनता द्वारा खरीदी गई निर्गमित पूंजी का हिस्सा।", "જાહેર જનતા દ્વારા ખરીદવામાં આવેલ બહાર પાડેલ મૂડીનો ભાગ.", "The part of the issued capital which has been subscribed for by the public.", "noun"),
    ("Called-up Capital", "मांगी गई पूंजी", "મંગાવેલી મૂડી", "The amount the company has asked shareholders to pay.", "वह राशि जो कंपनी ने शेयरधारकों से भुगतान करने के लिए कहा है।", "કંપનીએ શેરધારકોને ચૂકવવા માટે કહેલી રકમ.", "That part of the subscribed capital which has been called up on the shares.", "noun"),
    ("Paid-up Capital", "चुकता पूंजी", "ભરપાઈ થયેલી મૂડી", "The amount actually paid by shareholders.", "शेयरधारकों द्वारा वास्तव में भुगतान की गई राशि।", "શેરધારકો દ્વારા ખરેખર ચૂકવેલ રકમ.", "The part of called-up capital which has actually been paid by the shareholders.", "noun"),
    ("Calls in Arrears", "बकाया मांग", "બાકી હપ્તા", "Money not paid by shareholders when requested.", "मांगे जाने पर शेयरधारकों द्वारा भुगतान नहीं किया गया पैसा।", "વિનંती કરવામાં આવે ત્યારે શેરધારકો દ્વારા ચૂકવવામાં ન આવેલ નાણાં.", "The amount called up by the company but not yet paid by the shareholders.", "noun"),
    ("Calls in Advance", "अग्रिम मांग", "અગાઉથી મળેલ હપ્તા", "Money paid by shareholders before it is requested.", "मांगे जाने से पहले शेयरधारकों द्वारा भुगतान किया गया पैसा।", "વિનંતી કરતા પહેલા શેરધારકો દ્વારા ચૂકવવામાં આવેલ નાણાં.", "The amount paid by shareholders in excess of the amount called up.", "noun"),
    ("Forfeiture of Shares", "शेयरों की जब्ती", "શેર જપ્તી", "Canceling shares because money was not paid.", "पैसे न चुकाने पर शेयर रद्द करना।", "નાણાં ન ચૂકવવા બદલ શેર રદ કરવા.", "The cancellation of shares for non-payment of calls due.", "noun"),
    ("Re-issue of Shares", "शेयरों का पुनर्निर्गमन", "શેરનું પુનઃ વેચાણ", "Selling the canceled shares again.", "रद्द किए गए शेयरों को फिर से बेचना।", "રદ કરાયેલા શેર ફરીથી વેચવા.", "The process of issuing forfeited shares to new or existing shareholders.", "noun"),
    ("Securities Premium Reserve", "प्रतिभूति प्रीमियम संचय", "જામીનગીરી પ્રીમિયમ અનામત", "Extra money collected above the share's face value.", "शेयर के अंकित मूल्य से अधिक एकत्र किया गया अतिरिक्त पैसा।", "શેરની મૂળ કિંમત કરતાં વધુ એકત્ર કરાયેલ વધારાના નાણાં.", "An account to which the premium collected on the issue of securities is credited.", "noun"),
    ("Capital Reserve", "पूंजीगत संचय", "મૂડી અનામત", "Savings made from special, non-regular profits.", "विशेष, गैर-नियमित मुनाफे से की गई बचत।", "ખાસ, બિન-નિયમિત નફામાંથી કરવામાં આવેલી બચત.", "A reserve created out of capital profits which are not normally available for distribution as dividend.", "noun"),
    ("Over-subscription", "अति-प्रार्थना", "વધુ ભરાવો", "When people want more shares than available.", "जब लोग उपलब्ध से अधिक शेयर चाहते हैं।", "જ્યારે લોકો ઉપલબ્ધ કરતાં વધુ શેર ઈચ્છે છે.", "A situation where the number of shares applied for is more than the number of shares issued.", "noun"),
    ("Under-subscription", "न्यून-प्रार्थना", "ઓછો ભરાવો", "When people want fewer shares than available.", "जब लोग उपलब्ध से कम शेयर चाहते हैं।", "જ્યારે લોકો ઉપલબ્ધ કરતાં ઓછા શેર ઈચ્છે છે.", "A situation where the number of shares applied for is less than the number of shares issued.", "noun"),
    ("Pro-rata Allotment", "आनुपातिक आवंटन", "પ્રમાણસર ફાળવણી", "Giving some shares to everyone in proportion.", "अनुपात में सभी को कुछ शेयर देना।", "દરેકને પ્રમાણસર કેટલાક શેર આપવા.", "The allotment of shares in proportion to the shares applied for, usually in case of over-subscription.", "noun"),
    ("Private Placement", "निजी नियोजन", "ખાનગી પ્લેસમેન્ટ", "Selling shares directly to selected people.", "चुने हुए लोगों को सीधे शेयर बेचना।", "પસંદ કરેલા લોકોને સીધા શેર વેચવા.", "The issue of shares or convertible securities by a company to a select group of persons.", "noun"),
    ("Sweat Equity Shares", "स्वेट इक्विटी शेयर", "સ્વેટ ઈક્વિટી શેર", "Shares given to workers for their hard work.", "कर्मचारियों को उनकी कड़ी मेहनत के लिए दिए गए शेयर।", "કર્મચારીઓને તેમની સખત મહેનત માટે આપવામાં આવતા શેર.", "Shares issued by a company to its employees or directors at a discount or for consideration other than cash.", "noun"),
    ("ESOP", "कर्मचारी स्टॉक विकल्प योजना", "ESOP", "A plan where workers can buy company shares cheaply.", "एक योजना जहां कर्मचारी कंपनी के शेयर सस्ते में खरीद सकते हैं।", "એક યોજના જ્યાં કર્મચારીઓ કંપનીના શેર સસ્તામાં ખરીદી શકે છે.", "Employee Stock Option Plan gives employees the right to purchase shares of the company at a pre-determined price.", "noun"),
    ("Registered Debentures", "पंजीकृत ऋणपत्र", "રજિસ્ટર્ડ ડિબેન્ચર", "Debentures whose owners' names are recorded.", "ऋणपत्र जिनके मालिकों के नाम दर्ज हैं।", "ડિબેન્ચર જેના માલિકોના નામ નોંધાયેલા છે.", "Debentures that are recorded in the register of debenture holders of the company.", "noun"),
    ("Bearer Debentures", "वाहक ऋणपत्र", "બેરર ડિબેન્ચર", "Debentures owned by whoever holds the paper.", "कागज रखने वाले के स्वामित्व वाले ऋणपत्र।", "જેની પાસે કાગળ છે તેની માલિકીના ડિબેન્ચર.", "Debentures which can be transferred by mere delivery, like currency notes.", "noun"),
    ("Secured Debentures", "सुरक्षित ऋणपत्र", "સલામત ડિબેન્ચર", "Loans protected by company property.", "कंपनी की संपत्ति द्वारा सुरक्षित ऋण।", "કંપનીની મિલકત દ્વારા સુરક્ષિત લોન.", "Debentures that are secured by a charge on the assets of the company.", "noun"),
    ("Unsecured Debentures", "असुरक्षित ऋणपत्र", "અસલામત ડિબેન્ચર", "Loans not protected by any property.", "किसी भी संपत्ति द्वारा सुरक्षित नहीं किए गए ऋण।", "કોઈપણ મિલકત દ્વારા સુરક્ષિત ન હોય તેવી લોન.", "Debentures which are not secured by any charge on the assets of the company.", "noun"),
    ("Convertible Debentures", "परिवर्तनीय ऋणपत्र", "કન્વર્ટિબલ ડિબેન્ચર", "Loans that can turn into shares later.", "ऋण जो बाद में शेयरों में बदल सकते हैं।", "લોન જે પછીથી શેરમાં ફેરવાઈ શકે છે.", "Debentures which can be converted into equity shares at a specified time.", "noun"),
    ("Non-convertible Debentures", "गैर-परिवर्तनीय ऋणपत्र", "નોન-કન્વર્ટિબલ ડિબેન્ચર", "Loans that will never turn into shares.", "ऋण जो कभी शेयरों में नहीं बदलेंगे।", "લોન જે ક્યારેય શેરમાં ફેરવાશે નહીં.", "Debentures which cannot be converted into equity shares.", "noun"),
    ("Redeemable Debentures", "प्रतिदेय ऋणपत्र", "રિડીમેબલ ડિબેન્ચર", "Loans that will be paid back on a fixed date.", "ऋण जो एक निश्चित तिथि पर वापस चुकाए जाएंगे।", "લોન જે નિશ્ચિત તારીખે પાછી ચૂકવવામાં આવશે.", "Debentures which are payable on the expiry of a specific period.", "noun"),
    ("Irredeemable Debentures", "अप्रतिदेय ऋणपत्र", "ઇર્રિડીમેબલ ડિબેન્ચર", "Loans paid back only when company closes.", "कंपनी बंद होने पर ही वापस चुकाए जाने वाले ऋण।", "કંપની બંધ થાય ત્યારે જ પાછી ચૂકવવામાં આવતી લોન.", "Debentures which are not repayable during the lifetime of the company.", "noun"),
    ("Trust Deed", "न्यास विलेख", "ટ્રસ્ટ ડીડ", "A legal document protecting loan givers.", "ऋण देने वालों की सुरक्षा करने वाला एक कानूनी दस्तावेज।", "લોન આપનારાઓનું રક્ષણ કરતો કાનૂની દસ્તાવેજ.", "A document created by a company to protect the interests of debenture holders.", "noun"),
    ("Sinking Fund", "शोधन कोष", "સિંકિંગ ફંડ", "Money saved regularly to pay a future debt.", "भविष्य के कर्ज का भुगतान करने के लिए नियमित रूप से बचाया गया पैसा।", "ભવિષ્યના દેવાની ચુકવણી કરવા માટે નિયમિતપણે બચાવેલ નાણાં.", "A fund created by appropriating a part of profit every year to pay off a liability.", "noun"),
    ("DRR", "ऋणपत्र शोधन संचय", "DRR", "Profits kept aside to repay debentures.", "ऋणपत्र चुकाने के लिए अलग रखा गया मुनाफा।", "ડિબેન્ચર ચૂકવવા માટે અલગ રાખવામાં આવેલો નફો.", "Debenture Redemption Reserve is a reserve created out of profits for the purpose of redeeming debentures.", "noun"),
    ("DRI", "ऋणपत्र शोधन निवेश", "DRI", "Money invested outside to help repay debentures.", "ऋणपत्र चुकाने में मदद करने के लिए बाहर निवेश किया गया पैसा।", "ડિબેન્ચર ચૂકવવામાં મદદ કરવા માટે બહાર રોકાણ કરાયેલ નાણાં.", "Debenture Redemption Investment refers to the investment made outside the business to ensure liquidity for redeeming debentures.", "noun"),
    ("Operating Activities", "परिचालन गतिविधियां", "કામગીરીની પ્રવૃત્તિઓ", "Main daily business activities.", "मुख्य दैनिक व्यावसायिक गतिविधियां।", "મુખ્ય દૈનિક વ્યવસાયિક પ્રવૃત્તિઓ.", "The principal revenue-producing activities of the enterprise.", "noun"),
    ("Investing Activities", "निवेश गतिविधियां", "રોકાણની પ્રવૃત્તિઓ", "Buying and selling long-term assets.", "दीर्घकालिक संपत्तियों की खरीद और बिक्री।", "લાંબા ગાળાની સંપત્તિની ખરીદી અને વેચાણ.", "The acquisition and disposal of long-term assets and other investments.", "noun"),
    ("Financing Activities", "वित्तीय गतिविधियां", "નાણાકીય પ્રવૃત્તિઓ", "Activities that change the capital and loans of a company.", "ऐसी गतिविधियां जो कंपनी की पूंजी और ऋण को बदलती हैं।", "કંપનીની મૂડી અને લોનમાં ફેરફાર કરતી પ્રવૃત્તિઓ.", "Activities that result in changes in the size and composition of the owners' capital and borrowings.", "noun"),
    ("Cash Equivalents", "नकद समतुल्य", "રોકડ સમકક્ષ", "Things that can quickly become cash.", "ऐसी चीजें जो जल्दी से नकद बन सकती हैं।", "એવી વસ્તુઓ જે ઝડપથી રોકડ બની શકે છે.", "Short-term, highly liquid investments that are readily convertible to known amounts of cash.", "noun"),
    ("Non-Cash Items", "गैर-नकद मदें", "બિન-રોકડ વસ્તુઓ", "Expenses where actual cash is not paid, like depreciation.", "ऐसे खर्च जहां वास्तविक नकद भुगतान नहीं किया जाता है, जैसे मूल्यह्रास।", "એવા ખર્ચ જ્યાં વાસ્તવિક રોકડ ચૂકવવામાં આવતી નથી, જેમ કે ઘસારો.", "Transactions that do not involve the actual flow of cash, such as depreciation and amortization.", "noun"),
    ("Extraordinary Items", "असाधारण मदें", "અસાધારણ વસ્તુઓ", "Rare events like an earthquake loss.", "भूकंप के नुकसान जैसी दुर्लभ घटनाएं।", "ભૂકંપના નુકસાન જેવી દુર્લભ ઘટનાઓ.", "Incomes or expenses that arise from events or transactions that are clearly distinct from the ordinary activities.", "noun"),
    ("Provision for Taxation", "कराधान के लिए प्रावधान", "કરવેરા માટેની જોગવાઈ", "Money kept aside to pay tax.", "टैक्स चुकाने के लिए अलग रखा गया पैसा।", "ટેક્સ ચૂકવવા માટે અલગ રાખવામાં આવેલા નાણાં.", "An estimated amount set aside out of profits to meet the tax liability of the current year.", "noun"),
    ("Proposed Dividend", "प्रस्तावित लाभांश", "સૂચિત ડિવિડન્ડ", "Profit that directors plan to give to shareholders.", "वह लाभ जो निदेशक शेयरधारकों को देने की योजना बनाते हैं।", "ડિરેક્ટરો શેરધારકોને આપવા માંગતા હોય તે નફો.", "The dividend recommended by the directors to be declared at the Annual General Meeting.", "noun"),
    ("Interim Dividend", "अंतरिम लाभांश", "વચગાળાનું ડિવિડન્ડ", "Profit given in the middle of the year.", "वर्ष के मध्य में दिया जाने वाला लाभ।", "વર્ષની મધ્યમાં આપવામાં આવતો નફો.", "A dividend declared and paid between two Annual General Meetings.", "noun"),
    ("Comparative Statements", "तुलनात्मक विवरण", "તુલનાત્મક પત્રકો", "Financial reports comparing two or more years.", "दो या दो से अधिक वर्षों की तुलना करने वाली वित्तीय रिपोर्ट।", "બે કે તેથી વધુ વર્ષોની સરખામણી કરતા નાણાકીય અહેવાલો.", "Financial statements that provide information for two or more accounting periods side by side.", "noun"),
    ("Common Size Statements", "समरूप विवरण", "સામાન્ય કદના પત્રકો", "Reports showing items as percentages.", "वस्तुओं को प्रतिशत के रूप में दिखाने वाली रिपोर्ट।", "વસ્તુઓને ટકાવારી તરીકે દર્શાવતા અહેવાલો.", "Statements in which items are expressed as a percentage of a common base, such as total assets or total revenue.", "noun"),
    ("Trend Analysis", "प्रवृत्ति विश्लेषण", "વલણ વિશ્લેષણ", "Checking if numbers are going up or down over years.", "यह जाँचना कि क्या संख्याएँ वर्षों से ऊपर या नीचे जा रही हैं।", "વર્ષોથી સંખ્યાઓ ઉપર કે નીચે જઈ રહી છે તે તપાસવું.", "A technique used to examine the direction and rate of change in financial data over a period of time.", "noun"),
    ("Ratio Analysis", "अनुपात विश्लेषण", "ગુણોત્તર વિશ્લેષણ", "Comparing two financial numbers.", "दो वित्तीय संख्याओं की तुलना करना।", "બે નાણાકીય સંખ્યાઓની સરખામણી.", "The process of determining and interpreting numerical relationships between figures of financial statements.", "noun"),
    ("Liquidity Ratio", "तरलता अनुपात", "તરલતા ગુણોત્તર", "Checking if a company can pay its short-term loans.", "यह जाँचना कि क्या कंपनी अपने अल्पकालिक ऋण चुका सकती है।", "કંપની તેની ટૂંકા ગાળાની લોન ચૂકવી શકે છે કે કેમ તે તપાસવું.", "Ratios that measure the ability of the firm to meet its short-term financial obligations.", "noun")
]

dictionary_list = []

for idx, (en, hi, gu, s_en, s_hi, s_gu, a_en, pos) in enumerate(terms_data):
    # generating 5 sentences
    sentences = [
        {"en": f"The concept of {en} is very important in accounting.", "hi": f"लेखांकन में {hi} की अवधारणा बहुत महत्वपूर्ण है।", "gu": f"એકાઉન્ટિંગમાં {gu} નો ખ્યાલ ખૂબ જ મહત્વપૂર્ણ છે."},
        {"en": f"Our teacher explained {en} with a real world example.", "hi": f"हमारे शिक्षक ने एक वास्तविक दुनिया के उदाहरण के साथ {hi} की व्याख्या की।", "gu": f"અમારા શિક્ષકે વાસ્તવિક દુનિયાના ઉદાહરણ સાથે {gu} સમજાવ્યું."},
        {"en": f"Understanding {en} helps in analyzing financial statements.", "hi": f"{hi} को समझने से वित्तीय विवरणों का विश्लेषण करने में मदद मिलती है।", "gu": f"{gu} સમજવાથી નાણાકીય પત્રકોનું વિશ્લેષણ કરવામાં મદદ મળે છે."},
        {"en": f"Many businesses rely heavily on proper management of their {en}.", "hi": f"कई व्यवसाय अपने {hi} के उचित प्रबंधन पर बहुत अधिक निर्भर करते हैं।", "gu": f"ઘણા વ્યવસાયો તેમના {gu} ના યોગ્ય સંચાલન પર ભારે આધાર રાખે છે."},
        {"en": f"Questions related to {en} are commonly asked in the board exams.", "hi": f"बोर्ड परीक्षा में आमतौर पर {hi} से संबंधित प्रश्न पूछे जाते हैं।", "gu": f"બોર્ડની પરીક્ષાઓમાં સામાન્ય રીતે {gu} સંબંધિત પ્રશ્નો પૂછવામાં આવે છે."}
    ]
    
    term_obj = {
        "id": f"DICT_ACC12_{idx+1:03d}",
        "term": {
            "english": en,
            "gujarati": gu,
            "hindi": hi
        },
        "pronunciation_en": en,
        "pronunciation_hi": hi,
        "definition": {
            "simple": {
                "en": s_en,
                "hi": s_hi,
                "gu": s_gu
            },
            "academic": {
                "en": a_en,
                "hi": f"शैक्षणिक परिभाषा: {a_en}",
                "gu": f"શૈક્ષણિક વ્યાખ્યા: {a_en}"
            }
        },
        "part_of_speech": pos,
        "examples": sentences,
        "media": {},
        "knowledge_graph_links": {
            "related": [],
            "prerequisites": [],
            "used_in": ["ACC_CH01"]
        },
        "ai_context": {
            "common_misconceptions": [f"{en} is often misunderstood by beginners."],
            "tutor_hint": f"Remember that {en} applies to accounting contexts."
        }
    }
    dictionary_list.append(term_obj)

output_dir = "/home/ubuntu/Shine_Academy_Naroda/app_core/universal_dictionary"
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "accounts_class12.json"), "w", encoding="utf-8") as f:
    json.dump(dictionary_list, f, indent=4, ensure_ascii=False)

print("Generated dictionary successfully!")
