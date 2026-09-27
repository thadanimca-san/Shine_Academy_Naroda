import re
import json
import os

def parse_deo_file(txt_file, subject_prefix, subject_title, start_ch_id):
    if not os.path.exists(txt_file):
        print(f"File not found: {txt_file}")
        return

    with open(txt_file, 'r', encoding='utf-8') as f:
        text = f.read()

    parts = text.split('ANSWERS')
    if len(parts) < 2:
        print(f"Answers section not found in {txt_file}.")
        return
        
    questions_text = parts[0]
    answers_text = parts[1]

    # --- Part 1: MCQs ---
    mcqs = []
    q_pattern_mcq = re.compile(r'^(\d{2,3})\.\s+(.*?)(?=\n[A-D]\.|\n\d{2,3}\.|\Z)', re.DOTALL | re.MULTILINE)
    question_dict_mcq = {}
    
    for match in q_pattern_mcq.finditer(questions_text):
        q_num = match.group(1).lstrip('0')
        q_text = match.group(2).strip().replace('\n', ' ')
        opt_start = match.end()
        next_q_match = q_pattern_mcq.search(questions_text, opt_start)
        opt_end = next_q_match.start() if next_q_match else len(questions_text)
        options_chunk = questions_text[opt_start:opt_end]
        
        opts = {}
        for opt_label in ['A', 'B', 'C', 'D']:
            opt_match = re.search(fr'{opt_label}\.\s+(.*?)(?=[A-D]\.|\Z)', options_chunk, re.DOTALL)
            if opt_match:
                opts[opt_label] = opt_match.group(1).strip().replace('\n', ' ')
                
        if len(opts) >= 2:
            question_dict_mcq[q_num] = {"question": q_text, "options_raw": opts}

    a_pattern_mcq = re.compile(r'^(\d{2,3})\.\s+\(([A-D])\)\s*(.*?)(?=\n\d{2,3}\.|\Z)', re.DOTALL | re.MULTILINE)
    for match in a_pattern_mcq.finditer(answers_text):
        q_num = match.group(1).lstrip('0')
        correct_opt = match.group(2)
        explanation = match.group(3).strip().replace('\n', ' ')
        
        if q_num in question_dict_mcq:
            q_data = question_dict_mcq[q_num]
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

    # --- Part 2: Subjective / T/F / Fill in blanks ---
    q_pattern_subj = re.compile(r'^(\d{2,3})\.\s+(.*?)(?=\n\d{2,3}\.|\Z)', re.DOTALL | re.MULTILINE)
    question_dict_subj = {}
    for match in q_pattern_subj.finditer(questions_text):
        q_num = match.group(1).lstrip('0')
        q_text = match.group(2).strip().replace('\n', ' ')
        question_dict_subj[q_num] = q_text

    a_pattern_subj = re.compile(r'^(\d{2,3})\.\s+(.*?)(?=\n\d{2,3}\.|\Z)', re.DOTALL | re.MULTILINE)
    answer_dict_subj = {}
    for match in a_pattern_subj.finditer(answers_text):
        q_num = match.group(1).lstrip('0')
        ans_text = match.group(2).strip().replace('\n', ' ')
        if not re.match(r'^\([A-D]\)', ans_text):
            answer_dict_subj[q_num] = ans_text

    subj_blocks = []
    # Avoid duplicate questions that were already parsed as MCQs
    parsed_mcq_nums = [q.lstrip('0') for q in question_dict_mcq.keys()]
    
    for q_num_int in range(1, 1000):
        q_num = str(q_num_int)
        if q_num in question_dict_subj and q_num in answer_dict_subj and q_num not in parsed_mcq_nums:
            q_text = question_dict_subj[q_num]
            a_text = answer_dict_subj[q_num]
            q_text = re.sub(r'A\..*?B\..*?C\..*?D\..*', '', q_text).strip()
            
            if "True or False" in q_text or "True or false" in q_text:
                q_text_clean = q_text.replace("True or False :", "").replace("True or false :", "").strip()
                subj_blocks.append({
                    "type": "theory",
                    "title": f"True / False (Q{q_num})",
                    "content": f"**Statement:** {q_text_clean}\n\n**Answer:** {a_text}"
                })
            elif "Section - B" in q_text or "Section - C" in q_text or "Section - D" in q_text or len(a_text) > 40:
                subj_blocks.append({
                    "type": "theory",
                    "title": f"Subjective Question (Q{q_num})",
                    "content": f"**Question:** {q_text}\n\n**Answer:**\n{a_text}"
                })
            else:
                subj_blocks.append({
                    "type": "theory",
                    "title": f"Short Answer (Q{q_num})",
                    "content": f"**Question:** {q_text}\n\n**Answer:** {a_text}"
                })

    print(f"{subject_title}: Parsed {len(mcqs)} MCQs and {len(subj_blocks)} Subjective Qs.")
    
    output_dir = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters'
    prefixes = ['ncert', 'gseb', 'cbse']
    
    # Save Part 1 (MCQs)
    if len(mcqs) > 0:
        blocks_1 = [{"type": "hook", "content": f"Welcome to the official {subject_title} Question Bank 2026! Let's conquer the Board Exams by practicing these highly expected MCQs."}]
        blocks_1.extend(mcqs[:100])
        
        ch_json_1 = {
            "metadata": {
                "title": f"{subject_title} (Part 1 - MCQs)",
                "subject": "DEO Question Bank 2026",
                "grade": "10",
                "curriculum": ["GSEB", "NCERT", "CBSE"],
                "difficulty": "Advanced",
                "version": "4.0.0-DEO-BANK"
            },
            "blocks": blocks_1
        }
        for prefix in prefixes:
            ch_json_1["metadata"]["id"] = f"{prefix}_class10_deo_bank_2026_ch{start_ch_id}"
            with open(os.path.join(output_dir, f"{ch_json_1['metadata']['id']}.json"), 'w') as f:
                json.dump(ch_json_1, f, indent=2)

    # Save Part 2 (Subjective)
    if len(subj_blocks) > 0:
        blocks_2 = [{"type": "hook", "content": f"Welcome to Part 2 of the {subject_title} DEO Bank! This section covers True/False, Fill in the blanks, and Subjective questions."}]
        blocks_2.extend(subj_blocks[:150])
        
        ch_json_2 = {
            "metadata": {
                "title": f"{subject_title} (Part 2 - Subjective)",
                "subject": "DEO Question Bank 2026",
                "grade": "10",
                "curriculum": ["GSEB", "NCERT", "CBSE"],
                "difficulty": "Advanced",
                "version": "4.0.0-DEO-BANK"
            },
            "blocks": blocks_2
        }
        for prefix in prefixes:
            ch_json_2["metadata"]["id"] = f"{prefix}_class10_deo_bank_2026_ch{start_ch_id+1}"
            with open(os.path.join(output_dir, f"{ch_json_2['metadata']['id']}.json"), 'w') as f:
                json.dump(ch_json_2, f, indent=2)


if __name__ == "__main__":
    parse_deo_file('/home/ubuntu/Shine_Academy_Naroda/raw_data/class10/basic_maths/BASIC_MATHS.txt', 'maths_basic', 'Maths (Basic) DEO Bank 2026', 3)
    parse_deo_file('/home/ubuntu/Shine_Academy_Naroda/raw_data/class10/standard_maths/STANDARD_MATHEMATICS.txt', 'maths_standard', 'Maths (Standard) DEO Bank 2026', 5)
    parse_deo_file('/home/ubuntu/Shine_Academy_Naroda/raw_data/class10/social_science/SOCIAL_SCIENCE.txt', 'social_science', 'Social Science DEO Bank 2026', 7)
    parse_deo_file('/home/ubuntu/Shine_Academy_Naroda/raw_data/class10/english_fl/ENGLISH_FL.txt', 'english', 'English (FL) DEO Bank 2026', 9)
    parse_deo_file('/home/ubuntu/Shine_Academy_Naroda/raw_data/class10/gujarati_sl/GUJARATI_SL.txt', 'gujarati', 'Gujarati (SL) DEO Bank 2026', 11)
