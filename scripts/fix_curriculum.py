import json

def fix_curriculum():
    file_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/curriculum/gseb_class12_commerce.json"
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    for subject in data.get('subjects', []):
        if 'chapters' in subject:
            # Filter out any chapter where module_id ends with _gu
            # but keep "guj" as it's the Gujarati language subject
            original_len = len(subject['chapters'])
            subject['chapters'] = [
                ch for ch in subject['chapters']
                if not ch.get('module_id', '').endswith('_gu')
            ]
            new_len = len(subject['chapters'])
            if original_len != new_len:
                print(f"Removed {original_len - new_len} duplicate _gu chapters from {subject.get('name')}")

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print("Fixed curriculum file!")

if __name__ == "__main__":
    fix_curriculum()
