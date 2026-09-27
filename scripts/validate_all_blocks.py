import os
import json
import glob

CHAPTERS_DIR = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters"

def validate_json_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        if 'metadata' not in data or 'blocks' not in data:
            return f"Missing 'metadata' or 'blocks' at root level."
            
        blocks = data['blocks']
        if not isinstance(blocks, list):
            return f"'blocks' must be a list."
            
        for i, block in enumerate(blocks):
            if 'type' not in block:
                return f"Block {i} missing 'type'."
            
            # Master Directive: Data inside content:{} wrapper is a common mistake.
            if 'content' in block and isinstance(block['content'], dict):
                btype = block['type']
                if btype not in ['animated_diagram', 'presentation', 'teacher_tip', 'common_mistakes', 'nursery_rhyme']:
                    return f"Block {i} of type {btype} has illegal 'content' wrapper. Fields must be at root level."
            
            # Check for correct_answer instead of correct_index
            if 'correct_answer' in block:
                return f"Block {i} uses illegal 'correct_answer'. Must use 'correct_index' (integer)."
                
            if 'id' not in block or block['id'] == 'UNKNOWN_ID':
                return f"Block {i} missing valid 'id'."
                
        return None # Valid
        
    except json.JSONDecodeError as e:
        return f"Invalid JSON syntax: {e}"
    except Exception as e:
        return f"Error: {e}"

def main():
    print("Starting Universal JSON Validation Engine...")
    
    files = glob.glob(os.path.join(CHAPTERS_DIR, "*.json"))
    print(f"Scanning {len(files)} files...")
    
    errors = []
    for filepath in files:
        err = validate_json_file(filepath)
        if err:
            errors.append((os.path.basename(filepath), err))
            
    if errors:
        print(f"\n⚠️ FOUND ERRORS IN {len(errors)} FILES:")
        for filename, err in errors:
            print(f" - {filename}: {err}")
    else:
        print(f"\n✅ All {len(files)} JSON files successfully validated against Master Standards!")

if __name__ == "__main__":
    main()
