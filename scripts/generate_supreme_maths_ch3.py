import json
import os

def generate_supreme_maths_ch3():
    chapter_id = "ncert_class10_maths_ch3"
    title = "Chapter 3: Pair of Linear Equations in Two Variables"
    
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
        "tags": ["maths", "linear_equations", "algebra", "board_special", "bilingual"],
        "learning_outcomes": [
            "Understand the geometric meaning of pair of linear equations.",
            "Solve linear equations algebraically (Substitution, Elimination).",
            "Identify consistency and inconsistency.",
            "Formulate and solve real-life word problems."
        ],
        "ai_context": {
            "learning_goal": "Help students visualize linear equations as straight lines. Understand the intersection points as solutions.",
            "common_misconceptions": [
                "Students struggle to translate word problems into algebraic equations.",
                "Students confuse a₁/a₂ ≠ b₁/b₂ with no solution instead of unique solution."
            ]
        }
    }
    
    blocks = []
    
    # ==========================================
    # MODULE 1: INTRODUCTION & GRAPHICAL MEANING
    # ==========================================
    blocks.append({
        "type": "hook",
        "content": "Imagine you go to a stationery shop. You buy 2 pencils and 3 erasers for ₹9. Your friend buys 4 pencils and 6 erasers of the same kind for ₹18. Can we find the price of each pencil and eraser? Welcome to the world of **Linear Equations in Two Variables (दो चर वाले रैखिक समीकरण / દ્વિચલ સુરેખ સમીકરણ)**!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Graphical Representation: Intersecting Lines. This means there is exactly one solution. (अद्वितीय हल / અનન્ય ઉકેલ)",
        "image_url": "assets/images/maths_ch3_intersecting.jpg",
        "alt_text": "Graph showing two straight lines intersecting at a single point."
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Graphical Representation: Parallel Lines. This means there is NO solution. (कोई हल नहीं / ઉકેલ નથી)",
        "image_url": "assets/images/maths_ch3_parallel.jpg",
        "alt_text": "Graph showing two straight lines that are perfectly parallel."
    })
    
    # ==========================================
    # MODULE 2: ALGEBRAIC CONDITIONS
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "**Standard Form:**\na₁x + b₁y + c₁ = 0\na₂x + b₂y + c₂ = 0\n\n**Conditions:**\n1. Intersecting Lines (Unique Solution): a₁/a₂ ≠ b₁/b₂\n2. Coincident Lines (Infinitely Many Solutions): a₁/a₂ = b₁/b₂ = c₁/c₂\n3. Parallel Lines (No Solution): a₁/a₂ = b₁/b₂ ≠ c₁/c₂",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC:** Consistency\nIf equations have at least one solution (intersecting or coincident), they are **Consistent (संगत / સુસંગત)**.\nIf they have no solution (parallel), they are **Inconsistent (असंगत / અસુસંગત)**.",
        "difficulty": "Advanced",
        "bloom": "Apply"
    })

    # ==========================================
    # MODULE 3: ALGEBRAIC METHODS
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "**Elimination Method (विलोपन विधि / લોપની રીત):**\nStep 1: Multiply equations to make the coefficients of one variable (x or y) equal.\nStep 2: Add or subtract to eliminate that variable.\nStep 3: Solve for the remaining variable.\nStep 4: Substitute back to find the eliminated variable.",
        "difficulty": "Intermediate",
        "bloom": "Apply"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_maths_ch3.json"
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_maths_ch3.json"
    final_json["metadata"]["id"] = "gseb_class10_maths_ch3"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Supreme Maths Chapter 3 Generated Successfully!")

if __name__ == "__main__":
    generate_supreme_maths_ch3()
