import json
import os
from datetime import datetime

def merge_chunks():
    chunks_dir = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class12_accounts_ch6_chunks'
    output_file = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class12_accounts_ch6.json'
    
    blocks = []
    
    # Read chunks 1 to 7 sequentially
    for i in range(1, 8):
        chunk_file = os.path.join(chunks_dir, f'chunk_{i}.json')
        if os.path.exists(chunk_file):
            try:
                with open(chunk_file, 'r', encoding='utf-8') as f:
                    chunk_data = json.load(f)
                    if isinstance(chunk_data, list):
                        blocks.extend(chunk_data)
                    else:
                        print(f"Warning: {chunk_file} does not contain a list of blocks.")
            except Exception as e:
                print(f"Error reading {chunk_file}: {e}")
        else:
            print(f"Warning: {chunk_file} not found. Subagent might have failed.")
            
    final_json = {
        "metadata": {
            "id": "ACC_GSEB_12_CH6",
            "title": "Retirement / Death of a Partner",
            "title_hi": "साझेदार की निवृत्ति / मृत्यु",
            "title_gu": "ભાગીદારની નિવૃત્તિ / મૃત્યુ",
            "subtitle": "Chapter 6 - Elements of Accounts Part I",
            "subtitle_hi": "अध्याय 6 - खातों के तत्व भाग I",
            "subtitle_gu": "પ્રકરણ 6 - નામાનાં મૂળતત્ત્વો ભાગ I",
            "subject": "Accounts",
            "grade": "12",
            "board": "GSEB",
            "curriculum": ["GSEB", "CBSE"],
            "language": "en, hi, gu",
            "difficulty": "Intermediate",
            "estimated_minutes": 180,
            "version": "2.0.0",
            "author": "Antigravity_EduOS",
            "reviewed_by": "System",
            "last_updated": datetime.utcnow().isoformat() + "Z",
            "tags": ["retirement", "death", "partner", "accounts", "goodwill", "revaluation"],
            "learning_outcomes": [
                "Understand the circumstances of retirement of a partner.",
                "Calculate new profit and loss sharing ratio and gaining ratio.",
                "Accounting treatment of goodwill on retirement/death.",
                "Revaluation of assets and liabilities.",
                "Determine amount payable to retiring/deceased partner."
            ],
            "ai_context": {
                "learning_goal": "Master the accounting entries and logic for a partner leaving the firm.",
                "common_misconceptions": [
                    "Students confuse sacrificing ratio (used in admission) with gaining ratio (used in retirement)."
                ],
                "tutor_hint": "Always remind students that the continuing partners compensate the retiring partner for their share of goodwill.",
                "next_topics": []
            }
        },
        "blocks": blocks
    }
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(final_json, f, indent=4, ensure_ascii=False)
        
    print(f"Successfully generated {output_file} with {len(blocks)} blocks.")

if __name__ == '__main__':
    merge_chunks()
