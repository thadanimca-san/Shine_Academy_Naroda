import re
import json
import os
from cleaner_utils import clean_textbook_text

def extract_pearls_from_guide(text, ch_title, subject):
    # This function acts as the "pearl picker". It looks for "GIST", "BASIC CONCEPTS", "SUMMARY" 
    # and ignores the rest of the massive dumps.
    
    blocks = [
        {
            "type": "hook",
            "content": f"Welcome to {ch_title}! Let's learn the core concepts of this chapter quickly and effectively."
        }
    ]
    
    # Try to find "GIST OF THE CHAPTER" or "BASIC CONCEPTS"
    gist_match = re.search(r'(GIST OF THE CHAPTER|BASIC CONCEPTS)(.*?)(?:QUESTIONS|EXERCISE|\Z)', text, re.DOTALL | re.IGNORECASE)
    
    if gist_match:
        gist_content = clean_textbook_text(gist_match.group(2)).strip()
        # Truncate if too long, but guides are usually concise.
        if len(gist_content) > 3000:
            gist_content = gist_content[:3000] + "...\n\n(Rest of the summary in class)"
            
        blocks.append({
            "type": "theory",
            "title": "Key Concepts (Guide Summary)",
            "content": gist_content
        })
    else:
        # Fallback if no specific header is found: Just take the first 1500 chars as summary
        clean_text = clean_textbook_text(text)
        blocks.append({
            "type": "theory",
            "title": "Key Concepts",
            "content": clean_text[:1500] + "...\n\n(Detailed explanation available in class)"
        })
        
    # Knowledge check
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": f"Have you understood the key concepts of '{ch_title}'?",
            "options": [
                "Yes, perfectly.",
                "I need to review the summary.",
                "It connects to real life applications.",
                "All of the above."
            ],
            "correct_answer": "All of the above.",
            "explanation": "Self-reflection is key to Socratic learning!"
        }
    })
    
    return blocks

def parse_guide_chapter(txt_file, ch_id, ch_title, subject, output_dir):
    if not os.path.exists(txt_file):
        return

    with open(txt_file, 'r', encoding='utf-8') as f:
        raw_text = f.read()

    # Skip empty/scanned PDFs (like Science)
    if len(raw_text.strip()) < 100:
        return

    blocks = extract_pearls_from_guide(raw_text, ch_title, subject)

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
    
    # Reparse SS with Guides
    ss_titles = [
        "Heritage of India", "Cultural Heritage of India", "Cultural Heritage of India: Sculpture and Architecture", 
        "Literary Heritage of India", "India's Heritage of Science and Technology", "Places of Indian Cultural Heritage", 
        "Preservation of Our Heritage", "Natural Resources", "Forest and Wildlife Resources", "India: Agriculture", 
        "India: Water Resources", "India: Minerals and Energy Resources", "Manufacturing Industries", 
        "Transportation, Communication and Trade", "Economic Development", "Economic Liberalization and Globalization", 
        "Economic Problems and Challenges", "Price Rise and Consumer Awareness", "Human Development", 
        "Social Problems of India and Challenges", "Social Change"
    ]
    for i in range(1, 22):
        txt_file = f'/home/ubuntu/Shine_Academy_Naroda/raw_data/class10/social_science/ch{i}g.txt'
        parse_guide_chapter(txt_file, i, ss_titles[i-1], "Social Science", out_dir)
        
    # Reparse Maths with Guides
    math_titles = ["Real Numbers", "Polynomials", "Pair of Linear Equations in Two Variables", "Quadratic Equations", "Arithmetic Progressions", "Triangles", "Coordinate Geometry", "Introduction to Trigonometry", "Some Applications of Trigonometry", "Circles", "Constructions", "Areas Related to Circles", "Surface Areas and Volumes", "Statistics", "Probability"]
    for i in range(1, 15):
        txt_file = f'/home/ubuntu/Shine_Academy_Naroda/raw_data/class10/maths/ch{i}g.txt'
        parse_guide_chapter(txt_file, i, math_titles[i-1], "Maths", out_dir)

    print("Cleaned and Parsed Guides (Moti) for SS & Maths!")
