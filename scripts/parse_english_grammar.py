import re
import json
import os
import glob

def clean_line(line):
    return line.replace('\x0c', '').strip()

def parse_grammar_file(txt_file, module_id, title):
    with open(txt_file, 'r', encoding='utf-8') as f:
        lines = [clean_line(line) for line in f.readlines() if clean_line(line) != '']
        
    blocks = [
        {
            "type": "hook",
            "content": f"Welcome to the module: '{title}'. Let's practice English sentences!"
        }
    ]
    
    current_sentences = []
    
    for line in lines:
        if re.match(r'^\d+\.', line):
            if current_sentences:
                blocks.append({
                    "type": "theory",
                    "title": "Practice Set",
                    "content": "\n".join(current_sentences)
                })
                current_sentences = []
            continue
            
        if "→" in line:
            parts = line.split("→")
            eng = parts[0].strip()
            hin = parts[1].strip()
            current_sentences.append(f"**{eng}**\n*Meaning:* {hin}\n")
        else:
            current_sentences.append(f"**{line}**")

    if current_sentences:
        blocks.append({
            "type": "theory",
            "title": "Practice Set",
            "content": "\n".join(current_sentences)
        })
        
    # Generate some knowledge checks
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "Can you translate these sentences accurately?",
            "options": [
                "Yes, I have mastered this set.",
                "I need to review the module again.",
                "I need more practice."
            ],
            "correct_answer": "Yes, I have mastered this set.",
            "explanation": "Consistent practice makes your English perfect!"
        }
    })
    
    chapter_json = {
        "metadata": {
            "id": module_id,
            "title": title,
            "subject": "Spoken English",
            "grade": "All",
            "curriculum": ["Learn English by Govindsir"],
            "difficulty": "Beginner",
            "version": "4.0.0"
        },
        "blocks": blocks
    }
    
    output_path = os.path.join("/home/ubuntu/Shine_Academy_Naroda/app_core/chapters", f"{module_id}.json")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(chapter_json, f, indent=2, ensure_ascii=False)

def main():
    txt_files = glob.glob("/home/ubuntu/Shine_Academy_Naroda/SAN/ENGLISH/pdfs/*.txt")
    
    for i, txt_file in enumerate(sorted(txt_files)):
        basename = os.path.basename(txt_file).replace('.txt', '')
        # Filter only grammar/sentence ones
        if 'simple' in basename or 'continuous' in basename or 'perfect' in basename or 'Sentences' in basename:
            module_id = f"spoken_english_mod_{i}"
            title = basename.replace("-", " ").replace("_", " ").title()
            parse_grammar_file(txt_file, module_id, title)
            print(f"Parsed: {title} -> {module_id}")

if __name__ == "__main__":
    main()
