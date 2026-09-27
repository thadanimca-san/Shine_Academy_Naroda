import json
import os

def generate_supreme_maths_ch13():
    chapter_id = "ncert_class10_maths_ch13"
    title = "Chapter 13: Surface Areas and Volumes"
    
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
        "tags": ["maths", "surface_areas", "volumes", "cylinder", "cone", "sphere", "board_special", "bilingual"],
        "learning_outcomes": [
            "Master the formulas for Surface Areas and Volumes of combinations of solids.",
            "Understand the concepts of Cylinder, Cone, and Sphere.",
            "Solve CBSE/State Board HOTS questions related to converting one solid into another.",
            "Apply logic to real-world scenarios."
        ],
        "ai_context": {
            "learning_goal": "Help students visualize 3D shapes. Use the 'Socratic Discovery Arc' to build intuition before giving formulas.",
            "common_misconceptions": [
                "Students get confused between Total Surface Area (TSA) and Curved Surface Area (CSA).",
                "Students make calculation errors when dealing with Pi (π) and radius."
            ]
        }
    }
    
    blocks = []
    
    # ==========================================
    # MODULE 1: INTRODUCTION
    # ==========================================
    blocks.append({
        "type": "hook",
        "content": "Imagine you have an ice cream cone with a scoop of ice cream on top! What if you want to know how much ice cream is there, or how much wafer is used to make the cone? This is where the magic of **Surface Areas and Volumes (पृष्ठीय क्षेत्रफल और आयतन / પૃષ્ઠફળ અને ઘનફળ)** comes in!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Visualize combinations of solids: A tent (cone on a cylinder), an ice cream cone (hemisphere on a cone).",
        "image_url": "assets/images/maths_ch13_solid_combos.jpg",
        "alt_text": "3D diagram showing combinations of various shapes like cylinders, cones, and hemispheres."
    })

    # ==========================================
    # MODULE 2: FORMULAS - CYLINDER, CONE, SPHERE
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "**Cylinder (बेलन / નળાકાર):**\n• Curved Surface Area (CSA) = 2πrh\n• Total Surface Area (TSA) = 2πr(r + h)\n• Volume = πr²h\n\n**Cone (शंकु / શંકુ):**\n• Slant Height (l) = √(r² + h²)\n• Curved Surface Area (CSA) = πrl\n• Total Surface Area (TSA) = πr(l + r)\n• Volume = (1/3)πr²h\n\n**Sphere (गोला / ગોલક):**\n• Surface Area = 4πr²\n• Volume = (4/3)πr³\n\n**Hemisphere (अर्धगोला / અર્ધગોલક):**\n• Curved Surface Area (CSA) = 2πr²\n• Total Surface Area (TSA) = 3πr²\n• Volume = (2/3)πr³",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Teacher's Secret:** When dealing with combinations of solids, remember that the Total Surface Area of the new solid is NOT the sum of the TSAs of the individual solids. You only add the visible areas (usually the CSAs)!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Conversion of Solids: Melting a big sphere to make smaller cones. The VOLUME remains the same!",
        "image_url": "assets/images/maths_ch13_melting.jpg",
        "alt_text": "Illustration showing a large melting sphere being poured into smaller cone moulds."
    })

    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC:** Conversion of solid from one shape to another.\n\n*Board Trick:* The fundamental rule is: **Volume of old solid = Volume of new solid**. Equate their formulas and solve for the unknown dimension (radius, height, or number of items).",
        "difficulty": "Advanced",
        "bloom": "Apply"
    })


    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_maths_ch13.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_maths_ch13.json"
    final_json["metadata"]["id"] = "gseb_class10_maths_ch13"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Supreme Maths Chapter 13 Generated Successfully!")

if __name__ == "__main__":
    generate_supreme_maths_ch13()
