import json
import glob
from googletrans import Translator
import time

translator = Translator()

def chunk_text(text):
    return [c for c in text.split('\n') if c.strip()]

def safe_translate(text, dest_lang):
    if not text or not text.strip():
        return text
    
    chunks = chunk_text(text)
    translated_chunks = []
    
    for chunk in chunks:
        try:
            res = translator.translate(chunk, src='en', dest=dest_lang)
            translated_chunks.append(res.text)
            time.sleep(0.5)
        except Exception as e:
            print(f"Failed to translate: {chunk[:20]}... Error: {e}")
            translated_chunks.append(chunk)
            
    return '\n'.join(translated_chunks)

def process_file(file_path):
    print(f"Processing: {file_path}")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        modified = False
        blocks = data.get('blocks', [])
        
        for block in blocks:
            for field in ['body', 'title', 'question', 'feedback_correct', 'term', 'definition', 'tip', 'guidance']:
                if field in block and block[field]:
                    # Fill Hindi
                    if f"{field}_hi" not in block or '[HINDI]' in str(block.get(f"{field}_hi", '')):
                        print(f"Translating {field} to hi...")
                        block[f"{field}_hi"] = safe_translate(block[field], 'hi')
                        modified = True
                        
                    # Fill Gujarati
                    if f"{field}_gu" not in block or '[GUJARATI]' in str(block.get(f"{field}_gu", '')):
                        print(f"Translating {field} to gu...")
                        block[f"{field}_gu"] = safe_translate(block[field], 'gu')
                        modified = True
                        
        if modified:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"Saved: {file_path}")
            
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

process_file('SAN/Year2026/10maths/learn_ch1.json')
process_file('SAN/Year2026/10maths/practice_ch1.json')
