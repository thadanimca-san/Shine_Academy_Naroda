import os

def fix_const_errors():
    with open('analyze_errors.log', 'r') as f:
        lines = f.readlines()

    file_fixes = {}
    for line in lines:
        line = line.strip()
        if not line or '|' not in line:
            continue
            
        parts = line.split('|')
        if len(parts) >= 6:
            severity = parts[0]
            if severity != 'ERROR':
                continue
                
            error_code = parts[2]
            filepath = parts[3]
            line_str = parts[4]
            col_str = parts[5]
            
            # Catch const-related errors
            if 'CONST' in error_code or 'const' in line.lower():
                line_num = int(line_str) - 1 # 0-indexed
                if filepath not in file_fixes:
                    file_fixes[filepath] = set()
                file_fixes[filepath].add(line_num)
        
    total_fixes = 0
    for filepath, lines_to_fix in file_fixes.items():
        if not os.path.exists(filepath):
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content_lines = f.readlines()
            
        modified = False
        for line_num in lines_to_fix:
            if line_num < len(content_lines):
                # Check current and up to 15 previous lines
                for offset in range(0, -15, -1):
                    target_idx = line_num + offset
                    if target_idx >= 0 and 'const ' in content_lines[target_idx]:
                        # Only replace the last occurrence of 'const ' on that line
                        content_lines[target_idx] = ' '.join(content_lines[target_idx].rsplit('const ', 1))
                        modified = True
                        total_fixes += 1
                        break # Found it, move to next error

        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.writelines(content_lines)
                
    print(f"Removed const from {total_fixes} lines across {len(file_fixes)} files based on machine logs.")

if __name__ == "__main__":
    fix_const_errors()
