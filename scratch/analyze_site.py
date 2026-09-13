import json
import os
import re

def main():
    base_dir = r"C:\Users\Lenovo\Documents\primavera brain"
    pages_path = os.path.join(base_dir, "scratch", "wp_pages.json")
    posts_path = os.path.join(base_dir, "scratch", "wp_posts.json")
    
    if not os.path.exists(pages_path) or not os.path.exists(posts_path):
        print("Scraped files not found!")
        return
        
    with open(pages_path, 'r', encoding='utf-8') as f:
        pages = json.load(f)
    with open(posts_path, 'r', encoding='utf-8') as f:
        posts = json.load(f)
        
    print("Site Optimization Analysis started...")
    
    report = {
        "summary": {
            "total_pages": len(pages),
            "total_posts": len(posts),
            "total_urls": len(pages) + len(posts)
        },
        "non_seo_urls": [],
        "thin_content_pages": [],
        "missing_seo_meta": [],
        "divi_bloat_pages": [],
        "pricing_findings": []
    }
    
    # 1. Analyze URLs/Slugs
    # Non-SEO URLs usually have patterns like number-number (e.g. 987509796-2)
    number_pattern = re.compile(r'\d{6,}-\d+')
    for item in pages + posts:
        slug = item.get("slug", "")
        url = item.get("link", "")
        title = item.get("title", {}).get("rendered", "")
        if number_pattern.search(slug) or "-" in slug and slug.replace("-", "").isdigit():
            report["non_seo_urls"].append({
                "title": title,
                "url": url,
                "slug": slug,
                "reason": "Contiene ID numérico genérico o duplicado generado por WordPress (posible error al guardar la página)"
            })
            
    # 2. Analyze Content Length (Thin Content)
    for item in pages + posts:
        url = item.get("link", "")
        title = item.get("title", {}).get("rendered", "")
        content = item.get("content", {}).get("rendered", "")
        
        # Strip html tags and shortcodes to get text count
        text = re.sub(r'<[\s\S]*?>', '', content)
        text = re.sub(r'\[/?\w+[^\]]*\]', '', text)
        text = re.sub(r'\s+', ' ', text).strip()
        
        word_count = len(text.split())
        if word_count < 15 and item.get("status") == "publish":
            report["thin_content_pages"].append({
                "title": title,
                "url": url,
                "word_count": word_count,
                "text_snippet": text[:100]
            })
            
    # 3. Analyze Yoast SEO Metadata
    for item in pages + posts:
        url = item.get("link", "")
        title = item.get("title", {}).get("rendered", "")
        yoast_json = item.get("yoast_head_json", {})
        
        meta_title = yoast_json.get("title", "")
        meta_desc = yoast_json.get("og_description", "") or yoast_json.get("twitter_description", "")
        
        issues = []
        if not meta_title:
            issues.append("Falta Meta Título SEO")
        if not meta_desc:
            issues.append("Falta Meta Descripción SEO (crítico para Google CTR)")
        elif len(meta_desc) < 80:
            issues.append(f"Meta Descripción demasiado corta ({len(meta_desc)} caracteres, ideal: 120-160)")
        elif len(meta_desc) > 200:
            issues.append(f"Meta Descripción demasiado larga ({len(meta_desc)} caracteres, ideal: 120-160)")
            
        if issues:
            report["missing_seo_meta"].append({
                "title": title,
                "url": url,
                "issues": issues,
                "current_desc": meta_desc[:60] + "..." if meta_desc else "Vacío"
            })
            
    # 4. Analyze Divi Bloat
    for item in pages:
        url = item.get("link", "")
        title = item.get("title", {}).get("rendered", "")
        content = item.get("content", {}).get("rendered", "")
        
        # Count Divi shortcodes
        divi_codes = len(re.findall(r'\[et_pb_', content))
        if divi_codes > 30:
            report["divi_bloat_pages"].append({
                "title": title,
                "url": url,
                "shortcode_count": divi_codes,
                "html_size_kb": round(len(content) / 1024, 1)
            })
            
    # 5. Pricing patterns and potential issues
    price_pattern = re.compile(r'\$\s*\d{1,3}(?:,\d{3})*(?:\.\d{2})?')
    for item in pages:
        url = item.get("link", "")
        title = item.get("title", {}).get("rendered", "")
        content = item.get("content", {}).get("rendered", "")
        text = re.sub(r'<[\s\S]*?>', '', content)
        text = re.sub(r'\[/?\w+[^\]]*\]', '', text)
        
        prices = price_pattern.findall(text)
        if prices:
            # Check if package page
            slug_lower = item.get("slug", "").lower()
            if "paquete" in slug_lower:
                report["pricing_findings"].append({
                    "title": title,
                    "url": url,
                    "prices_found": list(set(prices))
                })
                
    # Save report JSON
    with open(os.path.join(base_dir, "scratch", "site_audit_report.json"), "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print("Optimization analysis complete. Saved scratch/site_audit_report.json")

if __name__ == "__main__":
    main()
