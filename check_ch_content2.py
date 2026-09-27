import json
import os
import glob

files = glob.glob('app_core/chapters/gseb_class8_science_ch*.json')
files.sort(key=lambda x: int(x.split('_ch')[1].split('.')[0]))

for f in files:
    with open(f, 'r') as fp:
        try:
            data = json.load(fp)
            title = data.get('metadata', {}).get('title', 'Unknown')
            first_q = 'No questions'
            
            # Recursive search for a question
            def find_q(obj):
                if isinstance(obj, dict):
                    if 'question' in obj:
                        return obj['question']
                    for k, v in obj.items():
                        q = find_q(v)
                        if q: return q
                elif isinstance(obj, list):
                    for item in obj:
                        q = find_q(item)
                        if q: return q
                return None
                
            q = find_q(data.get('blocks', []))
            if q: first_q = q
            
            print(f"{os.path.basename(f)} - {first_q[:80]}")
        except Exception as e:
            print(f"Error in {f}: {e}")
