import sys
try:
    import pandas as pd
    print("pandas: OK")
except ImportError as e:
    print(f"pandas: ERROR ({e})")

try:
    import openpyxl
    print("openpyxl: OK")
except ImportError as e:
    print(f"openpyxl: ERROR ({e})")

try:
    from PIL import Image, ImageDraw, ImageFont
    print("PIL: OK")
except ImportError as e:
    print(f"PIL: ERROR ({e})")

try:
    import reportlab
    print("reportlab: OK")
except ImportError as e:
    print(f"reportlab: ERROR ({e})")
