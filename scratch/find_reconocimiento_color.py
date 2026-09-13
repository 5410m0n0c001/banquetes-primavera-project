import numpy as np
from PIL import Image

def find_color_pixels(img_path, target_color, tolerance=20):
    img = Image.open(img_path).convert('RGB')
    arr = np.array(img)
    
    # Calculate absolute distance in RGB space
    dist = np.linalg.norm(arr - target_color, axis=2)
    mask = dist < tolerance
    
    y_indices, x_indices = np.where(mask)
    if len(y_indices) > 0:
        print(f"\nFor {img_path}:")
        print(f"  Found {len(y_indices)} pixels matching color {target_color} (tolerance {tolerance})")
        print(f"  X range: {np.min(x_indices)} to {np.max(x_indices)} (center: {np.mean(x_indices):.1f})")
        print(f"  Y range: {np.min(y_indices)} to {np.max(y_indices)} (center: {np.mean(y_indices):.1f})")
    else:
        print(f"\nFor {img_path}: color {target_color} not found.")

target = [200, 56, 101]
find_color_pixels(r"reconocimientos\rq.png", target)
find_color_pixels(r"reconocimientos\rch.png", target)
find_color_pixels(r"reconocimientos\re.png", target)

# Let's also look for other potential text colors (like gold, navy blue, black, or dark grey) in re.png
# Let's count the most common colors in the middle of re.png
img_re = Image.open(r"reconocimientos\re.png").convert('RGB')
arr_re = np.array(img_re)
# Sample a central region
h, w, _ = arr_re.shape
mid_region = arr_re[int(h*0.3):int(h*0.7), int(w*0.2):int(w*0.8)]
pixels = mid_region.reshape(-1, 3)
# Find unique colors and their counts
unique_colors, counts = np.unique(pixels, axis=0, return_counts=True)
# Sort by count descending
sorted_idx = np.argsort(-counts)
print("\nMost common colors in the middle of re.png:")
for idx in sorted_idx[:10]:
    print(f"  Color {unique_colors[idx]}: count={counts[idx]}")
