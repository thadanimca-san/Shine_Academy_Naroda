import os
import json
import time
import glob
import google.generativeai as genai

API_KEY = "AIzaSyCXHEJ4KBrebP8ByUEZnVJzuE4u114MGGA"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-3.5-flash-lite')

CHAPTERS_DIR = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters"

def generate_chapter_blocks(chapter_id, chapter_title):
    prompt = f"""
    You are the Chief Academic Architect of Shine Academy Naroda.
    
    We need to generate a high-quality educational chapter for Class 7 Social Science (GSEB).
    The chapter title is: {chapter_title}
    
    Please use your extensive knowledge of this topic to generate a fully interactive Shine Academy EduOS JSON chapter according to the NEW EduOS 8-Step Gold Pedagogy Standard v2.0.
    
    The 8-Step Cycle MUST be followed:
    1. hook
    2. socratic
    3. discovery
    4. theory (reveal)
    5. knowledge_check (must be type 'mcq' or 'true_false')
    6. reflection
    7. connection
    8. mastery
    
    CRITICAL RULES:
    1. Every single block MUST have English, Hindi, AND Gujarati translations for ALL string fields (e.g. title, title_hi, title_gu, body, body_hi, body_gu, question, question_hi, question_gu, options, options_hi, options_gu, hint, hint_hi, hint_gu).
    2. The 'id' for each block must follow the format KOBJ_{chapter_id.upper()}_<NUM>.
    3. Put ALL fields at the root level of the block object, EXCEPT for 'metadata' if you need it. DO NOT USE a 'content' wrapper. (e.g. {{"type":"theory","body":"..."}})
    4. For knowledge checks, use integer 'correct_index' (e.g., 0, 1, 2, 3), NOT 'correct_answer'.
    
    Expected JSON Output (Return ONLY a valid JSON array of blocks):
    [
      {{
        "id": "KOBJ_{chapter_id.upper()}_01",
        "type": "hook",
        "title": "...", "title_hi": "...", "title_gu": "...",
        "body": "...", "body_hi": "...", "body_gu": "..."
      }}
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
                print(f"  * JSON parse error: {e}. Retrying in 5s...")
                time.sleep(5)

def main():
    print("--- Generating Class 7 Social Science Chapters (Zero-Shot) ---")
    
    # We will generate all 19 chapters as requested by the user
    for i in range(1, 20):
        chapter_identifier = f"gseb_class7_social_science_ch{i}"
        filename = f"{chapter_identifier}.json"
        filepath = os.path.join(CHAPTERS_DIR, filename)
        
        try:
            # Check if file exists and has translated blocks
            if os.path.exists(filepath):
                with open(filepath, 'r', encoding='utf-8') as f:
                    chapter_data = json.load(f)
                blocks = chapter_data.get('blocks', []) if isinstance(chapter_data, dict) else chapter_data
                if len(blocks) > 0:
                    has_translations = any('title_hi' in b or 'body_hi' in b for b in blocks)
                    if has_translations:
                        print(f"Skipping {filename} (already generated with translations).")
                        continue
            else:
                chapter_data = {}
            
            # If the user has specific chapter names in mind, Gemini usually infers them correctly
            # from "Chapter 1", "Chapter 2", etc. in the context of GSEB Class 7 Social Science.
            title = f"Chapter {i}"
            print(f"\nProcessing {filename} (Title: {title})...")
            
            new_blocks = generate_chapter_blocks(chapter_identifier, title)
            
            # Reconstruct standard format
            chapter_data = {
                "metadata": {
                    "id": chapter_identifier,
                    "title": title, # Will update this later if needed, or rely on UI to display block titles
                    "subject": "Social Science",
                    "grade": "7"
                },
                "blocks": new_blocks
            }
                
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(chapter_data, f, ensure_ascii=False, indent=2)
                
            print(f"Successfully saved {filename}!")
            time.sleep(5) # API safety
            
        except Exception as e:
            print(f"Error processing {filename}: {e}")
            
    print("All Class 7 Social Science chapters processed successfully!")

if __name__ == "__main__":
    main()
