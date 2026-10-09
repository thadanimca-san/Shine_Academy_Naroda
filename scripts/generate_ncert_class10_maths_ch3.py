import json

def generate_blocks():
    blocks = []
    
    # -------------------------------------------------------------------------
    # PART 1: INTRODUCTION & GRAPHICAL METHOD (EXERCISE 3.1 & 3.2)
    # -------------------------------------------------------------------------
    
    # Hook
    blocks.append({
        "id": "C10M_CH3_1",
        "type": "hook",
        "title": "The Mystery of the Fair",
        "body": "Akhila went to a fair with ₹20. She wanted to have rides on the Giant Wheel and play Hoopla. The number of times she played Hoopla is half the number of rides she had on the Giant Wheel. If each ride costs ₹3 and a game of Hoopla costs ₹4, how would you find out the number of rides she had? In this chapter, we will learn how to translate such real-world puzzles into Mathematics and solve them!",
        "title_hi": "मेले का रहस्य",
        "body_hi": "अखिला ₹20 लेकर एक मेले में गई। वह जायंट व्हील (Giant Wheel) की सवारी करना चाहती थी और हूपला (Hoopla) खेलना चाहती थी। उसने जितनी बार हूपला खेला, वह जायंट व्हील पर की गई सवारी की संख्या का आधा है। यदि प्रत्येक सवारी की कीमत ₹3 है और हूपला के एक खेल की कीमत ₹4 है, तो आप कैसे पता लगाएंगे कि उसने कितनी सवारी की? इस अध्याय में, हम सीखेंगे कि ऐसी वास्तविक दुनिया की पहेलियों को गणित में कैसे अनुवादित किया जाए और उन्हें कैसे हल किया जाए!",
        "title_gu": "મેળાનું રહસ્ય",
        "body_gu": "અખિલા ₹20 લઈને મેળામાં ગઈ. તે જાયન્ટ વ્હીલ (Giant Wheel) ની સવારી કરવા માંગતી હતી અને હૂપલા (Hoopla) રમવા માંગતી હતી. તેણે જેટલી વાર હૂપલા રમી, તે જાયન્ટ વ્હીલ પર કરેલી સવારીની સંખ્યા કરતાં અડધી છે. જો દરેક સવારીની કિંમત ₹3 હોય અને હૂપલાની એક રમતની કિંમત ₹4 હોય, તો તમે કેવી રીતે શોધી શકશો કે તેણે કેટલી સવારી કરી? આ પ્રકરણમાં, આપણે શીખીશું કે આવા વાસ્તવિક દુનિયાના કોયડાઓને ગણિતમાં કેવી રીતે અનુવાદિત કરવા અને તેમને કેવી રીતે ઉકેલવા!",
        "bloom": "Understand",
        "difficulty": "Beginner",
        "estimated_minutes": 2
    })
    
    # Socratic Thinking
    blocks.append({
        "id": "C10M_CH3_2",
        "type": "socratic_question",
        "question": "If we let the number of Giant Wheel rides be 'x' and Hoopla games be 'y', how can we write the condition 'Hoopla games is half the Giant Wheel rides' as an equation?",
        "options": ["y = 1/2 x", "x = 1/2 y", "y = 2x", "x + y = 1/2"],
        "correct_index": 0,
        "explanation": "Since Hoopla (y) is half of Giant Wheel (x), the equation is y = 1/2 x, or 2y = x.",
        "question_hi": "यदि हम जायंट व्हील की सवारी की संख्या को 'x' और हूपला खेलों को 'y' मान लें, तो हम 'हूपला खेल जायंट व्हील की सवारी का आधा है' की शर्त को एक समीकरण के रूप में कैसे लिख सकते हैं?",
        "options_hi": ["y = 1/2 x", "x = 1/2 y", "y = 2x", "x + y = 1/2"],
        "explanation_hi": "चूँकि हूपला (y) जायंट व्हील (x) का आधा है, समीकरण y = 1/2 x या 2y = x है।",
        "question_gu": "જો આપણે જાયન્ટ વ્હીલની સવારીની સંખ્યાને 'x' અને હૂપલા રમતોને 'y' માની લઈએ, તો આપણે 'હૂપલા રમતો જાયન્ટ વ્હીલની સવારી કરતા અડધી છે' શરતને સમીકરણ તરીકે કેવી રીતે લખી શકીએ?",
        "options_gu": ["y = 1/2 x", "x = 1/2 y", "y = 2x", "x + y = 1/2"],
        "explanation_gu": "કારણ કે હૂપલા (y) એ જાયન્ટ વ્હીલ (x) નો અડધો ભાગ છે, સમીકરણ y = 1/2 x અથવા 2y = x છે.",
        "bloom": "Apply",
        "difficulty": "Beginner",
        "estimated_minutes": 1
    })

    # Theory: General Form
    blocks.append({
        "id": "C10M_CH3_3",
        "type": "theory",
        "title": "General Form of a Pair of Linear Equations",
        "body": "An equation which can be put in the form **ax + by + c = 0**, where a, b and c are real numbers, and a and b are not both zero, is called a linear equation in two variables x and y.\n\nA **pair of linear equations** in two variables is represented as:\n**a₁x + b₁y + c₁ = 0**\n**a₂x + b₂y + c₂ = 0**\n\nGeometrically, each equation represents a straight line. When we draw two straight lines in a plane, only one of three possibilities can happen:\n1. The two lines **intersect** at one point (Exactly one solution).\n2. The two lines are **parallel** (No solution).\n3. The two lines are **coincident** (overlapping) (Infinitely many solutions).",
        "title_hi": "रैखिक समीकरण युग्म का व्यापक रूप",
        "body_hi": "एक समीकरण जिसे **ax + by + c = 0** के रूप में रखा जा सकता है, जहाँ a, b और c वास्तविक संख्याएँ हैं, और a और b दोनों शून्य नहीं हैं, दो चरों x और y में एक रैखिक समीकरण कहलाता है।\n\nदो चरों में **रैखिक समीकरणों का एक युग्म** इस प्रकार दर्शाया जाता है:\n**a₁x + b₁y + c₁ = 0**\n**a₂x + b₂y + c₂ = 0**\n\nज्यामितीय रूप से, प्रत्येक समीकरण एक सीधी रेखा का प्रतिनिधित्व करता है। जब हम एक तल (plane) में दो सीधी रेखाएँ खींचते हैं, तो तीन में से केवल एक संभावना हो सकती है:\n1. दोनों रेखाएँ एक बिंदु पर **प्रतिच्छेद (intersect)** करती हैं (ठीक एक हल)।\n2. दोनों रेखाएँ **समानांतर (parallel)** हैं (कोई हल नहीं)।\n3. दोनों रेखाएँ **संपाती (coincident)** (ओवरलैपिंग) हैं (अपरिमित रूप से अनेक हल)।",
        "title_gu": "સુરેખ સમીકરણ યુગ્મનું વ્યાપક સ્વરૂપ",
        "body_gu": "એક સમીકરણ જેને **ax + by + c = 0** ના સ્વરૂપમાં મૂકી શકાય છે, જ્યાં a, b અને c વાસ્તવિક સંખ્યાઓ છે, અને a અને b બંને શૂન્ય નથી, તેને બે ચલો x અને y માં સુરેખ સમીકરણ કહેવાય છે.\n\nબે ચલોમાં **સુરેખ સમીકરણોની એક જોડ** આ રીતે રજૂ થાય છે:\n**a₁x + b₁y + c₁ = 0**\n**a₂x + b₂y + c₂ = 0**\n\nભૌમિતિક રીતે, દરેક સમીકરણ એક સીધી રેખા દર્શાવે છે. જ્યારે આપણે સમતલ (plane) માં બે સીધી રેખાઓ દોરીએ છીએ, ત્યારે ત્રણમાંથી માત્ર એક જ શક્યતા હોઈ શકે છે:\n1. બે રેખાઓ એક બિંદુ પર **છેદે (intersect)** છે (બરાબર એક ઉકેલ).\n2. બે રેખાઓ **સમાંતર (parallel)** છે (કોઈ ઉકેલ નથી).\n3. બે રેખાઓ **સંપાતી (coincident)** (ઓવરલેપિંગ) છે (અનંત ઘણા ઉકેલો).",
        "bloom": "Understand",
        "difficulty": "Beginner",
        "estimated_minutes": 4
    })
    
    # Teacher Tip: Comparing ratios
    blocks.append({
        "id": "C10M_CH3_4",
        "type": "teacher_tip",
        "title": "The Ratio Trick!",
        "body": "You don't always need to draw the graph to know how the lines will behave! Just compare their coefficients:\n- Intersecting: a₁/a₂ ≠ b₁/b₂\n- Coincident: a₁/a₂ = b₁/b₂ = c₁/c₂\n- Parallel: a₁/a₂ = b₁/b₂ ≠ c₁/c₂",
        "title_hi": "अनुपात की युक्ति!",
        "body_hi": "यह जानने के लिए कि रेखाएँ कैसा व्यवहार करेंगी, आपको हमेशा ग्राफ़ बनाने की आवश्यकता नहीं है! बस उनके गुणांकों की तुलना करें:\n- प्रतिच्छेदी: a₁/a₂ ≠ b₁/b₂\n- संपाती: a₁/a₂ = b₁/b₂ = c₁/c₂\n- समानांतर: a₁/a₂ = b₁/b₂ ≠ c₁/c₂",
        "title_gu": "ગુણોત્તરની યુક્તિ!",
        "body_gu": "રેખાઓ કેવું વર્તન કરશે તે જાણવા માટે તમારે હંમેશા આલેખ દોરવાની જરૂર નથી! માત્ર તેમના સહગુણકોની સરખામણી કરો:\n- છેદતી: a₁/a₂ ≠ b₁/b₂\n- સંપાતી: a₁/a₂ = b₁/b₂ = c₁/c₂\n- સમાંતર: a₁/a₂ = b₁/b₂ ≠ c₁/c₂",
        "bloom": "Apply",
        "difficulty": "Beginner",
        "estimated_minutes": 2
    })

    # EXERCISE 3.1 & 3.2 Quiz section
    blocks.append({
        "id": "C10M_CH3_EX3_Q1",
        "type": "quiz",
        "question": "On comparing the ratios a₁/a₂, b₁/b₂ and c₁/c₂, find out whether the lines representing the following pair of linear equations intersect at a point, are parallel or coincident: \n5x - 4y + 8 = 0\n7x + 6y - 9 = 0",
        "options": ["Intersect at a point", "Parallel", "Coincident", "None of these"],
        "correct_index": 0,
        "explanation": "Here, a₁/a₂ = 5/7 and b₁/b₂ = -4/6 = -2/3. Since a₁/a₂ ≠ b₁/b₂, the lines intersect at a point.",
        "question_hi": "अनुपातों a₁/a₂, b₁/b₂ और c₁/c₂ की तुलना करके ज्ञात कीजिए कि निम्न रैखिक समीकरणों का युग्म एक बिंदु पर प्रतिच्छेद करता है, समानांतर है या संपाती है: \n5x - 4y + 8 = 0\n7x + 6y - 9 = 0",
        "options_hi": ["एक बिंदु पर प्रतिच्छेद करती हैं", "समानांतर हैं", "संपाती हैं", "इनमें से कोई नहीं"],
        "explanation_hi": "यहाँ, a₁/a₂ = 5/7 और b₁/b₂ = -4/6 = -2/3 है। चूँकि a₁/a₂ ≠ b₁/b₂, इसलिए रेखाएँ एक बिंदु पर प्रतिच्छेद करती हैं।",
        "question_gu": "ગુણોત્તર a₁/a₂, b₁/b₂ અને c₁/c₂ ની સરખામણી કરીને શોધો કે નીચેના સુરેખ સમીકરણોની જોડ એક બિંદુ પર છેદે છે, સમાંતર છે કે સંપાતી છે: \n5x - 4y + 8 = 0\n7x + 6y - 9 = 0",
        "options_gu": ["એક બિંદુ પર છેદે છે", "સમાંતર છે", "સંપાતી છે", "આમાંથી કોઈ નહિ"],
        "explanation_gu": "અહીં, a₁/a₂ = 5/7 અને b₁/b₂ = -4/6 = -2/3 છે. કારણ કે a₁/a₂ ≠ b₁/b₂, તેથી રેખાઓ એક બિંદુ પર છેદે છે.",
        "bloom": "Apply",
        "difficulty": "Intermediate",
        "estimated_minutes": 2
    })

    blocks.append({
        "id": "C10M_CH3_EX3_Q2",
        "type": "quiz",
        "question": "Are the following pair of linear equations consistent or inconsistent? \n3x + 2y = 5\n2x - 3y = 7",
        "options": ["Consistent", "Inconsistent", "Coincident", "Parallel"],
        "correct_index": 0,
        "explanation": "a₁/a₂ = 3/2 and b₁/b₂ = -2/3. Since a₁/a₂ ≠ b₁/b₂, they intersect and have a unique solution. Therefore, they are consistent.",
        "question_hi": "क्या निम्न रैखिक समीकरणों का युग्म संगत (consistent) है या असंगत (inconsistent)? \n3x + 2y = 5\n2x - 3y = 7",
        "options_hi": ["संगत", "असंगत", "संपाती", "समानांतर"],
        "explanation_hi": "a₁/a₂ = 3/2 और b₁/b₂ = -2/3। चूँकि a₁/a₂ ≠ b₁/b₂, वे प्रतिच्छेद करते हैं और उनका एक अद्वितीय हल है। इसलिए, वे संगत हैं।",
        "question_gu": "શું નીચેના સુરેખ સમીકરણોની જોડ સુસંગત (consistent) છે કે અસંગત (inconsistent)? \n3x + 2y = 5\n2x - 3y = 7",
        "options_gu": ["સુસંગત", "અસંગત", "સંપાતી", "સમાંતર"],
        "explanation_gu": "a₁/a₂ = 3/2 અને b₁/b₂ = -2/3. કારણ કે a₁/a₂ ≠ b₁/b₂, તેઓ છેદે છે અને તેમનો એક અનન્ય ઉકેલ છે. તેથી, તેઓ સુસંગત છે.",
        "bloom": "Apply",
        "difficulty": "Intermediate",
        "estimated_minutes": 2
    })

    # -------------------------------------------------------------------------
    # PART 2: SUBSTITUTION METHOD
    # -------------------------------------------------------------------------

    blocks.append({
        "id": "C10M_CH3_5",
        "type": "theory",
        "title": "Algebraic Methods: The Substitution Method",
        "body": "Graphing is not always precise. We use algebraic methods to find exact solutions. The first is the **Substitution Method**.\n\n**Steps:**\n1. Find the value of one variable (say y) in terms of the other (say x) from one equation.\n2. Substitute this value of y in the second equation. It becomes an equation in only one variable (x), which you can easily solve.\n3. Substitute the value of x back into the first equation to find y.",
        "title_hi": "बीजगणितीय विधियाँ: प्रतिस्थापन विधि (Substitution Method)",
        "body_hi": "ग्राफिंग हमेशा सटीक नहीं होती है। हम सटीक हल खोजने के लिए बीजगणितीय विधियों का उपयोग करते हैं। पहली विधि **प्रतिस्थापन विधि** है।\n\n**चरण:**\n1. एक समीकरण से एक चर (मान लें y) का मान दूसरे चर (मान लें x) के पदों में ज्ञात कीजिए।\n2. दूसरे समीकरण में y का यह मान प्रतिस्थापित (substitute) करें। यह केवल एक चर (x) में एक समीकरण बन जाता है, जिसे आप आसानी से हल कर सकते हैं।\n3. y ज्ञात करने के लिए पहले समीकरण में x का मान वापस प्रतिस्थापित करें।",
        "title_gu": "બીજગણિતીય રીતો: આદેશની રીત (Substitution Method)",
        "body_gu": "ગ્રાફિંગ હંમેશા ચોક્કસ હોતું નથી. આપણે ચોક્કસ ઉકેલો શોધવા માટે બીજગણિતીય રીતોનો ઉપયોગ કરીએ છીએ. પ્રથમ **આદેશની રીત** છે.\n\n**પગલાં:**\n1. એક સમીકરણમાંથી એક ચલ (ધારો કે y) ની કિંમત બીજા ચલ (ધારો કે x) ના સ્વરૂપમાં શોધો.\n2. બીજા સમીકરણમાં y ની આ કિંમત મૂકો (substitute). તે માત્ર એક ચલ (x) માં સમીકરણ બની જાય છે, જેને તમે સરળતાથી ઉકેલી શકો છો.\n3. y શોધવા માટે પ્રથમ સમીકરણમાં x ની કિંમત પાછી મૂકો.",
        "bloom": "Understand",
        "difficulty": "Intermediate",
        "estimated_minutes": 4
    })

    # Exercise Quiz: Substitution
    blocks.append({
        "id": "C10M_CH3_EX3_Q3",
        "type": "quiz",
        "question": "Solve the following pair of linear equations by the substitution method: \nx + y = 14 \nx - y = 4",
        "options": ["x = 9, y = 5", "x = 10, y = 4", "x = 8, y = 6", "x = 5, y = 9"],
        "correct_index": 0,
        "explanation": "From the second equation, x = y + 4. Substitute this into the first: (y + 4) + y = 14 => 2y = 10 => y = 5. Then x = 5 + 4 = 9.",
        "question_hi": "निम्न रैखिक समीकरण युग्म को प्रतिस्थापन विधि से हल कीजिए: \nx + y = 14 \nx - y = 4",
        "options_hi": ["x = 9, y = 5", "x = 10, y = 4", "x = 8, y = 6", "x = 5, y = 9"],
        "explanation_hi": "दूसरे समीकरण से, x = y + 4. इसे पहले में प्रतिस्थापित करें: (y + 4) + y = 14 => 2y = 10 => y = 5. फिर x = 5 + 4 = 9.",
        "question_gu": "નીચેના સુરેખ સમીકરણ યુગ્મને આદેશની રીતથી ઉકેલો: \nx + y = 14 \nx - y = 4",
        "options_gu": ["x = 9, y = 5", "x = 10, y = 4", "x = 8, y = 6", "x = 5, y = 9"],
        "explanation_gu": "બીજા સમીકરણ પરથી, x = y + 4. આને પ્રથમમાં મૂકો: (y + 4) + y = 14 => 2y = 10 => y = 5. પછી x = 5 + 4 = 9.",
        "bloom": "Apply",
        "difficulty": "Intermediate",
        "estimated_minutes": 3
    })

    # -------------------------------------------------------------------------
    # PART 3: ELIMINATION METHOD
    # -------------------------------------------------------------------------

    blocks.append({
        "id": "C10M_CH3_6",
        "type": "theory",
        "title": "Algebraic Methods: The Elimination Method",
        "body": "The **Elimination Method** is often faster. \n\n**Steps:**\n1. Multiply both equations by suitable non-zero constants to make the coefficients of one variable (either x or y) numerically equal.\n2. Add or subtract one equation from the other so that one variable gets eliminated.\n3. Solve the resulting equation in one variable.\n4. Substitute the value found into either original equation to find the other variable.",
        "title_hi": "बीजगणितीय विधियाँ: विलोपन विधि (Elimination Method)",
        "body_hi": "**विलोपन विधि** अक्सर तेज होती है।\n\n**चरण:**\n1. एक चर (x या y) के गुणांकों को संख्यात्मक रूप से समान बनाने के लिए दोनों समीकरणों को उपयुक्त गैर-शून्य स्थिरांक से गुणा करें।\n2. एक समीकरण को दूसरे से जोड़ें या घटाएं ताकि एक चर समाप्त (eliminate) हो जाए।\n3. एक चर में परिणामी समीकरण को हल करें।\n4. दूसरे चर को खोजने के लिए प्राप्त मान को किसी भी मूल समीकरण में प्रतिस्थापित करें।",
        "title_gu": "બીજગણિતીય રીતો: લોપની રીત (Elimination Method)",
        "body_gu": "**લોપની રીત** વારંવાર ઝડપી હોય છે.\n\n**પગલાં:**\n1. એક ચલ (x અથવા y) ના સહગુણકોને સંખ્યાત્મક રીતે સમાન બનાવવા માટે બંને સમીકરણોને યોગ્ય શૂન્યેતર અચળ વડે ગુણાકાર કરો.\n2. એક સમીકરણને બીજામાંથી ઉમેરો અથવા બાદ કરો જેથી એક ચલ દૂર (eliminate) થાય.\n3. એક ચલમાં પરિણામી સમીકરણ ઉકેલો.\n4. બીજો ચલ શોધવા માટે પ્રાપ્ત કિંમતને કોઈપણ મૂળ સમીકરણમાં મૂકો.",
        "bloom": "Understand",
        "difficulty": "Intermediate",
        "estimated_minutes": 4
    })

    # Exercise Quiz: Elimination
    blocks.append({
        "id": "C10M_CH3_EX3_Q4",
        "type": "quiz",
        "question": "Solve the following pair of linear equations by the elimination method: \n3x + 4y = 10 \n2x - 2y = 2",
        "options": ["x = 2, y = 1", "x = 1, y = 2", "x = -2, y = -1", "x = 3, y = 1"],
        "correct_index": 0,
        "explanation": "Multiply the second equation by 2: 4x - 4y = 4. Add to the first: (3x+4x) + (4y-4y) = 10+4 => 7x = 14 => x = 2. Substitute x=2 in 2x - 2y = 2 => 4 - 2y = 2 => 2y = 2 => y = 1.",
        "question_hi": "निम्न रैखिक समीकरण युग्म को विलोपन विधि से हल कीजिए: \n3x + 4y = 10 \n2x - 2y = 2",
        "options_hi": ["x = 2, y = 1", "x = 1, y = 2", "x = -2, y = -1", "x = 3, y = 1"],
        "explanation_hi": "दूसरे समीकरण को 2 से गुणा करें: 4x - 4y = 4। पहले में जोड़ें: (3x+4x) + (4y-4y) = 10+4 => 7x = 14 => x = 2। 2x - 2y = 2 में x=2 प्रतिस्थापित करें => 4 - 2y = 2 => 2y = 2 => y = 1।",
        "question_gu": "નીચેના સુરેખ સમીકરણ યુગ્મને લોપની રીતથી ઉકેલો: \n3x + 4y = 10 \n2x - 2y = 2",
        "options_gu": ["x = 2, y = 1", "x = 1, y = 2", "x = -2, y = -1", "x = 3, y = 1"],
        "explanation_gu": "બીજા સમીકરણને 2 વડે ગુણાકાર કરો: 4x - 4y = 4. પ્રથમમાં ઉમેરો: (3x+4x) + (4y-4y) = 10+4 => 7x = 14 => x = 2. 2x - 2y = 2 માં x=2 મૂકો => 4 - 2y = 2 => 2y = 2 => y = 1.",
        "bloom": "Apply",
        "difficulty": "Hard",
        "estimated_minutes": 5
    })

    # Word Problem using Elimination
    blocks.append({
        "id": "C10M_CH3_EX3_Q5",
        "type": "quiz",
        "question": "The sum of a two-digit number and the number obtained by reversing the digits is 66. If the digits of the number differ by 2, find the number. How many such numbers are there?",
        "options": ["42 and 24 (Two numbers)", "53 and 35 (Two numbers)", "60 (One number)", "42 (One number)"],
        "correct_index": 0,
        "explanation": "Let tens digit be x and units be y. Number is 10x+y. Reversed is 10y+x. (10x+y) + (10y+x) = 66 => 11(x+y) = 66 => x+y = 6. Also x-y = 2 or y-x = 2. Solving x+y=6 and x-y=2 gives x=4, y=2 (Number 42). Solving x+y=6 and y-x=2 gives x=2, y=4 (Number 24). There are two such numbers.",
        "question_hi": "दो अंकों की एक संख्या और उसके अंकों को उलटने पर प्राप्त संख्या का योग 66 है। यदि संख्या के अंकों का अंतर 2 है, तो संख्या ज्ञात कीजिए। ऐसी कितनी संख्याएँ हैं?",
        "options_hi": ["42 और 24 (दो संख्याएँ)", "53 और 35 (दो संख्याएँ)", "60 (एक संख्या)", "42 (एक संख्या)"],
        "explanation_hi": "मान लीजिए दहाई का अंक x है और इकाई y है। संख्या 10x+y है। उलटा 10y+x है। (10x+y) + (10y+x) = 66 => 11(x+y) = 66 => x+y = 6. साथ ही x-y = 2 या y-x = 2. x+y=6 और x-y=2 को हल करने पर x=4, y=2 (संख्या 42) मिलता है। x+y=6 और y-x=2 को हल करने पर x=2, y=4 (संख्या 24) मिलता है। ऐसी दो संख्याएँ हैं।",
        "question_gu": "બે અંકોની એક સંખ્યા અને તેના અંકોને ઉલટાવવાથી મળતી સંખ્યાનો સરવાળો 66 છે. જો સંખ્યાના અંકોનો તફાવત 2 હોય, તો સંખ્યા શોધો. આવી કેટલી સંખ્યાઓ છે?",
        "options_gu": ["42 અને 24 (બે સંખ્યાઓ)", "53 અને 35 (બે સંખ્યાઓ)", "60 (એક સંખ્યા)", "42 (એક સંખ્યા)"],
        "explanation_gu": "ધારો કે દશકનો અંક x છે અને એકમ y છે. સંખ્યા 10x+y છે. ઉલટાવી 10y+x છે. (10x+y) + (10y+x) = 66 => 11(x+y) = 66 => x+y = 6. વળી x-y = 2 અથવા y-x = 2. x+y=6 અને x-y=2 ઉકેલવાથી x=4, y=2 (સંખ્યા 42) મળે છે. x+y=6 અને y-x=2 ઉકેલવાથી x=2, y=4 (સંખ્યા 24) મળે છે. આવી બે સંખ્યાઓ છે.",
        "bloom": "Create",
        "difficulty": "Hard",
        "estimated_minutes": 8
    })

    return blocks

def get_metadata():
    return {
        "id": "ncert_class10_maths_ch3",
        "title": "Chapter 3: Pair of Linear Equations in Two Variables",
        "title_hi": "अध्याय 3: दो चर वाले रैखिक समीकरण युग्म",
        "title_gu": "પ્રકરણ 3: દ્વિચલ સુરેખ સમીકરણ યુગ્મ",
        "subject": "Mathematics",
        "grade": "10",
        "board": "CBSE/GSEB",
        "curriculum": ["CBSE", "NCERT", "GSEB"],
        "language": "English, Hindi, Gujarati",
        "difficulty": "Intermediate",
        "estimated_minutes": 180,
        "version": "1.0.0",
        "author": "Shine Academy EduOS",
        "last_updated": "2026-09-30",
        "tags": ["linear_equations", "substitution", "elimination", "graphical_method"]
    }

def generate_chapter():
    chapter_data = {
        "metadata": get_metadata(),
        "blocks": generate_blocks()
    }
    
    with open('app_core/chapters/ncert_class10_maths_ch3.json', 'w', encoding='utf-8') as f:
        json.dump(chapter_data, f, indent=2, ensure_ascii=False)
        
    print("Generated ncert_class10_maths_ch3.json successfully!")

if __name__ == "__main__":
    generate_chapter()
