import json

chapters = [
    {"chapter_number": 1, "title": "Nutrition in Plants"},
    {"chapter_number": 2, "title": "Nutrition in Animals"},
    {"chapter_number": 3, "title": "Heat"},
    {"chapter_number": 4, "title": "Acids, Bases and Salts"},
    {"chapter_number": 5, "title": "Physical and Chemical Changes"},
    {"chapter_number": 6, "title": "Respiration in Organisms"},
    {"chapter_number": 7, "title": "Transportation in Animals and Plants"},
    {"chapter_number": 8, "title": "Reproduction in Plants"},
    {"chapter_number": 9, "title": "Motion and Time"},
    {"chapter_number": 10, "title": "Electric Current and Its Effects"},
    {"chapter_number": 11, "title": "Light"},
    {"chapter_number": 12, "title": "Forests: Our Lifeline"},
    {"chapter_number": 13, "title": "Wastewater Story"}
]

filepath = "/home/ubuntu/Shine_Academy_Naroda/app_core/curriculum/gseb_class7.json"
with open(filepath, 'r') as f:
    data = json.load(f)

for subj in data.get("subjects", []):
    if subj["id"] == "science":
        subj["chapters"] = [
            {
                "chapter_number": c["chapter_number"],
                "title": c["title"],
                "module_id": f"gseb_class7_science_ch{c['chapter_number']}",
                "is_available": True,
                "status": "Available"
            }
            for c in chapters
        ]

with open(filepath, 'w') as f:
    json.dump(data, f, indent=2)

# Create CBSE
cbse_data = dict(data)
cbse_data["curriculum_id"] = "cbse_class7"
cbse_data["board"] = "CBSE"

with open("/home/ubuntu/Shine_Academy_Naroda/app_core/curriculum/cbse_class7.json", 'w') as f:
    json.dump(cbse_data, f, indent=2)

# Create NCERT
ncert_data = dict(data)
ncert_data["curriculum_id"] = "ncert_class7"
ncert_data["board"] = "NCERT"

with open("/home/ubuntu/Shine_Academy_Naroda/app_core/curriculum/ncert_class7.json", 'w') as f:
    json.dump(ncert_data, f, indent=2)

print("Class 7 Curriculum setup complete.")
