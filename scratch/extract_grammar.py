import os
import re

TEXT_FILE = "SAN/Year2026/speak_english_confidently.txt"

with open(TEXT_FILE, "r", encoding="utf-8") as f:
    lines = f.readlines()

missing_lessons = [1, 2, 20, 25, 26, 40, 54, 59, 60]
for idx, l_num in enumerate(missing_lessons):
    start_str = f"LESSON {l_num}"
    end_str = f"LESSON {l_num + 1}"
    
    start_idx = -1
    end_idx = -1
    
    for i, line in enumerate(lines):
        if line.startswith(start_str):
            start_idx = i
        if line.startswith(end_str) and start_idx != -1:
            end_idx = i
            break
            
    if end_idx == -1:
        end_idx = len(lines)
        
    if start_idx != -1:
        content = "".join(lines[start_idx:end_idx])
        with open(f"scratch/grammar/lesson_{l_num}.txt", "w", encoding="utf-8") as out:
            out.write(content)
        print(f"Extracted Lesson {l_num} ({len(content)} chars)")
    else:
        print(f"Failed to find Lesson {l_num}")
