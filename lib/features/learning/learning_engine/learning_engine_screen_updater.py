import re

path = '/home/ubuntu/Shine_Academy_Naroda/lib/features/learning/learning_engine/learning_engine_screen.dart'
with open(path, 'r') as f:
    content = f.read()

# Add import for block registry
if "import '../../../../core/engine/block_registry.dart';" not in content:
    content = content.replace("import '../../../../core/engine/block_validator.dart';", 
                              "import '../../../../core/engine/block_validator.dart';\nimport '../../../../core/engine/block_registry.dart';")

# Replace _buildBlock method
build_block_pattern = r"  Widget _buildBlock\(Map<String, dynamic> block\) \{.*?return _buildDiagnosticError\(block, e\.toString\(\), stackTrace: stack\.toString\(\)\);\n    \}\n  \}"

new_build_block = """  Widget _buildBlock(Map<String, dynamic> block) {
    try {
      BlockValidator.validateBlock(block);
      final childWidget = BlockRegistry.instance.build(block);
      if (childWidget != null) {
        return childWidget;
      } else {
        return _buildDiagnosticError(block, 'Unknown block type: ${block['type']}');
      }
    } catch (e, stack) {
      return _buildDiagnosticError(block, e.toString(), stackTrace: stack.toString());
    }
  }"""

content = re.sub(build_block_pattern, new_build_block, content, flags=re.DOTALL)

# Let's also remove unnecessary widget imports since they are now handled by default_blocks.dart
# Actually, keeping them doesn't hurt as they might be used elsewhere, but flutter analyze will tell us if they are unused.

with open(path, 'w') as f:
    f.write(content)

