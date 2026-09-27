import json
import os

curriculum_dir = '/home/ubuntu/Shine_Academy_Naroda/app_core/curriculum'

subjects_to_add = [
    {
        "id_suffix": "_hindi",
        "name": "Hindi (Second Language)",
        "color_hex": "0xFFE91E63",
        "icon": "translate",
        "chapters": [
            "Chapter 1: Prabhuji Tum Chandan Hum Pani",
            "Chapter 2: Meera Ke Pad",
            "Chapter 3: Savaiye",
            "Chapter 4: Ek Kutta Aur Ek Maina",
            "Chapter 5: Tota",
            "Chapter 6: Mahadevi Varma - Gilu",
            "Chapter 7: Surdas Ke Pad",
            "Chapter 8: Niti Ke Dohe",
            "Chapter 9: Kutta Aur Parchhai",
            "Chapter 10: Jeene Ki Kala"
        ]
    },
    {
        "id_suffix": "_gujarati",
        "name": "Gujarati (Second Language)",
        "color_hex": "0xFFFF9800",
        "icon": "auto_stories",
        "chapters": [
            "Chapter 1: Morli",
            "Chapter 2: Vaishnavjan To Tene Kahiye",
            "Chapter 3: Shilvant Sadhune",
            "Chapter 4: Dikri",
            "Chapter 5: Vatanthi Viday Thata",
            "Chapter 6: Boliye Na Kain",
            "Chapter 7: Jeev Ma Jeev Aavyo",
            "Chapter 8: Chopda Ni Indrajal",
            "Chapter 9: Dhingli",
            "Chapter 10: Bhukh Thi Ye Bhundi Bhikh"
        ]
    },
    {
        "id_suffix": "_sanskrit",
        "name": "Sanskrit",
        "color_hex": "0xFF8BC34A",
        "icon": "menu_book",
        "chapters": [
            "Chapter 1: Samvadadhvam (Let Us Speak Together)",
            "Chapter 2: Yad Bhavishyo Vinashyati",
            "Chapter 3: Swasthavrttam Samachara",
            "Chapter 4: Janardanasya Pashchimah Sandeshah",
            "Chapter 5: Gunavati Kanya",
            "Chapter 6: Kashthandah",
            "Chapter 7: Subhashitakusumani",
            "Chapter 8: Sakshi Bhutah Manushyah",
            "Chapter 9: Chakshushman Andha Eva",
            "Chapter 10: Tvameka Bhavani"
        ]
    }
]

files_to_update = ['ncert_class10.json', 'gseb_class10.json', 'cbse_class10.json']

for filename in files_to_update:
    filepath = os.path.join(curriculum_dir, filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r') as f:
        data = json.load(f)
        
    prefix = filename.split('_')[0] # ncert, gseb, cbse
        
    for sub_data in subjects_to_add:
        sub_id = f"{prefix}_class10{sub_data['id_suffix']}"
        
        # Find if it already exists
        subject_obj = None
        for s in data.get('subjects', []):
            if s.get('id') == sub_id:
                subject_obj = s
                break
                
        if not subject_obj:
            subject_obj = {
                "id": sub_id,
                "name": sub_data['name'],
                "color_hex": sub_data['color_hex'],
                "icon": sub_data['icon'],
                "chapters": []
            }
            data['subjects'].append(subject_obj)
            
        subject_obj['chapters'] = []
        for i, title in enumerate(sub_data['chapters']):
            subject_obj['chapters'].append({
                "chapter_id": f"{sub_id}_ch{i+1}",
                "title": title,
                "module_id": f"{sub_id}_ch{i+1}"
            })

    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)
        
    print(f"Updated {filename} with Languages.")
