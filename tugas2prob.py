import numpy as np
import pandas as pd
import mysql.connector

# Membuat koneksi ke MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="PS2[Adil]"
)

# Membuat objek cursor untuk mengeksekusi kueri
cursor = connection.cursor(dictionary=True)

try:
    # Mengeksekusi kueri SQL

    my_query = "SELECT * FROM nama_teman_sma_1;"
    cursor.execute(my_query)
    
    # Mengambil semua hasil kueri
    result = cursor.fetchall()
    
    # Menampilkan hasil kueri
    print("\nHasil Kueri:")
    for row in result:
        print(row)

finally:
    # Menutup kursor dan koneksi
    cursor.close()
    connection.close()
    
#mengonversi hasilkueri ke dataframe Pandas
df = pd.DataFrame(result)
#filter data berdasarkan kolom 'brick' yang bernilai 'NO'
df_filtered = df[
    (df['Gender'].str.lower() == 'l')
]
#menampilkan hasil filter
print("\nhasil filter :")
print(df_filtered)