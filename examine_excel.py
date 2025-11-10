import pandas as pd

# Read the Excel file
df = pd.read_excel('Spend.xlsx')

print("=== PETROL SPENDING DATA ANALYSIS ===")
print(f"Total records: {len(df)}")
print(f"Columns: {list(df.columns)}")
print("\n=== SAMPLE DATA ===")
print(df.head(10))
print("\n=== DATA TYPES ===")
print(df.dtypes)
print("\n=== MISSING VALUES ===")
print(df.isnull().sum())