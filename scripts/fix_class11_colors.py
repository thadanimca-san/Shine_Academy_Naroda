import json
import os

def fix_class11_curriculum():
    file_path = '/home/ubuntu/Shine_Academy_Naroda/app_core/curriculum/gseb_class11.json'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    subject_colors = {
        "gseb_class11_statistics": "0xFF3F51B5",
        "gseb_class11_economics": "0xFFFF9800",
        "gseb_class11_oc": "0xFF9C27B0",
        "gseb_class11_english": "0xFFE91E63",
        "gseb_class11_gujarati": "0xFF00BCD4",
        "gseb_class11_spcc": "0xFF795548",
        "gseb_class11_accounts": "0xFF4CAF50",
    }
    
    subject_icons = {
        "gseb_class11_statistics": "bar_chart",
        "gseb_class11_economics": "timeline",
        "gseb_class11_oc": "business",
        "gseb_class11_english": "language",
        "gseb_class11_gujarati": "translate",
        "gseb_class11_spcc": "assignment",
        "gseb_class11_accounts": "account_balance",
    }

    for subject in data.get('subjects', []):
        sid = subject.get('id')
        if 'color_hex' not in subject:
            subject['color_hex'] = subject_colors.get(sid, "0xFF607D8B")
        if 'icon' not in subject:
            subject['icon'] = subject_icons.get(sid, "menu_book")
            
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        
    print("Class 11 curriculum fixed.")

if __name__ == '__main__':
    fix_class11_curriculum()
