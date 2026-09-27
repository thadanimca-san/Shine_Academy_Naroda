import os
import json

TARGET_DIR = 'app_core/content_database/cbse_class10_maths'
INDEX_FILE = os.path.join(TARGET_DIR, 'index.json')

def main():
    chapters = []
    
    if not os.path.exists(TARGET_DIR):
        print(f"Directory {TARGET_DIR} not found.")
        return
        
    for f_name in sorted(os.listdir(TARGET_DIR)):
        if f_name.endswith('.json') and f_name != 'index.json':
            filepath = os.path.join(TARGET_DIR, f_name)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    
                meta = data.get('metadata', {})
                chapters.append({
                    'id': meta.get('id', ''),
                    'title': meta.get('title', f_name),
                    'file': f_name
                })
            except Exception as e:
                print(f"Error parsing {f_name}: {e}")
                
    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        json.dump(chapters, f, indent=2)
        
    print(f"Index created at {INDEX_FILE} with {len(chapters)} chapters.")

if __name__ == '__main__':
    main()
