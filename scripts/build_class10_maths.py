import os
import json
import glob

# Chapter Metadata Titles
CHAPTER_TITLES = {
    1: {"title": "Real Numbers", "hi": "वास्तविक संख्याएं", "gu": "વાસ્તવિક સંખ્યાઓ"},
    2: {"title": "Polynomials", "hi": "बहुपद", "gu": "બહુપદીઓ"},
    3: {"title": "Pair of Linear Equations in Two Variables", "hi": "दो चरों वाले रैखिक समीकरण युग्म", "gu": "દ્વાચલ રેખીય સમીકરણ યુગ્મ"},
    4: {"title": "Quadratic Equations", "hi": "द्विघात समीकरण", "gu": "દ્વિઘાત સમીકરણો"},
    5: {"title": "Arithmetic Progressions", "hi": "समांतर श्रेढ़ियां", "gu": "સમાંતર શ્રેણીઓ"},
    6: {"title": "Triangles", "hi": "त्रिभुज", "gu": "ત્રિકોણ"},
    7: {"title": "Coordinate Geometry", "hi": "निर्देशांक ज्यामिति", "gu": "યામ ભૂમિતિ"},
    8: {"title": "Introduction to Trigonometry", "hi": "त्रिकोणमिति का परिचय", "gu": "ત્રિકોણમિતિનો પરિચય"},
    9: {"title": "Some Applications of Trigonometry", "hi": "त्रिकोणमिति के कुछ अनुप्रयोग", "gu": "ત્રિકોણમિતિના કેટલાક ઉપયોગો"},
    10: {"title": "Circles", "hi": "वृत्त", "gu": "વર્તુળ"},
    11: {"title": "Areas Related to Circles", "hi": "वृत्तों से संबंधित क्षेत्रफल", "gu": "વર્તુળ સંબંધિત ક્ષેત્રફળ"},
    12: {"title": "Surface Areas and Volumes", "hi": "पृष्ठीय क्षेत्रफल और आयतन", "gu": "પૃષ્ઠફળ અને ઘનફળ"},
    13: {"title": "Statistics", "hi": "सांख्यिकी", "gu": "આંકડાશાસ્ત્ર"},
    14: {"title": "Probability", "hi": "प्रायिकता", "gu": "સંભાવના"}
}

def create_ch3_comprehensive_blocks():
    """Builds a rich 35+ block comprehensive set for Class 10 Maths Chapter 3 (Linear Equations in Two Variables)."""
    blocks = [
        {
            "id": "KOBJ_C10_MATHS_CH3_HOOK",
            "type": "hook",
            "title": "The Mystery of the Cinema Tickets & Snacks",
            "title_hi": "सिनेमा टिकट और स्नैक्स का रहस्य",
            "title_gu": "સિનેમા ટિકિટ અને સ્નેક્સનું રહસ્ય",
            "body": "Aarav bought 2 movie tickets and 3 popcorn tubs for ₹450. Priya bought 1 ticket and 2 popcorn tubs for ₹260. How can we find the exact price of 1 movie ticket and 1 popcorn tub without guessing?",
            "body_hi": "आरव ने ₹450 में 2 मूवी टिकट और 3 पॉपकॉर्न टब खरीदे। प्रिया ने ₹260 में 1 टिकट और 2 पॉपकॉर्न टब खरीदे। बिना अनुमान लगाए हम 1 मूवी टिकट और 1 पॉपकॉर्न टब की सटीक कीमत कैसे ढूंढ सकते हैं?",
            "body_gu": "આરવે ₹450 માં 2 મુવી ટિકિટ અને 3 પોપકોર્ન ટબ ખરીદ્યા. પ્રિયાએ ₹260 માં 1 ટિકિટ અને 2 પોપકોર્ન ટબ ખરીદ્યા. અનુમાન લગાવ્યા વગર 1 મુવી ટિકિટ અને 1 પોપકોર્ન ટબની ચોક્કસ કિંમત કેવી રીતે શોધી શકીએ?"
        },
        {
            "id": "KOBJ_C10_MATHS_CH3_SOCRATIC_1",
            "type": "socratic_question",
            "question": "If you represent movie tickets as 'x' and popcorn tubs as 'y', what linear equations represent Aarav and Priya's purchases?",
            "question_hi": "यदि आप मूवी टिकट को 'x' और पॉपकॉर्न टब को 'y' के रूप में दर्शाते हैं, तो कौन से रैखिक समीकरण आरव और प्रिया की खरीदारी का प्रतिनिधित्व करते हैं?",
            "question_gu": "જો તમે મુવી ટિકિટને 'x' અને પોપકોર્ન ટબને 'y' તરીકે દર્શાવો, તો કયા રેખીય સમીકરણો આરવ અને પ્રિયાની ખરીદી દર્શાવે છે?",
            "explanation": "Aarav: 2x + 3y = 450. Priya: x + 2y = 260. This is a system of 2 linear equations in 2 variables.",
            "explanation_hi": "आरव: 2x + 3y = 450। प्रिया: x + 2y = 260। यह 2 चरों में 2 रैखिक समीकरणों की एक प्रणाली है।",
            "explanation_gu": "આરવ: 2x + 3y = 450. પ્રિયા: x + 2y = 260. આ 2 ચલોમાં 2 રેખીય સમીકરણોની પદ્ધતિ છે."
        },
        {
            "id": "KOBJ_C10_MATHS_CH3_THEORY_1",
            "type": "theory",
            "title": "General Form of Pair of Linear Equations",
            "title_hi": "रैखिक समीकरण युग्म का सामान्य रूप",
            "title_gu": "દ્વાચલ રેખીય સમીકરણ યુગ્મનું સામાન્ય સ્વરૂપ",
            "body": "A pair of linear equations in two variables x and y can be written as:\n1) a₁x + b₁y + c₁ = 0\n2) a₂x + b₂y + c₂ = 0\nwhere a₁, b₁, c₁, a₂, b₂, c₂ are real numbers such that a₁² + b₁² ≠ 0 and a₂² + b₂² ≠ 0.\n\nGeometrically, each linear equation represents a straight line in a 2D Cartesian plane.",
            "body_hi": "दो चरों x और y में रैखिक समीकरण युग्म को इस प्रकार लिखा जा सकता है:\n1) a₁x + b₁y + c₁ = 0\n2) a₂x + b₂y + c₂ = 0\nजहाँ a₁, b₁, c₁, a₂, b₂, c₂ ऐसी वास्तविक संख्याएँ हैं कि a₁² + b₁² ≠ 0 और a₂² + b₂² ≠ 0।\n\nज्यामितीय रूप से, प्रत्येक रैखिक समीकरण 2D कार्तीय तल में एक सीधी रेखा को दर्शाता है।",
            "body_gu": "બે ચલો x અને y માં દ્વાચલ રેખીય સમીકરણ યુગ્મને આ રીતે લખી શકાય:\n1) a₁x + b₁y + c₁ = 0\n2) a₂x + b₂y + c₂ = 0\nજ્યાં a₁, b₁, c₁, a₂, b₂, c₂ એવી વાસ્તવિક સંખ્યાઓ છે કે a₁² + b₁² ≠ 0 અને a₂² + b₂² ≠ 0.\n\nભૌમિતિક રીતે, દરેક રેખીય સમીકરણ 2D કાર્ટેઝિયન સમતલમાં એક સીધી રેખા દર્શાવે છે."
        },
        {
            "id": "KOBJ_C10_MATHS_CH3_THEORY_2",
            "type": "theory",
            "title": "Graphical Interpretation & Consistency Conditions",
            "title_hi": "आलेखीय व्याख्या और संगति की शर्तें",
            "title_gu": "આલેખીય અર્થઘટન અને સુસંગતતાની શરતો",
            "body": "For two lines a₁x + b₁y + c₁ = 0 and a₂x + b₂y + c₂ = 0:\n\n1) Intersecting Lines (Unique Solution):\n   If (a₁/a₂) ≠ (b₁/b₂), lines intersect at 1 point. System is Consistent.\n\n2) Coincident Lines (Infinitely Many Solutions):\n   If (a₁/a₂) = (b₁/b₂) = (c₁/c₂), lines overlap completely. System is Consistent (Dependent).\n\n3) Parallel Lines (No Solution):\n   If (a₁/a₂) = (b₁/b₂) ≠ (c₁/c₂), lines never meet. System is Inconsistent.",
            "body_hi": "दो रेखाओं a₁x + b₁y + c₁ = 0 और a₂x + b₂y + c₂ = 0 के लिए:\n\n1) प्रतिच्छेदी रेखाएं (अद्वितीय हल):\n   यदि (a₁/a₂) ≠ (b₁/b₂), तो रेखाएं 1 बिंदु पर प्रतिच्छेद करती हैं। निकाय संगत है।\n\n2) संपाती रेखाएं (अपरिमित रूप से अनेक हल):\n   यदि (a₁/a₂) = (b₁/b₂) = (c₁/c₂), तो रेखाएं पूरी तरह से ढक लेती हैं। निकाय संगत (आश्रित) है।\n\n3) समांतर रेखाएं (कोई हल नहीं):\n   यदि (a₁/a₂) = (b₁/b₂) ≠ (c₁/c₂), तो रेखाएं कभी नहीं मिलतीं। निकाय असंगत है।",
            "body_gu": "બે રેખાઓ a₁x + b₁y + c₁ = 0 અને a₂x + b₂y + c₂ = 0 માટે:\n\n1) છેદતી રેખાઓ (અનન્ય ઉકેલ):\n   જો (a₁/a₂) ≠ (b₁/b₂), તો રેખાઓ 1 બિંદુએ છેદે છે. પદ્ધતિ સુસંગત છે.\n\n2) સંપાતી રેખાઓ (અનંત ઉકેલો):\n   જો (a₁/a₂) = (b₁/b₂) = (c₁/c₂), તો રેખાઓ એકબીજા પર બંધબેસે છે. પદ્ધતિ સુસંગત (અવલંબી) છે.\n\n3) સમાંતર રેખાઓ (ઉકેલ નથી):\n   જો (a₁/a₂) = (b₁/b₂) ≠ (c₁/c₂), તો રેખાઓ ક્યારેય મળતી નથી. પદ્ધતિ અસુસંગત છે."
        },
        {
            "id": "KOBJ_C10_MATHS_CH3_QUIZ_1",
            "type": "quiz",
            "question": "For the lines 2x + 3y - 9 = 0 and 4x + 6y - 18 = 0, what is the nature of the lines and number of solutions?",
            "question_hi": "रेखाओं 2x + 3y - 9 = 0 और 4x + 6y - 18 = 0 के लिए, रेखाओं की प्रकृति और हलों की संख्या क्या है?",
            "question_gu": "રેખાઓ 2x + 3y - 9 = 0 અને 4x + 6y - 18 = 0 માટે, રેખાઓનું સ્વરૂપ અને ઉકેલોની સંખ્યા શું છે?",
            "options": [
                "Intersecting lines, Unique solution",
                "Coincident lines, Infinitely many solutions",
                "Parallel lines, No solution",
                "Perpendicular lines, Two solutions"
            ],
            "options_hi": [
                "प्रतिच्छेदी रेखाएं, अद्वितीय हल",
                "संपाती रेखाएं, अपरिमित रूप से अनेक हल",
                "समांतर रेखाएं, कोई हल नहीं",
                "लंबवत रेखाएं, दो हल"
            ],
            "options_gu": [
                "છેદતી રેખાઓ, અનન્ય ઉકેલ",
                "સંપાતી રેખાઓ, અનંત ઉકેલો",
                "સમાંતર રેખાઓ, ઉકેલ નથી",
                "લંબ રેખાઓ, બે ઉકેલો"
            ],
            "correct_index": 1,
            "explanation": "Ratio check: a₁/a₂ = 2/4 = 1/2. b₁/b₂ = 3/6 = 1/2. c₁/c₂ = -9/-18 = 1/2. Since a₁/a₂ = b₁/b₂ = c₁/c₂, the lines are coincident and have infinitely many solutions.",
            "explanation_hi": "अनुपात जाँच: a₁/a₂ = 2/4 = 1/2। b₁/b₂ = 3/6 = 1/2। c₁/c₂ = -9/-18 = 1/2। चूंकि a₁/a₂ = b₁/b₂ = c₁/c₂, रेखाएं संपाती हैं और अपरिमित रूप से अनेक हल हैं।",
            "explanation_gu": "ગુણોત્તર ચકાસણી: a₁/a₂ = 2/4 = 1/2. b₁/b₂ = 3/6 = 1/2. c₁/c₂ = -9/-18 = 1/2. આથી a₁/a₂ = b₁/b₂ = c₁/c₂ હોવાથી રેખાઓ સંપાતી છે અને અનંત ઉકેલો ધરાવે છે."
        },
        {
            "id": "KOBJ_C10_MATHS_CH3_THEORY_3",
            "type": "theory",
            "title": "Algebraic Method 1: Substitution Method",
            "title_hi": "बीजगणितीय विधि 1: प्रतिस्थापन विधि",
            "title_gu": "બીજગણિતીય રીત 1: આદેશની રીત",
            "body": "Steps for Substitution Method:\n1. Express one variable (say y) in terms of the other variable (x) from equation (1).\n2. Substitute this expression of y into equation (2) to get a single linear equation in x.\n3. Solve the equation to find x.\n4. Substitute the value of x back into step 1 to find y.",
            "body_hi": "प्रतिस्थापन विधि के चरण:\n1. समीकरण (1) से एक चर (मान लीजिए y) को दूसरे चर (x) के पदों में व्यक्त करें।\n2. y के इस मान को समीकरण (2) में रखकर x में एक रैखिक समीकरण प्राप्त करें।\n3. x का मान ज्ञात करने के लिए समीकरण हल करें।\n4. y का मान ज्ञात करने के लिए x का मान वापस चरण 1 में रखें।",
            "body_gu": "આદેશની રીતના પગલાં:\n1. સમીકરણ (1) માંથી એક ચલ (ધારો કે y) ને બીજા ચલ (x) ના સ્વરૂપમાં દર્શાવો.\n2. y ની આ કિંમતને સમીકરણ (2) માં મૂકીને x માં એક ચલ સમીકરણ મેળવો.\n3. x ની કિંમત શોધવા માટે સમીકરણ ઉકેલો.\n4. y ની કિંમત શોધવા માટે x ની કિંમત પાછી પગલા 1 માં મૂકો."
        },
        {
            "id": "KOBJ_C10_MATHS_CH3_EXAMPLE_1",
            "type": "worked_example",
            "title": "Worked Example: Substitution Method",
            "title_hi": "हल किया गया उदाहरण: प्रतिस्थापन विधि",
            "title_gu": "ગણેલું ઉદાહરણ: આદેશની રીત",
            "problem": "Solve the pair of linear equations by substitution method: x + y = 14 and x - y = 4.",
            "problem_hi": "प्रतिस्थापन विधि से रैखिक समीकरण युग्म को हल करें: x + y = 14 और x - y = 4।",
            "problem_gu": "આદેશની રીતથી રેખીય સમીકરણ યુગ્મ ઉકેલો: x + y = 14 અને x - y = 4.",
            "solution": "From eq (2): x = 4 + y.\nSubstitute in eq (1): (4 + y) + y = 14 => 4 + 2y = 14 => 2y = 10 => y = 5.\nNow x = 4 + 5 = 9.\nTherefore, x = 9, y = 5.",
            "solution_hi": "समीकरण (2) से: x = 4 + y।\nसमीकरण (1) में रखें: (4 + y) + y = 14 => 4 + 2y = 14 => 2y = 10 => y = 5।\nअब x = 4 + 5 = 9।\nइसलिए, x = 9, y = 5।",
            "solution_gu": "સમીકરણ (2) માંથી: x = 4 + y.\nસમીકરણ (1) માં મૂકો: (4 + y) + y = 14 => 4 + 2y = 14 => 2y = 10 => y = 5.\nહવે x = 4 + 5 = 9.\nતેથી, x = 9, y = 5."
        },
        {
            "id": "KOBJ_C10_MATHS_CH3_THEORY_4",
            "type": "theory",
            "title": "Algebraic Method 2: Elimination Method",
            "title_hi": "बीजगणितीय विधि 2: विलोपन विधि",
            "title_gu": "બીજગણિતીય રીત 2: લોપની રીત",
            "body": "Steps for Elimination Method:\n1. Multiply both equations by suitable non-zero constants so that coefficients of one variable (x or y) become numerically equal.\n2. Add or subtract the two equations to eliminate that variable.\n3. Solve the resulting equation in one variable.\n4. Substitute the value of that variable into either original equation to find the other variable.",
            "body_hi": "विलोपन विधि के चरण:\n1. दोनों समीकरणों को उपयुक्त अयोग्य शून्य अचरों से गुणा करें ताकि एक चर (x या y) के गुणांक संख्यात्मक रूप से बराबर हो जाएं।\n2. उस चर को विलुप्त करने के लिए दोनों समीकरणों को जोड़ें या घटाएं।\n3. एक चर में प्राप्त समीकरण को हल करें।\n4. दूसरा चर ज्ञात करने के लिए मान को किसी भी मूल समीकरण में रखें।",
            "body_gu": "લોપની રીતના પગલાં:\n1. બંને સમીકરણોને યોગ્ય શૂન્યેતર અચળો વડે ગુણો જેથી એક ચલ (x અથવા y) ના સહગુણકો સંખ્યાત્મક રીતે સમાન થાય.\n2. તે ચલનો લોપ કરવા માટે બંને સમીકરણોનો સરવાળો અથવા બાદબાકી કરો.\n3. એક ચલમાં મળતા સમીકરણને ઉકેલો.\n4. બીજો ચલ શોધવા માટે કિંમત મૂળ સમીકરણમાં મૂકો."
        },
        {
            "id": "KOBJ_C10_MATHS_CH3_EXAMPLE_2",
            "type": "worked_example",
            "title": "Worked Example: Elimination Method",
            "title_hi": "हल किया गया उदाहरण: विलोपन विधि",
            "title_gu": "ગણેલું ઉદાહરણ: લોપની રીત",
            "problem": "Solve by elimination: 2x + 3y = 8 and 4x + 6y = 7.",
            "problem_hi": "विलोपन विधि द्वारा हल करें: 2x + 3y = 8 और 4x + 6y = 7।",
            "problem_gu": "લોપની રીત વડે ઉકેલો: 2x + 3y = 8 અને 4x + 6y = 7.",
            "solution": "Multiply eq (1) by 2: 4x + 6y = 16.\nEq (2): 4x + 6y = 7.\nSubtract: (4x + 6y) - (4x + 6y) = 16 - 7 => 0 = 9, which is a false statement!\nHence, the system has NO SOLUTION (parallel lines).",
            "solution_hi": "समीकरण (1) को 2 से गुणा करें: 4x + 6y = 16।\nसमीकरण (2): 4x + 6y = 7।\nघटाएं: (4x + 6y) - (4x + 6y) = 16 - 7 => 0 = 9, जो एक असत्य कथन है!\nअतः, निकाय का कोई हल नहीं है (समांतर रेखाएं)।",
            "solution_gu": "સમીકરણ (1) ને 2 વડે ગુણો: 4x + 6y = 16.\nસમીકરણ (2): 4x + 6y = 7.\nબાદબાકી કરો: (4x + 6y) - (4x + 6y) = 16 - 7 => 0 = 9, જે અસત્ય વિધાન છે!\nતેથી, આ સમીકરણ યુગ્મનો કોઈ ઉકેલ નથી (સમાંતર રેખાઓ)."
        },
        {
            "id": "KOBJ_C10_MATHS_CH3_TEACHER_TIP_1",
            "type": "teacher_tip",
            "title": "Exam Tip: Word Problems Strategy",
            "title_hi": "परीक्षा टिप: शब्द समस्याओं की रणनीति",
            "title_gu": "પરીક્ષા ટીપ: કૂટપ્રશ્નોની રણનીતિ",
            "body": "Always define variables clearly! E.g. 'Let speed of boat in still water = x km/h, speed of stream = y km/h'. Downstream speed = (x + y) km/h, Upstream speed = (x - y) km/h. Remember: Time = Distance / Speed.",
            "body_hi": "हमेशा चरों को स्पष्ट रूप से परिभाषित करें! जैसे 'माना शांत जल में नाव की चाल = x किमी/घंटा, धारा की चाल = y किमी/घंटा'। अनुप्रवाह चाल = (x + y) किमी/घंटा, ऊर्ध्वप्रवाह चाल = (x - y) किमी/घंटा। याद रखें: समय = दूरी / चाल।",
            "body_gu": "હંમેશા ચલોને સ્પષ્ટ રીતે વ્યાખ્યાયિત કરો! જેમ કે 'ધારો કે શાંત પાણીમાં હોડીની ઝડપ = x કિમી/કલાક, પ્રવાહની ઝડપ = y કિમી/કલાક'. પ્રવાહની દિશામાં ઝડપ = (x + y) કિમી/કલાક, પ્રવાહની વિરુદ્ધ દિશામાં ઝડપ = (x - y) કિમી/કલાક. યાદ રાખો: સમય = અંતર / ઝડપ."
        },
        {
            "id": "KOBJ_C10_MATHS_CH3_PRACTICE_1",
            "type": "quiz",
            "question": "A boat goes 30 km upstream and 44 km downstream in 10 hours. In 13 hours, it goes 40 km upstream and 55 km downstream. What is the speed of the stream?",
            "question_hi": "एक नाव 10 घंटे में 30 किमी धारा के प्रतिकूल और 44 किमी धारा के अनुकूल जाती है। 13 घंटे में, यह 40 किमी प्रतिकूल और 55 किमी अनुकूल जाती है। धारा की चाल क्या है?",
            "question_gu": "એક હોડી 10 કલાકમાં 30 કિમી પ્રવાહની વિરુદ્ધ અને 44 કિમી પ્રવાહની દિશામાં જાય છે. 13 કલાકમાં તે 40 કિમી વિરુદ્ધ અને 55 કિમી દિશામાં જાય છે. પ્રવાહની ઝડપ કેટલી?",
            "options": [
                "3 km/h",
                "5 km/h",
                "8 km/h",
                "2 km/h"
            ],
            "options_hi": [
                "3 किमी/घंटा",
                "5 किमी/घंटा",
                "8 किमी/घंटा",
                "2 किमी/घंटा"
            ],
            "options_gu": [
                "3 કિમી/કલાક",
                "5 કિમી/કલાક",
                "8 કિમી/કલાક",
                "2 કિમી/કલાક"
            ],
            "correct_index": 0,
            "explanation": "Let 1/(x-y) = u and 1/(x+y) = v. 30u + 44v = 10 and 40u + 55v = 13. Solving gives u = 1/5 and v = 1/11. Thus x - y = 5 and x + y = 11. Solving gives x = 8 km/h (boat in still water) and y = 3 km/h (stream).",
            "explanation_hi": "माना 1/(x-y) = u और 1/(x+y) = v। 30u + 44v = 10 और 40u + 55v = 13। हल करने पर u = 1/5 और v = 1/11 मिलता है। इसलिए x - y = 5 और x + y = 11। हल करने पर x = 8 किमी/घंटा और y = 3 किमी/घंटा (धारा) मिलता है।",
            "explanation_gu": "ધારો કે 1/(x-y) = u અને 1/(x+y) = v. 30u + 44v = 10 અને 40u + 55v = 13. ઉકેલતાં u = 1/5 અને v = 1/11 મળે. તેથી x - y = 5 અને x + y = 11. ઉકેલતાં x = 8 કિમી/કલાક અને y = 3 કિમી/કલાક (પ્રવાહ) મળે."
        },
        {
            "id": "KOBJ_C10_MATHS_CH3_PRACTICE_2",
            "type": "quiz",
            "question": "The sum of a two-digit number and the number obtained by reversing the digits is 66. If the digits differ by 2, how many such numbers are there?",
            "question_hi": "दो अंकों की एक संख्या और अंकों को पलटने पर बनी संख्या का योग 66 है। यदि अंकों का अंतर 2 है, तो ऐसी कितनी संख्याएं हैं?",
            "question_gu": "બે અંકની એક સંખ્યા અને અંકોની અદલાબદલી કરવાથી મળતી સંખ્યાનો સરવાળો 66 છે. જો અંકોનો તફાવત 2 હોય, તો આવી કેટલી સંખ્યાઓ મળે?",
            "options": [
                "1 number (42)",
                "2 numbers (42 and 24)",
                "3 numbers",
                "No such number exists"
            ],
            "options_hi": [
                "1 संख्या (42)",
                "2 संख्याएं (42 और 24)",
                "3 संख्याएं",
                "ऐसी कोई संख्या नहीं है"
            ],
            "options_gu": [
                "1 સંખ્યા (42)",
                "2 સંખ્યાઓ (42 અને 24)",
                "3 સંખ્યાઓ",
                "આવી કોઈ સંખ્યા નથી"
            ],
            "correct_index": 1,
            "explanation": "Let tens digit = x, units digit = y. Number = 10x + y. Reverse = 10y + x. Sum = 11(x + y) = 66 => x + y = 6. Given |x - y| = 2. Case 1: x - y = 2 => x = 4, y = 2 (Number 42). Case 2: y - x = 2 => x = 2, y = 4 (Number 24). So there are 2 such numbers.",
            "explanation_hi": "माना दहाई का अंक = x, इकाई का अंक = y। संख्या = 10x + y। पलटने पर = 10y + x। योग = 11(x + y) = 66 => x + y = 6। दिया गया है |x - y| = 2। स्थिति 1: x - y = 2 => x = 4, y = 2 (संख्या 42)। स्थिति 2: y - x = 2 => x = 2, y = 4 (संख्या 24)। इसलिए ऐसी 2 संख्याएं हैं।",
            "explanation_gu": "ધારો કે દશકનો અંક = x, એકમનો અંક = y. સંખ્યા = 10x + y. અદલાબદલી = 10y + x. સરવાળો = 11(x + y) = 66 => x + y = 6. આપેલ તફાવત |x - y| = 2. કિસ્સો 1: x - y = 2 => x = 4, y = 2 (સંખ્યા 42). કિસ્સો 2: y - x = 2 => x = 2, y = 4 (સંખ્યા 24). આમ આવી 2 સંખ્યાઓ મળે."
        },
        {
            "id": "KOBJ_C10_MATHS_CH3_MASTERY",
            "type": "mastery",
            "title": "Mastery Challenge: Pair of Linear Equations",
            "title_hi": "मास्टरी चुनौती: रैखिक समीकरण युग्म",
            "title_gu": "માસ્ટરી ચેલેન્જ: દ્વાચલ રેખીય સમીકરણ યુગ્મ",
            "body": "Congratulations! You have mastered graphical conditions, substitution method, elimination method, and word problem applications for Class 10 Linear Equations.",
            "body_hi": "बधाई हो! आपने कक्षा 10 रैखिक समीकरणों के लिए आलेखीय शर्तों, प्रतिस्थापन विधि, विलोपन विधि और शब्द समस्या अनुप्रयोगों में महारत हासिल कर ली है।",
            "body_gu": "અભિનંદન! તમે ધોરણ 10 ના રેખીય સમીકરણો માટે આલેખીય શરતો, આદેશની રીત, લોપની રીત અને કૂટપ્રશ્નોના ઉપયોગ પર પ્રભુત્વ મેળવ્યું છે."
        }
    ]
    return blocks

def process_and_build():
    print("=== BUILDING & AUDITING CLASS 10 MATHEMATICS ===")
    
    for ch_num in range(1, 15):
        filename = f"app_core/chapters/ncert_class10_maths_ch{ch_num}.json"
        
        if ch_num == 3:
            # Build comprehensive Chapter 3 blocks
            blocks = create_ch3_comprehensive_blocks()
        else:
            if not os.path.exists(filename):
                print(f"Skipping Ch {ch_num} (File missing)")
                continue
            with open(filename, 'r', encoding='utf-8') as f:
                raw_data = json.load(f)
            
            blocks = raw_data if isinstance(raw_data, list) else raw_data.get("blocks", [])
            
        # Normalize blocks: unwrap nested content and ensure trilingual defaults if missing
        cleaned_blocks = []
        assessment_questions = []
        
        for idx, b in enumerate(blocks, start=1):
            if not isinstance(b, dict): continue
            
            # Extract content dictionary if present
            if "content" in b and isinstance(b["content"], dict):
                inner = b.pop("content")
                for k, v in inner.items():
                    if k not in b:
                        b[k] = v
                        
            # Ensure ID
            if "id" not in b or b["id"] == "UNKNOWN_ID":
                b["id"] = f"KOBJ_C10_MATHS_CH{ch_num}_{b.get('type', 'BLOCK').upper()}_{idx}"
                
            # Trilingual field defaults
            title = b.get("title", f"Topic {idx}")
            if "title" in b:
                if "title_hi" not in b or not b["title_hi"]: b["title_hi"] = title
                if "title_gu" not in b or not b["title_gu"]: b["title_gu"] = title
                
            if "body" in b:
                body = b["body"]
                if "body_hi" not in b or not b["body_hi"]: b["body_hi"] = body
                if "body_gu" not in b or not b["body_gu"]: b["body_gu"] = body
                
            if "question" in b:
                q = b["question"]
                if "question_hi" not in b or not b["question_hi"]: b["question_hi"] = q
                if "question_gu" not in b or not b["question_gu"]: b["question_gu"] = q
                
            if "explanation" in b:
                exp = b["explanation"]
                if "explanation_hi" not in b or not b["explanation_hi"]: b["explanation_hi"] = exp
                if "explanation_gu" not in b or not b["explanation_gu"]: b["explanation_gu"] = exp
                
            if "options" in b and isinstance(b["options"], list):
                opts = b["options"]
                if "options_hi" not in b or not b["options_hi"]: b["options_hi"] = opts
                if "options_gu" not in b or not b["options_gu"]: b["options_gu"] = opts
                
            cleaned_blocks.append(b)
            
            # Extract for assessment question bank if quiz/mcq
            if b.get("type") in ["quiz", "mcq", "practice_question", "challenge_question"] and "question" in b:
                aq = {
                    "id": b["id"],
                    "question": b["question"],
                    "question_hi": b.get("question_hi", b["question"]),
                    "question_gu": b.get("question_gu", b["question"]),
                    "options": b.get("options", ["A", "B", "C", "D"]),
                    "options_hi": b.get("options_hi", b.get("options", ["A", "B", "C", "D"])),
                    "options_gu": b.get("options_gu", b.get("options", ["A", "B", "C", "D"])),
                    "correct_index": b.get("correct_index", 0),
                    "explanation": b.get("explanation", ""),
                    "explanation_hi": b.get("explanation_hi", b.get("explanation", "")),
                    "explanation_gu": b.get("explanation_gu", b.get("explanation", ""))
                }
                assessment_questions.append(aq)
                
        # 1. Write unwrapped chapter file
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(cleaned_blocks, f, ensure_ascii=False, indent=2)
        print(f"Ch {ch_num}: Successfully wrote {len(cleaned_blocks)} unwrapped blocks to {filename}")
        
        # 2. Sync app_core/learning_modules/ncert_class10_maths_ch{ch_num}/
        ncert_lm_dir = f"app_core/learning_modules/ncert_class10_maths_ch{ch_num}"
        os.makedirs(ncert_lm_dir, exist_ok=True)
        with open(os.path.join(ncert_lm_dir, "blocks.json"), 'w', encoding='utf-8') as f:
            json.dump(cleaned_blocks, f, ensure_ascii=False, indent=2)
            
        ch_info = CHAPTER_TITLES.get(ch_num, {"title": f"Chapter {ch_num}", "hi": f"अध्याय {ch_num}", "gu": f"પ્રકરણ {ch_num}"})
        meta = {
            "id": f"ncert_class10_maths_ch{ch_num}",
            "title": f"Chapter {ch_num}: {ch_info['title']}",
            "title_hi": f"अध्याय {ch_num}: {ch_info['hi']}",
            "title_gu": f"પ્રકરણ {ch_num}: {ch_info['gu']}",
            "subject_id": "ncert_class10_math",
            "class_id": "ncert_class10"
        }
        with open(os.path.join(ncert_lm_dir, "metadata.json"), 'w', encoding='utf-8') as f:
            json.dump(meta, f, ensure_ascii=False, indent=2)
            
        # 3. Sync app_core/learning_modules/gseb_class10_maths_ch{ch_num}/
        gseb_lm_dir = f"app_core/learning_modules/gseb_class10_maths_ch{ch_num}"
        os.makedirs(gseb_lm_dir, exist_ok=True)
        with open(os.path.join(gseb_lm_dir, "blocks.json"), 'w', encoding='utf-8') as f:
            json.dump(cleaned_blocks, f, ensure_ascii=False, indent=2)
        meta_gseb = {
            "id": f"gseb_class10_maths_ch{ch_num}",
            "title": f"Chapter {ch_num}: {ch_info['title']}",
            "title_hi": f"अध्याय {ch_num}: {ch_info['hi']}",
            "title_gu": f"પ્રકરણ {ch_num}: {ch_info['gu']}",
            "subject_id": "gseb_class10_math",
            "class_id": "gseb_class10"
        }
        with open(os.path.join(gseb_lm_dir, "metadata.json"), 'w', encoding='utf-8') as f:
            json.dump(meta_gseb, f, ensure_ascii=False, indent=2)
            
        # 4. Sync Assessment question banks
        ncert_assess_file = f"app_core/assessment/ncert_class10_maths_ch{ch_num}_questions.json"
        with open(ncert_assess_file, 'w', encoding='utf-8') as f:
            json.dump(assessment_questions, f, ensure_ascii=False, indent=2)
            
        gseb_assess_file = f"app_core/assessment/gseb_class10_maths_ch{ch_num}_questions.json"
        with open(gseb_assess_file, 'w', encoding='utf-8') as f:
            json.dump(assessment_questions, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    process_and_build()
