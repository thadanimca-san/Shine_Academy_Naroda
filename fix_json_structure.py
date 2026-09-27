import json
import glob
import os

files = glob.glob('app_core/chapters/gseb_class7_social_science_ch[123].json')

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        data = json.load(file)
        
    if isinstance(data, list):
        # We need to wrap it
        
        # Try to find chapter title block
        title = "Chapter"
        for b in data:
            if b.get('type') == 'chapter_title' and 'title' in b:
                title = b['title']
                break
                
        ch_num = os.path.basename(f).replace('gseb_class7_social_science_ch', '').replace('.json', '')
        
        new_data = {
            "metadata": {
                "id": f"gseb_class7_social_science_ch{ch_num}",
                "title": f"Chapter {ch_num}: {title}",
                "subject": "Social Science",
                "grade": "7"
            },
            "blocks": data
        }
        
        with open(f, 'w', encoding='utf-8') as out_file:
            json.dump(new_data, out_file, indent=2, ensure_ascii=False)
        print(f"Fixed {f}")
    else:
        print(f"{f} is already a dict.")
