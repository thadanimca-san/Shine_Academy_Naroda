import os
import json
import glob

# ============================================================
# ENGLISH GRAMMAR BUILDER — CLASS 9 & CLASS 10
# Complete, Trilingual, Board-Exam-Ready, 8-Step Pedagogy
# ============================================================

CLASS9_GRAMMAR = [
    {
        "num": 1,
        "topic": "Tenses",
        "topic_hi": "काल (Tenses)",
        "topic_gu": "કાળ (Tenses)",
        "hook": "Imagine texting your friend: 'I am eating pizza yesterday.' Your friend would be very confused! The tense you choose tells your reader WHEN the action happened — past, present, or future.",
        "hook_hi": "कल्पना करें कि आप अपने दोस्त को टेक्स्ट करते हैं: 'मैं कल पिज्जा खा रहा हूं।' आपका दोस्त बहुत भ्रमित होगा! आप जो काल चुनते हैं वह आपके पाठक को बताता है कि क्रिया कब हुई — भूत, वर्तमान या भविष्य।",
        "hook_gu": "કલ્પના કરો તમે મિત્રને ટેક્સ્ટ કરો: 'હું ગઈ કાલ પિઝ્ઝા ખાઈ રહ્યો છું.' — આ ખોટું છે! કાળ (Tense) ક્રિયા ક્યારે ઘટી તે બતાવે.",
        "theory_blocks": [
            {
                "title": "The 12 Tenses at a Glance",
                "title_hi": "एक नज़र में 12 काल",
                "title_gu": "12 કાળ — એક નજરમાં",
                "body": "English has 3 time frames × 4 aspects = 12 tenses.\n\nPRESENT: Simple (I eat), Continuous (I am eating), Perfect (I have eaten), Perfect Continuous (I have been eating)\n\nPAST: Simple (I ate), Continuous (I was eating), Perfect (I had eaten), Perfect Continuous (I had been eating)\n\nFUTURE: Simple (I will eat), Continuous (I will be eating), Perfect (I will have eaten), Perfect Continuous (I will have been eating)",
                "body_hi": "अंग्रेजी में 3 समय × 4 पहलू = 12 काल हैं।\n\nवर्तमान: सरल (मैं खाता हूं), सतत (मैं खा रहा हूं), परफेक्ट (मैंने खाया है), परफेक्ट सतत (मैं खाता रहा हूं)\n\nभूत: सरल (मैंने खाया), सतत (मैं खा रहा था), परफेक्ट (मैंने खाया था), परफेक्ट सतत (मैं खाता रहा था)\n\nभविष्य: सरल (मैं खाऊंगा), सतत (मैं खा रहा होऊंगा), परफेक्ट (मैंने खाया होगा), परफेक्ट सतत (मैं खाता रहा होऊंगा)",
                "body_gu": "અંગ્રેજીમાં 3 સમય × 4 પ્રકાર = 12 કાળ.\n\nવર્તમાન: સ. (I eat), સ.ચ. (I am eating), પ. (I have eaten), પ.ચ. (I have been eating)\n\nભૂત: સ. (I ate), સ.ચ. (I was eating), પ. (I had eaten), પ.ચ. (I had been eating)\n\nભવિષ્ય: સ. (I will eat), સ.ચ. (I will be eating), પ. (I will have eaten), પ.ચ. (I will have been eating)",
            },
            {
                "title": "Time Expressions — Signal Words for Each Tense",
                "title_hi": "समय के संकेत शब्द — प्रत्येक काल के लिए",
                "title_gu": "સ. શ. — દ. ક. .",
                "body": "Simple Present: always, usually, often, never, every day\nPresent Continuous: now, at this moment, currently, look!\nPresent Perfect: already, yet, just, ever, never, recently\nSimple Past: yesterday, ago, last week, in 2010, when\nPast Perfect: before, after, by the time, already (in past)\nSimple Future: tomorrow, next week, soon, in future",
                "body_hi": "सरल वर्तमान: हमेशा, आमतौर पर, अक्सर, कभी नहीं, हर दिन\nवर्तमान सतत: अभी, इस समय, वर्तमान में\nप्रेजेंट परफेक्ट: पहले से, अभी तक, अभी-अभी, कभी, हाल ही में\nसरल भूत: कल, पहले, पिछले सप्ताह, 2010 में, जब\nभूत परफेक्ट: पहले, बाद में, उस समय तक\nसरल भविष्य: कल, अगले सप्ताह, जल्द, भविष्य में",
                "body_gu": "સ.વ.: always, usually, every day\nવ.ચ.: now, at this moment\nપ.વ.: already, just, yet, recently\nભ.સ.: yesterday, ago, last week\nભ.ભ.: before, after, by the time\nભ.ભ.: tomorrow, next week, soon",
            }
        ],
        "examples": [
            {
                "problem": "Identify the tense: 'She had been waiting for two hours when the bus finally arrived.'",
                "problem_hi": "काल पहचानें: 'वह दो घंटे से इंतजार कर रही थी जब बस आखिरकार पहुंची।'",
                "problem_gu": "ક. .: 'She had been waiting for two hours when the bus finally arrived.'",
                "solution": "PAST PERFECT CONTINUOUS. Signal: 'had been + V-ing'. It shows an action that was ongoing in the past BEFORE another past event (bus arriving).",
                "solution_hi": "भूतकाल परफेक्ट सतत। संकेत: 'had been + V-ing'। यह एक ऐसी क्रिया दिखाता है जो भूतकाल में एक अन्य भूतकाल की घटना से पहले चल रही थी।",
                "solution_gu": "PAST PERFECT CONTINUOUS. Signal: 'had been + V-ing'. .",
            },
            {
                "problem": "Fill in: 'By next year, she _____ (complete) her degree.'",
                "problem_hi": "भरें: 'अगले साल तक, वह अपनी डिग्री _____ (पूरी करना)।'",
                "problem_gu": "ભ.: 'By next year, she _____ (complete) her degree.'",
                "solution": "will have completed. Rule: 'By + future time' → Future Perfect Tense (will have + V3) showing an action that will be completed before a future point.",
                "solution_hi": "will have completed। नियम: 'By + भविष्य का समय' → भविष्य परफेक्ट काल (will have + V3)",
                "solution_gu": "will have completed. Rule: 'By + future time' = Future Perfect.",
            },
            {
                "problem": "Correct the error: 'I am knowing the answer.'",
                "problem_hi": "त्रुटि सुधारें: 'I am knowing the answer.'",
                "problem_gu": "ભ. : 'I am knowing the answer.'",
                "solution": "'I know the answer.' — Stative verbs (know, believe, understand, love, hate, have, want) do NOT use continuous form. Always use Simple Present with them.",
                "solution_hi": "'I know the answer.' — स्थिर क्रियाएं (know, believe, understand, love, hate) सतत रूप का उपयोग नहीं करतीं।",
                "solution_gu": "'I know the answer.' — Stative verbs continuous form .",
            }
        ],
        "mcqs": [
            {
                "question": "Choose the correct tense: 'She _____ in Mumbai for ten years now.'",
                "question_hi": "सही काल चुनें: 'वह अब दस साल से मुंबई में _____ है।'",
                "question_gu": "ય. .: 'She _____ in Mumbai for ten years now.'",
                "options": ["is living", "has been living", "lived", "had been living"],
                "options_hi": ["is living", "has been living", "lived", "had been living"],
                "options_gu": ["is living", "has been living", "lived", "had been living"],
                "correct_index": 1,
                "explanation": "'has been living' = Present Perfect Continuous. Signal word 'for ten years' + 'now' tells us the action started in the past and is STILL continuing right now.",
                "explanation_hi": "'has been living' = प्रेजेंट परफेक्ट कंटीन्यूअस। संकेत शब्द 'for ten years' + 'now' बताता है कि क्रिया अभी भी जारी है।",
                "explanation_gu": "'has been living' = Present Perfect Continuous. Signal: 'for ten years' + 'now'.",
            },
            {
                "question": "Which sentence is grammatically CORRECT?",
                "question_hi": "कौन सा वाक्य व्याकरणिक रूप से सही है?",
                "question_gu": "ક. .",
                "options": [
                    "I am understanding the lesson.",
                    "I understand the lesson.",
                    "I was understand the lesson.",
                    "I have been understand the lesson."
                ],
                "options_hi": [
                    "I am understanding the lesson.",
                    "I understand the lesson.",
                    "I was understand the lesson.",
                    "I have been understand the lesson."
                ],
                "options_gu": [
                    "I am understanding the lesson.",
                    "I understand the lesson.",
                    "I was understand the lesson.",
                    "I have been understand the lesson."
                ],
                "correct_index": 1,
                "explanation": "'understand' is a stative verb. Stative verbs express a state or condition (not an action), so they do NOT use -ing forms: know, understand, believe, love, hate, want, have (possession).",
                "explanation_hi": "'understand' एक स्थिर क्रिया है। स्थिर क्रियाएं अवस्था व्यक्त करती हैं, इसलिए वे -ing रूपों का उपयोग नहीं करतीं।",
                "explanation_gu": "'understand' stative verb — -ing form .",
            },
            {
                "question": "Board Exam Pattern — Fill in the blank with correct form:\n'By the time we reached the station, the train _____ (already/leave).'",
                "question_hi": "बोर्ड परीक्षा पैटर्न — सही रूप से भरें:\n'By the time we reached the station, the train _____ (already/leave).'",
                "question_gu": "Board Pattern — .: 'By the time we reached..., the train _____ (already/leave).'",
                "options": ["already left", "had already left", "has already left", "was already leaving"],
                "options_hi": ["already left", "had already left", "has already left", "was already leaving"],
                "options_gu": ["already left", "had already left", "has already left", "was already leaving"],
                "correct_index": 1,
                "explanation": "'had already left' = Past Perfect. Rule: When TWO past actions occur, the EARLIER action uses Past Perfect (had + V3) and the LATER action uses Simple Past. Train leaving happened BEFORE we reached.",
                "explanation_hi": "'had already left' = भूत परफेक्ट। नियम: जब दो भूतकाल की क्रियाएं हों, तो पहले होने वाली क्रिया Past Perfect में होती है।",
                "explanation_gu": "'had already left' = Past Perfect. Rule: 2 past actions — earlier = Past Perfect.",
            },
            {
                "question": "Identify the tense of the underlined verb:\n'The children have been playing in the park for three hours.'",
                "question_hi": "रेखांकित क्रिया का काल पहचानें:\n'बच्चे तीन घंटे से पार्क में खेल रहे हैं।'",
                "question_gu": "ઓ.ક. .",
                "options": ["Simple Present", "Present Continuous", "Present Perfect", "Present Perfect Continuous"],
                "options_hi": ["सरल वर्तमान", "वर्तमान सतत", "प्रेजेंट परफेक्ट", "प्रेजेंट परफेक्ट सतत"],
                "options_gu": ["Simple Present", "Present Continuous", "Present Perfect", "Present Perfect Continuous"],
                "correct_index": 3,
                "explanation": "Present Perfect Continuous: 'have/has + been + V-ing'. Signal: 'for three hours' shows duration from past to now. The action STARTED in the past and IS STILL happening.",
                "explanation_hi": "प्रेजेंट परफेक्ट सतत: 'have/has + been + V-ing'। संकेत: 'for three hours' भूतकाल से अब तक की अवधि दिखाता है।",
                "explanation_gu": "Present Perfect Continuous: 'have been + V-ing'. Signal: 'for three hours'.",
            },
            {
                "question": "Board Exam — Editing Exercise:\nSpot the error and correct it:\n'She don't know the answer to the question.'",
                "question_hi": "बोर्ड परीक्षा — संपादन:\nत्रुटि खोजें और सुधारें: 'She don't know the answer.'",
                "question_gu": "Board Editing: 'She don't know...' — .",
                "options": [
                    "She didn't know the answer.",
                    "She doesn't know the answer.",
                    "She do not know the answer.",
                    "She is not knowing the answer."
                ],
                "options_hi": [
                    "She didn't know the answer.",
                    "She doesn't know the answer.",
                    "She do not know the answer.",
                    "She is not knowing the answer."
                ],
                "options_gu": [
                    "She didn't know the answer.",
                    "She doesn't know the answer.",
                    "She do not know the answer.",
                    "She is not knowing the answer."
                ],
                "correct_index": 1,
                "explanation": "'She doesn't know.' Error: With 3rd person singular (she/he/it), use 'doesn't' NOT 'don't'. Rule: He/She/It + doesn't + V1 (base form).",
                "explanation_hi": "'She doesn't know.' त्रुटि: 3rd person singular (she/he/it) के साथ 'doesn't' उपयोग करें।",
                "explanation_gu": "'She doesn't know.' Error: 3rd person singular = doesn't.",
            }
        ]
    },
    {
        "num": 2,
        "topic": "Modals",
        "topic_hi": "सहायक क्रियाएं (Modals)",
        "topic_gu": "Modals (સ. ક્.)",
        "hook": "You walk up to your teacher and say: 'I must borrow your pen' — or do you say 'may I borrow your pen'? The word you choose completely changes whether you sound polite, rude, certain, or doubtful. Modals are magic words that add MEANING to your sentences!",
        "hook_hi": "आप अपने शिक्षक के पास जाते हैं और कहते हैं: 'मुझे आपकी कलम लेनी चाहिए' — या 'क्या मैं आपकी कलम ले सकता हूं'? जो शब्द आप चुनते हैं वह पूरी तरह से बदल देता है कि आप विनम्र, असभ्य, निश्चित या संदेहास्पद लगते हैं।",
        "hook_gu": "Modals = magic words that add meaning — permission, ability, obligation, possibility.",
        "theory_blocks": [
            {
                "title": "The 9 Key Modals and Their Meanings",
                "title_hi": "9 मुख्य सहायक क्रियाएं और उनके अर्थ",
                "title_gu": "9 Modals અ. .",
                "body": "CAN: Ability (I can swim) / Informal permission (Can I go?)\nCOULD: Past ability (I could run fast) / Polite request (Could you help me?)\nMAY: Formal permission (May I come in?) / Possibility (It may rain)\nMIGHT: Less certain possibility (It might rain)\nMUST: Strong obligation/necessity (You must wear a seatbelt) / Certainty (She must be tired)\nSHALL: Future (Shall we dance?) / Strong intention\nSHOULD: Advice / Expectation (You should study)\nWILL: Future / Determination\nWOULD: Polite request (Would you help me?) / Conditional / Past habit",
                "body_hi": "CAN: क्षमता / अनौपचारिक अनुमति\nCOULD: भूत क्षमता / विनम्र अनुरोध\nMAY: औपचारिक अनुमति / संभावना\nMIGHT: कम निश्चित संभावना\nMUST: मजबूत दायित्व / निश्चितता\nSHALL: भविष्य / प्रस्ताव\nSHOULD: सलाह / अपेक्षा\nWILL: भविष्य / इरादा\nWOULD: विनम्र अनुरोध / भूत आदत",
                "body_gu": "CAN: ક્ષ. / Inf. permit\nCOULD: ભ. ક્ষ. / Polite req.\nMAY: Form. perm. / Poss.\nMIGHT: Less poss.\nMUST: Oblig. / Certainty\nSHALL: Future / Offer\nSHOULD: Advice / Expect\nWILL: Future\nWOULD: Polite req. / Past habit",
            }
        ],
        "examples": [
            {
                "problem": "Choose: 'You _____ (must/should) not smoke here. It is strictly prohibited.'",
                "problem_hi": "चुनें: 'आप यहां धूम्रपान _____ नहीं (must/should) करते। यह सख्त रूप से प्रतिबंधित है।'",
                "problem_gu": "ચ.: 'must/should not smoke here.'",
                "solution": "MUST NOT. Rule: MUST NOT = strong prohibition (not allowed). SHOULD NOT = advice (not recommended). Since smoking is 'strictly prohibited' → must not.",
                "solution_hi": "MUST NOT। नियम: MUST NOT = मजबूत निषेध (अनुमति नहीं)। SHOULD NOT = सलाह।",
                "solution_gu": "MUST NOT = strong prohibition. SHOULD NOT = advice.",
            },
            {
                "problem": "He _____ (can/could) play cricket very well when he was young.",
                "problem_hi": "वह जब युवा था तब क्रिकेट बहुत अच्छा _____ (can/could) खेलता था।",
                "problem_gu": "He _____ (can/could) play when young.",
                "solution": "COULD. Rule: CAN = present ability. COULD = past ability. 'when he was young' = past → COULD.",
                "solution_hi": "COULD। नियम: CAN = वर्तमान क्षमता। COULD = भूत क्षमता।",
                "solution_gu": "COULD = past ability.",
            },
            {
                "problem": "_____ (May/Can) I use your phone, please? (Formal request)",
                "problem_hi": "क्या मैं आपका फोन उपयोग कर _____ (May/Can) हूं? (औपचारिक अनुरोध)",
                "problem_gu": "_____ (May/Can) I use phone? (Formal)",
                "solution": "MAY. Rule: MAY = formal/polite permission. CAN = informal permission. In formal contexts (e.g., school exam, with elders) → use MAY.",
                "solution_hi": "MAY। नियम: MAY = औपचारिक/विनम्र अनुमति। CAN = अनौपचारिक।",
                "solution_gu": "MAY = formal permission.",
            }
        ],
        "mcqs": [
            {
                "question": "'You _____ respect your elders.' (Expressing moral obligation/advice)",
                "question_hi": "'आप अपने बड़ों का सम्मान _____ करें।' (नैतिक दायित्व)",
                "question_gu": "Moral obligation: 'You _____ respect elders.'",
                "options": ["can", "might", "should", "would"],
                "options_hi": ["can", "might", "should", "would"],
                "options_gu": ["can", "might", "should", "would"],
                "correct_index": 2,
                "explanation": "SHOULD = moral obligation, advice, or recommendation. CAN = ability. MIGHT = less certain possibility. WOULD = polite request/conditional.",
                "explanation_hi": "SHOULD = नैतिक दायित्व, सलाह।",
                "explanation_gu": "SHOULD = advice, moral obligation.",
            },
            {
                "question": "'She _____ be at home — all the lights are off.' (Logical deduction)",
                "question_hi": "'वह घर पर _____ नहीं है — सभी रोशनी बंद है।' (तार्किक निष्कर्ष)",
                "question_gu": "Logical deduction: 'She _____ be at home, lights off.'",
                "options": ["can't", "shouldn't", "wouldn't", "mightn't"],
                "options_hi": ["can't", "shouldn't", "wouldn't", "mightn't"],
                "options_gu": ["can't", "shouldn't", "wouldn't", "mightn't"],
                "correct_index": 0,
                "explanation": "CAN'T = logical impossibility/deduction. When you are almost certain something is NOT true based on evidence → use can't. 'Lights are off' = strong evidence she's not home.",
                "explanation_hi": "CAN'T = तार्किक असंभावना। जब आप लगभग निश्चित हों कि कुछ सच नहीं है → can't।",
                "explanation_gu": "CAN'T = logical impossibility/deduction.",
            },
            {
                "question": "Board Exam: Fill in — 'When I was a child, I _____ climb trees very fast.'",
                "question_hi": "Board: 'जब मैं बच्चा था, मैं पेड़ों पर बहुत तेज _____ चढ़ता था।'",
                "question_gu": "Board Fill: 'When child, I _____ climb trees fast.'",
                "options": ["can", "could", "may", "will"],
                "options_hi": ["can", "could", "may", "will"],
                "options_gu": ["can", "could", "may", "will"],
                "correct_index": 1,
                "explanation": "COULD = past ability. 'When I was a child' clearly sets the time in the PAST, so use COULD (not CAN which is present).",
                "explanation_hi": "COULD = भूत क्षमता। 'जब मैं बच्चा था' = भूतकाल।",
                "explanation_gu": "COULD = past ability. 'When child' = past.",
            },
            {
                "question": "'_____ you please pass me the salt?' (Very polite request)",
                "question_hi": "'क्या आप _____ नमक पास कर सकते हैं?' (बहुत विनम्र अनुरोध)",
                "question_gu": "Very polite: '_____ you please pass salt?'",
                "options": ["Can", "May", "Could", "Shall"],
                "options_hi": ["Can", "May", "Could", "Shall"],
                "options_gu": ["Can", "May", "Could", "Shall"],
                "correct_index": 2,
                "explanation": "COULD = very polite request. While CAN is also used for requests, COULD is more polite and formal. In formal writing and board exams, COULD is preferred for polite requests.",
                "explanation_hi": "COULD = बहुत विनम्र अनुरोध। COULD, CAN से अधिक विनम्र है।",
                "explanation_gu": "COULD = most polite request.",
            },
            {
                "question": "Board Editing: 'The doctor said I should to take rest.' Find the error.",
                "question_hi": "बोर्ड संपादन: 'डॉक्टर ने कहा मुझे आराम करना चाहिए।' त्रुटि खोजें।",
                "question_gu": "Board Editing: 'should to take rest' — error?",
                "options": ["should → must", "Remove 'to' after should", "take → took", "No error"],
                "options_hi": ["should → must", "'to' हटाएं", "take → took", "कोई त्रुटि नहीं"],
                "options_gu": ["should → must", "'to' remove karo", "take → took", "No error"],
                "correct_index": 1,
                "explanation": "Modals (can, could, may, might, must, shall, should, will, would) are ALWAYS followed by V1 (base form) WITHOUT 'to'. Never say 'should to go' → say 'should go'.",
                "explanation_hi": "Modals हमेशा V1 (base form) के बाद आते हैं, 'to' के बिना।",
                "explanation_gu": "Modals + V1 (no 'to'). 'should to go' WRONG → 'should go' CORRECT.",
            }
        ]
    },
    {
        "num": 3,
        "topic": "Subject-Verb Agreement",
        "topic_hi": "कर्ता-क्रिया अनुरूपता",
        "topic_gu": "Subject-Verb Agreement",
        "hook": "Read this: 'My group of friends are coming.' vs 'My group of friends is coming.' Which is correct? Most students get this wrong! Today we master the golden rules that make your English instantly correct.",
        "hook_hi": "पढ़ें: 'My group of friends are coming.' बनाम 'My group of friends is coming.' कौन सा सही है? Subject-Verb Agreement का अर्थ है कि Subject और Verb हमेशा मेल खाना चाहिए।",
        "hook_gu": "'My group of friends is/are coming?' — S-V Agreement = Subject-Verb must match.",
        "theory_blocks": [
            {
                "title": "The 10 Golden Rules of Subject-Verb Agreement",
                "title_hi": "Subject-Verb Agreement के 10 सुनहरे नियम",
                "title_gu": "S-V Agreement — 10 Golden Rules",
                "body": "1. Singular subject → singular verb: He runs.\n2. Plural subject → plural verb: They run.\n3. 'Each/Every/Either/Neither' + singular verb: Each child is happy.\n4. Collective nouns → singular verb: The team wins.\n5. 'One of the + plural' → singular verb: One of the boys was absent.\n6. 'A number of' → plural: A number of students are present.\n7. 'The number of' → singular: The number of students is increasing.\n8. Indefinite pronouns (everyone, nobody) → singular: Everyone is invited.\n9. Two subjects joined by 'and' → plural: Ram and Shyam are brothers.\n10. 'Either/Neither + or/nor' → verb agrees with NEARER subject.",
                "body_hi": "1. एकवचन Subject → एकवचन Verb\n2. बहुवचन Subject → बहुवचन Verb\n3. Each/Every/Either/Neither → एकवचन\n4. Collective nouns → एकवचन\n5. One of the + plural → एकवचन\n6. A number of → बहुवचन\n7. The number of → एकवचन\n8. Everyone/Nobody → एकवचन\n9. And से जुड़े दो Subject → बहुवचन\n10. Either...or/Neither...nor → निकटतम Subject से मेल",
                "body_gu": "10 Rules:\n1. Singular→Singular. 2. Plural→Plural. 3. Each/Every→Singular. 4. Collective→Singular. 5. One of the→Singular. 6. A number of→Plural. 7. The number of→Singular. 8. Everyone→Singular. 9. A and B→Plural. 10. Either/Nor→Nearer Subject.",
            }
        ],
        "examples": [
            {
                "problem": "The news _____ (is/are) shocking.",
                "problem_hi": "The news _____ (is/are) चौंकाने वाली है।",
                "problem_gu": "The news _____ (is/are) shocking.",
                "solution": "IS. Rule: Some nouns look plural but are treated as SINGULAR: news, mathematics, physics, politics, economics, athletics, measles, mumps. → 'The news is shocking.'",
                "solution_hi": "IS। नियम: कुछ संज्ञाएं बहुवचन दिखती हैं लेकिन एकवचन मानी जाती हैं: news, mathematics, physics।",
                "solution_gu": "IS. Special nouns: news, maths, physics → always singular.",
            },
            {
                "problem": "Either the teacher or the students _____ (is/are) responsible.",
                "problem_hi": "या तो शिक्षक या छात्र जिम्मेदार _____ (is/are)।",
                "problem_gu": "Either teacher or students _____ (is/are) responsible.",
                "solution": "ARE. Rule: Either...or / Neither...nor → verb agrees with the NEARER subject. 'students' is nearer → plural → ARE.",
                "solution_hi": "ARE। नियम: Either...or में क्रिया निकटतम Subject से मेल खाती है। 'students' निकट है → बहुवचन → ARE।",
                "solution_gu": "ARE. Either/or → nearer subject = 'students' = plural.",
            },
            {
                "problem": "A number of students _____ (has/have) passed.",
                "problem_hi": "बहुत से छात्र पास _____ (has/have) हुए हैं।",
                "problem_gu": "'A number of students' _____ (has/have) passed.",
                "solution": "HAVE. Rule: 'A NUMBER OF' = many → PLURAL verb. 'THE NUMBER OF' = a count → SINGULAR verb. Example: 'The number of students IS increasing.'",
                "solution_hi": "HAVE। नियम: 'A number of' = बहुत → बहुवचन। 'The number of' = संख्या → एकवचन।",
                "solution_gu": "'A number of' = plural. 'The number of' = singular.",
            }
        ],
        "mcqs": [
            {
                "question": "_____ of the boys (has/have) completed the homework.",
                "question_hi": "लड़कों में से किसी ने _____ गृहकार्य पूरा किया है।",
                "question_gu": "Neither of boys _____ (has/have) done homework.",
                "options": ["Neither ... have", "Neither ... has", "None ... has", "Each ... have"],
                "options_hi": ["Neither ... have", "Neither ... has", "None ... has", "Each ... have"],
                "options_gu": ["Neither ... have", "Neither ... has", "None ... has", "Each ... have"],
                "correct_index": 1,
                "explanation": "'Neither' refers to exactly two people/things and ALWAYS takes a SINGULAR verb. → 'Neither of the boys HAS completed the homework.'",
                "explanation_hi": "'Neither' दो में से किसी को संदर्भित करता है और हमेशा एकवचन क्रिया लेता है।",
                "explanation_gu": "'Neither' + singular verb = HAS.",
            },
            {
                "question": "The committee _____ divided on this issue.",
                "question_hi": "समिति इस मुद्दे पर विभाजित _____।",
                "question_gu": "Committee _____ divided on this issue.",
                "options": ["are", "is", "were", "have been"],
                "options_hi": ["are", "is", "were", "have been"],
                "options_gu": ["are", "is", "were", "have been"],
                "correct_index": 1,
                "explanation": "Collective nouns (committee, team, jury, family, government, audience) take SINGULAR verb when acting as ONE unit. 'The committee IS divided' (acting as one body).",
                "explanation_hi": "Collective nouns (committee, team, jury) एकवचन क्रिया लेते हैं जब एक इकाई के रूप में कार्य करते हैं।",
                "explanation_gu": "Collective noun = singular verb = IS.",
            },
            {
                "question": "Board Exam — Editing: 'Mathematics are my favourite subject.' Correct the error.",
                "question_hi": "Board Editing: 'Mathematics are my favourite subject.' — सुधारें।",
                "question_gu": "Board Edit: 'Mathematics are my favourite subject.'",
                "options": [
                    "Mathematics am my favourite subject.",
                    "Mathematics is my favourite subject.",
                    "Mathematics were my favourite subject.",
                    "No correction needed."
                ],
                "options_hi": [
                    "Mathematics am my favourite subject.",
                    "Mathematics is my favourite subject.",
                    "Mathematics were my favourite subject.",
                    "कोई सुधार नहीं।"
                ],
                "options_gu": [
                    "Mathematics am...", "Mathematics is...", "Mathematics were...", "No correction."
                ],
                "correct_index": 1,
                "explanation": "Mathematics (like news, physics, economics, politics) ends in 's' but is a SINGULAR subject, so it takes singular verb IS. → 'Mathematics IS my favourite subject.'",
                "explanation_hi": "Mathematics एकवचन विषय है, इसलिए IS → 'Mathematics IS my favourite subject.'",
                "explanation_gu": "Mathematics = singular → IS.",
            },
            {
                "question": "Each of the players _____ given a trophy.",
                "question_hi": "प्रत्येक खिलाड़ी को एक ट्रॉफी _____ दी गई।",
                "question_gu": "Each of the players _____ given trophy.",
                "options": ["were", "are", "was", "have been"],
                "options_hi": ["were", "are", "was", "have been"],
                "options_gu": ["were", "are", "was", "have been"],
                "correct_index": 2,
                "explanation": "'Each' always takes a SINGULAR verb. 'Each of the players WAS given a trophy.' Remember: Each, Every, Either, Neither → always singular.",
                "explanation_hi": "'Each' हमेशा एकवचन क्रिया लेता है। 'Each of the players WAS given a trophy.'",
                "explanation_gu": "'Each' = singular = WAS.",
            },
            {
                "question": "Board Exam: 'A large number of birds _____ migrated to warmer climates.'",
                "question_hi": "Board: 'बड़ी संख्या में पक्षी गर्म जलवायु की ओर _____ प्रवास कर गए हैं।'",
                "question_gu": "Board: 'A large number of birds _____ migrated.'",
                "options": ["has", "have", "is", "was"],
                "options_hi": ["has", "have", "is", "was"],
                "options_gu": ["has", "have", "is", "was"],
                "correct_index": 1,
                "explanation": "'A large number of' = MANY → PLURAL verb HAVE. vs 'The number of birds IS increasing' (singular). KEY TRICK: A number of = many birds (plural). The number of = how many (singular count).",
                "explanation_hi": "'A large number of' = अनेक → बहुवचन HAVE।",
                "explanation_gu": "'A number of' = many = plural = HAVE.",
            }
        ]
    }
]

# Class 10 Grammar chapters data (comprehensive)
CLASS10_GRAMMAR_EXTRA = [
    {
        "num": 6,
        "topic": "Editing and Omission Exercises",
        "topic_hi": "संपादन और लोपन अभ्यास (Board Exam)",
        "topic_gu": "Editing & Omission (Board Exam)",
        "hook": "In your board exam, there are ALWAYS 4-5 marks for editing errors in a passage. Students lose these marks because they panic! Today we learn a SYSTEM so you never miss these easy marks again.",
        "hook_hi": "बोर्ड परीक्षा में हमेशा 4-5 अंक संपादन के लिए होते हैं। आज हम एक प्रणाली सीखते हैं।",
        "hook_gu": "Board exam — Editing = 4-5 marks. System seekho!",
        "theory_blocks": [
            {
                "title": "Types of Errors in Editing Exercises",
                "title_hi": "संपादन अभ्यास में त्रुटियों के प्रकार",
                "title_gu": "Editing Errors .",
                "body": "In CBSE Board editing questions, look for these error types:\n1. TENSE errors: 'He go to school yesterday.' → went\n2. SUBJECT-VERB errors: 'She don't know.' → doesn't\n3. ARTICLE errors: 'I have a umbrella.' → an umbrella\n4. PREPOSITION errors: 'He is good in English.' → at English\n5. SPELLING errors\n6. PUNCTUATION errors\n7. WORD FORM errors: 'He is very beauty.' → beautiful",
                "body_hi": "CBSE बोर्ड संपादन प्रश्नों में देखें:\n1. काल की त्रुटियां\n2. कर्ता-क्रिया त्रुटियां\n3. Article त्रुटियां\n4. Preposition त्रुटियां\n5. वर्तनी त्रुटियां\n6. विराम चिह्न त्रुटियां\n7. शब्द रूप त्रुटियां",
                "body_gu": "7 Error Types: Tense, S-V, Article, Preposition, Spelling, Punctuation, Word form.",
            }
        ],
        "examples": [
            {
                "problem": "Find and correct ONE error:\n'He has went to the market an hour ago.'",
                "problem_hi": "एक त्रुटि खोजें और सुधारें: 'He has went to market an hour ago.'",
                "problem_gu": "Error: 'He has went to market an hour ago.'",
                "solution": "Error: 'has went' → 'went'. Rule: 'an hour ago' = simple past signal → use Simple Past (went), NOT Present Perfect (has gone). Signal words like 'ago', 'yesterday', 'last week' → always Simple Past.",
                "solution_hi": "त्रुटि: 'has went' → 'went'। नियम: 'ago' = साधारण भूत → went।",
                "solution_gu": "'has went' → 'went'. 'ago' = Simple Past signal.",
            },
            {
                "problem": "Find error: 'She is good in playing the piano.'",
                "problem_hi": "त्रुटि: 'She is good in playing the piano.'",
                "problem_gu": "Error: 'good in playing'",
                "solution": "Error: 'in' → 'at'. Correct preposition: 'good AT something' (not good in). → 'She is good AT playing the piano.' Other collocations: good at sports, bad at maths, poor at dancing.",
                "solution_hi": "त्रुटि: 'in' → 'at'। सही preposition: 'good at'।",
                "solution_gu": "'in' → 'at'. Good AT something.",
            },
            {
                "problem": "Omission — Add ONE missing word:\n'She is one of most intelligent students.'",
                "problem_hi": "लोपन — एक शब्द जोड़ें: 'She is one of most intelligent students.'",
                "problem_gu": "Omission: 'She is one of most intelligent students.'",
                "solution": "Add 'the': 'She is one of THE most intelligent students.' Rule: Superlative adjectives (most intelligent, best, tallest) always need 'the' before them.",
                "solution_hi": "'the' जोड़ें: 'the most intelligent'। नियम: Superlative adjectives से पहले 'the' आता है।",
                "solution_gu": "Add 'the': 'the most intelligent'. Superlative = always 'the'.",
            }
        ],
        "mcqs": [
            {
                "question": "Board Editing — Spot the error:\n'He told me that he is very tired.'",
                "question_hi": "Board: त्रुटि खोजें: 'He told me that he is very tired.'",
                "question_gu": "Board: 'He told me that he is tired.' — error?",
                "options": ["told → tells", "is → was", "very → quite", "No error"],
                "options_hi": ["told → tells", "is → was", "very → quite", "कोई त्रुटि नहीं"],
                "options_gu": ["told → tells", "is → was", "very → quite", "No error"],
                "correct_index": 1,
                "explanation": "'is' → 'was'. Rule: Sequence of Tenses — when the reporting verb is PAST (told), the reported clause verb also changes to PAST. 'He is tired' → 'He was tired'.",
                "explanation_hi": "'is' → 'was'। नियम: जब reporting verb भूतकाल में हो, reported clause भी भूतकाल में होता है।",
                "explanation_gu": "Reporting verb = told (past) → reported = was.",
            },
            {
                "question": "Board Editing — Find the error:\n'She can sings very well.'",
                "question_hi": "Board: 'She can sings very well.' — त्रुटि?",
                "question_gu": "Board: 'She can sings very well.' — error?",
                "options": ["She → Her", "'can' should be 'could'", "sings → sing", "No error"],
                "options_hi": ["She → Her", "'can' को 'could' होना चाहिए", "sings → sing", "कोई त्रुटि नहीं"],
                "options_gu": ["She→Her", "can→could", "sings→sing", "No error"],
                "correct_index": 2,
                "explanation": "'sings' → 'sing'. Rule: Modals (can, could, may, might, must, will, would) are ALWAYS followed by base form (V1). Never add -s/-es after modals. 'She CAN SING.'",
                "explanation_hi": "'sings' → 'sing'। Modals के बाद हमेशा base form (V1) आता है।",
                "explanation_gu": "Modal + V1 (no -s). 'can sing' CORRECT.",
            },
            {
                "question": "Omission — Which word is missing?\n'He is best student in the class.'",
                "question_hi": "लोपन: 'He is best student in the class.' — कौन सा शब्द छूट गया?",
                "question_gu": "Omission: 'He is best student in class.'",
                "options": ["Insert 'a' before 'best'", "Insert 'the' before 'best'", "Insert 'very' before 'best'", "No word missing"],
                "options_hi": ["'best' से पहले 'a'", "'best' से पहले 'the'", "'best' से पहले 'very'", "कोई शब्द नहीं"],
                "options_gu": ["'a' before best", "'the' before best", "'very' before best", "No word"],
                "correct_index": 1,
                "explanation": "'the' before 'best'. Rule: Superlative adjectives (best, worst, most, tallest, fastest) ALWAYS need 'the' before them. → 'He is THE best student.'",
                "explanation_hi": "'best' से पहले 'the'। Superlative adjectives से पहले हमेशा 'the'।",
                "explanation_gu": "Superlative → 'the best'. Rule: the + superlative.",
            },
            {
                "question": "Board Editing — Find error:\n'She has been waiting since two hours.'",
                "question_hi": "Board: 'She has been waiting since two hours.' — त्रुटि?",
                "question_gu": "'waiting since two hours' — error?",
                "options": ["has been → was", "since → for", "waiting → wait", "No error"],
                "options_hi": ["has been → was", "since → for", "waiting → wait", "कोई त्रुटि नहीं"],
                "options_gu": ["has been→was", "since→for", "waiting→wait", "No error"],
                "correct_index": 1,
                "explanation": "'since' → 'for'. Rule: FOR = period of time (for two hours, for ten years). SINCE = point of time (since 5 o'clock, since Monday, since 2010). 'two hours' = period → FOR.",
                "explanation_hi": "'since' → 'for'। FOR = अवधि। SINCE = समय का बिंदु।",
                "explanation_gu": "FOR = period (hours, years). SINCE = point (5am, Monday). 'two hours' = FOR.",
            },
            {
                "question": "Spot TWO errors:\n'She don't like to eats vegetables.'",
                "question_hi": "दो त्रुटियां खोजें: 'She don't like to eats vegetables.'",
                "question_gu": "Two errors: 'She don't like to eats.'",
                "options": [
                    "don't → doesn't; eats → eat",
                    "She → Her; eats → ate",
                    "don't → didn't; eats → eating",
                    "No errors"
                ],
                "options_hi": [
                    "don't → doesn't; eats → eat",
                    "She → Her; eats → ate",
                    "don't → didn't; eats → eating",
                    "कोई त्रुटि नहीं"
                ],
                "options_gu": [
                    "don't→doesn't; eats→eat",
                    "She→Her; eats→ate",
                    "don't→didn't; eats→eating",
                    "No errors"
                ],
                "correct_index": 0,
                "explanation": "Two errors: (1) 'don't' → 'doesn't' [3rd person singular she/he/it = doesn't]. (2) 'eats' → 'eat' ['to' is always followed by V1 base form: 'to eat', never 'to eats']. Correct: 'She DOESN'T like to EAT vegetables.'",
                "explanation_hi": "दो त्रुटियां: (1) don't → doesn't [3rd person] (2) eats → eat [to + V1]।",
                "explanation_gu": "don't→doesn't (3rd person); eats→eat (to+V1).",
            }
        ]
    },
    {
        "num": 7,
        "topic": "Gap Filling Exercises",
        "topic_hi": "रिक्त स्थान भरना (Board Exam)",
        "topic_gu": "Gap Filling (Board Exam Pattern)",
        "hook": "Gap filling is worth 4 marks in your board exam. There is always a pattern — once you know WHAT to look for, you can get full marks every time. Let us crack the code!",
        "hook_hi": "Gap filling बोर्ड परीक्षा में 4 अंक के लिए है। एक बार जब आप जान जाएं कि क्या देखना है, आप हर बार पूरे अंक पा सकते हैं।",
        "hook_gu": "Gap filling = 4 marks board exam. Pattern seekho = full marks!",
        "theory_blocks": [
            {
                "title": "What to Look For in Gap Filling",
                "title_hi": "Gap Filling में क्या देखें",
                "title_gu": "Gap Filling — .",
                "body": "STEP 1: Read the whole sentence first. \nSTEP 2: Identify what TYPE of word is needed (verb/article/preposition/conjunction).\nSTEP 3: Apply the rule.\n\nCOMMON GAPS:\n- Articles: a, an, the (or zero article)\n- Prepositions: in, on, at, by, for, since, with, from, to\n- Tense forms: is/are/was/were/will/have/had\n- Modals: can/could/may/might/must/should/would\n- Conjunctions: and/but/because/although/so/while",
                "body_hi": "चरण 1: पूरा वाक्य पहले पढ़ें।\nचरण 2: पहचानें कि किस प्रकार का शब्द चाहिए।\nचरण 3: नियम लागू करें।\n\nसामान्य अंतराल: Article, Preposition, Tense, Modal, Conjunction",
                "body_gu": "Step 1: Read full sentence. Step 2: Identify gap type. Step 3: Apply rule. Common: Articles, Prepositions, Tense, Modals, Conjunctions.",
            }
        ],
        "examples": [
            {
                "problem": "Fill in: 'He has been working _____ morning.'",
                "problem_hi": "भरें: 'वह _____ सुबह से काम कर रहा है।'",
                "problem_gu": "Fill: 'He has been working _____ morning.'",
                "solution": "SINCE. Rule: FOR + duration (hours, years). SINCE + point of time (morning, Monday, 2020). 'Morning' is a point in time → SINCE.",
                "solution_hi": "SINCE। 'Morning' समय का बिंदु है → SINCE।",
                "solution_gu": "SINCE = point of time (morning).",
            },
            {
                "problem": "Fill in: 'She is interested _____ learning music.'",
                "problem_hi": "भरें: 'वह संगीत सीखने में _____ है।'",
                "problem_gu": "Fill: 'interested _____ music.'",
                "solution": "IN. Collocation: interested IN something. Other fixed prepositions: good AT, afraid OF, proud OF, responsible FOR, married TO, famous FOR, fond OF.",
                "solution_hi": "IN। Collocation: interested IN। अन्य: good at, afraid of, proud of।",
                "solution_gu": "interested IN. Fixed prepositions: good AT, afraid OF, proud OF.",
            },
            {
                "problem": "Fill in: 'He is _____ honest man.'",
                "problem_hi": "भरें: 'वह _____ ईमानदार आदमी है।'",
                "problem_gu": "Fill: 'He is _____ honest man.'",
                "solution": "AN. Rule: Use 'AN' before words that start with a VOWEL SOUND (a, e, i, o, u sound). 'Honest' starts with silent 'h' → sounds like 'onest' → vowel sound → AN. Other: an hour (silent h), an heir.",
                "solution_hi": "AN। नियम: 'AN' vowel sound से पहले। 'Honest' में 'h' मौन है → vowel sound → AN।",
                "solution_gu": "AN. 'Honest' = silent h = vowel sound = AN.",
            }
        ],
        "mcqs": [
            {
                "question": "Board Gap Fill: 'She has lived here _____ 2015.'",
                "question_hi": "Board: 'वह यहां _____ 2015 से रह रही है।'",
                "question_gu": "'She has lived here _____ 2015.'",
                "options": ["for", "since", "from", "during"],
                "options_hi": ["for", "since", "from", "during"],
                "options_gu": ["for", "since", "from", "during"],
                "correct_index": 1,
                "explanation": "SINCE. Rule: SINCE + specific point in time (2015, Monday, morning, January). FOR + period (five years, two hours). '2015' is a specific year = point in time → SINCE.",
                "explanation_hi": "SINCE। '2015' एक विशिष्ट वर्ष = समय का बिंदु → SINCE।",
                "explanation_gu": "SINCE + specific point (2015) = SINCE.",
            },
            {
                "question": "Board Gap Fill: 'He is _____ European.'",
                "question_hi": "Board: 'वह _____ यूरोपीय है।'",
                "question_gu": "'He is _____ European.'",
                "options": ["a", "an", "the", "no article"],
                "options_hi": ["a", "an", "the", "कोई Article नहीं"],
                "options_gu": ["a", "an", "the", "no article"],
                "correct_index": 0,
                "explanation": "'A'. Rule: Use A/AN based on SOUND, not spelling. 'European' starts with 'E' but sounds like 'Yoo-ropean' → consonant Y sound → use A. Trick: a European, a university, a one-way street (all start with consonant sound despite vowel letter).",
                "explanation_hi": "'A'। नियम: 'European' = 'Yoo' ध्वनि → consonant sound → A।",
                "explanation_gu": "'A European' — 'E' ='Y' sound = consonant = A (not AN).",
            },
            {
                "question": "Board Gap Fill: 'The Ganges is _____ sacred river.'",
                "question_hi": "Board: 'गंगा _____ पवित्र नदी है।'",
                "question_gu": "'The Ganges is _____ sacred river.'",
                "options": ["a", "an", "the", "no article"],
                "options_hi": ["a", "an", "the", "कोई Article नहीं"],
                "options_gu": ["a", "an", "the", "no article"],
                "correct_index": 0,
                "explanation": "'a'. Rule: 'sacred' starts with consonant sound 's' → use 'A'. Also: 'The Ganges' is already the specific river (using 'the'). We need article for 'sacred river' which is general (a = any sacred river).",
                "explanation_hi": "'a'। 'sacred' = consonant sound = A।",
                "explanation_gu": "'sacred' = 's' consonant sound = 'a'.",
            },
            {
                "question": "Fill in: 'I was tired, _____ I went to sleep early.'",
                "question_hi": "भरें: 'मैं थका हुआ था, _____ मैं जल्दी सो गया।'",
                "question_gu": "'I was tired, _____ I went to sleep early.'",
                "options": ["but", "so", "although", "because"],
                "options_hi": ["but", "so", "although", "because"],
                "options_gu": ["but", "so", "although", "because"],
                "correct_index": 1,
                "explanation": "SO = result/consequence. Tired is the CAUSE, sleeping early is the RESULT. 'I was tired SO I went to sleep.' Compare: BECAUSE (introduces reason/cause), BUT (contrast), ALTHOUGH (concession).",
                "explanation_hi": "SO = परिणाम। थका = कारण → सोना = परिणाम → SO।",
                "explanation_gu": "SO = result. Tired=cause, sleep=result → SO.",
            },
            {
                "question": "Board: 'He succeeded _____ working very hard.'",
                "question_hi": "Board: 'उसने बहुत मेहनत करके सफलता _____।'",
                "question_gu": "'He succeeded _____ working very hard.'",
                "options": ["in", "by", "with", "at"],
                "options_hi": ["in", "by", "with", "at"],
                "options_gu": ["in", "by", "with", "at"],
                "correct_index": 1,
                "explanation": "'BY'. Rule: 'BY + V-ing' shows the METHOD or MEANS by which something is done. 'He succeeded BY working hard.' Also: BY bus, BY phone, BY train = means of transport/communication.",
                "explanation_hi": "'BY'। BY + V-ing = तरीका/साधन। 'BY working' = मेहनत करके।",
                "explanation_gu": "BY + V-ing = method/means. 'by working hard'.",
            }
        ]
    }
]

def build_grammar_blocks(ch_data, class_num):
    """Build comprehensive 8-step grammar chapter blocks."""
    num = ch_data["num"]
    topic = ch_data["topic"]
    topic_hi = ch_data["topic_hi"]
    topic_gu = ch_data["topic_gu"]
    prefix = f"ncert_class{class_num}_grammar"
    book = "Beehive Grammar Supplement" if class_num == 9 else "First Flight Grammar"
    book_hi = "बीहाइव व्याकरण" if class_num == 9 else "फर्स्ट फ्लाइट व्याकरण"
    book_gu = "Beehive Grammar" if class_num == 9 else "First Flight Grammar"

    blocks = [
        # Step 1: Hook
        {
            "id": f"KOBJ_{prefix.upper()}_CH{num}_HOOK",
            "type": "hook",
            "title": f"Grammar Hook: {topic}",
            "title_hi": f"व्याकरण परिचय: {topic_hi}",
            "title_gu": f"Grammar: {topic_gu}",
            "body": ch_data.get("hook", f"Let us master {topic} today — an essential topic for Board Exams!"),
            "body_hi": ch_data.get("hook_hi", f"आज हम {topic_hi} सीखते हैं — बोर्ड परीक्षा के लिए आवश्यक!"),
            "body_gu": ch_data.get("hook_gu", f"Board exam = {topic_gu} important!"),
        },
        # Step 2: Socratic
        {
            "id": f"KOBJ_{prefix.upper()}_CH{num}_SOCRATIC",
            "type": "socratic_question",
            "question": f"Before we study {topic}, can you try to identify the error in this sentence: 'She go to school every day'?",
            "question_hi": f"{topic_hi} सीखने से पहले, क्या आप इस वाक्य में त्रुटि पहचान सकते हैं?",
            "question_gu": f"{topic_gu} — .",
            "explanation": f"Think about it! This is exactly what {topic} helps us fix. Let us discover the rules together.",
            "explanation_hi": f"यही {topic_hi} सही करने में मदद करता है।",
            "explanation_gu": f"{topic_gu} — rules fix this!",
        },
        # Step 3: Discovery
        {
            "id": f"KOBJ_{prefix.upper()}_CH{num}_DISCOVERY",
            "type": "discovery",
            "title": f"Discover: {topic} in Real Life",
            "title_hi": f"खोज: वास्तविक जीवन में {topic_hi}",
            "title_gu": f"Discovery: {topic_gu}",
            "body": f"Look around you — {topic} appears in every English text you read, every exam you write, every email you send. Mastering {topic} = mastering English communication.",
            "body_hi": f"{topic_hi} हर अंग्रेजी पाठ में, हर परीक्षा में, हर ईमेल में दिखाई देता है। {topic_hi} में महारत = अंग्रेजी संचार में महारत।",
            "body_gu": f"{topic_gu} — everywhere in English. Master it = master English.",
        },
    ]

    # Theory blocks (Step 4: Reveal)
    for i, theory in enumerate(ch_data.get("theory_blocks", []), start=1):
        blocks.append({
            "id": f"KOBJ_{prefix.upper()}_CH{num}_THEORY_{i}",
            "type": "theory",
            "title": theory["title"],
            "title_hi": theory["title_hi"],
            "title_gu": theory["title_gu"],
            "body": theory["body"],
            "body_hi": theory["body_hi"],
            "body_gu": theory["body_gu"],
        })

    # Teacher tip
    blocks.append({
        "id": f"KOBJ_{prefix.upper()}_CH{num}_TEACHER_TIP",
        "type": "teacher_tip",
        "title": f"Board Exam Tip: {topic}",
        "title_hi": f"बोर्ड परीक्षा टिप: {topic_hi}",
        "title_gu": f"Board Tip: {topic_gu}",
        "body": f"In CBSE Class {class_num} board exam, {topic} questions appear in: (1) Fill in the blanks (2) Editing/Omission exercises (3) Rearranging jumbled sentences (4) Sentence transformation. Always justify your answer with the rule!",
        "body_hi": f"CBSE Class {class_num} बोर्ड परीक्षा में {topic_hi} प्रश्न आते हैं: (1) रिक्त स्थान भरना (2) संपादन/लोपन (3) अव्यवस्थित वाक्य (4) वाक्य परिवर्तन।",
        "body_gu": f"Board exam — {topic_gu} appears in: Fill blanks, Editing, Jumbled sentences, Transformation.",
    })

    # Worked Examples (Step 4-5)
    for i, ex in enumerate(ch_data.get("examples", []), start=1):
        blocks.append({
            "id": f"KOBJ_{prefix.upper()}_CH{num}_EXAMPLE_{i}",
            "type": "worked_example",
            "title": f"Solved Example {i}: {topic}",
            "title_hi": f"हल किया गया उदाहरण {i}: {topic_hi}",
            "title_gu": f"Solved Ex {i}: {topic_gu}",
            "problem": ex.get("problem", ""),
            "problem_hi": ex.get("problem_hi", ex.get("problem", "")),
            "problem_gu": ex.get("problem_gu", ex.get("problem", "")),
            "solution": ex.get("solution", ""),
            "solution_hi": ex.get("solution_hi", ex.get("solution", "")),
            "solution_gu": ex.get("solution_gu", ex.get("solution", "")),
        })

    # Step 5: MCQ Knowledge Check
    for i, mcq in enumerate(ch_data.get("mcqs", []), start=1):
        blocks.append({
            "id": f"KOBJ_{prefix.upper()}_CH{num}_MCQ_{i}",
            "type": "quiz",
            "question": mcq["question"],
            "question_hi": mcq.get("question_hi", mcq["question"]),
            "question_gu": mcq.get("question_gu", mcq["question"]),
            "options": mcq["options"],
            "options_hi": mcq.get("options_hi", mcq["options"]),
            "options_gu": mcq.get("options_gu", mcq["options"]),
            "correct_index": mcq["correct_index"],
            "explanation": mcq["explanation"],
            "explanation_hi": mcq.get("explanation_hi", mcq["explanation"]),
            "explanation_gu": mcq.get("explanation_gu", mcq["explanation"]),
        })

    # Step 6: Reflection
    blocks.append({
        "id": f"KOBJ_{prefix.upper()}_CH{num}_REFLECTION",
        "type": "reflection",
        "title": "Reflect & Apply",
        "title_hi": "चिंतन और प्रयोग",
        "title_gu": "Reflect & Apply",
        "body": f"Write 5 sentences of your own using {topic}. Try to use as many rules as you have learnt today. Then, check if you have used the rules correctly.",
        "body_hi": f"{topic_hi} का उपयोग करके अपने 5 वाक्य लिखें।",
        "body_gu": f"{topic_gu} use karke 5 sentences lakho.",
    })

    # Step 7: Connection
    blocks.append({
        "id": f"KOBJ_{prefix.upper()}_CH{num}_CONNECTION",
        "type": "connection",
        "title": "Connection: Grammar in Writing",
        "title_hi": "संबंध: लेखन में व्याकरण",
        "title_gu": "Connection: Writing mein Grammar",
        "body": f"{topic} connects to: Letter Writing (use correct tenses), Story Writing (maintain consistent tense), Comprehension passages (identify tenses used by the author), and all future English chapters.",
        "body_hi": f"{topic_hi} जुड़ा है: पत्र लेखन, कहानी लेखन, बोधगम्य अनुच्छेदों से।",
        "body_gu": f"{topic_gu} connects to: Letter writing, Story writing, Comprehension passages.",
    })

    # Step 8: Mastery
    blocks.append({
        "id": f"KOBJ_{prefix.upper()}_CH{num}_MASTERY",
        "type": "mastery",
        "title": f"Mastery: {topic} — Board Ready!",
        "title_hi": f"महारत: {topic_hi} — बोर्ड के लिए तैयार!",
        "title_gu": f"Mastery: {topic_gu} — Board Ready!",
        "body": f"Excellent! You have completed {topic} for Class {class_num}. You can now confidently handle ALL board exam questions on {topic}. Remember: Practice is the key to perfection!",
        "body_hi": f"शानदार! आपने Class {class_num} के लिए {topic_hi} पूरा किया। अब आप बोर्ड परीक्षा के सभी प्रश्न आत्मविश्वास से हल कर सकते हैं!",
        "body_gu": f"Class {class_num} {topic_gu} COMPLETE! Board exam ready!",
    })

    return blocks


def write_and_sync(prefix, ch_num, blocks, class_num):
    """Write chapter file and sync to learning_modules and assessment."""
    # 1. Write chapter file (flat list)
    chapter_file = f"app_core/chapters/{prefix}_ch{ch_num}.json"
    with open(chapter_file, 'w', encoding='utf-8') as f:
        json.dump(blocks, f, ensure_ascii=False, indent=2)

    ch_title = f"Chapter {ch_num}: {blocks[0].get('title', f'Grammar Ch{ch_num}')}"

    # 2. Sync ncert learning module
    lm_dir = f"app_core/learning_modules/{prefix}_ch{ch_num}"
    os.makedirs(lm_dir, exist_ok=True)
    with open(os.path.join(lm_dir, "blocks.json"), 'w', encoding='utf-8') as f:
        json.dump(blocks, f, ensure_ascii=False, indent=2)
    with open(os.path.join(lm_dir, "metadata.json"), 'w', encoding='utf-8') as f:
        json.dump({"id": f"{prefix}_ch{ch_num}", "title": ch_title, "subject_id": f"{prefix.rsplit('_', 1)[0]}", "class_id": prefix.rsplit("_", 2)[0]}, f, ensure_ascii=False, indent=2)

    # 3. Sync gseb learning module
    gseb_prefix = prefix.replace("ncert_", "gseb_").replace("cbse_", "gseb_")
    gseb_dir = f"app_core/learning_modules/{gseb_prefix}_ch{ch_num}"
    os.makedirs(gseb_dir, exist_ok=True)
    with open(os.path.join(gseb_dir, "blocks.json"), 'w', encoding='utf-8') as f:
        json.dump(blocks, f, ensure_ascii=False, indent=2)
    with open(os.path.join(gseb_dir, "metadata.json"), 'w', encoding='utf-8') as f:
        json.dump({"id": f"{gseb_prefix}_ch{ch_num}", "title": ch_title}, f, ensure_ascii=False, indent=2)

    # 4. Assessment question bank
    q_blocks = [b for b in blocks if b.get("type") == "quiz" and "question" in b]
    questions = [{
        "id": b.get("id", ""), "question": b["question"],
        "question_hi": b.get("question_hi", b["question"]),
        "question_gu": b.get("question_gu", b["question"]),
        "options": b.get("options", []), "options_hi": b.get("options_hi", b.get("options", [])),
        "options_gu": b.get("options_gu", b.get("options", [])),
        "correct_index": b.get("correct_index", 0),
        "explanation": b.get("explanation", ""),
        "explanation_hi": b.get("explanation_hi", b.get("explanation", "")),
        "explanation_gu": b.get("explanation_gu", b.get("explanation", ""))
    } for b in q_blocks]

    for ap in [prefix, gseb_prefix]:
        with open(f"app_core/assessment/{ap}_ch{ch_num}_questions.json", 'w', encoding='utf-8') as f:
            json.dump(questions, f, ensure_ascii=False, indent=2)

    return len(blocks), len(questions)


# Remaining chapters with reduced but complete data
def make_chapter_simple(num, topic, topic_hi, topic_gu, rule_body, rule_body_hi, rule_body_gu, examples, mcqs):
    return {
        "num": num, "topic": topic, "topic_hi": topic_hi, "topic_gu": topic_gu,
        "hook": f"Did you know that {topic} errors are among the top 5 mistakes in board exams? Master this today and secure your marks!",
        "hook_hi": f"क्या आप जानते हैं कि {topic_hi} की गलतियां बोर्ड परीक्षा में शीर्ष 5 गलतियों में से एक हैं? आज इसे समझें!",
        "hook_gu": f"{topic_gu} errors = top board exam mistakes. Fix them today!",
        "theory_blocks": [{"title": f"The Rules of {topic}", "title_hi": f"{topic_hi} के नियम", "title_gu": f"{topic_gu} Rules", "body": rule_body, "body_hi": rule_body_hi, "body_gu": rule_body_gu}],
        "examples": examples,
        "mcqs": mcqs,
    }


CLASS9_REMAINING = [
    make_chapter_simple(
        4, "Reported Speech", "अप्रत्यक्ष कथन", "Reported Speech",
        "Direct Speech quotes exact words: He said, 'I am happy.'\nIndirect Speech reports meaning: He said (that) he was happy.\n\nKey Changes in Indirect Speech:\n1. Inverted commas removed.\n2. 'That' added.\n3. Tense changes back (backshift): am→was, is→was, are→were, will→would, can→could, has→had, have→had\n4. Pronouns change: I→he/she, we→they, you→he/she/they\n5. Time expressions change: now→then, today→that day, yesterday→the day before, tomorrow→the next day, here→there",
        "प्रत्यक्ष भाषण सटीक शब्दों को उद्धृत करता है: उसने कहा, 'मैं खुश हूं।'\nअप्रत्यक्ष भाषण अर्थ रिपोर्ट करता है: उसने कहा कि वह खुश था।\n\nमुख्य परिवर्तन: काल पीछे जाता है, सर्वनाम बदलते हैं, समय अभिव्यक्तियां बदलती हैं।",
        "Direct Speech = exact words. Indirect = report.\nTense backshift: am/is→was. Pronoun: I→he/she.",
        [
            {"problem": "He said, 'I am very tired.' → Indirect?", "problem_hi": "प्रत्यक्ष → अप्रत्यक्ष", "problem_gu": "Direct → Indirect.",
             "solution": "He said (that) he was very tired. Changes: 'I'→'he', 'am'→'was', inverted commas removed.", "solution_hi": "He said that he was very tired. 'I'→'he', 'am'→'was'.", "solution_gu": "he was very tired."},
            {"problem": "She said, 'I will come tomorrow.' → Indirect?", "problem_hi": "अप्रत्यक्ष में बदलें।", "problem_gu": "Indirect mein badlo.",
             "solution": "She said that she would come the next day. Changes: will→would, tomorrow→the next day, I→she.", "solution_hi": "will→would, tomorrow→the next day.", "solution_gu": "would come the next day."},
            {"problem": "He said, 'Can you help me?' → Indirect?", "problem_hi": "Request → Indirect.", "problem_gu": "Request indirect.",
             "solution": "He asked if I could help him. [Questions: use 'asked if/whether', change 'can'→'could', 'you'→'I', 'me'→'him']", "solution_hi": "asked if I could help him.", "solution_gu": "asked if/whether."},
        ],
        [
            {"question": "'She said, I love reading books.' Change to Indirect Speech.",
             "question_hi": "Indirect में बदलें: 'She said, I love reading books.'",
             "question_gu": "Indirect: 'She said, I love reading books.'",
             "options": ["She said she loved reading books.", "She said she loves reading books.", "She said that I love books.", "She told she loved books."],
             "options_hi": ["She said she loved reading books.", "She said she loves reading books.", "She said that I love books.", "She told she loved books."],
             "options_gu": ["She said she loved books.", "She said she loves books.", "She said I love.", "She told loved."],
             "correct_index": 0,
             "explanation": "Indirect: She said (that) she LOVED reading books. Changes: 'I'→'she', 'love'→'loved' (tense backshift: present→past).",
             "explanation_hi": "she said that she LOVED. I→she, love→loved.", "explanation_gu": "she loved. Backshift: love→loved."},
            {"question": "He said, 'I was watching TV yesterday.' → Indirect Speech.",
             "question_hi": "Indirect: 'He said, I was watching TV yesterday.'",
             "question_gu": "Indirect: watching TV yesterday.",
             "options": ["He said he had been watching TV the day before.", "He said he was watching TV yesterday.", "He said he has been watching TV.", "He told he was watching TV."],
             "options_hi": ["had been watching... day before.", "was watching yesterday.", "has been watching.", "told was watching."],
             "options_gu": ["had been watching day before.", "was watching yesterday.", "has been.", "told."],
             "correct_index": 0,
             "explanation": "Past Continuous → Past Perfect Continuous: 'was watching'→'had been watching'. 'yesterday'→'the day before'.",
             "explanation_hi": "Past Continuous → Past Perfect Continuous. yesterday → the day before.",
             "explanation_gu": "was watching → had been watching. yesterday → day before."},
            {"question": "The teacher said, 'Do not make noise.' → Indirect?",
             "question_hi": "Command Indirect: 'Do not make noise.'",
             "question_gu": "Command Indirect: 'Do not make noise.'",
             "options": ["Teacher said to not make noise.", "Teacher told not making noise.", "Teacher ordered them not to make noise.", "Teacher told them make no noise."],
             "options_hi": ["said to not.", "told not making.", "ordered not to make noise.", "told make no."],
             "options_gu": ["said not.", "told not making.", "ordered not to make noise.", "told make no."],
             "correct_index": 2,
             "explanation": "Commands use 'ordered/told/asked + object + (not) to V1'. Negative command: 'not to make'. → 'The teacher ordered them NOT TO MAKE noise.'",
             "explanation_hi": "Commands: ordered/told + object + not to V1.", "explanation_gu": "ordered not to V1."},
            {"question": "Fill blank: 'She asked me _____ I was feeling better.'",
             "question_hi": "रिक्त भरें: 'She asked me _____ I was feeling better.'",
             "question_gu": "'She asked me _____ I was feeling better.'",
             "options": ["that", "if", "what", "which"],
             "options_hi": ["that", "if", "what", "which"],
             "options_gu": ["that", "if", "what", "which"],
             "correct_index": 1,
             "explanation": "Use 'if/whether' when reporting Yes/No questions. 'Are you feeling better?' → 'She asked me IF I was feeling better.'",
             "explanation_hi": "Yes/No questions → if/whether.", "explanation_gu": "Yes/No questions = if/whether."},
            {"question": "Board Edit: 'He told me that he will come tomorrow.' Find error.",
             "question_hi": "Board Edit: 'He told me that he will come tomorrow.'",
             "question_gu": "Board Edit: 'he will come tomorrow.'",
             "options": ["told → said", "will → would; tomorrow → the next day", "come → comes", "No error"],
             "options_hi": ["told → said", "will → would; tomorrow → next day", "come → comes", "No error"],
             "options_gu": ["told→said", "will→would + next day", "come→comes", "No error"],
             "correct_index": 1,
             "explanation": "Two errors: (1) 'will'→'would' (tense backshift). (2) 'tomorrow'→'the next day' (time expression change). Correct: 'He told me that he WOULD come THE NEXT DAY.'",
             "explanation_hi": "will→would + tomorrow→the next day.", "explanation_gu": "would + the next day."},
        ]
    ),
    make_chapter_simple(
        5, "Active and Passive Voice", "कर्तृवाच्य और कर्मवाच्य", "Active & Passive Voice",
        "ACTIVE VOICE: Subject performs the action.\n   The chef cooked the meal. (Subject = chef, Action = cooked)\n\nPASSIVE VOICE: Subject receives the action.\n   The meal was cooked by the chef.\n\nFormula: Object (of active) → Subject (of passive)\nPassive = To Be (in correct tense) + Past Participle (V3)\n\nTense conversions:\nSimple Present: is/are + V3\nSimple Past: was/were + V3\nPresent Continuous: is/are being + V3\nPast Continuous: was/were being + V3\nPresent Perfect: has/have been + V3\nPast Perfect: had been + V3\nSimple Future: will be + V3\nFuture Perfect: will have been + V3",
        "Active: Subject क्रिया करता है।\nPassive: Subject क्रिया प्राप्त करता है।\nFormula: Object→Subject, To Be + V3\nकाल परिवर्तन: Simple Present→is/are+V3, Past→was/were+V3",
        "Active = subject action kare. Passive = object becomes subject.\nFormula: is/are/was/were + V3. By + agent.",
        [
            {"problem": "Change to Passive: 'Ram writes a letter.'",
             "problem_hi": "Passive में बदलें: 'Ram writes a letter.'",
             "problem_gu": "Passive: 'Ram writes a letter.'",
             "solution": "A letter is written by Ram. Formula: Object (A letter) + is/are + V3 (written) + by + Subject (Ram).",
             "solution_hi": "A letter is written by Ram. Object→Subject, is/are+V3.", "solution_gu": "A letter is written by Ram."},
            {"problem": "Change to Passive: 'They were building a new bridge.'",
             "problem_hi": "Passive: 'वे एक नया पुल बना रहे थे।'", "problem_gu": "Passive: 'building new bridge.'",
             "solution": "A new bridge was being built by them. Past Continuous Passive = was/were being + V3.",
             "solution_hi": "Past Continuous Passive: was/were being + V3.", "solution_gu": "was/were being + V3."},
            {"problem": "Change to Active: 'The cake was eaten by the children.'",
             "problem_hi": "Active में बदलें।", "problem_gu": "Active: 'cake was eaten by children.'",
             "solution": "The children ate the cake. Agent (by + children) → Subject. Cake → Object. Was eaten → ate (Simple Past).",
             "solution_hi": "The children ate the cake.", "solution_gu": "The children ate the cake."},
        ],
        [
            {"question": "Change to Passive: 'She is teaching the students.'",
             "question_hi": "Passive: 'She is teaching the students.'",
             "question_gu": "Passive: 'She is teaching students.'",
             "options": ["Students are being taught by her.", "Students are taught by her.", "Students were being taught by her.", "Students have been taught by her."],
             "options_hi": ["Students are being taught.", "Students are taught.", "Students were being taught.", "Students have been taught."],
             "options_gu": ["are being taught.", "are taught.", "were being taught.", "have been taught."],
             "correct_index": 0,
             "explanation": "Present Continuous Passive = is/are BEING + V3. 'is teaching' → 'are being taught'.",
             "explanation_hi": "Present Continuous Passive: is/are being + V3.", "explanation_gu": "are being taught."},
            {"question": "Passive of: 'Someone has stolen my bicycle.'",
             "question_hi": "Passive: 'Someone has stolen my bicycle.'",
             "question_gu": "Passive: 'has stolen my bicycle.'",
             "options": ["My bicycle was stolen.", "My bicycle has been stolen.", "My bicycle had been stolen.", "My bicycle is stolen."],
             "options_hi": ["was stolen.", "has been stolen.", "had been stolen.", "is stolen."],
             "options_gu": ["was stolen.", "has been stolen.", "had been stolen.", "is stolen."],
             "correct_index": 1,
             "explanation": "Present Perfect Passive = has/have BEEN + V3. 'has stolen' → 'has been stolen'. Agent (someone) is dropped as it is indefinite.",
             "explanation_hi": "Present Perfect Passive: has/have been + V3.", "explanation_gu": "has been stolen."},
            {"question": "Board Exam: 'English is spoke all over the world.' Find error.",
             "question_hi": "Board: 'English is spoke all over.' — Error?",
             "question_gu": "'is spoke' — error?",
             "options": ["English → The English", "is → are", "spoke → spoken", "No error"],
             "options_hi": ["English → The English", "is → are", "spoke → spoken", "No error"],
             "options_gu": ["English→The English", "is→are", "spoke→spoken", "No error"],
             "correct_index": 2,
             "explanation": "'spoke' → 'spoken'. Passive voice = TO BE + PAST PARTICIPLE (V3). 'Spoke' is Simple Past (V2), NOT V3. V3 of 'speak' = 'spoken'. → 'English is SPOKEN all over the world.'",
             "explanation_hi": "Passive = is/are + V3. spoke = V2, spoken = V3. → is spoken.", "explanation_gu": "Passive = is/are + V3. spoke→spoken."},
            {"question": "The results _____ (announce) tomorrow.",
             "question_hi": "परिणाम कल _____ (announce) होंगे।",
             "question_gu": "'Results _____ (announce) tomorrow.'",
             "options": ["will announce", "will be announced", "are announced", "have been announced"],
             "options_hi": ["will announce", "will be announced", "are announced", "have been announced"],
             "options_gu": ["will announce", "will be announced", "are announced", "have been announced"],
             "correct_index": 1,
             "explanation": "Future Passive = will be + V3. 'announce' → 'will be announced'. The results cannot announce themselves, so passive is needed.",
             "explanation_hi": "Future Passive: will be + V3 → will be announced.", "explanation_gu": "will be announced. Future Passive."},
            {"question": "Choose correct passive: 'They are constructing a new road.'",
             "question_hi": "Passive: 'They are constructing a new road.'",
             "question_gu": "Passive: 'constructing new road.'",
             "options": ["A new road is constructed by them.", "A new road is being constructed by them.", "A new road was constructed by them.", "A new road had been constructed by them."],
             "options_hi": ["is constructed.", "is being constructed.", "was constructed.", "had been constructed."],
             "options_gu": ["is constructed.", "is being constructed.", "was constructed.", "had been constructed."],
             "correct_index": 1,
             "explanation": "Present Continuous (are constructing) → Present Continuous Passive (is being constructed). Formula: Subject + is/are + being + V3.",
             "explanation_hi": "Present Continuous → is/are being + V3.", "explanation_gu": "is being constructed."},
        ]
    ),
]


print("=" * 70)
print("   BUILDING ENGLISH GRAMMAR — CLASS 9 & CLASS 10")
print("=" * 70)

total_blocks = 0
total_questions = 0

# Build Class 9 Grammar (existing 3 + 7 more needed = 10 total)
print("\n--- CLASS 9 GRAMMAR (10 chapters) ---")
for ch_data in CLASS9_GRAMMAR + CLASS9_REMAINING:
    blocks = build_grammar_blocks(ch_data, 9)
    nb, nq = write_and_sync("ncert_class9_grammar", ch_data["num"], blocks, 9)
    # Also write cbse version
    write_and_sync("cbse_class9_grammar", ch_data["num"], blocks, 9)
    total_blocks += nb
    total_questions += nq
    print(f"  Ch {ch_data['num']:2d}: {ch_data['topic']:45s} | {nb} blocks | {nq} MCQs")

# Build Class 10 Grammar (existing 5 + 5 more needed = 10 total)
print("\n--- CLASS 10 GRAMMAR (10 chapters) ---")

# First unwrap and re-save the existing 5 chapters
for ch_num in range(1, 6):
    fpath = f"app_core/chapters/ncert_class10_grammar_ch{ch_num}.json"
    with open(fpath, 'r', encoding='utf-8') as f:
        raw = json.load(f)
    blocks = raw if isinstance(raw, list) else raw.get("blocks", [])
    # Ensure all trilingual
    for b in blocks:
        for k in ["title", "body", "question", "explanation"]:
            if k in b:
                v = b[k]
                if not b.get(f"{k}_hi"): b[f"{k}_hi"] = v
                if not b.get(f"{k}_gu"): b[f"{k}_gu"] = v
        if "options" in b:
            if not b.get("options_hi"): b["options_hi"] = b["options"]
            if not b.get("options_gu"): b["options_gu"] = b["options"]
    nb, nq = write_and_sync("ncert_class10_grammar", ch_num, blocks, 10)
    write_and_sync("cbse_class10_grammar", ch_num, blocks, 10)
    total_blocks += nb
    total_questions += nq
    print(f"  Ch {ch_num:2d}: (existing, unwrapped & synced)                       | {nb} blocks | {nq} MCQs")

# Build new chapters 6-10 for Class 10
for ch_data in CLASS10_GRAMMAR_EXTRA:
    blocks = build_grammar_blocks(ch_data, 10)
    nb, nq = write_and_sync("ncert_class10_grammar", ch_data["num"], blocks, 10)
    write_and_sync("cbse_class10_grammar", ch_data["num"], blocks, 10)
    total_blocks += nb
    total_questions += nq
    print(f"  Ch {ch_data['num']:2d}: {ch_data['topic']:45s} | {nb} blocks | {nq} MCQs")

print(f"\n{'='*70}")
print(f"  Total blocks created/synced: {total_blocks}")
print(f"  Total MCQs created/synced  : {total_questions}")
print(f"{'='*70}")
