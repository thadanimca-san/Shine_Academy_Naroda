import os
import json

curriculum_dir = "app_core/curriculum"

for filename in os.listdir(curriculum_dir):
    if filename.endswith(".json"):
        filepath = os.path.join(curriculum_dir, filename)
        with open(filepath, 'r') as f:
            data = json.load(f)
            
        curr_id = data.get("curriculum_id")
        subjects = data.get("subjects", [])
        
        if not curr_id or not subjects:
            continue
            
        if curr_id == "gseb_class9":
            continue
            
        first_subject = subjects[0]
        subj_id = first_subject.get("id")
        subj_name = first_subject.get("name")
        
        # Add the chapters array to the first subject
        if "chapters" not in first_subject or not first_subject["chapters"]:
            first_subject["chapters"] = [
                {
                    "chapter_number": 1,
                    "title": f"Basics of {subj_name}",
                    "module_id": f"{curr_id}_{subj_id}_ch1",
                    "is_available": True
                }
            ]
            
        # For all other subjects, just add an empty chapters array to prevent Null cast errors
        for i in range(1, len(subjects)):
            if "chapters" not in subjects[i]:
                subjects[i]["chapters"] = []
                
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
            
print("Curriculum files fixed!")
