import os
from PIL import Image, ImageDraw, ImageFont

# Load re.png
img_path = r"reconocimientos\re.png"
logo_path = r"C:\Users\Lenovo\Documents\expo expositores\assets\logo_new5.png"

def test_dresses_overlay_v3(option_name, x, y, size=110):
    img = Image.open(img_path).convert('RGB')
    img_letter = img.resize((1275, 1650))
    draw = ImageDraw.Draw(img_letter)
    
    # Write name
    font_path = r'C:\Windows\Fonts\georgiab.ttf'
    font = ImageFont.truetype(font_path, 36)
    name = "Humberto Carranza Núñez"
    color = (200, 56, 101)
    draw.text((328, 668), name, fill=color, font=font, anchor="mm")
    
    # Load and overlay logo
    if os.path.exists(logo_path):
        logo = Image.open(logo_path).convert('RGBA')
        logo = logo.resize((size, size))
        img_letter.paste(logo, (x, y), logo)
            
    out_path = f"scratch/draft_dresses_v3_{option_name}.png"
    img_letter.save(out_path, "PNG")
    print(f"Draft saved to {out_path}")

# Test slightly shifted:
test_dresses_overlay_v3("shift_970_910", 970, 910)
test_dresses_overlay_v3("shift_980_950", 980, 950)
