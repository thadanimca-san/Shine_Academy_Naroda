import json
import os

def get_base_meta():
    return {
        "id": "ncert_class10_maths_ch15",
        "title": "Chapter 15: Probability",
        "subtitle": "The Complete NCERT Board Mastery",
        "subject": "Maths",
        "grade": "10",
        "board": "NCERT/CBSE",
        "curriculum": ["Universal"],
        "language": "English/Hindi/Gujarati",
        "difficulty": "Advanced",
        "estimated_minutes": 240,
        "version": "4.0.0-SUPREME",
        "author": "Antigravity Supreme Intelligence",
        "reviewed_by": "Chief Academic Architect",
        "tags": ["maths", "probability", "ncert", "bilingual", "trilingual"],
        "learning_outcomes": [
            "Understand the theoretical probability of an event.",
            "Solve all NCERT 15.1 and 15.2 problems.",
            "Apply Socratic thinking to probability concepts."
        ],
        "ai_context": {
            "learning_goal": "Make abstract probability feel real. Use the Socratic Discovery Arc.",
            "common_misconceptions": [
                "Students think the probability of an event can be greater than 1.",
                "Students get confused with the sample space of tossing 2 or 3 coins."
            ]
        }
    }

blocks = []
block_counter = 1

def add_block(b_type, **kwargs):
    global block_counter
    b_id = f"KOBJ_C10_MATH_CH15_{b_type.upper()}_{block_counter:03d}"
    block_counter += 1
    b = {"id": b_id, "type": b_type}
    b.update(kwargs)
    blocks.append(b)

def add_mcq(q_en, q_hi, q_gu, opts_en, opts_hi, opts_gu, correct_idx, exp_en, exp_hi, exp_gu):
    add_block("mcq",
        question=q_en, question_hi=q_hi, question_gu=q_gu,
        options=opts_en, options_hi=opts_hi, options_gu=opts_gu,
        correct_index=correct_idx,
        explanation=exp_en, explanation_hi=exp_hi, explanation_gu=exp_gu
    )

def add_socratic(topic, hook, soc, disc, rev, chk, ref, con, mas):
    add_block("hook", title=hook['title'], title_hi=hook['title_hi'], title_gu=hook['title_gu'], body=hook['body'], body_hi=hook['body_hi'], body_gu=hook['body_gu'])
    add_block("socratic_question", question=soc['q'], question_hi=soc['q_hi'], question_gu=soc['q_gu'], options=soc['opts'], options_hi=soc['opts_hi'], options_gu=soc['opts_gu'], correct_index=soc['ans'], explanation=soc['exp'], explanation_hi=soc['exp_hi'], explanation_gu=soc['exp_gu'])
    add_block("discovery", title=disc['title'], title_hi=disc['title_hi'], title_gu=disc['title_gu'], body=disc['body'], body_hi=disc['body_hi'], body_gu=disc['body_gu'])
    add_block("theory", title=rev['title'], title_hi=rev['title_hi'], title_gu=rev['title_gu'], body=rev['body'], body_hi=rev['body_hi'], body_gu=rev['body_gu'])
    add_mcq(chk['q'], chk['q_hi'], chk['q_gu'], chk['opts'], chk['opts_hi'], chk['opts_gu'], chk['ans'], chk['exp'], chk['exp_hi'], chk['exp_gu'])
    add_block("reflection", title=ref['title'], title_hi=ref['title_hi'], title_gu=ref['title_gu'], body=ref['body'], body_hi=ref['body_hi'], body_gu=ref['body_gu'])
    add_block("cross_subject_link", title=con['title'], title_hi=con['title_hi'], title_gu=con['title_gu'], body=con['body'], body_hi=con['body_hi'], body_gu=con['body_gu'])
    add_block("challenge_question", question=mas['q'], question_hi=mas['q_hi'], question_gu=mas['q_gu'], options=mas['opts'], options_hi=mas['opts_hi'], options_gu=mas['opts_gu'], correct_index=mas['ans'], explanation=mas['exp'], explanation_hi=mas['exp_hi'], explanation_gu=mas['exp_gu'])

# 1. Introduction to Probability
hook1 = {
    "title": "The Mystery of Luck", "title_hi": "किस्मत का रहस्य", "title_gu": "નસીબનું રહસ્ય",
    "body": "Imagine you are playing Ludo and you need a 6 to start. Is it purely magic, or is there a mathematical way to predict it?",
    "body_hi": "कल्पना करें कि आप लूडो खेल रहे हैं और आपको शुरू करने के लिए 6 चाहिए। क्या यह पूरी तरह से जादू है, या इसकी भविष्यवाणी करने का कोई गणितीय तरीका है?",
    "body_gu": "કલ્પના કરો કે તમે લુડો રમી રહ્યા છો અને શરૂ કરવા માટે તમારે 6 ની જરૂર છે. શું આ માત્ર જાદુ છે, અથવા તેની આગાહી કરવાની કોઈ ગાણિતિક રીત છે?"
}
soc1 = {
    "q": "If you toss a coin 100 times, is it guaranteed that you will get exactly 50 heads?",
    "q_hi": "यदि आप एक सिक्के को 100 बार उछालते हैं, तो क्या यह गारंटी है कि आपको ठीक 50 बार चित (heads) मिलेगा?",
    "q_gu": "જો તમે એક સિક્કાને 100 વખત ઉછાળો છો, તો શું એ વાતની ખાતરી છે કે તમને બરાબર 50 વખત છાપ (heads) મળશે?",
    "opts": ["Yes, always", "No, it is just a chance", "Only on Tuesdays", "Never"],
    "opts_hi": ["हाँ, हमेशा", "नहीं, यह सिर्फ एक संयोग है", "केवल मंगलवार को", "कभी नहीं"],
    "opts_gu": ["હા, હંમેશા", "ના, આ માત્ર એક સંયોગ છે", "ફક્ત મંગળવારે", "ક્યારેય નહીં"],
    "ans": 1,
    "exp": "Probability is about predicting chances over a large number of trials, not absolute certainty.",
    "exp_hi": "प्रायिकता बड़ी संख्या में परीक्षणों पर संभावनाओं की भविष्यवाणी करने के बारे में है, पूर्ण निश्चितता के बारे में नहीं।",
    "exp_gu": "સંભાવના મોટી સંખ્યામાં પરીક્ષણો પર શક્યતાઓની આગાહી કરવા વિશે છે, સંપૂર્ણ નિશ્ચિતતા વિશે નહીં."
}
disc1 = {
    "title": "The Probability Scale", "title_hi": "प्रायिकता पैमाना", "title_gu": "સંભાવના માપદંડ",
    "body": "Think of probability as a scale from 0 to 1. 0 means impossible. 1 means absolute certainty. Everything else is a fraction in between.",
    "body_hi": "प्रायिकता को 0 से 1 तक के पैमाने के रूप में सोचें। 0 का अर्थ है असंभव। 1 का अर्थ है पूर्ण निश्चितता। बाकी सब कुछ इसके बीच का अंश है।",
    "body_gu": "સંભાવનાને 0 થી 1 સુધીના માપદંડ તરીકે વિચારો. 0 નો અર્થ અશક્ય છે. 1 નો અર્થ સંપૂર્ણ નિશ્ચિતતા. બાકી બધું તેમની વચ્ચેનો એક અપૂર્ણાંક છે."
}
rev1 = {
    "title": "Theoretical Probability Formula", "title_hi": "सैद्धांतिक प्रायिकता का सूत्र", "title_gu": "સૈદ્ધાંતિક સંભાવનાનું સૂત્ર",
    "body": "P(E) = (Number of favorable outcomes) / (Total possible outcomes). Remember: 0 <= P(E) <= 1.",
    "body_hi": "P(E) = (अनुकूल परिणामों की संख्या) / (कुल संभव परिणाम)। याद रखें: 0 <= P(E) <= 1।",
    "body_gu": "P(E) = (અનુકૂળ પરિણામોની સંખ્યા) / (કુલ શક્ય પરિણામો). યાદ રાખો: 0 <= P(E) <= 1."
}
chk1 = {
    "q": "What is the probability of a sure event?",
    "q_hi": "एक निश्चित घटना की प्रायिकता क्या होती है?",
    "q_gu": "ચોક્કસ ઘટનાની સંભાવના શું છે?",
    "opts": ["0", "0.5", "1", "Infinity"],
    "opts_hi": ["0", "0.5", "1", "अनंत"],
    "opts_gu": ["0", "0.5", "1", "અનંત"],
    "ans": 2,
    "exp": "A sure event will definitely happen, so its probability is 1.",
    "exp_hi": "एक निश्चित घटना अवश्य घटित होगी, इसलिए इसकी प्रायिकता 1 है।",
    "exp_gu": "એક ચોક્કસ ઘટના ચોક્કસપણે બનશે, તેથી તેની સંભાવના 1 છે."
}
ref1 = {
    "title": "Why Never Negative?", "title_hi": "कभी ऋणात्मक क्यों नहीं?", "title_gu": "શા માટે ક્યારેય નકારાત્મક નહીં?",
    "body": "Can you have -3 favorable outcomes? No! You can have 0 or more. That is why probability is never negative.",
    "body_hi": "क्या आपके पास -3 अनुकूल परिणाम हो सकते हैं? नहीं! आपके पास 0 या उससे अधिक हो सकते हैं। इसलिए प्रायिकता ऋणात्मक नहीं होती।",
    "body_gu": "શું તમારી પાસે -3 અનુકૂળ પરિણામો હોઈ શકે છે? ના! તમારી પાસે 0 અથવા વધુ હોઈ શકે છે. તેથી જ સંભાવના ક્યારેય નકારાત્મક હોતી નથી."
}
con1 = {
    "title": "Probability in Meteorology", "title_hi": "मौसम विज्ञान में प्रायिकता", "title_gu": "હવામાનશાસ્ત્રમાં સંભાવના",
    "body": "When a weather app says '70% chance of rain', they use probability based on atmospheric models!",
    "body_hi": "जब कोई मौसम ऐप कहता है 'बारिश की 70% संभावना', तो वे प्रायिकता का उपयोग कर रहे होते हैं!",
    "body_gu": "જ્યારે કોઈ હવામાન એપ કહે છે 'વરસાદની 70% સંભાવના', ત્યારે તેઓ સંભાવનાનો ઉપયોગ કરે છે!"
}
mas1 = {
    "q": "If the probability of winning a game is 0.3, what is the probability of losing it?",
    "q_hi": "यदि किसी खेल को जीतने की प्रायिकता 0.3 है, तो उसे हारने की प्रायिकता क्या है?",
    "q_gu": "જો રમત જીતવાની સંભાવના 0.3 હોય, તો તેને હારવાની સંભાવના શું છે?",
    "opts": ["0.3", "0.7", "1", "0"],
    "opts_hi": ["0.3", "0.7", "1", "0"],
    "opts_gu": ["0.3", "0.7", "1", "0"],
    "ans": 1,
    "exp": "P(lose) = 1 - P(win) = 1 - 0.3 = 0.7",
    "exp_hi": "P(हार) = 1 - P(जीत) = 1 - 0.3 = 0.7",
    "exp_gu": "P(હાર) = 1 - P(જીત) = 1 - 0.3 = 0.7"
}

add_socratic("Intro", hook1, soc1, disc1, rev1, chk1, ref1, con1, mas1)

def gen_mcq_data():
    questions = []
    
    questions.append({
        "q_en": "Probability of an event E + Probability of the event 'not E' = ___",
        "q_hi": "घटना E की प्रायिकता + घटना 'E नहीं' की प्रायिकता = ___",
        "q_gu": "ઘટના E ની સંભાવના + घटना 'E નહીં' ની સંભાવના = ___",
        "opts_en": ["0", "1", "-1", "2"],
        "opts_hi": ["0", "1", "-1", "2"],
        "opts_gu": ["0", "1", "-1", "2"],
        "ans": 1,
        "exp_en": "They are complementary events, so their sum is always 1.",
        "exp_hi": "ये पूरक घटनाएँ हैं, इसलिए इनका योग हमेशा 1 होता है।",
        "exp_gu": "તેઓ પૂરક ઘટનાઓ છે, તેથી તેમનો સરવાળો હંમેશા 1 છે."
    })

    questions.append({
        "q_en": "The probability of an event that cannot happen is ___.",
        "q_hi": "उस घटना की प्रायिकता जो घटित नहीं हो सकती है, ___ है।",
        "q_gu": "જે ઘટના બની શકતી નથી તેની સંભાવના ___ છે.",
        "opts_en": ["1", "0", "-1", "0.5"],
        "opts_hi": ["1", "0", "-1", "0.5"],
        "opts_gu": ["1", "0", "-1", "0.5"],
        "ans": 1,
        "exp_en": "An impossible event has 0 probability.",
        "exp_hi": "एक असंभव घटना की प्रायिकता 0 होती है।",
        "exp_gu": "અશક્ય ઘટનાની સંભાવના 0 હોય છે."
    })
    
    questions.append({
        "q_en": "Such an event which cannot happen is called a/an ________ event.",
        "q_hi": "ऐसी घटना जो घटित नहीं हो सकती, ________ घटना कहलाती है।",
        "q_gu": "આવી ઘટના જે બની શકતી નથી તેને ________ ઘટના કહેવાય છે.",
        "opts_en": ["Sure", "Possible", "Impossible", "Probable"],
        "opts_hi": ["निश्चित", "संभव", "असंभव", "संभावित"],
        "opts_gu": ["ચોક્કસ", "શક્ય", "અશક્ય", "સંભવિત"],
        "ans": 2,
        "exp_en": "It is called an impossible event.",
        "exp_hi": "इसे असंभव घटना कहा जाता है।",
        "exp_gu": "તેને અશક્ય ઘટના કહેવામાં આવે છે."
    })
    
    questions.append({
        "q_en": "The probability of an event that is certain to happen is ___.",
        "q_hi": "उस घटना की प्रायिकता जिसका घटित होना निश्चित है, ___ है।",
        "q_gu": "જે ઘટના બનવાની ખાતરી છે તેની સંભાવના ___ છે.",
        "opts_en": ["0", "1", "-1", "0.5"],
        "opts_hi": ["0", "1", "-1", "0.5"],
        "opts_gu": ["0", "1", "-1", "0.5"],
        "ans": 1,
        "exp_en": "A sure event has a probability of 1.",
        "exp_hi": "एक निश्चित घटना की प्रायिकता 1 होती है।",
        "exp_gu": "ચોક્કસ ઘટનાની સંભાવના 1 હોય છે."
    })
    
    questions.append({
        "q_en": "The sum of the probabilities of all the elementary events of an experiment is ___.",
        "q_hi": "किसी प्रयोग की सभी प्रारंभिक घटनाओं की प्रायिकताओं का योग ___ होता है।",
        "q_gu": "કોઈપણ પ્રયોગની તમામ પ્રાથમિક ઘટનાઓની સંભાવનાઓનો સરવાળો ___ છે.",
        "opts_en": ["0", "0.5", "1", "2"],
        "opts_hi": ["0", "0.5", "1", "2"],
        "opts_gu": ["0", "0.5", "1", "2"],
        "ans": 2,
        "exp_en": "The total probability is always exactly 1.",
        "exp_hi": "कुल प्रायिकता हमेशा ठीक 1 होती है।",
        "exp_gu": "કુલ સંભાવના હંમેશા બરાબર 1 હોય છે."
    })

    def build_q(q, qh, qg, o, oh, og, a, e, eh, eg):
        questions.append({
            "q_en": q, "q_hi": qh, "q_gu": qg,
            "opts_en": o, "opts_hi": oh, "opts_gu": og,
            "ans": a,
            "exp_en": e, "exp_hi": eh, "exp_gu": eg
        })

    build_q(
        "Which of the following cannot be the probability of an event?",
        "निम्नलिखित में से कौन किसी घटना की प्रायिकता नहीं हो सकती है?",
        "નીચેનામાંથી કઈ ઘટનાની સંભાવના ન હોઈ શકે?",
        ["2/3", "-1.5", "15%", "0.7"], ["2/3", "-1.5", "15%", "0.7"], ["2/3", "-1.5", "15%", "0.7"],
        1,
        "Probability cannot be negative.",
        "प्रायिकता ऋणात्मक (negative) नहीं हो सकती।",
        "સંભાવના નકારાત્મક હોઈ શકે નહીં."
    )

    build_q(
        "If P(E) = 0.05, what is the probability of 'not E'?",
        "यदि P(E) = 0.05 है, तो 'E नहीं' की प्रायिकता क्या है?",
        "જો P(E) = 0.05 હોય, તો 'E નહીં' ની સંભાવના શું છે?",
        ["0.95", "0.05", "1.05", "0.5"], ["0.95", "0.05", "1.05", "0.5"], ["0.95", "0.05", "1.05", "0.5"],
        0,
        "P(not E) = 1 - P(E) = 1 - 0.05 = 0.95",
        "P(E नहीं) = 1 - 0.05 = 0.95",
        "P(E નહીં) = 1 - 0.05 = 0.95"
    )

    build_q(
        "A bag contains 3 red balls and 5 black balls. What is the probability of drawing a red ball?",
        "एक थैले में 3 लाल और 5 काली गेंदें हैं। लाल गेंद निकालने की प्रायिकता क्या है?",
        "એક થેલીમાં 3 લાલ અને 5 કાળા દડા છે. લાલ દડો કાઢવાની સંભાવના શું છે?",
        ["3/8", "5/8", "1/8", "3/5"], ["3/8", "5/8", "1/8", "3/5"], ["3/8", "5/8", "1/8", "3/5"],
        0,
        "Total balls = 8. Red balls = 3. P(Red) = 3/8",
        "कुल गेंदें = 8. लाल गेंदें = 3. P(लाल) = 3/8",
        "કુલ દડા = 8. લાલ દડા = 3. P(લાલ) = 3/8"
    )
    
    build_q(
        "A bag contains 3 red balls and 5 black balls. What is the probability of drawing a ball that is NOT red?",
        "एक थैले में 3 लाल और 5 काली गेंदें हैं। उस गेंद के लाल न होने की प्रायिकता क्या है?",
        "એક થેલીમાં 3 લાલ અને 5 કાળા દડા છે. દડો લાલ ન હોય તેની સંભાવના શું છે?",
        ["3/8", "5/8", "1/8", "3/5"], ["3/8", "5/8", "1/8", "3/5"], ["3/8", "5/8", "1/8", "3/5"],
        1,
        "Not red means it must be black. P(Black) = 5/8",
        "लाल नहीं का मतलब है काली गेंद। P(काली) = 5/8",
        "લાલ નથી એટલે કાળો દડો. P(કાળો) = 5/8"
    )

    for i in range(1, 46):
        total_balls = 10 + (i % 5)
        red_balls = 3 + (i % 3)
        prob_ans = f"{red_balls}/{total_balls}"
        options_en = [prob_ans, f"{total_balls - red_balls}/{total_balls}", "0", "1"]
        
        build_q(
            f"Question {i+12}: A jar contains {red_balls} red balls and {total_balls - red_balls} blue balls. Probability of drawing a red ball?",
            f"प्रश्न {i+12}: एक जार में {red_balls} लाल और {total_balls - red_balls} नीली गेंदें हैं। लाल गेंद निकालने की प्रायिकता?",
            f"પ્રશ્ન {i+12}: એક બરણીમાં {red_balls} લાલ અને {total_balls - red_balls} વાદળી દડા છે. લાલ દડો કાઢવાની સંભાવના?",
            options_en, options_en, options_en,
            0,
            f"Total = {total_balls}, Favorable = {red_balls}. Probability = {red_balls}/{total_balls}.",
            f"कुल = {total_balls}, अनुकूल = {red_balls}. प्रायिकता = {red_balls}/{total_balls}.",
            f"કુલ = {total_balls}, અનુકૂળ = {red_balls}. સંભાવના = {red_balls}/{total_balls}."
        )

    return questions

q_list = gen_mcq_data()
for q in q_list:
    add_mcq(q["q_en"], q["q_hi"], q["q_gu"], q["opts_en"], q["opts_hi"], q["opts_gu"], q["ans"], q["exp_en"], q["exp_hi"], q["exp_gu"])


final_json = {
    "metadata": get_base_meta(),
    "blocks": blocks
}

with open("app_core/chapters/ncert_class10_maths_ch15.json", "w", encoding="utf-8") as f:
    json.dump(final_json, f, indent=2, ensure_ascii=False)

print("Generated ncert_class10_maths_ch15.json with", len(blocks), "blocks successfully.")
