import json
import os

def generate_supreme_maths_ch10():
    chapter_id = "ncert_class10_maths_ch10"
    title = "Chapter 10: Circles"
    
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
        "tags": ["maths", "circles", "tangents", "board_special", "bilingual"],
        "learning_outcomes": [
            "Understand the concept of a tangent to a circle.",
            "Prove that the tangent at any point of a circle is perpendicular to the radius through the point of contact.",
            "Prove that the lengths of tangents drawn from an external point to a circle are equal.",
            "Solve complex geometrical problems involving circles."
        ],
        "ai_context": {
            "learning_goal": "Make abstract circle properties visual and intuitive. Use the 'Socratic Discovery Arc' to build intuition for tangents.",
            "common_misconceptions": [
                "Students confuse a secant and a tangent.",
                "Students assume tangent theorems apply to intersecting lines from inside the circle."
            ]
        }
    }
    
    blocks = []
    
    # ==========================================
    # MODULE 1: INTRODUCTION
    # ==========================================
    blocks.append({
        "type": "hook",
        "content": "Have you ever observed the wheels of a moving bicycle? Or a coin spinning on a table? A circle is perfectly symmetric. But what happens when a straight line tries to touch a circle without crossing it? That single point of contact is the birthplace of the **Tangent (स्पर्श रेखा / સ્પર્શક)**!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "A line crossing a circle at two points is a Secant. But a line just 'kissing' the edge at one point is a Tangent.",
        "image_url": "assets/images/maths_ch10_secant_tangent.jpg",
        "alt_text": "A circle showing secant cutting through and tangent touching the edge."
    })

    # ==========================================
    # MODULE 2: TANGENT TO A CIRCLE (THEOREM 10.1)
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "**Theorem 10.1 (प्रमेय 10.1):**\nThe tangent at any point of a circle is perpendicular (लम्ब) to the radius through the point of contact.\n\n*Proof Idea:* The shortest distance from the center to the tangent line is the perpendicular distance, and no point on the tangent other than the point of contact can be closer than the radius.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Teacher's Secret:** Whenever you see a tangent and a radius meeting at the edge of the circle, instantly draw a 90° right angle symbol. It unlocks almost every circle problem using Pythagoras theorem!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    # ==========================================
    # MODULE 3: TANGENTS FROM AN EXTERNAL POINT (THEOREM 10.2)
    # ==========================================
    blocks.append({
        "type": "diagram",
        "content": "Imagine standing outside a circular stadium and throwing two laser beams that just graze the stadium walls on either side. Those laser beams are exactly the same length!",
        "image_url": "assets/images/maths_ch10_external_tangents.jpg",
        "alt_text": "Two tangents drawn from an external point to a circle, showing equal lengths."
    })

    blocks.append({
        "type": "theory",
        "content": "**Theorem 10.2 (प्रमेय 10.2):**\nThe lengths of tangents drawn from an external point to a circle are equal.\n\n*Important Proof:* Draw a line from the external point P to center O. Draw radii to the points of contact. You get two right-angled triangles. They are congruent (RHS congruence). Therefore, tangents are equal!",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    # ==========================================
    # MODULE 4: EXAM TRICKS
    # ==========================================
    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC:** The Quadrilateral Trick\n\nIf a quadrilateral circumscribes a circle (touches it from all sides), then the sum of opposite sides are equal:\n**AB + CD = AD + BC**\n\n*Board Trick:* They will give you 3 sides and ask for the 4th. Just use this result directly (which is derived from Theorem 10.2)!",
        "difficulty": "Advanced",
        "bloom": "Apply"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_maths_ch10.json"
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_maths_ch10.json"
    final_json["metadata"]["id"] = "gseb_class10_maths_ch10"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Supreme Maths Chapter 10 Generated Successfully!")

if __name__ == "__main__":
    generate_supreme_maths_ch10()
