import json
import os

def generate_supreme_chapter_2():
    chapter_id = "ncert_class10_science_ch2"
    title = "Chapter 2: Acids, Bases and Salts"
    
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
        "tags": ["chemistry", "acids", "bases", "salts", "pH_scale", "board_special", "bilingual"],
        "learning_outcomes": [
            "Master the differences between Acids and Bases.",
            "Understand the pH scale and its real-world importance.",
            "Write the chemical reactions of Acids and Bases with metals and carbonates.",
            "Solve CBSE/State Board HOTS questions about everyday salts like Baking Soda and Plaster of Paris."
        ],
        "ai_context": {
            "learning_goal": "Transform the student from a beginner to a board-exam topper in Acids, Bases, and Salts. Use the 'Socratic Discovery Arc'.",
            "common_misconceptions": [
                "Students think all acids are dangerous and all bases are safe. (Fact: Strong bases like NaOH are extremely corrosive).",
                "Students confuse pH 1 (strong acid) with pH 14 (strong base)."
            ]
        }
    }
    
    blocks = []
    
    # ==========================================
    # MODULE 1: INTRODUCTION TO ACIDS & BASES
    # ==========================================
    blocks.append({
        "type": "hook",
        "content": "Have you ever tasted a sour lemon (खट्टा नींबू / ખાટું લીંબુ) or accidentally tasted bitter soap (कड़वा साबुन / કડવો સાબુ) while bathing? These everyday experiences are your first introduction to the world of **Acids and Bases (अम्ल और क्षारक / એસિડ અને બેઝ)**!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Acids (like lemon juice) are typically sour to taste, while Bases (like soap) are bitter and soapy to touch.",
        "image_url": "assets/images/acid_vs_base.jpg",
        "alt_text": "Lemon dripping juice vs Soap with bubbles"
    })

    blocks.append({
        "type": "theory",
        "content": "An **Acid (अम्ल / એસિડ)** is a substance that produces Hydrogen ions (**H⁺**) when dissolved in water.\n*Example:* Hydrochloric Acid (**HCl**), Sulphuric Acid (**H₂SO₄**).\n\nA **Base (क्षारक / બેઝ)** is a substance that produces Hydroxide ions (**OH⁻**) when dissolved in water.\n*Example:* Sodium Hydroxide (**NaOH**), Potassium Hydroxide (**KOH**).\n\nIf a base dissolves in water, it gets a special VIP name: **Alkali (क्षार / આલ્કલી)**.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "memory_trick",
        "content": "**Litmus Paper Trick:**\n- **A**cid turns blue litmus **R**ed. (**A**pple is **R**ed)\n- **B**ase turns red litmus **B**lue. (**B**ase = **B**lue)",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    # ==========================================
    # MODULE 2: CHEMICAL PROPERTIES & REACTIONS
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "**1. Reaction with Metals (धातुओं के साथ अभिक्रिया):**\nWhen an acid reacts with a metal, it produces salt and Hydrogen gas (**H₂**).\n*Equation:* **Zn + H₂SO₄ ⟶ ZnSO₄ + H₂**\n\n**Test for Hydrogen gas:** When a burning matchstick is brought near the gas, it burns with a 'Pop' sound (पॉप की आवाज़)!",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC:** Why should curd and sour substances NOT be kept in brass or copper vessels? \n\n**Answer Structure:** Because curd contains lactic acid (लैक्टिक अम्ल). This acid reacts with the metal of the vessel to form toxic (ज़हरीले) compounds, which can cause food poisoning.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    # ==========================================
    # MODULE 3: NEUTRALIZATION REACTION
    # ==========================================
    blocks.append({
        "type": "diagram",
        "content": "What happens when you mix a fiery acid and a strong base? They destroy each other's effect and peacefully form salt and water. This is called a Neutralization Reaction!",
        "image_url": "assets/images/neutralization_clash.jpg",
        "alt_text": "Acid and Base colliding to form salt and water"
    })

    blocks.append({
        "type": "theory",
        "content": "**Neutralization Reaction (उदासीनीकरण अभिक्रिया / તટસ્થીકરણ પ્રતિક્રિયા):**\nThe reaction between an acid and a base to give a salt and water is known as a neutralization reaction.\n\n*Equation:* **Base + Acid ⟶ Salt + Water**\n*Example:* **NaOH + HCl ⟶ NaCl + H₂O**",
        "difficulty": "Intermediate",
        "bloom": "Apply"
    })

    # ==========================================
    # MODULE 4: THE pH SCALE
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "How do we know how strong an acid or a base is? We use the **pH Scale**!\nThe 'p' stands for 'potenz' (meaning power in German), and 'H' stands for Hydrogen.\n\n- **pH < 7:** Acidic (अम्लीय) - The lower the number, the stronger the acid.\n- **pH = 7:** Neutral (उदासीन) - Like pure water.\n- **pH > 7:** Basic (क्षारीय) - The higher the number, the stronger the base.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "diagram",
        "content": "The Universal Indicator shows different colors at different pH values. Red indicates strong acid, green indicates neutral, and dark blue/purple indicates strong base.",
        "image_url": "assets/images/ph_scale_glowing.jpg",
        "alt_text": "Glowing pH Scale from 0 to 14"
    })

    # ==========================================
    # MODULE 5: EVERYDAY SALTS (BOARD FAVORITES)
    # ==========================================
    blocks.append({
        "type": "teacher_tip",
        "content": "Students, the next section is the MOST important part of this chapter for board exams. You must memorize the common name, chemical name, formula, and uses of these 4 salts!",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "theory",
        "content": "1. **Baking Soda (बेकिंग सोडा):**\n- *Chemical Name:* Sodium Hydrogen Carbonate\n- *Formula:* **NaHCO₃**\n- *Use:* Makes cakes and bread fluffy by releasing **CO₂** gas when heated.\n\n2. **Washing Soda (धावन सोडा):**\n- *Chemical Name:* Sodium Carbonate Decahydrate\n- *Formula:* **Na₂CO₃·10H₂O**\n- *Use:* Removes permanent hardness of water.",
        "difficulty": "Advanced",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC: Plaster of Paris (PoP)**\n- *Formula:* **CaSO₄·½H₂O** (Calcium Sulphate Hemihydrate)\n\n**Board Question:** Why should PoP be stored in a moisture-proof container? \n**Answer:** Because if it absorbs moisture (H₂O), it reacts and turns into a hard solid mass called **Gypsum (CaSO₄·2H₂O)**, becoming useless for setting fractured bones.",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_science_ch2.json"
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_science_ch2.json"
    final_json["metadata"]["id"] = "gseb_class10_science_ch2"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Supreme Chapter 2 Generated Successfully!")

if __name__ == "__main__":
    generate_supreme_chapter_2()
