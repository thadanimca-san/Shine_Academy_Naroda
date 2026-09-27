import os
import json
import time
import subprocess
import google.generativeai as genai

API_KEY = "AIzaSyCXHEJ4KBrebP8ByUEZnVJzuE4u114MGGA"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-3.5-flash-lite')

PDF_FILE = "/home/ubuntu/Shine_Academy_Naroda/SAN/Year2026/vedikmathspdf/vedic_maths-1.pdf"
OUTPUT_DIR = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters"

SYSTEM_PROMPT = """
You are a master Vedic Maths Teacher for Shine Academy.
We are extracting a Vedic Maths textbook into Socratic JSON chapters.

CRITICAL RULES:
1. You MUST STRICTLY follow the CHAPTER_STANDARD.yaml.
2. Every block MUST have fields at the ROOT level. DO NOT wrap data in a "content": {} object.
3. Every string MUST be translated into Hindi and Gujarati (e.g., body, body_hi, body_gu).
4. Follow the 8-Step Socratic Gold Pedagogy (Hook -> Socratic Question -> Discovery -> Reveal -> Knowledge Check -> Mastery).
5. Explain the Sutras clearly with step-by-step worked examples.
"""

def extract_text_from_pdf(pdf_path):
    print(f"Extracting text from {pdf_path}...")
    try:
        result = subprocess.run(['pdftotext', pdf_path, '-'], capture_output=True, text=True, check=True)
        return result.stdout
    except FileNotFoundError:
        print("Error: pdftotext is not installed. Please install poppler-utils.")
        return ""
    except subprocess.CalledProcessError as e:
        print(f"Error during extraction: {e}")
        return ""

def generate_chapter(ch_num, chapter_text):
    filepath = os.path.join(OUTPUT_DIR, f"vedic_maths_level1_ch{ch_num}.json")
    if os.path.exists(filepath):
        print(f"Skipping Vedic Maths Chapter {ch_num} (already generated).")
        return

    prompt = f"""
    Here is a section from the Vedic Maths textbook (Chapter {ch_num}):
    
    {chapter_text[:6000]} # Limit to avoid token overflow
    
    Generate a JSON chapter for this section. Focus on the mathematical Sutra being taught.
    """
    print(f"Generating Vedic Maths Chapter {ch_num} via Gemini API...")
    try:
        response = model.generate_content(
            contents=[{"role": "user", "parts": [SYSTEM_PROMPT + "\n\n" + prompt]}],
            generation_config=genai.types.GenerationConfig(
                temperature=0.7,
                response_mime_type="application/json"
            )
        )
        json_str = response.text.strip()
        data = json.loads(json_str)
        
        filepath = os.path.join(OUTPUT_DIR, f"vedic_maths_level1_ch{ch_num}.json")
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Saved: {filepath}")
        
    except Exception as e:
        print(f"Failed to generate Chapter {ch_num}: {e}")

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    full_text = extract_text_from_pdf(PDF_FILE)
    
    if not full_text:
        print("Could not extract text. Aborting.")
        return
        
    # Simple chunking for demonstration (roughly 5000 characters per chapter)
    chunk_size = 5000
    chunks = [full_text[i:i+chunk_size] for i in range(0, len(full_text), chunk_size)]
    
    # Process up to 5 chapters for this demo
    max_chapters = min(5, len(chunks))
    
    for i in range(max_chapters):
        generate_chapter(i+1, chunks[i])
        time.sleep(2)
        
    print("Vedic Maths curriculum generation complete!")

if __name__ == "__main__":
    main()
