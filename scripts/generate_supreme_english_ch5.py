import json
import os

def generate_supreme_english_ch5():
    chapter_id = "ncert_class10_english_ch5"
    title = "Chapter 5: The Hundred Dresses - I"
    
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
        "tags": ["english", "first_flight", "hundred_dresses", "board_special", "bilingual"],
        "learning_outcomes": [
            "Understand the impact of bullying and discrimination.",
            "Master difficult vocabulary (Peggy, Maddie, Wanda, Boggins Heights).",
            "Write a perfect Character Sketch of Wanda Petronski.",
            "Solve CBSE/State Board HOTS questions related to Maddie's guilt."
        ],
        "ai_context": {
            "learning_goal": "Make literature emotional and easy to understand for ESL students. Use Bilingual translations for tough words.",
            "common_misconceptions": [
                "Students think Maddie was as bad as Peggy. (Fact: Maddie felt guilty but lacked courage to stop Peggy).",
                "Students misunderstand the meaning of having 'a hundred dresses'."
            ]
        }
    }
    
    blocks = []
    
    # ==========================================
    # MODULE 1: INTRODUCTION & HOOK
    # ==========================================
    blocks.append({
        "type": "hook",
        "content": "Have you ever been teased for wearing the same clothes every day or having a strange name? Meet Wanda Petronski, a quiet girl who sits in the corner of Room Thirteen. Every day, the most popular girls tease her, asking how many dresses she has. Her answer? 'A hundred.' But she always wears the same faded blue dress. Let's uncover the truth behind Wanda's hundred dresses.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Wanda Petronski standing alone in the schoolyard while Peggy and Maddie look at her.",
        "image_url": "assets/images/eng_ch5_wanda_alone.jpg",
        "alt_text": "A quiet girl standing alone while two other girls whisper about her."
    })

    # ==========================================
    # MODULE 2: VOCABULARY & TRANSLATIONS
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "**Master These Difficult Words:**\n1. **Scuffling of feet (पैरों की घसीटने की आवाज़ / પગ ઘસડવાનો અવાજ):** Noisy dragging movements of feet on the ground.\n2. **Inseparable (अभिन्न / ન છૂટા પાડી શકાય તેવા):** People who are always together (like Peggy and Maddie).\n3. **Stolidly (भावहीन होकर / લાગણીવિહીન રીતે):** Showing little or no emotion.\n4. **Exquisite (अति सुंदर / ખૂબ સુંદર):** Extremely beautiful and delicately made.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    # ==========================================
    # MODULE 3: THE PLOT & SOCRATIC DISCOVERY
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "Wanda came from Boggins Heights, a poor neighborhood, and her shoes were always covered in dry mud. Peggy, the most popular girl, started the 'dresses game' to mock Wanda. Maddie, Peggy's best friend, was also poor and wore hand-me-down clothes. She felt uncomfortable when Peggy teased Wanda, fearing she might be the next target.\n\nDespite the teasing, Wanda calmly claimed she had a hundred dresses all lined up in her closet.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Teacher's Secret:** Maddie wanted to write a note to Peggy to stop teasing Wanda. But she tore it up because she was afraid of losing Peggy's friendship and becoming the new target. This shows how peer pressure makes people stay silent against bullying.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    # ==========================================
    # MODULE 4: THE REVELATION
    # ==========================================
    blocks.append({
        "type": "diagram",
        "content": "Room Thirteen filled with beautiful drawings of a hundred different dresses.",
        "image_url": "assets/images/eng_ch5_hundred_drawings.jpg",
        "alt_text": "A classroom decorated with many colorful and beautiful dress designs."
    })

    blocks.append({
        "type": "theory",
        "content": "The school held a drawing and coloring contest. Everyone expected Peggy to win the girls' medal. But when they entered Room Thirteen, they were amazed. The room was filled with a hundred beautiful, exquisite designs of dresses!\n\nThe winner was Wanda Petronski. Those were her 'hundred dresses'. However, Wanda was not there to receive her medal; she had been absent for days.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    # ==========================================
    # MODULE 5: BOARD EXAM HOTS
    # ==========================================
    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC:** Character Contrast: Peggy vs. Maddie\n\n**Answer Structure:** \n1. **Peggy:** Popular, pretty, but thoughtless. She didn't think teasing Wanda was cruel because Wanda claimed to have 100 dresses while wearing only one.\n2. **Maddie:** Poor herself, highly sensitive, and empathetic. She felt guilty about the teasing but lacked the courage to stand up to her best friend due to peer pressure.\n3. **The Core Lesson:** Silent bystanders (like Maddie) suffer from guilt and are part of the bullying problem.",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_english_ch5.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_english_ch5.json"
    final_json["metadata"]["id"] = "gseb_class10_english_ch5"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Supreme English Chapter 5 Generated Successfully!")

if __name__ == "__main__":
    generate_supreme_english_ch5()
