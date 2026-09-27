import json
import os

def generate_supreme_maths_ch11():
    chapter_id = "ncert_class10_maths_ch11"
    title = "Chapter 11: Constructions"
    
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
        "tags": ["maths", "constructions", "geometry", "board_special", "bilingual"],
        "learning_outcomes": [
            "Master the division of a line segment in a given ratio.",
            "Construct a triangle similar to a given triangle.",
            "Construct tangents to a circle from an external point.",
            "Write perfect steps of construction for board exams."
        ],
        "ai_context": {
            "learning_goal": "Make constructions intuitive and precise. Explain 'why' each step works instead of just 'how' to do it.",
            "common_misconceptions": [
                "Students forget to write the steps of construction or justification.",
                "Students get confused with the scale factor (proper vs improper fraction)."
            ]
        }
    }
    
    blocks = []
    
    # ==========================================
    # MODULE 1: INTRODUCTION
    # ==========================================
    blocks.append({
        "type": "hook",
        "content": "Have you ever wondered how architects draw perfectly scaled blueprints for skyscrapers or bridges? They use the power of geometric constructions! In this chapter, all you need is a compass, a ruler, and the logic of similar triangles to create perfect geometrical shapes.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "The Architect's Tools: Compass, Ruler, and Pencil.",
        "image_url": "assets/images/maths_ch11_tools.jpg",
        "alt_text": "An image showing geometry box tools like compass, ruler, and pencil."
    })

    # ==========================================
    # MODULE 2: DIVISION OF A LINE SEGMENT
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "**Division of a Line Segment (रेखाखंड का विभाजन):**\nTo divide a line segment AB in a given ratio m:n, we draw a ray AX making an acute angle with AB, then locate m+n points at equal distances on AX. We join the last point to B, and draw a line parallel to it from the m-th point to intersect AB.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Teacher's Secret:** The justification for dividing a line segment lies in **Thales Theorem (Basic Proportionality Theorem)**. The parallel lines create similar triangles!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    # ==========================================
    # MODULE 3: CONSTRUCTING SIMILAR TRIANGLES
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "**Constructing a Similar Triangle:**\nWhen constructing a triangle similar to a given triangle, the **scale factor (m/n)** decides the size.\n- If m/n < 1, the new triangle is **smaller** (inside the original).\n- If m/n > 1, the new triangle is **larger** (outside the original).",
        "difficulty": "Advanced",
        "bloom": "Apply"
    })

    blocks.append({
        "type": "diagram",
        "content": "Visualizing scale factors: Smaller vs Larger similar triangles.",
        "image_url": "assets/images/maths_ch11_scale_factor.jpg",
        "alt_text": "Diagram showing two sets of similar triangles, one scaled down and one scaled up."
    })

    # ==========================================
    # MODULE 4: TANGENTS TO A CIRCLE
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "**Steps of Construction: Tangents from an External Point (बाह्य बिंदु से स्पर्श रेखाएँ):**\nLet the circle have center O, and P be an external point.\n1. Join PO and bisect it. Let M be the midpoint of PO.\n2. Taking M as center and MO as radius, draw a circle. Let it intersect the given circle at points Q and R.\n3. Join PQ and PR. Then PQ and PR are the required two tangents.\n\n*Justification:* The angle in a semi-circle is a right angle. Since PQ is perpendicular to the radius OQ, PQ must be a tangent!",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC:** Steps of Construction and Justification\n\n*Board Trick:* Examiners don't just look at your drawing! You MUST write the steps clearly and often provide the geometric justification. Always keep your pencil sharp and draw neat arcs. Don't erase the construction arcs!",
        "difficulty": "Advanced",
        "bloom": "Apply"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_maths_ch11.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_maths_ch11.json"
    final_json["metadata"]["id"] = "gseb_class10_maths_ch11"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Supreme Maths Chapter 11 Generated Successfully!")

if __name__ == "__main__":
    generate_supreme_maths_ch11()
