import os
import json
import time
import google.generativeai as genai

API_KEY = "AIzaSyCXHEJ4KBrebP8ByUEZnVJzuE4u114MGGA"
genai.configure(api_key=API_KEY)
# Using flash-lite to avoid restrictive daily quotas on the standard flash model
model = genai.GenerativeModel('gemini-3.5-flash-lite')

CHAPTERS_DIR = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters"
TEXT_DIR = "/home/ubuntu/Shine_Academy_Naroda/SAN/shineboard_library/class_12/accounts"

def generate_chapter_blocks(chapter_id, chapter_title, chapter_text):
    prompt = f"""
    You are the Chief Academic Architect of Shine Academy Naroda.
    
    We need to generate a high-quality educational chapter for Class 12 Accounts (GSEB).
    The chapter title is: {chapter_title}
    
    Below is the ACTUAL TEXT of the chapter extracted from the textbook. You MUST read this text and generate your educational content strictly based on it.
    
    === CHAPTER TEXT BEGIN ===
    {chapter_text}
    === CHAPTER TEXT END ===
    
    Please generate a fully interactive Shine Academy EduOS JSON chapter according to the NEW EduOS 8-Step Gold Pedagogy Standard v2.0.
    
    You must generate AT LEAST 20 assessment blocks (MCQs, True/False, Theory, Flashcards) that cover the entire text.
    
    The 8-Step Cycle MUST be followed for the main concepts:
    1. hook
    2. socratic
    3. discovery
    4. theory (reveal)
    5. knowledge_check (must be type 'mcq' or 'true_false')
    6. reflection
    7. connection
    8. mastery
    
    ACCOUNTS-SPECIFIC INSTRUCTIONS:
    - Focus heavily on conceptual understanding, formulas, and rules of debit/credit.
    - Since large 10-mark balance sheet problems don't work well on mobile, break down numerical problems into smaller conceptual 'mcq' or 'flashcard' tests.
    - Ask students to identify which account is debited/credited for a specific transaction.
    - Ensure formulas (e.g., Goodwill valuation, Accounting Ratios) are clearly stated in 'theory' blocks.
    
    CRITICAL RULES:
    1. Every single block MUST have English, Hindi, AND Gujarati translations for ALL string fields (e.g. title, title_hi, title_gu, body, body_hi, body_gu, question, question_hi, question_gu, options, options_hi, options_gu, hint, hint_hi, hint_gu).
    2. The 'id' for each block must follow the format KOBJ_{chapter_id.upper()}_<NUM> (e.g., KOBJ_GSEB_CLASS12_ACCOUNTS_CH1_01).
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
    1: "Chapter 1: Introduction to Partnership",
    2: "Chapter 2: Final Accounts (Financial Statements)",
    3: "Chapter 3: Valuation of Goodwill",
    4: "Chapter 4: Reconstruction of Partnership",
    5: "Chapter 5: Admission of a Partner",
    6: "Chapter 6: Retirement / Death of a Partner",
    7: "Chapter 7: Dissolution of Partnership Firm",
    8: "Chapter 8: Accounting for Share Capital",
    9: "Chapter 9: Accounting for Debentures",
    10: "Chapter 10: Company Final Accounts",
    11: "Chapter 11: Analysis of Financial Statements",
    12: "Chapter 12: Accounting Ratios and Analysis",
    13: "Chapter 13: Cash Flow Statement"
}

def main():
    print("--- Generating Class 12 Accounts Chapters from Text Files ---")
    
    for i in range(1, 14):
        chapter_identifier = f"gseb_class12_accounts_ch{i}"
        filename = f"{chapter_identifier}.json"
        filepath = os.path.join(CHAPTERS_DIR, filename)
        text_filepath = os.path.join(TEXT_DIR, f"textbook_gseb_class12_accounts_ch{i}.txt")
        
        title = titles.get(i, f"Chapter {i}")
        print(f"\nProcessing {filename} (Title: {title})...")
        
        try:
            with open(text_filepath, 'r', encoding='utf-8') as f:
                chapter_text = f.read()
        except Exception as e:
            print(f"  Could not read {text_filepath}: {e}")
            continue
            
        new_blocks = generate_chapter_blocks(chapter_identifier, title, chapter_text)
        
        chapter_data = {
            "metadata": {
                "id": chapter_identifier,
                "title": title,
                "subject": "Accounts",
                "grade": "12"
            },
            "blocks": new_blocks
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(chapter_data, f, indent=2, ensure_ascii=False)
            
        print(f"  Successfully wrote {len(new_blocks)} blocks to {filename}")
        time.sleep(2)

if __name__ == "__main__":
    main()
