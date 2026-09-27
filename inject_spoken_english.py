import json
import os
import glob

curriculum_dir = "app_core/curriculum"
files = glob.glob(os.path.join(curriculum_dir, "*.json"))

target_classes = ["class3", "class4", "class5", "class6", "class7", "class8", "class9", "class10"]

grammar_subject = {
  "id": "interactive_grammar",
  "name": "English Grammar (Interactive)",
  "color_hex": "0xFF009688",
  "icon": "translate",
  "chapters": []
}

for file_path in files:
    filename = os.path.basename(file_path)
    # Check if the filename contains one of the target classes
    is_target = any(cls in filename for cls in target_classes)
    if is_target:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        # Check if already injected
        subjects = data.get("subjects", [])
        already_has = any(s.get("id") == "interactive_grammar" for s in subjects)
        
        if not already_has:
            # We want to insert it right after the normal English subject if it exists, or at the end
            inserted = False
            for i, subj in enumerate(subjects):
                name = subj.get("name", "").lower()
                if name == "english" or "english" in name:
                    subjects.insert(i + 1, grammar_subject)
                    inserted = True
                    break
            
            if not inserted:
                subjects.append(grammar_subject)
            
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"Injected into {filename}")
