import zipfile
import xml.etree.ElementTree as ET
import os
import json

def extract_odt_text(filepath):
    with zipfile.ZipFile(filepath, 'r') as z:
        content_xml = z.read('content.xml')
    root = ET.fromstring(content_xml)
    texts = []
    for elem in root.iter():
        if elem.text:
            text = elem.text.strip()
            if text:
                texts.append(text)
    return texts

def create_chapter_json(module_id, title, lines, output_dir):
    blocks = [
        {
            "type": "hook",
            "content": f"Welcome to '{title}'! Let's master these essential English sentences."
        }
    ]
    
    current_content = []
    for line in lines:
        current_content.append(line)
        
    if current_content:
        blocks.append({
            "type": "theory",
            "title": "Trilingual Conversational Practice",
            "content": "\n".join(current_content)
        })
        
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": "Are you confident in pronouncing these sentences correctly?",
            "options": [
                "Yes, I practiced with the Audio TTS.",
                "I need to listen to them again.",
                "I am still practicing."
            ],
            "correct_answer": "Yes, I practiced with the Audio TTS.",
            "explanation": "Great! Listening to native pronunciation helps build fluency."
        }
    })
    
    chapter_json = {
        "metadata": {
            "id": module_id,
            "title": title,
            "subject": "Spoken English",
            "grade": "All",
            "curriculum": ["Learn English by Govindsir"],
            "difficulty": "Intermediate",
            "version": "4.0.0"
        },
        "blocks": blocks
    }
    
    output_path = os.path.join(output_dir, f"{module_id}.json")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(chapter_json, f, indent=2, ensure_ascii=False)

def main():
    filepath = '/home/ubuntu/Shine_Academy_Naroda/SAN/ENGLISH/my new version english book.odt'
    output_dir = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters'
    
    print("Reading ODT file...")
    lines = extract_odt_text(filepath)
    print(f"Extracted {len(lines)} lines of text.")
    
    # We will chunk the book into modules of 100 lines each to keep them digestible
    chunk_size = 100
    module_counter = 16 # Start from 16 since 0-15 were used by grammar
    
    # Skip the first 20 lines (copyright, dedication, etc.)
    content_lines = lines[20:]
    
    for i in range(0, len(content_lines), chunk_size):
        chunk = content_lines[i:i + chunk_size]
        module_id = f"spoken_english_mod_{module_counter}"
        title = f"Conversational Practice - Part {module_counter - 15}"
        create_chapter_json(module_id, title, chunk, output_dir)
        module_counter += 1
        
    print(f"Successfully generated {module_counter - 16} new modules from the English Book!")

if __name__ == "__main__":
    main()
