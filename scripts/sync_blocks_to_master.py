import json
import os
import glob

def sync_all_blocks_to_master():
    master_file = "/home/ubuntu/Shine_Academy_Naroda/app_core/learning_modules/master_curriculum.json"
    
    print("Loading master_curriculum.json...")
    try:
        with open(master_file, 'r', encoding='utf-8') as f:
            master_data = json.load(f)
    except Exception as e:
        print(f"Error loading master_curriculum: {e}")
        return

    modules_dir = "/home/ubuntu/Shine_Academy_Naroda/app_core/learning_modules"
    blocks_files = glob.glob(f"{modules_dir}/*/blocks.json")
    
    updated_count = 0
    
    for block_file in blocks_files:
        module_id = os.path.basename(os.path.dirname(block_file))
        
        # Only update if this module already exists in the master curriculum
        if module_id in master_data:
            try:
                with open(block_file, 'r', encoding='utf-8') as f:
                    blocks_data = json.load(f)
                
                # Check if it's a list (just blocks) or a dict with a 'blocks' key
                if isinstance(blocks_data, list):
                    master_data[module_id]["blocks"] = blocks_data
                elif isinstance(blocks_data, dict) and "blocks" in blocks_data:
                    master_data[module_id]["blocks"] = blocks_data["blocks"]
                    
                updated_count += 1
                print(f"Synced changes for: {module_id}")
            except Exception as e:
                print(f"Error reading {block_file}: {e}")
    
    print(f"\nWriting updated data back to {master_file}...")
    with open(master_file, 'w', encoding='utf-8') as f:
        json.dump(master_data, f, indent=2, ensure_ascii=False)
        
    print(f"Success! {updated_count} modules were synced to the master curriculum.")

if __name__ == "__main__":
    sync_all_blocks_to_master()
