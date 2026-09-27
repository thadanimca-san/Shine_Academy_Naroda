import json
import glob

# 1. Fix animated diagram structure for Class 9
files = glob.glob("/home/ubuntu/Shine_Academy_Naroda/app_core/learning_modules/gseb_class9_science_ch*/blocks.json")

for filepath in files:
    with open(filepath, 'r') as f:
        data = json.load(f)
        
    modified = False
    for block in data:
        if block.get("type") == "animated_diagram":
            title = block.get("title", "Animated Diagram")
            desc = block.get("description", "")
            
            content_val = block.get("content")
            if isinstance(content_val, str):
                desc = content_val
                
            block["content"] = {
                "title": title,
                "description": desc,
                "paths": [
                    "M 200, 150 m -100, 0 a 100,100 0 1,0 200,0 a 100,100 0 1,0 -200,0",
                    "M 200 50 L 286 200 L 114 200 Z",
                    "M 50 150 Q 100 50, 150 150 T 250 150 T 350 150"
                ]
            }
            if "description" in block:
                del block["description"]
            
            modified = True
            
    if modified:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Fixed crashes in {filepath}")

print("Class 9 Science fixed.")
