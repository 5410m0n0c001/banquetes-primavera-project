import re

html_path = r"C:\Users\Lenovo\AppData\Local\Temp\claude\C--Users-Lenovo-Documents-alexros-brain--claude-worktrees-sweet-lamarr-4a87c5\5ca18579-37a3-4846-91ca-842e6fecd613\scratchpad\carrusel_ig_venues.html"
out_path = r"C:\Users\Lenovo\Documents\primavera brain\scratch\carrusel_text.txt"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Remove style tags and base64
html = re.sub(r'<style.*?>.*?</style>', '', html, flags=re.DOTALL)
html = re.sub(r'data:image[^\s"]+', '', html)

text = re.sub(r'<[^>]+>', '\n', html)
lines = [l.strip() for l in text.splitlines() if l.strip() and len(l.strip()) < 300]

with open(out_path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print("Saved to", out_path)
