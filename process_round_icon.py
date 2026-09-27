from PIL import Image, ImageDraw

def make_circle_transparent():
    # Open the image
    img = Image.open('assets/app_icon.png').convert("RGBA")
    
    # Get dimensions
    width, height = img.size
    
    # Create a circular mask
    mask = Image.new('L', (width, height), 0)
    draw = ImageDraw.Draw(mask)
    
    # Draw a white circle filling the exact dimensions
    draw.ellipse((0, 0, width, height), fill=255)
    
    # Apply the mask to the image (this will make the outside of the circle transparent)
    result = Image.new('RGBA', (width, height), (0,0,0,0))
    result.paste(img, (0,0), mask=mask)
    
    # Save the final transparent round icon
    result.save('assets/app_icon_transparent.png')
    print("Successfully created assets/app_icon_transparent.png")

if __name__ == '__main__':
    make_circle_transparent()
