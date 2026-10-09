import re

path = 'lib/core/services/tts_service.dart'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Change all setPitch(0.9) / 0.95 / 1.1 to setPitch(1.0)
content = re.sub(r'setPitch\(0\.9\)', 'setPitch(1.0)', content)
content = re.sub(r'setPitch\(0\.95\)', 'setPitch(1.0)', content)
content = re.sub(r'setPitch\(1\.1\)', 'setPitch(1.0)', content)
content = re.sub(r'\(pitch: 0\.9\)', '(pitch: 1.0)', content)
content = re.sub(r'\(pitch: 0\.95\)', '(pitch: 1.0)', content)
content = re.sub(r'\(pitch: 1\.1\)', '(pitch: 1.0)', content)
content = content.replace('// 🎶 Softer pitch for Hindi — warmer, sweeter sound', '// Natural male pitch for Hindi')
content = content.replace('// Slightly softer pitch for Gujarati', '// Natural male pitch for Gujarati')
content = content.replace('// Slightly higher pitch for English for a sweeter, friendly sound', '// Natural male pitch for English')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed pitch")
