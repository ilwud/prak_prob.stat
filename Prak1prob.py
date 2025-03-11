import pandas as pd

df = pd.read_clipboard()
print(df)

rata_tinggi = df['Tinggi Badan'].mean()
print(rata_tinggi)

print(df.dtypes)

df['Angkatan'] = df['Angkatan'].astype(str)

print(df.dtypes)
