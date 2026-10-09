import os
import json

def inspect_details():
    for i in range(1, 15):
        fn = f"app_core/chapters/ncert_class10_maths_ch{i}.json"
        if os.path.exists(fn):
            with open(fn, 'r', encoding='utf-8') as f:
                data = json.load(f)
            blocks = data if isinstance(data, list) else data.get("blocks", [])
            
            types = {}
            missing_hi = 0
            missing_gu = 0
            for b in blocks:
                t = b.get("type", "unknown")
                types[t] = types.get(t, 0) + 1
                for k in ["title", "body", "question", "explanation"]:
                    if k in b and f"{k}_hi" not in b: missing_hi += 1
                    if k in b and f"{k}_gu" not in b: missing_gu += 1
                if "options" in b:
                    if "options_hi" not in b: missing_hi += 1
                    if "options_gu" not in b: missing_gu += 1
                    
            print(f"Ch {i}: {len(blocks)} blocks | wrapped={isinstance(data, dict)} | missing_hi={missing_hi}, missing_gu={missing_gu} | types={types}")

if __name__ == "__main__":
    inspect_details()
