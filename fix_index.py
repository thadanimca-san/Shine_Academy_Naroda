import json

path = "app_core/universal_dictionary/dictionary_index.json"
with open(path, "r") as f:
    data = json.load(f)

# check if it's already there
found = False
for entry in data['index']:
    if entry['file'] == 'app_core/universal_dictionary/class3_picture_dict.json':
        found = True
        break

if not found:
    data['index'].append({
        "file": "app_core/universal_dictionary/class3_picture_dict.json",
        "category": "english",
        "description": "Class 3 Picture Dictionary"
    })
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    print("Added to index!")
else:
    print("Already in index.")
