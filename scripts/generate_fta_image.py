import os
from PIL import Image, ImageDraw, ImageFont

def generate_fta_image(output_path):
    width, height = 1200, 1000
    bg_color = (15, 23, 42) # Dark slate
    title_color = (45, 212, 191) # Teal
    step_color = (192, 132, 252) # Purple
    text_color = (248, 250, 252) # Off-white
    
    img = Image.new('RGB', (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)
    
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 64)
        subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf", 42)
        math_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 96)
        text_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 48)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        math_font = ImageFont.load_default()
        text_font = ImageFont.load_default()

    margin = 80
    y_offset = 80
    
    draw.text((margin, y_offset), "Fundamental Theorem", font=title_font, fill=title_color)
    y_offset += 80
    draw.text((margin, y_offset), "of Arithmetic", font=title_font, fill=title_color)
    y_offset += 120
    
    desc = "Every composite number can be uniquely\nexpressed as a product of primes."
    for line in desc.split('\n'):
        draw.text((margin, y_offset), line, font=subtitle_font, fill=text_color)
        y_offset += 60
        
    y_offset += 80
    draw.text((margin, y_offset), "Example: Factoring 12", font=text_font, fill=step_color)
    y_offset += 120
    
    draw.text((margin + 100, y_offset), "12 = 2 × 2 × 3", font=math_font, fill=title_color)
    y_offset += 140
    
    draw.text((margin + 100, y_offset), "12 = 2² × 3", font=math_font, fill=step_color)
    
    draw.rectangle([20, 20, width-20, height-20], outline=title_color, width=4)
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path)
    print(f"Generated FTA image at: {output_path}")

if __name__ == "__main__":
    output_path = "/home/ubuntu/Shine_Academy_Naroda/assets/images/maths_ch1_fta.jpg"
    generate_fta_image(output_path)
