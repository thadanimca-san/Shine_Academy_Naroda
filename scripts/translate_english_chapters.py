import os
import glob
import re
import json
import time
import google.generativeai as genai

# Configure API Key
API_KEY = "AIzaSyCXHEJ4KBrebP8ByUEZnVJzuE4u114MGGA"
genai.configure(api_key=API_KEY)

MODEL_NAME = 'gemini-3.5-flash-lite'
model = genai.GenerativeModel(MODEL_NAME)

DATA_DIR = "/home/ubuntu/Shine_Academy_Naroda/lib/features/learning/school/english/data"

def translate_chapter(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already translated
    if 'hindiText:' in content or 'gujaratiText:' in content:
        print(f"[SKIP] {os.path.basename(filepath)} already translated.")
        return True

    # Extract chapterText block
    match = re.search(r'chapterText:\s*(.*?),\s*hindiSummary:', content, re.DOTALL)
    if not match:
        print(f"[ERROR] Could not find chapterText in {os.path.basename(filepath)}")
        return False
        
    chapter_text_block = match.group(1)
    
    prompt = f"""
    You are an expert translator for Shine Academy Naroda.
    Translate the following English story into both Hindi and Gujarati. 
    Maintain the tone, which is suitable for Indian school students.
    
    English Story (Dart string format):
    {chapter_text_block}
    
    Return ONLY a raw valid JSON object (no markdown, no formatting) with this exact structure:
    {{
        "hindi": "<Full Hindi translation here>",
        "gujarati": "<Full Gujarati translation here>"
    }}
    """

    while True:
        try:
            print(f"Translating {os.path.basename(filepath)}...")
            response = model.generate_content(prompt)
            result_text = response.text.strip()
            
            if result_text.startswith('```json'):
                result_text = result_text[7:-3].strip()
            elif result_text.startswith('```'):
                result_text = result_text[3:-3].strip()
                
            data = json.loads(result_text)
            
            hindi_text = data['hindi'].replace("'", "\\'").replace("$", "\\$")
            gujarati_text = data['gujarati'].replace("'", "\\'").replace("$", "\\$")
            
            # Inject into dart file using triple quotes
            injection = f"hindiText: '''{hindi_text}''',\n  gujaratiText: '''{gujarati_text}''',\n  hindiSummary:"
            new_content = content.replace("hindiSummary:", injection, 1)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
                
            print(f"[SUCCESS] {os.path.basename(filepath)}")
            return True
            
        except Exception as e:
            if "429" in str(e) or "Quota exceeded" in str(e):
                print(f"* Quota exceeded. Waiting 60 seconds...")
                time.sleep(60)
            else:
                print(f"[ERROR] Failed to parse or generate for {os.path.basename(filepath)}: {e}")
                print(f"Raw response: {result_text if 'result_text' in locals() else 'None'}")
                return False

def main():
    files = glob.glob(os.path.join(DATA_DIR, "chapter_class*.dart"))
    print(f"Found {len(files)} chapters to translate.")
    
    success_count = 0
    for f in files:
        if translate_chapter(f):
            success_count += 1
            
    print(f"\nDone! Translated {success_count}/{len(files)} chapters.")

if __name__ == "__main__":
    main()
