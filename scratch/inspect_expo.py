import os
import re
import sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

expo_path = "C:\\Users\\Lenovo\\Documents\\primavera brain\\scratch\\clones\\expo-boda-y-15-a-os"

def inspect_file(filename, title_only=False):
    filepath = os.path.join(expo_path, filename)
    if not os.path.exists(filepath):
        print(f"{filename}: NOT FOUND")
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    title = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
    title_str = title.group(1).strip() if title else "No Title"
    
    print(f"\nFILE: {filename} | Title: {title_str} | Size: {len(content)/1024:.2f} KB")
    if not title_only:
        text = re.sub(r'<script.*?>.*?</script>', '', content, flags=re.IGNORECASE | re.DOTALL)
        text = re.sub(r'<style.*?>.*?</style>', '', text, flags=re.IGNORECASE | re.DOTALL)
        text = re.sub(r'<.*?>', ' ', text)
        text = re.sub(r'\s+', ' ', text).strip()
        print(f"Snippet: {text[:600]}...")

# Inspect some critical files
inspect_file("index.html")
inspect_file("plan-marketing.html")
inspect_file("manual.html", title_only=True)
inspect_file("directorio.html")
inspect_file("cronograma.html")
inspect_file("vendedores.html", title_only=True)

# Let's inspect js/leads-data.js to see if there are leads in it
leads_file = os.path.join(expo_path, "js", "leads-data.js")
if os.path.exists(leads_file):
    with open(leads_file, 'r', encoding='utf-8') as f:
        js_content = f.read()
    print(f"\nFILE: js/leads-data.js | Size: {len(js_content)/1024:.2f} KB")
    print(f"Snippet:\n{js_content[:800]}")
