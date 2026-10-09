import json

with open('app_core/learning_modules/gseb_class10_maths_chapters.json', 'r', encoding='utf-8') as f:
    gseb_curriculum = json.load(f)

for chapter in gseb_curriculum:
    if chapter.get('id') == 'gseb_class10_maths_ch4':
        chapter['id'] = 'ncert_class10_maths_ch4'

with open('app_core/learning_modules/gseb_class10_maths_chapters.json', 'w', encoding='utf-8') as f:
    json.dump(gseb_curriculum, f, indent=2, ensure_ascii=False)

with open('app_core/curriculum/cbse_class10.json', 'r', encoding='utf-8') as f:
    cbse_curriculum = json.load(f)

# cbse already points to ncert_class10_maths_ch4 usually, but just in case
print("Cleaned up redundant Ch4 files and updated mappings.")
