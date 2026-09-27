import os
import json
import re
import time
import glob
import google.genai as genai

# Configure API Key
API_KEY = "AIzaSyCXHEJ4KBrebP8ByUEZnVJzuE4u114MGGA"
client = genai.Client(api_key=API_KEY)

MODEL_NAME = 'gemini-3.5-flash-lite'

CHAPTERS_DIR = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters"
UNIVERSAL_DICT_DIR = "/home/ubuntu/Shine_Academy_Naroda/app_core/universal_dictionary"
OUTPUT_FILE = os.path.join(UNIVERSAL_DICT_DIR, "generated_massive_dict.json")

# Simple stop words to ignore
STOP_WORDS = set([
    "the", "and", "a", "to", "of", "in", "i", "is", "that", "it", "on", "you", "this", "for", "but", "with",
    "are", "have", "be", "at", "or", "as", "was", "so", "if", "out", "not", "he", "she", "they", "we", "my",
    "your", "his", "her", "their", "our", "me", "him", "them", "us", "from", "by", "about", "what", "which",
    "when", "where", "who", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other",
    "some", "such", "no", "nor", "too", "very", "can", "will", "just", "then", "there", "now", "up", "down",
    "an", "do", "did", "does", "has", "had", "would", "could", "should", "am", "are", "been", "being"
])

def extract_unique_words():
    print("Scanning all chapters in the application for vocabulary...")
    unique_words = set()
    files = glob.glob(os.path.join(CHAPTERS_DIR, "*.json"))
    
    for f in files:
        try:
            with open(f, 'r', encoding='utf-8') as file:
                content = file.read()
                # Basic tokenization
                words = re.findall(r'\b[a-zA-Z]{3,12}\b', content)
                for w in words:
                    w_lower = w.lower()
                    if w_lower not in STOP_WORDS:
                        unique_words.add(w_lower)
        except Exception as e:
            print(f"Error reading {f}: {e}")
            
    print(f"Total unique English words found in app: {len(unique_words)}")
    return list(unique_words)

def load_existing_words():
    print("Scanning all existing dictionaries to find already defined words...")
    existing_words = set()
    
    # Load all json files in universal_dictionary
    dict_files = glob.glob(os.path.join(UNIVERSAL_DICT_DIR, "*.json"))
    for f in dict_files:
        # Skip index and anomalies files
        if "dictionary_index" in f or "anomalies_to_fix" in f:
            continue
            
        try:
            with open(f, 'r', encoding='utf-8') as file:
                data = json.load(file)
                # Dictionaries have an array called "terms"
                if "terms" in data:
                    for t in data["terms"]:
                        if "term" in t and "english" in t["term"]:
                            existing_words.add(t["term"]["english"].lower())
        except Exception as e:
            pass # Ignore files that don't match standard schema
            
    print(f"Total words already defined in dictionaries: {len(existing_words)}")
    return existing_words

def generate_dictionary_entries(words_batch):
    prompt = f"""
    You are an expert curriculum designer for Shine Academy Naroda.
    Generate a JSON dictionary array for the following English words: {', '.join(words_batch)}.
    
    CRITICAL INSTRUCTION:
    Every single word MUST follow this strict schema, no exceptions!
    
    IMPORTANT RULES:
    1. For the 'part_of_speech' field, use 'noun', 'verb', 'adjective', etc.
    2. YOU MUST PROVIDE EXACTLY 5 EXAMPLE SENTENCES IN THE 'examples' ARRAY FOR EVERY WORD.
    3. Every example sentence MUST have an English ('en'), Hindi ('hi'), and Gujarati ('gu') translation.
    4. For 'pronunciation_hi': Write the English word phonetically in Devanagari script (Hindi letters) so
       a Hindi-speaking student can READ the Devanagari and know how to PRONOUNCE the English word.
       This is NOT the Hindi meaning — it is how the English word SOUNDS written in Hindi script.
       Examples: "sun" → "सन", "apple" → "एपल", "beautiful" → "ब्यूटीफुल", "school" → "स्कूल",
       "water" → "वॉटर", "computer" → "कम्प्यूटर", "friend" → "फ्रेंड", "costly" → "कॉस्टली"
    
    Expected JSON Array format (Return ONLY valid JSON):
    [
      {{
        "id": "DICT_ENG_WORD",
        "term": {{
          "english": "Apple",
          "hindi": "सेब",
          "gujarati": "સફરજન"
        }},
        "pronunciation_hi": "एपल",
        "part_of_speech": "noun",
        "definition": {{
          "simple": {{
            "en": "A round fruit with red or green skin.",
            "hi": "लाल या हरे छिलके वाला एक गोल फल।",
            "gu": "લાલ અથવા લીલી છાલવાળું ગોળ ફળ."
          }},
          "academic": {{
            "en": "The fleshy, usually rounded red, yellow, or green edible pome fruit of a usually cultivated tree (genus Malus) of the rose family."
          }}
        }},
        "examples": [
          {{ "en": "Sentence 1", "hi": "Translation 1", "gu": "Translation 1" }},
          {{ "en": "Sentence 2", "hi": "Translation 2", "gu": "Translation 2" }},
          {{ "en": "Sentence 3", "hi": "Translation 3", "gu": "Translation 3" }},
          {{ "en": "Sentence 4", "hi": "Translation 4", "gu": "Translation 4" }},
          {{ "en": "Sentence 5", "hi": "Translation 5", "gu": "Translation 5" }}
        ],
        "media": {{}},
        "knowledge_graph_links": {{ "related": [], "prerequisites": [], "used_in": [] }},
        "ai_context": {{ "common_misconceptions": [], "tutor_hint": "" }}
      }}
    ]
    """
    
    while True:
        try:
            print(f"Requesting generation for {len(words_batch)} words via Gemini API...")
            response = client.models.generate_content(model=MODEL_NAME, contents=prompt)
            result_text = response.text.strip()
            
            if result_text.startswith('```json'):
                result_text = result_text[7:-3].strip()
            elif result_text.startswith('```'):
                result_text = result_text[3:-3].strip()
                
            data = json.loads(result_text)
            return data
            
        except Exception as e:
            if "429" in str(e) or "Quota exceeded" in str(e):
                print(f"* Quota exceeded. Waiting 60 seconds...")
                time.sleep(60)
            else:
                print(f"[ERROR] Failed to parse or generate for batch: {e}")
                return None

def main():
    print("--- Shine Academy Naroda 100% Dictionary Coverage Tool ---")
    all_words_in_app = extract_unique_words()
    already_defined_words = load_existing_words()
    
    words_to_generate = [w for w in all_words_in_app if w not in already_defined_words]
    
    # Also double check against the output file just in case it was interrupted
    generated_terms = []
    if os.path.exists(OUTPUT_FILE):
        try:
            with open(OUTPUT_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if "terms" in data:
                    generated_terms = data["terms"]
        except Exception:
            pass
            
    already_generated_in_file = set([t["term"]["english"].lower() for t in generated_terms if "term" in t and "english" in t["term"]])
    words_to_generate = [w for w in words_to_generate if w not in already_generated_in_file]
    
    print(f"Total NEW words that need to be added to the dictionary: {len(words_to_generate)}")
    
    if len(words_to_generate) == 0:
        print("Congratulations! 100% Dictionary Coverage Achieved!")
        return
        
    batch_size = 10
    
    for i in range(0, len(words_to_generate), batch_size):
        batch = words_to_generate[i:i+batch_size]
        print(f"\\nProcessing batch {i//batch_size + 1} of {(len(words_to_generate)//batch_size)+1}: {batch}")
        
        new_terms = generate_dictionary_entries(batch)
        if new_terms and isinstance(new_terms, list):
            generated_terms.extend(new_terms)
            
            # Save progress
            with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
                json.dump({"terms": generated_terms}, f, indent=2, ensure_ascii=False)
            print(f"Successfully saved batch. Total terms in massive dictionary: {len(generated_terms)}")
            
        time.sleep(4) # Delay to be polite to the API
        
    print("Finished generating all missing words!")

if __name__ == "__main__":
    main()
