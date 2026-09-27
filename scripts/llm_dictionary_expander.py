import json
import os
import glob
import time
import re
from google.api_core.exceptions import ResourceExhausted

import google.genai as genai

API_KEY = "AIzaSyCXHEJ4KBrebP8ByUEZnVJzuE4u114MGGA"
client = genai.Client(api_key=API_KEY)
MODEL = "gemini-3.5-flash-lite"

PROMPT_TEMPLATE = """
You are an expert Educational Curriculum Designer for an Indian EdTech platform.
I am providing you with a JSON dictionary entry for a term.

Your Tasks:
1. TYPO FIX: Check the `term.english`. If it has a stray 'n' at the beginning (e.g., "nhonest" instead of "honest", "natom" instead of "atom") or other obvious parsing typos, FIX IT.
2. EXPANSION: The current definitions are too short. Expand BOTH `definition.simple` and `definition.academic` to be EXACTLY 5 sentences long each. Make them highly educational, clear, and engaging for a student.
3. TRANSLATION: Provide perfect Hindi and Gujarati translations for the newly expanded definitions.
4. EXAMPLES & AI CONTEXT: Ensure there are 3-4 examples, and fill out the `ai_context` (common misconceptions and tutor hint) if they are missing or too brief. Provide Hindi and Gujarati for these too.
5. OUTPUT: Return ONLY valid, raw JSON. Do not include markdown formatting like ```json. 

Ensure the output exactly matches this schema:
{
  "id": "KEEP_ORIGINAL_ID",
  "term": {
    "english": "Corrected English Term",
    "hindi": "Translated Term",
    "gujarati": "Translated Term"
  },
  "definition": {
    "simple": "5 sentences in English...",
    "simple_hi": "5 sentences in Hindi...",
    "simple_gu": "5 sentences in Gujarati...",
    "academic": "5 sentences in English...",
    "academic_hi": "5 sentences in Hindi...",
    "academic_gu": "5 sentences in Gujarati..."
  },
  "examples": ["Ex1", "Ex2"],
  "examples_hi": ["Ex1_hi", "Ex2_hi"],
  "examples_gu": ["Ex1_gu", "Ex2_gu"],
  "ai_context": {
    "common_misconceptions": ["Misconception 1 in English"],
    "common_misconceptions_hi": ["Misconception 1 in Hindi"],
    "common_misconceptions_gu": ["Misconception 1 in Gujarati"],
    "tutor_hint": "Hint in English",
    "tutor_hint_hi": "Hint in Hindi",
    "tutor_hint_gu": "Hint in Gujarati"
  }
}

Here is the original JSON to fix and expand:
{json_data}
"""

def clean_json_response(text):
    text = text.strip()
    if text.startswith("```json"):
        text = text[7:]
    if text.startswith("```"):
        text = text[3:]
    if text.endswith("```"):
        text = text[:-3]
    return text.strip()

def process_file(file_path):
    print(f"\nProcessing: {os.path.basename(file_path)}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            original_data = json.load(f)
        except Exception as e:
            print(f"  [X] Failed to load JSON: {e}")
            return False

    simple_def = original_data.get('definition', {}).get('simple', '')
    if 'simple_hi' in original_data.get('definition', {}) and len(simple_def.split('.')) >= 4:
         print("  [✓] Already expanded. Skipping.")
         return False

    prompt = PROMPT_TEMPLATE.replace("{json_data}", json.dumps(original_data, ensure_ascii=False, indent=2))

    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model=MODEL,
                contents=prompt
            )
            output = clean_json_response(response.text)
            new_data = json.loads(output)
            
            new_data['id'] = original_data.get('id', new_data.get('id'))
            if 'media' in original_data:
                new_data['media'] = original_data['media']
            if 'knowledge_graph_links' in original_data:
                new_data['knowledge_graph_links'] = original_data['knowledge_graph_links']

            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(new_data, f, ensure_ascii=False, indent=2)
                f.write('\n')
            
            print("  [+] Successfully expanded and saved!")
            time.sleep(2) 
            return True
            
        except ResourceExhausted:
            print("  [!] Rate limit hit. Waiting 30 seconds...")
            time.sleep(30)
        except json.JSONDecodeError:
            print("  [!] LLM returned invalid JSON. Retrying...")
            time.sleep(2)
        except Exception as e:
            print(f"  [X] Unexpected error: {e}")
            time.sleep(2)
            
    print("  [X] Failed after max retries.")
    return False

def main():
    print("==================================================================")
    print("AI DICTIONARY EXPANDER: 5 SENTENCES + TYPO FIXER (NEW SDK)")
    print("==================================================================")
    print("Press Ctrl+C at any time to safely stop. Progress is saved per file.")
    
    files = glob.glob('app_core/knowledge_graph/dictionary/*.json')
    total_files = len(files)
    expanded_count = 0
    
    for i, file_path in enumerate(files):
        print(f"\n--- File {i+1}/{total_files} ---")
        try:
            if process_file(file_path):
                expanded_count += 1
        except KeyboardInterrupt:
            print("\n\n[🛑] Script paused by user! Progress saved.")
            break
            
    print("\n==================================================================")
    print(f"FINISHED! Expanded and fixed {expanded_count} dictionary entries.")
    print("==================================================================")

if __name__ == "__main__":
    main()
