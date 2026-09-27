import json
import glob
import os

def check_kaamchori():
    files = glob.glob('app_core/chapters/*class12*.json')
    if not files:
        print("No Class 12 files found.")
        return

    print("=========================================================")
    print("GLOBAL KAAMCHORI AUDIT: CLASS 12 (GSEB & CBSE)")
    print("=========================================================\n")

    total_chapters = len(files)
    total_blocks_scanned = 0
    kaamchori_findings = []
    
    for file_path in files:
        filename = os.path.basename(file_path)
        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except Exception as e:
                kaamchori_findings.append(f"❌ [FATAL ERROR] {filename}: Invalid JSON format ({e})")
                continue
                
            if isinstance(data, list):
                blocks = data
                # It's an old file format, which is also a form of kaamchori!
                kaamchori_findings.append(f"❌ [OLD FORMAT] {filename}: Root level is an array. Must be a Map {{metadata: ..., blocks: [...]}}")
            else:
                blocks = data.get('blocks', [])
            total_blocks_scanned += len(blocks)
            
            # Rule 1: Too few blocks (Less than 10 blocks for a Class 12 chapter is kaamchori)
            if len(blocks) < 10:
                kaamchori_findings.append(f"🚩 [SHORT CHAPTER] {filename}: Only {len(blocks)} blocks. (Class 12 board chapters should have 30+ blocks including all textbook exercises).")
                
            missing_translations = 0
            lazy_options = 0
            missing_solutions = 0
            
            for block in blocks:
                block_id = block.get('id', 'UNKNOWN')
                
                # Rule 2: Missing Translations
                keys_to_translate = [k for k, v in block.items() if isinstance(v, str) and not k.endswith('_hi') and not k.endswith('_gu') and k not in ['id', 'type', 'media_url']]
                for k in keys_to_translate:
                    if (k + '_hi') not in block or (k + '_gu') not in block:
                        missing_translations += 1
                        
                # Rule 3: Lazy Options
                if 'options' in block:
                    options = block['options']
                    for opt in options:
                        if opt.lower().strip() in ['option a', 'option b', 'option c', 'option d', 'option 1', 'option 2']:
                            lazy_options += 1
                            
                # Rule 4: Missing Solutions
                if block.get('type') == 'practice_question' or block.get('type') == 'numerical':
                    if 'solution' not in block or len(block['solution']) < 20: # Solution is missing or suspiciously short
                        missing_solutions += 1

            # Report for the chapter if there's any kaamchori
            if missing_translations > 0 or lazy_options > 0 or missing_solutions > 0:
                report = f"⚠️ [KAAMCHORI DETECTED] {filename}:\n"
                if missing_translations > 0:
                    report += f"   - Missing Hindi/Gujarati translations in {missing_translations} fields.\n"
                if lazy_options > 0:
                    report += f"   - Lazy MCQ Options ('Option A/B') found {lazy_options} times.\n"
                if missing_solutions > 0:
                    report += f"   - Missing or very short solutions in {missing_solutions} numerical questions.\n"
                kaamchori_findings.append(report)

    print(f"Scanned {total_chapters} chapters and {total_blocks_scanned} total blocks.\n")
    
    if not kaamchori_findings:
        print("✅ AMAZING! Zero kaamchori detected. All Class 12 data is Gold Standard.")
    else:
        for finding in kaamchori_findings:
            print(finding)
            
    print("\n=========================================================")
    print(f"Total Issues Found: {len(kaamchori_findings)}")

if __name__ == "__main__":
    check_kaamchori()
