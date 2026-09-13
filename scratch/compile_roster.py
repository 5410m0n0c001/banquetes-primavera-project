import json
import re
import os
import pandas as pd

# 1. Load from Excel
excel_path = r"C:\Users\Lenovo\Documents\expo expositores\PLANTILLA_FINAL_CORREGIDA.xlsx"
xls = pd.ExcelFile(excel_path)
excel_exhibitors = []
for sheet in xls.sheet_names:
    df = pd.read_excel(excel_path, sheet_name=sheet)
    profile_header = ""
    contact_name = ""
    for r_idx, row in df.iterrows():
        val0 = str(row.iloc[0]) if len(row) > 0 and pd.notna(row.iloc[0]) else ""
        if "PERFIL DEL EXPOSITOR" in val0.upper():
            profile_header = val0
        if "TITULAR" in val0.upper() or "CONTACTO" in val0.upper():
            if len(row) > 1 and pd.notna(row.iloc[1]):
                contact_name = str(row.iloc[1]).strip()
    if not contact_name:
        for r_idx, row in df.iterrows():
            for c_idx, val in enumerate(row):
                if pd.notna(val) and ("TITULAR" in str(val).upper() or "CONTACTO" in str(val).upper()):
                    if c_idx + 1 < len(row) and pd.notna(row.iloc[c_idx + 1]):
                        contact_name = str(row.iloc[c_idx + 1]).strip()
                        break
            if contact_name:
                break
    
    business_name = sheet
    if profile_header:
        m = re.search(r"PERFIL DEL EXPOSITOR:\s*(.*)", profile_header, re.IGNORECASE)
        if m:
            business_name = m.group(1).strip()
            
    excel_exhibitors.append({
        "source": "excel",
        "sheet_name": sheet,
        "business_name": business_name,
        "contact_name": contact_name
    })

# 2. Load from cronograma.js (logos)
cronograma_js_path = r"C:\Users\Lenovo\Documents\expo expositores\js\cronograma.js"
logo_images = []
if os.path.exists(cronograma_js_path):
    with open(cronograma_js_path, "r", encoding="utf-8") as f:
        content = f.read()
    matches = re.findall(r"\{\s*src:\s*['\"]([^'\"]+)['\"]\s*,\s*caption:\s*['\"]([^'\"]+)['\"]\s*\}", content)
    for src, caption in matches:
        logo_images.append({
            "source": "cronograma_js",
            "logo_path": src,
            "caption": caption
        })

# 3. Load from directorio.html
directorio_html_path = r"C:\Users\Lenovo\Documents\expo expositores\directorio.html"
directory_providers = []
if os.path.exists(directorio_html_path):
    with open(directorio_html_path, "r", encoding="utf-8") as f:
        content = f.read()
    matches = re.findall(r"data-name=\"([^\"]+)\"", content)
    for name in matches:
        directory_providers.append({
            "source": "directorio_html",
            "name": name
        })

# 4. Load from cronograma.html (activities)
cronograma_html_path = r"C:\Users\Lenovo\Documents\expo expositores\cronograma.html"
activities = []
if os.path.exists(cronograma_html_path):
    with open(cronograma_html_path, "r", encoding="utf-8") as f:
        content = f.read()
    titles = re.findall(r"class=\"timeline-title\">([^<]+)</h3>", content)
    descs = re.findall(r"class=\"timeline-desc\">([^<]+)</p>", content)
    for t, d in zip(titles, descs):
        activities.append({
            "source": "cronograma_html",
            "title": t.strip(),
            "desc": d.strip()
        })

# Save to raw json file
output = {
    "excel": excel_exhibitors,
    "logos": logo_images,
    "directory": directory_providers,
    "activities": activities
}

os.makedirs("scratch", exist_ok=True)
with open(r"scratch\roster_raw.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2, ensure_ascii=False)

print("roster_raw.json compiled successfully.")
