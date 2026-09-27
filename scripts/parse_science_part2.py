import re
import json
import os

def parse_science_part2():
    with open('/home/ubuntu/Shine_Academy_Naroda/raw_data/class10/science/SCIENCE.txt', 'r', encoding='utf-8') as f:
        text = f.read()

    parts = text.split('ANSWERS')
    if len(parts) < 2:
        print("Answers section not found.")
        return
        
    questions_text = parts[0]
    answers_text = parts[1]

    # Find Fill in the blanks (Q80 to Q143)
    # The format is "80. ............. is not an olfactory..."
    
    # Simple regex to find questions starting with "XX. "
    q_pattern = re.compile(r'^(\d{2,3})\.\s+(.*?)(?=\n\d{2,3}\.|\Z)', re.DOTALL | re.MULTILINE)
    
    question_dict = {}
    for match in q_pattern.finditer(questions_text):
        q_num = match.group(1).lstrip('0')
        q_text = match.group(2).strip().replace('\n', ' ')
        question_dict[q_num] = q_text

    # Parse answers (anything that isn't A, B, C, D in parentheses)
    # Since MCQs answers were like "01. (B) the fuel...", other answers are like "80. Phenolphthalein"
    a_pattern = re.compile(r'^(\d{2,3})\.\s+(.*?)(?=\n\d{2,3}\.|\Z)', re.DOTALL | re.MULTILINE)
    
    answer_dict = {}
    for match in a_pattern.finditer(answers_text):
        q_num = match.group(1).lstrip('0')
        ans_text = match.group(2).strip().replace('\n', ' ')
        
        # If it starts with (A), (B), (C), (D) it's an MCQ, skip it
        if not re.match(r'^\([A-D]\)', ans_text):
            answer_dict[q_num] = ans_text

    blocks = [{"type": "hook", "content": "Welcome to Part 2 of the Science DEO Bank! This section covers True/False, Fill in the blanks, and Subjective questions."}]
    
    parsed_count = 0
    
    # Let's just process Q80 to Q500 if we have both Q and A
    for q_num_int in range(80, 561):
        q_num = str(q_num_int)
        if q_num in question_dict and q_num in answer_dict:
            q_text = question_dict[q_num]
            a_text = answer_dict[q_num]
            
            # Remove MCQ options if they accidentally got attached to q_text
            q_text = re.sub(r'A\..*?B\..*?C\..*?D\..*', '', q_text).strip()
            
            # Determine type
            if "True or False" in q_text or "True or false" in q_text:
                q_text_clean = q_text.replace("True or False :", "").replace("True or false :", "").strip()
                blocks.append({
                    "type": "theory",
                    "title": f"True / False (Q{q_num})",
                    "content": f"**Statement:** {q_text_clean}\n\n**Answer:** {a_text}"
                })
                parsed_count += 1
                
            elif "Section - B" in q_text or "Section - C" in q_text or "Section - D" in q_text or len(a_text) > 40:
                # Treat as subjective
                blocks.append({
                    "type": "theory",
                    "title": f"Subjective Question (Q{q_num})",
                    "content": f"**Question:** {q_text}\n\n**Answer:**\n{a_text}"
                })
                parsed_count += 1
                
            else:
                # Treat as short answer
                blocks.append({
                    "type": "theory",
                    "title": f"Short Answer (Q{q_num})",
                    "content": f"**Question:** {q_text}\n\n**Answer:** {a_text}"
                })
                parsed_count += 1

    print(f"Parsed {parsed_count} subjective/T/F questions.")
    
    if parsed_count > 0:
        chapter_json = {
            "metadata": {
                "id": "ncert_class10_deo_bank_2026_ch2",
                "title": "Science DEO Bank 2026 (Part 2 - Subjective)",
                "subject": "DEO Question Bank 2026",
                "grade": "10",
                "curriculum": ["GSEB", "NCERT", "CBSE"],
                "difficulty": "Advanced",
                "version": "4.0.0-DEO-BANK"
            },
            "blocks": blocks[:150] # Limit to 150 blocks so UI doesn't lag too much
        }
        
        output_dir = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters'
        
        with open(os.path.join(output_dir, 'ncert_class10_deo_bank_2026_ch2.json'), 'w') as f:
            json.dump(chapter_json, f, indent=2)
            
        with open(os.path.join(output_dir, 'gseb_class10_deo_bank_2026_ch2.json'), 'w') as f:
            json_data_gseb = dict(chapter_json)
            json_data_gseb["metadata"]["id"] = "gseb_class10_deo_bank_2026_ch2"
            json.dump(json_data_gseb, f, indent=2)
            
        with open(os.path.join(output_dir, 'cbse_class10_deo_bank_2026_ch2.json'), 'w') as f:
            json_data_cbse = dict(chapter_json)
            json_data_cbse["metadata"]["id"] = "cbse_class10_deo_bank_2026_ch2"
            json.dump(json_data_cbse, f, indent=2)
            
        print("Generated JSON for Ch2.")

if __name__ == "__main__":
    parse_science_part2()
