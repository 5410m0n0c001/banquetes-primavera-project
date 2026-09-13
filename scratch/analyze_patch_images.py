import os
from PIL import Image

paths = {
    "media1": r"C:\Users\Lenovo\.gemini\antigravity\brain\2a465b7c-538b-40b3-8943-c29e5c6f6bdb\media__1782932415975.jpg",
    "media2": r"C:\Users\Lenovo\.gemini\antigravity\brain\2a465b7c-538b-40b3-8943-c29e5c6f6bdb\media__1782932416154.jpg"
}

for name, path in paths.items():
    if os.path.exists(path):
        img = Image.open(path)
        print(f"\nAnalyzing center of {name} ({img.size}):")
        cx, cy = img.size[0] // 2, img.size[1] // 2
        colors = set()
        for x in range(cx - 50, cx + 50):
            for y in range(cy - 50, cy + 50):
                colors.add(img.getpixel((x, y)))
        print(f"Number of unique colors in center box: {len(colors)}")
        sample = list(colors)[:10]
        print(f"Sample colors: {sample}")
