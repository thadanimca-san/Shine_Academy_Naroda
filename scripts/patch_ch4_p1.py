import json

file_path = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class11_spcc_part1_ch4.json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

new_blocks = [
    {
        "type": "numerical",
        "question": "Explain with examples how the date of a letter is written in the American and British method.",
        "question_hi": "अमेरिकी और ब्रिटिश पद्धति में पत्र की तिथि कैसे लिखी जाती है, उदाहरण सहित स्पष्ट कीजिए।",
        "question_gu": "અમેરિકન અને બ્રિટિશ પદ્ધતિમાં પત્રની તારીખ કેવી રીતે લખવામાં આવે છે તે ઉદાહરણો સાથે સમજાવો.",
        "solution": "There are two accepted methods of writing the date in a business letter:\n1. **American Method:** The month is written first, followed by the date, a comma, and the year. \n*Example:* January 15, 2024\n2. **British Method:** The date is written first (using ordinal numbers like st, nd, rd, th), followed by the month, and then the year.\n*Example:* 15th January, 2024\n*(Note: Dates should never be written purely in numbers like 15/01/2024 in a formal letter).*.",
        "solution_hi": "व्यावसायिक पत्र में तिथि लिखने की दो स्वीकृत विधियाँ हैं:\n1. **अमेरिकी विधि:** सबसे पहले महीना लिखा जाता है, उसके बाद तारीख, अल्पविराम (comma) और फिर वर्ष।\n*उदाहरण:* January 15, 2024\n2. **ब्रिटिश विधि:** सबसे पहले तारीख लिखी जाती है (st, nd, rd, th जैसे क्रमसूचक संख्याओं का उपयोग करके), उसके बाद महीना, और फिर वर्ष।\n*उदाहरण:* 15th January, 2024\n*(नोट: औपचारिक पत्र में तिथियों को कभी भी केवल 15/01/2024 जैसे अंकों में नहीं लिखा जाना चाहिए)।*.",
        "solution_gu": "વાણિજ્યિક પત્રમાં તારીખ લખવાની બે સ્વીકૃત પદ્ધતિઓ છે:\n1. **અમેરિકન પદ્ધતિ:** મહિનો પહેલા લખાય છે, ત્યારબાદ તારીખ, અલ્પવિરામ (comma) અને પછી વર્ષ.\n*ઉદાહરણ:* January 15, 2024\n2. **બ્રિટિશ પદ્ધતિ:** તારીખ પહેલા લખવામાં આવે છે (st, nd, rd, th જેવી ક્રમસૂચક સંખ્યાઓનો ઉપયોગ કરીને), ત્યારબાદ મહિનો અને પછી વર્ષ.\n*ઉદાહરણ:* 15th January, 2024\n*(નોંધ: ઔપચારિક પત્રમાં તારીખો ક્યારેય માત્ર 15/01/2024 જેવા અંકોમાં લખવી જોઈએ નહીં).*.",
        "id": "KOBJ_GSEB_11SPCC_P1C4_NUME_004"
    },
    {
        "type": "numerical",
        "question": "Name the compulsory parts of a business letter.",
        "question_hi": "एक व्यावसायिक पत्र के अनिवार्य भागों के नाम बताइए।",
        "question_gu": "વાણિજ્યિક પત્રના ફરજિયાત ભાગોના નામ જણાવો.",
        "solution": "The compulsory parts of a business letter, without which the letter is considered incomplete, are:\n1. Heading (Letterhead)\n2. Date\n3. Inside Address (Receiver's address)\n4. Salutation (e.g., Respected Sir)\n5. Body of the letter\n6. Complimentary Close (e.g., Yours faithfully)\n7. Signature",
        "solution_hi": "व्यावसायिक पत्र के अनिवार्य भाग, जिनके बिना पत्र अधूरा माना जाता है, वे हैं:\n1. शीर्षक (Letterhead)\n2. दिनांक\n3. अंदर का पता (प्राप्तकर्ता का पता)\n4. अभिवादन (जैसे, आदरणीय महोदय)\n5. पत्र का मुख्य भाग (Body of the letter)\n6. मानार्थ समापन (जैसे, भवदीय)\n7. हस्ताक्षर",
        "solution_gu": "વાણિજ્યિક પત્રના ફરજિયાત ભાગો, જેના વિના પત્ર અધૂરો માનવામાં આવે છે, તે નીચે મુજબ છે:\n1. શીર્ષક (Letterhead)\n2. તારીખ\n3. અંદરનું સરનામું (મેળવનારનું સરનામું)\n4. સંબોધન (દા.ત., આદરણીય સાહેબ)\n5. પત્રનો મુખ્ય ભાગ (Body of the letter)\n6. સમાપન (દા.ત., આપનો વિશ્વાસુ)\n7. સહી",
        "id": "KOBJ_GSEB_11SPCC_P1C4_NUME_005"
    },
    {
        "type": "numerical",
        "question": "Name the occasional parts of a business letter.",
        "question_hi": "एक व्यावसायिक पत्र के सामयिक (occasional) भागों के नाम बताइए।",
        "question_gu": "વાણિજ્યિક પત્રના પ્રસંગોપાત (occasional) ભાગોના નામ જણાવો.",
        "solution": "The occasional parts of a business letter, which are used only when necessary, are:\n1. Personal or Mailing Instruction\n2. Attention Line\n3. Subject Line\n4. Enclosure (Attachments)\n5. Carbon Copy (CC) or Blind Carbon Copy (BCC)\n6. Identification Line\n7. Postscript (P.S.)",
        "solution_hi": "व्यावसायिक पत्र के सामयिक (कभी-कभार इस्तेमाल होने वाले) भाग, जिनका उपयोग केवल आवश्यकता पड़ने पर किया जाता है, वे हैं:\n1. व्यक्तिगत या मेलिंग निर्देश\n2. ध्यान रेखा (Attention Line)\n3. विषय रेखा (Subject Line)\n4. संलग्नक (Enclosures)\n5. कार्बन कॉपी (CC) या ब्लाइंड कार्बन कॉपी (BCC)\n6. पहचान रेखा (Identification Line)\n7. पोस्टस्क्रिप्ट (P.S.)",
        "solution_gu": "વાણિજ્યિક પત્રના પ્રસંગોપાત (ક્યારેક વપરાતા) ભાગો, જેનો ઉપયોગ માત્ર જરૂર પડે ત્યારે જ થાય છે, તે નીચે મુજબ છે:\n1. વ્યક્તિગત અથવા મેઇલિંગ સૂચના\n2. ધ્યાન આકર્ષક રેખા (Attention Line)\n3. વિષય રેખા (Subject Line)\n4. બિડાણ (Enclosures)\n5. કાર્બન કોપી (CC) અથવા બ્લાઇન્ડ કાર્બન કોપી (BCC)\n6. ઓળખ રેખા (Identification Line)\n7. તાજા કલમ (P.S.)",
        "id": "KOBJ_GSEB_11SPCC_P1C4_NUME_006"
    },
    {
        "type": "numerical",
        "question": "Write a short note on 'Mailing Instruction'.",
        "question_hi": "'मेलिंग निर्देश' (Mailing Instruction) पर एक संक्षिप्त टिप्पणी लिखें।",
        "question_gu": "'મેઇલિંગ સૂચના' (Mailing Instruction) પર ટૂંકી નોંધ લખો.",
        "solution": "Mailing Instructions provide specific directions to the postal department or courier on how the letter should be delivered.\nFor example, if a letter is important and needs to reach quickly, the sender writes instructions like \"By Speed Post\", \"By Registered AD\", \"By Courier\", or \"Air Mail\" at the top right or center of the envelope and the letterhead.\nThis ensures that the letter is handled according to its priority and importance.",
        "solution_hi": "मेलिंग निर्देश डाक विभाग या कूरियर को विशिष्ट निर्देश प्रदान करते हैं कि पत्र कैसे वितरित किया जाना चाहिए।\nउदाहरण के लिए, यदि कोई पत्र महत्वपूर्ण है और उसे जल्दी पहुंचने की आवश्यकता है, तो प्रेषक लिफाफे और लेटरहेड के ऊपर दाईं या मध्य में \"बाय स्पीड पोस्ट\", \"बाय रजिस्टर्ड एडी\", \"बाय कूरियर\" या \"एयर मेल\" जैसे निर्देश लिखता है।\nयह सुनिश्चित करता है कि पत्र को उसकी प्राथमिकता और महत्व के अनुसार संभाला जाए।",
        "solution_gu": "મેઇલિંગ સૂચનાઓ ટપાલ વિભાગ અથવા કુરિયરને પત્ર કેવી રીતે વિતરિત કરવો તે અંગે ચોક્કસ નિર્દેશો પૂરા પાડે છે.\nઉદાહરણ તરીકે, જો કોઈ પત્ર મહત્વપૂર્ણ હોય અને તેને ઝડપથી પહોંચાડવાની જરૂર હોય, તો મોકલનાર પરબીડિયા અને લેટરહેડની ઉપર જમણી અથવા મધ્યમાં \"બાય સ્પીડ પોસ્ટ\", \"બાય રજિસ્ટર્ડ એડી\", \"બાય કુરિયર\" અથવા \"એર મેઇલ\" જેવી સૂચનાઓ લખે છે.\nઆ સુનિશ્ચિત કરે છે કે પત્રને તેની પ્રાથમિકતા અને મહત્વ અનુસાર સંચાલિત કરવામાં આવે.",
        "id": "KOBJ_GSEB_11SPCC_P1C4_NUME_007"
    },
    {
        "type": "numerical",
        "question": "Explain the position of the 'Attention Line' in commercial letter with an example.",
        "question_hi": "व्यावसायिक पत्र में 'ध्यान रेखा' (Attention Line) की स्थिति को एक उदाहरण के साथ स्पष्ट कीजिए।",
        "question_gu": "વાણિજ્યિક પત્રમાં 'ધ્યાન આકર્ષક રેખા' (Attention Line) નું સ્થાન ઉદાહરણ સાથે સમજાવો.",
        "solution": "The 'Attention Line' is used when a letter is addressed to a large organization, but the sender wants a specific person or manager to read it promptly.\n**Position:** It is placed exactly between the Inside Address (Receiver's address) and the Salutation.\n**Example:**\n\nTo,\nThe Manager,\nReliance Industries Ltd.,\nMumbai - 400001\n\n**For the Attention of: Mr. Sharma (Purchase Officer)**\n\nRespected Sir,\n...",
        "solution_hi": "'ध्यान रेखा' का उपयोग तब किया जाता है जब कोई पत्र किसी बड़े संगठन को संबोधित किया जाता है, लेकिन प्रेषक चाहता है कि कोई विशिष्ट व्यक्ति या प्रबंधक इसे तुरंत पढ़े।\n**स्थिति:** यह बिल्कुल अंदर के पते (प्राप्तकर्ता का पता) और अभिवादन (Salutation) के बीच रखा जाता है।\n**उदाहरण:**\n\nप्रति,\nप्रबंधक,\nरिलायंस इंडस्ट्रीज लिमिटेड,\nमुंबई - 400001\n\n**ध्यानार्थ: श्रीमान शर्मा (क्रय अधिकारी)**\n\nआदरणीय महोदय,\n...",
        "solution_gu": "'ધ્યાન આકર્ષક રેખા' નો ઉપયોગ ત્યારે થાય છે જ્યારે પત્ર કોઈ મોટી સંસ્થાને સંબોધવામાં આવે છે, પરંતુ મોકલનાર ઈચ્છે છે કે કોઈ ચોક્કસ વ્યક્તિ અથવા મેનેજર તેને તાત્કાલિક વાંચે.\n**સ્થાન:** તે બરાબર અંદરના સરનામા (મેળવનારનું સરનામું) અને સંબોધન (Salutation) ની વચ્ચે મૂકવામાં આવે છે.\n**ઉદાહરણ:**\n\nપ્રતિ,\nમેનેજર,\nરિલાયન્સ ઇન્ડસ્ટ્રીઝ લિમિટેડ,\nમુંબઈ - 400001\n\n**ધ્યાનાર્થે: શ્રી શર્મા (ખરીદી અધિકારી)**\n\nઆદરણીય સાહેબ,\n...",
        "id": "KOBJ_GSEB_11SPCC_P1C4_NUME_008"
    }
]

data['blocks'].extend(new_blocks)

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Part 1 Chapter 4 updated with user questions!")
