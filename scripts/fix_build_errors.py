import os
import re

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # 1. Fix onSurfaceXX invalid getters
    # Theme.of(context).colorScheme.onSurface12 -> Theme.of(context).colorScheme.onSurface.withOpacity(0.12)
    content = re.sub(r'\.onSurface(\d{2})', r'.onSurface.withOpacity(0.\1)', content)

    # 2. Fix const keyword errors (removing const from TextStyle and BoxShadow)
    # The build fails when const is used with Theme.of(context)
    # E.g. style: const TextStyle(...) -> style: TextStyle(...)
    content = re.sub(r'const\s+TextStyle\(', r'TextStyle(', content)
    content = re.sub(r'const\s+\[BoxShadow\(', r'[BoxShadow(', content)
    content = re.sub(r'const\s+BoxShadow\(', r'BoxShadow(', content)
    
    # Sometimes there is `const Icon(Icons.close, color: Theme.of(context)...)`
    content = re.sub(r'const\s+Icon\(', r'Icon(', content)

    # 3. Fix missing TrilingualService imports
    if 'TrilingualService' in content and 'trilingual_service.dart' not in content:
        # Add import at the top after other imports
        import_stmt = "import 'package:shine_academy_naroda/core/services/trilingual_service.dart';\n"
        # Find the last import
        imports = re.findall(r'^import\s+.*;', content, flags=re.MULTILINE)
        if imports:
            last_import = imports[-1]
            content = content.replace(last_import, last_import + "\n" + import_stmt, 1)
        else:
            content = import_stmt + content

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    print("Starting Build Error Fixes...")
    lib_dir = '/home/ubuntu/Shine_Academy_Naroda/lib'
    
    modified_count = 0
    for root, dirs, files in os.walk(lib_dir):
        for file in files:
            if file.endswith('.dart'):
                filepath = os.path.join(root, file)
                if fix_file(filepath):
                    modified_count += 1
                    
    print(f"Fixed build errors in {modified_count} Dart files!")

if __name__ == "__main__":
    main()
