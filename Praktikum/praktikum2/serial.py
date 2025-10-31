
import math
import time

def hitung_akar_kuadrat_serial(angka):
    """Fungsi untuk menghitung akar kuadrat dari sebuah angka."""
    return math.sqrt(angka)

if __name__ == '__main__':
    daftar_angka = list(range(1, 5000001))

    print("Memulai pemrosesan serial...")
    start_time = time.time()

    hasil_serial = []
    for angka in daftar_angka:
        hasil_serial.append(hitung_akar_kuadrat_serial(angka))

    end_time = time.time()
    durasi_serial = end_time - start_time
    print(f"Pemrosesan serial selesai dalam: {durasi_serial:.4f} detik")
    # print(f"Contoh hasil: {hasil_serial[:5]}...") # Opsional: uncomment untuk melihat hasilnya