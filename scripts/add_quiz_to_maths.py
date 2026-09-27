import json
import glob
import os

def generate_questions(chapter_id, chapter_title):
    q_blocks = []
    for i in range(1, 16):
        q_blocks.append({
            "id": f"QUIZ_{chapter_id}_{i}",
            "type": "quiz",
            "question": f"Sample mock test question {i} for {chapter_title}?",
            "question_hi": f"क्या यह {chapter_title} के लिए नमूना मॉक टेस्ट प्रश्न {i} है?",
            "options": [
                "Correct Answer",
                "Incorrect Option 1",
                "Incorrect Option 2",
                "Incorrect Option 3"
            ],
            "options_hi": [
                "सही उत्तर",
                "गलत विकल्प 1",
                "गलत विकल्प 2",
                "गलत विकल्प 3"
            ],
            "correct_index": 0,
            "explanation": f"Explanation for question {i}. This tests your understanding of {chapter_title}.",
            "explanation_hi": f"प्रश्न {i} के लिए स्पष्टीकरण। यह {chapter_title} की आपकी समझ का परीक्षण करता है।"
        })
    return q_blocks

def main():
    chapters_dir = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters"
    files = glob.glob(os.path.join(chapters_dir, "*class10_maths_ch*.json"))
    
    updated = 0
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except:
                continue
                
        is_raw_list = isinstance(data, list)
        blocks = data if is_raw_list else data.get('blocks', [])
        
        has_quiz = any(b.get('type') in ['quiz', 'mcq'] for b in blocks if isinstance(b, dict))
        
        if not has_quiz:
            title = "Maths Chapter"
            ch_id = "CH_UNKNOWN"
            if not is_raw_list:
                title = data.get('metadata', {}).get('title', 'Maths Chapter')
                ch_id = data.get('metadata', {}).get('id', 'CH_UNKNOWN')
            else:
                ch_id = os.path.basename(file).replace('.json', '')
            
            quizzes = generate_questions(ch_id, title)
            blocks.extend(quizzes)
            
            with open(file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            updated += 1
            print(f"Added 15 mock questions to {os.path.basename(file)}")
            
    print(f"Updated {updated} maths chapter files.")

if __name__ == "__main__":
    main()
