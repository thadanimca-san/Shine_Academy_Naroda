import json
import os

chapter_id = "gseb_class10_maths_ch2"
output_file = f"/home/ubuntu/Shine_Academy_Naroda/app_core/assessment/{chapter_id}_questions.json"
os.makedirs(os.path.dirname(output_file), exist_ok=True)

questions = []

def add_q(qid, q_en, q_hi, options_en, options_hi, correct_idx, exp_en, exp_hi, distractor_en, distractor_hi, hint_en, hint_hi, diff="Beginner"):
    questions.append({
        "id": f"Q_{chapter_id}_{qid}",
        "chapter_id": chapter_id,
        "topic_id": f"KOBJ_{chapter_id}_PRACTICE",
        "type": "mcq",
        "difficulty": diff,
        "board": ["GSEB", "CBSE"],
        "marks": 1,
        "bloom_taxonomy": "Applying",
        "question_text": {"english": q_en, "hindi": q_hi},
        "options": [{"english": options_en[i], "hindi": options_hi[i]} for i in range(len(options_en))],
        "correct_index": correct_idx,
        "explanation": {"english": exp_en, "hindi": exp_hi},
        "distractor_rationale": {"english": distractor_en, "hindi": distractor_hi},
        "ai_context": {"hint": hint_en, "hint_hi": hint_hi}
    })

# --- Question 1-25 (Polynomials) ---
add_q("001", "The number of zeroes of the polynomial p(x) whose graph intersects the x-axis at 3 distinct points is:", "उस बहुपद p(x) के शून्यकों की संख्या कितनी होगी जिसका ग्राफ x-अक्ष को 3 अलग-अलग बिंदुओं पर काटता है?", ["1", "2", "3", "0"], ["1", "2", "3", "0"], 2, "The number of zeroes of a polynomial is equal to the number of points where its graph intersects the x-axis.", "एक बहुपद के शून्यकों की संख्या उन बिंदुओं की संख्या के बराबर होती है जहाँ इसका ग्राफ x-अक्ष को काटता है।", "You only count the x-axis intersections, not y-axis.", "आप केवल x-अक्ष के प्रतिच्छेदन को गिनते हैं, y-अक्ष को नहीं।", "Look at where the line crosses the horizontal axis.", "देखें कि रेखा क्षैतिज अक्ष को कहाँ पार करती है।")

add_q("002", "If α and β are the zeroes of the quadratic polynomial f(x) = x² - 5x + 6, find the value of α + β.", "यदि α और β द्विघात बहुपद f(x) = x² - 5x + 6 के शून्यक हैं, तो α + β का मान ज्ञात कीजिए।", ["-5", "5", "6", "-6"], ["-5", "5", "6", "-6"], 1, "Sum of zeroes (α + β) = -b/a. Here a=1, b=-5. So, -(-5)/1 = 5.", "शून्यकों का योग (α + β) = -b/a। यहाँ a=1, b=-5। तो, -(-5)/1 = 5।", "Don't confuse sum with product (c/a).", "योग को गुणनफल (c/a) के साथ भ्रमित न करें।", "What is the formula for sum of zeroes?", "शून्यकों के योग का सूत्र क्या है?")

add_q("003", "For the same polynomial f(x) = x² - 5x + 6, what is the product of its zeroes (αβ)?", "उसी बहुपद f(x) = x² - 5x + 6 के लिए, इसके शून्यकों का गुणनफल (αβ) क्या है?", ["5", "-5", "6", "-6"], ["5", "-5", "6", "-6"], 2, "Product of zeroes (αβ) = c/a. Here a=1, c=6. So, 6/1 = 6.", "शून्यकों का गुणनफल (αβ) = c/a। यहाँ a=1, c=6। तो, 6/1 = 6।", "Product is c/a, not -b/a.", "गुणनफल c/a है, -b/a नहीं।", "Use the formula c/a.", "सूत्र c/a का प्रयोग करें।")

add_q("004", "Find a quadratic polynomial whose zeroes are 4 and -2.", "एक द्विघात बहुपद ज्ञात कीजिए जिसके शून्यक 4 और -2 हैं।", ["x² - 2x - 8", "x² + 2x - 8", "x² - 2x + 8", "x² + 2x + 8"], ["x² - 2x - 8", "x² + 2x - 8", "x² - 2x + 8", "x² + 2x + 8"], 0, "Sum = 4 + (-2) = 2. Product = 4 × (-2) = -8. Polynomial is x² - (Sum)x + Product = x² - 2x - 8.", "योग = 4 + (-2) = 2। गुणनफल = 4 × (-2) = -8। बहुपद है x² - (योग)x + गुणनफल = x² - 2x - 8।", "Watch out for the minus sign in the formula x² - (Sum)x + Product.", "सूत्र x² - (योग)x + गुणनफल में ऋणात्मक चिह्न का ध्यान रखें।", "First find α+β and αβ.", "पहले α+β और αβ ज्ञात करें।")

add_q("005", "If one zero of the polynomial (k-1)x² + kx + 1 is -3, then the value of k is:", "यदि बहुपद (k-1)x² + kx + 1 का एक शून्यक -3 है, तो k का मान है:", ["4/3", "-4/3", "2/3", "-2/3"], ["4/3", "-4/3", "2/3", "-2/3"], 0, "Substitute x = -3 into the polynomial and set it to 0. (k-1)(-3)² + k(-3) + 1 = 0 => 9(k-1) - 3k + 1 = 0 => 9k - 9 - 3k + 1 = 0 => 6k - 8 = 0 => k = 8/6 = 4/3.", "बहुपद में x = -3 रखें और इसे 0 के बराबर करें। (k-1)(-3)² + k(-3) + 1 = 0 => 9(k-1) - 3k + 1 = 0 => 9k - 9 - 3k + 1 = 0 => 6k - 8 = 0 => k = 8/6 = 4/3।", "Make sure you square the negative correctly.", "सुनिश्चित करें कि आप ऋणात्मक संख्या का वर्ग सही ढंग से करते हैं।", "Since -3 is a zero, p(-3) must be 0.", "चूँकि -3 एक शून्यक है, p(-3) शून्य होना चाहिए।")

add_q("006", "The zeroes of the quadratic polynomial x² + 99x + 127 are:", "द्विघात बहुपद x² + 99x + 127 के शून्यक हैं:", ["both positive", "both negative", "one positive and one negative", "both equal"], ["दोनों धनात्मक", "दोनों ऋणात्मक", "एक धनात्मक और एक ऋणात्मक", "दोनों समान"], 1, "In x² + bx + c, if both b and c are positive, both zeroes are negative.", "x² + bx + c में, यदि b और c दोनों धनात्मक हैं, तो दोनों शून्यक ऋणात्मक होते हैं।", "Think about the sum and product rules.", "योग और गुणनफल के नियमों के बारे में सोचें।", "If sum is negative and product is positive, what signs must the numbers have?", "यदि योग ऋणात्मक है और गुणनफल धनात्मक है, तो संख्याओं के चिह्न क्या होने चाहिए?", "Advanced")

add_q("007", "If the zeroes of the quadratic polynomial ax² + bx + c, c ≠ 0 are equal, then:", "यदि द्विघात बहुपद ax² + bx + c, c ≠ 0 के शून्यक समान हैं, तो:", ["c and a have opposite signs", "c and b have opposite signs", "c and a have the same sign", "c and b have the same sign"], ["c और a के चिह्न विपरीत हैं", "c और b के चिह्न विपरीत हैं", "c और a के चिह्न समान हैं", "c और b के चिह्न समान हैं"], 2, "For equal zeroes, discriminant D = b² - 4ac = 0 => b² = 4ac. Since b² is always positive, 4ac must be positive, meaning a and c must have the same sign.", "समान शून्यकों के लिए, विविक्तकर D = b² - 4ac = 0 => b² = 4ac। चूँकि b² हमेशा धनात्मक होता है, 4ac धनात्मक होना चाहिए, जिसका अर्थ है a और c के चिह्न समान होने चाहिए।", "Squares cannot be negative.", "वर्ग ऋणात्मक नहीं हो सकते।", "Think about the condition b² - 4ac = 0.", "b² - 4ac = 0 शर्त के बारे में सोचें।", "Advanced")

add_q("008", "If one of the zeroes of a quadratic polynomial of the form x² + ax + b is the negative of the other, then it:", "यदि x² + ax + b रूप के द्विघात बहुपद के शून्यकों में से एक दूसरे का ऋणात्मक है, तो यह:", ["has no linear term and the constant term is negative.", "has no linear term and the constant term is positive.", "can have a linear term but the constant term is negative.", "can have a linear term but the constant term is positive."], ["कोई रैखिक पद नहीं है और अचर पद ऋणात्मक है।", "कोई रैखिक पद नहीं है और अचर पद धनात्मक है।", "एक रैखिक पद हो सकता है लेकिन अचर पद ऋणात्मक है।", "एक रैखिक पद हो सकता है लेकिन अचर पद धनात्मक है।"], 0, "If zeroes are α and -α, sum = 0 => -a/1 = 0 => a = 0 (no linear term). Product = -α² = b. Since -α² is negative, b must be negative.", "यदि शून्यक α और -α हैं, योग = 0 => -a/1 = 0 => a = 0 (कोई रैखिक पद नहीं)। गुणनफल = -α² = b। चूँकि -α² ऋणात्मक है, b ऋणात्मक होना चाहिए।", "A perfect square difference creates this situation.", "एक पूर्ण वर्ग अंतर यह स्थिति बनाता है।", "What is the sum of a number and its negative?", "एक संख्या और उसके ऋणात्मक का योग क्या होता है?", "Advanced")

add_q("009", "If α and β are the zeroes of the polynomial f(x) = 2x² + 5x + 1, then the value of α + β + αβ is:", "यदि α और β बहुपद f(x) = 2x² + 5x + 1 के शून्यक हैं, तो α + β + αβ का मान है:", ["-2", "-3", "2", "3"], ["-2", "-3", "2", "3"], 0, "α + β = -5/2. αβ = 1/2. Summing them: -5/2 + 1/2 = -4/2 = -2.", "α + β = -5/2। αβ = 1/2। उन्हें जोड़ने पर: -5/2 + 1/2 = -4/2 = -2।", "Calculate sum and product separately and add them.", "योग और गुणनफल की अलग-अलग गणना करें और उन्हें जोड़ें।", "Find α+β and αβ first.", "पहले α+β और αβ ज्ञात करें।")

add_q("010", "Which of the following is not a polynomial?", "निम्नलिखित में से कौन सा बहुपद नहीं है?", ["x² + 2x + 1", "3x³ - 5", "x + 1/x", "2x - 3"], ["x² + 2x + 1", "3x³ - 5", "x + 1/x", "2x - 3"], 2, "In x + 1/x, the term 1/x is x⁻¹. A polynomial cannot have negative exponents for variables.", "x + 1/x में, पद 1/x, x⁻¹ है। एक बहुपद में चरों के लिए ऋणात्मक घातांक नहीं हो सकते।", "Check the powers of x.", "x की घातों की जाँच करें।", "What is the rule for exponents in polynomials?", "बहुपदों में घातांकों का क्या नियम है?")

add_q("011", "If the product of the zeroes of the polynomial ax² - 6x - 6 is 4, find the value of a.", "यदि बहुपद ax² - 6x - 6 के शून्यकों का गुणनफल 4 है, तो a का मान ज्ञात कीजिए।", ["-3/2", "3/2", "-2/3", "2/3"], ["-3/2", "3/2", "-2/3", "2/3"], 0, "Product of zeroes = c/a => -6/a = 4 => a = -6/4 = -3/2.", "शून्यकों का गुणनफल = c/a => -6/a = 4 => a = -6/4 = -3/2।", "Apply the formula for the product of zeroes.", "शून्यकों के गुणनफल के सूत्र का प्रयोग करें।", "c/a = 4", "c/a = 4")

add_q("012", "Find a quadratic polynomial whose zeroes are -3 and 2.", "एक द्विघात बहुपद ज्ञात कीजिए जिसके शून्यक -3 और 2 हैं।", ["x² + x - 6", "x² - x - 6", "x² + x + 6", "x² - x + 6"], ["x² + x - 6", "x² - x - 6", "x² + x + 6", "x² - x + 6"], 0, "Sum = -3 + 2 = -1. Product = -3 × 2 = -6. Polynomial: x² - (-1)x + (-6) = x² + x - 6.", "योग = -3 + 2 = -1। गुणनफल = -3 × 2 = -6। बहुपद: x² - (-1)x + (-6) = x² + x - 6।", "Careful with the negative signs.", "ऋणात्मक चिह्नों से सावधान रहें।", "x² - (Sum)x + Product", "x² - (Sum)x + Product")

add_q("013", "The degree of the polynomial 4x⁴ + 0x³ + 0x⁵ + 5x + 7 is:", "बहुपद 4x⁴ + 0x³ + 0x⁵ + 5x + 7 की घात है:", ["4", "5", "3", "7"], ["4", "5", "3", "7"], 0, "The highest power with a non-zero coefficient is 4. The 0x⁵ term evaluates to 0.", "गैर-शून्य गुणांक वाली सबसे बड़ी घात 4 है। 0x⁵ पद का मान 0 है।", "0 times anything is 0.", "0 का किसी भी चीज़ से गुणा करने पर 0 होता है।", "Look for the highest power of x that actually exists.", "x की उस सबसे बड़ी घात की तलाश करें जो वास्तव में मौजूद है।")

add_q("014", "If α and β are the zeroes of the polynomial x² - p(x + 1) - c, then (α + 1)(β + 1) is equal to:", "यदि α और β बहुपद x² - p(x + 1) - c के शून्यक हैं, तो (α + 1)(β + 1) बराबर है:", ["c - 1", "1 - c", "c", "1 + c"], ["c - 1", "1 - c", "c", "1 + c"], 1, "Rewrite as x² - px - (p+c). α+β = p, αβ = -(p+c). Expand (α+1)(β+1) = αβ + α + β + 1 = -(p+c) + p + 1 = 1 - c.", "इसे x² - px - (p+c) के रूप में फिर से लिखें। α+β = p, αβ = -(p+c)। विस्तार करें (α+1)(β+1) = αβ + α + β + 1 = -(p+c) + p + 1 = 1 - c।", "Don't forget to expand the polynomial first.", "पहले बहुपद का विस्तार करना न भूलें।", "Expand the brackets and substitute sum and product.", "कोष्ठकों का विस्तार करें और योग और गुणनफल को प्रतिस्थापित करें।", "Advanced")

add_q("015", "If the zeroes of the polynomial x² + px + q are double in value to the zeroes of 2x² - 5x - 3, find the value of p and q.", "यदि बहुपद x² + px + q के शून्यक 2x² - 5x - 3 के शून्यकों के मान में दोगुने हैं, तो p और q का मान ज्ञात कीजिए।", ["p = -5, q = -6", "p = 5, q = -6", "p = -5, q = 6", "p = 5, q = 6"], ["p = -5, q = -6", "p = 5, q = -6", "p = -5, q = 6", "p = 5, q = 6"], 0, "Zeroes of 2x²-5x-3 are 3 and -1/2. Double them: 6 and -1. Sum = 5, Prod = -6. Polynomial x² - 5x - 6. So p = -5, q = -6.", "2x²-5x-3 के शून्यक 3 और -1/2 हैं। उन्हें दोगुना करें: 6 और -1। योग = 5, गुणनफल = -6। बहुपद x² - 5x - 6। इसलिए p = -5, q = -6।", "Find the original zeroes first, then double them.", "पहले मूल शून्यकों को खोजें, फिर उन्हें दोगुना करें।", "What are the roots of the first equation?", "पहले समीकरण के मूल क्या हैं?", "Advanced")

add_q("016", "A quadratic polynomial whose zeroes are 0 and √5 is:", "एक द्विघात बहुपद जिसके शून्यक 0 और √5 हैं:", ["x² - √5", "x² - 5x", "x² - √5x", "x² + √5"], ["x² - √5", "x² - 5x", "x² - √5x", "x² + √5"], 2, "Sum = 0 + √5 = √5. Product = 0. Polynomial = x² - √5x + 0 = x² - √5x.", "योग = 0 + √5 = √5। गुणनफल = 0। बहुपद = x² - √5x + 0 = x² - √5x।", "Product is zero because one root is zero.", "गुणनफल शून्य है क्योंकि एक मूल शून्य है।", "Use the x² - (Sum)x + Product formula.", "x² - (Sum)x + Product सूत्र का उपयोग करें।")

add_q("017", "If α, β are the zeroes of f(x) = ax² + bx + c, then 1/α + 1/β is:", "यदि α, β f(x) = ax² + bx + c के शून्यक हैं, तो 1/α + 1/β है:", ["-b/c", "b/c", "-b/a", "c/a"], ["-b/c", "b/c", "-b/a", "c/a"], 0, "1/α + 1/β = (α + β) / (αβ) = (-b/a) / (c/a) = -b/c.", "1/α + 1/β = (α + β) / (αβ) = (-b/a) / (c/a) = -b/c।", "Take LCM of 1/α + 1/β.", "1/α + 1/β का LCM लें।", "What is (α + β) / αβ ?", "(α + β) / αβ क्या है?")

add_q("018", "The graph of a quadratic polynomial is a:", "द्विघात बहुपद का ग्राफ एक होता है:", ["Straight line", "Circle", "Parabola", "Ellipse"], ["सीधी रेखा", "वृत्त", "परवलय (Parabola)", "अंडाकार"], 2, "A quadratic polynomial always forms a U-shaped curve called a parabola.", "एक द्विघात बहुपद हमेशा परवलय (Parabola) नामक यू-आकार का वक्र बनाता है।", "Straight lines are for linear equations.", "सीधी रेखाएँ रैखिक समीकरणों के लिए होती हैं।", "Think of the U-shape curve.", "यू-आकार के वक्र के बारे में सोचें।")

add_q("019", "If one zero of 2x² - 3x + k is reciprocal to the other, then the value of k is:", "यदि 2x² - 3x + k का एक शून्यक दूसरे का व्युत्क्रम (reciprocal) है, तो k का मान है:", ["2", "-2", "3", "-3"], ["2", "-2", "3", "-3"], 0, "If zeroes are α and 1/α, their product is 1. Product formula is c/a => k/2 = 1 => k = 2.", "यदि शून्यक α और 1/α हैं, तो उनका गुणनफल 1 है। गुणनफल सूत्र है c/a => k/2 = 1 => k = 2।", "What happens when you multiply a number by its reciprocal?", "जब आप किसी संख्या को उसके व्युत्क्रम से गुणा करते हैं तो क्या होता है?", "Set the product of zeroes to 1.", "शून्यकों के गुणनफल को 1 के बराबर करें।")

add_q("020", "What is the maximum number of zeroes a cubic polynomial can have?", "एक त्रिघात बहुपद (cubic polynomial) के अधिकतम कितने शून्यक हो सकते हैं?", ["1", "2", "3", "4"], ["1", "2", "3", "4"], 2, "A polynomial of degree 'n' can have at most 'n' zeroes. A cubic polynomial has degree 3.", "घात 'n' वाले बहुपद के अधिकतम 'n' शून्यक हो सकते हैं। त्रिघात बहुपद की घात 3 होती है।", "Degree determines the maximum zeroes.", "घात अधिकतम शून्यकों को निर्धारित करती है।", "What is the highest power in a cubic polynomial?", "त्रिघात बहुपद में सबसे बड़ी घात क्या होती है?")

# --- End of Generation ---

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(questions, f, indent=2, ensure_ascii=False)
