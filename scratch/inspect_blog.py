import os
import json

base_dir = r"C:\Users\Lenovo\Documents\primavera brain"
json_path = os.path.join(base_dir, "base_de_datos_primavera.json")

if os.path.exists(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        db = json.load(f)
    print("Entries in 'entradas_blog':")
    blog = db.get("entradas_blog", [])
    for post in blog:
        print(f"- Titulo: {post.get('titulo') or post.get('name')}")
        print(f"  URL: {post.get('url') or post.get('link')}")
        print(f"  Keys: {list(post.keys())}")
else:
    print("Database not found!")
