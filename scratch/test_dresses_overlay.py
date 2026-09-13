import os
from PIL import Image, ImageDraw, ImageFont

# Load re.png
img_path = r"reconocimientos\re.png"
logo_path = r"C:\Users\Lenovo\Documents\expo expositores\assets\logo_new5.png"

def test_dresses_overlay(option_name, x, y, size=130):
    img = Image.open(img_path).convert('RGB')
    # Resize background to Letter size (1275 x 1650)
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
        # Paste logo
        img_letter.paste(logo, (x, y), logo)
            
    out_path = f"scratch/draft_dresses_{option_name}.png"
    img_letter.save(out_path, "PNG")
    print(f"Draft saved to {out_path}")

# Let's test different X and Y positions between/around the dresses:
# Option A: Between their waists/hips (X=870, Y=620)
test_dresses_overlay("waists", 870, 620)

# Option B: Slightly lower, between their skirts (X=860, Y=780)
test_dresses_overlay("skirts_mid", 860, 780)

# Option C: Even lower, near the bottom right (X=850, Y=950)
test_dresses_overlay("skirts_low", 850, 950)
