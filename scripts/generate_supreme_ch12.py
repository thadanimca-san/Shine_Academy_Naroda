import json
import os

def generate_supreme_chapter_12():
    chapter_id = "ncert_class10_science_ch12"
    title = "Chapter 12: Magnetic Effects of Electric Current"
    
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
        "tags": ["physics", "magnetism", "electric_current", "solenoid", "motor", "board_special", "bilingual"],
        "learning_outcomes": [
            "Understand the concept of magnetic fields and field lines.",
            "Explain the magnetic field due to a current-carrying conductor and a solenoid.",
            "Understand Fleming's Left-Hand Rule.",
            "Understand the working principle of an Electric Motor."
        ],
        "ai_context": {
            "learning_goal": "Transform the student from a beginner to a board-exam topper in Magnetic Effects of Electric Current. Use the 'Socratic Discovery Arc'.",
            "common_misconceptions": [
                "Students confuse electric field lines with magnetic field lines.",
                "Students struggle to apply Fleming's Left-Hand Rule correctly."
            ]
        }
    }
    
    blocks = []
    
    # ==========================================
    # MODULE 1: INTRODUCTION TO MAGNETIC EFFECTS
    # ==========================================
    blocks.append({
        "type": "hook",
        "content": "Have you ever played with magnets (चुंबक / ચુંબક) and noticed how they attract or repel each other? But did you know that electricity can also act like a magnet? This magical connection is called the **Magnetic Effect of Electric Current (विद्युत धारा के चुंबकीय प्रभाव / વિદ્યુત પ્રવાહની ચુંબકીય અસરો)**!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Magnetic field lines around a bar magnet showing the invisible force field that loops from North to South pole.",
        "image_url": "assets/images/ch12_magnetic_field.jpg",
        "alt_text": "Magnetic field lines of a bar magnet"
    })

    blocks.append({
        "type": "theory",
        "content": "A compass needle gets deflected when placed near a current-carrying wire. This proves that an electric current produces a **Magnetic Field (चुंबकीय क्षेत्र / ચુંબકીય ક્ષેત્ર)** around it.\n\n**Magnetic Field Lines (चुंबकीय क्षेत्र रेखाएँ / ચુંબકીય ક્ષેત્ર રેખાઓ):**\n- They always emerge from the North pole and merge at the South pole.\n- They form closed continuous curves.\n- They never intersect each other.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    # ==========================================
    # MODULE 2: MAGNETIC FIELD DUE TO CURRENT
    # ==========================================
    blocks.append({
        "type": "memory_trick",
        "content": "**Right-Hand Thumb Rule (दक्षिण-हस्त अंगुष्ठ नियम):**\nImagine holding a current-carrying straight conductor in your right hand. If the thumb points in the direction of the current, then your fingers wrap around the conductor in the direction of the magnetic field lines!",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "theory",
        "content": "What happens if we bend the wire into many circular turns? We get a **Solenoid (परिनालिका / સોલેનોઇડ)**!\nA coil of many circular turns of insulated copper wire wrapped closely in the shape of a cylinder is called a solenoid.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "diagram",
        "content": "A current-carrying solenoid behaves exactly like a bar magnet, with its own North and South poles.",
        "image_url": "assets/images/ch12_solenoid.jpg",
        "alt_text": "Magnetic field lines inside and outside a solenoid"
    })

    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC: Electromagnet (विद्युत चुंबक)**\nWhen a soft iron core is placed inside a current-carrying solenoid, it becomes a strong temporary magnet called an **Electromagnet**.\n\n**Board Question:** What happens to the magnetic field if we increase the current or the number of turns in the solenoid?\n**Answer:** The strength of the magnetic field increases proportionally!",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    # ==========================================
    # MODULE 3: FORCE ON CURRENT-CARRYING CONDUCTOR
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "When a current-carrying conductor is placed in a magnetic field, it experiences a force (बल / બળ). But how do we find the direction of this force? We use **Fleming's Left-Hand Rule (फ्लेमिंग का वामहस्त नियम)**!\n\nStretch your thumb, forefinger, and middle finger of your left hand so they are mutually perpendicular:\n- **F**orefinger = Magnetic **F**ield\n- **M**iddle finger = Current (**M**otion of charges)\n- **T**humb = Force or **T**hrust (Motion)",
        "difficulty": "Intermediate",
        "bloom": "Apply"
    })

    # ==========================================
    # MODULE 4: ELECTRIC MOTOR
    # ==========================================
    blocks.append({
        "type": "teacher_tip",
        "content": "Students, the Electric Motor is a guaranteed long-answer question for board exams. Understand the principle and the function of the split-ring commutator!",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "diagram",
        "content": "An Electric Motor converts electrical energy into mechanical energy.",
        "image_url": "assets/images/ch12_electric_motor.jpg",
        "alt_text": "Schematic diagram of an electric motor with magnets, coil, and split rings"
    })

    blocks.append({
        "type": "theory",
        "content": "**Electric Motor (विद्युत मोटर / વિદ્યુત મોટર):**\n- *Principle:* A current-carrying coil placed in a magnetic field experiences a torque (force) which makes it rotate.\n- *Commutator (दिक्परिवर्तक / કમ્યુટેટર):* A device that reverses the direction of current in a circuit. In an electric motor, the **split rings** act as a commutator.",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_science_ch12.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_science_ch12.json"
    final_json["metadata"]["id"] = "gseb_class10_science_ch12"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Supreme Chapter 12 Generated Successfully!")

if __name__ == "__main__":
    generate_supreme_chapter_12()
