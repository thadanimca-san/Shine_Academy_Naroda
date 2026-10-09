import os
import re

json_dir = 'app_core/chapters/'
source_dir = 'science_images_from_prompts/'
target_dir = 'assets/images/science/'

# Find all required image URLs in JSONs
required_images = []
for file in os.listdir(json_dir):
    if not file.endswith('.json'): continue
    with open(os.path.join(json_dir, file), 'r', encoding='utf-8') as f:
        content = f.read()
        urls = re.findall(r'"image_url":\s*"(assets/images/science/[^"]+)"', content)
        required_images.extend(urls)

# Find missing ones
missing_images = []
for url in required_images:
    if not os.path.exists(url):
        missing_images.append(url)

# Sort them just to be deterministic
missing_images = sorted(list(set(missing_images)))

# List available prompts images
available_images = []
for file in os.listdir(source_dir):
    if file.endswith('.png') or file.endswith('.webp'):
        # Extract row number for proper sorting
        match = re.search(r'row (\d+)', file)
        row = int(match.group(1)) if match else 999
        available_images.append((row, file))

available_images.sort(key=lambda x: x[0])

# Map available to missing
count = 0
for row, file in available_images:
    if count >= len(missing_images):
        break
    
    target_path = missing_images[count]
    source_path = os.path.join(source_dir, file)
    
    os.system(f'cp "{source_path}" "{target_path}"')
    print(f'Mapped {file} -> {target_path}')
    count += 1

print(f"Successfully mapped {count} missing images.")
