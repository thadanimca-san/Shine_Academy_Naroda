import os
import json
import re
from spellchecker import SpellChecker

DICT_PATH = "/home/ubuntu/Shine_Academy_Naroda/app_core/universal_dictionary/generated_massive_dict.json"
ANOMALIES_PATH = "/home/ubuntu/Shine_Academy_Naroda/app_core/universal_dictionary/anomalies_to_fix.json"

def is_english_letters_present(text):
    if not isinstance(text, str):
        return True
    return bool(re.search(r'[a-zA-Z]', text))

def audit_dictionary():
    print("Loading massive dictionary...")
    with open(DICT_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    terms = data.get("terms", [])
    print(f"Total terms loaded: {len(terms)}")
    
    spell = SpellChecker()
    
    clean_terms = []
    anomalies = []
    
    for i, entry in enumerate(terms):
        if i % 5000 == 0 and i > 0:
            print(f"Processed {i} entries...")
            
        term = entry.get("term", {})
        eng = term.get("english", "")
        hin = term.get("hindi", "")
        guj = term.get("gujarati", "")
        
        reasons = []
        
        # 1. Check missing fields
        if not eng or not hin or not guj:
            reasons.append("Missing one or more term translations")
            
        # 2. English letters in Hindi/Gujarati translation
        if is_english_letters_present(hin):
            reasons.append("English characters found in Hindi term")
        if is_english_letters_present(guj):
            reasons.append("English characters found in Gujarati term")
            
        # 3. Spell check English term
        # Only check single words without spaces or hyphens
        if eng.isalpha():
            if spell.correction(eng.lower()) != eng.lower() and eng.lower() not in spell:
                reasons.append(f"Possible spelling error in English term: '{eng}'")
                
        # 4. Check Examples for nouns
        pos = entry.get("part_of_speech", "")
        examples = entry.get("examples", [])
        if pos == "noun" and len(examples) != 5:
            reasons.append(f"Noun has {len(examples)} examples instead of 5")
            
        for ex in examples:
            if not isinstance(ex, dict):
                reasons.append("Example is not an object (probably a raw string)")
                break
            if not ex.get("en") or not ex.get("hi") or not ex.get("gu"):
                reasons.append("Missing translation in one of the examples")
                break
                
        if reasons:
            entry["audit_reasons"] = reasons
            anomalies.append(entry)
        else:
            clean_terms.append(entry)
            
    print(f"\nAudit Complete!")
    print(f"Clean terms: {len(clean_terms)}")
    print(f"Anomalies found: {len(anomalies)}")
    
    # Save anomalies
    with open(ANOMALIES_PATH, 'w', encoding='utf-8') as f:
        json.dump({"terms": anomalies}, f, indent=2, ensure_ascii=False)
    
    # Overwrite massive dict with clean terms
    data["terms"] = clean_terms
    with open(DICT_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        
    print(f"\nAnomalies saved to {ANOMALIES_PATH}")
    print(f"Clean dictionary saved to {DICT_PATH}")

if __name__ == "__main__":
    audit_dictionary()
