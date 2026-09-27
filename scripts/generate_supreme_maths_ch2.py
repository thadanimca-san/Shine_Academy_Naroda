import json
import os

def generate_supreme_maths_ch2():
    chapter_id = "ncert_class10_maths_ch2"
    title = "Chapter 2: Polynomials"
    
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
        "tags": ["maths", "polynomials", "zeros", "board_special", "bilingual"],
        "learning_outcomes": [
            "Understand the geometrical meaning of the zeroes of a polynomial.",
            "Find the zeroes of a quadratic polynomial.",
            "Verify the relationship between zeroes and coefficients.",
            "Solve CBSE/State Board HOTS questions related to Polynomials."
        ],
        "ai_context": {
            "learning_goal": "Make algebraic expressions visual. Use the 'Socratic Discovery Arc' to connect algebraic equations with graphs before jumping to formulas.",
            "common_misconceptions": [
                "Students confuse the degree of a polynomial with the number of terms.",
                "Students struggle with the relationship between zeros and coefficients."
            ]
        }
    }
    
    blocks = []
    
    # ==========================================
    # MODULE 1: INTRODUCTION
    # ==========================================
    blocks.append({
        "type": "hook",
        "content": "Imagine you throw a ball in the air. The path it takes forms a beautiful curve called a parabola. Did you know you can predict exactly where the ball will land using just one equation? Welcome to the magic of **Polynomials (बहुपद / બહુપદીઓ)**!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "A Polynomial Rollercoaster: The graph of a quadratic polynomial creates a curve that crosses the x-axis. The points where it crosses are the 'Zeroes'!",
        "image_url": "assets/images/maths_ch2_parabola_curve.jpg",
        "alt_text": "A glowing parabolic curve crossing the x-axis at two points, representing the zeroes of a polynomial."
    })

    # ==========================================
    # MODULE 2: DEGREES AND TYPES
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "**Degree of a Polynomial (बहुपद की घात / બહુપદીની ઘાત):**\nThe highest power of x in p(x) is called the degree of the polynomial.\n\n* Linear Polynomial (रैखिक बहुपद): Degree 1, e.g., 2x - 3\n* Quadratic Polynomial (द्विघात बहुपद): Degree 2, e.g., ax² + bx + c\n* Cubic Polynomial (त्रिघात बहुपद): Degree 3, e.g., ax³ + bx² + cx + d",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Teacher's Secret:** The degree tells you the MAXIMUM number of zeroes a polynomial can have. A quadratic polynomial (degree 2) like ax² + bx + c can have at most 2 zeroes!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    # ==========================================
    # MODULE 3: ZEROES AND COEFFICIENTS
    # ==========================================
    blocks.append({
        "type": "diagram",
        "content": "Visualizing Zeroes: Just look at the x-axis. The number of times the graph intersects the x-axis is exactly the number of zeroes (शून्यक / શૂન્યો) the polynomial has.",
        "image_url": "assets/images/maths_ch2_graph_intersections.jpg",
        "alt_text": "Different graphs intersecting the x-axis, illustrating 1, 2, and 3 zeroes."
    })

    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC:** Relationship between Zeroes and Coefficients\n\nFor a quadratic polynomial ax² + bx + c, if α and β are the zeroes:\n**Sum of zeroes (α + β) = -b/a**\n**Product of zeroes (α × β) = c/a**\n\n*Board Trick:* Often, questions will give you the sum and product and ask for the polynomial. Just use: x² - (α + β)x + αβ!",
        "difficulty": "Advanced",
        "bloom": "Apply"
    })

    # ==========================================
    # MODULE 4: GEOMETRICAL MEANING
    # ==========================================
    blocks.append({
        "type": "memory_trick",
        "content": "**The Zero Rule:**\nFinding a zero means setting p(x) = 0. Geometrically, this is where the height (y-value) is zero—which is exactly on the x-axis! So, if the graph doesn't touch the x-axis, there are no real zeroes.",
        "difficulty": "Intermediate",
        "bloom": "Apply"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    # Ensure directory exists
    os.makedirs("/home/ubuntu/Shine_Academy_Naroda/app_core/chapters", exist_ok=True)
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_maths_ch2.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(final_json, f, indent=2, ensure_ascii=False)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_maths_ch2.json"
    final_json["metadata"]["id"] = "gseb_class10_maths_ch2"
    with open(gseb_path, "w", encoding="utf-8") as f:
        json.dump(final_json, f, indent=2, ensure_ascii=False)
        
    print("Supreme Maths Chapter 2 Generated Successfully!")

if __name__ == "__main__":
    generate_supreme_maths_ch2()
