import json

questions = []

def add_q(q):
    questions.append(q)

add_q({
    "id": "Q_MATH10_CH2_001",
    "chapter_id": "gseb_class10_maths_ch2",
    "topic_id": "KOBJ_C10_MATH_CH2_DEF_001",
    "type": "mcq",
    "difficulty": "Beginner",
    "board": ["GSEB", "CBSE"],
    "marks": 1,
    "bloom_taxonomy": "Remembering",
    "keywords": ["degree", "polynomial"],
    "estimated_time_minutes": 1,
    "exam_frequency": "High",
    "question_text": "What is the degree of a quadratic polynomial? (द्विघात बहुपद की घात क्या होती है?)",
    "answer": "2",
    "options": ["1", "2", "3", "0"],
    "explanation": "A polynomial of degree 2 is called a quadratic polynomial. Example: x² + 2x + 1. (घात 2 वाले बहुपद को द्विघात बहुपद कहा जाता है। उदाहरण: x² + 2x + 1।)",
    "distractor_rationale": "1 is linear, 3 is cubic, and 0 is a constant polynomial.",
    "ai_context": {
        "learning_goal": "Recall the definition of a quadratic polynomial's degree.",
        "common_misconceptions": ["Thinking 'quadratic' means 4 (like quad)."],
        "hint": "Quadrate means square. What is the power of a squared variable? (Quadrate का अर्थ वर्ग होता है। वर्ग चर की घात क्या होती है?)"
    }
})

add_q({
    "id": "Q_MATH10_CH2_002",
    "chapter_id": "gseb_class10_maths_ch2",
    "topic_id": "KOBJ_C10_MATH_CH2_THEO_002",
    "type": "mcq",
    "difficulty": "Intermediate",
    "board": ["GSEB", "CBSE"],
    "marks": 1,
    "bloom_taxonomy": "Understanding",
    "keywords": ["zeroes", "x-axis", "graph"],
    "estimated_time_minutes": 2,
    "exam_frequency": "High",
    "question_text": "The zeroes of a polynomial p(x) are precisely the x-coordinates of the points where the graph of y = p(x) intersects the: (किसी बहुपद p(x) के शून्यक उन बिंदुओं के x-निर्देशांक होते हैं जहाँ y = p(x) का ग्राफ प्रतिच्छेद करता है:)",
    "answer": "X-axis (X-अक्ष)",
    "options": ["X-axis (X-अक्ष)", "Y-axis (Y-अक्ष)", "Origin (मूल बिंदु)", "None of these (इनमें से कोई नहीं)"],
    "explanation": "The value of polynomial p(x) becomes zero on the x-axis, so the points of intersection with the x-axis give the zeroes. (बहुपद p(x) का मान x-अक्ष पर शून्य हो जाता है, इसलिए x-अक्ष के साथ प्रतिच्छेदन बिंदु शून्यक देते हैं।)",
    "distractor_rationale": "Y-axis gives the value of p(0).",
    "ai_context": {
        "learning_goal": "Understand the geometric meaning of zeroes of a polynomial.",
        "common_misconceptions": ["Thinking the y-intercept is a zero."],
        "hint": "We are looking for points where y is 0. (हम उन बिंदुओं की तलाश कर रहे हैं जहां y 0 है।)"
    }
})

add_q({
    "id": "Q_MATH10_CH2_003",
    "chapter_id": "gseb_class10_maths_ch2",
    "topic_id": "KOBJ_C10_MATH_CH2_FORMULA_001",
    "type": "mcq",
    "difficulty": "Advanced",
    "board": ["GSEB", "CBSE"],
    "marks": 2,
    "bloom_taxonomy": "Applying",
    "keywords": ["sum", "product", "quadratic"],
    "estimated_time_minutes": 3,
    "exam_frequency": "High",
    "question_text": "Find a quadratic polynomial whose sum and product of zeroes are -3 and 2, respectively. (वह द्विघात बहुपद ज्ञात कीजिए जिसके शून्यकों का योग और गुणनफल क्रमशः -3 और 2 है।)",
    "answer": "x² + 3x + 2",
    "options": ["x² - 3x + 2", "x² + 3x + 2", "x² - 2x - 3", "x² + 2x - 3"],
    "explanation": "Formula: x² - (sum of zeroes)x + (product of zeroes). x² - (-3)x + 2 = x² + 3x + 2. (सूत्र: x² - (शून्यकों का योग)x + (शून्यकों का गुणनफल)। x² - (-3)x + 2 = x² + 3x + 2।)",
    "distractor_rationale": "Students might forget the minus sign in the formula x² - (sum)x + product.",
    "ai_context": {
        "learning_goal": "Construct a quadratic polynomial from given sum and product of zeroes.",
        "common_misconceptions": ["Adding the sum directly as the middle term without changing its sign."],
        "hint": "Remember the formula: k[x² - (α+β)x + αβ]. (सूत्र याद रखें: k[x² - (α+β)x + αβ]।)"
    }
})

add_q({
    "id": "Q_MATH10_CH2_004",
    "chapter_id": "gseb_class10_maths_ch2",
    "topic_id": "KOBJ_C10_MATH_CH2_FORMULA_001",
    "type": "mcq",
    "difficulty": "Intermediate",
    "board": ["GSEB", "CBSE"],
    "marks": 1,
    "bloom_taxonomy": "Analyzing",
    "keywords": ["zeroes", "quadratic"],
    "estimated_time_minutes": 2,
    "exam_frequency": "Medium",
    "question_text": "If α and β are the zeroes of the polynomial x² - 4x + 3, what is the value of α² + β²? (यदि α और β बहुपद x² - 4x + 3 के शून्यक हैं, तो α² + β² का मान क्या है?)",
    "answer": "10",
    "options": ["10", "16", "22", "6"],
    "explanation": "We know α + β = -(-4)/1 = 4, and αβ = 3/1 = 3. Using identity α² + β² = (α+β)² - 2αβ = (4)² - 2(3) = 16 - 6 = 10. (हम जानते हैं कि α + β = -(-4)/1 = 4, और αβ = 3/1 = 3। सर्वसमिका α² + β² = (α+β)² - 2αβ का उपयोग करने पर = (4)² - 2(3) = 16 - 6 = 10।)",
    "distractor_rationale": "16 is just (α+β)². 22 is (α+β)² + 2αβ.",
    "ai_context": {
        "learning_goal": "Analyze the relationship between zeroes and apply algebraic identities.",
        "common_misconceptions": ["Finding individual zeroes first, which can be time-consuming."],
        "hint": "Can you express α² + β² using (α+β) and αβ? (क्या आप (α+β) और αβ का उपयोग करके α² + β² व्यक्त कर सकते हैं?)"
    }
})

add_q({
    "id": "Q_MATH10_CH2_005",
    "chapter_id": "gseb_class10_maths_ch2",
    "topic_id": "KOBJ_C10_MATH_CH2_MCQ_003",
    "type": "mcq",
    "difficulty": "Intermediate",
    "board": ["GSEB", "CBSE"],
    "marks": 1,
    "bloom_taxonomy": "Applying",
    "keywords": ["cubic", "polynomial"],
    "estimated_time_minutes": 2,
    "exam_frequency": "Medium",
    "question_text": "What is the maximum number of zeroes a polynomial of degree 'n' can have? ('n' घात वाले बहुपद के अधिकतम कितने शून्यक हो सकते हैं?)",
    "answer": "n",
    "options": ["n-1", "n", "n+1", "infinite (अनंत)"],
    "explanation": "A polynomial of degree 'n' has at most 'n' zeroes. (घात 'n' वाले बहुपद के अधिकतम 'n' शून्यक होते हैं।)",
    "distractor_rationale": "Degree defines the maximum intersections with the x-axis.",
    "ai_context": {
        "learning_goal": "Apply the fundamental theorem of algebra regarding the number of zeroes.",
        "common_misconceptions": [],
        "hint": "A line (degree 1) crosses the x-axis at most 1 time. A parabola (degree 2) crosses at most 2 times. (एक रेखा (घात 1) x-अक्ष को अधिकतम 1 बार काटती है। परवलय (घात 2) अधिकतम 2 बार काटता है।)"
    }
})

with open('/home/ubuntu/Shine_Academy_Naroda/app_core/assessment/gseb_class10_maths_ch2_questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, indent=2, ensure_ascii=False)
