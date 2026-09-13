import pandas as pd
excel_path = r"C:\Users\Lenovo\Documents\expo expositores\PLANTILLA_FINAL_CORREGIDA.xlsx"
xls = pd.ExcelFile(excel_path)
print("Sheet names in Excel:", xls.sheet_names)

for sheet in xls.sheet_names:
    print(f"\n==================================================")
    print(f"SHEET: {sheet}")
    df = pd.read_excel(excel_path, sheet_name=sheet)
    # Drop rows/columns that are completely empty
    df_clean = df.dropna(how='all').dropna(axis=1, how='all')
    for r_idx, row in df_clean.iterrows():
        row_vals = [f"{col}: {val}" for col, val in row.items() if pd.notna(val)]
        if row_vals:
            print(f"  Row {r_idx}: {', '.join(row_vals)}")
