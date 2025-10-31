from mpi4py import MPI
import sys

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    
    # Pastikan ada tepat 4 proses
    if size != 4:
        if rank == 0:
            print("Error: Program ini membutuhkan tepat 4 proses!")
            print("Gunakan: mpiexec -n 4 python circular_message.py")
        return
    
    # Pesan yang akan dikirim
    message = f'Halo dari proses {rank}'
    
    # Tentukan proses sumber dan tujuan
    source = (rank - 1) % size  # proses yang mengirim ke saya
    dest = (rank + 1) % size    # proses yang saya kirimi
    
    print(f"Proses {rank} siap mengirim ke proses {dest} dan menerima dari proses {source}")
    
    # Strategi untuk menghindari deadlock:
    # Proses dengan rank genap mengirim dulu kemudian menerima
    # Proses dengan rank ganjil menerima dulu kemudian mengirim
    if rank % 2 == 0:
        # Rank genap (0, 2): kirim dulu → terima
        comm.send(message, dest=dest)
        received_message = comm.recv(source=source)
    else:
        # Rank ganjil (1, 3): terima dulu → kirim
        received_message = comm.recv(source=source)
        comm.send(message, dest=dest)
    
    # Output hasil
    print(f'Proses {rank} menerima pesan: \"{received_message}\" dari proses {source}')

if __name__ == "__main__":
    main()