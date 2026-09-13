import os
from PIL import Image

paths = {
    "clasico": r"C:\Users\Lenovo\.gemini\antigravity\brain\2a465b7c-538b-40b3-8943-c29e5c6f6bdb\media__1783174544740.png",
    "premium": r"C:\Users\Lenovo\.gemini\antigravity\brain\2a465b7c-538b-40b3-8943-c29e5c6f6bdb\media__1783174544748.jpg"
}

for name, path in paths.items():
    img = Image.open(path)
    bg_color = (254, 254, 254) if name == "clasico" else (6, 6, 6)
    width, height = img.size
    
    # Let's find non-background pixels at the top (Y=[0, 300])
    top_pixels = []
    for x in range(width):
        for y in range(300):
            px = img.getpixel((x, y))
            is_bg = True
            for c_val, bg_val in zip(px[:3], bg_color):
                if abs(c_val - bg_val) > 15:
                    is_bg = False
                    break
            if not is_bg:
                top_pixels.append((x, y))
                
    # Let's find non-background pixels at the bottom (Y=[750, 1024])
    bottom_pixels = []
    for x in range(width):
        for y in range(750, height):
            px = img.getpixel((x, y))
            is_bg = True
            for c_val, bg_val in zip(px[:3], bg_color):
                if abs(c_val - bg_val) > 15:
                    is_bg = False
                    break
            if not is_bg:
                bottom_pixels.append((x, y))
                
    print(f"\n--- {name.upper()} ---")
    if top_pixels:
        txs = [p[0] for p in top_pixels]
        tys = [p[1] for p in top_pixels]
        print(f"Top graphics bounds: X=[{min(txs)}, {max(txs)}], Y=[{min(tys)}, {max(tys)}]")
    else:
        print("No top graphics found.")
        
    if bottom_pixels:
        bxs = [p[0] for p in bottom_pixels]
        bys = [p[1] for p in bottom_pixels]
        print(f"Bottom graphics bounds: X=[{min(bxs)}, {max(bxs)}], Y=[{min(bys)}, {max(bys)}]")
    else:
        print("No bottom graphics found.")
