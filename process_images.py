import json
import csv
import os
import glob
import shutil

# 1. Read science_image_prompts.csv and map prompt text to row number
prompt_to_row = {}
with open('science_image_prompts.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    row_num = 2
    for row in reader:
        if len(row) > 7:
            # The prompt is the last non-empty column?
            prompt = ""
            for col in reversed(row):
                if col.strip():
                    prompt = col.strip()
                    break
            if prompt:
                prompt_to_row[prompt] = row_num
        row_num += 1

print(f"Loaded {len(prompt_to_row)} prompts from CSV")

# 2. Scan all JSON files in app_core/chapters/
json_files = glob.glob('app_core/chapters/*.json')
tasks = [] # list of (json_file, block_index, asset_path, prompt)

for jf in json_files:
    try:
        with open(jf, 'r', encoding='utf-8') as f:
            blocks = json.load(f)
        
        # If it's a dict, check if it has a 'learning_blocks' key
        if isinstance(blocks, dict):
            if 'learning_blocks' in blocks:
                blocks = blocks['learning_blocks']
            elif 'blocks' in blocks:
                blocks = blocks['blocks']
            else:
                blocks = [blocks] # fallback
                
        if not isinstance(blocks, list):
            print(f"Skipping {jf}, root is not a list")
            continue

        for i, b in enumerate(blocks):
            if isinstance(b, dict) and b.get('type') == 'teacher_tip' and b.get('title') in ['Image Required', 'छवि आवश्यक है']:
                body = b.get('body', '')
                if 'MISSING IMAGE REQUIRED: ' in body and 'PROMPT FOR GEMINI:\n' in body:
                    parts = body.split('PROMPT FOR GEMINI:\n')
                    if len(parts) == 2:
                        asset_path = parts[0].replace('MISSING IMAGE REQUIRED: ', '').strip()
                        prompt = parts[1].strip()
                        tasks.append((jf, i, asset_path, prompt))
    except Exception as e:
        print(f"Error parsing {jf}: {e}")

print(f"Found {len(tasks)} missing image placeholders in JSON files.")

# 3. Match and replace
replaced_count = 0
missing_images = []

for jf, i, asset_path, prompt in tasks:
    # Check if this prompt is in the CSV
    matched_row = None
    for p, row_num in prompt_to_row.items():
        if p[:50] in prompt or prompt[:50] in p: # partial match just in case
            matched_row = row_num
            break
            
    if matched_row and os.path.exists(f"science_images_from_prompts/image from row {matched_row}.png"):
        # Copy image
        src = f"science_images_from_prompts/image from row {matched_row}.png"
        dest = asset_path
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.copy(src, dest)
        # print(f"Copied {src} to {dest}")
        
        # We need to update the JSON
        with open(jf, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        data[i] = {
            "type": "animated_diagram",
            "asset_path": dest
        }
        
        with open(jf, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        replaced_count += 1
    else:
        # We still need to replace it with an animated_diagram pointing to the asset_path
        # But we record it as missing so we can assign it to a subagent
        missing_images.append({
            "json_file": jf,
            "asset_path": asset_path,
            "prompt": prompt
        })
        
        # Replace the placeholder in the JSON anyway so the app is clean
        with open(jf, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        data[i] = {
            "type": "animated_diagram",
            "asset_path": asset_path
        }
        
        with open(jf, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Replaced {replaced_count} placeholders using existing images.")
print(f"There are {len(missing_images)} missing images to generate via subagents.")

with open('missing_images_tasks.json', 'w', encoding='utf-8') as f:
    json.dump(missing_images, f, indent=2)

