import os

clones_path = os.path.join(os.path.dirname(__file__), 'clones')
dirs = os.listdir(clones_path)

for d in dirs:
    dir_path = os.path.join(clones_path, d)
    if not os.path.isdir(dir_path):
        continue
        
    print(f"\n========================================")
    print(f"REPO: {d}")
    print(f"========================================")
    
    for root, subdirs, files in os.walk(dir_path):
        if '.git' in subdirs:
            subdirs.remove('.git')
        for f in files:
            full_path = os.path.join(root, f)
            rel_path = os.path.relpath(full_path, dir_path)
            size_kb = os.path.getsize(full_path) / 1024
            print(f"- {rel_path} ({size_kb:.2f} KB)")
