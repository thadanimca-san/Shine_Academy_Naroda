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
        time.sleep(0.5) 
        return translator.translate(text, src='en', dest=dest_lang).text
    except Exception as e:
        print(f"      [!] Translation failed: {e}")
        return text

def process_dictionary_file(file_path):
    print(f"\nScanning Dictionary: {os.path.basename(file_path)}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except Exception as e:
            print(f"  [X] Failed to load JSON: {e}")
            return False

    needs_save = False
    
    # 1. Translate Definitions
    if 'definition' in data:
        df = data['definition']
        
        # Simple Definition
        if 'simple' in df:
            if 'simple_hi' not in df:
                print("      -> Translating simple definition to Hindi...")
                df['simple_hi'] = safe_translate(df['simple'], 'hi')
                needs_save = True
            if 'simple_gu' not in df:
                print("      -> Translating simple definition to Gujarati...")
                df['simple_gu'] = safe_translate(df['simple'], 'gu')
                needs_save = True
                
        # Academic Definition
        if 'academic' in df:
            if 'academic_hi' not in df:
                print("      -> Translating academic definition to Hindi...")
                df['academic_hi'] = safe_translate(df['academic'], 'hi')
                needs_save = True
            if 'academic_gu' not in df:
                print("      -> Translating academic definition to Gujarati...")
                df['academic_gu'] = safe_translate(df['academic'], 'gu')
                needs_save = True

    # 2. Translate Examples List
    if 'examples' in data and isinstance(data['examples'], list) and len(data['examples']) > 0:
        if 'examples_hi' not in data or len(data['examples_hi']) != len(data['examples']):
            print("      -> Translating examples to Hindi...")
            data['examples_hi'] = [safe_translate(ex, 'hi') for ex in data['examples']]
            needs_save = True
        if 'examples_gu' not in data or len(data['examples_gu']) != len(data['examples']):
            print("      -> Translating examples to Gujarati...")
            data['examples_gu'] = [safe_translate(ex, 'gu') for ex in data['examples']]
            needs_save = True

    # 3. Translate AI Context
    if 'ai_context' in data:
        ac = data['ai_context']
        
        # Tutor Hint
        if 'tutor_hint' in ac:
            if 'tutor_hint_hi' not in ac:
                print("      -> Translating tutor hint to Hindi...")
                ac['tutor_hint_hi'] = safe_translate(ac['tutor_hint'], 'hi')
                needs_save = True
            if 'tutor_hint_gu' not in ac:
                print("      -> Translating tutor hint to Gujarati...")
                ac['tutor_hint_gu'] = safe_translate(ac['tutor_hint'], 'gu')
                needs_save = True
                
        # Misconceptions
        if 'common_misconceptions' in ac and isinstance(ac['common_misconceptions'], list) and len(ac['common_misconceptions']) > 0:
            if 'common_misconceptions_hi' not in ac or len(ac['common_misconceptions_hi']) != len(ac['common_misconceptions']):
                print("      -> Translating misconceptions to Hindi...")
                ac['common_misconceptions_hi'] = [safe_translate(mc, 'hi') for mc in ac['common_misconceptions']]
                needs_save = True
            if 'common_misconceptions_gu' not in ac or len(ac['common_misconceptions_gu']) != len(ac['common_misconceptions']):
                print("      -> Translating misconceptions to Gujarati...")
                ac['common_misconceptions_gu'] = [safe_translate(mc, 'gu') for mc in ac['common_misconceptions']]
                needs_save = True

    # Save if modified
    if needs_save:
        print(f"  [💾] Saving translations for {os.path.basename(file_path)}...")
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write('\n')
        return True
    else:
        print("  [✓] Dictionary file is fully translated.")
        return False

def main():
    print("==================================================================")
    print("OFFLINE DICTIONARY FIXER: TRANSLATING DEFINITIONS & EXAMPLES")
    print("==================================================================")
    print("Press Ctrl+C at any time to safely stop. Progress is saved per file.")
    
    files = glob.glob('app_core/knowledge_graph/dictionary/*.json')
    total_files = len(files)
    fixed_files = 0
    
    for i, file_path in enumerate(files):
        print(f"\n--- Progress: {i+1}/{total_files} ---")
        try:
            if process_dictionary_file(file_path):
                fixed_files += 1
        except KeyboardInterrupt:
            print("\n\n[🛑] Script paused by user! Progress saved.")
            return
            
    print("\n==================================================================")
    print(f"FINISHED! Successfully translated definitions in {fixed_files} dictionary files.")
    print("==================================================================")

if __name__ == "__main__":
    main()
