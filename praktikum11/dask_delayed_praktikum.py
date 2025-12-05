# dask_delayed_praktikum.py

from dask import delayed
import time

print("--- Praktikum Dask Delayed ---")

# Fungsi Python biasa yang dibungkus delayed
# @delayed menandakan bahwa fungsi ini harus dimasukkan ke Task Graph
@delayed
def fungsi_tambah(x, y):
    time.sleep(0.5) # Simulasi pekerjaan yang memakan waktu
    print(f"Task Tambah: {x} + {y}")
    return x + y

@delayed
def fungsi_kali(x, y):
    time.sleep(1.0) # Simulasi pekerjaan yang lebih lama
    print(f"Task Kali: {x} * {y}")
    return x * y

# 1. Rangkai fungsi menjadi alur kerja (Task Graph): (2 * 3) + (4 * 5)
# Tidak ada eksekusi yang terjadi di sini, hanya pembangunan grafik
a = fungsi_kali(2, 3)
b = fungsi_kali(4, 5)
hasil_delayed = fungsi_tambah(a, b)

print(f"Objek yang dihasilkan: {type(hasil_delayed)}")
# 
print("Task Graph telah dibuat. Kunjungi Dashboard Dask untuk melihatnya (jika Distributed Client aktif).")

# 2. Eksekusi komputasi secara paralel
print("\nMemulai komputasi (membutuhkan waktu karena ada sleep)...")
# Dask akan mencoba menjalankan 'kali(2, 3)' dan 'kali(4, 5)' secara paralel
hasil = hasil_delayed.compute()
print(f"Hasil Akhir: {hasil}") # (6 + 20) = 26