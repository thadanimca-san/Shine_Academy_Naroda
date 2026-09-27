import os
import json
import time
import glob
import google.generativeai as genai

API_KEY = "AIzaSyCXHEJ4KBrebP8ByUEZnVJzuE4u114MGGA"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-3.5-flash-lite')

CHAPTERS_DIR = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters"

def fix_and_translate_mcq(block, chapter_id, q_num):
    # If already fixed, skip
    if block.get("type") == "mcq" and "question_hi" in block:
        return block

    content = block.get("content", {})
    if not content:
        # Might be a hook
        if block.get("type") == "hook":
            return block
        return None

    question_en = content.get("question", "")
    options_en = content.get("options", [])
    correct_answer = content.get("correct_answer", "")
    explanation_en = content.get("explanation", "")

    # Fix correct_index
    correct_index = 0
    for i, opt in enumerate(options_en):
        if opt.strip() == correct_answer.strip():
            correct_index = i
            break

    prompt = f"""
    Translate the following English MCQ into Hindi and Gujarati.
    
    Question: {question_en}
    Options: {json.dumps(options_en)}
    Explanation: {explanation_en}
    
    Return EXACTLY this JSON structure:
    {{
        "question_hi": "Hindi question",
        "question_gu": "Gujarati question",
        "options_hi": ["Option 1 hi", "Option 2 hi", "Option 3 hi", "Option 4 hi"],
        "options_gu": ["Option 1 gu", "Option 2 gu", "Option 3 gu", "Option 4 gu"],
        "explanation_hi": "Hindi explanation",
        "explanation_gu": "Gujarati explanation"
    }}
    """

    while True:
        try:
            print(f"  Translating Q{q_num} via Gemini...")
            response = model.generate_content(prompt)
            res_text = response.text.strip()
            if res_text.startswith("```json"):
                res_text = res_text[7:-3].strip()
            elif res_text.startswith("```"):
                res_text = res_text[3:-3].strip()
                
            trans_data = json.loads(res_text)
            
            new_block = {
                "id": f"KOBJ_{chapter_id.upper()}_MCQ_{q_num}",
                "type": "mcq",
                "question": question_en,
                "question_hi": trans_data["question_hi"],
                "question_gu": trans_data["question_gu"],
                "options": options_en,
                "options_hi": trans_data["options_hi"],
                "options_gu": trans_data["options_gu"],
                "correct_index": correct_index,
                "explanation": explanation_en,
                "explanation_hi": trans_data["explanation_hi"],
                "explanation_gu": trans_data["explanation_gu"]
            }
            return new_block
            
        except Exception as e:
            if "429" in str(e) or "Quota" in str(e):
                print("  * Rate limit hit. Waiting 60 seconds...")
                time.sleep(60)
            else:
                print(f"  * JSON parse error: {e}. Retrying in 5s...")
                time.sleep(5)

def main():
    print("--- Fixing CBSE Class 10 English MCQs ---")
    
    for i in range(1, 10):
        filename = f"cbse_class10_english_ch{i}.json"
        filepath = os.path.join(CHAPTERS_DIR, filename)
        
        if not os.path.exists(filepath):
            continue
            
        print(f"\nProcessing {filename}...")
        
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        new_blocks = []
        q_counter = 1
        
        for block in data.get("blocks", []):
            if block.get("type") == "hook":
                # Ensure it has translations
                if "content_hi" not in block:
                    block["content_hi"] = "इस कहानी के बारे में आपकी समझ का परीक्षण करें।"
                    block["content_gu"] = "આ વાર્તા વિશે તમારી સમજણની કસોટી કરો."
                new_blocks.append(block)
            else:
                fixed_block = fix_and_translate_mcq(block, f"CBSE_CH{i}", q_counter)
                if fixed_block:
                    new_blocks.append(fixed_block)
                    q_counter += 1
                time.sleep(2) # Polite API delay
                
        data["blocks"] = new_blocks
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
        print(f"Successfully saved {filename}!")
        
    print("All files processed!")

if __name__ == "__main__":
    main()
