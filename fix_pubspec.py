import os

pubspec_path = "pubspec.yaml"
base_dir = "app_core/learning_modules"

# Get all nursery directories
nursery_dirs = [d for d in os.listdir(base_dir) if d.startswith("nursery_") and os.path.isdir(os.path.join(base_dir, d))]
nursery_dirs.sort()

# Read pubspec
with open(pubspec_path, "r") as f:
    lines = f.readlines()

# Find the last asset under app_core/learning_modules/
insert_idx = -1
for i, line in enumerate(lines):
    if "- app_core/learning_modules/" in line:
        insert_idx = i

if insert_idx != -1:
    # We will insert right after the last gseb line. Let's find the last line that starts with "    - " in the assets block
    last_asset_idx = insert_idx
    for i in range(insert_idx, len(lines)):
        if lines[i].strip().startswith("- "):
            last_asset_idx = i
        elif lines[i].strip() == "":
            pass # Keep going if it's an empty line, but usually we just append at last_asset_idx
        elif not lines[i].strip().startswith("- "):
            break

    # Check which ones are missing
    existing_assets = "".join(lines)
    
    lines_to_add = []
    for d in nursery_dirs:
        asset_str = f"    - app_core/learning_modules/{d}/\n"
        if asset_str not in existing_assets:
            lines_to_add.append(asset_str)
            
    if lines_to_add:
        lines = lines[:last_asset_idx+1] + lines_to_add + lines[last_asset_idx+1:]
        
        with open(pubspec_path, "w") as f:
            f.writelines(lines)
        print(f"Added {len(lines_to_add)} nursery assets to pubspec.yaml")
    else:
        print("All nursery assets are already in pubspec.yaml")
else:
    print("Could not find assets section!")
