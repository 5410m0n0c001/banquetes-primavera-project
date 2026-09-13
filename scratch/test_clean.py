import json
import re
import html
import os

def clean_html(html_str):
    if not html_str:
        return ""
    
    # Strip headers, style, script, svg
    html_str = re.sub(r'<head[\s\S]*?</head>', '', html_str, flags=re.IGNORECASE)
    html_str = re.sub(r'<style[\s\S]*?</style>', '', html_str, flags=re.IGNORECASE)
    html_str = re.sub(r'<script[\s\S]*?</script>', '', html_str, flags=re.IGNORECASE)
    html_str = re.sub(r'<svg[\s\S]*?</svg>', '', html_str, flags=re.IGNORECASE)
    
    # Strip Divi shortcodes [et_pb_...]
    html_str = re.sub(r'\[/?et_pb_[^\]]*\]', '', html_str)
    # Strip any other shortcodes
    html_str = re.sub(r'\[/?\w+[^\]]*\]', '', html_str)
    
    # Convert tables to markdown tables
    def table_repl(match):
        table_html = match.group(0)
        trs = re.findall(r'<tr[\s\S]*?>([\s\S]*?)</tr>', table_html, flags=re.IGNORECASE)
        rows = []
        for tr in trs:
            tds = re.findall(r'<(td|th)[\s\S]*?>([\s\S]*?)</\1>', tr, flags=re.IGNORECASE)
            row = []
            for td_tag, td_content in tds:
                cell_text = re.sub(r'<[\s\S]*?>', '', td_content).strip()
                cell_text = re.sub(r'\s+', ' ', cell_text)
                row.append(cell_text)
            if row:
                rows.append(row)
        if not rows:
            return ""
        md_table = "\n"
        for i, row in enumerate(rows):
            md_table += "| " + " | ".join(row) + " |\n"
            if i == 0:
                md_table += "| " + " | ".join(["---"] * len(row)) + " |\n"
        md_table += "\n"
        return md_table
        
    html_str = re.sub(r'<table[\s\S]*?>[\s\S]*?</table>', table_repl, html_str, flags=re.IGNORECASE)
    
    # Convert headings
    html_str = re.sub(r'<h[1-6][\s\S]*?>([\s\S]*?)</h[1-6]>', lambda m: f"\n\n### {re.sub(r'<[\s\S]*?>', '', m.group(1)).strip()}\n\n", html_str, flags=re.IGNORECASE)
    
    # Convert paragraphs
    html_str = re.sub(r'<p[\s\S]*?>([\s\S]*?)</p>', lambda m: f"\n{re.sub(r'<[\s\S]*?>', '', m.group(1)).strip()}\n", html_str, flags=re.IGNORECASE)
    
    # Convert lists
    html_str = re.sub(r'<li[\s\S]*?>([\s\S]*?)</li>', lambda m: f"\n- {re.sub(r'<[\s\S]*?>', '', m.group(1)).strip()}\n", html_str, flags=re.IGNORECASE)
    
    # Strip any remaining tags
    html_str = re.sub(r'<[\s\S]*?>', '', html_str)
    
    # Unescape HTML entities
    html_str = html.unescape(html_str)
    
    # Normalize spacing and newlines
    html_str = re.sub(r'\n\s*\n\s*\n+', '\n\n', html_str)
    html_str = re.sub(r'[ \t]+', ' ', html_str)
    
    return html_str.strip()

def extract_prices(text):
    pattern = r'\$\s*\d{1,3}(?:,\d{3})*(?:\.\d{2})?(?:\s*(?:MXN|p/p|por persona))?'
    prices = re.findall(pattern, text, re.IGNORECASE)
    seen = set()
    deduped = []
    for p in prices:
        p_clean = re.sub(r'\s+', ' ', p).strip()
        if p_clean not in seen:
            seen.add(p_clean)
            deduped.append(p_clean)
    return deduped

def main():
    base_dir = r"C:\Users\Lenovo\Documents\primavera brain"
    pages_path = os.path.join(base_dir, "scratch", "wp_pages.json")
    
    with open(pages_path, 'r', encoding='utf-8') as f:
        pages = json.load(f)
        
    print(f"Total pages: {len(pages)}")
    # Clean the first page
    p = pages[0]
    print(f"Title: {p['title']['rendered']}")
    print(f"URL: {p['link']}")
    
    cleaned = clean_html(p['content']['rendered'])
    print("\n--- Cleaned Text (First 300 chars) ---")
    print(cleaned[:300])
    
    prices = extract_prices(cleaned)
    print("\n--- Prices Found ---")
    print(prices)

if __name__ == "__main__":
    main()
