from dask.distributed import Client
import time
import os

# Fungsi yang akan dijalankan oleh Dask Worker
def hitung_kuadrat(x):
    """Menghitung kuadrat dari x dan menunggu sebentar."""
    # Menunggu 1 detik untuk simulasi tugas berat
    time.sleep(1)
    # print(f"Menghitung {x}**2 pada proses: {os.getpid()}", flush=True)
    return x * x

if __name__ == '__main__':
    # 1. Sambungkan ke Dask Scheduler
    # PENTING: Menggunakan hostname internal Docker dan port internal 8786
    SCHEDULER_ADDRESS = "tcp://dask-scheduler:8786" # <-- PERUBAHAN INI PENTING!
    
    try:
        # Menghubungkan ke Dask Scheduler di dalam jaringan Docker
        client = Client(SCHEDULER_ADDRESS)
        print(f"✅ Berhasil tersambung ke Dask Cluster pada {SCHEDULER_ADDRESS}!")
        print(f"Info Cluster: {client}")
        
        # 2. Buat daftar input (10 tugas)
        data_input = list(range(10)) 
        
        start_time = time.time()
        
        # 3. Kirim tugas ke Cluster (komputasi terdistribusi)
        futures = client.map(hitung_kuadrat, data_input)
        
        print(f"\n🚀 Mengirim {len(futures)} tugas ke cluster...")

        # 4. Tunggu hasil dan ambil (Pull)
        results = client.gather(futures)
        
        end_time = time.time()
        
        # 5. Tampilkan hasil
        print("\n✨ Hasil komputasi terdistribusi:")
        print(results)
        
        # Bandingkan waktu eksekusi
        execution_time = end_time - start_time
        print(f"\n⏳ Total waktu eksekusi: {execution_time:.2f} detik")
        
        # 6. Tutup koneksi
        client.close()

    except ConnectionRefusedError:
        print(f"❌ GAGAL tersambung ke Dask Scheduler di {SCHEDULER_ADDRESS}. Pastikan Docker Compose sudah berjalan.")
    except Exception as e:
        print(f"Terjadi error: {e}")
