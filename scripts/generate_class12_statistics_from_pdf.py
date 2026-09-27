import os
import json
import time
import glob
import subprocess
import google.generativeai as genai

API_KEY = "AIzaSyCXHEJ4KBrebP8ByUEZnVJzuE4u114MGGA"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-3.5-flash-lite')

PDF_DIR = "/home/ubuntu/Shine_Academy_Naroda/SAN/Year2026/statisticspdf12thcommerce"
OUTPUT_DIR = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters"

def extract_text(pdf_path):
    text_path = pdf_path.replace(".pdf", ".txt")
    
    try:
        if not os.path.exists(text_path):
            print(f"  Extracting massive text from {os.path.basename(pdf_path)}...")
            subprocess.run(["pdftotext", pdf_path, text_path], check=True)
            
        with open(text_path, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read()
    except Exception as e:
        print(f"  Failed to extract text from {pdf_path}: {e}")
        return ""

def generate_statistics_blocks(text_chunk, part_identifier):
    prompt = f"""
    You are the Chief Academic Architect of Shine Academy Naroda.
    
    We are generating a Masterclass for Class 12 Statistics (CBSE / Applied Mathematics equivalent). 
    Statistics must be taught through Socratic discovery, not rote memorization of formulas.
    
    Read the following text chunk (extracted from a massive Statistics textbook PDF).
    
    Use the 8-Step Socratic Gold Pedagogy to generate an interactive lesson:
    1. A 'hook' block (Use a real-world scenario like sports, business, or weather to introduce the concept).
    2. A 'socratic' block asking the student a logical question leading to the formula.
    3. A 'theory' block revealing the Formula and Concept clearly.
    4. Multiple 'theory' blocks breaking down a Solved Example into Micro-Steps.
    5. A 'reflection' block explaining WHY the final statistical answer makes sense in the real world.
    
    CRITICAL RULE:
    Every single block MUST have English, Hindi, AND Gujarati translations for ALL text (title_hi, title_gu, body_hi, body_gu). Numbers can remain standard digits, but the surrounding text must be translated.
    
    Text chunk:
    {text_chunk}
    
    Expected JSON Output (Return ONLY a valid JSON array of blocks):
    [
      {{
        "id": "KOBJ_STAT12_{part_identifier}_HOOK",
        "type": "hook",
        "title": "Real World Scenario", "title_hi": "...", "title_gu": "...",
        "body": "...", "body_hi": "...", "body_gu": "..."
      }}
    ]
    """
    
    while True:
        try:
            print(f"  Generating Statistics JSON blocks via Gemini API...")
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
    print("--- 📊 Generating Class 12 Statistics Masterclass ---")
    
    pdf_files = glob.glob(os.path.join(PDF_DIR, "*.pdf"))
    
    if not pdf_files:
        print(f"Error: No PDFs found in {PDF_DIR}")
        return
        
    print(f"Found {len(pdf_files)} PDF files to process.")
    
    for pdf_path in sorted(pdf_files):
        filename = os.path.basename(pdf_path)
        
        # Determine if it's Part 1 or Part 2
        part_identifier = "PART1" if "Part-1" in filename else "PART2"
        
        print(f"\nProcessing {filename} ({part_identifier})...")
        
        full_text = extract_text(pdf_path)
        if not full_text:
            continue
            
        full_text = full_text.replace('\f', '\n').strip()
        
        # Take an initial chunk of 6000 characters to process the main chapter concept
        chunk_size = 6000
        first_chunk = full_text[:chunk_size]
        
        blocks = generate_statistics_blocks(first_chunk, part_identifier)
        
        chapter_json = {
            "metadata": {
                "id": f"ncert_class12_statistics_{part_identifier.lower()}",
                "title": f"Statistics - {part_identifier.capitalize()}",
                "subject": "Statistics",
                "grade": "12",
                "curriculum": ["CBSE", "NCERT"],
                "difficulty": "Advanced",
                "estimated_minutes": 60
            },
            "blocks": blocks
        }
        
        out_filename = f"ncert_class12_statistics_{part_identifier.lower()}.json"
        out_filepath = os.path.join(OUTPUT_DIR, out_filename)
        
        with open(out_filepath, 'w', encoding='utf-8') as f:
            json.dump(chapter_json, f, ensure_ascii=False, indent=2)
            
        print(f"  ✅ Successfully saved {out_filename}!")
        time.sleep(5) # API safety
        
    print("All Statistics chapters generated successfully!")

if __name__ == "__main__":
    main()
