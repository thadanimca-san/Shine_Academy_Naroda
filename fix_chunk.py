import re

path = 'lib/core/engine/universal_pdf_engine.dart'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('const int chunkSize = 10;', 'const int chunkSize = 1;')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed chunk size")
