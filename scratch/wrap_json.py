import json

def wrap_file(path, chapter_id):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # If it's already a dictionary with 'blocks', skip
    if isinstance(data, dict) and 'blocks' in data:
        return
        
    wrapped = {
        "metadata": {
            "id": chapter_id,
            "title": "Chapter 4: Quadratic Equations",
            "subtitle": "The Ultimate Board Exam Mastery Guide",
            "subject": "Maths",
            "grade": "10",
            "board": "NCERT/CBSE",
            "curriculum": ["Universal"],
            "language": "English/Hindi",
            "difficulty": "Advanced",
            "estimated_minutes": 180,
            "version": "3.0.0-SUPREME-MATHS",
            "author": "Antigravity Supreme Intelligence",
            "reviewed_by": "Chief Academic Architect",
            "tags": ["maths", "quadratic_equations", "roots", "board_special"],
            "learning_outcomes": [
              "Identify quadratic equations in various forms.",
              "Solve quadratic equations using factorization and quadratic formula.",
              "Understand the nature of roots using the discriminant.",
              "Apply quadratic equations to solve real-life word problems."
            ],
            "ai_context": {
              "learning_goal": "Make abstract algebraic concepts visual.",
              "common_misconceptions": [
                "Students confuse linear and quadratic equations.",
                "Students struggle with signs when using the quadratic formula."
              ]
            }
        },
        "blocks": data
    }
    
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(wrapped, f, ensure_ascii=False, indent=2)

wrap_file('/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/cbse_class10_maths_ch4.json', 'cbse_class10_maths_ch4')
wrap_file('/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_maths_ch4.json', 'gseb_class10_maths_ch4')
print("Successfully wrapped JSONs with metadata!")
