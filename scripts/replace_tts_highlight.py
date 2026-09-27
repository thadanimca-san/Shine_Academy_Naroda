import os
import glob

def process_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    new_content = content.replace("TtsHighlightText", "TtsInteractiveText")
    new_content = new_content.replace("tts_highlight_text.dart", "tts_interactive_text.dart")

    if content != new_content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

for filepath in glob.glob('/home/ubuntu/Shine_Academy_Naroda/lib/**/*.dart', recursive=True):
    if not filepath.endswith('tts_highlight_text.dart') and not filepath.endswith('tts_interactive_text.dart'):
        process_file(filepath)
