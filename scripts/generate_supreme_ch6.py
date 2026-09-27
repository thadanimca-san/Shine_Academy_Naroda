import json
import os

def generate_supreme_chapter_6():
    chapter_id = "ncert_class10_science_ch6"
    title = "Chapter 6: Control and Coordination"
    
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
        "tags": ["biology", "control", "coordination", "neuron", "brain", "hormones", "board_special", "bilingual"],
        "learning_outcomes": [
            "Understand the structure and function of a Neuron.",
            "Identify the main parts of the Human Brain and their functions.",
            "Explain how plants coordinate without a nervous system using Plant Hormones.",
            "Master the difference between voluntary, involuntary, and reflex actions."
        ],
        "ai_context": {
            "learning_goal": "Transform the student from a beginner to a board-exam topper in Control and Coordination. Use the 'Socratic Discovery Arc'.",
            "common_misconceptions": [
                "Students think plants have a nervous system. (Fact: Plants use chemical coordination via hormones).",
                "Students confuse cerebrum and cerebellum functions."
            ]
        }
    }
    
    blocks = []
    
    # ==========================================
    # MODULE 1: THE NERVOUS SYSTEM & NEURON
    # ==========================================
    blocks.append({
        "type": "hook",
        "content": "Imagine you accidentally touch a hot pan (गर्म बर्तन / ગરમ વાસણ). You instantly pull your hand away without even thinking! How did your hand know it was hot? How did the message reach your muscles so fast? Welcome to the fascinating world of **Control and Coordination (नियंत्रण एवं समन्वय / નિયંત્રણ અને સંકલન)**!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "The Neuron is the fundamental unit of our nervous system, designed to transmit electrical signals at lightning speed.",
        "image_url": "assets/images/ch6_neuron.jpg",
        "alt_text": "Structure of a Neuron showing Dendrites, Cell Body, Axon, and Nerve Ending"
    })

    blocks.append({
        "type": "theory",
        "content": "The **Neuron (तंत्रिका कोशिका / ચેતાકોષ)** is the longest cell in the human body. It has three main parts:\n1. **Dendrite (द्रुमिका / શિખાતંતુ):** Receives the signal.\n2. **Cell Body & Axon (कोशिका पिंड और तंत्रिकाक्ष / કોષકાય અને અક્ષતંતુ):** Carries the electrical impulse.\n3. **Nerve Ending:** Releases chemicals (neurotransmitters) into the **Synapse (अंतर्ग्रथन / ચેતોપાગમ)** to pass the message to the next neuron.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC:** What is a Synapse? \n\n**Answer:** It is the microscopic gap between two adjacent neurons. Electrical signals cannot jump this gap, so they are converted into chemical signals to cross the synapse.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    # ==========================================
    # MODULE 2: THE HUMAN BRAIN
    # ==========================================
    blocks.append({
        "type": "diagram",
        "content": "The Human Brain is the ultimate supercomputer, protected by the skull and cerebrospinal fluid.",
        "image_url": "assets/images/ch6_human_brain.jpg",
        "alt_text": "Human Brain showing Fore-brain, Mid-brain, and Hind-brain"
    })

    blocks.append({
        "type": "theory",
        "content": "The **Human Brain (मानव मस्तिष्क / માનવ મગજ)** is divided into three main regions:\n\n1. **Fore-brain (अग्रमस्तिष्क / અગ્રમગજ):** The main thinking part. Contains the **Cerebrum (प्रमस्तिष्क / બૃહદ મસ્તિષ્ક)**, responsible for reasoning, memory, and voluntary actions.\n2. **Mid-brain (मध्यमस्तिष्क / મધ્યમગજ):** Controls involuntary actions like pupil size changes.\n3. **Hind-brain (पश्चमस्तिष्क / પશ્વમગજ):** Contains the **Cerebellum (अनुमस्तिष्क / અનુમસ્તિષ્ક)** which controls posture and balance (like riding a bicycle), and the Medulla which controls heartbeat and breathing.",
        "difficulty": "Intermediate",
        "bloom": "Apply"
    })

    # ==========================================
    # MODULE 3: COORDINATION IN PLANTS
    # ==========================================
    blocks.append({
        "type": "hook",
        "content": "Plants don't have a brain or a nervous system. So how does a sunflower know to face the sun? How do roots know to grow downwards? The secret lies in chemicals!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "diagram",
        "content": "Plant hormones coordinate growth, development, and responses to the environment.",
        "image_url": "assets/images/ch6_plant_hormones.jpg",
        "alt_text": "Plant showing action of Auxins, Gibberellins, and Cytokinins"
    })
    
    blocks.append({
        "type": "theory",
        "content": "**Plant Hormones (पादप हार्मोन / વનસ્પતિ અંતઃસ્ત્રાવો) or Phytohormones:**\n\n1. **Auxin (ऑक्सिन):** Synthesized at the shoot tip. Helps the cells to grow longer. It bends the stem towards light (**Phototropism / प्रकाशानुवर्तन / પ્રકાશાનુવર્તન**).\n2. **Gibberellins (जिबरेलिन):** Help in the growth of the stem.\n3. **Cytokinins (साइटोकाइनिन):** Promote cell division (found in fruits and seeds).\n4. **Abscisic Acid (एब्सिसिक अम्ल):** The 'villain' hormone! It inhibits growth and causes wilting of leaves.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    os.makedirs("/home/ubuntu/Shine_Academy_Naroda/app_core/chapters", exist_ok=True)
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_science_ch6.json"
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_science_ch6.json"
    final_json["metadata"]["id"] = "gseb_class10_science_ch6"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Supreme Chapter 6 Generated Successfully!")

if __name__ == "__main__":
    generate_supreme_chapter_6()
