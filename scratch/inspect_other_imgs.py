from PIL import Image

for name in ['rq.png', 'rch.png']:
    try:
        img = Image.open(f"reconocimientos/{name}")
        print(f"{name}: format={img.format}, size={img.size}, mode={img.mode}")
    except Exception as e:
        print(f"Error {name}: {e}")
