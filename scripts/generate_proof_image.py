import os
from PIL import Image, ImageDraw, ImageFont

def generate_proof_image(output_path):
    # Image dimensions
    width, height = 1200, 2800
    
    # Colors (Dark theme with teal/purple accents)
    bg_color = (15, 23, 42) # Dark slate
    title_color = (45, 212, 191) # Teal
    step_color = (192, 132, 252) # Purple
    text_color = (248, 250, 252) # Off-white
    highlight_color = (251, 191, 36) # Amber for contradiction
    
    # Create image
    img = Image.new('RGB', (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)
    
    # Try to load a nice font, fallback to default
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 64)
        step_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 48)
        text_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 42)
        math_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf", 42)
    except:
        title_font = ImageFont.load_default()
        step_font = ImageFont.load_default()
        text_font = ImageFont.load_default()
        math_font = ImageFont.load_default()
        print("Warning: Standard fonts not found, using default.")

    # Content
    y_offset = 80
    margin = 80
    
    # Title
    draw.text((margin, y_offset), "Proof by Contradiction:", font=title_font, fill=title_color)
    y_offset += 80
    draw.text((margin, y_offset), "√2 is Irrational", font=title_font, fill=title_color)
    y_offset += 120
    
    # Steps
    steps = [
        ("Step 1: The Assumption", "Let us assume that √2 is a rational number.\nThis means we can write it as a fraction\nin simplest form:\n√2 = a / b\nwhere 'a' and 'b' are co-prime integers\n(meaning they have no common factors)."),
        ("Step 2: Squaring Both Sides", "Square both sides of the equation:\n2 = a² / b²\nRearrange to solve for a²:\na² = 2b²"),
        ("Step 3: What this means for 'a'", "Since a² = 2 × (something),\na² must be an EVEN number.\nIf a square is even, its root must also be even.\nTherefore, 'a' is an EVEN number.\nWe can write: a = 2c (where c is some integer)."),
        ("Step 4: Substitute back", "Substitute a = 2c into our equation (a² = 2b²):\n(2c)² = 2b²\n4c² = 2b²\nDivide by 2:\n2c² = b²"),
        ("Step 5: What this means for 'b'", "Now we see that b² = 2 × (something).\nThis means b² is an EVEN number.\nTherefore, 'b' is also an EVEN number."),
        ("Step 6: The Contradiction!", "We just proved that BOTH 'a' and 'b' are EVEN.\nThis means they share a common factor of 2.\nBUT in Step 1, we assumed they were co-prime\n(no common factors).\nThis is a LOGICAL CONTRADICTION!"),
        ("Conclusion:", "Our initial assumption was completely wrong.\nTherefore, √2 cannot be written as a fraction.\n√2 is IRRATIONAL.")
    ]
    
    for i, (title, content) in enumerate(steps):
        # Draw step title
        color = highlight_color if i >= 5 else step_color
        draw.text((margin, y_offset), title, font=step_font, fill=color)
        y_offset += 60
        
        # Draw step content
        for line in content.split('\n'):
            draw.text((margin + 40, y_offset), line, font=text_font, fill=text_color)
            y_offset += 55
            
        y_offset += 40
        
    # Draw a nice border
    draw.rectangle([20, 20, width-20, height-20], outline=title_color, width=4)
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Save
    img.save(output_path)
    print(f"Generated complete proof image at: {output_path}")

if __name__ == "__main__":
    output_path = "/home/ubuntu/Shine_Academy_Naroda/assets/images/maths_ch1_contradiction.jpg"
    generate_proof_image(output_path)
