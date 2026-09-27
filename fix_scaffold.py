import re

with open("lib/features/learning/learning_engine/learning_engine_screen.dart", "r") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "return Scaffold(" in line and "appBar: BrandAppBar(" in lines[i+2]:
        start_idx = i
        break

# Find the matching closing bracket of the Scaffold
open_brackets = 0
end_idx = -1
for i in range(start_idx, len(lines)):
    open_brackets += lines[i].count("(") - lines[i].count(")")
    if open_brackets == 0:
        end_idx = i
        break

# Wrap
lines.insert(start_idx, "    return ListenableBuilder(\n      listenable: TrilingualService.instance,\n      builder: (context, _) {\n")
# Indent the scaffold
for i in range(start_idx+1, end_idx+2):
    lines[i] = "  " + lines[i]
lines.insert(end_idx+2, "      },\n    );\n")

# Need to change the original `return Scaffold(` to just `return Scaffold(` inside the builder.
# Actually the replacement above already did it! Wait, no:
lines[start_idx+1] = lines[start_idx+1].replace("return Scaffold(", "return Scaffold(")

with open("lib/features/learning/learning_engine/learning_engine_screen.dart", "w") as f:
    f.writelines(lines)
print("Done")
