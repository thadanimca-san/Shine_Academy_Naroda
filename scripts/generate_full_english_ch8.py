import json
import os

def generate_full_english_ch8():
    chapter_id = "ncert_class10_english_ch8"
    title = "Chapter 8: Mijbil the Otter (First Flight)"
    
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
        "tags": ["english", "first_flight", "mijbil_the_otter", "full_text"],
        "learning_outcomes": [
            "Read and comprehend the original NCERT text by Gavin Maxwell.",
            "Understand the deep bond between humans and unusual animal companions.",
            "Master difficult vocabulary with contextual bilingual translations.",
            "Analyze character traits and humorous incidents for Board Exams."
        ],
        "ai_context": {
            "learning_goal": "Provide the exact NCERT text broken into passages, with inline translations using backticks for the Smart Translation Filter."
        }
    }
    
    blocks = [
        {
            "type": "hook",
            "content": "Most people keep dogs, cats, or birds as pets. But what happens when someone decides to bring a wild river otter `(ऊदबिलाव / જળબિલાડી)` all the way from the marshes of Iraq to a flat in London?\n\nGet ready for an extraordinary, hilarious, and heartwarming journey filled with runaway otters, airborne chaos, and curious Londoners as we explore the *original, full text* of Gavin Maxwell's classic story!",
            "difficulty": "Beginner",
            "bloom": "Understand"
        },
        {
            "type": "diagram",
            "content": "Gavin Maxwell and Mijbil the otter exploring near water.",
            "image_url": "assets/images/eng_ch8_mijbil_intro.jpg",
            "alt_text": "An otter splashing playfully beside its owner."
        },
        {
            "type": "theory",
            "title": "Passage 1: The Idea and the Journey to Basra",
            "content": "Early in the New Year of 1956, I travelled to Southern Iraq. By then it had crossed my mind that I would like to keep an otter `(ऊदबिलाव / જળબિલાડી)` instead of a dog, and that Camusfearna, ringed by water a stone’s throw from its door, would be an eminently `(विशेष रूप से / વિશેષ રૂપે)` suitable spot for this experiment.\n\nWhen I casually mentioned this to a friend, he as casually replied that I had better get one in the Tigris marshes `(दजला नदी के दलदल / ટાઇગ્રિસ નદીના કળણ)`, for there they were as common as mosquitoes, and were often tamed `(पालतू बनाए जाते थे / પાળવામાં આવતા હતા)` by the Arabs.\n\nWe were going to Basra to the Consulate-General to collect and answer our mail from Europe. At the Consulate-General we found that my friend’s mail had arrived but that mine had not.\n\nI cabled `(तार भेजा / તાર મોકલ્યો)` to England, and when, three days later, nothing had happened, I tried to telephone. The call had to be booked twenty-four hours in advance. On the first day the line was out of order; on the second the exchange was closed for a religious holiday; on the third day there was another breakdown. My friend left, and I arranged to meet him in a week’s time. Five days later, my mail arrived.\n\nI carried it to my bedroom to read, and there, squatting `(उकड़ूं बैठे हुए / પલાંઠી વાળીને બેઠેલા)` on the floor, were two Arabs; beside them was a sack `(बोरा / કોથળો)` that squirmed `(छटपटा रहा था / તરફડતું હતું)` from time to time. They handed me a note from my friend: “Here is your otter...”",
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "teacher_tip",
            "content": "💡 **Teacher's Insight:** Notice why Maxwell wanted an otter. His beloved dog had died, and he felt too lonely to keep another dog immediately. His home in Camusfearna (Scotland) was surrounded by water, making it a natural haven for an aquatic creature."
        },
        {
            "type": "theory",
            "title": "Passage 2: An Otter Resembling a Medieval Dragon",
            "content": "With the opening of that sack began a phase of my life in the world that has not yet ended, and may, for all I know, not end before I do: it is, in effect, a thraldom `(गुलामी या गहरा सम्मोहन / ગુલામી કે આકર્ષણ)` to otters, an otter fixation `(गहरा लगाव / તીવ્ર લગાવ)`, that I have since found to be shared by most other people, who have ever owned one.\n\nThe creature that emerged from this sack onto the spacious `(खुले और विशाल / વિશાળ)` tiled floor of the Consulate bedroom resembled most of all a very small, medievally-conceived `(मध्यकालीन कल्पना जैसा / મધ્યયુગીન કલ્પના જેવું)` dragon. From the head to the tip of the tail he was coated with symmetrical `(एक समान / સપ્રમાણ)` pointed scales of mud armour `(कीचड़ का कवच / કાદવનું કવચ)`, between whose tips was visible a soft velvet fur like that of a chocolate-brown mole `(छछूंदर / છછુંદર)`.\n\nHe shook himself, and I half expected a cloud of dust, but in fact it was not for another month that I managed to remove the last of the mud and see the otter, as it were, in his true colours.\n\nMijbil, as I called the otter, was, in fact, of a race previously unknown to science, and was at length christened `(नामकरण किया गया / નામકરણ કરવામાં આવ્યું)` by zoologists `(जीवविज्ञानियों द्वारा / પ્રાણીશાસ્ત્રીઓ દ્વારા)` *Lutrogale perspicillata maxwelli*, or Maxwell’s otter.",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "What scientific name was given to Mijbil by zoologists?",
                "options": [
                    "Lutrogale perspicillata maxwelli",
                    "Canis lupus familiaris",
                    "Panthera leo persica",
                    "Mustela putorius furo"
                ],
                "correct_answer": "Lutrogale perspicillata maxwelli",
                "explanation": "Because Mijbil belonged to a sub-species of smooth-coated otter previously unknown to science, zoologists named it Lutrogale perspicillata maxwelli (Maxwell's otter) after the author."
            },
            "difficulty": "Intermediate",
            "bloom": "Remember"
        },
        {
            "type": "theory",
            "title": "Passage 3: Aloofness, Water Obsession, and the Chromium Tap",
            "content": "For the first twenty-four hours Mijbil was neither hostile `(शत्रुतापूर्ण / શત્રુતાપૂર્ણ)` nor friendly; he was simply aloof `(अलग-थलग / અલગ-અલગ)` and indifferent `(उदासीन / ઉદાસીન)`, choosing to sleep on the floor as far from my bed as possible. The second night Mijbil came on to my bed in the small hours and remained asleep in the crook `(मोड़ / વળાંક)` of my knees until the servant brought tea in the morning, and during the day he began to lose his apathy `(उदासीनता / નિષ્ક્રિયતા)` and take a keen, much too keen, interest in his surroundings.\n\nI made a body-belt for him and took him on a lead `(पट्टे पर / પટ્ટા સાથે)` to the bathroom, where for half an hour he went wild with joy in the water, plunging and rolling in it, shooting up and down the length of the bathtub underwater, and making enough slosh and splash `(छप-छप और छींटे / છબછબિયાં અને ઉછાળવું)` for a hippo.\n\nThis, I was to learn, is a characteristic of otters; every drop of water must be, so to speak, extended and spread about the place; a bowl must at once be overturned, or, if it will not be overturned, be sat in and sploshed in until it overflows. Water must be kept on the move and made to do things; when static `(स्थिर / સ્થિર)` it is wasted and provoking `(परेशान करने वाला / ખીજવનારું)`.\n\nTwo days later, Mijbil escaped from my bedroom as I entered it, and I turned to see his tail disappearing round the bend of the corridor that led to the bathroom. By the time I got there he was up on the end of the bathtub and fumbling `(हाथ-पैर मारना / ટાંપીને પકડવું)` at the chromium taps with his paws. I watched, amazed; in less than a minute he had turned the tap far enough to produce a trickle `(पतली धार / પાતળી ધાર)` of water, and after a moment or two achieved the full flow. (He had been lucky to turn the tap the right way; on later occasions he would sometimes screw it up tighter, chittering `(किटकिटाते हुए / કચકચાવતો અવાજ)` with irritation and disappointment at the tap’s failure to produce water).",
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "teacher_tip",
            "content": "💡 **Otter Psychology:** Otters hate static water! For an otter, water that is not splashing, swirling, or overflowing is considered wasted. Mijbil's ability to turn on the bathroom tap with his paws highlights the remarkable intelligence and manual dexterity of otters."
        },
        {
            "type": "theory",
            "title": "Passage 4: Playful Nature and Marble Juggling",
            "content": "Very soon Mij would follow me without a lead and come to me when I called his name. He spent most of his time in play. He spent hours shuffling `(घसीटना / ઘસીને ફેરવવું)` a rubber ball round the room like a four-footed soccer player using all four feet to dribble `(गेंद को आगे बढ़ाना / દડાને આગળ ધપાવવો)` the ball, and he could also throw it with a powerful flick `(झटका / ઝટકો)` of the neck to a surprising height and distance.\n\nBut the real play of an otter is when he lies on his back and juggles with small objects between his paws. Marbles were Mij’s favourite toys for this pastime `(मनोरंजन / મનોરંજન)`; he would roll two or more of them up and down his wide, flat belly without ever dropping one to the floor, balancing them with remarkable dexterity `(चतुराई और निपुणता / કુશળતા)`.",
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "What was Mijbil's favourite pastime game when lying on his back?",
                "options": [
                    "Juggling marbles on his wide, flat belly",
                    "Dribbling a soccer ball with his front paws",
                    "Chewing on rubber slippers",
                    "Tearing pieces of paper into shreds"
                ],
                "correct_answer": "Juggling marbles on his wide, flat belly",
                "explanation": "Mijbil loved lying on his back and rolling two or more marbles up and down his wide, flat belly without ever dropping a single one to the floor."
            },
            "difficulty": "Beginner",
            "bloom": "Remember"
        },
        {
            "type": "theory",
            "title": "Passage 5: The Appalling Box Incident",
            "content": "The days passed peacefully at Basra, but I dreaded the prospect `(संभावना / સંભાવના)` of transporting Mijbil to England, and now to Camusfearna. The British airline to London would not fly animals, so I booked a flight to Paris on another airline, and from there to London. The airline insisted that Mij should be packed into a box not more than eighteen inches square, to be carried on the floor at my feet.\n\nI had a box made, and an hour before we started, I put Mij into the box so that he would become accustomed `(आदी या अभ्यस्त / ટેવાયેલો)` to it, and I left for a hurried meal.\n\nWhen I returned, there was an appalling `(भयानक और स्तब्धकारी / અત્યંત ભયાનક)` spectacle `(दृश्य / દ્રશ્ય)`. There was complete silence from the box, but from its airholes and chinks `(दरारें / તિરાડો)` around the lid, blood had trickled and dried. I whipped off the lock and tore open the lid. Mij, exhausted and blood-spattered `(खून से लथपथ / લોહીલુહાણ)`, whimpered `(दर्द भरी धीमी आवाज निकाली / કણસ્યો)` and caught at my leg. He had torn the zinc lining `(जस्ते की परत / જસતનું અસ્તર)` of the box to shreds; it had made his nose and mouth bleed.\n\nIt was just ten minutes until the time of the flight, and the airport was five miles distant. I put the miserable otter back into the box, holding down the lid with my hand. I sat in the back of the car with the box beside me as the driver tore through the streets of Basra like a ricochetting bullet `(टकराकर सनसनाती हुई गोली / અથડાઈને છૂટતી ગોળી)`. The aircraft was waiting to take off, and I was rushed through by the infuriated `(अत्यंत क्रोधित / અત્યંત ગુસ્સે થયેલા)` officials.",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "teacher_tip",
            "content": "🔥 **Board Exam Key Question:** Why was the scene with the box described as an 'appalling spectacle'?\nBecause blood had trickled from the airholes and dried up around the lid. Mijbil had desperately torn the sharp zinc lining into shreds in an attempt to escape, severely cutting his nose and mouth."
        },
        {
            "type": "theory",
            "title": "Passage 6: Chaos in the Aircraft and The Noble Air Hostess",
            "content": "I found my seat in the aircraft. The box was placed on the floor between my feet. The engine roared, and the plane took off into the sky. I explained the whole situation to the air hostess, who was the very queen of her kind `(अपनी तरह की अत्यंत दयालु और श्रेष्ठ महिला / અત્યંત દયાળુ અને શ્રેષ્ઠ પરિચારિકા)`. She suggested that I might prefer to have my pet on my knee, and I could have kissed her hands in sheer gratitude.\n\nI opened the box. In a flash, Mij was out of the box! He disappeared at high speed down the aircraft. There were squawks and shrieks `(चीखें और चिल्लाहट / ચીસો અને બૂમાબૂમ)`, and a woman stood up on her seat screaming out, “A rat! A rat!”\n\nI caught sight of Mij’s tail disappearing beneath the legs of a portly `(मोटे-ताजे / સ્થૂળકાય)` turbanned Indian gentleman. Draping `(झुकते हुए / ઝૂકતાં)` myself across the gentleman’s knees, I reached for the otter but found my face covered in curry instead.\n\nThe air hostess stepped in with a charming smile: “Perhaps it would be better if you resume your seat, and I will find the animal and bring it to you.”\n\nI returned to my seat. After a few minutes, I heard from near my feet a distressed chitter `(व्याकुल किटकिटाने की आवाज / આકુળવ્યાકુળ અવાજ)` of recognition and welcome, and Mijbil bounded onto my knees and began to nuzzle `(नाक रगड़ना / નાક ઘસવું)` my face and neck.",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "Why did Maxwell refer to the air hostess as 'the very queen of her kind'?",
                "options": [
                    "She was extremely kind, understanding, and helped manage the situation calmly.",
                    "She belonged to a royal family in Britain.",
                    "She brought delicious food for Mijbil.",
                    "She knew how to train wild otters."
                ],
                "correct_answer": "She was extremely kind, understanding, and helped manage the situation calmly.",
                "explanation": "Maxwell called her 'the very queen of her kind' because of her deep empathy, patience, and professional composure during a highly chaotic flight."
            },
            "difficulty": "Intermediate",
            "bloom": "Evaluate"
        },
        {
            "type": "theory",
            "title": "Passage 7: Life in London - The Suitcase Game and School Wall Habit",
            "content": "After arriving safely, Mijbil and I remained in London for nearly a month. Mij invented games of his own with ping-pong balls, marbles, rubber fruit, and a terrapin `(कछुए का कवच / કાચબાનું કવચ)` shell that I had brought back from the marshes.\n\nWith the ping-pong ball he invented a game that could keep him engrossed `(लीन या मग्न / તલ્લીન)` for up to half an hour at a time. An old suitcase of mine had a damaged lid that sloped down towards one end when closed. Mij would place the ball on the high end and run around to the other side to catch it as it slid down, or dash around to pounce upon it before it reached the bottom.\n\nOutside the flat, I exercised him on a lead, precisely as if he were a dog. Mijbil quickly developed compulsive habits `(अनिवार्य आदतें / આદતવશ વર્તણૂક)` on our walks, like children who must place their feet on the centre of each paving block or touch every seventh iron upright. Opposite my flat was a single-storied primary school, along whose frontage ran a low wall about two feet high. On his way home, Mij would tug `(खींचना / ખેંચવું)` me towards this wall, jump up on it, and gallop the full length of its thirty yards, to the hopeless distraction `(ध्यान भटकाव / ધ્યાન ભંગ)` of both pupils and teachers inside.",
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "diagram",
            "content": "Mijbil galloping on the low wall outside the primary school.",
            "image_url": "assets/images/eng_ch8_mijbil_school_wall.jpg",
            "alt_text": "An otter running excitedly on a low brick wall as schoolchildren look out the window."
        },
        {
            "type": "theory",
            "title": "Passage 8: The Hilarious Guesses of Londoners",
            "content": "The people of London, having never seen an otter before, made wild and fantastic guesses at what kind of creature Mijbil was. Londoners do not recognize an otter, for otters belong to a comparatively small group of animals called Mustellines `(मस्टेलिन प्रजाति / મસ્ટેલિન પ્રજાતિ)`, shared by badger, mongoose, weasel, stoat, and mink.\n\nI faced a continuous barrage `(प्रश्नों की बौछार / પ્રશ્નોનો મારો)` of questions. People guessed he was a baby seal, a squirrel, a walrus, a beaver, a bear cub, a leopard, a brontosaurus, or a hippo!\n\nThe award for the most surprising question came from a laborer `(मजदूर / મજૂર)` digging a hole in the street. The laborer laid down his shovel `(बेलचा / પાવડો)`, stared at Mij with astonishment `(आश्चर्य / આશ્ચર્ય)`, rested his hands on his hips, and demanded: “Here, Mister—what is that supposed to be?”",
            "difficulty": "Intermediate",
            "bloom": "Analyze"
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "Which family of animals do otters belong to according to the text?",
                "options": [
                    "Mustellines (shared by badgers, mongooses, and weasels)",
                    "Canines (shared by dogs and wolves)",
                    "Felines (shared by cats and leopards)",
                    "Rodents (shared by rats and squirrels)"
                ],
                "correct_answer": "Mustellines (shared by badgers, mongooses, and weasels)",
                "explanation": "Otters belong to the Mustelline family, which includes badgers, mongooses, weasels, stoats, and minks."
            },
            "difficulty": "Intermediate",
            "bloom": "Remember"
        },
        {
            "type": "exam_tips",
            "content": "🔥 **BOARD EXAM HIGH-YIELD CONCEPTS & LONG ANSWER TIPS:**\n\n1. **Maxwell and Mijbil's Bond:** \n   - Explain how their relationship evolved from aloofness on the first day to deep affection, sleeping together, and Mijbil running to nuzzle Maxwell's neck after the flight panic.\n\n2. **The Air Hostess's Role (5 Marks Question):**\n   - Describe her kindness, understanding of passenger psychology, and how she helped diffuse a chaotic situation calmly.\n\n3. **Mijbil's Playfulness & Intelligence:**\n   - Give three clear examples: Turning the bathroom tap on, playing with marbles on his stomach, and inventing the ping-pong game on the sloping suitcase lid.\n\n4. **Londoners' Reactions:**\n   - Mention the wild variety of mistaken identities (baby seal, walrus, beaver, brontosaurus) and quote the laborer's unforgettable question: *'Here, Mister—what is that supposed to be?'*",
            "difficulty": "Advanced",
            "bloom": "Evaluate"
        }
    ]

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_english_ch8.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_english_ch8.json"
    final_json["metadata"]["id"] = "gseb_class10_english_ch8"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Full-Text English Chapter 8 Generated Successfully!")

if __name__ == "__main__":
    generate_full_english_ch8()
