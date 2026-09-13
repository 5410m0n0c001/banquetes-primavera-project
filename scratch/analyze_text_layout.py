import numpy as np
from PIL import Image

img = Image.open(r"reconocimientos\re.png").convert('RGB')
arr = np.array(img)
h, w, _ = arr.shape

# Let's crop to middle columns (from 25% to 75% of width)
col_start = int(w * 0.25)
col_end = int(w * 0.75)
mid_cols = arr[:, col_start:col_end]

# Background color is around [247, 232, 239] or [245, 238, 242]
# Let's define background threshold
bg_mask = (mid_cols[:, :, 0] > 240) & (mid_cols[:, :, 1] > 220) & (mid_cols[:, :, 2] > 220)
non_bg_mask = ~bg_mask

# For each row, calculate percentage of non-background pixels in the middle column range
row_non_bg_pct = np.mean(non_bg_mask, axis=1) * 100

print(f"Analyzing middle columns (from X={col_start} to {col_end}):")
print("Text/Graphics bands in middle columns:")
in_text = False
start_y = 0
for y in range(0, h, 2):
    pct = row_non_bg_pct[y]
    is_text = pct > 1.5  # lower threshold since it's cropped
    if is_text and not in_text:
        start_y = y
        in_text = True
    elif not is_text and in_text:
        end_y = y - 1
        print(f"  Text/Graphics band: Y={start_y} to {end_y} (height={end_y-start_y+1}, avg pct={np.mean(row_non_bg_pct[start_y:end_y+1]):.1f}%)")
        in_text = False
if in_text:
    end_y = h - 1
    print(f"  Text/Graphics band: Y={start_y} to {end_y} (height={end_y-start_y+1}, avg pct={np.mean(row_non_bg_pct[start_y:end_y+1]):.1f}%)")

# Find blank bands in the middle y-range (Y=400 to Y=1000)
print("\nBlank bands (candidate spots for name overlay) between Y=400 and Y=1000:")
in_blank = False
start_y = 0
for y in range(400, 1000):
    pct = row_non_bg_pct[y]
    is_blank = pct <= 1.5
    if is_blank and not in_blank:
        start_y = y
        in_blank = True
    elif not is_blank and in_blank:
        end_y = y - 1
        if end_y - start_y > 20:
            print(f"  Blank band: Y={start_y} to {end_y} (height={end_y-start_y+1}, avg pct={np.mean(row_non_bg_pct[start_y:end_y+1]):.1f}%)")
        in_blank = False
if in_blank:
    end_y = 999
    if end_y - start_y > 20:
        print(f"  Blank band: Y={start_y} to {end_y} (height={end_y-start_y+1}, avg pct={np.mean(row_non_bg_pct[start_y:end_y+1]):.1f}%)")
