import numpy as np
from PIL import Image

try:
    img_re = Image.open(r"c:\Users\Lenovo\Documents\primavera brain\reconocimientos\re.png").convert('RGB')
    img_rq = Image.open(r"c:\Users\Lenovo\Documents\primavera brain\reconocimientos\rq.png").convert('RGB')
    img_rch = Image.open(r"c:\Users\Lenovo\Documents\primavera brain\reconocimientos\rch.png").convert('RGB')
    
    # Resize to match exactly
    img_re_res = img_re.resize((1080, 1456))
    img_rq_res = img_rq.resize((1080, 1456))
    img_rch_res = img_rch.resize((1080, 1456))
    
    arr_re = np.array(img_re_res, dtype=np.float32)
    arr_rq = np.array(img_rq_res, dtype=np.float32)
    arr_rch = np.array(img_rch_res, dtype=np.float32)
    
    diff_re_rq = np.mean(np.abs(arr_re - arr_rq))
    diff_re_rch = np.mean(np.abs(arr_re - arr_rch))
    diff_rq_rch = np.mean(np.abs(arr_rq - arr_rch))
    
    print(f"Mean absolute difference re vs rq: {diff_re_rq:.2f}")
    print(f"Mean absolute difference re vs rch: {diff_re_rch:.2f}")
    print(f"Mean absolute difference rq vs rch: {diff_rq_rch:.2f}")
    
except Exception as e:
    print("Error:", e)
