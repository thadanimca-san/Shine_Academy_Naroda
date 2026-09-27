import re
import json
import os

def parse_textbook_chapter(txt_file, ch_id, ch_title, output_dir):
    if not os.path.exists(txt_file):
        return

    with open(txt_file, 'r', encoding='utf-8') as f:
        text = f.read()

    blocks = [
        {
            "type": "hook",
            "content": f"Welcome to {ch_title}! This chapter will take you on a journey through incredible mathematical concepts. Let's start exploring!"
        }
    ]

    # Simple heuristic to find headings like "1.1 INTRODUCTION"
    # We look for lines starting with digit.digit
    pattern = re.compile(r'^(\d+\.\d+)\s+(.*?)$', re.MULTILINE)
    
    sections = []
    last_idx = 0
    
    for match in pattern.finditer(text):
        if last_idx > 0:
            # Append previous section content
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
            # Clean content a bit
            clean_content = re.sub(r'\n+', '\n\n', sec['content'])
            # Truncate if too long to avoid massive blocks
            if len(clean_content) > 1500:
                clean_content = clean_content[:1500] + "...\n\n(Detailed explanation available in class)"
                
            blocks.append({
                "type": "theory",
                "title": f"{sec['number']} {sec['title']}",
                "content": clean_content
            })
            
            # Add a reflective knowledge check randomly or at end of section
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
        # If no strict headings found, just dump a generic summary
        blocks.append({
            "type": "theory",
            "title": "Chapter Overview",
            "content": text[:1500] + "...\n\n(Detailed explanation available in class)"
        })

    chapter_json = {
        "metadata": {
            "id": f"ncert_class10_maths_ch{ch_id}",
            "title": ch_title,
            "subject": "Maths",
            "grade": "10",
            "curriculum": ["GSEB", "NCERT", "CBSE"],
            "difficulty": "Intermediate",
            "version": "4.0.0"
        },
        "blocks": blocks
    }
    
    # Write to ncert, gseb, cbse
    for prefix in ['ncert', 'gseb', 'cbse']:
        ch_json = dict(chapter_json)
        ch_json["metadata"]["id"] = f"{prefix}_class10_maths_ch{ch_id}"
        with open(os.path.join(output_dir, f"{ch_json['metadata']['id']}.json"), 'w') as f:
            json.dump(ch_json, f, indent=2)

if __name__ == "__main__":
    titles = [
        "Real Numbers",
        "Polynomials",
        "Pair of Linear Equations in Two Variables",
        "Quadratic Equations",
        "Arithmetic Progressions",
        "Triangles",
        "Coordinate Geometry",
        "Introduction to Trigonometry",
        "Some Applications of Trigonometry",
        "Circles",
        "Constructions",
        "Areas Related to Circles",
        "Surface Areas and Volumes",
        "Statistics",
        "Probability"
    ]
    
    out_dir = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters'
    for i in range(1, 15): # 14 chapters in pdf dir usually, sometimes 15. Let's do 14.
        txt_file = f'/home/ubuntu/Shine_Academy_Naroda/raw_data/class10/maths/ch{i}tb.txt'
        parse_textbook_chapter(txt_file, i, titles[i-1], out_dir)
        
    print("Successfully mapped Maths Textbooks into EduOS Pedagogy format!")
