import json
import os

files_to_fix = [
    "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/cbse_class10_maths_ch4.json",
    "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_maths_ch4.json",
    "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/cbse_class10_maths_ch5.json",
    "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_maths_ch5.json"
]

def fix_newlines_in_dict(d):
    for key, value in d.items():
        if isinstance(value, str):
            # Replace literal backslash-n with actual newline
            d[key] = value.replace("\\n", "\n")
        elif isinstance(value, dict):
            fix_newlines_in_dict(value)
        elif isinstance(value, list):
            fix_newlines_in_list(value)

def fix_newlines_in_list(lst):
    for i in range(len(lst)):
        if isinstance(lst[i], str):
            lst[i] = lst[i].replace("\\n", "\n")
        elif isinstance(lst[i], dict):
            fix_newlines_in_dict(lst[i])
        elif isinstance(lst[i], list):
            fix_newlines_in_list(lst[i])

for file_path in files_to_fix:
    if not os.path.exists(file_path):
        continue
        
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    if isinstance(data, dict):
        fix_newlines_in_dict(data)
    elif isinstance(data, list):
        fix_newlines_in_list(data)
        
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

print("Successfully fixed newlines in JSON files!")
