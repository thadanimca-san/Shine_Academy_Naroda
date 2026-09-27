import os
import json
import time
from google import genai
from google.genai import types

# Path configuration
TEXT_FILE = "/home/ubuntu/Shine_Academy_Naroda/SAN/Year2026/speak_english_confidently.txt"
OUTPUT_DIR = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters"

def get_api_key():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        api_key = input("Please enter your Gemini API Key: ")
    return api_key

def get_text_content():
    with open(TEXT_FILE, "r", encoding="utf-8") as f:
        return f.read()

def generate_chapter_json(client, text_content, lesson_number):
    print(f"\n[{time.strftime('%X')}] 🚀 Generating Lesson {lesson_number}...")
    print(f"[{time.strftime('%X')}] ⏳ Waiting for Gemini to read the 11,000-line book and extract the lesson (this takes 30-60 seconds, please don't cancel)...")
    
    prompt = f"""
    You are an expert educational content creator for Shine Academy.
    I am providing you with the complete text of the book 'Speak English Confidently'.
    
    Your task is to extract the content for **LESSON {lesson_number}** ONLY, and format it into a highly structured JSON according to our EduOS Standards.
    
    The book has a Table of Contents at the beginning which lists all the lesson titles. Find the title for Lesson {lesson_number}, locate the corresponding content in the body of the text, and convert it into the JSON format below.
    
    CRITICAL RULES:
    1. Every block must have an id starting with `govindsir_english_ch{lesson_number}_` (e.g. `govindsir_english_ch{lesson_number}_1`).
    2. Every single block of content (titles, bodies, questions, options, explanations, teacher tips) MUST include its Hindi equivalent (e.g., `body_hi`, `title_hi`) AND its Gujarati equivalent (`body_gu`, `title_gu`).
    3. Follow the 8-Step Socratic Discovery Arc where possible (Hook, Socratic Question, Exploration, Reveal, Knowledge Check, Reflection, Connection, Mastery).
    4. Ensure the JSON is 100% valid. Do not output markdown code blocks like ```json, just the raw JSON.
    
    JSON SCHEMA EXAMPLE:
    {{
      "metadata": {{
        "id": "govindsir_english_ch{lesson_number}",
        "title": "Lesson {lesson_number}: <Title Here>",
        "subject": "Spoken English",
        "grade": "All",
        "difficulty": "Beginner",
        "estimated_minutes": 20,
        "learning_outcomes": ["...", "..."],
        "core_concepts": ["...", "..."],
        "ai_context": {{
          "learning_goal": "...",
          "common_misconceptions": ["..."]
        }}
      }},
      "blocks": [
        {{
          "id": "govindsir_english_ch{lesson_number}_1",
          "type": "theory",
          "title": "...",
          "title_hi": "...",
          "title_gu": "...",
          "body": "...",
          "body_hi": "...",
          "body_gu": "..."
        }}
      ]
    }}
    
    Here is the full text of the book:
    {text_content}
    """
    
    response = client.models.generate_content(
        model='gemini-3.6-flash',
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            temperature=0.2,
        ),
    )
    return response.text

def main():
    api_key = get_api_key()
    client = genai.Client(api_key=api_key)
    text_content = get_text_content()
    
    # Let's say we want to process chapters 3 to 60 (since 1 and 2 are done)
    for i in range(3, 61):
        try:
            json_str = generate_chapter_json(client, text_content, i)
            
            # Basic validation to ensure it's parseable JSON
            parsed_json = json.loads(json_str)
            
            output_file = os.path.join(OUTPUT_DIR, f"govindsir_english_ch{i}.json")
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(parsed_json, f, indent=2, ensure_ascii=False)
                
            print(f"Successfully saved Lesson {i} to {output_file}")
            
            # Sleep to avoid rate limits
            time.sleep(30)
            
        except Exception as e:
            error_str = str(e)
            print(f"Failed to generate Lesson {i}: {error_str}")
            if "429" in error_str or "RESOURCE_EXHAUSTED" in error_str:
                print("Rate limit reached. Waiting 60 seconds before retrying...")
                time.sleep(60)
                # We want to retry the same lesson, so we decrement i
                # But since this is a for loop, we can't easily decrement the loop variable.
                # Let's handle retries inside a while loop.
                pass
            else:
                time.sleep(10)

def main():
    api_key = get_api_key()
    client = genai.Client(api_key=api_key)
    text_content = get_text_content()
    
    i = 3
    while i <= 60:
        try:
            json_str = generate_chapter_json(client, text_content, i)
            
            parsed_json = json.loads(json_str)
            
            output_file = os.path.join(OUTPUT_DIR, f"govindsir_english_ch{i}.json")
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(parsed_json, f, indent=2, ensure_ascii=False)
                
            print(f"Successfully saved Lesson {i} to {output_file}")
            i += 1
            time.sleep(30)
        except Exception as e:
            error_str = str(e)
            print(f"Failed to generate Lesson {i}: {error_str}")
            if "429" in error_str or "RESOURCE_EXHAUSTED" in error_str:
                print("Rate limit reached. Waiting 60 seconds before retrying...")
                time.sleep(60)
            else:
                print("Non-rate-limit error. Skipping this lesson.")
                i += 1
                time.sleep(10)

if __name__ == "__main__":
    main()
