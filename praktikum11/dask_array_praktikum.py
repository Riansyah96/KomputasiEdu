# dask_array_praktikum.py

import dask.array as da

print("--- Praktikum Dask Array ---")

# 1. Buat Dask Array berukuran 5000x5000
# Dask membagi array menjadi blok (chunks) 1000x1000 untuk pemrosesan paralel
N = 5000
chunks = (1000, 1000)
x = da.random.random((N, N), chunks=chunks)
print(f"Bentuk Dask Array (Shape): {x.shape}")
print(f"Ukuran Chunk Dask Array: {x.chunks}")

# 2. Lakukan operasi matriks (misalnya, x kuadrat dan hitung rata-rata)
# Operasi ini bersifat 'lazy'
x_squared_mean = (x ** 2).mean()
print(f"Tipe Hasil Operasi (Lazy): {type(x_squared_mean)}")

# 3. Eksekusi komputasi secara paralel
print("\nMemulai komputasi...")
hasil = x_squared_mean.compute()
print(f"Hasil Rata-rata (x^2): {hasil}")