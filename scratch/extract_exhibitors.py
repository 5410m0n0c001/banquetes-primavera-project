import pandas as pd
import re

excel_path = r"C:\Users\Lenovo\Documents\expo expositores\PLANTILLA_FINAL_CORREGIDA.xlsx"
xls = pd.ExcelFile(excel_path)

exhibitors = []

for sheet in xls.sheet_names:
    df = pd.read_excel(excel_path, sheet_name=sheet)
    
    # We want to find:
    # 1. The profile header (usually row 4, Unnamed: 0: "PERFIL DEL EXPOSITOR: ...")
    # 2. The Titular (Contacto) (usually row 6, Unnamed: 1)
    
    profile_header = ""
    contact_name = ""
    
    # Let's search row by row
    for r_idx, row in df.iterrows():
        # Check first column for "PERFIL DEL EXPOSITOR"
        val0 = str(row.iloc[0]) if len(row) > 0 and pd.notna(row.iloc[0]) else ""
        if "PERFIL DEL EXPOSITOR" in val0.upper():
            profile_header = val0
            
        # Check first column for "Titular" or "Contacto"
        if "TITULAR" in val0.upper() or "CONTACTO" in val0.upper():
            if len(row) > 1 and pd.notna(row.iloc[1]):
                contact_name = str(row.iloc[1]).strip()
                
    # If contact_name is still empty, let's search if any column contains contact info
    if not contact_name:
        for r_idx, row in df.iterrows():
            for c_idx, val in enumerate(row):
                if pd.notna(val) and ("TITULAR" in str(val).upper() or "CONTACTO" in str(val).upper()):
                    if c_idx + 1 < len(row) and pd.notna(row.iloc[c_idx + 1]):
                        contact_name = str(row.iloc[c_idx + 1]).strip()
                        break
            if contact_name:
                break
                
    # Clean business name from profile header
    business_name = sheet
    if profile_header:
        # Match after "PERFIL DEL EXPOSITOR:"
        m = re.search(r"PERFIL DEL EXPOSITOR:\s*(.*)", profile_header, re.IGNORECASE)
        if m:
            business_name = m.group(1).strip()
            
    exhibitors.append({
        "sheet_name": sheet,
        "business_name": business_name,
        "contact_name": contact_name
    })

# Print the extracted data
print(f"Total sheets: {len(exhibitors)}")
for idx, ex in enumerate(exhibitors, 1):
    print(f"{idx}. Sheet: '{ex['sheet_name']}' | Business: '{ex['business_name']}' | Contact: '{ex['contact_name']}'")
