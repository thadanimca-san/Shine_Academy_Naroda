import os

pubspec_path = "pubspec.yaml"
base_dir = "app_core/learning_modules"

prefixes = ["nursery_", "lkg_", "ukg_", "class1_"]
all_dirs = []
for d in os.listdir(base_dir):
    if any(d.startswith(p) for p in prefixes) and os.path.isdir(os.path.join(base_dir, d)):
        all_dirs.append(d)
        
all_dirs.sort()

with open(pubspec_path, "r") as f:
    lines = f.readlines()

insert_idx = -1
for i, line in enumerate(lines):
    if "- app_core/learning_modules/" in line:
        insert_idx = i

if insert_idx != -1:
    last_asset_idx = insert_idx
    for i in range(insert_idx, len(lines)):
        if lines[i].strip().startswith("- "):
            last_asset_idx = i
        elif lines[i].strip() == "":
            pass
        elif not lines[i].strip().startswith("- "):
            break

    existing_assets = "".join(lines)
    
    lines_to_add = []
    for d in all_dirs:
        asset_str = f"    - app_core/learning_modules/{d}/\n"
        if asset_str not in existing_assets:
            lines_to_add.append(asset_str)
            
    if lines_to_add:
        lines = lines[:last_asset_idx+1] + lines_to_add + lines[last_asset_idx+1:]
        
        with open(pubspec_path, "w") as f:
            f.writelines(lines)
        print(f"Added {len(lines_to_add)} assets to pubspec.yaml")
    else:
        print("All assets are already in pubspec.yaml")
else:
    print("Could not find assets section!")
