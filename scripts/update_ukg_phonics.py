import json
import os

def update_ukg_phonics():
    print("Updating UKG Phonics chapters 1-5...")
    
    cvc_words = {
        1: {
            "title": "The 'a' sound (CVC)",
            "words": [("c", "a", "t", "cat"), ("m", "a", "t", "mat"), ("b", "a", "t", "bat"), ("r", "a", "t", "rat")]
        },
        2: {
            "title": "The 'e' sound (CVC)",
            "words": [("p", "e", "n", "pen"), ("t", "e", "n", "ten"), ("h", "e", "n", "hen"), ("b", "e", "d", "bed")]
        },
        3: {
            "title": "The 'i' sound (CVC)",
            "words": [("p", "i", "n", "pin"), ("t", "i", "n", "tin"), ("b", "i", "n", "bin"), ("z", "i", "p", "zip")]
        },
        4: {
            "title": "The 'o' sound (CVC)",
            "words": [("d", "o", "g", "dog"), ("l", "o", "g", "log"), ("f", "o", "g", "fog"), ("t", "o", "p", "top")]
        },
        5: {
            "title": "The 'u' sound (CVC)",
            "words": [("s", "u", "n", "sun"), ("b", "u", "n", "bun"), ("r", "u", "n", "run"), ("j", "u", "g", "jug")]
        }
    }
    
    updated_count = 0
    
    for i in range(1, 6):
        filepath = f"app_core/chapters/ukg_phonics_ch{i}.json"
        
        if not os.path.exists(filepath):
            continue
            
        chapter_info = cvc_words[i]
        
        blocks = [
            {
                "id": f"KOBJ_UKG_PHON_{i}_01",
                "type": "hook",
                "title": "Three Letter Words!",
                "body": "Tap the big green play button to hear the 3 letters blend together into a word!"
            }
        ]
        
        # Add phonics blender blocks
        for j, (l1, l2, l3, result) in enumerate(chapter_info["words"]):
            blocks.append({
                "id": f"KOBJ_UKG_PHON_{i}_0{j+2}",
                "type": "phonics_blender",
                "parts": [l1, l2, l3],
                "result": result
            })
            
        blocks.append({
            "id": f"KOBJ_UKG_PHON_{i}_99",
            "type": "quiz",
            "question": f"Which of these words did we just read?",
            "options": [chapter_info["words"][0][3], "zoo", "car"],
            "correct_index": 0,
            "explanation": "Great job paying attention!"
        })
        
        data = {
            "metadata": {
                "id": f"ukg_phonics_ch{i}",
                "title": chapter_info["title"],
                "subject": "Phonics & Words",
                "difficulty": "Beginner",
                "estimated_minutes": 15
            },
            "blocks": blocks
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            
        updated_count += 1
        
    print(f"Updated {updated_count} UKG Phonics chapters.")

if __name__ == "__main__":
    update_ukg_phonics()
