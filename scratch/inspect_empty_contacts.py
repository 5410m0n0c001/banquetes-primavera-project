import pandas as pd
excel_path = r"C:\Users\Lenovo\Documents\expo expositores\PLANTILLA_FINAL_CORREGIDA.xlsx"
xls = pd.ExcelFile(excel_path)

empty_contact_sheets = [
    'Andrea Lozano Beauty Salon',
    'calesa',
    'letras gigantes LG',
    'redes',
    'mia pasteleria',
    'Producciones DJ Classic',
    'coreografias y bailes david'
]

for target in empty_contact_sheets:
    # Find matching sheet
    sheet_name = None
    for s in xls.sheet_names:
        if target.lower() in s.lower():
            sheet_name = s
            break
            
    if sheet_name:
        print(f"\n==========================================")
        print(f"SHEET: {sheet_name}")
        df = pd.read_excel(excel_path, sheet_name=sheet_name)
        df_clean = df.dropna(how='all').dropna(axis=1, how='all')
        for r_idx, row in df_clean.iterrows():
            row_vals = [f"Col{c_idx}({col}): {val}" for c_idx, (col, val) in enumerate(row.items()) if pd.notna(val)]
            print(f"  Row {r_idx}: {', '.join(row_vals)}")
