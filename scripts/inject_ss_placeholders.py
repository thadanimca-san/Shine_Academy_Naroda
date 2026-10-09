import json
import csv
import os
import re

# Constants
CSV_FILE = "ncert_social_science_prompts.csv"
CHAPTERS_DIR = "app_core/chapters"
IMAGES_DIR = "assets/images/social_science"

def sanitize_filename(filename):
    # Keep alphanumeric, replace space with underscore
    clean = re.sub(r'[^a-zA-Z0-9\s]', '', filename)
    clean = clean.replace(' ', '_').lower()
    return clean

def load_prompts():
    # Read science_image_prompts.csv
    prompts_by_file = {}
    with open(CSV_FILE, mode="r", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        for row in reader:
            if not row or len(row) < 4:
                continue
            
            chapter_file = row[0].strip()
            if not chapter_file.endswith(".json"):
                continue
                
            concept = row[2].strip()
            prompt = row[3].strip()
            
            if chapter_file not in prompts_by_file:
                prompts_by_file[chapter_file] = []
                
            prompts_by_file[chapter_file].append({
                "concept": concept,
                "prompt": prompt
            })
            
    return prompts_by_file

def fuzzy_match(concept, block):
    # Check if words from concept are in the block body or title
    concept_words = [w.lower() for w in concept.split() if len(w) > 3]
    if not concept_words:
        return False
        
    text_to_search = ""
    for key in ["title", "body", "question", "front"]:
        if key in block and isinstance(block[key], str):
            text_to_search += block[key].lower() + " "
            
    matches = sum(1 for w in concept_words if w in text_to_search)
    return matches >= 1

def process_chapters():
    prompts_by_file = load_prompts()
    
    for filename in os.listdir(CHAPTERS_DIR):
        is_ss = filename.startswith("ncert_class10_") and any(s in filename for s in ["history", "geography", "civics", "economics"])
        if not (is_ss and filename.endswith(".json")):
            continue
            
        filepath = os.path.join(CHAPTERS_DIR, filename)
        if filename not in prompts_by_file:
            print(f"Skipping {filename}, no prompts found.")
            continue
            
        print(f"Processing {filename}...")
        
        with open(filepath, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except Exception as e:
                print(f"Failed to load {filename}: {e}")
                continue
                
        if isinstance(data, list):
            blocks = data
        else:
            blocks = data.get("blocks", [])
            
        new_blocks = []
        
        prompts_to_inject = prompts_by_file[filename].copy()
        
        ch_num_match = re.search(r'ch(\d+)', filename)
        ch_num = ch_num_match.group(1) if ch_num_match else "X"
        
        subj_match = re.search(r'class10_([a-z_]+)_ch', filename)
        subj = subj_match.group(1) if subj_match else "ss"
        
        for i, block in enumerate(blocks):
            new_blocks.append(block)
            
            matched_prompt = None
            for p in prompts_to_inject:
                if fuzzy_match(p["concept"], block):
                    matched_prompt = p
                    break
                    
            if matched_prompt:
                prompts_to_inject.remove(matched_prompt)
                
                concept_clean = sanitize_filename(matched_prompt['concept'])
                img_filename = f"class10_{subj}_ch{ch_num}_{concept_clean}.png"
                img_path = os.path.join(IMAGES_DIR, img_filename)
                
                # Check if image already exists in block (very naive check)
                if "image_url" in block:
                    continue
                
                if os.path.exists(img_path):
                    img_block = {
                        "id": f"{block['id']}_IMG",
                        "type": "image",
                        "image_url": f"assets/images/social_science/{img_filename}",
                        "caption": matched_prompt['concept']
                    }
                    new_blocks.append(img_block)
                    print(f"  [+] Injected IMAGE block for '{matched_prompt['concept']}'")
                else:
                    body_msg = f"MISSING IMAGE REQUIRED: assets/images/social_science/{img_filename}\n\nPROMPT FOR GEMINI:\n{matched_prompt['prompt']}"
                    tip_block = {
                        "id": f"{block['id']}_MISSING_IMG",
                        "type": "teacher_tip",
                        "title": "Image Required",
                        "body": body_msg,
                        "title_hi": "छवि आवश्यक है",
                        "body_hi": body_msg,
                        "title_gu": "છબી જરૂરી છે",
                        "body_gu": body_msg
                    }
                    new_blocks.append(tip_block)
                    print(f"  [!] Injected MISSING IMAGE tip for '{matched_prompt['concept']}'")
                    
        for p in prompts_to_inject:
            concept_clean = sanitize_filename(p['concept'])
            img_filename = f"class10_{subj}_ch{ch_num}_{concept_clean}.png"
            body_msg = f"MISSING IMAGE REQUIRED: assets/images/social_science/{img_filename}\n\nPROMPT FOR GEMINI:\n{p['prompt']}"
            tip_block = {
                "id": f"KOBJ_NCERT_C10_{subj.upper()}_CH{ch_num}_END_IMG_{len(new_blocks)}",
                "type": "teacher_tip",
                "title": "Image Required (Unmatched)",
                "body": body_msg,
                "title_hi": "छवि आवश्यक है",
                "body_hi": body_msg,
                "title_gu": "છબી જરૂરી છે",
                "body_gu": body_msg
            }
            new_blocks.append(tip_block)
            print(f"  [?] Appended unmatched MISSING IMAGE tip for '{p['concept']}'")
            
        if isinstance(data, list):
            data = new_blocks
        else:
            data["blocks"] = new_blocks
        
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
    print("Done processing chapters.")

if __name__ == "__main__":
    process_chapters()
