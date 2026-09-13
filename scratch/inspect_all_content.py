import os
import re

clones_path = "C:\\Users\\Lenovo\\Documents\\primavera brain\\scratch\\clones"

def inspect_html(filepath, repo_name):
    if not os.path.exists(filepath):
        print(f"{repo_name}: FILE NOT FOUND")
        return
        
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
        
    # Get Title
    title = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE | re.DOTALL)
    title_str = title.group(1).strip() if title else "No Title"
    
    # Get Body text snippets or key sections
    body_text = re.sub(r'<script.*?>.*?</script>', '', html, flags=re.IGNORECASE | re.DOTALL)
    body_text = re.sub(r'<style.*?>.*?</style>', '', body_text, flags=re.IGNORECASE | re.DOTALL)
    body_text = re.sub(r'<.*?>', ' ', body_text)
    body_text = re.sub(r'\s+', ' ', body_text).strip()
    
    print(f"\n========================================")
    print(f"REPO: {repo_name} | Title: {title_str}")
    print(f"Size: {len(html)/1024:.2f} KB")
    print(f"Snippet: {body_text[:500]}...")
    
    # Search for potential prices
    prices = re.findall(r'\$\s*\d{1,3}(?:,\d{3})*(?:\.\d{2})?', html)
    print(f"Potential prices: {list(set(prices))[:10]}")

# Let's inspect index.html for cotizaciones and venues
inspect_html(os.path.join(clones_path, "antonio-cotizacion", "index.html"), "antonio-cotizacion")
inspect_html(os.path.join(clones_path, "viviana-cotizaci-n-", "index.html"), "viviana-cotizaci-n-")
inspect_html(os.path.join(clones_path, "cotizaci-n-DIF", "index.html"), "cotizaci-n-DIF")
inspect_html(os.path.join(clones_path, "cotizaci-n-edie", "index.html"), "cotizaci-n-edie")
inspect_html(os.path.join(clones_path, "-Sra.-Sandra-cotizaci-n", "index.html"), "-Sra.-Sandra-cotizaci-n")
inspect_html(os.path.join(clones_path, "cotizacion-viky-solaire", "index.html"), "cotizacion-viky-solaire")
