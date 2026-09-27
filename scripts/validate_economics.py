import json
import glob

def validate_json_files():
    files = glob.glob('app_core/chapters/cbse_class12_economics_*.json')
    if not files:
        print("No Economics files found.")
        return
        
    all_valid = True
    for file_path in files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
                # Check root structure
                if 'metadata' not in data or 'blocks' not in data:
                    print(f"ERROR in {file_path}: Missing 'metadata' or 'blocks' at root level.")
                    all_valid = False
                    continue
                    
                # Check Hindi/Gujarati translation existence
                for block in data['blocks']:
                    if 'title' in block and ('title_hi' not in block or 'title_gu' not in block):
                        print(f"ERROR in {file_path}, block {block.get('id')}: Missing title translations.")
                        all_valid = False
                    if 'body' in block and ('body_hi' not in block or 'body_gu' not in block):
                        print(f"ERROR in {file_path}, block {block.get('id')}: Missing body translations.")
                        all_valid = False
                        
            print(f"OK: {file_path}")
        except json.JSONDecodeError as e:
            print(f"JSON ERROR in {file_path}: {e}")
            all_valid = False
            
    if all_valid:
        print("\nSUCCESS: All Economics chapters validated perfectly!")
    else:
        print("\nFAILED: Validation errors found.")

if __name__ == "__main__":
    validate_json_files()
