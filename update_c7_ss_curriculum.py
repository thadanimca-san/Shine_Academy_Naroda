import json
import glob
import os

files = glob.glob('app_core/chapters/gseb_class7_social_science_ch*.json')
chapters = []
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        data = json.load(file)
        
        # Handle both list of blocks and dict with 'blocks' key
        blocks = data if isinstance(data, list) else data.get('blocks', [])
        
        # Try to find a title block or hook block for the chapter name
        title = "Unknown Chapter"
        for block in blocks:
            if isinstance(block, dict) and block.get('type') in ['chapter_title', 'hook'] and 'title' in block:
                title = block['title']
                break
        
        # Extract ch number from filename
        ch_num_str = os.path.basename(f).replace('gseb_class7_social_science_ch', '').replace('.json', '')
        try:
            ch_num = int(ch_num_str)
        except ValueError:
            continue
            
        chapters.append({
            "chapter_id": f"gseb_class7_social_science_ch{ch_num}",
            "title": f"Chapter {ch_num}: {title}",
            "module_id": f"gseb_class7_social_science_ch{ch_num}"
        })

# Sort by chapter number
chapters.sort(key=lambda x: int(x['chapter_id'].split('ch')[-1]))

# Update all curriculum files
for curr in ['gseb_class7.json', 'cbse_class7.json', 'ncert_class7.json']:
    filepath = f"app_core/curriculum/{curr}"
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    for subj in data.get("subjects", []):
        if subj["id"] == "gseb_class7_social_science" or subj["name"] == "Social Science":
            subj["chapters"] = chapters
            
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        
print("Curriculum updated with all Social Science chapters!")
