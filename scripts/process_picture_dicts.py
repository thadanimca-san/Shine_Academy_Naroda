import os
import re
import json
import time
import glob
import google.generativeai as genai

# Configure API Key
API_KEY = "AIzaSyCXHEJ4KBrebP8ByUEZnVJzuE4u114MGGA"
genai.configure(api_key=API_KEY)
MODEL_NAME = 'gemini-3.6-flash'
try:
    model = genai.GenerativeModel(MODEL_NAME)
except Exception:
    import google.generativeai as genai_fallback
    # in case gemini-3.6-flash is not valid in this sdk version
    model = genai.GenerativeModel('gemini-1.5-flash')

base_dir = "lib/features/learning/school/english/data"
all_dart_files = [f for f in os.listdir(base_dir) if f.endswith(".dart")]

# We want class4_*.dart through class10_*.dart
target_files = []
for f in all_dart_files:
    match = re.match(r'class(\d+)_', f)
    if match:
        grade = int(match.group(1))
        if 4 <= grade <= 10:
            target_files.append(f)

print(f"Found {len(target_files)} target dart files.")

# Load existing universal dictionaries
dict_dir = "app_core/universal_dictionary"
existing_words = {}

for json_file in glob.glob(f"{dict_dir}/*.json"):
    if json_file.endswith("dictionary_index.json"): continue
    try:
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            terms = data.get('terms', [])
            for term in terms:
                word_en = term.get('term', {}).get('english', '').lower().strip()
                if word_en:
                    existing_words[word_en] = term.get('id')
    except Exception as e:
        print(f"Failed to load {json_file}: {e}")

print(f"Loaded {len(existing_words)} existing words from universal dictionary.")

word_pattern = re.compile(r"DictionaryWord\((.*?)\)", re.DOTALL)
words_to_generate = []
word_data_map = {}

# Extract words
for f in target_files:
    filepath = os.path.join(base_dir, f)
    with open(filepath, "r", encoding='utf-8') as file:
        content = file.read()
    
    matches = word_pattern.findall(content)
    for m in matches:
        word_data = {}
        fields = ["word", "partOfSpeech", "emoji", "imagePath", "meaningEn", "meaningHi", "meaningGu", "category"]
        for field in fields:
            match = re.search(rf"{field}:\s*['\"](.*?)['\"]", m)
            if match:
                word_data[field] = match.group(1)
        
        word = word_data.get('word', '').lower().strip()
        if word and word not in existing_words:
            if word not in word_data_map:
                words_to_generate.append(word_data)
                word_data_map[word] = word_data

print(f"Found {len(words_to_generate)} new words to generate.")

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
        
    try:
        response = model.generate_content(prompt)
        text = response.text
        if "```json" in text:
            text = text.split("```json")[1].split("```")[0]
        elif "```" in text:
            text = text.split("```")[1].split("```")[0]
        return json.loads(text.strip())
    except Exception as e:
        print(f"Error generating content: {e}")
        return []

output_file = "app_core/universal_dictionary/class4_to_10_picture_dict.json"
results = {"terms": []}
if os.path.exists(output_file):
    try:
        with open(output_file, 'r', encoding='utf-8') as f:
            results = json.load(f)
            for t in results.get('terms', []):
                word_en = t.get('term', {}).get('english', '').lower().strip()
                if word_en:
                    existing_words[word_en] = t.get('id')
    except Exception:
        pass

# Generate new words
batch_size = 5
batch = []

# Filter words_to_generate again just in case some were loaded from the output_file
words_to_generate = [w for w in words_to_generate if w.get('word', '').lower().strip() not in existing_words]

print(f"Generating for {len(words_to_generate)} remaining new words...")

for idx, word_obj in enumerate(words_to_generate):
    batch.append(word_obj)
    if len(batch) >= batch_size or idx == len(words_to_generate) - 1:
        res = process_batch(batch)
        if res:
            for item in res:
                results['terms'].append(item)
                word_en = item.get('term', {}).get('english', '').lower().strip()
                if word_en:
                    existing_words[word_en] = item.get('id')
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(results, f, indent=2, ensure_ascii=False)
            print(f"Processed batch, total new terms saved: {len(results['terms'])}")
        batch = []
        time.sleep(2)

# Update index if needed
index_file = "app_core/universal_dictionary/dictionary_index.json"
with open(index_file, 'r', encoding='utf-8') as f:
    index_data = json.load(f)

if not any(entry.get('file') == output_file for entry in index_data.get('index', [])):
    index_data['index'].append({
        "file": output_file,
        "category": "english",
        "description": "Class 4 to 10 Picture Dictionary"
    })
    with open(index_file, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, indent=2, ensure_ascii=False)

print("Rewriting dart files...")
# Now rewrite dart files
for f in target_files:
    filepath = os.path.join(base_dir, f)
    with open(filepath, "r", encoding='utf-8') as file:
        content = file.read()
    
    # Extract words to get their order
    matches = word_pattern.findall(content)
    word_ids = []
    for m in matches:
        match = re.search(r"word:\s*['\"](.*?)['\"]", m)
        if match:
            word = match.group(1).lower().strip()
            if word in existing_words:
                word_ids.append(existing_words[word])
            else:
                # Fallback format if for some reason generation failed
                word_ids.append(f"DICT_ENG_{word.upper().replace(' ', '_')}")
    
    # Replace the words array with wordIds array
    # The structure in Dart is typically:
    # words: [
    #   DictionaryWord(...),
    #   ...
    # ],
    
    # We replace from 'words: [' up to the closing '],'
    # with 'wordIds: ['ID1', 'ID2'],'
    
    new_wordIds_str = "wordIds: [\n    " + ",\n    ".join(f"'{wid}'" for wid in word_ids) + "\n  ],"
    
    content = re.sub(r'words:\s*\[.*?\]\s*,?', new_wordIds_str, content, flags=re.DOTALL)
    
    with open(filepath, "w", encoding='utf-8') as file:
        file.write(content)
    
    print(f"Updated {f} with {len(word_ids)} wordIds.")

print("All done!")
