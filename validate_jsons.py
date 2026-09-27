import json
import glob
import sys

files = glob.glob('app_core/**/*.json', recursive=True)
error = False
for f in files:
    try:
        with open(f, 'r') as file:
            json.load(file)
        print(f"✅ {f} is valid.")
    except Exception as e:
        print(f"❌ Error in {f}: {e}")
        error = True

if error:
    sys.exit(1)
