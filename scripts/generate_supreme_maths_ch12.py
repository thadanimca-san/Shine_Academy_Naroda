import json
import os

def generate_supreme_maths_ch12():
    chapter_id = "ncert_class10_maths_ch12"
    title = "Chapter 12: Areas Related to Circles"
    
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
        "tags": ["maths", "areas", "circles", "sectors", "segments", "board_special", "bilingual"],
        "learning_outcomes": [
            "Calculate the perimeter and area of a circle.",
            "Understand and calculate the area of sectors and segments of a circle.",
            "Solve CBSE/State Board HOTS questions related to combinations of plane figures.",
            "Apply formulas to real-world scenarios like finding areas of designs."
        ],
        "ai_context": {
            "learning_goal": "Make abstract geometric areas easy to visualize. Use the 'Socratic Discovery Arc' to build intuition before giving formulas.",
            "common_misconceptions": [
                "Students confuse sectors with segments.",
                "Students make mistakes when calculating the area of a major segment."
            ]
        }
    }
    
    blocks = []
    
    # ==========================================
    # MODULE 1: INTRODUCTION
    # ==========================================
    blocks.append({
        "type": "hook",
        "content": "Imagine you have a large circular pizza and you want to share it equally among your 4 friends. The piece you get is called a sector. But what if you cut the pizza along a straight line not passing through the center? You get a segment! Welcome to the fascinating world of **Areas Related to Circles (वृत्तों से संबंधित क्षेत्रफल / વર્તુળ સંબંધિત ક્ષેત્રફળ)**!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Visualizing Sectors and Segments: A sector is like a slice of pizza, bounded by two radii and an arc. A segment is bounded by a chord and an arc.",
        "image_url": "assets/images/maths_ch12_sector_segment.jpg",
        "alt_text": "A pizza showing a slice (sector) and a straight cut (segment)."
    })

    # ==========================================
    # MODULE 2: PERIMETER AND AREA OF A CIRCLE
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "**Perimeter and Area of a Circle:**\nThe distance covered by travelling once around a circle is its perimeter, usually called its circumference.\n\n*Formulas:*\nCircumference = 2πr or πd (where d is diameter)\nArea = πr²",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Teacher's Secret:** The value of π is approximately 22/7 or 3.14. Always check if the radius is a multiple of 7 before choosing which value to use. If r is a multiple of 7, 22/7 makes calculations much easier!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    # ==========================================
    # MODULE 3: AREAS OF SECTOR AND SEGMENT
    # ==========================================
    blocks.append({
        "type": "diagram",
        "content": "Understanding the angle of a sector. If the total angle is 360°, a sector with angle θ takes up a fraction (θ/360°) of the entire circle's area.",
        "image_url": "assets/images/maths_ch12_angle_sector.jpg",
        "alt_text": "A circle showing an angle theta for a sector."
    })

    blocks.append({
        "type": "theory",
        "content": "**Area of Sector (त्रिज्यखंड का क्षेत्रफल / વૃત્તાંશનું ક્ષેત્રફળ):**\nLet θ be the angle of the sector in degrees.\nArea of sector = (θ/360°) × πr²\nLength of an arc of a sector = (θ/360°) × 2πr",
        "difficulty": "Advanced",
        "bloom": "Apply"
    })

    # ==========================================
    # MODULE 4: EXAM TRICKS
    # ==========================================
    blocks.append({
        "type": "memory_trick",
        "content": "**Area of Segment (वृत्तखंड का क्षेत्रफल / વૃત્તખંડનું ક્ષેત્રફળ):**\nArea of minor segment = Area of corresponding sector - Area of the corresponding triangle.\nArea of major segment = Area of circle - Area of minor segment.\n\n*Pro Tip:* To find the area of the triangle formed by radii and a chord, use the formula ½ r² sin(θ) if you know trigonometry, or split it into two right-angled triangles!",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_maths_ch12.json"
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_maths_ch12.json"
    final_json["metadata"]["id"] = "gseb_class10_maths_ch12"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Supreme Maths Chapter 12 Generated Successfully!")

if __name__ == "__main__":
    generate_supreme_maths_ch12()
