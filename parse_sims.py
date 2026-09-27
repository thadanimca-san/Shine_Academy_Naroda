import json

with open('all_sims.json', 'r') as f:
    for i, line in enumerate(f):
        try:
            d = json.loads(line.strip())
            title = d.get('title')
            content = d.get('content', {})
            if isinstance(content, dict):
                inner_title = content.get('title', '')
                desc = content.get('description', '')
                if inner_title or desc:
                    print(f"{i}: {inner_title} - {desc}")
            elif isinstance(content, str):
                print(f"{i}: {title} - {content[:100]}...")
        except Exception: pass
