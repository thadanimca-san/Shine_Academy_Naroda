import json
import os

def main():
    metadata = {
        "title": "Quadratic Equations",
        "subject": "Maths",
        "grade": "10",
        "curriculum": ["GSEB", "NCERT", "CBSE"],
        "difficulty": "Intermediate",
        "version": "4.0.0",
        "id": "cbse_class10_maths_ch4"
    }

    blocks = []

    # 8-Step Socratic Pedagogy Arc
    
    # 1. HOOK
    blocks.append({
        "id": "KOBJ_CLASS10_MATH_CH4_HOOK",
        "type": "hook",
        "title": "The Carpet Problem",
        "title_hi": "कालीन की समस्या",
        "title_gu": "કાર્પેટની સમસ્યા",
        "body": "Imagine you have a beautiful rectangular carpet, and its area is 300 square meters. You know that its length is one meter more than twice its breadth. How can we find the exact length and breadth? This puzzle leads us into the world of Quadratic Equations!",
        "body_hi": "कल्पना कीजिए कि आपके पास एक सुंदर आयताकार कालीन है, और इसका क्षेत्रफल 300 वर्ग मीटर है। आप जानते हैं कि इसकी लंबाई इसकी चौड़ाई के दोगुने से एक मीटर अधिक है। हम सटीक लंबाई और चौड़ाई कैसे ज्ञात कर सकते हैं? यह पहेली हमें द्विघात समीकरणों की दुनिया में ले जाती है!",
        "body_gu": "કલ્પના કરો કે તમારી પાસે એક સુંદર લંબચોરસ કાર્પેટ છે, અને તેનું ક્ષેત્રફળ 300 ચોરસ મીટર છે. તમે જાણો છો કે તેની લંબાઈ તેની પહોળાઈના બમણા કરતાં એક મીટર વધુ છે. આપણે ચોક્કસ લંબાઈ અને પહોળાઈ કેવી રીતે શોધી શકીએ? આ કોયડો આપણને દ્વિઘાત સમીકરણોની દુનિયામાં લઈ જાય છે!"
    })

    # 2. SOCRATIC THINKING
    blocks.append({
        "id": "KOBJ_CLASS10_MATH_CH4_SOCRATIC",
        "type": "socratic_question",
        "title": "Think About It",
        "title_hi": "इस पर विचार करें",
        "title_gu": "આના વિશે વિચારો",
        "body": "If we say the breadth is 'x', then the length is '2x + 1'. What happens when you multiply them to find the area?",
        "body_hi": "यदि हम कहते हैं कि चौड़ाई 'x' है, तो लंबाई '2x + 1' होगी। जब आप क्षेत्रफल ज्ञात करने के लिए उनका गुणा करते हैं तो क्या होता है?",
        "body_gu": "જો આપણે કહીએ કે પહોળાઈ 'x' છે, તો લંબાઈ '2x + 1' છે. જ્યારે તમે ક્ષેત્રફળ શોધવા માટે તેમનો ગુણાકાર કરો છો ત્યારે શું થાય છે?",
        "options": ["You get a linear equation", "You get a number", "You get an expression with x squared (x²)", "You get an expression with x cubed (x³)"],
        "options_hi": ["आपको एक रैखिक समीकरण मिलता है", "आपको एक संख्या मिलती है", "आपको x वर्ग (x²) वाला व्यंजक मिलता है", "आपको x घन (x³) वाला व्यंजक मिलता है"],
        "options_gu": ["તમને રેખીય સમીકરણ મળે છે", "તમને એક નંબર મળે છે", "તમને x વર્ગ (x²) સાથે અભિવ્યક્તિ મળે છે", "તમને x ઘન (x³) સાથે અભિવ્યક્તિ મળે છે"],
        "correct_index": 2,
        "explanation": "Multiplying x and (2x + 1) gives 2x² + x. The highest power of x is 2, which makes it a 'quadratic' expression.",
        "explanation_hi": "x और (2x + 1) का गुणा करने पर 2x² + x प्राप्त होता है। x की उच्चतम घात 2 है, जो इसे 'द्विघात' व्यंजक बनाता है।",
        "explanation_gu": "x અને (2x + 1) નો ગુણાકાર કરવાથી 2x² + x મળે છે. x ની સૌથી વધુ ઘાત 2 છે, જે તેને 'દ્વિઘાત' અભિવ્યક્તિ બનાવે છે."
    })

    # 3. DISCOVERY
    blocks.append({
        "id": "KOBJ_CLASS10_MATH_CH4_DISCOVERY",
        "type": "discovery",
        "title": "The Power of Two",
        "title_hi": "दो की शक्ति",
        "title_gu": "બે ની શક્તિ",
        "body": "Whenever we model situations involving area, gravity, or profit optimization, we often encounter equations where the unknown variable is squared. This 'power of two' gives the equation a curve (a parabola) when graphed, unlike the straight lines of linear equations.",
        "body_hi": "जब भी हम क्षेत्रफल, गुरुत्वाकर्षण, या लाभ अनुकूलन जैसी स्थितियों का मॉडल बनाते हैं, तो हम अक्सर ऐसे समीकरणों का सामना करते हैं जहाँ अज्ञात चर का वर्ग (squared) होता है। यह 'दो की शक्ति' रैखिक समीकरणों की सीधी रेखाओं के विपरीत, ग्राफ़ पर बनाए जाने पर समीकरण को एक वक्र (पैराबोला) देती है।",
        "body_gu": "જ્યારે પણ આપણે ક્ષેત્રફળ, ગુરુત્વાકર્ષણ અથવા નફાના ઑપ્ટિમાઇઝેશનને લગતી પરિસ્થિતિઓનું મોડેલ કરીએ છીએ, ત્યારે આપણે ઘણીવાર એવા સમીકરણોનો સામનો કરીએ છીએ જ્યાં અજાણ્યા ચલનો વર્ગ હોય છે. આ 'બે ની શક્તિ' સમીકરણને આલેખિત કરવામાં આવે ત્યારે વળાંક (પેરાબોલા) આપે છે, રેખીય સમીકરણોની સીધી રેખાઓથી વિપરીત."
    })

    # 4. REVEAL
    blocks.append({
        "id": "KOBJ_CLASS10_MATH_CH4_REVEAL",
        "type": "theory",
        "title": "The Standard Form",
        "title_hi": "मानक रूप",
        "title_gu": "પ્રમાણભૂત સ્વરૂપ",
        "body": "A quadratic equation in the variable x is an equation of the form ax² + bx + c = 0, where a, b, and c are real numbers, and a ≠ 0. For example, 2x² + x - 300 = 0 is a quadratic equation. The name 'Quadratic' comes from 'quad' meaning square, because the variable gets squared (like the area of a square).",
        "body_hi": "चर x में एक द्विघात समीकरण ax² + bx + c = 0 के रूप का एक समीकरण है, जहाँ a, b, और c वास्तविक संख्याएँ हैं, और a ≠ 0 है। उदाहरण के लिए, 2x² + x - 300 = 0 एक द्विघात समीकरण है। 'क्वाड्रेटिक' (Quadratic) नाम 'क्वाड' (quad) से आया है जिसका अर्थ है वर्ग, क्योंकि चर का वर्ग किया जाता है (जैसे वर्ग का क्षेत्रफल)।",
        "body_gu": "ચલ x માં દ્વિઘાત સમીકરણ એ ax² + bx + c = 0 ના સ્વરૂપનું સમીકરણ છે, જ્યાં a, b, અને c વાસ્તવિક સંખ્યાઓ છે, અને a ≠ 0. ઉદાહરણ તરીકે, 2x² + x - 300 = 0 એ દ્વિઘાત સમીકરણ છે. 'ક્વાડ્રેટિક' નામ 'ક્વાડ' પરથી આવે છે જેનો અર્થ ચોરસ થાય છે, કારણ કે ચલનો વર્ગ થાય છે (જેમ કે ચોરસનું ક્ષેત્રફળ)."
    })

    # 5. KNOWLEDGE CHECK
    blocks.append({
        "id": "KOBJ_CLASS10_MATH_CH4_CHECK",
        "type": "mcq",
        "question": "Which of the following is the standard form of a quadratic equation?",
        "question_hi": "निम्नलिखित में से कौन सा द्विघात समीकरण का मानक रूप है?",
        "question_gu": "નીચેનામાંથી કયું દ્વિઘાત સમીકરણનું પ્રમાણભૂત સ્વરૂપ છે?",
        "options": ["ax + b = 0", "ax² + bx + c = 0, a ≠ 0", "ax³ + bx² + cx + d = 0", "y = mx + c"],
        "options_hi": ["ax + b = 0", "ax² + bx + c = 0, a ≠ 0", "ax³ + bx² + cx + d = 0", "y = mx + c"],
        "options_gu": ["ax + b = 0", "ax² + bx + c = 0, a ≠ 0", "ax³ + bx² + cx + d = 0", "y = mx + c"],
        "correct_index": 1,
        "explanation": "The standard form is ax² + bx + c = 0, where 'a' cannot be zero. If 'a' is zero, it becomes a linear equation.",
        "explanation_hi": "मानक रूप ax² + bx + c = 0 है, जहाँ 'a' शून्य नहीं हो सकता। यदि 'a' शून्य है, तो यह एक रैखिक समीकरण बन जाता है।",
        "explanation_gu": "પ્રમાણભૂત સ્વરૂપ ax² + bx + c = 0 છે, જ્યાં 'a' શૂન્ય ન હોઈ શકે. જો 'a' શૂન્ય છે, તો તે રેખીય સમીકરણ બની જાય છે."
    })

    # 6. REFLECTION
    blocks.append({
        "id": "KOBJ_CLASS10_MATH_CH4_REFLECTION",
        "type": "reflection",
        "title": "Reflection",
        "title_hi": "चिंतन (Reflection)",
        "title_gu": "પ્રતિબિંબ",
        "body": "Can you think of a situation in real life, other than calculating area, where you might need to multiply two unknown quantities that depend on each other? How about speed, distance, and time?",
        "body_hi": "क्या आप वास्तविक जीवन में कोई ऐसी स्थिति सोच सकते हैं, क्षेत्रफल की गणना के अलावा, जहाँ आपको एक-दूसरे पर निर्भर दो अज्ञात राशियों को गुणा करने की आवश्यकता हो सकती है? गति, दूरी और समय के बारे में क्या विचार है?",
        "body_gu": "શું તમે વાસ્તવિક જીવનમાં એવી પરિસ્થિતિ વિચારી શકો છો, ક્ષેત્રફળની ગણતરી સિવાય, જ્યાં તમારે એકબીજા પર આધાર રાખતી બે અજાણી માત્રાઓનો ગુણાકાર કરવાની જરૂર પડી શકે? ઝડપ, અંતર અને સમય વિશે શું?"
    })

    # 7. CONNECTION
    blocks.append({
        "id": "KOBJ_CLASS10_MATH_CH4_CONNECTION",
        "type": "theory",
        "title": "Connecting the Graph",
        "title_hi": "ग्राफ को जोड़ना",
        "title_gu": "ગ્રાફને જોડવું",
        "body": "In Chapter 2 (Polynomials), you learned that a quadratic polynomial ax² + bx + c forms a U-shaped curve called a parabola. The points where this curve crosses the x-axis are the 'zeros' of the polynomial. When we equate it to zero (ax² + bx + c = 0), those exact 'zeros' become the 'roots' or solutions of our quadratic equation!",
        "body_hi": "अध्याय 2 (बहुपद) में, आपने सीखा कि एक द्विघात बहुपद ax² + bx + c एक U-आकार का वक्र बनाता है जिसे पैराबोला कहा जाता है। वे बिंदु जहाँ यह वक्र x-अक्ष को पार करता है, बहुपद के 'शून्यक' (zeros) कहलाते हैं। जब हम इसे शून्य के बराबर करते हैं (ax² + bx + c = 0), तो वही 'शून्यक' हमारे द्विघात समीकरण के 'मूल' (roots) या हल बन जाते हैं!",
        "body_gu": "પ્રકરણ 2 (બહુપદીઓ) માં, તમે શીખ્યા કે દ્વિઘાત બહુપદી ax² + bx + c એક U-આકારનો વળાંક બનાવે છે જેને પેરાબોલા કહેવાય છે. જે બિંદુઓ પર આ વળાંક x-અક્ષને પાર કરે છે તે બહુપદીના 'શૂન્યો' છે. જ્યારે આપણે તેને શૂન્ય સમાન કરીએ છીએ (ax² + bx + c = 0), ત્યારે તે જ 'શૂન્યો' આપણા દ્વિઘાત સમીકરણના 'મૂળ' અથવા ઉકેલો બની જાય છે!"
    })

    # 8. MASTERY
    blocks.append({
        "id": "KOBJ_CLASS10_MATH_CH4_MASTERY",
        "type": "mastery",
        "title": "Mastery Challenge",
        "title_hi": "महारत की चुनौती",
        "title_gu": "માસ્ટરી ચેલેન્જ",
        "body": "Take a piece of paper. Try to expand the equation (x + 2)³ = x³ - 4. Once expanded, simplify it by bringing all terms to one side. Does it become a quadratic equation? Check if the highest power of x remaining is 2.",
        "body_hi": "एक कागज का टुकड़ा लें। समीकरण (x + 2)³ = x³ - 4 का विस्तार करने का प्रयास करें। विस्तार होने के बाद, सभी पदों को एक तरफ लाकर इसे सरल बनाएं। क्या यह एक द्विघात समीकरण बन जाता है? जाँच करें कि क्या x की बची हुई उच्चतम घात 2 है।",
        "body_gu": "કાગળનો ટુકડો લો. સમીકરણ (x + 2)³ = x³ - 4 ને વિસ્તૃત કરવાનો પ્રયાસ કરો. એકવાર વિસ્તૃત થઈ ગયા પછી, બધી શરતોને એક બાજુ લાવીને તેને સરળ બનાવો. શું તે દ્વિઘાત સમીકરણ બને છે? તપાસો કે શું x ની બાકી રહેલી સૌથી વધુ ઘાત 2 છે."
    })

    # Adding EXERCISES
    # EXERCISE 4.1
    # Q1: Check whether the following are quadratic equations:
    ex_questions = [
        {"q": "(x + 1)² = 2(x - 3)", "ans": "Yes", "idx": 0},
        {"q": "x² - 2x = (-2)(3 - x)", "ans": "Yes", "idx": 0},
        {"q": "(x - 2)(x + 1) = (x - 1)(x + 3)", "ans": "No", "idx": 1},
        {"q": "(x - 3)(2x + 1) = x(x + 5)", "ans": "Yes", "idx": 0},
        {"q": "(2x - 1)(x - 3) = (x + 5)(x - 1)", "ans": "Yes", "idx": 0},
        {"q": "x² + 3x + 1 = (x - 2)²", "ans": "No", "idx": 1},
        {"q": "(x + 2)³ = 2x(x² - 1)", "ans": "No", "idx": 1},
        {"q": "x³ - 4x² - x + 1 = (x - 2)³", "ans": "Yes", "idx": 0}
    ]

    for i, item in enumerate(ex_questions):
        blocks.append({
            "id": f"KOBJ_CLASS10_MATH_CH4_EX4_1_Q1_{i+1}",
            "type": "mcq",
            "question": f"Check whether the following is a quadratic equation: {item['q']}",
            "question_hi": f"जांचें कि क्या निम्नलिखित एक द्विघात समीकरण है: {item['q']}",
            "question_gu": f"તપાસો કે શું નીચેનું દ્વિઘાત સમીકરણ છે: {item['q']}",
            "options": ["Yes, it is a quadratic equation", "No, it is not a quadratic equation"],
            "options_hi": ["हाँ, यह एक द्विघात समीकरण है", "नहीं, यह द्विघात समीकरण नहीं है"],
            "options_gu": ["હા, તે દ્વિઘાત સમીકરણ છે", "ના, તે દ્વિઘાત સમીકરણ નથી"],
            "correct_index": item['idx'],
            "explanation": f"Simplifying {item['q']} helps determine the highest degree of x.",
            "explanation_hi": f"{item['q']} को सरल बनाने से x की उच्चतम घात निर्धारित करने में मदद मिलती है।",
            "explanation_gu": f"{item['q']} ને સરળ બનાવવાથી x ની ઉચ્ચતમ ડિગ્રી નક્કી કરવામાં મદદ મળે છે."
        })

    # EXERCISE 4.2 - Factorisation
    factorisation_qs = [
        {"q": "x² - 3x - 10 = 0", "ans": "x = 5, x = -2", "opts": ["x = 5, x = -2", "x = -5, x = 2", "x = 10, x = 1", "x = -10, x = 1"], "idx": 0},
        {"q": "2x² + x - 6 = 0", "ans": "x = -2, x = 3/2", "opts": ["x = 2, x = -3/2", "x = -2, x = 3/2", "x = 3, x = -1", "x = -3, x = 1"], "idx": 1},
        {"q": "√2x² + 7x + 5√2 = 0", "ans": "x = -5/√2, x = -√2", "opts": ["x = 5/√2, x = √2", "x = -5/√2, x = -√2", "x = 5, x = √2", "x = -5, x = -√2"], "idx": 1},
        {"q": "2x² - x + 1/8 = 0", "ans": "x = 1/4, x = 1/4", "opts": ["x = 1/8, x = 1", "x = -1/4, x = -1/4", "x = 1/4, x = 1/4", "x = 1/2, x = 1/2"], "idx": 2},
        {"q": "100x² - 20x + 1 = 0", "ans": "x = 1/10, x = 1/10", "opts": ["x = 1/10, x = 1/10", "x = -1/10, x = -1/10", "x = 1/5, x = 1/5", "x = 1/20, x = 1/20"], "idx": 0},
    ]

    for i, item in enumerate(factorisation_qs):
        blocks.append({
            "id": f"KOBJ_CLASS10_MATH_CH4_EX4_2_Q1_{i+1}",
            "type": "mcq",
            "question": f"Find the roots of the quadratic equation by factorisation: {item['q']}",
            "question_hi": f"गुणनखंडन द्वारा द्विघात समीकरण के मूल ज्ञात कीजिए: {item['q']}",
            "question_gu": f"અવયવીકરણ દ્વારા દ્વિઘાત સમીકરણના મૂળ શોધો: {item['q']}",
            "options": item['opts'],
            "options_hi": item['opts'],
            "options_gu": item['opts'],
            "correct_index": item['idx'],
            "explanation": "Use splitting the middle term to factorise and find the values of x.",
            "explanation_hi": "मध्य पद को विभक्त करके गुणनखंड करें और x के मान ज्ञात करें।",
            "explanation_gu": "મધ્યમ પદને વિભાજિત કરીને અવયવો પાડો અને x ના મૂલ્યો શોધો."
        })

    # Discriminant and Nature of roots (Ex 4.4 / 4.3 depending on syllabus)
    discriminant_qs = [
        {"q": "2x² - 3x + 5 = 0", "ans": "No real roots", "opts": ["Two distinct real roots", "Two equal real roots", "No real roots", "Cannot be determined"], "idx": 2},
        {"q": "3x² - 4√3x + 4 = 0", "ans": "Two equal real roots", "opts": ["Two distinct real roots", "Two equal real roots", "No real roots", "Cannot be determined"], "idx": 1},
        {"q": "2x² - 6x + 3 = 0", "ans": "Two distinct real roots", "opts": ["Two distinct real roots", "Two equal real roots", "No real roots", "Cannot be determined"], "idx": 0}
    ]

    opts_hi_disc = ["दो भिन्न वास्तविक मूल", "दो समान वास्तविक मूल", "कोई वास्तविक मूल नहीं", "निर्धारित नहीं किया जा सकता"]
    opts_gu_disc = ["બે ભિન્ન વાસ્તવિક મૂળ", "બે સમાન વાસ્તવિક મૂળ", "કોઈ વાસ્તવિક મૂળ નથી", "નક્કી કરી શકાતું નથી"]

    for i, item in enumerate(discriminant_qs):
        blocks.append({
            "id": f"KOBJ_CLASS10_MATH_CH4_NATURE_{i+1}",
            "type": "mcq",
            "question": f"Find the nature of the roots of the quadratic equation: {item['q']}",
            "question_hi": f"द्विघात समीकरण के मूलों की प्रकृति ज्ञात कीजिए: {item['q']}",
            "question_gu": f"દ્વિઘાત સમીકરણના મૂળની પ્રકૃતિ શોધો: {item['q']}",
            "options": item['opts'],
            "options_hi": opts_hi_disc,
            "options_gu": opts_gu_disc,
            "correct_index": item['idx'],
            "explanation": "Calculate the discriminant (b² - 4ac). If > 0, roots are distinct. If = 0, roots are equal. If < 0, no real roots.",
            "explanation_hi": "विविक्तकर (b² - 4ac) की गणना करें। यदि > 0, मूल भिन्न हैं। यदि = 0, मूल समान हैं। यदि < 0, कोई वास्तविक मूल नहीं।",
            "explanation_gu": "વિવેચક (b² - 4ac) ની ગણતરી કરો. જો > 0, મૂળ ભિન્ન છે. જો = 0, મૂળ સમાન છે. જો < 0, કોઈ વાસ્તવિક મૂળ નથી."
        })

    # Word problems
    blocks.append({
        "id": "KOBJ_CLASS10_MATH_CH4_WP_1",
        "type": "mcq",
        "question": "Find two numbers whose sum is 27 and product is 182.",
        "question_hi": "ऐसी दो संख्याएँ ज्ञात कीजिए जिनका योग 27 हो और गुणनफल 182 हो।",
        "question_gu": "બે એવી સંખ્યાઓ શોધો જેનો સરવાળો 27 હોય અને ગુણાકાર 182 હોય.",
        "options": ["12 and 15", "13 and 14", "10 and 17", "11 and 16"],
        "options_hi": ["12 और 15", "13 और 14", "10 और 17", "11 और 16"],
        "options_gu": ["12 અને 15", "13 અને 14", "10 અને 17", "11 અને 16"],
        "correct_index": 1,
        "explanation": "Let numbers be x and 27-x. Then x(27-x) = 182 => x² - 27x + 182 = 0. Roots are 13 and 14.",
        "explanation_hi": "माना संख्याएँ x और 27-x हैं। तब x(27-x) = 182 => x² - 27x + 182 = 0. मूल 13 और 14 हैं।",
        "explanation_gu": "ધારો કે સંખ્યાઓ x અને 27-x છે. તો x(27-x) = 182 => x² - 27x + 182 = 0. મૂળ 13 અને 14 છે."
    })

    blocks.append({
        "id": "KOBJ_CLASS10_MATH_CH4_WP_2",
        "type": "mcq",
        "question": "The altitude of a right triangle is 7 cm less than its base. If the hypotenuse is 13 cm, find the other two sides.",
        "question_hi": "एक समकोण त्रिभुज की ऊँचाई इसके आधार से 7 सेमी कम है। यदि कर्ण 13 सेमी का है, तो अन्य दो भुजाएँ ज्ञात कीजिए।",
        "question_gu": "કાટકોણ ત્રિકોણની ઊંચાઈ તેના પાયા કરતા 7 સેમી ઓછી છે. જો કર્ણ 13 સેમી હોય, તો અન્ય બે બાજુઓ શોધો.",
        "options": ["Base = 12cm, Altitude = 5cm", "Base = 10cm, Altitude = 3cm", "Base = 14cm, Altitude = 7cm", "Base = 15cm, Altitude = 8cm"],
        "options_hi": ["आधार = 12 सेमी, ऊँचाई = 5 सेमी", "आधार = 10 सेमी, ऊँचाई = 3 सेमी", "आधार = 14 सेमी, ऊँचाई = 7 सेमी", "आधार = 15 सेमी, ऊँचाई = 8 सेमी"],
        "options_gu": ["પાયો = 12 સેમી, ઊંચાઈ = 5 સેમી", "પાયો = 10 સેમી, ઊંચાઈ = 3 સેમી", "પાયો = 14 સેમી, ઊંચાઈ = 7 સેમી", "પાયો = 15 સેમી, ઊંચાઈ = 8 સેમી"],
        "correct_index": 0,
        "explanation": "Let base be x. Altitude = x - 7. By Pythagoras theorem, x² + (x - 7)² = 13². Solving gives x = 12. So altitude is 5.",
        "explanation_hi": "माना आधार x है। ऊँचाई = x - 7. पाइथागोरस प्रमेय द्वारा, x² + (x - 7)² = 13²। हल करने पर x = 12 मिलता है। इसलिए ऊँचाई 5 है।",
        "explanation_gu": "ધારો કે પાયો x છે. ઊંચાઈ = x - 7. પાયથાગોરસ પ્રમેય દ્વારા, x² + (x - 7)² = 13². ઉકેલતા x = 12 મળે છે. તેથી ઊંચાઈ 5 છે."
    })

    # Wrap up in final structure
    output = {
        "metadata": metadata,
        "blocks": blocks
    }

    with open('app_core/chapters/ncert_class10_maths_ch4.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print("Generated successfully!")

if __name__ == '__main__':
    main()
