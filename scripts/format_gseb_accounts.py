import os
import json
import re

CHAPTERS_DIR = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters'

def extract_table(text):
    if not text:
        return None, None, None
    table_pattern = re.compile(r'(\n(?:\|.*?\|\n)+)')
    match = table_pattern.search(text + '\n')
    if not match:
        return None, None, None
    table_text = match.group(1).strip()
    start, end = match.span(1)
    pre_text = text[:start].strip()
    post_text = text[end:].strip()
    return pre_text, table_text, post_text

def process_file(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    is_list = isinstance(data, list)
    blocks_list = data if is_list else data.get('blocks', [])
    
    new_blocks = []
    modified = False
    
    for block in blocks_list:
        b_type = block.get('type')
        
        text_fields = []
        if b_type == 'theory':
            text_fields = ['body', 'body_hi', 'body_gu']
        elif b_type in ['mcq', 'practice_question', 'socratic_question']:
            text_fields = ['question', 'question_hi', 'question_gu']
        else:
            new_blocks.append(block)
            continue
            
        en_field = text_fields[0]
        hi_field = text_fields[1]
        gu_field = text_fields[2]
        
        pre_en, tbl_en, post_en = extract_table(block.get(en_field, ''))
        
        if tbl_en:
            modified = True
            pre_hi, tbl_hi, post_hi = extract_table(block.get(hi_field, ''))
            pre_gu, tbl_gu, post_gu = extract_table(block.get(gu_field, ''))
            
            # Pre-Table Block
            if pre_en:
                pre_block = {
                    "id": block.get('id', 'UNKNOWN_ID') + "_PRE",
                    "type": "theory",
                    "title": block.get('title', "Problem Context"),
                    "title_hi": block.get('title_hi', "समस्या का संदर्भ"),
                    "title_gu": block.get('title_gu', "સમસ્યાનો સંદર્ભ"),
                    "body": pre_en,
                    "body_hi": pre_hi or pre_en,
                    "body_gu": pre_gu or pre_en
                }
                new_blocks.append(pre_block)
                
            # Markdown Table Block
            table_block = {
                "id": block.get('id', 'UNKNOWN_ID') + "_TBL",
                "type": "markdown_table",
                "title": block.get('title', "Data Table") + " (Table)",
                "title_hi": block.get('title_hi', "डेटा तालिका") + " (तालिका)",
                "title_gu": block.get('title_gu', "માહિતી કોષ્ટક") + " (કોષ્ટક)",
                "table_markdown": tbl_en
            }
            if tbl_hi: table_block["table_markdown_hi"] = tbl_hi
            if tbl_gu: table_block["table_markdown_gu"] = tbl_gu
            new_blocks.append(table_block)
            
            # Post-Table Block
            if post_en or b_type != 'theory':
                post_block = dict(block)
                post_block['id'] = block.get('id', 'UNKNOWN_ID') + "_POST"
                if b_type == 'theory':
                    post_block['body'] = post_en
                    if hi_field in post_block: post_block[hi_field] = post_hi or post_en
                    if gu_field in post_block: post_block[gu_field] = post_gu or post_en
                else:
                    post_block['question'] = post_en or "Refer to the table above to answer the question."
                    if hi_field in post_block: post_block[hi_field] = post_hi or "प्रश्न का उत्तर देने के लिए ऊपर दी गई तालिका देखें।"
                    if gu_field in post_block: post_block[gu_field] = post_gu or "પ્રશ્નનો જવાબ આપવા માટે ઉપરના કોષ્ટકનો સંદર્ભ લો."
                new_blocks.append(post_block)
        else:
            new_blocks.append(block)
            
    # Also fix root-level array mistake while we're modifying the file
    if modified or is_list:
        if is_list:
            print(f" -> FIXED ROOT ARRAY MISTAKE IN {file_path}")
            data = {
                "metadata": {
                    "id": os.path.basename(file_path).split('.')[0],
                    "title": "GSEB Accounts Chapter"
                },
                "blocks": new_blocks
            }
        else:
            data['blocks'] = new_blocks
            
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            f.write('\n')
        print(f" -> Modified {file_path}")
    else:
        print(f" -> No tables found.")

if __name__ == '__main__':
    for f in os.listdir(CHAPTERS_DIR):
        if f.startswith('gseb_class12_accounts') and f.endswith('.json'):
            try:
                process_file(os.path.join(CHAPTERS_DIR, f))
            except Exception as e:
                print(f"Error processing {f}: {e}")
