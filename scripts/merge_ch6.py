import json
import os

def merge_chunks():
    chunks_dir = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ch6_chunks"
    output_file = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class12_accounts_ch6.json"
    
    all_blocks = []
    
    # Process chunks 1 to 15 in order
    for i in range(1, 16):
        chunk_file = os.path.join(chunks_dir, f"chunk_{i}.json")
        if not os.path.exists(chunk_file):
            print(f"Warning: {chunk_file} does not exist.")
            continue
            
        with open(chunk_file, "r", encoding="utf-8") as f:
            try:
                blocks = json.load(f)
                if isinstance(blocks, list):
                    for block in blocks:
                        if "id" not in block:
                            print(f"Warning: block in chunk {i} missing ID")
                        all_blocks.append(block)
                else:
                    print(f"Warning: {chunk_file} does not contain a JSON array.")
            except json.JSONDecodeError as e:
                print(f"Error decoding {chunk_file}: {e}")
                
    print(f"Total blocks merged: {len(all_blocks)}")
    
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(all_blocks, f, indent=2, ensure_ascii=False)
    print(f"Saved merged JSON to {output_file}")

if __name__ == "__main__":
    merge_chunks()
