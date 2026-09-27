import json

with open('app_core/curriculum/gseb_class11.json', 'r') as f:
    data = json.load(f)

economics_titles = [
    "Economics: An Introduction",
    "Fundamental Concepts and Terminologies",
    "Demand",
    "Supply",
    "Cost of Production and Concepts of Revenue",
    "Market",
    "Indian Economy",
    "Economic Reforms",
    "National Income",
    "Budget",
    "Economic Ideas"
]

for subject in data['subjects']:
    if subject['id'] == 'gseb_class11_economics':
        new_chapters = []
        for i, title in enumerate(economics_titles):
            ch_num = i + 1
            new_chapters.append({
                "chapter_id": f"gseb_class11_economics_ch{ch_num}",
                "title": f"Chapter {ch_num}: {title}",
                "module_id": f"gseb_class11_economics_ch{ch_num}"
            })
        subject['chapters'] = new_chapters
        break

with open('app_core/curriculum/gseb_class11.json', 'w') as f:
    json.dump(data, f, indent=2)
print("Updated successfully")
