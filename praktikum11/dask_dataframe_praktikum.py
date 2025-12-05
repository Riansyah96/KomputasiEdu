import dask.dataframe as dd
import pandas as pd
import os

print("--- Praktikum Dask DataFrame ---")

# 1. Buat file CSV simulasi data besar
data = {'id': range(10000), 'nilai': [i * 1.5 for i in range(10000)]}
pdf = pd.DataFrame(data)
pdf.to_csv('data_besar_simulasi.csv', index=False)
print("File 'data_besar_simulasi.csv' (10000 baris) berhasil dibuat.")

# 2. Baca file menggunakan Dask DataFrame
# Dask akan membaca file dalam partisi, tidak memuat semuanya ke RAM
ddf = dd.read_csv('data_besar_simulasi.csv', blocksize=5000) # Membaca dengan blok 5KB (simulasi partisi)
print(f"Jumlah Partisi Dask DataFrame: {ddf.npartitions}")

# 3. Lakukan operasi (Hitung rata-rata kolom 'nilai')
# Operasi ini bersifat 'lazy' (malas) [cite: 97]
mean_nilai_lazy = ddf['nilai'].mean()
print(f"Tipe Hasil Operasi (Lazy): {type(mean_nilai_lazy)}")

# 4. Eksekusi komputasi secara paralel
print("\nMemulai komputasi...")
hasil = mean_nilai_lazy.compute()
print(f"Hasil Rata-rata Kolom 'nilai': {hasil}")

# Bersihkan file simulasi
os.remove('data_besar_simulasi.csv')