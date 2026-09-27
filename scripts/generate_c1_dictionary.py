import json
import os
from datetime import datetime

def save_json(filepath, data):
    # Ensure directory exists
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def generate_c1_dictionary():
    print("Generating Class 1 Dictionary for Knowledge Graph...")
    
    current_time = datetime.utcnow().isoformat() + "Z"
    
    # 4 Foundational terms for the 4 subjects
    terms = [
        {
            "id": "DICT_C1_MAT_CORE",
            "term": "Numbers and Counting",
            "definition": "The foundation of mathematics. Using numbers to count, add, and measure.",
            "subject": "Mathematics",
            "related": ["DICT_C1_ADDITION", "DICT_C1_SUBTRACTION"],
            "used_in": ["class1_maths_ch1", "class1_maths_ch2", "class1_maths_ch3"]
        },
        {
            "id": "DICT_C1_ENG_CORE",
            "term": "English Grammar",
            "definition": "The rules for forming words and sentences in the English language.",
            "subject": "English",
            "related": ["DICT_C1_NOUN", "DICT_C1_VERB"],
            "used_in": ["class1_english_ch4", "class1_english_ch5", "class1_english_ch6"]
        },
        {
            "id": "DICT_C1_EVS_CORE",
            "term": "Environmental Studies",
            "definition": "The study of our surroundings, including our body, family, plants, animals, and earth.",
            "subject": "EVS",
            "related": ["DICT_C1_BODY", "DICT_C1_NATURE"],
            "used_in": ["class1_evs_ch1", "class1_evs_ch2", "class1_evs_ch14", "class1_evs_ch15"]
        },
        {
            "id": "DICT_C1_HIN_CORE",
            "term": "Hindi Varnamala",
            "definition": "The alphabet of the Hindi language, consisting of Swar (vowels) and Vyanjan (consonants).",
            "subject": "Hindi",
            "related": ["DICT_C1_SWAR", "DICT_C1_VYANJAN"],
            "used_in": ["class1_hindi_ch1", "class1_hindi_ch2"]
        }
    ]
    
    # Also add the related sub-terms so there are no broken links in the Knowledge Graph
    sub_terms = [
        ("DICT_C1_ADDITION", "Addition", "Putting things together to find the total.", "Mathematics"),
        ("DICT_C1_SUBTRACTION", "Subtraction", "Taking things away to find what is left.", "Mathematics"),
        ("DICT_C1_NOUN", "Noun", "A naming word for a person, place, animal, or thing.", "English"),
        ("DICT_C1_VERB", "Verb", "An action word that tells what someone or something is doing.", "English"),
        ("DICT_C1_BODY", "Human Body", "The physical structure of a human, including eyes, nose, hands, and legs.", "EVS"),
        ("DICT_C1_NATURE", "Nature", "The physical world around us, including plants, animals, and water.", "EVS"),
        ("DICT_C1_SWAR", "Swar", "Hindi vowels, starting with अ.", "Hindi"),
        ("DICT_C1_VYANJAN", "Vyanjan", "Hindi consonants, starting with क.", "Hindi")
    ]
    
    for id, term, definition, subject in sub_terms:
        terms.append({
            "id": id,
            "term": term,
            "definition": definition,
            "subject": subject,
            "related": [],
            "used_in": []
        })
    
    for term_data in terms:
        dict_obj = {
            "metadata": {
                "id": term_data["id"],
                "term": term_data["term"],
                "subject": term_data["subject"],
                "grade": "1",
                "difficulty": "Beginner",
                "last_updated": current_time
            },
            "definition": term_data["definition"],
            "relationships": {
                "related": term_data["related"],
                "prerequisites": [],
                "used_in": term_data["used_in"]
            }
        }
        
        filepath = f"app_core/dictionary/{term_data['id'].lower()}.json"
        save_json(filepath, dict_obj)
        print(f"Generated Dictionary Term: {term_data['term']}")

if __name__ == "__main__":
    generate_c1_dictionary()
