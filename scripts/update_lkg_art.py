import json
import os

def update_lkg_art_shapes():
    print("Updating LKG Art chapters 1-5...")
    
    shapes = {
        1: "tree",
        2: "house",
        3: "rainbow",
        4: "ball",
        5: "cat"
    }
    
    updated_count = 0
    
    for i in range(1, 6):
        filepath = f"app_core/chapters/lkg_art_ch{i}.json"
        
        if not os.path.exists(filepath):
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        shape_name = shapes[i]
        
        # Update title and hook title
        data["metadata"]["title"] = f"Color the {shape_name.capitalize()}"
        
        for block in data.get("blocks", []):
            if block.get("type") == "color_canvas":
                block["shape"] = shape_name
            if block.get("type") == "hook":
                block["title"] = "Time for Magic!"
                block["body"] = f"Let's bring this {shape_name} to life with some beautiful colors!"
            if block.get("type") == "quiz":
                block["question"] = f"Did you enjoy coloring the {shape_name}?"
                block["options"] = ["Yes! I love it!", "It was okay."]
                
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            
        updated_count += 1
        
    print(f"Updated {updated_count} LKG Art chapters.")

if __name__ == "__main__":
    update_lkg_art_shapes()
