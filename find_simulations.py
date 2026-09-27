import os
import json

def search_json(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r') as f:
                        data = json.load(f)
                    
                    blocks = data.get('blocks', [])
                    for i, block in enumerate(blocks):
                        b_type = block.get('type')
                        if b_type in ['simulation', 'animated_diagram']:
                            print(f"Found {b_type} in {filepath} [Block {i}]")
                            if 'title' in block:
                                print(f"  Title: {block['title']}")
                            if 'body' in block:
                                print(f"  Body excerpt: {block['body'][:100]}...")
                            if 'url' in block:
                                print(f"  URL: {block['url']}")
                except Exception as e:
                    pass

search_json('app_core')
