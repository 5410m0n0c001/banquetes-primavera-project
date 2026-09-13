import pandas as pd
excel_path = r"C:\Users\Lenovo\Documents\expo expositores\PLANTILLA_FINAL_CORREGIDA.xlsx"
xls = pd.ExcelFile(excel_path)
print("Sheet names:", xls.sheet_names)
for sheet in xls.sheet_names:
    print(f"\n--- Sheet: {sheet} ---")
    df = pd.read_excel(excel_path, sheet_name=sheet)
    print("Columns:", df.columns.tolist())
    print("Shape:", df.shape)
    print("Head:\n", df.head(3))
