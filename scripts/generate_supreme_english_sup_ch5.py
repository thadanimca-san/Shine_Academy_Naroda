import json
import os

def generate_supreme_english_sup_ch5():
    chapter_id = "ncert_class10_english_sup_ch5"
    title = "Chapter 5: Footprints without Feet (Supplementary)"
    
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
        "tags": ["english", "supplementary", "footprints_without_feet", "board_special", "bilingual"],
        "learning_outcomes": [
            "Understand the concept of a brilliant but lawless scientist.",
            "Master the difficult vocabulary (Invisible, Eccentric, Callous).",
            "Write a perfect Character Sketch of Griffin.",
            "Solve CBSE/State Board HOTS questions related to Griffin's misuse of science."
        ],
        "ai_context": {
            "learning_goal": "Make literature emotional and easy to understand for ESL (English as a Second Language) students. Use Bilingual translations for tough words.",
            "common_misconceptions": [
                "Students think Griffin was a hero because he was brilliant. (Fact: He was lawless and misused his discovery).",
                "Students misspell 'Eccentric' and 'Invisible' in exams."
            ]
        }
    }
    
    blocks = []
    
    # ==========================================
    # MODULE 1: INTRODUCTION & HOOK
    # ==========================================
    blocks.append({
        "type": "hook",
        "content": "Imagine you could become completely invisible! You could go anywhere and do anything without being seen. Would you use this power to help people, or would you use it to steal and cause trouble? Meet Griffin, a brilliant scientist who discovered the secret of invisibility, but chose the wrong path. Let's uncover the thrilling mystery of the muddy footprints that appeared out of nowhere!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Two boys staring in amazement at fresh muddy footprints appearing on the steps, with no one visible making them.",
        "image_url": "assets/images/eng_sup_ch5_muddy_footprints.jpg",
        "alt_text": "Muddy footprints appearing magically on steps."
    })

    # ==========================================
    # MODULE 2: VOCABULARY & TRANSLATIONS
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "**Master These Difficult Words:**\n1. **Invisible (अदृश्य / અદ્રશ્ય):** Unable to be seen.\n2. **Eccentric (सनकी / વિચિત્ર):** Unconventional and slightly strange behavior.\n3. **Callous (कठोर / કઠોર):** Showing or having an insensitive and cruel disregard for others.\n4. **Wanderer (घुमक्कड़ / ભટકનાર):** A person who travels aimlessly.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    # ==========================================
    # MODULE 3: THE PLOT & SOCRATIC DISCOVERY
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "Griffin was a brilliant scientist who swallowed rare drugs that made his body as transparent as a sheet of glass. However, to remain invisible, he had to take off all his clothes! In the middle of a freezing London winter, he became a homeless wanderer.\n\nHe broke into stores for warmth, stole food and money, and even attacked innocent people like Mrs. Hall, the landlord's wife, when they got suspicious.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Teacher's Secret:** Griffin's story is a classic example of 'Science without Humanity'. He had an incredible brain but no heart. He used his genius invention not for the betterment of society, but for selfish and criminal acts. That's why he is called a 'lawless' person.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    # ==========================================
    # MODULE 4: THE CLIMAX
    # ==========================================
    blocks.append({
        "type": "diagram",
        "content": "A headless man fighting with a village constable, throwing clothes in the air to become invisible again.",
        "image_url": "assets/images/eng_sup_ch5_headless_fight.jpg",
        "alt_text": "A headless man struggling with a policeman in a village."
    })

    blocks.append({
        "type": "theory",
        "content": "When the village constable, Mr. Jaffers, arrived to arrest him, Griffin started taking off his clothes one by one. The constable found himself struggling with someone he could not see at all! Griffin knocked Jaffers unconscious and escaped once again, completely unseen.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    # ==========================================
    # MODULE 5: BOARD EXAM HOTS
    # ==========================================
    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC:** Character Sketch of Griffin\n\n**Answer Structure:** \n1. **Brilliant Scientist:** Discovered how to make the human body invisible.\n2. **Lawless Person:** Set his landlord's house on fire for revenge.\n3. **Selfish & Callous:** Stole from innocent people (shopkeepers, clergyman) and physically attacked them (Mrs. Hall).\n4. **Misuse of Science:** His brilliant discovery became a curse because he lacked moral values.",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_english_sup_ch5.json"
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_english_sup_ch5.json"
    final_json["metadata"]["id"] = "gseb_class10_english_sup_ch5"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Supreme English Supplementary Chapter 5 Generated Successfully!")

if __name__ == "__main__":
    generate_supreme_english_sup_ch5()
