import json
import os
import uuid

def create_mcq(q_en, q_hi, q_gu, opt_en, opt_hi, opt_gu, correct, exp_en, exp_hi, exp_gu):
    return {
        "type": "mcq",
        "id": f"KOBJ_CLASS10_MATH_CH2_EXTRA_{uuid.uuid4().hex[:8].upper()}",
        "question": q_en,
        "question_hi": q_hi,
        "question_gu": q_gu,
        "options": opt_en,
        "options_hi": opt_hi,
        "options_gu": opt_gu,
        "correct_index": correct,
        "explanation": exp_en,
        "explanation_hi": exp_hi,
        "explanation_gu": exp_gu
    }

mcqs = [
    create_mcq(
        "A quadratic polynomial, whose zeroes are -3 and 4, is",
        "एक द्विघात बहुपद, जिसके शून्यक -3 और 4 हैं, है",
        "એક દ્વિઘાત બહુપદી, જેના શૂન્યો -3 અને 4 છે, તે છે",
        ["x² - x + 12", "x² + x + 12", "x² - x - 12", "x² + x - 12"],
        ["x² - x + 12", "x² + x + 12", "x² - x - 12", "x² + x - 12"],
        ["x² - x + 12", "x² + x + 12", "x² - x - 12", "x² + x - 12"],
        2,
        "Sum of zeroes = -3 + 4 = 1. Product of zeroes = -3 * 4 = -12. Polynomial = x² - (Sum)x + Product = x² - x - 12.",
        "शून्यकों का योग = -3 + 4 = 1. शून्यकों का गुणनफल = -3 * 4 = -12. बहुपद = x² - (योग)x + गुणनफल = x² - x - 12.",
        "શૂન્યોનો સરવાળો = -3 + 4 = 1. શૂન્યોનો ગુણાકાર = -3 * 4 = -12. બહુપદી = x² - (સરવાળો)x + ગુણાકાર = x² - x - 12."
    ),
    create_mcq(
        "If the zeroes of the quadratic polynomial x² + (a + 1)x + b are 2 and -3, then",
        "यदि द्विघात बहुपद x² + (a + 1)x + b के शून्यक 2 और -3 हैं, तो",
        "જો દ્વિઘાત બહુપદી x² + (a + 1)x + b ના શૂન્યો 2 અને -3 હોય, તો",
        ["a = -7, b = -1", "a = 5, b = -1", "a = 2, b = -6", "a = 0, b = -6"],
        ["a = -7, b = -1", "a = 5, b = -1", "a = 2, b = -6", "a = 0, b = -6"],
        ["a = -7, b = -1", "a = 5, b = -1", "a = 2, b = -6", "a = 0, b = -6"],
        3,
        "Sum = -1. So -(a+1) = -1 => a=0. Product = -6. So b = -6.",
        "योग = -1. इसलिए -(a+1) = -1 => a=0. गुणनफल = -6. इसलिए b = -6.",
        "સરવાળો = -1. તેથી -(a+1) = -1 => a=0. ગુણાકાર = -6. તેથી b = -6."
    ),
    create_mcq(
        "The number of polynomials having zeroes as -2 and 5 is",
        "-2 और 5 को शून्यक के रूप में रखने वाले बहुपदों की संख्या है",
        "-2 અને 5 ને શૂન્યો તરીકે ધરાવતી બહુપદીઓની સંખ્યા છે",
        ["1", "2", "3", "More than 3"],
        ["1", "2", "3", "3 से अधिक"],
        ["1", "2", "3", "3 થી વધુ"],
        3,
        "There are infinitely many polynomials of the form k(x² - 3x - 10) where k is a real number.",
        "k(x² - 3x - 10) के रूप में अनंत रूप से कई बहुपद हैं जहाँ k एक वास्तविक संख्या है।",
        "k(x² - 3x - 10) ના રૂપમાં અસંખ્ય બહુપદીઓ છે જ્યાં k એક વાસ્તવિક સંખ્યા છે."
    ),
    create_mcq(
        "If one of the zeroes of the cubic polynomial x³ + ax² + bx + c is -1, then the product of the other two zeroes is",
        "यदि त्रिघात बहुपद x³ + ax² + bx + c का एक शून्यक -1 है, तो अन्य दो शून्यकों का गुणनफल है",
        "જો ત્રિઘાત બહુપદી x³ + ax² + bx + c નું એક શૂન્ય -1 હોય, તો અન્ય બે શૂન્યોનો ગુણાકાર છે",
        ["b - a + 1", "b - a - 1", "a - b + 1", "a - b - 1"],
        ["b - a + 1", "b - a - 1", "a - b + 1", "a - b - 1"],
        ["b - a + 1", "b - a - 1", "a - b + 1", "a - b - 1"],
        0,
        "Since -1 is a zero, f(-1) = 0 => -1 + a - b + c = 0 => c = 1 - a + b. Product of all zeroes = -c. So αβ(-1) = -c => αβ = c = 1 - a + b.",
        "चूँकि -1 एक शून्यक है, f(-1) = 0 => -1 + a - b + c = 0 => c = 1 - a + b. सभी शून्यकों का गुणनफल = -c. इसलिए αβ(-1) = -c => αβ = c = 1 - a + b.",
        "કારણ કે -1 એ શૂન્ય છે, f(-1) = 0 => -1 + a - b + c = 0 => c = 1 - a + b. બધા શૂન્યોનો ગુણાકાર = -c. તેથી αβ(-1) = -c => αβ = c = 1 - a + b."
    ),
    create_mcq(
        "The zeroes of the quadratic polynomial x² + 99x + 127 are",
        "द्विघात बहुपद x² + 99x + 127 के शून्यक हैं",
        "દ્વિઘાત બહુપદી x² + 99x + 127 ના શૂન્યો છે",
        ["both positive", "both negative", "one positive and one negative", "both equal"],
        ["दोनों धनात्मक", "दोनों ऋणात्मक", "एक धनात्मक और एक ऋणात्मक", "दोनों बराबर"],
        ["બંને ધનાત્મક", "બંને ઋણાત્મક", "એક ધનાત્મક અને એક ઋણાત્મક", "બંને સમાન"],
        1,
        "Since all coefficients (1, 99, 127) are positive, both zeroes must be negative.",
        "चूँकि सभी गुणांक (1, 99, 127) धनात्मक हैं, दोनों शून्यक ऋणात्मक होने चाहिए।",
        "કારણ કે બધા સહગુણકો (1, 99, 127) ધનાત્મક છે, બંને શૂન્યો ઋણાત્મક હોવા જોઈએ."
    ),
    create_mcq(
        "If the zeroes of the quadratic polynomial ax² + bx + c, c ≠ 0, are equal, then",
        "यदि द्विघात बहुपद ax² + bx + c, c ≠ 0 के शून्यक समान हैं, तो",
        "જો દ્વિઘાત બહુપદી ax² + bx + c, c ≠ 0 ના શૂન્યો સમાન હોય, તો",
        ["c and a have opposite signs", "c and b have opposite signs", "c and a have the same sign", "c and b have the same sign"],
        ["c और a के चिन्ह विपरीत हैं", "c और b के चिन्ह विपरीत हैं", "c और a के समान चिन्ह हैं", "c और b के समान चिन्ह हैं"],
        ["c અને a ના ચિન્હો વિરુદ્ધ છે", "c અને b ના ચિન્હો વિરુદ્ધ છે", "c અને a ના સમાન ચિન્હો છે", "c અને b ના સમાન ચિન્હો છે"],
        2,
        "For equal zeroes, discriminant b² - 4ac = 0 => b² = 4ac. Since b² is always positive, ac must be positive, which means a and c have the same sign.",
        "समान शून्यकों के लिए, विविक्तकर b² - 4ac = 0 => b² = 4ac. चूँकि b² हमेशा धनात्मक होता है, ac धनात्मक होना चाहिए, जिसका अर्थ है कि a और c के समान चिन्ह हैं।",
        "સમાન શૂન્યો માટે, વિવેચક b² - 4ac = 0 => b² = 4ac. કારણ કે b² હંમેશા ધનાત્મક હોય છે, ac ધનાત્મક હોવું જોઈએ, જેનો અર્થ છે કે a અને c સમાન ચિન્હો ધરાવે છે."
    ),
    create_mcq(
        "If one of the zeroes of a quadratic polynomial of the form x² + ax + b is the negative of the other, then it",
        "यदि x² + ax + b रूप के द्विघात बहुपद का एक शून्यक दूसरे का ऋणात्मक है, तो यह",
        "જો x² + ax + b ના રૂપના દ્વિઘાત બહુપદીનું એક શૂન્ય બીજાનું ઋણાત્મક હોય, તો તે",
        ["has no linear term and the constant term is negative", "has no linear term and the constant term is positive", "can have a linear term but the constant term is negative", "can have a linear term but the constant term is positive"],
        ["में कोई रैखिक पद नहीं है और अचर पद ऋणात्मक है", "में कोई रैखिक पद नहीं है और अचर पद धनात्मक है", "में रैखिक पद हो सकता है लेकिन अचर पद ऋणात्मक है", "में रैखिक पद हो सकता है लेकिन अचर पद धनात्मक है"],
        ["માં કોઈ રેખીય પદ નથી અને અચળ પદ ઋણાત્મક છે", "માં કોઈ રેખીય પદ નથી અને અચળ પદ ધનાત્મક છે", "માં રેખીય પદ હોઈ શકે છે પરંતુ અચળ પદ ઋણાત્મક છે", "માં રેખીય પદ હોઈ શકે છે પરંતુ અચળ પદ ધનાત્મક છે"],
        0,
        "If zeroes are α and -α, sum = 0 => -a/1 = 0 => a = 0. Product = -α² = b. Since α² is positive, b must be negative.",
        "यदि शून्यक α और -α हैं, योग = 0 => -a/1 = 0 => a = 0. गुणनफल = -α² = b. चूँकि α² धनात्मक है, b ऋणात्मक होना चाहिए।",
        "જો શૂન્યો α અને -α હોય, સરવાળો = 0 => -a/1 = 0 => a = 0. ગુણાકાર = -α² = b. કારણ કે α² ધનાત્મક છે, b ઋણાત્મક હોવું જોઈએ."
    ),
    create_mcq(
        "Which of the following is not the graph of a quadratic polynomial?",
        "निम्नलिखित में से कौन सा द्विघात बहुपद का ग्राफ नहीं है?",
        "નીચેનામાંથી કયો દ્વિઘાત બહુપદીનો આલેખ નથી?",
        ["A parabola opening upwards", "A parabola opening downwards", "A straight line", "A U-shaped curve intersecting x-axis twice"],
        ["ऊपर की ओर खुलने वाला परवलय", "नीचे की ओर खुलने वाला परवलय", "एक सीधी रेखा", "दो बार x-अक्ष को काटने वाला U-आकार का वक्र"],
        ["ઉપરની તરફ ખુલતો પરવલય", "નીચેની તરફ ખુલતો પરવલય", "એક સીધી રેખા", "બે વાર x-અક્ષને છેદતો U-આકારનો વક્ર"],
        2,
        "A quadratic polynomial's graph is always a parabola, never a straight line.",
        "एक द्विघात बहुपद का ग्राफ हमेशा एक परवलय होता है, कभी भी सीधी रेखा नहीं।",
        "દ્વિઘાત બહુપદીનો આલેખ હંમેશા પરવલય હોય છે, ક્યારેય સીધી રેખા નથી."
    ),
    create_mcq(
        "The maximum number of zeroes that a polynomial of degree 3 can have is",
        "घात 3 वाले बहुपद के शून्यकों की अधिकतम संख्या हो सकती है",
        "ઘાત 3 વાળી બહુપદીના શૂન્યોની મહત્તમ સંખ્યા હોઈ શકે છે",
        ["1", "2", "3", "4"],
        ["1", "2", "3", "4"],
        ["1", "2", "3", "4"],
        2,
        "A polynomial of degree n can have at most n zeroes.",
        "घात n वाले बहुपद के अधिकतम n शून्यक हो सकते हैं।",
        "ઘાત n વાળી બહુપદીમાં વધુમાં વધુ n શૂન્યો હોઈ શકે છે."
    ),
    create_mcq(
        "If α, β are the zeroes of the polynomial f(x) = x² + x + 1, then 1/α + 1/β =",
        "यदि α, β बहुपद f(x) = x² + x + 1 के शून्यक हैं, तो 1/α + 1/β =",
        "જો α, β એ બહુપદી f(x) = x² + x + 1 ના શૂન્યો હોય, તો 1/α + 1/β =",
        ["1", "-1", "0", "None of these"],
        ["1", "-1", "0", "इनमें से कोई नहीं"],
        ["1", "-1", "0", "આમાંથી કોઈ નહિ"],
        1,
        "1/α + 1/β = (α+β)/(αβ). Here α+β = -1 and αβ = 1. So -1/1 = -1.",
        "1/α + 1/β = (α+β)/(αβ). यहाँ α+β = -1 और αβ = 1. इसलिए -1/1 = -1.",
        "1/α + 1/β = (α+β)/(αβ). અહી α+β = -1 અને αβ = 1. તેથી -1/1 = -1."
    ),
    create_mcq(
        "If α, β are the zeroes of the polynomial p(x) = 4x² + 3x + 7, then 1/α + 1/β is equal to",
        "यदि α, β बहुपद p(x) = 4x² + 3x + 7 के शून्यक हैं, तो 1/α + 1/β बराबर है",
        "જો α, β એ બહુપદી p(x) = 4x² + 3x + 7 ના શૂન્યો હોય, તો 1/α + 1/β બરાબર છે",
        ["7/3", "-7/3", "3/7", "-3/7"],
        ["7/3", "-7/3", "3/7", "-3/7"],
        ["7/3", "-7/3", "3/7", "-3/7"],
        3,
        "1/α + 1/β = (α+β)/(αβ). α+β = -3/4, αβ = 7/4. (-3/4) / (7/4) = -3/7.",
        "1/α + 1/β = (α+β)/(αβ). α+β = -3/4, αβ = 7/4. (-3/4) / (7/4) = -3/7.",
        "1/α + 1/β = (α+β)/(αβ). α+β = -3/4, αβ = 7/4. (-3/4) / (7/4) = -3/7."
    ),
    create_mcq(
        "If one zero of the polynomial f(x) = (k² + 4)x² + 13x + 4k is reciprocal of the other, then k =",
        "यदि बहुपद f(x) = (k² + 4)x² + 13x + 4k का एक शून्यक दूसरे का व्युत्क्रम है, तो k =",
        "જો બહુપદી f(x) = (k² + 4)x² + 13x + 4k નું એક શૂન્ય બીજાનું વ્યસ્ત હોય, તો k =",
        ["2", "-2", "1", "-1"],
        ["2", "-2", "1", "-1"],
        ["2", "-2", "1", "-1"],
        0,
        "Let zeroes be α and 1/α. Product = 1. c/a = 1 => 4k / (k² + 4) = 1 => k² - 4k + 4 = 0 => (k-2)² = 0 => k=2.",
        "मान लीजिए शून्यक α और 1/α हैं। गुणनफल = 1. c/a = 1 => 4k / (k² + 4) = 1 => k² - 4k + 4 = 0 => (k-2)² = 0 => k=2.",
        "ધારો કે શૂન્યો α અને 1/α છે. ગુણાકાર = 1. c/a = 1 => 4k / (k² + 4) = 1 => k² - 4k + 4 = 0 => (k-2)² = 0 => k=2."
    ),
    create_mcq(
        "If the sum of the zeroes of the polynomial p(x) = (k² - 14)x² - 2x - 12 is 1, then k =",
        "यदि बहुपद p(x) = (k² - 14)x² - 2x - 12 के शून्यकों का योग 1 है, तो k =",
        "જો બહુપદી p(x) = (k² - 14)x² - 2x - 12 ના શૂન્યોનો સરવાળો 1 હોય, તો k =",
        ["√14", "-√14", "4", "Both 4 and -4"],
        ["√14", "-√14", "4", "4 और -4 दोनों"],
        ["√14", "-√14", "4", "4 અને -4 બંને"],
        3,
        "Sum = -b/a = -(-2) / (k² - 14) = 2 / (k² - 14). We are given sum = 1. So 2 = k² - 14 => k² = 16 => k = ±4.",
        "योग = -b/a = -(-2) / (k² - 14) = 2 / (k² - 14). दिया गया है योग = 1. इसलिए 2 = k² - 14 => k² = 16 => k = ±4.",
        "સરવાળો = -b/a = -(-2) / (k² - 14) = 2 / (k² - 14). આપેલ છે સરવાળો = 1. તેથી 2 = k² - 14 => k² = 16 => k = ±4."
    ),
    create_mcq(
        "If α, β are the zeroes of a polynomial such that α + β = -6 and αβ = 5, then find the polynomial.",
        "यदि α, β एक बहुपद के ऐसे शून्यक हैं कि α + β = -6 और αβ = 5, तो बहुपद ज्ञात कीजिए।",
        "જો α, β એ બહુપદીના એવા શૂન્યો હોય કે જેથી α + β = -6 અને αβ = 5, તો બહુપદી શોધો.",
        ["x² + 6x + 5", "x² - 6x + 5", "x² + 6x - 5", "x² - 6x - 5"],
        ["x² + 6x + 5", "x² - 6x + 5", "x² + 6x - 5", "x² - 6x - 5"],
        ["x² + 6x + 5", "x² - 6x + 5", "x² + 6x - 5", "x² - 6x - 5"],
        0,
        "Polynomial is x² - (Sum)x + Product = x² - (-6)x + 5 = x² + 6x + 5.",
        "बहुपद है x² - (योग)x + गुणनफल = x² - (-6)x + 5 = x² + 6x + 5.",
        "બહુપદી છે x² - (સરવાળો)x + ગુણાકાર = x² - (-6)x + 5 = x² + 6x + 5."
    ),
    create_mcq(
        "Find the condition that zeroes of polynomial p(x) = ax² + bx + c are reciprocal of each other.",
        "शर्त ज्ञात कीजिए कि बहुपद p(x) = ax² + bx + c के शून्यक एक दूसरे के व्युत्क्रम हैं।",
        "શરત શોધો કે બહુપદી p(x) = ax² + bx + c ના શૂન્યો એકબીજાના વ્યસ્ત હોય.",
        ["a = b", "b = c", "a = c", "a = b = c"],
        ["a = b", "b = c", "a = c", "a = b = c"],
        ["a = b", "b = c", "a = c", "a = b = c"],
        2,
        "If zeroes are reciprocal, product = 1. So c/a = 1 => c = a.",
        "यदि शून्यक व्युत्क्रम हैं, गुणनफल = 1. इसलिए c/a = 1 => c = a.",
        "જો શૂન્યો વ્યસ્ત હોય, ગુણાકાર = 1. તેથી c/a = 1 => c = a."
    )
]

file_path = "app_core/chapters/ncert_class10_maths_ch2.json"
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Find the index of the last MCQ to insert after it, or just append at the end
data['blocks'].extend(mcqs)

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(mcqs)} new MCQs to Chapter 2.")
