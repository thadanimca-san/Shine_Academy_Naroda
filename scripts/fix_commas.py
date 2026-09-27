import os
import re

directory = '/home/ubuntu/Shine_Academy_Naroda/lib/features/learning/school/english3to6/data'
for filename in os.listdir(directory):
    if filename.startswith('chapter_class') and filename.endswith('.dart'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as f:
            content = f.read()
            
        # Add comma after gujaratiSummary if missing before glosses
        # Regex to find gujaratiSummary: '...' \n glosses:
        # We can just look for the single quote followed by newline and glosses
        content = re.sub(r'\'\s*\n\s*glosses:', r"',\n  glosses:", content)
        
        with open(filepath, 'w') as f:
            f.write(content)
print('Fixed missing commas.')
