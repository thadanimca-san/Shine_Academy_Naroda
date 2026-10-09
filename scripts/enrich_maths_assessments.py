import json
import os

def generate_maths_assessments():
    os.makedirs("app_core/assessment", exist_ok=True)

    maths_exercises = {
        1: [
            {
                "id": "KOBJ_CLASS9_MATHS_CH1_Q1",
                "question": "Is zero a rational number? Can you write it in the form p/q, where p and q are integers and q ≠ 0?",
                "question_hi": "क्या शून्य एक परिमेय संख्या है? क्या इसे p/q के रूप में लिखा जा सकता है, जहाँ p और q पूर्णांक हैं और q ≠ 0?",
                "question_gu": "શું શૂન્ય એ સંમેય સંખ્યા છે? શું તેને p/q સ્વરૂપમાં લખી શકાય, જ્યાં p અને q પૂર્ણાંક છે અને q ≠ 0?",
                "options": ["Yes, 0 = 0/1", "No, it cannot be written as p/q", "Only if q = 0", "None of these"],
                "options_hi": ["हाँ, 0 = 0/1", "नहीं, इसे p/q के रूप में नहीं लिखा जा सकता", "केवल यदि q = 0", "इनमें से कोई नहीं"],
                "options_gu": ["હા, 0 = 0/1", "ના, તેને p/q સ્વરૂપમાં લખી શકાતું નથી", "માત્ર જો q = 0 હોય", "આમાંથી એક પણ નહીં"],
                "correct_index": 0,
                "explanation": "Zero is a rational number because it can be written as 0/1, 0/2, etc., where denominator q ≠ 0.",
                "explanation_hi": "शून्य एक परिमेय संख्या है क्योंकि इसे 0/1, 0/2 आदि के रूप में लिखा जा सकता है, जहाँ हर q ≠ 0 है।",
                "explanation_gu": "શૂન્ય એ સંમેય સંખ્યા છે કારણ કે તેને 0/1, 0/2 વગેરે સ્વરૂપમાં લખી શકાય છે, જ્યાં છેદ q ≠ 0 છે."
            },
            {
                "id": "KOBJ_CLASS9_MATHS_CH1_Q2",
                "question": "Find six rational numbers between 3 and 4.",
                "question_hi": "3 और 4 के बीच छह परिमेय संख्याएँ ज्ञात कीजिए।",
                "question_gu": "3 અને 4 વચ્ચે છ સંમેય સંખ્યાઓ શોધો.",
                "options": ["22/7, 23/7, 24/7, 25/7, 26/7, 27/7", "3.1, 3.2, 3.3, 3.4, 3.5, 3.6", "21/7 to 28/7", "Both A and B are valid"],
                "options_hi": ["22/7, 23/7, 24/7, 25/7, 26/7, 27/7", "3.1, 3.2, 3.3, 3.4, 3.5, 3.6", "21/7 से 28/7", "A और B दोनों मान्य हैं"],
                "options_gu": ["22/7, 23/7, 24/7, 25/7, 26/7, 27/7", "3.1, 3.2, 3.3, 3.4, 3.5, 3.6", "21/7 થી 28/7", "A અને B બંને માન્ય છે"],
                "correct_index": 3,
                "explanation": "Multiplying numerator and denominator by 7 gives 21/7 and 28/7. Rational numbers: 22/7, 23/7, 24/7, 25/7, 26/7, 27/7.",
                "explanation_hi": "अंश और हर को 7 से गुणा करने पर 21/7 और 28/7 मिलता है। परिमेय संख्याएँ: 22/7, 23/7, 24/7, 25/7, 26/7, 27/7।",
                "explanation_gu": "અંશ અને છેદને 7 વડે ગુણતાં 21/7 અને 28/7 મળે છે. સંમેય સંખ્યાઓ: 22/7, 23/7, 24/7, 25/7, 26/7, 27/7."
            }
        ],
        2: [
            {
                "id": "KOBJ_CLASS9_MATHS_CH2_Q1",
                "question": "Find the value of polynomial p(x) = 5x - 4x² + 3 at x = -1.",
                "question_hi": "x = -1 पर बहुपद p(x) = 5x - 4x² + 3 का मान ज्ञात कीजिए।",
                "question_gu": "x = -1 પર બહુપદી p(x) = 5x - 4x² + 3 ની કિંમત શોધો.",
                "options": ["-6", "-3", "6", "4"],
                "options_hi": ["-6", "-3", "6", "4"],
                "options_gu": ["-6", "-3", "6", "4"],
                "correct_index": 0,
                "explanation": "p(-1) = 5(-1) - 4(-1)² + 3 = -5 - 4 + 3 = -6.",
                "explanation_hi": "p(-1) = 5(-1) - 4(1) + 3 = -5 - 4 + 3 = -6.",
                "explanation_gu": "p(-1) = 5(-1) - 4(1) + 3 = -5 - 4 + 3 = -6."
            }
        ],
        3: [
            {
                "id": "KOBJ_CLASS9_MATHS_CH3_Q1",
                "question": "In which quadrant does the point (-3, 5) lie?",
                "question_hi": "बिंदु (-3, 5) किस चतुर्थांश में स्थित है?",
                "question_gu": "બિંદુ (-3, 5) કયા ચરણમાં આવેલું છે?",
                "options": ["Quadrant I", "Quadrant II", "Quadrant III", "Quadrant IV"],
                "options_hi": ["प्रथम चतुर्थांश", "द्वितीय चतुर्थांश", "तृतीय चतुर्थांश", "चतुर्थ चतुर्थांश"],
                "options_gu": ["પ્રથમ ચરણ", "દ્વિતીય ચરણ", "તૃતીય ચરણ", "ચતુર્થ ચરણ"],
                "correct_index": 1,
                "explanation": "Since x-coordinate is negative (-3) and y-coordinate is positive (5), the point lies in Quadrant II.",
                "explanation_hi": "चूंकि x-निर्देशांक ऋणात्मक (-3) और y-निर्देशांक धनात्मक (5) है, बिंदु द्वितीय चतुर्थांश में स्थित है।",
                "explanation_gu": "x-યામ ઋણ (-3) અને y-યામ ધન (5) હોવાથી, બિંદુ દ્વિતીય ચરણમાં આવેલું છે."
            }
        ],
        4: [
            {
                "id": "KOBJ_CLASS9_MATHS_CH4_Q1",
                "question": "Find the value of k, if x = 2, y = 1 is a solution of the equation 2x + 3y = k.",
                "question_hi": "यदि x = 2, y = 1 समीकरण 2x + 3y = k का एक हल है, तो k का मान ज्ञात कीजिए।",
                "question_gu": "જો x = 2, y = 1 એ સમીકરણ 2x + 3y = k નો ઉકેલ હોય, તો k ની કિંમત શોધો.",
                "options": ["7", "5", "6", "8"],
                "options_hi": ["7", "5", "6", "8"],
                "options_gu": ["7", "5", "6", "8"],
                "correct_index": 0,
                "explanation": "Substitute x = 2 and y = 1 into equation: 2(2) + 3(1) = 4 + 3 = 7. Thus k = 7.",
                "explanation_hi": "x = 2 और y = 1 रखें: 2(2) + 3(1) = 4 + 3 = 7। अतः k = 7।",
                "explanation_gu": "x = 2 અને y = 1 મૂકતાં: 2(2) + 3(1) = 4 + 3 = 7. તેથી k = 7."
            }
        ],
        5: [
            {
                "id": "KOBJ_CLASS9_MATHS_CH5_Q1",
                "question": "How many lines can pass through a single point?",
                "question_hi": "एक बिंदु से होकर कितनी रेखाएं गुजर सकती हैं?",
                "question_gu": "એક બિંદુમાંથી કેટલી રેખાઓ પસાર થઈ શકે?",
                "options": ["Only one", "Only two", "Infinitely many", "Zero"],
                "options_hi": ["केवल एक", "केवल दो", "अनंत", "शून्य"],
                "options_gu": ["માત્ર એક", "માત્ર બે", "અસંખ્ય (અનંત)", "શૂન્ય"],
                "correct_index": 2,
                "explanation": "According to Euclid's Axioms, infinitely many lines can pass through a single point.",
                "explanation_hi": "यूक्लिड के अभिगृहीतों के अनुसार, एक बिंदु से होकर अनंत रेखाएँ गुजर सकती हैं।",
                "explanation_gu": "યુક્લિડના સ્વયંસિદ્ધ સત્યો અનુસાર, એક બિંદુમાંથી અસંખ્ય રેખાઓ પસાર થઈ શકે છે."
            }
        ],
        6: [
            {
                "id": "KOBJ_CLASS9_MATHS_CH6_Q1",
                "question": "If two interior angles on the same side of a transversal are in ratio 2:3, find the larger angle.",
                "question_hi": "यदि तिर्यक रेखा के एक ही ओर के दो अंतः कोण 2:3 के अनुपात में हैं, तो बड़ा कोण ज्ञात कीजिए।",
                "question_gu": "જો છેદિકાની એક જ તરફના બે અંતઃકોણ 2:3 ના પ્રમાણમાં હોય, તો મોટો કોણ શોધો.",
                "options": ["108°", "72°", "90°", "120°"],
                "options_hi": ["108°", "72°", "90°", "120°"],
                "options_gu": ["108°", "72°", "90°", "120°"],
                "correct_index": 0,
                "explanation": "Consecutive interior angles are supplementary (sum = 180°). 2x + 3x = 180° => 5x = 180° => x = 36°. Larger angle = 3 × 36° = 108°.",
                "explanation_hi": "अंतः कोणों का योग = 180°। 5x = 180° => x = 36°। बड़ा कोण = 3 × 36° = 108°।",
                "explanation_gu": "અંતઃકોણોનો સરવાળો = 180°। 5x = 180° => x = 36°। મોટો કોણ = 3 × 36° = 108°."
            }
        ],
        7: [
            {
                "id": "KOBJ_CLASS9_MATHS_CH7_Q1",
                "question": "Which of the following is NOT a criterion for congruence of triangles?",
                "question_hi": "निम्नलिखित में से कौन सा त्रिभुजों की सर्वांगसमता की कसौटी नहीं है?",
                "question_gu": "નીચેનામાંથી કઈ ત્રિકોણની સરૂપતા/સર્વાંગસમતાની કસોટી નથી?",
                "options": ["SSA", "SAS", "ASA", "SSS"],
                "options_hi": ["SSA (भुजा-भुजा-कोण)", "SAS (भुजा-कोण-भुजा)", "ASA (कोण-भुजा-कोण)", "SSS (भुजा-भुजा-भुजा)"],
                "options_gu": ["SSA (બાજુ-બાજુ-ખૂણો)", "SAS (બાજુ-ખૂણો-બાજુ)", "ASA (ખૂણો-બાજુ-ખૂણો)", "SSS (બાજુ-બાજુ-બાજુ)"],
                "correct_index": 0,
                "explanation": "SSA (Side-Side-Angle) is not a valid congruence rule in Euclidean Geometry.",
                "explanation_hi": "SSA (भुजा-भुजा-कोण) यूक्लिडीय ज्यामिति में एक मान्य सर्वांगसमता नियम नहीं है।",
                "explanation_gu": "SSA (બાજુ-બાજુ-ખૂણો) એ ભૂમિતિમાં માન્ય સર્વાંગસમતાનો નિયમ નથી."
            }
        ],
        8: [
            {
                "id": "KOBJ_CLASS9_MATHS_CH8_Q1",
                "question": "The three angles of a quadrilateral are 75°, 90°, and 75°. Find the fourth angle.",
                "question_hi": "एक चतुर्भुज के तीन कोण 75°, 90° और 75° हैं। चौथा कोण ज्ञात कीजिए।",
                "question_gu": "ચતુષ્કોણના ત્રણ ખૂણાઓ 75°, 90° અને 75° છે. ચોથો ખૂણો શોધો.",
                "options": ["120°", "90°", "105°", "110°"],
                "options_hi": ["120°", "90°", "105°", "110°"],
                "options_gu": ["120°", "90°", "105°", "110°"],
                "correct_index": 0,
                "explanation": "Sum of all four interior angles of a quadrilateral = 360°. Fourth angle = 360° - (75° + 90° + 75°) = 360° - 240° = 120°.",
                "explanation_hi": "चतुर्भुज के सभी अंतः कोणों का योग = 360°। चौथा कोण = 360° - 240° = 120°।",
                "explanation_gu": "ચતુષ્કોણના ચારેય ખૂણાઓનો સરવાળો = 360°। ચોથો ખૂણો = 360° - 240° = 120°."
            }
        ],
        9: [
            {
                "id": "KOBJ_CLASS9_MATHS_CH9_Q1",
                "question": "Equal chords of a circle subtend _____ angles at the centre.",
                "question_hi": "वृत्त की समान जीवाएं केंद्र पर _____ कोण अंतरित करती हैं।",
                "question_gu": "વર્તુળની સમાન જીવાઓ કેન્દ્ર આગળ _____ ખૂણા આંતરે છે.",
                "options": ["Equal", "Unequal", "Right angles", "Complementary"],
                "options_hi": ["बराबर (समान)", "असमान", "समकोण", "पूरक"],
                "options_gu": ["સમાન", "અસમાન", "કાટખૂણા", "કોટિકોણ"],
                "correct_index": 0,
                "explanation": "Theorem 9.1: Equal chords of a circle subtend equal angles at the centre.",
                "explanation_hi": "प्रमेय 9.1: वृत्त की समान जीवाएं केंद्र पर बराबर कोण अंतरित करती हैं।",
                "explanation_gu": "પ્રમેય 9.1: વર્તુળની સમાન જીવાઓ કેન્દ્ર આગળ સમાન ખૂણા આંતરે છે."
            }
        ],
        10: [
            {
                "id": "KOBJ_CLASS9_MATHS_CH10_Q1",
                "question": "Find the area of a triangle with sides 13 cm, 14 cm, and 15 cm using Heron's Formula.",
                "question_hi": "हीरोन के सूत्र का उपयोग करके 13 cm, 14 cm और 15 cm भुजाओं वाले त्रिभुज का क्षेत्रफल ज्ञात कीजिए।",
                "question_gu": "હેરોનના સૂત્રનો ઉપયોગ કરીને 13 cm, 14 cm અને 15 cm બાજુઓવાળા ત્રિકોણનું ક્ષેત્રફળ શોધો.",
                "options": ["84 cm²", "42 cm²", "168 cm²", "90 cm²"],
                "options_hi": ["84 cm²", "42 cm²", "168 cm²", "90 cm²"],
                "options_gu": ["84 cm²", "42 cm²", "168 cm²", "90 cm²"],
                "correct_index": 0,
                "explanation": "Semi-perimeter s = (13+14+15)/2 = 21 cm. Area = √(21 × 8 × 7 × 6) = √(7056) = 84 cm².",
                "explanation_hi": "s = 21 cm। क्षेत्रफल = √(21 × 8 × 7 × 6) = 84 cm²।",
                "explanation_gu": "s = 21 cm। ક્ષેત્રફળ = √(21 × 8 × 7 × 6) = 84 cm²."
            }
        ],
        11: [
            {
                "id": "KOBJ_CLASS9_MATHS_CH11_Q1",
                "question": "Find the total surface area of a hemisphere of radius 10 cm. (Use π = 3.14)",
                "question_hi": "10 cm त्रिज्या वाले एक अर्धगोले का कुल पृष्ठीय क्षेत्रफल ज्ञात कीजिए। (π = 3.14 का प्रयोग करें)",
                "question_gu": "10 cm ત્રિજ્યા ધરાવતા અર્ધગોળકની કુલ સપાટીનું ક્ષેત્રફળ શોધો. (π = 3.14 લો)",
                "options": ["942 cm²", "628 cm²", "1256 cm²", "314 cm²"],
                "options_hi": ["942 cm²", "628 cm²", "1256 cm²", "314 cm²"],
                "options_gu": ["942 cm²", "628 cm²", "1256 cm²", "314 cm²"],
                "correct_index": 0,
                "explanation": "Total Surface Area of Hemisphere = 3πr² = 3 × 3.14 × 100 = 942 cm².",
                "explanation_hi": "कुल पृष्ठीय क्षेत्रफल = 3πr² = 3 × 3.14 × 100 = 942 cm²।",
                "explanation_gu": "કુલ સપાટીનું ક્ષેત્રફળ = 3πr² = 3 × 3.14 × 100 = 942 cm²."
            }
        ],
        12: [
            {
                "id": "KOBJ_CLASS9_MATHS_CH12_Q1",
                "question": "In a bar graph, what does the width of each bar represent?",
                "question_hi": "एक दंड आलेख (Bar graph) में, प्रत्येक दंड की चौड़ाई क्या दर्शाती है?",
                "question_gu": "સ્તંભ આલેખ (Bar graph) માં, દરેક સ્તંભની પહોળાઈ શું દર્શાવે છે?",
                "options": ["Width is arbitrary and uniform; height represents frequency", "Width represents frequency", "Width represents cumulative frequency", "None of these"],
                "options_hi": ["चौड़ाई स्वेच्छ और समान होती है; ऊंचाई बारंबारता दर्शाती है", "चौड़ाई बारंबारता दर्शाती है", "चौड़ाई संचयी बारंबारता दर्शाती है", "इनमें से कोई नहीं"],
                "options_gu": ["પહોળાઈ સ્વેચ્છિક અને સમાન હોય છે; ઊંચાઈ આવૃત્તિ દર્શાવે છે", "પહોળાઈ આવૃત્તિ દર્શાવે છે", "પહોળાઈ સંચિત આવૃત્તિ દર્શાવે છે", "આમાંથી એક પણ નહીં"],
                "correct_index": 0,
                "explanation": "In bar graphs, bars have uniform width separated by equal spaces. Only the height of the bar is proportional to the frequency.",
                "explanation_hi": "दंड आलेखों में, दंड समान चौड़ाई के होते हैं। केवल दंड की ऊंचाई बारंबारता के समानुपाती होती है।",
                "explanation_gu": "સ્તંભ આલેખમાં સ્તંભો સમાન પહોળાઈ ધરાવે છે. માત્ર સ્તંભની ઊંચાઈ જ આવૃત્તિના સમપ્રમાણમાં હોય છે."
            }
        ]
    }

    for ch_num, q_list in maths_exercises.items():
        assess_file = f"app_core/assessment/gseb_class9_maths_ch{ch_num}_questions.json"
        with open(assess_file, "w", encoding="utf-8") as f:
            json.dump(q_list, f, ensure_ascii=False, indent=2)
        print(f"Populated Maths Ch {ch_num} assessment bank with {len(q_list)} questions.")

if __name__ == "__main__":
    generate_maths_assessments()
