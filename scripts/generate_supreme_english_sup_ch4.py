import json
import os

def generate_supreme_english_sup_ch4():
    chapter_id = "ncert_class10_english_sup_ch4"
    title = "Chapter 4: A Question of Trust (Footprints without Feet)"
    
    metadata = {
        "id": chapter_id,
        "title": title,
        "subtitle": "The Ultimate Board Exam Mastery Guide",
        "subject": "English",
        "grade": "10",
        "board": "NCERT/CBSE",
        "curriculum": ["Universal"],
        "language": "English/Hindi/Gujarati (Bilingual)",
        "difficulty": "Advanced",
        "estimated_minutes": 120,
        "version": "3.0.0-SUPREME-ENGLISH",
        "author": "Antigravity Supreme Intelligence",
        "reviewed_by": "Chief Academic Architect",
        "tags": ["english", "supplementary", "a_question_of_trust", "board_special", "bilingual"],
        "learning_outcomes": [
            "Understand the theme of trust and deception.",
            "Master the difficult vocabulary (Hay fever, Safe, Burglar).",
            "Write a perfect Character Sketch of Horace Danby.",
            "Solve CBSE/State Board HOTS questions related to the lady in red's trickery."
        ],
        "ai_context": {
            "learning_goal": "Make literature emotional and easy to understand for ESL (English as a Second Language) students. Use Bilingual translations for tough words.",
            "common_misconceptions": [
                "Students think Horace was a completely bad person. (Fact: He was generally good, but had a weakness for rare books).",
                "Students misunderstand who the real culprit was."
            ]
        }
    }
    
    blocks = []
    
    # ==========================================
    # MODULE 1: INTRODUCTION & HOOK
    # ==========================================
    blocks.append({
        "type": "hook",
        "content": "Have you ever heard of a thief who steals only once a year? And that too, just to buy rare and expensive books! Meet Horace Danby, a respected lock-maker who has a secret life as a burglar. But what happens when a master thief is tricked by another master thief? Let's uncover the mystery of 'A Question of Trust'.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Horace Danby carefully opening a safe with his specialized tools.",
        "image_url": "assets/images/eng_sup_ch4_horace_safe.jpg",
        "alt_text": "A man carefully picking the lock of a large iron safe."
    })

    # ==========================================
    # MODULE 2: VOCABULARY & TRANSLATIONS
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "**Master These Difficult Words:**\n1. **Hay fever (परागज ज्वर / પરાગરજની એલર્જી):** An allergy caused by pollen or dust that makes you sneeze.\n2. **Safe (तिजोरी / તિજોરી):** A strong fireproof cabinet for keeping money or valuables.\n3. **Burglar (सेंधमार / ચોર):** A thief who breaks into a building to steal.\n4. **Accomplice (सह अपराधी / સાથીદાર):** A person who helps someone commit a crime.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    # ==========================================
    # MODULE 3: THE PLOT & SOCRATIC DISCOVERY
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "Horace Danby was a good and respectable citizen, but not completely honest. He loved rare books and robbed one safe every year to buy them. He planned his next robbery at a house in Shotover Grange. \n\nWhile trying to open the safe, he started sneezing because of flowers (Hay fever). Suddenly, a beautiful young lady dressed in red appeared. She pretended to be the owner of the house and threatened to call the police!",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Teacher's Secret:** Horace was so scared of going to prison that he completely believed the lady in red. He opened the safe for her without his gloves, leaving his fingerprints everywhere. He thought he was helping the owner, but he was actually being tricked!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    # ==========================================
    # MODULE 4: THE IRONICAL ENDING
    # ==========================================
    blocks.append({
        "type": "diagram",
        "content": "The lady in red smiling holding jewels, while Horace is arrested later.",
        "image_url": "assets/images/eng_sup_ch4_lady_red.jpg",
        "alt_text": "A young lady in a red dress holding a necklace, smiling cunningly."
    })

    blocks.append({
        "type": "theory",
        "content": "Two days later, the police arrested Horace Danby for the jewel robbery at Shotover Grange. His fingerprints were all over the room! \n\nHe told them that the lady of the house asked him to open the safe. But the real owner was a sixty-year-old woman, not the young lady in red. The lady in red was actually another thief! \n\n**The Irony:** Horace Danby, a careful thief, was outsmarted by a younger, cleverer thief. Now he hates the saying 'honour among thieves'.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    # ==========================================
    # MODULE 5: BOARD EXAM HOTS
    # ==========================================
    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC:** Character Sketch of Horace Danby\n\n**Answer Structure:** \n1. **Respectable but not completely honest:** A successful lock-maker but robbed a safe annually.\n2. **Passionate about rare books:** His only motive for stealing was his love for expensive books.\n3. **Meticulous planner:** He studied the house at Shotover Grange for two weeks before the robbery.\n4. **Gullible / Easily tricked:** He was so afraid of prison that he trusted the lady in red blindly and left his fingerprints.",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

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
        
    print("Supreme English Supplementary Chapter 4 Generated Successfully!")

if __name__ == "__main__":
    generate_supreme_english_sup_ch4()
