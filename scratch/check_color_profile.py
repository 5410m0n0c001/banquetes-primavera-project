import numpy as np
from PIL import Image

img = Image.open(r"c:\Users\Lenovo\Documents\primavera brain\reconocimientos\re.png")
gray = img.convert('L')
arr = np.array(gray)

# We check middle y-range (500 to 900)
# We calculate variance of each column across this y-range
col_vars = np.var(arr[500:900, :], axis=0)

# If it is centered, we expect the variance to be symmetric, or have a uniform region in the middle
print("Middle rows column variance (sampled every 50 pixels):")
for x in range(0, 1080, 50):
    val = np.mean(col_vars[x:x+50]) if x+50 <= 1080 else np.mean(col_vars[x:])
    print(f"Col {x}-{x+50 if x+50<=1080 else 1080}: var={val:.1f}")
