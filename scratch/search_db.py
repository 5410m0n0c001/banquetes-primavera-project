import json

with open("base_de_datos_primavera.json", "r", encoding="utf-8") as f:
    db = json.load(f)

print("Top-level keys in database:", list(db.keys()))
if "expositores" in db:
    print("Found 'expositores' key! Length:", len(db["expositores"]))
    print("First 3 expositores:", db["expositores"][:3])
elif "providers" in db:
    print("Found 'providers' key! Length:", len(db["providers"]))
    print("First 3 providers:", db["providers"][:3])
else:
    for key in db.keys():
        if isinstance(db[key], list) and len(db[key]) > 0:
            print(f"Key '{key}' is a list of length {len(db[key])}")
            print("First item:", db[key][0])
