import json
import os

def generate_full_english_ch3():
    chapter_id = "ncert_class10_english_ch3"
    title = "Chapter 3: Two Stories about Flying (First Flight)"
    
    metadata = {
        "id": chapter_id,
        "title": title,
        "subtitle": "Interactive Full-Text Reading",
        "subject": "English",
        "grade": "10",
        "board": "NCERT/CBSE",
        "curriculum": ["Universal"],
        "language": "English/Hindi/Gujarati (Bilingual)",
        "difficulty": "Advanced",
        "estimated_minutes": 120,
        "version": "4.0.0-FULL-TEXT",
        "author": "Antigravity Supreme Intelligence",
        "reviewed_by": "Chief Academic Architect",
        "tags": ["english", "first_flight", "two_stories_about_flying", "his_first_flight", "black_aeroplane", "full_text"],
        "learning_outcomes": [
            "Read and comprehend the original NCERT texts of Part I ('His First Flight') and Part II ('The Black Aeroplane').",
            "Understand the universal themes of conquering fear, self-reliance, taking calculated risks, and human instinct.",
            "Master difficult vocabulary with contextual bilingual translations (Hindi/Gujarati).",
            "Analyze literary techniques including irony, suspense, symbolism, and solve Board Exam HOTS questions."
        ],
        "ai_context": {
            "learning_goal": "Provide the exact NCERT text broken into passages, with inline translations using backticks for the Smart Translation Filter."
        }
    }
    
    blocks = [
        {
            "type": "hook",
            "content": "Have you ever stood on the edge of a diving board or faced a terrifying challenge where your legs froze and fear held you captive?\n\nIn Chapter 3 of *First Flight*, we explore two breathtaking stories about courage and conquering the skies:\n1. **Part I: His First Flight** (by Liam O'Flaherty) — A young seagull who is terrified of flying and starves on a lonely cliff until motherly love forces him into the air!\n2. **Part II: The Black Aeroplane** (by Frederick Forsyth) — A pilot trapped inside pitch-black storm clouds whose instruments fail completely, guided to safety by a phantom black aircraft!\n\nLet's read the *original, full stories* line-by-line with rich bilingual translations!",
            "difficulty": "Beginner",
            "bloom": "Understand"
        },
        {
            "type": "diagram",
            "content": "The young seagull hesitating on the cliff edge while his family flies across the sea.",
            "image_url": "assets/images/eng_ch3_seagull_ledge.jpg",
            "alt_text": "A young seagull standing on a cliff ledge looking down at the vast sea."
        },
        {
            "type": "theory",
            "title": "Passage 1: The Young Seagull on the Ledge",
            "content": "The young seagull was alone on his ledge `(छज्जा, चट्टान की निकली हुई धार / ટેકરીની ધાર, છાજલી)`. His two brothers and his sister had already flown away the day before. He had been afraid to fly with them. Somehow when he had taken a little run forward to the brink `(किनारा / કાંઠો, કિનારો)` of the ledge and attempted to flap `(फड़फड़ाना / ફફડાવવું)` his wings he became afraid.\n\nThe great expanse `(विशाल फैलाव / વિશાળ વિસ્તાર)` of sea stretched down beneath, and it was such a long way down — miles down. He felt certain that his wings would never support him; so he bent his head and ran away back to the little hole under the ledge where he slept at night.\n\nEven when each of his brothers and his little sister, whose wings were far shorter than his own, ran to the brink, flapped their wings, and flew away, he failed to muster up courage `(हिम्मत जुटाना / હિંમત ભેગી કરવી)` to take that plunge `(कूद, छलांग / કૂદકો, છલાંગ)` which appeared to him so desperate `(हताश, भयानक / હતાશ, લાચાર)`.\n\nHis father and mother had come around calling to him shrilly `(तीखी आवाज में / તીણા અવાજે)`, upbraiding `(डांटते हुए, फटकारते हुए / ઠપકો આપતા, વઢતા)` him, threatening to let him starve `(भूखों मरना / ભૂખે મરવું)` on his ledge unless he flew away. But for the life of him he could not move.",
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "teacher_tip",
            "content": "💡 **Teacher's Insight (Parental Motivation):** Notice how the seagull's parents do not pamper him. They scold, threaten, and leave him alone to starve. Why? Because overprotectiveness would keep him grounded forever. True growth requires stepping out of one's comfort zone and confronting fear!"
        },
        {
            "type": "theory",
            "title": "Passage 2: Abandoned, Hungry and Mocked",
            "content": "That was twenty-four hours ago. Since then nobody had come near him. The day before, all day long, he had watched his parents flying about with his brothers and sister, perfecting `(निपुण बनाना / કુશળ બનાવવું)` them in the art of flight, teaching them how to skim `(सतह को छूते हुए उड़ना / સપાટી પરથી હળવેથી સરકવું)` the waves and how to dive for fish.\n\nHe had, in fact, seen his older brother catch his first herring `(एक प्रकार की समुद्री मछली / એક પ્રકારની દરિયાઈ માછલી)` and devour `(जल्दी-जल्दी निगलना / ઝડપથી ગળી જવું)` it, standing on a rock, while his parents circled around raising a proud cackle `(हर्ष की आवाज / ગૌરવપૂર્ણ કલબલાટ)`. And all the morning the whole family had walked about on the big plateau `(पठार / ઉચ્ચપ્રદેશ)` midway down the opposite cliff taunting `(ताना मारना / મહેણાં મારવા)` him with his cowardice `(कायरता / કાયરતા, ડરપોકપણું)`.\n\nThe sun was now ascending `(ऊपर चढ़ रहा था / આકાશમાં ઉપર ચઢી રહ્યો હતો)` the sky, blazing on his ledge that faced the south. He felt the heat because he had not eaten since the previous nightfall.\n\nHe stepped slowly out to the brink of the ledge, and standing on one leg with the other leg hidden under his wing, he closed one eye, then the other, and pretended to be falling asleep. Still they took no notice of him. He saw his two brothers and his sister lying on the plateau dozing `(ऊंघते हुए / ઝોકાં ખાતા)` with their heads sunk into their necks. His father was preening `(चोंच से पंख संवारना / ચાંચથી પીંછા સાફ કરવા)` the feathers on his white back. Only his mother was looking at him.",
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "Why did the young seagull pretend to be falling asleep on the brink of the ledge?",
                "options": [
                    "He was genuinely exhausted from attempting to fly",
                    "To attract the attention and sympathy of his family",
                    "Because he was suffering from an illness",
                    "To hide from predator birds circling above"
                ],
                "correct_answer": "To attract the attention and sympathy of his family",
                "explanation": "He stood on one leg with the other hidden under his wing and closed his eyes hoping his family would notice his misery and bring him food, but they ignored his act."
            },
            "difficulty": "Intermediate",
            "bloom": "Remember"
        },
        {
            "type": "theory",
            "title": "Passage 3: The Mother's Plunge and The First Flight",
            "content": "She was standing on a little high hump `(टीला, उभार / ઊંચો ટેકરો)` on the plateau, her white breast thrust forward. Now and again, she tore at a piece of fish that lay at her feet and then scraped `(रगड़ा / ઘસ્યું)` each side of her beak on the rock. The sight of the food maddened `(पागल कर दिया / ગાંડો કરી મૂક્યો)` him. How he loved to tear food that way, scraping his beak now and again to whet `(तेज करना, धार लगाना / ધાર કાઢવી, તીક્ષ્ણ કરવું)` it!\n\n\"Ga, ga, ga,\" he cried begging her to bring him some food. \"Gaw-col-ah,\" she screamed back derisively `(उपहासपूर्ण ढंग से / મજાક ઉડાવતા)`. But he kept calling plaintively `(दर्द भरे स्वर में / દર્દભર્યા અવાજે)`, and after a minute or so he uttered a joyful scream. His mother had picked up a piece of the fish and was flying across to him with it.\n\nHe leaned out eagerly, tapping the rock with his feet, trying to get nearer to her as she flew across. But when she was just opposite to him, she halted, her wings motionless, the piece of fish in her beak almost within reach of his beak.\n\nHe waited a moment in surprise, wondering why she did not come nearer, and then, maddened by hunger, he dived at the fish. With a loud scream he fell outwards and downwards into space. Then a monstrous `(भयानक / ભયાનક, રાક્ષસી)` terror seized `(जकड़ लिया / જકડી લીધું)` him and his heart stood still. He could hear nothing. But it only lasted a minute. The next moment he felt his wings spread outwards. The wind rushed against his breast feathers, then under his stomach, and against his wings.",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "teacher_tip",
            "content": "🔥 **Crucial Symbolism - Hunger as the Catalyst:** Notice that fear could not make the seagull fly, nor could scolding. It was **hunger `(भूख / ભૂખ)`** and the sight of fish that maddened him to dive off the ledge. Nature uses necessity as the mother of courage! Once he leapt, his innate flying instincts automatically took over."
        },
        {
            "type": "theory",
            "title": "Passage 4: Soaring High and Landing on the Green Sea",
            "content": "He could feel the tips of his wings cutting through the air. He was not falling headlong `(सिर के बल / માથાભેર)` now. He was soaring `(ऊंचाई पर उड़ना / હવામાં ઊંચે ઊડવું)` gradually downwards and outwards. He was no longer afraid. He just felt a bit dizzy `(चक्कर आना / ચક્કર આવવા)`.\n\nThen he flapped his wings once and he soared upwards. \"Ga, ga, ga, Ga, ga, ga, Gaw-col-ah!\" His mother swooped `(झपट्टा मारते हुए नीचे आई / ઝડપથી નીચે આવી)` past him, her wings making a loud noise. He answered her with another scream. Then his father flew over him screaming. He saw his two brothers and his sister flying around him curveting `(घोड़े की तरह छलांग लगाना / ઘોડાની જેમ હવામાં કૂદવું)` and banking `(एक पंख ऊपर उठाकर तिरछा उड़ना / ત્રાંસા થઈને ઊડવું)` and soaring and diving.\n\nThen he completely forgot that he had not always been able to fly, and commended `(सराहना की / પ્રશંસા કરી)` himself to dive and soar and curve, shrieking `(चीखते हुए / ચીસ પાડતા)` shrilly.\n\nHe was near the sea now, flying straight over it, facing straight out over the ocean. He saw a vast green sea beneath him, with little ridges `(लहरों की धारियाँ / મોજાંઓની કિનારીઓ)` moving over it and he turned his beak sideways and cawed `(कांव-कांव की आवाज निकाली / અવાજ કર્યો)` amusedly.\n\nHis parents and his brothers and sister had landed on this green flooring ahead of him. They were beckoning `(इशारे से बुलाना / ઈશારો કરીને બોલાવવું)` to him, calling shrilly. He dropped his legs to stand on the green sea. His legs sank into it. He screamed with fright and attempted to rise again flapping his wings. But he was tired and weak with hunger and he could not rise, exhausted `(थका-मांदा / થાકીને લોથપોથ)` by the strange exercise. His feet sank into the green sea, and then his belly touched it and he sank no further. He was floating on it, and around him his family was screaming, praising him and their beaks were offering him scraps of dog-fish `(छोटी शार्क मछली के टुकड़े / નાની શાર્ક માછલીના ટુકડા)`. He had made his first flight.",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "What happened when the young seagull tried to stand on the green sea after his first flight?",
                "options": [
                    "He immediately drowned because seagulls cannot float",
                    "His feet sank, but his belly touched the water and he floated safely",
                    "He panicked and flew straight back to his mountain ledge",
                    "His father had to carry him on his back"
                ],
                "correct_answer": "His feet sank, but his belly touched the water and he floated safely",
                "explanation": "When his feet sank into the sea, he thought he was drowning and screamed with fright. But as soon as his belly touched the surface, he realized he naturally floated on water."
            },
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "diagram",
            "content": "The old Dakota 088 entering the pitch-black storm clouds guided by the mysterious black aircraft.",
            "image_url": "assets/images/eng_ch3_black_aeroplane.jpg",
            "alt_text": "An old Dakota plane flying through dark storm clouds alongside a mysterious black aeroplane."
        },
        {
            "type": "theory",
            "title": "Passage 5: The Midnight Flight to England",
            "content": "The moon was coming up in the east, behind me, and stars were shining in the clear sky above me. There wasn't a cloud in the sky. I was happy to be alone high up above the sleeping countryside `(ग्रामीण इलाका / ગ્રામીણ વિસ્તાર)`. I was flying my old Dakota `(डकोटा विमान / જૂનું ડકોટા વિમાન)` aeroplane over France back to England. I was dreaming of my holiday and looking forward to being with my family. I looked at my watch: one-thirty in the morning.\n\n'I ought to call Paris Control soon,' I thought. As I looked down past the nose of the aeroplane, I saw the lights of a big city in front of me. I switched on the radio and said, \"Paris Control, Dakota DS 088 here. Can you hear me? I'm on my way to England. Over.\"\n\nThe voice from the radio answered me immediately: \"DS 088, I can hear you. You ought to turn twelve degrees west now, DS 088. Over.\"\n\nI checked the map and the compass `(दिक्सूचक यंत्र / હોકાયંત્ર)`, switched over to my second and last fuel tank, and turned the Dakota twelve degrees west towards England. 'I'll be in time for breakfast,' I thought. A good big English breakfast! Everything was going well — it was an easy flight.",
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "teacher_tip",
            "content": "💡 **Literary Setting & Foreshadowing:** The story begins with utter tranquility — clear starry skies, serene moonlight, and cheerful thoughts of an English breakfast with family. This peaceful opening creates a sharp dramatic contrast with the catastrophic storm that suddenly confronts the pilot 150 km past Paris!"
        },
        {
            "type": "theory",
            "title": "Passage 6: Inside the Black Storm Clouds",
            "content": "Paris was about 150 kilometres behind me when I saw the clouds. Storm clouds. They were huge. They looked like black mountains standing in front of me across the sky. I knew I could not fly up and over them, and I did not have enough fuel to fly around them to the north or south.\n\n\"I ought to go back to Paris,\" I thought, but I wanted to get home. I wanted that breakfast. 'I'll take the risk,' I thought, and flew that old Dakota straight into the storm.\n\nInside the clouds, everything was suddenly black. It was impossible to see anything outside the aeroplane. The old aeroplane jumped and twisted `(हवा में मरोड़ खाया / હવામાં ગોળ ઘૂમ્યું)` in the air. I looked at the compass. I couldn't believe my eyes: the compass was turning round and round and round. It was dead. It would not work! The other instruments were suddenly dead, too. I tried the radio.\n\n\"Paris Control? Paris Control? Can you hear me?\" There was no answer. The radio was dead too. I had no radio, no compass, and I could not see where I was. I was lost in the storm.",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "What metaphor does the author use to describe the storm clouds standing in front of the Dakota?",
                "options": [
                    "Fluffy cotton pillows floating in the sky",
                    "Black mountains standing across the sky",
                    "A massive dark wall of stone",
                    "An endless ocean of smoke"
                ],
                "correct_answer": "Black mountains standing across the sky",
                "explanation": "The author explicitly compares the gigantic, menacing storm clouds to 'black mountains' standing directly across the sky."
            },
            "difficulty": "Intermediate",
            "bloom": "Remember"
        },
        {
            "type": "theory",
            "title": "Passage 7: The Mysterious Black Aeroplane",
            "content": "Then, in the black clouds quite near me, I saw another aeroplane. It had no lights on its wings, but I could see it flying next to me through the storm. I could see the pilot's face — turned towards me. I was very glad to see another person. He lifted one hand and waved.\n\n\"Follow me,\" he was saying. \"Follow me.\" 'He knows that I am lost,' I thought. 'He's trying to help me.'\n\nHe turned his aeroplane slowly to the north, in front of my Dakota, so that it would be easier for me to follow him. I was very happy to go behind the strange aeroplane like an obedient `(आज्ञाकारी / આજ્ઞાકારી)` child.\n\nAfter half an hour the strange black aeroplane was still there in front of me in the clouds. Now there was only enough fuel in the old Dakota's last tank to fly for five or ten minutes more. I was starting to feel frightened `(डरा हुआ / ડરી ગયેલ)` again. But then he started to go down and I followed through the storm.",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "teacher_tip",
            "content": "💡 **Psychological Insight - The 'Obedient Child' Simile:** The narrator states he followed the mysterious black aeroplane 'like an obedient child'. In moments of extreme crisis and panic, human beings often surrender overthinking and place total trust in an external guide or inner instinct to guide them out of danger."
        },
        {
            "type": "theory",
            "title": "Passage 8: Safe Landing and the Radar Mystery",
            "content": "Suddenly I came out of the clouds and saw two long straight lines of lights in front of me. It was a runway `(हवाई पट्टी / રનવે, વિમાન પટ્ટી)`! An airport! I was safe! I turned to look for my friend in the black aeroplane, but the sky was empty. There was nothing there. The black aeroplane was gone. I could not see it anywhere.\n\nI landed and was not sorry to walk away from the old Dakota near the control tower. I went and asked a woman in the control centre where I was and who the other pilot was. I wanted to say 'Thank you'.\n\nShe looked at me very strangely `(अजीब तरह से / વિચિત્ર રીતે)`, and then laughed. \"Another aeroplane? Up there in this storm? No other aeroplanes were flying tonight. Yours was the only one I could see on the radar `(विमान खोजने का यंत्र / રડાર યંત્ર)`.\"\n\nSo who helped me to arrive there safely without a compass or a radio, and without any more fuel in my tanks? Who was the pilot on the strange black aeroplane, flying in the storm, without lights?",
            "difficulty": "Advanced",
            "bloom": "Evaluate"
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "What unexpected information did the woman in the control center give the narrator?",
                "options": [
                    "The black aeroplane had landed at a different airport",
                    "There were no other aeroplanes flying that night, and only his plane appeared on the radar",
                    "The black aeroplane belonged to the military",
                    "The storm was not real and his instruments had malfunctioned"
                ],
                "correct_answer": "There were no other aeroplanes flying that night, and only his plane appeared on the radar",
                "explanation": "The woman in the control room confirmed that no other plane was in the sky during the storm; the Dakota DS 088 was the solitary dot on the radar."
            },
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "exam_tips",
            "content": "🔥 **BOARD EXAM HOT TOPICS & HIGH-SCORING ANSWERS**\n\n**1. Theme & Message of 'His First Flight':**\n- **Theme:** Fear of the unknown and the necessity of self-reliance.\n- **Key Takeaway:** The first step is always the hardest. The young seagull lacked confidence in his own wings. His mother's tough love (withholding food) forced him to take the plunge, discovering his innate capability. Courage is not the absence of fear, but conquering it.\n\n**2. The Mystery of the Black Aeroplane — Who was the Pilot?**\n- **Question:** Who was the pilot on the strange black aeroplane?\n- **Board Exam Answer:** The author leaves this mystery intentionally open-ended. There are two strong interpretations:\n  - *Interpretation A (Rational/Psychological):* The black aeroplane was a projection of the pilot's own subconscious mind and deep flying experience. In extreme panic, his instinct took over, hallucinating a guide that gave him the calm confidence needed to navigate the dead instruments.\n  - *Interpretation B (Supernatural/Divine):* The mysterious black plane was a guardian angel or miraculous intervention that guided a doomed man safely home.\n\n**3. Vocabulary Key for Board Exams:**\n- `Ledge`: A narrow shelf projecting from a rock/cliff.\n- `Muster up courage`: Gather enough bravery to act.\n- `Preening`: Cleaning and smoothing feathers with a beak.\n- `Whet`: To sharpen a blade or beak.\n- `Radar`: Radio detection and ranging system to track aircraft.",
            "difficulty": "Advanced",
            "bloom": "Evaluate"
        }
    ]

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_english_ch3.json"
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_english_ch3.json"
    final_json["metadata"]["id"] = "gseb_class10_english_ch3"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Full-Text English Chapter 3 Generated Successfully!")

if __name__ == "__main__":
    generate_full_english_ch3()
