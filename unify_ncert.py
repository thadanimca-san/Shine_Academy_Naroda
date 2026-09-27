import os
import glob
import re

curriculum_dir = "app_core/curriculum"
cbse_files = glob.glob(os.path.join(curriculum_dir, "cbse_*.json"))

# Regex to match module_id for cbse maths or science
# It matches "module_id": "cbse_classX_maths_chY" and cbse_classX_science_chY
pattern = re.compile(r'"module_id":\s*"cbse_(class\d+_(maths|science)_[^"]+)"')

total_replacements = 0

for file_path in cbse_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace cbse_ with gseb_ only for maths and science
    new_content, count = pattern.subn(r'"module_id": "gseb_\1"', content)
    
    if count > 0:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {file_path} - replaced {count} module_ids")
        total_replacements += count

print(f"Total module_ids replaced: {total_replacements}")
