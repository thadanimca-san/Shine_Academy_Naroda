import json
import sqlite3
import os

def init_db(db_path):
    if os.path.exists(db_path):
        os.remove(db_path)
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE terms (
            id TEXT PRIMARY KEY,
            word_en TEXT,
            word_hi TEXT,
            word_gu TEXT,
            source_file TEXT,
            data JSON
        )
    ''')
    
    cursor.execute('CREATE INDEX idx_word_en ON terms(word_en)')
    cursor.execute('CREATE INDEX idx_word_hi ON terms(word_hi)')
    cursor.execute('CREATE INDEX idx_word_gu ON terms(word_gu)')
    
    return conn, cursor

def process_file(cursor, filepath):
    if not os.path.exists(filepath):
        print(f"Warning: File {filepath} does not exist.")
        return 0

    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    count = 0
    terms = data.get('terms', [])
    for term in terms:
        term_id = term.get('id')
        if not term_id:
            continue
            
        term_data = term.get('term', {})
        word_en = str(term_data.get('english', '')).lower().strip()
        word_hi = str(term_data.get('hindi', term_data.get('hi', ''))).lower().strip()
        word_gu = str(term_data.get('gujarati', term_data.get('gu', ''))).lower().strip()
        
        cursor.execute('''
            INSERT OR REPLACE INTO terms (id, word_en, word_hi, word_gu, source_file, data)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (term_id, word_en, word_hi, word_gu, filepath, json.dumps(term, ensure_ascii=False)))
        count += 1
        
    return count

def main():
    base_dir = '/home/ubuntu/Shine_Academy_Naroda'
    index_path = os.path.join(base_dir, 'app_core/universal_dictionary/dictionary_index.json')
    db_path = os.path.join(base_dir, 'assets/dictionary/universal_dictionary.db')
    
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn, cursor = init_db(db_path)
    
    total_count = 0
    with open(index_path, 'r', encoding='utf-8') as f:
        index_data = json.load(f)
        
    for entry in index_data.get('index', []):
        file_rel = entry.get('file')
        if file_rel:
            filepath = os.path.join(base_dir, file_rel)
            print(f"Processing {filepath}...")
            count = process_file(cursor, filepath)
            total_count += count
            
    conn.commit()
    conn.close()
    print(f"Successfully compiled {total_count} terms into {db_path}")

if __name__ == '__main__':
    main()
