import json
import glob
import os

files = glob.glob("/home/ubuntu/Shine_Academy_Naroda/app_core/learning_modules/gseb_class8_science_ch*/blocks.json")

def validate(block, filepath):
    t = block.get('type')
    if not t:
        print(f"MISSING TYPE in {filepath}: {block}")
        return False
        
    if t in ['theory', 'example']:
        if 'text' not in block and 'content' not in block:
            print(f"MISSING text/content for {t} in {filepath}: {block}")
            return False
    elif t == 'activity':
        if 'title' not in block:
            print(f"MISSING title for activity in {filepath}: {block}")
            return False
    elif t == 'quiz':
        if 'question' not in block and ('content' not in block or 'question' not in block.get('content', {})):
            print(f"MISSING question for quiz in {filepath}: {block}")
            return False
        if 'options' not in block and ('content' not in block or 'options' not in block.get('content', {})):
            print(f"MISSING options for quiz in {filepath}: {block}")
            return False
        if 'correct_index' not in block and ('content' not in block or 'correct_index' not in block.get('content', {})):
            print(f"MISSING correct_index for quiz in {filepath}: {block}")
            return False
            
        ci = block.get('correct_index')
        if ci is not None and not isinstance(ci, int):
            print(f"INVALID correct_index type for quiz in {filepath}: {type(ci)} - {ci}")
            return False
            
    elif t == 'dictionary_link':
        if 'term_id' not in block and ('content' not in block or 'term_id' not in block.get('content', {})):
            print(f"MISSING term_id for dictionary_link in {filepath}: {block}")
            return False
            
    # Check animated_diagram widget crash
    if t == 'animated_diagram':
        # animated diagram expects 'content' to be a map, or null.
        if 'content' in block and block['content'] is not None and not isinstance(block['content'], dict):
             print(f"INVALID content type for animated_diagram in {filepath}: {type(block['content'])}")
             return False
             
    return True

has_error = False
for f in files:
    with open(f, 'r') as fp:
        try:
            data = json.load(fp)
            for b in data:
                if not validate(b, f):
                    has_error = True
        except Exception as e:
            print(f"Error parsing {f}: {e}")
            has_error = True

if not has_error:
    print("ALL BLOCKS PASSED PYTHON VALIDATION.")
