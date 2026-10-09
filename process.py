import json
import urllib.request
import urllib.parse
import os

def translate_to_gu(text):
    if not text:
        return text
    if isinstance(text, list):
        return [translate_to_gu(t) for t in text]
    
    # Translate Hindi to Gujarati
    url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=hi&tl=gu&dt=t&q=" + urllib.parse.quote(text)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        response = urllib.request.urlopen(req)
        data = json.loads(response.read().decode('utf-8'))
        return "".join([x[0] for x in data[0]])
    except Exception as e:
        print(f"Error translating '{text}': {e}")
        return text

def process_file():
    input_file = '/home/ubuntu/Shine_Academy_Naroda/app_core/maybe_used_in_future/cbse_class10_hindi_ch1.json'
    output_file = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/cbse_class10_hindi_ch1.json'
    
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Process metadata
    if 'title_hi' in data['metadata']:
        data['metadata']['title_gu'] = translate_to_gu(data['metadata']['title_hi'])
    
    # Process blocks
    for block in data['blocks']:
        # Update ID
        if block.get('id', '').startswith('KOBJ_CH1_'):
            block['id'] = block['id'].replace('KOBJ_CH1_', 'cbse_class10_hindi_ch1_')
        
        # Remove content wrapper if exists
        if 'content' in block:
            content = block.pop('content')
            block.update(content)
        
        # Fix correct_index
        if 'correct_index' in block:
            block['correct_index'] = int(block['correct_index'])
        elif 'correct_answer' in block:
            # Mistake prevention rule 3
            # We assume it should be converted if we could, but here we just ensure correct_index is int if it exists.
            pass
        
        # Translate fields
        for key in ['title', 'body', 'question', 'options', 'explanation']:
            hi_key = f"{key}_hi"
            gu_key = f"{key}_gu"
            if hi_key in block:
                block[gu_key] = translate_to_gu(block[hi_key])
                
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Successfully processed and saved to {output_file}")

if __name__ == '__main__':
    process_file()
