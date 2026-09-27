import json
import os
import random

def save_json(data, filepath):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def generate_mcq_paper(subject, chapter_id, title):
    # Generates a 50-mark MCQ paper (Part A)
    blocks = []
    for i in range(1, 51):
        blocks.append({
            "id": f"KOBJ_{chapter_id}_Q{i}",
            "type": "quiz",
            "section": "Part A: Multiple Choice Questions",
            "marks": 1,
            "question": f"Sample Board MCQ Question {i} for {subject}",
            "options": [
                "Option A (Correct concept)",
                "Option B (Common misconception)",
                "Option C (Irrelevant)",
                "Option D (Calculation error)"
            ],
            "correct_index": 0,
            "explanation": f"Detailed Board Explanation for Q{i}: Option A is correct because of the fundamental principles of {subject}. Examiner Tip: Students often confuse this with Option B due to sign errors."
        })
        
    data = {
        "metadata": {
            "id": chapter_id,
            "title": title,
            "subject": subject,
            "difficulty": "Board Level",
            "estimated_minutes": 60,
            "is_exam_paper": True,
            "paper_type": "mcq",
            "total_marks": 50
        },
        "blocks": blocks
    }
    filepath = f"app_core/chapters/{chapter_id}.json"
    save_json(data, filepath)
    print(f"Generated {filepath}")

def generate_subjective_paper(subject, chapter_id, title):
    # Generates a 50-mark Subjective paper (Part B)
    # Section A: 2 marks x 9 questions = 18 marks (Out of 12 questions) -> Let's just generate 9 for simplicity
    # Section B: 3 marks x 6 questions = 18 marks (Out of 9 questions)
    # Section C: 4 marks x 5 questions = 20 marks ... wait, 18+18+20 = 56. 
    # Let's do standard GSEB: Section A (10x2=20), Section B (6x3=18), Section C (3x4=12). Total = 50.
    
    sections = [
        {"name": "Section A: Short Answer Type", "count": 10, "marks": 2},
        {"name": "Section B: Medium Answer Type", "count": 6, "marks": 3},
        {"name": "Section C: Long Answer Type", "count": 3, "marks": 4}
    ]
    
    blocks = []
    q_num = 1
    for sec in sections:
        for i in range(sec["count"]):
            blocks.append({
                "id": f"KOBJ_{chapter_id}_Q{q_num}",
                "type": "theory",
                "section": sec["name"],
                "marks": sec["marks"],
                "question": f"Board Subjective Question {q_num} ({sec['marks']} Marks) for {subject}",
                "model_answer": f"Step 1: Write given data.\nStep 2: Apply formula for {subject}.\nStep 3: Final Answer with units.",
                "teacher_tip": f"EXAMINER MARKING SCHEME:\n- 1 Mark for formula.\n- {sec['marks']-1} Marks for correct steps and final answer.\nCommon Mistake: Forgetting to write the SI Unit."
            })
            q_num += 1
            
    data = {
        "metadata": {
            "id": chapter_id,
            "title": title,
            "subject": subject,
            "difficulty": "Board Level",
            "estimated_minutes": 120,
            "is_exam_paper": True,
            "paper_type": "subjective",
            "total_marks": 50
        },
        "blocks": blocks
    }
    filepath = f"app_core/chapters/{chapter_id}.json"
    save_json(data, filepath)
    print(f"Generated {filepath}")

def generate_deo_bank():
    papers = [
        {"id": "gseb_class10_deo_bank_2026_ch1", "subj": "Science", "title": "Science DEO Bank (Part 1 - MCQs)", "type": "mcq"},
        {"id": "gseb_class10_deo_bank_2026_ch2", "subj": "Science", "title": "Science DEO Bank (Part 2 - Subject)", "type": "subjective"},
        {"id": "gseb_class10_deo_bank_2026_ch3", "subj": "Maths Basic", "title": "Maths Basic DEO Bank (Part 1 - MCQs)", "type": "mcq"},
        {"id": "gseb_class10_deo_bank_2026_ch4", "subj": "Maths Basic", "title": "Maths Basic DEO Bank (Part 2 - Subject)", "type": "subjective"},
        {"id": "gseb_class10_deo_bank_2026_ch5", "subj": "Maths Standard", "title": "Maths Standard DEO Bank (Part 1 - MCQs)", "type": "mcq"},
        {"id": "gseb_class10_deo_bank_2026_ch6", "subj": "Maths Standard", "title": "Maths Standard DEO Bank (Part 2 - Subject)", "type": "subjective"},
        {"id": "gseb_class10_deo_bank_2026_ch7", "subj": "Social Science", "title": "Social Science DEO Bank (Part 1 - MCQs)", "type": "mcq"},
        {"id": "gseb_class10_deo_bank_2026_ch8", "subj": "Social Science", "title": "Social Science DEO Bank (Part 2 - Subject)", "type": "subjective"},
        {"id": "gseb_class10_deo_bank_2026_ch9", "subj": "English (FL)", "title": "English (FL) DEO Bank (Part 1 - MCQs)", "type": "mcq"},
        {"id": "gseb_class10_deo_bank_2026_ch10", "subj": "English (FL)", "title": "English (FL) DEO Bank (Part 2 - Subject)", "type": "subjective"},
        {"id": "gseb_class10_deo_bank_2026_ch11", "subj": "Gujarati (SL)", "title": "Gujarati (SL) DEO Bank (Part 1 - MCQs)", "type": "mcq"},
        {"id": "gseb_class10_deo_bank_2026_ch12", "subj": "Gujarati (SL)", "title": "Gujarati (SL) DEO Bank (Part 2 - Subject)", "type": "subjective"}
    ]
    
    os.makedirs("app_core/chapters", exist_ok=True)
    
    for p in papers:
        if p["type"] == "mcq":
            generate_mcq_paper(p["subj"], p["id"], p["title"])
        else:
            generate_subjective_paper(p["subj"], p["id"], p["title"])

if __name__ == "__main__":
    generate_deo_bank()
    print("DEO Bank papers generated successfully.")
