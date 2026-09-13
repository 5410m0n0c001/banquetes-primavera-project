from PIL import Image, ImageDraw, ImageFont

img = Image.open(r"reconocimientos\re.png").convert('RGB')
draw = ImageDraw.Draw(img)

w, h = img.size
font = ImageFont.load_default()

# Draw vertical lines
for x in range(0, w, 100):
    draw.line([(x, 0), (x, h)], fill=(255, 0, 0), width=1)
    draw.text((x + 5, 5), str(x), fill=(255, 0, 0), font=font)

# Draw horizontal lines
for y in range(0, h, 100):
    draw.line([(0, y), (w, y)], fill=(255, 0, 0), width=1)
    draw.text((5, y + 5), str(y), fill=(255, 0, 0), font=font)

# Draw minor lines every 50
for x in range(0, w, 50):
    if x % 100 != 0:
        draw.line([(x, 0), (x, h)], fill=(200, 200, 200), width=1)
for y in range(0, h, 50):
    if y % 100 != 0:
        draw.line([(0, y), (w, y)], fill=(200, 200, 200), width=1)

img.save(r"scratch\re_grid.png", "PNG")
print("re_grid.png saved in scratch folder.")
