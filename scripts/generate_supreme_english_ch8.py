import json
import os

def generate_supreme_english_ch8():
    chapter_id = "ncert_class10_english_ch8"
    title = "Chapter 8: Mijbil the Otter (First Flight)"
    
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
        "tags": ["english", "first_flight", "mijbil_the_otter", "board_special", "bilingual"],
        "learning_outcomes": [
            "Understand the bond between humans and unusual pets.",
            "Master the difficult vocabulary (Otter, Appalling, Thraldom).",
            "Write a perfect Character Sketch of Maxwell and Mijbil.",
            "Solve CBSE/State Board HOTS questions related to the flight to London."
        ],
        "ai_context": {
            "learning_goal": "Make literature emotional and easy to understand for ESL (English as a Second Language) students. Use Bilingual translations for tough words.",
            "common_misconceptions": [
                "Students think Mijbil was a common pet like a dog or cat. (Fact: He was an otter!).",
                "Students misspell 'Mijbil' and 'Camusfearna' in exams."
            ]
        }
    }
    
    blocks = []
    
    # ==========================================
    # MODULE 1: INTRODUCTION & HOOK
    # ==========================================
    blocks.append({
        "type": "hook",
        "content": "Most people keep dogs, cats, or maybe parrots as pets. But what if you decided to keep a wild river animal? In this hilarious and touching story, the author decides to keep an **Otter (ऊदबिलाव / જળબિલાડી)**! Let's follow the chaotic and loving journey of Maxwell and his unusual pet, Mijbil.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Maxwell playing with Mijbil the otter in the bathtub.",
        "image_url": "assets/images/eng_ch8_mijbil_bathtub.jpg",
        "alt_text": "An otter splashing water playfully inside a bathtub."
    })

    # ==========================================
    # MODULE 2: VOCABULARY & TRANSLATIONS
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "**Master These Difficult Words:**\n1. **Otter (ऊदबिलाव / જળબિલાડી):** A semi-aquatic fish-eating mammal.\n2. **Appalling (भयानक / ભયંકર):** Horrifying or shocking.\n3. **Thraldom (गुलामी / ગુલામી):** The state of being under the control of another person or animal's charm.\n4. **Hostile (शत्रुतापूर्ण / પ્રતિકૂળ):** Unfriendly or aggressive.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    # ==========================================
    # MODULE 3: THE PLOT & SOCRATIC DISCOVERY
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "Maxwell travelled to Basra, Iraq, where two Arabs gifted him an otter. He named him Mijbil. At first, Mijbil was aloof, but soon he became incredibly friendly and obsessed with playing with water (as otters love water). \n\nThe real challenge started when Maxwell had to transport Mijbil by air from Basra to London. British Airways wouldn't allow animals, so he had to book a flight with a different airline that required Mijbil to be packed in a box.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Teacher's Secret:** The flight journey is the most important and comedic part of the chapter! Mijbil tore the box, injured himself, and later escaped in the airplane causing massive panic among the passengers. The brave and kind air hostess helped Maxwell handle the situation.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    # ==========================================
    # MODULE 4: LIFE IN LONDON
    # ==========================================
    blocks.append({
        "type": "diagram",
        "content": "Londoners staring confused at Mijbil while he walks on a leash.",
        "image_url": "assets/images/eng_ch8_mijbil_london.jpg",
        "alt_text": "People on a London street looking confused at a strange animal on a leash."
    })

    blocks.append({
        "type": "theory",
        "content": "In London, Mijbil developed a routine. He would play with toys and balance ping-pong balls on his belly. When Maxwell took him for walks, Londoners couldn't guess what animal he was! They guessed everything from a baby seal, a squirrel, a walrus, to a hippo!\n\n**The Irony:** A completely normal animal in the marshes of Iraq became a mysterious alien creature in the streets of London!",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    # ==========================================
    # MODULE 5: BOARD EXAM HOTS
    # ==========================================
    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC:** The Role of the Air Hostess\n\n**Answer Structure:** \n1. **Compassionate:** She understood Maxwell's love for his pet and allowed him to keep Mijbil on his knee.\n2. **Queen of her kind:** Maxwell called her this because she was extremely supportive during a highly stressful and bloody situation.\n3. **Professional:** She remained calm even when the otter escaped and caused a commotion in the cabin.",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_english_ch8.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_english_ch8.json"
    final_json["metadata"]["id"] = "gseb_class10_english_ch8"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Supreme English Chapter 8 Generated Successfully!")

if __name__ == "__main__":
    generate_supreme_english_ch8()
