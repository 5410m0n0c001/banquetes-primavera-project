import urllib.request
import json
import os

def fetch_api(url):
    print(f"Fetching: {url}")
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    )
    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                return json.loads(response.read().decode('utf-8'))
    except Exception as e:
        print(f"Error fetching {url}: {e}")
    return None

def main():
    pages_url = "https://primaveraeventsgroup.com/wp-json/wp/v2/pages?per_page=100"
    posts_url = "https://primaveraeventsgroup.com/wp-json/wp/v2/posts?per_page=100"
    
    pages = fetch_api(pages_url)
    posts = fetch_api(posts_url)
    
    output_dir = r"C:\Users\Lenovo\Documents\primavera brain\scratch"
    os.makedirs(output_dir, exist_ok=True)
    
    if pages:
        print(f"Successfully fetched {len(pages)} pages.")
        with open(os.path.join(output_dir, "wp_pages.json"), "w", encoding="utf-8") as f:
            json.dump(pages, f, indent=2, ensure_ascii=False)
    else:
        print("Failed to fetch pages via public REST API.")
        
    if posts:
        print(f"Successfully fetched {len(posts)} posts.")
        with open(os.path.join(output_dir, "wp_posts.json"), "w", encoding="utf-8") as f:
            json.dump(posts, f, indent=2, ensure_ascii=False)
    else:
        print("Failed to fetch posts via public REST API.")

if __name__ == "__main__":
    main()
