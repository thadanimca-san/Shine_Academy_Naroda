from PIL import Image
import glob
import os

for f in glob.glob('assets/images/*.jpg'):
    try:
        img = Image.open(f)
        # Convert to RGB to strip any weird CMYK or indexed palettes
        img = img.convert('RGB')
        img.save(f, 'JPEG', quality=90)
        print(f"Re-encoded {f}")
    except Exception as e:
        print(f"Error reading {f}: {e}")

for f in glob.glob('assets/dictionary/*.jpg'):
    try:
        img = Image.open(f)
        img = img.convert('RGB')
        img.save(f, 'JPEG', quality=90)
        print(f"Re-encoded {f}")
    except Exception as e:
        pass

