import json
import os

def generate_supreme_chapter_4():
    chapter_id = "ncert_class10_science_ch4"
    title = "Chapter 4: Carbon and its Compounds"
    
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
        "tags": ["chemistry", "carbon", "covalent", "allotropes", "micelle", "board_special", "bilingual"],
        "learning_outcomes": [
            "Understand the versatile nature of Carbon.",
            "Master Covalent bonding.",
            "Explain the allotropes of Carbon.",
            "Understand soaps, detergents, and micelle formation."
        ],
        "ai_context": {
            "learning_goal": "Transform the student from a beginner to a board-exam topper in Carbon and its Compounds. Use the 'Socratic Discovery Arc'.",
            "common_misconceptions": [
                "Students confuse covalent bonds with ionic bonds.",
                "Students struggle with the concept of micelle formation in cleansing action."
            ]
        }
    }
    
    blocks = []
    
    # MODULE 1: INTRODUCTION TO CARBON
    blocks.append({
        "type": "hook",
        "content": "Look around you! The food you eat, the clothes you wear, the medicines you take, and even your own body (आपका शरीर / તમારું શરીર) are all made up of a magical element. Can you guess? It is **Carbon (कार्बन / કાર્બન)**!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    # MODULE 2: COVALENT BONDS
    blocks.append({
        "type": "theory",
        "content": "Carbon has 4 electrons in its outermost shell (valence shell). To become stable, it needs 4 more electrons. But losing or gaining 4 electrons is very difficult! So, it **shares** its electrons with other atoms. This sharing forms a **Covalent Bond (सहसंयोजी आबंध / સહસંયોજક બંધ)**.\n\n*Example:* Methane (**CH₄**). Carbon shares its 4 valence electrons with 4 Hydrogen atoms.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "diagram",
        "content": "Carbon shares electrons with other atoms to complete its octet, forming strong covalent bonds.",
        "image_url": "assets/images/ch4_covalent_bond.jpg",
        "alt_text": "Covalent bonding in Carbon"
    })

    # MODULE 3: ALLOTROPES OF CARBON
    blocks.append({
        "type": "theory",
        "content": "**Allotropes of Carbon (कार्बन के अपररूप / કાર્બનના બહુરૂપો):**\nThe same element Carbon can exist in very different forms physically, even though chemically they are the same.\n\n1. **Diamond (हीरा / હીરો):** The hardest natural substance. Each Carbon atom is bonded to 4 other Carbon atoms in a rigid 3D structure.\n2. **Graphite (ग्रेफाइट / ગ્રેફાઇટ):** Soft and slippery. It conducts electricity! Each Carbon atom is bonded to 3 other Carbon atoms in hexagonal layers.\n3. **Fullerene (फुलरिन / ફુલેરીન):** Looks like a football (e.g., C₆₀).",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "diagram",
        "content": "The structures of Diamond, Graphite, and Fullerene show how differently Carbon atoms can arrange themselves.",
        "image_url": "assets/images/ch4_allotropes.jpg",
        "alt_text": "Structures of Diamond, Graphite, and Fullerene"
    })

    # MODULE 4: SOAPS AND MICELLES
    blocks.append({
        "type": "theory",
        "content": "**Cleansing Action of Soap (साबुन की सफाई प्रक्रिया / સાબુની સફાઈ પ્રક્રિયા):**\nWhen soap is added to water, its molecules arrange themselves in a unique spherical cluster called a **Micelle (मिसेल / મિસેલ)**.\n\nThe soap molecule has two ends:\n- **Hydrophilic (जलरागी / જળઅનુરાગી) head:** Loves water, dissolves in water.\n- **Hydrophobic (जलविरागी / જળવિરાગી) tail:** Hates water, attaches to oil and dirt.\n\nThese micelles trap the dirt in the center and can be easily washed away with water!",
        "difficulty": "Advanced",
        "bloom": "Apply"
    })

    blocks.append({
        "type": "diagram",
        "content": "A micelle is a spherical cluster where the hydrophobic tails point inward (trapping the dirt), and the hydrophilic heads point outward towards the water.",
        "image_url": "assets/images/ch4_micelle.jpg",
        "alt_text": "Micelle formation showing hydrophilic head and hydrophobic tail"
    })
    
    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC: Why doesn't soap work well in hard water?**\n\n**Answer Structure:** Hard water contains Calcium (Ca²⁺) and Magnesium (Mg²⁺) ions. Soap reacts with these ions to form an insoluble substance called **Scum (स्कम)** instead of lather (झाग), which reduces its cleaning power.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_science_ch4.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_science_ch4.json"
    final_json["metadata"]["id"] = "gseb_class10_science_ch4"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Supreme Chapter 4 Generated Successfully!")

if __name__ == "__main__":
    generate_supreme_chapter_4()
