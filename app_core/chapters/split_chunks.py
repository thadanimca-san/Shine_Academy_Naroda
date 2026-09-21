import re
import json

def split_textbook(filepath, output_json):
    with open(filepath, 'r') as f:
        text = f.read()

    chunks = []
    
    # Simple logic to split the textbook text into manageable parts
    # For accounts chapter 6, we know there are main headings and an EXERCISE section
    
    # Find exercise section
    exercise_match = re.search(r'EXERCISE\n(.*)', text, re.DOTALL)
    theory_text = text
    exercise_text = ""
    
    if exercise_match:
        exercise_text = exercise_match.group(1)
        theory_text = text[:exercise_match.start()]
    
    # Split theory text by main sections (1., 2., 3., etc.)
    # For now, just split it roughly by lines to keep it simple, around 800 lines per chunk
    lines = theory_text.split('\n')
    chunk_size = 800
    for i in range(0, len(lines), chunk_size):
        chunk = "\n".join(lines[i:i+chunk_size])
        chunks.append({"type": "theory", "content": chunk})
        
    # Split exercises by questions
    # Question 1: MCQs
    # Question 2: Short questions
    # Question 3: Calculation questions
    # Question 4: Journal entries
    # etc.
    # Let's chunk the exercises text by 800 lines as well, or by specific question numbers if possible.
    ex_lines = exercise_text.split('\n')
    for i in range(0, len(ex_lines), chunk_size):
        chunk = "\n".join(ex_lines[i:i+chunk_size])
        chunks.append({"type": "exercise", "content": chunk})

    with open(output_json, 'w') as f:
        json.dump(chunks, f, indent=4)
        
    print(f"Split into {len(chunks)} chunks.")

if __name__ == '__main__':
    split_textbook('/home/ubuntu/Shine_Academy_Naroda/SAN/shineboard_library/class_12/accounts/textbook_gseb_class12_accounts_ch6.txt', '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class12_accounts_ch6_chunks.json')
