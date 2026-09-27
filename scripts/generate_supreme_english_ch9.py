import json
import os

def generate_supreme_english_ch9():
    chapter_id = "ncert_class10_english_ch9"
    title = "Chapter 9: Madam Rides the Bus (First Flight)"
    
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
        "tags": ["english", "first_flight", "madam_rides_the_bus", "board_special", "bilingual"],
        "learning_outcomes": [
            "Understand Valli's meticulous planning and determination.",
            "Master difficult vocabulary (Fascinating, Overwhelming, Excursion).",
            "Write a perfect Character Sketch of Valli.",
            "Analyze the theme of life and death as experienced by Valli."
        ],
        "ai_context": {
            "learning_goal": "Make literature emotional and easy to understand for ESL (English as a Second Language) students. Use Bilingual translations for tough words.",
            "common_misconceptions": [
                "Students think Valli was just a stubborn child. (Fact: She was highly organized and mature for her age!)."
            ]
        }
    }
    
    blocks = []
    
    # ==========================================
    # MODULE 1: INTRODUCTION & HOOK
    # ==========================================
    blocks.append({
        "type": "hook",
        "content": "Have you ever wanted something so badly that you planned every single detail to get it? Meet Valli, an eight-year-old girl whose biggest dream was simply to ride the bus that passed her village! Let's explore her fascinating and touching journey.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Valli standing at her doorway, looking longingly at the bus.",
        "image_url": "assets/images/eng_ch9_valli_doorway.jpg",
        "alt_text": "An eight-year-old girl watching a bus on the street."
    })

    # ==========================================
    # MODULE 2: VOCABULARY & TRANSLATIONS
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "**Master These Difficult Words:**\n1. **Fascinating (आकर्षक / આકર્ષક):** Extremely interesting.\n2. **Overwhelming (अत्यधिक / ખૂબ જ વધારે):** Very strong in effect or large in amount.\n3. **Excursion (छोटी यात्रा / ટૂંકી મુસાફરી):** A short journey or trip.\n4. **Haughty (घमंडी / ઘમંડી):** Arrogant and superior.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    # ==========================================
    # MODULE 3: THE PLOT & SOCRATIC DISCOVERY
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "Valli carefully saved every coin she could, resisting the temptation to buy toys or peppermints. She found out the bus fare was 30 paise one way, and the trip to town took 45 minutes. \n\nOne afternoon, she successfully got on the bus. The conductor playfully called her 'Madam' because she acted like a confident adult. She enjoyed the view of the canal, palm trees, and a young cow running playfully in front of the bus.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Teacher's Secret:** The conductor calling her 'Madam' highlights Valli's mature behavior. Despite being eight, she paid her own fare and refused his help, showing strong independence.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    # ==========================================
    # MODULE 4: THE REALIZATION OF LIFE AND DEATH
    # ==========================================
    blocks.append({
        "type": "diagram",
        "content": "Valli looking out of the bus window at a dead cow by the roadside.",
        "image_url": "assets/images/eng_ch9_dead_cow.jpg",
        "alt_text": "A sad girl looking at a lifeless cow from a bus window."
    })

    blocks.append({
        "type": "theory",
        "content": "On her return journey, the excitement vanished. Valli saw the same young cow lying dead by the roadside, struck by a fast-moving vehicle. \n\nThe memory of the dead cow haunted her, damping her enthusiasm. This was her first encounter with the harsh reality of death, transforming her from an innocent child to a more mature individual who understood the fragility of life.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    # ==========================================
    # MODULE 5: BOARD EXAM HOTS
    # ==========================================
    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC:** Character Sketch of Valli\n\n**Answer Structure:** \n1. **Determined and Planner:** Saved money meticulously for months.\n2. **Independent:** Refused help from the conductor and an elderly lady.\n3. **Mature Observer:** Understood the deep meaning of life and death by observing the cow.\n4. **Confident:** Handled herself well among adults without fear.",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_english_ch9.json"
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_english_ch9.json"
    final_json["metadata"]["id"] = "gseb_class10_english_ch9"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Supreme English Chapter 9 Generated Successfully!")

if __name__ == "__main__":
    generate_supreme_english_ch9()
