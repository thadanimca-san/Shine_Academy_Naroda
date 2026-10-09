import re

path = 'lib/features/learning/school/english/services/speech_service.dart'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

voice_injection = """
      _log('Setting language to: "$chosen"');
      await _tts!.setLanguage(chosen);
      _resolvedLanguage = chosen;
      _log('Language set successfully: "$_resolvedLanguage"');

      // Attempt to force a male voice for this language
      try {
        final voices = await _tts!.getVoices;
        if (voices != null) {
          final List<Map<Object?, Object?>> voiceList = List<Map<Object?, Object?>>.from(voices);
          
          final localVoices = voiceList.where((v) {
            final locale = (v['locale']?.toString() ?? '').toLowerCase();
            return locale == chosen?.toLowerCase() || locale.replaceAll('_', '-') == chosen?.toLowerCase();
          }).toList();

          if (localVoices.isNotEmpty) {
            final maleVoices = localVoices.where((v) {
              final name = (v['name']?.toString() ?? '').toLowerCase();
              return name.contains('male') && !name.contains('female');
            }).toList();

            final selectedVoice = maleVoices.isNotEmpty ? maleVoices.first : localVoices.first;
            
            final voiceMap = {
              "name": selectedVoice['name']?.toString() ?? '',
              "locale": selectedVoice['locale']?.toString() ?? ''
            };
            
            await _tts!.setVoice(voiceMap);
            _log('Forced male voice: ${voiceMap['name']}');
          }
        }
      } catch (e) {
        _log('Failed to force male voice: $e');
      }
"""

old_str = """
      _log('Setting language to: "$chosen"');
      await _tts!.setLanguage(chosen);
      _resolvedLanguage = chosen;
      _log('Language set successfully: "$_resolvedLanguage"');
"""

content = content.replace(old_str.strip(), voice_injection.strip())

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated speech_service")
