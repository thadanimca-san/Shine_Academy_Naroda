import json
import glob
import os

files = glob.glob("/home/ubuntu/Shine_Academy_Naroda/app_core/learning_modules/gseb_class8_science_ch*/blocks.json")

for filepath in files:
    with open(filepath, 'r') as f:
        data = json.load(f)
        
    modified = False
    for block in data:
        if block.get("type") == "animated_diagram":
            # Extract root properties
            title = block.get("title", "Animated Diagram")
            desc = block.get("description", "")
            
            # If content is a string, it's actually the description
            content_val = block.get("content")
            if isinstance(content_val, str):
                desc = content_val
                
            # Restructure content to be a dictionary as expected by the widget
            block["content"] = {
                "title": title,
                "description": desc,
                "paths": []
            }
            
            # Clean up root
            if "description" in block:
                del block["description"]
            
            modified = True
            
    if modified:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Fixed diagrams in {filepath}")

print("Done fixing animated diagrams.")
