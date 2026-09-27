import json
import os
import glob
import time
try:
    from googletrans import Translator
except ImportError:
    print("Please install googletrans first: pip install googletrans==4.0.0-rc1")
    exit(1)

translator = Translator()

def safe_translate(text, dest_lang):
    if not text or len(text.strip()) == 0:
        return ""
    try:
        # Adding a small delay to avoid Google Translate rate limits
        time.sleep(0.5) 
        return translator.translate(text, src='en', dest=dest_lang).text
    except Exception as e:
        print(f"      [!] Translation failed for '{text[:20]}...': {e}")
        # Return the original text so we don't lose data, or leave it blank to retry later
        return text

def process_file(file_path):
    print(f"\nScanning: {os.path.basename(file_path)}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except Exception as e:
            print(f"  [X] Failed to load JSON: {e}")
            return False

    needs_save = False
    
    # 1. FIX OLD FORMAT KAMCHORI (List to Dict)
    if isinstance(data, list):
        print("  [*] Found old array format. Converting to standard Map format...")
        new_data = {
            "metadata": {
                "id": os.path.basename(file_path).replace('.json', '').upper(),
                "title": "Converted Chapter",
                "title_hi": "परिवर्तित अध्याय",
                "title_gu": "રૂપાંતરિત પ્રકરણ",
                "subject": "Unknown",
                "class": "Class 12",
                "board": "Unknown"
            },
            "blocks": data
        }
        data = new_data
        needs_save = True

    blocks = data.get('blocks', [])
    
    # 2. FIX MISSING TRANSLATIONS (Hindi & Gujarati)
    blocks_translated_count = 0
    for block in blocks:
        block_modified = False
        keys_to_translate = [k for k, v in block.items() if isinstance(v, str) and not k.endswith('_hi') and not k.endswith('_gu') and k not in ['id', 'type', 'media_url']]
        
        for key in keys_to_translate:
            val = block[key]
            if not val:
                continue
                
            # Check for Hindi
            if (key + '_hi') not in block:
                print(f"      -> Translating {key} to Hindi...")
                block[key + '_hi'] = safe_translate(val, 'hi')
                block_modified = True
                
            # Check for Gujarati
            if (key + '_gu') not in block:
                print(f"      -> Translating {key} to Gujarati...")
                block[key + '_gu'] = safe_translate(val, 'gu')
                block_modified = True
                
        # Handle MCQ Options
        if 'options' in block:
            options = block['options']
            
            if 'options_hi' not in block or len(block['options_hi']) != len(options):
                print(f"      -> Translating MCQ options to Hindi...")
                block['options_hi'] = [safe_translate(opt, 'hi') for opt in options]
                block_modified = True
                
            if 'options_gu' not in block or len(block['options_gu']) != len(options):
                print(f"      -> Translating MCQ options to Gujarati...")
                block['options_gu'] = [safe_translate(opt, 'gu') for opt in options]
                block_modified = True

        if block_modified:
            blocks_translated_count += 1
            needs_save = True

    if blocks_translated_count > 0:
        print(f"  [+] Fixed missing translations in {blocks_translated_count} blocks.")

    # 3. SAVE IMMEDIATELY (Makes script resumable!)
    if needs_save:
        print(f"  [💾] Saving progress for {os.path.basename(file_path)}...")
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write('\n')
        return True
    else:
        print("  [✓] File is already perfect. No kaamchori found.")
        return False

def main():
    print("==================================================================")
    print("RESUMABLE OFFLINE AUTO-FIXER: TRANSLATIONS & JSON FORMATTING")
    print("==================================================================")
    print("Press Ctrl+C at any time to safely stop. Progress is saved per file.")
    print("When you run this again, it will skip files that are already perfect.\n")
    
    files = glob.glob('app_core/chapters/*.json')
    total_files = len(files)
    fixed_files = 0
    
    for i, file_path in enumerate(files):
        print(f"\n--- Progress: {i+1}/{total_files} ---")
        try:
            was_fixed = process_file(file_path)
            if was_fixed:
                fixed_files += 1
        except KeyboardInterrupt:
            print("\n\n[🛑] Script paused by user! Progress up to the last file is saved safely.")
            print("Just run the script again later to resume.")
            return
            
    print("\n==================================================================")
    print(f"FINISHED! Successfully fixed and translated {fixed_files} files.")
    print("==================================================================")

if __name__ == "__main__":
    main()
