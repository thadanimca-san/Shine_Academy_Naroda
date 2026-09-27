import re

filepath = "/home/ubuntu/Shine_Academy_Naroda/pubspec.yaml"
with open(filepath, 'r') as f:
    content = f.read()

# Check if already present
if "gseb_class7_science_ch1/" in content:
    print("Class 7 Science already in pubspec.yaml")
else:
    insertion = "\n" + "\n".join([f"    - app_core/learning_modules/gseb_class7_science_ch{i}/" for i in range(1, 14)]) + "\n"
    
    # Insert after gseb_class8_science_ch13/
    search_str = "    - app_core/learning_modules/gseb_class8_science_ch13/\n"
    if search_str in content:
        content = content.replace(search_str, search_str + insertion.strip('\n') + '\n')
    else:
        # Fallback to general assets insertion
        search_str = "  assets:\n"
        content = content.replace(search_str, search_str + insertion.strip('\n') + '\n')

    with open(filepath, 'w') as f:
        f.write(content)
    print("Added Class 7 Science to pubspec.yaml")
