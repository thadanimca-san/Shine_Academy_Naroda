import os
import json
import re

DART_REGISTRY_PATH = 'lib/core/engine/default_blocks.dart'
CONTENT_DIR = 'app_core'

def get_registered_types():
    """Extracts all registered block types from the Dart BlockRegistry file."""
    if not os.path.exists(DART_REGISTRY_PATH):
        print(f"Warning: Could not find {DART_REGISTRY_PATH}. Using a basic default list.")
        return {'theory', 'mcq', 'socratic', 'heading'}

    with open(DART_REGISTRY_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    types = set()
    
    # Find exact registry.register(BlockDefinition(type: '...'))
    matches1 = re.findall(r"type:\s*'([^']+)'", content)
    types.update(matches1)
    
    # Find all strings in single quotes that look like block type identifiers (e.g. in lists like theoryLikeTypes = ['theory', ...])
    # Ignore strings that have spaces or uppercase (block types are snake_case)
    matches2 = re.findall(r"'([a-z0-9_]+)'", content)
    for m in matches2:
        types.add(m)
        
    # Some common ignored words that might be caught
    types.discard('id')
    types.discard('title')
    types.discard('body')
    types.discard('svg_path')
    types.discard('shape')
    types.discard('letter')
    types.discard('character')
    types.discard('target_number')
    types.discard('parts')
    types.discard('target_chapter_id')
    
    return types

def fix_json_file(filepath, valid_types):
    """Scans a JSON file for unregistered block types and converts them to standard 'theory' blocks."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"⚠️  Skipping {filepath} (Invalid JSON format: {e})")
        return False

    changed = False
    
    # Extract blocks based on Shine Academy JSON structure
    blocks_to_check = []
    if isinstance(data, dict):
        if 'blocks' in data:
            blocks_to_check = data['blocks']
        elif 'modules' in data: # Master curriculum format
            for module in data.get('modules', []):
                for chapter in module.get('chapters', []):
                    for section in chapter.get('sections', []):
                        for block in section.get('blocks', []):
                            blocks_to_check.append(block)
    elif isinstance(data, list):
        blocks_to_check = data

    for block in blocks_to_check:
        if not isinstance(block, dict):
            continue
            
        btype = block.get('type')
        if not btype:
            continue
            
        if btype not in valid_types:
            print(f"🔧 Fixing block id '{block.get('id', 'UNKNOWN')}' in {os.path.basename(filepath)}")
            print(f"   - Invalid type: '{btype}' -> Changed to 'theory'")
            
            block['type'] = 'theory'
            
            # Serialize any custom arrays/objects into the 'body' string so content is not lost on screen
            extra_body = ""
            keys_to_delete = []
            
            for key, val in block.items():
                # Skip standard fields that TheoryWidget already understands
                if key in ['id', 'type', 'title', 'title_hi', 'title_gu', 'body', 'body_hi', 'body_gu', 'image', 'audio']:
                    continue
                
                if isinstance(val, list):
                    extra_body += f"\n\n--- {key.upper()} ---\n"
                    for item in val:
                        if isinstance(item, dict):
                            for k, v in item.items():
                                if isinstance(v, str):
                                    extra_body += f"• {k}: {v}\n"
                            extra_body += "\n"
                        elif isinstance(item, str):
                            extra_body += f"• {item}\n"
                    keys_to_delete.append(key)
                    
                elif isinstance(val, dict):
                    extra_body += f"\n\n--- {key.upper()} ---\n"
                    for k, v in val.items():
                        if isinstance(v, str):
                            extra_body += f"• {k}: {v}\n"
                    keys_to_delete.append(key)
            
            if extra_body:
                extra_body = extra_body.strip()
                block['body'] = block.get('body', '') + "\n\n" + extra_body
                if 'body_hi' in block:
                    block['body_hi'] = block.get('body_hi', '') + "\n\n(Note: Custom fields converted)\n" + extra_body
                if 'body_gu' in block:
                    block['body_gu'] = block.get('body_gu', '') + "\n\n(Note: Custom fields converted)\n" + extra_body
                
            for k in keys_to_delete:
                del block[k]
                
            changed = True

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    return False

def main():
    print("============================================================")
    print("🚀 AUTO-FIX: BLOCK RENDER ERRORS")
    print("============================================================")
    
    valid_types = get_registered_types()
    print(f"✅ Found {len(valid_types)} valid block types in Flutter engine.")
    print("Scanning content database for invalid blocks...\n")
    
    files_fixed = 0
    for root, dirs, files in os.walk(CONTENT_DIR):
        for file in files:
            if file.endswith('.json'):
                filepath = os.path.join(root, file)
                if fix_json_file(filepath, valid_types):
                    files_fixed += 1

    print("\n============================================================")
    if files_fixed > 0:
        print(f"🎉 SUCCESS: Fixed {files_fixed} file(s) with Block Render Errors.")
        print("💡 REMINDER: You MUST completely stop the app ('q') and run 'flutter run' again to see changes!")
    else:
        print("✅ ALL CLEAR: No Block Render Errors found in JSON files.")
    print("============================================================")

if __name__ == '__main__':
    main()
