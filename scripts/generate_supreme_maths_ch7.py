import json
import os

def generate_supreme_maths_ch7():
    chapter_id = "ncert_class10_maths_ch7"
    title = "Chapter 7: Coordinate Geometry"
    
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
        "tags": ["maths", "coordinate_geometry", "distance_formula", "section_formula", "board_special", "bilingual"],
        "learning_outcomes": [
            "Master the Distance Formula to find the length between two points.",
            "Understand the Section Formula to find coordinates of a point dividing a line segment.",
            "Solve CBSE/State Board HOTS questions related to coordinate geometry.",
            "Apply logic to real-world geometric scenarios."
        ],
        "ai_context": {
            "learning_goal": "Make abstract coordinates feel real. Use the 'Socratic Discovery Arc' to build intuition before giving formulas.",
            "common_misconceptions": [
                "Students get confused with negative signs in the formulas.",
                "Students struggle with the ratio in the section formula."
            ]
        }
    }
    
    blocks = []
    
    # ==========================================
    # MODULE 1: INTRODUCTION
    # ==========================================
    blocks.append({
        "type": "hook",
        "content": "Imagine you are standing at point A and your friend is at point B on a giant grid. How do you find the exact distance between you two? Or what if you want to meet exactly halfway? This is the power of **Coordinate Geometry (निर्देशांक ज्यामिति / યામ ભૂમિતિ)**!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "The Cartesian Plane: The map of mathematical reality where every point has an address (x, y).",
        "image_url": "assets/images/maths_ch7_cartesian_plane.jpg",
        "alt_text": "A glowing Cartesian plane showing the X and Y axes with a point."
    })

    # ==========================================
    # MODULE 2: DISTANCE FORMULA
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "**Distance Formula (दूरी सूत्र):**\nThe distance between two points P(x₁, y₁) and Q(x₂, y₂) is given by:\n**PQ = √[(x₂ - x₁)² + (y₂ - y₁)²]**\n\n*Example:* Distance between (0,0) and (3,4) is √[(3-0)² + (4-0)²] = √(9+16) = √25 = 5 units.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Teacher's Secret:** The Distance Formula is just the Pythagorean Theorem in disguise! Draw a right triangle between the two points, and the distance is simply the hypotenuse.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    # ==========================================
    # MODULE 3: SECTION FORMULA
    # ==========================================
    blocks.append({
        "type": "diagram",
        "content": "The Section Formula: Finding the exact coordinate that divides a journey into specific ratios.",
        "image_url": "assets/images/maths_ch7_section_formula.jpg",
        "alt_text": "A line segment divided into a ratio m1:m2 with coordinates shown."
    })

    blocks.append({
        "type": "theory",
        "content": "**Section Formula (विभाजन सूत्र):**\nThe coordinates of the point P(x, y) which divides the line segment joining the points A(x₁, y₁) and B(x₂, y₂) internally in the ratio m₁ : m₂ are:\n**x = (m₁x₂ + m₂x₁) / (m₁ + m₂)**\n**y = (m₁y₂ + m₂y₁) / (m₁ + m₂)**",
        "difficulty": "Advanced",
        "bloom": "Apply"
    })

    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC:** The Midpoint Formula\n\nIf the ratio is 1:1, P is the midpoint! The formula simplifies to:\n**( (x₁+x₂)/2 , (y₁+y₂)/2 )**\n\n*Board Trick:* Use k:1 ratio when you need to find the ratio itself! It makes calculations much easier.",
        "difficulty": "Advanced",
        "bloom": "Apply"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_maths_ch7.json"
    
    # Ensure directory exists just in case
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_maths_ch7.json"
    final_json["metadata"]["id"] = "gseb_class10_maths_ch7"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Supreme Maths Chapter 7 Generated Successfully!")

if __name__ == "__main__":
    generate_supreme_maths_ch7()
