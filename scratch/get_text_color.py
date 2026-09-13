from PIL import Image

path = r"C:\Users\Lenovo\.gemini\antigravity\brain\2a465b7c-538b-40b3-8943-c29e5c6f6bdb\scratch\test_mesa_2.png"
img = Image.open(path)

# Let's find the darkest pixel in the center box (X=[220, 510], Y=[350, 800])
darkest_color = (255, 255, 255)
darkest_val = 765 # sum of RGB

for x in range(220, 511):
    for y in range(350, 801):
        px = img.getpixel((x, y))
        val = sum(px[:3])
        if val < darkest_val:
            darkest_val = val
            darkest_color = px[:3]

print(f"Darkest color in text area (likely text color): {darkest_color}")
