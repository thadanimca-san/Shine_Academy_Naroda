import json

with open('app_core/learning_modules/ncert_class10_science_chapters.json', 'r', encoding='utf-8') as f:
    curriculum = json.load(f)

for chapter in curriculum:
    if chapter.get('id') == 'ncert_class10_science_ch2' or chapter.get('id') == 'gseb_class10_science_ch2':
        chapter['id'] = 'ncert_class10_science_ch2'

with open('app_core/learning_modules/ncert_class10_science_chapters.json', 'w', encoding='utf-8') as f:
    json.dump(curriculum, f, indent=2, ensure_ascii=False)

try:
    with open('app_core/learning_modules/gseb_class10_science_chapters.json', 'r', encoding='utf-8') as f:
        g_curriculum = json.load(f)
    for chapter in g_curriculum:
        if chapter.get('id') == 'gseb_class10_science_ch2':
            chapter['id'] = 'ncert_class10_science_ch2'
    with open('app_core/learning_modules/gseb_class10_science_chapters.json', 'w', encoding='utf-8') as f:
        json.dump(g_curriculum, f, indent=2, ensure_ascii=False)
except:
    pass

print("Cleaned up redundant Sci Ch2 files and updated mappings.")
