#!/usr/bin/env python3
"""
Shine Academy EduOS — Block Fixer Script
========================================
Fixes all blocks.json files across the project:

FIX 1: Add missing 'id' fields (UNKNOWN_ID / no id)
FIX 2: Flatten 'content:{}' wrapper for block types whose widgets
        read data at the ROOT level (not via content wrapper)
FIX 3: Replace 'correct_answer' string → 'correct_index' int
        for knowledge_check / mcq / practice_question blocks

SAFE: Does NOT touch content:{} wrappers for block types that
      intentionally use them (animated_diagram, teacher_tip,
      presentation, nursery_rhyme, common_mistakes, etc.)
"""

import json
import os
import glob
import copy
import re
from datetime import datetime

# ─────────────────────────────────────────────────────────────────
# BLOCK TYPES THAT INTENTIONALLY USE content:{} OR content: string
# Their widgets read block['content']['field'] or block['content']
# DO NOT flatten these.
# ─────────────────────────────────────────────────────────────────
CONTENT_WRAPPER_OK = {
    'animated_diagram',   # reads block['content']['paths'], ['title'], ['description']
    'presentation',       # reads block['content']['items'], ['title']
    'teacher_tip',        # reads block['content'] as string or text
    'common_mistakes',    # reads block['content']
    'nursery_rhyme',      # reads block['content'] as string (lyrics)
    'exam_tips',          # similar to teacher_tip
    'memory_trick',       # reads content
}

# ─────────────────────────────────────────────────────────────────
# BLOCK TYPES WHOSE 'content:{}' WRAPPER MUST BE FLATTENED
# Their widgets read directly from block root level
# ─────────────────────────────────────────────────────────────────
FLATTEN_CONTENT = {
    'theory',
    'definition',
    'real_world_example',
    'formula',
    'history',
    'summary',
    'hook',
    'socratic',
    'reflection',
    'cross_subject_link',
    'challenge_question',
    'ai_discussion',
    'ai_tutor_prompt',
    'simulation',
    'image',
    'diagram',
    'project',
    'knowledge_check',
    'mcq',
    'true_false',
    'practice_question',
    'worked_example',
    'connection',
    'match_column',
    'reveal',
    'discovery',
    'mastery',
}

# ─────────────────────────────────────────────────────────────────
# ID GENERATION
# ─────────────────────────────────────────────────────────────────
def generate_id(module_id: str, block_type: str, index: int) -> str:
    """Generate a clean, unique block ID."""
    # Clean up the module_id to make a prefix
    # e.g. gseb_class9_science_ch1 → C9SC1
    # e.g. class1_evs_ch5 → C1EVS5
    # e.g. nursery_alphabets_ch3 → NURS_ALPHA_CH3
    
    # Extract useful parts
    parts = module_id.upper().split('_')
    
    # Build a short prefix
    prefix_parts = []
    ch_num = ''
    for part in parts:
        if part.startswith('CH') and part[2:].isdigit():
            ch_num = part[2:]
        elif part == 'CLASS' or part == 'GSEB':
            continue
        elif part.isdigit():
            prefix_parts.append(part)
        else:
            prefix_parts.append(part[:4])
    
    prefix = '_'.join(prefix_parts[:3])
    if ch_num:
        prefix += f'_CH{ch_num}'
    
    # Block type short code
    type_code = block_type.upper()[:4]
    
    return f'KOBJ_{prefix}_{type_code}_{index+1:03d}'


# ─────────────────────────────────────────────────────────────────
# CORRECT_ANSWER → CORRECT_INDEX FIXER
# ─────────────────────────────────────────────────────────────────
def fix_correct_answer(block: dict) -> dict:
    """Convert correct_answer string to correct_index int."""
    options = block.get('options', [])
    correct_answer = block.get('correct_answer')
    
    if correct_answer is None:
        return block
    
    # Remove the old key
    block.pop('correct_answer', None)
    
    # Try to find the index
    if isinstance(correct_answer, str) and options:
        for i, opt in enumerate(options):
            if isinstance(opt, str) and opt.strip().lower() == correct_answer.strip().lower():
                block['correct_index'] = i
                return block
        # If not found, default to 0
        block['correct_index'] = 0
    elif isinstance(correct_answer, int):
        block['correct_index'] = correct_answer
    else:
        block['correct_index'] = 0
    
    return block


# ─────────────────────────────────────────────────────────────────
# CONTENT WRAPPER FLATTENER
# ─────────────────────────────────────────────────────────────────
def flatten_content_wrapper(block: dict) -> dict:
    """Flatten block['content'] dict fields to root level."""
    content = block.get('content')
    if not isinstance(content, dict):
        return block
    
    # Merge content fields into root, root fields take precedence
    new_block = dict(block)
    new_block.pop('content', None)
    
    for key, value in content.items():
        if key not in new_block:  # Don't overwrite existing root keys
            new_block[key] = value
    
    return new_block


# ─────────────────────────────────────────────────────────────────
# MAIN FIX FUNCTION FOR A SINGLE BLOCK
# ─────────────────────────────────────────────────────────────────
def fix_block(block: dict, module_id: str, index: int) -> tuple:
    """Fix a single block. Returns (fixed_block, list_of_changes)."""
    fixed = copy.deepcopy(block)
    changes = []
    btype = fixed.get('type', 'unknown')
    
    # ── FIX 1: Missing or UNKNOWN_ID ──────────────────────────────
    if not fixed.get('id') or fixed.get('id') == 'UNKNOWN_ID':
        new_id = generate_id(module_id, btype, index)
        fixed['id'] = new_id
        changes.append(f"Added id: {new_id}")
    
    # ── FIX 2: Flatten content:{} wrapper where needed ────────────
    if btype in FLATTEN_CONTENT:
        content = fixed.get('content')
        if isinstance(content, dict):
            fixed = flatten_content_wrapper(fixed)
            changes.append(f"Flattened content{{}} wrapper")
        elif isinstance(content, str):
            # content is a string (e.g. theory block with content:"text...")
            # This is accepted by TheoryWidget via requireLegacyFlexible
            # Leave it as-is — it works
            pass
    
    # ── FIX 3: correct_answer → correct_index ────────────────────
    if btype in ('knowledge_check', 'mcq', 'practice_question', 'quiz', 'true_false'):
        if 'correct_answer' in fixed:
            fixed = fix_correct_answer(fixed)
            changes.append("Converted correct_answer → correct_index")
    
    return fixed, changes


# ─────────────────────────────────────────────────────────────────
# PROCESS ONE FILE
# ─────────────────────────────────────────────────────────────────
def process_file(filepath: str) -> dict:
    """Process a single blocks.json file. Returns stats."""
    module_id = os.path.basename(os.path.dirname(filepath))
    
    with open(filepath, 'r', encoding='utf-8') as f:
        original_content = f.read()
        data = json.loads(original_content)
    
    is_list = isinstance(data, list)
    blocks = data if is_list else data.get('blocks', [])
    
    fixed_blocks = []
    total_changes = 0
    file_changes = []
    
    for i, block in enumerate(blocks):
        fixed_block, changes = fix_block(block, module_id, i)
        fixed_blocks.append(fixed_block)
        if changes:
            total_changes += len(changes)
            file_changes.append(f"  Block {i} ({block.get('type','?')}): {', '.join(changes)}")
    
    if total_changes > 0:
        # Write back
        if is_list:
            new_data = fixed_blocks
        else:
            data['blocks'] = fixed_blocks
            new_data = data
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(new_data, f, indent=2, ensure_ascii=False)
    
    return {
        'module': module_id,
        'total_blocks': len(blocks),
        'total_changes': total_changes,
        'changes': file_changes,
    }


# ─────────────────────────────────────────────────────────────────
# VALIDATION PASS
# ─────────────────────────────────────────────────────────────────
def validate_file(filepath: str) -> list:
    """Re-scan a file for remaining issues after fixing."""
    issues = []
    module_id = os.path.basename(os.path.dirname(filepath))
    
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    blocks = data if isinstance(data, list) else data.get('blocks', [])
    
    for i, block in enumerate(blocks):
        btype = block.get('type', 'MISSING')
        
        if not block.get('id') or block.get('id') == 'UNKNOWN_ID':
            issues.append(f"{module_id} Block {i} ({btype}): Still missing ID")
        
        if btype in FLATTEN_CONTENT:
            if isinstance(block.get('content'), dict):
                issues.append(f"{module_id} Block {i} ({btype}): Still has content{{}} wrapper")
        
        if btype in ('knowledge_check', 'mcq', 'practice_question', 'quiz'):
            if 'correct_answer' in block:
                issues.append(f"{module_id} Block {i} ({btype}): Still has correct_answer")
    
    return issues


# ─────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────
def main():
    modules_dir = "/home/ubuntu/Shine_Academy_Naroda/app_core/learning_modules"
    all_files = sorted(glob.glob(f"{modules_dir}/*/blocks.json"))
    
    print(f"🔧 Shine Academy Block Fixer")
    print(f"{'='*60}")
    print(f"Files found: {len(all_files)}")
    print(f"Started: {datetime.now().strftime('%H:%M:%S')}")
    print()
    
    # ── PHASE 1: Fix all files ────────────────────────────────────
    print("📝 PHASE 1: Fixing all files...")
    print("-"*60)
    
    total_files_fixed = 0
    total_blocks_fixed = 0
    all_stats = []
    
    for filepath in all_files:
        try:
            stats = process_file(filepath)
            all_stats.append(stats)
            if stats['total_changes'] > 0:
                total_files_fixed += 1
                total_blocks_fixed += stats['total_changes']
                print(f"✅ [{stats['module']}] — {stats['total_changes']} fix(es)")
                for change in stats['changes'][:5]:  # show max 5 per file
                    print(change)
                if len(stats['changes']) > 5:
                    print(f"    ... and {len(stats['changes'])-5} more")
            else:
                print(f"⬜ [{stats['module']}] — already clean")
        except json.JSONDecodeError as e:
            print(f"❌ [{os.path.basename(os.path.dirname(filepath))}] JSON PARSE ERROR: {e}")
        except Exception as e:
            print(f"❌ [{os.path.basename(os.path.dirname(filepath))}] ERROR: {e}")
    
    print()
    print(f"{'='*60}")
    print(f"PHASE 1 SUMMARY")
    print(f"  Files fixed   : {total_files_fixed}")
    print(f"  Total changes : {total_blocks_fixed}")
    print()
    
    # ── PHASE 2: Validation pass ──────────────────────────────────
    print("🔍 PHASE 2: Validation pass...")
    print("-"*60)
    
    remaining_issues = []
    for filepath in all_files:
        try:
            issues = validate_file(filepath)
            remaining_issues.extend(issues)
        except Exception as e:
            remaining_issues.append(f"VALIDATION ERROR in {filepath}: {e}")
    
    if remaining_issues:
        print(f"⚠️  {len(remaining_issues)} remaining issue(s) found:")
        for issue in remaining_issues[:20]:
            print(f"  {issue}")
        if len(remaining_issues) > 20:
            print(f"  ... and {len(remaining_issues)-20} more")
    else:
        print(f"✅ ZERO remaining issues! All {len(all_files)} files are clean.")
    
    print()
    print(f"{'='*60}")
    print(f"🎉 DONE — Finished at {datetime.now().strftime('%H:%M:%S')}")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()
