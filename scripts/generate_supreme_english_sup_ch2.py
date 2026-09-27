import json
import os

def generate_supreme_english_sup_ch2():
    chapter_id = "ncert_class10_english_sup_ch2"
    title = "Chapter 2: The Thief's Story (Footprints Without Feet)"
    
    metadata = {
        "id": chapter_id,
        "title": title,
        "subtitle": "The Ultimate Board Exam Mastery Guide",
        "subject": "English Supplementary",
        "grade": "10",
        "board": "NCERT/CBSE",
        "curriculum": ["Universal"],
        "language": "English/Hindi/Gujarati (Bilingual)",
        "difficulty": "Advanced",
        "estimated_minutes": 120,
        "version": "3.0.0-SUPREME-ENGLISH",
        "author": "Antigravity Supreme Intelligence",
        "reviewed_by": "Chief Academic Architect",
        "tags": ["english", "footprints_without_feet", "thiefs_story", "board_special", "bilingual"],
        "learning_outcomes": [
            "Understand the theme of trust, guilt, and transformation.",
            "Master the difficult vocabulary (Flattery, Appealing, Balcony).",
            "Write perfect Character Sketches of Hari Singh and Anil.",
            "Analyze the psychological journey of a thief."
        ],
        "ai_context": {
            "learning_goal": "Make literature emotional and easy to understand for ESL students. Emphasize the transformation of the thief through kindness.",
            "common_misconceptions": [
                "Students think Anil was foolish. (Fact: Anil knew about the theft but chose to forgive him to help him reform).",
                "Students confuse the real name of the thief."
            ]
        }
    }
    
    blocks = []
    
    # ==========================================
    # MODULE 1: INTRODUCTION & HOOK
    # ==========================================
    blocks.append({
        "type": "hook",
        "content": "Can kindness and trust change a criminal? Imagine you are a 15-year-old experienced thief who targets innocent people. You meet a simple, trusting man and decide to rob him. But when the moment comes, something inside you stops you. Let's explore 'The Thief's Story'—a tale of a boy named Hari Singh and how true education and trust transformed his life.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "A 15-year-old boy (Hari Singh) approaching a young man (Anil) watching a wrestling match.",
        "image_url": "assets/images/eng_sup_ch2_wrestling_match.jpg",
        "alt_text": "A young thief approaching a trusting man."
    })

    # ==========================================
    # MODULE 2: VOCABULARY & TRANSLATIONS
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "**Master These Difficult Words:**\n1. **Flattery (चापलूसी / ખુશામત):** Excessive and insincere praise, given especially to further one's own interests.\n2. **Appealing (आकर्षक / આકર્ષક):** Attractive or interesting (Hari Singh's fake smile).\n3. **Unlined (बिना झुर्रियों वाला / કરચલીઓ વગરનું):** A face without lines of worry or age, showing innocence.\n4. **Drizzling (बूंदाबांदी / ઝરમર વરસાદ):** Light rain.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    # ==========================================
    # MODULE 3: THE PLOT & SOCRATIC DISCOVERY
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "The narrator, a 15-year-old thief who calls himself Hari Singh (not his real name), meets Anil, a 25-year-old struggling writer. Hari uses his appealing smile and flattery to win Anil's trust. Anil, being kind-hearted, allows Hari to live with him, teaches him how to cook, and even promises to teach him how to read and write whole sentences.\n\nHari makes a small profit from the daily shopping, which Anil knows about but ignores. One day, Anil makes a large sum of money (600 rupees) and brings it home.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Teacher's Secret:** Education is the real game-changer here! Hari Singh realizes that stealing gives him temporary money, but being educated will make him a really big, clever, and respected man. This is what ultimately stops him from running away.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    # ==========================================
    # MODULE 4: THE CLIMAX AND TRANSFORMATION
    # ==========================================
    blocks.append({
        "type": "diagram",
        "content": "Hari Singh standing in the rain at the railway station, looking confused and guilty.",
        "image_url": "assets/images/eng_sup_ch2_station_rain.jpg",
        "alt_text": "A boy standing in the rain at a train station."
    })

    blocks.append({
        "type": "theory",
        "content": "At night, Hari steals the money and runs to the railway station to catch the Lucknow Express. But he hesitates and misses the train. Standing in the cold drizzling rain, he realizes he has lost the only person who trusted him. He realizes the value of the education Anil was giving him.\n\nGuilt-ridden, he returns the wet notes back under the mattress. The next morning, Anil gives him a 50-rupee note (which is still wet). Anil knew about the theft, but he said nothing, choosing forgiveness over punishment.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    # ==========================================
    # MODULE 5: BOARD EXAM HOTS
    # ==========================================
    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC:** Character Sketch of Hari Singh vs. Anil\n\n**Hari Singh (The Thief):**\n1. Experienced and successful thief at just 15.\n2. Good judge of character (knew who to rob).\n3. Has an inner conscience that ultimately transforms him.\n\n**Anil (The Writer):**\n1. Easy-going, kind, and simple.\n2. Valued trust and compassion over money.\n3. His silent forgiveness was more powerful than any punishment.",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_english_sup_ch2.json"
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_english_sup_ch2.json"
    final_json["metadata"]["id"] = "gseb_class10_english_sup_ch2"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Supreme English Supplementary Chapter 2 Generated Successfully!")

if __name__ == "__main__":
    generate_supreme_english_sup_ch2()
