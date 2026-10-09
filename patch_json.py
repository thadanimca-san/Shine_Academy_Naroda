import os

file_path = "app_core/chapters/ncert_class10_science_ch1.json"
with open(file_path, 'rb') as f:
    content = f.read()

# Let's decode with errors='ignore' just to find the substring, or we can work with bytes
content_str = content.decode('utf-8', errors='replace')

lines = content_str.split('\n')
for i, line in enumerate(lines):
    if '"id": "KOBJ_NCERT_C10_SCI_CH1_021"' in line:
        target_idx = i
        break

# The body_gu is at target_idx + 7 (lines 333 is id, 340 is body_gu)
# Let's just find the exact line 340 and replace it.
# Wait, it's safer to just read the file line by line in binary, and modify line 339 (0-indexed).

with open(file_path, 'rb') as f:
    lines_bin = f.readlines()

line_to_modify = lines_bin[339]

# Append the new fields to this line
new_fields = b',\n    "image_url": "assets/images/science/exothermic_endothermic_reactions.png",\n    "caption": "Comparison of Exothermic and Endothermic Reactions",\n    "caption_hi": "\xe0\xa4\x8a\xe0\xa4\xb7\xe0\xa5\x8d\xe0\xa4\xae\xe0\xa4\xbe\xe0\xa4\x95\xe0\xa5\x8d\xe0\xa4\xb7\xe0\xa5\x87\xe0\xa4\xaa\xe0\xa5\x80 \xe0\xa4\x94\xe0\xa4\xb0 \xe0\xa4\x8a\xe0\xa4\xb7\xe0\xa5\x8d\xe0\xa4\xae\xe0\xa4\xbe\xe0\xa4\xb6\xe0\xa5\x8b\xe0\xa4\xb7\xe0\xa5\x80 \xe0\xa4\x85\xe0\xa4\xad\xe0\xa4\xbf\xe0\xa4\x95\xe0\xa5\x8d\xe0\xa4\xb0\xe0\xa4\xbf\xe0\xa4\xaf\xe0\xa4\xbe\xe0\xa4\x93\xe0\xa4\x82 \xe0\xa4\x95\xe0\xa5\x80 \xe0\xa4\xa4\xe0\xa5\x81\xe0\xa4\xb2\xe0\xa4\xa8\xe0\xa4\xbe",\n    "caption_gu": "\xe0\xaa\x89\xe0\xaa\xb7\xe0\xaa\xae\xe0\xaa\xbe\xe0\xaa\x95\xe0\xaa\xbf\xe0\xaa\xb7\xe0\xaa\xbe\xe0\xaa\xaa\xe0\xaa\x95 \xe0\xaa\x85\xe0\xaa\xa8\xe0\xaa\x87 \xe0\xaa\x89\xe0\xaa\xb7\xe0\xaa\xae\xe0\xaa\xbe\xe0\xaa\xb6\xe0\xaa\xbe\xe0\xaa\xb7\xe0\xaa\x95 \xe0\xaa\xaa\xe0\xaa\xbf\xe0\xaa\xb0\xe0\xaa\x95\xe0\xaa\xbf\xe0\xaa\xb0\xe0\xaa\xbf\xe0\xaa\xaf\xe0\xaa\xbe\xe0\xaa\x93\xe0\xaa\xa8\xe0\xaa\xbf \xe0\xaa\xb8\xe0\xaa\xb0\xe0\xaa\x96\xe0\xaa\xbe\xe0\xaa\xae\xe0\xaa\xa3\xe0\xaa\xbf"\n'

# wait, line_to_modify ends with \n or \r\n. We should strip it, add our string, and then put it back
line_to_modify_clean = line_to_modify.rstrip(b'\r\n')
# However, caption_gu has unicode escapes, wait, Python string literals handles this:
caption_hi_str = "ऊष्माक्षेपी और ऊष्माशोषी अभिक्रियाओं की तुलना"
caption_gu_str = "ઉષ્માક્ષેપક અને ઉષ્માશોષક પ્રક્રિયાઓની સરખામણી"

new_fields_str = f',\n    "image_url": "assets/images/science/exothermic_endothermic_reactions.png",\n    "caption": "Comparison of Exothermic and Endothermic Reactions",\n    "caption_hi": "{caption_hi_str}",\n    "caption_gu": "{caption_gu_str}"\n'

lines_bin[339] = line_to_modify_clean + new_fields_str.encode('utf-8')

with open(file_path, 'wb') as f:
    f.writelines(lines_bin)

print("Modified successfully")
