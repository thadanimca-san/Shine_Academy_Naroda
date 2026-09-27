import json
import os

def save_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Generated {file_path} successfully!")

def gen_part1_ch3():
    data = {
        "metadata": {
            "id": "gseb_class11_spcc_p1_ch3",
            "title": "Physical Appearance of a Business Letter",
            "title_hi": "व्यावसायिक पत्र का भौतिक स्वरूप",
            "title_gu": "વાણિજ્યિક પત્રનો ભૌતિક દેખાવ",
            "subject": "SPCC",
            "grade": "11",
            "board": "GSEB",
            "curriculum": ["GSEB"],
            "difficulty": "Beginner",
            "estimated_minutes": 60,
            "learning_outcomes": [
                "Understand the importance of paper quality in letter writing.",
                "Learn about margins, typing, and folding of a commercial letter.",
                "Identify different types of envelopes and their uses."
            ]
        },
        "blocks": [
            {
                "type": "theory",
                "content": "Imagine going to a highly anticipated job interview wearing unwashed, wrinkled clothes. No matter how smart you are, the first impression is ruined. \nSimilarly, a business letter is the 'representative' of a company. Before the receiver even reads a single word, they judge the company based on the **Physical Appearance** of the letter. The paper, envelope, margin, and folding speak volumes about the company's status.",
                "content_hi": "कल्पना कीजिए कि आप बिना धुले, झुर्रीदार कपड़े पहनकर बहुप्रतीक्षित नौकरी के साक्षात्कार के लिए जा रहे हैं। आप चाहे कितने भी चतुर क्यों न हों, पहली छाप खराब हो जाती है।\nइसी तरह, एक व्यावसायिक पत्र कंपनी का 'प्रतिनिधि' होता है। इससे पहले कि प्राप्तकर्ता एक शब्द भी पढ़े, वे पत्र के **भौतिक स्वरूप** के आधार पर कंपनी का न्याय करते हैं। कागज, लिफाफा, हाशिया (Margin) और तह (Folding) कंपनी की स्थिति के बारे में बहुत कुछ बताते हैं।",
                "content_gu": "કલ્પના કરો કે તમે ધોયા વિનાના, કરચલીવાળા કપડાં પહેરીને ખૂબ જ અપેક્ષિત નોકરીના ઇન્ટરવ્યુ માટે જઈ રહ્યા છો. તમે ગમે તેટલા સ્માર્ટ હોવ, પ્રથમ છાપ બગડી જાય છે.\nતેવી જ રીતે, વાણિજ્યિક પત્ર એ કંપનીનો 'પ્રતિનિધિ' છે. મેળવનાર એક શબ્દ પણ વાંચે તે પહેલાં, તેઓ પત્રના **ભૌતિક દેખાવ** ના આધારે કંપનીનો ન્યાય કરે છે. કાગળ, પરબીડિયું, માર્જિન અને ફોલ્ડિંગ કંપનીની સ્થિતિ વિશે ઘણું કહે છે.",
                "id": "KOBJ_GSEB_11SPCC_P1C3_THEO_001"
            },
            {
                "type": "quiz",
                "question": "Socratic Question: Why is it advised to use only high-quality paper for commercial letters?",
                "question_hi": "सॉक्रेटिक प्रश्न: व्यावसायिक पत्रों के लिए केवल उच्च गुणवत्ता वाले कागज का उपयोग करने की सलाह क्यों दी जाती है?",
                "question_gu": "સોક્રેટિક પ્રશ્ન: વાણિજ્યિક પત્રો માટે માત્ર ઉચ્ચ ગુણવત્તાવાળા કાગળનો ઉપયોગ કરવાની સલાહ શા માટે આપવામાં આવે છે?",
                "options": [
                    "Because low-quality paper ink spreads and it ruins the company's image.",
                    "Because high-quality paper is cheaper.",
                    "Because it is required by government law.",
                    "Because low-quality paper weighs more."
                ],
                "options_hi": [
                    "क्योंकि कम गुणवत्ता वाले कागज की स्याही फैलती है और यह कंपनी की छवि को खराब करती है।",
                    "क्योंकि उच्च गुणवत्ता वाला कागज सस्ता होता है।",
                    "क्योंकि यह सरकारी कानून द्वारा आवश्यक है।",
                    "क्योंकि कम गुणवत्ता वाले कागज का वजन अधिक होता है।"
                ],
                "options_gu": [
                    "કારણ કે ઓછી ગુણવત્તાવાળા કાગળની શાહી ફેલાય છે અને તે કંપનીની છબીને બગાડે છે.",
                    "કારણ કે ઉચ્ચ ગુણવત્તાવાળા કાગળ સસ્તા હોય છે.",
                    "કારણ કે તે સરકારી કાયદા દ્વારા જરૂરી છે.",
                    "કારણ કે ઓછી ગુણવત્તાવાળા કાગળનું વજન વધુ હોય છે."
                ],
                "correct_index": 0,
                "explanation": "A high-quality paper reflects professionalism. Low-quality paper may cause the ink to blot, look unprofessional, and tear easily during transit.",
                "explanation_hi": "एक उच्च गुणवत्ता वाला कागज व्यावसायिकता को दर्शाता है। कम गुणवत्ता वाले कागज के कारण स्याही धब्बेदार हो सकती है, अव्यावसायिक दिख सकती है, और पारगमन के दौरान आसानी से फट सकती है।",
                "explanation_gu": "ઉચ્ચ ગુણવત્તાવાળો કાગળ વ્યાવસાયિકતા (Professionalism) દર્શાવે છે. ઓછી ગુણવત્તાવાળા કાગળને કારણે શાહી ફેલાઈ શકે છે, અવ્યાવસાયિક દેખાઈ શકે છે અને પરિવહન દરમિયાન સરળતાથી ફાટી શકે છે.",
                "id": "KOBJ_GSEB_11SPCC_P1C3_QUIZ_002"
            },
            {
                "type": "theory",
                "content": "**Margins in Letter Writing**\nA margin is the blank space left around the text on a paper. It makes the letter look attractive and saves the text from getting torn or punched out when filed. \nTypically, a margin of **1.5 inches** is kept on the **Left side** (for filing) and **1 inch** on the **Right side**. Similarly, margins are kept at the top and bottom.",
                "content_hi": "**पत्र लेखन में हाशिया (Margin)**\nहाशिया कागज पर पाठ (Text) के चारों ओर छोड़ा गया खाली स्थान है। यह पत्र को आकर्षक बनाता है और फाइल किए जाने पर पाठ को फटने या छिद्रित होने से बचाता है।\nआमतौर पर, **बाईं ओर (Left side) 1.5 इंच** का हाशिया (फाइलिंग के लिए) और **दाईं ओर 1 इंच** का हाशिया रखा जाता है। इसी तरह ऊपर और नीचे भी हाशिये रखे जाते हैं।",
                "content_gu": "**પત્ર લેખનમાં માર્જિન (Margin)**\nમાર્જિન એ કાગળ પર લખાણ (Text) ની આસપાસ છોડવામાં આવેલી ખાલી જગ્યા છે. તે પત્રને આકર્ષક બનાવે છે અને જ્યારે ફાઇલ કરવામાં આવે ત્યારે લખાણને ફાટી જવાથી કે પંચ થવાથી બચાવે છે.\nસામાન્ય રીતે, **ડાબી બાજુએ (Left side) 1.5 ઇંચ** (ફાઇલિંગ માટે) અને **જમણી બાજુએ 1 ઇંચ** માર્જિન રાખવામાં આવે છે. એ જ રીતે, ઉપર અને નીચે પણ માર્જિન રાખવામાં આવે છે.",
                "id": "KOBJ_GSEB_11SPCC_P1C3_THEO_003"
            },
            {
                "type": "teacher_tip",
                "content": "**Types of Envelopes & Their Uses:**\n1. **Window Envelope:** It has a transparent cut-out showing the receiver's address printed on the letter inside. Used by banks & LIC to save time writing addresses.\n2. **Closed Envelope:** Standard opaque envelope for confidential letters.\n3. **Open Envelope:** Unsealed envelope used for sending circulars or greeting cards (postage is cheaper).",
                "content_hi": "**लिफाफे के प्रकार और उनके उपयोग:**\n1. **विंडो लिफाफा (Window Envelope):** इसमें एक पारदर्शी कट-आउट होता है जो अंदर पत्र पर छपे प्राप्तकर्ता का पता दिखाता है। पता लिखने का समय बचाने के लिए बैंकों और एलआईसी द्वारा उपयोग किया जाता है।\n2. **बंद लिफाफा (Closed Envelope):** गोपनीय पत्रों के लिए मानक अपारदर्शी लिफाफा।\n3. **खुला लिफाफा (Open Envelope):** परिपत्र (Circulars) या ग्रीटिंग कार्ड भेजने के लिए उपयोग किया जाने वाला बिना सील किया गया लिफाफा (डाक खर्च सस्ता होता है)।",
                "content_gu": "**પરબીડિયાના પ્રકાર અને તેના ઉપયોગો:**\n1. **બારીવાળું પરબીડિયું (Window Envelope):** તેમાં પારદર્શક કટ-આઉટ હોય છે જે અંદરના પત્ર પર છાપેલ મેળવનારનું સરનામું દર્શાવે છે. સરનામું લખવાનો સમય બચાવવા માટે બેંકો અને LIC દ્વારા વપરાય છે.\n2. **બંધ પરબીડિયું (Closed Envelope):** ગોપનીય પત્રો માટે પ્રમાણભૂત અપારદર્શક પરબીડિયું.\n3. **ખુલ્લું પરબીડિયું (Open Envelope):** પરિપત્રો (Circulars) અથવા ગ્રીટિંગ કાર્ડ મોકલવા માટે વપરાતું સીલ વિનાનું પરબીડિયું (ટપાલ ખર્ચ સસ્તો છે).",
                "id": "KOBJ_GSEB_11SPCC_P1C3_TEAC_004"
            }
        ]
    }
    save_json('app_core/chapters/gseb_class11_spcc_part1_ch3.json', data)

def gen_part1_ch4():
    data = {
        "metadata": {
            "id": "gseb_class11_spcc_p1_ch4",
            "title": "Layout of a Business Letter",
            "title_hi": "व्यावसायिक पत्र का लेआउट",
            "title_gu": "વાણિજ્યિક પત્રનું માળખું (લેઆઉટ)",
            "subject": "SPCC",
            "grade": "11",
            "board": "GSEB",
            "curriculum": ["GSEB"],
            "difficulty": "Intermediate",
            "estimated_minutes": 60,
            "learning_outcomes": [
                "Understand the Compulsory parts of a business letter.",
                "Understand the Occasional parts of a business letter.",
                "Write dates using American and British methods.",
                "Understand the use of the Attention Line and Mailing Instructions."
            ]
        },
        "blocks": [
            {
                "type": "theory",
                "content": "**Compulsory Parts vs Occasional Parts**\nA business letter has a specific structure. Some parts are absolutely mandatory, without which the letter is legally or practically useless. These are **Compulsory Parts** (e.g., Heading, Date, Inside Address, Salutation, Body of Letter, Complimentary Close, Signature).\nOther parts are used only when needed. These are **Occasional Parts** (e.g., Personal/Mailing Instruction, Attention Line, Subject Line, Enclosures, Carbon Copy (CC)).",
                "content_hi": "**अनिवार्य भाग बनाम सामयिक (Occasional) भाग**\nएक व्यावसायिक पत्र की एक विशिष्ट संरचना होती है। कुछ भाग बिल्कुल अनिवार्य हैं, जिनके बिना पत्र कानूनी या व्यावहारिक रूप से बेकार है। ये **अनिवार्य भाग (Compulsory Parts)** हैं (जैसे, शीर्षक, दिनांक, अंदर का पता, अभिवादन, पत्र का मुख्य भाग, मानार्थ समापन, हस्ताक्षर)।\nअन्य भागों का उपयोग केवल आवश्यकता पड़ने पर ही किया जाता है। ये **सामयिक भाग (Occasional Parts)** हैं (जैसे, व्यक्तिगत/मेलिंग निर्देश, ध्यान रेखा, विषय रेखा, संलग्नक, कार्बन कॉपी)।",
                "content_gu": "**ફરજિયાત ભાગો વિરુદ્ધ પ્રસંગોપાત ભાગો**\nવાણિજ્યિક પત્રનું ચોક્કસ માળખું હોય છે. કેટલાક ભાગો બિલકુલ ફરજિયાત છે, જેના વિના પત્ર કાયદેસર અથવા વ્યવહારિક રીતે નકામો છે. આ **ફરજિયાત ભાગો (Compulsory Parts)** છે (દા.ત., શીર્ષક, તારીખ, અંદરનું સરનામું, સંબોધન, પત્રનો મુખ્ય ભાગ, સમાપન, સહી).\nઅન્ય ભાગોનો ઉપયોગ માત્ર જરૂર પડે ત્યારે જ થાય છે. આ **પ્રસંગોપાત ભાગો (Occasional Parts)** છે (દા.ત., વ્યક્તિગત/મેઇલિંગ સૂચના, ધ્યાન આકર્ષક રેખા, વિષય રેખા, બિડાણ, કાર્બન કોપી).",
                "id": "KOBJ_GSEB_11SPCC_P1C4_THEO_001"
            },
            {
                "type": "theory",
                "content": "**Writing Dates: American vs British Method**\n1. **American Method:** Month is written first, followed by the date and year. A comma separates the date and year. \n*Example:* January 15, 2024\n2. **British Method:** Date is written first (with st, nd, rd, th), followed by the month and year. \n*Example:* 15th January, 2024\n\n*Note: NEVER write dates in numbers like 15/01/2024 in a formal business letter!*",
                "content_hi": "**तिथियां लिखना: अमेरिकी बनाम ब्रिटिश विधि**\n1. **अमेरिकी विधि:** महीना पहले लिखा जाता है, उसके बाद तारीख और वर्ष। एक अल्पविराम (Comma) तारीख और वर्ष को अलग करता है।\n*उदाहरण:* January 15, 2024\n2. **ब्रिटिश विधि:** तारीख पहले लिखी जाती है (st, nd, rd, th के साथ), उसके बाद महीना और वर्ष।\n*उदाहरण:* 15th January, 2024\n\n*नोट: औपचारिक व्यावसायिक पत्र में कभी भी 15/01/2024 जैसे नंबरों में तिथियां न लिखें!*",
                "content_gu": "**તારીખો લખવી: અમેરિકન વિરુદ્ધ બ્રિટિશ પદ્ધતિ**\n1. **અમેરિકન પદ્ધતિ:** મહિનો પહેલા લખાય છે, ત્યારબાદ તારીખ અને વર્ષ. અલ્પવિરામ (Comma) તારીખ અને વર્ષને અલગ કરે છે.\n*ઉદાહરણ:* January 15, 2024\n2. **બ્રિટિશ પદ્ધતિ:** તારીખ પહેલા લખવામાં આવે છે (st, nd, rd, th સાથે), ત્યારબાદ મહિનો અને વર્ષ.\n*ઉદાહરણ:* 15th January, 2024\n\n*નોંધ: ઔપચારિક વાણિજ્યિક પત્રમાં ક્યારેય 15/01/2024 જેવા નંબરોમાં તારીખો લખશો નહીં!*",
                "id": "KOBJ_GSEB_11SPCC_P1C4_THEO_002"
            },
            {
                "type": "teacher_tip",
                "content": "**Attention Line:** Sometimes a letter is addressed to a large company (e.g., Reliance), but the sender wants only a specific manager to open and read it. In this case, an 'Attention Line' is placed between the Inside Address and Salutation. \n*Example: For the Attention of Mr. Shah (Purchase Manager)*",
                "content_hi": "**ध्यान रेखा (Attention Line):** कभी-कभी एक पत्र एक बड़ी कंपनी (जैसे, रिलायंस) को संबोधित किया जाता है, लेकिन प्रेषक चाहता है कि केवल एक विशिष्ट प्रबंधक ही इसे खोले और पढ़े। इस मामले में, अंदर के पते और अभिवादन के बीच एक 'ध्यान रेखा' रखी जाती है।\n*उदाहरण: For the Attention of Mr. Shah (Purchase Manager)*",
                "content_gu": "**ધ્યાન આકર્ષક રેખા (Attention Line):** કેટલીકવાર પત્ર મોટી કંપની (દા.ત., રિલાયન્સ) ને સંબોધવામાં આવે છે, પરંતુ મોકલનાર ઈચ્છે છે કે માત્ર ચોક્કસ મેનેજર જ તેને ખોલે અને વાંચે. આ કિસ્સામાં, અંદરના સરનામા અને સંબોધન વચ્ચે 'ધ્યાન આકર્ષક રેખા' મૂકવામાં આવે છે.\n*ઉદાહરણ: For the Attention of Mr. Shah (Purchase Manager)*",
                "id": "KOBJ_GSEB_11SPCC_P1C4_TEAC_003"
            }
        ]
    }
    save_json('app_core/chapters/gseb_class11_spcc_part1_ch4.json', data)

def gen_part1_ch5():
    data = {
        "metadata": {
            "id": "gseb_class11_spcc_p1_ch5",
            "title": "Inquiry Letters and their Replies",
            "title_hi": "पूछताछ पत्र और उनके उत्तर",
            "title_gu": "પૂછપરછના પત્રો અને તેના પ્રત્યુત્તરો",
            "subject": "SPCC",
            "grade": "11",
            "board": "GSEB",
            "curriculum": ["GSEB"],
            "difficulty": "Advanced",
            "estimated_minutes": 120,
            "learning_outcomes": [
                "Draft an inquiry letter for purchasing goods.",
                "Draft a reply to an inquiry letter providing quotations and terms.",
                "Understand specific terms like Quotation, Catalogue, and Terms of Payment."
            ]
        },
        "blocks": [
            {
                "type": "theory",
                "content": "Before making a large purchase, a businessman needs information about price, quality, discount, and payment terms. He doesn't just call; he writes a formal **Inquiry Letter** to various sellers. \nThe seller reads the inquiry and sends back a **Reply to Inquiry (Quotation Letter)** detailing the exact prices, delivery timelines, and conditions.",
                "content_hi": "बड़ी खरीदारी करने से पहले, एक व्यवसायी को कीमत, गुणवत्ता, छूट और भुगतान की शर्तों के बारे में जानकारी की आवश्यकता होती है। वह केवल फोन नहीं करता; वह विभिन्न विक्रेताओं को एक औपचारिक **पूछताछ पत्र (Inquiry Letter)** लिखता है।\nविक्रेता पूछताछ को पढ़ता है और सटीक कीमतों, डिलीवरी समयसीमा और शर्तों का विवरण देते हुए **पूछताछ का उत्तर (Quotation Letter)** वापस भेजता है।",
                "content_gu": "મોટી ખરીદી કરતા પહેલા, વેપારીને કિંમત, ગુણવત્તા, વળતર (Discount) અને ચુકવણીની શરતો વિશે માહિતીની જરૂર હોય છે. તે માત્ર ફોન કરતો નથી; તે વિવિધ વેચાણકર્તાઓને ઔપચારિક **પૂછપરછનો પત્ર (Inquiry Letter)** લખે છે.\nવેચાણકર્તા પૂછપરછ વાંચે છે અને ચોક્કસ કિંમતો, ડિલિવરી સમયમર્યાદા અને શરતોની વિગતો આપતો **પૂછપરછનો પ્રત્યુત્તર (Quotation Letter)** પાછો મોકલે છે.",
                "id": "KOBJ_GSEB_11SPCC_P1C5_THEO_001"
            },
            {
                "type": "numerical",
                "question": "On behalf of Tapasvi Tea Traders, Kalol, write a letter to Gujarat Tea Depot, Kalupur, Ahmedabad, inquiring about large scale purchase of different types of tea, their prices, and terms of payment.",
                "question_hi": "तपस्वी टी ट्रेडर्स, कलोल की ओर से गुजरात टी डिपो, कालूपुर, अहमदाबाद को एक पत्र लिखें, जिसमें विभिन्न प्रकार की चाय की बड़े पैमाने पर खरीद, उनकी कीमतों और भुगतान की शर्तों के बारे में पूछताछ की गई हो।",
                "question_gu": "તપસ્વી ટી ટ્રેડર્સ, કલોલ વતી ગુજરાત ટી ડેપો, કાલુપુર, અમદાવાદને એક પત્ર લખો, જેમાં વિવિધ પ્રકારની ચાની મોટા પાયે ખરીદી, તેમની કિંમતો અને ચુકવણીની શરતો વિશે પૂછપરછ કરવામાં આવી હોય.",
                "solution": "**TAPASVI TEA TRADERS**\nStation Road, Kalol - 382721\nPhone: (02764) 223456\nDate: 25th September, 2026\n\nTo,\nThe Manager,\nGujarat Tea Depot,\nKalupur,\nAhmedabad - 380001\n\n**Subject: Inquiry regarding large scale purchase of different types of tea.**\n\nRespected Sir,\n\nWe are a leading wholesaler of tea in Kalol and surrounding areas. The demand for premium quality tea is increasing rapidly in our region as the festival season approaches.\n\nWe came to know through trade directories that you are a prominent supplier of Assam and Darjeeling tea. We intend to purchase approximately 500 kgs of different varieties of tea from you on a regular basis.\n\nKindly send us your latest catalogue, price list, and the terms of payment. Also, clearly state the trade discount you offer on bulk purchases, and the estimated time for transportation.\n\nWe expect a prompt and favorable reply.\n\nYours faithfully,\n\n(Signature)\n(Owner)\nTapasvi Tea Traders",
                "solution_hi": "(अंग्रेजी समाधान देखें। यह एक व्यावसायिक पत्र है। ऊपर प्रेषक का नाम (Tapasvi Tea Traders), फिर प्राप्तकर्ता (Gujarat Tea Depot), विषय और मुख्य भाग आता है।)",
                "solution_gu": "(અંગ્રેજી ઉકેલ જુઓ. આ એક વાણિજ્યિક પત્ર છે. ટોચ પર મોકલનારનું નામ (Tapasvi Tea Traders), પછી મેળવનાર (Gujarat Tea Depot), વિષય અને મુખ્ય ભાગ આવે છે.)",
                "id": "KOBJ_GSEB_11SPCC_P1C5_NUME_002"
            },
            {
                "type": "numerical",
                "question": "Gujarat Tea Depot, Ahmedabad, has received the letter inquiring about quality and price of tea. Draft a suitable reply for it to Tapasvi Tea Traders, Kalol.",
                "question_hi": "गुजरात टी डिपो, अहमदाबाद को चाय की गुणवत्ता और कीमत के बारे में पूछताछ करने वाला पत्र मिला है। तपस्वी टी ट्रेडर्स, कलोल के लिए इसका उपयुक्त उत्तर (Reply) तैयार करें।",
                "question_gu": "ગુજરાત ટી ડેપો, અમદાવાદને ચાની ગુણવત્તા અને કિંમત વિશે પૂછપરછ કરતો પત્ર મળ્યો છે. તપસ્વી ટી ટ્રેડર્સ, કલોલ માટે તેનો યોગ્ય પ્રત્યુત્તર (Reply) તૈયાર કરો.",
                "solution": "**GUJARAT TEA DEPOT**\nKalupur, Ahmedabad - 380001\nEmail: sales@gujarattea.in\nDate: 28th September, 2026\n\nTo,\nThe Owner,\nTapasvi Tea Traders,\nStation Road,\nKalol - 382721\n\n**Subject: Reply to your inquiry about tea purchase.**\n**Reference: Your letter dated 25th September, 2026.**\n\nRespected Sir,\n\nWe thank you for your letter dated 25th September inquiring about our tea products. We are delighted to know your interest in our Assam and Darjeeling tea varieties.\n\nAs requested, we have enclosed our latest catalogue and price list with this letter. Since you are planning a bulk purchase of 500 kgs, we are happy to offer you a special Trade Discount of 10% on the catalogue prices.\n\n**Terms of Payment:** 50% advance along with the order, and the remaining 50% within 15 days of delivery.\n**Transportation:** Goods will be dispatched via local transport within 3 days of receiving the advance payment.\n\nWe look forward to receiving a large order from you soon.\n\nYours faithfully,\n\n(Signature)\n(Sales Manager)\nGujarat Tea Depot\n\n**Enclosure:** Catalogue and Price List.",
                "solution_hi": "(अंग्रेजी समाधान देखें। यह एक उत्तर पत्र है। इसमें संदर्भ (Reference) और छूट (Discount) का उल्लेख किया गया है।)",
                "solution_gu": "(અંગ્રેજી ઉકેલ જુઓ. આ એક પ્રત્યુત્તર પત્ર છે. તેમાં સંદર્ભ (Reference) અને વળતર (Discount) નો ઉલ્લેખ કરવામાં આવ્યો છે.)",
                "id": "KOBJ_GSEB_11SPCC_P1C5_NUME_003"
            }
        ]
    }
    save_json('app_core/chapters/gseb_class11_spcc_part1_ch5.json', data)

if __name__ == "__main__":
    gen_part1_ch3()
    gen_part1_ch4()
    gen_part1_ch5()
