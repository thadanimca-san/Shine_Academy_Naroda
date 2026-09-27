import os
import re

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # 1. Fix Colors.black87Variant to Colors.black54
    content = content.replace('Colors.black87Variant', 'Colors.black54')

    # 2. Fix const BoxDecoration and const Shadow
    content = re.sub(r'const\s+BoxDecoration\(', r'BoxDecoration(', content)
    content = re.sub(r'const\s+Shadow\(', r'Shadow(', content)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    print("Starting final cleanup...")
    lib_dir = '/home/ubuntu/Shine_Academy_Naroda/lib'
    
    modified_count = 0
    for root, dirs, files in os.walk(lib_dir):
        for file in files:
            if file.endswith('.dart'):
                filepath = os.path.join(root, file)
                if fix_file(filepath):
                    modified_count += 1
                    
    print(f"Fixed final errors in {modified_count} Dart files!")

if __name__ == "__main__":
    main()
