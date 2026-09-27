import re

with open('lib/core/engine/default_blocks.dart', 'r') as f:
    content = f.read()

content = content.replace(
    "'quiz', 'mcq', 'knowledge_check', 'true_false',",
    "'quiz', 'mcq', 'knowledge_check', 'true_false', 'quiz_multiple_choice',"
)

with open('lib/core/engine/default_blocks.dart', 'w') as out:
    out.write(content)

print("Patched default_blocks.dart!")
