import json
from PIL import Image, ImageDraw, ImageFont

def create_image():
    # Image dimensions
    width, height = 800, 600
    
    # Background color (dark blue/slate)
    bg_color = (30, 41, 59)
    
    # Text colors
    title_color = (250, 204, 21) # Yellow
    text_color = (248, 250, 252) # White
    highlight_color = (56, 189, 248) # Light blue
    
    # Create image
    img = Image.new('RGB', (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)
    
    # Use default font
    try:
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
        font_text = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
        font_math = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf", 28)
    except IOError:
        font_title = ImageFont.load_default()
        font_text = ImageFont.load_default()
        font_math = ImageFont.load_default()

    # Draw Title
    draw.text((40, 40), "Proof by Contradiction: √2 is Irrational", fill=title_color, font=font_title)
    
    # Draw steps
    y = 120
    spacing = 45
    
    steps = [
        ("Step 1: The Wrong Assumption", text_color, font_text),
        ("Let us assume the OPPOSITE of what we want to prove.", text_color, font_text),
        ("Assume √2 is a rational number.", highlight_color, font_math),
        ("", text_color, font_text),
        
        ("Step 2: The Setup", text_color, font_text),
        ("If it is rational, it can be written as a fraction p/q", text_color, font_text),
        ("where p and q are co-prime (no common factors).", text_color, font_text),
        ("√2 = p/q", highlight_color, font_math),
        ("", text_color, font_text),
        
        ("Step 3: The Algebra", text_color, font_text),
        ("Square both sides: 2 = p² / q²", highlight_color, font_math),
        ("Rearrange: 2q² = p²", highlight_color, font_math),
        ("This means p² is an even number, so p is also even.", text_color, font_text),
        ("", text_color, font_text),
        
        ("Step 4: The Contradiction!", title_color, font_title),
        ("If p is even, then p = 2k. Substitute back:", text_color, font_text),
        ("2q² = (2k)²  ->  2q² = 4k²  ->  q² = 2k²", highlight_color, font_math),
        ("Now q is also even! But we said p and q have NO common factors!", text_color, font_text),
        ("Our assumption was wrong. √2 MUST be irrational.", title_color, font_math)
    ]
    
    for text, color, font in steps:
        draw.text((40, y), text, fill=color, font=font)
        y += spacing
        if font == font_title:
            y += 10
            
    img.save("assets/images/maths_ch1_contradiction.jpg", quality=95)
    print("Created image!")

create_image()
