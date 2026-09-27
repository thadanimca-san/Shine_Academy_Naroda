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
            "grade": "9",
            "curriculum": ["GSEB", "NCERT", "CBSE"],
            "difficulty": "Intermediate",
            "version": "4.0.0"
        },
        "blocks": blocks
    }
    
    for prefix in ['ncert', 'gseb', 'cbse']:
        ch_json = dict(chapter_json)
        ch_json["metadata"]["id"] = f"{prefix}_class9_{sub_id}_ch{ch_id}"
        with open(os.path.join(output_dir, f"{ch_json['metadata']['id']}.json"), 'w') as f:
            json.dump(ch_json, f, indent=2)

if __name__ == "__main__":
    out_dir = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters'
    
    # Class 9 SS
    ss_titles = ["Rise of British Rule in India", "First World War and Russian Revolution", "Movement Towards a New World", "National Movements in India", "Movement Towards Independence", "India: After Independence", "Post-Independence India", "Framing of Constitution and its Features", "Fundamental Rights, Fundamental Duties and Directive Principles of State Policy", "Organs of Government", "Indian Judiciary", "Indian Democracy", "India: Location, Geological Structure and Physiography I", "India: Location, Geological Structure and Physiography II", "Drainage System", "Climate", "Natural Vegetation", "Wildlife", "India: Human Life", "Disaster Management"]
    for i in range(1, 21):
        txt_file = f'/home/ubuntu/Shine_Academy_Naroda/SAN/9ss/ch{i}mcq.txt'
        parse_mcq_chapter(txt_file, i, ss_titles[i-1], "Social Science", out_dir)
        
    # Class 9 English
    english_titles = ["The Fun They Had", "The Sound of Music", "The Little Girl", "A Truly Beautiful Mind", "The Snake and the Mirror", "My Childhood", "Packing", "Reach for the Top", "The Bond of Love", "Kathmandu", "If I Were You"]
    for i in range(1, 10):
        txt_file = f'/home/ubuntu/Shine_Academy_Naroda/SAN/9english/ch{i}mcq.txt'
        parse_mcq_chapter(txt_file, i, english_titles[i-1], "English", out_dir)

    print("Extracted Class 9 SS & English MCQs (Pearls) successfully!")
