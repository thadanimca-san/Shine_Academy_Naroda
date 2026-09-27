from PIL import Image, ImageDraw

def create_icon(input_path, output_path):
    # Open the HD rectangular logo (1536x1024)
    img = Image.open(input_path).convert("RGBA")
    orig_w, orig_h = img.size
    
    # We want a 1536x1536 perfectly square, HD icon
    size = 1536
    
    # Create a transparent square canvas
    canvas = Image.new('RGBA', (size, size), (0,0,0,0))
    
    # Draw a perfect white circle on the canvas
    draw = ImageDraw.Draw(canvas)
    draw.ellipse((0, 0, size, size), fill=(255, 255, 255, 255))
    
    # We need to scale the logo so it fits INSIDE the circle.
    # The circle has diameter 1536. 
    # Let's scale the logo down to a width of 1100 so it has some breathing room inside the circle.
    target_w = 1200
    target_h = int(orig_h * (target_w / orig_w))
    img_resized = img.resize((target_w, target_h), Image.Resampling.LANCZOS)
    
    # Calculate perfectly centered coordinates
    x = (size - target_w) // 2
    y = (size - target_h) // 2
    
    # Paste the resized logo onto the white circle (using the logo's alpha just in case, though it's a JPG)
    canvas.paste(img_resized, (x, y), img_resized)
    
    # Save the final HD icon
    canvas.save(output_path)
    print("HD Icon created successfully!")

create_icon('/home/ubuntu/Shine_Academy_Naroda/assets/shineacademynarodalogo.jpg', '/home/ubuntu/Shine_Academy_Naroda/assets/app_icon_transparent.png')
