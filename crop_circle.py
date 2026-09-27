from PIL import Image, ImageDraw

def crop_to_circle(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    
    # Assuming the white circle is centered. We will just create a circular mask
    # that is exactly the size of the image, or slightly smaller if the blue square is large.
    # Let's inspect the image size first.
    width, height = img.size
    
    # Create a mask same size as image
    mask = Image.new('L', (width, height), 0)
    draw = ImageDraw.Draw(mask)
    
    # The blue square is the background. The circle is inside.
    # Looking at the thumbnail, the circle touches the edges of the square.
    # So the bounding box for the circle is (0, 0, width, height)
    draw.ellipse((0, 0, width, height), fill=255)
    
    # Apply the mask
    result = Image.new('RGBA', (width, height), (0,0,0,0))
    result.paste(img, (0, 0), mask=mask)
    
    # Save the result
    result.save(output_path)
    print("Image processed successfully.")

crop_to_circle('/home/ubuntu/.gemini/antigravity/brain/fec251e7-56c6-4b62-97ea-fb1fb0fb087d/media__1786120775147.png', '/home/ubuntu/Shine_Academy_Naroda/assets/app_icon_transparent.png')
