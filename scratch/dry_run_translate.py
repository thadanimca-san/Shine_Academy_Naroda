import os
import re

lib_dir = 'lib'
count = 0
files_modified = 0

text_pattern = re.compile(r"Text\(\s*(['\"])([^$'\"]+)\1")

for root, _, files in os.walk(lib_dir):
    for file in files:
        if file.endswith('.dart'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find all matches
            matches = text_pattern.findall(content)
            if matches:
                # filter out those that are already wrapped (though TrilingualService... wouldn't match this pattern because it matches Text('string' but if it's Text(TrilingualService it won't match Text('...'))
                valid_matches = []
                for match in matches:
                    if 'TrilingualService' not in match[1]:
                        valid_matches.append(match)
                        
                if valid_matches:
                    count += len(valid_matches)
                    files_modified += 1
                    # print(f"Found {len(valid_matches)} in {filepath}")

print(f"Total pure text widgets found: {count} in {files_modified} files")
