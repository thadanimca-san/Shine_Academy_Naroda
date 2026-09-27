import json
import os

def generate_supreme_english_ch3():
    chapter_id = "ncert_class10_english_ch3"
    title = "Chapter 3: Two Stories about Flying (First Flight)"
    
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
        "tags": ["english", "first_flight", "two_stories_about_flying", "board_special", "bilingual"],
        "learning_outcomes": [
            "Overcome the fear of trying new things just like the young seagull.",
            "Understand the mystery of the black aeroplane and its pilot.",
            "Master the bilingual vocabulary (Seagull, Ledge, Compass, Radar).",
            "Solve CBSE/State Board HOTS questions related to courage and risk-taking."
        ],
        "ai_context": {
            "learning_goal": "Make literature emotional and easy to understand for ESL (English as a Second Language) students. Use Bilingual translations for tough words.",
            "common_misconceptions": [
                "Students think someone else flew the black aeroplane. (Fact: It is left as a mystery or a hallucination!).",
                "Students confuse the order of events in His First Flight."
            ]
        }
    }
    
    blocks = []
    
    # ==========================================
    # MODULE 1: INTRODUCTION & HOOK
    # ==========================================
    blocks.append({
        "type": "hook",
        "content": "Have you ever been terrified of trying something for the first time? Riding a bicycle? Swimming? In our first story, a young bird is terrified to fly. In our second story, a pilot takes a massive risk by flying his plane into a deadly storm! Let's explore two incredible stories about courage and facing your fears.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "A young seagull standing on the edge of a cliff, looking down at the vast sea, terrified to take its first flight.",
        "image_url": "assets/images/eng_ch3_seagull_ledge.jpg",
        "alt_text": "A young seagull afraid to fly off a cliff."
    })

    # ==========================================
    # MODULE 2: VOCABULARY & TRANSLATIONS
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "**Master These Difficult Words:**\n1. **Seagull (समुद्री पक्षी / સીગલ):** A seabird.\n2. **Ledge (छज्जा / છાજલી):** A narrow horizontal surface projecting from a wall, cliff, or other surface.\n3. **Maddened (पागल हो गया / ગાંડો થઈ ગયો):** Extremely annoyed or angry.\n4. **Compass (दिक्सूचक / હોકાયંત્ર):** An instrument containing a magnetized pointer that shows the direction of magnetic north.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    # ==========================================
    # MODULE 3: THE PLOT & SOCRATIC DISCOVERY
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "**Part I: His First Flight:** The young seagull was afraid to fly. His parents, brothers, and sister had already flown away. He was left alone and starving on the ledge. Finally, maddened by hunger when his mother tempted him with a piece of fish, he dived off the cliff. Fear seized him for a moment, but then his wings spread outwards, and he was flying!\n\n**Part II: The Black Aeroplane:** A pilot was flying his old Dakota aeroplane over France back to England. Suddenly, he saw huge storm clouds looking like black mountains. Instead of going back, he took the risk and flew straight into the storm. His compass and radio stopped working. Then, he saw another 'Black Aeroplane' with no lights on its wings. The pilot of the black aeroplane guided him out of the storm to a safe landing.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Teacher's Secret:** In the second story, when the pilot asks the control center about the other plane, the woman says there was NO OTHER PLANE flying that night! Was it a ghost? An angel? Or the pilot's own subconscious mind pushing him to survive? The author leaves it as an open mystery!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    # ==========================================
    # MODULE 4: THE MYSTERY ENDING
    # ==========================================
    blocks.append({
        "type": "diagram",
        "content": "An old Dakota plane flying through dark storm clouds alongside a mysterious black aeroplane with no lights.",
        "image_url": "assets/images/eng_ch3_black_aeroplane.jpg",
        "alt_text": "Two aeroplanes flying in a dark stormy cloud."
    })

    blocks.append({
        "type": "theory",
        "content": "Both stories teach us a powerful lesson. The young seagull learned that fear is only in the mind and taking the first leap is the hardest part. The pilot learned that sometimes you have to trust your instincts and take a leap of faith to overcome obstacles. **Courage is not the absence of fear, but the triumph over it!**",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    # ==========================================
    # MODULE 5: BOARD EXAM HOTS
    # ==========================================
    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC:** The Mystery of the Black Aeroplane\n\n**Answer Structure:** \n1. **The Situation:** Pilot was caught in a severe storm, instruments failed.\n2. **The Rescue:** A mysterious black plane guided him out.\n3. **The Twist:** Control tower confirmed he was the only plane on the radar.\n4. **Conclusion:** It was likely his own hallucination or inner strength that guided his skills in the panic, rather than a real external entity.",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_english_ch3.json"
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_english_ch3.json"
    final_json["metadata"]["id"] = "gseb_class10_english_ch3"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Supreme English Chapter 3 Generated Successfully!")

if __name__ == "__main__":
    generate_supreme_english_ch3()
