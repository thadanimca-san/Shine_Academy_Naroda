import os
import re

def process_files():
    lib_dir = 'lib'
    
    # Matches 'Text('something'' or 'const Text('something''
    # Group 1 is the quote character (' or ")
    # Group 2 is the exact string content, correctly handling escaped quotes like \' or \"
    pattern = re.compile(r"(?:const\s+)?Text\(\s*(['\"])((?:(?!\1)[^\\]|\\.)*)\1")
    
    import_stmt = "import 'package:shine_academy_naroda/core/services/trilingual_service.dart';"
    
    files_modified = 0
    texts_modified = 0
    
    for root, _, files in os.walk(lib_dir):
        for file in files:
            if not file.endswith('.dart'):
                continue
                
            filepath = os.path.join(root, file)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            matches = pattern.findall(content)
            
            if not matches:
                continue
                
            # Perform replacement
            def replacer(match):
                quote = match.group(1)
                text_content = match.group(2)
                
                # Exclude if it's already using TrilingualService or has string interpolation ($)
                if 'TrilingualService' in text_content or '$' in text_content:
                    return match.group(0)
                    
                return f"Text(TrilingualService.instance.getUIText({quote}{text_content}{quote})"
                
            new_content = pattern.sub(replacer, content)
            
            if new_content != content:
                # Calculate how many were actually replaced
                replaced_count = len(re.findall(r"TrilingualService.instance.getUIText", new_content)) - len(re.findall(r"TrilingualService.instance.getUIText", content))
                
                if replaced_count > 0:
                    # Add import if missing
                    if import_stmt not in new_content and 'TrilingualService.instance' in new_content:
                        lines = new_content.split('\n')
                        last_import_idx = -1
                        for i, line in enumerate(lines):
                            if line.startswith('import '):
                                last_import_idx = i
                        
                        if last_import_idx != -1:
                            lines.insert(last_import_idx + 1, import_stmt)
                        else:
                            lines.insert(0, import_stmt)
                        
                        new_content = '\n'.join(lines)
                    
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    
                    files_modified += 1
                    texts_modified += replaced_count
                    print(f"Updated {filepath} ({replaced_count} texts)")

    print(f"Mass UI Translation complete. Modified {texts_modified} texts in {files_modified} files.")

if __name__ == "__main__":
    process_files()
