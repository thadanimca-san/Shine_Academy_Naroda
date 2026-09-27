import os
import json
import glob

def fix_routing_loopholes():
    directory = 'app_core/learning_modules'
    json_files = glob.glob(os.path.join(directory, '*_chapters.json'))
    
    total_files_fixed = 0
    total_chapters_fixed = 0
    
    for filepath in json_files:
        # e.g., filepath = "app_core/learning_modules/gseb_class9_science_chapters.json"
        filename = os.path.basename(filepath)
        
        # e.g., prefix = "gseb_class9_science"
        prefix = filename.replace('_chapters.json', '')
        
        with open(filepath, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except Exception as e:
                print(f"Error loading {filepath}: {e}")
                continue
                
        if 'chapters' not in data:
            continue
            
        modified = False
        for chapter in data['chapters']:
            num = chapter.get('number')
            if num is None:
                continue
                
            expected_id = f"{prefix}_ch{num}"
            expected_route = f"/learning_engine/{expected_id}"
            
            if chapter.get('id') != expected_id or chapter.get('route') != expected_route:
                chapter['id'] = expected_id
                if 'route' in chapter:
                    chapter['route'] = expected_route
                modified = True
                total_chapters_fixed += 1
                
        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            total_files_fixed += 1
            
    print(f"Routing Loophole Closed. Fixed {total_chapters_fixed} chapters across {total_files_fixed} index files.")

if __name__ == '__main__':
    fix_routing_loopholes()
