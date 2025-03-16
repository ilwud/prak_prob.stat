import pandas as pd

df = pd.read_csv("D:/Kuliah/semester2/PRAKprobstat/H1/nama_teman(Sheet1).csv", sep = ';')
print(df)

df = pd.read_excel("D:/Kuliah/semester2/PRAKprobstat/H1/namateman.xlsx")  
print(df)

data_nama = pd.read_csv("D:/Kuliah/semester2/PRAKprobstat/H1/nama_teman(Sheet1).csv")
View(data_nama)
