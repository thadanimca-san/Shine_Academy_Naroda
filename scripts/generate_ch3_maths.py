import json
import random

def generate_chapter():
    metadata = {
        "title": "Pair of Linear Equations in Two Variables",
        "subject": "Maths",
        "grade": "10",
        "curriculum": ["GSEB", "NCERT", "CBSE"],
        "difficulty": "Intermediate",
        "version": "4.0.0",
        "id": "cbse_class10_maths_ch3"
    }

    blocks = []

    # 1. HOOK
    blocks.append({
        "id": "KOBJ_10_MATH_CH3_HOOK_01",
        "type": "hook",
        "title": "The Mystery of Ages",
        "title_hi": "उम्र का रहस्य",
        "title_gu": "ઉંમરનું રહસ્ય",
        "body": "A father tells his daughter, 'Seven years ago, I was seven times as old as you were then. Also, three years from now, I shall be three times as old as you will be.' Isn't this interesting? How can we find their present ages?",
        "body_hi": "एक पिता अपनी बेटी से कहता है, 'सात साल पहले, मैं तुम्हारी उस समय की उम्र का सात गुना था। साथ ही, अब से तीन साल बाद, मैं तुम्हारी उम्र का तीन गुना हो जाऊंगा।' क्या यह दिलचस्प नहीं है? हम उनकी वर्तमान उम्र कैसे जान सकते हैं?",
        "body_gu": "એક પિતા તેની પુત્રીને કહે છે, 'સાત વર્ષ પહેલાં, હું તારા કરતાં સાત ગણો મોટો હતો. વળી, હવેથી ત્રણ વર્ષ પછી, હું તારી ઉંમર કરતાં ત્રણ ગણો થઈશ.' શું આ રસપ્રદ નથી? આપણે તેમની વર્તમાન ઉંમર કેવી રીતે શોધી શકીએ?"
    })

    # 2. SOCRATIC THINKING
    blocks.append({
        "id": "KOBJ_10_MATH_CH3_SOCR_01",
        "type": "socratic_question",
        "title": "Think About It",
        "title_hi": "इस पर विचार करें",
        "title_gu": "આના વિશે વિચારો",
        "question": "If you have two unknown values to find (like the father's age and the daughter's age), how many different clues or equations do you think you need to find both values exactly?",
        "question_hi": "यदि आपको खोजने के लिए दो अज्ञात मान हैं (जैसे पिता की उम्र और बेटी की उम्र), तो आपको लगता है कि दोनों मानों को सटीक रूप से खोजने के लिए आपको कितने अलग-अलग सुराग या समीकरणों की आवश्यकता है?",
        "question_gu": "જો તમારે શોધવા માટે બે અજ્ઞાત મૂલ્યો છે (જેમ કે પિતાની ઉંમર અને પુત્રીની ઉંમર), તો તમને બંને મૂલ્યો બરાબર શોધવા માટે કેટલા જુદા જુદા સંકેતો અથવા સમીકરણોની જરૂર છે?",
        "options": ["1", "2", "3", "None"],
        "options_hi": ["1", "2", "3", "कोई नहीं"],
        "options_gu": ["1", "2", "3", "કોઈ નહીં"],
        "correct_index": 1,
        "explanation": "To solve for two variables, we generally need two distinct equations.",
        "explanation_hi": "दो चरों को हल करने के लिए, हमें आम तौर पर दो अलग-अलग समीकरणों की आवश्यकता होती है।",
        "explanation_gu": "બે ચલો ઉકેલવા માટે, આપણને સામાન્ય રીતે બે અલગ-અલગ સમીકરણોની જરૂર હોય છે."
    })

    # 3. DISCOVERY
    blocks.append({
        "id": "KOBJ_10_MATH_CH3_DISC_01",
        "type": "discovery",
        "title": "Connecting the Dots",
        "title_hi": "कड़ियों को जोड़ना",
        "title_gu": "બિંદુઓને જોડવું",
        "body": "When we represent two straight lines on a graph, they can either intersect at one point, be parallel and never touch, or overlap completely. This visual geometry is exactly what happens with pairs of linear equations!",
        "body_hi": "जब हम एक ग्राफ पर दो सीधी रेखाओं का प्रतिनिधित्व करते हैं, तो वे या तो एक बिंदु पर प्रतिच्छेद कर सकती हैं, समानांतर हो सकती हैं और कभी नहीं छू सकती हैं, या पूरी तरह से ओवरलैप कर सकती हैं। यह दृश्य ज्यामिति बिल्कुल वही है जो रैखिक समीकरणों के जोड़े के साथ होती है!",
        "body_gu": "જ્યારે આપણે આલેખ પર બે સીધી રેખાઓ રજૂ કરીએ છીએ, ત્યારે તે કાં તો એક બિંદુ પર છેદે છે, સમાંતર હોઈ શકે છે અને ક્યારેય સ્પર્શ કરી શકતી નથી, અથવા સંપૂર્ણપણે ઓવરલેપ થઈ શકે છે. આ દ્રશ્ય ભૂમિતિ બરાબર છે જે રેખીય સમીકરણોની જોડી સાથે થાય છે!"
    })

    # 4. REVEAL
    blocks.append({
        "id": "KOBJ_10_MATH_CH3_REV_01",
        "type": "theory",
        "title": "General Form of a Linear Equation",
        "title_hi": "रैखिक समीकरण का सामान्य रूप",
        "title_gu": "રેખીય સમીકરણનું સામાન્ય સ્વરૂપ",
        "body": "An equation of the form ax + by + c = 0, where a, b, and c are real numbers, and a and b are not both zero, is called a linear equation in two variables x and y.",
        "body_hi": "ax + by + c = 0 के रूप का एक समीकरण, जहाँ a, b, और c वास्तविक संख्याएँ हैं, और a और b दोनों शून्य नहीं हैं, दो चरों x और y में एक रैखिक समीकरण कहलाता है।",
        "body_gu": "ax + by + c = 0 ના સ્વરૂપનું સમીકરણ, જ્યાં a, b અને c વાસ્તવિક સંખ્યાઓ છે, અને a અને b બંને શૂન્ય નથી, તેને x અને y બે ચલોમાં રેખીય સમીકરણ કહેવાય છે."
    })

    # 5. KNOWLEDGE CHECK
    blocks.append({
        "id": "KOBJ_10_MATH_CH3_KC_01",
        "type": "mcq",
        "question": "Which of the following is a linear equation in two variables?",
        "question_hi": "निम्नलिखित में से कौन दो चरों में एक रैखिक समीकरण है?",
        "question_gu": "નીચેનામાંથી કયું બે ચલોમાં રેખીય સમીકરણ છે?",
        "options": ["2x^2 + 3y = 5", "x + y + z = 1", "3x - 4y = 7", "5x = 10"],
        "options_hi": ["2x^2 + 3y = 5", "x + y + z = 1", "3x - 4y = 7", "5x = 10"],
        "options_gu": ["2x^2 + 3y = 5", "x + y + z = 1", "3x - 4y = 7", "5x = 10"],
        "correct_index": 2,
        "explanation": "3x - 4y = 7 is of the form ax + by + c = 0 with two variables.",
        "explanation_hi": "3x - 4y = 7, दो चरों के साथ ax + by + c = 0 के रूप में है।",
        "explanation_gu": "3x - 4y = 7 એ બે ચલો સાથે ax + by + c = 0 ના સ્વરૂપમાં છે."
    })

    # 6. REFLECTION
    blocks.append({
        "id": "KOBJ_10_MATH_CH3_REFL_01",
        "type": "reflection",
        "title": "Your Turn",
        "title_hi": "आपकी बारी",
        "title_gu": "તમારો વારો",
        "body": "Explain in your own words the difference between 'consistent' and 'inconsistent' pair of linear equations.",
        "body_hi": "अपने शब्दों में रैखिक समीकरणों के 'संगत' (consistent) और 'असंगत' (inconsistent) युग्म के बीच का अंतर स्पष्ट करें।",
        "body_gu": "તમારા પોતાના શબ્દોમાં રેખીય સમીકરણોની 'સુસંગત' (consistent) અને 'અસંગત' (inconsistent) જોડી વચ્ચેનો તફાવત સમજાવો."
    })

    # 7. CONNECTION
    blocks.append({
        "id": "KOBJ_10_MATH_CH3_CONN_01",
        "type": "theory",
        "title": "Connecting to Graphs",
        "title_hi": "ग्राफ से जोड़ना",
        "title_gu": "આલેખ સાથે જોડવું",
        "body": "Remember when we plotted points on a coordinate plane in Class 9? A pair of linear equations simply gives us two lines on that same plane. Where they cross is our solution!",
        "body_hi": "याद करें जब हमने कक्षा 9 में एक निर्देशांक तल पर बिंदुओं को आलेखित किया था? रैखिक समीकरणों का एक जोड़ा हमें उसी तल पर दो रेखाएँ देता है। जहाँ वे पार करते हैं वह हमारा समाधान है!",
        "body_gu": "યાદ કરો જ્યારે આપણે ધોરણ 9 માં સંકલન સમતલ પર બિંદુઓનું આલેખન કર્યું હતું? રેખીય સમીકરણોની જોડી આપણને સમાન સમતલ પર બે રેખાઓ આપે છે. જ્યાં તેઓ પાર કરે છે તે આપણો ઉકેલ છે!"
    })

    # 8. MASTERY
    blocks.append({
        "id": "KOBJ_10_MATH_CH3_MAST_01",
        "type": "mastery",
        "title": "The Final Challenge",
        "title_hi": "अंतिम चुनौती",
        "title_gu": "અંતિમ પડકાર",
        "body": "Use the substitution method to solve the equations: x + y = 14 and x - y = 4. What are the values of x and y?",
        "body_hi": "समीकरणों को हल करने के लिए प्रतिस्थापन विधि का उपयोग करें: x + y = 14 और x - y = 4. x और y के मान क्या हैं?",
        "body_gu": "સમીકરણો ઉકેલવા માટે આદેશની રીત (substitution method) નો ઉપયોગ કરો: x + y = 14 અને x - y = 4. x અને y ના મૂલ્યો શું છે?"
    })

    # Now we generate 50-60 MCQs representing the exercise questions
    q_id_counter = 1

    def add_mcq(q, q_hi, q_gu, opts, opts_hi, opts_gu, ci, exp, exp_hi, exp_gu):
        nonlocal q_id_counter
        blocks.append({
            "id": f"KOBJ_10_MATH_CH3_Q_{q_id_counter:03d}",
            "type": "mcq",
            "question": q,
            "question_hi": q_hi,
            "question_gu": q_gu,
            "options": opts,
            "options_hi": opts_hi,
            "options_gu": opts_gu,
            "correct_index": ci,
            "explanation": exp,
            "explanation_hi": exp_hi,
            "explanation_gu": exp_gu
        })
        q_id_counter += 1

    # 1. Nature of lines (15 questions)
    # Generate random linear equations
    for _ in range(5):
        # Intersecting lines: a1/a2 != b1/b2
        a1, b1 = random.choice([(2,3), (3,4), (1,2), (5,-1), (2,-3)])
        a2, b2 = random.choice([(3,2), (1,3), (2,1), (3,-2), (1,-1)])
        if a1*b2 == a2*b1: a2 += 1
        c1, c2 = random.randint(-5, 5), random.randint(-5, 5)
        
        eq1 = f"{a1}x + {b1}y + ({c1}) = 0"
        eq2 = f"{a2}x + {b2}y + ({c2}) = 0"
        
        add_mcq(
            f"The pair of equations {eq1} and {eq2} have:",
            f"समीकरणों के युग्म {eq1} और {eq2} का/के:",
            f"સમીકરણોની જોડી {eq1} અને {eq2} ને:",
            ["Unique solution", "No solution", "Infinitely many solutions", "Two solutions"],
            ["अद्वितीय समाधान", "कोई समाधान नहीं", "अपरिमित रूप से अनेक समाधान", "दो समाधान"],
            ["અનન્ય ઉકેલ", "કોઈ ઉકેલ નથી", "અનંત ઉકેલો", "બે ઉકેલો"],
            0,
            f"Here a1/a2 = {a1}/{a2} and b1/b2 = {b1}/{b2}. Since a1/a2 != b1/b2, the lines intersect and have a unique solution.",
            f"यहाँ a1/a2 = {a1}/{a2} और b1/b2 = {b1}/{b2}। चूँकि a1/a2 != b1/b2, रेखाएँ प्रतिच्छेद करती हैं और इनका एक अद्वितीय समाधान है।",
            f"અહીં a1/a2 = {a1}/{a2} અને b1/b2 = {b1}/{b2}. કારણ કે a1/a2 != b1/b2, રેખાઓ છેદે છે અને તેનો અનન્ય ઉકેલ છે."
        )

    for _ in range(5):
        # Parallel lines: a1/a2 == b1/b2 != c1/c2
        k = random.randint(2, 4)
        a1, b1 = random.randint(1, 4), random.randint(1, 4)
        a2, b2 = a1 * k, b1 * k
        c1 = random.randint(1, 5)
        c2 = c1 * k + random.randint(1, 3) # ensure not equal ratio
        
        eq1 = f"{a1}x + {b1}y + {c1} = 0"
        eq2 = f"{a2}x + {b2}y + {c2} = 0"
        
        add_mcq(
            f"The pair of equations {eq1} and {eq2} have:",
            f"समीकरणों के युग्म {eq1} और {eq2} का/के:",
            f"સમીકરણોની જોડી {eq1} અને {eq2} ને:",
            ["Unique solution", "No solution", "Infinitely many solutions", "Two solutions"],
            ["अद्वितीय समाधान", "कोई समाधान नहीं", "अपरिमित रूप से अनेक समाधान", "दो समाधान"],
            ["અનન્ય ઉકેલ", "કોઈ ઉકેલ નથી", "અનંત ઉકેલો", "બે ઉકેલો"],
            1,
            f"Here a1/a2 = {a1}/{a2} = 1/{k}, b1/b2 = 1/{k}, but c1/c2 = {c1}/{c2}. Since a1/a2 = b1/b2 != c1/c2, lines are parallel.",
            f"यहाँ a1/a2 = {a1}/{a2} = 1/{k}, b1/b2 = 1/{k}, लेकिन c1/c2 = {c1}/{c2}। चूँकि a1/a2 = b1/b2 != c1/c2, रेखाएँ समानांतर हैं।",
            f"અહીં a1/a2 = {a1}/{a2} = 1/{k}, b1/b2 = 1/{k}, પરંતુ c1/c2 = {c1}/{c2}. કારણ કે a1/a2 = b1/b2 != c1/c2, રેખાઓ સમાંતર છે."
        )

    for _ in range(5):
        # Coincident lines: a1/a2 == b1/b2 == c1/c2
        k = random.randint(2, 4)
        a1, b1, c1 = random.randint(1, 4), random.randint(1, 4), random.randint(1, 5)
        a2, b2, c2 = a1 * k, b1 * k, c1 * k
        
        eq1 = f"{a1}x + {b1}y + {c1} = 0"
        eq2 = f"{a2}x + {b2}y + {c2} = 0"
        
        add_mcq(
            f"The pair of equations {eq1} and {eq2} have:",
            f"समीकरणों के युग्म {eq1} और {eq2} का/के:",
            f"સમીકરણોની જોડી {eq1} અને {eq2} ને:",
            ["Unique solution", "No solution", "Infinitely many solutions", "Two solutions"],
            ["अद्वितीय समाधान", "कोई समाधान नहीं", "अपरिमित रूप से अनेक समाधान", "दो समाधान"],
            ["અનન્ય ઉકેલ", "કોઈ ઉકેલ નથી", "અનંત ઉકેલો", "બે ઉકેલો"],
            2,
            f"Here a1/a2 = {a1}/{a2} = 1/{k}, b1/b2 = {b1}/{b2} = 1/{k}, c1/c2 = {c1}/{c2} = 1/{k}. Since all ratios are equal, lines are coincident.",
            f"यहाँ a1/a2 = b1/b2 = c1/c2 = 1/{k}। चूँकि सभी अनुपात समान हैं, रेखाएँ संपाती हैं।",
            f"અહીં a1/a2 = b1/b2 = c1/c2 = 1/{k}. કારણ કે તમામ ગુણોત્તર સમાન છે, રેખાઓ એકરૂપ છે."
        )

    # 2. Find value of k (10 questions)
    for _ in range(10):
        val = random.randint(2, 6)
        a1, b1 = random.randint(1, 4), random.randint(1, 4)
        a2 = a1 * val
        # b2 is k
        add_mcq(
            f"For what value of k, do the equations {a1}x + {b1}y = 5 and {a2}x + ky = 10 represent parallel or coincident lines (i.e. not intersecting)?",
            f"k के किस मान के लिए, समीकरण {a1}x + {b1}y = 5 और {a2}x + ky = 10 समानांतर या संपाती रेखाओं का प्रतिनिधित्व करते हैं?",
            f"k ના કયા મૂલ્ય માટે, સમીકરણો {a1}x + {b1}y = 5 અને {a2}x + ky = 10 સમાંતર અથવા એકરૂપ રેખાઓનું પ્રતિનિધિત્વ કરે છે?",
            [str(b1*val), str(b1*val + 1), str(b1*val - 1), str(-b1*val)],
            [str(b1*val), str(b1*val + 1), str(b1*val - 1), str(-b1*val)],
            [str(b1*val), str(b1*val + 1), str(b1*val - 1), str(-b1*val)],
            0,
            f"For lines to not intersect uniquely, a1/a2 = b1/b2. So {a1}/{a2} = {b1}/k => 1/{val} = {b1}/k => k = {b1*val}.",
            f"रेखाओं के विशिष्ट रूप से प्रतिच्छेद न करने के लिए, a1/a2 = b1/b2. अतः 1/{val} = {b1}/k => k = {b1*val}.",
            f"રેખાઓ અનન્ય રીતે છેદે નહીં તે માટે, a1/a2 = b1/b2. તેથી 1/{val} = {b1}/k => k = {b1*val}."
        )

    # 3. Solving equations (15 questions)
    for _ in range(15):
        x = random.randint(-5, 5)
        y = random.randint(-5, 5)
        a1, b1 = random.randint(1, 4), random.choice([-3, -2, -1, 1, 2, 3])
        a2, b2 = random.randint(1, 4), random.choice([-3, -2, -1, 1, 2, 3])
        if a1*b2 == a2*b1: 
            a2 += 1
        
        c1 = a1*x + b1*y
        c2 = a2*x + b2*y
        
        eq1 = f"{a1}x {'+' if b1>0 else '-'} {abs(b1)}y = {c1}"
        eq2 = f"{a2}x {'+' if b2>0 else '-'} {abs(b2)}y = {c2}"
        
        opts = [
            f"x = {x}, y = {y}",
            f"x = {x+1}, y = {y-1}",
            f"x = {y}, y = {x}",
            f"x = {-x}, y = {-y}"
        ]
        correct = 0
        
        add_mcq(
            f"Solve for x and y: {eq1} and {eq2}",
            f"x और y के लिए हल करें: {eq1} और {eq2}",
            f"x અને y માટે ઉકેલો: {eq1} અને {eq2}",
            opts, opts, opts,
            correct,
            f"By solving the equations using substitution or elimination, we get x = {x} and y = {y}.",
            f"प्रतिस्थापन या विलोपन विधि से हल करने पर, हमें x = {x} और y = {y} मिलता है।",
            f"આદેશ અથવા લોપની રીતનો ઉપયોગ કરીને સમીકરણો ઉકેલવાથી, આપણને x = {x} અને y = {y} મળે છે."
        )

    # 4. Word problems - Ages (5 questions)
    for i in range(5):
        son_age = random.randint(10, 20)
        father_age = son_age * random.randint(2, 4) + random.randint(0, 5)
        
        diff = father_age - son_age
        sum_ages = father_age + son_age
        
        add_mcq(
            f"The sum of the ages of a father and his son is {sum_ages} years. The difference of their ages is {diff} years. Find the age of the father.",
            f"एक पिता और उसके पुत्र की आयु का योग {sum_ages} वर्ष है। उनकी आयु का अंतर {diff} वर्ष है। पिता की आयु ज्ञात कीजिए।",
            f"પિતા અને તેના પુત્રની ઉંમરનો સરવાળો {sum_ages} વર્ષ છે. તેમની ઉંમરનો તફાવત {diff} વર્ષ છે. પિતાની ઉંમર શોધો.",
            [f"{father_age} years", f"{father_age - 2} years", f"{father_age + 2} years", f"{son_age} years"],
            [f"{father_age} वर्ष", f"{father_age - 2} वर्ष", f"{father_age + 2} वर्ष", f"{son_age} वर्ष"],
            [f"{father_age} વર્ષ", f"{father_age - 2} વર્ષ", f"{father_age + 2} વર્ષ", f"{son_age} વર્ષ"],
            0,
            f"Let father's age be x and son's age be y. x + y = {sum_ages}, x - y = {diff}. Adding gives 2x = {sum_ages + diff} => x = {father_age}.",
            f"माना पिता की आयु x है और पुत्र की आयु y है। x + y = {sum_ages}, x - y = {diff}. जोड़ने पर 2x = {sum_ages + diff} => x = {father_age} मिलता है।",
            f"ધારો કે પિતાની ઉંમર x છે અને પુત્રની ઉંમર y છે. x + y = {sum_ages}, x - y = {diff}. ઉમેરવાથી 2x = {sum_ages + diff} => x = {father_age} મળે છે."
        )

    # 5. Word problems - Fractions (5 questions)
    for i in range(5):
        num = random.randint(2, 7)
        den = num + random.randint(1, 5)
        
        num_new = num + 1
        num_new_str = f"{num_new}/{den}"
        
        den_new = den + 1
        den_new_str = f"{num}/{den_new}"
        
        add_mcq(
            f"A fraction becomes {num_new_str} if 1 is added to the numerator. It becomes {den_new_str} if 1 is added to the denominator. Find the fraction.",
            f"एक भिन्न {num_new_str} हो जाता है यदि अंश में 1 जोड़ा जाए। यदि हर में 1 जोड़ा जाए तो यह {den_new_str} हो जाता है। भिन्न ज्ञात कीजिए।",
            f"જો અંશમાં 1 ઉમેરવામાં આવે તો અપૂર્ણાંક {num_new_str} બને છે. જો છેદમાં 1 ઉમેરવામાં આવે તો તે {den_new_str} બને છે. અપૂર્ણાંક શોધો.",
            [f"{num}/{den}", f"{num+1}/{den-1}", f"{den}/{num}", f"{num-1}/{den+1}"],
            [f"{num}/{den}", f"{num+1}/{den-1}", f"{den}/{num}", f"{num-1}/{den+1}"],
            [f"{num}/{den}", f"{num+1}/{den-1}", f"{den}/{num}", f"{num-1}/{den+1}"],
            0,
            f"Let fraction be x/y. (x+1)/y = {num_new_str} and x/(y+1) = {den_new_str}. Solving these gives x = {num} and y = {den}.",
            f"माना भिन्न x/y है। (x+1)/y = {num_new_str} और x/(y+1) = {den_new_str}। इन्हें हल करने पर x = {num} और y = {den} प्राप्त होता है।",
            f"ધારો કે અપૂર્ણાંક x/y છે. (x+1)/y = {num_new_str} અને x/(y+1) = {den_new_str}. આને ઉકેલવાથી x = {num} અને y = {den} મળે છે."
        )
        
    # 6. Word problems - Two digit numbers (5 questions)
    for i in range(5):
        t = random.randint(2, 8)
        u = random.randint(1, 9)
        num = t * 10 + u
        sum_digits = t + u
        diff = (t - u) * 9
        
        if diff < 0:
            cond = f"If {abs(diff)} is added to the number, its digits are reversed."
            cond_hi = f"यदि संख्या में {abs(diff)} जोड़ा जाता है, तो इसके अंक उलट जाते हैं।"
            cond_gu = f"જો સંખ્યામાં {abs(diff)} ઉમેરવામાં આવે, તો તેના અંકો ઉલટાઈ જાય છે."
        else:
            cond = f"If {diff} is subtracted from the number, its digits are reversed."
            cond_hi = f"यदि संख्या से {diff} घटाया जाता है, तो इसके अंक उलट जाते हैं।"
            cond_gu = f"જો સંખ્યામાંથી {diff} બાદ કરવામાં આવે, તો તેના અંકો ઉલટાઈ જાય છે."
            
        if diff == 0:
            cond = f"The units digit equals the tens digit."
            cond_hi = "इकाई का अंक दहाई के अंक के बराबर है।"
            cond_gu = "એકમનો અંક દશકના અંક બરાબર છે."
            
        add_mcq(
            f"The sum of the digits of a two-digit number is {sum_digits}. {cond} Find the number.",
            f"दो अंकों की एक संख्या के अंकों का योग {sum_digits} है। {cond_hi} संख्या ज्ञात कीजिए।",
            f"બે અંકની સંખ્યાના અંકોનો સરવાળો {sum_digits} છે. {cond_gu} સંખ્યા શોધો.",
            [str(num), str(u*10+t), str(num+9), str(abs(num-18))],
            [str(num), str(u*10+t), str(num+9), str(abs(num-18))],
            [str(num), str(u*10+t), str(num+9), str(abs(num-18))],
            0,
            f"Let tens digit be x and units be y. x+y={sum_digits}. Reversing the digits and applying the condition yields the number {num}.",
            f"माना दहाई का अंक x है और इकाई का अंक y है। x+y={sum_digits}। अंकों को उलटने और शर्त लागू करने पर संख्या {num} प्राप्त होती है।",
            f"ધારો કે દશકનો અંક x છે અને એકમનો અંક y છે. x+y={sum_digits}. અંકોને ઉલટાવીને અને શરત લાગુ કરવાથી સંખ્યા {num} મળે છે."
        )

    # 7. Word problems - Cost (10 questions)
    for i in range(10):
        cost1 = random.randint(3, 10)
        cost2 = random.randint(2, 8)
        qty1_1, qty1_2 = random.randint(2, 5), random.randint(3, 6)
        qty2_1, qty2_2 = random.randint(3, 6), random.randint(2, 5)
        
        total1 = cost1 * qty1_1 + cost2 * qty1_2
        total2 = cost1 * qty2_1 + cost2 * qty2_2
        
        add_mcq(
            f"The cost of {qty1_1} pens and {qty1_2} pencils is Rs {total1}. The cost of {qty2_1} pens and {qty2_2} pencils is Rs {total2}. Find the cost of one pen.",
            f"{qty1_1} पेन और {qty1_2} पेंसिल की कीमत {total1} रुपये है। {qty2_1} पेन और {qty2_2} पेंसिल की कीमत {total2} रुपये है। एक पेन की कीमत ज्ञात कीजिए।",
            f"{qty1_1} પેન અને {qty1_2} પેન્સિલની કિંમત {total1} રૂપિયા છે. {qty2_1} પેન અને {qty2_2} પેન્સિલની કિંમત {total2} રૂપિયા છે. એક પેનની કિંમત શોધો.",
            [f"Rs {cost1}", f"Rs {cost2}", f"Rs {cost1 + 2}", f"Rs {cost1 - 1}"],
            [f"{cost1} रुपये", f"{cost2} रुपये", f"{cost1 + 2} रुपये", f"{cost1 - 1} रुपये"],
            [f"{cost1} રૂપિયા", f"{cost2} રૂપિયા", f"{cost1 + 2} રૂપિયા", f"{cost1 - 1} રૂપિયા"],
            0,
            f"Let cost of 1 pen be x and 1 pencil be y. {qty1_1}x + {qty1_2}y = {total1} and {qty2_1}x + {qty2_2}y = {total2}. Solving gives x = {cost1}.",
            f"माना 1 पेन की कीमत x और 1 पेंसिल की कीमत y है। {qty1_1}x + {qty1_2}y = {total1} और {qty2_1}x + {qty2_2}y = {total2}। हल करने पर x = {cost1} मिलता है।",
            f"ધારો કે 1 પેનની કિંમત x અને 1 પેન્સિલની કિંમત y છે. {qty1_1}x + {qty1_2}y = {total1} અને {qty2_1}x + {qty2_2}y = {total2}. ઉકેલવાથી x = {cost1} મળે છે."
        )

    # 8. Word problems - Speed/Distance (10 questions)
    for i in range(10):
        speed_boat = random.randint(10, 20)
        speed_stream = random.randint(2, 6)
        
        speed_down = speed_boat + speed_stream
        speed_up = speed_boat - speed_stream
        
        dist_down = speed_down * random.randint(2, 4)
        dist_up = speed_up * random.randint(2, 4)
        
        add_mcq(
            f"A boat goes {dist_down} km downstream and {dist_up} km upstream. Its downstream speed is {speed_down} km/h and upstream speed is {speed_up} km/h. Find the speed of the boat in still water.",
            f"एक नाव {dist_down} किमी धारा के अनुकूल और {dist_up} किमी धारा के प्रतिकूल जाती है। इसकी धारा के अनुकूल गति {speed_down} किमी/घंटा और धारा के प्रतिकूल गति {speed_up} किमी/घंटा है। शांत जल में नाव की गति ज्ञात कीजिए।",
            f"એક હોડી {dist_down} કિમી પ્રવાહની દિશામાં અને {dist_up} કિમી પ્રવાહની વિરુદ્ધ દિશામાં જાય છે. તેની પ્રવાહની દિશામાં ઝડપ {speed_down} કિમી/કલાક અને પ્રવાહની વિરુદ્ધ દિશામાં ઝડપ {speed_up} કિમી/કલાક છે. સ્થિર પાણીમાં હોડીની ઝડપ શોધો.",
            [f"{speed_boat} km/h", f"{speed_stream} km/h", f"{speed_boat + 2} km/h", f"{speed_boat - 2} km/h"],
            [f"{speed_boat} किमी/घंटा", f"{speed_stream} किमी/घंटा", f"{speed_boat + 2} किमी/घंटा", f"{speed_boat - 2} किमी/घंटा"],
            [f"{speed_boat} કિમી/કલાક", f"{speed_stream} કિમી/કલાક", f"{speed_boat + 2} કિમી/કલાક", f"{speed_boat - 2} કિમી/કલાક"],
            0,
            f"Let speed of boat in still water be x and stream be y. x+y={speed_down} and x-y={speed_up}. Adding gives 2x = {speed_down+speed_up} => x = {speed_boat}.",
            f"माना शांत जल में नाव की गति x है और धारा की गति y है। x+y={speed_down} और x-y={speed_up}। जोड़ने पर 2x = {speed_down+speed_up} => x = {speed_boat} मिलता है।",
            f"ધારો કે સ્થિર પાણીમાં હોડીની ઝડપ x અને પ્રવાહની ઝડપ y છે. x+y={speed_down} અને x-y={speed_up}. ઉમેરવાથી 2x = {speed_down+speed_up} => x = {speed_boat} મળે છે."
        )

    # Output to file
    with open('app_core/chapters/ncert_class10_maths_ch3.json', 'w', encoding='utf-8') as f:
        json.dump({"metadata": metadata, "blocks": blocks}, f, ensure_ascii=False, indent=2)
        
if __name__ == '__main__':
    generate_chapter()
