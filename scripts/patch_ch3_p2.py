import json

file_path = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class11_spcc_part2_ch3.json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

new_blocks = [
    {
        "type": "numerical",
        "question": "Into how many and what stages is the procedure for incorporation of company divided?",
        "question_hi": "कंपनी के निगमन (incorporation) की प्रक्रिया को कितने और किन चरणों में विभाजित किया गया है?",
        "question_gu": "કંપનીની નોંધણી (incorporation) ની પ્રક્રિયાને કેટલા અને કયા તબક્કામાં વહેંચવામાં આવી છે?",
        "solution": "The procedure for the incorporation (formation) of a company is divided into two main stages:\n1. **Pre-incorporation stage (Promotion):** Involves the idea of starting a company, primary investigation, extensive investigation, and gathering resources (land, capital, machinery).\n2. **Incorporation stage:** Involves obtaining a Certificate of Incorporation by submitting required documents (Memorandum of Association, Articles of Association, consent of directors, etc.) to the Registrar of Companies.",
        "solution_hi": "कंपनी के निगमन (गठन) की प्रक्रिया को दो मुख्य चरणों में बांटा गया है:\n1. **निगमन-पूर्व चरण (प्रवर्तन/Promotion):** इसमें कंपनी शुरू करने का विचार, प्राथमिक जांच, विस्तृत जांच और संसाधन (भूमि, पूंजी, मशीनरी) जुटाना शामिल है।\n2. **निगमन चरण:** कंपनी रजिस्ट्रार को आवश्यक दस्तावेज (संस्था का ज्ञापन, अंतर्नियम, निदेशकों की सहमति, आदि) जमा करके निगमन का प्रमाण पत्र (Certificate of Incorporation) प्राप्त करना शामिल है।",
        "solution_gu": "કંપનીની નોંધણી (રચના) ની પ્રક્રિયાને બે મુખ્ય તબક્કામાં વહેંચવામાં આવી છે:\n1. **નોંધણી પૂર્વેનો તબક્કો (પ્રવર્તન/Promotion):** કંપની શરૂ કરવાનો વિચાર, પ્રાથમિક તપાસ, વિસ્તૃત તપાસ અને સંસાધનો (જમીન, મૂડી, મશીનરી) એકત્રિત કરવાનો સમાવેશ થાય છે.\n2. **નોંધણીનો તબક્કો:** કંપનીઓના રજિસ્ટ્રારને જરૂરી દસ્તાવેજો (આવેદનપત્ર, નિયમનપત્ર, ડિરેક્ટરોની સંમતિ વગેરે) સબમિટ કરીને નોંધણીનું પ્રમાણપત્ર (Certificate of Incorporation) મેળવવાનો સમાવેશ થાય છે.",
        "id": "KOBJ_GSEB_11SPCC_P2C3_NUME_005"
    },
    {
        "type": "numerical",
        "question": "Why is extensive investigation necessary?",
        "question_hi": "विस्तृत जांच (extensive investigation) क्यों आवश्यक है?",
        "question_gu": "વિસ્તૃત તપાસ (extensive investigation) શા માટે જરૂરી છે?",
        "solution": "After the primary investigation of a business idea seems favorable, an extensive investigation is necessary before spending huge amounts of money.\nIt is necessary because it involves a detailed study of experts' opinions regarding the availability of raw materials, market demand, transport facilities, power supply, and estimated costs.\nWithout an extensive investigation, the promoters might start a company that is practically unviable, leading to massive financial losses.",
        "solution_hi": "व्यावसायिक विचार की प्राथमिक जांच अनुकूल प्रतीत होने के बाद, बड़ी मात्रा में धन खर्च करने से पहले विस्तृत जांच आवश्यक है।\nयह आवश्यक है क्योंकि इसमें कच्चे माल की उपलब्धता, बाजार की मांग, परिवहन सुविधाओं, बिजली की आपूर्ति और अनुमानित लागत के संबंध में विशेषज्ञों की राय का विस्तृत अध्ययन शामिल है।\nविस्तृत जांच के बिना, प्रमोटर एक ऐसी कंपनी शुरू कर सकते हैं जो व्यावहारिक रूप से अव्यवहार्य (unviable) हो, जिससे भारी वित्तीय नुकसान हो सकता है।",
        "solution_gu": "વ્યવસાયિક વિચારની પ્રાથમિક તપાસ સાનુકૂળ જણાયા પછી, મોટી રકમ ખર્ચતા પહેલા વિસ્તૃત તપાસ જરૂરી છે.\nતે જરૂરી છે કારણ કે તેમાં કાચો માલ, બજારની માંગ, પરિવહન સુવિધાઓ, વીજ પુરવઠો અને અંદાજિત ખર્ચ અંગેના નિષ્ણાતોના અભિપ્રાયોનો વિગતવાર અભ્યાસ સામેલ છે.\nવિસ્તૃત તપાસ વિના, પ્રમોટરો એવી કંપની શરૂ કરી શકે છે જે વ્યવહારિક રીતે અશક્ય (unviable) હોય, જેનાથી ભારે નાણાકીય નુકસાન થઈ શકે છે.",
        "id": "KOBJ_GSEB_11SPCC_P2C3_NUME_006"
    },
    {
        "type": "numerical",
        "question": "Why does every director have to give written consent?",
        "question_hi": "प्रत्येक निदेशक को लिखित सहमति क्यों देनी होती है?",
        "question_gu": "દરેક ડિરેક્ટરે લેખિત સંમતિ શા માટે આપવી પડે છે?",
        "solution": "Every person whose name is mentioned as a proposed Director must give their written consent to the Registrar.\nThis is necessary to legally prove that they have voluntarily agreed to accept the position of a Director and its associated responsibilities. It prevents a company from fraudulently using someone's name as a director without their knowledge.",
        "solution_hi": "जिस व्यक्ति का नाम प्रस्तावित निदेशक (proposed Director) के रूप में वर्णित है, उसे रजिस्ट्रार को अपनी लिखित सहमति देनी होगी।\nयह कानूनी रूप से साबित करने के लिए आवश्यक है कि वे स्वेच्छा से निदेशक का पद और उससे जुड़ी जिम्मेदारियों को स्वीकार करने के लिए सहमत हुए हैं। यह किसी कंपनी को किसी व्यक्ति की जानकारी के बिना धोखाधड़ी से निदेशक के रूप में उसके नाम का उपयोग करने से रोकता है।",
        "solution_gu": "જે વ્યક્તિનું નામ સૂચિત ડિરેક્ટર (proposed Director) તરીકે દર્શાવેલ હોય, તેણે રજિસ્ટ્રારને પોતાની લેખિત સંમતિ આપવી પડે છે.\nકાયદેસર રીતે સાબિત કરવા માટે આ જરૂરી છે કે તેઓ સ્વેચ્છાએ ડિરેક્ટરનું પદ અને તેની સાથે સંકળાયેલી જવાબદારીઓ સ્વીકારવા માટે સંમત થયા છે. તે કંપનીને કોઈપણ વ્યક્તિની જાણ વિના છેતરપિંડીથી ડિરેક્ટર તરીકે તેના નામનો ઉપયોગ કરતા અટકાવે છે.",
        "id": "KOBJ_GSEB_11SPCC_P2C3_NUME_007"
    },
    {
        "type": "numerical",
        "question": "Which matters are shown in the Affidavit of the Directors?",
        "question_hi": "निदेशकों के हलफनामे (Affidavit) में कौन सी बातें दिखाई जाती हैं?",
        "question_gu": "ડિરેક્ટરોના સોગંદનામામાં (Affidavit) કઈ બાબતો દર્શાવવામાં આવે છે?",
        "solution": "The Directors, First Subscribers, and Promoters must submit a legal affidavit stating that:\n1. They have never been convicted for any offense related to the establishment or management of any company.\n2. They have not been found guilty of fraud or breach of duty under the Companies Act in the last 5 years.\n3. All the documents and information submitted for the company's registration are true, complete, and correct to the best of their knowledge.",
        "solution_hi": "निदेशकों, प्रथम ग्राहकों (Subscribers) और प्रमोटरों को एक कानूनी हलफनामा जमा करना होता है जिसमें कहा गया हो कि:\n1. उन्हें कभी भी किसी कंपनी की स्थापना या प्रबंधन से संबंधित किसी अपराध के लिए दोषी नहीं ठहराया गया है।\n2. उन्हें पिछले 5 वर्षों में कंपनी अधिनियम के तहत धोखाधड़ी या कर्तव्य भंग (breach of duty) का दोषी नहीं पाया गया है।\n3. कंपनी के पंजीकरण के लिए प्रस्तुत किए गए सभी दस्तावेज और जानकारी उनकी सर्वोत्तम जानकारी के अनुसार सत्य, पूर्ण और सही हैं।",
        "solution_gu": "ડિરેક્ટરો, પ્રથમ સબ્સ્ક્રાઇબર્સ અને પ્રમોટરોએ એક કાનૂની સોગંદનામું સબમિટ કરવું આવશ્યક છે જેમાં જણાવવામાં આવ્યું હોય કે:\n1. તેઓને કોઈપણ કંપનીની સ્થાપના અથવા સંચાલન સંબંધિત કોઈપણ ગુના માટે ક્યારેય દોષિત ઠેરવવામાં આવ્યા નથી.\n2. તેઓ છેલ્લા 5 વર્ષમાં કંપની ધારા હેઠળ છેતરપિંડી અથવા ફરજ ભંગ (breach of duty) માટે દોષિત જણાયા નથી.\n3. કંપનીની નોંધણી માટે સબમિટ કરવામાં આવેલા તમામ દસ્તાવેજો અને માહિતી તેમના શ્રેષ્ઠ જ્ઞાન મુજબ સાચા, સંપૂર્ણ અને યોગ્ય છે.",
        "id": "KOBJ_GSEB_11SPCC_P2C3_NUME_008"
    },
    {
        "type": "numerical",
        "question": "Which matters are required to be extensive at the extensive investigation during the formation of a company?",
        "question_hi": "कंपनी के गठन के दौरान विस्तृत जांच के समय किन मामलों का विस्तृत होना आवश्यक है?",
        "question_gu": "કંપનીની રચના દરમિયાન વિસ્તૃત તપાસ વખતે કઈ બાબતો વિસ્તૃત હોવી જરૂરી છે?",
        "solution": "During the extensive investigation phase, promoters must extensively analyze and gather expert opinions on:\n1. **Financial aspect:** The total estimated cost of the project and sources of capital.\n2. **Commercial aspect:** Market demand for the product, potential competition, and expected sales.\n3. **Technical aspect:** Availability of raw materials, machinery, power supply, skilled labor, and transport facilities.",
        "solution_hi": "विस्तृत जांच के चरण के दौरान, प्रमोटरों को निम्नलिखित का विस्तार से विश्लेषण करना चाहिए और विशेषज्ञों की राय एकत्र करनी चाहिए:\n1. **वित्तीय पहलू:** परियोजना की कुल अनुमानित लागत और पूंजी के स्रोत।\n2. **वाणिज्यिक पहलू:** उत्पाद के लिए बाजार की मांग, संभावित प्रतिस्पर्धा और अपेक्षित बिक्री।\n3. **तकनीकी पहलू:** कच्चे माल, मशीनरी, बिजली की आपूर्ति, कुशल श्रम और परिवहन सुविधाओं की उपलब्धता।",
        "solution_gu": "વિસ્તૃત તપાસના તબક્કા દરમિયાન, પ્રમોટરોએ વિસ્તૃત રીતે વિશ્લેષણ કરવું જોઈએ અને આના પર નિષ્ણાતોના મંતવ્યો એકત્રિત કરવા જોઈએ:\n1. **નાણાકીય પાસું:** પ્રોજેક્ટનો કુલ અંદાજિત ખર્ચ અને મૂડીના સ્ત્રોત.\n2. **વાણિજ્યિક પાસું:** ઉત્પાદન માટે બજારની માંગ, સંભવિત સ્પર્ધા અને અપેક્ષિત વેચાણ.\n3. **તકનીકી પાસું:** કાચો માલ, મશીનરી, વીજ પુરવઠો, કુશળ શ્રમ અને પરિવહન સુવિધાઓની ઉપલબ્ધતા.",
        "id": "KOBJ_GSEB_11SPCC_P2C3_NUME_009"
    },
    {
        "type": "numerical",
        "question": "Which matters are required to be shown while presenting the list of Directors?",
        "question_hi": "निदेशकों की सूची प्रस्तुत करते समय किन बातों को दर्शाना आवश्यक है?",
        "question_gu": "ડિરેક્ટરોની યાદી રજૂ કરતી વખતે કઈ બાબતો દર્શાવવી જરૂરી છે?",
        "solution": "A company must present a list of people who have agreed to act as the first Directors. This list submitted to the Registrar must show the following details for every director:\n1. Full Name\n2. Residential Address\n3. Nationality\n4. Date of Birth\n5. Occupation\n6. Details of their Directorship in any other companies.\n*(Note: A public company must have at least one female director).*.",
        "solution_hi": "एक कंपनी को उन लोगों की सूची प्रस्तुत करनी होती है जो प्रथम निदेशक के रूप में कार्य करने के लिए सहमत हुए हैं। रजिस्ट्रार को प्रस्तुत इस सूची में प्रत्येक निदेशक के लिए निम्नलिखित विवरण दिखाना आवश्यक है:\n1. पूरा नाम\n2. आवासीय पता\n3. राष्ट्रीयता\n4. जन्म तिथि\n5. व्यवसाय (Occupation)\n6. किसी अन्य कंपनी में उनके निदेशक पद (Directorship) का विवरण।\n*(नोट: एक सार्वजनिक कंपनी में कम से कम एक महिला निदेशक का होना अनिवार्य है)।*",
        "solution_gu": "કંપનીએ એવા લોકોની યાદી રજૂ કરવી પડશે જેઓ પ્રથમ ડિરેક્ટર તરીકે કાર્ય કરવા સંમત થયા છે. રજિસ્ટ્રારને સુપરત કરાયેલી આ યાદીમાં દરેક ડિરેક્ટર માટે નીચેની વિગતો દર્શાવવી આવશ્યક છે:\n1. પૂરું નામ\n2. રહેણાંક સરનામું\n3. રાષ્ટ્રીયતા\n4. જન્મ તારીખ\n5. વ્યવસાય (Occupation)\n6. અન્ય કોઈપણ કંપનીમાં તેમના ડિરેક્ટર પદ (Directorship) ની વિગતો.\n*(નોંધ: જાહેર કંપનીમાં ઓછામાં ઓછા એક મહિલા ડિરેક્ટર હોવા ફરજિયાત છે).*.",
        "id": "KOBJ_GSEB_11SPCC_P2C3_NUME_010"
    }
]

data['blocks'].extend(new_blocks)

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Part 2 Chapter 3 updated with user questions!")
