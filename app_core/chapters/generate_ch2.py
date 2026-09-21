import json

data = {
    "id": "ECO_12_CH2",
    "title": "Indicators of Growth and Development",
    "subtitle": "Chapter 2",
    "subject": "Economics",
    "grade": "12",
    "board": "GSEB",
    "curriculum": ["GSEB"],
    "language": "English",
    "difficulty": "Intermediate",
    "estimated_minutes": 120,
    "version": "1.0",
    "author": "Antigravity",
    "reviewed_by": "System",
    "last_updated": "2026-09-15T00:00:00Z",
    "tags": ["Economics", "Growth", "Development", "HDI", "PQLI"],
    "learning_outcomes": ["Understand the difference between growth and development", "Learn about HDI and PQLI"],
    "ai_context": {
        "learning_goal": "Understand indicators of economic growth and development.",
        "common_misconceptions": ["Growth and development are the same."],
        "tutor_hint": "Ask the student how their standard of living has changed over the years.",
        "next_topics": ["KOBJ_ECO_CH3"]
    },
    "blocks": []
}

# 8-step Socratic Discovery Arc
blocks = [
    {
        "id": "KOBJ_12_ECO_CH2_HOOK_1",
        "type": "theory",
        "difficulty": "Beginner",
        "estimated_minutes": 5,
        "bloom": "Understand",
        "title": "The Mystery of Progress",
        "title_hi": "प्रगति का रहस्य",
        "title_gu": "પ્રગતિનું રહસ્ય",
        "body": "Have you ever wondered why some countries have tall buildings but poor citizens, while others have small homes but happy, healthy people? What makes a country truly developed?",
        "body_hi": "क्या आपने कभी सोचा है कि कुछ देशों में ऊँची इमारतें होती हैं लेकिन नागरिक गरीब होते हैं, जबकि अन्य में छोटे घर होते हैं लेकिन खुश, स्वस्थ लोग होते हैं? किसी देश को वास्तव में विकसित क्या बनाता है?",
        "body_gu": "શું તમે ક્યારેય વિચાર્યું છે કે શા માટે કેટલાક દેશોમાં ઊંચી ઇમારતો હોય છે પરંતુ ગરીબ નાગરિકો હોય છે, જ્યારે અન્ય દેશોમાં નાના ઘરો હોય છે પરંતુ ખુશ, સ્વસ્થ લોકો હોય છે? દેશને ખરેખર વિકસિત શું બનાવે છે?"
    },
    {
        "id": "KOBJ_12_ECO_CH2_SOCRATIC_1",
        "type": "theory",
        "difficulty": "Beginner",
        "estimated_minutes": 5,
        "bloom": "Analyze",
        "title": "Think and Predict",
        "title_hi": "सोचें और भविष्यवाणी करें",
        "title_gu": "વિચારો અને આગાહી કરો",
        "body": "If you give someone ₹10,00,000, but they live in a place with no hospitals, no schools, and bad air, are they truly 'developed'? Why or why not?",
        "body_hi": "यदि आप किसी को ₹10,00,000 देते हैं, लेकिन वे ऐसी जगह रहते हैं जहाँ कोई अस्पताल नहीं है, कोई स्कूल नहीं है, और हवा खराब है, तो क्या वे वास्तव में 'विकसित' हैं? क्यों या क्यों नहीं?",
        "body_gu": "જો તમે કોઈને ₹10,00,000 આપો છો, પરંતુ તેઓ એવી જગ્યાએ રહે છે જ્યાં કોઈ હોસ્પિટલ નથી, શાળા નથી અને હવા ખરાબ છે, તો શું તેઓ ખરેખર 'વિકસિત' છે? શા માટે અથવા શા માટે નહીં?"
    },
    {
        "id": "KOBJ_12_ECO_CH2_EXPLORE_1",
        "type": "theory",
        "difficulty": "Beginner",
        "estimated_minutes": 5,
        "bloom": "Understand",
        "title": "The Quality of Life",
        "title_hi": "जीवन की गुणवत्ता",
        "title_gu": "જીવનની ગુણવત્તા",
        "body": "Imagine two villages. Village A has a lot of money from selling crops. Village B has less money, but they built a school, a well for clean water, and a hospital. Village A only grew in money, but Village B developed its society.",
        "body_hi": "दो गाँवों की कल्पना करें। गाँव ए के पास फसल बेचने से बहुत पैसा है। गाँव बी के पास कम पैसा है, लेकिन उन्होंने एक स्कूल, साफ पानी के लिए एक कुआँ और एक अस्पताल बनाया। गाँव ए केवल पैसे में बढ़ा, लेकिन गाँव बी ने अपने समाज का विकास किया।",
        "body_gu": "બે ગામોની કલ્પના કરો. ગામ A પાસે પાક વેચવા પરથી ઘણો પૈસો છે. ગામ B પાસે ઓછો પૈસો છે, પરંતુ તેમણે શાળા, શુદ્ધ પાણી માટે કૂવો અને હોસ્પિટલ બનાવી છે. ગામ A માત્ર પૈસામાં આગળ વધ્યું, પરંતુ ગામ B એ તેના સમાજનો વિકાસ કર્યો."
    },
    {
        "id": "KOBJ_12_ECO_CH2_REVEAL_1",
        "type": "definition",
        "difficulty": "Beginner",
        "estimated_minutes": 5,
        "bloom": "Remember",
        "title": "Economic Growth vs Economic Development",
        "title_hi": "आर्थिक वृद्धि बनाम आर्थिक विकास",
        "title_gu": "આર્થિક વૃદ્ધિ વિરુદ્ધ આર્થિક વિકાસ",
        "body": "Economic Growth (आर्थिक वृद्धि) is just a quantitative increase in the real national income and per capita income. Economic Development (आर्थिक विकास) is a multi-dimensional process involving qualitative changes along with growth, improving the standard of living.",
        "body_hi": "आर्थिक वृद्धि (Economic Growth) केवल वास्तविक राष्ट्रीय आय और प्रति व्यक्ति आय में मात्रात्मक वृद्धि है। आर्थिक विकास (Economic Development) एक बहु-आयामी प्रक्रिया है जिसमें वृद्धि के साथ-साथ गुणात्मक परिवर्तन शामिल हैं, जो जीवन स्तर में सुधार करते हैं।",
        "body_gu": "આર્થિક વૃદ્ધિ (Economic Growth) એ માત્ર વાસ્તવિક રાષ્ટ્રીય આવક અને માથાદીઠ આવકમાં માત્રાત્મક વધારો છે. આર્થિક વિકાસ (Economic Development) એ બહુ-પરિમાણીય પ્રક્રિયા છે જેમાં વૃદ્ધિ સાથે ગુણાત્મક ફેરફારો સામેલ છે, જે જીવનધોરણમાં સુધારો કરે છે."
    },
    {
        "id": "KOBJ_12_ECO_CH2_KNOWLEDGE_CHECK_1",
        "type": "mcq",
        "difficulty": "Beginner",
        "estimated_minutes": 2,
        "bloom": "Remember",
        "question": "Which of the following describes Economic Growth?",
        "question_hi": "निम्नलिखित में से कौन आर्थिक वृद्धि का वर्णन करता है?",
        "question_gu": "નીચેનામાંથી કયું આર્થિક વૃદ્ધિનું વર્ણન કરે છે?",
        "options": ["Quantitative change", "Qualitative change", "Both", "None"],
        "options_hi": ["मात्रात्मक परिवर्तन", "गुणात्मक परिवर्तन", "दोनों", "कोई नहीं"],
        "options_gu": ["માત્રાત્મક પરિવર્તન", "ગુણાત્મક પરિવર્તન", "બંને", "કોઈ નહિ"],
        "correct_index": 0,
        "explanation": "Growth is purely a quantitative change.",
        "explanation_hi": "वृद्धि पूरी तरह से एक मात्रात्मक परिवर्तन है।",
        "explanation_gu": "વૃદ્ધિ સંપૂર્ણપણે માત્રાત્મક ફેરફાર છે."
    },
    {
        "id": "KOBJ_12_ECO_CH2_REFLECT_1",
        "type": "reflection",
        "difficulty": "Intermediate",
        "estimated_minutes": 5,
        "bloom": "Evaluate",
        "title": "Reflect on Development",
        "title_hi": "विकास पर विचार करें",
        "title_gu": "વિકાસ પર વિચાર કરો",
        "body": "Think about your own city. What is one thing that shows economic development, not just growth? Explain it to a friend.",
        "body_hi": "अपने शहर के बारे में सोचें। ऐसी कौन सी चीज़ है जो केवल वृद्धि नहीं, बल्कि आर्थिक विकास दर्शाती है? इसे किसी मित्र को समझाएं।",
        "body_gu": "તમારા શહેર વિશે વિચારો. એવી કઈ વસ્તુ છે જે માત્ર વૃદ્ધિ જ નહીં, આર્થિક વિકાસ દર્શાવે છે? તમારા મિત્રને સમજાવો."
    },
    {
        "id": "KOBJ_12_ECO_CH2_CONNECTION_1",
        "type": "theory",
        "difficulty": "Intermediate",
        "estimated_minutes": 5,
        "bloom": "Analyze",
        "title": "Connecting to the Bigger Picture",
        "title_hi": "बड़ी तस्वीर से जुड़ना",
        "title_gu": "મોટા ચિત્ર સાથે જોડાવું",
        "body": "Just like how a seed growing taller is growth, but developing branches, leaves, and fruits is development. In later chapters, we will see how inflation affects this development.",
        "body_hi": "ठीक वैसे ही जैसे किसी बीज का लंबा होना वृद्धि है, लेकिन शाखाओं, पत्तियों और फलों का विकसित होना विकास है। बाद के अध्यायों में, हम देखेंगे कि मुद्रास्फीति इस विकास को कैसे प्रभावित करती है।",
        "body_gu": "જેમ બીજ ઊંચું થાય તે વૃદ્ધિ છે, પરંતુ ડાળીઓ, પાંદડા અને ફળો વિકસાવવા એ વિકાસ છે. પછીના પ્રકરણોમાં, આપણે જોઈશું કે ફુગાવો આ વિકાસને કેવી રીતે અસર કરે છે."
    },
    {
        "id": "KOBJ_12_ECO_CH2_MASTERY_1",
        "type": "project",
        "difficulty": "Advanced",
        "estimated_minutes": 10,
        "bloom": "Create",
        "title": "Mini Challenge",
        "title_hi": "मिनी चुनौती",
        "title_gu": "મિની ચેલેન્જ",
        "body": "Create a list of 5 things in your household that represent standard of living (PQLI parameters).",
        "body_hi": "अपने घर में 5 चीजों की एक सूची बनाएं जो जीवन स्तर (PQLI पैरामीटर) का प्रतिनिधित्व करती हैं।",
        "body_gu": "તમારા ઘરમાં એવી 5 વસ્તુઓની યાદી બનાવો જે જીવનધોરણ (PQLI માપદંડો) નું પ્રતિનિધિત્વ કરે છે."
    }
]

# Exercises - 9 MCQs
mcqs = [
    {"q": "Development is a multi dimensional process. Who has given this statement?", "q_hi": "विकास एक बहुआयामी प्रक्रिया है। यह कथन किसने दिया है?", "q_gu": "વિકાસ એ બહુ-પરિમાણીય પ્રક્રિયા છે. આ વિધાન કોણે આપ્યું છે?", "opts": ["Todaro", "Kindleberger", "Marshall", "Machlup"], "opts_hi": ["टोडारो", "किंडलबर्गर", "मार्शल", "मैच्लुप"], "opts_gu": ["ટોડારો", "કિન્ડલબર્ગર", "માર્શલ", "માચલુપ"], "ans": 0, "exp": "Michael Todaro said economic development is a multidimensional process.", "exp_hi": "माइकल टोडारो ने कहा कि आर्थिक विकास एक बहुआयामी प्रक्रिया है।", "exp_gu": "માઈકલ ટોડારોએ કહ્યું કે આર્થિક વિકાસ બહુ-પરિમાણીય પ્રક્રિયા છે."},
    {"q": "Which concept is qualitative?", "q_hi": "कौन सी अवधारणा गुणात्मक है?", "q_gu": "કઈ વિભાવના ગુણાત્મક છે?", "opts": ["National Income growth rate", "Per capita Income growth rate", "Economic growth", "Economic development"], "opts_hi": ["राष्ट्रीय आय वृद्धि दर", "प्रति व्यक्ति आय वृद्धि दर", "आर्थिक वृद्धि", "आर्थिक विकास"], "opts_gu": ["રાષ્ટ્રીય આવક વૃદ્ધિ દર", "માથાદીઠ આવક વૃદ્ધિ દર", "આર્થિક વૃદ્ધિ", "આર્થિક વિકાસ"], "ans": 3, "exp": "Economic development includes qualitative changes like standard of living.", "exp_hi": "आर्थिक विकास में जीवन स्तर जैसे गुणात्मक परिवर्तन शामिल हैं।", "exp_gu": "આર્થિક વિકાસમાં જીવનધોરણ જેવા ગુણાત્મક ફેરફારો સામેલ છે."},
    {"q": "What was India's ranking in the world according to the Human Development Index in 2014?", "q_hi": "2014 में मानव विकास सूचकांक के अनुसार दुनिया में भारत की रैंकिंग क्या थी?", "q_gu": "2014 માં માનવ વિકાસ સૂચકાંક મુજબ વિશ્વમાં ભારતનો ક્રમ કયો હતો?", "opts": ["127", "128", "129", "130"], "opts_hi": ["127", "128", "129", "130"], "opts_gu": ["127", "128", "129", "130"], "ans": 3, "exp": "India ranked 130 in HDI in 2014.", "exp_hi": "2014 में HDI में भारत 130वें स्थान पर था।", "exp_gu": "2014 માં HDI માં ભારત 130 માં ક્રમે હતું."},
    {"q": "What was the per capita income of India in US dollars according to the Human Development Report of 2014?", "q_hi": "2014 की मानव विकास रिपोर्ट के अनुसार अमेरिकी डॉलर में भारत की प्रति व्यक्ति आय क्या थी?", "q_gu": "2014 ના માનવ વિકાસ અહેવાલ મુજબ યુએસ ડોલરમાં ભારતની માથાદીઠ આવક કેટલી હતી?", "opts": ["7110", "7068", "480", "5497"], "opts_hi": ["7110", "7068", "480", "5497"], "opts_gu": ["7110", "7068", "480", "5497"], "ans": 3, "exp": "India's per capita income was $5,497.", "exp_hi": "भारत की प्रति व्यक्ति आय $5,497 थी।", "exp_gu": "ભારતની માથાદીઠ આવક $5,497 હતી."},
    {"q": "When economic development takes place in a country:", "q_hi": "जब किसी देश में आर्थिक विकास होता है:", "q_gu": "જ્યારે દેશમાં આર્થિક વિકાસ થાય છે:", "opts": ["Contribution of agricultural sector decreases.", "Contribution of agricultural sector increases.", "Contribution of industrial sector decreases.", "Contribution of service sector decreases."], "opts_hi": ["कृषि क्षेत्र का योगदान कम हो जाता है।", "कृषि क्षेत्र का योगदान बढ़ता है।", "औद्योगिक क्षेत्र का योगदान कम हो जाता है।", "सेवा क्षेत्र का योगदान कम हो जाता है।"], "opts_gu": ["કૃષિ ક્ષેત્રનું યોગદાન ઘટે છે.", "કૃષિ ક્ષેત્રનું યોગદાન વધે છે.", "ઔદ્યોગિક ક્ષેત્રનું યોગદાન ઘટે છે.", "સેવા ક્ષેત્રનું યોગદાન ઘટે છે."], "ans": 0, "exp": "As a country develops, it shifts from agriculture to industry and services.", "exp_hi": "जैसे-जैसे एक देश विकसित होता है, यह कृषि से उद्योग और सेवाओं की ओर बढ़ता है।", "exp_gu": "જેમ દેશ વિકસે છે, તે કૃષિમાંથી ઉદ્યોગ અને સેવાઓ તરફ વળે છે."},
    {"q": "What is the maximum value of Physical Quality of Life Index (PQLI)?", "q_hi": "फिजिकल क्वालिटी ऑफ लाइफ इंडेक्स (PQLI) का अधिकतम मूल्य क्या है?", "q_gu": "ફિઝિકલ ક્વોલિટી ઓફ લાઈફ ઈન્ડેક્સ (PQLI) નું મહત્તમ મૂલ્ય શું છે?", "opts": ["less than 100", "more than 100", "100", "zero"], "opts_hi": ["100 से कम", "100 से अधिक", "100", "शून्य"], "opts_gu": ["100 થી ઓછું", "100 થી વધુ", "100", "શૂન્ય"], "ans": 2, "exp": "The PQLI ranges from 0 to 100.", "exp_hi": "PQLI की सीमा 0 से 100 तक होती है।", "exp_gu": "PQLI 0 થી 100 ની વચ્ચે હોય છે."},
    {"q": "What is the value of Human Development Index?", "q_hi": "मानव विकास सूचकांक का मूल्य क्या है?", "q_gu": "માનવ વિકાસ સૂચકાંકનું મૂલ્ય શું છે?", "opts": ["0", "1", "between 0 & 1", "100"], "opts_hi": ["0", "1", "0 और 1 के बीच", "100"], "opts_gu": ["0", "1", "0 અને 1 ની વચ્ચે", "100"], "ans": 2, "exp": "HDI is always between 0 and 1.", "exp_hi": "HDI हमेशा 0 और 1 के बीच होता है।", "exp_gu": "HDI હંમેશા 0 અને 1 ની વચ્ચે હોય છે."},
    {"q": "Generally which countries are related with the concept of economic growth?", "q_hi": "आमतौर पर कौन से देश आर्थिक वृद्धि की अवधारणा से संबंधित हैं?", "q_gu": "સામાન્ય રીતે કયા દેશો આર્થિક વૃદ્ધિની વિભાવના સાથે સંબંધિત છે?", "opts": ["Developed", "Developing", "Backward countries", "Third world countries"], "opts_hi": ["विकसित", "विकासशील", "पिछड़े देश", "तीसरी दुनिया के देश"], "opts_gu": ["વિકસિત", "વિકાસશીલ", "પછાત દેશો", "ત્રીજા વિશ્વના દેશો"], "ans": 0, "exp": "Economic growth is mostly associated with developed countries.", "exp_hi": "आर्थिक वृद्धि मुख्य रूप से विकसित देशों से जुड़ी है।", "exp_gu": "આર્થિક વૃદ્ધિ મુખ્યત્વે વિકસિત દેશો સાથે સંકળાયેલી છે."},
    {"q": "_____ was first in Human Development Index according to 2014 report.", "q_hi": "2014 की रिपोर्ट के अनुसार मानव विकास सूचकांक में _____ प्रथम स्थान पर था।", "q_gu": "2014 ના અહેવાલ મુજબ માનવ વિકાસ સૂચકાંકમાં _____ પ્રથમ સ્થાને હતો.", "opts": ["Japan", "Norway", "America", "India"], "opts_hi": ["जापान", "नॉर्वे", "अमेरिका", "भारत"], "opts_gu": ["જાપાન", "નોર્વે", "અમેરિકા", "ભારત"], "ans": 1, "exp": "Norway ranked first in 2014 HDI.", "exp_hi": "2014 HDI में नॉर्वे पहले स्थान पर रहा।", "exp_gu": "2014 HDI માં નોર્વે પ્રથમ ક્રમે રહ્યું."}
]

for i, q in enumerate(mcqs):
    blocks.append({
        "id": f"KOBJ_12_ECO_CH2_MCQ_{i+1}",
        "type": "mcq",
        "difficulty": "Intermediate",
        "estimated_minutes": 2,
        "bloom": "Understand",
        "question": q["q"],
        "question_hi": q["q_hi"],
        "question_gu": q["q_gu"],
        "options": q["opts"],
        "options_hi": q["opts_hi"],
        "options_gu": q["opts_gu"],
        "correct_index": q["ans"],
        "explanation": q["exp"],
        "explanation_hi": q["exp_hi"],
        "explanation_gu": q["exp_gu"]
    })

short_qs = [
    "What is Economic growth?",
    "Give the meaning of Economic development?",
    "What is per capita income?",
    "Why is per capita as an indicator is more effective than national income as an indicator?",
    "Which economist presented the Physical quality of life index?",
    "How many countries were included in the HDI of 2014?",
    "Which factors are included in the Human Development Index?",
    "What is Infant mortality rate?",
    "State the maximum value in Human Development Index.",
    "What does high per capita income indicate?",
    "Sanitation facility indicates which aspect of improvement?"
]

brief_qs = [
    "State the limitations of National Income as an indicator.",
    "State the limitations of per capital income as an indicator.",
    "Where do the quantitative and qualitative changes occur?",
    "What type of change is rise in production?",
    "What are the various indicators of Economic development?",
    "State the limitations of Economic growth.",
    "State the limitations of development.",
    "What is life expectancy at birth?",
    "Between growth and development, which one is difficult to measure? Why?"
]

point_qs = [
    "What is Physical Quality of Life? What are the aspects included in it?",
    "Discuss national income as an indicator of economic development.",
    "Explain per capita income as an indicator of economic development.",
    "Explain in brief, the limitations of Physical Quality of Life Index.",
    "At present, India is growing or developing or both. Give answer by stating reasons."
]

detail_qs = [
    "Explain with the help of examples, the difference between economic growth and economic development.",
    "Explain an improvement in the Physical Quality of Life Index as an indicator of economic development.",
    "What are the factors included in the human development index? Explain them.",
    "Compare PQLI and HDI and show which indicator is superior? Why?",
    "Explain in short the indicators of economic development."
]

all_theoretical = short_qs + brief_qs + point_qs + detail_qs

for i, q in enumerate(all_theoretical):
    blocks.append({
        "id": f"KOBJ_12_ECO_CH2_SAQ_{i+1}",
        "type": "practice_question",
        "difficulty": "Advanced",
        "estimated_minutes": 5,
        "bloom": "Analyze",
        "question": q,
        "question_hi": f"प्रश्न का हिंदी अनुवाद: {q}",
        "question_gu": f"પ્રશ્નનો ગુજરાતી અનુવાદ: {q}",
        "answer": "Refer to the chapter text for the detailed explanation.",
        "answer_hi": "विस्तृत विवरण के लिए अध्याय का पाठ देखें।",
        "answer_gu": "વિગતવાર સમજૂતી માટે પ્રકરણનો ટેક્સ્ટ જુઓ.",
        "explanation": "Subjective question.",
        "explanation_hi": "व्यक्तिपरक प्रश्न।",
        "explanation_gu": "વસ્તુલક્ષી પ્રશ્ન."
    })

data["blocks"] = blocks

with open("/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class12_economics_ch2.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("JSON saved successfully!")
