from PIL import Image, ImageDraw

def create_circular_icon():
    img = Image.open('assets/app_icon.png').convert("RGBA")
    width, height = img.size
    print(f"Original size: {width}x{height}")
    
    pixels = img.load()
    bg_color = pixels[0, 0][:3]  # Get RGB of top-left pixel
    
    mid_y = height // 2
    left_x = 0
    right_x = width - 1
    
    # Tolerance for background color matching
    def is_bg(c):
        return abs(c[0] - bg_color[0]) < 10 and abs(c[1] - bg_color[1]) < 10 and abs(c[2] - bg_color[2]) < 10
    
    # Find left edge of the circle
    for x in range(width):
        if not is_bg(pixels[x, mid_y][:3]):
            left_x = x
            break
            
    # Find right edge
    for x in range(width - 1, -1, -1):
        if not is_bg(pixels[x, mid_y][:3]):
            right_x = x
            break
            
    # Find top edge
    mid_x = width // 2
    top_y = 0
    for y in range(height):
        if not is_bg(pixels[mid_x, y][:3]):
            top_y = y
            break
            
    # Find bottom edge
    bottom_y = height - 1
    for y in range(height - 1, -1, -1):
        if not is_bg(pixels[mid_x, y][:3]):
            bottom_y = y
            break
            
    print(f"Detected bounding box: Left={left_x}, Right={right_x}, Top={top_y}, Bottom={bottom_y}")
    
    # In case detection fails, use a fallback
    if left_x >= right_x or top_y >= bottom_y or right_x - left_x < 100:
        print("Detection failed, using 90% of image size as fallback.")
        margin = int(width * 0.05)
        left_x, right_x = margin, width - margin
        top_y, bottom_y = margin, height - margin
        
    mask = Image.new('L', (width, height), 0)
    draw = ImageDraw.Draw(mask)
    
    margin = 2
    bbox = [left_x + margin, top_y + margin, right_x - margin, bottom_y - margin]
    draw.ellipse(bbox, fill=255)
    
    result = img.copy()
    result.putalpha(mask)
    
    result = result.crop((left_x, top_y, right_x, bottom_y))
    result.save('assets/app_icon_round.png')
    print("Saved as assets/app_icon_round.png")

if __name__ == "__main__":
    create_circular_icon()
