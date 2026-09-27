with open('/home/ubuntu/Shine_Academy_Naroda/scripts/mass_translate.py', 'r') as f:
    lines = f.read()

lines = lines.replace(
    "if 'blocks' in data:",
    "if isinstance(data, list):\n            blocks = data\n        elif 'blocks' in data:"
)

with open('/home/ubuntu/Shine_Academy_Naroda/scripts/mass_translate.py', 'w') as f:
    f.write(lines)
