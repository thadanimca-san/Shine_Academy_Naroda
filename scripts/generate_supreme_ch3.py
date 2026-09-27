import json
import os

def generate_supreme_chapter_3():
    chapter_id = "ncert_class10_science_ch3"
    title = "Chapter 3: Metals and Non-metals"
    
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
        "tags": ["chemistry", "metals", "non-metals", "reactivity_series", "ionic_bond", "metallurgy", "board_special", "bilingual"],
        "learning_outcomes": [
            "Master the physical and chemical properties of Metals and Non-metals.",
            "Understand the Reactivity Series and displacement reactions.",
            "Explain the formation and properties of Ionic compounds.",
            "Learn the extraction of metals (Metallurgy) and prevention of corrosion."
        ],
        "ai_context": {
            "learning_goal": "Transform the student from a beginner to a board-exam topper in Metals and Non-metals. Use the 'Socratic Discovery Arc'.",
            "common_misconceptions": [
                "Students think all metals are solid at room temperature. (Fact: Mercury is a liquid metal).",
                "Students confuse calcination with roasting in metallurgy."
            ]
        }
    }
    
    blocks = []
    
    # ==========================================
    # MODULE 1: INTRODUCTION TO METALS & NON-METALS
    # ==========================================
    blocks.append({
        "type": "hook",
        "content": "Look around you! From the iron (लोहा / લોખંડ) in bridges to the oxygen (ऑक्सीजन / ઓક્સિજન) we breathe, everything is made of elements. But how do we divide them? Welcome to the epic world of **Metals and Non-metals (धातु और अधातु / ધાતુ અને અધાતુ)**!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "content": "**Metals (धातु / ધાતુ):** They are typically hard, shiny (lustrous), malleable (can be beaten into sheets), ductile (can be drawn into wires), and good conductors of heat and electricity.\n*Example:* Iron (**Fe**), Copper (**Cu**), Gold (**Au**).\n\n**Non-metals (अधातु / અધાતુ):** They are usually dull, brittle (break easily), non-ductile, and poor conductors.\n*Example:* Carbon (**C**), Oxygen (**O₂**), Sulphur (**S**).",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "Exceptions are super important for boards! Remember: **Mercury (Hg)** is a metal but liquid at room temperature. **Graphite** (a form of Carbon) is a non-metal but a *good* conductor of electricity!",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    # ==========================================
    # MODULE 2: CHEMICAL PROPERTIES & REACTIVITY SERIES
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "When metals react with oxygen, they form metal oxides. These oxides are generally basic in nature.\n*Equation:* **4Fe + 3O₂ ⟶ 2Fe₂O₃** (Iron(III) oxide).",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "diagram",
        "content": "The Reactivity Series helps us predict how metals will react. Potassium and Sodium are at the top (most reactive), while Gold and Platinum are at the bottom (least reactive).",
        "image_url": "assets/images/ch3_reactivity_series.jpg",
        "alt_text": "Reactivity Series of Metals"
    })

    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC:** Why are Sodium (Na) and Potassium (K) kept immersed in kerosene oil?\n\n**Answer Structure:** Because they are highly reactive (अत्यधिक क्रियाशील) and can easily catch fire when exposed to oxygen and moisture in the air.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    # ==========================================
    # MODULE 3: FORMATION OF IONIC BONDS
    # ==========================================
    blocks.append({
        "type": "diagram",
        "content": "Metals give away electrons and become positive ions (cations), while non-metals accept those electrons and become negative ions (anions). They attract each other strongly to form an Ionic Bond!",
        "image_url": "assets/images/ch3_ionic_bond.jpg",
        "alt_text": "Transfer of electrons from Sodium to Chlorine to form NaCl"
    })

    blocks.append({
        "type": "theory",
        "content": "**Ionic Compounds (आयनिक यौगिक / આયનીય સંયોજનો):**\nCompounds formed by the transfer of electrons from a metal to a non-metal are known as ionic or electrovalent compounds.\n\n*Properties:* They have high melting and boiling points, are solid and brittle, and conduct electricity in molten or aqueous state (but not in solid state).",
        "difficulty": "Intermediate",
        "bloom": "Apply"
    })

    # ==========================================
    # MODULE 4: METALLURGY & CORROSION
    # ==========================================
    blocks.append({
        "type": "diagram",
        "content": "The journey of a metal from the earth's crust to pure metal involves concentration of ore, conversion to oxide (roasting/calcination), reduction to metal, and finally refining.",
        "image_url": "assets/images/ch3_metallurgy.jpg",
        "alt_text": "Flowchart of Extraction of Metals from Ores"
    })

    blocks.append({
        "type": "theory",
        "content": "**Roasting (भर्जन) vs Calcination (निस्तापन):**\n- **Roasting:** Heating sulphide ores in the *presence* of excess air. (e.g., **2ZnS + 3O₂ ⟶ 2ZnO + 2SO₂**)\n- **Calcination:** Heating carbonate ores in the *limited* supply of air. (e.g., **ZnCO₃ ⟶ ZnO + CO₂**)",
        "difficulty": "Advanced",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC: Prevention of Corrosion (संक्षारण)**\nRusting of iron (**Fe₂O₃·xH₂O**) can be prevented by painting, oiling, greasing, galvanizing, chrome plating, or making alloys.\n*Galvanization:* Coating iron/steel with a thin layer of Zinc to protect it from rusting.",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_science_ch3.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_science_ch3.json"
    final_json["metadata"]["id"] = "gseb_class10_science_ch3"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Supreme Chapter 3 Generated Successfully!")

if __name__ == "__main__":
    generate_supreme_chapter_3()
