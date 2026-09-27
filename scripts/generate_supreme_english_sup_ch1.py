import json
import os

def generate_supreme_english_sup_ch1():
    chapter_id = "ncert_class10_english_sup_ch1"
    title = "Supplementary Chapter 1: A Triumph of Surgery"
    
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
        "tags": ["english", "supplementary", "triumph_of_surgery", "board_special", "bilingual"],
        "learning_outcomes": [
            "Understand the theme of over-indulgence and its consequences.",
            "Master the difficult vocabulary (Sausage, Rheumy, Convalescing).",
            "Write a perfect Character Sketch of Mrs. Pumphrey and Mr. Herriot.",
            "Solve CBSE/State Board HOTS questions related to the dog's recovery without medicine."
        ],
        "ai_context": {
            "learning_goal": "Make literature emotional and easy to understand for ESL (English as a Second Language) students. Use Bilingual translations for tough words.",
            "common_misconceptions": [
                "Students think Mr. Herriot gave medicine to Tricki. (Fact: He just controlled his diet and gave him exercise).",
                "Students misunderstand the meaning of 'Triumph of Surgery' (Surgery here means a veterinary hospital or clinic, not an operation)."
            ]
        }
    }
    
    blocks = []
    
    # ==========================================
    # MODULE 1: INTRODUCTION & HOOK
    # ==========================================
    blocks.append({
        "type": "hook",
        "content": "Have you ever loved a pet so much that you overfed them with sweets, chocolates, and rich food? That's exactly what the rich and emotional Mrs. Pumphrey did to her little dog, Tricki! Let's read how a smart veterinary doctor, Mr. Herriot, saves the overly pampered dog without giving him a single medicine.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "A hugely fat Tricki, looking like a bloated sausage with a leg at each corner.",
        "image_url": "assets/images/eng_sup_ch1_fat_tricki.jpg",
        "alt_text": "A very fat dog looking lethargic."
    })

    # ==========================================
    # MODULE 2: VOCABULARY & TRANSLATIONS
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "**Master These Difficult Words:**\n1. **Sausage (कबाब जैसा / સોસેજ):** Finely minced meat stuffed into a casing.\n2. **Rheumy (आँखों से पानी आना / આંખમાંથી પાણી આવવું):** Watery discharge from the eyes.\n3. **Convalescing (स्वास्थ्य लाभ करना / સાજા થવું):** Recovering health and strength over a period of time after an illness.\n4. **Surgery (पशु चिकित्सालय / પ્રાણીઓનું દવાખાનું):** A place where a doctor, dentist, or veterinary surgeon treats patients.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    # ==========================================
    # MODULE 3: THE PLOT & SOCRATIC DISCOVERY
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "Mrs. Pumphrey thought Tricki was suffering from malnutrition (कुपोषण / કુપોષણ), so she fed him malt, cod-liver oil, and Horlicks between meals. Predictably, Tricki became seriously ill. He refused food, had bouts of vomiting, and spent all his time panting on a rug.\n\nMr. Herriot, the veterinary surgeon, knew the only cure was to get Tricki out of the house. He admitted Tricki to his 'surgery' for a fortnight.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Teacher's Secret:** The real 'surgery' was strict diet control and plenty of water for the first two days, followed by mixing him with other dogs for exercise. No medical treatment was given!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    # ==========================================
    # MODULE 4: THE RECOVERY AND CONCLUSION
    # ==========================================
    blocks.append({
        "type": "diagram",
        "content": "Tricki playing happily and energetically with a pack of other dogs at the surgery.",
        "image_url": "assets/images/eng_sup_ch1_playing_tricki.jpg",
        "alt_text": "A healthy dog running and playing with other dogs."
    })

    blocks.append({
        "type": "theory",
        "content": "Within two weeks, Tricki transformed into a flexible, hard-muscled animal. When Mrs. Pumphrey came to collect him, Tricki took a tremendous leap and sailed into her lap. Tears shone in her eyes as she cried, *\"Oh, Mr. Herriot, how can I ever thank you? This is a **triumph of surgery** (शल्य चिकित्सा की विजय / સર્જરીનો વિજય)!\"*\n\n**The Irony:** Mrs. Pumphrey thought a medical operation cured Tricki, but it was just diet and exercise!",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    # ==========================================
    # MODULE 5: BOARD EXAM HOTS
    # ==========================================
    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC:** Character Sketch of Mrs. Pumphrey\n\n**Answer Structure:** \n1. **Extremely Rich & Pampering:** Provided Tricki with tweed coats, different bowls, and rich food.\n2. **Foolish but Loving:** Mistook his greed for malnutrition. Her excessive love harmed the dog.\n3. **Grateful:** Deeply thankful to Mr. Herriot at the end.\n\n🔥 **HOT TOPIC:** Character Sketch of Mr. Herriot\n1. **Practical & Tactful:** Knew exactly how to cure Tricki without arguing with the rich owner.\n2. **Observant:** Diagnosed Tricki just by looking at his physical condition.\n3. **Opportunistic (Funny):** Enjoyed the wine and eggs sent by Mrs. Pumphrey for Tricki!",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_english_sup_ch1.json"
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_english_sup_ch1.json"
    final_json["metadata"]["id"] = "gseb_class10_english_sup_ch1"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Supreme English Supplementary Chapter 1 Generated Successfully!")

if __name__ == "__main__":
    generate_supreme_english_sup_ch1()
