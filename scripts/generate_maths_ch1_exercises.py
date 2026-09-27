import json
import time
import google.generativeai as genai
from google.api_core import exceptions

def generate_exercises():
    genai.configure(api_key="AIzaSyCXHEJ4KBrebP8ByUEZnVJzuE4u114MGGA")
    
    prompt = """
    You are an expert curriculum developer for Shine Academy.
    Your task is to extract ALL exercise questions from the latest rationalised NCERT Class 10 Mathematics textbook, Chapter 1: Real Numbers.
    Specifically:
    Exercise 1.1 (Prime Factorisation, LCM & HCF, checking digits, composite numbers)
    Exercise 1.2 (Proving irrationality of sqrt(5), 3+2sqrt(5), etc.)
    
    Convert each question into a JSON block suitable for the EduOS Assessment Engine.
    For questions that are purely subjective (like "Prove that sqrt(5) is irrational"), use type: "short_note".
    For calculation questions (like "Find the LCM and HCF of 26 and 91"), use type: "short_note".
    
    CRITICAL: You MUST provide translations for English (en), Hindi (hi), and Gujarati (gu) for EVERYTHING (question, answer, explanation).
    
    Output a RAW JSON array of objects (do not wrap in markdown ```json).
    
    Schema for each block:
    {
      "type": "short_note",
      "id": "KOBJ_CLASS10_MATH_CH1_EX_...",
      "difficulty": "Intermediate",
      "marks": 2,
      "question_en": "Question text...",
      "question_hi": "Question in Hindi...",
      "question_gu": "Question in Gujarati...",
      
      "answer_en": "Step by step solution...",
      "answer_hi": "Step by step solution...",
      "answer_gu": "Step by step solution...",
      
      "explanation_en": "Explanation...",
      "explanation_hi": "Explanation...",
      "explanation_gu": "Explanation..."
    }
    
    Make sure you generate EVERY SINGLE QUESTION from Exercise 1.1 and 1.2.
    """
    
    model = genai.GenerativeModel('gemini-3.6-flash')
    
    max_retries = 5
    for attempt in range(max_retries):
        try:
            print("Calling Gemini API via google.generativeai...")
            response = model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=0.2,
                )
            )
            break
        except exceptions.ResourceExhausted as e:
            print(f"Rate limit hit. Waiting 60 seconds... (Attempt {attempt+1}/{max_retries})")
            time.sleep(60)
    else:
        print("Failed after retries.")
        return
        
    raw_json = response.text.strip()
    if raw_json.startswith("```json"):
        raw_json = raw_json[7:-3].strip()
    elif raw_json.startswith("```"):
        raw_json = raw_json[3:-3].strip()
        
    new_blocks = json.loads(raw_json)
    
    file_path = "app_core/chapters/ncert_class10_maths_ch1.json"
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    data["blocks"].append({
      "type": "heading",
      "id": "KOBJ_CLASS10_MATH_CH1_EX_HEADING",
      "title": "Textbook Exercises",
      "title_hi": "पाठ्यपुस्तक अभ्यास",
      "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય"
    })
    
    data["blocks"].extend(new_blocks)
    
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    print(f"Successfully appended {len(new_blocks)} exercise questions!")

if __name__ == "__main__":
    generate_exercises()
