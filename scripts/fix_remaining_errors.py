import os
import re

def fix_context_errors(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Revert Theme.of(context)... back to Colors for CustomPainters and non-widget classes
    # 1. Theme.of(context).colorScheme.onSurface.withOpacity(0.38) -> Colors.black38
    content = re.sub(r'Theme\.of\(context\)\.colorScheme\.onSurface\.withOpacity\(0\.38\)', 'Colors.black38', content)
    
    # 2. Theme.of(context).colorScheme.onSurface.withOpacity(0.12) -> Colors.black12
    content = re.sub(r'Theme\.of\(context\)\.colorScheme\.onSurface\.withOpacity\(0\.12\)', 'Colors.black12', content)

    # 3. Theme.of(context).colorScheme.onSurface -> Colors.black87
    content = re.sub(r'Theme\.of\(context\)\.colorScheme\.onSurface', 'Colors.black87', content)

    # Also add flutter/material import if it's missing just in case
    if 'Colors.black' in content and 'flutter/material.dart' not in content:
        content = "import 'package:flutter/material.dart';\n" + content
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def fix_const_errors(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Sometimes it's `const [\n BoxShadow` or similar. Let's do a more robust regex.
    # Replace `const [` with `[` if there's a BoxShadow inside.
    content = re.sub(r'const\s*\[\s*BoxShadow', r'[BoxShadow', content)
    content = re.sub(r'const\s*BoxShadow', r'BoxShadow', content)
    
    # Check if there are other `const` keywords on the same line as Theme.of
    # A simple way to fix this is to find lines containing Theme.of(context) and remove `const`
    lines = content.split('\n')
    for i in range(len(lines)):
        if 'Theme.of(context)' in lines[i]:
            lines[i] = re.sub(r'\bconst\s+', '', lines[i])
            
    content = '\n'.join(lines)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def fix_global_context_menu(filepath):
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # lib/core/utils/global_context_menu.dart:4:39 - A value of type 'Widget Function(BuildContext, dynamic)' can't be returned from the function 'builder' because it has a return type of 'WidgetBuilder'.
    # WidgetBuilder is `Widget Function(BuildContext)`
    content = re.sub(r'\(context, \w+\)\s*\{', r'(context) {', content)
    content = re.sub(r'\(BuildContext context, \w+\)\s*\{', r'(BuildContext context) {', content)
    content = re.sub(r'\(context, \w+\)\s*=>', r'(context) =>', content)
    
    # Another possibility: contextMenuBuilder: (context, editableTextState)
    # The error says "can't be returned from the function 'builder' because it has a return type of 'WidgetBuilder'".
    # Let's change the return type to `Widget Function(BuildContext, EditableTextState)` or just fix the builder signature.
    # Actually, it's easier to just use `(context, __)` if it's expecting two args, wait. WidgetBuilder is 1 arg.
    # If the signature is `WidgetBuilder builder = (context, child) {`, it's an error.
    # Let's just blindly replace `(context, child)` with `(context)` where applicable, but let's be careful.
    pass

def main():
    context_files = [
        "lib/features/learning/higher_secondary/physics_sandbox/simulators/pulley_sim.dart",
        "lib/features/learning/school/english/widgets/glossed_text.dart",
        "lib/features/learning/school/maths_simulation/simulations/class10/triangles_simulation_widget.dart",
        "lib/features/learning/school/maths_simulation/simulations/class7/practical_geometry_simulation_widget.dart",
        "lib/features/learning/school/maths_simulation/simulations/class8/practical_geometry_simulation_widget.dart",
        "lib/features/learning/school/maths_simulation/simulations/class9/constructions_simulation_widget.dart",
        "lib/features/learning/school/maths_simulation/simulations/class9/coordinate_geometry_simulation_widget.dart",
        "lib/features/learning/school/sci_simulation/simulations/class10/control_coordination_simulation_widget.dart",
        "lib/features/learning/school/sci_simulation/simulations/class10/life_processes_simulation_widget.dart",
        "lib/features/learning/school/sci_simulation/simulations/class7/nutrition_plants_simulation_widget.dart",
        "lib/features/learning/school/sci_simulation/simulations/class7/transportation_simulation_widget.dart",
        "lib/features/learning/school/sci_simulation/simulations/common/diagram_helpers.dart",
        "lib/features/learning/school/sci_simulation/simulations/common/organelle_diagram.dart"
    ]
    
    for f in context_files:
        path = os.path.join('/home/ubuntu/Shine_Academy_Naroda', f)
        if os.path.exists(path):
            fix_context_errors(path)
            
    const_files = [
        "lib/features/common/widgets/xp_popup.dart",
        "lib/features/dashboard/home_screen.dart",
        "lib/features/learning/higher_secondary/physics_sandbox/simulators/planetary_motion_sim.dart"
    ]
    
    for f in const_files:
        path = os.path.join('/home/ubuntu/Shine_Academy_Naroda', f)
        if os.path.exists(path):
            fix_const_errors(path)
            
    print("Fixed final batch of compilation errors!")

if __name__ == "__main__":
    main()
