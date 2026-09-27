import json
import os

def generate_supreme_chapter_8():
    chapter_id = "ncert_class10_science_ch8"
    title = "Chapter 8: Heredity"
    
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
        "tags": ["biology", "heredity", "genetics", "mendel", "dna", "board_special", "bilingual"],
        "learning_outcomes": [
            "Understand the basic concepts of Heredity and variation.",
            "Explain Mendel's experiments with pea plants and the laws of inheritance.",
            "Understand how traits are expressed through DNA and proteins.",
            "Explain the process of sex determination in human beings."
        ],
        "ai_context": {
            "learning_goal": "Transform the student from a beginner to a board-exam topper in Heredity. Use the 'Socratic Discovery Arc'.",
            "common_misconceptions": [
                "Students think only dominant traits are inherited. (Fact: Both dominant and recessive alleles are inherited, but recessive traits are only expressed when two copies are present).",
                "Students confuse genes with chromosomes or DNA."
            ]
        }
    }
    
    blocks = []
    
    # ==========================================
    # MODULE 1: INTRODUCTION TO HEREDITY
    # ==========================================
    blocks.append({
        "type": "hook",
        "content": "Have you ever wondered why you look a little bit like your father and a little bit like your mother? Why do puppies look like dogs and not cats? This magical passing down of features is called **Heredity (आनुवंशिकता / આનુવંશિકતા)**!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "A DNA double helix structure containing the genetic information of life.",
        "image_url": "assets/images/ch8_dna_structure.jpg",
        "alt_text": "Glowing DNA structure double helix"
    })

    blocks.append({
        "type": "theory",
        "content": "**Heredity (आनुवंशिकता)** is the transmission of traits or characteristics from parents to their offspring.\n\n**Variation (विभिन्नता / ભિન્નતા)** is the difference in the characters among the individuals of a species.\nFor example, human height, skin color, and eye color vary from person to person.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    # ==========================================
    # MODULE 2: MENDEL'S EXPERIMENTS
    # ==========================================
    blocks.append({
        "type": "teacher_tip",
        "content": "Gregor Johann Mendel is known as the 'Father of Genetics'. He used pea plants for his experiments. Let's see why!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "diagram",
        "content": "Mendel observing tall and short pea plants in his garden.",
        "image_url": "assets/images/ch8_mendel_peas.jpg",
        "alt_text": "Gregor Mendel in a garden of pea plants"
    })

    blocks.append({
        "type": "theory",
        "content": "**Why Pea Plants (मटर के पौधे / વટાણાના છોડ)?**\n1. They have easily observable contrasting characters (like tall/short, round/wrinkled seeds).\n2. They have a short life span.\n3. Normally self-pollinating but can be cross-pollinated.\n\n**Monohybrid Cross (एकल संकरण):** A cross involving only one pair of contrasting characters. \nExample: Tall plant (TT) x Short plant (tt). In F1 generation, all plants were Tall (Tt). In F2 generation, the ratio of Tall:Short was 3:1.",
        "difficulty": "Intermediate",
        "bloom": "Apply"
    })

    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC:** Differentiate between Phenotype and Genotype.\n\n**Answer Structure:** \n- **Phenotype (लक्षणप्ररूप):** Physical appearance of an organism (e.g., Tall or Short).\n- **Genotype (जीनप्ररूप):** Genetic makeup of an organism (e.g., TT, Tt, or tt).",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    # ==========================================
    # MODULE 3: SEX DETERMINATION
    # ==========================================
    blocks.append({
        "type": "hook",
        "content": "Who decides the gender of a baby? The mother or the father? Let's discover the science behind it!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "diagram",
        "content": "Flowchart showing sex determination in humans with XX and XY chromosomes.",
        "image_url": "assets/images/ch8_sex_determination.jpg",
        "alt_text": "Human sex determination flowchart XX and XY"
    })

    blocks.append({
        "type": "theory",
        "content": "In human beings, there are 23 pairs of chromosomes. Out of these, 22 pairs are called autosomes, and the 23rd pair is the sex chromosome.\n- Females have a perfect pair of sex chromosomes, **XX**.\n- Males have a mismatched pair, **XY**.\n\nDuring fertilization, if the sperm carrying the 'X' chromosome fuses with the egg, the child will be a girl (XX). If the sperm carrying the 'Y' chromosome fuses with the egg, the child will be a boy (XY). Thus, the **father** determines the sex of the child.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC: Justify how the sex of a child is determined by the father.**\n\n**Board Question:** 'In human beings, the statistical probability of getting either a male or female child is 50 : 50.' Give a suitable explanation. \n**Answer:** Since a male produces 50% sperms with 'X' chromosome and 50% sperms with 'Y' chromosome, there is an equal 50:50 chance of an X-bearing or Y-bearing sperm fertilizing the egg (which always has an X chromosome).",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_science_ch8.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_science_ch8.json"
    final_json["metadata"]["id"] = "gseb_class10_science_ch8"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Supreme Chapter 8 Generated Successfully!")

if __name__ == "__main__":
    generate_supreme_chapter_8()
