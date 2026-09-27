import json
import sys
import os

def inject_question(json_str):
    try:
        new_q = json.loads(json_str)
    except Exception as e:
        print(f"Error parsing JSON: {e}")
        sys.exit(1)

    board_list = new_q.get("board", [])
    board = board_list[0].lower() if board_list else ""
    cls = f"class{new_q.get('class', '').strip().lower()}"
    subject = new_q.get("subject", "").strip().lower()
    ch = new_q.get("chapter_id", "").strip().lower()

    # Construct possible module IDs
    candidates = [
        f"{board}_{cls}_{subject}_{ch}",
        f"{cls}_{subject}_{ch}",
        f"{cls}_{subject.replace(' ', '_')}_{ch}",
    ]

    modules_dir = "/home/ubuntu/Shine_Academy_Naroda/app_core/learning_modules"
    target_module = None
    target_folder = None

    for candidate in candidates:
        candidate_path = os.path.join(modules_dir, candidate)
        if os.path.isdir(candidate_path):
            target_module = candidate
            target_folder = candidate_path
            break
            
    if not target_module:
        # Fallback to creating the folder if it doesn't exist
        target_module = candidates[0]
        target_folder = os.path.join(modules_dir, target_module)
        os.makedirs(target_folder, exist_ok=True)
        print(f"Created new module folder: {target_module}")

    blocks_file = os.path.join(target_folder, "blocks.json")
    
    # 1. Update blocks.json
    blocks = []
    if os.path.isfile(blocks_file):
        with open(blocks_file, 'r', encoding='utf-8') as f:
            try:
                blocks = json.load(f)
                if not isinstance(blocks, list):
                    if isinstance(blocks, dict) and "blocks" in blocks:
                        blocks = blocks["blocks"]
                    else:
                        blocks = []
            except json.JSONDecodeError:
                blocks = []

    blocks.append(new_q)
    
    with open(blocks_file, 'w', encoding='utf-8') as f:
        json.dump(blocks, f, indent=2, ensure_ascii=False)
        
    print(f"Added to {blocks_file}")

    # 2. Update master_curriculum.json
    master_file = os.path.join(modules_dir, "master_curriculum.json")
    if os.path.isfile(master_file):
        with open(master_file, 'r', encoding='utf-8') as f:
            try:
                master_data = json.load(f)
            except Exception:
                master_data = {}
                
        if target_module not in master_data:
            master_data[target_module] = {"metadata": {}, "blocks": []}
            
        master_data[target_module]["blocks"] = blocks
        
        with open(master_file, 'w', encoding='utf-8') as f:
            json.dump(master_data, f, indent=2, ensure_ascii=False)
            
        print(f"Synced {target_module} to master_curriculum.json")
    else:
        print("master_curriculum.json not found!")

    # 3. Update app_core/chapters file (for Gold Standard Chapter View)
    chapters_dir = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters"
    chapter_file = os.path.join(chapters_dir, f"{target_module}.json")
    if os.path.isfile(chapter_file):
        with open(chapter_file, 'r', encoding='utf-8') as f:
            try:
                chapter_data = json.load(f)
            except Exception:
                chapter_data = {}
                
        # The chapter file usually has 'content' or 'blocks'
        if "content" in chapter_data:
            chapter_data["content"].append(new_q)
        elif "blocks" in chapter_data:
            chapter_data["blocks"].append(new_q)
        else:
            chapter_data["blocks"] = [new_q]
            
        with open(chapter_file, 'w', encoding='utf-8') as f:
            json.dump(chapter_data, f, indent=2, ensure_ascii=False)
            
        print(f"Synced {target_module} to chapters folder")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the JSON string as an argument.")
        sys.exit(1)
        
    json_input = sys.argv[1]
    inject_question(json_input)
