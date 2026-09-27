import os
import json
import time
import google.generativeai as genai

API_KEY = "AIzaSyCXHEJ4KBrebP8ByUEZnVJzuE4u114MGGA"
genai.configure(api_key=API_KEY)
# Using gemini-1.5-flash for large context and fast generation, or pro for deep instruction following.
model = genai.GenerativeModel('gemini-1.5-flash')

TEXT_FILE = "/home/ubuntu/Shine_Academy_Naroda/SAN/shineboard_library/class_12/accounts/textbook_gseb_class12_accounts_ch7.txt"
OUTPUT_FILE = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class12_accounts_ch7.json"
CHAPTER_ID = "GSEB_CLASS12_ACCOUNTS_CH7"

def call_gemini(prompt, retries=3):
    for i in range(retries):
        try:
            print("  Calling Gemini API...")
            response = model.generate_content(prompt)
            res_text = response.text.strip()
            if res_text.startswith("```json"):
                res_text = res_text[7:-3].strip()
            elif res_text.startswith("```"):
                res_text = res_text[3:-3].strip()
            return json.loads(res_text)
        except Exception as e:
            print(f"  * Error: {e}. Retrying in 10s...")
            time.sleep(10)
    return []

def main():
    print("Reading text file...")
    with open(TEXT_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Split into theory and exercises (Exercise starts around line 3697)
    exercise_index = 0
    for i, line in enumerate(lines):
        if "EXERCISE" in line.upper():
            exercise_index = i
            break
            
    if exercise_index == 0:
        exercise_index = len(lines) // 2
        
    theory_text = "".join(lines[:exercise_index])
    exercise_text = "".join(lines[exercise_index:])
    
    # Chunk theory further if needed, but 3600 lines is small enough for the context window.
    # However, to force comprehensive output, we break it into parts.
    
    all_blocks = []
    
    print("Generating Theory Part 1...")
    theory_prompt_1 = f"""
    You are the Chief Academic Architect of Shine Academy Naroda.
    Convert the following Part 1 of the textbook chapter into a fully interactive Shine Academy EduOS JSON array.
    Apply the EduOS 8-Step Socratic Discovery Arc (hook, socratic, discovery, theory/reveal, knowledge_check, reflection, connection, mastery).
    
    RULES:
    1. NO `content` wrapper. Root-level properties only.
    2. Assign a unique `id` to EVERY block (e.g., KOBJ_{CHAPTER_ID}_THEORY_01).
    3. Include full Hindi and Gujarati translations (`title_hi`, `title_gu`, `body_hi`, `body_gu`).
    4. For MCQs (knowledge_check), use integer `correct_index` (0,1,2,3).
    
    TEXT PART 1:
    {theory_text[:len(theory_text)//2]}
    
    Return ONLY a JSON array of objects.
    """
    blocks = call_gemini(theory_prompt_1)
    all_blocks.extend(blocks)
    
    print("Generating Theory Part 2...")
    theory_prompt_2 = theory_prompt_1.replace("Part 1", "Part 2").replace(theory_text[:len(theory_text)//2], theory_text[len(theory_text)//2:])
    blocks = call_gemini(theory_prompt_2)
    all_blocks.extend(blocks)
    
    print("Generating Exercises Part 1...")
    # Exercises must be fully comprehensive.
    ex_prompt_1 = f"""
    You are generating the EXERCISES section for the EduOS JSON format.
    The user is highly strict: "EVERY SINGLE EXERCISE QUESTION MUST BE INCLUDED. NO SHORTCUTS."
    Format complex numerical problems and P&L accounts using Markdown tables in the `body` or `question`.
    Include full Hindi and Gujarati translations for EVERYTHING (`question_hi`, `options_hi`, etc).
    Use root-level properties, NO `content` wrapper.
    Assign a unique `id` to EVERY block (e.g., KOBJ_{CHAPTER_ID}_EX_01).
    For MCQs, use integer `correct_index`.
    
    TEXT EXERCISES PART 1:
    {exercise_text[:len(exercise_text)//3]}
    
    Return ONLY a JSON array of objects representing these exercise questions.
    """
    blocks = call_gemini(ex_prompt_1)
    all_blocks.extend(blocks)
    
    print("Generating Exercises Part 2...")
    ex_prompt_2 = ex_prompt_1.replace("Part 1", "Part 2").replace(exercise_text[:len(exercise_text)//3], exercise_text[len(exercise_text)//3 : 2*len(exercise_text)//3])
    blocks = call_gemini(ex_prompt_2)
    all_blocks.extend(blocks)
    
    print("Generating Exercises Part 3...")
    ex_prompt_3 = ex_prompt_1.replace("Part 1", "Part 3").replace(exercise_text[:len(exercise_text)//3], exercise_text[2*len(exercise_text)//3:])
    blocks = call_gemini(ex_prompt_3)
    all_blocks.extend(blocks)
    
    print(f"Total blocks generated: {len(all_blocks)}")
    
    # Save the output
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    chapter_data = {
        "metadata": {
            "id": CHAPTER_ID.lower(),
            "title": "Dissolution of Partnership Firm",
            "subject": "Accounts",
            "grade": "12"
        },
        "blocks": all_blocks
    }
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(chapter_data, f, indent=2, ensure_ascii=False)
        
    print(f"Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
