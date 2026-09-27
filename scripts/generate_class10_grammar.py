import json
import os

def create_grammar_chapter(ch_num, ch_title, ch_title_hi, ch_title_gu, blocks_data):
    blocks = []
    for i, b in enumerate(blocks_data):
        b["id"] = f"KOBJ_NCERT_C10_GRAMMAR_CH{ch_num}_{str(i+1).zfill(3)}"
        blocks.append(b)
        
    data = {
        "metadata": {
            "id": f"ncert_class10_grammar_ch{ch_num}",
            "title": f"English Grammar Chapter {ch_num}: {ch_title}",
            "subject": "English Grammar",
            "grade": "10"
        },
        "blocks": blocks
    }
    
    output_path = f'/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_grammar_ch{ch_num}.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Successfully wrote {len(blocks)} blocks to {output_path}")

# --- Chapter 1: Tenses ---
ch1_blocks = [
    {
        "type": "hook",
        "title": "The Time Traveler's Mistake",
        "title_hi": "समय यात्री की गलती (The Time Traveler's Mistake)",
        "title_gu": "ટાઇમ ટ્રાવેલરની ભૂલ (The Time Traveler's Mistake)",
        "body": "Imagine a time traveler who wants to warn you about tomorrow, but he says: 'I *went* to the future tomorrow!' Does that make sense? No! Because 'went' means it already happened, but 'tomorrow' hasn't happened yet! Tenses are the time-traveling tools of English. If you use the wrong tense, you might accidentally send your listener to the past instead of the future!",
        "body_hi": "कल्पना करें कि एक समय यात्री (time traveler) जो आपको कल के बारे में चेतावनी देना चाहता है, लेकिन वह कहता है: 'मैं कल भविष्य में गया था (I went to the future tomorrow)!' क्या इसका कोई मतलब है? नहीं! क्योंकि 'went' (गया था) का अर्थ है कि यह पहले ही हो चुका है, लेकिन 'कल' (tomorrow) तो अभी तक आया ही नहीं है! काल (Tenses) अंग्रेजी के समय-यात्रा उपकरण हैं। यदि आप गलत काल का उपयोग करते हैं, तो आप गलती से अपने श्रोता को भविष्य के बजाय अतीत में भेज सकते हैं!",
        "body_gu": "કલ્પના કરો કે એક સમય યાત્રી (time traveler) જે તમને આવતીકાલ વિશે ચેતવણી આપવા માંગે છે, પરંતુ તે કહે છે: 'હું આવતીકાલે ભવિષ્યમાં ગયો હતો (I went to the future tomorrow)!' શું તેનો કોઈ અર્થ છે? ના! કારણ કે 'went' (ગયો હતો) નો અર્થ થાય છે કે તે પહેલાથી જ થઈ ગયું છે, પરંતુ 'આવતીકાલ' (tomorrow) હજી આવ્યો જ નથી! કાળ (Tenses) એ અંગ્રેજીના સમય-યાત્રા સાધનો છે. જો તમે ખોટા કાળનો ઉપયોગ કરો છો, તો તમે ભૂલથી તમારા શ્રોતાને ભવિષ્યની જગ્યાએ ભૂતકાળમાં મોકલી શકો છો!"
    },
    {
        "type": "theory",
        "title": "Present Tense: What's Happening Now?",
        "title_hi": "वर्तमान काल (Present Tense): अब क्या हो रहा है?",
        "title_gu": "વર્તમાન કાળ (Present Tense): હવે શું થઈ રહ્યું છે?",
        "body": "The Present Tense tells us about things that are happening right now, or things that happen regularly (habits).\n1. Simple Present: Used for habits and facts. (e.g., The sun rises in the east. I play football.)\n2. Present Continuous: Used for actions happening at this exact moment. (e.g., I am reading a book.)\n3. Present Perfect: Used for actions that just finished, but the effect is still there. (e.g., I have finished my homework.)\n4. Present Perfect Continuous: Used for actions that started in the past and are STILL happening. (e.g., I have been studying for two hours.)",
        "body_hi": "वर्तमान काल (Present Tense) हमें उन चीजों के बारे में बताता है जो अभी हो रही हैं, या जो नियमित रूप से (आदतें) होती हैं।\n1. Simple Present: आदतों और तथ्यों के लिए। (जैसे, सूर्य पूर्व में उगता है। मैं फुटबॉल खेलता हूँ।)\n2. Present Continuous: इस सटीक क्षण में होने वाले कार्यों के लिए। (जैसे, मैं एक किताब पढ़ रहा हूँ।)\n3. Present Perfect: उन कार्यों के लिए जो अभी समाप्त हुए हैं, लेकिन प्रभाव अभी भी है। (जैसे, मैंने अपना होमवर्क पूरा कर लिया है।)\n4. Present Perfect Continuous: उन कार्यों के लिए जो अतीत में शुरू हुए और अभी भी हो रहे हैं। (जैसे, मैं दो घंटे से पढ़ रहा हूँ।)",
        "body_gu": "વર્તમાન કાળ (Present Tense) આપણને તે વસ્તુઓ વિશે જણાવે છે જે અત્યારે થઈ રહી છે, અથવા જે નિયમિતપણે (આદતો) થાય છે.\n1. Simple Present: આદતો અને તથ્યો માટે. (દા.ત., સૂર્ય પૂર્વમાં ઉગે છે. હું ફૂટબોલ રમું છું.)\n2. Present Continuous: આ ચોક્કસ ક્ષણે થતી ક્રિયાઓ માટે. (દા.ત., હું એક પુસ્તક વાંચી રહ્યો છું.)\n3. Present Perfect: એવી ક્રિયાઓ માટે કે જે હમણાં જ પૂર્ણ થઈ ગઈ છે, પરંતુ અસર હજુ પણ છે. (દા.ત., મેં મારું હોમવર્ક પૂરું કર્યું છે.)\n4. Present Perfect Continuous: એવી ક્રિયાઓ માટે કે જે ભૂતકાળમાં શરૂ થઈ અને હજી પણ થઈ રહી છે. (દા.ત., હું બે કલાકથી અભ્યાસ કરી રહ્યો છું.)"
    },
    {
        "type": "mcq",
        "title": "Knowledge Check: Tenses",
        "title_hi": "ज्ञान परीक्षण: काल",
        "title_gu": "જ્ઞાન ચકાસણી: કાળ",
        "question": "Fill in the blank: She _______ in this school since 2015.",
        "question_hi": "रिक्त स्थान भरें (Fill in the blank): She _______ in this school since 2015.",
        "question_gu": "ખાલી જગ્યા ભરો (Fill in the blank): She _______ in this school since 2015.",
        "options": [
            "is teaching",
            "has been teaching",
            "was teaching",
            "teaches"
        ],
        "options_hi": [
            "is teaching (पढ़ा रही है)",
            "has been teaching (पढ़ाती आ रही है)",
            "was teaching (पढ़ा रही थी)",
            "teaches (पढ़ाती है)"
        ],
        "options_gu": [
            "is teaching (ભણાવી રહી છે)",
            "has been teaching (ભણાવતી આવી રહી છે)",
            "was teaching (ભણાવી રહી હતી)",
            "teaches (ભણાવે છે)"
        ],
        "correct_index": 1,
        "explanation": "We use 'has been teaching' (Present Perfect Continuous) because the action started in the past (2015) and is still continuing now.",
        "explanation_hi": "हम 'has been teaching' (Present Perfect Continuous) का उपयोग करते हैं क्योंकि कार्रवाई अतीत (2015) में शुरू हुई थी और अभी भी जारी है।",
        "explanation_gu": "આપણે 'has been teaching' (Present Perfect Continuous) નો ઉપયોગ કરીએ છીએ કારણ કે ક્રિયા ભૂતકાળમાં (2015) શરૂ થઈ હતી અને અત્યારે પણ ચાલુ છે."
    }
]

# --- Chapter 2: Modals ---
ch2_blocks = [
    {
        "type": "hook",
        "title": "The Power Words",
        "title_hi": "शक्तिशाली शब्द (The Power Words)",
        "title_gu": "શક્તિશાળી શબ્દો (The Power Words)",
        "body": "Think of a student asking a teacher: 'I go to the toilet.' The teacher might say, 'Yes, you go, but you should ask properly!' The correct sentence is 'May I go to the toilet?'. Words like May, Can, Should, and Must are called Modals. They don't just show an action; they show the 'mood' or attitude—like permission, ability, obligation, or possibility.",
        "body_hi": "सोचिए एक छात्र शिक्षक से कह रहा है: 'मैं शौचालय जाता हूँ (I go to the toilet)।' शिक्षक कह सकता है, 'हाँ, तुम जाते हो, लेकिन तुम्हें ठीक से पूछना चाहिए!' सही वाक्य है 'क्या मैं शौचालय जा सकता हूँ? (May I go to the toilet?)'। May, Can, Should, और Must जैसे शब्दों को Modals कहा जाता है। वे केवल एक कार्य नहीं दिखाते; वे 'मनोदशा' (mood) या रवैया दिखाते हैं - जैसे अनुमति (permission), क्षमता (ability), दायित्व (obligation), या संभावना (possibility)।",
        "body_gu": "વિચારો કે એક વિદ્યાર્થી શિક્ષકને પૂછે છે: 'હું શૌચાલય જાઉં છું (I go to the toilet)'. શિક્ષક કહી શકે છે, 'હા, તું જાય છે, પણ તારે યોગ્ય રીતે પૂછવું જોઈએ!' સાચું વાક્ય છે 'શું હું શૌચાલય જઈ શકું? (May I go to the toilet?)'. May, Can, Should અને Must જેવા શબ્દોને Modals કહેવાય છે. તેઓ માત્ર ક્રિયા બતાવતા નથી; તેઓ 'મૂડ' (mood) અથવા વલણ બતાવે છે - જેમ કે પરવાનગી (permission), ક્ષમતા (ability), જવાબદારી (obligation), અથવા શક્યતા (possibility)."
    },
    {
        "type": "theory",
        "title": "Common Modals and Their Uses",
        "title_hi": "सामान्य मोडल (Modals) और उनके उपयोग",
        "title_gu": "સામાન્ય મોડલ (Modals) અને તેના ઉપયોગો",
        "body": "- CAN / COULD: Ability (I can swim) or Request (Can you help me?). Could is the past tense of Can.\n- MAY / MIGHT: Permission (May I come in?) or Possibility (It might rain today).\n- MUST: Strong obligation or necessity (You must wear a helmet).\n- SHOULD / OUGHT TO: Advice or recommendation (You should study hard).",
        "body_hi": "- CAN / COULD: क्षमता (Ability - मैं तैर सकता हूँ) या अनुरोध (Request - क्या आप मेरी मदद कर सकते हैं?)। Could, Can का भूतकाल (past tense) है।\n- MAY / MIGHT: अनुमति (Permission - क्या मैं अंदर आ सकता हूँ?) या संभावना (Possibility - आज बारिश हो सकती है)।\n- MUST: मजबूत दायित्व या आवश्यकता (Obligation - आपको हेलमेट पहनना ही चाहिए)।\n- SHOULD / OUGHT TO: सलाह या सिफारिश (Advice - आपको कड़ी मेहनत करनी चाहिए)।",
        "body_gu": "- CAN / COULD: ક્ષમતા (Ability - હું તરી શકું છું) અથવા વિનંતી (Request - શું તમે મને મદદ કરી શકો છો?). Could એ Can નો ભૂતકાળ (past tense) છે.\n- MAY / MIGHT: પરવાનગી (Permission - શું હું અંદર આવી શકું?) અથવા શક્યતા (Possibility - આજે વરસાદ પડી શકે છે).\n- MUST: મજબૂત જવાબદારી અથવા જરૂરિયાત (Obligation - તમારે હેલ્મેટ પહેરવું જ જોઈએ).\n- SHOULD / OUGHT TO: સલાહ અથવા ભલામણ (Advice - તમારે સખત અભ્યાસ કરવો જોઈએ)."
    },
    {
        "type": "mcq",
        "title": "Knowledge Check: Modals",
        "title_hi": "ज्ञान परीक्षण: Modals",
        "title_gu": "જ્ઞાન ચકાસણી: Modals",
        "question": "Fill in the blank: You _______ respect your elders. (Advice/Moral obligation)",
        "question_hi": "रिक्त स्थान भरें (Fill in the blank): You _______ respect your elders. (सलाह/नैतिक दायित्व)",
        "question_gu": "ખાલી જગ્યા ભરો (Fill in the blank): You _______ respect your elders. (સલાહ/નૈતિક જવાબદારી)",
        "options": [
            "can",
            "might",
            "ought to",
            "would"
        ],
        "options_hi": [
            "can",
            "might",
            "ought to (चाहिए)",
            "would"
        ],
        "options_gu": [
            "can",
            "might",
            "ought to (જોઈએ)",
            "would"
        ],
        "correct_index": 2,
        "explanation": "'Ought to' is used to express moral obligation or strong advice. 'Should' could also be correct, but 'ought to' specifically highlights moral duty.",
        "explanation_hi": "'Ought to' का उपयोग नैतिक दायित्व (moral obligation) या मजबूत सलाह व्यक्त करने के लिए किया जाता है। 'Should' भी सही हो सकता है, लेकिन 'ought to' विशेष रूप से नैतिक कर्तव्य को उजागर करता है।",
        "explanation_gu": "'Ought to' નો ઉપયોગ નૈતિક જવાબદારી (moral obligation) અથવા મજબૂત સલાહ વ્યક્ત કરવા માટે થાય છે. 'Should' પણ સાચું હોઈ શકે છે, પરંતુ 'ought to' ખાસ કરીને નૈતિક ફરજને પ્રકાશિત કરે છે."
    }
]

# --- Chapter 3: Subject-Verb Concord ---
ch3_blocks = [
    {
        "type": "hook",
        "title": "The Balancing Act",
        "title_hi": "संतुलन का कार्य (The Balancing Act)",
        "title_gu": "સંતુલનનું કાર્ય (The Balancing Act)",
        "body": "If one elephant sits on a small seesaw, what happens? It breaks! A seesaw needs balance. Similarly, sentences need balance between the Subject (who is doing the action) and the Verb (the action). If the subject is singular (one person), the verb must also be singular. If the subject is plural (many), the verb must be plural. This balancing act is called Subject-Verb Concord (Agreement).",
        "body_hi": "यदि एक छोटा झूला (seesaw) पर एक हाथी बैठ जाए, तो क्या होगा? वह टूट जाएगा! झूले को संतुलन (balance) की आवश्यकता होती है। इसी तरह, वाक्यों को विषय (Subject - जो कार्य कर रहा है) और क्रिया (Verb - कार्य) के बीच संतुलन की आवश्यकता होती है। यदि विषय एकवचन (singular - एक व्यक्ति) है, तो क्रिया भी एकवचन होनी चाहिए। यदि विषय बहुवचन (plural - कई) है, तो क्रिया बहुवचन होनी चाहिए। इस संतुलन कार्य को Subject-Verb Concord (Agreement) कहा जाता है।",
        "body_gu": "જો એક હાથી નાના ચીંચવા (seesaw) પર બેસે તો શું થાય? તે તૂટી જાય છે! ચીંચવાને સંતુલન (balance) ની જરૂર છે. તેવી જ રીતે, વાક્યોને વિષય (Subject - જે ક્રિયા કરી રહ્યો છે) અને ક્રિયાપદ (Verb - ક્રિયા) વચ્ચે સંતુલનની જરૂર છે. જો વિષય એકવચન (singular - એક વ્યક્તિ) હોય, તો ક્રિયાપદ પણ એકવચન હોવું જોઈએ. જો વિષય બહુવચન (plural - ઘણા) હોય, તો ક્રિયાપદ બહુવચન હોવું જોઈએ. આ સંતુલન કાર્યને Subject-Verb Concord (Agreement) કહેવાય છે."
    },
    {
        "type": "theory",
        "title": "Rule 1: The 'S' Rule",
        "title_hi": "नियम 1: 'S' का नियम (The 'S' Rule)",
        "title_gu": "નિયમ 1: 'S' નો નિયમ (The 'S' Rule)",
        "body": "In Present Tense, if the subject is singular (He, She, It, Rahul), the verb gets an 's' or 'es' at the end.\nExample: He playS cricket. (Singular subject, verb with 'S')\nIf the subject is plural (They, We, Boys), or 'I/You', the verb does NOT get an 's'.\nExample: They play cricket. (Plural subject, verb without 'S').",
        "body_hi": "वर्तमान काल (Present Tense) में, यदि विषय एकवचन (He, She, It, Rahul) है, तो क्रिया के अंत में 's' या 'es' लगता है।\nउदाहरण: He playS cricket. (एकवचन विषय, 'S' के साथ क्रिया)\nयदि विषय बहुवचन (They, We, Boys), या 'I/You' है, तो क्रिया में 's' नहीं लगता है।\nउदाहरण: They play cricket. (बहुवचन विषय, 'S' के बिना क्रिया)।",
        "body_gu": "વર્તમાન કાળ (Present Tense) માં, જો વિષય એકવચન (He, She, It, Rahul) હોય, તો ક્રિયાપદના અંતે 's' અથવા 'es' આવે છે.\nઉદાહરણ: He playS cricket. (એકવચન વિષય, 'S' સાથે ક્રિયાપદ)\nજો વિષય બહુવચન (They, We, Boys), અથવા 'I/You' હોય, તો ક્રિયાપદમાં 's' આવતો નથી.\nઉદાહરણ: They play cricket. (બહુવચન વિષય, 'S' વગર ક્રિયાપદ)."
    },
    {
        "type": "mcq",
        "title": "Knowledge Check: Agreement",
        "title_hi": "ज्ञान परीक्षण: Agreement",
        "title_gu": "જ્ઞાન ચકાસણી: Agreement",
        "question": "Fill in the blank: Each of the students _______ given a certificate.",
        "question_hi": "रिक्त स्थान भरें: Each of the students _______ given a certificate.",
        "question_gu": "ખાલી જગ્યા ભરો: Each of the students _______ given a certificate.",
        "options": [
            "are",
            "were",
            "was",
            "have"
        ],
        "options_hi": [
            "are",
            "were",
            "was",
            "have"
        ],
        "options_gu": [
            "are",
            "were",
            "was",
            "have"
        ],
        "correct_index": 2,
        "explanation": "Even though 'students' is plural, the word 'Each' makes the subject singular (focusing on one student at a time). Therefore, the singular verb 'was' is correct.",
        "explanation_hi": "भले ही 'students' (छात्र) बहुवचन है, शब्द 'Each' (प्रत्येक) विषय को एकवचन बनाता है (एक समय में एक छात्र पर ध्यान केंद्रित करता है)। इसलिए, एकवचन क्रिया 'was' सही है।",
        "explanation_gu": "જોકે 'students' (વિદ્યાર્થીઓ) બહુવચન છે, શબ્દ 'Each' (દરેક) વિષયને એકવચન બનાવે છે (એક સમયે એક વિદ્યાર્થી પર ધ્યાન કેન્દ્રિત કરે છે). તેથી, એકવચન ક્રિયાપદ 'was' સાચું છે."
    }
]

# --- Chapter 4: Reported Speech ---
ch4_blocks = [
    {
        "type": "hook",
        "title": "The Gossip Machine",
        "title_hi": "गपशप मशीन (The Gossip Machine)",
        "title_gu": "ગોસિપ મશીન (The Gossip Machine)",
        "body": "When you tell your friend a secret, like \"I am tired,\" and then your friend tells someone else, they don't say, \"Rahul said, 'I am tired'\" because people will think YOUR FRIEND is tired! Instead, they change the words and say, \"Rahul said that HE WAS tired.\" This act of changing the words to report what someone else said is called Reported Speech (or Indirect Speech).",
        "body_hi": "जब आप अपने दोस्त को एक रहस्य बताते हैं, जैसे \"I am tired\" (मैं थक गया हूँ), और फिर आपका दोस्त किसी और को बताता है, तो वे यह नहीं कहते हैं, \"Rahul said, 'I am tired'\" क्योंकि लोग सोचेंगे कि आपका दोस्त थक गया है! इसके बजाय, वे शब्द बदलते हैं और कहते हैं, \"Rahul said that HE WAS tired (राहुल ने कहा कि वह थका हुआ था)।\" किसी और ने जो कहा उसे रिपोर्ट करने के लिए शब्दों को बदलने के इस कार्य को Reported Speech (या Indirect Speech) कहा जाता है।",
        "body_gu": "જ્યારે તમે તમારા મિત્રને એક રહસ્ય કહો છો, જેમ કે \"I am tired\" (હું થાકી ગયો છું), અને પછી તમારો મિત્ર કોઈ અન્યને કહે છે, ત્યારે તેઓ એવું નથી કહેતા કે, \"Rahul said, 'I am tired'\" કારણ કે લોકો વિચારશે કે તમારો મિત્ર થાકી ગયો છે! તેના બદલે, તેઓ શબ્દો બદલે છે અને કહે છે, \"Rahul said that HE WAS tired (રાહુલે કહ્યું કે તે થાકી ગયો હતો).\" કોઈ અન્ય વ્યક્તિએ જે કહ્યું છે તેની જાણ કરવા માટે શબ્દો બદલવાના આ કાર્યને Reported Speech (અથવા Indirect Speech) કહેવાય છે."
    },
    {
        "type": "theory",
        "title": "The Golden Rule of Reported Speech",
        "title_hi": "Reported Speech का सुनहरा नियम",
        "title_gu": "Reported Speech નો સુવર્ણ નિયમ",
        "body": "When we change Direct Speech to Indirect Speech, we usually take one step back in time (change the tense to the past).\n- Present Simple becomes Past Simple (I play -> he played)\n- Present Continuous becomes Past Continuous (I am playing -> he was playing)\n- Will becomes Would\n- Can becomes Could\nWe also remove the quotation marks (\"\") and usually add the word 'that'.",
        "body_hi": "जब हम Direct Speech को Indirect Speech में बदलते हैं, तो हम आमतौर पर समय में एक कदम पीछे (past) चले जाते हैं।\n- Present Simple, Past Simple बन जाता है (I play -> he played)\n- Present Continuous, Past Continuous बन जाता है (I am playing -> he was playing)\n- Will, Would बन जाता है\n- Can, Could बन जाता है\nहम उद्धरण चिह्न (quotation marks \"\") भी हटा देते हैं और आमतौर पर 'that' शब्द जोड़ते हैं।",
        "body_gu": "જ્યારે આપણે Direct Speech ને Indirect Speech માં બદલીએ છીએ, ત્યારે આપણે સામાન્ય રીતે સમયમાં એક પગલું પાછળ (past) જઈએ છીએ.\n- Present Simple, Past Simple બની જાય છે (I play -> he played)\n- Present Continuous, Past Continuous બની જાય છે (I am playing -> he was playing)\n- Will, Would બની જાય છે\n- Can, Could બની જાય છે\nઆપણે અવતરણ ચિહ્નો (quotation marks \"\") પણ દૂર કરીએ છીએ અને સામાન્ય રીતે 'that' શબ્દ ઉમેરીએ છીએ."
    },
    {
        "type": "mcq",
        "title": "Knowledge Check: Reported Speech",
        "title_hi": "ज्ञान परीक्षण: Reported Speech",
        "title_gu": "જ્ઞાન ચકાસણી: Reported Speech",
        "question": "Change into Indirect Speech: Reena said, \"I will call you tomorrow.\"",
        "question_hi": "Indirect Speech में बदलें: Reena said, \"I will call you tomorrow.\"",
        "question_gu": "Indirect Speech માં બદલો: Reena said, \"I will call you tomorrow.\"",
        "options": [
            "Reena said that she will call me tomorrow.",
            "Reena said that she would call me the next day.",
            "Reena said that I would call her tomorrow.",
            "Reena said that she would call me tomorrow."
        ],
        "options_hi": [
            "Reena said that she will call me tomorrow.",
            "Reena said that she would call me the next day.",
            "Reena said that I would call her tomorrow.",
            "Reena said that she would call me tomorrow."
        ],
        "options_gu": [
            "Reena said that she will call me tomorrow.",
            "Reena said that she would call me the next day.",
            "Reena said that I would call her tomorrow.",
            "Reena said that she would call me tomorrow."
        ],
        "correct_index": 1,
        "explanation": "In indirect speech, 'will' changes to 'would', and words indicating time change too ('tomorrow' becomes 'the next day' or 'the following day').",
        "explanation_hi": "Indirect speech में, 'will' को 'would' में बदल दिया जाता है, और समय को दर्शाने वाले शब्द भी बदल जाते हैं ('tomorrow', 'the next day' या 'the following day' बन जाता है)।",
        "explanation_gu": "Indirect speech માં, 'will' બદલાઈને 'would' થાય છે, અને સમય દર્શાવતા શબ્દો પણ બદલાય છે ('tomorrow' એ 'the next day' અથવા 'the following day' બની જાય છે)."
    }
]

# --- Chapter 5: Determiners ---
ch5_blocks = [
    {
        "type": "hook",
        "title": "Pointing Fingers at Nouns",
        "title_hi": "संज्ञाओं (Nouns) पर उंगली उठाना",
        "title_gu": "નામો (Nouns) પર આંગળી ચીંધવી",
        "body": "Imagine going into a shop and shouting, \"Give me apple!\" The shopkeeper will be confused. Which apple? How many apples? But if you say, \"Give me THAT apple\" or \"Give me AN apple\" or \"Give me SOME apples,\" it is very clear. Words like That, An, Some, Many, and The are called Determiners. They introduce a noun and clarify what exactly you are talking about.",
        "body_hi": "कल्पना कीजिए कि आप एक दुकान में जाते हैं और चिल्लाते हैं, \"Give me apple! (मुझे सेब दो!)\" दुकानदार भ्रमित (confused) हो जाएगा। कौन सा सेब? कितने सेब? लेकिन अगर आप कहते हैं, \"मुझे वह (THAT) सेब दो\" या \"मुझे एक (AN) सेब दो\" या \"मुझे कुछ (SOME) सेब दो,\" तो यह बिल्कुल स्पष्ट है। That, An, Some, Many और The जैसे शब्दों को Determiners कहा जाता है। वे एक संज्ञा (noun) का परिचय देते हैं और स्पष्ट करते हैं कि आप वास्तव में किस बारे में बात कर रहे हैं।",
        "body_gu": "કલ્પના કરો કે દુકાનમાં જઈને બૂમો પાડો, \"Give me apple! (મને સફરજન આપો!)\" દુકાનદાર મૂંઝવણમાં (confused) આવશે. કયું સફરજન? કેટલા સફરજન? પરંતુ જો તમે કહો છો, \"મને તે (THAT) સફરજન આપો\" અથવા \"મને એક (AN) સફરજન આપો\" અથવા \"મને થોડા (SOME) સફરજન આપો,\" તો તે ખૂબ જ સ્પષ્ટ છે. That, An, Some, Many અને The જેવા શબ્દોને Determiners કહેવાય છે. તેઓ સંજ્ઞા (noun) નો પરિચય આપે છે અને સ્પષ્ટ કરે છે કે તમે ખરેખર શેના વિશે વાત કરી રહ્યાં છો."
    },
    {
        "type": "theory",
        "title": "Types of Determiners",
        "title_hi": "Determiners के प्रकार",
        "title_gu": "Determiners ના પ્રકાર",
        "body": "1. Articles: A, An, The (e.g., The boy is here).\n2. Demonstratives: This, That, These, Those (pointing at things).\n3. Possessives: My, Your, His, Her (showing ownership).\n4. Quantifiers: Some, Any, Many, Much, Few (showing quantity without giving an exact number).",
        "body_hi": "1. Articles (उपपद): A, An, The (जैसे, The boy is here - लड़का यहाँ है)।\n2. Demonstratives (संकेतवाचक): This, That, These, Those (चीजों की ओर इशारा करना)।\n3. Possessives (अधिकारवाचक): My, Your, His, Her (स्वामित्व दिखाना)।\n4. Quantifiers (परिमाणवाचक): Some, Any, Many, Much, Few (सटीक संख्या दिए बिना मात्रा दिखाना)।",
        "body_gu": "1. Articles (ઉપપદ): A, An, The (દા.ત., The boy is here - છોકરો અહીં છે).\n2. Demonstratives (સંકેતવાચક): This, That, These, Those (વસ્તુઓ તરફ ઈશારો કરવો).\n3. Possessives (અધિકારવાચક): My, Your, His, Her (માલિકી દર્શાવે છે).\n4. Quantifiers (પરિમાણવાચક): Some, Any, Many, Much, Few (ચોક્કસ સંખ્યા આપ્યા વિના જથ્થો દર્શાવે છે)."
    },
    {
        "type": "mcq",
        "title": "Knowledge Check: Quantifiers",
        "title_hi": "ज्ञान परीक्षण: Quantifiers",
        "title_gu": "જ્ઞાન ચકાસણી: Quantifiers",
        "question": "Fill in the blank: There is not _______ milk left in the fridge.",
        "question_hi": "रिक्त स्थान भरें (Fill in the blank): There is not _______ milk left in the fridge.",
        "question_gu": "ખાલી જગ્યા ભરો (Fill in the blank): There is not _______ milk left in the fridge.",
        "options": [
            "many",
            "much",
            "some",
            "few"
        ],
        "options_hi": [
            "many (कई)",
            "much (बहुत/ज्यादा)",
            "some (कुछ)",
            "few (थोड़े)"
        ],
        "options_gu": [
            "many (ઘણા)",
            "much (ઘણું/વધુ)",
            "some (થોડા)",
            "few (થોડા)"
        ],
        "correct_index": 1,
        "explanation": "'Milk' is an uncountable noun. We use 'much' with uncountable nouns (like water, sugar, milk) in negative sentences. 'Many' is used for countable nouns (like apples, cars).",
        "explanation_hi": "'Milk' (दूध) एक अगणनीय संज्ञा (uncountable noun) है। हम नकारात्मक वाक्यों में अगणनीय संज्ञाओं (जैसे पानी, चीनी, दूध) के साथ 'much' का उपयोग करते हैं। 'Many' का प्रयोग गणनीय संज्ञाओं (countable nouns - जैसे सेब, कारें) के लिए किया जाता है।",
        "explanation_gu": "'Milk' (દૂધ) એ ગણી ન શકાય તેવી સંજ્ઞા (uncountable noun) છે. આપણે નકારાત્મક વાક્યોમાં ન ગણી શકાય તેવી સંજ્ઞાઓ (જેમ કે પાણી, ખાંડ, દૂધ) સાથે 'much' નો ઉપયોગ કરીએ છીએ. 'Many' નો ઉપયોગ ગણી શકાય તેવી સંજ્ઞાઓ (countable nouns - જેમ કે સફરજન, કાર) માટે થાય છે."
    }
]

if __name__ == "__main__":
    create_grammar_chapter(1, "Tenses", "काल (Tenses)", "કાળ (Tenses)", ch1_blocks)
    create_grammar_chapter(2, "Modals", "मोडल (Modals)", "મોડલ (Modals)", ch2_blocks)
    create_grammar_chapter(3, "Subject-Verb Concord", "विषय-क्रिया समझौता (Subject-Verb Concord)", "વિષય-ક્રિયા સમજૂતી (Subject-Verb Concord)", ch3_blocks)
    create_grammar_chapter(4, "Reported Speech", "अप्रत्यक्ष कथन (Reported Speech)", "અપ્રત્યક્ષ કથન (Reported Speech)", ch4_blocks)
    create_grammar_chapter(5, "Determiners", "निर्धारक (Determiners)", "નિર્ધારકો (Determiners)", ch5_blocks)
