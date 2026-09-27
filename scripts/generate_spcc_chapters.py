import os
import json
import time
import google.generativeai as genai

# Setup Gemini API
API_KEY = "AIzaSyCXHEJ4KBrebP8ByUEZnVJzuE4u114MGGA"
genai.configure(api_key=API_KEY)
# Try using gemini-1.5-flash which is widely known to handle large contexts well
model = genai.GenerativeModel('gemini-3.6-flash')

MODULES_DIR = "/home/ubuntu/Shine_Academy_Naroda/app_core/learning_modules"
SPCC_TEXT_FILE = "/home/ubuntu/Shine_Academy_Naroda/SAN/shineboard_library/class_12/spcc/Std-12 Commercial Cooresponda...Secretarial Practice E.M..txt"

def get_spcc_text():
    with open(SPCC_TEXT_FILE, 'r', encoding='utf-8', errors='ignore') as f:
        return f.read()

CHAPTERS = [
  {"id": "gseb_class12_spcc_ch2", "title": "Chapter 2: Correspondence with Government Departments"},
  {"id": "gseb_class12_spcc_ch3", "title": "Chapter 3: Inter Departmental and Employee Related Correspondence"},
  {"id": "gseb_class12_spcc_ch4", "title": "Chapter 4: Insurance Letters"},
  {"id": "gseb_class12_spcc_ch5", "title": "Chapter 5: E-Communication"},
  {"id": "gseb_class12_spcc_ch6", "title": "Chapter 6: Presentation Skills"},
  {"id": "gseb_class12_spcc_ch7", "title": "Chapter 7: Issue of Shares"},
  {"id": "gseb_class12_spcc_ch8", "title": "Chapter 8: Transfer and Transmission of Share"},
  {"id": "gseb_class12_spcc_ch9", "title": "Chapter 9: Debenture"},
  {"id": "gseb_class12_spcc_ch10", "title": "Chapter 10: Membership"},
  {"id": "gseb_class12_spcc_ch11", "title": "Chapter 11: Directors of a Company"},
  {"id": "gseb_class12_spcc_ch12", "title": "Chapter 12: The Meetings of the Company"},
  {"id": "gseb_class12_spcc_ch13", "title": "Chapter 13: Dissolution of a Company"}
]

def generate_chapter(ch_id, title, full_text):
    prompt = f"""
    You are the Chief Academic Architect of Shine Academy Naroda.
    
    We are generating an interactive Masterclass for Class 12. 
    Subject: SPCC (Commercial Correspondence and Secretarial Practice)
    Topic/Chapter: {title}
    
    Use the 8-Step Socratic Gold Pedagogy to generate an interactive lesson for this topic:
    1. 'hook' block (Use a real-world scenario to introduce the concept).
    2. 'socratic' block asking the student a logical question leading to the concept.
    3. 'theory' block revealing the Concept clearly.
    4. 'worked_example' or 'real_world_example' block (e.g. sample letter or process).
    5. 'reflection' block explaining WHY the final answer/concept makes sense.
    6. 'mcq' block (A Knowledge Check - provide correct_index and explanation).
    
    CRITICAL RULES:
    1. Every single block MUST have English, Hindi, AND Gujarati translations for ALL text fields.
       - theory: "title", "title_hi", "title_gu", "body", "body_hi", "body_gu"
       - mcq/true_false: "question", "question_hi", "question_gu", "options": [], "options_hi": [], "options_gu": [], "explanation", "explanation_hi", "explanation_gu", "correct_index"
    2. Incorporate exercise questions for this specific chapter.
    3. Return ONLY a valid JSON array of blocks. Do not add markdown like ```json.
    
    Here is the ENTIRE textbook text. You must ONLY search for and focus on the section corresponding to '{title}'. Ignore the rest.
    
    TEXTBOOK:
    {full_text[:50000]} # Just passing the first 50000 chars for now, will adjust if needed.
    """
    
    for attempt in range(3):
        try:
            print(f"Generating {title} (Attempt {attempt+1})")
            response = model.generate_content(prompt)
            res_text = response.text.strip()
            if res_text.startswith("```json"):
                res_text = res_text[7:-3].strip()
            elif res_text.startswith("```"):
                res_text = res_text[3:-3].strip()
                
            data = json.loads(res_text)
            if not isinstance(data, list) or len(data) == 0:
                raise ValueError("Did not return a JSON array of blocks")
                
            # Assign IDs
            for i, b in enumerate(data):
                b['id'] = f"{ch_id.upper()}_{i+1:02d}"
                
            return data
            
        except Exception as e:
            print(f"  * Exception: {e}. Retrying in 10s...")
            time.sleep(10)
    return []

def main():
    print("--- 🚀 Generating SPCC Chapters 2-13 ---")
    
    full_text = get_spcc_text()
    
    for ch in CHAPTERS:
        ch_id = ch['id']
        title = ch['title']
        ch_dir = os.path.join(MODULES_DIR, ch_id)
        blocks_file = os.path.join(ch_dir, 'blocks.json')
        
        if os.path.exists(blocks_file):
            print(f"Skipping {ch_id} - already exists.")
            continue
            
        print(f"\nProcessing {ch_id} - {title}...")
        blocks = generate_chapter(ch_id, title, full_text)
        
        if blocks:
            os.makedirs(ch_dir, exist_ok=True)
            with open(blocks_file, 'w', encoding='utf-8') as f:
                json.dump(blocks, f, ensure_ascii=False, indent=2)
            print(f"  ✅ Successfully generated and saved {len(blocks)} blocks!")
        else:
            print(f"  ❌ Failed to generate blocks for {ch_id}.")
            
        time.sleep(5)

if __name__ == "__main__":
    main()
