import json

metadata = {
    "id": "NCERT_10_MATH_CH09",
    "title": "Some Applications of Trigonometry",
    "title_hi": "त्रिकोणमिति के कुछ अनुप्रयोग",
    "title_gu": "ત્રિકોણમિતિના કેટલાક ઉપયોગો",
    "subject": "Mathematics",
    "subject_hi": "गणित",
    "subject_gu": "ગણિત",
    "grade": "Class 10",
    "board": "Universal",
    "curriculum": ["CBSE", "GSEB", "ICSE"],
    "chapter_number": 9,
    "difficulty": "intermediate",
    "version": "2.0"
}

blocks = []

blocks.append({
    "id": "MATH10_CH09_HOOK_01",
    "type": "hook",
    "title": "How Do We Measure Mount Everest?",
    "title_hi": "हम माउंट एवरेस्ट को कैसे मापते हैं?",
    "title_gu": "આપણે માઉન્ટ એવરેસ્ટને કેવી રીતે માપીએ છીએ?",
    "body": "Did you know that the height of Mount Everest was not measured by climbing it with a long measuring tape? In 1852, an Indian mathematician named Radhanath Sikdar used a giant instrument called a Theodolite from over 240 km away! He used Trigonometry to calculate its height. Today, we will learn exactly how he did it.",
    "body_hi": "क्या आप जानते हैं कि माउंट एवरेस्ट की ऊंचाई किसी लंबे मापने वाले टेप से नहीं मापी गई थी? 1852 में, राधानाथ सिकदर नामक एक भारतीय गणितज्ञ ने 240 किमी दूर से थियोडोलाइट नामक एक विशाल उपकरण का उपयोग किया था! उन्होंने इसकी ऊंचाई की गणना करने के लिए त्रिकोणमिति का उपयोग किया। आज, हम सीखेंगे कि उन्होंने यह कैसे किया।",
    "body_gu": "શું તમે જાણો છો કે માઉન્ટ એવરેસ્ટની ઊંચાઈ કોઈ લાંબી મેઝરિંગ ટેપથી માપવામાં આવી ન હતી? 1852માં, રાધાનાથ સિકદર નામના એક ભારતીય ગણિતશાસ્ત્રીએ 240 કિમી દૂરથી થિયોડોલાઇટ નામના એક વિશાળ સાધનનો ઉપયોગ કર્યો હતો! તેણે તેની ઊંચાઈની ગણતરી કરવા માટે ત્રિકોણમિતિનો ઉપયોગ કર્યો. આજે, આપણે શીખીશું કે તેણે તે કેવી રીતે કર્યું."
})

blocks.append({
    "id": "MATH10_CH09_SOCRATIC_01",
    "type": "socratic_question",
    "title": "Think Before You Answer",
    "title_hi": "जवाब देने से पहले सोचें",
    "title_gu": "જવાબ આપતા પહેલા વિચારો",
    "body": "Imagine you are standing 10 meters away from a tall tree, looking exactly at its top. If you know how far you are from the tree, and the exact angle at which you are looking up, can you find the tree's height without actually climbing it? What do you think?",
    "body_hi": "कल्पना करें कि आप एक ऊंचे पेड़ से 10 मीटर दूर खड़े हैं, और ठीक उसकी चोटी की ओर देख रहे हैं। यदि आप जानते हैं कि आप पेड़ से कितनी दूर हैं, और आप किस सटीक कोण पर ऊपर देख रहे हैं, तो क्या आप वास्तव में उस पर चढ़े बिना पेड़ की ऊंचाई का पता लगा सकते हैं? आप क्या सोचते हैं?",
    "body_gu": "કલ્પના કરો કે તમે એક ઊંચા ઝાડથી 10 મીટર દૂર ઉભા છો, અને બરાબર તેની ટોચ તરફ જોઈ રહ્યા છો. જો તમને ખબર હોય કે તમે ઝાડથી કેટલા દૂર છો, અને તમે કયા ચોક્કસ ખૂણા પર ઉપર જોઈ રહ્યા છો, તો શું તમે ખરેખર તેના પર ચઢ્યા વિના ઝાડની ઊંચાઈ શોધી શકો છો? તમે શું વિચારો છો?"
})

blocks.append({
    "id": "MATH10_CH09_DISCOVERY_01",
    "type": "discovery",
    "title": "Discover the Right-Angled Triangle",
    "title_hi": "समकोण त्रिभुज की खोज करें",
    "title_gu": "કાટકોણ ત્રિકોણ શોધો",
    "body": "Try to visualize this:\n1. Your distance from the tree is the 'Base'.\n2. The tree is standing straight, which is the 'Perpendicular'.\n3. Your line of sight to the top forms the 'Hypotenuse'.\n\nThis forms a perfect Right-Angled Triangle! Since we know the Base and want to find the Perpendicular, we can use the Tangent ratio: tan(θ) = Perpendicular / Base.",
    "body_hi": "इसकी कल्पना करने का प्रयास करें:\n1. पेड़ से आपकी दूरी 'आधार' है।\n2. पेड़ सीधा खड़ा है, जो 'लंब' है।\n3. शीर्ष तक आपकी दृष्टि रेखा 'कर्ण' बनाती है।\n\nयह एक पूर्ण समकोण त्रिभुज बनाता है! चूंकि हम आधार जानते हैं और लंब खोजना चाहते हैं, हम स्पर्शज्या अनुपात का उपयोग कर सकते हैं: tan(θ) = लंब / आधार।",
    "body_gu": "આની કલ્પના કરવાનો પ્રયાસ કરો:\n1. ઝાડથી તમારું અંતર 'આધાર' છે.\n2. ઝાડ સીધું ઊભું છે, જે 'લંબ' છે.\n3. ટોચ સુધી તમારી દ્રષ્ટિ રેખા 'કર્ણ' બનાવે છે.\n\nઆ એક સંપૂર્ણ કાટકોણ ત્રિકોણ બનાવે છે! કારણ કે આપણે આધાર જાણીએ છીએ અને લંબ શોધવા માંગીએ છીએ, આપણે ટેન્જેન્ટ ગુણોત્તરનો ઉપયોગ કરી શકીએ છીએ: tan(θ) = લંબ / આધાર."
})

blocks.append({
    "id": "MATH10_CH09_REVEAL_01",
    "type": "reveal",
    "title": "Line of Sight & Angles",
    "title_hi": "दृष्टि रेखा और कोण",
    "title_gu": "દ્રષ્ટિ રેખા અને ખૂણા",
    "body": "Let's define the formal terms:\n\n• Line of Sight: The line drawn from the eye of an observer to the point being viewed on the object.\n• Angle of Elevation: The angle formed by the line of sight with the horizontal when the object is ABOVE the horizontal level (looking up).\n• Angle of Depression: The angle formed by the line of sight with the horizontal when the object is BELOW the horizontal level (looking down).",
    "body_hi": "आइए औपचारिक शब्दों को परिभाषित करें:\n\n• दृष्टि रेखा: प्रेक्षक की आँख से वस्तु पर देखे जा रहे बिंदु तक खींची गई रेखा।\n• उन्नयन कोण: दृष्टि रेखा और क्षैतिज रेखा के बीच बना कोण जब वस्तु क्षैतिज स्तर से ऊपर हो (ऊपर देखना)।\n• अवनमन कोण: दृष्टि रेखा और क्षैतिज रेखा के बीच बना कोण जब वस्तु क्षैतिज स्तर से नीचे हो (नीचे देखना)।",
    "body_gu": "ચાલો ઔપચારિક શબ્દોને વ્યાખ્યાયિત કરીએ:\n\n• દ્રષ્ટિ રેખા: નિરીક્ષકની આંખથી વસ્તુ પર જોવાતા બિંદુ સુધી દોરવામાં આવેલી રેખા.\n• ઉત્સેધકોણ: દ્રષ્ટિ રેખા અને સમક્ષિતિજ રેખા વચ્ચે બનતો ખૂણો જ્યારે વસ્તુ સમક્ષિતિજ સ્તરથી ઉપર હોય (ઉપર જોવું).\n• અવસેધકોણ: દ્રષ્ટિ રેખા અને સમક્ષિતિજ રેખા વચ્ચે બનતો ખૂણો જ્યારે વસ્તુ સમક્ષિતિજ સ્તરથી નીચે હોય (નીચે જોવું)."
})

blocks.append({
    "id": "MATH10_CH09_QUIZ_01",
    "type": "mcq",
    "title": "Quick Check",
    "title_hi": "त्वरित जाँच",
    "title_gu": "ઝડપી ચકાસણી",
    "body": "If you are standing on the roof of a building and looking down at a car parked on the street, which angle is formed between your line of sight and the horizontal line?",
    "body_hi": "यदि आप किसी इमारत की छत पर खड़े हैं और सड़क पर खड़ी एक कार को नीचे देख रहे हैं, तो आपकी दृष्टि रेखा और क्षैतिज रेखा के बीच कौन सा कोण बनता है?",
    "body_gu": "જો તમે કોઈ ઇમારતની છત પર ઉભા છો અને રસ્તા પર ઉભેલી કારને નીચે જોઈ રહ્યા છો, તો તમારી દ્રષ્ટિ રેખા અને સમક્ષિતિજ રેખા વચ્ચે કયો ખૂણો બને છે?",
    "options": ["Angle of Elevation", "Angle of Depression", "Right Angle", "Acute Angle"],
    "options_hi": ["उन्नयन कोण", "अवनमन कोण", "समकोण", "न्यून कोण"],
    "options_gu": ["ઉત્સેધકોણ", "અવસેધકોણ", "કાટખૂણો", "લઘુકોણ"],
    "correct_index": 1,
    "explanation": "Since you are looking down at the car, the line of sight is below the horizontal level, forming an Angle of Depression.",
    "explanation_hi": "चूंकि आप कार को नीचे देख रहे हैं, दृष्टि रेखा क्षैतिज स्तर से नीचे है, जिससे एक अवनमन कोण बनता है।",
    "explanation_gu": "કારણ કે તમે કારને નીચે જોઈ રહ્યા છો, દ્રષ્ટિ રેખા સમક્ષિતિજ સ્તરથી નીચે છે, જેનાથી અવસેધકોણ બને છે."
})

blocks.append({
    "id": "MATH10_CH09_REFLECTION_01",
    "type": "reflection",
    "title": "Think and Connect",
    "title_hi": "सोचें और जोड़ें",
    "title_gu": "વિચારો અને જોડો",
    "body": "Imagine a bird looking down at you from a tree, and you looking up at the bird. The bird makes an angle of depression, and you make an angle of elevation. Because the two horizontal lines (one at the bird's eye level, one at your eye level) are parallel, these two angles are Alternate Interior Angles. Therefore, the Angle of Elevation is always equal to the Angle of Depression!",
    "body_hi": "कल्पना करें कि एक पक्षी पेड़ से आपको नीचे देख रहा है, और आप पक्षी को ऊपर देख रहे हैं। पक्षी अवनमन कोण बनाता है, और आप उन्नयन कोण बनाते हैं। क्योंकि दो क्षैतिज रेखाएं (एक पक्षी की आंख के स्तर पर, एक आपकी आंख के स्तर पर) समानांतर हैं, ये दोनों कोण एकांतर अंतःकोण हैं। इसलिए, उन्नयन कोण हमेशा अवनमन कोण के बराबर होता है!",
    "body_gu": "કલ્પના કરો કે એક પક્ષી ઝાડ પરથી તમને નીચે જોઈ રહ્યું છે, અને તમે પક્ષીને ઉપર જોઈ રહ્યા છો. પક્ષી અવસેધકોણ બનાવે છે, અને તમે ઉત્સેધકોણ બનાવો છો. કારણ કે બે સમક્ષિતિજ રેખાઓ (એક પક્ષીની આંખના સ્તરે, એક તમારી આંખના સ્તરે) સમાંતર છે, આ બંને ખૂણાઓ યુગ્મકોણ છે. તેથી, ઉત્સેધકોણ હંમેશા અવસેધકોણ સમાન હોય છે!"
})

blocks.append({
    "id": "MATH10_CH09_CONNECTION_01",
    "type": "connection",
    "title": "Real-World Connection",
    "title_hi": "वास्तविक दुनिया का कनेक्शन",
    "title_gu": "વાસ્તવિક દુનિયાનું જોડાણ",
    "body": "Heights and distances aren't just for exams. Air Traffic Controllers use these concepts to guide airplanes safely to the runway. Sailors use them to determine the distance of a ship from a lighthouse. Astronomers use them to calculate the distance of planets and stars from Earth!",
    "body_hi": "ऊंचाई और दूरियां सिर्फ परीक्षाओं के लिए नहीं हैं। एयर ट्रैफिक कंट्रोलर हवाई जहाजों को रनवे पर सुरक्षित रूप से निर्देशित करने के लिए इन अवधारणाओं का उपयोग करते हैं। नाविक लाइटहाउस से जहाज की दूरी निर्धारित करने के लिए उनका उपयोग करते हैं। खगोलविदों पृथ्वी से ग्रहों और तारों की दूरी की गणना करने के लिए उनका उपयोग करते हैं!",
    "body_gu": "ઊંચાઈ અને અંતર માત્ર પરીક્ષાઓ માટે નથી. એર ટ્રાફિક કંટ્રોલર એરોપ્લેનને સુરક્ષિત રીતે રનવે પર માર્ગદર્શન આપવા માટે આ ખ્યાલોનો ઉપયોગ કરે છે. નાવિકો લાઇટહાઉસથી વહાણનું અંતર નક્કી કરવા માટે તેનો ઉપયોગ કરે છે. ખગોળશાસ્ત્રીઓ પૃથ્વીથી ગ્રહો અને તારાઓના અંતરની ગણતરી કરવા માટે તેનો ઉપયોગ કરે છે!"
})

blocks.append({
    "id": "MATH10_CH09_MASTERY_01",
    "type": "mastery",
    "title": "The 3-Step Method to Solve Any Problem",
    "title_hi": "किसी भी समस्या को हल करने की 3-चरणीय विधि",
    "title_gu": "કોઈપણ સમસ્યા હલ કરવાની 3-પગલાની રીત",
    "body": "To solve any height and distance problem:\n1. Draw a clean, accurate Right-Angled Triangle based on the word problem.\n2. Label the known sides/angles and the unknown side (x).\n3. Choose the correct Trigonometric Ratio (sin, cos, or tan) that links the known and unknown values, and solve for x.\n\nNow, let's practice with all the textbook exercises!",
    "body_hi": "किसी भी ऊंचाई और दूरी की समस्या को हल करने के लिए:\n1. शब्द समस्या के आधार पर एक साफ, सटीक समकोण त्रिभुज बनाएं।\n2. ज्ञात भुजाओं/कोणों और अज्ञात भुजा (x) को लेबल करें।\n3. सही त्रिकोणमितीय अनुपात (sin, cos, या tan) चुनें जो ज्ञात और अज्ञात मूल्यों को जोड़ता है, और x के लिए हल करें।\n\nअब, आइए पाठ्यपुस्तक के सभी अभ्यासों के साथ अभ्यास करें!",
    "body_gu": "ઊંચાઈ અને અંતરની કોઈપણ સમસ્યા હલ કરવા માટે:\n1. શબ્દ સમસ્યાના આધારે સ્વચ્છ, સચોટ કાટકોણ ત્રિકોણ દોરો.\n2. જાણીતી બાજુઓ/ખૂણાઓ અને અજ્ઞાત બાજુ (x) ને લેબલ કરો.\n3. સાચો ત્રિકોણમિતીય ગુણોત્તર (sin, cos અથવા tan) પસંદ કરો જે જાણીતા અને અજ્ઞાત મૂલ્યોને જોડે છે, અને x માટે ઉકેલો.\n\nહવે, ચાલો પાઠ્યપુસ્તકના તમામ સ્વાધ્યાય સાથે પ્રેક્ટિસ કરીએ!"
})

# Let's add exact NCERT Exercise 9.1 questions and then 34+ more MCQs
# I will write a generator function

mcqs = []

# Q1
mcqs.append({
    "id": "MATH10_CH09_EX1_Q01",
    "type": "mcq",
    "title": "NCERT Exercise 9.1 - Q1",
    "title_hi": "NCERT प्रश्नावली 9.1 - प्रश्न 1",
    "title_gu": "NCERT સ્વાધ્યાય 9.1 - પ્રશ્ન 1",
    "body": "A circus artist is climbing a 20 m long rope, which is tightly stretched and tied from the top of a vertical pole to the ground. Find the height of the pole, if the angle made by the rope with the ground level is 30°.",
    "body_hi": "सर्कस का एक कलाकार एक 20 मीटर लंबी डोरी पर चढ़ रहा है, जो अच्छी तरह से तनी हुई है और एक ऊर्ध्वाधर खंभे के शिखर से जमीन तक बंधी है। खंभे की ऊंचाई ज्ञात कीजिए, यदि डोरी द्वारा जमीन के स्तर के साथ बनाया गया कोण 30° है।",
    "body_gu": "એક સર્કસનો કલાકાર 20 મીટર લાંબા દોરડા પર ચઢી રહ્યો છે, જે ચુસ્ત રીતે ખેંચાયેલું છે અને એક ઊભા થાંભલાની ટોચથી જમીન સુધી બાંધેલું છે. થાંભલાની ઊંચાઈ શોધો, જો દોરડા દ્વારા જમીનના સ્તર સાથે બનેલો ખૂણો 30° હોય.",
    "options": ["10 m", "10√3 m", "20 m", "15 m"],
    "options_hi": ["10 मीटर", "10√3 मीटर", "20 मीटर", "15 मीटर"],
    "options_gu": ["10 મીટર", "10√3 મીટર", "20 મીટર", "15 મીટર"],
    "correct_index": 0,
    "explanation": "Let height of pole = h. The rope is hypotenuse = 20m. Angle = 30°. sin(30°) = Perpendicular / Hypotenuse = h / 20. Since sin(30°) = 1/2, 1/2 = h / 20 => h = 10 m.",
    "explanation_hi": "माना खंभे की ऊंचाई = h है। डोरी कर्ण = 20 मीटर है। कोण = 30° है। sin(30°) = लंब / कर्ण = h / 20। चूंकि sin(30°) = 1/2, 1/2 = h / 20 => h = 10 मीटर।",
    "explanation_gu": "ધારો કે થાંભલાની ઊંચાઈ = h. દોરડું કર્ણ = 20 મીટર છે. ખૂણો = 30° છે. sin(30°) = લંબ / કર્ણ = h / 20. કારણ કે sin(30°) = 1/2, 1/2 = h / 20 => h = 10 મીટર."
})

# Q2
mcqs.append({
    "id": "MATH10_CH09_EX1_Q02",
    "type": "mcq",
    "title": "NCERT Exercise 9.1 - Q2",
    "title_hi": "NCERT प्रश्नावली 9.1 - प्रश्न 2",
    "title_gu": "NCERT સ્વાધ્યાય 9.1 - પ્રશ્ન 2",
    "body": "A tree breaks due to a storm and the broken part bends so that the top of the tree touches the ground making an angle 30° with it. The distance between the foot of the tree to the point where the top touches the ground is 8 m. Find the height of the tree.",
    "body_hi": "आंधी आने से एक पेड़ टूट जाता है और टूटा हुआ भाग इस तरह झुक जाता है कि पेड़ का शिखर जमीन को छूने लगता है और इसके साथ 30° का कोण बनाता है। पेड़ के पाद-बिंदु से उस बिंदु तक की दूरी जहां शिखर जमीन को छूता है, 8 मीटर है। पेड़ की ऊंचाई ज्ञात कीजिए।",
    "body_gu": "વાવાઝોડાને કારણે એક ઝાડ તૂટી જાય છે અને તૂટેલો ભાગ એવી રીતે વળી જાય છે કે ઝાડની ટોચ જમીનને સ્પર્શે છે અને તેની સાથે 30° નો ખૂણો બનાવે છે. ઝાડના પાયાથી તે બિંદુ સુધીનું અંતર જ્યાં ટોચ જમીનને સ્પર્શે છે, 8 મીટર છે. ઝાડની ઊંચાઈ શોધો.",
    "options": ["8√3 m", "16√3 m", "24 m", "8 m"],
    "options_hi": ["8√3 मीटर", "16√3 मीटर", "24 मीटर", "8 मीटर"],
    "options_gu": ["8√3 મીટર", "16√3 મીટર", "24 મીટર", "8 મીટર"],
    "correct_index": 0,
    "explanation": "Let broken part on ground be hypotenuse (y) and standing part be perpendicular (x). Base = 8m. cos(30°) = 8/y => y = 16/√3. tan(30°) = x/8 => x = 8/√3. Total height = x + y = 24/√3 = 8√3 m.",
    "explanation_hi": "माना जमीन पर टूटा भाग कर्ण (y) है और खड़ा भाग लंब (x) है। आधार = 8 मीटर। cos(30°) = 8/y => y = 16/√3। tan(30°) = x/8 => x = 8/√3। कुल ऊंचाई = x + y = 24/√3 = 8√3 मीटर।",
    "explanation_gu": "ધારો કે જમીન પર તૂટેલો ભાગ કર્ણ (y) છે અને ઊભો ભાગ લંબ (x) છે. આધાર = 8 મીટર. cos(30°) = 8/y => y = 16/√3. tan(30°) = x/8 => x = 8/√3. કુલ ઊંચાઈ = x + y = 24/√3 = 8√3 મીટર."
})

# Q3
mcqs.append({
    "id": "MATH10_CH09_EX1_Q03",
    "type": "mcq",
    "title": "NCERT Exercise 9.1 - Q3",
    "title_hi": "NCERT प्रश्नावली 9.1 - प्रश्न 3",
    "title_gu": "NCERT સ્વાધ્યાય 9.1 - પ્રશ્ન 3",
    "body": "A contractor plans to install two slides for children in a park. For children below 5 years, she prefers to have a slide whose top is at a height of 1.5 m and is inclined at 30° to the ground. For elder children, she wants a steep slide at a height of 3 m, inclined at 60°. What should be the length of the slide in each case?",
    "body_hi": "एक ठेकेदार एक पार्क में बच्चों के खेलने के लिए दो फिसलपट्टी लगाना चाहता है। 5 वर्ष से कम उम्र के बच्चों के लिए, वह एक ऐसी फिसलपट्टी पसंद करती है जिसका शिखर 1.5 मीटर की ऊंचाई पर हो और जमीन के साथ 30° के कोण पर झुका हो। बड़े बच्चों के लिए, वह 3 मीटर की ऊंचाई पर 60° के कोण पर एक ढालू फिसलपट्टी लगाना चाहती है। प्रत्येक स्थिति में फिसलपट्टी की लंबाई क्या होनी चाहिए?",
    "body_gu": "એક કોન્ટ્રાક્ટર બાળકો માટે બગીચામાં બે લપસણી લગાવવાનું આયોજન કરે છે. 5 વર્ષથી ઓછી ઉંમરના બાળકો માટે, તેણી એવી લપસણી પસંદ કરે છે જેની ટોચ 1.5 મીટરની ઊંચાઈ પર હોય અને જમીન સાથે 30° નો ખૂણો બનાવે. મોટા બાળકો માટે, તેણી 3 મીટરની ઊંચાઈ પર 60° ના ખૂણે નમેલી લપસણી લગાવવા માંગે છે. દરેક કિસ્સામાં લપસણીની લંબાઈ કેટલી હોવી જોઈએ?",
    "options": ["3 m and 2√3 m", "1.5 m and 3 m", "3 m and 3√3 m", "2√3 m and 3 m"],
    "options_hi": ["3 मीटर और 2√3 मीटर", "1.5 मीटर और 3 मीटर", "3 मीटर और 3√3 मीटर", "2√3 मीटर और 3 मीटर"],
    "options_gu": ["3 મીટર અને 2√3 મીટર", "1.5 મીટર અને 3 મીટર", "3 મીટર અને 3√3 મીટર", "2√3 મીટર અને 3 મીટર"],
    "correct_index": 0,
    "explanation": "Case 1: sin(30°) = 1.5/L1 => 1/2 = 1.5/L1 => L1 = 3 m. Case 2: sin(60°) = 3/L2 => √3/2 = 3/L2 => L2 = 6/√3 = 2√3 m. The lengths are 3m and 2√3m.",
    "explanation_hi": "स्थिति 1: sin(30°) = 1.5/L1 => 1/2 = 1.5/L1 => L1 = 3 मीटर। स्थिति 2: sin(60°) = 3/L2 => √3/2 = 3/L2 => L2 = 6/√3 = 2√3 मीटर। लंबाइयां 3 मीटर और 2√3 मीटर हैं।",
    "explanation_gu": "કિસ્સો 1: sin(30°) = 1.5/L1 => 1/2 = 1.5/L1 => L1 = 3 મીટર. કિસ્સો 2: sin(60°) = 3/L2 => √3/2 = 3/L2 => L2 = 6/√3 = 2√3 મીટર. લંબાઈ 3 મીટર અને 2√3 મીટર છે."
})

# Q4
mcqs.append({
    "id": "MATH10_CH09_EX1_Q04",
    "type": "mcq",
    "title": "NCERT Exercise 9.1 - Q4",
    "title_hi": "NCERT प्रश्नावली 9.1 - प्रश्न 4",
    "title_gu": "NCERT સ્વાધ્યાય 9.1 - પ્રશ્ન 4",
    "body": "The angle of elevation of the top of a tower from a point on the ground, which is 30 m away from the foot of the tower, is 30°. Find the height of the tower.",
    "body_hi": "जमीन के एक बिंदु से, जो मीनार के पाद-बिंदु से 30 मीटर की दूरी पर है, मीनार के शिखर का उन्नयन कोण 30° है। मीनार की ऊंचाई ज्ञात कीजिए।",
    "body_gu": "જમીન પરના એક બિંદુથી, જે ટાવરના પાયાથી 30 મીટર દૂર છે, ટાવરની ટોચનો ઉત્સેધકોણ 30° છે. ટાવરની ઊંચાઈ શોધો.",
    "options": ["10√3 m", "30√3 m", "15 m", "10 m"],
    "options_hi": ["10√3 मीटर", "30√3 मीटर", "15 मीटर", "10 मीटर"],
    "options_gu": ["10√3 મીટર", "30√3 મીટર", "15 મીટર", "10 મીટર"],
    "correct_index": 0,
    "explanation": "Let height be h. tan(30°) = h / 30. 1/√3 = h / 30 => h = 30/√3 = 10√3 m.",
    "explanation_hi": "माना ऊंचाई h है। tan(30°) = h / 30। 1/√3 = h / 30 => h = 30/√3 = 10√3 मीटर।",
    "explanation_gu": "ધારો કે ઊંચાઈ h છે. tan(30°) = h / 30. 1/√3 = h / 30 => h = 30/√3 = 10√3 મીટર."
})

# Q5
mcqs.append({
    "id": "MATH10_CH09_EX1_Q05",
    "type": "mcq",
    "title": "NCERT Exercise 9.1 - Q5",
    "title_hi": "NCERT प्रश्नावली 9.1 - प्रश्न 5",
    "title_gu": "NCERT સ્વાધ્યાય 9.1 - પ્રશ્ન 5",
    "body": "A kite is flying at a height of 60 m above the ground. The string attached to the kite is temporarily tied to a point on the ground. The inclination of the string with the ground is 60°. Find the length of the string, assuming there is no slack.",
    "body_hi": "एक पतंग जमीन से 60 मीटर की ऊंचाई पर उड़ रही है। पतंग से जुड़ी डोरी को अस्थायी रूप से जमीन के एक बिंदु से बांध दिया गया है। जमीन के साथ डोरी का झुकाव 60° है। डोरी की लंबाई ज्ञात कीजिए, यह मानते हुए कि डोरी में कोई ढील नहीं है।",
    "body_gu": "એક પતંગ જમીનથી 60 મીટરની ઊંચાઈ પર ઉડી રહી છે. પતંગ સાથે જોડાયેલી દોરી કામચલાઉ રીતે જમીન પરના એક બિંદુ સાથે બાંધેલી છે. જમીન સાથે દોરીનો ઝુકાવ 60° છે. દોરીની લંબાઈ શોધો, એ માનીને કે દોરીમાં કોઈ ઢીલ નથી.",
    "options": ["40√3 m", "20√3 m", "60 m", "120 m"],
    "options_hi": ["40√3 मीटर", "20√3 मीटर", "60 मीटर", "120 मीटर"],
    "options_gu": ["40√3 મીટર", "20√3 મીટર", "60 મીટર", "120 મીટર"],
    "correct_index": 0,
    "explanation": "sin(60°) = 60 / Length. √3/2 = 60 / L => L = 120 / √3 = 40√3 m.",
    "explanation_hi": "sin(60°) = 60 / लंबाई। √3/2 = 60 / L => L = 120 / √3 = 40√3 मीटर।",
    "explanation_gu": "sin(60°) = 60 / લંબાઈ. √3/2 = 60 / L => L = 120 / √3 = 40√3 મીટર."
})

# Q6
mcqs.append({
    "id": "MATH10_CH09_EX1_Q06",
    "type": "mcq",
    "title": "NCERT Exercise 9.1 - Q6",
    "title_hi": "NCERT प्रश्नावली 9.1 - प्रश्न 6",
    "title_gu": "NCERT સ્વાધ્યાય 9.1 - પ્રશ્ન 6",
    "body": "A 1.5 m tall boy is standing at some distance from a 30 m tall building. The angle of elevation from his eyes to the top of the building increases from 30° to 60° as he walks towards the building. Find the distance he walked towards the building.",
    "body_hi": "एक 1.5 मीटर लंबा लड़का 30 मीटर ऊंची इमारत से कुछ दूरी पर खड़ा है। जब वह इमारत की ओर चलता है, तो उसकी आंखों से इमारत के शिखर का उन्नयन कोण 30° से बढ़कर 60° हो जाता है। ज्ञात कीजिए कि वह इमारत की ओर कितनी दूरी चला।",
    "body_gu": "એક 1.5 મીટર ઊંચો છોકરો 30 મીટર ઊંચી ઇમારતથી અમુક અંતરે ઉભો છે. જ્યારે તે ઇમારત તરફ ચાલે છે, ત્યારે તેની આંખોથી ઇમારતની ટોચનો ઉત્સેધકોણ 30° થી વધીને 60° થાય છે. શોધો કે તે ઇમારત તરફ કેટલું અંતર ચાલ્યો.",
    "options": ["19√3 m", "28.5 m", "19 m", "28.5√3 m"],
    "options_hi": ["19√3 मीटर", "28.5 मीटर", "19 मीटर", "28.5√3 मीटर"],
    "options_gu": ["19√3 મીટર", "28.5 મીટર", "19 મીટર", "28.5√3 મીટર"],
    "correct_index": 0,
    "explanation": "Effective height of building = 30 - 1.5 = 28.5 m. Initial distance (x+y): tan(30°) = 28.5 / (x+y) => x+y = 28.5√3. Final distance (y): tan(60°) = 28.5 / y => y = 28.5/√3 = 9.5√3. Distance walked (x) = 28.5√3 - 9.5√3 = 19√3 m.",
    "explanation_hi": "इमारत की प्रभावी ऊंचाई = 30 - 1.5 = 28.5 मीटर। प्रारंभिक दूरी (x+y): tan(30°) = 28.5 / (x+y) => x+y = 28.5√3। अंतिम दूरी (y): tan(60°) = 28.5 / y => y = 28.5/√3 = 9.5√3। चली गई दूरी (x) = 28.5√3 - 9.5√3 = 19√3 मीटर।",
    "explanation_gu": "ઇમારતની અસરકારક ઊંચાઈ = 30 - 1.5 = 28.5 મીટર. પ્રારંભિક અંતર (x+y): tan(30°) = 28.5 / (x+y) => x+y = 28.5√3. અંતિમ અંતર (y): tan(60°) = 28.5 / y => y = 28.5/√3 = 9.5√3. ચાલેલું અંતર (x) = 28.5√3 - 9.5√3 = 19√3 મીટર."
})

# Q7
mcqs.append({
    "id": "MATH10_CH09_EX1_Q07",
    "type": "mcq",
    "title": "NCERT Exercise 9.1 - Q7",
    "title_hi": "NCERT प्रश्नावली 9.1 - प्रश्न 7",
    "title_gu": "NCERT સ્વાધ્યાય 9.1 - પ્રશ્ન 7",
    "body": "From a point on the ground, the angles of elevation of the bottom and the top of a transmission tower fixed at the top of a 20 m high building are 45° and 60° respectively. Find the height of the tower.",
    "body_hi": "जमीन के एक बिंदु से, एक 20 मीटर ऊंचे भवन के शिखर पर लगे एक संचार मीनार के तल और शिखर के उन्नयन कोण क्रमशः 45° और 60° हैं। मीनार की ऊंचाई ज्ञात कीजिए।",
    "body_gu": "જમીન પરના એક બિંદુથી, 20 મીટર ઊંચા મકાનની ટોચ પર લગાવેલા ટ્રાન્સમિશન ટાવરના તળિયા અને ટોચના ઉત્સેધકોણ અનુક્રમે 45° અને 60° છે. ટાવરની ઊંચાઈ શોધો.",
    "options": ["20(√3 - 1) m", "20(√3 + 1) m", "20√3 m", "40 m"],
    "options_hi": ["20(√3 - 1) मीटर", "20(√3 + 1) मीटर", "20√3 मीटर", "40 मीटर"],
    "options_gu": ["20(√3 - 1) મીટર", "20(√3 + 1) મીટર", "20√3 મીટર", "40 મીટર"],
    "correct_index": 0,
    "explanation": "Let distance from building be x. tan(45°) = 20 / x => x = 20 m. Let height of tower be h. tan(60°) = (20 + h) / x => √3 = (20 + h) / 20 => 20√3 = 20 + h => h = 20(√3 - 1) m.",
    "explanation_hi": "माना भवन से दूरी x है। tan(45°) = 20 / x => x = 20 मीटर। माना मीनार की ऊंचाई h है। tan(60°) = (20 + h) / x => √3 = (20 + h) / 20 => 20√3 = 20 + h => h = 20(√3 - 1) मीटर।",
    "explanation_gu": "ધારો કે મકાનથી અંતર x છે. tan(45°) = 20 / x => x = 20 મીટર. ધારો કે ટાવરની ઊંચાઈ h છે. tan(60°) = (20 + h) / x => √3 = (20 + h) / 20 => 20√3 = 20 + h => h = 20(√3 - 1) મીટર."
})

# Q8
mcqs.append({
    "id": "MATH10_CH09_EX1_Q08",
    "type": "mcq",
    "title": "NCERT Exercise 9.1 - Q8",
    "title_hi": "NCERT प्रश्नावली 9.1 - प्रश्न 8",
    "title_gu": "NCERT સ્વાધ્યાય 9.1 - પ્રશ્ન 8",
    "body": "A statue, 1.6 m tall, stands on the top of a pedestal. From a point on the ground, the angle of elevation of the top of the statue is 60° and from the same point the angle of elevation of the top of the pedestal is 45°. Find the height of the pedestal.",
    "body_hi": "एक पेडस्टल के शिखर पर एक 1.6 मीटर ऊंची मूर्ति लगी है। जमीन के एक बिंदु से मूर्ति के शिखर का उन्नयन कोण 60° है और उसी बिंदु से पेडस्टल के शिखर का उन्नयन कोण 45° है। पेडस्टल की ऊंचाई ज्ञात कीजिए।",
    "body_gu": "એક પેડેસ્ટલ (બેઠક) ની ટોચ પર 1.6 મીટર ઊંચી પ્રતિમા મૂકેલી છે. જમીન પરના એક બિંદુથી પ્રતિમાની ટોચનો ઉત્સેધકોણ 60° છે અને તે જ બિંદુથી પેડેસ્ટલની ટોચનો ઉત્સેધકોણ 45° છે. પેડેસ્ટલની ઊંચાઈ શોધો.",
    "options": ["0.8(√3 + 1) m", "1.6(√3 - 1) m", "0.8(√3 - 1) m", "1.6(√3 + 1) m"],
    "options_hi": ["0.8(√3 + 1) मीटर", "1.6(√3 - 1) मीटर", "0.8(√3 - 1) मीटर", "1.6(√3 + 1) मीटर"],
    "options_gu": ["0.8(√3 + 1) મીટર", "1.6(√3 - 1) મીટર", "0.8(√3 - 1) મીટર", "1.6(√3 + 1) મીટર"],
    "correct_index": 0,
    "explanation": "Let height of pedestal be h, distance be x. tan(45°) = h / x => x = h. tan(60°) = (h + 1.6) / x => √3 = (h + 1.6) / h => h√3 - h = 1.6 => h(√3 - 1) = 1.6 => h = 1.6 / (√3 - 1) = 1.6(√3 + 1) / 2 = 0.8(√3 + 1) m.",
    "explanation_hi": "माना पेडस्टल की ऊंचाई h है, दूरी x है। tan(45°) = h / x => x = h। tan(60°) = (h + 1.6) / x => √3 = (h + 1.6) / h => h√3 - h = 1.6 => h(√3 - 1) = 1.6 => h = 1.6 / (√3 - 1) = 1.6(√3 + 1) / 2 = 0.8(√3 + 1) मीटर।",
    "explanation_gu": "ધારો કે પેડેસ્ટલની ઊંચાઈ h છે, અંતર x છે. tan(45°) = h / x => x = h. tan(60°) = (h + 1.6) / x => √3 = (h + 1.6) / h => h√3 - h = 1.6 => h(√3 - 1) = 1.6 => h = 1.6 / (√3 - 1) = 1.6(√3 + 1) / 2 = 0.8(√3 + 1) મીટર."
})

# Q9
mcqs.append({
    "id": "MATH10_CH09_EX1_Q09",
    "type": "mcq",
    "title": "NCERT Exercise 9.1 - Q9",
    "title_hi": "NCERT प्रश्नावली 9.1 - प्रश्न 9",
    "title_gu": "NCERT સ્વાધ્યાય 9.1 - પ્રશ્ન 9",
    "body": "The angle of elevation of the top of a building from the foot of the tower is 30° and the angle of elevation of the top of the tower from the foot of the building is 60°. If the tower is 50 m high, find the height of the building.",
    "body_hi": "एक मीनार के पाद-बिंदु से एक भवन के शिखर का उन्नयन कोण 30° है और भवन के पाद-बिंदु से मीनार के शिखर का उन्नयन कोण 60° है। यदि मीनार 50 मीटर ऊंची हो, तो भवन की ऊंचाई ज्ञात कीजिए।",
    "body_gu": "એક ટાવરના પાયાથી એક ઇમારતની ટોચનો ઉત્સેધકોણ 30° છે અને ઇમારતના પાયાથી ટાવરની ટોચનો ઉત્સેધકોણ 60° છે. જો ટાવર 50 મીટર ઊંચો હોય, તો ઇમારતની ઊંચાઈ શોધો.",
    "options": ["16.67 m (or 50/3 m)", "25 m", "50√3 m", "20 m"],
    "options_hi": ["16.67 मीटर (या 50/3 मीटर)", "25 मीटर", "50√3 मीटर", "20 मीटर"],
    "options_gu": ["16.67 મીટર (અથવા 50/3 મીટર)", "25 મીટર", "50√3 મીટર", "20 મીટર"],
    "correct_index": 0,
    "explanation": "Let distance between them be x. tan(60°) = 50 / x => √3 = 50 / x => x = 50/√3. Let building height be h. tan(30°) = h / x => 1/√3 = h / (50/√3) => h = 50/3 = 16.67 m.",
    "explanation_hi": "माना उनके बीच की दूरी x है। tan(60°) = 50 / x => √3 = 50 / x => x = 50/√3। माना भवन की ऊंचाई h है। tan(30°) = h / x => 1/√3 = h / (50/√3) => h = 50/3 = 16.67 मीटर।",
    "explanation_gu": "ધારો કે તેમની વચ્ચેનું અંતર x છે. tan(60°) = 50 / x => √3 = 50 / x => x = 50/√3. ધારો કે ઇમારતની ઊંચાઈ h છે. tan(30°) = h / x => 1/√3 = h / (50/√3) => h = 50/3 = 16.67 મીટર."
})

# Q10
mcqs.append({
    "id": "MATH10_CH09_EX1_Q10",
    "type": "mcq",
    "title": "NCERT Exercise 9.1 - Q10",
    "title_hi": "NCERT प्रश्नावली 9.1 - प्रश्न 10",
    "title_gu": "NCERT સ્વાધ્યાય 9.1 - પ્રશ્ન 10",
    "body": "Two poles of equal heights are standing opposite each other on either side of the road, which is 80 m wide. From a point between them on the road, the angles of elevation of the top of the poles are 60° and 30°, respectively. Find the height of the poles and the distances of the point from the poles.",
    "body_hi": "एक 80 मीटर चौड़ी सड़क के दोनों ओर आमने-सामने समान लंबाई वाले दो खंभे लगे हुए हैं। सड़क के बीच एक बिंदु से खंभों के शिखर के उन्नयन कोण क्रमशः 60° और 30° हैं। खंभों की ऊंचाई और खंभों से बिंदु की दूरी ज्ञात कीजिए।",
    "body_gu": "80 મીટર પહોળા રસ્તાની બંને બાજુએ સમાન ઊંચાઈના બે થાંભલા સામસામે ઉભા છે. રસ્તા પરના તેમની વચ્ચેના એક બિંદુથી થાંભલાઓની ટોચના ઉત્સેધકોણ અનુક્રમે 60° અને 30° છે. થાંભલાઓની ઊંચાઈ અને થાંભલાઓથી તે બિંદુના અંતર શોધો.",
    "options": ["Height = 20√3 m, Distances = 20 m & 60 m", "Height = 10√3 m, Distances = 40 m & 40 m", "Height = 40√3 m, Distances = 20 m & 60 m", "Height = 20 m, Distances = 30 m & 50 m"],
    "options_hi": ["ऊंचाई = 20√3 मीटर, दूरियां = 20 मीटर और 60 मीटर", "ऊंचाई = 10√3 मीटर, दूरियां = 40 मीटर और 40 मीटर", "ऊंचाई = 40√3 मीटर, दूरियां = 20 मीटर और 60 मीटर", "ऊंचाई = 20 मीटर, दूरियां = 30 मीटर और 50 मीटर"],
    "options_gu": ["ઊંચાઈ = 20√3 મીટર, અંતર = 20 મીટર અને 60 મીટર", "ઊંચાઈ = 10√3 મીટર, અંતર = 40 મીટર અને 40 મીટર", "ઊંચાઈ = 40√3 મીટર, અંતર = 20 મીટર અને 60 મીટર", "ઊંચાઈ = 20 મીટર, અંતર = 30 મીટર અને 50 મીટર"],
    "correct_index": 0,
    "explanation": "Let height = h. Point is x m from first pole, (80-x) from second. tan(60°) = h/x => h = x√3. tan(30°) = h/(80-x) => 1/√3 = x√3 / (80-x) => 80-x = 3x => 4x = 80 => x = 20 m. So distances are 20m & 60m. h = 20√3 m.",
    "explanation_hi": "माना ऊंचाई = h। बिंदु पहले खंभे से x मीटर और दूसरे से (80-x) मीटर दूर है। tan(60°) = h/x => h = x√3। tan(30°) = h/(80-x) => 1/√3 = x√3 / (80-x) => 80-x = 3x => 4x = 80 => x = 20 मीटर। तो दूरियां 20 मीटर और 60 मीटर हैं। h = 20√3 मीटर।",
    "explanation_gu": "ધારો કે ઊંચાઈ = h. બિંદુ પહેલા થાંભલાથી x મીટર, બીજાથી (80-x) મીટર દૂર છે. tan(60°) = h/x => h = x√3. tan(30°) = h/(80-x) => 1/√3 = x√3 / (80-x) => 80-x = 3x => 4x = 80 => x = 20 મીટર. તેથી અંતર 20 મીટર અને 60 મીટર છે. h = 20√3 મીટર."
})

# Q11
mcqs.append({
    "id": "MATH10_CH09_EX1_Q11",
    "type": "mcq",
    "title": "NCERT Exercise 9.1 - Q11",
    "title_hi": "NCERT प्रश्नावली 9.1 - प्रश्न 11",
    "title_gu": "NCERT સ્વાધ્યાય 9.1 - પ્રશ્ન 11",
    "body": "A TV tower stands vertically on a bank of a canal. From a point on the other bank directly opposite the tower, the angle of elevation of the top of the tower is 60°. From another point 20 m away from this point on the line joining this point to the foot of the tower, the angle of elevation of the top of the tower is 30°. Find the height of the tower and the width of the canal.",
    "body_hi": "एक नहर के एक तट पर एक टीवी टावर ऊर्ध्वाधर खड़ा है। टावर के ठीक सामने दूसरे तट के एक बिंदु से टावर के शिखर का उन्नयन कोण 60° है। इस बिंदु से 20 मीटर दूर और इस बिंदु को मीनार के पाद से मिलाने वाली रेखा पर स्थित एक अन्य बिंदु से टावर के शिखर का उन्नयन कोण 30° है। टावर की ऊंचाई और नहर की चौड़ाई ज्ञात कीजिए।",
    "body_gu": "નહેરના એક કાંઠે એક ટીવી ટાવર ઊભો છે. ટાવરની બરાબર સામે બીજા કાંઠાના એક બિંદુથી ટાવરની ટોચનો ઉત્સેધકોણ 60° છે. આ બિંદુથી 20 મીટર દૂર અને આ બિંદુને ટાવરના પાયા સાથે જોડતી રેખા પરના બીજા બિંદુથી ટાવરની ટોચનો ઉત્સેધકોણ 30° છે. ટાવરની ઊંચાઈ અને નહેરની પહોળાઈ શોધો.",
    "options": ["Height = 10√3 m, Width = 10 m", "Height = 20√3 m, Width = 20 m", "Height = 10 m, Width = 10√3 m", "Height = 30 m, Width = 15 m"],
    "options_hi": ["ऊंचाई = 10√3 मीटर, चौड़ाई = 10 मीटर", "ऊंचाई = 20√3 मीटर, चौड़ाई = 20 मीटर", "ऊंचाई = 10 मीटर, चौड़ाई = 10√3 मीटर", "ऊंचाई = 30 मीटर, चौड़ाई = 15 मीटर"],
    "options_gu": ["ઊંચાઈ = 10√3 મીટર, પહોળાઈ = 10 મીટર", "ઊંચાઈ = 20√3 મીટર, પહોળાઈ = 20 મીટર", "ઊંચાઈ = 10 મીટર, પહોળાઈ = 10√3 મીટર", "ઊંચાઈ = 30 મીટર, પહોળાઈ = 15 મીટર"],
    "correct_index": 0,
    "explanation": "Let height be h and width of canal be x. tan(60°) = h/x => h = x√3. tan(30°) = h/(x+20) => 1/√3 = (x√3)/(x+20) => x+20 = 3x => 2x = 20 => x = 10 m. Then h = 10√3 m.",
    "explanation_hi": "माना ऊंचाई h और नहर की चौड़ाई x है। tan(60°) = h/x => h = x√3। tan(30°) = h/(x+20) => 1/√3 = (x√3)/(x+20) => x+20 = 3x => 2x = 20 => x = 10 मीटर। तब h = 10√3 मीटर।",
    "explanation_gu": "ધારો કે ઊંચાઈ h છે અને નહેરની પહોળાઈ x છે. tan(60°) = h/x => h = x√3. tan(30°) = h/(x+20) => 1/√3 = (x√3)/(x+20) => x+20 = 3x => 2x = 20 => x = 10 મીટર. તો h = 10√3 મીટર."
})

# Q12
mcqs.append({
    "id": "MATH10_CH09_EX1_Q12",
    "type": "mcq",
    "title": "NCERT Exercise 9.1 - Q12",
    "title_hi": "NCERT प्रश्नावली 9.1 - प्रश्न 12",
    "title_gu": "NCERT સ્વાધ્યાય 9.1 - પ્રશ્ન 12",
    "body": "From the top of a 7 m high building, the angle of elevation of the top of a cable tower is 60° and the angle of depression of its foot is 45°. Determine the height of the tower.",
    "body_hi": "एक 7 मीटर ऊंचे भवन के शिखर से एक केबल टावर के शिखर का उन्नयन कोण 60° है और इसके पाद का अवनमन कोण 45° है। टावर की ऊंचाई निर्धारित कीजिए।",
    "body_gu": "7 મીટર ઊંચી ઇમારતની ટોચ પરથી એક કેબલ ટાવરની ટોચનો ઉત્સેધકોણ 60° છે અને તેના પાયાનો અવસેધકોણ 45° છે. ટાવરની ઊંચાઈ નક્કી કરો.",
    "options": ["7(√3 + 1) m", "7(√3 - 1) m", "14 m", "7√3 m"],
    "options_hi": ["7(√3 + 1) मीटर", "7(√3 - 1) मीटर", "14 मीटर", "7√3 मीटर"],
    "options_gu": ["7(√3 + 1) મીટર", "7(√3 - 1) મીટર", "14 મીટર", "7√3 મીટર"],
    "correct_index": 0,
    "explanation": "Let distance between them be x. Angle of depression to foot is 45°, so tan(45°) = 7/x => x = 7 m. Let tower part above building be h. tan(60°) = h/x => √3 = h/7 => h = 7√3 m. Total height = h + 7 = 7√3 + 7 = 7(√3 + 1) m.",
    "explanation_hi": "माना उनके बीच की दूरी x है। पाद तक का अवनमन कोण 45° है, इसलिए tan(45°) = 7/x => x = 7 मीटर। माना भवन के ऊपर टावर का भाग h है। tan(60°) = h/x => √3 = h/7 => h = 7√3 मीटर। कुल ऊंचाई = h + 7 = 7√3 + 7 = 7(√3 + 1) मीटर।",
    "explanation_gu": "ધારો કે તેમની વચ્ચેનું અંતર x છે. પાયા સુધીનો અવસેધકોણ 45° છે, તેથી tan(45°) = 7/x => x = 7 મીટર. ધારો કે ઇમારતની ઉપર ટાવરનો ભાગ h છે. tan(60°) = h/x => √3 = h/7 => h = 7√3 મીટર. કુલ ઊંચાઈ = h + 7 = 7√3 + 7 = 7(√3 + 1) મીટર."
})

# Q13
mcqs.append({
    "id": "MATH10_CH09_EX1_Q13",
    "type": "mcq",
    "title": "NCERT Exercise 9.1 - Q13",
    "title_hi": "NCERT प्रश्नावली 9.1 - प्रश्न 13",
    "title_gu": "NCERT સ્વાધ્યાય 9.1 - પ્રશ્ન 13",
    "body": "As observed from the top of a 75 m high lighthouse from the sea-level, the angles of depression of two ships are 30° and 45°. If one ship is exactly behind the other on the same side of the lighthouse, find the distance between the two ships.",
    "body_hi": "समुद्र तल से 75 मीटर ऊंचे लाइटहाउस के शिखर से देखने पर दो समुद्री जहाजों के अवनमन कोण 30° और 45° हैं। यदि लाइटहाउस के एक ही ओर एक जहाज दूसरे जहाज के ठीक पीछे हो, तो दो जहाजों के बीच की दूरी ज्ञात कीजिए।",
    "body_gu": "દરિયાની સપાટીથી 75 મીટર ઊંચા લાઇટહાઉસની ટોચ પરથી જોતાં બે જહાજોના અવસેધકોણ 30° અને 45° છે. જો લાઇટહાઉસની એક જ બાજુએ એક જહાજ બીજા જહાજની બરાબર પાછળ હોય, તો બંને જહાજો વચ્ચેનું અંતર શોધો.",
    "options": ["75(√3 - 1) m", "75(√3 + 1) m", "75√3 m", "75 m"],
    "options_hi": ["75(√3 - 1) मीटर", "75(√3 + 1) मीटर", "75√3 मीटर", "75 मीटर"],
    "options_gu": ["75(√3 - 1) મીટર", "75(√3 + 1) મીટર", "75√3 મીટર", "75 મીટર"],
    "correct_index": 0,
    "explanation": "Distance of first ship: tan(45°) = 75/x => x = 75 m. Distance of second ship: tan(30°) = 75/y => 1/√3 = 75/y => y = 75√3 m. Distance between ships = y - x = 75√3 - 75 = 75(√3 - 1) m.",
    "explanation_hi": "पहले जहाज की दूरी: tan(45°) = 75/x => x = 75 मीटर। दूसरे जहाज की दूरी: tan(30°) = 75/y => 1/√3 = 75/y => y = 75√3 मीटर। जहाजों के बीच की दूरी = y - x = 75√3 - 75 = 75(√3 - 1) मीटर।",
    "explanation_gu": "પ્રથમ જહાજનું અંતર: tan(45°) = 75/x => x = 75 મીટર. બીજા જહાજનું અંતર: tan(30°) = 75/y => 1/√3 = 75/y => y = 75√3 મીટર. જહાજો વચ્ચેનું અંતર = y - x = 75√3 - 75 = 75(√3 - 1) મીટર."
})

# Q14
mcqs.append({
    "id": "MATH10_CH09_EX1_Q14",
    "type": "mcq",
    "title": "NCERT Exercise 9.1 - Q14",
    "title_hi": "NCERT प्रश्नावली 9.1 - प्रश्न 14",
    "title_gu": "NCERT સ્વાધ્યાય 9.1 - પ્રશ્ન 14",
    "body": "A 1.2 m tall girl spots a balloon moving with the wind in a horizontal line at a height of 88.2 m from the ground. The angle of elevation of the balloon from the eyes of the girl at any instant is 60°. After some time, the angle of elevation reduces to 30°. Find the distance travelled by the balloon during the interval.",
    "body_hi": "1.2 मीटर लंबी एक लड़की जमीन से 88.2 मीटर की ऊंचाई पर एक क्षैतिज रेखा में हवा के साथ उड़ रहे गुब्बारे को देखती है। किसी भी क्षण लड़की की आंखों से गुब्बारे का उन्नयन कोण 60° है। कुछ समय बाद, उन्नयन कोण घटकर 30° हो जाता है। इस अंतराल के दौरान गुब्बारे द्वारा तय की गई दूरी ज्ञात कीजिए।",
    "body_gu": "1.2 મીટર ઊંચી એક છોકરી જમીનથી 88.2 મીટરની ઊંચાઈ પર આડી રેખામાં પવન સાથે ઉડતા બલૂનને જુએ છે. કોઈપણ ક્ષણે છોકરીની આંખોથી બલૂનનો ઉત્સેધકોણ 60° છે. થોડા સમય પછી, ઉત્સેધકોણ ઘટીને 30° થાય છે. આ સમયગાળા દરમિયાન બલૂન દ્વારા કપાયેલું અંતર શોધો.",
    "options": ["58√3 m", "87√3 m", "29√3 m", "58 m"],
    "options_hi": ["58√3 मीटर", "87√3 मीटर", "29√3 मीटर", "58 मीटर"],
    "options_gu": ["58√3 મીટર", "87√3 મીટર", "29√3 મીટર", "58 મીટર"],
    "correct_index": 0,
    "explanation": "Effective height = 88.2 - 1.2 = 87 m. Initial distance (x): tan(60°) = 87/x => √3 = 87/x => x = 29√3 m. Final distance (y): tan(30°) = 87/y => 1/√3 = 87/y => y = 87√3 m. Distance travelled = y - x = 87√3 - 29√3 = 58√3 m.",
    "explanation_hi": "प्रभावी ऊंचाई = 88.2 - 1.2 = 87 मीटर। प्रारंभिक दूरी (x): tan(60°) = 87/x => √3 = 87/x => x = 29√3 मीटर। अंतिम दूरी (y): tan(30°) = 87/y => 1/√3 = 87/y => y = 87√3 मीटर। तय की गई दूरी = y - x = 87√3 - 29√3 = 58√3 मीटर।",
    "explanation_gu": "અસરકારક ઊંચાઈ = 88.2 - 1.2 = 87 મીટર. પ્રારંભિક અંતર (x): tan(60°) = 87/x => √3 = 87/x => x = 29√3 મીટર. અંતિમ અંતર (y): tan(30°) = 87/y => 1/√3 = 87/y => y = 87√3 મીટર. કપાયેલું અંતર = y - x = 87√3 - 29√3 = 58√3 મીટર."
})

# Q15
mcqs.append({
    "id": "MATH10_CH09_EX1_Q15",
    "type": "mcq",
    "title": "NCERT Exercise 9.1 - Q15",
    "title_hi": "NCERT प्रश्नावली 9.1 - प्रश्न 15",
    "title_gu": "NCERT સ્વાધ્યાય 9.1 - પ્રશ્ન 15",
    "body": "A straight highway leads to the foot of a tower. A man standing at the top of the tower observes a car at an angle of depression of 30°, which is approaching the foot of the tower with a uniform speed. Six seconds later, the angle of depression of the car is found to be 60°. Find the time taken by the car to reach the foot of the tower from this point.",
    "body_hi": "एक सीधा राजमार्ग एक मीनार के पाद तक जाता है। मीनार के शिखर पर खड़ा एक आदमी एक कार को 30° के अवनमन कोण पर देखता है, जो एक समान गति से मीनार के पाद की ओर आ रही है। छह सेकंड बाद, कार का अवनमन कोण 60° हो जाता है। इस बिंदु से मीनार के पाद तक पहुंचने में कार द्वारा लिया गया समय ज्ञात कीजिए।",
    "body_gu": "એક સીધો હાઇવે ટાવરના પાયા તરફ જાય છે. ટાવરની ટોચ પર ઉભેલો માણસ એક કારને 30° ના અવસેધકોણે જુએ છે, જે સમાન ઝડપે ટાવરના પાયા તરફ આવી રહી છે. છ સેકન્ડ પછી, કારનો અવસેધકોણ 60° જણાય છે. આ બિંદુથી ટાવરના પાયા સુધી પહોંચવા માટે કાર દ્વારા લેવાયેલો સમય શોધો.",
    "options": ["3 seconds", "6 seconds", "2 seconds", "4 seconds"],
    "options_hi": ["3 सेकंड", "6 सेकंड", "2 सेकंड", "4 सेकंड"],
    "options_gu": ["3 સેકન્ડ", "6 સેકન્ડ", "2 સેકન્ડ", "4 સેકન્ડ"],
    "correct_index": 0,
    "explanation": "Let height be h. Initial distance (x+y): tan(30°) = h/(x+y) => x+y = h√3. Later distance (y): tan(60°) = h/y => y = h/√3. Distance travelled in 6s = x = h√3 - h/√3 = 2h/√3. Since distance 2h/√3 takes 6s, distance h/√3 will take half the time, which is 3 seconds.",
    "explanation_hi": "माना ऊंचाई h है। प्रारंभिक दूरी (x+y): tan(30°) = h/(x+y) => x+y = h√3। बाद की दूरी (y): tan(60°) = h/y => y = h/√3। 6s में तय की गई दूरी = x = h√3 - h/√3 = 2h/√3। चूंकि 2h/√3 दूरी में 6s लगते हैं, h/√3 दूरी में आधा समय लगेगा, जो कि 3 सेकंड है।",
    "explanation_gu": "ધારો કે ઊંચાઈ h છે. પ્રારંભિક અંતર (x+y): tan(30°) = h/(x+y) => x+y = h√3. પછીનું અંતર (y): tan(60°) = h/y => y = h/√3. 6s માં કપાયેલું અંતર = x = h√3 - h/√3 = 2h/√3. કારણ કે 2h/√3 અંતર માટે 6s લાગે છે, h/√3 અંતર માટે અડધો સમય લાગશે, જે 3 સેકન્ડ છે."
})

# Q16
mcqs.append({
    "id": "MATH10_CH09_EX1_Q16",
    "type": "mcq",
    "title": "NCERT Exercise 9.1 - Q16",
    "title_hi": "NCERT प्रश्नावली 9.1 - प्रश्न 16",
    "title_gu": "NCERT સ્વાધ્યાય 9.1 - પ્રશ્ન 16",
    "body": "The angles of elevation of the top of a tower from two points at a distance of 4 m and 9 m from the base of the tower and in the same straight line with it are complementary. What is the height of the tower?",
    "body_hi": "मीनार के आधार से और एक ही सीधी रेखा में 4 मीटर और 9 मीटर की दूरी पर स्थित दो बिंदुओं से मीनार के शिखर के उन्नयन कोण पूरक हैं। मीनार की ऊंचाई क्या है?",
    "body_gu": "ટાવરના પાયાથી અને તેની સાથે એક જ સીધી રેખામાં 4 મીટર અને 9 મીટરના અંતરે આવેલા બે બિંદુઓથી ટાવરની ટોચના ઉત્સેધકોણ કોટિકોણ છે. ટાવરની ઊંચાઈ કેટલી છે?",
    "options": ["6 m", "36 m", "5 m", "7.5 m"],
    "options_hi": ["6 मीटर", "36 मीटर", "5 मीटर", "7.5 मीटर"],
    "options_gu": ["6 મીટર", "36 મીટર", "5 મીટર", "7.5 મીટર"],
    "correct_index": 0,
    "explanation": "Let height be h and angles be θ and 90°-θ. tan(θ) = h/4 and tan(90°-θ) = h/9 => cot(θ) = h/9. Multiplying both equations: tan(θ) * cot(θ) = (h/4) * (h/9) => 1 = h² / 36 => h² = 36 => h = 6 m.",
    "explanation_hi": "माना ऊंचाई h है और कोण θ और 90°-θ हैं। tan(θ) = h/4 और tan(90°-θ) = h/9 => cot(θ) = h/9। दोनों समीकरणों को गुणा करने पर: tan(θ) * cot(θ) = (h/4) * (h/9) => 1 = h² / 36 => h² = 36 => h = 6 मीटर।",
    "explanation_gu": "ધારો કે ઊંચાઈ h છે અને ખૂણા θ અને 90°-θ છે. tan(θ) = h/4 અને tan(90°-θ) = h/9 => cot(θ) = h/9. બંને સમીકરણોનો ગુણાકાર કરતા: tan(θ) * cot(θ) = (h/4) * (h/9) => 1 = h² / 36 => h² = 36 => h = 6 મીટર."
})

# I need 34 more questions to reach 50 MCQs. I'll use variations of the standard concepts.
# Since writing 34 questions manually in script takes a lot of lines, I'll programmatically generate them.

def gen_tower_q(id_num, angle, dist, height, angle_str):
    return {
        "id": f"MATH10_CH09_VAR_{id_num:02d}",
        "type": "mcq",
        "title": f"Practice Question {id_num}",
        "title_hi": f"अभ्यास प्रश्न {id_num}",
        "title_gu": f"પ્રેક્ટિસ પ્રશ્ન {id_num}",
        "body": f"The angle of elevation of the top of a tower from a point on the ground, which is {dist} m away from the foot of the tower, is {angle_str}°. Find the height of the tower.",
        "body_hi": f"जमीन के एक बिंदु से, जो मीनार के पाद-बिंदु से {dist} मीटर की दूरी पर है, मीनार के शिखर का उन्नयन कोण {angle_str}° है। मीनार की ऊंचाई ज्ञात कीजिए।",
        "body_gu": f"જમીન પરના એક બિંદુથી, જે ટાવરના પાયાથી {dist} મીટર દૂર છે, ટાવરની ટોચનો ઉત્સેધકોણ {angle_str}° છે. ટાવરની ઊંચાઈ શોધો.",
        "options": [f"{height} m", f"{dist} m", f"{float(height)*2} m", "None of these"],
        "options_hi": [f"{height} मीटर", f"{dist} मीटर", f"{float(height)*2} मीटर", "इनमें से कोई नहीं"],
        "options_gu": [f"{height} મીટર", f"{dist} મીટર", f"{float(height)*2} મીટર", "આમાંથી કોઈ નહીં"],
        "correct_index": 0,
        "explanation": f"tan({angle_str}°) = height / {dist}. Height = {dist} * tan({angle_str}°).",
        "explanation_hi": f"tan({angle_str}°) = ऊंचाई / {dist}। ऊंचाई = {dist} * tan({angle_str}°)।",
        "explanation_gu": f"tan({angle_str}°) = ઊંચાઈ / {dist}. ઊંચાઈ = {dist} * tan({angle_str}°)."
    }

# We need a variety of questions. Let's create an array of data and then map it.
q_data_1 = [
    (1, "45", 20, "20", "1"),
    (2, "45", 50, "50", "1"),
    (3, "45", 100, "100", "1"),
    (4, "60", 10, "10√3", "√3"),
    (5, "60", 25, "25√3", "√3"),
    (6, "60", 40, "40√3", "√3"),
    (7, "30", 15, "5√3", "1/√3"),
    (8, "30", 60, "20√3", "1/√3"),
    (9, "30", 90, "30√3", "1/√3"),
    (10, "45", 12.5, "12.5", "1")
]

for item in q_data_1:
    mcqs.append(gen_tower_q(item[0], item[1], item[2], item[3], item[1]))

def gen_kite_q(id_num, angle, height, length, angle_str):
    return {
        "id": f"MATH10_CH09_VAR_{id_num:02d}",
        "type": "mcq",
        "title": f"Practice Question {id_num}",
        "title_hi": f"अभ्यास प्रश्न {id_num}",
        "title_gu": f"પ્રેક્ટિસ પ્રશ્ન {id_num}",
        "body": f"A kite is flying at a height of {height} m above the ground. The inclination of the string with the ground is {angle_str}°. Find the length of the string.",
        "body_hi": f"एक पतंग जमीन से {height} मीटर की ऊंचाई पर उड़ रही है। जमीन के साथ डोरी का झुकाव {angle_str}° है। डोरी की लंबाई ज्ञात कीजिए।",
        "body_gu": f"એક પતંગ જમીનથી {height} મીટરની ઊંચાઈ પર ઉડી રહી છે. જમીન સાથે દોરીનો ઝુકાવ {angle_str}° છે. દોરીની લંબાઈ શોધો.",
        "options": [f"{length} m", f"{height} m", f"{float(height)*2} m", "None of these"],
        "options_hi": [f"{length} मीटर", f"{height} मीटर", f"{float(height)*2} मीटर", "इनमें से कोई नहीं"],
        "options_gu": [f"{length} મીટર", f"{height} મીટર", f"{float(height)*2} મીટર", "આમાંથી કોઈ નહીં"],
        "correct_index": 0,
        "explanation": f"sin({angle_str}°) = {height} / length. Length = {height} / sin({angle_str}°).",
        "explanation_hi": f"sin({angle_str}°) = {height} / लंबाई। लंबाई = {height} / sin({angle_str}°)।",
        "explanation_gu": f"sin({angle_str}°) = {height} / લંબાઈ. લંબાઈ = {height} / sin({angle_str}°)."
    }

q_data_2 = [
    (11, "30", 20, "40", "30"),
    (12, "30", 50, "100", "30"),
    (13, "30", 15.5, "31", "30"),
    (14, "45", 10, "10√2", "45"),
    (15, "45", 25, "25√2", "45"),
    (16, "45", 100, "100√2", "45"),
    (17, "60", 30, "20√3", "60"),
    (18, "60", 90, "60√3", "60"),
    (19, "60", 15, "10√3", "60"),
    (20, "30", 5, "10", "30")
]

for item in q_data_2:
    mcqs.append(gen_kite_q(item[0], item[1], item[2], item[3], item[4]))

def gen_shadow_q(id_num, angle, height, shadow, angle_str):
    return {
        "id": f"MATH10_CH09_VAR_{id_num:02d}",
        "type": "mcq",
        "title": f"Practice Question {id_num}",
        "title_hi": f"अभ्यास प्रश्न {id_num}",
        "title_gu": f"પ્રેક્ટિસ પ્રશ્ન {id_num}",
        "body": f"If the height of a vertical pole is {height} m and the length of its shadow on the ground is {shadow} m, then the angle of elevation of the sun is:",
        "body_hi": f"यदि एक ऊर्ध्वाधर खंभे की ऊंचाई {height} मीटर है और जमीन पर इसकी छाया की लंबाई {shadow} मीटर है, तो सूर्य का उन्नयन कोण है:",
        "body_gu": f"જો એક ઊભા થાંભલાની ઊંચાઈ {height} મીટર છે અને જમીન પર તેના પડછાયાની લંબાઈ {shadow} મીટર છે, તો સૂર્યનો ઉત્સેધકોણ છે:",
        "options": [f"{angle_str}°", "30°", "45°", "60°"],
        "options_hi": [f"{angle_str}°", "30°", "45°", "60°"],
        "options_gu": [f"{angle_str}°", "30°", "45°", "60°"],
        "correct_index": 0,
        "explanation": f"tan(θ) = Height / Shadow = {height} / {shadow}. So θ = {angle_str}°.",
        "explanation_hi": f"tan(θ) = ऊंचाई / छाया = {height} / {shadow}। तो θ = {angle_str}°।",
        "explanation_gu": f"tan(θ) = ઊંચાઈ / પડછાયો = {height} / {shadow}. તેથી θ = {angle_str}°."
    }

q_data_3 = [
    (21, "45", "10", "10", "45"),
    (22, "45", "15", "15", "45"),
    (23, "45", "100", "100", "45"),
    (24, "60", "10√3", "10", "60"),
    (25, "60", "15", "5√3", "60"),
    (26, "60", "30", "10√3", "60"),
    (27, "30", "10", "10√3", "30"),
    (28, "30", "15", "15√3", "30"),
    (29, "30", "50", "50√3", "30"),
    (30, "45", "x", "x", "45")
]

for item in q_data_3:
    if item[4] == "45":
        mcqs.append(gen_shadow_q(item[0], item[1], item[2], item[3], "45"))
    elif item[4] == "30":
        mcqs.append(gen_shadow_q(item[0], item[1], item[2], item[3], "30"))
    else:
        mcqs.append(gen_shadow_q(item[0], item[1], item[2], item[3], "60"))

# To ensure exactly 50 total MCQs in the chapter, let's add 4 more generic conceptual MCQs.
# Currently we have 16 NCERT + 30 Gen = 46. Let's add 4 more.
mcqs.append({
    "id": "MATH10_CH09_CONCEPT_01",
    "type": "mcq",
    "title": "Conceptual Understanding",
    "title_hi": "वैचारिक समझ",
    "title_gu": "વૈચારિક સમજ",
    "body": "When we move closer to a tall building, what happens to the angle of elevation of its top?",
    "body_hi": "जब हम किसी ऊंची इमारत के करीब जाते हैं, तो उसके शिखर के उन्नयन कोण का क्या होता है?",
    "body_gu": "જ્યારે આપણે કોઈ ઊંચી ઇમારતની નજીક જઈએ છીએ, ત્યારે તેની ટોચના ઉત્સેધકોણનું શું થાય છે?",
    "options": ["It increases", "It decreases", "It remains the same", "It becomes zero"],
    "options_hi": ["यह बढ़ता है", "यह घटता है", "यह समान रहता है", "यह शून्य हो जाता है"],
    "options_gu": ["તે વધે છે", "તે ઘટે છે", "તે સમાન રહે છે", "તે શૂન્ય થઈ જાય છે"],
    "correct_index": 0,
    "explanation": "As the base distance decreases, the angle must increase to reach the same height.",
    "explanation_hi": "जैसे-जैसे आधार की दूरी कम होती है, समान ऊंचाई तक पहुंचने के लिए कोण बढ़ना चाहिए।",
    "explanation_gu": "જેમ આધારનું અંતર ઘટે છે, સમાન ઊંચાઈ સુધી પહોંચવા માટે ખૂણો વધવો જોઈએ."
})

mcqs.append({
    "id": "MATH10_CH09_CONCEPT_02",
    "type": "mcq",
    "title": "Conceptual Understanding",
    "title_hi": "वैचारिक समझ",
    "title_gu": "વૈચારિક સમજ",
    "body": "The angle of depression is always measured downwards from which line?",
    "body_hi": "अवनमन कोण हमेशा किस रेखा से नीचे की ओर मापा जाता है?",
    "body_gu": "અવસેધકોણ હંમેશા કઈ રેખાથી નીચેની તરફ માપવામાં આવે છે?",
    "options": ["Horizontal line", "Vertical line", "Line of sight", "Perpendicular line"],
    "options_hi": ["क्षैतिज रेखा", "ऊर्ध्वाधर रेखा", "दृष्टि रेखा", "लंब रेखा"],
    "options_gu": ["સમક્ષિતિજ રેખા", "ઊભી રેખા", "દ્રષ્ટિ રેખા", "લંબ રેખા"],
    "correct_index": 0,
    "explanation": "Both angles of elevation and depression are measured from the horizontal line.",
    "explanation_hi": "उन्नयन और अवनमन दोनों कोण क्षैतिज रेखा से मापे जाते हैं।",
    "explanation_gu": "ઉત્સેધકોણ અને અવસેધકોણ બંને સમક્ષિતિજ રેખા પરથી માપવામાં આવે છે."
})

mcqs.append({
    "id": "MATH10_CH09_CONCEPT_03",
    "type": "mcq",
    "title": "Conceptual Understanding",
    "title_hi": "वैचारिक समझ",
    "title_gu": "વૈચારિક સમજ",
    "body": "If the angle of elevation of a tower is 45°, what is the relationship between its height and the distance of the observer from its foot?",
    "body_hi": "यदि किसी मीनार का उन्नयन कोण 45° है, तो उसकी ऊंचाई और उसके पाद से प्रेक्षक की दूरी के बीच क्या संबंध है?",
    "body_gu": "જો કોઈ ટાવરનો ઉત્સેધકોણ 45° હોય, તો તેની ઊંચાઈ અને તેના પાયાથી નિરીક્ષકના અંતર વચ્ચે શું સંબંધ છે?",
    "options": ["They are equal", "Height is twice the distance", "Distance is twice the height", "Cannot be determined"],
    "options_hi": ["वे बराबर हैं", "ऊंचाई दूरी की दोगुनी है", "दूरी ऊंचाई की दोगुनी है", "निर्धारित नहीं किया जा सकता"],
    "options_gu": ["તેઓ સમાન છે", "ઊંચાઈ અંતર કરતા બમણી છે", "અંતર ઊંચાઈ કરતા બમણું છે", "નક્કી કરી શકાતું નથી"],
    "correct_index": 0,
    "explanation": "tan(45°) = 1. Since tan(θ) = Height / Distance, 1 = Height / Distance => Height = Distance.",
    "explanation_hi": "tan(45°) = 1। चूंकि tan(θ) = ऊंचाई / दूरी, 1 = ऊंचाई / दूरी => ऊंचाई = दूरी।",
    "explanation_gu": "tan(45°) = 1. કારણ કે tan(θ) = ઊંચાઈ / અંતર, 1 = ઊંચાઈ / અંતર => ઊંચાઈ = અંતર."
})

mcqs.append({
    "id": "MATH10_CH09_CONCEPT_04",
    "type": "mcq",
    "title": "Conceptual Understanding",
    "title_hi": "वैचारिक समझ",
    "title_gu": "વૈચારિક સમજ",
    "body": "An observer looks at the top of a lighthouse from a boat. If the boat moves away from the lighthouse, the angle of elevation will:",
    "body_hi": "एक प्रेक्षक नाव से लाइटहाउस के शिखर को देखता है। यदि नाव लाइटहाउस से दूर जाती है, तो उन्नयन कोण:",
    "body_gu": "એક નિરીક્ષક હોડીમાંથી લાઇટહાઉસની ટોચને જુએ છે. જો હોડી લાઇટહાઉસથી દૂર જાય છે, તો ઉત્સેધકોણ:",
    "options": ["Decrease", "Increase", "Remain same", "First increase then decrease"],
    "options_hi": ["घटेगा", "बढ़ेगा", "समान रहेगा", "पहले बढ़ेगा फिर घटेगा"],
    "options_gu": ["ઘટશે", "વધશે", "સમાન રહેશે", "પહેલા વધશે પછી ઘટશે"],
    "correct_index": 0,
    "explanation": "As distance increases, you don't have to look up as steeply, so the angle decreases.",
    "explanation_hi": "जैसे-जैसे दूरी बढ़ती है, आपको उतनी तेजी से ऊपर नहीं देखना पड़ता, इसलिए कोण कम हो जाता है।",
    "explanation_gu": "જેમ જેમ અંતર વધે છે, તમારે એટલું તીવ્ર ઉપર જોવું પડતું નથી, તેથી ખૂણો ઘટે છે."
})

# Compile all
blocks.extend(mcqs)

output = {
    "metadata": metadata,
    "blocks": blocks
}

with open('/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_maths_ch9.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"Generated {len(blocks)} blocks successfully, including {len(mcqs)} MCQs.")
