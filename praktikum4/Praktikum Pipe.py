import multiprocessing
import time
import base64
import os

# --- Fungsi Proses Anak 1: Encoder ---
def encoder_process(input_pipe, output_pipe):
    """Menerima data dari input_pipe, melakukan encoding, dan mengirim ke output_pipe."""
    
    print(f"[{os.getpid()} P1_Encoder] Siap menerima data...")
    
    while True:
        try:
            # 1. Menerima data dari pipe input (dari Proses Utama)
            message = input_pipe.recv() 
            
            if message is None:
                print(f"[{os.getpid()} P1_Encoder] Menerima sinyal berhenti (None).")
                output_pipe.send(None) # Meneruskan sinyal berhenti ke proses berikutnya
                break

            # Simulasi beban kerja (CPU-bound ringan)
            time.sleep(0.05) 
            
            # Melakukan Encoding
            encoded_bytes = base64.b64encode(message.encode('utf-8'))
            encoded_message = encoded_bytes.decode('utf-8')
            
            print(f"[{os.getpid()} P1_Encoder] Encoded: {message} -> {encoded_message[:15]}...")
            
            # 2. Mengirim hasil encoding ke pipe output (ke Proses Anak 2)
            output_pipe.send(encoded_message)

        except EOFError:
            break # Pipe ditutup
        except Exception as e:
            print(f"Error di Encoder: {e}")
            break

# --- Fungsi Proses Anak 2: Decoder ---
def decoder_process(input_pipe):
    """Menerima data encoded dari input_pipe, melakukan decoding, dan mencetak hasilnya."""
    
    print(f"[{os.getpid()} P2_Decoder] Siap menerima data encoded...")
    
    while True:
        try:
            # 1. Menerima data dari pipe input (dari Proses Anak 1)
            encoded_message = input_pipe.recv() 
            
            if encoded_message is None:
                print(f"[{os.getpid()} P2_Decoder] Menerima sinyal berhenti (None). Selesai.")
                break

            # Simulasi beban kerja (CPU-bound ringan)
            time.sleep(0.1) 
            
            # Melakukan Decoding
            decoded_bytes = base64.b64decode(encoded_message)
            decoded_message = decoded_bytes.decode('utf-8')
            
            print(f"[{os.getpid()} P2_Decoder] Decoded: {encoded_message[:15]}... -> '{decoded_message}'")

        except EOFError:
            break
        except Exception as e:
            print(f"Error di Decoder: {e}")
            break

if __name__ == '__main__':
    print(f"[Main Process {os.getpid()}] Sistem Pipelining dimulai.")
    
    # 1. Membuat Pipe pertama (Main -> Encoder)
    parent_conn_1, child_conn_1 = multiprocessing.Pipe()
    
    # 2. Membuat Pipe kedua (Encoder -> Decoder)
    parent_conn_2, child_conn_2 = multiprocessing.Pipe()
    
    # Pesan yang akan diproses
    messages = ["Data Kuliah", "Studi Kasus Python", "Pipe Multiprocessing", "Selesai"]
    
    # --- Inisialisasi Proses ---
    
    # P1: Encoder (Input: child_conn_1, Output: parent_conn_2)
    p1 = multiprocessing.Process(target=encoder_process, args=(child_conn_1, parent_conn_2))
    
    # P2: Decoder (Input: child_conn_2)
    p2 = multiprocessing.Process(target=decoder_process, args=(child_conn_2,))
    
    # Mulai kedua proses
    p1.start()
    p2.start()
    
    # --- Mengirim Data dari Proses Utama ---
    
    time.sleep(1) # Beri waktu proses anak untuk memulai
    print("-" * 40)
    
    for msg in messages:
        print(f"[Main Process] Mengirim: '{msg}'")
        parent_conn_1.send(msg) # Mengirim melalui ujung 'parent' dari Pipe 1
        time.sleep(0.3)
        
    # Mengirim sinyal berhenti (sentinel) setelah semua pesan dikirim
    parent_conn_1.send(None)
    
    # Menunggu kedua proses anak selesai
    p1.join()
    p2.join()
    
    print("-" * 40)
    print(f"[Main Process {os.getpid()}] Semua pemrosesan selesai.")