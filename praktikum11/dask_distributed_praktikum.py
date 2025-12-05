# dask_distributed_praktikum_FIXED.py

from dask.distributed import Client
import dask.array as da
import time

def jalankan_praktikum():
    """Fungsi utama yang menjalankan Dask Client dan komputasi."""
    
    print("--- Praktikum Dask Distributed ---")

    # 1. Inisialisasi Client
    # Client akan meluncurkan Scheduler dan Worker lokal
    print("Meluncurkan Dask Client (Scheduler dan Worker lokal)...")
    # Mengurangi jumlah worker mungkin membantu jika resource terbatas
    client = Client(n_workers=2, threads_per_worker=1) 

    # 2. Tampilkan Tautan Dashboard
    print(f"Tautan Web Dashboard Dask: {client.dashboard_link}")
    print("Silakan buka tautan di browser untuk memantau aktivitas!")
    print("-" * 50)

    # 3. Buat dan Eksekusi Komputasi (Contoh Dask Array)
    N = 8000
    x = da.random.random((N, N), chunks=(1000, 1000))
    y = (x ** 2 + x).mean()

    print("\nMemulai komputasi pada Client, perhatikan Task Graph di Dashboard...")

    # Meminta hasil.
    future = client.compute(y) 
    
    # Tunggu hasilnya
    hasil = future.result()
    print(f"Hasil Rata-rata Komputasi: {hasil}")

    # 4. Tutup Client
    print("\nMenutup Dask Client...")
    client.close()

# BLOK PENGAMAN: Pastikan kode hanya berjalan ketika file dieksekusi sebagai program utama
if __name__ == '__main__':
    jalankan_praktikum()