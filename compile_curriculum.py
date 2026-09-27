import os
import json

def compile_curriculum():
    base_path = 'app_core/learning_modules'
    output_file = 'app_core/learning_modules/master_curriculum.json'
    
    if not os.path.exists(base_path):
        print(f"Error: {base_path} does not exist.")
        return

    master_db = {}
    
    for folder in os.listdir(base_path):
        folder_path = os.path.join(base_path, folder)
        
        # Only process directories
        if not os.path.isdir(folder_path):
            continue
            
        blocks_path = os.path.join(folder_path, 'blocks.json')
        meta_path = os.path.join(folder_path, 'metadata.json')
        
        # We only care about modules that have a blocks.json
        if os.path.exists(blocks_path):
            try:
                with open(blocks_path, 'r', encoding='utf-8') as f:
                    blocks_data = json.load(f)
                
                meta_data = {}
                if os.path.exists(meta_path):
                    with open(meta_path, 'r', encoding='utf-8') as f:
                        meta_data = json.load(f)
                        
                master_db[folder] = {
                    "metadata": meta_data,
                    "blocks": blocks_data
                }
            except Exception as e:
                print(f"Warning: Failed to parse {folder}: {e}")

    # Write the master database
    with open(output_file, 'w', encoding='utf-8') as f:
        # We use indent=None and separators to minify the json and save space
        json.dump(master_db, f, separators=(',', ':'))
        
    print(f"Successfully compiled {len(master_db)} modules into {output_file}")
    print(f"Database size: {os.path.getsize(output_file) / 1024:.2f} KB")

if __name__ == "__main__":
    compile_curriculum()
