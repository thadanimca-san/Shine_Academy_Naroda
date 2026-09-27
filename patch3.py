import re

with open('lib/features/assessment/exam_engine_screen.dart', 'r') as f:
    content = f.read()

content = content.replace('''optionsHi: block['options_hi'] != null ? List<String>.from(block['options_hi']) : null,''',
                          '''optionsHi: block['options_hi'] != null ? (block['options_hi'] as List).map((e) => e.toString()).toList().cast<String>() : null,''')

with open('lib/features/assessment/exam_engine_screen.dart', 'w') as out:
    out.write(content)

print("Patched options_hi!")
