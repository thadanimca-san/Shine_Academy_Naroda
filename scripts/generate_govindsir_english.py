import os
import json
import time
import zipfile
import xml.etree.ElementTree as ET
import google.generativeai as genai

API_KEY = "AIzaSyCXHEJ4KBrebP8ByUEZnVJzuE4u114MGGA"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-3.5-flash-lite')

ODT_FILE = "/home/ubuntu/Shine_Academy_Naroda/SAN/Year2026/speak_english_confidently.odt"
OUTPUT_DIR = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters"

def extract_text_from_odt(file_path):
    print("Extracting text from ODT file...")
    text_content = []
    try:
        with zipfile.ZipFile(file_path, 'r') as zf:
            content_xml = zf.read('content.xml')
            
        root = ET.fromstring(content_xml)
        
        # ODT namespace map
        namespaces = {
            'text': 'urn:oasis:names:tc:opendocument:xmlns:text:1.0'
        }
        
        for elem in root.iter():
            if elem.tag.endswith('}p') or elem.tag.endswith('}h'):
                if elem.text:
                    text_content.append(elem.text)
                for child in elem:
                    if child.text:
                        text_content.append(child.text)
                    if child.tail:
                        text_content.append(child.tail)
                        
        full_text = "\n".join(text_content)
        print(f"Successfully extracted {len(full_text)} characters of text.")
        return full_text
    except Exception as e:
        print(f"Failed to read ODT: {e}")
        return ""

def generate_chapter_blocks(text_chunk, ch_num):
    prompt = f"""
    You are an expert curriculum designer for 'Learn English by GovindSir'.
    
    Convert the following text chunk into a fully interactive Shine Academy EduOS JSON chapter according to the Gold Standard Pedagogy.
    
    CRITICAL RULE:
    Every single block MUST have English, Hindi, AND Gujarati translations (e.g. title, title_hi, title_gu, body, body_hi, body_gu).
    
    Text chunk:
    {text_chunk}
    
    Expected JSON Output (Return ONLY a JSON array of blocks):
    [
      {{
        "id": "GOVIND_ENG_CH{ch_num}_HOOK",
        "type": "hook",
        "title": "...", "title_hi": "...", "title_gu": "...",
        "body": "...", "body_hi": "...", "body_gu": "..."
      }},
      {{
        "id": "GOVIND_ENG_CH{ch_num}_THEORY",
        "type": "theory",
        "title": "...", "title_hi": "...", "title_gu": "...",
        "body": "...", "body_hi": "...", "body_gu": "..."
      }}
    ]
    """
    
    while True:
        try:
            print(f"  Generating JSON for chapter {ch_num}...")
            response = model.generate_content(prompt)
            res_text = response.text.strip()
            if res_text.startswith("```json"):
                res_text = res_text[7:-3].strip()
            elif res_text.startswith("```"):
                res_text = res_text[3:-3].strip()
                
            data = json.loads(res_text)
            return data
            
        except Exception as e:
            if "429" in str(e) or "Quota" in str(e):
                print("  * Rate limit hit. Waiting 60 seconds...")
                time.sleep(60)
            else:
                print(f"  * JSON parse error: {e}. Retrying in 5s...")
                time.sleep(5)

def main():
    print("--- Generating 'Learn English by GovindSir' Chapters ---")
    
    if not os.path.exists(ODT_FILE):
        print("Error: speak_english_confidently.odt not found!")
        return
        
    full_text = extract_text_from_odt(ODT_FILE)
    if not full_text:
        return
        
    # Chunk the text into ~2000 character pieces to act as chapters
    chunk_size = 2000
    chunks = [full_text[i:i+chunk_size] for i in range(0, len(full_text), chunk_size)]
    
    print(f"Split document into {len(chunks)} chapters to generate.")
    
    for idx, chunk in enumerate(chunks):
        ch_num = idx + 1
        blocks = generate_chapter_blocks(chunk, ch_num)
        
        chapter_json = {
            "metadata": {
                "id": f"govind_english_ch{ch_num}",
                "title": f"Speak English Confidently - Module {ch_num}",
                "subject": "Spoken English",
                "grade": "All",
                "difficulty": "Beginner",
                "estimated_minutes": 20
            },
            "blocks": blocks
        }
        
        filename = f"govind_english_ch{ch_num}.json"
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(chapter_json, f, ensure_ascii=False, indent=2)
            
        print(f"Successfully saved {filename}!")
        time.sleep(5) # API safety
        
    print("All GovindSir English chapters generated successfully!")

if __name__ == "__main__":
    main()
