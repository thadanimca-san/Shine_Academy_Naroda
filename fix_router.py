import re

path = '/home/ubuntu/Shine_Academy_Naroda/lib/foundation/navigation/app_router.dart'
with open(path, 'r') as f:
    content = f.read()

# Comment out missing imports
content = re.sub(r"(import '../../features/learning/school/social_science_simulation/social_science_main.dart' as sst_sim;)", r"// \1", content)
content = re.sub(r"(import '../../features/learning/school/sanskrit_simulation/sanskrit_main.dart' as sanskrit_sim;)", r"// \1", content)
content = re.sub(r"(import '../../features/learning/school/gujarati_simulation/gujarati_main.dart' as gujarati_sim;)", r"// \1", content)
content = re.sub(r"(import '../../features/learning/school/computer_simulation/computer_main.dart' as computer_sim;)", r"// \1", content)
content = re.sub(r"(import '../../features/learning/school/hindi_simulation/hindi_main.dart' as hindi_sim;)", r"// \1", content)

# Remove routes for these missing modules
content = re.sub(r"GoRoute\(path:\s*'sst_sim',\s*builder:\s*\(context,\s*state\)\s*=>\s*ExitOverlay\(child:\s*sst_sim.AppGate\(\)\)\),", r"", content)
content = re.sub(r"GoRoute\(path:\s*'sanskrit_sim',\s*builder:\s*\(context,\s*state\)\s*=>\s*ExitOverlay\(child:\s*sanskrit_sim.AppGate\(\)\)\),", r"", content)
content = re.sub(r"GoRoute\(path:\s*'gujarati_sim',\s*builder:\s*\(context,\s*state\)\s*=>\s*ExitOverlay\(child:\s*gujarati_sim.AppGate\(\)\)\),", r"", content)
content = re.sub(r"GoRoute\(path:\s*'computer_sim',\s*builder:\s*\(context,\s*state\)\s*=>\s*ExitOverlay\(child:\s*computer_sim.AppGate\(\)\)\),", r"", content)
content = re.sub(r"GoRoute\(path:\s*'hindi_sim',\s*builder:\s*\(context,\s*state\)\s*=>\s*ExitOverlay\(child:\s*hindi_sim.AppGate\(\)\)\),", r"", content)

with open(path, 'w') as f:
    f.write(content)
