import re
import json
import os
from cleaner_utils import clean_textbook_text

def parse_textbook_chapter(txt_file, ch_id, ch_title, subject, output_dir):
    if not os.path.exists(txt_file):
        return

    with open(txt_file, 'r', encoding='utf-8') as f:
        raw_text = f.read()

    text = clean_textbook_text(raw_text)

    blocks = [
        {
            "type": "hook",
            "content": f"Welcome to {ch_title}! This chapter will take you on a journey through incredible {subject} concepts. Let's start exploring!"
        }
    ]

    pattern = re.compile(r'^(\d+\.\d+)\s+(.*?)$', re.MULTILINE)
    
    sections = []
    last_idx = 0
    
    for match in pattern.finditer(text):
        if last_idx > 0:
            sections[-1]['content'] = text[last_idx:match.start()].strip()
            
        sections.append({
            "number": match.group(1),
            "title": match.group(2).strip(),
            "content": ""
        })
        last_idx = match.end()
        
    if len(sections) > 0:
        sections[-1]['content'] = text[last_idx:].strip()
        
        for sec in sections:
            clean_content = sec['content']
            if len(clean_content) > 1200:
                clean_content = clean_content[:1200] + "...\n\n(Detailed explanation available in class)"
                
            blocks.append({
                "type": "theory",
                "title": f"{sec['number']} {sec['title']}",
                "content": clean_content
            })
            
            blocks.append({
                "type": "knowledge_check",
                "content": {
                    "question": f"Based on what we just read about '{sec['title']}', what is the key takeaway?",
                    "options": [
                        "I understand the concept perfectly.",
                        "I need to review this again.",
                        "It connects to real life applications.",
                        "All of the above."
                    ],
                    "correct_answer": "All of the above.",
                    "explanation": "Self-reflection is key to Socratic learning!"
                }
            })
            
    else:
        blocks.append({
            "type": "theory",
            "title": "Chapter Overview",
            "content": text[:1200] + "...\n\n(Detailed explanation available in class)"
        })

    sub_id = subject.lower().replace(" ", "_")
    chapter_json = {
        "metadata": {
            "title": ch_title,
            "subject": subject,
            "grade": "10",
            "curriculum": ["GSEB", "NCERT", "CBSE"],
            "difficulty": "Intermediate",
            "version": "4.0.0"
        },
        "blocks": blocks
    }
    
    for prefix in ['ncert', 'gseb', 'cbse']:
        ch_json = dict(chapter_json)
        ch_json["metadata"]["id"] = f"{prefix}_class10_{sub_id}_ch{ch_id}"
        with open(os.path.join(output_dir, f"{ch_json['metadata']['id']}.json"), 'w') as f:
            json.dump(ch_json, f, indent=2)

if __name__ == "__main__":
    out_dir = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters'
    
    # Reparse Science
    sci_titles = ["Chemical Reactions and Equations", "Acids, Bases and Salts", "Metals and Non-metals", "Carbon and its Compounds", "Life Processes", "Control and Coordination", "How do Organisms Reproduce?", "Heredity", "Light - Reflection and Refraction", "The Human Eye and the Colourful World", "Electricity", "Magnetic Effects of Electric Current", "Our Environment"]
    for i in range(1, 14):
        txt_file = f'/home/ubuntu/Shine_Academy_Naroda/raw_data/class10/science/ch{i}tb.txt'
        parse_textbook_chapter(txt_file, i, sci_titles[i-1], "Science", out_dir)
        
    # Reparse Maths
    math_titles = ["Real Numbers", "Polynomials", "Pair of Linear Equations in Two Variables", "Quadratic Equations", "Arithmetic Progressions", "Triangles", "Coordinate Geometry", "Introduction to Trigonometry", "Some Applications of Trigonometry", "Circles", "Constructions", "Areas Related to Circles", "Surface Areas and Volumes", "Statistics", "Probability"]
    for i in range(1, 15):
        txt_file = f'/home/ubuntu/Shine_Academy_Naroda/raw_data/class10/maths/ch{i}tb.txt'
        parse_textbook_chapter(txt_file, i, math_titles[i-1], "Maths", out_dir)

    print("Cleaned and Reparsed Science & Maths Textbooks!")
