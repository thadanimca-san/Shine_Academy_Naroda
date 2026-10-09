import os
import re

files_to_fix = [
    "lib/features/learning/school/sci_simulation/services/pdf_generator_service.dart",
    "lib/features/learning/school/maths_simulation/services/pdf_generator_service.dart",
    "lib/features/learning/school/english/services/pdf_generator_service.dart",
    "lib/features/learning/higher_secondary/english_simulation/services/pdf_generator_service.dart",
    "lib/features/english_simulation_11to12/services/pdf_generator_service.dart",
    "lib/features/assessment/services/pdf_export_service.dart",
    "lib/features/learning/school/english/services/question_paper_pdf.dart"
]

def process_file(filepath):
    if not os.path.exists(filepath):
        return
        
    with open(filepath, 'r') as f:
        content = f.read()

    if "tts_interactive_text.dart" not in content:
        content = "import 'package:shine_academy_naroda/features/common/widgets/tts_interactive_text.dart';\n" + content
    
    # We must be careful not to replace things like `RichText(` or `TextSpan(`
    # But just `Text(` or ` Text(` or `child: Text(`.
    # Regex: replace `Text(` but ensure it's not a word character before it.
    
    content = re.sub(r'(?<![a-zA-Z0-9_])Text\(', r'TtsInteractiveText(text: ', content)

    with open(filepath, 'w') as f:
        f.write(content)
        
    print(f"Fixed {filepath}")

for f in files_to_fix:
    process_file(f)
