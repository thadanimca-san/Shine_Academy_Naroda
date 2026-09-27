import os
import json
import time
import glob
import subprocess
import google.generativeai as genai

API_KEY = "AIzaSyCXHEJ4KBrebP8ByUEZnVJzuE4u114MGGA"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-3.5-flash-lite')

PDF_DIR = "/home/ubuntu/Shine_Academy_Naroda/SAN/Year2026/engpdf12thcommerce"
OUTPUT_DIR = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters"

def extract_text(pdf_path):
    text_path = pdf_path.replace(".pdf", ".txt")
    
    try:
        if not os.path.exists(text_path):
            print(f"  Extracting literature text from {os.path.basename(pdf_path)}...")
            subprocess.run(["pdftotext", pdf_path, text_path], check=True)
            
        with open(text_path, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read()
    except Exception as e:
        print(f"  Failed to extract text from {pdf_path}: {e}")
        return ""

def generate_english_blocks(text_chunk, filename):
    prompt = f"""
    You are the Chief Academic Architect of Shine Academy Naroda.
    
    We are generating a Masterclass for Class 12 English (CBSE NCERT). 
    This is a literature subject, so focus on Comprehension, Themes, Poetic Devices, and Vocabulary.
    
    Read the following text chunk (extracted from an NCERT English textbook PDF).
    
    Use a literature-focused version of the 8-Step Socratic Gold Pedagogy:
    1. A 'hook' block introducing the theme (e.g., poverty, courage, childhood).
    2. A 'socratic' block asking the student to predict something about the characters.
    3. Several 'theory' blocks summarizing the story/poem in easy-to-read bites.
    4. A 'teacher_tip' block explaining a difficult English vocabulary word or a Poetic Device (Simile, Metaphor).
    5. A 'reflection' block on the moral of the story.
    
    CRITICAL RULE:
    Every single block MUST have English, Hindi, AND Gujarati translations for ALL text (title_hi, title_gu, body_hi, body_gu). This is crucial for students who struggle with English.
    
    Text chunk:
    {text_chunk}
    
    Expected JSON Output (Return ONLY a valid JSON array of blocks):
    [
      {{
        "id": "KOBJ_ENG12_{filename.split('.')[0].upper()}_HOOK",
        "type": "hook",
        "title": "Story Theme", "title_hi": "...", "title_gu": "...",
        "body": "...", "body_hi": "...", "body_gu": "..."
      }}
    ]
    """
    
    while True:
        try:
            print(f"  Generating Literature JSON blocks via Gemini API...")
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
    print("--- 📚 Generating Class 12 English Literature Masterclass ---")
    
    pdf_files = glob.glob(os.path.join(PDF_DIR, "*.pdf"))
    
    if not pdf_files:
        print(f"Error: No PDFs found in {PDF_DIR}")
        return
        
    print(f"Found {len(pdf_files)} PDF files to process.")
    
    for pdf_path in sorted(pdf_files):
        filename = os.path.basename(pdf_path)
        base_name = filename.split('.')[0]
        
        print(f"\nProcessing {filename}...")
        
        out_filename = f"ncert_class12_english_{base_name}.json"
        out_filepath = os.path.join(OUTPUT_DIR, out_filename)
        if os.path.exists(out_filepath):
            try:
                with open(out_filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                b = data.get('blocks', []) if isinstance(data, dict) else data
                if len(b) > 0:
                    print(f"  Skipping {filename} (already generated with blocks).")
                    continue
            except Exception:
                pass
        
        full_text = extract_text(pdf_path)
        if not full_text:
            continue
            
        full_text = full_text.replace('\f', '\n').strip()
        
        # Take an initial chunk of 6000 characters to capture the story summary
        chunk_size = 6000
        first_chunk = full_text[:chunk_size]
        
        blocks = generate_english_blocks(first_chunk, filename)
        
        chapter_json = {
            "metadata": {
                "id": f"ncert_class12_english_{base_name}",
                "title": f"Class 12 English - {base_name.capitalize()}",
                "subject": "English Core",
                "grade": "12",
                "curriculum": ["CBSE", "NCERT"],
                "difficulty": "Intermediate",
                "estimated_minutes": 45
            },
            "blocks": blocks
        }
        
        out_filename = f"ncert_class12_english_{base_name}.json"
        out_filepath = os.path.join(OUTPUT_DIR, out_filename)
        
        with open(out_filepath, 'w', encoding='utf-8') as f:
            json.dump(chapter_json, f, ensure_ascii=False, indent=2)
            
        print(f"  ✅ Successfully saved {out_filename}!")
        time.sleep(5) # API safety
        
    print("All Class 12 English chapters generated successfully!")

if __name__ == "__main__":
    main()
