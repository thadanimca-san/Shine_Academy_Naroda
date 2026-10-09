import re
import json
import os

def parse_science_mcqs():
    with open('/home/ubuntu/Shine_Academy_Naroda/raw_data/class10/science/SCIENCE.txt', 'r', encoding='utf-8') as f:
        text = f.read()

    # Split into Questions part and Answers part
    # Look for "Section - A" then find the first answer block
    parts = text.split('ANSWERS')
    if len(parts) < 2:
        print("Answers section not found.")
        return
        
    questions_text = parts[0]
    answers_text = parts[1]

    mcqs = []
    
    # Simple regex to find questions starting with "XX. "
    q_pattern = re.compile(r'^(\d{2,3})\.\s+(.*?)(?=\n[A-D]\.|\n\d{2,3}\.|\Z)', re.DOTALL | re.MULTILINE)
    
    # Dictionary to store questions
    question_dict = {}
    
    for match in q_pattern.finditer(questions_text):
        q_num = match.group(1).lstrip('0')
        q_text = match.group(2).strip().replace('\n', ' ')
        
        # Now try to find options for this question
        # Options usually follow the question text
        opt_start = match.end()
        # Find next question start or end of string
        next_q_match = q_pattern.search(questions_text, opt_start)
        opt_end = next_q_match.start() if next_q_match else len(questions_text)
        
        options_chunk = questions_text[opt_start:opt_end]
        
        # Extract options A, B, C, D
        opts = {}
        for opt_label in ['A', 'B', 'C', 'D']:
            opt_match = re.search(fr'{opt_label}\.\s+(.*?)(?=[A-D]\.|\Z)', options_chunk, re.DOTALL)
            if opt_match:
                opts[opt_label] = opt_match.group(1).strip().replace('\n', ' ')
                
        if len(opts) >= 2: # At least 2 options, likely an MCQ
            question_dict[q_num] = {
                "question": q_text,
                "options_raw": opts
            }

    # Now parse answers
    a_pattern = re.compile(r'^(\d{2,3})\.\s+\(([A-D])\)\s*(.*?)(?=\n\d{2,3}\.|\Z)', re.DOTALL | re.MULTILINE)
    for match in a_pattern.finditer(answers_text):
        q_num = match.group(1).lstrip('0')
        correct_opt = match.group(2)
        explanation = match.group(3).strip().replace('\n', ' ')
        
        if q_num in question_dict:
            q_data = question_dict[q_num]
            options_list = []
            correct_ans_text = ""
            for lbl in ['A', 'B', 'C', 'D']:
                if lbl in q_data['options_raw']:
                    opt_text = q_data['options_raw'][lbl]
                    options_list.append(opt_text)
                    if lbl == correct_opt:
                        correct_ans_text = opt_text
            
            if correct_ans_text:
                mcqs.append({
                    "type": "knowledge_check",
                    "content": {
                        "question": q_data["question"],
                        "options": options_list,
                        "correct_answer": correct_ans_text,
                        "explanation": explanation if explanation else "Correct Answer: " + correct_ans_text
                    }
                })

    print(f"Parsed {len(mcqs)} MCQs.")
    
    if len(mcqs) > 0:
        blocks = [{"type": "hook", "content": "Welcome to the official question Ahmedabad Question Bank 2026 for Science! Let's conquer the Board Exams by practicing these highly expected MCQs."}]
        blocks.extend(mcqs[:100]) # Take top 100 for part 1
        
        chapter_json = {
            "metadata": {
                "id": "ncert_class10_deo_bank_2026_ch1",
                "title": "Science question Bank 2026 (Part 1 - MCQs)",
                "subject": "question Question Bank 2026",
                "grade": "10",
                "curriculum": ["GSEB", "NCERT", "CBSE"],
                "difficulty": "Advanced",
                "version": "4.0.0-question-BANK"
            },
            "blocks": blocks
        }
        
        output_dir = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters'
        
        with open(os.path.join(output_dir, 'ncert_class10_deo_bank_2026_ch1.json'), 'w') as f:
            json.dump(chapter_json, f, indent=2)
            
        with open(os.path.join(output_dir, 'gseb_class10_question_bank_2026_ch1.json'), 'w') as f:
            json_data_gseb = dict(chapter_json)
            json_data_gseb["metadata"]["id"] = "gseb_class10_question_bank_2026_ch1"
            json.dump(json_data_gseb, f, indent=2)
            
        with open(os.path.join(output_dir, 'cbse_class10_deo_bank_2026_ch1.json'), 'w') as f:
            json_data_cbse = dict(chapter_json)
            json_data_cbse["metadata"]["id"] = "cbse_class10_deo_bank_2026_ch1"
            json.dump(json_data_cbse, f, indent=2)
            
        print("Generated JSON for Ch1.")

if __name__ == "__main__":
    parse_science_mcqs()
