import json
import os

def generate_full_english_sup_ch3():
    chapter_id = "ncert_class10_english_sup_ch3"
    title = "Chapter 3: The Midnight Visitor (Footprints Without Feet)"
    
    metadata = {
        "id": chapter_id,
        "title": title,
        "subtitle": "Interactive Full-Text Reading",
        "subject": "English Supplementary",
        "grade": "10",
        "board": "NCERT/CBSE",
        "curriculum": ["Universal"],
        "language": "English/Hindi/Gujarati (Bilingual)",
        "difficulty": "Advanced",
        "estimated_minutes": 120,
        "version": "4.0.0-FULL-TEXT",
        "author": "Antigravity Supreme Intelligence",
        "reviewed_by": "Chief Academic Architect",
        "tags": ["english", "footprints_without_feet", "midnight_visitor", "full_text", "bilingual"],
        "learning_outcomes": [
            "Read and comprehend the original unabridged text of 'The Midnight Visitor'.",
            "Analyze how Ausable uses wit, composure, and psychological deception instead of physical force.",
            "Master rich vocabulary and literary expressions with inline Hindi and Gujarati translations.",
            "Excel in CBSE and State Board character sketch and theme-based analysis questions."
        ],
        "ai_context": {
            "learning_goal": "Provide the exact NCERT text broken into passages, with inline translations using backticks for the Smart Translation Filter.",
        }
    }
    
    blocks = [
        {
            "type": "hook",
            "content": "Imagine stepping into the room of a top secret agent, expecting high-tech gadgets, sleek black suits, and deadly weapons like James Bond—only to meet a very fat, slow-moving man who speaks with a wheezy American drawl in a gloomy French hotel! Fowler was utterly disappointed. But when they open the door, an armed assassin is standing in the dark with an automatic pistol pointed straight at them!\n\nHow does this unarmed, overweight secret agent eliminate a dangerous rival without firing a single bullet or throwing a punch? Let's read the *complete, unabridged story* line-by-line to witness one of the most brilliant psychological masterstrokes in detective fiction!",
            "difficulty": "Beginner",
            "bloom": "Understand"
        },
        {
            "type": "diagram",
            "content": "Ausable, a fat secret agent, walking down a gloomy corridor with Fowler, a young romantic writer.",
            "image_url": "assets/images/eng_sup_ch3_ausable_fowler.jpg",
            "alt_text": "A fat secret agent and a young writer entering a gloomy hotel corridor."
        },
        {
            "type": "theory",
            "title": "Passage 1: A Secret Agent Who Didn't Look the Part",
            "content": "Ausable did not fit any description of a secret agent Fowler had ever read. Following him down the musty `(सीलन भरा, बदबूदार / વાસી, ગંધાતું)` corridor `(गलियारा / પરસાળ, ગલિયારો)` of the gloomy `(अंधकारमय, उदास / અંધકારમય, ઉદાસ)` French hotel where Ausable had a room, Fowler felt let down `(निराश हुआ / નિરાશ થયો)`. It was a small room, on the sixth and top floor, and scarcely `(मुश्किल से / ભાગ્યે જ)` a setting for a romantic adventure.\n\nAusable was, for one thing, fat. Very fat. And then there was his accent `(बोलने का लहजा / ઉચ્ચારણની રીત)`. Though he spoke French and German passably `(कामचलाऊ रूप से / ચલાવી શકાય તેવું)`, he had never altogether lost the American accent he had brought to Paris from Boston twenty years ago.\n\n\"You are disappointed `(निराश / નિરાશ)`,\" Ausable said wheezily `(भारी सांस लेते हुए / હાંફતાં હાંફતાં)` over his shoulder. \"You were told that I was a secret agent, a spy `(जासूस / જાસૂસ)`, dealing in espionage `(जासूसी / જાસૂસી)` and danger. You wished to meet me because you are a writer, young and romantic `(काल्पनिक / કાલ્પનિક)`. You envisioned `(कल्पना की थी / કલ્પના કરી હતી)` mysterious figures in the night, the crack of pistols, drugs in the wine.\"",
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "teacher_tip",
            "content": "💡 **Literary Contrast & Irony:** The author, Robert Arthur, sets up an immediate contrast between stereotype and reality. Pop culture depicts spies as athletic, glamorous, and dangerous. Ausable is physically sloppy, overweight, and mundane. This subversion makes the climax far more impactful!"
        },
        {
            "type": "theory",
            "title": "Passage 2: The Anticipation of a Historic Report",
            "content": "\"Instead, you have spent a dull evening in a French music hall with a sloppy `(लापरवाह, ढीला-ढाला / ગંદો, અસ્તવ્યસ્ત)` fat man who, instead of having messages slipped into his hand by dark-eyed beauties, gets only a prosaic `(नीरस, साधारण / સામાન્ય, નીરસ)` telephone call making an appointment in his room. You have been bored `(ऊब गए / કંટાળી ગયા)!\" The fat man chuckled `(दबी हंसी हंसा / ધીમેથી હસ્યો)` to himself as he unlocked the door of his room and stood aside to let his frustrated `(हताश / નિરાશ)` guest enter.\n\n\"Cheer up, my young friend,\" Ausable said. \"Presently you will see a paper, a quite important paper for which several men and women have risked their lives, come to me. Some day soon that paper may well affect the course of history. In that thought is drama, is there not?\"\n\nAs he spoke, Ausable closed the door behind him. Then he switched on the light.",
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "Why was Fowler disappointed upon meeting Ausable?",
                "options": [
                    "Ausable refused to share any secrets with him",
                    "Ausable was fat, sloppy, and lived in a gloomy hotel instead of being a glamorous spy",
                    "Ausable could not speak French or German",
                    "Ausable did not show up for their appointment"
                ],
                "correct_answer": "Ausable was fat, sloppy, and lived in a gloomy hotel instead of being a glamorous spy",
                "explanation": "Fowler was a romantic young writer who expected a secret agent to be mysterious, fit, and dramatic, but Ausable was very fat and lived in a cheap, gloomy room."
            },
            "difficulty": "Intermediate",
            "bloom": "Remember"
        },
        {
            "type": "theory",
            "title": "Passage 3: The Midnight Intruder - Max with a Pistol",
            "content": "And as the light came on, Fowler had his first authentic `(असली, सच्चा / સાચો, અસલી)` thrill `(रोमांच / રોમાંચ)` of the day. For halfway across the room, a man stood with a small automatic pistol `(स्वचालित पिस्तौल / સ્વચાલિત પિસ્તોલ)` in his hand.\n\nAusable blinked a few times.\n\n\"Max,\" he wheezed `(धीमी आवाज में कहा / ધીમા સાદે બોલ્યો)`, \"you gave me a start `(चौंका दिया / ચોંકાવી દીધો)`. I thought you were in Berlin. What are you doing here in my room?\"\n\nMax was slender `(पतला-दुबला / પાતળો)`, a little less than tall, with a face that suggested slightly the crafty `(चालाक, धूर्त / કપટી, ચાલાક)`, pointed countenance `(चेहरा, मुखाकृति / ચહેરો)` of a fox. There was about him—aside from the gun—nothing especially menacing `(डरावना, खतरनाक / ડરામણું, ભયજનક)`.\n\n\"The report,\" he murmured `(फुसफुसाया / ગણગણ્યો)`. \"The report that is being brought to you tonight concerning some new missiles `(प्रक्षेप्यास्त्र, मिसाइल / મિસાઇલ)`. I thought I would take it from you. It will be safer in my hands than in yours.\"",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "teacher_tip",
            "content": "💡 **Character Contrast:** Look at how Max is described: slender, fox-like, crafty, and holding a weapon. Yet notice Ausable's reaction—he doesn't panic, sweat, or yell. He calmly blinks and speaks softly. A calm mind under deadly pressure is a true master's superpower."
        },
        {
            "type": "theory",
            "title": "Passage 4: The Tale of the Annoying Balcony",
            "content": "Ausable moved to an armchair and sat down heavily. \"I’m going to raise the devil `(हंगामा खड़ा करना / ભારે વિરોધ કરવો)` with the management this time, and you can bet on it,\" he said grimly `(गंभीरता से / ગંભીરતાપૂર્વક)`. \"This is the second time in a month that somebody has got into my room through that nuisance `(मुसीबत, सिरदर्द / મુશ્કેલી, કનડગત)` of a balcony `(छज्जा, बालकनी / બાલ્કની)`!\"\n\nFowler’s eyes went to the single window of the room. It was an ordinary window, against which now the night was pressing blackly.\n\n\"Balcony?\" Max said, with a rising inflection `(आश्चर्य से स्वर उठाते हुए / અવાજનો ચડાવ-ઉતાર)`. \"No, I had a passkey `(मास्टर चाबी / માસ્ટર ચાવી)`. I did not know about the balcony. It might have saved me some trouble had I known.\"\n\n\"It’s not my balcony,\" Ausable said with extreme irritation `(अत्यधिक चिढ़ / ખૂબ જ ચીડ)`. \"It belongs to the next apartment.\" He glanced explanatorily `(समझाते हुए / સમજાવતાં)` at Fowler. \"You see,\" he said, \"this room used to be part of a large unit, and the next room—through that door there—used to be the living room. It had the balcony, which extends under my window now. Anyone can get onto it from the empty room two doors down—and somebody did, last month. The management promised to block it off `(बंद करना / બંધ કરી દેવું)`. But they haven’t.\"",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "How did Ausable describe the origin of the alleged balcony?",
                "options": [
                    "It was built specifically for his room on the sixth floor",
                    "It belonged to the next apartment and extended under his window",
                    "It was a fire escape ladder connected to the roof",
                    "It was a garden terrace built by the French hotel management"
                ],
                "correct_answer": "It belonged to the next apartment and extended under his window",
                "explanation": "Ausable fabricated a detailed, realistic architectural backstory explaining that his room used to be part of a larger unit connected to the balcony of the next room."
            },
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "theory",
            "title": "Passage 5: Waiting for 12:30 & The Sudden Knock",
            "content": "Max looked at Fowler, who was standing stiffly `(अकड़कर / જકડાઈને)` not far from Ausable, and waved the gun with a commanding gesture `(आदेशात्मक इशारा / આદેશ આપતો ઈશારો)`. \"Please sit down,\" he said. \"We have a wait of half an hour, I think.\"\n\n\"Thirty-one minutes,\" Ausable said moodily `(उदासी से / ઉદાસીથી)`. \"The appointment was for twelve-thirty. I wish I knew how you learned about the report, Max.\"\n\nThe little spy smiled evilly `(दुष्टता से / દૂષ્ટતાથી)`. \"And we wish we knew how your people got the report. But no harm has been done. I’ll get it back tonight. What is that? Who is at the door?\"\n\nFowler jumped at the sudden knocking at the door. Ausable just smiled. \"That will be the police,\" he said. \"I thought that so important a paper as the one we are waiting for should have a little extra protection `(सुरक्षा / સુરક્ષા)`. I told them to check on me to make sure everything was all right `(सब ठीक-ठाक / બધું બરાબર)`.\"",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "teacher_tip",
            "content": "💡 **Psychological Warfare:** Ausable plants two seeds of deception in Max's brain:\n1. The physical existence of an easily accessible balcony right outside the window.\n2. An impending mortal threat—the police arriving to check on him.\nBy combining an escape route with extreme panic, Ausable forces Max to take the fatal leap voluntarily!"
        },
        {
            "type": "theory",
            "title": "Passage 6: The Claim of the Police & Max's Panic",
            "content": "Max bit his lip nervously `(घबराहट में / ગભરાટમાં)`. The knocking was repeated.\n\n\"What will you do now, Max?\" Ausable asked. \"If I do not answer the door, they will enter anyway. The door is unlocked. And they will not hesitate `(हिचकिचाएंगे / અચકાશે)` to shoot.\"\n\nMax’s face was black with anger as he backed swiftly towards the window. He swung one leg over the sill `(खिड़की की चौखट / બારીની ફ્રેમ)`.\n\n\"Send them away!\" he warned. \"I will wait on the balcony. Send them away or I’ll shoot and take my chances `(जोखिम उठाऊंगा / જોખમ ઉઠાવીશ)`!\"\n\nThe knocking at the door grew louder, and a voice was raised: \"*Monsieur Ausable! Monsieur Ausable!*\"",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "Why did Max jump out of the window instead of fighting the police?",
                "options": [
                    "He wanted to escape through the street below",
                    "He believed Ausable's story about the balcony and intended to hide there until the police left",
                    "He saw a helicopter waiting to rescue him",
                    "He was pushed out of the window by Fowler"
                ],
                "correct_answer": "He believed Ausable's story about the balcony and intended to hide there until the police left",
                "explanation": "Max completely believed Ausable's convincing lie about the balcony and planned to hide on it while Ausable dismissed the supposed police."
            },
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "theory",
            "title": "Passage 7: The Leap into the Dark",
            "content": "Keeping his body twisted so that his gun still covered the fat man and his guest, the man at the window grasped the frame with his free hand to support himself. Then he swung his other leg over the window sill.\n\nThe doorknob turned. Swiftly Max pushed with his left hand to free himself from the sill and drop into the balcony.\n\nAnd then, as he dropped, he screamed once, shrilly `(तीखी, भयानक चीख के साथ / તીણી, ભયાનક ચીસ સાથે)`.",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "teacher_tip",
            "content": "💡 **Foreshadowing & Sensory Details:** The single shrill scream is the definitive clue that Max hit the ground from the sixth floor. There was no balcony to catch him. Ausable's composure never wavered for a millisecond."
        },
        {
            "type": "theory",
            "title": "Passage 8: The Waiter and the Masterstroke",
            "content": "The door opened, and a waiter stood there with a tray, a bottle and two glasses.\n\n\"Here is the drink you ordered for when you returned, sir,\" he said, and set the tray upon the table, deftly `(कुशलता से, सफाई से / ચપળતાપૂર્વક)` uncorked `(ढक्कन खोला / બૂચ ખોલ્યો)` the bottle, and left the room.\n\nWhite-faced, Fowler stared after him. \"But... but what about the police?\" he stammered `(हकलाया / હકલાયો)`.\n\n\"There were no police,\" Ausable sighed. \"Only Henry, whom I was expecting.\"\n\n\"But won't that man out on the balcony...?\" Fowler began.\n\n\"No,\" said Ausable, \"he won't return. You see, my young friend, there is no balcony `(कोई बालकनी नहीं है / કોઈ બાલ્કની નથી)`.\"",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "Who was actually knocking at the door?",
                "options": [
                    "The Paris Police department",
                    "Henry, the waiter delivering the drinks Ausable had ordered",
                    "The hotel manager coming to inspect the balcony",
                    "Another secret agent from Berlin"
                ],
                "correct_answer": "Henry, the waiter delivering the drinks Ausable had ordered",
                "explanation": "There were never any police; it was simply Henry the waiter delivering the drink Ausable had ordered when entering the hotel."
            },
            "difficulty": "Intermediate",
            "bloom": "Remember"
        },
        {
            "type": "diagram",
            "content": "Max jumping backwards out of the 6th floor hotel window into empty air, while Ausable sits calmly.",
            "image_url": "assets/images/eng_sup_ch3_max_jumping.jpg",
            "alt_text": "A man with a gun dropping out of a window in panic."
        },
        {
            "type": "exam_tips",
            "content": "🔥 **BOARD EXAM MASTERY & CHARACTER SKETCHES**\n\n### 1. Character Sketch of Ausable (5 Marks)\n* **Deceptive Appearance:** Fat, clumsy, speaks with an American accent, lives in a shabby room on the 6th floor of a gloomy French hotel.\n* **Master of Psychology:** Understands human fear and reaction. Concocts a believable lie about a non-existent balcony on the spot.\n* **Unflappable Composure:** Stays remarkably calm when staring down the barrel of Max's gun.\n* **Intellectual Dominance:** Proves that in espionage, brainpower, quick thinking, and presence of mind are far deadlier than physical weapons.\n\n### 2. Character Sketch of Max\n* **Stereotypical Spy:** Slender, fox-like, crafty, overconfident, relies entirely on his firearm.\n* **Gullible & Impulsive:** Lacks observation and critical thinking. Falls hook, line, and sinker for Ausable's fabricated story of the balcony and police knock.\n\n### 3. Core Theme: 'Appearances Can Be Deceptive'\n* Ausable looks like the farthest thing from a hero or spy, yet outwits a dangerous armed rival.\n* The supposed 'police' is merely a polite waiter named Henry.\n* The supposed 'balcony' of refuge is empty air six floors above the ground.",
            "difficulty": "Advanced",
            "bloom": "Evaluate"
        }
    ]

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_english_sup_ch3.json"
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_english_sup_ch3.json"
    final_json["metadata"]["id"] = "gseb_class10_english_sup_ch3"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Full-Text English Supplementary Chapter 3 Generated Successfully!")

if __name__ == "__main__":
    generate_full_english_sup_ch3()
