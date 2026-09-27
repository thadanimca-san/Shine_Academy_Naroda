import os
import json
import time
import glob
import subprocess
import google.generativeai as genai

API_KEY = "AIzaSyCXHEJ4KBrebP8ByUEZnVJzuE4u114MGGA"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-3.5-flash-lite')

OUTPUT_DIR = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters"

DIRECTORIES_TO_SCAN = {
    "science": "/home/ubuntu/Shine_Academy_Naroda/SAN/Year2026/sciencepdf10th",
    "maths": "/home/ubuntu/Shine_Academy_Naroda/SAN/10maths/pdfs",
    "sanskrit": "/home/ubuntu/Shine_Academy_Naroda/SAN/10sanskrit/pdfs",
    "gujarati": "/home/ubuntu/Shine_Academy_Naroda/SAN/10gujarati/pdfs"
}

def extract_text(pdf_path):
    text_path = pdf_path.replace(".pdf", ".txt")
    
    try:
        if not os.path.exists(text_path):
            print(f"    Extracting text from {os.path.basename(pdf_path)}...")
            subprocess.run(["pdftotext", pdf_path, text_path], check=True)
            
        with open(text_path, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read()
    except Exception as e:
        print(f"    Failed to extract text from {pdf_path}: {e}")
        return ""

def generate_chapter_blocks(text_chunk, subject_id, chapter_id):
    prompt = f"""
    You are the Chief Academic Architect of Shine Academy Naroda.
    
    Convert the following textbook text for Class 10 {subject_id.capitalize()} into a fully interactive Shine Academy EduOS JSON chapter according to the NEW EduOS 8-Step Gold Pedagogy Standard v2.0.
    
    The 8-Step Cycle MUST be followed:
    1. hook
    2. socratic
    3. discovery
    4. theory (reveal)
    5. knowledge_check
    6. reflection
    7. connection
    8. mastery
    
    CRITICAL RULE:
    Every single block MUST have English, Hindi, AND Gujarati translations (e.g. title, title_hi, title_gu, body, body_hi, body_gu).
    
    Text chunk:
    {text_chunk}
    
    Expected JSON Output (Return ONLY a valid JSON array of blocks):
    [
      {{
        "id": "KOBJ_{subject_id.upper()}_{chapter_id}_HOOK",
        "type": "hook",
        "title": "...", "title_hi": "...", "title_gu": "...",
        "body": "...", "body_hi": "...", "body_gu": "..."
      }}
    ]
    """
    
    while True:
        try:
            print(f"    Generating JSON blocks via Gemini API...")
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
                print("    * Rate limit hit. Waiting 60 seconds...")
                time.sleep(60)
            else:
                print(f"    * JSON parse error: {e}. Retrying in 5s...")
                time.sleep(5)

def main():
    print("--- 🚀 Generating Complete Class 10 Curriculum OVERHAUL ---")
    
    for subject, pdf_dir in DIRECTORIES_TO_SCAN.items():
        print(f"\n=========================================")
        print(f"Scanning {subject.upper()} directory: {pdf_dir}")
        print(f"=========================================")
        
        # In maths and sanskrit, target 'tb' (textbook) or 'scich' for science to avoid processing raw MCQs/solution PDFs endlessly
        if subject == "science":
            search_pattern = "scich*.pdf"
        elif subject == "maths":
            search_pattern = "*tb.pdf"
        else:
            search_pattern = "*.pdf"
            
        pdf_files = glob.glob(os.path.join(pdf_dir, search_pattern))
        
        if not pdf_files:
            print(f"  No matching PDFs found for {subject}")
            continue
            
        print(f"  Found {len(pdf_files)} PDF files to process for {subject}.")
        
        for pdf_path in sorted(pdf_files):
            filename = os.path.basename(pdf_path)
            chapter_identifier = filename.replace(".pdf", "").upper()
            
            print(f"  -> Processing {filename}...")
            
            full_text = extract_text(pdf_path)
            if not full_text:
                continue
                
            full_text = full_text.replace('\f', '\n').strip()
            
            # Take a chunk of 4000 characters to process the main chapter concept
            chunk_size = 4000
            first_chunk = full_text[:chunk_size]
            
            blocks = generate_chapter_blocks(first_chunk, subject, chapter_identifier)
            
            chapter_json = {
                "metadata": {
                    "id": f"ncert_class10_{subject}_{chapter_identifier.lower()}",
                    "title": f"{subject.capitalize()} - {chapter_identifier}",
                    "subject": subject.capitalize(),
                    "grade": "10",
                    "curriculum": ["NCERT", "CBSE", "GSEB"],
                    "difficulty": "Intermediate",
                    "estimated_minutes": 45
                },
                "blocks": blocks
            }
            
            out_filename = f"ncert_class10_{subject}_{chapter_identifier.lower()}.json"
            out_filepath = os.path.join(OUTPUT_DIR, out_filename)
            
            with open(out_filepath, 'w', encoding='utf-8') as f:
                json.dump(chapter_json, f, ensure_ascii=False, indent=2)
                
            print(f"  ✅ Successfully saved {out_filename}!")
            time.sleep(5) # API safety
            
    print("\n🎉 MASTER SCRIPT COMPLETE! All dummy data has been replaced with Gold Standard files.")

if __name__ == "__main__":
    main()
