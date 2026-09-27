import json
import os

def generate_supreme_chapter_5():
    chapter_id = "ncert_class10_science_ch5"
    title = "Chapter 5: Life Processes"
    
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
        "estimated_minutes": 240,
        "version": "3.0.0-SUPREME-VISUAL",
        "author": "Antigravity Supreme Intelligence",
        "reviewed_by": "Chief Academic Architect",
        "tags": ["biology", "life processes", "nutrition", "respiration", "transportation", "excretion", "board_special", "bilingual"],
        "learning_outcomes": [
            "Understand the four basic life processes: Nutrition, Respiration, Transportation, and Excretion.",
            "Explain the process of photosynthesis in plants.",
            "Trace the flow of blood through the human heart.",
            "Understand the functioning of nephrons in the human kidney."
        ],
        "ai_context": {
            "learning_goal": "Transform the student from a beginner to a board-exam topper in Life Processes. Use the EduOS 8-Step Learning Cycle.",
            "common_misconceptions": [
                "Students think respiration is just breathing. (Fact: Respiration is the cellular breakdown of glucose to release energy).",
                "Students confuse arteries and veins."
            ]
        }
    }
    
    blocks = []
    
    # STEP 1: HOOK
    blocks.append({
        "type": "hook",
        "content": "Have you ever wondered what keeps a sleeping dog alive, or how a giant banyan tree survives without a mouth to eat? The answer lies in the invisible engine of life: **Life Processes (जैव प्रक्रम / જૈવિક ક્રિયાઓ)**!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    # STEP 2: SOCRATIC THINKING
    blocks.append({
        "type": "ai_tutor_prompt",
        "content": "Why do you think viruses are considered the 'zombies' of biology? Are they alive or dead? What happens to a virus when it is outside a host body versus inside one?",
        "difficulty": "Intermediate",
        "bloom": "Analyze"
    })

    # STEP 3: DISCOVERY
    blocks.append({
        "type": "diagram",
        "content": "Let's discover how plants make their own food using sunlight. This is nature's own solar-powered kitchen!",
        "image_url": "assets/images/ch5_photosynthesis.jpg",
        "alt_text": "Process of Photosynthesis showing sunlight, carbon dioxide, and water"
    })
    
    # STEP 4: REVEAL
    blocks.append({
        "type": "theory",
        "content": "**Photosynthesis (प्रकाश संश्लेषण / પ્રકાશ સંશ્લેષણ):**\nIt is the process by which green plants synthesize nutrients from carbon dioxide and water in the presence of sunlight and chlorophyll.\n*Equation:* **6CO₂ + 12H₂O + Sunlight ⟶ C₆H₁₂O₆ (Glucose) + 6O₂ + 6H₂O**",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    # STEP 5: KNOWLEDGE CHECK
    blocks.append({
        "type": "mcq",
        "content": "Which gas is released as a byproduct during photosynthesis?",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    # STEP 6: REFLECTION
    blocks.append({
        "type": "reflection",
        "content": "Imagine if humans had chlorophyll in their skin. How would our daily lives change? Would we still need restaurants?",
        "difficulty": "Advanced",
        "bloom": "Create"
    })

    # STEP 7: CONNECTION
    blocks.append({
        "type": "cross_subject_link",
        "content": "Connect this with Chemistry: The breakdown of glucose in our bodies is a combination of chemical reactions, specifically oxidation-reduction (redox) reactions!",
        "difficulty": "Intermediate",
        "bloom": "Analyze"
    })
    
    # TRANSPORTATION
    blocks.append({
        "type": "theory",
        "content": "**Transportation in Humans (वहन / વહન):**\nThe human heart (मानव हृदय / માનવ હૃદય) is a muscular organ that pumps blood to all parts of the body. It has four chambers to prevent oxygen-rich blood from mixing with carbon dioxide-rich blood.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "diagram",
        "content": "The Human Heart is like a highly efficient double-pump system.",
        "image_url": "assets/images/ch5_human_heart.jpg",
        "alt_text": "Sectional view of the human heart"
    })
    
    blocks.append({
        "type": "memory_trick",
        "content": "**A**rteries carry blood **A**way from the heart. Veins bring blood **IN**to the heart.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })
    
    # EXCRETION
    blocks.append({
        "type": "theory",
        "content": "**Excretion (उत्सर्जन / ઉત્સર્જન):**\nThe biological process involved in the removal of harmful metabolic wastes from the body is called excretion. In humans, the kidney uses basic filtration units called **Nephrons (नेफ्रॉन / નેફ્રોન)**.",
        "difficulty": "Advanced",
        "bloom": "Apply"
    })

    blocks.append({
        "type": "diagram",
        "content": "The Nephron is the micro-filter of our body, working tirelessly to clean our blood.",
        "image_url": "assets/images/ch5_nephron.jpg",
        "alt_text": "Structure of a nephron"
    })
    
    # STEP 8: MASTERY
    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC:** Differentiate between Aerobic and Anaerobic respiration.\n\n**Answer Structure:** Aerobic requires oxygen and produces 38 ATP. Anaerobic occurs without oxygen (e.g., in yeast or our muscles during heavy exercise) and produces less energy.",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    # Save the output
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_science_ch5.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(final_json, f, indent=2, ensure_ascii=False)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_science_ch5.json"
    final_json["metadata"]["id"] = "gseb_class10_science_ch5"
    with open(gseb_path, "w", encoding="utf-8") as f:
        json.dump(final_json, f, indent=2, ensure_ascii=False)
        
    print("Supreme Chapter 5 Generated Successfully!")

if __name__ == "__main__":
    generate_supreme_chapter_5()
