import time
import threading
import requests
import sys

# Daftar URL yang akan diakses (mensimulasikan tugas I/O-Bound)
URLS = [
    'https://jsonplaceholder.typicode.com/posts/1',
    'https://jsonplaceholder.typicode.com/posts/2',
    'https://jsonplaceholder.typicode.com/posts/3',
    'https://jsonplaceholder.typicode.com/posts/4',
    'https://jsonplaceholder.typicode.com/posts/5',
    'https://jsonplaceholder.typicode.com/posts/6',
]

def fetch_url(url):
    """Fungsi pekerja: Mengambil data dari URL tertentu."""
    try:
        # Permintaan HTTP adalah operasi I/O yang memakan waktu tunggu
        response = requests.get(url, timeout=5) 
        # print(f"Sukses mengambil {url} - Status: {response.status_code}") # Opsional: untuk debug
        return len(response.text) # Mengembalikan panjang konten
    except Exception as e:
        print(f"Gagal mengambil {url}: {e}", file=sys.stderr)
        return 0

# --- Metode A: Eksekusi Serial (Tanpa Multithreading) ---

def run_serial():
    print("--- Memulai Eksekusi Serial ---")
    start_time = time.time()
    
    total_data_length = 0
    for url in URLS:
        length = fetch_url(url)
        total_data_length += length
        
    end_time = time.time()
    print(f"Total data yang diproses (Serial): {total_data_length} bytes")
    print(f"Waktu Eksekusi Serial: {end_time - start_time:.4f} detik")
    return end_time - start_time

# --- Metode B: Eksekusi dengan Multithreading ---

def run_multithreaded():
    print("\n--- Memulai Eksekusi Multithreading ---")
    start_time = time.time()
    
    threads = []
    # Menggunakan list untuk menyimpan hasil karena thread tidak mengembalikan nilai secara langsung
    results = [0] * len(URLS) 
    
    def thread_worker(index, url):
        """Fungsi pembungkus untuk menyimpan hasil ke daftar bersama."""
        results[index] = fetch_url(url)
        
    # 1. Membuat dan memulai thread
    for i, url in enumerate(URLS):
        # Setiap URL mendapat thread-nya sendiri
        t = threading.Thread(target=thread_worker, args=(i, url))
        threads.append(t)
        t.start()
        
    # 2. Menunggu semua thread selesai
    for t in threads:
        t.join() 
        
    end_time = time.time()
    total_data_length = sum(results)
    print(f"Total data yang diproses (Thread): {total_data_length} bytes")
    print(f"Waktu Eksekusi Multithreading: {end_time - start_time:.4f} detik")
    return end_time - start_time

# --- Eksekusi Utama dan Perbandingan ---

if __name__ == '__main__':
    # Pastikan library 'requests' sudah terinstal: pip install requests
    
    # Jalankan kedua metode
    serial_duration = run_serial()
    thread_duration = run_multithreaded()
    
    # Hasil Perbandingan
    print("\n--- Ringkasan Perbandingan ---")
    print(f"Waktu Serial:        {serial_duration:.4f} detik")
    print(f"Waktu Multithreading: {thread_duration:.4f} detik")
    
    if thread_duration > 0:
        print(f"Percepatan (Speedup): {serial_duration / thread_duration:.2f}x")
    else:
        print("Tidak dapat menghitung speedup.")