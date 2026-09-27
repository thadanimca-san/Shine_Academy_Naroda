import json
import os

def save_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Generated {file_path} successfully!")

def gen_ch2():
    data = {
        "metadata": {
            "id": "cbse_class12_accounts_ch2",
            "title": "Goodwill: Nature and Valuation",
            "title_hi": "ख्याति: प्रकृति और मूल्यांकन",
            "title_gu": "પાઘડી: સ્વરૂપ અને મૂલ્યાંકન",
            "subject": "Accountancy",
            "subject_hi": "लेखाशास्त्र",
            "subject_gu": "નામાનાં મૂળતત્ત્વો",
            "grade": "12",
            "board": "CBSE",
            "curriculum": ["CBSE"],
            "difficulty": "Intermediate",
            "estimated_minutes": 60,
            "learning_outcomes": [
                "Understand the meaning, nature, and factors affecting Goodwill.",
                "Calculate Goodwill using Average Profit Method.",
                "Calculate Goodwill using Super Profit Method.",
                "Calculate Goodwill using Capitalisation Method."
            ],
            "learning_outcomes_hi": [
                "ख्याति के अर्थ, प्रकृति और उसे प्रभावित करने वाले कारकों को समझें।",
                "औसत लाभ विधि (Average Profit Method) का उपयोग करके ख्याति की गणना करें।",
                "अधि-लाभ विधि (Super Profit Method) का उपयोग करके ख्याति की गणना करें।",
                "पूंजीकरण विधि (Capitalisation Method) का उपयोग करके ख्याति की गणना करें।"
            ],
            "learning_outcomes_gu": [
                "પાઘડીનો અર્થ, સ્વરૂપ અને તેને અસર કરતા પરિબળો સમજો.",
                "સરેરાશ નફાની પદ્ધતિ (Average Profit Method) નો ઉપયોગ કરીને પાઘડીની ગણતરી કરો.",
                "અધિક નફાની પદ્ધતિ (Super Profit Method) નો ઉપયોગ કરીને પાઘડીની ગણતરી કરો.",
                "મૂડીકરણ પદ્ધતિ (Capitalisation Method) નો ઉપયોગ કરીને પાઘડીની ગણતરી કરો."
            ],
            "core_concepts": [
                "Meaning of Goodwill",
                "Purchased vs Self-generated Goodwill",
                "Average Profit Method",
                "Super Profit Method",
                "Capitalisation Method"
            ],
            "ai_context": {
                "learning_goal": "Master the valuation of goodwill under various methods, understanding why a business might pay more than the net asset value when acquiring another firm.",
                "common_misconceptions": [
                    "Thinking self-generated goodwill can be recorded in the books (AS 26 prohibits this).",
                    "Forgetting to deduct abnormal gains or add abnormal losses when calculating normal business profits."
                ]
            }
        },
        "blocks": [
            {
                "type": "theory",
                "content": "Imagine two identical sweet shops side-by-side. Shop A is 50 years old and always crowded. Shop B just opened yesterday and is empty. If you were to buy one of these shops, which one would cost you more? Shop A, of course! But why? They have the exact same furniture and space. \nYou are paying extra for Shop A's reputation, its loyal customers, and its brand name. In accounting, this invisible asset is called **Goodwill**.",
                "content_hi": "कल्पना कीजिए कि दो एक जैसी मिठाई की दुकानें साथ-साथ हैं। दुकान A 50 साल पुरानी है और वहां हमेशा भीड़ रहती है। दुकान B कल ही खुली है और खाली है। यदि आपको इनमें से कोई एक दुकान खरीदनी हो, तो आपको किसकी कीमत अधिक चुकानी होगी? बेशक दुकान A की! लेकिन क्यों? उनके पास बिल्कुल एक जैसा फर्नीचर और जगह है।\nआप दुकान A की प्रतिष्ठा, उसके वफादार ग्राहकों और उसके ब्रांड नाम के लिए अतिरिक्त भुगतान कर रहे हैं। लेखांकन में, इस अदृश्य संपत्ति को **ख्याति (Goodwill)** कहा जाता है।",
                "content_gu": "કલ્પના કરો કે બે સમાન મીઠાઈની દુકાનો પાસપાસે છે. દુકાન A 50 વર્ષ જૂની છે અને હંમેશા ભીડ રહે છે. દુકાન B ગઈકાલે જ ખુલી છે અને ખાલી છે. જો તમારે આમાંથી કોઈ એક દુકાન ખરીદવી હોય, તો તમારા માટે કઈ વધુ મોંઘી હશે? દુકાન A, અલબત્ત! પરંતુ શા માટે? તેમની પાસે બરાબર સમાન ફર્નિચર અને જગ્યા છે.\nતમે દુકાન A ની પ્રતિષ્ઠા, તેના વફાદાર ગ્રાહકો અને તેના બ્રાન્ડ નામ માટે વધારાની ચૂકવણી કરી રહ્યા છો. એકાઉન્ટિંગમાં, આ અદ્રશ્ય મિલકતને **પાઘડી (Goodwill)** કહેવામાં આવે છે.",
                "id": "KOBJ_CBSE_ACC12_CH2_THEO_001"
            },
            {
                "type": "quiz",
                "question": "Socratic Question: Can you physically touch or see 'Goodwill'? If not, does it still have financial value?",
                "question_hi": "सॉक्रेटिक प्रश्न: क्या आप भौतिक रूप से 'ख्याति' को छू या देख सकते हैं? यदि नहीं, तो क्या इसका अभी भी वित्तीय मूल्य है?",
                "question_gu": "સોક્રેટિક પ્રશ્ન: શું તમે શારીરિક રીતે 'પાઘડી' ને સ્પર્શ કરી શકો છો કે જોઈ શકો છો? જો નહિં, તો શું તે હજુ પણ નાણાકીય મૂલ્ય ધરાવે છે?",
                "options": [
                    "Yes, you can touch it because it is cash.",
                    "No, you can't touch it, so it has zero value.",
                    "No, you can't touch it, but it is an Intangible Asset with immense financial value.",
                    "It is a fictional asset with no real value."
                ],
                "options_hi": [
                    "हाँ, आप इसे छू सकते हैं क्योंकि यह नकद है।",
                    "नहीं, आप इसे नहीं छू सकते, इसलिए इसका मूल्य शून्य है।",
                    "नहीं, आप इसे नहीं छू सकते, लेकिन यह अत्यधिक वित्तीय मूल्य वाली एक अमूर्त संपत्ति है।",
                    "यह एक काल्पनिक संपत्ति है जिसका कोई वास्तविक मूल्य नहीं है।"
                ],
                "options_gu": [
                    "હા, તમે તેને સ્પર્શ કરી શકો છો કારણ કે તે રોકડ છે.",
                    "ના, તમે તેને સ્પર્શ કરી શકતા નથી, તેથી તેનું મૂલ્ય શૂન્ય છે.",
                    "ના, તમે તેને સ્પર્શ કરી શકતા નથી, પરંતુ તે એક અમૂર્ત મિલકત (Intangible Asset) છે જેનું ઘણું નાણાકીય મૂલ્ય છે.",
                    "તે વાસ્તવિક મૂલ્ય વિનાની કાલ્પનિક મિલકત છે."
                ],
                "correct_index": 2,
                "explanation": "Goodwill is an Intangible Asset. Though invisible, it generates future profits.",
                "explanation_hi": "ख्याति एक अमूर्त संपत्ति है। यद्यपि अदृश्य है, यह भविष्य में लाभ उत्पन्न करती है।",
                "explanation_gu": "પાઘડી એક અદ્રશ્ય મિલકત છે. જોકે તે જોઈ શકાતી નથી, તે ભવિષ્યમાં નફો પેદા કરે છે.",
                "id": "KOBJ_CBSE_ACC12_CH2_QUIZ_002"
            },
            {
                "type": "teacher_tip",
                "content": "According to Accounting Standard 26 (AS 26), only 'Purchased Goodwill' can be recorded in the books of accounts because money was actually paid for it. 'Self-generated Goodwill' (reputation built over time) cannot be recorded as an asset because its exact cost cannot be objectively measured.",
                "content_hi": "लेखांकन मानक 26 (AS 26) के अनुसार, केवल 'क्रय की गई ख्याति (Purchased Goodwill)' को ही लेखा पुस्तकों में दर्ज किया जा सकता है क्योंकि इसके लिए वास्तव में धन का भुगतान किया गया था। 'स्व-निर्मित ख्याति' (समय के साथ बनी प्रतिष्ठा) को संपत्ति के रूप में दर्ज नहीं किया जा सकता क्योंकि इसकी सटीक लागत को मापा नहीं जा सकता।",
                "content_gu": "એકાઉન્ટિંગ સ્ટાન્ડર્ડ 26 (AS 26) મુજબ, માત્ર 'ખરીદેલી પાઘડી (Purchased Goodwill)' જ હિસાબી ચોપડામાં નોંધી શકાય છે કારણ કે તેના માટે વાસ્તવમાં પૈસા ચૂકવવામાં આવ્યા હતા. 'સ્વ-ઉત્પન્ન પાઘડી' (સમય જતાં બનેલી પ્રતિષ્ઠા) ને મિલકત તરીકે નોંધી શકાતી નથી કારણ કે તેની ચોક્કસ પડતર માપી શકાતી નથી.",
                "id": "KOBJ_CBSE_ACC12_CH2_TEAC_003"
            },
            {
                "type": "theory",
                "content": "**Methods of Valuation of Goodwill**\nSince Goodwill is invisible, how do we put a price tag on it? Accountants use three main mathematical methods based on the firm's past profits:\n1. **Average Profit Method:** Simple or Weighted Average of past years' profits.\n2. **Super Profit Method:** Profit earned OVER and ABOVE the normal profit of the industry.\n3. **Capitalisation Method:** Capitalising the average or super profits at the normal rate of return.",
                "content_hi": "**ख्याति के मूल्यांकन की विधियां**\nचूंकि ख्याति अदृश्य है, हम इस पर मूल्य कैसे तय कर सकते हैं? लेखाकार फर्म के पिछले मुनाफे के आधार पर तीन मुख्य गणितीय विधियों का उपयोग करते हैं:\n1. **औसत लाभ विधि:** पिछले वर्षों के मुनाफे का साधारण या भारित औसत।\n2. **अधि-लाभ विधि:** उद्योग के सामान्य लाभ के ऊपर और उससे अधिक कमाया गया लाभ।\n3. **पूंजीकरण विधि:** सामान्य प्रतिफल दर पर औसत या अधि-लाभ का पूंजीकरण।",
                "content_gu": "**પાઘડીના મૂલ્યાંકનની પદ્ધતિઓ**\nકારણ કે પાઘડી અદ્રશ્ય છે, આપણે તેના પર કિંમત કેવી રીતે નક્કી કરી શકીએ? એકાઉન્ટન્ટ્સ પેઢીના ભૂતકાળના નફાના આધારે ત્રણ મુખ્ય ગાણિતિક પદ્ધતિઓનો ઉપયોગ કરે છે:\n1. **સરેરાશ નફાની પદ્ધતિ:** પાછલા વર્ષોના નફાની સાદી અથવા ભારિત સરેરાશ.\n2. **અધિક નફાની પદ્ધતિ:** ઉદ્યોગના સામાન્ય નફા કરતાં વધુ કમાયેલ નફો.\n3. **મૂડીકરણ પદ્ધતિ:** વળતરના સામાન્ય દર પર સરેરાશ અથવા અધિક નફાનું મૂડીકરણ.",
                "id": "KOBJ_CBSE_ACC12_CH2_THEO_004"
            },
            {
                "type": "common_mistakes",
                "content": "Before calculating ANY average, you must adjust the past profits! You must REMOVE Abnormal Gains (like winning a lottery or selling machinery at a profit) and ADD BACK Abnormal Losses (like loss by fire). We only want the NORMAL operating business profit.",
                "content_hi": "किसी भी औसत की गणना करने से पहले, आपको पिछले मुनाफे को समायोजित करना होगा! आपको असामान्य लाभ (जैसे लॉटरी जीतना या मशीनरी बेचना) को हटाना होगा और असामान्य नुकसान (जैसे आग से नुकसान) को वापस जोड़ना होगा। हम केवल सामान्य परिचालन व्यवसाय लाभ चाहते हैं।",
                "content_gu": "કોઈપણ સરેરાશની ગણતરી કરતા પહેલા, તમારે પાછલા નફાને સમાયોજિત (Adjust) કરવો જ પડશે! તમારે અસામાન્ય નફો (જેમ કે લોટરી જીતવી અથવા મશીનરી વેચવી) બાદ કરવો પડશે અને અસામાન્ય નુકસાન (જેમ કે આગથી નુકસાન) ઉમેરવું પડશે. અમને માત્ર સામાન્ય કામગીરીનો નફો જોઈએ છે.",
                "id": "KOBJ_CBSE_ACC12_CH2_COMM_005"
            },
            {
                "type": "numerical",
                "question": "A firm earns a profit of ₹1,00,000, ₹1,20,000, and ₹1,40,000 during the last 3 years. The profit of the second year included an abnormal gain of ₹20,000 from the sale of an old machine. The normal rate of return in this industry is 10%. The capital employed by the firm is ₹10,00,000.\nCalculate Goodwill using the **Super Profit Method** at 2 years' purchase.",
                "question_hi": "एक फर्म पिछले 3 वर्षों के दौरान ₹1,00,000, ₹1,20,000 और ₹1,40,000 का लाभ कमाती है। दूसरे वर्ष के लाभ में एक पुरानी मशीन की बिक्री से ₹20,000 का असामान्य लाभ (Abnormal Gain) शामिल था। इस उद्योग में प्रतिफल की सामान्य दर (Normal Rate of Return) 10% है। फर्म द्वारा नियोजित पूंजी (Capital Employed) ₹10,00,000 है।\n2 वर्ष की खरीद (2 years' purchase) पर **अधि-लाभ विधि (Super Profit Method)** का उपयोग करके ख्याति की गणना करें।",
                "question_gu": "એક પેઢી છેલ્લા 3 વર્ષ દરમિયાન ₹1,00,000, ₹1,20,000 અને ₹1,40,000 નો નફો કમાય છે. બીજા વર્ષના નફામાં જૂના મશીનના વેચાણથી ₹20,000 નો અસામાન્ય નફો (Abnormal Gain) સામેલ હતો. આ ઉદ્યોગમાં વળતરનો સામાન્ય દર (Normal Rate of Return) 10% છે. પેઢી દ્વારા રોકાયેલી મૂડી (Capital Employed) ₹10,00,000 છે.\n2 વર્ષની ખરીદી (2 years' purchase) પર **અધિક નફાની પદ્ધતિ (Super Profit Method)** નો ઉપયોગ કરીને પાઘડીની ગણતરી કરો.",
                "solution": "Step-by-Step Calculation for Super Profit Method:\n\n**Step 1: Adjust Past Profits to find Normal Profit**\nYear 1: ₹1,00,000\nYear 2: ₹1,20,000 - ₹20,000 (Deduct Abnormal Gain) = ₹1,00,000\nYear 3: ₹1,40,000\nTotal Normal Profit = 1,00,000 + 1,00,000 + 1,40,000 = ₹3,40,000\n\n**Step 2: Calculate Average Normal Profit**\nAverage Profit = Total Profit / Number of Years\nAverage Profit = 3,40,000 / 3 = **₹1,13,333.33** (approx)\n\n**Step 3: Calculate Normal Profit (Based on Capital)**\nNormal Profit = Capital Employed × (Normal Rate of Return / 100)\nNormal Profit = 10,00,000 × (10 / 100) = **₹1,00,000**\n\n**Step 4: Calculate Super Profit**\nSuper Profit = Average Profit - Normal Profit\nSuper Profit = 1,13,333.33 - 1,00,000 = **₹13,333.33**\n\n**Step 5: Calculate Goodwill**\nGoodwill = Super Profit × Number of Years' Purchase\nGoodwill = 13,333.33 × 2 = **₹26,667 (approx)**\n\n*(Conclusion: The firm is generating ₹13,333 MORE than what an average firm with the same capital would generate. This 'extra' capability is why the firm has Goodwill!)*",
                "solution_hi": "सुपर प्रॉफिट मेथड (Super Profit Method) के लिए चरण-दर-चरण गणना:\n\n**चरण 1: सामान्य लाभ खोजने के लिए पिछले मुनाफे को समायोजित करें**\nवर्ष 1: ₹1,00,000\nवर्ष 2: ₹1,20,000 - ₹20,000 (असामान्य लाभ घटाएं) = ₹1,00,000\nवर्ष 3: ₹1,40,000\nकुल सामान्य लाभ = 1,00,000 + 1,00,000 + 1,40,000 = ₹3,40,000\n\n**चरण 2: औसत सामान्य लाभ की गणना करें**\nऔसत लाभ = कुल लाभ / वर्षों की संख्या\nऔसत लाभ = 3,40,000 / 3 = **₹1,13,333.33**\n\n**चरण 3: सामान्य लाभ की गणना करें (पूंजी के आधार पर)**\nसामान्य लाभ = नियोजित पूंजी × (सामान्य प्रतिफल दर / 100)\nसामान्य लाभ = 10,00,000 × (10 / 100) = **₹1,00,000**\n\n**चरण 4: अधि-लाभ (Super Profit) की गणना करें**\nसुपर प्रॉफिट = औसत लाभ - सामान्य लाभ\nसुपर प्रॉफिट = 1,13,333.33 - 1,00,000 = **₹13,333.33**\n\n**चरण 5: ख्याति (Goodwill) की गणना करें**\nख्याति = सुपर प्रॉफिट × खरीद के वर्षों की संख्या\nख्याति = 13,333.33 × 2 = **₹26,667 (लगभग)**",
                "solution_gu": "અધિક નફાની પદ્ધતિ માટે તબક્કાવાર ગણતરી:\n\n**પગલું 1: સામાન્ય નફો શોધવા માટે પાછલા નફાને સમાયોજિત કરો**\nવર્ષ 1: ₹1,00,000\nવર્ષ 2: ₹1,20,000 - ₹20,000 (અસામાન્ય નફો બાદ કરો) = ₹1,00,000\nવર્ષ 3: ₹1,40,000\nકુલ સામાન્ય નફો = 1,00,000 + 1,00,000 + 1,40,000 = ₹3,40,000\n\n**પગલું 2: સરેરાશ સામાન્ય નફાની ગણતરી કરો**\nસરેરાશ નફો = કુલ નફો / વર્ષોની સંખ્યા\nસરેરાશ નફો = 3,40,000 / 3 = **₹1,13,333.33**\n\n**પગલું 3: સામાન્ય નફાની ગણતરી કરો (મૂડીના આધારે)**\nસામાન્ય નફો = રોકાયેલી મૂડી × (વળતરનો સામાન્ય દર / 100)\nસામાન્ય નફો = 10,00,000 × (10 / 100) = **₹1,00,000**\n\n**પગલું 4: અધિક નફાની (Super Profit) ગણતરી કરો**\nઅધિક નફો = સરેરાશ નફો - સામાન્ય નફો\nઅધિક નફો = 1,13,333.33 - 1,00,000 = **₹13,333.33**\n\n**પગલું 5: પાઘડી (Goodwill) ની ગણતરી કરો**\nપાઘડી = અધિક નફો × ખરીદીના વર્ષોની સંખ્યા\nપાઘડી = 13,333.33 × 2 = **₹26,667 (આશરે)**",
                "id": "KOBJ_CBSE_ACC12_CH2_NUME_006"
            }
        ]
    }
    save_json('app_core/chapters/cbse_class12_accounts_ch2.json', data)

def gen_ch3():
    data = {
        "metadata": {
            "id": "cbse_class12_accounts_ch3",
            "title": "Change in Profit-Sharing Ratio Among the Existing Partners",
            "title_hi": "विद्यमान साझेदारों के लाभ-विभाजन अनुपात में परिवर्तन",
            "title_gu": "ચાલુ ભાગીદારો વચ્ચે નફા-નુકસાનના પ્રમાણમાં ફેરફાર",
            "subject": "Accountancy",
            "subject_hi": "लेखाशास्त्र",
            "subject_gu": "નામાનાં મૂળતત્ત્વો",
            "grade": "12",
            "board": "CBSE",
            "curriculum": ["CBSE"],
            "difficulty": "Advanced",
            "estimated_minutes": 90,
            "learning_outcomes": [
                "Understand the concept of Reconstitution of a Partnership Firm.",
                "Calculate Sacrificing Ratio and Gaining Ratio.",
                "Pass journal entries for accounting treatment of Goodwill.",
                "Prepare Revaluation Account for Assets and Liabilities."
            ],
            "learning_outcomes_hi": [
                "साझेदारी फर्म के पुनर्गठन की अवधारणा को समझें।",
                "त्याग अनुपात (Sacrificing Ratio) और लाभ प्राप्ति अनुपात (Gaining Ratio) की गणना करें।",
                "ख्याति के लेखांकन उपचार के लिए जर्नल प्रविष्टियाँ पारित करें।",
                "संपत्तियों और देनदारियों के लिए पुनर्मूल्यांकन खाता (Revaluation Account) तैयार करें।"
            ],
            "learning_outcomes_gu": [
                "ભાગીદારી પેઢીના પુનર્ગઠનનો ખ્યાલ સમજો.",
                "ત્યાગનું પ્રમાણ (Sacrificing Ratio) અને લાભનું પ્રમાણ (Gaining Ratio) ની ગણતરી કરો.",
                "પાઘડીની હિસાબી અસરો માટે આમનોંધ પસાર કરો.",
                "મિલકતો અને દેવાઓ માટે પુનઃમૂલ્યાંકન ખાતું (Revaluation Account) તૈયાર કરો."
            ],
            "core_concepts": [
                "Reconstitution of Partnership",
                "Sacrificing Ratio",
                "Gaining Ratio",
                "Treatment of Goodwill",
                "Revaluation Account",
                "Workmen Compensation Reserve"
            ],
            "ai_context": {
                "learning_goal": "Understand how a change in the internal profit-sharing ratio acts as a 'mini-sale' where the gaining partner compensates the sacrificing partner using the firm's goodwill.",
                "common_misconceptions": [
                    "Confusing Old Ratio - New Ratio (Sacrifice) with New Ratio - Old Ratio (Gain).",
                    "Distributing Revaluation Profit in the New Ratio instead of the Old Ratio."
                ]
            }
        },
        "blocks": [
            {
                "type": "theory",
                "content": "Imagine you and your friend own a pizza shop. For years, you shared the pizzas 50-50 (1:1). Now, your friend decides he will do 80% of the heavy lifting and cooking, so you both agree to change the ratio to 80-20. \nWhen existing partners change their agreement without ending the business, it is called **Reconstitution of the Partnership Firm**. The old agreement dies, and a new agreement is born.",
                "content_hi": "कल्पना करें कि आप और आपका दोस्त एक पिज्जा शॉप के मालिक हैं। वर्षों तक, आपने पिज्जा 50-50 (1:1) साझा किया। अब, आपका दोस्त फैसला करता है कि वह 80% भारी काम और खाना पकाने का काम करेगा, इसलिए आप दोनों अनुपात को 80-20 में बदलने के लिए सहमत होते हैं।\nजब मौजूदा साझेदार व्यवसाय को समाप्त किए बिना अपने समझौते को बदलते हैं, तो इसे **साझेदारी फर्म का पुनर्गठन (Reconstitution)** कहा जाता है। पुराना समझौता मर जाता है, और एक नया समझौता पैदा होता है।",
                "content_gu": "કલ્પના કરો કે તમે અને તમારો મિત્ર પિઝાની દુકાન ધરાવો છો. વર્ષોથી, તમે પિઝા 50-50 (1:1) વહેંચ્યા. હવે, તમારો મિત્ર નક્કી કરે છે કે તે 80% ભારે કામ અને રસોઈ કરશે, તેથી તમે બંને પ્રમાણને 80-20 માં બદલવા માટે સંમત થાઓ છો.\nજ્યારે વર્તમાન ભાગીદારો વ્યવસાયને સમાપ્ત કર્યા વિના તેમના કરારમાં ફેરફાર કરે છે, ત્યારે તેને **ભાગીદારી પેઢીનું પુનર્ગઠન (Reconstitution)** કહેવામાં આવે છે. જૂનો કરાર સમાપ્ત થાય છે, અને નવો કરાર જન્મે છે.",
                "id": "KOBJ_CBSE_ACC12_CH3_THEO_001"
            },
            {
                "type": "quiz",
                "question": "In the pizza shop example above, your share went from 50% down to 20%. What happened to your share?",
                "question_hi": "उपरोक्त पिज्जा शॉप के उदाहरण में, आपकी हिस्सेदारी 50% से गिरकर 20% हो गई। आपकी हिस्सेदारी का क्या हुआ?",
                "question_gu": "ઉપરના પિઝા શોપના ઉદાહરણમાં, તમારો હિસ્સો 50% થી ઘટીને 20% થઈ ગયો. તમારા હિસ્સાનું શું થયું?",
                "options": [
                    "I gained a 30% share.",
                    "I sacrificed a 30% share to my friend.",
                    "My share remained the same.",
                    "The business absorbed the share."
                ],
                "options_hi": [
                    "मैंने 30% हिस्सेदारी हासिल की।",
                    "मैंने अपने दोस्त को 30% हिस्सेदारी का त्याग किया।",
                    "मेरा हिस्सा वही रहा।",
                    "व्यवसाय ने हिस्सेदारी को अवशोषित कर लिया।"
                ],
                "options_gu": [
                    "મેં 30% હિસ્સો મેળવ્યો.",
                    "મેં મારા મિત્ર માટે 30% હિસ્સાનો ત્યાગ કર્યો.",
                    "મારો હિસ્સો એ જ રહ્યો.",
                    "વ્યવસાયે હિસ્સો શોષી લીધો."
                ],
                "correct_index": 1,
                "explanation": "You gave up a portion of your future profits. This is called a Sacrifice. Formula: Sacrificing Ratio = Old Ratio - New Ratio.",
                "explanation_hi": "आपने अपने भविष्य के मुनाफे का एक हिस्सा छोड़ दिया। इसे त्याग (Sacrifice) कहा जाता है। सूत्र: त्याग अनुपात = पुराना अनुपात - नया अनुपात।",
                "explanation_gu": "તમે તમારા ભવિષ્યના નફાનો એક ભાગ છોડી દીધો. આને ત્યાગ (Sacrifice) કહેવામાં આવે છે. સૂત્ર: ત્યાગનું પ્રમાણ = જૂનું પ્રમાણ - નવું પ્રમાણ.",
                "id": "KOBJ_CBSE_ACC12_CH3_QUIZ_002"
            },
            {
                "type": "theory",
                "content": "**The Golden Rule of Reconstitution:**\nWhenever the ratio changes, one partner LOSES (Sacrifices) and another WINS (Gains). Because the Gaining Partner will receive more profit in the future, he must compensate the Sacrificing Partner TODAY. This compensation is paid using the firm's **Goodwill**.\n\nJournal Entry:\n**Gaining Partner's Capital A/c ... Dr.**\n    **To Sacrificing Partner's Capital A/c**",
                "content_hi": "**पुनर्गठन का स्वर्णिम नियम:**\nजब भी अनुपात बदलता है, एक भागीदार हारता है (त्याग करता है) और दूसरा जीतता है (लाभ प्राप्त करता है)। चूंकि लाभ प्राप्त करने वाले भागीदार को भविष्य में अधिक लाभ मिलेगा, इसलिए उसे आज ही त्याग करने वाले भागीदार को मुआवजा देना होगा। यह मुआवजा फर्म की **ख्याति (Goodwill)** का उपयोग करके चुकाया जाता है।\n\nजर्नल प्रविष्टि:\n**लाभ प्राप्त करने वाले साझेदार का पूंजी खाता ... Dr.**\n    **To त्याग करने वाले साझेदार का पूंजी खाता**",
                "content_gu": "**પુનર્ગઠનનો સુવર્ણ નિયમ:**\nજ્યારે પણ પ્રમાણ બદલાય છે, ત્યારે એક ભાગીદાર ગુમાવે છે (ત્યાગ કરે છે) અને બીજો જીતે છે (લાભ મેળવે છે). કારણ કે લાભ મેળવનાર ભાગીદારને ભવિષ્યમાં વધુ નફો મળશે, તેણે આજે જ ત્યાગ કરનાર ભાગીદારને વળતર આપવું પડશે. આ વળતર પેઢીની **પાઘડી (Goodwill)** નો ઉપયોગ કરીને ચૂકવવામાં આવે છે.\n\nઆમનોંધ:\n**લાભ લેનાર ભાગીદારનું મૂડી ખાતું ... ઉધાર**\n    **તે ત્યાગ કરનાર ભાગીદારના મૂડી ખાતે**",
                "id": "KOBJ_CBSE_ACC12_CH3_THEO_003"
            },
            {
                "type": "teacher_tip",
                "content": "Memorize the formula:\nSacrifice = Old Share - New Share. \nIf the answer is POSITIVE, it is a Sacrifice. If the answer is NEGATIVE, it is a Gain!",
                "content_hi": "सूत्र याद रखें:\nत्याग = पुराना हिस्सा - नया हिस्सा।\nयदि उत्तर धनात्मक (Positive) है, तो यह त्याग है। यदि उत्तर ऋणात्मक (Negative) है, तो यह लाभ है!",
                "content_gu": "સૂત્ર યાદ રાખો:\nત્યાગ = જૂનો ભાગ - નવો ભાગ.\nજો જવાબ હકારાત્મક (Positive) છે, તો તે ત્યાગ છે. જો જવાબ નકારાત્મક (Negative) છે, તો તે લાભ છે!",
                "id": "KOBJ_CBSE_ACC12_CH3_TEAC_004"
            },
            {
                "type": "numerical",
                "question": "X, Y and Z are partners sharing profits in the ratio of 5:3:2. They decide to share future profits equally (1:1:1). The Goodwill of the firm is valued at ₹90,000.\nCalculate the Sacrifice/Gain of each partner and pass the necessary Journal Entry.",
                "question_hi": "X, Y और Z 5:3:2 के अनुपात में लाभ साझा करने वाले भागीदार हैं। वे भविष्य के मुनाफे को समान रूप से (1:1:1) साझा करने का निर्णय लेते हैं। फर्म की ख्याति (Goodwill) का मूल्य ₹90,000 है।\nप्रत्येक भागीदार के त्याग/लाभ की गणना करें और आवश्यक जर्नल प्रविष्टि पारित करें।",
                "question_gu": "X, Y અને Z 5:3:2 ના પ્રમાણમાં નફો વહેંચતા ભાગીદારો છે. તેઓ ભવિષ્યના નફાને સમાન રીતે (1:1:1) વહેંચવાનું નક્કી કરે છે. પેઢીની પાઘડીનું મૂલ્ય ₹90,000 નક્કી કરવામાં આવ્યું છે.\nદરેક ભાગીદારના ત્યાગ/લાભની ગણતરી કરો અને જરૂરી આમનોંધ પસાર કરો.",
                "solution": "Step 1: Calculate Sacrifice or Gain (Old Share - New Share)\nOld Ratio = 5:3:2 (Base = 10)\nNew Ratio = 1:1:1 (Base = 3)\n\nLCM of 10 and 3 is 30.\n\nX = (5/10) - (1/3) = (15 - 10) / 30 = **5/30 (Positive = Sacrifice)**\nY = (3/10) - (1/3) = (9 - 10) / 30 = **-1/30 (Negative = Gain)**\nZ = (2/10) - (1/3) = (6 - 10) / 30 = **-4/30 (Negative = Gain)**\n\nStep 2: Calculate Goodwill Compensation\nTotal Goodwill = ₹90,000\nX (Sacrificed) will receive = 90,000 × (5/30) = **₹15,000**\nY (Gained) will pay = 90,000 × (1/30) = **₹3,000**\nZ (Gained) will pay = 90,000 × (4/30) = **₹12,000**\n\nStep 3: Journal Entry\n| Date | Particulars | L.F. | Debit (₹) | Credit (₹) |\n| :--- | :--- | :--- | :--- | :--- |\n| | Y's Capital A/c ... Dr. | | 3,000 | |\n| | Z's Capital A/c ... Dr. | | 12,000 | |\n| |    To X's Capital A/c | | | 15,000 |\n| | (Being goodwill adjusted due to change in ratio) | | | |",
                "solution_hi": "(अंग्रेजी समाधान के समान, गणितीय गणना देखें। Y और Z को डेबिट किया जाएगा, X को क्रेडिट किया जाएगा।)",
                "solution_gu": "(અંગ્રેજી ઉકેલ સમાન, ગાણિતિક ગણતરી જુઓ. Y અને Z ઉધાર થશે, X જમા થશે.)",
                "id": "KOBJ_CBSE_ACC12_CH3_NUME_005"
            }
        ]
    }
    save_json('app_core/chapters/cbse_class12_accounts_ch3.json', data)

def gen_ch4():
    data = {
        "metadata": {
            "id": "cbse_class12_accounts_ch4",
            "title": "Admission of a Partner",
            "title_hi": "एक साझेदार का प्रवेश",
            "title_gu": "ભાગીદારનો પ્રવેશ",
            "subject": "Accountancy",
            "subject_hi": "लेखाशास्त्र",
            "subject_gu": "નામાનાં મૂળતત્ત્વો",
            "grade": "12",
            "board": "CBSE",
            "curriculum": ["CBSE"],
            "difficulty": "Advanced",
            "estimated_minutes": 150,
            "learning_outcomes": [
                "Understand the legal provisions regarding the admission of a new partner.",
                "Calculate the New Profit Sharing Ratio and Sacrificing Ratio.",
                "Pass journal entries for the premium for Goodwill brought by the new partner.",
                "Prepare Revaluation Account, Partner Capital Accounts, and the New Balance Sheet."
            ],
            "learning_outcomes_hi": [
                "नए साझेदार के प्रवेश के संबंध में कानूनी प्रावधानों को समझें।",
                "नए लाभ साझाकरण अनुपात और त्याग अनुपात की गणना करें।",
                "नए भागीदार द्वारा लाए गए ख्याति के प्रीमियम के लिए जर्नल प्रविष्टियां पारित करें।",
                "पुनर्मूल्यांकन खाता, भागीदार पूंजी खाते और नई बैलेंस शीट तैयार करें।"
            ],
            "learning_outcomes_gu": [
                "નવા ભાગીદારના પ્રવેશ અંગેની કાનૂની જોગવાઈઓ સમજો.",
                "નફા-નુકસાનનું નવું પ્રમાણ અને ત્યાગના પ્રમાણની ગણતરી કરો.",
                "નવા ભાગીદાર દ્વારા લાવવામાં આવેલ પાઘડીના પ્રીમિયમ માટે આમનોંધ પસાર કરો.",
                "પુનઃમૂલ્યાંકન ખાતું, ભાગીદારોના મૂડી ખાતા અને નવું પાકું સરવૈયું તૈયાર કરો."
            ],
            "core_concepts": [
                "Admission of Partner",
                "Premium for Goodwill",
                "Hidden Goodwill",
                "Revaluation of Assets and Liabilities",
                "Accumulated Profits and Reserves",
                "Capital Adjustment"
            ],
            "ai_context": {
                "learning_goal": "Understand the comprehensive accounting treatment when a new partner brings capital and goodwill to join an existing business.",
                "common_misconceptions": [
                    "Distributing accumulated reserves in the new ratio (they belong to old partners in the old ratio!).",
                    "Crediting the Premium for Goodwill in the old ratio instead of the sacrificing ratio."
                ]
            }
        },
        "blocks": [
            {
                "type": "theory",
                "content": "A business is expanding rapidly. The existing partners need more capital to open a new branch, and they also need a person with exceptional marketing skills. They decide to bring in a third person. \nAccording to Section 31(1) of the Indian Partnership Act, 1932, a new partner can be admitted ONLY with the consent of **ALL** existing partners.",
                "content_hi": "एक व्यवसाय तेजी से विस्तार कर रहा है। मौजूदा साझेदारों को नई शाखा खोलने के लिए अधिक पूंजी की आवश्यकता है, और उन्हें असाधारण मार्केटिंग कौशल वाले व्यक्ति की भी आवश्यकता है। वे तीसरे व्यक्ति को लाने का निर्णय लेते हैं।\nभारतीय साझेदारी अधिनियम, 1932 की धारा 31(1) के अनुसार, एक नए भागीदार को **सभी** मौजूदा भागीदारों की सहमति से ही भर्ती किया जा सकता है।",
                "content_gu": "એક વ્યવસાય ઝડપથી વિસ્તરી રહ્યો છે. વર્તમાન ભાગીદારોને નવી શાખા ખોલવા માટે વધુ મૂડીની જરૂર છે, અને તેમને અસાધારણ માર્કેટિંગ કુશળતા ધરાવતા વ્યક્તિની પણ જરૂર છે. તેઓ ત્રીજી વ્યક્તિને લાવવાનું નક્કી કરે છે.\nભારતીય ભાગીદારી અધિનિયમ, 1932 ની કલમ 31(1) મુજબ, નવા ભાગીદારને **તમામ** વર્તમાન ભાગીદારોની સંમતિથી જ દાખલ કરી શકાય છે.",
                "id": "KOBJ_CBSE_ACC12_CH4_THEO_001"
            },
            {
                "type": "quiz",
                "question": "A, B, and C are partners. They want to admit D as a new partner. A and B agree, but C strongly opposes. Can D be admitted?",
                "question_hi": "A, B, और C भागीदार हैं। वे D को नए भागीदार के रूप में भर्ती करना चाहते हैं। A और B सहमत हैं, लेकिन C कड़ा विरोध करता है। क्या D को भर्ती किया जा सकता है?",
                "question_gu": "A, B, અને C ભાગીદારો છે. તેઓ D ને નવા ભાગીદાર તરીકે દાખલ કરવા માંગે છે. A અને B સંમત થાય છે, પરંતુ C સખત વિરોધ કરે છે. શું D ને દાખલ કરી શકાય?",
                "options": [
                    "Yes, because the majority (A and B) agreed.",
                    "No, because admission requires the unanimous consent of ALL existing partners.",
                    "Yes, but D will only get a share from A and B.",
                    "Yes, if D pays extra money to C."
                ],
                "options_hi": [
                    "हाँ, क्योंकि बहुमत (A और B) सहमत थे।",
                    "नहीं, क्योंकि प्रवेश के लिए सभी मौजूदा भागीदारों की सर्वसम्मत सहमति की आवश्यकता होती है।",
                    "हाँ, लेकिन D को केवल A और B से हिस्सा मिलेगा।",
                    "हाँ, यदि D, C को अतिरिक्त धन का भुगतान करता है।"
                ],
                "options_gu": [
                    "હા, કારણ કે બહુમતી (A અને B) સંમત થયા હતા.",
                    "ના, કારણ કે પ્રવેશ માટે તમામ વર્તમાન ભાગીદારોની સર્વસંમત સંમતિની જરૂર છે.",
                    "હા, પરંતુ D ને માત્ર A અને B પાસેથી જ હિસ્સો મળશે.",
                    "હા, જો D, C ને વધારાના પૈસા ચૂકવે છે."
                ],
                "correct_index": 1,
                "explanation": "Every single partner must agree. Even one dissenting voice blocks the admission.",
                "explanation_hi": "हर एक साथी को सहमत होना चाहिए। यहां तक कि एक असहमति वाली आवाज भी प्रवेश को रोक देती है।",
                "explanation_gu": "દરેક ભાગીદાર સંમત થવો જોઈએ. એક અસંમતિનો અવાજ પણ પ્રવેશને અવરોધે છે.",
                "id": "KOBJ_CBSE_ACC12_CH4_QUIZ_002"
            },
            {
                "type": "theory",
                "content": "**The Two Main Contributions of a New Partner**\nWhen a new partner enters, he acquires two rights:\n1. Right to share the **Assets** of the firm. For this, he brings **Capital**.\n2. Right to share the future **Profits** of the firm. For this, he brings an extra amount called **Premium for Goodwill** to compensate the old partners who are sacrificing a piece of their profit share for him.",
                "content_hi": "**एक नए भागीदार के दो मुख्य योगदान**\nजब कोई नया भागीदार प्रवेश करता है, तो वह दो अधिकार प्राप्त करता है:\n1. फर्म की **संपत्ति** साझा करने का अधिकार। इसके लिए वह **पूंजी (Capital)** लाता है।\n2. फर्म के भविष्य के **मुनाफे** को साझा करने का अधिकार। इसके लिए, वह **प्रीमियम फॉर गुडविल** नामक एक अतिरिक्त राशि लाता है जो पुराने भागीदारों को मुआवजा देने के लिए है, जो उसके लिए अपने लाभ के हिस्से का त्याग कर रहे हैं।",
                "content_gu": "**નવા ભાગીદારના બે મુખ્ય યોગદાન**\nજ્યારે નવો ભાગીદાર પ્રવેશે છે, ત્યારે તે બે અધિકારો પ્રાપ્ત કરે છે:\n1. પેઢીની **મિલકતો** વહેંચવાનો અધિકાર. આ માટે, તે **મૂડી (Capital)** લાવે છે.\n2. પેઢીના ભવિષ્યના **નફા** વહેંચવાનો અધિકાર. આ માટે, તે **પાઘડીનું પ્રીમિયમ (Premium for Goodwill)** નામની વધારાની રકમ લાવે છે જે જૂના ભાગીદારોને વળતર આપવા માટે છે, જેઓ તેના માટે તેમના નફાના હિસ્સાનું બલિદાન આપી રહ્યા છે.",
                "id": "KOBJ_CBSE_ACC12_CH4_THEO_003"
            },
            {
                "type": "common_mistakes",
                "content": "DANGER ZONE: When the new partner brings the Premium for Goodwill in cash, you MUST distribute this premium to the old partners ONLY in their **Sacrificing Ratio**, never in their Old Ratio (unless Old Ratio = Sacrificing Ratio).",
                "content_hi": "खतरे का क्षेत्र: जब नया भागीदार नकद में ख्याति के लिए प्रीमियम लाता है, तो आपको इस प्रीमियम को पुराने भागीदारों को केवल उनके **त्याग अनुपात (Sacrificing Ratio)** में वितरित करना चाहिए, कभी भी उनके पुराने अनुपात में नहीं (जब तक कि पुराना अनुपात = त्याग अनुपात न हो)।",
                "content_gu": "ડેન્જર ઝોન: જ્યારે નવો ભાગીદાર રોકડમાં પાઘડી માટે પ્રીમિયમ લાવે છે, ત્યારે તમારે આ પ્રીમિયમ જૂના ભાગીદારોને ફક્ત તેમના **ત્યાગના પ્રમાણમાં (Sacrificing Ratio)** વહેંચવું જોઈએ, ક્યારેય તેમના જૂના પ્રમાણમાં નહીં (જ્યાં સુધી જૂનું પ્રમાણ = ત્યાગનું પ્રમાણ ન હોય).",
                "id": "KOBJ_CBSE_ACC12_CH4_COMM_004"
            }
        ]
    }
    save_json('app_core/chapters/cbse_class12_accounts_ch4.json', data)

if __name__ == "__main__":
    gen_ch2()
    gen_ch3()
    gen_ch4()
