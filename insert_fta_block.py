import json
import glob

def insert_block(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        # For individual chapters
        if 'blocks' in data:
            blocks = data['blocks']
        elif 'modules' in data: # master_curriculum
            print(f"Skipping master curriculum for now, or would need recursive search: {file_path}")
            return
        else:
            return
            
        new_blocks = []
        for block in blocks:
            new_blocks.append(block)
            if block.get('type') == 'theory' and 'Fundamental Theorem of Arithmetic' in block.get('content', ''):
                # Check if diagram is already added
                if not any(b.get('image_url') == 'assets/images/maths_ch1_fta.jpg' for b in blocks):
                    print(f"Adding FTA diagram to {file_path}")
                    new_blocks.append({
                        "type": "diagram",
                        "content": "A Factor Tree for 12, demonstrating the Fundamental Theorem of Arithmetic.",
                        "image_url": "assets/images/maths_ch1_fta.jpg",
                        "alt_text": "Factor tree showing 12 splitting into 2 and 6, and 6 splitting into 2 and 3."
                    })
                    
        data['blocks'] = new_blocks
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            
    except Exception as e:
        print(f"Error in {file_path}: {e}")

files = glob.glob('app_core/chapters/*class10_maths_ch1.json')
for f in files:
    insert_block(f)
