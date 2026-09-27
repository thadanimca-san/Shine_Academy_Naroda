import json

path = "app_core/curriculum/cbse_class10.json"
with open(path, "r") as f:
    data = json.load(f)

# Find the Science subject
for subject in data.get("subjects", []):
    if subject.get("id") == "cbse_class10_science":
        # Check if the exam paper is already there
        exists = any(c.get("module_id") == "cbse_class10_science_mock_exam_1" for c in subject.get("chapters", []))
        if not exists:
            # Add it to the top
            new_chapter = {
                "chapter_id": "cbse_class10_science_mock_exam_1",
                "title": "Board Exam: Full Science Paper 1 (With Solutions)",
                "module_id": "cbse_class10_science_mock_exam_1"
            }
            subject["chapters"].insert(0, new_chapter)
            
with open(path, "w") as f:
    json.dump(data, f, indent=2)

print("Updated cbse_class10.json")
