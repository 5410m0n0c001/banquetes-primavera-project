import pandas as pd
excel_path = r"C:\Users\Lenovo\Downloads\CHECK LIST.xlsx"
try:
    xls = pd.ExcelFile(excel_path)
    print("Sheets in CHECK LIST.xlsx:", xls.sheet_names)
    for sheet in xls.sheet_names:
        df = pd.read_excel(excel_path, sheet_name=sheet)
        print(f"\n--- Sheet: {sheet} ---")
        print("Shape:", df.shape)
        print("Columns:", df.columns.tolist())
        print(df.head(10))
except Exception as e:
    print(f"Error: {e}")
