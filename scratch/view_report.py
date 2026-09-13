import json
import os

def main():
    base_dir = r"C:\Users\Lenovo\Documents\primavera brain"
    report_path = os.path.join(base_dir, "scratch", "site_audit_report.json")
    
    with open(report_path, 'r', encoding='utf-8') as f:
        r = json.load(f)
        
    print(f"Total Pages: {r['summary']['total_pages']}")
    print(f"Total Posts: {r['summary']['total_posts']}")
    print(f"Non-SEO URLs Found: {len(r['non_seo_urls'])}")
    for item in r['non_seo_urls']:
        print(f"  - {item['title']}: {item['url']} ({item['slug']})")
        
    print(f"Thin Content Pages: {len(r['thin_content_pages'])}")
    for item in r['thin_content_pages'][:5]:
        print(f"  - {item['title']}: {item['word_count']} words")
        
    print(f"Missing/Incorrect SEO Meta Pages: {len(r['missing_seo_meta'])}")
    for item in r['missing_seo_meta'][:5]:
        print(f"  - {item['title']}: {item['issues']}")
        
    print(f"Divi Bloat Pages: {len(r['divi_bloat_pages'])}")
    for item in r['divi_bloat_pages'][:5]:
        print(f"  - {item['title']}: {item['shortcode_count']} shortcodes, {item['html_size_kb']} KB")

if __name__ == "__main__":
    main()
