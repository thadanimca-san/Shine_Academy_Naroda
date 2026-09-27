import os
import json

chapters_dir = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters'
total_removed = 0
files_modified = 0

for root, _, files in os.walk(chapters_dir):
    for filename in files:
        if filename.endswith('.json'):
            filepath = os.path.join(root, filename)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                except:
                    continue
                    
            if not isinstance(data, list):
                # Also handle dictionary like {"blocks": [...]}
                if isinstance(data, dict) and "blocks" in data and isinstance(data["blocks"], list):
                    blocks_list = data["blocks"]
                    is_dict = True
                else:
                    continue
            else:
                blocks_list = data
                is_dict = False
                
            new_blocks = []
            removed_count = 0
            
            for block in blocks_list:
                is_dummy = False
                
                # Sometimes options are at root, sometimes inside 'content'
                opts = block.get('options', [])
                if not opts and isinstance(block.get('content'), dict):
                    opts = block['content'].get('options', [])
                    
                if isinstance(opts, list):
                    for opt in opts:
                        if isinstance(opt, str) and opt.strip().lower() in ('option a', 'option 1', 'option c'):
                            is_dummy = True
                            break
                            
                q = block.get('question', '')
                if not q and isinstance(block.get('content'), dict):
                    q = block['content'].get('question', '')
                if isinstance(q, str) and ('Question text' in q or 'Dummy Question' in q):
                    is_dummy = True
            
                if not is_dummy:
                    new_blocks.append(block)
                else:
                    removed_count += 1
                    
            if removed_count > 0:
                if is_dict:
                    data["blocks"] = new_blocks
                    new_data = data
                else:
                    new_data = new_blocks
                    
                with open(filepath, 'w', encoding='utf-8') as f:
                    json.dump(new_data, f, indent=2, ensure_ascii=False)
                    f.write('\n')
                print(f"Removed {removed_count} dummy questions from {filename}")
                total_removed += removed_count
                files_modified += 1

print(f"\nFinished! Removed {total_removed} dummy questions across {files_modified} files.")
