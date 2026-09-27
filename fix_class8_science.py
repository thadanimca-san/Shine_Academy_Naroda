import json
import os

# Titles for all 18 chapters
titles = {
    1: "Crop Production and Management",
    2: "Microorganisms: Friend and Foe",
    3: "Synthetic Fibres and Plastics",
    4: "Materials: Metals and Non-Metals",
    5: "Coal and Petroleum",
    6: "Combustion and Flame",
    7: "Conservation of Plants and Animals",
    8: "Cell - Structure and Functions",
    9: "Reproduction in Animals",
    10: "Reaching the Age of Adolescence",
    11: "Force and Pressure",
    12: "Friction",
    13: "Sound",
    14: "Chemical Effects of Electric Current",
    15: "Some Natural Phenomena",
    16: "Light",
    17: "Stars and the Solar System",
    18: "Pollution of Air and Water"
}

# The Gold Standard file mappings (if exists)
gold_standard_files = {
    4: "GSEB_SCI_08_CH04",
    5: "GSEB_SCI8_CH5",
    6: "GSEB_SCI_08_CH06",
    8: "GSEB_SCI_C8_CH8",
    9: "GSEB_SCI_8_CH9",
    10: "GSEB_SCI_8_CH10",
    15: "GSEB_SCI_08_CH15",
    17: "GSEB_SCI_8_CH17"
}

# Where the true blocks are currently hiding for non-gold chapters
# Format: { chapter_num: 'source_file_path' }
source_files = {
    1: "app_core/chapters/gseb_class8_science_ch1.json",
    2: "app_core/chapters/gseb_class8_science_ch2.json",
    3: "app_core/chapters/gseb_class8_science_ch3.json",
    7: "app_core/chapters/gseb_class8_science_ch5.json", # Data shifted here
    12: "app_core/chapters/gseb_class8_science_ch9.json", # Data shifted here
    14: "app_core/chapters/gseb_class8_science_ch11.json", # Data shifted here
    16: "app_core/chapters/gseb_class8_science_ch13.json" # Data shifted here
}

def create_empty_blocks(title):
    return [
        {
            "type": "hook",
            "content": f"Welcome to '{title}'! Content is coming soon."
        }
    ]

# 1. First, create repaired files for all non-gold chapters
for ch_num in range(1, 19):
    if ch_num in gold_standard_files:
        continue # We'll just point curriculum to Gold Standard

    title = titles[ch_num]
    new_id = f"gseb_class8_science_ch{ch_num}"
    
    # Get blocks
    blocks = []
    if ch_num in source_files and os.path.exists(source_files[ch_num]):
        with open(source_files[ch_num], 'r') as f:
            data = json.load(f)
            blocks = data.get('blocks', [])
            if not blocks:
                blocks = create_empty_blocks(title)
    else:
        blocks = create_empty_blocks(title)

    # Build new json
    new_data = {
        "metadata": {
            "title": title,
            "subject": "Science",
            "grade": "8",
            "curriculum": ["GSEB", "NCERT", "CBSE"],
            "difficulty": "Intermediate",
            "version": "4.0.0",
            "id": new_id
        },
        "blocks": blocks
    }
    
    # Save it (overwriting if needed, but since we are doing this in-memory and saving to the correct names, it's fine)
    # Note: we should write them to a temp directory first so we don't overwrite files we still need to read from.
    os.makedirs('temp_chapters', exist_ok=True)
    with open(f"temp_chapters/{new_id}.json", 'w') as f:
        json.dump(new_data, f, indent=2)

# Move temp files to main directory
for ch_num in range(1, 19):
    if ch_num in gold_standard_files:
        continue
    new_id = f"gseb_class8_science_ch{ch_num}"
    os.rename(f"temp_chapters/{new_id}.json", f"app_core/chapters/{new_id}.json")
os.rmdir('temp_chapters')

# 2. Rebuild the curriculum index for Science
curriculum_file = 'app_core/curriculum/gseb_class8.json'
with open(curriculum_file, 'r') as f:
    curriculum = json.load(f)

for subject in curriculum.get('subjects', []):
    if subject['id'] == 'gseb_class8_science':
        # Keep simulations
        simulations = [ch for ch in subject['chapters'] if 'sci_sim:' in ch['module_id'] or '[Simulation]' in ch['title']]
        
        # Build perfect chapter list
        new_chapters = []
        for ch_num in range(1, 19):
            module_id = gold_standard_files[ch_num] if ch_num in gold_standard_files else f"gseb_class8_science_ch{ch_num}"
            new_chapters.append({
                "chapter_id": module_id,
                "title": f"Chapter {ch_num}: {titles[ch_num]}",
                "module_id": module_id
            })
            
        subject['chapters'] = new_chapters + simulations
        break

with open(curriculum_file, 'w') as f:
    json.dump(curriculum, f, indent=2, ensure_ascii=False)

print("Class 8 Science repaired successfully!")
