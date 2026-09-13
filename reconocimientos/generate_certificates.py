# -*- coding: utf-8 -*-
import os
import tempfile
from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Input paths
BASE_DIR = r'c:\Users\Lenovo\Documents\primavera brain\reconocimientos'
TXT_PATH = os.path.join(BASE_DIR, 'listado de nombres.txt')
IMG_QUINGEANERA = os.path.join(BASE_DIR, 'rq.png')
IMG_CHAMBELAN = os.path.join(BASE_DIR, 'rch.png')

# Output directory
PDF_OUT_DIR = os.path.join(BASE_DIR, 'pdfs')
os.makedirs(PDF_OUT_DIR, exist_ok=True)

# Configuration for drawing text
FONT_PATH = r'C:\Windows\Fonts\georgiab.ttf'
BASE_FONT_SIZE = 30
COLOR = (200, 56, 101)  # RGB matching the 'RECONOCIMIENTO' text

# Layout configurations
LAYOUTS = {
    'quinceanera': {
        'x_center': 310,
        'y_center': 610,
        'max_width': 500
    },
    'chambelan': {
        'x_center': 310,
        'y_center': 583,
        'max_width': 500
    }
}

def parse_names(file_path):
    """
    Parses names from the txt file.
    Uses 'quince' and 'chambel' to identify categories to be robust against encoding.
    """
    quinceaneras = []
    chambelanes = []
    current_category = None
    
    # Read with utf-8 encoding
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            lower_line = line.lower()
            if 'quince' in lower_line:
                current_category = 'quinceanera'
                continue
            elif 'chambel' in lower_line:
                current_category = 'chambelan'
                continue
            elif 'reconocimiento' in lower_line:
                continue  # skip title line
            
            # Add to list based on active category
            if current_category == 'quinceanera':
                quinceaneras.append(line)
            elif current_category == 'chambelan':
                chambelanes.append(line)
                
    return quinceaneras, chambelanes

def create_certificate_pdf(name, bg_img_path, output_pdf_path, x_center, y_center, max_width):
    """
    Generates a certificate image with the name overlaid and saves it as a US Letter size PDF.
    """
    # 1. Open background image
    img = Image.open(bg_img_path)
    draw = ImageDraw.Draw(img)
    
    # 2. Determine font and adjust size if name is too long
    font_size = BASE_FONT_SIZE
    font = ImageFont.truetype(FONT_PATH, font_size)
    bbox = font.getbbox(name)
    width = bbox[2] - bbox[0]
    
    while width > max_width and font_size > 12:
        font_size -= 1
        font = ImageFont.truetype(FONT_PATH, font_size)
        bbox = font.getbbox(name)
        width = bbox[2] - bbox[0]
        
    # Log if text was resized
    if font_size < BASE_FONT_SIZE:
        print(f"  [Info] Name '{name}' resized to {font_size}pt to fit container.")
        
    # 3. Draw text centered
    draw.text((x_center, y_center), name, fill=COLOR, font=font, anchor="mm")
    
    # 4. Save to temporary PNG file
    temp_fd, temp_png_path = tempfile.mkstemp(suffix=".png")
    os.close(temp_fd)
    try:
        img.save(temp_png_path, "PNG")
        
        # 5. Convert to US Letter size PDF using ReportLab
        c = canvas.Canvas(output_pdf_path, pagesize=letter)
        # Letter width is 612 pt, height is 792 pt
        c.drawImage(temp_png_path, 0, 0, width=612, height=792)
        c.showPage()
        c.save()
    finally:
        # Clean up temp file
        if os.path.exists(temp_png_path):
            os.remove(temp_png_path)

def main():
    print("Starting certificate generation...")
    
    # Parse lists of names
    quinceaneras, chambelanes = parse_names(TXT_PATH)
    print(f"Found {len(quinceaneras)} quinceañeras and {len(chambelanes)} chambelanes.")
    
    # Generate for Quinceañeras
    print("\nGenerating Quinceañeras certificates...")
    config_q = LAYOUTS['quinceanera']
    for idx, name in enumerate(quinceaneras, 1):
        # Format filename
        safe_name = name.replace(" ", "_")
        pdf_filename = f"Reconocimiento_Quinceanera_{safe_name}.pdf"
        pdf_path = os.path.join(PDF_OUT_DIR, pdf_filename)
        
        print(f"[{idx}/{len(quinceaneras)}] Generating PDF for: {name}")
        create_certificate_pdf(
            name, 
            IMG_QUINGEANERA, 
            pdf_path,
            x_center=config_q['x_center'],
            y_center=config_q['y_center'],
            max_width=config_q['max_width']
        )
        
    # Generate for Chambelanes
    print("\nGenerating Chambelanes certificates...")
    config_c = LAYOUTS['chambelan']
    for idx, name in enumerate(chambelanes, 1):
        # Format filename
        safe_name = name.replace(" ", "_")
        pdf_filename = f"Reconocimiento_Chambelan_{safe_name}.pdf"
        pdf_path = os.path.join(PDF_OUT_DIR, pdf_filename)
        
        print(f"[{idx}/{len(chambelanes)}] Generating PDF for: {name}")
        create_certificate_pdf(
            name, 
            IMG_CHAMBELAN, 
            pdf_path,
            x_center=config_c['x_center'],
            y_center=config_c['y_center'],
            max_width=config_c['max_width']
        )
        
    print("\nAll certificates generated successfully!")
    print(f"PDFs are saved in: {PDF_OUT_DIR}")

if __name__ == '__main__':
    main()
