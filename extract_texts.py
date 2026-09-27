import os, glob, re, json

files = glob.glob('lib/features/learning/school/english/data/chapter_class3*.dart')
out = {}
for f in files:
    with open(f, 'r') as file:
        content = file.read()
    match = re.search(r"chapterText:\s*'''(.*?)'''|chapterText:\s*'((?:\\'|[^'])*)'", content, re.DOTALL)
    if match:
        text = match.group(1) if match.group(1) else match.group(2)
        out[os.path.basename(f)] = text.replace("\\'", "'")
print(json.dumps(out, indent=2))
