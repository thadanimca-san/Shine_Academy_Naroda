import json

def fix_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    modified = False
    for block in data.get('blocks', []):
        if 'content' in block and isinstance(block['content'], str):
            if block.get('type') in ['hook', 'theory', 'exam_tips']:
                block['body'] = block.pop('content')
                modified = True
            elif block.get('type') in ['diagram']:
                # The Gold Standard doesn't specify if diagram uses 'body', but typically yes or we can just leave it if not needed, but wait: diagram usually has 'body' too, or 'description'
                pass # let's just do hook and theory
    
    if modified:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Fixed {path}")

fix_file('app_core/chapters/ncert_class10_maths_ch1.json')
