import os
import json
import time
import argparse
import re
from spellchecker import SpellChecker
import google.generativeai as genai

DICT_DIR = "/home/ubuntu/Shine_Academy_Naroda/app_core/universal_dictionary"
ANOMALIES_PATH = os.path.join(DICT_DIR, "anomalies_to_fix.json")

def init_genai(api_key, model_name="gemini-1.5-flash"):
    genai.configure(api_key=api_key)
    return genai.GenerativeModel(model_name)

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
            print(f"Calling Gemini API for batch of {len(words_list)} words...")
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

def add_words(args):
    model = init_genai(args.api_key, args.model)
    
    if not os.path.exists(args.input_file):
        print(f"Error: {args.input_file} not found.")
        return
        
    with open(args.input_file, 'r', encoding='utf-8') as f:
        words = [line.strip() for line in f if line.strip()]
        
    print(f"Loaded {len(words)} words from {args.input_file}")
    
    # Process in batches of 20
    batch_size = 20
    all_new_terms = []
    
    for i in range(0, len(words), batch_size):
        batch = words[i:i+batch_size]
        print(f"Processing batch {i//batch_size + 1} ({len(batch)} words)...")
        terms = generate_dictionary_entries(model, batch)
        all_new_terms.extend(terms)
        time.sleep(2) # brief pause
        
    # Append to target dictionary file
    target_path = os.path.join(DICT_DIR, args.target_dict)
    if os.path.exists(target_path):
        with open(target_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = {"terms": []}
        
    data["terms"].extend(all_new_terms)
    
    with open(target_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully added {len(all_new_terms)} new terms to {args.target_dict}")

def audit_dictionary(args):
    dict_path = os.path.join(DICT_DIR, args.target_dict)
    if not os.path.exists(dict_path):
        print(f"Error: {dict_path} not found.")
        return
        
    print(f"Loading dictionary from {args.target_dict} for audit...")
    with open(dict_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    terms = data.get("terms", [])
    print(f"Total terms loaded: {len(terms)}")
    
    spell = SpellChecker()
    
    clean_terms = []
    anomalies = []
    
    print("Auditing words (this may take a few moments for large files)...")
    for i, entry in enumerate(terms):
        term_obj = entry.get("term", {})
        eng = term_obj.get("english", "").strip().lower()
        
        is_clean = True
        
        # Check if the English word is actually a transliterated garbage word (e.g. 'paada')
        # We only strictly check words that are alphabetic (no spaces/hyphens)
        if eng.isalpha():
            if eng not in spell and spell.correction(eng) != eng:
                is_clean = False
                entry["audit_reasons"] = [f"Not a valid English dictionary word: '{eng}'"]
                
        if is_clean:
            clean_terms.append(entry)
        else:
            anomalies.append(entry)
            
    print(f"\nAudit Complete!")
    print(f"Clean (Real English) terms kept: {len(clean_terms)}")
    print(f"Garbage/Anomalies removed: {len(anomalies)}")
    
    # Save anomalies
    if os.path.exists(ANOMALIES_PATH):
        with open(ANOMALIES_PATH, 'r', encoding='utf-8') as f:
            existing_anomalies = json.load(f).get("terms", [])
    else:
        existing_anomalies = []
        
    existing_anomalies.extend(anomalies)
    
    with open(ANOMALIES_PATH, 'w', encoding='utf-8') as f:
        json.dump({"terms": existing_anomalies}, f, indent=2, ensure_ascii=False)
        
    # Overwrite dict with clean terms
    data["terms"] = clean_terms
    with open(dict_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        
    print(f"Cleaned dictionary saved to {dict_path}")
    print(f"Anomalies moved to {ANOMALIES_PATH}")
    print("\nIMPORTANT: Run 'python3 scripts/compile_dictionary_db.py' after you are done!")

def main():
    parser = argparse.ArgumentParser(description="Universal Dictionary Manager")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # Audit Parser
    audit_parser = subparsers.add_parser("audit", help="Audit an existing dictionary to strip out non-English transliterated words.")
    audit_parser.add_argument("--target_dict", type=str, default="generated_massive_dict.json", help="The json file inside app_core/universal_dictionary to audit (e.g. generated_massive_dict.json)")
    
    # Add Words Parser
    add_parser = subparsers.add_parser("add_words", help="Add new words from a text file using Gemini API.")
    add_parser.add_argument("--api_key", type=str, required=True, help="Your Gemini API Key")
    add_parser.add_argument("--input_file", type=str, required=True, help="Path to a .txt file containing one word per line")
    add_parser.add_argument("--target_dict", type=str, default="generated_massive_dict.json", help="The json file inside app_core/universal_dictionary to append to")
    add_parser.add_argument("--model", type=str, default="gemini-1.5-flash", help="Model name (e.g. gemini-1.5-flash)")
    
    args = parser.parse_args()
    
    if args.command == "audit":
        audit_dictionary(args)
    elif args.command == "add_words":
        add_words(args)

if __name__ == "__main__":
    main()
