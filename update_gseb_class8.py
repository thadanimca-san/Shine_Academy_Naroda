import json

filepath = "/home/ubuntu/Shine_Academy_Naroda/app_core/curriculum/gseb_class8.json"

with open(filepath, 'r') as f:
    data = json.load(f)

science_chapters = [
    {"chapter_number": 1, "title": "Exploring the Investigative World of Science", "module_id": "gseb_class8_science_ch1", "is_available": True},
    {"chapter_number": 2, "title": "The Invisible Living World", "module_id": "gseb_class8_science_ch2", "is_available": True},
    {"chapter_number": 3, "title": "Health: The Ultimate Treasure", "module_id": "gseb_class8_science_ch3", "is_available": True},
    {"chapter_number": 4, "title": "Electricity: Magnetic and Heating Effects", "module_id": "gseb_class8_science_ch4", "is_available": True},
    {"chapter_number": 5, "title": "Exploring Forces", "module_id": "gseb_class8_science_ch5", "is_available": True},
    {"chapter_number": 6, "title": "Pressure, Winds, Storms, and Cyclones", "module_id": "gseb_class8_science_ch6", "is_available": True},
    {"chapter_number": 7, "title": "Particulate Nature of Matter", "module_id": "gseb_class8_science_ch7", "is_available": True},
    {"chapter_number": 8, "title": "Nature of Matter: Elements, Compounds, and Mixtures", "module_id": "gseb_class8_science_ch8", "is_available": True},
    {"chapter_number": 9, "title": "The Amazing World of Solutes, Solvents, and Solutions", "module_id": "gseb_class8_science_ch9", "is_available": True},
    {"chapter_number": 10, "title": "Light: Mirrors and Lenses", "module_id": "gseb_class8_science_ch10", "is_available": True},
    {"chapter_number": 11, "title": "Keeping Time with the Skies", "module_id": "gseb_class8_science_ch11", "is_available": True},
    {"chapter_number": 12, "title": "How Nature Works in Harmony", "module_id": "gseb_class8_science_ch12", "is_available": True},
    {"chapter_number": 13, "title": "Our Home: Earth, a Unique Life Sustaining Planet", "module_id": "gseb_class8_science_ch13", "is_available": True}
]

for subject in data["subjects"]:
    if subject["id"] == "science":
        subject["chapters"] = science_chapters
        break

with open(filepath, 'w') as f:
    json.dump(data, f, indent=2)
    
print("Updated gseb_class8.json")
