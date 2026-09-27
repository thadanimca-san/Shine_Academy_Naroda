import json
import os

def generate_supreme_chapter_11():
    chapter_id = "ncert_class10_science_ch11"
    title = "Chapter 11: Electricity"
    
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
        "tags": ["physics", "electricity", "current", "ohms_law", "resistance", "board_special", "bilingual"],
        "learning_outcomes": [
            "Master the concepts of Electric Current and Potential Difference.",
            "Understand Ohm's Law and its mathematical representation.",
            "Calculate equivalent resistance for series and parallel circuits.",
            "Solve CBSE/State Board HOTS questions about Electric Power and Heating Effect."
        ],
        "ai_context": {
            "learning_goal": "Transform the student from a beginner to a board-exam topper in Electricity. Use the 'Socratic Discovery Arc'.",
            "common_misconceptions": [
                "Students think positive charges move in a circuit. (Fact: Electrons flow from negative to positive, while conventional current is positive to negative).",
                "Students confuse voltage with current."
            ]
        }
    }
    
    blocks = []
    
    # ==========================================
    # MODULE 1: INTRODUCTION TO ELECTRICITY
    # ==========================================
    blocks.append({
        "type": "hook",
        "content": "Imagine a world without your smartphone, TV, or even fans! Everything would come to a standstill. What invisible magic powers all these devices? It's **Electricity (विद्युत / વિદ્યુત)**!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "A simple electric circuit showing a battery, a bulb, and the flow of electrons.",
        "image_url": "assets/images/ch11_electric_circuit.jpg",
        "alt_text": "Simple Electric Circuit with Battery and Bulb"
    })

    blocks.append({
        "type": "theory",
        "content": "Electric Current (विद्युत धारा / વિદ્યુત પ્રવાહ) is the rate of flow of electric charges. The SI unit of electric current is Ampere (A).\n*Formula:* **I = Q / t** (Current = Charge / Time)\n\nPotential Difference (विभवांतर / વિદ્યુત સ્થિતિમાનનો તફાવત) is the work done to move a unit charge from one point to another.\n*Formula:* **V = W / Q** (Voltage = Work / Charge)",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "memory_trick",
        "content": "**Ammeter vs Voltmeter:**\n- **A**mmeter measures Current (**A**mpere) and is always connected in **Series**.\n- **V**oltmeter measures **V**oltage and is always connected in **Parallel**.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    # ==========================================
    # MODULE 2: OHM'S LAW
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "**Ohm's Law (ओम का नियम / ઓહ્મનો નિયમ):**\nAt a constant temperature, the current flowing through a conductor is directly proportional to the potential difference across its ends.\n*Formula:* **V = I × R**\nWhere **R** is the Resistance (प्रतिरोध / અવરોધ).",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "diagram",
        "content": "A graph showing the linear relationship between Voltage (V) and Current (I) for an ohmic conductor.",
        "image_url": "assets/images/ch11_ohms_law.jpg",
        "alt_text": "V-I Graph for Ohm's Law"
    })

    # ==========================================
    # MODULE 3: RESISTANCE IN SERIES AND PARALLEL
    # ==========================================
    blocks.append({
        "type": "teacher_tip",
        "content": "Students, circuit numericals (सर्किट के सवाल) are guaranteed to appear in your board exams! Let's understand how to combine resistances.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "theory",
        "content": "**1. Resistors in Series (श्रेणीक्रम में प्रतिरोध):**\nThe equivalent resistance is the sum of individual resistances.\n*Formula:* **R_s = R₁ + R₂ + R₃**\n\n**2. Resistors in Parallel (पार्श्वक्रम में प्रतिरोध):**\nThe reciprocal of equivalent resistance is the sum of reciprocals of individual resistances.\n*Formula:* **1/R_p = 1/R₁ + 1/R₂ + 1/R₃**",
        "difficulty": "Advanced",
        "bloom": "Apply"
    })

    blocks.append({
        "type": "diagram",
        "content": "Visual comparison of resistors connected end-to-end (series) vs connected across the same two points (parallel).",
        "image_url": "assets/images/ch11_resistances.jpg",
        "alt_text": "Resistors in Series and Parallel"
    })
    
    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC:** Why are domestic circuits connected in parallel?\n\n**Answer Structure:** Because in a parallel circuit: 1) If one appliance stops working, others keep working. 2) Each appliance gets the same voltage (220V).",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_science_ch11.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_science_ch11.json"
    final_json["metadata"]["id"] = "gseb_class10_science_ch11"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Supreme Chapter 11 Generated Successfully!")

if __name__ == "__main__":
    generate_supreme_chapter_11()
