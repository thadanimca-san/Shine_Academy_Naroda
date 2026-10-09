import json
import os
import re

CHAPTERS_DIR = "app_core/chapters"

def process_chapters():
    count_converted = 0
    for filename in os.listdir(CHAPTERS_DIR):
        if not filename.endswith(".json"):
            continue
            
        filepath = os.path.join(CHAPTERS_DIR, filename)
        
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
            
        modified = False
        new_blocks = []
        
        for block in blocks:
            if block.get("type") == "teacher_tip" and "MISSING IMAGE REQUIRED:" in block.get("body", ""):
                body = block["body"]
                # Extract filename
                match = re.search(r"MISSING IMAGE REQUIRED:\s*([^\n]+)", body)
                if match:
                    img_path = match.group(1).strip().strip("'\"")
                    
                    # Check if file exists
                    if os.path.exists(img_path):
                        print(f"  [CONVERTED] Found image {img_path} in {filename}")
                        img_block = {
                            "id": block["id"],
                            "type": "image",
                            "image_url": img_path,
                            "caption": "Image"
                        }
                        new_blocks.append(img_block)
                        modified = True
                        count_converted += 1
                        continue
                        
            new_blocks.append(block)
            
        if modified:
            if isinstance(data, list):
                data = new_blocks
            else:
                data["blocks"] = new_blocks
                
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
                
    print(f"Conversion complete! Converted {count_converted} missing image placeholders to actual images.")

if __name__ == "__main__":
    process_chapters()
