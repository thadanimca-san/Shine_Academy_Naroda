import json
import os

def generate_supreme_maths_ch8():
    chapter_id = "ncert_class10_maths_ch8"
    title = "Chapter 8: Introduction to Trigonometry"
    
    metadata = {
        "id": chapter_id,
        "title": title,
        "subtitle": "The Ultimate Board Exam Mastery Guide",
        "subject": "Maths",
        "grade": "10",
        "board": "NCERT/CBSE",
        "curriculum": ["Universal"],
        "language": "English/Hindi/Gujarati (Bilingual)",
        "difficulty": "Advanced",
        "estimated_minutes": 180,
        "version": "3.0.0-SUPREME-MATHS",
        "author": "Antigravity Supreme Intelligence",
        "reviewed_by": "Chief Academic Architect",
        "tags": ["maths", "trigonometry", "sin_cos_tan", "board_special", "bilingual"],
        "learning_outcomes": [
            "Master trigonometric ratios.",
            "Understand and apply SOH CAH TOA.",
            "Solve CBSE/State Board HOTS questions related to trigonometric identities.",
            "Apply logic to real-world scenarios involving heights and distances."
        ],
        "ai_context": {
            "learning_goal": "Make abstract trigonometry feel real. Use the 'Socratic Discovery Arc' to build intuition before giving formulas.",
            "common_misconceptions": [
                "Students get confused about opposite and adjacent sides.",
                "Students forget the trigonometric identities."
            ]
        }
    }
    
    blocks = []
    
    # ==========================================
    # MODULE 1: INTRODUCTION
    # ==========================================
    blocks.append({
        "type": "hook",
        "content": "Imagine you are looking at the top of the Burj Khalifa from a distance. If you know the angle at which you are looking up and how far you are from the building, can you find its exact height without measuring it directly? Yes! This is the magic of **Trigonometry (त्रिकोणमिति / ત્રિકોણમિતિ)**!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "The Right Angled Triangle: The foundation of all trigonometry.",
        "image_url": "assets/images/maths_ch8_triangle.jpg",
        "alt_text": "A right angled triangle highlighting the Hypotenuse, Opposite, and Adjacent sides with respect to angle θ."
    })

    # ==========================================
    # MODULE 2: TRIGONOMETRIC RATIOS
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "**Trigonometric Ratios (त्रिकोणमितीय अनुपात):**\nThese are ratios of the lengths of the sides of a right-angled triangle. They relate the angles of a triangle to the lengths of its sides.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "memory_trick",
        "content": "💡 **Teacher's Secret (The SOH CAH TOA Trick):**\nRemember this to easily recall the formulas:\n**SOH** -> **S**in = **O**pposite / **H**ypotenuse\n**CAH** -> **C**os = **A**djacent / **H**ypotenuse\n**TOA** -> **T**an = **O**pposite / **A**djacent",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Visual representation of SOH CAH TOA to cement it in your memory.",
        "image_url": "assets/images/maths_ch8_sohcahtoa.jpg",
        "alt_text": "A colorful infographic showing SOH CAH TOA with corresponding triangle sides highlighted."
    })

    # ==========================================
    # MODULE 3: TRIGONOMETRIC IDENTITIES
    # ==========================================
    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC:** The Supreme Identity\n\nThis is the most important identity in trigonometry:\n**sin²θ + cos²θ = 1**\n\n*Board Trick:* Almost every proof question in the exam will use this identity directly or indirectly. Memorize it!",
        "difficulty": "Advanced",
        "bloom": "Apply"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_maths_ch8.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_maths_ch8.json"
    final_json["metadata"]["id"] = "gseb_class10_maths_ch8"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Supreme Maths Chapter 8 Generated Successfully!")

if __name__ == "__main__":
    generate_supreme_maths_ch8()
