import json

def update_ukg_art():
    print("Fixing UKG Art Chapters...")
    
    # The actual shapes needed for UKG based on ukg.json
    shapes = ["boat", "scenery", "dog", "hand", "face"]
    
    for i in range(1, 6):
        filepath = f"app_core/chapters/ukg_art_ch{i}.json"
        
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        shape_name = shapes[i-1]
        
        # We know there's a color_canvas block from the previous upgrade
        for block in data.get("blocks", []):
            if block.get("type") == "color_canvas":
                block["shape"] = shape_name
                
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            
    print("Successfully fixed UKG Art!")

if __name__ == "__main__":
    update_ukg_art()
