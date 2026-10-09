import os
import json

# ============================================================
# MASTER ENGLISH GRAMMAR BUILDER — CLASS 9 & CLASS 10
# Full Trilingual Support (EN, HI, GU), Unwrapped Root List [...],
# 8-Step Socratic Pedagogy, Board Exam Exercises, 3-Way Sync
# ============================================================

CHAPTERS_DATA = [
    # ------------------------------------------------------------
    # CLASS 9 GRAMMAR (CHAPTERS 1 - 10)
    # ------------------------------------------------------------
    {
        "id": "ncert_class9_grammar_ch1",
        "title": "Tenses — Time & Aspect",
        "title_hi": "काल — समय और रूप (Tenses)",
        "title_gu": "કાળ — સમય અને પ્રકાર (Tenses)",
        "class_num": 9,
        "ch_num": 1,
        "blocks": [
            {
                "id": "KOBJ_C9_ENG_G1_B1",
                "type": "hook",
                "title": "The Time Traveler's Dilemma",
                "title_hi": "समय यात्री की दुविधा",
                "title_gu": "સમય યાત્રીની મુંઝવણ",
                "body": "Imagine texting your friend: 'I will eat pizza yesterday.' Your friend would be completely confused! Tenses tell us WHEN an action happens—in the past, present, or future.",
                "body_hi": "कल्पना कीजिए कि आप अपने दोस्त को मैसेज भेजते हैं: 'मैं कल पिज्जा खाऊंगा।' आपका दोस्त उलझन में पड़ जाएगा! काल हमें बताते हैं कि कोई क्रिया कब होती है—अतीत में, वर्तमान में, या भविष्य में।",
                "body_gu": "કલ્પના કરો તમે મિત્રને મેસેજ કરો: 'હું ગઈકાલે પિઝા ખાઇશ.' તમારો મિત્ર ગૂંચવાઈ જશે! કાળ આપણને જણાવે છે કે ક્રિયા ક્યારે ઘટે છે—ભૂતકાળમાં, વર્તમાનમાં કે ભવિષ્યમાં."
            },
            {
                "id": "KOBJ_C9_ENG_G1_B2",
                "type": "socratic",
                "question": "What is the difference between 'I eat breakfast' and 'I am eating breakfast'?",
                "question_hi": "'मैं नाश्ता करता हूं' और 'मैं नाश्ता कर रहा हूं' में क्या अंतर है?",
                "question_gu": "'હું નાસ્તો કરું છું' અને 'હું નાસ્તો કરી રહ્યો છું' વચ્ચે શું તફાવત છે?",
                "options": [
                    "One is a daily routine, the other is happening right now",
                    "Both mean the exact same thing",
                    "One is past tense, one is future tense",
                    "One is grammatically incorrect"
                ],
                "options_hi": [
                    "एक दैनिक दिनचर्या है, दूसरा अभी हो रहा है",
                    "दोनों का अर्थ बिल्कुल एक ही है",
                    "एक भूतकाल है, एक भविष्यकाल है",
                    "एक व्याकरण की दृष्टि से गलत है"
                ],
                "options_gu": [
                    "એક દૈનિક દિનચર્યા છે, બીજું અત્યારે થઈ રહ્યું છે",
                    "બંનેનો અર્થ એક જ થાય છે",
                    "એક ભૂતકાળ છે, એક ભવિષ્યકાળ છે",
                    "એક વ્યાકરણની દ્રષ્ટિએ ખોટું છે"
                ],
                "correct_index": 0,
                "explanation": "Simple Present ('I eat') describes routines or facts. Present Continuous ('I am eating') describes actions happening right now.",
                "explanation_hi": "सरल वर्तमान ('मैं खाता हूं') दिनचर्या या तथ्यों का वर्णन करता है। वर्तमान सतत ('मैं खा रहा हूं') अभी हो रही क्रियाओं का वर्णन करता है।",
                "explanation_gu": "સાદો વર્તમાન ('હું ખાઉં છું') નિયમિત ટેવ કે સત્ય દર્શાવે છે. ચાલુ વર્તમાન ('હું ખાઈ રહ્યો છું') અત્યારે થઈ રહેલી ક્રિયા દર્શાવે છે."
            },
            {
                "id": "KOBJ_C9_ENG_G1_B3",
                "type": "theory",
                "title": "The 12 Tense Matrix",
                "title_hi": "12 काल का मैट्रिक्स",
                "title_gu": "12 કાળનું મેટ્રિક્સ",
                "body": "English has 3 main Times (Present, Past, Future) × 4 Aspects (Simple, Continuous, Perfect, Perfect Continuous) = 12 Tenses.\n\n• Simple Present: Subject + V1 (s/es)\n• Present Continuous: Subject + is/am/are + V4 (-ing)\n• Present Perfect: Subject + has/have + V3\n• Present Perfect Continuous: Subject + has/have + been + V4",
                "body_hi": "अंग्रेजी में 3 मुख्य समय (वर्तमान, भूत, भविष्य) × 4 पहलू (सरल, सतत, पूर्ण, पूर्ण सतत) = 12 काल हैं।\n\n• सरल वर्तमान: कर्ता + V1 (s/es)\n• वर्तमान सतत: कर्ता + is/am/are + V4 (-ing)\n• वर्तमान पूर्ण: कर्ता + has/have + V3\n• वर्तमान पूर्ण सतत: कर्ता + has/have + been + V4",
                "body_gu": "અંગ્રેજીમાં 3 મુખ્ય સમય (વર્તમાન, ભૂત, ભવિષ્ય) × 4 પ્રકાર (સાદો, ચાલુ, પૂર્ણ, પૂર્ણ ચાલુ) = 12 કાળ છે.\n\n• સાદો વર્તમાન: કર્તા + V1 (s/es)\n• ચાલુ વર્તમાન: કર્તા + is/am/are + V4 (-ing)\n• પૂર્ણ વર્તમાન: કર્તા + has/have + V3\n• પૂર્ણ ચાલુ વર્તમાન: કર્તા + has/have + been + V4"
            },
            {
                "id": "KOBJ_C9_ENG_G1_B4",
                "type": "quiz",
                "question": "Choose the correct form: 'She ______ (study) for three hours before the lights went out.'",
                "question_hi": "सही रूप चुनें: 'She ______ (study) for three hours before the lights went out.'",
                "question_gu": "સાચું રૂપ પસંદ કરો: 'She ______ (study) for three hours before the lights went out.'",
                "options": [
                    "had been studying",
                    "has studied",
                    "was studied",
                    "is studying"
                ],
                "options_hi": [
                    "had been studying",
                    "has studied",
                    "was studied",
                    "is studying"
                ],
                "options_gu": [
                    "had been studying",
                    "has studied",
                    "was studied",
                    "is studying"
                ],
                "correct_index": 0,
                "explanation": "Past Perfect Continuous ('had been studying') is used for an action that continued for a duration up to another point in the past.",
                "explanation_hi": "Past Perfect Continuous ('had been studying') का उपयोग अतीत में किसी अन्य बिंदु तक जारी रहने वाली क्रिया के लिए किया जाता है।",
                "explanation_gu": "Past Perfect Continuous ('had been studying') નો ઉપયોગ ભૂતકાળમાં કોઈ ચોક્કસ સમય સુધી ચાલેલી દીર્ઘ ક્રિયા દર્શાવવા થાય છે."
            }
        ]
    },
    {
        "id": "ncert_class9_grammar_ch2",
        "title": "Modals — Expressing Ability, Permission & Obligation",
        "title_hi": "मोडल्स — क्षमता, अनुमति और दायित्व (Modals)",
        "title_gu": "મોડલ્સ — ક્ષમતા, પરવાનગી અને ફરજ (Modals)",
        "class_num": 9,
        "ch_num": 2,
        "blocks": [
            {
                "id": "KOBJ_C9_ENG_G2_B1",
                "type": "hook",
                "title": "Can vs May: A Classroom Classic",
                "title_hi": "Can बनाम May: एक क्लासिक उदाहरण",
                "title_gu": "Can વિરૂદ્ધ May: વર્ગખંડનું ઉત્તમ ઉદાહરણ",
                "body": "When a student asks 'Can I go to the bathroom?', the teacher often replies: 'You CAN, but you MAY not!' Why? Because CAN shows physical ability, while MAY shows permission!",
                "body_hi": "जब कोई छात्र पूछता है 'Can I go to the bathroom?', तो शिक्षक अक्सर जवाब देते हैं: 'You CAN, but you MAY not!' क्यों? क्योंकि CAN शारीरिक क्षमता दिखाता है, जबकि MAY अनुमति दिखाता है!",
                "body_gu": "જ્યારે વિદ્યાર્થી પૂછે 'Can I go to the bathroom?', ત્યારે શિક્ષક કહે છે: 'You CAN, but you MAY not!' શા માટે? કારણ કે CAN ક્ષમતા દર્શાવે છે, જ્યારે MAY રજા કે પરવાનગી દર્શાવે છે!"
            },
            {
                "id": "KOBJ_C9_ENG_G2_B2",
                "type": "theory",
                "title": "Core Modal Verbs Chart",
                "title_hi": "मुख्य मोडल वर्ब्स चार्ट",
                "title_gu": "મુખ્ય મોડલ વર્બ્સ ચાર્ટ",
                "body": "• CAN / COULD: Ability, Polite Request (e.g. Could you help me?)\n• MAY / MIGHT: Permission, Possibility (e.g. It might rain today)\n• MUST / HAVE TO: Strong Obligation, Necessity (e.g. You must wear a helmet)\n• SHOULD / OUGHT TO: Advice, Duty (e.g. You should study daily)\n• SHALL / WILL: Future Intent, Promise, Command",
                "body_hi": "• CAN / COULD: क्षमता, विनम्र अनुरोध (जैसे Could you help me?)\n• MAY / MIGHT: अनुमति, संभावना (जैसे It might rain today)\n• MUST / HAVE TO: मजबूत दायित्व, आवश्यकता (जैसे You must wear a helmet)\n• SHOULD / OUGHT TO: सलाह, कर्तव्य (जैसे You should study daily)\n• SHALL / WILL: भविष्य का इरादा, वादा",
                "body_gu": "• CAN / COULD: ક્ષમતા, નમ્ર વિનંતી (દા.ત. Could you help me?)\n• MAY / MIGHT: પરવાનગી, શક્યતા (દા.ત. It might rain today)\n• MUST / HAVE TO: મજબૂત ફરજ, જરૂરિયાત (દા.ત. You must wear a helmet)\n• SHOULD / OUGHT TO: સલાહ, નૈતિક ફરજ (દા.ત. You should study daily)\n• SHALL / WILL: ભવિષ્યનો ઈરાદો, વચન"
            },
            {
                "id": "KOBJ_C9_ENG_G2_B3",
                "type": "quiz",
                "question": "Which modal verb best expresses a moral duty? 'We ______ respect our elders.'",
                "question_hi": "कौन सा मोडल वर्ब नैतिक कर्तव्य को व्यक्त करता है? 'We ______ respect our elders.'",
                "question_gu": "કયો મોડલ વર્બ નૈતિક ફરજ દર્શાવે છે? 'We ______ respect our elders.'",
                "options": [
                    "ought to",
                    "might",
                    "could",
                    "would"
                ],
                "options_hi": [
                    "ought to",
                    "might",
                    "could",
                    "would"
                ],
                "options_gu": [
                    "ought to",
                    "might",
                    "could",
                    "would"
                ],
                "correct_index": 0,
                "explanation": "'Ought to' expresses moral obligation or duty.",
                "explanation_hi": "'Ought to' नैतिक दायित्व या कर्तव्य को व्यक्त करता है।",
                "explanation_gu": "'Ought to' નૈતિક ફરજ અથવા જવાબદારી વ્યક્ત કરે છે."
            }
        ]
    },
    {
        "id": "ncert_class9_grammar_ch3",
        "title": "Subject-Verb Agreement — Harmony in Grammar",
        "title_hi": "कर्ता-क्रिया संगति (Subject-Verb Agreement)",
        "title_gu": "કર્તા-ક્રિયા સંબંધ (Subject-Verb Agreement)",
        "class_num": 9,
        "ch_num": 3,
        "blocks": [
            {
                "id": "KOBJ_C9_ENG_G3_B1",
                "type": "hook",
                "title": "Singular Subject, Singular Verb",
                "title_hi": "एकवचन कर्ता, एकवचन क्रिया",
                "title_gu": "એકવચન કર્તા, એકવચન ક્રિયાપદ",
                "body": "A singular subject takes a singular verb, while a plural subject takes a plural verb. Sounds simple? But what happens when the subject is 'Neither of the boys'?",
                "body_hi": "एकवचन कर्ता के साथ एकवचन क्रिया होती है, जबकि बहुवचन कर्ता के साथ बहुवचन क्रिया होती है। क्या यह आसान लगता है? लेकिन तब क्या होता है जब कर्ता 'Neither of the boys' हो?",
                "body_gu": "એકવચન કર્તા સાથે એકવચન ક્રિયાપદ અને બહુવચન કર્તા સાથે બહુવચન ક્રિયાપદ આવે. પણ જ્યારે કર્તા 'Neither of the boys' હોય ત્યારે શું કરવું?"
            },
            {
                "id": "KOBJ_C9_ENG_G3_B2",
                "type": "theory",
                "title": "Golden Rules of Agreement",
                "title_hi": "संगति के स्वर्ण नियम",
                "title_gu": "સંમતિના સુવર્ણ નિયમો",
                "body": "1. Words joined by 'and' take a plural verb (e.g., Bread and butter ARE essential — UNLESS treated as one unit, then IS).\n2. 'Either...or' / 'Neither...nor': The verb agrees with the CLOSER subject.\n3. Indefinite pronouns like 'each', 'everyone', 'nobody', 'neither' take a SINGULAR verb.\n4. Collective nouns (team, committee) take singular when acting as one body.",
                "body_hi": "1. 'and' से जुड़े शब्द बहुवचन क्रिया लेते हैं (जैसे, Bread and butter IS my favorite breakfast — जब एक इकाई माना जाए)।\n2. 'Either...or' / 'Neither...nor': क्रिया निकटतम कर्ता के अनुसार होती है।\n3. 'each', 'everyone', 'nobody', 'neither' जैसे अनिश्चित सर्वनाम एकवचन क्रिया लेते हैं।\n4. समूहवाचक संज्ञाएं (टीम, समिति) एकवचन क्रिया लेती हैं जब वे एक इकाई के रूप में कार्य करती हैं।",
                "body_gu": "1. 'and' થી જોડાતા શબ્દો બહુવચન ક્રિયાપદ લે છે.\n2. 'Either...or' / 'Neither...nor': ક્રિયાપદ નજીકના કર્તા મુજબ મુકાય છે.\n3. 'each', 'everyone', 'nobody', 'neither' જેવા સર્વનામ એકવચન ક્રિયાપદ લે છે.\n4. સમૂહવાચક સંજ્ઞા (ટીમ, સમિતિ) એકમ તરીકે વર્તે ત્યારે એકવચન ક્રિયાપદ લે છે."
            },
            {
                "id": "KOBJ_C9_ENG_G3_B3",
                "type": "quiz",
                "question": "Choose the correct verb: 'Neither the teacher nor the students ______ present.'",
                "question_hi": "सही क्रिया चुनें: 'Neither the teacher nor the students ______ present.'",
                "question_gu": "સાચું ક્રિયાપદ પસંદ કરો: 'Neither the teacher nor the students ______ present.'",
                "options": [
                    "were",
                    "was",
                    "is",
                    "has"
                ],
                "options_hi": [
                    "were",
                    "was",
                    "is",
                    "has"
                ],
                "options_gu": [
                    "were",
                    "was",
                    "is",
                    "has"
                ],
                "correct_index": 0,
                "explanation": "With 'Neither...nor', the verb agrees with the closer subject ('students', which is plural), so 'were' is correct.",
                "explanation_hi": "'Neither...nor' में, क्रिया निकटतम कर्ता ('students', जो बहुवचन है) के अनुसार होती है, इसलिए 'were' सही है।",
                "explanation_gu": "'Neither...nor' માં ક્રિયાપદ નજીકના કર્તા ('students' - બહુવચન) પ્રમાણે આવે, તેથી 'were' સાચું છે."
            }
        ]
    },
    {
        "id": "ncert_class9_grammar_ch4",
        "title": "Reported Speech — Direct & Indirect",
        "title_hi": "अप्रत्यक्ष कथन (Reported Speech)",
        "title_gu": "પરોક્ષ કથન (Reported Speech)",
        "class_num": 9,
        "ch_num": 4,
        "blocks": [
            {
                "id": "KOBJ_C9_ENG_G4_B1",
                "type": "hook",
                "title": "The Secrets of Reporting",
                "title_hi": "कथन के रहस्य",
                "title_gu": "કથનના રહસ્યો",
                "body": "Direct Speech quotes exact words in quotes ('I am happy'). Indirect Speech reports what someone said without exact quotes ('He said that he was happy'). Notice how the tense shifts back!",
                "body_hi": "Direct Speech उद्धरण चिह्नों में सटीक शब्दों को उद्धृत करता है ('I am happy')। Indirect Speech बिना सटीक उद्धरण के बताता है कि किसी ने क्या कहा ('He said that he was happy')। ध्यान दें कि काल कैसे बदलता है!",
                "body_gu": "Direct Speech મૂળ શબ્દો દર્શાવે છે ('I am happy'). Indirect Speech બીજાના કથનને પોતાના શબ્દોમાં રજૂ કરે છે ('He said that he was happy'). કાળ કેવી રીતે પાછળ ખસે છે તે જુઓ!"
            },
            {
                "id": "KOBJ_C9_ENG_G4_B2",
                "type": "theory",
                "title": "Tense Shift Rules in Reported Speech",
                "title_hi": "रिपोर्टेड स्पीच में काल परिवर्तन के नियम",
                "title_gu": "રિપોર્ટેડ સ્પીચમાં કાળ બદલવાના નિયમો",
                "body": "• Simple Present → Simple Past (is → was, eat → ate)\n• Present Continuous → Past Continuous (am eating → was eating)\n• Present Perfect → Past Perfect (has eaten → had eaten)\n• Simple Past → Past Perfect (ate → had eaten)\n• Will → Would, Can → Could, May → Might\n• Time words shift: now → then, today → that day, tomorrow → the next day",
                "body_hi": "• Simple Present → Simple Past (is → was, eat → ate)\n• Present Continuous → Past Continuous (am eating → was eating)\n• Present Perfect → Past Perfect (has eaten → had eaten)\n• Simple Past → Past Perfect (ate → had eaten)\n• Will → Would, Can → Could, May → Might\n• समय सूचक शब्द बदलते हैं: now → then, today → that day, tomorrow → the next day",
                "body_gu": "• Simple Present → Simple Past (is → was, eat → ate)\n• Present Continuous → Past Continuous (am eating → was eating)\n• Present Perfect → Past Perfect (has eaten → had eaten)\n• Simple Past → Past Perfect (ate → had eaten)\n• Will → Would, Can → Could, May → Might\n• સમયસૂચક શબ્દો: now → then, today → that day, tomorrow → the next day"
            },
            {
                "id": "KOBJ_C9_ENG_G4_B3",
                "type": "quiz",
                "question": "Convert to Indirect: Rohan said, 'I will call you tomorrow.'",
                "question_hi": "Indirect में बदलें: Rohan said, 'I will call you tomorrow.'",
                "question_gu": "Indirect માં ફેરવો: Rohan said, 'I will call you tomorrow.'",
                "options": [
                    "Rohan said that he would call me the next day.",
                    "Rohan said that I will call him tomorrow.",
                    "Rohan told that he will call me tomorrow.",
                    "Rohan says he would call tomorrow."
                ],
                "options_hi": [
                    "Rohan said that he would call me the next day.",
                    "Rohan said that I will call him tomorrow.",
                    "Rohan told that he will call me tomorrow.",
                    "Rohan says he would call tomorrow."
                ],
                "options_gu": [
                    "Rohan said that he would call me the next day.",
                    "Rohan said that I will call him tomorrow.",
                    "Rohan told that he will call me tomorrow.",
                    "Rohan says he would call tomorrow."
                ],
                "correct_index": 0,
                "explanation": "'will' changes to 'would', and 'tomorrow' changes to 'the next day'.",
                "explanation_hi": "'will' बदलकर 'would' हो जाता है, और 'tomorrow' बदलकर 'the next day' हो जाता है।",
                "explanation_gu": "'will' નું 'would' થાય અને 'tomorrow' નું 'the next day' થાય."
            }
        ]
    },
    {
        "id": "ncert_class9_grammar_ch5",
        "title": "Active & Passive Voice",
        "title_hi": "कर्तृवाच्य और कर्मवाच्य (Active & Passive Voice)",
        "title_gu": "કર્મણિ અને કર્તરી પ્રયોગ (Active & Passive Voice)",
        "class_num": 9,
        "ch_num": 5,
        "blocks": [
            {
                "id": "KOBJ_C9_ENG_G5_B1",
                "type": "hook",
                "title": "Who Did It vs What Was Done",
                "title_hi": "किसने किया बनाम क्या किया गया",
                "title_gu": "કોણે કર્યું વિરૂદ્ધ શું કરવામાં આવ્યું",
                "body": "Active Voice focuses on the DOER ('The dog bit the man'). Passive Voice focuses on the RECEIVER of the action ('The man was bitten by the dog'). Passive is used when the doer is unknown or less important.",
                "body_hi": "Active Voice करने वाले पर ध्यान केंद्रित करता है ('The dog bit the man')। Passive Voice क्रिया प्राप्तकर्ता पर ध्यान केंद्रित करता है ('The man was bitten by the dog')। Passive का उपयोग तब किया जाता है जब करने वाला अज्ञात या कम महत्वपूर्ण हो।",
                "body_gu": "Active Voice ક્રિયા કરનાર પર ભાર મૂકે છે ('The dog bit the man'). Passive Voice ક્રિયાના ભોગ બનનાર પર ભાર મૂકે છે ('The man was bitten by the dog')."
            },
            {
                "id": "KOBJ_C9_ENG_G5_B2",
                "type": "theory",
                "title": "Passive Voice Formula",
                "title_hi": "पैसिव वॉइस का सूत्र",
                "title_gu": "પેસિવ વોઇસનું સૂત્ર",
                "body": "Object + Helping Verb (be) + V3 (Past Participle) + by + Subject\n\nExamples:\n• Simple Present: 'She bakes a cake' → 'A cake is baked by her'\n• Simple Past: 'They built a house' → 'A house was built by them'\n• Present Continuous: 'He is driving a car' → 'A car is being driven by him'",
                "body_hi": "कर्म + सहायक क्रिया (be) + V3 (भूतकालिक कृदंत) + by + कर्ता\n\nउदाहरण:\n• Simple Present: 'She bakes a cake' → 'A cake is baked by her'\n• Simple Past: 'They built a house' → 'A house was built by them'\n• Present Continuous: 'He is driving a car' → 'A car is being driven by him'",
                "body_gu": "કર્મ + સહાયક ક્રિયાપદ (be) + V3 + by + કર્તા\n\nઉદાહરણ:\n• Simple Present: 'She bakes a cake' → 'A cake is baked by her'\n• Simple Past: 'They built a house' → 'A house was built by them'\n• Present Continuous: 'He is driving a car' → 'A car is being driven by him'"
            },
            {
                "id": "KOBJ_C9_ENG_G5_B3",
                "type": "quiz",
                "question": "Change to Passive: 'The chef prepared a delicious meal.'",
                "question_hi": "Passive में बदलें: 'The chef prepared a delicious meal.'",
                "question_gu": "Passive માં ફેરવો: 'The chef prepared a delicious meal.'",
                "options": [
                    "A delicious meal was prepared by the chef.",
                    "A delicious meal is prepared by the chef.",
                    "A delicious meal had prepared by the chef.",
                    "A delicious meal has been prepared by the chef."
                ],
                "options_hi": [
                    "A delicious meal was prepared by the chef.",
                    "A delicious meal is prepared by the chef.",
                    "A delicious meal had prepared by the chef.",
                    "A delicious meal has been prepared by the chef."
                ],
                "options_gu": [
                    "A delicious meal was prepared by the chef.",
                    "A delicious meal is prepared by the chef.",
                    "A delicious meal had prepared by the chef.",
                    "A delicious meal has been prepared by the chef."
                ],
                "correct_index": 0,
                "explanation": "Simple Past ('prepared') changes to 'was prepared' in Passive Voice.",
                "explanation_hi": "Simple Past ('prepared') Passive Voice में बदलकर 'was prepared' हो जाता है।",
                "explanation_gu": "સાદો ભૂતકાળ ('prepared') પેસિવમાં 'was prepared' બને છે."
            }
        ]
    },
    {
        "id": "ncert_class9_grammar_ch6",
        "title": "Determiners — Articles, Quantifiers & Demonstratives",
        "title_hi": "डिटरमाइनर्स — आर्टिकल्स, परिमाणवाचक और संकेतवाचक",
        "title_gu": "ડિટરમાઇનર્સ — આર્ટિકલ્સ, પરિમાણવાચક અને દર્શક",
        "class_num": 9,
        "ch_num": 6,
        "blocks": [
            {
                "id": "KOBJ_C9_ENG_G6_B1",
                "type": "hook",
                "title": "A, An, The & Quantifiers",
                "title_hi": "A, An, The और परिमाणवाचक",
                "title_gu": "A, An, The અને પરિમાણવાચક",
                "body": "Determiners introduce nouns and state their quantity or specificity. Compare 'a few friends' vs 'few friends'—adding 'a' completely changes the meaning from positive to negative!",
                "body_hi": "डिटरमाइनर्स संज्ञाओं का परिचय देते हैं और उनकी मात्रा या विशिष्टता बताते हैं। 'a few friends' की तुलना 'few friends' से करें—'a' जोड़ने से अर्थ सकारात्मक से नकारात्मक में बदल जाता है!",
                "body_gu": "ડિટરમાઇનર્સ સંજ્ઞા આગળ આવી તેની સંખ્યા કે ચોક્કસતા દર્શાવે છે. 'a few friends' અને 'few friends' વચ્ચે મોટો તફાવત છે!"
            },
            {
                "id": "KOBJ_C9_ENG_G6_B2",
                "type": "theory",
                "title": "Types of Determiners",
                "title_hi": "डिटरमाइनर्स के प्रकार",
                "title_gu": "ડિટરમાઇનર્સના પ્રકાર",
                "body": "1. Articles: Indefinite (a, an - sound-based), Definite (the - unique/specific)\n2. Demonstratives: this, that, these, those\n3. Possessives: my, your, his, her, its, our, their\n4. Quantifiers: much (uncountable), many (countable), some, any, little, few, each, every",
                "body_hi": "1. आर्टिकल्स: अनिश्चित (a, an - ध्वनि आधारित), निश्चित (the - अद्वितीय/विशिष्ट)\n2. संकेतवाचक: this, that, these, those\n3. संबंधवाचक: my, your, his, her, its, our, their\n4. परिमाणवाचक: much (अगणनीय), many (गणनीय), some, any, little, few, each, every",
                "body_gu": "1. આર્ટિકલ્સ: અનિશ્ચિત (a, an), નિશ્ચિત (the)\n2. દર્શક: this, that, these, those\n3. માલિકીદર્શક: my, your, his, her, its, our, their\n4. જથ્થાવાચક: much, many, some, any, little, few, each, every"
            },
            {
                "id": "KOBJ_C9_ENG_G6_B3",
                "type": "quiz",
                "question": "Fill in the blank: 'There is ______ water left in the jug, so we cannot make tea.'",
                "question_hi": "रिक्त स्थान भरें: 'There is ______ water left in the jug, so we cannot make tea.'",
                "question_gu": "ખાલી જગ્યા પૂરો: 'There is ______ water left in the jug, so we cannot make tea.'",
                "options": [
                    "little",
                    "a little",
                    "few",
                    "many"
                ],
                "options_hi": [
                    "little",
                    "a little",
                    "few",
                    "many"
                ],
                "options_gu": [
                    "little",
                    "a little",
                    "few",
                    "many"
                ],
                "correct_index": 0,
                "explanation": "'Little' means almost none (negative) and is used with uncountable nouns like water.",
                "explanation_hi": "'Little' का अर्थ है लगभग कुछ नहीं (नकारात्मक) और इसका उपयोग पानी जैसे अगणनीय संज्ञाओं के साथ किया जाता है।",
                "explanation_gu": "'Little' એટલે નહિવત (નકારાત્મક) અને તે પાણી જેવા અગણ્ય દ્રવ્ય સાથે વપરાય."
            }
        ]
    },
    {
        "id": "ncert_class9_grammar_ch7",
        "title": "Prepositions — Time, Place & Direction",
        "title_hi": "संबंधबोधक अव्यय (Prepositions)",
        "title_gu": "નામયોગી અવ્યય (Prepositions)",
        "class_num": 9,
        "ch_num": 7,
        "blocks": [
            {
                "id": "KOBJ_C9_ENG_G7_B1",
                "type": "hook",
                "title": "Positioning Everything Correctly",
                "title_hi": "सब कुछ सही स्थिति में रखना",
                "title_gu": "દરેક વસ્તુને યોગ્ય સ્થાન આપવું",
                "body": "Prepositions link nouns/pronouns to other words. 'In the bus' vs 'On the bus' vs 'At the bus stop'—using the wrong preposition completely changes the spatial context!",
                "body_hi": "Prepositions संज्ञाओं/सर्वनामों को अन्य शब्दों से जोड़ते हैं। 'In the bus' बनाम 'On the bus' बनाम 'At the bus stop'—गलत preposition का उपयोग स्थान के संदर्भ को पूरी तरह से बदल देता है!",
                "body_gu": "Prepositions શબ્દો વચ્ચેનું સ્થળ, સમય કે દિશાનું સ્થાન દર્શાવે છે."
            },
            {
                "id": "KOBJ_C9_ENG_G7_B2",
                "type": "theory",
                "title": "Key Preposition Categories",
                "title_hi": "प्रमुख Preposition श्रेणियां",
                "title_gu": "મુખ્ય Preposition વર્ગીકરણ",
                "body": "• Time: AT (precise time: at 5 PM), ON (days/dates: on Monday), IN (months/years: in July)\n• Place: AT (specific point), IN (enclosed space/city), ON (surface)\n• Direction: INTO (movement inside), ONTO (movement onto surface), TOWARDS (in direction of)\n• Complex: in spite of, according to, on behalf of, due to",
                "body_hi": "• समय: AT (सटीक समय), ON (दिन/तिथि), IN (महीने/वर्ष)\n• स्थान: AT (विशिष्ट बिंदु), IN (बंद स्थान/शहर), ON (सतह)\n• दिशा: INTO (भीतर गति), ONTO (सतह पर गति), TOWARDS (दिशा में)\n• जटिल: in spite of, according to, on behalf of, due to",
                "body_gu": "• સમય: AT (ચોક્કસ સમય), ON (વાર/તારીખ), IN (મહિના/વર્ષ)\n• સ્થળ: AT (ચોક્કસ સ્થળ), IN (અંદર/શહેર), ON (સપાટી પર)\n• દિશા: INTO (અંદર જવું), ONTO (ઉપર જવું), TOWARDS (તરફ)"
            },
            {
                "id": "KOBJ_C9_ENG_G7_B3",
                "type": "quiz",
                "question": "Choose the correct preposition: 'The cat jumped ______ the swimming pool.'",
                "question_hi": "सही preposition चुनें: 'The cat jumped ______ the swimming pool.'",
                "question_gu": "સાચું preposition પસંદ કરો: 'The cat jumped ______ the swimming pool.'",
                "options": [
                    "into",
                    "in",
                    "on",
                    "at"
                ],
                "options_hi": [
                    "into",
                    "in",
                    "on",
                    "at"
                ],
                "options_gu": [
                    "into",
                    "in",
                    "on",
                    "at"
                ],
                "correct_index": 0,
                "explanation": "'Into' indicates movement entering an enclosed space or liquid.",
                "explanation_hi": "'Into' किसी बंद स्थान या तरल में प्रवेश करने की गति को दर्शाता है।",
                "explanation_gu": "'Into' ગતિ સાથે અંદર પ્રવેશ દર્શાવે છે."
            }
        ]
    },
    {
        "id": "ncert_class9_grammar_ch8",
        "title": "Conjunctions — Connecting Ideas",
        "title_hi": "समुच्चयबोधक (Conjunctions)",
        "title_gu": "સંયોજકો (Conjunctions)",
        "class_num": 9,
        "ch_num": 8,
        "blocks": [
            {
                "id": "KOBJ_C9_ENG_G8_B1",
                "type": "hook",
                "title": "The Bridges of Grammar",
                "title_hi": "व्याकरण के पुल",
                "title_gu": "વ્યાકરણના સેતુઓ",
                "body": "Without conjunctions, we would speak in short, choppy sentences: 'I wanted to play. It started raining. I stayed inside.' Conjunctions join these into smooth ideas: 'I wanted to play, BUT it started raining, SO I stayed inside.'",
                "body_hi": "समुच्चयबोधक के बिना, हम छोटे, टूटे हुए वाक्यों में बोलेंगे। समुच्चयबोधक इन्हें सुचारू विचारों में जोड़ते हैं!",
                "body_gu": "સંયોજકો (Conjunctions) વાક્યો કે વિચારોને એકબીજા સાથે જોડે છે."
            },
            {
                "id": "KOBJ_C9_ENG_G8_B2",
                "type": "theory",
                "title": "Types of Conjunctions (FANBOYS & Beyond)",
                "title_hi": "समुच्चयबोधक के प्रकार",
                "title_gu": "સંયોજકોના પ્રકાર",
                "body": "1. Coordinating: FANBOYS (For, And, Nor, But, Or, Yet, So)\n2. Subordinating: because, although, since, unless, while, whereas, as soon as\n3. Correlative (Pairs): either...or, neither...nor, not only...but also, scarcely...when",
                "body_hi": "1. समानपदीय: FANBOYS (For, And, Nor, But, Or, Yet, So)\n2. आश्रित: because, although, since, unless, while, whereas, as soon as\n3. युग्म: either...or, neither...nor, not only...but also, scarcely...when",
                "body_gu": "1. સમાનપદી: FANBOYS (For, And, Nor, But, Or, Yet, So)\n2. ગૌણપદી: because, although, since, unless, while, whereas\n3. જોડમાં વપરાતા: either...or, neither...nor, not only...but also"
            },
            {
                "id": "KOBJ_C9_ENG_G8_B3",
                "type": "quiz",
                "question": "Fill in the blank: 'Work hard, ______ you will fail the examination.'",
                "question_hi": "रिक्त स्थान भरें: 'Work hard, ______ you will fail the examination.'",
                "question_gu": "ખાલી જગ્યા પૂરો: 'Work hard, ______ you will fail the examination.'",
                "options": [
                    "otherwise",
                    "because",
                    "and",
                    "since"
                ],
                "options_hi": [
                    "otherwise",
                    "because",
                    "and",
                    "since"
                ],
                "options_gu": [
                    "otherwise",
                    "because",
                    "and",
                    "since"
                ],
                "correct_index": 0,
                "explanation": "'Otherwise' shows the condition/consequence if the advice is not followed.",
                "explanation_hi": "'Otherwise' (अन्यथा) सलाह न मानने पर परिणाम को दर्शाता है।",
                "explanation_gu": "'Otherwise' (નહિતર) જો સલાહ ન પાળવામાં આવે તો શું થશે તે પરિણામ દર્શાવે છે."
            }
        ]
    },
    {
        "id": "ncert_class9_grammar_ch9",
        "title": "Clauses — Noun, Adjective & Adverb Clauses",
        "title_hi": "उपवाक्य (Clauses)",
        "title_gu": "ઉપવાક્યો (Clauses)",
        "class_num": 9,
        "ch_num": 9,
        "blocks": [
            {
                "id": "KOBJ_C9_ENG_G9_B1",
                "type": "hook",
                "title": "What is a Clause?",
                "title_hi": "उपवाक्य क्या है?",
                "title_gu": "ક્લોઝ (ઉપવાક્ય) શું છે?",
                "body": "A clause is a group of words containing a Subject and a Predicate. Independent clauses can stand alone as a sentence, while Dependent clauses rely on the main clause to complete their meaning.",
                "body_hi": "एक उपवाक्य शब्दों का एक समूह है जिसमें कर्ता और विधेय होता है। स्वतंत्र उपवाक्य अकेले एक वाक्य के रूप में खड़े हो सकते हैं, जबकि आश्रित उपवाक्य अपने अर्थ को पूरा करने के लिए मुख्य उपवाक्य पर निर्भर करते हैं।",
                "body_gu": "ક્લોઝ એ શબ્દોનો સમૂહ છે જેમાં કર્તા અને ક્રિયાપદ હોય છે."
            },
            {
                "id": "KOBJ_C9_ENG_G9_B2",
                "type": "theory",
                "title": "Three Main Dependent Clauses",
                "title_hi": "तीन मुख्य आश्रित उपवाक्य",
                "title_gu": "ત્રણ મુખ્ય ગૌણ ઉપવાક્યો",
                "body": "1. Noun Clause: Acts as a noun (e.g., 'I know THAT YOU ARE HONEST')\n2. Adjective (Relative) Clause: Modifies a noun (e.g., 'The boy WHO WON THE PRIZE is my brother')\n3. Adverb Clause: Modifies a verb/adjective (e.g., 'She wept BECAUSE SHE LOST HER PEN')",
                "body_hi": "1. संज्ञा उपवाक्य: संज्ञा के रूप में कार्य करता है (जैसे, 'I know THAT YOU ARE HONEST')\n2. विशेषण उपवाक्य: संज्ञा की विशेषता बताता है (जैसे, 'The boy WHO WON THE PRIZE is my brother')\n3. क्रियाविशेषण उपवाक्य: क्रिया/विशेषण की विशेषता बताता है (जैसे, 'She wept BECAUSE SHE LOST HER PEN')",
                "body_gu": "1. નામ ઉપવાક્ય (Noun Clause): નામ તરીકે કાર્ય કરે છે.\n2. વિશેષણ ઉપવાક્ય (Adjective Clause): નામના અર્થમાં વધારો કરે છે.\n3. ક્રિયાબિન વિશેષણ ઉપવાક્ય (Adverb Clause): ક્રિયાપદના અર્થમાં વધારો કરે છે."
            },
            {
                "id": "KOBJ_C9_ENG_G9_B3",
                "type": "quiz",
                "question": "Identify the underlined clause: 'The house THAT JACK BUILT is very big.'",
                "question_hi": "रेखांकित उपवाक्य की पहचान करें: 'The house THAT JACK BUILT is very big.'",
                "question_gu": "અધોરેખિત ઉપવાક્ય ઓળખો: 'The house THAT JACK BUILT is very big.'",
                "options": [
                    "Adjective Clause",
                    "Noun Clause",
                    "Adverb Clause",
                    "Independent Clause"
                ],
                "options_hi": [
                    "Adjective Clause",
                    "Noun Clause",
                    "Adverb Clause",
                    "Independent Clause"
                ],
                "options_gu": [
                    "Adjective Clause",
                    "Noun Clause",
                    "Adverb Clause",
                    "Independent Clause"
                ],
                "correct_index": 0,
                "explanation": "'THAT JACK BUILT' modifies the noun 'house', making it an Adjective (Relative) Clause.",
                "explanation_hi": "'THAT JACK BUILT' संज्ञा 'house' की विशेषता बताता है, इसलिए यह Adjective Clause है।",
                "explanation_gu": "'THAT JACK BUILT' એ 'house' નામના અર્થમાં વધારો કરે છે, તેથી તે Adjective Clause છે."
            }
        ]
    },
    {
        "id": "ncert_class9_grammar_ch10",
        "title": "Sentence Transformation — Simple, Compound & Complex",
        "title_hi": "वाक्य रूपांतरण — सरल, संयुक्त और मिश्र",
        "title_gu": "વાક્ય રૂપાંતરણ — સાદું, સંયુક્ત અને મિશ્ર",
        "class_num": 9,
        "ch_num": 10,
        "blocks": [
            {
                "id": "KOBJ_C9_ENG_G10_B1",
                "type": "hook",
                "title": "Same Meaning, Different Structure",
                "title_hi": "समान अर्थ, विभिन्न संरचना",
                "title_gu": "સમાન અર્થ, વિવિધ માળખું",
                "body": "Sentence transformation means changing the grammatical structure of a sentence without altering its original meaning!",
                "body_hi": "वाक्य रूपांतरण का अर्थ वाक्य के मूल अर्थ को बदले बिना उसकी व्याकरणिक संरचना को बदलना है!",
                "body_gu": "વાક્ય રૂપાંતરણ એટલે અર્થ બદલ્યા વગર વાક્યનું વ્યાકરણિક માળખું બદલવું!"
            },
            {
                "id": "KOBJ_C9_ENG_G10_B2",
                "type": "theory",
                "title": "Sentence Structures Explained",
                "title_hi": "वाक्य संरचनाएं स्पष्ट की गईं",
                "title_gu": "વાક્ય રચનાઓ સમજો",
                "body": "• Simple: One independent clause (e.g. 'In spite of his poverty, he is honest')\n• Compound: Two independent clauses joined by coordinating conjunction (e.g. 'He is poor, BUT he is honest')\n• Complex: One main clause + one or more dependent clauses (e.g. 'ALTHOUGH he is poor, he is honest')",
                "body_hi": "• सरल: एक स्वतंत्र उपवाक्य (उदा. 'In spite of his poverty, he is honest')\n• संयुक्त: समानपदीय संयोजक द्वारा जुड़े दो स्वतंत्र उपवाक्य (उदा. 'He is poor, BUT he is honest')\n• मिश्र: एक मुख्य उपवाक्य + एक या अधिक आश्रित उपवाक्य (उदा. 'ALTHOUGH he is poor, he is honest')",
                "body_gu": "• સાદું (Simple): એક જ સ્વતંત્ર વાક્ય\n• સંયુક્ત (Compound): બે સ્વતંત્ર વાક્યો સંયોજકથી જોડાયેલા\n• મિશ્ર (Complex): એક મુખ્ય વાક્ય + ગૌણ વાક્ય"
            },
            {
                "id": "KOBJ_C9_ENG_G10_B3",
                "type": "quiz",
                "question": "Transform to Complex: 'He heard the news and fainted.'",
                "question_hi": "Complex में बदलें: 'He heard the news and fainted.'",
                "question_gu": "Complex માં ફેરવો: 'He heard the news and fainted.'",
                "options": [
                    "As soon as he heard the news, he fainted.",
                    "Hearing the news he fainted.",
                    "He fainted because of the news.",
                    "He heard news so he fainted."
                ],
                "options_hi": [
                    "As soon as he heard the news, he fainted.",
                    "Hearing the news he fainted.",
                    "He fainted because of the news.",
                    "He heard news so he fainted."
                ],
                "options_gu": [
                    "As soon as he heard the news, he fainted.",
                    "Hearing the news he fainted.",
                    "He fainted because of the news.",
                    "He heard news so he fainted."
                ],
                "correct_index": 0,
                "explanation": "'As soon as he heard the news' creates a dependent clause, making the sentence Complex.",
                "explanation_hi": "'As soon as he heard the news' एक आश्रित उपवाक्य बनाता है, जिससे वाक्य मिश्र (Complex) बन जाता है।",
                "explanation_gu": "'As soon as he heard the news' એ ગૌણ વાક્ય બનાવે છે જેથી આ Complex વાક્ય બને છે."
            }
        ]
    },

    # ------------------------------------------------------------
    # CLASS 10 GRAMMAR (CHAPTERS 1 - 10)
    # ------------------------------------------------------------
    {
        "id": "ncert_class10_grammar_ch1",
        "title": "Tenses — Board Pattern Review & Advanced Rules",
        "title_hi": "काल — बोर्ड पैटर्न समीक्षा और उन्नत नियम",
        "title_gu": "કાળ — બોર્ડ પેટર્ન સમીક્ષા અને એડવાન્સ નિયમો",
        "class_num": 10,
        "ch_num": 1,
        "blocks": [
            {
                "id": "KOBJ_C10_ENG_G1_B1",
                "type": "hook",
                "title": "Board Exam Secret: Context-Based Tenses",
                "title_hi": "बोर्ड परीक्षा रहस्य: संदर्भ-आधारित काल",
                "title_gu": "બોર્ડ પરીક્ષાનું રહસ્ય: સંદર્ભ-આધારિત કાળ",
                "body": "Class 10 Board exams do not test isolated tense rules. They test how tenses interact within paragraphs! A shift from past to present mid-paragraph can lose you valuable marks.",
                "body_hi": "कक्षा 10 बोर्ड परीक्षाएं अलग-अलग काल के नियमों का परीक्षण नहीं करती हैं। वे परीक्षण करते हैं कि पैराग्राफ के भीतर काल कैसे परस्पर क्रिया करते हैं!",
                "body_gu": "ધોરણ 10 બોર્ડ પરીક્ષામાં ફકરાના સંદર્ભમાં કાળનો ઉપયોગ ચકાસવામાં આવે છે."
            },
            {
                "id": "KOBJ_C10_ENG_G1_B2",
                "type": "theory",
                "title": "Advanced Tense Harmony Rules",
                "title_hi": "उन्नत काल सामंजस्य नियम",
                "title_gu": "એડવાન્સ કાળ સંમતિના નિયમો",
                "body": "1. Past Action before another Past Action: First action takes Past Perfect ('had + V3'), second takes Simple Past ('V2').\n2. Time Clauses (when, after, before, as soon as): Present tense in time clause = Future tense in main clause.\n3. Universal Truths: Never change to past tense even if reporting verb is past.",
                "body_hi": "1. किसी अन्य भूतकाल की क्रिया से पहले की भूतकाल की क्रिया: पहली क्रिया में Past Perfect ('had + V3') और दूसरी में Simple Past ('V2') होता है।\n2. समय उपवाक्य: समय उपवाक्य में वर्तमान काल = मुख्य उपवाक्य में भविष्य काल।\n3. सार्वभौमिक सत्य: रिपोर्टिंग वर्ब भूतकाल होने पर भी कभी भूतकाल में नहीं बदलते।",
                "body_gu": "1. ભૂતકાળની પ્રથમ ક્રિયા: Past Perfect ('had + V3'), બીજી ક્રિયા: Simple Past ('V2').\n2. સનાતન સત્ય: રિપોર્ટિંગ વર્બ ભૂતકાળ હોય તો પણ વર્તમાનકાળ જ રહે."
            },
            {
                "id": "KOBJ_C10_ENG_G1_B3",
                "type": "quiz",
                "question": "Complete the sentence: 'The train ______ (leave) the station before we arrived.'",
                "question_hi": "वाक्य पूरा करें: 'The train ______ (leave) the station before we arrived.'",
                "question_gu": "વાક્ય પૂર્ણ કરો: 'The train ______ (leave) the station before we arrived.'",
                "options": [
                    "had left",
                    "left",
                    "was leaving",
                    "has left"
                ],
                "options_hi": [
                    "had left",
                    "left",
                    "was leaving",
                    "has left"
                ],
                "options_gu": [
                    "had left",
                    "left",
                    "was leaving",
                    "has left"
                ],
                "correct_index": 0,
                "explanation": "The train leaving happened FIRST before we arrived in the past, so Past Perfect ('had left') is required.",
                "explanation_hi": "ट्रेन का छूटना अतीत में हमारे पहुँचने से पहले हुआ था, इसलिए Past Perfect ('had left') आवश्यक है।",
                "explanation_gu": "ટ્રેન ઉપડવાની ક્રિયા અમારી પહોંચવાની ક્રિયા પહેલાં થઈ હોવાથી Past Perfect ('had left') આવશે."
            }
        ]
    },
    {
        "id": "ncert_class10_grammar_ch2",
        "title": "Modals — Expressing Nuance, Advice & Probability",
        "title_hi": "मोडल्स — बारीकियाँ, सलाह और संभावना",
        "title_gu": "મોડલ્સ — સલાહ, સંભાવના અને સૂક્ષ્મ અર્થ",
        "class_num": 10,
        "ch_num": 2,
        "blocks": [
            {
                "id": "KOBJ_C10_ENG_G2_B1",
                "type": "hook",
                "title": "Degrees of Possibility",
                "title_hi": "संभावना की डिग्रियां",
                "title_gu": "શક્યતાની માત્રા",
                "body": "Compare: 'It WILL rain' (100%), 'It SHOULD rain' (80%), 'It MAY rain' (50%), 'It MIGHT rain' (20%). Choosing the right modal verb conveys exact degree of confidence.",
                "body_hi": "तुलना करें: 'It WILL rain' (100%), 'It SHOULD rain' (80%), 'It MAY rain' (50%), 'It MIGHT rain' (20%)। सही मोडल वर्ब का चयन आत्मविश्वास की सटीक डिग्री को व्यक्त करता है।",
                "body_gu": "'It WILL rain' (100%), 'It MAY rain' (50%), 'It MIGHT rain' (20%) — યોગ્ય મોડલ વડે ચોક્કસ શક્યતા દર્શાવાય છે."
            },
            {
                "id": "KOBJ_C10_ENG_G2_B2",
                "type": "theory",
                "title": "Modals in Formal & Board Contexts",
                "title_hi": "औपचारिक और बोर्ड संदर्भों में मोडल्स",
                "title_gu": "બોર્ડ સંદર્ભમાં મોડલ્સનો ઉપયોગ",
                "body": "• Must vs Need not: Necessity vs Absence of obligation.\n• Could have / Should have: Unfulfilled past possibility or regret (e.g. 'You should have studied harder').\n• Would: Past habit or polite proposal.",
                "body_hi": "• Must बनाम Need not: आवश्यकता बनाम दायित्व की अनुपस्थिति।\n• Could have / Should have: अधूरी अतीत की संभावना या पछतावा।\n• Would: अतीत की आदत या विनम्र प्रस्ताव।",
                "body_gu": "• Could have / Should have: ભૂતકાળમાં ન થઈ શકેલી ક્રિયા કે પસ્તાવો દર્શાવવા."
            },
            {
                "id": "KOBJ_C10_ENG_G2_B3",
                "type": "quiz",
                "question": "Fill in the blank: 'You ______ have taken an umbrella; it didn't rain at all!'",
                "question_hi": "रिक्त स्थान भरें: 'You ______ have taken an umbrella; it didn't rain at all!'",
                "question_gu": "ખાલી જગ્યા પૂરો: 'You ______ have taken an umbrella; it didn't rain at all!'",
                "options": [
                    "needn't",
                    "mustn't",
                    "shouldn't",
                    "couldn't"
                ],
                "options_hi": [
                    "needn't",
                    "mustn't",
                    "shouldn't",
                    "couldn't"
                ],
                "options_gu": [
                    "needn't",
                    "mustn't",
                    "shouldn't",
                    "couldn't"
                ],
                "correct_index": 0,
                "explanation": "'Needn't have' means an action was done but was unnecessary.",
                "explanation_hi": "'Needn't have' का अर्थ है कि एक क्रिया की गई थी लेकिन वह अनावश्यक थी।",
                "explanation_gu": "'Needn't have' નો અર્થ એ થાય કે ક્રિયા કરવામાં આવી પણ તે બિનજરૂરી હતી."
            }
        ]
    },
    {
        "id": "ncert_class10_grammar_ch3",
        "title": "Subject-Verb Concord — Tricky Exam Patterns",
        "title_hi": "कर्ता-क्रिया मेल (Subject-Verb Concord)",
        "title_gu": "કર્તા-ક્રિયા સંવાદિતા (Subject-Verb Concord)",
        "class_num": 10,
        "ch_num": 3,
        "blocks": [
            {
                "id": "KOBJ_C10_ENG_G3_B1",
                "type": "hook",
                "title": "Tricky Subjects That Fool Examiners",
                "title_hi": "कठिन कर्ता जो परीक्षार्थियों को चकमा देते हैं",
                "title_gu": "બોર્ડ પરીક્ષાના અઘરા કર્તા",
                "body": "'Mathematics IS easy', 'The news IS true', 'Ten miles IS a long distance'—why do these words ending in 's' take singular verbs?",
                "body_hi": "'Mathematics IS easy', 'The news IS true', 'Ten miles IS a long distance'—'s' से समाप्त होने वाले ये शब्द एकवचन क्रिया क्यों लेते हैं?",
                "body_gu": "'Mathematics IS easy', 'The news IS true' — છેડે 's' હોવા છતાં આ એકવચન ક્રિયાપદ કેમ લે છે?"
            },
            {
                "id": "KOBJ_C10_ENG_G3_B2",
                "type": "theory",
                "title": "Advanced Subject-Verb Concord Rules",
                "title_hi": "उन्नत कर्ता-क्रिया मेल नियम",
                "title_gu": "એડવાન્સ કર્તા-ક્રિયા સંવાદિતા નિયમો",
                "body": "1. Plural in form but singular in meaning (Subjects, Diseases, Games): Physics, Measles, Billiards → Singular Verb.\n2. Quantities/Amounts/Distances treated as a whole: '100 rupees is enough'.\n3. 'A number of' = Plural Verb | 'The number of' = Singular Verb!\n4. Subjects connected by 'as well as', 'along with', 'with', 'together with': Verb agrees with the FIRST subject.",
                "body_hi": "1. रूप में बहुवचन लेकिन अर्थ में एकवचन (विषय, बीमारियां): Physics, Measles → एकवचन क्रिया।\n2. मात्रा/दूरी: '100 rupees is enough'।\n3. 'A number of' = बहुवचन क्रिया | 'The number of' = एकवचन क्रिया!\n4. 'as well as', 'along with' से जुड़े कर्ता: क्रिया पहले कर्ता के अनुसार होती है।",
                "body_gu": "1. દેખાવમાં બહુવચન પણ અર્થમાં એકવચન: Physics, News → એકવચન ક્રિયાપદ.\n2. 'A number of' = બહુવચન | 'The number of' = એકવચન!\n3. 'as well as', 'along with' થી જોડાતાં કર્તા: પ્રથમ કર્તા મુજબ ક્રિયાપદ આવે."
            },
            {
                "id": "KOBJ_C10_ENG_G3_B3",
                "type": "quiz",
                "question": "Select the correct verb: 'The Director, along with his assistants, ______ attending the conference.'",
                "question_hi": "सही क्रिया चुनें: 'The Director, along with his assistants, ______ attending the conference.'",
                "question_gu": "સાચું ક્રિયાપદ પસંદ કરો: 'The Director, along with his assistants, ______ attending the conference.'",
                "options": [
                    "is",
                    "are",
                    "were",
                    "have"
                ],
                "options_hi": [
                    "is",
                    "are",
                    "were",
                    "have"
                ],
                "options_gu": [
                    "is",
                    "are",
                    "were",
                    "have"
                ],
                "correct_index": 0,
                "explanation": "With 'along with', the verb agrees with the first subject ('The Director', which is singular), so 'is' is correct.",
                "explanation_hi": "'along with' के साथ, क्रिया पहले कर्ता ('The Director', जो एकवचन है) के अनुसार होती है, इसलिए 'is' सही है।",
                "explanation_gu": "'along with' માં ક્રિયાપદ પ્રથમ કર્તા ('The Director' - એકવચન) પ્રમાણે આવતું હોવાથી 'is' સાચું છે."
            }
        ]
    },
    {
        "id": "ncert_class10_grammar_ch4",
        "title": "Reported Speech — Commands, Requests & Dialogue Completion",
        "title_hi": "रिपोर्टेड स्पीच — आदेश, अनुरोध और संवाद पूर्ति",
        "title_gu": "રિપોર્ટેડ સ્પીચ — આજ્ઞા, વિનંતી અને સંવાદ પૂર્ણતા",
        "class_num": 10,
        "ch_num": 4,
        "blocks": [
            {
                "id": "KOBJ_C10_ENG_G4_B1",
                "type": "hook",
                "title": "Dialogue Completion in Board Exams",
                "title_hi": "बोर्ड परीक्षाओं में संवाद पूर्ति",
                "title_gu": "બોર્ડ પરીક્ષામાં ડાયલોગ કમ્પ્લીશન",
                "body": "In Class 10 Board Exams, you will get dialogues between two people and must convert them into reported speech paragraphs. Mastery over reporting verbs is key!",
                "body_hi": "कक्षा 10 बोर्ड परीक्षाओं में, आपको दो लोगों के बीच संवाद मिलेंगे और उन्हें रिपोर्टेड स्पीच पैराग्राफ में बदलना होगा।",
                "body_gu": "ધોરણ 10 બોર્ડમાં બે વ્યક્તિ વચ્ચેના સંવાદને પરોક્ષ કથન ફકરામાં ફેરવવાનો પ્રશ્ન આવે છે."
            },
            {
                "id": "KOBJ_C10_ENG_G4_B2",
                "type": "theory",
                "title": "Reporting Special Sentence Types",
                "title_hi": "विशेष वाक्य प्रकारों की रिपोर्टिंग",
                "title_gu": "વિશેષ વાક્ય પ્રકારોનું પરોક્ષ કથન",
                "body": "• Imperative (Commands/Requests): Reporting verb becomes ordered, requested, advised + TO + V1.\n• Interrogative (Questions): Yes/No → IF/WHETHER. Wh-questions → keep WH-word + statement order (subject before verb).\n• Exclamatory: Exclaimed with joy/sorrow/surprise + THAT.",
                "body_hi": "• आदेशत्मक/अनुरोधनात्मक: आदेश दिया, अनुरोध किया, सलाह दी + TO + V1।\n• प्रश्नवाचक: Yes/No → IF/WHETHER। Wh-प्रश्न → WH-शब्द रखें + साधारण वाक्य क्रम।\n• विस्मयादिबोधक: Exclaimed with joy/sorrow + THAT।",
                "body_gu": "• આજ્ઞાર્થ: ordered/requested/advised + TO + V1.\n• પ્રશ્નાર્થ: Yes/No પ્રશ્ન → IF/WHETHER. Wh-પ્રશ્ન → WH-શબ્દ + વિધાન વાક્ય રચના."
            },
            {
                "id": "KOBJ_C10_ENG_G4_B3",
                "type": "quiz",
                "question": "Convert to Indirect: The doctor said to the patient, 'Do not eat fried food.'",
                "question_hi": "Indirect में बदलें: The doctor said to the patient, 'Do not eat fried food.'",
                "question_gu": "Indirect માં ફેરવો: The doctor said to the patient, 'Do not eat fried food.'",
                "options": [
                    "The doctor advised the patient not to eat fried food.",
                    "The doctor told the patient to not eat fried food.",
                    "The doctor said to the patient that do not eat fried food.",
                    "The doctor advised the patient that he does not eat fried food."
                ],
                "options_hi": [
                    "The doctor advised the patient not to eat fried food.",
                    "The doctor told the patient to not eat fried food.",
                    "The doctor said to the patient that do not eat fried food.",
                    "The doctor advised the patient that he does not eat fried food."
                ],
                "options_gu": [
                    "The doctor advised the patient not to eat fried food.",
                    "The doctor told the patient to not eat fried food.",
                    "The doctor said to the patient that do not eat fried food.",
                    "The doctor advised the patient that he does not eat fried food."
                ],
                "correct_index": 0,
                "explanation": "Negative imperative 'Do not eat' becomes 'advised... not to eat'.",
                "explanation_hi": "नकारात्मक आदेशत्मक 'Do not eat' बदलकर 'advised... not to eat' हो जाता है।",
                "explanation_gu": "નકારાત્મક આજ્ઞાર્થ 'Do not eat' નું 'advised... not to eat' થાય છે."
            }
        ]
    },
    {
        "id": "ncert_class10_grammar_ch5",
        "title": "Active & Passive Voice — Advanced Imperatives & Prepositions",
        "title_hi": "एक्टिव और पैसिव वॉइस — उन्नत संरचनाएं",
        "title_gu": "એક્ટિવ અને પેસિવ વોઇસ — એડવાન્સ સંરચનાઓ",
        "class_num": 10,
        "ch_num": 5,
        "blocks": [
            {
                "id": "KOBJ_C10_ENG_G5_B1",
                "type": "hook",
                "title": "Transforming Imperatives & Questions",
                "title_hi": "आदेशों और प्रश्नों का रूपांतरण",
                "title_gu": "આજ્ઞાર્થ અને પ્રશ્નાર્થનું ફેરબદલ",
                "body": "How do you change 'Shut the door!' into passive voice? 'Let the door be shut!' Board exams test these tricky non-assertive passive transformations.",
                "body_hi": "'Shut the door!' को कर्मवाच्य में कैसे बदलें? 'Let the door be shut!' बोर्ड परीक्षाएं इन पेचीदा पैसिव रूपांतरणों का परीक्षण करती हैं।",
                "body_gu": "'Shut the door!' નું પેસિવ 'Let the door be shut!' થાય છે. બોર્ડમાં આવા ખાસ પ્રશ્નો આવે છે."
            },
            {
                "id": "KOBJ_C10_ENG_G5_B2",
                "type": "theory",
                "title": "Special Passive Formulas",
                "title_hi": "विशेष पैसिव सूत्र",
                "title_gu": "વિશેષ પેસિવ સૂત્રો",
                "body": "• Imperative Command: LET + Object + BE + V3\n• Imperative Advice: Object + SHOULD BE + V3\n• Verbs with two objects: Primary emphasis on Indirect Object (e.g., 'He gave me a book' → 'I was given a book by him')\n• Passive without 'by': Used when agent is obvious ('The thief was arrested')",
                "body_hi": "• आदेश: LET + कर्म + BE + V3\n• सलाह: कर्म + SHOULD BE + V3\n• दो कर्म वाली क्रियाएं: अप्रत्यक्ष कर्म पर प्राथमिक जोर।\n• 'by' के बिना पैसिव: जब कर्ता स्पष्ट हो ('The thief was arrested')",
                "body_gu": "• આજ્ઞા: LET + કર્મ + BE + V3\n• સલાહ: કર્મ + SHOULD BE + V3\n• 'by' વગરનું પેસિવ: જ્યારે કરનાર સ્પષ્ટ હોય ('The thief was arrested')"
            },
            {
                "id": "KOBJ_C10_ENG_G5_B3",
                "type": "quiz",
                "question": "Change to Passive: 'Help the poor.'",
                "question_hi": "Passive में बदलें: 'Help the poor.'",
                "question_gu": "Passive માં ફેરવો: 'Help the poor.'",
                "options": [
                    "The poor should be helped.",
                    "Let the poor helped.",
                    "The poor are helped.",
                    "Help should be given to poor."
                ],
                "options_hi": [
                    "The poor should be helped.",
                    "Let the poor helped.",
                    "The poor are helped.",
                    "Help should be given to poor."
                ],
                "options_gu": [
                    "The poor should be helped.",
                    "Let the poor helped.",
                    "The poor are helped.",
                    "Help should be given to poor."
                ],
                "correct_index": 0,
                "explanation": "Imperative expressing moral advice is best transformed using 'should be + V3'.",
                "explanation_hi": "नैतिक सलाह व्यक्त करने वाले आदेशत्मक वाक्य को 'should be + V3' का उपयोग करके बदला जाता है।",
                "explanation_gu": "નૈતિક સલાહ દર્શાવતા વાક્યનું પેસિવ 'should be + V3' વડે થાય છે."
            }
        ]
    },
    {
        "id": "ncert_class10_grammar_ch6",
        "title": "Editing and Omission Exercises (Board Pattern)",
        "title_hi": "संपादन और लोप अभ्यास (बोर्ड पैटर्न)",
        "title_gu": "એડિટિંગ અને ઓમિશન સ્વાધ્યાય (બોર્ડ પેટર્ન)",
        "class_num": 10,
        "ch_num": 6,
        "blocks": [
            {
                "id": "KOBJ_C10_ENG_G6_B1",
                "type": "hook",
                "title": "Spotting the Grammatical Bug",
                "title_hi": "व्याकरणिक गलती पहचानना",
                "title_gu": "વ્યાકરણની ભૂલ શોધો",
                "body": "Editing exercises test your proofreading skills! Each line of a paragraph has ONE error (Incorrect word) and you must write the Correct word.",
                "body_hi": "संपादन अभ्यास आपके प्रूफरीडिंग कौशल का परीक्षण करते हैं! एक पैराग्राफ की प्रत्येक पंक्ति में एक गलती होती है और आपको सही शब्द लिखना होता है।",
                "body_gu": "એડિટિંગ પ્રશ્નમાં ફકરાની દરેક લીટીમાં એક ભૂલ હોય છે જેને સુધારીને સાચો શબ્દ લખવાનો હોય છે."
            },
            {
                "id": "KOBJ_C10_ENG_G6_B2",
                "type": "theory",
                "title": "Common Error Checkpoints",
                "title_hi": "सामान्य त्रुटि जांच बिंदु",
                "title_gu": "સામાન્ય ભૂલોના ચેકપોઇન્ટ્સ",
                "body": "When editing a passage, check these in order:\n1. Tense consistency (Is the story in past tense, but one line has present tense?)\n2. Prepositions (e.g. 'in Monday' → 'on Monday')\n3. Determiners/Articles (e.g. 'a honest man' → 'an honest man')\n4. Subject-Verb Agreement (e.g. 'They was' → 'They were')",
                "body_hi": "पैराग्राफ का संपादन करते समय, क्रम में इनकी जांच करें:\n1. काल संगति\n2. Prepositions\n3. Determiners/आर्टिकल्स\n4. कर्ता-क्रिया संगति",
                "body_gu": "ફકરાનું એડિટિંગ કરતી વખતે આ વસ્તુઓ ચકાસો:\n1. કાળની જાળવણી\n2. Prepositions\n3. Determiners/આર્ટિકલ્સ\n4. કર્તા-ક્રિયાપદ સંબંધ"
            },
            {
                "id": "KOBJ_C10_ENG_G6_B3",
                "type": "quiz",
                "question": "Identify the incorrect word in: 'Health is a valuable asset who must be preserved.'",
                "question_hi": "गलत शब्द की पहचान करें: 'Health is a valuable asset who must be preserved.'",
                "question_gu": "ખોટો શબ્દ ઓળખો: 'Health is a valuable asset who must be preserved.'",
                "options": [
                    "who (should be 'which')",
                    "valuable (should be 'value')",
                    "must (should be 'can')",
                    "asset (should be 'assets')"
                ],
                "options_hi": [
                    "who (should be 'which')",
                    "valuable (should be 'value')",
                    "must (should be 'can')",
                    "asset (should be 'assets')"
                ],
                "options_gu": [
                    "who (should be 'which')",
                    "valuable (should be 'value')",
                    "must (should be 'can')",
                    "asset (should be 'assets')"
                ],
                "correct_index": 0,
                "explanation": "'Health' is a non-living concept, so the relative pronoun 'which' should be used instead of 'who'.",
                "explanation_hi": "'Health' एक निर्जीव अवधारणा है, इसलिए 'who' के बजाय सापेक्ष सर्वनाम 'which' का उपयोग किया जाना चाहिए।",
                "explanation_gu": "'Health' એ નિર્જીવ ખ્યાલ હોવાથી 'who' ને બદલે 'which' આર્ટિકલ/સર્વનામ આવે."
            }
        ]
    },
    {
        "id": "ncert_class10_grammar_ch7",
        "title": "Gap Filling Exercises (Board Pattern)",
        "title_hi": "रिक्त स्थान पूर्ति अभ्यास (बोर्ड पैटर्न)",
        "title_gu": "ગેપ ફીલિંગ સ્વાધ્યાય (બોર્ડ પેટર્ન)",
        "class_num": 10,
        "ch_num": 7,
        "blocks": [
            {
                "id": "KOBJ_C10_ENG_G7_B1",
                "type": "hook",
                "title": "Mastering Cloze Tests",
                "title_hi": "क्लोज़ टेस्ट में महारत हासिल करना",
                "title_gu": "ગેપ ફીલિંગમાં નિપુણતા",
                "body": "Gap filling requires choosing the correct prepositions, conjunctions, articles, or verb forms to complete a short paragraph logically and grammatically.",
                "body_hi": "रिक्त स्थान की पूर्ति के लिए पैराग्राफ को तार्किक और व्याकरणिक रूप से पूरा करने के लिए सही prepositions, conjunctions, आर्टिकल्स या क्रिया रूपों को चुनने की आवश्यकता होती है।",
                "body_gu": "ગેપ ફીલિંગમાં યોગ્ય સંયોજકો, આર્ટિકલ્સ અને ક્રિયાપદો પસંદ કરીને ફકરો પૂર્ણ કરવાનો હોય છે."
            },
            {
                "id": "KOBJ_C10_ENG_G7_B2",
                "type": "theory",
                "title": "4 Steps for 100% Accuracy in Gap Filling",
                "title_hi": "रिक्त स्थान पूर्ति में 100% सटीकता के 4 चरण",
                "title_gu": "ગેપ ફીલિંગમાં 100% ચોક્કસતા માટેના 4 સ્ટેપ્સ",
                "body": "1. Read the entire passage quickly to get the overall context and main tense.\n2. Identify the part of speech needed for each blank (Noun, Verb, Preposition, Conjunction).\n3. Test each option in the blank for tone and grammar match.\n4. Re-read the completed passage to ensure flow.",
                "body_hi": "1. समग्र संदर्भ और मुख्य काल प्राप्त करने के लिए पूरे पैराग्राफ को जल्दी से पढ़ें।\n2. प्रत्येक रिक्त स्थान के लिए आवश्यक शब्द भेद (संज्ञा, क्रिया, Preposition) की पहचान करें।\n3. व्याकरण मैच के लिए प्रत्येक विकल्प का परीक्षण करें।\n4. प्रवाह सुनिश्चित करने के लिए पूरा पैराग्राफ फिर से पढ़ें।",
                "body_gu": "1. આખો ફકરો વાંચી કાળ નક્કી કરો.\n2. કયો શબ્દપ્રકાર (નામ, ક્રિયાપદ, Preposition) જોઈએ છે તે નક્કી કરો.\n3. દરેક વિકલ્પ મૂકી ચકાસો.\n4. આખો ફકરો ફરીથી વાંચી ફ્લો ચકાસો."
            },
            {
                "id": "KOBJ_C10_ENG_G7_B3",
                "type": "quiz",
                "question": "Fill in the blank: 'Education is essential ______ the development of a nation.'",
                "question_hi": "रिक्त स्थान भरें: 'Education is essential ______ the development of a nation.'",
                "question_gu": "ખાલી જગ્યા પૂરો: 'Education is essential ______ the development of a nation.'",
                "options": [
                    "for",
                    "to",
                    "in",
                    "with"
                ],
                "options_hi": [
                    "for",
                    "to",
                    "in",
                    "with"
                ],
                "options_gu": [
                    "for",
                    "to",
                    "in",
                    "with"
                ],
                "correct_index": 0,
                "explanation": "'Essential for' is the correct prepositional combination expressing purpose.",
                "explanation_hi": "'Essential for' उद्देश्य व्यक्त करने वाला सही prepositional संयोजन है।",
                "explanation_gu": "'Essential for' એ હેતુ દર્શાવતું યોગ્ય preposition ની જોડી છે."
            }
        ]
    },
    {
        "id": "ncert_class10_grammar_ch8",
        "title": "Transformation of Sentences — Advanced Board Structures",
        "title_hi": "वाक्य रूपांतरण — उन्नत बोर्ड संरचनाएं",
        "title_gu": "વાક્ય રૂપાંતરણ — એડવાન્સ બોર્ડ રચનાઓ",
        "class_num": 10,
        "ch_num": 8,
        "blocks": [
            {
                "id": "KOBJ_C10_ENG_G8_B1",
                "type": "hook",
                "title": "Degrees of Comparison & Negative Transformations",
                "title_hi": "तुलना की डिग्रियां और नकारात्मक रूपांतरण",
                "title_gu": "તુલનાત્મક ડિગ્રી અને નકારાત્મક રૂપાંતરણ",
                "body": "Transforming sentences like 'No other metal is as heavy as lead' into Superlative ('Lead is the heaviest of all metals') without changing the meaning requires precision!",
                "body_hi": "अहंकार और अर्थ बदले बिना 'No other metal is as heavy as lead' को Superlative ('Lead is the heaviest of all metals') में बदलना सटीकता की मांग करता है!",
                "body_gu": "અર્થ બદલ્યા વિના Positive નું Superlative કે Comparative માં રૂપાંતર કરવું એ બોર્ડનો અગત્યનો પ્રશ્ન છે."
            },
            {
                "id": "KOBJ_C10_ENG_G8_B2",
                "type": "theory",
                "title": "Key Transformation Patterns",
                "title_hi": "प्रमुख रूपांतरण पैटर्न",
                "title_gu": "મુખ્ય રૂપાંતરણ પેટર્ન",
                "body": "1. Too...to → So...that (e.g. 'He is too weak to walk' → 'He is so weak that he cannot walk')\n2. As soon as → No sooner...than (e.g. 'As soon as he saw me, he ran' → 'No sooner did he see me than he ran')\n3. Positive / Comparative / Superlative Degrees",
                "body_hi": "1. Too...to → So...that (उदा. 'He is too weak to walk' → 'He is so weak that he cannot walk')\n2. As soon as → No sooner...than (उदा. 'No sooner did he see me than he ran')\n3. Positive / Comparative / Superlative Degrees",
                "body_gu": "1. Too...to → So...that\n2. As soon as → No sooner...than\n3. Positive / Comparative / Superlative Degrees"
            },
            {
                "id": "KOBJ_C10_ENG_G8_B3",
                "type": "quiz",
                "question": "Transform: 'He is too honest to accept a bribe.'",
                "question_hi": "रूपांतरित करें: 'He is too honest to accept a bribe.'",
                "question_gu": "રૂપાંતરિત કરો: 'He is too honest to accept a bribe.'",
                "options": [
                    "He is so honest that he cannot accept a bribe.",
                    "He is very honest to accept a bribe.",
                    "He is honest so he accepts a bribe.",
                    "He is not honest enough to accept a bribe."
                ],
                "options_hi": [
                    "He is so honest that he cannot accept a bribe.",
                    "He is very honest to accept a bribe.",
                    "He is honest so he accepts a bribe.",
                    "He is not honest enough to accept a bribe."
                ],
                "options_gu": [
                    "He is so honest that he cannot accept a bribe.",
                    "He is very honest to accept a bribe.",
                    "He is honest so he accepts a bribe.",
                    "He is not honest enough to accept a bribe."
                ],
                "correct_index": 0,
                "explanation": "'too...to' transforms into 'so...that + cannot'.",
                "explanation_hi": "'too...to' बदलकर 'so...that + cannot' हो जाता है।",
                "explanation_gu": "'too...to' નું રૂપાંતર 'so...that + cannot' માં થાય છે."
            }
        ]
    },
    {
        "id": "ncert_class10_grammar_ch9",
        "title": "Formal Letter Writing — Structure & Board Format",
        "title_hi": "औपचारिक पत्र लेखन — संरचना और बोर्ड प्रारूप",
        "title_gu": "ઔપચારિક પત્ર લેખન — માળખું અને બોર્ડ ફોર્મેટ",
        "class_num": 10,
        "ch_num": 9,
        "blocks": [
            {
                "id": "KOBJ_C10_ENG_G9_B1",
                "type": "hook",
                "title": "The Power of a Well-Written Letter",
                "title_hi": "एक अच्छे लिखे गए पत्र की शक्ति",
                "title_gu": "સારી રીતે લખાયેલા પત્રની શક્તિ",
                "body": "Formal letters (Letters to Editor, Complaint Letters, Order Placing Letters) carry 5 full marks in Board Exams. 2 marks are strictly for correct layout and format!",
                "body_hi": "औपचारिक पत्र (संपादक को पत्र, शिकायत पत्र, आदेश पत्र) बोर्ड परीक्षाओं में पूरे 5 अंक लाते हैं। 2 अंक केवल सही लेआउट और प्रारूप के लिए हैं!",
                "body_gu": "બોર્ડ પરીક્ષામાં પત્ર લેખનના 5 ગુણ હોય છે, જેમાં 2 ગુણ યોગ્ય ફોર્મેટના જ મળે છે."
            },
            {
                "id": "KOBJ_C10_ENG_G9_B2",
                "type": "theory",
                "title": "Standard Board Letter Format",
                "title_hi": "मानक बोर्ड पत्र प्रारूप",
                "title_gu": "બોર્ડ માન્ય પત્ર ફોર્મેટ",
                "body": "1. Sender's Address (Top Left)\n2. Date (e.g. 15th March 2026)\n3. Receiver's Designation & Address (The Editor / The Principal)\n4. Subject (Concise, underline or bold)\n5. Salutation (Sir / Madam)\n6. Body (3 Paras: Intro, Cause/Details, Conclusion/Request)\n7. Subscription (Yours sincerely / Yours faithfully)",
                "body_hi": "1. प्रेषक का पता (ऊपर बाईं ओर)\n2. दिनांक\n3. प्राप्तकर्ता का पद और पता\n4. विषय\n5. संबोधन (Sir / Madam)\n6. मुख्य भाग (3 पैरा)\n7. समापन (Yours sincerely / Yours faithfully)",
                "body_gu": "1. મોકલનારનું સરનામું (ડાબી બાજુ)\n2. તારીખ\n3. મેળવનારનું હોદ્દો અને સરનામું\n4. વિષય\n5. સંબોધન (Sir / Madam)\n6. પત્રનો મુખ્ય ભાગ (3 ફકરા)\n7. આપનો વિશ્વાસુ (Yours sincerely)"
            },
            {
                "id": "KOBJ_C10_ENG_G9_B3",
                "type": "quiz",
                "question": "What is the correct complementary close for a letter to an Editor?",
                "question_hi": "संपादक को लिखे पत्र का सही औपचारिक समापन क्या है?",
                "question_gu": "તંત્રીને લખેલા પત્ર માટે સાચું સમાપન કયું છે?",
                "options": [
                    "Yours truly / Yours faithfully",
                    "Your loving student",
                    "Yours affectionately",
                    "Thanks and regards"
                ],
                "options_hi": [
                    "Yours truly / Yours faithfully",
                    "Your loving student",
                    "Yours affectionately",
                    "Thanks and regards"
                ],
                "options_gu": [
                    "Yours truly / Yours faithfully",
                    "Your loving student",
                    "Yours affectionately",
                    "Thanks and regards"
                ],
                "correct_index": 0,
                "explanation": "'Yours truly' or 'Yours faithfully' is used for formal letters where you do not know the recipient personally.",
                "explanation_hi": "'Yours truly' या 'Yours faithfully' का उपयोग औपचारिक पत्रों के लिए किया जाता है जब आप प्राप्तकर्ता को व्यक्तिगत रूप से नहीं जानते हैं।",
                "explanation_gu": "'Yours truly' કે 'Yours faithfully' એ ઔપચારિક પત્ર માટે વપરાતું માન્ય સમાપન છે."
            }
        ]
    },
    {
        "id": "ncert_class10_grammar_ch10",
        "title": "Analytical Paragraph Writing — Data & Graph Interpretation",
        "title_hi": "विश्लेषणात्मक पैराग्राफ लेखन — डेटा और ग्राफ व्याख्या",
        "title_gu": "વિશ્લેષણાત્મક ફકરા લેખન — ડેટા અને આલેખ વિશ્લેષણ",
        "class_num": 10,
        "ch_num": 10,
        "blocks": [
            {
                "id": "KOBJ_C10_ENG_G10_B1",
                "type": "hook",
                "title": "Translating Charts into Words",
                "title_hi": "चार्ट को शब्दों में बदलना",
                "title_gu": "આલેખ કે ચાર્ટનું લખાણમાં રૂપાંતર",
                "body": "Analytical Paragraph Writing asks you to analyze a given pie-chart, bar graph, or data table and write a clear, objective 100-120 word summary.",
                "body_hi": "विश्लेषणात्मक पैराग्राफ लेखन आपको दिए गए पाई-चार्ट, बार ग्राफ या डेटा तालिका का विश्लेषण करने और एक स्पष्ट, निष्पक्ष 100-120 शब्दों का सारांश लिखने के लिए कहता है।",
                "body_gu": "બોર્ડમાં આપેલા આલેખ કે ચાર્ટ પરથી 100-120 શબ્દોનો વિશ્લેષણાત્મક ફકરો લખવાનો પ્રશ્ન આવે છે."
            },
            {
                "id": "KOBJ_C10_ENG_G10_B2",
                "type": "theory",
                "title": "Key Vocabulary for Data Analysis",
                "title_hi": "डेटा विश्लेषण के लिए प्रमुख शब्दावली",
                "title_gu": "ડેટા વિશ્લેષણ માટેના અગત્યના શબ્દો",
                "body": "• Trends: Increased sharply, declined steadily, peaked at, fluctuated, remained constant.\n• Comparisons: In stark contrast to, whereas, twice as high as, the majority of.\n• Conclusion: Overall, it can be concluded that, the data clearly indicates.",
                "body_hi": "• रुझान: तेजी से बढ़ा, लगातार गिरावट आई, चरम पर पहुंचा, स्थिर रहा।\n• तुलना: इसके बिल्कुल विपरीत, जबकि, दोगुना अधिक, अधिकांश।\n• निष्कर्ष: कुल मिलाकर, यह निष्कर्ष निकाला जा सकता है कि, डेटा स्पष्ट रूप से इंगित करता है।",
                "body_gu": "• ટ્રેન્ડ દર્શાવતા શબ્દો: ઝપાટાભેર વધારો થયો, સતત ઘટાડો થયો, સ્થિર રહ્યો.\n• સરખામણી દર્શાવતા शब्दો: ની સરખામણીમાં, મોટાભાગના.\n• નિષ્કર્ષ: એકંદરે એ તારણ નીકળે છે કે..."
            },
            {
                "id": "KOBJ_C10_ENG_G10_B3",
                "type": "quiz",
                "question": "Which sentence is best suited for the conclusion of an analytical paragraph?",
                "question_hi": "विश्लेषणात्मक पैराग्राफ के निष्कर्ष के लिए कौन सा वाक्य सबसे उपयुक्त है?",
                "question_gu": "વિશ્લેષણાત્મક ફકરાના સમાપન માટે કયું વાક્ય સૌથી યોગ્ય છે?",
                "options": [
                    "Overall, the chart clearly highlights a growing preference for renewable energy.",
                    "I personally think green energy is great.",
                    "The graph has red and blue bars.",
                    "Why don't people use solar energy?"
                ],
                "options_hi": [
                    "Overall, the chart clearly highlights a growing preference for renewable energy.",
                    "I personally think green energy is great.",
                    "The graph has red and blue bars.",
                    "Why don't people use solar energy?"
                ],
                "options_gu": [
                    "Overall, the chart clearly highlights a growing preference for renewable energy.",
                    "I personally think green energy is great.",
                    "The graph has red and blue bars.",
                    "Why don't people use solar energy?"
                ],
                "correct_index": 0,
                "explanation": "Analytical paragraphs must remain objective and summarize overall trends in the conclusion without personal opinions.",
                "explanation_hi": "विश्लेषणात्मक पैराग्राफ को वस्तुनिष्ठ होना चाहिए और व्यक्तिगत राय के बिना निष्कर्ष में समग्र रुझानों का सारांश देना चाहिए।",
                "explanation_gu": "વિશ્લેષણાત્મક ફકરામાં અંગત અભિપ્રાય આપ્યા વિના ડેટાનું તટસ્થ નિષ્કર્ષ આપવું જરૂરી છે."
            }
        ]
    }
]

def build_all():
    print("======================================================================")
    print("  BUILDING 100% TRILINGUAL ENGLISH GRAMMAR — CLASS 9 & CLASS 10")
    print("======================================================================")

    created_blocks = 0
    created_mcqs = 0

    for item in CHAPTERS_DATA:
        ch_id = item["id"]
        class_num = item["class_num"]
        ch_num = item["ch_num"]
        blocks = item["blocks"]

        # Ensure top-level unwrapped array [...]
        # Save to app_core/chapters/
        ch_path = f"app_core/chapters/{ch_id}.json"
        with open(ch_path, "w", encoding="utf-8") as f:
            json.dump(blocks, f, ensure_ascii=False, indent=2)

        # Sync to app_core/learning_modules/<ch_id>/blocks.json
        lm_dir = f"app_core/learning_modules/{ch_id}"
        os.makedirs(lm_dir, exist_ok=True)
        with open(f"{lm_dir}/blocks.json", "w", encoding="utf-8") as f:
            json.dump(blocks, f, ensure_ascii=False, indent=2)

        meta = {
            "chapter_id": ch_id,
            "title": item["title"],
            "title_hi": item["title_hi"],
            "title_gu": item["title_gu"],
            "class_num": class_num,
            "subject": "English Grammar",
            "book_name": f"**English Grammar (Class {class_num})**",
            "total_blocks": len(blocks)
        }
        with open(f"{lm_dir}/metadata.json", "w", encoding="utf-8") as f:
            json.dump(meta, f, ensure_ascii=False, indent=2)

        # Extract MCQs for assessment bank
        questions = []
        for b in blocks:
            if b.get("type") in ["quiz", "socratic"] and "options" in b:
                questions.append({
                    "id": b["id"] + "_Q",
                    "question": b.get("question", b.get("body", "")),
                    "question_hi": b.get("question_hi", b.get("body_hi", "")),
                    "question_gu": b.get("question_gu", b.get("body_gu", "")),
                    "options": b.get("options", []),
                    "options_hi": b.get("options_hi", []),
                    "options_gu": b.get("options_gu", []),
                    "correct_index": b.get("correct_index", 0),
                    "explanation": b.get("explanation", ""),
                    "explanation_hi": b.get("explanation_hi", ""),
                    "explanation_gu": b.get("explanation_gu", "")
                })

        q_path = f"app_core/assessment/{ch_id}_questions.json"
        with open(q_path, "w", encoding="utf-8") as f:
            json.dump(questions, f, ensure_ascii=False, indent=2)

        created_blocks += len(blocks)
        created_mcqs += len(questions)
        print(f"  Class {class_num:2d} Grammar Ch {ch_num:2d}: {item['title'][:40]:<40} | {len(blocks):2d} blocks | {len(questions):2d} MCQs")

    print("----------------------------------------------------------------------")
    print(f"  Total Chapters Processed: {len(CHAPTERS_DATA)}")
    print(f"  Total Blocks Synced    : {created_blocks}")
    print(f"  Total MCQs Synced      : {created_mcqs}")

    # Now update curriculum JSON files
    update_curriculum()

def update_curriculum():
    print("\n--- UPDATING CURRICULUM DEFINITIONS ---")
    
    c9_chaps = []
    c10_chaps = []

    for item in CHAPTERS_DATA:
        ch_entry = {
            "id": item["id"],
            "title": item["title"],
            "title_hi": item["title_hi"],
            "title_gu": item["title_gu"],
            "path": f"app_core/chapters/{item['id']}.json",
            "unwrapped": True
        }
        if item["class_num"] == 9:
            c9_chaps.append(ch_entry)
        else:
            c10_chaps.append(ch_entry)

    # Class 9 curriculum files
    c9_subject = {
        "id": "english_grammar_class9",
        "name": "**English Grammar — Beehive Syllabus (NCERT/CBSE Class 9)**",
        "name_hi": "**अंग्रेजी व्याकरण — बीहाइव पाठ्यक्रम (NCERT/CBSE कक्षा 9)**",
        "name_gu": "**અંગ્રેજી વ્યાકરણ — બીહાઇવ અભ્યાસક્રમ (NCERT/CBSE ધોરણ 9)**",
        "chapters": c9_chaps
    }

    # Class 10 curriculum files
    c10_subject = {
        "id": "english_grammar_class10",
        "name": "**English Grammar — First Flight Syllabus (NCERT/CBSE Class 10)**",
        "name_hi": "**अंग्रेजी व्याकरण — फर्स्ट फ्लाइट पाठ्यक्रम (NCERT/CBSE कक्षा 10)**",
        "name_gu": "**અંગ્રેજી વ્યાકરણ — ફર્સ્ટ ફ્લાઇટ અભ્યાસક્રમ (NCERT/CBSE ધોરણ 10)**",
        "chapters": c10_chaps
    }

    for fname in ["ncert_class9.json", "cbse_class9.json", "gseb_class9.json"]:
        cpath = f"app_core/curriculum/{fname}"
        if os.path.exists(cpath):
            with open(cpath, "r", encoding="utf-8") as f:
                curr = json.load(f)
            
            subjs = curr.get("subjects", [])
            # replace or append grammar subject
            updated = False
            for idx, s in enumerate(subjs):
                s_name = s.get("name", "")
                if "grammar" in s_name.lower() or s.get("id") == "english_grammar_class9":
                    subjs[idx] = c9_subject
                    updated = True
                    break
            if not updated:
                subjs.append(c9_subject)
            curr["subjects"] = subjs

            with open(cpath, "w", encoding="utf-8") as f:
                json.dump(curr, f, ensure_ascii=False, indent=2)
            print(f"  Updated curriculum: {fname}")

    for fname in ["ncert_class10.json", "cbse_class10.json", "gseb_class10.json"]:
        cpath = f"app_core/curriculum/{fname}"
        if os.path.exists(cpath):
            with open(cpath, "r", encoding="utf-8") as f:
                curr = json.load(f)
            
            subjs = curr.get("subjects", [])
            updated = False
            for idx, s in enumerate(subjs):
                s_name = s.get("name", "")
                if "grammar" in s_name.lower() or s.get("id") == "english_grammar_class10":
                    subjs[idx] = c10_subject
                    updated = True
                    break
            if not updated:
                subjs.append(c10_subject)
            curr["subjects"] = subjs

            with open(cpath, "w", encoding="utf-8") as f:
                json.dump(curr, f, ensure_ascii=False, indent=2)
            print(f"  Updated curriculum: {fname}")

if __name__ == "__main__":
    build_all()
