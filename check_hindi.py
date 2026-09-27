import json
import glob
import sys

files = glob.glob('/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/*class10*.json')
missing_hindi = 0
total_blocks = 0

for file_path in files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except:
        continue
    
    if not isinstance(data, dict) or 'blocks' not in data:
        continue
        
    for block in data['blocks']:
        if not isinstance(block, dict):
            continue
        total_blocks += 1
        
        missing = False
        t = block.get('type')
        if t in ['theory', 'hook', 'teacher_tip', 'memory_trick', 'common_mistakes', 'real_world_example', 'insight']:
            if 'title' in block and 'title_hi' not in block:
                missing = True
            if 'body' in block and 'body_hi' not in block:
                missing = True
        elif t in ['quiz', 'mcq', 'quiz_multiple_choice']:
            if 'question' in block and 'question_hi' not in block:
                missing = True
            if 'options' in block and 'options_hi' not in block:
                missing = True
            if 'explanation' in block and 'explanation_hi' not in block:
                missing = True
        
        if missing:
            missing_hindi += 1
            # print(f"Missing Hindi in {file_path} - block {block.get('id')}")

print(f"Total Class 10 blocks: {total_blocks}")
print(f"Blocks missing Hindi: {missing_hindi}")
