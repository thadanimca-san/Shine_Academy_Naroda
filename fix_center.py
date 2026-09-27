from PIL import Image, ImageDraw

def process_image(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    width, height = img.size
    
    pixels = img.load()
    
    # Let's sample the top-left pixel to get the background color (the blue square color)
    bg_color = pixels[0, 0]
    
    # We want to find the bounding box of everything that is NOT the bg_color.
    # To be safe against compression artifacts, we use a color distance threshold.
    def color_dist(c1, c2):
        return sum((a - b) ** 2 for a, b in zip(c1[:3], c2[:3]))
    
    min_x = width
    min_y = height
    max_x = 0
    max_y = 0
    
    for y in range(height):
        for x in range(width):
            if color_dist(pixels[x, y], bg_color) > 1000: # Threshold
                if x < min_x: min_x = x
                if y < min_y: min_y = y
                if x > max_x: max_x = x
                if y > max_y: max_y = y
                
    # Now we have the exact bounding box of the white circle!
    # Let's crop exactly to this bounding box
    cropped = img.crop((min_x, min_y, max_x, max_y))
    
    new_width, new_height = cropped.size
    
    # Create a circular mask for this perfectly cropped image
    mask = Image.new('L', (new_width, new_height), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, new_width, new_height), fill=255)
    
    result = Image.new('RGBA', (new_width, new_height), (0,0,0,0))
    result.paste(cropped, (0, 0), mask=mask)
    
    result.save(output_path)
    print(f"Detected bounds: ({min_x}, {min_y}, {max_x}, {max_y})")
    print("Perfectly centered image saved.")

process_image('/home/ubuntu/.gemini/antigravity/brain/fec251e7-56c6-4b62-97ea-fb1fb0fb087d/media__1786120775147.png', '/home/ubuntu/Shine_Academy_Naroda/assets/app_icon_transparent.png')
