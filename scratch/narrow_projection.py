import numpy as np
from PIL import Image

img = Image.open(r"reconocimientos\re.png").convert('RGB')
arr = np.array(img)
h, w, _ = arr.shape

# We look at a narrow center column (from X=450 to X=630)
col_start = 450
col_end = 630
center_strip = arr[:, col_start:col_end]

# Background color is beige [247, 233, 240]
# We calculate distance from background color
bg_color = np.array([247, 233, 240])
dist_to_bg = np.linalg.norm(center_strip - bg_color, axis=2)
# If distance > 10, it's non-background (text)
is_text = dist_to_bg > 15

# Row-wise percentage of text
row_text_pct = np.mean(is_text, axis=1) * 100

print(f"Narrow center strip analysis (X={col_start} to {col_end}):")
for y in range(0, h, 10):
    pct = np.mean(row_text_pct[y:y+10])
    if pct > 1.0:
        print(f"Y={y:4d} to {y+9:4d}: text/graphics presence = {pct:.1f}%")
