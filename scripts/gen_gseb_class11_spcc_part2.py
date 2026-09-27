import json
import os

def save_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Generated {file_path} successfully!")

def gen_part2_ch1():
    data = {
        "metadata": {
            "id": "gseb_class11_spcc_p2_ch1",
            "title": "Meaning and Types of Secretary",
            "title_hi": "सचिव का अर्थ और प्रकार",
            "title_gu": "સેક્રેટરીનો અર્થ અને પ્રકારો",
            "subject": "SPCC",
            "grade": "11",
            "board": "GSEB",
            "curriculum": ["GSEB"],
            "difficulty": "Beginner",
            "estimated_minutes": 60,
            "learning_outcomes": [
                "Understand the meaning of the word 'Secretary'.",
                "Learn about the historical use of secretaries (Mantri).",
                "Identify different types of secretaries (Private, Ministerial, Embassy, Company)."
            ]
        },
        "blocks": [
            {
                "type": "theory",
                "content": "**The Origin of the Word 'Secretary'**\nIn olden days, kings and emperors had highly trusted individuals who kept their secrets and handled important correspondence. In India, they were called **'Mantri' or 'Sachiv'**. For example, Chanakya was a Mantri for Chandragupta Maurya.\nThe English word 'Secretary' comes from the Latin word **'Secretarius'**, which means a person entrusted with a secret.",
                "content_hi": "**'सचिव' (Secretary) शब्द की उत्पत्ति**\nपुराने दिनों में, राजाओं और सम्राटों के पास अत्यधिक विश्वसनीय व्यक्ति होते थे जो उनके रहस्य रखते थे और महत्वपूर्ण पत्राचार संभालते थे। भारत में, उन्हें **'मंत्री' या 'सचिव'** कहा जाता था। उदाहरण के लिए, चाणक्य चंद्रगुप्त मौर्य के लिए एक मंत्री थे।\nअंग्रेजी शब्द 'सेक्रेटरी' लैटिन शब्द **'Secretarius'** से आया है, जिसका अर्थ है एक व्यक्ति जिसे किसी रहस्य के साथ सौंपा गया हो।",
                "content_gu": "**'સેક્રેટરી' (Secretary) શબ્દની ઉત્પત્તિ**\nજૂના સમયમાં, રાજાઓ અને સમ્રાટો પાસે અત્યંત વિશ્વાસુ વ્યક્તિઓ હતી જેઓ તેમના રહસ્યો રાખતા હતા અને મહત્વપૂર્ણ પત્રવ્યવહાર સંભાળતા હતા. ભારતમાં, તેમને **'મંત્રી' અથવા 'સચિવ'** કહેવામાં આવતા હતા. ઉદાહરણ તરીકે, ચાણક્ય ચંદ્રગુપ્ત મૌર્ય માટે મંત્રી હતા.\nઅંગ્રેજી શબ્દ 'સેક્રેટરી' લેટિન શબ્દ **'Secretarius'** પરથી આવ્યો છે, જેનો અર્થ થાય છે રહસ્ય જાળવનાર વ્યક્તિ.",
                "id": "KOBJ_GSEB_11SPCC_P2C1_THEO_001"
            },
            {
                "type": "theory",
                "content": "**Types of Secretaries**\n1. **Personal / Private Secretary (PA):** Appointed by busy professionals (doctors, lawyers, politicians, actors) to manage their schedules, phone calls, and daily tasks.\n2. **Ministerial Secretary:** Appointed by government ministers to run their respective departments smoothly (e.g., Education Secretary, Finance Secretary).\n3. **Secretary of Embassy (Ambassador):** Appointed by the Central Government to represent our country in a foreign nation and protect our citizens' interests there.\n4. **Company Secretary:** An essential officer appointed by the Board of Directors of a company to ensure legal compliance.",
                "content_hi": "**सचिव के प्रकार**\n1. **व्यक्तिगत / निजी सचिव (PA):** व्यस्त पेशेवरों (डॉक्टर, वकील, राजनेता, अभिनेता) द्वारा उनके कार्यक्रम, फोन कॉल और दैनिक कार्यों का प्रबंधन करने के लिए नियुक्त किया जाता है।\n2. **विभागीय सचिव (Ministerial Secretary):** सरकारी मंत्रियों द्वारा अपने संबंधित विभागों को सुचारू रूप से चलाने के लिए नियुक्त किया जाता है (जैसे, शिक्षा सचिव, वित्त सचिव)।\n3. **दूतावास के सचिव (राजदूत):** विदेशी राष्ट्र में हमारे देश का प्रतिनिधित्व करने और वहां हमारे नागरिकों के हितों की रक्षा करने के लिए केंद्र सरकार द्वारा नियुक्त किया जाता है।\n4. **कंपनी सचिव:** कानूनी अनुपालन सुनिश्चित करने के लिए कंपनी के निदेशक मंडल द्वारा नियुक्त एक आवश्यक अधिकारी।",
                "content_gu": "**સેક્રેટરીના પ્રકારો**\n1. **અંગત / ખાનગી સેક્રેટરી (PA):** વ્યસ્ત વ્યાવસાયિકો (ડોકટરો, વકીલો, રાજકારણીઓ, કલાકારો) દ્વારા તેમના સમયપત્રક, ફોન કૉલ્સ અને દૈનિક કાર્યોનું સંચાલન કરવા માટે નિમણૂક કરવામાં આવે છે.\n2. **વિભાગીય સેક્રેટરી (Ministerial Secretary):** સરકારી મંત્રીઓ દ્વારા તેમના સંબંધિત વિભાગોને સરળ રીતે ચલાવવા માટે નિમણૂક કરવામાં આવે છે (દા.ત., શિક્ષણ સચિવ, નાણા સચિવ).\n3. **દૂતાવાસના સેક્રેટરી (રાજદૂત):** વિદેશી રાષ્ટ્રમાં આપણા દેશનું પ્રતિનિધિત્વ કરવા અને ત્યાં આપણા નાગરિકોના હિતોનું રક્ષણ કરવા કેન્દ્ર સરકાર દ્વારા નિમણૂક કરવામાં આવે છે.\n4. **કંપની સેક્રેટરી:** કાનૂની પાલન સુનિશ્ચિત કરવા માટે કંપનીના બોર્ડ ઓફ ડિરેક્ટર્સ દ્વારા નિમણૂક કરાયેલ આવશ્યક અધિકારી.",
                "id": "KOBJ_GSEB_11SPCC_P2C1_THEO_002"
            },
            {
                "type": "teacher_tip",
                "content": "A Company Secretary works strictly under the control of the Board of Directors. Furthermore, an **Administrative Secretary** acts as a crucial link between the Board of Directors (the policymakers) and the Company (the employees executing the policies).",
                "content_hi": "एक कंपनी सचिव कड़ाई से निदेशक मंडल (Board of Directors) के नियंत्रण में काम करता है। इसके अलावा, एक **प्रशासनिक सचिव (Administrative Secretary)** निदेशक मंडल (नीति निर्माता) और कंपनी (नीतियों को निष्पादित करने वाले कर्मचारियों) के बीच एक महत्वपूर्ण कड़ी के रूप में कार्य करता है।",
                "content_gu": "કંપની સેક્રેટરી બોર્ડ ઓફ ડિરેક્ટર્સ (Board of Directors) ના નિયંત્રણ હેઠળ ચુસ્તપણે કામ કરે છે. વધુમાં, એક **વહીવટી સેક્રેટરી (Administrative Secretary)** બોર્ડ ઓફ ડિરેક્ટર્સ (નીતિ ઘડનારાઓ) અને કંપની (નીતિઓનો અમલ કરતા કર્મચારીઓ) વચ્ચે નિર્ણાયક કડી તરીકે કામ કરે છે.",
                "id": "KOBJ_GSEB_11SPCC_P2C1_TEAC_003"
            }
        ]
    }
    save_json('app_core/chapters/gseb_class11_spcc_part2_ch1.json', data)

def gen_part2_ch3():
    data = {
        "metadata": {
            "id": "gseb_class11_spcc_p2_ch3",
            "title": "Incorporation of a Company",
            "title_hi": "एक कंपनी का निगमन (स्थापना)",
            "title_gu": "કંપનીની સ્થાપના (Incorporation)",
            "subject": "SPCC",
            "grade": "11",
            "board": "GSEB",
            "curriculum": ["GSEB"],
            "difficulty": "Intermediate",
            "estimated_minutes": 90,
            "learning_outcomes": [
                "Understand the stages of incorporation.",
                "Learn about the extensive investigation required before starting.",
                "Understand the documents required like Written Consent and Affidavit.",
                "Know the rules regarding the words 'Limited' and 'Private Limited'."
            ]
        },
        "blocks": [
            {
                "type": "theory",
                "content": "Starting a joint-stock company is not as simple as opening a small grocery shop. It involves a lengthy legal process. The procedure for the Incorporation of a Company is divided into TWO main stages:\n1. **Promotion Stage** (Planning and preparing to start the business).\n2. **Incorporation Stage** (Filing documents with the Registrar of Companies to get legal status).",
                "content_hi": "एक संयुक्त स्टॉक कंपनी शुरू करना उतना आसान नहीं है जितना कि एक छोटी किराने की दुकान खोलना। इसमें एक लंबी कानूनी प्रक्रिया शामिल है। कंपनी के निगमन की प्रक्रिया को दो मुख्य चरणों में बांटा गया है:\n1. **प्रवर्तन चरण (Promotion Stage):** (योजना बनाना और व्यवसाय शुरू करने की तैयारी करना)।\n2. **निगमन चरण (Incorporation Stage):** (कानूनी दर्जा पाने के लिए कंपनियों के रजिस्ट्रार के पास दस्तावेज दाखिल करना)।",
                "content_gu": "જોઇન્ટ સ્ટોક કંપની શરૂ કરવી એ નાની કરિયાણાની દુકાન ખોલવા જેટલું સરળ નથી. તેમાં લાંબી કાનૂની પ્રક્રિયા સામેલ છે. કંપનીની સ્થાપનાની પ્રક્રિયાને બે મુખ્ય તબક્કામાં વહેંચવામાં આવે છે:\n1. **પ્રમોશનનો તબક્કો (Promotion Stage):** (વ્યવસાય શરૂ કરવા માટે આયોજન અને તૈયારી કરવી).\n2. **નોંધણીનો તબક્કો (Incorporation Stage):** (કાનૂની દરજ્જો મેળવવા માટે રજિસ્ટ્રાર ઓફ કંપનીઝ પાસે દસ્તાવેજો ફાઇલ કરવા).",
                "id": "KOBJ_GSEB_11SPCC_P2C3_THEO_001"
            },
            {
                "type": "theory",
                "content": "**Important Steps in Promotion & Incorporation:**\n- **Extensive Investigation:** Before starting, promoters must thoroughly investigate the market demand, availability of raw materials, and required capital. This prevents the company from failing immediately after starting.\n- **Written Consent of Directors:** Every person named as a Director must give their *written consent* to act as a director, agreeing to buy qualification shares and take responsibility.\n- **Affidavit of Directors:** An affidavit stating that they have never been convicted of fraud or breach of duty regarding the formation or management of any company in the past.",
                "content_hi": "**प्रवर्तन और निगमन में महत्वपूर्ण कदम:**\n- **विस्तृत जांच:** शुरू करने से पहले, प्रमोटरों को बाजार की मांग, कच्चे माल की उपलब्धता और आवश्यक पूंजी की पूरी तरह से जांच करनी चाहिए। यह कंपनी को शुरू होने के तुरंत बाद विफल होने से रोकता है।\n- **निदेशकों की लिखित सहमति:** निदेशक के रूप में नामित प्रत्येक व्यक्ति को योग्यता शेयर खरीदने और जिम्मेदारी लेने के लिए सहमत होने के लिए अपनी *लिखित सहमति* देनी होगी।\n- **निदेशकों का शपथ पत्र (Affidavit):** एक हलफनामा जिसमें कहा गया हो कि उन्हें अतीत में किसी भी कंपनी के गठन या प्रबंधन के संबंध में धोखाधड़ी या कर्तव्य के उल्लंघन का दोषी नहीं ठहराया गया है।",
                "content_gu": "**પ્રમોશન અને નોંધણીમાં મહત્વપૂર્ણ પગલાં:**\n- **વિસ્તૃત તપાસ:** શરૂ કરતા પહેલા, પ્રમોટરોએ બજારની માંગ, કાચા માલની ઉપલબ્ધતા અને જરૂરી મૂડીની સંપૂર્ણ તપાસ કરવી જોઈએ. આ કંપનીને શરૂ કર્યા પછી તરત જ નિષ્ફળ થવાથી બચાવે છે.\n- **ડિરેક્ટરોની લેખિત સંમતિ:** ડિરેક્ટર તરીકે નિયુક્ત દરેક વ્યક્તિએ લાયકાતના શેર ખરીદવા અને જવાબદારી લેવા માટે સંમત થઈને પોતાની *લેખિત સંમતિ* આપવી જ જોઇએ.\n- **ડિરેક્ટરોનું સોગંદનામું (Affidavit):** એક સોગંદનામું જેમાં જણાવવામાં આવ્યું હોય કે તેઓ ભૂતકાળમાં કોઈપણ કંપનીની સ્થાપના અથવા સંચાલન અંગે ક્યારેય છેતરપિંડી કે ફરજ ભંગ માટે દોષિત ઠર્યા નથી.",
                "id": "KOBJ_GSEB_11SPCC_P2C3_THEO_002"
            },
            {
                "type": "quiz",
                "question": "Sanjay asks his teacher: 'Which type of company is EXEMPT from writing the word 'Limited' or 'Private Limited' at the end of its name?' What is the correct answer?",
                "question_hi": "संजय अपने शिक्षक से पूछता है: 'किस प्रकार की कंपनी को अपने नाम के अंत में 'लिमिटेड' या 'प्राइवेट लिमिटेड' शब्द लिखने से छूट (EXEMPT) है?' सही उत्तर क्या है?",
                "question_gu": "સંજય તેના શિક્ષકને પૂછે છે: 'કયા પ્રકારની કંપનીને તેના નામના અંતે 'લિમિટેડ' અથવા 'પ્રાઇવેટ લિમિટેડ' શબ્દ લખવામાંથી મુક્તિ (EXEMPT) છે?' સાચો જવાબ શું છે?",
                "options": [
                    "A Public Company",
                    "A Section 8 Company (Not-for-Profit Organization)",
                    "A Government Company",
                    "A One Person Company (OPC)"
                ],
                "options_hi": [
                    "एक सार्वजनिक कंपनी",
                    "एक धारा 8 कंपनी (गैर-लाभकारी संगठन)",
                    "एक सरकारी कंपनी",
                    "एक व्यक्ति कंपनी (OPC)"
                ],
                "options_gu": [
                    "એક જાહેર કંપની",
                    "કલમ 8 કંપની (નફાના હેતુ વિનાની સંસ્થા)",
                    "એક સરકારી કંપની",
                    "એક વ્યક્તિ કંપની (OPC)"
                ],
                "correct_index": 1,
                "explanation": "Companies formed for promoting commerce, art, science, religion, or charity (Section 8 Companies) are exempt from adding 'Limited' or 'Private Limited' to their names.",
                "explanation_hi": "वाणिज्य, कला, विज्ञान, धर्म या दान को बढ़ावा देने के लिए गठित कंपनियों (धारा 8 कंपनियों) को अपने नाम में 'लिमिटेड' या 'प्राइवेट लिमिटेड' जोड़ने से छूट दी गई है।",
                "explanation_gu": "વાણિજ્ય, કળા, વિજ્ઞાન, ધર્મ અથવા ચેરિટીને પ્રોત્સાહન આપવા માટે રચાયેલી કંપનીઓ (કલમ 8 કંપનીઓ) ને તેમના નામમાં 'લિમિટેડ' અથવા 'પ્રાઇવેટ લિમિટેડ' ઉમેરવામાંથી મુક્તિ આપવામાં આવી છે.",
                "id": "KOBJ_GSEB_11SPCC_P2C3_QUIZ_003"
            }
        ]
    }
    save_json('app_core/chapters/gseb_class11_spcc_part2_ch3.json', data)

def gen_part2_ch4():
    data = {
        "metadata": {
            "id": "gseb_class11_spcc_p2_ch4",
            "title": "Memorandum of Association",
            "title_hi": "संस्था का ज्ञापन (Memorandum of Association)",
            "title_gu": "આવેદનપત્ર (Memorandum of Association)",
            "subject": "SPCC",
            "grade": "11",
            "board": "GSEB",
            "curriculum": ["GSEB"],
            "difficulty": "Advanced",
            "estimated_minutes": 120,
            "learning_outcomes": [
                "Understand the importance of the Object Clause.",
                "Know the rules and restrictions of the Name Clause.",
                "Understand the process of changing the Capital Clause and Liability Clause.",
                "Understand the Registered Office Clause."
            ]
        },
        "blocks": [
            {
                "type": "theory",
                "content": "The **Memorandum of Association (MoA)** is the fundamental document of a company. It is the constitution of the company. It contains 6 important clauses: Name, Registered Office, Object, Liability, Capital, and Association clause.\nFor everyone who has a relationship with 'Binaca Company' (investors, creditors, public), the MoA is an important document because it tells them exactly what the company is allowed to do and what its limits are.",
                "content_hi": "**संस्था का ज्ञापन (MoA)** किसी कंपनी का मूलभूत दस्तावेज है। यह कंपनी का संविधान है। इसमें 6 महत्वपूर्ण खंड (Clauses) शामिल हैं: नाम, पंजीकृत कार्यालय, उद्देश्य, दायित्व, पूंजी और संघ खंड।\n'बिनाका कंपनी' के साथ संबंध रखने वाले हर व्यक्ति (निवेशक, लेनदार, जनता) के लिए, एमओए एक महत्वपूर्ण दस्तावेज है क्योंकि यह उन्हें बताता है कि कंपनी को वास्तव में क्या करने की अनुमति है और इसकी सीमाएं क्या हैं।",
                "content_gu": "**આવેદનપત્ર (MoA)** એ કંપનીનો મૂળભૂત દસ્તાવેજ છે. તે કંપનીનું બંધારણ છે. તેમાં 6 મહત્વપૂર્ણ કલમો (Clauses) છે: નામ, નોંધાયેલ ઓફિસ, ઉદ્દેશ, જવાબદારી, મૂડી અને સ્થાપનાની કલમ.\n'બિનાકા કંપની' (Binaca Company) સાથે સંબંધ ધરાવતા દરેક વ્યક્તિ (રોકાણકારો, લેણદારો, જનતા) માટે, MoA એ એક મહત્વપૂર્ણ દસ્તાવેજ છે કારણ કે તે તેમને બરાબર જણાવે છે કે કંપનીને શું કરવાની છૂટ છે અને તેની મર્યાદાઓ શું છે.",
                "id": "KOBJ_GSEB_11SPCC_P2C4_THEO_001"
            },
            {
                "type": "theory",
                "content": "**The Name Clause**\nYou can name your company almost anything, but there are strict restrictions under the Name Clause:\n1. It should not be identical or too similar to an existing company.\n2. It should not contain words suggesting connection with the Government or National heroes without permission. \n\n*Example:* You CANNOT name your company **'Narendra Modi Textiles Limited'**. Using the name of the current Prime Minister or national figures violates the Emblems and Names (Prevention of Improper Use) Act. The Registrar will reject it immediately.",
                "content_hi": "**नाम खंड (The Name Clause)**\nआप अपनी कंपनी का नाम लगभग कुछ भी रख सकते हैं, लेकिन नाम खंड के तहत सख्त प्रतिबंध हैं:\n1. यह किसी मौजूदा कंपनी के समान या बहुत मिलता-जुलता नहीं होना चाहिए।\n2. इसमें ऐसे शब्द शामिल नहीं होने चाहिए जो बिना अनुमति के सरकार या राष्ट्रीय नायकों के साथ संबंध का सुझाव देते हों।\n\n*उदाहरण:* आप अपनी कंपनी का नाम **'नरेंद्र मोदी टेक्सटाइल्स लिमिटेड'** नहीं रख सकते। वर्तमान प्रधान मंत्री या राष्ट्रीय हस्तियों के नाम का उपयोग करना प्रतीक और नाम (अनुचित उपयोग की रोकथाम) अधिनियम का उल्लंघन करता है। रजिस्ट्रार इसे तुरंत खारिज कर देगा।",
                "content_gu": "**નામની કલમ (The Name Clause)**\nતમે તમારી કંપનીનું નામ લગભગ કંઈપણ રાખી શકો છો, પરંતુ નામની કલમ હેઠળ કડક નિયંત્રણો છે:\n1. તે અસ્તિત્વમાં રહેલી કંપની સમાન અથવા ખૂબ સમાન હોવું જોઈએ નહીં.\n2. તેમાં પરવાનગી વિના સરકાર અથવા રાષ્ટ્રીય નાયકો સાથે જોડાણ સૂચવતા શબ્દો ન હોવા જોઈએ.\n\n*ઉદાહરણ:* તમે તમારી કંપનીનું નામ **'નરેન્દ્ર મોદી ટેક્સટાઇલ્સ લિમિટેડ'** રાખી શકતા નથી. વર્તમાન વડા પ્રધાન અથવા રાષ્ટ્રીય વ્યક્તિઓના નામનો ઉપયોગ એ પ્રતીકો અને નામો (અયોગ્ય ઉપયોગ નિવારણ) કાયદાનું ઉલ્લંઘન કરે છે. રજિસ્ટ્રાર તેને તરત જ નામંજૂર કરશે.",
                "id": "KOBJ_GSEB_11SPCC_P2C4_THEO_002"
            },
            {
                "type": "theory",
                "content": "**The Object Clause: The Most Important Clause**\nThe Object clause states the main purpose for which the company is formed. It is considered the most important clause because a company CANNOT do any business outside its Object Clause. Any act done beyond it is 'Ultra Vires' (beyond powers) and is legally void. This protects investors' money from being used in risky, unapproved businesses.",
                "content_hi": "**उद्देश्य खंड (Object Clause): सबसे महत्वपूर्ण खंड**\nउद्देश्य खंड उस मुख्य उद्देश्य को बताता है जिसके लिए कंपनी का गठन किया गया है। इसे सबसे महत्वपूर्ण खंड माना जाता है क्योंकि कोई कंपनी अपने उद्देश्य खंड के बाहर कोई व्यवसाय नहीं कर सकती है। इसके परे किया गया कोई भी कार्य 'अल्ट्रा वायर्स' (अधिकारों से परे) है और कानूनी रूप से शून्य है। यह निवेशकों के पैसे को जोखिम भरे, अनधिकृत व्यवसायों में उपयोग होने से बचाता है।",
                "content_gu": "**ઉદ્દેશની કલમ (Object Clause): સૌથી મહત્વપૂર્ણ કલમ**\nઉદ્દેશની કલમ મુખ્ય હેતુ જણાવે છે જેના માટે કંપનીની રચના કરવામાં આવી છે. તે સૌથી મહત્વપૂર્ણ કલમ માનવામાં આવે છે કારણ કે કંપની તેની ઉદ્દેશ કલમની બહાર કોઈ વ્યવસાય કરી શકતી નથી. તેનાથી આગળ કરવામાં આવેલ કોઈપણ કાર્ય 'અલ્ટ્રા વાયર્સ' (સત્તા બહારનું) છે અને કાયદેસર રીતે રદબાતલ છે. આ રોકાણકારોના નાણાંને જોખમી, અસ્વીકૃત વ્યવસાયોમાં વપરાતા અટકાવે છે.",
                "id": "KOBJ_GSEB_11SPCC_P2C4_THEO_003"
            },
            {
                "type": "teacher_tip",
                "content": "**Changing Clauses (Process):**\n- **Changing Capital Clause:** If Ronak Public Limited wants to increase its capital, it must pass an Ordinary Resolution in the general meeting of shareholders and inform the Registrar within 30 days.\n- **Registered Office:** If Ashoka Company moves its office from Bapunagar to Satellite (within the same city of Ahmedabad), it simply passes a Board Resolution and informs the Registrar. No major legal hurdle!",
                "content_hi": "**खंडों को बदलना (प्रक्रिया):**\n- **पूंजी खंड बदलना:** यदि रौनक पब्लिक लिमिटेड अपनी पूंजी बढ़ाना चाहता है, तो उसे शेयरधारकों की आम बैठक में एक साधारण प्रस्ताव (Ordinary Resolution) पारित करना होगा और 30 दिनों के भीतर रजिस्ट्रार को सूचित करना होगा।\n- **पंजीकृत कार्यालय:** यदि अशोका कंपनी अपने कार्यालय को बापू नगर से सैटेलाइट (उसी शहर अहमदाबाद के भीतर) ले जाती है, तो वह केवल एक बोर्ड प्रस्ताव पारित करती है और रजिस्ट्रार को सूचित करती है। कोई बड़ी कानूनी बाधा नहीं!",
                "content_gu": "**કલમોમાં ફેરફાર (પ્રક્રિયા):**\n- **મૂડીની કલમ બદલવી:** જો રોનક પબ્લિક લિમિટેડ તેની મૂડી વધારવા માંગતી હોય, તો તેણે શેરધારકોની સામાન્ય સભામાં સામાન્ય ઠરાવ (Ordinary Resolution) પસાર કરવો પડશે અને 30 દિવસની અંદર રજિસ્ટ્રારને જાણ કરવી પડશે.\n- **નોંધાયેલ ઓફિસ:** જો અશોકા કંપની તેની ઓફિસ બાપુનગરથી સેટેલાઇટ (અમદાવાદના સમાન શહેરમાં) ખસેડે છે, તો તે ફક્ત બોર્ડનો ઠરાવ પસાર કરે છે અને રજિસ્ટ્રારને જાણ કરે છે. કોઈ મોટી કાનૂની અડચણ નથી!",
                "id": "KOBJ_GSEB_11SPCC_P2C4_TEAC_004"
            }
        ]
    }
    save_json('app_core/chapters/gseb_class11_spcc_part2_ch4.json', data)

if __name__ == "__main__":
    gen_part2_ch1()
    gen_part2_ch3()
    gen_part2_ch4()
