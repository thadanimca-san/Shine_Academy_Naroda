import json
import os
import google.generativeai as genai
import time

# Configure API Key
API_KEY = "AIzaSyCXHEJ4KBrebP8ByUEZnVJzuE4u114MGGA"
genai.configure(api_key=API_KEY)

MODEL_NAME = 'gemini-3.6-flash'
model = genai.GenerativeModel(MODEL_NAME)

with open('temp_class3_words.json', 'r') as f:
    words = json.load(f)

output_file = "app_core/universal_dictionary/class3_picture_dict.json"

results = {"terms": []}
if os.path.exists(output_file):
    try:
        with open(output_file, 'r') as f:
            results = json.load(f)
    except:
        pass

existing_words = {term['term']['english'].lower() for term in results.get('terms', [])}

def process_batch(batch):
    prompt = """
You are an expert curriculum developer. Convert the following words into the universal dictionary JSON format.
For each word, you must provide EXACTLY 5 example sentences in English, Hindi, and Gujarati.
The dictionary format must match this structure EXACTLY (output ONLY valid JSON):
[
  {
    "id": "DICT_ENG_[WORD_UPPERCASE]",
    "term": {
      "english": "Word",
      "hindi": "Hindi translation",
      "gujarati": "Gujarati translation"
    },
    "definition": {
      "simple": {
        "en": "Simple english meaning",
        "hi": "Simple hindi meaning",
        "gu": "Simple gujarati meaning"
      }
    },
    "examples": [
      {
        "en": "Sentence 1",
        "hi": "Hindi 1",
        "gu": "Gujarati 1"
      },
      ... 5 sentences exactly!
    ],
    "media": {
      "emoji": "emoji",
      "imagePath": "imagePath"
    }
  }
]

Words to process:
"""
    for w in batch:
        prompt += f"- {w.get('word', '')} (emoji: {w.get('emoji', '')}, imagePath: {w.get('imagePath', '')}, category: {w.get('category', 'None')})\n"
        
    response = model.generate_content(prompt)
    
    text = response.text
    # remove markdown blocks if any
    if "```json" in text:
        text = text.split("```json")[1].split("```")[0]
    elif "```" in text:
        text = text.split("```")[1].split("```")[0]
        
    return json.loads(text.strip())


batch_size = 5
batch = []
count = 0

for word_obj in words:
    if word_obj.get('word', '').lower() in existing_words:
        continue
        
    batch.append(word_obj)
    if len(batch) >= batch_size:
        try:
            res = process_batch(batch)
            results['terms'].extend(res)
            
            with open(output_file, 'w') as f:
                json.dump(results, f, indent=2)
            print(f"Processed {len(results['terms'])} terms...")
        except Exception as e:
            print(f"Failed batch: {e}")
            time.sleep(2)
        batch = []
        time.sleep(1)

if batch:
    try:
        res = process_batch(batch)
        results['terms'].extend(res)
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2)
    except Exception as e:
        print(f"Failed final batch: {e}")

print("Done! Total terms:", len(results['terms']))
