import os
import json
import re

def main():
    json_types = set()
    chapters_dir = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters'
    
    # 1. Find all types in JSON files
    for root, _, files in os.walk(chapters_dir):
        for f in files:
            if f.endswith('.json'):
                path = os.path.join(root, f)
                with open(path, 'r', encoding='utf-8') as file:
                    try:
                        data = json.load(file)
                        if isinstance(data, list):
                            for block in data:
                                if isinstance(block, dict) and 'type' in block:
                                    json_types.add(block['type'])
                    except:
                        pass
                        
    # 2. Find all registered types in default_blocks.dart
    dart_file = '/home/ubuntu/Shine_Academy_Naroda/lib/core/engine/default_blocks.dart'
    with open(dart_file, 'r', encoding='utf-8') as file:
        dart_content = file.read()
        
    # Extract string literals in registry.register(BlockDefinition(type: '...'))
    # and lists like ['theory', 'formula', ...]
    registered_types = set()
    
    # Match type: 'something'
    matches = re.findall(r"type:\s*'([^']+)'", dart_content)
    registered_types.update(matches)
    
    # Match lists
    lists = re.findall(r"\[(.*?)\];", dart_content, re.DOTALL)
    for lst in lists:
        strings = re.findall(r"'([^']+)'", lst)
        registered_types.update(strings)
        
    print(f"Total unique types in JSON: {len(json_types)}")
    print(f"Total registered types in Dart: {len(registered_types)}")
    
    missing_types = json_types - registered_types
    print(f"\nMissing types (present in JSON, but NOT registered):")
    for t in sorted(missing_types):
        print(f"- {t}")

if __name__ == '__main__':
    main()
