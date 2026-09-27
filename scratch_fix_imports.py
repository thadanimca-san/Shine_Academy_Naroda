with open("lib/features/learning/learning_engine/learning_engine_screen.dart", "r") as f:
    content = f.read()

import_str = "import '../../../../core/engine/curriculum_database.dart';\n"
if import_str not in content:
    content = import_str + content

with open("lib/features/learning/learning_engine/learning_engine_screen.dart", "w") as f:
    f.write(content)
