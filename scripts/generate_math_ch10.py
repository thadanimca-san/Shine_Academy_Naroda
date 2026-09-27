import json
import math

blocks = []
block_counter = 1

def generate_id():
    global block_counter
    bid = f"KOBJ_CLASS10_MATH_CH10_B{block_counter:03d}"
    block_counter += 1
    return bid

def add_block(b_type, data):
    b = {"id": generate_id(), "type": b_type}
    b.update(data)
    blocks.append(b)

# --- 8-Step Socratic Pedagogy for Concept 1: Tangent to a Circle ---
# Step 1: Hook
add_block("theory", {
    "title": "Step 1: The Hook - Wheels in Motion",
    "title_hi": "चरण 1: हुक - गति में पहिए",
    "title_gu": "પગલું 1: હૂક - ગતિમાં પૈડાં",
    "body": "Have you ever observed a bicycle tire moving on a flat road? Even though the tire is round, it touches the ground at only ONE specific point at any given moment. Imagine drawing a straight line representing the road, and a circle representing the tire. How do they interact?",
    "body_hi": "क्या आपने कभी साइकिल के टायर को समतल सड़क पर चलते हुए देखा है? भले ही टायर गोल होता है, लेकिन यह किसी भी समय जमीन को केवल एक विशिष्ट बिंदु पर छूता है। कल्पना करें कि एक सीधी रेखा सड़क का प्रतिनिधित्व कर रही है, और एक वृत्त टायर का प्रतिनिधित्व कर रहा है। वे एक दूसरे से कैसे संपर्क करते हैं?",
    "body_gu": "શું તમે ક્યારેય સાયકલના ટાયરને સપાટ રસ્તા પર ફરતા જોયા છે? ટાયર ગોળ હોવા છતાં, તે કોઈપણ ક્ષણે માત્ર એક ચોક્કસ બિંદુ પર જમીનને સ્પર્શે છે. કલ્પના કરો કે રસ્તાનું પ્રતિનિધિત્વ કરતી સીધી રેખા અને ટાયરનું પ્રતિનિધિત્વ કરતું વર્તુળ દોરવામાં આવે. તેઓ કેવી રીતે ક્રિયાપ્રતિક્રિયા કરે છે?"
})

# Step 2: Socratic Thinking
add_block("socratic_question", {
    "question": "If you throw a straight stick across a circular hoop, what are the possible ways it can intersect the hoop?",
    "question_hi": "यदि आप एक वृत्ताकार घेरे (hoop) के आर-पार एक सीधी छड़ी फेंकते हैं, तो यह घेरे को किन संभावित तरीकों से काट सकती है?",
    "question_gu": "જો તમે ગોળાકાર રિંગ પર સીધી લાકડી ફેંકો, તો તે રિંગને કઈ સંભવિત રીતોથી છેદી શકે છે?",
    "options": [
        "It can either miss it completely or touch it at one point",
        "It can miss it, touch it at exactly one point, or cut through it at two points",
        "It can only cut through it at two points",
        "It can touch it at three points"
    ],
    "options_hi": [
        "यह या तो पूरी तरह से चूक सकती है या इसे एक बिंदु पर छू सकती है",
        "यह चूक सकती है, इसे ठीक एक बिंदु पर छू सकती है, या इसे दो बिंदुओं पर काट सकती है",
        "यह केवल इसे दो बिंदुओं पर काट सकती है",
        "यह इसे तीन बिंदुओं पर छू सकती है"
    ],
    "options_gu": [
        "તે ક્યાં તો તેને સંપૂર્ણપણે ચૂકી શકે છે અથવા તેને એક બિંદુ પર સ્પર્શ કરી શકે છે",
        "તે ચૂકી શકે છે, તેને બરાબર એક બિંદુ પર સ્પર્શ કરી શકે છે, અથવા તેને બે બિંદુઓ પર કાપી શકે છે",
        "તે ફક્ત તેને બે બિંદુઓ પર કાપી શકે છે",
        "તે તેને ત્રણ બિંદુઓ પર સ્પર્શ કરી શકે છે"
    ],
    "correct_index": 1,
    "explanation": "A line can be non-intersecting, it can touch at just one point, or it can cut through intersecting at exactly two points.",
    "explanation_hi": "एक रेखा अप्रतिच्छेदी हो सकती है, यह केवल एक बिंदु पर छू सकती है, या यह ठीक दो बिंदुओं पर प्रतिच्छेद करते हुए काट सकती है।",
    "explanation_gu": "એક રેખા બિન-છેદતી હોઈ શકે છે, તે માત્ર એક બિંદુ પર સ્પર્શ કરી શકે છે, અથવા તે બરાબર બે બિંદુઓ પર કાપી શકે છે."
})

# Step 3: Discovery
add_block("theory", {
    "title": "Step 3: Discovery - The Three Scenarios",
    "title_hi": "चरण 3: खोज - तीन परिदृश्य",
    "title_gu": "પગલું 3: શોધ - ત્રણ દૃશ્યો",
    "body": "When a line and a circle are drawn on a plane, there are exactly three possibilities:\n1. Non-intersecting line: No common points.\n2. Secant: The line cuts the circle at two distinct points.\n3. Tangent: The line touches the circle at exactly one single point.",
    "body_hi": "जब एक विमान पर एक रेखा और एक वृत्त खींचा जाता है, तो ठीक तीन संभावनाएं होती हैं:\n1. अप्रतिच्छेदी रेखा: कोई सामान्य बिंदु नहीं।\n2. छेदक रेखा (Secant): रेखा वृत्त को दो अलग-अलग बिंदुओं पर काटती है।\n3. स्पर्शरेखा (Tangent): रेखा वृत्त को ठीक एक बिंदु पर छूती है।",
    "body_gu": "જ્યારે પ્લેન પર રેખા અને વર્તુળ દોરવામાં આવે છે, ત્યારે બરાબર ત્રણ શક્યતાઓ છે:\n1. બિન-છેદતી રેખા: કોઈ સામાન્ય બિંદુઓ નથી.\n2. છેદિકા (Secant): રેખા વર્તુળને બે અલગ-અલગ બિંદુઓ પર કાપે છે.\n3. સ્પર્શક (Tangent): રેખા વર્તુળને બરાબર એક જ બિંદુ પર સ્પર્શ કરે છે."
})

# Step 4: Reveal
add_block("theory", {
    "title": "Step 4: Reveal - Defining Tangent & Secant",
    "title_hi": "चरण 4: प्रकटीकरण - स्पर्शरेखा और छेदक रेखा को परिभाषित करना",
    "title_gu": "પગલું 4: પ્રકટીકરણ - સ્પર્શક અને છેદિકાની વ્યાખ્યા",
    "body": "A line that intersects a circle at two distinct points is called a **Secant**. The word 'secant' comes from the Latin word 'secare', which means 'to cut'.\nA line that intersects the circle at only one point is called a **Tangent**. The word 'tangent' comes from the Latin 'tangere', meaning 'to touch'. The common point is called the **Point of Contact**.",
    "body_hi": "एक रेखा जो किसी वृत्त को दो अलग-अलग बिंदुओं पर काटती है, **छेदक रेखा (Secant)** कहलाती है। 'Secant' शब्द लैटिन शब्द 'secare' से आया है, जिसका अर्थ है 'काटना'।\nएक रेखा जो वृत्त को केवल एक बिंदु पर काटती है, **स्पर्शरेखा (Tangent)** कहलाती है। 'Tangent' शब्द लैटिन शब्द 'tangere' से आया है, जिसका अर्थ है 'छूना'। उभयनिष्ठ बिंदु को **स्पर्श बिंदु (Point of Contact)** कहा जाता है।",
    "body_gu": "એક રેખા જે વર્તુળને બે અલગ-અલગ બિંદુઓ પર કાપે છે તેને **છેદિકા (Secant)** કહેવામાં આવે છે. 'Secant' શબ્દ લેટિન શબ્દ 'secare' પરથી આવ્યો છે, જેનો અર્થ થાય છે 'કાપવું'.\nએક રેખા જે વર્તુળને માત્ર એક જ બિંદુ પર કાપે છે તેને **સ્પર્શક (Tangent)** કહેવામાં આવે છે. 'Tangent' શબ્દ લેટિન 'tangere' પરથી આવ્યો છે, જેનો અર્થ થાય છે 'સ્પર્શ કરવો'. સામાન્ય બિંદુને **સ્પર્શ બિંદુ (Point of Contact)** કહેવામાં આવે છે."
})

# Step 5: Knowledge Check
add_block("mcq", {
    "question": "What is the specific name for the common point between a tangent and a circle?",
    "question_hi": "स्पर्शरेखा और वृत्त के बीच के सामान्य बिंदु का विशिष्ट नाम क्या है?",
    "question_gu": "સ્પર્શક અને વર્તુળ વચ્ચેના સામાન્ય બિંદુનું ચોક્કસ નામ શું છે?",
    "options": ["Centre", "Point of Contact", "Intersection Point", "Secant Point"],
    "options_hi": ["केंद्र (Centre)", "स्पर्श बिंदु (Point of Contact)", "प्रतिच्छेदन बिंदु (Intersection Point)", "छेदक बिंदु (Secant Point)"],
    "options_gu": ["કેન્દ્ર (Centre)", "સ્પર્શ બિંદુ (Point of Contact)", "છેદન બિંદુ (Intersection Point)", "છેદિકા બિંદુ (Secant Point)"],
    "correct_index": 1,
    "explanation": "The single point where the tangent touches the circle is formally called the Point of Contact.",
    "explanation_hi": "वह एक बिंदु जहाँ स्पर्शरेखा वृत्त को छूती है, औपचारिक रूप से स्पर्श बिंदु (Point of Contact) कहलाता है।",
    "explanation_gu": "એક બિંદુ જ્યાં સ્પર્શક વર્તુળને સ્પર્શ કરે છે તેને ઔપચારિક રીતે સ્પર્શ બિંદુ કહેવામાં આવે છે."
})

# Step 6: Reflection
add_block("theory", {
    "title": "Step 6: Reflection",
    "title_hi": "चरण 6: प्रतिबिंब (Reflection)",
    "title_gu": "પગલું 6: પ્રતિબિંબ (Reflection)",
    "body": "Think about it: A tangent is simply a special case of a secant! Imagine a secant cutting the circle at points P and Q. If you slide the secant away from the center, points P and Q move closer and closer together until they merge into a single point. That's when the secant becomes a tangent!",
    "body_hi": "सोचिए: स्पर्शरेखा केवल छेदक रेखा का एक विशेष मामला है! कल्पना करें कि एक छेदक रेखा वृत्त को P और Q बिंदुओं पर काट रही है। यदि आप छेदक रेखा को केंद्र से दूर खिसकाते हैं, तो P और Q बिंदु एक-दूसरे के करीब और करीब आते जाते हैं जब तक कि वे एक बिंदु में विलीन नहीं हो जाते। तभी छेदक रेखा एक स्पर्शरेखा बन जाती है!",
    "body_gu": "વિચારો: સ્પર્શક એ માત્ર છેદિકાનો એક ખાસ કિસ્સો છે! કલ્પના કરો કે એક છેદિકા વર્તુળને P અને Q બિંદુઓ પર કાપે છે. જો તમે છેદિકાને કેન્દ્રથી દૂર સરકાવો છો, તો બિંદુઓ P અને Q એકબીજાની વધુ ને વધુ નજીક જાય છે જ્યાં સુધી તેઓ એક જ બિંદુમાં ભળી ન જાય. ત્યારે છેદિકા સ્પર્શક બની જાય છે!"
})

# Step 7: Connection
add_block("theory", {
    "title": "Step 7: Connection to Real Life",
    "title_hi": "चरण 7: वास्तविक जीवन से संबंध",
    "title_gu": "પગલું 7: વાસ્તવિક જીવન સાથે જોડાણ",
    "body": "In physics, when an object spins in a circle (like a stone tied to a string), its velocity at any given moment is always directed along the tangent. This is why mud flying off a spinning bicycle wheel always travels in straight tangential lines!",
    "body_hi": "भौतिकी में, जब कोई वस्तु एक वृत्त में घूमती है (जैसे डोरी से बंधा पत्थर), तो किसी भी क्षण उसका वेग हमेशा स्पर्शरेखा की दिशा में होता है। यही कारण है कि घूमते हुए साइकिल के पहिये से उड़ने वाली कीचड़ हमेशा सीधी स्पर्शरेखीय रेखाओं में यात्रा करती है!",
    "body_gu": "ભૌતિકશાસ્ત્રમાં, જ્યારે કોઈ પદાર્થ વર્તુળમાં ફરે છે (જેમ કે દોરી સાથે બાંધેલો પથ્થર), ત્યારે કોઈપણ ક્ષણે તેનો વેગ હંમેશા સ્પર્શકની દિશામાં હોય છે. આથી જ ફરતા સાયકલના પૈડામાંથી ઉડતો કાદવ હંમેશા સીધી સ્પર્શક રેખાઓમાં મુસાફરી કરે છે!"
})

# Step 8: Mastery
add_block("mcq", {
    "question": "How many tangents can be parallel to a single secant in a circle?",
    "question_hi": "एक वृत्त में एक ही छेदक रेखा के समांतर कितनी स्पर्शरेखाएँ हो सकती हैं?",
    "question_gu": "વર્તુળમાં એક જ છેદિકાને સમાંતર કેટલા સ્પર્શકો હોઈ શકે?",
    "options": ["One", "Two", "Three", "Infinitely many"],
    "options_hi": ["एक", "दो", "तीन", "अनंत"],
    "options_gu": ["એક", "બે", "ત્રણ", "અનંત"],
    "correct_index": 1,
    "explanation": "For any secant, you can slide it towards either edge of the circle to form a tangent. Since a circle has two opposite 'edges' relative to the secant, there can be exactly two parallel tangents.",
    "explanation_hi": "किसी भी छेदक रेखा के लिए, आप इसे स्पर्शरेखा बनाने के लिए वृत्त के किसी भी किनारे की ओर खिसका सकते हैं। चूँकि वृत्त में छेदक रेखा के सापेक्ष दो विपरीत 'किनारे' होते हैं, इसलिए ठीक दो समांतर स्पर्शरेखाएँ हो सकती हैं।",
    "explanation_gu": "કોઈપણ છેદિકા માટે, તમે સ્પર્શક બનાવવા માટે તેને વર્તુળની બંને ધાર તરફ સરકાવી શકો છો. વર્તુળમાં છેદિકાની સાપેક્ષ બે વિરુદ્ધ 'ધારો' હોવાથી, બરાબર બે સમાંતર સ્પર્શકો હોઈ શકે છે."
})


# --- Concept 2: Theorem 10.1 (Tangent is perpendicular to radius) ---
add_block("theory", {
    "title": "Theorem 10.1",
    "title_hi": "प्रमेय 10.1",
    "title_gu": "પ્રમેય 10.1",
    "body": "The tangent at any point of a circle is perpendicular to the radius through the point of contact.",
    "body_hi": "वृत्त के किसी भी बिंदु पर स्पर्शरेखा, स्पर्श बिंदु से होकर जाने वाली त्रिज्या पर लंब (perpendicular) होती है।",
    "body_gu": "વર્તુળના કોઈપણ બિંદુ પરનો સ્પર્શક સ્પર્શ બિંદુમાંથી પસાર થતી ત્રિજ્યાને લંબ (perpendicular) હોય છે."
})

add_block("theory", {
    "title": "Theorem 10.2",
    "title_hi": "प्रमेय 10.2",
    "title_gu": "પ્રમેય 10.2",
    "body": "The lengths of tangents drawn from an external point to a circle are equal.",
    "body_hi": "किसी बाह्य बिंदु से वृत्त पर खींची गई स्पर्शरेखाओं की लंबाइयाँ बराबर होती हैं।",
    "body_gu": "વર્તુળની બહારના બિંદુમાંથી વર્તુળ પર દોરેલા સ્પર્શકોની લંબાઈ સમાન હોય છે."
})

# generating 50 MCQs. To do this systematically without repeating manually:
# I will generate specific parameterized questions around Theorem 10.1, Theorem 10.2, Pythagoras applications in circles, angles of tangents, etc.

mcq_data = []

# Ex 10.1 base questions
mcq_data.extend([
    {
        "q": "How many tangents can a circle have?",
        "q_hi": "एक वृत्त की कितनी स्पर्शरेखाएँ हो सकती हैं?",
        "q_gu": "વર્તુળને કેટલા સ્પર્શકો હોઈ શકે?",
        "opts": ["1", "2", "0", "Infinitely many"],
        "opts_hi": ["1", "2", "0", "अनंत (Infinitely many)"],
        "opts_gu": ["1", "2", "0", "અનંત (Infinitely many)"],
        "ans": 3,
        "exp": "A circle is made up of infinitely many points, and at each point, one tangent can be drawn.",
        "exp_hi": "एक वृत्त अनंत बिंदुओं से बना होता है, और प्रत्येक बिंदु पर एक स्पर्शरेखा खींची जा सकती है।",
        "exp_gu": "વર્તુળ અનંત બિંદુઓનું બનેલું છે, અને દરેક બિંદુ પર એક સ્પર્શક દોરી શકાય છે."
    },
    {
        "q": "A tangent to a circle intersects it in _____ point(s).",
        "q_hi": "किसी वृत्त की स्पर्शरेखा उसे _____ बिंदु(ओं) पर प्रतिच्छेद करती है।",
        "q_gu": "વર્તુળનો સ્પર્શક તેને _____ બિંદુ(ઓ) માં છેદે છે.",
        "opts": ["One", "Two", "Three", "Zero"],
        "opts_hi": ["एक", "दो", "तीन", "शून्य"],
        "opts_gu": ["એક", "બે", "ત્રણ", "શૂન્ય"],
        "ans": 0,
        "exp": "A tangent always touches the circle at exactly one point.",
        "exp_hi": "एक स्पर्शरेखा हमेशा वृत्त को ठीक एक बिंदु पर छूती है।",
        "exp_gu": "સ્પર્શક હંમેશા વર્તુળને બરાબર એક બિંદુ પર સ્પર્શ કરે છે."
    },
    {
        "q": "A circle can have _____ parallel tangents at the most.",
        "q_hi": "एक वृत्त की अधिकतम _____ समांतर स्पर्शरेखाएँ हो सकती हैं।",
        "q_gu": "વર્તુળમાં વધુમાં વધુ _____ સમાંતર સ્પર્શકો હોઈ શકે છે.",
        "opts": ["One", "Two", "Three", "Infinitely many"],
        "opts_hi": ["एक", "दो", "तीन", "अनंत (Infinitely many)"],
        "opts_gu": ["એક", "બે", "ત્રણ", "અનંત (Infinitely many)"],
        "ans": 1,
        "exp": "For any given secant or diameter, there are only two parallel tangents (one on each opposite side).",
        "exp_hi": "किसी भी दी गई छेदक रेखा या व्यास के लिए, केवल दो समांतर स्पर्शरेखाएँ होती हैं (विपरीत दिशाओं में एक-एक)।",
        "exp_gu": "કોઈપણ આપેલ છેદિકા અથવા વ્યાસ માટે, ફક્ત બે સમાંતર સ્પર્શકો હોય છે (વિરુદ્ધ બાજુઓ પર એક-એક)."
    },
    {
        "q": "A line intersecting a circle in two points is called a:",
        "q_hi": "एक रेखा जो वृत्त को दो बिंदुओं पर काटती है, क्या कहलाती है?",
        "q_gu": "બે બિંદુઓમાં વર્તુળને છેદતી રેખાને શું કહેવામાં આવે છે?",
        "opts": ["Tangent", "Secant", "Radius", "Diameter"],
        "opts_hi": ["स्पर्शरेखा (Tangent)", "छेदक रेखा (Secant)", "त्रिज्या (Radius)", "व्यास (Diameter)"],
        "opts_gu": ["સ્પર્શક (Tangent)", "છેદિકા (Secant)", "ત્રિજ્યા (Radius)", "વ્યાસ (Diameter)"],
        "ans": 1,
        "exp": "A line intersecting at two points is a secant.",
        "exp_hi": "दो बिंदुओं पर काटने वाली रेखा छेदक रेखा होती है।",
        "exp_gu": "બે બિંદુઓ પર છેદતી રેખા છેદિકા છે."
    },
])

# Adding computational problems for Theorem 10.1 (Pythagoras)
# Format: radius (r), tangent length (t), distance from center (d). r^2 + t^2 = d^2
pythagoras_triplets = [(3, 4, 5), (5, 12, 13), (7, 24, 25), (8, 15, 17), (9, 40, 41), (20, 21, 29), (6, 8, 10), (15, 20, 25)]

for r, t, d in pythagoras_triplets:
    # Type A: Find hypotenuse (d)
    mcq_data.append({
        "q": f"A tangent PQ at a point P of a circle of radius {r} cm meets a line through the centre O at a point Q so that length PQ is {t} cm. The length of OQ is:",
        "q_hi": f"{r} सेमी त्रिज्या वाले एक वृत्त के बिंदु P पर स्पर्शरेखा PQ केंद्र O से जाने वाली एक रेखा से बिंदु Q पर इस प्रकार मिलती है कि PQ की लंबाई {t} सेमी है। OQ की लंबाई है:",
        "q_gu": f"{r} સેમી ત્રિજ્યાવાળા વર્તુળના બિંદુ P પર સ્પર્શક PQ કેન્દ્ર O માંથી પસાર થતી રેખાને બિંદુ Q પર એવી રીતે મળે છે કે PQ ની લંબાઈ {t} સેમી છે. OQ ની લંબાઈ છે:",
        "opts": [f"{d-1} cm", f"{d} cm", f"{d+1} cm", f"{d+2} cm"],
        "opts_hi": [f"{d-1} cm", f"{d} cm", f"{d+1} cm", f"{d+2} cm"],
        "opts_gu": [f"{d-1} cm", f"{d} cm", f"{d+1} cm", f"{d+2} cm"],
        "ans": 1,
        "exp": f"By Pythagoras theorem, OQ² = OP² + PQ² = {r}² + {t}² = {r**2} + {t**2} = {d**2}. Thus, OQ = {d} cm.",
        "exp_hi": f"पाइथागोरस प्रमेय द्वारा, OQ² = OP² + PQ² = {r}² + {t}² = {r**2} + {t**2} = {d**2}। इसलिए, OQ = {d} सेमी।",
        "exp_gu": f"પાયથાગોરસ પ્રમેય દ્વારા, OQ² = OP² + PQ² = {r}² + {t}² = {r**2} + {t**2} = {d**2}. તેથી, OQ = {d} સેમી."
    })
    
    # Type B: Find tangent (t)
    mcq_data.append({
        "q": f"From a point Q, the distance of Q from the centre is {d} cm. The radius of the circle is {r} cm. The length of the tangent to the circle is:",
        "q_hi": f"एक बिंदु Q से, केंद्र से Q की दूरी {d} सेमी है। वृत्त की त्रिज्या {r} सेमी है। वृत्त पर स्पर्शरेखा की लंबाई है:",
        "q_gu": f"એક બિંદુ Q થી, કેન્દ્રથી Q નું અંતર {d} સેમી છે. વર્તુળની ત્રિજ્યા {r} સેમી છે. વર્તુળના સ્પર્શકની લંબાઈ છે:",
        "opts": [f"{t-2} cm", f"{t-1} cm", f"{t} cm", f"{t+1} cm"],
        "opts_hi": [f"{t-2} cm", f"{t-1} cm", f"{t} cm", f"{t+1} cm"],
        "opts_gu": [f"{t-2} cm", f"{t-1} cm", f"{t} cm", f"{t+1} cm"],
        "ans": 2,
        "exp": f"By Pythagoras, Tangent² = Distance² - Radius² = {d}² - {r}² = {d**2} - {r**2} = {t**2}. So Tangent = {t} cm.",
        "exp_hi": f"पाइथागोरस द्वारा, स्पर्शरेखा² = दूरी² - त्रिज्या² = {d}² - {r}² = {t}²। इसलिए स्पर्शरेखा = {t} सेमी।",
        "exp_gu": f"પાયથાગોરસ દ્વારા, સ્પર્શક² = અંતર² - ત્રિજ્યા² = {d}² - {r}² = {t}². તેથી સ્પર્શક = {t} સેમી."
    })

# Angle properties for Tangents (Theorem 10.2 applications)
# Sum of central angle and angle between tangents is 180 degrees.
angles = [40, 50, 60, 70, 80, 90, 100, 110, 120]
for a in angles:
    opp_angle = 180 - a
    half_opp = opp_angle // 2
    mcq_data.append({
        "q": f"If TP and TQ are the two tangents to a circle with centre O so that ∠POQ = {a}°, then ∠PTQ is equal to:",
        "q_hi": f"यदि TP और TQ केंद्र O वाले वृत्त पर दो स्पर्शरेखाएँ इस प्रकार हैं कि ∠POQ = {a}° है, तो ∠PTQ बराबर है:",
        "q_gu": f"જો TP અને TQ કેન્દ્ર O વાળા વર્તુળના બે સ્પર્શકો હોય કે જેથી ∠POQ = {a}° થાય, તો ∠PTQ બરાબર છે:",
        "opts": [f"{opp_angle - 10}°", f"{opp_angle}°", f"{opp_angle + 10}°", f"{opp_angle + 20}°"],
        "opts_hi": [f"{opp_angle - 10}°", f"{opp_angle}°", f"{opp_angle + 10}°", f"{opp_angle + 20}°"],
        "opts_gu": [f"{opp_angle - 10}°", f"{opp_angle}°", f"{opp_angle + 10}°", f"{opp_angle + 20}°"],
        "ans": 1,
        "exp": f"The radius-tangent angles are 90°. In quadrilateral OPTQ, the sum of angles is 360°. So, ∠PTQ + ∠POQ = 180°. ∠PTQ = 180° - {a}° = {opp_angle}°.",
        "exp_hi": f"चतुर्भुज OPTQ के कोणों का योग 360° है। इसलिए, ∠PTQ + ∠POQ = 180°। अतः, ∠PTQ = 180° - {a}° = {opp_angle}°।",
        "exp_gu": f"ચતુષ્કોણ OPTQ ના ખૂણાઓનો સરવાળો 360° છે. તેથી, ∠PTQ + ∠POQ = 180°. આમ, ∠PTQ = 180° - {a}° = {opp_angle}°."
    })

    # Asking for half angle
    mcq_data.append({
        "q": f"If tangents PA and PB from a point P to a circle with centre O are inclined to each other at angle of {a}°, then ∠POA is equal to:",
        "q_hi": f"यदि एक बिंदु P से केंद्र O वाले वृत्त पर स्पर्शरेखाएँ PA और PB एक दूसरे से {a}° के कोण पर झुकी हुई हैं, तो ∠POA बराबर है:",
        "q_gu": f"જો બિંદુ P થી કેન્દ્ર O વાળા વર્તુળના સ્પર્શકો PA અને PB એકબીજા તરફ {a}° ના ખૂણે ઝુકેલા હોય, તો ∠POA બરાબર છે:",
        "opts": [f"{half_opp}°", f"{half_opp + 10}°", f"{half_opp - 10}°", f"{opp_angle}°"],
        "opts_hi": [f"{half_opp}°", f"{half_opp + 10}°", f"{half_opp - 10}°", f"{opp_angle}°"],
        "opts_gu": [f"{half_opp}°", f"{half_opp + 10}°", f"{half_opp - 10}°", f"{opp_angle}°"],
        "ans": 0,
        "exp": f"∠APB = {a}°. ∠AOB = 180° - {a}° = {opp_angle}°. OP bisects ∠AOB, so ∠POA = {opp_angle}° / 2 = {half_opp}°.",
        "exp_hi": f"∠APB = {a}°। ∠AOB = 180° - {a}° = {opp_angle}°। OP, ∠AOB को समद्विभाजित करता है, इसलिए ∠POA = {opp_angle}° / 2 = {half_opp}°।",
        "exp_gu": f"∠APB = {a}°. ∠AOB = 180° - {a}° = {opp_angle}°. OP, ∠AOB ને દુભાગે છે, તેથી ∠POA = {opp_angle}° / 2 = {half_opp}°."
    })

# Concentric circles problems: chord of larger circle touching smaller circle
# R^2 = r^2 + (chord/2)^2 => chord = 2 * sqrt(R^2 - r^2)
concentric_pairs = [(5, 3), (13, 5), (25, 7), (17, 8), (41, 9)]
for R, r in concentric_pairs:
    half_chord = int(math.sqrt(R**2 - r**2))
    chord = 2 * half_chord
    mcq_data.append({
        "q": f"Two concentric circles are of radii {R} cm and {r} cm. The length of the chord of the larger circle which touches the smaller circle is:",
        "q_hi": f"दो संकेंद्रिय वृत्तों की त्रिज्याएँ {R} सेमी और {r} सेमी हैं। बड़े वृत्त की उस जीवा की लंबाई जो छोटे वृत्त को स्पर्श करती है:",
        "q_gu": f"બે સમકેન્દ્રી વર્તુળોની ત્રિજ્યા {R} સેમી અને {r} સેમી છે. મોટા વર્તુળની જીવાની લંબાઈ જે નાના વર્તુળને સ્પર્શ કરે છે:",
        "opts": [f"{half_chord} cm", f"{chord} cm", f"{chord+2} cm", f"{R+r} cm"],
        "opts_hi": [f"{half_chord} cm", f"{chord} cm", f"{chord+2} cm", f"{R+r} cm"],
        "opts_gu": [f"{half_chord} cm", f"{chord} cm", f"{chord+2} cm", f"{R+r} cm"],
        "ans": 1,
        "exp": f"Let half-chord be x. x² = {R}² - {r}² = {R**2 - r**2}. So x = {half_chord}. Full chord = 2x = {chord} cm.",
        "exp_hi": f"मान लीजिए आधी जीवा x है। x² = {R}² - {r}² = {R**2 - r**2}। इसलिए x = {half_chord}। पूरी जीवा = 2x = {chord} सेमी।",
        "exp_gu": f"ધારો કે અડધી જીવા x છે. x² = {R}² - {r}² = {R**2 - r**2}. તેથી x = {half_chord}. સંપૂર્ણ જીવા = 2x = {chord} સેમી."
    })

# Additional conceptual proofs as MCQs (True/False or fill in the blank based)
mcq_data.extend([
    {
        "q": "Tangents drawn at the ends of a diameter of a circle are:",
        "q_hi": "एक वृत्त के व्यास के सिरों पर खींची गई स्पर्शरेखाएँ होती हैं:",
        "q_gu": "વર્તુળના વ્યાસના છેડે દોરેલા સ્પર્શકો હોય છે:",
        "opts": ["Perpendicular", "Parallel", "Intersecting", "None of the above"],
        "opts_hi": ["लंबवत (Perpendicular)", "समांतर (Parallel)", "प्रतिच्छेदी (Intersecting)", "इनमें से कोई नहीं"],
        "opts_gu": ["લંબ (Perpendicular)", "સમાંતર (Parallel)", "છેદતી (Intersecting)", "ઉપરનામાંથી કોઈ નહિ"],
        "ans": 1,
        "exp": "Since the radii to the points of contact form a straight line (the diameter), both tangents are perpendicular to this same line. Hence, they are parallel.",
        "exp_hi": "चूँकि स्पर्श बिंदुओं की त्रिज्याएँ एक सीधी रेखा (व्यास) बनाती हैं, दोनों स्पर्शरेखाएँ इसी रेखा पर लंब होती हैं। इसलिए, वे समांतर हैं।",
        "exp_gu": "સ્પર્શ બિંદુઓ સુધીની ત્રિજ્યાઓ સીધી રેખા (વ્યાસ) બનાવે છે, તેથી બંને સ્પર્શકો આ સમાન રેખાને લંબ છે. આથી, તેઓ સમાંતર છે."
    },
    {
        "q": "The perpendicular at the point of contact to the tangent to a circle always passes through the:",
        "q_hi": "वृत्त की स्पर्शरेखा के स्पर्श बिंदु पर डाला गया लंब हमेशा कहाँ से होकर गुजरता है:",
        "q_gu": "વર્તુળના સ્પર્શક પર સ્પર્શ બિંદુએ લંબ હંમેશા ક્યાંથી પસાર થાય છે:",
        "opts": ["Secant", "Chord", "Centre", "Outside the circle"],
        "opts_hi": ["छेदक रेखा (Secant)", "जीवा (Chord)", "केंद्र (Centre)", "वृत्त के बाहर"],
        "opts_gu": ["છેદિકા (Secant)", "જીવા (Chord)", "કેન્દ્ર (Centre)", "વર્તુળની બહાર"],
        "ans": 2,
        "exp": "According to Theorem 10.1, the radius drawn from the centre to the point of contact is perpendicular to the tangent.",
        "exp_hi": "प्रमेय 10.1 के अनुसार, केंद्र से स्पर्श बिंदु तक खींची गई त्रिज्या स्पर्शरेखा पर लंब होती है।",
        "exp_gu": "પ્રમેય 10.1 મુજબ, કેન્દ્રથી સ્પર્શ બિંદુ સુધી દોરવામાં આવેલી ત્રિજ્યા સ્પર્શકને લંબ હોય છે."
    },
    {
        "q": "A quadrilateral ABCD is drawn to circumscribe a circle. Which of the following is true?",
        "q_hi": "एक चतुर्भुज ABCD एक वृत्त के परिगत खींचा गया है। निम्नलिखित में से कौन सा सत्य है?",
        "q_gu": "ચતુષ્કોણ ABCD વર્તુળને ઘેરી લેવા દોરવામાં આવેલ છે. નીચેનામાંથી કયું સાચું છે?",
        "opts": ["AB + CD = AD + BC", "AB + BC = CD + AD", "AB * CD = AD * BC", "AB = CD"],
        "opts_hi": ["AB + CD = AD + BC", "AB + BC = CD + AD", "AB * CD = AD * BC", "AB = CD"],
        "opts_gu": ["AB + CD = AD + BC", "AB + BC = CD + AD", "AB * CD = AD * BC", "AB = CD"],
        "ans": 0,
        "exp": "Since tangents from an external point to a circle are equal in length, the sums of opposite sides are equal: AB + CD = AD + BC.",
        "exp_hi": "चूंकि एक बाहरी बिंदु से एक वृत्त पर स्पर्शरेखाओं की लंबाई समान होती है, विपरीत भुजाओं का योग बराबर होता है: AB + CD = AD + BC।",
        "exp_gu": "બહારના બિંદુથી વર્તુળ પરના સ્પર્શકોની લંબાઈ સમાન હોવાથી, વિરુદ્ધ બાજુઓનો સરવાળો સમાન છે: AB + CD = AD + BC."
    },
    {
        "q": "A parallelogram circumscribing a circle is always a:",
        "q_hi": "वृत्त के परिगत एक समांतर चतुर्भुज (parallelogram) हमेशा एक _____ होता है:",
        "q_gu": "વર્તુળને ઘેરી લેતો સમાંતરબાજુ ચતુષ્કોણ હંમેશા _____ હોય છે:",
        "opts": ["Rectangle", "Rhombus", "Trapezium", "Square"],
        "opts_hi": ["आयत (Rectangle)", "समचतुर्भुज (Rhombus)", "समलंब (Trapezium)", "वर्ग (Square)"],
        "opts_gu": ["લંબચોરસ (Rectangle)", "સમબાજુ ચતુષ્કોણ (Rhombus)", "સમલંબ (Trapezium)", "ચોરસ (Square)"],
        "ans": 1,
        "exp": "For any circumscribing quadrilateral, sums of opposite sides are equal. For a parallelogram, opposite sides are equal. Thus, all four sides become equal, making it a rhombus.",
        "exp_hi": "किसी भी परिगत चतुर्भुज के लिए, विपरीत भुजाओं का योग बराबर होता है। समांतर चतुर्भुज के लिए, विपरीत भुजाएँ बराबर होती हैं। इस प्रकार, चारों भुजाएँ बराबर हो जाती हैं, जिससे यह समचतुर्भुज बन जाता है।",
        "exp_gu": "કોઈપણ પરિગત ચતુષ્કોણ માટે, વિરુદ્ધ બાજુઓનો સરવાળો સમાન છે. સમાંતરબાજુ ચતુષ્કોણ માટે, વિરુદ્ધ બાજુઓ સમાન છે. આમ, ચારેય બાજુઓ સમાન બને છે, જે તેને સમબાજુ ચતુષ્કોણ બનાવે છે."
    },
    {
        "q": "Opposite sides of a quadrilateral circumscribing a circle subtend _____ angles at the centre of the circle.",
        "q_hi": "एक वृत्त के परिगत एक चतुर्भुज की विपरीत भुजाएँ वृत्त के केंद्र पर _____ कोण अंतरित (subtend) करती हैं।",
        "q_gu": "વર્તુળને ઘેરી લેતા ચતુષ્કોણની વિરુદ્ધ બાજુઓ વર્તુળના કેન્દ્રમાં _____ ખૂણાઓ બનાવે છે.",
        "opts": ["Complementary (90°)", "Supplementary (180°)", "Equal", "Acute"],
        "opts_hi": ["पूरक (90°)", "संपूरक (180°)", "समान", "न्यूनकोण"],
        "opts_gu": ["કોટિકોણ (90°)", "પૂરકકોણ (180°)", "સમાન", "લઘુકોણ"],
        "ans": 1,
        "exp": "It is a proven theorem that opposite sides of a circumscribing quadrilateral subtend supplementary angles at the centre.",
        "exp_hi": "यह एक सिद्ध प्रमेय है कि परिगत चतुर्भुज की विपरीत भुजाएँ केंद्र पर संपूरक कोण (180°) अंतरित करती हैं।",
        "exp_gu": "એક સાબિત પ્રમેય છે કે પરિગત ચતુષ્કોણની વિરુદ્ધ બાજુઓ કેન્દ્રમાં પૂરકકોણ (180°) બનાવે છે."
    }
])

# Adding the mcqs to blocks
for m in mcq_data:
    add_block("mcq", {
        "question": m["q"],
        "question_hi": m["q_hi"],
        "question_gu": m["q_gu"],
        "options": m["opts"],
        "options_hi": m["opts_hi"],
        "options_gu": m["opts_gu"],
        "correct_index": m["ans"],
        "explanation": m["exp"],
        "explanation_hi": m["exp_hi"],
        "explanation_gu": m["exp_gu"]
    })


# Writing to file
with open('/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_maths_ch10.json', 'w', encoding='utf-8') as f:
    json.dump(blocks, f, ensure_ascii=False, indent=2)

print(f"Generated {len(blocks)} blocks successfully.")
