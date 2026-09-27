import glob
import re

files = glob.glob("lib/features/learning/school/english/data/class*.dart")
for f in files:
    with open(f, 'r') as file:
        content = file.read()
    
    # We need to find lines like: 'DICT_ENG_UNCLE_(FATHER'S_BROTHER)',
    # and replace them with: "DICT_ENG_UNCLE_(FATHER'S_BROTHER)",
    # Let's find wordIds list and fix the strings.
    def replacer(match):
        inner = match.group(1)
        # remove anything after the 's if it's broken or just use double quotes if it contains a single quote.
        # But wait, the python script generated: 'DICT_ENG_UNCLE_(FATHER'S_BROTHER)'
        # so the single quote in FATHER'S terminates the string.
        # So it looks like: 'DICT_ENG_UNCLE_(FATHER'S_BROTHER)', in dart
        # which is a syntax error. We can replace:
        # 'DICT_ENG_(.*?)'S_(.*?)', with 'DICT_ENG_\1S_\2',
        return match.group(0)

    # Let's just fix it dumbly by reading line by line
    lines = content.split('\n')
    new_lines = []
    modified = False
    for line in lines:
        if "DICT_ENG_" in line:
            # check if there's a problem
            # The line looks like:     'DICT_ENG_UNCLE_(FATHER'S_BROTHER)',
            if line.count("'") > 2:
                # Replace 'S_ with S_ to remove the apostrophe
                new_line = line.replace("'S_", "S_")
                if new_line.count("'") > 2:
                    new_line = new_line.replace("S')", "S)") # e.g. 'DICT_ENG_BOY'S'
                new_lines.append(new_line)
                modified = True
                print(f"Fixed line in {f}: {new_line.strip()}")
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)

    if modified:
        with open(f, 'w') as file:
            file.write("\n".join(new_lines))
