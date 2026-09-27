import os
import glob

directory = 'lib/features/learning/higher_secondary/physics_sandbox/data/lessons/'
for file_path in glob.glob(os.path.join(directory, '*.dart')):
    with open(file_path, 'r') as f:
        content = f.read()
    
    if 'sandboxBuilder: null,' in content:
        new_content = content.replace('sandboxBuilder: null,', 'sandboxBuilder: (_) => const SizedBox.shrink(),')
        with open(file_path, 'w') as f:
            f.write(new_content)
        print(f"Fixed {file_path}")
