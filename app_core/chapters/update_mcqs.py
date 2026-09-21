import json

mcqs = [
    {
        "id": "QUIZ_ncert_class10_maths_ch10_1",
        "type": "quiz",
        "question": "If a line intersects a circle at two distinct points, what is the line called?",
        "question_hi": "यदि एक रेखा वृत्त को दो भिन्न बिंदुओं पर प्रतिच्छेद करती है, तो रेखा को क्या कहा जाता है?",
        "options": ["Tangent", "Secant", "Chord", "Diameter"],
        "options_hi": ["स्पर्श रेखा", "छेदक रेखा", "जीवा", "व्यास"],
        "correct_index": 1,
        "explanation": "A line that intersects a circle at two distinct points is called a secant. A tangent touches at one point, and a chord is a line segment whose endpoints lie on the circle.",
        "explanation_hi": "एक रेखा जो वृत्त को दो भिन्न बिंदुओं पर काटती है उसे छेदक रेखा (secant) कहा जाता है। स्पर्श रेखा केवल एक बिंदु पर छूती है, और जीवा एक रेखाखंड है जिसके दोनों सिरे वृत्त पर होते हैं।"
    },
    {
        "id": "QUIZ_ncert_class10_maths_ch10_2",
        "type": "quiz",
        "question": "How many parallel tangents can a circle have at the most?",
        "question_hi": "एक वृत्त की अधिकतम कितनी समांतर स्पर्श रेखाएँ हो सकती हैं?",
        "options": ["1", "2", "3", "Infinite"],
        "options_hi": ["1", "2", "3", "अनंत"],
        "correct_index": 1,
        "explanation": "A circle can have at most two parallel tangents. They will be at opposite ends of a diameter.",
        "explanation_hi": "एक वृत्त की अधिकतम दो समांतर स्पर्श रेखाएँ हो सकती हैं। वे एक व्यास के विपरीत सिरों पर होंगी।"
    },
    {
        "id": "QUIZ_ncert_class10_maths_ch10_3",
        "type": "quiz",
        "question": "A tangent PQ at a point P of a circle of radius 5 cm meets a line through the centre O at a point Q so that OQ = 12 cm. Length PQ is:",
        "question_hi": "5 सेमी त्रिज्या वाले एक वृत्त के बिंदु P पर स्पर्श रेखा PQ केंद्र O से जाने वाली एक रेखा से बिंदु Q पर इस प्रकार मिलती है कि OQ = 12 सेमी है। PQ की लंबाई है:",
        "options": ["12 cm", "13 cm", "8.5 cm", "√119 cm"],
        "options_hi": ["12 सेमी", "13 सेमी", "8.5 सेमी", "√119 सेमी"],
        "correct_index": 3,
        "explanation": "Since tangent is perpendicular to radius, ΔOPQ is right-angled at P. By Pythagoras Theorem: OQ² = OP² + PQ². 12² = 5² + PQ² ⇒ 144 = 25 + PQ² ⇒ PQ² = 119 ⇒ PQ = √119 cm.",
        "explanation_hi": "चूँकि स्पर्श रेखा त्रिज्या पर लंब होती है, ΔOPQ, P पर समकोण है। पाइथागोरस प्रमेय द्वारा: OQ² = OP² + PQ²। 12² = 5² + PQ² ⇒ 144 = 25 + PQ² ⇒ PQ² = 119 ⇒ PQ = √119 सेमी।"
    },
    {
        "id": "QUIZ_ncert_class10_maths_ch10_4",
        "type": "quiz",
        "question": "If tangents PA and PB from a point P to a circle with centre O are inclined to each other at angle of 80°, then ∠POA is equal to:",
        "question_hi": "यदि एक बिंदु P से केंद्र O वाले किसी वृत्त पर PA और PB स्पर्श रेखाएँ परस्पर 80° के कोण पर झुकी हों, तो ∠POA बराबर है:",
        "options": ["50°", "60°", "70°", "80°"],
        "options_hi": ["50°", "60°", "70°", "80°"],
        "correct_index": 0,
        "explanation": "In quadrilateral OAPB, ∠A = ∠B = 90°. ∠APB = 80°. So ∠AOB = 360 - (90 + 90 + 80) = 100°. In ΔPOA and ΔPOB, they are congruent. So ∠POA = ∠AOB / 2 = 100 / 2 = 50°.",
        "explanation_hi": "चतुर्भुज OAPB में, ∠A = ∠B = 90°। ∠APB = 80°। अतः ∠AOB = 360 - (90 + 90 + 80) = 100°। ΔPOA और ΔPOB में, वे सर्वांगसम हैं। इसलिए ∠POA = ∠AOB / 2 = 100 / 2 = 50°।"
    },
    {
        "id": "QUIZ_ncert_class10_maths_ch10_5",
        "type": "quiz",
        "question": "The lengths of tangents drawn from an external point to a circle are:",
        "question_hi": "वृत्त के बाहर स्थित किसी बिंदु से वृत्त पर खींची गई स्पर्श रेखाओं की लंबाइयाँ होती हैं:",
        "options": ["Unequal", "Equal", "Parallel", "Perpendicular"],
        "options_hi": ["असमान", "समान (बराबर)", "समांतर", "लंबवत"],
        "correct_index": 1,
        "explanation": "According to Theorem 10.2, the lengths of tangents drawn from an external point to a circle are equal.",
        "explanation_hi": "प्रमेय 10.2 के अनुसार, वृत्त के बाहर स्थित किसी बिंदु से वृत्त पर खींची गई स्पर्श रेखाओं की लंबाइयाँ समान (बराबर) होती हैं।"
    },
    {
        "id": "QUIZ_ncert_class10_maths_ch10_6",
        "type": "quiz",
        "question": "If TP and TQ are two tangents to a circle with centre O so that ∠POQ = 110°, then ∠PTQ is equal to:",
        "question_hi": "यदि केंद्र O वाले किसी वृत्त पर TP और TQ दो स्पर्श रेखाएँ इस प्रकार हैं कि ∠POQ = 110° है, तो ∠PTQ बराबर है:",
        "options": ["60°", "70°", "80°", "90°"],
        "options_hi": ["60°", "70°", "80°", "90°"],
        "correct_index": 1,
        "explanation": "In quadrilateral OPTQ, ∠OPT = ∠OQT = 90° (Radius ⊥ Tangent). Sum of angles = 360°. So, ∠PTQ = 360° - (90° + 90° + 110°) = 70°.",
        "explanation_hi": "चतुर्भुज OPTQ में, ∠OPT = ∠OQT = 90° (त्रिज्या ⊥ स्पर्श रेखा)। कोणों का योग = 360°। अतः, ∠PTQ = 360° - (90° + 90° + 110°) = 70°।"
    },
    {
        "id": "QUIZ_ncert_class10_maths_ch10_7",
        "type": "quiz",
        "question": "A circle can be inscribed in a quadrilateral ABCD. Which of the following is true?",
        "question_hi": "एक वृत्त को एक चतुर्भुज ABCD के अंदर खींचा (inscribed) जा सकता है। निम्नलिखित में से कौन सा सत्य है?",
        "options": ["AB + BC = CD + AD", "AB + CD = AD + BC", "AC = BD", "AB = CD"],
        "options_hi": ["AB + BC = CD + AD", "AB + CD = AD + BC", "AC = BD", "AB = CD"],
        "correct_index": 1,
        "explanation": "When a quadrilateral circumscribes a circle, the sum of its opposite sides are equal. Hence, AB + CD = AD + BC.",
        "explanation_hi": "जब एक चतुर्भुज एक वृत्त के परिगत (बाहर से छूता हुआ) होता है, तो उसकी सम्मुख भुजाओं का योग बराबर होता है। अतः, AB + CD = AD + BC।"
    },
    {
        "id": "QUIZ_ncert_class10_maths_ch10_8",
        "type": "quiz",
        "question": "The angle between the tangent at any point of a circle and the radius through the point of contact is:",
        "question_hi": "वृत्त के किसी बिंदु पर स्पर्श रेखा और स्पर्श बिंदु से होकर जाने वाली त्रिज्या के बीच का कोण होता है:",
        "options": ["30°", "45°", "60°", "90°"],
        "options_hi": ["30°", "45°", "60°", "90°"],
        "correct_index": 3,
        "explanation": "Theorem 10.1 states that the tangent at any point of a circle is perpendicular (90°) to the radius through the point of contact.",
        "explanation_hi": "प्रमेय 10.1 के अनुसार, वृत्त के किसी बिंदु पर स्पर्श रेखा स्पर्श बिंदु से जाने वाली त्रिज्या पर लंब (90°) होती है।"
    },
    {
        "id": "QUIZ_ncert_class10_maths_ch10_9",
        "type": "quiz",
        "question": "From a point Q, the length of the tangent to a circle is 24 cm and the distance of Q from the centre is 25 cm. The radius of the circle is:",
        "question_hi": "एक बिंदु Q से एक वृत्त पर स्पर्श रेखा की लंबाई 24 सेमी है तथा Q की केंद्र से दूरी 25 सेमी है। वृत्त की त्रिज्या है:",
        "options": ["7 cm", "12 cm", "15 cm", "24.5 cm"],
        "options_hi": ["7 सेमी", "12 सेमी", "15 सेमी", "24.5 सेमी"],
        "correct_index": 0,
        "explanation": "Let O be the center. OQ = 25, PQ = 24. ΔOPQ is right-angled at P. OP² = OQ² - PQ² = 25² - 24² = 625 - 576 = 49. OP = √49 = 7 cm.",
        "explanation_hi": "माना कि O केंद्र है। OQ = 25, PQ = 24। ΔOPQ, P पर समकोण है। OP² = OQ² - PQ² = 25² - 24² = 625 - 576 = 49। OP = √49 = 7 सेमी।"
    },
    {
        "id": "QUIZ_ncert_class10_maths_ch10_10",
        "type": "quiz",
        "question": "Two concentric circles are of radii 5 cm and 3 cm. The length of the chord of the larger circle which touches the smaller circle is:",
        "question_hi": "दो संकेंद्री वृत्तों की त्रिज्याएँ 5 सेमी तथा 3 सेमी हैं। बड़े वृत्त की उस जीवा की लंबाई ज्ञात कीजिए जो छोटे वृत्त को स्पर्श करती हो:",
        "options": ["4 cm", "8 cm", "10 cm", "6 cm"],
        "options_hi": ["4 सेमी", "8 सेमी", "10 सेमी", "6 सेमी"],
        "correct_index": 1,
        "explanation": "Let chord be AB, touching inner circle at P. OP ⊥ AB. OP=3, OA=5. In ΔOPA, AP² = 5² - 3² = 16 ⇒ AP=4 cm. Since perpendicular from center bisects chord, AB = 2 × AP = 8 cm.",
        "explanation_hi": "माना कि जीवा AB है, जो छोटे वृत्त को P पर छूती है। OP ⊥ AB। OP=3, OA=5। ΔOPA में, AP² = 5² - 3² = 16 ⇒ AP=4 सेमी। चूँकि केंद्र से लंब जीवा को समद्विभाजित करता है, AB = 2 × AP = 8 सेमी।"
    },
    {
        "id": "QUIZ_ncert_class10_maths_ch10_11",
        "type": "quiz",
        "question": "A tangent intersecting a circle at exactly one point is also known as:",
        "question_hi": "एक वृत्त को ठीक एक बिंदु पर प्रतिच्छेद करने वाली स्पर्श रेखा को इस रूप में भी जाना जाता है:",
        "options": ["Secant", "Radius", "Chord", "None of these"],
        "options_hi": ["छेदक रेखा", "त्रिज्या", "जीवा", "इनमें से कोई नहीं"],
        "correct_index": 3,
        "explanation": "A tangent is specifically a line that touches the circle at exactly one point. A secant intersects at two points, and a chord is a segment. Thus, none of the other terms mean tangent.",
        "explanation_hi": "स्पर्श रेखा विशेष रूप से एक ऐसी रेखा है जो वृत्त को ठीक एक बिंदु पर छूती है। छेदक रेखा दो बिंदुओं पर काटती है, और जीवा एक रेखाखंड है। इसलिए, अन्य विकल्पों में से कोई भी सही नहीं है।"
    },
    {
        "id": "QUIZ_ncert_class10_maths_ch10_12",
        "type": "quiz",
        "question": "In a right triangle ABC, right-angled at B, BC = 12 cm and AB = 5 cm. The radius of the circle inscribed in the triangle is:",
        "question_hi": "एक समकोण त्रिभुज ABC में, जिसका कोण B समकोण है, BC = 12 सेमी और AB = 5 सेमी है। त्रिभुज के अंदर बने वृत्त की त्रिज्या है:",
        "options": ["1 cm", "2 cm", "3 cm", "4 cm"],
        "options_hi": ["1 सेमी", "2 सेमी", "3 सेमी", "4 सेमी"],
        "correct_index": 1,
        "explanation": "Hypotenuse AC = √(12² + 5²) = 13 cm. For an inscribed circle in a right triangle, radius r = (AB + BC - AC) / 2 = (5 + 12 - 13) / 2 = 4 / 2 = 2 cm.",
        "explanation_hi": "कर्ण AC = √(12² + 5²) = 13 सेमी। एक समकोण त्रिभुज में अंतःवृत्त की त्रिज्या r = (AB + BC - AC) / 2 = (5 + 12 - 13) / 2 = 4 / 2 = 2 सेमी।"
    },
    {
        "id": "QUIZ_ncert_class10_maths_ch10_13",
        "type": "quiz",
        "question": "If a hexagon ABCDEF circumscribes a circle, then which of the following relations is correct?",
        "question_hi": "यदि एक षट्भुज ABCDEF एक वृत्त के परिगत है, तो निम्नलिखित में से कौन सा संबंध सही है?",
        "options": ["AB + CD + EF = BC + DE + FA", "AB = CD = EF", "AB + BC + CD = DE + EF + FA", "None of the above"],
        "options_hi": ["AB + CD + EF = BC + DE + FA", "AB = CD = EF", "AB + BC + CD = DE + EF + FA", "उपरोक्त में से कोई नहीं"],
        "correct_index": 0,
        "explanation": "For any polygon with an even number of sides circumscribing a circle, the sum of alternate sides is equal. Therefore, AB + CD + EF = BC + DE + FA.",
        "explanation_hi": "किसी भी सम-भुजाओं वाले बहुभुज के लिए जो एक वृत्त के परिगत होता है, एकांतर (alternate) भुजाओं का योग बराबर होता है। इसलिए, AB + CD + EF = BC + DE + FA।"
    },
    {
        "id": "QUIZ_ncert_class10_maths_ch10_14",
        "type": "quiz",
        "question": "A quadrilateral ABCD is drawn to circumscribe a circle. If AB = 4 cm, CD = 7 cm, and AD = 6 cm, what is the length of BC?",
        "question_hi": "एक चतुर्भुज ABCD एक वृत्त के परिगत खींचा गया है। यदि AB = 4 सेमी, CD = 7 सेमी और AD = 6 सेमी है, तो BC की लंबाई क्या है?",
        "options": ["3 cm", "4 cm", "5 cm", "6 cm"],
        "options_hi": ["3 सेमी", "4 सेमी", "5 सेमी", "6 सेमी"],
        "correct_index": 2,
        "explanation": "We know AB + CD = AD + BC. Substituting the values: 4 + 7 = 6 + BC ⇒ 11 = 6 + BC ⇒ BC = 5 cm.",
        "explanation_hi": "हम जानते हैं कि AB + CD = AD + BC. मान रखने पर: 4 + 7 = 6 + BC ⇒ 11 = 6 + BC ⇒ BC = 5 सेमी।"
    },
    {
        "id": "QUIZ_ncert_class10_maths_ch10_15",
        "type": "quiz",
        "question": "If tangents PA and PB from a point P to a circle with centre O are drawn, and ∠APB = 60°, then ΔPAB is:",
        "question_hi": "यदि एक बिंदु P से केंद्र O वाले वृत्त पर स्पर्श रेखाएँ PA और PB खींची जाती हैं, और ∠APB = 60° है, तो ΔPAB है:",
        "options": ["Right-angled", "Isosceles but not equilateral", "Equilateral", "Scalene"],
        "options_hi": ["समकोण", "समद्विबाहु लेकिन समबाहु नहीं", "समबाहु", "विषमबाहु"],
        "correct_index": 2,
        "explanation": "We know PA = PB (tangents from an external point). So ΔPAB is isosceles. This means ∠PAB = ∠PBA. Since ∠APB = 60°, the other two angles must sum to 120°, meaning each is 60°. A triangle with all angles 60° is equilateral.",
        "explanation_hi": "हम जानते हैं कि PA = PB (बाह्य बिंदु से स्पर्श रेखाएँ)। अतः ΔPAB समद्विबाहु है। इसका अर्थ है ∠PAB = ∠PBA। चूँकि ∠APB = 60° है, अन्य दो कोणों का योग 120° होना चाहिए, अर्थात प्रत्येक 60° है। एक त्रिभुज जिसके सभी कोण 60° हों, समबाहु (Equilateral) होता है।"
    }
]

file_path = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_maths_ch10.json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

new_blocks = [block for block in data['blocks'] if block.get('type') != 'quiz']
new_blocks.extend(mcqs)
data['blocks'] = new_blocks

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("JSON successfully updated")
