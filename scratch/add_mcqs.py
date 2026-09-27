import json
import os
import shutil

# Existing file path
file_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/cbse_class10_maths_ch4.json"
gseb_file_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_maths_ch4.json"

with open(file_path, "r", encoding="utf-8") as f:
    blocks = json.load(f)

# Define 10 new MCQs
new_mcqs = [
    {
        "id": "KOBJ_CLASS10_MATH_CH4_101_MCQ",
        "type": "mcq",
        "question": "Which of the following is a quadratic equation?",
        "question_hi": "निम्नलिखित में से कौन सा एक द्विघात समीकरण है?",
        "options": [
            "x² + 2x + 1 = (4 - x)² + 3",
            "-2x² = (5 - x)(2x - 2/5)",
            "(k + 1)x² + (3/2)x = 7, where k = -1",
            "x³ - x² = (x - 1)³"
        ],
        "options_hi": [
            "x² + 2x + 1 = (4 - x)² + 3",
            "-2x² = (5 - x)(2x - 2/5)",
            "(k + 1)x² + (3/2)x = 7, जहाँ k = -1",
            "x³ - x² = (x - 1)³"
        ],
        "correct_index": 3,
        "explanation": "Expanding x³ - x² = (x - 1)³, we get x³ - x² = x³ - 3x² + 3x - 1. Simplifying gives 2x² - 3x + 1 = 0, which is a quadratic equation.",
        "explanation_hi": "x³ - x² = (x - 1)³ का विस्तार करने पर, हमें x³ - x² = x³ - 3x² + 3x - 1 प्राप्त होता है। सरल करने पर 2x² - 3x + 1 = 0 मिलता है, जो एक द्विघात समीकरण है।"
    },
    {
        "id": "KOBJ_CLASS10_MATH_CH4_102_MCQ",
        "type": "mcq",
        "question": "If 1/2 is a root of the equation x² + kx - 5/4 = 0, then the value of k is:",
        "question_hi": "यदि 1/2 समीकरण x² + kx - 5/4 = 0 का एक मूल है, तो k का मान है:",
        "options": [
            "2",
            "-2",
            "1/4",
            "1/2"
        ],
        "options_hi": [
            "2",
            "-2",
            "1/4",
            "1/2"
        ],
        "correct_index": 0,
        "explanation": "Substitute x = 1/2 in the equation: (1/2)² + k(1/2) - 5/4 = 0 ⇒ 1/4 + k/2 - 5/4 = 0 ⇒ k/2 - 4/4 = 0 ⇒ k/2 - 1 = 0 ⇒ k = 2.",
        "explanation_hi": "समीकरण में x = 1/2 रखें: (1/2)² + k(1/2) - 5/4 = 0 ⇒ 1/4 + k/2 - 5/4 = 0 ⇒ k/2 - 4/4 = 0 ⇒ k/2 - 1 = 0 ⇒ k = 2।"
    },
    {
        "id": "KOBJ_CLASS10_MATH_CH4_103_MCQ",
        "type": "mcq",
        "question": "The quadratic equation 2x² - √5x + 1 = 0 has:",
        "question_hi": "द्विघात समीकरण 2x² - √5x + 1 = 0 के हैं:",
        "options": [
            "Two distinct real roots",
            "Two equal real roots",
            "No real roots",
            "More than 2 real roots"
        ],
        "options_hi": [
            "दो भिन्न वास्तविक मूल",
            "दो समान वास्तविक मूल",
            "कोई वास्तविक मूल नहीं",
            "2 से अधिक वास्तविक मूल"
        ],
        "correct_index": 2,
        "explanation": "Calculate discriminant D = b² - 4ac = (-√5)² - 4(2)(1) = 5 - 8 = -3. Since D < 0, the equation has no real roots.",
        "explanation_hi": "विविक्तकर (Discriminant) D = b² - 4ac = (-√5)² - 4(2)(1) = 5 - 8 = -3 की गणना करें। चूँकि D < 0, समीकरण का कोई वास्तविक मूल नहीं है।"
    },
    {
        "id": "KOBJ_CLASS10_MATH_CH4_104_MCQ",
        "type": "mcq",
        "question": "What is the maximum number of roots a quadratic equation can have?",
        "question_hi": "एक द्विघात समीकरण के अधिकतम कितने मूल हो सकते हैं?",
        "options": [
            "1",
            "2",
            "3",
            "Infinite"
        ],
        "options_hi": [
            "1",
            "2",
            "3",
            "अनंत"
        ],
        "correct_index": 1,
        "explanation": "A quadratic equation (degree 2) can have at most two roots. They can be distinct, equal, or complex.",
        "explanation_hi": "एक द्विघात समीकरण (घात 2) के अधिकतम दो मूल हो सकते हैं। वे भिन्न, समान या सम्मिश्र (complex) हो सकते हैं।"
    },
    {
        "id": "KOBJ_CLASS10_MATH_CH4_105_MCQ",
        "type": "mcq",
        "question": "Which of the following equations has 2 as a root?",
        "question_hi": "निम्नलिखित में से किस समीकरण का एक मूल 2 है?",
        "options": [
            "x² - 4x + 5 = 0",
            "x² + 3x - 12 = 0",
            "2x² - 7x + 6 = 0",
            "3x² - 6x - 2 = 0"
        ],
        "options_hi": [
            "x² - 4x + 5 = 0",
            "x² + 3x - 12 = 0",
            "2x² - 7x + 6 = 0",
            "3x² - 6x - 2 = 0"
        ],
        "correct_index": 2,
        "explanation": "Substitute x = 2 in 2x² - 7x + 6 = 0: 2(2)² - 7(2) + 6 = 2(4) - 14 + 6 = 8 - 14 + 6 = 0. Since it satisfies the equation, 2 is a root.",
        "explanation_hi": "2x² - 7x + 6 = 0 में x = 2 रखें: 2(2)² - 7(2) + 6 = 2(4) - 14 + 6 = 8 - 14 + 6 = 0. क्योंकि यह समीकरण को संतुष्ट करता है, 2 एक मूल है।"
    },
    {
        "id": "KOBJ_CLASS10_MATH_CH4_106_MCQ",
        "type": "mcq",
        "question": "Values of k for which the quadratic equation 2x² - kx + k = 0 has equal roots is:",
        "question_hi": "k के वे मान जिनके लिए द्विघात समीकरण 2x² - kx + k = 0 के समान मूल हैं, है:",
        "options": [
            "0 only",
            "4",
            "8 only",
            "0, 8"
        ],
        "options_hi": [
            "केवल 0",
            "4",
            "केवल 8",
            "0, 8"
        ],
        "correct_index": 3,
        "explanation": "For equal roots, D = 0 ⇒ b² - 4ac = 0 ⇒ (-k)² - 4(2)(k) = 0 ⇒ k² - 8k = 0 ⇒ k(k - 8) = 0. Therefore, k = 0 or k = 8.",
        "explanation_hi": "समान मूलों के लिए, D = 0 ⇒ b² - 4ac = 0 ⇒ (-k)² - 4(2)(k) = 0 ⇒ k² - 8k = 0 ⇒ k(k - 8) = 0। इसलिए, k = 0 या k = 8।"
    },
    {
        "id": "KOBJ_CLASS10_MATH_CH4_107_MCQ",
        "type": "mcq",
        "question": "If the discriminant of a quadratic equation is zero, then its roots are:",
        "question_hi": "यदि किसी द्विघात समीकरण का विविक्तकर शून्य है, तो इसके मूल हैं:",
        "options": [
            "Real and distinct",
            "Real and equal",
            "Not real",
            "Cannot be determined"
        ],
        "options_hi": [
            "वास्तविक और भिन्न",
            "वास्तविक और समान",
            "वास्तविक नहीं",
            "निर्धारित नहीं किया जा सकता"
        ],
        "correct_index": 1,
        "explanation": "When the discriminant (b² - 4ac) is exactly equal to 0, the quadratic formula gives x = -b/2a, resulting in two real and equal roots.",
        "explanation_hi": "जब विविक्तकर (b² - 4ac) ठीक 0 के बराबर होता है, तो द्विघात सूत्र x = -b/2a देता है, जिसके परिणामस्वरूप दो वास्तविक और समान मूल प्राप्त होते हैं।"
    },
    {
        "id": "KOBJ_CLASS10_MATH_CH4_108_MCQ",
        "type": "mcq",
        "question": "The sum of the roots of the quadratic equation 3x² - 9x + 5 = 0 is:",
        "question_hi": "द्विघात समीकरण 3x² - 9x + 5 = 0 के मूलों का योग है:",
        "options": [
            "3",
            "-3",
            "5/3",
            "-5/3"
        ],
        "options_hi": [
            "3",
            "-3",
            "5/3",
            "-5/3"
        ],
        "correct_index": 0,
        "explanation": "The sum of the roots of ax² + bx + c = 0 is given by -b/a. Here a = 3, b = -9. Sum = -(-9)/3 = 9/3 = 3.",
        "explanation_hi": "ax² + bx + c = 0 के मूलों का योग -b/a द्वारा दिया जाता है। यहाँ a = 3, b = -9. योग = -(-9)/3 = 9/3 = 3।"
    },
    {
        "id": "KOBJ_CLASS10_MATH_CH4_109_MCQ",
        "type": "mcq",
        "question": "If x = 1 is a common root of the equations ax² + ax + 3 = 0 and x² + x + b = 0, then ab equals:",
        "question_hi": "यदि x = 1 समीकरणों ax² + ax + 3 = 0 और x² + x + b = 0 का एक उभयनिष्ठ (common) मूल है, तो ab बराबर है:",
        "options": [
            "3",
            "3.5",
            "6",
            "-3"
        ],
        "options_hi": [
            "3",
            "3.5",
            "6",
            "-3"
        ],
        "correct_index": 0,
        "explanation": "Put x = 1 in both equations. First: a(1)² + a(1) + 3 = 0 ⇒ 2a = -3 ⇒ a = -3/2. Second: 1² + 1 + b = 0 ⇒ 2 + b = 0 ⇒ b = -2. So, ab = (-3/2) × (-2) = 3.",
        "explanation_hi": "दोनों समीकरणों में x = 1 रखें। पहला: a(1)² + a(1) + 3 = 0 ⇒ 2a = -3 ⇒ a = -3/2. दूसरा: 1² + 1 + b = 0 ⇒ 2 + b = 0 ⇒ b = -2. इसलिए, ab = (-3/2) × (-2) = 3।"
    },
    {
        "id": "KOBJ_CLASS10_MATH_CH4_110_MCQ",
        "type": "mcq",
        "question": "The product of two consecutive positive integers is 306. To find the integers, this can be represented as:",
        "question_hi": "दो क्रमागत धनात्मक पूर्णांकों का गुणनफल 306 है। पूर्णांक ज्ञात करने के लिए, इसे इस प्रकार निरूपित किया जा सकता है:",
        "options": [
            "x² + x - 306 = 0",
            "x² - x - 306 = 0",
            "x² + 2x - 306 = 0",
            "x² - 2x - 306 = 0"
        ],
        "options_hi": [
            "x² + x - 306 = 0",
            "x² - x - 306 = 0",
            "x² + 2x - 306 = 0",
            "x² - 2x - 306 = 0"
        ],
        "correct_index": 0,
        "explanation": "Let the consecutive integers be x and x + 1. Their product is x(x + 1) = 306 ⇒ x² + x - 306 = 0.",
        "explanation_hi": "माना क्रमागत पूर्णांक x और x + 1 हैं। उनका गुणनफल x(x + 1) = 306 ⇒ x² + x - 306 = 0 है।"
    }
]

# Append the new MCQs
blocks.extend(new_mcqs)

# Write back to cbse file
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(blocks, f, ensure_ascii=False, indent=2)

# Copy to gseb file
shutil.copy2(file_path, gseb_file_path)

print("Successfully added 10 MCQs and synced CBSE and GSEB files!")
