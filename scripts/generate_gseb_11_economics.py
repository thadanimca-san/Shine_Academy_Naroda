import os
import json
import time
import subprocess
import google.generativeai as genai

API_KEY = "AIzaSyCXHEJ4KBrebP8ByUEZnVJzuE4u114MGGA"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-3.6-flash')

OUTPUT_DIR = "/home/ubuntu/Shine_Academy_Naroda/SAN/Year2026/GSEB/11economics"
LIBRARY_DIR = "/home/ubuntu/Shine_Academy_Naroda/SAN/shineboard_library/class_11/economics"

# Standard map of GSEB 11 Economics chapters (approximate titles if exact is unknown)
CHAPTER_TITLES = {
    1: "Economics: An Introduction",
    2: "Fundamental Concepts and Terminologies",
    3: "Demand",
    4: "Supply",
    5: "Cost of Production and Concepts of Revenue",
    6: "Market",
    7: "Indian Economy",
    8: "Economic Reforms",
    9: "National Income",
    10: "Budget",
    11: "Emerging Issues in Indian Economy",
    12: "Economic Environment" # Wait, there's a guide_ch12.pdf in the directory
}

def extract_pdf_text(filepath):
    try:
        result = subprocess.run(['pdftotext', '-q', filepath, '-'], capture_output=True, text=True, timeout=30)
        return result.stdout.strip()
    except Exception as e:
        print(f"Error extracting PDF: {e}")
        return ""

def generate_chapter_blocks(chapter_num, chapter_title, context_text):
    prompt = f"""
    You are the Chief Academic Architect of Shine Academy Naroda.
    
    We need to generate a high-quality educational chapter for GSEB Class 11 Economics.
    The chapter is: Chapter {chapter_num}: {chapter_title}
    
    --- TEXTBOOK / GUIDE TEXT EXTRACTED ---
    {context_text}
    ---------------------------------------
    
    Please use your extensive knowledge and strictly adhere to the provided TEXTBOOK / GUIDE TEXT to generate a fully interactive Shine Academy EduOS JSON chapter according to the NEW EduOS 8-Step Gold Pedagogy Standard v2.0.
    
    CRITICAL INSTRUCTION:
    THIS IS NOT A SMALL PROJECT. EVERY SINGLE EXERCISE QUESTION FROM THE GUIDE FOR THIS CHAPTER MUST BE INCLUDED AT THE END OF THE CHAPTER AS MCQ OR TRUE/FALSE. NO SHORTCUTS. NO LAZY SUMMARIES.

    The 8-Step Cycle MUST be followed for the theory part:
    1. hook
    2. socratic_question (must use 'socratic_question' type)
    3. discovery
    4. theory (reveal)
    5. knowledge_check (must be type 'mcq' or 'true_false')
    6. reflection
    7. connection
    8. mastery
    
    After the theory part, include ALL textbook exercise questions found in the extracted text.
    
    CRITICAL RULES:
    1. Every single block MUST have English, Hindi, AND Gujarati translations for ALL string fields (e.g. title, title_hi, title_gu, body, body_hi, body_gu, question, question_hi, question_gu, options, options_hi, options_gu, explanation, explanation_hi, explanation_gu).
    2. The 'id' for each block must follow the format KOBJ_GSEB_C11_ECO_CH{chapter_num}_<NUM>.
    3. Put ALL fields at the root level of the block object. DO NOT USE a 'content' wrapper. (e.g. {{"type":"theory","body":"..."}})
    4. For knowledge checks and MCQs, use integer 'correct_index' (e.g., 0, 1, 2, 3), NOT 'correct_answer'.
    
    Expected JSON Output (Return ONLY a valid JSON array of blocks, nothing else. Do not wrap in ```json):
    [
      {{
        "id": "KOBJ_GSEB_C11_ECO_CH{chapter_num}_001",
        "type": "hook",
        "title": "...", "title_hi": "...", "title_gu": "...",
        "body": "...", "body_hi": "...", "body_gu": "..."
      }},
      ...
    ]
    """
    
    while True:
        try:
            print(f"  Generating JSON blocks for '{chapter_title}' via Gemini API...")
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
                print(f"  * JSON parse error: {e}. Retrying in 10s...")
                time.sleep(10)

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    for chapter_num in range(1, 13):
        pdf_path = os.path.join(LIBRARY_DIR, f"guide_ch{chapter_num}.pdf")
        if not os.path.exists(pdf_path):
            print(f"Skipping chapter {chapter_num}: {pdf_path} not found.")
            continue
            
        title = CHAPTER_TITLES.get(chapter_num, f"Chapter {chapter_num}")
        filename = f"gseb_class11_economics_ch{chapter_num}.json"
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        if os.path.exists(filepath):
            print(f"Skipping {filename} - already exists.")
            continue
            
        print(f"\nProcessing Chapter {chapter_num}: {title}...")
        text = extract_pdf_text(pdf_path)
        if not text:
            print(f"  * Failed to extract text from {pdf_path}")
            continue
            
        print(f"  * Extracted {len(text)} characters of context.")
        blocks = generate_chapter_blocks(chapter_num, title, text)
        
        chapter_data = {
            "metadata": {
                "id": f"gseb_class11_economics_ch{chapter_num}",
                "title": f"Chapter {chapter_num}: {title}",
                "subject": "Economics",
                "grade": "11",
                "board": "GSEB"
            },
            "blocks": blocks
        }
            
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(chapter_data, f, ensure_ascii=False, indent=2)
            
        print(f"Successfully saved {filename}!")
        time.sleep(10)

if __name__ == "__main__":
    main()
