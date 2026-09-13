import os
import json

base_dir = r"C:\Users\Lenovo\Documents\primavera brain"
json_path = os.path.join(base_dir, "base_de_datos_primavera.json")

if os.path.exists(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        db = json.load(f)
    print("Database Keys:")
    for key in db.keys():
        val = db[key]
        if isinstance(val, list):
            print(f"- {key}: list of {len(val)} items")
        elif isinstance(val, dict):
            print(f"- {key}: dict with {len(val)} keys")
        else:
            print(f"- {key}: {type(val).__name__}")
else:
    print("Database file not found!")
