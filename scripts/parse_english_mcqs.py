import re
import json
import os
from cleaner_utils import clean_textbook_text

def parse_english_mcq_chapter(txt_file, ch_id, ch_title, output_dir):
    if not os.path.exists(txt_file):
        return

    with open(txt_file, 'r', encoding='utf-8') as f:
        raw_text = f.read()
        
    text = clean_textbook_text(raw_text)

    blocks = [
        {
            "type": "hook",
            "content": f"Welcome to '{ch_title}'! Let's test your understanding of this story with some hand-picked questions."
        }
    ]
    
    # Heuristic to find questions: "1. Question text" followed by "[A] ... [B] ... [C] ... [D] ..."
    # We look for \d+\.\s+(.*?)(?=\[A\])
    
    pattern = re.compile(r'(\d+)\.\s+(.*?)\s+(\[A\].*?\[D\].*?)(?=\n\d+\.|\Z)', re.DOTALL)
    
    mcq_count = 0
    for match in pattern.finditer(text):
        q_num = match.group(1)
        q_text = match.group(2).strip().replace('\n', ' ')
        options_text = match.group(3).strip().replace('\n', ' ')
        
        # Extract correct answer which has "(Correct)"
        # e.g., "[A] Option 1 [B] Option 2 [C] Option 3 (Correct) [D] Option 4"
        opt_pattern = re.compile(r'\[([A-D])\]\s+(.*?)(?=\[[A-D]\]|\Z)')
        
        parsed_options = []
        correct_answer = ""
        
        for opt_match in opt_pattern.finditer(options_text):
            opt_letter = opt_match.group(1)
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
                    "explanation": "Correct answer as per the DEO question bank."
                }
            })
            mcq_count += 1
            
        if mcq_count >= 15: # Limit to 15 pearls so it's not overwhelming
            break

    if mcq_count == 0:
        blocks.append({
            "type": "theory",
            "title": "Chapter Overview",
            "content": f"Please refer to the textbook for '{ch_title}'. Interactive questions will be added soon."
        })
        
    chapter_json = {
        "metadata": {
            "title": ch_title,
            "subject": "English",
            "grade": "10",
            "curriculum": ["GSEB", "NCERT", "CBSE"],
            "difficulty": "Intermediate",
            "version": "4.0.0"
        },
        "blocks": blocks
    }
    
    for prefix in ['ncert', 'gseb', 'cbse']:
        ch_json = dict(chapter_json)
        ch_json["metadata"]["id"] = f"{prefix}_class10_english_ch{ch_id}"
        with open(os.path.join(output_dir, f"{ch_json['metadata']['id']}.json"), 'w') as f:
            json.dump(ch_json, f, indent=2)

if __name__ == "__main__":
    out_dir = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters'
    
    # 9 Chapters for English First Flight (Prose/Poetry mix)
    english_titles = [
        "A Letter to God",
        "Nelson Mandela: Long Walk to Freedom",
        "Two Stories about Flying",
        "From the Diary of Anne Frank",
        "Glimpses of India",
        "Mijbil the Otter",
        "Madam Rides the Bus",
        "The Sermon at Benares",
        "The Proposal"
    ]
    for i in range(1, 10):
        txt_file = f'/home/ubuntu/Shine_Academy_Naroda/raw_data/class10/english/ch{i}mcq.txt'
        parse_english_mcq_chapter(txt_file, i, english_titles[i-1], out_dir)

    print("Extracted English MCQs (Pearls) successfully!")
