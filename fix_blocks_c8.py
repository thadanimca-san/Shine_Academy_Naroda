import os
import json
import glob

base_dir = "/home/ubuntu/Shine_Academy_Naroda/app_core/learning_modules"
pattern = os.path.join(base_dir, "gseb_class8_science_ch*", "blocks.json")

def fix_file(filepath):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            
        if isinstance(data, dict):
            if "blocks" in data:
                data = data["blocks"]
            else:
                data = [data]
                
        if not isinstance(data, list):
            return
            
        # Allowed block types in flutter
        allowed_types = ["theory", "dictionary_link", "real_world_example", "animated_diagram", "quiz", "history", "memory_trick", "summary"]
        
        fixed_data = []
        for block in data:
            if not isinstance(block, dict):
                continue
            t = block.get("type", "")
            if t == "mcq":
                block["type"] = "quiz"
            if block.get("type") in allowed_types:
                fixed_data.append(block)
                
        with open(filepath, 'w') as f:
            json.dump(fixed_data, f, indent=2)
            
        print(f"Fixed {filepath}")
        
    except Exception as e:
        print(f"Error on {filepath}: {e}")

for fp in glob.glob(pattern):
    fix_file(fp)
