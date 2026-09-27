import json
import glob

files_to_check = glob.glob('app_core/chapters/*class10_maths_ch1.json')
files_to_check.append('app_core/learning_modules/master_curriculum.json')

for file_path in files_to_check:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if '2²' in content:
            # Replace 2² with 2^2
            new_content = content.replace('2²', '2^2')
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed superscript in {file_path}")
    except Exception as e:
        print(f"Error {file_path}: {e}")
