import json
import os

def generate_full_english_sup_ch4():
    chapter_id = "ncert_class10_english_sup_ch4"
    title = "Chapter 4: A Question of Trust (Footprints without Feet)"
    
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
        "tags": ["english", "footprints_without_feet", "a_question_of_trust", "full_text", "bilingual"],
        "learning_outcomes": [
            "Read and comprehend the original NCERT text of 'A Question of Trust'.",
            "Understand the themes of deception, irony, and 'honour among thieves'.",
            "Master difficult vocabulary with contextual bilingual translations.",
            "Analyze the characters of Horace Danby and the Lady in Red for Board Exams."
        ],
        "ai_context": {
            "learning_goal": "Provide the exact NCERT story broken into comprehensive passages with inline translations using backticks for the Smart Translation Filter.",
            "common_misconceptions": [
                "Students assume Horace Danby was a career criminal who stole frequently. (Fact: He robbed only one safe per year solely to buy rare books).",
                "Students confuse the lady in red with the actual mistress of Shotover Grange. (Fact: She was a clever rival thief)."
            ]
        }
    }
    
    blocks = [
        {
            "type": "hook",
            "content": "Can a thief be honest? Is there really **'honour among thieves' `(चोरों के बीच सम्मान / ચોરો વચ્ચેની વફાદારી)`**?\n\nMeet Horace Danby—a 50-year-old respectable lock-maker who leads a secret double life. He robs only one safe every year to buy rare, precious books. But during his meticulously planned heist at Shotover Grange, he encounters a mysterious young woman dressed in red who turns his world upside down.\n\nLet's read the *original, complete story* by Victor Canning line-by-line with interactive bilingual vocabulary guidance!",
            "difficulty": "Beginner",
            "bloom": "Understand"
        },
        {
            "type": "diagram",
            "content": "Horace Danby planning his robbery and working on locks.",
            "image_url": "assets/images/eng_sup_ch4_horace_safe.jpg",
            "alt_text": "Horace Danby examining safe blueprints and lock-picking tools."
        },
        {
            "type": "theory",
            "title": "Passage 1: Horace Danby and His Secret Passion",
            "content": "Everyone thought that Horace Danby was a good, respectable `(सम्मानित / પ્રતિષ્ઠિત)` citizen. He was about fifty years old and unmarried, and he lived with a housekeeper `(गृह-प्रबंधिका / ઘરકામ કરનાર)` who worried over his health. In fact, he was usually very well and happy except for attacks of hay fever `(परागज ज्वर / પરાગરજની એલર્જી)` in summer. He made locks and was successful enough at his business to have two assistants. Yes, Horace Danby was good and respectable — but not completely honest.\n\nFifteen years ago, Horace had served his first and only sentence `(सजा / સજા)` in a prison `(जेल / જેલ)` library. He loved rare `(दुर्लभ / દુર્લભ)`, expensive books. So he robbed a safe every year. Each year he planned carefully just what he would do, stole enough to last for twelve months, and secretly bought the books he loved through an agent `(दलाल या प्रतिनिधि / એજન્ટ કે પ્રતિનિધિ)`.",
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "teacher_tip",
            "content": "💡 **Character Insight:** Notice the moral contradiction in Horace Danby. He is a skilled craftsman, runs a legitimate business, and is considered a model citizen. Yet, he justifies breaking the law once a year solely to feed his passion for rare books. He never robs poor people—only wealthy owners of large houses. Does having an intellectual motive make his crime acceptable?"
        },
        {
            "type": "theory",
            "title": "Passage 2: The Plan for Shotover Grange",
            "content": "Now, walking in the bright July sunshine, he felt sure that this year’s robbery `(चोरी / ચોરી)` was going to be as successful as all the others. For two weeks he had been studying the house at Shotover Grange, looking at its rooms, its electric wiring `(बिजली की वायरिंग / ઇલેક્ટ્રિક વાયરિંગ)`, its paths and its garden. This afternoon the two servants `(नौकर / નોકરો)`, who remained in the Grange while the family was in London, had gone to the movies. Horace saw them go, and he felt happy in spite of a little tickle of hay fever in his nose.\n\nHe came out from behind the garden wall, his tools carefully packed in a bag on his back. There were about fifteen thousand pounds `(पौंड - ब्रिटिश मुद्रा / પાઉન્ડ - બ્રિટિશ ચલણ)` worth of jewels in the Grange safe `(तिजोरी / તિજોરી)`. If he sold them one by one, he expected to get at least five thousand, which would be more than enough to buy the three very interesting books coming up for sale in the autumn.",
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "Why did Horace Danby rob only one safe each year?",
                "options": [
                    "To pay off heavy business debts",
                    "To buy rare and expensive books",
                    "To give money away in charity",
                    "To maintain a lavish, extravagant lifestyle"
                ],
                "correct_answer": "To buy rare and expensive books",
                "explanation": "Horace Danby was passionate about collecting rare and expensive books. He robbed one safe each year to get enough money to purchase the books he desired through an agent."
            },
            "difficulty": "Intermediate",
            "bloom": "Remember"
        },
        {
            "type": "theory",
            "title": "Passage 3: Inside the House and the Sudden Sneeze",
            "content": "He had seen the housekeeper hang the key to the kitchen door on a hook outside. He put on a pair of gloves `(दस्ताने / હાથમોજાં)`, took the key, and opened the door. He was always careful not to leave any fingerprints `(उंगलियों के निशान / આંગળીઓના નિશાન)`.\n\nA small dog was lying in the kitchen. It stirred, made a noise, and moved its tail in a friendly way.\n\n\"All right, Sherry,\" Horace said as he passed. All you had to do to keep dogs quiet was to call them by their right names, and show them love.\n\nThe safe was in the drawing room `(बैठक कक्ष / દિવાનખંડ)`, behind a rather poor painting. Horace wondered for a moment whether he should collect pictures instead of books. But they took up too much room; in a small house, books were better.\n\nThere was a great bowl of flowers on the table, and Horace felt his nose tickle. He gave a little sneeze `(छींक / છીંક)` and then put down his bag. He carefully arranged his tools. He had four hours before the servants returned.",
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "teacher_tip",
            "content": "💡 **Literary Clue:** Pay attention to two critical details here:\n1. Horace’s meticulous habit of wearing gloves to avoid leaving fingerprints.\n2. His allergy (hay fever) triggered by the bowl of flowers.\nThese two details become the central turning points of the entire climax!"
        },
        {
            "type": "theory",
            "title": "Passage 4: The Voice in the Doorway",
            "content": "The safe was not going to be hard to open. After all, he had lived with locks and safes all his life. The burglar alarm `(चोरी की चेतावनी देने वाली घंटी / ચોરીની એલાર્મ)` was poorly built. He went into the hall to cut its wires. He came back and sneezed loudly again as the smell of the flowers came to him.\n\nThen he heard a voice say quietly, \"What is it? A cold or hay fever?\"\n\nBefore he could think, Horace said, \"Hay fever,\" and found himself sneezing again.\n\nThe voice went on, \"You can cure it with a special treatment `(इलाज / સારવાર)`, you know, if you find out just what plant gives you the disease. I think you’d better see a doctor, if you’re serious about your work. I heard you from top of the house just now.\"\n\nHorace looked up. Standing in the doorway was a young, pretty woman, dressed in red. She walked to the fireplace and straightened the ornaments `(सजावटी सामान / સુશોભનની વસ્તુઓ)` there.\n\n\"Down, Sherry,\" she said. \"Anyone would think I’d been away for a month!\" She smiled at Horace, and went on, \"However, I came back just in time, though I didn’t expect to meet a burglar `(सेंधमार चोर / ઘરફોડ ચોર)`.\"",
            "difficulty": "Advanced",
            "bloom": "Understand"
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "How did the young woman in red first alert Horace Danby to her presence?",
                "options": [
                    "She screamed and called for help",
                    "She calmly asked if his sneezing was due to a cold or hay fever",
                    "She pointed a pistol at him from behind",
                    "She ordered the dog Sherry to attack him"
                ],
                "correct_answer": "She calmly asked if his sneezing was due to a cold or hay fever",
                "explanation": "The lady in red spoke in a calm, quiet voice from the doorway, inquiring whether his sneezing was caused by a cold or hay fever."
            },
            "difficulty": "Intermediate",
            "bloom": "Remember"
        },
        {
            "type": "theory",
            "title": "Passage 5: The Clever Psychological Game",
            "content": "Horace had some hope because she seemed to be amused at meeting him. If he treated her the right way, he might avoid trouble. He replied, \"I didn’t expect to meet one of the family.\"\n\nShe nodded. \"I see what an inconvenience `(असुविधा / અગવડ)` it is for you to meet me. What are you going to do?\"\n\nHorace said, \"My first thought was to run.\"\n\n\"Of course, you could do that. But I would telephone the police and tell them all about you. They’d get you immediately.\"\n\nHorace said, \"I would of course cut the telephone wires first and then...\" He hesitated `(हिचकिचाया / ખચકાયો)`, a smile on his face. \"I would make sure that you could do nothing for some time. A few hours would be enough.\"\n\nShe looked at him seriously. \"You’d hurt me?\"\n\nHorace paused, and then said, \"I think I was trying to frighten `(डराना / ડરાવવું)` you when I said that.\"\n\n\"You didn’t frighten me,\" the lady replied.\n\nHorace said, \"You’d let me go, wouldn’t you? I promise never to do this again. I really mean it. I’m only afraid of prison `(जेल / જેલ)`. I hate the thought of going to prison.\"",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "teacher_tip",
            "content": "💡 **Psychological Warfare:** Notice how skillfully the lady in red manipulates Horace Danby. She maintains complete composure, neither panicking nor shouting. She immediately identifies his greatest weakness—his terror of *prison*—and uses it to make him compliant and desperate to earn her mercy."
        },
        {
            "type": "theory",
            "title": "Passage 6: The Trap Closes",
            "content": "She was silent, watching him closely. Then she said, \"You are really afraid of going to prison, aren’t you?\"\n\nShe came over to him shaking her head. \"I have always liked the wrong kind of people.\"\n\nShe picked up a silver box from the table and took a cigarette from it. Horace, eager to please her and seeing that she might help him, took off his gloves `(दस्ताने / હાથમોજાં)` and handed her his cigarette lighter.\n\n\"You’ll let me go?\" he asked, holding the lighter towards her.\n\n\"Yes, if you’ll do something for me.\"\n\n\"Anything you say.\"\n\n\"Before we went to London, I promised my husband to take my jewels `(गहने / ઘરેણાં)` to our bank. But I left them here in the safe. I want to wear them to a party tonight, so I came down to get them, but...\"\n\nHorace smiled. \"You’ve forgotten the numbers to open the safe, haven’t you?\"\n\n\"Yes,\" laughed the young lady.\n\n\"Just leave it to me and you’ll have them within an hour. But I’ll have to break your safe.\"\n\n\"Don’t worry about that,\" she said. \"My husband won’t be back for a month, and I’ll have the safe mended by that time.\"",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "Why did Horace Danby remove his gloves in front of the lady in red?",
                "options": [
                    "To flick his lighter and light her cigarette to please her",
                    "His hands were sweating due to the summer heat",
                    "Because the safe lock could only be picked with bare hands",
                    "To prove that he did not have any hidden weapons"
                ],
                "correct_answer": "To flick his lighter and light her cigarette to please her",
                "explanation": "Desperate to win her goodwill so she would let him go, Horace took off his gloves to offer a flame from his cigarette lighter."
            },
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "theory",
            "title": "Passage 7: Betrayal and The Ironical Climax",
            "content": "And within an hour Horace had opened the safe, given her the jewels, and gone happily away, believing he was safe from the law.\n\nFor two days he kept his promise to the kind young lady. On the morning of the third day, however, he thought of the books he wanted and he knew he would have to look for another safe. But he never got the chance to begin his plan.\n\nBy noon a policeman had arrested him for the jewel robbery `(डकैती / ચોરી)` at Shotover Grange.\n\nHis fingerprints `(उंगलियों के निशान / આંગળીઓના નિશાન)`, for he had opened the safe without gloves, were all over the room, and no one believed him when he said that the wife of the owner of the house had asked him to open the safe for her.\n\nThe wife herself was a grey-haired `(सफेद बालों वाली / સફેદ વાળવાળી)`, sharp-tongued `(कड़वी जुबान वाली / તીખી વાણીવાળી)` woman of sixty. She said that the story was nonsense `(बकवास / બકવાસ)!`\n\nHorace is now the assistant librarian in the prison `(जेल / જેલ)`. He often thinks of the charming `(आकर्षक / આકર્ષક)`, clever young lady who was in the same profession as he was, and who had tricked him completely.\n\nHe gets very angry when anyone talks about 'honour among thieves' `(चोरों के बीच सम्मान या वफ़ादारी / ચોરો વચ્ચેનું સન્માન કે વફાદારી)`.",
            "difficulty": "Advanced",
            "bloom": "Evaluate"
        },
        {
            "type": "diagram",
            "content": "The lady in red smiling triumphantly with jewels while Horace is in prison library.",
            "image_url": "assets/images/eng_sup_ch4_lady_red.jpg",
            "alt_text": "The lady in red holding jewellery with a cunning smile."
        },
        {
            "type": "exam_tips",
            "content": "🔥 **BOARD EXAM HOT TOPIC: Themes, Character Analysis & Irony**\n\n**1. The Central Irony of the Story:**\n• **Expectation:** Horace Danby considered himself a master burglar who took every precaution (studied the house for 2 weeks, wore gloves, timed the servants).\n• **Reality:** He was completely outsmarted by a younger, bolder, and more cunning thief who pretended to be the mistress of Shotover Grange.\n• **The Ultimate Irony:** Horace did the hard work of cracking the safe and breaking the law, but walked away empty-handed only to be arrested, while the real thief walked away with all the jewels scot-free!\n\n**2. Why does Horace get furious at 'Honour among Thieves'?**\n• The ancient proverb suggests that even criminals adhere to a code of mutual respect and integrity towards one another.\n• Horace felt deeply betrayed because a fellow thief took advantage of his courtesy and trust, exploiting his fear of prison to make him open the safe and leave his fingerprints behind.\n\n**3. Key Character Contrasts:**\n• **Horace Danby:** Meticulous, naive, non-violent, fearful of prison, blinded by his desire to avoid trouble.\n• **The Lady in Red:** Highly confident, quick-witted, master manipulator, composed under pressure, opportunistic.",
            "difficulty": "Advanced",
            "bloom": "Evaluate"
        }
    ]

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_english_sup_ch4.json"
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_english_sup_ch4.json"
    final_json["metadata"]["id"] = "gseb_class10_english_sup_ch4"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Full-Text English Supplementary Chapter 4 Generated Successfully!")

if __name__ == "__main__":
    generate_full_english_sup_ch4()
