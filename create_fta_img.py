import json
from PIL import Image, ImageDraw, ImageFont

def create_image():
    # Image dimensions
    width, height = 800, 500
    
    # Background color (dark slate)
    bg_color = (30, 41, 59)
    
    # Text colors
    title_color = (250, 204, 21) # Yellow
    text_color = (248, 250, 252) # White
    highlight_color = (56, 189, 248) # Light blue
    accent_color = (244, 114, 182) # Pink for primes
    
    # Create image
    img = Image.new('RGB', (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)
    
    # Use default font
    try:
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 32)
        font_text = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
        font_math = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 48)
        font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
    except IOError:
        font_title = ImageFont.load_default()
        font_text = ImageFont.load_default()
        font_math = ImageFont.load_default()
        font_small = ImageFont.load_default()

    # Draw Title
    draw.text((40, 40), "Fundamental Theorem of Arithmetic", fill=title_color, font=font_title)
    
    # Draw text
    draw.text((40, 100), "Every composite number is a unique product of primes!", fill=text_color, font=font_text)
    
    # Draw Math Tree for 12
    # 12 -> 2 and 6
    # 6 -> 2 and 3
    
    # 12
    draw.text((380, 160), "12", fill=highlight_color, font=font_math)
    draw.line((370, 220, 320, 270), fill=text_color, width=3)
    draw.line((430, 220, 480, 270), fill=text_color, width=3)
    
    # 2 and 6
    draw.text((280, 280), "2", fill=accent_color, font=font_math)
    draw.text((270, 340), "(Prime)", fill=accent_color, font=font_small)
    
    draw.text((480, 280), "6", fill=highlight_color, font=font_math)
    draw.line((470, 340, 420, 390), fill=text_color, width=3)
    draw.line((530, 340, 580, 390), fill=text_color, width=3)
    
    # 2 and 3
    draw.text((380, 400), "2", fill=accent_color, font=font_math)
    draw.text((370, 460), "(Prime)", fill=accent_color, font=font_small)
    
    draw.text((580, 400), "3", fill=accent_color, font=font_math)
    draw.text((570, 460), "(Prime)", fill=accent_color, font=font_small)
    
    # Summary
    draw.text((40, 400), "12 = 2 × 2 × 3", fill=title_color, font=font_math)
    draw.text((40, 460), "12 = 2² × 3", fill=highlight_color, font=font_math)
    
    img.save("assets/images/maths_ch1_fta.jpg", quality=95)
    print("Created image!")

create_image()
