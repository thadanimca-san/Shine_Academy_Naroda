import os
import json
import time
import subprocess
import glob
import google.generativeai as genai

# Setup Gemini API
API_KEY = "AIzaSyCXHEJ4KBrebP8ByUEZnVJzuE4u114MGGA"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-3.6-flash')

CHAPTERS_DIR = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters"
SAN_DIR = "/home/ubuntu/Shine_Academy_Naroda/SAN/Year2026"

# A basic map to try and find a relevant PDF based on subject
SUBJECT_PDF_MAP = {
    "Statistics": "statisticspdf12thcommerce",
    "Economics": "ecopdf12commerce",
    "Accountancy": "accountpdf12thcommerce",
    "English": "engpdf12thcommerce",
    "OC": "bspdf12commerce", # OC / Management -> Business Studies
    "Organization of Commerce": "bspdf12commerce",
    "Business Studies": "bspdf12commerce"
}

def extract_text(pdf_path):
    text_path = pdf_path.replace(".pdf", ".txt")
    try:
        if not os.path.exists(text_path):
            subprocess.run(["pdftotext", pdf_path, text_path], check=True)
        with open(text_path, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read()
    except Exception as e:
        return ""

def generate_socratic_blocks(title, subject, pdf_context):
    prompt = f"""
    You are the Chief Academic Architect of Shine Academy Naroda.
    
    We are generating an interactive Masterclass for Class 12. 
    Subject: {subject}
    Topic/Chapter: {title}
    
    Use the 8-Step Socratic Gold Pedagogy to generate an interactive lesson for this topic:
    1. 'hook' block (Use a real-world scenario to introduce the concept).
    2. 'socratic' block asking the student a logical question leading to the concept.
    3. 'theory' block revealing the Concept clearly.
    4. 'worked_example' or 'theory' block breaking down a Solved Example or Case Study into Micro-Steps.
    5. 'reflection' block explaining WHY the final answer/concept makes sense in the real world.
    6. 'mcq' block (A Knowledge Check - provide correct_index and explanation).
    
    CRITICAL RULE:
    Every single block MUST have English, Hindi, AND Gujarati translations for ALL text fields.
    For example, a theory block must have:
    "title", "title_hi", "title_gu"
    "body", "body_hi", "body_gu"
    
    For mcq blocks:
    "question", "question_hi", "question_gu"
    "options": ["A", "B", "C", "D"], "options_hi": ["...", ...], "options_gu": ["...", ...]
    "explanation", "explanation_hi", "explanation_gu"
    "correct_index": 0
    
    Here is some extracted text from the syllabus/textbook to guide you (if available):
    {pdf_context[:5000]}
    
    If no text is provided, use your expert knowledge of the standard CBSE/GSEB Class 12 {subject} curriculum to generate the content for '{title}'.
    
    Expected JSON Output (Return ONLY a valid JSON array of blocks, no markdown formatting outside of JSON):
    """
    
    for attempt in range(3):
        try:
            response = model.generate_content(prompt)
            res_text = response.text.strip()
            if res_text.startswith("```json"):
                res_text = res_text[7:-3].strip()
            elif res_text.startswith("```"):
                res_text = res_text[3:-3].strip()
                
            data = json.loads(res_text)
            
            # Basic validation
            if not isinstance(data, list) or len(data) == 0:
                raise ValueError("Did not return a JSON array of blocks")
                
            return data
            
        except Exception as e:
            print(f"  * Exception: {e}. Retrying in 10s...")
            time.sleep(10)
    return []

def main():
    print("--- 🚀 Mass Generating Class 12 Commerce Empty Chapters ---")
    
    empty_files = []
    for fname in os.listdir(CHAPTERS_DIR):
        if not fname.endswith('.json'):
            continue
        if 'class12' not in fname:
            continue
            
        fpath = os.path.join(CHAPTERS_DIR, fname)
        try:
            with open(fpath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            blocks = data.get('blocks', []) if isinstance(data, dict) else data
            if len(blocks) == 0:
                empty_files.append((fname, fpath, data))
        except:
            pass
            
    print(f"Found {len(empty_files)} empty Class 12 chapters to process.")
    
    for fname, fpath, data in sorted(empty_files):
        print(f"\nProcessing {fname}...")
        
        # Extract metadata
        meta = data.get('metadata', {})
        title = meta.get('title', fname.replace('.json', ''))
        subject = meta.get('subject', 'Commerce')
        
        # Try to find a relevant PDF folder
        pdf_folder_name = None
        for key, val in SUBJECT_PDF_MAP.items():
            if key.lower() in subject.lower() or key.lower() in fname.lower():
                pdf_folder_name = val
                break
                
        pdf_context = ""
        if pdf_folder_name:
            pdf_dir = os.path.join(SAN_DIR, pdf_folder_name)
            if os.path.exists(pdf_dir):
                # Just grab the first PDF we find in this directory for context
                pdfs = glob.glob(os.path.join(pdf_dir, "*.pdf"))
                if pdfs:
                    pdf_context = extract_text(pdfs[0])
                    if pdf_context:
                        print(f"  -> Extracted {len(pdf_context)} chars from {os.path.basename(pdfs[0])} for context.")
        
        if not pdf_context:
            print(f"  -> No specific PDF context found. Using Gemini's base knowledge for {title}.")
            
        # Generate blocks
        blocks = generate_socratic_blocks(title, subject, pdf_context)
        
        if blocks:
            # Ensure every block has an ID
            for i, b in enumerate(blocks):
                if 'id' not in b:
                    b['id'] = f"KOBJ_{fname.replace('.json', '').upper()}_{i+1:02d}"
                    
            if isinstance(data, dict):
                data['blocks'] = blocks
                # Ensure is_available is true
                if 'is_available' in data:
                    data['is_available'] = True
            else:
                # If the root is a list, we just save the blocks list, but chapters should be dicts with metadata
                # Let's rebuild it properly
                data = {
                    "metadata": meta,
                    "blocks": blocks
                }
                
            with open(fpath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"  ✅ Successfully generated and saved {len(blocks)} blocks!")
        else:
            print(f"  ❌ Failed to generate blocks for {fname}.")
            
        # Sleep to avoid rate limits
        time.sleep(5)

if __name__ == "__main__":
    main()
