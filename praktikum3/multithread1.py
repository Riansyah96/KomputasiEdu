import threading
import time
import random

# 1. Definisikan fungsi (tugas) yang akan dijalankan oleh thread
def tugas_koki(nama_tugas, durasi_langkah):
    """
    Fungsi ini mensimulasikan pekerjaan yang memakan waktu.
    """
    print(f">>> {nama_tugas} dimulai.")
    
    # Simulasikan beberapa langkah kerja
    for i in range(1, 4):
        print(f"    {nama_tugas}: Langkah ke-{i}")
        # Jeda sejenak untuk mensimulasikan waktu tunggu (misalnya, I/O)
        time.sleep(durasi_langkah) 
        
    print(f"<<< {nama_tugas} selesai.")

# 2. Program Utama
if __name__ == "__main__":
    
    print("Program Utama dimulai. Chef mulai bekerja! 🧑‍🍳")
    
    # Mendefinisikan tugas dan argumennya
    # Tugas 1: Membuat Kopi (durasi langkah 0.5 detik)
    thread_kopi = threading.Thread(
        target=tugas_koki, 
        args=("Tugas Kopi ☕", 0.5)
    )
    
    # Tugas 2: Memanggang Roti (durasi langkah 1.0 detik, lebih lama)
    thread_roti = threading.Thread(
        target=tugas_koki, 
        args=("Tugas Roti 🍞", 1.0)
    )
    
    # Memulai eksekusi thread
    thread_kopi.start()
    thread_roti.start()
    
    # Perintah join() memastikan program utama menunggu kedua thread selesai
    # sebelum mencetak "Program Utama selesai."
    thread_kopi.join()
    thread_roti.join()
    
    print("Program Utama selesai. (Semua pesanan terkirim!)")