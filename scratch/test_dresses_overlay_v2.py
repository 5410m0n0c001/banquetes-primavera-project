import os
from PIL import Image, ImageDraw, ImageFont

# Load re.png
img_path = r"reconocimientos\re.png"
logo_path = r"C:\Users\Lenovo\Documents\expo expositores\assets\logo_new5.png"

def test_dresses_overlay_v2(option_name, x, y, size=110): # Slightly smaller logo for better fit
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
            
    out_path = f"scratch/draft_dresses_v2_{option_name}.png"
    img_letter.save(out_path, "PNG")
    print(f"Draft saved to {out_path}")

# Test new options:
# Option D: More to the right, over the pink dress border at Y=900 (X=960, Y=900, size 110)
test_dresses_overlay_v2("right_skirts_mid", 960, 900)

# Option E: Lower down, between their skirts (X=930, Y=1150, size 110)
test_dresses_overlay_v2("bottom_right_skirts", 930, 1150)

# Option F: Between their waists/hips but shifted right to avoid "EXPO BODA" text (X=960, Y=620, size 110)
test_dresses_overlay_v2("right_waists", 960, 620)
