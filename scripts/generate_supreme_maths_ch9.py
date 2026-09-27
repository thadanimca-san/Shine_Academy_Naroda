import json
import os

def generate_supreme_maths_ch9():
    chapter_id = "ncert_class10_maths_ch9"
    title = "Chapter 9: Some Applications of Trigonometry"
    
    metadata = {
        "id": chapter_id,
        "title": title,
        "subtitle": "Heights and Distances: The Ultimate Guide",
        "subject": "Maths",
        "grade": "10",
        "board": "NCERT/CBSE",
        "curriculum": ["Universal"],
        "language": "English/Hindi/Gujarati (Bilingual)",
        "difficulty": "Advanced",
        "estimated_minutes": 120,
        "version": "3.0.0-SUPREME-MATHS",
        "author": "Antigravity Supreme Intelligence",
        "reviewed_by": "Chief Academic Architect",
        "tags": ["maths", "trigonometry", "heights_distances", "angle_of_elevation", "angle_of_depression"],
        "learning_outcomes": [
            "Understand the concepts of Line of Sight, Angle of Elevation, and Angle of Depression.",
            "Apply trigonometric ratios to solve real-world problems involving heights and distances.",
            "Visualize problems using diagrams to accurately form right-angled triangles."
        ],
        "ai_context": {
            "learning_goal": "Help students visualize heights and distances problems using right-angled triangles.",
            "common_misconceptions": [
                "Students confuse the angle of elevation with the angle of depression.",
                "Students forget to draw a horizontal line when measuring the angle of depression."
            ]
        }
    }
    
    blocks = []
    
    # MODULE 1: INTRODUCTION
    blocks.append({
        "type": "hook",
        "content": "Have you ever wondered how astronomers calculate the distance to the moon, or how engineers build towering skyscrapers? They don't use a giant measuring tape! They use the magic of **Trigonometry**! Let's explore how to measure heights and distances using triangles.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Line of Sight and Angle of Elevation. When you look UP at an object, the angle formed by your line of sight with the horizontal is the Angle of Elevation.",
        "image_url": "assets/images/maths_ch9_elevation.jpg",
        "alt_text": "A person looking up at the top of a tower, showing the horizontal line, line of sight, and angle of elevation."
    })

    # MODULE 2: ANGLES OF ELEVATION AND DEPRESSION
    blocks.append({
        "type": "theory",
        "content": "**Angle of Elevation (उन्नयन कोण):**\nWhen you are looking UP at an object, the angle between the horizontal line and your line of sight is called the Angle of Elevation. It's like your eyes 'elevating' to see something high.\n\n**Angle of Depression (अवनमन कोण):**\nWhen you are looking DOWN at an object, the angle between the horizontal line and your line of sight is called the Angle of Depression. Always remember to draw the horizontal line at eye level!",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Line of Sight and Angle of Depression. When you look DOWN at an object, the angle formed by your line of sight with the horizontal is the Angle of Depression.",
        "image_url": "assets/images/maths_ch9_depression.jpg",
        "alt_text": "A person looking down from a balcony at a car on the road, showing the horizontal line, line of sight, and angle of depression."
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Teacher's Secret:** By Alternate Interior Angles, the Angle of Depression from the top is ALWAYS EQUAL to the Angle of Elevation from the bottom! So you can often convert a depression problem into an elevation problem to make it easier.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC:** The Multi-Triangle Problem\n\nMany 4-mark and 5-mark questions will involve TWO triangles (e.g., observing a tower from two different points). \n*Board Trick:* Find a common side (usually the height or the base) between the two triangles, express it in terms of trigonometric ratios for both triangles, and equate them!",
        "difficulty": "Advanced",
        "bloom": "Apply"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_maths_ch9.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_maths_ch9.json"
    final_json["metadata"]["id"] = "gseb_class10_maths_ch9"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Supreme Maths Chapter 9 Generated Successfully!")

if __name__ == "__main__":
    generate_supreme_maths_ch9()
