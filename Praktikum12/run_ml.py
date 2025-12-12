import time
from dask_ml.model_selection import train_test_split
from dask_ml.linear_model import LogisticRegression
from dask.distributed import Client, LocalCluster

import dask.array as da

# 1. Inisialisasi Klien Dask
client = None # <--- KOREKSI: Inisialisasi client
try:
    # KOREKSI: Gunakan nama service 'dask-scheduler' dan tingkatkan timeout
    client = Client("tcp://dask-scheduler:8786", timeout="60s") 
    print("✅ Berhasil tersambung ke Dask Cluster!")
    print(f"Info Cluster: {client}")
except Exception:
    print("⚠️ Gagal tersambung ke scheduler di tcp://dask-scheduler:8786. Pastikan Dask Scheduler berjalan.")
    
# --- PENGUKURAN WAKTU UNTUK PRE-PEMROSESAN DATA ---
start_time_data = time.time()

# 2. Pembuatan Data Dummy Skala Besar
X = da.random.random((1000000, 20), chunks=(10000, 20)) 
y = da.random.randint(0, 2, size=(1000000,), chunks=(10000,))
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

end_time_data = time.time()
data_time = end_time_data - start_time_data

print(f"\n⏰ Waktu untuk Pembuatan & Pembagian Data (Lazy): {data_time:.4f} detik")
print(f"Ukuran Data: {X.shape[0]} baris, {X.shape[1]} fitur")
print("-" * 50)

# --- PENGUKURAN WAKTU UNTUK PELATIHAN MODEL ---
model = LogisticRegression()

start_time_fit = time.time()

# 3. Pelatihan Model
print("⏳ Memulai pelatihan model...")
model.fit(X_train, y_train)

end_time_fit = time.time()
fit_time = end_time_fit - start_time_fit

print("✅ Pelatihan model selesai!")
print(f"⏰ Waktu Eksekusi Pelatihan Model (model.fit()): {fit_time:.4f} detik")
print("-" * 50)

# 4. Total Waktu
total_time = data_time + fit_time
print(f"⏱️ Total Waktu (Pre-proses Lazy + Pelatihan): {total_time:.4f} detik")

# 5. Tutup Klien Dask
if client: # <--- KOREKSI: Hanya tutup jika client berhasil dibuat
    client.close()
