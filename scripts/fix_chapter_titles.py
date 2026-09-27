import json
import glob

titles = {
    1: "Rajput Age : New Ruler and States",
    2: "The Delhi Sultanate",
    3: "Mughal Empire",
    4: "Medieval Architecture, Cities, Merchants and Craftsman",
    5: "Adivasis",
    6: "Nomadic and Denotified Tribes",
    7: "Bhakti Age : Religious Sects and Saints",
    8: "Formation of Regional Culture",
    9: "Political Rulers of 18th Century",
    10: "Earth's Internal Composition and Landforms",
    11: "Components of the Environment and Interrelationships",
    12: "Effects of Atmosphere on Living Beings",
    13: "Disaster Management",
    14: "Conservation and Preservation of Resources",
    15: "Equality in Democracy",
    16: "State Government",
    17: "Gender Discrimination",
    18: "Means of Communication and Advertisement",
    19: "Markets",
    20: "Let's test the understanding"
}

files = glob.glob('app_core/chapters/gseb_class7_social_science_ch*.json')

for filepath in files:
    try:
        chapter_num_str = filepath.split('_ch')[-1].split('.json')[0]
        chapter_num = int(chapter_num_str)
        
        if chapter_num in titles:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Update metadata
            if 'metadata' in data:
                data['metadata']['title'] = titles[chapter_num]
            
            # Update chapter_title block if it exists
            if 'blocks' in data:
                for block in data['blocks']:
                    if block.get('type') == 'chapter_title':
                        block['title'] = titles[chapter_num]
                        # some might have title_hi, title_gu, but for now we update the English one.
                        # Wait, what if it's "Chapter X: Title"? Let's just set it to the title from the index.
                        
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
                
            print(f"Updated {filepath}")
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

