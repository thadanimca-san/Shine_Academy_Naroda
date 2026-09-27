import re

with open('lib/features/assessment/exam_engine_screen.dart', 'r') as f:
    content = f.read()

content = content.replace('''          _error = 'Failed to generate Mock Test for this chapter.';''', '''          _error = 'Failed to generate Mock Test for this chapter. Error: ' + e.toString();''')

with open('lib/features/assessment/exam_engine_screen.dart', 'w') as out:
    out.write(content)

print("Patched error message display!")
