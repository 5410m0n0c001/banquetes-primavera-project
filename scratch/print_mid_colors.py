import numpy as np
from PIL import Image

img = Image.open(r"reconocimientos\re.png").convert('RGB')
arr = np.array(img)
h, w, _ = arr.shape

print(f"Image size: {w}x{h}")
print("Colors down the middle column (X = 540) every 50 pixels:")
for y in range(0, h, 50):
    print(f"Y={y:4d}: {arr[y, 540]}")
