import json
import os
import glob

def fix_all_curriculums():
    files = glob.glob('/home/ubuntu/Shine_Academy_Naroda/app_core/curriculum/*.json')
    
    subject_colors = {
        "maths": "0xFF2196F3",
        "science": "0xFF4CAF50",
        "english": "0xFFE91E63",
        "social_science": "0xFFFF9800",
        "social": "0xFFFF9800",
        "hindi": "0xFF9C27B0",
        "gujarati": "0xFF00BCD4",
        "sanskrit": "0xFF795548",
        "computer": "0xFF607D8B",
        "physics": "0xFF3F51B5",
        "chemistry": "0xFF009688",
        "biology": "0xFF8BC34A",
        "account": "0xFF4CAF50",
        "statistics": "0xFF3F51B5",
        "economics": "0xFFFF9800",
        "oc": "0xFF9C27B0",
        "spcc": "0xFF795548",
    }
    
    subject_icons = {
        "maths": "calculate",
        "science": "science",
        "english": "language",
        "social_science": "public",
        "social": "public",
        "hindi": "translate",
        "gujarati": "translate",
        "sanskrit": "menu_book",
        "computer": "computer",
        "physics": "bolt",
        "chemistry": "biotech",
        "biology": "psychology",
        "account": "account_balance",
        "statistics": "bar_chart",
        "economics": "timeline",
        "oc": "business",
        "spcc": "assignment",
    }
    
    count = 0
    for file_path in files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            if not isinstance(data, dict) or 'subjects' not in data:
                continue
                
            modified = False
            for subject in data.get('subjects', []):
                sid = subject.get('id', '').lower()
                
                # Guess the category to assign right colors
                cat = sid
                for k in subject_colors.keys():
                    if k in sid:
                        cat = k
                
                if 'color_hex' not in subject:
                    subject['color_hex'] = subject_colors.get(cat, "0xFF607D8B")
                    modified = True
                if 'icon' not in subject:
                    subject['icon'] = subject_icons.get(cat, "menu_book")
                    modified = True
                    
            if modified:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                print(f"Fixed missing colors in {os.path.basename(file_path)}")
                count += 1
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            
    print(f"Successfully fixed {count} curriculum files.")

if __name__ == '__main__':
    fix_all_curriculums()
