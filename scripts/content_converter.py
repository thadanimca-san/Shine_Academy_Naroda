import os
import re
import json
import shutil

INTAKE_DIR = "../content_intake/markdown"
PROCESSED_DIR = "../content_intake/processed"
OUTPUT_DIR = "../app_core/knowledge_graph/dictionary"

def parse_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    data = {
        "id": "",
        "term": {},
        "subject": {},
        "chapter": {},
        "class": {"grades": []},
        "definition": {},
        "real_life_examples": [],
        "importance": {},
        "related_terms": [],
        "teacher_notes": {},
        "practice": {"easy": [], "medium": [], "difficult": []},
        "search_keywords": [],
        "voice": {},
        "animation": {},
        "diagram": {},
        "status": {"reviewed": True, "version": "1.0"}
    }

    # Extract Metadata
    metadata_match = re.search(r'# Metadata\n(.*?)(?=\n# |\Z)', content, re.DOTALL)
    if metadata_match:
        meta_lines = metadata_match.group(1).strip().split('\n')
        for line in meta_lines:
            if ':' in line:
                key, val = line.split(':', 1)
                key = key.strip().lower()
                val = val.strip()
                if key == 'id': data['id'] = val
                elif key == 'subject code': data['subject']['code'] = val
                elif key == 'subject name': data['subject']['name'] = val
                elif key == 'chapter code': data['chapter']['code'] = val
                elif key == 'chapter title': data['chapter']['title'] = val
                elif key == 'difficulty': data['difficulty'] = int(val) if val.isdigit() else val
                elif key == 'estimated time': data['estimated_time'] = int(val) if val.isdigit() else val
                elif key == 'version': data['status']['version'] = val

    # Extract Term
    term_match = re.search(r'# Term\n(.*?)(?=\n# |\Z)', content, re.DOTALL)
    if term_match:
        for line in term_match.group(1).strip().split('\n'):
            if ':' in line:
                lang, val = line.split(':', 1)
                data['term'][lang.strip().lower()] = val.strip()

    # Extract Class
    class_match = re.search(r'# Class\n(.*?)(?=\n# |\Z)', content, re.DOTALL)
    if class_match:
        lines = class_match.group(1).strip().split('\n')
        for line in lines:
            if line.startswith('Board:'):
                data['class']['board'] = line.split(':', 1)[1].strip()
            elif line.startswith('- '):
                data['class']['grades'].append(line[2:].strip())

    # Extract Definitions
    def_match = re.search(r'# Definition\n(.*?)(?=\n# |\Z)', content, re.DOTALL)
    if def_match:
        sections = re.split(r'\n## ', def_match.group(1).strip())
        for sec in sections:
            if not sec.strip(): continue
            parts = sec.split('\n', 1)
            if len(parts) == 2:
                level = parts[0].strip().lower().replace('## ', '')
                text = parts[1].strip()
                data['definition'][level] = text

    # Extract Lists (Real Life Examples, Related Terms, Search Keywords)
    def extract_list(header, key):
        match = re.search(fr'# {header}\n(.*?)(?=\n# |\Z)', content, re.DOTALL)
        if match:
            lines = match.group(1).strip().split('\n')
            data[key] = [line[2:].strip() for line in lines if line.startswith('- ')]

    extract_list("Real Life Examples", "real_life_examples")
    extract_list("Related Terms", "related_terms")
    extract_list("Search Keywords", "search_keywords")

    # Extract Importance
    imp_match = re.search(r'# Importance\n(.*?)(?=\n# |\Z)', content, re.DOTALL)
    if imp_match:
        sections = re.split(r'\n## ', imp_match.group(1).strip())
        for sec in sections:
            if not sec.strip(): continue
            parts = sec.split('\n', 1)
            if len(parts) == 2:
                domain = parts[0].strip().lower().replace('## ', '')
                lines = parts[1].strip().split('\n')
                data['importance'][domain] = [line[2:].strip() for line in lines if line.startswith('- ')]

    # Extract Teacher Notes
    tn_match = re.search(r'# Teacher Notes\n(.*?)(?=\n# |\Z)', content, re.DOTALL)
    if tn_match:
        sections = re.split(r'\n## ', tn_match.group(1).strip())
        for sec in sections:
            if not sec.strip(): continue
            parts = sec.split('\n', 1)
            if len(parts) == 2:
                note_type = parts[0].strip().lower().replace('## ', '')
                text = parts[1].strip()
                data['teacher_notes'][note_type] = text

    # Extract Practice
    prac_match = re.search(r'# Practice\n(.*?)(?=\n# |\Z)', content, re.DOTALL)
    if prac_match:
        sections = re.split(r'\n## ', prac_match.group(1).strip())
        for sec in sections:
            if not sec.strip(): continue
            parts = sec.split('\n', 1)
            if len(parts) == 2:
                level = parts[0].strip().lower().replace('## ', '')
                lines = parts[1].strip().split('\n')
                data['practice'][level] = [line[2:].strip() for line in lines if line.startswith('- ')]

    # Extract Media Required
    media_match = re.search(r'# Media Required\n(.*?)(?=\n# |\Z)', content, re.DOTALL)
    if media_match:
        lines = media_match.group(1).strip().split('\n')
        for line in lines:
            if ':' in line:
                key, val = line.split(':', 1)
                key = key.strip().lower()
                val = val.strip().lower() == 'true'
                if key == 'pronunciation': data['voice']['pronunciation'] = val
                elif key == 'animation': data['animation']['required'] = val
                elif key == 'diagram': data['diagram']['required'] = val

    return data

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    intake_dir = os.path.join(script_dir, INTAKE_DIR)
    processed_dir = os.path.join(script_dir, PROCESSED_DIR)
    out_dir = os.path.join(script_dir, OUTPUT_DIR)
    
    os.makedirs(intake_dir, exist_ok=True)
    os.makedirs(processed_dir, exist_ok=True)
    os.makedirs(out_dir, exist_ok=True)

    count = 0
    for filename in os.listdir(intake_dir):
        if filename.endswith(".md"):
            file_path = os.path.join(intake_dir, filename)
            print(f"Processing {filename}...")
            
            try:
                # Parse
                json_data = parse_markdown(file_path)
                
                # Output filename
                out_name = json_data.get("id", "UNKNOWN_ID") + ".json"
                out_path = os.path.join(out_dir, out_name)
                
                # Write JSON
                with open(out_path, 'w', encoding='utf-8') as jf:
                    json.dump(json_data, jf, indent=2, ensure_ascii=False)
                
                # Move to processed
                shutil.move(file_path, os.path.join(processed_dir, filename))
                print(f"Successfully converted and moved {filename} to {out_name}")
                count += 1
                
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    print(f"Processed {count} files.")

if __name__ == "__main__":
    main()
