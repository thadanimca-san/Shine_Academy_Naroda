import os
import re

base_dir = '/home/ubuntu/Shine_Academy_Naroda/lib/features/learning/school/english/data'
files = [f for f in os.listdir(base_dir) if f.startswith('reading_class') and f.endswith('.dart')]

for file_name in files:
    file_path = os.path.join(base_dir, file_name)
    with open(file_path, 'r') as f:
        content = f.read()

    # The problem is `bodyHi: '...',` appears twice for the same ReadingPassage due to the earlier translation script appending it inside but leaving the old one if it existed, or something similar.
    # We can fix duplicate named arguments using a regex that finds all 'bodyHi: ...,' in a ReadingPassage and keeps only the first one.
    
    # Actually, a simpler way since it's just a few files with `duplicate_named_argument`:
    # Let's do a simple line-by-line deduplication inside each ReadingPassage block.
    
    lines = content.split('\n')
    out_lines = []
    in_passage = False
    has_body_hi = False
    
    for line in lines:
        if 'ReadingPassage(' in line:
            in_passage = True
            has_body_hi = False
            out_lines.append(line)
        elif in_passage and 'bodyHi:' in line:
            if not has_body_hi:
                has_body_hi = True
                out_lines.append(line)
            else:
                # skip this line
                pass
        elif in_passage and ');' in line: # end of passage
            in_passage = False
            out_lines.append(line)
        else:
            out_lines.append(line)

    with open(file_path, 'w') as f:
        f.write('\n'.join(out_lines))

print("Fixed duplicate bodyHi")
