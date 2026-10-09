import re

def update_voice_logic(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    old_logic = """
            final maleVoices = localVoices.where((v) {
              final name = (v['name']?.toString() ?? '').toLowerCase();
              return name.contains('male') && !name.contains('female');
            }).toList();
"""

    old_logic_2 = """
          // Prefer male voices as requested by user
          final maleVoices = offlineIndianVoices.where((v) {
            final name = (v['name']?.toString() ?? '').toLowerCase();
            return name.contains('male') && !name.contains('female');
          }).toList();
"""

    new_logic = """
          // Google TTS uses 'end' and 'ene' for male en-IN voices
          final maleVoices = {list}.where((v) {
            final name = (v['name']?.toString() ?? '').toLowerCase();
            return name.contains('male') || name.contains('end-local') || name.contains('ene-local') || name.contains('end-network') || name.contains('ene-network');
          }).toList();
"""
    
    if 'tts_service.dart' in path:
        content = content.replace(old_logic_2, new_logic.replace('{list}', 'offlineIndianVoices'))
    else:
        content = content.replace(old_logic, new_logic.replace('{list}', 'localVoices'))

    # If the list is empty, we must lower the pitch of the female voice so it sounds male!
    # Where does it set the pitch?
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)


update_voice_logic('lib/core/services/tts_service.dart')
update_voice_logic('lib/features/learning/school/english/services/speech_service.dart')

print("Fixed male voice logic")
