import os
import re

def refactor_colors_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # We want to replace hardcoded Colors.black87, Colors.black54, Colors.black
    # with Theme.of(context).colorScheme.onSurface
    # Note: We must be careful that 'context' is actually available in the build method.
    # Usually, if it's inside a build method, context is available.
    
    # Let's target the most common ones that break dark mode
    replacements = [
        (r'color:\s*Colors\.black87', 'color: Theme.of(context).colorScheme.onSurface'),
        (r'color:\s*Colors\.black54', 'color: Theme.of(context).colorScheme.onSurfaceVariant'),
        (r'color:\s*Colors\.black', 'color: Theme.of(context).colorScheme.onSurface'),
        (r'color:\s*Colors\.black12', 'color: Theme.of(context).colorScheme.surfaceContainerHighest'),
        (r'color:\s*Colors\.black26', 'color: Theme.of(context).colorScheme.outlineVariant'),
    ]
    
    original_content = content
    for pattern, replacement in replacements:
        content = re.sub(pattern, replacement, content)
        
    if content != original_content:
        # Check if flutter/material.dart is imported (usually is)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    print("Starting The Great Theming Refactor...")
    lib_dir = '/home/ubuntu/Shine_Academy_Naroda/lib'
    
    modified_count = 0
    for root, dirs, files in os.walk(lib_dir):
        for file in files:
            if file.endswith('.dart'):
                filepath = os.path.join(root, file)
                if refactor_colors_in_file(filepath):
                    modified_count += 1
                    
    print(f"Refactored hardcoded colors in {modified_count} Dart files!")

if __name__ == "__main__":
    main()
