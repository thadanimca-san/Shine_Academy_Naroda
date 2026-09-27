import json
import os

def generate_supreme_english_sup_ch3():
    chapter_id = "ncert_class10_english_sup_ch3"
    title = "Chapter 3: The Midnight Visitor (Footprints Without Feet)"
    
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
        "tags": ["english", "footprints_without_feet", "midnight_visitor", "board_special", "bilingual"],
        "learning_outcomes": [
            "Understand that appearances can be deceptive.",
            "Master difficult vocabulary (Espionage, Authentic, Balcony).",
            "Write a perfect Character Sketch of Ausable.",
            "Solve CBSE/State Board HOTS questions related to Ausable's quick thinking."
        ],
        "ai_context": {
            "learning_goal": "Make literature emotional and easy to understand for ESL (English as a Second Language) students. Use Bilingual translations for tough words.",
            "common_misconceptions": [
                "Students think Ausable fought Max with weapons. (Fact: He used his brain!).",
                "Students misunderstand the significance of the non-existent balcony."
            ]
        }
    }
    
    blocks = []
    
    # ==========================================
    # MODULE 1: INTRODUCTION & HOOK
    # ==========================================
    blocks.append({
        "type": "hook",
        "content": "When you think of a secret agent, you probably imagine a tall, handsome man like James Bond with a gun. But what if a secret agent is short, very fat, and speaks with an American accent in Paris? Meet Ausable! How does this unlikely spy defeat a dangerous enemy with a gun using only his brain? Let's find out in 'The Midnight Visitor'.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Ausable (fat and short) and Fowler (a young writer) entering a dark hotel room.",
        "image_url": "assets/images/eng_sup_ch3_ausable_fowler.jpg",
        "alt_text": "A fat secret agent and a young writer entering a gloomy hotel corridor."
    })

    # ==========================================
    # MODULE 2: VOCABULARY & TRANSLATIONS
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "**Master These Difficult Words:**\n1. **Espionage (जासूसी / જાસૂસી):** The practice of spying or using spies.\n2. **Authentic (प्रामाणिक / અધિકૃત):** Of undisputed origin; genuine.\n3. **Deceive (धोखा देना / છેતરવું):** Cause someone to believe something that is not true.\n4. **Balcony (छज्जा / બાલ્કની):** A platform enclosed by a wall or balustrade on the outside of a building.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    # ==========================================
    # MODULE 3: THE PLOT & SOCRATIC DISCOVERY
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "Fowler, a young writer, meets Ausable, a secret agent, expecting thrilling adventures. Instead, he finds Ausable boring and fat. However, when they enter Ausable's hotel room, they find another secret agent, Max, holding an automatic pistol! Max wants a highly important report concerning some new missiles.\n\nAusable doesn't panic. Instead, he complains angrily to the hotel management about a non-existent **'balcony'** outside his window.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Teacher's Secret:** Ausable was playing a psychological mind game. By acting annoyed about the fake balcony and mentioning that the police were coming, he created a believable trap for Max. Max panicked and jumped out the window, expecting a balcony—but there was none. He fell to his death!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    # ==========================================
    # MODULE 4: THE IRONICAL ENDING
    # ==========================================
    blocks.append({
        "type": "diagram",
        "content": "Max jumping out of the window thinking there is a balcony, while Ausable smiles.",
        "image_url": "assets/images/eng_sup_ch3_max_jumping.jpg",
        "alt_text": "A man with a gun jumping out of a window in panic."
    })

    blocks.append({
        "type": "theory",
        "content": "When there was a sudden knocking at the door, Ausable said it was the police. Terrified, Max jumped out of the window to hide on the 'balcony'—and screamed as he fell from the sixth floor. \n\nThe door opened, and it was just a waiter with drinks Ausable had ordered earlier! Fowler was completely shocked to see how a fat, 'boring' man was actually a genius secret agent.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    # ==========================================
    # MODULE 5: BOARD EXAM HOTS
    # ==========================================
    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC:** Character Sketch of Ausable\n\n**Answer Structure:** \n1. **Deceptive Appearance:** Fat, sluggish, and not looking like a typical secret agent.\n2. **Presence of Mind:** Stayed calm under the pressure of a gun.\n3. **Quick Thinker:** Invented the story of the balcony and the police on the spot.\n4. **Master of Psychology:** Understood Max's fear and manipulated him into jumping out the window.",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_english_sup_ch3.json"
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_english_sup_ch3.json"
    final_json["metadata"]["id"] = "gseb_class10_english_sup_ch3"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Supreme English Supplementary Chapter 3 Generated Successfully!")

if __name__ == "__main__":
    generate_supreme_english_sup_ch3()
