import re

with open('lib/foundation/navigation/app_router.dart', 'r', encoding='utf-8') as f:
    code = f.read()

# Add import
import_stmt = "import '../../features/learning/tools/mt_trainer_screen.dart';\n"
if "mt_trainer_screen.dart" not in code:
    code = code.replace("import '../../features/activation/activation_screen.dart';", "import '../../features/activation/activation_screen.dart';\n" + import_stmt)

# Add route
route_stmt = """
        GoRoute(
          path: '/tools/mt_trainer',
          builder: (context, state) => const MultiplicationTableView(),
        ),"""

if "/tools/mt_trainer" not in code:
    code = code.replace("path: '/home',", "path: '/home'," + route_stmt.replace("path: '/home',", ""))

with open('lib/foundation/navigation/app_router.dart', 'w', encoding='utf-8') as f:
    f.write(code)

print("Done")
