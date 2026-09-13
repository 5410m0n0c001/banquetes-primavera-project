import numpy as np
from PIL import Image

img = Image.open(r"c:\Users\Lenovo\Documents\primavera brain\reconocimientos\re.png")
# Convert to grayscale
gray = img.convert('L')
arr = np.array(gray)

# We want to find rows that have very low variance (i.e. uniform background)
row_vars = np.var(arr, axis=1)
row_means = np.mean(arr, axis=1)

print("Image size:", img.size)
print("Row variance stats: min =", np.min(row_vars), "max =", np.max(row_vars), "mean =", np.mean(row_vars))

# Let's print out segments where variance is low (indicating empty space)
# We look for contiguous bands of low variance
threshold = 200.0  # arbitrary threshold for "uniform" row
uniform_rows = row_vars < threshold

print("\nUniform bands (background):")
in_band = False
start = 0
for y, is_uniform in enumerate(uniform_rows):
    if is_uniform and not in_band:
        start = y
        in_band = True
    elif not is_uniform and in_band:
        end = y - 1
        if end - start > 10:  # only bands thicker than 10 pixels
            print(f"y: {start} to {end} (height: {end-start+1}) - mean color: {np.mean(row_means[start:end+1]):.1f}")
        in_band = False
if in_band:
    end = len(uniform_rows) - 1
    if end - start > 10:
        print(f"y: {start} to {end} (height: {end-start+1}) - mean color: {np.mean(row_means[start:end+1]):.1f}")
