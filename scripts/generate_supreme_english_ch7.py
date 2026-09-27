import json
import os

def generate_supreme_english_ch7():
    chapter_id = "ncert_class10_english_ch7"
    title = "Chapter 7: Glimpses of India (First Flight)"
    
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
        "tags": ["english", "first_flight", "glimpses_of_india", "board_special", "bilingual"],
        "learning_outcomes": [
            "Explore the cultural heritage of Goa, Coorg, and Assam.",
            "Master difficult vocabulary (Pader, Kabai, Martial, Pranjol).",
            "Write perfect descriptions of the traditional Goan baker and Coorg's bravery.",
            "Solve CBSE/State Board HOTS questions related to the legends of tea."
        ],
        "ai_context": {
            "learning_goal": "Make literature emotional and easy to understand for ESL students. Use Bilingual translations for tough words.",
            "common_misconceptions": [
                "Students confuse the locations of Coorg and Assam.",
                "Students forget the two legends about the discovery of tea."
            ]
        }
    }
    
    blocks = []
    
    # ==========================================
    # MODULE 1: INTRODUCTION & HOOK
    # ==========================================
    blocks.append({
        "type": "hook",
        "content": "India is a land of diverse cultures and beautiful landscapes. Have you ever wondered what makes Goa's bread so special, or why Coorg's people are known for their bravery, or how tea was first discovered in Assam? Let's take a journey across three fascinating parts of India: Goa, Coorg, and Assam! (भारत की एक झलक / ભારતની ઝલક)",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "A traditional baker in Goa carrying a bamboo basket filled with fresh bread.",
        "image_url": "assets/images/eng_ch7_goan_baker.jpg",
        "alt_text": "A Goan baker delivering traditional bread."
    })

    # ==========================================
    # MODULE 2: VOCABULARY & TRANSLATIONS
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "**Master These Difficult Words:**\n1. **Pader (पाडेर / પાડેર):** The traditional baker in Goa.\n2. **Kabai (कबाई / કબાઈ):** A peculiar dress worn by bakers in the past, consisting of a single-piece long frock.\n3. **Martial (युद्ध संबंधी / યુદ્ધ સંબંધિત):** Having to do with war (referring to the men of Coorg).\n4. **Monastery (मठ / મઠ):** A building occupied by a community of monks living under religious vows (seen in Coorg).",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    # ==========================================
    # MODULE 3: THE PLOT & SOCRATIC DISCOVERY
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "This chapter has three parts:\n\n**I. A Baker from Goa:** Highlights the importance of the traditional baker (pader) in Goan culture, especially during festivals and marriages.\n**II. Coorg:** Describes the beautiful land of rolling hills, its martial men, beautiful women, and rich coffee plantations. Coorgis are fiercely independent and brave.\n**III. Tea from Assam:** Rajvir and Pranjol travel to Assam. Rajvir shares two legends about the discovery of tea (Chinese legend of Bodhidharma and an Indian legend). Assam has the largest concentration of tea plantations in the world.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Teacher's Secret:** To remember the two legends of tea, think of 'Boiling Water' (Chinese Emperor) and 'Sleepy Eyelids' (Buddhist monk Bodhidharma).",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    # ==========================================
    # MODULE 4: LEGENDS & STORIES
    # ==========================================
    blocks.append({
        "type": "diagram",
        "content": "Lush green tea gardens in Assam with women plucking tea leaves.",
        "image_url": "assets/images/eng_ch7_assam_tea.jpg",
        "alt_text": "Tea gardens of Assam with workers plucking leaves."
    })

    blocks.append({
        "type": "theory",
        "content": "The discovery of tea has fascinating stories. In the Indian legend, a Buddhist ascetic named Bodhidharma cut off his eyelids because he felt sleepy during meditation. Ten tea plants grew out of the eyelids! When the leaves were put in hot water and drunk, they banished sleep.\n\n**Key Takeaway:** Different regions of India have unique stories, cultures, and traditions that make the country truly incredible.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    # ==========================================
    # MODULE 5: BOARD EXAM HOTS
    # ==========================================
    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC:** The significance of a baker in Goan village OR the courage of Coorgis.\n\n**Answer Structure:** \n1. **Goan Baker:** Bread is essential for marriages (bol), parties, and Christmas (bolinhas). The baker is a friend, companion, and guide.\n2. **Coorgis:** Known for hospitality and bravery. The Coorg Regiment is one of the most decorated in the Indian Army. General Cariappa, the first Chief of the Indian Army, was a Coorgi.",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_english_ch7.json"
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_english_ch7.json"
    final_json["metadata"]["id"] = "gseb_class10_english_ch7"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Supreme English Chapter 7 Generated Successfully!")

if __name__ == "__main__":
    generate_supreme_english_ch7()
