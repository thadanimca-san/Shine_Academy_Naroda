import json
import os

def generate_supreme_english_ch11():
    chapter_id = "ncert_class10_english_ch11"
    title = "Chapter 11: The Proposal (First Flight)"
    
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
        "tags": ["english", "first_flight", "the_proposal", "board_special", "bilingual"],
        "learning_outcomes": [
            "Understand the theme of the play - marriage as an economic alliance.",
            "Master difficult vocabulary (Palpitations, Hypochondriac, Meadows).",
            "Write perfect Character Sketches of Lomov, Natalya, and Chubukov.",
            "Solve CBSE/State Board HOTS questions related to the arguments over property and dogs."
        ],
        "ai_context": {
            "learning_goal": "Make literature emotional and easy to understand for ESL (English as a Second Language) students. Use Bilingual translations for tough words.",
            "common_misconceptions": [
                "Students think it is a romantic play. (Fact: It is actually a farce about economic marriage!).",
                "Students confuse the names of the dogs (Guess and Squeezer)."
            ]
        }
    }
    
    blocks = []
    
    # ==========================================
    # MODULE 1: INTRODUCTION & HOOK
    # ==========================================
    blocks.append({
        "type": "hook",
        "content": "Imagine you go to your neighbor's house to propose to his daughter, but instead of talking about love, you start fighting over a piece of land! And then you fight over whose dog is better! Welcome to **The Proposal (प्रस्ताव / દરખાસ્ત)**, a hilarious Russian play by Anton Chekhov where marriage is more about money than romance.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Lomov arriving at Chubukov's house dressed formally.",
        "image_url": "assets/images/eng_ch11_lomov_arrives.jpg",
        "alt_text": "A man in formal dress arriving at a neighbor's house."
    })

    # ==========================================
    # MODULE 2: VOCABULARY & TRANSLATIONS
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "**Master These Difficult Words:**\n1. **Palpitations (घबराहट / ધબકારા વધવા):** A noticeably rapid, strong, or irregular heartbeat due to agitation.\n2. **Hypochondriac (रोगभ्रमी / રોગભ્રમી):** A person who is abnormally anxious about their health.\n3. **Meadows (घास के मैदान / ઘાસના મેદાનો):** A piece of grassland, especially one used for hay.\n4. **Farce (प्रहसन / પ્રહસન):** A comic dramatic work using buffoonery and horseplay.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    # ==========================================
    # MODULE 3: THE PLOT & SOCRATIC DISCOVERY
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "Ivan Lomov is a wealthy, hypochondriac landowner who visits his neighbor, Stepan Chubukov, to ask for his daughter Natalya's hand in marriage. Chubukov is thrilled. However, when Lomov and Natalya are alone, they start arguing about the ownership of the **Oxen Meadows (ऑक्सन मीडोज़ / ઓક્સન મીડોઝ)** before he can even propose!",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Teacher's Secret:** Chekhov uses this funny situation to make a serious point about Russian society. Rich people married each other to increase their wealth and property, not because they were in love!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    # ==========================================
    # MODULE 4: THE SECOND ARGUMENT & ENDING
    # ==========================================
    blocks.append({
        "type": "diagram",
        "content": "Lomov fainting while arguing with Natalya and Chubukov.",
        "image_url": "assets/images/eng_ch11_lomov_faints.jpg",
        "alt_text": "A man fainting during a heated argument with two other people."
    })

    blocks.append({
        "type": "theory",
        "content": "After Natalya learns he came to propose, she forces her father to bring him back. But guess what? They start arguing AGAIN! This time about whose hunting dog is better: Lomov's **Guess** or Natalya's **Squeezer**. Lomov gets so excited he faints (बेहोश होना / બેહોશ થવું). Fearing Lomov might die before they get married, Chubukov forcefully puts their hands together and blesses them while they are still shouting at each other!",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    # ==========================================
    # MODULE 5: BOARD EXAM HOTS
    # ==========================================
    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC:** Character Sketch of the three main characters\n\n**Answer Structure:** \n1. **Lomov:** A hypochondriac, nervous, argumentative, but looking for an economic alliance.\n2. **Natalya:** Quarrelsome, desperate to get married, possessive about her property and dog.\n3. **Chubukov:** A hypocrite, easily excited, worried about marrying off his grown-up daughter.\n\n**Key Theme:** The play is a **farce** that mocks the fake, materialistic nature of marriages in wealthy families.",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_english_ch11.json"
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_english_ch11.json"
    final_json["metadata"]["id"] = "gseb_class10_english_ch11"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Supreme English Chapter 11 Generated Successfully!")

if __name__ == "__main__":
    generate_supreme_english_ch11()
