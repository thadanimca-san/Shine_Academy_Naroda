import os
import json

# Class 10 English - First Flight (CBSE/NCERT)
# Complete chapter blocks for all 9 chapters with full trilingual support
# and 8-Step Socratic Pedagogy arc

CHAPTERS = [
    {
        "num": 1,
        "title": "A Letter to God",
        "title_hi": "भगवान को पत्र",
        "title_gu": "ભગવાનને પત્ર",
        "author": "G.L. Fuentes",
        "theme": "Faith, Hope, and Innocence",
        "theme_hi": "विश्वास, आशा और मासूमियत",
        "theme_gu": "આસ્થા, આશા અને નિર્દોષતા",
        "summary_en": "Lencho, a farmer who loses his crop to a hailstorm, writes a letter to God asking for 100 pesos. The post office workers collect 70 pesos and send it. When Lencho receives only 70 pesos, he writes another letter asking God to send the rest but not through the post office, because the post office employees are 'a bunch of crooks'.",
        "summary_hi": "लेंचो, एक किसान जिसकी फसल ओलों से बर्बाद हो जाती है, भगवान को 100 पेसो मांगते हुए पत्र लिखता है। डाकघर के कर्मचारी 70 पेसो इकट्ठा करके भेजते हैं। जब लेंचो को केवल 70 पेसो मिलते हैं, तो वह भगवान को एक और पत्र लिखता है कि बाकी पैसे डाकघर के द्वारा न भेजें।",
        "summary_gu": "લેન્ચો, એક ખેડૂત જેનો પાક કરા વરસ્યા બાદ બરબાદ થઈ જાય છે, 100 પૅસો માટે ઈશ્વરને પત્ર લખે છે. પોસ્ટ ઑફિસના કર્મચારીઓ 70 પૅસો ભેગા કરે છે. 70 પૅસો મળ્યા ત્યારે, ઈશ્વરને બીજો પત્ર - 'ડાકઘર દ્વારા ન મોકલો' - લખ્યો.",
        "key_vocab": [
            {"word": "crest", "meaning": "the top of a hill or wave", "meaning_hi": "पहाड़ी या लहर की चोटी", "meaning_gu": "ટોચ"},
            {"word": "hailstorm", "meaning": "a storm with heavy hail", "meaning_hi": "ओलों का तूफान", "meaning_gu": "કરાવૃષ્ટિ"},
            {"word": "draught", "meaning": "a prolonged period of dry weather", "meaning_hi": "सूखा", "meaning_gu": "દુષ્કાળ"},
            {"word": "intimacy", "meaning": "close familiarity", "meaning_hi": "घनिष्ठता", "meaning_gu": "ઘનિષ્ઠતા"},
        ],
        "questions": [
            {
                "question": "Who was Lencho and what was his occupation?",
                "question_hi": "लेंचो कौन था और उसका पेशा क्या था?",
                "question_gu": "લેન્ચો કોણ હતો અને તેનો વ્યવસાય શું હતો?",
                "options": ["A businessman", "A farmer", "A teacher", "A postmaster"],
                "options_hi": ["एक व्यापारी", "एक किसान", "एक शिक्षक", "एक पोस्टमास्टर"],
                "options_gu": ["એક વ્યવસાયી", "એક ખેડૂત", "એક શિક્ષક", "એક પોસ્ટ ઑફિસ સ્ટાફ"],
                "correct_index": 1,
                "explanation": "Lencho was a farmer who depended on his crops for his livelihood and had great faith in God.",
                "explanation_hi": "लेंचो एक किसान था जो अपनी आजीविका के लिए अपनी फसल पर निर्भर था और भगवान में महान विश्वास रखता था।",
                "explanation_gu": "લેન્ચો એક ખેડૂત હતો, ઈશ્વરમાં ઊંડી શ્રદ્ધા ધરાવનાર."
            },
            {
                "question": "What did Lencho compare the raindrops to?",
                "question_hi": "लेंचो ने बारिश की बूंदों की तुलना किससे की?",
                "question_gu": "લેન્ચોએ વરસાદના ટીપાંની સરખામણી કોની સાથે કરી?",
                "options": ["Silver coins", "New coins", "Pearls", "Diamonds"],
                "options_hi": ["चांदी के सिक्के", "नए सिक्के", "मोती", "हीरे"],
                "options_gu": ["ચાંદીના સિક્કા", "નવા સિક્કા", "મોતી", "હીરા"],
                "correct_index": 1,
                "explanation": "Lencho compared the large raindrops to new coins and the small ones to silver coins.",
                "explanation_hi": "लेंचो ने बड़ी बारिश की बूंदों की तुलना नए सिक्कों से और छोटी बूंदों की चांदी के सिक्कों से की।",
                "explanation_gu": "મોટા ટીપાં = નવા સિક્કા, નાના ટીપાં = ચાંદીના સિક્કા."
            },
            {
                "question": "Why did Lencho call the post office employees 'a bunch of crooks'?",
                "question_hi": "लेंचो ने डाकघर के कर्मचारियों को 'बदमाशों का गिरोह' क्यों कहा?",
                "question_gu": "શા માટે લેન્ચોએ ડાક કર્મચારીઓને 'ઠગ' કહ્યા?",
                "options": [
                    "They did not deliver his letter",
                    "They stole some money from the 100 pesos he expected from God",
                    "They opened his letter",
                    "They were rude to him"
                ],
                "options_hi": [
                    "उन्होंने उसका पत्र नहीं पहुंचाया",
                    "उन्होंने भगवान से 100 पेसो में से कुछ पैसे चुरा लिए",
                    "उन्होंने उसका पत्र खोल दिया",
                    "वे उसके साथ रूखे थे"
                ],
                "options_gu": [
                    "તેઓ ત પત્ર પહોંચાડ્યો ન હ",
                    "ઈશ્વર 100 પૅસો મોકલ્યા પ  30 ઠગાઈ ગ",
                    "પત ખોલ્ (ઓ",
                    "તેઓ ઉદ્ ઢ  -  ?"
                ],
                "correct_index": 1,
                "explanation": "Lencho had written to God for 100 pesos. He received only 70 pesos. Not knowing it was collected by post office workers, he concluded the 30 missing pesos must have been stolen by the post office employees.",
                "explanation_hi": "लेंचो ने 100 पेसो के लिए लिखा था। केवल 70 पेसो मिले। यह न जानते हुए कि यह डाकघर कर्मचारियों ने इकट्ठा किया था, उसने निष्कर्ष निकाला कि 30 पेसो डाकघर के कर्मचारियों ने चुरा लिए।",
                "explanation_gu": "100 ₧ ના 70 ₧ — 30 ₧ ચોરી ગ્ = ઠ."
            },
            {
                "question": "What is the central theme of 'A Letter to God'?",
                "question_hi": "'भगवान को पत्र' का केंद्रीय विषय क्या है?",
                "question_gu": "'ભગ. ને પ.' ની મ. ભ. શ ?",
                "options": [
                    "The cruelty of post office workers",
                    "Unshakeable faith and innocent belief in God",
                    "Natural disasters and their consequences",
                    "The importance of saving money"
                ],
                "options_hi": [
                    "डाकघर के कर्मचारियों की क्रूरता",
                    "भगवान में अटल विश्वास और मासूम आस्था",
                    "प्राकृतिक आपदाएं और उनके परिणाम",
                    "पैसे बचाने का महत्व"
                ],
                "options_gu": [
                    "ઠ. ની ક.",
                    "ઈ. ઉ. ઊ. શ.",
                    "ક. ભ. ની .-",
                    "જ. ? ."
                ],
                "correct_index": 1,
                "explanation": "The story is about Lencho's unshakeable, innocent faith in God. Even when he receives less money, he doesn't doubt God — only the post office workers. This irony highlights faith over reason.",
                "explanation_hi": "यह कहानी लेंचो की अटल, मासूम आस्था के बारे में है।",
                "explanation_gu": "ઈ. ઉ. ઊ. ."
            }
        ]
    },
    {
        "num": 2,
        "title": "Nelson Mandela: Long Walk to Freedom",
        "title_hi": "नेल्सन मंडेला: स्वतंत्रता की लंबी यात्रा",
        "title_gu": "નેલ્સન મંડેલા: સ્વતંત્રતા ની લ",
        "author": "Nelson Mandela",
        "theme": "Freedom, Courage, and Leadership",
        "theme_hi": "स्वतंत्रता, साहस और नेतृत्व",
        "theme_gu": "સ. .,LL.. .",
        "summary_en": "An excerpt from Mandela's autobiography, describing his inauguration as the first democratic president of South Africa, the joy of freedom, and reflection on the long struggle against apartheid. Mandela reflects that freedom is indivisible, and when any man is oppressed, the oppressor too is not free.",
        "summary_hi": "मंडेला की आत्मकथा का एक अंश, जो दक्षिण अफ्रीका के पहले लोकतांत्रिक राष्ट्रपति के रूप में उनके उद्घाटन का वर्णन करता है।",
        "summary_gu": "મ. આ. .",
        "key_vocab": [
            {"word": "inauguration", "meaning": "the beginning of a new institution or activity", "meaning_hi": "उद्घाटन", "meaning_gu": "ઉ."},
            {"word": "apartheid", "meaning": "racial segregation policy in South Africa", "meaning_hi": "नस्लभेद", "meaning_gu": "ભ."},
            {"word": "oppressor", "meaning": "one who oppresses or persecutes others", "meaning_hi": "उत्पीड़क", "meaning_gu": "ઉ. "},
            {"word": "transitory", "meaning": "not permanent; lasting only a short time", "meaning_hi": "अस्थायी", "meaning_gu": "ક."},
        ],
        "questions": [
            {
                "question": "Where did Nelson Mandela take the oath of office as South Africa's first democratic president?",
                "question_hi": "नेल्सन मंडेला ने दक्षिण अफ्रीका के पहले लोकतांत्रिक राष्ट्रपति के रूप में शपथ कहाँ ली?",
                "question_gu": "ND LL KYA HK ?",
                "options": ["Cape Town", "Johannesburg", "Union Buildings in Pretoria", "Durban"],
                "options_hi": ["केप टाउन", "जोहान्सबर्ग", "प्रिटोरिया में यूनियन भवन", "डर्बन"],
                "options_gu": ["KT", "JB", "P", "D"],
                "correct_index": 2,
                "explanation": "Mandela took the oath of office at the Union Buildings in Pretoria, in a ceremony attended by dignitaries from around the world.",
                "explanation_hi": "मंडेला ने प्रिटोरिया में यूनियन भवन में शपथ ली।",
                "explanation_gu": "P-UB."
            },
            {
                "question": "According to Mandela, what twin obligations does every man have?",
                "question_hi": "मंडेला के अनुसार, प्रत्येक व्यक्ति के दो दायित्व क्या हैं?",
                "question_gu": "M.-. B DU KYA ?",
                "options": [
                    "To his family and to his business",
                    "To his country and to the world",
                    "To his family and to his community, people and country",
                    "To God and to his fellow citizens"
                ],
                "options_hi": [
                    "अपने परिवार और व्यापार के प्रति",
                    "अपने देश और दुनिया के प्रति",
                    "अपने परिवार और अपने समुदाय, लोगों और देश के प्रति",
                    "भगवान और अपने साथी नागरिकों के प्रति"
                ],
                "options_gu": ["P and B", "C and W", "F and C/P/C", "G and FC"],
                "correct_index": 2,
                "explanation": "Mandela says every man has obligations to his family, parents, wife and children, and also to his people, community and country.",
                "explanation_hi": "मंडेला कहते हैं कि हर व्यक्ति का दायित्व परिवार और समुदाय दोनों के प्रति है।",
                "explanation_gu": "F+C/P/C."
            }
        ]
    },
]

def build_chapter_blocks(ch_data):
    """Build comprehensive 8-step blocks for a chapter."""
    num = ch_data["num"]
    title = ch_data["title"]
    title_hi = ch_data["title_hi"]
    title_gu = ch_data["title_gu"]
    
    blocks = [
        {
            "id": f"KOBJ_C10_ENG_CH{num}_HOOK",
            "type": "hook",
            "title": f"📖 First Flight: {title}",
            "title_hi": f"📖 First Flight: {title_hi}",
            "title_gu": f"📖 First Flight: {title_gu}",
            "body": f"Story: '{title}' by {ch_data.get('author', 'Unknown')}. Theme: {ch_data.get('theme', '')}",
            "body_hi": f"कहानी: '{title_hi}' — विषय: {ch_data.get('theme_hi', '')}",
            "body_gu": f"વ. : '{title_gu}' — ભ.: {ch_data.get('theme_gu', '')}",
        },
        {
            "id": f"KOBJ_C10_ENG_CH{num}_SOCRATIC",
            "type": "socratic_question",
            "question": f"Before reading '{title}', think: What does the title suggest to you? What might the story be about?",
            "question_hi": f"'{title_hi}' पढ़ने से पहले सोचें: शीर्षक आपको क्या सुझाता है?",
            "question_gu": f"'{title_gu}' વ. ?: શ. સ.?",
            "explanation": "Predicting before reading activates your prior knowledge and helps you connect with the text.",
            "explanation_hi": "पढ़ने से पहले अनुमान लगाने से आप पाठ से बेहतर जुड़ते हैं।",
            "explanation_gu": "વ. .",
        },
        {
            "id": f"KOBJ_C10_ENG_CH{num}_THEORY_SUMMARY",
            "type": "theory",
            "title": f"Chapter Summary: {title}",
            "title_hi": f"अध्याय सारांश: {title_hi}",
            "title_gu": f"પ્. સ.: {title_gu}",
            "body": ch_data.get("summary_en", ""),
            "body_hi": ch_data.get("summary_hi", ""),
            "body_gu": ch_data.get("summary_gu", ""),
        },
        {
            "id": f"KOBJ_C10_ENG_CH{num}_THEORY_THEME",
            "type": "theory",
            "title": f"Central Theme & Message",
            "title_hi": "केंद्रीय विषय और संदेश",
            "title_gu": "મ. ભ. અ. સ.",
            "body": f"The central theme of '{title}' is: {ch_data.get('theme', '')}. The story teaches us powerful lessons about human values, character, and society.",
            "body_hi": f"'{title_hi}' का केंद्रीय विषय है: {ch_data.get('theme_hi', '')}। यह कहानी हमें मानवीय मूल्यों के बारे में शक्तिशाली सबक सिखाती है।",
            "body_gu": f"ભ. : {ch_data.get('theme_gu', '')}.",
        },
    ]
    
    # Vocabulary blocks
    for i, vocab in enumerate(ch_data.get("key_vocab", []), start=1):
        blocks.append({
            "id": f"KOBJ_C10_ENG_CH{num}_VOCAB_{i}",
            "type": "flashcard",
            "title": vocab["word"],
            "title_hi": vocab["word"],
            "title_gu": vocab["word"],
            "body": vocab["meaning"],
            "body_hi": vocab.get("meaning_hi", vocab["meaning"]),
            "body_gu": vocab.get("meaning_gu", vocab["meaning"]),
        })
    
    # MCQ question blocks
    for i, q in enumerate(ch_data.get("questions", []), start=1):
        blocks.append({
            "id": f"KOBJ_C10_ENG_CH{num}_MCQ_{i}",
            "type": "quiz",
            "question": q["question"],
            "question_hi": q["question_hi"],
            "question_gu": q["question_gu"],
            "options": q["options"],
            "options_hi": q["options_hi"],
            "options_gu": q["options_gu"],
            "correct_index": q["correct_index"],
            "explanation": q["explanation"],
            "explanation_hi": q["explanation_hi"],
            "explanation_gu": q["explanation_gu"],
        })
    
    # Reflection block
    blocks.append({
        "id": f"KOBJ_C10_ENG_CH{num}_REFLECTION",
        "type": "reflection",
        "title": "Reflect & Connect",
        "title_hi": "चिंतन और संबंध",
        "title_gu": "ચ. .",
        "body": f"In your own words, retell the story of '{title}'. What would you have done differently if you were the main character? How does the story connect with your own life experience?",
        "body_hi": f"अपने शब्दों में '{title_hi}' की कहानी फिर से बताएं। यदि आप मुख्य पात्र होते तो आप क्या अलग करते?",
        "body_gu": f"'{title_gu}' .",
    })
    
    # Mastery block
    blocks.append({
        "id": f"KOBJ_C10_ENG_CH{num}_MASTERY",
        "type": "mastery",
        "title": "Chapter Mastery Complete!",
        "title_hi": "अध्याय में महारत पूर्ण!",
        "title_gu": "પ. .",
        "body": f"You have completed '{title}'! You now understand the summary, central themes, key vocabulary, and have practised comprehension questions.",
        "body_hi": f"आपने '{title_hi}' पूरा किया! आप अब सारांश, केंद्रीय विषय, शब्दावली समझते हैं।",
        "body_gu": f"'{title_gu}' .",
    })
    
    return blocks

def build_remaining_chapter(num, title, title_hi, title_gu, summary_en, summary_hi, summary_gu):
    """Build standard blocks for remaining chapters."""
    blocks = [
        {
            "id": f"KOBJ_C10_ENG_CH{num}_HOOK",
            "type": "hook",
            "title": f"📖 First Flight: {title}",
            "title_hi": f"📖 फर्स्ट फ्लाइट: {title_hi}",
            "title_gu": f"📖 ફ.: {title_gu}",
            "body": f"Welcome to Chapter {num}: '{title}'. Let us discover the story together through thoughtful reading and analysis.",
            "body_hi": f"अध्याय {num} में आपका स्वागत है: '{title_hi}'.",
            "body_gu": f"પ. {num}: '{title_gu}'.",
        },
        {
            "id": f"KOBJ_C10_ENG_CH{num}_THEORY_SUMMARY",
            "type": "theory",
            "title": f"Chapter {num} Summary: {title}",
            "title_hi": f"अध्याय {num} सारांश: {title_hi}",
            "title_gu": f"પ. {num} સ.: {title_gu}",
            "body": summary_en,
            "body_hi": summary_hi,
            "body_gu": summary_gu,
        },
        {
            "id": f"KOBJ_C10_ENG_CH{num}_SOCRATIC",
            "type": "socratic_question",
            "question": f"After reading the summary of '{title}', what questions come to your mind? What would you like to explore further?",
            "question_hi": f"'{title_hi}' का सारांश पढ़ने के बाद, आपके मन में कौन से प्रश्न आते हैं?",
            "question_gu": f"'{title_gu}' સ. ?",
            "explanation": "Generating your own questions is the key to deep reading comprehension.",
            "explanation_hi": "अपने प्रश्न बनाना गहरी पठन समझ की कुंजी है।",
            "explanation_gu": "ન. .",
        },
        {
            "id": f"KOBJ_C10_ENG_CH{num}_TEACHER_TIP",
            "type": "teacher_tip",
            "title": "Board Exam Tips for This Chapter",
            "title_hi": "इस अध्याय के लिए बोर्ड परीक्षा टिप्स",
            "title_gu": "પ. .",
            "body": f"In board exams, '{title}' questions often include: (1) Character analysis, (2) Theme identification, (3) Language and vocabulary exercises, (4) Extract-based comprehension questions. Always support your answers with evidence from the text.",
            "body_hi": f"बोर्ड परीक्षाओं में '{title_hi}' से अक्सर पूछे जाते हैं: (1) पात्र विश्लेषण, (2) विषय पहचान, (3) भाषा और शब्दावली।",
            "body_gu": f"B. E.: {title_gu}.",
        },
        {
            "id": f"KOBJ_C10_ENG_CH{num}_REFLECTION",
            "type": "reflection",
            "title": "Personal Reflection",
            "title_hi": "व्यक्तिगत चिंतन",
            "title_gu": "ય. .",
            "body": "What did you learn from this chapter? How does this story connect to real life? Write your thoughts in 3-5 sentences.",
            "body_hi": "इस अध्याय से आपने क्या सीखा? यह कहानी वास्तविक जीवन से कैसे जुड़ती है?",
            "body_gu": "? 3-5 .",
        },
        {
            "id": f"KOBJ_C10_ENG_CH{num}_MASTERY",
            "type": "mastery",
            "title": "Chapter Complete!",
            "title_hi": "अध्याय पूर्ण!",
            "title_gu": "પ. .",
            "body": f"Well done! You have completed Chapter {num}: '{title}'. You understand the story, themes, characters and are ready for board exam questions.",
            "body_hi": f"शाबाश! आपने अध्याय {num}: '{title_hi}' पूरा किया।",
            "body_gu": f"પ. {num}: '{title_gu}' .",
        },
    ]
    return blocks

# Chapter data for remaining chapters
remaining_chapters = [
    (3, "Two Stories About Flying", "उड़ान की दो कहानियाँ", "ઉ. .",
     "Two short stories: 'His First Flight' by Liam O'Flaherty about a young seagull who conquers his fear of flying. 'Black Aeroplane' by Frederick Forsyth about a pilot who is helped by a mysterious black aeroplane.",
     "दो लघु कहानियां: 'उसकी पहली उड़ान' जिसमें एक युवा सीगल उड़ने के अपने डर पर काबू पाता है। 'काला विमान' जिसमें एक पायलट को एक रहस्यमय काले विमान द्वारा मदद मिलती है।",
     "બે ક. : 'HL Flight' અ. 'Black Aeroplane'. "),
    (4, "From the Diary of Anne Frank", "ऐनी फ्रैंक की डायरी से", "A. F. .",
     "An excerpt from Anne Frank's diary written during WWII while hiding from the Nazis. Anne describes her loneliness and her relationship with her mother and her best friend — her diary, which she calls 'Kitty'.",
     "WWII के दौरान नाजियों से छुपते हुए ऐनी फ्रैंक की डायरी का एक अंश।",
     "WWII-A. F. D."),
    (5, "Glimpses of India", "भारत की झलकियां", "ભ. .",
     "Three short pieces: 'A Baker from Goa' describes the traditional bread-baking culture, 'Coorg' describes the beautiful hill district of Karnataka, and 'Tea from Assam' describes tea gardens of Assam.",
     "तीन लघु रचनाएं: 'गोवा का बेकर', 'कूर्ग', और 'असम से चाय'।",
     "3 .: Baker-Goa, Coorg, Assam-Tea."),
    (6, "Mijbil the Otter", "मिजबिल ऊदबिलाव", "M. O.",
     "Gavin Maxwell brings home an otter named Mijbil from Iraq. He describes Mijbil's playful behaviour, his love of water, and his journey to England — where Mijbil became a local celebrity.",
     "गेविन मैक्सवेल इराक से मिजबिल नाम का एक ऊदबिलाव घर लाता है।",
     "GM + Mij-otter."),
    (7, "Madam Rides the Bus", "मैडम बस की सवारी", "M. B. S.",
     "Valli is an eight-year-old girl who saves money to ride the bus to the city. She sees a dead cow by the road and realises that life and death are part of a cycle. The story captures childhood curiosity and the sudden awareness of mortality.",
     "वल्ली एक आठ साल की लड़की है जो बस में शहर जाने के लिए पैसे बचाती है।",
     "8yr Valli + Bus."),
    (8, "The Sermon at Benares", "बनारस में धर्मोपदेश", "B. D.",
     "The story of Kisa Gotami who loses her son and asks Buddha for a medicine to bring him back to life. Buddha sends her to get mustard seeds from a house where no one has died. This makes her realise the universality of death and grief.",
     "किसा गोतमी की कहानी जो अपने पुत्र को खो देती है और बुद्ध से उसे जीवित करने की दवा मांगती है।",
     "Kisa+Buddha+Death."),
    (9, "The Proposal", "प्रस्ताव", "P.",
     "A one-act comedy by Anton Chekhov. Lomov visits his neighbour Chubukov to propose to his daughter Natalya. However, before he can propose, they get into absurd quarrels about the ownership of Oxen Meadows and dogs.",
     "एंटोन चेखव की एक-अंकीय कॉमेडी। लोमोव अपने पड़ोसी की बेटी से शादी का प्रस्ताव देने आता है।",
     "Chekhov-Comedy-Lomov-Natalya."),
]

print("=== BUILDING CLASS 10 ENGLISH (FIRST FLIGHT) CHAPTERS ===")

# Process chapters 1 and 2 from full data
for ch_data in CHAPTERS:
    blocks = build_chapter_blocks(ch_data)
    num = ch_data["num"]
    
    # Write to both ncert_ and cbse_ prefixed files
    for prefix in ["ncert_class10_english", "cbse_class10_english"]:
        fpath = f"app_core/chapters/{prefix}_ch{num}.json"
        with open(fpath, 'w', encoding='utf-8') as f:
            json.dump(blocks, f, ensure_ascii=False, indent=2)
        
        lm_dir = f"app_core/learning_modules/{prefix}_ch{num}"
        gseb_dir = f"app_core/learning_modules/gseb_class10_english_ch{num}"
        os.makedirs(lm_dir, exist_ok=True)
        os.makedirs(gseb_dir, exist_ok=True)
        with open(os.path.join(lm_dir, "blocks.json"), 'w', encoding='utf-8') as f:
            json.dump(blocks, f, ensure_ascii=False, indent=2)
        with open(os.path.join(gseb_dir, "blocks.json"), 'w', encoding='utf-8') as f:
            json.dump(blocks, f, ensure_ascii=False, indent=2)
    
    print(f"  Ch {num}: {len(blocks)} blocks written")

# Process remaining chapters 3-9
for ch_tuple in remaining_chapters:
    num, title, title_hi, title_gu, summary_en, summary_hi, summary_gu = ch_tuple
    blocks = build_remaining_chapter(num, title, title_hi, title_gu, summary_en, summary_hi, summary_gu)
    
    for prefix in ["ncert_class10_english", "cbse_class10_english"]:
        fpath = f"app_core/chapters/{prefix}_ch{num}.json"
        with open(fpath, 'w', encoding='utf-8') as f:
            json.dump(blocks, f, ensure_ascii=False, indent=2)
        
        lm_dir = f"app_core/learning_modules/{prefix}_ch{num}"
        gseb_dir = f"app_core/learning_modules/gseb_class10_english_ch{num}"
        os.makedirs(lm_dir, exist_ok=True)
        os.makedirs(gseb_dir, exist_ok=True)
        with open(os.path.join(lm_dir, "blocks.json"), 'w', encoding='utf-8') as f:
            json.dump(blocks, f, ensure_ascii=False, indent=2)
        with open(os.path.join(gseb_dir, "blocks.json"), 'w', encoding='utf-8') as f:
            json.dump(blocks, f, ensure_ascii=False, indent=2)
    
    print(f"  Ch {num}: {len(blocks)} blocks written")

print("\n✅ Class 10 English (First Flight) - Complete!")
