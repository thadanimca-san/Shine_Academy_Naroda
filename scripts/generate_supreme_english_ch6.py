import json
import os

def generate_supreme_english_ch6():
    chapter_id = "ncert_class10_english_ch6"
    title = "Chapter 6: The Hundred Dresses - II"
    
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
        "tags": ["english", "first_flight", "hundred_dresses_2", "board_special", "bilingual"],
        "learning_outcomes": [
            "Understand the themes of forgiveness, regret, and bullying.",
            "Master difficult vocabulary (Contemporaries, Exquisite, Cowardice).",
            "Write a Character Sketch of Wanda, Peggy, and Maddie.",
            "Solve CBSE/State Board HOTS questions related to Wanda's letter and Maddie's guilt."
        ],
        "ai_context": {
            "learning_goal": "Make literature emotional and easy to understand for ESL (English as a Second Language) students. Use Bilingual translations for tough words.",
            "common_misconceptions": [
                "Students think Peggy was purely evil. (Fact: She wasn't, she just didn't realize she was hurting Wanda).",
                "Students confuse Maddie's guilt with Peggy's attitude."
            ]
        }
    }
    
    blocks = []
    
    # ==========================================
    # MODULE 1: INTRODUCTION & HOOK
    # ==========================================
    blocks.append({
        "type": "hook",
        "content": "Have you ever stayed silent when someone was being bullied, and later deeply regretted it? In Part 1, we saw how Wanda Petronski was teased about her 'hundred dresses'. Now, in Part 2, a shocking letter arrives from Wanda's father. Will Peggy and Maddie get a chance to say sorry? Let's uncover this emotional conclusion.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Maddie and Peggy listening as Miss Mason reads the letter from Mr. Petronski.",
        "image_url": "assets/images/eng_ch6_miss_mason_letter.jpg",
        "alt_text": "A teacher reading a letter to a silent, attentive classroom."
    })

    # ==========================================
    # MODULE 2: VOCABULARY & TRANSLATIONS
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "**Master These Difficult Words:**\n1. **Contemporaries (समकालीन / સમકાલીન):** People of the same age or time.\n2. **Exquisite (अति सुंदर / અત્યંત સુંદર):** Extremely beautiful and delicately made.\n3. **Cowardice (कायरता / કાયરતા):** Lack of bravery.\n4. **Amends (क्षतिपूर्ति / સુધારો):** To make up for a wrong action.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    # ==========================================
    # MODULE 3: THE PLOT & SOCRATIC DISCOVERY
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "A letter from Wanda's father, Jan Petronski, shocks the class. He writes that they are moving to a big city where no one will make fun of their funny name (मज़ाक उड़ाना / મજાક ઉડાવવી). \n\nMiss Mason is deeply disappointed. Maddie feels crushed by guilt—she stood silently while Peggy teased Wanda. She decides she must find Wanda and apologize.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Teacher's Secret:** Peggy feels bad too, but she tries to justify her actions by saying her teasing gave Wanda the idea for the dress designs. Maddie, however, takes full moral responsibility. This shows the difference in their character growth!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    # ==========================================
    # MODULE 4: THE FORGIVENESS
    # ==========================================
    blocks.append({
        "type": "diagram",
        "content": "Maddie looking at Wanda's drawing of a blue dress and realizing the face matches her own.",
        "image_url": "assets/images/eng_ch6_maddie_drawing.jpg",
        "alt_text": "A young girl looking emotionally at a drawing of a dress."
    })

    blocks.append({
        "type": "theory",
        "content": "Peggy and Maddie visit Boggins Heights but find the house empty. They write a friendly letter to Wanda instead. \n\nAt Christmas, Wanda writes back. She asks Miss Mason to give the green dress drawing to Peggy and the blue one to Maddie. When Maddie looks closely at the drawing, she realizes Wanda had drawn *her* face! Wanda had forgiven them completely.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    # ==========================================
    # MODULE 5: BOARD EXAM HOTS
    # ==========================================
    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC:** Maddie's Internal Conflict\n\n**Answer Structure:** \n1. **Guilt:** She felt her silence was as bad as Peggy's teasing.\n2. **Fear:** She was poor herself and feared she might be the next target.\n3. **Resolution:** She makes an important decision never to stand by and watch anyone being bullied again. This is her true character transformation.",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_english_ch6.json"
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_english_ch6.json"
    final_json["metadata"]["id"] = "gseb_class10_english_ch6"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Supreme English Chapter 6 Generated Successfully!")

if __name__ == "__main__":
    generate_supreme_english_ch6()
