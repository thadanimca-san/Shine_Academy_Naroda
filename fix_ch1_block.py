import json

filepath = "/home/ubuntu/Shine_Academy_Naroda/app_core/learning_modules/gseb_class8_science_ch1/blocks.json"
with open(filepath, 'r') as f:
    data = json.load(f)

for block in data:
    if block.get("type") == "animated_diagram":
        block["type"] = "theory"
        block["title"] = block.get("content", {}).get("title", "The Scientific Method")
        block["content"] = block.get("content", {}).get("description", "A stunning visualization of the scientific method.")
        block["visual_url"] = "assets/images/science_method.jpg"

with open(filepath, 'w') as f:
    json.dump(data, f, indent=2)

print("Updated Chapter 1 block to use AI-generated image!")
