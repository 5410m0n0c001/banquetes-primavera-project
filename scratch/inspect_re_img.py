from PIL import Image
try:
    img = Image.open(r"c:\Users\Lenovo\Documents\primavera brain\reconocimientos\re.png")
    print("re.png format:", img.format)
    print("re.png size:", img.size)
    print("re.png mode:", img.mode)
except Exception as e:
    print("Error:", e)
