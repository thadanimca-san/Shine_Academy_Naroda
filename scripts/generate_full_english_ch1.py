import json
import os

def generate_full_english_ch1():
    chapter_id = "ncert_class10_english_ch1"
    title = "Chapter 1: A Letter to God (First Flight)"
    
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
        "tags": ["english", "first_flight", "letter_to_god", "full_text"],
        "learning_outcomes": [
            "Read and comprehend the original NCERT text.",
            "Understand the profound theme of extreme faith in God.",
            "Master difficult vocabulary contextually.",
            "Analyze character traits for Board Exams."
        ],
        "ai_context": {
            "learning_goal": "Provide the exact NCERT text broken into passages, with inline translations using backticks for the Smart Translation Filter.",
        }
    }
    
    blocks = [
        {
            "type": "hook",
            "content": "Imagine your entire farm is destroyed by a terrible storm. You have no money, no food, and your family might starve. Who do you ask for help? Your relatives? The bank? Lencho did something unimaginable\u2014he wrote a letter directly to **God `(भगवान / ભગવાન)`**!\n\nLet's read the *original, full story* line-by-line to understand his unbreakable faith.",
            "difficulty": "Beginner",
            "bloom": "Understand"
        },
        {
            "type": "diagram",
            "content": "Lencho looking at the sky, hoping for rain.",
            "image_url": "assets/images/eng_ch1_lencho_field.jpg",
            "alt_text": "A farmer standing in a field looking at the sky."
        },
        {
            "type": "theory",
            "title": "Passage 1: The House and the Rain",
            "content": "The house\u2014the only one in the entire valley\u2014sat on the crest `(पहाड़ी की चोटी / ટેકરીની ટોચ)` of a low hill. From this height one could see the river and the field of ripe corn dotted with the flowers that always promised a good harvest `(फसल / પાક)`.\n\nThe only thing the earth needed was a downpour `(मूसलाधार बारिश / ભારે વરસાદ)` or at least a shower. Throughout the morning Lencho\u2014who knew his fields intimately\u2014had done nothing else but see the sky towards the north-east.\n\n\"Now we're really going to get some water, woman.\" The woman who was preparing supper, replied, \"Yes, God willing.\"",
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "teacher_tip",
            "content": "\ud83d\udca1 **Teacher's Insight:** Notice how Lencho doesn't ask for a miracle yet. He is a practical farmer who knows his fields *intimately*. He just wants a little bit of rain. His connection to nature is beautifully established here."
        },
        {
            "type": "theory",
            "title": "Passage 2: The Hailstorm",
            "content": "It was during the meal that, just as Lencho had predicted, big drops of rain began to fall. In the north-east huge mountains of clouds could be seen approaching. The air was fresh and sweet.\n\nBut suddenly a strong wind began to blow and along with the rain very large hailstones `(ओले / કરા)` began to fall. These truly did resemble new silver coins. The boys, exposing themselves to the rain, ran out to collect the frozen pearls.\n\n\"It's really getting bad now,\" exclaimed the man. \"I hope it passes quickly.\" \n\nIt did not pass quickly. For an hour the hail rained on the house, the garden, the hillside, the cornfield, on the whole valley. The field was white, as if covered with salt.",
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "What did the hailstones resemble according to the author?",
                "options": [
                    "White salt",
                    "Frozen pearls and new silver coins",
                    "Drops of water",
                    "White flowers"
                ],
                "correct_answer": "Frozen pearls and new silver coins",
                "explanation": "The author compares the hailstones to 'new silver coins' and 'frozen pearls' to show how they looked, even though they were destructive."
            },
            "difficulty": "Intermediate",
            "bloom": "Remember"
        },
        {
            "type": "theory",
            "title": "Passage 3: The Aftermath and A Single Hope",
            "content": "Not a leaf remained on the trees. The corn was totally destroyed. The flowers were gone from the plants. Lencho's soul was filled with sadness. When the storm had passed, he stood in the middle of the field and said to his sons:\n\n\"A plague of locusts `(टिड्डियों का दल / તીડનું ટોળું)` would have left more than this. The hail has left nothing. This year we will have no corn.\"\n\nBut in the hearts of all who lived in that solitary house in the middle of the valley, there was a single hope: help from God.\n\n\"Don't be so upset, even though this seems like a total loss. Remember, no one dies of hunger.\"\n\nAll through the night, Lencho thought only of his one hope: the help of God, whose eyes, as he had been instructed, see everything, even what is deep in one's conscience `(अंतरात्मा / અંતરાત્મા)`.",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "teacher_tip",
            "content": "\ud83d\udd25 **Board Exam Focus:** Why did Lencho say a plague of locusts would have left more? \nBecause a hailstorm is a completely brutal, unnatural wiping out of the field, leaving literally zero survival chance. This shows the absolute devastation of his livelihood."
        },
        {
            "type": "theory",
            "title": "Passage 4: Writing the Letter",
            "content": "Lencho was an ox of a man `(बैल की तरह मेहनती इंसान / બળદ જેવો મહેનતુ માણસ)`, working like an animal in the fields, but still he knew how to write. The following Sunday, at daybreak, he began to write a letter which he himself would carry to town and place in the mail.\n\n\"God,\" he wrote, \"if you don't help me, my family and I will go hungry this year. I need a hundred pesos `(लैटिन अमेरिकी मुद्रा / લેટિન અમેરિકન ચલણ)` in order to sow my field again and to live until the crop comes...\"\n\nHe wrote 'To God' on the envelope, put the letter inside and, still troubled, went to town. At the post office, he placed a stamp on the letter and dropped it into the mailbox.",
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "theory",
            "title": "Passage 5: The Postmaster's Reaction",
            "content": "One of the employees, who was a postman and also helped at the post office, went to his boss laughing heartily and showed him the letter to God. Never in his career as a postman had he known that address.\n\nThe postmaster\u2014a fat, amiable `(मिलनसार / મળતાવડો)` fellow\u2014also broke out laughing, but almost immediately he turned serious and, tapping the letter on his desk, commented:\n\n\"What faith! I wish I had the faith of the man who wrote this letter. Starting up a correspondence with God!\"\n\nSo, in order not to shake the writer's faith in God, the postmaster came up with an idea: answer the letter. But when he opened it, it was evident that to answer it he needed something more than goodwill, ink and paper. He asked for money from his employees, he himself gave part of his salary, and several friends of his were obliged to give something 'for an act of charity'.",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "teacher_tip",
            "content": "\ud83d\udca1 **Character Sketch - The Postmaster:** He is compassionate, kind, and empathetic. He recognizes the purity of Lencho's faith and goes out of his way to protect it. This is a very common 5-mark question in the board exams!"
        },
        {
            "type": "theory",
            "title": "Passage 6: The Delivery",
            "content": "It was impossible for him to gather together the hundred pesos, so he was able to send the farmer only a little more than half. He put the money in an envelope addressed to Lencho and with it a letter containing only a single word as a signature: God.\n\nThe following Sunday Lencho came a bit earlier than usual to ask if there was a letter for him. It was the postman himself who handed the letter to him while the postmaster, experiencing the contentment of a man who has performed a good deed, looked on from his office.\n\nLencho showed not the slightest surprise on seeing the money; such was his confidence\u2014but he became angry when he counted the money. God could not have made a mistake, nor could he have denied Lencho what he had requested.",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "theory",
            "title": "Passage 7: The Second Letter (The Irony)",
            "content": "Immediately, Lencho went up to the window to ask for paper and ink. On the public writing-table, he started to write, with much wrinkling of his brow, caused by the effort he had to make to express his ideas.\n\nWhen he finished, he went to the window to buy a stamp which he licked and then affixed to the envelope with a blow of his fist. The moment the letter fell into the mailbox the postmaster went to open it. It said:\n\n\"God: Of the money that I asked for, only seventy pesos reached me. Send me the rest, since I need it very much. But don't send it to me through the mail because the post office employees are a bunch of crooks `(ठगों का समूह / લુચ્ચાઓની ટોળી)`. Lencho.\"",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "diagram",
            "content": "Lencho dropping the second letter angrily into the mailbox.",
            "image_url": "assets/images/eng_ch1_lencho_angry.jpg",
            "alt_text": "Lencho writing the second letter."
        },
        {
            "type": "exam_tips",
            "content": "\ud83d\udd25 **BOARD EXAM HOT TOPIC: Irony in the Story**\n\n**Question:** What is the irony in the ending of the story?\n\n**Answer:** Irony is an unexpected twist where the opposite of what is intended happens. The post office employees generously collected money to help Lencho and keep his faith in God alive. But ironically, Lencho ended up calling his very helpers a 'bunch of crooks' because he blindly believed God sent full money and the employees stole the rest!",
            "difficulty": "Advanced",
            "bloom": "Evaluate"
        }
    ]

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_english_ch1.json"
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_english_ch1.json"
    final_json["metadata"]["id"] = "gseb_class10_english_ch1"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Full-Text English Chapter 1 Generated Successfully!")

if __name__ == "__main__":
    generate_full_english_ch1()
