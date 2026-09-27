import json
import os

def generate_supreme_chapter_7():
    chapter_id = "ncert_class10_science_ch7"
    title = "Chapter 7: How do Organisms Reproduce?"
    
    metadata = {
        "id": chapter_id,
        "title": title,
        "subtitle": "The Ultimate Board Exam Mastery Guide",
        "subject": "Science",
        "grade": "10",
        "board": "NCERT/CBSE",
        "curriculum": ["Universal"],
        "language": "English/Hindi/Gujarati (Bilingual)",
        "difficulty": "Advanced",
        "estimated_minutes": 180,
        "version": "3.0.0-SUPREME-VISUAL",
        "author": "Antigravity Supreme Intelligence",
        "reviewed_by": "Chief Academic Architect",
        "tags": ["biology", "reproduction", "asexual", "sexual", "board_special", "bilingual"],
        "learning_outcomes": [
            "Understand the fundamental difference between asexual and sexual reproduction.",
            "Master the various modes of asexual reproduction.",
            "Analyze the process of sexual reproduction in flowering plants.",
            "Understand human reproduction and reproductive health."
        ],
        "ai_context": {
            "learning_goal": "Transform the student from a beginner to a board-exam topper in Reproduction. Use the 'Socratic Discovery Arc'.",
            "common_misconceptions": [
                "Students think only animals reproduce sexually, forgetting plants do too.",
                "Confusion between binary fission and multiple fission."
            ]
        }
    }
    
    blocks = []
    
    # ==========================================
    # MODULE 1: INTRODUCTION TO REPRODUCTION
    # ==========================================
    blocks.append({
        "type": "hook",
        "content": "Why do living things create copies of themselves? Why aren't dogs giving birth to cats? Today, we unlock the greatest secret of life: **Reproduction (प्रजनन / પ્રજનન)**!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "content": "**Reproduction** is the biological process by which new individual organisms (offspring) are produced from their parents.\n\nIt is essential for the survival of a species, not an individual. This process involves the copying of DNA.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    # ==========================================
    # MODULE 2: ASEXUAL REPRODUCTION
    # ==========================================
    blocks.append({
        "type": "diagram",
        "content": "In Amoeba, a single cell simply splits into two to create new life! This is Asexual Reproduction.",
        "image_url": "assets/images/ch7_binary_fission.jpg",
        "alt_text": "Binary fission in amoeba"
    })

    blocks.append({
        "type": "theory",
        "content": "**Asexual Reproduction (अलैंगिक जनन / અલિંગી પ્રજનન):**\nReproduction by a single parent without the fusion of gametes.\n\n*Examples:*\n- **Binary Fission:** Amoeba (अमीबा).\n- **Budding:** Hydra and Yeast.\n- **Regeneration:** Planaria.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    # ==========================================
    # MODULE 3: SEXUAL REPRODUCTION IN PLANTS
    # ==========================================
    blocks.append({
        "type": "diagram",
        "content": "A flower isn't just beautiful; it's the reproductive organ of a plant!",
        "image_url": "assets/images/ch7_flower_reproduction.jpg",
        "alt_text": "Longitudinal section of a flower showing stamen and pistil"
    })

    blocks.append({
        "type": "theory",
        "content": "**Sexual Reproduction (लैंगिक जनन / લિંગી પ્રજનન):**\nInvolves two parents (male and female) and the fusion of gametes.\n\nIn plants, the **Stamen (पुंकेसर)** is the male part, and the **Pistil/Carpel (स्त्रीकेसर)** is the female part.\nPollen grains (male) must reach the stigma (female). This is called **Pollination (परागण)**.",
        "difficulty": "Advanced",
        "bloom": "Apply"
    })

    # ==========================================
    # MODULE 4: SEXUAL REPRODUCTION IN HUMANS
    # ==========================================
    blocks.append({
        "type": "diagram",
        "content": "Human reproduction involves highly specialized systems in males and females that work together.",
        "image_url": "assets/images/ch7_human_reproduction.jpg",
        "alt_text": "Human reproductive system overview"
    })

    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC:** What is Placenta (प्लैसेंटा / જરાયુ)? \n\n**Answer Structure:** It is a special tissue connection between the mother and the fetus. It provides oxygen and nutrients to the baby and removes waste products.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    os.makedirs("/home/ubuntu/Shine_Academy_Naroda/app_core/chapters", exist_ok=True)
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_science_ch7.json"
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_science_ch7.json"
    final_json["metadata"]["id"] = "gseb_class10_science_ch7"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Supreme Chapter 7 Generated Successfully!")

if __name__ == "__main__":
    generate_supreme_chapter_7()
