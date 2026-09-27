import json
import os

def generate_supreme_chapter_9():
    chapter_id = "ncert_class10_science_ch9"
    title = "Chapter 9: Light - Reflection and Refraction"
    
    metadata = {
        "id": chapter_id,
        "title": title,
        "subtitle": "The Ultimate Board Exam Mastery Guide",
        "subject": "Science",
        "grade": "10",
        "board": "NCERT/CBSE",
        "curriculum": ["Universal"],
        "language": "English/Hindi/Gujarati (Bilingual)",
        "difficulty": "Advanced",
        "estimated_minutes": 180,
        "version": "3.0.0-SUPREME-VISUAL",
        "author": "Antigravity Supreme Intelligence",
        "reviewed_by": "Chief Academic Architect",
        "tags": ["physics", "light", "reflection", "refraction", "lenses", "mirrors", "board_special", "bilingual"],
        "learning_outcomes": [
            "Understand the laws of reflection and refraction.",
            "Draw ray diagrams for spherical mirrors and lenses.",
            "Apply the mirror formula and lens formula to solve numericals.",
            "Understand the concept of refractive index and power of a lens."
        ],
        "ai_context": {
            "learning_goal": "Transform the student from a beginner to a board-exam topper in Light - Reflection and Refraction. Use the 'Socratic Discovery Arc'.",
            "common_misconceptions": [
                "Students confuse between convex and concave mirrors/lenses.",
                "Students struggle with sign conventions in mirror and lens formulas."
            ]
        }
    }
    
    blocks = []
    
    # ==========================================
    # MODULE 1: INTRODUCTION TO LIGHT
    # ==========================================
    blocks.append({
        "type": "hook",
        "content": "Why can we see things only when there is light (प्रकाश / પ્રકાશ)? When you look in a mirror, how does your image form? Today, we will uncover the mysteries of Light - how it bounces and bends!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Light bouncing off a smooth surface is called Reflection.",
        "image_url": "assets/images/ch9_reflection.jpg",
        "alt_text": "Reflection of light from a plane mirror"
    })

    blocks.append({
        "type": "theory",
        "content": "**Reflection of Light (प्रकाश का परावर्तन / પ્રકાશનું પરાવર્તન):**\nWhen light falls on a highly polished surface like a mirror, most of the light is sent back into the same medium.\n\n**Laws of Reflection:**\n1. The angle of incidence is equal to the angle of reflection (**∠i = ∠r**).\n2. The incident ray, the normal to the mirror at the point of incidence, and the reflected ray, all lie in the same plane.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "memory_trick",
        "content": "**Convex vs Concave (उत्तल और अवतल / બહિર્ગોળ અને અંતર્ગોળ):**\n- **Concave:** Think of a 'Cave' (गुफा). It caves inwards.\n- **Convex:** Bulges outwards.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    # ==========================================
    # MODULE 2: REFRACTION OF LIGHT
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "**Refraction of Light (प्रकाश का अपवर्तन / પ્રકાશનું વક્રીભવન):**\nWhen light travels from one transparent medium to another, it changes its direction (bends) at the boundary. This happens due to a change in the speed of light.\n\n*Example:* A pencil dipped in water appears bent at the surface.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "diagram",
        "content": "Refraction of light through a rectangular glass slab. Note how the emergent ray is parallel to the incident ray but shifted laterally.",
        "image_url": "assets/images/ch9_refraction_glass.jpg",
        "alt_text": "Refraction through a glass slab"
    })

    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC: Refractive Index (अपवर्तनांक / વક્રીભવનાંક)**\nIt is the ratio of the speed of light in vacuum (c) to the speed of light in the medium (v). **n = c/v**\n\n**Board Question:** Why does light bend towards the normal when passing from air to glass?\n**Answer:** Because glass is optically denser than air, so the speed of light decreases.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    # ==========================================
    # MODULE 3: LENSES & FORMULAS
    # ==========================================
    blocks.append({
        "type": "diagram",
        "content": "Convex lenses converge light rays, while Concave lenses diverge them.",
        "image_url": "assets/images/ch9_lenses.jpg",
        "alt_text": "Convex and Concave lenses focusing light rays"
    })

    blocks.append({
        "type": "theory",
        "content": "**Mirror Formula:** **1/v + 1/u = 1/f**\n**Lens Formula:** **1/v - 1/u = 1/f**\n\nWhere:\n- **u:** Object distance\n- **v:** Image distance\n- **f:** Focal length",
        "difficulty": "Intermediate",
        "bloom": "Apply"
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "Always use the New Cartesian Sign Convention carefully! By convention, the object is always placed to the left of the mirror/lens, meaning **u is always negative**.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_science_ch9.json"
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_science_ch9.json"
    final_json["metadata"]["id"] = "gseb_class10_science_ch9"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Supreme Chapter 9 Generated Successfully!")

if __name__ == "__main__":
    generate_supreme_chapter_9()
