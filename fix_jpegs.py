from PIL import Image
import glob
import os

for f in glob.glob('assets/images/*.jpg'):
    try:
        img = Image.open(f)
        img.verify()
    except Exception as e:
        print(f"Error reading {f}: {e}")

