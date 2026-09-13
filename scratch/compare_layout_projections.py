import numpy as np
from PIL import Image

def get_row_pct(img_path):
    img = Image.open(img_path).convert('L') # convert to grayscale
    # Resize to exactly 1080x1456 to compare side-by-side
    img_res = img.resize((1080, 1456))
    arr_res = np.array(img_res)
    center_strip = arr_res[:, 200:880] # wider strip to catch text
    # Text is dark, background is light. Let's count pixels with grayscale value < 150
    is_text = center_strip < 150
    return np.mean(is_text, axis=1) * 100

pct_re = get_row_pct(r"reconocimientos\re.png")
pct_rq = get_row_pct(r"reconocimientos\rq.png")
pct_rch = get_row_pct(r"reconocimientos\rch.png")

print(f"{'Y':5s} | {'re.png':10s} | {'rq.png':10s} | {'rch.png':10s}")
print("-" * 45)
for y in range(300, 900, 20):
    val_re = np.mean(pct_re[y:y+20])
    val_rq = np.mean(pct_rq[y:y+20])
    val_rch = np.mean(pct_rch[y:y+20])
    print(f"{y:5d} | {val_re:9.1f}% | {val_rq:9.1f}% | {val_rch:9.1f}%")
