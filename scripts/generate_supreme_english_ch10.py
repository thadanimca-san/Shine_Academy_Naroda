import json
import os

def generate_supreme_english_ch10():
    chapter_id = "ncert_class10_english_ch10"
    title = "Chapter 10: The Sermon at Benares (First Flight)"
    
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
        "tags": ["english", "first_flight", "sermon_at_benares", "board_special", "bilingual"],
        "learning_outcomes": [
            "Understand the profound themes of life, death, and grief.",
            "Master the difficult vocabulary (Sermon, Inscrutable, Lamentation).",
            "Write a perfect Character Sketch of Kisa Gotami and Gautama Buddha.",
            "Solve CBSE/State Board HOTS questions related to Buddha's teachings."
        ],
        "ai_context": {
            "learning_goal": "Make literature emotional and easy to understand for ESL (English as a Second Language) students. Use Bilingual translations for tough words.",
            "common_misconceptions": [
                "Students think Kisa Gotami was crazy. (Fact: She was just a grieving mother unable to accept her child's death).",
                "Students misunderstand the meaning of 'mustard seed' in the story."
            ]
        }
    }
    
    blocks = []
    
    # ==========================================
    # MODULE 1: INTRODUCTION & HOOK
    # ==========================================
    blocks.append({
        "type": "hook",
        "content": "Have you ever lost something or someone you loved dearly? How did you feel? In this chapter, we meet Kisa Gotami, a mother who has lost her only son, and Gautama Buddha, who teaches her the most painful yet beautiful truth about life and death. Let's explore this deeply moving story.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Kisa Gotami weeping over her dead child.",
        "image_url": "assets/images/eng_ch10_kisa_gotami_weeping.jpg",
        "alt_text": "A grieving mother holding her dead child, looking desperate."
    })

    # ==========================================
    # MODULE 2: VOCABULARY & TRANSLATIONS
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "**Master These Difficult Words:**\n1. **Sermon (प्रवचन / પ્રવચન):** A religious or moral talk.\n2. **Inscrutable (रहस्यमय / ગૂઢ):** Impossible to understand or interpret.\n3. **Lamentation (विलाप / વિલાપ):** An expression of great sorrow or weeping.\n4. **Kinsmen (रिश्तेदार / સગાંવહાલાં):** Relatives or family members.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    # ==========================================
    # MODULE 3: THE PLOT & SOCRATIC DISCOVERY
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "Gautama Buddha, born as a prince, gave up his royal life after seeing suffering (a sick man, an aged man, a funeral procession, and a monk). He achieved enlightenment and gave his first sermon at Benares.\n\nMeanwhile, Kisa Gotami's only son died. She carried his dead body to all her neighbors, asking for medicine. People thought she had lost her senses. Finally, someone advised her to go to the Buddha.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Teacher's Secret:** Buddha didn't just tell her that death is common. Instead, he made her realize it herself through a practical task. He asked her to bring a handful of mustard seeds from a house where no one had ever died!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    # ==========================================
    # MODULE 4: THE REALIZATION
    # ==========================================
    blocks.append({
        "type": "diagram",
        "content": "Kisa Gotami asking for mustard seeds from house to house.",
        "image_url": "assets/images/eng_ch10_mustard_seeds.jpg",
        "alt_text": "A woman asking for something at a door, looking tired but hopeful."
    })

    blocks.append({
        "type": "theory",
        "content": "Kisa Gotami went from door to door. People were ready to give her the mustard seeds, but every house had lost a family member—a father, a mother, a son, or a friend. \n\nShe sat by the wayside watching the city lights flicker and fade, realizing that human lives are just like those lights. She finally understood Buddha's lesson: **Death is common to all (मृत्यु सब के लिए समान है / મૃત્યુ સૌ માટે સમાન છે).** Grief and lamentation only bring pain, not peace.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    # ==========================================
    # MODULE 5: BOARD EXAM HOTS
    # ==========================================
    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC:** The Significance of the Mustard Seed\n\n**Answer Structure:** \n1. **The Task:** Buddha asked Kisa to bring a mustard seed from a house with no death.\n2. **The Purpose:** To make her practically realize that death is universal and inescapable.\n3. **The Result:** She learned that grieving does not bring the dead back; acceptance brings peace of mind.\n4. **Conclusion:** It shifted her perspective from selfish grief to universal understanding.",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_english_ch10.json"
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_english_ch10.json"
    final_json["metadata"]["id"] = "gseb_class10_english_ch10"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Supreme English Chapter 10 Generated Successfully!")

if __name__ == "__main__":
    generate_supreme_english_ch10()
