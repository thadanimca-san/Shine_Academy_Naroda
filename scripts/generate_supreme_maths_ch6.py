import json
import os

def generate_supreme_maths_ch6():
    chapter_id = "ncert_class10_maths_ch6"
    title = "Chapter 6: Triangles"
    
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
        "tags": ["maths", "triangles", "thales_theorem", "pythagoras_theorem", "similarity", "board_special"],
        "learning_outcomes": [
            "Master the concept of Similarity of Triangles.",
            "Understand and prove Thales Theorem (Basic Proportionality Theorem).",
            "Understand and apply Pythagoras Theorem in complex problems.",
            "Solve CBSE/State Board HOTS questions related to Triangles."
        ],
        "ai_context": {
            "learning_goal": "Make geometry visual and intuitive. Use the 'Socratic Discovery Arc' to build intuition before formal proofs.",
            "common_misconceptions": [
                "Students confuse congruence with similarity.",
                "Students struggle to identify corresponding sides in similar triangles."
            ]
        }
    }
    
    blocks = []
    
    # ==========================================
    # MODULE 1: INTRODUCTION TO SIMILARITY
    # ==========================================
    blocks.append({
        "type": "hook",
        "content": "Have you ever wondered how we can measure the height of a mountain without actually climbing it with a tape measure? The secret lies in shadows and the magical property of **Similar Triangles (समरूप त्रिभुज / સમરૂપ ત્રિકોણ)**!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Congruent vs Similar: Congruent means exact same shape and size (like identical twins). Similar means same shape but different size (like a real car and its toy model).",
        "image_url": "assets/images/maths_ch6_similarity.jpg",
        "alt_text": "A large and a small triangle showing similarity vs congruence."
    })

    # ==========================================
    # MODULE 2: THALES THEOREM (BPT)
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "**Basic Proportionality Theorem (Thales Theorem):**\nIf a line is drawn parallel to one side of a triangle to intersect the other two sides in distinct points, the other two sides are divided in the same ratio. This is a powerful tool in geometry!",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Teacher's Secret:** When writing the proof for Thales Theorem, always start by constructing perpendiculars. The trick is to compare the areas of the triangles formed to get the required ratios!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC:** Thales Theorem HOTS\n\n*Question:* In a trapezium ABCD with AB || DC, the diagonals intersect at O. Prove that AO/BO = CO/DO.\n*Trick:* Draw a line through O parallel to AB and use Thales Theorem in two different triangles to equate the ratios!",
        "difficulty": "Advanced",
        "bloom": "Apply"
    })

    # ==========================================
    # MODULE 3: PYTHAGORAS THEOREM
    # ==========================================
    blocks.append({
        "type": "diagram",
        "content": "The famous Pythagoras Theorem isn't just an equation; it's the relationship between the areas of squares drawn on the sides of a right-angled triangle.",
        "image_url": "assets/images/maths_ch6_pythagoras.jpg",
        "alt_text": "A right angled triangle with squares on all three sides showing area relation."
    })

    blocks.append({
        "type": "theory",
        "content": "**Pythagoras Theorem (पाइथागोरस प्रमेय):**\nIn a right-angled triangle, the square of the hypotenuse is equal to the sum of the squares of the other two sides. Formula: **Hypotenuse² = Base² + Perpendicular²**.",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })
    
    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC:** Pythagoras Theorem HOTS\n\n*Question:* A ladder rests against a wall at a height of 8m. If the ladder is 10m long, find the distance of the foot of the ladder from the wall.\n*Trick:* This forms a right-angled triangle. Hypotenuse is the ladder (10m), perpendicular is the wall (8m). Apply Pythagoras Theorem: 10² = Base² + 8². Base² = 100 - 64 = 36. So, Base = 6m!",
        "difficulty": "Advanced",
        "bloom": "Apply"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_maths_ch6.json"
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_maths_ch6.json"
    final_json["metadata"]["id"] = "gseb_class10_maths_ch6"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Supreme Maths Chapter 6 Generated Successfully!")

if __name__ == "__main__":
    generate_supreme_maths_ch6()
