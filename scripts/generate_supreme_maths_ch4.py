import json
import os

def generate_supreme_maths_ch4():
    chapter_id = "ncert_class10_maths_ch4"
    title = "Chapter 4: Quadratic Equations"
    
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
        "tags": ["maths", "quadratic_equations", "roots", "board_special", "bilingual"],
        "learning_outcomes": [
            "Identify quadratic equations in various forms.",
            "Solve quadratic equations using factorization and quadratic formula.",
            "Understand the nature of roots using the discriminant.",
            "Apply quadratic equations to solve real-life word problems."
        ],
        "ai_context": {
            "learning_goal": "Make abstract algebraic concepts visual. Connect quadratic equations to parabolic shapes in real life.",
            "common_misconceptions": [
                "Students confuse linear and quadratic equations.",
                "Students struggle with signs when using the quadratic formula."
            ]
        }
    }
    
    blocks = []
    
    # ==========================================
    # MODULE 1: INTRODUCTION
    # ==========================================
    blocks.append({
        "type": "hook",
        "content": "Imagine throwing a basketball into a hoop. The path the ball takes through the air is a perfect curve! This curve is called a parabola, and the mathematics that describes this beautiful arc is none other than **Quadratic Equations (द्विघात समीकरण / દ્વિઘાત સમીકરણ)**!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "A beautiful glowing parabola representing the path of a basketball, with its corresponding quadratic equation shown next to it.",
        "image_url": "assets/images/maths_ch4_parabola_basketball.jpg",
        "alt_text": "Basketball thrown in a parabolic arc."
    })
    
    # ==========================================
    # MODULE 2: STANDARD FORM
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "**Standard Form of a Quadratic Equation:**\nAny equation of the form **ax² + bx + c = 0**, where a, b, and c are real numbers and a ≠ 0, is a quadratic equation.\nThe highest power (degree) of x is exactly 2 (notice the superscript x²!).",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })
    
    # ==========================================
    # MODULE 3: SOLVING THE EQUATION
    # ==========================================
    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC:** The Quadratic Formula (श्रीधराचार्य सूत्र)\n\nTo find the roots (solutions) for x, use this magical formula:\n**x = [-b ± √(b² - 4ac)] / 2a**\n\n*Board Trick:* Always write the values of a, b, and c clearly with their signs before substituting them into the formula!",
        "difficulty": "Advanced",
        "bloom": "Apply"
    })
    
    # ==========================================
    # MODULE 4: NATURE OF ROOTS
    # ==========================================
    blocks.append({
        "type": "diagram",
        "content": "The Discriminant tells us the story of the roots before we even solve the equation! Let's see how parabolas behave based on D.",
        "image_url": "assets/images/maths_ch4_parabola_roots.jpg",
        "alt_text": "Three parabolas showing two real roots, one real root, and no real roots."
    })

    blocks.append({
        "type": "memory_trick",
        "content": "**The Discriminant (D = b² - 4ac):**\nThink of D as a magic detector!\n1. If **D > 0**: Two distinct real roots (The parabola cuts the x-axis twice).\n2. If **D = 0**: Two equal real roots (The parabola just touches the x-axis).\n3. If **D < 0**: No real roots (The parabola never touches the x-axis).",
        "difficulty": "Intermediate",
        "bloom": "Analyze"
    })
    
    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    # Ensure directory exists before writing
    os.makedirs("/home/ubuntu/Shine_Academy_Naroda/app_core/chapters", exist_ok=True)
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_maths_ch4.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(final_json, f, indent=2, ensure_ascii=False)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_maths_ch4.json"
    final_json["metadata"]["id"] = "gseb_class10_maths_ch4"
    with open(gseb_path, "w", encoding="utf-8") as f:
        json.dump(final_json, f, indent=2, ensure_ascii=False)
        
    print("Supreme Maths Chapter 4 Generated Successfully!")

if __name__ == "__main__":
    generate_supreme_maths_ch4()
