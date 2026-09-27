import json
import os

def generate_supreme_english_ch4():
    chapter_id = "ncert_class10_english_ch4"
    title = "Chapter 4: From the Diary of Anne Frank (First Flight)"
    
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
        "tags": ["english", "first_flight", "anne_frank", "board_special", "bilingual"],
        "learning_outcomes": [
            "Understand the historical context of the Holocaust and Anne Frank's life.",
            "Master the difficult vocabulary (Chatterbox, Incorrigible, Quaking).",
            "Write a perfect Character Sketch of Anne Frank.",
            "Understand the relationship between Anne and Mr. Keesing."
        ],
        "ai_context": {
            "learning_goal": "Make literature emotional and easy to understand for ESL (English as a Second Language) students. Use Bilingual translations for tough words.",
            "common_misconceptions": [
                "Students think the diary was written after the war. (Fact: It was written while hiding!).",
                "Students misunderstand Mr. Keesing's character as merely strict rather than a teacher with a sense of humor."
            ]
        }
    }
    
    blocks = []
    
    # ==========================================
    # MODULE 1: INTRODUCTION & HOOK
    # ==========================================
    blocks.append({
        "type": "hook",
        "content": "Have you ever felt that no one understands you? Imagine hiding in a secret room for two years, unable to step outside, with only a diary as your true friend. Meet Anne Frank, a 13-year-old girl who poured her heart into a red-checked diary she named **'Kitty' (किट्टी / કિટી)**. Let's explore her world!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Anne Frank writing in her diary in the secret annex.",
        "image_url": "assets/images/eng_ch4_anne_writing.jpg",
        "alt_text": "A young girl writing in a diary with a thoughtful expression."
    })

    # ==========================================
    # MODULE 2: VOCABULARY & TRANSLATIONS
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "**Master These Difficult Words:**\n1. **Chatterbox (बातूनी / વાતોડિયું):** A person who talks a lot.\n2. **Incorrigible (जिसे सुधारा न जा सके / ન સુધારી શકાય તેવું):** Something that cannot be corrected or changed.\n3. **Quaking (कांपना / ધ્રૂજવું):** Shaking with fear or nervousness.\n4. **Confide (रहस्य बताना / વિશ્વાસ રાખીને ખાનગી વાત કહેવી):** To tell personal secrets to someone you trust.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    # ==========================================
    # MODULE 3: THE PLOT & SOCRATIC DISCOVERY
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "Anne felt that **'paper has more patience than people'**. Though she had a loving family and friends, she didn't have a *true* friend to share her deepest feelings with. So, she made her diary her best friend.\n\nIn her diary, she writes about her math teacher, Mr. Keesing. He was annoyed because Anne talked too much in class. As a punishment, he gave her extra homework to write essays on being a 'Chatterbox'.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Teacher's Secret:** Anne didn't just write a boring essay! She wrote a clever argument that talking is a student's trait and she inherited it from her mother. Mr. Keesing was impressed by her smart response!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    # ==========================================
    # MODULE 4: THE IRONICAL ENDING
    # ==========================================
    blocks.append({
        "type": "diagram",
        "content": "Mr. Keesing reading Anne's poem about the ducklings.",
        "image_url": "assets/images/eng_ch4_mr_keesing_reading.jpg",
        "alt_text": "A teacher reading a poem and laughing in a classroom."
    })

    blocks.append({
        "type": "theory",
        "content": "After three essays, Mr. Keesing asked her to write on *'Quack, Quack, Quack, Said Mistress Chatterbox'*. Anne, with the help of her friend Sanne, wrote it in verse (a poem). \n\nIt was a funny poem about a father swan who bit his three baby ducklings to death because they quacked too much. Mr. Keesing took the joke the right way. After that, he never gave her extra homework and even started making jokes in class himself!",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    # ==========================================
    # MODULE 5: BOARD EXAM HOTS
    # ==========================================
    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC:** Character Sketch of Anne Frank\n\n**Answer Structure:** \n1. **Intelligent & Witty:** Wrote clever arguments in her punishment essays.\n2. **Lonely but Surrounded by People:** Had family and friends, but craved a 'true' confidante (her diary, Kitty).\n3. **Talkative:** Her defining trait in class, which caused conflict with Mr. Keesing.\n4. **Mature:** Her thoughts about paper having more patience than people show deep maturity for a 13-year-old.",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_english_ch4.json"
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_english_ch4.json"
    final_json["metadata"]["id"] = "gseb_class10_english_ch4"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Supreme English Chapter 4 Generated Successfully!")

if __name__ == "__main__":
    generate_supreme_english_ch4()
