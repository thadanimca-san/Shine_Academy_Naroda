import json
import os

def update_lkg_phonics():
    print("Updating LKG Phonics chapters 1-4...")
    
    blends = {
        1: {
            "title": "The 'A' Blend (am, an, at, as)",
            "words": [("a", "m", "am"), ("a", "n", "an"), ("a", "t", "at"), ("a", "s", "as")]
        },
        2: {
            "title": "The 'I' Blend (in, is, it, if)",
            "words": [("i", "n", "in"), ("i", "s", "is"), ("i", "t", "it"), ("i", "f", "if")]
        },
        3: {
            "title": "The 'O' Blend (on, of, or, ox)",
            "words": [("o", "n", "on"), ("o", "f", "of"), ("o", "r", "or"), ("o", "x", "ox")]
        },
        4: {
            "title": "The 'U' Blend (up, us)",
            "words": [("u", "p", "up"), ("u", "s", "us")]
        }
    }
    
    updated_count = 0
    
    for i in range(1, 5):
        filepath = f"app_core/chapters/lkg_phonics_ch{i}.json"
        
        if not os.path.exists(filepath):
            continue
            
        chapter_info = blends[i]
        
        blocks = [
            {
                "id": f"KOBJ_LKG_PHON_{i}_01",
                "type": "hook",
                "title": "Let's Blend!",
                "body": "Tap the big green play button to hear the sounds blend together!"
            }
        ]
        
        # Add phonics blender blocks
        for j, (l1, l2, result) in enumerate(chapter_info["words"]):
            blocks.append({
                "id": f"KOBJ_LKG_PHON_{i}_0{j+2}",
                "type": "phonics_blender",
                "parts": [l1, l2],
                "result": result
            })
            
        blocks.append({
            "id": f"KOBJ_LKG_PHON_{i}_99",
            "type": "quiz",
            "question": f"Which of these is a real word we just learned?",
            "options": [chapter_info["words"][0][2], "zoo", "car"],
            "correct_index": 0,
            "explanation": "Great job listening!"
        })
        
        data = {
            "metadata": {
                "id": f"lkg_phonics_ch{i}",
                "title": chapter_info["title"],
                "subject": "Two-Letter Phonics",
                "difficulty": "Beginner",
                "estimated_minutes": 15
            },
            "blocks": blocks
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            
        updated_count += 1
        
    print(f"Updated {updated_count} LKG Phonics chapters.")

if __name__ == "__main__":
    update_lkg_phonics()
