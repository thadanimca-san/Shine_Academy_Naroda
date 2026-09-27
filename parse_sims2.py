import json

with open('all_sims.json', 'r') as f:
    for i, line in enumerate(f):
        try:
            d = json.loads(line.strip())
            title = d.get('title')
            content = d.get('content', {})
            inner_title = content.get('title', '') if isinstance(content, dict) else ''
            
            t = inner_title or title or ''
            if any(x in t for x in ["Color Changing", "Neutralization", "Acid Fire", "Energy Factory", "Blueprint", "Electrons Moving", "Oersted", "Straight Tube", "Bouncing Ball", "Prism", "Forest Ecosystem"]):
                print(f"Match: {t} \nData: {line}\n")
        except Exception: pass
