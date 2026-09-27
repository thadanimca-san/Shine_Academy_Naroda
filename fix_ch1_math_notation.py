#!/usr/bin/env python3
"""
Fix math notation in Real Numbers chapter.
Replace LaTeX ($...$, $$...$$) with plain Unicode math.
"""
import json, re

def fix_math(text):
    if not isinstance(text, str):
        return text
    
    # Remove display math $$ ... $$ → just the content
    text = re.sub(r'\$\$(.+?)\$\$', lambda m: clean_expr(m.group(1)), text, flags=re.DOTALL)
    # Remove inline math $ ... $ → just the content
    text = re.sub(r'\$(.+?)\$', lambda m: clean_expr(m.group(1)), text)
    
    return text

def clean_expr(expr):
    expr = expr.strip()
    # LaTeX commands → Unicode
    expr = expr.replace(r'\times', '×')
    expr = expr.replace(r'\leq', '≤')
    expr = expr.replace(r'\geq', '≥')
    expr = expr.replace(r'\neq', '≠')
    expr = expr.replace(r'\quad', '  ')
    expr = expr.replace(r'\mathbb{R}', 'ℝ')
    expr = expr.replace(r'\mathbb{Q}', 'ℚ')
    expr = expr.replace(r'\sqrt{2}', '√2')
    expr = expr.replace(r'\sqrt{3}', '√3')
    expr = expr.replace(r'\sqrt{5}', '√5')
    expr = expr.replace(r'\sqrt{7}', '√7')
    expr = expr.replace(r'\pi', 'π')
    expr = expr.replace(r'\cdot', '×')
    expr = expr.replace(r'\ldots', '...')
    expr = expr.replace(r'\Rightarrow', '→')
    expr = expr.replace(r'\rightarrow', '→')
    expr = expr.replace(r'\infty', '∞')
    expr = expr.replace(r'\frac{', '(').replace(r'}{', ')/(').replace(r'}', ')')
    # Superscripts
    expr = re.sub(r'\^(\{[^}]+\}|\w)', lambda m: to_super(m.group(1).strip('{}')), expr)
    # Subscripts  
    expr = re.sub(r'_(\{[^}]+\}|\w)', lambda m: to_sub(m.group(1).strip('{}')), expr)
    # Clean leftover braces
    expr = expr.replace('{', '').replace('}', '')
    return expr

def to_super(s):
    table = str.maketrans('0123456789+-=()nmikabc', '⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ⁿᵐⁱᵏᵃᵇᶜ')
    try:
        return s.translate(table)
    except:
        return '^' + s

def to_sub(s):
    table = str.maketrans('0123456789', '₀₁₂₃₄₅₆₇₈₉')
    try:
        return s.translate(table)
    except:
        return '_' + s

def fix_block(block):
    text_keys = ['title', 'title_hi', 'title_gu',
                 'body', 'body_hi', 'body_gu',
                 'question', 'question_hi', 'question_gu',
                 'explanation', 'explanation_hi', 'explanation_gu',
                 'solution', 'solution_hi', 'solution_gu',
                 'hint', 'hint_hi', 'hint_gu',
                 'front', 'front_hi', 'front_gu',
                 'back', 'back_hi', 'back_gu',
                 'statement', 'statement_hi', 'statement_gu',
                 'answer']
    for key in text_keys:
        if key in block:
            block[key] = fix_math(block[key])
    
    # Fix options lists
    for key in ['options', 'options_hi', 'options_gu', 'tips', 'tips_hi', 'tips_gu', 'steps', 'steps_hi', 'steps_gu']:
        if key in block and isinstance(block[key], list):
            block[key] = [fix_math(item) for item in block[key]]
    
    return block

# Process both files
files = [
    '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_maths_ch1.json',
    '/home/ubuntu/Shine_Academy_Naroda/app_core/content_database/cbse_class10_maths/cls10_math_realnumbers.json',
    '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/cbse_class10_math_ch1.json',
]

for path in files:
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    
    blocks = data.get('blocks', data if isinstance(data, list) else [])
    fixed = [fix_block(b) for b in blocks]
    
    if isinstance(data, list):
        out = fixed
    else:
        data['blocks'] = fixed
        out = data
    
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    
    print(f'Fixed: {path.split("/")[-1]}')

# Show sample of fixed content
with open(files[0], encoding='utf-8') as f:
    d = json.load(f)
print('\nSample after fix:')
for b in d['blocks'][:4]:
    body = b.get('body','')[:200]
    if body:
        print(f'[{b["type"]}] {b.get("title","")}')
        print(body)
        print()
print('✅ All math notation fixed!')
