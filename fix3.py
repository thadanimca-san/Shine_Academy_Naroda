import re

with open('lib/features/dictionary/dictionary_popup.dart', 'r') as f:
    lines = f.readlines()

new_lines = []
skip = False
for i, line in enumerate(lines):
    if "child: Column(" in line and "crossAxisAlignment: CrossAxisAlignment.stretch" in lines[i+1]:
        skip = True
        continue
    if skip:
        if ")," in line and "}" not in line and "]" not in line:
            pass # wait, let's just use regex to replace everything between 'This word is not in our dictionary yet' and 'Nearest match card'
        continue
    new_lines.append(line)
