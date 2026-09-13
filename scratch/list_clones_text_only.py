import os

clones_path = os.path.join(os.path.dirname(__file__), 'clones')
dirs = os.listdir(clones_path)

allowed_exts = {'.html', '.json', '.md', '.js', '.css', '.txt', '.xml', '.svg'}

for d in sorted(dirs):
    dir_path = os.path.join(clones_path, d)
    if not os.path.isdir(dir_path):
        continue
        
    print(f"\nREPO: {d}")
    
    files_found = []
    for root, subdirs, files in os.walk(dir_path):
        if '.git' in subdirs:
            subdirs.remove('.git')
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            if ext in allowed_exts:
                full_path = os.path.join(root, f)
                rel_path = os.path.relpath(full_path, dir_path)
                size_kb = os.path.getsize(full_path) / 1024
                files_found.append(f"- {rel_path} ({size_kb:.2f} KB)")
                
    if files_found:
        for f in files_found:
            print(f)
    else:
        print("- (No text/code files found)")
