import os
import re

def fix_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    str_pat = r"(?:'[^'\\]*(?:\\.[^'\\]*)*'|\"[^\"\\]*(?:\\.[^\"\\]*)*\")"
    # Matches: getUIText( <str> ) \n <str>
    # Note: we also want to catch cases without \n, just spaces.
    pattern = r"TrilingualService\.instance\.getUIText\(\s*(" + str_pat + r")\s*\)\s*(\n?\s*" + str_pat + r")"
    
    new_content = content
    while True:
        replaced = re.sub(pattern, r"TrilingualService.instance.getUIText(\1\2)", new_content)
        if replaced == new_content:
            break
        new_content = replaced
        
    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Fixed {filepath}")

for root, dirs, files in os.walk('lib'):
    for file in files:
        if file.endswith('.dart'):
            fix_file(os.path.join(root, file))
