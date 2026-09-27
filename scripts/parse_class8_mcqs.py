import re
import json
import os
from cleaner_utils import clean_textbook_text

def parse_mcq_chapter(txt_file, ch_id, ch_title, subject, output_dir):
    if not os.path.exists(txt_file):
        return

    with open(txt_file, 'r', encoding='utf-8') as f:
        raw_text = f.read()
        
    text = clean_textbook_text(raw_text)

    blocks = [
        {
            "type": "hook",
            "content": f"Welcome to '{ch_title}'! Let's test your understanding with some hand-picked questions."
        }
    ]
    
    pattern = re.compile(r'(\d+)\.\s+(.*?)\s+(\[A\].*?\[D\].*?)(?=\n\d+\.|\Z)', re.DOTALL)
    
    mcq_count = 0
    for match in pattern.finditer(text):
        q_num = match.group(1)
        q_text = match.group(2).strip().replace('\n', ' ')
        options_text = match.group(3).strip().replace('\n', ' ')
        
        opt_pattern = re.compile(r'\[([A-D])\]\s+(.*?)(?=\[[A-D]\]|\Z)')
        
        parsed_options = []
        correct_answer = ""
        
        for opt_match in opt_pattern.finditer(options_text):
            opt_val = opt_match.group(2).strip()
            
            if "(Correct)" in opt_val:
                clean_val = opt_val.replace("(Correct)", "").strip()
                correct_answer = clean_val
                parsed_options.append(clean_val)
            else:
                parsed_options.append(opt_val)
                
        if len(parsed_options) >= 2 and correct_answer != "":
            blocks.append({
                "type": "knowledge_check",
                "content": {
                    "question": f"Q{q_num}: {q_text}",
                    "options": parsed_options,
                    "correct_answer": correct_answer,
                    "explanation": "Correct answer as per the question bank."
                }
            })
            mcq_count += 1
            
        if mcq_count >= 15:
            break

    if mcq_count == 0:
        blocks.append({
            "type": "theory",
            "title": "Chapter Overview",
            "content": f"Please refer to the textbook for '{ch_title}'. Interactive questions will be added soon."
        })
        
    sub_id = subject.lower().replace(" ", "_")
    chapter_json = {
        "metadata": {
            "title": ch_title,
            "subject": subject,
            "grade": "8",
            "curriculum": ["GSEB", "NCERT", "CBSE"],
            "difficulty": "Intermediate",
            "version": "4.0.0"
        },
        "blocks": blocks
    }
    
    for prefix in ['ncert', 'gseb', 'cbse']:
        ch_json = dict(chapter_json)
        ch_json["metadata"]["id"] = f"{prefix}_class8_{sub_id}_ch{ch_id}"
        with open(os.path.join(output_dir, f"{ch_json['metadata']['id']}.json"), 'w') as f:
            json.dump(ch_json, f, indent=2)

if __name__ == "__main__":
    out_dir = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters'
    
    # Class 8 Maths
    math_titles = ["Rational Numbers", "Linear Equations in One Variable", "Understanding Quadrilaterals", "Practical Geometry", "Data Handling", "Squares and Square Roots", "Cubes and Cube Roots", "Comparing Quantities", "Algebraic Expressions and Identities", "Visualising Solid Shapes", "Mensuration", "Exponents and Powers", "Direct and Inverse Proportions"]
    for i in range(1, 14):
        txt_file = f'/home/ubuntu/Shine_Academy_Naroda/SAN/8maths/ch{i}mcq.txt'
        parse_mcq_chapter(txt_file, i, math_titles[i-1], "Maths", out_dir)
        
    # Class 8 Science
    sci_titles = ["Crop Production and Management", "Microorganisms: Friend and Foe", "Synthetic Fibres and Plastics", "Materials: Metals and Non-Metals", "Coal and Petroleum", "Combustion and Flame", "Conservation of Plants and Animals", "Cell - Structure and Functions", "Reproduction in Animals", "Reaching the Age of Adolescence", "Force and Pressure", "Friction", "Sound"]
    for i in range(1, 14):
        txt_file = f'/home/ubuntu/Shine_Academy_Naroda/SAN/8science/ch{i}mcq.txt'
        parse_mcq_chapter(txt_file, i, sci_titles[i-1], "Science", out_dir)

    # Class 8 SS
    ss_titles = ["Arrival of Europeans in India", "What is Around Us", "Indian Constitution", "How the Supreme Court Functions", "Natural Disasters", "Effects of British Rule in India", "Environmental Changes", "Role of Parliament in a Democratic Country", "The Freedom Movement of 1857", "Socio-Religious Reforms", "Agriculture", "Industry", "Human Resources", "Disaster Management", "Judiciary", "Criminal Justice System", "Understanding Marginalisation", "Confronting Marginalisation", "Public Facilities"]
    for i in range(1, 20):
        txt_file = f'/home/ubuntu/Shine_Academy_Naroda/SAN/8ss/ch{i}mcq.txt'
        parse_mcq_chapter(txt_file, i, ss_titles[i-1], "Social Science", out_dir)

    # Class 8 English
    english_titles = ["The Best Christmas Present in the World", "The Tsunami", "Glimpses of the Past", "Bepin Choudhury's Lapse of Memory", "The Summit Within", "This is Jody's Fawn", "A Visit to Cambridge", "A Short Monsoon Diary"]
    for i in range(1, 9):
        txt_file = f'/home/ubuntu/Shine_Academy_Naroda/SAN/8english/ch{i}mcq.txt'
        parse_mcq_chapter(txt_file, i, english_titles[i-1], "English", out_dir)

    print("Extracted Class 8 MCQs (Pearls) successfully!")
