import os
from PIL import Image, ImageDraw, ImageFont
import qrcode

# Paths
brain_dir = r"C:\Users\Lenovo\.gemini\antigravity\brain\2a465b7c-538b-40b3-8943-c29e5c6f6bdb"
clasico_template = os.path.join(brain_dir, "media__1783174544740.png")
premium_template = os.path.join(brain_dir, "media__1783174544748.jpg")

base_output_dir = r"C:\Users\Lenovo\Documents\primavera brain\identificadores_mesa_resenas"
clasico_out_dir = os.path.join(base_output_dir, "clasico")
premium_out_dir = os.path.join(base_output_dir, "premium_black")

# Create output directories if they don't exist
os.makedirs(clasico_out_dir, exist_ok=True)
os.makedirs(premium_out_dir, exist_ok=True)

# Font configuration
font_path = r"C:\Windows\Fonts\georgiab.ttf"
if not os.path.exists(font_path):
    font_path = "georgiab.ttf"
font_size = 320

# Google Review Link
review_url = "https://g.page/r/CRYo3lgLK8NEEBM/review"

# Generate a high-contrast, low-density QR code (Level L) pointing to Google Review link
def make_clear_qr(size, back_color):
    qr = qrcode.QRCode(
        version=None, # auto-fit
        error_correction=qrcode.constants.ERROR_CORRECT_L, # Level L (lowest density)
        box_size=10,
        border=2,
    )
    qr.add_data(review_url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color=back_color).convert("RGBA")
    return qr_img.resize((size, size), Image.Resampling.LANCZOS)

print("Starting generation of 60 table cards (1 to 30 for Clásico & Premium)...")

# Generate 30 Clásico cards
if os.path.exists(clasico_template):
    for i in range(1, 31):
        img = Image.open(clasico_template).convert("RGBA")
        draw = ImageDraw.Draw(img)
        
        # Patch starts exactly at Y=350 to leave the word "Mesa" untouched
        draw.rectangle([210, 350, 520, 800], fill=(254, 254, 254, 255))
        
        # Load font and draw table number in Burgundy
        try:
            font = ImageFont.truetype(font_path, font_size)
        except Exception:
            font = ImageFont.load_default()
        
        draw.text((365, 515), str(i), fill=(129, 64, 80, 255), font=font, anchor="mm")
        
        # Generate 190x190 QR code pointing to review URL
        qr_img = make_clear_qr(190, (254, 254, 254))
        img.paste(qr_img, (440, 700), qr_img)
        
        # Save directly as PDF
        pdf_path = os.path.join(clasico_out_dir, f"identificador_mesa_{i}.pdf")
        img.convert("RGB").save(pdf_path, "PDF")
        
    print("All 30 Clásico table cards generated successfully in PDF!")
else:
    print(f"Error: Clásico template not found at {clasico_template}")

# Generate 30 Premium Black cards
if os.path.exists(premium_template):
    for i in range(1, 31):
        img = Image.open(premium_template).convert("RGBA")
        draw = ImageDraw.Draw(img)
        
        # Patch starts exactly at Y=350 to leave the word "Mesa" untouched
        draw.rectangle([210, 350, 520, 800], fill=(6, 6, 6, 255))
        
        # Load font and draw table number in Gold
        try:
            font = ImageFont.truetype(font_path, font_size)
        except Exception:
            font = ImageFont.load_default()
        
        draw.text((365, 515), str(i), fill=(214, 163, 71, 255), font=font, anchor="mm")
        
        # Create white background square for QR code (190x190)
        draw.rectangle([440, 700, 630, 890], fill=(255, 255, 255, 255))
        draw.rectangle([440, 700, 630, 890], outline=(214, 163, 71, 255), width=3)
        
        # Paste black QR code inside the box (170x170)
        qr_img = make_clear_qr(170, (255, 255, 255))
        img.paste(qr_img, (450, 710), qr_img)
        
        # Save directly as PDF
        pdf_path = os.path.join(premium_out_dir, f"identificador_mesa_{i}.pdf")
        img.convert("RGB").save(pdf_path, "PDF")
        
    print("All 30 Premium Black table cards generated successfully in PDF!")
else:
    print(f"Error: Premium template not found at {premium_template}")

print("Verification: All 60 table cards are ready in C:\\Users\\Lenovo\\Documents\\primavera brain\\identificadores_mesa_resenas")
