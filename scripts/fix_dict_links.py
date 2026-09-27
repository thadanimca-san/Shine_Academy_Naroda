#!/usr/bin/env python3
import os
import json
import glob

DICT_DIR = "app_core/knowledge_graph/dictionary"

def fix_dictionary_links():
    term_to_id = {}
    json_files = glob.glob(f"{DICT_DIR}/*.json")
    
    # 1. Build map of term name -> ID
    for file_path in json_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if 'id' in data and 'term' in data and 'english' in data['term']:
                    term_to_id[data['term']['english']] = data['id']
        except Exception:
            pass

    print(f"Loaded {len(term_to_id)} terms for mapping.")

    # 2. Fix related_terms arrays
    for file_path in json_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            modified = False
            if 'related_terms' in data and isinstance(data['related_terms'], list):
                new_related = []
                for term in data['related_terms']:
                    if term in term_to_id:
                        # Replace word with ID
                        new_related.append(term_to_id[term])
                        modified = True
                        print(f"Fixed link in {data.get('id')}: {term} -> {term_to_id[term]}")
                    elif term.startswith("ACC_DICT_"):
                        new_related.append(term)
                    else:
                        print(f"Warning: Could not find ID for related term '{term}' in {data.get('id')}")
                        # Keep it anyway, or remove it. We'll remove broken links.
                        modified = True
                
                data['related_terms'] = new_related
            
            if modified:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=4)
                    
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    fix_dictionary_links()
