import json
import os

def generate_supreme_maths_ch1():
    chapter_id = "ncert_class10_maths_ch1"
    title = "Chapter 1: Real Numbers"
    
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
        "tags": ["maths", "real_numbers", "euclids_lemma", "board_special", "bilingual"],
        "learning_outcomes": [
            "Master the Fundamental Theorem of Arithmetic.",
            "Understand why √2 and √3 are irrational.",
            "Solve CBSE/State Board HOTS questions related to HCF and LCM.",
            "Apply logic to real-world scenarios."
        ],
        "ai_context": {
            "learning_goal": "Make abstract numbers feel real. Use the 'Socratic Discovery Arc' to build intuition before giving formulas.",
            "common_misconceptions": [
                "Students think rational numbers are only fractions.",
                "Students get confused between HCF and LCM word problems."
            ]
        }
    }
    
    blocks = []
    
    # ==========================================
    # MODULE 1: INTRODUCTION
    # ==========================================
    blocks.append({
        "type": "hook",
        "content": "Imagine you have 120 red apples and 180 green apples. You want to pack them in boxes such that each box has the same number of apples, and no apples are mixed. What is the maximum number of apples you can put in one box? This isn't just a puzzle; it's the magic of **Real Numbers (वास्तविक संख्याएँ / વાસ્તવિક સંખ્યાઓ)**!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "The Number Tree: Every number you know (except imaginary numbers) belongs to the family of Real Numbers.",
        "image_url": "assets/images/maths_ch1_number_tree.jpg",
        "alt_text": "A glowing tree showing Rational and Irrational numbers branching out."
    })

    # ==========================================
    # MODULE 2: FUNDAMENTAL THEOREM OF ARITHMETIC
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "**Fundamental Theorem of Arithmetic (अंकगणित की आधारभूत प्रमेय):**\nEvery composite number (भाज्य संख्या) can be expressed (factorised) as a product of primes (अभाज्य संख्या), and this factorisation is unique, apart from the order in which the prime factors occur.\n\n*Example:* 12 = 2² × 3 (Notice the superscript 2² meaning 2 squared!)",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Teacher's Secret:** When finding **HCF** (Highest Common Factor / महत्तम समापवर्तक), take the **smallest** power of each common prime factor. When finding **LCM** (Least Common Multiple / लघुत्तम समापवर्त्य), take the **greatest** power of each prime factor.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC:** The Relationship Formula\n\nFor any two positive integers a and b:\n**HCF(a, b) × LCM(a, b) = a × b**\n\n*Board Trick:* They will give you 3 values and ask you to find the 4th. Don't waste time finding prime factors, just use this formula!",
        "difficulty": "Advanced",
        "bloom": "Apply"
    })

    # ==========================================
    # MODULE 3: IRRATIONAL NUMBERS
    # ==========================================
    blocks.append({
        "type": "diagram",
        "content": "Proving √2 is irrational uses 'Proof by Contradiction' (विरोधाभास द्वारा प्रमाण). It's like proving a man is a thief by first assuming he is a saint, and then finding stolen goods in his pocket!",
        "image_url": "assets/images/maths_ch1_contradiction.jpg",
        "alt_text": "Detective looking at a mathematical proof."
    })

    blocks.append({
        "type": "theory",
        "content": "**Irrational Numbers (अपरिमेय संख्याएँ / અસંમેય સંખ્યાઓ):**\nA number is irrational if it cannot be written in the form p/q. \nExamples: **√2, √3, π (Pi)**.\n\n*Important Proof:* Let us assume √2 is a rational number. Then √2 = a/b (where a and b are co-prime). Squaring both sides, we get 2 = a²/b², so 2b² = a². This means a² is divisible by 2, which means 'a' is also divisible by 2. This leads to a contradiction!",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    # ==========================================
    # MODULE 4: TERMINATING & NON-TERMINATING
    # ==========================================
    blocks.append({
        "type": "memory_trick",
        "content": "**The 2 and 5 Rule:**\nLook at the denominator (हर) of a fraction. If its prime factors are ONLY 2s or 5s (in the form **2ⁿ × 5ᵐ**), then the decimal expansion will **Terminate** (शांत / શાંત). If there is any other number (like 3 or 7), it will be **Non-terminating repeating** (अशांत आवर्ती / અનંત આવર્ત)!",
        "difficulty": "Intermediate",
        "bloom": "Apply"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_maths_ch1.json"
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_maths_ch1.json"
    final_json["metadata"]["id"] = "gseb_class10_maths_ch1"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Supreme Maths Chapter 1 Generated Successfully!")

if __name__ == "__main__":
    generate_supreme_maths_ch1()
