import json
import os

# --- Learn JSON ---
learn_data = {
    "metadata": {
        "id": "gseb_class10_maths_ch12",
        "title": "Chapter 12: Surface Areas and Volumes",
        "subtitle": "Combinations of Solids (NCERT/GSEB)",
        "subject": "Maths",
        "grade": "10",
        "board": "GSEB/CBSE",
        "curriculum": ["Universal"],
        "language": "English/Hindi/Gujarati (Trilingual)",
        "difficulty": "Intermediate",
        "estimated_minutes": 120,
        "version": "1.0.0",
        "author": "Antigravity",
        "reviewed_by": "Chief Academic Architect",
        "tags": ["maths", "surface_area", "volume", "combinations", "solids"],
        "learning_outcomes": [
            "Visualize combinations of basic solids in real life.",
            "Calculate Total Surface Area (TSA) of combined solids.",
            "Calculate Volume of combined solids.",
            "Understand why surface area is not just added, but volume is."
        ],
        "ai_context": {
            "learning_goal": "Help students visualize how complex shapes are made of simple shapes (cones, cylinders, hemispheres) and why surface areas merge differently than volumes.",
            "common_misconceptions": [
                "Adding TSA of two solids to get TSA of the combined solid.",
                "Confusing CSA and TSA when solids are joined."
            ]
        }
    },
    "blocks": [
        {
            "type": "hook",
            "difficulty": "Beginner",
            "bloom": "Understand",
            "id": "CH12_LEARN_B1",
            "body": "Have you ever seen an oil tanker truck on the highway? It looks like a huge cylinder, but the ends are rounded like bowls! Or think of a medicinal capsule. These aren't simple cylinders or spheres. They are **combinations** of solids! Let's discover how to measure them.",
            "body_hi": "क्या आपने कभी हाईवे पर तेल का टैंकर ट्रक देखा है? यह एक विशाल बेलन (सिलेंडर) जैसा दिखता है, लेकिन इसके सिरे कटोरे की तरह गोल होते हैं! या किसी दवा के कैप्सूल के बारे में सोचें। ये साधारण बेलन या गोले नहीं हैं। ये ठोस आकृतियों के **संयोजन** हैं! आइए जानें कि उन्हें कैसे मापा जाए।",
            "body_gu": "શું તમે ક્યારેય હાઇવે પર ઓઇલ ટેન્કર ટ્રક જોઈ છે? તે એક વિશાળ નળાકાર જેવું લાગે છે, પરંતુ છેડા વાટકાની જેમ ગોળ હોય છે! અથવા દવાની કેપ્સ્યુલ વિશે વિચારો. આ માત્ર સાદા નળાકાર અથવા ગોળા નથી. તેઓ ઘન આકારોના **સંયોજનો** છે! ચાલો તેમને કેવી રીતે માપવા તે શોધીએ."
        },
        {
            "type": "theory",
            "difficulty": "Beginner",
            "bloom": "Analyze",
            "id": "CH12_LEARN_B2",
            "title": "Socratic Question",
            "title_hi": "सुकराती प्रश्न",
            "title_gu": "સોક્રેટીક પ્રશ્ન",
            "body": "Imagine you glue a hemisphere (half-sphere) on top of a cylinder to make a toy rocket. If you want to paint the whole rocket, will you paint the flat top of the cylinder? \n\nThink about it! When two shapes join, their connecting faces get hidden. You can't paint them anymore!",
            "body_hi": "कल्पना करें कि आप एक खिलौना रॉकेट बनाने के लिए बेलन (सिलेंडर) के ऊपर एक अर्धगोला चिपकाते हैं। यदि आप पूरे रॉकेट को रंगना चाहते हैं, तो क्या आप बेलन के सपाट शीर्ष को रंगेंगे?\n\nइसके बारे में सोचें! जब दो आकृतियाँ जुड़ती हैं, तो उनके जुड़ने वाले चेहरे छिप जाते हैं। अब आप उन्हें रंग नहीं सकते!",
            "body_gu": "કલ્પના કરો કે તમે રમકડાનું રોકેટ બનાવવા માટે નળાકારની ઉપર અર્ધગોળો ચોંટાડો છો. જો તમે આખા રોકેટને રંગવા માંગતા હો, તો શું તમે નળાકારની સપાટ ટોચને રંગ કરશો?\n\nતેના વિશે વિચારો! જ્યારે બે આકારો જોડાય છે, ત્યારે તેમના જોડાતા ચહેરાઓ છુપાઈ જાય છે. હવે તમે તેમને રંગી શકતા નથી!"
        },
        {
            "type": "theory",
            "difficulty": "Intermediate",
            "bloom": "Remember",
            "id": "CH12_LEARN_B3",
            "title": "The Golden Rule of Surface Area",
            "title_hi": "पृष्ठीय क्षेत्रफल का सुनहरा नियम",
            "title_gu": "પૃષ્ઠફળનો સુવર્ણ નિયમ",
            "body": "**TSA of a Combined Solid ≠ Sum of TSAs of individual solids**\n\nWhen we join two solids, some surface area is hidden. To find the Total Surface Area (TSA) of the new object, we only add the visible outer surfaces. Usually, this means adding the **Curved Surface Areas (CSA)** of the parts.",
            "body_hi": "**संयोजित ठोस का कुल पृष्ठीय क्षेत्रफल ≠ अलग-अलग ठोसों के कुल पृष्ठीय क्षेत्रफलों का योग**\n\nजब हम दो ठोसों को जोड़ते हैं, तो कुछ पृष्ठीय क्षेत्रफल छिप जाता है। नई वस्तु का कुल पृष्ठीय क्षेत्रफल (TSA) ज्ञात करने के लिए, हम केवल दिखाई देने वाली बाहरी सतहों को जोड़ते हैं। आमतौर पर, इसका मतलब है भागों के **वक्र पृष्ठीय क्षेत्रफलों (CSA)** को जोड़ना।",
            "body_gu": "**સંયુક્ત ઘનનું કુલ પૃષ્ઠફળ ≠ અલગ-અલગ ઘનોના કુલ પૃષ્ઠફળોનો સરવાળો**\n\nજ્યારે આપણે બે ઘન આકારોને જોડીએ છીએ, ત્યારે અમુક સપાટી છુપાઈ જાય છે. નવી વસ્તુનું કુલ પૃષ્ઠફળ (TSA) શોધવા માટે, આપણે માત્ર દૃશ્યમાન બહારની સપાટીઓ જ ઉમેરીએ છીએ. સામાન્ય રીતે, આનો અર્થ એ છે કે ભાગોના **વક્ર પૃષ્ઠફળ (CSA)** ઉમેરવા."
        },
        {
            "type": "teacher_tip",
            "difficulty": "Intermediate",
            "bloom": "Understand",
            "id": "CH12_LEARN_B4",
            "body": "💡 **Teacher's Secret:** Whenever a question asks for the 'Surface Area' or 'Total Surface Area' of a combined toy or vessel, don't blindly use the TSA formulas! Ask yourself: 'If I hold this object in my hand, which parts can I actually touch?' Only calculate the area of those touching parts.",
            "body_hi": "💡 **शिक्षक का रहस्य:** जब भी किसी प्रश्न में एक संयुक्त खिलौने या बर्तन का 'पृष्ठीय क्षेत्रफल' या 'कुल पृष्ठीय क्षेत्रफल' पूछा जाए, तो आँख मूँद कर TSA सूत्रों का उपयोग न करें! अपने आप से पूछें: 'यदि मैं इस वस्तु को अपने हाथ में पकड़ूँ, तो मैं वास्तव में किन भागों को छू सकता हूँ?' केवल उन्हीं छूने वाले भागों के क्षेत्रफल की गणना करें।",
            "body_gu": "💡 **શિક્ષકનું રહસ્ય:** જ્યારે પણ પ્રશ્નમાં સંયુક્ત રમકડા અથવા વાસણનું 'પૃષ્ઠફળ' અથવા 'કુલ પૃષ્ઠફળ' પૂછવામાં આવે, ત્યારે આંધળા થઈને TSA સૂત્રોનો ઉપયોગ કરશો નહીં! તમારી જાતને પૂછો: 'જો હું આ વસ્તુને મારા હાથમાં પકડું, તો હું કયા ભાગોને સ્પર્શ કરી શકું છું?' ફક્ત તે જ સ્પર્શતા ભાગોના ક્ષેત્રફળની ગણતરી કરો."
        },
        {
            "id": "CH12_LEARN_B5",
            "type": "quiz",
            "question": "A vessel is in the form of a hollow hemisphere mounted by a hollow cylinder. The diameter of the hemisphere is 14 cm and the total height of the vessel is 13 cm. What is the inner surface area of the vessel? (Take π = 22/7)",
            "question_hi": "एक बर्तन एक खोखले अर्धगोले के आकार का है जिसके ऊपर एक खोखला बेलन अध्यारोपित है। अर्धगोले का व्यास 14 सेमी है और बर्तन की कुल ऊँचाई 13 सेमी है। बर्तन का आंतरिक पृष्ठीय क्षेत्रफल क्या है? (π = 22/7 लें)",
            "question_gu": "એક વાસણ એક પોલા અર્ધગોળાના આકારનું છે જેના પર એક પોલો નળાકાર મૂકવામાં આવ્યો છે. અર્ધગોળાનો વ્યાસ 14 સેમી છે અને વાસણની કુલ ઊંચાઈ 13 સેમી છે. વાસણનું આંતરિક પૃષ્ઠફળ શું છે? (π = 22/7 લો)",
            "options": ["572 cm²", "624 cm²", "462 cm²", "680 cm²"],
            "options_hi": ["572 cm²", "624 cm²", "462 cm²", "680 cm²"],
            "options_gu": ["572 cm²", "624 cm²", "462 cm²", "680 cm²"],
            "correct_index": 0,
            "explanation": "Radius (r) = 14/2 = 7 cm. Height of hemisphere = 7 cm. Height of cylinder (h) = Total height - radius = 13 - 7 = 6 cm. Inner Surface Area = CSA of cylinder + CSA of hemisphere = 2πrh + 2πr² = 2 × 22/7 × 7 × 6 + 2 × 22/7 × 7 × 7 = 264 + 308 = 572 cm².",
            "explanation_hi": "त्रिज्या (r) = 14/2 = 7 सेमी। अर्धगोले की ऊँचाई = 7 सेमी। बेलन की ऊँचाई (h) = कुल ऊँचाई - त्रिज्या = 13 - 7 = 6 सेमी। आंतरिक पृष्ठीय क्षेत्रफल = बेलन का CSA + अर्धगोले का CSA = 2πrh + 2πr² = 2 × 22/7 × 7 × 6 + 2 × 22/7 × 7 × 7 = 264 + 308 = 572 सेमी²।",
            "explanation_gu": "ત્રિજ્યા (r) = 14/2 = 7 સેમી. અર્ધગોળાની ઊંચાઈ = 7 સેમી. નળાકારની ઊંચાઈ (h) = કુલ ઊંચાઈ - ત્રિજ્યા = 13 - 7 = 6 સેમી. આંતરિક પૃષ્ઠફળ = નળાકારનું CSA + અર્ધગોળાનું CSA = 2πrh + 2πr² = 2 × 22/7 × 7 × 6 + 2 × 22/7 × 7 × 7 = 264 + 308 = 572 સેમી²."
        },
        {
            "id": "CH12_LEARN_B6",
            "type": "quiz",
            "question": "A medicine capsule is in the shape of a cylinder with two hemispheres stuck to each of its ends. The length of the entire capsule is 14 mm and the diameter of the capsule is 5 mm. Find its surface area.",
            "question_hi": "एक दवा का कैप्सूल एक बेलन के आकार का है जिसके दोनों सिरों पर दो अर्धगोले चिपके हुए हैं। पूरे कैप्सूल की लंबाई 14 मिमी है और कैप्सूल का व्यास 5 मिमी है। इसका पृष्ठीय क्षेत्रफल ज्ञात कीजिए।",
            "question_gu": "દવાની એક કેપ્સ્યુલ એક નળાકારના આકારની છે જેના બંને છેડે બે અર્ધગોળા ચોંટેલા છે. આખી કેપ્સ્યુલની લંબાઈ 14 મીમી છે અને કેપ્સ્યુલનો વ્યાસ 5 મીમી છે. તેનું પૃષ્ઠફળ શોધો.",
            "options": ["110 mm²", "190 mm²", "220 mm²", "250 mm²"],
            "options_hi": ["110 mm²", "190 mm²", "220 mm²", "250 mm²"],
            "options_gu": ["110 mm²", "190 mm²", "220 mm²", "250 mm²"],
            "correct_index": 2,
            "explanation": "Radius (r) = 5/2 = 2.5 mm. Length of cylindrical part (h) = 14 - (2.5 + 2.5) = 14 - 5 = 9 mm. Surface Area = CSA of cylinder + 2 × CSA of hemisphere = 2πrh + 2 × (2πr²) = 2πr(h + 2r) = 2 × 22/7 × 2.5 × (9 + 5) = 2 × 22/7 × 2.5 × 14 = 220 mm².",
            "explanation_hi": "त्रिज्या (r) = 5/2 = 2.5 मिमी। बेलनाकार भाग की लंबाई (h) = 14 - (2.5 + 2.5) = 14 - 5 = 9 मिमी। पृष्ठीय क्षेत्रफल = बेलन का CSA + 2 × अर्धगोले का CSA = 2πrh + 2 × (2πr²) = 2πr(h + 2r) = 2 × 22/7 × 2.5 × (9 + 5) = 2 × 22/7 × 2.5 × 14 = 220 मिमी²।",
            "explanation_gu": "ત્રિજ્યા (r) = 5/2 = 2.5 મીમી. નળાકાર ભાગની લંબાઈ (h) = 14 - (2.5 + 2.5) = 14 - 5 = 9 મીમી. પૃષ્ઠફળ = નળાકારનું CSA + 2 × અર્ધગોળાનું CSA = 2πrh + 2 × (2πr²) = 2πr(h + 2r) = 2 × 22/7 × 2.5 × (9 + 5) = 2 × 22/7 × 2.5 × 14 = 220 મીમી²."
        },
        {
            "type": "theory",
            "difficulty": "Intermediate",
            "bloom": "Remember",
            "id": "CH12_LEARN_B7",
            "title": "The Rule for Volume",
            "title_hi": "आयतन का नियम",
            "title_gu": "ઘનફળનો નિયમ",
            "body": "While Surface Area behaves differently when shapes are joined, **Volume is very simple!**\n\nThe volume of the solid formed by joining two basic solids will actually be the exact **sum of the volumes** of the constituents.\n\nWhy? Because matter takes up space. If you melt two solids and merge them, the total space (volume) they occupy is just added together.",
            "body_hi": "जबकि आकृतियों को जोड़ने पर पृष्ठीय क्षेत्रफल अलग व्यवहार करता है, **आयतन बहुत सरल है!**\n\nदो मूल ठोसों को जोड़कर बने ठोस का आयतन वास्तव में घटकों के **आयतन का सटीक योग** होगा।\n\nक्यों? क्योंकि पदार्थ स्थान घेरता है। यदि आप दो ठोसों को पिघलाकर मिलाते हैं, तो उनके द्वारा घेरा गया कुल स्थान (आयतन) बस एक साथ जुड़ जाता है।",
            "body_gu": "જ્યારે આકારો જોડાય છે ત્યારે પૃષ્ઠફળ અલગ રીતે વર્તે છે, પરંતુ **ઘનફળ ખૂબ જ સરળ છે!**\n\nબે મૂળ ઘનોને જોડીને બનેલા ઘનનું ઘનફળ ખરેખર ઘટકોના **ઘનફળોનો ચોક્કસ સરવાળો** હશે.\n\nશા માટે? કારણ કે પદાર્થ જગ્યા રોકે છે. જો તમે બે ઘન આકારોને ઓગાળીને ભેગા કરો છો, તો તેઓ દ્વારા રોકાયેલી કુલ જગ્યા (ઘનફળ) ખાલી ઉમેરવામાં આવે છે."
        },
        {
            "id": "CH12_LEARN_B8",
            "type": "quiz",
            "question": "A solid is in the shape of a cone standing on a hemisphere with both their radii being equal to 1 cm and the height of the cone is equal to its radius. Find the volume of the solid in terms of π.",
            "question_hi": "एक ठोस एक अर्धगोले पर खड़े शंकु के आकार का है, जिसकी दोनों त्रिज्याएं 1 सेमी के बराबर हैं और शंकु की ऊँचाई उसकी त्रिज्या के बराबर है। π के पदों में ठोस का आयतन ज्ञात कीजिए।",
            "question_gu": "એક ઘન અર્ધગોળા પર ઊભેલા શંકુના આકારનો છે, જેમની બંને ત્રિજ્યા 1 સેમી સમાન છે અને શંકુની ઊંચાઈ તેની ત્રિજ્યા જેટલી છે. π ના સંદર્ભમાં ઘનનું ઘનફળ શોધો.",
            "options": ["π cm³", "2π cm³", "3π cm³", "π/3 cm³"],
            "options_hi": ["π cm³", "2π cm³", "3π cm³", "π/3 cm³"],
            "options_gu": ["π cm³", "2π cm³", "3π cm³", "π/3 cm³"],
            "correct_index": 0,
            "explanation": "Radius (r) = 1 cm, Height of cone (h) = 1 cm. Volume of solid = Volume of cone + Volume of hemisphere = (1/3)πr²h + (2/3)πr³ = (1/3)π(1)²(1) + (2/3)π(1)³ = π/3 + 2π/3 = 3π/3 = π cm³.",
            "explanation_hi": "त्रिज्या (r) = 1 सेमी, शंकु की ऊँचाई (h) = 1 सेमी। ठोस का आयतन = शंकु का आयतन + अर्धगोले का आयतन = (1/3)πr²h + (2/3)πr³ = (1/3)π(1)²(1) + (2/3)π(1)³ = π/3 + 2π/3 = 3π/3 = π सेमी³।",
            "explanation_gu": "ત્રિજ્યા (r) = 1 સેમી, શંકુની ઊંચાઈ (h) = 1 સેમી. ઘનનું ઘનફળ = શંકુનું ઘનફળ + અર્ધગોળાનું ઘનફળ = (1/3)πr²h + (2/3)πr³ = (1/3)π(1)²(1) + (2/3)π(1)³ = π/3 + 2π/3 = 3π/3 = π સેમી³."
        },
        {
            "id": "CH12_LEARN_B9",
            "type": "quiz",
            "question": "A juice seller has a cylindrical glass of inner diameter 5 cm and height 10 cm, but the bottom has a hemispherical raised portion. (Use π = 3.14). Which of the following is true?",
            "question_hi": "एक जूस विक्रेता के पास 5 सेमी आंतरिक व्यास और 10 सेमी ऊँचाई का एक बेलनाकार गिलास है, लेकिन नीचे की ओर एक अर्धगोलाकार उभरा हुआ भाग है। (π = 3.14 का उपयोग करें)। निम्नलिखित में से कौन सा सत्य है?",
            "question_gu": "જ્યુસ વેચનાર પાસે 5 સેમી આંતરિક વ્યાસ અને 10 સેમી ઊંચાઈ ધરાવતો નળાકાર ગ્લાસ છે, પરંતુ નીચેના ભાગમાં અર્ધગોળાકાર ઊભરેલો ભાગ છે. (π = 3.14 નો ઉપયોગ કરો). નીચેનામાંથી કયું સાચું છે?",
            "options": [
                "Actual capacity = 196.25 cm³",
                "Actual capacity is less than apparent capacity by 32.71 cm³",
                "Actual capacity is greater than apparent capacity",
                "Apparent capacity = 163.54 cm³"
            ],
            "options_hi": [
                "वास्तविक क्षमता = 196.25 सेमी³",
                "वास्तविक क्षमता आभासी क्षमता से 32.71 सेमी³ कम है",
                "वास्तविक क्षमता आभासी क्षमता से अधिक है",
                "आभासी क्षमता = 163.54 सेमी³"
            ],
            "options_gu": [
                "વાસ્તવિક ક્ષમતા = 196.25 સેમી³",
                "વાસ્તવિક ક્ષમતા દેખીતી ક્ષમતા કરતાં 32.71 સેમી³ ઓછી છે",
                "વાસ્તવિક ક્ષમતા દેખીતી ક્ષમતા કરતાં વધુ છે",
                "દેખીતી ક્ષમતા = 163.54 સેમી³"
            ],
            "correct_index": 1,
            "explanation": "Apparent capacity = Volume of cylinder = πr²h = 3.14 × 2.5 × 2.5 × 10 = 196.25 cm³. The raised hemisphere reduces space. Volume of hemisphere = (2/3)πr³ = (2/3) × 3.14 × 2.5³ = 32.71 cm³. Actual capacity = 196.25 - 32.71 = 163.54 cm³. Thus, it is less by 32.71 cm³.",
            "explanation_hi": "आभासी क्षमता = बेलन का आयतन = πr²h = 3.14 × 2.5 × 2.5 × 10 = 196.25 सेमी³। उभरा हुआ अर्धगोला स्थान कम करता है। अर्धगोले का आयतन = (2/3)πr³ = (2/3) × 3.14 × 2.5³ = 32.71 सेमी³। वास्तविक क्षमता = 196.25 - 32.71 = 163.54 सेमी³। इस प्रकार, यह 32.71 सेमी³ कम है।",
            "explanation_gu": "દેખીતી ક્ષમતા = નળાકારનું ઘનફળ = πr²h = 3.14 × 2.5 × 2.5 × 10 = 196.25 સેમી³. ઊભરેલો અર્ધગોળો જગ્યા ઘટાડે છે. અર્ધગોળાનું ઘનફળ = (2/3)πr³ = (2/3) × 3.14 × 2.5³ = 32.71 સેમી³. વાસ્તવિક ક્ષમતા = 196.25 - 32.71 = 163.54 સેમી³. આમ, તે 32.71 સેમી³ ઓછી છે."
        }
    ]
}

# --- Practice JSON ---
practice_data = {
    "metadata": {
        "id": "NCERT_MATH_10_CH12_PRACTICE",
        "title": "Chapter 12: Surface Areas and Volumes (Mock Test)",
        "subtitle": "Test Your Mastery",
        "subject": "Maths",
        "grade": "10",
        "board": "GSEB",
        "curriculum": ["Universal", "CBSE", "GSEB"],
        "language": "English/Hindi/Gujarati (Trilingual)",
        "difficulty": "Intermediate",
        "estimated_minutes": 60,
        "version": "1.0.0",
        "author": "Antigravity",
        "reviewed_by": "Chief Academic Architect",
        "tags": ["maths", "surface area", "volume", "mock test", "practice", "trilingual"],
        "learning_outcomes": [
            "Calculate combined surface areas correctly.",
            "Solve complex volume problems.",
            "Determine the remaining volume or surface area after hollowed parts."
        ],
        "ai_context": {
            "learning_goal": "Assess the student's mastery of Chapter 12 through remaining NCERT exercise questions.",
            "common_misconceptions": []
        }
    },
    "blocks": [
        {
            "id": "CH12_PRACTICE_Q1",
            "type": "quiz",
            "question": "2 cubes each of volume 64 cm³ are joined end to end. Find the surface area of the resulting cuboid.",
            "question_hi": "प्रत्येक 64 सेमी³ आयतन वाले 2 घनों को सिरे से सिरे तक जोड़ा जाता है। परिणामी घनाभ का पृष्ठीय क्षेत्रफल ज्ञात कीजिए।",
            "question_gu": "દરેક 64 સેમી³ ઘનફળ ધરાવતા 2 સમઘનને છેડાથી છેડા સુધી જોડવામાં આવે છે. પરિણામી લંબઘનનું પૃષ્ઠફળ શોધો.",
            "options": ["160 cm²", "128 cm²", "144 cm²", "192 cm²"],
            "options_hi": ["160 cm²", "128 cm²", "144 cm²", "192 cm²"],
            "options_gu": ["160 cm²", "128 cm²", "144 cm²", "192 cm²"],
            "correct_index": 0,
            "explanation": "Volume of a cube = a³ = 64 => a = 4 cm. Joining two such cubes forms a cuboid of dimensions: Length = 4+4 = 8 cm, Breadth = 4 cm, Height = 4 cm. Surface Area = 2(lb + bh + hl) = 2(8×4 + 4×4 + 4×8) = 2(32 + 16 + 32) = 2(80) = 160 cm².",
            "explanation_hi": "घन का आयतन = a³ = 64 => a = 4 सेमी। ऐसे दो घनों को जोड़ने पर विमाओं वाला एक घनाभ बनता है: लंबाई = 4+4 = 8 सेमी, चौड़ाई = 4 सेमी, ऊँचाई = 4 सेमी। पृष्ठीय क्षेत्रफल = 2(lb + bh + hl) = 2(8×4 + 4×4 + 4×8) = 2(32 + 16 + 32) = 2(80) = 160 सेमी²।",
            "explanation_gu": "સમઘનનું ઘનફળ = a³ = 64 => a = 4 સેમી. આવા બે સમઘનને જોડવાથી લંબઘન બને છે જેનું માપ: લંબાઈ = 4+4 = 8 સેમી, પહોળાઈ = 4 સેમી, ઊંચાઈ = 4 સેમી. પૃષ્ઠફળ = 2(lb + bh + hl) = 2(8×4 + 4×4 + 4×8) = 2(32 + 16 + 32) = 2(80) = 160 સેમી²."
        },
        {
            "id": "CH12_PRACTICE_Q2",
            "type": "quiz",
            "question": "A toy is in the form of a cone of radius 3.5 cm mounted on a hemisphere of same radius. The total height of the toy is 15.5 cm. Find the total surface area of the toy. (π = 22/7)",
            "question_hi": "एक खिलौना समान त्रिज्या वाले अर्धगोले पर अध्यारोपित 3.5 सेमी त्रिज्या वाले शंकु के आकार का है। खिलौने की कुल ऊँचाई 15.5 सेमी है। खिलौने का कुल पृष्ठीय क्षेत्रफल ज्ञात कीजिए। (π = 22/7)",
            "question_gu": "એક રમકડું સમાન ત્રિજ્યાવાળા અર્ધગોળા પર મૂકવામાં આવેલા 3.5 સેમી ત્રિજ્યાવાળા શંકુના આકારનું છે. રમકડાની કુલ ઊંચાઈ 15.5 સેમી છે. રમકડાનું કુલ પૃષ્ઠફળ શોધો. (π = 22/7)",
            "options": ["214.5 cm²", "234.5 cm²", "275 cm²", "190 cm²"],
            "options_hi": ["214.5 cm²", "234.5 cm²", "275 cm²", "190 cm²"],
            "options_gu": ["214.5 cm²", "234.5 cm²", "275 cm²", "190 cm²"],
            "correct_index": 0,
            "explanation": "Radius = 3.5 cm. Height of cone = Total height - radius of hemisphere = 15.5 - 3.5 = 12 cm. Slant height (l) = √(12² + 3.5²) = √(144 + 12.25) = √156.25 = 12.5 cm. Total Surface Area = CSA of cone + CSA of hemisphere = πrl + 2πr² = (22/7 × 3.5 × 12.5) + (2 × 22/7 × 3.5²) = 137.5 + 77 = 214.5 cm².",
            "explanation_hi": "त्रिज्या = 3.5 सेमी। शंकु की ऊँचाई = कुल ऊँचाई - अर्धगोले की त्रिज्या = 15.5 - 3.5 = 12 सेमी। तिर्यक ऊँचाई (l) = √(12² + 3.5²) = √(144 + 12.25) = √156.25 = 12.5 सेमी। कुल पृष्ठीय क्षेत्रफल = शंकु का CSA + अर्धगोले का CSA = πrl + 2πr² = (22/7 × 3.5 × 12.5) + (2 × 22/7 × 3.5²) = 137.5 + 77 = 214.5 सेमी²।",
            "explanation_gu": "ત્રિજ્યા = 3.5 સેમી. શંકુની ઊંચાઈ = કુલ ઊંચાઈ - અર્ધગોળાની ત્રિજ્યા = 15.5 - 3.5 = 12 સેમી. ત્રાંસી ઊંચાઈ (l) = √(12² + 3.5²) = √(144 + 12.25) = √156.25 = 12.5 સેમી. કુલ પૃષ્ઠફળ = શંકુનું CSA + અર્ધગોળાનું CSA = πrl + 2πr² = (22/7 × 3.5 × 12.5) + (2 × 22/7 × 3.5²) = 137.5 + 77 = 214.5 સેમી²."
        },
        {
            "id": "CH12_PRACTICE_Q3",
            "type": "quiz",
            "question": "A cubical block of side 7 cm is surmounted by a hemisphere. What is the greatest diameter the hemisphere can have? Find the surface area of the solid.",
            "question_hi": "7 सेमी भुजा वाले एक घनाकार ब्लॉक के ऊपर एक अर्धगोला रखा गया है। अर्धगोले का अधिकतम व्यास क्या हो सकता है? ठोस का पृष्ठीय क्षेत्रफल ज्ञात कीजिए।",
            "question_gu": "7 સેમી બાજુવાળા એક સમઘન બ્લોકની ઉપર એક અર્ધગોળો મૂકવામાં આવ્યો છે. અર્ધગોળાનો મહત્તમ વ્યાસ કેટલો હોઈ શકે? ઘનનું પૃષ્ઠફળ શોધો.",
            "options": ["7 cm, 332.5 cm²", "7 cm, 385 cm²", "3.5 cm, 294 cm²", "14 cm, 332.5 cm²"],
            "options_hi": ["7 सेमी, 332.5 सेमी²", "7 सेमी, 385 सेमी²", "3.5 सेमी, 294 सेमी²", "14 सेमी, 332.5 सेमी²"],
            "options_gu": ["7 સેમી, 332.5 સેમી²", "7 સેમી, 385 સેમી²", "3.5 સેમી, 294 સેમી²", "14 સેમી, 332.5 સેમી²"],
            "correct_index": 0,
            "explanation": "Greatest diameter of hemisphere = side of cube = 7 cm (so radius r = 3.5 cm). Surface Area = TSA of cube + CSA of hemisphere - Base area of hemisphere = 6a² + 2πr² - πr² = 6a² + πr² = 6(7²) + (22/7 × 3.5 × 3.5) = 294 + 38.5 = 332.5 cm².",
            "explanation_hi": "अर्धगोले का अधिकतम व्यास = घन की भुजा = 7 सेमी (अतः त्रिज्या r = 3.5 सेमी)। पृष्ठीय क्षेत्रफल = घन का TSA + अर्धगोले का CSA - अर्धगोले के आधार का क्षेत्रफल = 6a² + 2πr² - πr² = 6a² + πr² = 6(7²) + (22/7 × 3.5 × 3.5) = 294 + 38.5 = 332.5 सेमी²।",
            "explanation_gu": "અર્ધગોળાનો મહત્તમ વ્યાસ = સમઘનની બાજુ = 7 સેમી (તેથી ત્રિજ્યા r = 3.5 સેમી). પૃષ્ઠફળ = સમઘનનું TSA + અર્ધગોળાનું CSA - અર્ધગોળાના આધારનું ક્ષેત્રફળ = 6a² + 2πr² - πr² = 6a² + πr² = 6(7²) + (22/7 × 3.5 × 3.5) = 294 + 38.5 = 332.5 સેમી²."
        },
        {
            "id": "CH12_PRACTICE_Q4",
            "type": "quiz",
            "question": "A hemispherical depression is cut out from one face of a cubical wooden block such that the diameter 'l' of the hemisphere is equal to the edge of the cube. Determine the surface area of the remaining solid.",
            "question_hi": "एक घनाकार लकड़ी के ब्लॉक के एक फलक से एक अर्धगोलाकार गड्ढा इस प्रकार काटा जाता है कि अर्धगोले का व्यास 'l' घन के किनारे के बराबर है। शेष ठोस का पृष्ठीय क्षेत्रफल ज्ञात कीजिए।",
            "question_gu": "લાકડાના સમઘન બ્લોકના એક ચહેરા પરથી એક અર્ધગોળાકાર ખાડો એ રીતે કાપવામાં આવે છે કે અર્ધગોળાનો વ્યાસ 'l' સમઘનની બાજુ જેટલો હોય. બાકીના ઘનનું પૃષ્ઠફળ શોધો.",
            "options": ["(l²/4)(24 + π)", "(l²/4)(24 - π)", "6l² - πl²/4", "(l²/2)(12 + π)"],
            "options_hi": ["(l²/4)(24 + π)", "(l²/4)(24 - π)", "6l² - πl²/4", "(l²/2)(12 + π)"],
            "options_gu": ["(l²/4)(24 + π)", "(l²/4)(24 - π)", "6l² - πl²/4", "(l²/2)(12 + π)"],
            "correct_index": 0,
            "explanation": "Edge of cube = diameter = l. Radius = l/2. Surface Area = TSA of cube - Area of circle + CSA of hemisphere = 6l² - πr² + 2πr² = 6l² + πr² = 6l² + π(l/2)² = 6l² + (πl²/4). Taking l²/4 common: (l²/4)(24 + π).",
            "explanation_hi": "घन का किनारा = व्यास = l। त्रिज्या = l/2। पृष्ठीय क्षेत्रफल = घन का TSA - वृत्त का क्षेत्रफल + अर्धगोले का CSA = 6l² - πr² + 2πr² = 6l² + πr² = 6l² + π(l/2)² = 6l² + (πl²/4)। l²/4 सामान्य लेने पर: (l²/4)(24 + π)।",
            "explanation_gu": "સમઘનની બાજુ = વ્યાસ = l. ત્રિજ્યા = l/2. પૃષ્ઠફળ = સમઘનનું TSA - વર્તુળનું ક્ષેત્રફળ + અર્ધગોળાનું CSA = 6l² - πr² + 2πr² = 6l² + πr² = 6l² + π(l/2)² = 6l² + (πl²/4). l²/4 સામાન્ય લેતા: (l²/4)(24 + π)."
        },
        {
            "id": "CH12_PRACTICE_Q5",
            "type": "quiz",
            "question": "Rachel was asked to make a model shaped like a cylinder with two cones attached at its ends. Diameter is 3 cm, total length is 12 cm, and height of each cone is 2 cm. Find the volume of air contained in the model. (π = 22/7)",
            "question_hi": "राहेल को एक बेलन के आकार का एक मॉडल बनाने के लिए कहा गया था जिसके दोनों सिरों पर दो शंकु जुड़े हुए हैं। व्यास 3 सेमी है, कुल लंबाई 12 सेमी है, और प्रत्येक शंकु की ऊँचाई 2 सेमी है। मॉडल में मौजूद हवा का आयतन ज्ञात कीजिए। (π = 22/7)",
            "question_gu": "રશેલને એક નળાકાર આકારનું મોડેલ બનાવવા માટે કહેવામાં આવ્યું હતું જેના બંને છેડે બે શંકુ જોડાયેલા હોય. વ્યાસ 3 સેમી છે, કુલ લંબાઈ 12 સેમી છે, અને દરેક શંકુની ઊંચાઈ 2 સેમી છે. મોડેલમાં રહેલી હવાનું ઘનફળ શોધો. (π = 22/7)",
            "options": ["66 cm³", "75 cm³", "55 cm³", "84 cm³"],
            "options_hi": ["66 cm³", "75 cm³", "55 cm³", "84 cm³"],
            "options_gu": ["66 cm³", "75 cm³", "55 cm³", "84 cm³"],
            "correct_index": 0,
            "explanation": "Radius = 1.5 cm. Height of each cone = 2 cm. Height of cylinder = 12 - (2 + 2) = 8 cm. Total Volume = Volume of cylinder + 2 × Volume of cone = πr²h_cyl + 2(1/3 πr²h_cone) = πr² (8 + 2/3 × 2) = π(1.5)²(8 + 4/3) = (22/7) × 2.25 × (28/3) = 22 × 2.25 × 4/3 = 22 × 0.75 × 4 = 22 × 3 = 66 cm³.",
            "explanation_hi": "त्रिज्या = 1.5 सेमी। प्रत्येक शंकु की ऊँचाई = 2 सेमी। बेलन की ऊँचाई = 12 - (2 + 2) = 8 सेमी। कुल आयतन = बेलन का आयतन + 2 × शंकु का आयतन = πr²h_cyl + 2(1/3 πr²h_cone) = πr² (8 + 2/3 × 2) = π(1.5)²(8 + 4/3) = (22/7) × 2.25 × (28/3) = 22 × 2.25 × 4/3 = 22 × 0.75 × 4 = 22 × 3 = 66 सेमी³।",
            "explanation_gu": "ત્રિજ્યા = 1.5 સેમી. દરેક શંકુની ઊંચાઈ = 2 સેમી. નળાકારની ઊંચાઈ = 12 - (2 + 2) = 8 સેમી. કુલ ઘનફળ = નળાકારનું ઘનફળ + 2 × શંકુનું ઘનફળ = πr²h_cyl + 2(1/3 πr²h_cone) = πr² (8 + 2/3 × 2) = π(1.5)²(8 + 4/3) = (22/7) × 2.25 × (28/3) = 22 × 2.25 × 4/3 = 22 × 0.75 × 4 = 22 × 3 = 66 સેમી³."
        },
        {
            "id": "CH12_PRACTICE_Q6",
            "type": "quiz",
            "question": "A gulab jamun contains sugar syrup up to about 30% of its volume. Find approximately how much syrup would be found in 45 gulab jamuns, each shaped like a cylinder with two hemispherical ends with length 5 cm and diameter 2.8 cm.",
            "question_hi": "एक गुलाब जामुन में उसके आयतन का लगभग 30% चीनी की चाशनी होती है। 45 गुलाब जामुनों में लगभग कितनी चाशनी होगी, जिनमें से प्रत्येक एक बेलन के आकार का है जिसके दोनों सिरे अर्धगोलाकार हैं और जिसकी लंबाई 5 सेमी और व्यास 2.8 सेमी है।",
            "question_gu": "ગુલાબ જાંબુમાં તેના ઘનફળના આશરે 30% ખાંડની ચાસણી હોય છે. 45 ગુલાબ જાંબુમાં આશરે કેટલી ચાસણી હશે, જે દરેક એક નળાકાર આકારનું છે જેના બંને છેડા અર્ધગોળાકાર છે અને જેની લંબાઈ 5 સેમી અને વ્યાસ 2.8 સેમી છે.",
            "options": ["338 cm³", "345 cm³", "312 cm³", "380 cm³"],
            "options_hi": ["338 cm³", "345 cm³", "312 cm³", "380 cm³"],
            "options_gu": ["338 cm³", "345 cm³", "312 cm³", "380 cm³"],
            "correct_index": 0,
            "explanation": "Radius = 1.4 cm. Cylinder length = 5 - (1.4+1.4) = 2.2 cm. Volume of 1 gulab jamun = πr²h + (4/3)πr³ = πr²(h + 4/3 r) = (22/7)(1.4²)(2.2 + 4/3(1.4)) ≈ 25.05 cm³. Volume of 45 gulab jamuns = 45 × 25.05 = 1127.25 cm³. Syrup = 30% of 1127.25 ≈ 338 cm³.",
            "explanation_hi": "त्रिज्या = 1.4 सेमी। बेलन की लंबाई = 5 - (1.4+1.4) = 2.2 सेमी। 1 गुलाब जामुन का आयतन = πr²h + (4/3)πr³ = πr²(h + 4/3 r) = (22/7)(1.4²)(2.2 + 4/3(1.4)) ≈ 25.05 सेमी³। 45 गुलाब जामुन का आयतन = 45 × 25.05 = 1127.25 सेमी³। चाशनी = 1127.25 का 30% ≈ 338 सेमी³।",
            "explanation_gu": "ત્રિજ્યા = 1.4 સેમી. નળાકારની લંબાઈ = 5 - (1.4+1.4) = 2.2 સેમી. 1 ગુલાબ જાંબુનું ઘનફળ = πr²h + (4/3)πr³ = πr²(h + 4/3 r) = (22/7)(1.4²)(2.2 + 4/3(1.4)) ≈ 25.05 સેમી³. 45 ગુલાબ જાંબુનું ઘનફળ = 45 × 25.05 = 1127.25 સેમી³. ચાસણી = 1127.25 ના 30% ≈ 338 સેમી³."
        },
        {
            "id": "CH12_PRACTICE_Q7",
            "type": "quiz",
            "question": "A pen stand is a cuboid with four conical depressions. Cuboid is 15 cm x 10 cm x 3.5 cm. Radius of depression is 0.5 cm, depth is 1.4 cm. Find volume of wood.",
            "question_hi": "एक पेन स्टैंड एक घनाभ है जिसमें चार शंक्वाकार गड्ढे हैं। घनाभ 15 सेमी x 10 सेमी x 3.5 सेमी है। गड्ढे की त्रिज्या 0.5 सेमी, गहराई 1.4 सेमी है। लकड़ी का आयतन ज्ञात कीजिए।",
            "question_gu": "પેન સ્ટેન્ડ એક લંબઘન છે જેમાં ચાર શંકુ આકારના ખાડા છે. લંબઘન 15 સેમી x 10 સેમી x 3.5 સેમી છે. ખાડાની ત્રિજ્યા 0.5 સેમી, ઊંડાઈ 1.4 સેમી છે. લાકડાનું ઘનફળ શોધો.",
            "options": ["523.53 cm³", "525 cm³", "520.44 cm³", "521.8 cm³"],
            "options_hi": ["523.53 cm³", "525 cm³", "520.44 cm³", "521.8 cm³"],
            "options_gu": ["523.53 cm³", "525 cm³", "520.44 cm³", "521.8 cm³"],
            "correct_index": 0,
            "explanation": "Vol of cuboid = 15 × 10 × 3.5 = 525 cm³. Vol of 4 cones = 4 × (1/3 πr²h) = 4/3 × 22/7 × (0.5)² × 1.4 = 4/3 × 22/7 × 0.25 × 1.4 = 4/3 × 0.11 = 1.466 cm³. Vol of wood = 525 - 1.466 = 523.53 cm³.",
            "explanation_hi": "घनाभ का आयतन = 15 × 10 × 3.5 = 525 सेमी³। 4 शंकुओं का आयतन = 4 × (1/3 πr²h) = 4/3 × 22/7 × (0.5)² × 1.4 = 4/3 × 22/7 × 0.25 × 1.4 = 4/3 × 0.11 = 1.466 सेमी³। लकड़ी का आयतन = 525 - 1.466 = 523.53 सेमी³।",
            "explanation_gu": "લંબઘનનું ઘનફળ = 15 × 10 × 3.5 = 525 સેમી³. 4 શંકુનું ઘનફળ = 4 × (1/3 πr²h) = 4/3 × 22/7 × (0.5)² × 1.4 = 4/3 × 22/7 × 0.25 × 1.4 = 4/3 × 0.11 = 1.466 સેમી³. લાકડાનું ઘનફળ = 525 - 1.466 = 523.53 સેમી³."
        }
    ]
}

# Write files
with open("/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_maths_ch12.json", "w") as f:
    json.dump(learn_data, f, indent=2, ensure_ascii=False)

with open("/home/ubuntu/Shine_Academy_Naroda/app_core/assessment/gseb_class10_maths_ch12_questions.json", "w") as f:
    json.dump(practice_data, f, indent=2, ensure_ascii=False)

print("Files created successfully.")
