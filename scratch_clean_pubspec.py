import re

pubspec_path = 'pubspec.yaml'

with open(pubspec_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
in_assets = False

for line in lines:
    if line.strip() == 'assets:':
        in_assets = True
        new_lines.append(line)
        continue
        
    if in_assets:
        # Stop processing if we hit another top-level key or empty lines that break the block
        if not line.startswith(' ') and not line.strip() == '' and not line.strip().startswith('#'):
            in_assets = False
            
    if in_assets:
        if '- app_core/learning_modules/' in line:
            # We want to keep "- app_core/learning_modules/" but remove all subdirectories
            if line.strip() == '- app_core/learning_modules/':
                pass # Keep it, but actually let's just add master_curriculum.json instead
            continue
            
    new_lines.append(line)

# Let's insert master_curriculum.json properly
# Find the assets block again and insert it
for i, line in enumerate(new_lines):
    if line.strip() == '- app_core/curriculum/':
        new_lines.insert(i + 1, "    - app_core/learning_modules/master_curriculum.json\n")
        break

with open(pubspec_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
