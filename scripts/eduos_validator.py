#!/usr/bin/env python3
import os
import json
import glob
from collections import defaultdict
from datetime import datetime

APP_CORE = "app_core"
ASSETS = "assets"
REPORT_FILE = "app_core/validation_report.json"

VALID_BLOCK_TYPES = [
    "theory", "example", "activity", "quiz", "flashcard", "teacher_tip",
    "common_mistakes", "dictionary_link", "nursery_rhyme", "trace_alphabet",
    "counting_game", "color_canvas", "nursery_art", "mcq"
]

def run_validation():
    print("=============================================")
    print(" 🩺 EduOS JSON Validation Engine 🩺")
    print("=============================================\n")

    report = {
        "timestamp": datetime.utcnow().isoformat(),
        "summary": {
            "total_files_scanned": 0,
            "pass_count": 0,
            "warning_count": 0,
            "error_count": 0,
        },
        "errors": [],
        "warnings": [],
        "status": "PASS"
    }

    global_ids = defaultdict(list)
    
    json_files = glob.glob(f"{APP_CORE}/**/*.json", recursive=True)
    report["summary"]["total_files_scanned"] = len(json_files)

    for file_path in json_files:
        if file_path == REPORT_FILE:
            continue
            
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                if not content:
                    data = {} # Handle completely empty files gracefully
                else:
                    data = json.loads(content)
        except json.JSONDecodeError as e:
            report["errors"].append({
                "file": file_path,
                "type": "INVALID_JSON",
                "message": f"Syntax error: {str(e)}"
            })
            continue

        file_name = os.path.basename(file_path)

        # Only validate block structure if it is a blocks.json or question_bank.json
        if isinstance(data, list) and (file_name == 'blocks.json' or file_name == 'question_bank.json'):
            for i, block in enumerate(data):
                if not isinstance(block, dict):
                    report["errors"].append({"file": file_path, "type": "INVALID_BLOCK_FORMAT", "message": f"Block at index {i} is not a dictionary."})
                    continue
                
                # Check for ID uniqueness only within block files to avoid curriculum overlaps
                if 'id' in block:
                    global_ids[block['id']].append(file_path)

                # Check for block type
                b_type = block.get('type')
                if not b_type:
                    report["errors"].append({"file": file_path, "type": "MISSING_BLOCK_TYPE", "message": f"Block at index {i} is missing 'type'."})
                elif b_type not in VALID_BLOCK_TYPES:
                    report["warnings"].append({"file": file_path, "type": "UNKNOWN_BLOCK_TYPE", "message": f"Block at index {i} has unknown type: '{b_type}'"})

                # Check asset paths if they exist
                for k, v in block.items():
                    if isinstance(v, str) and (v.startswith('assets/images/') or v.startswith('assets/audio/')):
                        if not os.path.exists(v):
                            report["errors"].append({"file": file_path, "type": "BROKEN_ASSET_LINK", "message": f"Asset not found: {v}"})

        # Dictionary link validation
        if isinstance(data, dict):
            # We don't check global ID for everything anymore to avoid metadata vs curriculum overlaps
            if 'related_terms' in data and isinstance(data['related_terms'], list):
                for term in data['related_terms']:
                    if not os.path.exists(f"{APP_CORE}/knowledge_graph/dictionary/{term}.json"):
                        report["errors"].append({"file": file_path, "type": "BROKEN_DICT_LINK", "message": f"Dictionary term '{term}' referenced but does not exist."})

    # 2. Check for Duplicate IDs (only block IDs)
    for block_id, files in global_ids.items():
        if len(files) > 1:
            report["errors"].append({
                "file": "Multiple",
                "type": "DUPLICATE_ID",
                "message": f"ID '{block_id}' is duplicated across files: {', '.join(files)}"
            })

    # 3. Finalize Report
    report["summary"]["error_count"] = len(report["errors"])
    report["summary"]["warning_count"] = len(report["warnings"])
    report["summary"]["pass_count"] = report["summary"]["total_files_scanned"] - len(set([e['file'] for e in report["errors"]]))

    if report["summary"]["error_count"] > 0:
        report["status"] = "ERROR"
    elif report["summary"]["warning_count"] > 0:
        report["status"] = "WARNING"
    else:
        report["status"] = "PASS"

    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=4)

    # Print summary
    print(f"Status: {report['status']}")
    print(f"Files Scanned: {report['summary']['total_files_scanned']}")
    print(f"Errors Found: {report['summary']['error_count']}")
    print(f"Warnings Found: {report['summary']['warning_count']}")

if __name__ == "__main__":
    run_validation()
