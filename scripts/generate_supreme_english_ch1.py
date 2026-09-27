import json
import os

def generate_supreme_english_ch1():
    chapter_id = "ncert_class10_english_ch1"
    title = "Chapter 1: A Letter to God (First Flight)"
    
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
        "tags": ["english", "first_flight", "letter_to_god", "board_special", "bilingual"],
        "learning_outcomes": [
            "Understand the profound theme of extreme faith in God.",
            "Master the difficult vocabulary (Hailstones, Locusts, Peso).",
            "Write a perfect Character Sketch of Lencho.",
            "Solve CBSE/State Board HOTS questions related to the Postmaster's empathy."
        ],
        "ai_context": {
            "learning_goal": "Make literature emotional and easy to understand for ESL (English as a Second Language) students. Use Bilingual translations for tough words.",
            "common_misconceptions": [
                "Students think the post office employees were bad. (Fact: They actually helped him!).",
                "Students misspell 'Hailstones' and 'Locusts' in exams."
            ]
        }
    }
    
    blocks = []
    
    # ==========================================
    # MODULE 1: INTRODUCTION & HOOK
    # ==========================================
    blocks.append({
        "type": "hook",
        "content": "Imagine your entire farm is destroyed by a terrible storm. You have no money and your family might starve. Who do you ask for help? Your relatives? The bank? Our hero, Lencho, did something unimaginable—he wrote a letter directly to **God (भगवान / ભગવાન)**! Let's dive into this beautiful story of unbreakable faith.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Lencho looking at his ruined cornfield after the terrible hailstorm.",
        "image_url": "assets/images/eng_ch1_lencho_field.jpg",
        "alt_text": "A farmer standing in a destroyed field with ice everywhere."
    })

    # ==========================================
    # MODULE 2: VOCABULARY & TRANSLATIONS
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "**Master These Difficult Words:**\n1. **Hailstones (ओले / કરા):** Small balls of ice that fall like rain.\n2. **Locusts (टिड्डियों का दल / તીડ):** Insects that fly in big groups and destroy crops.\n3. **Pesos (पीसो / પીસો):** Currency of several Latin American countries.\n4. **Amiable (मिलनसार / મળતાવડો):** Friendly and pleasant (Used to describe the Postmaster).",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    # ==========================================
    # MODULE 3: THE PLOT & SOCRATIC DISCOVERY
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "Lencho was a hardworking farmer. His cornfield needed a good downpour (बारिश / વરસાદ). The rain started, but suddenly it turned into a destructive hailstorm. His field became totally white, as if covered with salt. \n\nWith zero hope left, he went to the post office and dropped a letter into the mailbox addressed to: **'To God'**, asking for 100 pesos to sow his field again.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Teacher's Secret:** When the Postmaster read the letter, he first laughed. But then, he became serious. He was deeply moved by Lencho's innocent faith. He didn't want to break that faith, so he decided to collect money from his employees to help Lencho!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    # ==========================================
    # MODULE 4: THE IRONICAL ENDING
    # ==========================================
    blocks.append({
        "type": "diagram",
        "content": "Lencho counting the money angrily, thinking the post office employees stole the rest.",
        "image_url": "assets/images/eng_ch1_lencho_angry.jpg",
        "alt_text": "A farmer counting money angrily inside a post office."
    })

    blocks.append({
        "type": "theory",
        "content": "The Postmaster could only collect **70 pesos**. When Lencho opened the envelope, he wasn't surprised to see the money (that's how strong his faith was!). But when he counted it, he got angry. \n\nHe wrote a second letter to God saying: *\"God, next time don't send the money through the mail, because the post office employees are a **bunch of crooks (ठगों का समूह / લુચ્ચાઓની ટોળી)**!\"*\n\n**The Irony:** The very people who helped him were called crooks by him!",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    # ==========================================
    # MODULE 5: BOARD EXAM HOTS
    # ==========================================
    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC:** Character Sketch of Lencho\n\n**Answer Structure:** \n1. **Hardworking:** Like an ox in the fields.\n2. **Unshakable Faith:** Believed God sees everything and will definitely help.\n3. **Innocent/Naive:** He actually thought a letter could reach God and God would mail him currency notes.\n4. **Ungrateful (Unintentionally):** He called his helpers 'crooks' because of his blind faith in God.",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_english_ch1.json"
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_english_ch1.json"
    final_json["metadata"]["id"] = "gseb_class10_english_ch1"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Supreme English Chapter 1 Generated Successfully!")

if __name__ == "__main__":
    generate_supreme_english_ch1()
