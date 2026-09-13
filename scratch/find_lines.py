import numpy as np
from PIL import Image

img = Image.open(r"c:\Users\Lenovo\Documents\primavera brain\reconocimientos\re.png")
gray = img.convert('L')
arr = np.array(gray)

# Let's find rows where there's a strong horizontal line (e.g. a line of black/dark pixels)
# A line of black pixels would have a low mean value (dark) and low variance across the line (if it's a solid line)
# Or a line where a signature line is.
row_means = np.mean(arr, axis=1)
row_vars = np.var(arr, axis=1)

print("Top 10 darkest rows:")
dark_rows = np.argsort(row_means)[:20]
for r in dark_rows:
    print(f"Row {r}: mean={row_means[r]:.1f}, var={row_vars[r]:.1f}")
