from PIL import Image, ImageDraw

def reduce_border(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    width, height = img.size
    
    # We want to reduce the border. This means cropping inward.
    # Let's crop 10 pixels from every side.
    crop_amount = 12
    left = crop_amount
    top = crop_amount
    right = width - crop_amount
    bottom = height - crop_amount
    
    # Crop the image tighter
    cropped = img.crop((left, top, right, bottom))
    new_width, new_height = cropped.size
    
    # Now apply a circular mask to the tightly cropped image
    mask = Image.new('L', (new_width, new_height), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, new_width, new_height), fill=255)
    
    result = Image.new('RGBA', (new_width, new_height), (0,0,0,0))
    result.paste(cropped, (0, 0), mask=mask)
    
    # Save the result
    result.save(output_path)
    print("Image cropped tighter successfully.")

reduce_border('/home/ubuntu/.gemini/antigravity/brain/fec251e7-56c6-4b62-97ea-fb1fb0fb087d/media__1786120775147.png', '/home/ubuntu/Shine_Academy_Naroda/assets/app_icon_transparent.png')
