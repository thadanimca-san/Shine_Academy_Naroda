import json
import glob

files = glob.glob("/home/ubuntu/Shine_Academy_Naroda/app_core/learning_modules/gseb_class8_science_ch*/blocks.json")

# Some cool geometric paths
circle_path = "M 200, 150 m -100, 0 a 100,100 0 1,0 200,0 a 100,100 0 1,0 -200,0"
triangle_path = "M 200 50 L 286 200 L 114 200 Z"
sine_path = "M 50 150 Q 100 50, 150 150 T 250 150 T 350 150"
dna_path = "M 50 50 Q 100 150, 150 50 T 250 50 T 350 50"

default_paths = [circle_path, triangle_path, sine_path, dna_path]

for filepath in files:
    modified = False
    with open(filepath, 'r') as f:
        data = json.load(f)
        
    for block in data:
        if block.get("type") == "animated_diagram":
            content = block.get("content", {})
            if isinstance(content, dict):
                content["paths"] = default_paths
                modified = True
                
    if modified:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Injected SVG animations into {filepath}")

print("Done injecting SVGs.")
