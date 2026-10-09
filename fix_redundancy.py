import json
import os

# 1. Read the rich CBSE file we created
with open('app_core/chapters/gseb_class10_maths_ch1.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 2. Update its ID to the unified NCERT id
data['metadata']['id'] = "ncert_class10_maths_ch1"

# 3. Save it as the unified ncert file
with open('app_core/chapters/ncert_class10_maths_ch1.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# 4. Remove the redundant files
os.remove('app_core/chapters/cbse_class10_math_ch1.json')
os.remove('app_core/chapters/gseb_class10_maths_ch1.json')

# 5. Update GSEB curriculum to point to the unified ID
with open('app_core/learning_modules/gseb_class10_maths_chapters.json', 'r', encoding='utf-8') as f:
    gseb_curriculum = json.load(f)

for chapter in gseb_curriculum:
    if chapter.get('id') == 'gseb_class10_maths_ch1':
        chapter['id'] = 'ncert_class10_maths_ch1'
    elif chapter.get('id') == 'gseb_class10_maths_ch2':
        chapter['id'] = 'ncert_class10_maths_ch2'
        
with open('app_core/learning_modules/gseb_class10_maths_chapters.json', 'w', encoding='utf-8') as f:
    json.dump(gseb_curriculum, f, indent=2, ensure_ascii=False)

print("Redundancy fixed! Moved to ncert_class10_maths_ch1.json")
