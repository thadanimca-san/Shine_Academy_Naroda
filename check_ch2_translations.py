import json

with open('app_core/chapters/ncert_class10_maths_ch2.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

missing = []

for idx, block in enumerate(data.get('blocks', [])):
    block_id = block.get('id', f"Block_{idx}")
    
    # Check title
    if 'title' in block:
        if 'title_hi' not in block or not block['title_hi']:
            missing.append(f"{block_id}: Missing title_hi")
        if 'title_gu' not in block or not block['title_gu']:
            missing.append(f"{block_id}: Missing title_gu")
            
    # Check body
    if 'body' in block:
        if 'body_hi' not in block or not block['body_hi']:
            missing.append(f"{block_id}: Missing body_hi")
        if 'body_gu' not in block or not block['body_gu']:
            missing.append(f"{block_id}: Missing body_gu")
            
    # Check question (socratic_question or quiz)
    if 'question' in block:
        if 'question_hi' not in block or not block['question_hi']:
            missing.append(f"{block_id}: Missing question_hi")
        if 'question_gu' not in block or not block['question_gu']:
            missing.append(f"{block_id}: Missing question_gu")
            
    # Check options
    if 'options' in block:
        if 'options_hi' not in block or not block['options_hi']:
            missing.append(f"{block_id}: Missing options_hi")
        if 'options_gu' not in block or not block['options_gu']:
            missing.append(f"{block_id}: Missing options_gu")
            
    # Check explanation
    if 'explanation' in block:
        if 'explanation_hi' not in block or not block['explanation_hi']:
            missing.append(f"{block_id}: Missing explanation_hi")
        if 'explanation_gu' not in block or not block['explanation_gu']:
            missing.append(f"{block_id}: Missing explanation_gu")

if missing:
    print("Found missing translations:")
    for m in missing:
        print(m)
else:
    print("All blocks have Hindi and Gujarati translations!")
