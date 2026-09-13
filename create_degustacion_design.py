import os
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# Paths
input_heic = r"C:\Users\Lenovo\Documents\degustacion 2.0\imagenes\IMG_3963.HEIC"
input_png = r"C:\Users\Lenovo\Documents\degustacion 2.0\imagenes\IMG_3963.png"
logo_path = r"c:\Users\Lenovo\Documents\primavera brain\assets\images\logo_principal_p.png"

output_dir_doc = r"C:\Users\Lenovo\Documents\degustacion 2.0\imagenes"
output_dir_art = r"C:\Users\Lenovo\.gemini\antigravity\brain\2662e14f-6269-4a71-8fa5-e4f99bece5d8"

out_4k_doc = os.path.join(output_dir_doc, "IMG_3963_degustacion_primavera_4k.png")
out_social_doc = os.path.join(output_dir_doc, "IMG_3963_degustacion_primavera_social.png")

out_4k_art = os.path.join(output_dir_art, "IMG_3963_degustacion_primavera_4k.png")
out_social_art = os.path.join(output_dir_art, "IMG_3963_degustacion_primavera_social.png")

def load_or_convert_base_image():
    if os.path.exists(input_png):
        return Image.open(input_png).convert("RGBA")
    elif os.path.exists(input_heic):
        import pillow_heif
        heif_file = pillow_heif.read_heif(input_heic)
        img = Image.frombytes(heif_file.mode, heif_file.size, heif_file.data, 'raw')
        img.save(input_png)
        return img.convert("RGBA")
    else:
        raise FileNotFoundError("Input image not found!")

def draw_text_with_shadow(draw, position, text, font, fill_color, shadow_color=(0, 0, 0, 210), offset=(3, 3), anchor=None):
    x, y = position
    sx, sy = offset
    if shadow_color:
        draw.text((x + sx, y + sy), text, font=font, fill=shadow_color, anchor=anchor)
    draw.text((x, y), text, font=font, fill=fill_color, anchor=anchor)

def create_design(base_img, target_width=1800):
    orig_w, orig_h = base_img.size
    aspect = orig_h / orig_w
    target_height = int(target_width * aspect)
    
    img = base_img.resize((target_width, target_height), Image.Resampling.LANCZOS)
    width, height = img.size
    
    # Overlay layer for gradients and frames
    overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw_overlay = ImageDraw.Draw(overlay)
    
    # 1. Top Gradient (Dark translucent fade for header legibility)
    top_gradient_h = int(height * 0.22)
    for y in range(top_gradient_h):
        alpha = int(220 * (1.0 - (y / top_gradient_h)**1.2))
        draw_overlay.line([(0, y), (width, y)], fill=(15, 15, 15, alpha))
        
    # 2. Bottom Gradient (Dark translucent fade for title & footer)
    bottom_gradient_h = int(height * 0.26)
    gradient_start_y = height - bottom_gradient_h
    for y in range(gradient_start_y, height):
        progress = (y - gradient_start_y) / bottom_gradient_h
        alpha = int(235 * (progress ** 0.75))
        draw_overlay.line([(0, y), (width, y)], fill=(15, 15, 15, alpha))
        
    # 3. Gold Filigree Border & Frame
    border_inset = int(width * 0.04)
    border_color = (201, 169, 110, 230) # Gold #C9A96E
    border_width = max(2, int(width * 0.0022))
    
    rect_box = [border_inset, border_inset, width - border_inset, height - border_inset]
    draw_overlay.rectangle(rect_box, outline=border_color, width=border_width)
    
    # Inner subtle line
    inner_inset = border_inset + int(width * 0.007)
    draw_overlay.rectangle([inner_inset, inner_inset, width - inner_inset, height - inner_inset], outline=(201, 169, 110, 110), width=1)
    
    # Corner Accents (Gold Diamonds/Ticks)
    corner_size = int(width * 0.014)
    corners = [
        (border_inset, border_inset),
        (width - border_inset, border_inset),
        (border_inset, height - border_inset),
        (width - border_inset, height - border_inset)
    ]
    for cx, cy in corners:
        draw_overlay.rectangle([cx - corner_size//2, cy - corner_size//2, cx + corner_size//2, cy + corner_size//2], fill=(201, 169, 110, 255))

    # Composite gradient layer onto image
    img = Image.alpha_composite(img, overlay)
    draw = ImageDraw.Draw(img)
    
    # 4. Fonts Setup
    font_dir = r"C:\Windows\Fonts"
    
    try:
        font_title = ImageFont.truetype(os.path.join(font_dir, "georgiai.ttf"), int(width * 0.062))
        font_slogan = ImageFont.truetype(os.path.join(font_dir, "georgiab.ttf"), int(width * 0.038))
        font_header = ImageFont.truetype(os.path.join(font_dir, "georgiab.ttf"), int(width * 0.034))
        font_sub = ImageFont.truetype(os.path.join(font_dir, "segoeui.ttf"), int(width * 0.021))
        font_small = ImageFont.truetype(os.path.join(font_dir, "segoeuil.ttf"), int(width * 0.017))
    except:
        font_title = ImageFont.load_default()
        font_slogan = font_title
        font_header = font_title
        font_sub = font_title
        font_small = font_title

    # 5. Logo Placement
    if os.path.exists(logo_path):
        logo_raw = Image.open(logo_path).convert("RGBA")
        logo_size = int(width * 0.085)
        logo_scaled = logo_raw.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
        
        # Backing circle with gold rim
        backing_margin = int(logo_size * 0.08)
        backing_size = logo_size + backing_margin * 2
        backing = Image.new("RGBA", (backing_size, backing_size), (0, 0, 0, 0))
        b_draw = ImageDraw.Draw(backing)
        b_draw.ellipse([0, 0, backing_size, backing_size], fill=(255, 255, 255, 245), outline=(201, 169, 110, 255), width=int(width * 0.003))
        
        backing.paste(logo_scaled, (backing_margin, backing_margin), logo_scaled)
        
        logo_x = (width - backing_size) // 2
        logo_y = border_inset + int(height * 0.015)
        img.paste(backing, (logo_x, logo_y), backing)
        
        header_y_start = logo_y + backing_size + int(height * 0.012)
    else:
        header_y_start = border_inset + int(height * 0.03)

    # 6. Top Header Typography
    draw_text_with_shadow(draw, (width // 2, header_y_start), "PRIMAVERA EVENTS GROUP®", font_header, fill_color=(255, 255, 255, 255), shadow_color=(0, 0, 0, 200), anchor="mm")
    
    # Gold divider line below header
    div_y = header_y_start + int(height * 0.02)
    div_w = int(width * 0.32)
    draw.line([(width//2 - div_w//2, div_y), (width//2 + div_w//2, div_y)], fill=(201, 169, 110, 255), width=max(1, int(width * 0.0015)))
    
    draw_text_with_shadow(draw, (width // 2, div_y + int(height * 0.016)), "EXPERIENCIAS GASTRONÓMICAS DE GALA", font_sub, fill_color=(201, 169, 110, 255), shadow_color=(0, 0, 0, 180), anchor="mm")

    # 7. Bottom Main Title & Sophisticated Wording
    bottom_center_y = height - int(height * 0.135)
    
    # Sub-tagline above title
    draw_text_with_shadow(draw, (width // 2, bottom_center_y - int(height * 0.062)), "— NUESTRAS CELEBRACIONES —", font_sub, fill_color=(246, 92, 122, 255), shadow_color=(0, 0, 0, 220), anchor="mm")
    
    # Main Headline Title: « Una Degustación Más »
    title_text = "« Una Degustación Más »"
    draw_text_with_shadow(draw, (width // 2, bottom_center_y - int(height * 0.02)), title_text, font_title, fill_color=(255, 255, 255, 255), shadow_color=(0, 0, 0, 240), offset=(3, 3), anchor="mm")
    
    # Subheadline: EL ARTE DE SERVIR · HECHO REALIDAD
    draw_text_with_shadow(draw, (width // 2, bottom_center_y + int(height * 0.03)), "EL ARTE DE SERVIR · HECHO REALIDAD", font_slogan, fill_color=(201, 169, 110, 255), shadow_color=(0, 0, 0, 220), anchor="mm")
    
    # Sub-details
    draw_text_with_shadow(draw, (width // 2, bottom_center_y + int(height * 0.065)), "Degustación de Menú de Gala & Montaje de Alta Gama en Morelos", font_sub, fill_color=(240, 240, 240, 255), shadow_color=(0, 0, 0, 200), anchor="mm")
    
    # Bottom Footer Line
    footer_y = height - border_inset - int(height * 0.018)
    draw_text_with_shadow(draw, (width // 2, footer_y), "www.primaveraeventsgroup.com  |  Tel / WhatsApp: +52 777 458 7923  |  Cuernavaca, Morelos", font_small, fill_color=(200, 200, 200, 220), shadow_color=(0, 0, 0, 180), anchor="mm")

    return img.convert("RGB")

if __name__ == '__main__':
    base_img = load_or_convert_base_image()
    
    # 1. Social Media / Standard Version (1800 px width)
    img_social = create_design(base_img, target_width=1800)
    img_social.save(out_social_doc, quality=95)
    img_social.save(out_social_art, quality=95)
    print(f"Generated Social design at: {out_social_doc}")
    
    # 2. Ultra 4K Version (3600 px width)
    img_4k = create_design(base_img, target_width=3600)
    img_4k.save(out_4k_doc, quality=95)
    img_4k.save(out_4k_art, quality=95)
    print(f"Generated 4K design at: {out_4k_doc}")
