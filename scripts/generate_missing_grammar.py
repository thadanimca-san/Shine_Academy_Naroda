import os
import json
import time
from google import genai
from google.genai import types

TEXT_FILE = "/home/ubuntu/Shine_Academy_Naroda/SAN/Year2026/speak_english_confidently.txt"
OUTPUT_DIR = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters"

def get_text_content():
    with open(TEXT_FILE, "r", encoding="utf-8") as f:
        return f.read()

def generate_chapter_json(client, text_content, lesson_number):
    print(f"\n[{time.strftime('%X')}] 🚀 Generating Lesson {lesson_number}...")
    
    prompt = f"""
    You are an expert educational content creator for Shine Academy.
    I am providing you with the complete text of the book 'Speak English Confidently'.
    
    Your task is to extract the content for **LESSON {lesson_number}** ONLY, and format it into a highly structured JSON according to our EduOS Standards.
    
    CRITICAL RULES:
    1. Every block must have an id starting with `govindsir_english_ch{lesson_number}_`
    2. Every single block of content MUST include its Hindi equivalent (e.g., `body_hi`, `title_hi`) AND its Gujarati equivalent (`body_gu`, `title_gu`).
    3. Follow the 8-Step Socratic Discovery Arc where possible (Hook, Socratic Question, Exploration, Reveal, Knowledge Check, Reflection, Connection, Mastery).
    4. Ensure the JSON is 100% valid. Do not output markdown code blocks.
    
    Here is the full text of the book:
    {text_content}
    """
    
    response = client.models.generate_content(
        model='gemini-3.1-pro-preview',
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            temperature=0.2,
        ),
    )
    return response.text

def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        api_key = input("Please enter your Gemini API Key: ")
    client = genai.Client(api_key=api_key)
    text_content = get_text_content()
    
    missing_lessons = [1, 2, 20, 25, 26, 40, 54, 59, 60]
    
    for i in missing_lessons:
        success = False
        while not success:
            try:
                json_str = generate_chapter_json(client, text_content, i)
                parsed_json = json.loads(json_str)
                
                output_file = os.path.join(OUTPUT_DIR, f"govindsir_english_ch{i}.json")
                with open(output_file, "w", encoding="utf-8") as f:
                    json.dump(parsed_json, f, indent=2, ensure_ascii=False)
                    
                print(f"Successfully saved Lesson {i} to {output_file}")
                success = True
                time.sleep(5)
            except Exception as e:
                error_str = str(e)
                print(f"Failed to generate Lesson {i}: {error_str}")
                if "429" in error_str or "RESOURCE_EXHAUSTED" in error_str:
                    time.sleep(15)
                else:
                    time.sleep(5)

if __name__ == "__main__":
    main()
