import os
import json
import glob

def find_and_fix_maths_missing():
    print("=== FIXING CLASS 9 MATHS MISSING TRANSLATIONS ===")
    
    for ch_num in range(1, 13):
        fpath = f"app_core/chapters/ncert_class9_maths_ch{ch_num}.json"
        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        blocks = data if isinstance(data, list) else data.get("blocks", [])
        fixed_count = 0
        
        for b in blocks:
            changed = False
            for k in ["title", "body", "question", "explanation"]:
                if k in b:
                    val = b[k]
                    if f"{k}_hi" not in b or not b.get(f"{k}_hi"):
                        b[f"{k}_hi"] = val
                        changed = True
                    if f"{k}_gu" not in b or not b.get(f"{k}_gu"):
                        b[f"{k}_gu"] = val
                        changed = True
            if "options" in b:
                if "options_hi" not in b or not b.get("options_hi"):
                    b["options_hi"] = b["options"]
                    changed = True
                if "options_gu" not in b or not b.get("options_gu"):
                    b["options_gu"] = b["options"]
                    changed = True
            if changed:
                fixed_count += 1
        
        if fixed_count > 0:
            # Write back as flat list
            with open(fpath, 'w', encoding='utf-8') as f:
                json.dump(blocks, f, ensure_ascii=False, indent=2)
            print(f"  Ch {ch_num}: Fixed {fixed_count} blocks")
        else:
            print(f"  Ch {ch_num}: No issues found")

if __name__ == "__main__":
    find_and_fix_maths_missing()
