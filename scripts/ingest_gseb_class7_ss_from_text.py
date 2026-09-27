import os
import json
import time
import google.generativeai as genai

API_KEY = "AIzaSyCXHEJ4KBrebP8ByUEZnVJzuE4u114MGGA"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-3.5-flash-lite')

CHAPTERS_DIR = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters"
TEXT_DIR = "/home/ubuntu/Shine_Academy_Naroda/SAN/shineboard_library/class_7/ss"

def generate_chapter_blocks(chapter_id, chapter_title, chapter_text):
    prompt = f"""
    You are the Chief Academic Architect of Shine Academy Naroda.
    
    We need to generate a high-quality educational chapter for Class 7 Social Science (GSEB).
    The chapter title is: {chapter_title}
    
    Below is the ACTUAL TEXT of the chapter. You MUST read this text and generate your educational content strictly based on it.
    
    === CHAPTER TEXT BEGIN ===
    {chapter_text}
    === CHAPTER TEXT END ===
    
    Please generate a fully interactive Shine Academy EduOS JSON chapter according to the NEW EduOS 8-Step Gold Pedagogy Standard v2.0.
    
    You must generate AT LEAST 15 assessment questions (MCQs, True/False, Flashcards) that cover the entire text. Do NOT just generate 2-3 questions. 
    
    The 8-Step Cycle MUST be followed for the main concepts:
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
    3. Put ALL fields at the root level of the block object. DO NOT USE a 'content' wrapper. (e.g. {{"type":"theory","body":"..."}})
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
                print(f"  * Rate limit hit: {e}. Waiting 60 seconds...")
                time.sleep(60)
            else:
                print(f"  * JSON parse error: {e}. Retrying in 5s...")
                time.sleep(5)

titles = {
    1: "Chapter 1: Rajput Age : New Ruler and States",
    2: "Chapter 2: The Delhi Sultanate",
    3: "Chapter 3: Mughal Empire",
    4: "Chapter 4: Medieval Architecture, Cities, Merchants and Craftsman",
    5: "Chapter 5: Adivasis",
    6: "Chapter 6: Nomadic and Denotified Tribes",
    7: "Chapter 7: Bhakti Age : Religious Sects and Saints",
    8: "Chapter 8: Formation of Regional Culture",
    9: "Chapter 9: Political Rulers of 18th Century",
    10: "Chapter 10: Earth's Internal Composition and Landforms",
    11: "Chapter 11: Components of the Environment and Interrelationships",
    12: "Chapter 12: Effects of Atmosphere on Living Beings",
    13: "Chapter 13: Disaster Management",
    14: "Chapter 14: Conservation and Preservation of Resources",
    15: "Chapter 15: Equality in Democracy",
    16: "Chapter 16: State Government",
    17: "Chapter 17: Gender Discrimination",
    18: "Chapter 18: Means of Communication and Advertisement",
    19: "Chapter 19: Markets",
    20: "Let's test the understanding"
}

def main():
    print("--- Generating Class 7 Social Science Chapters from Text Files ---")
    
    for i in range(13, 21):
        chapter_identifier = f"gseb_class7_social_science_ch{i}"
        filename = f"{chapter_identifier}.json"
        filepath = os.path.join(CHAPTERS_DIR, filename)
        text_filepath = os.path.join(TEXT_DIR, f"textbook_gseb_ch{i}.txt")
        
        # We want to OVERWRITE the hallucinated ones, so we do not skip based on existence
        
        title = titles.get(i, f"Chapter {i}")
        print(f"\nProcessing {filename} (Title: {title})...")
        
        try:
            with open(text_filepath, 'r', encoding='utf-8') as f:
                chapter_text = f.read()
        except Exception as e:
            print(f"  Could not read {text_filepath}: {e}")
            continue
            
        new_blocks = generate_chapter_blocks(chapter_identifier, title, chapter_text)
        
        # Reconstruct standard format
        chapter_data = {
            "metadata": {
                "id": chapter_identifier,
                "title": title,
                "subject": "Social Science",
                "grade": "7"
            },
            "blocks": new_blocks
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(chapter_data, f, indent=2, ensure_ascii=False)
            
        print(f"  Successfully wrote {len(new_blocks)} blocks to {filename}")
        # Sleep briefly to avoid aggressive rate limiting
        time.sleep(2)

if __name__ == "__main__":
    main()
