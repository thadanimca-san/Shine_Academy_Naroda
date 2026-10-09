import os
import json

def make_quiz(id_str, q_en, q_hi, q_gu, opts_en, opts_hi, opts_gu, correct_idx, expl_en, expl_hi, expl_gu, bloom="Apply", diff="Intermediate", mins=2):
    return {
        "id": id_str,
        "type": "quiz",
        "question": q_en,
        "options": opts_en,
        "correct_index": correct_idx,
        "explanation": expl_en,
        "question_hi": q_hi,
        "options_hi": opts_hi,
        "explanation_hi": expl_hi,
        "question_gu": q_gu,
        "options_gu": opts_gu,
        "explanation_gu": expl_gu,
        "bloom": bloom,
        "difficulty": diff,
        "estimated_minutes": mins
    }

def get_part1_blocks():
    blocks = []

    # =========================================================================
    # STEP 1: HOOK (The Ladder and the Daily Piggy Bank)
    # =========================================================================
    blocks.append({
        "id": "C10M_CH5_1",
        "type": "hook",
        "title": "The Rhythm of Constant Steps",
        "body": "Look closely at a ladder. Each rung is spaced at an identical distance from the previous one. If the first rung is 30 cm from the ground, the second is at 60 cm, the third at 90 cm, and so on. Or imagine saving money in a piggy bank: you start with ₹100 on day one, and add ₹20 every single day. \n\nEvery day your savings grow by a fixed, predictable amount: ₹100, ₹120, ₹140, ₹160... In mathematics, whenever numbers advance step-by-step by adding the same constant difference, we enter the world of **Arithmetic Progressions (समान्तर श्रेढ़ियाँ / સમાંતર શ્રેણીઓ)**!",
        "title_hi": "समान कदमों की लय",
        "body_hi": "किसी सीढ़ी को ध्यान से देखें। प्रत्येक डंडा पिछले डंडे से एक समान दूरी पर स्थित होता है। यदि पहला डंडा जमीन से 30 सेमी ऊपर है, तो दूसरा 60 सेमी पर, तीसरा 90 सेमी पर, और इसी तरह आगे बढ़ता है। या गुल्लक में पैसे बचाने की कल्पना करें: आप पहले दिन ₹100 से शुरू करते हैं, और हर दिन ₹20 जोड़ते हैं।\n\nहर दिन आपकी बचत एक निश्चित राशि से बढ़ती है: ₹100, ₹120, ₹140, ₹160... गणित में, जब भी संख्याएँ एक निश्चित अंतर जोड़कर कदम-दर-कदम आगे बढ़ती हैं, तो हम **समान्तर श्रेढ़ी (AP)** की दुनिया में प्रवेश करते हैं!",
        "title_gu": "સમાન પગથિયાંનો લય",
        "body_gu": "કોઈ સીડીને ધ્યાનથી જુઓ. દરેક પગથિયું અગાઉના પગથિયાથી સમાન અંતરે ગોઠવાયેલું હોય છે. જો પહેલું પગથિયું જમીનથી 30 સેમી ઊંચાઈએ હોય, તો બીજું 60 સેમી પર, ત્રીજું 90 સેમી પર, અને એ જ રીતે આગળ વધે છે. અથવા ગલ્લામાં બચત કરવાની કલ્પના કરો: તમે પહેલા દિવસે ₹100 મૂકો છો અને દરરોજ ₹20 ઉમેરો છો.\n\nદરરોજ તમારી બચત એક નિશ્ચિત રકમથી વધે છે: ₹100, ₹120, ₹140, ₹160... ગણિતમાં, જ્યારે પણ સંખ્યાઓ એક સમાન તફાવત ઉમેરીને ક્રમશઃ આગળ વધે છે, ત્યારે આપણે **સમાંતર શ્રેણી (AP)** ની દુનિયામાં પ્રવેશ કરીએ છીએ!",
        "bloom": "Understand",
        "difficulty": "Beginner",
        "estimated_minutes": 3
    })

    # =========================================================================
    # STEP 2: SOCRATIC THINKING
    # =========================================================================
    blocks.append({
        "id": "C10M_CH5_2",
        "type": "socratic_question",
        "question": "A girl starts walking up a flight of stairs. Step 1 is 15 cm high, Step 2 is 30 cm high, and Step 3 is 45 cm high. By how many centimetres does her height increase with each new step?",
        "options": ["15 cm", "30 cm", "45 cm", "10 cm"],
        "correct_index": 0,
        "explanation": "Subtracting successive steps: 30 - 15 = 15 cm, and 45 - 30 = 15 cm. The height increases by exactly 15 cm with each step.",
        "question_hi": "एक लड़की सीढ़ियों पर चढ़ना शुरू करती है। पहला कदम 15 सेमी ऊँचा है, दूसरा कदम 30 सेमी ऊँचा है, और तीसरा कदम 45 सेमी ऊँचा है। प्रत्येक नए कदम के साथ उसकी ऊँचाई कितने सेंटीमीटर बढ़ती है?",
        "options_hi": ["15 सेमी", "30 सेमी", "45 सेमी", "10 सेमी"],
        "explanation_hi": "उत्तरोत्तर पदों को घटाने पर: 30 - 15 = 15 सेमी, और 45 - 30 = 15 सेमी। प्रत्येक कदम के साथ ऊँचाई ठीक 15 सेमी बढ़ती है।",
        "question_gu": "એક છોકરી પગથિયાં ચઢવાનું શરૂ કરે છે. પહેલું પગથિયું 15 સેમી ઊંચું છે, બીજું પગથિયું 30 સેમી ઊંચું છે, અને ત્રીજું પગથિયું 45 સેમી ઊંચું છે. દરેક નવા પગથિયા સાથે તેની ઊંચાઈ કેટલા સેન્ટીમીટર વધે છે?",
        "options_gu": ["15 સેમી", "30 સેમી", "45 સેમી", "10 સેમી"],
        "explanation_gu": "ક્રમિક પદોની બાદબાકી કરતા: 30 - 15 = 15 સેમી, અને 45 - 30 = 15 સેમી. દરેક પગથિયા સાથે ઊંચાઈ બરાબર 15 સેમી વધે છે.",
        "bloom": "Apply",
        "difficulty": "Beginner",
        "estimated_minutes": 1
    })

    # =========================================================================
    # STEP 3: DISCOVERY (Linear Addition vs Multiplication)
    # =========================================================================
    blocks.append({
        "id": "C10M_CH5_3",
        "type": "discovery",
        "title": "Discovery: Adding vs Multiplying",
        "body": "Compare these two lists of numbers:\n\nList A: 2, 4, 6, 8, 10...\nList B: 2, 4, 8, 16, 32...\n\nNotice the vital difference:\n- In List A, we **add 2** to get the next number ($4-2 = 2, 6-4 = 2, 8-6 = 2$). The difference is constant!\n- In List B, we **multiply by 2** to get the next number ($4-2 = 2, 8-4 = 4, 16-8 = 8$). The difference is NOT constant.\n\nOnly sequences where we add a fixed number belong to an **Arithmetic Progression (AP)**. Sequences where we multiply belong to Geometric Progressions.",
        "title_hi": "खोज: जोड़ना बनाम गुणा करना",
        "body_hi": "संख्याओं की इन दो सूचियों की तुलना करें:\n\nसूची A: 2, 4, 6, 8, 10...\nसूची B: 2, 4, 8, 16, 32...\n\nमहत्वपूर्ण अंतर पर ध्यान दें:\n- सूची A में, अगली संख्या प्राप्त करने के लिए हम **2 जोड़ते हैं** ($4-2 = 2, 6-4 = 2, 8-6 = 2$)। अंतर स्थिर है!\n- सूची B में, अगली संख्या प्राप्त करने के लिए हम **2 से गुणा करते हैं** ($4-2 = 2, 8-4 = 4, 16-8 = 8$)। अंतर स्थिर नहीं है।\n\nकेवल वे अनुक्रम जिनमें हम एक निश्चित संख्या जोड़ते हैं, **समान्तर श्रेढ़ी (AP)** कहलाते हैं।",
        "title_gu": "શોધ: સરવાળો કરવો વિરુદ્ધ ગુણાકાર કરવો",
        "body_gu": "સંખ્યાઓની આ બે યાદીઓની સરખામણી કરો:\n\nયાદી A: 2, 4, 6, 8, 10...\nયાદી B: 2, 4, 8, 16, 32...\n\nમહત્વપૂર્ણ તફાવત નોંધો:\n- યાદી A માં, આગળની સંખ્યા મેળવવા માટે આપણે **2 ઉમેરીએ છીએ** ($4-2 = 2, 6-4 = 2, 8-6 = 2$). તફાવત અચળ છે!\n- યાદી B માં, આગળની સંખ્યા મેળવવા માટે આપણે **2 વડે ગુણીએ છીએ** ($4-2 = 2, 8-4 = 4, 16-8 = 8$). તફાવત અચળ નથી.\n\nમાત્ર એવા જ શ્રેણીઓ જેમાં આપણે નિશ્ચિત સંખ્યા ઉમેરીએ છીએ તેને **સમાંતર શ્રેણી (AP)** કહેવાય છે.",
        "bloom": "Understand",
        "difficulty": "Beginner",
        "estimated_minutes": 3
    })

    # =========================================================================
    # STEP 4: REVEAL (Formal Definition & General Form)
    # =========================================================================
    blocks.append({
        "id": "C10M_CH5_4",
        "type": "theory",
        "title": "Definition & General Form of an AP",
        "body": "An **Arithmetic Progression (AP)** is a list of numbers in which each term is obtained by adding a fixed number to the preceding term, except the first term.\n\n**Key Terminology:**\n- **First Term ($a$ or $a_1$):** The very first number in the sequence.\n- **Common Difference ($d$):** The fixed number added to each term. \n  $$d = a_{k+1} - a_k$$\n  **Note:** $d$ can be **positive**, **negative**, or **zero**!\n\n**General Form of an AP:**\n$$a, a + d, a + 2d, a + 3d, \\dots$$\n\n- If an AP has a finite number of terms, it is a **Finite AP** (has a last term).\n- If it goes on endlessly, it is an **Infinite AP** (no last term).",
        "title_hi": "समान्तर श्रेढ़ी (AP) की परिभाषा और व्यापक रूप",
        "body_hi": "एक **समान्तर श्रेढ़ी (AP)** संख्याओं की एक ऐसी सूची है जिसमें प्रत्येक पद (पहले पद के अतिरिक्त) अपने पूर्व पद में एक निश्चित संख्या जोड़ने पर प्राप्त होता है।\n\n**प्रमुख शब्दावली:**\n- **प्रथम पद ($a$ या $a_1$):** अनुक्रम की पहली संख्या।\n- **सार्व अंतर ($d$):** प्रत्येक पद में जोड़ी जाने वाली निश्चित संख्या।\n  $$d = a_{k+1} - a_k$$\n  **ध्यान दें:** $d$ **धनात्मक**, **ऋणात्मक** या **शून्य** हो सकता है!\n\n**AP का व्यापक रूप:**\n$$a, a + d, a + 2d, a + 3d, \\dots$$\n\n- यदि किसी AP में पदों की संख्या सीमित हो, तो उसे **परिमित AP** कहते हैं (इसका अंतिम पद होता है)।\n- यदि यह अनवरत चलती रहे, तो उसे **अपरिमित AP** कहते हैं (कोई अंतिम पद नहीं होता)।",
        "title_gu": "સમાંતર શ્રેણી (AP) ની વ્યાખ્યા અને વ્યાપક સ્વરૂપ",
        "body_gu": "એક **સમાંતર શ્રેણી (AP)** એ સંખ્યાઓની એવી યાદી છે જેમાં પ્રથમ પદ સિવાયનું દરેક પદ આગળના પદમાં નિશ્ચિત સંખ્યા ઉમેરીને મેળવી શકાય છે.\n\n**મુખ્ય સંકલ્પનાઓ:**\n- **પ્રથમ પદ ($a$ અથવા $a_1$):** શ્રેણીની સૌથી પહેલી સંખ્યા.\n- **સામાન્ય તફાવત ($d$):** દરેક પદમાં ઉમેરવામાં આવતી નિશ્ચિત સંખ્યા.\n  $$d = a_{k+1} - a_k$$\n  **નોંધ:** $d$ **ધન**, **ઋણ** કે **શૂન્ય** હોઈ શકે છે!\n\n**AP નું વ્યાપક સ્વરૂપ:**\n$$a, a + d, a + 2d, a + 3d, \\dots$$\n\n- જો AP માં પદોની સંખ્યા શાંત (મર્યાદિત) હોય, તો તેને **શાંત AP** કહેવાય છે (તેનું છેલ્લું પદ હોય છે).\n- જો તે અનંત સુધી ચાલતી રહે, તો તેને **અનંત AP** કહેવાય છે (છેલ્લું પદ હોતું નથી).",
        "bloom": "Remember",
        "difficulty": "Beginner",
        "estimated_minutes": 3
    })

    # =========================================================================
    # STEP 5: TEACHER TIP & COMMON MISTAKES
    # =========================================================================
    blocks.append({
        "id": "C10M_CH5_5",
        "type": "teacher_tip",
        "title": "Teacher Tip: How to Calculate Common Difference 'd'",
        "body": "**Golden Rule:** Always subtract the PRECEDING term from the SUCCEEDING term: \n$$d = a_2 - a_1 = a_3 - a_2 = a_4 - a_3$$\n\n**Common Mistake:** Never calculate $a_1 - a_2$! If the sequence is decreasing, such as $10, 7, 4, 1...$, then:\n$$d = 7 - 10 = -3$$\nHere $d$ is negative! If you mistakenly do $10 - 7 = +3$, all subsequent calculations will be ruined.",
        "title_hi": "शिक्षक युक्ति: सार्व अंतर 'd' की सही गणना",
        "body_hi": "**स्वर्ण नियम:** हमेशा अगले पद में से पिछले पद को घटाएं: \n$$d = a_2 - a_1 = a_3 - a_2 = a_4 - a_3$$\n\n**सामान्य गलती:** कभी भी $a_1 - a_2$ न करें! यदि अनुक्रम घट रहा है, जैसे $10, 7, 4, 1...$, तो:\n$$d = 7 - 10 = -3$$\nयहाँ $d$ ऋणात्मक है! यदि आप भूलवश $10 - 7 = +3$ लिखते हैं, तो आपके सभी आगे के उत्तर गलत हो जाएंगे।",
        "title_gu": "શિક્ષકની સલાહ: સામાન્ય તફાવત 'd' ની સાચી ગણતરી",
        "body_gu": "**સુવર્ણ નિયમ:** હંમેશા આગળના પદમાંથી પાછળનું પદ બાદ કરો: \n$$d = a_2 - a_1 = a_3 - a_2 = a_4 - a_3$$\n\n**સામાન્ય ભૂલ:** ક્યારેય $a_1 - a_2$ ન કરો! જો શ્રેણી ઘટતી હોય, જેમ કે $10, 7, 4, 1...$, તો:\n$$d = 7 - 10 = -3$$\nઅહીં $d$ ઋણ છે! જો તમે ભૂલથી $10 - 7 = +3$ ગણશો, તો આગળની બધી ગણતરીઓ ખોટી પડશે.",
        "bloom": "Apply",
        "difficulty": "Beginner",
        "estimated_minutes": 2
    })

    # =========================================================================
    # EXERCISE 5.1 - QUESTION 1 (All 4 Real-Life Situations)
    # =========================================================================
    # Q1.1
    blocks.append(make_quiz(
        "C10M_CH5_EX5.1_Q1_p1",
        "Exercise 5.1 (Q1.i): In which of the following situations does the list of numbers involved make an arithmetic progression, and why?\n'The taxi fare after each km when the fare is ₹15 for the first km and ₹8 for each additional km.'",
        "प्रश्नावली 5.1 (Q1.i): निम्नलिखित स्थितियों में से किन स्थितियों में संबद्ध संख्याओं की सूची AP है और क्यों?\n'प्रत्येक किलोमीटर के बाद का टैक्सी का किराया, जबकि प्रथम किलोमीटर के लिए किराया ₹15 है और प्रत्येक अतिरिक्त किलोमीटर के लिए किराया ₹8 है।'",
        "સ્વાધ્યાય 5.1 (Q1.i): નીચે આપેલી સ્થિતિમાંથી કઈ સ્થિતિમાં સંબંધિત સંખ્યાઓની યાદી સમાંતર શ્રેણી બને છે અને કેમ?\n'ટેક્ષીનું ભાડું, પ્રથમ કિમી માટે ₹15 અને પછીના દરેક કિમી માટે ₹8 છે.'",
        [
            "Yes, it forms an AP because the difference between successive fares is constantly ₹8",
            "No, it does not form an AP because the first km costs more",
            "No, it is a geometric progression",
            "Yes, it forms an AP with common difference ₹15"
        ],
        [
            "हाँ, यह एक AP बनाती है क्योंकि क्रमिक किरायों के बीच का अंतर स्थिर रूप से ₹8 है",
            "नहीं, यह AP नहीं बनाती क्योंकि पहले किलोमीटर का किराया अधिक है",
            "नहीं, यह एक गुणोत्तर श्रेढ़ी है",
            "हाँ, यह सार्व अंतर ₹15 वाली एक AP बनाती है"
        ],
        [
            "હા, તે AP બનાવે છે કારણ કે ક્રમિક ભાડા વચ્ચેનો તફાવત સતત ₹8 છે",
            "ના, તે AP બનાવતી નથી કારણ કે પ્રથમ કિમીનું ભાડું વધારે છે",
            "ના, તે સમગુણોત્તર શ્રેણી છે",
            "હા, તે સામાન્ય તફાવત ₹15 વાળી AP બનાવે છે"
        ],
        0,
        "Fare for 1st km = 15. For 2 km = 15 + 8 = 23. For 3 km = 23 + 8 = 31. The terms are 15, 23, 31, 39... Since (a_{k+1} - a_k) = 8 (constant), it forms an AP with a = 15 and d = 8.",
        "पहले किमी का किराया = 15। 2 किमी का = 15 + 8 = 23। 3 किमी का = 23 + 8 = 31। पद हैं: 15, 23, 31, 39... चूँकि सार्व अंतर d = 8 स्थिर है, यह a = 15 और d = 8 वाली AP है।",
        "પ્રથમ કિમીનું ભાડું = 15. 2 કિમી માટે = 15 + 8 = 23. 3 કિમી માટે = 23 + 8 = 31. પદો: 15, 23, 31, 39... સામાન્ય તફાવત d = 8 અચળ હોવાથી, તે a = 15 અને d = 8 વાળી AP બનાવે છે."
    ))

    # Q1.2
    blocks.append(make_quiz(
        "C10M_CH5_EX5.1_Q1_p2",
        "Exercise 5.1 (Q1.ii): Does the situation form an AP?\n'The amount of air present in a cylinder when a vacuum pump removes 1/4 of the air remaining in the cylinder at a time.'",
        "प्रश्नावली 5.1 (Q1.ii): क्या यह स्थिति AP बनाती है?\n'किसी बेलन (सिलेंडर) में उपस्थित हवा की मात्रा, जबकि वायु निकालने वाला पम्प प्रत्येक बार बेलन की शेष हवा का 1/4 भाग बाहर निकाल देता है।'",
        "સ્વાધ્યાય 5.1 (Q1.ii): શું આ સ્થિતિ AP બનાવે છે?\n'નળાકારમાં રહેલ હવાનું પ્રમાણ, જ્યારે વેક્યુમ પંપ દરેક વખતે નળાકારમાં બાકી રહેલ હવાનો 1/4 ભાગ બહાર કાઢે છે.'",
        [
            "No, it does not form an AP because the difference between successive volumes is not constant",
            "Yes, it forms an AP with common difference -1/4",
            "Yes, it forms an AP with common difference 3/4",
            "No, because the volume increases"
        ],
        [
            "नहीं, यह AP नहीं बनाती क्योंकि क्रमिक आयતनों के बीच का अंतर स्थिर नहीं है",
            "हाँ, यह सार्व अंतर -1/4 वाली एक AP बनाती है",
            "हाँ, यह सार्व अंतर 3/4 वाली एक AP बनाती है",
            "नहीं, क्योंकि आयतन बढ़ता है"
        ],
        [
            "ના, તે AP બનાવતી નથી કારણ કે ક્રમિક કદ વચ્ચેનો તફાવત અચળ નથી",
            "હા, તે સામાન્ય તફાવત -1/4 વાળી AP બનાવે છે",
            "હા, તે સામાન્ય તફાવત 3/4 વાળી AP બનાવે છે",
            "ના, કારણ કે કદ વધે છે"
        ],
        0,
        "Let initial volume be V. After 1st removal: V - V/4 = (3/4)V. After 2nd removal: (3/4)V - (1/4)(3/4)V = (9/16)V. The differences are -V/4 and -3V/16. Since differences are unequal, it is NOT an AP.",
        "माना प्रारंभिक आयतन V है। पहली बार निकालने पर: (3/4)V। दूसरी बार निकालने पर: (9/16)V। अंतर -V/4 और -3V/16 हैं, जो समान नहीं हैं। अतः यह AP नहीं है।",
        "ધારો કે પ્રારંભિક કદ V છે. પ્રથમ વખત પછી: (3/4)V. બીજી વખત પછી: (9/16)V. તફાવત -V/4 અને -3V/16 છે જે સમાન નથી. તેથી તે AP નથી."
    ))

    # Q1.3
    blocks.append(make_quiz(
        "C10M_CH5_EX5.1_Q1_p3",
        "Exercise 5.1 (Q1.iii): Does the situation form an AP?\n'The cost of digging a well after every metre of digging, when it costs ₹150 for the first metre and rises by ₹50 for each subsequent metre.'",
        "प्रश्नावली 5.1 (Q1.iii): क्या यह स्थिति AP बनाती है?\n'प्रत्येक मीटर की खुदाई के बाद, एक कुआँ खोदने की लागत, जबकि प्रथम मीटर खुदाई की लागत ₹150 है और बाद में प्रत्येक मीटर खुदाई की लागत ₹50 बढ़ती जाती है।'",
        "સ્વાધ્યાય 5.1 (Q1.iii): શું આ સ્થિતિ AP બનાવે છે?\n'પ્રત્યેક મીટરના ખોદકામ બાદ એક કૂવો ખોદવાનો ખર્ચ, પ્રથમ મીટર માટે ₹150 અને પછીના પ્રત્યેક મીટર દીઠ ₹50 વધતો જાય છે.'",
        [
            "Yes, it forms an AP with a = 150 and d = 50",
            "No, it does not form an AP",
            "Yes, it forms an AP with a = 50 and d = 150",
            "No, because the cost must be constant"
        ],
        [
            "हाँ, यह a = 150 और d = 50 वाली एक AP बनाती है",
            "नहीं, यह AP नहीं बनाती है",
            "हाँ, यह a = 50 और d = 150 वाली एक AP बनाती है",
            "नहीं, क्योंकि लागत स्थिर होनी चाहिए"
        ],
        [
            "હા, તે a = 150 અને d = 50 વાળી AP બનાવે છે",
            "ના, તે AP બનાવતી નથી",
            "હા, તે a = 50 અને d = 150 વાળી AP બનાવે છે",
            "ના, કારણ કે ખર્ચ અચળ હોવો જોઈએ"
        ],
        0,
        "Costs for successive metres are: 150, 200, 250, 300... The common difference is d = 200 - 150 = 50 (constant). Therefore, it is an AP.",
        "क्रमिक मीटरों की लागत है: 150, 200, 250, 300... सार्व अंतर d = 200 - 150 = 50 (स्थिर) है। अतः यह एक AP है।",
        "ક્રમિક મીટર માટે ખર્ચ: 150, 200, 250, 300... સામાન્ય તફાવત d = 200 - 150 = 50 (અચળ) છે. તેથી તે AP છે."
    ))

    # Q1.4
    blocks.append(make_quiz(
        "C10M_CH5_EX5.1_Q1_p4",
        "Exercise 5.1 (Q1.iv): Does the situation form an AP?\n'The amount of money in the account every year, when ₹10,000 is deposited at compound interest at 8% per annum.'",
        "प्रश्नावली 5.1 (Q1.iv): क्या यह स्थिति AP बनाती है?\n'खाते में प्रत्येक वर्ष का मिश्रधन, जबकि ₹10,000 की राशि 8% वार्षिक की दर से चक्रवृद्धि ब्याज पर जमा की जाती है।'",
        "સ્વાધ્યાય 5.1 (Q1.iv): શું આ સ્થિતિ AP બનાવે છે?\n'ખાતામાં જમા થયેલ વાર્ષિક રકમ, જ્યારે ₹10,000 ની રકમ 8% ના વાર્ષિક ચક્રવૃદ્ધિ વ્યાજના દરે મુકવામાં આવે છે.'",
        [
            "No, it does not form an AP because compound interest increases the principal multiplicatively",
            "Yes, it forms an AP with common difference ₹800",
            "Yes, it forms an AP with common difference ₹10,800",
            "No, because the interest is 0"
        ],
        [
            "नहीं, यह AP नहीं बनाती क्योंकि चक्रवृद्धि ब्याज मूलधन को गुणात्मक रूप से बढ़ाता है",
            "हाँ, यह सार्व अंतर ₹800 वाली एक AP बनाती है",
            "हाँ, यह सार्व अंतर ₹10,800 वाली एक AP बनाती है",
            "नहीं, क्योंकि ब्याज 0 है"
        ],
        [
            "ના, તે AP બનાવતી નથી કારણ કે ચક્રવૃદ્ધિ વ્યાજ રકમને ગુણાત્મક રીતે વધારે છે",
            "હા, તે સામાન્ય તફાવત ₹800 વાળી AP બનાવે છે",
            "હા, તે સામાન્ય તફાવત ₹10,800 વાળી AP બનાવે છે",
            "ના, કારણ કે વ્યાજ 0 છે"
        ],
        0,
        "Amount after n years is 10000(1 + 8/100)^n. Year 1: 10800, Year 2: 11664, Year 3: 12597.12. The differences are 800, 864, 933.12... which are not equal. Hence it is NOT an AP.",
        "n वर्षों के बाद की राशि 10000(1 + 8/100)^n होती है। वर्ष 1: 10800, वर्ष 2: 11664... अंतर 800, 864... समान नहीं हैं। अतः यह AP नहीं है।",
        "n વર્ષ પછીની રકમ 10000(1 + 8/100)^n છે. વર્ષ 1: 10800, વર્ષ 2: 11664... તફાવત 800, 864... સમાન નથી. તેથી તે AP નથી."
    ))

    # =========================================================================
    # EXERCISE 5.1 - QUESTION 2 (Write First 4 Terms, 5 Subparts)
    # =========================================================================
    q2_data = [
        ("a = 10, d = 10", ["10, 20, 30, 40", "10, 100, 1000, 10000", "0, 10, 20, 30", "10, 20, 40, 80"], 0, "a₁ = 10, a₂ = 10+10 = 20, a₃ = 20+10 = 30, a₄ = 30+10 = 40."),
        ("a = -2, d = 0", ["-2, -2, -2, -2", "-2, 0, 2, 4", "-2, -4, -6, -8", "0, 0, 0, 0"], 0, "Since d = 0, every term is identical: -2, -2, -2, -2."),
        ("a = 4, d = -3", ["4, 1, -2, -5", "4, 7, 10, 13", "4, -12, 36, -108", "4, 1, 0, -3"], 0, "a₁ = 4, a₂ = 4 + (-3) = 1, a₃ = 1 + (-3) = -2, a₄ = -2 + (-3) = -5."),
        ("a = -1, d = 1/2", ["-1, -1/2, 0, 1/2", "-1, -3/2, -2, -5/2", "-1, 0, 1, 2", "-1, -1/2, -1/4, -1/8"], 0, "a₁ = -1, a₂ = -1 + 1/2 = -1/2, a₃ = -1/2 + 1/2 = 0, a₄ = 0 + 1/2 = 1/2."),
        ("a = -1.25, d = -0.25", ["-1.25, -1.50, -1.75, -2.00", "-1.25, -1.00, -0.75, -0.50", "-1.25, -1.50, -2.00, -2.50", "-1.25, 0.25, 1.75, 3.25"], 0, "a₁ = -1.25, a₂ = -1.25 + (-0.25) = -1.50, a₃ = -1.75, a₄ = -2.00.")
    ]
    q2_data_hi = [
        "a₁ = 10, a₂ = 10+10 = 20, a₃ = 20+10 = 30, a₄ = 30+10 = 40।",
        "चूँकि d = 0 है, प्रत्येक पद समान होगा: -2, -2, -2, -2।",
        "a₁ = 4, a₂ = 4 + (-3) = 1, a₃ = 1 + (-3) = -2, a₄ = -2 + (-3) = -5।",
        "a₁ = -1, a₂ = -1 + 1/2 = -1/2, a₃ = -1/2 + 1/2 = 0, a₄ = 0 + 1/2 = 1/2।",
        "a₁ = -1.25, a₂ = -1.25 + (-0.25) = -1.50, a₃ = -1.75, a₄ = -2.00।"
    ]
    q2_data_gu = [
        "a₁ = 10, a₂ = 10+10 = 20, a₃ = 20+10 = 30, a₄ = 30+10 = 40.",
        "કારણ કે d = 0 છે, દરેક પદ સમાન રહે છે: -2, -2, -2, -2.",
        "a₁ = 4, a₂ = 4 + (-3) = 1, a₃ = 1 + (-3) = -2, a₄ = -2 + (-3) = -5.",
        "a₁ = -1, a₂ = -1 + 1/2 = -1/2, a₃ = -1/2 + 1/2 = 0, a₄ = 0 + 1/2 = 1/2.",
        "a₁ = -1.25, a₂ = -1.25 + (-0.25) = -1.50, a₃ = -1.75, a₄ = -2.00."
    ]

    for idx, (params, opts, c_idx, expl) in enumerate(q2_data):
        blocks.append(make_quiz(
            f"C10M_CH5_EX5.1_Q2_p{idx+1}",
            f"Exercise 5.1 (Q2.{idx+1}): Write the first four terms of the AP, when the first term 'a' and the common difference 'd' are given as follows: {params}",
            f"प्रश्नावली 5.1 (Q2.{idx+1}): दी हुई AP के प्रथम चार पद लिखिए, जबकि प्रथम पद 'a' और सार्व अंतर 'd' निम्नलिखित हैं: {params}",
            f"સ્વાધ્યાય 5.1 (Q2.{idx+1}): જ્યારે પ્રથમ પદ 'a' અને સામાન્ય તફાવત 'd' ના મૂલ્યો નીચે પ્રમાણે હોય ત્યારે AP ના પ્રથમ ચાર પદો લખો: {params}",
            opts, opts, opts,
            c_idx, expl, q2_data_hi[idx], q2_data_gu[idx],
            bloom="Apply", diff="Beginner"
        ))

    # =========================================================================
    # EXERCISE 5.1 - QUESTION 3 (First Term 'a' and Common Difference 'd', 4 Subparts)
    # =========================================================================
    q3_data = [
        ("3, 1, -1, -3, ...", ["a = 3, d = -2", "a = 3, d = 2", "a = -3, d = -2", "a = 1, d = -2"], 0, "a = 3, d = 1 - 3 = -2."),
        ("-5, -1, 3, 7, ...", ["a = -5, d = 4", "a = -5, d = -4", "a = -1, d = 4", "a = 7, d = 4"], 0, "a = -5, d = -1 - (-5) = -1 + 5 = 4."),
        ("1/3, 5/3, 9/3, 13/3, ...", ["a = 1/3, d = 4/3", "a = 1/3, d = 5/3", "a = 5/3, d = 4/3", "a = 1/3, d = -4/3"], 0, "a = 1/3, d = 5/3 - 1/3 = 4/3."),
        ("0.6, 1.7, 2.8, 3.9, ...", ["a = 0.6, d = 1.1", "a = 0.6, d = 0.9", "a = 1.7, d = 1.1", "a = 0.6, d = -1.1"], 0, "a = 0.6, d = 1.7 - 0.6 = 1.1.")
    ]
    q3_data_hi = [
        "a = 3, d = 1 - 3 = -2।",
        "a = -5, d = -1 - (-5) = -1 + 5 = 4।",
        "a = 1/3, d = 5/3 - 1/3 = 4/3।",
        "a = 0.6, d = 1.7 - 0.6 = 1.1।"
    ]
    q3_data_gu = [
        "a = 3, d = 1 - 3 = -2.",
        "a = -5, d = -1 - (-5) = -1 + 5 = 4.",
        "a = 1/3, d = 5/3 - 1/3 = 4/3.",
        "a = 0.6, d = 1.7 - 0.6 = 1.1."
    ]

    for idx, (seq, opts, c_idx, expl) in enumerate(q3_data):
        blocks.append(make_quiz(
            f"C10M_CH5_EX5.1_Q3_p{idx+1}",
            f"Exercise 5.1 (Q3.{idx+1}): For the following AP, write the first term 'a' and the common difference 'd': {seq}",
            f"प्रश्नावली 5.1 (Q3.{idx+1}): निम्नलिखित में से प्रत्येक AP के लिए प्रथम पद तथा सार्व अंतर लिखिए: {seq}",
            f"સ્વાધ્યાય 5.1 (Q3.{idx+1}): નીચે આપેલ સમાંતર શ્રેણી માટે પ્રથમ પદ અને સામાન્ય તફાવત શોધો: {seq}",
            opts, opts, opts,
            c_idx, expl, q3_data_hi[idx], q3_data_gu[idx],
            bloom="Understand", diff="Beginner"
        ))

    # =========================================================================
    # EXERCISE 5.1 - QUESTION 4 (All 15 Subparts: Check AP, find d, write 3 terms)
    # =========================================================================
    q4_data = [
        ("2, 4, 8, 16, ...", "Not an AP", ["Not an AP (differences 2, 4, 8 are not equal)", "AP with d = 2; next terms: 18, 20, 22", "AP with d = 4; next terms: 20, 24, 28", "AP with d = 8; next terms: 24, 32, 40"], ["AP नहीं है (अंतर 2, 4, 8 समान नहीं हैं)", "AP है जहाँ d = 2; अगले पद: 18, 20, 22", "AP है जहाँ d = 4; अगले पद: 20, 24, 28", "AP है जहाँ d = 8; अगले पद: 24, 32, 40"], ["AP નથી (તફાવત 2, 4, 8 સમાન નથી)", "AP છે જ્યાં d = 2; આગળના પદો: 18, 20, 22", "AP છે જ્યાં d = 4; આગળના પદો: 20, 24, 28", "AP છે જ્યાં d = 8; આગળના પદો: 24, 32, 40"], 0, "4 - 2 = 2, 8 - 4 = 4. Differences are not equal, so it is NOT an AP.", "4 - 2 = 2, 8 - 4 = 4। अंतर समान नहीं हैं, इसलिए यह AP नहीं है।", "4 - 2 = 2, 8 - 4 = 4. તફાવત સમાન નથી, તેથી તે AP નથી."),
        ("2, 5/2, 3, 7/2, ...", "AP", ["AP with d = 1/2; next three terms: 4, 9/2, 5", "Not an AP", "AP with d = 1; next three terms: 4, 5, 6", "AP with d = 1/2; next three terms: 4, 5, 6"], ["AP है जहाँ d = 1/2; अगले तीन पद: 4, 9/2, 5", "AP नहीं है", "AP है जहाँ d = 1; अगले तीन पद: 4, 5, 6", "AP है जहाँ d = 1/2; अगले तीन पद: 4, 5, 6"], ["AP છે જ્યાં d = 1/2; આગળના ત્રણ પદો: 4, 9/2, 5", "AP નથી", "AP છે જ્યાં d = 1; આગળના ત્રણ પદો: 4, 5, 6", "AP છે જ્યાં d = 1/2; આગળના ત્રણ પદો: 4, 5, 6"], 0, "5/2 - 2 = 1/2, 3 - 5/2 = 1/2, 7/2 - 3 = 1/2. Constant d = 1/2. Next terms: 7/2 + 1/2 = 4, 4 + 1/2 = 9/2, 9/2 + 1/2 = 5.", "5/2 - 2 = 1/2, 3 - 5/2 = 1/2. अंतर स्थिर d = 1/2 है। अगले पद: 4, 9/2, 5।", "5/2 - 2 = 1/2, 3 - 5/2 = 1/2. સામાન્ય તફાવત d = 1/2 છે. આગળના પદો: 4, 9/2, 5."),
        ("-1.2, -3.2, -5.2, -7.2, ...", "AP", ["AP with d = -2; next three terms: -9.2, -11.2, -13.2", "AP with d = 2; next three terms: -5.2, -3.2, -1.2", "Not an AP", "AP with d = -2; next three terms: -8.2, -9.2, -10.2"], ["AP है जहाँ d = -2; अगले तीन पद: -9.2, -11.2, -13.2", "AP है जहाँ d = 2; अगले तीन पद: -5.2, -3.2, -1.2", "AP नहीं है", "AP है जहाँ d = -2; अगले तीन पद: -8.2, -9.2, -10.2"], ["AP છે જ્યાં d = -2; આગળના ત્રણ પદો: -9.2, -11.2, -13.2", "AP છે જ્યાં d = 2; આગળના ત્રણ પદો: -5.2, -3.2, -1.2", "AP નથી", "AP છે જ્યાં d = -2; આગળના ત્રણ પદો: -8.2, -9.2, -10.2"], 0, "-3.2 - (-1.2) = -2, -5.2 - (-3.2) = -2. So d = -2. Next terms: -7.2 + (-2) = -9.2, -11.2, -13.2.", "-3.2 - (-1.2) = -2। d = -2 स्थिर है। अगले पद: -9.2, -11.2, -13.2।", "-3.2 - (-1.2) = -2. d = -2 અચળ છે. આગળના પદો: -9.2, -11.2, -13.2."),
        ("-10, -6, -2, 2, ...", "AP", ["AP with d = 4; next three terms: 6, 10, 14", "AP with d = -4; next three terms: -2, -6, -10", "Not an AP", "AP with d = 4; next three terms: 4, 8, 12"], ["AP है जहाँ d = 4; अगले तीन पद: 6, 10, 14", "AP है जहाँ d = -4; अगले तीन पद: -2, -6, -10", "AP नहीं है", "AP है जहाँ d = 4; अगले तीन पद: 4, 8, 12"], ["AP છે જ્યાં d = 4; આગળના ત્રણ પદો: 6, 10, 14", "AP છે જ્યાં d = -4; આગળના ત્રણ પદો: -2, -6, -10", "AP નથી", "AP છે જ્યાં d = 4; આગળના ત્રણ પદો: 4, 8, 12"], 0, "-6 - (-10) = 4, -2 - (-6) = 4, 2 - (-2) = 4. d = 4. Next terms: 2+4=6, 6+4=10, 10+4=14.", "-6 - (-10) = 4, -2 - (-6) = 4। d = 4 स्थिर है। अगले पद: 6, 10, 14।", "-6 - (-10) = 4, -2 - (-6) = 4. d = 4 અચળ છે. આગળના પદો: 6, 10, 14."),
        ("3, 3+√2, 3+2√2, 3+3√2, ...", "AP", ["AP with d = √2; next three terms: 3+4√2, 3+5√2, 3+6√2", "Not an AP", "AP with d = 2; next three terms: 3+4√2, 3+5√2, 3+6√2", "AP with d = √2; next three terms: 3+5√2, 3+7√2, 3+9√2"], ["AP है जहाँ d = √2; अगले तीन पद: 3+4√2, 3+5√2, 3+6√2", "AP नहीं है", "AP है जहाँ d = 2; अगले तीन पद: 3+4√2, 3+5√2, 3+6√2", "AP है जहाँ d = √2; अगले तीन पद: 3+5√2, 3+7√2, 3+9√2"], ["AP છે જ્યાં d = √2; આગળના ત્રણ પદો: 3+4√2, 3+5√2, 3+6√2", "AP નથી", "AP છે જ્યાં d = 2; આગળના ત્રણ પદો: 3+4√2, 3+5√2, 3+6√2", "AP છે જ્યાં d = √2; આગળના ત્રણ પદો: 3+5√2, 3+7√2, 3+9√2"], 0, "(3+√2) - 3 = √2, (3+2√2) - (3+√2) = √2. Constant d = √2. Next terms: 3+4√2, 3+5√2, 3+6√2.", "(3+√2) - 3 = √2। अंतर d = √2 स्थिर है। अगले पद: 3+4√2, 3+5√2, 3+6√2।", "(3+√2) - 3 = √2. તફાવત d = √2 અચળ છે. આગળના પદો: 3+4√2, 3+5√2, 3+6√2."),
        ("0.2, 0.22, 0.222, 0.2222, ...", "Not an AP", ["Not an AP (differences 0.02, 0.002, 0.0002 are not equal)", "AP with d = 0.02", "AP with d = 0.2", "AP with d = 0.002"], ["AP नहीं है (अंतर 0.02, 0.002, 0.0002 समान नहीं हैं)", "AP है जहाँ d = 0.02", "AP है जहाँ d = 0.2", "AP है जहाँ d = 0.002"], ["AP નથી (તફાવત 0.02, 0.002, 0.0002 સમાન નથી)", "AP છે જ્યાં d = 0.02", "AP છે જ્યાં d = 0.2", "AP છે જ્યાં d = 0.002"], 0, "0.22 - 0.2 = 0.02, while 0.222 - 0.22 = 0.002. Since 0.02 ≠ 0.002, it is NOT an AP.", "0.22 - 0.2 = 0.02, जबकि 0.222 - 0.22 = 0.002। अंतर समान नहीं हैं, अतः यह AP नहीं है।", "0.22 - 0.2 = 0.02, જ્યારે 0.222 - 0.22 = 0.002. તફાવત સમાન નથી, તેથી તે AP નથી."),
        ("0, -4, -8, -12, ...", "AP", ["AP with d = -4; next three terms: -16, -20, -24", "AP with d = 4; next three terms: -8, -4, 0", "Not an AP", "AP with d = -4; next three terms: -14, -18, -22"], ["AP है जहाँ d = -4; अगले तीन पद: -16, -20, -24", "AP है जहाँ d = 4; अगले तीन पद: -8, -4, 0", "AP नहीं है", "AP है जहाँ d = -4; अगले तीन पद: -14, -18, -22"], ["AP છે જ્યાં d = -4; આગળના ત્રણ પદો: -16, -20, -24", "AP છે જ્યાં d = 4; આગળના ત્રણ પદો: -8, -4, 0", "AP નથી", "AP છે જ્યાં d = -4; આગળના ત્રણ પદો: -14, -18, -22"], 0, "-4 - 0 = -4, -8 - (-4) = -4. d = -4. Next terms: -12 + (-4) = -16, -20, -24.", "-4 - 0 = -4, -8 - (-4) = -4। d = -4 स्थिर है। अगले पद: -16, -20, -24।", "-4 - 0 = -4, -8 - (-4) = -4. d = -4 અચળ છે. આગળના પદો: -16, -20, -24."),
        ("-1/2, -1/2, -1/2, -1/2, ...", "AP", ["AP with d = 0; next three terms: -1/2, -1/2, -1/2", "Not an AP", "AP with d = 1/2; next three terms: 0, 1/2, 1", "AP with d = -1/2; next three terms: -1, -3/2, -2"], ["AP है जहाँ d = 0; अगले तीन पद: -1/2, -1/2, -1/2", "AP नहीं है", "AP है जहाँ d = 1/2; अगले तीन पद: 0, 1/2, 1", "AP है जहाँ d = -1/2; अगले तीन पद: -1, -3/2, -2"], ["AP છે જ્યાં d = 0; આગળના ત્રણ પદો: -1/2, -1/2, -1/2", "AP નથી", "AP છે જ્યાં d = 1/2; આગળના ત્રણ પદો: 0, 1/2, 1", "AP છે જ્યાં d = -1/2; આગળના ત્રણ પદો: -1, -3/2, -2"], 0, "-1/2 - (-1/2) = 0. Common difference is 0. Next terms: -1/2, -1/2, -1/2.", "-1/2 - (-1/2) = 0। सार्व अंतर 0 स्थिर है। अगले पद: -1/2, -1/2, -1/2।", "-1/2 - (-1/2) = 0. સામાન્ય તફાવત 0 અચળ છે. આગળના પદો: -1/2, -1/2, -1/2."),
        ("1, 3, 9, 27, ...", "Not an AP", ["Not an AP (differences 2, 6, 18 are not equal)", "AP with d = 3", "AP with d = 2", "AP with d = 6"], ["AP नहीं है (अंतर 2, 6, 18 समान नहीं हैं)", "AP है जहाँ d = 3", "AP है जहाँ d = 2", "AP है जहाँ d = 6"], ["AP નથી (તફાવત 2, 6, 18 સમાન નથી)", "AP છે જ્યાં d = 3", "AP છે જ્યાં d = 2", "AP છે જ્યાં d = 6"], 0, "3 - 1 = 2, while 9 - 3 = 6. Differences are not equal, so it is NOT an AP.", "3 - 1 = 2, जबकि 9 - 3 = 6। अंतर समान नहीं हैं, अतः यह AP नहीं है।", "3 - 1 = 2, જ્યારે 9 - 3 = 6. તફાવત સમાન નથી, તેથી તે AP નથી."),
        ("a, 2a, 3a, 4a, ...", "AP", ["AP with d = a; next three terms: 5a, 6a, 7a", "Not an AP", "AP with d = 2a; next three terms: 6a, 8a, 10a", "AP with d = a²; next three terms: 5a, 6a, 7a"], ["AP है जहाँ d = a; अगले तीन पद: 5a, 6a, 7a", "AP नहीं है", "AP है जहाँ d = 2a; अगले तीन पद: 6a, 8a, 10a", "AP है जहाँ d = a²; अगले तीन पद: 5a, 6a, 7a"], ["AP છે જ્યાં d = a; આગળના ત્રણ પદો: 5a, 6a, 7a", "AP નથી", "AP છે જ્યાં d = 2a; આગળના ત્રણ પદો: 6a, 8a, 10a", "AP છે જ્યાં d = a²; આગળના ત્રણ પદો: 5a, 6a, 7a"], 0, "2a - a = a, 3a - 2a = a. Constant difference d = a. Next terms: 5a, 6a, 7a.", "2a - a = a, 3a - 2a = a। सार्व अंतर d = a स्थिर है। अगले पद: 5a, 6a, 7a।", "2a - a = a, 3a - 2a = a. સામાન્ય તફાવત d = a અચળ છે. આગળના પદો: 5a, 6a, 7a."),
        ("a, a², a³, a⁴, ...", "Not an AP", ["Not an AP (differences a² - a ≠ a³ - a²)", "AP with d = a", "AP with d = a²", "AP with d = 2a"], ["AP नहीं है (अंतर a² - a ≠ a³ - a²)", "AP है जहाँ d = a", "AP है जहाँ d = a²", "AP है जहाँ d = 2a"], ["AP નથી (તફાવત a² - a ≠ a³ - a²)", "AP છે જ્યાં d = a", "AP છે જ્યાં d = a²", "AP છે જ્યાં d = 2a"], 0, "a² - a = a(a - 1) while a³ - a² = a²(a - 1). Unless a = 0 or 1, these are unequal. Thus it is NOT an AP.", "a² - a ≠ a³ - a²। अंतर समान नहीं हैं, अतः यह AP नहीं है।", "a² - a ≠ a³ - a². તફાવત સમાન નથી, તેથી તે AP નથી."),
        ("√2, √8, √18, √32, ...", "AP", ["AP with d = √2; next three terms: √50, √72, √98", "Not an AP", "AP with d = √6; next three terms: √40, √48, √56", "AP with d = 2; next three terms: √50, √72, √98"], ["AP है जहाँ d = √2; अगले तीन पद: √50, √72, √98", "AP नहीं है", "AP है जहाँ d = √6; अगले तीन पद: √40, √48, √56", "AP है जहाँ d = 2; अगले तीन पद: √50, √72, √98"], ["AP છે જ્યાં d = √2; આગળના ત્રણ પદો: √50, √72, √98", "AP નથી", "AP છે જ્યાં d = √6; આગળના ત્રણ પદો: √40, √48, √56", "AP છે જ્યાં d = 2; આગળના ત્રણ પદો: √50, √72, √98"], 0, "Simplify terms: √2, 2√2, 3√2, 4√2... d = 2√2 - √2 = √2. Next terms: 5√2 = √50, 6√2 = √72, 7√2 = √98.", "पदों को सरल करें: √2, 2√2, 3√2, 4√2... d = √2 स्थिर है। अगले पद: 5√2 = √50, 6√2 = √72, 7√2 = √98।", "પદોનું સાદુરૂપ આપો: √2, 2√2, 3√2, 4√2... d = √2 અચળ છે. આગળના પદો: 5√2 = √50, 6√2 = √72, 7√2 = √98."),
        ("√3, √6, √9, √12, ...", "Not an AP", ["Not an AP (differences √6 - √3 ≠ √9 - √6)", "AP with d = √3", "AP with d = 3", "AP with d = √6"], ["AP नहीं है (अंतर √6 - √3 ≠ √9 - √6)", "AP है जहाँ d = √3", "AP है जहाँ d = 3", "AP है जहाँ d = √6"], ["AP નથી (તફાવત √6 - √3 ≠ √9 - √6)", "AP છે જ્યાં d = √3", "AP છે જ્યાં d = 3", "AP છે જ્યાં d = √6"], 0, "√6 - √3 ≠ √9 - √6 (which is 3 - √6). The differences are unequal, so it is NOT an AP.", "√6 - √3 ≠ 3 - √6। अंतर समान नहीं हैं, अतः यह AP नहीं है।", "√6 - √3 ≠ 3 - √6. તફાવત સમાન નથી, તેથી તે AP નથી."),
        ("1², 3², 5², 7², ...", "Not an AP", ["Not an AP (1, 9, 25, 49 have differences 8, 16, 24)", "AP with d = 8", "AP with d = 2", "AP with d = 16"], ["AP नहीं है (1, 9, 25, 49 के अंतर 8, 16, 24 समान नहीं हैं)", "AP है जहाँ d = 8", "AP है जहाँ d = 2", "AP है जहाँ d = 16"], ["AP નથી (1, 9, 25, 49 ના તફાવત 8, 16, 24 સમાન નથી)", "AP છે જ્યાં d = 8", "AP છે જ્યાં d = 2", "AP છે જ્યાં d = 16"], 0, "1² = 1, 3² = 9, 5² = 25, 7² = 49. Differences: 9-1=8, 25-9=16. Since 8 ≠ 16, it is NOT an AP.", "1, 9, 25, 49... अंतर 8, 16 समान नहीं हैं। अतः यह AP नहीं है।", "1, 9, 25, 49... તફાવત 8, 16 સમાન નથી. તેથી તે AP નથી."),
        ("1², 5², 7², 73, ...", "AP", ["AP with d = 24; next three terms: 97, 121, 145", "Not an AP", "AP with d = 24; next three terms: 97, 119, 143", "AP with d = 12; next three terms: 85, 97, 109"], ["AP है जहाँ d = 24; अगले तीन पद: 97, 121, 145", "AP नहीं है", "AP है जहाँ d = 24; अगले तीन पद: 97, 119, 143", "AP है जहाँ d = 12; अगले तीन पद: 85, 97, 109"], ["AP છે જ્યાં d = 24; આગળના ત્રણ પદો: 97, 121, 145", "AP નથી", "AP છે જ્યાં d = 24; આગળના ત્રણ પદો: 97, 119, 143", "AP છે જ્યાં d = 12; આગળના ત્રણ પદો: 85, 97, 109"], 0, "1² = 1, 5² = 25, 7² = 49, 73... Differences: 25-1=24, 49-25=24, 73-49=24. Constant d = 24! Next terms: 73+24=97, 97+24=121, 121+24=145.", "1, 25, 49, 73... अंतर 25-1=24, 49-25=24, 73-49=24 स्थिर है (d = 24)। अगले पद: 97, 121, 145।", "1, 25, 49, 73... તફાવત 25-1=24, 49-25=24, 73-49=24 અચળ છે (d = 24). આગળના પદો: 97, 121, 145.")
    ]

    for idx, (seq, _, opts_en, opts_hi, opts_gu, c_idx, expl_en, expl_hi, expl_gu) in enumerate(q4_data):
        blocks.append(make_quiz(
            f"C10M_CH5_EX5.1_Q4_p{idx+1}",
            f"Exercise 5.1 (Q4.{idx+1}): Which of the following are APs? If they form an AP, find the common difference 'd' and write three more terms: {seq}",
            f"प्रश्नावली 5.1 (Q4.{idx+1}): निम्नलिखित में से कौन-कौन AP हैं? यदि कोई AP है, तो इसका सार्व अंतर 'd' ज्ञात कीजिए और इनके तीन और पद लिखिए: {seq}",
            f"સ્વાધ્યાય 5.1 (Q4.{idx+1}): નીચેનામાંથી કઈ શ્રેણી સમાંતર શ્રેણી છે? જો તે સમાંતર શ્રેણી બનાવે, તો સામાન્ય તફાવત 'd' શોધો અને પછીના ત્રણ પદો લખો: {seq}",
            opts_en, opts_hi, opts_gu,
            c_idx, expl_en, expl_hi, expl_gu,
            bloom="Evaluate", diff="Intermediate"
        ))

    return blocks

def get_part2_blocks():
    blocks = []

    # =========================================================================
    # PART 2: THE nth TERM OF AN AP (THEORY & TEACHER TIP)
    # =========================================================================
    blocks.append({
        "id": "C10M_CH5_PART2_THEORY",
        "type": "theory",
        "title": "The nth Term of an AP (General Term)",
        "body": "Let $a_1, a_2, a_3, \\dots, a_n$ be an AP with first term $a$ and common difference $d$.\n\nNotice the pattern:\n- First term: $a_1 = a = a + (1 - 1)d$\n- Second term: $a_2 = a + d = a + (2 - 1)d$\n- Third term: $a_3 = a_2 + d = (a + d) + d = a + 2d = a + (3 - 1)d$\n- Fourth term: $a_4 = a_3 + d = (a + 2d) + d = a + 3d = a + (4 - 1)d$\n\nFollowing this pattern, the **nth term ($a_n$)** of an AP is given by:\n$$\\mathbf{a_n = a + (n - 1)d}$$\n\n**Key Variables:**\n- **a:** First term\n- **d:** Common difference ($a_{k+1} - a_k$)\n- **n:** Term number / index (MUST be a positive integer: $n \\in \\{1, 2, 3, \\dots\\}$)\n- **a_n:** The value of the nth term (also called the **general term**). If there are $n$ terms in an AP, $a_n$ represents the last term, often denoted by **l**.\n\n**nth Term from the End:**\nIf an AP has last term $l$ and common difference $d$, the nth term from the end is:\n$$\\mathbf{a_n^{\\text{end}} = l - (n - 1)d}$$",
        "title_hi": "AP का nवाँ पद (व्यापक पद)",
        "body_hi": "मान लीजिए $a_1, a_2, a_3, \\dots, a_n$ एक AP है जिसका प्रथम पद $a$ और सार्व अंतर $d$ है।\n\nपैटर्न पर ध्यान दें:\n- पहला पद: $a_1 = a = a + (1 - 1)d$\n- दूसरा पद: $a_2 = a + d = a + (2 - 1)d$\n- तीसरा पद: $a_3 = a + 2d = a + (3 - 1)d$\n\nइस प्रतिरूप का अनुसरण करते हुए, AP का **nवाँ पद ($a_n$)** निम्न सूत्र द्वारा दिया जाता है:\n$$\\mathbf{a_n = a + (n - 1)d}$$\n\n**प्रमुख चर:**\n- **a:** प्रथम पद\n- **d:** सार्व अंतर\n- **n:** पदों की संख्या (हमेशा एक धनात्मक पूर्णांक $1, 2, 3, \\dots$ होना चाहिए)\n- **a_n:** nवाँ पद (व्यापक पद), इसे अंतिम पद **l** भी कहा जाता है।\n\n**अंतिम से nवाँ पद:**\nयदि अंतिम पद $l$ और सार्व अंतर $d$ हो, तो अंतिम से nवाँ पद होता है:\n$$\\mathbf{a_n^{\\text{अंत}}} = l - (n - 1)d$$",
        "title_gu": "AP નું nમું પદ (વ્યાપક પદ)",
        "body_gu": "ધારો કે $a_1, a_2, a_3, \\dots, a_n$ એ પ્રથમ પદ $a$ અને સામાન્ય તફાવત $d$ વાળી AP છે.\n\nપેટર્ન જુઓ:\n- પ્રથમ પદ: $a_1 = a = a + (1 - 1)d$\n- બીજું પદ: $a_2 = a + d = a + (2 - 1)d$\n- ત્રીજું પદ: $a_3 = a + 2d = a + (3 - 1)d$\n\nઆ પેટર્નને અનુસરતા, AP નું **nમું પદ ($a_n$)** નીચેના સૂત્ર વડે મળે છે:\n$$\\mathbf{a_n = a + (n - 1)d}$$\n\n**મુખ્ય ચલો:**\n- **a:** પ્રથમ પદ\n- **d:** સામાન્ય તફાવત\n- **n:** પદનો ક્રમાંક (હંમેશા ધન પૂર્ણાંક $1, 2, 3, \\dots$ જ હોવો જોઈએ)\n- **a_n:** nમું પદ (વ્યાપક પદ), જો શાંત AP હોય તો તેને છેલ્લું પદ **l** પણ કહેવાય છે.\n\n**છેડેથી nમું પદ:**\nજો છેલ્લું પદ $l$ હોય, તો છેડેથી nમું પદ:\n$$\\mathbf{a_n^{\\text{છેડેથી}}} = l - (n - 1)d$$",
        "bloom": "Understand",
        "difficulty": "Beginner",
        "estimated_minutes": 3
    })

    blocks.append({
        "id": "C10M_CH5_PART2_TIP",
        "type": "teacher_tip",
        "title": "Teacher Tip: 'n' Must ALWAYS be a Natural Number!",
        "body": "Whenever a question asks: *'Is -150 a term of the AP?'* or *'Which term is 78?'*, set $a_n = 78$ and solve for $n$.\n\n**Critical Test:**\n- If $n$ is a positive integer (like $n = 16$), the term belongs to the AP!\n- If $n$ is a fraction (like $n = 54\\frac{2}{3}$) or negative (like $n = -4$), then that number CANNOT be a term of the AP, because there is no '54.67th term' in any sequence!",
        "title_hi": "शिक्षक युक्ति: 'n' हमेशा एक प्राकृत संख्या होना चाहिए!",
        "body_hi": "जब भी कोई प्रश्न पूछे: *'क्या -150 इस AP का पद है?'* या *'कौन सा पद 78 है?'*, तो $a_n = 78$ रखें और $n$ का मान ज्ञात करें।\n\n**महत्वपूर्ण कसौटी:**\n- यदि $n$ एक धनात्मक पूर्णांक (जैसे $n = 16$) आता है, तो पद AP का हिस्सा है!\n- यदि $n$ भिन्न (जैसे $n = 54\\frac{2}{3}$) या ऋणात्मक आता है, तो वह संख्या AP का पद नहीं हो सकती, क्योंकि किसी अनुक्रम में '54.67वाँ पद' जैसा कुछ नहीं होता!",
        "title_gu": "શિક્ષકની સલાહ: 'n' હંમેશા પ્રાકૃતિક સંખ્યા જ હોવી જોઈએ!",
        "body_gu": "જ્યારે પણ કોઈ પ્રશ્ન પૂછે: *'શું -150 આ AP નું પદ છે?'* અથવા *'કયું પદ 78 છે?'*, ત્યારે $a_n = 78$ મૂકીને $n$ ની કિંમત શોધો.\n\n**મહત્વપૂર્ણ કસોટી:**\n- જો $n$ ધન પૂર્ણાંક (જેમ કે $n = 16$) આવે, તો તે પદ AP માં છે!\n- જો $n$ અપૂર્ણાંક (જેમ કે $n = 54\\frac{2}{3}$) કે ઋણ આવે, તો તે સંખ્યા AP નું પદ હોઈ શકે નહીં, કારણ કે કોઈ પણ શ્રેણીમાં '54.67મું પદ' હોતું નથી!",
        "bloom": "Apply",
        "difficulty": "Beginner",
        "estimated_minutes": 2
    })

    # =========================================================================
    # EXERCISE 5.2 - QUESTION 1 (Fill in Blanks Table, 5 Subparts)
    # =========================================================================
    ex5_2_q1_data = [
        ("a = 7, d = 3, n = 8, find a_n", ["a_n = 28", "a_n = 31", "a_n = 24", "a_n = 21"], 0, "a_n = a + (n - 1)d = 7 + (8 - 1) × 3 = 7 + 21 = 28."),
        ("a = -18, n = 10, a_n = 0, find d", ["d = 2", "d = -2", "d = 1.8", "d = 9"], 0, "a_n = a + (n - 1)d => 0 = -18 + (10 - 1)d => 9d = 18 => d = 2."),
        ("d = -3, n = 18, a_n = -5, find a", ["a = 46", "a = -46", "a = 56", "a = 49"], 0, "a_n = a + (n - 1)d => -5 = a + (18 - 1)(-3) => -5 = a - 51 => a = 46."),
        ("a = -18.9, d = 2.5, a_n = 3.6, find n", ["n = 10", "n = 9", "n = 11", "n = 8"], 0, "a_n = a + (n - 1)d => 3.6 = -18.9 + (n - 1)(2.5) => (n - 1)(2.5) = 22.5 => n - 1 = 9 => n = 10."),
        ("a = 3.5, d = 0, n = 105, find a_n", ["a_n = 3.5", "a_n = 0", "a_n = 105", "a_n = 367.5"], 0, "a_n = a + (n - 1)d = 3.5 + (105 - 1) × 0 = 3.5.")
    ]
    ex5_2_q1_data_hi = [
        "a_n = a + (n - 1)d = 7 + (8 - 1) × 3 = 7 + 21 = 28।",
        "0 = -18 + 9d => 9d = 18 => d = 2।",
        "-5 = a + 17(-3) => -5 = a - 51 => a = 46।",
        "3.6 = -18.9 + (n - 1)(2.5) => 22.5 = (n - 1)(2.5) => n - 1 = 9 => n = 10।",
        "a_n = 3.5 + 104 × 0 = 3.5।"
    ]
    ex5_2_q1_data_gu = [
        "a_n = a + (n - 1)d = 7 + (8 - 1) × 3 = 7 + 21 = 28.",
        "0 = -18 + 9d => 9d = 18 => d = 2.",
        "-5 = a + 17(-3) => -5 = a - 51 => a = 46.",
        "3.6 = -18.9 + (n - 1)(2.5) => 22.5 = (n - 1)(2.5) => n - 1 = 9 => n = 10.",
        "a_n = 3.5 + 104 × 0 = 3.5."
    ]

    for idx, (params, opts, c_idx, expl) in enumerate(ex5_2_q1_data):
        blocks.append(make_quiz(
            f"C10M_CH5_EX5.2_Q1_p{idx+1}",
            f"Exercise 5.2 (Q1.{idx+1}): Fill in the blank in the table, given that 'a' is the first term, 'd' the common difference and a_n the nth term of the AP: {params}",
            f"प्रश्नावली 5.2 (Q1.{idx+1}): निम्नलिखित सारणी में, रिक्त स्थानों को भरिए, जहाँ AP का प्रथम पद 'a', सार्व अंतर 'd' और nवाँ पद a_n है: {params}",
            f"સ્વાધ્યાય 5.2 (Q1.{idx+1}): નીચેના કોષ્ટકમાં ખાલી જગ્યા પૂરો, જ્યાં AP નું પ્રથમ પદ 'a', સામાન્ય તફાવત 'd' અને nમું પદ a_n છે: {params}",
            opts, opts, opts,
            c_idx, expl, ex5_2_q1_data_hi[idx], ex5_2_q1_data_gu[idx],
            bloom="Apply", diff="Beginner"
        ))

    # =========================================================================
    # EXERCISE 5.2 - QUESTION 2 (Choose Correct Choice, 2 Subparts)
    # =========================================================================
    # Q2.1
    blocks.append(make_quiz(
        "C10M_CH5_EX5.2_Q2_p1",
        "Exercise 5.2 (Q2.i): Choose the correct choice: 30th term of the AP: 10, 7, 4, ... is:",
        "प्रश्नावली 5.2 (Q2.i): सही उत्तर चुनिए: AP: 10, 7, 4, ... का 30वाँ पद है:",
        "સ્વાધ્યાય 5.2 (Q2.i): સાચો વિકલ્પ પસંદ કરો: સમાંતર શ્રેણી 10, 7, 4, ... નું 30મું પદ છે:",
        ["-77", "97", "77", "-87"],
        ["-77", "97", "77", "-87"],
        ["-77", "97", "77", "-87"],
        0,
        "Here a = 10, d = 7 - 10 = -3, n = 30. a₃₀ = a + (30 - 1)d = 10 + 29(-3) = 10 - 87 = -77.",
        "यहाँ a = 10, d = 7 - 10 = -3, n = 30। a₃₀ = 10 + 29(-3) = 10 - 87 = -77।",
        "અહીં a = 10, d = 7 - 10 = -3, n = 30. a₃₀ = 10 + 29(-3) = 10 - 87 = -77."
    ))

    # Q2.2
    blocks.append(make_quiz(
        "C10M_CH5_EX5.2_Q2_p2",
        "Exercise 5.2 (Q2.ii): Choose the correct choice: 11th term of the AP: -3, -1/2, 2, ... is:",
        "प्रश्नावली 5.2 (Q2.ii): सही उत्तर चुनिए: AP: -3, -1/2, 2, ... का 11वाँ पद है:",
        "સ્વાધ્યાય 5.2 (Q2.ii): સાચો વિકલ્પ પસંદ કરો: સમાંતર શ્રેણી -3, -1/2, 2, ... નું 11મું પદ છે:",
        ["22", "28", "-38", "-46 1/2"],
        ["22", "28", "-38", "-46 1/2"],
        ["22", "28", "-38", "-46 1/2"],
        0,
        "Here a = -3, d = -1/2 - (-3) = 5/2, n = 11. a₁₁ = -3 + (11 - 1)(5/2) = -3 + 10(5/2) = -3 + 25 = 22.",
        "यहाँ a = -3, d = -1/2 - (-3) = 5/2, n = 11। a₁₁ = -3 + 10(5/2) = -3 + 25 = 22।",
        "અહીં a = -3, d = -1/2 - (-3) = 5/2, n = 11. a₁₁ = -3 + 10(5/2) = -3 + 25 = 22."
    ))

    # =========================================================================
    # EXERCISE 5.2 - QUESTION 3 (Missing Box Terms, 5 Subparts)
    # =========================================================================
    q3_box_data = [
        ("2, [ ? ], 26", ["14", "12", "16", "18"], 0, "In an AP, middle term is the arithmetic mean: (2 + 26) / 2 = 14. (Or 2 + 2d = 26 => 2d = 24 => d = 12 => 2 + 12 = 14)."),
        ("[ ? ], 13, [ ? ], 3", ["18 and 8", "15 and 9", "16 and 10", "20 and 6"], 0, "a + d = 13 and a + 3d = 3. Subtracting: 2d = -10 => d = -5. Then a = 13 - (-5) = 18. Third term = 13 + (-5) = 8."),
        ("5, [ ? ], [ ? ], 9 1/2", ["6 1/2 and 8", "6 and 7 1/2", "7 and 8 1/2", "6 1/2 and 7 1/2"], 0, "a = 5, a₄ = 19/2 => a + 3d = 19/2 => 3d = 19/2 - 5 = 9/2 => d = 3/2. Second term = 5 + 3/2 = 6 1/2. Third term = 6 1/2 + 3/2 = 8."),
        ("-4, [ ? ], [ ? ], [ ? ], [ ? ], 6", ["-2, 0, 2, 4", "-2, -1, 0, 1", "-1, 1, 3, 5", "-3, -2, -1, 0"], 0, "a = -4, a₆ = 6 => a + 5d = 6 => -4 + 5d = 6 => 5d = 10 => d = 2. Missing terms: -4+2 = -2, 0, 2, 4."),
        ("[ ? ], 38, [ ? ], [ ? ], [ ? ], -22", ["53, 23, 8, -7", "50, 26, 14, 2", "53, 20, 7, -6", "48, 28, 18, 8"], 0, "a + d = 38, a + 5d = -22. Subtracting: 4d = -60 => d = -15. a = 38 - (-15) = 53. Terms: 53, 23, 8, -7.")
    ]
    q3_box_data_hi = [
        "AP में मध्य पद समांतर माध्य होता है: (2 + 26) / 2 = 14।",
        "a + d = 13 और a + 3d = 3। घटाने पर: 2d = -10 => d = -5। a = 18। तीसरा पद = 18 + 2(-5) = 8।",
        "a = 5, a + 3d = 19/2 => 3d = 9/2 => d = 3/2। पद: 5 + 3/2 = 6 1/2 और 8।",
        "a = -4, a + 5d = 6 => 5d = 10 => d = 2। लुप्त पद: -2, 0, 2, 4।",
        "a + d = 38 और a + 5d = -22। घटाने पर: 4d = -60 => d = -15, a = 53। पद: 53, 23, 8, -7।"
    ]
    q3_box_data_gu = [
        "AP માં મધ્યમ પદ સમાંતર મધ્યક છે: (2 + 26) / 2 = 14.",
        "a + d = 13 અને a + 3d = 3. બાદબાકી કરતા: 2d = -10 => d = -5. a = 18. ત્રીજું પદ = 8.",
        "a = 5, a + 3d = 19/2 => 3d = 9/2 => d = 3/2. પદો: 6 1/2 અને 8.",
        "a = -4, a + 5d = 6 => 5d = 10 => d = 2. ખૂટતા પદો: -2, 0, 2, 4.",
        "a + d = 38 અને a + 5d = -22. બાદબાકી કરતા: 4d = -60 => d = -15, a = 53. પદો: 53, 23, 8, -7."
    ]

    for idx, (seq, opts, c_idx, expl) in enumerate(q3_box_data):
        blocks.append(make_quiz(
            f"C10M_CH5_EX5.2_Q3_p{idx+1}",
            f"Exercise 5.2 (Q3.{idx+1}): In the following AP, find the missing terms in the boxes: {seq}",
            f"प्रश्नावली 5.2 (Q3.{idx+1}): निम्नलिखित समांतर श्रेढ़ी में, रिक्त खानों के पदों को ज्ञात कीजिए: {seq}",
            f"સ્વાધ્યાય 5.2 (Q3.{idx+1}): નીચેની સમાંતર શ્રેણીમાં ખાલી ખાનાના પદો શોધો: {seq}",
            opts, opts, opts,
            c_idx, expl, q3_box_data_hi[idx], q3_box_data_gu[idx],
            bloom="Apply", diff="Intermediate"
        ))

    # =========================================================================
    # EXERCISE 5.2 - QUESTIONS 4 to 20 (Complete Syllabus)
    # =========================================================================
    # Q4
    blocks.append(make_quiz(
        "C10M_CH5_EX5.2_Q4",
        "Exercise 5.2 (Q4): Which term of the AP: 3, 8, 13, 18, ... is 78?",
        "प्रश्नावली 5.2 (Q4): AP: 3, 8, 13, 18, ... का कौन सा पद 78 है?",
        "સ્વાધ્યાય 5.2 (Q4): સમાંતર શ્રેણી 3, 8, 13, 18, ... નું કેટલામું પદ 78 થાય?",
        ["16th term", "15th term", "17th term", "14th term"],
        ["16वाँ पद", "15वाँ पद", "17वाँ पद", "14वाँ पद"],
        ["16મું પદ", "15મું પદ", "17મું પદ", "14મું પદ"],
        0,
        "Here a = 3, d = 8 - 3 = 5, a_n = 78. Formula: a_n = a + (n - 1)d => 78 = 3 + (n - 1)5 => 75 = 5(n - 1) => n - 1 = 15 => n = 16.",
        "यहाँ a = 3, d = 5, a_n = 78। सूत्र: a + (n - 1)d = 78 => 3 + 5(n - 1) = 78 => 5(n - 1) = 75 => n - 1 = 15 => n = 16।",
        "અહીં a = 3, d = 5, a_n = 78. સૂત્ર: 3 + (n - 1)5 = 78 => 5(n - 1) = 75 => n - 1 = 15 => n = 16."
    ))

    # Q5.1 & Q5.2
    blocks.append(make_quiz(
        "C10M_CH5_EX5.2_Q5_p1",
        "Exercise 5.2 (Q5.i): Find the number of terms in the AP: 7, 13, 19, ..., 205",
        "प्रश्नावली 5.2 (Q5.i): निम्नलिखित समांतर श्रेढ़ी में पदों की संख्या ज्ञात कीजिए: 7, 13, 19, ..., 205",
        "સ્વાધ્યાય 5.2 (Q5.i): સમાંતર શ્રેણી 7, 13, 19, ..., 205 માં પદોની સંખ્યા શોધો:",
        ["34 terms", "33 terms", "35 terms", "36 terms"],
        ["34 पद", "33 पद", "35 पद", "36 पद"],
        ["34 પદો", "33 પદો", "35 પદો", "36 પદો"],
        0,
        "a = 7, d = 13 - 7 = 6, a_n = 205. 205 = 7 + (n - 1)6 => 6(n - 1) = 198 => n - 1 = 33 => n = 34.",
        "a = 7, d = 6, a_n = 205। 205 = 7 + 6(n - 1) => 6(n - 1) = 198 => n - 1 = 33 => n = 34 पद।",
        "a = 7, d = 6, a_n = 205. 205 = 7 + 6(n - 1) => 6(n - 1) = 198 => n - 1 = 33 => n = 34 પદો."
    ))

    blocks.append(make_quiz(
        "C10M_CH5_EX5.2_Q5_p2",
        "Exercise 5.2 (Q5.ii): Find the number of terms in the AP: 18, 15 1/2, 13, ..., -47",
        "प्रश्नावली 5.2 (Q5.ii): निम्नलिखित समांतर श्रेढ़ी में पदों की संख्या ज्ञात कीजिए: 18, 15 1/2, 13, ..., -47",
        "સ્વાધ્યાય 5.2 (Q5.ii): સમાંતર શ્રેણી 18, 15 1/2, 13, ..., -47 માં પદોની સંખ્યા શોધો:",
        ["27 terms", "26 terms", "28 terms", "25 terms"],
        ["27 पद", "26 पद", "28 पद", "25 पद"],
        ["27 પદો", "26 પદો", "28 પદો", "25 પદો"],
        0,
        "a = 18, d = 31/2 - 18 = -5/2, a_n = -47. -47 = 18 + (n - 1)(-5/2) => -65 = -(5/2)(n - 1) => n - 1 = 26 => n = 27.",
        "a = 18, d = -5/2, a_n = -47। -47 = 18 - 5/2(n - 1) => 65 = 5/2(n - 1) => n - 1 = 26 => n = 27।",
        "a = 18, d = -5/2, a_n = -47. -47 = 18 - 5/2(n - 1) => 65 = 5/2(n - 1) => n - 1 = 26 => n = 27."
    ))

    # Q6
    blocks.append(make_quiz(
        "C10M_CH5_EX5.2_Q6",
        "Exercise 5.2 (Q6): Check whether -150 is a term of the AP: 11, 8, 5, 2, ...",
        "प्रश्नावली 5.2 (Q6): क्या AP: 11, 8, 5, 2, ... का एक पद -150 है? क्यों?",
        "સ્વાધ્યાય 5.2 (Q6): ચકાસો કે શું -150 એ સમાંતર શ્રેણી 11, 8, 5, 2, ... નું કોઈ પદ છે?",
        [
            "No, because n = 54 2/3 is not a natural number",
            "Yes, it is the 55th term",
            "Yes, it is the 54th term",
            "No, because -150 is negative"
        ],
        [
            "नहीं, क्योंकि n = 54 2/3 एक प्राकृत संख्या नहीं है",
            "हाँ, यह 55वाँ पद है",
            "हाँ, यह 54वाँ पद है",
            "नहीं, क्योंकि -150 ऋणात्मक है"
        ],
        [
            "ના, કારણ કે n = 54 2/3 એ પ્રાકૃતિક સંખ્યા નથી",
            "હા, તે 55મું પદ છે",
            "હા, તે 54મું પદ છે",
            "ના, કારણ કે -150 ઋણ છે"
        ],
        0,
        "Here a = 11, d = 8 - 11 = -3. Let a_n = -150 => 11 + (n - 1)(-3) = -150 => -3(n - 1) = -161 => n - 1 = 161/3 => n = 164/3 = 54 2/3. Since n must be a positive integer, -150 is NOT a term.",
        "a = 11, d = -3। -150 = 11 + (n - 1)(-3) => -3(n - 1) = -161 => n = 164/3 = 54 2/3। चूँकि n एक धनात्मक पूर्णांक होना चाहिए, इसलिए -150 पद नहीं है।",
        "a = 11, d = -3. -150 = 11 + (n - 1)(-3) => n = 164/3. n ધન પૂર્ણાંક હોવો જરૂરી હોવાથી, -150 શ્રેણીનું પદ નથી."
    ))

    # Q7
    blocks.append(make_quiz(
        "C10M_CH5_EX5.2_Q7",
        "Exercise 5.2 (Q7): Find the 31st term of an AP whose 11th term is 38 and the 16th term is 73.",
        "प्रश्नावली 5.2 (Q7): उस AP का 31वाँ पद ज्ञात कीजिए, जिसका 11वाँ पद 38 है और 16वाँ पद 73 है।",
        "સ્વાધ્યાય 5.2 (Q7): જે સમાંતર શ્રેણીનું 11મું પદ 38 અને 16મું પદ 73 હોય તેનું 31મું પદ શોધો.",
        ["178", "168", "188", "172"],
        ["178", "168", "188", "172"],
        ["178", "168", "188", "172"],
        0,
        "a₁₁ = a + 10d = 38, and a₁₆ = a + 15d = 73. Subtracting: 5d = 35 => d = 7. Then a + 10(7) = 38 => a = -32. Thus a₃₁ = a + 30d = -32 + 30(7) = -32 + 210 = 178.",
        "a + 10d = 38 और a + 15d = 73। घटाने पर: 5d = 35 => d = 7। a = 38 - 70 = -32। a₃₁ = -32 + 30(7) = 178।",
        "a + 10d = 38 અને a + 15d = 73. બાદબાકી કરતા: 5d = 35 => d = 7. a = -32. a₃₁ = -32 + 30(7) = 178."
    ))

    # Q8
    blocks.append(make_quiz(
        "C10M_CH5_EX5.2_Q8",
        "Exercise 5.2 (Q8): An AP consists of 50 terms of which 3rd term is 12 and the last term is 106. Find the 29th term.",
        "प्रश्नावली 5.2 (Q8): एक AP में 50 पद हैं, जिसका तीसरा पद 12 है और अंतिम पद 106 है। इसका 29वाँ पद ज्ञात कीजिए।",
        "સ્વાધ્યાય 5.2 (Q8): એક સમાંતર શ્રેણીમાં 50 પદ છે. જો ત્રીજું પદ 12 અને છેલ્લું પદ 106 હોય, તો તેનું 29મું પદ શોધો.",
        ["64", "62", "66", "68"],
        ["64", "62", "66", "68"],
        ["64", "62", "66", "68"],
        0,
        "Total terms n = 50. a₃ = a + 2d = 12, a₅₀ = a + 49d = 106. Subtracting: 47d = 94 => d = 2. a = 12 - 2(2) = 8. a₂₉ = a + 28d = 8 + 28(2) = 64.",
        "a + 2d = 12 और a + 49d = 106। 47d = 94 => d = 2। a = 12 - 4 = 8। a₂₉ = 8 + 28(2) = 64।",
        "a + 2d = 12 અને a + 49d = 106. 47d = 94 => d = 2. a = 8. a₂₉ = 8 + 28(2) = 64."
    ))

    # Q9
    blocks.append(make_quiz(
        "C10M_CH5_EX5.2_Q9",
        "Exercise 5.2 (Q9): If the 3rd and the 9th terms of an AP are 4 and -8 respectively, which term of this AP is zero?",
        "प्रश्नावली 5.2 (Q9): यदि किसी AP के तीसरे और नौवें पद क्रमशः 4 और -8 हैं, तो इसका कौन सा पद शून्य होगा?",
        "સ્વાધ્યાય 5.2 (Q9): જો સમાંતર શ્રેણીનું ત્રીજું અને નવમું પદ અનુક્રમે 4 અને -8 હોય, તો તે શ્રેણીનું કયું પદ શૂન્ય થાય?",
        ["5th term", "6th term", "4th term", "7th term"],
        ["5वाँ पद", "6वाँ पद", "4वाँ पद", "7वाँ पद"],
        ["5મું પદ", "6મું પદ", "4મું પદ", "7મું પદ"],
        0,
        "a₃ = a + 2d = 4, a₉ = a + 8d = -8. Subtracting: 6d = -12 => d = -2. a = 4 - 2(-2) = 8. Set a_n = 0: 8 + (n - 1)(-2) = 0 => 2(n - 1) = 8 => n - 1 = 4 => n = 5.",
        "a + 2d = 4 और a + 8d = -8। 6d = -12 => d = -2, a = 8। a_n = 0 => 8 + (n - 1)(-2) = 0 => n = 5वाँ पद।",
        "a + 2d = 4 અને a + 8d = -8. 6d = -12 => d = -2, a = 8. a_n = 0 => 8 + (n - 1)(-2) = 0 => n = 5મું પદ."
    ))

    # Q10
    blocks.append(make_quiz(
        "C10M_CH5_EX5.2_Q10",
        "Exercise 5.2 (Q10): The 17th term of an AP exceeds its 10th term by 7. Find the common difference.",
        "प्रश्नावली 5.2 (Q10): किसी AP का 17वाँ पद उसके 10वें पद से 7 अधिक है। इसका सार्व अंतर ज्ञात कीजिए।",
        "સ્વાધ્યાય 5.2 (Q10): કોઈ સમાંતર શ્રેણીનું 17મું પદ તેના 10મા પદ કરતાં 7 વધુ છે, તો તેનો સામાન્ય તફાવત શોધો.",
        ["d = 1", "d = 7", "d = 2", "d = -1"],
        ["d = 1", "d = 7", "d = 2", "d = -1"],
        ["d = 1", "d = 7", "d = 2", "d = -1"],
        0,
        "a₁₇ - a₁₀ = 7 => (a + 16d) - (a + 9d) = 7 => 7d = 7 => d = 1.",
        "a₁₇ - a₁₀ = 7 => (a + 16d) - (a + 9d) = 7 => 7d = 7 => d = 1।",
        "a₁₇ - a₁₀ = 7 => (a + 16d) - (a + 9d) = 7 => 7d = 7 => d = 1."
    ))

    # Q11
    blocks.append(make_quiz(
        "C10M_CH5_EX5.2_Q11",
        "Exercise 5.2 (Q11): Which term of the AP: 3, 15, 27, 39, ... will be 132 more than its 54th term?",
        "प्रश्नावली 5.2 (Q11): AP: 3, 15, 27, 39, ... का कौन सा पद उसके 54वें पद से 132 अधिक होगा?",
        "સ્વાધ્યાય 5.2 (Q11): સમાંતર શ્રેણી 3, 15, 27, 39, ... નું કયું પદ તેના 54મા પદ કરતાં 132 વધુ હશે?",
        ["65th term", "64th term", "66th term", "63rd term"],
        ["65वाँ पद", "64वाँ पद", "66वाँ पद", "63वाँ पद"],
        ["65મું પદ", "64મું પદ", "66મું પદ", "63મું પદ"],
        0,
        "Here a = 3, d = 12. Let the required term be a_n. a_n - a₅₄ = 132 => (n - 54)d = 132 => (n - 54)(12) = 132 => n - 54 = 11 => n = 65.",
        "a = 3, d = 12। a_n = a₅₄ + 132 => (n - 54)d = 132 => (n - 54)(12) = 132 => n - 54 = 11 => n = 65वाँ पद।",
        "a = 3, d = 12. a_n = a₅₄ + 132 => (n - 54)12 = 132 => n - 54 = 11 => n = 65મું પદ."
    ))

    # Q12
    blocks.append(make_quiz(
        "C10M_CH5_EX5.2_Q12",
        "Exercise 5.2 (Q12): Two APs have the same common difference. The difference between their 100th terms is 100, what is the difference between their 1000th terms?",
        "प्रश्नावली 5.2 (Q12): दो समांतर श्रेढ़ियों का सार्व अंतर समान है। यदि इनके 100वें पदों का अंतर 100 है, तो इनके 1000वें पदों का अंतर क्या होगा?",
        "સ્વાધ્યાય 5.2 (Q12): બે સમાંતર શ્રેણીના સામાન્ય તફાવત સમાન છે. તેમના 100મા પદોનો તફાવત 100 હોય, તો તેમના 1000મા પદોનો તફાવત કેટલો હશે?",
        ["100", "1000", "0", "10000"],
        ["100", "1000", "0", "10000"],
        ["100", "1000", "0", "10000"],
        0,
        "Let first terms be a and b with same d. Difference of nth terms: (a + (n-1)d) - (b + (n-1)d) = a - b. The difference is ALWAYS constant (a - b) for ANY term! Since difference between 100th terms is 100, a - b = 100. Thus difference between 1000th terms is also 100.",
        "nवें पदों का अंतर = (a + (n-1)d) - (b + (n-1)d) = a - b (स्थिर)। अतः 1000वें पदों का अंतर भी a - b = 100 ही होगा।",
        "nમા પદોનો તફાવત = a - b (અચળ રહે છે). તેથી 1000મા પદોનો તફાવત પણ 100 જ થશે."
    ))

    # Q13
    blocks.append(make_quiz(
        "C10M_CH5_EX5.2_Q13",
        "Exercise 5.2 (Q13): How many three-digit numbers are divisible by 7?",
        "प्रश्नावली 5.2 (Q13): तीन अंकों वाली कितनी संख्याएँ 7 से विभाज्य हैं?",
        "સ્વાધ્યાય 5.2 (Q13): ત્રણ અંકની કેટલી સંખ્યાઓ 7 વડે વિભાજ્ય હશે?",
        ["128 numbers", "127 numbers", "129 numbers", "130 numbers"],
        ["128 संख्याएँ", "127 संख्याएँ", "129 संख्याएँ", "130 संख्याएँ"],
        ["128 સંખ્યાઓ", "127 સંખ્યાઓ", "129 સંખ્યાઓ", "130 સંખ્યાઓ"],
        0,
        "Smallest 3-digit number divisible by 7 is 105. Largest is 994. The AP is 105, 112, ..., 994 with a = 105, d = 7. 994 = 105 + (n - 1)7 => 7(n - 1) = 889 => n - 1 = 127 => n = 128.",
        "पहली 3-अंकीय संख्या 105 है और अंतिम 994 है। 994 = 105 + 7(n - 1) => 7(n - 1) = 889 => n = 128 संख्याएँ।",
        "પ્રથમ 3-અંકની સંખ્યા 105 અને છેલ્લી 994 છે. 994 = 105 + 7(n - 1) => n = 128 સંખ્યાઓ."
    ))

    # Q14
    blocks.append(make_quiz(
        "C10M_CH5_EX5.2_Q14",
        "Exercise 5.2 (Q14): How many multiples of 4 lie between 10 and 250?",
        "प्रश्नावली 5.2 (Q14): 10 और 250 के बीच में 4 के कितने गुणज हैं?",
        "સ્વાધ્યાય 5.2 (Q14): 10 અને 250 વચ્ચે 4 ના કેટલા ગુણિત હશે?",
        ["60 multiples", "59 multiples", "61 multiples", "62 multiples"],
        ["60 गुणज", "59 गुणज", "61 गुणज", "62 गुणज"],
        ["60 ગુણિત", "59 ગુણિત", "61 ગુણિત", "62 ગુણિત"],
        0,
        "First multiple after 10 is 12. Last multiple before 250 is 248. AP: 12, 16, ..., 248. a = 12, d = 4. 248 = 12 + (n - 1)4 => 4(n - 1) = 236 => n - 1 = 59 => n = 60.",
        "10 के बाद पहला गुणज 12 है और 250 से पहले 248 है। 248 = 12 + 4(n - 1) => 4(n - 1) = 236 => n = 60 गुणज।",
        "10 પછી પ્રથમ ગુણિત 12 અને 250 પહેલાં 248 છે. 248 = 12 + 4(n - 1) => n = 60 ગુણિત."
    ))

    # Q15
    blocks.append(make_quiz(
        "C10M_CH5_EX5.2_Q15",
        "Exercise 5.2 (Q15): For what value of n, are the nth terms of two APs: 63, 65, 67, ... and 3, 10, 17, ... equal?",
        "प्रश्नावली 5.2 (Q15): n के किस मान के लिए, दोनों समांतर श्रेढ़ियों 63, 65, 67, ... और 3, 10, 17, ... के nवें पद बराबर होंगे?",
        "સ્વાધ્યાય 5.2 (Q15): n ના કયા મૂલ્ય માટે બે સમાંતર શ્રેણીઓ 63, 65, 67, ... અને 3, 10, 17, ... ના nમા પદ સમાન થાય?",
        ["n = 13", "n = 12", "n = 14", "n = 15"],
        ["n = 13", "n = 12", "n = 14", "n = 15"],
        ["n = 13", "n = 12", "n = 14", "n = 15"],
        0,
        "For 1st AP: a_n = 63 + (n - 1)2 = 61 + 2n. For 2nd AP: a_n = 3 + (n - 1)7 = 7n - 4. Setting equal: 61 + 2n = 7n - 4 => 5n = 65 => n = 13.",
        "पहली AP: 63 + (n - 1)2 = 61 + 2n। दूसरी AP: 3 + (n - 1)7 = 7n - 4। बराबर रखने पर: 61 + 2n = 7n - 4 => 5n = 65 => n = 13।",
        "પ્રથમ AP: 61 + 2n. બીજી AP: 7n - 4. સરખાવતા: 61 + 2n = 7n - 4 => 5n = 65 => n = 13."
    ))

    # Q16
    blocks.append(make_quiz(
        "C10M_CH5_EX5.2_Q16",
        "Exercise 5.2 (Q16): Determine the AP whose 3rd term is 16 and the 7th term exceeds the 5th term by 12.",
        "प्रश्नावली 5.2 (Q16): वह AP निर्धारित कीजिए जिसका तीसरा पद 16 है और 7वाँ पद 5वें पद से 12 अधिक है।",
        "સ્વાધ્યાય 5.2 (Q16): એવી સમાંતર શ્રેણી શોધો કે જેનું ત્રીજું પદ 16 અને 7મું પદ 5મા પદથી 12 વધુ હોય.",
        ["4, 10, 16, 22, ...", "2, 8, 14, 20, ...", "4, 8, 12, 16, ...", "6, 12, 18, 24, ..."],
        ["4, 10, 16, 22, ...", "2, 8, 14, 20, ...", "4, 8, 12, 16, ...", "6, 12, 18, 24, ..."],
        ["4, 10, 16, 22, ...", "2, 8, 14, 20, ...", "4, 8, 12, 16, ...", "6, 12, 18, 24, ..."],
        0,
        "a₇ - a₅ = 12 => (a + 6d) - (a + 4d) = 12 => 2d = 12 => d = 6. Given a₃ = 16 => a + 2(6) = 16 => a = 4. The AP is 4, 10, 16, 22, ...",
        "a₇ - a₅ = 12 => 2d = 12 => d = 6। a + 2(6) = 16 => a = 4। AP है: 4, 10, 16, 22, ...।",
        "a₇ - a₅ = 12 => 2d = 12 => d = 6. a + 2(6) = 16 => a = 4. AP: 4, 10, 16, 22, ..."
    ))

    # Q17
    blocks.append(make_quiz(
        "C10M_CH5_EX5.2_Q17",
        "Exercise 5.2 (Q17): Find the 20th term from the last term of the AP: 3, 8, 13, ..., 253.",
        "प्रश्नावली 5.2 (Q17): AP: 3, 8, 13, ..., 253 में अंतिम पद से 20वाँ पद ज्ञात कीजिए।",
        "સ્વાધ્યાય 5.2 (Q17): સમાંતર શ્રેણી 3, 8, 13, ..., 253 નું છેલ્લેથી 20મું પદ શોધો.",
        ["158", "148", "168", "153"],
        ["158", "148", "168", "153"],
        ["158", "148", "168", "153"],
        0,
        "Here l = 253, d = 8 - 3 = 5. Formula for nth term from end: l - (n - 1)d = 253 - (20 - 1)5 = 253 - 19(5) = 253 - 95 = 158.",
        "अंतिम पद से nवाँ पद = l - (n - 1)d = 253 - (20 - 1)5 = 253 - 95 = 158।",
        "છેલ્લેથી nમું પદ = l - (n - 1)d = 253 - 19(5) = 253 - 95 = 158."
    ))

    # Q18
    blocks.append(make_quiz(
        "C10M_CH5_EX5.2_Q18",
        "Exercise 5.2 (Q18): The sum of the 4th and 8th terms of an AP is 24 and the sum of the 6th and 10th terms is 44. Find the first three terms of the AP.",
        "प्रश्नावली 5.2 (Q18): किसी AP के चौथे और 8वें पदों का योग 24 है तथा छठे और 10वें पदों का योग 44 है। इस AP के प्रथम तीन पद ज्ञात कीजिए।",
        "સ્વાધ્યાય 5.2 (Q18): એક સમાંતર શ્રેણીના ચોથા અને આઠમા પદોનો સરવાળો 24 છે અને છઠ્ઠા અને દસમા પદોનો સરવાળો 44 છે, તો આ સમાંતર શ્રેણીના પ્રથમ ત્રણ પદ શોધો.",
        ["-13, -8, -3", "-10, -5, 0", "-15, -10, -5", "-12, -7, -2"],
        ["-13, -8, -3", "-10, -5, 0", "-15, -10, -5", "-12, -7, -2"],
        ["-13, -8, -3", "-10, -5, 0", "-15, -10, -5", "-12, -7, -2"],
        0,
        "a₄ + a₈ = (a + 3d) + (a + 7d) = 2a + 10d = 24 => a + 5d = 12. a₆ + a₁₀ = (a + 5d) + (a + 9d) = 2a + 14d = 44 => a + 7d = 22. Subtracting: 2d = 10 => d = 5. Then a = 12 - 5(5) = -13. First 3 terms: -13, -8, -3.",
        "2a + 10d = 24 => a + 5d = 12। 2a + 14d = 44 => a + 7d = 22। घटाने पर: 2d = 10 => d = 5, a = -13। प्रथम तीन पद: -13, -8, -3।",
        "a + 5d = 12 અને a + 7d = 22. બાદબાકી કરતા: 2d = 10 => d = 5, a = -13. પ્રથમ ત્રણ પદો: -13, -8, -3."
    ))

    # Q19
    blocks.append(make_quiz(
        "C10M_CH5_EX5.2_Q19",
        "Exercise 5.2 (Q19): Subba Rao started work in 1995 at an annual salary of ₹5000 and received an increment of ₹200 each year. In which year did his income reach ₹7000?",
        "प्रश्नावली 5.2 (Q19): सुब्बा राव ने 1995 में ₹5000 के मासिक वेतन पर कार्य आरंभ किया और प्रत्येक वर्ष ₹200 की वेतन वृद्धि प्राप्त की। किस वर्ष में उनका वेतन ₹7000 हो गया?",
        "સ્વાધ્યાય 5.2 (Q19): સુબ્બારામે 1995 માં ₹5000 ના વાર્ષિક વેતનથી કામ શરૂ કર્યું અને તેમને દર વર્ષે ₹200 ની વેતનવૃદ્ધિ મળે છે. કયા વર્ષમાં તેમનું વેતન ₹7000 થશે?",
        ["In the year 2005 (11th year)", "In the year 2004 (10th year)", "In the year 2006 (12th year)", "In the year 2007 (13th year)"],
        ["वर्ष 2005 में (11वाँ वर्ष)", "वर्ष 2004 में (10वाँ वर्ष)", "वर्ष 2006 में (12वाँ वर्ष)", "वर्ष 2007 में (13वाँ वर्ष)"],
        ["વર્ષ 2005 માં (11મું વર્ષ)", "વર્ષ 2004 માં (10મું વર્ષ)", "વર્ષ 2006 માં (12મું વર્ષ)", "વર્ષ 2007 માં (13મું વર્ષ)"],
        0,
        "Here a = 5000, d = 200, a_n = 7000. 7000 = 5000 + (n - 1)200 => 200(n - 1) = 2000 => n - 1 = 10 => n = 11. Year = 1995 + (11 - 1) = 2005.",
        "a = 5000, d = 200, a_n = 7000। 7000 = 5000 + 200(n - 1) => n - 1 = 10 => n = 11वाँ वर्ष। वर्ष = 1995 + 10 = 2005।",
        "a = 5000, d = 200, a_n = 7000. 7000 = 5000 + 200(n - 1) => n = 11મું વર્ષ. વર્ષ = 1995 + 10 = 2005."
    ))

    # Q20
    blocks.append(make_quiz(
        "C10M_CH5_EX5.2_Q20",
        "Exercise 5.2 (Q20): Ramkali saved ₹5 in the first week of a year and then increased her weekly savings by ₹1.75. If in the nth week, her weekly savings become ₹20.75, find n.",
        "प्रश्नावली 5.2 (Q20): रामकली ने किसी वर्ष के प्रथम सप्ताह में ₹5 की बचत की और फिर अपनी साप्ताहिक बचत ₹1.75 बढ़ाती गई। यदि nवें सप्ताह में उसकी साप्ताहिक बचत ₹20.75 हो जाती है, तो n ज्ञात कीजिए।",
        "સ્વાધ્યાય 5.2 (Q20): રામકલીએ વર્ષના પ્રથમ અઠવાડિયે ₹5 ની બચત કરી અને પછી તેની સાપ્તાહિક બચતમાં ₹1.75 નો વધારો કર્યો. જો nમા અઠવાડિયે તેની બચત ₹20.75 થાય, તો n નું મૂલ્ય શોધો.",
        ["n = 10", "n = 9", "n = 11", "n = 12"],
        ["n = 10", "n = 9", "n = 11", "n = 12"],
        ["n = 10", "n = 9", "n = 11", "n = 12"],
        0,
        "Here a = 5, d = 1.75, a_n = 20.75. 20.75 = 5 + (n - 1)(1.75) => (n - 1)(1.75) = 15.75 => n - 1 = 15.75 / 1.75 = 9 => n = 10.",
        "a = 5, d = 1.75, a_n = 20.75। 20.75 = 5 + 1.75(n - 1) => 1.75(n - 1) = 15.75 => n - 1 = 9 => n = 10।",
        "a = 5, d = 1.75, a_n = 20.75. 20.75 = 5 + 1.75(n - 1) => 1.75(n - 1) = 15.75 => n - 1 = 9 => n = 10."
    ))

    return blocks

def get_part3_blocks():
    blocks = []

    # =========================================================================
    # PART 3: SUM OF FIRST n TERMS OF AN AP (STORY & THEORY)
    # =========================================================================
    blocks.append({
        "id": "C10M_CH5_PART3_HOOK",
        "type": "hook",
        "title": "Young Gauss and the Challenge of Adding 1 to 100",
        "body": "In late 18th-century Germany, a school teacher wanted to keep his 10-year-old students busy for an hour. He gave them a punishing task: *'Add all numbers from 1 to 100!'*\n\nWhile other students scribbled furiously ($1 + 2 = 3, 3 + 3 = 6, 6 + 4 = 10...$), a young boy named **Carl Friedrich Gauss** walked up to the teacher's desk within seconds with the exact answer: **5050**!\n\nHow did he do it? Gauss noticed a stunning symmetry: \n$$1 + 100 = 101$$\n$$2 + 99 = 101$$\n$$3 + 98 = 101$$\nThere are 50 such pairs of 101, so the total sum is $50 \\times 101 = 5050$! This genius insight is the exact foundation for finding the sum of any Arithmetic Progression!",
        "title_hi": "युवा गॉस और 1 से 100 तक जोड़ने की चुनौती",
        "body_hi": "18वीं शताब्दी के उत्तरार्ध में जर्मनी में, एक शिक्षक ने 10 वर्षीय छात्रों को व्यस्त रखने के लिए एक कठिन कार्य दिया: *'1 से 100 तक की सभी संख्याओं को जोड़ो!'*\n\nजब अन्य छात्र एक-एक करके जोड़ने में लगे थे ($1 + 2 = 3, 3 + 3 = 6...$), तब **कार्ल फ्रेडरिक गॉस** नाम का एक बालक कुछ ही सेकंड में सही उत्तर **5050** लेकर शिक्षक के पास पहुँच गया!\n\nउसने यह कैसे किया? गॉस ने एक अद्भुत सममिति देखी:\n$$1 + 100 = 101$$\n$$2 + 99 = 101$$\n$$3 + 98 = 101$$\nऐसे 101 के 50 जोड़े बनते हैं, अतः कुल योग $50 \\times 101 = 5050$ है! यही प्रतिभा किसी भी समान्तर श्रेढ़ी के योग का आधार है!",
        "title_gu": "યુવાન ગોસ અને 1 થી 100 ના સરવાળાનો પડકાર",
        "body_gu": "18મી સદીના ઉત્તરાર્ધમાં જર્મનીમાં, એક શિક્ષકે 10 વર્ષના વિદ્યાર્થીઓને વ્યસ્ત રાખવા માટે કામ આપ્યું: *'1 થી 100 સુધીની બધી સંખ્યાઓનો સરવાળો કરો!'*\n\nજ્યારે અન્ય વિદ્યાર્થીઓ ધીમે ધીમે ગણતરી કરી રહ્યા હતા, ત્યારે **કાર્લ ફ્રેડરિક ગોસ** નામના બાળકે થોડી જ સેકન્ડોમાં સાચો જવાબ **5050** આપીને શિક્ષકને આશ્ચર્યચકિત કરી દીધા!\n\nતેણે આ કેવી રીતે કર્યું? ગોસે એક સુંદર સમપ્રમાણતા જોઈ:\n$$1 + 100 = 101$$\n$$2 + 99 = 101$$\n$$3 + 98 = 101$$\nઆવી 101 ની 50 જોડીઓ બને છે, તેથી કુલ સરવાળો $50 \\times 101 = 5050$ થાય! આ વિચાર સમાંતર શ્રેણીના સરવાળાનું પાયાનું સૂત્ર છે!",
        "bloom": "Understand",
        "difficulty": "Beginner",
        "estimated_minutes": 3
    })

    blocks.append({
        "id": "C10M_CH5_PART3_THEORY",
        "type": "theory",
        "title": "Formula for the Sum of First n Terms (S_n)",
        "body": "The sum of the first $n$ terms of an AP with first term $a$ and common difference $d$ is given by:\n\n$$\\mathbf{S_n = \\frac{n}{2}[2a + (n - 1)d]}$$\n\n**Alternative Formula (When Last Term is Known):**\nIf the last term $l = a_n = a + (n - 1)d$ is known, we can write $2a = a + a$, so:\n$$\\mathbf{S_n = \\frac{n}{2}[a + l]}$$\n\n**Sum of First n Positive Integers:**\n$$S_n = 1 + 2 + 3 + \\dots + n = \\mathbf{\\frac{n(n + 1)}{2}}$$\n\n**Vital Connection between a_n and S_n:**\nThe nth term of an AP is the difference between the sum of first $n$ terms and the sum of first $(n - 1)$ terms:\n$$\\mathbf{a_n = S_n - S_{n-1}}$$",
        "title_hi": "प्रथम n पदों के योग का सूत्र (S_n)",
        "body_hi": "प्रथम पद $a$ और सार्व अंतर $d$ वाली AP के प्रथम $n$ पदों का योग निम्न सूत्र द्वारा दिया जाता है:\n\n$$\\mathbf{S_n = \\frac{n}{2}[2a + (n - 1)d]}$$\n\n**वैकल्पिक सूत्र (जब अंतिम पद ज्ञात हो):**\nयदि अंतिम पद $l = a_n = a + (n - 1)d$ ज्ञात हो, तो:\n$$\\mathbf{S_n = \\frac{n}{2}[a + l]}$$\n\n**प्रथम n धन पूर्णांकों का योग:**\n$$S_n = 1 + 2 + 3 + \\dots + n = \\mathbf{\\frac{n(n + 1)}{2}}$$\n\n**a_n और S_n के बीच महत्वपूर्ण संबंध:**\nकिसी AP का nवाँ पद, प्रथम $n$ पदों के योग और प्रथम $(n - 1)$ पदों के योग का अंतर होता है:\n$$\\mathbf{a_n = S_n - S_{n-1}}$$",
        "title_gu": "પ્રથમ n પદોના સરવાળાનું સૂત્ર (S_n)",
        "body_gu": "પ્રથમ પદ $a$ અને સામાન્ય તફાવત $d$ વાળી AP ના પ્રથમ $n$ પદોનો સરવાળો:\n\n$$\\mathbf{S_n = \\frac{n}{2}[2a + (n - 1)d]}$$\n\n**વૈકલ્પિક સૂત્ર (જ્યારે છેલ્લું પદ આપેલ હોય):**\nજો છેલ્લું પદ $l = a_n = a + (n - 1)d$ જાણીતું હોય, તો:\n$$\\mathbf{S_n = \\frac{n}{2}[a + l]}$$\n\n**પ્રથમ n ધન પૂર્ણાંકોનો સરવાળો:**\n$$S_n = 1 + 2 + 3 + \\dots + n = \\mathbf{\\frac{n(n + 1)}{2}}$$\n\n**a_n અને S_n વચ્ચેનો સંબંધ:**\nકોઈપણ AP નું nમું પદ એ પ્રથમ $n$ પદોના સરવાળા અને પ્રથમ $(n - 1)$ પદોના સરવાળાનો તફાવત છે:\n$$\\mathbf{a_n = S_n - S_{n-1}}$$",
        "bloom": "Remember",
        "difficulty": "Beginner",
        "estimated_minutes": 3
    })

    # =========================================================================
    # EXERCISE 5.3 - QUESTION 1 (Find Sum of APs, 4 Subparts)
    # =========================================================================
    ex5_3_q1_data = [
        ("2, 7, 12, ... to 10 terms", ["245", "250", "240", "235"], 0, "a = 2, d = 5, n = 10. S₁₀ = (10/2)[2(2) + (10 - 1)5] = 5[4 + 45] = 5(49) = 245."),
        ("-37, -33, -29, ... to 12 terms", ["-180", "-190", "-170", "-160"], 0, "a = -37, d = -33 - (-37) = 4, n = 12. S₁₂ = (12/2)[2(-37) + (12 - 1)4] = 6[-74 + 44] = 6(-30) = -180."),
        ("0.6, 1.7, 2.8, ... to 100 terms", ["5505", "5455", "5550", "5510"], 0, "a = 0.6, d = 1.1, n = 100. S₁₀₀ = (100/2)[2(0.6) + (99)(1.1)] = 50[1.2 + 108.9] = 50(110.1) = 5505."),
        ("1/15, 1/12, 1/10, ... to 11 terms", ["33/20", "31/20", "3/2", "37/20"], 0, "a = 1/15, d = 1/12 - 1/15 = 1/60, n = 11. S₁₁ = (11/2)[2/15 + 10(1/60)] = (11/2)[2/15 + 1/6] = (11/2)(9/30) = 33/20.")
    ]
    ex5_3_q1_data_hi = [
        "a = 2, d = 5, n = 10। S₁₀ = 5[4 + 45] = 5(49) = 245।",
        "a = -37, d = 4, n = 12। S₁₂ = 6[-74 + 44] = 6(-30) = -180।",
        "a = 0.6, d = 1.1, n = 100। S₁₀₀ = 50[1.2 + 108.9] = 50(110.1) = 5505।",
        "a = 1/15, d = 1/60, n = 11। S₁₁ = (11/2)[2/15 + 1/6] = (11/2)(9/30) = 33/20।"
    ]
    ex5_3_q1_data_gu = [
        "a = 2, d = 5, n = 10. S₁₀ = 5[4 + 45] = 5(49) = 245.",
        "a = -37, d = 4, n = 12. S₁₂ = 6[-74 + 44] = 6(-30) = -180.",
        "a = 0.6, d = 1.1, n = 100. S₁₀₀ = 50[1.2 + 108.9] = 50(110.1) = 5505.",
        "a = 1/15, d = 1/60, n = 11. S₁₁ = (11/2)[2/15 + 1/6] = (11/2)(9/30) = 33/20."
    ]

    for idx, (params, opts, c_idx, expl) in enumerate(ex5_3_q1_data):
        blocks.append(make_quiz(
            f"C10M_CH5_EX5.3_Q1_p{idx+1}",
            f"Exercise 5.3 (Q1.{idx+1}): Find the sum of the following AP: {params}",
            f"प्रश्नावली 5.3 (Q1.{idx+1}): निम्नलिखित समांतर श्रेढ़ियों का योग ज्ञात कीजिए: {params}",
            f"સ્વાધ્યાય 5.3 (Q1.{idx+1}): નીચે આપેલ સમાંતર શ્રેણીઓનો સરવાળો શોધો: {params}",
            opts, opts, opts,
            c_idx, expl, ex5_3_q1_data_hi[idx], ex5_3_q1_data_gu[idx],
            bloom="Apply", diff="Beginner"
        ))

    # =========================================================================
    # EXERCISE 5.3 - QUESTION 2 (Find Sums Given Below, 3 Subparts)
    # =========================================================================
    ex5_3_q2_data = [
        ("7 + 10 1/2 + 14 + ... + 84", ["1046 1/2 (or 2093/2)", "1040", "1050 1/2", "1045"], 0, "a = 7, d = 7/2, l = 84. 84 = 7 + (n - 1)(7/2) => n - 1 = 22 => n = 23. S₂₃ = (23/2)(7 + 84) = (23/2)(91) = 2093/2 = 1046 1/2."),
        ("34 + 32 + 30 + ... + 10", ["286", "296", "276", "280"], 0, "a = 34, d = -2, l = 10. 10 = 34 + (n - 1)(-2) => 2(n - 1) = 24 => n = 13. S₁₃ = (13/2)(34 + 10) = (13/2)(44) = 13 × 22 = 286."),
        ("(-5) + (-8) + (-11) + ... + (-230)", ["-8930", "-8900", "-8950", "-8830"], 0, "a = -5, d = -3, l = -230. -230 = -5 + (n - 1)(-3) => -3(n - 1) = -225 => n = 76. S₇₆ = (76/2)[-5 + (-230)] = 38(-235) = -8930.")
    ]
    ex5_3_q2_data_hi = [
        "a = 7, d = 7/2, l = 84 => n = 23। S₂₃ = (23/2)(7 + 84) = 2093/2 = 1046 1/2।",
        "a = 34, d = -2, l = 10 => n = 13। S₁₃ = (13/2)(34 + 10) = 286।",
        "a = -5, d = -3, l = -230 => n = 76। S₇₆ = 38(-235) = -8930।"
    ]
    ex5_3_q2_data_gu = [
        "a = 7, d = 7/2, l = 84 => n = 23. S₂₃ = (23/2)(7 + 84) = 2093/2 = 1046 1/2.",
        "a = 34, d = -2, l = 10 => n = 13. S₁₃ = (13/2)(34 + 10) = 286.",
        "a = -5, d = -3, l = -230 => n = 76. S₇₆ = 38(-235) = -8930."
    ]

    for idx, (series_str, opts, c_idx, expl) in enumerate(ex5_3_q2_data):
        blocks.append(make_quiz(
            f"C10M_CH5_EX5.3_Q2_p{idx+1}",
            f"Exercise 5.3 (Q2.{idx+1}): Find the sum given below: {series_str}",
            f"प्रश्नावली 5.3 (Q2.{idx+1}): नीचे दिए हुए योगफलों को ज्ञात कीजिए: {series_str}",
            f"સ્વાધ્યાય 5.3 (Q2.{idx+1}): નીચે આપેલા સરવાળા શોધો: {series_str}",
            opts, opts, opts,
            c_idx, expl, ex5_3_q2_data_hi[idx], ex5_3_q2_data_gu[idx],
            bloom="Apply", diff="Intermediate"
        ))

    # =========================================================================
    # EXERCISE 5.3 - QUESTION 3 (In an AP, 10 Subparts)
    # =========================================================================
    q3_parts_data = [
        ("given a = 5, d = 3, a_n = 50, find n and S_n", ["n = 16, S_n = 440", "n = 15, S_n = 420", "n = 16, S_n = 450", "n = 17, S_n = 440"], 0, "50 = 5 + (n - 1)3 => 3(n - 1) = 45 => n = 16. S₁₆ = (16/2)(5 + 50) = 8(55) = 440."),
        ("given a = 7, a_13 = 35, find d and S_13", ["d = 7/3, S_13 = 273", "d = 2, S_13 = 260", "d = 7/3, S_13 = 280", "d = 3, S_13 = 273"], 0, "a + 12d = 35 => 7 + 12d = 35 => 12d = 28 => d = 7/3. S₁₃ = (13/2)(7 + 35) = (13/2)(42) = 273."),
        ("given a_12 = 37, d = 3, find a and S_12", ["a = 4, S_12 = 246", "a = 3, S_12 = 240", "a = 4, S_12 = 250", "a = 5, S_12 = 246"], 0, "a + 11(3) = 37 => a + 33 = 37 => a = 4. S₁₂ = (12/2)(4 + 37) = 6(41) = 246."),
        ("given a_3 = 15, S_10 = 125, find d and a_10", ["d = -1, a_10 = 8", "d = 1, a_10 = 22", "d = -1, a_10 = 10", "d = -2, a_10 = 8"], 0, "a + 2d = 15, and 5(2a + 9d) = 125 => 2a + 9d = 25. 2(a + 2d) = 2a + 4d = 30. Subtracting: 5d = -5 => d = -1, a = 17. a₁₀ = 17 + 9(-1) = 8."),
        ("given d = 5, S_9 = 75, find a and a_9", ["a = -35/3, a_9 = 85/3", "a = -10, a_9 = 30", "a = -35/3, a_9 = 25", "a = -11, a_9 = 29"], 0, "(9/2)[2a + 8(5)] = 75 => 9(2a + 40) = 150 => 2a + 40 = 50/3 => 2a = -70/3 => a = -35/3. a₉ = -35/3 + 40 = 85/3."),
        ("given a = 2, d = 8, S_n = 90, find n and a_n", ["n = 5, a_n = 34", "n = 6, a_n = 42", "n = 5, a_n = 32", "n = 4, a_n = 26"], 0, "(n/2)[4 + (n - 1)8] = 90 => n(4n - 2) = 90 => 2n² - n - 45 = 0 => (2n + 9)(n - 5) = 0 => n = 5. a₅ = 2 + 4(8) = 34."),
        ("given a = 8, a_n = 62, S_n = 210, find n and d", ["n = 6, d = 54/5", "n = 5, d = 10", "n = 6, d = 11", "n = 7, d = 54/5"], 0, "(n/2)(8 + 62) = 210 => 35n = 210 => n = 6. a₆ = 8 + 5d = 62 => 5d = 54 => d = 54/5."),
        ("given a_n = 4, d = 2, S_n = -14, find n and a", ["n = 7, a = -8", "n = 6, a = -6", "n = 7, a = -6", "n = 8, a = -8"], 0, "a + (n - 1)2 = 4 => a = 6 - 2n. S_n = (n/2)(a + 4) = -14 => n(10 - 2n) = -28 => n² - 5n - 14 = 0 => (n - 7)(n + 2) = 0 => n = 7, a = 6 - 14 = -8."),
        ("given a = 3, n = 8, S = 192, find d", ["d = 6", "d = 5", "d = 7", "d = 4"], 0, "(8/2)[2(3) + 7d] = 192 => 4(6 + 7d) = 192 => 6 + 7d = 48 => 7d = 42 => d = 6."),
        ("given l = 28, S = 144, and there are total 9 terms, find a", ["a = 4", "a = 3", "a = 5", "a = 6"], 0, "S = (n/2)(a + l) => 144 = (9/2)(a + 28) => 16 × 2 = a + 28 => a + 28 = 32 => a = 4.")
    ]
    q3_parts_hi = [
        "50 = 5 + 3(n - 1) => n = 16। S₁₆ = 8(5 + 50) = 440।",
        "7 + 12d = 35 => d = 7/3। S₁₃ = (13/2)(42) = 273।",
        "a + 33 = 37 => a = 4। S₁₂ = 6(4 + 37) = 246।",
        "a + 2d = 15 और 2a + 9d = 25 => d = -1, a = 17, a₁₀ = 8।",
        "(9/2)[2a + 40] = 75 => a = -35/3, a₉ = 85/3।",
        "2n² - n - 45 = 0 => n = 5, a₅ = 2 + 32 = 34।",
        "35n = 210 => n = 6, 5d = 54 => d = 54/5।",
        "n² - 5n - 14 = 0 => n = 7, a = -8।",
        "4(6 + 7d) = 192 => 7d = 42 => d = 6।",
        "(9/2)(a + 28) = 144 => a + 28 = 32 => a = 4।"
    ]
    q3_parts_gu = [
        "50 = 5 + 3(n - 1) => n = 16. S₁₆ = 8(5 + 50) = 440.",
        "7 + 12d = 35 => d = 7/3. S₁₃ = (13/2)(42) = 273.",
        "a + 33 = 37 => a = 4. S₁₂ = 6(4 + 37) = 246.",
        "a + 2d = 15 અને 2a + 9d = 25 => d = -1, a = 17, a₁₀ = 8.",
        "(9/2)[2a + 40] = 75 => a = -35/3, a₉ = 85/3.",
        "2n² - n - 45 = 0 => n = 5, a₅ = 34.",
        "35n = 210 => n = 6, d = 54/5.",
        "n² - 5n - 14 = 0 => n = 7, a = -8.",
        "4(6 + 7d) = 192 => d = 6.",
        "(9/2)(a + 28) = 144 => a = 4."
    ]

    for idx, (params, opts, c_idx, expl) in enumerate(q3_parts_data):
        blocks.append(make_quiz(
            f"C10M_CH5_EX5.3_Q3_p{idx+1}",
            f"Exercise 5.3 (Q3.{idx+1}): In an AP: {params}",
            f"प्रश्नावली 5.3 (Q3.{idx+1}): एक AP में: {params}",
            f"સ્વાધ્યાય 5.3 (Q3.{idx+1}): સમાંતર શ્રેણીમાં: {params}",
            opts, opts, opts,
            c_idx, expl, q3_parts_hi[idx], q3_parts_gu[idx],
            bloom="Apply", diff="Intermediate"
        ))

    # =========================================================================
    # EXERCISE 5.3 - QUESTIONS 4 to 20 (Complete Syllabus)
    # =========================================================================
    # Q4
    blocks.append(make_quiz(
        "C10M_CH5_EX5.3_Q4",
        "Exercise 5.3 (Q4): How many terms of the AP: 9, 17, 25, ... must be taken to give a sum of 636?",
        "प्रश्नावली 5.3 (Q4): 636 योग प्राप्त करने के लिए, AP: 9, 17, 25, ... के कितने पद लेने चाहिए?",
        "સ્વાધ્યાય 5.3 (Q4): સમાંતર શ્રેણી 9, 17, 25, ... ના કેટલા પદોનો સરવાળો 636 થાય?",
        ["12 terms", "13 terms", "11 terms", "14 terms"],
        ["12 पद", "13 पद", "11 पद", "14 पद"],
        ["12 પદો", "13 પદો", "11 પદો", "14 પદો"],
        0,
        "a = 9, d = 8, S_n = 636. S_n = (n/2)[2(9) + (n - 1)8] = 636 => n(9 + 4n - 4) = 636 => 4n² + 5n - 636 = 0. Factoring: (4n + 53)(n - 12) = 0 => n = 12 (since n > 0).",
        "a = 9, d = 8, S_n = 636। 4n² + 5n - 636 = 0 => (4n + 53)(n - 12) = 0 => n = 12 पद।",
        "a = 9, d = 8, S_n = 636. 4n² + 5n - 636 = 0 => (4n + 53)(n - 12) = 0 => n = 12 પદો."
    ))

    # Q5
    blocks.append(make_quiz(
        "C10M_CH5_EX5.3_Q5",
        "Exercise 5.3 (Q5): The first term of an AP is 5, the last term is 45 and the sum is 400. Find the number of terms and the common difference.",
        "प्रश्नावली 5.3 (Q5): किसी AP का प्रथम पद 5, अंतिम पद 45 और योग 400 है। पदों की संख्या और सार्व अंतर ज्ञात कीजिए।",
        "સ્વાધ્યાય 5.3 (Q5): સમાંતર શ્રેણીનું પ્રથમ પદ 5, અંતિમ પદ 45 અને સરવાળો 400 છે. શ્રેણીના પદોની સંખ્યા અને સામાન્ય તફાવત શોધો.",
        ["n = 16, d = 8/3", "n = 15, d = 3", "n = 16, d = 3", "n = 17, d = 8/3"],
        ["n = 16, d = 8/3", "n = 15, d = 3", "n = 16, d = 3", "n = 17, d = 8/3"],
        ["n = 16, d = 8/3", "n = 15, d = 3", "n = 16, d = 3", "n = 17, d = 8/3"],
        0,
        "a = 5, l = 45, S_n = 400. S_n = (n/2)(a + l) => 400 = (n/2)(50) => 25n = 400 => n = 16. Then 45 = 5 + 15d => 15d = 40 => d = 8/3.",
        "S_n = (n/2)(5 + 45) = 400 => 25n = 400 => n = 16। 45 = 5 + 15d => d = 40/15 = 8/3।",
        "S_n = (n/2)(5 + 45) = 400 => 25n = 400 => n = 16. 45 = 5 + 15d => d = 8/3."
    ))

    # Q6
    blocks.append(make_quiz(
        "C10M_CH5_EX5.3_Q6",
        "Exercise 5.3 (Q6): The first and the last terms of an AP are 17 and 350 respectively. If the common difference is 9, how many terms are there and what is their sum?",
        "प्रश्नावली 5.3 (Q6): किसी AP के प्रथम और अंतिम पद क्रमशः 17 और 350 हैं। यदि सार्व अंतर 9 है, तो इसमें कितने पद हैं और इनका योग क्या है?",
        "સ્વાધ્યાય 5.3 (Q6): સમાંતર શ્રેણીના પ્રથમ અને અંતિમ પદ અનુક્રમે 17 અને 350 છે. જો સામાન્ય તફાવત 9 હોય, તો તેમાં કેટલા પદ છે અને તેમનો સરવાળો કેટલો થાય?",
        ["n = 38, S_n = 6973", "n = 37, S_n = 6973", "n = 38, S_n = 6873", "n = 39, S_n = 7020"],
        ["n = 38, S_n = 6973", "n = 37, S_n = 6973", "n = 38, S_n = 6873", "n = 39, S_n = 7020"],
        ["n = 38, S_n = 6973", "n = 37, S_n = 6973", "n = 38, S_n = 6873", "n = 39, S_n = 7020"],
        0,
        "a = 17, l = 350, d = 9. 350 = 17 + (n - 1)9 => 9(n - 1) = 333 => n - 1 = 37 => n = 38. S₃₈ = (38/2)(17 + 350) = 19 × 367 = 6973.",
        "350 = 17 + 9(n - 1) => n = 38। S₃₈ = 19(17 + 350) = 19 × 367 = 6973।",
        "350 = 17 + 9(n - 1) => n = 38. S₃₈ = 19 × 367 = 6973."
    ))

    # Q7
    blocks.append(make_quiz(
        "C10M_CH5_EX5.3_Q7",
        "Exercise 5.3 (Q7): Find the sum of first 22 terms of an AP in which d = 7 and 22nd term is 149.",
        "प्रश्नावली 5.3 (Q7): उस AP के प्रथम 22 पदों का योग ज्ञात कीजिए, जिसमें d = 7 है और 22वाँ पद 149 है।",
        "સ્વાધ્યાય 5.3 (Q7): જે સમાંતર શ્રેણીમાં d = 7 અને 22મું પદ 149 હોય, તેના પ્રથમ 22 પદોનો સરવાળો શોધો.",
        ["1661", "1650", "1672", "1640"],
        ["1661", "1650", "1672", "1640"],
        ["1661", "1650", "1672", "1640"],
        0,
        "n = 22, d = 7, a₂₂ = 149. a + 21(7) = 149 => a + 147 = 149 => a = 2. S₂₂ = (22/2)(a + a₂₂) = 11(2 + 149) = 11(151) = 1661.",
        "a + 21(7) = 149 => a = 2। S₂₂ = 11(2 + 149) = 11 × 151 = 1661।",
        "a + 21(7) = 149 => a = 2. S₂₂ = 11(2 + 149) = 1661."
    ))

    # Q8
    blocks.append(make_quiz(
        "C10M_CH5_EX5.3_Q8",
        "Exercise 5.3 (Q8): Find the sum of first 51 terms of an AP whose second and third terms are 14 and 18 respectively.",
        "प्रश्नावली 5.3 (Q8): उस AP के प्रथम 51 पदों का योग ज्ञात कीजिए, जिसके दूसरे और तीसरे पद क्रमशः 14 और 18 हैं।",
        "સ્વાધ્યાય 5.3 (Q8): એક સમાંતર શ્રેણીનું બીજું અને ત્રીજું પદ અનુક્રમે 14 અને 18 હોય, તો તેના પ્રથમ 51 પદોનો સરવાળો શોધો.",
        ["5610", "5510", "5620", "5710"],
        ["5610", "5510", "5620", "5710"],
        ["5610", "5510", "5620", "5710"],
        0,
        "a₂ = 14, a₃ = 18 => d = 18 - 14 = 4. First term a = 14 - 4 = 10. S₅₁ = (51/2)[2(10) + (51 - 1)4] = (51/2)[20 + 200] = (51/2)(220) = 51 × 110 = 5610.",
        "d = 18 - 14 = 4, a = 10। S₅₁ = (51/2)[20 + 200] = 51 × 110 = 5610।",
        "d = 18 - 14 = 4, a = 10. S₅₁ = (51/2)[20 + 200] = 51 × 110 = 5610."
    ))

    # Q9
    blocks.append(make_quiz(
        "C10M_CH5_EX5.3_Q9",
        "Exercise 5.3 (Q9): If the sum of first 7 terms of an AP is 49 and that of 17 terms is 289, find the sum of first n terms.",
        "प्रश्नावली 5.3 (Q9): यदि किसी AP के प्रथम 7 पदों का योग 49 है और प्रथम 17 पदों का योग 289 है, तो इसके प्रथम n पदों का योग ज्ञात कीजिए।",
        "સ્વાધ્યાય 5.3 (Q9): જો સમાંતર શ્રેણીના પ્રથમ 7 પદોનો સરવાળો 49 અને 17 પદોનો સરવાળો 289 હોય, તો તેના પ્રથમ n પદોનો સરવાળો શોધો.",
        ["S_n = n²", "S_n = 2n²", "S_n = n(n + 1)", "S_n = n² + n"],
        ["S_n = n²", "S_n = 2n²", "S_n = n(n + 1)", "S_n = n² + n"],
        ["S_n = n²", "S_n = 2n²", "S_n = n(n + 1)", "S_n = n² + n"],
        0,
        "S₇ = (7/2)(2a + 6d) = 49 => a + 3d = 7. S₁₇ = (17/2)(2a + 16d) = 289 => a + 8d = 17. Subtracting: 5d = 10 => d = 2, a = 1. S_n = (n/2)[2(1) + (n - 1)2] = (n/2)(2n) = n².",
        "a + 3d = 7 और a + 8d = 17 => d = 2, a = 1। S_n = (n/2)[2 + 2n - 2] = n²।",
        "a + 3d = 7 અને a + 8d = 17 => d = 2, a = 1. S_n = (n/2)[2 + 2n - 2] = n²."
    ))

    # Q10.1 & Q10.2
    blocks.append(make_quiz(
        "C10M_CH5_EX5.3_Q10_p1",
        "Exercise 5.3 (Q10.i): Show that a₁, a₂, ..., a_n, ... form an AP where a_n = 3 + 4n. Also find the sum of the first 15 terms.",
        "प्रश्नावली 5.3 (Q10.i): दर्शाइए कि a₁, a₂, ..., a_n, ... से एक AP बनती है, जहाँ a_n = 3 + 4n है। साथ ही प्रथम 15 पदों का योग ज्ञात कीजिए।",
        "સ્વાધ્યાય 5.3 (Q10.i): સાબિત કરો કે a₁, a₂, ..., a_n, ... સમાંતર શ્રેણી બનાવે છે, જ્યાં a_n = 3 + 4n. તેના પ્રથમ 15 પદોનો સરવાળો પણ શોધો.",
        ["Forms an AP (d = 4); S_15 = 525", "Forms an AP (d = 3); S_15 = 520", "Not an AP", "Forms an AP (d = 4); S_15 = 535"],
        ["AP बनती है (d = 4); S_15 = 525", "AP बनती है (d = 3); S_15 = 520", "AP नहीं बनती", "AP बनती है (d = 4); S_15 = 535"],
        ["AP બને છે (d = 4); S_15 = 525", "AP બને છે (d = 3); S_15 = 520", "AP બનતી નથી", "AP બને છે (d = 4); S_15 = 535"],
        0,
        "a_n = 3 + 4n. Terms: a₁ = 7, a₂ = 11, a₃ = 15. Common difference d = 11 - 7 = 4 (constant). S₁₅ = (15/2)[2(7) + 14(4)] = (15/2)[14 + 56] = (15/2)(70) = 525.",
        "a₁ = 7, a₂ = 11, a₃ = 15 => d = 4 (स्थिर)। S₁₅ = (15/2)[14 + 56] = 15 × 35 = 525।",
        "a₁ = 7, a₂ = 11 => d = 4. S₁₅ = (15/2)(70) = 525."
    ))

    blocks.append(make_quiz(
        "C10M_CH5_EX5.3_Q10_p2",
        "Exercise 5.3 (Q10.ii): Show that a₁, a₂, ..., a_n, ... form an AP where a_n = 9 - 5n. Also find the sum of the first 15 terms.",
        "प्रश्नावली 5.3 (Q10.ii): दर्शाइए कि a₁, a₂, ..., a_n, ... से एक AP बनती है, जहाँ a_n = 9 - 5n है। साथ ही प्रथम 15 पदों का योग ज्ञात कीजिए।",
        "સ્વાધ્યાય 5.3 (Q10.ii): સાબિત કરો કે a₁, a₂, ..., a_n, ... સમાંતર શ્રેણી બનાવે છે, જ્યાં a_n = 9 - 5n. તેના પ્રથમ 15 પદોનો સરવાળો પણ શોધો.",
        ["Forms an AP (d = -5); S_15 = -465", "Forms an AP (d = 5); S_15 = 465", "Not an AP", "Forms an AP (d = -5); S_15 = -450"],
        ["AP बनती है (d = -5); S_15 = -465", "AP बनती है (d = 5); S_15 = 465", "AP नहीं बनती", "AP बनती है (d = -5); S_15 = -450"],
        ["AP બને છે (d = -5); S_15 = -465", "AP બને છે (d = 5); S_15 = 465", "AP બનતી નથી", "AP બને છે (d = -5); S_15 = -450"],
        0,
        "a_n = 9 - 5n. Terms: a₁ = 4, a₂ = -1, a₃ = -6. d = -1 - 4 = -5 (constant). S₁₅ = (15/2)[2(4) + 14(-5)] = (15/2)[8 - 70] = (15/2)(-62) = -465.",
        "a₁ = 4, a₂ = -1 => d = -5। S₁₅ = (15/2)[8 - 70] = 15 × (-31) = -465।",
        "a₁ = 4, a₂ = -1 => d = -5. S₁₅ = (15/2)(-62) = -465."
    ))

    # Q11
    blocks.append(make_quiz(
        "C10M_CH5_EX5.3_Q11",
        "Exercise 5.3 (Q11): If the sum of the first n terms of an AP is 4n - n², what is the first term (S₁)? What is the sum of first two terms? What is the second term? Similarly, find the 3rd, the 10th and the nth terms.",
        "प्रश्नावली 5.3 (Q11): यदि किसी AP के प्रथम n पदों का योग 4n - n² है, तो इसका प्रथम पद क्या है? प्रथम दो पदों का योग क्या है? दूसरा पद क्या है? इसी प्रकार, तीसरे, 10वें और nवें पद ज्ञात कीजिए।",
        "સ્વાધ્યાય 5.3 (Q11): જો કોઈ સમાંતર શ્રેણીના પ્રથમ n પદોનો સરવાળો 4n - n² હોય, તો તેનું પ્રથમ પદ કયું હશે? પ્રથમ બે પદોનો સરવાળો કેટલો હશે? બીજું પદ કયું હશે? આ જ રીતે ત્રીજું, 10મું અને nમું પદ શોધો.",
        [
            "S₁ = 3, S₂ = 4, a₂ = 1, a₃ = -1, a₁₀ = -15, a_n = 5 - 2n",
            "S₁ = 3, S₂ = 4, a₂ = 2, a₃ = 0, a₁₀ = -14, a_n = 5 - n",
            "S₁ = 4, S₂ = 6, a₂ = 2, a₃ = -1, a₁₀ = -15, a_n = 4 - 2n",
            "S₁ = 3, S₂ = 5, a₂ = 2, a₃ = 1, a₁₀ = -13, a_n = 5 - 2n"
        ],
        [
            "S₁ = 3, S₂ = 4, a₂ = 1, a₃ = -1, a₁₀ = -15, a_n = 5 - 2n",
            "S₁ = 3, S₂ = 4, a₂ = 2, a₃ = 0, a₁₀ = -14, a_n = 5 - n",
            "S₁ = 4, S₂ = 6, a₂ = 2, a₃ = -1, a₁₀ = -15, a_n = 4 - 2n",
            "S₁ = 3, S₂ = 5, a₂ = 2, a₃ = 1, a₁₀ = -13, a_n = 5 - 2n"
        ],
        [
            "S₁ = 3, S₂ = 4, a₂ = 1, a₃ = -1, a₁₀ = -15, a_n = 5 - 2n",
            "S₁ = 3, S₂ = 4, a₂ = 2, a₃ = 0, a₁₀ = -14, a_n = 5 - n",
            "S₁ = 4, S₂ = 6, a₂ = 2, a₃ = -1, a₁₀ = -15, a_n = 4 - 2n",
            "S₁ = 3, S₂ = 5, a₂ = 2, a₃ = 1, a₁₀ = -13, a_n = 5 - 2n"
        ],
        0,
        "S_n = 4n - n². S₁ = 4(1) - 1² = 3 (First term a = 3). S₂ = 4(2) - 2² = 4. a₂ = S₂ - S₁ = 4 - 3 = 1. d = a₂ - a₁ = 1 - 3 = -2. a₃ = a + 2d = 3 + 2(-2) = -1. a₁₀ = 3 + 9(-2) = -15. a_n = S_n - S_{n-1} = 5 - 2n.",
        "S₁ = 3 (प्रथम पद)। S₂ = 4। a₂ = 4 - 3 = 1। d = -2। a₃ = -1, a₁₀ = -15, a_n = 5 - 2n।",
        "S₁ = 3 (પ્રથમ પદ). S₂ = 4. a₂ = 1. d = -2. a₃ = -1, a₁₀ = -15, a_n = 5 - 2n."
    ))

    # Q12
    blocks.append(make_quiz(
        "C10M_CH5_EX5.3_Q12",
        "Exercise 5.3 (Q12): Find the sum of the first 40 positive integers divisible by 6.",
        "प्रश्नावली 5.3 (Q12): ऐसे प्रथम 40 धन पूर्णांकों का योग ज्ञात कीजिए जो 6 से विभाज्य हैं।",
        "સ્વાધ્યાય 5.3 (Q12): 6 વડે વિભાજ્ય હોય તેવા પ્રથમ 40 ધન પૂર્ણાંકોનો સરવાળો શોધો.",
        ["4920", "4820", "5020", "4960"],
        ["4920", "4820", "5020", "4960"],
        ["4920", "4820", "5020", "4960"],
        0,
        "Integers are: 6, 12, 18, ..., to 40 terms. a = 6, d = 6, n = 40. S₄₀ = (40/2)[2(6) + (39)(6)] = 20[12 + 234] = 20(246) = 4920.",
        "AP: 6, 12, 18... a = 6, d = 6, n = 40। S₄₀ = 20(12 + 234) = 20 × 246 = 4920।",
        "AP: 6, 12, 18... a = 6, d = 6, n = 40. S₄₀ = 20 × 246 = 4920."
    ))

    # Q13
    blocks.append(make_quiz(
        "C10M_CH5_EX5.3_Q13",
        "Exercise 5.3 (Q13): Find the sum of the first 15 multiples of 8.",
        "प्रश्नावली 5.3 (Q13): 8 के प्रथम 15 गुणजों का योग ज्ञात कीजिए।",
        "સ્વાધ્યાય 5.3 (Q13): 8 ના પ્રથમ 15 ગુણિતોનો સરવાળો શોધો.",
        ["960", "940", "980", "1000"],
        ["960", "940", "980", "1000"],
        ["960", "940", "980", "1000"],
        0,
        "Multiples of 8: 8, 16, 24, ... to 15 terms. a = 8, d = 8, n = 15. S₁₅ = (15/2)[2(8) + (14)(8)] = (15/2)[16 + 112] = (15/2)(128) = 15 × 64 = 960.",
        "AP: 8, 16, 24... a = 8, d = 8, n = 15। S₁₅ = (15/2)(128) = 15 × 64 = 960।",
        "AP: 8, 16, 24... a = 8, d = 8, n = 15. S₁₅ = 15 × 64 = 960."
    ))

    # Q14
    blocks.append(make_quiz(
        "C10M_CH5_EX5.3_Q14",
        "Exercise 5.3 (Q14): Find the sum of the odd numbers between 0 and 50.",
        "प्रश्नावली 5.3 (Q14): 0 और 50 के बीच की विषम संख्याओं का योग ज्ञात कीजिए।",
        "સ્વાધ્યાય 5.3 (Q14): 0 અને 50 વચ્ચેના અયુગ્મ પૂર્ણાંકોનો સરવાળો શોધો.",
        ["625", "650", "600", "576"],
        ["625", "650", "600", "576"],
        ["625", "650", "600", "576"],
        0,
        "Odd numbers: 1, 3, 5, ..., 49. a = 1, d = 2, l = 49. 49 = 1 + (n - 1)2 => 2(n - 1) = 48 => n = 25. S₂₅ = (25/2)(1 + 49) = (25/2)(50) = 25 × 25 = 625.",
        "विषम संख्याएँ: 1, 3, 5, ..., 49। n = 25। S₂₅ = (25/2)(1 + 49) = 25 × 25 = 625।",
        "અયુગ્મ સંખ્યાઓ: 1, 3, ..., 49. n = 25. S₂₅ = 25 × 25 = 625."
    ))

    # Q15
    blocks.append(make_quiz(
        "C10M_CH5_EX5.3_Q15",
        "Exercise 5.3 (Q15): A contract on construction job specifies a penalty for delay of completion beyond a certain date as follows: ₹200 for the first day, ₹250 for the second day, ₹300 for the third day, etc., the penalty for each succeeding day being ₹50 more than for the preceding day. How much money the contractor has to pay as penalty, if he has delayed the work by 30 days?",
        "प्रश्नावली 5.3 (Q15): निर्माण कार्य से संबंधित किसी ठेके में, एक निश्चित तिथि के बाद कार्य को विलंब से पूरा करने के लिए जुर्माना लगाने का प्रावधान इस प्रकार है: पहले दिन के लिए ₹200, दूसरे दिन के लिए ₹250, तीसरे दिन के लिए ₹300 इत्यादि, अर्थात् प्रत्येक उत्तरोत्तर दिन का जुर्माना अपने से ठीक पहले दिन के जुर्माने से ₹50 अधिक है। एक ठेकेदार को जुर्माने के रूप में कितनी राशि अदा करनी पड़ेगी, यदि वह इस कार्य में 30 दिन का विलंब कर देता है?",
        "સ્વાધ્યાય 5.3 (Q15): નિર્માણ કામના કરારમાં નિશ્ચિત તારીખ કરતાં વિલંબ થાય તો દંડની જોગવાઈ નીચે મુજબ છે: પ્રથમ દિવસ માટે ₹200, બીજા દિવસ માટે ₹250, ત્રીજા દિવસ માટે ₹300 વગેરે. પ્રત્યેક દિવસનો દંડ તેના આગળના દિવસ કરતાં ₹50 વધુ છે. જો કોન્ટ્રાક્ટર 30 દિવસનો વિલંબ કરે તો તેને કેટલો દંડ ભરવો પડશે?",
        ["₹27,750", "₹27,500", "₹28,000", "₹26,750"],
        ["₹27,750", "₹27,500", "₹28,000", "₹26,750"],
        ["₹27,750", "₹27,500", "₹28,000", "₹26,750"],
        0,
        "Here a = 200, d = 50, n = 30. S₃₀ = (30/2)[2(200) + (30 - 1)(50)] = 15[400 + 1450] = 15(1850) = ₹27,750.",
        "a = 200, d = 50, n = 30। S₃₀ = 15[400 + 1450] = 15 × 1850 = ₹27,750।",
        "a = 200, d = 50, n = 30. S₃₀ = 15[400 + 1450] = 15 × 1850 = ₹27,750."
    ))

    # Q16
    blocks.append(make_quiz(
        "C10M_CH5_EX5.3_Q16",
        "Exercise 5.3 (Q16): A sum of ₹700 is to be used to give seven cash prizes to students of a school for their overall academic performance. If each prize is ₹20 less than its preceding prize, find the value of each of the prizes.",
        "प्रश्नावली 5.3 (Q16): किसी स्कूल के विद्यार्थियों को उनके समग्र शैक्षिक प्रदर्शन के लिए 7 नकद पुरस्कार देने के लिए ₹700 की राशि रखी गई है। यदि प्रत्येक पुरस्कार अपने से ठीक पहले पुरस्कार से ₹20 कम है, तो प्रत्येक पुरस्कार का मान ज्ञात कीजिए।",
        "સ્વાધ્યાય 5.3 (Q16): કોઈ શાળામાં વિદ્યાર્થીઓને સમગ્ર શૈક્ષણિક પ્રદર્શન માટે 7 રોકડ પુરસ્કારો આપવા માટે કુલ ₹700 ની જોગવાઈ છે. જો પ્રત્યેક પુરસ્કાર તેના આગળના પુરસ્કાર કરતાં ₹20 ઓછો હોય, તો પ્રત્યેક પુરસ્કારનું મૂલ્ય શોધો.",
        [
            "₹160, ₹140, ₹120, ₹100, ₹80, ₹60, ₹40",
            "₹150, ₹130, ₹110, ₹90, ₹70, ₹50, ₹30",
            "₹170, ₹150, ₹130, ₹110, ₹90, ₹70, ₹50",
            "₹160, ₹140, ₹120, ₹100, ₹80, ₹50, ₹30"
        ],
        [
            "₹160, ₹140, ₹120, ₹100, ₹80, ₹60, ₹40",
            "₹150, ₹130, ₹110, ₹90, ₹70, ₹50, ₹30",
            "₹170, ₹150, ₹130, ₹110, ₹90, ₹70, ₹50",
            "₹160, ₹140, ₹120, ₹100, ₹80, ₹50, ₹30"
        ],
        [
            "₹160, ₹140, ₹120, ₹100, ₹80, ₹60, ₹40",
            "₹150, ₹130, ₹110, ₹90, ₹70, ₹50, ₹30",
            "₹170, ₹150, ₹130, ₹110, ₹90, ₹70, ₹50",
            "₹160, ₹140, ₹120, ₹100, ₹80, ₹50, ₹30"
        ],
        0,
        "n = 7, S₇ = 700, d = -20. S₇ = (7/2)[2a + 6(-20)] = 700 => (7/2)(2a - 120) = 700 => 2a - 120 = 200 => 2a = 320 => a = 160. The 7 prizes are: ₹160, ₹140, ₹120, ₹100, ₹80, ₹60, ₹40.",
        "(7/2)[2a - 120] = 700 => 2a - 120 = 200 => a = 160। पुरस्कार हैं: ₹160, ₹140, ₹120, ₹100, ₹80, ₹60, ₹40।",
        "(7/2)[2a - 120] = 700 => a = 160. પુરસ્કારો: ₹160, ₹140, ₹120, ₹100, ₹80, ₹60, ₹40."
    ))

    # Q17
    blocks.append(make_quiz(
        "C10M_CH5_EX5.3_Q17",
        "Exercise 5.3 (Q17): In a school, students thought of planting trees in and around the school to reduce air pollution. It was decided that the number of trees, that each section of each class will plant, will be the same as the class, in which they are studying (e.g. section of Class I will plant 1 tree, Class II will plant 2 trees and so on till Class XII). There are three sections of each class. How many trees will be planted by the students?",
        "प्रश्नावली 5.3 (Q17): एक स्कूल के विद्यार्थियों ने वायु प्रदूषण कम करने के लिए स्कूल के अंदर और बाहर पेड़ लगाने के बारे में सोचा। यह निर्णय लिया गया कि प्रत्येक कक्षा का प्रत्येक अनुभाग अपनी कक्षा की संख्या के बराबर पेड़ लगाएगा (कक्षा I का एक अनुभाग 1 पेड़, कक्षा II का 2 पेड़... कक्षा XII का 12 पेड़ लगाएगा)। प्रत्येक कक्षा के तीन अनुभाग हैं। विद्यार्थियों द्वारा लगाए गए कुल पेड़ों की संख्या कितनी होगी?",
        "સ્વાધ્યાય 5.3 (Q17): એક શાળાના વિદ્યાર્થીઓએ વાયુ પ્રદૂષણ ઘટાડવા માટે શાળાની અંદર અને બહાર વૃક્ષો વાવવાનું નક્કી કર્યું. એવું નક્કી કરાયું કે દરેક ધોરણનો દરેક વર્ગ તે જે ધોરણમાં ભણતો હોય તેટલા વૃક્ષ વાવશે (દા.ત. ધોરણ I નો એક વર્ગ 1 વૃક્ષ, ધોરણ II નો 2 વૃક્ષ... ધોરણ XII નો 12 વૃક્ષ). દરેક ધોરણના ત્રણ વર્ગ (sections) છે. વિદ્યાર્થીઓ દ્વારા કુલ કેટલા વૃક્ષો વવાશે?",
        ["234 trees", "224 trees", "244 trees", "216 trees"],
        ["234 पेड़", "224 पेड़", "244 पेड़", "216 पेड़"],
        ["234 વૃક્ષો", "224 વૃક્ષો", "244 વૃક્ષો", "216 વૃક્ષો"],
        0,
        "Trees planted by each class (with 3 sections): Class 1 = 3(1) = 3, Class 2 = 3(2) = 6, ..., Class 12 = 3(12) = 36. AP: 3, 6, 9, ..., 36. a = 3, d = 3, n = 12. S₁₂ = (12/2)(3 + 36) = 6(39) = 234 trees.",
        "प्रत्येक कक्षा द्वारा: 3, 6, 9, ..., 36। n = 12। S₁₂ = 6(3 + 36) = 6 × 39 = 234 पेड़।",
        "દરેક ધોરણ દ્વારા: 3, 6, 9, ..., 36. n = 12. S₁₂ = 6(3 + 36) = 6 × 39 = 234 વૃક્ષો."
    ))

    # Q18
    blocks.append(make_quiz(
        "C10M_CH5_EX5.3_Q18",
        "Exercise 5.3 (Q18): A spiral is made up of successive semicircles, with centres alternately at A and B, starting with centre at A, of radii 0.5 cm, 1.0 cm, 1.5 cm, 2.0 cm, ... What is the total length of such a spiral made up of thirteen consecutive semicircles? (Take π = 22/7)",
        "प्रश्नावली 5.3 (Q18): केंद्र A से प्रारंभ करते हुए, बारी-बारी से केंद्रों A और B को लेते हुए, त्रिज्याओं 0.5 cm, 1.0 cm, 1.5 cm, 2.0 cm, ... वाले उत्तरोत्तर अर्धवृत्तों को खींचकर एक सर्पिल (spiral) बनाया गया है। तेरह क्रमागत अर्धवृत्तों से बने इस सर्पिल की कुल लंबाई क्या है? (π = 22/7 लीजिए)",
        "સ્વાધ્યાય 5.3 (Q18): વારાફરતી A અને B ને કેન્દ્ર લઈ ક્રમિક અર્ધવર્તુળોની મદદથી એક કુંતલ (spiral) બનાવેલ છે. તેની શરૂઆત A થી થાય છે. ત્રિજ્યાઓ 0.5 cm, 1.0 cm, 1.5 cm, 2.0 cm, ... છે. આવા 13 ક્રમિક અર્ધવર્તુળોથી બનતા કુંતલની કુલ લંબાઈ કેટલી થશે? (π = 22/7 લો)",
        ["143 cm", "132 cm", "154 cm", "144 cm"],
        ["143 cm", "132 cm", "154 cm", "144 cm"],
        ["143 cm", "132 cm", "154 cm", "144 cm"],
        0,
        "Length of semicircle of radius r is πr. The lengths are: π(0.5), π(1.0), π(1.5), ..., π(6.5). Total length = π[0.5 + 1.0 + 1.5 + ... to 13 terms]. Sum = (13/2)(0.5 + 6.5) = (13/2)(7) = 91/2. Total length = (22/7) × (91/2) = 11 × 13 = 143 cm.",
        "अर्धवृत्त की लंबाई = πr। कुल लंबाई = π[0.5 + 1.0 + ... 13 पदों तक] = (22/7) × (13/2)(7) = 11 × 13 = 143 cm।",
        "અર્ધવર્તુળની લંબાઈ = πr. કુલ લંબાઈ = (22/7) × (13/2)(7) = 11 × 13 = 143 cm."
    ))

    # Q19
    blocks.append(make_quiz(
        "C10M_CH5_EX5.3_Q19",
        "Exercise 5.3 (Q19): 200 logs are stacked in the following manner: 20 logs in the bottom row, 19 in the next row, 18 in the row next to it and so on. In how many rows are the 200 logs placed and how many logs are in the top row?",
        "प्रश्नावली 5.3 (Q19): 200 लट्ठों (logs) को ढेरी के रूप में इस प्रकार रखा जाता है: सबसे नीचे वाली पंक्ति में 20 लट्ठे, उससे अगली पंक्ति में 19 लट्ठे, उससे अगली पंक्ति में 18 लट्ठे, इत्यादि। ये 200 लट्ठे कितनी पंक्तियों में रखे गए हैं तथा सबसे ऊपरी पंक्ति में कितने लट्ठे हैं?",
        "સ્વાધ્યાય 5.3 (Q19): 200 લાકડાના ભારીયાઓ (logs) નીચે પ્રમાણે ગોઠવવામાં આવ્યા છે: તળિયેની હારમાં 20, તેની ઉપરની હારમાં 19, તેની ઉપર 18 વગેરે. આ 200 ભારીયાઓ કેટલી હારમાં મુકાયા હશે અને સૌથી ઉપરની હારમાં કેટલા ભારીયા હશે?",
        [
            "16 rows; 5 logs in top row",
            "25 rows; -4 logs in top row",
            "15 rows; 6 logs in top row",
            "16 rows; 4 logs in top row"
        ],
        [
            "16 पंक्तियाँ; सबसे ऊपरी पंक्ति में 5 लट्ठे",
            "25 पंक्तियाँ; सबसे ऊपरी पंक्ति में -4 लट्ठे",
            "15 पंक्तियाँ; सबसे ऊपरी पंक्ति में 6 लट्ठे",
            "16 पंक्तियाँ; सबसे ऊपरी पंक्ति में 4 लट्ठे"
        ],
        [
            "16 હાર; સૌથી ઉપરની હારમાં 5 ભારીયા",
            "25 હાર; સૌથી ઉપરની હારમાં -4 ભારીયા",
            "15 હાર; સૌથી ઉપરની હારમાં 6 ભારીયા",
            "16 હાર; સૌથી ઉપરની હારમાં 4 ભારીયા"
        ],
        0,
        "a = 20, d = -1, S_n = 200. (n/2)[2(20) + (n - 1)(-1)] = 200 => n(41 - n) = 400 => n² - 41n + 400 = 0 => (n - 16)(n - 25) = 0. If n = 25, a₂₅ = 20 + 24(-1) = -4 (impossible). Thus n = 16 rows. Logs in top row = a₁₆ = 20 + 15(-1) = 5 logs.",
        "n² - 41n + 400 = 0 => (n - 16)(n - 25) = 0। यदि n = 25, तो a₂₅ = -4 (असंभव)। अतः n = 16 पंक्तियाँ। सबसे ऊपरी पंक्ति में a₁₆ = 20 - 15 = 5 लट्ठे।",
        "n² - 41n + 400 = 0 => n = 16 (કારણ કે n = 25 માટે પદો ઋણ બને જે અશક્ય છે). ટોચની હારમાં પદ a₁₆ = 20 - 15 = 5 ભારીયા."
    ))

    # Q20
    blocks.append(make_quiz(
        "C10M_CH5_EX5.3_Q20",
        "Exercise 5.3 (Q20): In a potato race, a bucket is placed at the starting point, which is 5 m from the first potato, and the other potatoes are placed 3 m apart in a straight line. There are ten potatoes in the line. A competitor starts from the bucket, picks up the nearest potato, runs back with it, drops it in the bucket, runs back to pick up the next potato, runs to the bucket to drop it in, and she continues in the same way until all the potatoes are in the bucket. What is the total distance the competitor has to run?",
        "प्रश्नावली 5.3 (Q20): एक आलू दौड़ (potato race) में, प्रारंभिक स्थान पर एक बाल्टी रखी हुई है, जो पहले आलू से 5 m की दूरी पर है, तथा अन्य आलुओं को एक सीधी रेखा में परस्पर 3 m की दूरियों पर रखा गया है। इस रेखा पर 10 आलू रखे गए हैं। प्रत्येक प्रतियोगी बाल्टी से चलना प्रारंभ करता है, निकटतम आलू को उठाता है, उसे लेकर वापस दौड़कर बाल्टी में डालता है, दूसरा आलू उठाने के लिए वापस दौड़ता है, उसे उठाकर वापस बाल्टी में डालता है, और वह ऐसा तब तक करती रहती है, जब तक कि सभी आलू बाल्टी में न आ जाएँ। इसमें प्रतियोगी को कुल कितनी दूरी दौड़नी पड़ेगी?",
        "સ્વાધ્યાય 5.3 (Q20): એક બટાકાની દોડ (potato race) માં, પ્રારંભિક બિંદુ પર એક ડોલ રાખેલી છે, જે પ્રથમ બટાકાથી 5 m દૂર છે અને બાકીના બટાકા સીધી રેખામાં એકબીજાથી 3 m ના અંતરે ગોઠવાયેલા છે. આવા 10 બટાકા મૂકેલા છે. સ્પર્ધકે ડોલ પાસેથી દોડી નજીકનું બટાકું લઈ ડોલમાં નાખવાનું, પછી બીજું બટાકું લઈ પાછા આવી ડોલમાં નાખવાનું. બધા 10 બટાકા ડોલમાં મુકાય ત્યાં સુધી આ ચાલુ રહે છે. સ્પર્ધકે કુલ કેટલું અંતર દોડવું પડશે?",
        ["740 m", "720 m", "760 m", "700 m"],
        ["740 m", "720 m", "760 m", "700 m"],
        ["740 m", "720 m", "760 m", "700 m"],
        0,
        "Distance to pick 1st potato and return = 2 × 5 = 10 m. For 2nd potato = 2 × (5 + 3) = 16 m. For 3rd potato = 2 × (5 + 3 + 3) = 22 m. AP: 10, 16, 22, ... to 10 terms. a = 10, d = 6, n = 10. S₁₀ = (10/2)[2(10) + (9)(6)] = 5[20 + 54] = 5(74) = 370 m per way × 2 = 740 m total.",
        "दूरी AP: 10, 16, 22, ... (10 पद)। a = 10, d = 6, n = 10। S₁₀ = 5[20 + 54] = 5 × 74 = 370 × 2... कुल दूरी = 5 × 74 = 370 m... प्रतीक्षा करें: 10, 16, 22... का योग = 5(20 + 54) = 370 m... नहीं! 2 × (5 + 8 + 11 + ... + 32) = 2 × 370 = 740 m। कुल दूरी 740 m है।",
        "દરેક બટાકા માટેનું અંતર: 10, 16, 22... (10 પદો). a = 10, d = 6, n = 10. S₁₀ = 5[20 + 54] = 5 × 74 = 370... કુલ અંતર = 740 m."
    ))

    return blocks

def get_part4_blocks():
    blocks = []

    # =========================================================================
    # EXERCISE 5.4 (OPTIONAL / ADVANCED MASTERY - QUESTIONS 1 to 5)
    # =========================================================================
    # Q1
    blocks.append(make_quiz(
        "C10M_CH5_EX5.4_Q1",
        "Exercise 5.4 (Q1): Which term of the AP: 121, 117, 113, ... is its first negative term?",
        "प्रश्नावली 5.4 (Q1): AP: 121, 117, 113, ... का कौन सा पद सबसे पहला ऋणात्मक पद होगा?",
        "સ્વાધ્યાય 5.4 (Q1): સમાંતર શ્રેણી 121, 117, 113, ... નું પ્રથમ ઋણ પદ કયું હશે?",
        ["32nd term", "31st term", "33rd term", "30th term"],
        ["32वाँ पद", "31वाँ पद", "33वाँ पद", "30वाँ पद"],
        ["32મું પદ", "31મું પદ", "33મું પદ", "30મું પદ"],
        0,
        "a = 121, d = 117 - 121 = -4. We need a_n < 0 => 121 + (n - 1)(-4) < 0 => 121 - 4n + 4 < 0 => 125 < 4n => n > 125/4 => n > 31.25. The least natural number greater than 31.25 is n = 32. Thus, the 32nd term is the first negative term.",
        "a = 121, d = -4। a_n < 0 => 121 - 4(n - 1) < 0 => 4n > 125 => n > 31.25। अतः पहला ऋणात्मक पद 32वाँ पद होगा।",
        "a = 121, d = -4. a_n < 0 => 4n > 125 => n > 31.25. તેથી પ્રથમ ઋણ પદ 32મું પદ થશે."
    ))

    # Q2
    blocks.append(make_quiz(
        "C10M_CH5_EX5.4_Q2",
        "Exercise 5.4 (Q2): The sum of the third and the seventh terms of an AP is 6 and their product is 8. Find the sum of first sixteen terms of the AP.",
        "प्रश्नावली 5.4 (Q2): किसी AP के तीसरे और सातवें पदों का योग 6 है और उनका गुणनफल 8 है। इस AP के प्रथम 16 पदों का योग ज्ञात कीजिए।",
        "સ્વાધ્યાય 5.4 (Q2): એક સમાંતર શ્રેણીના ત્રીજા અને સાતમા પદોનો સરવાળો 6 અને તેમનો ગુણાકાર 8 છે, તો તે સમાંતર શ્રેણીના પ્રથમ 16 પદોનો સરવાળો શોધો.",
        ["76 or 20 (Two possible answers)", "76 only", "20 only", "80 or 24"],
        ["76 या 20 (दो संभावित उत्तर)", "केवल 76", "केवल 20", "80 या 24"],
        ["76 અથવા 20 (બે સંભવિત જવાબો)", "માત્ર 76", "માત્ર 20", "80 અથવા 24"],
        0,
        "a₃ + a₇ = (a + 2d) + (a + 6d) = 2a + 8d = 6 => a + 4d = 3 => a = 3 - 4d. Product: (a + 2d)(a + 6d) = (3 - 2d)(3 + 2d) = 9 - 4d² = 8 => 4d² = 1 => d = ±1/2. Case 1: d = 1/2 => a = 1 => S₁₆ = 8[2(1) + 15(1/2)] = 8[2 + 15/2] = 76. Case 2: d = -1/2 => a = 5 => S₁₆ = 8[2(5) + 15(-1/2)] = 8[10 - 15/2] = 20.",
        "a + 4d = 3। (3 - 2d)(3 + 2d) = 8 => 9 - 4d² = 8 => d = ±1/2। यदि d = 1/2, S₁₆ = 76। यदि d = -1/2, S₁₆ = 20। दो संभावित उत्तर हैं: 76 या 20।",
        "a + 4d = 3. 9 - 4d² = 8 => d = ±1/2. જો d = 1/2, S₁₆ = 76. જો d = -1/2, S₁₆ = 20."
    ))

    # Q3
    blocks.append(make_quiz(
        "C10M_CH5_EX5.4_Q3",
        "Exercise 5.4 (Q3): A ladder has rungs 25 cm apart. The rungs decrease uniformly in length from 45 cm at the bottom to 25 cm at the top. If the top and bottom rungs are 2 1/2 m apart, what is the length of the wood required for the rungs?",
        "प्रश्नावली 5.4 (Q3): एक सीढ़ी के डंडे परस्पर 25 cm की दूरी पर हैं। डंडों की लंबाई एक समान रूप से घटती जाती है तथा सबसे निचले डंडे की लंबाई 45 cm है और सबसे ऊपर वाले डंडे की लंबाई 25 cm है। यदि ऊपरी और निचले डंडे के बीच की दूरी 2 1/2 m है, तो डंडों के लिए कितनी लकड़ी की आवश्यकता होगी?",
        "સ્વાધ્યાય 5.4 (Q3): એક સીડીના બે ક્રમિક પગથિયા વચ્ચેનું અંતર 25 cm છે. પગથિયાની લંબાઈ સમાન રીતે ઘટતી જાય છે. સૌથી નીચેના પગથિયાની લંબાઈ 45 cm અને સૌથી ઉપરના પગથિયાની લંબાઈ 25 cm છે. જો સૌથી ઉપર અને સૌથી નીચેના પગથિયા વચ્ચેનું અંતર 2 1/2 m હોય, તો પગથિયા માટે કેટલી લંબાઈનું લાકડું જોઈશે?",
        ["385 cm", "375 cm", "395 cm", "360 cm"],
        ["385 cm", "375 cm", "395 cm", "360 cm"],
        ["385 cm", "375 cm", "395 cm", "360 cm"],
        0,
        "Total distance between top and bottom rungs = 2 1/2 m = 250 cm. Distance between consecutive rungs = 25 cm. Number of rungs n = (250 / 25) + 1 = 10 + 1 = 11. Bottom rung a = 45 cm, top rung l = 25 cm. Total length of wood S₁₁ = (11/2)(a + l) = (11/2)(45 + 25) = (11/2)(70) = 11 × 35 = 385 cm.",
        "डंडों की संख्या n = (250 / 25) + 1 = 11। a = 45 cm, l = 25 cm। लकड़ी की कुल लंबाई S₁₁ = (11/2)(45 + 25) = 11 × 35 = 385 cm।",
        "પગથિયાંની સંખ્યા n = (250 / 25) + 1 = 11. a = 45, l = 25. લાકડાની લંબાઈ S₁₁ = (11/2)(70) = 385 cm."
    ))

    # Q4
    blocks.append(make_quiz(
        "C10M_CH5_EX5.4_Q4",
        "Exercise 5.4 (Q4): The houses of a row are numbered consecutively from 1 to 49. Show that there is a value of x such that the sum of the numbers of the houses preceding the house numbered x is equal to the sum of the numbers of the houses following it. Find this value of x.",
        "प्रश्नावली 5.4 (Q4): एक पंक्ति के मकानों को क्रमागत रूप से 1 से 49 तक क्रमांकित किया गया है। दर्शाइए कि x का एक ऐसा मान है कि x से अंकित मकान से पहले के मकानों के नंबरों का योग उसके बाद के मकानों के नंबरों के योग के बराबर है। x का मान ज्ञात कीजिए।",
        "સ્વાધ્યાય 5.4 (Q4): એક હારમાં રહેલા મકાનોના નંબર ક્રમિક રીતે 1 થી 49 છે. સાબિત કરો કે x નું એવું મૂલ્ય મળે જેથી x નંબરવાળા મકાનની આગળના મકાનોના નંબરોનો સરવાળો, તેની પાછળના મકાનોના નંબરોના સરવાળા જેટલો થાય. x નું મૂલ્ય શોધો.",
        ["x = 35", "x = 36", "x = 34", "x = 30"],
        ["x = 35", "x = 36", "x = 34", "x = 30"],
        ["x = 35", "x = 36", "x = 34", "x = 30"],
        0,
        "Sum of houses 1 to (x - 1) = S_{x-1}. Sum of houses from (x + 1) to 49 = S₄₉ - S_x. Setting them equal: S_{x-1} = S₄₉ - S_x => [(x - 1)x]/2 = [49 × 50]/2 - [x(x + 1)]/2. Multiplying by 2: x² - x + x² + x = 2450 => 2x² = 2450 => x² = 1225 => x = 35.",
        "S_{x-1} = S₄₉ - S_x => x(x - 1)/2 + x(x + 1)/2 = 49 × 50 / 2 => 2x² / 2 = 1225 => x² = 1225 => x = 35।",
        "S_{x-1} = S₄₉ - S_x => x² = 1225 => x = 35."
    ))

    # Q5
    blocks.append(make_quiz(
        "C10M_CH5_EX5.4_Q5",
        "Exercise 5.4 (Q5): A small terrace at a football ground comprises of 15 steps each of which is 50 m long and built of solid concrete. Each step has a rise of 1/4 m and a tread of 1/2 m. Calculate the total volume of concrete required to build the terrace.",
        "प्रश्नावली 5.4 (Q5): एक फुटबॉल के मैदान में एक छोटा चबूतरा है जिसमें 15 सीढ़ियाँ बनी हुई हैं। इनमें से प्रत्येक सीढ़ी की लंबाई 50 m है और वह ठोस कंक्रीट की बनी है। प्रत्येक सीढ़ी का फैलाव (tread) 1/2 m है और ऊँचाई (rise) 1/4 m है। इस चबूतरे को बनाने में लगी कंक्रीट का कुल आयतन परिकलित कीजिए।",
        "સ્વાધ્યાય 5.4 (Q5): ફૂટબોલના મેદાનમાં એક નાનો ઓટો (ચબૂતરો) છે, જેમાં 15 પગથિયાં છે. દરેક પગથિયાની લંબાઈ 50 m છે અને તે નક્કર કોંક્રીટથી બનેલું છે. દરેક પગથિયાની ઊંચાઈ 1/4 m અને પહોળાઈ 1/2 m છે. આ ઓટો બનાવવા માટે વપરાયેલ કોંક્રીટનું કુલ ઘનફળ શોધો.",
        ["750 m³", "720 m³", "780 m³", "700 m³"],
        ["750 m³", "720 m³", "780 m³", "700 m³"],
        ["750 m³", "720 m³", "780 m³", "700 m³"],
        0,
        "Volume of 1st step = 50 × 1/2 × 1/4 = 25/4 m³. Volume of 2nd step = 50 × 1/2 × (2 × 1/4) = 2 × (25/4) m³. Volume of nth step = n × (25/4) m³. Total volume = (25/4)[1 + 2 + ... + 15] = (25/4) × [(15 × 16)/2] = (25/4) × 120 = 25 × 30 = 750 m³.",
        "पहले पायदान का आयतन = 50 × 1/2 × 1/4 = 25/4 m³। कुल आयतन = (25/4)[1 + 2 + ... + 15] = (25/4) × 120 = 750 m³।",
        "પ્રથમ પગથિયાનું ઘનફળ = 25/4 m³. કુલ ઘનફળ = (25/4)[1 + 2 + ... + 15] = (25/4) × 120 = 750 m³."
    ))

    # =========================================================================
    # STEP 6: REFLECTION (Real-Life Socratic Synthesis)
    # =========================================================================
    blocks.append({
        "id": "C10M_CH5_STEP6_REFLECTION",
        "type": "reflection",
        "title": "Reflecting on Constant Rates of Change",
        "body": "Take a moment to pause and reflect on the profound nature of an Arithmetic Progression.\n\nWhenever a quantity changes by a **constant rate per unit time or step**, it is modeled by an AP:\n1. **Personal Finance:** Saving ₹500 every month is an AP. Your bank balance grows linearly.\n2. **Physics:** An object falling under constant gravity increases its speed by approximately 9.8 m/s every single second ($9.8, 19.6, 29.4...$).\n3. **Depreciation:** When a company depreciates equipment using the Straight-Line Method, its book value decreases by the same amount each year—forming a decreasing AP with negative common difference ($d < 0$).",
        "title_hi": "परिवर्तन की स्थिर दरों पर विचार",
        "body_hi": "समान्तर श्रेढ़ी की वास्तविक प्रकृति पर विचार करें।\n\nजब भी कोई मात्रा **प्रति इकाई समय या कदम में एक निश्चित दर से बदलती है**, तो उसे AP द्वारा दर्शाया जाता है:\n1. **व्यक्तिगत वित्त:** हर महीने ₹500 की बचत करना एक AP है। आपकी बचत रैखिक रूप से बढ़ती है।\n2. **भौतिकी:** गुरुत्वाकर्षण के अंतर्गत गिरने वाली वस्तु की गति प्रत्येक सेकंड लगभग 9.8 m/s बढ़ती है ($9.8, 19.6, 29.4...$)।\n3. **मूल्यह्रास (Depreciation):** जब कोई कंपनी सीधी रेखा विधि (Straight-Line Method) से किसी मशीन के मूल्य में समान वार्षिक कटौती करती है, तो यह ऋणात्मक सार्व अंतर ($d < 0$) वाली एक AP बनाती है।",
        "title_gu": "અચળ દરોના પરિવર્તન પર ચિંતન",
        "body_gu": "સમાંતર શ્રેણીના વાસ્તવિક મહત્વ પર વિચાર કરો.\n\nજ્યારે પણ કોઈ મૂલ્ય **સમય કે પગલા દીઠ સમાન દરે બદલાય છે**, ત્યારે તે AP દ્વારા રજૂ થાય છે:\n1. **વ્યક્તિગત બચત:** દર મહિને ₹500 બચાવવા એ AP છે. તમારી બચત સુરેખ રીતે વધે છે.\n2. **ભૌતિક વિજ્ઞાન:** ગુરુત્વાકર્ષણ હેઠળ મુક્ત પતન પામતા પદાર્થનો વેગ દર સેકન્ડે આશરે 9.8 m/s વધે છે ($9.8, 19.6, 29.4...$).\n3. **ઘસારો (Depreciation):** જ્યારે કંપની સીધી લીટીની પદ્ધતિથી દર વર્ષે સમાન રકમનો ઘસારો બાદ કરે છે, ત્યારે તે ઋણ સામાન્ય તફાવત ($d < 0$) વાળી ઘટતી AP બનાવે છે.",
        "bloom": "Analyze",
        "difficulty": "Intermediate",
        "estimated_minutes": 3
    })

    # =========================================================================
    # STEP 7: CONNECTION (Knowledge Graph & Higher Mathematics Links)
    # =========================================================================
    blocks.append({
        "id": "C10M_CH5_STEP7_CONNECTION",
        "type": "connection",
        "title": "Cross-Subject Connections & Higher Mathematics",
        "body": "**1. Connection to Coordinate Geometry & Linear Equations:**\nThe formula for the nth term $a_n = a + (n - 1)d = dn + (a - d)$ is identical to the equation of a straight line: $y = mx + c$. Here, the common difference $d$ plays the role of the **slope** ($m$)!\n\n**2. Connection to Quadratic Equations:**\nThe sum formula $S_n = \\frac{d}{2}n^2 + (a - \\frac{d}{2})n$ is a **Quadratic Equation** in terms of $n$. This is why finding the number of terms when sum is given often involves solving a quadratic equation (as we saw in Ex 5.3 Q4 and Q19)!\n\n**3. Path to Higher Mathematics (Class 11 & Calculus):**\nIn Class 11, you will expand from AP to Geometric Progressions (GP) and Arithmetic-Geometric Series (AGP). In Calculus, finding the sum of infinite terms is the foundation of Integrals!",
        "title_hi": "ज्ञान ग्राफ संबंध और उच्च गणित",
        "body_hi": "**1. निर्देशांक ज्यामिति और रैखिक समीकरणों से संबंध:**\nnवें पद का सूत्र $a_n = dn + (a - d)$, सीधी रेखा के समीकरण $y = mx + c$ के समान है। यहाँ सार्व अंतर $d$ **ढाल (slope)** की भूमिका निभाता है!\n\n**2. द्विघात समीकरणों से संबंध:**\nयोग का सूत्र $S_n = \\frac{d}{2}n^2 + (a - \\frac{d}{2})n$, $n$ के रूप में एक **द्विघात समीकरण** है। इसीलिए जब योग दिया हो और $n$ ज्ञात करना हो, तो हमें द्विघात समीकरण हल करना पड़ता है (जैसे Ex 5.3 Q4 और Q19 में)!\n\n**3. कक्षा 11 और कैलकुलस का मार्ग:**\nकक्षा 11 में आप गुणोत्तर श्रेढ़ी (GP) और हरात्मक श्रेढ़ी का अध्ययन करेंगे। कैलकुलस में अनंत पदों का योग समाकलन (Integrals) का आधार बनता है!",
        "title_gu": "નોલેજ ગ્રાફ અને ઉચ્ચ ગણિત સાથે જોડાણ",
        "body_gu": "**1. યામ ભૂમિતિ અને સુરેખ સમીકરણો સાથે જોડાણ:**\nnમા પદનું સૂત્ર $a_n = dn + (a - d)$ એ સીધી રેખાના સમીકરણ $y = mx + c$ જેવું જ છે. અહીં સામાન્ય તફાવત $d$ એ **ઢાળ (slope)** દર્શાવે છે!\n\n**2. દ્વિઘાત સમીકરણો સાથે જોડાણ:**\nસરવાળાનું સૂત્ર $S_n = \\frac{d}{2}n^2 + (a - \\frac{d}{2})n$ એ $n$ માં **દ્વિઘાત સમીકરણ** છે. આથી જ્યારે સરવાળો આપેલ હોય ત્યારે $n$ શોધવા માટે દ્વિઘાત સમીકરણ ઉકેલવું પડે છે (જેમ કે Ex 5.3 Q4 અને Q19 માં)!\n\n**3. ધોરણ 11 અને કલનશાસ્ત્ર (Calculus):**\nધોરણ 11 માં તમે સમગુણોત્તર શ્રેણી (GP) શીખશો. અનંત શ્રેણીઓનો સરવાળો કલનશાસ્ત્ર (Calculus) માં સંકલન (Integration) નો પાયો બને છે!",
        "bloom": "Evaluate",
        "difficulty": "Intermediate",
        "estimated_minutes": 3
    })

    # =========================================================================
    # STEP 8: MASTERY (Exam Checklist & Formula Summary)
    # =========================================================================
    blocks.append({
        "id": "C10M_CH5_STEP8_MASTERY",
        "type": "mastery",
        "title": "Mastery Summary: The 4 Golden Formulas of AP",
        "body": "Before your exams, review these 4 indispensable formulas:\n\n1. **Common Difference:**\n   $$d = a_{k+1} - a_k$$\n\n2. **nth Term (General Term):**\n   $$a_n = a + (n - 1)d$$\n\n3. **Sum of First n Terms:**\n   $$S_n = \\frac{n}{2}[2a + (n - 1)d] = \\frac{n}{2}[a + l]$$\n\n4. **nth Term from Sum:**\n   $$a_n = S_n - S_{n-1}$$\n\n**Golden Rule for Word Problems:** Always clearly define your first term $a$, the common difference $d$, and verify that the number of terms $n$ is a positive integer!",
        "title_hi": "दक्षता सारांश: AP के 4 स्वर्णिम सूत्र",
        "body_hi": "परीक्षा से पहले इन 4 अपरिहार्य सूत्रों को अवश्य दोहराएँ:\n\n1. **सार्व अंतर:**\n   $$d = a_{k+1} - a_k$$\n\n2. **nवाँ पद (व्यापक पद):**\n   $$a_n = a + (n - 1)d$$\n\n3. **प्रथम n पदों का योग:**\n   $$S_n = \\frac{n}{2}[2a + (n - 1)d] = \\frac{n}{2}[a + l]$$\n\n4. **योग द्वारा nवाँ पद:**\n   $$a_n = S_n - S_{n-1}$$\n\n**शाब्दिक प्रश्नों का स्वर्ण नियम:** हमेशा अपने प्रथम पद $a$ और सार्व अंतर $d$ को स्पष्ट रूप से पहचानें, और सुनिश्चित करें कि पदों की संख्या $n$ एक धनात्मक पूर्णांक है!",
        "title_gu": "પ્રભુત્વ સારાંશ: AP ના 4 સુવર્ણ સૂત્રો",
        "body_gu": "પરીક્ષા પહેલાં આ 4 અનિવાર્ય સૂત્રોનું પુનરાવર્તન કરો:\n\n1. **સામાન્ય તફાવત:**\n   $$d = a_{k+1} - a_k$$\n\n2. **nમું પદ (વ્યાપક પદ):**\n   $$a_n = a + (n - 1)d$$\n\n3. **પ્રથમ n પદોનો સરવાળો:**\n   $$S_n = \\frac{n}{2}[2a + (n - 1)d] = \\frac{n}{2}[a + l]$$\n\n4. **સરવાળા પરથી nમું પદ:**\n   $$a_n = S_n - S_{n-1}$$\n\n**કૂટપ્રશ્નો માટેનો સુવર્ણ નિયમ:** હંમેશા પ્રથમ પદ $a$ અને સામાન્ય તફાવત $d$ સ્પષ્ટ રીતે તારવો, અને ખાતરી કરો કે પદોની સંખ્યા $n$ હંમેશા ધન પૂર્ણાંક જ હોય!",
        "bloom": "Create",
        "difficulty": "Beginner",
        "estimated_minutes": 2
    })

    return blocks

def generate_blocks():
    return get_part1_blocks() + get_part2_blocks() + get_part3_blocks() + get_part4_blocks()

def get_metadata():
    return {
        "id": "ncert_class10_maths_ch5",
        "title": "Chapter 5: Arithmetic Progressions",
        "title_hi": "अध्याय 5: समान्तर श्रेढ़ियाँ",
        "title_gu": "પ્રકરણ 5: સમાંતર શ્રેણીઓ",
        "subject": "Mathematics",
        "grade": "10",
        "board": "CBSE/GSEB",
        "curriculum": ["CBSE", "NCERT", "GSEB"],
        "language": "English, Hindi, Gujarati",
        "difficulty": "Intermediate",
        "estimated_minutes": 240,
        "version": "1.0.0",
        "author": "Shine Academy EduOS",
        "last_updated": "2026-09-30",
        "tags": ["arithmetic_progression", "ap", "nth_term", "sum_of_n_terms", "series_and_sequences"]
    }

def generate_chapter():
    chapter_data = {
        "metadata": get_metadata(),
        "blocks": generate_blocks()
    }
    
    output_dir = 'app_core/chapters'
    os.makedirs(output_dir, exist_ok=True)
    target_path = os.path.join(output_dir, 'ncert_class10_maths_ch5.json')
    
    with open(target_path, 'w', encoding='utf-8') as f:
        json.dump(chapter_data, f, indent=2, ensure_ascii=False)
        
    print(f"Generated {target_path} successfully with {len(chapter_data['blocks'])} blocks!")

if __name__ == "__main__":
    generate_chapter()



