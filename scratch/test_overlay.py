import os
from PIL import Image, ImageDraw, ImageFont

# Load re.png
img_path = r"reconocimientos\re.png"
logo_path = r"C:\Users\Lenovo\Documents\expo expositores\assets\logo_new5.png"

# Target US Letter size: 1275 x 1650 (at 150 DPI)
# The original size is 1080 x 1457.
# Scaling factor:
# X scale: 1275 / 1080 = 1.1805
# Y scale: 1650 / 1457 = 1.1325

def generate_draft(option_name, logo_pos):
    img = Image.open(img_path).convert('RGB')
    # Resize background to Letter size
    img_letter = img.resize((1275, 1650))
    draw = ImageDraw.Draw(img_letter)
    
    # Scale coordinates:
    # Original name line is at Y=610. Let's place text center at Y=590.
    # In Letter size: Y = 590 * 1.1325 = 668.
    # Original X center of line is around 278. In Letter size: X = 278 * 1.1805 = 328.
    # Let's write name
    font_path = r'C:\Windows\Fonts\georgiab.ttf'
    font = ImageFont.truetype(font_path, 36)
    name = "Humberto Carranza Núñez"
    color = (200, 56, 101) # Matching red/pink color
    
    draw.text((328, 668), name, fill=color, font=font, anchor="mm")
    
    # Load and overlay logo
    if os.path.exists(logo_path):
        logo = Image.open(logo_path).convert('RGBA')
        # Resize logo to say 120x120 pixels
        logo = logo.resize((120, 120))
        
        # Paste logo based on option
        if logo_pos == "top_left":
            # Top-left of certificate area: X=50 * 1.1805 = 59, Y=50 * 1.1325 = 57
            img_letter.paste(logo, (60, 60), logo)
        elif logo_pos == "top_right":
            # Top-right of certificate area: X=450 * 1.1805 = 531, Y=50 * 1.1325 = 57
            img_letter.paste(logo, (530, 60), logo)
        elif logo_pos == "bottom_left":
            # Bottom-left of certificate area: X=50, Y=1450
            img_letter.paste(logo, (60, 1400), logo)
        elif logo_pos == "near_name":
            # Place next to the name line or above "A:"
            # Let's put it at Y = 450 (which is above A:), centered horizontally
            # X center is 328, so top-left of 120x120 logo is X = 328 - 60 = 268
            # Y center is Y = 450 * 1.1325 = 510, so Y top-left is 510 - 60 = 450
            img_letter.paste(logo, (268, 500), logo)
            
    out_path = f"scratch/draft_{option_name}.png"
    img_letter.save(out_path, "PNG")
    print(f"Draft saved to {out_path}")

generate_draft("top_left", "top_left")
generate_draft("top_right", "top_right")
generate_draft("near_name", "near_name")
