import json
import re

def update_curriculum_bold_names(filepath, curriculum_id, updates):
    """Update subject names in a curriculum JSON to have explicit bold book names."""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    changed = 0
    for subject in data.get("subjects", []):
        subj_id = subject.get("id", "")
        if subj_id in updates:
            old_name = subject.get("name", "")
            subject["name"] = updates[subj_id]["name"]
            if "edition" in updates[subj_id]:
                subject["edition"] = updates[subj_id]["edition"]
            if "color_hex" in updates[subj_id]:
                subject["color_hex"] = updates[subj_id]["color_hex"]
            if "icon" in updates[subj_id]:
                subject["icon"] = updates[subj_id]["icon"]
            changed += 1
            print(f"  Updated '{old_name}' -> '{subject['name']}'")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return changed

# ============== NCERT CLASS 9 ==============
ncert9_updates = {
    "ncert_class9_science": {"name": "Science — NCERT Science (New Rationalized Edition)", "edition": "New Rationalized Edition", "color_hex": "0xFF4CAF50", "icon": "science"},
    "ncert_class9_math": {"name": "Mathematics — Ganita Prakash (New 2024 Edition)", "edition": "Ganita Prakash (New Edition)", "color_hex": "0xFF2196F3", "icon": "calculate"},
    "ncert_class9_maths": {"name": "Mathematics — Ganita Prakash (New 2024 Edition)", "edition": "Ganita Prakash (New Edition)", "color_hex": "0xFF2196F3", "icon": "calculate"},
    "ncert_class9_social": {"name": "Social Science — Democratic Politics + India & Contemporary World + Contemporary India", "edition": "NCERT Classic Edition", "color_hex": "0xFF9C27B0", "icon": "book"},
    "ncert_class9_english": {"name": "English — Beehive (Main Textbook) & Moments (Supplementary Reader)", "edition": "Beehive + Moments", "color_hex": "0xFFFF9800", "icon": "menu_book"},
}

# ============== NCERT CLASS 10 ==============
ncert10_updates = {
    "ncert_class10_science": {"name": "Science — NCERT Science (New Rationalized Edition)", "edition": "New Rationalized Edition", "color_hex": "0xFF4CAF50", "icon": "science"},
    "ncert_class10_math": {"name": "Mathematics — Ganita Prakash (New 2024 Edition)", "edition": "Ganita Prakash (New Edition)", "color_hex": "0xFFE91E63", "icon": "calculate"},
    "ncert_class10_social": {"name": "Social Science — History + Civics + Geography + Economics", "edition": "NCERT Classic + Rationalized Edition", "color_hex": "0xFF9C27B0", "icon": "book"},
    "ncert_class10_english": {"name": "English — First Flight (Main Textbook) & Footprints Without Feet (Supplementary)", "edition": "First Flight + Footprints Without Feet", "color_hex": "0xFFFF9800", "icon": "menu_book"},
}

# ============== CBSE CLASS 9 ==============
cbse9_updates = {
    "cbse_class9_science": {"name": "Science — NCERT Science (New CBSE Rationalized Edition)", "edition": "New Rationalized Edition"},
    "cbse_class9_maths_new": {"name": "Mathematics — Ganita Prakash (New 2024 CBSE Edition)", "edition": "Ganita Prakash (New Edition)"},
    "cbse_class9_maths_classic": {"name": "Mathematics — NCERT Mathematics (Classic Full Edition)", "edition": "Classic Full Edition"},
    "cbse_class9_english": {"name": "English — Beehive (Main Textbook) & Moments (Supplementary Reader)", "edition": "Beehive + Moments"},
    "cbse_class9_social": {"name": "Social Science — History, Civics, Geography & Economics", "edition": "NCERT Classic Edition"},
}

# ============== CBSE CLASS 10 ==============
cbse10_updates = {
    "cbse_class10_science": {"name": "Science — NCERT Science (New CBSE Rationalized Edition)", "edition": "New Rationalized Edition"},
    "cbse_class10_math": {"name": "Mathematics — Ganita Prakash (New 2024 CBSE Edition)", "edition": "Ganita Prakash (New Edition)"},
    "cbse_class10_english": {"name": "English — First Flight (Main Textbook) & Footprints Without Feet (Supplementary)", "edition": "First Flight + Footprints Without Feet"},
    "cbse_class10_social": {"name": "Social Science — History + Civics + Geography + Economics", "edition": "NCERT Classic + Rationalized Edition"},
}

curriculum_files = [
    ("app_core/curriculum/ncert_class9.json", "ncert_class9", ncert9_updates),
    ("app_core/curriculum/ncert_class10.json", "ncert_class10", ncert10_updates),
    ("app_core/curriculum/cbse_class9.json", "cbse_class9", cbse9_updates),
    ("app_core/curriculum/cbse_class10.json", "cbse_class10", cbse10_updates),
]

print("=== UPDATING CURRICULUM FILES WITH BOLD BOOK NAMES ===")
for filepath, cid, updates in curriculum_files:
    print(f"\n{filepath}:")
    try:
        c = update_curriculum_bold_names(filepath, cid, updates)
        print(f"  {c} subjects updated.")
    except Exception as e:
        print(f"  ERROR: {e}")

print("\n✅ Done!")
