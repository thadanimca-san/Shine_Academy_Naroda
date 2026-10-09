import os
import re

files_to_fix = [
    "lib/features/learning/school/sci_simulation/services/pdf_generator_service.dart",
    "lib/features/learning/school/maths_simulation/services/pdf_generator_service.dart",
    "lib/features/learning/school/english/services/pdf_generator_service.dart",
    "lib/features/learning/higher_secondary/english_simulation/services/pdf_generator_service.dart",
    "lib/features/english_simulation_11to12/services/pdf_generator_service.dart"
]

def process_file(filepath):
    if not os.path.exists(filepath):
        return
        
    with open(filepath, 'r') as f:
        content = f.read()

    # Find where the trailing garbage is
    # It looks like:
    #     );
    #   }_Class$standard' ...
    #   }
    # }
    
    # We want to replace everything from `    );\n  }_Class` to the end with `    );\n  }\n}`
    
    pattern = r'(\s*await UniversalPdfEngine\.generatePdfFromWidgets\([^;]+;\s*\n\s*\}).*?(\s*\n\})'
    content = re.sub(pattern, r'\1\2', content, flags=re.DOTALL)

    with open(filepath, 'w') as f:
        f.write(content)
        
    print(f"Fixed {filepath}")

for f in files_to_fix:
    process_file(f)
