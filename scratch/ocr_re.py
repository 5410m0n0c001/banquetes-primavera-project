try:
    import pytesseract
    from PIL import Image
    
    img = Image.open(r"c:\Users\Lenovo\Documents\primavera brain\reconocimientos\re.png")
    # Tesseract OCR
    # Note: under Windows, tesseract needs to be installed, let's see if we can run it.
    text = pytesseract.image_to_string(img)
    print("OCR Text:\n", text)
except Exception as e:
    print("Error:", e)
