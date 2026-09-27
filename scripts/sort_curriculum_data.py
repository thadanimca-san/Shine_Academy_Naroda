import os
import glob
import json
import shutil

def sort_curriculum():
    source_dir = 'app_core/chapters'
    future_dir = 'app_core/maybe_used_in_future'
    
    if not os.path.exists(future_dir):
        os.makedirs(future_dir)
        
    files = glob.glob(os.path.join(source_dir, '*.json'))
    if not files:
        print("No JSON files found in app_core/chapters/")
        return
        
    stats = {
        'deleted': 0,
        'moved': 0,
        'kept': 0
    }
    
    print("=========================================================")
    print("DATA SORTING ENGINE: TRASH vs FUTURE vs ACTIVE")
    print("=========================================================\n")
    
    for file_path in files:
        filename = os.path.basename(file_path)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception as e:
            # Corrupted JSON -> Useless
            print(f"🗑️ DELETING (Corrupted): {filename}")
            os.remove(file_path)
            stats['deleted'] += 1
            continue
            
        blocks = []
        is_old_format = False
        
        if isinstance(data, list):
            blocks = data
            is_old_format = True
        else:
            blocks = data.get('blocks', [])
            
        num_blocks = len(blocks)
        
        # Rule 1: Useless Data (Delete)
        # Any chapter with less than 10 blocks is considered lazy/useless because 
        # it means textbook exercises and pedagogy were skipped.
        if num_blocks < 10:
            print(f"🗑️ DELETING (Only {num_blocks} blocks): {filename}")
            os.remove(file_path)
            stats['deleted'] += 1
            continue
            
        # Rule 2: Future Use (Move)
        # Check for missing translations or old array formats
        missing_translations = 0
        missing_solutions = 0
        lazy_options = 0
        
        for block in blocks:
            # Check translations
            keys_to_translate = [k for k, v in block.items() if isinstance(v, str) and not k.endswith('_hi') and not k.endswith('_gu') and k not in ['id', 'type', 'media_url']]
            for k in keys_to_translate:
                if (k + '_hi') not in block or (k + '_gu') not in block:
                    missing_translations += 1
                    
            # Check lazy options
            if 'options' in block:
                for opt in block['options']:
                    if opt.lower().strip() in ['option a', 'option b', 'option c', 'option d', 'option 1', 'option 2']:
                        lazy_options += 1
                        
            # Check missing solutions
            if block.get('type') in ['practice_question', 'numerical']:
                if 'solution' not in block or len(block['solution']) < 20:
                    missing_solutions += 1
                    
        # If there is ANY kaamchori, or if it's the old format, it gets moved to future use
        if missing_translations > 0 or missing_solutions > 0 or lazy_options > 0 or is_old_format:
            dest_path = os.path.join(future_dir, filename)
            print(f"📦 MOVING TO FUTURE USE (Missing Trans: {missing_translations}, Missing Sol: {missing_solutions}): {filename}")
            shutil.move(file_path, dest_path)
            stats['moved'] += 1
            continue
            
        # Rule 3: Gold Standard (Keep Active)
        print(f"✅ RETAINING ACTIVE (Gold Standard): {filename}")
        stats['kept'] += 1

    print("\n=========================================================")
    print("SORTING SUMMARY:")
    print(f"Deleted (Useless Data): {stats['deleted']}")
    print(f"Moved to maybe_used_in_future: {stats['moved']}")
    print(f"Retained in Active Chapters: {stats['kept']}")
    print("=========================================================")

if __name__ == "__main__":
    sort_curriculum()
