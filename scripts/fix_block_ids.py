import os
import json
import uuid

def fix_blocks_json(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            blocks = json.load(f)
            
        modified = False
        if isinstance(blocks, list):
            for i, block in enumerate(blocks):
                if 'id' not in block:
                    block['id'] = f"auto_{uuid.uuid4().hex[:8]}"
                    modified = True
                    
        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(blocks, f, indent=2, ensure_ascii=False)
            print(f"Fixed missing IDs in {filepath}")
    except Exception as e:
        print(f"Error in {filepath}: {e}")

def fix_chapter_json(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        modified = False
        if 'sections' in data:
            for sec_idx, section in enumerate(data['sections']):
                if 'blocks' in section:
                    for blk_idx, block in enumerate(section['blocks']):
                        if 'id' not in block:
                            block['id'] = f"auto_{uuid.uuid4().hex[:8]}"
                            modified = True
                            
        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"Fixed missing IDs in {filepath}")
    except Exception as e:
        print(f"Error in {filepath}: {e}")

def run_fixer():
    base_dir = "app_core/learning_modules"
    print("Scanning all modules for missing block IDs...")
    
    for root, dirs, files in os.walk(base_dir):
        if "blocks.json" in files:
            fix_blocks_json(os.path.join(root, "blocks.json"))
        if "chapter.json" in files:
            fix_chapter_json(os.path.join(root, "chapter.json"))

if __name__ == "__main__":
    run_fixer()
    print("Done scanning and fixing.")
