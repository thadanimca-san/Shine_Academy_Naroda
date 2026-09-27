import glob
import json

chapter_files = glob.glob('app_core/chapters/*class9*.json')
missing_texts = set()

for f in chapter_files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for block in data.get('blocks', []):
                b_type = block.get('type', 'theory')
                
                if b_type in ['theory', 'hook', 'teacher_tip', 'memory_trick', 'common_mistakes', 'real_world_example', 'insight']:
                    if 'title' in block and 'title_hi' not in block:
                        missing_texts.add(block['title'])
                    if 'body' in block and 'body_hi' not in block:
                        missing_texts.add(block['body'])
                elif b_type in ['quiz', 'mcq', 'quiz_multiple_choice']:
                    if 'question' in block and 'question_hi' not in block:
                        missing_texts.add(block['question'])
                    if 'options' in block and 'options_hi' not in block:
                        for opt in block['options']:
                            missing_texts.add(opt)
                    if 'explanation' in block and 'explanation_hi' not in block:
                        missing_texts.add(block['explanation'])
                
                if 'content' in block and 'content_hi' not in block and isinstance(block['content'], str):
                    missing_texts.add(block['content'])

    except Exception:
        pass

for i, text in enumerate(list(missing_texts)[:50]):
    print(f"{i}: {text}")
print(f"Total unique missing: {len(missing_texts)}")
