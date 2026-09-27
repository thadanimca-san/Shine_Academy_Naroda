with open('lib/features/assessment/exam_engine_screen.dart', 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "void _startTimer()" in line:
        # Check lines before this to remove an extra '}'
        # the lines before are likely:
        # }
        # }
        # 
        # void _startTimer()
        for j in range(i-1, -1, -1):
            if lines[j].strip() == '}':
                # Remove this brace!
                print(f"Found brace to remove at line {j+1}")
                del lines[j]
                break
        break

with open('lib/features/assessment/exam_engine_screen.dart', 'w') as f:
    f.writelines(lines)
