import json

titles = {
    1: "Chapter 1: Rajput Age : New Ruler and States",
    2: "Chapter 2: The Delhi Sultanate",
    3: "Chapter 3: Mughal Empire",
    4: "Chapter 4: Medieval Architecture, Cities, Merchants and Craftsman",
    5: "Chapter 5: Adivasis",
    6: "Chapter 6: Nomadic and Denotified Tribes",
    7: "Chapter 7: Bhakti Age : Religious Sects and Saints",
    8: "Chapter 8: Formation of Regional Culture",
    9: "Chapter 9: Political Rulers of 18th Century",
    10: "Chapter 10: Earth's Internal Composition and Landforms",
    11: "Chapter 11: Components of the Environment and Interrelationships",
    12: "Chapter 12: Effects of Atmosphere on Living Beings",
    13: "Chapter 13: Disaster Management",
    14: "Chapter 14: Conservation and Preservation of Resources",
    15: "Chapter 15: Equality in Democracy",
    16: "Chapter 16: State Government",
    17: "Chapter 17: Gender Discrimination",
    18: "Chapter 18: Means of Communication and Advertisement",
    19: "Chapter 19: Markets",
    20: "Let's test the understanding"
}

filepath = 'app_core/curriculum/gseb_class7.json'

with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

for subject in data.get('subjects', []):
    if subject.get('name') == 'Social Science':
        chapters = []
        for i in range(1, 21):
            chapters.append({
                "chapter_id": f"gseb_class7_social_science_ch{i}",
                "title": titles[i],
                "module_id": f"gseb_class7_social_science_ch{i}"
            })
        subject['chapters'] = chapters
        break

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Patched gseb_class7.json successfully!")
