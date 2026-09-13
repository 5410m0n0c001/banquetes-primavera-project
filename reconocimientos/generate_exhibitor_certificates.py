# -*- coding: utf-8 -*-
import os
import json
import re
from PIL import Image, ImageDraw, ImageFont

# Input paths
BASE_DIR = r'c:\Users\Lenovo\Documents\primavera brain\reconocimientos'
ROSTER_PATH = r'c:\Users\Lenovo\Documents\primavera brain\scratch\final_roster.json'
TEMPLATE_PATH = os.path.join(BASE_DIR, 're.png')
ASSETS_DIR = r'C:\Users\Lenovo\Documents\expo expositores\assets'

# Output directory
PNG_OUT_DIR = os.path.join(BASE_DIR, 'pngs')
os.makedirs(PNG_OUT_DIR, exist_ok=True)

# Configuration for drawing text
FONT_PATH = r'C:\Windows\Fonts\georgiab.ttf'
BASE_FONT_SIZE = 36
TEXT_COLOR = (200, 56, 101) # RGB pink/red matching 'RECONOCIMIENTO'

# Layout coordinates (scaled for Letter size 1275x1650)
X_CENTER = 328
Y_CENTER = 668
MAX_WIDTH = 500

# Logo coordinates (scaled for Letter size 1275x1650)
LOGO_X = 980
LOGO_Y = 950
LOGO_SIZE = 110

def sanitize_filename(name):
    """
    Cleans up the name to make a safe filename.
    """
    # Replace non-alphanumeric (except underscores) with empty space or underscore
    # Remove accents/special chars to be safe on all systems
    import unicodedata
    n = unicodedata.normalize('NFKD', name).encode('ASCII', 'ignore').decode('ASCII')
    n = re.sub(r'[^\w\s-]', '', n)
    n = n.strip().replace(' ', '_')
    return n

def main():
    print("Starting certificate generation script...")
    
    # 1. Load the roster
    if not os.path.exists(ROSTER_PATH):
        print(f"Error: consolidated roster not found at {ROSTER_PATH}")
        return
        
    with open(ROSTER_PATH, "r", encoding="utf-8") as f:
        roster = json.load(f)
        
    print(f"Loaded roster with {len(roster)} entries.")
    
    # 2. Check font
    if not os.path.exists(FONT_PATH):
        print(f"Warning: Font {FONT_PATH} not found. Falling back to default font.")
        use_default_font = True
    else:
        use_default_font = False
        
    # 3. Process each participant
    for idx, entry in enumerate(roster, 1):
        name = entry["displayName"]
        brand = entry["brandName"]
        logo_name = entry["logoName"]
        
        print(f"\n[{idx}/{len(roster)}] Processing: '{name}' (Brand: '{brand}')")
        
        # Load template
        if not os.path.exists(TEMPLATE_PATH):
            print(f"  Error: Base template image {TEMPLATE_PATH} not found!")
            continue
            
        img = Image.open(TEMPLATE_PATH).convert('RGB')
        
        # Resize to US Letter size (1275 x 1650 pixels)
        img_letter = img.resize((1275, 1650))
        draw = ImageDraw.Draw(img_letter)
        
        # Select font and shrink size if name is too long
        font_size = BASE_FONT_SIZE
        if use_default_font:
            font = ImageFont.load_default()
        else:
            font = ImageFont.truetype(FONT_PATH, font_size)
            
            # Check width
            bbox = font.getbbox(name)
            width = bbox[2] - bbox[0]
            
            while width > MAX_WIDTH and font_size > 14:
                font_size -= 1
                font = ImageFont.truetype(FONT_PATH, font_size)
                bbox = font.getbbox(name)
                width = bbox[2] - bbox[0]
                
            if font_size < BASE_FONT_SIZE:
                print(f"  [Info] Text shrunk to {font_size}pt to fit inside line.")
                
        # Draw the name centered horizontally and vertically at designated coordinate
        draw.text((X_CENTER, Y_CENTER), name, fill=TEXT_COLOR, font=font, anchor="mm")
        
        # Overlay the logo if it exists and matches
        if logo_name:
            logo_path = os.path.join(ASSETS_DIR, logo_name)
            if os.path.exists(logo_path):
                try:
                    logo = Image.open(logo_path).convert('RGBA')
                    logo = logo.resize((LOGO_SIZE, LOGO_SIZE))
                    
                    # Paste using the logo itself as alpha mask to preserve transparency
                    img_letter.paste(logo, (LOGO_X, LOGO_Y), logo)
                    print(f"  [Info] Logo '{logo_name}' successfully overlayed at bottom-right.")
                except Exception as e:
                    print(f"  [Warning] Failed to paste logo '{logo_name}': {e}")
            else:
                print(f"  [Warning] Logo file '{logo_name}' not found in assets directory.")
        else:
            print("  [Info] No logo to draw (exhibitor has no logo).")
            
        # Save output PNG
        safe_name = sanitize_filename(name)
        out_filename = f"Reconocimiento_Expositor_{safe_name}.png"
        out_path = os.path.join(PNG_OUT_DIR, out_filename)
        
        img_letter.save(out_path, "PNG")
        print(f"  [Success] Saved certificate to: {out_path}")
        
    print("\nAll certificates generated successfully!")
    print(f"PNG files are saved in: {PNG_OUT_DIR}")

if __name__ == '__main__':
    main()
