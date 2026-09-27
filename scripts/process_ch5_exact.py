import os
import json
import time
import re
import google.generativeai as genai

API_KEY = "AIzaSyCXHEJ4KBrebP8ByUEZnVJzuE4u114MGGA"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-pro')

CHAPTER_ID = "GSEB_CLASS12_ACCOUNTS_CH5"
OUT_FILE = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class12_accounts_ch5.json"
IN_FILE = "/home/ubuntu/Shine_Academy_Naroda/SAN/shineboard_library/class_12/accounts/textbook_gseb_class12_accounts_ch5.txt"

def call_gemini(prompt, retries=3):
    for attempt in range(retries):
        try:
            print(f"Calling Gemini API (Attempt {attempt+1})...")
            response = model.generate_content(prompt)
            text = response.text.strip()
            if "```json" in text:
                text = text.split("```json")[1].split("```")[0].strip()
            elif "```" in text:
                text = text.split("```")[1].strip()
            return json.loads(text)
        except Exception as e:
            print(f"Error: {e}")
            if "429" in str(e) or "Quota" in str(e):
                time.sleep(30)
            else:
                time.sleep(5)
    return []

def process_theory_chunk(chunk_text, chunk_index):
    prompt = f"""
You are the Chief Academic Architect of Shine Academy Naroda. 
Process the following THEORY section of Class 12 Accounts Chapter 5 (Admission of a Partner).

Apply the EduOS 8-Step Socratic Discovery Arc for theory concepts: hook -> socratic -> discovery -> theory (reveal) -> knowledge_check (mcq/true_false) -> reflection -> connection -> mastery.
Every block MUST have full Hindi and Gujarati translations (`title_hi`, `title_gu`, `body_hi`, `body_gu`, `question_hi`, `question_gu`, `options_hi`, `options_gu`, etc.).
Structure the JSON correctly: NO `content` wrapper. Use root-level properties. Assign a unique `id` to EVERY block. Use integer `correct_index` for MCQs.

TEXT CHUNK (Part {chunk_index}):
{chunk_text}

Output ONLY a JSON array of block objects. No markdown formatting outside the JSON array.
"""
    return call_gemini(prompt)

def process_exercise_chunk(chunk_text, chunk_index):
    prompt = f"""
You are the Chief Academic Architect of Shine Academy Naroda. 
Process the following EXERCISE section of Class 12 Accounts Chapter 5.

You MUST include EVERY SINGLE EXERCISE QUESTION (MCQs, Short Answer, Long Answer, Numerical/Accounting Problems). Use markdown tables in the `body` or `question` if there are Trial Balances or P&L accounts. NO SHORTCUTS. Format them as 'mcq', 'practice_question', or 'worked_example'.
Every block MUST have full Hindi and Gujarati translations.
Structure the JSON correctly: NO `content` wrapper. Root-level properties. Unique `id`. Integer `correct_index` for MCQs.

EXERCISE TEXT CHUNK (Part {chunk_index}):
{chunk_text}

Output ONLY a JSON array of block objects. No markdown formatting outside the JSON array.
"""
    return call_gemini(prompt)

def main():
    if not os.path.exists(IN_FILE):
        print(f"File not found: {IN_FILE}")
        return

    with open(IN_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Find where EXERCISE starts
    exercise_start_idx = len(lines)
    for i, line in enumerate(lines):
        if line.strip() == "EXERCISE":
            exercise_start_idx = i
            break

    theory_lines = lines[:exercise_start_idx]
    exercise_lines = lines[exercise_start_idx:]

    all_blocks = []
    
    # Process Theory in chunks of 500 lines
    chunk_size = 500
    for i in range(0, len(theory_lines), chunk_size):
        chunk = "".join(theory_lines[i:i+chunk_size])
        print(f"Processing Theory Chunk {i//chunk_size + 1}")
        blocks = process_theory_chunk(chunk, i//chunk_size + 1)
        all_blocks.extend(blocks)
        
    # Process Exercises in chunks of 100 lines to ensure no missed questions
    ex_chunk_size = 100
    for i in range(0, len(exercise_lines), ex_chunk_size):
        chunk = "".join(exercise_lines[i:i+ex_chunk_size])
        print(f"Processing Exercise Chunk {i//ex_chunk_size + 1}")
        blocks = process_exercise_chunk(chunk, i//ex_chunk_size + 1)
        all_blocks.extend(blocks)

    # Fix IDs and validate
    for idx, block in enumerate(all_blocks):
        block["id"] = f"KOBJ_{CHAPTER_ID}_{idx+1:03d}"

    chapter_data = {
        "metadata": {
            "id": CHAPTER_ID.lower(),
            "title": "Chapter 5: Admission of a Partner",
            "subject": "Accounts",
            "grade": "12",
            "language": "en, hi, gu"
        },
        "blocks": all_blocks
    }

    os.makedirs(os.path.dirname(OUT_FILE), exist_ok=True)
    with open(OUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(chapter_data, f, indent=2, ensure_ascii=False)

    print(f"Successfully processed chapter. Total blocks: {len(all_blocks)}. Saved to {OUT_FILE}")

if __name__ == "__main__":
    main()
