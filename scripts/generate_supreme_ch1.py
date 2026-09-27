import json
import os

def generate_supreme_chapter():
    chapter_id = "ncert_class10_science_ch1"
    title = "Chapter 1: Chemical Reactions and Equations"
    
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
        "tags": ["chemistry", "reactions", "equations", "balancing", "redox", "board_special", "bilingual"],
        "learning_outcomes": [
            "Master the art of balancing ANY chemical equation mathematically.",
            "Identify 5 major types of chemical reactions instantly.",
            "Solve CBSE/State Board HOTS and Assertion-Reasoning questions.",
            "Understand Redox reactions in everyday life (Rusting, Rancidity)."
        ],
        "ai_context": {
            "learning_goal": "Transform the student from a beginner to a board-exam topper in Chemical Reactions. Use extreme depth, analogies, and step-by-step logic. Content is bilingual to help English-medium students who struggle with pure English.",
            "common_misconceptions": [
                "Students often change subscripts (like O₂ to O₃) while balancing instead of coefficients.",
                "Students confuse Displacement with Double Displacement.",
                "Students struggle to identify the oxidizing/reducing agent."
            ],
            "tutor_hint": "If a student fails a balancing question, drop down to the 'See-Saw' analogy. If they fail Redox, remind them OIL RIG (Oxidation Is Loss, Reduction Is Gain)."
        }
    }
    
    blocks = []
    
    # ==========================================
    # MODULE 1: THE MAGIC OF CHEMISTRY AROUND US
    # ==========================================
    blocks.append({
        "type": "real_world_example",
        "content": "Look at an iron gate rusting in the rain (लोहे पर जंग लगना / લોખંડને કાટ લાગવો). Smell the sour milk (दूध का खट्टा होना / દૂધ ખાટું થવું) left out in the summer heat. Watch a Diwali firecracker explode in a burst of colors. What do these have in common? They are all **Chemical Reactions (रासायनिक अभिक्रिया / રાસાયણિક પ્રતિક્રિયા)**! Chemistry isn't just in test tubes; it's the invisible magic running the universe.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Here is a comparison between a slow chemical reaction (Rusting) and a fast chemical reaction (Burning). Notice how in both cases, entirely new substances are formed!",
        "image_url": "assets/images/chemical_vs_physical_1786850644356.jpg",
        "alt_text": "Rusting Iron Gate vs Burning Paper"
    })

    blocks.append({
        "type": "ai_tutor_prompt",
        "content": "So, if you tear a piece of paper, it's a physical change (भौतिक परिवर्तन / ભૌતિક પરિવર્તન). But if you BURN that same piece of paper, is it physical or chemical? Why?",
        "options": ["Physical, because it's still paper.", "Chemical, because ash and smoke are new substances.", "Neither."],
        "correct_answer": "Chemical, because ash and smoke are new substances.",
        "explanation": "Burning (दहन / દહન) creates entirely new substances with new properties, making it an irreversible chemical change."
    })
    
    blocks.append({
        "type": "theory",
        "content": "A **Chemical Reaction (रासायनिक अभिक्रिया / રાસાયણિક પ્રતિક્રિયા)** is a process where the bonds between atoms are broken and new bonds are formed, creating completely new substances (नए पदार्थ / નવા પદાર્થો). \n\nYou can identify a chemical reaction if you observe any of these four things: \n1. Change in State (अवस्था में परिवर्तन / સ્થિતિમાં ફેરફાર) \n2. Change in Colour (रंग में परिवर्तन / રંગમાં ફેરફાર) \n3. Evolution of a Gas (गैस का निकलना / ગેસનું ઉત્સર્જન) \n4. Change in Temperature (तापमान में परिवर्तन / તાપમાનમાં ફેરફાર).",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    blocks.append({
        "type": "memory_trick",
        "content": "**Mnemonic to Remember signs of a Chemical Reaction:** \n**C**ity **C**ats **G**et **T**hirsty.\n- **C**olour change\n- **C**hemical State change\n- **G**as evolution\n- **T**emperature change",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    # ==========================================
    # MODULE 2: BALANCING EQUATIONS (STEP-BY-STEP)
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "Why do we balance equations? We MUST follow the **Law of Conservation of Mass (द्रव्यमान संरक्षण का नियम / દળ સંરક્ષણનો નિયમ)**: 'Mass can neither be created nor destroyed in a chemical reaction.' \nIf you start with 2 atoms of Hydrogen on the left side, you MUST end with 2 atoms of Hydrogen on the right side. The universe doesn't do magic tricks with atoms!",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "diagram",
        "content": "Think of a chemical equation like a perfectly balanced antique weighing scale (तराज़ू / ત્રાજવું). The atoms on the left (Reactants) must exactly match the atoms on the right (Products).",
        "image_url": "assets/images/atoms_weighing_scale_1786850335332.jpg",
        "alt_text": "Weighing scale balancing atoms"
    })

    blocks.append({
        "type": "common_mistakes",
        "content": "⚠️ **THE GOLDEN RULE OF BALANCING:** \nYou can ONLY change the coefficients (the big numbers in front). You can NEVER change the subscripts (the small numbers). \nChanging H₂O to H₂O₂ is not balancing; you just turned drinking water (पानी) into toxic hydrogen peroxide (ज़हर)!",
        "difficulty": "Intermediate",
        "bloom": "Analyze"
    })
    blocks.append({
        "type": "worked_example",
        "content": "**Let's balance the rusting of iron (लोहे पर जंग लगना):** \n\n**Step 1 (Unbalanced):** Fe + H₂O ⟶ Fe₃O₄ + H₂\n\n**Step 2 (Fix Oxygen):** We have 4 O on the right, so put a 4 in front of H₂O.\nFe + 4H₂O ⟶ Fe₃O₄ + H₂\n\n**Step 3 (Fix Hydrogen):** We now have 8 H on the left, so put a 4 in front of H₂.\nFe + 4H₂O ⟶ Fe₃O₄ + 4H₂\n\n**Step 4 (Fix Iron):** We need 3 Fe on the left.\n\n**Final Balanced Equation:** \n**3Fe + 4H₂O ⟶ Fe₃O₄ + 4H₂**",
        "difficulty": "Advanced",
        "bloom": "Apply"
    })

    # ==========================================
    # MODULE 3: TYPES OF REACTIONS (COMBINATION & DECOMPOSITION)
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "Just like human relationships, chemicals have different ways of interacting. Let's look at the first two: \n\n1. **Combination Reaction (संयोजन अभिक्रिया / સંયોજન પ્રતિક્રિયા):** Two or more substances combine to form a single product. (A + B ⟶ AB)\n*Example:* Burning of Coal (C + O₂ ⟶ CO₂)\n\n2. **Decomposition Reaction (वियोजन अभिक्रिया / વિઘટન પ્રતિક્રિયા):** A single reactant breaks down to give simpler products. (AB ⟶ A + B)\n*Example:* Heating Limestone (CaCO₃ ⟶ CaO + CO₂)",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    # ==========================================
    # MODULE 4: DISPLACEMENT & DOUBLE DISPLACEMENT
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "3. **Displacement Reaction (विस्थापन अभिक्रिया / વિસ્થાપન પ્રતિક્રિયા - The Bully):** A more reactive element kicks out a less reactive element from its compound. (A + BC ⟶ AC + B)\n*Example:* Fe + CuSO₄ ⟶ FeSO₄ + Cu (Iron kicks out Copper because it is more reactive/ताकतवर).\n\n4. **Double Displacement (द्विविस्थापन अभिक्रिया / દ્વિવિસ્થાપન પ્રતિક્રિયા - Wife Swap):** There is an exchange of ions between the reactants. (AB + CD ⟶ AD + CB)\n*Example:* Na₂SO₄ + BaCl₂ ⟶ BaSO₄ + 2NaCl",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "diagram",
        "content": "A highly reactive metal (like Iron - the superhero) will forcefully kick out a weaker metal (like Copper) from its compound (the castle). This is Displacement!",
        "image_url": "assets/images/displacement_reaction_1786850629581.jpg",
        "alt_text": "Superhero iron kicking out copper"
    })

    # ==========================================
    # MODULE 5: OXIDATION AND REDUCTION (REDOX)
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "**Oxidation (उपचयन / ઓક્સિડેશન)** is the addition of Oxygen OR the removal of Hydrogen.\n**Reduction (अपचयन / રિડક્શન)** is the addition of Hydrogen OR the removal of Oxygen.\n\nWhen Oxidation and Reduction happen together in the same reaction, it is called a **Redox Reaction (रेडॉक्स अभिक्रिया)**.\n*Example:* CuO + H₂ ⟶ Cu + H₂O",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })
    
    # ==========================================
    # MODULE 6: BOARD EXAM MASTERY (PYQs & HOTS)
    # ==========================================
    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC (Exam me zarur aayega!):** The CBSE/State Boards ALWAYS ask about the color change when Iron nails are dipped in Copper Sulphate solution. \n\n**Answer Structure:** State the reaction type (Displacement), write the balanced equation (**Fe + CuSO₄ ⟶ FeSO₄ + Cu**), and mention that the blue colour of CuSO₄ fades to light green (FeSO₄) and a brown coating of copper deposits on the iron nail.",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_science_ch1.json"
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    # Also sync to GSEB immediately
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_science_ch1.json"
    final_json["metadata"]["id"] = "gseb_class10_science_ch1"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Supreme Bilingual Visual Chapter Generated with Subscripts!")

if __name__ == "__main__":
    generate_supreme_chapter()
