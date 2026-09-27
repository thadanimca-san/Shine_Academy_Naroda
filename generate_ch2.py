import json
import os

def create_block(b_type, b_id, title_en, title_hi, title_gu, body_en, body_hi, body_gu, extra=None):
    b = {
        "type": b_type,
        "id": b_id,
        "title": title_en,
        "title_hi": title_hi,
        "title_gu": title_gu,
        "body": body_en,
        "body_hi": body_hi,
        "body_gu": body_gu
    }
    if extra:
        b.update(extra)
    return b

def create_mcq(b_id, q_en, q_hi, q_gu, opt_en, opt_hi, opt_gu, correct, exp_en, exp_hi, exp_gu):
    return {
        "type": "mcq",
        "id": b_id,
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

def create_worked_example(b_id, title_en, title_hi, title_gu, q_en, q_hi, q_gu, sol_en, sol_hi, sol_gu):
    return {
        "type": "worked_example",
        "id": b_id,
        "title": title_en,
        "title_hi": title_hi,
        "title_gu": title_gu,
        "question": q_en,
        "question_hi": q_hi,
        "question_gu": q_gu,
        "solution": sol_en,
        "solution_hi": sol_hi,
        "solution_gu": sol_gu
    }

blocks = []

# 8-step cycle for Polynomials introduction
blocks.append(create_block("hook", "KOBJ_CLASS10_MATH_CH2_01", 
    "The Rollercoaster Ride", "रोलरकोस्टर की सवारी", "રોલરકોસ્ટરની સવારી",
    "Have you ever seen the track of a rollercoaster? It goes up, comes down, and twists around. Believe it or not, mathematicians use special mathematical expressions to design these smooth curves. Let's find out how!",
    "क्या आपने कभी रोलरकोस्टर का ट्रैक देखा है? यह ऊपर जाता है, नीचे आता है, और चारों ओर घूमता है। मानो या न मानो, गणितज्ञ इन घुमावदार पटरियों को डिजाइन करने के लिए विशेष गणितीय व्यंजकों का उपयोग करते हैं। आइए जानें कैसे!",
    "શું તમે ક્યારેય રોલરકોસ્ટરનો ટ્રેક જોયો છે? તે ઉપર જાય છે, નીચે આવે છે, અને આસપાસ વળે છે. માનો કે ન માનો, ગણિતશાસ્ત્રીઓ આ સરળ વળાંકોને ડિઝાઇન કરવા માટે ખાસ ગાણિતિક સમીકરણોનો ઉપયોગ કરે છે. ચાલો જાણીએ કેવી રીતે!"
))

blocks.append(create_mcq("KOBJ_CLASS10_MATH_CH2_02",
    "If a car travels along a path represented by y = x² - 4, and the x-axis represents the ground, how many times will the car touch the ground?",
    "यदि कोई कार y = x² - 4 द्वारा दर्शाए गए पथ पर यात्रा करती है, और x-अक्ष जमीन का प्रतिनिधित्व करता है, तो कार कितनी बार जमीन को छुएगी?",
    "જો કોઈ કાર y = x² - 4 દ્વારા દર્શાવેલ માર્ગ પર મુસાફરી કરે છે, અને x-અક્ષ જમીનનું પ્રતિનિધિત્વ કરે છે, તો કાર કેટલી વાર જમીનને સ્પર્શ કરશે?",
    ["0 times", "1 time", "2 times", "3 times"],
    ["0 बार", "1 बार", "2 बार", "3 बार"],
    ["0 વખત", "1 વખત", "2 વખત", "3 વખત"],
    2,
    "The equation x² - 4 becomes 0 at x = 2 and x = -2. So, it touches the ground 2 times.",
    "समीकरण x² - 4, x = 2 और x = -2 पर 0 हो जाता है। इसलिए, यह जमीन को 2 बार छूता है।",
    "સમીકરણ x² - 4, x = 2 અને x = -2 પર 0 બને છે. તેથી, તે જમીનને 2 વખત સ્પર્શ કરે છે."
))

blocks.append(create_block("discovery", "KOBJ_CLASS10_MATH_CH2_03",
    "Visualizing the Math", "गणित की कल्पना करना", "ગણિતની કલ્પના કરવી",
    "Imagine throwing a ball in the air. The path it takes is a curve. We can represent this path using an algebraic expression with variables and powers. These expressions are called Polynomials. The highest power of the variable decides the shape of the curve!",
    "हवा में एक गेंद उछालने की कल्पना करें। इसका पथ एक वक्र (curve) होता है। हम चर और घात वाले बीजगणितीय व्यंजक का उपयोग करके इस पथ का प्रतिनिधित्व कर सकते हैं। इन व्यंजकों को बहुपद (Polynomials) कहा जाता है। चर की सबसे बड़ी घात वक्र का आकार तय करती है!",
    "હવામાં બોલ ફેંકવાની કલ્પના કરો. તે જે માર્ગ લે છે તે એક વળાંક છે. આપણે ચલ અને ઘાતવાળા બીજગણિતીય સમીકરણનો ઉપયોગ કરીને આ માર્ગનું પ્રતિનિધિત્વ કરી શકીએ છીએ. આ સમીકરણોને બહુપદી (Polynomials) કહેવામાં આવે છે. ચલની સૌથી મોટી ઘાત વળાંકનો આકાર નક્કી કરે છે!"
))

blocks.append(create_block("theory", "KOBJ_CLASS10_MATH_CH2_04",
    "What is a Polynomial?", "बहुपद क्या है?", "બહુપદી શું છે?",
    "A polynomial is an expression consisting of variables and coefficients, that involves only the operations of addition, subtraction, multiplication, and non-negative integer exponents of variables. For example, 2x² - 3x + 4. The highest power of x in p(x) is called the degree of the polynomial.",
    "बहुपद एक ऐसा व्यंजक है जिसमें चर और गुणांक होते हैं, जिसमें केवल जोड़, घटाव, गुणा और चरों के गैर-ऋणात्मक पूर्णांक घातांक शामिल होते हैं। उदाहरण के लिए, 2x² - 3x + 4। p(x) में x की अधिकतम घात को बहुपद की घात (degree) कहा जाता है।",
    "બહુપદી એ એક એવું સમીકરણ છે જેમાં ચલ અને સહગુણકો હોય છે, જેમાં માત્ર સરવાળો, બાદબાકી, ગુણાકાર અને ચલોના બિન-ઋણાત્મક પૂર્ણાંક ઘાતાંક સામેલ હોય છે. ઉદાહરણ તરીકે, 2x² - 3x + 4. p(x) માં x ની મહત્તમ ઘાતને બહુપદીની ઘાત (degree) કહેવામાં આવે છે."
))

blocks.append(create_mcq("KOBJ_CLASS10_MATH_CH2_05",
    "Which of the following is NOT a polynomial?",
    "निम्नलिखित में से कौन सा बहुपद नहीं है?",
    "નીચેનામાંથી કયું બહુપદી નથી?",
    ["x² + 2x + 1", "3x³ - 5", "x + 1/x", "5"],
    ["x² + 2x + 1", "3x³ - 5", "x + 1/x", "5"],
    ["x² + 2x + 1", "3x³ - 5", "x + 1/x", "5"],
    2,
    "In x + 1/x, the term 1/x is x⁻¹. The exponent is negative (-1), so it is not a polynomial.",
    "x + 1/x में, पद 1/x का मतलब x⁻¹ है। घातांक ऋणात्मक (-1) है, इसलिए यह बहुपद नहीं है।",
    "x + 1/x માં, પદ 1/x નો અર્થ x⁻¹ છે. ઘાતાંક ઋણાત્મક (-1) છે, તેથી તે બહુપદી નથી."
))

blocks.append(create_block("reflection", "KOBJ_CLASS10_MATH_CH2_06",
    "Reflect on Degrees", "घात पर चिंतन", "ઘાત પર પ્રતિબિંબ",
    "Look around your room. If a straight line has degree 1 (linear), and a parabola has degree 2 (quadratic), can you think of any physical object that might require a degree 3 (cubic) equation to describe its shape?",
    "अपने कमरे के चारों ओर देखें। यदि एक सीधी रेखा की घात 1 (रैखिक) है, और एक परवलय (parabola) की घात 2 (द्विघात) है, तो क्या आप किसी ऐसी भौतिक वस्तु के बारे में सोच सकते हैं जिसके आकार का वर्णन करने के लिए 3 घात (त्रिघात) वाले समीकरण की आवश्यकता हो सकती है?",
    "તમારા રૂમની આસપાસ જુઓ. જો સીધી રેખાની ઘાત 1 (સુરેખ) હોય, અને પેરાબોલાની ઘાત 2 (દ્વિઘાત) હોય, તો શું તમે એવી કોઈ ભૌતિક વસ્તુ વિશે વિચારી શકો છો જેના આકારનું વર્ણન કરવા માટે 3 ઘાત (ત્રિઘાત) વાળા સમીકરણની જરૂર પડી શકે છે?"
))

blocks.append(create_block("theory", "KOBJ_CLASS10_MATH_CH2_07",
    "Geometric Meaning of the Zeroes of a Polynomial", "बहुपद के शून्यकों का ज्यामितीय अर्थ", "બહુપદીના શૂન્યોનો ભૌમિતિક અર્થ",
    "The zeroes of a polynomial p(x) are precisely the x-coordinates of the points, where the graph of y = p(x) intersects the x-axis. A linear polynomial has at most one zero. A quadratic polynomial has at most two zeroes. A cubic polynomial has at most three zeroes.",
    "बहुपद p(x) के शून्यक वास्तव में उन बिंदुओं के x-निर्देशांक होते हैं, जहाँ y = p(x) का ग्राफ x-अक्ष को काटता है। एक रैखिक बहुपद का अधिकतम एक शून्यक होता है। एक द्विघात बहुपद के अधिकतम दो शून्यक होते हैं। एक त्रिघात बहुपद के अधिकतम तीन शून्यक होते हैं।",
    "બહુપદી p(x) ના શૂન્યો એ ચોક્કસપણે એવા બિંદુઓના x-યામ છે, જ્યાં y = p(x) નો આલેખ x-અક્ષને છેદે છે. સુરેખ બહુપદીમાં વધુમાં વધુ એક શૂન્ય હોય છે. દ્વિઘાત બહુપદીમાં વધુમાં વધુ બે શૂન્યો હોય છે. ત્રિઘાત બહુપદીમાં વધુમાં વધુ ત્રણ શૂન્યો હોય છે."
))

blocks.append(create_block("mastery", "KOBJ_CLASS10_MATH_CH2_08",
    "Mastery: Graph Analysis", "महारत: ग्राफ विश्लेषण", "માસ્ટરી: ગ્રાફ વિશ્લેષણ",
    "If I show you a graph of y = p(x) that crosses the x-axis at x = -3, x = 1, and x = 4, what is the minimum degree of this polynomial? It must be at least 3 (cubic) because it has 3 zeroes!",
    "यदि मैं आपको y = p(x) का एक ग्राफ दिखाऊं जो x-अक्ष को x = -3, x = 1 और x = 4 पर पार करता है, तो इस बहुपद की न्यूनतम घात क्या है? यह कम से कम 3 (त्रिघात) होना चाहिए क्योंकि इसके 3 शून्यक हैं!",
    "જો હું તમને y = p(x) નો ગ્રાફ બતાવું જે x-અક્ષને x = -3, x = 1 અને x = 4 પર પાર કરે છે, તો આ બહુપદીની ન્યૂનતમ ઘાત શું છે? તે ઓછામાં ઓછું 3 (ત્રિઘાત) હોવું જોઈએ કારણ કે તેમાં 3 શૂન્યો છે!"
))

# Exercise 2.1 Questions as MCQs
ex21_graphs = [
    (0, "A straight line parallel to the x-axis.", "x-अक्ष के समानांतर एक सीधी रेखा।", "x-અક્ષને સમાંતર એક સીધી રેખા."),
    (1, "A curve intersecting the x-axis at exactly one point.", "एक वक्र जो x-अक्ष को ठीक एक बिंदु पर प्रतिच्छेद करता है।", "એક વળાંક જે x-અક્ષને બરાબર એક બિંદુ પર છેદે છે."),
    (3, "A curve intersecting the x-axis at three points.", "एक वक्र जो x-अक्ष को तीन बिंदुओं पर प्रतिच्छेद करता है।", "એક વળાંક જે x-અક્ષને ત્રણ બિંદુઓ પર છેદે છે."),
    (2, "A parabola intersecting the x-axis at two points.", "एक परवलय जो x-अक्ष को दो बिंदुओं पर प्रतिच्छेद करता है।", "એક પેરાબોલા જે x-અક્ષને બે બિંદુઓ પર છેદે છે."),
    (4, "A curve intersecting the x-axis at four points.", "एक वक्र जो x-अक्ष को चार बिंदुओं पर प्रतिच्छेद करता है।", "એક વળાંક જે x-અક્ષને ચાર બિંદુઓ પર છેદે છે."),
    (3, "A curve intersecting the x-axis at one point and touching it at two other points.", "एक वक्र जो x-अक्ष को एक बिंदु पर काटता है और दो अन्य बिंदुओं पर छूता है।", "એક વળાંક જે x-અક્ષને એક બિંદુ પર કાપે છે અને અન્ય બે બિંદુઓ પર સ્પર્શ કરે છે.")
]

for i, (ans, desc_en, desc_hi, desc_gu) in enumerate(ex21_graphs):
    idx = str(i+1).zfill(2)
    q_en = f"Exercise 2.1 - Q1({i+1}): The graph of y = p(x) is given. The graph is described as: {desc_en} Find the number of zeroes of p(x)."
    q_hi = f"प्रश्नावली 2.1 - Q1({i+1}): y = p(x) का ग्राफ दिया गया है। ग्राफ का वर्णन इस प्रकार है: {desc_hi} p(x) के शून्यकों की संख्या ज्ञात कीजिए।"
    q_gu = f"સ્વાધ્યાય 2.1 - Q1({i+1}): y = p(x) નો આલેખ આપેલ છે. આલેખનું વર્ણન આ પ્રમાણે છે: {desc_gu} p(x) ના શૂન્યોની સંખ્યા શોધો."
    
    opts = ["0", "1", "2", "3", "4"]
    corr = opts.index(str(ans))
    
    blocks.append(create_mcq(f"KOBJ_CLASS10_MATH_CH2_EX21_{idx}",
        q_en, q_hi, q_gu,
        opts, opts, opts, corr,
        f"The number of zeroes is {ans} because the graph intersects the x-axis at {ans} point(s).",
        f"शून्यकों की संख्या {ans} है क्योंकि ग्राफ x-अक्ष को {ans} बिंदु(ओं) पर प्रतिच्छेद करता है।",
        f"શૂન્યોની સંખ્યા {ans} છે કારણ કે આલેખ x-અક્ષને {ans} બિંદુ(ઓ) પર છેદે છે."
    ))

# Concept 2: Relationship between Zeroes and Coefficients
blocks.append(create_block("theory", "KOBJ_CLASS10_MATH_CH2_09",
    "Relationship between Zeroes and Coefficients", "शून्यकों और गुणांकों के बीच संबंध", "શૂન્યો અને સહગુણકો વચ્ચેનો સંબંધ",
    "For a quadratic polynomial ax² + bx + c, if α and β are its zeroes, then:\nSum of zeroes (α + β) = -b/a = -(Coefficient of x) / (Coefficient of x²)\nProduct of zeroes (αβ) = c/a = (Constant term) / (Coefficient of x²)",
    "द्विघात बहुपद ax² + bx + c के लिए, यदि α और β इसके शून्यक हैं, तो:\nशून्यकों का योग (α + β) = -b/a = -(x का गुणांक) / (x² का गुणांक)\nशून्यकों का गुणनफल (αβ) = c/a = (अचर पद) / (x² का गुणांक)",
    "દ્વિઘાત બહુપદી ax² + bx + c માટે, જો α અને β તેના શૂન્યો હોય, તો:\nશૂન્યોનો સરવાળો (α + β) = -b/a = -(x નો સહગુણક) / (x² નો સહગુણક)\nશૂન્યોનો ગુણાકાર (αβ) = c/a = (અચળ પદ) / (x² નો સહગુણક)"
))

# Exercise 2.2 Q1
ex22_q1 = [
    ("x² - 2x - 8", "(x - 4)(x + 2)", "4, -2", "2", "-8", 1),
    ("4s² - 4s + 1", "(2s - 1)²", "1/2, 1/2", "1", "1/4", 2),
    ("6x² - 3 - 7x", "6x² - 7x - 3 = (3x + 1)(2x - 3)", "3/2, -1/3", "7/6", "-1/2", 3),
    ("4u² + 8u", "4u(u + 2)", "0, -2", "-2", "0", 4),
    ("t² - 15", "(t - √15)(t + √15)", "√15, -√15", "0", "-15", 5),
    ("3x² - x - 4", "(3x - 4)(x + 1)", "4/3, -1", "1/3", "-4/3", 6)
]

for i, (poly, fact, zeroes, sum_z, prod_z, idx) in enumerate(ex22_q1):
    blocks.append(create_worked_example(f"KOBJ_CLASS10_MATH_CH2_EX22_1_{idx}",
        f"Exercise 2.2 - Q1({idx})", f"प्रश्नावली 2.2 - Q1({idx})", f"સ્વાધ્યાય 2.2 - Q1({idx})",
        f"Find the zeroes of the quadratic polynomial {poly} and verify the relationship between the zeroes and the coefficients.",
        f"द्विघात बहुपद {poly} के शून्यक ज्ञात कीजिए और शून्यकों तथा गुणांकों के बीच संबंध की सत्यता की जाँच कीजिए।",
        f"દ્વિઘાત બહુપદી {poly} ના શૂન્યો શોધો અને શૂન્યો અને સહગુણકો વચ્ચેના સંબંધની ચકાસણી કરો.",
        f"p(x) = {poly}\nTo find zeroes, put p(x) = 0.\n{poly} = 0\nFactors: {fact} = 0\nZeroes (α, β) = {zeroes}\nSum of zeroes = α + β = {sum_z}. Also, -b/a = {sum_z}.\nProduct of zeroes = αβ = {prod_z}. Also, c/a = {prod_z}.\nHence verified.",
        f"p(x) = {poly}\nशून्यक ज्ञात करने के लिए, p(x) = 0 रखें।\n{poly} = 0\nगुणनखंड: {fact} = 0\nशून्यक (α, β) = {zeroes}\nशून्यकों का योग = α + β = {sum_z}. और, -b/a = {sum_z}.\nशून्यकों का गुणनफल = αβ = {prod_z}. और, c/a = {prod_z}.\nअतः सत्यापित हुआ।",
        f"p(x) = {poly}\nશૂન્યો શોધવા માટે, p(x) = 0 મૂકો.\n{poly} = 0\nઅવયવો: {fact} = 0\nશૂન્યો (α, β) = {zeroes}\nશૂન્યોનો સરવાળો = α + β = {sum_z}. અને, -b/a = {sum_z}.\nશૂન્યોનો ગુણાકાર = αβ = {prod_z}. અને, c/a = {prod_z}.\nઆમ ચકાસણી થઈ."
    ))

# Exercise 2.2 Q2
ex22_q2 = [
    ("1/4", "-1", "k(4x² - x - 4)", 1),
    ("√2", "1/3", "k(3x² - 3√2x + 1)", 2),
    ("0", "√5", "k(x² + √5)", 3),
    ("1", "1", "k(x² - x + 1)", 4),
    ("-1/4", "1/4", "k(4x² + x + 1)", 5),
    ("4", "1", "k(x² - 4x + 1)", 6)
]

for i, (sum_z, prod_z, ans, idx) in enumerate(ex22_q2):
    blocks.append(create_worked_example(f"KOBJ_CLASS10_MATH_CH2_EX22_2_{idx}",
        f"Exercise 2.2 - Q2({idx})", f"प्रश्नावली 2.2 - Q2({idx})", f"સ્વાધ્યાય 2.2 - Q2({idx})",
        f"Find a quadratic polynomial each with the given numbers as the sum and product of its zeroes respectively: {sum_z}, {prod_z}",
        f"एक द्विघात बहुपद ज्ञात कीजिए जिसके शून्यकों के योग तथा गुणनफल क्रमशः दी गई संख्याएँ हैं: {sum_z}, {prod_z}",
        f"એક દ્વિઘાત બહુપદી શોધો જેના શૂન્યોનો સરવાળો અને ગુણાકાર અનુક્રમે આપેલ સંખ્યાઓ છે: {sum_z}, {prod_z}",
        f"Let the polynomial be ax² + bx + c, and its zeroes be α and β.\nGiven: α + β = {sum_z} = -b/a, and αβ = {prod_z} = c/a.\nA quadratic polynomial is given by k(x² - (sum)x + product).\nSo, p(x) = k(x² - ({sum_z})x + ({prod_z})).\nBy taking suitable k to clear denominators, we get the polynomial as {ans}.",
        f"मान लीजिए कि बहुपद ax² + bx + c है, और इसके शून्यक α और β हैं।\nदिया गया है: α + β = {sum_z} = -b/a, और αβ = {prod_z} = c/a.\nएक द्विघात बहुपद k(x² - (योग)x + गुणनफल) द्वारा दिया जाता है।\nइसलिए, p(x) = k(x² - ({sum_z})x + ({prod_z}))।\nहर (denominator) को हटाने के लिए उपयुक्त k लेने पर, हमें बहुपद {ans} प्राप्त होता है।",
        f"ધારો કે બહુપદી ax² + bx + c છે, અને તેના શૂન્યો α અને β છે.\nઆપેલ છે: α + β = {sum_z} = -b/a, અને αβ = {prod_z} = c/a.\nદ્વિઘાત બહુપદી k(x² - (સરવાળો)x + ગુણાકાર) દ્વારા આપવામાં આવે છે.\nતેથી, p(x) = k(x² - ({sum_z})x + ({prod_z})).\nછેદ દૂર કરવા માટે યોગ્ય k લેવાથી, આપણને બહુપદી {ans} મળે છે."
    ))

chapter = {
    "metadata": {
        "title": "Polynomials",
        "subject": "Maths",
        "grade": "10",
        "curriculum": ["GSEB", "NCERT", "CBSE"],
        "difficulty": "Intermediate",
        "version": "4.0.0",
        "id": "cbse_class10_maths_ch2"
    },
    "blocks": blocks
}

with open("app_core/chapters/ncert_class10_maths_ch2.json", "w", encoding="utf-8") as f:
    json.dump(chapter, f, ensure_ascii=False, indent=2)

print("JSON generation complete.")
