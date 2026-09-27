import json
import os
import glob
import time
import re
from deep_translator import GoogleTranslator

# Initialize translators
translator_hi = GoogleTranslator(source='en', target='hi')
translator_gu = GoogleTranslator(source='en', target='gu')

# Regex to strip inline translations like: (लोहे पर जंग लगना / લોખંડને કાટ લાગવો)
# or 'लोहे पर जंग लगना / લોખંડને કાટ લાગવો'
inline_trans_pattern = re.compile(r'[\(\'\"\[]?\s*[\u0900-\u097F]+[\s/\|\\]+[\u0A80-\u0AFF]+\s*[\)\'\"\]]?')


# Fields to translate in blocks
FIELDS_TO_TRANSLATE = ['body', 'title', 'question', 'explanation', 'feedback_correct', 'term', 'definition', 'tip', 'guidance']

# Dictionary files also have special fields
DICT_FIELDS = ['word', 'meaning', 'example_sentence', 'etymology']

def clean_inline_text(text):
    if not text or not isinstance(text, str):
        return text
    # Remove inline translations
    cleaned = inline_trans_pattern.sub('', text)
    # Also clean single brackets that might have been left behind
    cleaned = re.sub(r'\s*\(\s*\)\s*', ' ', cleaned)
    # Remove double spaces
    cleaned = re.sub(r'\s{2,}', ' ', cleaned)
    return cleaned.strip()

def safe_translate(translator, text, max_retries=5):
    if not text or not isinstance(text, str):
        return text
    if text.strip() == '':
        return text
    
    # Split text into chunks by double newline to avoid Google Translator limits on complex mathematical texts
    chunks = text.split('\n\n')
    translated_chunks = []
    
    for chunk in chunks:
        if chunk.strip() == '':
            translated_chunks.append(chunk)
            continue
            
        chunk_res = None
        backoff = 2
        for attempt in range(max_retries):
            try:
                if len(chunk) > 4900:
                    chunk_res = translator.translate(chunk[:4900])
                else:
                    chunk_res = translator.translate(chunk)
                    
                if chunk_res:
                    time.sleep(0.5) # Prevent rate limiting
                    break
                
            except Exception as e:
                print(f"Translation error on attempt {attempt+1}: {e}")
                time.sleep(backoff)
                backoff *= 2
                
        if chunk_res:
            translated_chunks.append(chunk_res)
        else:
            print(f"Failed to translate chunk after {max_retries} attempts, keeping original.")
            translated_chunks.append(chunk)
            
    return '\n\n'.join(translated_chunks)

def safe_translate_options(translator, options):
    if not isinstance(options, list):
        return options
    translated_options = []
    for opt in options:
        if isinstance(opt, str):
            translated_options.append(safe_translate(translator, opt))
        else:
            translated_options.append(opt)
    return translated_options

def safe_translate_list(translator, str_list):
    if not isinstance(str_list, list):
        return str_list
    return [safe_translate(translator, s) if isinstance(s, str) else s for s in str_list]

def process_file(file_path):
    if 'languages/' in file_path:
        return False
        
    print(f"Processing: {file_path}")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        modified = False
        
        # Determine file type
        blocks = []
        is_dict = False
        
        if isinstance(data, list):
            blocks = data
        elif 'blocks' in data:
            blocks = data['blocks']
        elif 'content' in data and isinstance(data['content'], list):
            blocks = data['content']
        elif 'entries' in data and isinstance(data['entries'], list):
            # It's a dictionary file
            blocks = data['entries']
            is_dict = True
            
        if not blocks:
            # Maybe it's a single dict entry file (not a list)?
            if 'word' in data and 'meaning' in data:
                blocks = [data]
                is_dict = True
            else:
                print(f"Skipping {file_path} - No recognizable blocks found")
                return False

        fields_to_check = DICT_FIELDS if is_dict else FIELDS_TO_TRANSLATE

        for block in blocks:
            for field in fields_to_check:
                if field in block and block[field]:
                    hi_key = f"{field}_hi"
                    gu_key = f"{field}_gu"
                    
                    # Clean the English text first
                    original_text = block[field]
                    cleaned_text = clean_inline_text(original_text)
                    if cleaned_text != original_text:
                        block[field] = cleaned_text
                        modified = True
                        
                    # Always re-translate if we just cleaned it, or if missing/placeholder
                    if cleaned_text != original_text or hi_key not in block or '[HINDI]' in str(block.get(hi_key, '')):
                        block[hi_key] = safe_translate(translator_hi, block[field])
                        modified = True
                        
                    if cleaned_text != original_text or gu_key not in block or '[GUJARATI]' in str(block.get(gu_key, '')):
                        block[gu_key] = safe_translate(translator_gu, block[field])
                        modified = True
            
            if not is_dict:
                # Handle options list specifically for MCQ
                if 'options' in block and isinstance(block['options'], list) and len(block['options']) > 0:
                    if 'options_hi' not in block or any('[HINDI]' in str(o) for o in block.get('options_hi', [])):
                        block['options_hi'] = safe_translate_options(translator_hi, block['options'])
                        modified = True
                    if 'options_gu' not in block or any('[GUJARATI]' in str(o) for o in block.get('options_gu', [])):
                        block['options_gu'] = safe_translate_options(translator_gu, block['options'])
                        modified = True
            else:
                # Handle dictionary specific array fields
                for list_field in ['examples', 'synonyms', 'antonyms']:
                    if list_field in block and isinstance(block[list_field], list) and len(block[list_field]) > 0:
                        hi_key = f"{list_field}_hi"
                        gu_key = f"{list_field}_gu"
                        
                        if hi_key not in block:
                            block[hi_key] = safe_translate_list(translator_hi, block[list_field])
                            modified = True
                        if gu_key not in block:
                            block[gu_key] = safe_translate_list(translator_gu, block[list_field])
                            modified = True

        if modified:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"Successfully translated and saved: {file_path}")
            return True
        else:
            print(f"No translation needed for: {file_path}")
            return False
            
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    # Gather all JSON files
    all_files = glob.glob('app_core/**/*.json', recursive=True)
    
    print(f"Found {len(all_files)} JSON files to process.")
    for file in all_files:
        process_file(file)

if __name__ == "__main__":
    main()
