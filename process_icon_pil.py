from PIL import Image, ImageDraw

def create_circular_icon():
    img = Image.open('assets/app_icon.png').convert("RGBA")
    width, height = img.size
    print(f"Original size: {width}x{height}")
    
    # We want to create a circular mask
    mask = Image.new('L', (width, height), 0)
    draw = ImageDraw.Draw(mask)
    
    # The circle in the image doesn't perfectly touch the edges.
    # Let's assume the circle has a slight padding. We'll search for the bounding box.
    # We can sample the center row to find the left and right edges of the white circle.
    pixels = img.load()
    
    mid_y = height // 2
    left_x = 0
    right_x = width - 1
    
    # Find left edge of white circle
    for x in range(width):
        r, g, b, a = pixels[x, mid_y]
        if r > 240 and g > 240 and b > 240:
            left_x = x
            break
            
    # Find right edge
    for x in range(width - 1, -1, -1):
        r, g, b, a = pixels[x, mid_y]
        if r > 240 and g > 240 and b > 240:
            right_x = x
            break
            
    # Find top edge
    mid_x = width // 2
    top_y = 0
    for y in range(height):
        r, g, b, a = pixels[mid_x, y]
        if r > 240 and g > 240 and b > 240:
            top_y = y
            break
            
    # Find bottom edge
    bottom_y = height - 1
    for y in range(height - 1, -1, -1):
        r, g, b, a = pixels[mid_x, y]
        if r > 240 and g > 240 and b > 240:
            bottom_y = y
            break
            
    print(f"Detected bounding box: Left={left_x}, Right={right_x}, Top={top_y}, Bottom={bottom_y}")
    
    # Define a bounding box for the mask
    # We slightly reduce the radius (add 1 or 2 pixels of margin) to avoid anti-aliasing artifacts
    margin = 2
    bbox = [left_x + margin, top_y + margin, right_x - margin, bottom_y - margin]
    
    # Draw a solid white circle on the mask
    draw.ellipse(bbox, fill=255)
    
    # Apply the mask to the alpha channel
    result = img.copy()
    result.putalpha(mask)
    
    # Crop the image tightly to the circle bounding box
    result = result.crop((left_x, top_y, right_x, bottom_y))
    
    result.save('assets/app_icon_round.png')
    print("Saved as assets/app_icon_round.png")

if __name__ == "__main__":
    create_circular_icon()
