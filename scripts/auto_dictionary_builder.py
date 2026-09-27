import os
import json
import time
import argparse
import re
import sqlite3
import google.generativeai as genai

CHAPTERS_DIR = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters"
DICT_DIR = "/home/ubuntu/Shine_Academy_Naroda/app_core/universal_dictionary"
MINED_PATH = os.path.join(DICT_DIR, "mined_words.json")
INDEX_PATH = os.path.join(DICT_DIR, "dictionary_index.json")
DB_PATH = "/home/ubuntu/Shine_Academy_Naroda/assets/dictionary/universal_dictionary.db"

def init_genai(api_key, model_name="gemini-1.5-flash"):
    genai.configure(api_key=api_key)
    return genai.GenerativeModel(model_name)

def extract_words_from_chapters():
    all_words = set()
    print("Scanning chapters for vocabulary...")
    for filename in os.listdir(CHAPTERS_DIR):
        if not filename.endswith(".json"):
            continue
        filepath = os.path.join(CHAPTERS_DIR, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            # Extract all English letter sequences, length 3 or more
            words = re.findall(r'\b[a-zA-Z]{3,}\b', content)
            for w in words:
                all_words.add(w.lower())
        except Exception as e:
            print(f"Error reading {filename}: {e}")
            
    # Filter out common stop words and obvious code artifacts (like 'true', 'false', 'type', 'id')
    stop_words = {"the", "and", "that", "this", "for", "with", "from", "are", "have", 
                  "has", "had", "was", "were", "type", "true", "false", "null", "content", 
                  "title", "body", "question", "answer", "explanation", "options"}
    filtered_words = {w for w in all_words if w not in stop_words}
    print(f"Extracted {len(filtered_words)} unique English words from chapters.")
    return filtered_words

def get_existing_words():
    existing_words = set()
    if os.path.exists(DB_PATH):
        try:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute("SELECT word_en FROM terms")
            rows = cursor.fetchall()
            for row in rows:
                if row[0]:
                    existing_words.add(row[0].lower())
            conn.close()
            print(f"Found {len(existing_words)} existing words in dictionary database.")
        except Exception as e:
            print(f"Could not read existing database: {e}")
    else:
        print("Dictionary database not found. Assuming empty dictionary.")
    return existing_words

def update_dictionary_index():
    # Make sure mined_words.json is included in the dictionary index so it gets compiled
    if not os.path.exists(INDEX_PATH):
        return
        
    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        index_data = json.load(f)
        
    already_indexed = False
    for entry in index_data.get("index", []):
        if entry.get("file") == "app_core/universal_dictionary/mined_words.json":
            already_indexed = True
            break
            
    if not already_indexed:
        index_data["index"].append({
            "id": "dict_mined_words",
            "file": "app_core/universal_dictionary/mined_words.json",
            "subject": "General",
            "grade": "All"
        })
        with open(INDEX_PATH, 'w', encoding='utf-8') as f:
            json.dump(index_data, f, indent=2, ensure_ascii=False)
        print("Added mined_words.json to dictionary_index.json")

def generate_dictionary_entries(model, words_list):
    prompt = f"""
    You are an expert linguist for Shine Academy EduOS.
    I will provide a list of English words. For EACH word, you must generate a JSON object matching the EduOS Dictionary Standard.

    CRITICAL RULES:
    1. Every term MUST have translations in Hindi AND Gujarati.
    2. 'id' must be format: DICT_ENG_<WORD_IN_UPPERCASE>
    3. Include pronunciation in Hindi text (e.g. "एप्पल").
    
    Expected output is ONLY a raw JSON array of objects. Do not wrap in markdown ```json.
    
    WORDS TO PROCESS:
    {", ".join(words_list)}
    
    Schema per word:
    {{
      "id": "DICT_ENG_APPLE",
      "term": {{
        "english": "apple",
        "hindi": "सेब",
        "gujarati": "સફરજન"
      }},
      "part_of_speech": "noun",
      "definition": {{
        "simple": {{
          "en": "A round fruit with red or green skin.",
          "hi": "लाल या हरे छिलके वाला एक गोल फल।",
          "gu": "લાલ અથવા લીલી છાલવાળું ગોળ ફળ."
        }},
        "academic": {{
          "en": "The fleshy, usually rounded red, yellow, or green edible pome fruit of a usually cultivated tree (genus Malus) of the rose family."
        }}
      }},
      "examples": [
        {{
          "en": "I ate an apple.",
          "hi": "मैंने एक सेब खाया।",
          "gu": "મેં સફરજન ખાધું."
        }}
      ],
      "pronunciation_hi": "एप्पल"
    }}
    """
    
    while True:
        try:
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
    parser = argparse.ArgumentParser(description="Automated Dictionary Miner")
    parser.add_argument("--api_key", type=str, required=True, help="Your Gemini API Key")
    parser.add_argument("--model", type=str, default="gemini-1.5-flash", help="Model name (e.g. gemini-1.5-flash)")
    args = parser.parse_args()
    
    print("=== STARTING AUTOMATED DICTIONARY MINING ===")
    
    # 1. Scan chapters
    chapter_words = extract_words_from_chapters()
    
    # 2. Get existing dictionary words
    existing_words = get_existing_words()
    
    # 3. Calculate missing words
    missing_words = list(chapter_words - existing_words)
    missing_words.sort()
    print(f"\nFound {len(missing_words)} words missing from the dictionary!")
    
    if not missing_words:
        print("Dictionary is already up-to-date with all chapters!")
        return
        
    # 4. Generate and save
    model = init_genai(args.api_key, args.model)
    update_dictionary_index()
    
    batch_size = 15
    for i in range(0, len(missing_words), batch_size):
        batch = missing_words[i:i+batch_size]
        print(f"\nProcessing batch {i//batch_size + 1}/{(len(missing_words) + batch_size - 1)//batch_size} ({len(batch)} words)...")
        
        terms = generate_dictionary_entries(model, batch)
        
        # Append to mined_words.json
        if os.path.exists(MINED_PATH):
            with open(MINED_PATH, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                except:
                    data = {"terms": []}
        else:
            data = {"terms": []}
            
        data["terms"].extend(terms)
        
        with open(MINED_PATH, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            
        print(f"Successfully saved {len(terms)} new terms to mined_words.json")
        time.sleep(2) # brief pause to respect API limits

if __name__ == "__main__":
    main()
