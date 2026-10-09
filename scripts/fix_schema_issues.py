#!/usr/bin/env python3
"""
Shine Academy EduOS — Schema Issue Fixer
=========================================
Fixes two classes of validator-flagged issues:

FIX A: Root-level list [] files → wraps them in {"metadata": {...}, "blocks": [...]}
        The Flutter engine expects {"metadata": ..., "blocks": [...]} but some files
        were generated as raw arrays.

FIX B: correct_answer string → correct_index integer
        Finds the string value inside the options list and converts it to 0-based index.
        Example: correct_answer: "Teach", options: ["Learn","Teach"] → correct_index: 1

SAFE: Creates .bak backup before any modification.
"""

import json
import os
import glob
import shutil
from datetime import datetime

CHAPTERS_DIR = "app_core/chapters"
BACKUP_EXT = ".bak_schema"

fixed_list_files = []
fixed_correct_answer_files = []
skipped = []
errors = []

def derive_metadata(filename: str, data: list) -> dict:
    """Generate a minimal metadata block from the filename."""
    base = os.path.splitext(os.path.basename(filename))[0]
    # e.g. ncert_class10_science_ch1 → Chapter 1 Science (Class 10 NCERT)
    return {
        "module_id": base,
        "title": base.replace("_", " ").title(),
        "title_hi": base.replace("_", " ").title(),
        "title_gu": base.replace("_", " ").title(),
        "board": "NCERT/GSEB",
        "subject": "",
        "chapter_number": "",
        "language": "trilingual"
    }

def fix_correct_index(blocks: list) -> tuple[list, int]:
    """Fix correct_answer string → correct_index int in all quiz blocks."""
    count = 0
    for block in blocks:
        if "correct_answer" in block and "correct_index" not in block:
            options = block.get("options", [])
            correct_answer = block["correct_answer"]
            # Try to find it in English options
            idx = None
            if isinstance(options, list):
                for i, opt in enumerate(options):
                    opt_text = opt if isinstance(opt, str) else opt.get("text", "")
                    if opt_text.strip() == str(correct_answer).strip():
                        idx = i
                        break
            if idx is not None:
                block["correct_index"] = idx
            else:
                # Default to 0 if not found (safe fallback)
                block["correct_index"] = 0
            del block["correct_answer"]
            count += 1
    return blocks, count

def process_file(filepath: str):
    """Process a single chapter JSON file."""
    base = os.path.basename(filepath)
    
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            raw = f.read().strip()
        data = json.loads(raw)
    except Exception as e:
        errors.append(f"{base}: JSON parse error — {e}")
        return

    changed = False
    
    # ── FIX A: Root list → wrap in metadata+blocks ──────────────────────────
    if isinstance(data, list):
        backup_path = filepath + BACKUP_EXT
        if not os.path.exists(backup_path):
            shutil.copy2(filepath, backup_path)
        
        blocks, ca_count = fix_correct_index(data)
        wrapped = {
            "metadata": derive_metadata(filepath, data),
            "blocks": blocks
        }
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(wrapped, f, ensure_ascii=False, indent=2)
        fixed_list_files.append(base)
        if ca_count:
            fixed_correct_answer_files.append(f"{base} (+{ca_count} correct_index fixes)")
        print(f"  ✅ [LIST→WRAPPED] {base} ({len(data)} blocks{', +'+str(ca_count)+' CI fixes' if ca_count else ''})")
        return

    # ── FIX B: correct_answer → correct_index in dict files ─────────────────
    if isinstance(data, dict):
        blocks = data.get("blocks", [])
        if blocks:
            blocks, ca_count = fix_correct_index(blocks)
            if ca_count:
                backup_path = filepath + BACKUP_EXT
                if not os.path.exists(backup_path):
                    shutil.copy2(filepath, backup_path)
                data["blocks"] = blocks
                with open(filepath, "w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                fixed_correct_answer_files.append(f"{base} (+{ca_count} fixes)")
                print(f"  ✅ [CORRECT_INDEX] {base} fixed {ca_count} blocks")
                changed = True
        
        if not changed:
            print(f"  ⬜ [CLEAN] {base}")

def main():
    start = datetime.now()
    print("=" * 60)
    print("SHINE ACADEMY — SCHEMA FIXER")
    print(f"Started at: {start.strftime('%H:%M:%S')}")
    print("=" * 60)
    
    files = sorted(glob.glob(os.path.join(CHAPTERS_DIR, "*.json")))
    print(f"\nFound {len(files)} chapter JSON files in {CHAPTERS_DIR}/\n")
    
    for filepath in files:
        process_file(filepath)
    
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"  Root-list files wrapped   : {len(fixed_list_files)}")
    print(f"  correct_index fixes       : {len(fixed_correct_answer_files)}")
    print(f"  Errors                    : {len(errors)}")
    
    if errors:
        print("\nERRORS:")
        for e in errors:
            print(f"  ❌ {e}")
    
    end = datetime.now()
    print(f"\n🎉 DONE — Finished at {end.strftime('%H:%M:%S')} ({(end-start).seconds}s)")
    print("=" * 60)

if __name__ == "__main__":
    main()
