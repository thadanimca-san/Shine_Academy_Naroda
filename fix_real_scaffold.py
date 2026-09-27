with open("lib/features/learning/learning_engine/learning_engine_screen.dart", "r") as f:
    lines = f.readlines()

# First, let's remove the wrong ListenableBuilder from _isComingSoon
# We know it starts around line 331
start_remove = -1
for i, line in enumerate(lines):
    if "if (_isComingSoon) {" in line:
        start_remove = i + 1
        break

if start_remove != -1 and "ListenableBuilder" in lines[start_remove]:
    lines.pop(start_remove) # return ListenableBuilder
    lines.pop(start_remove) # listenable:
    lines.pop(start_remove) # builder:
    # unindent the scaffold
    for i in range(start_remove, start_remove + 30):
        if "      }," in lines[i]:
            lines.pop(i)
            lines.pop(i)
            break
        lines[i] = lines[i][2:] # remove 2 spaces
        if "return Scaffold" in lines[i]:
            lines[i] = lines[i].replace("return Scaffold(", "return Scaffold(")

# Now wrap the CORRECT scaffold
start_wrap = -1
for i, line in enumerate(lines):
    if "final isDictionary = widget.moduleId.contains('DICT');" in line:
        start_wrap = i + 2
        break

if start_wrap != -1 and "return Scaffold" in lines[start_wrap]:
    lines.insert(start_wrap, "    return ListenableBuilder(\n      listenable: TrilingualService.instance,\n      builder: (context, _) {\n")
    end_wrap = -1
    open_brackets = 0
    for i in range(start_wrap+1, len(lines)):
        lines[i] = "  " + lines[i]
        open_brackets += lines[i].count("(") - lines[i].count(")")
        if open_brackets == 0:
            end_wrap = i
            break
    lines[start_wrap+1] = lines[start_wrap+1].replace("return Scaffold(", "return Scaffold(")
    if end_wrap != -1:
        lines.insert(end_wrap+1, "      },\n    );\n")

with open("lib/features/learning/learning_engine/learning_engine_screen.dart", "w") as f:
    f.writelines(lines)
print("Done fixing main scaffold")
