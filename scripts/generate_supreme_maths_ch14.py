import json
import os

def generate_supreme_maths_ch14():
    chapter_id = "ncert_class10_maths_ch14"
    title = "Chapter 14: Statistics"
    
    metadata = {
        "id": chapter_id,
        "title": title,
        "subtitle": "Master Data Analysis and Central Tendency",
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
        "tags": ["maths", "statistics", "mean", "median", "mode", "bilingual"],
        "learning_outcomes": [
            "Calculate Mean of grouped data using various methods.",
            "Find the Mode of grouped data.",
            "Determine the Median of grouped data.",
            "Understand the empirical relationship between mean, median, and mode."
        ],
        "ai_context": {
            "learning_goal": "Help students visualize data and understand the real-world applications of central tendency. Use the 'Socratic Discovery Arc'.",
            "common_misconceptions": [
                "Students confuse the formulas for Mean, Median, and Mode.",
                "Difficulty in finding cumulative frequencies."
            ]
        }
    }
    
    blocks = []
    
    # ==========================================
    # MODULE 1: INTRODUCTION
    # ==========================================
    blocks.append({
        "type": "hook",
        "content": "Imagine you are the manager of a cricket team. You need to pick the best batsman based on their past 10 matches. Should you look at their average score? Or the score they hit most frequently? Or the middle value of their scores? Welcome to the fascinating world of **Statistics (सांख्यिकी / આંકડાશાસ્ત્ર)**!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "The Three Pillars of Central Tendency: Mean, Median, and Mode. They help us find the 'center' of the data in different ways.",
        "image_url": "assets/images/maths_ch14_central_tendency.jpg",
        "alt_text": "Illustration showing Mean, Median, and Mode."
    })

    # ==========================================
    # MODULE 2: MEAN OF GROUPED DATA
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "**Mean (माध्य / મધ્યક):**\nThe average of the data.\nFor grouped data (Direct Method):\nx̄ = Σ(fᵢxᵢ) / Σfᵢ\n\nWhere 'x̄' is the mean, 'fᵢ' is the frequency, and 'xᵢ' is the class mark.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    # ==========================================
    # MODULE 3: MODE OF GROUPED DATA
    # ==========================================
    blocks.append({
        "type": "diagram",
        "content": "Finding the Mode means finding the peak of the data, the most frequent observation.",
        "image_url": "assets/images/maths_ch14_mode_peak.jpg",
        "alt_text": "Graph showing the peak frequency representing the mode."
    })

    blocks.append({
        "type": "theory",
        "content": "**Mode (बहुलक / બહુલક):**\nThe value that occurs most frequently.\nFormula for grouped data:\nMode = l + [ (f₁ - f₀) / (2f₁ - f₀ - f₂) ] × h\n\nWhere 'l' is the lower limit of the modal class, 'h' is the class size, 'f₁' is the frequency of the modal class, 'f₀' is the frequency of the preceding class, and 'f₂' is the frequency of the succeeding class.",
        "difficulty": "Advanced",
        "bloom": "Apply"
    })

    # ==========================================
    # MODULE 4: MEDIAN OF GROUPED DATA
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "**Median (माध्यक / મધ્યસ્થ):**\nThe middle value of the sorted data.\nFormula for grouped data:\nMedian = l + [ (n/2 - cf) / f ] × h\n\nWhere 'l' is the lower limit of median class, 'n' is number of observations, 'cf' is cumulative frequency of class preceding the median class, 'f' is frequency of median class, and 'h' is class size.",
        "difficulty": "Advanced",
        "bloom": "Apply"
    })

    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC:** Empirical Relationship\n\n**3 Median = Mode + 2 Mean**\n\n*Board Trick:* You might be given any two values and asked to find the third. Memorize this relation!",
        "difficulty": "Intermediate",
        "bloom": "Apply"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_maths_ch14.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_maths_ch14.json"
    final_json["metadata"]["id"] = "gseb_class10_maths_ch14"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Supreme Maths Chapter 14 Generated Successfully!")

if __name__ == "__main__":
    generate_supreme_maths_ch14()
