import os
import json
import traceback

def fix_faqs_in_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        changed = False
        
        # Check if this is a chapter format (list of blocks or dict with blocks)
        blocks_to_check = []
        if isinstance(data, dict):
            if 'blocks' in data:
                blocks_to_check = data['blocks']
            elif 'modules' in data: # For master_curriculum
                for module in data.get('modules', []):
                    for chapter in module.get('chapters', []):
                        for section in chapter.get('sections', []):
                            for block in section.get('blocks', []):
                                blocks_to_check.append(block)
        elif isinstance(data, list):
            blocks_to_check = data
            
        for block in blocks_to_check:
            if not isinstance(block, dict):
                continue
                
            if block.get('type') == 'faqs':
                # Determine what type it should actually be based on its contents
                # if it has "questions", it becomes "theory" with bullet points.
                # if it has "body" but no "questions", it is just "theory" or "socratic".
                
                new_type = "theory"
                if "SOC" in block.get("id", ""):
                    new_type = "socratic"
                    
                block['type'] = new_type
                
                if 'questions' in block:
                    # Build body string from questions
                    body = ""
                    body_hi = ""
                    body_gu = ""
                    
                    for q in block['questions']:
                        question = q.get('question', '')
                        answer = q.get('answer', '')
                        body += f"• {question}: {answer}\n"
                        
                        question_hi = q.get('question_hi', '')
                        answer_hi = q.get('answer_hi', '')
                        if question_hi or answer_hi:
                            body_hi += f"• {question_hi}: {answer_hi}\n"
                            
                        question_gu = q.get('question_gu', '')
                        answer_gu = q.get('answer_gu', '')
                        if question_gu or answer_gu:
                            body_gu += f"• {question_gu}: {answer_gu}\n"
                    
                    if 'body' in block:
                        block['body'] = block['body'] + "\n\n" + body.strip()
                    else:
                        block['body'] = body.strip()
                        
                    if body_hi.strip():
                        if 'body_hi' in block:
                            block['body_hi'] = block['body_hi'] + "\n\n" + body_hi.strip()
                        else:
                            block['body_hi'] = body_hi.strip()
                            
                    if body_gu.strip():
                        if 'body_gu' in block:
                            block['body_gu'] = block['body_gu'] + "\n\n" + body_gu.strip()
                        else:
                            block['body_gu'] = body_gu.strip()
                    
                    del block['questions']
                changed = True

        if changed:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"Fixed faqs in {filepath}")
            
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

# walk directory
for root, dirs, files in os.walk('app_core'):
    for file in files:
        if file.endswith('.json'):
            fix_faqs_in_file(os.path.join(root, file))
