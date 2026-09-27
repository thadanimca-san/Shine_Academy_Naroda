import json

new_blocks = [
    {
      "type": "heading",
      "id": "KOBJ_CLASS10_MATH_CH1_EX_1_1",
      "title": "Exercise 1.1",
      "title_hi": "प्रश्नावली 1.1",
      "title_gu": "સ્વાધ્યાય 1.1"
    },
    {
      "type": "short_note",
      "id": "KOBJ_CLASS10_MATH_CH1_EX_1_1_Q1",
      "difficulty": "Beginner",
      "marks": 2,
      "question_en": "Express 140 as a product of its prime factors.",
      "question_hi": "140 को अभाज्य गुणनखंडों के गुणनफल के रूप में व्यक्त कीजिए।",
      "question_gu": "140 ને તેના અવિભાજ્ય અવયવોના ગુણાકાર સ્વરૂપે દર્શાવો.",
      "answer_en": "140 = 2 × 2 × 5 × 7 = 2² × 5 × 7",
      "answer_hi": "140 = 2 × 2 × 5 × 7 = 2² × 5 × 7",
      "answer_gu": "140 = 2 × 2 × 5 × 7 = 2² × 5 × 7",
      "explanation_en": "We divide 140 by the smallest prime number 2 to get 70. Divide 70 by 2 to get 35. Divide 35 by 5 to get 7. Since 7 is a prime number, we stop here.",
      "explanation_hi": "हम 140 को सबसे छोटी अभाज्य संख्या 2 से विभाजित करते हैं जिससे 70 मिलता है। 70 को 2 से विभाजित करने पर 35 मिलता है। 35 को 5 से विभाजित करने पर 7 मिलता है। चूँकि 7 एक अभाज्य संख्या है, इसलिए हम यहीं रुक जाते हैं।",
      "explanation_gu": "આપણે 140 ને સૌથી નાની અવિભાજ્ય સંખ્યા 2 વડે ભાગીએ છીએ જેથી 70 મળે. 70 ને 2 વડે ભાગવાથી 35 મળે. 35 ને 5 વડે ભાગવાથી 7 મળે. 7 અવિભાજ્ય સંખ્યા હોવાથી આપણે અહીં અટકીએ છીએ."
    },
    {
      "type": "short_note",
      "id": "KOBJ_CLASS10_MATH_CH1_EX_1_1_Q2",
      "difficulty": "Intermediate",
      "marks": 3,
      "question_en": "Find the LCM and HCF of 26 and 91 and verify that LCM × HCF = product of the two numbers.",
      "question_hi": "26 और 91 के LCM और HCF ज्ञात कीजिए तथा इसकी जाँच कीजिए कि दो संख्याओं का गुणनफल = HCF × LCM है।",
      "question_gu": "26 અને 91 ના ગુ.સા.અ. અને લ.સા.અ. શોધો અને ચકાસો કે ગુ.સા.અ. × લ.સા.અ. = બંને સંખ્યાઓનો ગુણાકાર.",
      "answer_en": "Prime factorisation:\n26 = 2 × 13\n91 = 7 × 13\nHCF = 13\nLCM = 2 × 7 × 13 = 182\nVerification: LCM × HCF = 182 × 13 = 2366. Product of numbers = 26 × 91 = 2366.",
      "answer_hi": "अभाज्य गुणनखंड:\n26 = 2 × 13\n91 = 7 × 13\nHCF = 13\nLCM = 2 × 7 × 13 = 182\nसत्यापन: LCM × HCF = 182 × 13 = 2366. संख्याओं का गुणनफल = 26 × 91 = 2366.",
      "answer_gu": "અવિભાજ્ય અવયવો:\n26 = 2 × 13\n91 = 7 × 13\nગુ.સા.અ. = 13\nલ.સા.અ. = 2 × 7 × 13 = 182\nચકાસણી: ગુ.સા.અ. × લ.સા.અ. = 182 × 13 = 2366. સંખ્યાઓનો ગુણાકાર = 26 × 91 = 2366.",
      "explanation_en": "HCF is the product of the smallest power of each common prime factor. LCM is the product of the greatest power of each prime factor.",
      "explanation_hi": "HCF प्रत्येक उभयनिष्ठ अभाज्य गुणनखंड की सबसे छोटी घात का गुणनफल है। LCM प्रत्येक अभाज्य गुणनखंड की सबसे बड़ी घात का गुणनफल है।",
      "explanation_gu": "ગુ.સા.અ. એ દરેક સામાન્ય અવિભાજ્ય અવયવની સૌથી નાની ઘાતનો ગુણાકાર છે. લ.સા.અ. એ દરેક અવિભાજ્ય અવયવની સૌથી મોટી ઘાતનો ગુણાકાર છે."
    },
    {
      "type": "short_note",
      "id": "KOBJ_CLASS10_MATH_CH1_EX_1_1_Q4",
      "difficulty": "Intermediate",
      "marks": 2,
      "question_en": "Given that HCF (306, 657) = 9, find LCM (306, 657).",
      "question_hi": "HCF (306, 657) = 9 दिया है। LCM (306, 657) ज्ञात कीजिए।",
      "question_gu": "જો ગુ.સા.અ. (306, 657) = 9 આપેલ હોય, તો લ.સા.અ. (306, 657) શોધો.",
      "answer_en": "We know that LCM × HCF = Product of two numbers.\nLCM × 9 = 306 × 657\nLCM = (306 × 657) / 9\nLCM = 34 × 657 = 22338",
      "answer_hi": "हम जानते हैं कि LCM × HCF = दो संख्याओं का गुणनफल।\nLCM × 9 = 306 × 657\nLCM = (306 × 657) / 9\nLCM = 34 × 657 = 22338",
      "answer_gu": "આપણે જાણીએ છીએ કે ગુ.સા.અ. × લ.સા.અ. = બે સંખ્યાઓનો ગુણાકાર.\nલ.સા.અ. × 9 = 306 × 657\nલ.સા.અ. = (306 × 657) / 9\nલ.સા.અ. = 34 × 657 = 22338",
      "explanation_en": "This uses the fundamental relationship between LCM and HCF of any two positive integers a and b: LCM(a,b) × HCF(a,b) = a × b.",
      "explanation_hi": "यह किन्हीं दो धनात्मक पूर्णांकों a और b के LCM और HCF के बीच मूलभूत संबंध का उपयोग करता है: LCM(a,b) × HCF(a,b) = a × b.",
      "explanation_gu": "આ કોઈપણ બે ધન પૂર્ણાંકો a અને b ના ગુ.સા.અ. અને લ.સા.અ. વચ્ચેના મૂળભૂત સંબંધનો ઉપયોગ કરે છે: લ.સા.અ.(a,b) × ગુ.સા.અ.(a,b) = a × b."
    },
    {
      "type": "short_note",
      "id": "KOBJ_CLASS10_MATH_CH1_EX_1_1_Q5",
      "difficulty": "Advanced",
      "marks": 2,
      "question_en": "Check whether 6ⁿ can end with the digit 0 for any natural number n.",
      "question_hi": "जाँच कीजिए कि क्या किसी प्राकृत संख्या n के लिए, 6ⁿ अंक 0 पर समाप्त हो सकती है।",
      "question_gu": "ચકાસો કે કોઈ પ્રાકૃતિક સંખ્યા n માટે 6ⁿ નો અંતિમ અંક 0 હોઈ શકે કે કેમ.",
      "answer_en": "If a number ends with 0, it must be divisible by 10 (i.e., by both 2 and 5).\nThe prime factorisation of 6ⁿ is (2 × 3)ⁿ = 2ⁿ × 3ⁿ.\nSince there is no factor of 5 in the prime factorisation, 6ⁿ can never end with the digit 0.",
      "answer_hi": "यदि कोई संख्या 0 पर समाप्त होती है, तो वह 10 (यानी 2 और 5 दोनों) से विभाज्य होनी चाहिए।\n6ⁿ का अभाज्य गुणनखंडन (2 × 3)ⁿ = 2ⁿ × 3ⁿ है।\nचूँकि अभाज्य गुणनखंडन में 5 का कोई गुणनखंड नहीं है, इसलिए 6ⁿ कभी भी अंक 0 पर समाप्त नहीं हो सकता।",
      "answer_gu": "જો કોઈ સંખ્યા 0 પર સમાપ્ત થાય, તો તે 10 (એટલે ​​કે 2 અને 5 બંને) વડે વિભાજ્ય હોવી જોઈએ.\n6ⁿ ના અવિભાજ્ય અવયવો (2 × 3)ⁿ = 2ⁿ × 3ⁿ છે.\nઅવિભાજ્ય અવયવોમાં 5 નો કોઈ અવયવ ન હોવાથી, 6ⁿ ક્યારેય 0 અંક પર સમાપ્ત થઈ શકે નહીં.",
      "explanation_en": "According to the Fundamental Theorem of Arithmetic, this prime factorisation is unique. Without a factor of 5, the number cannot be a multiple of 10.",
      "explanation_hi": "अंकगणित की आधारभूत प्रमेय के अनुसार, यह अभाज्य गुणनखंडन अद्वितीय है। 5 के गुणनखंड के बिना, संख्या 10 का गुणज नहीं हो सकती है।",
      "explanation_gu": "અંકગણિતના મૂળભૂત પ્રમેય મુજબ, આ અવિભાજ્ય અવયવો અદ્વિતીય છે. 5 ના અવયવ વિના, સંખ્યા 10 નો ગુણક હોઈ શકે નહીં."
    },
    {
      "type": "heading",
      "id": "KOBJ_CLASS10_MATH_CH1_EX_1_2",
      "title": "Exercise 1.2",
      "title_hi": "प्रश्नावली 1.2",
      "title_gu": "સ્વાધ્યાય 1.2"
    },
    {
      "type": "short_note",
      "id": "KOBJ_CLASS10_MATH_CH1_EX_1_2_Q1",
      "difficulty": "Advanced",
      "marks": 3,
      "question_en": "Prove that √5 is irrational.",
      "question_hi": "सिद्ध कीजिए कि √5 एक अपरिमेय संख्या है।",
      "question_gu": "સાબિત કરો કે √5 અસંમેય છે.",
      "answer_en": "Let us assume √5 is rational. Then √5 = a/b (where a and b are coprime integers, b ≠ 0).\nSquaring both sides: 5 = a²/b² => a² = 5b².\nThis means a² is divisible by 5, so 'a' is also divisible by 5. Let a = 5c.\nSubstituting a: (5c)² = 5b² => 25c² = 5b² => b² = 5c².\nThis means b² is divisible by 5, so 'b' is also divisible by 5.\nSince both a and b are divisible by 5, they are not coprime. This contradicts our assumption. Hence, √5 is irrational.",
      "answer_hi": "माना कि √5 एक परिमेय संख्या है। तब √5 = a/b (जहाँ a और b सहअभाज्य पूर्णांक हैं, b ≠ 0)।\nदोनों पक्षों का वर्ग करने पर: 5 = a²/b² => a² = 5b².\nइसका अर्थ है कि a², 5 से विभाज्य है, इसलिए 'a' भी 5 से विभाज्य होगा। माना a = 5c.\na का मान रखने पर: (5c)² = 5b² => 25c² = 5b² => b² = 5c².\nइसका अर्थ है कि b², 5 से विभाज्य है, इसलिए 'b' भी 5 से विभाज्य होगा।\nचूँकि a और b दोनों 5 से विभाज्य हैं, इसलिए वे सहअभाज्य नहीं हैं। यह हमारी कल्पना का विरोधाभास है। अतः √5 एक अपरिमेय संख्या है।",
      "answer_gu": "ધારો કે √5 સંમેય સંખ્યા છે. તેથી √5 = a/b (જ્યાં a અને b પરસ્પર અવિભાજ્ય પૂર્ણાંકો છે, b ≠ 0).\nબંને બાજુનો વર્ગ કરતા: 5 = a²/b² => a² = 5b².\nઆનો અર્થ એ છે કે a² એ 5 વડે વિભાજ્ય છે, તેથી 'a' પણ 5 વડે વિભાજ્ય છે. ધારો કે a = 5c.\na ની કિંમત મુકતા: (5c)² = 5b² => 25c² = 5b² => b² = 5c².\nઆનો અર્થ એ છે કે b² એ 5 વડે વિભાજ્ય છે, તેથી 'b' પણ 5 વડે વિભાજ્ય છે.\nકારણ કે a અને b બંને 5 વડે વિભાજ્ય છે, તેઓ પરસ્પર અવિભાજ્ય નથી. આ આપણી ધારણાનો વિરોધાભાસ છે. તેથી, √5 અસંમેય છે.",
      "explanation_en": "This is a classic proof by contradiction. We assume the opposite of what we want to prove, and show that it leads to a logical impossibility.",
      "explanation_hi": "यह विरोधाभास द्वारा एक क्लासिक प्रमाण है। हम जो साबित करना चाहते हैं उसके विपरीत मान लेते हैं, और दिखाते हैं कि इससे तार्किक असंभवता उत्पन्न होती है।",
      "explanation_gu": "આ વિરોધાભાસ દ્વારા એક ઉત્તમ સાબિતી છે. આપણે જે સાબિત કરવા માંગીએ છીએ તેનાથી વિરુદ્ધ ધારીએ છીએ, અને બતાવીએ છીએ કે તે તાર્કિક અશક્યતા તરફ દોરી જાય છે."
    },
    {
      "type": "short_note",
      "id": "KOBJ_CLASS10_MATH_CH1_EX_1_2_Q2",
      "difficulty": "Intermediate",
      "marks": 3,
      "question_en": "Prove that 3 + 2√5 is irrational.",
      "question_hi": "सिद्ध कीजिए कि 3 + 2√5 एक अपरिमेय संख्या है।",
      "question_gu": "સાબિત કરો કે 3 + 2√5 અસંમેય છે.",
      "answer_en": "Assume 3 + 2√5 is rational. Let 3 + 2√5 = a/b (a, b are coprime integers, b ≠ 0).\n2√5 = (a/b) - 3 = (a - 3b) / b\n√5 = (a - 3b) / 2b\nSince a and b are integers, (a - 3b)/2b is a rational number.\nThis implies √5 is rational. But we know √5 is irrational.\nThis contradiction arises because of our incorrect assumption. Hence, 3 + 2√5 is irrational.",
      "answer_hi": "माना कि 3 + 2√5 एक परिमेय संख्या है। माना 3 + 2√5 = a/b (a, b सहअभाज्य पूर्णांक हैं, b ≠ 0)।\n2√5 = (a/b) - 3 = (a - 3b) / b\n√5 = (a - 3b) / 2b\nचूँकि a और b पूर्णांक हैं, (a - 3b)/2b एक परिमेय संख्या है।\nइसका अर्थ है कि √5 परिमेय है। लेकिन हम जानते हैं कि √5 अपरिमेय है।\nयह विरोधाभास हमारी गलत कल्पना के कारण उत्पन्न हुआ है। अतः 3 + 2√5 अपरिमेय है।",
      "answer_gu": "ધારો કે 3 + 2√5 સંમેય સંખ્યા છે. ધારો કે 3 + 2√5 = a/b (a, b પરસ્પર અવિભાજ્ય પૂર્ણાંકો છે, b ≠ 0).\n2√5 = (a/b) - 3 = (a - 3b) / b\n√5 = (a - 3b) / 2b\nકારણ કે a અને b પૂર્ણાંકો છે, (a - 3b)/2b સંમેય સંખ્યા છે.\nઆ દર્શાવે છે કે √5 સંમેય છે. પરંતુ આપણે જાણીએ છીએ કે √5 અસંમેય છે.\nઆ વિરોધાભાસ આપણી ખોટી ધારણાને કારણે ઊભો થયો છે. તેથી, 3 + 2√5 અસંમેય છે.",
      "explanation_en": "By isolating the irrational part (√5), we show that a rational number would have to equal an irrational one, which is impossible.",
      "explanation_hi": "अपरिमेय भाग (√5) को अलग करके, हम दिखाते हैं कि एक परिमेय संख्या को एक अपरिमेय संख्या के बराबर होना होगा, जो असंभव है।",
      "explanation_gu": "અસંમેય ભાગ (√5) ને અલગ કરીને, આપણે બતાવીએ છીએ કે સંમેય સંખ્યા અસંમેય સંખ્યા બરાબર હોવી જોઈએ, જે અશક્ય છે."
    }
]

file_path = "app_core/chapters/ncert_class10_maths_ch1.json"
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

existing_ids = [block.get("id") for block in data.get("blocks", [])]
count = 0
for block in new_blocks:
    if block["id"] not in existing_ids:
        data["blocks"].append(block)
        count += 1

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Successfully appended {count} exercise blocks!")
