import json
import os

def generate_supreme_maths_ch5():
    chapter_id = "ncert_class10_maths_ch5"
    title = "Chapter 5: Arithmetic Progressions"
    
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
        "tags": ["maths", "arithmetic_progressions", "nth_term", "sum_of_n_terms", "board_special", "bilingual"],
        "learning_outcomes": [
            "Understand the concept of an Arithmetic Progression (AP).",
            "Calculate the nth term (aₙ) of an AP.",
            "Calculate the sum of first n terms (Sₙ) of an AP.",
            "Solve CBSE/State Board HOTS questions related to APs."
        ],
        "ai_context": {
            "learning_goal": "Make sequences feel intuitive. Use real-life examples like savings and stadium seating before jumping into formulas.",
            "common_misconceptions": [
                "Students confuse the number of terms 'n' with the nth term 'aₙ'.",
                "Students forget the common difference 'd' can be negative."
            ]
        }
    }
    
    blocks = []
    
    # ==========================================
    # MODULE 1: INTRODUCTION
    # ==========================================
    blocks.append({
        "type": "hook",
        "content": "Imagine you get Rs. 100 on your first birthday, Rs. 150 on your second, Rs. 200 on your third, and so on. Every year, the amount increases by a fixed Rs. 50. What will you get on your 18th birthday? This magic of predictable patterns is called an **Arithmetic Progression (समांतर श्रेढ़ी / સમાંતર શ્રેણી)**!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "A staircase where every step is of equal height represents an AP perfectly.",
        "image_url": "assets/images/maths_ch5_staircase.jpg",
        "alt_text": "A staircase with each step marked with numbers showing a constant difference."
    })

    # ==========================================
    # MODULE 2: NTH TERM OF AN AP
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "**Nth Term Formula (nवाँ पद):**\nIf 'a' is the first term and 'd' is the common difference, the nth term aₙ is given by:\n\n**aₙ = a + (n - 1)d**\n\n*Example:* If a = 2, d = 3, then a₅ = 2 + (5 - 1)3 = 14.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Teacher's Secret:** Don't confuse **'n'** (the position of the term, like the 5th chair) with **'aₙ'** (the value of the term, like who is sitting in the 5th chair)!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    # ==========================================
    # MODULE 3: SUM OF FIRST N TERMS
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "**Sum of First n Terms (प्रथम n पदों का योग):**\nThe sum Sₙ of the first n terms of an AP is:\n\n**Sₙ = n/2 × [2a + (n - 1)d]**\n\nAlternatively, if you know the first term 'a' and the last term 'l', **Sₙ = n/2 × (a + l)**.",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    blocks.append({
        "type": "diagram",
        "content": "Visualizing the sum of an AP by matching the first and last terms, just like young Gauss did to add 1 to 100 instantly!",
        "image_url": "assets/images/maths_ch5_gauss_sum.jpg",
        "alt_text": "A diagram showing how pairing numbers from the beginning and end of a sequence gives a constant sum."
    })

    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC:** Word problems on Sₙ\n\n*Board Trick:* When 3 terms are in AP, assume them as **a - d, a, a + d**. This makes addition much simpler because the 'd's cancel out!",
        "difficulty": "Advanced",
        "bloom": "Apply"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_maths_ch5.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_maths_ch5.json"
    final_json["metadata"]["id"] = "gseb_class10_maths_ch5"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Supreme Maths Chapter 5 Generated Successfully!")

if __name__ == "__main__":
    generate_supreme_maths_ch5()
