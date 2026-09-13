import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter

# Paths
input_image_path = r"C:\Users\Lenovo\Downloads\Captura de pantalla 2026-08-31 122838.png"
logo_path = r"c:\Users\Lenovo\Documents\primavera brain\assets\images\logo_principal_p.png"

artifact_dir = r"C:\Users\Lenovo\.gemini\antigravity\brain\2662e14f-6269-4a71-8fa5-e4f99bece5d8"
downloads_dir = r"C:\Users\Lenovo\Downloads"
brain_dir = r"C:\Users\Lenovo\Documents\primavera brain"

out_option1_downloads = os.path.join(downloads_dir, "Jose_Gabriel_3_Anos_Portada_TikTok_Gala.png")
out_option1_brain = os.path.join(brain_dir, "Jose_Gabriel_3_Anos_Portada_TikTok_Gala.png")
out_option1_art = os.path.join(artifact_dir, "Jose_Gabriel_3_Anos_Portada_TikTok_Gala.png")

out_option2_downloads = os.path.join(downloads_dir, "Jose_Gabriel_3_Anos_Portada_TikTok_Vibrant.png")
out_option2_brain = os.path.join(brain_dir, "Jose_Gabriel_3_Anos_Portada_TikTok_Vibrant.png")
out_option2_art = os.path.join(artifact_dir, "Jose_Gabriel_3_Anos_Portada_TikTok_Vibrant.png")

def enhance_image(pil_img):
    """
    Enhances image quality, contrast, sharpness, and color saturation without noise artifacts.
    """
    img = pil_img.convert("RGB")
    
    # 1. Mild Denoise / Smoothing pass
    img = img.filter(ImageFilter.SMOOTH_MORE)
    
    # 2. Color Enhancement (Warm champagne & gold boost)
    enhancer_color = ImageEnhance.Color(img)
    img = enhancer_color.enhance(1.15)
    
    # 3. Contrast Enhancement
    enhancer_contrast = ImageEnhance.Contrast(img)
    img = enhancer_contrast.enhance(1.12)
    
    # 4. Brightness Adjustment
    enhancer_brightness = ImageEnhance.Brightness(img)
    img = enhancer_brightness.enhance(1.05)
    
    # 5. Unsharp Masking (Crisp edges for suit, mariachi embroidery & faces)
    img = img.filter(ImageFilter.UnsharpMask(radius=1.5, percent=120, threshold=3))
    
    return img

def create_tiktok_cover(base_img, mode="gala"):
    # TikTok vertical dimensions: 1080 x 1920 (9:16 aspect ratio)
    W, H = 1080, 1920
    
    # Enhance the original cropped image
    enhanced_base = enhance_image(base_img)
    
    # Create main canvas
    canvas = Image.new("RGBA", (W, H), (15, 15, 15, 255))
    
    # Resize base photo to fit in central window
    orig_w, orig_h = enhanced_base.size
    target_photo_h = int(H * 0.74)
    scale = target_photo_h / orig_h
    new_w = int(orig_w * scale)
    new_h = target_photo_h
    
    photo_resized = enhanced_base.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    # Fill background with elegant blurred & darkened version
    blur_bg = enhanced_base.resize((W, H), Image.Resampling.LANCZOS).filter(ImageFilter.GaussianBlur(35))
    dark_bg_overlay = Image.new("RGBA", (W, H), (12, 12, 12, 175))
    blur_bg = Image.alpha_composite(blur_bg.convert("RGBA"), dark_bg_overlay)
    
    canvas.paste(blur_bg, (0, 0))
    
    # Paste photo centered vertically & horizontally
    photo_x = (W - new_w) // 2
    photo_y = int(H * 0.13)
    canvas.paste(photo_resized, (photo_x, photo_y))
    
    # Overlay for gradients, borders, and text
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw_overlay = ImageDraw.Draw(overlay)
    
    # Top Dark Gradient
    top_h = int(H * 0.23)
    for y in range(top_h):
        alpha = int(235 * (1.0 - (y / top_h)**1.2))
        draw_overlay.line([(0, y), (W, y)], fill=(12, 12, 12, alpha))
        
    # Bottom Dark Gradient
    bottom_h = int(H * 0.26)
    start_y = H - bottom_h
    for y in range(start_y, H):
        prog = (y - start_y) / bottom_h
        alpha = int(245 * (prog**0.75))
        draw_overlay.line([(0, y), (W, y)], fill=(12, 12, 12, alpha))
        
    # Gold Filigree Border
    border_margin = 32
    gold_color = (201, 169, 110, 240) if mode == "gala" else (246, 92, 122, 240)
    draw_overlay.rectangle([border_margin, border_margin, W - border_margin, H - border_margin], outline=gold_color, width=4)
    
    # Inner hairline frame
    draw_overlay.rectangle([border_margin + 8, border_margin + 8, W - border_margin - 8, H - border_margin - 8], outline=(201, 169, 110, 110), width=1)
    
    # Corner Accents (Gold Ticks)
    corner_size = 14
    corners = [
        (border_margin, border_margin),
        (W - border_margin, border_margin),
        (border_margin, H - border_margin),
        (W - border_margin, H - border_margin)
    ]
    for cx, cy in corners:
        draw_overlay.rectangle([cx - corner_size//2, cy - corner_size//2, cx + corner_size//2, cy + corner_size//2], fill=(201, 169, 110, 255))

    # Composite overlay
    canvas = Image.alpha_composite(canvas, overlay)
    draw = ImageDraw.Draw(canvas)
    
    # Load Fonts
    font_dir = r"C:\Windows\Fonts"
    try:
        font_hook = ImageFont.truetype(os.path.join(font_dir, "georgiab.ttf"), 38)
        font_sub = ImageFont.truetype(os.path.join(font_dir, "georgiai.ttf"), 34)
        font_name = ImageFont.truetype(os.path.join(font_dir, "georgiab.ttf"), 62)
        font_brand = ImageFont.truetype(os.path.join(font_dir, "segoeuib.ttf"), 28)
        font_small = ImageFont.truetype(os.path.join(font_dir, "segoeui.ttf"), 22)
    except:
        font_hook = font_sub = font_name = font_brand = font_small = ImageFont.load_default()
        
    # Add Logo on top center
    if os.path.exists(logo_path):
        logo_raw = Image.open(logo_path).convert("RGBA")
        logo_size = 85
        logo_scaled = logo_raw.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
        
        # Round backing
        backing = Image.new("RGBA", (105, 105), (0, 0, 0, 0))
        b_draw = ImageDraw.Draw(backing)
        b_draw.ellipse([0, 0, 105, 105], fill=(255, 255, 255, 245), outline=gold_color, width=3)
        backing.paste(logo_scaled, (10, 10), logo_scaled)
        
        canvas.paste(backing, (W // 2 - 52, 48), backing)
        top_text_y = 168
    else:
        top_text_y = 65

    # Top Brand Header
    draw.text((W//2, top_text_y), "PRIMAVERA EVENTS GROUP®", font=font_brand, fill=(255, 255, 255, 255), anchor="mm")
    draw.line([(W//2 - 170, top_text_y + 20), (W//2 + 170, top_text_y + 20)], fill=gold_color, width=2)

    # High Impact TikTok Hook Header
    hook_bg_y = top_text_y + 52
    if mode == "gala":
        hook_text = "• LOS 3 AÑOS DE JOSÉ GABRIEL •"
        tag_text = "— FIESTA DE GALA & BAUTIZO —"
    else:
        hook_text = "• FIESTA INFANTIL DE GALA •"
        tag_text = "— CUMPLEAÑOS #3 JOSÉ GABRIEL —"

    draw.text((W//2, hook_bg_y + 10), hook_text, font=font_hook, fill=(201, 169, 110) if mode=="gala" else (255, 255, 255), anchor="mm")

    # Bottom Title & Branding Block
    bottom_y = H - 230
    
    # Red/Pink Accent Badge
    draw.text((W//2, bottom_y - 60), tag_text, font=font_sub, fill=(246, 92, 122) if mode=="gala" else (201, 169, 110), anchor="mm")
    
    # Main Headline
    draw.text((W//2, bottom_y), "JOSÉ GABRIEL", font=font_name, fill=(255, 255, 255), anchor="mm")
    draw.text((W//2, bottom_y + 54), "« MI TERCER AÑITO »", font=font_sub, fill=(201, 169, 110), anchor="mm")
    
    # Subtitle / Footer
    draw.text((W//2, bottom_y + 105), "Organización Integral & Banquete de Gala | Cuernavaca, Morelos", font=font_small, fill=(220, 220, 220), anchor="mm")
    draw.text((W//2, bottom_y + 135), "www.primaveraeventsgroup.com · Tel/WA: +52 777 458 7923", font=font_small, fill=(180, 180, 180), anchor="mm")

    return canvas.convert("RGB")

if __name__ == '__main__':
    base_img = Image.open(input_image_path)
    
    # Option 1: Gala Luxury TikTok Cover
    cov1 = create_tiktok_cover(base_img, mode="gala")
    cov1.save(out_option1_downloads, quality=95)
    cov1.save(out_option1_brain, quality=95)
    cov1.save(out_option1_art, quality=95)
    print(f"Generated Option 1 Gala Cover at: {out_option1_downloads}")
    
    # Option 2: Vibrant Celebration TikTok Cover
    cov2 = create_tiktok_cover(base_img, mode="vibrant")
    cov2.save(out_option2_downloads, quality=95)
    cov2.save(out_option2_brain, quality=95)
    cov2.save(out_option2_art, quality=95)
    print(f"Generated Option 2 Vibrant Cover at: {out_option2_downloads}")
