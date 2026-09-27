import os
import re

base_dir = '/home/ubuntu/Shine_Academy_Naroda/lib/features/learning/school/english/data'
files = [f for f in os.listdir(base_dir) if f.startswith('practice_class') and f.endswith('.dart')]

imports = ["import '../models/practice_question.dart';"]
classes = {
    'Class 3': [], 'Class 4': [], 'Class 5': [], 'Class 6': [],
    'Class 7': [], 'Class 8': [], 'Class 9': [], 'Class 10': []
}

for file_name in sorted(files):
    if file_name == 'practice_topics.dart': continue
    imports.append(f"import '{file_name}';")
    
    with open(os.path.join(base_dir, file_name), 'r') as f:
        content = f.read()
        m = re.search(r'const\s+(\w+)\s*=\s*PracticeTopic', content)
        if m:
            var_name = m.group(1)
            grade_match = re.search(r"grade:\s*'([^']+)'", content)
            if grade_match:
                grade = grade_match.group(1)
                if grade in classes:
                    classes[grade].append(var_name)

out = "\n".join(imports) + "\n\n"
out += "const Map<String, List<PracticeTopic>> practiceTopicsByGrade = {\n"

for grade in sorted(classes.keys(), key=lambda x: int(x.split(' ')[1])):
    topics = classes[grade]
    out += f"  '{grade}': [\n"
    for t in topics:
        out += f"    {t},\n"
    out += "  ],\n"

out += "};\n"
out += "\nfinal allPracticeTopics = practiceTopicsByGrade.values.expand((topics) => topics).toList();\n"

with open(f'{base_dir}/practice_topics.dart', 'w') as f:
    f.write(out)
