import os
import json
import time
import argparse
import google.generativeai as genai

# NOTE: google.generativeai is deprecated, but since your environment still uses it, 
# this script ensures compatibility with your current project setup!

CHAPTERS_DIR = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters"

def generate_chapter_blocks(model, board, grade, subject, chapter_num, chapter_title, context_dir=None):
    context_text = ""
    if context_dir:
        tb_path = os.path.join(context_dir, f"ch{chapter_num}tb.txt")
        g_path = os.path.join(context_dir, f"ch{chapter_num}g.txt")
        
        if os.path.exists(tb_path):
            with open(tb_path, 'r', encoding='utf-8') as f:
                context_text += "\n\n--- TEXTBOOK SOURCE ---\n" + f.read()
        if os.path.exists(g_path):
            with open(g_path, 'r', encoding='utf-8') as f:
                context_text += "\n\n--- GUIDE/SOLUTIONS SOURCE ---\n" + f.read()

    prompt = f"""
    You are the Chief Academic Architect of Shine Academy Naroda.
    
    We need to generate a high-quality educational chapter for {board} Class {grade} {subject}.
    The chapter is: Chapter {chapter_num}: {chapter_title}
    
    {context_text}
    
    Please use your extensive knowledge of the {board} Class {grade} {subject} textbook to generate a fully interactive Shine Academy EduOS JSON chapter according to the NEW EduOS 8-Step Gold Pedagogy Standard v2.0.
    
    CRITICAL INSTRUCTION:
    THIS IS NOT A SMALL PROJECT. EVERY SINGLE EXERCISE QUESTION FROM THE {board} CLASS {grade} TEXTBOOK FOR THIS CHAPTER MUST BE INCLUDED AT THE END OF THE CHAPTER AS MCQ OR TRUE/FALSE. NO SHORTCUTS. NO LAZY SUMMARIES.

    The 8-Step Cycle MUST be followed for the theory part:
    1. hook
    2. socratic_question (must use 'socratic_question' type)
    3. discovery
    4. theory (reveal)
    5. knowledge_check (must be type 'mcq' or 'true_false')
    6. reflection
    7. connection
    8. mastery
    
    After the theory part, include ALL textbook exercise questions.
    
    CRITICAL RULES:
    1. Every single block MUST have English, Hindi, AND Gujarati translations for ALL string fields (e.g. title, title_hi, title_gu, body, body_hi, body_gu, question, question_hi, question_gu, options, options_hi, options_gu, explanation, explanation_hi, explanation_gu).
    2. The 'id' for each block must follow the format KOBJ_{board.upper()}_C{grade}_{subject[:3].upper()}_CH{chapter_num}_<NUM>.
    3. Put ALL fields at the root level of the block object, EXCEPT for 'metadata' if you need it. DO NOT USE a 'content' wrapper. (e.g. {{"type":"theory","body":"..."}})
    4. For knowledge checks and MCQs, use integer 'correct_index' (e.g., 0, 1, 2, 3), NOT 'correct_answer'.
    
    Expected JSON Output (Return ONLY a valid JSON array of blocks, nothing else. Do not wrap in ```json):
    [
      {{
        "id": "KOBJ_{board.upper()}_C{grade}_{subject[:3].upper()}_CH{chapter_num}_001",
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
                print(f"  * JSON parse error: {e}. Retrying in 5s...")
                time.sleep(5)

def main():
    parser = argparse.ArgumentParser(description="Generate Gold Standard EduOS Chapter with Custom API Key")
    parser.add_argument('--api_key', type=str, required=True, help="Your new Gemini API Key")
    parser.add_argument('--board', type=str, required=True, help="Board name (e.g., NCERT, GSEB)")
    parser.add_argument('--grade', type=int, required=True, help="Grade (e.g., 7, 10)")
    parser.add_argument('--subject', type=str, required=True, help="Subject (e.g., Social_Science, Science, Maths)")
    parser.add_argument('--chapter_num', type=int, required=True, help="Chapter number")
    parser.add_argument('--chapter_title', type=str, required=True, help="Chapter title")
    parser.add_argument('--model', type=str, default="gemini-1.5-flash", help="Model name (e.g. gemini-1.5-flash, gemini-1.5-pro)")
    
    args = parser.parse_args()
    
    # Configure API key dynamically
    genai.configure(api_key=args.api_key)
    model = genai.GenerativeModel(args.model)
    
    chapter_identifier = f"{args.board.lower()}_class{args.grade}_{args.subject.lower()}_ch{args.chapter_num}"
    filename = f"{chapter_identifier}.json"
    filepath = os.path.join(CHAPTERS_DIR, filename)
    
    print(f"\nProcessing {filename} (Title: {args.chapter_title})...")
    new_blocks = generate_chapter_blocks(model, args.board, args.grade, args.subject, args.chapter_num, args.chapter_title)
    
    chapter_data = {
        "metadata": {
            "id": chapter_identifier,
            "title": f"Chapter {args.chapter_num}: {args.chapter_title}",
            "subject": args.subject.replace("_", " "),
            "grade": str(args.grade)
        },
        "blocks": new_blocks
    }
        
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(chapter_data, f, ensure_ascii=False, indent=2)
        
    print(f"Successfully saved {filename}!")

if __name__ == "__main__":
    main()
