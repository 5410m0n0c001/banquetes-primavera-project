import json
import os
import re

with open(r"scratch\roster_raw.json", "r", encoding="utf-8") as f:
    raw_data = json.load(f)

excel = raw_data["excel"]
logos = raw_data["logos"]
directory = raw_data["directory"]
activities = raw_data["activities"]

# Standard exclusions
exclusions = [
    "anet warneros",
    "anetth guarneros",
    "viajando con la musica",
    "viajando con la música",
    "vcm",
    "red",
    "redes"
]

def is_excluded(name):
    if not name:
        return True
    n_lower = name.lower()
    for ex in exclusions:
        if ex in n_lower or n_lower == ex:
            return True
    return False

# Roster database
roster = {}

# 1. Process Excel
for ex in excel:
    sheet = ex["sheet_name"]
    business = ex["business_name"]
    contact = ex["contact_name"]
    
    if is_excluded(sheet) or is_excluded(business) or is_excluded(contact):
        continue
        
    display = contact if contact else business
    key = business.lower()
    roster[key] = {
        "displayName": display,
        "entityName": business,
        "personName": contact,
        "logoPath": None,
        "sources": ["excel"]
    }

def find_match(name):
    if not name:
        return None
    name_l = name.lower()
    if name_l in roster:
        return name_l
    for k in roster.keys():
        if k in name_l or name_l in k:
            return k
    return None

# 2. Process Logos
for logo in logos:
    caption = logo["caption"]
    logo_path = logo["logo_path"]
    
    if is_excluded(caption):
        continue
        
    match_key = find_match(caption)
    if match_key:
        roster[match_key]["logoPath"] = logo_path
        if "logos" not in roster[match_key]["sources"]:
            roster[match_key]["sources"].append("logos")
    else:
        key = caption.lower()
        roster[key] = {
            "displayName": caption,
            "entityName": caption,
            "personName": "",
            "logoPath": logo_path,
            "sources": ["logos"]
        }

# 3. Process Directory
for item in directory:
    name = item["name"]
    if is_excluded(name):
        continue
        
    match_key = find_match(name)
    if match_key:
        if "directory" not in roster[match_key]["sources"]:
            roster[match_key]["sources"].append("directory")
    else:
        key = name.lower()
        roster[key] = {
            "displayName": name,
            "entityName": name,
            "personName": "",
            "logoPath": None,
            "sources": ["directory"]
        }

# 4. Process Activities
activity_participants = [
    {"name": "Saxofonista Solista", "match_target": "Saxofonista"},
    {"name": "Espectáculo de Marimba", "match_target": "Marimba"},
    {"name": "Banda Instrumental", "match_target": "Banda Instrumental"},
    {"name": "Grupo Bonanza", "match_target": "Grupo Bonanza"},
    {"name": "Banda Lago Negro", "match_target": "Banda Lago Negro"},
    {"name": "Paola (Academia JHANADE)", "match_target": "Paola"},
    {"name": "Academia de Baile Dance Queens", "match_target": "Dance Queens"},
    {"name": "Mariachi Xiuhtépetl", "match_target": "Mariachi Xiuhtépetl"}
]

for p in activity_participants:
    name = p["name"]
    target = p["match_target"]
    if is_excluded(name) or is_excluded(target):
        continue
        
    match_key = find_match(target)
    if match_key:
        if "activities" not in roster[match_key]["sources"]:
            roster[match_key]["sources"].append("activities")
    else:
        key = name.lower()
        roster[key] = {
            "displayName": name,
            "entityName": name,
            "personName": "",
            "logoPath": None,
            "sources": ["activities"]
        }

# Write summary to text file
final_list = list(roster.values())
with open(r"scratch\roster_consolidated.txt", "w", encoding="utf-8") as out:
    out.write("================ FINAL CONSOLIDATED ROSTER ================\n")
    out.write(f"Total Unique Certificates to Generate: {len(roster)}\n\n")
    for idx, entry in enumerate(final_list, 1):
        logo_status = f"Logo: {entry['logoPath']}" if entry['logoPath'] else "No Logo"
        out.write(f"{idx:2d}. Display Name: '{entry['displayName']}' | Entity: '{entry['entityName']}' | Person: '{entry['personName']}' | {logo_status} | Sources: {entry['sources']}\n")

# Save consolidated list as JSON
with open(r"scratch\consolidated_roster.json", "w", encoding="utf-8") as f:
    json.dump(final_list, f, indent=2, ensure_ascii=False)

print("roster consolidated and analyzed successfully.")
