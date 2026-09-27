import json

metadata = {
    "title": "Real Numbers",
    "subject": "Maths",
    "grade": "10",
    "board": "CBSE",
    "curriculum": ["CBSE", "NCERT"],
    "difficulty": "Intermediate",
    "version": "5.0.0",
    "id": "cbse_class10_maths_ch1",
    "tags": ["Maths", "Real Numbers", "CBSE", "Class 10"],
    "ai_context": {
        "learning_goal": "Master Euclid's Division Lemma, Fundamental Theorem of Arithmetic, and proofs of irrationality.",
        "common_misconceptions": ["Thinking HCF x LCM = Product works for 3 numbers.", "Confusing rational approximations with true irrational numbers."],
        "tutor_hint": "If a student struggles with irrationality proofs, remind them of 'Proof by Contradiction'.",
        "next_topics": ["KOBJ_CLASS10_MATH_CH2_POLYNOMIALS"]
    }
}

blocks = [
    # Topic 1: Euclid's Division Lemma
    {
        "id": "KOBJ_CLASS10_MATH_CH1_01",
        "type": "theory",
        "title": "A Puzzle from the Past (The Hook)",
        "title_hi": "अतीत से एक पहेली (हूक)",
        "title_gu": "ભૂતકાળમાંથી એક કોયડો (હૂક)",
        "body": "Imagine you have a basket of eggs. If you count them in twos, 1 is left. If you count in threes, 2 are left. If you count in fours, 3 are left... up to counting in sevens where 0 are left. How many eggs are there? This is an ancient puzzle. How do we even begin to solve it?",
        "body_hi": "कल्पना करें कि आपके पास अंडों की एक टोकरी है। यदि आप उन्हें दो-दो करके गिनते हैं, तो 1 बचता है। यदि आप तीन-तीन करके गिनते हैं, तो 2 बचते हैं। यदि आप चार-चार करके गिनते हैं, तो 3 बचते हैं... और यदि सात-सात करके गिनते हैं तो 0 बचते हैं। कुल कितने अंडे हैं? यह एक प्राचीन पहेली है। हम इसे हल करना कैसे शुरू करें?",
        "body_gu": "કલ્પના કરો કે તમારી પાસે ઈંડાની ટોપલી છે. જો તમે તેમને બબ્બે ગણો છો, તો 1 વધે છે. જો તમે ત્રણ-ત્રણ ગણો છો, તો 2 વધે છે. જો તમે ચાર-ચાર ગણો છો, તો 3 વધે છે... અને જો તમે સાત-સાત ગણો છો તો 0 વધે છે. કુલ કેટલા ઈંડા છે? આ એક પ્રાચીન કોયડો છે. આપણે આને ઉકેલવાનું કેવી રીતે શરૂ કરીશું?"
    },
    {
        "id": "KOBJ_CLASS10_MATH_CH1_02",
        "type": "theory",
        "title": "Think About Division (Socratic Question)",
        "title_hi": "विभाजन के बारे में सोचें (सुकराती प्रश्न)",
        "title_gu": "ભાગાકાર વિશે વિચારો (સોક્રેટિક પ્રશ્ન)",
        "body": "When you divide 17 by 3, what happens? You get a quotient of 5 and a remainder of 2. Can you write this relationship in a single line? What if you try to find a remainder that is bigger than 3? Is that possible?",
        "body_hi": "जब आप 17 को 3 से भाग देते हैं, तो क्या होता है? आपको भागफल 5 और शेषफल 2 मिलता है। क्या आप इस संबंध को एक पंक्ति में लिख सकते हैं? क्या होगा यदि आप ऐसा शेषफल खोजने की कोशिश करें जो 3 से बड़ा हो? क्या यह संभव है?",
        "body_gu": "જ્યારે તમે 17 ને 3 વડે ભાગો છો, ત્યારે શું થાય છે? તમને ભાગફળ 5 અને શેષ 2 મળે છે. શું તમે આ સંબંધને એક લીટીમાં લખી શકો છો? જો તમે 3 કરતાં મોટી શેષ શોધવાનો પ્રયાસ કરો તો શું થશે? શું તે શક્ય છે?"
    },
    {
        "id": "KOBJ_CLASS10_MATH_CH1_03",
        "type": "theory",
        "title": "Euclid's Division Lemma (The Reveal)",
        "title_hi": "यूक्लिड विभाजन प्रमेयिका (प्रकटीकरण)",
        "title_gu": "યુક્લિડની ભાગાકારની પૂર્વપ્રમેય (પ્રકટીકરણ)",
        "body": "Euclid's Division Lemma states: Given positive integers a and b, there exist unique integers q and r satisfying a = bq + r, where 0 ≤ r < b. Here, 'a' is the dividend, 'b' is the divisor, 'q' is the quotient, and 'r' is the remainder.",
        "body_hi": "यूक्लिड विभाजन प्रमेयिका कहती है: दिए गए धनात्मक पूर्णांकों a और b के लिए, ऐसी अद्वितीय पूर्ण संख्याएँ q और r विद्यमान हैं कि a = bq + r, जहाँ 0 ≤ r < b है। यहाँ 'a' भाज्य है, 'b' भाजक है, 'q' भागफल है, और 'r' शेषफल है।",
        "body_gu": "યુક્લિડની ભાગાકારની પૂર્વપ્રમેય જણાવે છે: આપેલા ધન પૂર્ણાંકો a અને b માટે, અનન્ય પૂર્ણાંકો q અને r અસ્તિત્વમાં છે જે a = bq + r ને સંતોષે છે, જ્યાં 0 ≤ r < b. અહીં, 'a' ભાજ્ય છે, 'b' ભાજક છે, 'q' ભાગફળ છે અને 'r' શેષ છે."
    },
    {
        "id": "KOBJ_CLASS10_MATH_CH1_04",
        "type": "mcq",
        "question": "According to Euclid's Division Lemma (a = bq + r), which of the following conditions is strictly true for the remainder 'r'?",
        "question_hi": "यूक्लिड विभाजन प्रमेयिका (a = bq + r) के अनुसार, शेषफल 'r' के लिए निम्नलिखित में से कौन सी शर्त सत्य है?",
        "question_gu": "યુક્લિડની ભાગાકારની પૂર્વપ્રમેય (a = bq + r) મુજબ, શેષ 'r' માટે નીચેનામાંથી કઈ શરત સત્ય છે?",
        "options": [
            "0 < r ≤ b",
            "0 ≤ r < b",
            "0 ≤ r ≤ b",
            "r < 0"
        ],
        "options_hi": [
            "0 < r ≤ b",
            "0 ≤ r < b",
            "0 ≤ r ≤ b",
            "r < 0"
        ],
        "options_gu": [
            "0 < r ≤ b",
            "0 ≤ r < b",
            "0 ≤ r ≤ b",
            "r < 0"
        ],
        "correct_index": 1,
        "explanation": "The remainder must be at least 0 but strictly less than the divisor 'b'.",
        "explanation_hi": "शेषफल कम से कम 0 होना चाहिए लेकिन भाजक 'b' से सख्ती से कम होना चाहिए।",
        "explanation_gu": "શેષ ઓછામાં ઓછી 0 હોવી જોઈએ પરંતુ ભાજક 'b' કરતા કડક રીતે ઓછી હોવી જોઈએ."
    },
    
    # Topic 2: Fundamental Theorem of Arithmetic
    {
        "id": "KOBJ_CLASS10_MATH_CH1_05",
        "type": "theory",
        "title": "The Prime Building Blocks (Hook)",
        "title_hi": "अभाज्य निर्माण खंड (हूक)",
        "title_gu": "અવિભાજ્ય નિર્માણ ખંડો (હૂક)",
        "body": "Imagine you are building a giant wall. Instead of using bricks of the same size, you have a magical set of 'prime' bricks that can never be broken down further. Did you know every number can be built using only these prime bricks?",
        "body_hi": "कल्पना करें कि आप एक विशाल दीवार बना रहे हैं। समान आकार की ईंटों का उपयोग करने के बजाय, आपके पास 'अभाज्य' ईंटों का एक जादुई सेट है जिसे कभी भी आगे नहीं तोड़ा जा सकता है। क्या आप जानते हैं कि हर संख्या केवल इन्हीं अभाज्य ईंटों का उपयोग करके बनाई जा सकती है?",
        "body_gu": "કલ્પના કરો કે તમે એક વિશાળ દિવાલ બનાવી રહ્યા છો. સમાન કદની ઇંટોનો ઉપયોગ કરવાને બદલે, તમારી પાસે 'અવિભાજ્ય' ઇંટોનો એક જાદુઈ સમૂહ છે જેને ક્યારેય આગળ તોડી શકાતો નથી. શું તમે જાણો છો કે દરેક સંખ્યા માત્ર આ અવિભાજ્ય ઇંટોનો ઉપયોગ કરીને બનાવી શકાય છે?"
    },
    {
        "id": "KOBJ_CLASS10_MATH_CH1_06",
        "type": "theory",
        "title": "Fundamental Theorem of Arithmetic (Reveal)",
        "title_hi": "अंकगणित का आधारभूत प्रमेय (प्रकटीकरण)",
        "title_gu": "અંકગણિતનું મૂળભૂત પ્રમેય (પ્રકટીકરણ)",
        "body": "Every composite number can be expressed (factorised) as a product of primes, and this factorisation is unique, apart from the order in which the prime factors occur.",
        "body_hi": "प्रत्येक भाज्य संख्या को अभाज्य संख्याओं के एक गुणनफल के रूप में व्यक्त (गुणनखंडित) किया जा सकता है, और यह गुणनखंडन अद्वितीय होता है, इस पर ध्यान दिए बिना कि अभाज्य गुणनखंड किस क्रम में आते हैं।",
        "body_gu": "દરેક વિભાજ્ય સંખ્યાને અવિભાજ્ય સંખ્યાઓના ગુણાકાર તરીકે વ્યક્ત કરી શકાય છે, અને આ અવયવીકરણ અનન્ય છે, અવિભાજ્ય અવયવો જે ક્રમમાં આવે છે તેને બાદ કરતા."
    },
    {
        "id": "KOBJ_CLASS10_MATH_CH1_07",
        "type": "worked_example",
        "title": "Exercise 1.1 Q1: Prime Factorisation",
        "title_hi": "प्रश्नावली 1.1 Q1: अभाज्य गुणनखंडन",
        "title_gu": "સ્વાધ્યાય 1.1 Q1: અવિભાજ્ય અવયવીકરણ",
        "question": "Express each number as a product of its prime factors: (i) 140 (ii) 156 (iii) 3825 (iv) 5005 (v) 7429",
        "question_hi": "निम्नलिखित संख्याओं को अभाज्य गुणनखंडों के गुणनफल के रूप में व्यक्त कीजिए: (i) 140 (ii) 156 (iii) 3825 (iv) 5005 (v) 7429",
        "question_gu": "નીચેની સંખ્યાઓને અવિભાજ્ય અવયવોના ગુણાકાર તરીકે દર્શાવો: (i) 140 (ii) 156 (iii) 3825 (iv) 5005 (v) 7429",
        "solution": "(i) 140 = 2 × 2 × 5 × 7 = 2² × 5 × 7\n(ii) 156 = 2 × 2 × 3 × 13 = 2² × 3 × 13\n(iii) 3825 = 3 × 3 × 5 × 5 × 17 = 3² × 5² × 17\n(iv) 5005 = 5 × 7 × 11 × 13\n(v) 7429 = 17 × 19 × 23",
        "solution_hi": "(i) 140 = 2 × 2 × 5 × 7 = 2² × 5 × 7\n(ii) 156 = 2 × 2 × 3 × 13 = 2² × 3 × 13\n(iii) 3825 = 3 × 3 × 5 × 5 × 17 = 3² × 5² × 17\n(iv) 5005 = 5 × 7 × 11 × 13\n(v) 7429 = 17 × 19 × 23",
        "solution_gu": "(i) 140 = 2 × 2 × 5 × 7 = 2² × 5 × 7\n(ii) 156 = 2 × 2 × 3 × 13 = 2² × 3 × 13\n(iii) 3825 = 3 × 3 × 5 × 5 × 17 = 3² × 5² × 17\n(iv) 5005 = 5 × 7 × 11 × 13\n(v) 7429 = 17 × 19 × 23"
    },
    {
        "id": "KOBJ_CLASS10_MATH_CH1_08",
        "type": "worked_example",
        "title": "Exercise 1.1 Q5: Number ending with zero",
        "title_hi": "प्रश्नावली 1.1 Q5: शून्य पर समाप्त होने वाली संख्या",
        "title_gu": "સ્વાધ્યાય 1.1 Q5: શૂન્ય પર સમાપ્ત થતી સંખ્યા",
        "question": "Check whether 6^n can end with the digit 0 for any natural number n.",
        "question_hi": "जाँच कीजिए कि क्या किसी प्राकृत संख्या n के लिए 6^n अंक 0 पर समाप्त हो सकता है।",
        "question_gu": "ચકાસો કે શું કોઈ પ્રાકૃતિક સંખ્યા n માટે 6^n અંક 0 પર સમાપ્ત થઈ શકે છે.",
        "solution": "If any number ends with the digit 0, it should be divisible by 10 or in other words, it will also be divisible by 2 and 5 as 10 = 2 × 5.\nPrime factorisation of 6^n = (2 × 3)^n = 2^n × 3^n.\nIt can be observed that 5 is not in the prime factorisation of 6^n.\nHence, for any value of n, 6^n will not be divisible by 5.\nTherefore, 6^n cannot end with the digit 0 for any natural number n.",
        "solution_hi": "यदि कोई संख्या अंक 0 पर समाप्त होती है, तो उसे 10 से विभाज्य होना चाहिए या दूसरे शब्दों में, यह 2 और 5 से भी विभाज्य होगी क्योंकि 10 = 2 × 5।\n6^n का अभाज्य गुणनखंडन = (2 × 3)^n = 2^n × 3^n।\nयह देखा जा सकता है कि 6^n के अभाज्य गुणनखंडन में 5 नहीं है।\nअतः, n के किसी भी मान के लिए, 6^n, 5 से विभाज्य नहीं होगा।\nइसलिए, किसी भी प्राकृत संख्या n के लिए 6^n अंक 0 पर समाप्त नहीं हो सकता।",
        "solution_gu": "જો કોઈ સંખ્યા અંક 0 પર સમાપ્ત થાય છે, તો તે 10 વડે વિભાજ્ય હોવી જોઈએ અથવા બીજા શબ્દોમાં કહીએ તો, તે 2 અને 5 વડે પણ વિભાજ્ય હશે કારણ કે 10 = 2 × 5.\n6^n નું અવિભાજ્ય અવયવીકરણ = (2 × 3)^n = 2^n × 3^n.\nએવું જોઈ શકાય છે કે 6^n ના અવિભાજ્ય અવયવીકરણમાં 5 નથી.\nઆથી, n ના કોઈપણ મૂલ્ય માટે, 6^n એ 5 વડે વિભાજ્ય રહેશે નહીં.\nતેથી, કોઈપણ પ્રાકૃતિક સંખ્યા n માટે 6^n અંક 0 પર સમાપ્ત થઈ શકશે નહીં."
    },
    {
        "id": "KOBJ_CLASS10_MATH_CH1_09",
        "type": "worked_example",
        "title": "Exercise 1.1 Q6: Composite Numbers",
        "title_hi": "प्रश्नावली 1.1 Q6: भाज्य संख्याएँ",
        "title_gu": "સ્વાધ્યાય 1.1 Q6: વિભાજ્ય સંખ્યાઓ",
        "question": "Explain why 7 × 11 × 13 + 13 and 7 × 6 × 5 × 4 × 3 × 2 × 1 + 5 are composite numbers.",
        "question_hi": "व्याख्या कीजिए कि 7 × 11 × 13 + 13 और 7 × 6 × 5 × 4 × 3 × 2 × 1 + 5 भाज्य संख्याएँ क्यों हैं।",
        "question_gu": "સમજાવો કે 7 × 11 × 13 + 13 અને 7 × 6 × 5 × 4 × 3 × 2 × 1 + 5 વિભાજ્ય સંખ્યાઓ શા માટે છે.",
        "solution": "Numbers are of two types: prime and composite. Prime numbers have only two factors, 1 and the number itself. Composite numbers have more than two factors.\nFirst number: 7 × 11 × 13 + 13 = 13 × (7 × 11 + 1) = 13 × (77 + 1) = 13 × 78 = 13 × 13 × 6.\nThe given expression has 6 and 13 as its factors. Therefore, it is a composite number.\nSecond number: 7 × 6 × 5 × 4 × 3 × 2 × 1 + 5 = 5 × (7 × 6 × 4 × 3 × 2 × 1 + 1) = 5 × (1008 + 1) = 5 × 1009.\n1009 cannot be factorised further. Therefore, the given expression has 5 and 1009 as its factors. Hence, it is a composite number.",
        "solution_hi": "संख्याएँ दो प्रकार की होती हैं: अभाज्य और भाज्य। अभाज्य संख्याओं के केवल दो गुणनखंड होते हैं, 1 और वह संख्या स्वयं। भाज्य संख्याओं के दो से अधिक गुणनखंड होते हैं।\nपहली संख्या: 7 × 11 × 13 + 13 = 13 × (7 × 11 + 1) = 13 × (77 + 1) = 13 × 78 = 13 × 13 × 6.\nदिए गए व्यंजक के गुणनखंड 6 और 13 हैं। इसलिए, यह एक भाज्य संख्या है।\nदूसरी संख्या: 7 × 6 × 5 × 4 × 3 × 2 × 1 + 5 = 5 × (7 × 6 × 4 × 3 × 2 × 1 + 1) = 5 × (1008 + 1) = 5 × 1009.\n1009 को आगे गुणनखंडित नहीं किया जा सकता है। इसलिए, दिए गए व्यंजक के गुणनखंड 5 और 1009 हैं। अतः, यह एक भाज्य संख्या है।",
        "solution_gu": "સંખ્યાઓ બે પ્રકારની હોય છે: અવિભાજ્ય અને વિભાજ્ય. અવિભાજ્ય સંખ્યાઓમાં માત્ર બે જ અવયવો હોય છે, 1 અને સંખ્યા પોતે. વિભાજ્ય સંખ્યાઓમાં બે કરતાં વધુ અવયવો હોય છે.\nપ્રથમ સંખ્યા: 7 × 11 × 13 + 13 = 13 × (7 × 11 + 1) = 13 × (77 + 1) = 13 × 78 = 13 × 13 × 6.\nઆપેલ પદાવલિમાં 6 અને 13 તેના અવયવો તરીકે છે. તેથી, તે વિભાજ્ય સંખ્યા છે.\nબીજી સંખ્યા: 7 × 6 × 5 × 4 × 3 × 2 × 1 + 5 = 5 × (7 × 6 × 4 × 3 × 2 × 1 + 1) = 5 × (1008 + 1) = 5 × 1009.\n1009 ના વધુ અવયવો પાડી શકાતા નથી. તેથી, આપેલ પદાવલિમાં 5 અને 1009 તેના અવયવો તરીકે છે. આથી, તે વિભાજ્ય સંખ્યા છે."
    },
    
    # Topic 3: HCF & LCM Applications
    {
        "id": "KOBJ_CLASS10_MATH_CH1_10",
        "type": "theory",
        "title": "HCF and LCM Link (Connection)",
        "title_hi": "HCF और LCM संबंध (कनेक्शन)",
        "title_gu": "HCF અને LCM સંબંધ (કનેક્શન)",
        "body": "For any two positive integers a and b, HCF(a, b) × LCM(a, b) = a × b. This is a very powerful formula, but remember, it ONLY works for exactly TWO numbers, not three!",
        "body_hi": "किन्हीं दो धनात्मक पूर्णांकों a और b के लिए, HCF(a, b) × LCM(a, b) = a × b. यह एक बहुत ही शक्तिशाली सूत्र है, लेकिन याद रखें, यह केवल दो संख्याओं के लिए काम करता है, तीन के लिए नहीं!",
        "body_gu": "કોઈપણ બે ધન પૂર્ણાંકો a અને b માટે, HCF(a, b) × LCM(a, b) = a × b. આ એક ખૂબ જ શક્તિશાળી સૂત્ર છે, પરંતુ યાદ રાખો, તે ફક્ત બે સંખ્યાઓ માટે જ કામ કરે છે, ત્રણ માટે નહીં!"
    },
    {
        "id": "KOBJ_CLASS10_MATH_CH1_11",
        "type": "worked_example",
        "title": "Exercise 1.1 Q2: LCM, HCF and Verification",
        "title_hi": "प्रश्नावली 1.1 Q2: LCM, HCF और सत्यापन",
        "title_gu": "સ્વાધ્યાય 1.1 Q2: LCM, HCF અને ચકાસણી",
        "question": "Find the LCM and HCF of the following pairs of integers and verify that LCM × HCF = product of the two numbers.\n(i) 26 and 91 (ii) 510 and 92 (iii) 336 and 54",
        "question_hi": "पूर्णांकों के निम्नलिखित युग्मों के LCM और HCF ज्ञात कीजिए तथा इसकी जाँच कीजिए कि LCM × HCF = दो संख्याओं का गुणनफल है।\n(i) 26 और 91 (ii) 510 और 92 (iii) 336 और 54",
        "question_gu": "નીચે આપેલા પૂર્ણાંકોની જોડીના LCM અને HCF શોધો અને ચકાસો કે LCM × HCF = બે સંખ્યાઓનો ગુણાકાર.\n(i) 26 અને 91 (ii) 510 અને 92 (iii) 336 અને 54",
        "solution": "(i) 26 = 2 × 13; 91 = 7 × 13. HCF = 13, LCM = 2 × 7 × 13 = 182.\nVerification: LCM × HCF = 182 × 13 = 2366. Product = 26 × 91 = 2366. Hence verified.\n\n(ii) 510 = 2 × 3 × 5 × 17; 92 = 2 × 2 × 23. HCF = 2, LCM = 2² × 3 × 5 × 17 × 23 = 23460.\nVerification: LCM × HCF = 23460 × 2 = 46920. Product = 510 × 92 = 46920. Hence verified.\n\n(iii) 336 = 2⁴ × 3 × 7; 54 = 2 × 3³. HCF = 2 × 3 = 6. LCM = 2⁴ × 3³ × 7 = 3024.\nVerification: LCM × HCF = 3024 × 6 = 18144. Product = 336 × 54 = 18144. Hence verified.",
        "solution_hi": "(i) 26 = 2 × 13; 91 = 7 × 13. HCF = 13, LCM = 2 × 7 × 13 = 182.\nसत्यापन: LCM × HCF = 182 × 13 = 2366. गुणनफल = 26 × 91 = 2366. अतः सत्यापित।\n\n(ii) 510 = 2 × 3 × 5 × 17; 92 = 2 × 2 × 23. HCF = 2, LCM = 2² × 3 × 5 × 17 × 23 = 23460.\nसत्यापन: LCM × HCF = 23460 × 2 = 46920. गुणनफल = 510 × 92 = 46920. अतः सत्यापित।\n\n(iii) 336 = 2⁴ × 3 × 7; 54 = 2 × 3³. HCF = 2 × 3 = 6. LCM = 2⁴ × 3³ × 7 = 3024.\nसत्यापन: LCM × HCF = 3024 × 6 = 18144. गुणनफल = 336 × 54 = 18144. अतः सत्यापित।",
        "solution_gu": "(i) 26 = 2 × 13; 91 = 7 × 13. HCF = 13, LCM = 2 × 7 × 13 = 182.\nચકાસણી: LCM × HCF = 182 × 13 = 2366. ગુણાકાર = 26 × 91 = 2366. આમ સાબિત થયું.\n\n(ii) 510 = 2 × 3 × 5 × 17; 92 = 2 × 2 × 23. HCF = 2, LCM = 2² × 3 × 5 × 17 × 23 = 23460.\nચકાસણી: LCM × HCF = 23460 × 2 = 46920. ગુણાકાર = 510 × 92 = 46920. આમ સાબિત થયું.\n\n(iii) 336 = 2⁴ × 3 × 7; 54 = 2 × 3³. HCF = 2 × 3 = 6. LCM = 2⁴ × 3³ × 7 = 3024.\nચકાસણી: LCM × HCF = 3024 × 6 = 18144. ગુણાકાર = 336 × 54 = 18144. આમ સાબિત થયું."
    },
    {
        "id": "KOBJ_CLASS10_MATH_CH1_12",
        "type": "worked_example",
        "title": "Exercise 1.1 Q3: LCM and HCF of 3 numbers",
        "title_hi": "प्रश्नावली 1.1 Q3: 3 संख्याओं का LCM और HCF",
        "title_gu": "સ્વાધ્યાય 1.1 Q3: 3 સંખ્યાઓનો LCM અને HCF",
        "question": "Find the LCM and HCF of the following integers by applying the prime factorisation method.\n(i) 12, 15 and 21\n(ii) 17, 23 and 29\n(iii) 8, 9 and 25",
        "question_hi": "अभाज्य गुणनखंडन विधि द्वारा निम्नलिखित पूर्णांकों के LCM और HCF ज्ञात कीजिए।\n(i) 12, 15 और 21\n(ii) 17, 23 और 29\n(iii) 8, 9 और 25",
        "question_gu": "અવિભાજ્ય અવયવીકરણ પદ્ધતિ લાગુ કરીને નીચેના પૂર્ણાંકોના LCM અને HCF શોધો.\n(i) 12, 15 અને 21\n(ii) 17, 23 અને 29\n(iii) 8, 9 અને 25",
        "solution": "(i) 12 = 2² × 3; 15 = 3 × 5; 21 = 3 × 7. HCF = 3. LCM = 2² × 3 × 5 × 7 = 420.\n(ii) 17 = 17 × 1; 23 = 23 × 1; 29 = 29 × 1. These are all prime. HCF = 1. LCM = 17 × 23 × 29 = 11339.\n(iii) 8 = 2³; 9 = 3²; 25 = 5². No common prime factor. HCF = 1. LCM = 2³ × 3² × 5² = 8 × 9 × 25 = 1800.",
        "solution_hi": "(i) 12 = 2² × 3; 15 = 3 × 5; 21 = 3 × 7. HCF = 3. LCM = 2² × 3 × 5 × 7 = 420.\n(ii) 17 = 17 × 1; 23 = 23 × 1; 29 = 29 × 1. ये सभी अभाज्य हैं। HCF = 1. LCM = 17 × 23 × 29 = 11339.\n(iii) 8 = 2³; 9 = 3²; 25 = 5². कोई उभयनिष्ठ अभाज्य गुणनखंड नहीं। HCF = 1. LCM = 2³ × 3² × 5² = 8 × 9 × 25 = 1800.",
        "solution_gu": "(i) 12 = 2² × 3; 15 = 3 × 5; 21 = 3 × 7. HCF = 3. LCM = 2² × 3 × 5 × 7 = 420.\n(ii) 17 = 17 × 1; 23 = 23 × 1; 29 = 29 × 1. આ તમામ અવિભાજ્ય છે. HCF = 1. LCM = 17 × 23 × 29 = 11339.\n(iii) 8 = 2³; 9 = 3²; 25 = 5². કોઈ સામાન્ય અવિભાજ્ય અવયવ નથી. HCF = 1. LCM = 2³ × 3² × 5² = 8 × 9 × 25 = 1800."
    },
    {
        "id": "KOBJ_CLASS10_MATH_CH1_13",
        "type": "worked_example",
        "title": "Exercise 1.1 Q4: Finding LCM using HCF",
        "title_hi": "प्रश्नावली 1.1 Q4: HCF का उपयोग करके LCM ज्ञात करना",
        "title_gu": "સ્વાધ્યાય 1.1 Q4: HCF નો ઉપયોગ કરીને LCM શોધવો",
        "question": "Given that HCF (306, 657) = 9, find LCM (306, 657).",
        "question_hi": "दिया गया है HCF (306, 657) = 9, LCM (306, 657) ज्ञात कीजिए।",
        "question_gu": "આપેલ છે કે HCF (306, 657) = 9, તો LCM (306, 657) શોધો.",
        "solution": "We know that HCF(a, b) × LCM(a, b) = a × b.\nHere, a = 306, b = 657, HCF = 9.\n9 × LCM = 306 × 657\nLCM = (306 × 657) / 9\nLCM = 34 × 657 = 22338.",
        "solution_hi": "हम जानते हैं कि HCF(a, b) × LCM(a, b) = a × b.\nयहाँ, a = 306, b = 657, HCF = 9.\n9 × LCM = 306 × 657\nLCM = (306 × 657) / 9\nLCM = 34 × 657 = 22338.",
        "solution_gu": "આપણે જાણીએ છીએ કે HCF(a, b) × LCM(a, b) = a × b.\nઅહીં, a = 306, b = 657, HCF = 9.\n9 × LCM = 306 × 657\nLCM = (306 × 657) / 9\nLCM = 34 × 657 = 22338."
    },
    {
        "id": "KOBJ_CLASS10_MATH_CH1_14",
        "type": "worked_example",
        "title": "Exercise 1.1 Q7: Circular Path Problem",
        "title_hi": "प्रश्नावली 1.1 Q7: वृत्ताकार पथ की समस्या",
        "title_gu": "સ્વાધ્યાય 1.1 Q7: વર્તુળાકાર માર્ગની સમસ્યા",
        "question": "There is a circular path around a sports field. Dwija takes 18 minutes to drive one round of the field, while Vedant takes 12 minutes for the same. Suppose they both start at the same point and at the same time, and go in the same direction. After how many minutes will they meet again at the starting point?",
        "question_hi": "किसी खेल के मैदान के चारो ओर एक वृत्ताकार पथ है। द्विजा को मैदान का एक चक्कर लगाने में 18 मिनट लगते हैं, जबकि वेदांत को 12 मिनट लगते हैं। मान लीजिए वे दोनों एक ही बिंदु से एक ही समय पर चलना प्रारंभ करते हैं और एक ही दिशा में जाते हैं। कितने मिनट बाद वे पुनः प्रारंभिक स्थान पर मिलेंगे?",
        "question_gu": "રમતગમતના મેદાનની આસપાસ એક વર્તુળાકાર માર્ગ છે. દ્વિજાને મેદાનનો એક રાઉન્ડ ચલાવવામાં 18 મિનિટનો સમય લાગે છે, જ્યારે વેદાંતને તેના માટે 12 મિનિટ લાગે છે. ધારો કે તેઓ બંને એક જ બિંદુથી અને એક જ સમયે શરૂ કરે છે, અને સમાન દિશામાં જાય છે. કેટલી મિનિટ પછી તેઓ ફરીથી પ્રારંભિક બિંદુ પર મળશે?",
        "solution": "They will meet again at the starting point when they have completed a whole number of rounds. The time taken will be a multiple of both 18 and 12.\nTo find the minimum time they will meet again, we need to find the LCM of 18 and 12.\nPrime factorisation:\n18 = 2 × 3²\n12 = 2² × 3\nLCM(18, 12) = 2² × 3² = 4 × 9 = 36.\nTherefore, Dwija and Vedant will meet again at the starting point after 36 minutes.",
        "solution_hi": "वे प्रारंभिक बिंदु पर फिर से मिलेंगे जब उन्होंने पूरे चक्कर पूरे कर लिए होंगे। लिया गया समय 18 और 12 दोनों का गुणज होगा।\nन्यूनतम समय ज्ञात करने के लिए जब वे फिर से मिलेंगे, हमें 18 और 12 का LCM ज्ञात करना होगा।\nअभाज्य गुणनखंडन:\n18 = 2 × 3²\n12 = 2² × 3\nLCM(18, 12) = 2² × 3² = 4 × 9 = 36.\nइसलिए, द्विजा और वेदांत 36 मिनट बाद फिर से प्रारंभिक स्थान पर मिलेंगे।",
        "solution_gu": "જ્યારે તેઓએ આખો રાઉન્ડ પૂર્ણ કર્યો હશે ત્યારે તેઓ પ્રારંભિક બિંદુ પર ફરીથી મળશે. લીધેલો સમય 18 અને 12 બંનેનો ગુણાંક હશે.\nતેઓ ફરી ક્યારે મળશે તે ન્યૂનતમ સમય શોધવા માટે, આપણે 18 અને 12 નો LCM શોધવાની જરૂર છે.\nઅવિભાજ્ય અવયવીકરણ:\n18 = 2 × 3²\n12 = 2² × 3\nLCM(18, 12) = 2² × 3² = 4 × 9 = 36.\nતેથી, દ્વિજા અને વેદાંત 36 મિનિટ પછી પ્રારંભિક બિંદુ પર ફરીથી મળશે."
    },
    
    # Topic 4: Revisiting Irrational Numbers
    {
        "id": "KOBJ_CLASS10_MATH_CH1_15",
        "type": "theory",
        "title": "The Numbers that Never End (Hook)",
        "title_hi": "संख्याएँ जो कभी समाप्त नहीं होतीं (हूक)",
        "title_gu": "સંખ્યાઓ જે ક્યારેય સમાપ્ત થતી નથી (હૂક)",
        "body": "We have seen that rational numbers either terminate or repeat. But what about numbers that neither terminate nor repeat, like Pi (π) or √2? These are called Irrational Numbers. Understanding this boundary helps us map the entire universe of Real Numbers!",
        "body_hi": "हमने देखा है कि परिमेय संख्याएँ या तो समाप्त हो जाती हैं या दोहराई जाती हैं। लेकिन उन संख्याओं के बारे में क्या जो न तो समाप्त होती हैं और न ही दोहराई जाती हैं, जैसे Pi (π) या √2? इन्हें अपरिमेय संख्याएँ कहा जाता है। इस सीमा को समझने से हमें वास्तविक संख्याओं के संपूर्ण ब्रह्मांड को मैप करने में मदद मिलती है!",
        "body_gu": "આપણે જોયું છે કે સંમેય સંખ્યાઓ કાં તો સમાપ્ત થાય છે અથવા પુનરાવર્તિત થાય છે. પરંતુ જે સંખ્યાઓ ન તો સમાપ્ત થાય છે કે ન તો પુનરાવર્તિત થાય છે, જેમ કે Pi (π) અથવા √2, તેમના વિશે શું? આને અસંમેય સંખ્યાઓ કહેવામાં આવે છે. આ સીમાને સમજવાથી આપણને વાસ્તવિક સંખ્યાઓના સમગ્ર બ્રહ્માંડનો નકશો બનાવવામાં મદદ મળે છે!"
    },
    {
        "id": "KOBJ_CLASS10_MATH_CH1_16",
        "type": "theory",
        "title": "Proof by Contradiction (Discovery)",
        "title_hi": "विरोधाभास द्वारा प्रमाण (खोज)",
        "title_gu": "વિરોધાભાસ દ્વારા સાબિતી (શોધ)",
        "body": "How do you prove someone is NOT at home? You assume they ARE at home, knock on the door, check every room, and if you don't find them, your assumption was wrong! This is called 'Proof by Contradiction', and it's our favorite tool for proving numbers are irrational.",
        "body_hi": "आप कैसे साबित करते हैं कि कोई घर पर नहीं है? आप मान लेते हैं कि वे घर पर हैं, दरवाज़ा खटखटाते हैं, हर कमरे की जाँच करते हैं, और यदि वे नहीं मिलते हैं, तो आपकी धारणा गलत थी! इसे 'विरोधाभास द्वारा प्रमाण' कहा जाता है, और यह संख्याओं को अपरिमेय साबित करने का हमारा पसंदीदा उपकरण है।",
        "body_gu": "તમે કેવી રીતે સાબિત કરશો કે કોઈ ઘરે નથી? તમે ધારો છો કે તેઓ ઘરે છે, દરવાજો ખખડાવો છો, દરેક રૂમ તપાસો છો, અને જો તમને તેઓ ન મળે, તો તમારી ધારણા ખોટી હતી! આને 'વિરોધાભાસ દ્વારા સાબિતી' કહેવામાં આવે છે, અને સંખ્યાઓ અસંમેય છે તે સાબિત કરવા માટે તે અમારું મનપસંદ સાધન છે."
    },
    {
        "id": "KOBJ_CLASS10_MATH_CH1_17",
        "type": "worked_example",
        "title": "Exercise 1.2 Q1: Prove √5 is irrational",
        "title_hi": "प्रश्नावली 1.2 Q1: सिद्ध कीजिए कि √5 एक अपरिमेय संख्या है",
        "title_gu": "સ્વાધ્યાય 1.2 Q1: સાબિત કરો કે √5 અસંમેય છે",
        "question": "Prove that √5 is irrational.",
        "question_hi": "सिद्ध कीजिए कि √5 एक अपरिमेय संख्या है।",
        "question_gu": "સાબિત કરો કે √5 અસંમેય છે.",
        "solution": "Let us assume, to the contrary, that √5 is rational.\nThen √5 = a/b, where a and b are co-prime integers and b ≠ 0.\nSquaring both sides:\n5 = a²/b² => a² = 5b².\nThis shows a² is divisible by 5, meaning 'a' is also divisible by 5. (Let a = 5c for some integer c).\nSubstitute a = 5c:\n(5c)² = 5b² => 25c² = 5b² => b² = 5c².\nThis shows b² is divisible by 5, meaning 'b' is also divisible by 5.\nSince both a and b are divisible by 5, they are not co-prime. This contradicts our initial assumption.\nTherefore, √5 is an irrational number.",
        "solution_hi": "मान लीजिए, इसके विपरीत, कि √5 एक परिमेय संख्या है।\nतब √5 = a/b, जहाँ a और b सह-अभाज्य पूर्णांक हैं और b ≠ 0।\nदोनों पक्षों का वर्ग करने पर:\n5 = a²/b² => a² = 5b².\nयह दर्शाता है कि a², 5 से विभाज्य है, जिसका अर्थ है कि 'a' भी 5 से विभाज्य है। (माना किसी पूर्णांक c के लिए a = 5c)।\na = 5c प्रतिस्थापित करें:\n(5c)² = 5b² => 25c² = 5b² => b² = 5c².\nयह दर्शाता है कि b², 5 से विभाज्य है, जिसका अर्थ है कि 'b' भी 5 से विभाज्य है।\nचूँकि a और b दोनों 5 से विभाज्य हैं, वे सह-अभाज्य नहीं हैं। यह हमारी प्रारंभिक धारणा का खंडन करता है।\nइसलिए, √5 एक अपरिमेय संख्या है।",
        "solution_gu": "ચાલો ધારી લઈએ કે, વિપરિત રીતે, કે √5 સંમેય છે.\nપછી √5 = a/b, જ્યાં a અને b સહ-અવિભાજ્ય પૂર્ણાંકો છે અને b ≠ 0.\nબંને બાજુ વર્ગ કરતા:\n5 = a²/b² => a² = 5b².\nઆ દર્શાવે છે કે a² એ 5 વડે વિભાજ્ય છે, એટલે કે 'a' પણ 5 વડે વિભાજ્ય છે. (ધારો કે કોઈ પૂર્ણાંક c માટે a = 5c).\na = 5c મૂકો:\n(5c)² = 5b² => 25c² = 5b² => b² = 5c².\nઆ દર્શાવે છે કે b² એ 5 વડે વિભાજ્ય છે, એટલે કે 'b' પણ 5 વડે વિભાજ્ય છે.\nકારણ કે a અને b બંને 5 વડે વિભાજ્ય છે, તેઓ સહ-અવિભાજ્ય નથી. આ આપણી પ્રારંભિક ધારણાનો વિરોધાભાસ કરે છે.\nતેથી, √5 એક અસંમેય સંખ્યા છે."
    },
    {
        "id": "KOBJ_CLASS10_MATH_CH1_18",
        "type": "worked_example",
        "title": "Exercise 1.2 Q2: Prove 3 + 2√5 is irrational",
        "title_hi": "प्रश्नावली 1.2 Q2: सिद्ध कीजिए कि 3 + 2√5 अपरिमेय है",
        "title_gu": "સ્વાધ્યાય 1.2 Q2: સાબિત કરો કે 3 + 2√5 અસંમેય છે",
        "question": "Prove that 3 + 2√5 is irrational.",
        "question_hi": "सिद्ध कीजिए कि 3 + 2√5 एक अपरिमेय संख्या है।",
        "question_gu": "સાબિત કરો કે 3 + 2√5 અસંમેય છે.",
        "solution": "Let us assume that 3 + 2√5 is rational.\nTherefore, 3 + 2√5 = a/b (where a and b are co-prime integers, b ≠ 0).\nRearranging the terms, we get:\n2√5 = (a/b) - 3 = (a - 3b)/b\nFurther isolating √5, we get:\n√5 = (a - 3b) / (2b)\nSince a and b are integers, (a - 3b)/(2b) is a rational number.\nThis implies that √5 is rational.\nHowever, this contradicts the fact that √5 is irrational.\nTherefore, our assumption was incorrect. 3 + 2√5 is irrational.",
        "solution_hi": "मान लीजिए कि 3 + 2√5 एक परिमेय संख्या है।\nइसलिए, 3 + 2√5 = a/b (जहाँ a और b सह-अभाज्य पूर्णांक हैं, b ≠ 0)।\nपदों को व्यवस्थित करने पर, हम पाते हैं:\n2√5 = (a/b) - 3 = (a - 3b)/b\n√5 को अलग करने पर, हम पाते हैं:\n√5 = (a - 3b) / (2b)\nचूँकि a और b पूर्णांक हैं, (a - 3b)/(2b) एक परिमेय संख्या है।\nइसका तात्पर्य यह है कि √5 परिमेय है।\nहालाँकि, यह इस तथ्य का खंडन करता है कि √5 अपरिमेय है।\nइसलिए, हमारी धारणा गलत थी। 3 + 2√5 अपरिमेय है।",
        "solution_gu": "ધારો કે 3 + 2√5 એ સંમેય છે.\nતેથી, 3 + 2√5 = a/b (જ્યાં a અને b સહ-અવિભાજ્ય પૂર્ણાંકો છે, b ≠ 0).\nપદોની ગોઠવણી કરતા, આપણને મળે છે:\n2√5 = (a/b) - 3 = (a - 3b)/b\n√5 ને અલગ કરતા, આપણને મળે છે:\n√5 = (a - 3b) / (2b)\nકારણ કે a અને b પૂર્ણાંકો છે, (a - 3b)/(2b) એક સંમેય સંખ્યા છે.\nઆ સૂચવે છે કે √5 સંમેય છે.\nજો કે, આ એ હકીકતનો વિરોધાભાસ કરે છે કે √5 અસંમેય છે.\nતેથી, આપણી ધારણા ખોટી હતી. 3 + 2√5 અસંમેય છે."
    },
    {
        "id": "KOBJ_CLASS10_MATH_CH1_19",
        "type": "worked_example",
        "title": "Exercise 1.2 Q3: Proving more irrationals",
        "title_hi": "प्रश्नावली 1.2 Q3: अधिक अपरिमेय सिद्ध करना",
        "title_gu": "સ્વાધ્યાય 1.2 Q3: વધુ અસંમેય સાબિત કરવું",
        "question": "Prove that the following are irrationals: (i) 1/√2 (ii) 7√5 (iii) 6 + √2",
        "question_hi": "सिद्ध कीजिए कि निम्नलिखित अपरिमेय हैं: (i) 1/√2 (ii) 7√5 (iii) 6 + √2",
        "question_gu": "સાબિત કરો કે નીચેના અસંમેય છે: (i) 1/√2 (ii) 7√5 (iii) 6 + √2",
        "solution": "(i) Prove 1/√2 is irrational:\nAssume 1/√2 is rational. So 1/√2 = a/b (a, b co-prime integers, a, b ≠ 0).\nTaking reciprocals: √2 = b/a.\nSince b/a is rational, this means √2 is rational, which is a contradiction. Hence 1/√2 is irrational.\n\n(ii) Prove 7√5 is irrational:\nAssume 7√5 is rational. So 7√5 = a/b (a, b co-prime integers, b ≠ 0).\nIsolating the root: √5 = a / (7b).\nSince a/(7b) is rational, √5 must be rational, which is a contradiction. Hence 7√5 is irrational.\n\n(iii) Prove 6 + √2 is irrational:\nAssume 6 + √2 is rational. So 6 + √2 = a/b (a, b co-prime integers, b ≠ 0).\nRearranging: √2 = (a/b) - 6 = (a - 6b) / b.\nSince (a - 6b)/b is rational, √2 must be rational, which is a contradiction. Hence 6 + √2 is irrational.",
        "solution_hi": "(i) सिद्ध करें 1/√2 अपरिमेय है:\nमान लें 1/√2 परिमेय है। अतः 1/√2 = a/b (a, b सह-अभाज्य पूर्णांक, a, b ≠ 0)।\nव्युत्क्रम लेने पर: √2 = b/a।\nचूँकि b/a परिमेय है, इसका अर्थ है √2 परिमेय है, जो एक विरोधाभास है। अतः 1/√2 अपरिमेय है।\n\n(ii) सिद्ध करें 7√5 अपरिमेय है:\nमान लें 7√5 परिमेय है। अतः 7√5 = a/b (a, b सह-अभाज्य पूर्णांक, b ≠ 0)।\nमूल को अलग करने पर: √5 = a / (7b)।\nचूँकि a/(7b) परिमेय है, √5 को परिमेय होना चाहिए, जो एक विरोधाभास है। अतः 7√5 अपरिमेय है।\n\n(iii) सिद्ध करें 6 + √2 अपरिमेय है:\nमान लें 6 + √2 परिमेय है। अतः 6 + √2 = a/b (a, b सह-अभाज्य पूर्णांक, b ≠ 0)।\nव्यवस्थित करने पर: √2 = (a/b) - 6 = (a - 6b) / b।\nचूँकि (a - 6b)/b परिमेय है, √2 को परिमेय होना चाहिए, जो एक विरोधाभास है। अतः 6 + √2 अपरिमेय है।",
        "solution_gu": "(i) સાબિત કરો 1/√2 અસંમેય છે:\nધારો કે 1/√2 સંમેય છે. તેથી 1/√2 = a/b (a, b સહ-અવિભાજ્ય પૂર્ણાંકો, a, b ≠ 0).\nવ્યસ્ત લેતાં: √2 = b/a.\nકારણ કે b/a સંમેય છે, આનો અર્થ એ છે કે √2 સંમેય છે, જે એક વિરોધાભાસ છે. આથી 1/√2 અસંમેય છે.\n\n(ii) સાબિત કરો 7√5 અસંમેય છે:\nધારો કે 7√5 સંમેય છે. તેથી 7√5 = a/b (a, b સહ-અવિભાજ્ય પૂર્ણાંકો, b ≠ 0).\nમૂળને અલગ કરતા: √5 = a / (7b).\nકારણ કે a/(7b) સંમેય છે, √5 સંમેય હોવું જ જોઈએ, જે એક વિરોધાભાસ છે. આથી 7√5 અસંમેય છે.\n\n(iii) સાબિત કરો 6 + √2 અસંમેય છે:\nધારો કે 6 + √2 સંમેય છે. તેથી 6 + √2 = a/b (a, b સહ-અવિભાજ્ય પૂર્ણાંકો, b ≠ 0).\nગોઠવણ કરતા: √2 = (a/b) - 6 = (a - 6b) / b.\nકારણ કે (a - 6b)/b સંમેય છે, √2 સંમેય હોવું જ જોઈએ, જે એક વિરોધાભાસ છે. આથી 6 + √2 અસંમેય છે."
    },
    
    # Topic 5: Board Exam / Challenge Questions
    {
        "id": "KOBJ_CLASS10_MATH_CH1_20",
        "type": "theory",
        "is_board_challenge": True,
        "title": "Board Preparations (Solved Question Papers)",
        "title_hi": "बोर्ड की तैयारी (हल किए गए प्रश्न पत्र)",
        "title_gu": "બોર્ડની તૈયારી (ઉકેલાયેલા પ્રશ્નપત્રો)",
        "body": "Now that you have mastered the core concepts, let's look at some important past year questions to ensure you are fully prepared for your board exams.",
        "body_hi": "अब जब आपने मूल अवधारणाओं में महारत हासिल कर ली है, तो आइए यह सुनिश्चित करने के लिए कि आप अपनी बोर्ड परीक्षाओं के लिए पूरी तरह से तैयार हैं, पिछले वर्ष के कुछ महत्वपूर्ण प्रश्नों को देखें।",
        "body_gu": "હવે જ્યારે તમે મુખ્ય વિભાવનાઓમાં નિપુણતા મેળવી લીધી છે, તો ચાલો તમે તમારી બોર્ડની પરીક્ષાઓ માટે સંપૂર્ણ રીતે તૈયાર છો તેની ખાતરી કરવા માટે કેટલાક મહત્વપૂર્ણ પાછલા વર્ષના પ્રશ્નો જોઈએ."
    },
    {
        "id": "KOBJ_CLASS10_MATH_CH1_21",
        "type": "mcq",
        "is_board_challenge": True,
        "question": "If two positive integers a and b are written as a = x³y² and b = xy³, where x and y are prime numbers, then HCF(a, b) is:",
        "question_hi": "यदि दो धनात्मक पूर्णांक a और b, a = x³y² और b = xy³ के रूप में लिखे जाते हैं, जहाँ x और y अभाज्य संख्याएँ हैं, तो HCF(a, b) क्या है?",
        "question_gu": "જો બે ધન પૂર્ણાંકો a અને b ને a = x³y² અને b = xy³ તરીકે લખવામાં આવે છે, જ્યાં x અને y અવિભાજ્ય સંખ્યાઓ છે, તો HCF(a, b) છે:",
        "options": ["xy", "xy²", "x³y³", "x²y²"],
        "options_hi": ["xy", "xy²", "x³y³", "x²y²"],
        "options_gu": ["xy", "xy²", "x³y³", "x²y²"],
        "correct_index": 1,
        "explanation": "To find the HCF, we take the smallest power of each common prime factor. The common factors are x and y. Minimum power of x is 1, and minimum power of y is 2. So HCF is xy².",
        "explanation_hi": "HCF ज्ञात करने के लिए, हम प्रत्येक उभयनिष्ठ अभाज्य गुणनखंड की सबसे छोटी घात लेते हैं। उभयनिष्ठ गुणनखंड x और y हैं। x की न्यूनतम घात 1 है, और y की न्यूनतम घात 2 है। इसलिए HCF xy² है।",
        "explanation_gu": "HCF શોધવા માટે, આપણે દરેક સામાન્ય અવિભાજ્ય અવયવની સૌથી નાની ઘાત લઈએ છીએ. સામાન્ય અવયવો x અને y છે. x ની ન્યૂનતમ ઘાત 1 છે, અને y ની ન્યૂનતમ ઘાત 2 છે. તેથી HCF xy² છે."
    }
]

metadata["blocks"] = blocks

with open('/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/cbse_class10_maths_ch1.json', 'w', encoding='utf-8') as f:
    json.dump(metadata, f, ensure_ascii=False, indent=2)

print("Chapter 1 generated successfully.")
