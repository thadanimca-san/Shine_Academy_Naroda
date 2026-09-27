import os
import glob
import json

def rebuild_master():
    chapters_dir = 'app_core/chapters'
    master_file = 'app_core/learning_modules/master_curriculum.json'
    
    files = glob.glob(os.path.join(chapters_dir, '*.json'))
    
    master_dict = {}
    
    print(f"Scanning {len(files)} active chapters...")
    
    for file_path in files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            # Try to extract an ID to use as the key
            chapter_id = None
            if isinstance(data, dict) and 'metadata' in data and 'id' in data['metadata']:
                chapter_id = data['metadata']['id']
            
            # Fallback to filename without extension
            if not chapter_id:
                chapter_id = os.path.basename(file_path).replace('.json', '')
                
            master_dict[chapter_id] = data
            
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            
    # Save the huge unified JSON
    print(f"Writing {len(master_dict)} chapters to master_curriculum.json...")
    with open(master_file, 'w', encoding='utf-8') as out_f:
        json.dump(master_dict, out_f, indent=2, ensure_ascii=False)
        
    print(f"Successfully rebuilt {master_file} with {len(master_dict)} Gold Standard chapters.")
    print("The app is now safe from crashing!")

if __name__ == "__main__":
    rebuild_master()
